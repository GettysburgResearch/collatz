# Seventh coordinating review: exact exceptional-set geometry and genuine local barriers

November 28, 2026. This is another checkpoint of the continuing nine-hour pass, following public commit `5f2f65f503a5cc1752b3ce05276a584e2791703e`, tree `d876c8c74da98dc62f32a22309bfbcea1a4d1e6a`. **Collatz remains unresolved.** The coordinator independently reconstructed each written argument below. The analytic theorems remain proposed written results with the stated primary dependencies; the Lean and finite controls have their separately specified scope. `SOURCE_MANIFEST.json` pins the exact reviewed versions.

## The exact gauge concerns the entire survivor

`EXACT_MERGER_GAUGE.md` establishes a finite positive Hausdorff gauge for the full nonabsorbing set of the canonical integer pair process. If \(h(z)=s+\mathbb E_zM\) is Leen's capacity, then

\[
c h(z)\le\mathcal H^\psi(E_z)\le C h(z),\qquad
\psi(2^{-t})=2^{-t}\sqrt{t\log\log t}.
\]

The distinction between an almost-sure result under a changed measure and an upper bound for the entire exceptional set is essential here. A null set for the capacity law need not have zero measure for this larger gauge. The final proof therefore pays for all unresolved live cylinders directly.

The imported ingredients are precise statements from Leen's October 9 manuscripts: binary cylinders with their Haar masses, the capacity identity and sharp fixed-state tail, a uniform physical return envelope \(Cs/\sqrt t\), finite expected boundary coast time, fractional moments of the first return offset, and an exponential moment for the complete departure count. The coordinator checked the original statements and the short holding argument in the three source files listed below. The external full manuscripts and their Lean developments have not been rebuilt here.

For a positive excursion, tilting by the terminal level gives the immortal law with embedded transitions \((j\pm1)/(2j)\). A waiting time is uniformly dominated by \(v_2(3^j-1)\) plus a geometric variable. The first clock proof solves the residue-class Poisson equation for occupation of zero modulo \(2^k\). Its successive differences are bounded independently of the modulus. Azuma controls all moduli through \(n^{1/4}\); the remaining dyadic valuation levels are paid using occupation of the largest retained modulus. The terminal-level tilt costs at most \(n+1\), leaving a polynomially small error. Conditional exponential moments then give a linear physical clock with absolute constants, uniformly in the incoming offset.

The second, independently developed clock proof in `IMMORTAL_EXCURSION_CLOCK.md` uses \(f(k)=v_2(k)-1\). Its partial sums are minus the binary digit sum. Solving \(\Delta^2W(k)=2kf(k)\) and putting \(U(k)=W(k)/k\) gives the exact Bessel-chain Poisson equation \(QU-U=f\), with increments \(O(\log k)\). A hyperbolic-sine martingale bounds the maximum level. Together these give a clock error \(C_s\exp(-cr^{1/3})\) and almost-sure mean valuation one. This result concerns the immortal positive excursion, not the full process with returns to zero.

For the high-level trial, each tilted direction dominates an independent fair sign. Disjoint dyadic blocks have probability at least \(c j^{-1/2}\) of reaching \(b\sqrt{2^j\log j}\). The product of their failure probabilities is stretched exponential in \(\log t\). Intersecting with the clock-good event places one such level at a genuine physical date. No independence between the clock and direction event is asserted. Conditioning at the last interior date and using the uniform return envelope converts this to a Haar survival estimate with factor \(s/\sqrt t\).

The full residual uses three explicit payments. The chance of more than a fixed multiple of \(\log t\) departures is polynomially small by the exponential moment. The chance that the total time outside positive excursions exceeds \(t^{4/5}\) is \(O_z(t^{-4/5})\). Finally, the chance of two excursions longer than \(u=t^{7/10}\) is \(O_z(u^{-7/8})=O_z(t^{-49/80})\). For the last estimate, charge a later excursion only after the earlier long excursion has completed; its conditional tail is then \(C/\sqrt u\). Hölder with the fourth departure-count moment pays for the random number of entries. This chronology avoids conditioning a return bound on its own future duration.

