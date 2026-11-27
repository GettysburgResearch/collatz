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

The first checkpoint subsequently passed its immutable-checkout replay:
14 new modules, 49 new public theorem audits, the rebuilt `Portal`
dependency with nine additional audits, ten exact controls in both Python
modes, and all eleven repository validation commands. The exact science
tree is `994d15152f99a8cf7499d7752f96fde9b774d7fd`; the published science
commit is `95c572c0af668be6ada185d35a7ff1041e4e7588`. See
[the checkpoint receipt](CHECKPOINT_VERIFICATION.md). The reviews below
concern subsequent work and have their own final replay gate.

## Post-checkpoint review: integral filters and actual rank spacing

The root reconstructed the common small-filter calculation in
`arithmetic/SMALL_FILTER.md`. The coefficients are chosen by the stated
modulo-three recursion; they are not chosen independently at each rank.
The relation between the mechanical quotient and the actual rank shift
telescopes with the displayed factors of two. Thus each filtered value
has the same full odd reduced denominator as its input. In the
denominator-one case the positive variant produces small positive
ordinary integers. The transferred inhomogeneous term, however, need
not be the low bit of that integer. The rational controls and the
one-state control test this exact branch obstruction. Goodness of the
small filtered integer has not been transferred to the original source.

For `arithmetic/RANK_SPACING.md`, the root checked that the longer
mechanical schedules include every phase cell, including the terminal
mask. The support count concerns actual possible binary residues of a
rank value. It yields the stated many close pairs at the one supplied
scale after the pigeonhole argument and the rank approximation are
combined. The averaging estimate in the scale parameter is a different
statement: it excludes most real scales but supplies no bound at the
particular scale belonging to the hypothetical integer cycle. Rotating
the anchor does not turn this into independent samples of that scale.
The new exact population certificate is included in the final replay.

The root also considered an additive-energy estimate from convex
subsequences of the approximately exponential rank values. It cannot
replace the short-bridge energy certificate as presently used. An equal
bridge carry permits nonzero endpoint co-differences of the form
`t (2^S,3^L)`; equality of the actual starting pair sums only treats
`t=0`. No improved cycle exponent is claimed from this observation.

## Post-checkpoint review: finitely many missing physical blocks

The root independently checked `arithmetic/PUNCTURED_WINDOWS.md`.
Each missing block has its actual odd count fixed in both words.
Unrolling gives the displayed integer coordinates `Z_0,Z_i`, and the
local product at the places infinity, two and three is bounded by a
polynomial in the length times `D 2^(-A)`. The two-adic replacement form
is the full sum of the coordinates; its divisibility comes from the
two actual integer endpoints. The other local forms are coordinates,
so all three matrices are nonsingular.

Passing to primitive vectors is legitimate. The product of the local
absolute values of their common integer divisor is at least one, so
division does not increase the relevant product. Height is at most
exponential in the length, and the assumed saving is exponential.
The fixed-place Subspace Theorem therefore confines a hypothetical
infinite family to finitely many proper rational subspaces. In a fixed
relation the initial coordinate dominates at the real place because
`D/K` tends to infinity. After its coefficient vanishes, the first
remaining hole has a strictly smaller two-adic valuation than all
later holes, even after the fixed coefficients are included. It cannot
cancel. Removing a zero hole is justified by fixed-grade carry
injectivity, which is also part of the Lean kernel.

This is a written argument using Schlickewei's Subspace Theorem. The
root read the original theorem's bibliographic record and Evertse's
author notes, *The p-adic Subspace Theorem* (May 2011), Theorem 1.1 and
its primitive-vector formulation. The theorem itself is not imported
as a proved Lean result. The number of holes and the margins must be
fixed; the onset is ineffective. Counting retained patterns by this
decoder alone does not reach the cycle-exclusion exponent.

## Post-checkpoint review: actual carry alignment and distortion records

