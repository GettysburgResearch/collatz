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

Execution receipts and their exact tested commit are added after the clean
scientific-checkpoint run. Earlier packet receipts retain their own tested
heads and are not relabeled as executions of this continuation.
