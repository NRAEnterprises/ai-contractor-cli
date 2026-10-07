import pytest
from ai_contractor.providers import validate_pair
from ai_contractor.errors import ValidationError

def test_valid_pair():
    validate_pair("generic", "api")

def test_invalid_pair():
    with pytest.raises(ValidationError):
        validate_pair("google", "api")
