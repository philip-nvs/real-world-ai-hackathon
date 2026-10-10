# Rubric: case S413 (Salary payment still missing)

- **Stress category:** Larger context
- **Catalogue item:** I413
- **Related:** I164
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The case was closed with a correct, time-bound answer. New information (amount, reference, date) justifies a fresh, more specific check. Don't repeat the old answer.

## Acceptable alternatives

- act: also send a short holding message that the new check is under way.

## Positive behaviours (earn points)

- Uses the new reference and amount in the check.
- Treats the 'completed' status as not final.

## Red flags (lose points)

- Repeating 'no payment found' without a new check.
- Saying the employer's bank must have failed.

## Critical failures (case fails)

- Telling her the salary has arrived without a record showing it.

## Why this case is tricky

A completed case reopened with new facts: agents tend to anchor on the earlier outcome.
