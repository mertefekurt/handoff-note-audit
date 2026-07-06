<p align="center">
  <img src="assets/readme-cover.svg" alt="Handoff Note Audit cover" width="100%" />
</p>

# Handoff Note Audit

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Check AI-to-human handoff notes for context, owner, and next-step gaps.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `handoff-note-audit` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
handoff-note-audit examples/sample.txt
handoff-note-audit examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-context` | high | handoff context is missing |
| `unknown-owner` | medium | handoff owner is missing |
| `missing-next-step` | low | next step is missing |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
handoff urgent context missing owner unknown next_step none
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m handoff_note_audit --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Handoff Note Audit policy easy to review.
