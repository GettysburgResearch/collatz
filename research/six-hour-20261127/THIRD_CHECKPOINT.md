# Moving rational shadows, signed grades and narrow binary cycles

**Collatz remains open.** This third checkpoint of the six-hour session adds three written proof families and four Lean modules. The strongest cycle conclusion is finiteness at each fixed denominator in a specified narrow binary class, using a named 2026 preprint. It does not identify the finite exceptions or exclude general positive cycles. The strongest escape conclusions constrain one supplied positive orbit but do not yet force descent.

The [root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE3.md) records the reconstructed arguments, exact repairs and evidence boundaries. The build now has **21 local Lean modules and 190 audited declarations**. **27 finite programs** reproduce their complete frozen outputs in both Python modes.

## 1. A moving-shadow complexity bound on an actual positive orbit

Let `x_i` be successive positive odd Collatz states. Split a length-`T` window beginning at `n` into `k` pieces. Each piece is either a single actual edge or an exact rational track

\[
2^{e_i}t_{i+1}=3t_i-1,
\]

with nonzero `x_i+t_i`, rational phase height at most `H`, and denominators prime to three. The phases may change from piece to piece, and their denominators may be even. The [moving-shadow theorem](pointwise/MOVING_RATIONAL_SHADOWS.md) gives an absolute effective constant `C` such that

\[
T+1\le \exp\!\left(C\frac{k+1}{\log(k+2)}\right)\log(n+2H+2).
\]

The proof extends a periodic-dictionary method by retaining moving endpoints, packet-specific denominators, and the ordered binary/ternary positions of every term. It uses Evertse–Ferretti's published quantitative Subspace Theorem. The original singleton placement contained an error; its corrected identity and the rejected original are both preserved. A [separate review](../../reports/six-hour-20261127/MOVING_SHADOW_INDEPENDENT_REVIEW.md) checked the external theorem interface and independently exercised 44,036 actual finite packets.

### A waiting interval independent of the height cutoff

For every `n,H≥1`, some clock

\[
0\le j\le\left\lceil\log_2(3(n+1))\right\rceil
\]

simultaneously satisfies

\[
v_3\bigl(U^j(n)+p/q\bigr)
\le C\log(2H)\log(3+\log(n+1))
\]

for every positive reduced rational of height at most `H`. The chosen clock can depend on `H`. The [proof](pointwise/HEIGHT_FREE_ANCHOR_CLOCK.md) uses the exact bound `2^(k+s)3^r≤H(n+1)`, checked in [TernaryEndpointBudget.lean](pointwise/TernaryEndpointBudget.lean), followed by Yu's logarithmic-form estimate.

### Many shallow dates in every sufficiently long dyadic stack

For shells `[2^iJ,2^(i+1)J]`, permit a different polynomially bounded rational-height cap on every shell. If `S_i` counts its simultaneous shallow dates at the stated local Yu threshold, the [sliding-stack theorem](pointwise/MULTISCALE_SHALLOW_CLOCKS.md) proves

\[
\sum_{i<r}S_i\gg r\log(r+1)
\]

for all sufficiently large `r`, uniformly in `J`. This includes rapidly growing ordinary orbits. On an injective orbit it also forces many distinct ternary cofactors at the same dates for every fixed positive anchor.

The [weighted coupling](pointwise/SHALLOW_TROPICAL_ISOLATION.md) identifies a precise remaining target. These dates have divergent weight

\[
\sum_{t\in\mathcal S}
\frac1{(1+\log t)(1+\log\log t)^2}=\infty.
\]

For a hypothetical fixed escape, pinned PR 201 gives a summable cost for the cheapest larger sibling. A sufficiently cheap ordinary inverse word on a divergent-weight part of these dates would contradict that summability. The required cost upper bound remains open.

The companion [short-lag theorem](pointwise/SHORT_LAG_DEFECTS.md) forces increasing numbers of block-sum defects on every sufficiently short lag. The [stationary decoder control](pointwise/DECODER_AND_ORDINARY_LIFTS.md) shows that exact one-digit prediction and strong rational-height avoidance can coexist, including every finite observation on a terminating positive orbit with a changing source. Such finite realizations do not supply the original-law escape mass.

## 2. Reflected-grade sparsity on one ordinary positive trajectory

The exact overhead criterion from checkpoint two reduces possible cheaper visitors to a finite pool of positive roots and a marked reflected-17 condition. The [new sparsity theorem](pointwise/SIGNED_GRADE_SPARSITY.md) proves, for every interval `I` of `L` ranks,

\[
\#(S_h\cap I)\ll (3/2)^h\frac{L}{\log(2+L)}.
\]

