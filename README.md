# AI Contractor++

AI Contractor++ creates explicit completion contracts for AI-assisted software work. It turns a plan into an interface- and provider-aware artifact, preserves the full scope, and supplies a close-out gate for CLI sessions. It is a workflow aid—not a sandbox, execution environment, or substitute for human review.

## Install

```sh
python -m pip install ai-contractor-cli
ai-contractor --help
```

From a checkout: `python -m pip install -e .`.

## Quick start

```sh
ai-contractor init --project my-app --provider generic --interface cli --plan plan.md
```

The command prints the generated contract and writes its contract, apply instructions, close block, and JSON session record beneath the configured data directory. For an interactive setup, omit `--plan` and enter the plan at the prompt. Copy/paste the generated instructions into the target AI session. Use `ai-contractor close SESSION_ID --evidence evidence.json` at the end of a CLI-driven session. Web/API/GUI artifacts contain a one-shot close loop because those environments do not have a reliable local command callback.

Useful commands: `init`, `show`, `list`, `verify`, `close`, `amend`, `version`, `help`. Run `ai-contractor help` for syntax.

Storage defaults to `$HOME/.ai-contractor-cli` (or `$XDG_DATA_HOME/ai-contractor-cli` when XDG is set) and can be overridden with `AI_CONTRACTOR_HOME`. Set `AI_CONTRACTOR_HOME=/opt/ai-contractor-cli` for a shared installation. No project files are silently changed. Generated artifacts are written only to the chosen storage root unless `--output` is supplied.

## Principles

The contract instructs the model to inspect before changing, identify missing requirements rather than silently assuming them away, implement the complete necessary solution, validate it, and report evidence and unresolved blockers. It explicitly forbids fabricated test results and requires scope-affecting questions to be raised. See [docs/DISCIPLINE.md](docs/DISCIPLINE.md) and [docs/WORKFLOWS.md](docs/WORKFLOWS.md).

## Development

```sh
python -m pip install -e . pytest
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and the documentation index.
