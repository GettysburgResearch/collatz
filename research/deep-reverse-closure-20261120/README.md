# Deep reverse closure: exact reductions, complete subclasses, and the remaining step

**Collatz remains OPEN.** This packet attacks the latest reverse criterion
in PR146 and the analytic and arithmetic obligations in PR160--162. Its
new mathematical claims are **PROPOSED**, with independent internal
reconstructions and the explicit external qualifications below. The
finite replay is evidence for exact identities and complete finite covers;
it is not a replacement for the written proofs or a proof of Collatz.

## The strongest positive results

### 1. A least failure has finitely many possible fourth valuations

PR146's exact deep reverse criterion says that Collatz is equivalent to

\[
128k+1\in C\ \Longrightarrow\ 64k+1\in C,
\qquad k>0,\quad4\nmid k,
\]

where `C` is the actual basin of 1 for the positive shortcut map. Suppose
this implication fails, and choose its **globally least upper antecedent**
`X_*`. The [height theorem](LEAST_FAILURE_HEIGHT.md) proves

\[
176106n<X_*\quad\Longrightarrow\quad n\in C.
\]

This is a genuine strong-induction argument using smaller eligible
implications. It does not assume every smaller integer converges. The
constant comes from a complete replay of the source's 71 directed affine
paths: the exact maximum conditional antecedent/source ratio is
`2025217/23<88053`.

For `c=v_2(162k+4)`, every least failure must then satisfy

\[
\boxed{c\in\{1\}\cup\{3,5,\ldots,77\}
                  \cup\{6,8,\ldots,70\}.}
\]

Its upper first-hit certificate must have at least five odd inputs.
At rank five, the complete `c=1` and `c=3` families are also excluded;
`c=4` is always directly solvable. These are exclusions for the same
global minimum, not unconditional convergence assertions for every
source in the excluded families.

The [all-rank kernel](REVERSE_CERTIFICATE_KERNEL.md) supplies exact
ordinary residuals, a complete rank-five congruence parameterization,
and the precise pure-power/Mersenne targets. Its remaining parameter
`z in C` and the supplied stopping certificate are unbounded.

There is also a positive [adaptive exclusion at arbitrary rank](C3_SINGLE_RUN_CERTIFICATES.md):
every `c=3` upper whose known tail has one initial run of valuation-one
steps followed by its terminal step is excluded from being the least
failure. The proof constructs an unbounded ordinary merger with a
pure power of three below `X_*/176106`, apart from one explicitly
certified exception. It covers the explicit certified witnesses of the
bounded-clock obstruction below. Thus that method barrier is compatible
with a successful source-dependent argument on the same infinite family.

An explicit remaining `c=3` case already has upper odd rank six: its
lower companion reaches `2^(341+486j)-1`, for every `j>=0`. At the
known upper stopping clock the lower has grown above the upper.
C3S3 proves these identities; it does not assert that those Mersennes
fail to converge. This family differs from the rank-five Mersenne
progression in the separate witness-depth theorem.

### 2. The single legal five slice controls the whole tripling energy

For any ordinary-invariant metric label `f`, put

\[
E_5(s)=\sum_{\substack{x>0\ \mathrm{odd}\\3\nmid x}}
x^{-s}d(f(5x),f(x)),\qquad
D_3(s)=\sum_{n>0}n^{-s}d(f(3n),f(n)).
\]

The [complete comparison theorem](FIVE_SLICE_ENERGY.md) proves, for
every `s>0`, as an inequality of nonnegative extended quantities,

\[
\boxed{D_3(s)\le
\frac{248(7153/21)^s}{(1-2^{-s})^2}\,E_5(s),}
\qquad
\boxed{D_3(1)\le10000E_5(1).}
\]

Its certificate has 67 word pairs and 109 affine cells covering every
odd residue modulo 2,073,600. Every multiplication or division by five
retains its full defect cost and its unit-domain guard. The proof checks
injectivity before summing all sources, including their even fibers.
This closes the specific energy-propagation question SE-002 in PR160.

