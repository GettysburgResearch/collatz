# Finite merger decisions, complete denominators, and ordinary clocks

**PROPOSED research; Collatz remains open.** This checkpoint joins three
results that retain the ordinary source or the complete reduced denominator.
It gives an executable, kernel-checked decision for a bounded odd-step
merger budget; sharp restrictions on several structured cycle classes;
and a bound on the largest clock fibers summed across all ordinary
components. A fourth result forces a genuine periodic return when an
ordinary itinerary has only a fixed number of sufficiently simple pieces.
The hypotheses on budget, structure, and sampling remain explicit.

## An exact finite decision with no lower-clock cutoff

Fix `K≥1`, a positive ordinary source `n`, and

\[
                         2n\ge K(1+3^K).
\]

For any `j,δ≥0` with `2^j | 2^δ(n+1)`, put
`Y+1=3^j 2^δ(n+1)/2^j`. The new decision procedure determines whether
there exist a positive `m<n` and **any** physical clock taking `m` to `Y`
with at most `j+K` odd departures. It constructs a smaller visitor when
one exists. The optimized registry also returns its minimum odd count
within the specified budget.

The finite data consist of an odd signed origin `−M` that reaches `−1`,
its even count `ℓ`, a binary scale `δ`, and a reverse word at its first
strict coefficient crossing below one. A row has a bounded odd grade
and length, and one congruence for the original `n` modulo a power of
three. Its signed run is finite. No reachability oracle is hidden in
the row predicate.

The height cutoff is proved by retaining the actual positive reverse
path. Before a strict crossing, its normalized affine offset rises by
at most `1/2` per odd inverse. A purported smaller endpoint without
a crossing would force `2n<K(1+3^K)`. At a crossing, divisibility of the
endpoint restores every native intermediate parity. A binary lift of
the signed suffix then supplies the original positive target.

[ScaleSelector.lean](descent/postpeak/ScaleSelector.lean) proves the
equivalence with finite arithmetic rows. The explicit Boolean function
`decideScale` in [DecideSelector.lean](descent/postpeak/DecideSelector.lean)
enumerates a finite reference search and proves that it decides the
ordinary all-clock assertion. The faster
[Python selector](descent/postpeak/scale_selector.py) uses first crossings
and mirrors the written construction. Its independent comparison searches
ordinary integer predecessors directly, without the modular registry.
See [the complete selector statement](descent/postpeak/SELECTOR.md).

For a maximal postpeak word `w`, of odd grade `f` and even count `q`,
the previous cone theorem supplies an exact finite list of relevant
scales: `δ=f−Q(β)`, where `β` has the same length and signed offset as `w`.
Under `H≥21q+9K+3` and the source height cutoff, a smaller visitor with
at most `H+f+K` odds exists exactly when one of those scaled rows accepts.
[PostSelector.lean](descent/postpeak/PostSelector.lean) proves this
ordinary equivalence in both directions.

The scaled list is essential. For `n≡60 mod81`, `n=2^H v−1`, and
`3^H v≡3 mod4`, the postpeak word is `EO`. The source

\[
                         m=\frac{64n-33}{81}<n
\]

reaches its endpoint with `H+5` odds. For `H≥60`, the complete registry
shows that this is optimal, while the pure peak has no smaller visitor
with at most `H+4` odds. The competing tail is `EE`, whose equal signed
offset supplies scale one. This family is a control against using only
the unscaled peak criterion.

## Protected residue classes and the sharp six-even threshold

The written [common-scale density argument](descent/postpeak/SCALED_DENSITY.md)
constructs, for every `K`, a set of at least

\[
                         \frac{259}{960}\,3^K
\]

classes modulo `3^K` protected simultaneously at **every** binary scale
and every eligible pure-ramp length, above the same source cutoff.
Every smaller visitor then costs more than the ramp grade plus `K`.
The maximal-word consumer transfers this protection beyond the peak.
Counting odd sources in a large shell gives a lower bound
`(259/1920−o(1))N` in `[N,2N)` with
`K=log₃N−log₃log₃N−O(1)`.

The signed-origin decomposition and the stopped Kraft mechanism have
an exact antecedent in Weaver 178/v1, §7, which already proves a stronger
pure-ramp density estimate in its own setting. The present density claim
concerns a common finite-precision set across all binary scales and its
postpeak transfer. PR201 also already treats unrestricted visitors at
shifted sites. These are substantive predecessors, not merely related
heuristics. The density estimate is a written proof; the source-specific
selector and its physical consumer are the kernel-checked statements.

