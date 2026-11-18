# The modulus scale for the two clocks at the global minimum

**Proposed, with two imported synchronization and clock estimates.** Draw n uniformly from {1,…,X}. Let m be the minimum of its whole positive orbit, τ the number of shortcut steps to its first visit, and J the number of odd steps before that visit. Use either coordinates (τ,J) or the even and odd counts (τ−J,J). For each positive integer q, let Δ_X(q) denote the total variation distance (supremum over events) between the empirical joint law of (m,τ mod q,J mod q) and the product of the empirical law of m with the uniform law on (Z/qZ)².

Write c=log₂3, L=log X (natural logarithm), and take consecutive continued-fraction denominators s,t of c such that s≤L^(1/4)<t. Define

    D(X) = max(s, √L/t).

For all large X one has Δ_X(q)≪min(1,q/D(X)). Conversely,

    q/D(X) → ∞    implies    Δ_X(q) → 1.                              (1)

Thus the two clock residues have their uniform product law up to an error tending to zero for q=o(D(X)). Above that scale a single group character distinguishes the empirical law with probability tending to one. The bounds apply on every fixed proportional source interval of positive length. They leave the regime q comparable to D(X) open.

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
