"""Record a dated amendment to contract policy."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
from ..paths import data_home


def configure(subparsers) -> None:
    parser = subparsers.add_parser("amend", help="Record a versioned policy amendment")
    parser.add_argument("version")
    parser.add_argument("--text", help="Amendment text; otherwise read stdin")
    parser.add_argument("--root", help="Storage root")
    parser.set_defaults(handler=run)


def run(args) -> int:
    import sys
    text = args.text if args.text is not None else sys.stdin.read()
    if not text.strip():
        raise ValueError("Amendment text must not be empty")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_version = "".join(c if c.isalnum() or c in ".-_" else "-" for c in args.version)
    directory = (Path(args.root).expanduser() if args.root else data_home()) / "amendments"
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / f"{safe_version}_{stamp}.md"
    target.write_text(f"# Amendment {args.version}\n\nRecorded: {stamp}\n\n{text.rstrip()}\n", encoding="utf-8")
    print(target)
    return 0
