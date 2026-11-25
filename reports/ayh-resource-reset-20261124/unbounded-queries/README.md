# Execution and review: unbounded ordinary queries

The [scientific packet](../../../research/ayh-resource-reset-20261124/unbounded-queries/README.md) gives the statements, proofs, scopes and final Lean proposal. Collatz and the displayed universal `RemainingExclusion` remain OPEN.

## Actual current-pass execution

The root rebuilt **56 distinct repository modules**: 52 mathematical modules and four axiom-audit modules. The 44-module baseline was built into initially empty object storage, and no author objects were imported for the new module builds. The compiler was Lean 4.34.1 at `5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. Commands used `-j1 -DautoImplicit=false -DwarningAsError=true`.

The new packet adds **eleven mathematical modules and 49 public theorems**. The exhaustive final audit prints **253 unique public theorem declarations**, covering the entire compiled closure chain. Their axioms are subsets of `propext`, `Classical.choice` and `Quot.sound`. No `sorry`, `admit`, `native_decide`, new axiom or opaque escape was used. Each final Lean source hash matches its latest successful root compilation.

| Receipt | Actual scope |
|---|---|
| [baseline-execution.json](baseline-execution.json) | 44 fresh baseline compiles, all successful |
| [new-execution.json](new-execution.json) | Initial ten new mathematical modules plus initial audit, all successful |
| [final-extension-execution.json](final-extension-execution.json) | Wide pump and final assembly successful; first combined audit rejected a module doc comment before imports |
| [audit-execution.json](audit-execution.json) | Corrected combined audit successful, all 253 declarations printed |
| [axiom-audit.json](axiom-audit.json) | Exact declaration set, final source hashes, allowed axioms and invocation counts |
| [finite-execution.json](finite-execution.json) | Eight root executions: three scientific programs and independent tower reviewer, each normal and optimized |
| [wide-finite-execution.json](wide-finite-execution.json) | Two root executions of the independent wide-parameter modular reviewer |

There were 58 successful compiler invocations and one failed audit invocation. The failed invocation was an import-position error in the generated audit file; moving the module doc comment after the imports fixed it. The mathematical module sources did not change for that correction. All final compiled files are covered by successful receipts. This history is retained rather than relabeled as a single failure-free run.

The ten Python executions all passed. Each normal/optimized pair produced identical output. They checked 252 physical carry controls, six literal checkpoint mergers, eleven preassigned binary-power certificates, five fixed-class controls, the 68-input all-clock trap, seventeen rational-center parameter lifts, and two complete large positive pump traces. The tower replay checked 18,240 return clock pairs and 309,385 lower-cone meetings. Its independent reviewer checked twelve exact asynchronous deadlines. The wider-row reviewer checked exact thresholds and all three output-digit lifts at nine depths, including 404, 405 and 406. These counts describe finite executions, not the scope of the universal Lean theorems.

## Independent mathematical reviews

- [Root review](ROOT_REVIEW.md): statements, physical interpretation, quantifiers, source-specific consumers and final-source compilation.
- [Checkpoint cross-review](CHECKPOINT_CROSS_REVIEW.md): independently reconstructed off-grid identity, all-earlier criterion and original-parent consumer.
- [Center cross-review](CENTER_CROSS_REVIEW.md): cofinal ordinary construction, actual height comparison, denominator theorem and exact parameter classes.
- [Wide-center review](WIDE_CENTER_REVIEW.md): 405 threshold, three-digit shift and full progression exclusion, with a separate strict build.
- [Fixed-tower review](INDEPENDENT_FIXED_TOWER_REVIEW.md): reflection, all-smaller-base orientation and final exact-deadline theorem, with a separate strict build.
- [Source comparison](SOURCE_REVIEW.md): the frozen PR192, PR193, PR195, PR201, PR206 and PR210 interfaces and the relevant literature. Source inspections do not imply builds of every upstream file.

The author tower receipt and log are retained with their author scope. The root receipts above are separate executions. Internal agents and the root supplied these reviews; no external referee acceptance or remote CI run is claimed.

## Publication boundary

The research branch is `research/ayh-resource-reset-20261124`, continuing draft PR197 from `10d87fee615d1095990d6b7ea329126b4cf7aa5a`. The previous PR description is archived in [PRIOR_PR_DESCRIPTION.json](PRIOR_PR_DESCRIPTION.json). [OPEN_PR_INTAKE.json](OPEN_PR_INTAKE.json) records the forty-item metadata snapshot; it is not a full mathematical review of forty branches.

[source-hashes.json](source-hashes.json) seals the delivered scientific and report files, excluding itself. [initial-source-manifest.json](initial-source-manifest.json) preserves the agent-source inputs before the root extended the final assembly and audit. The final source hashes in the axiom receipt take precedence for compiled files.

After publication, the root runs `python -X utf8 -B tools/validate.py` in a clean, complete checkout of the actual published commit. Its exact receipt and hash are placed in the PR description. That event checks repository integrity and selected fixtures; it is separate from the mathematical build above. The report does not claim an execution merely because the validation command exists.
