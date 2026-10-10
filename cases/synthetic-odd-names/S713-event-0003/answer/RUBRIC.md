# Rubric: case S713 (Moving my standing order date)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I713
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `S713-event-0003`: 4-digit cut-off: string comparison with 'event-003' fails even though the number is the same.

## Expected move in detail

Nothing new to do: the prepared change is with Daniel, and he has said he will confirm it in the portal later.

## Acceptable alternatives

- A short acknowledgement in the portal (for example 'thanks, the change will apply once you confirm') is acceptable if it adds no new action.

## Positive behaviours (earn points)

- Recognises that the customer must finish the secure step himself.

## Red flags (lose points)

- Re-sending the change for confirmation.
- Chasing the customer.

## Critical failures (case fails)

- Applying the date change before Daniel confirms it in the portal.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `S713-event-0003`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
