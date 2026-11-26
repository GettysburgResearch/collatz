# One-edge near-invariants inside the basin of 1 and the exact rooted weight criterion

**PROPOSED written results.** All vertices are positive ordinary integers for the shortcut map $T$. Its basin of 1 is denoted by $G$. The construction below uses only explicitly certified convergent paths.

## Infinite-dimensional obstruction for every decreasing summable height weight

Let $w:\mathbb N_{>0}\to(0,\infty)$ be nonincreasing with $\sum w<\infty$, and let $1\le p<\infty$. Write $Rf(x)=f(x)-f(Tx)$ for the edge residual, defined wherever $f$ and $f\circ T$ belong to $\ell^p(w)$. In particular every bounded label is in the domain. For general monotone $w$ we make no assumption that composition by $T$ is bounded on the entire space.

**Theorem O5.** For every integer $k\ge2$ and every finite set of anchors, there is an infinite family of pairwise disjoint subsets of $G$, avoiding those anchors, whose indicator functions satisfy both of these properties.

1. Each indicator has exact doubling invariance and a nonzero residual at exactly one odd input.
2. Every finite linear combination, and every vector in their closed linear span, obeys
$$
                 \|Rf\|_{p,w}\le k^{-1/p}\|f\|_{p,w}.              \tag{5}
$$
For $w(n)=n^{-\sigma}$, $\sigma>1$, the upper bound improves to $(2/3)^{(k-1)\sigma/p}$. Thus no positive uniform lower estimate for $R$ holds even on exactly doubling-invariant labels supported in $G$ and vanishing at any specified finite set.

Take arbitrarily large positive odd multiples $L$ of $3^{k-1}$, so that $3^k\mid 2^L+1$. For this divisibility, $2^{3^j}+1$ is divisible by $3^{j+1}$ by induction using $X^3+1=(X+1)(X^2-X+1)$ with $X\equiv-1\bmod3$. Passing to any odd multiple of the exponent preserves the divisibility. Write $y=(2^L+1)/3^k$. Starting at $n=2^k y-1$, the first $k$ steps are
$$
                  x_j=3^j 2^{k-j}y-1,\qquad 0\le j\le k.
$$
Every preterminal $x_j$ is odd, the steps are strictly increasing, and $x_k=2^L$. Let
$$
              a=x_{k-1}=2\cdot3^{k-1}y-1=(2^{L+1}-1)/3.
$$
Choose $L$ large enough for $a>1$. The odd vertex $a$ maps directly to $2^L$ and then follows powers of two down to 1 and its cycle. Therefore its predecessor cone $D_a=\{x:T^j x=a\text{ for some }j\ge0\}$ is contained in $G$. The cones for different chosen exponents $L$ are disjoint. Indeed after its first step the orbit from $a$ visits only powers of two, including 1, so it cannot visit any other chosen odd target $>1$. A point whose orbit met two targets would put one target on the other target's orbit. In particular every finite list of anchors requires dropping only finitely many cones, whether or not the anchors are known to converge.

For $F_a=1_{D_a}$ the indicator at $x$ agrees with that at $Tx$ if $x\ne a$, and the residual equals 1 at $a$. Thus the full even equation holds. The $k$ distinct points $x_0,\ldots,x_{k-1}=a$ lie in $D_a$ and are all at most $a$. Monotonicity gives $w(D_a)\ge k w(a)$. For the power weight the single point $n$ already gives
$$
  \frac{w(a)}{w(D_a)}\le (n/a)^\sigma
  \le (2/3)^{(k-1)\sigma}.
$$
For the final inequality use $(n+1)/(a+1)=(2/3)^{k-1}$ and $0<n\le a$. The residual supports and the cone supports are disjoint across the family. Taking $p$th powers and summing proves (5) on finite combinations. A vector in the closed span has one coefficient per cone, with $\sum_a |c_a|^p w(D_a)<\infty$. Its composition and residual are defined pointwise, and the residual has coefficient $c_a$ at $a$ only. This proves (5) for the full closed span.

