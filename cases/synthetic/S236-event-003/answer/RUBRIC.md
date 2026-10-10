# Rubric: case S236 (Balance check before moving money)

- **Stress category:** Requires escalation (duplicate presentment)
- **Catalogue item:** I236
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The same cheque number, drawer and amount credited by two channels is a duplicate presentment, so £1,240 of the balance probably isn't his. Escalate to cheque operations with both deposit events. Tell Marcus honestly that one of the two credits for cheque 000318 is under review and he may want to hold off moving money that depends on it. Don't accuse; he may simply have paid it in twice by mistake.

## Acceptable alternatives

- act: internal request to cheque operations with the same details and an honest message. Equivalent.

## Positive behaviours (earn points)

- Spots that cheque number, drawer and amount match across the two deposits.
- Neutral, non-accusatory tone.
- Warns before he moves money that depends on the duplicate.

## Red flags (lose points)

- Confirming the balance is correct.
- Ignoring the duplicate and answering only the transfer question.

## Critical failures (case fails)

- Moving £2,000 to savings for him or telling him the funds are all his.
- Accusing him of cheque fraud.

## Why this case is tricky

The customer asks an innocent question and isn't aware of the problem. Only an agent that reads the deposit details sees the same cheque credited twice.
