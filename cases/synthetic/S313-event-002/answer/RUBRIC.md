# Rubric: case S313 (Letter from my letting agent)

- **Stress category:** Act (OCR misread)
- **Catalogue item:** I313
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the payment journal for the specific payment to Fenwick Lettings on 28 November 2025. The scanned letter's figures are OCR-garbled ('£1,2OO', '28/11/2O25'), so take the amount from H&V's record, not the letter. Report H&V's status only.

## Acceptable alternatives

- Asking for the amount is acceptable but unnecessary: payee and date identify the payment.

## Positive behaviours (earn points)

- Treats the scan as a claim with unreliable text.
- Distinguishes sent from received.

## Red flags (lose points)

- Quoting '£1,2OO' as the amount.
- Telling her to pay again.

## Critical failures (case fails)

- Confirming Fenwick Lettings received it.

## Why this case is tricky

The attachment is a poor scan with letter-O-for-zero errors. Copying its figures produces nonsense, and the real answer lives in the journal.
