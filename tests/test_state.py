from datetime import datetime, timezone
from ai_contractor.state import save_session, load_session, list_sessions

def test_roundtrip(temp_root):
    record = dict(session_id="abc123", project_id="demo", status="open", provider="generic", interface="cli", created_at=datetime.now(timezone.utc).isoformat(), plan="plan")
    folder = save_session(record, temp_root)
    assert load_session("abc123", temp_root)["plan"] == "plan"
    assert len(list_sessions(temp_root)) == 1
    assert (folder / "04_SESSION.json").exists()
