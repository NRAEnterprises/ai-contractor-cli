# Commands

- `init`: generate contract, apply note, close block, and session record.
- `show ID`: print JSON record.
- `list [--status open|complete|halted]`: list sessions.
- `verify ID`: validate record and required artifacts.
- `close ID [--evidence FILE] [--status complete|halted]`: record final evidence.
- `amend VERSION [--text TEXT]`: write a dated policy amendment.
- `--help`, `help`, and `--version`: CLI help/version.

Commands accept `--root PATH` where applicable. `AI_CONTRACTOR_HOME` overrides the default storage location.
