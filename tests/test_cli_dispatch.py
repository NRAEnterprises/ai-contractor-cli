from ai_contractor.cli import main

def test_dispatch(capsys):
    assert main(["list", "--root", "/not-created-test-root"]) == 0
    assert "No sessions" in capsys.readouterr().out
