# Execution and independent review

This report accompanies [the research packet](../../research/astra-birth-rigidity-20261124/README.md).
**Full Collatz remains open.** Written mathematical review, bounded arithmetic
replay, compilation of finite Lean kernels, and repository-integrity validation
are different evidence levels.

## Sources and written reviews

- [Fresh source-head inventory](SOURCE_HEADS.json) covers PR146 and PR173--191.
  It pins twenty heads, including the latest phase-packing round. This inventory
  is not a claim that every historical file was independently reviewed.
- [Root reconstruction](ROOT_RECONSTRUCTION.md) explains the independent algebra,
  quantifiers and ordinary-source attachments checked in this investigation.
- [Stationary and finite-window audit](STATIONARY_REVIEW.md) records specific
  verdicts at PR180, PR182 and PR189 and credits the earlier stationary theorem.
- [Bounded-birth cross-review](BIRTH_BOUND_REVIEW.md) separately reconstructs the
  optimized transfer bound and the ordinary occupation exponent.
- [Mahler cross-review](MAHLER_CROSS_REVIEW.md) pins the exact extension document
  and checks its nonprimitive and fixed-letter cases.

The source inventory retains the head at which the mathematical review began.
A subsequent attribution-only correction to PR189 was published and freshly
read back at `a390a1a4c75ee95db98b4b683d17c503f4e4a118`. It credits PR180's
`research/whole-source-20261123/COLLISION_CORE.md` for S1. The reviewed scientific
statements at the older head are preserved.

### New heads found at publication

PR192 and PR193 were discovered after the first PR194 publication. The
[additional source inventory](LATEST_SOURCE_HEADS.json) freezes both heads.
The root read their phase, translated packing, cycle-factor, reduced-denominator
and guarded-merger arguments and reconstructed the three deductions in the
[synthesis](../../research/astra-birth-rigidity-20261124/LATEST_SOURCE_SYNTHESIS.md).
The three agents separately supplied a [phase and escape review](LATEST_ESCAPE_REVIEW.md),
[cycle review](LATEST_CYCLE_REVIEW.md), and [formal-source/receipt review](LATEST_FORMAL_REVIEW.md).
The mixed-family deduction has a separate
[arithmetic reconstruction](MIXED_DENOMINATOR_RECONSTRUCTION.md).

The cycle reviewer reports bounded exact replays of both pinned cycle programs
and 176 instances of the new mixed-family denominator divisibility; the escape
reviewer reports exact rational verification of the structural series bound.
These additional runs belong to those agents and are described in their reviews.
The root independently checked the written arguments, without repeating those
finite replays. The newer Lean module receipts were inspected and matched to
their source bytes, not independently re-executed. They are not included in
this packet's own compiled declaration counts.

## Executed Lean work

Toolchain: Lean **4.34.1**, release commit
`5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` (tag v4.34.1). The checkout and
declared dependency versions were inspected, and the remote Mathlib tag was
queried. The formal run used the pinned compiled dependency cache; it did not
rebuild all of Mathlib or use a second independent kernel.

[UpstreamFiniteKernels.lean](../../research/astra-birth-rigidity-20261124/lean/UpstreamFiniteKernels.lean)
is a complete tested module combining eight source files from six PR heads.
Its **66 theorem/lemma declarations and 14 definitions** were compiled with
one thread, warnings as errors and `autoImplicit=false`. All 80 named authored
declarations were included in the transitive `#print axioms` audit, including
private auxiliaries. The 119 printed lines include original duplicated checks.
Only `propext`, `Classical.choice`, and `Quot.sound` appeared. No `sorryAx`, custom
axiom, or native-decision axiom appeared.

| Frozen source | Included finite core |
|---|---|
| PR182 round 12, PhasePacking.lean | Carry telescope, normalized edge, height guard, prefix and returning comparisons, endpoint uniqueness |
| PR182 round 11, RepetitionWindow.lean | Exact shared-word divisibility, finite height bounds and repetition contradiction |
| PR187, RepeatObstruction.lean | Full binary-clock difference and finite ordinary equality tests |
| PR188, CarryCocycle.lean | Arbitrary-carry local inequality and clock amortization |
| PR188, ResidueDefect.lean | Finite arithmetic support for the residue-norm interface |
| PR189, CarryBudget.lean | Carry identity, low-clock budget, word recovery and no birth across digit one |
| PR190, MahlerCore.lean | Finite weights, concatenation, substitution and affine Mahler identities |
| PR191, TwoSidedPacking.lean | Finite spread/spacing, complete-carry differences, shadow and Bezout identities |

This is a **repaired combined-module compilation**, not a claim that all eight
original broad-import files independently compiled unchanged. The original
`import Mathlib` runs were slow under shared memory pressure. Nine narrower
Mathlib imports were sufficient for the tested module. Two removed lemma-name
uses in PhasePacking were replaced; two redundant `ring` steps and one unused
hypothesis proof were repaired there. Three tactic-sequencing changes in
CarryCocycle removed warnings that strict compilation treats as errors. All
changes are inside proof bodies or import/audit scaffolding; the mathematical
statements are retained.

