from ai_contractor.renderers.gui_renderer import render_gui

def test_gui_renderer_preserves_contract():
    assert "CONTRACT" in render_gui("CONTRACT")
