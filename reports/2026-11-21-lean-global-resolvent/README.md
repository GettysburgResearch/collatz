# Lean global-attempt checkpoints

## Checkpoint 1

The [scientific guide](../../research/lean-global-resolvent-20261121/README.md) identifies the exact theorem statements and open closing conditions. [checkpoint1-lean.json](checkpoint1-lean.json) records the actual core build and axiom audit, including every compiled source hash. The accompanying logs preserve actual output.

The new proofs establish exact least-failure geometry, source-rank normalization and global equivalences. They do not discharge the closing assertions. Principal dependency reports contain only `propext`, `Classical.choice` and `Quot.sound`.

Repository structural validation is run on the full clean published checkout. Its exact commit, result and receipt are recorded in the pull request. Scientific compilation and repository integrity are different checks; neither an equivalence nor a structural gate is a full convergence proof.

## Checkpoint 2

[checkpoint2-lean.json](checkpoint2-lean.json) pins the actual compiled core
and Mathlib sources and the three execution logs. The core build and axiom
audit passed. The standalone Mathlib module compiled with warnings treated
as errors and printed only standard Lean axioms for its principal theorems.

This checkpoint adds the common certificate-order kernel, exact universal
checks of the two longer paired replacements, the uniform even-exponent
Mersenne fold, and the full component-preserving asynchronous normalization.
The six upper/lower path checks use actual natural-number arithmetic
for every parameter; they are not a numerical sample. All-input rule coverage
and the arithmetic repair conditions remain open.

Lean: `4.34.1`, commit `5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.

## Checkpoint 3

[checkpoint3-lean.json](checkpoint3-lean.json) records the exact final sources
and four actual Lean execution logs. The core project, its axiom audit, the
complete-certificate Mathlib module and the primitive-source Mathlib module
all passed. Every audit command treated warnings as errors. Principal theorem
dependencies are only the standard Lean axioms, with no `sorryAx`.

The new unbounded reset proves its full variable-length paths and strict
bound on every source state under explicit arithmetic guards. The analytic
module proves its source partition, exact survivor decomposition, complete
geometric tail bound and equivalence with full ordinary convergence. It does
not prove decay of the primitive-source sum. The valuation selector and the
restricted-fold invariant remain written proofs with their scope stated in
the research packet.

The short `check_flux_obstruction.py` replay was executed once on the published
script before this checkpoint. It confirmed the specified fixed-loss
counterexample using exact integers and fractions. Its analytic all-source
tail is justified in the note; this finite replay is not a Lean proof of a
global survival estimate.

## Checkpoint 4

[checkpoint4-lean.json](checkpoint4-lean.json) pins the broader core reset,
the odd-state certificate measure, and their composed Mathlib theorem.
The core build and audit, compilation of the odd-state module to its actual
importable output, and compilation of the composed reset all passed with
warnings treated as errors in the audit commands. The final two composed
theorems depend only on `propext`, `Classical.choice`, and `Quot.sound`.

The generator verifies the frozen core-source hashes. Lean then rechecks the
extracted proof bodies and the exact equality of the two iteration
conventions. The theorem is therefore a single checked statement about
every complete supplied certificate under the stated arithmetic guard;
there is no assumed interface between the two proof projects.

The normalized-unit selector and the final different-exit obstruction are
written arguments, explicitly distinguished from the compiled module set.
No all-state selector or primitive-moment decay proof was obtained.
