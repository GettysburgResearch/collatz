# Reset clocks at one fixed source

**Written result, independent reconstruction of a weaker known positive-integer conclusion.** For each positive odd ordinary source, let $a_i=v_2(3x_i+1)$ be its actual successive odd division exponents, and put $d_i=\sum_{h<i}(a_h-1)$. Then
\[
             \lim_{i\to\infty}d_i/\log(i+2)=+\infty.                 \tag{1}
\]
In particular $x_i=o_{x_0,M}((3/2)^i/i^M)$ for each fixed $M>0$. These are all-clock limits without an escape assumption. Published online before this investigation, rStation paper 174/v1, Theorem 1 and §6, gives a stronger proposed bound on the number of separate rise groups on a fixed aperiodic ordinary trajectory, of order $\log i\log\log i$. The elementary periodic cases supply (1) as well. The independent argument below establishes (1) by the qualitative Subspace Theorem. It also applies to algebraic $2$-adic sources, as stated precisely below. No priority claim is made. [Paper 174/v1](https://rstation.ai/problems/collatz/papers/174/v1)

## An algebraic two-adic version

Write $T(2v)=v$, $T(2v+1)=3v+2$ on $\mathbb Z_2$. For any $\xi\in\mathbb Z_2$ algebraic over $\mathbb Q$, any symbol that occurs infinitely often in the shortcut parity sequence has counting function $K(N)$ satisfying $K(N)/\log(N+2)\to\infty$. This includes both symbols whenever the sequence contains infinitely many zeros and ones. No real sign or growth assumption on $\xi$ is needed.

Let $n_j$ be the zero-based native position of occurrence $j\ge1$ of the chosen symbol and $p_n$ the number of odd departures in the first $n$ steps. If the symbol is zero, put $c=\xi+1$ and $u_j=2^{n_j}/3^{p_{n_j}}$. A shifted even departure sends $y=x+1$ to $(y+1)/2$ and a shifted odd departure to $3y/2$. Consequently, after $n$ native steps,
\[
 c+\sum_{n_j<n}u_j=2^n3^{-p_n}(T^n\xi+1).
\]
At a zero departure $T^{n_j}\xi+1$ is odd. For the symbol one put $c=\xi$ and $u_j=2^{n_j}/3^{p_{n_j}+1}$ instead. Then the same formula has $T^n\xi$ without the shift on its right. That value is odd at each chosen one. In both cases, putting $B_j=c+\sum_{h\le j}u_h$, we have
\[
             v_2(B_j)=n_{j+1},\qquad v_2(u_j)=n_j.               \tag{2}
\]
These equalities hold already on finite prefixes containing the specified next departure. When the symbol is zero, $p_{n_j}=n_j-j+1$. When the symbol is one, $p_{n_j}=j-1$. Thus for indices a bounded distance apart with bounded position difference, their $u$ ratio takes only finitely many positive rational values. Their absolute logarithmic heights are $O(n_j+1)$. Also $h(B_j)=O_\xi(n_j+1)$: the common denominator of the rational summands divides $3^{n_j+1}$ and the sum of their ordinary positive numerators after clearing it is at most $j\,2^{n_j}3^{n_j+1}$. Adding the fixed $c$ changes the bound by a fixed multiplicative constant on the logarithmic scale.

Suppose $\limsup_j\log(n_j+2)/j>0$. Choose $\gamma>0$ strictly below this limsup. There are infinitely many strict new maxima of $\log(n_m+2)-\gamma m$. At these, set $m=j+1$, $T=n_{j+1}+2$. For every fixed $k$ and all sufficiently large such $j$,
\[
 n_{j+1}-n_j\ge(1-e^{-\gamma})T,
 \qquad n_{j-k}+2\le e^{-(k+1)\gamma}T.                       \tag{3}
\]
Work in $K=\mathbb Q(\xi)\subseteq\mathbb Q_2$ and use the usual product-formula normalized absolute values. The chosen place $v$ has $|b|_v=2^{-v_2(b)/[K:\mathbb Q]}$. Take for $S$ all infinite places, all places above two and three, and any remaining denominator places of $c$. For fixed $k$ pass to a subsequence so each of the finitely many adjacent gaps among $n_{j-k+1},\ldots,n_j$ is a fixed integer or tends to infinity. Merge runs of bounded gaps into clusters. Take the last $u$ of each cluster as a coordinate $U_l$. Let $C_l$ be the sum of that cluster divided by $U_l$. The bounded-ratio property allows another subsequence on which all the positive rationals $C_l$ are fixed. Write $r$ for the number of clusters, $U_r=u_j$, and $X=(B_{j-k},U_1,\ldots,U_r)$. At every place except $v$ use coordinate forms. At $v$ replace the last coordinate form by $X_0+\sum_l C_l X_l$. This replacement is invertible because $C_r>0$. Its value is exactly $B_j$.

Each $U_l$ is an $S$-unit. Outside $S$ the local max norm of $X$ equals one. By (2) the whole unnormalized product of the selected forms over $S$ is at most
\[
 \exp\{[C_\xi(n_{j-k}+1)]-(\log 2)(n_{j+1}-n_j)/[K:\mathbb Q]\}.       \tag{4}
\]
Indeed the coordinate product for $B_{j-k}$ is at most $e^{h(B_{j-k})}$, and the cost of replacing $U_r$ is exactly $|B_j/U_r|_v$. Choose fixed $k$ large enough in (3) to make (4) at most $e^{-\delta T}$ with $\delta>0$. The projective height of $X$ is at most $e^{O_{\xi,k}(T)}$ by the individual height bounds. Thus (4) is at most $H(X)^{-\epsilon}$ for some fixed $\epsilon>0$. Because all outside-$S$ max norms equal one this is the projective Subspace Theorem inequality. The fixed dimension is at least two. The theorem places these vectors in finitely many proper $K$-linear subspaces. [Evertse, *An improvement of the quantitative Subspace theorem*, Compositio Math. 101 (1996), pp. 225–228](https://numdam.org/item/CM_1996__101_3_225_0.pdf)

One proper subspace must occur infinitely often. Change coordinates by the fixed invertible partial-sum transformation, replacing $X$ by the successive values $B_{j-k}$ and $B_h$ at the last index $h$ of each cluster. By (2) their valuations are the positions at the beginning of the first cluster, the beginning of each subsequent cluster, and the next occurrence $n_{j+1}$. Each successive difference tends to infinity by cluster separation and the terminal gap in (3). A fixed nonzero $K$-linear relation is impossible, since its first nonzero summand eventually has uniquely smallest valuation at $v$. This contradiction proves $\log(n_j+2)/j\to0$. If $K(N)=j$ then $N\le n_{j+1}$, proving the asserted all-clock limit.

## Return to the ordinary trajectory

An ordinary positive source has infinitely many native zeros. Otherwise the trajectory is all odd from a finite time, and each subsequent step multiplies its shifted positive integer by $3/2$. This would make the shifted source divisible by every power of two. At native time $A_i=\sum_{h<i}a_h$, exactly $d_i=A_i-i$ zeros have occurred. Since $A_i\ge i$, the preceding theorem gives (1).

For the growth corollary put $N_i=2^{d_i}x_i$. Then $N_{i+1}=(3N_i+2^{d_i})/2\le2N_i$, so $d_i\le i+\log_2 x_0$. Exact iteration gives
\[
 \frac{x_i}{(3/2)^i}=x_0 2^{-d_i}+\frac13\sum_{t<i}(2/3)^t2^{d_t-d_i}.
\]
Split the sum at $B\log(i+2)$. Before the split $2^{d_t}\le x_0 2^t\le x_0(i+2)^{B\log2}$. After the split $2^{d_t-d_i}\le1$, so this part is $O((i+2)^{-B\log(3/2)})$. Choose $B$ large for the supplied $M$ and use (1) on the first part. No uniform onset in the source is asserted.

**Remaining obstruction.** The multicoordinate saving is the final gap $n_{j+1}-n_j$ in (4). At clocks such as $n_j\asymp j^2$ the $k$-step-earlier height scale is still $\asymp j^2$ while the saving is only $O(j)$, for every fixed $k$. Such clocks are model sequences, not asserted ordinary examples. Neither (1) nor the stronger paper-174 growth count gives the linear drift and control of critical excursions needed for fixed-source trapping. The method does not exclude any positive cycle.
