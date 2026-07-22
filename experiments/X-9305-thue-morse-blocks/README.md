# X-9305 — Exact Thue--Morse appended-block audit

**Experiment ID:** X-9305  
**Status:** EMPIRICAL / exact finite interface audit  
**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Associated claims:** `T-9316`, `L-9314`  
**Date:** 2026-07-22

## Research question

The wave-5 literature audit identifies Thue--Morse sign words as the equality/extremal patterns that must be translated into the native nearest-integer block recurrence.

For the Thue--Morse itinerary

```text
e_n = popcount(n) mod 2,
```

this audit asks:

1. do the exact finite nearest-integer cylinders and appended base-64 blocks replay correctly?;
2. where do zero appended blocks occur in a bounded prefix?;
3. do the self-similar square witnesses used by `T-9316` replay exactly?

The experiment is not a proof of nonstabilization. `T-9316` proves nonstabilization from the efficient square family.

## Exact recurrence

For digits `e_0,...,e_(K+1)`, put

\[
d_K=e_K-e_{K+1}.
\]

The nearest integers satisfy

\[
64B_{K+1}=81B_K+d_K.
\]

A prefix through transition `K-1` selects one initial cylinder

\[
B_0\equiv R_K\pmod{64^K}.
\]

Writing

\[
R_{K+1}=R_K+q_K64^K,
\qquad0\le q_K<64,
\]

`L-9314` gives

\[
q_K
\equiv
-81^{-(K+1)}(81C_K+d_K)
\pmod{64},
\]

where `C_K` is the terminal nearest integer of the length-`K` cylinder.

The script checks this recurrence using exact integers at every transition. It independently reconstructs the full residue formula through depth 32 and at the power-of-two checkpoints 64, 128, 256, 512, and 1024.

## Thue--Morse square witnesses

The fixed point begins

```text
01101001...
```

and has `11` at zero-based positions `1,2`. Applying the length-two morphism repeatedly gives equal adjacent factors of length `2^m` at starts

```text
1*2^m and 2*2^m.
```

The script verifies every such witness fitting in the frozen prefix, through `m=8` and factor length `256`.

This is the sharper witness used by the current `T-9316`. It improves the recurrence ratio from the earlier starts `5*2^m,6*2^m` to `1*2^m,2*2^m`.

## Replay

```bash
python3 -B -m py_compile experiments/X-9305-thue-morse-blocks/run.py
python3 -B experiments/X-9305-thue-morse-blocks/run.py \
  --check-results \
  experiments/X-9305-thue-morse-blocks/results/canonical.json
```

## Frozen result

Through block index `1024`:

```text
blocks checked   = 1024
nonzero blocks   = 1005
zero blocks      = 19
longest zero run = 1
```

The zero positions are

```text
65, 88, 135, 137, 179, 196, 233, 254, 302, 320,
329, 423, 504, 514, 659, 706, 781, 913, 956.
```

The canonical payload SHA-256 is

```text
c5a7bfb2cc674c5aba9ada80f291d69c79a2a4151d2eba22c784ea3ae64b59dc
```

## Interpretation

The finite data are consistent with `T-9316`: zero blocks occur, but there is no finite sign of an eventual zero tail. The theorem does not depend on this pattern. It uses the explicit self-similar square family and the ordinary recurrence cone.

The experiment is useful as a regression suite for any future translation of a Dubickas extremal sign convention into native digits and blocks.

## Limitations

- Only the first 1024 block extensions are checked.
- Finite nonzero blocks do not prove infinitely many nonzero blocks.
- The exact Dubickas equality language for `(81,64)` has not been acquired or asserted.
- No positive centered parameter, ordinary survivor, or Collatz counterexample is constructed.
