#!/bin/zsh
# Monthly GSC pull — invoked by launchd com.timboussardon.gsc-pull.plist
# 1) gsc-fetch.py pulls Search Console via service account → raw/data/exports-gsc/
# 2) /gsc-watcher déverse les exports dans wiki/preuves/
# Dégrade proprement si le credential ou les deps manquent (mode dépôt manuel).
set -euo pipefail

export PATH="/Users/timothee/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Code/seo-kb"
BIN="/Users/timothee/.local/bin/seo-kb"
VENV="$BIN/.venv"
LOG_DIR="$VAULT/.claude/logs"
LOG_FILE="$LOG_DIR/gsc-pull-$(date +%Y-%m-%d).log"
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
  echo "=== gsc-pull run started at $(date -Iseconds) ==="

  # --- venv (créé une fois, deps installées si absentes) ---
  if [ ! -d "$VENV" ]; then
    echo "Création du venv $VENV"
    /usr/bin/python3 -m venv "$VENV" || python3 -m venv "$VENV"
  fi
  "$VENV/bin/pip" install --quiet --upgrade pip >/dev/null 2>&1 || true
  "$VENV/bin/python" -c "import google.oauth2.service_account, google.auth.transport.requests" 2>/dev/null \
    || "$VENV/bin/pip" install --quiet google-auth requests

  # --- 1) fetch API (sort 0 si pas de creds → mode dépôt manuel) ---
  set +e
  "$VENV/bin/python" "$BIN/gsc-fetch.py"
  FETCH_CODE=$?
  set -e
  echo "gsc-fetch.py exit $FETCH_CODE"

  # --- 2) watcher : traite tout export présent (auto ou manuel) ---
  set +e
  claude_retry -p "/gsc-watcher" --permission-mode bypassPermissions
  WATCH_CODE=$?
  set -e

  echo ""
  echo "--- auto-commit ---"
  git add raw/data/exports-gsc/ wiki/preuves/ wiki/hypotheses.md wiki/contradictions.md wiki/log.md 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "No GSC/preuves changes to commit."
  else
    git -c user.email="noreply@anthropic.com" -c user.name="gsc-pull-cron" \
      commit -m "GSC pull + preuves — ${TODAY} (auto)"
    # resync avant push (evite la divergence chronique : remote a pu avancer)
    git pull --rebase --autostash origin main 2>/dev/null || true
    if git push origin main; then
      echo "Pushed."
    else
      echo "WARN: git push failed. Commit kept locally for next run."
    fi
  fi
  echo "=== gsc-pull run ended at $(date -Iseconds) — fetch $FETCH_CODE / watcher $WATCH_CODE ==="
} >> "$LOG_FILE" 2>&1
