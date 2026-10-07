"""List saved sessions."""
import argparse
from pathlib import Path
from ..paths import data_home
from ..state import list_sessions


def configure(subparsers) -> None:
    parser = subparsers.add_parser("list", help="List saved sessions")
    parser.add_argument("--status", choices=("open", "complete", "halted"))
    parser.add_argument("--root")
    parser.set_defaults(handler=run)


def run(args) -> int:
    records = list_sessions(Path(args.root).expanduser() if args.root else data_home())
    if args.status:
        records = [r for r in records if r["status"] == args.status]
    if not records:
        print("No sessions found")
        return 0
    print("SESSION ID                          STATUS    PROJECT              PROVIDER/INTERFACE")
    for record in records:
        print(f"{record['session_id']:<36} {record['status']:<9} {record.get('project', record['project_id'])[:20]:<20} {record['provider']}/{record['interface']}")
    return 0
