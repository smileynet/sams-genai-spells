#!/bin/bash
# Install/update sams-spells plugin for Claude Code (LOCAL)
#
# This creates a LOCAL installation. To update, re-run this script.
# For remote installation (auto-updates via GitHub), use:
#   /plugin marketplace add smileynet/sams-genai-spells
#   /plugin install spell@sams-genai-spells

set -e

if ! command -v claude &>/dev/null; then
  printf "Error: 'claude' CLI not found. Install Claude Code first.\n" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
MARKETPLACE_DIR="$HOME/.claude/plugins/marketplaces/sams-spells-marketplace"

# Get version from plugin.json
VERSION=$(grep '"version"' "$REPO_DIR/plugins/claude-code/.claude-plugin/plugin.json" | head -1 | sed 's/.*: *"\([^"]*\)".*/\1/')

printf "Installing sams-spells plugin v%s for Claude Code...\n\n" "$VERSION"

# Step 1: Create marketplace directory structure
mkdir -p "$MARKETPLACE_DIR/.claude-plugin" \
         "$MARKETPLACE_DIR/spell/.claude-plugin" \
         "$MARKETPLACE_DIR/spell/commands" \
         "$MARKETPLACE_DIR/spell/rituals"

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
      "description": "Sam's Spells - idiomatic, socratic, bpap, progressive-disclosure, diataxis, task-graph, diagnose, cause-map, deep-dive, prior-art, blind-spot, zoom-out, handoff, ritual",
      "version": "$VERSION"
    }
  ]
}
EOF

# Copy plugin manifest and commands from repo
cp "$REPO_DIR/plugins/claude-code/.claude-plugin/plugin.json" "$MARKETPLACE_DIR/spell/.claude-plugin/"
rm -f "$MARKETPLACE_DIR/spell/commands/"*.md
cp "$REPO_DIR/plugins/claude-code/commands/"*.md "$MARKETPLACE_DIR/spell/commands/"

# Copy ritual definitions
rm -f "$MARKETPLACE_DIR/spell/rituals/"*.md
cp "$REPO_DIR/core/rituals/"*.md "$MARKETPLACE_DIR/spell/rituals/"

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

printf "\nInstallation complete! (LOCAL) v%s\n" "$VERSION"
printf "IMPORTANT: Start a new Claude Code session (/clear) for changes to take effect.\n"
printf "           Claude Code caches commands per version — new commands require version bump.\n"
printf "\nTo update this local installation:\n"
printf "  cd %s && git pull && ./dev/sync-commands.sh && ./dev/install-claude-code.sh\n" "$REPO_DIR"
printf "\nFor remote installation (auto-updates):\n"
printf "  /plugin uninstall spell\n"
printf "  /plugin marketplace add smileynet/sams-genai-spells\n"
printf "  /plugin install spell@sams-genai-spells\n"
