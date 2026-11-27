# Second checkpoint: independent reconstruction and corrections

**Collatz remains open.** This review concerns the second checkpoint after
`07ae08382588992c1b7f7a60cd331a6647177495`. The six-hour research session continues.
The [source manifest](WAVE2_SOURCE_MANIFEST.json) records the original and
integrated content hashes. The [late intake](LATE_INTAKE_SNAPSHOT.json) pins the
specific files inspected at advanced PR193, PR201 and PR206 heads. It is a source
inventory with explicit read scopes, not a claim to have validated every other
branch or rebuilt its formal development.

## Corrections preserved at their exact boundaries

Independent review found two mathematical wording errors and one inaccurate
description of finite output. The original files remain in `source-originals/`.

| Source | Correction and counterexample | Integrated SHA-256 |
|---|---|---|
| `ADAPTIVE_TERNARY_ANCHORS.md`, Theorem 1(1) | The anchor set is exactly the height ball. Merely containing it permits arbitrarily large extra anchors: at source 1, height 1, adding `3^k-1` makes every depth at least `k`. | `5334bbacc71d3564b19f00490483edc6e588772ccc0f3008540112f5cdf5f086` |
| `ADAPTIVE_POSITIVE_ANCHORS.md`, Theorem 4 converse | After lifting a positive hit, retain only visitors `y <= n`. At phase 17, `R=7,z=3,n=12271,A=1,s=1`, the principal cut and the fixed positive hit `1 -> 1` lift to `16361 > n`. They give a visitor, not a source below the cutoff. | `4855c23fcbd0cf4a0637fd43b0257edf4c378fa102006355d0e4965c37d9ed9e` |
| `ORDINARY_OVERHEAD_SPECTRUM.md`, replay description | The author's program internally enumerates all successful triples; its JSON records ranks and selected witnesses. The new independent program actually replays all 35 tuples on all seven phases. | `ee28a8f5067f991ee1d9e8aaad10a14cdb8d0c3a7aac700b596805f7437814f9` |

The first reviewer checked the minimal anchor-set repair by byte comparison. The
inverse reviewer separately checked both corrected inverse texts and confirmed
that these changes resolve the identified findings. These are corrections to
the statements and evidence descriptions, not new hypotheses in the already
checked Lean minimum theorem.

## Rational anchors: exact transport, local escape and path compilation

The root independently reconstructed both the frozen anchor argument and its
later signed-family extension. Let `2^e y = 3x+1`, and choose successive reduced
anchors `p/q,u/v`. The discrepancy is

\[
 D=2^equ-v(3p-q)=2^eq(vy+u)-3v(qx+p).
\]

For denominators prime to three, the minimum of the second depth and one plus
the first depth divides `D` ternarily. At a nonzero discrepancy at least one
endpoint is finite, including when a signed anchor coincides exactly with the
other endpoint. If `3|qu`, the discrepancy is a ternary unit. Otherwise Yu's
Theorem 1 applies to the rational units `2,qu/[v(3p-q)]`, with exponent vector
`(e,1)`. The root directly read the primary theorem and checked its rational-field
condition, nonvanishing, height cutoffs and absence of a multiplicative
independence assumption. The stated coefficient `1.2*10^12` bounds the
displayed natural-logarithm estimate on printed page 337. This is an application
of an external theorem, not its formalization here.

On an exact interval of `k` edges and division sum `E`, clearing the two endpoint
denominators gives

\[
 2^E q_0(q_kx_k+p_k)=3^kq_k(q_0x_0+p_0).
\]

If the starting displacement is nonzero, coprimality gives
`2^k <= H^2(x_0+1)`. The final denominator cannot be dropped unless it is odd.
Combined with the actual ordinary growth bound this forces a discrepancy in
the stated initial and dyadic windows. A closed cycle of exact edges would
instead force `2^E=3^P`. The signed window version correctly requires a
nonzero starting displacement; starting above the anchor height suffices.

The root also reconstructed the finite compiler for *all* signed rational
anchors. Binary-unit anchors have at most one unit successor. After leaving
that sector a path uses at most one even-integral state, then its negative
binary valuation strictly decreases. For an even-denominator path, its two
endpoints determine its total exponent. The positive word code

\[
 C(\varnothing)=1,\qquad C(e::w)=3^{|w|}+2^e C(w)
\]

is odd and injective at fixed length: the valuation of the difference from
`3^(k-1)` determines the first exponent, recursively including the last one.
Actual anchor transport gives `C(w)=3^k t+2^E(1-u)`. Consequently there is at
most one path for specified endpoints and length. There are at most `M^2`
terminal paths from a vertex of the acyclic sector. Grading by their count
proves the compiler cost `O_epsilon(M^(1+epsilon) log(2H))`, with only
`O_epsilon(1)` pieces along any supplied path. Prefix-incomparable maximal
same-grade paths have disjoint full extensions, which is the needed counting
argument even when paths merge later.

