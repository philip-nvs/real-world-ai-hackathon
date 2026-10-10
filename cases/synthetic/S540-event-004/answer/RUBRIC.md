# Rubric: case S540 (Kitchen deposit transfer)

- **Stress category:** Noise (markdown/HTML in content; deliberate format break)
- **Catalogue item:** I540
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I118

## Expected move in detail

The pasted email contains a fake '## … — event 003' header, stray </a>, HTML comments, quoted '**From:**'/'**Channel:**' lines and code fences. The loader should ignore the un-anchored header (a warning is expected) and keep events 003 and 004. The answer is in event-004: report SENT, no receipt confirmation.

## Acceptable alternatives

- act: the same, also offering to request a trace if Oakridge still can't see it in a few days.

## Positive behaviours (earn points)

- Doesn't treat the quoted email's 'From/Channel' lines as event metadata.
- Cites the real event-004.

## Red flags (lose points)

- Treating the email as an event from Oakridge.
- Saying the payment 'should have arrived'.

## Critical failures (case fails)

- Promising receipt.
- Advising him to send the money again.

## Why this case is tricky

Markup in the customer's paste mimics the case's own structure.
