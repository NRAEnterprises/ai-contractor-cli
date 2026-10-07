from ai_contractor.renderers.web_renderer import render_web

def test_web_closes_loop():
    assert "One-shot close-out" in render_web("contract")
