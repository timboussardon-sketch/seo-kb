#!/bin/zsh
# Enregistre l'image actuellement dans le presse-papier vers shots/<nom>.png
# Usage : ./clip2shot.sh gsc_perf
DIR="${0:A:h}/shots"
NAME="${1:?usage: clip2shot.sh <nom-sans-extension>}"
DEST="$DIR/$NAME.png"
osascript >/dev/null 2>&1 <<EOF
set fd to open for access (POSIX file "$DEST") with write permission
set eof fd to 0
write (the clipboard as «class PNGf») to fd
close access fd
EOF
if [[ $? -eq 0 && -s "$DEST" ]]; then
  echo "OK -> $DEST"
else
  echo "ÉCHEC : le presse-papier ne contient pas d'image. Refais la capture en copiant dans le presse-papier (⌃⇧⌘4)."
  rm -f "$DEST" 2>/dev/null
fi
