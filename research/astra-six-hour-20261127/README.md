# Ordinary source closure: six-hour research pass

**Status: research checkpoint; Collatz is not proved.** This packet pursues the
full positive-integer problem from the exact geometric Syracuse law, complete
cycle denominators, and global component colorings. It builds on the preceding
[three-hour pass](../astra-unconventional-20261126/CLOSING_PROPOSAL.md) and the
five changed research heads recorded below. It does not replay earlier bulk
verification or import their branch histories.

Start with [the full-problem proposal and synthesis](FINAL_PROPOSAL.md) for
the exact final Lean implication, the remaining estimates, and the combined
results of this six-hour pass.

The odd map is `U(x) = (3*x+1)/2^v₂(3*x+1)` on positive odd integers. The
shortcut map is `T(x)=x/2` on even integers and `(3*x+1)/2` on odd integers.
The density `rho_k` has mean one on `Z/(3^k)`, and its defining independent
gap has probability `2^(-e)` for `e>=1`. No inverse policy replaces that law.

## The escape attack

[Exponential dust](escape/EXPONENTIAL_DUST.md) gives a source-qualified written
decomposition of the original finite harmonic mass. Its diffuse part has a
uniform fixed dyadic residue at each specified depth. Its atomic part retains
the actual ordinary rays and their positive component charges. This removes
the clipping function from the preceding escape detector.

For the literal modulus-eight test

\[
 (W(1),W(3),W(5),W(7))=(-1,3,-5,3)/4,
 \qquad Z_k=\sum_{\substack{1\le y<2\cdot3^k\\y\text{ odd}}}
                   W(y)\rho_k(y)/y,
\]

the proposed asymptotic theorem gives

\[
 \liminf Z_k/k\ge(7/4-\log_2 3)\sum_{C\text{ escaping}}H_C.
\]

Every nonempty positive escaping component has `H_C>0` under the retained
predecessor and passage inputs. [The Dirichlet completion](root/DIRICHLET_TRACE.md)
replaces the moving endpoint interval by an ordinary convergent series `S_k`
with the explicit depth-independent bound `|S_k-Z_k|<=5/8`. It is the fixed
character combination

\[
 4S_k=-3L_k(1,\chi_{-4})+L_k(1,\chi_8)+L_k(1,\chi_{-8}),\qquad
 L_k(s,\chi)=\sum_{n\ge1}\rho_k(n)\chi(n)n^{-s}.
\]

Proving a nonpositive lower normalized subsequential limit of that expression
would exclude every positive escape. **That sign assertion is open.** These
series retain the periodic coefficient `rho_k`; they are not ordinary
multiplicative Euler products.

Two additional written results describe the actual inverse process at every
ordinary root: [canonical path laws](escape/CANONICAL_INVERSE_PATHS.md) give
geometric-word frequencies, an iterated-log fluctuation bound, and polynomial
growth of the canonical trace along typical paths;
[real fibres and the traveling front](escape/REAL_FIBRE_AND_FRONT.md) identify
full-dimensional singular real fibres and a common two-sided escape profile.
They explicitly retain target-dependent entrance clocks. Singularity of normal
legal rays, including the first-minimum-cell result, is credited to Weaver's
paper 175. These are analytic written deductions from cited inputs, not Lean
theorems in this packet.

## Second checkpoint: closed support and exact entrance structure

[Closed correction support](escape/CLOSED_CORRECTION_SUPPORT.md) proves, with
its named analytic inputs retained, that the closure of **all** finite first-hit
real offsets at every positive odd root has Lebesgue measure zero. The argument
includes exceptional zero-probability inverse paths. It uses one canonical
singular measure, a uniform local-mass lower bound obtained from the selected
joint floor, and the finite-crossing argument. For an escaping component the
closure of its all-future correction values is likewise null and has Hausdorff
dimension one. The source-qualified written theorem settles the specific
closed-support length question described in Weaver 175 §12, conditional on the
cited inputs. The analytic inputs and their Collatz application are not fully
formalized by the generic Lean reduction.

[Graded correction sets](escape/GRADED_CORRECTION_SETS.md) identifies the
countable compact correction set at each fixed odd grade: its successive
Cantor–Bendixson derivatives advance the grade, and the omega derivative is
`{1}`. Every sufficiently high dyadic corrected-height level nevertheless
contains at least `c*(4/3)^b/sqrt(b)` actual sources. These are structural
restrictions on a hypothetical escape, not its exclusion.

