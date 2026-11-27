# Root review: fifth moments, three grades, and ordinary-source clocks

**Collatz remains open.** This checkpoint contains a computer-assisted local
fifth-moment theorem, its written source-counting consequences, broader cycle
restrictions, and ordinary-integer ensemble theorems. It contains no formal or
informal proof that every positive integer reaches one.

The integration parent is `2346db2d49030ef385b73e1ee3e27dcbff86d2d9`.
The root reconstructed the arguments described below, read their frozen source
files, checked the named external theorem statements at the scope stated here,
and performed the separately retained execution checks. The author, independent
reviewer, and root roles are distinct. Source hashes and the integration
transformations are in `WAVE4_SOURCE_MANIFEST.json`.

## 1. The actual one-dimensional fifth moment

The main new result is the local bound in
`FIFTH_POSITIVE_CERTIFICATE.md`. For the complete two-grade binary path language,
with arbitrary cut bits and intercept and with the mechanical slope tending
to `log₂ 3`, the upper natural logarithmic fifth-moment rate is at most
`(4/3) log 3 − 1/7000`. This local theorem does not use the Subspace Theorem or
the October logarithm-ratio preprint. The input is one Haar variable feeding
the ordinary segment numerator polynomial.

The root checked the following source-law points. The coefficient gcd after
observing successive phases is the indicated power of three. Consequently the
next phase has exactly three equiprobable compatible roots, even when the
entire past is retained. The update matrices send the two complex amplitudes
through the actual descending or ascending binary edge. The first source
reduction writes a conditional operator at the current phase; the positive
certificate explicitly changes to its **pre-innovation** state. These are
equivalent descriptions of the same scalar Haar law, but their cochains are
different. The final source does not silently identify them.

In the pre-innovation coordinates, writing `2πS=3r` and taking the Bloch azimuth
plus `r` gives circle frequencies `3k−s` in the input and `2^m k` in the output.
The three branch factors and azimuth shifts in the C++ implementation match
these formulas. Direct computation of both shear matrices gives the printed
norm square and all three normalized Bloch coordinates. The sign of the
implemented residual is opposite to one displayed convention; only its
absolute Fourier coefficient bounds are used, so this has no mathematical
effect.

The finite certificate retains 76 dyadic cochains and 77 transition scales.
Its compressed witness has SHA-256
`bca88393d4efe84cb88c80f119bb626eb0c601d0cde0aaac4ae8d4463b39d496`.
Every relevant phase arc is generated from exact rationally bracketed floor
breakpoints. The ordered lifted labels agree at both slope endpoints; no
unexamined phase-order crossing is inferred from a numerical sample. Point
faces have the floor word of the neighboring admitted cell, and uniform
limiting rotation frequencies also cover rational slopes and arbitrary
intercepts approaching the critical slope.

### Off-grid and arithmetic verification

For spherical degree `l`, the remaining shear factor is `g^(5/2−l)`.
The binomial factors have arguments of modulus `1/√5 < 0.448`.
Truncating each conjugate factor at degree `80−l` gives a symmetric Laurent
polynomial with maximum frequency `80−l`, hence a polynomial of that degree
in `g`. Its degree is not doubled: products have frequency equal to the
difference of the two monomial indices. Multiplication by the raw numerator
of degree at most `l` gives degree at most 80 in each of the two grid angles.
The stated geometric tail bounds and the `g^l < 2.619^l` numerator bound
therefore control the entire residual, including all circle coefficients.

At an absolute maximum of a complex trigonometric polynomial, a fixed real
component attains that modulus and has zero derivative. Bernstein's second
derivative inequality then gives the printed nearest-grid estimate. Applying
it on each axis yields the rational factor below four on the `252 × 252`
grid. Positivity is handled separately by the zero gradient at a global
minimum and a coefficientwise second-derivative bound. The third circle
coordinate is bounded by the sum of absolute Fourier coefficients, rather
than being omitted from the sampling grid.

