# T-9420 — Withdrawn rationality-periodicity classification

Claim ID: `T-9420`  
Title: Rationality was not shown to force eventual periodicity because the tail-state height bound used the wrong completion  
Status: `WITHDRAWN — INVALID PROOF; STATEMENT OPEN`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Withdrawn: 2026-07-22  
Dependencies audited: `D-9401`, `L-9402`, `L-9417`  
Scope: binary survivor codes  
Related counterexample candidates: none

## Withdrawn statement

The previous version claimed

```text
Phi(epsilon) in Q
 <=> epsilon is eventually periodic.                 (1)
```

Only the reverse implication is currently proved:

```text
eventually periodic epsilon
 -> Phi(epsilon) in Q.                                (2)
```

The forward implication remains open.

## First invalid inference

`L-9417` validly proves that if the `2`-adic digit-tail values are rational,
their reduced denominators divide one fixed odd integer `B`.

The withdrawn proof then placed those rational `2`-adic values in the compact
real interval

```text
[0,81/17].                                            (3)
```

But (3) bounds the **real limits** of the positive digit-series partial sums,
not the rational values of their `2`-adic limits. The two completion values
need not agree. Thus fixed denominators do not leave finitely many possible
`2`-adic tail states: their ordinary numerators may be unbounded.

Without finiteness, no repeated tail state and no eventual periodicity follow.

## What remains valid

1. Every eventually periodic code has the rational geometric expression
   ```text
   finite prefix + T^r P(T)/(1-T^s).
   ```
2. `L-9417` gives a descending divisor chain for rational `2`-adic digit-tail
   denominators.
3. `L-9402` gives exact code injectivity.

These three facts do not currently combine into the converse of (2).

## Why the claim would have been unusually strong

A proof of (1) would classify every rational point of the full binary
`64 -> 81` attractor and would immediately transform the M1 question. Such a
classification requires genuine numerator/height control and cannot follow
from a denominator chain alone.

## Dependency audit

- `L-9417` remains valid after its completion convention is corrected.
- `L-9402` remains valid.
- `T-9421` depended on the withdrawn forward implication and is withdrawn.
- No native Padé or source-dependent periodic theorem is affected.

## Suggested next attack

Seek a second coordinate that bounds the ordinary numerators of rational
`2`-adic tails. PR #16's centered nearest-integer blocks, an ordinary tail-state
assumption, or a two-tail product-formula determinant may supply that missing
height. Until then, rationality versus eventual periodicity remains open.
