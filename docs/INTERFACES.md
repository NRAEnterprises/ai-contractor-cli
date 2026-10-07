# Interfaces

`cli` produces a bootstrap artifact that keeps a local close command in the loop. `web`, `gui`, and `api` produce portable one-shot artifacts with embedded close-out instructions because those surfaces cannot reliably call local state. Interface rendering changes delivery format, not the quality gates. Generated contract prints to stdout and is also saved as `01_CONTRACT.md`; `--output` creates an additional copy.
