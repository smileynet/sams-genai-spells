"""Tests for check-plugin-health.py marketplace.json validation."""

import importlib
import json
import tempfile
from pathlib import Path

# Module filename uses hyphens — import dynamically
_mod = importlib.import_module("check-plugin-health")
check_marketplace = _mod.check_marketplace


def _make_marketplace(root: Path, data: dict) -> None:
    """Write a marketplace.json file under .claude-plugin/."""
    mp_dir = root / ".claude-plugin"
    mp_dir.mkdir(parents=True, exist_ok=True)
    (mp_dir / "marketplace.json").write_text(json.dumps(data, indent=2))


def test_valid_marketplace():
    """A well-formed marketplace.json with plugins[0].name == 'spell' passes."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _make_marketplace(root, {
            "name": "sams-genai-spells",
            "plugins": [{"name": "spell", "source": "./plugins/claude-code/"}],
        })
        result = check_marketplace(root)
        assert result.errors == []
        assert result.warnings == []


def test_missing_marketplace():
    """Missing marketplace.json is an error."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        result = check_marketplace(root)
        assert len(result.errors) == 1
        msg = result.errors[0].lower()
        assert "not found" in msg or "missing" in msg, f"Expected 'not found' or 'missing' in: {result.errors[0]}"


def test_invalid_json():
    """Unparseable marketplace.json is an error."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        mp_dir = root / ".claude-plugin"
        mp_dir.mkdir(parents=True)
        (mp_dir / "marketplace.json").write_text("{bad json")
        result = check_marketplace(root)
        assert len(result.errors) == 1
        msg = result.errors[0].lower()
        assert "json" in msg or "parse" in msg, f"Expected 'json' or 'parse' in: {result.errors[0]}"


def test_wrong_plugin_name():
    """plugins[0].name != 'spell' is an error."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _make_marketplace(root, {
            "name": "sams-genai-spells",
            "plugins": [{"name": "wrong-name", "source": "./plugins/claude-code/"}],
        })
        result = check_marketplace(root)
        assert len(result.errors) == 1
        assert "spell" in result.errors[0].lower()


def test_empty_plugins_array():
    """Empty plugins array is an error."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _make_marketplace(root, {"name": "sams-genai-spells", "plugins": []})
        result = check_marketplace(root)
        assert len(result.errors) == 1
        assert "plugin" in result.errors[0].lower(), f"Expected 'plugin' in: {result.errors[0]}"


def test_missing_plugins_key():
    """Missing 'plugins' key is an error."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _make_marketplace(root, {"name": "sams-genai-spells"})
        result = check_marketplace(root)
        assert len(result.errors) == 1
        assert "plugin" in result.errors[0].lower(), f"Expected 'plugin' in: {result.errors[0]}"
