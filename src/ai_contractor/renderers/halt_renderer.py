"""Halt report template renderer."""
def render_halt(session_id: str, reason: str = "") -> str:
    return f"# Work halted — {session_id}\n\nReason / blocker: {reason or '[state the concrete blocker]'}\n\nCompleted independently: [list]\nRemaining scope: [list]\nEvidence and attempted checks: [list]\nDecision or access needed: [state the minimum needed]\n"
