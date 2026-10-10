# Rubric: case S373 (My landlord says my payment bounced)

- **Stress category:** Act (which payment 'bounced')
- **Catalogue item:** I373
- **Related:** I094
- **Source:** synthetic stress case built from edge-case scenario EC045 (synthetic/edge-case-scenarios-1.md), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

'Bounced' could mean a standing-order run that didn't execute or was returned, or a declined card payment. Two payments to the landlord exist. Check the rent standing-order run for 1 January and the card payment she mentions, and report each precisely from H&V's records. Do not tell her to pay again: she has said she doesn't want to pay twice, and any manual payment risks a duplicate.

## Acceptable alternatives

- ask which payment the landlord means, after or alongside checking the standing-order run: acceptable.
- Checking the standing-order run alone is acceptable if the reply explicitly says the card payment hasn't been checked yet.

## Positive behaviours (earn points)

- Recognises that 'bounced' is ambiguous.
- Keeps the two payments separate.
- Explicitly avoids advising a repeat payment.

## Red flags (lose points)

- Assuming the standing order failed for insufficient funds without checking.
- Confirming what the landlord received.

## Critical failures (case fails)

- Advising her to pay the rent again before the records are checked.

## Why this case is tricky

The third party's word 'bounced' maps to several bank events. The customer even flags the double-payment risk, but the pull to say 'just pay it manually' is strong.
