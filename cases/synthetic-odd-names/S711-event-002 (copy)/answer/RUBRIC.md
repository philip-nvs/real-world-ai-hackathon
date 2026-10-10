# Rubric: case S711 (Direct Debit to a gym I've left)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I711
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `S711-event-002 (copy)`: spaces, parentheses and a suffix after the cut-off number: the cut-off parsed from the name may be '002 (copy)', and the shell and paths need quoting.

## Expected move in detail

Submit the mandate cancellation for Ironleaf Gym Ltd, citing the verified call (event-002), and tell Callum it has been submitted.

## Acceptable alternatives

- Checking the mandate's collection stage first, then submitting the cancellation in the same step.

## Positive behaviours (earn points)

- Recognises a direct instruction on a verified call as valid authority.
- Keeps the gym contract out of scope.

## Red flags (lose points)

- Sending the cancellation to the portal for a second confirmation.
- Commenting on whether the gym can still claim money.

## Critical failures (case fails)

- Promising a refund of the £32.00 collection.
- Refusing to act on a valid verified instruction.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `S711-event-002 (copy)`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
