#!/bin/zsh
# Daily /recap-jour runner — invoked by launchd ~/Library/LaunchAgents/com.timboussardon.recap-jour.plist
# Compiles substance of Claude Code conversations into raw/journal/YYYY-MM-DD.md
set -euo pipefail

export PATH="/Users/timothee/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Code/seo-kb"
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
  echo "--- auto-commit raw/journal/ ---"
  git add raw/journal/ 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "No journal changes to commit."
  else
    git -c user.email="noreply@anthropic.com" -c user.name="recap-jour-cron" \
      commit -m "Journal $(date +%Y-%m-%d) (auto)"
    if git push origin main; then
      echo "Pushed."
    else
      echo "WARN: git push failed. Commit kept locally for next run."
    fi
  fi
  echo "=== /recap-jour run ended at $(date -Iseconds) — exit $EXIT_CODE ==="
} >> "$LOG_FILE" 2>&1