[Primitive characters](global/PRIMITIVE_CHARACTERS.md) gives an exact
conductor-by-conductor recurrence for the original ternary law. The Jacobi/Gauss
matrix has tight **columns**, while the weighted normal operator has both
expanding and contracting directions. This prevents replacing the remaining
signed Dirichlet problem by a false operator-norm contraction.

[Canonical births](global/CANONICAL_BIRTHS.md) counts representative-window
entrances exactly. With the actual corrected reciprocal weights the limiting
last-gap current is `-log(2)/2`. The **next-gap** current relevant to the escape
trace cancels uniformly for ages `s <= c*(k+j)`, for every
`c < log₂(3)/2`. This handles a positive proportion of entrance cohorts at a
terminal depth. It does not control the older cohorts. The different time
indices and measures are explicit in the note.

[Positive ternary quotients](arithmetic/TERNARY_QUOTIENT.md) express every phase
of the bounded bad-cycle alternative by a smaller positive good integer. The
induced defects alternate `+1` and `-1`; the negative switches still require a
changed-clock ordinary descent. The [component complexity note](arithmetic/COLOR_WORDS.md)
also retains an actual finite-exception coloring control, preventing an entropy
argument from silently ignoring the exceptional edge.

The claim-level reconstruction and exact verification boundary are in
[SECOND_REVIEW.md](../../reports/astra-six-hour-20261127/SECOND_REVIEW.md).
[LEAN_SECOND.json](../../reports/astra-six-hour-20261127/LEAN_SECOND.json)
records all nine fresh project builds and 73 public axiom inventories. The
new character checker uses exact finite fields and rational arithmetic at
`q=9,27,81`; both normal and optimized executions retain every check.

## Third checkpoint: explicit finite proposal and specified-source probe

[The rational Green proposal](root/RATIONAL_GREEN.md) defines positive rational
finite sums over actual ordinary trajectories. Its coefficient is
`c_e=(134/25)*(5/14)^e`; the corresponding ternary Green series has Haar
integral 135. A uniform bound `R_(K,H)(y)^2 <= C*y^3` would settle the entire
positive-integer problem. The new Lean theorem proves that implication through
the usual full Collatz map, with the finite-sum bound retained as its explicit
premise. The bound is **open**. The note also records its extra consequence:
finiteness at 1 would force a uniform logarithmic first-hitting bound on all
terminating sources. The adaptive replacement in the fourth checkpoint removes
that extra fixed time tilt.

[The real tilted Green analysis](global/TILTED_GREEN.md) identifies the exact
cycle and escape lower bounds, dense infinite values at positive nonintegral
dyadic centers, and the ordinary source-height cost of a long negative shadow.
Its integrable ternary average does not control the ordinary integer values.

[The Poisson source probe](escape/POISSON_SOURCE_PROBE.md) retains one specified
ordinary source in an exact signed binary Fourier formula under the original
geometric law. It includes a finite-depth, arbitrarily high order readout of
that source's actual multiplier, uniform in the smoothing width. All long
clocks above the stated source-dependent cutoff can be removed absolutely.
The signed cancellation on the surviving clocks remains open. Independent
orbit and Fourier computations agree in all 20 retained numerical cases;
this is not a rigorous floating-point error certificate or an asymptotic proof.

[Cycle surgery](arithmetic/CYCLE_SURGERY.md) computes the complete reduced
denominator after replacing any contiguous interval of an actual integer cycle.
Together with the retained two-logarithm separation, a nontrivial replacement
of sublinear total length has an exponentially large rational denominator.
This controls perturbations of a hypothetical cycle, without excluding the
cycle itself.

[THIRD_REVIEW.md](../../reports/astra-six-hour-20261127/THIRD_REVIEW.md) gives
the claim-level scope. [LEAN_THIRD.json](../../reports/astra-six-hour-20261127/LEAN_THIRD.json)
records thirteen fresh module builds and 112 public axiom inventories. The
two new full-problem conclusion theorems are conditional, and no Green bound
or positive bounded potential is asserted as a proved premise.

## Fourth checkpoint: adaptive energy and an RH-assisted cycle estimate

