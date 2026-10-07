from ai_contractor.cli import main

def test_verify_session(temp_root, tmp_path, capsys):
    plan = tmp_path / "plan"; plan.write_text("plan")
    main(["init", "--project", "demo", "--plan", str(plan), "--root", str(temp_root)])
    session = next((temp_root / "sessions" / "demo").iterdir()).name
    assert main(["verify", session, "--root", str(temp_root)]) == 0
    assert "expected artifacts present" in capsys.readouterr().out