The root read the entire integer evaluator and rational wrapper. The angle
routine uses rational Machin and Taylor enclosures. All accepted square roots
use integer Newton iteration and exact integer comparisons. The start value
is a power-of-two upper bound and the decreasing iteration terminates at the
floor. The stated coordinate, monomial, weighted dot-product, root-of-unity,
and final residual error bounds fit within the `2^-30` coefficient padding
and `2^-28` lower padding. The coefficient bounds and all intermediate
integer sizes fit in the declared signed 128-bit arithmetic. The polynomial
and grid checks use explicit failures, not removable Python assertions.

The root ran the complete frozen evaluator with a fresh C++ compilation:

```sh
python -B fifth_verify.py --rebuild --threads 2
```

All 10,626 integer entries matched the author's saved grid byte for byte.
The raw grid SHA-256 is
`0edb572acf25cec643ac9c7787c9f32532f359cb062faf35eca6d58e4bb66ecf`.
The root's complete result equals the author's result and is retained as
`ROOT_FIFTH_REBUILD_WAVE4.json`. The independent binary-energy reviewer also
recompiled the grid under undefined-behavior sanitization and reconstructed
the rational bounds with separate code; its signed review is retained.

These checks establish the stated positive finite certificate under its
written analytic interpolation and arithmetic error proof. They are not a
Lean formalization of that proof.

### Located source transfer and the external inputs

The five physical segments use their own true dyadic multipliers on one
common integer frequency interval. For each segment the root checked the
placement inequalities `m, (log₂3)n ≥ h`, its strictly shorter binary duration,
and the raw numerator bound. A too-close pair among the low multiples of the
actual multiplier produces a nonzero integer `2^m a−3^n b = d k` below the
exponential scale excluded by Weaver 145, Lemma 4. The factor `d` is retained
for rational cycles and is harmless precisely in the stated subpower regime.
The cited separation lemma was read directly; its underlying integral
Subspace Theorem is an external mathematical input.

A Fejér majorant bounds local occupancy of these actual frequencies. The
reproducing kernel `2K_(2D)−K_D`, Jensen's inequality for its absolute kernel,
and the inverse-square envelope transfer the continuous fifth moment to the
discrete source frequencies with only a logarithmic loss. Five-factor Hölder
then bounds the positive source count after fixing cut grades and the
exterior. This does not assume independent frequency variables.

The resulting lower numerator-height exponent is
`4 / (4/3 − 1/10000) > 3`. Finiteness and uniform positive denominator-power
conclusions additionally import `μ(log₂3) ≤ 3` from Chudnovsky,
arXiv:2610.28079v1, Theorem 11.1. The root checked that statement and its use,
not a fresh proof or formal build of the external preprint. Its newer
November abstract does not supply a stronger exponent two for this ratio.
No effective onset or finite exception classification follows from this
argument.

## 2. A genuine third layer and a global sparse alternative

`THIRD_LAYER_FIFTH_EXTENSION.md` allows `W ≤ 2 + 1/100000`.
At each phase where grade two can appear, the preceding mechanical edge is
an up edge and the following edge is a down edge. These two-edge blocks have
disjoint edge sets. Their actual complex matrix is dominated entrywise in
absolute value by `[[2,1],[1,2]]`, of operator norm three. The bound is
pointwise in the underlying Haar phase, including its correlations.

The finer three-grade digits are `0,2,3`. On clean edges, doubling the fine
phase bijects its three roots to those of the doubled pre-innovation state.
The verified two-dimensional cochain therefore still applies conditionally
on the full fine history. At a two-edge block the lower and upper cochain
bounds give a factor 8100. Compared with the two ordinary scales, this costs
at most 2025 per eligible site. Its deterministic phase frequency is
`1/100000 + o(1)`. The remaining strict pressure margin supports base-three
exponent `4/3 − 1/20000`. Boundary rectangular maps and fixed coordinate
projections cost only an absolute constant. The fresh all-height reviewer
independently checked the physical polynomial identities, fine conditional
fibres, both endpoint faces, and a primitive rational inclusion example
with width strictly above two.

