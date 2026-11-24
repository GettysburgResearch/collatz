# Verification of the two-class descent checkpoint

The scientific packet is [Original-source descent and projection](../../../research/ayh-resource-reset-20261124/two-class-descent/README.md). Collatz remains open. This report separates exact formal evidence, finite controls, internal mathematical review and the final repository publication receipt.

## Fresh Lean build

The coordinator's fresh build compiled **six new Lean modules**, rebuilt the two-module local import closure and succeeded with empty stderr. It used Lean 4.34.1, one worker, auto-implicit arguments disabled, warnings as errors, and Mathlib commit d13f23b723b8a846827a245b89c10fc7d3f11612. Only the pinned third-party Mathlib cache was reused; local modules were rebuilt in a fresh temporary directory.

All **15 new public theorem declarations** were queried in one aggregate axiom audit. Their transitive dependencies are subsets of propext, Classical.choice and Quot.sound.

| Module | Public theorems | Exact formal scope |
| --- | ---: | --- |
| HighGradeShadow | 3 | Word-numerator parity, fixed-weight dyadic injection, exact oriented shadow update |
| RoundedHeadDescent | 1 | Five unbounded integer families reach the same endpoint in 13 shortcut steps |
| FrontierCoarea | 3 | One dyadic first crossing per clock, finite incidence sum and a minimizing floor |
| KilledEntryContraction | 1 | Uniform weighted contraction from drift and a small-set survival deficit |
| PairedSourceShuffle | 4 | Lower/upper fiber fringes, total trimming and retrospective residue numerator |
| LargestSlopeProjection | 3 | Largest-slope endpoint band, equal-anchor source diameter and joint integer record census |

[Complete build log](lean-build.log) · [Execution metadata and source digests](lean-build.json) · [Named axiom inventory](axiom-audit.json) · [Frozen scientific sources](source-hashes.json).

The long-time probability estimates, source-transfer assembly, floor-menu conclusions, incidence recurrence and sieve consumer are **written proofs**. The complete claims are not asserted to be Lean formalized.

## Executed finite controls

The coordinator executed the frozen high-grade checker. It verified **32,766** fixed-weight chronological words through length 14 and **2,040** actual high-start physical histories. The largest tested normalized proxy error, multiplied by the grid size, was exactly \(1/9\). Every tested residue produced the expected distinct parity word and satisfied the specified shadow error inequality.

The process returned zero with empty stderr. [Exact command, source digest and counts](finite-checks.json). The finite cases corroborate their stated algebra and bounded error; they do not establish the asymptotic source estimates. Previously completed expensive regressions were not rerun.

## Mathematical reconstruction and exact revision boundaries

Three parallel GPT-6.2 Astra streams developed the direct descent, occupation and source-projection approaches. Their arguments were cross-checked where they interact; the coordinator reconstructed the integrated statements.

* [Rounded descent and main incidence review](ROUNDED_DESCENT_REVIEW.md) pins the rounded descent and the original main recurrence. The later distinct-head and sparse-band additions have coordinator review.
* [High-grade shadow review](HIGH_GRADE_SHADOW_REVIEW.md) checks the scalar mesh, actual source transfer, orientation and bounded post-passage buffer.
* [Adaptive and forward projection review](ADAPTIVE_PROJECTION_REVIEW.md) checks the exact joint record, largest-slope cancellation, rare selected populations and forward endpoint counts.
* [Area/occupation improvement review](AREA_FRONTIER_REVIEW.md) checks the arbitrary-clock cancellation and the quarter-exponent coarea theorem.
* [Finite-floor review](FINITE_FLOOR_REVIEW.md) checks the parameter-product amplification, adapted stopping rule, local excursion sum and growing menu.
* [Sifted-source review](SIFTED_SOURCES_REVIEW.md) checks the actual surviving cylinders, CRT Fourier normalization, large-sieve truncation and rough-visit exponents.
* [Coordinator reconstruction](ROOT_REVIEW.md) records the independent algebra, quantifiers, external-input boundary and final open color problem.

These are internal written audits with exact source pins. They do not certify neighboring statements or later changed files by association. The sifted-source copy corrects one missing LaTeX backslash; the finite-floor copy removes spaces on a blank line. Their mathematical text is unchanged from the reviewed versions. Recent external source estimates retain their SOURCE-QUALIFIED status; their probability formalizations were not rebuilt.

## Publication evidence and earlier history

The remote scientific tree is compared with the tested local tree. After fetching the published commit into a clean complete checkout, the mandatory default repository validator is executed at that exact head. Its complete receipt, head, tree and SHA-256 are placed in PR 197 without modifying the validated commit. Repository integrity does not prove the mathematics.

The preceding checkpoint's full PR body, with trailing whitespace normalized and its exact historical validation receipts retained, is preserved in [PRIOR_PR_DESCRIPTION.md](PRIOR_PR_DESCRIPTION.md). This avoids indefinitely expanding the current PR body while preserving earlier evidence.
