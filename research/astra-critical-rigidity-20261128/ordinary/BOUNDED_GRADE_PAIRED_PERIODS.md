# Entrance slopes for two different bounded-grade periodic calendars

**Proposed theorem.** Fix $P\ge1$. Consider two positive rational periodic phases $z,w$ of the shortcut map with native primitive periods $L_1,L_2$ and $1\le p_i\le P$ odd departures per period. Suppose in some orientation
$$
                  w=3^jz-a,\qquad j\ge0,\ a\in\mathbb Z,
                        \quad (j,a)\ne(0,0).                              \tag{1}
$$
As $L_*:=\max(L_1,L_2)\to\infty$ along such pairs,
$$
             L_1p_2=L_2p_1\ \text{eventually},\qquad
                            L_*=o(j).                                     \tag{2}
$$
The phases may belong to different rational cycles and may have different native calendars after entry. Equality of rational phases is allowed on an unequal-slope line. The result generalizes the [common-phase bounded-grade obstruction](RATIONAL_PERIODIC_SHADOWS.md) and covers finite-calendar motifs which persist by preserving the same line on two different words.

## Two physical clocks force equal densities

Every cyclic phase has odd denominator prime to three and ternary-unit numerator. By (1) both complete reduced denominators are the same $q$. If a word has length $L$, grade $p$ and offset $C$, its phase is $C/(2^L-3^p)$. The usual offset bound $C\le2^L3^p$ uniformly bounds every rotated phase by $2\cdot3^P$ when $L$ is large. A gap between odd departures of length at least $L/p$ starts at a phase $v$ and ends at $(3v+1)/2^{\rm gap}\ge1/q$. Hence $q\ge2^{L_*/P}/(6\cdot3^P+1)$. Also $q\mid2^{L_i}-3^{p_i}$, so both $L_i\to\infty$.

