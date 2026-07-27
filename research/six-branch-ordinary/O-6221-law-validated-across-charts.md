```text
Claim ID:            O-6221
Title:               The least-root law m_N ~ (2^q/D)^N validated across seven architectures
                     spanning dimension 0.136 to 0.787
Status:              EMPIRICAL (exact computation)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        T-6121, T-6131(e), M-6120, X-6110
Scope:               full (k,q) macro-block charts, plus the six-branch chart
Experiment:          experiments/X-6220-law-across-charts/
```

## Why this claim exists

Almost everything this namespace asserts about architectures rests on one predictive law:

```text
an architecture of dimension d has least roots growing like 2^((1-d) L) per Collatz step,
equivalently  m_N ~ (2^q / D)^N  per macro block.
```

It underwrites T-6131(e), T-6121, M-6120's gate, O-6182's normalisation, and the headline
message that *the depth of an architecture's finite survivors measures the chart, not the
conjecture*. **Until now it had been validated at exactly one architecture** — the six-branch
chart, `d = 0.136`. A law tested at one point is a fitted constant.

## The test

For the **full** `(k,q)` chart (all `C(q-1,k-1)` words), `n` is legal for `N` blocks iff every
consecutive block of `q` shortcut steps starts at an odd number and contains exactly `k` odd
steps. `m_N` is then computable by direct forward scan, exactly. Seven architectures:

| chart | `D` | `dim` | predicted log-rate | fitted slope | ratio | points |
|---|---:|---:|---:|---:|---:|---:|
| `(2,3)` | 2 | 0.3333 | 1.3863 | 1.2733 | 0.918 | 13 |
| `(3,4)` | 3 | 0.3962 | 1.6740 | 1.6526 | 0.987 | 10 |
| `(4,6)` | 10 | 0.5537 | 1.8563 | 1.6315 | 0.879 | 10 |
| `(5,7)` | 15 | 0.5581 | 2.1440 | 2.3233 | 1.084 | 7 |
| `(7,11)` | 210 | 0.7013 | 2.2775 | 2.2557 | 0.990 | 7 |
| `(12,19)` | 31824 | 0.7873 | 2.8018 | 2.7614 | 0.986 | 6 |
| six-branch | 6 | 0.1361 | 11.3780 | 11.5067 | 1.011 | 16 |

```text
mean ratio measured/predicted : 0.9794
range                         : 0.879 to 1.084
dimension range covered       : 0.1361 to 0.7873
log-rate range covered        : 1.27 to 11.51   (a factor of 9)
```

**The law holds across the whole accessible range, to within `+-12%` in the exponent and `2%`
in the mean.** The six-branch chart, with a log-rate nine times larger than the `(2,3)` chart,
is fitted by the same formula with no adjustment.

## What this does and does not establish

* It establishes that `m_N ~ (2^q/D)^N` is a *law*, not a coincidence of the one chart it was
  discovered on. The consequences drawn from it in T-6131(e), T-6121 and M-6120 stand on
  measured ground.
* It does **not** upgrade the law to a theorem. The passage from exact density (which is
  proved, L-6105(a)) to least roots assumes equidistribution of the surviving classes, and
  that remains the C-6111 heuristic. Seven confirmations are seven confirmations.

## Gap audit

* Fits use `6` to `16` points of a heavy-tailed extreme-value statistic (`m_N` is essentially
  the minimum of `D^N` residues spread over `[0, 2^qN)`), so `+-10%` scatter in a slope is
  expected and observed. The `(4,6)` chart at `0.879` and `(5,7)` at `1.084` are the extremes
  and both use few points.
* `N = 1` is discarded everywhere: it is a boundary value, not governed by the asymptotic law
  (e.g. `(12,19)` has `m_1 = 97`, giving a spurious `log m_1/1 = 4.57` against a rate of 2.80).
* The charts are the *full* `(k,q)` families; the six-branch chart is a `1:5304` restriction of
  one of them. That the law fits both a full family and a thin restriction of it is the most
  informative single line of the table.
* Scan bounds limit depth: `(12,19)` reached only `N = 7` before `m_8 > 4 * 10^8`.

## Suggested next attack

None on the law itself — it is now adequately tested. The useful follow-on is the one M-6120
already asks for: have each open lane in this repository publish its `D/Q` and its predicted
least-root growth, and check its own measured survivors against this curve. Any lane whose
survivors grow *slower* than `(2^q/D)^N` is a genuine anomaly and should be escalated; any lane
that tracks it is on the predicted path to emptiness.
