from ai_contractor.conduct_check import prompts, checklist

def test_conduct_prompts_are_renderable():
    assert prompts()
    assert "[ ]" in checklist()
