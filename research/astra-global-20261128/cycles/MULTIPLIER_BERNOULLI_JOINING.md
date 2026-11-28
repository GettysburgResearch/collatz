# Independent physical parity at nonsmooth proportional sources

Let $T$ be the ordinary shortcut Collatz map on $\mathbb Z_2$ and let $n$ have Haar law. Fix positive odd multipliers $A,B$ with $A/B\notin 3^{\mathbb Z}$ and ordinary integer offsets $a,b$. For almost every $n$, the empirical measures
\[
    \frac1N\sum_{m<N}\delta_{(T^m(An+a),\,T^m(Bn+b))}
                    \quad\longrightarrow\quad
                 \mathrm{Haar}_{\mathbb Z_2}\otimes\mathrm{Haar}_{\mathbb Z_2}
                                                                         \tag{1}
\]
converge weakly. In particular every specified pair of binary parity words of equal fixed length $k$ occurs at synchronous physical dates with limiting frequency $4^{-k}$. The fraction of mixed departures tends exactly to one half. At any fixed observation depth the two paths still use a single source and have at most $2^k$ possible length-$k$ pairs when observed from date zero.

For any fixed finite collection $A_i n+a_i$ whose positive odd multipliers have pairwise ratios outside $3^{\mathbb Z}$, the linearly interpolated processes
\[
         t\longmapsto
          \left(\frac{2k_{\lfloor Nt\rfloor}(A_i n+a_i)-\lfloor Nt\rfloor}
                          {\sqrt N}\right)_i                              \tag{2}
\]
at the grid dates converge jointly in law to **independent standard Brownian motions**. Here $k_m$ is the genuine number of odd departures in $m$ steps. For ordinary integer sources in $[X,2X)$ both results transfer in probability for empirical finite parity words and in distribution for the processes on $[0,1]$ whenever $N\to\infty$ and $2^N=o(X)$. This proves a joint functional central limit theorem up to the binary observation horizon. The statements involve neither ordinary postcritical hitting times nor independent entire parity words for three or more coordinates.

The proof uses the arithmetic waiting and two-adic logarithm estimates of [the Hamming calculation](MULTIPLIER_PARITY_SEPARATION.md). Integer offsets change the intercept of its native affine line only, so its fair-sign, waiting-time and slope-valuation proofs apply verbatim. In the complementary case $A/B\in3^{\mathbb Z}$ and zero offsets, the source-qualified counted synchronization in that calculation gives eventual equal-time parity agreement for Haar-almost every source. In particular, for ordinary positive odd dilates the smooth-group boundary is exact.

## The direction distribution at physical times

Write $X_m=T^m(An+a)$, $Y_m=T^m(Bn+b)$ and $D_m=k_m(Bn+b)-k_m(An+a)$. Given the source modulo $2^m$ both states are affine functions of one fresh Haar variable, with respective odd slopes $A3^{k_m(An+a)}$ and $B3^{k_m(Bn+b)}$. Consequently their conditional law is uniform on the graph
\[
          Y=\alpha_m X+\beta_m,\qquad
          \alpha_m=(B/A)3^{D_m},\quad \beta_m\in\mathbb Z_2.             \tag{3}
\]
Both parameters are measurable before the next source bit is revealed. Write $v(d)=v_2(B3^d-A)$, so $v(D_m)=v_2(\alpha_m-1)$. The nonsmooth hypothesis makes each valuation finite.

Let $\tau_j$ be the time just after the $j$th mixed departure, with $\tau_0=0$, and set $S_j=D_{\tau_j}$. The intervals $[\tau_j,\tau_{j+1})$ have constant direction $(B/A)3^{S_j}$, including the final mixed departure; the direction changes immediately afterward. At the mixed clock $S_j$ is a genuine simple symmetric walk. For $W_j=\tau_{j+1}-\tau_j$ and its starting history,
\[
             \mathbb E_j W_j\le2+v(S_j),\qquad
                         \operatorname{Var}_j W_j\le2.                   \tag{4}
\]
These are physical native statements: if the state difference is already distinguishable below the slope valuation, the common run length is fixed and shorter; otherwise it is that valuation plus an ordinary geometric two-adic valuation of the fresh input. The last new mixed sign uses the next fair bit. [Native affine prefix kernel](MixedParity.lean)

