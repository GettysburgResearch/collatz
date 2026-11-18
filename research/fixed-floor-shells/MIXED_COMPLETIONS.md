# Three signed-cycle itineraries admit the same positive-measure set of ternary lifts

**Proposed, partly computer-assisted.** A mixed pair consists of an odd dyadic integer specifying all forward Syracuse valuations and a ternary integer z testing integrality of all inverse words. Apply the prescribed forward affine maps to z in the ternary integers. After any number j of forward letters, follow any inverse word at its resulting target that is integral in the ternary integers. The slope of the composite is the product of the forward multipliers 3/2^e and the reverse multipliers 2^e/3. Call the pair strict when every such composite has slope greater than one except for the exact cancellation of the entire forward arm, including the empty arm. Thus the only slope-one composite is the identity, with zero translation.

The dyadic coordinates −1, −5 and −17 all give strict pairs at **both** z=0 and z=1. In addition, the set of ternary units z giving a strict pair at **all three** dyadic coordinates has additive Haar measure greater than 0.043. The first dyadic coordinate alone admits a short proof giving at least 5/24 Haar mass among ternary nonunits. None of these dyadic coordinates represents a positive ordinary source. The pairs do imply that no finite family of lowering words or of favorable slope-one translations covers even the finite ordinary positive congruence cylinders approaching these pairs: dyadic forward valuations and ternary legality through any fixed set of word lengths persist under the Chinese remainder theorem.

## The all-one dyadic arm

At the dyadic coordinate −1 the forward valuations are all one, so after j steps the ternary target is (3/2)^j(z+1)−1. Cancel any inverse letters that exactly retrace the last part of the arm. A proper uncancelled forward prefix has slope greater than one. An inverse continuation after complete cancellation is precisely an initial competitor at z.

Otherwise let l≥1 be the residual forward length at the first departure. Its ternary target is −1 modulo 3^l. Through any q≤l letters the same inverse word is therefore legal at the signed integer −1. With its signs reversed, the mirror word follows inverse steps y↦(2^e y+1)/3 from 1. The first letter differs from the only cycle letter and is at least three. Put b equal to the total of e−1 through these q letters. Then y≤2^b, since each step maps y to at most 2^(e−1)y. The relative slope (3/2)^(l−q)2^b exceeds one.

At exactly l letters the composite ternary state is s=2^b(z+1)−y, with y odd, 3≤y<2^b, and b≥2. For z=0 or 1 this is a positive odd integer. A nonempty continuation with inverse multiplier D≤2^(−b) would give a positive ordinary ancestor x<Ds<z+1. At z=0 this is impossible. At z=1 the only possible x is 1, whose positive Syracuse orbit never reaches s≥2^b. At the initial target z=0 no letter is legal, and any nonempty inverse word at z=1 has source x<D, ruling out D≤1. This proves strictness at both specified lifts.

For additive Haar z, the terminal s is itself additive Haar. The [all-depth inverse screen](PREDECESSOR_MINIMA.md) bounds the chance that it admits an inverse continuation of multiplier at most 2^(−b) by 4^(−b). Across all first departures, with residual forward length equal to the first l backward letters, the positive mirror labels y are distinct. Their forward mirror orbits determine the clock and exponents up to first visit to 1. In particular there is no repeated root lap since the first inverse letter departed from the loop. Summing over all odd y≥3 and using 2^b≥y bounds the union by

    Σ_(h≥2) 2^(h−2) 4^(−h) = 1/8.

Here 2^(h−2) counts the odd y in (2^(h−1),2^h]. The initial condition costs nothing on z divisible by 3, leaving good nonunit mass at least 1/3−1/8.

## The three signed cycles

For d=1,5,17 use the following cycles in the positive mirror map V(y)=(3y−1)/2^v₂(3y−1). These determine the forward dyadic arms starting at −d.

| d | successive mirror states before returning | successive valuations |
| --- | --- | --- |
| 1 | 1 | 1 |
| 5 | 5, 7 | 1, 2 |
| 17 | 17, 25, 37, 55, 41, 61, 91 | 1, 1, 1, 2, 1, 1, 4 |