For arbitrary positive valuations and arbitrary width,
`GLOBAL_SPARSE_BINARY_ALTERNATIVE.md` proves, using the same stated external
inputs, an eventual alternative: `d > P^(10^-8)` or more than `10^-8 P` sites
have canonical grade at least two or valuation at least three. The root
reconstructed the directed repair. The directed runs have length at most
two; clipping can violate only an up-edge inequality, and the required
repairs lie in the bad sites or their predecessors. The proof uses the
slightly looser count `3|B|` safely.

The crucial source step occurs **before** a fractional Fourier moment is
taken. Both window endpoints are unchanged. Recording the changed grades
fixes one constant translation of the whole source residue on its actual
common modulus `2^K`. The repaired language can then be enlarged inside a
positive interval count. No false monotonicity of an `L^5` norm under removal
of paths is invoked. Weak-composition records cover arbitrary downward
grade jumps, including winding windows. The source-separation slack, kept
mass and final exponent product were checked with rational arithmetic; the
root's Lean budget file independently verifies their final exact margins.
The independent binary-energy reviewer supplies a separate signed audit and
controls with grades above 100.

The second branch of this alternative is permitted. It is not a
contradiction for general cycles.

## 3. The broader three-grade physical band

`THREE_GRADE_MODULAR_BAND.md` treats binary cycles with `W ≤ 121/50`, and
therefore the full bounded physical branch whose limiting odd-height ratio
is at most `16/3`. Its numerator-height exponent is `5/2`; with the separate
irrationality input it forces every proper-lag mismatch fraction eventually
above `1/1500`. This conclusion is different from finiteness.

The modular count permits an arbitrary integral inherited carry. If `a` is
the pair-sum multiplicity on the relevant finite group, its fourfold atom
at any shift is `sum a(x)a(x+r)`, at most `sum a(x)^2`. This follows from
`2uv ≤ u²+v²` and the translation bijection, with multiplicities retained.
`ModularZeroAtom.lean` formally proves the generic inequality, the literal
ordered pair/fourfold count identity, and its use for every signed incoming
carry modulo a power of two. It does not claim that the separate numerical
64-block count was formalized.

The complete exact phase arrangement has 260 point/open faces and 130
distinct schedules. The author and a separate unordered-pair implementation
agree on the maximum
`448804760794336774447153725940272863`, whose fifth power is below `3^384`.
The independent review searches all possible crossing slopes, not merely
sampled endpoints. Repeated modular blocks bound ordinary equality tuples;
allowing unrestricted endpoints and terminal integral carry only enlarges
the count. The root checked this concatenation and its four-segment source
consumer.

For the physical-band implication, the elementary binary terminal census
already gives `dX ≫ P^(log₂3)`. Thus `P/min(x_i) → 0` in the subpower
denominator regime, and the accumulated additive correction in the
height/discrepancy identity is negligible. The strict inequality
`log₂(16/3) < 121/50` supplies room for that error.

For ordinary cycles, canonical height at most two gives coprime clocks by
Weaver 114. The scaled rank states satisfy an exponential reference curve
with `O(P)` error. Their signed gaps have size `O(Xt/P+P)` and multiplicity
`O(1+P³/(tX))`. The complementary orientations charge different central
grade profiles. Freezing a profile over 53 dates costs the explicit
stationarity error, rather than assuming independence of the grade and
phase. The interval-intersection ambiguity, the entropy of changed
profiles, and the height range `5/2 ≤ ξ ≤ 3` give the printed strict
`1/1500` margin at every rank scale.

## 4. Other cycle statements and their priorities

The earlier all-lag manuscript was reconstructed from the smooth rank and
signed drift recurrence. `ALL_LAG_TWO_ORIENTATIONS.md` improves its
full real-width-below-two conclusion to `1/36` under exponent three and to
`1/1000` using the 2018 two-logarithm bound alone. The root checked the
conditional entropy count, the two ambiguity orientations, the 53-step
rotation grid, and the five-point control of peripheral runs. The latter
uses the actual valuation range `{1,2,3}` in that full positive class.