The [residual classification](descent/postpeak/POSTPEAK.md) proves that
every word beginning `EO` with at most five even departures is maximal
in its same-length signed-offset fiber. The total length and odd count
are unrestricted. The finite automaton retains a normalized integer
carry and uses terminal bounds; it covers arbitrarily many repeated odd
steps. [ResidualFive.lean](descent/postpeak/ResidualFive.lean) checks its
finite closure and connects it to the actual word relation. Six evens
are sharp: `EOEEEEEO` and `EOEOOOEE` have equal offset and respective
odd grades two and four. The positive eight-step example is credited
to PR192; the universal exclusion below six evens is the new threshold.

A separate [tower result](descent/postpeak/TOWER_PAYOFF.md) applies the
prior quantitative pair-coalescence theorem to arithmetic progressions
of ramp exponents. All but `O(JN/√log N)` of `N` consecutive progression
indices have simultaneous common-clock mergers across `J` adjacent
peaks. The error constant stays uniform when the progression preserves
an arbitrarily prescribed ternary depth. The formal
[finite payoff](descent/postpeak/TowerPayoff.lean) constructs the smaller
ordinary source from those merger data. The quantitative coalescence
input and the density conclusion remain written results. This does not
convert an exceptional exponent into a typical one.

## Whole-denominator restrictions for structured cycles

Let a positive rational shortcut cycle have primitive word length `n`,
weight `u`, affine numerator `C`, determinant `D=2^n−3^u`, cancelled
factor `G=gcd(C,D)`, and complete reduced denominator `d=D/G`.

The [two-swap classification](cycles/phase3/ADJACENT_SWAPS.md) treats
every proper rotation obtainable by at most two cyclic adjacent swaps
of unequal letters. Two disjoint opposite-direction swaps leave an
explicit entire geometric quotient dividing `d`; in particular,

\[
                              d>2^{n/2}.
\]

The exponent is sharp along a primitive family at critical weight.
For two disjoint same-direction swaps, the cancelled factor divides a
joint power gcd of 2 and 3 with exponent `O(n)`, and the cited BCZ theorem
gives `log G=o(n)`. Earlier one-swap and overlapping-swap observations
receive explicit credit. [SwapArithmetic.lean](cycles/phase3/SwapArithmetic.lean)
checks the modular-power gcd, the geometric quotient divisor, and its
strict lower bound. It does not formalize BCZ or the word classification.

For a fixed number `K` of odd runs, the
[bounded-run theorem](cycles/phase3/BOUNDED_RUNS.md) yields

\[
 \frac{\log_2 d}{n}
 \ge \max\left\{\frac1K,\frac1{\gcd(n,u)}\right\}-o_K(1).
\]

The proof uses the published outside-`S` gcd theorem of Levin and Wang,
separates common polynomial factors on a minimal torus translate, and
retains a surviving rational factor in the **full** denominator. A
positive top layer prevents total cancellation. Coprime `n,u` force
full denominator exponent. Rhin's bound controls proximity to the
determinant's positive root. The onset is ineffective.

For each fixed template, [symbol dilations](cycles/phase3/DILATIONS.md)
admit a sharper exact answer. Replace every symbol by `ℓ` copies of
itself and let `g=gcd(n,u)`. Signed run corners form finite arrays on
`Z/g`; if `S` is the union of their Fourier supports, then

\[
                  \lim_{\ell\to\infty}
                  \frac{\log_2 d_\ell}{\ell n}=\frac{|S|}{g}.
\]

Cyclotomic polynomial remainders compute `S` using exact integer
arithmetic. A primitive template forces these characters to generate
the full dual group. In particular prime `g` gives exponent one, and
prime-power `g` gives at least `(1+φ(g))/g`. The primitive template
`10110100` attains `3/4`. This is a fixed-template limit, without a
uniform onset over changing templates.

## Ordinary source height versus simple periodic pieces

Fix a maximum of `K` consecutive pieces and `0<δ<1`. The
[small-anchor theorem](rigidity/phase4/SMALL_ANCHOR_WORDS.md) proves that
there are `ε>0` and `L₀` such that the following holds. If a positive
ordinary source `x≤2^((1−δ)L)` realizes a word of length `L≥L₀`, each
of its at most `K` pieces has a rational affine fixed point of logarithmic
height at most `εL`, then the physical orbit hits one piece's exact
fixed point at the start of that piece. It therefore makes an actual
periodic return. The displayed choice of `ε` is explicit; `L₀` is not.

