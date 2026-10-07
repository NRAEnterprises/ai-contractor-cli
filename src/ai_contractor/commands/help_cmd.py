"""Help command implementation."""
def run(_args=None) -> int:
    from ..cli import build_parser
    build_parser().print_help()
    return 0
