#!/bin/zsh
# Daily revue-presse runner — invoked by launchd ~/Library/LaunchAgents/com.timboussardon.revue-presse.plist
# Generates raw/revue-de-presse/YYYY-MM-DD-revue-presse.md via the revue-presse-quotidienne skill
set -euo pipefail

export PATH="/Users/timothee/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Code/seo-kb"
LOG_DIR="$VAULT/.claude/logs"
LOG_FILE="$LOG_DIR/revue-presse-$(date +%Y-%m-%d).log"
TODAY="$(date +%Y-%m-%d)"
TARGET="$VAULT/raw/revue-de-presse/${TODAY}-revue-presse.md"

mkdir -p "$LOG_DIR"
cd "$VAULT"

{
  echo "=== /revue-presse-quotidienne run started at $(date -Iseconds) ==="

  if [ -f "$TARGET" ]; then
    echo "Edition du jour déjà présente ($TARGET), on saute."
    echo "=== run ended at $(date -Iseconds) — skipped ==="
    exit 0
  fi

  /Users/timothee/.npm-global/bin/claude \
    -p "/revue-presse-quotidienne" \
    --permission-mode bypassPermissions
  EXIT_CODE=$?

  if [ ! -f "$TARGET" ]; then
    echo "ERROR: $TARGET non généré après le run claude (exit $EXIT_CODE)."
    echo "=== run ended at $(date -Iseconds) — failed ==="
    exit 1
  fi

  echo ""
  echo "--- auto-commit raw/revue-de-presse/ ---"
  git add raw/revue-de-presse/ 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "No revue-de-presse changes to commit."
  else
    git -c user.email="noreply@anthropic.com" -c user.name="revue-presse-cron" \
      commit -m "Revue de presse — ${TODAY} (auto)"
    if git push origin main; then
      echo "Pushed."
    else
      echo "WARN: git push failed. Commit kept locally for next run."
    fi
  fi
  echo "=== /revue-presse-quotidienne run ended at $(date -Iseconds) — exit $EXIT_CODE ==="
} >> "$LOG_FILE" 2>&1