For words with boundedly many odd runs, the anchors are zero and minus
one. A positive source cannot hit either. Consequently such words need
source height `x≥2^(L−o(L))`, with sharp binary coefficient one.
Powers of a fixed number of templates of length `o(L)` obey the same
alternative. The proof uses the rational three-place Subspace Theorem,
then an exact chronological projection. The finite transport and the
conversion from that projection to a physical return are proved in
[ChronologicalAnchor.lean](rigidity/phase4/ChronologicalAnchor.lean).

The [rational-path extension](cycles/phase3/RATIONAL_PIECES.md) retains
the denominator cost explicitly:

\[
       \log_2\max(1,x)+K\log_2d\ge(1-o(1))L,
\]

unless a piece's actual starting state equals its anchor. Applied at
a suitable boundary of a primitive positive cycle, this gives
`liminf log₂d/n≥1/K` for `K` proper small-anchor pieces. The exponent
is sharp for two pieces. The closest prior effective periodic-dictionary
bound is Weaver 15/v2; the note distinguishes that result from the
sharp coefficient and general rational-anchor formulation here.

No claim supplies such a bounded-piece decomposition for every orbit.
An arbitrary parity sequence can evade the theorem by needing more
pieces or anchors of greater height.

## Clock dispersion across all ordinary components

Cut the outgoing odd edge at the minimum of each periodic component,
and put an integer clock on each resulting ordinary component, increasing
by one along every retained shortcut edge. Its origin may be chosen
independently in each component. Let `N_X(C,k)` count the starts at most
`X` in component `C` and clock `k`. The written
[clock theorem](rigidity/phase3/CLOCK_DISPERSION.md) gives

\[
                      \sum_C\max_k N_X(C,k)
                       =O\!\left(\frac{X}{\sqrt{\log(2X)}}\right).
\]

At most `w` independently selected clock values in every component
therefore capture `O(wX/√log X)` starts in total. The conditional clock
entropy is at least `(1/2)log log X−O(1)`. The proof handles all possible
cycle cuts simultaneously by an elementary finite parity estimate. It
then builds a single positive error measure for balanced dilations by
2 and 3 and telescopes each translated atom until it leaves a common
finite support. Summing the component maxima is done before discarding
that common envelope. [ClockEnvelope.lean](root/phase3/ClockEnvelope.lean)
checks this finite measure consumer abstractly.

[Joint clock phases](rigidity/phase3/CLOCK_PHASES.md) also equidistribute
modulo every fixed modulus, with the total error summed over all
components in ambient-prefix normalization. The note identifies real
frequency resonances and the bounded ordinary Green height they retain.
No component density is assumed in these statements. In particular,
the estimate is not a relative bound for an arbitrary sparse subset.
Arbitrarily long common-clock blocks give a concrete obstruction to
replacing initial-prefix averages by uniform local intervals.

## Verification and the remaining step

The root reconstructed the written arguments, including the first-crossing
cutoff, scale-dependent witness, whole-denominator divisors, torus-factor
argument, both chronological projection proofs, and the common positive
clock envelope. Fresh replay rebuilt all 21 local modules in this
checkpoint's dependency chains, including 14 new modules. Together with
the first two checkpoints, 42 distinct local modules have been rebuilt.
Printed public axiom inventories contain only `propext`, `Classical.choice`,
and `Quot.sound`, or subsets thereof.

Nine finite programs ran in both normal and optimized Python, with
identical outputs. These comprise four finite identity/fixture checkers,
the two scaled decision/count programs, and three exploratory enumeration
programs. The latter are not proofs of universal automaton or density
claims. The universal five-even exclusion has its separate Lean proof.
Detailed executions, source hashes, and repository regression receipts
belong in the separate `reports/` archive.

The finite classifier can answer either way; it does not prove that every
source eventually has a smaller merger. The structural cycle restrictions
leave high-complexity words. Clock dispersion leaves thin selected cohorts.
The small-anchor theorem needs a decomposition that an arbitrary orbit
need not possess. These are the remaining mathematical obligations, not
silent premises in a claim to have resolved Collatz.
