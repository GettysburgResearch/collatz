# Physical escape mass through finite integer gates

**Status.** Proposed theorem with proof and exact finite controls. The sorted masses exiting a finite interval converge in $\ell^1$ to one atom per escaping component of the actual positive-integer graph. The augmented total decreases to their sum. Every finite observable uses ordinary integer arithmetic at positive integer exponents. The limit may vanish and no effective rate is established.

Write $T(x)=x/2$ for even $x$ and $(3x+1)/2$ otherwise, $c(x)=1/2$ or $3/2$ respectively, and $C_k(x)=\prod_{i<k}c(T^ix)$. The empty product is one. If $T^kx=y$, the retained fraction of source weight is
$$
 d_s(x,k)=\left(\frac{xC_k(x)}{y}\right)^s
 =\prod_{i<k}\left(1+\frac{\mathbf1_{T^ix\ {\rm odd}}}{3T^ix}\right)^{-s}\le1.
$$
It multiplies exactly across successive trajectory segments. Fix $s>1$.

## OP-G1. Finite computation and monotone total

For integer $X\ge2$, put $\tau_X(x)=\inf\{k\ge0:T^kx\ge X\}$ and $g_X(x)=T^{\tau_X(x)}x$ when the hitting time is finite. Define the finitely supported nonnegative vector
$$
 J_{s,X}(y)=
 \sum_{\substack{x<X,\ \tau_X(x)<\infty\\g_X(x)=y}}
                 x^{-s}d_s(x,\tau_X(x)).
$$
All starts here are positive. A search terminates by exit or repetition of a vertex below $X$ after at most $X-1$ steps. Its support is exactly
$$
 \{y\in\mathbb Z:\ X\le y\le (3(X-1)+1)/2,\quad y\equiv2\bmod3\}.
$$
An exit from below must use an odd predecessor. Conversely, each displayed $y$ has the positive odd predecessor $z=(2y-1)/3<X$, which itself exits in one step. Each gate therefore has at least $(3/(2y))^s$ of mass. In particular the unaugmented total is always at least of order $X^{1-s}$ for large $X$.

There is an exact substochastic transport from cutoff $X$ to $Y>X$. Put at each old gate $y$ its mass $J_{s,X}(y)$ and add fresh weights $x^{-s}$ for $X\le x<Y$. For each of these labeled weights at $z$, erase it if $\tau_Y(z)=\infty$. Otherwise move it to $g_Y(z)$ multiplied by $d_s(z,\tau_Y(z))$. A weight already at or beyond $Y$ stays in place. Adding arriving weights gives exactly $J_{s,Y}$. Indeed for every old source that ever reaches $Y$, the first hit at $X$ occurs no later and the two intervening retentions multiply. A source killed before $X$ cannot reach $Y$.

Consequently the augmented total
$$
 A_s(X)=\|J_{s,X}\|_1+\sum_{x\ge X}x^{-s}
$$
is nonincreasing and lies in $[0,\zeta(s)]$. Sourcewise, its summand is $x^{-s}$ above the cutoff and the surviving retained weight below it, or zero upon failure to exit. It decreases as $X$ increases. Each $J_{s,X}$ is rational at integral $s>1$, and $A_s(X)$ is a computable real whenever $s>1$ is fixed and computable, using the integral test for the untouched tail.

## OP-G2. Atomic component limit

Every forward component is eventually cyclic or has coalescent, simple trajectories tending to infinity. These facts follow from functional-graph connectivity and finiteness of every bounded integer interval. In an escaping component $D$, let
$$
 L(x)=x\prod_{i\ge0}\left(1+\frac{\mathbf1_{T^ix\ {\rm odd}}}{3T^ix}\right),\qquad
 Z_D(s)=\sum_{x\in D}L(x)^{-s}.
