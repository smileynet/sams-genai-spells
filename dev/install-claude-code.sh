#!/bin/bash
# Install/update sams-spells plugin for Claude Code
#
# Uses the official Claude Code CLI to register the marketplace and install
# the plugin. To update, re-run this script.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
MARKETPLACE_DIR="$HOME/.claude/plugins/marketplaces/sams-spells-marketplace"

# Get version from plugin.json
VERSION=$(grep '"version"' "$REPO_DIR/plugins/claude-code/.claude-plugin/plugin.json" | head -1 | sed 's/.*: *"\([^"]*\)".*/\1/')

printf "Installing sams-spells plugin v%s for Claude Code...\n\n" "$VERSION"

# Step 1: Create marketplace directory structure
mkdir -p "$MARKETPLACE_DIR/.claude-plugin"
mkdir -p "$MARKETPLACE_DIR/spell/.claude-plugin"
mkdir -p "$MARKETPLACE_DIR/spell/commands"

# Write marketplace manifest
cat > "$MARKETPLACE_DIR/.claude-plugin/marketplace.json" << EOF
{
  "name": "sams-spells-marketplace",
  "owner": { "name": "smileynet" },
  "metadata": {
    "description": "Real-world concepts from programming, education, and design — packaged as AI commands",
    "version": "$VERSION",
    "install_type": "local",
    "source_path": "$REPO_DIR"
  },
  "plugins": [
    {
      "name": "spell",
      "source": "./spell",
      "description": "Sam's Spells - idiomatic, socratic, bpap, progressive-disclosure, diataxis, task-graph, debug, deep-dive",
      "version": "$VERSION"
    }
  ]
}
EOF

# Copy plugin manifest and commands from repo
cp "$REPO_DIR/plugins/claude-code/.claude-plugin/plugin.json" "$MARKETPLACE_DIR/spell/.claude-plugin/"
rm -f "$MARKETPLACE_DIR/spell/commands/"*.md
cp "$REPO_DIR/plugins/claude-code/commands/"*.md "$MARKETPLACE_DIR/spell/commands/"

# Step 2: Register marketplace via CLI (idempotent — re-adding updates it)
printf "Registering marketplace...\n"
claude plugin marketplace add "$MARKETPLACE_DIR"

# Step 3: Install plugin via CLI (handles cache + installed_plugins.json)
printf "Installing plugin...\n"
claude plugin install spell@sams-spells-marketplace --scope user

# Verify
printf "\nInstalled commands:\n"
for f in "$MARKETPLACE_DIR/spell/commands/"*.md; do
  printf "  /spell:%s\n" "$(basename "$f" .md)"
done

printf "\nInstallation complete! v%s\n" "$VERSION"
printf "Start a new Claude Code session (/clear) for changes to take effect.\n"
printf "\nTo update:\n"
printf "  cd %s && ./dev/sync-commands.sh && ./dev/install-claude-code.sh\n" "$REPO_DIR"
