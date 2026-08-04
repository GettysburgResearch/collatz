# O-8801 — Fair-parity drift threshold

Claim ID: O-8801  
Title: Exact model drift changes sign between `3x+1` and `5x+1`  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801  
Scope: independent fair-bit multiplicative model only  
Related counterexample candidates: issue #26; no orbit-level claim

## Statement

In the model that chooses the even and odd shortcut branches independently with
probability `1/2`, the expected base-`2` logarithmic multiplier for `T_a` is

```text
lambda_fair(a)
 = (1/2)log_2(a/2) + (1/2)log_2(1/2)
 = (1/2)log_2(a)-1.
```

Therefore

```text
lambda_fair(3) = -0.2075187496394219... < 0,
lambda_fair(5) =  0.1609640474436812... > 0.
```

The sign threshold is `a=4`; among odd integer multipliers it separates `a=3`
from every `a>=5`.

This is a statement about the stipulated random model. It is not a theorem that
physical parity bits are independent or fair, and it proves nothing about an
individual orbit.

## Definitions

The model assigns multiplier `1/2` to an even step and `a/2` to an odd step.
The expectation is taken before any additive `+1` correction or arithmetic
conditioning is modeled.

## Motivation

The `a=5` universe is useful precisely because the simplest drift heuristic has
the opposite sign from `a=3`. When a rigorous obstruction survives in both
universes, its source is likely certificate format, ordinary-section height, or
arithmetic realization rather than this first-order drift model.

## Proof or construction

Average the two branch log multipliers:

```text
(1/2)log_2(1/2)+(1/2)log_2(a/2)
 = -1/2 + (1/2)(log_2(a)-1)
 = (1/2)log_2(a)-1.
```

This is negative exactly when `log_2(a)<2`, equivalently `a<4`, and positive
when `a>4`. Substitution gives the two displayed decimals. **QED within the
model.**

## Dependency audit

Only the branch slopes in D-8801 and elementary logarithm algebra are used.

## Gap audit

- The actual parity process is arithmetically dependent.
- Additive corrections matter, especially for small values.
- A positive expected model drift does not prove any positive integer orbit
  diverges.
- A negative expected model drift does not prove all orbits terminate.
- “Drift-driven” elsewhere in the packet means dependence on constants related
  to expansion; it does not mean this independent model has been imported as a
  theorem.

## Adversarial tests

X-8801 records the constants with high-precision decimal arithmetic. Its
million-step seed-`7` ledger has nearly balanced parity counts, but that finite
observation is not a dependency of the formula.

## Remaining uncertainty

None in the model identity. Its applicability to physical trajectories is
explicitly unresolved.

## Suggested next attack

For each active obstruction, replace informal references to “drift” by the
specific deterministic constant it uses. Compare that constant across `a=3`
and the exact T-8802 chart rather than importing independence heuristics.
