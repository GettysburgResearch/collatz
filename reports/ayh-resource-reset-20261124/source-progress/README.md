# Source-progress execution and review report

**Collatz remains open.** The [scientific packet](../../../research/ayh-resource-reset-20261124/source-progress/README.md) extends PR197 at `b27a6fe31a487adf5615e173329ad009b975a3cd`. Three GPT-6.2 Astra delegates used **ultra** reasoning effort for the Mersenne, higher-rank and joint-grid attacks. The root integrated the proofs and independently rebuilt the local dependency chain. This report records executed evidence and its limits.

## Fresh Lean execution

The compiler was Lean **4.34.1**, commit `5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib pinned at `d13f23b723b8a846827a245b89c10fc7d3f11612`. Root started with an empty repository object directory, compiled every inherited local dependency, then compiled the new files in successive development batches. No delegate-produced local object was used in these root executions. Mathlib used its pinned binary cache.

All **29 mathematical modules and two public audit modules** compiled successfully with `-j1 -DautoImplicit=false -DwarningAsError=true`. The sum of the final, source-matching successful invocations is **801.764 seconds**. This is a sum across batches, not one uninterrupted invocation of the replay script. The [execution receipt](lean-execution.json) records each source path, SHA-256, exit code, elapsed time and compiler output. Earlier failed development drafts and superseded compilations are not represented as final successes.

The explicit [public audit](axiom-audit.json) contains **152 distinct declarations: 100 inherited and 52 new**. Each axiom list is a subset of `propext`, `Classical.choice` and `Quot.sound`; two of the new declarations use no axioms. This checks dependencies of the stated theorems. Explicit hypotheses remain hypotheses: in particular no proof of `ResidualExclusion` is supplied.

The new [check_lean.sh](../../../research/ayh-resource-reset-20261124/source-progress/check_lean.sh) reproduces the complete local dependency order into its own fresh temporary object directory. Supply `LEAN` pointing to Lean 4.34.1 and `LEAN_PATH` containing the pinned Mathlib and its package build directories. The script was syntax checked; the compiler executions recorded here were run in root's sequential batches rather than by invoking that shell script. The baseline's long quantitative-return certificate was rebuilt in this pass, not merely imported from an earlier run.

## Exact finite replays

All five programs below passed both normal and optimized Python, giving **ten successful executions with identical paired stdout**. [Full commands' modes, source hashes, timings and outputs](finite-execution.json).

| Program | Executed coverage |
| --- | --- |
| `check_word_realization.py` | 620 congruence constructions; 311 literal complete first hits, maximum clock 5,824; 93 symbolic dense-descent certificates; six larger all-even congruence controls. The six huge terminal exponents were handled symbolically, not by materializing their complete orbits. |
| `check_uniform_mersenne_quotient.py` | Complete proof-bounded candidate census at the four residual states and the two other-family controls. It returns the two stated queries and no queries from their successor states. The written potential and integrality bounds, rather than an arbitrary word-length cap, justify completeness. |
| `check_two_checkpoint_rescue.py` | All eleven affine merger rows, both rational endpoint coefficients, the binary lift selecting the explicit progression, and the finite signed controls. The universal ordinary progression is separately proved in Lean. |
| `check_grid_transfer.py` | 1,680 literal finite graphs, including 944 clean-partition cases, 734 cases with extra numerical mergers, 72 large-lift half-component controls, and 24 complete labelled-grid distributions. |
| [check_word_independent.py](check_word_independent.py) | Separately authored CRT and direct discrete-log reconstruction of 90 examples, with sources up to 30,700 bits; eight literal positive contraction examples through a forced odd run of length 500. |

The [independent word output](word-independent.json) includes the actual ordinary sources and clock/rank data. In its `q=500` case the source has 1,047 bits, the lower contraction occurs at clock 1,048, and the upper first hit is at clock 3,174 with exactly 1,341 odd inputs. The [grid output](grid-controls.json) retains the full finite distributions. These numerical examples check implementations; the universal claims rely on the corresponding Lean or written arguments, with their stated premises.

## Independent reconstruction and final review

- [Mersenne quotient and checkpoint review](MERSENNE_REVIEW.md) reconstructs the unbounded-word potential, proof-bounded query census, both checkpoint calculations, the one-sixteenth family, the eleven merger rows and the source-qualified density transfer. It pins successive reviewed versions separately.
- [Final cylinder and dispatch review](FINAL_CYLINDER_REVIEW.md) reviews the exact final `MersenneRescueCylinder.lean`, `MersenneProgressCases.lean` and `FinalProgressProposal.lean`. The reviewer independently rebuilt those files and their source-case consumer, recomputed all eleven modular constants, checked positivity and subtraction, and followed the actual quantitative-return theorem into the least-defect contradiction.
- [Ordinary source-case review](SOURCE_CASES_REVIEW.md) reconstructs the ternary lift, exact first-hit upper rank, full ordinary contraction and the quantifier boundary between cofinal constructed members and a fixed supplied source.
- [Grid review](LATTICE_REVIEW.md) checks the label/physical-graph directions, exceptional lifts, original-source occupancy transfer and the shared-bit dependence that prevents multiplying single-clock estimates.

The later cylinder kernel supersedes the earlier Mersenne review's written-only exponent-to-row attachment. In the integrated checkpoint manuscript, root repaired the relative first-index link and added this evidence-level upgrade. The written multiplicative-order identification, arbitrary-deadline comparison and density estimate retain their separate scope; the final cylinder review does not silently formalize those statements.

## Sources and open boundary

[SOURCES.json](../../../research/ayh-resource-reset-20261124/source-progress/SOURCES.json) distinguishes the compiled baseline, exact upstream analytic input, focused comparisons and primary literature. [OPEN_PR_INTAKE.json](OPEN_PR_INTAKE.json) is a metadata inventory of the 30 most recently updated open PRs at intake, not a mathematical audit of all open branches. [PRIOR_PR_DESCRIPTION.json](PRIOR_PR_DESCRIPTION.json) preserves the preceding PR197 description.

The source-dependent checkpoints prove new pointwise exclusions. The fixed-gap density-one deduction still uses PR146's written symbolic absorption bound. The joint-grid application uses the named selected-population inputs from PR197. Neither imported analytic argument is an axiom of the new Lean consumer. The consumer's one remaining `ResidualExclusion` hypothesis must rule out every least reverse defect outside the proved cases; it remains **OPEN**.

[source-hashes.json](source-hashes.json) binds the final packet, reports, independent checker and navigation edit. After publication, the PR description records the exact remote head/tree and the complete clean-checkout validator receipt. That integrity check is a separate event and does not establish the missing mathematical implication.
