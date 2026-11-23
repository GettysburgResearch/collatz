# Universal-step checkpoint: execution and review boundaries

23 November 2026. The [scientific packet](../../../research/lean-exact-witness-global-20261121/universal-step-20261123/README.md)
continues published PR177 head `f47a5ec51aa5853f104013a6d5046d6220ff7423`.
Full Collatz and the original residue implication remain open.

## What was newly checked

The coordinating agent freshly ran the **two new standalone Std-only Lean
modules** and the **four new exact Python checkers**, normally and with
optimization. All ten commands exited zero. The actual combined outputs
are preserved in [ROOT_REPLAY.json](ROOT_REPLAY.json).

Lean version: **4.34.1**, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`. Both modules were compiled with
`-j 1 -DwarningAsError=true`. All **21 public axiom audits** contain only
subsets of `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or
custom research axiom is present.

| New component | Formal or executed scope |
|---|---|
| `NegativeCandidate.lean` | Thirteen finite declarations: negative halving and clock, sharp backward-code bounds, executable ordinary-hit soundness, funded replay/completeness for literal first-crossing certificates |
| `BlockMixture.lean` | Eight all-length finite declarations: exact affine path composition, complete carry decomposition, and arbitrary mixed closed-path exclusion for a 6-smooth carry gap |
| `negative_candidate.py --self-test` | Sixteen known finite source fixtures, their unreduced presentations, 64 wrong candidates, two wrong crossings, one giant exponent, and sixteen sharp equality cases |
| `block_carry_capacity_check.py` | Exact full-carry schedules, common contexts, transposition families, general affine capacity controls, and invalid-input rejections; finite supporting coverage only |
| `check_balanced_transport.py` | Twelve residue/colour entries, 1,554 finite paired paths, physical valuation/cocycle identities, and three damaged tables |
| `check_unequal_blocks.py` | Twelve abstract unequal-shape affine cycles including minimum plateaus and pure-even blocks; fifteen literal sparse-defect identities; strict-threshold and invalid-hypothesis controls |

For each of the four Python checkers, normal and optimized outputs were
byte-identical. The cycle and commutator controls explicitly distinguish
abstract affine examples from actual Collatz parity blocks. No numerical
counterexample to Collatz is claimed.

Author receipts retain separate command records and source hashes:

- [Candidate receipt](candidate/REPLAY.json) and [scope](candidate/README.md).
- [Equal-shape cycle receipt](cycles/execution.json) and [scope](cycles/README.md).
- [Ordinary inverse-transport receipt](escape/CHECKS.json).

The full equality-to-Omega interpretation, polynomial bit-complexity
analysis, general nonsmooth cycle capacity, unequal-shape dictionary
theorem, and measure-theoretic escape results are **written proofs**.
They are not silently counted among the 21 Lean declarations.

## Internal reconstruction

- [Coordinating reconstruction](reviews/REVIEW_COORDINATING.md) covers the
  candidate, full-denominator cycle argument, and ordinary basin transport.
- [Negative candidate review](reviews/REVIEW_NEGATIVE_CANDIDATE.md) is by
  the escape lane, separate from the candidate author.
- [Unequal-block review](reviews/REVIEW_UNEQUAL_BLOCK_COMMUTATOR.md)
  discloses the cycle lane's earlier contribution to the strengthening.
- [Fresh unequal-block reconstruction](reviews/REVIEW_COMMUTATOR_CANDIDATE_LANE.md)
  is by the candidate lane, without contributing to that argument.
- [Ordinary basin and transport review](reviews/REVIEW_ORDINARY_ESCAPE_TRANSPORT.md)
  reconstructs both manuscripts at their exact source hashes. Its
  [independent finite controls](reviews/escape-independent-controls.json)
  are separate from the author's checker.

These are internal mathematical reconstructions, not external referee
acceptance. Each review applies only to its stated source hash and scope.
[SOURCES.json](SOURCES.json) records the selected peer heads and inspection
boundaries. [FILES.json](FILES.json) binds the checkpoint's other changed
files without a self-referential hash.

## Publication gate

The repository requires a clean complete-checkout integrity gate before
publication. Its final receipt is kept outside that checkout, and the
checked commit, matching tree, command outcomes, file count, and receipt
hash are recorded in the final PR description after execution. This report
does not invent a future gate result. Repository integrity is separate
from mathematical proof checking.

Only the new modules and checkers were replayed for this research
checkpoint. No old mathematical corpus or large historical census was
rerun. The frozen earlier packets and their formal sources remain unchanged.

## Strongest remaining uncertainty

The recognizer decides a supplied candidate and emits an actual complete
tuple on success. It does not construct a successful candidate from every
complete source witness. The cycle theorem does not cover arbitrary cycle
words or expanding block dictionaries. The inverse-tree compiler retains
an unbounded signed cost; no near-logarithmic ordinary Green comparison
or escape exclusion is proved.
