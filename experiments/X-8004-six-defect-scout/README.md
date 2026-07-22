# X-8004 — bounded six-defect scout

This is the first exact finite scout beyond `T-8001`.

Scope:

```text
exactly six valuations different from 2
0 <= total neutral 2s <= 10
at most two high defects
each high valuation in 3..12
one largest neutral gap rotated to the terminal position
```

Frozen result:

```text
2,616,236 exact words
440 pass D>0 and E_core>=2D
0 exact divisor hits
```

This is bounded evidence only.  Its purpose is to identify the next theorem
shape: the first unresolved modified cores contain two separated high defects,
for which the five-defect `<2` comparison can fail.

Replay:

```bash
python3 -B run.py --check-results results/canonical.json
```
