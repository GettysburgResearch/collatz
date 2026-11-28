# Checkpoint 06: fourfold cycles and sharp terminal mass scales

**The nine-hour pass continues; Collatz remains unresolved.** This snapshot
contains a source-qualified asymptotic cycle exclusion, quantitative Fourier
decay for actual terminal correction laws, their sharp fixed-mass covering
scale, and new supplied-root real constructions. The coordinator reconstructed
the written arguments separately from the finite and Lean checks. Phase seven
and all draft files are excluded.

## Physical cycle width reaches four

[FOURFOLD_ODD_SPREAD.md](../../research/astra-nine-hour-20261128/cycles/phase6/FOURFOLD_ODD_SPREAD.md)
proves the following using Chudnovsky's October 2026 Theorem 11.1:
for every fixed R<4, only finitely many primitive positive integer Collatz
cycles have largest odd state X and smallest odd state m satisfying X/m≤R.
Thus every sequence of distinct cycles has lower limiting odd width at least
four. The corresponding shortcut and ordinary widths have lower limits at
least six and twelve. This is a finiteness theorem at each fixed strict
margin. It supplies neither an effective period cutoff nor an exclusion of
an isolated additional cycle.

The actual cycle folds into two dyadic grades. Its increasing register map
advances the sorted rank by the total halving count A. The angular empirical
measure tends to Haar measure for the irrational rotation log₂3. Strict
width margins let every small fixed fraction of consecutive ranks use only
the tags one and two, including a wrap through the sorted seam. PR214's
rank comparison then makes the initial pair sums unique. A chronological
tag code of length N=log₃m+O(1) is consequently an additive Sidon code of
size comparable to the odd period p. The coordinator checked the lifted
seam, the sign propagation, the Eisenstein nonvanishing step, and the exact
divisibility that transfers register pair uniqueness to the code.

The new improvement retains a physical restriction between adjacent dates.
At a register date with only one division, the binary tag cannot fall from
one to zero: the true odd exponent would be zero. Such dates are disjoint
as adjacent pairs, because A/p>3/2. The code therefore lies in a mixed
product alphabet with proportions 2−γ of three-letter pairs and 2γ−3 of
binary singletons, where γ=log₂3. Their ordered difference alphabets have
sizes seven and three. If P is the number of selected prefix patterns and
D the number of suffix differences, ordered-difference uniqueness and
Cauchy's inequality give the finite bound M²≤P(M+D).

Optimizing how many blocks of each type enter the prefix gives

\[
 U=(2-\gamma)\gamma+2\gamma-3,\qquad
 V=(2-\gamma)\log_2 7+(2\gamma-3)\gamma,\qquad
 d=UV/(U+V).
\]

The exact rational certificate proves 0.5248<d<0.5249 and
3.0196<γ/d<3.0198. An infinite bounded-width family would therefore give
rational approximants A/p to γ with exponent above 3.0196. The recent
upper bound μ(γ)≤3 contradicts that family. The coordinator independently
recomputed the numerical values to high precision and checked the rational
certificate; no floating comparison is used for the strict inequality.

