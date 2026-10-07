from ai_contractor.renderers.close_renderer import render_close

def test_close_requires_factual_report():
    assert "Do not report success by default" in render_close("id")