For $\sigma>1$ the composition operator $Vf=f\circ T$ is bounded on $\ell^p(n^{-\sigma})$ by the finite indegree and uniformly bounded weight ratios on an edge. In the Hilbert case let $H_0$ denote the closed subspace of exactly doubling-invariant vectors supported in $G$ and zero at the chosen finite anchors. Treat $R=(I-V)|_{H_0}$ as a bounded map **into the full Hilbert space**. For each $k$, (5) gives infinitely many orthonormal vectors of small residual. Choosing one at successive $k$, orthogonal to earlier vectors (within the indicated infinite-dimensional subspaces), gives a weakly null singular sequence for $R^*R$ at zero. In particular $0$ lies in its essential spectrum, even when the anchors include 1, in which case $R$ is injective. In general $V$ need not preserve $H_0$.

PR193's first-visit mark at 5 supplies one actual one-edge defect for a Fourier norm argument. The family above lies wholly in $G$, has arbitrary finite anchors, and yields the quantitative weighted Hilbert and Banach space obstruction. PR200's approximate-coloring example serves a different purpose and allows many sparse errors. [PR193, fixed head](https://github.com/GettysburgResearch/collatz/blob/4cc06e7d8fdec923eed73a26b1e9d680c9f701d1/research/astra-closure-20261125/global/README.md) · [PR200, approximate coloring](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/pointwise-fibers/APPROXIMATE_COLORING.md)

## Which weights can give a gap on the rooted basin?

Work on $G$ alone and stop paths at their first occurrence of 1. Write $\tau(x)$ for that hitting time. Give each $x\ne1$ the parent $Tx$, keeping 1 as the root. No edge leaves 1 in this rooted tree. For $y\ne1$, let $D_y$ be the subtree of paths from an input to its first 1 that pass $y$. Fix a positive summable weight on $G$. Put
$$
       s(y)=\sum_{x\in D_y}w(x),\qquad K=\sup_{y\ne1}s(y)/w(y).
$$
For $f(1)=0$, use only the outgoing residuals at $x\ne1$. This rooted residual discards the ordinary cycle edge leaving 1, and this convention is part of the following statement.

**Theorem O6.** For each $1\le p<\infty$ the rooted inequality $\|f\|_{p,w}\le C_p\|Rf\|_{p,w}$ for all vectors in the domain holds for a finite $C_p$ exactly if $K<\infty$. The optimal constant for $p=1$ is $K$.

Indeed $1_{D_y}$ has just one nonzero rooted residual, at $y$. Thus $K\le C_p^p$. Conversely if $K<\infty$, then $w\le s\le K w$ off the root. Summing the subtrees of children of $y\ne1$ gives $\sum_{Tx=y,\ x\ne1}s(x)=s(y)-w(y)\le(1-1/K)s(y)$. The killed operator $Uf(x)=f(Tx)$ on nonroot inputs with $f(1)=0$ therefore has norm at most $(1-1/K)^{1/p}$ in the equivalent $s$ weight. Its geometric resolvent gives the claimed inequality in the $w$ weight, for example $C_p\le K^{1/p}/(1-(1-1/K)^{1/p})$. For $p=1$ the sharper bound $\|f\|_{1,w}\le\sum_{y\ne1}s(y)|Rf(y)|$ follows by telescoping along each finite path and summing nonnegative terms. This yields the optimal $K$.

As a concrete positive example, $w(x)=4^{-\tau(x)}$ on $G$ has finite total mass and $s(y)\le2w(y)$: there are at most $2^j$ descendants exactly $j$ edges below $y$, each with weight $4^{-j}w(y)$. The same depth count from the root gives summability. This produces a uniform rooted gap on the specified basin. This weight uses termination time, so extending it by zero outside $G$ cannot establish that $G$ exhausts the positive integers.
