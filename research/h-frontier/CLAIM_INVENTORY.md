# Noncanonical claim inventory: H exact frontier

This index reserves the `*-9500` identifiers for issue #17. It is not the
repository's canonical `CLAIMS.md`. All theorem-level statements remain
`PROPOSED` pending independent review. The finite audit `X-9501` is
`EMPIRICAL` and does not promote any universal claim.

## Packet files

- [`claims/EXACT_SYSTEM.md`](claims/EXACT_SYSTEM.md) — `D-9501`, `L-9501`–`L-9504`.
- [`claims/SURVIVOR_THEORY.md`](claims/SURVIVOR_THEORY.md) — `T-9501`–`T-9503`, `L-9505`.
- [`claims/DISPLACEMENT_FRONTIER.md`](claims/DISPLACEMENT_FRONTIER.md) — `C-9501`, `L-9506`, `Q-9501`.
- [`claims/STRUCTURAL_RESULTS.md`](claims/STRUCTURAL_RESULTS.md) — `L-9507`–`L-9510`, `R-9501`, `R-9502`, `Q-9502`.

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
| `Q-9501` | Carry-rectangle lemma | IDEA | closes or refutes `C-9501` |
| `Q-9502` | Weighted bounded-representative termination | IDEA | final one-sided obstruction |
| `L-9509` | Two-sided exact-window density | PROPOSED | finite-window consequence |
| `L-9510` | Long expanding finite shadows | PROPOSED | finite shadows are not infinite orbits |

## Dependency summary

A proof of H would follow from the signed-displacement theorem together with
weighted bounded-representative termination:

1. `C-9501` and `L-9506` would make every contracting exact segment descend.
2. Infinite repeated descent is impossible in positive integers.
3. Any surviving tail would be prefix-expanding.
4. `Q-9502` would exclude that tail.

Without `C-9501`, the unconditional results `T-9501`–`T-9503` still reduce the
infinite problem to a one-sided nonperiodic real-escaping ghost. No positive
integer witness and no proof excluding all such ghosts is contained in this
packet.
