"""Tests for check-platform-parity.py command discovery normalization."""

import importlib
import tempfile
from pathlib import Path

# Module filename uses hyphens — import dynamically
_mod = importlib.import_module("check-platform-parity")
CORE_COMMANDS = _mod.CORE_COMMANDS
discover_claude_code_commands = _mod.discover_claude_code_commands
discover_opencode_commands = _mod.discover_opencode_commands
discover_kiro_commands = _mod.discover_kiro_commands


def _make_commands_dir(base: Path, platform_path: str, filenames: list[str]) -> Path:
    """Create a platform commands directory with the given files."""
    commands_dir = base / platform_path
    commands_dir.mkdir(parents=True)
    for name in filenames:
        (commands_dir / name).write_text("# stub")
    return base


def test_claude_code_ignores_non_command_md_files():
    """A README.md or other non-command .md file should not be counted."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _make_commands_dir(
            root,
            "plugins/claude-code/commands",
            ["help.md", "diagnose.md", "README.md"],
        )
        result = discover_claude_code_commands(root)
        assert "README" not in result
        assert result == {"help", "diagnose"}


def test_claude_code_discovers_core_commands():
    """All core command files are discovered."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        filenames = [f"{cmd}.md" for cmd in CORE_COMMANDS]
        _make_commands_dir(root, "plugins/claude-code/commands", filenames)
        result = discover_claude_code_commands(root)
        assert result == CORE_COMMANDS


def test_opencode_not_affected_by_stray_files():
    """OpenCode already uses spell-* prefix so stray files are ignored."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _make_commands_dir(
            root,
            "plugins/opencode/commands",
            ["spell-help.md", "spell-diagnose.md", "README.md"],
        )
        result = discover_opencode_commands(root)
        assert "README" not in result
        assert result == {"help", "diagnose"}


def test_kiro_not_affected_by_stray_files():
    """Kiro already uses spell-* prefix so stray files are ignored."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _make_commands_dir(
            root,
            "plugins/kiro/prompts",
            ["spell-help.md", "spell-diagnose.md", "README.md"],
        )
        result = discover_kiro_commands(root)
        assert "README" not in result
        assert result == {"help", "diagnose"}
