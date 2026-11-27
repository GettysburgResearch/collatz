# Final review of the six-hour research pass

## Conclusion and formal boundary

This packet does not prove Collatz. The principal Lean endpoint is
`Collatz.SixHour.RationalEnergy.energy_criterion_implies_collatz`:
`EnergyCriterion -> Universal`. The premise consists of a uniform bound of
8 for the explicitly defined finite rational energies and uniform decay as
the target tends to infinity, with both source and depth cutoffs arbitrary.
No instance of that premise is constructed. The written converse in
`root/RATIONAL_ENERGY.md` uses convergence alone and imposes no logarithmic
stopping-time hypothesis; that converse is not formalized here.

The final build receipt, `LEAN_FINAL.json`, records 17 freshly built project
modules and 136 public declaration inventories. It uses Lean 4.34.1 and
Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`, with
`autoImplicit=false` and warnings treated as errors. Only `propext`,
`Quot.sound` and `Classical.choice` occur in the printed public inventories.
The one missing cached Mathlib dependency is rebuilt from its pinned source
in a temporary overlay. None of the analytic theorems below is imported as
a new axiom. The receipt's successful finite kernels and conditional
conclusions do not constitute an audit of the entire written analysis.

## Original-law and escape analysis

The root read the final statements and proofs of the critical Poisson
profile, critical support neighborhoods, positive trace budget, stationary
selection, marked solenoid, stopped rate and endpoint rate notes.

* `CRITICAL_POISSON_PROFILE.md` retains the actual first-hit pair of clocks
  and the real exit mark. Its local limit uses the specified ordinary joint
  mixing input, followed by the native lattice average. The displayed
  Gaussian width is independent of the smoothing exponent. Its amplitude
  still contains the unknown basin density `d1`.
* `CRITICAL_SUPPORT_NEIGHBORHOODS.md` gives the lower neighborhood-content
  bound from the exact central odd-integer mesh and the marked exit law.
  It does not assert a positive Hausdorff measure at a critical gauge.
* `POSITIVE_TRACE_BUDGET.md` credits **both** the global positive budget and
  the exact finite-depth first difference to Weaver 176, Theorem 2 and
  equation (6). The component formulas, physical tail for nonperiodic
  terms and finite sign controls are the deductions retained here. The
  basin-of-1 sum has not been shown to exhaust the budget.
* `STATIONARY_SELECTION.md` constructs bounded changes to an auxiliary
  ordinary harmonic function preserving finite observations and polynomial
  exit moments while changing a reciprocal moment. It does not change the
  original finite rows, their selected limit, or the basin of 1. It asserts
  ordinary pointwise harmonicity, not pointwise harmonicity on all of Z3.
* `MARKED_SOLENOID.md` extends the retained solenoid theorem to covers
  retaining integer labels. Averaging occurs before the correlated
  translation; the proof does not assume independence of the translation
  and the binomial clock. It has no relative error at the tiny arithmetic
  fibres needed for a specified ordinary integer. A full dyadic-clock
  cover keeps the original singular law, so that range is not claimed.
* `STOPPED_RATE_TEST.md` uses actual positive depth differences at a
  specified escaping ray. Weaver 174's rise-group estimate strengthens
  the lower detector beyond every fixed polynomial times `(2/3)^k`.
  The requisite upper estimate remains open.
* `ENDPOINT_RATE_TEST.md` adds a finite real-prefix mark that detects an
  extra cycle without an assumption that a signed cycle eigenmode survives.
  The exact inverse-lap scaling and the attained finite-prefix minimum
  give a positive consecutive-row difference at every sufficiently large
  depth. Restricting the endpoint band removes the discrete-atom
  obstruction already present at the known transient root 5. The combined
  positive statistic would prove full convergence from one suitably small
  subsequence. The final addendum replaces the unknown packing constant
  by the explicit band `1/(j+1)` and supplies rigorous finite rational
  truncation errors. No upper estimate for that statistic has been obtained.

The retained prerequisites include the original individual-depth law,
ordinary source positivity, the physical reciprocal-packing bound, the
specified joint mixing statements and the placed depth-difference theorem.
The new notes cite their exact sources. These prerequisites are used as
written mathematics and were not rebuilt in Lean during this pass.

## Complete-denominator cycle arithmetic

The root read the rank-division, tagged-division, binary-past cube and local
Hankel-rank proofs, and replayed the two new exact control programs.

`RANK_DIVISION.md` gives a positive small combination of phases at every
rank while retaining the complete reduced denominator. Its coefficients
are common to the candidate and include the boundary doublings. The three
identities in `RankDivision.lean` are included in the fresh kernel audit.
The tagged extension preserves finite dyadic and ternary data using CRT,
but its output obeys signed forcing rather than the ordinary Collatz map.
Its 3-adic logarithm application uses the cited two-logarithm estimate
with a varying algebraic input, rather than an unjustified fixed-input
bound.

`HANKEL_RANK.md` proves full rational column rank on an explicit consecutive
window, for either folded labels or lowbits. For `1 <= m < p`, the weights
`v2(q_j)+j*h/p` have a unique minimum separated by the positive quantity
`delta_m`. Each vanishing row would force a decrease by `delta_m` in a
normalized valuation confined to a half-open interval of width three.
The window length permits enough consecutive moves for a contradiction.
This proof is independent of the real sizes of the coefficients. It gives
no archimedean lower bound for minors. In particular PR200's abstract
subcubic labels already meet these valuation hypotheses; the result alone
does not bypass their obstruction to a cubic size conclusion.

`BINARY_PAST_CUBES.md` realizes the sharp four-sum energy on exact native
binary words. It has two distinct physical realizations: all words occur
on disjoint intervals of one finite ordinary path in a band of ratio below
8/3, and separately an exact integer cube of endpoints can lie in one
specified dyadic residue class. Neither construction is an ordinary cycle
or a single infinite ordinary path. This prevents applying an unjustified
stronger local energy bound to finish the cycle argument.

The earlier Mellin-spacing estimate retains its explicit ordered-band
hypotheses and the external RH/Lindelof input. It is not claimed as the
strongest ordinary size estimate now in the repository. PR200's fifth
absolute moment already extends the width range beyond this packet's
method-specific fourth-energy threshold, and PR201's later full physical
source estimate is stronger in its own stated ordinary setting.

## Global arithmetic and operator routes

The root read the positive S-unit, physical-height, all-height transfer,
ordinary relation and conformal atom proofs. The root wrote the adelic
clock note after checking the cited capacity criterion.

The positive S-unit argument uses finiteness of nondegenerate relations in
a fixed finite-rank multiplicative group. Positivity and persistent large
subsum clusters are essential; no uniform bound for arbitrary signed
degenerate relations is assumed. Physical-height clean blocks use the
fixed-place Subspace input and handle height drops by restarting and
summing a geometric series. The positive rational anchors are controlled
simultaneously at the returned dates. These are exclusions of particular
representations on an escaping ray, not a theorem that the ray has one of
those representations.

`ORDINARY_RELATIONS.md` clears denominators of actual affine words and
applies divisibility at a nonzero integer root. Its three integer-root
kernels are formalized. The simultaneous density-one statement is written
and follows from an elementary upper-density estimate for large total
dyadic clocks. It distinguishes a genuinely independent polynomial
relation from a formal identity of the affine templates.

`ALL_HEIGHT_TRANSFER.md` uses the exact fixed-height date supplied by
PR200, optimizes one height cutoff, and restarts after sufficiently large
height drops. The resulting score is measured at the returned target's
own height. It does not promote a typical census to a statement about one
specified escaping ray.

`CONFORMAL_ATOMS.md` constructs finite atomic eigenmeasures for the entire
critical squared inverse operator. The root checked the fractional-moment
summability, the signed first-visit input, the Haar-preserving continuation
coordinates, closure under inverse children, and the unique successor
selected by a coherent binary unit. Positive real realizations and every
finite ordinary CRT realization are supplied. The infinite ternary,
binary and real seeds are selected separately. These are counterexamples
to a general uniqueness proposal, not counterexamples to Collatz. The
disjoint sets of atoms need not have disjoint topological closures.

`ADELIC_CLOCK.md` computes disk radii whose product is at most one. The
Bost--Chambert-Loir theorem needs strict positive capacity or additional
analytic continuation; it is not invoked at the equality boundary. The
positive first omitted term supplies an explicit obstruction to a claimed
strict interpolation gain from the existing truncations alone.

## Exact new finite controls

These three new controls were executed independently by the root in normal
Python. They use Python assertions; no optimized-mode assertion protection
is claimed for these programs.

1. `check_rank_division.py` checked all 8,190 binary calendars of lengths
   one through twelve and three complete rational cycles, of periods 5,
   8 and 41. The retained output is `arithmetic/RANK_DIVISION.json`.
2. `check_binary_past_cube.py` checked the 64-word construction at native
   length 15 and total clock 24. All three energy counts equal 46,656.
   Its common ordinary path has 3,234 odd steps and 5,126 shortcut steps;
   the smallest state has 5,191 binary digits. It checks the band inequality
   by exact integers. The retained output is `arithmetic/BINARY_PAST_CUBES.json`.
3. `check_first_return.py --depth 13` used integer outward enclosures,
   independent wrapped rows through depth five, and independent forward
   comparisons for 517 of 665 inverse-cell sources. The depth-12 loss lies
   in `[0.152466222,0.152466540]`, above `log(4/3)/2`; the depth-13 loss lies
   in `[0.143172250,0.143172361]`, below it. These certify both signs of
   the finite-part increment. They do not establish its asymptotic sign.

The final source manifest records hashes and checks the Lean receipt
against the final source bytes. Repository integrity validation is a
separate check on a complete clean commit. Its five structural commands
are not a mathematical verification of the analytic deductions.

## Closing repository intake

The final metadata and selected new source paths are recorded in
`FINAL_INTAKE.json`. The closing heads are PR192 `ae48a04c`, PR200 `7af83b78`
and PR201 `6795369a`; earlier head inventories remain available. Each agent
read the new guide and the statements relevant to its attack. The root read
the PR201 final synthesis and the relevant source material identified above.
No inherited bulk finite census was rerun.

The newer period exclusions, source laws and current formulas were
retained at their stated scope. In particular the conditional asymptotic
finiteness estimates have not been shown to overlap effectively with the
finite period exclusion. No universal source merger, uniform finite-energy
decay, stopped-row upper rate, or full cycle exclusion was obtained.
