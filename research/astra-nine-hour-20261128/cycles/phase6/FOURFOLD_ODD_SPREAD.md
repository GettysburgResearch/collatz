# Fourfold asymptotic spread of the odd states

**Source-qualified written theorem.** For every fixed $R<4$, only finitely many positive integer Collatz cycles of least period can have greatest odd state $X$ and least odd state $m$ with $X/m\le R$. Equivalently every sequence of distinct positive integer cycles satisfies
$$                         \liminf X/m\ge4.                         \tag{1} $$
Consequently the corresponding shortcut and ordinary maximum-to-minimum ratios have limit inferior at least six and twelve, respectively. The shortcut maximum is $(3X+1)/2$, the ordinary maximum is $3X+1$, and the minimum in either convention is $m$.

The argument uses the two-grade Sidon comparison from PR214 and Chudnovsky's stated upper bound of three for the irrationality exponent of $\log_2 3$. The new step keeps the physical transition constraints between neighboring binary code coordinates. The mixed-alphabet calculation below gives a required approximation exponent greater than $3.0196$ uniformly at each fixed $R<4$. The result supplies no effective bound for the exceptional periods. A sequence of ratios approaching four from below and an isolated ordinary cycle both remain possible. Canonical defect width $W$ and the physical ratio $X/m$ are different quantities. [PR214, f769b0c79059cc18b0be89e880ed6ea6a279e1c0, TWO_GRADE_SIDON.md](https://github.com/GettysburgResearch/collatz/blob/f769b0c79059cc18b0be89e880ed6ea6a279e1c0/research/astra-critical-rigidity-20261128/cycles/TWO_GRADE_SIDON.md) · [Chudnovsky, arXiv:2610.28079v1, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)

### An all-date Sidon code from the physical cycle

Increase $R$ slightly if necessary so $2<R<4$. Suppose there is a sequence of distinct cycles with this bound. Write $p$ for the least odd period, $A$ for the total number of halvings, and $\gamma=\log_2 3$. Then $m,p\to\infty$. Indeed cycles are disjoint as sets of integers, and at bounded $p$ the bound $A<2p$ leaves finitely many exponent words, each with a unique rational solution. Multiplying the genuine odd transitions gives
$$ 0<\rho-\gamma=\frac1p\sum_{x\text{ odd}}\log_2(1+1/(3x))\le\frac1{3m\ln2},\qquad \rho=A/p.\tag{2} $$

For completeness, fold the odd states into $[L,2L)$ by $Z=cx$, $c\in\{1,2\}$, doubling exactly those $x<L$. Take $\eta=\log_2(R/2)$, $v=(1-\eta)/2$, $L=2^{1-v}m$. Thus there are strict margins $L<2m$ and $X<2L$. Sort the $p$ distinct labels, extend $Z_{r+p}=2 Z_r$, $c_{r+p}=2c_r$. In this unwrapped list the map $Z\mapsto3Z+c$ preserves strict order. Inside the base it follows from integrality and the tag range; at the seam the first doubled tag is at least the last tag. The odd successor permutes the rays and the formula commutes with doubling. It is a bijection of the unwrapped list and therefore acts by a constant rank shift. That shift is $A$ by summing the native division counts after telescoping the dyadic rescalings. In particular $(A,p)=1$ and $Z_{r+A}=3Z_r+c_r$ throughout the lift.

The normalized angular empirical measures tend weakly to uniform measure. Indeed the true angular increments tend uniformly to the irrational rotation $\gamma\bmod1$ by (2); every weak limit is invariant, and its nonconstant Fourier coefficients vanish. Uniform convergence of the cumulative distributions gives $\log_2(Z_r/L)=r/p+o(1)$ uniformly on the fundamental ranks. Near the left endpoint every tag is one since $Z<2m$; near the right endpoint every tag is two since $Z>X$. Consequently for some fixed $\epsilon>0$ depending on $R$, all unwrapped tags in $[r,r+\epsilon p]$ at every fundamental origin $r$ belong to $\{1,2\}$ for late members. After a wrap the tags from the next left end double from one to two. This is where a fixed strict width margin enters.

