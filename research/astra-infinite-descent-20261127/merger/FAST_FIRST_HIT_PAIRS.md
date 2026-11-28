# First-hit pairs in every relative interval

**PROPOSED, with the relative-window first-hit pair theorem strictly compiled in Lean.** Let $T$ be the ordinary shortcut map. Fix a nonnegative gap $d$, a ternary precision $s$ and a relative width $\delta>0$. There exist constants $C,K,G$ depending only on $d,s,\delta$ with the following property.

For **every** natural target $y$ prime to three, every source class $c\bmod3^s$, and every real $X\ge Cy$, there is a positive integer $x\equiv c\bmod3^s$ such that
$$
X\le x\le x+d\le(1+\delta)X .
$$
Both $x$ and $x+d$ visit $y$ **for the first time at the same shortcut clock** $D$. Each uses the same number of odd departures, at most $G$. The clock satisfies
$$
\log_2((x+d)/y)\ \le\ D\ \le\ \log_2(X/y)+K.
$$
The lower inequality holds for every ordinary path from $x+d$ to $y$, since each step has output at least half its input. The upper inequality is within a fixed additive constant of this physical lower bound. In particular it is a first-hit statement even when $y=1$ or $y$ lies on a hypothetical nontrivial positive cycle.

## Moving onto an ordinary branch before the first hit

For each $y$ as above, choose $1\le e_0\le4$ such that $z=(2^{e_0}y-1)/3$ is a positive ternary unit. Directly inspecting the six unit classes modulo nine gives such a choice. The other odd predecessor $z'=64z+21=(2^{e_0+6}y-1)/3$ is also a unit.

At most one of $z,z'$ belongs to the forward orbit of $y$. In fact $T^6 z'=3z+1$ and $T^{e_0}(3z+1)=T^{e_0}z=y$. If $z,z'$ both occur after $y$, then $z$ and the distinct value $3z+1$ would be two points on the cycle of $y$ with the same $e_0$-th iterate. The map restricted to a cycle is a permutation. The formal proof uses actual clocks and proves the same injectivity directly, without deciding whether the target is periodic.

Choose the predecessor $b$ outside that forward orbit and denote its one-gap clock by $e\le10$. In its direct leg, all proper states after its first step and before its terminal are $2^j y$ with $j\ge1$. Since $b$ is also distinct from $y$, the whole leg first hits $y$ at $e$. Any path that reaches $b$ before following this leg cannot have hit $y$ earlier, since otherwise $y$ would reach $b$. Applying the fixed-gap theorem directly to $b$ yields an independent all-clock result. If its original threshold was $B$ and its odd grade was $g$, then every $D\ge B+10$ is a common **first** clock to $y$ for some pair at the prescribed gap and source class, with grade $g+1$.

## Placing the pair

Take the uniform fixed-gap threshold $H=B$ and grade $g$ at $(d,s)$ from the [fixed-gap theorem](README.md). Write $A=2^H/3^g$ and let $\eta=\min(\delta/8,1/8)$. Use the [ordinary inverse phase ladder](../escape/FAST_PREDECESSOR.md) at $b$. Its finite rotation net and first inverse exponent can be chosen for $\eta$ alone. Hence there are $M_\eta,J_\eta,\nu_\eta$ independent of $b$ such that for every $Z\ge M_\eta b$ a positive ternary unit $w\in[Z,(1+\eta)Z]$ reaches $b$ with odd grade $j\le J_\eta$ and shortcut clock
$$
t\le\log_2(w/b)+J_\eta\log_2 3+\nu_\eta.
$$
The dyadic dilation in the ladder can make $w$ even. The fixed-gap theorem accepts even targets prime to three.

Choose $Z=(1+\eta)X/A$. Apply the fixed-gap theorem at the exact clock $H$ to the **chosen** $w$. Its pair satisfies $T^H x=T^H(x+d)=w$ with odd count $g$ and source class $c$. The physical affine bounds give
$$
Aw-2^H\ \le\ x\ \le\ Aw .
$$
Thus $x\ge (1+\eta)X-2^H$ and $x+d\le(1+\eta)^2X+d$. Taking $X\ge (2^H+d)/\eta$ places the whole pair inside the requested interval. The direct predecessor has $y/2\le b\le 2^{10}y$, so $Z\ge M_\eta b$ holds as soon as $X/y\ge 2^{10}A M_\eta$. These requirements admit one $C$ independent of $y,c$.

