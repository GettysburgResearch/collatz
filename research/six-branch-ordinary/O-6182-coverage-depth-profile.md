```text
Claim ID:            O-6182
Title:               Measured depth profile of the backward tree from 1, and what it costs to
                     push the coverage exponent
Status:              EMPIRICAL (exact computation, single scale)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        X-6180
Scope:               X = 10^8
Serves:              issue #25
```

## Statement

For `X = 10^8`, with `coverage(d) = #{n <= X : n reaches 1 within d shortcut steps}`:

```text
coverage reaches X^0.50 at d =  30      X^0.95  at d = 105
                 X^0.70 at d =  45      X^0.99  at d = 160
                 X^0.84 at d =  65      X^0.999 at d = 220
                 X^0.90 at d =  80      X       at d = 592
```

Every `n <= 10^8` reaches 1, the deepest at `d = 592`. The last `51,361` integers below `10^8`
require depth `> 300`.

## Three readings

1. **The Krasikov-Lagarias-type exponent `0.84` lives at depth `65`** — only `2.45 log2(X)`.
   The obstruction to improving it is not depth.
2. **The whole cost is the tail.** `0.84 -> 1` costs a factor `9` in depth. Half of all
   integers are covered by depth `~118`; the last `0.05%` need more depth than the first
   `99.95%`.
3. **Exponent `1` is a genuine intermediate target, but a weaker one than the conjecture.**
   `X^{1-o(1)}` coverage permits `X^{o(1)}` exceptions. Contrast T-6170, where the forward
   least-root question is *equivalent* to Collatz.

## Correction to Q-6174

Q-6174 compared the two routes as "forward gap `0.535` of dimension versus backward gap `~0.16`
of exponent — roughly three times narrower" and recommended the backward lane on that basis.
That comparison is **not like-for-like**, and this file corrects it: closing the forward gap
would *prove the conjecture*, whereas closing the backward gap would not. The backward target
is both nearer and weaker. The recommendation survives in weakened form — the backward lane is
the one not capped by T-6131 — but the numerical comparison should not be quoted as if the two
gaps were the same kind of object.

## The scaling is logarithmic, and `c(e)` is an invariant

The "suggested next attack" below was carried out in the same session: the profile was
recomputed at `X = 10^6, 10^7, 10^8, 10^9`. Writing `d(e, X)` for the depth at which coverage
first reaches `X^e`, the normalised quantity `c(e) = d(e,X)/log2(X)` is:

| `X` | `e=0.5` | `0.7` | `0.84` | `0.9` | `0.95` | `0.99` | `0.999` | full |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `10^6` | 1.25 | 1.76 | 2.51 | **3.01** | 4.26 | 6.52 | 8.78 | 16.51 |
| `10^7` | 1.08 | 1.72 | 2.37 | **3.01** | 4.09 | 6.24 | 8.60 | 18.45 |
| `10^8` | 1.13 | 1.69 | 2.45 | **3.01** | 3.95 | 6.02 | 8.28 | 22.28 |
| `10^9` | 1.17 | 1.67 | 2.34 | **3.01** | 3.85 | 5.85 | 8.03 | 20.60 |

**Confirmed for `e <= 0.9`:** `d(e,X) ≈ c(e) log2(X)` with `c(e)` stable across three orders of
magnitude — and at `e = 0.9` the ratio is `3.01` at every scale tested, to two decimals.

For `e >= 0.95` the ratio drifts slowly downward (`4.26 -> 3.85`, `6.52 -> 5.85`), so the
logarithmic law is at best approximate there. **Full coverage does not scale logarithmically at
all** (`16.51, 18.45, 22.28, 20.60` — non-monotone): it is set by the single deepest integer, an
extreme-value statistic, not a bulk property.

So the curve

```text
c(0.5) ~ 1.15,  c(0.7) ~ 1.7,  c(0.84) ~ 2.4,  c(0.9) = 3.01,
c(0.95) ~ 3.9,  c(0.99) ~ 5.9,  c(0.999) ~ 8.0,  c(1) undefined
```

is the precise shape of what a coverage argument must climb, and its blow-up as `e -> 1`
locates the difficulty: not in reaching a high exponent, but in the last sliver, where the
governing statistic stops being a bulk average.

## Gap audit

* Four scales `10^6 ... 10^9`; the logarithmic law is confirmed for `e <= 0.9` and only
  approximate above, with full coverage not scaling logarithmically at all.
* Measures where the tree is, not what is provable about it. Analytic tree-counting bounds do
  not proceed by explicit depth, so a shallow empirical depth does not imply an easy proof.
* The `0.84` is quoted from memory of the literature (Krasikov-Lagarias-type) and needs a
  proper citation before the comparison is relied upon.

## Suggested next attack

Done in-session (see above): the scaling holds for `e <= 0.9`. What remains open is the
`e >= 0.95` regime, where `c(e)` drifts downward — is that a genuine sub-logarithmic
correction, or a finite-size effect that settles? Distinguishing them needs `X = 10^{11}` or
beyond, which is a memory problem (one byte per integer), not a time problem.
