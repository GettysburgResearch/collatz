# An iterated-logarithm-scale upper bound on fixed-root inverse paths

The almost-sure bounds of [the first-landing rate argument](PATH-RATE.md)
hold with q^(3/4) replaced by

    V(q) = √(q log log(q+16)).

Thus the physical and odd clocks, the information of the realized
prefix, log h(X_q), and each fixed cylinder count have an almost-sure
error O_f(V(q)). This gives an upper order only. The proof uses
first-passage stabilization in addition to the boundary comparison.
For information it retains the setwise power estimate of the earlier
argument.

[Tao, Proposition 1.11](https://arxiv.org/html/1909.03562v7#S1.SS3)
· [Valbuena, first-passage stabilization, local passage and first-hit clocks](https://doi.org/10.5281/zenodo.23025885)
· [Density-boundary comparison, §10.1](https://rstation.ai/problems/collatz/papers/12)
· [Setwise power estimate, Theorem 1](https://rstation.ai/problems/collatz/papers/102).

## Transporting all events of an incoming segment to a short source window

Fix a=1.001. Let Q_y be an odd integer drawn with reciprocal weights
on [y,y^a]. For a real threshold R let D_R be the first odd iterate
≤R, with value 1 assigned on failed passage. Write ν_R for the law of
D_R(Q_(R^a)), and μ_R^* for the limiting relative odd natural-density
law with the same default. The stabilization bound is

    d_TV(law(D_R(Q_(R^a))), law(D_R(Q_(R^(a²))))) ≤ C(log R)^(−c).

The deterministic composition identity D_R∘D_x=D_R for x≥R≥1 holds
also on failure. Applying it at x=R^(a^i) for successive i≥0 gives

    d_TV(μ_R^*,ν_R) ≤ C' (log R)^(−c).                               (1)

In detail the difference between the pushed laws of ν_x and ν_(x^a)
is bounded by C(log x)^(−c); their sum is geometric. For fixed R the
pushed law of ν_x tends to μ_R^* along x=R^(a^i): its coordinates
are the log-window averages of the finite-label indicators D_R on
[x^a,x^(a²)]. Relative odd natural density of the limiting landing
cells, with failures sent to 1, implies precisely this convergence
by partial summation. This is the same telescoping mechanism used in
Valbuena's first-hit clock argument.

For nonperiodic t, the last-below-R vertex Y_R of the fixed-root
inverse path has P_t(Y_R∈A)≤C_t μ_R^*(A) for R≥t by the finite-depth
cylinder argument in the [strong laws](ALMOST-SURE.md). Sending failures
to 1 can only enlarge the measure of a set of finite labels. Consequently
every event depending on the label and any part of its subsequent
deterministic forward trajectory has probability at most

    C_t (P(D_R(Q_(R^a)) belongs to the event) + C'(log R)^(−c)).      (2)

## A maximal estimate from the actual source

Write L=log R, N=⌊L/20⌋, u=B_f V(L). For the source z=Q_(R^a)
consider the first N forward steps and a fixed product-cylinder test f.
Outside probability O_f(exp(−c_f u²/N)+exp(−cN)), simultaneously at
every 0≤m≤N,

    |Σ_(i<m) a(U^i z)−2m| ≤ u,
    |Σ_(i<m) f(U^i z,U^i z)−mν(f)| ≤ u.                             (3)

To verify this bound, first use the iid geometric law under dyadic Haar.
For the centered geometric sum the maximum over m≤N has two-sided
tail ≤2exp(−c u²/N) for u=o(N): apply the nonnegative exponential
martingale maximal inequality with tilt of size u/N of either sign.
For the bounded test discard its fixed initial ternary memory d.
After that it is a bounded function of a fixed window of geometric
letters with stationary product mean ν(f). Split positions by their
index modulo the window length. The centered variables in any one
class are independent. Apply the same maximal inequality there with
a bounded-variable moment-generating bound, and union over the fixed
number of classes. Changing constants absorbs the discarded terms.
The classes and the test are as in the strong-law proof.

The first N letters and the additional fixed dyadic lookahead are
decided by 4(N+O_f(1)) dyadic bits except on probability O(exp(−cN)).
Declare paths exceeding that bit budget bad. The common good conditions
in (3) are sufficient for every starting ternary point because its first
d bounded contributions were discarded. The resulting dyadic bad set is
periodic. Its counting discrepancy from its odd-Haar proportion in
[1,Z] is O(2^(4(N+O_f(1)))). Partial summation on the logarithmically
weighted interval [R^a,R^(a²)] then costs O(exp(−cL)) since
4N log 2 < aL/2. This proves the maximal estimate for the actual
integer source. Unlike a union over all prefix lengths, the maximal
inequality incurs no growing prefactor.

Throughout these N steps the log height is at least
aL−(2N+u)log 2 > L/2. The affine correction summed over this path
is o(1); hence its log height at m equals log z−ℓm+O(u), ℓ=log(4/3).
Since a²−ℓ/20 < 1/a, this path reaches both R and R^(1/a) by N,
in that order. The log height at each first entry differs from its
threshold log by O(u), since consecutive heights differ by O(u)
as follows by subtracting two consecutive prefix estimates. Between
those entries the odd clock differs from (1−1/a)L/ℓ by O(u).
Every partial sum on this segment differs from its stationary linear
prediction by O_f(u) by subtraction in (3), including the valuation
sum. These statements now involve only the landing label and its
forward trajectory to the smaller threshold. They transfer by (2).

Take R_j=exp(a^j). The errors (log R_j)^(−c) in (2) are summable.
The exponential maximal tails are also summable in j on choosing B_f
large enough, since log log(log R_j)=log j+O(1). Almost surely all
the stated segment and partial-segment estimates therefore hold for
large j. Concatenating these segments exactly as in the strong laws
costs O_f(V(log R_j)) in total error since the log scales increase
geometrically. An arbitrary partial segment costs the same order by
prefix subtraction. This gives S_q=2q+O(V(q)), log X_q=ℓq+O(V(q))
and cylinder counts qν(f)+O_f(V(q)), at every sufficiently large q.

For information, at the dense thresholds ⌊exp(k)⌋ the new height bound
places last-visit depths at k/ℓ+O(V(k)), with consecutive gaps O(V(k)).
The heavy-label count and the setwise power estimate in the previous
rate argument give information ≥k−O(√k) at each of these last visits.
Monotonicity gives −log p_q≥ℓq−O(V(q)). The opposite bound and
log h(X_q)=O(V(q)) follow from the normalized path identity, the
clock bound and the positive lower bound of h. Conditioning at the
first cycle exit handles periodic roots. Countable intersection gives
the simultaneous assertion for all fixed cylinders.
