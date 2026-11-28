# Global rigidity and the critical ordinary clock

**Collatz remains open.** This is the second checkpoint of the nine-hour pass begun 2026-11-27 at 22:59:19 UTC. It continues [PR213's frozen packet](https://github.com/GettysburgResearch/collatz/tree/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127). The intended end is 2026-11-28 at 07:59:19 UTC. The current material is a checkpoint, not a claim that the full pass has elapsed.

We use the shortcut map `T(2x)=x`, `T(2x+1)=3x+2`. An odd departure contributes one to `Q_k`; the clock counts shortcut steps. The odd map removes the complete power of two in `3x+1`. These clocks are distinguished throughout.

## Results and their exact limits

| Result | Evidence and dependency boundary | Next missing step |
| --- | --- | --- |
| [Exact width-language entropy](cycles/EXACT_WIDTH_ENTROPY.md): for `2 ≤ R ≤ 4`, putting `η=log₂(R/2)`, `a=log₂3−1`, the entropy in nats per odd step is `η log 2 + (η−a)₊ log(3/4)`. | Written proof; exact finite language and rational-realization controls. The matching calculation determines the symbolic function introduced by Witteveen. The exponentially many rational cycles typically have exponentially large complete denominators. | Exclude the exceptional **denominator-one** atoms, which the typical-denominator estimate allows. |
| [Height forces entropy](cycles/HEIGHT_ENTROPY.md): sufficiently many distinct polynomial-height phases force a positive entropy floor; bounded-width ordinary cycles stay a positive edit distance from locally subexponential languages. | Written finite counting proof and exact integer controls; the polynomial-height conclusion uses the published two-logarithm estimate. The cycle may have arbitrary collisions from phases outside the selected low-height set. | A global arithmetic restriction that contradicts this entropy floor, beyond a low-complexity model of a restricted family. |
| [Finite component partition](mass/FINITE_COMPONENT_PARTITION.md): a bounded observation and restart algorithm asymptotically recovers the full component-mass spectrum. | Source-qualified deduction from the indicated Mazur descent/tightness input; density statements retain their additional inputs. No unresolved labels are falsely merged. | Force the computed pair energy to one, or the escape energy to zero. The algorithm identifies these quantities but does not force their endpoints. |
| [Critical native odd count](mass/CRITICAL_NATIVE_COUNT.md): a bounded statistic of ordinary counts at `L=(2/log(4/3)) log X + z sqrt(log X)` detects any bad component, for every fixed real `z`. | Source-qualified written deduction, including the actual-source crop and first-hit [window argument](mass/FIXED_BASIN_NATIVE_WINDOW.md). Its fixed-root bridge premise includes joint mixing (J). The finite post-hit count identities and drift are formalized separately. | Establish the centered Gaussian comparison for the **unstopped ordinary counts** without assuming the fate of the small state visited. |
| [Protected prime Mersenne sources with later mergers](mersenne/PRIME_MERSENNE.md): explicit prime progressions give long protection against cheaper visitors yet later mergers with many smaller Mersenne sources. | Source-qualified asymptotic theorem; stated Dirichlet-GRH input; exact compressed certificates for supplied ordinary sources. Lean gives an all-time weighted obstruction at exponent 19, connected to its actual original ramp. | Replace typical prime-progressions conclusions by a theorem resolving each fixed source or the least counterexample. |

## Lean source and current build status

**Checkpoint 2: four modules and all 32 public theorem roots freshly compiled and axiom-audited.** The successful [receipt](../../reports/astra-global-rigidity-20261128/checkpoint2/lean.json) pins Lean 4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. Only `propext`, `Classical.choice`, and `Quot.sound` occur in the public-root inventories. This is one compiler/runtime audit, with reused compiled dependencies whose optional Mathlib overlay is byte-verified against the pinned cache.

The [first timeout](../../reports/astra-global-rigidity-20261128/checkpoint1/lean-timeout.json) remains as historical evidence. The old dependency-heavy `CriticalCount.lean` was replaced by `mass/CriticalCountStandalone.lean`, using the same actual-map recurrences with a small dependency closure. It proves signed count additivity, the alternating count after a true visit to one, and a uniform rational drift after a true visit to a fixed nonconvergent anchor.

`mass/BasinDefects.lean` proves actual orbit comparability, the single exceptional edge for the visit set of 5, and disjointness of the visit sets of 5 and 85. `cycles/WidthCarry.lean` proves the four-copy no-carry step, the two local energy counts, and an explicit six-copy collision. It does not formalize the Subspace Theorem or the global counting argument.

`mersenne/MersenneCrests.lean` contains the actual Mersenne ramp, a finite-cut criterion that excludes all future augmented meetings, and its supplied exponent-19 instance. An augmented state includes the actual height and accumulated odd count; an obstruction for those states must not be restated as an obstruction to unweighted orbit intersection.

The analytic limit laws, ordinary density inputs, asymptotic prime distribution, and full entropy arguments are written mathematics. The Lean audit does not certify them by proximity. Run `check_lean.py --help` for the exact pinned compiler and Mathlib interface. Compiled dependencies are reused; packet objects and public-theorem axiom audits are fresh.

## Larger restrictions added at checkpoint 2

### Cycles of arbitrary width

[Mesoscopic complexity](cycles/MESOSCOPIC_COMPLEXITY.md) deduces a finite-scale theorem from Weaver 173: at each sufficiently large scale compatible with the actual rational input height and denominator, a long simple trajectory must have more than `A k` length-`k` factors. A cycle with uniformly linear factor complexity therefore has period `O_A(1+log q)`, where `q` is its complete denominator. Its maximum height is at most `(2q)^{O_A(1)}`. This covers arbitrary width and native valuations. It does not prove that an arbitrary cycle has linear complexity.

[Four-copy width bounds](cycles/FOUR_COPY_WIDTH.md) track the available grade sites as width varies between 2 and 4. They retain the full denominator in the physical source count. At width 4 the exponent and the `6^a 15^h` energy are already Weaver 145; the width-dependent availability, uniform denominator factor, and stated fixed-order moment limitation are the deductions here. The improved bounded-width exclusion retains the cited irrationality-exponent input and is ineffective at the remaining finite range.

### Ordinary basins, source trits, and endpoint atoms

[Ordinary basin windows](mass/ORDINARY_BASIN_WINDOWS.md) shows why local overlap cannot be assumed from positive basin densities. The actual, disjoint visit sets of 5 and 85 remain segregated on subpolynomial windows, even though both converge to one. The same argument forces substantial low-frequency Fourier coefficients and gives nonconstant fixed vectors modulo density-zero defects.

[Weighted basin cuts](mass/WEIGHTED_BASIN_CUTS.md) constructs disjoint cuts entirely in the known convergent component. For every positive decreasing summable vertex weight, their normalized defects tend to zero. This rules out uniform coercivity of the indicated operator, including after removing finitely many directions. It does not rule out strong extinction, which is a weaker and still relevant target. The underlying gates, long ramps, and prior weighted spectral constructions are credited to PR211.

[Translated ternary sources](mass/TRANSLATED_TERNARY_SOURCE.md) proves a uniform joint mixing statement for source trits and the actual future endpoint, native clock, and initial halvings, on arbitrary translated intervals. It uses the precise joint offset-total input of Weaver–Wren 48. This compatibility with segregated basins identifies why source-trit uniformity alone does not imply physical mixing.

[Native endpoint atoms](mass/NATIVE_ENDPOINT_ATOMS.md) gives an all-clock bound `O(1/sqrt(log X))` for every nonperiodic endpoint, from the frozen uniform first-arrival theorem. At the critical clock it derives the actual cycle-phase mixture, retaining each period. An escaping ray attains the possible normalized collision scale; an independently proved smaller order above the critical clock would exclude escape and is still missing.

### All-clock ascent costs and actual prime representatives

[Ascent logarithms](mersenne/ASCENT_LOGARITHMS.md) uses Matveev's weighted coefficient parameter to bound the odd count of every smaller visitor, at every site of an entire ascent, in terms of the actual reduced cofactor ratio. A substantially cheaper visitor must have a large part supported outside every prescribed finite prime set. The physical carry inequalities are checked independently of the analytic bound.

[Direct ancestors](mersenne/DIRECT_ANCESTORS.md) determines the first attainable all-clock cost for a supplied `N ≡ 1 (mod 3^K)` above an explicit threshold. The optimum is characterized by finitely many reference endpoints and exact ternary classes. The extra cost tends to infinity; supplied prime exponents have certified costs 50 and 171 that are globally optimal at their original sites, and a certified feasible cost 402 at a larger site. The last example is not claimed optimal.

[Prime progressions](mersenne/PRIME_PROGRESSIONS.md) combines Shao's recent narrow-progression theorem with counted fusion: every fixed ordinary unit target has many narrow prime progressions whose entire intervening integer block shares an actual first hit. [Prime midpoints](mersenne/PRIME_MIDPOINTS.md) constructs protected prime arithmetic progressions with certified convergent exterior entries and a middle entry in any supplied component. These are source-qualified existence and transfer results. They retain, rather than solve, the fixed-component convergence question; the finite examples explicitly disprove a stronger finite-deadline inference.

## Finite replay

Run `python -X utf8 -B research/astra-global-rigidity-20261128/check_finite.py --receipt /tmp/collatz-global-finite.json` from the repository root. It replays each checker in ordinary and optimized Python, retains output and source hashes, and requires the paired outputs to agree. These are bounded mathematical controls, not a proof of any infinite assertion.

The cycle controls enumerate genuine rational cycles, all endpoints and cells in the tested width-language bands, and exact integer entropy inequalities. The Mersenne checker uses modular affine certificates with matching augmented counts. Its very large exponents are **not** claims to have explicitly expanded or iterated billion-bit starting integers; the written affine argument explains why the compressed certificates concern those fixed ordinary integers.

## Prior work and review

The entropy language is credited to Sven Witteveen, *Entropy barriers for bounded-amplitude Collatz cycles*, [exact source](https://github.com/kulltc/collatz-entropy-barriers/blob/fc0854799b094fa04250ce8309279609276f3c58/paper/main.tex), §5. The physical-height argument credits Weaver's earlier injection. The all-low-height full-cycle entropy bound is already stated in [PR195 at 3fa7ef4a, final paragraph](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/cycles/PHASE_POPULATION.md). The new extensions retain a positive selected fraction, translated progressions, and quantitative Hamming/Levenshtein distance. The Mersenne ramp protections are credited to PR146, PR201 and PR211 as specified in the paper; they are inputs to the new combination. The fixed-target Gaussian is prior work, and the unavailable primary Leen file is not represented as independently read. The supplied derivation instead spells out the frozen PR213 inputs used here.

The [review](../../reports/astra-global-rigidity-20261128/REVIEW.md) states the narrow claim boundaries and failed strengthenings. The [intake](../../reports/astra-global-rigidity-20261128/INTAKE.json) freezes all 149 open-PR heads visible at the start. Reading their metadata is not a mathematical review of all those heads. No neighboring claim inherits a verdict from this packet.
