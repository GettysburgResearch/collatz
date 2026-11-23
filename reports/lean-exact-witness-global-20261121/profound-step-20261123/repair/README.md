# Integer-repair lane: evidence and boundaries

23 November 2026. The lane attempted an actual small ordinary ancestor of
the fixed sibling. **No universal repair or Collatz closure was obtained.**

## Proved output

The [manuscript](../../../../research/lean-exact-witness-global-20261121/profound-step-20261123/repair/ADELIC_INTEGER_REPAIR.md)
gives the exact canonical rational pullback, its primitive ternary
denominator and exact binary precision. For every fixed upper sibling
power, the displayed three-place Subspace product is at least `7/3`.
This rules out applying that theorem through the specified unaccelerated
approximants. It does not rule out other approximants or actual integer
ancestors. Signed periodic completion is computed explicitly and its
error is identified with the complete integral block displacement.

## Actual executions

The six declarations in `AdelicRepair.lean` compiled with
`-j 1 -DwarningAsError=true` under Lean 4.34.1, using Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
The audit contains only `propext`, `Classical.choice`, and `Quot.sound`.
No infinite convergence, valuation theorem, Subspace Theorem, or repair
existence is assumed as a Lean axiom. The module formalizes six cleared
arithmetic identities; the stated analytic and valuation arguments remain
written scope.

The exact checker was freshly run normally and under `-O`. The paired
outputs are byte-identical. After the independent reviewer corrected a
wording ambiguity and a block-boundary index in the manuscript, both
checker runs were repeated to bind its final bytes.

| Control | Count |
|---|---:|
| Canonical pullbacks and consecutive increments | 4,602 |
| Primitive pairs and exact binary precision | 4,368 |
| Literal positive rational forward edges | 3,042 |
| Complete finite adelic products | 13,104 |
| Signed block extrapolants | 1,404 |
| Blocks with a convergent real periodic model | 348 |
| Damaged primitive certificates rejected | 4 |

The minimum finite product is exactly `7/3`. The checker also retains the
ordinary path `75 -> 113 -> 85`, while the canonical rational pullback
from the length-eight odd prefix of 65 is `14822219/2187`. Thus it rejects
the incorrect inference from canonical nonintegrality to nonexistence of
an ordinary repair. All sampled starting integers converge; no sampled
trajectory is represented as a hypothetical escaping example.

[REPLAY.json](REPLAY.json) records actual commands, exit codes, stdout
hashes and source bindings. [SOURCES.json](SOURCES.json) distinguishes
the primary theorem actually read from the contextual literature and
unchanged repository dependencies. Internal review is separately bound
in the checkpoint's reviews directory.
