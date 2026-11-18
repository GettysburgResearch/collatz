# Uniform transport of the complete ordinary Sinai clock profile

**PROPOSED, source-qualified.** Let $y_j=U^j(n)$ be a nonperiodic positive odd Syracuse orbit, $J_j=3/2^{v_2(3y_j+1)}$, and $D_j=J_0\cdots J_{j-1}$ with $D_0=1$. Write $g_q(y)$ for the ordinary value of the depth-$q$ ternary Sinai density, as in [the low-ancestor and width bounds](../unsafe-return-weights/SINAI_LOW_ANCESTORS.md), commits `f0ad2cb` and `31d9fe3`. For all integers $k$ set
$$
 P_j(k)=\begin{cases}g_{j+k}(y_j)/D_j,&j+k\ge0,\\0,&j+k<0.\end{cases}
$$
Then $P_j$ increases coordinatewise to a bounded function $P$ on $\mathbb Z$ and
$$
 \sum_{j\ge0}\|P_{j+1}-P_j\|_\infty<\infty .
$$
In particular the convergence is uniform simultaneously over all incoming clocks. The limit tends to zero at negative infinity and is bounded away from zero on the nonnegative integers, using the [unit minorization](../native-pressure-20261118/MINORIZATION.md), commit `a367328`, for the latter conclusion. The vanishing at negative infinity sharpens to the quantitative tail bound by the variation series below. This describes a necessary profile if an ordinary orbit escapes.

Put $Z_j=\{z:U(z)=y_{j+1},\ z\ne y_j\}$, always taking odd positive sources. Every $z\in Z_j$ first enters the spine at $y_{j+1}$. The orbit is injective, so $Z=\bigcup_j Z_j$ is a reachability antichain of nonperiodic states. The width estimate (4) at the cited pin gives
$$
 \sum_{z\in Z}\sup_{q\ge1} g_q(z)/z\le C .
$$
The exact positive first-step recursion gives
$$
 R_{j,q}=g_{q+1}(y_{j+1})-J_j g_q(y_j)
  =\sum_{z\in Z_j}\frac3{2^{v_2(3z+1)}}g_q(z)\ge0 .
$$
Every coefficient divided by $y_{j+1}$ is at most $1/z$. Thus the preceding antichain bound yields $\sum_j\sup_{q\ge1} R_{j,q}/y_{j+1}\le C$. Also $R_{j,0}\le\sum_{a\ge1}3/2^a=3$, and $\sum_j1/y_j<\infty$ by the [simple-path reciprocal bound](CRITICAL_MOMENT.md). Hence $\sum_j\sup_{q\ge0}R_{j,q}/y_{j+1}<\infty$.

The ordinary affine product gives $y_j/D_j=n\prod_{i<j}(1+1/(3y_i))$, bounded above and below by positive constants depending on $n$. The new boundary coordinate $k=-j-1$ contributes $1/D_{j+1}$; all older coordinates increase by $R_{j,j+k}/D_{j+1}$. Consequently
$$
 \|P_{j+1}-P_j\|_\infty\le C_n\frac{1+\sup_{q\ge0}R_{j,q}}{y_{j+1}},
$$
which is summable. The initial $P_0$ is bounded by the same width estimate for the singleton $n$, together with its depth-zero entry. For $k<-j$, $P_j(k)=0$, so $\sup_{k<-j}P(k)\le\sum_{i\ge j}\|P_{i+1}-P_i\|_\infty\to0$. For every fixed negative $k$, its first depth-zero entry gives $P(k)\ge1/D_{-k}>0$. For $k\ge0$, $y_1$ is a ternary unit and the minorization gives $P(k)\ge P_1(k)=g_{k+1}(y_1)/D_1\ge c/D_1$.

Equivalently, define the integer phase of a source $x$ in the merger component by $b-j$ if $U^b(x)=y_j$; injectivity of the spine makes this independent of the meeting chosen. Put $r(x)=\prod_{i\ge0}(1+1/(3U^i(x)))^{-1}>0$. For each $k$ the limiting profile equals
$$
 P(k)=\sum_{x:\,\mathrm{phase}(x)=k}\frac{n\,r(x)}{x\,r(n)} .
$$
Indeed $P_j(k)$ includes exactly the sources in that phase already joined by clock $j$; each has the displayed weight by telescoping. Coordinatewise monotone convergence gives the formula. The bounded variation above therefore proves uniform convergence of these positive harmonic sums across all phase classes, including the clocks arbitrarily far ahead of the spine.
