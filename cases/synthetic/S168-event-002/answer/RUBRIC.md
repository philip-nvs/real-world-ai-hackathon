# Rubric: case S168 (Credit card bill paid twice)

- **Stress category:** Larger context
- **Catalogue item:** I165
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Cite clause 14.3: if H&V makes a payment from his account by mistake, it will refund it within 1 business day of finding the error. The journal flags the second £310 as a system duplicate, so raise an internal request for the correction and tell Faisal what the terms say. Don't give a date beyond the terms.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Finds the specific clause in the long PDF.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Paraphrasing the wrong clause.
- Inventing terms.

## Why this case is tricky

Long document; the needed clause is buried in it.
