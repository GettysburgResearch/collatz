# A two-hit proof for ordinary Sturmian parity and valuation schedules

Let $d_j=A j+B\lfloor j\alpha+\beta\rfloor+D$ with integers $A,B\ge1$, $0<\alpha<1$ irrational, and $D$ fixed. Put $\theta=A+B\alpha>1$ and suppose, by scaling, $d_j\ge0$. The 2-adic number $\Xi=\sum_{j\ge0}2^{d_j}3^{-j}$ is irrational. This proof uses the best approximation property of continued fractions and integer size bounds.

For convergents $p/q$ from below set $P_q=Aq+Bp$ and use $G_q$ from [the main proof](PROOF.md). It is a sum of terms $(2^B-1)2^{d_j}3^{-j}$ over the visits to an interval of width $\|q\alpha\|$. There are infinitely many visits; let $m<m'$ be the first two, with $m'\ge m+q$. At 2 the valuation of $G_q$ is exactly $d_m$, and subtracting its first term gives valuation exactly $d_{m'}$.

If $\Xi$ were rational, all $G_q$ would have denominators dividing one fixed positive odd integer $D_0$. Indeed $3^q$ clears the 3-power denominators from the finite prefix and possible powers of 2 in the denominator cancel by 2-integrality. Write $\lambda=3/2^\theta$ and $L=\max(0,\log\lambda)$. In the ordinary absolute value the finite defining expression gives
$$
 |G_q|\ll(q+1)e^{Lq}.
$$
This follows from $P_q=\theta q+O(1)$, $d_j=\theta j+O(1)$, and the finite geometric sum for the prefix. Since $D_0G_q$ is a nonzero integer divisible by $2^{d_m}$, with $u=L/(\theta\log2)$ we obtain
$$
m\le uq+O(\log q).                                               \tag{1}
$$
After subtracting the first hit and clearing denominators, the nonzero integer gives
$$
2^{d_{m'}}\le D_0 3^m |G_q|+D_0(2^B-1)2^{d_m}.
$$
If $\lambda\le1$, (1) gives $m=O(\log q)$, so the right side is polynomial in $q$ while $m'\ge q$. If $\lambda>1$, one has $2^{d_m}\ll3^m$, and taking logarithms yields
$$
\theta(m+q)\log2\le m\log3 +Lq+O(\log q).
$$
Because $\log3=\theta\log2+L$, this implies $1\le u+u^2+o(1)$ by (1). But $\theta\ge1$ gives $u\le\log_2(3/2)<3/5$ (since $3^5<2^8$), while $3/5+(3/5)^2=24/25<1$. This contradiction proves irrationality.
