#!/usr/bin/env python3
"""Install Sam's Spells for Kiro CLI.

Usage:
    ./install.py [--global | --local]
    ./install.py --version

Options:
    --global   Install to ~/.kiro/ (default)
    --local    Install to .kiro/ in current directory
    --version  Print version and exit
"""

import argparse
import shutil
import sys
from pathlib import Path

VERSION = "0.8.1"


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Sam's Spells for Kiro CLI")
    parser.add_argument(
        "--version",
        action="version",
        version=f"sams-spells v{VERSION} (Kiro)",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--global",
        dest="global_install",
        action="store_true",
        default=True,
        help="Install to ~/.kiro/ (default)",
    )
    group.add_argument(
        "--local",
        dest="global_install",
        action="store_false",
        help="Install to .kiro/ in current directory",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent.resolve()

    if args.global_install:
        kiro_dir = Path.home() / ".kiro"
        print(f"Installing Sam's Spells v{VERSION} for Kiro CLI (global)...")
        # Warn if local .kiro/ would shadow global install
        local_kiro = Path.cwd() / ".kiro"
        if local_kiro.is_dir():
            print()
            print(f"  Warning: Local .kiro/ directory detected at {local_kiro}")
            print("     Local installations take precedence over global. Consider:")
            print(f"     - Remove local: rm -rf {local_kiro}")
            print("     - Or re-run with --local")
            print()
    else:
        kiro_dir = Path.cwd() / ".kiro"
        print(f"Installing Sam's Spells v{VERSION} for Kiro CLI (local)...")

    # Create directories
    (kiro_dir / "prompts").mkdir(parents=True, exist_ok=True)

    # Copy prompts
    prompts_src = script_dir / "prompts"
    if not prompts_src.exists():
        sys.exit(f"Error: prompts directory not found at {prompts_src}")

    prompt_files = sorted(prompts_src.glob("*.md"))
    if not prompt_files:
        sys.exit(f"Error: No prompt files found in {prompts_src}")

    print(f"Installing prompts ({len(prompt_files)} commands)...")
    for prompt_file in prompt_files:
        shutil.copy(prompt_file, kiro_dir / "prompts" / prompt_file.name)

    print()
    print("Installation complete!")
    print()
    print(f"Installed to: {kiro_dir}")
    print()
    print("Files installed:")
    for prompt_file in prompt_files:
        print(f"  prompts/{prompt_file.name}")
    print()
    print("Available @prompts:")
    for prompt_file in prompt_files:
        name = prompt_file.stem
        print(f"  @{name}")


if __name__ == "__main__":
    main()