For any two distinct unordered pairs of offsets in $[0,\lfloor\epsilon p\rfloor]$, including repetitions within pairs, form $P(T)=T^i+T^j-T^k-T^l$ and $H_r=P(E)Z_r$ with $E$ the spatial unit shift. For $r'=(r+A)\bmod p$ and $b(r)=\lfloor(r+A)/p\rfloor$ one has
$$ 2^{b(r)} H_{r'}=3 H_r+P(E)c_r,\qquad |P(E)c_r|\le2. $$
Every nonzero sign propagates strictly around the transitive base. All $H_r$ cannot vanish, since with $\xi=2^{1/p}$ the weighted sum $\sum_r\xi^{-r}H_r=P(\xi)\sum_r\xi^{-r}Z_r$ is nonzero by Eisenstein for $T^p-2$ and $\deg P<p$. This gives the pair-sum uniqueness at the initial origin used below. These rank and sign arguments are those of PR214. Its triple-sum comparison treats the separate range $R<27/8$. [PR214, same head, THREE_SUM_RANK_ORDER.md](https://github.com/GettysburgResearch/collatz/blob/f769b0c79059cc18b0be89e880ed6ea6a279e1c0/research/astra-critical-rigidity-20261128/cycles/THREE_SUM_RANK_ORDER.md)

Choose $N=\lceil\log_3(8L)\rceil+2$, $r_t=tA\bmod p$, $b_t=b(r_t)$. Thus $N=(\log_2m)/\gamma+O_R(1)$, and $2^{\sum_{t<N}b_t}=2^{\lfloor N\rho\rfloor}>4L$. For each offset $0\le j\le\lfloor\epsilon p\rfloor$ use the entire binary word $c_{r_t+j}-1$ at $0\le t<N$. If two unordered pairs of these codewords have equal coordinatewise integer sums, their tag forcings are equal at all $N$ dates. The doubled register recursion then gives $2^{\sum b_t}\mid3^N(Z_i+Z_j-Z_k-Z_l)$. Its initial integer difference has magnitude less than $2L$. Hence it vanishes and the pair-sum uniqueness just proved identifies the original unordered pair. The code has the $B_2$ property and cardinality $M=1+\lfloor\epsilon p\rfloor$.

### The physical register forbids one adjacent pair

For each column write its current and next unwrapped tags $c,c'$ and its corresponding true odd states $x,x'$. The same register relation gives
$$ 2^{b_t} c'x'=3cx+c=c(3x+1)=c\,2^e x',\qquad
 e=b_t+\log_2 c'-\log_2 c\ge1.                                  \tag{3} $$
Thus whenever $b_t=1$ the bit pair $10$ is impossible for every column. The allowed pair alphabet is $\{00,01,11\}$. No two such dates are adjacent, since $\rho>3/2$ and the two-letter winding sum is at least three. Eventually $b_t\in\{1,2\}$, and the count of ones among the first $N$ windings is $2N-\lfloor N\rho\rfloor$. Discard the last pairing if it would require bit $N$. The resulting disjoint pairs and remaining singleton coordinates number
$$  (2-\gamma+o(1))N,\qquad (2\gamma-3+o(1))N, $$
respectively. This uses all chronological bits, including bits forced for all columns. Each pair block has at most three letters and seven ordered differences (zero and six distinct nonzero differences). Each singleton has at most two letters and three differences.

### Prefix shortening for the two alphabets

Define
$$ U=(2-\gamma)\log_2 3+(2\gamma-3),\qquad
 V=(2-\gamma)\log_2 7+(2\gamma-3)\log_2 3,\qquad d=\frac{UV}{U+V}. $$
An ordered difference of distinct codewords identifies both codewords because an equality of differences rearranges to an equality of two unordered sums. Fix a fraction $0\le\lambda<1$, and use as a prefix $\lfloor\lambda s\rfloor$ blocks of each type occurring $s$ times. The prefix permits $P\le2^{(\lambda U+o(1))N}$ patterns. The suffix permits $D\le2^{((1-\lambda)V+o(1))N}$ different ordered differences. If the prefix bucket sizes are $t_a$, the distinct equal-prefix ordered pairs give $\sum_a t_a(t_a-1)\le D$. Cauchy's inequality now yields the finite bound
$$                            M^2\le P(M+D).                            \tag{4} $$
This is a prefix/suffix difference argument for a product of unequal alphabets. Prefix/suffix bounds for separable and $B_2$ codes have a long history. [Della Fiore and Dalai, *A note on 2-separable codes and B2 codes*, Discrete Mathematics 345 (2022)](https://doi.org/10.1016/j.disc.2021.112751)

Pass to a subsequence giving $r=\limsup (\log_2 M)/N\le U$. If $r>0$ choose $\lambda<r/U$. Then $D\ge M^2/P-M$ has lower exponent $2r-\lambda U$, so $2r-\lambda U\le(1-\lambda)V$. Send $\lambda\uparrow r/U$ to obtain $r\le d$, also valid when $r=0$. Therefore
$$ \limsup\frac{\log p}{\log m}\le\frac d\gamma,\qquad
 0<\frac A p-\gamma\le p^{-\gamma/d+o(1)}.                           \tag{5} $$
Rigorous intervals give $0.5248<d<0.5249$ and $3.0196<\gamma/d<3.0198$. In particular the required rational approximation exponent in (5) strictly exceeds three. The stated Theorem 11.1 of Chudnovsky applies to $3,2$ since these positive rationals are multiplicatively independent. Its bound $\mu(\gamma)\le3$ excludes (5) on an infinite sequence. This completes (1). The separate effective clock bound used elsewhere in this packet does not give this conclusion. The strict local Lean replay covers the finite combinatorial lemmas independently of the imported irrationality theorem.

Earlier work already deduced coprimality at canonical widths at most two, and precise order reversals in a repeated phase. The proof here uses the physical two-grade interval and the restrictions between adjacent chronological tag bits within each codeword. [Weaver, rStation 114/v1, Theorem 1](https://rstation.ai/problems/collatz/papers/114/v1) · [Weaver, rStation 145/v1, Theorems 2 and 5](https://rstation.ai/problems/collatz/papers/145/v1)
