# A two-prime obstruction for polynomial-length substitution stages

**PROPOSED.** Let a positive rational 2-adic integer follow the ordinary shortcut map T. Consider any word consisting, after a finite prefix, of the successive stages indexed by n=0,1,…,

    W₁^(a₁n+b₁) G₁ W₂^(a₂n+b₂) G₂ … W_h^(a_h n+b_h) G_h,              (1)

where the W_i are fixed nonempty binary words, G_i fixed possibly empty words, a_i≥1 and b_i≥0 integers. For h≤2 the rational orbit is eventually periodic. This permits distinct changing slopes and distinct gaps in each stage. For larger fixed h the same conclusion holds whenever the constants below satisfy (3). No morphic structure has been established for general escaping orbits. Prior exponential-growth substitution theorems explicitly set aside polynomial-growth presentations such as (1). [Paper 69, scope](https://rstation.ai/problems/collatz/papers/69/v1)

Put L=Σ a_i |W_i| and p=Σ a_i (#ones in W_i). If p log 3<L log 2, an aperiodic positive rational orbit is excluded by the elementary drift argument in [the one-stage result](QUADRATIC_INTERRUPTS.md). Equality is impossible. In the remaining case set

    q=P/D=3^p/2^L>1,       C_h=(2h+1)/(6h²),       D_h=(2h+3)/(6(h+1)²).

The condition for the many-stage result is

    (2/3)log(P/D) < C_h log D + D_h log P.                              (3)

At h=2 this reads P^116<D^189, automatic because p≤L and 3^116<2^189. Both constants are larger at h=1. The same proof allows h in (3) to be replaced by the number of nonzero distinct exponentials in (4) below when that number is smaller.

The determinant method has established q-series precedents. In particular the one-exponential constants 1/2 for the convergent tail and 5/24 for the forward recurrence occur for the Tschakaloff specialization of Krattenthaler, Rochev, Väänänen and Zudilin. Here the two suppression estimates are imposed at different finite primes for a rational stage orbit and are stated for an exponential-polynomial inhomogeneity. [Prior Hankel determinant and difference-operator estimates, Propositions 2 and 3](https://arxiv.org/abs/0812.2921)

## The scalar stage recurrence

Let ξ_i be the affine fixed point of W_i, λ_i its slope, and γ_i the slope of G_i. The ξ_i have fixed odd denominators and are 2-adically integral. Center at ξ_i before each power. Passing through the power and the following gap takes the centered value z to γ_i λ_i^(a_i n+b_i) z + (G_i(ξ_i)−ξ_(i+1)), with cyclic subscripts. Composing the h transitions gives the centered stage-start sequence

    z_(n+1)=u q^n z_n + Σ_(l=1)^s c_l v_l^n,                    s≤h,   (4)

with fixed rationals, u,v_l positive. Each v_l is a product of the suffix slopes λ_i^a_i. Combine equal exponentials and delete zero coefficients. The empty sum forces z₀=0 by bounded 2-adic norm in (4); this gives an actual return to ξ₁. Otherwise use h as an upper bound for s (or set h=s). The ordinary rational states have uniformly bounded reduced denominators dividing the source's fixed odd denominator, since taking the correct branch preserves this property. The centered z_n likewise have a common fixed denominator. Multiply (4) by that denominator and absorb it into the c_l so all z_n are integers for n≥0.

The ordinary uncentered real affine maps have nonnegative offsets and positive slopes. Thus the original positive starting state, times u^n q^(n(n−1)/2), lower bounds its nth ordinary stage state. In the other direction each additive term in (4) is at most exponential in n. Variation of constants gives

    log |z_n| = (n²/2)log q + O(n+1)                        for large n.

In particular the rational sequence has no constant-coefficient linear recurrence. Its k-by-k principal Hankel determinant H_k=det(z_(i+j))_(0≤i,j<k) is an integer. From the permutation formula, monotone rearrangement of Σ iπ(i), and Σ i²=k³/3+O(k²),

    log |H_k|∞ ≤ (2/3)k³ log q + O(k²+k log k)                when H_k≠0. (5)

## At 2: the inverse expansion

Solving (4) backwards from the 2-adically bounded nonnegative-index sequence gives, for every n≥0,

    z_n=Σ_(l,t≥1) b_(l,t) α_(l,t)^n,
    α_(l,t)=v_l q^(−t),    b_(l,t)=−c_l v_l^(t−1) u^(−t) q^(−t(t−1)/2).

Here l ranges up to s. The remainder vanishes, and the series converges even at n=0. In the normalization w(x)=−log|x|₂/log D, one has w(α_(l,t))≥t−O(1) and w(b_(l,t))≥t²/2−O(t+1). For any finite cutoff on t factor the truncated Hankel matrix as a Vandermonde matrix, a diagonal matrix of the b's, and the transpose Vandermonde matrix. The Cauchy–Binet expansion gives products of k weights times squares of pairwise differences of the α's. Sort each selected k-tuple by its t_i, indexed i=1,…,k. Then t_i≥ceil(i/h). Each difference with a later entry has valuation ≥t_i−O(1). Consequently every summand has valuation at least

    Σ_i [t_i²/2+2(k−i)t_i−O(t_i+1)] − O(k²)
       ≥ C_h k³−O(k²).

For the last inequality replace t_i by i/h in the quadratic-minus-linear bound, after completing a square for the finitely small i. Shared poles or zero terms only increase the valuation. The estimate is uniform in the truncation, hence survives the 2-adic limit. Thus log |H_k|₂≤−C_h k³ log D+O(k²).

## At 3: the forward differences

Write w(x)=−log|x|₃/log P, so w(q)=1. Extend the rational recurrence (4) to negative indices by algebraic inversion. It is important that

    w(z_n)≥−O(1+|n|)                   for all integral n.

For n≥0 this follows from integrality. For n=−r<0 use z_(−r)=u^(−1)q^r [z_(1−r)−Σ c_l v_l^(−r)] and induct, choosing a linear lower bound that dominates all the finitely many valuations of the v_l. The positive r in the valuation of q^r absorbs the fixed u cost at large r.

Let N denote backward shift in the sequence index. For r≥0 define

    A_r(N)=∏_(t=0)^(r−1) ∏_(l=1)^s (1−v_l q^t N).

Iterating (4) forward r times expresses z_k as a sum of constant multiples of (v_l q^t)^k, t<r, plus the exact remainder u^r q^(rk−r(r+1)/2) z_(k−r). This holds even for negative intermediate indices. The operator A_r kills every indicated exponential. Its coefficient at N^d has valuation at least d²/(2h)−O(d+1), since selecting d factors from levels t=0,1,… with at most h per level has sum ≥d²/(2h)−O(d). Therefore for i,j<k, starting index i+j and any r≤i/h,

    w(A_r z_(i+j)) ≥ r(i+j)−(h+1)r²/2−O(k+1).

Indeed for the shifted remainder at i+j−d add d²/(2h)−rd≥−h r²/2. The negative-index linear bound absorbs all remaining terms in O(k+1).

For matrix size k choose r_i=min(floor(i/h),floor((k−1)/(h+1))). Apply A_(r_i) to row i using the preceding rows, proceeding in descending order of i. Its constant coefficient is one and its degree is at most i, so H_k is unchanged. For any determinant permutation the sum of valuations is bounded below by

    Σ_i [r_i(k−1)−(h+1)r_i²/2]−O(k²) = D_h k³−O(k²).

Here r_i is nondecreasing, so the reverse permutation gives the least possible Σ r_i π(i). To evaluate the leading coefficient integrate R−(h+1)R²/2 on [0,1] with R=min(x/h,1/(h+1)). This proves log |H_k|₃≤−D_h k³ log P+O(k²).

## Contradiction and scope

Under (3), (5) and the two finite-place estimates imply |H_k|∞ |H_k|₂ |H_k|₃<1 for every sufficiently large k with H_k≠0. A nonzero integer cannot have this product; hence all sufficiently large principal Hankel determinants vanish. For completeness, choose the last r with H_r≠0, allowing H₀=1. Solve for the order-r monic linear recurrence matching the first r rows. If its residual sequence first has a nonzero entry at index j≥r, subtract that recurrence from columns r through j of H_(j+1), from right to left. The new upper right block vanishes, and the lower right block has first nonzero anti-diagonal equal to that residual entry. Its determinant is nonzero, contrary to the maximality of r. The recurrence must extend forever, contradicting the superexponential real growth. This proves the stated ordinary rational exclusion.
