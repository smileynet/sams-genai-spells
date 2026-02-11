#!/bin/bash
set -e

# Sync command templates to Claude Code, OpenCode, and Kiro destinations
# Usage: ./dev/sync-commands.sh

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATES_DIR="$REPO_DIR/core/templates/commands"
CLAUDE_DIR="$REPO_DIR/plugins/claude-code/commands"
OPENCODE_DIR="$REPO_DIR/plugins/opencode/commands"
KIRO_DIR="$REPO_DIR/plugins/kiro/prompts"

# Color output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

printf "${BLUE}Syncing command templates...${NC}\n"

for template in "$TEMPLATES_DIR"/*.md.template; do
    [ -f "$template" ] || continue
    name=$(basename "$template" .md.template)

    echo "  $name.md"

    # Claude Code version: `spell:` namespace, keep CC blocks, strip OpenCode/Kiro blocks
    sed 's/@NAMESPACE@/spell:/g' "$template" \
      | sed '/@IF_OPENCODE@/,/@ENDIF_OPENCODE@/d' \
      | sed '/@IF_KIRO@/,/@ENDIF_KIRO@/d' \
      | sed '/@IF_CLAUDECODE@/d; /@ENDIF_CLAUDECODE@/d' \
      > "$CLAUDE_DIR/${name}.md"

    # OpenCode version: `spell-` namespace, keep OpenCode blocks, strip Claude Code/Kiro blocks
    sed 's/@NAMESPACE@/spell-/g' "$template" \
      | sed '/@IF_CLAUDECODE@/,/@ENDIF_CLAUDECODE@/d' \
      | sed '/@IF_KIRO@/,/@ENDIF_KIRO@/d' \
      | sed '/@IF_OPENCODE@/d; /@ENDIF_OPENCODE@/d' \
      > "$OPENCODE_DIR/spell-${name}.md"

    # Kiro version: `@spell-` namespace, keep OpenCode+Kiro blocks, strip Claude Code blocks
    # Also strips YAML frontmatter (awk removes everything up to second --- delimiter)
    sed 's|/@NAMESPACE@|@spell-|g' "$template" \
      | sed 's/@NAMESPACE@/spell-/g' \
      | sed '/@IF_CLAUDECODE@/,/@ENDIF_CLAUDECODE@/d' \
      | sed '/@IF_OPENCODE@/d; /@ENDIF_OPENCODE@/d' \
      | sed '/@IF_KIRO@/d; /@ENDIF_KIRO@/d' \
      | awk 'BEGIN{c=0;p=0} /^---$/ && !p {c++; if(c==2) p=1; next} p{print}' \
      | sed '/./,$!d' \
      > "$KIRO_DIR/spell-${name}.md"
done

printf "${GREEN}✓ Commands synced${NC}\n"