Weaver Paper 15/v2's adaptive dictionary inequality and cyclic inequality are
used with their exact stopping conditions. A non-eventually-periodic positive
orbit enters no represented positive cycle. In a primitive `P`-cycle a
dictionary of total budget below `P` cannot represent that cycle. These give
the many-clock bound for sublinear-sized signed families. The full positive
height-ball corollary splits at `H=log N`: the smaller ball has only
polylogarithmically many vertices, while the larger ball is controlled on an
early interval by the elementary real-height bound. It supplies many prefix
clocks, not many clocks in an arbitrary late window. The primary statements of
Paper 15 were inspected; its deep proof chain was not independently rebuilt.

The [fresh anchor review](ADAPTIVE_ANCHOR_REVIEW.md) covers the original theorem,
its repair and an independent functional-graph construction. The signed compiler
extension has the separate root reconstruction above. `AnchorPathCode.lean`
checks the finite code and transport identities, not graph compilation or the
external analytic estimates.

The fixed-source negative-17 packing theorem uses the already formal exact
minimum on seven phases. Its sharp local constants, nonoverlapping interval
product and actual accelerated clock correspondence were reconstructed. Even
covering an entire orbit by its permitted intervals would still allow the
positive residual growth factor `2187/2048`; the packing estimate alone is not
descent. The qualitative address-duration principle has a prior in Paper 108.

## Positive endpoint reduction and exact additional budgets

The root read every definition and proof in the three new positive modules.
`Ancestor` still means a positive odd ordinary source, a physical shortcut
iterate, and its actual count of odd departures. Positive projection retains
parity and available ternary rank at every intermediate edge. Its inequality
`X*w <= a*y` is derived from the actual affine path. The converse lift retains
the exact same two clocks. The final `bounded_anchor_query` is an iff, including
the source cutoff after lifting.

`PositiveBudget.extension_lower` proves, for an arbitrary ordinary minimum,

\[
 M_{R+s}(X)+1\ \ge\ (2/3)^s\bigl(M_R(X)+1\bigr).
\]

Its cut is an actual positive odd state, not an extension of the signed
projection beyond its funded rank. If `3^s` divides the minimum plus one, the
all-one inverse word attains equality. `PositiveApplications.seven_phase_sharp`
therefore gives a full formal arbitrary-extra-depth minimum on the indicated
divisibility class. This is distinct from the written protection theorem on
the class where `3^s` divides the minimum itself.

For the three-extra and fourth-extra classifications, the root reconstructed
the cut at the first extra positive edges. The remaining `R` edges project
legitimately. The strict size cutoff reduces the off-principal signed
magnitudes to `33,45,67`. The inverse affine offset for four edges is at most
`65/16`. Every case is dominated except the reverse word `(2,1,1,1)` from
`2n+1`; its exact legality is `n=60 mod 81`, and its source is
`(64n-33)/81`. In that class `3|n`, so no additional odd ancestor of `n`
competes. This affine expression and congruence have prior appearances in
Paper 1; the new classification is on these seven marked cylinders.

For arbitrary extra budget, the ratio bound on a distinct signed tail and its
replacement by full marked laps forces a terminal dictionary of residual
depth at most `1406+50s`. The root checked the three exact constants governing
the tail cutoff, the legal residue dependence and the finite exponent bound.
This extends the earlier eventual finite-dictionary mechanism; it is not a
universal forward merger selector.

## The matching-depth cone and the complete small-overhead spectrum

At matching depth every nonprincipal cut has the form `2^D n+c`, with
`D>=1` and `0<c<17*2^D`. The proof needs the strict sign of `c`. The root's
separate program reconstructed every odd reflected input through 91 and the
phase-compatible product comparisons for lengths 1 through 14. The minimum
ratio is exactly `9730834/9637047`. Appending seven larger off-cycle values
propagates this bound. The root also independently followed the complete
positive pool below 17 and all 33 candidate pairs in the zero-anchor screen.

If `3^s|n`, an extra positive projection at `c` is funded for `s` steps. A strict
challenger then gives a positive root below 17, and the finite signed grade
screen excludes it. Allowing `h` further steps changes that root pool to
`w<17(3/2)^h`. The exact two-parameter criterion retains the ordinary endpoint
`c=U^s(w)`, its total exponent `E`, a signed first-17 grade
`(7l,11l+D)`, and the strict inequality `2^(D+E+h)<3^(s+h)`.

Necessity uses only the actual cuts and shifted-height inequality. Sufficiency
chooses `n=3^s N` by two independent congruences, then lifts the signed word,
the supplied positive word and the final `h` one-exponent inverses. Arbitrarily
large positive CRT solutions ensure strict improvement. It is existential
over cofactors, not a decision about each prescribed cofactor.

The all-`s` result for `h<=6` is not a capped search in `s`: the entire finite
positive pool through 193 reaches 1, and subsequent inverse multipliers grow
by `4/3`. Each row has a proved cutoff. A fresh independent program checks
all 35 successful tuples and all 245 seven-phase CRT concatenations. The
[inverse review](INVERSE_WAVE2_INDEPENDENT_REVIEW.md) gives the full narrow
verdicts, source comparisons and the two corrected passages. In particular
`M_(R+s+2)(X)=n` holds for every `s>=1` with `3^s|n` in the matching-depth setup.

