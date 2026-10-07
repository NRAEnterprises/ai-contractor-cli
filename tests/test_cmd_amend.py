from argparse import Namespace
from ai_contractor.commands.amend_cmd import run

def test_amend_writes_record(temp_root):
    run(Namespace(version="1.0", text="change policy", root=str(temp_root)))
    assert list((temp_root / "amendments").glob("*.md"))
