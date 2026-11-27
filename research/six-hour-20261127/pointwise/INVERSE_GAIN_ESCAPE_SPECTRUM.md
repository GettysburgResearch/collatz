# The positive limit values of the unrestricted inverse gain

For every positive odd integer $z$, let $G(z)$ be the largest homogeneous gain $3^k/2^h$ of any actual positive odd Collatz path ending at $z$. The visitor may start anywhere and use any finite odd clock $k$ and total valuation $h$. The empty path is included. Define $Q(z)=G(z)/z$. A component is an equivalence class of positive odd integers under eventual forward meeting.

**Theorem.** For each escaping component $C$ let $P_C$ be its least corrected height as defined below. For each real $c>0$, the entire set of positive odd $z$ with $Q(z)\ge c$ differs by a finite set from a disjoint union of one ordinary forward tail in each escaping component satisfying $P_C\le1/c$. There are finitely many such components. The statement also holds with $Q(z)>c$, with the same inclusive cutoff on $P_C$.

Consequently the positive accumulation values of $Q(z)$ as $z\to\infty$ are exactly the numbers $1/P_C$. This set is locally finite away from zero. The value zero itself is always a limit along positive odd multiples of three. Put $L=0$ when all positive orbits are bounded and $L=1/\min_C P_C$ otherwise. Then

$$
\lim_{Y\to\infty}\ \max_{Y\le z<3Y/2+1,\ z\text{ odd}} Q(z)=L .
$$

In particular, even the liminf of the dyadic-octave maxima is zero exactly when all ordinary orbits are bounded. This criterion leaves possible nontrivial cycles separate.

**Inputs and priority.** Weaver's Paper 177 defines and bounds the maximum inverse gain. Paper 178 treats its maximizing clock, physical minimum-source law and unrestricted visitor times. Weaver's Paper 207 explicitly constructs the corrected height on an escaping component, proves the component minimum exists and stabilizes its equal-gain source sets on the deadline copies. The statements here combine these ingredients to describe the complete positive-integer superlevel sets and limit spectrum. No priority for the gain, corrected height, minimizer or finite two-place coalescence obstruction is claimed. The short packing proof below suffices for all pointwise assertions.

