# A two-prime coefficient bound excludes all stack periods through 237

**PROPOSED.** Every native positive-increment stack word of period $1\le r\le237$ has irrational 2-adic value, for every initial height and after any finite positive steering prefix. We strengthen the [combined-moment proof](PROOF.md) using divisibility of its first nonzero coefficient, a bound for the entire real tail after cancellation, and a weighted count of the possible root moduli. The proof fixes r and the word before letting n tend to infinity. All constants implicit in error terms can depend on those fixed data.

Use the setup of Sections 1–3 of [the previous proof](PROOF.md) with $d=5$, $D=M=5n$, $\mu=M+n/2$, and even n. In particular $E_j=aj^2/2+bj+u_j$, with $u_j$ bounded periodic, $a=9S/r$, and $E_{j+1}-E_j=9m_{j+1}+1$ strictly increasing. The same box argument provides a nonzero vector of integers with
$$
 \log_{81}H_n\le a n^2(u+o(1)),\qquad u=\frac5{16},
$$
annihilating the n rows $M\le j<M+n$. The exponents are $g_k=\lfloor a(\mu k-k^2/2)\rfloor$.

## 1. Both primes divide the first nonzero coefficient deeply

Write $k_0=\min\{k:c_k\ne0\}$. Then
$$
 v_2(c_{k_0})\ge6a n^2/8-O(n),\qquad
 v_3(c_{k_0})\ge4a n^2/8-O(n).                                  \tag{1}
$$
For prime 2 consider row costs
$$
 f_j(k)=v_2(c_k)/6+g_k+E_{j-k}
$$
on the nonzero columns. Each row has at least two minimizing indices, since its weighted rational terms sum to zero. From one row to the next the increment $f_{j+1}(k)-f_j(k)=E_{j+1-k}-E_{j-k}$ strictly decreases in k. Hence the largest minimizing index in row j is at most the smallest minimizing index in row $j+1$: otherwise a later smaller index would lose strictly to the earlier larger one. In particular the row maxima strictly increase.

Traverse $j=M+i$, $0\le i<n/2$. At the first row let v denote $k_0$, and thereafter let v be the previous row's largest minimizer. Write w for the current largest minimizer. In every case $w-v\ge1$ and $f_j(v)\ge f_j(w)$. The quadratic-periodic formula and the floor error in $g_k$ give, uniformly,
$$
 \frac{v_2(c_v)-v_2(c_w)}6
 \ge a(\mu-j)(w-v)-|b|(w-v)-O(1).
$$
The intervals $(v,w]$ in this traversal are disjoint, so the total $|b|$ error is $O(D)=O(n)$. The positive slopes $\mu-j=n/2-i$ sum to $n^2/8+O(n)$. Telescoping and nonnegativity of the last valuation prove the first inequality in (1).

For prime 3 use $f_j(k)=v_3(c_k)/4-g_k-E_{j-k}$ and traverse $j=M+n-1-i$, $0\le i<n/2$. The increment on passing from j to $j-1$ is $E_{j-k}-E_{j-1-k}$, again strictly decreasing in k. The same minimizer argument now has slopes $j-\mu=n/2-1-i\ge0$, with the same leading sum. This proves the second inequality. The two integer divisibilities together imply, for $\rho=\log_{81}64$,
$$
 \log_{81}|c_{k_0}|\ge a n^2(1+\rho)/8-O(n).
$$

## 2. The exact identity on the new grid

Assume the 2-adic limit equals a rational $\xi$. As in Section 1 of the previous proof, $\xi\ne\Theta_R$. Choose all multiples s of r with $1\le\sigma=s/n\le243/10$. Equations (5)–(6) of that proof hold verbatim with $d=5$. They force the rational identity $(\xi-P_s)V(y_s)=T^{E_s}U(y_s)$ at every such $y_s=T^{as}$, because
$$
 p(\sigma)=\rho[(\sigma+d+1)^2/2-d/2]-[(\sigma+d)^2/2+d/2+u]>0.
