from ai_contractor.cli import main

def test_list_empty(capsys, temp_root):
    assert main(["list", "--root", str(temp_root)]) == 0
    assert "No sessions" in capsys.readouterr().out
