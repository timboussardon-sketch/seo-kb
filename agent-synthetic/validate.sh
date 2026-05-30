#!/usr/bin/env bash
# Validation du cerveau transactionnel SyntheticBrain.
# Une ligne JSONL cassée = l'agent perd confiance dans sa mémoire. À lancer AVANT tout commit.
# Usage : ./validate.sh   (exit 0 = OK, exit 1 = au moins un fichier invalide)

set -uo pipefail
cd "$(dirname "$0")" || exit 1

fail=0

# 1. Tous les .jsonl des ledgers parsent ligne par ligne
for f in ledgers/*.jsonl; do
  [ -e "$f" ] || continue
  n=0
  while IFS= read -r line || [ -n "$line" ]; do
    n=$((n+1))
    [ -z "$line" ] && continue
    echo "$line" | python3 -c "import json,sys; json.loads(sys.stdin.read())" 2>/dev/null || {
      echo "INVALIDE: $f ligne $n"
      fail=1
    }
  done < "$f"
done

# 2. Les JSON purs (manifest dérivé) parsent
for f in derived/*.json; do
  [ -e "$f" ] || continue
  python3 -c "import json,sys; json.load(open('$f'))" 2>/dev/null || { echo "INVALIDE: $f"; fail=1; }
done

# 3. capture_mode present sur chaque ligne de runs.jsonl et claims.jsonl
for f in ledgers/runs.jsonl ledgers/claims.jsonl; do
  [ -e "$f" ] || continue
  while IFS= read -r line || [ -n "$line" ]; do
    [ -z "$line" ] && continue
    echo "$line" | python3 -c "import json,sys; d=json.loads(sys.stdin.read()); sys.exit(0 if 'capture_mode' in d else 1)" 2>/dev/null || {
      echo "capture_mode MANQUANT dans $f: ${line:0:60}..."
      fail=1
    }
  done < "$f"
done

if [ "$fail" -eq 0 ]; then
  echo "OK: mémoire valide (JSONL + JSON + capture_mode)"
else
  echo "ÉCHEC: corriger avant commit"
fi
exit $fail
