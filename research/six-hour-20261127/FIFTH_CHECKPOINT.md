# Fifth checkpoint: a finite rational-sum proposal with its full Lean consumer

**Collatz remains open.** The new all-input Lean theorem proves the conclusion from an explicit family of finite rational inequalities. Those inequalities are the remaining research target; they have not been established.

For the shortcut map `T`, write `q_j(x)` for its actual number of odd inputs before time `j`. For every positive depth `N`, define

\[
S_N=\{1\le r<2^N:5j\le8q_j(r)\text{ for every }0\le j\le N\},
\qquad J_N=\sum_{r\in S_N}\frac1r.
\]

The checked implication is

\[
(\forall B\ge1\;\exists N\ge1:\;J_N<1/B)
\quad\Longrightarrow\quad
\forall x>0\;\exists h:\;T^h(x)=1.
\]

It proceeds through the global least bad ordinary input, a fifth-power step inequality above 32, exact preservation of every prefix by its positive binary residue, and the reciprocal contribution of that single source. The finite-cutoff version proves convergence through any supplied bound `B` from one such rational inequality. The written converse identifies the limiting sum with ordinary permanent survivors. The birth reserve controls new sources and does not supply the missing vanishing estimate.

[Definition, full proof and open target](BINARY_PREFIX_CRITERION.md) · [Lean](BinaryPrefixCriterion.lean) · [Finite controls](BINARY_PREFIX_CONTROLS.json)

## Additional results

| Packet | Result | Scope |
|---|---|---|
| [Delayed batch](coupling/DELAYED_BATCH.md) | Actual same-clock mergers at all 512 consecutive delayed parameters, with full affine carries and both odd grades | Finite computed rows consumed by a general Lean lifting theorem |
| [Ternary pump](coupling/TERNARY_PUMP.md) | Smaller canonical predecessors on exact valuation classes, plus all sufficiently deep shifted ternary balls | Four Lean declarations; constructive density `1/54 + 17/(18*3^68)` in the delayed parameter |
| [Anchor overhead](coupling/ANCHOR_OVERHEAD.md) | Matching extra-rank bounds in terms of the minimum ordinary division sum to 589 | Eight Lean route lemmas; written LTE class construction and asymptotic cost theorem |
| [Four-copy tails](arithmetic/FOUR_COPY_TAILS.md) | Wide binary-cycle source exponent below `3/8`; positive density of high or high-valuation odd sites at ratio `3.959` | Four Lean carry lemmas and exact finite certificates; written ineffective analytic deductions with specified external inputs |

The previous effective exclusion of bounded binary cycles through odd period `10^1000` is preserved. The new exponent and density statements do not close that branch or exclude divergent trajectories.

## Review and validation

The root independently reconstructed the physical-source formulas, reverse carry and phase-frequency recursions, and the positive-anchor cost argument. A separate agent rebuilt and reviewed the ordinary-integer connection of the new all-input Lean criterion. The root review records the exact formal, computational and written boundaries.

The fifth replay covers twelve Lean modules with **59 printed declaration audits**, including **25 new audits** and 34 dependency audits, plus **five full deterministic controls** in normal and optimized Python. The final receipt and manifest record the actual replay result and exact source hashes.

[Root review](../../reports/six-hour-20261127/ROOT_FIFTH_REVIEW.md) · [Replay driver](../../reports/six-hour-20261127/replay_fifth.py) · [Replay receipt](../../reports/six-hour-20261127/FIFTH_REPLAY.json) · [Manifest](../../reports/six-hour-20261127/FIFTH_CHECKPOINT_MANIFEST.json)