The root checked the actual-prefix inequality in
`descent/CARRY_ALIGNMENT.md`. If the same parity word starts at the
small control and at the supplied source, its positive affine
correction gives the displayed comparison with the actual lower
floor. In the bounded canonical interval the full good control can
only be the stated source one. In a restricted cycle the parity pair
before arrival at one is incompatible with the restricted valuations.
This excludes the proposed universal alignment mechanism; it is not
a nonconvergence argument.

For `descent/DISTORTION_RECORDS.md`, the root reconstructed the first
crossing of the two actual multiplicative corrections. At the first
lower crossing the final lower odd step yields the strict half-unit
interval. When both residual exponents are nonnegative, integrality
forces equality; reduction modulo three then removes the remaining
ternary factor and gives an actual synchronized merger. Both the
native time and the counted odd inputs matter.

When the lower crossing occurs later, clearing its binary denominator
gives a small positive integer residual. A residual which is an actual
word carry decodes to an ordinary ancestor, but its height is larger
than twice the last lower odd input. It therefore supplies no smaller
source under the original minimum. The `161` example demonstrates this
size direction, and `164513` demonstrates that an arbitrary residual
need not be an actual word carry. The complete-word charge identity
at good controls shows why forcing such a record for every good pair
would be too strong. The replay tests actual paths and carries, not
only their homogeneous multipliers.

## Post-checkpoint review: the original canonical minimum

The root checked the interval theorem in
`descent/ORIGINAL_CANONICAL_FLOOR.md` directly. Write
`y=1+2^d u`, with odd `u` and `d>=4`. For even `d=2l`, the
successive two-clock identities and one more shortcut merge `y` with
the stated smaller positive multiple `3^(l-1)u`. For odd `d=2l+1`,
the actual five parities of `3,5,8,4,2,1`, followed by the two-clock
identities, merge `3y` with `3^l u`. The inequalities
`3(y-1)/16` and `9(y-1)/32` are in the correct direction. The
hypothesis that every positive multiple of three below `M` is good
therefore certifies one of the two orientations throughout the whole
specified interval, including off-cycle integers.

The pinned bound `243(z-1)<=1024(s-1)` places every smaller
canonical integer in that interval at `M=2s+1`. An earlier bad
canonical integer would have a good triple and contradict the
original leastness. Thus the same original `z` is the least bad
integer in the class `17 mod 48`. No new minimizer is substituted.
Its two-adic valuation `v_2(z-1)` is odd. The four actual shortcuts
send the whole canonical row bijectively to `10 mod 27`, proving
the equivalent row minimum. At the length-two capture case this
row minimum is the original global minimum `s`, so the added
inequality need not have a positive margin.

The subsequent inverse-path calculation keeps the original ceiling.
The only first nonnative odd predecessor that could stay below `z`
is `4v+1`, with `v<(256/243)s`. Its own only possible further
predecessor below the ceiling is the stated multiple of three,
which has no odd predecessor. The alternatives of larger exponent
already exceed the ceiling. These possibilities contain no canonical
integer. Consequently a smaller off-cycle canonical ancestor, if
one is forced by the original hypotheses, must be obtained through
an intermediate overshoot. The theorem has not established such
an ancestor. It also has not assumed that the original `z` lies
on the distinguished bounded cycle.

## Post-checkpoint review: a scalar physical flux and large real strips

The root checked the local identities in
`transport/SUSCEPTIBILITY.md`, including the squared edge weight
and the positive source term in the Green recurrence. The quadratic
test function gives the displayed positive escape contribution when
the named ordinary-trace and first-passage results are supplied.
The infinite undamped sum need not be finite; cancelling its incoming
and outgoing terms would remove exactly the possible escape flux.
The proposed absolute-continuity conclusion for the threshold function
is an open sufficient condition, not a consequence of the finite
recurrence. Its known derivative is allowed to be singular.

The root reconstructed the exact finite-cylinder submeasure in
`transport/UNIT_STRIPS.md`. Along an escape, a fixed ordinary
source measure is transported by the actual affine prefix, with
mass multiplier equal to its real dilation. Differentiating Lebesgue
measure relative to the singular source measure gives divergence
of the mass in the resulting fixed-width strips. The stronger
limsup statement uses the cited Hausdorff gauge and the bound of
three halves on each upward dilation step. Neither step averages
over moving integer terminals.

