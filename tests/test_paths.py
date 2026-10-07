from ai_contractor.paths import data_home, session_dir
from ai_contractor.errors import SessionNotFoundError
import pytest

def test_override_and_missing_session(monkeypatch, tmp_path):
    monkeypatch.setenv("AI_CONTRACTOR_HOME", str(tmp_path))
    assert data_home() == tmp_path.resolve()
    with pytest.raises(SessionNotFoundError):
        session_dir("missing")
