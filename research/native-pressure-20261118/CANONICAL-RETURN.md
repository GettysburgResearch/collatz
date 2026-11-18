# Pointwise lower trace and the return law on every ordinary inverse tree

Let ρ_q=(2/3)3^q μ_q be the finite Syracuse weights and let h be the
essential lower regularization of their L¹ limit on Z₃. At **every positive
integer t**,

    h(t)=liminf_q ρ_q(t)=lim_Q Q^(−1) sum_(q<Q) ρ_q(t),
    lim_Q Q^(−1) sum_(q<Q) |ρ_q(t)−h(t)|=0.                         (1)

Thus the stationary density's canonical lower-semicontinuous representative
agrees on the ordinary integers with Valbuena's canonical Cesàro trace
(in the displayed normalization). The finite-depth sequence converges
in natural density of depths. Ordinary convergence at every depth is
a different assertion.

For the harmonic inverse walk starting at any positive odd unit t, the
random empirical distribution of its first Q states, regarded in
E=Z₂^odd × Z₃, converges **in probability** to the same measure

    ν = normalized odd dyadic Haar × μ.                               (2)

In particular every fixed finite valuation pattern has its iid geometric
frequency in probability on every ordinary component. The law in (2)
concerns the random inverse path, not a typicality assertion about a
prescribed forward trajectory.

