# Full-theorem attempts and exact remaining obligations

This pass targeted universal ordinary convergence. **It did not prove
Collatz.** Its positive Lean results are stated in the package README;
this file records the constructive attempts so that an unfinished step
cannot be mistaken for a completed one.

## 1. Deterministic comparison with a supplied source certificate

For every supplied ordinary witness `T^d(x)=1`, the source's subsequent
odd count at clock `d+2m` is exactly `oddCount(x,d)+m`. The compiled
relative-parity theorem shows that a single sufficiently late crossing of

\[
16\,\operatorname{oddCount}(5x,d+2m)
\le 16\,\operatorname{oddCount}(x,d+2m)+d+2m
\]

proves convergence of `5x`. Arbitrarily late crossings for every such
source are equivalent to forward-five closure. This equivalence does not
assert the crossings.

The attempted completion followed the actual source certificate, including
its deterministic period-two tail. A normalized target quantity of the
form `Y/3^k` has a contracting affine recurrence, but its denominator is
unbounded. That recurrence is not a well-founded rank and gives no upper
return bound on the relative odd level `k`.

Consuming an inverse certificate also creates affine target offsets. An odd
source edge `n=(2m−1)/3` turns the first target step into `5m−2`, so an
invariant restricted to pure multiples of a certified source is not closed.
At the source's terminal value one, the target degree and offset can still
be unbounded. A complete invariant controlling those states was not found.

## 2. Adaptive prescribed endpoints

PR146's whole-interval synchronization constructs a common binary class,
then prescribes its ordinary endpoint through a ternary congruence.
`EndpointSteering.lean` preserves its exact ordinary divisibility and
nonnegative-lift conditions.

The attempt to remove the large steering cost by keeping a fixed parity
cell led instead to `SiblingRigidity.lean`: with positive prefix odd count
`p` and the stated equal-count merger, the extra clock must be a positive
multiple of `2·3^(p−1)`. This proves a structural lower bound for that
specific construction class.

We then tried a nested tree of two legal unit children

\[
x_L=(2^Lq-7)/9,\qquad
L=L_0,L_0+6,L_0+12,\quad 6\le L_0\le11,
\]

discarding the unique child divisible by three. Its sibling map
`x -> 64x+49` runs through every residue modulo every power of three when
unrestricted iterates are allowed. The unproved improvement is a bound
linear in the target precision for the **nested bounded-child tree**.
Each inverse step divides by nine and changes previously steered digits.
No induction preserving all those digits was completed. Details and the
ordinary physical-five interpretation are in `INVERSE_TREE_ATTEMPT.md`.

Even that depth bound alone would not prove the earlier clean-shell test:
the height cost would still need to satisfy the shell's quantitative
inequality. The newer PR173 five-block interface is a separate possible
closing test, not a consequence of the endpoint identity alone.

## 3. Global rank synthesis

The first proposal used fixed-width binary-window histograms. The compiled
`LocalProfileObstruction.lean` rules out **every** strictly decreasing rank
that factors through one such histogram, with no restriction to linear
weights and no finite size cutoff.

We therefore attempted two broader classes, always aiming at a rank valid
on every ordinary input:

- A rank decreasing after an even fixed clock `q`, allowing independent
  terminal-context corrections and periodic position weights. Its exact
  finite transducer accepts arbitrary canonical binary lengths. Concrete
  inputs generate candidates; they do not certify them. The full verifier
  rejected fitted candidates at inputs outside their initial constraint
  sets. `FIXED_CLOCK_SYNTHESIS.md` records the precise class, actual outcomes,
  and the absence of a successful global certificate.
- Polynomial position weights
  `sum w(context,d)*binomial(position,d)`, with polynomial node-potential
  and lower-bound certificates. `search/polynomial_position_search.py`
  generates sufficient edge and terminal inequalities for every scan
  position, translating them to the least reachable position of each
  state. The actual translated searches reported infeasibility through
  width eight at degree one and through width six at degree two; the
  larger attempted instances reached time limits. These outcomes concern
  the chosen sufficient coefficient constraints and are numerical search
  evidence, not proofs that all polynomial-position ranks are impossible.

The polynomial implementation controls compared its exact feature
differences with direct binary-word calculations at 1,029 inputs per
window width, for widths one through nine and degree three, including
inputs with 257 bits. Those controls test implementation identities only.
The recorded search has no successful rank witness to formalize in Lean.

## 4. Late related work considered

The initial exact source pins are in the package README. A focused late
refresh read the following PR descriptions and, for PR180, its current
scientific guide. These were research interfaces, not new kernel premises
or broad independent reviews.

| PR | Frozen head considered | Relevant interface |
|---|---|---|
| 173 | `cccf14d13250d3f98ef9b01ddbd304d11294e603` | Ordinary five-block nonmeeting counts, exact dyadic residue mixing, and the remaining passing-stage bound |
| 174 | `011b89e5362ea89427c2704e5e6c1f434e860da0` | Ordinary `3x−1` closure and the remaining power-of-three family |
| 176 | `d2303ea3144ba652d089c1ec38ad3879c3ea5ef7` | No-loss least odd-child failure and mixed multiset certificate induction; complete rules remain open |
| 177 | `23bbf7383b30bff37434fe823b957759bcdf2c1f` | Exact witness formalization and an unbounded reset whose displayed size can grow arbitrarily relative to its source |
| 179 | `4bf2675bcc78b42a3f17c0dd826e1dfcc4c8f35b` | Coefficient-crossing budget sufficient for full descent; universal budget remains open |
| 180 | `995ae97b10e851e4f91f7c74395a5b28bcacfebc` | Joint comparison rank search; written logarithmic predecessor-density bridge with finite five-energy still open |

PR146 remained at `f431078244e868dc699fad011044f0d5e7f76437` at this
refresh. None of the inspected current descriptions asserted a completed
proof of the universal closing statement. No analytic claim from PR180 is
imported as a Lean axiom here.

### Applying the newer five-block test

A focused follow-up read PR173's new README and criterion interfaces at
`cccf14d13250d3f98ef9b01ddbd304d11294e603`. Its population-strengthened
bound has `p=2^k`, `k=25h+3`, and requires

\[
4((4k+1)M(p,t)+1)<2^{21h}.
\]

That stronger Lean equivalence retains `Population84` as an explicit
hypothesis. This pass does not re-prove its published predecessor-count
input or import it into the present Lean package.

Thus it asks for a relative nonmeeting rate of order
`p^(−0.16)/log p` or smaller on the actual five-block interval. That is a
different and substantially less restrictive numerical target than the
earlier elementary test, but no such estimate was obtained here.

PR146's random whole-interval synchronization at block length comparable
to `p` needs order `(log p)^2` fresh source bits for its median bound. The
five-block sample has only `log2 p+O(1)` input bits of freedom. Its fixed
ordinary high digits cannot be replaced by fresh bits after that horizon.
The exact dyadic square identity uses inputs below `p²`; it supplies label
stability, not additional independent bits for this smaller sample.
Consequently the existing synchronization estimate does not by itself
prove passing stages in the new criterion. The bounded inverse tree also
does not currently provide this ordinary nonmeeting count.

## Outstanding full-theorem target

The exact target retained by the compiled comparison module is
`RelativeBudgetReturns`, on the actual ordinary pair with its supplied
source witness. It remains unproved. A complete alternative rank or a
successful ordinary passing-stage theorem would provide a different route;
neither was obtained in this pass.
