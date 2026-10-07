# Troubleshooting

- Command not found: install the package in the active interpreter and ensure its scripts directory is on PATH; alternatively use `python -m ai_contractor`.
- Wrong storage root: inspect `AI_CONTRACTOR_HOME`, `XDG_DATA_HOME`, and `--root`.
- Session missing: use `ai-contractor list`; session IDs are opaque and case-sensitive.
- Invalid provider/interface: check `ai-contractor init --help` and the supported combinations.
- Permission errors: choose a writable private root; do not run as root merely to bypass permissions.
- Close rejects empty evidence: provide a factual evidence file or stdin report.
