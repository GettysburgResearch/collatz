# Finite first moments of ordinary orbit minima

**PROPOSED.** Let T be the positive shortcut map, `m(n)=min_{i≥0}T^i(n)`, and `m_k(n)=min_{0≤i≤k}T^i(n)`. The finite population below is a full dyadic shell `X=2^k≤n<2X`. Set `p=log₃2`, `h=H₂(p)=0.949955527…`. Then

    1/X Σ_{X≤n<2X} m_k(n) ≍ X^h/(1+log X)^(3/2).                       (1)

In particular the right side bounds the true global-minimum first moment from above. The matching lower bound concerns the first k physical shortcut steps. It prevents reaching the logarithmic threshold of the [first-moment reduction](https://github.com/GettysburgResearch/collatz/blob/a2c9f95/research/fixed-floor-shells/FIRST_MOMENT.md) by any stopping rule confined to those k steps.

## Sharp native-window calculation

The parity vectors over the shell give every binary length-k word exactly once. At each t≤k with q odd inputs, `T^t(n)=3^q n/2^t+E`, `0≤E≤(3/2)^q−1≤3^q n/2^t`. The last inequality uses `n≥2^t`. Thus each value, and its running minimum, is within a factor two of its homogeneous counterpart. Set `S_t=q_t log3−t log2` and `M=min_{t≤k} S_t`, including t=0. The desired mean is comparable to `X E_(1/2) exp(M)` under independent fair bits.

Change the Bernoulli parameter to p, so S has mean zero. Put `λ=log(p/(1−p))/log3`, with `0<λ<1`, and `ρ=2^(h−1)`. On every word the fair probability divided by the p-probability equals `ρ^k exp(−λ S_k)`. Consequently the tilted integrand, after removing ρ^k, is `exp(−(1−λ)(−M)−λ(S_k−M))`.

For integers a,b≥0, the probability that `a≤−M<a+1` and `b≤S_k−M<b+1` is at most `C(a+2)(b+2)/(1+k)^(3/2)`. Split the walk into three comparable independent blocks. The first must stay above `−a−1`; the reversed final increments must have partial sums at most `b+1`. The one-sided bounds are `O((a+2)/√k)` and `O((b+2)/√k)` by the [centered walk survival estimate](https://github.com/GettysburgResearch/collatz/blob/4182367ada14d566b5cc1c86daabe6838f88da2e/research/critical-orbit-mellin/CRITICAL_MOMENT.md). Conditional on these blocks the middle sum must place S_k in a fixed interval of length two, with probability `O(1/√k)` by the binomial maximal atom and fixed lattice spacing. Sum over a,b against the two exponential factors. This proves the upper bound.

For the lower bound take exactly `⌈pk⌉` odd bits. The terminal sum is in `[0,log3]`, and this count has p-probability `≫1/√k` by Stirling. At least one cyclic rotation of each such word has all partial sums nonnegative, by cutting at a minimum. Rotational invariance conditional on the count gives probability at least `1/k` for the required sign restriction. There M=0 and `exp(−λ S_k)` is bounded below. This yields (1).

For any fixed `1<C<log₂3`, even testing `⌊Ck⌋` physical steps gives a polynomial lower bound on the shell mean:

    1/X Σ_{X≤n<2X} m_(⌊Ck⌋)(n) ≫_C X^H₂(Cp)/(1+k)^(3/2).                 (2)

Indeed choose `⌈Cpk⌉` odd bits in the first k. At least a `1/k` fraction of these words stay above their initial homogeneous value throughout that prefix. At its end the multiplier is at least `2^((C−1)k)`. Every further step at most halves the value, so the entire tested segment has minimum at least X. Stirling's formula for the number of words proves (2). No all-time survival is asserted.

## A positive ordinary sibling defect

For positive odd x let `L(x)=4x+1`, let U be the odd Syracuse map, and write `D(x)=m(L(x))−m(x)`. Since `U(L(x))=U(x)<L(x)`, one has exactly

    D(x)=m(U(x))−m(x)≥0.                                               (3)

It is positive only when x is the strict minimum of its future including time zero. On an escaping odd orbit list its successive strict suffix minima `r_0<r_1<…`, starting with the minimum of the entire orbit. Then `m(U(r_i))=r_(i+1)` and `r_(i+1)≤(3r_i+1)/2`. For every X≥r₀, telescope (3) along this chain through its last member at most X to find

    Σ_{odd x≤X} D(x) > X−r_0.                                          (4)

Distinct escaping merger components contribute disjoint such chains. Thus even `liminf_X X^(−1) Σ D(x)<1` excludes escape. More generally any finite upper limit of this normalized sum bounds the number of escaping components. The sum is a difference of two exact finite first-moment totals; density-one equality of the summands supplies no uniform-integrability conclusion for their unbounded sizes.

For B≥1 let `N(B)=#{odd x≤B: U^j(x)>B for all j≥1}`. The intervals `[x,m(Ux))` for positive defects give precisely N(B) overlaps at B. Integrating these counts through X bounds their integral above by `Σ_{x≤X}D(x)`. A divergent orbit forces an actual last exit across every sufficiently high floor. The first-landing theorem also gives `N(B)≪ B ε(B)` for B≥2, where ε(B) is the upper natural density of ordinary inputs avoiding `[1,B]` forever. Each such exit has U(x)>B and hence first valuation one; the distinct images `U(x)=(3x+1)/2` lie in `(B,(3B+1)/2]`. First landing at each image at the common threshold `(3B+1)/2` certifies disjoint sets of ordinary inputs that never meet B, of uniform lower density `≫1/B` apiece. This upper depends on the true tail, for which a sufficient rate remains missing.

## Domination by the truncated limiting minimum law

Write `p_t=d{n:m(n)=t}` for the existing natural-density law. For every nonnegative nondecreasing f on positive integers and X≥8,

    1/X Σ_{X/4<n≤X} f(m(n)) ≤ C Σ_{t≤4X+1} f(t)p_t.                   (5)

Here all positive integers in the shell are counted. For its odd members use the unit injection of [the prior finite first-landing comparison](https://rstation.ai/problems/collatz/papers/12/v1), Theorems 14 and 16: keep a unit n fixed and replace a multiple of three by `φ(n)=4n+1`. Moved values exceed X whereas unmoved ones are at most X. Since `U(φ(n))=U(n)`, we have `m(φ(n))≥m(n)` even when a density-zero starting-point minimum is lost. At threshold `L=⌊4X+1⌋`, every image receives at least `cY/L` odd first-landings in `(Y/4,Y]` for large Y. These incoming sets are disjoint. Their global minimum is the minimum of their image, and is at most L. Multiply by f and divide by Y. Taking Y→∞ bounds the left contribution from the odd starts by a constant times the right side since the truncated limiting label has finite support. Apply the same estimate to the odd parts of the states of each fixed binary valuation at scale `X/2^v`, summing the scale factors `2^(−v)`. The finitely small scaled populations are absorbed using `p_1>0` and the directly verified minimum 1 for starts at most 8. The argument works for any positive real shell scale; rounding changes only absolute constants.

The reverse bound supplied by the first-landing lower theorem is instead `≫Σ_{t∈R, Ct≤X} f(t)/t`, where R consists of unit exact minima. Equality of these two controls would require an upper estimate for their true masses. With `f(t)=t` equation (5) transfers a sufficient moment estimate to actual finite shells, but does not establish it.
