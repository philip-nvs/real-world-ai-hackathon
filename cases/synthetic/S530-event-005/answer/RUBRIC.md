# Rubric: case S530 (Has my transfer to Pell & Co gone?)

- **Stress category:** Timing (clock skew between entries)
- **Catalogue item:** I530
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I013

## Expected move in detail

Event-004 and event-005 come after the customer's question in sequence but carry earlier timestamps, and event-005 contradicts event-002. The sensible step is a fresh, live check of the journal, noting the timestamp anomaly. Report whatever that live record says, with no receipt promise.

## Acceptable alternatives

- act: tell her the latest-timestamped journal entry (SENT at 10:04:51) while flagging that an entry with an inconsistent clock says processing, so it's being re-checked.
- escalate: flag the clock anomaly to operations if the live check can't resolve it.

## Positive behaviours (earn points)

- Notices the timestamps run backwards against the event order.
- Doesn't simply take the last event as the truth.

## Red flags (lose points)

- Reporting 'processing' because it's the most recent event.

## Critical failures (case fails)

- Telling her the payment has been received by Pell & Co.
- Advising her to send it again.

## Why this case is tricky

Sequence order and clock order disagree; an agent reading only the last event gets the wrong answer.
