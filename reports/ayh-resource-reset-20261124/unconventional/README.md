# Execution and review: unconventional ordinary-source pass

**Collatz remains OPEN.** This is the evidence packet for the
[scientific overview](../../../research/ayh-resource-reset-20261124/unconventional/README.md).
It extends PR197 at `f74d2144275c3e1f9148b0b2997fecc7931ae7f5`.
Three GPT-6.2 Astra delegates used the requested ultra reasoning effort;
the coordinator reconstructed key arguments, supplied independent finite
replays, checked the final interfaces, and rebuilt the complete local
Lean chain. The work was a time-boxed research pass, not an external peer
review or a proof of universal convergence.

## Mathematical execution

The final fresh build passed **95 distinct local modules**: 90 mathematical
modules and five audits. It includes **38 new mathematical modules**, one
new audit, **150 new public theorem declarations**, and **403 public
declarations** in the combined audit. Every reported axiom dependency is
a subset of `propext`, `Classical.choice`, and `Quot.sound`; some declarations
have no axioms. There is no `sorry`, new axiom, or `native_decide` in the
new sources.

The driver built every local object into a newly created temporary
directory, using Lean 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and the existing external
Mathlib/package cache at Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. It used `-j1`, disabled
`autoImplicit`, and treated warnings as errors. No author-generated local
object was used in this complete rebuild.

- [Execution receipt](lean-execution.json) records the command, actual
  times, all 95 source hashes, source stability, compiler pins, and log hash.
- [Complete build log](lean-final.log) records all module compilations and
  axiom output.
- [Combined axiom audit](axiom-audit.json) checks every expected public name.
- [New public theorem inventory](public-theorems.json) identifies the new
  module/name pairs, including the final consumer.

The receipt's checkout HEAD is the prepublication parent. The compiled
new source bytes are identified explicitly. The separate validator run
on the subsequently published clean complete checkout is recorded in the
PR description with that actual commit and tree. These are different
execution events; the prepublication build is not presented as a build
performed at the later commit.

## Exact finite replays

All **nine** replay programs passed in both normal and optimized Python,
for **18 successful executions**. Each pair produced byte-identical output.
The [finite receipt](controls/receipt.json) records every invocation, exit
code, output hash, and the unchanged scientific Lean/Python sources.

| Replay | What its exact execution checks |
|---|---|
| `check_adelic.py` | Ordinary inverse construction, finite arithmetic, and gain/count controls |
| `check_geometric.py` | Positive and negative logarithmic units, direct precision cross-check, all 164 negative-profile blocks and literal source data |
| `check_wall_controls.py` | Rational/signed and positive-local transport countermodels and wall controls |
| `check_wall_periods.py --through 30` | All 4,719 primitive parity-admissible necklaces in the stated length range and their finite signed-orbit classifications |
| `check_precision.py` | Directed local-precision arithmetic and record/population controls |
| `check_entry_edges.py` | Reconstruction of marked entry configurations and complete-branch comparisons |
| `check_fresh_ascent.py` | Signed first-hit classification, transfer and forest controls, and the finite reduction supporting the sharp fresh gain |
| `check_log_tower_independent.py` | Coordinator's separate reconstruction of the literal positive logarithmic residue and both anchor profiles |
| `check_wall_independent.py` | Coordinator's separate parsing and replay of all wheel rows and 854 covering leaves |

These executions do not prove the analytic estimates. The long negative
ordinary profile itself is Lean checked; its identification with the
stabilized logarithmic derivative has separate written and exact-arithmetic
evidence. The sharp `3/8` fresh-gain classification uses a written finite
reduction plus exact enumeration, not a Lean theorem for that whole claim.

The corrected exploratory cross-prefix program has a separate
[receipt](cross-prefix-execution.json) and
[output](cross-prefix-corrected-h3-43.log). It leaves 1,726,884 words at
depth 43 under its finite three-extra-clock constraints. The initial
root-mask omission is documented in the review. This count is neither
an infinite-entropy theorem nor an ordinary Collatz counterexample.

## Source review and exact scope

[ROOT_REVIEW.md](ROOT_REVIEW.md) records the independent coordinator
checks, corrections, and first unsupported steps.
[SOURCE_REVIEW.md](SOURCE_REVIEW.md) covers the AYH lineage, pinned
analytic inputs, selected current PRs, prior credit, and optional recent
manuscript assumptions. [SOURCES.json](SOURCES.json),
[adelic-source-inputs.json](adelic-source-inputs.json), and
[critical-source-inputs.json](critical-source-inputs.json) identify exact
repository commits, paths, blob identities, and primary external sources.
The prior PR description is preserved in
[PRIOR_PR_DESCRIPTION.json](PRIOR_PR_DESCRIPTION.json).

The [all-state intake](ALL_PR_INTAKE.json) contains metadata for 169 PRs,
146 open at intake. It is not a mathematical audit of all 169 branches.
The [late selected-head refresh](LATE_SELECTED_INTAKE.json) records live
heads during the pass. PR193's further advance is compared separately in
[LATE_PR193_REVIEW.md](LATE_PR193_REVIEW.md); no verdict is extended to a
later commit automatically. The final selected-head refresh also found
PR201 at `3eb251fae9082fef33c047079a511d1c3f4c5969`; its scoped comparison
is [LATE_PR201_REVIEW.md](LATE_PR201_REVIEW.md), with metadata in
[FREEZE_HEADS.json](FREEZE_HEADS.json).

Delegate and cross-lane review records:

- [Adelic review](ADELIC_DELEGATE_REVIEW.md)
- [Wall review](HARMONIC_DELEGATE_REVIEW.md),
  [final interface review](HARMONIC_FINAL_SCOPE_REVIEW.md), and
  [wall module manifest](HARMONIC_MANIFEST.md)
- [Arithmetic and gain review](CRITICAL_DELEGATE_REVIEW.md) and
  [late cross-review](LATE_CROSS_REVIEW.md)

## What remains unproved

`UnconventionalProposal.collatz_iff_remaining` is a checked equivalence.
Its `RemainingExclusion` is a named **OPEN proposition**, not an added
axiom or a theorem supplied by this packet. The complete signed-cycle
hypotheses imply the stated ordinary wall restrictions; they do not cover
every binary word or every aperiodic wall. Dense successful subcylinders,
perfect-power exclusions, and uniform geometric-slice bounds do not
supply success for every original parameter. The all-source clock bounds
are necessary conditions for meetings, not assertions that a successful
small query exists. The stronger first-contact delay has a written proof,
while its weaker all-meeting bound is formalized.

The exact source boundary is recorded in [source-hashes.json](source-hashes.json).
Repository integrity, Lean kernel checking, finite arithmetic execution,
and the mathematical status of the written analytic inputs remain
separate evidence categories throughout the packet.
