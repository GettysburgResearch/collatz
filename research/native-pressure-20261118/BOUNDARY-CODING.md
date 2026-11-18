# Exact stationary decoding and residual integer-fibre information

Under the stationary iid geometric affine law the full exponent sequence
is determined almost surely by its joint real and ternary boundary value.
At every fixed positive odd inverse root t, the realized real boundary
value B₀ leaves at most half a logarithm in the following pointwise sense.
Let p_q^B be a regular conditional probability of the realized length-q
inverse prefix given B₀. Almost surely,

    limsup_(q→∞) (−log p_q^B)/log q ≤ 1/2.

The integer-root conclusion permits nonunique coding. It compares to
the unconditioned information ℓq+O(√(q log log q)) of that prefix.

[Same-division disjointness and the rational-affine boundary context, §§1,8.1](https://rstation.ai/problems/collatz/papers/19/v2)
· [Integer path clock](ITERATED-LOG-BOUND.md)
· [Real-tail estimates and two-shell comparison](REAL-TAILS.md).

## The stationary joint boundary

Write (B,Z) for the joint affine series of iid exponents and (B_n,Z_n)
for the shifted tail. The boundary, the exponent total S_n and the
integer part ⌊B_n⌋ together determine the n-letter prefix. Indeed the
same-total image rectangles in the cited disjointness result are
disjoint for a unit seed strip [0,1)×Z₃. Replacing this strip by
[j,j+1)×Z₃ translates all their real intervals equally at fixed S_n.
Equivalently, distinct same-total integer intercepts with intersecting
ternary cells differ by a nonzero multiple of 3^n, which separates the
half-open real intervals at this multiplier. Equality of the intercept
at fixed total forces equality of the word by the exact dyadic valuation
coding. The half-open convention includes integer real endpoints.

The conditional entropy of the n letters given the boundary is therefore
at most H(S_n)+H(⌊B_n⌋)=O(log n). The first entropy has this order from
the mean 2n alone (compare the entropy of a geometric distribution of
that mean). The second is finite uniformly in n since B has a finite
positive subcritical moment (compare an integer law proportional to
(j+1)^(−2)). Conversely, conditional chain rule gives this same
conditional entropy exactly n H(a₁|B,Z). Once preceding letters have
been specified the invertible affine map recovers their shifted boundary,
and the remaining iid sequence together with that boundary is independent
of the specified letters. Dividing by n proves H(a₁|B,Z)=0. Iterating
on the shifted sequence recovers the entire code. This is a direct
same-total argument in the known rational-affine Poisson-boundary setting.

## A bounded tail close to every sufficiently high depth

Use the two-shell comparisons of the real-tail estimates and their
notation. On a shell of log height L the proxy supplies N comparable
to L iid geometric letters in reverse order. Put H=⌈A log L⌉ with A
larger than the thresholds for the exponential far-tail bounds in
both adjacent shells. The H-term real affine series has probability
at least 1/2 of being ≤K for some fixed K independent of H, by its
uniform subcritical moment. For any interval of ⌈D(log L)²⌉ consecutive
origins there are order D log L/A disjoint H-letter trials; restrict
to trials whose full windows stay inside the interval. Failure at every
trial has probability at most exp(−cD log L/A). A union over O(N)
possible interval starts and the source-to-boundary comparison make
these failures summable on geometric log-height shells if D is large.
Use the extra outer shell to cover origins near the end of the inner
shell, as in the real-tail proof. The true far tail beyond H is o(1)
at every such origin on the almost-sure eventual exponential-drift
event. Thus almost surely every sufficiently large q has a later
m∈[q,q+(log q)³] with B_m≤K+1. The extra logarithm absorbs fixed
constants and rounding.

## An explicit short list at an ordinary root

Given t, B₀=b, the index m, its total s=S_m and j=⌊B_m⌋, there is
at most one possible endpoint. Subtract the real and integer exact
affine identities to obtain

    X_m = (t−b) 2^s/3^m + B_m.

The half-open interval [(t−b)2^s/3^m+j,(t−b)2^s/3^m+j+1) has exactly
one integer. Forward iteration through m steps recovers the word when
this candidate is a legal endpoint; otherwise discard it. For specified
q,b, enumerate m∈[q,q+(log q)³], 0≤j≤⌊K+1⌋ and integers s with
|s−2m|≤√m log m. Retain the resulting length-q prefixes. This
measurable list contains O(√q (log q)^4) candidates uniformly in b.
The all-depth clock bound and the bounded-tail visit show it contains
the realized prefix eventually almost surely.

Conditionally on any b, the chance that the sampled prefix belongs to
that list but has conditional probability below q^(−1/2−ε) is at most
O((log q)^4 q^(−ε)). Integrate over b and use Borel–Cantelli along
q=2^k. Conditional prefix probabilities along a realized infinite word
are nonincreasing, taking coherent versions outside one null set.
Consecutive logarithms in the dyadic sequence have ratio tending to
one. Interpolation and ε↓0 prove the claim. At a periodic root only
finitely many initial states precede cycle exit almost surely; the
endpoint and decoding identities above also hold directly on the
entire path there.

## Separation of alternative typical clocks

Fix two distinct inverse paths from the same integer t having the
same real B₀ and for which the empirical joint tails converge to Σ
and its marginals as in the real-tail theorem. Then for every fixed M,

    density {i : |S_i−S'_i|≤M} = 0.                                  (1)

Indeed, after their first different letter their prefix maps F_w,F_v
are distinct words of the same length. Exact stationary decoding implies
(F_w)_*Σ and (F_v)_*Σ are mutually singular: they are the conditional
boundary laws of disjoint positive-probability prefix events recovered
from the joint boundary value. Thus g_*Σ and Σ are mutually singular
for g=F_v^(−1)F_w. Both affine coordinates are acted on diagonally.
Writing T_i=(B_i,X_i in Z₃) and using equality of the two initial
joint points gives T'_i=g_i(T_i) with g_i=F_v^(−1)F_w. Its slope
is 2^(S'_i−S_i) and its translation is the dyadic rational
c_i=X'_i−2^(S'_i−S_i)X_i, by the integer coordinate identities.
When the clock difference is bounded by M and both real B-tails are
bounded by K, the denominator of c_i divides 2^M and its real absolute
value is ≤(1+2^M)K by the real identities. Only finitely many g_i can
then occur.

If any fixed g in that list occurred on a positive upper density of
these indices, take a subsequence with positive limiting mass and weak
limits of the corresponding partial empirical measures of T_i. They
are tight because they are dominated by the full empirical measures
converging to Σ. Their nonzero limit is dominated by Σ, and its image
under the fixed continuous affine g is also dominated by Σ, by the
second path's empirical limit. This contradicts g_*Σ⊥Σ. Finally let
K tend to infinity through continuity thresholds of the stationary real
marginal to obtain (1).

One can express this as a conditional collision identity. For almost
every real boundary b let π_b be the conditional infinite path law
at t given B₀=b. Then for each fixed M≥0,

    lim_(q→∞) q^(−1) Σ_(i≤q) (π_b×π_b){|S_i−S'_i|≤M}
        = Σ_(path atoms ω) π_b({ω})².

Indeed both paths are typical for π_b×π_b-almost every pair by
disintegration. Their clock-gap frequency is one when the paths
coincide and zero otherwise. Integrate by bounded convergence.
