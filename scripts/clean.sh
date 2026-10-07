#!/usr/bin/env sh
set -eu
rm -rf build dist .pytest_cache .coverage htmlcov
find . -type d -name __pycache__ -prune -exec rm -rf {} +
find . -type d -name '*.egg-info' -prune -exec rm -rf {} +
