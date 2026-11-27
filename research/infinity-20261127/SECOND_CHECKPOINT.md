# Second checkpoint: denominators, physical clocks, and paired sources

**Collatz remains open.** This checkpoint sharpens three actual-trajectory
constructions and records a conditional energy route. It does not prove
the finite-mass hypothesis of the universal Lean consumer. The preceding
checkpoint is [here](FIRST_CHECKPOINT.md).

## Denominators cannot be suppressed in arithmetic packing

For a primitive positive rational odd cycle, write each state as `n_i/d`,
where `gcd(d,6)=1`, and retain every actual edge
`2^a n_next=3n+d`. The Pell equation is now

\[
 X^2-DV^2=d^2,\qquad X=6n+d,\qquad D=\operatorname{sf}(3n(3n+d)).
\]

Keeping only `D` loses an essential congruence. Keep also
`R=X/V mod d^2`, a square root of `D`. In one joint `(D,R)` class, the
quotient of two Pell points is integral, has norm one, and has trace
congruent to 1 modulo 12. This gives a height ratio greater than 25.
An actual return to the same joint class after `h` shortcut ticks satisfies
the normalized height bound `x<3*12^h`. There are at most `2^omega(d)`
roots to keep, so the denominator appears explicitly in the population
bound.

The control `5/7 <-> 11/7` has a repeated discriminant but different roots
modulo 49. A separate actual 200-phase cycle with denominator 1661 gives a
joint-class return of quotient trace 13, showing why the ordinary
trace-97 bound cannot simply be transferred. The complete control checks
284 primitive words, 1,298 edges, and that 200-phase cycle.
[Full Pell argument](arithmetic/FULL_DENOMINATOR_PELL.md).

The cubic counterpart gives a stronger denominator-sensitive statement.
Let `r` be the affine rank of the complete edge-product cubeclasses and
let `omega_1(d)` count denominator primes congruent to 1 modulo 3. Then
the written bound is

\[
 P\le40\,5^r3^{\omega_1(d)},
\]

with 20 in place of 40 when the odd period `P` is odd. For ordinary
cycles (`d=1`) the sharper bound is `P<=4*5^r`, or `2*5^r` for odd `P`.
Together with the separately named published period floor, a nontrivial
ordinary cycle must have this cubic affine rank at least 16.

The argument tracks adjacent numerator classes and uses their coprimality:
each pivot coordinate has five permissible ordered choices, rather than
nine. After fixing a cubic root modulo `d`, an integral binary cubic
equation has right-hand side 1. The named external inputs are Bennett's
2001 bounds for those equations; the root checked the exact statements
in both primary papers. The full Diophantine result is written mathematics,
not a new formalization of Bennett's theorems.
[Cubeclass argument and sources](arithmetic/FULL_DENOMINATOR_CUBES.md) ·
[Seven checked algebraic/counting interfaces](arithmetic/FullDenominatorPacking.lean).

These results obstruct low-rank rational cycles with small denominators.
They give no upper rank bound for arbitrary ordinary cycles.

## A shorter upper certificate requires a long physical comparison

For `H=18+162t` let the canonical lower state `z` satisfy
`81z+271=2^H`. Its upper companion `3z` reaches 1 for the first time at
shortcut clock `H`. The lower arm reaches the large Mersenne peak
`3^(H-7)-1` at that same clock.

Suppose another canonical pair `(y,3y)` has a shorter upper certificate
`h<H`. Then `2y+31<=z`. More strongly, if four physical clocks, all at
most `B`, witness a lower meeting and an upper meeting between the pairs,
then

\[
                         H<5(B+9)+4.
\]

Even replacing the upper meeting by an independently certified upper
power-of-two tail still forces `H<6(B+7)+4` under the stated tail-clock
hypotheses. Thus this hard family cannot acquire the proposed shorter
certificate through a uniformly bounded comparison of its ordinary arms.

The proof compares the exact integer slopes and intercepts, uses the
initial forced parity pattern, and separates leading powers of two from
their remainders. An explicit upper-only family attains asymptotic lower
height ratio `1/2`; it does not supply the missing lower meeting.
[Written barrier](coupling/UPPER_CLOCK_BARRIER.md) ·
[Actual upper trajectory](coupling/UpperClock.lean) ·
[Clock inequalities](coupling/ClockBarrier.lean).

