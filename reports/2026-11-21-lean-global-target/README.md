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
full convergence proof. Exact published-commit executions are recorded in the
PR body and retained here in a later checkpoint; the command must run before
its result can be attributed to that commit.

## Open global obligations

- Paired returns: prove a total ordinary return grammar with a well-founded
  charge, including expanding exits and orientation changes.
- Correction synthesis: prove that every required target receives a positive
  legal word with a successful terminal equation.
- Inverse pressure: control the ordinary primitive-endpoint tail in the
  required weighted norm; a probability-law contraction is insufficient.

No theorem here discharges a sufficient global obligation. The relevant
conditional implications remain explicitly conditional.
