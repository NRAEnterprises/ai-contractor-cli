# Contributing

Contributions should preserve predictable output, safe path handling, and accurate reporting. Open an issue for major behavior changes; include a reproduction and expected behavior for bugs.

## Setup and checks

```sh
python -m pip install -e .
pytest
python -m compileall src
```

Keep the runtime dependency-free where practical. Add or update tests for observable behavior, avoid claiming commands were run unless they were, and document user-facing flags. Use conventional, focused commits. Never include secrets or real user session artifacts in fixtures.
