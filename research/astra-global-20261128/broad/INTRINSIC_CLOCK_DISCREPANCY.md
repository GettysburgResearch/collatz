# Additive discrepancies of actual even-event clocks

**Written proof.** Let $x\ge0$ be an even ordinary integer source. Fix $s\ge1$, $M=7s$, $h=4s$ and $m=h+1$. Observe all $M+1=7s+1$ even inputs, including the input at time zero and the final input. Write their times as $0=t_0<t_1<\cdots<t_M$ under the shortcut map. Put $u_j=t_j-j$ and $g_j=u_{j+1}-u_j$, the count of odd steps between neighboring even inputs. Use the finite collection
$$
 {\cal D}=\{u_k+u_j-u_{k+j}:0\le k\le h,\ j\ge0,\ k+j\le M\}.
$$
It contains zero. Write $L=-\min{\cal D}$, $U=\max{\cal D}$ and $W=L+U$. Set $H=3^W$, $C=8(mH)^4$, and $g=\min_{0\le j<h}g_j$. If
$$
 4C\,[2(2/3)^g]\le1, \tag{1}
$$
then
$$
 \boxed{\quad 2^{t_M}\le 3^{u_h}\,2C(x+2).\quad} \tag{2}
$$
The observed gaps are arbitrary integers. The hypothesis measures how much the odd count in a segment of $k$ gaps changes when the segment is translated. The sign test only needs the first $h$ gaps to be large. The endpoint and all discrepancy bounds come from the actual path.

### Finite proof

Set $p_j=2^{t_j}/3^{u_j}=2^j(2/3)^{u_j}$ and $D=2^L3^U$. For each $k+j\le M$ in the stated range,
$$
 a_{k,j}=Dp_kp_j/p_{k+j}=2^{L+u_k+u_j-u_{k+j}}3^{U-u_k-u_j+u_{k+j}}
$$
is an integer between 1 and $H$. Also $D\le H$. The finite even-event calibration gives $y=- (x+1)<0$ and
$$
 y-\sum_{j<M}p_j=-p_M\,(T^{t_M}x+1).
$$
The terminal factor is odd. Thus the difference has exact binary valuation $t_M$.

For $\ell=h+1,\ldots,M-1$ impose the $3s-1$ integer equations
$$
 \sum_{k=0}^h q_k a_{k,\ell-k}=0 .
$$
There is a nonzero integer solution with $|q_k|\le B=(2mH)^3$. Indeed the linear map takes $\{0,\ldots,B\}^m$ into $\{0,\ldots,mHB\}^{3s-1}$. Writing $r=3s-1$, one has $3(m-r)=3s+6>r$. Therefore
$$
 (B+1)^m>B^m>(2mH)^rB^r\ge(mHB+1)^r.
$$
Two distinct vectors have equal images, and their difference gives the stated solution. Write $C=mBH$. Form the finite rational numbers
$$
 Q_*=\sum_{k=0}^h q_kp_k,\qquad
 P_*=\sum_{\ell=0}^h A_\ell p_\ell,\qquad
 A_\ell=\sum_{k=0}^{\ell} q_k a_{k,\ell-k}.
$$
The $A_\ell$ are integral with $|A_\ell|\le C$. If $k$ is the first nonzero coordinate of $q$, then $A_i=0$ for $i<k$ and $A_k=Dq_k$. Since $p_{i+1}/p_i=2(2/3)^{g_i}$, the ordinary absolute values of the contributions after index $k$, divided by $p_k$, are bounded by $C[2(2/3)^g]/[1-2(2/3)^g]\le1/2$ in both $Q_*$ and $P_*$. Their leading coefficients are nonzero integers of the same sign. Therefore $F=DQ_* y-P_*\ne0$.

Put $S_M=\sum_{j<M}p_j$. In the finite product $DQ_*S_M$, the terms with $k+j\le h$ sum to $P_*$; the rows with $h<k+j<M$ vanish by construction. Each remaining term has $k+j\ge M$, hence $j\ge M-k$. Since $t_j$ increases,
$$
 v_2(Dp_kp_j)\ge v_2(Dp_kp_{M-k})=v_2(a_{k,M-k}p_M)\ge t_M.
$$
The term $DQ_*(y-S_M)$ has at least the same precision. Rational sums of terms with that binary divisibility retain it. Thus $3^{u_h}F$ is a nonzero integer divisible by $2^{t_M}$, since $u_j$ is nondecreasing and both finite forms use $j\le h$. Finally $|Q_*|\le2B$, $|P_*|\le2C$, so $|3^{u_h}F|\le3^{u_h}2C(x+2)$. This proves (2).

### Real slopes and balanced words

Suppose $G>0$ is any real number and $|u_j-jG|\le V$ for all $j\le M$. Then $W\le6V$, $g\ge G-2V$, $u_h\le hG+V$ and $t_M\ge M(G+1)-V$. No rationality or denominator restriction on $G$ is needed. Put $\gamma=\log_2 3$, $c=\gamma-1$. A sufficient condition for (1) is
$$
 c(G-2V)\ge6+4\log_2 m+24\gamma V .
$$
If so, taking logarithms in (2) gives
$$
 \log_2(x+2)\ge (7-4\gamma)sG+7s-(1+\gamma)V-\log_2(2C).
$$
In particular a large mean gap, comparatively small global discrepancy and a number of events with $\log M=o(G)$ lead to a physical bit-length bound, uniformly in the arrangement of the gaps. Integer-slope strips admit the improved constants of [the scalar-polynomial proof](SCALAR_CLOCK_STRIP.md), since in that case the coefficients can be normalized directly using the single error $u_j-jG$.

The actual even-event calibration and the constant intercept in $p_j$ are essential. The finite approximation and positive-source sign have precedents in Weaver paper 104 for aligned Syracuse dictionaries, which carries a separate dictionary dimension. The construction here is indexed directly by a scalar array of translated odd-count differences. It gives a finite restriction and no assertion that an arbitrary escaping orbit has an obstructing window. [Weaver, paper 104](https://rstation.ai/problems/collatz/papers/104).
