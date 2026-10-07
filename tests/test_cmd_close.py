import json
from ai_contractor.cli import main

def test_close_records_evidence(temp_root, tmp_path):
    plan = tmp_path / "plan"; plan.write_text("plan")
    main(["init", "--project", "demo", "--plan", str(plan), "--root", str(temp_root)])
    session = next((temp_root / "sessions" / "demo").iterdir()).name
    evidence = tmp_path / "evidence.json"; evidence.write_text(json.dumps({"checks_run": ["pytest passed"]}))
    assert main(["close", session, "--evidence", str(evidence), "--root", str(temp_root)]) == 0
