from ai_contractor.cli import main

def test_init_creates_all_artifacts(temp_root, tmp_path, capsys):
    plan = tmp_path / "plan.md"
    plan.write_text("Make a complete app", encoding="utf-8")
    assert main(["init", "--project", "demo", "--plan", str(plan), "--root", str(temp_root)]) == 0
    assert "BEGIN CONTRACT" in capsys.readouterr().out
    sessions = list((temp_root / "sessions" / "demo").iterdir())
    assert (sessions[0] / "01_CONTRACT.md").is_file()
