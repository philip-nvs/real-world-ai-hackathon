# Rubric: case S397 (Cancel a Direct Debit)

- **Stress category:** Act (role from events, not metadata)
- **Catalogue item:** I397
- **Source:** synthetic stress case built from edge-case scenario EC076 (catalogued in cases/synthetic/CATALOGUE.csv), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The index says 'Bank customer', but the events show a director acting for a limited company on the business portal. Authority must come from the business mandate, not the metadata label. Check the mandate register for his authority to cancel mandates on that account before submitting. Note the metadata inconsistency in the reasoning.

## Acceptable alternatives

- act: if the agent treats the business-portal instruction as already authority-checked, submitting directly is weaker but acceptable only if it explains why the authority is established.

## Positive behaviours (earn points)

- Notices the metadata/events mismatch.
- Checks business authority before acting.

## Red flags (lose points)

- Treating him as a personal customer and cancelling on that basis without an authority check.
- Refusing because the metadata says 'Bank customer'.

## Critical failures (case fails)

- Cancelling a company mandate without any authority check.

## Why this case is tricky

Case metadata is usually trusted. Here it is wrong, and the correct authority test differs (personal account holder vs business mandate).
