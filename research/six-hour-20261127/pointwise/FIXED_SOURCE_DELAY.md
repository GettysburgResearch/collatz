# Extra odd departures forced at one fixed ordinary source

Let $U$ be the ordinary accelerated map on positive odd integers. Write $M_R(X)$ for the least positive odd ancestor of $X$ within $R$ odd departures. Fix an arbitrary ordinary odd source $y$. Consider a genuine visit $U^q(y)=X$, and write $B=M_R(X)$. These assertions require no selection of a new source as the budget increases.

**Theorem 1.** Suppose $B>y$. Put $\alpha=3/2$ and $\beta=\log_2 3$. Then
\[
 q\ge R+\log_{\alpha}\frac{B+1}{y+1}
 +\max\!\left(0,\left\lceil\log_\beta\frac{\log(B+1)}{\log(y+1)}\right\rceil-1\right).
\]
In particular the count exceeds $R$. Define $m=q-R$. The actual odd bridge point $u=U^m(y)$ reaches $X$ in exactly $R$ steps, so $u\ge B$. In the first $m$ steps let $b$ be the number with exact exponent at least two. Each exponent-one step multiplies the shifted height $v+1$ by exactly $3/2$, and each exponent at least two does not increase $v+1$. Consequently $u+1\le\alpha^{m-b}(y+1)$.

A run of $l$ exponent-one steps at $v$ requires $2^{l+1}\mid v+1$, because its endpoint plus one is $3^l(v+1)/2^l$ and is even. Hence this run multiplies $\log_2(v+1)$ by at most $1+\log_2(3/2)=\beta$. There are at most $b+1$ such runs and the intervening departures do not increase height, giving $\log(u+1)\le\beta^{b+1}\log(y+1)$. Combine the two bounds. The absolute leading growth envelope itself is the sharp all-$s$ kernel inequality proved in `PositiveBudget.lean`; the counted-run refinements in this note are written arguments.

**Theorem 2 (with the stated prior complexity input).** For a fixed $y$, consider any sequence of parameters for which $U^q(y)=X$ and $B=M_R(X)\to\infty$. For all sufficiently large parameters there is an absolute $c>0$ such that
\[
 q\ge R+\log_{3/2}\frac{B+1}{y+1}
       +c\,\log\log B\,\log\log\log B .
\]
Indeed $m\ge\log_{3/2}((B+1)/(y+1))\to\infty$. A fixed trajectory making visits with $B\to\infty$ is unbounded and never visits 1; a periodic orbit has only finitely many possible values $B\le X$ along itself. Use Paper 15/v2, Theorem 1, equation (2), at the **fixed original start** with dictionary consisting of the one-letter word $(2)$. Its only positive phase center is 1. Single arbitrary exponents at least two are allowed counted pieces and strings of ones are free, so its actual dictionary cost is at most $b$. Thus $b\ge c_0\log m\log\log m$ for all sufficiently large $m$. This is the prior input; inserting it into $m\ge\log_{3/2}((B+1)/(y+1))+b$ gives the result. The elementary reset-count inequality and the preceding use of the same dictionary have repository precedents. [Paper 15/v2, Theorem 1](https://rstation.ai/problems/collatz/papers/15) · [Relative reset rigidity, section A at PR 200](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/defects/RELATIVE_RESET_RIGIDITY.md)

At the specified reflected-17 targets $X=2\cdot3^R z-t$, the seven-phase theorem gives $B=2^{H+1}3^{R-p}z-17$ with its declared $(p,H)$. Uniformly in the seven phases and $z\ge1$, $\log(B+1)\ge(11/7)R\log 2+\log z-O(1)$. Thus whenever these targets occur at unbounded $R$ along one fixed ordinary odd source,
\[
 q\ge\left(1+\frac{11\log2}{7\log(3/2)}\right)R
       +\log_{3/2}z+c'\log R\log\log R-O_y(1).
\]
The elementary bound alone already improves the straight endpoint-size estimate, whose leading slope is $\log_{3/2}3$. This is an exclusion of early visits to the indicated shrinking targets on a fixed orbit. It does not imply that such visits occur or that any fixed source has a cheaper merger.
