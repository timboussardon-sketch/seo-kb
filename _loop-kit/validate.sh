#!/usr/bin/env bash
# Loop Kit - validation generique d'un brain (memoire append-only).
# Une ligne JSONL cassee = l'agent perd confiance dans sa memoire. A lancer AVANT tout commit.
# Usage : ./validate.sh [chemin_du_brain]   (defaut : dossier courant). exit 0 = OK, 1 = invalide.
set -uo pipefail
DIR="${1:-.}"
cd "$DIR" || exit 1
fail=0
for f in ledgers/*.jsonl; do
  [ -e "$f" ] || continue
  n=0
  while IFS= read -r line || [ -n "$line" ]; do
    n=$((n+1)); [ -z "$line" ] && continue
    echo "$line" | python3 -c "import json,sys; json.loads(sys.stdin.read())" 2>/dev/null || { echo "INVALIDE: $DIR/$f ligne $n"; fail=1; }
  done < "$f"
done
for f in derived/*.json; do
  [ -e "$f" ] || continue
  python3 -c "import json; json.load(open('$f'))" 2>/dev/null || { echo "INVALIDE: $DIR/$f"; fail=1; }
done
for f in ledgers/runs.jsonl ledgers/claims.jsonl; do
  [ -e "$f" ] || continue
  while IFS= read -r line || [ -n "$line" ]; do
    [ -z "$line" ] && continue
    echo "$line" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); sys.exit(0 if 'capture_mode' in d else 1)" 2>/dev/null || { echo "capture_mode MANQUANT dans $DIR/$f: ${line:0:60}..."; fail=1; }
  done < "$f"
done
if [ "$fail" -eq 0 ]; then echo "OK: memoire valide ($DIR)"; else echo "ECHEC: corriger avant commit ($DIR)"; fi
exit $fail
