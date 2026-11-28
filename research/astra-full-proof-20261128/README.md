# Three-hour attempt at the missing global steps

**Status: OPEN research, 28 November 2026. No proof of Collatz is claimed.**

**Current focus:** the [finite-date near-critical parity consumer](mass/MODERATE_PARITY_AT_ONE.md)
reduces full convergence to a vanishing upper tail on the original positive
integer interval at `m = floor(kappa*k + k^(3/5))`, where
`kappa = 1/(1-log_2(3)/2)`, with threshold `m/2 + k^(3/5)/16`.
The deduction uses an outside written first-passage theorem and the qualified
positive-predecessor theorem. The required upper-tail estimate is open.

This packet pursues statements that would rule out every positive counterexample,
including both escape and a nonstandard cycle. It deliberately does not target a
larger finite verification range, another bounded-period exclusion, or an improved
constant without a route through the remaining universal quantifier.

The map is the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

## Initial attacks

1. **Canonical ordinary descent.** Given a least counterexample in the
   `17 mod 48` reverse-defect class, use the actual finite certificate that its
   triple reaches one to construct a strictly smaller ordinary witness in the
   same component. The input and output sources must remain fixed while their
   two meeting clocks may differ. PR201 supplies the factor `98304` reduction;
   PR197's all-higher-rank selector remains open.
2. **Long-time parity on the original interval.** For actual starts
   `1 <= n <= 2^k`, seek a vanishing upper-tail proportion
   `Q_(5k)(n) >= 0.501 * 5k`, at least along an unbounded sequence of `k`.
   The elementary bad-orbit lower bound is greater than `0.5024` once the
   finite floor through 64 is checked. The external positive-density theorem
   would then exclude every counterexample. Uniform independent parity words
   and changing congruence representatives are not substitutes for this count.
3. **Extinction of retained ordinary mass.** Under the all-prefix odd-clock
   gate `4 A_j <= 7j`, prove that the reciprocal mass of the positive principal
   representatives tends to zero. Follow each retained integer through its
   future; do not refresh its law at the next depth. The existing exponentially
   small birth bound leaves a genuine old-atom loss problem.
4. **Independent arithmetic search.** Test whether the dyadic companion admits
   a finite triadic reconstruction at every positive ordinary input, or whether
   a stronger outside theorem supplies a missing global regularity statement.

The allocation can change if one route yields a plausible closure. An equivalent
criterion is an interface for an attack, not a resolution of the open step.

## First substantive checkpoint

- [Signed parity analysis](parity/README.md) proves that the reflected negative
  interval saturates the proposed long-clock upper tail at every scale. Its
  Fourier window has exactly the same magnitudes as the positive interval.
  Consequently an absolute-value Fourier estimate cannot establish the desired
  positive result. The surviving target is a specific signed cancellation.
- [Ordinary inverse-tree record flux](mass/RECORD_FLUX.md) identifies all late
  harmonic losses, up to exponentially small error, with first-hit paths into
  the actual integer 1. The remaining global step is the normalization
  `L(1) = 1 + E(1)`, which would force the mass of every permanent bad atom to
  vanish. Neither the normalization nor the equivalent extinction is proved.
- [Canonical-route congestion](descent/ROUTE_CONGESTION.md) bounds how many
  ordinary sources in one octave can use one specified extra arrow. The bound
  exposes why a zero-density set of arrows can still carry positive-density
  traffic into a fixed small defect. [First-grade separation](descent/RESONANCE.md)
  supplies an exact signed carry obstruction to a proposed merger mechanism.
- [ClosureConsumer.lean](ClosureConsumer.lean) checks the complete implication
  from an explicitly assumed positive-density theorem and a vanishing parity
  tail along an unbounded subsequence to universal ordinary reachability of 1.
  The upper-tail premise remains open; the density premise is not silently
  replaced by a project axiom.
