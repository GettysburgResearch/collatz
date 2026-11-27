# The final Lean proposal remains incomplete

The file [FinalProposal.lean](FinalProposal.lean) compiles, but its final
universal conclusion still requires an unproved mathematical hypothesis:

```lean
theorem final_proposal (remaining : FrontierMerger) :
    ∀ n : Nat, 0<n → Good n
```

`Good` is actual finite convergence under the ordinary positive shortcut
map. `FrontierMerger` is the existing pinned PR192 merger proposition; it is
not redefined to weaken the requested conclusion. A standard transitive
axiom report does not discharge a theorem argument. The theorem is a checked
consumer of the open premise, not a complete proof of Collatz.

## Closed results in the same assembly

`convergent_control_outside_anchors` proves that 3645 reaches 1 and that no
immediate transfer in the stated anchor architecture reaches its full lower
cone. Its destination may contain any power of two, and it may use a smaller
base or the same base 5 at an earlier ternary exponent. Positive anchors
reach phase +1; negative anchors reach any periodic phase with magnitude at
most 136. All preperiods and positive-length returns are quantified without
a clock cutoff. The proof reduces zero-preperiod cases to a bounded actual
prefix and uses scale theorems for arbitrary positive preperiods. It does
not assert this obstruction for every positive cycle phase or for arbitrary
compositions of transfers.

`all_exponents_have_descent` supplies a whole progression of bases with an
actual endpoint below that base for every supplied initial exponent and
every positive exponent gain. It excludes each member of those progressions
from `FirstTower`. It does not supply the progression membership of an
arbitrary alleged first bad base.

## Module and evidence boundary

| New module | Selected declarations | Checked mathematical scope |
|---|---:|---|
| `AnchorDescent` | 11 | Ordinary positive and negative lift meetings, explicit all-exponent family, native descent and unrestricted scale inequalities. |
| `AnchorControl` | 4 | Full lower-cone prefix exclusion, arbitrary-clock positive/negative anchor exclusion at 3645, and its actual convergence. |
| `TraceCensus` | 6 | Physical image envelope, one-path shifted injection, residual bounds and fixed rational comparisons. |
| `LocalDenominator` | 7 | Doubled-seam ideal identity, recovery from two powered differences, exact finite residue decoding and lap uniqueness. |
| `TemplateChain` | 4 | Ordinary rational centered map, powered iteration and sparse telescoping endpoint identity. |
| `FinalProposal` | 3 | Closed countercontrol, explicit descent progressions and universal consumer with its open premise. |

The four reused dependencies are `SourceDeletion`, `MinimumFailure`,
`SmoothCore`, and `TowerClock`, with 48 additional selected inventories.
All source bytes are pinned in [SOURCES.json](../SOURCES.json).

The complete polynomial-quotient application and asymptotic short-window
criterion are written arguments. The S-unit finiteness theorems use the
published Evertse–Schlickewei–Schmidt result, not a local Lean proof of it.
The precise trace census recurrence is evaluated with exact Python integers
and fractions; the exhaustive finite Collatz floor is an external published
input. The numerical trace cutoff is not asserted as a Lean theorem.

## Execution and review

The root rebuilt all ten modules in an empty project output directory using
Lean 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Warnings were errors.
The runner verified the dependency pins, compiler identity, Mathlib revision,
selected inventory names and unchanged source hashes. Each reported
transitive axiom was in `{propext, Classical.choice, Quot.sound}`. It reused
the pinned cached Mathlib/package modules and did not rebuild the compiler.

[Root Lean receipt](../../../../reports/astra-global-closure-20261124/round11/lean/receipt.json)
· [Template review](../../../../reports/astra-global-closure-20261124/round11/diagonal/TEMPLATE_REVIEW.md)
· [Closure review](../../../../reports/astra-global-closure-20261124/round11/diagonal/CLOSURE_REVIEW.md)
· [Cycle review](../../../../reports/astra-global-closure-20261124/round11/closure/CYCLE_REVIEW.md)
· [Trace review](../../../../reports/astra-global-closure-20261124/round11/cycle/DIAGONAL_REVIEW.md)

Use [check_lean.py](../check_lean.py) with the three required absolute paths
shown in the packet README. The runner rejects a missing project module,
unexpected import, changed pinned dependency, nonstandard selected axiom,
failed compilation or changed source. Its scan is supplementary; the Lean
kernel and transitive reports supply the stated proof evidence.
