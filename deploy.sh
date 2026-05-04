#!/usr/bin/env bash
# deploy.sh — Erstellt eine ZIP der Website fuer den IONOS-Upload.
#
# Output: ~/Downloads/satk-website-<datum>-<sha>.zip
# Inhalt: alle git-tracked Dateien des aktuellen HEAD (respektiert .gitignore).
#
# Aufruf: ./deploy.sh
#
# Tipp: Vor dem Aufruf committen, sonst landen lokale Aenderungen NICHT in der ZIP.

set -euo pipefail

cd "$(dirname "$0")"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Fehler: nicht in einem git-Repo." >&2
  exit 1
fi

if ! git diff --quiet HEAD || ! git diff --cached --quiet; then
  echo "Hinweis: ungetrackte oder uncommittete Aenderungen vorhanden."
  echo "Die ZIP enthaelt NUR den Stand des letzten Commits ($(git rev-parse --short HEAD))."
  echo "Falls du auch die lokalen Aenderungen brauchst: erst committen, dann nochmal aufrufen."
  echo
fi

DATE=$(date +%Y-%m-%d)
SHA=$(git rev-parse --short HEAD)
OUT="$HOME/Downloads/satk-website-${DATE}-${SHA}.zip"

git archive --format=zip --output="$OUT" HEAD

SIZE=$(du -h "$OUT" | cut -f1)
COUNT=$(unzip -l "$OUT" | tail -1 | awk '{print $2}')

echo "ZIP erstellt: $OUT"
echo "Groesse: $SIZE  ·  $COUNT Dateien"
echo
echo "Naechster Schritt: ZIP im IONOS-Webspace-Manager hochladen,"
echo "dann Rechtsklick -> Entpacken -> bestehende Dateien ueberschreiben."
