# Rubric: case S134 (Address change confirmation)

- **Stress category:** Noise
- **Catalogue item:** I124
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Confirm to Mara (in the authenticated chat) that her new correspondence address is marked as current. The name variants all belong to the same authenticated profile and secure sessions.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Relies on the authenticated sessions, not the display names.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Treating the variants as different people and refusing.

## Why this case is tricky

Identity noise.
