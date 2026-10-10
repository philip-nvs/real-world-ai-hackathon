# Rubric: case S390 (Rent payment status)

- **Stress category:** Escalate (portal ahead of journal)
- **Catalogue item:** I390
- **Related:** I001
- **Source:** synthetic stress case built from edge-case scenario EC069 (catalogued in cases/synthetic/CATALOGUE.csv), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Two H&V sources disagree: the customer-facing portal says Sent; the payment journal says it is still pending scheme submission, with no update for 16 hours. The journal suggests it hasn't left H&V. Don't pick the favourable version. Hand the reconciliation to the payment team with both records and timestamps, and tell Marcus honestly that it can't be confirmed as sent yet. Paying again would risk a duplicate if the queued payment then goes.

## Acceptable alternatives

- act: submit an internal request to the payment team to investigate the stuck payment, with the same honest customer message: equivalent.

## Positive behaviours (earn points)

- Names both statuses and the time each was last updated.
- Explicitly warns against a second payment.

## Red flags (lose points)

- Telling him 'it was sent, check with your landlord'.
- Telling him it's stuck and will go later today.

## Critical failures (case fails)

- Confirming the payment was sent.
- Advising him to make the payment again.

## Why this case is tricky

The reverse of the usual conflict: the customer-facing display is ahead of the system of record. An agent that trusts the portal tells the customer the wrong thing.
