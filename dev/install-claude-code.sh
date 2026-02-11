#!/bin/bash
# Install/update sams-spells plugin for Claude Code
#
# This creates a LOCAL installation. To update, re-run this script.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
MARKETPLACE_DIR="$HOME/.claude/plugins/marketplaces/sams-spells-marketplace"

# Get version from plugin.json
VERSION=$(grep '"version"' "$REPO_DIR/plugins/claude-code/.claude-plugin/plugin.json" | head -1 | sed 's/.*: *"\([^"]*\)".*/\1/')

echo "Installing sams-spells plugin v$VERSION for Claude Code (local)..."

# Create marketplace structure if needed
mkdir -p "$MARKETPLACE_DIR/.claude-plugin"
mkdir -p "$MARKETPLACE_DIR/spell/.claude-plugin"
mkdir -p "$MARKETPLACE_DIR/spell/commands"

# Copy marketplace manifest with dynamic version
cat > "$MARKETPLACE_DIR/.claude-plugin/marketplace.json" << EOF
{
  "name": "sams-spells-marketplace",
  "owner": { "name": "smileynet" },
  "metadata": {
    "description": "Prompt engineering techniques packaged as reusable AI commands",
    "version": "$VERSION",
    "install_type": "local",
    "source_path": "$REPO_DIR"
  },
  "plugins": [
    {
      "name": "spell",
      "source": "./spell",
      "description": "Prompt engineering spells - idiomatic, socratic, best-practices, progressive-disclosure, diataxis",
      "version": "$VERSION"
    }
  ]
}
EOF

# Copy plugin manifest
cp "$REPO_DIR/plugins/claude-code/.claude-plugin/plugin.json" "$MARKETPLACE_DIR/spell/.claude-plugin/"

# Clear old commands and copy fresh
rm -f "$MARKETPLACE_DIR/spell/commands/"*.md
cp "$REPO_DIR/plugins/claude-code/commands/"*.md "$MARKETPLACE_DIR/spell/commands/"

# List installed commands
echo ""
echo "Installed commands:"
for f in "$MARKETPLACE_DIR/spell/commands/"*.md; do
  name=$(basename "$f" .md)
  echo "  /spell:$name"
done

echo ""
echo "Installation complete! (LOCAL) - v$VERSION"
echo ""
echo "IMPORTANT: Start a new Claude Code session (/clear) for changes to take effect."
echo ""
echo "To update this local installation:"
echo "  cd $REPO_DIR && ./dev/sync-commands.sh && ./dev/install-claude-code.sh"
