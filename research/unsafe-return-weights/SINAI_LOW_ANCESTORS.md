# Low ancestors account for the linear part of the ordinary Sinai density

**PROPOSED, source-qualified.** Let `U(x)=(3x+1)/2^a` on positive odd integers, with `a=v₂(3x+1)`. Write `g_q(y)=3^q μ_q(y mod 3^q)` for the density of the q-step geometric Syracuse offset on the ternary quotient, with `g_0=1`. Define `J(x,d)=3^d/2^(a₁+⋯+a_d)` along the actual d-step orbit. All floors below concern ordinary positive states.

Let ε(B) be the upper logarithmic density among **all positive integers** whose ordinary Collatz orbit never enters `[1,B]`. Tao's almost-bounded-minimum theorem gives ε(B)→0. Indeed, otherwise for increasing integer B one could choose successively dominant cutoffs with a fixed positive logarithmic proportion avoiding B. Taking an increasing step function f equal to each such B up through its cutoff would contradict the theorem for f tending to infinity. Accelerating to odd states preserves eventual entry into `[1,B]`.

Fix 1<r<2 and θ=1−1/r. The input from [the harmonic capacity proof at d38541225127acf076879dfb180140e8491ffaa1](https://github.com/GettysburgResearch/collatz/blob/d38541225127acf076879dfb180140e8491ffaa1/research/native-pressure-20261118/ANTICHAINS.md) is that for any reachability antichain A of positive targets prime to 3, the lower natural density of the union of their ordinary predecessor basins is at least `c_r (Σ_A 1/x)^(1/θ)`. The comparison of lower natural with upper logarithmic density uses partial summation. The capacity proof relies on Mazur's Proposition 3.1 and Tao's Proposition 1.14. [Tao, Theorem 1.3](https://arxiv.org/abs/1909.03562).

## Finite low-source formula

Let y be nonperiodic and odd with its entire forward orbit strictly above B. Let D be the largest U-distance from any odd state ≤B to y, or zero if there is none. Let L be those odd ancestors ℓ≤B whose orbit segment after ℓ and up to y contains no further state ≤B. Write d(ℓ) for the distance from ℓ to y. For **every** q>D,

    0 ≤ g_q(y) − Σ_{ℓ∈L} J(ℓ,d(ℓ)) g_{q−d(ℓ)}(ℓ)
      ≤ C_r ε(B)^θ y.                                               (1)

For the exact integer representation, a word of q positive exponents and total A has affine endpoint `(3^q x+u)/2^A`. Its offset represents y modulo 3^q precisely when its inverse source `(2^A y−u)/3^q` is integral. Recover the itinerary backwards: the last exponent gives `(2^a y−1)/3`, an odd positive integer when integral, with exact valuation a in the forward map. The full congruence gives divisibility at every stage by successively peeling the terminal digit. Thus `g_q(y)=Σ_{U^q x=y} J(x,q)`, with `J(x,q)≤y/x`. All summands are positive. Paths containing a low state partition by their last low state ℓ; multiplicativity gives the sum in (1).

Let A consist of the remaining sources. All of their future states exceed B. They form an antichain: if one reached another at positive distance, y would return to itself. Replace each x divisible by 3 with the unit `4x+1`, which is odd and has the same U-successor. The resulting set A′ is still in the inverse q-level (q≥1) and all its members have entire futures above B. No odd state ≤B reaches a member, since this would give a low ancestor of y at distance at least q>D. No even state ≤B can reach one either, by initial halvings. Therefore every predecessor of every member of A′ avoids `[1,B]` forever. Each unit target in A′ has at most one replaced companion, whose reciprocal is at most five times its own. The capacity inequality gives

    Σ_{x∈A} J(x,q)/y ≤ Σ_{x∈A} 1/x ≤ 6 Σ_{z∈A′} 1/z
                        ≤ 6 c_r^(−θ) ε(B)^θ.

This proves (1), including infinite inverse levels by monotone convergence.

## Persistent density along an escaping spine

Suppose `y_j=U^j(n)` is divergent. For each fixed B, eventually its future exceeds B and the set L in (1) stabilizes: the finitely many low states that ever enter the spine have all joined by some finite j, and all their subsequent low visits end after finitely many steps. For every such j, the unaccounted part of `g_q(y_j)/y_j` is at most `C_r ε(B)^θ` for all q beyond the explicitly defined D, uniformly in j. In particular it tends uniformly to zero as B grows in this order of limits. There is no estimate here allowing q≤D in (1).

The finite sum itself can persist. In fact `g_{q+j}(y_j) ≥ J(n,j) g_q(n)`, and `y_j/J(n,j)=n ∏_{i<j}(1+1/(3y_i))`. This product has a finite positive limit along a divergent orbit by the reciprocal-orbit bound in [the critical Mellin proof](https://github.com/GettysburgResearch/collatz/commit/f702a03). Hence any positive limsup of `g_q(n)` propagates a linear-size subsequence of density values to every y_j. Bounding the residual in (1) supplies no decay for this inherited mass.

## A sharp age threshold on a divergent spine

In fact a true sublinear pointwise estimate holds before the age of the spine. For every divergent odd orbit `y_j=U^j(n)`,

    lim_{K→∞} sup_{j≥q+K, q≥0} g_q(y_j)/y_j = 0.                  (2)

Fix B. There are finitely many odd s≤B. For each whose orbit ever meets the spine, fix one meeting `U^h(s)=y_i`. Choose I larger than all these i, all i−h, and the indices of every visit of the spine to `[1,B]`. Enlarge I if necessary so that no point in any of the finitely many pre-meeting segments is y_j with j≥I. If j−q≥I, all of the following hold. No U-path of length q to y_j can contain a low state, since the distance of any such s to y_j is `h+j−i>q`. If a low state reaches any member of the q-level, that member must be `y_(j−q)`, since the last q steps from the low state all occur after its chosen meeting. These observations also cover all the unit aliases from the proof of (1), for q≥1. Remove the single possible unit exception from A′. Every predecessor basin remaining avoids `[1,B]` forever. The previous capacity proof now gives

    g_q(y_j)/y_j ≤ 6/y_(j−q) + C_r ε(B)^θ.                         (3)

For q=0 the left side is exactly `1/y_j`, so the estimate continues to hold. Since `inf_{i≥K} y_i→∞`, take K→∞ and then B→∞ to get (2).

At q=j the inclusion of n in the inverse level gives `g_j(y_j)/y_j ≥ 1/[n P_∞(n)]` for all j, where `P_∞(n)` is the finite correction product above. For any fixed lag k≥0 the same argument from y_k gives `g_{j−k}(y_j)/y_j ≥ 1/[y_k P_∞(y_k)]` for j≥k. Thus diverging lag in (2) is necessary. The [uniform unit minorization at ddae6fe](https://github.com/GettysburgResearch/collatz/blob/ddae6fe/research/native-pressure-20261118/MINORIZATION.md) gives `g_s(y_1)≥c` over s≥1, since y₁ is a ternary unit. Propagation from y₁ therefore gives a positive lower bound on `g_{j+k}(y_j)/y_j` simultaneously for every j≥1 and every k≥0. The q=j sharpness is independent of that additional analytic input.

Telescoping (2) against the q=j lower bound gives a necessary temporal discontinuity. There exist fixed K,c>0 for this spine such that, for every sufficiently large j, some `j−K≤s<j` satisfies `|g_(s+1)(y_j)−g_s(y_j)|≥c y_j`. Consequently uniform decay of `sup_y |g_(s+1)(y)−g_s(y)|/y` on ordinary odd units would exclude divergent orbits. A Haar integral estimate for these increments does not provide this uniform ordinary-point control.

## Width of all large ordinary density values

For any reachability antichain Y of nonperiodic odd targets and any independently chosen integer depths `q_y≥1`, the unitized inverse levels used above form one antichain. Indeed, if two sources from different levels were comparable, their targets would lie on the same forward orbit and would be comparable. Both unitization and the factor-six reciprocal bound operate within the chosen level of each target. The capacity bound with the union of all basins of Y now gives

    Σ_{y∈Y} sup_{q≥1} g_q(y)/y ≤ C_r lower_density(⋃_{y∈Y} P(y))^θ.   (4)

To handle the suprema, approximate each from below on a finite subset, then take the supremum of all such sums. In particular the set of nonperiodic targets satisfying `sup_q g_q(y)/y>δ` has reachability width at most `C_r/δ`. It is a union of at most `⌈C_r/δ⌉` chains: apply finite Dilworth to successive finite subsets, then use compactness of the finitely branching tree of compatible chain colorings. For singleton Y, (4) supplies an upper bound paired with the [lower Cesàro bound at c2c25da](https://github.com/GettysburgResearch/collatz/blob/c2c25dabf3b837a223a46310d0092ef32e2119dd/research/native-pressure-20261118/ORDINARY-DENSITIES.md), which bounds the liminf of the normalized depth averages below by a constant times the lower density of P(y).
