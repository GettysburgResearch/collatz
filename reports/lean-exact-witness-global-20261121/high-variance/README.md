# Checkpoint fifteen: finite boundary, atomic pressure, and cycle carry

Date: 23 November 2026. Parent: `0444986571f09f302cb3687b4bba3552600e4119`.

**Full Collatz, the original residue-512 implication, and `FloorIntervalStep`
remain OPEN.** This checkpoint develops three direct closing attacks and
records their proved results and precise remaining steps.

## Scientific results

| Lane | Completed result | Remaining closing step |
|---|---|---|
| [Witness boundary](../../../research/lean-exact-witness-global-20261121/HIGH_VARIANCE_WITNESS.md) | Every arbitrary complete capturing witness reduces to a finite ordinary boundary; exact global minimum grade and maximum-source tie; finite optimizer and record plateau/jump laws | Actual entry of the original target into the certified graph or an original-target contradiction |
| [Ordinary atomic pressure](../../../research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md) | Elementary positive path product; exact Haar multiplier; strict actual-gap surplus; ordinary Green source sum; complete classification of finite positive ordinary atomic eigenmeasures | Exclusion of the nonzero ordinary atomic cone, which is equivalent to escape existence |
| [Cycle arithmetic](../../../research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ARITHMETIC.md) | Cyclic discrepancy in terms of the actual minimum; run-moment consequences; full-denominator integer carry and M-matrix class | All-word exclusion of the nontrivial zero class; neither the bounded carry box nor the general M-matrix theorem supplies it |

The new pressure/eigenmeasure results reconstruct their orbit-count input
directly. They do not depend on the earlier source-qualified canonical
envelope, predecessor-density or mixing construction. The cyclic power
estimate uses the precise Rhin inequality reproduced in the cited primary
Lagarias–Soundararajan paper; its original proof was not replayed.

## Focused Lean execution

[Actual replay receipt](checkpoint-fifteen.json),
[target build](checkpoint-fifteen-build.txt),
[strict source compilation](checkpoint-fifteen-strict.txt), and
[five-theorem axiom output](checkpoint-fifteen-axioms.txt).

- Lean 4.34.1, compiler `5045d0056413266e57c625dcd7c365b10e377c52`.
- Core Lean only; no Mathlib or external theorem axioms.
- New `Collatz.FiniteSourceBoundary` target built successfully.
- Fresh source compilation and exhaustive audit of its five public theorems,
  both with warnings treated as errors: PASS.
- Axiom union: `propext`, `Classical.choice`, `Quot.sound` only.
- All 45 inherited Lean source files outside the two updated aggregate/audit
  indexes match checkpoint fourteen by SHA256.
- The witness author cold-built the 20 required existing modules after the
  local object cache was unavailable. The coordinating replay reused those
  objects. [Dependency build transcription](dependency-build-transcript.json)
  explicitly distinguishes the earlier executed tool results from a fresh replay.
- Unrelated earlier proof modules and the full historical 308-declaration
  audit were not rebuilt. Adding the five names to the full audit index is
  not reported as rerunning that historical audit.

The five new public theorems are `last_exit`, `trim_certificate`,
`minimum_on_boundary`, `boundary_minimum_iff`, and `boundary_maximum_iff`.
The finite graph algorithm, record laws, infinite pressure results and cycle
analysis remain written mathematics. No `sorry`, custom conjectural axiom,
or native proof shortcut was added.

## New exact executable controls

The [finite graph replay](finite-source-boundary-replay.json) checks all
383 boundary certificates for the two specified targets and recovers their
global selected sources 1092 and 2184. Three damaged graph certificates are
rejected in both normal and optimized Python. Both executions have identical
output: [normal](finite-source-boundary-normal.json),
[optimized](finite-source-boundary-optimized.json).

The [arithmetic replay](arithmetic-controls-replay.json) checks the pure
dyadic M-matrix counterexample, all seven nonempty binary firing supports,
the displayed rational cycle and reduced inverse, and the nine-state
even-divisor circulation with determinant 797 and eight-step carry
termination. It also checks the exact integer margin in the orbit-cylinder
count. [Normal](arithmetic-controls-normal.json) and
[optimized](arithmetic-controls-optimized.json) outputs agree. The divisor-ten
control is explicitly **not** a Collatz cycle.

These are targeted checks of new finite constructions and proposed closing
shortcuts. They are not an expanded cycle census or a proof of target
convergence. The reproducing scripts are
[finite_source_boundary.py](../../../research/lean-exact-witness-global-20261121/finite_source_boundary.py)
and [arithmetic_carry_controls.py](../../../research/lean-exact-witness-global-20261121/arithmetic_carry_controls.py).

## Independent written reviews and frozen sources

- [Witness reconstruction](REVIEW_WITNESS.md): last-exit geometry, original
  grade order, all-certificate completeness, finite graph and record laws.
- [Escape reconstruction](REVIEW_ESCAPE.md): elementary product estimate,
  operator domains and Haar normalization, atomic measure construction and
  converse, complete cone classification, full topological support and
  exact integrability/norm obstructions.
- [Arithmetic reconstruction](REVIEW_ARITHMETIC.md): cyclic averaging,
  whole-denominator unit certificate, height-layer correction, integer
  carry and M-matrix controls, with external theorem scope distinguished.
- [Source snapshot](SOURCES.json): eight current PR head pins and 13
  selected exact file hashes. This is not a claim to re-audit every branch.
- [File manifest](FILES.json): source and execution artifacts belonging to
  this checkpoint, excluding the manifest itself.

The required default repository validator is run before publication in a
clean complete checkout of the proposed commit. Its exact checked commit,
tree, command results and receipt digest are recorded on PR177 after that
execution. The optional historical regression bundle is not part of this
focused checkpoint. Repository integrity does not certify mathematics.