- [Weaver, Paper 177/v1, §7](https://rstation.ai/problems/collatz/papers/177/v1)
- [Weaver, Paper 178/v1, §§1–2 and 7](https://rstation.ai/problems/collatz/papers/178/v1)
- [Weaver, Paper 207/v1, corrected heights and component representatives](https://rstation.ai/problems/collatz/papers/207/v1)

### Finite attainment and reciprocal packing

Write $U(x)=(3x+1)/2^{e(x)}$. A path from $v$ to $z$ of gain $g$ obeys $z\ge gv$, strictly for nonempty paths. Any path of gain at least one therefore starts at $v\le z$. For each of the finitely many such positive odd starts, subsequent visits to $z$ after its first visit require a positive cycle lap at $z$. A full lap has gain $\mu<1$, since the positive affine offset gives $z=\mu z+b$, $b>0$. Thus $G(z)$ is attained, and every maximizing visitor satisfies $v\le1/Q(z)$. Equality of two maximal gains forces equality of both the odd clock and total valuation by unique factorization.

For completeness, in the shortcut map $T(n)=(3n+1)/2$ at odd $n$, and $n/2$ at even $n$, an injective infinite path has at most $O(Y^{1-\delta})$ states up to $Y$, with absolute $\delta>0$. Use $d=\lfloor\log_2Y\rfloor$. Each parity word of length $d$ has one class modulo $2^d$ and hence at most three starts in $[1,Y]$. Words with more than $3d/5$ odd letters number $O(2^{H_2(3/5)d})$ by the binomial bound. All other words send any such start to at most $3^{3d/5}Y/2^d+(3/2)^d$, by the affine formula and the maximum all-odd affine offset. Their endpoints are distinct along an injective path. Both $H_2(3/5)$ and $(3/5)\log_2 3$ are strictly below one. Dyadic summation gives a uniform finite bound on the sum of reciprocal heights on an escaping path. The positive odd states of an escaping accelerated path occur on an injective shortcut path as well.

### Stabilization on an escaping path

For an escaping odd $v$, let

$$
\Phi(v)=v\prod_{j=0}^{\infty}\left(1+\frac1{3U^j(v)}\right).
$$

Packing makes this finite, and $\Phi(v)>v$. Factoring out the first term gives $\Phi(Uv)=3\Phi(v)/2^{e(v)}$. The minimum $P_C=\min_{v\in C}\Phi(v)$ exists since all competitors below any one value have bounded positive integer height. Choose an attaining $b$.

Fix $x\in C$ and put $x_t=U^t(x)$, $g_t=3^t/2^{\sum_{j<t}e(x_j)}$, $g_0=1$. Every actual ancestor $v$ of $x_t$ belongs to $C$, and the gain of its path is exactly $\Phi(x_t)/\Phi(v)$. The ancestor sets increase with $t$. Once the path from $b$ first meets the path from $x$, the minimum of $\Phi$ over the ancestor set equals $P_C$ for all later $t$. Hence

$$
G(x_t)=\frac{\Phi(x_t)}{P_C},\qquad
\frac{G(x_t)}{g_t}=\frac{\Phi(x)}{P_C},\qquad
Q(x_t)=\frac1{P_C}\prod_{j\ge t}\left(1+\frac1{3x_j}\right)
$$

on the whole remaining tail. In particular $Q(x_t)$ decreases strictly to $1/P_C$ from above, resolving the threshold equality case. From $b$ itself all three identities hold from date zero.

At any ordinary edge the Bellman inequality $G(Ux)\ge3G(x)/2^{e(x)}$ follows by continuing a maximizing visitor. Every escaping path has only finitely many strict inequalities. They are strict on at least one edge of every positive cycle lap by multiplication of the inequalities. Thus any positive odd path escapes if and only if it makes only finitely many strict Bellman inequalities. More quantitatively there are at most as many strict edges on an escape from $x$ as positive odd integers at most $\Phi(x)$. Each has to introduce a strictly smaller ancestor minimum, and its attaining visitor has physical height at most $\Phi(x)$. The uniform packing bound gives $\Phi(x)=O(x)$.

### The entire superlevel set

If $Q(z)\ge c$, choose a maximizing visitor $v\le1/c$. Hence every such $z$ is on the union of the complete forward orbits of the finitely many odd $v\le1/c$. Bounded orbits add a finite set. Escaping orbits in the same component coincide after deleting finite prefixes. On each remaining ray the preceding strict limit includes its full tail exactly when $P_C\le1/c$, for either choice of strict or weak superlevel set. Conversely each component meeting that inequality has a minimizer $b< P_C\le1/c$, so it is represented in the finite list. This proves the superlevel assertion. It gives the limit spectrum by applying the finite-ray assertion on each fixed positive superlevel, and by traversing every minimizing ray. Local finiteness follows from the same finite source list.

If there is at least one escaping component, the smallest $P_C$ exists by physical boundedness of all minimizers below any one candidate. Its ray crosses each real height $Y$ eventually. At its first crossing from an odd $x<Y$, the odd successor satisfies $Ux\le(3x+1)/2<3Y/2+1$. The crossed states therefore provide the lower bound $L$ for the limit of the interval maxima. The upper bound is the global limsup supplied by the spectrum and the bound $Q\le1$. If all paths are bounded, every fixed positive superlevel is finite, so the interval maxima tend to zero. For an odd multiple of three there is no nonempty odd inverse path, giving $Q(z)=1/z$.

### Exact finite superlevels

For an integer $B\ge1$, it suffices to visit the paths from the odd starts $v\le B$ when computing the complete set $Q(z)\ge1/B$. Track $g_t/z_t$, which strictly decreases on each forward path because $z_{t+1}/g_{t+1}=z_t/g_t+1/(3g_t)$. Each start may stop at its first subthreshold value, or at a repeated state since future visits only reduce the gain. If each of these finitely many searches stops, their union is the exact global set, including targets of arbitrarily great possible height. Conversely a single nonterminating search must be an escaping path and must have $\Phi(v)\le B$. This procedure supplies no termination theorem uniform in $B$.

The accompanying exact census uses this decreasing threshold independently of any conjecture about the remaining starts. It also compares to a second computation from complete trajectories through their first occurrence of one and checks the exact gains at ordinary targets. The mathematical criterion still requires control of all finite source cutoffs or all large octaves.

For $B=65,535$ the complete superlevel consists of 52,048 distinct positive odd targets, of which 19,280 exceed $B$. Its largest member is 197,759,717, with maximizing source 60,975. The independent complete trajectory method made 1,228,333 visits from 32,768 positive odd starts, counting endpoints. The code computes the same complete set at four smaller cutoffs.
