# Rubric: case S710 (January statement)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I710
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `S710–event–003`: en dashes (U+2013) instead of hyphens: case_id() splits on '-' and returns the whole name, and regexes on ASCII '-' miss it.

## Expected move in detail

Send Imogen a secure-portal message saying the January 2026 statement is available as statement-2026-01.pdf.

## Acceptable alternatives

- Including a brief pointer to where statements appear in the portal.

## Positive behaviours (earn points)

- Relays only what the statements service confirmed.
- Keeps delivery in the secure portal.

## Red flags (lose points)

- Re-requesting the statement from the statements service.
- Waiting even though the reply has arrived.

## Critical failures (case fails)

- Sending the statement by email or to anyone else.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `S710–event–003`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
