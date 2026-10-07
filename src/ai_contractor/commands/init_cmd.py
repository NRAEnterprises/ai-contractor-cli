"""Create a contract session."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import re
import uuid
from ..paths import data_home
from ..providers import provider_names, INTERFACES, validate_pair
from ..render import render_contract, render_cli, render_gui, render_web, render_api, render_apply, render_close
from ..state import save_session


def _slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-.")
    return value[:80] or "project"


def configure(subparsers) -> None:
    parser = subparsers.add_parser("init", help="Create and print a completion contract")
    parser.add_argument("--project", help="Project name or ID")
    parser.add_argument("--plan", help="Path to plan markdown; reads stdin when set to -")
    parser.add_argument("--provider", choices=provider_names(), default="generic")
    parser.add_argument("--interface", choices=INTERFACES, default="cli")
    parser.add_argument("--output", help="Optional directory for a copy of generated artifacts")
    parser.add_argument("--root", help="Session storage root (defaults to AI_CONTRACTOR_HOME)")
    parser.set_defaults(handler=run)


def run(args) -> int:
    import sys
    project = args.project or input("Project name: ").strip()
    if args.plan == "-":
        plan = sys.stdin.read()
    elif args.plan:
        plan = Path(args.plan).expanduser().read_text(encoding="utf-8")
    else:
        print("Enter the complete project plan. Finish with Ctrl-D (Ctrl-Z on Windows):")
        plan = sys.stdin.read()
    if not plan.strip():
        raise ValueError("Plan must not be empty")
    validate_pair(args.provider, args.interface)
    project_id = _slug(project)
    session_id = uuid.uuid4().hex
    contract = render_contract(project=project, plan=plan, provider=args.provider, interface=args.interface, session_id=session_id)
    if args.interface == "cli":
        primary = render_cli(contract, session_id)
    elif args.interface == "web":
        primary = render_web(contract)
    elif args.interface == "gui":
        primary = render_gui(contract)
    else:
        primary = render_api(contract)
    apply_text = render_apply(args.provider, args.interface, session_id)
    close_text = render_close(session_id)
    root = Path(args.root).expanduser() if args.root else data_home()
    record = {
        "session_id": session_id, "project_id": project_id, "project": project,
        "status": "open", "provider": args.provider, "interface": args.interface,
        "created_at": datetime.now(timezone.utc).isoformat(), "closed_at": None,
        "plan": plan, "evidence": None,
    }
    folder = save_session(record, root)
    artifacts = {
        "01_CONTRACT.md": primary,
        "02_APPLY_HERE.txt": apply_text,
        "03_CLOSE_BLOCK.md": close_text,
    }
    for name, content in artifacts.items():
        (folder / name).write_text(content, encoding="utf-8")
    (folder / "artifacts").mkdir(exist_ok=True)
    if args.output:
        out = Path(args.output).expanduser()
        out.mkdir(parents=True, exist_ok=True)
        for name, content in artifacts.items():
            (out / name).write_text(content, encoding="utf-8")
    print(primary, end="" if primary.endswith("\n") else "\n")
    print(f"\nSession {session_id} saved to {folder}", file=sys.stderr)
    return 0
