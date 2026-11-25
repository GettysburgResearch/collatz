# Review and replay record

This report accompanies [the mathematical packet](../../research/astra-ultra-closure-20261125/README.md). It records execution and provenance. It is not an additional scientific baseline or a proof of Collatz.

The work began from main commit `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Three child agents were explicitly launched with model `gpt-6.2-astra`, reasoning effort `ultra`, and independent initial task context. This used all three child slots available alongside the coordinator. The child tasks covered fixed-source descent, ordinary-orbit arithmetic, and the proposed transfer of recent analytic machinery; they also reconstructed each other's load-bearing arguments. Model settings are execution provenance, not evidence for a mathematical claim.

The final coordinator replay passed: **six Lean modules and all 56 public theorem declarations**, with transitive dependencies limited to `propext`, `Classical.choice`, and `Quot.sound`. The numerical 116-exponent calculations and the exact 1024-clock equivalence are included. Both modes of the finite Python checker also passed. Full commands and output are retained below.

## Evidence files

| File | What it records |
|---|---|
| [SOURCE_INTAKE.json](SOURCE_INTAKE.json) | The retrieved open-PR heads and base identities. Listing a PR does not mean its entire contents were reviewed. |
| [ROOT_REVIEW.md](ROOT_REVIEW.md) | The coordinator's claim-level reconstruction, source-qualified inputs, and unresolved boundaries. |
| [lean-initial-setup-failure.json](lean-initial-setup-failure.json) | The first replay failed because the initial Mathlib object cache lacked an imported module. This was an environment failure, not a successful build. |
| [lean-replay.json](lean-replay.json) | The final fresh build of all local Lean modules, exact source hashes, complete command output, and public-theorem axiom audit. |
| [finite-checks.json](finite-checks.json) | Exact tower-tail calculations and finite ordinary controls in normal and optimized Python modes. |
| [SOURCE_HASHES.json](SOURCE_HASHES.json) | SHA-256 identities of the mathematical sources, packet documentation, reviewers' notes, and replay programs at submission. |

The complete-checkout validator writes its receipt outside its input checkout. Its actual result and the publication identities are reported in the PR description. A GitHub-created commit can have different author metadata from the local validation commit; the comparison is the exact Git tree, not an assertion that two different commits are identical.

## Boundaries

The local Lean audit permits only the usual logical axioms `propext`, `Classical.choice`, and `Quot.sound`. Explicit hypotheses in a theorem remain hypotheses even when its axiom audit passes. The written cycle entropy estimate, its band-exit corollary, and the symbolic all-shifts construction are separately reviewed paper arguments. No external GRH development or logarithmic-form formalization was locally rebuilt. External theorems retain their source-qualified status.

Existing validation programs, workflows, accepted results, and source archives were not edited. The submission adds a research packet and its evidence records on a new branch.

The machinery author's opening note retains its original pending-review wording. The subsequent completed independent reconstruction is recorded in `fixed_source/REVIEW_MACHINERY.md` and the coordinator review. This report preserves the reviewed mathematical source bytes instead of changing a source after its reviewer recorded the hash.
