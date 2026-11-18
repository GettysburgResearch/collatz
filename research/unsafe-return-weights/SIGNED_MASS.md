# A signed harmonic sum measures the total mass of escaping components

**PROPOSED, source-qualified.** Let U(x) be the odd part of 3x+1 on positive odd integers. Write g_q=L^q1 for the finite ternary cylinder density, normalized to mean one, δ=log(4/3)/2 and g=lim g_q=(3/2)h on ordinary integers. For every q≥0, the series in increasing odd positive order converges and satisfies

    S_q := Σ_(t odd) (g_(q+1)(t)−g_q(t))/t
          = δ − Σ_(x odd) g_q(x)/[x(3x+1)].                            (1)

The finite-depth densities are periodic modulo 3^q and computable by a finite quotient recurrence. The series on the right is absolutely convergent and has explicit effective finite-depth tails. There is no first-return correction in this observable.

For each escaping odd component C write H_C=lim h(y_j)/y_j along one of its forward spines. Then

    lim S_q = Σ_(escaping C) (3/2) H_C ≥ 0.                             (2)

In particular, eventual periodicity of every positive orbit is equivalent to liminf S_q≤0, or equivalently to the single scalar identity

    Σ_(x odd) h(x)/[x(3x+1)] = log(4/3)/3.                              (3)

The right side in (2) sums all the escaping masses, whereas the [first-hit maximum](INVERSE_AGE_LAWS.md) selects the largest single profile jump. Neither test has established that this mass is zero. The criterion permits positive cycles besides the trivial one.

## Fixed-depth identity

Put a(x)=v₂(3x+1) and J_x=3/2^a(x), so U(x)=J_x(x+1/3). The two periodic densities in the left series of (1) have identical mean over odd integers, hence their difference has bounded partial sums and the increasing-order sum converges. Insert a factor t^-s, s>0, and let s decrease to zero. Absolute convergence at s>0 permits the change of variables t=U(x), with precursors weighted by J_x. The result splits into

    Σ_x g_q(x)[(x+1/3)^(-1-s)−x^(-1-s)]
       + Σ_(a≥1) ((2^a/3)^s−1) Z_a(s),

where Z_a(s) sums g_q(x)(x+1/3)^(-1-s) at a(x)=a. The first term tends to the negative correction series in (1) by domination, since g_q≤2^q. The Chinese remainder theorem gives lim_(s↓0) s Z_a(s)=2^(-a-1): a(x)=a selects one odd class modulo 2^(a+1), independent of g_q modulo 3^q. For taking the limit in the a-sum, every such x has x+1/3≥2^a/3, and consecutive such x differ by 2^(a+1). Comparison to the first term plus a decreasing integral shows s Z_a(s)≤C_q 2^(-a(1+s)) for 0<s≤1/2. The difference quotient for the exponential is bounded by C(a+1)max(1,(2^a/3)^s), making the product summable. Thus the limiting second term is Σ_(a≥1)2^(-a-1)(a log 2−log 3)=δ. Abel summation recovers the convergent left series.

## All depths and the ordinary distortion budget

For an odd source n let V_i(n)=∏_(0≤j<i)(1+1/(3U^j n))^(-1), with V_0=1. Let W_x(n) be V_i at its first visit to x, or zero when x is never visited. Let B_x be one off cycles and 1/(1−J_C) on a cycle C of multiplier J_C. A visit to x expends V_i/(3x+1)=V_i−V_(i+1). Repeated visits sum geometrically, giving a nonnegative identity for each n:

    Σ_(x odd) W_x(n) B_x/(3x+1) = 1−V_∞(n).                            (4)

On cyclic basins V_∞=0. On escaping components V_∞ is the reciprocal of the whole simple-orbit correction product, bounded between a fixed c>0 and 1.

Denote normalized odd logarithmic mean by E. The [prior canonical trace and component formula](https://doi.org/10.5281/zenodo.23025885) gives g(x)=δ B_x x E W_x, including ternary nonunits whose basin has zero density; it also gives E(V_∞ 1_C)=(3/2)H_C/δ. For the fixed-target step from Cesàro to ordinary depth use [every-depth convergence](https://github.com/GettysburgResearch/collatz/blob/27cd7ced4381a0d49470683c9cb492d23d207576/research/native-pressure-20261118/EVERY-DEPTH.md). Fatou's finite-sum argument in (4) gives Σ_x g(x)/[x(3x+1)]≤δ. The prior uniform domination g_q≤C g on odd units for q≥1 and vanishing on nonunits now allow dominated convergence in the correction series in (1). [Finite-level domination, Corollary 7](https://rstation.ai/problems/collatz/papers/12/v1)

To interchange E with the sum in (4), fix R and take M above all cycle vertices on the trajectories of the finitely many odd starts ≤R that eventually cycle. On every escaping path and every preperiodic simple prefix, vertices x>M expend at most C M^(-c) by the uniform simple-segment reciprocal tail. After the first cycle vertex the total remaining expenditure is at most one. If this cycle is not on the finite list, any trajectory in its basin has global minimum >R. Thus the expected loss from discarding x>M is at most C M^(-c)+Pr(m>R), which tends to zero by taking M then R to infinity. The same finite-root localization also permits summing E(V_∞ 1_C) over escaping components: outside components of the starts ≤R the mass is at most Pr(m>R). The canonical result gives existence of those individual means and Pr(m>R)→0. This proves (2) and (3). The simple-segment tail, global-minimum tightness and component formula are all available in the cited canonical trace paper.

For a numerical truncation one can sum x≤2k·3^q at any k≥1. In each subsequent odd block of length 2·3^q the density sums to 3^q by periodicity and normalization, so the positive remaining sum is ≤(1+1/k)/(12 k 3^q). This is only a spatial truncation bound at fixed q. The unresolved bound is on the limiting depth.

There is also a Cesàro version that does not require the new every-depth theorem. Put A_q=Σ_(t odd)(g_q(t)−1)/t in increasing order. Summing (1) over q telescopes to A_Q, since g_0=1. Prior pointwise Cesàro convergence and the same domination in the positive correction series prove

    A_Q/Q → Σ_(escaping C) (3/2)H_C.

Thus a sublinear upper bound on A_Q even along one subsequence would rule out escape. In a complete odd period the density has total mass 3^Q. Grouping all periods after the first in pairs of summands g_Q−1 against the varying reciprocal shows that replacing A_Q by its sum on t≤2·3^Q costs O(1) absolutely, independently of Q: on period number k≥1 subtract the constant 1/(2k·3^Q), use total absolute mass ≤2·3^Q and reciprocal oscillation ≤1/(2·3^Q·k(k+1)), then sum. Equivalently the ordinary finite certificate needed is

    liminf_(Q→∞) [1/Q · Σ_(1≤t≤2·3^Q, t odd) g_Q(t)/t] ≤ (log 3)/2.   (5)

For comparison the [directed integer replay](check_signed_mass.py) brackets S_q at depths 0 through 14. At q=0 it lies between −0.178797 and −0.178796, at q=12 between −0.008626 and −0.008625, at q=13 between 0.000668 and 0.000669, and at q=14 between 0.007317 and 0.007318. Thus the sign can change before the limit. Bounds use the positive tail above, directed dyadic quotient enclosures and the positive Taylor series atanh(1/7)=δ. None determines (5).
