# Coordinator review of the final analytic interfaces

28 November 2026. **VERIFIED AS WRITTEN / SOURCE-QUALIFIED at the scopes
below; full Collatz closure remains GAP/BLOCKED.** The scientific
assessment is in [FINAL_ASSESSMENT.md](../../research/astra-full-proof-20261128/FINAL_ASSESSMENT.md).
This report records reconstruction and computation, not an analytic
formalization claim.

## Reviewed additions after checkpoint 4

### Whole-source stationary trace

The coordinator derived and checked the complete-source bijection
in ACTUAL_SOURCE_STATIONARY_TRACE.md, beginning with the pinned
PR217 fixed-fibre integer-window identity. The full ternary
congruence makes the reconstructed source integral; reverse
binary induction recovers its unique actual word. The strict
lower and weak upper real endpoints select exactly N integers.
Summing all endpoints and grades before comparison leaves only
the symmetric difference of two length-N source intervals.
Consequently the error has no factor counting fibres.

When N is at most 2 to the word length, the endpoint lattice
spacing makes the selected endpoint unique, including the
equal-length boundary case. Its exact conditional probability
does not bias the seed law but can bias the future word. The
escape lane independently reconstructed these points, including
grade zero and arbitrary correlations between the seed's real
and ternary coordinates. The conditional mean sign remains OPEN.

The closing frontier read at PR217 head
e9c31f56099c9f7df07ed2ecb82a93883d7a74bd found its concurrent
whole-law aggregation and exact one-copy normalization in
STATIONARY_COLLISION_CONSUMER.md. The coordinator read that
argument, checked the shared-window coupling, and added
explicit overlap credit to the scientific note. Its logarithmic
error follows by optimizing the fractional-moment parameter
already displayed here. No exclusive priority is claimed for
the common aggregation.

### Positive rational kernel and fixed-floor absorption

The coordinator reconstructed the kernel normalization as a
partition of positive integer numerators by the geometric even
run before each formal odd departure. The separate root replay
checked 84 mesh grids and 126315 atoms with their normalizations.
No endpoint measure was substituted for the original source
measure.

For the new absorbing kernel, the coordinator and both other
lanes independently checked the two-power majorant at floor32.
The exact rational upper bound
1810432 / 1845585 < 99 / 100 leaves the stated auxiliary-power
margin. The leading logarithmic derivative is -log(4/3).
The original source normalization is retained.

For the stronger floor1 survival estimate, the fair prefix ends
strictly inside the actual numerator precision: the remaining
budget is (log2(3)-5/4)h+O(1). Both geometric-clock deviations
have a positive multiple of h as margin. Monotone domination
from the deterministic real start N avoids assuming the
initial size is independent of its parity word. In the killed
drift, choose the compact threshold first, then the additive
constant, and finally a positive contraction margin. This
order removes the potential circularity in the drift constants.
Future-independent fair innovations justify iteration after the
initial good event is bounded. The subcritical proof uses a union
bound for the source size and prefix deviation events.

The complete-component flux identity requires equality of the
ordinary mark on each edge in both directions. The final wording
states this as a union of complete components. A merely forward
invariant subset would be insufficient. The floor1 control is
an actual positive rational/ordinary discrepancy, not a symbolic
countermodel.

### Uniform small widths and the marked wide-width argument

The root checked the renewal strip bound directly by first
entry and exponential return estimates. Expanding the intercept
power into suffix products gives its weighted version. Splitting
at a logarithmic suffix length, coupling to the stationary real
intercept, and summing the uniform strip bounds gives an
all-denominator microscopic estimate. This avoids a factor
proportional to the full denominator clock.

For the first-repeat refinement, each extra integral inverse
step requires a prescribed parity of a fresh geometric run,
with conditional probability at most 2/3. Conditioning on the
last such runs leaves one translated strip for the independent
prefix. This proves the required exponential moment in the
integrality depth. Holder's inequality gives the stated small
width exponent; its constants are uniform for all sufficiently
large floors at fixed parameters. The mass lane independently
reconstructed this argument.

The wide-width argument is narrower than a general theorem for
history labels. For each fixed word every prior state increases
affinely with the candidate ordinary endpoint, so the whole
prefix floor is one lower cutoff. At a short common ordinary
clock, starts on the retained large octave cannot yet have
crossed the floor. The future-floor label is therefore a true
terminal-state test, to which the pinned PR215 total-variation
bound applies by subtraction of prefixes. The coordinator
reread its displayed equation (3) and proof at
4f33ecc2de6f0ccf605a68c28da5abea0348e47b.

The correction-product replacement error is
O(R^2 a^(-1-theta)(1+R/Y0)); choosing 2delta<theta makes it
o(1/a). The new fixed-floor absorption estimate controls the
final rational mass without the earlier polynomial endpoint
loss restriction. Both other lanes independently checked this
interface. Intermediate widths remain OPEN. A moving future
minimum argument alone does not remove a cycle with one fixed
minimum.

The all-fates finite observable stops the correction at the
first repeated state and uses the finite test that 1 has not
been hit by the evaluation date. Every bad ordinary source
retains positive weight by the cited distinct-segment bound.
Before the rational state becomes integral it cannot repeat;
the number of possibly omitted ordinary factors is bounded by
the initial numerator's ternary valuation. A later elementary
proof bounds the first d completed odd departures using the
actual numerator's binary precision. The affine intercept
is at least one half, so a small actual slope directly makes
the correction product exponentially small. Its combination
with the geometric tail of the ternary valuation proves an
exp(-c h^2/k) reference bound. This benchmark needs neither
the recursive entrance clock nor stationary real regularity.
This consumer covers cycles and escape. Its required
ordinary-to-rational comparison is OPEN.

## Actual additional finite replay

The coordinator ran
research/astra-full-proof-20261128/descent/check_survival_ladder.py
after importing the final structural note:

> 104 exact rational rung comparisons passed across 4552 occupied word instances

The checker includes physical future-floor observations, the
first-repeat correction, the inverse-integrality depth, and
the fixed-word lower-cutoff identity. This is a finite check
of exact formulas, not of the asymptotic estimates.

Earlier actual replays and the fresh eight-module Lean receipt
remain in the checkpoint reports. The separately recorded
[clean complete checkout receipt](FINAL_CHECKOUT.json) identifies
the exact validated scientific commit and tree; all five
required commands passed. The [source manifest](FINAL_SOURCES.json)
freezes the scientific files at that commit. The publication adds
these process receipts after validation. The receipt's scope is
repository integrity, not mathematical verification.

## Dependencies and priority

The source pins retain the initially inspected frontier and
the later explicitly reread PR217 and PR219 heads. The joint
stationary window construction credits PR217. The physical
harmonic boundary credits the earlier PR215 Mellin argument;
the fixed-shortcut-clock formulation does not claim to
originate that strategy. The adjacent-coalescence input in
PHYSICAL_HEIGHT_BOUNDARY.md is credited to Said Duran.

No outside full analytic Lean development was rebuilt.
Outside compile reports are retained as such. No conclusion
in this review upgrades a finite formal lemma into the
unproved analytic comparison.
