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