The long-interval improvement is also valid under the named
full-dimension and singularity inputs. At any fixed child depth,
the mean conditional entropy deficit has Cesaro mean tending to
zero. Fatou gives infinitely many parent cells at almost every
source point with every child having a fixed positive fraction
of the uniform conditional mass. Singular dyadic density tends
to infinity at the same point. First crossing of the required
affine dilation makes every transported child have length between
one quarter and three eighths. Every contained unit interval
therefore contains a whole child of large mass. A diagonal choice
of child depths yields intervals of diverging length with large
mass in every unit subinterval. The argument does not claim a
uniform logarithmic rate simultaneously on all those subintervals.

The exact-transport statement on any fixed interior relative band
uses the uniform reciprocal tail to force a visit to a finite
floor. Every relevant member of that floor has joined the escape
ray by one common finite date. Beyond that date all mass in the
band is inherited from one fixed earlier fibre. This identifies
why new high-suffix mixing does not itself control its fine real
concentration. The cited stationary product-ball bound has a
resolution-dependent logarithmic loss and is not the needed
ordinary unit-strip upper bound.

## Post-checkpoint review: a common closed correction set

The root read the new PR193 fixed-root closed-support proof at
`2796977d3f02ad57daeb7510f16da29527f9afde`, together with the deduction
in `transport/GLOBAL_CORRECTION_GAPS.md`. On any band away from
correction one, the uniform simple-path reciprocal tail forces a
visit to one of finitely many small odd vertices. Splitting there
places the correction in a compact null first-hit set times a
countable compact set from one deterministic future. This product
is compact and null. Taking the wider preliminary band handles
limits at the band endpoint; a countable exhaustion and the point
one give one compact null set for all simple segments.

The deduction uses PR193's written closed-null theorem and its
named analytic hypotheses. This pass has not replayed every
dependency of that external branch in Lean. For nonperiodic
ordinary targets, all finite inverse prefixes are simple, so the
result gives the claimed exact zero strips on compact sets of
relative positions outside the reflected correction set. The
escape's amplified strips lie in the exceptional set, so these
two conclusions are compatible.

The all-segment dichotomy is also consistent. With finitely many
cycles, removing whole laps gives a finite union of geometrically
scaled copies of the simple correction set, with zero as the
only added limit from unbounded lap counts. With infinitely many
cycles, their minima tend to infinity, their one-lap corrections
tend to one, and their repeated corrections approximate every
point of `[0,1]`. This does not establish finiteness of the set
of cycles. The one-sided linear lower mass bound at intermediate
scales is compatible with singular dimension one; it is not a
porosity or absolute-continuity theorem.

## Post-checkpoint review: exact ordinary parent rows

The root checked the endpoint formula and reverse decoding in
`transport/PARENT_ROWS.md`. At fixed total binary cost the actual
compositions have one endpoint in every odd residue modulo that
power of two. The last gap can be recovered from `v_2(3v+1)`
unless it exhausts the total cost, in which case the composition
is unique. The endpoint bands then force the displayed complete
integer subinterval, rather than only a limiting density there.

For the limiting row, conditioning the fair renewal bits to renew
at the last date gives the uniform compositions. A bounded initial
part of the infinite code is independent of that sufficiently late
bit. Approximation by those initial parts and the exact odd grids
prove that the limiting fractional part is Haar. Its compact
real support has positive measure and lies in the two stated
bands. The iterated similarities have total contraction one, so
their support images overlap only on a null set and normalized
Lebesgue measure is stationary. Uniqueness of the contracting
stationary law, followed by the Haar fractional part, makes the
support a one-fold integer tile of measure one. These steps give
the row convergence for a bounded label only when its ordinary
mean exists. A whole escaping component has not silently been
assigned such a mean.

