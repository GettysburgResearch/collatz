# The modulus scale for the two clocks at the global minimum

**Proposed, with two imported synchronization and clock estimates.** Draw n uniformly from {1,…,X}. Let m be the minimum of its whole positive orbit, τ the number of shortcut steps to its first visit, and J the number of odd steps before that visit. Use either coordinates (τ,J) or the even and odd counts (τ−J,J). For each positive integer q, let Δ_X(q) denote the total variation distance (supremum over events) between the empirical joint law of (m,τ mod q,J mod q) and the product of the empirical law of m with the uniform law on (Z/qZ)².

Write c=log₂3, L=log X (natural logarithm), and take consecutive continued-fraction denominators s,t of c such that s≤L^(1/4)<t. Define

    D(X) = max(s, √L/t).

For all large X one has Δ_X(q)≪min(1,q/D(X)). Conversely,

    q/D(X) → ∞    implies    Δ_X(q) → 1.                              (1)

Thus the two clock residues have their uniform product law up to an error tending to zero for q=o(D(X)). Above that scale a single group character distinguishes the empirical law with probability tending to one. The bounds apply on every fixed proportional source interval of positive length. The final section treats the intermediate ratios using a separate singularity result.

The upper bound uses Leen's quantitative estimate on the coalescence of consecutive sources. The lower bound uses his diffusive tightness at the first global minimum, tightness of the minimum and the bounded terminal residue. His earlier histogram theorem identified continued-fraction near-periods in a single total stopping clock on the basin of 1. His Brownian theorem also proves independence of the global minimum and the diffusively rescaled descent clock. Here the events are discrete and resolve both clock coordinates modulo a growing q. [Synchronization estimates](https://doi.org/10.5281/zenodo.23268751) · [Brownian motion in Collatz orbits, main theorem, clock dictionary and terminal residue](https://doi.org/10.5281/zenodo.23252395) · [Stopping-time histogram, Theorems A–C](https://doi.org/10.5281/zenodo.23252397)

## Upper bound at the continued-fraction scales

For any convergent denominator H of c, the first H points of the rotation by c approximate every point modulo one to O(1/H). Indeed the matching rational rotation is a full 1/H mesh, and each of those points moves by less than the reciprocal of the next denominator. Consequently every bounded real z has an approximation i log 2+j log 3 with |i|+|j|=O(H) and error O(1/H), just as in (5) of the [growing-clock proof](GROWING_CLOCKS.md), using j for the rotation index. Its measure-valued argument, with the minimum retained as an auxiliary label, now gives the bound

    Δ_X(q) ≪ q (H/√L+1/H)                                              (2)

whenever the right side is small. Indeed qH=O(√L) then keeps every intermediate evaluation within the original synchronization range. Else use Δ_X≤1. For H=s the right side is at most 2q/s and for H=t it is at most 2qt/√L. Taking the better bound proves the assertion.

## A detecting character above that scale

The exact affine clock identity is

    τ = cJ + log₂(n/m) + R(n),
    R(n) = Σ log₂(1+1/(3u)),

where the sum is over the odd u before the first minimum. It follows by multiplying the factors of the forward shortcut steps. Put d=log(4/3). The cited Brownian theorem gives τ=2L/d+O_P(√L), m=O_P(1), and the residue is bounded; tightness alone suffices for R. Here O_P is boundedness in probability after the indicated normalization. Since log n=L+O_P(1), the identity and (2/d−1/log 2)/c=1/d imply J=L/d+O_P(√L). These tightness statements transfer from [1,X] to a fixed proportional subinterval by the positive lower bound on its relative size, or by changing X by a fixed factor.

Take the convergent p/s, so that |sc−p|<1/t. The character (τ,J)↦exp(2πi(sτ−pJ)/q) has order q since p and s are coprime. Under the product reference measure it is uniform on the qth roots of unity. Under the actual measure, subtract the deterministic center s log₂ X+(sc−p)L/d from its numerator. The remaining real quantity is

    s[log₂(n/X)−log₂m+R(n)] + (sc−p)[J−L/d]
                 = O_P(s+√L/t) = O_P(D(X)).

If q/D(X)→∞, a sequence of arcs whose angular lengths tend slowly to zero captures actual mass tending to one. The uniform mass on those arcs is at most their normalized length plus 1/q, which tends to zero. Their inverse images give (1). This lower bound already holds after forgetting the minimum coordinate.

## Extremal exponent

Always D(X)≤L^(1/4). At X=⌈exp(s⁴)⌉ along the convergent denominators, D(X)∼L^(1/4). Thus the exponent 1/4 is attained along an infinite sequence of source cutoffs, with both asymptotic conclusions above. Rhin's bound gives t≪s^13.3, hence D(X)≫L^(5/143) for every X. More generally, if log₂3 has irrationality exponent two, t≤s^(1+o(1)) and D(X)=L^(1/4+o(1)) throughout. The continued-fraction statement and the two unconditional bounds require no assumption about that irrationality exponent.

