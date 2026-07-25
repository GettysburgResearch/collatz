```text
Claim ID:            X-6110
Title:               Exact least-root sequence of the six-branch chart through depth 15
Status:              PROVED (finite exact computation; every value independently re-verified)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        L-6105 (algorithm correctness), T-6101 (physical meaning)
Scope:               the fixed chart of T-6101
Related counterexample candidates: none found
Experiment:          experiments/X-6110-six-branch-least-root/
Answers:             issue #58 / Q-7601, quantitatively but not decisively
```

## Research question

For the six-branch chart, compute `m_N = min { x > 0 : x is legal for N steps }` for as many
`N` as exact computation allows, and test the hypothesis `sup_N m_N < infinity`.

## Result

Every value below is exact. Each was independently re-verified by *forward iteration*
(`x -> ceil(Px/Q)`, checking the digit lies in `A`) from the printed integer, and the recorded
digit word was recomputed rather than trusted.

| `N` | `m_N` | digit word | `m_N/m_{N-1}` |
|---:|:---|:---|---:|
| 1 | 6472 | `4` | – |
| 2 | 1908874353 | `50` | 294944 |
| 3 | 44906374791168 | `041` | 23525 |
| 4 | 275202518480529950784 | `3222` | 6128362 |
| 5 | 735266885070322294097984 | `31552` | 2672 |
| 6 | 49927377479016341945330731072 | `345415` | 67904 |
| 7 | 31262847560142629190894965371116657 | `5500454` | 626166 |
| 8 | 181625992579115023082252809688279976000 | `34150040` | 5810 |
| 9 | 274731072270742333628800865325991165013963264 | `252541135` | 1512620 |
| 10 | 1986427850123090115679978949016973174519765670216 | `4032154251` | 7230 |
| 11 | 597061551299008579089934000992013372324288526534606848 | `03512524310` | 300570 |
| 12 | 83301137368103499460139839972641009013711852735287572369408 | `134324152111` | 139519 |
| 13 | 30699375960653180905548356146446826616831594299893600882131999048 | `4515040532345` | 368535 |
| 14 | 5507203783350029278298158112206428933561267597997030606259626621304832 | `01123340100302` | 179391 |
| 15 | 148637017271338238565064267618715766778481872048601196567971011267386061312 | `205431351450115` | 26990 |
| 16 | 4629285799073801695890071893291563216294381998435632568233291338101143197194568 | `4450023324032350` | 31145 |

and, from the exhaustion of the search bound,

```text
m_17 > 2^266 = 118571099379011784113736688648896417641748464297615937576404566024103044751294464.
```

**Consequences (unconditional).**

* `(m_N)` is **strictly** increasing for every one of the 16 computed levels. There is no
  stabilisation anywhere in the computed range, so the L-6105(d) criterion
  ("bounded ⟺ eventually constant ⟺ an all-time seed exists") is not met at any depth
  reached.
* Since `m_N` is nondecreasing, **any** positive all-time seed `x` of the six-branch chart
  satisfies

  ```text
  x  >  2^266  ≈  1.1857 * 10^80,
  ```

  and by T-6101 the corresponding physical Collatz seed satisfies

  ```text
  n = 6x - 5  >  6 * 2^266  ≈  7.1143 * 10^80.
  ```

* Each `m_N` passes exactly `N` gates and fails gate `N+1` (immediate from strict increase).

## Method

Depth-first walk of the lift tree of L-6105(b), pruning any node whose least positive
representative exceeds `B = 2^266`, which is valid by L-6105(c). Node state is the pair
`(r, X_k)`; the six children are computed with one modular multiplication each. Fixed-width
320-bit arithmetic (5 x 64-bit limbs) with a compile-time guard against shift overflow.

The search was split into six independent processes, one per first digit, and the per-depth
minima merged. Totals:

```text
nodes visited (all six processes) : 94,037,893,705
search bound                      : 2^266
maximum depth reached under bound : 16
wall time                         : ~40 min on 4 cores
```

An earlier run at bound `2^256` (15,749,362,937 nodes) agrees on every value it reached.
The node counts match the predicted `~1.2 * D^(log2 B / q)` — `1.2 * 6^(256/19) = 1.7e10` and
`1.2 * 6^(266/19) = 8.9e10` — to within 8% and 6%, itself a check that no subtree was
silently skipped.

## Verification performed

1. **Two independent implementations.** A Python reference implementation (`least_root.py`,
   arbitrary precision) and the C search (`lr.c`, fixed 320-bit) agree exactly on
   `m_1 ... m_6` (the range reachable by the Python version).
2. **A third, structurally different algorithm.** Brute-force scan of every `x < 2^40` in the
   six admissible residue classes mod `2^19` (`bf.py`) reproduces `m_1 = 6472`,
   `m_2 = 1908874353`, and finds no `x < 2^40` surviving 3 gates — consistent with
   `m_3 = 4.49 * 10^13`.
3. **Forward re-verification.** Every one of the 15 values was re-run through the forward map
   and its digit word recomputed (`merge.py`). All 15 verified.
4. **Physical replay in real Collatz arithmetic.** For `m_6`, `m_9` and `m_12`, the trajectory of
   `n = 6 m_N - 5` under the shortcut map was computed for `19N` steps (`replay.py`):
   the endpoint equals `6 x_N - 5`, the odd-step count is exactly `12N`, and the realised
   parity word equals the predicted concatenation of blocks `W_i`. This checks T-6101 on
   numbers of 29, 46 and 59 digits (`replay.py` also covers `m_12`).
5. **Sanity of the pruning rule.** Runs at bounds `2^60`, `2^110`, `2^160`, `2^256` and
   `2^266` agree on every `m_N` they share.

## Interpretation

The data is a clean geometric law. A least-squares fit gives

```text
log m_N = 11.5067 N - 2.106,        exp(11.5067) = 99380,
```

against the density prediction `Q/|A| = 2^19/6 = 87381.3` (`log = 11.3780`). The exponent
agrees to 1.13%; the residual spread is what an extreme-value model predicts, since `m_N` is
essentially the minimum of `6^N` residues spread over `[0, 2^19N)` and `log` of such a minimum
has fluctuation of order 1 in natural units. The individual ratios swing between `2.7e3` and
`6.1e6` around the mean, exactly the heavy-tailed behaviour expected; no ratio is anywhere
near `1`.

This is evidence for `m_N -> infinity`, i.e. for the **negative** resolution of Q-7601. It is
not a proof, and by L-6105's gap audit no finite prefix of `(m_N)` ever could be.

## Limitations

* The computation certifies `m_N` for `N <= 16` and the single inequality `m_17 > 2^266`.
  It says nothing about any `N > 17`.
* The cost of certifying `m_N` grows like `D^(N log(Q/D)/log Q)`, i.e. roughly `6^(0.863 N)`
  for this chart. Reaching `N = 20` costs about `6^17 ≈ 1.7 * 10^13` nodes — feasible only
  with a large cluster; `N = 30` is out of reach by this method forever. Deepening is
  therefore a losing game and should not be pursued past the point of establishing the law.
* A negative resolution of Q-7601 would exclude only this chart (6 of the 31824 possible
  `(12,19)` macro blocks — see M-6120).

## Reproduction

```text
cd experiments/X-6110-six-branch-least-root
make            # builds lr from lr.c
./run_all.sh 266  # reproduces the table (bound 2^266, ~40 min on 4 cores)
python3 verify.py   # re-verifies every published value by forward iteration
```
