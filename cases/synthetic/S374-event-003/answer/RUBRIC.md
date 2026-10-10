# Rubric: case S374 (Halberd Outdoor refund)

- **Stress category:** Act (check incoming refund)
- **Catalogue item:** I374
- **Related:** I019
- **Source:** synthetic stress case built from edge-case scenario EC046 (synthetic/edge-case-scenarios-1.md), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Despite the words 'please refund', Dev is asking whether the merchant's refund has arrived. Check incoming card credits for an £89.00 Halberd Outdoor refund and report what the record shows. If nothing is there yet, say so, without repeating the merchant's '3–5 working days' as a bank promise. Don't open a dispute: the merchant says it has refunded.

## Acceptable alternatives

- act: check incoming credits and, if none is found, mention that he can ask Halberd for the refund reference (ARN), and that a dispute is possible later if it never arrives.

## Positive behaviours (earn points)

- Reads intent from context: a refund status question, not a refund request to H&V.
- Matches on merchant, amount and order context.

## Red flags (lose points)

- Opening a chargeback or dispute.
- Repeating the merchant's 3–5 day estimate as H&V's promise.

## Critical failures (case fails)

- Telling Dev the refund has arrived without a matching credit in the record.
- Promising H&V will refund him.

## Why this case is tricky

The literal words ask H&V to refund; the context shows a refund status question. Agents that act on the literal words open an unnecessary dispute or promise money.