Fix $k\ge3$ and an odd direction residue $u\pmod{2^k}$. The possible $d$ with $(B/A)3^d\equiv u\pmod{2^k}$ form either the empty set or one class $J$ modulo $q=2^{k-2}$, the order of three there. Below all averages in $j$ are simultaneous for all of the countably many fixed choices of $k,u$. The empirical frequencies of fixed residue classes of $S_j$ are their uniform frequencies, including when the finite walk has period two, by the Poisson-equation estimate in the Hamming calculation. In addition that proof gives
\[
      \frac1m\sum_{j<m}v(S_j)\to \bar v,
      \qquad \bar v=3/2\ \text{or }5/2.                                \tag{5}
\]
It controls the growing valuation tail using Bugeaud–Laurent's Theorem 3 for the fixed odd rational units in the second case. To localize this assertion, truncate at any fixed $L\ge3$. Both $\min(v,L)$ and $\min(v,L)1_J$ are periodic. The means of $\min(v,L)$ over a period tend to $\bar v$ as $L\to\infty$, by the exact single-class counts for $v\ge l$, or the bounded alternating values in the first case. Subtract the fixed-truncation limit from (5). The time mean of $(v-L)_+$ therefore tends to the nonnegative corresponding tail with limit zero as $L\to\infty$. Since $0\le(v-L)_+1_J\le(v-L)_+$, this proves that the total time mean of $(2+v(S_j))1_J$ is its limit of periodic truncated means.

For $u\not\equiv1\pmod{2^k}$ the valuation on $J$ is fixed below $k$. For $u\equiv1\pmod{2^k}$, conditionally on this occupied class the uniform fractions satisfying $v\ge k+l$ are $2^{-l}$ for $l\ge1$, from the orders $2^{k+l-2}$. Such a class is occupied only in the second case of (5). It follows in either case that the limiting mean of $(2+v)1_J$ is at most $(k+3)/q$. The weighted fluctuation
\[
        \frac1m\sum_{j<m}1_J(S_j)(W_j-\mathbb E_jW_j)\to0
\]
almost surely by the martingale strong law and (4). Finally $W_m=o(m)$ almost surely: the unweighted partial sums of $W_j-\mathbb E_jW_j$ are $o(m)$, and those of $v(S_j)-\bar v$ are $o(m)$, so their successive differences give $W_m\le2+\bar v+o(m)$. Since $\tau_m\ge m$, the unfinished terminal interval has vanishing effect. Hence the physical direction capacity is
\[
    \limsup_{N\to\infty}\frac1N\#\{m<N:\alpha_m\equiv u\pmod{2^k}\}
                            \le 4(k+3)2^{-k}.                             \tag{6}
\]
This proof accounts for the actual length of each residence. Uniformity over all $u$ at a fixed $k$ follows from finiteness. Increasing an absolute constant covers $k=1,2$.

## The physical joining is a mixture of dyadic lines

Take the empirical measures of the quadruples $(\alpha_m,\beta_m,X_m,Y_m)$ on the compact product of the odd units and three copies of $\mathbb Z_2$. Fix a cylinder test $f$ depending on the pair of states modulo $2^k$ and put
\[
    L_f(\alpha,\beta)=2^{-k}\sum_{x\bmod2^k}f(x,\alpha x+\beta).
\]
Conditional on the history through bit $m-1$, (3) gives expectation $L_f(\alpha_m,\beta_m)$ for the actual test. Its value is known after the next $k$ bits. For each residue of $m$ modulo $k$, the differences between these two quantities are bounded martingale differences at the successive $k$-bit boundaries, and their averages vanish almost surely. This remains true after multiplying by any fixed bounded cylinder test of $(\alpha_m,\beta_m)$ already known at the initial history. Take the countable family of cylinder indicators in all four coordinates.

Thus in every subsequential limit the marginal $\nu$ of the pair $(X,Y)$ is the mixture of the uniform line laws $Y=\alpha X+\beta$ with parameter probability given by that same limit. This retains any correlation of direction and intercept. Its direction marginal $\sigma$ satisfies $\sigma(u+2^k\mathbb Z_2)\le C(k+3)2^{-k}$ by (6), since those cells are clopen. Independently, $\nu$ is invariant under $T\times T$: for a continuous test the time average of its one-step difference telescopes. The map $T$ is continuous on $\mathbb Z_2$.

## Incidence, entropy and the unique stationary law

