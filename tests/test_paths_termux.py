from ai_contractor.paths import data_home

def test_termux_home_override(monkeypatch, tmp_path):
    monkeypatch.setenv("AI_CONTRACTOR_HOME", str(tmp_path / "termux"))
    assert str(data_home()).endswith("termux")
