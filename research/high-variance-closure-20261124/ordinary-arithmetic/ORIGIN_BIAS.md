# Few strict improvements in ancestor minimization on a fixed escape

**Status.** Written fixed-source implication using an independently reviewed orbit occupation theorem. It concerns one hypothetical escaping ordinary shortcut orbit. No existence of an escape is assumed for the level-one counterexample in `RESET_EXIT.md`, whose witnesses instead vary with the scale.

Let $X_i=T^i(x)$ be a fixed positive escaping shortcut orbit. A **strict improvement** for a price $P$ with edge charge $c$ means $P(X_{i+1})<P(X_i)+c(X_i)$. The equality case is the cost inherited from the previous vertex. For the old $b_*$ price use $c=p=\mathbf1_{M_1^c}$. For the signed price $R^{\dagger}$ of `RESET_EXIT.md` use $c=v(1-3\mathbf1_{M_1})$ and the canonical clock growth bound $G(m)=O(1+\sqrt{\log(m+1)})$. Define respectively

$$
 Y_N=2+x+\sum_{i<N}p(X_i),\qquad
 Y_N=2+x+4G(x)+C_0+\sum_{i<N}v(X_i),
$$

where $C_0$ is the uniform path constant of the signed-price construction. There is an absolute $\epsilon>0$ for which the number of strict improvements before clock $N$ is $O(Y_N^{1-\epsilon})$ in each case. The implicit constants may depend on the pinned occupation bound and the fixed signed-price parameters. In particular $b_*(X_{i+1})=b_*(X_i)+1$ at all but $O_x(N^{1-\epsilon})$ unmarked dates, and $b_*$ stays constant at every marked date outside the same exceptional set. The signed statement counts strict improvements in its **own** cost time, which can be substantially smaller than the physical clock. This count does not bound the sizes of the individual discounts.

## One distinct minimizing origin per genuine improvement

In both cases write a bill as $A(m)+\sum_{i<k}c(T^im)$ for a path from $m$ to the target, with $A(m)=m$ or $m+4G(m)$. The previous results show that the minimum is attained. Every candidate bill is at least $m$ in the first case and at least $m-C_0$ in the second. The actual prefix from $x$ provides an upper bound for the minimizing bill at every $X_{i+1}$, $i<N$, so every chosen minimizing origin is at most $Y_N$.

If a minimizing path to a strict improvement at $X_{i+1}$ had visited some $X_j$, $0\le j\le i$, its remainder would be the literal segment of the fixed escaping orbit from that visit to $X_{i+1}$. Its price at $X_j$ is at least the minimum there. Extending the minimizing price from $X_j$ through $X_i$ would then give an inherited price at $X_{i+1}$ no larger than the chosen bill, contradicting strict improvement. An origin producing an improvement at an earlier date cannot do so again. Indeed the fixed orbit has distinct vertices, so its two endpoints, if both seen by the same origin, must occur on that origin's orbit in the same order. Thus the choices of minimizing origins for improvements are distinct. This argument allows arbitrary incoming branches.

## Short entries and long entries

The source-qualified estimate is PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, displayed Theorem (1), SHA-256 `bee22c362de8adcbb6a0360f48240ad276fdf6122f6383273eb10dee8e29271d`. Its separate review is `reports/2026-11-23-whole-repo-round3/CYCLE_ORBIT_COUNT_REVIEW.md`. It bounds the count below $Z$ on an injective, forward-invariant set of positive odd inputs of the odd map by $O(Z^\theta)$, where $\theta=H_2(\log_3 2)<1$. The odd points on the entire fixed escaping orbit satisfy these hypotheses. Every positive physical point on this orbit is $2^a y$ for its subsequent odd point $y$ (allowing $a=0$). Summing the odd bound at $Z/2^a$ gives $O(Z^\theta)$ for the **whole physical orbit**. This invocation is made only for endpoints on that orbit, never for its incoming basin.

Put $Y=Y_N$ and choose a fixed $0<\delta<1$ so small that $\theta(1+\delta\log_2(3/2))<1$. Let $L=\lfloor\delta\log_2Y\rfloor$. A minimizing entry path of fewer than $L$ steps has endpoint at most $(3/2)^L(Y+1)$. By the physical occupation bound and distinctness of endpoints, these paths account for $O(Y^{\theta(1+\delta\log_2(3/2))})$ improvements. Origins $m<2^L$ or below a fixed lower cutoff account for $O(1+Y^\delta)$ further improvements, because origins are distinct.

For every remaining minimizing path, $k\ge L$ and $m\ge2^L$. Write $q=T^L(m)$. The initial section of its bill costs at most $A(q)$, since otherwise starting its remaining path at $q$ gives a cheaper bill. For $b_*$ this implies $q\ge m$. For the signed price, formula (1) of `RESET_EXIT.md` gives $q+4G(q)\ge m-C_0$. If $q<m/2$ and $m$ is sufficiently large, the canonical growth bound on $G$ contradicts this. Hence $q\ge m/2$ suffices for both prices.

Let $P$ count the odd inputs in the first $L$ steps from $m$. Iterating the actual affine recurrences gives

$$
 \frac{2^Lq}{3^P}
 =m+\sum_{\substack{0\le i<L\\T^im\ \mathrm{odd}}}\frac{2^i}{3^{P_{i+1}}}
 \le m+2^L,
$$

where $P_{i+1}$ counts the odds through clock $i$. Since $q\ge m/2$ and $m\ge2^L$, it follows that $3^P\ge2^{L-2}$. For all sufficiently large $L$ this implies $P\ge3L/5$, as $\log_3 2>3/5$ follows from $2^5>3^3$. Prescribing $L$ shortcut parities fixes one residue modulo $2^L$. Each such residue supplies at most $Y/2^L+1$ possible origins. The upper binomial tail with $P\ge3L/5$ has at most $2^{L H_2(3/5)}$ words by the ordinary entropy bound. Thus long entries contribute at most

$$
 O\!\left(Y^{1-\delta(1-H_2(3/5))}\right).
$$

All three exponents are strictly below one, and bounded $L$ is absorbed into the constant. This proves the asserted power saving on **one fixed hypothetical escape**. Because the old separation bound gives at most $N/4+o(N)$ marked dates there, at least $3N/4-o(N)$ of the first $N$ edges actually increase $b_*$ by exactly one. Power-sparse but large discounts can still contribute order $N$ in total. The proof controls their number alone and supplies no universal descent.