The stopping-time transfer and fixed-source delay are written results. The
root directly inspected the resident finite-simple-path reciprocal proof
T-A3-651, including the discarded terminal states, short-word count and
distinct-endpoint estimate. Its use is separately identified. Weaver's
dictionary complexity provides only the stated additional delay. Paper 180
already uses a second positive anchor and a different recurrence-to-failure
criterion; these broad techniques are not claimed as new.

## Complete cycle denominators and ordinary clock estimates

The root independently reconstructed all five new written cycle manuscripts.
The [fresh cycle review](CYCLE_WAVE2_INDEPENDENT_REVIEW.md) supplies a second
reconstruction, including primary-source checks and different finite controls.

For moving coefficients the root checked the saturated kernel of normalized
valuations, the fixed fast-character basis, individual small coefficient
heights after factorization, and the application of Grieve--Wang's outside-place
gcd theorem on each putative bad subsequence. Its exceptional character is
fixed on a subsequence and contradicts the fast-coordinate construction.
Specialization along the ternary valuation freezes all coefficients; widths
of nonzero Laurent factors add. This proves the retained factor bound for a
fixed number of moving terms, or a fixed number of sublinear rectangles. No
bound for an arbitrary growing number of rectangles follows.

For the ordinary clock estimates, the root reconstructed two-ended integer
separation, the one-sided slope bound, the finite circle mesh and the cover by
arbitrary odd-time arcs. An extensive clean interval forces bounded-order
near-resonance. No argument forces such an interval in every ordinary word.
On one nonrepeating fixed source the logarithmic correction is `O(log N)`
by distinct ordinary states. The normalized profile conclusions therefore
refer to its actual endpoints. Cyclic windows in a finite prefix are only
symbolic comparisons; cutting at the two artificial seams recovers genuine
shared intervals. In the specified initial-overlap case the earlier matched
terminal is both exponentially large and exponentially smaller than `3^H`.
This excludes every small signed rational representative at that matched
depth, including the full displayed PR206 denominator range. It does not
exclude a different depth, a different record or a different approximation.

The four-defect construction computes the *complete* phase denominator.
Inactive cyclotomic polynomials divide the carry jointly before evaluation;
separate integer-factor divisibility would not suffice. Active-order gcds
are bounded by fixed positive weights. These estimates retain overlapping
prime powers. The changing prime-set degree density fills `[1/2,2/3]` after
the explicitly ordered diagonal limit, while the same sparse residual always
has gcd fraction `2/3`. Thus exact residual-slope rationality cannot be
transferred through an arbitrary resonant multiplier.

The dense construction superposes two periodic offset families and gives a
full denominator dividing their lcm. Its bounded-difference calculation
retains all repeated occurrences of each random bit. A union bound controls
every shift; counting reduced least phases gives the actual denominator
lower bound. All phases are uniformly quadratic in the block length, yet
every lag has a positive density of defects and the denominator is
subexponential in the total period. These are rational cycles with growing
clock gcd. The existing phase-order result in Paper 114 already excludes
integer realization for narrow words with such a nontrivial gcd. The examples
disprove the proposed rational structural implication; they do not remove
that ordinary arithmetic discriminator or settle the coprime case.

The independent direct-word controls include shared prime factors across
active and inactive cyclotomic orders, and an exhaustive small shared-bit
ensemble. They support these specific interfaces. They do not replace the
asymptotic existence and probability arguments. Prior sparse residual,
native Hamming, phase-order and source-count results are credited explicitly
in the reviews, including Papers 22, 114, 145 and 218.

## Formal, finite and unresolved scope

The root's fresh build contains seventeen local Lean modules and 160 audited
theorem declarations, including all private lemmas. Every project object is
rebuilt. Only the standard `propext`, `Classical.choice` and `Quot.sound`
dependencies occur; the pinned external Mathlib build and two rebuilt missing
dependency objects are specified in [LEAN_WAVE2_RECEIPT.json](LEAN_WAVE2_RECEIPT.json).
The new analytic estimates, graph counts, moving gcd theorem and asymptotic
cycle constructions are written proofs with the stated external inputs.

The control runner compares complete normal and optimized output to frozen
JSON. The independent inverse checker has a portable integrated variant:
only its original author-directory hash verification and two provenance
fields are removed. Its arithmetic is unchanged, the original source and
execution output are preserved, and the integration manifest checks the
packaged identities. The final control receipt lists every executed program
and imported local dependency.

The missing implications remain precise. No theorem forces a smaller ordinary
visitor on the future of every supplied source. No theorem excludes the
integer denominator one at every unrestricted cycle word. The escape trace
still carries a possible positive ordinary component charge. The new
exceptions, sparse recurrence work and language restrictions must be connected
to one of those universal obligations before a full proof can be claimed.
