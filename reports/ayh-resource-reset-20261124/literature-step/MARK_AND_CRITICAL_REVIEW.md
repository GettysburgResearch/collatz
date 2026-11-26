# Independent review of the mark count and common-scale critical fibers

Reviewed the statements and proof dependencies in the following versions.

| File | SHA-256 |
| --- | --- |
| `ForwardPliss.lean` | `8fad3c80e839a5e20a8fdc7b527224d80b8a3763e0438aa56be103675d724b2e` |
| `DiscordantPliss.lean` | `5e571fc7647f5cded16ebc9eb6b872dd62957ef77e082829f4b97f8ed6c032d6` |
| `BallisticColor.lean` | `f7fd5e2f4366de7a44447383337331ddd859f6f877a14d98ad602de4af030bd4` |
| `CRITICAL_SMALL_SCALE.md` | `942e3b489370d438dd50dbcb0ec9193fcf0dfdf7bca09b918268838079651c74` |
| `POST_DESCENT_TRANSFER.md` | `daf6edcf171ac3dfaf39486a6fe9fac08338da846b6fef8a2a5c78281cf37efa` |
| `CRITICAL_COMPRESSION.md` | `084f96f58618efced8ae55444be5d0461be3603826ed089b5f94e8b9fcf33d24` |
| `BASIN_COUNTING.md` | `d244fd5a0f19be23a52c28e27f9897a9485ab49958714cf997d6d340478538a0` |

**Mark count.** The integer tail minimum exists and is nondecreasing. A strict increase forces a record at its left endpoint, and the upper increment bound controls the jump even when the walk has downward jumps. Telescoping gives the claimed count on `Finset.range N`. The instantiation uses the same ordinary trajectories in every window and fixes the orientation from the bad arm to the good one. Its predicate quantifies over every future block length. The denominator 15 and allowance `2*(5*L+4*q+4)` follow from the exact laws for `16*(p_bad−p_good)−t`. The theorem with an existential allowance places it before the universal time horizon. For each fixed pair, division by `N` gives the stated lower time density. Anticipative records do not supply a new probability distribution on sources. These conclusions follow from statement and proof review. The parent build records the compiler audit separately.

**Common-scale partners.** In every exact fiber under consideration the map to odd endpoints is injective. The endpoints occupy one residue modulo six in the marked interval, giving cardinality comparable to `U/d`, where `log₂ U=4d/5+O(1)`. The enclosing one-arm estimate therefore loses a factor of order `d`, and its relative exception is `O_β(2^(−c_* d/2))`. At `d=AQ`, the two height exponents for the ordinary endpoint are respectively `7Q/10+O_β(1)` and `9Q/10+O_β(1)` in binary logarithms. Thus the delayed endpoint lies in `[Q²,2^(2Q)]` at large `Q`. Its ternary-unit property holds after the first physical odd step. The first, four-clock section of `BASIN_COUNTING.md` covers every such target, including even units. Its inverse source reaches the original target, with `log₂ m≤(5/4)(2+log₂(16/3))Q+O(1)<6Q<βd` because `βA≥8`. The inverse prefix to the odd endpoint costs `O(Q)` by its valuation and the remaining clocks cost at most `4Q`. The forward source uses `e+h=O_β(d)` clocks. These estimates apply simultaneously to all nonempty fibers at the selected octaves. They allow the surplus to change, and establish a written structural consequence without a pointwise or fixed-floor claim.

**Independent second orbit addendum.** For a fixed full second orbit, the number of its distinct states up to `Y` is uniformly `O(Y^0.98)`. On the complete binary period of length `2^ℓ` with `ℓ=ceil(log₂Y)`, the high-count words give exponent `H₂(3/5)<0.98`. For low counts the affine formula normalized by `3^p` has intercept at most `(1−2^(−ℓ))/3`, giving range exponent `(3/5)log₂3<0.98`. On a cyclic orbit with a preperiod, discarding at most the last `ℓ` transient states leaves the `ℓ`-step map injective on the retained states. At each precritical first clock, multiplying the number of targets by the first-arm multiplicity saves `0.02α−1.98η>0`. A union over its `O(log R)` clocks and averaging over an independently chosen second orbit preserve a power saving. This uniformly covers unlimited clocks of the second arm; it does not assert the same bound for a deterministically linked pair of sources.

No mathematical discrepancy was identified in the reviewed results at the stated hashes.
