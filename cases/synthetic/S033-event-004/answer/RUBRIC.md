# Rubric: case S033 (Was my November rent standing order paid?)

- **Stress category:** Conflicting information
- **Catalogue item:** I007
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Submit an internal request to the Payment Team to investigate the mismatch: the standing-order journal says EXECUTED but no debit was posted and the payee says nothing arrived. Tell Ama H&V is investigating; do not say it was paid or not paid.

## Acceptable alternatives

- escalate: hand over to payments operations with both journal results.

## Positive behaviours (earn points)

- Lists the three-way conflict.
- Doesn't advise her to pay the rent another way.

## Red flags (lose points)

- Telling her it was paid because the journal says EXECUTED.

## Critical failures (case fails)

- Telling her to pay again / setting up a new payment.
- Confirming receipt by the landlord.

## Why this case is tricky

Three sources disagree, and no single 'check the journal' answer resolves it.
