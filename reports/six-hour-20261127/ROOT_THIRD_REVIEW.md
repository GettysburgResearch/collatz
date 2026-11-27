# Independent review of the third six-hour packet

**Review boundary.** This review covers the exact files listed by the third
checkpoint manifest. The parent is PR201 at
`4c36876ebbe8d3cca69b2c4867aeee34f5700470`. The mathematical reviews below were
performed by the root agent independently of the three authors, followed by a
fresh Lean build and independent exact Python executions. No verdict applies to
later edits or to a full proof of Collatz.

## 1. Actual ordinary returns and paid height

**VERIFIED at the stated trajectory and leastness interfaces.** Files:
`coupling/PAID_CHECKPOINTS.md`, `PaidCheckpoint.lean`, `DelayedTurns.lean`,
`check_paid.py`, and `PAID_CONTROLS.json`, under
`research/six-hour-20261127/`.

The map is the native shortcut map, with an odd departure counted once even
when it is followed by an even departure. The parent equation is
`81*z+271=128*2^m`, with `m=11+162*j`. It implies the literal seven-clock
path from `z` to `2^m-1`, with four odd departures.

For `m=8111+13122*t`, the common parameter is
`X=2^(m-7)=502+19683*v`. The smaller canonical source is
`W=80225+3145728*v`. The two seed computations have lengths 13 and 20 and
odd counts eight and seven. Their dyadic strides are respectively
`2^13*(384*v)` and `2^20*(9*v)` after tripling on the upper arm. Thus the
displayed affine identities hold on every lift, not just the seed. In
particular the upper endpoint is `X+1`. The identity
`T^(2*n)(4^n*v+1)=3^n*v+1` gives the subsequent ordinary return. The strict
height payment follows from a checked base at `n=100` and induction. The
original exponent is far beyond that base. The separate modular calculation
maps every delayed `k=64 mod81` to this original-parent class.

For the signed-seventeen turns, the source in every theorem is a positive
natural number. The signed orbit is used to discover its finite coefficients.
The exact identity `T^11(2048*v-17)=2187*v-17` holds for every positive `v`.
For each of the five `k mod5` rows, the change in the very large exponent from
its representative `13<=k<=17` is divisible by both 11 and the relevant
dyadic precision. Consequently the remainder phase and the residue of the
earlier power of three are fixed. Literal intercept equality and equality of
the augmented slopes then give the unbounded ordinary merger. All five
classes have a positive earlier exponent more than forty below the original
one. The two original seed classes `k=376,1429 mod2187` are separately
connected to that checkpoint by positive smaller canonical sources. The
all-`k` checkpoint theorem alone does not supply such a source.

The final exclusion of a *least* canonical reverse disagreement consumes
PR197's quantitative-return theorem, pinned at
`1f0f496fbea37792439feada6106eaaff596bcd1`,
`research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean`,
declaration `CollatzQuantitativeReturn.bounded_return`. Its stated input is
an actual positive nonbasin integer and its output is a canonical reverse
defect of height at most `2^40` times that integer. The root read its
definition, soundness interface and final strong-induction consumer in the
pinned source. That external development was not rebuilt in this checkpoint.
Our new trajectory theorems do not assume that theorem. The written leastness
application does. It excludes the specified least parents and does not
independently prove convergence of every source in those progressions.

## 2. All earlier Mersennes up to a gap of five

**VERIFIED at the explicit two-hypothesis interface.** Files:
`coupling/EARLIER_OFFSETS.md`, `EarlierOffsets.lean`, `check_offsets.py`, and
`OFFSET_CONTROLS.json`.

The two consumed statements are: every positive `y` with `2^40*y<z` is
good; and every smaller positive canonical `W` satisfies
`Good(3*W) -> Good(W)`. Both are consequences of leastness together with
the pinned quantitative return, but the new Lean theorem states them as
arguments and does not hide either.