- [Outside input provenance](arithmetic/OUTSIDE_INPUTS.md) retains qualified
  density results and rejects two purported full-proof imports on their actual
  statements. The independent checks in
  [ExternalClaimChecks.lean](arithmetic/ExternalClaimChecks.lean) were compiled
  locally; this is not a claim to have rebuilt either outside project.

The newly written mass and congestion estimates are mathematical arguments,
not fully formalized theorems. The local Lean boundaries and printed axiom
lists are recorded with each packet. The next work targets the unresolved
global steps, rather than enlarging the finite checks above.

## Second checkpoint: actual terminal arithmetic

[The finite upper-certificate shadow](descent/UPPER_CERTIFICATE_SHADOW.md)
works at arbitrary odd rank. Every nonnegative signed release excludes the
corresponding sufficiently long terminal tails from being a least reverse
defect. A negative release persists under every added upper cycle; its exact
physical recurrence is the lower integer's own Collatz trajectory. A
hypothetical bad source, including one on a nonstandard cycle, enters this
negative chart after an explicit amount of padding. The remaining step is
therefore an ordinary merger or descent beyond that chart, not an extension
of the same padding argument.

[The positive sampling calculation](parity/POSITIVE_SAMPLING.md) identifies
the exact ordinary inverse graph inside a contracting ternary pole transfer.
Pointwise Green finiteness is proved even under hypothetical escape, so it
cannot serve as the missing extinction estimate. A global tilted bound is a
strictly stronger proposed condition.

The mass lane records [concentration of true first-entry cones](mass/FUNNEL_CONCENTRATION.md),
[uniqueness of a rooted low-mean necklace cut](mass/ROOTED_ROTATION.md), and
[actual positive controls against a paired predecessor floor](mass/PAIR_FLOOR_TEST.md).
These retain original integers and distinguish whole components from
incomparable branches that eventually join the same component.

[The coordinator review](../../reports/astra-full-proof-20261128/CHECKPOINT_02_REVIEW.md)
reconstructs the arguments and records independent checks. The fresh local
rebuild of the three core Lean modules and nine printed roots is recorded in
[CORE_LEAN.json](../../reports/astra-full-proof-20261128/CORE_LEAN.json).

## Evidence policy

The [third coordinator review](../../reports/astra-full-proof-20261128/CHECKPOINT_03_REVIEW.md)
checks this consumer, the [95 positive rational arcs](parity/POSITIVE_RATIONAL_ARCS.md),
the actual [terminal-phase calibration](mass/DYADIC_PHASE_CALIBRATION.md),
and [internal upper prefixes](descent/INTERNAL_PREFIX.md).
[CountedDeadline.lean](CountedDeadline.lean) locally verifies the deadline
under its explicit matching-grade premise. It does not bound arbitrary
stopping times. The full Fourier sum, including the large conductors, remains
the active analytic target.

- **LOCALLY COMPILED:** a named Lean file was actually compiled in this pass,
  with its toolchain and command recorded.
- **OUTSIDER-REPORTED LEAN:** a pinned external author or release reports a
  successful compile or audit; this pass has not independently rebuilt it.
- **WRITTEN:** a mathematical proof is supplied in prose, without a claim that
  Lean checks the full statement.
- **FINITE CHECK:** an exact finite calculation supports precisely its stated
  range and is not an all-depth argument.
- **OPEN / REFUTED:** the missing inference or a counterexample is explicit.

Outside theorems may be used with their exact hypotheses and the appropriate
evidence label. Lack of a local rebuild does not forbid a qualified dependency.

## Source boundary

The baseline is main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The current frontier is mostly in exploratory PRs. Exact starting heads are in
`SOURCE_PINS.json`; later changes do not inherit this pass's inspection.
Process and replay receipts belong under `reports/astra-full-proof-20261128/`.
The packet will end with the strongest proved statement, the first unsupported
step of each serious attempted closure, and precise replay/provenance records.
