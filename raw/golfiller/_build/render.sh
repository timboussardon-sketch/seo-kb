#!/bin/zsh
# Rendu du PDF Golfiller depuis golfiller.html (style Notion) via Chrome headless.
# Usage : ./render.sh
set -e
DIR="${0:A:h}"
OUT="$DIR/../golfiller-strat.pdf"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT" "file://$DIR/golfiller.html"

echo "OK -> $OUT"
