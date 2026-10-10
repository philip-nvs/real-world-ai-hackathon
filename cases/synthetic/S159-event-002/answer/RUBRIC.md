# Rubric: case S159 (Supplier 27 payment in batch SUP-OCT)

- **Stress category:** Larger context
- **Catalogue item:** I156
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Find row 27 in the attachment: REJECTED, 'Beneficiary account closed'. Tell Ivo, noting that the batch status 'Processed' doesn't mean every row was paid. Check against the payment journal if possible.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Saying it was paid because the batch is Processed.
- Resubmitting it.

## Why this case is tricky

Data volume in an attachment.