I checked the seventeen rows at even offsets 6 through 38. Their common
parameter `2^(m-80)=35+243*v` applies to every `m=173+162*j`. The source and
triple strides are divisible by the full lengths of their respective
prefixes. The recorded odd counts therefore prove both endpoint identities
on the whole progression. Each upper endpoint has a literal remaining odd
ascent to a strictly earlier Mersenne peak; the inequality in the exponent
has the required sign. The same constant and slope inequalities establish
positivity, canonical residue and `W<z`.

Strong induction on the earlier Mersenne exponent uses the forty-bit floor
for distant exponents, the genuine adjacent even-index merger for even
exponents, and one of the seventeen rows otherwise. The small original
`m=11` case is checked directly through `M_6`. This proves all positive
`M_t` with `t<=m-5` good. A first bad exponent must consequently be one of
`m-4,m-2,m`; this says nothing about which later exponents might also be bad.
The Lean `gap_five_return` accepts independent clocks on the two physical
peaks and proves goodness of the original parent from an actual merger.

The root also read the updated PR195 at
`03b26119164664d08eaa04a1ea1d159dd4eccd7a`,
`research/astra-six-hour-20261127/ordinary/README.md` and the corresponding
statements in `OrdinaryPower.lean`. Its gap-five two-sign mergers and
gap-five/gap-nine all-base power mergers are stated independently of its
bounded-cycle floor. Therefore replacing that floor consumer with our new
cutoff is valid. This gives a written least-parent exclusion for its
all-base degrees `d>=494`, even-base degrees `d>=63`, and the specified
signed multiplier classes. The physical merger is credited to that source;
it was not rebuilt here. The resulting conclusion remains a leastness
exclusion, not unconditional convergence outside those hypotheses.

## 3. Finite period and complete denominator screens

**VERIFIED as a written finite argument with exact computational evidence;
only the three advertised arithmetic lemmas are formalized.** Files:
`arithmetic/PERIOD_GAP.md`, `PeriodPacking.lean`, `check_period_gap.py`, and
`PERIOD_CONTROLS.json`.

I reconstructed both sides of the middle-numerator count. A fixed past of
`k` odd steps constrains that numerator modulo `3^k`; a fixed future with
total exponent `A` and odd last numerator constrains it modulo `2^(A+1)`.
Their coprimality gives the complete product modulus on the same numerator.
The actual bin has width at most `S/b`, so a half-open bin contains at most
the stated ceiling. Including incompatible pairs of words only enlarges
this upper bound. No independence between the two digit systems is used.
The denominator-13 five-cycle checks why the spacing must act on numerators
rather than rational physical values.

The finite path product error is below `100001/100000` for all windows used
at minima at least `2^30`. The reverse and forward grade inequalities in
the implementation follow with the stated directions from the physical
ceiling. Their grade search bounds include every allowed total. The initial
whole-strip count retains every possible reduced clock ratio.

For ordinary cycles below eight times their minimum, the ordered dyadic lift
has no inversion and acts by rank translation. This proves the needed
coprimality of period and total exponent. It also identifies the unwrapped
rank position before reducing modulo a period. The error from uniform
logarithmic rank is a difference of the averages on two complementary arcs,
bounded by `p/(12*s)`. The improved height bound and the required population
of every logarithmic bin follow with conservative errors. The three physical
bands are bounded separately and then summed. Rational-cycle tests assume
coprimality explicitly and use only the initial whole-strip count.

I inspected the integer logarithm enclosure and Farey enumerator. Repeated
downward division loses less than the recorded allowance; the discarded
tail is covered. Consecutive boundary fractions have determinant one and
denominator sum above the order. The modular-inverse successor therefore
visits every reduced fraction in the interval, not just convergents. The
first fraction at the full order exceeds the upper logarithm enclosure,
giving the finite maximum height index 6640. The largest word window is
4248, within the proved correction allowance of 10000. Independent literal
small-word and small-Farey checks exercise those routines.

The replay returns 125 first-pass pairs and 25 pairs after the joint rank
screen. Their largest period is `31150961018190238869556`; none is a cycle
construction. Minima below `2^71` cannot support more distinct integer
phases than that threshold, so the displayed finite period gap requires no
external trajectory census. Using Barina's published census to impose the
`2^71` minimum is separately source-qualified. Each of the three rational
tests excludes every pair in its stated interval for its *full reduced*
denominator cap. There is no enumeration beyond period `10^1000`.

