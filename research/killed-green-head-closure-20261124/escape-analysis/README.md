# An exact-clock finite test for escape and nontrivial cycles

**Status.** PROPOSED mathematical reduction. The upper estimate in the test is OPEN. The proof uses ordinary inverse arithmetic and the finite simple-path counting argument recalled below. It does not assume the analytic inverse floor F, the renewal input R or an independence hypothesis.

The [two-ended bridge](../two-end-bridge/README.md) at PR 201, `73a145ca99448a78219bd149e273f33b6e3fda4b`, §4 uses F to get a nearly linear lower count as the depth tends to infinity at a *fixed* terminal on an escaping ray. We give up that order of quantifiers. The clock remains exactly twice the odd depth. A nonconvergent orbit leaves enough unused clock to grow an elementary binary predecessor tree and correct the clock and source congruence simultaneously. The resulting test covers escape and nontrivial positive cycles.

## The finite statistic

Use the shortcut map T and the odd map U(x)=(3x+1)/2^v₂(3x+1). A unit is a positive odd integer prime to three. A chronological word w has length b, total valuation s and real offset β with

    U^b(x) = 3^b 2^(−s) x + β(w).

Choose any nonnegative integer function h(b) tending to infinity, for example h(b)=⌊log₂(b+1)⌋. For a unit q and rational 0<ε<1, let N_b(q,ε) count ordinary units x whose b odd steps have total 2b, end at q and satisfy β(w)≥εq. Periodic q and repeated states are allowed in this definition. Form

    M_b(ε) = max {N_b(q,ε) : q a unit and U^{h(b)}(q) ≠ 1},

where the exponent denotes h(b) iterations and an empty maximum has value zero. This is finite arithmetic for computable h. Appending a forward gap g changes β to (3β+1)/2^g≤(3β+1)/2. Starting with β=0 gives β≤(3/2)^b−1. Thus only q≤((3/2)^b−1)/ε need be tested. For fixed q, enumerate the compositions of 2b into b positive parts and test inverse integrality and source membership. Equivalently the carry test on this exact row is 3^b x≤(1−ε)4^b q.

**Theorem.** Exactly one of these alternatives holds.

1. If every positive integer reaches 1, then for every rational 0<ε<1, M_b(ε)=0 for all sufficiently large b.
2. If any positive integer fails to reach 1, there is a rational ε₀>0 such that for **every** sufficiently large b some ordinary unit q has U^{h(b)}(q)≠1 and

       N_b(q,ε₀) ≥ 2^⌊b/16⌋.

   The same q works inside **every prescribed unit source class** modulo 3^K, for each K≥1 satisfying 2·3^(K+1)+1≤b/40. The displayed lower count holds separately in each class. The onset may depend on the fixed nonconverging orbit but is independent of the chosen class, K and h.

Consequently the full positive-integer Collatz conjecture is equivalent to the statement that for every such ε there are arbitrarily large b with M_b(ε)<2^⌊b/16⌋. In particular a cofinal subexponential upper bound per ε suffices. The statistic can be defined with just the class 1 modulo 3 throughout, with the same equivalence.

## Two exact inverse constructions

For an ordinary unit z, the inverse I_e(z)=(2^e z−1)/3 is an ordinary unit exactly when 2^e z is 4 or 7 modulo 9. The six exponents 1 through 6 give all six unit residues of 2^e z, so **two choices** work at every vertex. For each legal choice the result is positive odd and its forward gap is exactly e. After m reverse steps this gives 2^m words of total at most 6m ending forward at the same given z.

There is also a two-gap construction with **any prescribed total** t≥2·3^(K+1)+1, the same terminal z and any specified unit residue r modulo 3^K. Write the chronological gaps as (f,t−f). Their composite requires

    9x = 2^t z − 2^f − 3.

The congruence 2^f≡2^t z−3−9r modulo 3^(K+2) has a solution in 1≤f≤2·3^(K+1), since the right side is a unit and 2 generates this unit group. Indeed the binomial expansion of (1+3^k u)^3 gives valuation k+1 for the difference from 1 whenever k≥1 and 3 does not divide u. Starting from 2²=1+3, this gives v₃(2^(2·3^j)−1)=j+1 and hence the full order 2·3^(K+1) at precision K+2. Now t−f≥1. Reduction modulo 3 gives integrality of y=I_(t−f)(z); substitution into the composite gives x=I_f(y) integral and x≡r modulo 3^K. Both inverse values are positive odd, and y is a unit because 2^f y≡1 modulo 3. This proves the claim for the supplied integer z without changing its lift. The total cutoff is sharp for this two-gap construction uniformly in z and r. For z=13, r=1 and t=2·3^(K+1), the required 2^f is 1 modulo 3^(K+2), forcing f to be a multiple of t, while two positive gaps require 1≤f<t.

