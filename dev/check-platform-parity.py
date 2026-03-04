#!/usr/bin/env python3
"""
check-platform-parity.py - Validate commands are consistent across
Claude Code, OpenCode, and Kiro platforms.

Usage:
    ./dev/check-platform-parity.py              # Human-readable report
    ./dev/check-platform-parity.py --json       # JSON output for CI
    ./dev/check-platform-parity.py --strict     # Exit 1 on warnings

Exit codes:
    0: All checks pass
    1: Errors found (missing required parity)
    2: Warnings found (with --strict)
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ParityResult:
    """Result of a parity check."""
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)


@dataclass
class PlatformAssets:
    """Assets discovered on a platform."""
    commands: set[str] = field(default_factory=set)


# Core commands that should exist on all platforms
CORE_COMMANDS = {
    "help", "idiomatic", "socratic", "bpap", "progressive-disclosure",
    "diataxis", "task-graph", "diagnose", "cause-map", "deep-dive",
    "prior-art", "blind-spot", "zoom-out", "handoff", "teach",
}


def discover_claude_code_commands(repo_root: Path) -> set[str]:
    """Discover commands from Claude Code plugin.

    Unlike OpenCode (spell-*.md) and Kiro (spell-*.md), Claude Code commands
    have no filename prefix. Filter against CORE_COMMANDS to avoid counting
    non-command .md files (e.g. README.md).
    """
    commands_dir = repo_root / "plugins" / "claude-code" / "commands"
    if not commands_dir.exists():
        return set()
    return {f.stem for f in commands_dir.glob("*.md") if f.stem in CORE_COMMANDS}


def discover_opencode_commands(repo_root: Path) -> set[str]:
    """Discover commands from OpenCode plugin."""
    commands_dir = repo_root / "plugins" / "opencode" / "commands"
    if not commands_dir.exists():
        return set()
    return {f.stem.replace("spell-", "") for f in commands_dir.glob("spell-*.md")}


def discover_kiro_commands(repo_root: Path) -> set[str]:
    """Discover commands from Kiro plugin."""
    prompts_dir = repo_root / "plugins" / "kiro" / "prompts"
    if not prompts_dir.exists():
        return set()
    return {f.stem.replace("spell-", "") for f in prompts_dir.glob("spell-*.md")}


def check_opencode_manifest(repo_root: Path, actual_commands: set[str]) -> ParityResult:
    """Check that OpenCode package.json commands array matches actual files."""
    result = ParityResult()

    package_path = repo_root / "plugins" / "opencode" / "package.json"
    if not package_path.exists():
        result.errors.append("OpenCode package.json not found")
        return result

    try:
        data = json.loads(package_path.read_text())
        manifest_commands = {
            cmd.replace("spell-", "")
            for cmd in data.get("opencode", {}).get("commands", [])
        }

        missing_from_manifest = actual_commands - manifest_commands
        extra_in_manifest = manifest_commands - actual_commands

        if missing_from_manifest:
            result.errors.append(
                f"OpenCode manifest missing commands that exist as files: {sorted(missing_from_manifest)}"
            )
        if extra_in_manifest:
            result.errors.append(
                f"OpenCode manifest lists commands without files: {sorted(extra_in_manifest)}"
            )

        if not missing_from_manifest and not extra_in_manifest:
            result.info.append("OpenCode manifest matches actual files")

    except (json.JSONDecodeError, KeyError) as e:
        result.errors.append(f"Error reading OpenCode package.json: {e}")

    return result


def check_command_parity(
    claude_code: set[str],
    opencode: set[str],
    kiro: set[str],
) -> ParityResult:
    """Check that commands are consistent across platforms."""
    result = ParityResult()

    # Check core commands on all platforms
    for cmd in CORE_COMMANDS:
        if cmd not in claude_code:
            result.errors.append(f"Claude Code missing core command: {cmd}")
        if cmd not in opencode:
            result.errors.append(f"OpenCode missing core command: {cmd}")
        if cmd not in kiro:
            result.errors.append(f"Kiro missing core command: {cmd}")

    # Check for unexpected commands (not in CORE_COMMANDS)
    platforms = {"Claude Code": claude_code, "OpenCode": opencode, "Kiro": kiro}
    for platform_name, commands in platforms.items():
        for cmd in commands - CORE_COMMANDS:
            result.info.append(f"{platform_name} has additional command: {cmd}")

    result.info.append(f"Claude Code commands: {sorted(claude_code)}")
    result.info.append(f"OpenCode commands: {sorted(opencode)}")
    result.info.append(f"Kiro commands: {sorted(kiro)}")

    return result


def format_human_report(
    command_result: Optional[ParityResult],
    manifest_result: Optional[ParityResult],
) -> str:
    """Format results as human-readable report."""
    lines = ["# Platform Parity Report", ""]

    total_errors = 0
    total_warnings = 0

    sections = [
        ("Commands", command_result),
        ("OpenCode Manifest", manifest_result),
    ]

    for section_name, result in sections:
        if result is None:
            continue

        lines.append(f"## {section_name}")
        lines.append("")

        if result.errors:
            lines.append("### Errors")
            for err in result.errors:
                lines.append(f"  - {err}")
            lines.append("")
            total_errors += len(result.errors)

        if result.warnings:
            lines.append("### Warnings")
            for warn in result.warnings:
                lines.append(f"  - {warn}")
            lines.append("")
            total_warnings += len(result.warnings)

        if result.info:
            lines.append("### Info")
            for msg in result.info:
                lines.append(f"  - {msg}")
            lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append(f"  Errors: {total_errors}")
    lines.append(f"  Warnings: {total_warnings}")

    if total_errors == 0 and total_warnings == 0:
        lines.append("")
        lines.append("  All checks passed!")

    return "\n".join(lines)


def format_json_report(
    command_result: Optional[ParityResult],
    manifest_result: Optional[ParityResult],
) -> str:
    """Format results as JSON."""
    report = {
        "commands": None,
        "manifest": None,
        "summary": {
            "errors": 0,
            "warnings": 0,
            "passed": True
        }
    }

    sections = [
        ("commands", command_result),
        ("manifest", manifest_result),
    ]

    for key, result in sections:
        if result:
            report[key] = {
                "errors": result.errors,
                "warnings": result.warnings,
                "info": result.info
            }
            report["summary"]["errors"] += len(result.errors)
            report["summary"]["warnings"] += len(result.warnings)

    report["summary"]["passed"] = report["summary"]["errors"] == 0

    return json.dumps(report, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Check platform parity across Claude Code, OpenCode, and Kiro"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output JSON instead of human-readable format"
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit with error code on warnings"
    )

    args = parser.parse_args()

    # Find repository root
    repo_root = Path(__file__).parent.parent

    # Discover commands from each platform
    claude_code_cmds = discover_claude_code_commands(repo_root)
    opencode_cmds = discover_opencode_commands(repo_root)
    kiro_cmds = discover_kiro_commands(repo_root)

    # Run checks
    command_result = check_command_parity(claude_code_cmds, opencode_cmds, kiro_cmds)
    manifest_result = check_opencode_manifest(repo_root, opencode_cmds)

    # Format output
    if args.json:
        print(format_json_report(command_result, manifest_result))
    else:
        print(format_human_report(command_result, manifest_result))

    # Determine exit code
    total_errors = len(command_result.errors) + len(manifest_result.errors)
    total_warnings = len(command_result.warnings) + len(manifest_result.warnings)

    if total_errors > 0:
        sys.exit(1)
    elif args.strict and total_warnings > 0:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
