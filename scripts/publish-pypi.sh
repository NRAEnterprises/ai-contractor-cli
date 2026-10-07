#!/usr/bin/env sh
set -eu
python -m build
python -m twine upload dist/*
