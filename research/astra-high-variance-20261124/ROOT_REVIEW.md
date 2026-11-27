# Coordinating reconstruction and exact scope

**Verdict:** the specific statements below have independently reconstructed
written proofs or the explicitly named kernel proofs. Universal Collatz
closure remains OPEN. A review verdict does not cover neighboring claims or
future file versions. The fresh execution receipt binds the final file bytes.

The workers' detailed reviews are [ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md)
and [REWRITING_REVIEW.md](REWRITING_REVIEW.md). This document records the
coordinating checks, the distinctions that matter for the closing target,
and the latest-source comparison. It does not count their executions as a
fresh coordinator replay.

## Expanding comparisons and the original floor

For each source macro with \(2^Aq'=3^pq+C\), substituting
\(Y=\lambda(q+7)-7\) gives the target carry
\(\lambda(C-7\cdot3^p+7\cdot2^A)+7(3^p-2^A)\). The ten finite
reset words and three entrances are genuine ordinary residue-class
identities, not just equal affine formulas. The lifting proof in Lean derives
the required initial residue from divisibility and then proves actual
iteration on every positive lift.

The integrality step keeps one fixed infinite input. Every comparison
denominator divides a fixed power of two. An odd affine slope forces a
nonintegral binary denominator to grow with every future macro, a
contradiction. In the formal version this is a finite induction on the
required binary divisibility, using future edges of that same sequence.
There is no passage from unrelated finite examples to an infinite ordinary
source. The formal tail assumptions are the actual integral affine edges and
height at least three; infinite ordinary L/P inputs supply those assumptions.

For the original-floor entrance, the cofactor identity follows from the
light equations and the odd terminal boundary. The definition of the small
start has a nonnegative exponent when \(r\ge7\); the bound is below both
\(q_0\) and the **first actual odd intermediate** \((3q_0+1)/4\).
The latter matters because a minimum need not occur at a block boundary.
The kernel theorem `original_floor_descent` proves positivity, oddness,
both strict inequalities and literal nonconvergence. `short_paid_drop`
checks the seven short-run inequalities, while attaching those endpoints to
the rest of the given source and handling odd sources below 17 are elementary
written/finite-control steps. This is not an end-to-end Lean formalization of
all odd-gap notation and all short cases.

Both multipliers exceed one. This is consistent with earlier finite-control
obstructions that require a shrinking slope. The smaller source is purchased
at the entrance, before the expanding tail comparison. The target is not
assumed to meet the original orbit. A smaller nonconverger in another component
contradicts a **globally** least nonconverger; it would not contradict a minimum
chosen only in the original component. The result therefore uses the stated
global floor and is not a convergence theorem for that language by induction
within the language.

## All-length extensions and unbounded paid runs

In ARITHMETIC_MACRO, the required carry for \(L^KP^s\) has exact binary
denominator unless \(3K+1\ge d\). Additional L buffers cancel because the
comparison commutes with L and the forced initial residue uniquely determines
the literal parity prefix. The signed-rational argument forces all but a fixed
number of final parity bits. Once that rational orbit enters its explicitly
listed cycle, finitely many unrestricted suffix tests exclude **every**
\(s\ge3\). This is an all-length reduction to finite certificates, not an
assertion drawn from checking paid runs up to a cutoff. Concatenating singleton
resets handles all sufficiently large internal separations; the smaller
remaining separations give exactly the exception \(j=3\).

The unbounded-run supplement changes the offset instead of requiring one
offset to cover all P lengths. Its free-to-interior step, arbitrary number of
interior loops and three-P exit give every \(h\ge4\); the first three lengths
have direct certificates. The outer light buffer is **four**. Initially a
five-light version was obtained; subtracting the commuting light prefix and
checking the resulting integral carries proves the stronger four-light
version. Both offset denominators remain bounded by 4096, including arbitrarily
long interiors. The signed −10 entrance retains the same ordinary start while
the exponent s varies. For a long initial ramp its resulting value is already
an ordinary integer before the final entrance word.

An odd-excess argument would fail for unbounded paid clusters. The correct
nonconvergence proof instead uses comparison boundaries greater than two at
arbitrarily large physical clocks. An actual infinite positive L/P source
never hits one, hence its boundary states are at least three; both comparison
formulas are then greater than two. This excludes the ordinary one-two cycle.
The unbounded paid-run theorem remains a written proof with exact controls.

## Equal clocks, representatives and disjoint paths

The raw half-script has an initial odd-count imbalance of one. An ordinary
return preserves it, a six-step swap reverses it, and the terminal block
cancels it. The actual raw source counts, rather than their shortcut lengths,
are what justify equal accelerated clocks. Deleting initial/final powers of
two contributes no odd input. Each accepted script fits the prescribed
\((d+2)^3\) horizon. Equality persists at every larger common horizon, so
chains of reductions compose at their maximum, including across octaves.

Taking the least marked same-horizon representative gives a member of the
decidable S: a nonresidual candidate would have a smaller marked partner
whose earlier equality persists to the current horizon. Residual representatives
of distinct marked visits on an injective orbit are distinct even if their
settlement delays differ. The delayed state records a true endpoint on the
original orbit, and a positive subsequent search makes the endpoint times
strictly increase. This verifies the periodicity equivalence without assuming
that the residual representatives themselves form a forward invariant set.

For the whole-path cost, the intermediate comparison point at intrinsic time
\(t+h\) cannot collide with a point of another time tag after any common
future odd clock: push both beyond their separate settlement delays and use
injectivity of the original orbit. `tagged_transversal` proves exactly this
implication in Std Lean for an arbitrary deterministic map. It assumes the
given actual endpoint equalities and trajectory injectivity; it assumes no
packing, summability or Collatz conclusion. The written packing theorem can
therefore be applied simultaneously to one choice at each time, including all
disjoint replacement strips. It is not applied to the whole branching basin.

The normalized phase ratios become an integral power of two tending to one,
which forces the exact octave identity eventually. The sum of the absolute
errors is finite because the strips are disjoint. These claims concern an
escaping component. Repeated laps of a nonstandard cycle do not satisfy the
infinite injectivity hypothesis. Identity projections may cost zero, and even
proper projections can have padded separation one. Neither total summability
nor infinitely many octave drops gives a contradiction by itself.

## Quantitative phase and switching bounds

The qualitative phase law follows from the exact ordinary equation with an
error tending to zero. The quantitative law additionally uses PR193's uniform
reciprocal budget for admissible sets. A finite collision-free prefix which
later merges into a cycle need not be admissible; it has only the weaker
harmonic estimate recorded in REWRITING_RETURN. A primitive cycle lap is
admissible because later common iterates permute its states.

The publisher text of Wu and Wang's Theorem 1 was inspected directly.
Setting its independent constant coefficient to zero and choosing the two
coefficients to be the nearest-integer approximation to \(h\log_2 3\)
gives \(\|h\log_2 3\|\ge c h^{-17/4}\), with an effective positive
constant after absorbing the finite initial range. The exponential-sum
telescope and the discrepancy inequality then give exponent \(4/25\).
For visitation, the reduced Dirichlet denominator is at least the source's
octave index plus two. The rational grid, its approximation error and the
positive ordinary perturbation place a visit in the marked arc. If the source
falls below \(4N^2\) first, restarting reduces its octave by at least one half
for sufficiently large sources. The resulting geometric sum avoids an extra
power of the logarithm. The total shortcut count is at most twice the odd
count plus the initial logarithmic height. Constants are not numerically
evaluated; no practical runtime improvement is asserted.

For varying shadows, summing the shifted logarithm identity over actual
disjoint macros gives finite total variation after the explicit integer
clock correction. The three-logarithm version uses the nonzero fixed
rational slope ratio as a third logarithm. Its linear form is exactly the
sum of ordinary local corrections and endpoint errors. A lower bound for
that form forces either a sufficiently long switch or an actual small visited
state. The latter may be an endpoint. Infinite cumulative statements need
injectivity on both ordinary arms; the finite small-state implication does not.
No construction of the required incompatible switch is supplied.

## Latest-source refresh and attribution

PR182 advanced during this pass from `9b02334f...` to
`f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67`. The latter adds eleven files;
the earlier marked-return and residual-construction dependencies are
byte-identical. The new fixed-floor argument agrees with the component levels
used here. Combining it with the *even-member deletion rule* gives the stronger
pointwise fact about the entire decidable S in ARITHMETIC_FLOOR: every retained
source has first odd gap at most two. Critical marks have an actual large
projection saving, but cofinal predecessors still do not force forward
critical visits or a saving below an earlier fixed floor.

The new atomic charge obstruction in GLOBAL_RANK preserves its finite moment
hypothesis. Its rational supremum is ordinary logarithmic height on odd
inputs; the failed centerwise estimate does not refute the restricted
supremum itself. The integrality note retains the endpoint obstruction at
fixed dimension and exhibits compatible exceptional hyperplanes at growing
dimension. These are specific failed closing arguments, not impossibility
theorems for all global ranks or all Subspace Theorem applications.

INTEGER_SUMMANDS supplies changing ordinary starts with a two-summand beginning
and arbitrarily long high-complexity blocks. It does not contradict PR192's
fixed-source result. Its final suggestion that an escaping source could still
have a tight subsequence must be read as an unmet *closing hypothesis*: the
pinned SOURCE_EXTENSION theorem already excludes such a subsequence on an
escaping source. Proving that every putative bad source had one would instead
rule out escape. No upstream file was changed here, and upstream compilation
receipts are not included in this checkpoint's execution totals.

The \(60/83\) guarded comparison was rediscovered during exploration and
checked against PR191 TCP-5. It is explicitly attributed to that earlier
source and is not counted as a new theorem. The new observation is that
alignment of two infinite L/P tails is forced after they merge, so the
modulus-83 sector cannot be changed by finite component-preserving grafting.

The inverse-density and fixed-root Cantor constructions are narrowly scoped
checks of proposed recurrence inferences. The former is a different integer
map; the latter consists of actual Collatz predecessors of a specified root.
Neither is an escaping ordinary Collatz orbit.

## Final all-header extension

The all-header theorem combines the thirteen previously closed headers with
three new profiles; it does not discard the seven-light tail buffer. I checked
the two free/interior bias formulas, the source-to-target carry identity, and
the decomposition of every paid-run length into entry, interior loop and exit.
The dyadic denominator argument uses one infinite ordinary input, and the
positive boundary lower bound excludes the trivial cycle even for unbounded
paid runs. The PLLPL entrance follows the signed cycle only for a finite
initial congruence segment of an actual positive starting integer. It does
not use a negative state as an ordinary source. The low-r proof uses the
second actual paid endpoint; the high-r proof compares against both original
floors. The independent rewrite-lane review covers the final exact profile
and certificate files. This extension is written mathematics with finite
arithmetic certificates; it is outside the earlier five-macro Lean theorem.

## Direct attacks on the universal obstruction

The final reassignment explicitly sought a smaller ordinary nonconverger from
the globally least one without future-language assumptions. None of the
three lanes obtained that universal implication. The following are the
reviewed outcomes, rather than a claim that the missing step is now routine.

**CENTRAL_RETURN.** I reconstructed the least-predecessor calculation and the
zero-saving critical lift. A forward critical *image* is not a forward critical
mark. Its least predecessor beats the original m exactly at the stated
absolute-height/residue intersection. The CRT construction tests every
competing inverse exponent, not a bounded list: formal evaluation at one
has no ternary denominator and remains positive before and after its dyadic
denominator clears. The affine slope is therefore at least one. Its positive
source changes with the horizon. In the variable-offset construction,
positive initial target plus exact ordinary word transport preserves
positivity. The target's odd/raw-clock excess excludes convergence. Strict
boundary separation does not exclude unequal-clock intersection; that wording
was corrected. The bounded both-label controller obstruction follows from the
order-82 multiplication modulo 83 on the bounded all-L cycle, without a search
cutoff. This is a statement about that controller class, not all ordinary paths.

**CENTRAL_DESCENT.** I checked the odd-cylinder count, its dyadic summation and
the explicit bound E(2)=247/1512. Global minimality applies to every positive
ancestor of the actual endpoint, giving the full inverse-cost inequality.
The nearby-depth denominator estimate retains both signs of the clock defect.
The first-paid-prefix theorem reduces arbitrary shorter inverse words to a
signed integer segment after exactly four inverse raw steps. The score bound
and removal of the neutral 5,7,10 cycle justify the finite 35-start control
uniformly in r. This is a written all-r argument supported by that finite
enumeration. The inverse optimization is not shown to fail eventually, and
no theorem puts every least nonconverger in the L/P sector.

**CENTRAL_CLOSURE.** The inverse congruence gives a positive odd predecessor at
every backward step, not merely an integral final formula. The least odd
endpoint lift is paired with the least positive odd dyadic source lift.
Every higher lift has distance from the real carry exceeding 2k·3^N, giving
the stated geometric tail after summation over independent words. Monotone
convergence of the total finite source mass includes both possible types of
nonconvergence. A fixed surviving source contributes exactly x^(-s) in the
least-lift moment at all sufficiently large depths. This identifies why
discarding exponentially rare words cannot establish decay. I checked the
minimum-over-excess-level equality and the Green weight's failure of global
summability. The arithmetic lane independently reconstructed these arguments
and replayed both finite Lean declarations. The universal moment identity is
a written equivalence; its decay is the unresolved mathematical assertion.

The primary published Tao paper was consulted at Propositions 1.14 and 1.17
and Remarks 1.4 and 1.16. Its offset mixing theorem is for the stated geometric
law and an unweighted residue statistic. No extension to the tilted law or the
singular joint real/ternary observable in CENTRAL_CLOSURE was established.
The latest PR193, PR197 and PR188 sources used in this comparison are pinned
in SOURCES.json. Their newly reported Lean builds are not counted in this
packet's fresh execution totals.

The integrating pass removed one trailing space from CENTRAL_DESCENT.md after
its independent review. The mathematical text and finite control are unchanged;
the fresh source manifest records the resulting file identity.
