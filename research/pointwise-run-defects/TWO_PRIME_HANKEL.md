# A two-prime obstruction for polynomial-length substitution stages

**PROPOSED.** Let a positive rational 2-adic integer follow the ordinary shortcut map T. Consider any word consisting, after a finite prefix, of the successive stages indexed by n=0,1,…,

    W₁^(a₁n+b₁) G₁ W₂^(a₂n+b₂) G₂ … W_h^(a_h n+b_h) G_h,              (1)

where the W_i are fixed nonempty binary words, G_i fixed possibly empty words, a_i≥1 and b_i≥0 integers. For h≤2 the rational orbit is eventually periodic. This permits distinct changing slopes and distinct gaps in each stage. For larger fixed h the same conclusion holds whenever the constants below satisfy (3). No morphic structure has been established for general escaping orbits. The existing [quadratic morphic reduction](../two-prime-growing-blocks/QUADRATIC_MORPHIC.md) already covers every one- and two-run template and gives a threshold for arbitrary fixed h, including signed rational sources. The improvement here is a lower threshold for the positive-source exclusion when h≥3.

Put L=Σ a_i |W_i| and p=Σ a_i (#ones in W_i). If p log 3<L log 2, an aperiodic positive rational orbit is excluded by the elementary drift argument in the appendix below. Equality is impossible. In the remaining case set

    q=P/D=3^p/2^L>1,       C_h=(2h+1)/(6h²),       D_h=(2h+3)/(6(h+1)²).

The condition for the many-stage result is

    (2/3)log(P/D) < C_h log D + D_h log P.                              (3)

At h=2 this reads P^116<D^189, automatic because p≤L and 3^116<2^189. Both constants are larger at h=1. The same proof allows h in (3) to be replaced by the number of nonzero distinct exponentials in (4) below when that number is smaller.

The determinant method has established q-series precedents. In particular the one-exponential constants 1/2 for the convergent tail and 5/24 for the forward recurrence occur for the Tschakaloff specialization of Krattenthaler, Rochev, Väänänen and Zudilin. Here the two suppression estimates are imposed at different finite primes for a rational stage orbit and are stated for an exponential-polynomial inhomogeneity. [Prior Hankel determinant and difference-operator estimates, Propositions 2 and 3](https://arxiv.org/abs/0812.2921)

## Earlier threshold and a newly covered schedule

Write ρ=log D/log P. The existing [two-prime determinant bound](../two-prime-growing-blocks/PROOF.md) uses the same C_h and the forward constant (2h−1)/(6h²), building on [Paper 46](https://rstation.ai/problems/collatz/papers/46/v1). The D_h above improves that constant by exactly 1/[6h²(h+1)²]. Consequently the sufficient threshold for ρ drops from (4h²−2h+1)/(4h²+2h+1) to (2/3−D_h)/(2/3+C_h). For h=3 the thresholds are 31/43 and 495/688, respectively.

For example use the three successive words consisting of 55 ones, then the word 10, then a one followed by seven zeros, each raised to n at stage n. Their fixed points are −1, 1 and 1/253, so all three centered forcing coefficients survive. Their suffix modes have distinct dyadic valuations. Here D=2^65 and P=3^57. The exact integer comparisons 2^(65·688)>3^(57·495) and 2^(65·43)<3^(57·31) place this template strictly between the two thresholds.

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

## Appendix. An alternative one-stage Padé proof

The following is an independent derivation for the previously covered one-stage family. The rational approximation estimates are adapted from [Zudilin’s real-place proof](https://arxiv.org/abs/math/0506086). In this appendix the stage is W^(An+B) V with fixed W,V, A≥1 and B≥0.

## Place-specific irrationality lemma

Let q=P/D>1 in lowest terms, with D a positive power of 2 and P odd. If P^13<D^21, then for every nonzero rational z the 2-adic value

    T_q(z)=Σ_(k≥0) z^k q^(−k(k−1)/2)                                   (2)

is irrational. The terms converge since |q|₂=D>1. We reproduce the rational approximation estimates, in particular their orientations, as the archimedean value need not equal the hypothetical rational 2-adic value.

Put m=⌊n/2⌋ and R(T)=∏_(i=1)^n(1−q^i T)=Σ C_k T^k. Its coefficients are integer polynomials in q of degree at most n(n+1)/2, more precisely degree at most kn−k(k−1)/2 for C_k. At either convergent place form

    I_n=Σ_(t≥1) R(q^(−t)) z^(t+m) q^(−(t+m)(t+m−1)/2).

Expanding C_k and substituting l=k+t+m writes I_n=B'_n T_q(z)−A'_n with

    B'_n=Σ_(k=0)^n z^(−k) C_k q^(k(k−1)/2+km),
    A'_n=Σ_(k=0)^n Σ_(l=0)^(k+m) z^(l−k) C_k q^(k(k−1)/2+km−l(l−1)/2).

Write z=z₁/z₂ in lowest terms. The common factor

    H_n=z₁^n z₂^m P^(m(m−1)/2) D^(n(n+m))

clears both denominators, since the minimum q exponent in A'_n is −m(m−1)/2, the maximum total degree is ≤n(n+m), and −n≤l−k≤m. Suppose the 2-adic value equals a rational α of denominator h>0. Then M_n=h H_n(B'_n α−A'_n) is an ordinary integer. For t≤n the terms of I_n vanish. At 2 every R(q^(−t)) for t>n has norm one; the t=n+1 term has strictly larger norm than all its successors once n is large. Consequently M_n≠0 and

    log |M_n|₂ ≤ −[n(n+m)+(n+m)(n+m+1)/2] log D + O_z,h(n).

At infinity |B'_n|≤exp(O_z(n)) q^(n(n+m)): use the coefficient degree bound and the at most 2^n unsigned monomials. Also |A'_n| satisfies the same estimate, since Σ_(l≥0)|z|^l q^(−l(l−1)/2) is finite. It follows for the same rational α, without any identification of the real and 2-adic series, that

    log |M_n|∞ ≤ [m(m−1)/2+n(n+m)] log P + O_(q,z,α)(n).

The logarithm of |M_n|∞ |M_n|₂ is therefore at most n²(13 log P−21 log D)/8+O(n). This is negative for large n, contradicting |M_n|∞ |M_n|₂≥1 for a nonzero ordinary integer. The estimates directly adapt [Zudilin, equations (3)–(10)](https://arxiv.org/abs/math/0506086).

## Application to a growing repeated block

Let ξ be the unique rational affine fixed point of W, let λ=3^p/2^v be its slope (v the width, p its odd count), and let μ>0 be the rational slope of V. The point ξ is 2-adically integral. Write d=V(ξ)−ξ for the uncentered affine value of V at ξ minus ξ. With x_j the starting state of the jth W-block and z_j=x_j−ξ, the exact equations are

    z_(j+1)=μ λ^(Aj+B) z_j + d.

When d=0, V is legally followed at ξ (its image is 2-adically integral) and returns to ξ. Each W also returns to ξ. The infinite parity tail (1) is therefore that of ξ; uniqueness of a 2-adic source for an infinite parity sequence gives x₀=ξ. Uniqueness follows directly from the parity-word bijection modulo every 2^L.

Suppose d≠0 and λ>1. Dividing through by the successive products in the recurrence gives, in the 2-adics,

    z₀=−d μ^(−1) λ^(−B) T_(λ^A)(μ^(−1) λ^(−A−B)).

Indeed the remainder tends to zero because all z_j are 2-adically integral and |λ|₂>1. The lemma applies: P=3^(pA), D=2^(vA), with P>D and P^13<D^21 since p≤v and 3^13=1594323<2097152=2^21. Thus z₀ cannot be rational.

It remains to consider λ<1 for positive rational input of odd denominator. The odd-input frequency along (1) is p/v, also along partial stages since each stage has length O(j) versus total length of order j². The denominator of every positive shortcut state divides the fixed initial odd denominator D₀. On a nonperiodic orbit the first N states are distinct, giving a reciprocal sum at most D₀ Σ_(i≤N)1/i=O_(D₀)(log N) by discreteness. The exact logarithmic product for T yields

    log T^N(x₀)/N → (p/v) log 3−log 2<0,

contradicting T^N(x₀)≥1/D₀. The possibility λ=1 never occurs for a nonempty word. Finite prepending or deletion preserves the rational-source exclusion by the rational affine word map.

Finally, eventually quadratic even positions have eventually positive, affine gaps between successive even letters; hence their suffix is (1) with W the odd letter and V the even letter. Equivalently the 2-adic identity −(x+1)=Σ_(j≥0)3^j(2/3)^(d_j) over even positions d_j is obtained by iterating the two affine maps on x+1. A quadratic d_j reduces that sum directly to (2).

## Cyclotomic factors away from 2 and 3

The stronger sufficient condition is

    (2/3)log(P/D) < C_h log D + (D_h+Γ_h)log P,
    Γ_h=π^(−2) Σ_(m≥1) [((h+2)m−1)^(−2)+((h+2)m)^(−2)].

For h=3 this lowers the sufficient ρ to approximately 0.69940. For example use W₁=W₂=1111, W₃=10, with an intervening fixed single even step G₁=0 and empty other gaps. All exponents are n. The cyclic pins are −1,−1,1; the single fixed step takes the first pin to −1/2, giving three nonzero centered gap constants 1/2,−2,2. Here P=3^9,D=2^10. This lies above the new threshold and below 495/688: π²<10 and the first ten terms of Γ₃ put the new threshold below 701/1000, while 2^10000>3^6309 and 2^(10·688)<3^(9·495) check the two required comparisons exactly.

The antecedent is [Krattenthaler, Rochev, Väänänen and Zudilin, Proposition 4 and Lemma 3](https://arxiv.org/abs/0812.2921), where the one-forcing-term multiplicity is exactly the h=1 bound below. We include the extension and place accounting because the old Collatz-specific two-prime bound uses only places 2 and 3.

Temporarily replace q in (4) by an indeterminate T, keeping u, the c_l,v_l and z₀ fixed. Then every z_n(T) for n≥0 is a polynomial. Treat the parameters as independent indeterminates first, with h distinct forcing modes. For a primitive dth root ζ, put T=ζ exp(w). Write z_(md+b)(T) in powers of w for residues 0≤b<d. The d-step recurrence at w=0 has homogeneous multiplier A=u^d ζ^(d(d−1)/2), independent of b. For each k≥0 the coefficient of w^k on each residue class is the sum of:

* A^m times a polynomial in m of degree at most 2k;
* (v_l^d)^m times polynomials in m of degree at most k, for 1≤l≤h.

Indeed the d-step homogeneous multiplier is A exp((d(md+b)+d(d−1)/2)w). Its w^j coefficient has degree at most j in m. The d-step inhomogeneous terms are v_l^(md+b) times a finite sum of exponentials exp((a m+b')w) with fixed coefficients depending on the residue, hence have the same degree-j bound. Induct on k. Solving the resulting recurrence with homogeneous multiplier A raises polynomial degree by one in the A-mode and keeps it in each other mode, since A differs generically from all v_l^d. For j≥1 the propagated A-mode degree is at most j+2(k−j)≤2k−1 before solving. The arbitrary homogeneous initial term is constant times A^m. This proves the claim including k=0.

Let E be forward shift. At each l-independent derivative order below t, the preceding bounds show that the monic operator

    B_t=(E^d−A)^(2t−1) ∏_l(E^d−v_l^d)^t,        t≥1,

kills the coefficient sequence. Thus B_t z_n(T) vanishes to order at least t at ζ; the same holds for the operator with one extra homogeneous factor. Use the identity for t=0. Set M=h+2. For row i use B_f with f=floor((i+d)/(Md)); for column j use the extra-factor operator of index g=floor(j/(Md)), interpreting any index-zero operator as the identity. These are unit triangular transformations: for the degree-b monic operator attached to row i take its combination of original rows starting at i−b, and do the same for columns. The row and column operators commute and their product is B_(f+g) or its extra-factor version when f+g>0. Every transformed entry therefore vanishes to order at least f+g. Explicitly the determinant polynomial is divisible by

    ∏_(d≥1) Φ_d(T)^e(k,d),
    e(k,d)=Σ_(i=0)^(k−1) [floor((i+d)/(Md))+floor(i/(Md))].

The identity first holds over the generic parameter field. Since the divisor is monic with integer coefficients, polynomial division commutes with specializing all the parameters, including resonance or cancellation. In the orbit application u,v_l have only powers of 2 and 3 in their denominators; after the original common scaling of z_n, enlarge by another fixed integer if necessary so z₀,c_l have no other denominator. All polynomial coefficients and the quotient then belong to the integers localized at 6. At T=P/D the homogeneous integer values Φ_d(P,D)=D^φ(d)Φ_d(P/D) are all coprime with 6, by the constant and highest coefficients of Φ_d and coprimality of P,D. Accordingly their full product to the indicated powers divides H_k away from 2 and 3. The factors need not be mutually coprime, since the full product was obtained before specialization.

For completeness, log|Φ_d(P,D)|=φ(d)log P+O_q(1), uniformly by Möbius inversion of P^d−D^d and convergence of Σ_(j≥1)|log(1−(D/P)^j)|. Also Σ_d e(k,d)=O(k²log k). Expanding both floors as counts gives the sum of φ(d)e(k,d) as the sum, over t=Mm−1 and t=Mm for m≥1, of Σ_(d<k/t)φ(d)(k−td). For each fixed t, the totient asymptotic Σ_(d≤x)φ(d)∼3x²/π² and partial summation give k³/(π²t²)+o(k³). The trivial φ(d)≤d bounds each contribution by O(k³/t²), allowing dominated convergence. Thus the logarithm of the certified integer divisor is Γ_h k³ log P+o(k³), independent of the two previous prime bounds. Adding all three savings to (5) proves the strengthened criterion.
