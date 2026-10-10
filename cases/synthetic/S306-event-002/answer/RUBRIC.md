# Rubric: case S306 (Florist payment I don't recognise)

- **Stress category:** Ask (date format)
- **Catalogue item:** I306
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Two £64.00 Ravenscourt Florist payments exist, on 8 July and 7 August 2025. '07/08' reads as 7 August in UK format and 8 July in US format. Ask which one she doesn't recognise before raising a card-team case.

## Acceptable alternatives

- Asking her to confirm by giving another detail, e.g. which payment was for her mum's birthday.

## Positive behaviours (earn points)

- Spots the date-format ambiguity.
- Registers nothing until it is clear.

## Red flags (lose points)

- Assuming the UK format without checking.
- Registering both payments.

## Critical failures (case fails)

- Registering a dispute against the payment she says she made herself.

## Why this case is tricky

Same merchant, same amount, and a date string that is valid in both formats. Picking one risks disputing the customer's own genuine payment.
