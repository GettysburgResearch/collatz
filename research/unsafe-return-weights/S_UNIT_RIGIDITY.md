# Every linear clock window at large moving index has only aligned repayments

**Status: PROPOSED application of a published S-unit gcd theorem.** Fix C>0. For all sufficiently large moving indices a, and all sources meeting the high-precision condition below, every cheaper merger with both clocks at most Ca is the endpoint of a positive number of ordinary, aligned 1^a0 blocks from the source. This holds even when the proposed witness uses two different physical words and clocks. It rules out *every* such short merger at a genuinely unsafe source. The phrase “sufficiently large” depends on C; no effective cutoff is supplied by this application.

## An arithmetic relation lattice with an escaping second direction

For a>=3 put d_a=3^a−2^{a+1}. Define

    Lambda_a = {(j,k) in Z² : 2^j 3^k = 1 mod d_a}.

The signed exponents are well-defined since d_a is coprime to six. The vector r_a=(−a−1,a) always lies in this lattice. For every fixed C>0 there is a_0(C) such that

    Lambda_a intersect [-Ca,Ca]² is contained in Z r_a    for a>=a_0(C).  (1)

Equivalently, the smallest sup norm of an independent second direction, divided by a, tends to infinity.

**External input and normalization.** Corvaja and Zannier, *A lower bound for the height of a rational function at S-unit points*, arXiv:math/0311030v2, Corollary 1, equation (1.3), states the following for a fixed finitely generated subgroup of the rational two-dimensional torus. For every epsilon>0, apart from finitely many multiplicatively independent pairs u,v in that group,

    sum_w log^- max(|u−1|_w,|v−1|_w) > −epsilon max(h(u),h(v)),

with log^- x=min(0,log x), |p|_p=p^{-1}, and rational height h(r/s)=log max(|r|,|s|) in reduced form. The sum includes all rational places. This use needs the version for independently varying rational S-units, including negative exponents. The estimate restricted to (2^N−1,3^N−1) with a single exponent N does not give (1). The [original preprint](https://arxiv.org/abs/math/0311030v2) was consulted at the displayed equation; this packet does not reprove its Subspace Theorem input.

**Proof of (1).** Apply the bound in the fixed group generated independently in each coordinate by 2 and 3, with

    u=3^a/2^{a+1},      v=2^j3^k.

The numerator of u−1 in lowest terms is d_a. At every p^e exactly dividing d_a, the congruence for v gives |v−1|_p<=p^{-e}, and |u−1|_p=p^{-e}. These places alone sum to −log d_a. All other terms are nonpositive. In the displayed window both heights are at most B_C a for all a>=3, for example B_C=2 log 3+C log 6. Also log d_a/a tends to log 3. Choosing epsilon=log(3)/(4 B_C) makes the external inequality impossible for a multiplicatively independent pair once a is large, apart from its finite exceptional set. Distinct a give distinct u, so the exceptions contribute only finitely many indices for this fixed C.

Thus u and v are multiplicatively dependent. Since 2 and 3 are independent generators of the positive rational S-units, the exponent vector (j,k) is rationally collinear with (−a−1,a). That latter integer vector is primitive, so (j,k) is an *integer* multiple, including zero. This proves (1).

## Consequence for every positive witness and both clocks

Use the [two-arm theorem](SHORT_MERGERS.md) and its [denominator refinement](OPTIMAL_CLOCKS.md). Suppose a minimizes R(n), a>=3, H=v3(z_a(n)), and both merger clocks t,s are at most M with

    3^H > 1000 d_a³ 27^M,             M <= Ca.              (2)

At all sufficiently large a, every physically legal lower-rank diagram in this range satisfies

    m = g_a^l(n),       l>=1,       (1^a0)^l legal at n,

where g_a is the affine map of the word 1^a0. Conversely any such physical aligned block strictly lowers the rank, whether (2) holds or not, since a minimized the source rank.

Indeed the companion must minimize in the same component a, and m−alpha_a=v(n−alpha_a) with v=2^{s-t}3^{q_v-q_w}; here q_v,q_w count the odd letters on the two arms. The common-root equation forces v=1 modulo d_a. Its exponent vector has sup norm at most M. By (1), v=(3^a/2^{a+1})^l for some integer l. The ratio of the two component ranks is exactly (3^a/4^{a+1})^l, requiring l>0. The affine center identifies m=g_a^l(n). Its ordinary integrality forces 2^{(a+1)l} to divide z_a(n), by multiplying the equality z_a(m)=(3^a/2^{a+1})^l z_a(n). The parity-cylinder criterion T-A3-901 gives exactly the displayed physical prefix. Its length is (a+1)l=t−s<=M from the first exponent coordinate. Thus the alternative two-arm certificate supplies a direct forward repayment within the same clock budget.

This dichotomy remains informative when C is an arbitrarily large *fixed* constant. For a sequence of unsafe sources n_i of minimizing indices a_i tending to infinity with H_i/a_i tending to infinity, condition (2) holds eventually at M=floor(C a_i) for every C. An unsafe source cannot start with an aligned module at a minimizing index. Consequently

    ell(n_i)/a_i -> infinity,

where ell is the least maximum arm length and may in general be infinite. This is a lower bound on computational or physical resources, with no assertion of divergence of an orbit.

For explicit terminating examples with finite ell take a>=5, H=a²+10, and impose z_a(n)=3^H modulo 3^{H+1}. As in the [exact-clock construction](OPTIMAL_CLOCKS.md), a uniquely minimizes for large n in that class. Impose instead the short physical prefix 100, and complete it by a final halving run to 1 using the [unit-target construction](TERMINATING_TOWERS.md). The first maximal module has word 10 because the next state is even. By the forward precision theorem its endpoint increases rank, so the initial odd unit belongs to the genuine re-entry support. Every one of these sources converges and hence has some finite lower witness, while the ratio ell/a along these examples tends to infinity. This construction chooses new ordinary sources as a grows.

## General binomial form

The same gcd argument applies to pairs u_i=3^{q_i}/2^{t_i} with d_i any common-modulus divisors of the numerator |3^{q_i}−2^{t_i}|. If max(q_i,t_i) tends to infinity, log d_i is at least a fixed positive multiple of that maximum, and 2^{j_i}3^{k_i}=1 mod d_i with |j_i|+|k_i| bounded by a fixed multiple of it, all sufficiently late exponent pairs are collinear with (−t_i,q_i). For nonprimitive (−t_i,q_i) this gives multiples of its *primitive reduction*. The exponential lower bound concerns the divisor actually retained: true integer cycle roots can cancel the full denominator and are not excluded by this result.

The [bounded lattice replay](check_lattice.py) includes exceptional *independent* small-index relations as adversarial controls as well as aligned and signed ones. They illustrate the need for the asymptotic quantifier without locating any universal cutoff.
