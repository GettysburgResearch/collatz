# Combined moments exclude every periodic stack increment word through period eighteen

**PROPOSED.** For every positive stack increment word of period $1\le r\le18$, every initial height $m\ge0$, and every finite steering prefix of positive increments, the native value $\Theta$ in $\mathbb Q_2$ is irrational. Thus none of these directives has an ordinary initial context. The proof works with arbitrary positive increments in the period. The previous source-pinned result covered all words through period nine. This statement concerns this stack construction alone.

Use PR #20 at `82ca2f932438a9fe0897704ba62959ca23ec830f`, `research/padic-repetition/claims/L-9407-stack-partial-theta-normal-form.md` and L-9408 for the stack interface. T-9422 at that head proves its period-nine theorem using L-9418. Here we choose one polynomial by a pigeonhole argument on combined coefficients and evaluate it at many shifted arguments. No theorem about the equality of real and 2-adic limits is used.

## 1. Quadratic exponents and distinct limits

Fix the period, its positive increments $d_1,\ldots,d_r$, their sum $S$, and the starting height m. Define
$$
 m_j=m+\sum_{i=1}^j d_i,\qquad E_0=0,\qquad E_j=\sum_{i=1}^j(9m_i+1),\qquad
 T=64/81,\qquad F(Y)=\sum_{j\ge0}T^{E_j}Y^j .
$$
Here the increments are extended periodically. Set $a=9S/r>0$. The difference $E_{j+r}-E_j$ is affine in j, with slope $9S$: the difference of successive such expressions is $9(m_{j+r+1}-m_{j+1})=9S$. Therefore $E_j=aj^2/2+bj+u_j$ for a fixed rational b and a bounded r-periodic $u_j$, with $u_0=0$. In particular for s a nonnegative multiple of r,
$$
 E_{s+j}=E_s+asj+E_j,\qquad
 F(1)=P_s+T^{E_s}F(T^{as}),\qquad P_s=\sum_{j<s}T^{E_j}.        \tag{1}
$$
Here $as$ is an integer and (1) holds in each completion separately. All estimates below may depend on the fixed word and m.

Write $\Theta_2=F(1)$ in $\mathbb Q_2$ and $\Theta_R=F(1)$ in $\mathbb R$. Assume $\Theta_2=\xi=A_0/B_0$ in lowest terms, with $B_0>0$ odd. Then necessarily $\xi\ne\Theta_R$. In fact $v_2(\xi-P_s)=6E_s$ by the unique first omitted term. If the two limits agreed, the nonzero integer $J=B_0 81^{E_{s-1}}(\xi-P_s)$ would satisfy
$$
 64^{E_s}\le |J|\le O_{B_0}(81^{E_{s-1}} T^{E_s}).
$$
The real tail estimate uses $E_{i+1}-E_i\ge1$. The displayed inequality contradicts $E_s-E_{s-1}\to\infty$. Hence $|\xi-P_s|$ in the real embedding is bounded below by a fixed positive constant for all large s.

## 2. Integer coefficients from n combined cancellation conditions

Let n tend to infinity through multiples of ten, and write
$$
 d=6/5,\quad D=M=dn,\quad \mu=M+n/2,\quad
 g_k=\left\lfloor a(\mu k-k^2/2)\right\rfloor \quad(0\le k\le D).
$$
In particular $g_k\ge0$. There are integers $c_0,\ldots,c_D$ not all zero with
$$
 |c_k|\le H_n,\qquad \log_{81} H_n\le a n^2(u+o(1)),\quad
 u=\frac{d}{4(d-1)}=\frac32,                                      \tag{2}
$$
such that the following n rational equalities hold:
$$
 \sum_{k=0}^D c_k T^{g_k+E_{j-k}}=0,\qquad M\le j<M+n.           \tag{3}
$$
To prove this, the exponents in row j differ from $aj^2/2+a(\mu-j)k$ by $O(n)$ uniformly over its columns. Their spread $R_j$ is at most $aD|\mu-j|+O(n)$. Subtract the least exponent, and clear the remaining denominator by $81^{R_j}$ (use the actual integer spread). All row entries are then positive integers at most $81^{R_j}$. The image of the box $\{0,\ldots,H\}^{D+1}$ has at most
$$
 [2(D+1)H]^n81^{\sum R_j}
$$
distinct row vectors for $H\ge1$. Since $\sum R_j\le aDn^2/4+O(n^2)$, an integer H with
$$
 \log_{81} H>\frac{\sum R_j+n\log_{81}(2(D+1))}{D+1-n}
$$
can be chosen to satisfy (2). The box has more elements than its image. Subtract two with identical image to obtain (3).

Set $V(Y)=\sum_{k=0}^D c_k T^{g_k}Y^k$ and let $U(Y)$ consist of the coefficients of $V(Y)F(Y)$ of degrees below M. The polynomial V is nonzero. By (3) the series $VF-U$ has no terms below degree $M+n$. No exact first nonzero coefficient or nonvanishing value of this series is assumed.

## 3. Rationality forces many exact real identities

