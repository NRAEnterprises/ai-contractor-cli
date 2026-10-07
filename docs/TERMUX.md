# Termux

Install Python with `pkg install python`, then install from a wheel/source using `python -m pip install ai-contractor-cli`. Termux uses its normal home/XDG data directory and Python site-packages; avoid hard-coded `/usr/lib` or `/opt` paths. Run `scripts/install-termux.sh` for a source checkout. Set `AI_CONTRACTOR_HOME` to private app storage if desired.