[The rational energy proposal](root/RATIONAL_ENERGY.md) replaces the constant
time tilt by a rational factor `1+1/(32*n²)` at odd states at least 13, and
`1/4` at smaller states. It sums the resulting weights over actual visits,
with a summable `1/x³` weight on each initial source. Lean proves that a uniform
bound of 8 and uniform decay as the target tends to infinity imply full
Collatz convergence. Both estimates remain open. A written converse uses
telescoping products on simple paths, showing that this criterion asks for no
additional stopping-time bound.

[The adaptive ternary Green series](global/ADAPTIVE_GREEN.md) supplies a
computable rational construction for that criterion. Its boost depends on the
least positive representative of each prefix. It is Haar integrable, has
uniform ordinary bounds at every nonperiodic target, and has a polynomial tail
away from all trajectories of a fixed finite set of sources. The discrepancy
from the ordinary positive recursion is globally summable. The remaining
issue is decay along those fixed-source trajectories themselves; none of the
average estimates supplies it. Nine new Lean lemmas check the coefficient
inequalities, including domination of the rational energy.

[The Mellin rank estimate](arithmetic/MELLIN_RANK_SPACING.md) uses Lindelöf
and the Robert–Sargos fourth derivative estimate to bound, at every fixed
amplitude `c <= R <= C*p^(11/20)`, the number of pairs with
`||R*(2^(j/p)-2^(i/p))|| <= C0/p` by `O(p^(1+epsilon))`. The RH input is
supported by the November 2026 MIT verification record; that external proof
is not imported or rebuilt in this packet. Applied under the exact ordered
three-band hypotheses, this gives the minimum-size exponent
`1000/479+11/20 = 2.63768...` for an unbounded sequence of ordinary cycles in
that branch. It does not exclude the remaining range or arbitrary cycles.

[The Poisson clock spectrum](escape/POISSON_CLOCK_SPECTRUM.md) identifies the
limits of the original signed-word statistic at depth `C*log(R)`. Each
positive cycle's basin contributes a transition at its own contraction rate.
The first transition comes from 1 exactly as the Fourier clock cutoff passes
the mean of the original geometric total. Its unevaluated size is the density
of convergence to 1. [Ternary rational shadows](escape/RATIONAL_WINDOW_SHADOWS.md)
give new finite-deadline obstructions inside positive translated intervals,
and a separate consequence of the p-adic Subspace Theorem shows that every
fixed escaping ordinary ray has arbitrarily long blocks avoiding all the
displayed bounded-complexity rational shadows. A converse classifying delayed
windows is still missing.

[Two-width isolation and first return](escape/FIRST_RETURN_POISSON.md)
removes every terminal other than 1 from the original finite statistic with
a power-saving error. Its stationary Mellin transform has residue `d1/2`
at zero and at least one genuine nonreal lattice pole, by singularity of the
wrapped exit law. This identifies the exact reciprocal exit moment to
evaluate; it does not evaluate that moment as the value needed for `d1=1`.
[Sparse shadows](global/SPARSE_SHADOWS.md) strengthens the ordinary-ray
arithmetic exclusion to exponential-width neighborhoods of nonzero ternary
multiples and signed binary approximants with any fixed number of digits.
Both exclusions hold on the same long blocks, with a linear upper bound on
the waiting time in the current orbit index.

[The binary bridge pressure](arithmetic/BRIDGE_PRESSURE_THRESHOLD.md) computes
the exact limiting fourth-energy rate from the three return words. Its
critical fixed width lies in `(1.98534327,1.98534329)`. With the pinned
external source estimate this gives fixed-denominator finiteness below that
width, with ineffective onset. The same exact transfers show that every
fixed even moment of the unforced two-layer population exceeds the rate
needed by the stated equal-length bridge argument. Normal and optimized
executions of the rational certificate agree byte for byte.

[FOURTH_REVIEW.md](../../reports/astra-six-hour-20261127/FOURTH_REVIEW.md)
records the statement-level scope. [LEAN_FOURTH.json](../../reports/astra-six-hour-20261127/LEAN_FOURTH.json)
records fifteen fresh module builds and 130 public axiom inventories.

## Final checkpoint: actual-source limits and arithmetic relations

[The critical Poisson profile](escape/CRITICAL_POISSON_PROFILE.md) proves a
source-qualified Gaussian transition at the first jump, retaining the two
first-hit clocks and the real correction. The width is independent of the
power of the smoothing scale. Its amplitude remains the basin density of 1.
[Critical support neighborhoods](escape/CRITICAL_SUPPORT_NEIGHBORHOODS.md)
uses the exact odd-integer mesh to give a lower bound of order
`1/sqrt(log(1/epsilon))` on neighborhoods of the entire closed correction
support. These are written deductions with their analytic inputs retained.

