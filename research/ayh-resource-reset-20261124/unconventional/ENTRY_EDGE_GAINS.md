# How many inverse generations can enter an ordinary escaping ray?

**Written theorem.** Every distinct positive odd trajectory would have summable maximal gain from its fresh inverse branches. The sum still converges at an exponent strictly below one when it includes a number of complete inverse generations proportional to the logarithm of their least ordinary ancestor. The proof groups actual sources at one shortcut clock and recovers the possible odd vertices on either side of that clock. The result leaves existence of a distinct positive trajectory open.

Let $T$ be the shortcut map, $U(x)=(3x+1)/2^{v_2(3x+1)}$ on odd inputs, and let $q_j=U^j(a)$, $j\ge0$, be distinct positive odd integers. The expanded shortcut ray containing all intervening even states is injective, since a repeated state would give a repeated odd state. For any off-ray odd $y$ first entering the odd ray at $q_j$, write $r_y\ge1$ for its number of odd transitions up to that first visit. We keep $j\ge1$ to agree with the fresh-sibling convention. Including arrivals to $q_0$ in the counting proof works as well. Let
$$
 m_y=\min\{v>0:\ v\text{ odd and }U^i(v)=y\text{ for some }i\ge0\}.
$$
All three-adic residue classes are allowed for $v$ and $y$.

## The actual entry fibre

For any interval $I$ of $M$ consecutive positive integers, any shortcut clock $h\ge0$ and integer $R\ge1$, let $N(I,R)$ count the distinct off-ray odd $y$ with $r_y\le R$ reachable from an odd $x\in I$. Let $G_h(M)$ be the uniform upper bound for distinct pairs $(T^h x,J_h(x))$ over any translated interval of length $M$, where $J_h$ counts odd steps. Then
$$
 N(I,R)\le G_h(M)\left[(h+2)\sum_{l=0}^{\min(h,R)}{h\choose l}+R\right]. \tag{1}
$$
In particular the bracket is at most $(h+2)^2$ when $R=1$.

Group the original starts by $z=T^h x$. Let $b$ be the physical time of the marked odd $y$ and $t>b$ the time of first odd-ray entry. Each admissible $y$ falls into one of three cases.

* If $b\ge h$, the portion from $z$ through its first odd-ray visit is fixed. Its last $R$ off-ray odd states give at most $R$ possibilities.
* If $b<h<t$, record the nonempty subset of times in $[b,h)$ at which the path is odd. It has at most $R$ members and its least member is $b$. Starting at $z$, reverse the specified odd and even steps down through that least member. Each marked bit has at most one inverse, so this reconstructs $y$. The last odd transition is allowed to straddle $h$ through a long run of halvings.
* If $b<t\le h$, choose $t$ in at most $h+1$ ways. The odd-ray entry $q_j$ is determined, since $T^{h-t}$ is injective on the expanded ray and $T^{h-t}q_j=z$. Record the set of at most $R$ odd times in $[b,t)$. Reversing from $q_j$ reconstructs $y$ as before.

There are at most $G_h(M)$ choices for $z$. This proves (1) for all physical first-entry times. A single $x$ may mark several vertices, and subtrees belonging to different generations can overlap. Neither fact changes the count of reconstructed labels.

## Compression and growing generations

Put $k=\lceil\log_2 M\rceil$, $\theta=H_2(\log_3 2)$, and $d=\theta-\gamma$ for the absolute $\gamma>0$ in Paper 28/v3, Theorem A (P1). That source proves $G_{k^2}(M)\ll M^d$, uniformly in the location of the interval. Thus (1) gives, for each fixed $R\ge1$,
$$
 N(I,R)\ll_R M^d(1+\log M)^{2R+2}. \tag{2}
