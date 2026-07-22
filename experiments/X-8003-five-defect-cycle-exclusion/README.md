# X-8003 — five-defect cycle exclusion tables

A **defect** is an accelerated valuation different from `2`.

`T-8001` reduces the exactly-five-defect theorem to three finite interfaces:

1. the cyclic `{1,3}^5` modified-core table when at least two defects are high;
2. all-one largest-tail arrangements at neutral totals `R=8,9`; and
3. one-high determinant rows at neutral totals `0<=R<=5`.

Frozen exact totals:

```text
modified-core necklaces:        6
all-one arrangements:         290
one-high patterns:            345
one-high determinant resonances: 0
one-high powers tested:      3,347
height survivors:              53
exact divisor hits:              0
```

The independently written `verify.py` reconstructs the high-core rotations,
all-one rows, and one-high determinant table with a different coefficient
method.

```text
results SHA-256:
1d277736a3570ec64dae6884b175e807b457e89729b75ce25893fc008760d6b0
```

Replay:

```bash
python3 -B run.py --check-results results/canonical.json
python3 -B verify.py results/canonical.json
```
