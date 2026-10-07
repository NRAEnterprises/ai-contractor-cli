"""GUI copy/paste artifact."""
def render_gui(contract: str) -> str:
    return "Paste this entire contract into the model's instruction or first-message field. Keep it available throughout the session.\n\n" + contract
