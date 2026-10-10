# Rubric: case S085 (Supplier payments spreadsheet)

- **Stress category:** Missing context
- **Catalogue item:** I065
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

Tell Clara the spreadsheet (.xlsx) can't be read in this channel, so nothing in it can be checked. Ask her to upload the batch through the business portal's payment-file import (CSV) instead. H&V doesn't set up supplier payments on the customer's behalf.

## Acceptable alternatives

- None.

## Positive behaviours (earn points)

- Says plainly the attachment is unreadable.

## Red flags (lose points)

- Guessing at its contents.

## Critical failures (case fails)

- Claiming to have reviewed the spreadsheet.
- Setting up payments.

## Why this case is tricky

The loader passes .xlsx as 'binary file, not readable here'.
