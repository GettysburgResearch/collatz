# Leading ternary digits cannot supply all the parity decisions

**PROPOSED.** Let x_j be a nonperiodic positive ordinary shortcut trajectory and b_j=x_j mod 2. Fix an integer a, a real clock frequency α, a circle phase β and any fixed binary labeling of a finite interval partition of the circle. Then the labeling of

    φ_j = {a log₃ x_j + αj + β}

cannot eventually coincide with b_j. This includes every fixed rule on the leading ternary significand. In the irrational effective-frequency case a stronger conclusion holds even when the rule may respond arbitrarily in shrinking boundary neighborhoods, as specified below. This uses the [moving-start Hamming-return theorem](../rotation-coded-orbits/ORDINARY_PREFIX_RETURNS.md); the earlier exact irrational-rotation exclusion does not alone apply, because the actual integer produces a varying phase error.

Put θ=α−a log₃2. For any forward interval of length i starting at t, logarithmic telescoping gives

    φ_(t+i) = φ_t + iθ + aD_(t,i)   mod 1,
    0 ≤ D_(t,i) = Σ_(t≤j<t+i, b_j=1) log₃(1+1/(3x_j)).

The integer a removes the count of odd steps exactly. Along an escaping orbit the cumulative D has a finite limit, by the [simple-orbit reciprocal estimate](../integrated/orbitwise-boundaries/README.md). If θ is rational, each residue class of times modulo its denominator therefore approaches one circle point monotonically from one side, or is eventually constant. Its finite-partition labeling is eventually constant on each class. The predicted word is eventually periodic, which cannot be the eventual parity of a nonperiodic ordinary orbit by the dyadic cylinder congruence. In this rational-frequency assertion the response is the actual labeling with fixed endpoint conventions.

Now take θ irrational, any fixed L>log(3/2)/log(4/3), and unbounded convergent denominators q for θ. Take t at the first strict suffix minimum of the orbit above q³. Such minima increase without bound. Their consecutive ratios are at most two: the next minimum is no larger than the immediate next state. Therefore q³≤x_t≤2q³ for all sufficiently large q, and every later state is at least x_t. For all i≤(L+1)q the physical phase differs from its rigid rotation φ_t+iθ by O_a,L(q^(-2)). Comparing times i and i+q, the reference phase shift has circle distance ||qθ||≤1/q. Thus the two predictions match unless the first reference phase is within O(1/q) of a partition boundary. In every q consecutive reference times these points are separated by at least 1/(2q), by best approximation using the preceding convergent denominator. There are only O_a,L,partition(1) possible prediction mismatches over 0≤i<floor(Lq), uniformly in φ_t.

By the moving-start theorem the number of actual parity mismatches between these two shifted portions tends to infinity, since log x_t=o(q). Each prediction error among the first (L+1)q positions accounts for at most two mismatched pairs. The number of prediction errors on these windows must itself tend to infinity; this concerns one fixed ordinary trajectory.

More generally let r(X) be nonincreasing with r(X)=o(1/log X). Even if the predictor is entirely unconstrained whenever its observed phase lies within r(x_j) of a boundary, unboundedly many errors must occur outside the permitted ambiguity on appropriate windows. Choose a height floor B_q with log B_q=o(q), B_q≥q³, and q r(B_q)=O(1). To see existence, for each fixed s≥1 one has q r(exp(q/s))→0; increase s to infinity sufficiently slowly and use B_q=exp(q/s), keeping s≤sqrt(q). Take the first strict suffix minimum above B_q, so B_q≤x_t≤2B_q. The cumulative phase error on the window remains O(q^(-2)). The count of positions in the allowed ambiguity, as well as the count of possible shifted prediction mismatches, is O(1) by the same spacing. The moving-start conclusion still applies. The conclusion supplies neither a positive density of errors nor a decision about escape.
