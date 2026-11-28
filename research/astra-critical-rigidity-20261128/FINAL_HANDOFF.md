# Nine-hour research pass: results, evidence and the next decisive questions

**Collatz remains unresolved.** This pass moved beyond the original reference-arc and rotation-plateau problem into actual minimum-time deviations, ordinary synchronous collisions, sharp rational-cycle spectra, sparse perturbations and fixed-root inverse paths. Its strongest outputs are explicit written theorems with identified original inputs, connected finite Lean kernels, and counterexamples to several overly strong intermediate conjectures.

The working branch is `research/astra-critical-rigidity-20261128`, based on main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; the review surface is [draft PR214](https://github.com/GettysburgResearch/collatz/pull/214). The pass began at approximately 23:00 UTC on November 27, with an authorized endpoint of 08:00 UTC on November 28. The [checkpoint ledger](README.md) and [coordinating reports](../../reports/astra-critical-rigidity-20261128) retain the incremental record. Every public checkpoint was frozen and subjected to full repository integrity validation in a clean complete checkout before its exact tree was published. Integrity checks do not certify mathematics.

## 1. The most substantial analytic result: the cutoff-clock conjecture

Let `T(n)=n/2` for even n and `(3n+1)/2` for odd n. Native time always counts these shortcut steps. Write tau*(n) for the first date at which the actual infinite trajectory attains its global minimum; this exists by well ordering and does not assume convergence to one. For a logarithmic threshold parameter s, use the first passage at or below `n^(1-s)`, capped at tau*(n). Set

\[
d=\log(4/3),\qquad \mu=2/d,\qquad
\sigma^2=2(\log3)^2/d^3.
\]

For an ordinary start sampled uniformly through X, the centered cutoff-clock process, normalized by `sigma*sqrt(log n)*sqrt(log log X)`, has the proposed uniform-topology moderate-deviation principle on every fixed `[0,1-eta]`. Its speed is `log log X`, and its rate is

\[
 I(f)=\frac12\int |f'(s)|^2\,ds
\]

for absolutely continuous paths starting at zero, and infinity otherwise. This is a **proposed written resolution of the functional conjecture stated in Leen's original supplement**, using that manuscript's precise relative passage and landing inputs. It is not an assertion that the complete probability theory has been formalized here. [Capped functional proof](ordinary/CAPPED_FUNCTIONAL_MODERATE_DEVIATIONS.md) · [Primary-source review](../../reports/astra-critical-rigidity-20261128/checkpoint21/original-source-review.json)

The proof's critical step is relative rare-event factorization. A negligible unconditional error would be inadequate for a moderate-deviation event. The argument instead keeps the terminal landing test in the local passage formula, uses fresh buffered sources at successive gates, and proves an all-threshold native modulus. The source-ratio extension, overshoots and arbitrary polynomial error orders are written explicitly. Root and both other lanes reconstructed these points.

### What changes at the actual minimum

The actual path through s=1 has a weak large-deviation principle. Cutting off at the moving height `exp((log n)^e)`, for any fixed `0<e<1/2`, gives the full principle. The full principle for the true minimum is equivalent to exponential tightness and the original explicit slow-side condition BS'. **BS' is still open.** [Endpoint analysis](ordinary/MODERATE_DEVIATIONS_AT_THE_MINIMUM.md)

The new moment formulation makes this gap quantitative. Define

\[
p_* = \sup\left(\{0\}\cup\left\{r>0:\ \frac1M\sum_{n\le M}(1+\tau_*(n))^r
 \le D_r(1+\log M)^{C_r}\text{ for all }M\right\}\right).
\]

The finite constants D_r and C_r may depend on r. Let B* be the best exponent for keeping the normalized full path inside one compact set with exceptional probability at most `(log X)^(-B+o(1))`. The proposed exact relation is

\[
                         B_* = p_*/2.
\]

Consequently the full endpoint principle is equivalent to p*=infinity. Every positive order 0<r<p* also has the sharp average asymptotic `(mu log M)^r`. No positive value of p* has been proved in this pass. Even p*=infinity would control the time to each source's own minimum; it would not identify that minimum as one. [Moment-index theorem](ordinary/MINIMUM_CLOCK_MOMENT_INDEX.md)

The reverse implication is genuinely arithmetic. Original Weaver Paper12 supplies a uniform clocked predecessor population for each positive odd target a<=M prime to three, under its stated selected-word inputs and with an absolute onset X>=C*M. Disjoint actual first-entry sets transfer a compact-tail bound to the distribution of slow targets. The scale `log X` proportional to `u^2/log(u+2)` gives the exponent two. The exact odd embedding `a -> 4a+1`, followed by dyadic stripping, extends the target estimate to all integers. The original theorem's statement and proof were read to check that no target-dependent onset was hidden. The new [NativeMinimumClock.lean](ordinary/NativeMinimumClock.lean) formalizes the actual global-minimum semantics, strict-record additivity and the unit-embedding identity, while the population and tail arguments remain written.

**Next consequential target:** obtain any positive p*, or exhibit a rigorous obstruction. This asks for uniform quantitative information about the genuinely exceptional sources and is not another refinement of the central Gaussian law. A finite positive moment would already imply a uniform polynomial-in-value worst-case bound on the time to the minimum. All moments would imply a subpower bound, without supplying a computable uniform onset or proving descent to one.

## 2. A concrete ordinary-source equivalence with Collatz

For independent ordinary starts n,m uniform through X and the common date `H_X=floor(mu log X)`, the pass gives a source-qualified equivalence:

\[
 \text{Collatz}\quad\Longleftrightarrow\quad
 \lim_{X\to\infty}\Pr(T^{H_X}n=T^{H_X}m)=\frac18.
\]

The limit is derived from the genuine cycle-basin masses and full shortcut periods, with all aperiodic components and large periods controlled. The probability is an actual finite-date, unmarked statistic. The value one eighth is **not evaluated here**. Positive predecessor-density inputs are what turn absence of exceptional component mass into absence of an exceptional source. [Synchronous collision theorem](ordinary/SYNCHRONOUS_PHASE_DISPERSION.md) · [Checkpoint16 review](../../reports/astra-critical-rigidity-20261128/checkpoint16/REVIEW.md)

This equivalence suggests a clear target for a new attack, but it is not a proof strategy by itself: one must establish the exact statistic for the unchanged integer map. The formal [SynchronousPhase.lean](ordinary/SynchronousPhase.lean) constructs the true same-date equivalence relation and invertible quotient shift, proves common dates for finite equal-phase families and connects phase returns to actual periodic tails. The distributional formula remains written.

The related ordered-carry reduction is also now connected in Lean. For the worst unmatched actual pair n,3n, for positive odd n and combined odd grade at most G, the work proves

\[
 (\tfrac12-o(1))G\log_2G\le K(G)=o(G^2).
\]

Thus a universal linear bound is false. The desired `K(G)=O(G log G)` bound is equivalent to an explicit ordered equal-grade carry inequality, with both directions realized by actual positive ordinary sources. The arithmetic inequality remains open. [Clock-carry equivalence](ordinary/ADJACENT_CYCLE_CLOSURE.md) · [Formal equivalence](ordinary/ClockCarryEquivalence.lean)

## 3. The complete denominator is governed by surviving chronological rank

The cycle program now retains the entire reduced denominator, arbitrary clock sheets, the physical native order and all prime-power cancellation. It no longer relies on assuming a favorable single recurrence factor.

For a genuine positive rational odd cycle, let p be its least odd period, q its common full reduced denominator, and r the rational minimal recurrence degree of the unfolded chronological state. Its monic annihilator f satisfies `q | abs(f(3))`, and as the minimum grows, `log_3(abs(f(3)))/r -> 1`. The exact numerator gcd is visible. Additional physical-order and sparse-inversion hypotheses force `log_3 q/r -> 1`. [Minimal denominator formula](cycles/MINIMAL_RECURRENCE_DENOMINATOR.md) · [Physical inversions](cycles/SPARSE_PHYSICAL_INVERSIONS.md)

The nearcritical constructions show why an unrestricted replacement of r by p cannot work. For every lambda in `[0,1]`, there are primitive genuine rational cycles with

\[
 \log_3q/p\to\lambda,\qquad r/p\to\lambda,\qquad \log_3q/r\to1,
\]

with minimum at least `p^(2-o(1))`, width `2+O(p^(-1+o(1)))`, and positive total clock defect at most `p^(-1+o(1))`. More strongly, finite families at one common sequence of native clocks `(p,A)` have their denominator rates approach the entire interval `[0,1]`. The construction selects genuine active Fourier components with binary sheet masks and bounds the full residual cancellation by integral resultants. A zero normalized rate does not mean denominator one. [Nearcritical spectrum](cycles/NEARCRITICAL_DENOMINATOR_SPECTRUM.md) · [Common-clock spectrum](cycles/SYNCHRONIZED_NEARCRITICAL_SPECTRA.md)

For any proper valuation rotation with u mismatches, an exact finite inequality survives:

\[
                            u(r-1)\ge p.
\]

The recurrence kernel is formalized. Its constant is attained at every even period by the explicit word `(1,2,...,2,3,2,...,2)`: p=2n, u=2, r=n+1 and `q=4^n+3^n`. These equality examples have width tending to four. [Exact equality](cycles/EXACT_ROTATION_RANK_EQUALITY.md) · [Formal kernel](cycles/RotationRecurrenceRank.lean)

For a fixed mismatch budget s>=4, the minimal full-denominator exponent c_s satisfies

\[
 \frac1{4\log_2(3)s}\le c_s\le\frac1{2L_s},
 \qquad L_s=\max\{L\text{ positive odd}:4L\le s\}.
\]

This settles the order of dependence, `c_s=Theta(1/s)`. The upper construction can simultaneously have increasing rotation order and the nearcritical geometry above. For every prescribed diverging allowed budget, rational rates can tend to zero. The problem of excluding q=1 at unrestricted increasing complexity remains. [Optimal mismatch order](cycles/OPTIMAL_ROTATION_DENOMINATOR_ORDER.md)

### Open residence and the recent logarithm input

The pass independently rebuilt all **1,002 original October project modules** behind Chudnovsky's logarithm-ratio theorem, then separately audited four original endpoint declarations and three local specializations. The October theorem gives irrationality exponent at most three for `log 3/log 2`; the November affine extension was inspected but not independently rebuilt. The source hashes, nine dependency revisions, original failed-cache repair and final endpoint audits are retained. [Import and exact scope](literature/CHUDNOVSKY_LOGARITHM_IMPORT.md) · [Kernel receipt](literature/CHUDNOVSKY_KERNEL_RECEIPT.json)

With that input, the physical matched-code argument implies that each fixed odd-state width R<4 contains only finitely many ordinary cycles, with ineffective onset. The new open-path result bounds every distinct actual ordinary integer odd run in a fixed sub-four band [M,RM] by `M^(0.4126437817607...+o(1))`; at width three the refined exponent is `0.21232611277034...`. For shrinking near-octaves, the stated width and denominator hypotheses give at most `(log M)^(3+o(1))` dates. [Open residence](cycles/UNIFORM_SUBFOUR_RESIDENCE.md) · [Width-dependent rates](cycles/OPEN_MATCHED_WIDTH_RATES.md) · [Polylogarithmic residence](cycles/POLYLOGARITHMIC_NEAR_OCTAVE_RESIDENCE.md)

These results still permit an exceptional orbit to leave the band. Another branch produces many exact physical equal-sum quadruples and repeated disjoint rounds in hypothetical near-four cycles. Turning those forced additive structures into a contradiction, or handling their excursions without losing the actual denominators, remains a substantive next step. [Repeated packings](cycles/REPEATED_ADDITIVE_PACKINGS.md)

## 4. Exact sparse capture exposes the limits of statistical evidence

For an octave `[2^j,2^(j+1))`, there is one fixed computable odd mask of relative density `O(j^-2)` with the following property: for every fixed cutoff B, the set of genuine starts visiting that mask above B strictly before their own minimum has natural density one. Yet every prescribed `o(log n)` initial deadline has vanishing capture probability. This reaches the exact logarithmic-square power and separates early faithful behavior from eventual sparse interception. [Critical capture](literature/EXACT_LOG_SQUARE_CAPTURE.md)

Closing the mask under the least odd integer at least the true odd successor yields a computable modified rule that preserves all even edges and any prescribed finite table, adds only zero or one at odd inputs, changes `O(X/log^2 X)` edges through X, and has a density-one set of divergent starts. The actual rounded arithmetic, bounded decidable closure, first-hit transfer and forced escape are formalized in [RoundedOrbitCapture.lean](literature/RoundedOrbitCapture.lean). The sparse-density and almost-everywhere capture statements remain written.

This is a modified-rule theorem, not a Collatz counterexample. It identifies a real limitation on methods using typical short prefixes or the known bulk fluctuation laws alone. Earlier constructions even preserve the full specified descent-law tests while changing global component behavior. The exact parity rule must enter any argument that seeks to rule out exceptional components.

The claimed sharpness is specific: square-root shell summability is a sufficient all-height avoidance criterion, and the logarithmic power two is critical for these constructions. The pass does **not** claim that every mask of density `o(j^-2)` is avoided; slowly varying factors require their own summability analysis. [All-height avoidance](literature/ALL_HIGH_TARGETS.md) · [Critical early masks](literature/CRITICAL_LOG_SQUARE_MASKS.md)

## 5. Genuine inverse paths and relative rare words

At a prescribed transient ternary-unit root, the natural-density inverse ray now has quantitative joint arithmetic laws, a stable Brownian height limit and a sharp two-sided iterated-logarithm law. If V_k is its native height, then

\[
 \limsup\frac{\log V_k-k/\mu}{(\log3/2)\sqrt{2k\log\log k}}=1,
 \qquad\liminf=-1.
\]

Cylinder information tracks log height within `O(log k)` almost surely and inherits the fluctuation laws. The proof uses summable quantitative coupling, conditional moderate tails and an all-date modulus; weak Brownian convergence alone would not imply the iterated-logarithm result. Prior inverse-speed, first-order frequency and entropy theorems are explicitly credited. [Fixed-root LIL](ordinary/FIXED_ROOT_ITERATED_LOGARITHM.md) · [Cylinder information](ordinary/INVERSE_RAY_CYLINDER_INFORMATION.md)

The largest recovery ratio on a genuine trajectory through its minimum has order log X in probability, with matching inverse-linear tail order. The maximum over a deterministic-length early prefix of a sampled start has an explicit Frechet law. On a fixed inverse ray the recovery maximum has almost-sure power one, is tight at the linear scale in probability, and nevertheless has unbounded normalized limsup. [Forward recovery](literature/MAXIMUM_PREMINIMUM_RECOVERY.md) · [Inverse recovery](literature/FIXED_ROOT_MAXIMUM_RECOVERY.md)

The final relative-word theorem handles rare word families without dividing a generic absolute error by their probability. It retains the high quotient while resampling low bits, controls the actual affine endpoints, and measures terminal labels against their empirical distribution on the source interval. On initial intervals through N, every individual word of length `o(sqrt(log N))` has its relative frequency in any fixed positive-density terminal class; balanced words can be longer under the displayed grade condition. On moving intervals the analogous conclusion requires the class's empirical mass to stay bounded below. The full word and label are asymptotically independent for length `o(log N)`. The earlier rare-prefix coupling from Weaver Paper124 is credited. [Relative parity law](literature/RELATIVE_PARITY_WORD_EQUIPARTITION.md)

## 6. What is formal, what is written, and where to begin review

The final local inventory is **133 packet-runner public theorem roots, three logarithm specializations and one motif specialization: 137 distinct local roots**. The final packet build compiles all 31 packet modules into fresh objects and performs a separate import axiom audit. The synchronous quotient-shift definition is audited additionally and is not counted as another theorem. The only allowed reported axioms are `Classical.choice`, `Quot.sound` and `propext`. [Final build receipt](../../reports/astra-critical-rigidity-20261128/checkpoint23/all-packet-lean.json)

The imported 1,002-module logarithm closure is separate and is not counted as 1,002 new local theorems. Cached pinned Mathlib and other third-party objects were reused. No cold dependency rebuild or independent LeanChecker replay is claimed. Formal kernels are connected to the actual map, native word carries, full divisors and first-entry semantics; the source-by-source scope in [the runner](check_lean.py) states the analytic conclusions that remain written.

Finite controls use exact arithmetic where their statements are exact, run normally and with Python optimization, and retain source hashes. The coordinating reviews distinguish finite evidence from infinite proofs, preserve failed checks and document corrections. All large analytic claims are proposed research proofs with identified original hypotheses, rather than declarations of external peer-reviewed consensus.

For a focused review, start with these five packages:

1. **The capped moderate-deviation proof and endpoint frontier.** Audit rare-event factorization, the all-threshold modulus, uniform predecessor onset and the compact-set construction. Then attack any positive moment order.
2. **The synchronized denominator spectrum.** Audit physical positivity/primitivity, active components and full prime-power cancellation. This determines exactly which universal denominator lower bounds are false.
3. **The ordinary synchronous collision criterion.** Audit the passage from finite true phases to the complete component inventory, then seek a way to evaluate the median statistic.
4. **The sharp sparse-mask construction.** Audit conditional low-bit coupling, the two orders of limits and first capture of the modified rule. This checks the barrier against purely bulk-statistical strategies.
5. **The remaining ordered carry inequality or a forced physical contradiction.** Either would address an actual worst-case arithmetic obstacle. More marginal improvements to already-strong typical laws will not by themselves settle it.

The source refresh considered recent finite computations, restricted first-crossing theorems, phase-cover results, predecessor-density advances and formal logarithm work, and distinguished each from universal termination. It did not treat announcements on unrelated problems as Collatz lemmas. [Original-source refresh and attribution](literature/PRIMARY_SOURCE_REFRESH.md)

The next pass should preserve these distinctions: rational witnesses may vary, a density-one statement may leave a single integer undecided, reaching one's own minimum need not reach one, and a correct formal finite kernel need not supply its missing global analytic hypothesis. The useful progress here is that several broad intermediate questions now have exact answers, and the remaining questions have concrete arithmetic or tail formulations.
