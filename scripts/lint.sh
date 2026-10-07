#!/usr/bin/env sh
set -eu
python -m compileall -q src tests
if command -v ruff >/dev/null 2>&1; then ruff check src tests; else echo 'ruff not installed; compile check completed' >&2; fi
