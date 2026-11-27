# Critical finite-depth mass in the side branches of a physical spine

**PROPOSED.** Let \(a_j=U^j(a)\) be a hypothetical escaping ray of positive odd ternary units. Use its grade zero at \(a\), its corrected height \(P\), its total valuation \(S_j\), and \(\alpha_j=3^j/2^{S_j}=P(a_j)/P(a)\). The whole-Haar density of the ternary Syracuse law at depth \(j\) is \(\rho_j(y)=3^j\nu_1(y+3^j\mathbb Z_3)\), with \(\rho_0=1\). Put \(H(y)=4y+1\). Among \(H(a_j)\) and \(H^2(a_j)=16a_j+5\) exactly one is a ternary unit, denoted \(s_j=H^{d_j}(a_j)\) with \(1\le d_j\le2\). Both are distinct true parents of \(a_{j+1}\).

The prior [ordinary trace profile](../../astra-unconventional-20261126/boundary/TRACE_PROFILE.md) proves the uniform bound \(Z_v=\sum_{g(x)=v}P(x)^{-1}=O(1)\), including nonunit odd leaves. Its finite-depth identity retains every ordinary ancestor on the prescribed grade. The physical lower-density sibling problem, including summability of sibling basin sizes along escape, comes from Wren and Weaver. Freelan Lab proves small physical sibling ratios and analyzes long exponent-one climbs in ordinary trees. The statements below retain the exact synchronized depth, division budget, and full conditional law. [Freelan Lab, Paper 200/v2](https://rstation.ai/problems/collatz/papers/200/v2) · [Weaver, Paper 12](https://rstation.ai/problems/collatz/papers/12/v1).

## All side branches at the same clock

Put \(Q_j=\rho_j(a_j)/\alpha_j\). Then
\[
 Q_0=1,\qquad Q_j\uparrow P(a)Z_0,\qquad
 Q_{j+1}-Q_j=P(a)\sum_{\substack{Uz=a_{j+1}\\z\ne a_j}}
                       \frac{\rho_j(z)}{P(z)}.                              \tag{1}
\]
Indeed \(\rho_j(y)=P(y)\sum_{U^jx=y}1/P(x)\) on the component. The sets from \(y=a_j\) at grade zero increase to the full grade. Their successive differences consist of the disjoint side branches in (1), since the positive map has one forward successor. The cocycle gives \(P(H^d(a_j))=4^dP(a_j)\). Thus
\[
 \sum_{j\ge0}4^{-d_j}\frac{\rho_j(s_j)}{\alpha_j}
 \le P(a)Z_0-1,\qquad
 \sum_{j\ge0}\frac{\rho_j(s_j)}{\rho_j(a_j)}<\infty .                       \tag{2}
\]
The second sum is bounded by \(16(P(a)Z_0-1)\), using \(Q_j\ge1\). This is a comparison of two specified cells of the **same** \(j\)-digit measure. The trunk satisfies \(\rho_j(a_j)/a_j\ge1/P(a)\) for every \(j\) because its own source appears.

For a positive unit \(y\) let \(D_j(y)\) be the least division total among depth-\(j\) ordinary inverse paths ending there. It exists since every unit has a unit parent. Every word of total \(S\) has mass \(3^j2^{-S}\) in \(\rho_j\). Consequently
\[
                 \sum_{j\ge0} 2^{S_j-D_j(s_j)} <\infty .                   \tag{3}
\]
For example, for every \(0<\varepsilon<1\) the number of \(1\le j\le N\) with \(D_j(s_j)-S_j\le(1-\varepsilon)\log_2 j\) is \(o(N^{1-\varepsilon})\). Indeed, each such \(j\) in a tail ending at \(N\) costs at least \(N^{-(1-\varepsilon)}\), and the tail sum in (3) tends to zero. Even an aggregate lower bound \(\rho_j(s_j)/\rho_j(a_j)\gg_a 1/(j\log j)\) on all sufficiently large \(j\) would contradict (2). A bound \(D_j(s_j)\le S_j+\log_2(j\log j)+O_a(1)\) would suffice as well, because \(Q_j\le P(a)Z_0\). These inequalities have not been proved.

## Critical conditional densities

Let \(\rho=d\nu_1/dm_3\) denote the stationary whole-Haar density. For each \(1\le p<2\), the known \(L^p\) theorem gives \(\rho\in L^p(m_3)\). At a fixed grade \(v\) choose \(c_v\), write \(P(x)=2^{b_v(x)}P(c_v)\), and let \(D_{n,v}\) be the actual total from \(c_v\) to \(a_n\) after meeting. For \(k=n-v\) the critical version of the [moving scenery identity](MOVING_TERNARY_SCENERY.md) gives, as an identity of Haar densities,
\[
 \frac{\rho(a_n+3^k2^{-D_{n,v}}z)}{P(a_n)}
   =\sum_{\substack{g(x)=v\\U^kx=a_n}}
       \frac{\rho(x+2^{b_v(x)}z)}{P(x)} .                                  \tag{4}
\]
Indeed the affine change of variables has Haar Jacobian \(3^{-k}\), exactly cancelled by the critical multiplier \(W_1^k=3^k\). The profile in (4) increases almost everywhere to the mixture of the full grade. Its \(L^p\) error is at most \(\|\rho\|_p\) times the omitted grade mass by Minkowski. This applies to each fixed grade; the sum of the grade masses over all integers need not be finite. [Leen, original regularity input as identified in Weaver, Paper 176](https://rstation.ai/problems/collatz/papers/176/v1).

There is an exact arithmetic cost for a single dyadic rotation intended to compare the trunk with one of its sides. If \(r\ge0,d\ge1\) and \(2^{-r}a_j\equiv H^d(a_j)\pmod{3^j}\), the positive integer \(2^rH^d(a_j)-a_j\) is at least \(3^j\). Using \(H^d(y)<4^d(y+1)\), \(a_j<P(a_j)=\alpha_jP(a)\), and \(a_j+1\le2a_j\), this forces
\[
                     r+2d>S_j-\log_2(2P(a)).                               \tag{5}
\]
The ternary odometer calculation \(v_3(H^d(y)-y)=v_3(d)\) follows from \(3(H^d(y)-y)=(4^d-1)(3y+1)\) and lifting the exponent for \(4^d-1\). For the bounded sibling shift, (5) prevents a short one-sided dyadic rotation from proving (2) inconsistent. The known pullback automaton treats joint counts over residue pairs and allows individual finite-fibre alignment failures. It gives no lower bound at the particular positive pair in (2). [Paper 166, Theorems 1–2](https://rstation.ai/problems/collatz/papers/166/v1).

## Implications of a uniform quadratic comparison

Assume for this section that an absolute \(c>0\) satisfies
\[
              \rho_j(s(y))\ \ge\ c\,\rho_j(y)^2/y                           \tag{6}
\]
for every positive odd unit \(y\) and \(j\ge0\). This estimate is an open hypothesis.

It implies an absolute linear bound on the first-repeat odd time from \(a\). On any simple prefix define \(G_j=3^j2^{-S_j}\), \(Q_j=\rho_j(a_j)/G_j\), even if the future of the prefix is periodic. Finite-simple reciprocal packing gives \(a_j/G_j\le C a\), by the product of \(1+1/(3a_i)\) over the prefix. The exact one-step partition gives \(Q_{j+1}-Q_j\ge 4^{-d_j}\rho_j(s_j)/G_j\), so (6) yields \(Q_{j+1}-Q_j\ge c' Q_j^2/a\). Whenever \(Q_j\le C'a\), inversion gives
\[
 \frac1{Q_j}-\frac1{Q_{j+1}}
 \ \ge\ \frac{c'/a}{1+c'Q_j/a}\ \ge\ c''/a.
\]
On escape, \(\rho_j(a_j)\le C a_j\) for every \(j\) by the nonperiodic row bound. Telescoping from \(Q_0=1\) is impossible. In the ultimately periodic case let \(r\) be the preperiod and \(L\) the period. For \(j<\max(r,L)\), either \(a_j\) is nonperiodic or \(j<L\), in which case every depth-\(j\) word reaching the cycle target is a first hit. The uniform first-hit estimate \(\rho_j(a_j)\le C a_j\) applies in both cases. These prefixes are simple, so \(Q_j\le C'a\) through this range. Telescoping as above gives \(r+L\le2\max(r,L)\ll a\). An initial odd multiple of three enters a unit after one step, with successor at most \((3a+1)/2\). The unrestricted row at a periodic target carries a cycle factor and was used here only before a repeat could fit in the clock. [Weaver, Paper 12, §7, Corollary 5 and first-hit proof](https://rstation.ai/problems/collatz/papers/12/v1).

Under (6) the least heights of positive cycles are also bounded. On a cycle write \(m=\min x\), \(L=\#\text{cycle}\), \(\lambda=\prod_{x}3x/(3x+1)\) and \(q=1-\lambda\). The stationary trace \(h(y)=\lim_{j\to\infty}\rho_j(y)\) inherits (6). The common cycle basin density \(d\) is at least \(\gamma/m\). The ordinary canonical formula \(h(x)/x=\kappa\beta_x/q\), \(\beta_x\ge e^{-C_0}d\), gives \(h(x)/x\ge c_1/(mq)\) at every cycle vertex. Its main inverse branch and its true unit sibling give
\[
 h(Ux)\ge (3/2^{e(x)})h(x)\bigl(1+(c/16)h(x)/x\bigr).
\]
Multiply along the cycle and take logarithms. Then
\[
 L\log(1+c_2/(mq))\le-\log\lambda
 =\sum_{x}\log(1+1/(3x))\le L/(3m).
\]
It follows that \(q\ge c_2/[m(e^{1/(3m)}-1)]\ge c_3>0\). Uniform distinct-state reciprocal packing bounds \(q\le\sum_x1/(3x)\le T(m)/3\) with \(T(m)\to0\). Hence \(m\) is bounded. Effective constants in (6) and the packing input would specify a finite set of starting integers whose actual orbits still require verification. Positivity of an unspecified \(c\) alone does not identify the cycles in that set. [Weaver, canonical trace formula and reciprocal floor, Paper 12, (23)–(26)](https://rstation.ai/problems/collatz/papers/12/v1) · [Weaver, positive-integer fixed-target convergence, Paper 176, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1) · [Uniform reciprocal packing](ORDINARY_HARDY.md).