$$
Indeed $94639/100000<\rho<94640/100000$ by exact integer powers. Replacing $\rho$ by the lower fraction yields positive endpoint values $0.00808$ and $0.01212255$, and the quadratic is concave. This justifies simultaneous rational equality before using the real embedding.

Now subtract the real identity $\Theta_R=P_s+T^{E_s}F(y_s)$ from the rational one after multiplication by V. This gives
$$
 (\xi-\Theta_R)V(y_s)=-T^{E_s}(VF-U)(y_s).
$$
The real power series on the right starts at degree $M+n$. The same exponent lower bound used for its 2-adic valuation gives, now using $0<T<1$ in the real embedding,
$$
 |V(y_s)|\le 81^{a n^2(u+o(1))}
 T^{a n^2[(\sigma+d+1)^2/2-d/2]-O(n)}.                         \tag{2}
$$
More explicitly the lower bound for an individual exponent at degree $j\ge M+n$ is $a[(s+j)^2/2+(\mu-j)D]-O(j+n)$. As j increases from $M+n$ this grows by at least a fixed positive multiple of n per step for large n, even with the subtracted linear error chosen consistently. Summing the geometric tail and the $D+1$ columns costs only a polynomial factor. All $o(1)$ terms in this note are uniform on the chosen compact interval of $\sigma$.

## 3. Jensen's inequality saves grid points

Write $V(Y)=T^{g_{k_0}}Y^{k_0} W(Y)$, so $W(0)=c_{k_0}$. Put $R=T^{-an/2}>1$. On $|Y|=R$, every term of W has absolute value at most $T^{-1}H_n$: for $k\ge k_0$,
$$
 g_k-g_{k_0}-(an/2)(k-k_0)
 =a\,[D-(k+k_0)/2](k-k_0)+O(1)\ge-1.
$$
The polynomial form of Jensen's formula, or the circle mean of $\log|Y-\zeta|$ applied to its factorization, gives
$$
 \sum_{W(\zeta)=0}\log^+(R/|\zeta|)
 \le\log\frac{(D+1)H_n}{T|c_{k_0}|}
 \le a n^2\log(81)(v+o(1)),\qquad v=u-(1+\rho)/8.             \tag{3}
$$
Zeros are counted with multiplicity. None is zero. This applies also to a constant W.

Choose $1<h<T^{-ar/2}$ so the intervals $[y_s/h,hy_s]$ are disjoint. If each contains a root modulus of W, those distinct roots alone contribute to (3) at least
$$
 \sum_s[an(\sigma+1/2)\log(1/T)-\log h]
 =\frac{a n^2\log(1/T)}r (b_1-b_0)
       ((b_1+b_0)/2+1/2)+O(n),
$$
where $b_0=1$, $b_1=243/10$. For $r\le237$ this violates (3). Indeed using $1-\rho>536/10000$ and $v<0.06920125$ gives
$$
 \frac{1-\rho}{v}(b_1-b_0)((b_1+b_0)/2+1/2)>237.31 .
$$
Thus at least one grid point is multiplicatively separated from every nonzero root of V. At that point, with $c=(h-1)/(h+1)$, the root product lower bound of the previous proof gives
$$
 |V(y_s)|\ge c^D |c_{k_0}|T^{g_{k_0}+as k_0}
 \ge c^D |c_{k_0}| T^{a n^2[(d+1/2+\sigma)d-d^2/2]+O(1)}.
$$
This contradicts (2): after cancellation the strict exponent margin needed is
$$
 (1-\rho)(\sigma+1)^2/2-v>0 .
$$
It holds even at $\sigma=1$. The contradiction gives the claimed irrationality, and the nonzero rational finite-prefix and context transfer from the previous proof applies.

**Boundary.** This is a sufficient uniform period range. The argument does not give an ordinary realization at any larger period. No unbounded-period or general growing-directive theorem follows from the displayed constants.
