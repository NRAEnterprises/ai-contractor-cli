"""Web-chat one-shot artifact."""
def render_web(contract: str) -> str:
    return contract.rstrip() + "\n\n## One-shot close-out\nBefore ending this chat, audit the implementation against every requirement above. Report exact checks actually run, their outcomes, unresolved work, and risks. If anything remains incomplete, say so plainly; do not claim completion. Preserve this final report as session evidence.\n"
