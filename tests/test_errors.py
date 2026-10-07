from ai_contractor.errors import ContractorError, ValidationError, SessionNotFoundError

def test_errors_are_user_facing_contractor_errors():
    assert issubclass(ValidationError, ContractorError)
    assert issubclass(SessionNotFoundError, ContractorError)
