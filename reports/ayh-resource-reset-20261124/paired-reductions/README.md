# Paired reductions: execution and independent review

**Overall mathematical status: OPEN.** The final consumer is a checked conditional equivalence. Its input `RemainingExclusion` has not been proved. The [scientific packet](../../../research/ayh-resource-reset-20261124/paired-reductions/README.md) keeps proved source exclusions, written extensions, finite replays and the open step separate.

## Fresh source execution

The root coordinator restored Lean 4.34.1 and Mathlib at the exact pins in the scientific README. The root object directory began empty. No author-generated repository-local object was copied into it.

| Batch | Compiler invocations | Successful elapsed seconds | Receipt |
|---|---:|---:|---|
| Previous source, rebuilt at baseline `156652e03fe7a78f9cd4442039779cc622fdf3de` | 31 | 733.222 | [baseline-execution.json](baseline-execution.json) |
| New research modules | 11 | 44.484 | [new-execution.json](new-execution.json) |
| Final assembly and exhaustive new audit | 2 | 2.875 | [assembly-execution.json](assembly-execution.json) |
| Final whitespace normalization and affected closing consumers | 5 | 16.519 | [formatting-execution.json](formatting-execution.json) |
| Total | 49 | 797.100 | Four actual batches, covering 41 distinct mathematical modules and three audit modules |

Each compiler invocation used `-j1 -DautoImplicit=false -DwarningAsError=true`. The final new-audit file initially placed a module documentation command before imports; this syntax error was corrected to an ordinary comment and the audit was recompiled successfully. A final staged whitespace check then found three trailing-space occurrences in two modules. Their removal, original hashes, final hashes and reversible line changes are recorded in [formatting-provenance.json](formatting-provenance.json). The fourth receipt records fresh strict compilation of those modules and their affected closing consumers. The last recorded execution of each path matches its final published bytes. There was no mathematical change.

The [axiom audit](axiom-audit.json) covers **204 distinct public theorem declarations**, including **all 52 non-private theorem declarations in the twelve new mathematical modules**. A source-declaration census matched the audit with no missing or extra names. Every reported dependency is a subset of `propext`, `Classical.choice`, and `Quot.sound`; no sorry axiom, custom convergence axiom, native-decide axiom, or unchecked closing input appears. This check does not prove the explicit argument of the conditional final theorem.

The standalone [check_lean.sh](../../../research/ayh-resource-reset-20261124/paired-reductions/check_lean.sh) reproduces the same 44-module dependency order in a fresh temporary directory. It is provided as a replay command; the execution evidence for this pass is the four recorded batches above.

## Exact finite replays

[finite-execution.json](finite-execution.json) records six checkers, each run normally and under `python -O`, with matching outputs. The programs use explicit failure checks that remain active under optimization. They cover:

- Checkpoint signed words, exact valuations, selected cofactor rescues and rational lifts.
- All thirteen rational-center rows, the guarded residue census and the complete finite integer-reference inversion.
- The small ordinary cutoff, exact 1024-clock integer thresholds and full ternary permutation census.
- Every one of the 67 smaller source candidates and the parent phase uniqueness certificate.
- 6,776 normalized checkpoint values against 108,416 comparator values in the 32-trajectory follow-up; all 2,314 meetings obey the stated constraints.
- An independent direct-integer reconstruction of 26 large positive members of the thirteen full progressions, plus 64 guarded-row executions and the integer-anchor census.

The independent [check_rewrite_independent.py](check_rewrite_independent.py) differs from the reviewer's staged script only in its path to the sibling scientific directory. It retains the source-hash guard and all arithmetic checks. These replays supplement the mathematical proofs and cannot establish universal convergence by finite testing.

## Independent reviews

Three GPT-6.2 Astra delegates ran at the user's requested **ultra** effort. Each research packet was checked by a different delegate, and the coordinator rebuilt all imported local source. Reviews are pinned to the exact file hashes they cover.

| Scope | Evidence and review |
|---|---|
| Four rewriting modules, complete integer-reference obstruction, thirteen rational rows and guarded bank | [INDEPENDENT_REWRITE_REVIEW.md](INDEPENDENT_REWRITE_REVIEW.md) |
| Five clock, rank and ternary modules; current upstream claim distinctions | [CLOCK_AND_TERNARY_REVIEW.md](CLOCK_AND_TERNARY_REVIEW.md) |
| Checkpoint unit exits and full written simultaneous-delay argument | [CHECKPOINT_REVIEW.md](CHECKPOINT_REVIEW.md) |
| All-clock 67-source certificate and separately written denominator transfer | [INDEPENDENT_CENTER_PHASE_REVIEW.md](INDEPENDENT_CENTER_PHASE_REVIEW.md) |
| Full written 32-comparator theorem within its exact clock windows | [THIRTY_TWO_REVIEW.md](THIRTY_TWO_REVIEW.md) |
| Final conditional consumer at its exact final hash | [CLOSING_PROPOSAL_REVIEW.md](CLOSING_PROPOSAL_REVIEW.md) |
| Coordinator's mathematical checks and source boundaries | [ROOT_REVIEW.md](ROOT_REVIEW.md) |
| Replay dependency order, exact upstream bytes and publication scopes | [PUBLICATION_READINESS.md](PUBLICATION_READINESS.md) |
| New PR192, PR195 and PR206 heads observed just before publication | [LIVE_SOURCE_SYNTHESIS.md](LIVE_SOURCE_SYNTHESIS.md) and its three pinned source reviews |

The full simultaneous delay, source-population tail, integer-reference obstruction, rational denominator transfer, and 32-comparator theorems have written proof scope. Their listed Lean kernels prove the stated algebraic or finite portions; the reports do not relabel every written extension as a Lean theorem. In particular the checkpoint population upper tail remains qualified by the exact PR146 source identified in the science ledger.

## Source and publication boundary

[OPEN_PR_INTAKE.json](OPEN_PR_INTAKE.json) freezes metadata for the forty most recently updated open PRs at initial intake. [SOURCES.json](../../../research/ayh-resource-reset-20261124/paired-reductions/SOURCES.json) records 42 exact source-file readings from the four initially changed relevant PR heads, the freshly rebuilt baseline, and the literature. A second live refresh and exact-head source review covers the subsequently changed PR192, PR195 and PR206; see [LIVE_PR_INTAKE.json](LIVE_PR_INTAKE.json) and [LIVE_SOURCE_SYNTHESIS.md](LIVE_SOURCE_SYNTHESIS.md). The prior PR197 title and full body are preserved in [PRIOR_PR_DESCRIPTION.json](PRIOR_PR_DESCRIPTION.json).

[initial-source-manifest.json](initial-source-manifest.json) records unchanged copies from the research delegates. [source-hashes.json](source-hashes.json) pins final scientific, report and navigation bytes, excluding itself to avoid self-reference.

The publication changes only this new packet, its reports, and the existing packet's navigation. The exact published commit is re-read from GitHub before reporting success. `tools/validate.py` is run on that clean complete checkout; its actual receipt and SHA-256 are attached to the PR description. That repository-integrity event is distinct from the Lean and mathematical checks above.
