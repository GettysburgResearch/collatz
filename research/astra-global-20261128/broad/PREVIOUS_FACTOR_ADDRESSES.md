# How far back can a compressed parity prefix obtain its copies?

Let a positive ordinary shortcut path have pairwise distinct input states $x_0,\ldots,x_{T-1}$. Write $B=\log_2(x_0+1)$, $D=\log(1+T/B)$ (natural logarithm), and $c=\log_2(3/2)$. Parse its parity word into literals and copies. A copy begins at $a_i$, uses the actual earlier start $b_i<a_i$, and matches through the first discrepancy; for the final copy the end of the observed path may truncate the match. The source can overlap the destination. This includes the greedy longest-previous-factor parse, with any tie-breaking, and the greedy parse using any allowed subset of earlier positions. Emitting the first unmatched symbol as a literal is also allowed. Count literals and copies in $z$.

**Written theorem.** Along any sequence of these paths and parses with $D\to\infty$ and $z\le CD$ for a fixed $C$,
$$
 \liminf\frac1D\sum_{i\ {\rm copies}}\frac{b_i}{B+a_i}
 \;\ge\; \frac{1-c}{2c}=0.3547556\ldots . \tag{1}
$$
The same lower bound holds if one first restricts to copies with observed length $L_i\ge\delta(B+a_i)$, then takes $\delta\downarrow0$ after the liminf. In particular any parses restricted to source addresses $b_i=o(B+a_i)$ uniformly outside an initial bounded range of logarithmic time must have $z/D\to\infty$. The version with the macroscopic-length restriction is important when extrapolating from a family with varying $B$. It prevents many early, short phrases from supplying the bound.

A separate mass statement has a sharper conclusion for very old addresses. Give physical time the probability measure $d\mu=dt/[(B+t)D]$ on $[0,T)$. For a fixed $\delta>0$, choose any disjoint exact copies with $L_i\ge\delta(B+a_i)$ and $\max_i b_i/(B+a_i)\to0$. Then
$$
 \limsup \mu\left(\bigcup_i[a_i,a_i+L_i)\right)\le c. \tag{2}
$$
Thus in a parse with $z=O(D)$ at most $c$ of the limiting logarithmic mass can use vanishing relative addresses. Here take macroscopic copies first and send $\delta$ down last. These claims apply to arbitrary varying earlier substrings. They do not bound the number of ordinary LZ phrases by a superlogarithm when comparable-time addresses are available.

## The integer-reference estimate

Let $a_1<\cdots<a_j$ be the starts of any selected disjoint macroscopic copies. Write $\ell_i=v_2(x_{a_i}-x_{b_i})$. The exact length is finite because the input states are distinct. It equals the observed $L_i$ except for a possibly truncated last copy, and
$$
 L_i\le \ell_i\le \log_2|x_{a_i}-x_{b_i}|\le B+c a_i\le B+a_i . \tag{3}
$$
The numerator is a nonzero integer. The equality between match length and valuation is the shortcut parity-cylinder congruence. Extend the last copy to $\ell_i$ for the arithmetic; its extra length can only increase $G_j=\sum_{i\le j}\ell_i$. Write $s_i,h_i,r_i=s_i+h_i$ for the counts of odd, even and all inputs in each intervening gap, and $A_i^{\rm gap}$ for its ordinary affine numerator. The two integer reference endpoints are $\rho_i=x_{b_i}$ and $\sigma_i=x_{b_i+\ell_i}$. Put
$$
 F_i=3^{s_i}\sigma_i+A_i^{\rm gap}-2^{r_i}\rho_{i+1}.
$$
It is odd even for an empty gap: the reference mismatches on the first following bit, and the next reference, when present at that position, matches it. The unrolled endpoint identity and the unique-valuation complement argument in `RATIONAL_MATCH_MASS.md` show that every nonempty subsum of its $d$ right-hand terms is nonzero. For $d\ge2$ consecutive selected copies, Evertse's Theorem 2, equations (13)–(14), with $S=\{\infty,2,3\}$ and $T'=\{2\}$ therefore gives
$$
 \sum_{i=1}^d\ell_i\le B+c a_1+
 \sum_{i<d}(\log_2 |F_i|-r_i)
 +\epsilon\log_2\max |w_i|+K_{d,\epsilon}. \tag{4}
