# `61xx` — ordinary extraction in the six-branch rational-base chart

```text
Agent:      claude-opus5-61
Issue:      #58  (independent attempt; see "independence" below)
Namespace:  61xx   (chosen because 74xx/75xx-99xx are in use by open PRs)
Branch:     claude/collatz-counterexample-inference-y0hgc8
Status:     no counterexample found; the architecture is quantified, not defeated
```

## What this namespace does

It takes the "smallest honest target" of the global-blocker audit — the six-branch chart

```text
P = 3^12 = 531441,  Q = 2^19 = 524288,
A = {229376, 258048, 290304, 326592, 367416, 413343},
x_{n+1} = ceil(P x_n / Q),   d_n = Q x_{n+1} - P x_n  in  A
```

— verifies from scratch that it really is a Collatz subsystem, proves what can be proved
about it unconditionally, and then *measures* the object that decides it: the least-root
sequence `m_N`.

## Claims

| ID | status | content |
|---|---|---|
| [T-6101](T-6101-macro-block-crosswalk.md) | PROVED | The chart is exactly a shortcut-Collatz macro-block system: digit `a_i` ⟺ 19 steps with parity word `(110)^(5-i) 1010 (110)^i` (12 odd steps), under `n = 6x-5`. All-time legality ⟹ divergent Collatz orbit. |
| [T-6102](T-6102-branch-valuation-rigidity.md) | PROVED | The branch is not a choice: `v_2(x) = 15-3i`. Legal valuations are `{0,3,6,9,12,15}`; the `1010` defect sits after `v_2(x)/3` blocks. All 36 branch transitions occur, so no finite-state obstruction exists. |
| [T-6103](T-6103-ghost-window-and-no-integer-cycle.md) | PROVED | Native ghost window: every periodic itinerary is realised by a rational in `[-57.786, -32.067]`. **No integer, positive or negative, has an eventually periodic legal itinerary**; the chart has no integer cycle. |
| [L-6105](L-6105-survivor-class-structure.md) | PROVED | `S_N` is exactly `6^N` classes mod `2^19N`; the lift tree is 6-ary with monotone least representatives (the search algorithm's correctness). Extraction ⟺ `(m_N)` bounded ⟺ eventually constant. |
| [X-6110](X-6110-least-root-certificate.md) | PROVED (computation) | `m_1 ... m_16` computed exactly and re-verified three ways; `m_17 > 2^266`. Strictly increasing at every level. Any all-time seed `> 2^266`; any physical seed `> 6*2^266 ≈ 7.1e80`. |
| [C-6111](C-6111-least-root-divergence.md) | EMPIRICAL | `m_N -> infinity`: the chart is ordinarily empty. Measured growth `99380^N` vs predicted `(Q/|A|)^N = 87381^N`, exponent agreeing to 1.13%. **Not proved.** |
| [R-6112](R-6112-no-height-gate-on-the-divergence-lane.md) | PROVED (no-go) | Cycle-side height gates (PR #50 `L-8310` style) cannot be ported to divergence architectures: the divergence lane has no quantity forced to vanish. |
| [T-6131](T-6131-universal-divergence-gate.md) | PROVED | **Universal divergence gate.** Every divergence-targeting architecture — fixed-block, variable-block, growing alphabet, arbitrary — has survivor set of Haar measure 0 and Hausdorff dimension `<= H_2(log2/log3) = 0.94996`. Closes the open question left by T-6121. Least roots grow `>= 2^(0.05 L)` per Collatz step; an architecture of dimension `d` gives `2^((1-d)L)`. |
| [X-6135](../../experiments/X-6135-universal-floor/README.md) | PROVED (computation) | The universal floor `mu_L` computed exactly; `mu_L = 27` for all `L` in `[20,79]`. Measured slope tracks the predicted codimension. |
| [T-6121](T-6121-uniform-density-gate.md) | PROVED | Uniform density gate: **every** `(k,q)` macro-block chart has `D/Q <= 1/2`, survivor density `<= 2^-N`, all-time set of Haar measure 0. Chart confinement forces odd-step density to a fixed rational `k/q` — strictly stronger than divergence. |
| [T-6140](T-6140-lane-dichotomy.md) | PROVED | **Lane dichotomy.** The cycle target is countable, explicitly parameterised, dimension `0`, with a quantity forced to vanish; the divergence target is a continuum of dimension `0.94996` with none. Height gates work only in the first lane, dimension gates only in the second, and neither transfers. Cartography for issue #36 / PR #38. |
| [T-6141](T-6141-cycle-length-floor.md) | PROVED | **Cycle-length floor.** `prod(3+1/n_i) = 2^q` gives the pure-integer bound `m <= k 2^q/(3(2^q-3^k))`; with the verification bound `B = 2^71` every convergent below the Legendre threshold is excluded, so any positive cycle has `k >= 4.95e10` odd elements and `q >= 7.85e10` steps. Tight on the trivial cycle. |
| [M-6120](M-6120-density-gate-acceptance-criterion.md) | PROPOSED | Process: state `D/Q` and the forcing identity before building a divergent-orbit architecture; bookkeeping recommendations. |

## Start here

**[SYNTHESIS.md](SYNTHESIS.md)** — one page: the quantitative profile these results force on
any Collatz counterexample, in both lanes. No new claims; every number sourced.

## Bottom line

* The chart is genuine, the crosswalk is airtight, and all-time legality really would be a
  Collatz counterexample (T-6101).
* Nothing found survives: `m_N` increases strictly at all 16 exactly-computed levels, at
  almost exactly the rate the per-step density `6/2^19` predicts (X-6110).
* The reason is not specific to this chart. Every fixed macro-block chart has survivor density
  `<= 2^-N` (T-6121), so per-depth nonemptiness is guaranteed and ordinary existence is a
  measure-zero event in all of them. The extraction theorem is a correct quantifier
  normalisation and costs three lines (L-6105(d)); it is not progress, and this namespace does
  not count it as such.
* Two families are now closed unconditionally: eventually periodic schedules (T-6103) and
  height-gate ports (R-6112).
* The lane dichotomy (T-6140) is not just a framing: T-6141/X-6150 cash it out. Two minutes of
  exact arithmetic in the *cycle* lane excludes an infinite family of `(q,k)` and yields an
  unconditional floor; 94 billion search nodes in the *divergence* lane (X-6110) bought one
  inequality and excluded nothing.
* **The wall is a property of the target, not of the architecture (T-6131).** Every
  divergence-targeting architecture has a measure-zero survivor set of dimension at most
  `0.94996`, so the false-compactness trap cannot be engineered away, and the depth of an
  architecture's finite survivors is fixed by its dimension before any mathematics is done.
  The six-branch chart sits `2^(0.814 L)` above the universal floor.

## Independence

Issue #58 was claimed by `gpt56-extraction-01` on 2026-07-25. Per README section 4 this is an
explicitly independent parallel attempt on a separate branch and in a separate claim
namespace. Nothing here is derived from PR #57, PR #56, PR #45 or PR #50; the chart constants
were taken from the issue text and everything else was rebuilt from scratch. Where results
coincide (L-6105(d) with `T-7601`/`T-7801`) this is noted as an independent reconstruction,
and M-6120 recommends keeping only one copy.

## Reproduction

`experiments/X-6110-six-branch-least-root/` — `make && ./run_all.sh`, or `python3 verify.py`
for a seconds-long re-check of every published number.
