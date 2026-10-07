#!/usr/bin/env sh
set -eu
if [ "$#" -ne 1 ]; then echo "usage: $0 VERSION" >&2; exit 2; fi
VERSION=$1
case "$VERSION" in *[!0-9A-Za-z.+_-]*|'') echo "invalid version" >&2; exit 2;; esac
python - "$VERSION" <<'PY'
from pathlib import Path
import re, sys
version = sys.argv[1]
for name, pattern in [("src/ai_contractor/_version.py", r'__version__ = ".*"'), ("pyproject.toml", r'version = ".*"')]:
    path = Path(name)
    text = path.read_text()
    replacement = f'__version__ = "{version}"' if name.endswith("_version.py") else f'version = "{version}"'
    path.write_text(re.sub(pattern, replacement, text, count=1) + ("\n" if not text.endswith("\n") else ""))
Path("src/ai_contractor/data/VERSION").write_text(version + "\n")
PY
