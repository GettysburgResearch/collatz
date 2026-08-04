# X-9505 — H centered-renewal and boundary audit

**Experiment ID:** `X-9505`  
**Status:** `EMPIRICAL / EXACT FINITE CHECK`  
**Agent:** `gpt56-h-01`  
**Issue:** #17  
**Associated claims:** `L-9517`, `L-9518`; plateau observation only  
**Date:** 2026-07-22

## Research questions

1. Do all tested finite-code closure boundaries have negative real value?
2. Do exact finite cylinder starts satisfy the dual renewal bridge and the
   integral sign law at every pair of consecutive nonzero letters?
3. Does the central plateau equation

   \[
   W(8^R4^b-9^R3^a)=9^R-8^R
   \]

   admit a positive exact solution in a substantial finite exponent box?

The third question is exploratory. Failure to find a plateau is not a proof of
universal nonexistence.

## Command

```bash
python3 -B experiments/X-9505-h-renewal-bridge/run.py \
  --output experiments/X-9505-h-renewal-bridge/results/summary.json
```

## Frozen parameters

- every nonempty finite word of length at most `6` over `r=0,...,5` for the
  boundary-sign check;
- `20,000` deterministic pseudorandom exact words, lengths `2,...,30`, letters
  `0,...,10`, seed `9505`;
- plateau scan `1 <= R,a <= 300`, with every integer `b` in the exact narrow
  real window where a positive plateau core could occur;
- Python standard library only.

## Frozen output

```text
finite-code boundaries checked:       55,986
random exact words replayed:           20,000
renewal bridges checked:              269,845
renewal sign laws checked:            269,845
plateau real-window candidates:            94
exact positive plateau solutions:           0
```

SHA-256 digest:

```text
f5c6aaab56111fd2a3167dd44896473d421d51e17635b08fd41775f71c295777
```

## Interpretation

The exact checks support the self-contained proofs in `L-9517` and `L-9518`.
The plateau scan suggests a narrower Diophantine question for the successive
renewal-core system, but no universal plateau-exclusion claim is made.

## Limitations

- All word and exponent searches are finite.
- Random cylinder starts are exact but do not approximate a uniform measure on
  infinite ordinary orbits.
- The plateau search does not invoke logarithmic-form bounds and cannot exclude
  a solution beyond the frozen box.
- No ordinary infinite H orbit is constructed or excluded by this experiment.
