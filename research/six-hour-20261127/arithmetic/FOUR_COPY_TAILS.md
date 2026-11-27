# Physical odd-cycle counts and sparse departures from a narrow band

Write $x_i$ for the distinct odd phases of an ordinary positive cycle, $p$ for the least odd period, $s=\min x_i$, $2^{e_i}x_{i+1}=3x_i+1$, and $\gamma=\log_2 3$. Indices are cyclic. Define

$$
 H_C=\#\{i:x_i>Cs\},\qquad V=\#\{i:e_i\ge3\}.
$$

**Written results with external analytic inputs.**

1. If $V=0$ and $\max x_i\le(16s+7)/3$, then $p\ll_\epsilon s^{\theta_0+\epsilon}$, where $\theta_0=\log_3(M)/(3\cdot256)<3/8$ and the exact integer $M$ appears in the control. Numerically $\theta_0=0.373834\ldots$. This improves the exponent $23/60$ of the independent dyadic physical-strip transfer of PR192. It applies to the bounded least-tripling-disagreement alternative. [PR192 at 75eac0c](https://github.com/GettysburgResearch/collatz/blob/75eac0cbc744469ae2886bc2f140685c484e9fe7/research/astra-sixhour-20261127/arithmetic/PHYSICAL_STRIP_TRANSFER.md)
2. Set $C=3959/1000$. On any sequence of primitive ordinary cycles with $p\to\infty$ and $(H_C+V)/p\to0$,
   $$
     \limsup\frac{\log p}{\log s}\le\frac{99999}{300000}.
   $$
   Hence if $\mu(\gamma)\le3$, there exist $c>0$ and $p_0$ such that every ordinary positive cycle of least odd period $p\ge p_0$ satisfies $H_C+V\ge cp$. Fully binary cycles in particular must spend a positive fraction of their odd period above $3.959s$. The constants are ineffective. The irrationality bound is quoted from Chudnovsky, Theorem 11.1. [arXiv:2610.28079v1, §11](https://arxiv.org/html/2610.28079v1#S11)

Both source counts use the fixed-place Subspace Theorem through Weaver's four-segment separation in the written arguments. PR200 gives the two-row equal-pair recursion and, using the quoted irrationality bound, fixed-denominator finiteness at global clock width $99/50$. Here the physical width for the second result is $4963/2500>99/50$. Its longest two return types each grow faster than $3^r$ at return length $r$. The strict saving comes from their phase frequencies together with the shorter return. The physical ceiling and the binary condition may both fail on a set of vanishing density. Weaver's Paper 181 already proves sparse occupation for unrestricted shortcut clocks, including a wider-ratio source census. The present narrow claim concerns odd sources and joint high-valuation exceptions. [PR200, four-bridge bound at 2346db2](https://github.com/GettysburgResearch/collatz/blob/2346db2d49030ef385b73e1ee3e27dcbff86d2d9/research/six-hour-20261127/cycles/FOUR_BRIDGE_BINARY_CYCLE_BOUND.md) · [Weaver, Paper 145/v1, §§4–6](https://rstation.ai/problems/collatz/papers/145/v1) · [Weaver, Paper 181/v1, §§3–4](https://rstation.ai/problems/collatz/papers/181/v1)

## The ordinary source and four interior segments

On a cyclic window starting at $x_0$ put $E_i=\sum_{j<i}e_j$. Iteration of the positive recurrence gives

$$
 E_i=i\gamma+\log_2(x_0/x_i)+c_i,\qquad
 0\le c_i\le i/(3s\log 2).
$$

In the wide case use $C_s=(16s+7)/(3s)$ and in the narrow case use $C=3959/1000$. Write $U$ for the applicable ratio and call a vertex low when $x_i\le Us$. Enclose all low dates of one window in the common strip
$$
   i\gamma+\varphi-W\le E_i\le i\gamma+\varphi,
   \qquad \varphi=\log_2(x_0/s)+b/(3s\log2).
$$
The choices $W=2419/1000$ in the wide case and $W=4963/2500$ in the narrow case exceed $\log_2 U+b/(3s\log2)$ for all sufficiently large $s$ at the depth $b=O(\log s)$ below. In particular the real phase is bounded when the origin is low. The $2(b+1)$ integer and lower-row breakpoints modulo one, their singleton phases, and the bounded integer part give $O(b)$ phase types. Within a type the full list of date choices **at every low site** is fixed.

Fix small $\eta>0$. Choose $n=256\lceil\log_3(Us)/(3\cdot256)\rceil$, $g=\lceil\eta n\rceil$, $b=4n+2g$, $h=\lfloor(1+\eta/2)\gamma n\rfloor$. Use four adjacent $n$-edge segments with starts $j=g,g+n,g+2n,g+3n$. Require their five endpoints and both ends of the window to be low. At each of those dates $E_i=i\gamma+O(1)$. For $K=E_b,u=E_j,T=E_{j+n}-u,m=K-u,v=j+n$, this gives
$$
  K-h\ge\log_2(Us),\qquad m\ge h,\qquad v\gamma\ge h,
  \qquad T\le h-c_\eta n .
$$
These hold eventually, uniformly in the low cuts. Each segment has ordinary numerator
$$
  B=\sum_{i=0}^{n-1}3^{n-1-i}2^{r_i},\qquad r_i=E_{j+i}-u.
$$
Even through a high excursion, $T-r_i\ge(n-i)\gamma-\log_2 U$, by the global floor $x_{j+i}\ge s$ and the low endpoint. Hence $B\ll n2^T$.

The ordinary source modulo $2^K$ is $-\sum_{i<b}2^{E_i}3^{-(i+1)}$. Since $2^K>Us$, a given word names at most one source in the physical interval. For a segment letter write $a=m-r_i$, $w=j+i+1$, and choose the least residues $A_i=[2^{-a}]_{3^w}$, $Z_i=[-3^{-w}]_{2^a}$. Then $2^a A_i-3^w Z_i=1$, since $1\le A_i<3^w$ and the implied quotient lies in $[0,2^a)$. Here $a>0$ by the final guard. Set $A=\sum 3^{n-1-i}A_i$, $Z=\sum2^{r_i}Z_i$. The segment contributes $Z/2^m$ to the normalized source and satisfies $2^m A-3^v Z=B$, $0\le A<n3^v$, $0\le Z<n2^m$.

Condition on the phase type, the cut dates, and all the outside or dirty data specified below. In each segment take the paths admitting at least one actual witness in that environment, so the preceding numerator estimate holds for **each path separately**. Their Cartesian product contains all the true full windows. Quantize each segment contribution to $\lfloor2^h\{Z/2^m\}\rfloor\bmod2^h$. A four-sum grid collision for one fixed segment gives, for signs $+,+,-,-$, an integer $k=O(n)$ and
$$
  a_0=\sum\pm A-k3^v,\quad b_0=\sum\pm Z-k2^m,\quad
  |b_0|\le 4\cdot2^{m-h},\quad 2^ma_0-3^vb_0=\sum\pm B .
$$
The last member has absolute value $\ll n2^T\le 2^h\exp(-c'_\eta n)$. The bounds on $a_0,b_0$, and on $2^m,3^v$ above give precisely the separation of Weaver, Paper 145/v1, Lemma 4. Thus eventually every such grid collision has $\sum\pm B=0$. This use of the external theorem is ineffective. [Weaver, Lemma 4 and source counting](https://rstation.ai/problems/collatz/papers/145/v1) · [Termwise reciprocity and quantization in PR200](https://github.com/GettysburgResearch/collatz/blob/2346db2d49030ef385b73e1ee3e27dcbff86d2d9/research/six-hour-20261127/cycles/FOUR_BRIDGE_BINARY_CYCLE_BOUND.md)

Let $Q_j$ be the number of ordinary numerator four-sum collisions of the paths in segment $j$, counted with multiplicity. Finite Fourier inversion and Hölder on $\mathbb Z/2^h\mathbb Z$ bound the largest convolution atom of the four unnormalized grid counting measures by $\prod_j Q_j^{1/4}$. Each true source is in a fixed interval of normalized length at most $2^{-h}$. The four within-bin errors sum to a number in $[0,4)$ grid units, so at most six circular convolution atoms are accepted. The count for one environment is therefore at most $6\prod_j Q_j^{1/4}$.

## Three possible rows and an exact reverse decoder

In the wide case every site is low and every exponent is one or two. The two guards cost at most $2^{2g}$ choices, and the seven cut dates cost $O(1)$. Split one interior into blocks of 256 edges. Enlarge the strip separately on each block by using the rational slope $1584962/10^6\le\gamma<1584963/10^6$ and width $2420/1000$. The added width exceeds the slope replacement error $256/10^6$. Taking the same lower real intercept at the start of each block gives integer lower row $L_i$ and at most three offsets $u_i$, beginning at zero. We may shift all relative dates on a segment up by a fixed constant to make every $L_i\ge0$, multiplying all four numerators by the same power of two.

For any genuine numerator equality set $P_0=P_n=0$, $P_{i+1}=3P_i+\sum_\ell\sigma_\ell 2^{r_{i,\ell}}$, with signs $+,+,-,-$ and the shifted dates. All future dates are at least $L_i$ because the actual dates strictly increase. Thus $2^{L_i}\mid 3^{n-i}P_i$, and coprimality gives $2^{L_i}\mid P_i$. Set $z_i=-P_i/2^{L_i}$. For one block, with $d_i=L_{i+1}-L_i$,
$$
  3 z_i=2^{d_i}z_{i+1}+\delta_i,\qquad
  \delta_i=2^{u_{i,1}}+2^{u_{i,2}}-2^{u_{i,3}}-2^{u_{i,4}}.
$$
A candidate predecessor offset $x$ for terminal offset $y$ must satisfy $1\le d_i+y-x\le2$.

The decoder keeps the four terminal offsets and $z_{i+1}\bmod27$. Conditional on the actual integer $z_{i+1}$, the next trit $t$ in $z_{i+1}\equiv r+27t\bmod81$ is **common to all the predecessor choices**. For each $t$, first sum predecessor upper bounds, rejecting when $2^{d_i}(r+27t)+\delta_i$ is not divisible by three and looking up the quotient modulo 27 otherwise. Then take the maximum over $t$. Start with the value one at every possible initial state and carry. This recursion bounds the number of reverse decodings of any fixed terminal four-state and actual carry, even with arbitrary initial state and carry. Sorting the two offsets of each equal-sign pair only identifies symmetric table entries while the predecessor sum retains the ordered multiplicities.

The exact program enumerates both endpoints and open cells of all local rational phase cuts. Its 1,028 intercept tests give 514 different schedules. Their maximum reverse count is $M$, with $M^8<3^{9\cdot256}$. Successive blocks may use different lower-row conventions at their common cut. Conditional on the actual absolute signed $P_i$ and four terminal dates, the appropriate normalized incoming integer for each preceding block is fixed. Hence multiplication of the uniform bounds is valid without equating the two representations. Starting at $P_n=0$ and the fixed final four dates gives $Q_j\le M^{n/256}$. The source count is at most $O(b)2^{2g}M^{n/256}$. Letting $\eta\downarrow0$ gives the first result.

## Two rows and rare high or nonbinary sites

Work along a putative sequence with $q=(H_C+V)/p\to0$. The minimum tends to infinity, since a bounded integer minimum supplies only finitely many forward orbits. At most $7H_C$ origins have a high mandatory cut. Cyclic averaging shows that all but $O(\sqrt q\,p)$ origins have at most $O(\sqrt q\,b)$ high vertices and high-valuation edges in their window, with the empty mask used for $q=0$. Thus at least $p/2$ distinct sources are available eventually, regardless of how high individual excursions rise.

In the four interiors mark both adjacent edges of every high vertex, and mark each edge with $e_i\ge3$. Also mark the two guards. The outer endpoints of each maximal marked run are low by construction, including the compulsory low vertices at the segment cuts. There are $o(b)$ marked interior edges and at most $2g+o(b)$ marked edges in all. Record the interior mask at cost $\exp(o(b))$. At each endpoint of a marked run, record its date, with $O(1)$ possibilities from the low strip. Over a marked run of $d$ edges the sum of the exponents is at most $\gamma d+\log_2 C+d/(3s\log2)$, because both endpoints are low. The combined exponent on the $D$ marked edges is at most $5D+O(1)$. The compositions into positive exponents, including the guards, cost at most $2^{5D+O(1)}$. This fixes the absolute ordinary date of **every** marked departure in every copy. The number of environments, including the real phase and the seven cuts, is consequently $\exp(O(\eta b)+o(b))$.

Use $F_i=\lfloor i\gamma+\varphi\rfloor$, $f_i=\{i\gamma+\varphi\}$, and write $E_i=F_i-z_i$ at a low site. Here $z_i\in\{0,1\}$ and $z_i=0$ is forced for $f_i>4963/2500-1$. Since marked dates are fixed individually, their four signed powers cancel. At any remaining departure, the four signed powers are a common power of two times an integer between $-2$ and 2, using one extra power of two if the bottom date is negative. Reading $\sum\pm B=0$ modulo three from the last letter backwards forces every signed digit to vanish in turn. Thus each unmarked departure has equal unordered bit pairs on the two sides. A clean terminal cut bit absent from $B$ is either already fixed or may be counted freely by a bounded factor per component.

At single-bit states there are six ordered equal-pair quadruples. Aggregate their counts into three coordinates $(x,y,z)$ according as the common sum is 0, 1 or 2, with $y$ denoting the sum over the four middle configurations. If $F_{i+1}-F_i=1$, admissibility of binary valuations makes the four lowering bits weakly decrease coordinatewise and the update is $(x+y+z,y+4z,z)$. If $F_{i+1}-F_i=2$, they weakly increase and the update is $(x,4x+y,x+y+z)$. A forced site projects onto $(x,0,0)$. These are precisely the two-row updates of PR200 cited above. The surviving four-copy paths between successive forced sites therefore multiply by a scalar $A_r$.

Write $\alpha=\gamma-1$. The forced starting phases with first return $r$ form finite unions of intervals cut at $\{-j\alpha\}$ and $\{4963/2500-1-j\alpha\}$, $0\le j\le147$. Boundaries are tested separately and have zero limiting frequency. On every phase a forced site occurs within 147 transitions. The certificate proves that the labeled cuts have one order throughout the rational bracket $58496250/10^8<\alpha<58496251/10^8$. In particular the return measures are affine in $\alpha$ on that bracket. The three possibilities are

| Return $r$ | Upper bound on $1000\log_3 A_r$ | Phase measure at lower slope | Phase measure at upper slope |
|---:|---:|---:|---:|
| 53 | 52922 | 943/80000 | 1178697/100000000 |
| 94 | 94129 | 51/40000 | 63797/50000000 |
| 147 | 147410 | 139/80000 | 173709/100000000 |

The full scalar integers, cut tests, and power comparisons are in the control. The measure-weighted return lengths sum to one at both slope endpoints. The measure-weighted upper bounds on $\log_3 A_r$ are $39998297/40000000$ and $1999914839/2000000000$, both strictly below $99999/100000$. They bound the intervening slope by affinity. Irrational rotation visits each of these finitely many intervals with its length as asymptotic frequency, uniformly in the initial phase, by the geometric-sum proof of equidistribution and interval approximation. Rotation cannot revisit a given boundary within an orbit, so finitely many such hits cost $O(1)$.

For one $n$-edge segment, discard all returns touching marked edges or its two ends. The remaining clean components have bounded incomplete pieces, at most $2\cdot147+2$ edges per component, and each edge admits at most $2^4$ ordered binary choices. They cost $\exp(o(b))$. Multiply the $A_r\ge1$ over the retained complete returns, and enlarge to all complete returns of the full phase schedule inside this segment. By the uniform frequencies just computed,
$$
 Q_j\le\exp(o(b))\,3^{(99999/100000+o(1))n}.
$$
The $o(b)$ terms include the sparse mask even if its locations are chosen using the orbit. The count of $p/2$ actual sources now gives the second source exponent after letting $\eta\downarrow0$.

Finally the cycle product gives $0<(\sum e_i)/p-\gamma\le1/(3s\log2)$. If $\mu(\gamma)\le3$, reducing this rational denominator gives $s\ll_\epsilon p^{3+\epsilon}$. The strict saving in the second estimate excludes any sequence with the asserted vanishing fraction, proving the positive-density statement by contradiction. This leaves the wide bounded branch open, since its demonstrated exponent exceeds one third and a positive fraction of its odd sites can lie between $3.959s$ and its ceiling. The first-crossing alternative is outside these hypotheses.

[Exact checker](check_four_copy_tails.py) · [Exact output](FOUR_COPY_CONTROLS.json) · [Normalized carry kernel](ReverseEnergy.lean)