Outside those events, an alive path at date \(t\) has one long excursion starting before \(t^{17/20}\) and surviving at least \(t/2\). Its interior high-level trial applies. Summing over all actual labelled entries costs exactly \(s+\mathbb E M=h(z)\). The residual level-t cover consequently has total gauge cost tending to zero. Stop the other cylinders at their first level exceeding a fixed multiple of \(\sqrt{t\log\log t}\); the capacity martingale pays their total cost by \(C h(z)\). This proves the upper bound for every survivor, including all capacity-null paths.

For the lower bound, the stopped fair-walk density gives a Gaussian maximum estimate under the immortal law. Borel–Cantelli bounds its level eventually by an absolute multiple of \(\sqrt{t\log\log t}\). Restricting to a positive-mass subset with one common starting depth gives the mass-distribution lower bound. The forever-positive sets attached to distinct departure histories are Borel and disjoint. Their similarity factors are the Haar prefix weights, so countable additivity supplies the total lower bound \(c h(z)\). Countably many unequal-slope physical intersections have zero measure and can be removed.

The ordinary lane independently reviewed the complete gauge proof. The coordinator also reconstructed `CRITICAL_MERGER_HAUSDORFF.md` and `SURVIVOR_LOWER_GAUGE.md`. The critical gauge \(2^{-t}\sqrt t\) has zero measure: the local capacity domination, the physical meander limit and a conditional martingale argument give unbounded level-to-square-root ratios; stopping at those large ratios makes the covering cost vanish. The lower-gauge note supplies a direct infinite positive-level construction. The prior Haar-null result for the same pair \((x,3x)\) is expressly credited. None of these size theorems decides whether a specified positive integer belongs to the survivor.

### Original pair-process input pins

