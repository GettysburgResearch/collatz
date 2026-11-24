# Polynomial-phase rigidity by a dilation–inverse-Weyl argument

**PROPOSED written proof.** Source-qualified PR146's ordinary tripling-defect and adjacent-variation estimates are used, as in PR200 MACROSCOPIC_RIGIDITY.md. The new analytic input is the classical quantitative inverse Weyl estimate in Green–Tao, *The quantitative behaviour of polynomial orbits on nilmanifolds*, Annals of Math. 175 (2012), Proposition 4.3 (the torus case). We do not import a general nilsequence inverse theorem. Full Collatz remains open.

Let f:N+ -> [0,1] be a binary invariant ordinary color, f(Tn)=f(n). Let c_X be its ordinary average through integer X. More generally, the conclusion uses only the shell adjacent variation, approximate irrational rotation and primitive discrepancy estimates stated below. For each fixed d>=1, the new estimate is

    sup_(real polynomials P of degree <=d)
      |(1/X) sum_(n<=X) (f(n)-c_X) exp(2*pi*i*P(n))|
      = O_d( (log log X)^(-1/2) ).                   (PW)

Polynomial coefficients may vary arbitrarily with X. Constants also depend on the pinned Collatz estimates and the fixed Diophantine exponent. This is a quantitative extension beyond the preceding linear Fourier result; the weaker rate is not intended to improve that result at degree one.

## 1. Shell reductions

For R large put t=log_2(x/R) on [R,2R), theta=log_2 3 modulo 1, and g_R(t)=f(floor(R 2^t)), extended periodically. Write a_R=integral g_R. The preceding checkpoint proves from PR146, uniformly in R,

    ||g_R(t+theta)-g_R(t)||_1 <= C epsilon_R,
    ||g_(2R)-g_R||_1 <= C epsilon_R,
    epsilon_R=(log R)^(-1/2),
    number of adjacent changes in [R,2R] <= C R epsilon_R.

The same checkpoint proves for some absolute a>0 (from the irrationality exponent of theta) that all subinterval sums of f-a_R on [R,2R) are O(R delta_R), delta_R=(log R)^(-a). These results, including the integer rounding, are imported at the exact head 39918be724038ac550d77c7fc95d17e05251dfc6. They require no assumption of independence of labels.

Write e(z)=exp(2*pi*i*z). Up to O(1/R), the shell sum normalized by R is

    integral_0^1 (g_R(t)-a_R) phi(t) dt,
    phi(t)=(log 2) 2^t e(P(floor(R 2^t))).

The weight comes from the exact real integral over integer cells, so no small-derivative assumption on P is needed in this conversion. Let Q>=2, later a small multiple of log log R. Replace phi by Q^(-1) sum_(i=0)^(Q-1) phi(t+i theta mod1). The resulting error is O(Q epsilon_R) by the approximate rotation identity and boundedness of phi. Cauchy-Schwarz bounds the replaced integral by the L2 norm of the average, since ||g_R-a_R||_2<=1.

If all off-diagonal inner products of the translates are O(1/Q), this norm is O(Q^(-1/2)), with bounded diagonal terms. The difficulty is a potentially resonant pair.

## 2. An inverse lemma for any resonant pair

**Claim.** Suppose an off-diagonal inner product for 0<=i<j<Q has magnitude >1/Q and Q<=c log log R for some fixed c. Then writing P(x)=sum_(l=0)^d alpha_l x^l, there is a common integer q>=1 and rationals r_l/q such that (allow integer parts in the numerators)

    q <= exp(C_d Q),
    |alpha_l-r_l/q| <= exp(C_d Q) R^(-l),  1<=l<=d.  (5)

Proof. On each of at most three intervals cut by the two wrap points, the scaled arguments of the translates are floor(c_i x), floor(c_j x), with x=R 2^t and c_i,c_j distinct positive rationals in [1/2,2]. They are of the form 3^i/2^b and 3^j/2^b' with exponents O(Q); distinctness follows from unique factorization, since i!=j. Let D be a common power-of-two denominator; D<=exp(O(Q)). Put A_i=D c_i, A_j=D c_j (distinct positive integers). The inner product on each interval becomes

    (1/R) integral_I W(x/R) e(P(floor(c_i x))-P(floor(c_j x))) dx,

with W and its derivative bounded absolutely (the weight is a constant times x/R). Discard the two incomplete D-blocks at each interval end, costing O(D/R). On x=Dm+u, 0<=u<D, replace W(x/R) by W(Dm/R) at cost O(D/R). For a fixed u the integer arguments are A_i m+b_i and A_j m+b_j, where b_i=floor(c_i u), b_j=floor(c_j u) have absolute value O(D). By averaging over u and the at most three intervals, there is a piece and a u for which the weighted polynomial exponential sum has absolute size >=c R/(QD). Partial summation removes the slowly varying bounded-variation weight, yielding a partial interval of length L>=c' R/(QD) with an unweighted sum of that size. The normalized correlation is >=c''/Q since L<=2R/D. Its start m0 has |m0|=O(R/D).

