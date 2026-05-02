#!/bin/zsh
# Daily /recap-jour runner — invoked by launchd ~/Library/LaunchAgents/com.timboussardon.recap-jour.plist
# Compiles substance of Claude Code conversations into raw/journal/YYYY-MM-DD.md
set -euo pipefail

export PATH="/Users/timothee/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Documents/seo-kb"
LOG_DIR="$VAULT/.claude/logs"
LOG_FILE="$LOG_DIR/recap-jour-$(date +%Y-%m-%d).log"

mkdir -p "$LOG_DIR"
cd "$VAULT"

{
  echo "=== /recap-jour run started at $(date -Iseconds) ==="
  /Users/timothee/.npm-global/bin/claude \
    -p "/recap-jour" \
    --permission-mode bypassPermissions
  EXIT_CODE=$?
  echo ""
  echo "=== /recap-jour run ended at $(date -Iseconds) — exit $EXIT_CODE ==="
} >> "$LOG_FILE" 2>&1
