# Execution and review record: global synthesis

The scientific packet is
[research/global-synthesis-20261122](../../research/global-synthesis-20261122/README.md).
It extends PR178 without altering its earlier proof sources or receipts.

## Evidence levels

The four new substantive Lean modules have twenty public theorem
declarations. Their complete audit is
`research/global-synthesis-20261122/lean/GlobalSynthesisAudit.lean`.
The source modules also retain their focused audits. These kernel statements
are narrower than the complete written arithmetic and analytic arguments.

- [Arithmetic review](ARITHMETIC_REVIEW.md): effective independent-exponent
  classification and complete `P^aQ^b` exclusion, with the precise external
  Matveev input. The full real-logarithm application is written mathematics.
- [Ordinary-mass review](ORDINARY_MASS_REVIEW.md): finite-scale and truncated
  moment deductions from the explicitly pinned PDU hypothesis. The imported
  analytic population proof is not newly certified here.
- [Merger review](MERGER_REVIEW.md): exact ordinary clocks, certified-root
  injectivity, first crossing, and the preserved literal certificate tail.
- [Source snapshot](SOURCE_REFRESH.json): complete available metadata
  inventory and its selective mathematical inspection boundary.

## Reproducible execution

`validate_synthesis.py` requires a clean complete checkout at a supplied
exact commit, an existing Lean 4.34.1 runtime, and the pinned Mathlib checkout.
It rebuilds the required frozen `ShellCover` dependency, all new modules,
and their audits with one compiler job and warnings treated as errors.
It checks that every public theorem is audited and that each axiom closure
is a subset of `propext`, `Classical.choice`, and `Quot.sound`.

An optional fast-storage runtime is accepted only after every file is
verified byte for byte against the original pinned toolchain and dependency
cache, before and after execution. No dependency installation or network
download is performed. The validator records actual command outputs,
timings, source hashes, compiler identity, and checkout identity.

The publication execution also runs the exact rational certificate checker
under ordinary and optimized Python, independently regenerates its data,
and replays the supplied-certificate selector and finite graph controls.
The repository's five-command default integrity gate is recorded separately;
it checks repository structure and does not establish mathematical truth.

## Actual clean scientific-checkpoint execution

Tested commit: **`2eb1006fba0128006f09fa4279202334f61a233a`**.

Tree: **`66184e17a49e8eb2054d1ba73deac14710949420`**.

Complete checkout: **474 tracked files**, clean before and after.

The new Lean execution ran on 22 November 2026 from
**05:24:30.304036 to 05:25:41.443399 UTC**. The compiler build itself took
29.897 seconds; the surrounding execution includes byte authentication of
the fast-storage toolchain and dependency copy.

- [Lean receipt](proof-lean.json): all seven invocations passed: the one
  required frozen import, four substantive new modules, and two audit
  modules. All twenty public theorem outputs were present. Their combined
  axiom set is exactly `propext`, `Classical.choice`, and `Quot.sound`.
  `small_full_denominator_exclusion` depends on no axioms. No custom
  convergence assumption or `sorryAx` supplies a theorem.
- [Arithmetic and construction receipt](proof-artifacts.json): exact
  rational checker passed under normal and optimized Python, including four
  corrupted-certificate rejection controls. A byte-identical copy of the
  generator ran outside the checkout and regenerated identical certificate
  data. The normal and optimized selector outputs were identical: twelve
  supplied-tail fixtures, four complete acyclic finite graphs, fifteen G3
  fixtures, and five G4 certified roots.
- [Repository receipt](proof-repository.json): all five default commands
  passed on that same complete clean checkout. Optional historical
  regression bundles were not rerun.

Compiler: Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib: tracked-clean
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
The optional storage copy contained 26,343 files, 4,230,630,328 bytes;
every file matched its pinned original before and after execution.

Receipt SHA256 values:

| Receipt | SHA256 |
|---|---|
| Lean | `884eb74258061c92719e59ba271f69ecb7a4689f254329cc8185e01110849a2f` |
| Exact artifacts | `51f64ade481f2b7525938fbc44709fab1cbef3431af6129b8adcbc8dc445ef5c` |
| Repository gate | `54b9356d18215e9a55deb213eea7bdeb94a3edef9adc1ef38a5180e6eef33a3a` |

The publication follow-up adds these receipts and updates this report.
All compiled sources, exact-certificate inputs, and reviewed mathematical
notes retain their checked bytes. Earlier packet receipts retain their
own tested heads and are not relabeled as executions of this continuation.

## Separate closing refresh

[LATE_SOURCE_REFRESH.json](LATE_SOURCE_REFRESH.json) pins four branch heads
that advanced during the checked pass. The accompanying
[reconciliation](../../research/global-synthesis-20261122/LATE_REFRESH.md)
credits the parallel PR183 classification and records the stronger late
analytic and carry interfaces. This source inspection does not constitute
a replay of those branches' Lean modules. The twenty-statement count,
compiled source hashes, and scientific-checkpoint receipts above retain
their original scope.

The separate [late review](LATE_REFRESH_REVIEW.md) covers the source-scope
reconciliation and the new written tail-capture composition.
[late-capture-fixtures.json](late-capture-fixtures.json) records exact
compatible certificates and sixteen parameter controls; normal and
optimized Python produced identical bytes. These finite controls are not
substituted for the all-parameter proof.
