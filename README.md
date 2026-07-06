# Handoff Note Audit

Check AI-to-human handoff notes for context, owner, and next-step gaps.

## First impression

![Handoff Note Audit cover](assets/readme-cover.svg)

When this tool reports something, I want the finding to be boringly explicit: what matched, how severe it is, and what a reviewer should clean up.

## Tripwires

- `missing-context` (high): handoff context is missing. Fix: Summarize what happened and what was tried..
- `unknown-owner` (medium): handoff owner is missing. Fix: Route to a named team or queue..
- `missing-next-step` (low): next step is missing. Fix: Add the recommended next action..

## Runbook

```bash
git clone https://github.com/mertefekurt/handoff-note-audit.git
cd handoff-note-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Then:

```bash
handoff-note-audit examples/sample.txt
handoff-note-audit examples/sample.txt --json
```

## Development note

The policy lives in `rules.py`; parsing and rendering stay separate so the rule list is easy to audit.
