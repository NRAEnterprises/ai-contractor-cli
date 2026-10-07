from ai_contractor.renderers.apply_renderer import render_apply

def test_apply_identifies_session():
    assert "id" in render_apply("generic", "cli", "id")
