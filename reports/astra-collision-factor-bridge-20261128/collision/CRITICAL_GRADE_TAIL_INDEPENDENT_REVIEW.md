# Independent review: critical negative-grade tail

Reviewer: collision lower-bound lane. Reviewed UTC: 2026-11-28T11:14:31.099699+00:00.

Source: `research/astra-collision-factor-bridge-20261128/arithmetic/CRITICAL_GRADE_TAIL.md`.

SHA-256: `b1c48fcaaa9aaeb977a8df44b5978451edf48beb05377819de36b326d40f3c5b`.

**Result: the written theorem and one-copy stationary consumer pass independent reconstruction under the named analytic inputs. The required lower bound is still open.** No new Lean certification of the probability limits is asserted.

## Native orbit and normalization checks

The actual finite product identity is exact. If its endpoint is not periodic, no state anywhere in that finite path has repeated. Uniform orbit sparsity therefore bounds the full logarithmic product correction by one absolute constant. At the median clock this bounds the physical window length below by a positive constant, whereas any fixed strictly negative normalized odd-count threshold makes that length tend uniformly to zero. Thus every source in such a negative tail has actually entered a cycle by the observation date, for all sufficiently large cutoffs.

The packing input was checked directly in Leen's retained original `collatz-teeth.tex`, SHA-256 `a58e9bf970aed4700c1338770270ae8bf983278c593f5b5a87351ac473ea4b3a`: the input statement is uniform over orbit sets and translated integer intervals, and its appendix supplies the synchronous-injectivity/parity-cylinder recurrence. Dyadic summation with exponent below one gives the needed absolute reciprocal-product bound. This review does not claim a full fresh Lean rebuild of that external development.

On a fixed cycle, the preentry product remains uniformly bounded, while each complete cycle turn contributes its exact negative logarithmic factor. The final incomplete turn and the cycle endpoint height contribute only a component-dependent bounded error. The source term log(X/n) is tight under the original uniform source law. These facts give the displayed affine relationship between normalized grade and entry time.

The coefficient was independently recalculated: the clock normalization factor gives 2*delta_C*sigma/(log(3)*sqrt(mu))=delta_C/delta_1. Hence the known cycle has scale exactly one. Any other positive cycle has all odd states at least three, giving the stated uniform scale bound strictly below one. The decimal illustrations are not used.

## Infinite-population interfaces

For a fixed cyclic component, tightness of the minimum makes the difference between first-minimum time and cycle-entry time tight. The imported joint minimum/clock law then gives the unnormalized Gaussian component measure. At a strictly negative threshold, the limiting entry-time event is strictly before the observation date, so restricting the grade formula to entered sources loses no mass.

The countable cycle sum is justified by pushing the proper discrete minimum law to component labels. That pushforward converges in total variation. One may alternatively retain all components represented by minima below a fixed cutoff; this is a finite set, and every omitted source lies in the small remaining minimum tail. No uniform estimate over cycle periods or component-dependent errors is assumed. Escaping endpoints are excluded separately by the uniform product bound.

The strict positive gap between the known and other cycle scales forces the known basin density to one if a single negative quantile attains the fair Gaussian lower bound. The separate positive-predecessor input is needed for the final universal, rather than merely density-one, conclusion.

## Stationary selector check

The full grade-and-endpoint total-variation transfer applies to this one union of grade bins. At the median common shortcut clock the one-copy selector is an indicator, and its probability is exactly X/2^h. The selected negative-grade event divided by that same probability equals the native empirical negative tail up to the stated vanishing error. The grade remains attached to the same stationary path; the binomial law before selection cannot be substituted for its law after this rare ordinary selector.

## Review correction retained

The original informal sentence about the exact threshold W<=0 was narrowed after review. The proved statement concerns fixed strictly negative thresholds, with the sequential limit z down to zero taken only after the source limit. The final note explicitly distinguishes that from an unproved boundary argument at the exact finite threshold. This wording change does not affect the main one-quantile theorem.
