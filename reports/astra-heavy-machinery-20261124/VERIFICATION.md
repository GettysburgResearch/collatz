# Verification of the heavy-machinery checkpoint

The scientific packet is `research/astra-heavy-machinery-20261124/`. It adds eleven public finite arithmetic theorems in three Std-only Lean files. All passed the root replay under official Lean 4.34.1, with `-j1 -DwarningAsError=true`, explicit queries for every public theorem's axioms, and no axioms outside `propext`, `Classical.choice`, and `Quot.sound`.

| Module | Public theorems | Scope |
| --- | ---: | --- |
| `ergodic/ErgodicWindow.lean` | 6 | Integer rounding, exact divisibility, finite word legality, and changing-denominator obstruction |
| `diophantine/MahlerCore.lean` | 3 | Weighted signed affine step, block-defect cancellation, and clock-one identity |
| `dynamics/KernelTransfer.lean` | 2 | Ordinary inverse digit and all-high-digits ternary-to-dyadic row realization |

The actual run and source hashes are in `LEAN_AND_CONTROLS.json`. The check driver makes audited copies with all axiom queries, verifies that source bytes remain unchanged during compilation, and records both source and copy hashes. The compiler logs are preserved alongside this report.

Four finite-control programs passed both in normal Python and with optimization enabled; their outputs agreed exactly. Their explicit checks remain active under `-O`.

| Program | Coverage recorded in the run |
| --- | --- |
| `ergodic/check.py` | 9,009 ordinary prefix/residue/rank constructions, including exact threshold rank, common endpoint and additive identity; largest witness 4,433 bits |
| `diophantine/check.py` | 250 rational starts × 40 steps; 1,364 full cycle words; seven explicitly convergent sources; 100 dyadic and 372 mixed rows |
| `diophantine/mixed_check.py` | 260 positive ordinary witnesses separating a source-time translate from five competing translates |
| `dynamics/controls.py` | All 2,186 ternary-unit rows through depth seven at five high digits each; exact timed-predictor comparison for sources through 20,000 |

The timed predictor deliberately leaves some true positives unrecognized within its finite clock: 3,313 target-one and 2,575 target-five examples in the tested range. The source-qualified asymptotic statement is about density of the missed true positives as the range tends to infinity, not about success throughout this control range. No extrapolation from finite controls is used.

Independent written reviews are retained in the diophantine lane, with exact target hashes. `ROOT_REVIEW.md` records a separate reconstruction of the new arguments and the narrow repair to the potential note. External analytic results and their formalization libraries were read at named versions, not rebuilt.

The repository's clean-complete-checkout validator is run separately on the committed checkpoint, with its receipt outside that checkout. Its result is a repository-integrity check, not an additional mathematical theorem. The earlier proof bundles were not rebuilt for this literature-driven continuation.
