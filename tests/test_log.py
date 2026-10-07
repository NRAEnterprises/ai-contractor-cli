from ai_contractor.log import get_logger

def test_logger():
    assert get_logger("test.contractor").name == "test.contractor"
