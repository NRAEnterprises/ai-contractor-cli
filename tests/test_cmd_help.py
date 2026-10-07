from ai_contractor.cli import main

def test_help(capsys):
    assert main([]) == 0
    assert "completion contracts" in capsys.readouterr().out
