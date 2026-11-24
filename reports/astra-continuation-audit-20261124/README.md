# Exact-clock and directed-cover verification checkpoint

The science entry point is
[Exact-clock amplification and directed single-residue closure](../../research/killed-green-head-closure-20261124/FINITE_CLOSURE.md).
Collatz remains open. These reports distinguish independently reconstructed
written arguments, finite controls, and formal finite theorems.

## Executed Lean verification

The [pinned runner and instructions](lean/README.md) and
[receipt](lean/RECEIPT.json) record 13 actual compiler executions:
four import-only original-source checks, seven verified modules, and
two generated complete affine-cover certificates. Every process exited
zero. All final module and certificate diagnostics are empty. The
original import-only KilledMoment and OctavePhase checks retain their
benign linter/exponentiation warnings verbatim in the receipt.

There are **46 distinct checked theorem declarations**: 22 from the
earlier candidates and 24 new ones. An additional 24 definitions,
inductives and structures were axiom-audited, giving 70 distinct
audited declarations. The four original-source executions separately
recheck the 22 original theorems; they do not increase the distinct
count. The two closed full-table decisions have no axioms. The
universal directed-tripling applications use only `propext` and
`Quot.sound`. The allowed union over all named declarations is
`propext`, `Classical.choice`, and `Quot.sound`.

Toolchain: Lean 4.34.1, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`; mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Runs used one worker
and reused the pinned prebuilt dependency cache. New project inputs
were reconstructed in temporary directories. The original four
umbrella-import files were not run unchanged; the import-only scope
is explicit. Receipt SHA-256:
`d08f6621c59ff586fd0588fdcf7fe89991e3fb741eb3769fdc2069be1fb2b313`.

## Exact finite programs

[NEW_CONTROLS_REPLAY.json](NEW_CONTROLS_REPLAY.json) binds source and
output hashes for fresh normal and optimized Python executions. Both
programs had zero AST `assert` nodes; checks remain active under `-O`.
Outputs agreed byte for byte and matched their stored expectations.

* The inverse construction replay checked 6,760 two-gap cases, three
  sharp-cutoff exclusions, 480 inverse-vs-forward row comparisons and
  40,336 literal padded sources. These last sources lie on four actual
  finite climbing prefixes, with maximum shortcut clock 448; they do
  not assert a nonconvergent orbit.
* The directed checker replayed 948 and 1,263 whole-progression leaves,
  totaling 84,642 affine letters and 5,026 forward query positions.
  Its arithmetic check applies to each entire nonnegative parameter
  progression. A separate recursive parser and direct affine replay
  independently recovered the same coverage and distortion bounds.

[PRIOR_CONTROLS_REPLAY.json](PRIOR_CONTROLS_REPLAY.json) records fresh
Node executions of all four originally published BigInt controls,
with matching original result payloads. Their historical wrappers and
source code were preserved. Exact integer checks also certify the
explicit constants in the simple-path and clock-slack arguments.

## Independent reviews and source boundaries

* [Coordinator reconstruction](ROOT_REVIEW.md): core arithmetic,
  elementary simple-path argument, directed checker semantics and
  the conditional status of the earlier analytic floor.
* [Finite-row cross-review](ESCAPE_CROSS_REVIEW.md): both nonconvergent
  alternatives, the actual fixed suffix, source distinctness,
  the cycle threshold and the version using only the recorded path.
* [Directed-cover cross-review](GLOBAL_CROSS_REVIEW.md): full infinite
  progression coverage and the ordered-cut interval inequality;
  imported downstream analytic results are outside this verdict.
* [Overview review](OVERVIEW_REVIEW.md): the explicit source cutoff,
  exact forward enumeration and the corrected endpoint/horizon scope.
* [Source intake](SOURCE_INTAKE.json): exact reviewed branch heads.
  This is not a blanket certification of every file on those branches.

The finite-row dichotomy and asymptotic transfers are written proofs,
not fully formalized Lean theorems. The missing uniform upper bound,
directed basin implication, and all remaining analytic inputs are
stated in the science packet. The required checkout validator checks
repository structure rather than mathematical truth. Publication
receipts will identify the actual remote commits checked.
