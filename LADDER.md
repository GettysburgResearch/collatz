# The Fiber Ladder: measurements

*Packets P6–P8 (issue #4). Scripts: `experiments/eq_ladder.py`,
`experiments/chart_bridges.py`, `experiments/fiber_widths.py`
(→ `results/eq-ladder.log`, `results/chart-bridges.log`,
`results/fiber-widths.log`). Theory companion: `SKELETON.md`.
All charts below were independently re-verified exactly before use
(session report 2026-07-21; identities checked to q = 10¹⁸+7).*

## 1. The ladder

Verified supercritical charts, densities marching toward
log₃2 = 0.63093:

| chart | L | N | \|D\| | a/L | per-fiber cost (L−log₂\|D\|)/L |
|---|---|---|---|---|---|
| 64→81 (interval) | 6 | 3⁴ | 2 | 0.66667 | 0.8333 |
| 512→729 (interval) | 9 | 3⁶ | 3 | 0.66667 | 0.8239 |
| 2¹⁷→3¹¹ (interval) | 17 | 3¹¹ | 6 | 0.64706 | 0.8479 |
| 2²²→3¹⁴ (sparse) | 22 | 3¹⁴ | 18 | 0.63636 | 0.8105 |

## 2. Survivor law at every rung (P6; `eq_ladder.py`)

For each chart, the coded sets `R_K` (product-formula coding verified
functionally; `|R_K| = |D|^K` exactly at every measured K) and the
minimal nontrivial survivor against the equidistribution law
`M^K/|D|^K`:

* 64→81, K ≤ 16: ratio ∈ [0.187, 1.905] — matches the migrated
  program's K ≤ 20 range [0.19, 1.9].
* 512→729, K ≤ 13: ratio ∈ [0.048, 2.654]. The 0.048 (K = 11) is a
  ~5% lower-tail event under the exponential min-statistic model
  (P(ratio < x) ≈ x); across the ~40 (rung, K) cells measured, one
  such excursion is expected. Extended checks K = 12: 0.117,
  K = 13: 0.428 — back in band. Fluctuation, not drift.
* 2¹⁷→3¹¹, K ≤ 7: ratio ∈ [0.363, 3.780].
* 2²²→3¹⁴, K ≤ 5: ratio ∈ [0.455, 2.459].

**Verdict: the survivor law holds at every rung; the tripwire did not
fire.** No bending of equidistribution is visible anywhere on the
ladder as density approaches critical. (EMPIRICAL; O-0009.)

## 3. Fiber widths (P8; `fiber_widths.py`)

Independent implementation of the coalescence recursion (derived
directly from the collision identity), L ≤ 26:

* Reproduces the PR #3 width table exactly: max widths 2, 3, 4, 5, 8,
  12, 18 first attained at L = 6, 9, 11, 14, 17, 19, 22.
* **New records: width 18 persists through L = 24; width 26 appears at
  L = 25** (a single fiber), persisting at L = 26.
* The `|D_L|` column (residues in fibers of size ≥ 2) agrees with the
  committed `atlas-spectrum.log` at every overlapping level 16–26 —
  three independent algorithms (chunked scan, coalescence recursion,
  and PR #3's X-0002 through L = 22) now agree on the atlas.
* Growth: log₂(width_max)/L ≈ 0.176, 0.183, 0.187, 0.188 at the
  record levels 17, 19, 22, 25 — slowly rising, ≈ **0.19 bits/level**.

**Model refutation (R-0003).** Under uniform hashing of the ~2^{0.95L}
tight-stratum residues into ~2^L value bins (the birthday picture),
the expected maximum fiber width is O(log L / log log L) —
logarithmic. The observed exponential growth ~2^{0.19L} refutes the
uniform model for fiber widths: `T^L`-values concentrate structurally,
the same phenomenon (in stronger form) that broke the birthday model
for |D_L| (R-0001).

**Composition obstruction (recorded dead end).** The tempting proof of
unbounded widths — "collision fibers compose multiplicatively across
levels via CRT steering" — **fails**: composing a width-k₁ fiber at L₁
with a width-k₂ fiber at L₂ matches the odd-counts but splits the
`T^{L₁+L₂}`-values by the carry offset `c(r′) = (3^{a₁}x(r′)+s₁−r′)/2^{L₂}`,
which varies with the second-level residue. Only the first factor's
width survives the composition. Unbounded width therefore needs a
genuinely different mechanism; the empirical 0.19 slope is unexplained.
(C-0003: conjecture — `log₂ width_max(L)/L → c ≈ 0.19`; EMPIRICAL.)

## 4. Bridge economics (P7; `chart_bridges.py` + `SKELETON.md` §4)

Bridges between any two charts are always CRT-solvable (odd multiplier
invertible mod 2^L) — reachability is free. The Proposition (T-0021)
shows free bridge words from every chart exit are *exactly* binomial
(Terras bijection; measured fraction 0.10506 = null 0.10506 at
j = 16 for all four charts — equality is a theorem, not luck). With
the convexity bound, relay cycles cannot beat the best single rung
(all rungs ≥ 0.81 bits/step, vs the pooled-atlas floor 0.05004).

**Synthesis.** Per-fiber cost is `1 − log₂(width)/L → 1 − 0.19 = 0.81`
bits/step under C-0003 — the width slope *is* the single-fiber cost
story, and it is stuck far above the pooled floor. Consequences:

1. chart *transitions* are economically irrelevant (T-0021);
2. single-fiber grammars pay ~0.81 bits/step forever;
3. the only routes below that are (a) pooling many fibers per level —
   which is exactly the atlas hierarchy already governed by the
   cost-floor theorem (0.05 bits/step, unbeatable by entropy), or
   (b) a structural break in the width law (C-0003 failing upward).

The offense frontier is therefore sharply localized: **either the
width slope c exceeds its entropy budget somewhere (then locate it),
or the S-adic schedule route through pooled atlases is the only
surviving format** — consistent with every rigidity theorem to date
(T-0013, T-0020, T-0003/T3, T4).

## 5. Next moves

1. Explain the 0.19: derive the width-growth exponent from the
   coalescence recursion (branching-process analysis of the even/odd
   merge tree) — target: prove C-0003 or refute the constant.
2. Push the width table past L = 26 (needs ~2.5 GB at L = 28,
   streaming or class-sampled beyond).
3. P2 (EQ interchange) untouched this session — next mathematical
   deep-dive, now with four rungs of dial data.
4. Independent review slots for T-0020/T-0021/L-0015 open (M-0003).
