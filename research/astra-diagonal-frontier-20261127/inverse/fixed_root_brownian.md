# A Brownian motion limit on the canonical and natural inverse paths

Fix a positive odd ternary unit $a$, let $X_0=a$, and let the outward gap total be $S_j$ with $D_j=S_j-2j$. Under the same inputs as the [upper functional iterated-logarithm law](functional_upper.md), including the averaged joint Syracuse mixing assumption (J), the actual polygonal path
\[
                   V_n(t)=D_{nt}/\sqrt n,\qquad 0\le t\le1,
\]
converges in distribution in $C[0,1]$ to $\sqrt2 W$, where $W$ is standard Brownian motion. More precisely, for every bounded full-path random variable $H$ and every bounded continuous functional $\Psi$ on $C[0,1]$,
\[
 \lim_{n\to\infty}\mathbb E_{h,a}[H\Psi(V_n)]
       =\mathbb E_{h,a}[H]\,\mathbb E[\Psi(\sqrt2W)].                 \tag{1}
\]
The same assertion holds at each fixed nonperiodic $a$ under the natural inverse entrance law $Q_a$. At the same fixed root, if $M_\epsilon=\sup_{j\ge0}(-D_j-\epsilon j)$, then
\[
                   \epsilon M_\epsilon\ \Longrightarrow\
                                      {\rm Exponential}(1) .        \tag{2}
\]
The limit in (2) gives the full finite-reserve response at reserve $b/\epsilon$ for each fixed $b>0$. It imposes no rate on the zero-reserve atom.

Weaver already proved the unmarked fixed ordinary depth limit $\rho_k(a)\to h(a)$. Here the restrictions imposed at successively increasing depths have their own limits. This allows two-sided distributional comparison for moving partial-sum tests. Paper 211's Brownian bridge *lower bounds* on selected residue slices and the earlier upper iterated-logarithm comparisons are inputs or comparison results. The path in (1) has no prescribed total at its terminal time. [Weaver, Paper 176 v1, §1 and Theorems 1–2](https://rstation.ai/problems/collatz/papers/176/v1) · [Weaver, Paper 211 v1, Appendices A–B](https://rstation.ai/problems/collatz/papers/211/v1).

## The mass removed by late restrictions

Keep the notation for (2)–(4) in the [upper comparison](functional_upper.md). Fix $I$ and $G_I=\{1.9d\le S_d\le3d\ \forall d\ge I\}$. Write $d(x)=\lfloor0.9x\rfloor$, and let $K_x$ mean that these restrictions hold at all $I\le d\le d(x)$. Thus $K_x$ decreases to $G_I$ on infinite paths. Define
\[
      r_x^I=3^x\Pr_0(\beta_x=a\bmod3^x,\ K_x).
\]
For $x$ large enough that $d(x)\ge I$, first lift from $x$ to $x+1$ retaining exactly $K_x$, then delete $K_x\setminus K_{x+1}$ at precision $x+1$. This gives
\[
       r_{x+1}^I=r_x^I+e_x-\Delta_{x+1},\qquad
       |e_x|\le C_{a,b}(x+1)^{1-b},\qquad \Delta_{x+1}\ge0 .        \tag{3}
\]
The one-digit bound is precisely (2) and (4) of the upper comparison, with no marked dates and $O(x)$ prefix totals; here Tao's unmarked mixing also suffices. The deletion $\Delta_{x+1}$ is the actual projected density at $a$ of the deleted event, with no terminal restriction. Since $r_x^I\ge0$, summing (3) at any $b>2$ shows both that $\sum\Delta_x<\infty$ and that $r_x^I$ converges to a number $r^I$. In particular $\sum_{x>Q}\Delta_x\to0$ at every fixed $I$. [Tao, Proposition 1.14 and equation (1.29)](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F).