## A whole interval of depths at the actual terminal

If any positive source fails to reach 1, remove initial powers of two and take one U step to obtain a fixed nonconverging ordinary unit q₀. Its full odd ray q_j=U^j(q₀) consists of units ≥5, including in the case where it enters a nontrivial cycle. For the actual suffix q₀ to q_i let A_i be its total valuation. Telescoping exact forward steps gives

    2^A_i = (q₀/q_i) ∏_{j<i}(3+1/q_j) ≤ (q₀/q_i)(16/5)^i.
    L_i := 2i−A_i ≥ i log₂(5/4) − log₂ q₀.

For i≥1 the relative carry of this fixed suffix is at least ε₀=1/(3q₀+1). In fact q_i=(3^i/2^A_i)q₀ D_i with D_i=∏_{j<i}(1+1/(3q_j))≥1+1/(3q₀), and its relative carry is 1−1/D_i. Appending this suffix to any positive inverse construction preserves the lower bound, by the positive affine multiplier and nonnegative earlier carry. This argument allows a repeated suffix.

Fix b, choose **any** integer ⌈b/32⌉≤m≤⌊b/16⌋, and set i=b−m−2. Starting at q₀, take each of the 2^m legal reverse words above with total E≤6m, reaching its own actual unit z. The two remaining front gaps must have total t=2b−A_i−E. Uniformly for these words,

    t ≥ L_i+4−4m ≥ b/32+17/5−log₂ q₀

for all sufficiently large b. Here log₂(5/4)>3/10 follows from 5^10>8·4^10. The last bound eventually exceeds b/40, so the two-gap construction supplies the prescribed clock and source class. In forward order each full word consists of those two gaps, the length-m path from z to q₀, and the actual suffix to q_i. The terminal is precisely q_i for **all** choices of the tree word and residue. Distinct tree words give distinct sources because each ordinary source has a unique forward gap sequence and the split positions are fixed. This remains true on a cycle. Also U^{h(b)}(q_i)≠1 for every h.

Taking m=⌊b/16⌋ gives alternative 2. More specifically, for each fixed large i the same q_i works throughout the corresponding interval of b satisfying ⌈b/32⌉≤b−i−2≤⌊b/16⌋. This is a linear-size interval with b comparable to i. It gives no lower estimate as b tends to infinity while i stays fixed.

There is a further multiplicity distinction. On an escaping ray, for each large b the above range of m gives at least b/32−1 **distinct** actual terminals. At most b/64 integers are ≤b/64, so at least b/64−1 of the terminals exceed b/64, each with at least 2^⌈b/32⌉ compatible sources in the chosen class at precisely this same row. On a nontrivial cycle one can instead fix any vertex of that cycle as terminal: once the index interval exceeds the period it contains an index of that phase at every sufficiently large b. Its count is at least 2^⌈b/32⌉. Neither conclusion uses an average over terminals.

## Why convergence gives eventual zero

The independent finite input is the simple-path estimate T-A3-651, [finite records, §1](../../astra-three-routes/pass3/FINITE_RECORDS.md) at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. We recall the argument to make the lack of an external inverse floor explicit.

For any finite simple shortcut path let S be its set of odd states. Then # (S∩[1,X]) ≤5 X^(39/40). For X≥1 put d=⌊(3/5)log₂ X⌋. If d=0 use the trivial count. Otherwise discard the last d odd states (or all of them if necessary). The remaining sources have distinct U^d endpoints in the path. For M=⌊5d/3⌋, words of total A≤M specify one odd residue modulo 2^(A+1) each, hence at most (3/2)X 2^(−A) sources per word since 2^M≤X. The residue follows by inverting the affine word modulo 2^(A+1) with odd endpoint bit, or by prescribing successive shortcut parity bits. At z=4/5 the geometric composition generating function gives

    Σ_{A≤M} binom(A−1,d−1) 2^(−A)
      ≤ z^(−M) [z/(2−z)]^d ≤ ρ^d,     ρ³=3125/3456.

For A>M the odd endpoints lie below σ^d X+(3/2)^d−1 with σ³=27/32<ρ³, by the affine bound. Injectivity bounds their count by [σ^d X+(3/2)^d]/2. Thus the full count is ≤2Xρ^d+(3/2)^d/2+d. Since ρ<2^(−1/24) and ρ>2/3, the first term is <3 X^(39/40). The second is ≤X^(39/40)/2, and d≤(6/5)X^(39/40) from log₂ X≤2√X. The stated constant follows. Integrating the count against dt/t² from M₀ to infinity shows that a finite simple path staying ≥M₀ has Σ_{x∈S}1/x≤200 M₀^(−1/40).

