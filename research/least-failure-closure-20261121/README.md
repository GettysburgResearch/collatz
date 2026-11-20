# Fixed-defect returns, excursion frequency, and physical five transport

**PROPOSED research; full Collatz convergence remains OPEN.** This packet
follows the latest PR146 least-failure sieve and proportional lifting
results, PR163's complete five-to-tripling energy comparison, and PR166's
unbounded physical ladder. Three parallel authors and the primary author
pursued the arithmetic, certificate, and energy closing steps, then
reconstructed one another's arguments at frozen file hashes.

The strongest new arithmetic statement bounds returns with a fixed number
of defects even when their ordinary duration is unbounded. Combining a
different fixed-length return bound with an exact run clock gives an
iterated-logarithm improvement to the necessary frequency of excursions.
The certificate results recognize the entire homogeneous transport
architecture and add three families beginning with valuation one. The
energy estimates cover a larger domain with smaller coefficients.

None supplies the missing universal upper bound, successful compiler, or
finite all-source defect energy. These are written proof drafts with
scoped independent AI reviews and exact finite checkers. They are not a
formal proof of Collatz or an update to the accepted theorem registry.

## Map and conventions

The shortcut map is `T(n)=n/2` for even `n` and `(3n+1)/2` for odd `n`.
The positive odd map is `U(n)=(3n+1)/2^a`, where `a=v_2(3n+1)`.
An odd edge with `a>=2` is called a **defect**; `a=1` multiplies the
shifted state `n+1` by `3/2`. A shifted core `R_P(n+1)` removes every
prime factor in a fixed finite prime pool `P` containing 2 and 3.
Throughout, a nonperiodic orbit means **not eventually periodic**, or
equivalently an orbit with no repeated state. A finite cycle's repeated
laps cannot be counted as distinct arithmetic solutions.

All logarithms below are natural unless a base is written. Counts of odd
edges and shortcut clocks are kept separate. Every source and path in the
theorems is an actual positive ordinary integer path.

## Arithmetic: return counts and a stronger convergence criterion

### Arbitrarily long fixed-defect returns

For prescribed shifted endpoint cores and exactly `d>=1` defects, a
**canonical** path begins and ends with a defect. If `s=|P|`, then the
number of such paths is at most

\[
F_{s,d}=\bigl(2^{35}(2d+1)^2\bigr)^{(2d+1)^3(s+1)}.
\]

There is no bound on their intervening valuation-one runs or on their odd
length in this statement. The proof compresses the shifted affine
equation to its defect positions. Exact binary valuations force any zero
subsum to include every term. After normalization, the resulting unit
vector recovers every defect position, including the unbounded final
position. Evertse's explicitly cited nondegenerate S-unit theorem then
counts the paths.

Read [FD1–FD3](FIXED_DEFECT_CORE_RETURNS.md). For a finite core set `Q`,
there are at most `|Q|^2 sum_(d<=D) F_(s,d)` distinct completed excursions
with at most `D` defects. Thus defect counts of successive completed
excursions tend to infinity on a nonperiodic orbit. Arbitrary leading and
trailing valuation-one extensions are also finite for a fixed core pair
and defect count, but their multiplicities have no uniform bound here.

The complementary [RU1–RU3](MULTISTEP_CORE_RETURNS.md) bound fixed odd
length `r` by `(2^35(r+2)^2)^((r+2)^3(s+1))`. Its full-path equation is
degenerate exactly for all-ones words. Intermediate cores are unrestricted
in both results. Neither bound is a height estimate or a last-return clock.

### An iterated-logarithm lower bound for outside visits

Fix one ordinary source and a finite core set `Q`. Let `C_N` count the
vertices outside `Q` among odd times `0,...,N`, including both endpoints.
Every nonperiodic orbit satisfies

\[
\liminf_{N\to\infty}
\frac{C_N}{\log(N+1)
 [\log\log(N+1)/\log\log\log(N+1)]^{1/3}}
\ge
\frac{1}{2\log(\log_2 3)\,[104(s+1)]^{1/3}}>0.
\]

In particular, `C_N/log N` tends to infinity. The source and finite core
set affect the onset, but this conservative limiting constant depends
only on `s`. The fixed source, fixed prime pool, and fixed finite core set
may not change with `N`.

[EF1–EF4](EXCURSION_FREQUENCY.md) first prove a finite-prefix inequality.
They split valuation-one blocks even when a defect connects two inside
vertices, count short intervening paths by RU2, and charge every long gap
to its actual outside vertices. An affine clock bound controls the total
length of the inside blocks. Optimizing the explicit unit-solution count
then gives the displayed rate.

For `P={2,3}` and `Q={1}`, PR161's elementary within-class cycle exclusion
also deals with eventual periodicity. Consequently **`C_N=O(log N)` is
sufficient for convergence to 1**. The stronger precise sufficient
condition is a liminf below the displayed constant. What remains missing
is any such upper bound for every actual source.

## Certificates: a complete recognizer and new valuation-one blocks

[HT1–HT5](HOMOGENEOUS_FIVE_TRANSPORT.md) give an exact unique decoder for
every block that transports `x -> q` and `5x -> 5q` with the same odd count
and shortcut clock. It decodes the fivefold affine correction by binary
valuations and proves every inverse division legal. On a supplied complete
first-hit word, this recognizer subsumes every compiler made entirely of
such blocks, including adaptive or infinite block dictionaries.

Among blocks beginning with valuation one, none has at most three odd
inputs. Exactly these three four-input families exist:

| Actual source word | Actual target word from `5x` | Guard |
| --- | --- | --- |
| `(1,1,1,b)` | `(1,2,5,b-5)` | `b>=6` |
| `(1,1,2,b)` | `(1,5,1,b-3)` | `b>=4` |
| `(1,1,4,b)` | `(1,3,5,b-3)` | `b>=4` |

