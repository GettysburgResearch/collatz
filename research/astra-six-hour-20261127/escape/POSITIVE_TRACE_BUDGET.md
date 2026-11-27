# The positive stationary trace budget and its first differences

Let \(h(x)=\lim_k\rho_k(x)\) be the individual-depth trace of the original geometric Syracuse law at the positive odd integer \(x\), and put \(h(x)=0\) at odd multiples of three. Set \(D=\log(4/3)\), \(\kappa=D/2\), \(w_x=3x/(3x+1)\), and
\[
                a_x=h(x)/x,\qquad \ell_x=(1-w_x)a_x
                           =\frac{h(x)}{x(3x+1)} .
\]
Weaver’s Theorem 2, equation (4), already gives the total positive stationary loss as \(\kappa(1-b)\), where \(b\) is the logarithmic surviving mass. With the previously identified escape charges \(H_C\), this prior scalar budget reads
\[
 \boxed{\qquad \sum_{x>0\ {\rm odd}}\ell_x+\sum_{C\ {\rm escaping}}H_C=\kappa .\qquad}                \tag{1}
\]
In particular absence of positive escape is equivalent to the stationary sum attaining \(\kappa\), assuming the retained positive charge at every escaping component. Cycles of every length are allowed. The sum restricted to vertices reaching 1 is exactly \(\kappa d_1\). Proving that this restricted sum attains \(\kappa\) would give full positive convergence using the all-unit predecessor floor. Weaver’s equation (6) also proves the exact finite first difference. Below we give an alternative Mellin derivation, componentwise sums, a physical height tail, and exact finite sign reversals. The identities do not prove saturation. [Weaver 176, Theorem 2 and equations (4), (6)](https://rstation.ai/problems/collatz/papers/176/v1)

## Local positive sums on the actual inverse tree

For a nonperiodic unit \(y\), write \(B_y\) for its ordinary odd predecessor set including itself, and let \(d_y\) denote its relative odd density. Then
\[
                \kappa d_y=a_y+\sum_{x\in B_y\setminus\{y\}}\ell_x .
                                                                         \tag{2}
\]
Indeed the trace transfer gives \(a_z=\sum_{Ux=z}w_x a_x\) at every positive odd integer. The sets \(L_j=\{x:U^jx=y\}\) for \(j\ge0\) are distinct first-hit levels. At every fixed level \(\sum_{x\in L_j}d_x=d_y\), by the full natural inverse law; nonunit leaves contribute zero. The identity \(a_x=\kappa\beta_x\le\kappa d_x\) gives finite level sums. As \(j\to\infty\), the least vertex in \(\bigcup_{t\ge j}L_t\) tends to infinity, since each integer has at most one depth and every bounded interval contains finitely many integers. All ancestors before a first hit to any \(x\in L_j\) are in that deep union. The uniform reciprocal tail on distinct-state paths shows \(\beta_x/d_x\to1\) uniformly over the positive-density members of these levels, using the natural first-hit correction definition of \(\beta_x\). Thus \(\sum_{L_j}a_x\to\kappa d_y\). The difference of consecutive level sums is precisely \(\sum_{L_{j+1}}\ell_x\) by harmonicity. Telescoping and positivity prove (2). [Weaver 19, (F13)](https://rstation.ai/problems/collatz/papers/19) · [Weaver 102, (27)–(29)](https://rstation.ai/problems/collatz/papers/102) · [Uniform reciprocal tail and fixed-level source laws](CANONICAL_INVERSE_PATHS.md)

If \(C\) reaches a cycle \(L\), sum the same transfer over its finitely many cycle vertices. The sum of \(\ell_x\) on the cycle equals the sum of \(w_z a_z\) over its off-cycle immediate parents. Distinct such parent basins partition \(C\setminus L\). Their densities sum to the ordinary component density \(d_C^{\rm ord}\): parents with least ancestor above a threshold \(M\) lie in the union of the at most \(|L|\) first-landing cells determined by their subsequent cycle point, with upper density \(O_L(M^{-\delta})\) for \(M\) above the cycle. All nonunit direct parents form finitely many exponential sequences and have density zero. The remaining parent family is finite by disjointness. Now apply (2) to each off-cycle unit parent, and add its own \(\ell_z\) to the descendant losses; its outside boundary contribution becomes \(w_z a_z\). This proves
\[
                       \kappa d_C^{\rm ord}=\sum_{x\in C}\ell_x .
                                                                         \tag{3}
\]
For the cycle of 1 the first term in (3) is \(h(1)/4\), followed by the positive losses on its transient ordinary branches. The same density appears in the [first-return Mellin residue](FIRST_RETURN_POISSON.md) and [critical Poisson transition](CRITICAL_POISSON_PROFILE.md). [Weaver 102, (2)–(3) and Proposition 6](https://rstation.ai/problems/collatz/papers/102)

On a positive escaping component \(C\) take successive points \(y_j\) on an actual ray. Its predecessor sets increase to \(C\), their densities tend to \(d_C^{\rm ord}\) by the natural component and minimum laws, and \(w_{y_j}a_{y_j}\to H_C\) by the positive trace profile. Rewrite (2) as \(\kappa d_{y_j}=w_{y_j}a_{y_j}+\sum_{B_{y_j}}\ell_x\) and use monotone convergence. Consequently
\[
                   \kappa d_C^{\rm ord}=H_C+\sum_{x\in C}\ell_x .     \tag{4}
\]
The ordinary component densities sum to one, by tightness of the minimum law. Summing (3) and (4) recovers (1) from its componentwise refinements. Components here include their odd nonunit leaves. [Moving trace charge](../../astra-unconventional-20261126/boundary/TRACE_PROFILE.md) · [Component and minimum inputs](https://rstation.ai/problems/collatz/papers/176/v1)

## A second derivation from the finite unmarked Dirichlet series

For real \(s>1\) define \(D_k(s)=\sum_{x>0\ {\rm odd}}\rho_k(x)x^{-s}\) and let \(C_k=\lim_{u\downarrow0}(D_k(1+u)-1/(2u))\). The periodic law has full odd mean one. Its pole has residue \(1/2\). The finite part differs by a fixed constant from Weaver’s height-ordered sum of \((\rho_k(x)-1)/x\). His equation (6) therefore gives the exact identity at each depth,
\[
 C_{k+1}-C_k=\kappa-\sum_{x>0\ {\rm odd}}\frac{\rho_k(x)}{x(3x+1)} .
                                                                         \tag{5}
\]
For an alternative proof using the Dirichlet limit, put \(c(x)=e(x)\log2-\log3\), \(e(x)=v_2(3x+1)\). The genuine affine change of variables at \(s=1+u\) splits the difference into
\[
 \sum_x\frac{\rho_k(x)}{x^{1+u}}(e^{u c(x)}-1)
 -\sum_x\frac{\rho_k(x)e^{u c(x)}}{x^{1+u}} (1-w_x^{1+u}).
\]
The second sum tends to the sum in (5) by dominated convergence, using \(2^{e(x)}\le3x+1\), \(1-w_x^{1+u}\ll1/x\) for \(0<u\le1/4\), and \(\rho_k\le3^k\). In the first term replace \(e^{u c(x)}-1\) by \(uc(x)\), at total cost \(O_k(u)\). Indeed the positive partial means of \((1+e(x)^2)2^{e(x)/4}\) are bounded. In an interval \([1,X]\) each valuation \(e\ge1\) occurs in one class modulo \(2^{e+1}\), at most \(X2^{-e}+1\) times, and vanishes for \(e>\log_2(3X+1)\). Partial summation then bounds the Taylor remainder. By CRT the ordinary counting mean of \(\rho_k(x)c(x)\), extending it by zero at even \(x\), is \(\kappa\): the odd-relative geometric valuation mean is two, independent of the fixed ternary residue. Truncating the valuations first is justified by the same uniform partial means. Abelian partial summation of \(u\sum_x\rho_k(x)c(x)x^{-1-u}\) gives \(\kappa\). This proves (5). [Finite affine Mellin transfer](../root/DIRICHLET_TRACE.md)

If \(q=3^k\), then
\[
       C_k=\sum_{1\le x<2q\ {\rm odd}}\rho_k(x)/x
                             -\tfrac12\log(2q)+O(1)
\]
with an absolute error, by summing the tails of the odd progressions. In detail, the regular part of \(\sum_{m\ge1}(m+x/(2q))^{-1-u}\) at \(u=0\) is uniformly bounded for \(0<x/(2q)<1\), by comparison with the ordinary zeta series term by term. Expanding \((2q)^{-u}\) against its pole gives the displayed logarithm. Weaver’s original harmonic asymptotic gives \(C_k/k\to\sum_C H_C\). Thus the Cesàro limit of the positive sums in (5) exists and is \(\kappa-\sum_C H_C\). At each positive ordinary \(x\) we have \(\rho_k(x)\to h(x)\). Fatou applied to the Cesàro means first gives global finiteness of \(\sum\ell_x\). For every \(k\ge1\), \(\rho_k(x)\le C h(x)\) on the units, by boundedness of \(\rho_1/h\) and its exact canonical Markov selection; both sides vanish on nonunits. Dominated convergence therefore upgrades the positive sums to an individual-depth limit and reproves (1). In particular
\[
                       C_{k+1}-C_k\longrightarrow\sum_C H_C.
\]
The same individual-depth increment limit follows immediately from (5) and Weaver’s prior total variation convergence of the finite stopping measures in his Theorem 2, (4). The difference detects escape through a fixed summable positive kernel on the stationary trace. A proof that this kernel exhausts the scale budget \(\kappa\) is still needed. [Weaver 176, Theorems 1–2](https://rstation.ai/problems/collatz/papers/176/v1) · [Ordinary-depth canonical selection](REAL_FIBRE_AND_FRONT.md)

## Exact finite sign control

The individual increments in (5) can have either sign. Fixed-point interval arithmetic gives the positive finite-law loss in \([0.152466222,0.152466540]\) at depth 12 and \([0.143172250,0.143172361]\) at depth 13. These lie on opposite sides of \(\kappa=0.143841036\ldots\). In particular a proof based on monotone decrease of all \(C_k\) would fail. The checker bounds the infinite progression tail using the exact total mass \(3^k\), verifies the first five density arrays independently by positive wrapped-word enumeration, and cross-checks the first-hit and real-defect cell indexing against ordinary forward iteration. [Checker](check_first_return.py) · [Rational outward enclosures](../../../reports/astra-six-hour-20261127/escape/first_return_budget.tsv)

## A physical tail for the positive sum on nonperiodic sites

Let \(T(R)\) bound the sum of reciprocals of the distinct states above \(R\) on any ordinary simple path. The same bound applies to any finite set of **nonperiodic** states visited by a single source, since their visits lie before any repetition. On the orbit interval-count input one has \(T(R)\ll_\theta R^{\theta-1}\) for each allowed fixed \(\theta<1\), by dyadic summation. For every \(R\ge1\),
\[
 \sum_{x>R,\,x\ {\rm nonperiodic}}\ell_x
             \le\frac{\kappa}{3}\sum_{x>R,\,x\ {\rm nonperiodic}}\frac{d_x}{x}
             \le\frac{\kappa}{3}T(R).                                 \tag{6}
\]
Indeed \(a_x=\kappa\beta_x\le\kappa d_x\) at these sites. For any finite set in the displayed sum, average its reciprocal occupation over odd sources up to a cutoff, then take the natural-density limit at the finitely many specified targets. The sum on each source is bounded by \(T(R)\). Supremizing over finite subsets proves (6). Thus the positive sum for \(d_1\) in (3) has a power-decaying tail when truncated by ordinary height. The point values \(h(x)\) are still canonical limiting traces. Formula (6) gives no such estimate for the contribution of unknown cycle vertices, where \(a_x=\kappa\beta_x\) cannot be used. Equations (1) and (3) already provide finiteness including those vertices. [Reciprocal tail and source pins](https://rstation.ai/problems/collatz/papers/176/v1) · [Explicit interval-sparsity exponent](https://rstation.ai/problems/collatz/papers/175/v1)
