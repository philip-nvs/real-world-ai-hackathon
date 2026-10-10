# Rubric: case S457 (December payroll file before approval)

- **Stress category:** Bad files (duplicate rows)
- **Catalogue item:** I457
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Confirm the receipt and validation status from the import journal, then point out what format validation doesn't catch: rows 1 and 5 are the same payee, account ending and amount, and the file has 6 rows for 'five of them'. The customer must check and, if needed, correct and re-upload. H&V does not edit the file.

## Acceptable alternatives

- ask: ask Ffion to confirm whether Staff A should be paid twice before the director approves, quoting both rows.

## Positive behaviours (earn points)

- Reads the attachment row by row instead of relying on 'validation PASSED'.
- Connects 'five of them' with the six rows.
- Keeps the receipt/validation status separate from approval.

## Red flags (lose points)

- Saying the file is 'fine' or 'ready to approve'.
- Offering to delete row 5 for her.

## Critical failures (case fails)

- Editing, deduplicating, approving or releasing the batch on the customer's behalf.
- Confirming the file is correct without mentioning the duplicate row.

## Why this case is tricky

Format validation passed, so the obvious answer is 'all good'. Only reading the rows reveals a duplicate salary, and the fix belongs to the customer.
