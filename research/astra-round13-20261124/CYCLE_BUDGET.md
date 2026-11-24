# An explicit common correction budget and a one-division test for contracting scalar cycles

**Status.** Written orbit-counting and classification proof, with exact rational finite arithmetic replay. The Lean companions target only the finite algebraic implications listed below; compiler status is recorded separately. Collatz remains open.

## 1. Count entire dyadic shells

Let S be any forward invariant set of positive odd integers on which the odd Collatz map U is injective. Suppose all elements exceed 2^68. S may be an infinite escape orbit, a primitive cycle, or the union of all nontrivial periodic points if the verified floor is used. For a finite list of repeated laps through a cycle, its set of vertices must be used only once.

For n≥69 put X=2^n, m=floor(log_3(2^(n-2))), and let F_n count S through X. Every length-m actual gap word with sum A satisfies
`U^m(q) ≤ 3^m q/2^A + (3/2)^m − 1`
by the positive complete affine carry bound. For A≥n and q≤X the endpoint is strictly below 2·3^m≤X/2. All such sources together inject into S through X/2, because the odd clock m is common and U preserves S injectively. For A<n each gap word selects one residue modulo 2^(A+1). This modulus divides X exactly; its count in [1,X] is X/2^(A+1). Therefore

    F_n − F_(n−1) ≤ 2^(n−1) T_n,
    T_n = 2^(-(n−1)) sum_(j=m)^(n−1) binom(n−1,j).

Indeed the word sum is (X/2) times the probability that the m-th success in independent fair bits occurs by time n−1. This is an equality of finite binomial counts; the orbit carries no probability assumption. Note that the cardinality bound on the shell follows by subtracting F_(n−1) after counting *all sources through X*. It does not assert that large-clock sources in that shell correspond bijectively to the lower shell.

Every q in the nth shell is strictly larger than 2^(n−1), giving

    sum_(q in S) 1/(3q) ≤ (1/3) sum_(n≥69) T_n < 17/50.

For 69≤n≤511 the supplied exact integer-binomial program bounds the partial sum divided by three by 335142/10^6. For n≥512, 2^27>3^17 implies m≥(17/27)(n−2)−1≥5n/8. Comparing the binomial tail termwise with (3/2)^(j−m) yields

    T_n ≤ (5/4)^(n−1) (3/2)^(-m) ≤ r^(n/8),   r = 390625/497664 < 1.

Grouping n by floor(n/8) bounds the remaining sum divided by three by 8r^64/[3(1−r)] < 3/10^6. These two rational bounds imply the strict advertised bound. The distributional comparison pertains only to the finite cylinder counts.

## 2. One common budget for all nonstandard positive cycles

