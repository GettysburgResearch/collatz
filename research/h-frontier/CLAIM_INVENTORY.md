# Noncanonical claim inventory: H exact frontier

This index reserves the `*-9500` identifiers for issue #17. It is not the
repository's canonical `CLAIMS.md`. All theorem-level statements remain
`PROPOSED` pending independent review. Finite audits `X-9501`, `X-9502`, and
`X-9503` are `EMPIRICAL` and do not promote any universal claim.

## Packet files

- [`claims/EXACT_SYSTEM.md`](claims/EXACT_SYSTEM.md) — `D-9501`, `L-9501`–`L-9504`.
- [`claims/SURVIVOR_THEORY.md`](claims/SURVIVOR_THEORY.md) — `T-9501`–`T-9503`, `L-9505`.
- [`claims/DISPLACEMENT_FRONTIER.md`](claims/DISPLACEMENT_FRONTIER.md) — `C-9501`, `L-9506`, `Q-9501`.
- [`claims/STRUCTURAL_RESULTS.md`](claims/STRUCTURAL_RESULTS.md) — `L-9507`–`L-9510`, `R-9501`, `R-9502`, `Q-9502`.
- [`claims/ITERATION_02.md`](claims/ITERATION_02.md) — `L-9511`, `L-9512`, `T-9504`, `T-9505`, `R-9503`, `Q-9503`.
- [`claims/ITERATION_03.md`](claims/ITERATION_03.md) — `L-9513`–`L-9515`, `T-9506`–`T-9508`, `Q-9504`, `Q-9505`.

## Status table

| ID | Title | Status | Main dependency / caveat |
| --- | --- | --- | --- |
| `D-9501` | Exact `p`-coordinate block system | PROPOSED | self-contained |
| `L-9501` | H-to-shortcut-Collatz lift | PROPOSED | `D-9501` |
| `L-9502` | Exact finite cylinders | PROPOSED | self-contained after `D-9501` |
| `L-9503` | Carries and ghost stabilization | PROPOSED | `L-9502` |
| `L-9504` | Toll-Euler identity | PROPOSED | `D-9501` |
| `T-9501` | Infinite-survivor harmonic summability | SUPERSEDED | stronger plastic bound `T-9506` |
| `T-9502` | Nonperiodic survivors real-escape | PROPOSED | `L-9504`, now preferably `T-9506` |
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
| `T-9504` | Subcritical weighted survivor moments | SUPERSEDED | stronger branchwise theorem `T-9507` |
| `T-9505` | Capital--core discounted budget | PROPOSED | `L-9504`, `T-9502` |
| `L-9513` | Exact first-crossing intermediate threshold | PROPOSED | zero-carry inequality remains |
| `L-9514` | Separated ghost IFS and plastic recurrence | PROPOSED | self-contained from ghost recursion |
| `T-9506` | Plastic power bound for ordinary survivors | PROPOSED | `L-9503`, `L-9514` |
| `T-9507` | Branchwise critical harmonic kernel | PROPOSED | gives uniform core-reciprocal budgets |
| `L-9515` | Repetition forces completion height | PROPOSED | complexity corollary uses real escape |
| `T-9508` | Critical/subcritical real-escape split | PROPOSED | depends on `T-9505` |
| `Q-9504` | `2`-adic logarithm critical-chain exclusion | IDEA | exact external theorem interface unaudited |
| `Q-9505` | Subcritical transformed-height finite trap | IDEA | integer height not yet found |

## Dependency summary

A proof of H would follow from the signed-displacement theorem together with
weighted bounded-representative termination:

1. `C-9501` and `L-9506` would make every contracting exact segment descend.
2. Infinite repeated descent is impossible in positive integers.
3. Any surviving tail would be prefix-expanding.
4. `Q-9502` would exclude that tail.

Iteration 02 sharpened both sides:

- `L-9511` reduced signed displacement to a canonical phase interval.
- `L-9512` proved all same-sign concatenations and confined the finite gap to
  actual-word mixed-sign crossings (`Q-9503`).
- `T-9505` forced every real-escaping ray to obey a finite exponentially
  discounted odd-core budget.

Iteration 03 adds:

- `L-9513`, an exact intermediate-state threshold for the final mixed-sign
  crossing;
- `L-9514` and `T-9506`, the plastic recurrence and the stronger
  `O(X^0.405686...)` survivor count;
- `T-9507`, a critical summable-kernel theorem and a uniform reciprocal budget
  at every valuation scale;
- `L-9515`, the H analogue of completion-height repetition rigidity;
- `T-9508`, the critical near-Pillai versus subcritical escape dichotomy;
- `Q-9504` and `Q-9505`, the two now-isolated infinite attack surfaces.

No positive integer witness and no proof excluding every real-escaping ghost is
contained in this packet.
