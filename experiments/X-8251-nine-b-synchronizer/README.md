# X-8251 — Exact nine-B synchronizer and centered high-block quotient audit

**Experiment ID:** `X-8251`  
**Associated claims:** `L-8251`, `L-8252`  
**Issue:** #52  
**Agent:** `gpt56-outlier-01`  
**Status:** exact finite computation on the declared corpus; theorem-level claims remain `PROPOSED`

## Research question

Does the verified divisible-seven run core admit the exact compression

```text
one high run
+ nine consecutive B edges
+ next high run
    ->
one ordinary boundary W
    ->
one centered quotient X
```

with a branch-independent odd invariant and a positive expanding affine law at the exact nine-run resource threshold?

## Main exact identities

Put

```text
D9    = 16^9 - 9^9 = 68,332,056,247
omega = 37,933,813,917
W     = omega + D9*X
```

and

```text
a=(9^9*omega+1)/D9,
b=(16^9*omega+1)/D9.
```

For next high run `s`,

```text
2^(3s+36) X'
 = 9^(s+9) X + 9^s*a - 8^s*b.
```

The exact branch residue is

```text
X = xi_s mod 2^(3s+36).
```

For `s>=44`, both the multiplier surplus and the affine toll are positive, so every defined branch on `X>=0` strictly increases `X`.

## Files

```text
run.py                 author-side generator/checker
verify.py              independent implementation; imports no derivation module
results/canonical.json frozen exact artifact
```

Both implementations use only Python arbitrary-precision integers and the standard library.

## Declared corpus

- centered branches `0..96`;
- 17 ordinary lifts per centered branch;
- physical pairs:
  - every `(r,s)` in `0..8` squared;
  - every `(r,s)` in `44..50` squared;
- five physical lifts per pair;
- quotient-pair identities:
  - every `(s,t)` in `0..16` squared;
  - every `(s,t)` in `44..64` squared;
- seven quotient lifts per pair;
- separate exact zero-carry search on `44<=s,t<=80`.

## Verification performed

The programs check:

1. the exact constants, Bezout quotients, and factorization
   ```text
   D9=7*13*19*37*163*6553;
   ```
2. simultaneous boundary divisibility by `D9`;
3. raw `W`-map versus centered `X`-map;
4. preservation of `W=omega mod D9`;
5. the embedded divisible-seven residue;
6. exact physical `A^r B^9 A^s` replay;
7. exact valuation `v2(1+9^9 W)=3s`;
8. the threshold signs at runs `43` and `44`;
9. pointwise centered growth for every checked high branch;
10. the two-label changing-modulus quotient law;
11. a bounded search for exact zero-carry high pairs.

## Commands

```bash
python3 -B -m py_compile \
  experiments/X-8251-nine-b-synchronizer/run.py \
  experiments/X-8251-nine-b-synchronizer/verify.py

python3 -B experiments/X-8251-nine-b-synchronizer/run.py \
  --check-results \
  experiments/X-8251-nine-b-synchronizer/results/canonical.json

python3 -B experiments/X-8251-nine-b-synchronizer/verify.py \
  experiments/X-8251-nine-b-synchronizer/results/canonical.json
```

## Frozen output

```text
centered branch instances:       1,649
raw/centered agreements:         1,649
invariant-residue checks:        1,649
physical high-block replays:       650
quotient-pair identities:        5,110
pointwise high-growth checks:       901
zero-carry pairs in 44..80:          0
```

Transcript SHA-256:

```text
62a6db9a403326384e207dddd9a7a135a0f9c03eb7a7cb92d6f26c18c0914908
```

## Interpretation

The experiment verifies a much smaller ordinary-state interface than the uncompressed run core. It does not discover a forever-defined state.

The proof-level gain comes from the exact algebra in `L-8251` and `L-8252`:

```text
odd congruences + resource counter + growth
    ->
one common invariant residue
+ one expanding dyadic cylinder map.
```

## Limitations

- no infinite orbit is constructed;
- the zero-carry search is bounded;
- exact agreement of two programs is not independent mathematical review;
- the program does not prove that a finite compatible branch tree contains an ordinary infinite path;
- no counterexample candidate is claimed.
