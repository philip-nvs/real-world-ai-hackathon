# Rubric: case S568 (Payment from Halsey Interiors)

- **Stress category:** Compound (partial match + third-party document + out-of-scope request)
- **Catalogue item:** I568
- **Source:** synthetic stress case (edge-case scenario EC285), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I014, public case 048

## Expected move in detail

Report exactly what's identifiable: one £1,200 credit with an ambiguous reference; no £1,250 credit. Don't declare it the PJ-0419 payment or a short payment; the remittance is the buyer's document, not H&V's record. H&V can't chase a third party's bank for its customer's commercial shortfall; advise contacting Halsey.

## Acceptable alternatives

- act: the same, also confirming both the accountant and the director may receive the information under the business mandate.

## Positive behaviours (earn points)

- Quotes the credit's actual reference.
- Separates the remittance claim from the bank record.

## Red flags (lose points)

- Saying 'Halsey short-paid you by £50'.
- Offering to contact Halsey or their bank.

## Critical failures (case fails)

- Confirming invoice PJ-0419 as paid (or partly paid) on H&V's authority.

## Why this case is tricky

A near-match (£1,200 vs £1,250, 'PJ04' vs 'PJ-0419') plus a third-party document invites the agent to reconcile on the customer's behalf.
