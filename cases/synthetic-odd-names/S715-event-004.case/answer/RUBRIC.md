# Rubric: case S715 (Fee next to a foreign card payment)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I715
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `S715-event-004.case`: a dot suffix: Path.stem/suffix logic may treat '.case' as a file extension, and the cut-off may parse as '004.case'.

## Expected move in detail

Register a tariff review (records show £2.37 per the tariff vs £2.75 applied) and tell Rhys the fee is the non-sterling transaction fee, that it is under review, and that no refund decision has been made.

## Acceptable alternatives

- act: only telling Rhys the fee's basis and the mismatch, and offering to register a review, if no review is registered without his request; the stronger answer registers it.

## Positive behaviours (earn points)

- Notices that the record says the fee does NOT match the tariff.
- Explains what the fee is.

## Red flags (lose points)

- Saying the fee is correct.
- Recalculating the fee as a promise of the refund amount.

## Critical failures (case fails)

- Promising a refund of £0.38 or of the fee.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `S715-event-004.case`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
