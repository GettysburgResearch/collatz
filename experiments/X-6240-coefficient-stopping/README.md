# X-6240 — attacking the coefficient-stopping-time question

```text
Experiment ID:   X-6240
Agent:           claude-opus5-61
Claims:          C-6241 (heuristic model), T-6242 (the theorem, which corrects C-6241)
Environment:     Linux 6.18.5, gcc 12 (-O2), Python 3.11 (fractions/decimal only)
Runtime:         heuristic.py ~1 min; chi_bound.py 1.3 s to j=3000; chi_fast ~1.6 min to j=2e5
```

## Question

`chi(n) <= sigma(n)` always (L-6173a). Is `chi = sigma` for all `n > 1`? Open since Terras 1976.

L-6173(b) reformulates the search over **words**: a counterexample with `chi(n) = j` satisfies
`n <= c_w/D`, `D = 2^j - 3^{k_j}`, with `n` fixed mod `2^j` by its word.

## Contents

| file | purpose |
|---|---|
| `heuristic.py` | exact `sum_w c_w` by DP; expected-counterexample series `E_j` (C-6241) |
| `chi_bound.py` | exact rational `Bmax(j) = max_w c_w/D`, to `j = 3000` |
| `chi_bound_fast.c` | log-space version of the same, to `j = 200000` (T-6242) |
| `maxbound.py` | first version, per-`j` re-run (superseded by the single-pass DP) |

## Headline result (T-6242)

```text
Bmax(j) < 2*10^9  for every j <= 125742,
and chi = sigma is verified for all n <= 2*10^9 (L-6173c)
=>  no counterexample to chi = sigma has chi(n) <= 125742.
```

The running maximum first reaches `2*10^9` at `j = 125743` — **the convergent `125743/79335`
of `log2(3)`**, where `2^j - 3^k` has `125725` bits against `2^j`'s `125743`. The same
convergents that govern the cycle floor (T-6141) govern this bound.

A scan of `2*10^9` integers therefore certifies `chi = sigma` for every `n` **of any size**
with `chi(n) <= 125742`.

## Verification

Exact rational and log-space float implementations agree wherever both run:
`867.1` at `j <= 100` (both), `9266.54` vs `9267` at `j = 317`, `420842` vs `4.208*10^5` at
`j = 2593`.

## Limitations

See T-6242's gap audit — in particular the `j > 3000` range rests on the float implementation,
and corollary (e) is heuristic.