Assume all positive orbits reach 1. For a counted path whose endpoint satisfies U^{h(b)}(q)≠1, all its shortcut states are distinct: any repeat traps q in the eventual cycle through 1 and forces its odd endpoint q to be 1. On a simple path remaining ≥M₀ its relative carry is

    1−D^(−1) ≤ log D ≤ (1/3)Σ_{x∈S}1/x ≤ (200/3) M₀^(−1/40).

For fixed ε choose M₀ so the right side is strictly less than ε. Every counted path must visit some integer below M₀. All forward trajectories from that finite set reach 1, so their union is finite, including all possible q. Their odd states have a common finite upper bound on the number of U steps to 1. Once h(b) exceeds that bound there are no eligible q in the union. This proves alternative 1. The cutoff depends on ε; there is no claim for an arbitrary threshold ε(b) decreasing to zero.

## Two tests using only the recorded row

**A single high threshold characterizes periodic targets.** Fix ε★=1−2^(−100). For every ordinary unit q>1, the following statements are equivalent.

1. q is periodic under U.
2. Some exact row (b,2b) terminating at q has a unit source with β/q≥ε★.
3. For every fixed rational 0<ε<1, all sufficiently large exact rows at this same q have exponentially many sources with β/q≥ε, even in each of the source classes specified in the theorem.

Indeed S at M₀=1 bounds D≤exp(200/3)<2^100 on each simple path, using log 2>2/3 (strict convexity of 1/t on [1,2]). Thus the witness in statement 2 already contains a repeated ordinary state, forcing its terminal q to be periodic. For statement 1 let q₀=q and let p be its period. Choose the unique index i divisible by p with m=b−i−2 in [⌊b/16⌋−p+1,⌊b/16⌋]. For large b this is in the above window. The actual suffix goes around the cycle i/p times, so D_i=D_p^(i/p) tends to infinity and its relative carry tends to 1. Each source class therefore has at least 2^(⌊b/16⌋−p+1) such sources at the supplied q for all large b. Statement 3 gives statement 2 with ε=ε★. The classical finite certificate of periodicity is the period itself; the additional content here is its characterization by a universal carry threshold and its exponentially many witnesses on the single prescribed clock at the fixed terminal.

**A full-conjecture test without a future iteration of q.** Let R_b(ε) be the maximum over units q>1 of the exact row count with β≥εq, retaining each word if q>b/64 or a shortcut state repeats inside its recorded path (including the endpoint). Every positive integer reaches 1 if and only if, for every rational 0<ε<1, there exist arbitrarily large b with R_b(ε)<2^⌈b/32⌉.

Under convergence every row ending at q>1 is simple and high carry confines q to the finite forward image of the small gate set for ε. Hence eventually R_b(ε)=0. On an escaping ray use the b/64−1 terminals above b/64 already constructed. On a nontrivial cycle use a fixed periodic q; its suffix contains a full period when b is large and the bound 2^(⌊b/16⌋−p+1) exceeds 2^⌈b/32⌉ eventually. Thus either way there is a fixed ε>0 and at least one eligible terminal with the claimed exponential count at every sufficiently large b. All tests here inspect only the recorded source-to-q path. The earlier statistic M_b keeps the larger explicit exponent 1/16.

## Scope, provenance and first missing step

Applegate and Lagarias use the classical pruned inverse tree and its modulo-nine rule in [Lower bounds for the total stopping time of 3x+1 iterates, §2](https://websites.umich.edu/lagarias/doc/3x%2B1bound.pdf). The real carry, the finite small-state cutoff and the idea of appending the actual terminal suffix already occur in PR 201 §4. Here the deterministic slack of a nonconverging suffix pays for a branching inverse family and a fixed-total, two-gap congruence correction. The moving-depth conclusion and the finite forward test change both the quantifiers and the coverage of that earlier criterion.

The unresolved step is a cofinal upper bound below the explicit exponential threshold for the **maximum** M_b(ε), for every fixed ε. The proof of eventual zero in the convergence case assumes the desired orbit conclusion. It is not such an upper bound under the present state of knowledge. The elementary floor in the other direction counts a smaller family than the order q(4/3)^b/√b in the earlier criterion and does not imply its fixed-q inner liminf.

## Finite controls

Run `python -B research/killed-green-head-closure-20261124/escape-analysis/controls.py` from the repository root. The ordinary interpreter and `python -O -B` both reproduced the stored bytes. Each guard raises explicitly and remains active in optimized mode. [The stored result](CONTROLS.json) records 6,760 positive two-gap cases, the three sharp-cutoff controls through K=3, and 480 comparisons of inverse enumeration with independent direct forward enumeration. A further 40,336 distinct row/class/source triples were replayed from source to the specified terminal on four exact rows, for the finite climbing prefixes of q₀=2^511−1. The largest row had b=224, clock 448 and 36,864 sources split over all 18 unit classes modulo 27. These examples check the carry threshold, source class, split positions and total clock. They assert only the finite initial climb of this ordinary q₀.
