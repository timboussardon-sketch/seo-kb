#!/bin/zsh
# Publications ingest — invoked by launchd com.timboussardon.publications-ingest.plist
# Scrape les dernières pages Algorithme (Substack) + Organikk (blog) et crée les fiches
# wiki/sources/ correspondantes via le skill publications-ingest, puis commit/push.
set -euo pipefail

export PATH="/Users/timothee/.npm-global/bin:/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Code/seo-kb"
LOG_DIR="$VAULT/.claude/logs"
LOG_FILE="$LOG_DIR/publications-ingest-$(date +%Y-%m-%d).log"
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
  echo "=== /publications-ingest run started at $(date -Iseconds) ==="

  # Resync AVANT le scrape : le vault local doit refleter le remote pour que la
  # dedup (grep URL dans wiki/sources/) ne recree pas des fiches deja poussees ailleurs.
  git pull --rebase --autostash origin main 2>/dev/null || echo "WARN: pull initial echoue, on continue sur l'etat local."

  set +e
  claude_retry -p "/publications-ingest" --permission-mode bypassPermissions
  EXIT_CODE=$?
  set -e

  echo ""
  echo "--- auto-commit wiki/ ---"
  git add wiki/ 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "Rien de nouveau a stager (un autocommit WIP concurrent a pu deja commit les fiches)."
  else
    git -c user.email="noreply@anthropic.com" -c user.name="publications-ingest-cron" \
      commit -m "Ingest publications (Algorithme + Organikk) — ${TODAY} (auto)"
  fi

  # Push si le local est en avance sur origin — que le commit vienne de nous OU d'un
  # autocommit WIP concurrent. Sinon les fiches restent bloquees en local (bug observe au 1er run).
  echo "--- push si en avance sur origin ---"
  git pull --rebase --autostash origin main 2>/dev/null || true
  AHEAD="$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)"
  if [ "$AHEAD" != "0" ]; then
    if git push origin main; then
      echo "Pushed ($AHEAD commit(s))."
    else
      echo "WARN: git push failed. Commits gardes en local pour le prochain run."
    fi
  else
    echo "A jour avec origin, rien a pousser."
  fi
  echo "=== /publications-ingest run ended at $(date -Iseconds) — exit $EXIT_CODE ==="
} >> "$LOG_FILE" 2>&1
