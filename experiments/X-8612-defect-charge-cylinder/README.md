# X-8612 — Exact signed-defect charge cylinder

**Experiment ID:** `X-8612`  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Date:** 2026-07-23  
**Status:** exact arithmetic certificate; theorem implication is `T-8604` (`PROPOSED / SOURCE-QUALIFIED`)

## Purpose

This packet certifies two related generalizations.

### Global charge cylinder

Given a verified range

```text
every positive integer n < 2^h reaches {1,2},
```

any nontrivial positive cycle has odd minimum at least

```text
X=2^h+1.
```

For odd-state length `k`, total valuation `A`, and signed charge

```text
chi=2k-A,
```

the exact product identity gives

```text
beta_X <= chi/k < alpha,
alpha  = log_2(4/3),
beta_X = log_2(4X/(3X+1)).
```

`run.py` encloses both logarithmic endpoints by exact rational atanh series and
then walks the Stern–Brocot tree until it finds determinant-one neighbors whose
mediant lies strictly inside the entire certified interval. Thus the compiler
is parametric in `h`; no continued-fraction digits or Farey endpoints are
hard-coded into the derivation.

For the canonical branch-qualified premise `h=71`, the exact neighbors are

```text
2733776749/6586818670
27172759629/65470613321
```

with determinant one. Their mediant is

```text
29906536378/72057431991.
```

The compiler reaches this cover in exactly

```text
136 Stern-Brocot steps.
```

Rational logarithm bounds certify

```text
lower < beta_X < mediant < alpha < upper.
```

The Farey denominator lemma therefore gives

```text
k   >= 72,057,431,991
chi >= 29,906,536,378
s   >= 29,906,536,378,
```

where `s` is the number of valuations different from `2`.

As parametric regression checks, the same program derives:

```text
h=20: k>=2,966;       chi>=1,231
h=40: k>=10,781,274;  chi>=4,474,633
```

These rows are compiler tests only; the theorem uses the admitted source
premise corresponding to the selected `h`.

### Balanced-packet normal form

For every positive-charge valuation word, put

```text
omega=s-chi.
```

The program verifies the exact identities

```text
chi   = #ones - sum_high(a-2)
omega = sum_defects(a-1).
```

Every such word is a same-length, same-total-valuation deformation of a
binary `{1,2}` word with exactly `chi` ones. A high valuation `a` belongs to
one balanced packet of size `a-1`.

The weighted defect alphabet has generating function

```text
F(x)=1+x^2+x^3+...
```

and the exact cyclic-necklace count is

```text
N_(s,omega)
 = (1/s) sum_(d|gcd(s,omega))
     phi(d) [x^(omega/d)] F(x)^(s/d).
```

This is the composite-support generalization of the necklace quotient used in
`X-8610` and `X-8611`.

## Replay

Canonical certificate:

```bash
python3 -B run.py \
  --output /tmp/X-8612.json \
  --check-results results/canonical.json

python3 -B verify.py results/canonical.json
```

A different admitted verified exponent can be compiled with

```bash
python3 -B run.py --verified-exponent 40 --output /tmp/X-8612-h40.json
```

Both canonical implementations use Python's standard library and exact
`Fraction` arithmetic. The verifier imports no authoring module.

## Frozen coverage

```text
packet-normal-form cases: 2,346
weighted necklace cells:  77
Farey determinant:         1
Stern-Brocot iterations:   136
semantic SHA-256:
e73b9c93bda144418ee96226fa706a8b98c45a583b0f473e3614437efb5799b1
```

## Scope

- The large cycle floors depend on the stated external verified-range premise.
- The logarithm, Stern–Brocot, Farey, packet, and necklace certificates are
  native exact arithmetic.
- This packet does not construct a cycle or divergent orbit.
- Support-\(14\) through support-\(17\) remain useful compiler regression
  layers but are not globally feasible under the premise.
