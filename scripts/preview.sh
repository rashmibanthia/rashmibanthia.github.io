#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
HUGO_BIN="${HUGO_BIN:-../bin/hugo}"
if [ ! -x "$HUGO_BIN" ]; then HUGO_BIN=hugo; fi
exec "$HUGO_BIN" --cacheDir "$PWD/../.hugo-cache" server --bind 127.0.0.1 --port "${PORT:-1313}" --poll 700ms --disableFastRender --noHTTPCache --renderToMemory
