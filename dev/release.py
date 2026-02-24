#!/usr/bin/env python3
"""
release.py - Automate mechanical steps of releasing a new sams-spells version.

Handles version sync, CHANGELOG transformation, and commit creation.
Preserves human judgment for content quality - the script only handles mechanics.

Usage:
    ./dev/release.py 0.6.0              # Prepare release (interactive)
    ./dev/release.py 0.6.0 --push       # Prepare + push (triggers GH release)
    ./dev/release.py 0.6.0 --dry-run    # Show what would change, no modifications
    ./dev/release.py --check            # Validate current state only

Exit codes:
    0: Success
    1: Pre-flight check failed
    2: Version update failed
    3: CHANGELOG update failed
    4: Commit failed
    5: Push failed
"""

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional


# ANSI colors for terminal output
class Colors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def color(text: str, color_code: str) -> str:
    """Wrap text in ANSI color codes."""
    return f"{color_code}{text}{Colors.ENDC}"


@dataclass
class PreflightResult:
    """Result of pre-flight checks."""
    passed: bool
    clean_tree: bool = True
    on_main: bool = True
    up_to_date: bool = True
    version_valid: bool = True
    changelog_ready: bool = True
    current_version: Optional[str] = None
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class ReleaseConfig:
    """Configuration for a release."""
    version: str
    dry_run: bool = False
    push: bool = False
    yes: bool = False
    repo_root: Path = field(default_factory=lambda: Path(__file__).parent.parent)
    previous_version: Optional[str] = None  # Set before updating versions


