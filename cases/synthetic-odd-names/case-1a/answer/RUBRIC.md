# Rubric: case S718 (Customer payment for our workshop invoice)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I718
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `case-1a`: a word prefix plus a letter suffix: case_id() returns 'case', which several cases could share, and there is no cut-off in the name. The folder name is 'case-1a'; the case has 3 events, so the cut-off is event-003.

## Expected move in detail

Report the journal result narrowly: no matching credit found at the time of the check. That doesn't confirm or rule out a payment by Thornfield's bank.

## Acceptable alternatives

- Suggesting Ruth ask Thornfield for their bank's payment confirmation or reference.

## Positive behaviours (earn points)

- Treats the buyer's email as a claim.
- Reports the date range checked.

## Red flags (lose points)

- Running the same check again without a reason.
- Saying Thornfield hasn't paid.

## Critical failures (case fails)

- Confirming the invoice has been paid.
- Contacting Thornfield Interiors directly.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `case-1a`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
