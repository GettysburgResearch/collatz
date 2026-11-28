# Independent review: critically damped atomic-anchor obstruction

Reviewer: collision lower-bound lane. Reviewed UTC: 2026-11-28T10:53:26.339834+00:00.

Source: `research/astra-collision-factor-bridge-20261128/arithmetic/CRITICAL_DAMPED_ANCHOR_OBSTRUCTION.md`.

SHA-256: `1c0c1cb0ebf3316a70d2e93db97b2833fa9cdb962845605ab6a29b35a6e39622`.

**Result: the stated self-contained obstruction passes independent reconstruction.** It is a restriction on the specified critically damped, absolutely height-summable atomic certificate class. It is not a Collatz convergence theorem; the infinite-dimensional result has not been formalized here.

## Critical points checked

- The monotone kernel has growth bounded by a constant times three to its valuation divided by a power of one plus that valuation. Monotonicity outside a bounded range converts the valuation bound into the asserted uniform sublinear ordinary estimate. The absolute first-height moment dominates the anchor sum. Since the damping exponent exceeds one, the actual inverse exponent sum converges absolutely.
- The ordinary average of a single kernel is controlled by the exact Haar level sum and a rounding term of order anchor height divided by a power of the logarithmic cutoff. Fixed-cylinder convergence follows by a finite-level truncation and the summable residual level weights.
- The potentially invalid shortcut is explicitly avoided: the affine pushforward need not preserve the first height moment. Instead, the unreduced new height is at least two to the inverse exponent and at most a constant times that factor times the old height. After multiplication by the inverse branch weight, the rounding error is bounded by a constant times old height divided by a power of exponent plus logarithmic cutoff. Summing exponents gives old height times the logarithmic cutoff to exponent one minus the damping exponent, tending to zero. This proves the transferred ordinary-to-Haar limit. The same positive-tail bound works inside any fixed ternary cylinder, and the original moment permits the countable signed anchor sum.
- Ordinary positivity and supersolution inequalities therefore pass to Haar integrals for this explicit class. Haar integral preservation forces an almost-everywhere harmonic identity.
- The correct shrinking-ball scale is the kernel prefix plus the rescaled tail of the level weights. Its dominant term is three to the ball depth times depth to exponent one minus the damping exponent. This scale extracts each atom by dominated convergence, forces nonnegative atomic coefficients, and has successive ratio tending to three. Applying the inverse equation to normalized ball averages therefore gives the mass-preserving atomic stationarity equation, with no subcritical multiplier.
- That stationary positive measure is impossible on the dyadic rational state space. Every nonintegral reduced dyadic denominator exponent strictly increases under every affine branch. Every integer has strictly positive probability of irreversibly leaving the integers, and no nonintegral state enters them. Integer mass is consequently zero; induction removes every positive denominator level. The remaining bounded residue background is excluded by the previously checked exponent-one inverse chain and CRT argument.

## Scope retained

The argument requires an integrable logarithmically damped kernel and an absolute first-height moment. It does not apply to a non-atomic measure, to a series outside this moment class, or to the existing joint potential whose real-distance factor depends on the target. No bound on that potential's unresolved ordinary Green tail is obtained.
