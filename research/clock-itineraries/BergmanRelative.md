# Ordinary Collatz components in the classical Bergman transfer

Let $Tn=n/2$ for even $n$ and $Tn=(3n+1)/2$ for odd $n$. Say that $a\sim b$ if their ordinary positive orbits meet, allowing different clocks. Let $U$ mean that every positive integer reaches 1. For the classical Bergman transfer $A$, its generated von Neumann algebra is exactly the algebra of operators preserving these components. A fixed partial isometry $V$ detects their possible separation at every transfer depth.

$$
\operatorname{dist}(VA^k,W^*(A)+\mathcal K)=
\begin{cases}
0 & U,\\
\|A^k\| & \neg U.
\end{cases}
$$

Here $\mathcal K$ is the ideal of compact operators. In the second case a single ordered pair of distinct components supplies the full lower bound for every $k$. The result reduces convergence to a strict upper bound for this distance at any one depth. Establishing that upper bound remains open.

## Components of the single weighted operator

Use the orthonormal monomial basis $e_j=\sqrt{j+1}\,z^j$, $j\ge3$, in the classical Bergman quotient by degrees 0 through 2. The quotient operator sends $e_j$ to $\sqrt{(j+1)/(Tj+1)}\,e_{Tj}$ when $Tj\ge3$ and to zero otherwise. The graph on these coordinates has the ordinary merger classes restricted to $j\ge3$ as its weak components. Indeed, every orbit coming from outside $\{1,2\}$ first enters this two-cycle through $4\to2$. Thus all members of the basin of 1 still connect through 4. The other components retain all their edges. [Béhani, Propositions 2.1 and 4.2](https://arxiv.org/pdf/2303.03203)

The squared norm of row $a$ of $A^k$ is

$$
m_k(a)=\sum_{T^k j=a}\frac{j+1}{a+1}.
$$

The sum is over positive ordinary inputs, and none of their first $k$ steps can leave the quotient if $a\ge3$. Distinct rows have disjoint supports, so $\|A^k\|^2=\sup_{a\ge3}m_k(a)$. In particular $AA^*$ is diagonal with entries

$$
m_1(a)=2-\frac1{a+1}+\frac23\,\mathbf1_{a\equiv2\ (3)}.
$$

The two cases occupy disjoint intervals. Within each case the entries strictly increase. The distance between $m_1(a)$ and any other entry is at least $1/((a+1)(a+2))$. Each singleton coordinate projection $p_a$ therefore belongs to $C^*(A)$ by continuous functional calculus. Explicitly, $(I-(AA^*-m_1(a)I)^2/9)^N$ converges in norm to $p_a$. Compressing $A$ between two singleton projections isolates each edge matrix unit. Taking adjoints and multiplying along finite paths gives every matrix unit within each component. For every bounded component-preserving operator $B$, its finite coordinate compressions lie in this algebra and converge strongly to $B$. All the generators preserve components, proving

$$
\mathcal M=W^*(A)=\prod_C B(\ell^2 C).
$$

In particular $A$ is irreducible exactly when $U$ holds. Mori previously proved the cyclic-vector and irreducibility equivalences for two unweighted full-step branch operators in Lemma 4.2.2 and Theorems 4.2.3 and 4.2.7. His Corollary 4.1.3 gives a sufficient condition using a single unweighted operator. Mori also proved the invariant-set injection and, under his totally uniqueness condition, its bijectivity for branch-generated algebras. Here the individual classical Bergman quotient operator supplies the singleton projections through its weights. [Mori, 2024](https://arxiv.org/html/2411.08084v1) · [Mori, 2025, v2, Theorems 2.8 and 4.3](https://arxiv.org/html/2508.05713v2)

PR 200 O1 gives equal essential norms across components for the branch algebra. O4 recovers the within-component compact ideal using separate weighted branches and periodic diagonal projections. O12 derives equal power norms and disk spectra for the classical transfer on components through rooted inverse subtrees. The relative distances below measure transfer between ordinary components under a dilation. [O1](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/operator/COMPONENT_OPERATORS.md) · [O4](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/operator/OPERATOR_STRUCTURE.md) · [O12](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/operator/BERGMAN_DISK.md)

## Distance carried by a pair of components

Suppose $S e_n=e_{\phi(n)}$ for an injection on a subset of the coordinates and $S e_n=0$ elsewhere. Write $G=\{n\in\operatorname{dom}\phi:n\not\sim\phi(n)\}$. For each height $H$ set

$$
R_H=\sup\big(\{0\}\cup\{m_k(n):n\in G,\ n>H\}\big).
$$

Then $\operatorname{dist}(SA^k,\mathcal M)^2=R_0$ and $\operatorname{dist}(SA^k,\mathcal M+\mathcal K)^2=\lim_{H\to\infty}R_H$. To see the upper bounds, keep the component-diagonal blocks of $SA^k$. The discarded rows have mutually disjoint output coordinates and mutually orthogonal initial vectors. The first $H$ rows give a finite-rank correction. For the lower bounds take $u_n=A^{*k}e_n/\sqrt{m_k(n)}$. For $n\in G$, $SA^ku_n=\sqrt{m_k(n)}e_{\phi(n)}$ while $Bu_n$ belongs to the component of $n$ for every $B\in\mathcal M$. The $u_n$ are orthonormal. Along any sequence of distinct defect rows, each compact correction consequently tends to zero on these vectors.

First take $D e_n=e_{3n}$, on normalized coordinates. If $U$ holds its distance is zero. Otherwise some positive $q$ has $q\not\sim3q$. Indeed, if every odd $q$ and $3q$ have the same basin-of-1 label, the tripling descent proves $U$. Doubling either endpoint preserves its ordinary component. If all tripling defects start at multiples of three, the only predecessors are even and $m_k(n)=(2^kn+1)/(n+1)$. A defective dyadic ray then gives distance $2^{k/2}$. If some defect starts at a ternary unit, its dyadic multiples visit every unit residue modulo $3^k$ arbitrarily high. On a fixed residue the masses increase to their limiting value. Nonunit rows are dominated by the even contribution of any sufficiently high unit row. This gives full distance $\|A^k\|$. Both conclusions hold with or without compact corrections. Hence $\operatorname{dist}(DA^k,\mathcal M+\mathcal K)<2^{k/2}$ is equivalent to $U$. [Ordinary tripling descent](TowerRecurrence.lean)

For the full-norm dichotomy define a fixed $V$ using $r(n)=1+\nu_5(\nu_2(n)+1)$. Put $V e_n=e_{3^{r(n)}n}$ for $3\nmid n$ and zero elsewhere. Removing all factors of three from an image recovers $n$, proving that $V$ is a partial isometry. Under $\neg U$, tripling descent gives a basin-of-1 label change between an odd $q$ and $3q$. Write $q=3^v u$, $3\nmid u$. At least one of $3^v u,3^{v+1}u$ has a different label from $u$. Choose a corresponding positive exponent $r$.

For $n=2^j u$, the requirement $r(n)=r$ follows from $j+1\equiv5^{r-1}\pmod{5^r}$. Prescribing $n\bmod3^k$ to be any unit gives a congruence for $j$ whose period divides $2\cdot3^k$, since 2 generates the ternary unit groups. The Chinese remainder theorem supplies simultaneous solutions of arbitrarily large height. Every such $n$ belongs to the fixed component of $u$ and its target belongs to that of $3^r u$. Their row masses dominate every specified finite row if the height is sufficiently large. This proves the displayed dichotomy, including for the compression from this one component to the other. The choice of component projections depends on the actual ordinary basins.

## Every nontrivial central projection

Let $P$ be any nonzero proper central projection in $\mathcal M$. Its diagonal label $p(n)\in\{0,1\}$ is constant on ordinary components. Extend the label to 1 and 2 by giving them the label of 4. The PR 146 descent uses only invariance under $T$ and equality of the labels at odd $q,3q$. Applied to the predicate $p(n)=p(1)$, it proves that every nonconstant $p$ changes somewhere along an odd tripling edge. The same factorization and congruences as above then carry this change to a full set of cofinal unit rows. On their initial vectors, $[P,V]A^k$ has the same row norm as $A^k$, with a possible sign. Its other rows have zero weight. Thus for every nontrivial central projection, simultaneously at every $k$,

$$
\|[P,V]A^k\|_{\rm ess}=\|[P,V]A^k\|=\|A^k\|.
$$

It follows unconditionally that $W^*(A,V)=B(\ell^2)$. Indeed every projection commuting with $A,A^*$ is a component projection by the product formula for $\mathcal M$. If it also commutes with $V,V^*$, the preceding identity at $k=0$ forces it to be zero or the identity. Spectral projections of self-adjoint elements then give a scalar joint commutant, and the bicommutant theorem gives the assertion. Equivalently, the graph obtained by adding the $V$ edges is connected. Products of the coordinate projections and edge operators along finite paths consequently put all finite matrix units, and hence all compact operators, in $C^*(A,V)$. The same connectivity argument applies to $D$ directly by the arbitrary-label tripling descent. This identifies the effect of adjoining the specified dilation even when the original ordinary orbits are unknown.

More generally, let $M_f$ be multiplication by a bounded complex function constant on components. Extend $f$ to 1 and 2 by its value at 4. Define

$$
\Delta(f)=\sup_{\substack{u\text{ positive odd},\,3\nmid u\\r\ge1}}
  |f(3^ru)-f(u)|.
$$

Then $\|[M_f,V]A^k\|_{\rm ess}=\|[M_f,V]A^k\|=\Delta(f)\|A^k\|$. Each nonzero row has an additional weight of modulus $|f(3^ru)-f(u)|$ for the odd part $u$ of its input coordinate and some $r$. This gives the upper bound. For each fixed $u,r$, the simultaneous congruences provide arbitrarily high rows with exactly this weight and transfer mass approaching the global supremum. Taking the supremum over pairs proves the lower bound, including modulo compacts. Moreover $\Delta(f)=0$ implies $f$ is constant, by applying the arbitrary-label descent to $f(n)=f(1)$. In particular an exactly component-constant multiplier can commute with $V$ modulo compact operators only when it is scalar.

## Finite residue information and finite meeting clocks

There is a rational pair $(s_k(r),b_k(r))$ for each residue $r\bmod3^k$ such that

$$
m_k(n)=s_k(r)-b_k(r)/(n+1),\qquad
0<s_k(r)\le3^k,\quad 0\le b_k(r)\le3^k .
$$

At depth zero the pair is $(1,0)$. Writing $e=2n$, $o=(2n-1)/3$ on an odd inverse branch, and $\epsilon=\mathbf1_{n\equiv2\ (3)}$, the next pair is

$$
s'=2s_e+\tfrac23\epsilon s_o,\qquad b'=s_e+b_e+\epsilon b_o.
$$

In particular $b_k>0$ for $k>0$. The full squared norm is the maximum of the finite slope table, in accordance with Béhani's Proposition 4.2. At depths 1 through 4 the values are $8/3,\ 52/9,\ 392/27,\ 2512/81$. Under failure each unit slope occurs as a limit of actual defect rows. Consequently if $Y=VA^k-\sum_C P_CVA^kP_C$, then the essential spectrum of $YY^*$ under failure consists precisely of zero and the finitely many unit slopes. Here a unit slope is $s_k(n\bmod3^k)$ for some $3\nmid n$, including the unique depth-zero slope. Indeed $YY^*$ is diagonal with a defect mass at each corresponding image coordinate. The uniform height error gives every possible nonzero accumulation point, and arbitrarily high defect rows in every unit residue realize each listed slope. Zero has infinite multiplicity on the unit output coordinates. Under $U$, $Y=0$. [Béhani, Proposition 4.2](https://arxiv.org/pdf/2303.03203)

A finite meeting-clock test can exhibit the same large masses inside the basin of 1. Take $u=1,r=1$ in the simultaneous congruences. For any height cutoff, row mass and clock $L$, one obtains $n=2^j$ above that cutoff and with at least that mass, $j>L$, and $V e_n=D e_n=e_{3n}$. Both orbits converge. Through time $L$ their values are powers of two and three times powers of two respectively, so they cannot meet using any two clocks bounded by $L$.

For example $n=2^{27}=134\,217\,728$ has $n\equiv80\bmod81$ and $r(n)=1$. The depth-four recurrence gives $m_4(n)=2512/81-33/(n+1)$, within $2.46\cdot10^{-7}$ of the full squared norm. Every pair of clocks at most 26 misses a meeting with $3n$. At clocks 24 and 29 the two orbits reach 8.

In a functional graph, an undirected path of length $d$ gives a forward meeting within $d$ steps from either endpoint. To verify this, concatenate the path edges using the fact that if the first two vertices meet at clocks $i,j$ and the last two at $j',h$, one can advance to the later of $j,j'$ at the middle vertex. The resulting clocks are bounded by the sum of the previous two bounds. Thus the graph distance in the quotient between $n$ and $3n$ exceeds $L$. A polynomial of degree $d$ in $A,A^*$ only has matrix entries between vertices at graph distance at most $d$. The vector $u_n$ is supported within distance $k$ of $n$. Taking $L>d+k$ kills the polynomial output at $3n$ on $u_n$. Along distinct choices of $n$ every compact correction tends to zero there. Norm approximation by polynomials gives, unconditionally, for $S=D,V$,

$$
\operatorname{dist}(SA^k,C^*(A)+\mathcal K)=\|A^k\|.
$$

The same lower bound holds after compression on both sides to the basin of 1. A proof of a strict upper bound in the von Neumann algebra must therefore use information beyond uniformly bounded orbit-meeting clocks.

## Lean scope

The native modules build in the order below. The namespace is $\texttt{Collatz.Itinerary.BergmanRelative}$.

1. [BergmanRelative.lean](mathlib/BergmanRelative.lean) proves the exact duplicate-free ordinary transfer fibers, finite-height row formula, separated one-step masses, simultaneous dyadic and ternary conditions, fixed pair of components under failure, and the unconditional convergent finite-clock controls.
2. [BergmanDistance.lean](mathlib/BergmanDistance.lean) proves the real supremum trichotomy for $D$, the full supremum dichotomy for $V$, and the equivalence with a strict gap for any depth and cutoff.
3. [BergmanCenter.lean](mathlib/BergmanCenter.lean) generalizes tripling descent to arbitrary component labels and proves the full real cutoff supremum for every nonconstant component projection.
4. [BergmanSpectrum.lean](mathlib/BergmanSpectrum.lean) proves the uniform slope error, cofinal approximation on actual defective unit rows, finite maximum for the full supremum, four exact controls, the abstract continuous-linear-map estimate for contraction tests, and the full supremum on converging controls outside each fixed undirected walk budget. This module and the preceding one each import BergmanDistance.
5. [BergmanAccumulation.lean](mathlib/BergmanAccumulation.lean) imports BergmanSpectrum. Its theorem $\texttt{defect_cluster_iff}$ characterizes every possible real cofinal limit of ordinary defect-row masses. Such a limit exists at a given $x$ exactly when $U$ fails and $x$ is a unit slope. The finite separation argument explicitly covers approximations that vary the unit residue at every stage.

The Hilbert-space identification of these row suprema with distances, the component algebra, the essential spectrum, and the finite-propagation C*-algebra corollary have written proofs above. The Lean modules formalize the arithmetic and real suprema underlying them.
