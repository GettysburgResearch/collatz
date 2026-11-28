# Eleventh coordinating review: denominator spectra, residue order and arithmetic occupation

Date: 2026-11-28. Branch: `research/astra-critical-rigidity-20261128`.

## Status and scope

The coordinating lane reconstructed the nine new mathematical notes in this checkpoint, read the exact programs, and independently replayed all eight controls with normal and optimized Python. The new `ResidueFiberOrder` public root was freshly compiled and imported into a separate axiom audit. The mathematical notes remain **proposed written theorems**; the finite controls verify their stated identities and examples, not their infinite conclusions. Classical Diophantine and algebraic inputs are cited at the point of use.

This checkpoint gives explicit prime-power spectra, realizes every positive rational denominator rate, and sharply separates prime and composite grades. It also proves the ordered-fiber kernel needed to retain the complete denominator in a physical cycle clock. The ordinary clock upper bound, the worst-case pure-three landing-time bound, exclusion of all nontrivial integer cycles, and convergence of all integer trajectories remain open.

The logarithm constants in the cycle notes here use the previously checked input with irrationality exponent at most 5.116201. A newly discovered primary-source claim of exponent three is undergoing its own source and fresh-build audit. It is not silently substituted into these proofs or used to certify any statement in this checkpoint.

## 1. Prime-power spectra: including the ramified factors

`PRIME_POWER_SPECTRA.md` completes the earlier fixed-grade decision theorem with explicit spectra at every prime power. For an odd prime \(\ell\) and \(p=\ell^a\), the possible rates are exactly

\[
\left\{\frac{1+\sum_{b\in B}\varphi(\ell^b)}p:
 a\in B\subseteq\{1,\ldots,a\}\right\}.
\]

The binary cases are \(\{1\}\) at two, \(\{3/4,1\}\) at four, and every integer multiple of \(1/p\) from one half to one at \(p=2^a\ge8\). Every value is attained by a primitive physical family with \(\log_2q=\sigma L+O_p(1)\).

The coordinator checked the full radical-degree reduction. The prior abelian-field argument supplies degree at least \(k'/\gcd(2,k')\), so only a factor of two can be missing from a cyclotomic component. The odd-prime proof includes the ramified prime three: in the remaining even-exponent case, the relevant square root defines an unramified or split quadratic extension at odd residue characteristic, and its odd valuation forces the entire remaining two-power degree. It is not enough merely to invoke the unramified valuation used for primes at least five.

At binary grade, the order-four component can split: \((1+i)^2=2i\). Higher two-power orders retain full degree because the appropriate cyclotomic square root would require the next primitive root of unity; the norm argument then forces the successive square-root tower. This is why a whole-cyclotomic-order analysis alone misses the half-rate family. The coordinator checked the retained-order least-common-multiple condition, the integral rate quantization, and the reduction from a shorter common clock.

For attainment away from one half, the digit construction factors the carry into elementary digit sums. Evaluation at each cyclotomic order gives the asserted exact support, while the top-order support proves primitivity. At grade eight the exceptional half-rate example has an explicit factorization and a nonzero residual resultant, 21,520,080. The higher-grade version uses eight groups of three motif carries in arithmetic progression. Its four surviving roots give rate one half; the only possible repetition is excluded by the opposite carry changes after four groups. These are actual positive rational cycles with recomputed complete denominators.

The prime-power control checks 50 primitive physical cycles, 12,332 distinct native states, 44 whole-order subsets and five eight-group families. Polynomial greatest common divisors, residual resultants, all native parities and least periods are verified exactly. Both other research lanes independently reconstructed this note.

## 2. Every rational rate, with a common fixed grade

`EVERY_RATIONAL_DENOMINATOR_RATE.md` proves an inverse construction. For any finite set of rational rates in \((0,1]\), there is a common group count \(g\) such that all sufficiently large fixed grades \(gr\) admit every requested rate on length \(gn\). Each family is primitive and has bounded additive error in its logarithmic denominator.

The finite motif input is `Collatz.BlockClock.cover` at commit `505d3fe782922904e86477990cc5d41e9110edda`, path `research/astra-infinite-descent-20261127/merger/BlockClock.lean`. Checkpoint three freshly rebuilt its eight dependencies and the local `SharpMotifInput` specialization. That receipt is an input here; the new Fourier construction is not claimed to be a Lean theorem.

The coordinator reconstructed the passage from consecutive positive motif sources to a common arithmetic progression of carries. Appending identical odd letters is an operation on the words and their affine carry formulas. The argument does not assert that the old integer realizations continue with odd parity after their original endpoints.

