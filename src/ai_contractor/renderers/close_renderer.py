"""Close-out block for persisted sessions."""
def render_close(session_id: str) -> str:
    return f'''# Close-out — session {session_id}

Do not report success by default. Compare the result to the full contract and supplied scope. List exact files/behavior changed, commands run with outcomes, tests not run and why, remaining defects/risks, and any incomplete scope. Attach or reference evidence. A session is complete only when required work and validation are complete; otherwise mark it halted/incomplete.
'''
