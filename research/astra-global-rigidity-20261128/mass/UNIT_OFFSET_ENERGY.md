# Unit real bins at every ternary depth

Let iid positive gaps have probability $2^{-e}$, put $S_j=\sum_{i\le j}e_i$, $A_j=3^j2^{-S_j}$, $R_j=\sum_{i\le j}A_i/3$, and let $(R,Z)$ be the real and ternary limits. Write $J_k=[k,k+1)$ for $k\ge0$. Define
\[
    g_k\,dm_3=\Pr(R\in J_k,Z\in dz),\qquad
    G_{j,k}(z)=3^j\Pr(R_j\in J_k,Z\equiv z\pmod {3^j})
\]
with Haar probability $m_3$. All real bins below have **absolute width one**. The following estimates concern the complete geometric-gap law. The final section gives an actual positive-ordinary finite-clock estimate.

## Stationary all-moment estimate

For each fixed $1<q<\infty$ and dyadic integer $B\ge1$,
\[
  \sum_{B\le k<2B}\int g_k^q\,dm_3
         \ll_q B^{-1}(\log(eB))^{q-1}.
                                                                  \tag{1}
\]
The bin $k=0$ has all finite moments as well. Consequently the sum over **all** real unit bins is finite for every such $q$. Aggregating the bins before raising to $q$ gives the unrestricted ternary density with its different, critical exponent two. Weaver's stationary shell theorem bounds the aggregated shell's $L^q$ norm by $C_q B^{1-2/q}(\log(eB))^{1-1/q}$. We use its input and refinement argument here. [Weaver, Paper 9/v2, Appendix B, (B2), (B4)–(B10), Appendix C, (C3)](https://rstation.ai/problems/collatz/papers/9).

Choose a function $F_k$ equal to one on $[k,k+1]$, vanishing outside $[k-1,k+2]$, linear in between and bounded by one. The vector $F=(F_k)_{B\le k<2B}$ has uniformly bounded $\ell^1$ norm and $\ell^1$ Lipschitz constant. Write $D_n$ for the vector of depth-$n$ ternary cylinder densities with marks $F_k(R)$. Its $L^1(m_3\times\#)$ norm is $O(1/B)$ by the scalar tail $\Pr(R>b)\ll1/(1+b)$ from (B8); bounded $B$ require only total mass. The last ternary digits are irrelevant for the depth-$n$ congruence after the first $n$ gaps.

We record a decomposition for $n\ge1$. The part $U_n$ from $A_n\le1$ and $R-R_n\le1$ satisfies $\|U_n\|_\infty\ll n$. Fix a total $s=S_n$. At each ternary residue the compatible real prefixes are separated by $A=3^n2^{-s}$, by fixed-total inverse-word injectivity. Each word contributes precisely $A$ to the cylinder density before insertion of its bounded mark. For a selected bin the prefix is thus restricted to an interval of length four and its eligible weight is at most $4+A\le5$. There are $O(n)$ totals with $s\le8n$. The total density from $s>8n$ is at most $3^n\Pr(S_n>8n)\le[6(3/4)^8]^n$. These bounds also hold after inserting the independent tail event defining $U_n$. The complementary part $V_n=D_n-U_n$ satisfies
\[
       \|V_n\|_1\ll e^{-cn},\qquad \|V_n\|_\infty\ll Bn.
\]
Indeed $R-R_n=A_nR'$ with an independent suffix and $\mathbb E A_n^a=\rho_a^n$, $\mathbb E(R')^a<\infty$ for any fixed $0<a<1$, where $\rho_a=3^a/(2^{1+a}-1)<1$. The bounded overlap controls the sum over bins on the exceptional event. For its supremum, all selected prefixes have $R_n\le 2B+2$, hence $A_n\le3R_n\le6B+6$. The same fixed-total spacing gives $O(B)$ per total and the preceding geometric tail treats $s>8n$.

For each $L>0$, the vector refinement satisfies
\[
       \|D_{n+1}-D_n\|_1
        \ll_L B^{-1}(1+n)^{-L}+O(e^{-cn}) \qquad(n\ge2).            \tag{2}
\]
Here and below the $L^1$ norm includes counting measure on the bins. Freeze $F(R)$ at $R_m$, $m=\lfloor n/2\rfloor$. At both ternary levels the sum of the absolute measure errors is at most $\mathbb E\|F(R)-F(R_m)\|_1\ll \mathbb E\min(1,A_mR')\ll e^{-cm}$. Given the first $m$ gaps, the remaining depth refinement is the translated and scaled original ternary refinement from level $n-m$ to $n+1-m$, with $L^1$ error $O_L((1+n)^{-L})$ by the ternary mixing input used in (B5), (B10) of the cited paper. The frozen vector multiplies this norm by $\|F(R_m)\|_1$. Its expectation is $O(1/B)$ since $R_m\le R$ and for $B\ge2$ its support requires $R_m\ge B-1$. This proves (2).

Take $N=\lceil K_q\log(eB)\rceil$ large enough in terms of $q$ and the fixed exponential rate. At depth $N$, supremum times mass interpolation for $U_N$ and $V_N$ gives
\[
      \|D_N\|_q\ll_q B^{-1/q}N^{1-1/q}.
\]
For $n\ge N$ the good difference $U_{n+1}-U_n$ has supremum $O(n)$ and $L^1$ bounded by (2) plus $O(e^{-cn})$. The exceptional pieces have supremum $O(Bn)$ and exponentially small mass. Therefore
\[
 \|D_{n+1}-D_n\|_q
 \ll_{q,L} n^{1-1/q}(B^{-1}n^{-L})^{1/q}
                    +(Bn)^{1-1/q}O_q(e^{-c'n/q}).
\]
Choose $L>3q$ and sum these bounds for $n\ge N$. They cost at most $O_q(B^{-1/q}N^{1-1/q})$, increasing $K_q$ for the exponential terms. The martingale limit gives the vector density for the tents, which dominates $(g_k)$. The same bound with bounded $B$ and a single tent covers $k=0$. This proves (1).

## Finite, unsmoothed offsets have critical exponent two

There is an absolute constant such that
\[
                 \sup_{j\ge0}\sum_{k\ge0}\int G_{j,k}^2\,dm_3<\infty .
                                                                      \tag{3}
\]
The same bound holds with each fixed $1\le q\le2$ in place of two, by interpolation and conservation of unit mass. For $q>2$ the left side at depth $j$ is at least
\[
         \biggl(\frac{3^{q-1}}{2^q-1}\biggr)^j-1,                   \tag{4}
\]
which grows exponentially. The finite intercept uses no random real continuation; the stationary law in (1) retains that continuation.

For $A_j\le1$, use an independent event $R'\le1$ of fixed positive probability. Then $R_j\in J_k$ forces $R\in[k,k+2]$, and the depth-$j$ residue is already determined. The corresponding part of $G_{j,k}$ is bounded by a fixed constant times the conditional expectation of the stationary ternary density with $R\in[k,k+2]$. One may replace the closed interval by three neighboring bins. Jensen and (1) bound its squared norm summed in $k$, uniformly in $j$.

For the remaining totals put $a_s=3^j2^{-s}>1$ and use a single odd integer representative $z$ of the chosen ternary residue. Every compatible word then has a signed odd integer origin $x_s$ and $R_j=z-a_s x_s$. Words at a common total have separation at least $a_s$ by injectivity. For $s<t$ two words have intercept difference $a_t(x_t-2^{t-s}x_s)$, up to sign. The parenthesized integer is odd, so the separation is at least $a_t>1$. Consequently **all high-multiplier words together** place at most one word in a given real-unit bin and ternary cylinder. This gives the exact identity, writing $G^>_{j,k}$ for their part,
\[
   \int (G^>_{j,k})^q\,dm_3
     =\mathbb E[A_j^{q-1};\ A_j>1,\ R_j\in J_k],\qquad q\ge1.       \tag{4a}
\]
At $q=2$ the sum is at most $\mathbb E A_j=1$, proving (3). For $q>2$ it is bounded below by $\mathbb E A_j^{q-1}-1$, proving (4).

## The exact unit defect at the critical moment

As a vector on Haar ternary space times the counting measure on the real bins, the part $G^\le_j$ from $A_j\le1$ converges strongly to $g=(g_k)$ in $L^q$ for every finite $1\le q<\infty$. To see this, its preceding envelope at $k$ is a constant times the depth-$j$ conditional expectation of $g_k+g_{k+1}+g_{k+2}$. By (1) and contraction in $L^q$, its $q$-moment tail beyond any bin cutoff tends to zero uniformly in $j$. For $q=1$ use conservation of stationary mass and bounded overlap. For each fixed bin $k$, the $L^1$ difference from the conditional expectation of $g_k$ tends to zero. Indeed $A_j\to0$ almost surely and $R_j\to R$ with $R$ nonatomic. An atom of largest positive mass at $r>0$ would force each of the distinct inverse values $(2^e r-1)/3$ to have that same maximal mass by stationarity; zero itself is not attained. The finite-bin indicator therefore converges in $L^1$. Conditional averaging over the depth-$j$ residue cannot enlarge this discrepancy. Martingale convergence handles the conditional expectation of $g_k$ itself. For $q>1$, interpolate by the preceding uniform bound at a moment above $q$, then use the uniform tails.

For $q<2$ the full vector $G_j$ also converges strongly in $L^q$. For $1<q<2$ the high contribution in (4a) is at most $(\mathbb E A_1^{q-1})^j$ with base strictly less than one. For $q=1$ it is bounded by $\Pr(A_j>1)\to0$. For $q>2$ the full $q$-moment sum is asymptotic to $(\mathbb E A_1^{q-1})^j$, by (4a), the bounded low-multiplier norm and the triangle inequality.

At $q=2$ there is instead an exact limiting defect:
\[
           \lim_{j\to\infty}\sum_k\int G_{j,k}^2\,dm_3
                       = 1+\sum_k\int g_k^2\,dm_3 .                   \tag{4b}
\]
The unit escaping every finite set of real bins has an explicit location. Tilt the product law by the density $A_j$ of mean one. Under this compatible tilt the iid gaps have probabilities $3/4^e$, mean $4/3$ and variance $4/9$. Put $v=\log3-(4/3)\log2>0$ and $\sigma=(2/3)\log2$. The tilted law of large numbers gives $j^{-1}\log A_j\to v$. Thus the squared high-sector masses in (4a), which are precisely the tilted probabilities with $A_j>1$, have total tending to one. Their projection by
\[
               k\longmapsto \frac{\log(1+k)-v j}{\sigma\sqrt j}
\]
converges weakly to the standard normal law. Indeed $R_j/A_j\ge1/3$ and is one third times a reversed sum of successive products of reciprocal multipliers, starting with the empty product. Under the tilted law such a multiplier has $\delta$-moment $\mathbb E A_1^{1-\delta}<1$ for $0<\delta<1$, so the whole sum has uniformly bounded $\delta$-moment by subadditivity. Therefore $\log(R_j/A_j)=O_{\Pr}(1)$, and the claim follows by the iid central limit theorem for $\log A_j$. Passing from $R_j$ to $1+\lfloor R_j\rfloor$ has negligible effect there. The low-sector energy is tight in $k$, so its cross term with the high sector tends to zero by splitting at a fixed cutoff and applying Cauchy–Schwarz. This proves (4b). The same split permits replacing the high squared sector by the full squared energy on sets of bins above any $K_j\to\infty$ satisfying $K_j\le\exp((v-\epsilon)j)$ for some fixed $0<\epsilon<v$. This is an exact loss of finite-prefix quadratic mass at large absolute intercepts, within the reference arithmetic itself.

## Actual integer crops

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odds and $b_j(x)=\prod_{i<j}3U^ix/(3U^ix+1)$. For a true word $y=U^j x$, its forward real intercept is $r=y(1-b_j(x))$. Its reverse gap order has the preceding $R_j=r$ exactly. Put $I_Y=[Y,\lambda Y]$ for fixed $\lambda>1$. For any $j\le\log_3Y$, the whole column is
\[
 H_{j,k}(y)=y\sum_{x:U^j x=y}\frac{b_j(x)}x1_{\{r\in J_k\}}
               =G_{j,k}(y).
\]
Indeed $A_j=yb_j(x)/x$, and $R_j\le(3/2)^j-1<Y$ makes every compatible word at $y$ positive. The period $3^j$ fits in a constant extension of the physical octave, also among odd representatives. Thus for any convex weights $p_j$ on this clock range, (3) yields
\[
       \frac1Y\sum_{y\in I_Y\,{\rm odd}}\sum_k
                     \biggl(\sum_j p_j H_{j,k}(y)\biggr)^2\ll_\lambda1.
                                                                    \tag{5}
\]
If the clock is unrestricted, crop the actual sources to $x\in[X,2X]$, $X\ge Y$, and restrict targets to nonperiodic odds. For any such fixed $j$ the cell sum $H^{[X,2X]}_{j,k}(y)$ is $O_\lambda(1)$ uniformly. The first-arrival word is simple, and so the source-qualified uniform reciprocal packing gives $b_j\ge c_0>0$. Consequently the compatible $A_j=yb_j/x$ belong to $[c_0Y/(2X),\lambda Y/X]$. There are $O_\lambda(1)$ division totals in this dyadic range, and each contributes at most $1+A_j=O_\lambda(1)$ by unit-bin spacing. Summing cell masses costs at most $\sum_{x\in[X,2X]}\lambda Y/x=O_\lambda(Y)$ by the deterministic image of each $x$. Hence (5) also holds with these cropped columns, over **any** convex clock average including arbitrarily large $j$. [Uniform simple-path packing, PR212 at 31311116](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md).

The genuine stationary integer fibre results from a supplied all-clock first-arrival limit. Its contributing clock rows must be summed at their actual weights. A uniform estimate on averages with $\sum p_j=1$ does not bound that total. In particular a single positive true word from $m$ to $y$ places mass $A_j\ge c_0y/m$ at its *finite* exact intercept. A putative raw pointwise finite-column bound $\sum_k G_{j,k}(y)^2\ll y$ at every nonperiodic $y$ and every $j$ would already bound every such excursion by $y\ll m^2$. Passing instead to the stationary real fibre smears this finite atom by the actual real law at $m$.

There is also a cross-clock spacing calculation before stationary continuation. Take two true prefixes ending at the same positive odd $y$, with unit sources $x,x'$ and distinct clock pairs $(j,s),(j',s')$. Their real intercepts differ by $A'x'-Ax$, an integral multiple of
\[
                      g=3^{\min(j,j')}2^{-\max(s,s')}.
\]
If $s\ne s'$, the multiple is nonzero by parity. If $s=s'$ and $j\ne j'$, it is nonzero modulo three since the source multiplying the smaller power of three is a unit. Thus the distance is at least $g$. In a simple source crop $x,x'\in[X,2X]$, $y\in[Y,\lambda Y]$ this gives $g\ge (c_0Y/(2X))3^{-|j-j'|}$. For $Y\gg X$ there is a logarithmic band of distinct clocks that cannot share a unit bin, even at a selected ordinary target. The complete canonical real mark adds $A R_x$ at that prefix, and that term can exceed the separation. This spacing alone therefore does not imply the [stationary ordinary macro-strip upper](MACROSCOPIC_REAL_ENERGY.md).