The boundary estimate uses a cylinder of exponent five lying
strictly in the support's interval. A boundary point cannot have
a code containing that cylinder. The weighted count of codes
avoiding this exponent has growth rate strictly below two, giving
the claimed geometric approximation error for the row sets.

For a fixed root in an escaping component the strict corrected
height margin forces a same-grade row endpoint to have exactly
the displayed corrected-height dilation, not an arbitrary nearby
power of two. A fixed positive distortion forces a visit to a
finite floor. Fixing the grade bounds the native odd depth of
that visit, and its native exponents are at most the row cost
plus a constant. This proves the polynomial count of same-grade
endpoints against the exponentially large complete row. It does
not turn the other endpoints into smaller witnesses. Intermediate
ordinary-parent nodes may leave and reenter the component.

Finally, the growing-translation estimate in
`transport/ORDINARY_TRANSLATES.md` retains a burn-in depending
on the translation size. The equal-rank square-root-logarithm
bound is explicitly credited to Paper 13/v1; the extended statement
and its marked application preserve this cost. Subexponential
translations at a large depth do not supply a pointwise merger
at the original source or its original height budget.

## Root synthesis: the full-mask boundary for every fixed real moment

The root constructed `synthesis/FULL_MASK_MOMENTS.md` after reading the
new PR200 fifth-moment source reduction, its narrow third-layer extension,
and its separate even-moment obstruction at
`df2f17a117bea06bb34040a5a97e7dc9711d9871`. The new certificate concerns
our wider complete physical mask. It does not contradict that branch's
fifth-moment result for a smaller family.

At 512 odd departures, all 514 phase schedules and 2,908 fixed-cut cases
have population greater than `3^(47*512/100)` and coordinatewise
unordered-pair collision count greater than `3^(109*512/100)`. The
root executed the exact transfers, checked their integer inequalities,
and compared both with literal path and ordered-pair-signature
enumeration at eight steps. The retained checker has no removable
Python assertions. Its final immutable replay is separate.

Fixed entrance and exit layers fix the full native duration. Peeling
the least dyadic term of the ordinary numerator recovers its odd
positions, so there is no last-layer ambiguity in Parseval's identity.
All-cut positivity gives uniform block concatenation, and a bounded
initial remainder can be chosen identically in the four copies.
The existing population upper rate is `12/25` per native binary clock.
In the joint critical-slope limit these three rates are therefore
`0.47`, `0.48`, and `1.09` in base three per odd departure.

Elementary supremum and probability-space norm inequalities, together
with the near-zero arc of the ordinary one-variable polynomial, give
five affine lower bounds for its logarithmic moment rate. Switching
at `q=2,61/18,4,5` covers every real `q>1` and yields the uniform
rate `(q-1)(1/3+1/30000)`. The finite rational piecewise envelope
and its strict cubic separation also pass strict local Lean checking.
This does not formalize the Fourier or asymptotic steps.

The arithmetic agent independently read the proof and checker, confirmed
the fixed-cut injectivity, concatenation, ordinary fourth-moment
orthogonality, degree bound and the joining inequalities, and reported
no gap in the stated scope. The conclusion concerns the cost of
individual unweighted segment norms in the stated Holder architecture.
It does not lower-bound the actual joint convolution atom and does not
apply after a genuinely smaller source family is specified.

The root then read the new PR201 carried inverse-rival argument at
`a577c1f19a00b8219dcde9744814813ddd636e66`. Temporary single-history
probes of its 584-context bank, and a 796-context extension to layer
two and the full width, still had sampled population rates around
`0.475` in base three per odd departure at 2,000 steps. The extension
also passed 1,592 literal ordinary-lift checks. These are exploratory
finite entropy probes with numerical phase sampling, not uniform
asymptotic bounds or new source-counting theorems. They guided the
ongoing search toward joint actual histories and stronger source
conditions; they are not included in the final theorem count.

## Actual bilateral histories and original upper gaps