For a selected divisor set containing one and \(g\), the integer sequence of Ramanujan sums has exactly the requested Fourier support. It stays in the finite carry progression supplied by the motif theorem. The complete carry polynomial consequently retains exactly \(k=\sum_{d\in S}\varphi(d)\) roots of the full clock polynomial. Monic cancellation and a fixed nonzero resultant give the full-denominator estimate. The presence of primitive \(g\)-th characters excludes a shorter physical period.

The anchored totient subset-sum step is explicit. For \(g=2^aN\), with odd \(N\), the powers of two fill an initial integer interval. The divisor blocks for odd divisors have steps at most \(\varphi(N)\); choosing \(2^a\) large enough prevents gaps when these progressions are added. Reserving the top divisor yields all integer sums from \(1+\varphi(g)\) through \(g\). Taking \(\varphi(g)/g\) sufficiently small and making all target denominators divide \(g\) realizes the finite target set. This establishes that the union over fixed grades is exactly \(\mathbb Q\cap(0,1]\).

A separate diagonal construction lets the grade grow more slowly than any prescribed divergent function of length and attains each real limit in \([0,1]\). Fixed-grade constants are absorbed by choosing each later length after fixing that stage's grade. There is no claimed uniform effective onset across all grades. The exact control checks 70 physical profiles, 27,216 distinct native states and 49 anchored totient intervals covering 110,632 integer numerators. Both other lanes independently checked the proof.

## 3. Composite scale and the full-denominator pumping obstruction

`COMPOSITE_DENOMINATOR_SCALE.md` bounds the least rate \(s(p)\) by

\[
p s(p)\gg \frac{(\log p)^2}{\log\log p}\quad(p\ge3),
\qquad
p s(p)\ll \frac{(\log p)^3}{(\log\log p)^2}
\quad\text{for infinitely many }p.
\]

For the lower bound, assign each maximal prime power dividing the common clock to a retained cyclotomic order containing it. The sum of totients controls, up to an absolute factor, the sum of those prime powers. Splitting small and large prime powers and using the elementary Chebyshev bound for the logarithm of a least common multiple gives the squared-logarithm lower bound. If the common clock is too small, the simpler radical-degree estimate is already stronger. The coordinator checked both regimes, including the factor-of-two possibility.

The upper construction uses one address prime and distinct data primes. At most one address indicator is active at each date, so the shift is binary and every odd gap is one of three neighboring integers. The exact Fourier support has size \(h(1+\sum_i(\ell_i-1))\). The only delicate noncancellation, with no nontrivial data character, is checked by clearing denominators and reducing at one data prime. The support generates the entire character group, which proves physical primitivity. The finite bound \(q\le(2^n+3)^s\) is kept separately from the fixed-grade asymptotic rate.

The note also gives an exact motif-transfer obstruction. With motif denominator \(q_0\), shifted-copy sum \(S\), and complete final denominator \(q\),

\[
q_0/\gcd(q_0,S)\mid q,
\qquad
\operatorname{ord}_{q_0}(3)
 \le N2^B\operatorname{ord}_q(3).
\]

The first statement is obtained prime by prime before discarding any clock factor; the second uses the actual kernel of reduction of unit groups. Thus a low total denominator rate does not by itself provide a cheap periodic pump. For the one-odd motif, a superlogarithmic pump with sublinear shift spread would still require the unresolved subexponential-order behavior of the full modulus \(2^n-3\).

The exact control checks the three support sizes 14/30, 33/105 and 85/385, all 8,320 native rational steps, and 128 motif-transfer cases including negative shifts and nontrivial denominator loss. It checks orders for the mandatory retained divisor; it does not claim to factor every large final denominator.

## 4. Residue-fiber inversions and the new Lean root

`RESIDUE_FIBER_INVERSIONS.md` works with the entire odd-dyadic lift of one primitive positive rational cycle. With odd period \(p\), total division exponent \(A\), \(g=\gcd(p,A)\), \(P=p/g\), \(B=A/g\), and complete denominator \(q\), put

\[
h=\operatorname{ord}_q(3^P2^{-B}),\qquad \operatorname{ord}_1=1.
\]

The residue-fiber inversion count \(I_q\) satisfies \(I_q\ge g/h-1\) and \(I_q\equiv g/h-1\pmod2\). Width at most nine has no inversions and therefore forces \(g=h\), in particular \(g\le q\).

The coordinator checked the homogeneous lift, its unique dyadic rays, both commuting maps, and the fact that equal residue gives an actual positive odd integer in the inversion relation. Sorting swaps adjacent inverted points together with all their dyadic translates. Each swap removes exactly one inversion orbit, preserves the residue action and mean winding, and changes the permutation of rays by one transposition. The sorted map is increasing between fibers. On a residue-preserving combination, transitivity makes its rank shift the same on all fibers, and its sign agrees with mean winding. This identifies every sorted cycle length as \(hP\), so there are \(g/h\) cycles. Transposition count and parity give the result.

