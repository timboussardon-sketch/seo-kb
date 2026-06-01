#!/bin/zsh
# Weekly ingest-backlog sweep — invoked by launchd com.timboussardon.ingest-backlog.plist
# Regenerates wiki/ingest-backlog.md via the ingest-backlog-sweep skill
set -euo pipefail

export PATH="/Users/timothee/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Code/seo-kb"
LOG_DIR="$VAULT/.claude/logs"
LOG_FILE="$LOG_DIR/ingest-backlog-$(date +%Y-%m-%d).log"
TODAY="$(date +%Y-%m-%d)"

mkdir -p "$LOG_DIR"
cd "$VAULT"

# Retry/backoff autour de claude headless (erreurs reseau transitoires en contexte launchd)
claude_retry() {
  local attempt=1 max=3 code=0
  while [ $attempt -le $max ]; do
    set +e
    /Users/timothee/.npm-global/bin/claude "$@"
    code=$?
    set -e
    [ $code -eq 0 ] && return 0
    echo "claude tentative $attempt/$max echouee (exit $code), nouvel essai dans $((attempt*30))s..."
    sleep $((attempt*30))
    attempt=$((attempt+1))
  done
  echo "claude a echoue apres $max tentatives (exit $code)."
  return $code
}

{
  echo "=== /ingest-backlog-sweep run started at $(date -Iseconds) ==="

  set +e
  claude_retry -p "/ingest-backlog-sweep" --permission-mode bypassPermissions
  EXIT_CODE=$?
  set -e

  echo ""
  echo "--- auto-commit wiki/ ---"
  git add wiki/ingest-backlog.md wiki/log.md 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "No backlog changes to commit."
  else
    git -c user.email="noreply@anthropic.com" -c user.name="ingest-backlog-cron" \
      commit -m "Ingest backlog sweep — ${TODAY} (auto)"
    # resync avant push (evite la divergence chronique : remote a pu avancer)
    git pull --rebase --autostash origin main 2>/dev/null || true
    if git push origin main; then
      echo "Pushed."
    else
      echo "WARN: git push failed. Commit kept locally for next run."
    fi
  fi
  echo "=== /ingest-backlog-sweep run ended at $(date -Iseconds) — exit $EXIT_CODE ==="
} >> "$LOG_FILE" 2>&1
