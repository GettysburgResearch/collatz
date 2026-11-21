# Repository-wide reframe: execution and review archive

The scientific entry point is
[the reframe packet](../../research/reframe-20261121/README.md).
Full Collatz convergence remains **OPEN**.

This archive separates new Lean checking, paper-level reconstruction, exact
finite arithmetic, and repository integrity. A source inventory or a passing
repository gate is not a proof of the mathematical statements.

## Frozen repository view

[REPOSITORY_SNAPSHOT.json](REPOSITORY_SNAPSHOT.json) records the 143 PRs and
40 non-PR issues returned at retrieval time. Main was
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; the starting PR178 head was
`0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`. The snapshot explicitly records
metadata coverage, not an audit of every proof in every branch.

The new Lean packet imports only the required `ShellCover` and
`ForwardSection` copies from PR173 head
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. Their source hashes are checked
by the new build script. The toolchain is Lean 4.34.1; Mathlib is pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

## Semantic review records

- [MERGER_REVIEW.md](MERGER_REVIEW.md) reconstructs both binary rounding
  directions, the exact cover equivalence, the guarded rising merger,
  and the same-first-hit population capacity bounds.
- [DISCRETE_REVIEW.md](DISCRETE_REVIEW.md) reconstructs the ordinary defect
  budget, fixed-prefix first-hit contradiction, context-free accelerated
  language consequence, and the separately scoped parity-automaton result.
- [GLOBAL_MASS_REVIEW.md](GLOBAL_MASS_REVIEW.md) reconstructs GM1–GM3,
  the Green norm loss, the compressed-weight thresholds, and the exact
  rational certificate.
- [GREEN_FRACTIONAL_MOMENTS_REVIEW.md](GREEN_FRACTIONAL_MOMENTS_REVIEW.md)
  reconstructs the compact word domains, sharp moment threshold, and
  exclusion of nonzero integrable superharmonic densities.
- [GREEN_TOPOLOGY_REVIEW.md](GREEN_TOPOLOGY_REVIEW.md) independently checks
  the dense residual null set of infinite Green values and the
  discontinuity at every positive ordinary target.

These records identify their actual source hashes and evidence limits.
Their verdicts do not extend to a later unreviewed version or to an unstated
ordinary sampling theorem.

## Reproducible execution recorder

[validate_reframe.py](validate_reframe.py) requires a clean, complete checkout
of an explicitly supplied commit. It records the new packet's build, every
public theorem's reported axioms, and the exact Green arithmetic replay.
It checks source and checkout identities before and after execution.
The required repository gate is recorded separately with
`python -X utf8 -B tools/validate.py --receipt /outside/the/checkout.json`.

The optional runtime/cache copy on fast storage is a byte-identical input
optimization. The recorder compares every file in that copy against the
original official Lean runtime or pinned Mathlib dependency cache before
and after use. It records the file count, byte count, and aggregate hash;
it does not accept an unrelated dependency cache merely because its path
looks compatible. Ordinary builds can use the pinned cache directly.

Run-specific receipts and their exact checked commit are added after the
clean execution. Their identity will not be changed to imply a later
documentation commit was also Lean-built.

## Preserved initial build-path failure

The first clean execution used commit
`c09585437b23c8b75d834872bada6b17810d2668`. Its repository gate passed, but
the Lean build wrapper invoked the pinned import from outside Lean's chosen
source root. Lean rejected that invocation before elaborating `ShellCover`.
The actual failed wrapper record is preserved as
[initial-build-path-rejection.json](initial-build-path-rejection.json).

The fix changes only the imported-module invocation: it runs from the
existing vendor directory and writes its output to this packet's ignored
build directory. No Lean theorem, source pin, or proof hypothesis changes.
The successful clean execution, when recorded below, has its own exact
commit and receipt rather than relabeling this failed attempt.
