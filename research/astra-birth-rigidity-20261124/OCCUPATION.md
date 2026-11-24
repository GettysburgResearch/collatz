# Ordinary occupation for finite canonical phase classes

**PROPOSED written theorem.** Let $S$ be a forward-invariant set of positive odd integers on which the accelerated map $U(q)=(3q+1)/2^{v_2(3q+1)}$ is injective. Suppose its actual scalar representatives $p(q)\in(1/2,3/2]$ take at most $L$ different values. There is an absolute $C$ such that
$$
F_S(X)=\#\{q\in S:q\le X\}\le CLX^{17/25}\qquad (X\ge1).
$$
This strengthens the exponent $47/50$ in PR189 S3. It covers a complete injective orbit in a specified rational phase class and its finite prefix after enlarging $L$. It also covers the union of periodic points with a fixed finite phase family. The union of predecessor basins generally does not satisfy the injectivity premise.

**Common clock.** For $X\ge24$ put $m=\lfloor\log_3(X/8)\rfloor\ge1$, $K=\lfloor\log_2 X\rfloor$. Starting at any $n\in S$ below $X$, follow $m$ odd steps to $q=U^m(n)$ and let $A$ be the sum of their actual gaps. Their positive affine carry satisfies
$$
q=3^mn/2^A+C_w/2^A,\qquad C_w/2^A\le
\sum_{r=1}^m 3^{r-1}2^{-r}=(3/2)^m-1 .
$$
For $A\ge K$, $X/2^A<2$ gives $q<3\cdot3^m\le3X/8<X/2$. The restriction of $U^m$ to $S$ is injective and the endpoint stays in $S$. Hence at most $F_S(X/2)$ sources belong to this lane.

**Recovering low-clock words.** For $m\le A<K$ the additive term is at most $3^m$, and $X/2^A>1$. Thus $q\le2\cdot3^m X/2^A$. As $\log_2 X=\alpha m+O(1)$ for $\alpha=\log_2 3$, the actual scalar endpoint bound gives
$$
k_m<1/2+\log_2(q)/3\le (2\alpha m-A)/3+O(1).
$$
Let $B=\sum_{i<m}b_i$, and $K_c=\sum_{i<m} k_i$. The exact clock identity $A+k_m=B+2K_c+k_0$ gives
$$
K_c\le (A+\alpha m)/3-B/2+O(1). \tag{1}
$$
All constants here are absolute. At fixed $A$ and fixed starting phase, the canonical word is determined by multiplication by three modulo one and the right-closed representative rule. The vector of the first $m$ carries determines $K_c$, $k_0$, and hence $k_m$ from the exact clock identity. The recurrence then determines every gap. Consequently counting the first $m$ carries bounds the number of actual words, even when several sources yield one word or several phases yield a common word.

Use RUN_PARTITION.md (1) with the first $m$ carry vertices and the $m-1$ intervening edges. Its partition is at most $D\lambda^{B-m}$, since the omitted final digit contributes $b_{m-1}-1\ge0$. Take the specified $x=u^2,\ \lambda=1/u$, so $-\log x=2\log\lambda$. Multiplying the partition by $x^{-[(A+\alpha m)/3-B/2+O(1)]}$ counts all vectors allowed by (1). The $B$ terms cancel. The number of candidate words at clock $A$ therefore has bounds
$$
\binom{A-1}{m-1},\qquad
CL\exp\!\left(\bigl[(2/3)(A+\alpha m)-m\bigr]\log\lambda\right). \tag{2}
$$
The first count is by positive compositions. Both counts are upper bounds for actual words, with an absolute constant in the second.

**Ordinary dyadic fibre.** Every fixed positive gap word permits at most one odd source residue modulo $2^{A+1}$. To see this directly, use the complete identity $3^mn+C_w=2^Aq$ and the odd terminal value $q$. Hence $3^mn+C_w\equiv2^A\bmod 2^{A+1}$, and $3^m$ is invertible there. It is enough that this congruence is necessary. For $A<K$, a residue class has at most $X/2^{A+1}+1\le X/2^A$ representatives up to $X$, since $X/2^{A+1}\ge1$.

**Exponent.** With $a=A/m$, the two counts in (2), each multiplied by the fibre bound, have exponents in $X$ bounded respectively by
$$
F_1(a)=1-a/\alpha+\Phi(a)/\log3,\qquad
F_2(a)=1-a/\alpha+\bigl[(2/3)(a+\alpha)-1\bigr]\log\lambda/\log3 ,
$$
up to absolute multiplicative constants and the factor $L$ in the second. Here $\Phi(a)=a\log a-(a-1)\log(a-1)$ with $\Phi(1)=0$. Indeed $\binom{A-1}{m-1}\le\binom A m\le e^{m\Phi(a)}$, and $\log X=m\log3+O(1)$; the error in the exponential is bounded uniformly since $1\le a\le\alpha+O(1/m)$.

$F_1$ increases up to $t=23/20<2$, by $\Phi'(a)=\log(a/(a-1))>\log2$ there. $F_2$ decreases throughout, because $(2/3)\log\lambda<\log2$. Both $F_1(t)$ and $F_2(t)$ are strictly below $6799/10000$; this rational comparison is certified in check_run_support.py. More explicitly $\alpha<317/200$ follows from $3^{200}<2^{317}$, $\lambda<100000/58457$ follows from the isolated root, and rational bounds on each logarithm follow by the convergent series for $2\operatorname{atanh}[(y-1)/(y+1)]$. Approaching $t$ from either side therefore gives an absolute margin below $17/25$. The low-clock lane has $O(m)$ clocks, whose factor is absorbed in this margin. We obtain
$$
F_S(X)\le F_S(X/2)+O(L X^{17/25}).
$$
Sum over dyadic scales and enlarge the constant for $X<24$.

**Subexponential complexity on one orbit.** For a particular injective orbit, the same proof allows the factor $P_b(m)$ in place of $L$, where $P_b(m)$ is the number of canonical words at this length on that orbit. Forward invariance and injectivity hold on the orbit as a set. If $\log P_b(m)=o(m)$, the product $P_b(m)O(m)=X^{o(1)}$ fits inside the strict exponent margin. Thus $F(X)\ll_q X^{17/25}$ on this wider class. The constant is source-dependent, since the asymptotic complexity assumption supplies no common modulus.