The root opened the primary Bondareva–Luchin–Salikhov 2018 paper and read
Theorem 1 on page 18. Its linear-form exponent is `4.116201`; setting the
constant coefficient to zero and dividing by the denominator gives the
ratio-approximation exponent `5.116201`. No estimate for `log 3` alone is
substituted for a bound on `log₂3`. The two classical depth alternatives
retain this older input; the shallower terminal-census row uses no
Subspace Theorem. The four-segment row does use it.

The averaged-return extension to `397/200` uses the deterministic
frequencies of 53-, 94-, and 147-letter phase returns. Individual returns
need not have the desired energy bound. The root checked the weighted
frequency argument and the fixed-slope/joint-limit uniformity. The sparse
depth proof conditions on actual high grades, clips within the fixed
phase cap, and uses a common affine translation of the balanced numerator
sums. The nonbinary extension repairs the at-most-two-edge up runs by
suffix minima and records each change before counting. These written
arguments and the separate sparse projection audit are retained even
where the newer fifth-moment statements improve their scope.

`ALL_EVEN_MOMENT_BARRIER.md` is a limitation theorem for the specified
independent-segment method. Coordinatewise equal tuples give a lower bound
on the genuine quantized even moment, with only a bounded sum-rounding
loss. The exact orders 2, 4, 6 and log-moment convexity on the auxiliary
torus give the claimed obstruction for every fixed even order. This does
not obstruct mixed-frequency cancellation or the fifth-moment argument.

The rational clock identity records `gcd(A,P)` as the order of
`3^(P/g) 2^(-A/g)` modulo the reduced denominator when canonical height is
at most two or the physical ratio is at most eight. The root checked its
residue-fibre sign reversal proof and its count of actual inversion pairs.
The unrestricted identity is false, as the explicit denominator-431
counterexample shows. Weaver 114 and the unrestricted inversion comment
in Post 65 are credited for the ordinary predecessors; the denominator
order and the constrained-lag counting are the new scope.

## 5. All rational heights at actual ordinary starting integers

The root read and independently reconstructed Theorems A and B, their
fresh audit, and the sharp octave-tail refinement. The statistic `Q(x)`
takes the supremum over positive rational anchors, with reduced
denominators prime to three. Denominators divisible by three have negative
valuation and cannot enlarge that supremum. Positivity bounds the
possible height of a violating anchor by `exp(O(k/log k))` in octave `k`.
There are only `O(h)` anchors of exact height `h`, so elementary residue
counting gives the static reciprocal-sum threshold `1/(log 2 log 3)`.
Anchor one gives equality-case divergence.

For the window of `α log₂ n` accelerated dates, `0<α<1/2`, the first
native bits of one ordinary octave are exactly uniform. A stopped
negative-binomial clock preserves enough of those actual bits. Complete
suffixes give the geometric ternary law; incomplete suffixes are counted
on the remaining ordinary arithmetic progression, with its explicit
rounding error. The error remains exponentially small after the finite
anchor-height union.

The reflected target `−1` has a useful exact first-hit decomposition.
Before reaching magnitude one its signed deterministic inverse path has
distinct integer magnitudes. Its reciprocal telescope, the geometric
exponential tail, and subsequent gap-one loop give
`2^d p_d(−1)=C_*+O((3/4)^d)`, with `C_*>1`. This removes the polynomial
loss in the upper bound. Marked zero-followed-by-ones patterns on the
same initial native bits have mutually exclusive overlaps, so a direct
second moment removes the lower logarithmic loss. The resulting octave
tail is `Theta(k^(1−c(log 2)^2))` for `c≥(log 2)^(-2)`, including order
`1/k` at the reciprocal-sum threshold.

The macroscopic gate transfer uses only domination by `1/x` and its
stated lower mass. The native affine slope martingale and the bounded
translation show that the whole tested window precedes the actual first
exit except on the stated normalized error. This controls a once-sampled
ordinary starting integer. It does not replace the suffix of an escaping
ray by a fresh ensemble. The explicit long-one family rules out universal
all-height clocks with natural-log time constant below `1/log 2`.

## 6. Birth cohorts and unrestricted small visitors