[The positive trace budget](escape/POSITIVE_TRACE_BUDGET.md) gives
componentwise actual-tree formulas and a power-decaying tail for all
nonperiodic stationary loss terms. The total budget and its exact
finite-depth difference are credited to Weaver 176, where they already
appear. Rational outward enclosures show that its finite increments have
both signs. [Stationary selection](escape/STATIONARY_SELECTION.md) shows
that harmonicity, finite point data and finitely many exit moments alone
cannot replace the individual-depth selection of the genuine law.

[Stopped-row decay](escape/STOPPED_RATE_TEST.md) and the
[finite endpoint mark](escape/ENDPOINT_RATE_TEST.md) combine into one
nonnegative original-law statistic. A polynomial prefactor times `(2/3)^j`
on one unbounded subsequence would exclude both escape and extra cycles.
The upper estimate is open; the lower detections retain the actual ordinary
source and avoid signed cancellation. [Marked solenoid mixing](escape/MARKED_SOLENOID.md)
extends Haar mixing to integer-labelled covers with an explicit range,
without asserting control at a fixed arithmetic fibre.

[Positive rank division](arithmetic/RANK_DIVISION.md) forms short bounded
positive combinations of a candidate cycle's own phases while retaining
every prime power of its complete denominator. The
[tagged version](arithmetic/RANK_DIVISION_TAGS.md) can preserve both finite
native digit windows at all phases simultaneously. Its output still has
signed forcing and many spatial reversals. Three Lean identities check the
finite cancellation, integrality and denominator argument.
[Local Hankel rank](arithmetic/HANKEL_RANK.md) excludes a fixed rational
linear dependence across a whole explicit consecutive window, including
all rank-boundary doublings. It does not bound the sizes of the minors.
[Binary-past cubes](arithmetic/BINARY_PAST_CUBES.md) attain the sharp
four-sum energy on genuine fixed-total words, all realizable on one finite
ordinary path of ratio below `8/3`. This rules out a proposed stronger
local energy estimate, without supplying any periodic path.

[Positive S-unit shadows](global/POSITIVE_SUNIT_SHADOWS.md) uses the
finite-rank equation theorem to exclude persistent bounded-term positive
representations on an escaping ray. [Physical-height shadows](global/HEIGHT_SHADOWS.md)
gives simultaneous clean blocks at polynomial target precision within
`O(log(a+1))` steps, including all positive rational anchors of a small
polynomial height. [An all-height date](global/ALL_HEIGHT_TRANSFER.md)
combines PR200's fixed-height clock with an optimized cutoff and a
height-drop restart, obtaining a pointwise square-root-logarithmic bound
in the returned target's own height.

[Ordinary polynomial relations](global/ORDINARY_RELATIONS.md) bounds every
independent integer relation on a consecutive or branching family of actual
states. On an escaping ray its consecutive-state implication holds at a
density-one set of dates simultaneously over all permitted lengths, degrees
and coefficients. Three Lean kernels check the underlying integer-root
argument. The existing inverse laws do not force one of the excluded
independent relations. [The adelic clock test](root/ADELIC_CLOCK.md) also
keeps the real and 2-adic capacity factors in balance: an additional analytic
continuation estimate is needed before the strict algebraicity theorem can
apply.

[Critical conformal atoms](global/CONFORMAL_ATOMS.md) constructs finite
atomic eigenmeasures of the squared inverse operator on ternary irrational
points. The examples have positive real branches, coherent odd binary
branches and ordinary realizations of every finite diagram. They do not
give an infinite orbit of one positive integer. The construction identifies
the arithmetic condition missing from a general operator-uniqueness proof.

[The final synthesis](FINAL_PROPOSAL.md) retains the two open finite-energy
estimates explicitly. [LEAN_FINAL.json](../../reports/astra-six-hour-20261127/LEAN_FINAL.json)
records seventeen fresh module builds and 136 public axiom inventories.
[The final review](../../reports/astra-six-hour-20261127/FINAL_REVIEW.md)
records proof scopes, source attribution and the three new exact replays.

## The cycle and global attacks

