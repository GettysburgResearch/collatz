# Verification of the joint-renewal checkpoint

The scientific packet is [Three-arm moments and actual landing weights](../../../research/ayh-resource-reset-20261124/joint-renewal/README.md). Universal convergence remains open.

## Formal evidence

The final fresh build compiles **eight new Lean modules** and rebuilds their four-module local import closure. It uses Lean 4.34.1, Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`, one worker, `autoImplicit=false`, and warnings as errors. Previously compiled third-party Mathlib dependencies are reused; local proof modules are rebuilt into a fresh temporary directory.

All **26 public theorem declarations** are queried in one aggregate audit. Their transitive axiom sets are subsets of `propext`, `Classical.choice`, and `Quot.sound`. No placeholder or custom axiom is used. The source of the genuinely differentiated potential, rather than only a named algebraic surrogate for its Hessian, is part of this build.

| Module | Public theorems | What the kernel checks |
| --- | ---: | --- |
| KilledGradeGreen | 3 | Finite killed-walk occupation, terminal potential and arbitrary level rewards |
| EndpointFibers | 3 | Odd-count uniqueness and endpoint-only first-entrance fiber cardinality |
| EntranceGrades | 4 | Safe prefixes, exact entrance/missing transfers, finite translation averaging |
| AffineGradeRigidity | 4 | Two-point affine slope equality and ordered/crossed valuation constraints |
| QuartetCollapse | 4 | Six all-parameter ordinary trajectories and their residual two-class profile |
| TripleGradeProduct | 3 | Ordered gap drift, tie injection and the mixed-parity identity |
| MiddleIsolationWindow | 2 | Physical-window isolation and sliding-window overlap bounds |
| SubcriticalCurvature | 3 | Actual real second directional derivatives, covariance contraction and its negative bound |

[Final build log](lean-build.log) · [Command and execution metadata](lean-build.json) · [Named axiom inventory](axiom-audit.json) · [Research source hashes](source-hashes.json).

The full probability theorem, Taylor remainder estimates, physical-clock comparison, infinite occupation bounds and moment argument are **written proofs**. This finite formal verification does not claim that those arguments, the external synchronization sources, or Collatz itself have been fully formalized.

## Executed ordinary controls

The coordinator reran the frozen entrance-grade checker. It tested **172,935** original/dilated digit comparisons and found **13,181** paired certificates satisfying its finite guard. For each certificate it checked four pairs of entrance sets, including all four possible hit/miss patterns under both dilations. It also checked finite translation averaging with exact rational arithmetic.

The replay returned zero with empty stderr. The record preserves the exact command, source digest and complete counts. These controls corroborate the specified finite transfer, not the asymptotic estimates. [Execution record](finite-checks.json).

## Independent mathematical reconstruction

- [Subcritical moment review](SUBCRITICAL_REVIEW.md) checks the strongest manuscript at its exact SHA-256, including the covariance, derivatives, block conditioning, near-tie cost and finite absorption. Two other streams also independently reconstructed this argument; the coordinator's final reconstruction is below.
- [Affine and source-weight review](AFFINE_REVIEW.md) checks the landing fibers, small-level occupation, joint clock transport and endpoint cardinality at the indicated revisions.
- [Renewal review](RENEWAL_REVIEW.md) covers the earlier reciprocal-clock triple proof and stopped-grade law at its explicitly named source hashes. Its scope does not automatically extend to later additions.
- [Coordinator reconstruction](ROOT_REVIEW.md) checks the final sources, identifies the recent external input and states the remaining two-class obstruction.

Exact review pins are preserved even when an earlier revision differs only by an added theorem or a wording correction. The current source manifest is authoritative for the published packet. Internal independent review does not constitute external peer review.

## Publication evidence

The remote tree must equal the tested local scientific tree. After fetching the resulting remote commit into a clean complete checkout, the mandatory default repository validator is run at that **exact** head. Its full receipt, head, tree and SHA-256 are placed in the PR description without changing the validated commit. Optional historical regressions are not part of this checkpoint. Repository integrity is distinct from proof checking.
