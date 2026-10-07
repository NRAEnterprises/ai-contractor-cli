#!/data/data/com.termux/files/usr/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
python -m pip install "$ROOT"
