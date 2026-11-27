# Quantitative two-torus recurrence on every bounded-clock schedule

**Written theorem.** Let $0<w<1/4$. There is an absolute constant $C$ such that for every $X_0\ge1$ and every positive real path satisfying $2^{a_j}X_{j+1}=3X_j$ with $1\le a_j\le4$ integral, every pair of open arcs $I,J$ of length $w$ has an ordinary path index and a dyadic shift satisfying
$$
j\le\lceil\log_2(X_0+1)\rceil+H(w),\qquad 0\le r\le H(w),
\qquad 2^r X_j\bmod1\in I,\quad \log_2 X_j\bmod1\in J,
$$
where $H(w)\le\exp\exp\exp(w^{-C})$. It suffices to have the indicated finite path. The two arcs may be chosen depending on the starting value. This supplies a growth estimate for E1 of [the accompanying proof](proof.md).

**Bounded-denominator escape.** Given an integer $n\ge1$, put $\delta=(20n^2)^{-1}$ and
$$
D=\lceil\log_2(X_0+1)\rceil+2\lceil\log_2 n\rceil+1.
$$
Some $X_k\bmod1$ with $0\le k\le D$ has distance greater than $\delta$ from every rational of denominator at most $n$. Otherwise there are $p_j/q_j$ with $1\le q_j\le n$ and $|X_j-p_j/q_j|\le\delta$ at every phase. Translating by an integer gives these literal approximants from circle approximants. At adjacent phases the integer $3p_jq_{j+1}-2^{a_j}p_{j+1}q_j$ has absolute value at most $19\delta n^2<1$. The rational recurrence is exact. Hence
$$
2^{\sum_{j<D}a_j}\,p_D q_0=3^D p_0q_D,
$$
so $2^D\mid p_0q_D$, which is a positive integer strictly smaller than $n^2(X_0+1)<2^D$. This is the contradiction. The denominators may differ at every phase.

**Quantitative higher-rank input.** Kravitz and Leng, Theorem 2.1, deduced from Bourgain, Lindenstrauss, Michel and Venkatesh's entropy and two-logarithm estimates, applies to every point of the circle. For precision $\eta>0$ and rational tolerance $\delta>0$, either its orbit under the multipliers $2^s3^t$, $0\le s,t\le K$, is $\eta$-dense, or the point lies within $\delta$ of a rational of denominator at most $n$. Their bounds permit
$$
n=\left\lceil\exp\exp\exp(\eta^{-C_1})\right\rceil,\qquad
K=\left\lceil\exp\exp(\eta^{-C_1})+\log_2(1/\delta)\right\rceil .
$$
For $\delta=(20n^2)^{-1}$ the preceding lemma supplies a phase $k\le D$ in the dense alternative, with $K+\log n\le\exp\exp(\eta^{-C_2})$ after enlarging the constant. [Kravitz and Leng, Theorem 2.1](https://arxiv.org/pdf/2510.17744)

**Targeting the leading phase at the same point.** Put $\alpha=\log_2 3$. There is an integer $L\le w^{-C_3}$ such that every $t_0$ has $t_0+h\alpha\bmod1\in J$ for some $0\le h\le L$. Indeed Dirichlet approximation supplies $k_0\le\lceil4/w\rceil$ with $\beta=\|k_0\alpha\|\le w/4$. Baker–Wüstholz gives $\beta\gg(1+k_0)^{-C_4}$ since 2 and 3 are multiplicatively independent. The points $jk_0\alpha$ through $j=\lfloor1/\beta\rfloor$ form a circle net with maximum gap at most $\beta$ in either orientation. This proves the claimed polynomial bound on the hitting time. [Baker–Wüstholz in the precise two-logarithm form used here, Bourgain et al., Theorem 4.3](https://math.stanford.edu/~akshay/research/blmv.pdf)

Choose $q=2^\ell-3$ with $8/w\le q\le 24/w$, taking the first such power reaching the lower bound. The odd $q$ is coprime to both 2 and 3. Choose $\xi=m/q$ at distance at least $w/4$ from the complement of $I$, possible by grid spacing. For every $0\le h\le L$ there is $0\le v_h<q$ with $2^{v_h}3^h\xi=\xi$ on the circle, by $3\equiv2^\ell\bmod q$ and Euler's theorem. Put
$$
\eta=(w/8)2^{-q}3^{-L}.
$$
At the good phase $k$ pick $s,t\le K$ with $2^s3^tX_k\bmod1$ within $\eta$ of $\xi$. Use the rotation bound on $\log_2 X_{k+t}$ to choose $h\le L$ with $\log_2 X_{k+t+h}\bmod1\in J$. The point $2^{v_h}3^h2^s3^tX_k$ lies within $2^{v_h}3^h\eta\le w/8$ of $\xi$ and hence belongs to $I$ modulo 1. Its exact physical realization is $2^rX_{k+t+h}$ with
$$
r=s+v_h+\sum_{m=k}^{k+t+h-1}a_m\le5K+q+4L.
$$
Thus the additive time cost beyond $\lceil\log_2(X_0+1)\rceil$ is bounded by $2\lceil\log_2 n\rceil+1+K+L$. Since $\eta^{-1}\le\exp(w^{-C_5})$, both costs satisfy the claimed triple exponential bound.

**Scale on an ordinary escape.** For example, for some $c>0$ and all sufficiently large $X_0$, arcs of length $w=(\log\log\log\log X_0)^{-c}$ can be hit with $j\le\lceil\log_2(X_0+1)\rceil+o(\log X_0)$ and $r=o(\log X_0)$. Indeed take $cC<1$. In particular this applies to the corrected minima $X_j=M_{i+j}$ under the actual-class hypotheses of E3. If the low residue cylinders are fixed, lift at a fixed extra rank as in E2 and E3. The fractional corrected arc is then hit at this scale. For the ordinary leading coordinate there is a precise dichotomy. Fix any $0<\gamma<1$. Write $m_j$ for the unrestricted synchronous-class minimum. One has $m_j\le n_j\le4m_j+1$, since if $3\mid m_j$ the sibling $4m_j+1$ is a ternary unit with the identical odd successor. Either some $j\ge i$ has $m_j<n_i^\gamma$, supplying a future unit representative at most $4n_i^\gamma+1$, or every future class has unrestricted minimum at least $n_i^\gamma$. The class-packing bound in §3 of the [pinned class proof](../../astra-global-synthesis-20261124/section/proof.md) then gives
$$
D_i\ll n_i^{-\gamma(1-\theta)},\qquad \theta=H_2(\log 2/\log 3)<1.
$$
Every ordinary source selected in a later class has leading phase within $D_i$ of its corrected phase. Use the middle half of the prescribed arc, with $c$ small enough for the same sublogarithmic costs, to obtain ordinary leading recurrence at the stated shrinking scale in the second case. In particular it holds on infinitely many actual windows of every hypothetical escape: take future-tail records $i$ with $m_i=\min_{j\ge i}m_j$. Such indices are unbounded because the distinct positive integers $m_i$ tend to infinity, and there $m_i\ge(n_i-1)/4$. Neither the triple exponential estimate nor this strengthened physical transfer guarantees the critical width $1/\log X_0$ for simultaneous targeting of both arcs on a logarithmic budget.