$$
The simple-path reciprocal estimate in [OP-D1](HYBRID_DESCENT.md) gives $x\le L(x)\le Kx$ with an absolute $K$. Thus $0<Z_D(s)$ for each such $D$ and $\sum_D Z_D(s)\le\zeta(s)$. Choose one representative $a_D$ per escaping component, for instance its least integer. Define the moving vector $M_X=\sum_D Z_D(s)\delta_{g_X(a_D)}$ on all positive integers, taking an immediate hit when $a_D\ge X$. These gates are distinct across components. Then
$$
 \lim_{X\to\infty}\|J_{s,X}-M_X\|_1=0,\qquad
 \lim_{X\to\infty}A_s(X)=\sum_D Z_D(s).
$$

For proof decompose both vectors by ordinary starting point $x$. For a fixed escaping $x$, its trajectory and that of $a_D$ meet after finite prefixes. Once $X$ exceeds every height of these prefixes, both first-exit gates coincide. The hitting time from $x$ tends to infinity with $X$, so the weight retained from $x$ tends to $L(x)^{-s}$. For a fixed periodic-basin start the actual contribution eventually vanishes once $X$ exceeds the largest point it ever visits. Each sourcewise difference has $\ell^1$ norm at most $2x^{-s}$. For any cutoff in source space $H$, all differences from $x>H$ have total norm bounded by $2\sum_{x>H}x^{-s}\le2H^{1-s}/(s-1)$. Take $X\to\infty$ for the finitely many smaller sources and then $H\to\infty$. This also handles infinitely many components whose representatives may at first be beyond the boundary shell. The augmentation tail tends to zero, giving the second formula.

Let $\downarrow$ denote rearrangement in decreasing order, with zero padding. Then
$$
 J_{s,X}^{\downarrow}\longrightarrow (Z_D(s))_D^{\downarrow}
 \quad\text{in }\ell^1.
$$
Indeed rearrangement contracts $\ell^1$ distance. At each positive level $t$ the rearranged exceedance sets are initial segments, whose symmetric difference is the absolute difference of their sizes. Integrating in $t$ bounds the rearranged distance by the unrearranged one. The multiset of nonzero masses of $M_X$ is fixed. It follows that the largest gate mass has a limit, positive exactly when there is positive escape, and each fixed higher order statistic has its own component-mass limit. For each integer $k\ge1$, the collision sum $\sum_yJ_{s,X}(y)^k$ tends to $\sum_DZ_D(s)^k$, by the Lipschitz bound for $t^k$ on $[0,\zeta(s)]$.

## Arithmetic deflation that finite data justify

For a finite set $V$ of starts whose full forward orbits have been certified finite, and $X$ exceeding their largest excursion, one has
$$
 A_s(X)\le \sum_{x\notin V}x^{-s}.
$$
For instance, if all starts through $H$ have been certified and their largest excursion is below $X$, this gives $A_s(X)\le H^{1-s}/(s-1)$. More generally the same certificate can omit a start's descendants already known to merge into a verified finite orbit. Finite-interval concentration can rise before it vanishes: for $s=2$ the computed largest gate carries over $0.008$ at $X=3000$, and below $0.000034$ at $X=10000$. Monotonicity belongs to the augmented total. A finite upper bound on a positive limit does not exclude additional escaping sources of still smaller weight. The theorem itself neither produces an infinite sequence of verified cutoffs with vanishing maximum nor excludes positive cycles.

## Replay

Run `python gate_controls.py` in this directory. It evaluates $s=2$ for nine cutoffs through $100000$, independently follows every initial path at the four smallest cutoffs through $300$ and again at $1000$, and checks the full transport identity between successive cutoffs through $1000$. It verifies exact gate support and the augmented monotonicity bounds throughout. Every gate weight is a reduced rational. The receipt records the SHA-256 of the complete binary-encoded weight vector, the integer floor of $10^{15}$ times its leading entries, and the number of exiting sources. At $X=100000$ there are $16667$ gates, $41038$ exiting sources, and the largest weight is at $125252$ with $1033$ contributing starts. [Exact computation](gate_controls.py) · [Receipt](GATE_CONTROLS.json)