If the two clocks are not proportional, $2^{L_1}/3^{p_1}$ and $2^{L_2}/3^{p_2}$ are multiplicatively independent $S$-units, $S=\{\infty,2,3\}$, of heights $O_P(L_*)$. Both are congruent to one modulo $q$. The rank-two gcd theorem for independent pairs forces $\log q=o(L_*)$ along any infinite such sequence, a contradiction. Distinct lengths give distinct points up to the fixed finite choices of $p_i$. [Corvaja and Zannier, Proposition 2](https://arxiv.org/pdf/math/0311030)

Pass to fixed $p_1,p_2$ and use the joint period $L=\operatorname{lcm}(L_1,L_2)\le P L_*$; both grades over it have the same value $p=\operatorname{lcm}(p_1,p_2)\le P^2$. Thus $L\asymp_P L_*$ and $\log q\gg_P L$ on the sequence.

Bounded $j$ is impossible. In that case $a$ is bounded by the uniform real phase bounds. Each of the finitely many possible noncollapsed lines is physically attainable by the [universal relation theorem](UNIVERSAL_RATIONAL_MERGERS.md): for $j>0$, reducing (1) at three gives $3\nmid a$, whereas for $j=0$ any nonzero $a$ is allowed. From a fixed line entrance prescribe the next $L$ paired letters of $z,w$ by refining its lower source coordinate. The rational pair realizes them, and both terminal word maps have equal slope and return the pair to its starting phases. Thus the entrance relation is preserved on the whole refined cylinder. If $j>0$ it has at most one diagonal intersection; if $j=0$ it stays a nonzero translation. Infinitely many positive ordinary lifts avoid a merger at the terminal date and hence at every earlier date. The total grade is bounded uniformly by the fixed entrance cost plus $2P^2$. The [finite unmatched-clock bound](PAIRED_SOURCE_GRADES.md) forbids $L\to\infty$. This proves $j\to\infty$.

## Keeping the independent power of three after restricting the binary exponents

Assume for contradiction $j=O(L)$ on a subsequence, and fix $p$. Write $D=2^L-3^p$, and $A,B$ for the two length-$L$ offsets. Then
$$
              q=D/\gcd(D,A),\qquad D\mid 3^j A-B.                       \tag{3}
$$
The divisor in (3) is the entire unnormalized word denominator; no cancellation is made in the second condition.

Collect $L$ and the $2p$ binary odd positions of the two words in a vector $n\in\mathbb Z^{1+2p}$. Choose a rational affine subspace of least possible dimension containing infinitely many of these vectors, retain that subsequence, and take an integer point $n_0$ on it from the sequence. A lattice basis $b_1,\ldots,b_r$ of its direction space intersected with $\mathbb Z^{1+2p}$ gives
$$
                    n=n_0+\sum_{i=1}^r m_i b_i,\qquad |m_i|=O(L).
$$
The height bound follows from a fixed left inverse on this fixed space. No fixed proper affine hyperplane in the $m_i$ can contain infinitely many retained points. Put $X_i=2^{m_i}$ and $Y=3^j$. The enlarged sequence $(X_1,\ldots,X_r,Y)$ eventually avoids every **fixed finite union** of translates of proper algebraic subgroups of the torus. On a translated subgroup some nontrivial character is constant. Taking its $3$-adic valuation forces the exponent of $Y$ to vanish, since $j\to\infty$. The $2$-adic valuation then gives a forbidden fixed affine hyperplane in the $m_i$. A constant character value on rational points is rational, so these two valuations apply even to a translate initially defined over an extension field.

Each binary power in (3) is now a fixed Laurent monomial in the $X_i$ with a coefficient a power of two. Write $F,A_0,B_0\in\mathbb Z[1/6][X_1^{\pm1},\ldots,X_r^{\pm1}]$ for the fixed Laurent polynomials evaluating to $D,A,B$. They are nonzero since the evaluations are nonzero. In this unique factorization ring let $H=\gcd(F,A_0,B_0)$. The nonconstant factors of $F$ are independent of $Y$, so over the rational Laurent ring
$$
           F/H\quad\text{and}\quad (Y A_0-B_0)/H
                     \quad\text{are coprime}.                              \tag{4}
$$
Indeed any common factor remaining from $F$ would divide both coefficients in $Y$. Passing from the integral to the rational coefficient ring removes only scalar factors. Clear negative exponents in each expression by its own minimal monomial, giving coprime ordinary polynomials. Multiplying by monomials does not change valuations outside $S$. The integral Laurent quotients $F/H,A_0/H,B_0/H$ all evaluate to $S$-integers.

At every prime $v\ge5$, (3) says that the second value in (4) has valuation at least the first. Also
$$
 v((F/H)(X))\ \ge\ v(q):
$$
the left side is nonnegative, and $v(H(X))\le v(A)$ since $A_0/H$ is integral away from $S$. Hence the logarithmic gcd of the values in (4), **outside** $S$, is at least $\log q\gg_P L$. If one polynomial is a nonzero constant, the gcd outside $S$ has a fixed bound already. Otherwise apply the multivariate $S$-unit gcd theorem to these two fixed coprime polynomials and points $(X,Y)$. For every fixed $\epsilon>0$ their outside-$S$ gcd logarithm is at most $\epsilon\max_i(h(X_i),h(Y))=O(\epsilon L)$ away from finitely many fixed proper subgroup translates. The preceding valuation argument excludes all of those translates eventually. Taking $\epsilon$ sufficiently small yields a contradiction and proves (2). [Levin and Wang, Theorem 1.13(a), stating the multivariate gcd theorem of Levin](https://doi.org/10.1515/crelle-2019-0033)

The conclusion is ineffective and does not assert a uniform exponential lower bound in $L_*/P$. In particular it allows super-$G\log G$ constructions paying a large subexponential entrance exponent, and it places no uniform restriction on motifs whose primitive odd grades grow.
