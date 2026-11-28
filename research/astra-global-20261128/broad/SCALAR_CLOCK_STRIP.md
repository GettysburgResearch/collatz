# A finite source-height bound for arbitrary positive gap sequences in a discrepancy strip

**Written proof.** Use the shortcut map and an even ordinary source $x\ge0$. Write $t_j$ for the time of the even input numbered $j$, starting with $t_0=0$. The odd-run lengths $g_i=t_{i+1}-t_i-1$ may take any nonnegative integer values in any order. Put $\gamma=\log_2 3$ and $c=\gamma-1$.

Fix positive integers $G,s$, let $M=7s$, and observe all $M+1=7s+1$ actual even inputs from $t_0$ through $t_M$. Set $E_j=t_j-j(G+1)$ for $0\le j\le M$ and $W=\max_j E_j-\min_j E_j$. Suppose
$$
 cG\ \ge\ 6+4\log_2(4s+1)+4\gamma W. \tag{1}
$$
Then
$$
 \log_2(x+2)\ \ge\ (7-4\gamma)sG-cG+7s+2
 \quad\hbox{and hence}\quad sG\le17\log_2(x+2). \tag{2}
$$

All prefixes are measured from the supplied state. In particular the alphabet size of the $g_i$, the order of their changes and their number of changes do not occur in the result. The positive real sign of the ordinary source is used in the proof. The window condition concerns **cumulative discrepancy** in event time. A small range of single gaps suffices only when that range times the number of events is small enough, or when the deviations cancel.

## 1. Integral coefficients and the physical tail

Let $u=-\min E_j$, $v=\max E_j$, so $u,v\ge0$ because $E_0=0$, and $u+v=W$. Put
$$
 \tau=2^{G+1}/3^G,\qquad D=2^u3^v,\qquad
 a_j=D(2/3)^{E_j}=2^{u+E_j}3^{v-E_j},\qquad H=3^W .
$$
Every $a_j$ for $j\le M$ is a positive integer of size at most $H$. These bounds are independent of the number of observed clocks. Set $Y=-D(x+1)$ and $A(X)=\sum_{j<M}a_jX^j$. The elementary finite even-clock calibration gives
$$
 Y-A(\tau)=-D\,\frac{2^{t_M}}{3^{t_M-M}}\bigl(T^{t_M}x+1\bigr).
$$
The last factor is odd, and $t_M\ge M$. Consequently $v_2(Y-A(\tau))=u+t_M=M(G+1)+u+E_M\ge M(G+1)$. This identity uses only executed bits through the last indicated even input.

## 2. One scalar Padé approximation

Put $h=4s$, $m=h+1$ and $B=(2mH)^3$. Seek integer coefficients $q_k$ for a polynomial $Q(X)=\sum_{0\le k\le h}q_k X^k$ such that the coefficients of $QA$ in degrees $h+1,\ldots,M-1$ vanish. There are $r=3s-1$ homogeneous equations in $m=4s+1$ unknowns. Each matrix entry is a nonnegative integer at most $H$.

In the integer box $\{0,\ldots,B\}^m$ there are $(B+1)^m$ vectors. Each image has $r$ coordinates in $\{0,\ldots,mHB\}$. Since $mHB+1\le2mHB$ and $3(m-r)=3s+6>r$, we have $B^{m-r}>(2mH)^r$. Hence two distinct vectors have the same image. Their difference supplies a nonzero $Q$ with $|q_k|\le B$.

Let $P$ contain the terms of $QA$ through degree $h$. Then $QA-P$ is an integer polynomial divisible by $X^M$ and every coefficient of $P$ has absolute value at most $mBH$. If $k$ is the first index with $q_k\ne0$, the first coefficient of $P$ is $q_ka_0$ in the same degree. Put $C=mBH=8(mH)^4$. Condition (1) gives
$$
 4C\tau\le1.
$$
Indeed $\log_2(4C\tau)=6+4\log_2(mH)-cG$. In particular $0<\tau\le1/2$. For $Q(\tau)/\tau^k$ and $P(\tau)/\tau^k$, the absolute contributions beyond their leading terms are at most $C\tau/(1-\tau)\le1/2$. Both leading coefficients are nonzero integers of the same sign. Thus $Q(\tau)$ and $P(\tau)$ are nonzero and have the same sign. As $Y<0$, $F=Q(\tau)Y-P(\tau)\ne0$.

## 3. The two size estimates

Since $\tau$ and $Q(\tau)$ are dyadically integral, the identity
$$
 F=Q(\tau)(Y-A(\tau))+(QA-P)(\tau)
$$
gives $v_2(F)\ge M(G+1)$. The nonzero integer $I=3^{Gh}F$ is therefore divisible by $2^{M(G+1)}$.

At the ordinary absolute value, $|Q(\tau)|\le2B$ and $|P(\tau)|\le2mBH$. Since $D\le H$ and $m\ge1$,
$$
 |I|\le 3^{Gh}\,2mBH(x+2)=3^{Gh}\,2C(x+2).
$$
The sign condition implies $\log_2(2C)\le cG-2$. Combining the two estimates gives (2). For the simpler constant, $(7-4\gamma)s-c\ge(8-5\gamma)s>s/17$, using $3^{17}<2^{27}$.

## 4. Consequences and boundaries

A non-even source can have an arbitrary first odd run of length $a=v_2(x+1)$. Its first even state $u=T^a x$ satisfies $u+1\le(x+1)^2$, so $\log_2(u+2)\le 2\log_2(x+1)+1$; also $a\le\log_2(x+1)$. Apply (2) at $u$ when the shifted observed clocks meet (1).

If each of the first $7s$ gap lengths lies in $[G,G+d]$, then $W\le7sd$. Condition (1) therefore holds whenever $cG\ge6+4\log_2(4s+1)+28\gamma sd$. For $d\ge1$, this gives the dichotomy $sG\ll\log_2(x+2)$ up to a constant multiple of $G/d$ observed gaps. Taking the largest admissible $s$ shows that a much longer band forces $\log_2(x+2)\gg G^2/d$ when $G/d$ tends to infinity. A balanced sequence can have a much smaller cumulative $W$ and admits a much longer test. For example, absent further constraints, the pairwise choices $(G-1,G+1)$ or $(G+1,G-1)$ may vary arbitrarily from pair to pair; their cumulative discrepancy is at most two. A number of events exponential in a small multiple of $G$ can meet (1).

The real sign argument and finite coefficient counting are directly related to Weaver's finite approximation for growing aligned dictionaries, particularly its cumulative-excess normalization in Theorem 4. Here the shift by one at the even input makes the native inverse-series intercept independent of its following gap. One scalar series and one family of linear constraints then handle arbitrary observed gaps in the stated discrepancy strip. The size of the interpolating system grows with the window, while the normalized coefficient bound depends only on $W$. [Weaver, paper 104](https://rstation.ai/problems/collatz/papers/104).

This theorem alone does not show that every escaping orbit has such a strip on a scale that violates (2).
