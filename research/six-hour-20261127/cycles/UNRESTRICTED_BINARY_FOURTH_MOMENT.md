# Uniform fourth-moment bounds in the full two-layer binary language

Use the coordinates and notation of FOUR_BRIDGE_BINARY_CYCLE_BOUND.md, but allow every bit in either layer subject to the binary gap transition. Thus any real width W<2 is covered; a positive density of forced sites is no longer assumed. For every long segment of a near-critical mechanical schedule, uniformly in its intercept, in its prescribed initial and final bit, and in 1.584961≤θ≤1.584964, its ordinary numerator four-sum energy E_a satisfies

$$
 c\,3^{(201/200)a}\le E_a\le C\,3^{(5031/5000)a}. \tag{1}
$$

In fact the same energy bounds hold in the language in which both layers are always eligible. A particular narrower word can belong to a smaller subfamily with lower energy. The positive lower bound (1) concerns the population of the full unforced path class, not the number of collisions in any arbitrarily selected subset of paths.

Cut the circle at f>49/50 as in the width-99/50 certificate. Now such a visit is merely a cut; the four paths need not be zero there. Let M_w be the nonnegative 3×3 matrix propagating the three grade counts over the return itinerary w. For v=(1000000,1866354,321361), direct multiplication gives the following three images:

| n | M_w v |
|---:|---|
| 12 | (576471858687,1075900511942,185255645195) |
| 41 | (45793364866920864068568821,85466625927097838944519922,14716207263618642277910810) |
| 53 | (26398586022831161298312507713234,49269104447211974349417481369986,8483479309882987817303195923417) |

Every row satisfies the componentwise bounds 3^{201n/200}v<M_wv<3^{5031n/5000}v. The exact rational circle catalogue and integer powers are replayed by full_bridge_pressure.py. Positivity composes these inequalities over any order of successive returns. An incomplete end has bounded length. Moreover both mechanical letters occur in any sufficiently long fixed-length fragment, and the product of a one and a two (in either order) is strictly positive on all three grades. Thus even from either single fixed entrance (all zeros or all ones), after a bounded number of letters the count vector dominates a fixed positive multiple of v. The same positivity at the other end bounds either fixed diagonal terminal from below. In this unforced class the equal-pair sums are exactly the four-copy ordinary numerator equalities by reverse ternary peeling, with no digit carries. This proves (1).

The upper bound replaces γ in the unnormalized four-segment proof. On any sequence of primitive positive rational binary cycles with W<2, P→∞, and log d=o(log P), this gives

$$
 \liminf \frac{\log(dX)}{\log P}\ge 15000/5031=2.9815\ldots .
$$

In particular the necessary one-sided approximation exponent for ordinarily integral cycles in the full class is at least this value. This bound still falls below the quoted logarithm-ratio exponent 3.

The lower estimate identifies a limitation of this particular use of the ordinary zero event. Arbitrary deterministic cut locations and fixed single-bit entrance and exit conditions still leave the full unweighted segment's zero-event count above 3^{1.005a} at long durations. Thus replacing the phase-uniform upper bound by a stationary average of the same counts, or merely varying segment boundaries with bounded end loss, cannot force the ingredient E_a≤3^{(1−δ)a}. The inequality does not exclude cancellation among the four actual quantized segment laws, stronger joint constraints on phases of a single cycle, weighting according to an independently proved restriction, or another proof architecture. Paper 145 §12 gives a separate population-based floor for independent-segment methods in general. The explicit obstruction here uses the full three-coordinate transfer of this particular binary model.

The fixed-width theorem uses the projection onto the first coordinate at each visit; retaining all three is precisely the distinction responsible for the gap. No irrationality result is used in (1) or its near-cubic phase lower bound, and no complete exclusion in the unrestricted two-layer class follows.
