# Critical geometric floors and unit-scale approximation on actual positive orbits

**Source-qualified written theorems.** Let $U(y)=(3y+1)/2^{e(y)}$ at a positive odd integer, $w_y=3y/(3y+1)$, $t_y=1-w_y$, $a_y=h(y)/y$, $\kappa=\log(4/3)/2$ and $H$ the original escaping charge. The ordinary stationary loss identity $\sum_y t_ya_y=\kappa-H$ is [Weaver, Paper176/v1, Theorem 2 following (4)](https://rstation.ai/problems/collatz/papers/176/v1). Uniform reciprocal packing on each distinct positive trajectory supplies the convergent correction on an escaping path. The fast quantitative version also uses the stated two-logarithm lower bound. No hypothesis on the existence of an escaping path is needed for the all-site stationary bound.

Write $g_1=3/2$, $g_e=2^e/3$ at $e\ge2$, $\ell_e=\log g_e>0$, and take $\theta\in[0,1)$. On an edge of exponent $e$, count the number $C_\theta(y)$ of levels of the grid $g_e^{\mathbb Z+\theta}$ between the smaller endpoint inclusive and the larger endpoint exclusive. A self-edge counts zero. The whole raw original edge measure, including any stationary cycle laps, satisfies
\[
 \int_0^1\sum_{y\ {\rm odd}} w_ya_y|C_\theta(y)-1|\,d\theta
                       \le \frac{\kappa-H}{\log(4/3)}.                 \tag{1}
\]
Consequently for almost every *single* phase the exact directed grid sample and the original uncut edge measure differ by a finite-total-variation measure over the entire positive graph. This applies also on retaining the original donor and date as marks in any positive decomposition of this stationary occupation, including the [preminimum/postminimum split](POSTMINIMUM_FLUX.md). The variation is bounded by the same quantity after projection or restriction. It permits the raw total occupation itself to be infinite.

There is a deterministic conclusion for **every** phase, including a separate phase $\theta_e$ chosen for each exponent. If $r_i=U^im$ is any ordinary escaping path, then
\[
          \sup_{(\theta_e)}\frac1N\sum_{i<N}|C_{\theta_{e(r_i)}}(r_i)-1|
                                 \longrightarrow0 .                    \tag{2}
\]
For every superpolynomially escaping path, meaning $\log r_i/\log i\to\infty$, the count in (2) before division is $O_m(\sqrt N)$. The fixed-base arithmetic statement behind (2) is not confined to edges of a particular exponent. For any $g=3^p2^{-q}>1$ with coprime integers $p,q$ and every fixed $0<c<1$,
\[
  \sup_{\theta\in[0,1)}
      \#\{i<N:[r_i,r_i+c)\cap g^{\mathbb Z+\theta}\ne\varnothing\}
                           =o_{m,g,c}(N).                              \tag{3}
\]
Any nonprimitive integer power of such a base is covered by containment in a translate of its primitive grid. The interval in (3) has absolute length less than one **at the original positive representative**. Its location involves the true orbit, and the progression translate is allowed to change with $N$. A sparse subset of dates is not ruled out.

## Exact distortion and phase averaging

The ideal uncorrected edge $y\mapsto 3y/2^e$ has logarithmic length $\ell_e$, so its half-open interval contains exactly one point of the specified grid, including when an endpoint is itself a grid level. Put $d_y=-\log w_y=\log(1+1/(3y))$. The positive $+1$ adds logarithmic length $d_y$ on an up-edge and removes it on a down-edge. At the known fixed odd site $1$, $e=2$ and $d_y=\ell_e$ remove the entire interval. Since $0<d_y\le\log(4/3)\le\ell_e$, the count differs from one by at most one. More precisely, the exceptional upper strip on an up-edge is $[g_1y,g_1(y+1/3))$, and the missing lower strip on a down-edge is $[y/g_e,(y+1/3)/g_e)$. Multiplication or division by one grid ratio preserves the grid. In both cases the exact condition is therefore
\[
   |C_\theta(y)-1|=1
           \quad\Longleftrightarrow\quad
             [y,y+1/3)\cap g_e^{\mathbb Z+\theta}\ne\varnothing.       \tag{4}
\]
The phase mean of this indicator is exactly $d_y/\ell_e$, including equality. Tonelli and $w_y(-\log w_y)\le1-w_y$ give (1). More precisely the expectation of the sum with weight $w_ya_y\ell_e$ equals $\sum_y w_ya_yd_y$, between $3\log(4/3)(\kappa-H)$ and $\kappa-H$ since $w_yd_y/t_y=3y\log(1+1/(3y))$. For a single escaping path the sum $\sum_i d_{r_i}$ converges, giving only finitely many defective edges for almost every phase. Countably many ordinary starting points permit the same full-measure set of phases for all escaping trajectories. Neither expectation argument gives (2) at a specified phase.

## The physical integer and its digitization error

Put $S_0=0$, $S_i=\sum_{j<i}e(r_j)$ and $P(m)=m/F(m)$. Since the positive orbit is distinct, $F(m)>0$, $F(r_i)\to1$ and $r_i\to\infty$. The exact log coordinate is
\[
    \log r_i=\log P(m)+i\log3-S_i\log2+\log F(r_i),
              \qquad S_i\le i\log_23+O_m(1).                          \tag{5}
\]
For $i<j$ let $A=3^{j-i}2^{-(S_j-S_i)}$. Iteration with the positive affine offset gives
\[
 r_j=A(r_i+\Xi_{i,j}),\qquad
 \Xi_{i,j}=\tfrac13\sum_{s=0}^{j-i-1}2^{S_{i+s}-S_i}3^{-s}
           \ge 1-(2/3)^{j-i}.                                         \tag{6}
\]
In particular $\Xi_{i,j}\ge1/3$. Also $r_j/(Ar_i)=F(r_j)/F(r_i)\to1$ uniformly over $j>i$ as $i\to\infty$.

Suppose first $p\ne0$ in (3), and set $K_i=q i-pS_i\in\mathbb Z$, $\ell=\log g$. Consider two candidate visits $i<j$ with the *same* $K_i=K_j$. Coprimality gives $p\mid j-i$, and $A=g^{(j-i)/p}$ maps the grid to itself. For sufficiently large $i$ a grid point $G_i\in[r_i,r_i+c)$ is unique. At two candidate visits, $G_j/(A G_i)\to1$ uniformly in $j>i$ and in the grid phase, by (5)–(6). As this ratio is an integer power of the fixed $g>1$, it must then equal one. Choose $T_c$ with $1-(2/3)^{T_c}\ge c$. If $j-i\ge T_c$ then $A G_i<A(r_i+\Xi_{i,j})=r_j$, which contradicts $G_j\ge r_j$. Each distinct $K$ is therefore used by at most $T_c$ sufficiently late candidate dates. At the critical aperture $c=1/3$ it is used at most once.

For each candidate, multiplying (5) by $p$ and using $p(i\log3-S_i\log2)=i\ell+K_i\log2$ shows that
\[
         \frac{K_i\log2}{\ell}\pmod1
          \text{ lies within }o_{m,p,q,c}(1)
          \text{ of }p\theta-\frac{p\log P(m)}{\ell}\pmod1.            \tag{7}
\]
The error tends uniformly to zero on all candidates past a fixed late index because $G_i/r_i=1+O(c/r_i)$ and $F(r_i)\to1$. The rotation $\log2/\ell$ is irrational by multiplicative independence of two and three and $p\ne0$. The possible $K_i$ through date $N$ lie in an integer interval $[-C_{m,p,q}N,C_{m,p,q}N]$. For each fixed arc length its visits under this irrational rotation are equidistributed uniformly in the arc center. This follows, for example, by upper and lower approximation on a fixed fine circular partition and the geometric sum for finite trigonometric polynomials. Bound the late candidates by $T_c$ times the number of integer rotation visits to the arc in (7), normalize, and then decrease its length to zero. The early indices are finite uniformly in $\theta$. This proves (3). For pure binary powers the primitive case is $g=2$. Now $\log_2r_i=i\log_23+\log_2P(m)+o(1)\pmod1$, so the same arc count applies directly using $i$. This case requires no coefficient class.

For each fixed $e$ apply the argument at $c=1/3$ to $g_e$, even before filtering by the actual exponent. For the exponent-one grid, the coefficient class is $\pm E_i$ where $E_i=S_i-i$ is the total number of even shortcut departures. Hence the number of defects **on exponent-one edges** is $o_m(1+E_N)$ uniformly over its phase, since the integer rotation now runs only through $[0,E_N]$. One has $E_N\to\infty$ on escape, as a positive starting point cannot have a terminal infinite run of ones. For any fixed $M$, the total of all defects at exponents $e\le M$ is $o_{m,M}(N)$ uniformly in their separately chosen phases. There are at most $S_N/M$ sites of exponent $e>M$. Increase $M$ and use (5) to obtain (2).

This uniform bound holds with the original measures on donors, even when the actual directed occupations are not known to have a uniform upper at any floor. With $\gamma_m$ from [the postminimum law](POSTMINIMUM_FLUX.md), one has
\[
  \sup_{(\theta_e)}\frac1N
      \sum_m\gamma_m\sum_{i<N} b_{i+1}(m)
      |C_{\theta_{e(U^im)}}(U^im)-1|\longrightarrow0.                  \tag{8}
\]
On escaping donors use (2) and $b_{i+1}\le1$. On each bounded donor the sum of all $b_{i+1}$ over its future is finite by geometric survival on its eventual cycle. The individual normalized bound is always one, and $\sum_m\gamma_m\le\kappa$, so dominated convergence after taking each individual supremum proves (8). It also holds with $\eta_m$ in place of $\gamma_mb_{i+1}$ on the escaping population. The coordinate aggregated in (8) is the chronological date from each donor's attained minimum.

## A square-root bound on every superpolynomially growing escape

Use the homogeneous two-logarithm consequence $|u\log2+v\log3|\ge c(1+|u|+|v|)^{-4.25}$ for nonzero integer coefficients, from the primary estimate of Bondareva, Luchin and Salikhov used in [the relative landing theorem](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md). [Primary Theorem 1](https://www.mathnet.ru/eng/cheb619).

Write $M(I)=\min_{j\ge I}r_j$. If the uniform distinct-path reciprocal tail above $t$ is $O(t^{-q_0})$, then $|\log F(r_i)|\ll M(I)^{-q_0}$ for $i\ge I$, by summing $\log(1+1/(3r_j))$ and decreasing $q_0$ to at most one. At defects of the same actual exponent $e$ use (5) directly with base $g_e$, choosing $p=1,q=1$ for $e=1$, and $p=-1,q=-e$ for $e\ge2$. Thus $|p|=1$ and all log errors before reduction modulo $\ell_e$ are $O(M(I)^{-q_0})$ with a constant independent of $e$. Subtract two instances of (7) before dividing by $\ell_e$. With $K_i\ne K_j$ this gives a nonzero integer two-log form of size $O(M(I)^{-q_0})$. Its coefficients are $O_m((1+N)^2)$ uniformly through $j<N$: by (5) each observed $e=O_m(N)$, $|K_i|\ll_m N^2$, and each grid index of a point through this date is $O_m(N)$ since $\log r_j\ll_m N$ and $\ell_e\ge\log(4/3)$. Multiplicative independence shows that a zero form would give the same $K$. The two-log bound therefore rules out two different $K$ once $M(I)$ exceeds a sufficiently large fixed power of $N$. The equal-$K$ argument in (6) is uniform in $e$ here because $|p|=1$, $c=1/3$ and all grid ratios are at least $4/3$.

It follows that after this $I$ there is at most one defective site *of each exponent* through $N$. If $\log r_i/\log i\to\infty$, take $I=\lceil N^{1/3}\rceil$; its tail minimum eventually exceeds every fixed power of $N$. The number of distinct observed exponent values is $O_m(\sqrt N)$ because their sum is at most $S_N=O_m(N)$. This proves the square-root claim uniformly over all choices of phases. With $\liminf i^{-1}\log r_i>0$, two distinct sufficiently late defects of the same fixed exponent at $i<j$ must satisfy $j\ge\exp(c_m i)$ after a possible change of constants (allowed to depend also on the fixed exponent), by the same two-log comparison. These quantitative conclusions retain their growth hypotheses. An upper bound on the unrelated raw crossing multiplicity of a slowly growing donor does not follow from the grid approximation.

[The finite rational control](check_postminimum_grid.py) checks the ideal and actual interval endpoints against the one-third strip at six phases through 4,096 positive odd sites. It compares powered rationals exactly and includes both possible error directions. The same control checks true truncated minimum splits, discounted signed occupation and the normalized affine lower on 37,422 short physical segments. Both Python modes reproduce [the finite receipt](../../../reports/astra-global-20261128/escape/POSTMINIMUM_GRID_CHECKS.json).

[NativeOffsetFloor.lean](NativeOffsetFloor.lean) proves the integer form of (6) for every supplied segment of positive native gaps, $3^j(x+1)\le2^s y+2^j$, and $3^{j-1}(3x+1)\le2^s y$ at every nonzero grade $j$. It uses the actual valuation and landing at every edge. The proof of (3) additionally uses uniform high simple-path correction, multiplicative independence, and irrational rotation.
