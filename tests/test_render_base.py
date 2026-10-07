from ai_contractor.renderers.base import render_contract

def test_contract_includes_plan_and_gates():
    text = render_contract(project="demo", plan="build a widget", provider="generic", interface="cli", session_id="id")
    assert "build a widget" in text
    assert "Completion checklist" in text
