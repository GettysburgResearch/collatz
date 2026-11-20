# How far apart can large counts of tripling failures be?

**PROPOSED.** Use the ordinary positive shortcut map. Let $E$ be the set of odd $n$ whose orbits never meet those of $3n$, and put $D(X)=|E\cap[1,X]|$. If Collatz is false, for each fixed $c>0$ and every sufficiently large real $Y$ (depending on $c$) there is a power of two $S$ satisfying
$$
 Y\le S\le Y^{32},\qquad |E\cap[S,2S)|\ge c S^{0.84}. \tag{1}
$$
Thus the maximum normalized count on these shells tends to infinity as $Y$ grows. The proof combines the published predecessor count and irrationality estimate with the finite chain controlling the variation of component labels. [Predecessor count, Theorem 6.1](https://arxiv.org/abs/math/0205002) · [Irrationality estimate, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007) · [Finite chain](TRIPLING_VARIATION.md)

## Arbitrarily large predecessor coefficients

For **each** actual component $C$ one has $|C\cap[1,X]|/X^{0.84}\to\infty$. Choose an odd positive ternary unit $a\in C$ off any cycle of the accelerated odd map $S(n)=(3n+1)/2^{v_2(3n+1)}$. Any odd ternary-unit target has at least two distinct odd ternary-unit preimages: among the three $1\le v\le6$ of the correct parity, exactly one gives $2^v a\equiv1\pmod9$, and the other two yield $(2^v a-1)/3$ of the required type. Every component contains an odd ternary unit, and if the initial one lies on a cycle, at most one of its preimages lies on that cycle. This supplies the required $a$.

For any fixed $k$, this inverse tree contains $2^k$ distinct ternary-unit odd targets $b$ with $S^k(b)=a$. None of them can reach another: $S^j(b)=b'$ for distinct such targets would imply $S^j(a)=a$ with $j>0$. Consequently all their ordinary predecessor sets are disjoint. Theorem 6.1 of Krasikov and Lagarias gives at least $X^{0.84}$ predecessors for each of these finitely many targets once $X$ exceeds their individual thresholds. Therefore $|C\cap[1,X]|\ge 2^kX^{0.84}$ eventually, for every $k$. This argument uses the theorem as printed. Its published proof also reports an unrounded exponent above $0.84$. [Theorem 6.1 and Table 2](https://arxiv.org/pdf/math/0205002)

There is also a bounded-multiplicity transfer from a cumulative count to a shell count for the same component. Write $n=2^v u$ with $u$ odd and put $W(u)=4u+1$. This has the same label since $T^2(W(u))=3u+1$. Set $w=u$ if $3\nmid u$ and $w=W(u)$ otherwise. Thus $w$ is an odd ternary unit and has at most two possible odd antecedents $u$. Choose $v+1\le a\le v+6$ with $2^a w$ congruent to 4 or 7 modulo 9; the order of 2 modulo 9 is six. Then $z=(2^a w-1)/3$ is an odd ternary unit in the same component, with $z\le 107n$. The integer $3z+1$ determines $a$ and $w$ uniquely, so each $z$ has at most twelve antecedents $n$. For $n\le M/107$ send each distinct such $z$ by doubling into $[M,2M)$. Distinct odd parts give distinct images, proving
$$
 |C\cap[M,2M)|\ge \tfrac1{12} |C\cap[1,M/107]|.
$$
In particular $|C\cap[M,2M)|/M^{0.84}\to\infty$. To transfer to the odd lattice $k=3y+1$ with scaling $k\mapsto4k$, choose $b\in\{1,2\}$ with $2^bz\equiv1\pmod3$ and $y=(2^b z-1)/3$. Then $y$ is positive and odd, the odd part of $3y+1$ recovers $z$, and $v_2(3y+1)=b\le2$. In particular $y$ has no odd predecessor under $W$, since $3W(h)+1=4(3h+1)$ for odd $h$. Distinct $y$ can therefore be lifted without collisions by iterating $W$ into $3W^i(y)+1\in[M,4M)$, after starting with $n\le M/428$. This gives the same diverging coefficient for the odd-lattice shells. [Fixed-ratio localization](ODD_TRIPLING_SHELLS.md)

## Comparing two different dyadic scales

Let $f(n)$ indicate the component of 1. Define $g_R(t)=f(\lfloor R2^t\rfloor)$ on the unit circle for a dyadic $R$, and write $T_\theta$ for rotation by $\theta=\log_2 3$. The adjacent-change estimate, doubling invariance and the comparison at $3\lfloor R2^t\rfloor$ give absolute constants $C_0,C_1$ for which
$$
 \operatorname{Var}(g_R)\le 1+C_1D(C_0R),\qquad
 \|g_R-g_{2R}\|_1+\|g_R\circ T_\theta-g_R\|_1\le C_1D(C_0R)/R. \tag{2}
$$
The boundary jump accounts for the possible extra one. The two norm estimates count respectively changes between $2n$ and $2n+1$, and changes introduced by tripling and rounding. [Details for the two comparisons](THREE_RAY_DENSITY.md#passing-to-a-limit-under-doubling)

Write $\alpha=0.84$ and $\kappa=4.117$. Suppose that at some large $Y$ all dyadic $S\in[Y,Y^{32}]$ have fewer than $\varepsilon S^\alpha$ failures in $[S,2S)$. Summing geometric series gives $D(t)\ll Y+\varepsilon t^\alpha$ for $1\le t\le Y^{32}$. Let $X$ be the largest power of two at most $Y^{32}/(2C_0)$, and let $Z$ be the largest power of two at most $Y^{1.192}$. For all dyadic $Y\le R\le Z$, telescoping (2) up to $X$ gives
$$
 \|g_R-g_X\|_1\ll Y/R+\varepsilon R^{\alpha-1}. \tag{3}
$$
Both powers in this geometric tail are strictly negative.

The lower bound $\|h\theta\|\gg h^{-\kappa}$ supplied by Wu and Wang, and Dirichlet approximation, give a reduced $p/q$ with
$$
 Z\le q\ll Z^\kappa,\qquad |\theta-p/q|\le q^{-2}.
$$
Indeed apply Dirichlet with size $L=\lceil K Z^\kappa\rceil$, where the absolute $K$ is sufficiently large. The reduced denominator satisfies $q\le L$ and $\|q\theta\|\le 1/L$, so $q\gg L^{1/\kappa}\ge Z$. The discrepancy of the first $q$ rotations is $O(1/q)$, uniformly in their initial point, by comparison with the rational grid. [Grid discrepancy proof and precise published exponent](THREE_RAY_VARIATION.md#rotation-on-the-logarithmic-circle)

Let $A_q$ be averaging over these rotations and let $m_R=\int g_R$. Apply discrepancy at the **smaller** scale to get $\|A_q g_R-m_R\|_1\ll (1+D(C_0R))/q$. At the **larger** scale, telescoping (2) gives $\|g_X-A_qg_X\|_1\ll qD(C_0X)/X$. Because $A_q$ is an $L^1$ contraction, (3) now gives
$$
 \|g_R-m_R\|_1
 \ll Y/R+\varepsilon R^{\alpha-1}
    +(1+Y+\varepsilon R^\alpha)/q
    +q(Y/X+\varepsilon X^{\alpha-1})
 \ll Y/R+\varepsilon R^{\alpha-1}. \tag{4}
$$
In the last estimate $q\ge Z\ge R$. Also $X\gg qR$ and $X\gg Rq^{1/(1-\alpha)}$, since $1.192(1+4.117/0.16)<32$. All implicit constants are independent of $Y$ and $\varepsilon>0$. The threshold on $Y$ may depend on the fixed $\varepsilon$.

For a binary $g_R$, $\|g_R-m_R\|_1=2m_R(1-m_R)$. On every dyadic shell $AY\le R<Z$, where $A$ is a large fixed absolute constant, (4) puts $m_R$ within $1/8$ of either zero or one for large $Y$. The choice is the same for all these shells: (3) puts every $m_R$ within $1/8$ of $m_X$. Every integer in $[R,2R)$ has logarithmic measure $\gg 1/R$. Hence the same minority color has $O(Y+\varepsilon R^\alpha)$ members in every such shell. Up to $Z$ its cumulative count is $O(Y\log Z+\varepsilon Z^\alpha)$, including the integers below $2AY$. Since $1.192\alpha>1$, the first term is $o(Z^\alpha)$. For each fixed $\varepsilon>0$, this bounds the minority count divided by $Z^\alpha$ by a fixed constant. Both the component of 1 and a fixed second component have that ratio tending to infinity, by the disjoint predecessor sets above. This contradiction proves (1) for every fixed coefficient.

## An exact comparison with the complement of a single component

Give the countable set of actual ordinary merger components its discrete metric, and now let $g_R(t)$ record the actual component. Measure distances between two such functions by the measure of the set where they differ. The two norm bounds in (2) still hold in this metric: the finite chain and the rounding argument count changes of arbitrary labels. Suppose $\sum_{d\in E}1/d<\infty$. Since $\sum_j 2^{-j} D(C_0 2^j)<\infty$ by exchanging the order of summation, the first Borel–Cantelli lemma implies the component labels $g_{2^j}(t)$ are eventually constant for almost every $t$. Their limit is an actual measurable component label. The rotation error tends to zero by (2), so the limit is invariant under irrational rotation almost everywhere. Ergodicity makes every one of its countably many level sets null or conull. One of them is conull, yielding a unique component $C$ of natural density one. This conclusion permits infinitely many other components.

More precisely, for each dyadic $R=2^j$ the measure $p_j$ of starting phases whose labels differ from $C$ satisfies
$$
 p_j\le C_1\sum_{k\ge j} 2^{-k}D(C_0 2^k).
$$
Outside the union of these successive change sets the current label already equals its almost-everywhere limit. Consequently there are $O(2^j p_j)$ ordinary integers outside $C$ in $[2^j,2^{j+1})$.

The upper bound for a dyadic shell also gives, with absolute constants,
$$
 A_C(X):=|[1,X]\setminus C|\ll D(X)+X\sum_{\substack{d\in E\d>X}}d^{-1}.
 \tag{4a}
$$
Indeed, apply the lossless transfer to the union outside $C$, choosing a dyadic shell $[M,2M)$ with $107X\le M<214X$. Its minority count is $O(Mp_{\log_2 M})$. In the dyadic tail for $p_{\log_2 M}$, a single $d$ contributes at most a constant times $\min(1,C_0M/d)$ after multiplication by $M$. Since $M\asymp X$, the resulting sum is equivalent up to absolute factors to the right side of (4a). The reverse elementary count is $D(X)\le 2A_C(3X)$.

Consequently a counterexample would force the **soft-cutoff count**
$$
 \frac{1}{X^{0.84}}\sum_{d\in E}\min(1,X/d)\longrightarrow\infty
$$
at every large scale. If the reciprocal sum diverges this expression is infinite already. Otherwise a fixed second component makes $A_C(X)/X^{0.84}\to\infty$, and (4a) applies. This all-scale statement includes a reciprocal tail of future failures; (1) is the corresponding conclusion here involving only actual failures up to a finite cutoff.

For every $0<s<1$ with $\sum_{d\in E}d^{-s}<\infty$ the same $C$ therefore satisfies
$$
 \frac{1}{1+3^s}\sum_{d\in E} d^{-s}
 \ \le\ \sum_{n\notin C} n^{-s}
 \ \ll_s\sum_{d\in E} d^{-s}. \tag{5}
$$
For the upper bound sum $2^{(1-s)j}p_j$ and exchange the two sums. The inner geometric sum through $k$ is $O_s(2^{(1-s)k})$, leaving $\sum_k 2^{-sk}D(C_02^k)\ll_s\sum_{d\in E}d^{-s}$. For the lower bound, valid for **any** component $C$, at least one of $d$ and $3d$ is outside $C$. Summing the two possible contributions proves the estimate.

For a set $S$ write $\delta(S)=\limsup_{X\to\infty}\log(1+|S\cap[1,X]|)/\log X$. Its Dirichlet series $\sum_{n\in S} n^{-s}$ converges for $s>\delta(S)$ and diverges for $0<s<\delta(S)$, by dyadic grouping and the counting definition. Formula (5) gives the exact identity
$$
 \delta(E)=\min_{C\ \mathrm{a\ component}}\delta(\mathbb N_{>0}\setminus C).
$$
If $\delta(E)<1$, the minimum is attained uniquely by the density-one component. Indeed its complement has dimension at most $\delta(E)$ by (5), and every other complement contains that density-one component. If $\delta(E)=1$, the lower-bound argument in (5) gives complement dimension one for every component.

These comparisons do not establish whether any odd tripling pair actually fails. A proof excluding the counts in (1), or giving a finite subcritical moment contradicted by the predecessor theorem, would settle the original problem.

## A critical moment and a tradeoff between growth exponents

A counterexample forces quantitative divergence at the critical exponent:
$$
 \frac{1}{\log\log X}\sum_{\substack{d\in E\\d\le X}}d^{-0.84}\longrightarrow\infty .
$$
Indeed choose $Y_{j+1}=3Y_j^{32}$ with $Y_0$ sufficiently large. The shells furnished by (1) are disjoint. Each contributes at least $2^{-0.84}c$ and there are $\gg\log\log X$ completed shells below $X$. The coefficient $c$ can be taken arbitrarily large. Even the sum of $d^{-0.84}/(1+\log\log d)$ over failed $d\ge3$ diverges, since $\log\log(2Y_j^{32})=O(j+1)$. The proof of (1) works uniformly over all partitions of the actual components that separate two fixed components. In that version $E$ is the set crossing the chosen partition, and the constants depend only on the two fixed predecessor targets. In particular the same critical lower bounds apply to every such cut.

Let $\ell$ and $\sigma$ be the lower and upper limits of $\log(1+D(X))/\log X$. A second component also forces
$$
 \sigma+\frac{1-\alpha}{\alpha}\,\ell\ge1,\qquad \alpha=0.84. \tag{6}
$$
When $\sigma=1$ this is immediate. Otherwise suppose more generally that $D(t)\ll t^\gamma$ for a fixed $\alpha\le\gamma<1$. The critical case $\gamma=\alpha$ is already excluded by (1). There is a unique density-one component $C$, and a fixed second component supplies
$$
 |[R,2R)\setminus C|/R^\alpha\longrightarrow\infty
$$
by the lossless shell transfer above. At a dyadic $R$ with $C_0R\le X$, split the bound for its minority count $O(Rp_{\log_2 R})$ at $C_02^k=X$. Since the dyadic weights from $k=\log_2 R$ have bounded total after multiplying by $R$, the earlier contribution is $O(D(X))$. The later tail is $O_\gamma(R X^{\gamma-1})$. For $\gamma>\alpha$ choose $R$ within a factor of two of $X^{(1-\gamma)/(1-\alpha)}$, which is $o(X)$ and makes the latter bound $O(R^\alpha)$. Thus
$$
 \frac{D(X)}{X^{\alpha(1-\gamma)/(1-\alpha)}}\longrightarrow\infty .
$$
Taking $\gamma>\max(\sigma,\alpha)$ and letting it decrease to $\sigma$ proves (6), since (1) gives $\sigma\ge\alpha$. For example, upper exponent at most $0.90$ forces lower exponent at least $0.525$. An actual upper bound $D(t)=O(t^{0.90})$ also forces a diverging coefficient at that lower power.


## A uniform weighted inequality for every union of components

For $0<s<1$ let $\mu_s(A)=\sum_{n\in A}n^{-s}$ and, for any union $A$ of components, set $e_s(A)=\sum_{d\text{ odd}}d^{-s}|1_A(d)-1_A(3d)|$. Applying the dyadic argument directly to this binary labeling gives, in the extended nonnegative reals,
$$
 (1+3^s)^{-1}e_s(A)\le \min(\mu_s(A),\mu_s(A^c))\le C_s e_s(A).
$$
For the upper bound, if $e_s(A)$ is finite then its reciprocal crossing sum is also finite. The binary dyadic limit is constant, and the calculation proving (5) bounds the weighted measure of the opposite side by $C_s e_s(A)$. The lower bound counts each crossing by its endpoint on either specified side. The constants are independent of $A$ even if there are infinitely many components.

In particular for any real step-invariant function $F$ with finite $\ell^p(\mu_s)$ norm, $1\le p<\infty$, one has
$$
 \left(\sum_n n^{-s}|F(n)|^p\right)^{1/p}
 \ll_{s,p} \left(\sum_{d\text{ odd}}d^{-s}|F(d)-F(3d)|^p\right)^{1/p}.
$$
Indeed the sets $A_t=\{|F|^p>t\}$ have finite measure for every $t>0$, so their complements have infinite measure. Integrate the cut inequality for $A_t$ over $t$ by Tonelli. Its right side becomes $C_s\sum_d d^{-s}||F(d)|^p-|F(3d)|^p|$. For $p=1$ apply the triangle inequality. For $p>1$ use $|u^p-v^p|\le p|u-v|(u+v)^{p-1}$ for $u,v\ge0$, followed by Hölder. The remaining factor is bounded by a constant times $\|F\|_p^{p-1}$ since $\sum_d d^{-s}|F(3d)|^p\le 3^s\|F\|_p^p$. This proves the inequality without choosing a median on the space of infinite total measure.
