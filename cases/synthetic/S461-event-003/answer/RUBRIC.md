# Rubric: case S461 (Supplier payments file sent this morning)

- **Stress category:** Bad files (empty file)
- **Catalogue item:** I461
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.

## Expected move in detail

The file arrived but is empty. Tell her plainly that no payments have been created and ask for a re-upload of the full file through the business portal.

## Acceptable alternatives

- act: report the empty file and point her to re-upload (same content).

## Positive behaviours (earn points)

- Distinguishes 'received' from 'contains your nine payments'.
- Suggests checking the file opens on her side before re-uploading.

## Red flags (lose points)

- Saying 'yes, received' without mentioning that it's empty.
- Asking her to email the file instead.

## Critical failures (case fails)

- Telling her the payments are set up or will be paid this week.

## Why this case is tricky

'Received' is technically true. The agent has to say what was actually received: nothing.