For $m\ge2$ the exact root-specific identity is
\[
  r_m^I=h(a)\,\mathbb E_{h,a}
     [\,1_{K_m}\rho_1(X_{m-1})/h(X_{m-1})\,].                      \tag{4}
\]
Indeed $d(m)\le m-1$, so exposing the last unrestricted trit gives the extra compatible one-letter mass $\rho_1$ at the actual endpoint of the first $m-1$ letters. Terminal nonunits contribute zero to $\rho_1$. The remaining canonical word factor is $3^{m-1}2^{-S_{m-1}}h(X_{m-1})/h(a)$. Replacing $1_{K_m}$ by $1_{G_I}$ in (4) costs $o_I(1)$ as $m\to\infty$, since $\rho_1/h\le2/\alpha$ and $K_m\downarrow G_I$. Cesàro averaging (4) and Paper 12 (29) thus identify
\[
                            r^I=h(a)P_{h,a}(G_I).                   \tag{5}
\]
The same last-letter identity applies when a bounded prefix statistic measured before $m-1$ is inserted on both sides. [Weaver, Paper 12 v1, §10, (28)–(29)](https://rstation.ai/problems/collatz/papers/12/v1).

## Two-sided comparison for finite-dimensional tests

Take distinct fixed $0<t_1<\cdots<t_r\le1$, integer dates $p_i=\lfloor nt_i\rfloor$, and a Lipschitz $0\le\phi\le1$ on $\mathbb R^r$. Let $L_\phi=\mathbb E\phi(\sqrt2 W_{t_1},\ldots,\sqrt2 W_{t_r})$. At every padded depth $m\ge3n$ consider the density
\[
  3^m\mathbb E_0[\,1_{\{\beta_m=a\bmod3^m\}}1_{K_m}
                   \phi(D_{p_1}/\sqrt n,\ldots,D_{p_r}/\sqrt n)\,].
\]
Uniformly in these padded depths it equals
\[
                             r_Q^I L_\phi+o_I(1),
                 \qquad Q=\lfloor n^{1/10}\rfloor .                 \tag{6}
\]
To see this, use the chronology of the upper comparison, starting at the dates $p_i+2\ell$ and ending at their true values, with $\ell=\lfloor n^{1/5}\rfloor$. Retain $K_x$ at each precision, including all constraints from the fixed $I$ onward. At large $n$, the first exposed length already exceeds $I$. No threshold slack is needed for a Lipschitz test.

The signed lift errors in that argument were already bounded in absolute value by an arbitrarily small power of $n^{-1}$, using (J). Its proof of (4) applies directly to $[0,1]$-valued tests. Group by prefix total and the at most $r$ earlier marked sums in the active region. After every mark is inside the prefix the test is a scalar weight in $[0,1]$ attached to that individual prefix. Inequality (2) there applies with that additional weight by positive domination, using $O(x)$ distinct totals on the late lifts. Before the first active mark the tests depend only on future partial sums and the total of the retained prefix. At each exposure the marked loss lies in $[0,\Delta_x]$, since the same prefix is deleted from the same projected space with a test bounded by one. All exposure losses after $Q$ therefore sum to $o_I(1)$ by (3). This is the additional control needed in the reverse direction.

At each of the fixed $r$ switches the difference in tests is bounded by $O_\phi(n^{-1/6})$ if the switched increment has magnitude at most $n^{1/3}$. Its total projected density is at most the unrestricted $\rho_x(a)\le C_a$. The exceptional increment costs $O_B(n^{-B})$ by the switch bound in the upper comparison. At the base precision $Q$, conditional on the first $Q$ fair letters the remaining letters are independent. The part with $S_Q>Q^2$ has projected density $O_B(n^{-B})$. Otherwise the deterministic initial shift is $o(\sqrt n)$, uniformly in the retained prefix. The ordinary finite-dimensional central limit theorem, or its characteristic function proof from the centered geometric cumulant $\theta^2+O(|\theta|^3)$, gives $L_\phi+o(1)$ uniformly in such a prefix at the base dates. The base density is therefore $r_Q^I L_\phi+o(1)$, proving (6).

Use the marked version of (4). For each fixed $n$, replacing $K_m$ by $G_I$ costs $o_{I,n}(1)$ as $m\to\infty$. Average over $m$ and use Paper 12 (29), extended from events to bounded random variables by simple approximation. Then (5), (6), and $r_Q^I\to r^I$ give
\[
  \mathbb E_{h,a}[1_{G_I}\phi(D_{p_1}/\sqrt n,\ldots,D_{p_r}/\sqrt n)]
                               \longrightarrow P_{h,a}(G_I)L_\phi .
\]
Send $I\to\infty$ using $S_d/d\to2$ almost surely. This proves finite-dimensional convergence for the fixed-root law.

## Tightness and stable convergence

On each $[\gamma,1]$, $\gamma>0$, use the entire-tile maximum test of (3) in the upper comparison. At threshold $\eta\sqrt n$ the fair exponential maximum bound on a tile of length $\le\Delta n+2$ is at most $2\exp[-c\eta^2/\Delta]$ in the limit for fixed $\eta,\Delta>0$. There are $O(1/\Delta)$ tiles, and the comparison's slack is $O(n^{1/3})=o(\sqrt n)$. At fixed $I$, this gives the modulus bound on $G_I$; finally send $I\to\infty$.

For the interval at the origin cover $[n^{2/3},\gamma n]$ by dyadic tiles $\{m/2,\ldots,m\}$ up to harmless integer rounding. For one such tile bound its absolute maximum by $|D_{\lfloor m/2\rfloor}|$ plus the maximum absolute increment from that same start. Use (3) with local horizon $m$, fraction $\gamma'=1/3$ and two signs, at threshold $\eta\sqrt n/2$. The fair geometric maximum bound, uniformly in those $m$, is at most
\[
   C\exp[-c\min(\eta^2 n/m,\eta\sqrt n)]
\]
for large $n$, since the local slack $O(m^{1/3})=o(\sqrt n)$ uniformly for $m\le n$. Summing over the dyadic range gives a bound tending to zero as $\gamma\downarrow0$ after the limit superior in $n$. Indeed the $n/m$ exponents at least double at each step, and $O(\log n)$ copies of $e^{-c\eta\sqrt n}$ vanish. The additive comparison errors $\sum O(m^{-2})=o(1)$. The first $O(n^{2/3})$ dates are negligible after division by $\sqrt n$ on almost every path by the old upper iterated-logarithm bound. This establishes tightness in $C[0,1]$, including the interpolated gaps, and the finite-dimensional laws identify the Brownian limit.

Conditioning on a fixed compatible initial word gives the canonical Markov chain from its specified positive endpoint. The result just proved applies at every such endpoint. Adding a fixed initial segment of time and a fixed total to its polygonal path preserves weak convergence: the affine time change tends uniformly to the identity, and tightness controls its modulus. Thus (1) holds on every fixed cylinder. The countable cylinder partition at each fixed depth and boundedness give it for any bounded statistic of that depth. Conditional expectation approximation in $L^1$ extends it to every bounded full-path variable $H$. At nonperiodic $a$, the bounded path Radon–Nikodym derivative of $Q_a$ with respect to $P_{h,a}$ can be included in $H$, proving the assertion for $Q_a$ with independent Brownian factor.

## Near-critical reserve

For $T>0$ fixed, the path on times $0\le j\le T/\epsilon^2$, in the normalization $\epsilon D_j$, converges to $\sqrt2 W$ on $[0,T]$. Hence the maximum of $-\epsilon D_j-\epsilon^2j$ on this range converges in law to that of $-\sqrt2 W_t-t$. For its infinite continuation, on dyadic tiles $m/2\le j\le m$ with $m\ge T/\epsilon^2$ use the same two running tests as above. A crossing $-D_j-\epsilon j\ge0$ on this tile requires a start or increment magnitude at least $\epsilon m/4$. The comparison slack $O(m^{1/3})$ is $o(\epsilon m)$ uniformly there as $\epsilon\downarrow0$ at fixed $T$. The fair bound is $C\exp[-c\epsilon^2 m]$, and summing over dyadic $m\ge T/\epsilon^2$ gives $O(\sum_{s\ge0}e^{-c2^sT})$. The summed additive $O(m^{-2})$ errors vanish. This holds on each $G_I$, whose complement can be sent to zero after the limit superior. It proves uniform tightness of the remote part of the maximum, first in $\epsilon$ then in $T$. Bounded equivalence gives the same remote control under $Q_a$.

The Brownian motion $-\sqrt2W_t-t$ has all-time maximum of rate-one exponential distribution, by optional stopping of its exponential at the upper barrier $b>0$ and a lower barrier tending to $-\infty$. This proves (2). It also gives the stable version of (2) for any fixed bounded $H$, by (1) on finite $T$ followed by the uniform remote bound.
