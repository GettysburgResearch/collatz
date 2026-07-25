# X-6180 — depth profile of the backward tree from 1

```text
Experiment ID:   X-6180
Agent:           claude-opus5-61
Claims:          O-6182; corrects the route comparison in Q-6174
Serves:          issue #25 (coverage-deficit / rooted Krasikov-Lagarias forests)
Environment:     Linux 6.18.5 x86_64, gcc 12 (-O2), 15 GB RAM
Runtime:         ~15 min, ~200 MB
```

## Research question

`n` is reachable from `1` by `d` **backward** shortcut steps exactly when `n` reaches `1` in
`d` **forward** steps. So the backward tree's depth profile is computable forward, by memoised
iteration. Define

```text
coverage(d, X) = #{ n <= X : n reaches 1 within d shortcut steps }.
```

This is the quantity a coverage-deficit argument must control. At what depth does it reach
`X^e` for each exponent `e` — in particular the Krasikov-Lagarias-type exponent `~0.84`, and
`1`?

## Method

Memoised forward iteration with an explicit path stack, so every node on a path is memoised in
one pass. `uint16_t` stopping times, `unsigned __int128` arithmetic, explicit overflow
counter (`0` overflow paths in the published run).

```sh
gcc -O2 -o coverage coverage.c -lm
./coverage 100000000 > results/coverage_1e8.txt
python3 analyse.py results/coverage_1e8.txt
```

## Results, `X = 10^8`

Every `n <= 10^8` reaches 1; the deepest needs `d = 592` shortcut steps.

| exponent `e` | depth `d` reaching `X^e` | `d / log2(X)` |
|---:|---:|---:|
| 0.50 | 30 | 1.13 |
| 0.70 | 45 | 1.69 |
| **0.84** | **65** | **2.45** |
| 0.90 | 80 | 3.01 |
| 0.95 | 105 | 3.95 |
| 0.99 | 160 | 6.02 |
| 0.999 | 220 | 8.28 |
| **1.00 (all of them)** | **592** | **22.28** |

Coverage fraction by depth: `4.4%` at `d = 60`, `54.4%` at `120`, `92.1%` at `180`, `99.3%` at
`240`, `99.9995%` at `360`. **The last 51,361 integers below `10^8` need depth `> 300`.**

## Interpretation

1. **The published exponent is reached very shallowly.** `X^0.84` is covered by depth `65`,
   only `2.45 log2(X)`. Whatever makes the Krasikov-Lagarias-type bound hard to improve, it is
   not that the tree has to be followed deep to reach `0.84`.
2. **The cost is all in the tail.** Going from exponent `0.84` to full coverage takes depth
   `65 -> 592`, a factor of `9`. The profile is extremely top-heavy: half the integers are
   covered by depth `~118`, and the last `0.05%` need more depth than the first `99.95%`.
3. **Exponent 1 is not the conjecture.** `#{n <= X reaching 1} = X^{1-o(1)}` permits `X^{o(1)}`
   exceptions, so even a proof of exponent `1` would not settle Collatz. This is a genuine
   intermediate target — unlike the forward least-root questions, which are equivalent to the
   conjecture (T-6170) — but it is also a *weaker* target, and the comparison in Q-6174 is
   corrected accordingly.

## Scaling across four scales

`c(e) = d(e,X)/log2(X)` at `X = 10^6, 10^7, 10^8, 10^9` (`scaling.py`, `results/scaling.txt`):

| `X` | `e=0.5` | `0.7` | `0.84` | `0.9` | `0.95` | `0.99` | `0.999` | full |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `10^6` | 1.25 | 1.76 | 2.51 | **3.01** | 4.26 | 6.52 | 8.78 | 16.51 |
| `10^7` | 1.08 | 1.72 | 2.37 | **3.01** | 4.09 | 6.24 | 8.60 | 18.45 |
| `10^8` | 1.13 | 1.69 | 2.45 | **3.01** | 3.95 | 6.02 | 8.28 | 22.28 |
| `10^9` | 1.17 | 1.67 | 2.34 | **3.01** | 3.85 | 5.85 | 8.03 | 20.60 |

Logarithmic scaling is confirmed for `e <= 0.9` — exactly `3.01` at `e = 0.9` at every scale.
Above that `c(e)` drifts down, and full coverage does not scale logarithmically at all: it is
set by the single deepest integer.

## Limitations

* Four scales, `10^6` to `10^9`. The `e >= 0.95` drift is unresolved; distinguishing a genuine
  sub-logarithmic correction from a finite-size effect needs `X >= 10^{11}`, a memory problem.
* Says nothing about *provability*: it measures where the tree actually is, not what a
  counting argument can prove about it. Krasikov-Lagarias-type bounds are analytic and do not
  proceed by explicit depth.
* The `0.84` figure is quoted from memory of the literature and is flagged in Q-6174 as needing
  a proper citation.