- [Exact proof changes](frozen-proof-repairs.diff)
- [Source, declaration and supplemental-audit manifest](declaration-manifest.json)
- [Compiler receipt](FINITE_KERNEL_RECEIPT.json)
- [Complete raw axiom output](UpstreamFiniteKernels.lean.log)
- [Reconstruction program](make_lean_replay.py), which verifies frozen Git blob
  and SHA256 identities before reproducing original or repaired sources

The compiled source SHA256 is
`f5a292583bacc29aafb0bd1d8032849a5a3c5085f02b5d1162fb8257be4346e5`.
The complete output SHA256 is
`2df0af4b6c3b67eac1fe8bead61d28c63ca2f18d48e417e0e9247200df05bc50`.
The repository copy preserves those exact bytes; its filename is descriptive.

### New Std-only modules

[RunSupport.lean](../../research/astra-birth-rigidity-20261124/lean/RunSupport.lean)
proves zero-carry persistence and the positive-prefix property.
[BoundedBirth.lean](../../research/astra-birth-rigidity-20261124/lean/BoundedBirth.lean)
proves five finite lemmas, including weighted transfer rows at `x=1/3` after
clearing denominators into natural numbers. The optimized algebraic value of x
used in the written theorem is not formalized by this specialization.
[PhaseTreeCertificate.lean](../../research/astra-birth-rigidity-20261124/lean/PhaseTreeCertificate.lean)
checks every one of the 60 child-carry choices by ordinary kernel `decide`.
Its three lemmas establish table dimensions, the inverse of two modulo 81, and
the complete lifted-residue certificate. The all-lifts proof uses an explicitly
increased heartbeat/recursion limit; it does not use `native_decide`.

The standalone
[CarryBudgetStd.lean](../../research/astra-birth-rigidity-20261124/lean/CarryBudgetStd.lean)
also compiles all six PR189 proof bodies with only Std, replacing the broad
import and appending the two omitted axiom inspections.
[Source-bound standalone receipts](STD_LEAN_RECEIPT.json) identify the actual
successful agent executions and copied logs. A duplicate root RunSupport replay
timed out after 120 seconds without diagnostics and is recorded as incomplete;
it is not counted as another successful run.

The entropy, limiting measures, global asymptotics, Mahler transcendence,
cyclotomic classification, infinite inverse-tree consumer and universal
mathematical conclusions are **written proofs**, not consequences claimed to be
fully formalized by these finite kernels.

## Executed exact arithmetic

The root inspected and reran all four programs normally and under Python
optimization. Every pair exited zero with byte-identical output. Inputs were
SHA256-bound before execution and unchanged afterward. The programs contain no
AST `assert` nodes, so optimization removes none of their checks.

| Program | Executed bounded scope |
|---|---|
| check_run_support.py | 2,548 run coefficient equalities; 180 rational transfer rows; exact root/logarithm and exponent certificates |
| check_top_component.py | 11,957 contracting normalized words through length 14; 11,495 classification checks; twelve mixed-prime families; explicit quartic cancellation and literal rational parity replay |
| check_phase_tree.py | All 60 invariant choices; 8,191 distinct ordinary nodes through depth 12; all eight affine-shadow coefficient pairs |
| check_triangular_scripts.py | 208 substitution/length pairs; 40,640 zero-clock, 10,624 digit-exponent and 1,664 matrix identities |

[Exact execution receipt](EXACT_RECEIPT.json) includes both commands and log hashes
for each program. The printed finite results have their own logs in this report.
Their finite scope is not an enumeration proof of an infinite theorem.

## Complete checkout gate and publication

A complete, clean isolated checkout of PR189 at
`a0be70b1ffa075cbc50755ac76036108c028d120` passed the five-command default
repository validator. [Full receipt](PR189_CHECKOUT_VALIDATION.json) and
[raw log](PR189_CHECKOUT_VALIDATION.log) retain its precise checkout identity.

The new science commit `9eaf881dd7bc39a9945189e73c98ad5e0e9f1383`, tree
`576e71c079884bc8f0dcc63362bd006c7b034f6e`, passed all five commands with
363 tracked files. [The complete receipt](CHECKOUT_VALIDATION.json) records
that clean checkout before and after execution. The final commit is checked
again after adding this receipt; its result and publication identity are
recorded in the PR body. An integrity pass
checks structure, frozen identities and the stated bounded self-tests; it does
not certify Collatz. No frozen historical artifact, repository workflow,
permission setting, or existing main-branch theorem was changed.

The raw unified proof patch retains four space-only context lines required by
its format; Git’s whitespace check flags those lines. No scientific source
change was hidden by stripping or regenerating that hash-bound patch.

The initial remote PR194 commit `764f3a9f539febf3d2661a9ca4acc1b10827878c`,
tree `320f35a90349b4e2c9e8c4ad695d23d1a2ed9b34`, was fetched into a clean
complete checkout and passed all five commands with 364 tracked files.
[Its full published-head receipt](INITIAL_PUBLISHED_CHECKOUT_VALIDATION.json)
is retained. The final addendum changes documentation and source bindings only.
Its exact published-head validation is recorded separately in the PR body.
