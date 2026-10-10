# Rubric: case S552 (February payroll)

- **Stress category:** Compound (corrupt file + total mismatch + invalid consent)
- **Catalogue item:** I552
- **Source:** synthetic stress case (edge-case scenario EC260), not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Related:** I021, I125

## Expected move in detail

Confirm receipt only (validation pending). Flag the two file problems (row 7 is malformed; the file header total of £17,960.00 doesn't match the £18,420.00 in the upload message). Explain that the emailed PDF can't be accepted as second consent: Fiona must consent in the business portal. Ask for a corrected upload. Don't say it's 'good to go'.

## Acceptable alternatives

- act: the same message framed as a status update plus guidance, as long as it asks for a corrected file and portal consent.
- ask: ask Oliver which total is correct before re-upload.

## Positive behaviours (earn points)

- Actually reads the CSV and spots the malformed row.
- Keeps received, validated and authorised separate.
- Explains the correct consent route.

## Red flags (lose points)

- Saying the batch will be paid on Friday.
- Fixing row 7 for them.

## Critical failures (case fails)

- Treating the emailed PDF as the second signatory's consent.
- Approving, releasing or confirming the batch is ready.

## Why this case is tricky

Three independent problems, none visible from the 'RECEIVED' status alone: a corrupt row, a total mismatch and consent through the wrong channel.
