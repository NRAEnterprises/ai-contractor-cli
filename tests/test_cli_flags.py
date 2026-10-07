from ai_contractor.cli import build_parser

def test_parser_defaults():
    args = build_parser().parse_args(["init", "--project", "demo", "--plan", "-"])
    assert args.provider == "generic"
    assert args.interface == "cli"
