# Synthetic cases with odd folder names

12 well-formed banking cases (catalogue items I708–I719, scenario EC468) whose only trap is the folder name: spaces, case, en dashes, suffixes, unicode, bare numbers, and one case whose files sit in an `inner/` subfolder. They test that the loader, evaluator and answer writer don't depend on the `S###-event-KKK` convention. They are kept out of `cases/synthetic/` so routine runs aren't affected.

    uv run evaluate.py --cases cases/synthetic-odd-names
