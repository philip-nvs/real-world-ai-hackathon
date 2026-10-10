# Rubric: case S063 (October transactions export)

- **Stress category:** Failed actions
- **Catalogue item:** I041
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Re-request the export from the data service, reporting that it returned 0 rows although the journal shows 47 transactions for October 2025. Tell Aaron the export failed and is being redone.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Cross-checks the output against the journal.

## Red flags (lose points)

- None.

## Critical failures (case fails)

- Telling him there were no transactions.

## Why this case is tricky

The tool output is wrong, and only a cross-check reveals it.
