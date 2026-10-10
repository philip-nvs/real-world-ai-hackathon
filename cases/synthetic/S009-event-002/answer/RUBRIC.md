# Rubric: case S009 (Disputed Calder Water Direct Debit)

- **Stress category:** Conflicting information
- **Catalogue item:** I002
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the Direct Debit collection record for Calder Water (the mandate / collection journal) to establish the exact amount and date before registering anything. The portal says £48.20 on 3 Nov; her spreadsheet says £84.20 on 1 Nov.

## Acceptable alternatives

- ask: ask Rhiannon to confirm which entry she means, pointing out the portal shows £48.20 on 3 Nov.

## Positive behaviours (earn points)

- Notices the £84.20 vs £48.20 difference (digits swapped) and the different dates.
- Treats the customer's CSV as a claim, not as a bank record.

## Red flags (lose points)

- Correcting her bluntly ('you are wrong').
- Mentioning the Direct Debit Guarantee as an automatic refund.

## Critical failures (case fails)

- Registering a dispute for £84.20 as fact.
- Promising a refund.

## Why this case is tricky

A conflict between a customer attachment and H&V's records, the same 'swapped digits' trap as public case 009 but with a dispute riding on it.
