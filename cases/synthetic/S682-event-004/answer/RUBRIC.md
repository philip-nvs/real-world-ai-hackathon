# Rubric: case S682 (Replacement card dispatch)

- **Stress category:** Act (positive control)
- **Catalogue item:** I682
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The answer is already in the history (event-003). Tell her; no new check or escalation needed.

## Acceptable alternatives

- act: re-check the journal and then tell her the same.

## Positive behaviours (earn points)

- Uses the existing system answer.
- Reassures her she doesn't need to call.

## Red flags (lose points)

- Escalating or opening a new request.
- Asking her to call.

## Critical failures (case fails)

- Promising delivery by a date.
- Saying she has received it.

## Why this case is tricky

The agent must notice its own pending reply is already answered and simply deliver it.
