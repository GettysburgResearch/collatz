# Exact-clock amplification and directed single-residue closure

**Collatz remains OPEN.** This continuation of PR 201 gives two global
reductions and checks the finite arithmetic connecting them to ordinary
integer trajectories. The new exact-clock dichotomy does not assume the
external inverse-counting floor used in the earlier continuation.

## 1. A finite row test for the whole conjecture

Use the shortcut map T and its odd acceleration U. A unit here is a
positive odd integer not divisible by three. A word with b odd steps,
total shortcut clock s, source x and endpoint q satisfies

    q = (3^b/2^s)x + beta.

Fix a rational `0 < epsilon < 1`. On the exact row `s=2b`, retain unit
sources and endpoints q>1 for which `beta >= epsilon*q`. Also require
either `q>b/64` or a repeated shortcut state within this recorded path.
Let `R_b(epsilon)` be the maximum retained source count at any one
endpoint q. The count is over actual integer paths with a fixed clock
and odd depth, not a stationary measure or average over endpoints.

The [complete proof](escape-analysis/README.md) establishes the dichotomy:

* If every positive integer reaches one, then for each fixed epsilon,
  `R_b(epsilon)=0` for every sufficiently large b.
* If any positive integer fails to reach one, some fixed rational epsilon
  has `R_b(epsilon) >= 2^ceil(b/32)` at **every** sufficiently large b.
  This includes both escape and nontrivial positive cycles. The lower
  bound can be retained separately in each unit source residue modulo
  `3^K` for `2*3^(K+1)+1 <= b/40`.

Thus a cofinal upper estimate below this exponential threshold for each
fixed epsilon would settle the whole conjecture. **That upper estimate
is not proved.** The argument showing eventual zero assumes convergence;
it must not be reused as an independent upper estimate.

### Why the lower alternative no longer needs an analytic floor

At every odd unit there are two legal unit inverse gaps among 1,...,6.
An m-level inverse tree therefore supplies `2^m` distinct sources at a
total clock cost at most 6m. On a hypothetical nonconverging ray, all
odd states are at least five. Its literal suffix consumes strictly less
than two clocks per odd step on average, apart from a fixed initial
cost. That saved clock pays for the inverse tree and two final gaps
which solve one exact power-of-two congruence. The construction preserves
the supplied terminal, total clock, odd count, source residue, and
positive relative carry simultaneously.

The convergence alternative uses an elementary finite simple-path bound:
the reciprocal sum of odd inputs above m is at most `200*m^(-1/40)`.
High relative carry therefore forces a visit below a fixed threshold.
If all those finitely many states converge, their complete forward
images form a finite set. This proof has been reconstructed independently
and is included with the new theorem.

### An explicit source bound for computing the test

This is genuinely a finite test. The universal carry bound is
`beta <= (3/2)^b-1`. Combining it with the displayed affine identity
and `beta >= epsilon*q` gives

    x <= ((1-epsilon)/epsilon) * (2^b-(4/3)^b)
      < ((1-epsilon)/epsilon) * 2^b.

Indeed `epsilon*(3/4)^b*x <= (1-epsilon)*beta`; substitute the carry
bound and divide by the positive coefficient. Consequently the entire
row test may instead scan this finite interval of ordinary unit sources,
iterate each exactly 2b shortcut steps, retain exactly b odd inputs and
an odd unit terminal, and inspect the recorded path and carry. No oracle
for eventual convergence is required to evaluate a row. The large search
size is not an efficient algorithm or evidence for the required upper
bound.

Two refinements have separate quantifiers. A finite forward test of h(b)
odd steps at q, with h(b) tending to infinity, permits the larger
exponential lower bound `2^floor(b/16)`. At a fixed ordinary unit q>1,
a row with relative carry at least `1-2^(-100)` exists
exactly when q is periodic; if so, every sufficiently large exact row
at that same q has exponentially many such sources. None of these
statements supplies a counterexample or excludes all nontrivial cycles.

## 2. Either direction on either odd unit residue suffices

Let C be the basin of one. Choose one residue `r in {1,5}` modulo six,
and choose one of the following directions:

    u in C implies 3u in C,
    3u in C implies u in C.

The [directed-cover packet](global-bridge/README.md) shows that proving
that one implication for all positive `u=r mod 6` would prove Collatz.
The global consumer is PR195's pinned directed descent theorem; the
new construction confines every query to the selected residue and
preserves its direction.

For every positive odd n, the new certificates route n to 3n using
ordinary Collatz edges in either direction and forward triplings in
the selected residue. The residue-one table covers 948 disjoint infinite
progressions; the residue-five table covers 1,263. Every leaf specifies
an affine path valid for its entire nonnegative integer parameter.
Together they contain 84,642 letters. Both universal statements have
passed the Lean kernel, using a proved semantic checker and separately
proved finite decisions.

For any binary Collatz-invariant label, a directed difference across
the full path forces a query with the same ordered labels. Query maps
are injective on each progression and have uniformly bounded height
ratios. This yields quantitative transfer without a logarithmic loss.
Combining the transfer with the separately pinned PR146 cut estimates
and the classical Krasikov-Lagarias predecessor theorem forces the
`0.84` count exponent in each selected residue and direction if Collatz
fails. The stronger head-series and moving-window corollaries retain
their additional density and pair inputs. No opposing upper bound is
proved in any of these interfaces.

The path can cross intermediate components at its extra tripling moves.
It is not a merger certificate for n and 3n until the required directed
law has been established. This is the first unsupported step.

## 3. What Lean now checks

The [verified sources](verified/) and
[execution record](../../reports/astra-continuation-audit-20261124/lean/README.md)
contain three kinds of formal evidence:

1. Portable copies of the four earlier finite proof candidates, with
   their actual source and import changes recorded. The originals are
   preserved as their historical bytes.
2. A general finite gap-word theorem: full extra-depth divisibility at
   a supplied positive odd endpoint gives a unique ordinary positive
   odd source in the specified residue, and the literal shortcut
   iterate at the exact summed clock. Equal-depth gap words are
   recovered uniquely from their source. Carry cutoffs and the
   two-gap router are attached to that same path definition.
3. A semantic affine-cover checker and both concrete directed routing
   theorems. The finite decision proofs use no axioms; the universal
   semantic statements use only standard Lean axioms listed in the
   replay receipt.

The infinite simple-path estimate, exact-row dichotomy, asymptotic
transfers and imported analytic inputs remain written mathematics.
The missing universal upper bound and the directed convergence law
are mathematical gaps, not unfinished formalization of a full proof.

## Review, replay and sources

* [Coordinator reconstruction](../../reports/astra-continuation-audit-20261124/ROOT_REVIEW.md).
* [Independent finite-row review](../../reports/astra-continuation-audit-20261124/ESCAPE_CROSS_REVIEW.md).
* [Independent directed-cover review](../../reports/astra-continuation-audit-20261124/GLOBAL_CROSS_REVIEW.md).
* [Frozen source intake](../../reports/astra-continuation-audit-20261124/SOURCE_INTAKE.json).
* [Fresh new finite controls](../../reports/astra-continuation-audit-20261124/NEW_CONTROLS_REPLAY.json).
* [Replay of the four earlier BigInt programs](../../reports/astra-continuation-audit-20261124/PRIOR_CONTROLS_REPLAY.json).

The classical inverse-tree idea is credited to the literature; the
specific contribution is the exact-clock construction, its changed
quantifiers, the whole-conjecture finite-row dichotomy, and the directed
single-residue covers. All older source qualifications remain in force.
