# X-8612 — Exact signed-defect charge cylinder

**Experiment ID:** `X-8612`  
**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Date:** 2026-07-23  
**Status:** exact arithmetic certificate; theorem implication is `T-8604` (`PROPOSED / SOURCE-QUALIFIED`)

## Purpose

This packet certifies two related generalizations.

### Global charge cylinder

Assuming the branch-qualified verified-range premise that every positive
integer below \(2^{71}\) reaches \(\{1,2\}\), any nontrivial positive cycle has
minimum at least

```text
X=2^71+1.
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

The exact Farey neighbors

```text
2733776749/6586818670
27172759629/65470613321
```

have determinant one, and their mediant is

```text
29906536378/72057431991.
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

```bash
python3 -B run.py \
  --output /tmp/X-8612.json \
  --check-results results/canonical.json

python3 -B verify.py results/canonical.json
```

Both implementations use Python's standard library and exact `Fraction`
arithmetic. The verifier imports no authoring module.

## Frozen coverage

```text
packet-normal-form cases: 2,346
weighted necklace cells:  77
Farey determinant:         1
```

## Scope

- The large cycle floors depend on the stated external verified-range premise.
- The logarithm and Farey certificates are native exact arithmetic.
- This packet does not construct a cycle or divergent orbit.
- Support-\(14\) through support-\(17\) remain useful compiler regression
  layers but are not globally feasible under the premise.
