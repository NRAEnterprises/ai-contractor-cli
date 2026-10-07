"""Version command implementation."""
from .._version import __version__

def run(_args=None) -> int:
    print(__version__)
    return 0
