# Carry support, finite entropy, and ordinary height

**PROPOSED written deductions.** The input is one positive odd ordinary source with an injective accelerated Collatz orbit. The estimates give necessary conditions for escape. Neither universal slow growth of the canonical word nor impossibility of nontrivial cycles has been established.

## The carry partition

Write the actual equations as
$$
2^{g_i}q_{i+1}=3q_i+1,\qquad g_i\ge1,\qquad \alpha=\log_2 3 .
$$
The scalar theorem in PR182 at f94a2ae1caba9a1857feda892ee1779695eea9d2, research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md, supplies
$h_i=\sum_{t\ge0}g_{i+t}/3^{t+1}$, $1/2<h_i\le1+\log_2(q_i)/3$ and $h_{i+1}=3h_i-g_i$. Let $p_i$ be its representative modulo one in $(1/2,3/2]$, $k_i=h_i-p_i\in\mathbb N_0$ and $b_i=3p_i-p_{i+1}\in\{1,2,3\}$. Then
$$
g_i+k_{i+1}=b_i+3k_i,\qquad k_{i+1}\le3k_i+b_i-1.
$$

In particular a carry of zero persists across a digit-one edge. Cut any given canonical word $w$ at all its edges with $b_i>1$. Within each remaining component the positive carry entries form a prefix. At $0<x<1/2$ put $D=(1-x)/(1-2x)$. The weighted sum of carry vectors on a component of $\ell$ vertices is at most
$$
\sum_{j=0}^{\ell}\left(\sum_{s\ge1}x^s\right)^j\le D.
$$
Thus the partition sum with weight $x^{\sum k_i}$ is at most $D^{1+\#\{i:b_i>1\}}$. This simple estimate counts positive integer assignments along each possible prefix. Retaining the size of a carry just after zero gives a sharper result.

For $c\ge0$, set $f(0)=1$ and $f(c)=Dx^c$ for $c>0$. Then $\sum_{c\ge0}f(c)=D$ and $f(c)\ge x^c$. For $b=1,2,3$, put
$$
\lambda_b=1+D\sum_{j=1}^{b-1}x^j,\qquad \lambda=\lambda_2.
$$
An empty sum equals zero. For the operator $(T_b f)(c)=x^c\sum_{0\le t\le3c+b-1}f(t)$, positivity gives $T_b f(c)\le f(c)$ when $c>0$. At $c=0$ there is the exact equality $T_b f(0)=\lambda_b f(0)$. Hence $T_b f\le\lambda_b f$ pointwise. Also $\lambda_3=1+D(x+x^2)\le(1+Dx)^2$ since $D\ge1$. For a fixed $m$-edge canonical word $w$, applying the positive operators in chronological order to the terminal vector $c\mapsto x^c$ and summing over initial $c$ proves
$$
Z_w(x)=\sum_{\text{legal }v} x^{\sum_{i=0}^m v_i}
\le D\prod_{i<m}\lambda_{w_i}\le D\lambda^{\sum_{i<m}(w_i-1)}. \tag{1}
$$
Here legal vectors may be any subset of the vectors satisfying the displayed edge inequalities. The sum over the full edge set is itself bounded by the operator product. All upper relaxations enlarge the weighted sum. For a conditional law supported on this set, the nonnegativity of relative entropy against its normalized weights gives
$$
H(K\mid B=w)\le -\log x\,\mathbb E(\textstyle\sum K_i\mid B=w)+\log D+\sum_{i<m}\log\lambda_{w_i}. \tag{2}
$$
All logs without subscript are natural.

## Finite empirical windows

Choose $1\le m\le N/2$, let $J$ be uniform on $0,\ldots,N-m$, $L=N-m+1$, and $R=1+m(m+\log(N+1))/L$. Set $B=(b_J,\ldots,b_{J+m-1})$, $G=(g_J,\ldots,g_{J+m-1})$, $K=(k_J,\ldots,k_{J+m})$, and define $A=\mathbb E\sum B_i,\ C=\mathbb E\sum_{i<m} k_{J+i}$. These are literal contiguous windows, including the last carry.

Indeed $V_i=\log_2(q_i)-h_i\ge-1$ satisfies $V_{i+1}-V_i=\log_2(3+1/q_i)-2h_i$. Distinct positive integer states imply $\sum_{i<T}1/q_i\le1+\log T$. Summing the exact recurrence and using $p_i>1/2$ gives
$$
2\sum_{i<T}h_i\le\alpha T+O_q(1+\log(T+1)),\qquad
2\sum_{i<T}k_i\le(\alpha-1)T+O_q(1+\log(T+1)).
$$
Each index occurs in at most $m$ sampled windows. The identity $\sum_{i<m}b_{J+i}=2\sum_{i<m}p_{J+i}+p_J-p_{J+m}$ and $|p_J-p_{J+m}|<1$ therefore imply
$$
A+2C\le\alpha m+O_q(R),\qquad
\mathbb E k_{J+m}\le L^{-1}\sum_{j=0}^N k_j=O_q(1). \tag{3}
$$
The endpoint estimate uses $L\ge N/2$. The constants can depend on the original ordinary source.

Let $u$ be the unique root of $u^5+u^3-2u^2-u+1=0$ in $(0.58457,0.58458)$. The polynomial takes opposite signs there and its derivative is negative throughout that short interval, for instance by $5(0.59)^4+3(0.59)^2-4(0.58)-1<0$. At $x=u^2$, the equation gives $\lambda=1+Dx=1/u$ and $-\log x=2\log\lambda$. Define
$$
d=(\alpha-1)\log\lambda/\log3=0.285859533495646\ldots .
$$
Use $\log\lambda_{b}\le(b-1)\log\lambda$ in (2) and substitute (3). Since $G$ is determined by $B,K$, the finite empirical law satisfies
$$
H(G)\le H(B)+d\,m\log3+O_q(R). \tag{4}
$$
The run-only calculation above gives the same inequality with $d=0.313543318239\ldots$, using $x=u_0^2$ for the root of $u_0^3-2u_0^2-u_0+1=0$ in $(0.55495,0.55496)$, at which $D=1/u_0$. PR189's disjoint-edge bound gives $d=0.541528190506\ldots$.

In fact (4) holds with a **uniform additive constant** $C_q$ for all $N\ge1,\ 1\le m\le N$. When $dm\log3\ge\log(N+1)$, use $H(G)\le\log L\le\log(N+1)$. Otherwise $m=O(\log(N+1))$, so $m\le N/2$ and $R=O(1)$ for all sufficiently large $N$. Enlarge the constant for the finitely many remaining $N$.

Let $\pi_N$ be the uniform law on $q_0,\ldots,q_N$. The ordinary affine identity
$$
2^{\sum G_i}q_{J+m}=3^m q_J+
\sum_{i=0}^{m-1}3^{m-1-i}2^{\sum_{t<i}G_t}
$$
determines $q_{J+m}\bmod 3^m$ from $G$. The endpoint collision sum after reduction is at least $\exp[-H(G)]$ by grouping and Jensen. Its weight in $\pi_N$ is $L/(N+1)$, bounded below away from zero for sufficiently large $N$ if $dm\log3<\log(N+1)$. Otherwise the finite support bound gives $\operatorname{Col}_{3^m}(\pi_N)\ge1/(N+1)$. Thus for $1\le m\le N$,
$$
\operatorname{Col}_{3^m}(\pi_N)\ge c_q e^{-H(B)}3^{-dm}. \tag{5}
$$
For bounded canonical factor complexity $P_b(m)\le L_0$, $e^{-H(B)}\ge1/L_0$. A fixed rational scalar has eventually periodic canonical word, so its finite prefix and its period admit a finite $L_0$. The extension far beyond logarithmic precisions uses only finite support.

## Height and occupation along the same orbit

Let $M_N=1+\max_{i\le N}q_i$, and $\kappa=\limsup_{m\to\infty}\log P_b(m)/m$ for the original word. Then
$$
\liminf_{N\to\infty}\frac{\log M_N}{\log N}
\ge \frac{\log3}{\kappa+d\log3}. \tag{6}
$$
On any subsequence with bounded $\log M_N/\log N$, take $m=\lceil\log_3 M_N\rceil=O(\log N)$. The $L$ distinct endpoints are below $3^m$, hence $\log L\le H(G)$. Use (4) and $H(B)\le\log P_b(m)$. As $N\to\infty$, $m\to\infty$ by distinctness. A contradiction to (6) would give a bounded-ratio subsequence of exactly this type.

For $\kappa=0$ the required exponent is $1/d=3.49822161875\ldots$. For a fixed rational phase (4) also gives $M_N\gg_q (N+1)^{1/d}$ with a fixed multiplicative constant. This last estimate follows first whenever $M_N\le N^{2/d}$, where $m=O(\log N)$ uniformly, and directly for larger $M_N$. PR188 at beed685ab713923191ae40c9559bf7400298d2d3, SC2 in research/scalar-carry-cocycle-20261124/SCALAR_COCYCLE.md, gives $M_N\ll_q D_N(N+1)(1+\log M_N)^{4/3}$, where $D_N$ is the largest canonical coefficient drawup over all subintervals of this prefix. If $D_N=O(N^\eta)$ along an unbounded subsequence, the crude $q_i\le2^i q_0$ first makes $M_N$ polynomial there. Reinserting this bound gives $M_N\ll_q N^{1+\eta}(1+\log N)^{4/3}$. Combined with $\kappa=0$, any $\eta<1/d-1=2.49822161875\ldots$ forces eventual periodicity.

A stronger consequence uses PR182 R12-1 at cbec52dde5bed390a693310dd04e911033ba0cc9, research/phase-packing-round12-20261124/README.md §2. Define the full-prefix canonical coefficient $P_i=3^i/2^{\sum_{j<i}b_j}$. That theorem gives, for each clock of the same injective orbit,
$$
P_i\ge C_q\,q_i/(1+\log q_i)^{\log_3 4}.
$$
Its additional inputs are the local carry inequality and the source occupation theorem implying $\sum_i1/q_i<\infty$, so the full multiplicative correction $\prod_i(1+1/(3q_i))$ is finite. Taking the index attaining the ordinary running maximum in (6), and using $\log(1+\log y)=o(\log y)$, yields
$$
\liminf_N\frac{\log\max_{i\le N}P_i}{\log N}
\ge \frac{\log3}{\kappa+d\log3}.
$$
The interval drawup $D_N$ includes all prefixes. In particular when $\kappa=0$, a bound on either maximum of order $O(N^\eta)$ on an unbounded subsequence with $\eta<3.49822161875\ldots$ forces eventual periodicity. R12-2 already excludes every polynomial upper bound in the special critical-mean, zero-complexity branch. The present general-complexity implication permits subcritical canonical mean.

The run bound also controls a fraction of visits. For $s>0$ with $s(\kappa+d\log3)<\log3$,
$$
\limsup_N \frac{\#\{j\le N:q_j\le N^s\}}{N+1}
\le\frac{(\alpha-1)\log\lambda}{\log3/s-\kappa}. \tag{7}
$$
Use $m=\lfloor s\log_3 N\rfloor+1$ and the window cost $T=2\sum_{i=0}^m k_{J+i}+\sum(B_i-1)$. Formula (3) gives $\mathbb ET\le(\alpha-1)m+O_q(1)$. At fixed $w$, (1) implies $\sum_v u^{2\sum v_i+\sum(w_i-1)}\le D$. At $T\le tm$ there are therefore at most $D\lambda^{tm}$ configurations per canonical word. A permitted gap word determines at most one positive endpoint below $N^s$, and injectivity prevents a repeat. The number of low-cost low endpoints is $o(N)$ if $\kappa+t\log\lambda<\log3/s$. The remaining fraction is at most $(\alpha-1)/t+o(1)$ by Markov. Drop the initial $m=o(N)$ endpoints and let $t$ increase to $(\log3/s-\kappa)/\log\lambda$.

## Fixed-period refinement

For a periodic canonical word let $\beta$ be its mean, let $f_j$ be the fraction of its digits equal to $j$, and put $\delta=(\alpha-\beta)/2$. The window has $A=\beta m+O(\mathrm{period})$ and $C\le\delta m+O_{q,\mathrm{phase}}(R)$. A negative $\delta$ is inconsistent with (3) as $m\to\infty$, for example with $N\ge m^2$. Zero is excluded by irrationality of $\alpha$. Before the uniform choice of $x$, (2) gives, for each fixed $0<x<1/2$, a conditional entropy rate at most
$$
c(x)=-\delta\log x+f_2\log(1+Dx)+f_3\log(1+D(x+x^2)).
$$
The above entropy-to-height argument gives a running maximum $\gg_{q,\mathrm{phase},x} N^{\log3/c(x)}$ for every specified $x$. The following certified lower bounds use rational test values, so they require no assertion about the optimizing $x$.

| Scalar phase | Canonical period | Test $x$ | Prior PR182 R12-2 exponent | New certified lower exponent |
|---|---|---:|---:|---:|
| $7/8$ | $2,1$ | $76858/10^6$ | $6.18740345\ldots$ | $7.36$ |
| $729/1456$ | six ones, five twos, one three | $1626/10^6$ | $166.23190699\ldots$ | $181.74$ |

These bounds require an injective ordinary realization of each phase. The phase $5/8$ is the cyclic shift of $7/8$. The shape of an abstract periodic word does not establish the existence of such an ordinary realization.
