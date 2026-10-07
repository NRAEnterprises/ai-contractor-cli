from ai_contractor.cli import main

def test_plan_stdin(monkeypatch, capsys, temp_root):
    monkeypatch.setattr("sys.stdin.read", lambda: "stdin plan")
    assert main(["init", "--project", "stdin-demo", "--plan", "-", "--root", str(temp_root)]) == 0
    assert "stdin plan" in capsys.readouterr().out