Their source cylinders are `271 mod512`, `135 mod256`, and `87 mod1024`.
They are disjoint from PR166's ladder. Together the domains have relative
natural density `85/1536` among odd ternary units, and every new endpoint
is at most `x/3`. These are whole-cylinder statements, not sampled starts.

The complete recognizer still fails on known convergent inputs, including
7. [Homogeneous localization](HOMOGENEOUS_LOCALIZATION.md) proves that
prepending a paired homogeneous prefix preserves complete admissibility
in both directions. It therefore explains why PR146's sufficient residue
class cannot by itself make this recognizer complete. The note supplies
an infinite explicitly convergent family inside `49 mod64` on which the
recognizer fails. This excludes only the stated architecture; different
clocks, other transports, and separately certified base families remain
available.

## Energy: larger renewal and the exact remaining charge

Let `f` be any metric-valued ordinary invariant and put
`e(x)=d(f(5x),f(x))`. Define `E_s(X)` as the sum of `x^(-s)e(x)` over odd
ternary units up to `X`. Let `R_s(X)` omit the combined transport domain.
[ER1–ER4](EXPANDED_FIVE_RENEWAL.md) prove

\[
E_1(X)\le R_1(X)+\tfrac58 E_1(X/3),\qquad
E_{21/25}(X)\le R_{21/25}(X)+\tfrac{91}{100}E_{21/25}(X/3).
\]

The proof correlates all inverse families at a common endpoint residue
modulo 81 before maximizing. Exact integer comparisons certify all 54
unit residue classes, including the fractional powers. At finite cutoffs
these imply comparison factors `8/3` and `100/9` with the respective
remainders. No initial summability assumption is used.

A further exact decomposition handles **every first valuation at least
three**, giving

\[
E_1(X)\le R_{12}(X)+J(X)+\tfrac78 E_1(X/2).
\]

Here `R_12` is the remaining first-valuation-one/two five energy, and `J`
retains the adjacent charge
`d(f(5*2^(a-2)q-1),f(5*2^(a-2)q))` with its original source weight and
multiplicity. No bound on `R_12+J` is proved.

These elementary inequalities need no external density theorem. Using
finite energy to infer global rigidity is a separate source-qualified
step: PR163 retains its named positive-lower-density input at exponent
one and its predecessor-moment input at exponent `21/25`. Neither is
silently promoted or reproved here.

[Density and congestion](DENSITY_CONGESTION.md) proves that the average
harmonic inverse-fiber kernel of a finite transport family equals its
binary cylinder mass. This limits uniform positive column estimates for
Haar-full covers, but does **not** identify Haar-full coverage with
coverage of every positive ordinary integer.

## Latest closing attempts and the first unsupported steps

The exact source heads and attribution are in [SOURCES.md](SOURCES.md)
and [source-snapshot.json](source-snapshot.json). The pass began at
PR146 `dd2d5dbd...` and incorporated its later `fd991063...` update,
together with PR164 `6fa6b429...`.

- [Latest five-reduction boundary](LATEST_FIVE_REDUCTION_BOUNDARY.md)
  derives the remaining adjacent comparison for the surviving Mersenne
  family and checks the domains of PR164's new rules. Fixed-defect
  finiteness does not create the missing physical return. The proportional
  lifts actually escape every fixed finite shifted-core family.
- [Homogeneous localization](HOMOGENEOUS_LOCALIZATION.md) proves the
  exact cancellation rule for the complete decoder and supplies explicit
  first-hit countercontrols to the proposed universal compiler.
- [Closing energy interfaces](CLOSING_ENERGY_INTERFACES.md) tests the
  new residue localization against renewal. A lift's weight and its
  inverse comparison factor cancel exactly. The large-clock sufficient
  progression lies in the remaining valuation-one/two domain. The note
  also records the mismatch between single-orbit excursion counts and
  all-source weighted energy.

The last note extracts a concrete analytic target from the sparse sieve.
For a normalized ordinary invariant label, every discarded comparison
has an actual positive row bound by its smaller query list, with every
repetition retained. The retained charge is summable even at the sieve's
critical exponent `rho≈0.949955527`, thanks to its `log^(-3/2)` factor.
The missing estimate is a strict weighted **column** bound for all the
incoming query occurrences, followed by the required energy-propagation
or rigidity theorem. The decreasing height and logarithmic length of
individual query lists do not supply that column bound.

No failed strengthening is a counterexample to Collatz. No density-one,
sparse-survivor, or fixed-core statement is substituted for a universal
ordinary assertion.

## Reviews and reproducibility

The [arithmetic review](CORE_RETURNS_INDEPENDENT_REVIEW.md),
[excursion review](EXCURSION_FREQUENCY_REVIEW.md),
[transport review](REVIEW_HOMOGENEOUS_FIVE_TRANSPORT.md),
[localization review](HOMOGENEOUS_LOCALIZATION_REVIEW.md), and
[renewal review](RENEWAL_REVIEW.md), together with the
[closing-interface review](CLOSING_INTERFACES_REVIEW.md), identify their exact target hashes
and what was independently reconstructed. Shared coordination on the
three transport blocks is disclosed. These are AI-agent reviews, not
external peer acceptance or formal verification.

From the repository root, replay the frozen exact reports with:

```bash
python -X utf8 -B research/least-failure-closure-20261121/replay.py --receipt ../least-failure-replay.json
```

The [execution record](../../reports/2026-11-21-least-failure-closure/README.md)
keeps actual command results, artifact identities and clean-checkout
validation separate from the mathematical claims. The written proofs,
not a finite Collatz census, carry the universal statements.