Let d_l be the state after l letters, S_l their valuation total, and P_l=3^l/2^S_l. Every nonempty prefix has P_l>1 by the displayed cycles, including full periods. At z the forward target is P_l(z+d)−d_l. Once shared letters have been cancelled, any remaining nonshared inverse prefix of length q≤l is legal at −d_l. In the positive mirror this gives an off-cycle y whose first entrance to the listed cycle is at d_l and has clock q. The first reverse departure excludes a cycle lap, and the forward mirror orbit of y is deterministic. For inverse word multiplier D and relative slope ρ=P_l D, the product of the q mirror steps gives

    y/ρ = (d_l/P_l) ∏_(i=1)^q (1−1/(3y_i))^(−1),

where y_i is the i-th off-cycle mirror input in inverse order. We claim that y/ρ<d for every such prefix. Every off-cycle label in this basin is greater than d, as may be checked by following just the odd starts below d. Consequently ρ>1, including at any possible end before l.

Here is the finite certificate for the claim. For entrance vertex v and depth i, take m_i(v) to be the smallest positive odd y≤10000 whose first cycle entrance is v in precisely i odd steps, or 10001 if there is none. The checker follows each of those finitely many starting integers until a classified path or a repetition. Then y_i≥m_i(d_l), and an upper bound for y/ρ is

    (d_l/P_l) ∏_(i=1)^l (1−1/(3m_i(d_l)))^(−1).

The largest i with a qualifying small label is 77, 64 and 85 in the three cycles respectively. Beyond that clock, advancing by a whole period p multiplies the bound by (30003/30002)^p/P_p<1. Thus checking through that last index plus one period suffices. The maxima of the indicated rational upper bounds are respectively 3/4, 19/4 and 67/4, all strictly below d. [Exact dictionary and comparisons](check_mixed_cycles.py)

At q=l we have ρ=2^b for the integer b equal to the difference of valuation totals. In particular b≥1, y<d·2^b, and the exact ternary state is s=2^b(z+d)−y. At z=0,1 this is a positive odd integer. A reducing or tying nonempty continuation of multiplier D'≤2^(−b) would supply an ordinary positive odd x<D's≤2^(−b)s<z+d. Follow each odd x<z+d up to its first visit to 1. Subsequent laps multiply the inverse coefficient by 4/3 and cannot cause its first crossing of a smaller value. For every earlier destination s and b≥1 with 2^bD'≤1, reconstruct y=2^b(z+d)−s. The checker verifies that no positive such y has the required entrance phase, depth l, and valuation difference b. The largest positive candidate in these tests is 19. The initial targets 0,1 satisfy the initial screen as above. This proves both explicit lifts for every arm.

## Simultaneous ordinary-unit Haar mass

Use additive ternary Haar measure. At the initial arm the global nonempty inverse screen of multiplier at most one has measure less than 0.517167 by the [certified shortcut first-crossing sum](PREDECESSOR_MINIMA.md). Among units that pass this screen, z≡1 modulo 3 since exponent one immediately lowers at z≡2. The available initial mass of units is at least 2/3−0.517167.

Each residual competitor is tested after l nonshared inverse letters through s=2^b z+c, where c=2^b d−y and y first enters its signed cycle in exactly l steps at d_l. A nonempty remaining word must have multiplier at most 2^(−b) to reduce or tie. If 2^b+c is zero modulo 3 the test cannot succeed on any surviving unit z. Otherwise the affine map of z to s preserves unrestricted additive Haar measure. Thus the cost of this residual event is at most 4^(−b) even before imposing the initial screen. Identical pairs (b,c) across the collection of arms give the same event.

For all odd mirror labels y≤50000 the checker groups the eligible events by this pair, counts 8803 distinct pairs, and certifies that the sum of their weights is less than 1/10 by exact rational arithmetic. For larger y in an arm, each label occurs at most once, since its first cycle entrance determines its depth, phase and word. Its weight is less than d²/y². Summing over all integers y>50000 and integrating x^(−2) bounds the combined remaining cost by (1+25+289)/50000=0.0063. Subtraction leaves mass greater than 0.043. This is a measure statement in the ternary completion. No passage from that Haar mass to the positivity of an ordinary dyadic coordinate is used.
