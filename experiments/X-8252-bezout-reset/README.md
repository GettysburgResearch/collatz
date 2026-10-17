# X-8252 — Exact Bézout-reset and canonical-exponent isometry audit

**Experiment ID:** `X-8252`  
**Associated claims:** `L-8253`, `L-8254`  
**Issue:** #52  
**Agent:** `gpt56-outlier-01`  
**Status:** exact finite computation on the declared corpus; theorem-level claims remain `PROPOSED`

## Research question

Does the centered nine-B machine reduce exactly to:

```text
Y=a+9^9 X;
q=v2(Y)=3s;
u=Y/2^q;
fixed gate 9^(s+9)u=-1 mod2^36;
Y'=(9^(s+9)u+1)/2^36,
```

and does varying a canonical initial label in one exact arithmetic progression give a `2`-adic isometry capable of compiling every finite future cylinder?

## Main exact identities

The constants satisfy

```text
2^36*a - 9^9*b = 1,
a=215,072,362,
b=38,148,886,279.
```

For a defined branch:

```text
Y=2^(3s)u,
9^s u = b+2^36 X',
Y'=a+9^9 X'.
```

Equivalently,

```text
9^s(a+9^9X)=8^s(b+2^36X').
```

All labels `s>=44` share the exact 132-bit prefix

```text
X=598051932619127473212326704339812739814 mod2^132.
```

For

```text
L=2^33*3^16=369,768,517,790,072,832,
```

canonical units are constant on `s=r+Lk`, and the canonical-output map

```text
H_r(k)=[9^(r+Lk+9)u_r+1]/2^36
```

obeys

```text
v2(H_r(k)-H_r(l))=v2(k-l).
```

Hence it permutes every ring `Z/2^h Z` and compiles any finite high-word cylinder into one exponent residue.

## Files

```text
run.py                 author-side generator/checker
verify.py              independent implementation; imports no derivation module
results/canonical.json frozen exact artifact
```

Both implementations use only Python arbitrary-precision integers and the standard library.

## Declared corpus

- reset branches `s=0..96`;
- 17 ordinary lifts per branch;
- high-prefix checks `s=44..96`;
- isometry bases `r in {44,64,96}`;
- all unordered pairs in `0..63` at 24-bit precision;
- complete permutation checks modulo `2^4`, `2^8`, and `2^12`;
- six deterministic finite future high words;
- canonical-output extension audit for `s=44..512`.

## Verification performed

The programs check:

1. `2^36*a-9^9*b=1`;
2. the centered branch against the reset `Y` branch;
3. intrinsic recovery `s=v2(Y)/3`;
4. the fixed 36-bit normalized-unit gate;
5. automatic return to `Y=a mod9^9`;
6. the exact two-base digit exchange;
7. pointwise high growth;
8. the common 132-bit prefix and its exact loss at label `44` versus every larger checked label;
9. the exact multiplicative orders
   ```text
   ord_(2^36)(9)=2^33,
   ord_(9^9)(8)=2*3^16;
   ```
10. `v2(9^L-1)=36`;
11. the isometry and finite-ring permutation claims;
12. six finite-word compiler instances;
13. a bounded canonical-output high-extension audit.

## Commands

```bash
python3 -B -m py_compile \
  experiments/X-8252-bezout-reset/run.py \
  experiments/X-8252-bezout-reset/verify.py

python3 -B experiments/X-8252-bezout-reset/run.py \
  --check-results \
  experiments/X-8252-bezout-reset/results/canonical.json

python3 -B experiments/X-8252-bezout-reset/verify.py \
  experiments/X-8252-bezout-reset/results/canonical.json
```

## Frozen output

```text
reset branch agreements:         1,649
intrinsic-label checks:           1,649
fixed-gate checks:                1,649
digit-exchange checks:            1,649
high-growth checks:                 901
common-prefix checks:               901
isometry pairs:                   6,048
finite-ring permutation rows:         9
finite-word compilers:                6
bounded canonical high extensions:    0
```

Transcript SHA-256:

```text
98b4dd43c79f3739b19a1498ca7c59c4250e56ec799732beadba86353eb39fc1
```

The bounded canonical audit found maximum next valuation `11`, at initial label `435`, over `44<=s<=512`; it is not extrapolated.

## Interpretation

The experiment verifies two distinct advances.

First, the branch table collapses to one fixed 36-bit gate around a rational `2`-adic center.

Second, arbitrary finite high futures can be compiled into one ordinary exponent residue because the exponent-to-output map is an exact isometry.

Neither fact proves that the nested exponent residue has finite binary support for an infinite future word.

## Limitations

- no forever-defined ordinary state is found;
- the finite-word compiler does not promote a `2`-adic limit to an ordinary exponent;
- the canonical-output search is bounded;
- agreement of two programs is not independent mathematical review;
- no counterexample candidate is claimed.
