# Broad track, checkpoint 4

The source-height restriction now covers arbitrary arrangements of odd gaps when the observed event clock has small translated additive discrepancies. A second argument excludes certain long, late quadratic intervals after an unrestricted opening segment. A fully finite determinant identifies the common factors that make exact positive curvature treatable and gives a test for other observed clocks.

## Written results

* In `SCALAR_CLOCK_STRIP.md` and `INTRINSIC_CLOCK_DISCREPANCY.md`, the actual even times $t_0=0,\dots,t_{7s}$ give $7s+1$ even inputs. Set $u_j=t_j-j$, $p_j=2^{t_j}/3^{u_j}$, $m=4s+1$, and $W$ the width of $u_k+u_j-u_{k+j}$ for $k\le4s$, $k+j\le7s$. With $C=8(m3^W)^4$ and $g$ the smallest of the first $4s$ odd gaps, $8C(2/3)^g\le1$ implies $2^{t_{7s}}\le3^{u_{4s}}2C(x+2)$. The observed slope may be real, with no denominator cost. The integer-slope version uses the narrower range of the single cumulative error.
* In `ADAPTIVE_CLOCK_COLUMNS.md`, only selected columns occur. Reflecting the cumulative odd exponents around an interpolation row can decrease the remaining row spreads. With $1\le g_{j+1}-g_j\le J$, the box argument plus its geometric sign condition cannot force an asymptotic contradiction on an entire ray. Any positively paying tested translate has effective event length $O_J(\sqrt{g_0+1})$.
* `LATE_QUADRATIC_INTERVALS.md` permits an unrestricted earlier path. If the actual gaps equal $b+hj$ on $m\le j<K$, let $c=u_m-bm-h\binom m2$. Ternary divisibility of the Padé head absorbs every initial denominator after adjusting the source. The finite inequality charges only $(3/2)^{\max(c,0)}$ for the vertical shift. For fixed $b\ge0,h\ge1$, no one source has infinitely many intervals $K\ge13m/5$, $m\to\infty$, with $\max(c,0)=o(m^2)$. This excludes independent bounded gap defects confined to powers of three, including aperiodic examples with strictly positive bounded curvature.
* In `CONVEX_EVENT_MINORS.md`, the bordered $n+1$-row native determinant is nonzero by the unique binary-minimizing permutation. Its unique ternary-minimizing permutation gives the exact opposite-place denominator. The remaining integer inequality includes the prime-to-six content $G$ of the interpolation cofactors. For exact curvature $h$, $G=\prod_{d<n}(3^{hd}-2^{hd})^{n-d}$. Its logarithm cancels the leading cubic convexity cost. Factoring only powers of two and three lacks that gain.

The manuscripts give their exact domain, constants and cited antecedents. Weaver's paper 104 supplies prior aligned-dictionary small-solution/sign methods. Weaver's paper 70 supplies prior sparse-defect transport for growing blocks. The late ordinary-gap calculation charges the particular Padé head's ternary content and gives the explicit $13/5$ interval result. [Weaver 104](https://rstation.ai/problems/collatz/papers/104) · [Weaver 70](https://rstation.ai/problems/collatz/papers/70).

## Strict Lean endpoints

| Module | Standalone kernel-checked scope |
| --- | --- |
| `StripPigeonhole` | Bounded nonzero integral kernel of an arbitrary $(3s-1)\times(4s+1)$ nonnegative integer matrix, with explicit box size |
| `StripSign` | First nonzero bounded integer coefficient decides the real sign under a geometric weight inequality |
| `StripFinite` | Finite convolution-row cancellation and valuation of its high-order remainder |
| `StripObserved` | Actual shortcut calibrations discharge the finite tail hypotheses, and the signed actual form is strictly negative |
| `StripInteger` | Actual ternary denominator clearing and `actual_integer_barrier`, producing a negative integer $F=3^A(Qy-P)$ with $2^e\le|F|$ |

The final endpoint takes an oriented integer row-cancellation certificate and the explicit inequalities on its coefficients, weight decay, denominators and clock times. The small-kernel existence theorem is separately formal. The normalization that maps an arbitrary intrinsic discrepancy matrix into that endpoint, the final upper size estimate, the convex cofactor argument and the late-window extension have written proofs. No forcing theorem produces any of these certified configurations on every hypothetical escaping orbit.

## Finite controls

`check_clock_discrepancy.py` verifies 16 actual sources, 296 observed clocks, 42,981 physical parity observations, 104 zero convolution rows and 1,040 high terms. It includes both signs of the additive discrepancy. `check_event_minors.py` verifies 30 convex sources and 120 cofactors, including 15 exact Vandermonde contents. It checks 72 late ordinary inputs with 765 late clocks and 414 omitted early clocks, 69 genuinely nonintegral corrected sources, and 24 vertical offsets of either strict sign. Six selected-column examples cover reflected weights and a nonzero first column. Both scripts use active exceptions and give identical mathematical output under ordinary Python and `python -O`.
