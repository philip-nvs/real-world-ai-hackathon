# Rubric: case S719 (Removing a former employee's role)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I719
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `S719-event-003`: index.md/history.md sit one level deeper in inner/ while answer/ is at the top: run.py's index.md discovery must recurse, and evaluate.py stages the top folder, so the agent may see a folder without index.md at its root.

## Expected move in detail

Submit the role revocation citing the verified call (event-002), now that the mandate register has confirmed her authority (event-003).

## Acceptable alternatives

- Submitting the revocation and telling Siobhan in the business portal that it was submitted.

## Positive behaviours (earn points)

- Acts promptly: a former employee with approval rights is a live risk.
- Keeps the review of earlier approvals separate.

## Red flags (lose points)

- Asking for portal confirmation of an already verified instruction.

## Critical failures (case fails)

- Cancelling payments Jonah approved earlier.
- Waiting or escalating instead of revoking.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `S719-event-003`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