$$
The $w_i$ are the summands in that identity. Indeed the part of the first summand outside 2 and 3 is at most $|x_{a_1}-x_{b_1}|/2^{\ell_1}$, each other outside part is at most $|F_i|$, the complete sum has valuation $a_d-a_1+\ell_d$, and the first summand has valuation $\ell_1$. All reference denominators are one. For $d=1$ use (3). [Evertse, *Compositio Mathematica* 53 (1984), printed p. 228, Theorem 2](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf).

The elementary bound $0\le A_i^{\rm gap}\le 2^{h_i}3^{s_i}$ and the growth bound $x_u+1\le 2^{B+cu}$ show
$$
 \log_2|F_i|-r_i\le c s_i+B+c\ell_i+c(b_i+b_{i+1})+2. \tag{5}
$$
In fact before splitting the last costs one may use $B+c\max(b_i+\ell_i,b_{i+1})$. The ordinary sizes in (4) obey $\log_2\max|w_i|\le C_0[B+a_1+(a_d-a_1)+1]$ with absolute $C_0$: write each summand as $2^{P_i}3^{J_i}F_i$ and use $P_i,J_i,r_i\le a_d-a_1$, $b_i+\ell_i\le a_d$ for every interior gap. Only the root term occurs at $d=1$.

## Boundary accounting and the finite cutoff

Write $M(t)$ for selected length up to $t$ and $U(t)$ for unselected odd inputs, with linear interpolation of counts. In particular $U(t)\le t-M(t)$. Fix $m$ and sum (4) over the $m$ shifted block partitions of the marks starting before or at $t$. Each interior gap is used $m-1$ times and every mark starts a block once, except the first which starts $m$ blocks. For $t\ge a_1$, writing $j$ for the number of these marks, $G_j\ge M(t)$ and $\sum_{i\le j}(B+a_i)\le G_j/\delta$. Thus (4)–(5) imply
$$
 [m-c(m-1)-(1+C_0\epsilon)/\delta]G_j
 \le c(m-1)U(t)+c(m-1)\sum_{i<j}(b_i+b_{i+1})
 + O_m\big((B+a_1)+(B+1+K)j+\epsilon(B+t)\big), \tag{6}
$$
where $K=\max_{d\le m}K_{d,\epsilon}$ is made positive. The total spans of blocks within one partition are at most $t$, which accounts for the last error. Before $a_1$, $M(t)=0$. Empty selections require no inequality. The macroscopic threshold makes $B+a_{i+1}\ge(1+\delta)(B+a_i)$, so $j\ll_\delta1+\log(1+t/B)$. The last copy, including its extension, satisfies (3); in particular there is no endpoint charge requiring a subsequent match.

Use the positive integration operator
$$
 {\cal I}(f)=\frac{f(T)}{B+T}+\int_0^T\frac{f(t)}{(B+t)^2}\,dt.
$$
For an increasing piecewise-linear cumulative length $f$ with $f(0)=0$ this equals $\int_0^Tdf(t)/(B+t)$. A step charge $h$ first visible at $u$ costs exactly $h/(B+u)$, including the endpoint term. Every $b_i$ charge on the right of (6) is visible only after $a_i$, at most twice. The first-mark charge costs $O_m(1)$ because it starts at $a_1$. The $j$ term costs $O_{m,\delta,\epsilon}(1)$: summing $(B+1+K)/(B+a_i)$ is a decreasing geometric series and $B\ge1$. The $\epsilon$ term costs $O_m(\epsilon(1+D))$. Choose $m$ sufficiently large compared with $1/[\delta(1-c)]$, for instance, then $\epsilon$ sufficiently small so the coefficient of $G_j$ is positive. Apply $\mathcal I$, replace $G_j$ by $M(t)$, divide by $mD$, take the large-path limit, then $\epsilon\downarrow0$, then $m\to\infty$. Equivalently the finite error in the following normalized inequality has nonpositive limsup after these ordered limits:
$$
 (1-c)\mu(M)\le c[1-\mu(M)]+\frac{2c}{D}\sum_{i\ {\rm selected}}\frac{b_i}{B+a_i}+o(1). \tag{7}
$$
The fixed $1/(m\delta)$ term disappears only at the last limit. For (2), the number of macroscopic marks is $O_\delta(1+D)$, hence the address term vanishes under the stated maximum. For (1), select all macroscopic copies. Each discarded small copy carries at most $\log(1+\delta)/D$ mass, hence their total is at most $C\log(1+\delta)$. The total mass of literals is at most $\log(1+z/B)/D=o(1)$ by placing their unit intervals as early as possible. Rearranging (7), then sending $\delta\downarrow0$ gives (1). If the address restriction is only imposed beyond $a\le K B$ for fixed $K$, the selected earlier starts cost $O_{\delta,K}(1)/D$ by the geometric spacing. This also proves the claimed old-address exclusion.

