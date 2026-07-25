```text
Claim ID:            O-6201
Title:               The backward tree grows at exactly its branching rate 4/3 until coverage
                     X^0.55, and the coverage deficit switches on there
Status:              EMPIRICAL (exact computation at X = 10^8); the branching factor is PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        X-6180 (the profile), X-6200 (branching + deficit)
Scope:               X = 10^8
Serves:              issue #25 (coverage-deficit / rooted Krasikov-Lagarias forests)
```

## The branching factor is exactly 4/3 (proved)

Under the shortcut map, the predecessors of `n` are

* `2n`, always;
* `(2n-1)/3`, exactly when `n = 2 (mod 3)` — and then it is automatically odd, since
  `n = 3j+2` gives `(2n-1)/3 = 2j+1`.

So a node has two predecessors **iff** `n = 2 (mod 3)`, a set of density `1/3`, and the mean
branching factor is exactly `1 + 1/3 = 4/3`. Verified for all `2 <= n <= 300000`, with every
predecessor checked to map back.

Moreover the backward tree from `1` is a genuine **tree**: each `n` has the unique parent
`T(n)`, so there are no duplicate nodes. **Therefore the only way the tree can fail to cover
integers below `X` is by producing nodes above `X`.** The coverage deficit is exactly that
escape, and nothing else.

## The measurement

If no node escaped, coverage would grow by `4/3` per level. Measured at `X = 10^8`
(`deficit.py`), the per-level ratio `coverage(d)/coverage(d-1)` against `4/3`:

| `d` | coverage | ratio | ratio / (4/3) | coverage as `X^e` |
|---:|---:|---:|---:|---:|
| 24 | 2,688 | 1.3287 | 0.997 | `X^0.429` |
| 28 | 8,470 | 1.3341 | 1.001 | `X^0.491` |
| 32 | 26,291 | 1.3207 | 0.991 | `X^0.553` |
| 36 | 77,207 | 1.3117 | 0.984 | `X^0.611` |
| 40 | 200,217 | 1.2497 | 0.937 | `X^0.663` |
| 48 | 945,026 | 1.1736 | 0.880 | `X^0.747` |
| 64 | 6,490,538 | 1.0883 | 0.816 | `X^0.852` |
| 80 | 18,100,301 | 1.0512 | 0.788 | `X^0.907` |
| 160 | 84,149,307 | 1.0040 | 0.753 | `X^0.991` |

**The tree realises its full `4/3` branching, to within `0.5%`, for the first `~32` levels —
up to coverage `X^0.55`. The deficit switches on there** and grows monotonically: by `X^0.75`
the tree is running at `88%` of its ideal rate, by `X^0.91` at `79%`, by `X^0.99` at `75%`.

## Why this is the useful number

The Krasikov-Lagarias-type exponent `~0.84` sits at `d = 62` (X-6180), which is **well past the
onset**: at that depth the tree is already running at about `82%` of its branching rate. So:

* any argument that reaches exponent `<= 0.55` can treat the tree as a free `4/3`-ary tree and
  will succeed without modelling escape at all;
* **any argument that goes beyond `~0.55` must already model the escape of nodes above `X`** —
  and that, not the branching, is what the remaining `0.84 -> 1` has to control.

This localises what issue #25 is actually up against, in one number.

## Gap audit

* The branching factor and the tree property are proved; the onset location is empirical at one
  scale. The `d/log2 X` normalisation is confirmed across `10^6 ... 10^9` for exponents up to
  `0.9` (O-6182), but the *onset* was only measured at `10^8`.
* A comparison of `c(e)` against `c_naive(e) = e * ln2/ln(4/3) = 2.4094 e` is included in
  `deficit.py`, but it is sensitive to an additive constant (the cumulative tree count is
  `~4 (4/3)^d`, not `(4/3)^d`), which matters at small `e`. **The per-level ratio above is the
  constant-free statement and is the one to quote.**
* "Escape above `X`" is the only loss mechanism *because* the backward tree has no duplicates.
  That in turn relies on excluding the trivial cycle `1 -> 2 -> 1`, where `1` and `2` are each
  other's parents.
* This measures where the tree is; it says nothing directly about what is provable.

## The escape model, attempted and only partly successful

The natural next step was carried out in the same session. A depth-`d` path with `b` rare steps
ends near `2^(d-b) (2/3)^b = 2^d 3^(-b)`, and there are about `C(d,b) 3^(-b)` such paths
(summing to `(4/3)^d`, as it must). A node is `<= X` iff `b >= b_min(d) = (d - log2 X)/log2 3`,
giving the parameter-free prediction

```text
coverage(d, X)  ~  sum_{j <= d} sum_{b >= b_min(j)} C(j,b) 3^(-b).
```

Tested against the exact data with **one** normalising constant, fitted once at `d = 24`:

| `d` | measured | model | model/meas | coverage |
|---:|---:|---:|---:|---:|
| 24 | 2,688 | 2,688 | 1.000 | `X^0.429` |
| 32 | 26,291 | 26,608 | 1.012 | `X^0.552` |
| 40 | 200,217 | 220,338 | 1.100 | `X^0.663` |
| 48 | 945,026 | 1,211,540 | 1.282 | `X^0.747` |
| 64 | 6,490,538 | 11,491,758 | 1.771 | `X^0.852` |
| 160 | 84,149,307 | 346,899,643 | 4.122 | `X^0.991` |
| 592 | 100,000,000 | 467,461,524 | 4.675 | `X^1` |

**Verdict: valid to within `10%` while coverage is below about `X^0.66`, and wrong thereafter**
— it ends up claiming `4.7 * 10^8` nodes below `10^8`, which is impossible. So the
leading-order value estimate `2^d 3^(-b)` **understates** the escape: substantially more tree
nodes leave `[1,X]` than the random-walk picture predicts.

That is the useful negative. The coverage deficit is not a bookkeeping artefact of the
branching factor, and it is not captured by the first-order value model either. Whatever
controls the regime beyond `X^0.66` is a genuine feature of the map, and it is precisely the
regime the Krasikov-Lagarias exponent lives in.

## Suggested next attack

Find the second-order correction. The obvious candidate is the correlation between the rare
branch being available (`n = 2 mod 3`) and the value already being large; the leading model
treats those as independent, and the direction of the error (too many nodes predicted below
`X`) is consistent with the rare branch being *less* available on the low-value paths that the
model is counting.
