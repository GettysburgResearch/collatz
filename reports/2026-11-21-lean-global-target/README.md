# Lean global-target checkpoint records

The science is in
[the research packet](../../research/lean-global-target-20261121/README.md).
This pass began from main ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a and
froze the current source heads listed in that packet's SOURCES.md.

The new branch is `research/lean-global-target-20261121`. Its first checkpoint
contains the completed Lean modules, their source notes, a reproducible
dependency audit, and the unchanged pinned imports.

`check_lean.py` records actual Lean execution and printed declaration axioms.
Repository `tools/validate.py --regressions` separately checks a clean complete
checkout's integrity and selected bounded regressions. Neither record is a
full convergence proof.

## Published checkpoint 1 execution

PR: [181](https://github.com/GettysburgResearch/collatz/pull/181).
The remote branch was read back before its exact commit was checked out into
a clean, complete working tree.

- Commit: 352bbb78234991e332153a180de9c2d6b028868b.
- Tree: 87fd46683b54cfb910a4fce0baad23b92511a1ad.
- [Lean execution receipt](checkpoint1-lean.json): build and warning-as-error
  audit passed; all 29 audited declaration dependency lists are subsets of
  propext, Classical.choice, and Quot.sound. Imported file hashes and the
  before/after source hashes matched.
- [Complete-checkout receipt](checkpoint1-checkout.json): all 11 commands of
  the required integrity and bounded-regression bundle passed; 341 tracked
  files, with unchanged commit/tree and clean tracked files afterward.
- The signed-debt Fraction replay also exited zero on that same checkout,
  reproducing the three carry controls and four valuation controls recorded
  in its adjacent note. This is bounded computational evidence.

These receipts identify checkpoint 1. They do not retroactively attest to
later documentation or source changes. The current PR body identifies any
subsequent exact-head execution.

## Open global obligations

- Paired returns: prove a total ordinary return grammar with a well-founded
  charge, including expanding exits and orientation changes.
- Correction synthesis: prove that every required target receives a positive
  legal word with a successful terminal equation.
- Inverse pressure: control the ordinary primitive-endpoint tail in the
  required weighted norm; a probability-law contraction is insufficient.

No theorem here discharges a sufficient global obligation. The relevant
conditional implications remain explicitly conditional.
