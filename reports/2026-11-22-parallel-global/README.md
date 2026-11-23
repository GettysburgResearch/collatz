# Checkpoint 8 execution evidence

The scientific guide is
[the parallel attack packet](../../research/lean-global-resolvent-20261121/overview/parallel/README.md).
This directory holds process evidence rather than another statement of
the mathematical frontier.

[checkpoint8-lean.json](checkpoint8-lean.json) records the successful
fresh-output execution of the portable driver. The executable and
Mathlib checkout match the exact commits recorded in the receipt.

- 14 frozen PR177 dependency modules and 4 new proof modules compiled.
- Both public audits compiled; 44 theorem outputs were counted.
- All 20 commands exited zero with warnings treated as errors.
- Axiom union: `propext`, `Classical.choice`, `Quot.sound`.
- All 20 source/audit hashes were unchanged by execution.
- The optional dependency mirror had 8,620 object/IR artifacts checked
  against the pinned original artifacts before it was used.

This receipt is evidence for the formal modules and their exact imports.
It does not claim that the written infinite analysis, source-qualified
analytic inputs, or open contact/merger estimates are Lean theorems.

The repository-integrity gate is separate. Publication runs
`python -X utf8 -B tools/validate.py` on a clean complete checkout and
records the actual published head and result in the PR. A repository
integrity pass is not additional mathematical evidence.
