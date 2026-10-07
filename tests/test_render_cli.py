from ai_contractor.renderers.cli_renderer import render_cli

def test_cli_handoff_has_close_command():
    assert "ai-contractor close id" in render_cli("contract", "id")
