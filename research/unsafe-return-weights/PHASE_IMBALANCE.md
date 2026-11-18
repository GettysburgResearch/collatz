# Adjacent-pair imbalance in every escaping component

**PROPOSED, source-qualified.** Use the positive odd Syracuse map U and let `y_j=U^j(n)` be one hypothetical divergent orbit. Its merger component comprises the odd x that reach some y_j. Define its forward phase k by `U^d(x)=y_j`, `k=j−d`. This is independent of the meeting because the spine does not repeat. Write `X_k` for this class, `P(x)=∏_{i≥0}(1+1/(3U^i(x)))` and `F(x)=xP(x)`. The [critical orbit bound](https://github.com/GettysburgResearch/collatz/blob/4182367ada14d566b5cc1c86daabe6838f88da2e/research/critical-orbit-mellin/CRITICAL_MOMENT.md) bounds P absolutely, and `F(Ux)=(3/2^a)F(x)` for `a=v₂(3x+1)`. The [complete spine clock profile](https://github.com/GettysburgResearch/collatz/blob/b5e28ee338f4c9e5c1694d777d822ad7fa7002ca/research/critical-orbit-mellin/SPINE_CLOCK_PROFILE.md) uses the opposite sign of phase.

Let `A_k=Σ_{x∈X_k}1/F(x)`. Indeed `g_(j−k)(y_j)/F(y_j)` sums exactly `1/F(x)` over the phase-k sources that have met the spine at or before y_j. As j increases these sets exhaust X_k. Thus the A_k are uniformly bounded, strictly positive for k≥0 by the member y_k, and tend to zero as k→+∞ by [the sharp pre-age estimate](SINAI_LOW_ANCESTORS.md). The [unit minorization](https://github.com/GettysburgResearch/collatz/blob/ddae6fe9d1c4686fd10c1d799a78378bba11f2aa/research/native-pressure-20261118/MINORIZATION.md) gives a positive lower bound on A_k for k≤0, by propagation from y₁.

## Signed flow and exceptional pairs

For every integer k,

    A_(k−1)−A_k = Σ_{x∈X_k} [1_{x≡2 mod 3}−1_{x≡0 mod 3}]/F(x).       (1)

Every member of X_(k−1) maps to X_k. The inverses of x with odd exponent contribute multipliers `3 Σ_{a odd} 2^(−a)=2` if x≡2 mod 3. Those with even exponent give 1 if x≡1, and x≡0 has no odd inverse. Summing over X_k establishes (1) with absolute convergence.

Pair the positive odd integers `v=6m+3, u=v+2`. Call them balanced if for some common number d of U-steps their endpoints agree and the totals of their d valuations agree. If one member lies in this component and the pair balances, then both members have the same phase and F-value. Conversely if both share phase and F, a meeting sufficiently far on the spine has equal d and conjugacy forces the total valuations to agree. All balanced pairs cancel in (1). Infinitely many positive k have `A_(k−1)>A_k`, since `A_k>0` and `A_k→0`. Each such phase therefore contains a positive-sign source `u≡5 mod 6` whose smaller partner u−2 never balances. These are infinitely many distinct ordinary pairs. The cancellation is the phase-summed form of the finite-depth signed difference `g_(q+1)−g_q=L^q(g_1−1)` suggested by the native-pressure investigation.

## Lower bound on arm-length discrepancy

Suppose u and v=u−2 are in the same escaping component, their full forward minima are at least B≥3, and they do not balance. Let Δ be the difference of their phases. Assume B sufficiently large for the estimates below. On each dyadic shell starting at B the orbit count is `O(Y^h/(log Y)^(3/2))`, where `h=H₂(log₃2)<1`. Hence

    0 ≤ log(F(x)/x) ≪ B^(h−1)/(log B)^(3/2)    (x=u,v).

The absolute log-ratio of u and v is `O(1/B)` as well. Conjugacy along their merging arms gives

    log(F(u)/F(v)) = ±Δ log 3 + b log 2

for some integer b. A zero form forces Δ=b=0 by unique factorization, hence balanced merger; the form here is nonzero. Its absolute value is at most `C B^(h−1)/(log B)^(3/2)`, so `|b|≪1+|Δ|`. The [Rozier–Terracol statement of Rhin's logarithmic form estimate](https://github.com/GettysburgResearch/collatz/blob/b20190b2220cc3b552615a76362f590fed9f6c41/research/cyclic-shift-distance/README.md) bounds its absolute value below by `c (1+|Δ|)^(−13.3)`. Therefore

    1+|Δ| ≫ B^((1−h)/13.3) (log B)^(3/26.6).                          (2)

The height exponent is about 0.00376274. In arbitrarily far forward exceptional phases, the smaller partners must either lie outside the escaping component or exhibit unbounded phase discrepancy (along the same-component subsequence). Indeed, ahead of sufficiently high phase no orbit visits any fixed finite set: each such point has a fixed phase, and phase increases forward. If discrepancies stayed bounded, both minima would tend to infinity, contradicting (2).

There is also a finite-arm tradeoff. If *any* two unbalanced arms of lengths at most L from adjacent odd u,v meet, and their states before that meeting are all at least B≥3, then

    (1+|d_u−d_v|)^13.3 (1+L) ≫ B,        L ≫ B^(1/14.3)−1.                (3)

Use their finite products in place of P. Each has log correction at most `L/(3B)`. If `(1+L)/B` is bounded below by a sufficiently small fixed constant, (3) follows immediately after adjusting constants. Otherwise the form is small, its binary coefficient is `O(1+|d_u−d_v|)`, and Rhin gives (3). A zero form implies both d and total valuations are equal, excluded by the arm hypothesis. This argument needs no infinite escaping extension. Thus at comparable source heights X and `B≥X^η` for fixed η>0, an unbalanced physical merger requires polynomial time; a polylogarithmic-time unbalanced merger must dip to at most a polylogarithmic height.

## What predecessor density supplies

A unit in an exceptional pair can have positive lower predecessor density while the adjacent partner has no odd inverse, since it is divisible by 3. Hence there is no positive-length U-pullback of the *pair* terminating simultaneously at these two targets. Typical balanced adjacent sources in the unit member's basin may both travel to that same member. Separate basin density and typical balanced synchronization do not assert a synchronized pullback to the distinct pair. For example `(3,5)` does not balance: both reach 1 at odd clock two with valuation totals 5 and 6, which retain their difference thereafter (the clock-one endpoints differ). The sibling lift `z↦16z+5` changes the first valuation by four while preserving the next odd value, so the two units `(53,85)` also do not balance. These examples are on the verified 1-cycle basin. An argument excluding the high exceptional signed flow in (1) remains open.