Take S to be the union of the distinct vertices of all nonstandard positive cycles above the floor; if all nonstandard cycles lie above it, this is the entire nonstandard periodic set. Injectivity holds on this union because a periodic vertex has a unique predecessor within its cycle and a shared vertex identifies the cycles. The hypothesis that all nonstandard cycles lie above 2^68 follows from the published computation verifying all starts below 2^71. That computation is an external input, not replayed here. The high-set statement in §1 is independent of it. [David Barina, *Improved verification limit for the convergence of the Collatz conjecture*, §6, 2025](https://doi.org/10.1007/s11227-025-07337-0).

On a primitive cycle C of k odd steps and full binary clock A, multiplication of the ordinary equations yields

    log(2^A/3^k) = sum_(q in C) log(1+1/(3q)) > 0.

There is also a logarithm-free rational proof of the per-cycle half-bit inequality. For a finite list of nonnegative corrections x, let P be the product of 1+x and S their sum. For S<1 induction gives P(1−S)≤1. At the next correction x, (1+x)(1−S−x)≤1−S. A second induction gives P(2−S)≤2+S, since the updated left-hand side is P(2−S)+xP(1−S−x), and the second summand is at most x by the first bound. Hence if S<17/50, P<117/83 and P²<2. This applies directly to all distinct-source arcs.

Since log(1+x)≤x, positivity and disjointness show that the **sum over all distinct primitive nonstandard cycles** of these clock overshoots is less than 17/50. In particular

    0 < A − k log_2 3 < 1/2,   A = ceil(k log_2 3).

Indeed log 2>2(1/3+(1/3)^3/3)=56/81>17/25 by the series of log((1+x)/(1−x)) at x=1/3 (or integrate 2/(1−x²)>2(1+x²)). Each individual bound also applies to the ordinary fixed point q=1 by direct inspection, since 4/3<sqrt(2). The common budget excludes the fixed point. A cycle traversed several times need not satisfy this bound with the repeated period. In particular, writing M_k for the number of distinct nonstandard primitive cycles of length k and d_k=ceil(k log_2 3)−k log_2 3, the *simultaneous* bound is sum_k M_k d_k < 17/(50 log 2). This bounds multiplicities for fixed k, for example at most one cycle when d_k≥1/4. If infinitely many distinct cycles exist, their positive overshoots must be summable.

More generally, on **any** distinct-source arc inside such an invariant S, let X=3^n q_i and Y=q_(i+n), with n>0. Its actual clock A satisfies X<2^A Y<sqrt(2) X. Thus the two endpoint heights and the odd step count alone determine A=ceil(log_2(X/Y)). For a proposed pair the necessary gate can be tested with positive integers by comparing X²<(2^A Y)²<2 X². A full primitive cycle counts as a permissible arc because its n source vertices are distinct, even though the endpoint equals its initial source.

For a fixed escaping positive ordinary source q, the odd orbit is injective and tends to infinity. Choose any tail minimum q_r exceeding 2^68, so that q_(r+n)≥q_r for every n; such r exist arbitrarily far along the same orbit. Apply §1 to this single infinite forward orbit. Its complete correction product on every finite prefix satisfies E_(r,r+n)<sqrt(2), simultaneously for all n. The affine equation q_(r+n)/q_r=3^n E_(r,r+n)/2^(A_(r,r+n)) therefore gives

    A_(r,r+n) ≤ floor(n log_2 3 + 1/2)  for every n≥1.

No bound on intermediate heights or exchange of finite source witnesses is involved. This one-sided ordinary clock restriction is compatible with divergent symbolic paths. Qualitatively, an arbitrarily small positive slack far enough along an escaping source already follows the older reciprocal summability result.

## 3. Eliminate all paid carries on the contracting branch

The actual scalar at each vertex of a primitive k-cycle is periodic on that same k-clock; its canonical phase and nonnegative integer carries are periodic there as well. Let B be its canonical clock and K the sum of carries over **one primitive ordinary cycle**. The exact telescope gives A=B+2K. If the minimal canonical phase has 3^L<2^s, its period L divides k and hence 3^k<2^B. The clock band in §2 implies 2^A<2·3^k<2^(B+1), so K=0. Every individual carry vanishes. The fixed point has scalar one, gap two, and also has zero carry.

Let a rational canonical phase have primitive contracting b-word of length L, total s, and ordered carry C_b from the affine return
`2^s z_L = 3^L z_0 + C_b`.
The only possible actual periodic solution with that phase is the canonical rational orbit anchored at z_0=C_b/(2^s−3^L). Indeed every actual gap equals its canonical letter by zero carries. The return map with the affine law is a strict contraction, so its only finite periodic point is its fixed point z_0, even if the actual cycle was initially assumed to have a longer period. Conversely, **the single divisibility (2^s−3^L) | C_b is sufficient**: write every cyclically rotated canonical rational point as C_rot/(2^s−3^L), with C_rot odd because its i=0 term is odd and all others are even. The denominator is odd. If z_0 is integral, then the identity 2^b z_1=3z_0+1 implies z_1 has denominator dividing a power of two. Since its reduced denominator is odd, z_1 is integral. Repeat around the orbit. Every such integer is odd and positive, so the valuations are exactly the b letters. Its actual scalar is the unique periodic solution to h_(i+1)=3h_i−b_i, equal to the supplied canonical phase representatives. Thus, conditional only on the published floor, for each supplied contracting canonical phase there is at most one primitive positive cycle, decided by integer division. An arbitrary supplied *source* with that phase must enter this cycle by the R12 guarded classifier; passing the phase test alone does not decide that a prescribed source reaches it.

For a primitive canonical word of length L, this immediately rules out every contraction with 2^s≥sqrt(2)·3^L, since any realized primitive ordinary cycle has exactly length L after the carries vanish. For a fast test with integers, square both sides. For controls inside the surviving band, the exact program uses words made of two constant runs, both nonempty, hence primitive. At lengths 512, 1025 and 4097 their canonical maxima have integer parts of 127, 252 and 998 bits respectively. Each passes the half-bit clock filter but fails the one-division test. These examples illustrate avoiding a global-height graph enumeration; a separate phase-specific local-minimum test could already resolve examples with small canonical minima.

This gives no contradiction for every contracting word: a divisibility success constructs an actual cycle. Expanding canonical phases can have paid carries; the ordinary clock band restricts their A, while leaving the individual carries open. No divergent fixed-source realization is excluded on that branch solely by the cycle argument.

## Source and verification audit

* PR182 Round 3, a7fd3ac9e5bff7412858df23d776bb847e9c1371, GLOBAL_ORBIT_COUNT.md §§1–4: the injective invariant-set and complete-word statements exactly cover cycles and their disjoint union. Its asymptotic big-O alone gives no numerical budget. Here the dyadic count and tail certificate provide the constants.
* Historical antecedent: research/astra-three-routes/pass2/ORBIT_MELLIN.md already gives an explicit cycle error bound in the orbit minimum. The contribution here is a small numerical uniform total at the verified floor, its common cycle budget, and the resulting carry classification. No literature priority claim.
* Actual scalar source f94a2ae1caba9a1857feda892ee1779695eea9d2; PR188 beed685ab713923191ae40c9559bf7400298d2d3, SCALAR_COCYCLE.md; PR187 099058f3f2602a48e109c964899f0a9a2a223338, fixed-source-repeat-obstruction README. The PR188 telescoping calculation and PR187 two-position argument preserve the same source. The repeat theorem does not supply repetitions on arbitrary phases.
* R12 is **published** at cbec52dde5bed390a693310dd04e911033ba0cc9, README blob fd8ef7549d98790bde1f5fbaac91992c891d8818. Audited the local (3) in its four cases, the exceptional-tail whole-orbit count, the direction of the prefix lower bound, shell inversion and summability, the window Markov count and 3-adic endpoint packing, and the contraction comparison. No logical defect was found in these written implications. Its equality decision propagates a candidate and rejects false guards; a guard-passing repeat still requires the comparison to the true scalar. Its confined functional graph omits escaping edges soundly because every actual cycle of that phase satisfies the uniform bound. The height result is a liminf bound for prefix maxima and supplies no universal opposing height estimate. Its controls are finite exact tests.
* cycle_budget.py uses exact arithmetic, with explicit exceptions and no optimization-sensitive assertions. Replay with python -B and python -O -B. CycleBudget.lean states both rational product estimates, the strict squared half-bit bound, the consequent one-bit clock band, and zero periodic carries given the band and telescope. IntegerClock.lean isolates zero carry and uniqueness of the integer clock with only the Lean standard environment. The dyadic count, analytic tail, and one-division recognition in this document are written proofs. The companion neither formalizes the verified floor nor the full conjecture.

### Kernel receipts

On 2026-11-24 the standalone mathlib file CycleBudget.lean (SHA-256 177ec2128103c1607d4d775e85adf1daf8a0fcc1f5b4d3ed77bc478bb42c3b65) passed Lean 4.34.1, compiler commit 5045d0056413266e57c625dcd7c365b10e377c52, with Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612 and flags `-j1 -DwarningAsError=true`. Exit 0. All six printed transitive axiom sets consist of propext, Classical.choice, Quot.sound. IntegerClock.lean (SHA-256 ef9b2fa141fdb8f735fd9f47b2aabf3aa87cf04b5b966b153cc030406a9038ec) also passed with the same compiler and flags, exit 0. Its integer clock uniqueness proof uses propext and Quot.sound; zero carry also uses Classical.choice. Complete stdout appears in the two accompanying check receipts. The endpoint_squares theorem has the two-sided strict **integer** square comparison as its conclusion, with the ordinary exact product identity and correction budget as explicit hypotheses. The analytic and invariant-set statements remain written, and the verified floor remains externally sourced.
