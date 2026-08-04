# Eureka report — signed charge cylinder and balanced defect packets

**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`  
**Date:** 2026-07-23

## Objective

Continue the full counterexample program after the exact centered-defect
exclusions through support seventeen, re-read the live repository, and seek a
general parameter that scales beyond another bounded support census.

## Repository refresh

The newest cartography pass showed that the project has converged to two
funnels:

1. exact ordinary changing-modulus refund machines, whose only positive gap is
   most-significant ordinary routing;
2. full-denominator positive-cycle synthesis.

The new cycle inputs were:

- PR #45's proposed exact exclusion through 50,000 odd states;
- the external verified range below \(2^{71}\), recorded branch-qualifiably by
  PR #12;
- PR #42's centered-defect compiler through support seventeen;
- PR #47's normalized centered half-join;
- PR #53's resultant finiteness for fixed pulse cones;
- PR #34's prime-power compatibility compiler.

The cartography had already combined the 50,000-state floor with the crude
support inequality to obtain a proposed support floor of 17,397. The present
pass looked for the exact quantity behind that inequality.

## Eureka 1 — the signed defect charge

For a valuation word of odd length `k` and total valuation `A`, define

```text
chi=2k-A.
```

This is the global dyadic deficit from the all-`2` word. If `p` valuations are
`1`, then

```text
chi=p-sum_(a>=3)(a-2).
```

For support `s`, define

```text
omega=s-chi.
```

Then exactly

```text
omega=sum_(a!=2)(a-1).
```

So every support/defect-sum cell is really a charge/slack cell:

```text
B=s+omega,
chi=s-omega.
```

This makes the previously unbounded high alphabet finite automatically:

```text
number of high defects <= floor(omega/2),
maximum high valuation <= omega+1.
```

## Eureka 2 — balanced packet deformation

Every positive-charge word can be converted to a binary `{1,2}` word of the
same length and total valuation:

- replace each high `a` by `2`;
- replace `a-2` distinct one-positions by `2`.

The base has exactly `chi` ones. The number of changed positions is exactly
`omega`. Conversely, the original word is recovered by disjoint balanced
packets.

Thus the full cycle compiler has the hierarchy

```text
(k,chi)
 -> binary base with chi ones
 -> packet slack omega
 -> partition of omega into parts >=2
 -> cyclic packet placement
 -> neutral gaps
 -> full denominator.
```

This is a profound change from enumerating arbitrary defect alphabets.

## Eureka 3 — exact 72-billion-state charge cylinder

Assume the repository's branch-qualified external premise:

```text
every positive n<2^71 reaches {1,2}.
```

A nontrivial cycle minimum is then at least

```text
X=2^71+1.
```

The product identity places every cycle charge ratio in

```text
beta_X <= chi/k < alpha,

alpha  = log_2(4/3),
beta_X = log_2(4X/(3X+1)).
```

The width is about `2.04e-22`, but the proof uses rational logarithm
enclosures.

The exact fractions

```text
L= 2733776749/6586818670
U=27172759629/65470613321
```

satisfy determinant one. Their mediant is

```text
M=29906536378/72057431991.
```

`X-8612` certifies

```text
L < beta_X < M < alpha < U.
```

Every reduced rational between determinant-one neighbors has denominator at
least the denominator sum. Therefore:

```text
odd-state length >= 72,057,431,991
signed charge   >= 29,906,536,378
non-2 support   >= 29,906,536,378.
```

This is source-qualified, not an unconditional theorem independent of the
verified range. It is nevertheless an exact native consequence of the premise
and improves the repository's prior proposed 17,397 support floor by more than
six orders of magnitude.

## Weighted necklace generalization

A defect `1` has slack weight zero and a high defect `a` has weight `a-1`.
Therefore

```text
F(x)=1+x^2+x^3+...
```

is the defect alphabet. If `c_(s,w)=[x^w]F(x)^s`, Burnside gives

```text
N_(s,w)
 =(1/s) sum_(d|gcd(s,w)) phi(d)c_(s/d,w/d).
```

This is an exact necklace formula for every composite support, replacing the
prime-support shortcut used at support seventeen.

The independent audit agrees with brute cyclic enumeration in 77 small cells.

## Candidate counterexamples

None.

No full-denominator divisibility hit or ordinary divergent initialization was
found. No `K-####` object is created.

## Correctness hardening

The earlier support-\(14\) through support-\(17\) fast modular programs contain
ordinary unsigned residue additions in cells whose modulus can approach
`2^64`. This pass also prepares a widened modular-addition repair. The theorem
files and canonical zero counts remain unchanged; the source hardening must be
committed and replayed before those near-`2^64` rows are considered fully
publication-ready.

## Files in this packet

```text
research/compressed-cycle-synthesis/claims/
  L-8605-signed-defect-charge-normal-form.md
  T-8604-source-qualified-charge-cylinder.md

experiments/X-8612-defect-charge-cylinder/
  README.md
  run.py
  verify.py
  results/canonical.json

reports/gpt56-cycle-01/
  2026-07-23-9-signed-charge-cylinder.md
```

## Next full-objective work

### Cycle funnel

Use the charge/slack hierarchy, not low support:

1. generate near-critical binary bases with the exact Farey charge cylinder;
2. attach finite balanced packets by slack partition;
3. quotient cyclic packet placements with the weighted Burnside formula;
4. enforce the full denominator factorwise and reconstruct every hit.

### Divergent-orbit funnel

The same structural lesson applies to refund machines. The relevant object is
not a raw future digit stack but an inverse-affine transported charge/carry
coordinate. A useful common theorem would express ordinary top-boundary
definedness as a balanced packet or determinant-one cylinder, then either
construct one finite root or prove a height ranking.

## Status

- `L-8605`: `PROPOSED / EXACT ALGEBRAIC NORMAL FORM`;
- `T-8604`: `PROPOSED / SOURCE-QUALIFIED EXACT CERTIFICATE`;
- `X-8612`: exact finite/rational computation;
- no counterexample claimed.