The discussion of Chudnovsky's `mu(log_2 3)<=3` is an external analytic
input for a proposed asymptotic route. It is not used in these finite
results. The existing count exponent is too large for that route to close.

## 4. Unrestricted visitors and the fixed-source boundary

**VERIFIED written derivation relative to the explicitly cited all-time
transfer; finite inputs independently kernel checked.** Files:
`escape/UNRESTRICTED_VISITORS.md`, `VisitorAnchor.lean`,
`check_visitor_anchor.py`, and `VISITOR_ANCHOR_CONTROLS.json`.

The root checked Weaver Paper1/v3, Lemma1, Theorem2 and Lemma3 in the
primary text. In particular shorter suffixes remain division-minimal even
when they start with two. A whole word starting with one has the full
positive-offset cone, and an excess of one forces offset one.

The inverse first-crossing words have legality mass times squared gain
equal to their probability under the independent letters `3/4^e`.
Prefix-freeness gives the inverse-gain tail without claiming that legality
events themselves are independent. On a ternary source ball of depth 128,
the first 128 inverse decisions are shared with each positive integer
offset. A strict early violation would come from source 1 or 3, whose
ordinary trajectories exclude it. At exactly that depth every remaining
endpoint is uniform on a full ternary ball, permitting the same tail bound
for its continuation.

Summing first over eligible powers of two and then over the actual positive
integer inverse endpoint is legitimate by nonnegativity. For a fixed
endpoint there is just one ordinary target at the specified depth. The
finite 2048-source computation supplies the gain reduction for sources at
most 4095; a reciprocal-square tail bounds all larger sources. The final
exact loss is below one percent. This proves one simultaneous Haar event
for all words in the language, with a unique principal gain winner.

For each fixed finite word, dyadic legality and the ternary conditions
transfer by CRT at a finite visitor deadline. The root checked the exact
late-arrival statement in Paper178/v1, Section2, and its cited
Paper177/v1, Section8, estimate (3). A failure after the deadline has a
least positive ancestor whose first arrival stays above its own source;
its target lies in that estimate's range after a constant rescaling
depending on the fixed word. This gives the stated `O_w(rho^J)` error and
justifies removing every visitor clock. No uniform onset in the word is
asserted. This external transfer was inspected, not formalized in our new
module.

The additional good-basin corollary states both further inputs: counted
fixed-shift fusion and positive lower density of the target-one basin.
The latter is the specified Mazur theorem M. Its public primary statement
was inspected in this pass, but the advertised external formalization was
not rebuilt. A classical sublinear predecessor bound would not suffice.

Finally the root checked the ternary-coordinate-15 control. The finite
closed set contains every odd start below 20 and misses 31 and every
candidate target at least 61. The branch at 15 itself cannot extend in
inverse odd depth. This proves all-horizon calibration at that ternary
coordinate. Its actual fourth gap is five, so the same integer cannot
realize any infinite script in the stated language. The positive rational
symbolic terminals do not supply the missing ordinary diagonal.

## Execution record

[THIRD_REPLAY.json](THIRD_REPLAY.json) contains the exact source hashes,
commands, compiler and mathlib pins, all forty audited declarations, and
the four complete normal/optimized control comparisons. Twenty declarations
are new and twenty belong to freshly rebuilt dependencies. Only
`propext`, `Classical.choice` and `Quot.sound` occur. No `sorry`, new axiom
or `native_decide` is used in the new modules.

The initial combined driver recorded all eight successful Lean modules,
then its process handle became unavailable before a complete control
receipt could be retrieved. A complete separate control execution passed.
The combined receipt preserves those two execution boundaries explicitly;
it does not invent a successful final status for the first driver.

**Still open:** the remaining actual-parent returns, ordinary positive
realization of an infinite expanding script, cycle exclusion at the
surviving pairs and beyond the finite cutoff, and the global Collatz claim.
