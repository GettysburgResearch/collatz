# Evidence for the directed-return checkpoint

The [science packet](../../../research/ayh-resource-reset-20261124/directed-return/README.md) separates complete ordinary arithmetic theorems from the source-qualified probability and color-complexity deductions. **Collatz remains open.**

## Executed kernel and exact arithmetic

The root fresh [Lean execution](lean-build.json) compiled all local dependencies and the complete ordinary reverse-17 basin equivalence, using Lean 4.34.1, the pinned Mathlib checkout, `autoImplicit=false`, one worker and warnings treated as errors. Local objects were made in a new temporary directory and deleted on exit. The run exited 0 in 239.321 seconds. Its [full log](lean-build.log) and [82-declaration axiom audit](axiom-audit.json) contain only the standard `propext`, `Classical.choice` and `Quot.sound` dependencies.

The [affine source-accounting replay](finite-certificate.json) and its [optimized execution](finite-certificate-optimized.json) both passed, including equality between the JSON and Lean motif banks. The independent [whole-cylinder replay](whole-cylinders.json) and [optimized execution](whole-cylinders-optimized.json) covered all 59,049 length-ten cylinders and reconstructed all 1,007 source positions and their height maximum. Each normal/optimized pair has identical stdout. Logs are retained beside the receipts. These checks do not establish the written probability estimates.

## Mathematical reviews

- [Coordinator reconstruction and scope](ROOT_REVIEW.md).
- [Independent complete ordinary consumer and fixed-factor return](CONSUMER_AND_STRICT_RETURN_REVIEW.md).
- [Independent strict-return calculations and native entropy comparison](STRICT_ORDINARY_RETURN_REVIEW.md).
- [Independent width, lookahead and delayed-tie review](INTERIOR_AND_TIE_REVIEW.md).
- [Independent source census and chronological color-tree review](SELECTED_TRIT_CELLS_REVIEW.md).
- [Independent fixed-feature extraction review](FIXED_TRIT_PATTERNS_REVIEW.md).
- [Independent actual color-variation review](SELECTED_COLOR_VARIATION_REVIEW.md).

The final assembled wording has a separate review in `INTEGRATED_WORDING_REVIEW.md`. Each review applies to its named bytes and hypotheses, rather than to an entire branch. The full finite localization itself also has the independent root kernel build and full-cylinder replay described above.

## Source identity and publication

[Source hashes](source-hashes.json), [draft provenance](draft-provenance.json), the [latest PR intake](PR_INTAKE.json) and the [science source ledger](../../../research/ayh-resource-reset-20261124/directed-return/SOURCES.json) identify all dependencies and review boundaries. The initial fixed-query introduction is preserved in [its draft](drafts/FIXED_TRIT_PATTERNS.initial.md): it omitted the growth restriction on the extra ternary parameter in one opening sentence. The corrected theorem states that restriction and retains both advertised regimes. The quantitative formula was unchanged.

The [previous PR description](PRIOR_PR_DESCRIPTION.json) preserves the complete preceding checkpoint. Its historical logs and claims retain their original scope. The final new commit is validated from a clean complete checkout using `python -X utf8 -B tools/validate.py --receipt ...`; the exact remote head, tree and resulting receipt are then recorded in [PR197](https://github.com/GettysburgResearch/collatz/pull/197). No repository-integrity check is represented as a proof of Collatz.
