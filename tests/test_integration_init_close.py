import json
from ai_contractor.cli import main

def test_full_session_lifecycle(tmp_path, capsys):
    root = tmp_path / "home"; plan = tmp_path / "plan.md"; plan.write_text("ship it")
    main(["init", "--project", "e2e", "--plan", str(plan), "--root", str(root)])
    session = next((root / "sessions" / "e2e").iterdir()).name
    proof = tmp_path / "proof.json"; proof.write_text(json.dumps({"tests": "passed"}))
    assert main(["close", session, "--evidence", str(proof), "--root", str(root)]) == 0
    assert main(["verify", session, "--root", str(root)]) == 0
