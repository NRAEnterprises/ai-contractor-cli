# Workflow

1. Write a plan describing goals, constraints, acceptance criteria, and known context.
2. Run `ai-contractor init --project NAME --plan plan.md --provider generic --interface cli`.
3. Paste the printed artifact into the matching model/environment and let the model inspect and work in the real project.
4. Keep the contract in force through integrated validation and audit.
5. For CLI, save final report/evidence and run `ai-contractor close ID --evidence evidence.json`. Use `--status halted` for unresolved work. Web/API/GUI artifacts request final evidence in their own response; optionally record it using close.
6. Review the evidence, then retain/archive the session as appropriate.

The CLI records evidence; it cannot independently establish that the AI's claims are true.
