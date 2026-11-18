# Which observations distinguish escape from convergence?

**The Collatz conjecture remains open.** This continuation of the [earlier investigation](../2026-11-18-four-hour-investigation/README.md) studies two possibilities that would disprove it. A positive orbit could escape every finite set, or it could enter a periodic orbit other than the one through 1. The new arguments below are proposed proofs. The computations replay exact finite instances.

## The signal for escape can recur on a path to 1

Use the accelerated map on positive odd integers, $U(x)=(3x+1)/2^{v_2(3x+1)}$. For an odd target $y$, the paper considers a positive quantity $K(y)$ that weights the paths entering $y$ by their real affine offsets. Every hypothetical escaping orbit has $K(y)$ at least proportional to $\log y$ at every sufficiently late state. A natural strategy was to prove that the ratio becomes small once a state is far from simple rational phases in ternary digits. The construction disproves that upper bound. [Definition and necessary escape bound](../../research/critical-orbit-mellin/STIELTJES_ESCAPE_FLOOR.md) · [Ordinary construction and proof](../../research/critical-orbit-mellin/ORDINARY_PHASE_AVOIDANCE.md)

- At any prescribed ternary unit, including an irrational one, ordinary positive integers approaching that phase can have $K(y)\gg\log y$. The phase can be prescribed independently of a later visit to 1.
- Fix any power $A>0$. There is one infinite sequence of distinct positive odd integers $x_0=1,x_1,x_2,\ldots$ with $U(x_{i+1})=x_i$. At a positive lower proportion of indices, $K(x_i)\gg\log x_i$ and none of the rational units of height up to $(\log x_i)^A$ matches $x_i$ to more than $O_A(\log\log x_i)$ ternary digits. The sequence contains arbitrarily long forward segments with this behavior that stay at or above their starting height. In fact the family of such paths has positive Hausdorff dimension when two paths sharing exactly $N$ reverse shortcut steps have distance $2^{-N}$. Positive lower frequency also holds when intervening even steps are counted. Every vertex of each infinite **backward** path reaches 1 in finitely many **forward** steps.
- For each sufficiently large $X$, at least $X^\gamma$ distinct ordinary starts below $X$ have such segments of length proportional to $\log X$ and reach any supplied positive odd unit $b$ later. Here $\gamma>0$ and the onset is allowed to depend on the fixed parameters. Their later paths may merge. The bounded-cost routing step uses Theorem 8 of the cited preprint. The analytic trace inequality uses the bounded real-offset estimate. [Full proof and source boundaries](../../research/critical-orbit-mellin/ORDINARY_PHASE_AVOIDANCE.md) · [Modular routing theorem](https://rstation.ai/problems/collatz/papers/48/v2)

Two ordinary examples were followed all the way to 1 with integer arithmetic. The forward replay checks the valuation at each prescribed step and the incoming affine offset. The infinite trace estimate enters through the analytic result above. [Runnable integer replay](../../research/critical-orbit-mellin/check_phase_avoidance.py)

| Finite example | Endpoint size | Further odd steps to 1 | Further shortcut steps to 1 |
|---|---:|---:|---:|
| Endpoint matches a ternary square root of 10 modulo $3^{64}$ | 3,350 bits | 8,280 | 16,473 |
| 65 consecutive ordinary states avoiding 2,506 rational residues modulo $3^{22}$, all at least the segment start | 3,451 bits | 8,035 | 16,186 |

## Smaller ancestors at every depth

For each $j$, take the odd positive starts $n$ such that **no smaller positive odd integer ever reaches $U^j(n)$**. The incoming competitor gets arbitrarily many steps. Write $b_j$ for the natural density of those starts among odds. The proposed result is $\lim b_j^{1/j}=3^{h-1}=0.9465045768\ldots$, with $h=H_2(\log_3 2)$. The same exponential rate already occurs when testing forward homogeneous descent alone. In the space of binary digits, the set surviving all the comparisons has Hausdorff dimension $h=0.949955527\ldots$. Whether that set contains a positive ordinary integer is equivalent to whether any positive orbit escapes. A separate finite-shell estimate covers $j\le10^{-6}\log_2 X$ with an asymptotic error and no numerical onset. [Definition and density transfer](../../research/fixed-floor-shells/BILATERAL_MINIMUM.md) · [Exponent and dimension](../../research/fixed-floor-shells/BILATERAL_DIMENSION.md) · [Finite-shell scope](../../research/fixed-floor-shells/BILATERAL_FINITE_SHELL.md)

Exact depth-16 enumeration over $3^{16}=43,046,721$ ternary classes, combined with the proven-in-packet residual estimate, gives the following outward-rounded enclosures for the all-depth densities. [Bounds and residual estimate](../../research/fixed-floor-shells/BILATERAL_MINIMUM.md) · [Integer checker](../../research/fixed-floor-shells/check_bilateral_minimum.py)

| Forward odd steps $j$ | Lower bound for $b_j$ | Upper bound for $b_j$ |
|---:|---:|---:|
| 1 | 0.256594 | 0.260595 |
| 5 | 0.064684 | 0.067495 |
| 10 | 0.019835 | 0.022532 |

## Remaining routes to a decision

| Route | What the continuation establishes | What would decide more |
|---|---|---|
| Escape through a spatial average | Each escaping component forces at least linear mass near zero in the limiting measure of relative offsets. Its Stieltjes transform $L(c)$ consequently exceeds a constant times $(\log c)/c$. At typical ordinary targets the full inverse measure admits a periodic approximation for bounded continuous tests. [Transform bound](../../research/critical-orbit-mellin/STIELTJES_ESCAPE_FLOOR.md) · [Typical targets](../../research/critical-orbit-mellin/FULL_FIBRE_IN_PROBABILITY.md) | An ordinary bound $L(c)=o((\log c)/c)$ along any unbounded sequence would rule out escape. The missing estimate concerns the mass at exceptional targets. |
| Cycles and divisibility | Primitive positive rational cycles can have every rotation numerator sharing almost the whole divisor $2^L-3^K$, while the reduced denominator exceeds one and has no prime factor up to $c_\epsilon\log L$. A separate variance test uses all phases even when $L$ and $K$ are coprime. Its exact value $204860/108241<4$ rejects the word 1101010. [Denominator construction](../../research/unrestricted-cycle-denominator/ROUGH_DENOMINATORS.md) · [Variance test](../../research/unrestricted-cycle-denominator/COPRIME_SEAM.md) | A uniform obstruction to exact divisibility at every rotation of an arbitrary nontrivial putative integer cycle. |
| Compression of one actual forward path | A simple ordinary segment formed from a fixed number of repeated parity blocks satisfies $L\le(1+\epsilon)\log_2(n+1)+O_{m,\epsilon}(B+1)$, where $B$ counts the unexpanded block lengths and the intervening letters. [Pointwise proof](../../research/pointwise-run-defects/COMPRESSED_DESCENT.md) · [Recursive version](../../research/pointwise-run-defects/RECURSIVE_COMPRESSION.md) · [Three-block determinant](../../research/pointwise-run-defects/TWO_PRIME_HANKEL.md) | A proof that a hypothetical escaping ordinary orbit has sufficiently compressed segments. |
| One finite scalar for both obstructions | A separate derivation of the earlier scalar limit uses Tao's published passage and trajectory bounds at one fixed scale, together with the reconstructed inverse estimates and simple-orbit arithmetic. The limit is zero exactly when every positive integer reaches 1. [One-scale proof](../../research/primary-evidence/ONE_SCALE_CLOCK.md) · [Finite scalar definition](../../research/critical-orbit-mellin/TWO_SCALE_TEST.md) · [Primary sources](../../research/primary-evidence/PRIMARY_SOURCES.md) | Determining the value of the limit. Its finitely computed entries give no convergence rate deciding that value. |

## Computational and source checks

The portable repository regression command is `python -X utf8 -B tools/validate.py --regressions`. The [replay receipt](REPLAY.md) records the scope and inputs of the clean-checkout run. The [source audit](../../research/primary-evidence/PRIMARY_SOURCES.md) separately checks 1,602 archived source hashes and dependency fingerprints and 1,787 recorded axiom reports. Four native Lean modules were freshly rebuilt through the inverse-block theorem. The canonical trace has 919 modules in its dependency closure. Its full local rebuild remained incomplete after the binary cache returned HTTP 403 and the source build stopped in prerequisites.
