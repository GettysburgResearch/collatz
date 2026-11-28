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
| [Exact diagonal cycle moment](cycles/DIAGONAL_CYCLE_MOMENT.md) | A positive native statistic equals three for the known odd cycle and exceeds $27/4$ if any extra positive cycle exists, under the stated external cycle inputs. The exact formula retains all periods. | An independent upper bound by $27/4$ is open. Log-loss moments can remain finite without controlling ordinary time. |
| [Cycle parity and height](cycles/ANNULUS_SPECTRAL_FACTOR.md) | A positive fraction of dates in a fixed multiplicative height band forces an irrational rotation factor in the limiting parity system. Bounded diagonal cost also forces positive entropy, using the separately credited integer-word injection. | [Full local parent information](cycles/FULL_PARENT_LOCAL_MODEL.md) is compatible with bounded-height, positive-entropy ordinary trajectory packets with free endpoints. Exact global closure remains essential. |
| [Structured rational approximation](broad/PIN_APPROXIMATION.md) | An exact pointwise Collatz criterion using positive rational sums with ordered exponents; a unique greedy maximizer at every arity. | The bound must be uniform as the number of terms grows. |
| [Complete pin criterion](broad/PinCriterion.lean) | Lean connects the greedy dyadic clock to bounded discounted rank and then to convergence of the same positive integer. | The all-arity bound itself is unproved. |
| [Fixed-arity arithmetic](broad/SPARSE_APPROXIMATION.md) | A classical Subspace Theorem application controls arbitrary exponents at every fixed arity and constrains the even-step clock. | Dimension-dependent constants do not yield the required linear clock bound. |
| [Growing arithmetic gap progressions](broad/QUADRATIC_CLOCK_PADE.md) and [finite decreasing gaps](broad/FINITE_DECREASING_CLOCKS.md) | Elementary finite Padé forms give an absolute $20{,}000\log_2(x+1)$ bound for a nonperiodic ordinary match, uniformly over slope, initial spacing and number of gaps. The positive-slope bound is $1{,}000\log_2(x+1)$. | Irregular adaptive schedules remain possible. The written finite proof is not yet fully formalized. |
| [Adaptive rational matches](broad/RATIONAL_MATCH_MASS.md) and [all overlapping periodic windows](broad/OVERLAPPING_PERIODIC_WINDOWS.md) | Shifted Subspace-Theorem accounting bounds the entire union of bit-length-scale periodic windows with sublinear periods, even when their references change. The classical residual-fraction constant is credited to prior work. | A hypothetical escaping word need not be covered by such windows. |
| [Cofactor collisions](broad/SHIFTED_COFACTOR_COLLISIONS.md) | Repeating the prime-to-three part of $2x+1$ forces an actual low state. The [formal finite bound](root/COFACTOR_FORMAL_BOUND.md) retains the exact difference of powers. | Early collisions have not been forced; same-depth sibling collisions require the two-arm qualification. |
| [Long odd runs](broad/MERSENNE_POST_BURST.md) | Explicit ordinary counterexamples to an additive fixed-arity bound, and an effective restriction with a growing number of later even events. | The compulsory even-step proportion can still tend to zero. |
| [Interpolation determinants](broad/INTERPOLATION_DETERMINANTS.md) | An arbitrary-dimension obstruction for positive one-variable sparse alternants on greedy sums, including exact two-prime valuations and universal fixed divisors. | Source-specific extra divisibility and mixed-coordinate cancellations remain available. |
| [Ranking obstructions](broad/RANKING_OBSTRUCTIONS.md) | Test broad families of local valuations and nonlinear combinations against actual ordinary trajectories. | A successful ranking must escape the proved local-observation obstructions. |

The [variation profile](escape/VARIATION_PROFILE.md) strengthens the marked classification in every interval $p$-variation norm with $p>1$, and the [critical source clock](escape/CRITICAL_SOURCE_CLOCK.md) retains the source, native age and terminal mark jointly. The [ordinary product comparison](escape/ORDINARY_PRODUCT_TRANSITION.md) explicitly credits PR145 for the Gaussian product transition and the half-mean criterion; its additional content is the uniform fixed-target soft-clock comparison and a direct marked telescoping proof. None of these results proves that the escape amplitudes vanish.

The manuscripts are proposed written arguments until their checkpoint review is recorded. Their Lean files prove the precise finite interfaces stated in those files; they do not formalize all analytic or Diophantine arguments in the manuscripts.

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
| PR145: prior Gaussian product transition, critical Mellin tests and terminal laws | `dd245a712f985909f541590e3f6c179b7ba011e4` |
| PR213: concurrent global rigidity packet, including prior height-entropy injection | `a743bd04d33945b15a1ec91deaca4a82c0261a07` |
| PR214: concurrent paired-clock and rotation-occupation packet | `7c381c5b53afec65fc473c598c5ed61762e9419f` |
| PR215: concurrent critical-parity and mixed-conductor packet | `8a50018b6a861e810b18512fdd59aaf45214bba1` |

The final three entries record a live-frontier refresh. Their PR descriptions and the relevant overlapping manuscripts were inspected; this is not a claim that all their proofs or formal artifacts were independently rebuilt here. The [real-branch audit](broad/REAL_BRANCH_AUDIT.md) gives a counterexample to the literal statement of López–Stoll's Lemma 24, keeping prescribed real branches separate from genuine ordinary parity. It is not a counterexample to Collatz.

## Reproduction and checkpoint practice

The complete baseline checkout passed `tools/validate.py` before new work. The pass uses Lean **4.34.1**, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612` with its pinned dependency manifest.

Run [replay_lean.py](replay_lean.py) with explicit `--lean`, `--mathlib` and `--receipt` paths. It builds this packet in fresh storage, follows only explicitly imported modules from the previous packet, and audits every local declaration, including private declarations. It rejects any transitive axiom beyond `propext`, `Classical.choice` and `Quot.sound`. A successful run checks the source hashes at both ends. Run [replay_checks.py](replay_checks.py) with `--receipt` to reproduce the finite controls with ordinary Python and `-O`; their explicit checks remain active in both modes.

Checkpoint receipts and independent reviews belong in [the pass report directory](../../reports/astra-global-20261128). Each publication must preserve an exact source tree, its proof scopes, bounded-control receipts and the still-open implication. No early draft or computation is a proof of Collatz.
