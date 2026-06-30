# handoff-note-audit

**Command Tour.** Check AI-to-human handoff notes for context, owner, and next-step gaps.

## First Command

Human handoffs fail when notes are vague. This CLI checks escalation summaries before tickets reach a queue.

## Useful Flags

`handoff-note-audit` accepts handoff notes, escalation summaries, or ticket comments in text, JSON, JSONL, or CSV form.

## Sample Input

```bash
python -m pip install -e ".[dev]"
handoff-note-audit examples/sample.txt
handoff-note-audit examples/sample.txt --json --fail-on medium
```

## Sample Output

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-context` | high | handoff context is missing |
| `unknown-owner` | medium | handoff owner is missing |
| `missing-next-step` | low | next step is missing |

## Tests

```bash
ruff check .
pytest
python -m handoff_note_audit --help
```

License: MIT

### Example Input

```text
handoff urgent context missing owner unknown next_step none
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the handoff-note-audit policy surface explicit.
