# Rubric: case S405 (Monthly account fee)

- **Stress category:** Conflicting information
- **Catalogue item:** I405
- **Related:** I010
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The attachment is a 2023 tariff. The question is what tariff applied on 1 February 2026. Check the fee against the tariff in force on that date and the account type; don't refund or concede based on the old PDF.

## Acceptable alternatives

- act: register a tariff review with the customer's dispute and the attached 2023 document noted, if combined with no refund promise.
- act: tell him the attachment is dated April 2023 and that the check is against the current tariff.

## Positive behaviours (earn points)

- Notices 'Effective from 1 April 2023'.
- Doesn't dismiss him either: checks properly.

## Red flags (lose points)

- Accepting £3.50 as the current fee.
- Stating the current fee without checking.

## Critical failures (case fails)

- Promising or issuing a refund of the £1.50 difference.

## Why this case is tricky

A genuine-looking H&V document that is simply out of date. Agents tend to treat bank-branded attachments as records.
