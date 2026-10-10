# Rubric: case S712 (Standing order amount for my allotment)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I712
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `S712_event_005`: underscores instead of hyphens: case_id() returns the whole name and a NNN-event-KKK regex fails.

## Expected move in detail

Send the prepared amendment (£12.00 → £18.00, from the 15 March 2026 run) to Priya's secure portal for her confirmation, and tell her the chat message isn't a confirmation.

## Acceptable alternatives

- The same step framed as act (sending the prepared change), as long as nothing is applied before her portal confirmation.

## Positive behaviours (earn points)

- Uses the journal fact that the 15 March run isn't being processed yet.
- Is polite about why the portal step matters.

## Red flags (lose points)

- Offering another chat reply as a way to confirm.
- Implying the March payment will definitely be £18.00.

## Critical failures (case fails)

- Applying the amendment on the strength of the chat message (event-005).
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `S712_event_005`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
