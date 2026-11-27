# Independent root review, six-hour continuation

This is a working review ledger. It records reconstruction by the root agent,
not agreement among the research agents. A written proof review, a source
inspection, a finite control and a Lean replay are different kinds of evidence.
The final fresh-checkout replay is recorded separately.

## Shared-background complete denominators

Reviewed `arithmetic/SHARED_BACKGROUND.md` at the first checkpoint. The asserted
scope fixes the number `r` of copies of one ordered valuation background, permits
all background and marker exponents to vary, and lets its length tend to infinity.
It does not cover an unrestricted cyclic word with a growing number of different
background pieces.

The root reconstructed the following steps independently.

1. Every block has the same numerator intercept `E`, regardless of its last
   marker exponent. Composition therefore gives the full numerator `E H(P)`
   and denominator `D`, without discarding any common factor. The estimate on
   `E` uses every remaining background exponent being at least one.
2. Fourier inversion on the fixed marker vector gives at least two nonzero
   frequencies unless all markers are equal. This also permits a nonprimitive
   marker pattern; it does not assume that every Fourier coefficient survives.
3. The outside-`S` gcd estimate actually needed is Theorem 1.12(a) in the authors'
   [preprint](https://arxiv.org/pdf/1903.03876), equations (5)–(6). Its statement
   was read directly. It has a finite union of translated proper algebraic
   subgroups as its exceptional set and has no nonvanishing-at-the-origin
   hypothesis for this outside-`S` assertion.
4. Along an alleged violating sequence, `k` tends to infinity. At a place above
   three the variable `x` has valuation proportional to `k`, whereas all marker
   variables have valuation zero. A fixed subgroup character involving `x`
   therefore cannot be constant on this sequence. Every remaining exceptional
   character imposes a nontrivial affine integral relation on marker exponents.
   Restricting to that lattice strictly lowers its rank. On each fixed lattice,
   a fixed left inverse bounds the new coordinates by the original height scale.
   A restricted Fourier polynomial that is nonzero on the retained sequence
   cannot vanish identically. This makes the finite descending argument valid.
5. At an outside-`S` prime, write the selected factor orders as `a_j` and the
   numerator order as `b`. The inequality
   `sum a_j - sum min(a_j,b) <= max(0,sum a_j-b)` is in the required direction.
   Thus shared primes between cyclotomic factors cause no overcount in the
   denominator lower bound. All selected factors are units above two and three.
6. Every archimedean conjugate has modulus at least `R-P`. The lower bound for
   this positive difference follows from the log-form bound in
   [Lagarias, Lemma 2.2](https://arxiv.org/pdf/math/0512006) in the near-critical
   range, and directly outside that range. The gcd loss is retained as
   `o(k+s+T)`, not silently replaced by `o(k)`. The two height regimes in the
   note then imply its stated length-scale consequence.
7. For two unequal markers, subtracting the two exact integer-numerator
   equations gives the displayed divisibility by `P+N`. Reducing the exponent
   of `N` modulo the marker difference keeps both arguments in a fixed
   two-dimensional `S`-unit group and with height `O(k)` in the bounded-difference
   regime. Their three-valuations prove multiplicative independence.
   [Corvaja–Zannier, Proposition 2](https://arxiv.org/pdf/math/0311030) was read
   directly. The separate long-gap estimate handles the complementary regime.

No gap was found in this reconstruction of the stated written theorem. Its
threshold is ineffective, the external gcd and log-form results have not been
formalized in this repository, and no claim of arbitrary-cycle exclusion follows.
The finite Lean interfaces and numerical controls remain subject to the final
independent replay.

## Reciprocal departure operator

The root independently derived and checked the correction in
`synthesis/RECIPROCAL_OPERATOR.md`. For the unaccelerated map, the product of
three successive positive states is at least eight. This proves the norm bound
for the operator whose departure weight is `1/n`, independently of convergence.
The cycle eigenvector gives its exact spectral radius `1/2` on the stated
weighted spaces after the written compactness and eigenvector-bootstrap steps.

`ReciprocalOperator.lean` compiled with warnings as errors and automatic implicit
variables disabled. Its four public declarations printed only the standard
logical axioms. The infinite-dimensional argument is a written argument, not a
claim about the extent of that Lean module.

## Complete denominators for every shift

The root reconstructed `arithmetic/SHIFT_DENOMINATORS.md`. The centered
coordinate `Y=2x+1` makes the common intercept one. Comparing the two positive
closed numerators before cancelling proves the required phasewise comparison
even when the words have different odd counts. On a common run, deterministic
parity decisions and least-period distinctness make the difference nonzero;
after clearing the complete reduced denominators its divisibility gives the
run-length bound. Summing the successive-run inequalities, including the final
virtual position, gives the displayed geometric sum without a restriction on
the order of the shift. No factor of the full denominator was substituted for
the full denominator itself.

The root read Lagarias's stated minimum bound, Hercher's period bound and its
corrigendum, and the publisher's statement of verification through `2^71`.
Those published numerical results are external inputs. The numerical
consequences in the note are conditional on those inputs; the new finite
checker does not reproduce their large computations. The rational controls
retain nontrivial complete denominators and so are not integer counterexamples.

## Paired compression and the actual source floor

The root reconstructed `descent/PAIRED_INTERVALS.md`, including arbitrary
subsets of translated ordinary intervals. Each step keeps both endpoint
equations and their independent prefix clocks. The thin strip normalizes to
bounded slope, and the exceptional count is charged before recursion on the
shorter parameter interval. The common terminal clock is supplied by actual
padding. This verifies the written all-rank compression deduction at its
stated exceptional-set scale. It does not select a designated least exceptional
integer, and no such consequence is claimed.

For `descent/DISTORTION.md`, the root checked the ternary-unit occupancy bound,
the fixed-clock injectivity on a distinct path after removal of the terminal
indices, the binomial grade counts, and the recursive interval lengths. The
four refinements and weighted octave sum are rational computations in the
finite checker. The separate infinite tail uses integer power inequalities.
Together these prove the stated product bound `<6/5` on distinct paths whose
odd states are at least `2^71`. Applying this to a nonbasin path imports the
external range verification. The resulting sign and clock-reserve statements
are retained with their original floor; a negative signed exit is not called
an ordinary descent.

For `descent/CUT_WALK_DEPTH.md`, the root read the frozen PR195 all-word
classification at `51d97cbe17054415acaf95e422801a3532545033`, including its
reduction to the 932 ordinary specializations. The new bounded-walk argument
separately controls coefficient denominators, intercepts, both local
congruences, and accidental numerical equality. The slope gap really
dominates the intercept at the selected positive input. Thus the frozen
all-word table applies even to a walk chosen after seeing that input. The
first directed jump cannot occur, so a jump walk is not silently replaced by
an ordinary walk. The signed centers of the two proposed endpoints end at
different signed fixed points, excluding equality of their affine forms.

The fixed-rank `log log z` lower bound uses only the exact power-of-two
congruence. The growing-rank `log z` and actual upper-clock bounds use
Paper 48/v2, Theorem 8 and equations (80)–(83); the root read those statements
and the displayed supplied-source construction directly. Its common length,
exact total twice that length, positive unit intermediates, and linear budget
are precisely the properties needed. The route to 5 cannot visit 1 earlier,
which justifies the claimed true first-hit clock. These are lower bounds on
specified proof mechanisms at convergent controls, not a counterexample.

## Marked ordinary inverse trace

The root reconstructed `transport/MARKED_TRACE.md` using the stated joint
oscillation input of Paper 5/v3 and the physical shell argument of
Paper 176/v1, sections 2–4. At a fixed ambient ternary precision, the inverse
of the geometric clock convolution is exactly `2 Q^-1 - I`; the shear and
clock translations commute with fine-residue averaging. Fixed forward marks
are the last reversed gaps. Their subprobability weights pay for the sum over
all countably many marks, so no factor for their cardinality is missing.

The physical shell comparison was checked for arbitrary marked tests, not
only a fixed terminal event. Its signed norm bound controls the central error.
All noncentral exclusions are charged by the same positive unmarked mass.
The upper bound for every marked set, its complement, and convergence of the
total mass give full total variation convergence. This is a written argument
about every positive ordinary ancestor; it is not an inference from a finite
residue experiment.

During review, the root identified the stronger directly applicable input
in Paper 48/v2, Theorem 6, equations (65)–(69). It supplies joint mixing at
precision `N+K` with `K` a sufficiently small positive fraction of the free
word length `N`. Applying it before the fixed reversed marks removes the
geometric deconvolution loss. Since the central prefix length is at least a
fixed positive multiple of the physical depth, the same argument retains
`L <= lambda_* d` initial forward gaps for some absolute `lambda_*>0`.
The constant is not numerically evaluated. The imported Fourier and renewal
proofs are not formalized or claimed independently rebuilt here.

The root also checked the fixed-target paired-layer consequence. Stripping
the initial lower even coast and completing the final one gives the displayed
multiplier exactly. Distinct synchronized terminal values forbid an earlier
fusion. Under the marked one-arm law this is a dyadic residue test, and
the geometric sum over initial even-coast lengths is finite. This proves
vanishing of each fixed target's individual grade layer. It does not bound
the sum over all grades.

## Ordinary translations and cumulative loss

The root reconstructed `transport/ORDINARY_TRANSLATES.md`. On a successful
affine fusion cylinder, equality of slopes fixes the difference in odd
counts, and the two ordinary predecessor weights agree exactly. The bad
cylinders are controlled on both sides by the marked trace, using the
measure-preserving inverse affine map on odd dyadics. Opposite-positivity
endpoints form a finite set and their fixed-source mass vanishes. Dropping
the ternary progression is used only for an upper bound.

For a specified escaping component, the first-entry comparison has one sign,
so its total-mass bound is also an ordinary `l1` bound. The order of limits
first fixes the ray target, then sends the past grade to negative infinity,
then moves the target. This gives the asserted component comparison without
discarding the original grade-zero atom. The outward ternary averaging
operator sends every positive source other than 1 to growing height. Testing
on finite intervals therefore proves that its vanishing one-step errors
must be nonsummable. The same obstruction occurs at the good transient
target 5. No Hellinger estimate is substituted for this one-arm norm.

## Hellinger estimate and review boundary

The root reconstructed the normalized-carry recurrence and the hold-pinning
argument in `transport/HELLINGER.md` and `transport/HOLD_PINNING.md`. The
independent streams are selected by predictable clock types; full hold
lengths are classified at entry, and the final truncated hold is omitted
when a full-length bound is used. A second long entry pins the intervening
odd count by its three-adic valuation. The fair mismatch stream, common
biased stream, and stopping indices are kept separate. The resulting rates
concern the two-path Hellinger mass as defined in the notes. They do not
control mass present on only one side of a comparison, which contributes
zero affinity.

## Fixed-grade ordinary spectrum

The root reconstructed `transport/GRADE_PARENT.md` through the first
checkpoint. The smaller odd parent really decreases at every source above
one, and its complete positive child list has column mass one. Its defect
identity is a statement about the new parent kernel, not an assertion that
this kernel is the Collatz map.

In one fixed escaping grade, diagonalizing the forward states gives either
a first constant ordinary successor, or avoidance of every fixed floor.
The times at which a finite set can be visited are bounded because the grade
is fixed. The uniform simple-path reciprocal tail then supplies the stated
classification of real ratio limits. Every term in the first alternative
lies strictly above its limiting successor ratio. This excludes an infinite
strictly increasing sequence without changing the fixed source grade.

Equality of two corrected ratios gives a power-of-two and power-of-three
relation between their ordinary odd labels. Oddness removes the power of
two, and a strictly later fixed successor is a ternary unit. These facts
justify isolation of each actual ratio. For the unit-only compact sets,
unbounded positive grades have limit one and each higher-grade ratio is
approached by actual unit inverse predecessors. This proves the stated
successive-accumulation-set identity. The use of unit labels is essential.

The relative-offset identity follows from the exact affine cocycle.
A positive macroscopic offset forces a visit to a fixed finite floor, so
the required reverse depth is at least the moving ray index minus a fixed
constant. The geometric fractional moment then bounds the unconditioned
mass of all such supplied-target words. It does not say that this positive
mass is zero. The adjacent-depth marked discontinuity retains the atom at
the original unit and uses continuity from above only for a finite grade
measure. Its conclusion is conditional on an actual escaping component;
the pointwise regularity that would contradict it is unproved.

## New finite physical-strip transfer

The root read the exact-mask argument in PR195 at
`03b26119164664d08eaa04a1ea1d159dd4eccd7a`, round13/cycle/README.md.
Its threshold rank `2p-h` is exactly the threshold for the next mechanical
increment to be two. Thus the masks in
`arithmetic/PHYSICAL_STRIP_TRANSFER.md` are the correct local enlargement
of the stated bounded branch, not a height-one substitution.

The root independently checked the normalized numerator and its signed
integer carry recursion. An ordinary zero difference forces divisibility
at every earlier block boundary because all later terms are divisible by
that boundary's power of two. Fourier Hölder bounds any specified residue
and four different entrance layers by the four single-layer fourth moments.
The last layers are included with multiplicity; the finite transfer is
not assuming that they are independent or fixed by the numerator.

The 64-step phase list follows by sampling all right-continuous cells cut
by the 66 multiples of the irrational slope, including the extra next
increment needed for the terminal mask. Its order remains valid on a
small fixed neighborhood of the critical slope. The separate eight-step
enumeration and the two large exact integer inequalities remain to be
independently executed by the checkpoint replay.

Conditional on that finite certificate, the root reconstructed the use of
Paper 145's raw duality and Subspace-Theorem separation. After conditioning
on exterior words and finitely many boundary layers, the four actual
bridges are independent uniform finite families. The four history counts
cancel against the denominators of their fourth moments. Exterior choices
are paid as `2^O(epsilon K)`. This gives every source exponent strictly
above `23/60`, and therefore the stated period/minimum bound for the
original bounded branch. The exponent remains above one third and the
onset is ineffective. No finiteness or universal cycle exclusion follows.

## Original smaller-source costs

The root checked the two rows in `descent/FIXED_RANK_LAWS.md` by summing
actual first-hit clock and odd-count changes around the supplied bad
cycle. Each ordinary link stays above one, and every queried input lies
below the original least bad integer. The fixed-terminal inverse-word
finiteness statement follows from the positive affine formula and the
strictly expanding inverse multiplier of any actual positive cycle.
It does not provide a rule generating new words under the same cap.

Later closure experiments are not covered by these checkpoint reviews.
The fresh-checkout Lean and finite-control replay is a separate pending gate.
