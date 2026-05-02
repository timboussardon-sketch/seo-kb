#!/bin/zsh
# Monthly snapshot refresh — invoked by launchd com.timboussardon.refresh-snapshots
# Refresh memory + transcripts archive, commit, push.
# No Claude API calls — pure shell.
set -euo pipefail

export PATH="/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Documents/seo-kb"
LOG_DIR="$VAULT/.claude/logs"
LOG_FILE="$LOG_DIR/refresh-snapshots-$(date +%Y-%m-%d).log"

mkdir -p "$LOG_DIR"
cd "$VAULT"

{
  echo "=== refresh-snapshots run started at $(date -Iseconds) ==="

  # 1. Memory snapshot — overwrite
  echo "--- memory ---"
  rm -rf .claude/memory-snapshot/*
  cp -r ~/.claude/projects/-Users-timothee-Documents-seo-kb/memory/. .claude/memory-snapshot/
  ls -la .claude/memory-snapshot/

  # 2. Transcripts tarball — new file each month
  TODAY=$(date +%Y-%m-%d)
  TARBALL=".claude/transcripts-archive/transcripts-${TODAY}-snapshot.tar.gz"
  echo "--- transcripts → $TARBALL ---"
  cd ~/.claude/projects
  tar czf "$VAULT/$TARBALL" -- "-Users-timothee-Documents-seo-kb" "-Users-timothee-Documents-organikk-next"
  cd "$VAULT"
  ls -lh "$TARBALL"

  # 3. Optional: prune tarballs older than 6 months (keep last 6 snapshots)
  echo "--- pruning old tarballs (>180 days) ---"
  find .claude/transcripts-archive/ -name "transcripts-*-snapshot.tar.gz" -mtime +180 -print -delete

  # 4. Git commit + push if anything changed
  echo "--- git status ---"
  git add .claude/memory-snapshot .claude/transcripts-archive

  if git diff --cached --quiet; then
    echo "No changes — nothing to commit."
  else
    git -c user.email="noreply@anthropic.com" -c user.name="refresh-snapshots-cron" \
      commit -m "Refresh memory + transcripts snapshot ${TODAY}"
    if git push origin main; then
      echo "Pushed."
    else
      echo "WARN: git push failed (network? conflict?). Commit kept locally for next run."
    fi
  fi

  echo "=== refresh-snapshots run ended at $(date -Iseconds) ==="
} >> "$LOG_FILE" 2>&1
