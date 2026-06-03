#!/usr/bin/env bash
# Validation du cerveau de contenu (content-brain).
# Usage : ./validate.sh <project>   (exit 0 = OK, 1 = au moins un fichier invalide)
# Une ligne JSONL cassée = la mémoire devient suspecte. À lancer AVANT tout commit.
set -uo pipefail
cd "$(dirname "$0")" || exit 1
proj="${1:-}"
[ -z "$proj" ] && { echo "usage: ./validate.sh <project>"; exit 1; }
dir="$proj"
[ -d "$dir/ledgers" ] || { echo "projet introuvable: $dir"; exit 1; }
fail=0
for f in "$dir"/ledgers/*.jsonl; do
  [ -e "$f" ] || continue
  n=0
  while IFS= read -r line || [ -n "$line" ]; do
    n=$((n+1)); [ -z "$line" ] && continue
    echo "$line" | python3 -c "import json,sys; json.loads(sys.stdin.read())" 2>/dev/null || { echo "INVALIDE: $f ligne $n"; fail=1; }
  done < "$f"
done
# capture_mode obligatoire sur runs.jsonl et claims.jsonl
for f in "$dir"/ledgers/runs.jsonl "$dir"/ledgers/claims.jsonl; do
  [ -e "$f" ] || continue
  while IFS= read -r line || [ -n "$line" ]; do
    [ -z "$line" ] && continue
    echo "$line" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); sys.exit(0 if 'capture_mode' in d else 1)" 2>/dev/null || { echo "capture_mode MANQUANT dans $f: ${line:0:60}..."; fail=1; }
  done < "$f"
done
[ "$fail" -eq 0 ] && echo "OK: mémoire $proj valide" || echo "ÉCHEC: corriger avant commit"
exit $fail