Wu–Wang's published two-logarithm theorem strengthens the factor to `L^(1-1/128)`. For one nonperiodic ordinary source, two marked visits with future positive floor `M` must be separated by `≫log M` odd steps, or `≫M^(1/640)` with the same logarithm input. These are upper restrictions on possible successes. They do not force even one successful future visitor.

The key actual-orbit bridge is simple to state. If `c+m=A2^D`, the positive and reflected paths have matching parities through physical clock `D`. Their states then sum to `A3^q`. A signed count bound therefore forces a small **actual future odd state** on the positive trajectory. [SignedGradeSplit.lean](pointwise/SignedGradeSplit.lean) proves this bridge with arbitrary marked coefficient and lap count.

The [digit families](pointwise/SIGNED_GRADE_DIGITS.md) give opposite answers to the marked predicate:

\[
c_1(k)=\frac{4^k-1}{3}\quad\text{is marked},\qquad
c_5(k)=\frac{10\cdot4^k-1}{3}\quad\text{is unmarked}.
\]

Both reach 1 within two positive odd steps. Each family meets every ternary residue class infinitely often, and the two witnesses can share arbitrarily long low binary prefixes. Fixed finite digit tests therefore cannot decide this particular grade. [SignedGradeDigits.lean](pointwise/SignedGradeDigits.lean) checks the positive family and the complete seven-branch exclusion, retaining the inherited cone inequality as an explicit premise. The ordinary set of marked endpoints nevertheless has count `O(X^(1-1/512))` through height `X` by the written proof.

## 3. Source concentration for narrow binary cycles

For a primitive positive rational cycle let `P` be its least odd period, `d` its full reduced denominator, `X` its largest odd phase, and

\[
W=\operatorname{range}(E_i-i\theta),\qquad \theta=E_P/P.
\]

Assume every accelerated valuation belongs to `{1,2}` and `W≤99/50`. The [four-bridge theorem](cycles/FOUR_BRIDGE_BINARY_CYCLE_BOUND.md) proves

\[
\liminf\frac{\log(dX)}{\log P}\ge\frac{3000}{999}
\]

on any growing sequence with `log d=o(log P)`. It retains the full denominator, actual source interval and same circular carry in both prime-power coordinates.

**Source-qualified consequence.** Chudnovsky's arXiv:2610.28079v1, Theorem 11.1, states `μ(log₂3)≤3`. On that imported theorem, the displayed sequence is impossible. The [independent review](../../reports/six-hour-20261127/INDEPENDENT_BINARY_ENERGY_REVIEW.md) extracts the explicit conclusion `d>P^(1/8000)` beyond an ineffective period threshold. In particular there are only finitely many cycles of each fixed denominator in this narrow binary class. The external preprint's full analytic and Lean developments were not independently rebuilt here.

[BinaryBridgeEnergy.lean](cycles/BinaryBridgeEnergy.lean) kernel-checks the six-state recurrence, all 216 enumerated phase faces, endpoint orders, exact slope bracket, and the three forced-return inequalities. The real interpolation, Subspace-Theorem application and asymptotic counting remain written mathematics. The method uses Weaver's source-separation and four-segment architecture with a new binary-specific energy count.

Two further conclusions clarify its reach:

- An [injective ordinary segment](cycles/FIXED_SOURCE_BINARY_EXCURSION.md) beginning at `A` leaves the same fixed critical corridor within `O_ε((A+1)^(999/3000+ε))` steps. This uses the Subspace Theorem but no irrationality-exponent preprint.
- In the [full unforced two-layer binary language](cycles/UNRESTRICTED_BINARY_FOURTH_MOMENT.md), the same fourth-moment calculation gives height exponent `15000/5031≈2.9815`, below three. Its exact positive-vector lower certificate explains why changing the cuts alone cannot close that gap with this individual-norm bound.

The [elementary denominator census](cycles/BINARY_CORRIDOR_DENOMINATORS.md) also treats arbitrarily many one-direction mechanical switches and sparse additional substitutions. [Positive two-ended controls](cycles/TWO_ENDED_LOCAL_INTEGER_CONTROLS.md) show that ordinary integrality and non-descent at the shorter natural coding horizon still permit more than `X^(1/3)` different finite centers. These controls identify a limitation on local counting, not a counterexample to Collatz.

## Reproduce and continue

The entry points remain [replay_lean.py](replay_lean.py) and [replay_controls.py](replay_controls.py). Exact sources, original corrections, independent reviews and output identities are in the [wave-three manifest](../../reports/six-hour-20261127/WAVE3_SOURCE_MANIFEST.json) and root review. The next work is the same-source cost comparison for escape and the unrestricted ordinary-cycle obstruction. Both remain explicit research obligations.
