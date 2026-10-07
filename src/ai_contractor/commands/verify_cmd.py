"""Verify session record and expected files."""
import argparse
from pathlib import Path
from ..paths import data_home, session_dir
from ..state import load_session


def configure(subparsers) -> None:
    parser = subparsers.add_parser("verify", help="Check session record and generated artifacts")
    parser.add_argument("session_id")
    parser.add_argument("--root")
    parser.set_defaults(handler=run)


def run(args) -> int:
    root = Path(args.root).expanduser() if args.root else data_home()
    record = load_session(args.session_id, root)
    folder = session_dir(args.session_id, root)
    expected = ["01_CONTRACT.md", "02_APPLY_HERE.txt", "03_CLOSE_BLOCK.md", "04_SESSION.json"]
    missing = [name for name in expected if not (folder / name).is_file()]
    if missing:
        print("Missing: " + ", ".join(missing))
        return 1
    print(f"OK: session {record['session_id']} ({record['status']}); expected artifacts present")
    return 0
