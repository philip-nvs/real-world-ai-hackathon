# Rubric: case S174 (Payroll row 4)

- **Stress category:** Larger context
- **Catalogue item:** I171
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Point out the pattern: row 4 has been rejected for 'beneficiary name mismatch' three months running, so the employee's name on file doesn't match their bank's records. Nia should update that payee's name (or check it with the employee) before resubmitting just that row.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- None.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Resubmitting the whole batch.
- Telling her it's H&V's fault without evidence.

## Why this case is tricky

Pattern recognition across months.
