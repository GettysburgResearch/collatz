# Lean global attack: execution and independent review

The scientific entry point is
[`research/lean-global-20261121/README.md`](../../research/lean-global-20261121/README.md).
Full Collatz convergence remains **OPEN**. This directory keeps execution
evidence and focused reviews separate from the scientific development.

## Published checkpoint identities

The dedicated branch is `research/lean-global-20261121`, with
[draft PR178](https://github.com/GettysburgResearch/collatz/pull/178).
Its base is main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.

The first checkpoint is
`7e40cb5e09f4ed84b96eebf1d2e3fe43fdadf862`, tree
`16d1f890246755cd80e1243ef90a687b5646dfa4`. It contains the credited
PR174 core imports and the exact ordinary orbit-lifting/failure transport
module. Actual clean, complete-checkout receipts are preserved as
[`checkpoint1-lean.json`](checkpoint1-lean.json) and
[`checkpoint1-repository.json`](checkpoint1-repository.json).
The Lean build and its axiom audit passed; the repository gate with all
eleven bounded replay commands also passed. These receipts concern that
exact checkpoint, not files added afterward.

The next checkpoint adds the common rank, same-goal expanding psi family,
finite normalizers, conjugation, global coverage and inverse obstructions,
and the reviews below. Its exact commit and clean-checkout execution
receipt are recorded in the PR body **after** commit creation and actual
execution. This file does not predeclare a receipt for its own future SHA.

## Formal checking

The project pins Lean 4.34.1 and has no Mathlib dependency. From
`research/lean-global-20261121/lean`, run:

```sh
lake build
lake env lean -DwarningAsError=true FinalAudit.lean
```

[`FinalAudit.lean`](../../research/lean-global-20261121/lean/FinalAudit.lean)
prints the axiom dependencies of every public theorem in the new
`CollatzGlobal` modules, and the imported global reduction. Expected
dependencies are only Lean's standard `propext`, `Classical.choice`, and
`Quot.sound`; some theorems use fewer or none. No conjectural closure is
added as an axiom, and no `sorry` proof is accepted. The explicit remaining
statement is `ResidualPsiClosure`, which has no proof here.

Checking these formal statements does not formalize every source-qualified
ordinary negative-template proof. Those old legality and certificate
transformations stay visible hypotheses of the bridge interface.

The repository's required gate is run separately in a clean complete
checkout:

```sh
python -X utf8 -B tools/validate.py --receipt /outside/checkout-receipt.json
```

It checks repository structure and frozen integration identities. It is
not mathematical verification and is not substituted for the Lean build.

## Independent reviews and exact replay programs

| Review or program | Scope |
|---|---|
| [Common-rank review](../../research/lean-global-20261121/COMMON_RANK_REVIEW.md) | Finite-sublevel proof of well-foundedness and simultaneous induction; checks the actual source/clock coordinates |
| [Clock review](COMMON_RANK_CLOCK_REVIEW.md) | All 32 affine retained prefixes, whole-progression legality and no-padding source-clock increment for the eight frozen rows; independently checks `RankMoves.lean` |
| [Expanding psi review](PSI_EXPANSION_REVIEW.md) | Two ordinary seed paths, unbounded affine lifting, strict score guard, and the general family's conditional convergence scope |
| [Retraction review](RETRACTION_REVIEW.md) | Exact inverse-extension/normalization identity and its consequence for ranks of the source/clock pair in any well-founded relation |
| [Author coefficient/prefix checker](../../research/lean-global-20261121/check_common_rank.py) | Exact integer/rational guards and all-parameter lower bounds; retains older template legality as a dependency |
| [Independent affine checker](check_common_rank_clocks.py) | Separate constant/slope implementation over each complete CRT progression, using frozen [inputs](common-rank-clock-inputs.json) |

The two checkers print reproducible JSON; both ordinary and optimized
Python must agree byte for byte with their frozen outputs. The outputs
are [`common-rank-data.json`](../../research/lean-global-20261121/common-rank-data.json)
and [`common-rank-clock-report.json`](common-rank-clock-report.json).
They establish exact finite algebra, not a universal successful selector.

The reviews pin source hashes and state their actual execution scope.
Claims about arbitrary future rules, extra certificate padding, or ordinary
smaller-input floors are deliberately outside those pinned verdicts.
