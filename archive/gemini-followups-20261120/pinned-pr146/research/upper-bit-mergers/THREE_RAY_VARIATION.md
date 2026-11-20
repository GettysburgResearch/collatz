# How sparse can failed multiplication by three be?

**PROPOSED.** Use the positive shortcut map. Write $D(X)$ for the number of odd $n\le X$ for which $n$ and $3n$ lie in different merger components. If Collatz is false, then $D(X)\gg X^\eta$ for all sufficiently large $X$ for an absolute effective exponent $\eta>0$. Along the prescribed cutoffs $Cq^2$, for $q$ a convergent denominator of $\log_2 3$ and an absolute $C$, the count satisfies
$$
 \liminf_{q\to\infty}\frac{\log D(Cq^2)}{\log(Cq^2)}\ge 0.42.
$$
The last exponent uses the published Krasikov–Lagarias predecessor theorem. An elementary inverse-tree argument gives $\log 2/(2\log(64/3))$ in its place. The subsequence argument uses ordinary rational approximation. The all-scales result also uses a classical lower bound for a linear form in $\log 2$ and $\log 3$.

Let $f$ be the indicator of the component of 1. For real $R\ge 4$, set
$$
 V_R=\#\{n\in\mathbb Z:R-2\le n\le7R+10,\ f(n)\ne f(n+1)\},
 \qquad B=1+D(2R)+V_R.
$$
For absolute constants, the finite chain of comparisons gives the following estimate on this fixed-ratio interval. [Tripling defects and adjacent variation](TRIPLING_VARIATION.md)
$$
 V_R\le C(1+D(CR)). \tag{1}
$$
Below, $u$ denotes an odd positive integer coprime to three in a second component. Implicit lower-bound constants may depend on $u$ and the inverse-tree exponent.

## Mass of two components on a coarser grid

For each fixed odd positive $y$ coprime to three its component has at least $\frac12(M/y)^\alpha$ elements in $[M,2M)$ for every real $M\ge y$. Here $\alpha=\log 2/\log(64/3)$. Indeed among $1\le v\le6$ exactly three have the parity making $2^vy\equiv1\pmod3$. Exactly one of these three also gives $2^v y\equiv1\pmod9$, by the order of 4 modulo 9. The other two yield different positive odd ternary units $(2^v y-1)/3$, each reaching $y$ under the accelerated odd map and bounded above by $(64/3)y$. Iterate this branching $k=\lfloor\log_{64/3}(M/y)\rfloor$ times. The $2^k$ resulting odd starts are distinct since a start determines its next $k$ odd iterates and their valuations uniquely. Multiplying each by a suitable power of two places it in the specified interval, preserving its distinct odd part. Every component has such a unit because the odd part of $3n+1$ is coprime to three for every odd positive $n$.