Sample the mixture twice independently. Conditional on its two lines $(\alpha,\beta),(\alpha',\beta')$, coincidence of the first coordinates modulo $2^k$ has probability $2^{-k}$ and their common residue is uniform. To coincide also in the second coordinate requires
\[
            (\alpha-\alpha')x\equiv \beta'-\beta\pmod{2^k}.
\]
The number of solutions is at most $2^{\min(k,v_2(\alpha-\alpha'))}$, with the convention $v_2(0)=\infty$. There is no assumption on either intercept. Averaging the two independent directions, the probability that they agree modulo $2^j$ is $\sum_u\sigma(u\bmod2^j)^2\le C(j+3)2^{-j}$. Therefore
\[
  \sum_{z\in(\mathbb Z/2^k)^2}\nu(z\bmod2^k)^2
     \le 2^{-2k}\left(1+\sum_{j=1}^k 2^{j-1}C(j+3)2^{-j}\right)
     \le C'(k+1)^2 2^{-2k}.                                              \tag{7}
\]
This is the planar line-incidence argument for mixed directions, here applied directly over each residue ring. It estimates the collision probability of the actual physical-time mixture rather than the cardinality of its support.

The Shannon entropy of these two residue coordinates is at least minus the logarithm of their collision probability, by Jensen's inequality, hence at least $2k\log2-O(\log(2+k))$. In each coordinate its first $k$ shortcut parities are a bijective recoding of the residue modulo $2^k$: equality of the first bit gives state differences multiplied by $1/2$ or $3/2$, so induction identifies exactly the binary congruence. Thus the same entropy bound holds for the length-$k$ block of a stationary process on four paired symbols. [Bernstein and Lagarias, *The 3x+1 conjugacy map*](https://doi.org/10.4153/CJM-1996-060-x)

For any fixed $l$, stationarity and entropy subadditivity imply that the entropy of an $ml$-block is at most $m$ times that of an $l$-block. Divide the preceding lower bound at $k=ml$ by $m$ and send $m\to\infty$. The $l$-block has entropy at least $l\log4$, which is the full finite-alphabet upper. Every $l$-block is consequently uniform. The coding bijection then gives uniformity of the state pair modulo every $2^l$. So $\nu$ is product Haar. All subsequential empirical limits have this same state marginal on the common probability-one set, proving (1).

## All-dimensional physical clock invariance

Apply (1) to each of the finitely many pairs in (2). The signed increment vector of the centred grade process is conditionally $v_m$ or $-v_m$ with equal probability for some predictable $v_m\in\{-1,1\}^r$, because one new bit flips all current parities. Its predictable covariance is $v_mv_m^{\mathsf T}$. Its off-diagonal $(i,j)$ entry is also the actual product of the two departure signs at that date. By (1) the time average of that entry is zero almost surely, and every diagonal entry equals one. Partial sums with $o(N)$ error have $o(N)$ maximal deviation up to time $N$, so the scaled predictable brackets converge uniformly on bounded rescaled time intervals to $tI_r$. The jumps are bounded by $\sqrt{r/N}$. The multidimensional martingale functional central limit theorem therefore gives (2), with independent Brownian coordinates. Equivalently, tightness follows from the individual fair-walk fourth moments, every continuous limit satisfies the martingale and bracket identities, and Lévy's characterization identifies the unique joint Brownian limit. [Whitt, *Proofs of the martingale FCLT*, Theorem 2.1](https://doi.org/10.1214/07-PS122)

For ordinary sources the entire path through physical date $N$ is determined by $n\bmod2^N$. The octave residue law differs from Haar by $O(2^N/X)$ in total variation. For a fixed-word frequency omit the last $k-1$ incomplete windows, costing $O(k/N)$. The transfer follows. In particular, along the family of dilations of the distinct odd sites of *any* hypothetical positive integer cycle of odd period $p$, (2) has $p$ independent limiting coordinates. All those sites are units prime to three, so two distinct ones have ratio outside $3^{\mathbb Z}$. The exceptional common scalar one which gives the original periodic trajectory has Haar mass zero. These source and horizon restrictions prevent inference of a cycle exclusion.

[AffineLineIncidence.lean](AffineLineIncidence.lean) proves the exact native affine tail, its two-coordinate line equation, the reduced-modulus spacing between any two intersections, and the cardinality upper $\gcd(q,s)$ for any positive modulus $q$ and slope difference $s$. All four endpoints compiled under the pinned strict environment. The first two use propositional extensionality and quotient soundness; the cardinality and spacing proofs additionally use classical choice. The Haar, entropy, logarithmic-form and functional-limit arguments are written mathematics. [Finite native control](check_multiplier_joining.py) · [Exact counts](../../../reports/astra-global-20261128/cycles/MULTIPLIER_JOINING.json)
