# Independent agent review of the ordered prime-height packet

**Verdict: VERIFIED at the frozen bytes below for AR-CLOCK-001--006 and
AR-CIRC-001--002, with the stated scopes.** This is an independent agent
reconstruction, not external mathematical acceptance. The estimates are
necessary restrictions and do not establish Collatz or exclude every cycle.

The review was conducted in the complete source checkout based at PR154,
`fe40bb6f88e8094290ef01207d9bf7c4798d35d0`. The reviewed additions were
uncommitted shared-workspace files, so their identities are pinned by
SHA256 rather than an invented commit:

| Path under `research/closure-attacks-20261120/arithmetic/` | SHA256 |
|---|---|
| `CLOCK_HEIGHT.md` | `513e610c2979600d713bf09e417a313e2dee37c6c2fd62df8583c4e3406b3b2e` |
| `PRIME_CIRCULATIONS.md` | `20ea6f9b90fb5b2cd5a01e70e4c1abaea3c302afb949e6bdc8e8060968dc5401` |
| `check_arithmetic_closure.py` | `76b4331a7aa0694ee2c6430f03b72ed1306375258b49992d61a00a225e7c1d7d` |
| `arithmetic-closure-report.json` | `320d3ee9c6a7bea4da7631c8a3ebb03b0eb5a08d445a12b08234f1a568dc14c5` |

## 1. The arithmetic and clock premises

The map is the actual positive odd map
`U(n)=(3n+1)/2^{v_2(3n+1)}`, with `x_i=log_2(n_i)`.
For a segment of `d` odd steps, its numerator is

\[
C=\sum_{t=0}^{d-1}3^{d-1-t}2^{A_t},\qquad A_t\le A-(d-t).
\]

Therefore

\[
0<C\le2^{A-d}(3^d-2^d)<2^A(3/2)^d.
\]

Any common divisor of the two ordinary endpoints divides `C`. Also
`A<=x_i-x_j+2d`, since `log_2(3+1/n)<=2`. This independently recovers the
strict gcd inequality printed in the source, and the ordinary upward
bound is `x_{i+1}-x_i<=1`. Consequently `t_i=3i-x_i` increases by at
least two, and prime heights `z_i` obey
`min(z_i,z_j)<t_j-t_i`. Repeated ordinary values do not invalidate any
of these estimates.

## 2. AR-CLOCK-001: the localized count

The decisive localization is correct. In a noninitial component of
`{i:x_i>=h/2}`, the first height is strictly below `h/2+1`. If a mark
`z_i>=h` occurs, upward increments bounded by one force component length
`ell>h/2`. Its clock span is strictly below `3 ell`, even when the final
height drops sharply just after the component. Marked clock gaps exceed
`h`, so the component pays fewer than `5 ell/h` marks.

The initial component lacks that entrance charge. The retained term
`(1+x_0/h) 1_{h<=2x_0}` is valid for it and necessary in this style of
estimate. A one-state input `x_0=z_0=h=100` already violates the proposed
bound if that term is removed. Single-state components, exact threshold
equalities, and a prefix ending within a high component were all retained.

Thus the result holds under the abstract clock hypotheses exactly as
claimed; it is not using a density assumption about actual prime powers.

## 3. AR-CLOCK-002--004: integration, source term, and quantifiers

The layer-cake integration is valid. Cutting at `h=2` contributes at most
`2N`. Each high-state term integrates to `5 ln^+ x_i`; the initial term
integrates to

\[
E(x_0)=2(x_0-1)_++x_0\ln^+x_0.
\]

Jensen is applied to `ln(1+x)`, not to the nonconcave truncated logarithm:
`ln^+x<=ln(1+x)` first, followed by concavity. Summing over a prime pool
is uniform in the identities of its primes. The pool may be chosen after
observing the prefix, but it must be the same pool throughout that prefix;
the source preserves this restriction.

