# Nine-hour global Collatz research pass

This pass began at **2026-11-27 22:56:49 UTC**, with a requested nine-hour window ending at **2026-11-28 07:56:49 UTC**. Its starting repository head is `505d3fe782922904e86477990cc5d41e9110edda`, on draft [PR212](https://github.com/GettysburgResearch/collatz/pull/212). The previous six-hour packet remains intact in [its own directory](../astra-infinite-descent-20261127/README.md).

**The Collatz conjecture remains open in this repository.** The aim here is to resolve global structural questions and search for a universal proof, with frequent published mathematical checkpoints. Written proofs, external inputs, bounded computations and kernel-checked declarations have separate scopes.

## Current mathematical work

| Track | Candidate result or target | Remaining universal obstruction |
| --- | --- | --- |
| [Original marked trace](escape/SUMMABLE_ORIGINAL_TRACE.md) | Finite total stopped variation across every grade and every threshold; fixed-target uniform CDF limits and atomlessness. The unmarked consequence is attributed to PR195. | Summable losses can coexist with nonzero mass escaping along an actual orbit. |
| [Whole spatial trace](escape/SPATIAL_TRACE_TAIL.md) and [all finite depths](escape/ALL_DEPTH_SPATIAL_PROFILE.md) | Uniform classification across changing ordinary targets and every simultaneous depth, using profiles attached to actual escaping components; finite low-root reconstruction with a power error. | The component amplitudes have not been proved to vanish. |
| [Unrestricted cycle periods](cycles/PERIOD_SPECTRUM.md) | Uniform bounds in every translated period interval, with unrestricted valuation words and both signs; a fractional gap budget and an affine-line alternative. | Sparsity does not exclude a single additional integer cycle. |
| [Cycle trace law](cycles/CYCLE_TRACE_LAW.md) and [delayed cycle contributions](cycles/DELAYED_CYCLE_TRACE.md) | An absolute raw harmonic floor on every positive cycle, uniform log-quantile limits, and finite ordinary atoms forcing a quantitative lower bound for the depth tail. | A uniform inverse-depth upper bound with the stated constant would exclude extra cycles; it has not been proved. |
| [Structured rational approximation](broad/PIN_APPROXIMATION.md) | An exact pointwise Collatz criterion using positive rational sums with ordered exponents; a unique greedy maximizer at every arity. | The bound must be uniform as the number of terms grows. |
| [Fixed-arity arithmetic](broad/SPARSE_APPROXIMATION.md) | A classical Subspace Theorem application controls arbitrary exponents at every fixed arity and constrains the even-step clock. | Dimension-dependent constants do not yield the required linear clock bound. |
| [Long odd runs](broad/MERSENNE_POST_BURST.md) | Explicit ordinary counterexamples to an additive fixed-arity bound, and an effective restriction with a growing number of later even events. | The compulsory even-step proportion can still tend to zero. |
| [Interpolation determinants](broad/INTERPOLATION_DETERMINANTS.md) | An arbitrary-dimension obstruction for positive one-variable sparse alternants on greedy sums, including exact two-prime valuations and universal fixed divisors. | Source-specific extra divisibility and mixed-coordinate cancellations remain available. |
| [Ranking obstructions](broad/RANKING_OBSTRUCTIONS.md) | Test broad families of local valuations and nonlinear combinations against actual ordinary trajectories. | A successful ranking must escape the proved local-observation obstructions. |

The first-pass manuscripts are proposed written arguments until their checkpoint review is recorded. Their Lean files prove the precise finite interfaces stated in those files; they do not formalize all analytic or Diophantine arguments in the manuscripts.

## Broad source review

The [primary-source map](broad/PRIMARY_SOURCES.md) distinguishes recent independently checked results from manuscript claims and from inputs reconstructed locally. In particular, the November 2026 RH and Dirichlet-GRH verification is relevant as a proof architecture and verification example; none of this packet's Collatz results assumes a new consequence of GRH.

The live repository frontier was checked at these pins:

| Work | Inspected head |
| --- | --- |
| PR211: reciprocal rigidity, endpoint/Farey censuses, finite-source variance and finite-seed reduction | `4b44cded44af5bb7c3ce67fb16a70c898ad505d5` |
| PR213: first-merge charge, upper bundles, stationary tails and synchronized grades | `5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128` |
| PR195: original trace depth differences | `3fa7ef4a0011b35447a70f587b400878d5ea8ebe` |
| PR193: real fibres and escape-front measure | `100ba857239a180840930765047d65ede92abeec` |
| PR206: physical return descent | `6bcf4f0b32d15678ab6775bdcc6e20d83736512d` |
| PR201: canonical tower mergers | `dac732467c6ed5307d1b78eaa8534653aeeb7a4c` |

## Reproduction and checkpoint practice

The complete baseline checkout passed `tools/validate.py` before new work. The pass uses Lean **4.34.1**, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612` with its pinned dependency manifest.

Run [replay_lean.py](replay_lean.py) with explicit `--lean`, `--mathlib` and `--receipt` paths. It builds this packet in fresh storage, follows only explicitly imported modules from the previous packet, and audits every local declaration, including private declarations. It rejects any transitive axiom beyond `propext`, `Classical.choice` and `Quot.sound`. A successful run checks the source hashes at both ends. Run [replay_checks.py](replay_checks.py) with `--receipt` to reproduce the finite controls with ordinary Python and `-O`; their explicit checks remain active in both modes.

Checkpoint receipts and independent reviews belong in [the pass report directory](../../reports/astra-global-20261128). Each publication must preserve an exact source tree, its proof scopes, bounded-control receipts and the still-open implication. No early draft or computation is a proof of Collatz.
