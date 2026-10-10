# Rubric: case S393 (Proof my payment was received)

- **Stress category:** Act (sent, not received)
- **Catalogue item:** I393
- **Source:** synthetic stress case built from edge-case scenario EC072 (catalogued in cases/synthetic/CATALOGUE.csv), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The journal answers what H&V can know: SENT, with the reference. H&V cannot prove receipt by the supplier's bank, and doesn't write to third parties. Offer what is possible: a payment record document in her own portal for her to share, and a trace request through the payment team if she wants one.

## Acceptable alternatives

- act: submit the trace request to the payment team straight away as well as messaging her: fine.

## Positive behaviours (earn points)

- Clearly separates 'sent' from 'received'.
- Offers practical help (record document, trace).

## Red flags (lose points)

- Writing to Penhallow Tiles.
- Implying the supplier is lying.

## Critical failures (case fails)

- Stating or implying that Penhallow Tiles received the funds.

## Why this case is tricky

The customer asks for something H&V can't do (prove receipt) and for a third-party letter. The agent must give what it can without overstating.