[Valbuena, prior canonical Cesàro and Abel trace results](https://doi.org/10.5281/zenodo.23025885).
[Earlier canonical inverse-word upper frequencies and prior results, §§8–10](https://rstation.ai/problems/collatz/papers/12).

## 1. Cancellation of all centered periodic observables

For an odd ordinary t use the geometric transfer L on odd source
functions, with weights J_q(y) at U^q y=t. For a function f periodic
on the odd positive integers, let m(f) be its mean over the odd classes
in one even period. Then

    sum_(q<Q) |L^q(f−m(f))(t)| ≤ C_f t sqrt(Q)                       (3)

uniformly over nonperiodic t. At periodic t multiply the absolute
constant by 1/(1−J_c), with J_c the odd cycle multiplier. To see this,
write f−m(f) as the average of f(y)−f(y+2j) over all shifts in one
period. In the signed sum at t, shift the second index. The two kernels
at sources y and y−2j agree once those sources balance at a common
shortcut clock and odd count before completion of q odd steps. The
finitely many unpaired small sources cost O_f(t) in the sum over q,
since each source occurs at most once when t is nonperiodic. The
uncancelled paired sources are counted by the dyadic shell argument
of the temporal variation estimate: at h shortcut steps the fraction
of pending pairs is O_j((1+h)^(−1/2)), by a union over 2j adjacent
pairs and the complete dyadic cylinder dictionary. The same shell
distance and geometric upper tail estimates apply. If t is periodic,
each source's later visits have geometric multipliers J_first J_c^s.
A failure before a contributing visit includes a failure before the
first visit whenever the shell-distance lower bound is applied.
Summing the weights therefore costs at most 1/(1−J_c). At multiples of
3 all nonempty inverse levels vanish.

[Dyadic shell bounds and geometric tail in detail](TEMPORAL-VARIATION.md).
[Leen, *Exact rates in Collatz synchronization*](https://doi.org/10.5281/zenodo.23268751).

Local functions on E (depending on finite dyadic and ternary digits)
are periodic on the odd integers; their periodic mean equals integral
against σ=normalized odd dyadic Haar × ternary Haar by the Chinese
remainder theorem. For each ordinary odd t the masses g_q(t)=L^q1(t)
are bounded uniformly in q. Approximation by local functions in sup
norm therefore extends (3), in time-average form, to all continuous z:

    Q^(−1) sum_(q<Q) [L^q z(t) − σ(z)g_q(t)] → 0.                   (4)

[Pointwise finite-height bounds, with prior trace comparisons](ORDINARY-DENSITIES.md).

## 2. Identification of the ordinary point values

The established lower-semicontinuous h has Haar mean 2/3, satisfies
h≥Lh everywhere, and is at least an absolute positive constant on the
units. Also h(t)≤liminf ρ_q(t), by its definition using local essential
infima. For n≥1 choose a nonnegative bounded local z_n increasing to
h, for example the infimum of min(h,n) in the ternary n-cylinder.
Every ρ_q(t) for positive odd t is bounded uniformly in q. Positivity
gives h(t)≥L^q z_n(t). Apply (4) and take the upper limit of the time
average to get

    h(t) ≥ σ(z_n) limsup_Q Q^(−1) sum_(q<Q) g_q(t).

Let n increase; σ(z_n)→2/3. On the other hand
h(t)≤liminf_q ρ_q(t)≤liminf_Q Q^(−1)sum ρ_q(t). This proves all the
equalities in (1) for odd t. A bounded sequence with the same finite
liminf and Cesàro limit has mean absolute deviation from that limit
tending to zero (the negative deviations tend to zero).

The same argument with L^q h(t) in place of h(t) shows the decreasing
sequence L^q h(t) has limit h(t), hence Lh(t)=h(t) at each odd t.
Moreover h(t)≥c g_q(t) uniformly: h≥c on units and at each level the
nonunit-source weights inject into unit sibling weights with a factor
four. At t=2^v u for u odd, shift the first inverse exponent a to a+v
to realize the same odd parent of u. Thus g_q(t)≤2^v g_q(u) for q≥1,
so h(t) is finite. The sum of J_a h(x_a) over the positive odd parents
is finite because Lh(t)≤h(t). In the recursion ρ_(q+1)(t)=Lρ_q(t),
the odd parent weights are dominated by a constant times h (with the
single depth-zero term handled separately). Dominated convergence of
the Cesàro averages over those parents gives the limit Lh(t). Now

    h(t) ≤ liminf ρ_q(t) ≤ Lh(t) ≤ h(t),

proving (1) and harmonicity at even t as well.

[Lower regularization, minorization and transfer inequalities](MINORIZATION.md).

## 3. Weak endpoint means and random empirical measures

The inverse transition t→x with Ux=t has probability J_1(x)h(x)/h(t).
All its states are positive odd units. With X_0=t and a bounded state
function f, E_t f(X_q)=L^q(h f)(t)/h(t). For 0≤f≤1 continuous on E,
bound h f from below by z_n f. Equations (1) and (4) and monotone
convergence give the lower bound (3/2)σ(h f)=ν(f) for the lower limit
of the mean of E_t f(X_q). Apply it to 1−f to obtain equality. Thus
the expectations of the random empirical measures converge weakly to ν.

Here ν is ergodic for the forward map
U(v,z)=((3v+1)/2^a,(3z+1)/2^a), a=v₂(3v+1). Define U arbitrarily at
v=−1/3, a ν-null set; it is continuous elsewhere. One direct proof
of ergodicity realizes ν as a factor of the two-sided iid geometric
shift. The future valuation list determines the dyadic odd v via
nested cylinders modulo 2^(a₀+…+a_(r−1)+1), each having the specified
geometric word probability 2^(−sum a) under normalized odd Haar.
The past list defines z by successive compositions of the F_a
contracting ternary distance by 1/3. This has law μ and is independent
of the future. Advancing the iid shift induces U.

Let η_Q=Q^(−1)sum_(q<Q)δ_(X_q,X_q), using the ordinary state in each
completion. Compactness gives subsequential limits of the laws of η_Q
on the space of probability measures on E. Every such limit has
barycenter ν by the preceding expectation calculation. Almost every
measure in the limit therefore gives the exceptional slice v=−1/3
zero mass. For continuous f the functional η↦η(f∘U) is continuous
at each such measure, by the bounded almost-everywhere-continuous
version of weak convergence. The exact reverse identity U(X_q)=X_(q−1)
gives |η_Q(f∘U)−η_Q(f)|≤2||f||∞/Q. Passing to limits, using a countable
dense family of continuous tests, shows the limiting random measures
are invariant almost surely. An ergodic probability is an extreme
invariant probability; its decomposition as their barycenter is
therefore concentrated at ν. Every subsequential law is δ_ν, proving
convergence in probability.

A fixed valuation word is a clopen dyadic cylinder with ν-mass
2^(−sum a). The same conclusion applies to joint clopen tests of
dyadic and ternary digits, and to all ν-continuity sets. At a
nonperiodic root there are no repeated inverse states. The uniform
simple-segment reciprocal bound then gives

    log X_Q = log t + log(2) sum_(j=1)^Q v₂(3X_j+1) − Q log(3) − O(1).

The bounded tests min(v₂(3v+1),K) are continuous after assigning value
K on the exceptional slice. Their limiting means tend to 2 as K grows.
Consequently P_t(log X_Q/Q < log(4/3)−ε)→0 for every ε>0. No upper
physical moment or uniform-in-moving-root assertion is used.