Take every multiple s of r satisfying
$$
 46/5\le\sigma=s/n\le156/5.
$$
For all sufficiently large n, we claim the exact rational identity
$$
 (\xi-P_s)V(y_s)=T^{E_s}U(y_s),\qquad y_s=T^{as}.                \tag{4}
$$
Indeed the difference, interpreted in $\mathbb Q_2$ by (1), equals $T^{E_s}(VF-U)(y_s)$. Its terms at degrees $j\ge M+n$ have exponents
$$
 E_s+asj+g_k+E_{j-k}
 = a[(s+j)^2/2+(\mu-j)k]+O(j+n).
$$
This bound is uniform over $0\le k\le D$, $j\ge M+n$, and the entire s interval. For a lower bound in the main term take $k=D$, since $\mu<j$. The quadratic in j has derivative $s+j-D\gg n$ throughout this range, so even after subtracting a fixed constant times $j+n$ its minimum occurs at $j=M+n$. All $c_k$ are integers. The 2-adic valuation of the difference is therefore at least
$$
 6a n^2[(\sigma+d+1)^2/2-d/2]-O(n).                             \tag{5}
$$

An ordinary common denominator for the difference in (4) is $B_0 81^K$ with
$$
 K\le a n^2[(\sigma+d)^2/2+d/2]+O(n).                            \tag{6}
$$
To check this, for a term of $T^{E_s}U(y_s)$ use the same exponent formula with $j<M$ and $k\le\min(j,D)$. The inequalities
$$
 (s+j)^2/2+(M-j)k\le(s+M)^2/2,\qquad (n/2)k\le nD/2
$$
give (6). On the other side the largest exponent is bounded by $E_{s-1}+g_D+asD$, since $g_k+ask$ is nondecreasing for $k\le D$. With $M=D$ this gives the same (6). All these exponents are nonnegative. Take K as the maximum actual exponent. In the real embedding $P_s$ is bounded, $|V(y_s)|\le(D+1)H_n$ and $|U(y_s)|\le M(D+1)H_n$. Thus after clearing, the integer has absolute value at most $81^{K+a n^2(u+o(1))}$. Its denominator multiplier is odd and preserves (5).

Put $\rho=\log_{81}64$. The p-adic lower bound on a nonzero integer's real absolute value exceeds this upper bound because
$$
 \rho[(\sigma+d+1)^2/2-d/2]-[(\sigma+d)^2/2+d/2+u]>0.             \tag{7}
$$
This concave quadratic has a uniform positive margin on the whole interval. Replacing $\rho$ by $88/93$ gives endpoint margins $1469/310$ and $227/930$, and $64^{93}>81^{88}$. Hence the integer is zero for every s in the range. This proves (4) without presupposing $V(y_s)\ne0$.

## 4. A geometric grid cannot support the forced smallness

In the real embedding (4) and Section 1 give
$$
 |V(y_s)|\ll M(D+1)H_n T^{E_s}.                                 \tag{8}
$$
The grid is positive with fixed successive ratio $\vartheta=T^{ar}=T^{9S}<1$. Choose $1<h<\vartheta^{-1/2}$. The closed intervals $[y_s/h,hy_s]$ are disjoint. At most D of them contain a modulus of a complex root of V, counted with or without multiplicity. There are at least $22n/r-1>D$ grid points for large n when $r\le18$. Select a grid point y without such a root. For every root $\zeta$,
$$
 |y-\zeta|\ge c(y+|\zeta|),\qquad c=(h-1)/(h+1)>0 .
$$
Multiplying over roots and expanding elementary symmetric functions gives $|V(y)|\ge c^D |c_k| T^{g_k}y^k$ for every k. This also holds for a constant polynomial. Choose any nonzero coefficient, which has $|c_k|\ge1$. Since $g_k+ask\le g_D+asD$,
$$
 |V(y)|\ge c^D T^{a n^2[(d+1/2+\sigma)d-d^2/2]+O(1)}.           \tag{9}
$$
The real upper bound (8) is strictly smaller for large n. Indeed with $\delta=1-\rho$ the exponent margin is
$$
 \delta[\sigma^2/2-(d+1/2+\sigma)d+d^2/2]-u>0.                   \tag{10}
$$
Here $\delta>1/19$ by $64^{19}<81^{18}$, the bracket increases for $\sigma>d$, and at $\sigma=46/5$ the lower bound on the margin is $73/950$. The terms $\log c^D$, the logarithms of the polynomial factors, the linear terms in $E_s$ and the $o(n^2)$ from (2) are absorbed by the strict margin. Equations (8) and (9) now contradict each other. This proves irrationality.

A finite steering prefix multiplies the tail value at its updated height by a nonzero rational and adds a rational partial sum. The context from L-9407 is also a rational affine function with nonzero multiplier. Neither operation can turn the irrational tail into an ordinary integer.

**Scope.** The proof uses both completions and first proves that a rational 2-adic limit would be *different* from the real limit. The later identities hold in both embeddings only after an ordinary integer is proved zero. The grid count in Section 4 is a sufficient condition; periods above eighteen and arbitrary aperiodic directives are not decided by that count.
