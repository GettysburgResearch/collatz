# Full local dimension and a positive Hausdorff gauge inside escaping slope levels

Let $X$ be the closed set of odd $2$-adic sources whose synchronized affine maps for $(s,3s)$ never agree identically. The [dyadic closure theorem](PRIMITIVE_SPARSE_PAIR_CLOSURES.md) identifies it using sparse, positive periodic pairs. Write $j_t=1+h_t-g_t$ for the signed upper-minus-lower affine exponent, where $g_t,h_t$ are the actual odd grades at native date $t$.

**Proposed lower bound.** Every dyadic cylinder meeting $X$ contains a subset on which the two actual values never agree, $j_t\to+\infty$, and
$$
     \mathcal H^\psi>0,\qquad
     \psi(2^{-n})=2^{-n}\sqrt{n\log\log n}\quad(n\text{ sufficiently large}).       \tag{1}
$$
On each such cylinder the Hausdorff dimension of this subset is one. Its Hausdorff measure is infinite for every gauge $2^{-n}n^c$, $c>1/2$. At the critical gauge $2^{-n}\sqrt n$, the [companion upper theorem](../literature/CRITICAL_MERGER_HAUSDORFF.md) proves zero measure even for the entire $X$, using David Leen's October 9 results. These bounds leave a factor $\sqrt{\log\log n}$ between the two gauges.

## A directly constructed measure on actual source cylinders

Given a cylinder meeting $X$, the [forward routing proof](ADJACENT_CYCLE_CLOSURE.md) extends it to an original-order state $(1,1)$, first returning to translation one and then applying U. Here $(j,a)$ denotes $B=3^j A-a$. From now on $j$ will stay positive. At each native step the two child cylinders prescribe the lower parity. If $a$ is even their paired letters are common and the exponent level stays fixed; give each child weight $1/2$. If $a$ is odd the two choices move the level up or down by one; from positive $j$ give these choices respective probabilities $(j+1)/(2j)$ and $(j-1)/(2j)$. The latter is zero at $j=1$. These locally consistent weights define a probability $\mu$ on the refined source cylinder. Measured from the end of the fixed routing prefix, every positive-mass length-$n$ cylinder has exactly
$$
                             \mu([w])=2^{-n}j_n .                           \tag{2}
$$
Indeed each one-step probability is half the ratio of new level to old including at common steps, and the initial level is one. This measure uses the positive-level walk killed at first level zero; it is distinct from the full-state capacity transform used in the companion upper theorem.

No atom can have positive mass since $j_n\le n+1$. The subset which ever has a synchronized value coincidence is countable under this construction: at every positive level $B=A$ determines at most one base in the prefix's affine cylinder. The fixed initial routing segment has no identically equal pair either, so contributes at most finitely many singletons. Similarly, from any positive level an indefinitely common parity tail forces $A=B$, because equal parity prefixes of every length imply equality modulo every power of two. Thus $\mu$-almost every path has infinitely many mixed letters.

At successive mixed letters the level process is the nearest-neighbor chain with the displayed transition probabilities. Indeed after any history the event of an eventual next mixed step has conditional probability one; summing over the countably many possible full histories up to just before that step leaves the same two probabilities at its current level. This chain tends to infinity almost surely. It reaches every fixed $H$: from below $H$ each successive group of $H$ direction choices has conditional chance at least $2^{-H}$ to reach it. Above any fixed $m\ge1$, $1/j$ is harmonic until return to $m$. By stopping this nonnegative martingale, the probability of ever hitting $m$ from $H>m$ is at most $m/H$. Applying this after first reaching $H$ and letting $H\to\infty$ excludes infinitely many visits to $m$. The same conclusion holds in native time since there are infinitely many mixed steps.

## A bound uniform in the holding times

For $\theta>0$ put $f_\theta(j)=\sinh(\theta j)/j$ for $j\ge1$. It increases with $j$. At a mixed step its conditional expectation equals $\cosh(\theta) f_\theta(j)$ by the addition identity for $\sinh$, also at $j=1$; at a common step it stays fixed. Thus $f_\theta(j_t)/(\cosh\theta)^t$ is a nonnegative supermartingale in the **native** clock. Stopping at the first level at least $a$, up to $n$, gives
$$
 \mu\{\max_{t\le n}j_t\ge a\}\le (\cosh\theta)^n\frac{a\sinh\theta}{\sinh(a\theta)}.
$$
For $\sqrt n\le a\le n$, take $\theta=a/n$. The inequalities $\cosh x\le e^{x^2/2}$, $\sinh x\le2x$ on $[0,1]$, and $\sinh y\ge e^y/3$ for $y\ge1$ give the upper bound $6(a^2/n)e^{-a^2/(2n)}$. Apply it at $n=2^k$, $a=\lceil 3\sqrt{2^k\log k}\rceil$. The probabilities sum over $k$, so Borel–Cantelli and passage between dyadic times give
$$
                           j_t=O(\sqrt{t\log\log t})\qquad\mu\text{-almost surely}.
$$
On a positive-measure Borel subset this bound holds with one uniform constant for all sufficiently large times, absorbing the finite initial segment into that constant. Remove the null exceptions identified above. Equation (2) bounds the restricted cylinder masses by a constant times their gauge in (1); the fixed preceding prefix changes only that constant. In the dyadic ultrametric arbitrary small sets lie in a cylinder of the same diameter. The mass distribution bound proves (1). Dividing the larger gauge $2^{-n}n^c$ by $\psi(2^{-n})$ gives a ratio tending to infinity for $c>1/2$, proving the asserted infinite measures and dimensions.

Leen already proved that counted synchronous coalescence occurs Haar-almost surely with a fixed-state square-root survival tail. A direct earlier application covers the exact odd $(s,3s)$ pair. The measure in (2) is deliberately singular with respect to Haar. The positive full-dimensional subset in (1) is compatible with that prior probability-one merger theorem. [Leen, *Exact rates in Collatz synchronization*, Theorem 7.2](https://doi.org/10.5281/zenodo.23268751) · [November 4 same-pair application](https://rstation.ai/r/collatz/posts/2?after=buQ2uW_A5TjNQd5h)