The width criterion is checked from the actual inverse chain: below the next possible inversion threshold, the only candidate is \(8x+1\), and its two odd successors force \(9x+2\). This contradicts width at most nine. Actual rational examples of width approximately 10.533 and 14.145 have \(h<g\); they explicitly rule out dropping the width or inversion hypothesis.

The preceding ordinary full-circuit argument is credited at commit `5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128` in the note's exact source link, path `research/astra-diagonal-frontier-20261127/arithmetic/FULL_CIRCUIT_INVERSIONS.md`. The coordinator read that pinned source in full and checked that the present claim adds the full-denominator residue resolution on the odd-dyadic lift, rather than relabeling the earlier ordinary result.

The separate Lean theorem `Collatz.ResidueFiberOrder.residue_order_eq_period` proves the ordered-fiber kernel. Given a finite-period self-map of a linearly ordered type, an equivariant group-valued residue, strict increase on each residue fiber, and a cyclic phase advancing by one, it derives equality between the group multiplier's order and the full period. The desired order is not assumed. Iterating by the multiplier order preserves a fiber; a strictly increasing finite-order self-map is the identity there; the phase then gives the reverse divisibility. The proof is valid for a general group.

The new module was freshly compiled with Lean 4.34.1, Mathlib source `d13f23b723b8a846827a245b89c10fc7d3f11612`, and a separate imported-root audit. Its only axioms are `propext`, `Classical.choice`, and `Quot.sound`. Cached third-party objects were reused. The physical lift, sorting argument and width criterion remain written. The cumulative inventory is **68 central public roots, or 69 including the separately rebuilt motif specialization**.

The exact inversion control covers 819 bounded primitive cycles and 12 named cases, including the wider counterexamples. It checks actual parities, complete denominators, sorting, mean winding, all-cut return signs and the count/parity identity.

## 5. Reduced-clock six sums and four-sum spacing

`REDUCED_CLOCK_SIX_SUMS.md` combines the full-denominator clock identity with the previous six-sum argument. Its modular-inverse stride constructs one spatial grid for the reduced period \(P\), but every column still obeys the recurrence on the full physical chronology. A stride can cross many full cycles. The de-meaned angular correction is periodic, so all full-lap contributions cancel exactly. The coordinator checked the integer scaling of each interior grid point and the alignment at every retained start; no fictitious reduced physical cycle is introduced.

Writing \(\nu=5.116201\), \(\theta=\eta\log_2(4096/924)/(6\gamma)\), \(\chi=\eta\ln6/(3\ln3)\), and \(b=1/(\nu\theta)-1\), the new period exponent is

\[
\max\left\{\frac b{b+\chi},
 \min\left(1-\chi,\frac{1-\nu\theta}{1-(\nu-1)\theta}\right)\right\}.
\]

It tends to approximately 0.681989 as the width bound tends to three. The proof splits \(\log m/\log p\le1\) from the complementary regime, retaining the earlier four-copy source count in the former and the reduced-clock six-sum bound in the latter. The separately pinned four-copy source theorem was reconstructed in the preceding review. Its dependence on the complete denominator is preserved.

The new focused control uses four genuine multisheet cycles. Positive and negative modular-inverse samples cover 20 to 133 physical laps; all 3,470 affine-column checks, the complete-denominator sheet orders, and the exact interior grid alignments pass. The previous six-sum checker is unchanged and is included in the source dependency fingerprints.

`FOUR_SUM_GEOMETRIC_SPACING.md` addresses the gap left by the triple-sum theorem. A five-region integer recurrence proves that any four-sum comparison which is zero at one origin stays within absolute value 20 at every origin. The coordinator checked each predecessor cap, the forced zero defects in the last two regions, the divisibility restriction, and the backward propagation around the transitive cycle. Comparisons above the corresponding geometric threshold have a strict global sign.

Actual dyadic code collisions then force at least \(p^{4.4676419-o(1)}\) eight-distinct offset tuples with geometric four-sum difference at most \(p^{-4.8439723+o(1)}\), for a hypothetical growing ordinary family of width at most \(3+o(1)\). The lower count uses the fourth collision moment of the binary cube. The earlier triple-order theorem removes common indices; repeated indices and diagonal tuples cost only a lower-order number of possibilities. Eisenstein separation ensures the surviving geometric differences are nonzero.

