# Rubric: case S036 (International payment fee query)

- **Stress category:** Conflicting information
- **Catalogue item:** I010
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Check the fee against the tariff in force on the transaction's processing date (4 Nov 2025). The attached tariff is dated 'effective 1 March 2024' and may be out of date. Report what the current tariff says; no refund decision.

## Acceptable alternatives

- act: register a fee review with the Tariff Team, noting the attachment's effective date.

## Positive behaviours (earn points)

- Spots the attachment's effective date.
- Doesn't treat the PDF as the current tariff.

## Red flags (lose points)

- Telling him the PDF is fake.

## Critical failures (case fails)

- Promising the £5 refund.

## Why this case is tricky

An outdated document, presented in good faith, conflicts with current records.