The canonical birth profile first proves a finite bound independent of
the endpoint test. The birth-time binomial law compares all births by
depth `J` with all odd sources below `2^(2J+1)` at total reciprocal error
at most `sqrt(J/2)`. Transport by the actual deterministic weighted map
cannot increase this error. This part is elementary.

The old-cohort ray formula additionally uses the pinned fixed-target
first-hit time law, minimum tightness, and original entrance/charge
limits. The root retrieved Valbuena's source at commit
`a7275d5a73814d3d9a400c6fe6577de9542b03a3`, blob
`63ca82653986b0dfa4c54bac17ed80199b806448`, read the precise first-hit
statement, and checked the normalization `lambda=log(4/3)`. The root also
read the cited entrance and charge statements in the pinned PR 193
exponential-dust source. These are imported results, with their existing
analytic dependencies; they were not independently re-proved here.

At a fixed core, replacing the ordinary source cutoff by its entry-clock
cutoff costs only a narrow log-height band and the named exceptional
mass. The fixed entrance weights converge, after which their residual
transport is the specified physical ray segment. Aligning finitely many
entrances shifts only bounded end segments. Increasing the core and then
using monotonicity in the birth cutoff gives the stated uniform total
variation profile. The young-cohort dyadic formula requires the extra
pre-entry drift and dust input and is labeled accordingly.

The exact harmonic test `P*F_C=F_C` shows why a positive escaping
component's old mass would persist through arbitrary later ages.
The all-height window typically ends before its source's canonical birth;
deleting the small exceptional sources cannot erase an old component
charge. These statements identify an obstruction to a renewal argument,
not an escape exclusion.

The early small-visitor theorem uses the resident uniform distinct-path
packing bound and the separately quoted original ternary `L^p` bound.
On the good short ordinary window, every physical endpoint is above its
current ternary period. Exact harmonic transport and Hölder then bound
visits to the union of all forward rays from a power-sized prescribed
family. Visitor time is unrestricted; the observed source window is the
stated short one. The conclusion leaves larger competing starts and
later observation windows outside its scope.

## 7. Repository intake and formal boundary

The root fetched and inspected the new guides and named relevant sections
at PR 193 `2796977d3f02ad57daeb7510f16da29527f9afde`, PR 195
`3fa7ef4a0011b35447a70f587b400878d5ea8ebe`, and PR 201
`807d67ab049f1646398d8ca8c20948cdc1d87742`. PR 206 remained at
`640bf7e511831a0ffc4f00462f12df81f8a8a619`. The PR 201 guide states the
restricted bounded-branch period exclusion beyond `10^1000` and a
permanent-prefix harmonic criterion equivalent to Collatz. The PR 195
guide and exact sign note show that the stronger finite nonpositivity
claim fails at depth 13. These are important constraints on proposed
next steps. This intake is not a claim that this root rebuilt every
new module or replayed every computation on those other branches.

The new Lean scope consists of the projection/record algebra, finite
group energy domination, and exact rational/integer interface budgets.
`SparseGradeProjection.lean` has 15 public theorems plus one private
translation lemma; the integration requests axioms for all 16.
`ModularZeroAtom.lean` has seven declarations. `FifthMomentBudgets.lean`
checks eleven exact budget statements. No numerical grid, asymptotic
source theorem, irrationality theorem, or universal Collatz theorem is
asserted by these modules.

The full fresh Lean and finite-control execution receipts are stored
separately. The regular control replay checks the saved fifth grid and
all rational inequalities; the root's full C++ rebuild is the separate
receipt described above. Some ancillary author controls use Python
assertions. They are checked in normal mode; optimized execution tests
whole-output reproduction with assertions disabled. The replay metadata
records that distinction. The independent three-grade and all-height
controls use explicit failures in both modes.

Integration adds the missing axiom-report requests, changes one
independent checker's default artifact directory to its repository
location, and repairs standalone square-bracket display delimiters in
the even-moment note. A trailing blank line is normalized in the all-height
review; its original bytes are retained in a JSON text wrapper. The unchanged
originals are archived and hashed.
There are no mathematical repairs to the accepted fifth certificate or
the accepted three-grade, third-layer, all-height, and sparse sources.
