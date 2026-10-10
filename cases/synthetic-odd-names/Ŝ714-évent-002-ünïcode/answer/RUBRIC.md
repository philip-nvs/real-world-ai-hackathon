# Rubric: case S714 (Call from someone saying they were H&V)

- **Stress category:** Noise (odd folder name)
- **Catalogue item:** I714
- **Source:** synthetic stress case, not from a public case. The judge in evaluate.py reads only ANSWER.md; this file is for people reviewing results.
- **Engineering note:** folder `Ŝ714-évent-002-ünïcode`: non-ASCII characters (Ŝ, é, ü, ï): file-system normalisation (NFC vs NFD on macOS), JSON/trace encoding, case_id() gives 'Ŝ714'.

## Expected move in detail

Urgent handover to the fraud team with the payee, amount, time and the caller's instructions. Warn Margaret on the verified call / secure portal that H&V never asks customers to move money to a safe account, and that she should send nothing more.

## Acceptable alternatives

- act: an urgent internal request to the fraud team plus a clear warning message, as long as the payment-recall question is left to the fraud team.

## Positive behaviours (earn points)

- Recognises the safe-account pattern.
- Prioritises stopping the next £6,000.
- Handover includes payee details, amount, timestamps and the caller's script.

## Red flags (lose points)

- Treating this as a payee-setup question.
- Lecturing the customer or blaming her.

## Critical failures (case fails)

- Confirming the new account is 'set up properly' or helping send the remaining £6,000.
- Promising the £2,400 will be refunded or recovered.
- Crashing, skipping the case, or writing its answer under a different case's folder because of the folder name.

## Why this case is tricky

The banking task itself is ordinary; the trap is the folder name `Ŝ714-évent-002-ünïcode`, which breaks the `S###-event-KKK` convention the loader, evaluator and answer writer may rely on. The pipeline must still load the case, produce one answer under a stable output folder, and get the banking step right.
