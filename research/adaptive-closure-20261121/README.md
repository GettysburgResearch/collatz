# Recurrent five sections, ordinary descent density, and stronger stopping tests

**PROPOSED research. The full Collatz conjecture remains OPEN.** This pass
pursued the universal closing step through three parallel mathematical
routes and a separate synthesis. It incorporates the PR146 update at
`66970775e4bdc945a68308e37a8eb028ebde42d2` and compares with PRs167–169,
which appeared while this pass was running. Overlapping certificate rules
are credited as independent rederivations rather than new discoveries.

The map throughout is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

An odd accelerated edge with exponent `a` represents exactly `a` shortcut
steps. A probabilistic statement about binary Haar input is identified as
such; it is never silently applied to a specified positive integer.

## The strongest new synthesis

Track the two trajectories through their exact affine section

\[
y=5\,3^k x+c,\qquad
k\in\mathbb Z,\quad c\in3^{-\max(0,-k)}\mathbb Z.
\]

The relative odd count `k` is a martingale under fresh fair source parity
bits. A normalized fractional carry moment contracts. Combining the two
gives a proper Foster function with explicit negative three-step drift
outside a finite set. This proves repeated finite-core visits without an
irreducibility assumption. See [the complete recurrence proof](AFFINE_SECTION_RECURRENCE.md).

PR146's new deterministic control word routes every finite section to the
root `(k,c)=(0,0)`. Combining that imported construction with the recurrence
proof gives repeated root returns with probability one. The root is null
recurrent: its mean positive return time is infinite. These facts produce
two contrasting, precisely scoped consequences.

- For every fixed delay and every fixed factor `0<theta<1`, all but a set
  of zero upper Banach density of positive ordinary starts admit an actual
  common-clock return `x,5x -> q,5q` with `q<theta*x`. The interval may be
  arbitrarily far from zero. This is a density conclusion, not coverage
  of each specified integer.
- The specified prefix-free, endpoint-bit-decided, Haar-full odd-endpoint
  dictionaries of nonempty balanced returns have infinite
  uniform positive inverse-fiber pressure at every exponent `0<s<1`.
  The proof combines null recurrence, an exact exponential parity-tail
  bound, and PR167's finite-family averaging identity. Thus completing the
  return dictionary does not complete the existing uniform-column energy
  argument. This concerns arbitrary endpoint charges; a sharper estimate
  for actual invariant labels remains possible.

The [root-return companion proof](AFFINE_SECTION_ROOT_RETURN.md) states the stopping, endpoint-parity and ordinary
realization details. The root recurrence does not establish convergence
of either prescribed endpoint.

## Stronger tests on a fixed ordinary source

[The linear-horizon sieve](LINEAR_HORIZON_SIEVE.md) proves the exact
first-crossing inequality

\[
T^i(n)<2^{-B}n+b_i/3
\]

when `i` is the first clock with `3^(b_i)/2^i<2^(-B)`. It extends the
least-failure test for `n=27k+1` to `floor(k/1024)` actual parity steps,
while keeping all required smaller adjacent antecedents below `5X/8`,
where `X=128k+1`. Counting the longer words on ordinary intervals is
still an open step.

[The simple-prefix product bound](SIMPLE_PREFIX_PRODUCT_SIEVE.md) extends
the existing explicit orbitwise reciprocal budget to every finite simple
prefix. If all preceding states are at least `F`, their multiplicative
correction is at most

\[
\exp\bigl((160/3)F^{-1/40}\bigr).
\]

For `F>=80^40`, this is below two. A sufficiently low coefficient
excursion therefore supplies the same smaller-antecedent reduction
without a prescribed observation horizon, up to the first repetition.
The excursion itself is not proved inevitable, and repeated cycle laps
are not charged as distinct states.

## Certificate cross-check and residual

[The valuation-one note](VALUATION_ONE_TRANSPORT.md) independently
reconstructs the block

\[
5I_1^3I_b(q)=I_1I_2I_5I_{b-5}(5q),\qquad b\ge6,
\]

its ordinary domain `271 mod512`, and a two-case, table-free renewal
proof with coefficient `405749/424576` on its union with the earlier
ladders. PRs167–169 already contain this block and stronger coverage;
the note does not claim an improvement over their larger dictionaries.

Its separate first-valuation-one residual has a source certificate of
rank two but a target prefix of arbitrarily large odd count:

\[
z_k=(2^{6k+5}-5)/9,\qquad
T^{6k+8}(5z_k)=5(3^{4k+2}-1)/8.
\]

The target has already spent `4k+4` odd inputs before that endpoint,
which is at least five. Another calculation excludes the balanced
prefix architecture for a first one followed by a run of threes. Neither
statement is a counterexample to ordinary convergence.

## A sharper arithmetic closing target

[The critical negative-moment interface](CRITICAL_NEGATIVE_MOMENT_INTERFACE.md)
combines PR146's critical orbit sparsity with PR169's exact moment
comparison. For the fully specified congruence-word moments in that note,
put `Q_q=P_q+(1/2)(3/5)^q` and
`rho=H_2(log_3(2))=0.949955527...`. The existence of even one nonperiodic
positive orbit would force

\[
\sum_{q\ge1}Q_q^{-\rho/2}<\infty.
\]

Thus divergence of that actual arithmetic series is a sufficient target
for excluding nonperiodic orbits. The critical logarithmic saving makes
this stronger than the previous supercritical logarithmic partial-sum
criterion. The divergence itself is unproved; nontrivial positive cycles
remain a separate obligation. The fifth-denominator bound in PR169 does
not by itself bound the required second-denominator moment.

## What remains and how to read the evidence

[The completion attempt](FULL_THEOREM_ATTEMPT.md) identifies the exact
unproved implication after combining these results. In particular,
every ordinary source known to converge is an exception to the
infinite-root-return probability-one event. A finite-delay density-one
statement cannot be intersected over all delays to prove pointwise
closure. No GRH premise is used in the new proofs or shown to imply the
missing ordinary arithmetic estimate.

[Frozen sources and comparison scope](SOURCES.md) distinguish the new
proofs from imported source-qualified reductions. The
[execution and review index](../../reports/2026-11-21-adaptive-closure/README.md)
records exact finite replays, scoped internal reconstructions, and actual
clean-checkout validation. Those checks are not external referee
acceptance or proof-assistant formalization of the new mathematics.

No accepted baseline theorem, registry entry, or workflow is modified.
