import pytest

@pytest.fixture
def temp_root(tmp_path):
    return tmp_path / "contractor"
