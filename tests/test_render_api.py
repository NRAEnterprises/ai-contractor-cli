from ai_contractor.renderers.api_renderer import render_api

def test_api_structured_evidence():
    assert "structured evidence" in render_api("contract")
