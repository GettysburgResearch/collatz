# Late quadratic event clocks with an unrestricted earlier path

**Written finite-source theorem.** Let $x$ be a nonnegative even ordinary shortcut source, $t_j$ the time of even input $j$ starting with $t_0=0$, $u_j=t_j-j$, and $p_j=2^{t_j}/3^{u_j}$. Put $C(j)=j(j-1)/2$, $U_j=bj+hC(j)$, $T_j=j+U_j$ and $a_j=2^{T_j}/3^{U_j}$, with fixed integers $b\ge0,h\ge1$. Suppose $u_j=U_j$ for $m\le j\le K$. All $u_j$ before $m$ are unrestricted subject to being actual event clocks. For any $n\ge1$ put
$$ d=n(b+1+h(n+m)),\quad W=d+T_{n+m+1},\quad H=(n+m+1)2^n(2\cdot3^b)^{n+m}3^{h(C(m)+n(n+m))}. $$
If $T_K>W$, then
$$ \boxed{\quad 2^W\le(x+2+2^{m+1})H.\quad} \tag{1} $$
This uses the original source size on the right, even if the first $m$ events have a completely different shape. In particular no ordinary integer source can agree on infinitely many intervals $[m,K]$, $m\to\infty$, with $K\ge(13/5)m$. Both $b,h$ are fixed for this asymptotic consequence. The finite test (1) also works with varying parameters.

**Proof.** Use the integral coefficients $B_k$ for general $m,n$ of `FINITE_PADE_KERNEL.md` and set $B=\sum B_k$, $A=\sum_k B_k\sum_{j\le m+k}a_j$. Formula `PadeIntegral.weight_factor` gives
$$3^{U_m}\mid B_k,\qquad v_2(B_k)=(n-k)(b+1+h(n+m)).$$
Thus $B$ is odd and $3^{U_m}\mid B$. For $y=-(x+1)$ put
$$y'=y-\sum_{j<m}(p_j-a_j).$$
Both $u_j$ and $U_j$ for $j<m$ are at most $U_m$. Every denominator in $y'$ divides $3^{U_m}$, so $By'-A$ is an integer. In the ordinary absolute value $0<p_j,a_j\le2^j$ and hence $1+|y'|\le x+2+2^{m+1}$. The coefficient bound $|A|,|B|\le H$ follows from the subset exponent budgets in `QUADRATIC_CLOCK_PADE.md`, with $n,m$ left free.

For the dyadic evaluation let $T=\sum_{j\ge0}a_j$ in $\mathbb Q_2$. All $p_j$ for $m\le j<K$ equal $a_j$. The native finite calibration at $K$ gives $v_2(y'-\sum_{j<K}a_j)=T_K$, since the actual state at $t_K$ is even. The omitted dyadic sum starts at $T_K$ in valuation. Therefore $v_2(y'-T)\ge T_K>W$. The same finite Padé cancellation as in `QUADRATIC_CLOCK_PADE.md` gives $v_2(BT-A)=d+T_{n+m+1}=W$ for all $n,m$. Since $B$ is odd, $By'-A$ is a nonzero integer with this exact valuation, proving (1). All uses of the infinite series can alternatively be replaced by a finite truncation at any index greater than $K+2n+m+2$.

For the numerical interval choose $n=\lfloor(87/100)m\rfloor$ and write $\gamma=\log_2 3$. As $m\to\infty$ with $h,b$ fixed the exact leading coefficients are
$$ W/(hm^2)=67507/20000+o(1),\qquad \log_2 H/(hm^2)=\gamma\,21269/10000+o(1). $$
They satisfy $67507/20000<169/50$ and $42538\gamma<67507$ (e.g. $\gamma<46/29$ since $3^{29}<2^{46}$). Thus $T_K>W$ and the right side of (1) loses only $O(m)$ further bits for fixed $x$. A positive quadratic excess remains, giving the contradiction.

**Vertical shifts and actual gap defects.** Suppose only $g_j=b+hj$ for $m\le j<K$, so $u_j=U_j+c$ on $m\le j\le K$ with $c=u_m-U_m$ of either sign. Put $c_+=\max(c,0)$ and
$$ y'=(3/2)^c\left(y-\sum_{j<m}p_j\right)+\sum_{j<m}a_j. $$
Then $2^{c_+}3^{U_m}y'$ is an integer. Indeed the first summand before multiplication has denominator dividing $3^{U_m+c}$ before application of $(3/2)^c$; the adjusted ternary denominator divides $3^{U_m}$ for either sign. The ideal sum has the same ternary bound. On the observed interval $(3/2)^cp_j=a_j$, and the native binary depth at $K$ shifts by exactly $-c$, giving $v_2(y'-\sum_{j<K}a_j)=T_K$ again. Thus $2^{c_+}(By'-A)$ is a nonzero integer of valuation $W+c_+$. Its binary clearing factor cancels in the ordinary size comparison. The full estimate is
$$ 2^W\le H(3/2)^{c_+}(x+2+2^{m+1}). \tag{2} $$
Any number of earlier actual gaps can be irregular. All negative offsets are free, and $c_+=o(m^2)$ preserves the $13/5$ exclusion with fixed $b,h$. In particular take $g_j=b+hj+e_j$ with bounded $e_j$ throughout, and with $e_j=0$ on infinitely many intervals $m\le j<K$ with $K\ge(13/5)m$. The offset $c=\sum_{j<m}e_j$ is $O(m)$, so such a trajectory cannot start at an ordinary integer. This covers independent true gap errors at the powers of three, for which the cumulative discrepancies can persist across each clean interval.

For example take $u_j=U_j+\epsilon_j$, where $\epsilon_j=0$ unless $j=3^k$, its other values are chosen independently from $\{0,1\}$, and $h\ge3$. Choosing $b\ge1$ ensures the initial gaps are nonnegative. This family can be genuinely aperiodic with positive bounded second differences. The intervals $[3^k+1,3^{k+1}-1]$ meet the criterion for all large $k$. No hypothesis controls how the discrepancies behave in the omitted intervals of the general theorem. The same argument does not cover defects at every $2^k$.

Weaver's paper 70, Theorem 4 and §8, already excludes sufficiently sparse bounded defects in growing-block schedules using a rational source obtained by reversing the clean prefix. It gives an explicit threshold depending on macroblock data. The argument above instead uses the ternary divisibility of the one-center Padé head to absorb the denominator of the corrected ordinary event sum. We do not identify the two schedule conventions or claim all sparse-defect exclusions as new. [Weaver, §8](https://rstation.ai/problems/collatz/papers/70) · [Zudilin, equations 7–10](https://arxiv.org/abs/math/0506086).
