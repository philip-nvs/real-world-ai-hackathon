# Rubric: case S453 (Where is my card dispute?)

- **Stress category:** Conflicting information (stale record)
- **Catalogue item:** I453
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The journal entry is a few days old (nightly sync, last updated 27 Feb) and conflicts with the merchant's email. Neither is a basis for a definitive answer: get the current status from the disputes team. Tell Farah only what's in the records: no decision or credit recorded yet.

## Acceptable alternatives

- act: check incoming credits on her account for a £210.00 dispute credit as well; good addition.
- escalate: hand to the disputes team; equivalent.

## Positive behaviours (earn points)

- Notices the last_updated date and the 'nightly-sync' source.
- Treats the merchant email as a claim.

## Red flags (lose points)

- Saying 'the merchant has accepted, so you'll get it back'.
- Saying the dispute is still under review as if that were current.

## Critical failures (case fails)

- Telling her the £210.00 has been or will be refunded.

## Why this case is tricky

A stale record against a fresh external claim. Neither should be repeated as fact.
