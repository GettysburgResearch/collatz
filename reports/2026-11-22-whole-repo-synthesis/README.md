# Execution and review scope

**22 November 2026.** This report accompanies the
[actual-orbit synthesis](../../research/whole-repo-synthesis-20261122/README.md).
It records finite executions and scoped mathematical review. It does
not certify full Collatz, the entire repository, or the pinned external
canonical constructions.

## Lean execution: PASS

The new proof module and its separate audit module compiled with Lean
4.34.1, compiler commit 5045d0056413266e57c625dcd7c365b10e377c52.
Both commands used automatic implicit variables disabled and warnings
treated as errors; both exited zero.

The audit covers **all 12 public declarations: 10 theorems and two
definitions**. The dependency union is exactly propext, Classical.choice,
and Quot.sound. No added axiom, admitted proof, or native-decision proof
step is present in the new source.

The composed theorem starts with literal natural-number Collatz edge
equalities, positivity, and distinctness. It proves the actual
logarithmic correction budget and the integer-frequency Fourier bound.
It does not assume a phase recurrence as an extra premise.

- [Exact compiler commands, source hashes and axiom inventory](lean-build.json).
- [Separate audit output](lean-audit.log).
- [Main compiler output](lean-compile.log); empty output with exit zero.
- [Reproducible build driver and formal scope](../../research/whole-repo-synthesis-20261122/phase/lean/README.md).

Mathlib was pinned at d13f23b723b8a846827a245b89c10fc7d3f11612,
tracked-clean, with four direct import source hashes checked. Existing
transitive dependency objects were reused. Only the two new project
modules were freshly compiled; this is not a Mathlib source rebuild or
a replay of the historical Lean corpus.

The compilation occurred in the development checkout with all output
outside it. The proof module, audit module and driver are bound to exact
SHA256 values. Publication verifies that the fetched proposed commit
has those identical source bytes rather than running an unnecessary
second compilation of unchanged code.

## Written mathematics

The Rhin linear-form input was inspected in the primary
Lagarias--Soundararajan paper, Lemma 5.3 and equation (5.11). The original
Rhin book chapter was not independently reconstructed. The finite
continued-fraction block argument and its optimization, binary-prefix
count, and polynomial moment deductions were reconstructed by another
researcher and checked against the final phase-note bytes.

Rhin, continued fractions, the discrepancy theorem and run consequences
are not formalized by the new Lean module. The energy application
retains its explicitly pinned canonical-energy premise. The entropy
and high-spike deductions similarly retain their ordinary harmonic,
contact and trace inputs.

[Review associations, contributions and exact publication hashes](REVIEW_SCOPE.json)
distinguish full phase review from narrower cross-reviews. These are
independent in-session mathematical reconstructions, not external
peer review or acceptance of all analytic inputs.

## Exact whole-word control: PASS

The arithmetic checker was executed normally and with Python
optimization enabled. Both executions exited zero and reproduced the
frozen fixture byte for byte.

The checker verifies a complete finite inverse-closure control, the
source-grade maxima used in its written all-word argument, and a
forward-closed set containing every positive start below 1263. Closure
establishes that none of those smaller sources at any natural inverse
clock hits target clocks 0 through 24. The first actual merger is at
target clock 25 and descent at 26.

[Commands, fixture hash and execution output](arithmetic-check.json)

This finite control does not prove the universal merger selector. Its
particular target converges. The arbitrary-word grade classification
also uses the written induction recorded in the accompanying note;
the finite executable is not labeled as an independent formalization
of that induction.

## Repository and publication gate

The [source snapshot](../../research/whole-repo-synthesis-20261122/SOURCE_SNAPSHOT.json)
inventories 145 PRs and freezes the selected inputs. Four late advanced
heads were incorporated into the synthesis. Their claims remain
attributed to their own exact source versions.

The [file inventory](FILES.json) binds every file in this checkpoint
other than the inventory itself, including the continuation link added
to the previous packet. The previous PR description is preserved in
[pr-description-before.json](pr-description-before.json).

Before moving the branch reference, the proposed GitHub commit is
fetched into a clean complete checkout. Its source and review hashes
are compared with these receipts, and the required five-command
repository validator is run there. The exact commit/tree/receipt
identity and observed result are recorded in PR178's published
description. That validator checks repository integrity and its
specified bounded controls, not the infinite mathematics. The optional
historical regression bundle is not part of this checkpoint.

Publication uses an expected-parent, non-forced branch update, followed
by an independent readback of the PR head and branch ref.
