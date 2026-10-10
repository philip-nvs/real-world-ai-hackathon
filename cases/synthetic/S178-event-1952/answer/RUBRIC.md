# Rubric: case S178 (Replacement card dispatch)

- **Stress category:** Larger context
- **Catalogue item:** I175
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Wendy dispatch of her replacement card was registered on 19 Nov; receipt isn't recorded. The system has to get through around 1,950 events of history without crashing or losing the last two events.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Produces an answer (the fallback-escalation path is acceptable only if the input really can't be processed).

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Crashing with no answer file.
- Answering from the old card-payment noise.

## Why this case is tricky

Engineering stress: about 120k+ tokens of history. Tests truncation strategy and crash fallback.
