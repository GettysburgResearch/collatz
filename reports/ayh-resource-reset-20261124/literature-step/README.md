# Evidence for the literature and first-passage checkpoint

The research packet is [Actual source transfer, spatial mixing and future parity marks](../../../research/ayh-resource-reset-20261124/literature-step/README.md). Universal Collatz remains open.

## Formal verification

The final invocation of `check_lean.sh` builds six new modules and their complete three-module local import closure into a fresh temporary output directory. It uses Lean 4.34.1, Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`, one worker, `autoImplicit=false`, and warnings as errors. Third-party compiled Mathlib dependencies are reused. All **21** public declarations have only subsets of the standard axioms `propext`, `Classical.choice`, and `Quot.sound`.

[Full build log](lean-build.log) · [Execution summary](lean-build.json) · [Public declaration audit](axiom-audit.json) · [Research source hashes](source-hashes.json).

This build verifies the exact formal interfaces described in the research table. It does not claim that the probability estimates, full rotation argument, external positive-density theorem or global closing conditions have been fully formalized.

## Bounded physical replay

The finite census enumerates all **538,083** head children on levels 1, 2 and 3, retaining separate clocks on both actual trajectories. It also checks **6,643** affine-profile identities on higher ordinary lifts. The execution returned exit zero, with no stderr. It checks the indicated finite paths and profile equations; the many missed deadlines are not counterexamples to convergence.

[Exact command, output and scope](finite-checks.json).

## Independent reconstruction

- [Spatial and residue-stream review](MACROSCOPIC_REVIEW.md) checks the finite-grid normalization, reciprocal cell weights, rotation averaging and the separately conditioned closing implication.
- [Mark-count, critical-fiber and independent-orbit review](MARK_AND_CRITICAL_REVIEW.md) records the exact source hashes and verifies quantifiers, source projections, inverse clocks and the changed-surplus scope.
- [First-passage review](FIRST_PASSAGE_REVIEW.md) independently reconstructs adaptive threshold counting and all sliding-window coverage, including the boundary past the final entrance.
- [Parent reconstruction](PARENT_REVIEW.md) states the checks and final weighted criterion in one place.

These are independent internal arguments at the recorded versions. They do not imply external peer review or a blanket verdict on later versions, neighboring PRs or all external sources.

## Publication integrity

The final pushed tree is required to equal the checked local tree. After the remote commit is fetched into a clean complete checkout, the mandatory default `tools/validate.py` run is recorded in the PR description with its exact published head, tree, receipt hash and full receipt. Keeping that receipt in the PR avoids changing the just-validated commit merely to record its own identity. The optional historical regression bundle is not part of this checkpoint. Repository integrity checks structural and frozen-source consistency; it is separate from proof checking.
