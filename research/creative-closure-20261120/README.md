# Physical five blocks, signed Hardy flows, and carry/capacity closure

**PROPOSED research. Collatz remains OPEN.** Four parallel attacks sought
an unconditional closing argument, followed by separate mathematical and
implementation reconstructions. This packet contains exact positive
constructions, explicit failures of several proposed closing estimates,
and the first unsupported inference in each route. It contains no accepted
Collatz proof, divergent positive orbit, or nontrivial positive cycle.

## The strongest positive results

### A physical multiplication-by-five block

For odd `q` prime to three, `ell>=6`, and `2^ell q=7 mod9`, put

\[
R_\ell(q)=\frac{2^\ell q-7}{9}.
\]

The ordinary shortcut paths satisfy

\[
T^\ell(R_\ell(q))=q,\qquad
T^\ell(5R_\ell(q))=5q,
\]

with exactly two odd inputs on each arm. Every odd ternary unit `q` has
a unit predecessor of this form with `6<=ell<=17`. The block transfers
both physical arms and provides descent on its covered source class.
It does not establish coverage of every convergent antecedent.

In particular, the infinite family already used in PR158,

\[
x_r=(2^{6r+4}-7)/9\qquad(r\ge1),
\]

has the complete first-hit odd-valuation certificates

\[
x_r:\ (2,6r+2),\qquad 5x_r:\ (5,6r-1,4).
\]

Thus `5x_r` reaches 1 in **exactly three odd steps for every parameter**.
PR158 studied the different companion `2x_r-1`; this is a positive
all-parameter result for the multiplied companion. See
[C5-001--002](five_closure.md).

### Infinite exact Hardy eigenspaces inside the known basin of one

On the unweighted positive Hardy space, let `Q e_n=e_(T(n))` and `P=Q*`.
A binary tree of actual inverse paths, each of shortcut length at most
seven, supports signed square-summable flows. They give

\[
\dim\ker(I-Q)=\infty,
\qquad
\dim\ker(Q-\lambda I)=\infty
\quad\text{for }|\lambda|<2^{1/14}.
\]

Every integer in every constructed support has an explicit finite path
to 1. These exact fixed points therefore do not encode exceptional
ordinary components. The construction also gives complete truncation
residuals and geometric tail bounds. The displayed disk is a sufficient
inclusion, not a sharp spectral-radius claim or a claim of priority over
the entire literature. Signed two-ray constructions, the classical
functional equation, and prior natural-boundary results are credited at
their original function-space normalizations.

The same note proves that nonnegative stationary vectors in finite
`ell^p` spaces are supported on cycles; this positive cone cannot detect
escape. A degree-dependent coercivity bound is optimal in logarithmic
order, and both relevant `I-P`/`I-Q` ranges are nonclosed. Consequently a
finite Fredholm-index interpretation cannot close the problem at this
normalization. See [CAF-001--006](analytic_flow.md).

### Finite information and saturated first-hit capacity

For the actual quarter-safe return `B` and the one fixed original input
`f0(u)=1/(u(u+1))`, coalescence has an unconditional finite information
budget. Each atom is retained along its actual path; absorption is kept
at a cemetery point. No endpoint-renormalized or changing input is used.

The saturated first-hit capacity

\[
C(y)=\sum_u f_0(u)\,1\{\text{the actual }B\text{-orbit of }u
\text{ ever reaches }y\}
\]

counts each original atom once per endpoint. Off periodic points it
satisfies the exact inverse identity
`C(y)=f0(y)+sum_(Bx=y) C(x)`. The pinned PR153 simple-path interval
theorem gives

\[
\sum_y C(y)y^{-s}<\infty
\quad\text{for every }s>H_2(\log_3 2)\approx0.949956,
\]

**including periodic states**. This is a spatial first-hit budget; the
open closing quantity charges every surviving return. See
[OCC-001--003](occupation.md).

## What the attempts also rule out

