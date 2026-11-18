# The compact-offset bulk of the moving ordinary fibres

Let G_x be the unnormalized positive-odd integer real fibre in the
[zero-cylinder flux formula](STATIONARY_ZERO_FLUX.md), with total mass
H(x)=lim g_q(x). Let (F,Z) have the stationary real–ternary affine law.
The following vague limit holds on (0,∞) × [0,∞) × ℤ₃:

    T⁻¹ Σ_(x odd positive) δ_(x/T) ⊗ G_x(dB) ⊗ δ_x
        → (du/2) ⊗ law(F,Z).                                         (1)

The order of coordinates on the right is (u,B,z). One can further retain
the odd dyadic coordinate of x, with independent normalized odd Haar
measure in the limit. In particular, the
family is uniformly tight after weighting by the *scaled Stieltjes kernels*
in (7) below, including at the ends of the spatial and real ranges.
The escape observable probes B of order x with an additional power of
T relative to (7). Formula (1) controls the ordinary bounded-offset
bulk without requiring a hypothesis on the escaping components.

## Marked source occupation

Write ℓ=log(4/3), δ=ℓ/2. At the i-th odd iterate x of a source n,
put V_i=∏_(j<i) (1+1/(3Uʲn))⁻¹ and B_i=x(1−V_i). In particular
B_0=0, and when x goes to Ux=(3x+1)/2^a the mark B goes to
(3B+1)/2^a. With E the limiting normalized odd logarithmic source
mean, each fixed x and bounded continuous φ satisfy

    ∫φ(B)G_x(dB)=δ x E Σ_(i:Uⁱn=x) V_i φ(B_i).                       (2)

Here infinitely many visits at a cyclic x are included. For φ=1 this
is the [canonical first-hit and geometric-lap formula](../unsafe-return-weights/SIGNED_MASS.md).
To see the marked version, consider visits with any specified last k
inverse letters w leading from y to x. The sum of their weights V_i
is exactly (J_w y/x) times the sum of weights at y, since the forward
orbit from y is deterministic. Thus their normalized limiting mass
is J_w H(y), and it sums over w to H(x) by harmonicity. In particular
short visits and truncations to finitely many words cause no loss in
the limit as the finite word sets exhaust the k-level. The terminal
prefix offsets β_w are precisely the bounded-support approximants of
the canonical fibre, increasing to its mark on inverse paths.

For clarity the actual B_i can be replaced by these prefix offsets.
Fix a large L. For a first hit of x, every visit before its last k
steps is above L once k exceeds the maximum first-hit distance to x
of any ancestor ≤L. The uniform simple-orbit reciprocal tail then gives
0≤B_i−β_w≤C x L^(−1/20), by multiplying the distortion from that
early segment by at most x in relative coordinates. At cyclic x,
first discard visits after m completed laps. Their total weighted
mass is at most J_C^m times the total mass at x, where J_C<1 is the
cycle multiplier. For the earlier visits increase k by m times the
period and apply the same bound. Uniform continuity on [0,x] proves
(2). The means of events depending on first landing in any fixed
finite interval exist by the first-landing theorem. Natural means for
these events also give the stated logarithmic means by partial summation.

## An incoming segment which retains the entire real mark

Fix a=1.001, R=T^a, G=T^40 and L=log R. Write Y_A for the first
ordinary label at most A, with default 1 on failure. Its limiting
source distribution differs by O((log A)^(−c)) in total variation from
that obtained from an odd reciprocal-weighted source in [A^a,A^(a²)].
On this proxy the two thresholds A and A^(1/a) are passed within
O(log A) steps outside a probability tending to zero, by the maximal
valuation and height estimates. Passage failure under the limiting
source measure is o(1) as A→∞ by natural-density almost boundedness.
These assertions use the [first-passage stabilization and short-window estimates](../native-pressure-20261118/ITERATED-LOG-BOUND.md).

The limiting probability that the segment from Y_G to Y_R consumes
more than C log T steps is o(1), with C absolute. Indeed take the
finite ladder G,G^(1/a),… down to the first threshold below R. Its
length is bounded independently of T. At each level the subsequent
passage time is a deterministic function of its landing label and its
failure probability transfers by total variation. Before reaching G
the orbit is simple and stays above G. Between first landing at G and
first landing at R, all source labels of the steps exceed R. Therefore,
except on limiting probability o(1),

    1−V_(entry at R) ≤ C G^(−1/20)+C(log T)/R.                        (3)

This bound is o(1/(T log T)). With initial mark zero at Y_R, a later
step ending at x thus miscalculates the original mark by at most x
times (3). For x in any fixed compact set of x/T and for O(log T)
subsequent tests, the total resulting error for a bounded Lipschitz
test is o(1). On bounded mark supports V_i=1−B_i/x=1+O(1/T).
The same error conclusions hold for the proxy started above R on its
first O(log T) steps, with the pre-entry sum bounded by O(log T)/R.

