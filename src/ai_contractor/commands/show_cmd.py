"""Print a stored session."""
import argparse
import json
from pathlib import Path
from ..state import load_session
from ..paths import data_home


def configure(subparsers) -> None:
    parser = subparsers.add_parser("show", help="Show a session record")
    parser.add_argument("session_id")
    parser.add_argument("--root")
    parser.set_defaults(handler=run)


def run(args) -> int:
    record = load_session(args.session_id, Path(args.root).expanduser() if args.root else data_home())
    print(json.dumps(record, indent=2, ensure_ascii=False))
    return 0
