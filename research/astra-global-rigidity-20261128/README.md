# Global rigidity and the critical ordinary clock

**Collatz remains open.** This is the first checkpoint of the nine-hour pass begun 2026-11-27 at 22:59:19 UTC. It continues [PR213's frozen packet](https://github.com/GettysburgResearch/collatz/tree/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127). The intended end is 2026-11-28 at 07:59:19 UTC. The current material is a checkpoint, not a claim that the full pass has elapsed.

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

**Checkpoint 1 build status: pending.** The new Lean sources are supplied for review. The first serial build timed out after 300 seconds while recompiling the unchanged `NativeGate` dependency; it did not reach either new module. The failed receipt is retained. Consequently this checkpoint does not claim new kernel-checked theorem roots. The continuing pass is repairing the runtime and testing a smaller dependency closure.

`mass/CriticalCount.lean` contains proofs of signed count additivity on the actual map, the alternating count after a true visit to one, and a uniform rational drift after a true visit to a fixed nonconvergent anchor. It imports three unchanged native modules from the previous packet.

`mersenne/MersenneCrests.lean` contains the actual Mersenne ramp, a finite-cut criterion that excludes all future augmented meetings, and its supplied exponent-19 instance. An augmented state includes the actual height and accumulated odd count; an obstruction for those states must not be restated as an obstruction to unweighted orbit intersection.

The analytic limit laws, ordinary density inputs, asymptotic prime distribution, and full entropy arguments are written mathematics. The Lean audit does not certify them by proximity. Run `check_lean.py --help` for the exact pinned compiler and Mathlib interface. Compiled dependencies are reused; packet objects and public-theorem axiom audits are fresh.

## Finite replay

Run `python -X utf8 -B research/astra-global-rigidity-20261128/check_finite.py --receipt /tmp/collatz-global-finite.json` from the repository root. It replays each checker in ordinary and optimized Python, retains output and source hashes, and requires the paired outputs to agree. These are bounded mathematical controls, not a proof of any infinite assertion.

The cycle controls enumerate genuine rational cycles, all endpoints and cells in the tested width-language bands, and exact integer entropy inequalities. The Mersenne checker uses modular affine certificates with matching augmented counts. Its very large exponents are **not** claims to have explicitly expanded or iterated billion-bit starting integers; the written affine argument explains why the compressed certificates concern those fixed ordinary integers.

## Prior work and review

The entropy language is credited to Sven Witteveen, *Entropy barriers for bounded-amplitude Collatz cycles*, [exact source](https://github.com/kulltc/collatz-entropy-barriers/blob/fc0854799b094fa04250ce8309279609276f3c58/paper/main.tex), §5. The physical-height argument credits Weaver's earlier injection. The all-low-height full-cycle entropy bound is already stated in [PR195 at 3fa7ef4a, final paragraph](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/cycles/PHASE_POPULATION.md). The new extensions retain a positive selected fraction, translated progressions, and quantitative Hamming/Levenshtein distance. The Mersenne ramp protections are credited to PR146, PR201 and PR211 as specified in the paper; they are inputs to the new combination. The fixed-target Gaussian is prior work, and the unavailable primary Leen file is not represented as independently read. The supplied derivation instead spells out the frozen PR213 inputs used here.

The [review](../../reports/astra-global-rigidity-20261128/REVIEW.md) states the narrow claim boundaries and failed strengthenings. The [intake](../../reports/astra-global-rigidity-20261128/INTAKE.json) freezes all 149 open-PR heads visible at the start. Reading their metadata is not a mathematical review of all those heads. No neighboring claim inherits a verdict from this packet.