def run_git(args: list[str], capture: bool = True) -> tuple[int, str]:
    """Run a git command and return exit code and output."""
    result = subprocess.run(
        ["git"] + args,
        capture_output=capture,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    return result.returncode, result.stdout.strip() if capture else ""


def get_current_version(repo_root: Path) -> Optional[str]:
    """Get current version from plugin.json."""
    plugin_path = repo_root / "plugins" / "claude-code" / ".claude-plugin" / "plugin.json"
    if not plugin_path.exists():
        return None
    try:
        data = json.loads(plugin_path.read_text())
        return data.get("version")
    except json.JSONDecodeError:
        return None


def parse_version(version: str) -> tuple[int, ...]:
    """Parse semver string into tuple of ints for comparison."""
    return tuple(int(x) for x in version.split("."))


def version_is_newer(new_version: str, current_version: str) -> bool:
    """Check if new_version > current_version using semver comparison."""
    try:
        return parse_version(new_version) > parse_version(current_version)
    except (ValueError, AttributeError):
        return False


def git_working_tree_clean() -> bool:
    """Check if git working tree is clean."""
    code, output = run_git(["status", "--porcelain"])
    return code == 0 and output == ""


def on_main_branch() -> bool:
    """Check if on main branch."""
    code, output = run_git(["branch", "--show-current"])
    return code == 0 and output == "main"


def up_to_date_with_remote() -> bool:
    """Check if local main is up to date with origin/main."""
    # Fetch first
    run_git(["fetch", "origin", "main"], capture=False)

    # Compare HEAD with origin/main
    code, local = run_git(["rev-parse", "HEAD"])
    if code != 0:
        return False

    code, remote = run_git(["rev-parse", "origin/main"])
    if code != 0:
        return False

    return local == remote


def changelog_has_unreleased_content(repo_root: Path) -> bool:
    """Check if CHANGELOG has content in [Unreleased] section."""
    changelog_path = repo_root / "CHANGELOG.md"
    if not changelog_path.exists():
        return False

    content = changelog_path.read_text()

    # Find [Unreleased] section and check if it has content before next version
    unreleased_match = re.search(
        r"## \[Unreleased\]\s*\n(.*?)(?=## \[\d+\.\d+\.\d+\]|\Z)",
        content,
        re.DOTALL
    )

    if not unreleased_match:
        return False

    unreleased_content = unreleased_match.group(1).strip()
    return bool(unreleased_content)


def preflight_checks(config: ReleaseConfig) -> PreflightResult:
    """Run all pre-flight checks."""
    result = PreflightResult(passed=True)

    # Git state checks
    result.clean_tree = git_working_tree_clean()
    if not result.clean_tree:
        result.errors.append("Working tree not clean. Commit or stash changes.")
        result.passed = False

    result.on_main = on_main_branch()
    if not result.on_main:
        result.errors.append("Not on main branch.")
        result.passed = False

    result.up_to_date = up_to_date_with_remote()
    if not result.up_to_date:
        result.errors.append("Local main behind origin/main. Pull first.")
        result.passed = False

    # Version validation
    result.current_version = get_current_version(config.repo_root)
    if result.current_version is None:
        result.errors.append("Could not read current version from plugin.json")
        result.version_valid = False
        result.passed = False
    elif not version_is_newer(config.version, result.current_version):
        result.errors.append(f"Version {config.version} not newer than {result.current_version}")
        result.version_valid = False
        result.passed = False

    # Changelog check
    result.changelog_ready = changelog_has_unreleased_content(config.repo_root)
    if not result.changelog_ready:
        result.errors.append("CHANGELOG [Unreleased] section is empty")
        result.passed = False

    return result


def update_json_file(file_path: Path, updates: dict[str, str], dry_run: bool = False) -> bool:
    """Update version fields in a JSON file.

    Args:
        file_path: Path to JSON file
        updates: Dict mapping JSON path to new value (e.g., {"version": "0.6.0"})
        dry_run: If True, don't actually write changes

    Returns:
        True if successful
    """
    try:
        data = json.loads(file_path.read_text())

        for path, value in updates.items():
            keys = path.split(".")
            obj = data
            for key in keys[:-1]:
                obj = obj[key]
            obj[keys[-1]] = value

        if not dry_run:
            # Preserve formatting with 2-space indent
            file_path.write_text(json.dumps(data, indent=2) + "\n")

        return True
    except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
        print(f"  {color('✗', Colors.RED)} Error updating {file_path}: {e}")
        return False


def update_versions(config: ReleaseConfig) -> bool:
    """Update version in all required files."""
    success = True

    # Update plugin.json (1 field)
    plugin_path = config.repo_root / "plugins" / "claude-code" / ".claude-plugin" / "plugin.json"
    if update_json_file(plugin_path, {"version": config.version}, config.dry_run):
        print(f"  {color('✓', Colors.GREEN)} plugins/claude-code/.claude-plugin/plugin.json")
    else:
        success = False

    # Update package.json (2 fields: top-level version + opencode.version)
    package_path = config.repo_root / "plugins" / "opencode" / "package.json"
    if update_json_file(package_path, {
        "version": config.version,
        "opencode.version": config.version
    }, config.dry_run):
        print(f"  {color('✓', Colors.GREEN)} plugins/opencode/package.json (2 locations)")
    else:
        success = False

    return success


def update_changelog(config: ReleaseConfig) -> bool:
    """Update CHANGELOG.md with new version section."""
    changelog_path = config.repo_root / "CHANGELOG.md"

    try:
        content = changelog_path.read_text()
        today = date.today().isoformat()

        # Replace [Unreleased] content with new version section
        pattern = r"(## \[Unreleased\])\s*\n"
        replacement = f"## [Unreleased]\n\n## [{config.version}] - {today}\n"

        new_content = re.sub(pattern, replacement, content, count=1)

        if new_content == content:
            print(f"  {color('✗', Colors.RED)} Could not find [Unreleased] section")
            return False

        # Update comparison links at bottom
        previous = config.previous_version
        links_ok = True

        # Update existing [Unreleased] link
        unreleased_link_pattern = r"\[Unreleased\]: (https://github\.com/[^/]+/[^/]+)/compare/v[\d.]+\.\.\.HEAD"
        unreleased_link_replacement = f"[Unreleased]: \\1/compare/v{config.version}...HEAD"
        updated_content = re.sub(unreleased_link_pattern, unreleased_link_replacement, new_content)
        if updated_content == new_content:
            print(f"  {color('⚠', Colors.YELLOW)} Could not update [Unreleased] comparison link (format mismatch)")
            links_ok = False
        new_content = updated_content

        # Extract repo URL from [Unreleased] link (avoids hardcoding)
        repo_url_match = re.search(r"\[Unreleased\]: (https://github\.com/[^/]+/[^/]+)/compare/", new_content)
        if repo_url_match:
            repo_url = repo_url_match.group(1)
        else:
            # Fallback: derive from git remote
            _, remote_url = run_git(["remote", "get-url", "origin"])
            repo_url = re.sub(r'\.git$', '', remote_url.replace("git@github.com:", "https://github.com/"))

        # Add new version link after [Unreleased] link
        new_version_link = f"[{config.version}]: {repo_url}/compare/v{previous}...v{config.version}"

        # Insert after [Unreleased] link line
        updated_content = re.sub(
            r"(\[Unreleased\]: https://github\.com/[^\n]+\n)",
            f"\\1{new_version_link}\n",
            new_content
        )
        if updated_content == new_content:
            print(f"  {color('⚠', Colors.YELLOW)} Could not insert version comparison link")
            links_ok = False
        new_content = updated_content

        if not config.dry_run:
            changelog_path.write_text(new_content)

        print(f"  {color('✓', Colors.GREEN)} Converted [Unreleased] → [{config.version}] - {today}")
        print(f"  {color('✓', Colors.GREEN)} Added new [Unreleased] section")
        if links_ok:
            print(f"  {color('✓', Colors.GREEN)} Updated comparison links")
        else:
            print(f"  {color('⚠', Colors.YELLOW)} Comparison links may need manual review")

        return True

    except FileNotFoundError:
        print(f"  {color('✗', Colors.RED)} CHANGELOG.md not found")
        return False
    except Exception as e:
        print(f"  {color('✗', Colors.RED)} Error updating CHANGELOG: {e}")
        return False


def create_commit(config: ReleaseConfig) -> bool:
    """Create release commit."""
    if config.dry_run:
        print(f"  {color('○', Colors.BLUE)} Would create commit: \"chore(release): v{config.version}\"")
        return True

    # Stage changes — only the 3 files we modify
    files_to_stage = [
        "plugins/claude-code/.claude-plugin/plugin.json",
        "plugins/opencode/package.json",
        "CHANGELOG.md",
    ]

    for file in files_to_stage:
        code, _ = run_git(["add", file])
        if code != 0:
            print(f"  {color('✗', Colors.RED)} Failed to stage {file}")
            return False

    # Create commit
    commit_message = f"chore(release): v{config.version}"
    code, output = run_git(["commit", "-m", commit_message])

    if code != 0:
        print(f"  {color('✗', Colors.RED)} Failed to create commit")
        return False

    # Get commit hash
    code, commit_hash = run_git(["rev-parse", "--short", "HEAD"])

    print(f"  {color('✓', Colors.GREEN)} Created: {commit_hash} \"{commit_message}\"")
    return True


def push_to_remote(config: ReleaseConfig) -> bool:
    """Push to remote to trigger GitHub release workflow."""
    if config.dry_run:
        print(f"  {color('○', Colors.BLUE)} Would push to origin/main")
        return True

    code, _ = run_git(["push", "origin", "main"])

    if code != 0:
        print(f"  {color('✗', Colors.RED)} Failed to push to remote")
        return False

    print(f"  {color('✓', Colors.GREEN)} Pushed to origin/main")
    return True


def print_header(version: str, dry_run: bool = False):
    """Print release header."""
    mode = " (DRY RUN)" if dry_run else ""
    title = f"RELEASE: sams-spells v{version}{mode}"
    width = max(len(title) + 6, 64)
    print()
    print(color("╔" + "═" * (width - 2) + "╗", Colors.BOLD))
    print(color(f"║  {title:<{width - 4}}║", Colors.BOLD))
    print(color("╚" + "═" * (width - 2) + "╝", Colors.BOLD))
    print()


def print_checklist():
    """Print pre-release checklist reminder."""
    print()
    print(color("Before releasing, verify:", Colors.YELLOW))
    print("  [ ] All notable changes documented")
    print("  [ ] Changes categorized correctly")
    print("  [ ] User-friendly language used")
    print("  [ ] Breaking changes highlighted (if any)")
    print()


def confirm_release(config: ReleaseConfig) -> bool:
    """Ask for confirmation before proceeding."""
    if config.yes or config.dry_run:
        return True

    try:
        response = input(f"Proceed with release v{config.version}? [y/N] ")
        return response.lower() in ("y", "yes")
    except (EOFError, KeyboardInterrupt):
        print()
        return False


def run_check_only(repo_root: Path) -> int:
    """Run validation checks only, without making changes."""
    print()
    print(color("Checking release readiness...", Colors.BOLD))
    print()

    errors = []

    # Check git state
    print("Git state:")
    if git_working_tree_clean():
        print(f"  {color('✓', Colors.GREEN)} Working tree clean")
    else:
        print(f"  {color('✗', Colors.RED)} Working tree not clean")
        errors.append("Working tree not clean")

    if on_main_branch():
        print(f"  {color('✓', Colors.GREEN)} On main branch")
    else:
        print(f"  {color('✗', Colors.RED)} Not on main branch")
        errors.append("Not on main branch")

    if up_to_date_with_remote():
        print(f"  {color('✓', Colors.GREEN)} Up to date with origin/main")
    else:
        print(f"  {color('✗', Colors.RED)} Behind origin/main")
        errors.append("Behind origin/main")

    # Check versions
    print()
    print("Versions:")
    current = get_current_version(repo_root)
    if current:
        print(f"  Current version: {current}")
    else:
        print(f"  {color('✗', Colors.RED)} Could not read version")
        errors.append("Could not read version")

    # Check changelog
    print()
    print("Changelog:")
    if changelog_has_unreleased_content(repo_root):
        print(f"  {color('✓', Colors.GREEN)} [Unreleased] section has content")
    else:
        print(f"  {color('✗', Colors.RED)} [Unreleased] section is empty")
        errors.append("[Unreleased] section is empty")

    # Summary
    print()
    if errors:
        print(color(f"✗ {len(errors)} error(s) found", Colors.RED))
        for err in errors:
            print(f"  - {err}")
        return 1

    print(color("✓ Ready to release", Colors.GREEN))
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Automate mechanical steps of releasing a new sams-spells version"
    )
    parser.add_argument(
        "version",
        nargs="?",
        help="Version to release (e.g., 0.6.0)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without making modifications"
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push to remote after commit (triggers GitHub release)"
    )
    parser.add_argument(
        "--yes", "-y",
        action="store_true",
        help="Skip confirmation prompt"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate current state only, don't release"
    )

    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent

    # Check-only mode
    if args.check:
        return run_check_only(repo_root)

    # Version required for release
    if not args.version:
        parser.error("version is required (or use --check for validation only)")

    # Validate version format
    if not re.match(r"^\d+\.\d+\.\d+$", args.version):
        print(color(f"Error: Invalid version format '{args.version}'. Use X.Y.Z", Colors.RED))
        return 1

    config = ReleaseConfig(
        version=args.version,
        dry_run=args.dry_run,
        push=args.push,
        yes=args.yes,
        repo_root=repo_root
    )

    # Print header
    print_header(config.version, config.dry_run)

    # Pre-flight checks
    print("Pre-flight checks:")
    preflight = preflight_checks(config)

    if preflight.clean_tree:
        print(f"  {color('✓', Colors.GREEN)} Working tree clean")
    else:
        print(f"  {color('✗', Colors.RED)} Working tree not clean")

    if preflight.on_main:
        print(f"  {color('✓', Colors.GREEN)} On main branch")
    else:
        print(f"  {color('✗', Colors.RED)} Not on main branch")

    if preflight.up_to_date:
        print(f"  {color('✓', Colors.GREEN)} Up to date with origin")
    else:
        print(f"  {color('✗', Colors.RED)} Behind origin/main")

    if preflight.version_valid:
        print(f"  {color('✓', Colors.GREEN)} Version {config.version} > {preflight.current_version}")
    else:
        print(f"  {color('✗', Colors.RED)} Version {config.version} not newer than {preflight.current_version}")

    if preflight.changelog_ready:
        print(f"  {color('✓', Colors.GREEN)} CHANGELOG has unreleased content")
    else:
        print(f"  {color('✗', Colors.RED)} CHANGELOG [Unreleased] is empty")

    if not preflight.passed:
        print()
        print(color("Pre-flight checks failed. Fix errors before releasing.", Colors.RED))
        return 1

    # Show checklist and confirm
    print_checklist()

    if not confirm_release(config):
        print("Release cancelled.")
        return 0

    # Capture current version before updating (for changelog links)
    config.previous_version = preflight.current_version

    def rollback(exit_code: int) -> int:
        """Rollback file changes and return the provided exit code."""
        if config.dry_run:
            return exit_code
        print(f"  {color('↩', Colors.YELLOW)} Rolling back file changes...")
        code, _ = run_git(["checkout", "--", "."])
        if code == 0:
            print(f"  {color('✓', Colors.GREEN)} Rolled back to clean state")
        else:
            print(f"  {color('⚠', Colors.YELLOW)} Rollback failed — run: git checkout -- .")
        return exit_code

    # Update versions
    print()
    print("Updating versions:")
    if not update_versions(config):
        print(color("Version update failed.", Colors.RED))
        return rollback(2)

    # Update changelog
    print()
    print("Updating CHANGELOG:")
    if not update_changelog(config):
        print(color("CHANGELOG update failed.", Colors.RED))
        return rollback(3)

    # Create commit
    print()
    print("Commit:")
    if not create_commit(config):
        print(color("Commit failed.", Colors.RED))
        print(f"  {color('hint', Colors.YELLOW)} Files were modified. Run: git checkout HEAD -- .")
        return 4

    # Push if requested
    if config.push:
        print()
        print("Push:")
        if not push_to_remote(config):
            print(color("Push failed.", Colors.RED))
            return 5

    # Success summary
    print()
    print(color("━" * 64, Colors.BOLD))
    print()

    if config.dry_run:
        print(color("DRY RUN COMPLETE", Colors.BLUE))
        print("No changes were made. Run without --dry-run to execute.")
    elif config.push:
        print(color(f"✓ Release v{config.version} complete and pushed!", Colors.GREEN))
        print("GitHub release workflow should be triggered.")
    else:
        print(color(f"✓ Release v{config.version} committed!", Colors.GREEN))
        print()
        print(color("NEXT STEP:", Colors.YELLOW), "git push (will trigger GitHub release workflow)")
        print()
        print(f"Or run: ./dev/release.py {config.version} --push")

    return 0


if __name__ == "__main__":
    sys.exit(main())
