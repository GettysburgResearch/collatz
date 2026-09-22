# X-9612 — Exact 1,024-block mechanical-library audit

## Purpose

This experiment freezes the finite base library used by `T-9608`.

Starting from the lower mechanical valuation word of slope `19/30`, it independently toggles ten pairwise disjoint adjacent swaps. The resulting `2^10=1,024` blocks all have the common summary

```text
odd-state length k = 30,
total valuation A = 49,
P = 3^30,
Q = 2^49,
D = Q-P.
```

The experiment verifies exactly that:

```text
all 1,024 chronological blocks have the same summary;
all 1,024 affine constants are distinct;
the adjacent-swap correction formula is exact;
the total constant span is 488,696,643,722,610 < 2^49;
no base constant is divisible by D;
the complete variant/residue transcript has the frozen SHA-256 digest.
```

## Logical boundary

`X-9612` is load-bearing only for the finite 1,024-block alphabet. It does **not** scan or extrapolate over repetition length.

The theorem for every ordered word over the alphabet and every `R>=1` is the mathematical carry-rigidity result `L-9608`, specialized in `T-9608`. That theorem proves that the narrow numerator diameter forces every full-denominator hit to use one constant block class at every position; the finite audit then rejects all 1,024 possible pure classes.

No positive cycle, divergent orbit, or Collatz conclusion outside this exact grammar is claimed.

## Replay

```bash
python3 -B experiments/X-9612-1024-block-library/run.py \
  --check-results \
  experiments/X-9612-1024-block-library/results/canonical.json

python3 -B experiments/X-9612-1024-block-library/verify.py \
  experiments/X-9612-1024-block-library/results/canonical.json
```

Both programs use only the Python standard library. `verify.py` does not import `run.py`; it reconstructs the mechanical word, all 1,024 variants, every affine constant, all residues, the correction vector, and the transcript digest independently.

## Frozen headline values

```text
variant count:                1,024
distinct constants:           1,024
minimum constant:             2,139,808,101,293,981
maximum constant:             2,628,504,745,016,591
constant span:                  488,696,643,722,610
Q=2^49:                         562,949,953,421,312
single-block divisor hits:                           0
transcript SHA-256:
d21492c18b71f2dbb4869357f746c3a04b44818e9f008dfaba67070494fbc95a
```