The root reconstructed the two-modulus graph argument in
`arithmetic/HISTORY_TRADES.md`. A future word fixes a residue modulo a
power of two; a past word fixes a residue modulo a power of three.
Only pairs actually occupied by one of the same cycle's integer phases
become edges. An alternating graph sum is divisible by the product of
the two moduli. The complete ordinary height bound then makes sufficiently
short alternating sums zero. The common-clock recurrence transports that
zero through the entire matched bilateral window. The full reduced odd
denominator is retained in the rational control, where the corresponding
signed sum is nonzero. The finite Lean statements prove the divisibility,
height-to-equality and synchronous transport implications, not the graph
population or imported logarithm estimate.

For equal windows the exponents are 49/32 for each modulus, 147/200 for
the vertex count, and 49/50 for the four-or-six-cycle extremal threshold.
Successive pivot deletion gives the stated independent relations. For
the longer window, the product dominates every graph cycle's possible
sum. Integer past and future potentials follow from a spanning tree;
their existence by itself is compatible with a hypothetical cycle.
The root subsequently proposed unequal windows to force four-edge
relations alone. The final strengthened version is reviewed separately
below when its source is frozen.

The root read `descent/ORIGINAL_UPPER_GAPS.md` after the odd ceiling was
weakened to 8s and the no-consecutive-evens assumption was removed.
Its upper is the same actual first-hit suffix throughout. The original
source's native two-edges yield L=2a+1 and the supplied upper meets T(a);
the stated first-hit cost shift follows because the entire finite prefix
stays above one. At each later upper gap the signed rational centre is
determined by the preceding odd positions, not by that new gap.

The actual physical product, with floor s and total ceiling 13s, bounds
every segment's clocks by less than twice its odd count plus four.
After the necessary lower odd departures the rational centre is an
integer c with -13*2^(t_q) <= c <= 13+5q. For negative c, the exact
ratio decrement bounds the number of matching odd departures. For
0<c<s, the good control's pre-hit odd sites are distinct, and all but
possibly the first are ternary units. Counting those sites in the
derived interval gives n<=24c+27. Eight subsequent trivial-cycle laps
would cross the bad floor. These estimates fit the displayed recursion
with constant 1000. The endpoint t_(r+1)=H is the actual first hit,
not an additional odd departure.

Thus for each fixed odd rank of this original upper, either the floor
is explicitly bounded or the original lower has a large physical peak
before that certificate's endpoint. The bounded-cycle case supplies
the peak bound; the off-cycle original does not automatically do so.
The estimate does not supply a uniform bound over all possible ranks.
The packing, induction and infinite-rank discussion are written proofs;
Lean checks the finite prefix, exit and affine-remainder kernels.

## Current balance and inverse certificates at the original floor

The root read `transport/ORIGINAL_CURRENT.md`, its six-theorem Lean
module, `RESIDUAL_CURRENT.md`, `ORIGINAL_FLOOR_SIEVE.md` and the full
original-floor checker. The current's earliest negative charge follows
from the absolute bad floor and the actual shortcut identities. The
reciprocal sum retains its nonnegative outgoing boundary term. Neither
later signed current nor that boundary is set to zero.

For the residual Radon measure the root checked the factors in each
pushforward: division by the residual removes the coefficients two and
three in the retained-layer identity. Summing gives a balance between
the full measure and its odd sector. The Mellin equation has the
displayed factors 1-2^(-sigma) and 1-3^(-sigma). The component floor
gives local finiteness, while the discounted trace input supplies the
asserted moments. The fixed-grade rotation calculation is compatible
with singularity at every one grade and Haar Cesaro averages over many
grades. The explicit two-geometric-ray singular control satisfies the
balance and has a positive floor, so the argument does not infer
separate dilation invariance.

The inverse-floor enumeration retains the supplied original source,
the native forced prefix, all intermediate integrality, and each of
the three stated strict floor tests. Its finite tables cover only the
declared depth and height ceiling. The separate all-depth statement
is a written proof about the countable union of asymptotically valid
fixed-word cylinders. It uses a positive virtual ternary control at
two, with the original dyadic residue retained independently.

