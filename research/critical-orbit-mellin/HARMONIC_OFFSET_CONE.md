# A positive real-offset test for ordinary escape

**PROPOSED, source-qualified.** Let $U$ be the ordinary accelerated odd map, and keep $g_Q(t)=\sum_{U^Qx=t}J_w$ and the normalization of [the finite harmonic criterion](../unsafe-return-weights/SIGNED_MASS.md), commit `1602f45`. Write $t=J_w x+F_w$ for the **real** affine offset of a length-$Q$ odd word. For $0<\theta<1$ define
$$
 B_Q(\theta)=\sum_{\substack{t\le2\cdot3^Q\\t\ \mathrm{odd}}}\frac1t
 \sum_{\substack{U^Qx=t,\ \mathrm{path\ pairwise\ distinct}\\ F_w\ge\theta t}}J_w.
$$
Every positive orbit is eventually periodic if and only if $\liminf_{Q\to\infty}B_Q(\theta)/Q=0$ for every fixed $\theta>0$. In the eventual-periodic direction $B_Q(\theta)$ is bounded in $Q$ for each $\theta$. One may equivalently test $\theta=1/k$ for integers $k\ge2$. The test has positive terms and no baseline subtraction. It discards words near the zero-relative-offset part of the joint law. Every retained target satisfies $t\le((3/2)^Q-1)/\theta$, by the maximal real offset for positive valuations. At fixed $Q,t$ the legal-word sum is interpreted as a nonnegative convergent series, as for $g_Q(t)$ itself.

The exact product identity gives
$$
 F_w/t=1-\prod_{i<Q}(1+1/(3U^i x))^{-1}.
$$
On a simple path avoiding all states $\le R$, the right side is at most $\sum_{i<Q}1/(3U^i x)$, which tends to zero uniformly as $R\to\infty$ by [the simple-segment reciprocal bound](CRITICAL_MOMENT.md). Fixing $\theta$ therefore forces each marked path to visit a bounded state $s\le R(\theta)$. If all orbits are eventually periodic, the targets then belong to the finite union of forward orbits of those states. The pointwise uniform bounds on $g_Q(t)$ at each of these finitely many ordinary targets give $B_Q(\theta)=O_\theta(1)$. Removing repeated visits in the definition prevents long runs around potentially large periodic cycles from mimicking a large simple-path distortion. [Ordinary finite-height bounds and external inputs](../native-pressure-20261118/ORDINARY-DENSITIES.md)

Conversely take a divergent odd ordinary unit $n$, available upon advancing at most one odd step on any nonperiodic orbit. Put $y_j=U^j(n)$ and $D_j=J(n,j)$. Along the path from $n$ to $y_j$, the real offset is at least $y_j/(3n+1)$ for $j\ge1$ by the first product factor. All longer words through $n$ have at least this offset by positivity of composition. Their paths are necessarily simple since they belong to a nonperiodic component. The distinct $y_j$, $1\le j\le Q$, lie below $2\cdot3^Q$ for all sufficiently large $Q$ because $y_j\le(n+1)(3/2)^j$. Consequently
$$
 B_Q(1/(3n+1))\ \ge\ \sum_{j=1}^Q\frac{D_j}{y_j}g_{Q-j}(n).
$$
Here $D_j/y_j\to r(n)/n>0$ by the reciprocal-product bound. The bounded sequence $g_k(n)$ has a strictly positive Cesàro mean $b(n)$ by the ordinary canonical trace. The normalized right side tends to $r(n)b(n)/n$, proving the equivalence. Thus any nonperiodic component puts linear harmonic mass on words whose real offset is a fixed positive fraction of the physical target. Bounded-real regularity alone misses exactly these inherited low-ancestor contributions. [Valbuena, canonical Cesàro trace](https://doi.org/10.5281/zenodo.23025885)

## Why Haar bounds alone do not settle the finite test

There are positive mean-one densities $f$ on $\mathbb Z_3$ with every finite moment, exponentially accurate $L^1$ martingale truncations $f_Q$, and
$$
 \liminf_Q\frac1Q\sum_{\substack{t\le2\cdot3^Q\\ t\ \rm odd}}f_Q(t)/t>\tfrac12\log3 .
$$
Fix an integer $K\ge3$. For each sufficiently large $j$ choose an odd $t_j$ in $[j^2,j^2+j]$ outside all previously chosen cylinders modulo $3^{Ki}$. Excluding earlier cylinders with small moduli removes $O(j\sum_{i\ge j_0}3^{-Ki})+O(\log j)$ integers: any earlier modulus $3^{Ki}>2j^2$ excludes none, as all earlier $t_i<t_j$ and are already below $j^2$. There are $O(\log j)$ remaining moduli. Their total density can be made arbitrarily small by taking $j_0$ large. Hence the new odd point exists. The cylinders $C_j=t_j+3^{Kj}\mathbb Z_3$ are disjoint. Put $d=\sum_{j\ge j_0}t_j3^{-Kj}$ and
$$
 f=1-d+\sum_{j\ge j_0}t_j{\bf1}_{C_j}.
$$
Its finite moments follow from $t_j=O(j^2)$ and exponential cylinder decay, and $\|f-f_Q\|_1\le2\sum_{Kj>Q}t_j3^{-Kj}\ll Q^2 3^{-Q}$. Every $j\le Q/K$ contributes its height $t_j$ at the sampled point $t_j$, giving a slope at least $(1-d)\log3/2+1/K>\log3/2$ for large $j_0$. This countermodel does not satisfy the Syracuse transfer; it isolates the need for arithmetic control of the sampled representatives. In particular arbitrarily good bounded-real $L^p$ estimates in isolation do not provide such control. The actual offset-cone bound $B_Q(\theta)=o(Q)$ on all ordinary targets remains open.
