# X-6110 — exact least-root sequence of the six-branch rational-base chart

```text
Experiment ID:   X-6110
Agent:           claude-opus5-61
Issue:           #58   (Q-7601: decide sup_N m_N < infinity  vs  m_N -> infinity)
Claims:          T-6101, T-6102, T-6103, L-6105, X-6110, C-6111, R-6112, T-6121
Environment:     Linux 6.18.5 x86_64, gcc 12 (-O2), Python 3.11, 4 cores
Randomness:      none (fully deterministic)
```

## Research question

For

```text
P = 3^12 = 531441,   Q = 2^19 = 524288,
A = {229376, 258048, 290304, 326592, 367416, 413343},
x_{n+1} = ceil(P x_n / Q),   d_n = Q x_{n+1} - P x_n,
```

compute `m_N = min { x > 0 : d_0,...,d_{N-1} in A }` exactly, as deep as possible, and test
whether `(m_N)` stabilises (which by L-6105(d) is equivalent to the existence of a positive
all-time seed, and by T-6101 to a divergent Collatz orbit).

## Contents

| file | purpose |
|---|---|
| `lr.c` | the search: DFS over the lift tree, 320-bit fixed-width arithmetic, prune at `2^E` |
| `least_root.py` | independent arbitrary-precision reference implementation (slow) |
| `bf.py` | third, structurally different check: brute-force scan of all `x < 2^40` |
| `merge.py` | merges the six per-branch runs, re-verifies, fits the growth law |
| `verify.py` | self-contained re-verification of the published table (no search needed) |
| `crosswalk.py` | digit algebra `a_i = 7*3^(2i)*2^(15-3i)`, and one physical replay per branch |
| `crosswalk_proof.py` | exact certificate for T-6101: `kappa_i`, residue classes, parity words |
| `converse.py` | shows the chart-illegal shifted class realises `W_i` but lands on an even number |
| `replay.py` | full physical Collatz replay of `m_6`, `m_9`, `m_12` (114/171/228 real steps) |
| `transitions.py` | explicit witnesses that all 36 ordered branch transitions occur (T-6102) |
| `ghosts.py` | native ghost family; exhaustive integral-ghost search over all words `L <= 8` |
| `window.py` | finite decision of all integer periodic orbits (the 25 window candidates) |
| `audit_premises.py` | independent check of the two native-ghost examples supplied in the brief |
| `results/` | raw output of the `2^266` run and the derived tables |

## Commands

```sh
make                      # gcc -O2 -o lr lr.c
./run_all.sh 266          # the 2^266 search, six processes; ~40 min on 4 cores
python3 verify.py         # re-verify the published table (seconds)
python3 replay.py         # physical Collatz replay
python3 window.py         # T-6103(c) finite check
python3 ghosts.py         # native ghosts + integral-ghost search (~1 min)
python3 bf.py             # independent brute force to 2^40 (~10 min)
```

`./lr E D B` runs the search with bound `2^E`, maximum depth `D`, restricted to first digit
`B` (omit `B` to search all six). `E <= 290` and `D <= 16` are enforced by the 320-bit limb
width; the program aborts rather than truncating.

## Result

`m_1 ... m_16` exactly (see `results/least_roots.txt` and the table in
`research/six-branch-ordinary/X-6110-least-root-certificate.md`), and `m_17 > 2^266`.

The sequence is **strictly increasing at all 16 levels** — no stabilisation — with

```text
least-squares fit   log m_N = 11.5067 N - 2.106       (exp(slope) = 99380)
density prediction  Q/|A| = 2^19/6 = 87381.3          (log = 11.3780)
agreement in the exponent: 1.13%
```

Search statistics for the published run: bound `2^266`, `94,037,893,705` nodes visited across
six processes, deepest node depth 16.

## Interpretation

Supports C-6111 (`m_N -> infinity`, i.e. the six-branch architecture contains no divergent
Collatz orbit) and yields the unconditional bound: any positive all-time seed exceeds `2^266`,
so any physical Collatz seed of this architecture exceeds `6 * 2^266 ≈ 7.11 * 10^80`.

## Limitations

* Exact only for `N <= 16`, plus the single inequality `m_17 > 2^266`.
* No finite prefix of `(m_N)` can certify boundedness (L-6105 gap audit), so this experiment
  can never resolve Q-7601 positively-or-negatively on its own.
* Cost per additional level is a factor `6^0.863 ≈ 4.6`; depth 20 needs `~1.7e13` nodes.
* Excludes nothing outside this chart: 6 of the 31824 possible `(12,19)` macro blocks.
