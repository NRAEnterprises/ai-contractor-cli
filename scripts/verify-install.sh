#!/usr/bin/env sh
set -eu
ai-contractor --version
ai-contractor --help >/dev/null
python -c 'import ai_contractor; print(ai_contractor.__version__)'
