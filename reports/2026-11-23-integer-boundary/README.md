# Checkpoint 15 execution and review evidence

Date: 23 November 2026. This report separates new-source execution, written
mathematical reconstruction, and the complete-checkout integrity gate.
None is a proof of the full Collatz conjecture.

The [scientific packet](../../research/lean-global-resolvent-20261121/overview/integer-boundary/README.md)
contains the statements, full arguments, explicit source qualifications,
and remaining global implications.

## New source checks

[new-source-checks.json](new-source-checks.json) records fresh strict
compilation of the real-separation module and its exhaustive declaration
audit. The module contains 10 theorems and 3 definitions. All declarations
were audited; the union is `propext`, `Classical.choice`, and `Quot.sound`.
There are no admissions, added mathematical axioms, or native proof
shortcuts. The literal ordinary inverse-series theorem keeps its reciprocal
budget as an explicit premise.

Lean: 4.34.1, compiler `5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`, with a clean tracked
source tree at execution. Existing Mathlib and package objects were reused.
The new module was compiled into a fresh temporary directory; no old
project Lean module was rebuilt.

Three exact Python controls passed normally and with optimization, with
identical outputs:

- Pressure: six actual convergent trajectories, 2,814 branch-filter cases,
  and 24,008 exact rational operator-coefficient comparisons.
- Numen: 512 inverse-prefix identities, six residue cases, and three
  rejected damaged-prefix controls.
- Band: 127 full matching-horizon controls and eight explicitly convergent
  pairs. The all-parameter conclusion is the written proof, not an
  extrapolation from these finite ranges.

The receipt includes the hashes of exactly the executed sources and the
complete Lean output. The verifier refuses to put its live receipt inside
the checkout; this copy was archived after execution.

## Independent written reconstructions

- [PRESSURE_REVIEW.md](PRESSURE_REVIEW.md) reconstructs the positive
  weighted quasimodes, exact defect, distance from the kernel, residue
  filters, and mixed equation, with exact reviewed hashes.
- [REVIEW_NUMEN.md](REVIEW_NUMEN.md) independently reconstructs both the
  irrational-preimage construction and the corrected two-place theorem.
  It also checks the primary literature's actual converse and hypotheses.
- [REVIEW_REAL_BRIDGE.md](REVIEW_REAL_BRIDGE.md) checks the Lean statements'
  semantic scope, literal dyadic specialization, and the budget conversion.
  Its semantic review is separate from the actual compiler execution.
- [ROOT_REVIEW.md](ROOT_REVIEW.md) records the coordinating researcher's
  reconstruction of the new band diagnostic and two-place argument, and
  the precise boundaries of the broad repository refresh.

These are scoped internal reviews. They are not a claim of external peer
review, formalization of the complete infinite arguments, or a new audit
of every imported analytic result.

## Source and repository scope

[pr-inventory.json](pr-inventory.json) contains 145 unique PR metadata
records obtained from the two listed queries. Some historical search
records do not supply a head SHA; that absence is preserved. Six newly
advanced branches supplied the 16 exact source-file pins in the packet's
[SOURCES.json](../../research/lean-global-resolvent-20261121/overview/integer-boundary/SOURCES.json).
The [band source ledger](band-source-pins.json) retains the original band
and lifting references as well.

The complete-checkout gate is run after committing these sources and
again on the fetched publication commit. Its receipt and exact published
head are reported in PR176. This gate checks repository structure and
scoped integrity controls, not the new mathematical theorems. No expensive
historical enumeration is part of this checkpoint.
