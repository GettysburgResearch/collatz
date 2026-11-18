# One stationary ternary observable detects the arithmetic cone obstruction

Use the limiting marked densities H_η(z,v) and λ-normalized ternary
Haar conditional expectations E_Q from the solenoid phase theorem.
For 0<η<1 put

    K_η(z)=∫_(0≤v<1/2) H_η(z,v) dv,
    K(z)=∫₀¹ 22 η^21 K_η(z) dη.

This version-independent nonnegative observable of the stationary joint
real and ternary law belongs to L^p(λ) for each 1≤p<2. Every positive
Collatz orbit is eventually periodic if and only if

    liminf_(Q→∞) (E_Q K)(0)/Q = 0.                                    (1)

In the eventual-periodic case the ratio tends to zero. An escaping orbit
forces a strictly positive lower limit. The test concerns one specified
ternary center, and does not establish the small-cylinder estimate in (1).

[Stationary densities and the generic phase result](SOLENOID_PHASE.md)
· [Physical simple cones](HARMONIC_OFFSET_CONE.md)
· [Repeated-path cycle domination and raw zero phase](TRIADIC_OFFSET.md)
· [Translated simple-orbit packing](../native-pressure-20261118/ORDINARY-DENSITIES.md).

## Comparing a stationary cylinder to an ordinary word sum

In the lower real half of the solenoid, the j-th denominator is
t'=t+2v with t=2j+1, j≥0, and its ternary label is t−2z. For
z uniform on 3^Q Z₃ this label is Haar on t+3^Q Z₃. Hence the
corresponding averaged marked density is exactly
3^Q P(Z≡t mod 3^Q, ηt'≤F≤t'). Peel Q outer iid letters of the
stationary affine series; the ternary congruence is settled by these
letters alone. Every compatible prefix w comes from exactly one
positive odd integer x with U^Q x=t and t=F_w+J_w x. Its normalized
weight is J_w. Its remaining real offset is J_w F' with F' an
independent stationary real series.

Let S_Q^0(θ) denote the raw mass marked by F_w/t∈[θ,1] on the original
finite odd grid. Any such word has θt≤F_w≤t. On F'≤1 one also has
F_w+J_w F'≤t since x≥1. As t≤t'≤2t, this contributes to the
stationary (θ/2)-cone with 1/t'≥1/(2t). Therefore

    (E_Q K_(θ/2))(0) ≥ c S_Q^0(θ)                                    (2)

for every Q, with c=P(F'≤1)/4>0. Positivity follows for example
by first choosing a sufficiently large independent outer exponent on
the event that the remaining finite tail lies in a fixed bounded set.

Conversely let T_Q(η) be the raw marked sum over all odd targets t≥1
with no upper grid cutoff. A stationary marked contribution with
F_w<ηt/2 requires F'≥ηt/(2J_w)≥ηx/2. Choose 0<s<1, so E(F')^s<∞.
Each x gives just one word at depth Q and 1/t'≤1/t, J_w/t≤1/x. Thus

    (E_Q K_η)(0) ≤ (1/2) T_Q(η/2) + C_s η^(−s) Σ_(x≥1) x^(−1−s).     (3)

When η is fixed and Q is sufficiently large T_Q(η/2)=S_Q^0(η/2),
since F_w≤(3/2)^Q−1. No limiting interchange in Q is needed for
the summable tail comparison.

## Combining all thresholds in a single scalar

Uniformly over Q≥1 and 0<η<1, T_Q(η)≤C Q(1+η^(−20)). Here are the
details supporting this domination. A simple path avoiding every value
≤R has F_w/t≤C R^(−1/20): sum reciprocals on dyadic shells using the
uniform O(Y^(19/20)) orbit count. Thus marked simple paths visit some
s≤C'η^(−20); at most Q+1 possible forward targets arise per s.
At each such target the simple layer has slope-sum divided by t bounded
absolutely. For nonperiodic targets this is the ordinary harmonic
antichain bound; a simple path to a periodic target is a first-hit
path, and obeys the first-hit layer bound. The repeated paths have
cyclic target on a cycle of period d≤Q. By the cited cycle argument
the total density over its d targets costs at most C(d+Q)p_C, where p_C
is the basin density. Summing gives O(Q). These arguments did not use a
target cutoff. In the eventual-periodic case simple marked targets at
fixed η form a finite set, and each fixed cycle contributes o(Q); the
same summable p_C domination shows T_Q(η)/Q→0.

The positive function K is in L^p: on 0≤v<1/2 all t'≥1; in dyadic
band B one must have t'≤2B/η, so B≥η/2 and there are O(B/η) possible
indices. The summable majorants of the solenoid proof therefore give
||K_η||_p≤C_p/η. Use (3), the preceding Q-bound, and dominated
convergence in η to obtain the forward direction of (1). If an orbit
escapes, the raw zero-phase theorem gives a fixed θ>0 with
liminf S_Q^0(θ)/Q>0. Monotonicity carries (2) to every η∈(0,θ/2).
The positive integral of 22η^21 over that interval proves the reverse
direction.

## The half-phase fixed point and limitations of average regularity

The half phase corresponds to the fixed natural-extension point
(z,v)=(−1/2,1/2). At the carry boundary its even grid uses t=2j,
1≤j≤3^Q. On the neighboring half 1/2<v<1 the denominators are
t'=2j+2v−1, and the ternary labels at z≡−1/2 mod 3^Q agree with t.
The actual integer identity t=F_w+J_w x with x≥1 still holds after
unfolding the final even valuation. Keeping F'≤1 just as in (2) gives

    E_Q[∫_(1/2)^1 H_(2θ/3)(·,v)dv](−1/2) ≥ c' A_Q(θ),

where A_Q is the simple half-phase cone. In particular its
superlogarithmic escape lower bound would be a growth condition on a
specified stationary cylinder average.

Neither Haar-generic convergence nor strong global moment control
excludes either specified-point growth. Indeed f(z)=v₃(z), defined
arbitrarily at zero, belongs to every finite L^p and has
(E_Q f)(0)=Q+1/2. Its error norm is exactly
3^(−Q/p)||f−1/2||_p, since outside the zero cylinder f is already
known exactly. Translating furnishes the same example at −1/2. This
is a comparison observable, not a claim that the actual K has this
behavior. Countably many translated singular fibre carriers likewise
do not control this local density at a given arithmetic center.

[Half-grid lower bounds](HALF_OFFSET.md) · [Ordinary real fibre carriers](../terminal-residue/SUPPORT.md).