This is a reduction to a concrete analytic spacing question. No incompatible upper bound has been proved. In particular, a generic moment theorem with several moment equations cannot be applied to the single geometric-value condition without an additional argument. The exact control checks 2,155,686 integer predecessors and all 273 nonempty uniform subsets of binary cubes of lengths one through three. Its eight-element integer example is a genuine three-sum Sidon set with an eight-distinct four-sum collision; it is correctly labeled as a combinatorial example, not an integer Collatz cycle.

## 6. Crossing cofactors and descending marked levels

`CROSSING_MARK_ARITHMETIC.md` and `LOCAL_CROSSING_COFACTORS.md` strengthen the earlier crossing occupation estimate. The signed impulses are retained exactly: outward contributes \(-1\), inward contributes \(3^{j-1}\), and a simultaneous odd departure contributes \(3^j-1\). Unrolling a fixed number of marks gives a positive high-power part and a nonnegative low part, with coefficient height controlled by native span.

For every fixed finite prime set containing two and three, the total deficit of the cofactor outside that set is at most \(\varepsilon I+C M\), where \(I\) is productive crossing weight and \(M\) is ordinal mismatch count. The coordinator checked the distinction between real-size deficit and prime-valuation deficit, the single sign flip for a sufficiently small negative productive value, the short-packet valuation separation, and the long-packet charging argument.

The stronger local form removes the total-period error term. If the initial two-adic valuation occupies a positive fraction of the current level, a fixed number of subsequent marks must fit in an arbitrarily small relative native span. Stopping inside the first putatively long even gap gives a moving-coefficient logarithm inequality whose coefficient height is too small. Otherwise the two-endpoint estimate bounds the packet span, and fixed-prime separation bounds the number of large valuations independently of packet size. Partitioning into large fixed mark packets gives the stated \(\varepsilon I+C M\) error.

The external moving-coefficient input was checked directly in Calegari–Dimitrov–Tang, Theorem 1.1, at `https://math.uchicago.edu/~fcale/papers/ICM.pdf`. For a fixed finitely generated group and fixed place, sufficient closeness of \(A\gamma\) to one bounds the height of \(\gamma\) linearly in \(1+h(A)\). This includes the nonarchimedean use. The review verifies the theorem's applicability and all internal reductions; it does not reprove that external theorem or its alternative holonomy proof.

The crossing control checks 510 closed adjacent calendars, 43 closed high packets, 54,626 open high integer windows, and 780 thin rational windows reaching level 774. It also records negative windows, sign flips and both zero and positive low-part cases. Some rational line controls have equal physical arms with a nonzero graded line; the claim is about the exact line identities there, not an assertion that these are unmatched ordinary pairs.

`DESCENDING_NUMERATOR_COFACTORS.md` gives a uniform marked-level result. With fixed prime support of the denominator cofactor \(q\), any consecutive window of \(w\) descending levels has at most \(\varepsilon w+C\) odd numerators whose outside-prime cofactor is below \((q3^h)^{1-\delta}\). The exact interval identity has a positive carry sum. For a bounded number of grade departures, the two-endpoint estimate bounds native span in terms of endpoint cofactors. Small real values and large fixed-prime valuations both force a positive fraction of logarithmic height per selected gap. Their number in a fixed packet is therefore bounded independently of packet length; the final partition gives the density estimate.

The coordinator checked signed sources, the possible terminal zero, the enlarged finite prime set containing the support of \(q\), and uniformity in the size of \(q\). The control covers 1,872 signed sources, 11,432 descending levels and 44,144 intervals, including 1,590 nontrivial common-prime valuations, 2,708 flip windows and 19 terminal-zero cases. The largest tested denominator has 358 bits. None of these marked-level statements bounds the worst native wait between levels.

## 7. Reproduction and publication boundary

The eight central control receipts record the exact script, manuscript and imported-checker fingerprints, interpreter version, stdout hashes, return codes and equality of normal and optimized outputs. Every selected guard is explicit and remains active under `-O`. The Lean receipt records the source hash, compiler and Mathlib pins, selected public root, separate import audit and exact scope of cached dependencies.

The source manifest binds the reviewed manuscripts, new formal source, checker inputs and author receipts. Repository validation is run from a clean detached checkout of the frozen selected commit before publication. That validation checks repository integrity; it does not prove the proposed mathematics. The preceding checkpoint's clean-validation receipt is included here, and this checkpoint's post-freeze receipt will accompany the next checkpoint so that it can name the exact validated commit without a circular self-reference.

Frequent checkpoint publication protects the reviewed work while the remaining research proceeds. No main-branch merge, proof of Collatz, effective last exceptional cycle, or proof of the worst-case logarithmic paired-clock bound is claimed.
