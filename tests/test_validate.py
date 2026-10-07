import pytest
from ai_contractor.validate import require_text, validate_session
from ai_contractor.errors import ValidationError

def test_text_and_session_validation():
    assert require_text(" x ", "value") == "x"
    with pytest.raises(ValidationError):
        require_text(" ", "value")
    with pytest.raises(ValidationError):
        validate_session({})