Apply the inverse Weyl estimate (Green–Tao Prop. 4.3): if the normalized exponential sum of a degree-d polynomial on [L] is >=eta, there is an integer denominator <=C_d eta^(-C_d) such that each coefficient in the binomial basis is within C_d eta^(-C_d)L^(-l) of a rational with that denominator (up to multiplying the constant by a power of d). To see its applicability to an exponential test, nontrivial mean of e(P) violates equidistribution at a constant times that mean; use real and imaginary parts as fixed Lipschitz torus tests. Conversion to the ordinary monomial basis changes the denominator by at most d! and the coefficient errors by d-dependent constants, since the binomial-to-monomial conversion is fixed triangular. Shift m0 back to the original m coordinate: coefficients of order l pick up higher-order errors multiplied by O_d((1+|m0|)^(s-l)). With L>=cR/(QD), all errors are <=exp(O_d(Q)) R^(-l). Thus every nonconstant coefficient of

    P(A_i m+b_i)-P(A_j m+b_j)

is within exp(O_d(Q)) R^(-l) of a rational with bounded common denominator <=exp(O_d(Q)).

The transformation on nonconstant monomial coefficients is upper triangular, with exact diagonal A_i^l-A_j^l !=0 at l>=1, and every integer entry has absolute value <=exp(O_d(Q)). Solve from degree d down to one. At each step subtract previously approximated higher coefficients and divide by the nonzero integer diagonal; their errors remain <=exp(O_d(Q))R^(-l). Multiplying the finitely many denominators and diagonal factors still costs exp(O_d(Q)). This proves (5). No uniform Weyl bound on a short interval selected after sampling a Collatz orbit is used; these are ordinary arithmetic progressions in a deterministic integral. QED.

## 3. Major arcs and choosing the scale

If (5) holds, write P(x)=P_rat(x)+P_slow(x)+alpha_0 where P_rat has integer numerators over q and P_slow coefficients bounded by H R^(-l), H<=exp(C_d Q). Then e(P_rat(n)) is exactly q-periodic on ordinary integers. On [R,2R], e(P_slow(x)) has derivative O_d(H/R).

Partition the shell into full q-blocks. Except on at most the number of adjacent f changes, f-a_R is constant within each block. Replace the periodic factor by its full-period mean on the good blocks, holding the slowly varying factor fixed at one point of each block. The normalized error is

    O_d(q epsilon_R + qH/R + q/R).

The resulting smooth weighted sum of f-a_R is O_d((1+H)delta_R) by the primitive discrepancy and Abel summation. Thus all major arcs of this complexity are harmless; in particular no new distribution assumption about f on residue classes is needed.

Choose Q=floor(c_d log log R) with c_d>0 sufficiently small depending on d and the fixed constants in (5) and delta_R. Then exp(C_d Q) is at most a sufficiently small power of log R, so all the major-arc errors are O_d((log R)^(-eta_d)) for some eta_d>0. In the alternative where all off-diagonal inner products are <=1/Q, the initial dilation averaging gives O(Q epsilon_R + Q^(-1/2)). This proves the uniform shell bound O_d((log log R)^(-1/2)), in both alternatives. The polynomial itself may depend on R or on an arbitrary larger cutoff.

For the full initial interval [1,X], sum complete dyadic shells down to sqrt X, using the earlier estimate |a_R-c_X|<=C(j epsilon_(sqrt X)+delta_X) at R=X/2^j. It follows from doubling comparison, primitive discrepancy on each shell, and geometric summation. The omitted prefix is O(sqrt X/X). All weighted errors sum to o(1/sqrt(log log X)); the uniform shell bound sums to O_d(1/sqrt(log log X)). This proves (PW).

## 4. Exact scope and possible consumer

The bound applies to every fixed-degree polynomial phase and hence to bounded-l1 linear combinations of them, uniformly in all their coefficients. It also applies to fixed-dimensional torus polynomial observables of fixed bounded Lipschitz norm by approximation with finite trigonometric sums. In particular a trigonometric polynomial-phase predictor with total coefficient l1 norm o(sqrt(log log X)) cannot correlate nontrivially with the centered invariant label.

Conditional on the reported fixed-target positive lower natural predecessor density M (used in the preceding checkpoint), a counterexample implies Var(f) on [1,X] is bounded below away from zero for the actual basin indicator. Therefore approximating its centered indicator in normalized mean square to o(1) by such polynomial-phase predictors would settle the conjecture. No such approximation is constructed.

This is not an all-order Gowers theorem: genuine polynomial phases do not cover general bracket-polynomial or higher-step nilsequence correlations. Nor does it imply independent colors along the actual Collatz graph or along the ratio-five paired comparisons. The countermodel in APPROXIMATE_COLORING.md demonstrates the limit of these approximate invariance methods even with exact doubling and both colors of positive density.