The classical Lempel–Ziv previous-occurrence construction supplies the combinatorial motivation. The arithmetic estimate uses the actual earlier integer states and applies to the exact-match parses specified above. Weaver's paper 173 proves a different finite descent condition using the number of distinct factors in a window at its source's bit-length scale. `FINITE_POWER_GRAMMAR.md` counts repetition-expression tree nodes, including separate occurrences of any identical subtree. Neither result by itself gives (1). [Lempel and Ziv, *On the Complexity of Finite Sequences*](https://doi.org/10.1109/TIT.1976.1055501) · [Weaver, paper 173/v1](https://rstation.ai/problems/collatz/papers/173/v1).

## Two finite bounds allowing arbitrary shared grammar nodes

Let $g$ be the number of reachable rules of a run-length straight-line grammar for the actual prefix. A rule is a bit, a concatenation of two previously defined nonempty words, or an arbitrary power $U^q$ with $q\ge2$. Expansions may refer to the same underlying node many times. Write $H(t)=\max_{0\le r\le\lfloor t\rfloor}\log_2(x_r+1)$. Then
$$
 \boxed{\int_0^T\frac{dt}{H(t)}\le2g+1.} \tag{8}
$$
Traverse the root left-to-right and store the start of each node's first completed expansion. An already completed node emits one copy at its stored address. A first power expansion recursively emits its child once, then emits the rest as one overlapping copy from that child's current start. A first concatenation descends to its two children; a first bit emits one literal. In this traversal there are at most $g$ first expansions. Counting their children and the additional power-copy packets (at most two per first internal expansion) bounds the total number of terminal packets by $2g+1$; for example count all visited frames plus power-copy packets, at most $1+2g$ of them. Every packet beginning at $a$ has length at most $H(a)$, since a copy agrees with an earlier but distinct state through its whole length and a literal has length one. Its integral in (8) is at most one. These copies need not end on a mismatch, which is why (8) uses no Evertse estimate.

In particular **a fixed nonperiodic positive ray with $\log(x_t+1)=o(t)$ has $g(w[0,T))/\log T\to\infty$ even with arbitrary sharing**. Its running maximum satisfies $H(t)=o(t)$. For every $\epsilon>0$ the integral in (8) from sufficiently large $t_0$ to $T$ is at least $\log(T/t_0)/\epsilon$. More generally an $O(D)$-rule grammar forces the logarithmic mass of $\{t: H(t)\le\epsilon(B+t)\}$ to be at most $\epsilon(2g+1)/D$. This does not assume the trajectory has a limiting growth rate.

There is also a finite factor-count estimate useful for comparing with paper 173. For $1\le n\le T/K$, let $p_K(n)$ count the distinct length-$n$ factors in the first $\lfloor Kn\rfloor$ bits. For each internal grammar node $v$, take its earliest expanded occurrence and define $d_v$ as the absolute position of its first internal boundary (after the left child, or after one power copy). Then
$$
 p_K(n)\le2\mathbf1_{n=1}+\sum_{v:\ d_v\le Kn}\min(n,d_v),\qquad
 \sum_{j:\ K2^j\le T}\frac{p_K(2^j)}{2^j}\le 2+(3+\log_2 K)g \quad(K\ge1). \tag{9}
$$
For each factor of length at least two, descend in its chosen occurrence until it first crosses an internal boundary. For a concatenation its start offset is determined by how far before the boundary it begins, leaving at most $\min(n,|U|)$ possibilities when $U$ is the left child. For a power with $|U|=p$, shift the factor left by whole copies to put its start in the first $U$. It still crosses a boundary, with at most $\min(n,p)$ phases. Move each to the earliest occurrence of that whole node. Its first boundary is no later than the originally crossed one, which occurred in the observed prefix. This proves the finite count. For each $d_v$, dyadic $n\in[d_v/K,d_v]$ contribute at most $1+\log_2 K$ and dyadic $n>d_v$ contribute less than two. This proves the sum. The horizon multiplier in paper 173 depends qualitatively on the target factor-count coefficient. Thus (9) does not supply that paper's local descent hypothesis at an arbitrary bit-length scale.
