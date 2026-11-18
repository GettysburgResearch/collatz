# Strong physical and arithmetic laws on every fixed-root inverse boundary

Let U(x) be the odd part of 3x+1, let a(x)=v₂(3x+1), and put
ℓ=log(4/3), with natural logarithms. Start the canonical inverse walk at
any fixed positive odd unit t. Write X₀=t, U(X_i)=X_(i−1),
S_q=Σ_(i=1)^q a(X_i), and p_q for the probability of the realized
length-q prefix. Almost surely,

    S_q/q → 2,       log X_q/q → ℓ,       −log p_q/q → ℓ,
    log h(X_q)/q → 0.

The empirical laws of (X_i,X_i) in the odd dyadic integers times the
ternary integers converge weakly almost surely to normalized odd dyadic
Haar times the stationary Syracuse-offset law μ. In particular every
fixed valuation word w has frequency 2^(−Σw), simultaneously. These are
path laws for each fixed starting root. Their external inputs are the
published setwise first-landing estimate and the identification of the
natural-density boundary with the canonical one up to a bounded density.

[Power bounds, Theorem 1, (2)](https://rstation.ai/problems/collatz/papers/102)
· [Boundary comparison, §10.1, and Valbuena trace, §8](https://rstation.ai/problems/collatz/papers/12)
· [Stationary arithmetic coding](CANONICAL-RETURN.md).

## Sampling a last visit from the inverse boundary

First take a nonperiodic t. For an ancestor x write d_x for the relative
odd natural density of its basin. The density boundary Q_t assigns the
cylinder ending at x mass d_x/d_t. Its paths and those of the canonical
law P_t have bounded likelihood ratios in both directions by the cited
boundary comparison, and d_t>0. A nonperiodic root has distinct states
on every inverse path and a unique depth for each ancestor. For R≥t let
n(R)=max{i:X_i≤R}, and put Y_R=X_(n(R)). All ancestors ≤R have depths
at most some finite deterministic N_R, since there are finitely many
integers ≤R. The label Y_R is determined by the prefix to depth N_R+1.

For A a set of odd labels ≤R, take any finite collection of those
depth-(N_R+1) cylinders having last label in A. Their terminal basins
are disjoint, and every odd source in their union first enters [1,R] at
that same last label of its cylinder. An earlier entry, before the source
reaches the terminal ancestor, would be an ancestor of t of depth above
N_R. Adding the basin densities, then increasing the finite collection,
gives Q_t(Y_R∈A)≤μ_R(A)/d_t, with μ_R the limiting relative odd
first-landing law. The cited power bound and the bounded likelihood
ratio therefore give constants C_t,C,g>0 with

    P_t(Y_R∈A) ≤ C_t exp(C√log R) ( |A|/R + R^(−g) ).               (1)

## Arithmetic statistics between nearby height thresholds

Take R_j=⌊exp(j³)⌋, L_j=log R_j, D_j=L_j−L_(j−1)∼3j². By (1) and
Borel–Cantelli, almost surely for all large j,

    L_j−j^(19/10) ≤ log Y_(R_j) ≤ L_j.                               (2)

Fix an odd dyadic/ternary product cylinder f, regarded as an indicator,
and denote its stationary product mean by ν(f). We now show that for
y=Y_(R_j), simultaneously for all 0≤m≤K_j=⌊10D_j/ℓ⌋,

    Σ_(i<m) a(U^i y) = 2m + o(D_j),
    Σ_(i<m) f(U^i y,U^i y) = mν(f) + o(D_j)                         (3)

almost surely. The constants and exceptional sets below may depend on f.

Here are details of the required integer count. On normalized odd dyadic
Haar the forward valuations are iid positive geometric with mass 2^(−a):
a specified initial word of sum s is one odd residue modulo 2^(s+1).
If f has ternary precision d, its ternary argument at any i≥d is
determined modulo 3^d by the previous d valuations alone, since each
forward affine step contracts ternary distances by 1/3. If f has dyadic
precision b, its dyadic argument at i is determined by the next b
valuations, since the inverse affine steps contract dyadic distances by
at least 1/2. Thus apart from at most d initial terms its indicator is
a bounded function of a fixed window of iid exponents. The window mean
is ν(f): disjoint past and future give μ modulo 3^d and independent
odd Haar modulo 2^b. This coding also proves the count for every starting
ternary integer, despite any dependence of the two physical coordinates.

For each fixed ε>0 the exceptional probability that either sum deviates
by more than εD_j for some m≤K_j is O_ε,f(exp(−c_ε,f D_j)).
For the unbounded geometric sum use its finite exponential moment near
zero and the Chernoff bound on both centered tails, choosing the tilt
small relative to ε and K_j/D_j. For the bounded fixed-window sum
split indices into finitely many disjoint residue classes modulo the
window length (or one for a constant function), then apply Hoeffding
to each class. A union over the O(D_j) partial lengths preserves the
exponential bound after decreasing c.

These events, together with all required valuations through K_j+b, are
decidable from M_j=⌈4(K_j+b+d+2)⌉ initial dyadic bits except for a set
of Haar probability O(exp(−c D_j)). Indeed the geometric total through
that horizon exceeds M_j−1 with at most that probability by Chernoff.
Declare uncompleted words bad; this enlarged bad event is a union of
residue classes modulo 2^M_j by the initial-word coding. On odd positive
integers ≤R_j the count of bad labels is consequently at most
O(R_j exp(−c_ε,f D_j)+2^M_j). Since D_j is of order j² and L_j is of
order j³, substitution in (1) is summable: the landing loss is only
exp(O(j^(3/2))). Borel–Cantelli and a countable intersection over
rational ε>0 and product cylinders give (3).

Until K_j steps, (2), (3) and U(x)≥3x/2^a(x) keep the path above
exp(L_j−O(D_j)), with the o(D_j) error in (2) understood. Thus the
total additive correction Σ log(1+1/(3U^i y)) is o(1) on this segment.
The forward log height at m is log y−ℓm+o(D_j) uniformly. Its first
entry below or at R_(j−1) occurs after

    m_j=D_j/ℓ+o(D_j)

steps: the uniform log formula brackets that time between
(1−ε)D_j/ℓ and (1+ε)D_j/ℓ for every ε>0. Since y is the last
inverse visit below or at R_j, this first entry on its forward orbit
is exactly the last inverse visit below or at R_(j−1). The root lies
below both thresholds for large j. Hence m_j=n(R_j)−n(R_(j−1)).
Summing gives n(R_j)∼L_j/ℓ, because Σ_(i≤j)o(D_i)=o(L_j).
Summing (3) on these same segments gives valuation mean 2 and test mean
ν(f) at those depths. The valuation sum is nonnegative, f is bounded,
and n(R_(j+1))/n(R_j)→1, which interpolates the means to every q.
The segment log formula gives log X_q/q→ℓ throughout, since D_j=o(L_j).
Product cylinders determine weak convergence on the compact product.

## Information of the realized prefix

For fixed ε>0 and q≤2L_j/ℓ there are at most R_j^(1−ε) depth-q
prefixes whose probability is ≥R_j^(−1+ε). Their terminal labels
over all such depths form a set of size O(L_j R_j^(1−ε)); intersect
with [1,R_j]. Bound (1) excludes Y_(R_j) from this set eventually
almost surely. Since n(R_j)∼L_j/ℓ the realized information at this
depth is ≥(1−ε)L_j. Prefix information is nondecreasing and consecutive
depth ratios tend to one, so its lower asymptotic rate is at least ℓ.
On the other hand the exact identity

    p_q=3^q 2^(−S_q) h(X_q)/h(t)

and the positive uniform lower bound of h on units give upper rate ℓ.
Rearranging the same identity gives log h(X_q)/q→0.

At a periodic root the probability of following the cycle backwards for
k full turns is J_c^k, by telescoping h; its forward affine multiplier
J_c is strictly below one by the positive intercept around the cycle.
Almost surely the path exits after finite time. Its first off-cycle
state is nonperiodic. Apply the nonperiodic result conditionally there;
a finite prefix changes none of the limits (its information is finite).
