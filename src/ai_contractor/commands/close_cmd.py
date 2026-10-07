"""Close or halt a session with an evidence record."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from ..state import load_session, save_session
from ..paths import data_home
from ..render import render_close


def configure(subparsers) -> None:
    parser = subparsers.add_parser("close", help="Record session evidence and close it")
    parser.add_argument("session_id")
    parser.add_argument("--evidence", help="Path to evidence file (JSON or text)")
    parser.add_argument("--status", choices=("complete", "halted"), default="complete")
    parser.add_argument("--root", help="Session storage root")
    parser.set_defaults(handler=run)


def run(args) -> int:
    import sys
    root = Path(args.root).expanduser() if args.root else data_home()
    record = load_session(args.session_id, root)
    if record["status"] != "open":
        raise ValueError(f"Session is already {record['status']}")
    if args.evidence:
        evidence_path = Path(args.evidence).expanduser()
        raw = evidence_path.read_text(encoding="utf-8")
        try:
            evidence = json.loads(raw)
        except json.JSONDecodeError:
            evidence = {"report": raw}
        evidence_file = evidence_path
    else:
        print("Paste the factual final report/evidence, then finish with Ctrl-D (Ctrl-Z on Windows):", file=sys.stderr)
        raw = sys.stdin.read()
        evidence = {"report": raw}
        evidence_file = None
    if not raw.strip():
        raise ValueError("Close requires non-empty evidence; session remains open")
    if args.status == "complete" and isinstance(evidence, dict):
        report = " ".join(str(v) for v in evidence.values())
        incomplete = any(word in report.lower() for word in ("incomplete", "not run", "blocked", "failed"))
        if incomplete:
            print("warning: evidence mentions incomplete work, unrun checks, blockers, or failures; consider --status halted", file=sys.stderr)
    folder = save_session({**record, "status": args.status, "closed_at": datetime.now(timezone.utc).isoformat(), "evidence": evidence}, root)
    (folder / "03_CLOSE_BLOCK.md").write_text(render_close(args.session_id), encoding="utf-8")
    artifact_dir = folder / "artifacts"
    artifact_dir.mkdir(exist_ok=True)
    if evidence_file:
        (artifact_dir / (evidence_file.name + ".copy")).write_text(raw, encoding="utf-8")
    print(f"Session {args.session_id} recorded as {args.status}: {folder}")
    return 0