The total first clock is $D=H+t+e$. Neither source has visited $y$ before reaching $b$, since any such visit would put $b$ on the forward orbit of $y$. The clock estimate becomes
$$
D\le\log_2(X/y)+(g+J_\eta)\log_2 3+11+2\log_2(1+\eta)+\nu_\eta .
$$
Their equal odd count is exactly $g+j+1$. The arithmetic first-hit construction, the generic attachment of an ordinary ladder path, and the two-sided affine source bounds are in [FirstArrival.lean](FirstArrival.lean). [FastPairs.lean](FastPairs.lean) checks the full unconditional relative-window assertion, both first arrivals and the common grade together. Its time conclusion uses the equivalent exponential bound $2^D y\le K_{\mathrm{Lean}}X$. The constants and witnesses vary with the fixed gap and relative width.

## Prescribing time and odd count in independent residue classes

The same written argument permits simultaneous phase constraints. Fix positive integers $M,Q$. In the main theorem one may also require $D\equiv t_0\bmod M$ and $O_D(x)=O_D(x+d)\equiv r_0\bmod Q$ for arbitrary supplied residues $t_0,r_0$. The constants then also depend on $M,Q$.

To see this, let $v_j$ be the odd unit ancestor from the phase ladder at $b$, with $j$ odd departures and cumulative inverse exponent $S_j$. For a sufficiently large lower bound on the first exponent the affine remainder gives
$$
\log_2(v_j/b)=S_j-j\log_2 3-\ell_j, \qquad 0\le\ell_j\le\nu ,
$$
where $\nu$ is as small as desired uniformly over $b,j$. At $j=0$ take $v_0=b,S_0=0,\ell_0=0$. Use only indices $j\equiv r_0-g-1\bmod Q$. The rotation step $Q\log_2 3$ is irrational modulo $M$, since $\log_2 3$ is irrational. Thus a finite initial portion of this restricted rotation is dense to any specified positive mesh size on the circle of circumference $M$. The index bound is uniform over all starting phases and all residues; there are only $Q$ starting index classes.

Choose only dyadic lifts $w=2^k v_j$ with $k+S_j\equiv t_0-H-e\bmod M$. Their log phases, relative to $b$, are
$$
\log_2(w/b)\equiv t_0-H-e-j\log_2 3-\ell_j\pmod M .
$$
In the unperturbed rotation, select a point at least $\nu$ above the lower boundary of the desired log interval and strictly below its upper boundary. A finite mesh finer than the interval width minus $\nu$ guarantees one such point. Its perturbation by $-\ell_j$ stays inside the interval. One can then add a multiple of $M$ to $k$ to put $w$ in the actual interval. The resulting $k$ is nonnegative for all sufficiently large $Z/b$, since the chosen finite set of $v_j/b$ has a uniform upper bound. The grade of the final pair is $g+j+1$, and the first clock is $H+k+S_j+e$. The prior proof of the relative position, equal first arrival and additive time bound applies with the enlarged finite index bound. This phase-congruence strengthening is a written derivation.

The [counting theorem](FAST_COUNTING.md) places many pairwise disjoint patterns in the same interval and determines the leading near-minimum-time counting exponent.

## An obstruction to uniform speed at arbitrarily fine resolution

For a fixed positive $y$ and nonnegative integer $K$, consider all positive sources $x\in[2^N y,2^{N+1}y]$, over every $N\ge0$, that reach $y$ at some $D\le N+K$. Their normalized phases $x/(2^N y)\in[1,2]$ lie in a common **compact countable** subset of the real line, so an open subinterval of $[1,2]$ misses every such phase in every octave.

Indeed $D\ge N$, and $3^g x\le2^D y$ gives $g\le K/\log_2 3$. If the odd departures are at times $t_1<\cdots<t_g<D$, the exact ordinary identity is
$$
\frac{x}{2^N y}
=2^{D-N}\left(3^{-g}-\frac1y\sum_{i=1}^g3^{-i}2^{-(D-t_i)}\right).
$$
The factors $2^{-(D-t_i)}$ belong to the compact countable set $\{0\}\cup\{2^{-j}:j\ge1\}$. For bounded $g,D-N$, the right side lies in a finite union of continuous images of finite products of that set. Each image is both compact and countable. A compact countable set cannot contain a real interval. This applies already to single sources and the ordinary target $1$. The additive allowance in the main theorem must therefore grow when the requested relative width tends to zero.

The new pair is located near a supplied height. Its first member is still a chosen integer in that interval. No estimate here forces a given individual start to reach $y$, or sends a fixed bad source below its component floor.
