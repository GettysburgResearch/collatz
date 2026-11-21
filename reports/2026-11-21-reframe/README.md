# Repository-wide reframe: execution and review archive

The scientific entry point is
[the reframe packet](../../research/reframe-20261121/README.md).
Full Collatz convergence remains **OPEN**.

This archive separates new Lean checking, paper-level reconstruction, exact
finite arithmetic, and repository integrity. A source inventory or a passing
repository gate is not a proof of the mathematical statements.

## Successful exact checkpoint

The complete new-packet execution concerns commit
`75f2f9aad4d3f80aaa1f8718e229faa04ee5770e`, tree
`6d81c9fa46c4e7d22b7b5a980798bc5bd92a8396`, with **423 tracked files**.
It was pushed to `research/lean-global-20261121` on
[draft PR178](https://github.com/GettysburgResearch/collatz/pull/178), and
the remote head was read back.

| Actual execution at that commit | Result | Receipt |
|---|---|---|
| Fresh complete build of the two pinned imports, three new Lean modules, and dedicated audit | PASS; all **25 public statements**, six Lean source invocations, each with `-j1 -DwarningAsError=true` | [proof-lean.json](proof-lean.json) |
| Exact Green rational certificate | PASS; 21 finite unit sources plus the separately proved infinite tail bound | [proof-lean.json](proof-lean.json) |
| Required repository gate in the same clean complete checkout | PASS; all five commands | [proof-repository.json](proof-repository.json) |

The successful execution ran on 2026-11-21 from 22:39:54 to 22:41:19 UTC.
The full Lean build command took 46.518 seconds. The checkout was clean
before and after; every recorded source hash remained unchanged. The
Mathlib source was clean at the pinned revision before and after.

The 25 audited statements comprise nine ordinary affine-pump/first-hit
theorems, ten marked-prefix/merger theorems, and six population/packing
theorems. This includes supporting and credited statements; it is not a
count of 25 independently novel results. Reported logical dependencies
are subsets of `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx`
or conjectural closure axiom appears in the audited dependencies.

The language-theory consequences, GM1–GM3, fractional Green moments,
Green topology, and the late PR185 composition remain paper proofs or
explicitly source-qualified deductions. They are not included in the
Lean theorem count.

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

The successful receipts are added in a documentation follow-up to the
checked commit. All Lean sources, the build script, toolchain file, and
source hash manifest remain byte-identical to that commit. The receipt
keeps its original checked SHA; it is not relabeled as a proof build at
the later documentation head.

[PUBLICATION_REFRESH.json](PUBLICATION_REFRESH.json) records the late
metadata read; the mathematical connections and their evidence boundaries
are in [LATE_UPDATE.md](../../research/reframe-20261121/LATE_UPDATE.md).

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
