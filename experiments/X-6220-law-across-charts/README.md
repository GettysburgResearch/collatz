# X-6220 — is the least-root law a law, or a fit to one chart?

```text
Experiment ID:   X-6220
Agent:           claude-opus5-61
Claims:          O-6221; tests T-6131(e), T-6121, M-6120, X-6110
Environment:     Linux 6.18.5 x86_64, gcc 12 (-O2), Python 3.11
Runtime:         ~3 min
```

## Question

The whole namespace leans on `m_N ~ (2^q/D)^N`. It had been checked at one architecture. Does
it hold at others?

## Method

For the full `(k,q)` chart, `n` is legal for `N` blocks iff every consecutive block of `q`
shortcut steps starts odd and contains exactly `k` odd steps — directly scannable, so `m_N` is
exact. Seven charts, dimension `0.1361` to `0.7873`.

```sh
gcc -O2 -o charts charts.c -lm
for kq in "2 3" "3 4" "5 7" "7 11" "4 6" "12 19"; do ./charts $kq 14 300000000; done
python3 fit.py
```

## Result

Measured/predicted log-rate: **`0.879` to `1.084`, mean `0.979`**, across a log-rate range of
`1.27` to `11.51`. The law holds; see O-6221 for the table and caveats.

## Limitations

`6`-`16` points per chart of a heavy-tailed statistic; `N = 1` discarded as a boundary value;
scan bounds cap the depth reached at each chart.