| Original source | SHA-256 of the inspected TeX | Inputs used |
|---|---|---|
| [Exact rates, 23268751](https://doi.org/10.5281/zenodo.23268751) | `d2f961635d339a4b215c82b1f2f8b9ca53143043f4c58b9aa67290f46056996e` | Uniform physical return envelope, raw and coasted return moments, finite boundary rewards, harmonic capacity and its fixed-state tail. |
| [Late family geometry, 23268753](https://doi.org/10.5281/zenodo.23268753) | `555a0bec4756feb08dc84f8d2e002a675db8a496acbe63ce6e489cb93363bd64` | Positive-excursion physical meander and exponential moments of all departures. |
| [Quantitative synchronization, 23268755](https://doi.org/10.5281/zenodo.23268755) | `2dd65fc17137f55d49d6cc9dc283660b524368a43182dc4a52901d12cd5056bd` | Exact canonical kernel, fresh labelled cylinders, conditional holding mechanism. |

## Actual word closure is now connected to positive integers in Lean

The coordinator read and freshly replayed `AdjacentWordClosure.lean`. Its four public roots prove that final affine divisibility characterizes the complete actual parity word, that an odd-step progression realizes every prescribed word, that the equal-grade carry equation preserves adjacent coordinates, and that arbitrarily large positive odd sources and their triples realize the resulting loop without an earlier synchronous equality.

The last theorem constructs the source above an arbitrary supplied bound. Its actual prefix begins in the residue class \(s\equiv3\pmod4\), reaches adjacent coordinates at date two, and follows both prescribed calendars. A final difference of one excludes every earlier equality by determinism. There is no assumption of the required earlier noncollision.

The central replay compiled both the new module and its `AffineOrbit` dependency into fresh objects, then imported them into a separate axiom audit. Seventeen roots were audited, of which four are new and thirteen were already counted. Only `propext`, `Classical.choice` and `Quot.sound` occurred. The cumulative inventory is 49 distinct central roots plus the separately rebuilt motif specialization, or 50 total. Lean 4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612` were used with cached dependencies. No cold rebuild or independent LeanChecker replay is claimed. The full converse router is still excluded from this checkpoint.

## Bounded motifs cannot support an inexpensive large merger

`BOUNDED_GRADE_PAIRED_PERIODS.md` treats two positive rational periodic phases, possibly from different cycles, related by \(w=3^jz-a\). With both odd grades bounded and the integer affine relation noncollapsed, growing native periods eventually have proportional clocks and are \(o(j)\). The coordinator and literature lane independently reconstructed the proof.

The full reduced denominators agree because multiplication by \(3^j\) is a unit at every prime in the denominator. A long even gap forces that common denominator to be exponential in the larger native period. A fixed-grade S-unit gcd argument first makes the two clocks proportional. Passing to their joint period keeps the joint grade bounded. Bounded \(j\) would leave only finitely many physical affine lines and contradict bounded-grade finiteness after actual positive lifts; hence \(j\) tends to infinity.

Assume along a subsequence that \(j\) is at most a constant times the period. Put the period and all odd positions in a minimal rational affine lattice, and use its coordinates as exponents of two, with \(3^j\) as one additional torus variable. A fixed translated subgroup relation would either force \(j\) constant by its ternary valuation, or confine the clock lattice to a smaller affine hyperplane by its dyadic valuation. Both are excluded by construction.

Remove the common polynomial factor of the two affine carry numerators and the determinant. The remaining determinant and translated numerator are coprime Laurent polynomials. Every prime power in the full reduced denominator still divides their common outside-\(\{2,3\}\) part: the valuation loss is bounded by the already removed numerator cancellation. Clearing each polynomial's own minimal monomial introduces no coordinate gcd. Levin–Wang's original Theorem 1.13(a) bounds this outside-S gcd by an arbitrarily small multiple of the maximum torus height off finitely many proper translates, contradicting the exponential denominator.

The coordinator checked the original 2020 paper and the exact distinction between Theorem 1.13(a) and (b). Only (a) is used; it does not require a nonzero value at the origin. This is an ineffective theorem at fixed bounded grade. It does not imply an exponential lower bound for the merger gap, and it does not handle unbounded motif grades.

## Large defects in nearly balanced windows

The coordinator reconstructed `BLOCK_SUM_DEFECTS.md`, including the noncoprime clock case and both signs of the window-count error. For a length-h exponent window, let \(v=\lfloor hA/p\rfloor+1\), \(\Delta=pv-hA\), and let \(n_v\) count windows whose exponent sum is not v. Paper 22 v4's canonical-root estimate gives width at most \(n_v+\Delta-2\); its original proof was re-read, including the count on each h-orbit. The canonical width bounds the real phase height by \(n_v+\Delta+O(\log p)\).

Combining this with the previous all-origin height theorem gives the rational denominator rate and the ordinary divergence \(s_h(n_v+\Delta+\log p)/p\to\infty\). The exact cyclic derivative gives \(s_h\le2n_v\), so \(\Delta=O(\sqrt p)\) forces \(n_v/\sqrt p\to\infty\). This is a growing multiplier over the earlier square-root obstruction, whose original authors are credited.

Under positive occupation of polynomially bounded states, the exact window identity relates its count error to the logarithmic ratio of its two actual endpoints plus a controlled correction. Low starting states force one tail of the count distribution; low ending states force the other. Therefore every lag with \(s_h\log p=O(p)\) has a positive proportion of errors on each side beyond every fixed multiple of \(p/s_h\). Two-value windows cannot meet this requirement: their gap times the mismatch count is bounded by the total variation of the exponent word. For bounded alphabets the same variation argument forces \(s_h/\sqrt p\to\infty\). The polynomial occupation hypothesis follows, in particular, from any fixed positive balanced-minimum ratio.

The exact replay covers 475 primitive rational cycles, 23,330 signed window identities, 124 noncoprime clocks and 36 proper cancellations in the full denominator. The asymptotic conclusions are the written proof, not a finite census inference.

## A genuine local obstruction at every width above three

`WIDTH_THREE_LOCAL_BARRIER.md` uses the exact sixth-difference polynomial from the pinned PR213 source. Its positive coefficients occupy six slots and its negative coefficients are minus two at three slots. A legal three-edge calendar with windings 1,2,1 realizes the signed digit cancellation

\[
9\cdot2+6\cdot1-8\cdot3=0.
\]

Duplicating each positive coordinate matches the actual stencil coefficients. One gadget has height 0,2,2,0; swapping its two triples has height 0,-2,-2,0. Irrational rotation places both gadgets, with arbitrarily long prescribed padding, at folded phases available whenever the physical width exceeds three.

The ordinary realization is exact. The terminal odd-output congruence modulo \(2^{B+1}\) enforces every specified native valuation. A simultaneous congruence modulo three makes all sources ternary units. The carry cancellation forces the stencil sum of the source residues to vanish modulo the full product modulus. Adjusting its final coefficient-one slot sets that sum exactly to zero without changing any source class.

Adding a sufficiently large multiple of \((1+j)^5\) makes every spatial difference through order five positive throughout the finite rectangle. The sixth-difference stencil annihilates this polynomial. A still larger common constant makes all ordinary states positive and places their global width below the prescribed \(R>3\); irrational phases and the strict first differences ensure distinctness. These are actual finite parallel ordinary trajectories with all requested predecessors and successors. They are not a closed ordinary cycle. The construction refutes an unrestricted extension of the local sign classification, while leaving a global circuit argument available.

The central replay checks 52,672 exact odd edges, 230,900 positive lower differences, and widths strictly between three and 3.1, 3.01 and 3.001. The largest tested minimum has 2,217 bits. Normal and optimized runs agree. The earlier finite-path interpolation and four-copy carry obstruction are explicitly credited at their exact commits.

## Algebraic corrected limits force extra divisions

The coordinator and cycle lane independently reconstructed `ALGEBRAIC_GROWTH_DEFICIT.md`. On a fixed positive odd orbit with positive lower exponential growth, the corrected real height \(P=\lim 2^{A_j}3^{-j}a_j\) exists and is positive. The result assumes additionally that P is algebraic of degree d. It does not derive this assumption from growth.

The quantities \(R_j=2^{A_j}3^{-j}(a_j+1)\) increase strictly exactly when an odd step has more than one division. Their exact increment and tail bound use one tested prefix at a time. If two successive strict increase dates u,v are well separated, the earlier rational approximant is close to P at the real place and has numerator divisible by \(2^v\). Its denominator is \(3^u\). Bugeaud–Evertse's original Corollary 5.2 bounds the number of such rational lines uniformly at a fixed gap ratio; rational P is allowed, and no unmentioned primitivity assumption is imposed.

The actual dyadic valuation condition and the height threshold are paid by discarding \(O((1+S_N)/\eta)\) early dates. Integrating over gap ratios and optimizing the cutoff gives the stated \((\log N)^{3/2}/\sqrt{\log(6d)\log\log N}\) lower bound on cumulative extra divisions. The proof follows the published quantitative gap architecture, with a new actual-prefix identity and two-place transfer. The corrected-height cocycle and smooth-part obstruction from the concurrent pinned work are credited.

The finite replay checks 132 ordinary sources, 14,256 physical odd steps, 50,966 neighboring increase pairs and 420 artificial truncated endpoints. It verifies the exact identities and finite inequalities. It neither constructs a growing ordinary counterexample nor checks algebraicity of an infinite limit.

## Publication evidence and remaining scope

All three new exact checkers passed central normal and optimized runs with identical output and stable source hashes. The four new Lean roots passed a separate central fresh-object and import audit. The sixth checkpoint's exact-tree validation receipt is included here. The selected seventh tree is validated in a clean complete checkout before publication; its own receipt is retained for the following checkpoint to avoid a self-referential commit hash.

The full converse router, the next global two-grade cycle argument and any later arithmetic extensions are excluded until separately reviewed. Repository validation establishes repository integrity, not the truth of an asymptotic theorem. The central unresolved issues remain the specified-source ordinary survivor, the ordered-carry upper bound and the global integrality constraint for closed ordinary cycles.
