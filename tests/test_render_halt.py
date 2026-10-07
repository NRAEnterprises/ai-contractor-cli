from ai_contractor.renderers.halt_renderer import render_halt

def test_halt_captures_blocker():
    assert "permission denied" in render_halt("id", "permission denied")
