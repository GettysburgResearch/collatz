# X-6230 — the status of issue #10's sanctuary target

```text
Experiment ID:   X-6230
Agent:           claude-opus5-61
Claims:          T-6230
Serves:          issue #10
Runtime:         seconds
```

Establishes that a forward-invariant set avoiding 1 consists entirely of counterexamples, that
its minimum is exactly the `T-6170` object whose boundedness is the conjecture, and that no
union of residue classes qualifies (checked for every class and every modulus `2..64` by
explicit small witness).

```sh
python3 sanctuary.py
```

See T-6230 for the statement, proof and gap audit — including the point that this does **not**
show a sanctuary cannot exist, only that building one entails exhibiting a counterexample.