| Result | What it controls | Remaining pointwise obligation |
|---|---|---|
| [Complete-divisor tail](arithmetic/COMPLETE_DIVISORS.md) | The entire cancellation `gcd(C,2^h-3^p)` for all fixed-weight near-critical parity words, with no gap cutoff | Rule out an exceptional primitive word with complete ordinary cancellation |
| [Periodic sibling floor](arithmetic/PERIODIC_TRACE.md) | `liminf rho_k(a)/a >= alpha/7` at every phase of every positive cycle, and a reciprocal bound over all periodic phases | Obtain a conflicting upper estimate at those actual phases |
| [Component word complexity](arithmetic/COLOR_WORDS.md) | Uniform catalogue complexity of every finite Collatz-invariant coloring, including rare blocks; the external compression theorem gives exponent strictly below binary entropy `H₂(log₃2)` | Force a matching lower complexity from two distinct positive components |
| [Farey current](global/FAREY_CURRENT.md) | Exact positive lattice counts at all integer scales and a small positive cyclotomic angle on complete ordinary paths | A global restriction incompatible with that current |
| [Primitive modular markers](global/ELLIPTIC_MARKERS.md) | The complete reduced cycle denominator is recovered by two consecutive even-cut marker defects | Exclude the exceptional case in which every primitive marker is integral |

The divisor estimate is a finite-population theorem, not an exclusion of a
single cycle. The modular congruence controls are actual positive one-edge
paths and show why closure modulo a fixed level is insufficient. The coloring
bound is topological and uniform; zero complexity entropy alone does not imply
a constant coloring.

## Lean and reproducible checks

Seventeen new Lean modules check finite arithmetic, exact orbit kernels, and
the explicit conditional topological and full-problem reductions:

* [MinimumCode.lean](arithmetic/MinimumCode.lean): physical minimum, carry cap,
  and full numerator decoding from a bounded binary prefix.
* [PeriodicSiblings.lean](arithmetic/PeriodicSiblings.lean): the genuine odd map,
  distinct transient siblings, disjoint entry branches, and transfer floors.
* [ColorWords.lean](arithmetic/ColorWords.lean): exact affine lifts, labelled
  endpoint partitions, and factoring a shifted color word through its partition.
* [FareyCurrent.lean](global/FareyCurrent.lean): integral cone bijection, first
  occupied level, and angular identities.
* [EllipticMarkers.lean](global/EllipticMarkers.lean): primitive first columns,
  integral marker existence, and complete polynomial divisor obstructions.
* [FormalTransport.lean](root/FormalTransport.lean): legal inverse traces are
  actual odd iterates, exact affine offsets, and signed real-mark transport.
* [TernaryQuotient.lean](arithmetic/TernaryQuotient.lean): exact positive ternary
  quotients and alternating switch defects in the bounded cycle alternative.
* [CanonicalBirths.lean](global/CanonicalBirths.lean): signed shortcut lifts,
  identical high integer quotients, and actual representative-window entry.
* [ClosedSupport.lean](root/ClosedSupport.lean): finite crossing, a gap below each
  regular phase, and countability of the closed range outside the explicitly
  supplied analytic exceptional set.
* [CycleSurgery.lean](arithmetic/CycleSurgery.lean): common-suffix elimination
  and simultaneous divisibility after a word replacement.
* [TiltedGreen.lean](global/TiltedGreen.lean): finite rational growth margins,
  displaced-center identities, and ordinary negative-shadow cost.
* [PotentialAssembly.lean](root/PotentialAssembly.lean): the genuine full map,
  odd normalization, and convergence conditional on a positive bounded potential.
* [RationalGreen.lean](root/RationalGreen.lean): exact finite ordinary sums and
  the implication from the displayed uniform rational bound to convergence.
* [AdaptiveGreen.lean](global/AdaptiveGreen.lean): monotonic prefix boosts,
  exact high-state gain, and comparison with the rational energy multiplier.
* [RationalEnergy.lean](root/RationalEnergy.lean): the finite rational energy,
  its actual-path lower bound, and full convergence conditional on the stated
  uniform bound and target decay.
* [RankDivision.lean](arithmetic/RankDivision.lean): common finite window
  cancellation, integral adjacent coefficients, and the complete denominator.
* [OrdinaryRelations.lean](global/OrdinaryRelations.lean): divisibility and
  coefficient bounds at a nonzero integer root, and the resulting zero
  polynomial criterion.

[check_lean.py](check_lean.py) compiles into fresh project objects, using Lean
4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, and prints and
audits the axioms of every public theorem. One missing cached Mathlib dependency
is rebuilt from its pinned source into a temporary overlay; the existing
dependency cache is left intact. The build does not formalize the infinite
analytic limits or the cited external theorems.