The analytic argument below applies to any $0<\alpha\le1$ such that these two components each have $\gg_u M^\alpha$ elements in $[M,2M)$ for every sufficiently large $M$. In particular, any $\alpha<0.84$ is admissible. Krasikov and Lagarias prove that for each fixed positive $y$ coprime to three at least $M^{0.84}$ starts up to $M$ visit $y$ for all sufficiently large $M$. Each odd part accounts for at most $1+\log_2 M$ of those starts. Doubling representatives of the distinct odd parts into $[M,2M)$ proves the assertion for $y=1$ and $y=u$. [Krasikov and Lagarias, Theorem 6.1, 2003](https://arxiv.org/pdf/math/0205002)

On the circle $0\le t<1$ put $g(t)=f(\lfloor R2^t\rfloor)$, extended periodically, and $m=\int_0^1 g(t)\,dt$. Suppose $R$ is sufficiently large. For $M\le R$ choose an integer $l\ge0$ with $Y=R/2^l\in[M,2M)$. Apply the preceding lower bound for $y=1$ and $y=u$ at scale $Y$. Each component supplies $\gg_u M^\alpha$ grid points $2^l z\in[R,2R)$ of its own color. These belong to one common grid of spacing $2^l$. The half-open bins of that width starting at these grid points are disjoint. At most $V_R+2$ bins either extend beyond $2R$ or have a change of color between the first point and a later point of the bin. Each remaining bin has just one color and logarithmic measure $\gg 2^l/R\gg1/M$. Taking $M=C_u B^{1/\alpha}$ with a large constant ensures at least $\gg_u M^\alpha$ remaining bins of each color. If this $M>R$, then $B\gg_u R^\alpha$, which suffices for both conclusions below. Otherwise we have proved
$$
 \min(m,1-m)\gg_u B^{-(1-\alpha)/\alpha}. \tag{2}
$$

## Rotation on the logarithmic circle

Set $\gamma=\log_2 3$. The total variation of $g$ on the circle is at most $V_R+1$, including the boundary jump. Also
$$
 \|g(\cdot+\gamma)-g\|_1\ll B/R. \tag{3}
$$
To verify (3), write $x=R2^t$ and $n=\lfloor x\rfloor$. Rotation sends $x$ to $3x/2^j\in[R,2R)$ with $j=1$ or 2. The integers $3n$ and $2^j\lfloor3x/2^j\rfloor$ differ by at most four. Thus different colors there require an adjacent change within four of $3n$. Each possible change concerns only boundedly many $n$'s. The latter integer has the same color as $\lfloor3x/2^j\rfloor$ by doubling invariance. To compare $n$ and $3n$, strip their common power of two. Each odd defect has only boundedly many representatives among the integers in $[R-1,2R]$, since they are its successive doublings. Altogether the number of bad unit intervals for $x$ is $O(B)$, each of logarithmic measure $O(1/R)$.

Suppose $p/q$ is a reduced fraction with $|\gamma-p/q|\le 1/q^2$. For any initial phase, the first $q$ iterates under rotation by $\gamma$ each lie within $1/q$ of the corresponding iterate under rotation by $p/q$. The latter points form a translated grid. Its interval discrepancy is $O(1/q)$, and expanding or shrinking an interval by $1/q$ at either end preserves this order. Summing the signed jumps of $g$ against interval discrepancies gives
$$
 \sup_t\left|q^{-1}\sum_{i=0}^{q-1}g(t+i\gamma)-m\right|\ll B/q.
$$
Telescoping (3) bounds the $L^1$ distance from $g$ to this orbit average by $O(qB/R)$. Since $g$ takes values in $\{0,1\}$, its distance from its mean is $2m(1-m)\ge\min(m,1-m)$. Together with (2), this gives
$$
 B\gg_u (q/R+1/q)^{-\alpha}. \tag{4}
$$
If the coarse grid had $M>R$, the same conclusion follows from $B\gg_u R^\alpha$.

## Consequences at two kinds of scale

Take any convergent denominator $q$ of the irrational $\log_2 3$ and $R=q^2$. By (1) and (4),
$$
 1+D(Cq^2)\gg_u q^\alpha.
$$
There are arbitrarily large such $q$. The elementary value of $\alpha$ gives a lower bound of approximately $0.113$ for the limsup exponent of $D$. Taking the supremum over $\alpha<0.84$ gives $0.42$ using Theorem 6.1 above. If one imports the newer source-qualified predecessor estimate $\pi_y(M)\gg_y M^{0.901}$, the same argument gives $0.4505$. [Repository audit of the newer predecessor estimate](../external/mazur-2026/predecessor-x090.md)

For all large $R$, choose an effective $\kappa\ge1$ with $\|h\log_2 3\|_{\mathbb R/\mathbb Z}\gg h^{-\kappa}$ for every positive integer $h$. This follows from the theorem on linear forms in logarithms applied to $h\log 3-p\log 2$ for $p$ nearest to $h\log_2 3$. Unique factorization makes the form nonzero. [Baker and Wüstholz, 1993](https://doi.org/10.1515/crll.1993.442.19)

By Dirichlet approximation with $L=\lfloor R^{\kappa/(\kappa+1)}\rfloor$ there is a reduced $p/q$ with $1\le q\le L$ and $|q\gamma-p|\le1/L$. The linear-form bound gives $q\gg L^{1/\kappa}$, while $q\le L$ gives $|\gamma-p/q|\le 1/q^2$. Thus $q/R+1/q\ll R^{-1/(\kappa+1)}$. Substituting in (4) and using (1) proves
$$
 D(X)\gg_u X^{\alpha/(\kappa+1)}
$$
for every sufficiently large $X$, after rescaling $X=CR$.

An explicit consequence with the published predecessor bound is $D(X)\gg_u X^{0.164}$ at every sufficiently large cutoff. Indeed Theorem 1 of Wu and Wang bounds $|b_0+b_1\log 2+b_2\log 3|$ below by $H^{-4.1163051-\epsilon}$ for $H=\max(|b_1|,|b_2|)$ sufficiently large. Take $(b_0,b_1,b_2)=(0,-p,h)$, so any $\kappa>4.1163051$ is allowed. For instance $\alpha=0.8399$ and $\kappa=4.117$ give $\alpha/(\kappa+1)>0.164$. [Wu and Wang, *On the irrationality measure of log 3*, Theorem 1, 2014](https://doi.org/10.1016/j.jnt.2014.03.007)

A distinct dyadic-limit proof gives $D(X)\ge cX^{0.84}$ along arbitrarily large cutoffs, without prescribing them as $Cq^2$. [Dyadic limit and predecessor count](THREE_RAY_DENSITY.md)

This every-scale argument bounds the cumulative count up to $X$. A power-saving upper bound below this exponent on an unbounded sequence of cutoffs would preclude a second component. Such an upper bound remains open.