## One exact translation pairs positive portions of the critical census

At depth `n=floor((K-1)log_2(3))+1`, use the actual gated population of
reduced rational sources with denominator `3^K`, as in the prior
[critical sector](../six-hour-20261127/escape/CRITICAL_SOURCE_SECTOR.md).
Fix an ordinary canonical `q=17 mod48` and a dyadic precision `r`.

The construction selects two finite physical heads of equal grade and
length. Between each head and its terminal bits it inserts the same
freely varying, bounded-carry critical bridge. The two actual sources
differ by one numerator translation `d_K` independent of that bridge.
At the common final clock they reach `q` and `3q`, respectively. The
first clears its denominator one tick earlier, at `2q`.

For any prescribed real center in `[1,3/2]` and small tolerance `epsilon`,
both starts can be placed within that tolerance while `2^r` divides
`d_K`. The paired portion of the real conditioned census has lower
fraction `exp(-C*(3/2)^r*q)*epsilon^C`. A fixed-head subsequence makes
the real normalized translation tend to zero while retaining a positive
fraction for each fixed `q,r`.

This is a physical population statement, not a substituted terminal
distribution. The proof includes the head coverage, common bridge count,
actual parity, reduced denominator, and first-clearance clock. Four exact
arithmetic/physical interfaces are formalized. The all-size selections
and ballot count remain written proofs.
[Complete construction](mass/CRITICAL_PAIRED_TRANSLATION.md) ·
[Lean interfaces](mass/CriticalPairTransport.lean).

For an invariant ordinary label, a disagreement between `q` and `3q`
therefore produces positive translation variation on this conditioned
census. **An upper bound on that same variation remains missing.** Fixed
dyadic precision and a vanishing real translation alone do not identify
the labels. The actual visit-five control with targets 113 and 509 shows
why generic real continuity would be false without additional structure.

## Two additional written deductions

The [ordinary period-spectrum note](arithmetic/ORDINARY_PERIOD_SPECTRUM.md)
uses the pinned uniform ordinary occupation bound to show that the total
logarithmic defect over all positive cycles is summable. Along continued
fraction denominator scales, the number of distinct actual odd periods
up to `Q` is `O(Q^(19/39))`. Its all-scale exponent `38/77+o(1)` retains
the explicitly quoted irrationality-exponent input. A sparse admissible
period spectrum is not an exclusion of every nontrivial cycle.

The root's [support-energy criterion](DYADIC_SUPPORT_ENERGY.md) uses a
feature absent from generic positive-voltage controls: an actual component
coefficient is zero off its component and bounded away from zero on it.
Consequently summability of its dyadic square energy itself, without a
square root, would make the Boolean support converge. Exact doubling,
ordinary affine coalescence, and the named predecessor-density theorem
then exclude a nontrivial support. The required summable estimate is
open; current `k^(-1/2)` coalescence errors do not supply it.

## Verification and scope

This checkpoint freshly compiles **four new Lean modules with 21 distinct
printed declaration audits**, along with five previously audited local
dependencies. Cumulatively this pass has 13 new modules with 57 audits,
plus nine distinct prior/dependency modules with 76 audits: 22 unique
modules and 133 declaration audits. Only `propext`, `Classical.choice`,
and `Quot.sound` occur in the audited declarations.

Three new control programs reproduce their complete archived JSON in
ordinary and optimized Python, bringing this pass to seven such controls.
The builds reuse the pinned compiled Mathlib dependencies. No cold build
of all Mathlib or independent LeanChecker run is claimed. Infinite
analytic and Diophantine arguments retain their written/external status.

[Root reconstruction](../../reports/infinity-20261127/ROOT_SECOND_REVIEW.md) ·
[Replay record](../../reports/infinity-20261127/SECOND_REPLAY.json) ·
[Concurrent-branch intake](../../reports/infinity-20261127/PR193_SECOND_INTAKE.md).