The root checked the countable-union step. After binary clearing, a
fixed ordinary virtual endpoint has uniformly bounded multiplicity at
each depth: its ordinary forward orbit determines the clearing value
and exponent for each of finitely many short prefixes. Infinitely
many occurrences of that fixed endpoint force a periodic terminal;
positive inverse cycle multipliers then tend to infinity. Summable
x^(-sigma) domination proves convergence of the prefix weights. The
tail union bound converges for 1<sigma<2. Its t=0 term accounts for
the as-yet-unfixed final ternary digit at depth R+n. This does address
all fixed-word cylinders, not just any one finite list.

The resulting Haar density-one survivor does not classify ordinary
integer counterexamples: those form a countable, Haar-null set.
Finite-source affine crossovers, more forward steps of the supplied
lower, and the complete good upper are separate information. Additional
ordinary controls and the later fixed-source depth consequences are
kept with their own stated scope in the final source note.

## Last external frontier intake

The final metadata snapshot records the heads observed at 04:01 UTC.
The root read PR201's eighth-checkpoint guide and full ternary-past
entropy proof at `860a67dedc860adcd82b964958d91b9e21d610f1`. Its
hereditary four-sum bound uses the actual binary ternary-past tree;
its entropy transfer retains fixed-place separation. The root also
read PR200's sixth-checkpoint guide and full abstract rank-cap
construction at `7af83b786636abba2f44fe8c81441153331377fc`.
The latter deliberately omits chronological Collatz equations.
These comparisons reinforce the need to retain those equations in
our bilateral history argument. Their bulk numerical and Lean
certificates were not rebuilt in this packet, and their new finite
cycle-period exclusion is not included in our verification counts.

PR193's guide at `67e5cdb3c1689836bf1dc01a57a7e46b85449dcd` describes
its adaptive rational-energy criterion. Its two uniform estimates
remain explicit open premises. The root did not import those premises,
or the guide's externally assisted Mellin estimate, into a closure.

## Strengthened four-phase core

The root read the completed asymmetric and ranked-core sections of
`HISTORY_TRADES.md` at 04:05 UTC and re-read the pinned physical-mask
prerequisite. The latter supplies the coprime rotation pair, actual
dyadic lifts and uniform logarithmic rank error for this bounded branch.
In particular the wrapped digit bound is eight, since the fundamental
digits are one, two or four.

With future and past modulus exponents 25/24 and 49/24, the part sizes
are p^(1/2+o(1)) and p^(49/50+o(1)). Counting pairs of neighbors gives
the four-cycle-free edge bound b+f*sqrt(b)=p^(99/100+o(1)). The product
modulus is p^(37/12+o(1)), large enough to turn every four-cycle into
an exact ordinary rectangle. Pivot deletion therefore gives at least
p-ceil(p^(199/200)) independent four-phase identities.

The root checked why the asymmetric choice eliminates the small-area
alternative. The physical rank error and s/p^2 tending to infinity give
a minimum true gap of constant times s/p. The long past side is a
nonzero multiple of 3^(L_P), asymptotically larger than p^2. Their area
therefore exceeds any constant times ps. The integer rank-log cross
difference forces the remaining area bound of constant times s^2/p.
This argument uses true ordinary phases, not a freely selected rank grid.

For the further refinement choose any fixed delta<1/25, record rank
modulo floor(p^delta) at the past vertex, and use modulus exponents
1+epsilon and 2+epsilon. Both four-cycle-free edge exponents remain
strictly below one for sufficiently small epsilon. Greedy increasing-rank
insertion produces one sublinear retained set. Every discarded edge
has its own four-corner identity with three earlier retained edges.
The rank cross is a nonzero multiple of the recorded modulus, giving
the stronger area floor of constant times s^2*p^(-1+delta).
The relations are independent because no discarded edge enters any
other relation's retained corners. A negative coefficient remains in
the reconstruction; these additive identities are not physical mergers.

