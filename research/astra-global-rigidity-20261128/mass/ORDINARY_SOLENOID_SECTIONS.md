# Compact quotient sections on a supplied escaping component

Use the compact solenoid $\mathcal S=(\mathbb R\times\mathbb Q_3)/\operatorname{diag}\mathbb Z[1/3]$, its projection $\pi$, and the finite partition $\mathcal Q_k$ of its fundamental domain $[0,1)\times\mathbb Z_3$ by real intervals of width $3^{-k}$ and ternary residue classes modulo $3^k$. There are $3^{2k}$ cells with uniform Haar mass vector $u_k$. Weaver proves dyadic pushforward equidistribution for the full joint stationary law; the following sampling instead fixes one supplied ordinary component and keeps its conditional real fibres before projection. [Weaver, Paper 19/v2, §10.6, (Q1)–(Q6)](https://rstation.ai/problems/collatz/papers/19).

Suppose a positive odd ordinary orbit escapes. Write $y$ for its successive vertices, $F(y)$ for its forward survival, $P(y)=y/F(y)$, and $\gamma_y=\pi_*(\mu_y\otimes\delta_y)$ for the projection of the canonical real fibre over its **actual integer ternary coordinate**. Let $y_j$ be the first ray vertex where $P(y_j)\ge2^j$, for all sufficiently large $j$. Since $P(Uy)/P(y)=3/2^{v_2(3y+1)}\le3/2$, the corrected height $\lambda_j=P(y_j)$ is in $[2^j,(3/2)2^j]$. Finitely many initial indices are immaterial.

For any nonnegative integer depths $k_j$, the following hold.
* If $k_j=o(j/\log j)$, then
\[
       J^{-1}\sum_{J\le j<2J}
           \|\mathcal Q_{k_j}\gamma_{y_j}-u_{k_j}\|_{\rm TV}
                         \longrightarrow 0.                            \tag{1}
\]
* If $k_j=o(j)$, then the logarithmic crossing average satisfies
\[
       (\log J)^{-1}\sum_{1\le j\le J}j^{-1}
           \|\mathcal Q_{k_j}\gamma_{y_j}-u_{k_j}\|_{\rm TV}
                         \longrightarrow 0.                            \tag{2}
\]
* On the other hand, along **every** sequence of late vertices $y$ and integer depths $k=k(y)$ such that $3^k\sqrt{\log y}/y\to\infty$,
\[
                 \|\mathcal Q_k\gamma_y-u_k\|_{\rm TV}\longrightarrow1. \tag{3}
\]
Total variation here is the supremum convention. In particular (1) gives equidistribution in density of the individual finite cell laws at every fixed resolution, even when the crossing list is restricted to any deterministic set of crossing indices of positive lower relative frequency in the tested dyadic blocks. The known full stationary dyadic pushforward theorem and (1) have different sampled measures.

## Entropy of the actual component parameter

In the [frozen bilateral ordinary coupling](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md), let $J_C=\prod w(Z_v)$ have law $\eta$. Conditional on $Z_n=y$ at ray grade $n$, $R_y-y=-P(y)J_C$. The grade event has probability tending to one, so in total variation uniformly over tests depending on $y$,
\[
    \gamma_y\quad\text{differs by }o(1)\text{ from }
               \mathcal L\big(\pi(-P(y)J_C,0)\big).
\]
We subtracted the actual diagonal integer $y$ in both coordinates. Given a grade-zero site $x$, $J_C=F(x)(1-R_x/x)$ under the canonical fixed-root law there. Thus $\eta$ is a countable mixture of fixed affine images of the real fibres in the [fixed-root logarithmic cell theorem](FIXED_FIBRE_CELL_MASS.md).

For each $\delta>0$ discard at most $\delta$ mass and normalize the rest to a law $\sigma$ on $[0,1]$. It can be chosen so its mass on every real interval of length $r\le1/2$ is at most $C_\delta r(1+\log(1/r))^4$. Indeed retain finitely many ordinary sites and at each a single restriction of arbitrarily high mass from (2) of the fixed-root proof; the finitely many fixed affine scalings only modify the constant. Let $D_m=m\log2-H(\mathcal D_m\sigma)$, where $\mathcal D_m$ is the dyadic partition of $[0,1)$ at depth $m$. Then $D_m$ is nonnegative and nondecreasing, and
\[
                         D_m\le 4\log(m+2)+O_\delta(1).                \tag{4}
\]
The entropy bound follows by integrating the logarithm of the dyadic cell density, bounded above by the interval estimate. We can work with $\sigma$ throughout (1) and (2), then send $\delta\downarrow0$ since normalized restriction changes total variation by at most the discarded mass.

## A block estimate allowing the actual, nonintegral height dilation

For any real $s$, the label $\mathcal Q_k\pi(s,0)$ is a bijective recoding of $\lfloor3^k s\rfloor\bmod3^{2k}$. In fact the fundamental-domain coordinates are $(\{s\},-\lfloor s\rfloor)$. Thus at height $\lambda_j$ this is the equal partition of $(-\lambda_j x/3^{k_j})\bmod1$ into $Q=3^{2k_j}$ cells, with $x\sim\sigma$. Write $d_j=\lfloor\log_2(\lambda_j/3^{k_j})\rfloor$. For an integer buffer $L\ge1$ and $d_j>L$, let $u=d_j-L$ and $v=d_j+\lceil\log_2 Q\rceil+L+2$. One has
\[
  \big\|\mathcal Q_{k_j}\mathcal L(\pi(-\lambda_j x,0))-u_{k_j}\big\|_{\rm TV}
               \le C2^{-L}+C\sqrt{D_v-D_u}.                           \tag{5}
\]
Conditional on one $\mathcal D_u$ parent, replace its fine-child probabilities on $\mathcal D_v$ by uniform ones. Chain rule and Pinsker bound the averaged total-variation cost by $\sqrt{(D_v-D_u)/2}$. Under normalized Lebesgue measure in the parent interval the scaled coordinate spans at least $2^L$ full periods up to two endpoint fragments. Its distribution among equal cells is within $C2^{-L}$ of uniform. A fine child has scaled length at most $2^{-L}/Q$. The normalized Lebesgue mass of the fine children meeting any label boundary inside the parent is $O(2^{-L})$: the parent spans $O(2^L Q)$ such boundaries and each costs at most two child lengths. Their original mass is bounded by this uniform mass plus the preceding conditional total-variation cost. Selecting the label at a representative point of each remaining child is exact. This proves (5), including translated boundaries.

For (1), on $J\le j<2J$ put $K=\sup k_j=o(J/\log J)$ and take $L=\lceil\log_2(J+2)\rceil$. Each index $i$ of an entropy increment $D_i-D_{i-1}$ lies in at most $O(K+L)$ of the intervals $(u,v]$ because each is within $O(K+L)$ of $j$. All indices are at most $3J$ for large $J$. Equation (4) gives a bound $O_\delta((K+L)\log J/J)$ on the average of $D_v-D_u$. Apply (5) and Cauchy–Schwarz.

For (2) choose $L_j=\lceil\log_2(j+2)\rceil$. When $k_j=o(j)$ all the entropy indices in $(u_j,v_j]$ equal $j+o(j)$. For every $\epsilon>0$ and all sufficiently large $i$,
\[
       \sum_{j:\,u_j<i\le v_j}1/j\le C\epsilon
\]
because the eligible large $j$ lie in $[i(1-C'\epsilon),i(1+C'\epsilon)]$, upon taking $k_j+L_j\le\epsilon j$ eventually. The finitely many initial $j$ cause $O(1)$ in the weighted sum. Expand $D_{v_j}-D_{u_j}$ into its nonnegative increments and exchange the sums. By (4) the result through $j\le J$ is $O(1)+C\epsilon D_{2J}=O(1)+O_\delta(\epsilon\log J)$. Let $\epsilon$ tend to zero. Weighted Cauchy–Schwarz and (5) give (2).

## Resolving the singular carrier

For each small fixed tolerance retain finitely many grade-zero sites $x$ of the component and at each retain a positive-measure piece of arbitrarily high conditional probability that lies in Weaver's $V_{N,1/i}(x)$ for every sufficiently large $N$, with fixed $i$. As in the [macroscopic unit-bin energy calculation](MACROSCOPIC_REAL_ENERGY.md), the resulting high-mass part of $J_C$ at every mesh $r$ has a cover by $O(1/(r\sqrt{\log(1/r)}))$ intervals of length $O(r)$; constants may depend on the retained part. Take $r=1/(P(y)3^k)$. After the actual dilation the intervals have length $O(3^{-k})$, and each meets only $O(1)$ quotient cells, also at the wrap. Their total Haar proportion is at most
\[
            O\!\left(\frac{P(y)}
                  {3^k\sqrt{\log(P(y)3^k)}}\right).
\]
This vanishes under the hypothesis of (3), since $P(y)/y\to1$. These cells have projected ordinary probability arbitrarily close to one. Conditional coupling costs $o(1)$, proving (3). In particular low-resolution quotient equidistribution of an actual escaping fibre is compatible with high-resolution singular concentration. The interval between the displayed regimes remains undetermined, and the results do not supply an upper on its physical macroscopic pair energy.