The prior subcritical coercivity theorem and the separately qualified
endpoint density input give the stated rigidity consequences **if the
five energy is finite**. No such upper bound for a hypothetical
separating component is proved. Neither signed Hardy eigenvectors nor
saturated first-hit capacity in PR162 supplies that missing bound.

Its physical paired block does give a [positive partial renewal](CLOSING_ATTEMPTS.md):
at `s=1`, the energy on the class `x=49 mod64` is charged to smaller
sources with total coefficient `64/441<1`. Thus finite energy on the
uncovered complement would suffice, with an explicit bound. The
complement is still infinite and has no established finite moment.

### 3. Complete dynamics inside the shifted two-prime class

Let `S={2^s3^t-1:s>=1,t>=0}` and `N_k=2*3^(k-1)-1`. The
[complete classification](SHIFTED_SMOOTH_COMPLETE.md) proves

\[
\boxed{U(N_k)\in S\quad\Longleftrightarrow\quad k\in\{1,2,4\}.}
\]

It uses the explicitly stated two-logarithm estimate in Lagarias,
*Ternary Expansions of Powers of 2*, Lemma 2.2(1), and an exact
127-index finite complement. For every other `n=2^s3^t-1`, its first
exit from `S` is exactly at odd time `s`. The seven sources that remain
in the class, already identified in PR161, reach 1. The new complete
transition list removes the possible increasing boundary-index path
without invoking Evertse's much larger bound.

Every hypothetical nonconvergent orbit must make the effective number
of outside visits given in CS3. No contrary upper bound on those
visits or on newly created cofactors is available. The
[pure-power core calculation](PURE_POWER_CORE.md) makes this limitation
explicit on infinite certified local families; it does not confuse
varying sources with the future of one fixed integer.

## Why the most direct finite completion does not work

The [guarded clock theorem](GUARDED_CLOCK_OBSTRUCTION.md) proves that,
even with fourth valuation fixed at three and an actually convergent
upper antecedent, a smaller-antecedent path can require arbitrarily
many ordinary edges before its first conditional arrow. Its witnesses
are ordinary certified sources, using the elementary
[basin residue construction](BASIN_CRT_DENSITY.md). Thus the finite
valuation list above does not imply a finite atlas of bounded words.

The [Mersenne witness theorem](MERSENNE_WITNESS_DEPTH.md) gives a
separate accelerated-depth obstruction in the rank-five `c=5` family.
For every prescribed bound there are actual exponents `e=119 (mod162)`
for which no eligible cheaper odd predecessor of `2^e-1` has that few
odd steps. It controls affine intercepts as well as slopes and does
not treat its rational congruence center as an ordinary source. This
does not exclude unbounded searches or paths with forward excursions.

The remaining route can still be adaptive: it may use the actual
unbounded certificate for `z`. An ordinary path from every residual
to that certified `z`, or to the proven initial interval, with all
conditional upper antecedents below the same `X_*`, would contradict
minimality and finish Collatz. That all-source construction is not
established here.

The analytic route has a different exact missing step: prove sufficient
finite five energy for an actual separating invariant label. The
[closing-attempts note](CLOSING_ATTEMPTS.md) records why the current
local-density and harmonic-renewal estimates do not do so, and keeps
the positive original-source occupation problem separate.

## Sources, review, and replay

[LATEST_SOURCES.md](LATEST_SOURCES.md) records the exact current heads,
including older PR146's newer commits and the concurrently opened
PR162. [The audit inventory](../../reports/2026-11-20-deep-reverse-closure/source-audit.json)
enumerates all 98 open PRs at the inspection point and the newest
20 closed PRs. Enumeration is not blanket mathematical verification.

The [review and validation guide](../../reports/2026-11-20-deep-reverse-closure/README.md)
identifies the independently reconstructed claims, finite checkers,
source hashes, and actual complete-checkout receipts. Internal agent
review is not human referee acceptance or formal verification. No Lean
build is claimed for PR146's existing formal files in this packet.