## The critical ratios after identifying the residue law

The [singularity theorem for the natural terminal residue](../terminal-residue/SINGULAR_FIBRES.md) settles the remaining zero-distance question:

    Δ_X(q(X)) → 0  if and only if  q(X)/D(X) → 0.                       (3)

This does not give a closed form for the distance at a finite positive limiting ratio. To prove necessity it suffices, by (1), to pass to a subsequence with 0<ε≤q/D(X)≤C. Take a further subsequence with s/q→a and (sc−p)√L/q→b, both finite. Since D(X)→∞, q→∞. The event m=1 has positive limiting probability by ordinary predecessor positivity. On this cell, let V denote the limiting terminal residue. By Leen's joint terminal Brownian theorem, (J−L/d)/√L tends to a centered Gaussian G of strictly positive variance, independent of V. This follows also from the exact clock dictionary and the endpoint theorem since the bounded R contributes o(1) after normalization. In the same limit n/X is uniform on [0,1] and independent of (G,V): difference the cumulative laws with source cutoffs uX, first for each fixed 0<u≤1. Their logarithmic center changes by O_u(1), and their conditional cell frequency tends to the same positive value. For a fixed proportional shell the uniform variable is instead uniform on its defining real interval.

For every fixed nonzero integer l the modulus of the expectation of the lth power of the detecting character conditional on m=1 thus converges to

    |E exp(2πi l b G)| · |E exp(2πi l a log₂ U)| · |E exp(2πi l a V)|,

where U is the corresponding uniform real variable. The deterministic phase omitted here has modulus one. The Gaussian factor is nonzero. The uniform-variable factor is also nonzero: integrating u^(iξ) gives an endpoint difference of terms with different absolute values, divided by 1+iξ. If a=0 the last factor is one. Otherwise V modulo 1/a has a singular distribution, so uniqueness of Fourier coefficients on the circle supplies some l≠0 for which the last factor is nonzero. Under the product reference, the same lth character expectation equals zero once q>|l|, since the primitive pair (s,p) gives a character of order q. The positive mass of the m=1 cell now precludes Δ_X(q)→0. The subsequence argument proves (3), and shows that for every ε>0 the distance is bounded away from zero when q≥εD(X) at sufficiently large X. [Leen, joint clock and residue theorem](https://doi.org/10.5281/zenodo.23252395) · [Positive density of the predecessor basin](../external/mazur-2026/README.md)

## Broad logarithmic sampling has a different sharp scale

Give n∈[X^u,X] probability proportional to 1/n, with fixed 0<u<1, and use its own empirical minimum as the reference marginal. For this sampling the joint clock distance tends to zero **if and only if** q=o(√log X). It tends to one if q/√log X→∞.

The upper bound O_u(q/√log X) follows from the logarithmic translation argument in [the growing-clock theorem](GROWING_CLOCKS.md). For the converse use the integer clock difference Z=τ−2J. Let c=log₂3, d=log(4/3). The exact dictionary gives

    Z=(c−2)(J−log(n)/d)−log₂ m+R(n),

since (c−2)/d=−1/log 2. The natural-source Brownian theorem gives (J−log n/d)/√log n tending to a nondegenerate centered Gaussian G, while the other two terms are tight. Under this logarithmic sampling, log n/log X tends to U uniform on [u,1], independent in the limit of the standardized Gaussian. To verify the change of sampling, for a bounded continuous test of the standardized variable use partial summation on [X^v,X^w], u≤v<w≤1. Its natural cumulative mean tends to the Gaussian expectation at every increasing cutoff, hence its reciprocal-weighted sum divided by log X tends to (w−v) times that expectation. Approximating tests of the logarithmic scale by steps gives the claimed joint convergence. The same partial summation transfers tightness of the other terms. Thus Z/√log X tends in law to (c−2)√U G.

The projection (τ,J)↦Z is surjective modulo q. If q/√log X tends to any finite nonzero l, the first Fourier coefficient of Z modulo q tends to the characteristic function of the centered scale mixture at 2π/l, which is strictly positive. The product reference has zero coefficient. If q/√log X→∞, tightness shows that Z modulo q is concentrated on an arc of vanishing relative length. Subsequence extraction gives the necessity assertion for arbitrary integer q(X). These harmonic-window conclusions use the source Brownian and synchronization theorems and do not require the real-fibre singularity input.

For the natural proportional-window exponent, there is a sharper uniform consequence than the explicit Rhin bound used earlier. Chudnovsky's recent Theorem 11.1, as stated for positive multiplicatively independent rational bases, gives irrationality exponent at most three for log₂3 (equivalently its reciprocal). Then t≪_ε s^(2+ε) for consecutive convergent denominators. Combining this with the exact D(X) gives D(X)≫_ε (log X)^(1/6−ε). This last numerical strengthening imports the preprint as stated; we did not rebuild its reported formal verification. The continued-fraction criterion itself uses the denominators directly. [Chudnovsky, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)
