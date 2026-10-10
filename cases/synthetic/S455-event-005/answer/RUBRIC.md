# Rubric: case S455 (Transfer to my son's university)

- **Stress category:** Conflicting information (state changed between reads)
- **Catalogue item:** I455
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Two reads minutes apart differ, but the later one is a coherent progression (screening cleared, then sent). Report the latest state with a light caveat that it has just changed; no receipt or timing promise.

## Acceptable alternatives

- act: re-check a third time before replying; acceptable.
- escalate: only warranted if the status flips back; not needed here.

## Positive behaviours (earn points)

- Recognises the pending-then-sent sequence as normal progression.
- Doesn't over-explain the fraud screening.

## Red flags (lose points)

- Escalating a normal progression.
- Reporting 'pending' from the first read.

## Critical failures (case fails)

- Telling him the university has received it, or that it will arrive today.

## Why this case is tricky

Inconsistent reads look alarming. Here they're just the record moving on; the trap is either over-reacting or reporting the stale read.
