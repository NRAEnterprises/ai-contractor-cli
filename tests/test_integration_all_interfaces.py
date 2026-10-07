from ai_contractor.cli import main
import pytest

@pytest.mark.parametrize("interface", ["cli", "web", "gui", "api"])
def test_interface_artifact(interface, tmp_path, capsys):
    plan = tmp_path / "plan"; plan.write_text("all interfaces")
    root = tmp_path / "root"
    assert main(["init", "--project", interface, "--plan", str(plan), "--interface", interface, "--root", str(root)]) == 0
    output = capsys.readouterr().out
    assert "all interfaces" in output