Let φ≥0 be Lipschitz in the real variables, compactly supported in
(u,B)∈(0,∞)×[0,∞), with any fixed ternary-cylinder dependence. From
Y_R form the deterministic sum of (x/T)φ(x/T,B,x) over the first
N=⌊L/20⌋ steps, setting the mark to zero initially and capping the
sum at M. Equations (2) and (3) bound the lower limit of the left
side of (1) paired with φ by δ times the lower limit of the same
capped statistic under the short proxy source. First T→∞ with M fixed:
the discarded events cost at most M·o(1). It suffices to count selected
visits in the first N steps of the proxy *from its initial source*.
Every selected visit with x in the test shell is after first landing
at R and within N steps thereafter. Failure default 1 has no influence
here; from 1 the actual labels remain 1. The proxy mark starting at
its initial label can be used by the preceding bound.

## Integrating the reciprocal source window

Up to exponentially small exceptional probability the first N letters
of the proxy can be coupled to independent weights 2⁻ᵃ, independently
of a continuous initial log height h uniform on [aL,a²L]. More
precisely, the integer source differs in absolute size from exp(h) by
O(2^(4N+2)), with the *integer* valuations equal to the coupled iid
letters. To verify this, divide the source interval into consecutive
blocks of length 2^(4N+2). Their incomplete ends and the relative
variation of reciprocal weights within a block cost O(poly(L)
2^(4N+2)/R^a) in total variation. Couple at block level to the
continuous reciprocal measure, then couple the odd residue in each
block to uniform odd dyadic residues independently of h. The geometric
valuation total exceeds 4N with exponentially small probability.
The absolute error in any resulting physical x is at most
(3/2)^N O(2^(4N+2)), which is o(T/L). The ternary residue at depths
j at least the test precision is determined exactly by the last fixed
number of iid letters, regardless of the initial integer. An optional
fixed dyadic test at x is decided by a fixed number of future letters
(each inverse step gains at least one dyadic bit). Enlarge the bit
budget and horizon by these fixed constants; the resulting test is
independent of the past marks and has the odd-Haar mean.

Write Δ=(a²−a)L and let j range through the integers in

    (aL−log T+L^(2/3))/ℓ ≤ j ≤ (a²L−log T−L^(2/3))/ℓ.                (4)

All these j tend to infinity and are less than N. The number is
(1+o(1))Δ/ℓ. For the iid prefix write D_j=log J_j and β_j for its
forward multiplier logarithm and offset. With probability 1−o(1)
uniformly for each such j, |D_j+ℓj|≤L^(2/3)/2 by Chernoff. On this
event integrate first over h: the scaled test location u is
(exp(h+D_j)+β_j)/T and dh=du/(u−β_j/T). For β_j in the fixed mark
support, the full u-support lies inside the source interval by (4).
The conditional integral of uφ divided by Δ is consequently

    Δ⁻¹ ∫ φ(u,β_j,z_j) du + O_φ(1/(TΔ)).                              (5)

On the exceptional D_j event the integral is O_φ(1/Δ) by the same
change of variables and the bounded mark support. Each (β_j,z_j)
converges in law to (F,Z) on every fixed ternary precision, by reversing
the iid letters and using convergence of the real series. Summing (5)
gives the uncapped selected-visit expectation ℓ⁻¹∫Eφ(u,F,Z)du+o(1).

Removing the cap M at the end is legitimate: each contributing visit
requires h+D_j−log T in a fixed compact interval, since β_j is
bounded. For every fixed h, the iid walk D_j has a uniformly bounded
second moment of its total occupation of any translate of such an
interval. After the first visit, a return at lag m requires its
increment in a fixed interval about zero, with exponentially decaying
probability by the negative drift. Summing one- and two-visit bounds
by the Markov property gives the uniform second moment. Thus the
truncation error is O_φ(1/M). Continuous physical-source replacement
on the coupled event costs o(1) by the Lipschitz bound and the o(T/L)
spatial error; on its complement the cap is bounded. We obtain

    liminf ∫φ dΓ_T ≥ (δ/ℓ) ∫Eφ(u,F,Z)du                                (6)

for Γ_T the left side of (1), by first T→∞ then M→∞.

## Saturation fixes the full limit

Use (2) of the [Stieltjes sum rules](STATIONARY_ZERO_FLUX.md) with c=T.
Its right side is the Γ_T integral of

    k_T(u,B)=[(1+1/T)/3] / [(u+B)(u+B+(1+1/T)/3)].                    (7)

The integral tends to δ. The pointwise limiting k is positive and
continuous on u>0, B≥0, with convergence uniform relative to k.
Against the right side of (1) its integral is exactly
(1/2)E log(1+1/(3F))=δ by real stationarity. Thus (6), applied on an
exhaustion of compact sets with continuous cutoffs, exhausts the
entire budget in (7). In detail the finite measures kΓ_T have total
masses tending to δ and dominate k(du/2)law(F,Z) in the lower-limit
test inequality. The latter measure has mass δ. Compact approximation
now gives weak convergence of these weighted measures and asymptotic
uniform tightness, and division by k on compact sets proves (1).
