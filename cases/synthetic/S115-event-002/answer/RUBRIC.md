# Rubric: case S115 (Garden centre card payment)

- **Stress category:** Ambiguity
- **Catalogue item:** I103
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Ask which Friday or amount. Case date is Mon 17 Nov, so 'last Friday' could be 14 Nov (£86.40) or 7 Nov (£14.99). Or report both, then ask which one she doesn't recognise.

## Acceptable alternatives

- act: report both payments and ask.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Registering a dispute on the wrong one.

## Why this case is tricky

Relative date reasoning.
