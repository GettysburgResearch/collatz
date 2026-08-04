# X-8501 — Exact linear quotient-refund audit

**Status:** `EMPIRICAL / EXACT FINITE INTERFACE AUDIT`  
**Issue:** `#43`  
**Claims checked:** `L-8501`, `L-8502`, `T-8501`, `T-8502`, `T-8503`

## Purpose

The experiment checks the finite arithmetic interfaces used by the universal proofs:

1. exact fixed-width exponent formulas and least refund thresholds;
2. exact Väänänen–Wallisser cutoff certificates at dimensions `58/59`;
3. the inverse-carry base-`3^112` update;
4. all 16 connector cells at several heights;
5. the deterministic low-block/top-block decoder;
6. the width-one doubling bound on independently generated valid residuals;
7. the quadratic cylinder-depth formula.

It does not search for or claim a forever-defined residual.

## Replay

```bash
python3 -B derive.py \
  --output results/canonical.json \
  --summary results/summary.txt

python3 -B verify.py \
  --check-results results/canonical.json
```

Run from this experiment directory, or prepend the repository path.

## Frozen derivation summary

```text
refund widths: 10
least width-1 refund base: 3744
least width-256 refund base: 477424
periodic source cutoff: 58 (condition first fails at 59)
inverse-carry rows: 5
connector normal-form cases: 80
forced decoder cases: 384
doubling-growth cases: 384
decoder digest:
b3607db562e5db1cc449021f11d68283d6a4cd1c459e24104861ec137d050986
periodic phase-identity cases: 75284
cylinder-depth rows: 12
payload digest:
6328faaa680e54ab0245ba8cca41c81cebbb03ede1299b9d948d1fbf1aee41fd
```

## Independent implementation

`verify.py` does not import `derive.py`. It:

- recomputes stage exponents by direct sums rather than closed formulas;
- reconstructs connectors from the anchor equation;
- derives the inverse carry independently;
- decodes valid residuals using a separately written six-bit test;
- uses different heights, lifts, and cylinder horizons.

## Limitations

- finite checks do not prove the infinite theorems;
- no modular lasso is treated as an ordinary orbit;
- no finite seed is claimed to survive indefinitely;
- the external Väänänen–Wallisser theorem itself is not re-proved by code.