The two-grade rank and Sidon arguments are explicitly credited to
[PR214 at f769b0c](https://github.com/GettysburgResearch/collatz/blob/f769b0c79059cc18b0be89e880ed6ea6a279e1c0/research/astra-critical-rigidity-20261128/cycles/TWO_GRADE_SIDON.md).
Earlier canonical-width coprimality results in Weaver 114 and 145 are also
credited. The new conclusion depends on the mixed chronological alphabet;
canonical defect width and the ratio X/m are not identified.

### The recent logarithm input has a separate audit boundary

[RECENT_LOGARITHM_INPUT.md](../../research/astra-nine-hour-20261128/phase6/RECENT_LOGARITHM_INPUT.md)
records the exact October theorem and the November extension. The coordinator
read Theorem 11.1, its parameter balance, the supplement's actual public Lean
types, and the author's axiom audit. The rational logarithm-ratio endpoint
does not take the desired interpolation conclusion as a theorem parameter.
The November paper develops the October argument and is not counted as an
independent replication.

An independent replay of the unchanged external source was attempted in
fresh storage. Its local closure contains 1,002 modules. Three modules
compiled; the fourth stopped because the available pinned Mathlib cache
lacks `Mathlib.Analysis.MeanInequalities.olean`. Neither requested endpoint
nor its recursive axiom audit was reached. The failed receipt is retained
as [EXTERNAL_LOG_RATIO_REPLAY_ATTEMPT.json](EXTERNAL_LOG_RATIO_REPLAY_ATTEMPT.json).
It is not part of this packet's successful Lean count. The author's audit
and this pass's incomplete replay are distinguished throughout. The cycle
theorem is a written application of the named external theorem.

## Quantitative Fourier decay of genuine correction laws

[LOCAL_TRIT_AND_RAJCHMAN.md](../../research/astra-nine-hour-20261128/escape/phase6/LOCAL_TRIT_AND_RAJCHMAN.md)
proves that the ordinary mean c(f) of n^(−iτ)f(n), for every bounded exact
Collatz branch eigenfunction with the real-size phases, satisfies

\[
 \sup_f|c(f)|\ll_\epsilon
 (1+\log(2+|\tau|))^{-1/2+\epsilon}.
\]

It also allows a single defective edge at any target height, uniformly in
that height. Hence every fixed-target first-hit law, every fixed positive
minimum-cell law, and a complete escaping-component correction law have
Fourier transforms tending to zero. The minimum-one law is included.
Weaver 175's earlier singularity, continuity and full dimension are credited.
This is decay at increasing frequencies; the surviving fixed resonant
escape amplitude is not set to zero.

The coordinator reconstructed the translated-interval extension of the
signed starting-trit estimate from the pinned physical-source proof. Its
binary period error depends on interval length, while its reciprocal
normalization retains the actual source height. Partial summation is
performed with uniform bounds for every prefix of the same interval.
This yields a residual that is rapidly small once log source size exceeds
log frequency. Stopping the negative-drift size walk brings an arbitrary
large source down to log frequency plus a small power of log frequency.

At that physical size, Weaver 124's growing-block theorem makes all branch
values identical on most sliding blocks. On each good block the remaining
logarithmic phase has an elementary first-derivative cancellation bound.
The failure probability costs (log block length)^4 divided by the square
root of log source size. Optimizing the block length proves the displayed
rate. A defective target can affect fewer than 2^t original integers before
date t, regardless of target height. This gives the uniform version without
assuming the target is below the source scale. The primary W124 theorem
and its all-lifts cylinder interpretation were read directly.

## Sharp fixed-mass covering and trimmed collision energy

[CRITICAL_QUANTILE_COVER.md](../../research/astra-nine-hour-20261128/escape/phase6/CRITICAL_QUANTILE_COVER.md)
determines a scale that previous support or Hausdorff statements alone do
not determine. For a fixed minimum-cell terminal log law, the least number
of mesh-1/T cells carrying any fixed mass strictly between zero and the
total is comparable to

\[
                         T/\sqrt{\log T}.
\]

For the canonical real correction law at successive roots y of an actual
escaping ray, the corresponding number of physical unit bins is comparable
to y/√log y. As a consequence, after discarding any fixed mass δ in (0,1),
the least possible normalized quadratic collision energy is comparable to
√log y. The lower and upper estimates hold at every sufficiently late root,
with constants depending on the component and the retained mass.

The lower estimate requires sampling the limiting law at moving resolution.
The note proves a uniform ordinary-source comparison for bounded tests
with Lipschitz constant T whenever X/T tends to infinity, including an
arbitrary moving target. The exact source recursion has rapidly decaying
forcing above log T. Equicontinuity and the bounded two-shift harmonic
equation make every translated limiting profile constant. A stopped-walk
comparison then identifies that constant with its own ordinary mean,
uniformly in the parameters. The coordinator checked this compactness and
stopping argument, including the single-target defect count. A second
route, using actual first landing below a polynomially larger height,
supplies the weaker sampling strength sufficient for the covering theorem.

Now take X=T². In a fixed Gaussian-sized first-arrival clock window there
are O(√log X) possible physical times and only O(1) odd counts for each
time. At a specified clock pair, one mark cell selects at most
O(X/T+1) original integers. Thus any o(T/√log T) cells carry vanishing
limiting mass. On an escaping component the same count uses signed clocks
to a fixed reference, whose Gaussian tightness follows by fixed-waypoint
exhaustion. Restricting to a moving target cannot enlarge the exceptional
population. PR213's exact weighted ordinary trace transfers this lower
bound to the canonical real law at that target.

For the upper bound, the explicit finite covers in Weaver 175 are exhausted
to carry any chosen fixed quantile. Along an escaping ray, the bilateral
law is a countable mixture of fixed-root laws; a finite submixture and total
variation convergence transfer those covers at resolution 1/y. This uses
the actual finite covers, not merely a claim of Hausdorff nullity. The
coordinator checked the physical/log coordinate changes and the bounded
weights in PR213's formula.

For trimmed energy, a cover of mass greater than δ gives the lower bound
by Cauchy–Schwarz. Bins heavier than K√log y/y occupy too few cells to carry
δ mass when K is sufficiently large; discarding them gives the matching
upper bound. The normalized cell information is consequently
log T−(1/2)log log T+O in probability. A further Gaussian bound controls the
heavy-bin tail after the fine-scale limit is taken first. None of these
statements bounds moments of arbitrarily large spikes at a moving scale.

The note explicitly compares
[PR212's logarithmic gauge result](https://github.com/GettysburgResearch/collatz/blob/0e4b428211b0bce432efc7d9d19ff4ea552248ec/research/astra-global-20261128/escape/REAL_FIBRE_LOG_GAUGE.md):
whole-support neighborhoods, Frostman exhaustion above exponent one half,
and an almost-everywhere limsup exponent were earlier results. The new
claim is every fixed-mass quantile at every fine scale, plus the physical
moving-root energy after fixed mass removal. Positive finite Hausdorff
measure at the critical gauge remains a different question.

### Why the current decay and energy results do not exclude escape

[ENERGY_CROSSOVER.md](../../research/astra-nine-hour-20261128/escape/phase6/ENERGY_CROSSOVER.md)
constructs a measure-level model from one genuine minimum-one correction
law. A fixed affine change followed by an exact moving-root rescaling
preserves the Fourier decay and makes the relative interior law stabilize
exactly. Its normalized unit-bin energy still grows at least as √log y.
The model has no asserted integer inverse genealogy. It shows that these
analytic conclusions are compatible; an exclusion argument needs more of
the actual genealogy or stronger integrated information. Smooth compact
weights preserve the logarithmic Fourier bound by Schwartz convolution,
so the two weighting conventions do not evade the example.

## Complete signed-clock rows and real support constructions

[SIGNED_RECIPROCAL_HEAT.md](../../research/astra-nine-hour-20261128/escape/phase6/SIGNED_RECIPROCAL_HEAT.md)
gives an exact binomial Green expansion for reciprocal mass on every full
signed physical/odd-clock level of every escaping component. The boundary
source is absolutely summable after grouping by the complete clock fibre.
Each such fibre is finite by its corrected-height bound. Integrating the
exact native population recursion yields the boundary formula, and the
distinct residual time levels justify Tonelli without an uncontrolled
infinite multiplicity. The resulting joint row law is κd_C times the fair
binomial row in sum norm. Retaining the real cross section gives an L¹ heat
limit with a positive aggregate measure after distributional differentiation.
It permits arbitrary nonzero escape mass; differentiated atomic rows are
not claimed to converge in total variation.

[MIDPOINT_VARIATION.md](../../research/astra-nine-hour-20261128/escape/phase6/MIDPOINT_VARIATION.md)
quantifies how a nontrivial invariant binary coloring accumulates sibling
variation in each sufficiently long dyadic range. Weaver's Paper 212
already proves divergence by the same strong/weak limit principle and is
credited. The new block estimate follows from a uniform prefix rate and
the exact midpoint identity. Its very long ranges do not contradict the
existing counted-fusion upper bound.

[POSITIVE_CORRECTION_SUMS.md](../../research/astra-nine-hour-20261128/machinery/phase6/POSITIVE_CORRECTION_SUMS.md)
proves an elementary supplied-root statement: the sum of the closed
first-hit correction sets at any 33 positive odd ternary-unit roots contains
[0,33/64]. Keeping unit inverse gaps at least three gives strictly growing
positive paths. The first such gap is at most six; later available gaps
differ by two or four. A commit/skip refinement has two separated child
hulls with relative lengths at least 15/512 and 20/512. Splitting the
largest of 33 hulls leaves enough total width in the other coordinates to
cover the gap. Nested refinement proves the interval inclusion. The
coordinator checked the numerical fractions and shrinking argument.
The statement concerns support and does not supply convolution density or
probability lower bounds.

[PRESCRIBED_SPEED_MARKS.md](../../research/astra-nine-hour-20261128/machinery/phase6/PRESCRIBED_SPEED_MARKS.md)
constructs genuine infinite first-hit inverse rays at every supplied unit
root with every speed in the earlier certified tilted interval. Balanced
block totals keep the entire limiting speed exact. The worst-root fixed-total
count supplies exponentially many children; distinct ordinary endpoints
space their real mark centers. The resulting mass-distribution estimate
gives the displayed entropy/real-contraction dimension lower bound. At
mean gap two, full dimension was already known and is credited. Retaining
the extreme children also gives finite interval sums using only infinite
rays of each prescribed speed. Neither construction resolves the critical
ternary reverse-entropy problem.

## Finite and formal verification

The fresh replay passes 23 local Lean modules and audits 471 declarations,
including 50 private declarations. `MixedAlphabet.lean` proves
ordered-difference uniqueness, the complete finite shortening inequality,
and the physical one-division exclusion. `DyadicMidpoint.lean` proves the
exact mismatch identity and triangle inequality. These kernels do not
formalize the external irrationality theorem, renewal arguments, or the
infinite covering conclusions. The aggregate receipt audits every local
declaration, including private declarations, with only the standard three
logical axioms allowed.

Both new Python controls pass normally and under optimization with identical
output. They cover 31,444 finite Sidon codes and 251,552 prefix projections,
21,634 register windows, 12,264 lifted counted-fusion cylinders, 2,679 actual
first-hit marks, 7,544 literal early hits, and 3,770 midpoint identities.
The clock-rate brackets use rational logarithm bounds. These are bounded
controls, not substitutes for the reviewed asymptotic arguments.

The exact frozen sources, strict Lean replay, and paired controls are retained
in the checkpoint-six receipts. The fifth publication's commit, matching
tree and clean-checkout validation are preserved with this checkpoint.
Publication uses the same reviewed tree and a full repository validation
on the exact published commit.
