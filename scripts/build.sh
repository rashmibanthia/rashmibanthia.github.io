#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
HUGO_BIN="${HUGO_BIN:-../bin/hugo}"
if [ ! -x "$HUGO_BIN" ]; then HUGO_BIN=hugo; fi
exec "$HUGO_BIN" --cacheDir "$PWD/../.hugo-cache" --minify --gc --cleanDestinationDir --destination "${BUILD_DESTINATION:-../preview}"
