# R-9404 — Unequal phase allocation does not repair period four

Claim ID: `R-9404`  
Title: Refutation of the phase-reallocation shortcut for the block Gaussian-binomial Padé family  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-9411`, `T-9416`  
Scope: one-root-product denominators with phasewise cancellation windows  
Related counterexample candidates: none

## Refuted inference

The following proposed repair of `R-9403` is false:

> The period-four exponent misses one only because `L-9410` allocates the same
> number of cancellation equations to all four phases. Give more roots to the
> difficult phases and fewer to the cheap phases; the resulting universal
> exponent will exceed one.

## Exact resolution

`L-9411` constructs the complete unequal-allocation root-product family. If the
asymptotic fractions of cancellation roots are

```text
p_0,...,p_(r-1),
sum p_j=1,
```

`T-9416` proves that its guaranteed first-phase valuation-to-height shape obeys

```text
min_j e_j(p)/h(p)
 <=(r^2+r+1)/(r(r+1)),
```

with equality only when every `p_j=1/r`.

Therefore equal allocation is not a convenience or an avoidable symmetry loss.
It is the unique optimum in the entire phasewise root-product class. At period
four the best possible universal exponent in this class remains

```text
mu_4=0.993714361875...<1.
```

## What is not refuted

This result does not exclude:

- common-factor reduction of the final rational approximant;
- exact cancellation between different first surviving phases;
- adjacent-order determinants;
- Hermite–Padé systems with genuinely coupled polynomial components;
- phase-sensitive constructions using the actual transfer polynomial `P_W`;
- period-four irrationality or the balanced nonperiodic frontier.

Those are now the only honest continuation routes. Merely moving the same roots
between phases is closed.

## Verification

`X-9410` checks 657,774 finite integer allocations. Every maximizer is balanced,
and every exact functional is below the theorem bound. The finite census is an
interface check only; `T-9416` is the proof.

## Process consequence

Future Padé experiments should declare whether their denominator is a single
phasewise root product. If it is, `T-9416` supplies the asymptotic ceiling and a
large computation cannot change it.