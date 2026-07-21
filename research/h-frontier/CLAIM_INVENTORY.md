# Noncanonical claim inventory: H exact frontier

This index reserves the `*-9500` identifiers for issue #17. It is not the
repository's canonical `CLAIMS.md`. All theorem-level statements remain
`PROPOSED` pending independent review. Finite audits `X-9501` and `X-9502` are
`EMPIRICAL` and do not promote any universal claim.

## Packet files

- [`claims/EXACT_SYSTEM.md`](claims/EXACT_SYSTEM.md) — `D-9501`, `L-9501`–`L-9504`.
- [`claims/SURVIVOR_THEORY.md`](claims/SURVIVOR_THEORY.md) — `T-9501`–`T-9503`, `L-9505`.
- [`claims/DISPLACEMENT_FRONTIER.md`](claims/DISPLACEMENT_FRONTIER.md) — `C-9501`, `L-9506`, `Q-9501`.
- [`claims/STRUCTURAL_RESULTS.md`](claims/STRUCTURAL_RESULTS.md) — `L-9507`–`L-9510`, `R-9501`, `R-9502`, `Q-9502`.
- [`claims/ITERATION_02.md`](claims/ITERATION_02.md) — `L-9511`, `L-9512`, `T-9504`, `T-9505`, `R-9503`, `Q-9503`.

## Status table

| ID | Title | Status | Main dependency / caveat |
| --- | --- | --- | --- |
| `D-9501` | Exact `p`-coordinate block system | PROPOSED | self-contained |
| `L-9501` | H-to-shortcut-Collatz lift | PROPOSED | `D-9501` |
| `L-9502` | Exact finite cylinders | PROPOSED | self-contained after `D-9501` |
| `L-9503` | Carries and ghost stabilization | PROPOSED | `L-9502` |
| `L-9504` | Toll-Euler identity | PROPOSED | `D-9501` |
| `T-9501` | Infinite-survivor harmonic summability | PROPOSED | counting proof requires review |
| `T-9502` | Nonperiodic survivors real-escape | PROPOSED | `L-9504`, `T-9501` |
| `T-9503` | Equivalent infinite-obstruction formulations | PROPOSED | `L-9503`, `T-9502` |
| `L-9505` | Bounded-representative finite branching | PROPOSED | exact finite-tree target |
| `C-9501` | Signed displacement for exact cylinders | EMPIRICAL | universal mixed-sign carry step open |
| `L-9506` | Conditional contracting-cylinder descent | PROPOSED | conditional on `C-9501` |
| `L-9507` | Finite prime support exclusion | PROPOSED | imports S-unit finiteness |
| `L-9508` | Prime reuse through offsets | PROPOSED | self-contained |
| `R-9501` | No finite itinerary-only obstruction | PROPOSED | consequence of `L-9502` |
| `R-9502` | Direct ghost congruence correction | PROPOSED | consequence of `L-9502` |
| `Q-9501` | Carry-rectangle lemma | IDEA | broad form of the mixed-sign gap |
| `Q-9502` | Weighted bounded-representative termination | IDEA | final one-sided obstruction |
| `L-9509` | Two-sided exact-window density | PROPOSED | finite-window consequence |
| `L-9510` | Long expanding finite shadows | PROPOSED | finite shadows are not infinite orbits |
| `L-9511` | Canonical endpoint range and fixed-point phase | PROPOSED | self-contained after `L-9502` |
| `L-9512` | Same-sign phase closure | PROPOSED | mixed-sign case remains |
| `Q-9503` | Word-specific mixed-sign crossing | IDEA | sharp finite descent frontier |
| `R-9503` | Naive first-letter fixed-point bound is false | PROPOSED | exact length-25 witness; `X-9502` |
| `T-9504` | Subcritical weighted survivor moments | PROPOSED | weighted extension of `T-9501` |
| `T-9505` | Capital--core discounted budget | PROPOSED | `L-9504`, `T-9502` |

## Dependency summary

A proof of H would follow from the signed-displacement theorem together with
weighted bounded-representative termination:

1. `C-9501` and `L-9506` would make every contracting exact segment descend.
2. Infinite repeated descent is impossible in positive integers.
3. Any surviving tail would be prefix-expanding.
4. `Q-9502` would exclude that tail.

Iteration 02 sharpens both sides:

- `L-9511` reduces signed displacement to a canonical phase interval.
- `L-9512` proves all same-sign concatenations and confines the finite gap to
  actual-word mixed-sign crossings (`Q-9503`).
- `T-9504` supplies every subcritical valuation-weighted survivor moment.
- `T-9505` forces every real-escaping ray to obey a finite exponentially
  discounted odd-core budget.

Without `C-9501`, `T-9501`–`T-9505` still reduce the infinite problem to a
one-sided nonperiodic real-escaping ghost under strong joint capital, spike, and
core restrictions. No positive integer witness and no proof excluding all such
ghosts is contained in this packet.