$$
For $R=\lfloor c\log M/\log\log M\rfloor$, fixed $c>0$, the binomial factor and the polynomial prefactor are $M^{c+o(1)}$, using natural logs and $\sum_{l\le R}{h\choose l}\le(eh/R)^R$ for $R\le h/2$. The corresponding upper bound is $M^{d+c+o(1)}$. No numerical value for $\gamma$ is needed. [Uniform Collatz interval compression, Theorem A](https://rstation.ai/problems/collatz/papers/28/v3)

A shorter clock reaches true logarithmic depth with an elementary exponent. Set
$$
 \rho=\max\{H_2(3/5),(3/5)\log_2 3\}<1.
$$
Then $G_k(M)\ll(k+1)2^{\rho k}$. Indeed each length-$k$ parity word occurs at most once in $I$: the usual parity lifting induction gives one residue modulo $2^k$. Words with more than $3k/5$ odds therefore contribute at most $2^{H_2(3/5)k}$. For the others, group by their exact odd count $p$. With $I=[A,A+M)$, all images in a group satisfy
$$
 2^{-k}3^p A\le T^k x<2^{-k}3^p(A+M)+(3/2)^p.
$$
The affine offset is largest when all odd steps occur last, by swapping each odd-even pair. The displayed width is at most $3^p+(3/2)^p$ since $M\le2^k$. Summing over the at most $k+1$ labels proves the bound, for every $A$.

For $0<\eta<1/2$ take $R=\lfloor\eta\log_2 M\rfloor$. Applying (1) at $h=k$ and the binary entropy bound gives
$$
 N(I,R)\ll (1+\log M)^2 M^{\rho+H_2(\eta)}. \tag{3}
$$
For example $\eta=1/512$ gives $\rho+H_2(\eta)<1$. Indeed $5^{200}<2^{275}3^{120}$ and $3^{24}<2^{39}$ give $\rho<39/40$, while $H_2(1/512)\le(\log_2(512e))/512<11/512$. Using decimal values gives an exponent about $0.9914$.

## The full-depth maximal gains

For an actual odd path $v\longrightarrow q_j$, let $g(v,j)=3^i/2^u$ with $i$ odd transitions and $u$ shortcut clocks. Write $M_j=g(a,j)$. Define the dimensionless gain of the entire inverse branch rooted at $y$ by
$$
       G_y=\sup_{v\to y}\frac{g(v,j)}{M_j}. \tag{4}
$$
Its supremum ranges over all ordinary odd ancestors at all depths. The number of permitted **marked** generations $r_y$ is a separate parameter.

The existing corrected height on an injective component is
$$
 P(v)=v\prod_{i\ge0}\left(1+\frac1{3U^i(v)}\right),
 \qquad v\le P(v)\le C v,\qquad
 P(Uv)=\frac3{2^{v_2(3v+1)}}P(v). \tag{5}
$$
For completeness the uniform bound follows from the elementary short-clock image estimate above: $T^k$ is injective on every expanded simple ray, so its number of vertices below $X$ is $O((1+\log X)X^{\rho})$. Dyadic summation gives a uniform reciprocal sum, and hence a uniform product bound. The last identity follows from the first factor. An ordinary source merging into the supplied ray belongs to just such a component. The prior tilted trace uses the stabilized ratio $vg(v,j)/(aM_j)$ for all unit sources and its atomic sum at powers greater than one. [Corrected-height construction](https://github.com/GettysburgResearch/collatz/blob/a1379492dbaae85e0d16662b41ccc7176ab3c66e/research/astra-global-synthesis-20261124/section/proof.md) · [Tilted trace, equations (7)–(9)](https://github.com/GettysburgResearch/collatz/blob/5cf2ea9dda23470b600a72a2fab20d929f668e5d/research/astra-unconventional-20261126/boundary/TILTED_TRACE.md)

Exact cancellation in (5) gives
$$
 G_y=\frac{P(a)}{\min_{v\to y}P(v)},\qquad
 \frac{P(a)}{C m_y}\le G_y\le\frac{P(a)}{m_y}. \tag{6}
$$
The minimum exists since $P(v)\ge v$. Apply (2)–(3) to $I=[1,\lfloor X\rfloor]$. A vertex with $m_y\le X$ is reached by its very own minimizing source in this interval. Dyadic summation yields the following, with constants uniform in the supplied ray after dividing each $G_y$ by $P(a)$.

1. For fixed $R$, $\sum_{1\le r_y\le R}G_y^s<\infty$ for every $s>d$. The case $R=1$ concerns all fresh sibling branches from the whole ray.
2. For fixed $c>0$ and $s>d+c$, summability persists over $r_y\le c\log m_y/\log\log m_y$, using $m_y\ge16$ and treating smaller minima separately at fixed depth. This uses (P1).
3. For fixed $0<\eta<1/2$ and $s>\rho+H_2(\eta)$,
$$
 \sum_{1\le r_y\le\eta\log_2 m_y}G_y^s<\infty. \tag{7}
$$
In particular (7) holds for some $s<1$ at $\eta=1/512$. This statement uses the elementary short-clock argument alone.

The earlier whole-ray theorem bounds basin-density losses and counts the *entry indices* $j$ from a translated interval. Its unit density floor also bounds an inverse-minimum subseries at one generation. Equations (1)–(7) track individual vertices, include nonunits, and control complete generations with a source-height-dependent radius. These estimates require no assumption on the existence of basin densities. [Summable branch losses and entry-index counting, sections 2–4](https://github.com/GettysburgResearch/collatz/blob/4cc06e7d8fdec923eed73a26b1e9d680c9f701d1/research/astra-multiple-attacks-20261125/synthesis/README.md)

## The obstruction to a descent proof

Given any $\beta>0$, every source with $g(v,j)/M_j\ge\beta$ has $v\le P(a)/\beta$. There are finitely many such ordinary sources in the component. After their last first-entry index, every one follows the prescribed odd ray. In particular the actual large-gain sources and their relative gains eventually stabilize. The component minimum of $P$ exists, and starting on such a minimizer maximizes every rooted multiplier over all paths to the same terminal vertex, at every future index. Local finiteness supplies a positive multiplicative gap to the next distinct corrected height. Paper 207 already selects such a corrected-height minimizer on every escaping component for its original-deadline visitor theorem. [Smaller Collatz visitors at the original deadline, §1](https://rstation.ai/problems/collatz/papers/207)

To contradict an escape, a fresh branch must supply enough full, normalized gain for one of the sums above to diverge. A gain measured only from $y$ to $q_j$ loses the factor $M_j$, which tends to infinity by (5). Ternary feasibility of a new local multiplier does not rebuild the fixed ordinary prefix: for a fixed $i$-odd prefix, changing its odd source while retaining its exponent word changes its odd endpoint by a nonzero multiple of $2\cdot3^i$. The anchored endpoint obeys $q_i+1\le(a+1)(3/2)^i$. Hence at large $i$ no distinct endpoint of comparable size can be reached by transplanting this entire prefix unchanged. A deterministic lower bound on the full fresh gain of the supplied ray is open.