For a fixed nonperiodic ordinary orbit, no value repeats, so the positive
integer states escape every finite set and their mean logarithmic height
tends to infinity. The specified growing-support condition kills both
terms, including the original-source term. For a periodic orbit, repeated
complete laps remove the source term after normalization. This is legal
because the finite theorem never assumes distinct states. The all-one
cycle is handled separately before division by its zero mean height.

## 4. AR-CLOCK-005: a window at a cyclic maximum

For `L=log_2(max n_i)`, take `N=floor(L)+1` periodic states ending at a
maximum. At distance `d` before it, height is at least `L-d`, so the
window mean is at least `L/2`. This remains true when the window spans
several laps. All its heights are at most `L`, with `L<N`.

The per-prime estimate is then

\[
Y_N(\{p\})/N\le4+6\ln(1+L).
\]

Summing over the actual full prime support, whose total prime height is
exactly the window height, gives
`L<=s(8+12 ln(1+L))`. The explicit inversion with
`L_*=128s ln(4s)` is also correct: `1+L_*<=257s^2`, its comparison
function is positive at `L_*`, and its derivative stays positive
thereafter. Hence `L<L_*` follows. No assumption of a fixed alphabet,
bounded period, or bounded individual division exponent entered.

The parameter is the number of primes in the whole cycle. It is not the
multiplicative rank, and no proof here bounds that support from above.

## 5. AR-CLOCK-006: finite-prefix maximum

Let the maximum occur at index `i`, and set `k=floor(L/2)`.
If `i<k`, the upward bound gives `L<2x_*`. Otherwise the last `k+1`
states before that maximum have heights between `L/2` and `L`, and their
initial height is less than twice their count. Thus the source term costs
at most `4+2 ln(1+L)` per state and the remaining budget costs
`2+5 ln(1+L)`. This yields
`L<=s(12+14 ln(1+L))` and then the stated explicit maximum bound.

This covers a support pool chosen after the finite prefix is known.
Applying it to an infinite orbit with one fixed finite pool proves boundedness
and eventual periodicity, without identifying the eventual cycle as one.

## 6. AR-CIRC-001--002: all-prime balance is insufficient

Both lists were reconstructed by literal integer accelerated steps. Their
weighted input and output products agree, while their vertex sets differ.
For the five-state relation, the prime-19, prime-29, prime-11 and prime-83
coordinates force all five coefficients equal; the remaining prime-5
coordinate then vanishes. This proves its one-dimensional kernel,
positive extreme ray, and inclusion minimality on exactly those edges.

In the seven-source relation, complete additivity sends the product
identity to a positive weighted sum of nonpositive drifts equal to zero.
This implication works in every totally ordered abelian group. The drift
at `5 -> 1` must vanish, so every power of five has potential zero.
Therefore no such globally nonincreasing completely additive potential
has finite sublevel sets. The proof does not cover nonadditive corrections
or ranks that decrease only at selected variable return times.

## 7. Replay actually performed

I ran the source checker with its output redirected to
`merger/arithmetic_source_replay.json`, preserving the arithmetic agent's
files. That report is byte-identical to the pinned source report.

I also wrote and ran a separate integer-only clock-interface checker,
`check_arithmetic_review.py`. It exhausts all lengths 1 through 4 with
integer states `0<=z<=x<=4`, retains only sequences satisfying the clock
premises, and tests the half-integer thresholds from `1/2` through `17/2`.
It checked 19,260 admissible sequences and 327,420 exact localized-tail
inequalities. It separately reconstructs both circulation products and
the source-term omission counterexample. The report is
`arithmetic_review_report.json`.

These finite controls test implementations and boundary cases. The
unbounded results were accepted here on the written reconstructions above.
The source's floating-point trajectory diagnostics remain explicitly
floating-point evidence. The external literature comparison and claims
about priority were not independently adjudicated in this review; those
papers are not needed by the elementary proofs checked here.