| Attempt | Exact outcome | Remaining scope |
| --- | --- | --- |
| Pair the five law using one universal two-odd block | The unique pattern has second odd inputs at clocks 2 and 5; its class admits real smaller paired returns. | No complete factorization of all supplied convergence certificates is proved. |
| Repair with a scalar ternary carry controller | Every branch has an ordinary realization. Explicit known-convergent families recharge the proposed valuation resources and increase both first-hit clocks. Unit exits can have arbitrarily large output/input ratio. | Termination, unit exits, quotient membership, and output size are separate obligations. |
| Supply one exceptional-rule allowance in the mixed-base system | `26^r P(word)+r` strictly decreases on every admitted rule, using the credited AYH ten-rule matrix order. Exact administrative work is independent of scheduling. | Exhausting the original allowance returns **UNRESOLVED**. No sufficient total source-dependent allowance is supplied. |
| Use polynomial or triangular orders | All-degree scalar natural polynomial interpretations collapse; all-dimensional positive-diagonal upper-triangular affine interpretations collapse. | General matrices, position-sensitive orders and other architectures remain outside these exclusions. |
| Repair linear ranks with polynomial run-length energies | Every bounded-below weakly monotone additive polynomial run energy has zero coefficients in degree at least two, even with signed real coefficients. | This does not exclude nonadditive or history-dependent energies. |
| Pay each reciprocal-psi occupation charge from that return's coalescence information | The unit-price inequality fails at return 8 for the **entire fixed input**, with a certified positive gap exceeding `0.000265165623`. | A different fixed-input amortized estimate is unproved. |
| Compactify capacity into a summable inverse supersolution | Both `C(y)y^(-s)` for every `s>=1/2` and `C(y)^(c bitlength(y))` for every `c>1` fail on the actual known-convergent edge `31 -> 121`. All omitted originals are included in the bounds. | A positive finite Poisson patch repairs this defect, but no finite all-defect repair budget is established. |

The proofs and boundaries are in [the physical five note](five_closure.md),
[the symbolic-order note](symbolic_order.md), and
[the occupation note](occupation.md). These are exclusions of specified
methods or estimates, not counterexamples to Collatz.

## The final latest-source bridge

PR146 advanced and PR158--161 appeared during this pass. Their new results
were inspected at exact heads before publication. We credit overlapping
source families, physical-return obstructions, prime-support estimates and
spatial analytic constructions; we do not relabel them as new discoveries.

One further attempt asked whether PR146's fixed-rank supplied antecedent
could bound the exceptional carry allowance. The marked first ternary
token in a canonical mixed-base word gives a schedule-independent lower
bound: the rank-two family above forces arbitrarily many exceptional
crossings. The resulting source-rank analysis also addresses the new
pure-power subproblem directly. See [the source-rank note](source_rank.md)
and [the exact latest-source comparison](LATEST_SOURCES.md).

## The missing global inference

The inherited PR157 forward-five criterion would settle Collatz if
`x in C => 5x in C` held for every odd ternary unit. The new block proves
this on a genuine infinite class, but no mechanism reduces every failed
antecedent into that class with a well-founded physical rank.

The occupation criterion would settle Collatz if, for the same fixed
full-support input, the total reciprocal-psi occupation were `o(log N)`.
Finite coalescence information and finite saturated spatial mass do not
establish that temporal bound. The exact failures above show where the
most immediate proposed deductions break.

The symbolic controller would settle the relevant termination problem if
one proved a sufficient finite allowance for every original source.
Bounded odd rank alone cannot supply a uniform allowance. An arbitrary
height-dependent or history-dependent allowance remains unconstructed.

None of these gaps is filled by counting finite samples, changing the
source after a return, using a signed Hardy norm as positive mass, or
assuming that an exit quotient converges.

## Review and replay

Scientific manuscripts are **PROPOSED with scoped internal reconstructions**.
The separate reviews reconstruct the named arguments and distinguish
universal written proofs from exact local certificates and bounded replay.
They are not external referee acceptance or formal proof-assistant builds.

See [reports and exact execution evidence](../../reports/2026-11-20-creative-closure/README.md).
From a clean complete checkout:

```sh
python -X utf8 -B reports/2026-11-20-creative-closure/run_bundle.py --receipt /tmp/creative-science.json
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/creative-checkout.json
```

Choose unused receipt paths outside the checkout. The scientific bundle
checks the frozen content manifest and runs the declared programs normally
and with optimized Python. The repository gate checks integrity and its
retained regressions. Neither execution is substituted for a mathematical
proof of the open conclusions.
