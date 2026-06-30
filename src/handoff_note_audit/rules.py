from __future__ import annotations

from handoff_note_audit.models import Rule

PROJECT_NAME = 'handoff-note-audit'
SUMMARY = 'Check AI-to-human handoff notes for context, owner, and next-step gaps.'
SAMPLE_RISK = 'handoff urgent context missing owner unknown next_step none'
SAMPLE_CLEAN = (
                   'handoff billing issue context invoice mismatch owner billing next_step v'
                   'erify charge id'
               )
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='missing-context',
        severity='high',
        pattern='\\bcontext\\s*(missing|none|null)\\b',
        message='handoff context is missing',
        recommendation='Summarize what happened and what was tried.',
    ),
    Rule(
        code='unknown-owner',
        severity='medium',
        pattern='\\bowner\\s*(unknown|none|null)\\b',
        message='handoff owner is missing',
        recommendation='Route to a named team or queue.',
    ),
    Rule(
        code='missing-next-step',
        severity='low',
        pattern='\\bnext_step\\s*(none|missing|null)\\b',
        message='next step is missing',
        recommendation='Add the recommended next action.',
    ),
)
