"""CLI-session bootstrap artifact."""
def render_cli(contract: str, session_id: str) -> str:
    return f'''# CLI AI session link / bootstrap

Paste the complete contract below into the active AI CLI conversation before requesting implementation. Keep this session open through verification. At the end, create a factual evidence JSON file if possible, then run:

```sh
ai-contractor close {session_id} --evidence evidence.json
```

If the CLI cannot invoke local commands, paste its final completion report into the close command's interactive prompt. Do not mark work complete without evidence.

--- BEGIN CONTRACT ---
{contract.rstrip()}
--- END CONTRACT ---
'''
