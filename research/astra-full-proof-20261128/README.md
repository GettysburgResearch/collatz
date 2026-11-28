# Three-hour attempt at the missing global steps

**Status: OPEN research, 28 November 2026. No proof of Collatz is claimed.**

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

## Evidence policy

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
