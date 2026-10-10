# Rubric: case S132 (Repeated text reminders)

- **Stress category:** Noise
- **Catalogue item:** I122
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Kofi the £60 to K Asante was sent on 11 Nov at 08:30, and apologise for the repeated texts (a known alerts problem). The ten texts are one reminder, not ten payments.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Treating the reminders as ten payments.
- Saying the cousin received it.

## Why this case is tricky

Repetition noise.