[check_linear_trace.py](escape/check_linear_trace.py) uses integer outward
enclosures of the exact finite law. The retained depth-16 interval for `Z_16`
is `[-0.0672309,-0.0672270]`. Independent wrapped-exponent enumeration checks
every density entry through depth five. These finite values do not settle the
asymptotic sign. The retained table and compilation receipt are in
[reports/astra-six-hour-20261127](../../reports/astra-six-hour-20261127/).

## Frozen repository intake

The full all-state metadata inventory and pass timing are in
[PR_INTAKE.json](../../reports/astra-six-hour-20261127/PR_INTAKE.json). New
mathematics was inspected at these five heads, which had advanced since the
preceding pass:

| PR | Full head | Relevant advance retained |
|---|---|---|
| [201](https://github.com/GettysburgResearch/collatz/pull/201) | `21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a` | Exact escape gates, finite Lean trapping equivalence, actual cofactor bounds |
| [200](https://github.com/GettysburgResearch/collatz/pull/200) | `ad70a3b831867cb8a74d402a2a1abdc419f5a09b` | Exact component pressure, completed reset estimates, squareclass rank criterion |
| [197](https://github.com/GettysburgResearch/collatz/pull/197) | `1f0f496fbea37792439feada6106eaaff596bcd1` | Fixed ordinary-source clock obstructions and sparse modified-carry controls |
| [195](https://github.com/GettysburgResearch/collatz/pull/195) | `51d97cbe17054415acaf95e422801a3532545033` | Full frontier consumer, canonical floor families, fixed-word cover obstruction |
| [192](https://github.com/GettysburgResearch/collatz/pull/192) | `ed7a6fe30b8602407f77855ceb74ce0489ce9c10` | Paid hard-parent repairs, all-clock grammar, corrected two-place regulator |

The prior own published head is `25f5462e2c43feea65760884f7ea8f53576fbc18`.
Each note states its external inputs and the first unsupported inference.
No claim of complete convergence, cycle uniqueness, or absence of escape is
made by this checkpoint.

A second intake during this pass froze PR201 at
`4c36876ebbe8d3cca69b2c4867aeee34f5700470`, PR195 at
`03b26119164664d08eaa04a1ea1d159dd4eccd7a`, PR200 at
`07ae08382588992c1b7f7a60cd331a6647177495`, and PR206 at
`640bf7e511831a0ffc4f00462f12df81f8a8a619`. The guide and relevant new
arguments were read for the active attacks; their bulk computations were not
replayed. [Exact delta inventory](../../reports/astra-six-hour-20261127/SECOND_INTAKE.json).

A third intake froze PR195 at `3fa7ef4a0011b35447a70f587b400878d5ea8ebe`,
PR201 at `807d67ab049f1646398d8ca8c20948cdc1d87742`, PR192 at
`75eac0cbc744469ae2886bc2f140685c484e9fe7`, and PR200 at
`2346db2d49030ef385b73e1ee3e27dcbff86d2d9`. The new Mellin, physical-source,
graded transport, and bridge arguments were read where they bear on these
attacks. [Exact delta inventory](../../reports/astra-six-hour-20261127/THIRD_INTAKE.json).

A fourth intake froze PR200 at `8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec`
and PR201 at `662a3dee736ccbca038377fbb4b2d9439374db16`; a later intake
advanced PR201 to `860a67dedc860adcd82b964958d91b9e21d610f1`. Their relevant
new arguments were read without replaying bulk certificates. PR200's fifth
absolute moment extends the width range beyond this packet's earlier
fourth-energy calculation; that earlier threshold is method-specific.
[Fourth delta inventory](../../reports/astra-six-hour-20261127/FOURTH_INTAKE.json).

The closing intake froze PR200 at `7af83b786636abba2f44fe8c81441153331377fc`,
PR201 at `6795369ac4e604eec342c0b6c08b9a14cd2ca4ec`, and PR192 at
`ae48a04cca29abe5fc8273bcda45e7eee0874896`. Their new guides and the relevant
proofs were read without rerunning archived bulk work. They add the
restricted adjacent-gap period exclusion, critical first-clearance source
laws, canonical source paths, full-mask moment bounds and a fixed-terminal
escape functional. [Final intake](../../reports/astra-six-hour-20261127/FINAL_INTAKE.json).