Finally the longer digit-matrix bound is a direct lattice count.
Small integral digit dependencies must annihilate the state by dyadic
divisibility and height. The irreducibility of X^p-2, together with
gcd(p,h)=1, makes the first L+1 twisted state shifts independent.
The elementary Gaussian image count bounds the codimension from above
by L+O(log p). This is compatible with the required lower bound L+1.
It does not make the finite-window relation space invariant under all
chronological shifts. That is an exact remaining obstruction to the
linear-algebra closure attempted here.

The final packing variant is consistent with these bounds. Averaging
common-past-neighbor counts produces K_(2,t) with t>=floor(p^tau) whenever
tau+delta<2/25 and the remaining edge count exceeds the chosen sublinear
threshold. Removing all its edges gives disjoint actual source families.
Their common positive gap follows from the already proved four-cycle
balances. The distinct decreasing rank displacements then give the stated
area bound between the extreme anchors. None of these estimates bounds
the common gap tightly enough to force a contradiction.

After completing its own lane, the descent agent independently reviewed
the asymmetric graph, rank-color core and repeated-gap packing. It
recomputed the modulus orientations, all extremal exponents, the
strict rank-log sign, and the permanent earlier-core argument. It
reported no gap in these sections under the stated physical-mask and
quoted logarithm-ratio inputs. This second mathematical review is
separate from the finite Lean replay.

## Final ordinary controls and finite-source consequences

The root checked the final source-specific additions to the transport
note. When v_3(z-2)=R, the rational separation between two distinct
comparison slopes is at least 1/(4^r*3^max(d-n,0)). At reverse depth
d<=R+n-8 it defeats every possible finite-source crossover. The explicit
Mersenne family has the claimed ternary period lifting because
v_3(2^162-1)=5. It supplies actual good upper arms of fixed odd rank,
without assigning a bad lower label to any constructed source.

At 353 the new Lean proof is an all-time predecessor exclusion, not just
a bounded trajectory test. Its finite table reaches the known 1/2 loop
without visiting 199; the proof then excludes a later visit at every time.
It also checks attainment of all three minima and convergence of both
original arms. This control concerns inverse paths from the forced
initial block. Further lower forward targets are not covered by it.

For the polynomial-height progression application the root read Weaver
Paper 13's Proposition 1, its underlying counted-fusion estimate, and the
even-prefix discussion, as well as Paper 12 section 8 equations (23) and
(24). The new application uses only the fixed target 5's positive lower
ordinary density. The initial-block proof averages over a complete
progression period; it does not assume a natural mean for the entire
good set or a relative estimate for a moving rare basin. Choosing a
sufficiently large fixed power of the modulus gives the claimed actual
good-upper control with logarithmic necessary lower inverse depth.
Those analytic results remain imported inputs, not Lean theorems here.

The current's final twelve-phase argument also checks directly. The
19/12 and 27/17 rational fences for log_2(3), together with the tiny
positive edge correction at the verified floor, place each twelve-block
within a one-sided displacement less than 11*(1/204+1/10000) of a
permuted twelve-grid. Its maximal circular gap is below 3/20. The high
shell fits in an arc shorter than 17/20, so every twelve-block has a low
phase. Counting all cyclic starts gives L_s>=P/(36s), without an
asymptotic rank-grid assumption. The larger P/30 constant retains its
own asymptotic premise. Both versions keep the same outgoing flux.

The final descent note's averaging recurrence permits actual sign
recovery. A nonpositive-to-positive centre change has new centre strictly
between zero and one half; its exact dyadic denominator then forces the
same good upper to reach at least 4s-1. The ordinary numerical example
tests this possibility with genuine first-hit paths. It does not assert
that the example is a hypothetical bad source or that a bounded initial
prefix extends to an entire bounded orbit.

The transport agent performed a final independent adversarial review of
the complete upper-gap proof. It checked the arbitrary-gap centre and
ratio recurrences, the loss of one ternary denominator factor per actual
lower odd departure, the positive-control packing constant, the finite
trivial-cycle tail, and the negative-centre bound. It reported no gap.
The no-consecutive-evens assumption is confined to the more specific
first-unpaid description on the distinguished cycle; it is not a hidden
premise of the final 8s peak/rank tradeoff.
