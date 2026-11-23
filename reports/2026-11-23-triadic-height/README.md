# Checkpoint 16: execution and review

Date: 23 November 2026. The [scientific packet](../../research/lean-global-resolvent-20261121/overview/triadic-height/README.md)
contains the complete new finite theorem and the remaining construction.
Full Collatz remains open.

## What is formalized

`TriadicAmortizedBudget.lean` proves 22 theorem declarations and defines
four objects. Its literal finite candidate theorem computes a height
budget from n,a,r and concludes an actual hit of one from the corresponding
finite list of complementary-parity tests. The signed denominator drop,
integral tie, zero entry, finite all-odd divisibility and complete horizon
are included. These are declaration counts, not 22 separate advances.

The source `TriadicDualClosure.lean` is copied unchanged from PR178 at
`4e204f54136c79cf8c9393b34e3330594f99ae0a`, SHA-256
`62a3d8a9541080864deb4887ba8c014a82222892869b14597c3b6385538913c7`.
The new module's axiom audit is transitive through that dependency.

The final endpoint-congruence consumer, logarithmic estimate for the
denominator weight, optimizer control and analytic/literature attempts
remain written mathematics. Universal candidate existence is not assumed
or proved by the new Lean module.

## Fresh execution

[new-source-checks.json](new-source-checks.json) records strict fresh
compilation of the copied dependency, new module and complete audit. The
audited axiom union is restricted to `propext`, `Classical.choice`, and
`Quot.sound`. No admission, custom research axiom or native proof shortcut
is allowed by the runner.

The executable is Lean 4.34.1, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib is pinned at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Existing Mathlib and package
objects are reused, while the two scoped project modules and the audit
are freshly compiled in a temporary directory.

The receipt also records exact Python controls in both normal and optimized
mode, requiring identical output. The independent state checker covers
95,540 compatible signed states, including 42,500 denominator drops,
350 zero entries, 50 ties and 47,117 two-step prefixes. The optimizer
checker retains all ten small unit-source trajectories, the full trajectory
from 31 to one, seven all-depth cutoffs and all ten compositions in its
fixed-target control. The author supplies separate finite candidate and
corrupted-candidate checks. These are scoped arithmetic controls, not a
search for a universal certificate or a proof by enumeration.

## Independent reconstruction and root review

[TRIADIC_INDEPENDENT_REVIEW.md](TRIADIC_INDEPENDENT_REVIEW.md) binds the
complete written proof by hash and reconstructs its finite clock and
congruence argument. It distinguishes that written reconstruction from
the later [independent strict Lean replay](independent-lean-replay.json).

[ROOT_INTEGRATION_REVIEW.md](ROOT_INTEGRATION_REVIEW.md) separately checks
the coordinating author's standalone two-carry question and overview,
including why the first carry selects the literal original word and why
the universal question is equivalent to convergence. It also reconstructs
the optimizer's all-depth cutoff and independently replays every smaller
unit source in [its exact controls](INTEGRATION_REVIEW_CONTROLS.json).
The triadic author performs this integration review; the separate
boundary agent reviews the triadic author's mathematical proof.

[ROOT_REVIEW.md](ROOT_REVIEW.md) records the coordinating researcher's
reconstruction of the formal claim, the all-depth optimizer control and
the two analytic corollaries, together with the primary statements actually
inspected. Root contributions and immediate inherited consequences are
not described as external peer review or independent new theorems.

## Source refresh and publication

[source-refresh.json](source-refresh.json) records a delta refresh of seven
active PR heads and descriptions against checkpoint 15's complete
145-record metadata inventory. The changed scientific branches were
PR178, PR180 and PR182; selected relevant source files were read at exact
heads and bound in the packet's source ledger. This is not a new audit of
all proofs in the repository.

The complete-checkout validator is run after committing this packet, then
on the fetched exact publication head. Its receipt and actual head are
reported in PR176. This gate covers repository structure and selected
integrity controls; it does not establish the infinite mathematics.
The [manifest](manifest.json) binds the delivered sources and reports.
The previous PR description is archived unchanged in
[previous-pr-description.json](previous-pr-description.json).
