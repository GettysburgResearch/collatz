# Rational rigidity for every finite set of division exponents

This theorem concerns ordinary Syracuse steps with arbitrary bounded division exponents. Its constants and the conclusion about finite cycles allow *every* finite ceiling. The proof permits cancellation between several incoming branches.

Fix $E\ge1$ and the coordinate $t=(x-1)/2$ on ordinary positive odd $x$. A step with exponent $1\le e\le E$ has the exact form
$$
 2^e v+r_e\longrightarrow3v+d_e,\qquad
 (r_e,d_e)=
 \begin{cases}
 ((2^{e-1}-2)/3,0) & e\text{ even},\\
 ((5\cdot2^{e-1}-2)/3,2) & e\text{ odd}.
 \end{cases}                                                        \tag{1}
$$
Indeed $t'=(3t+2-2^{e-1})/2^e$, and the displayed residue gives exactly $3v+d_e$. Each $r_e$ is an integer in $[0,2^e)$, and $2t'+1$ is odd. The source classes for distinct $e$ are disjoint by the uniqueness of $v_2(3x+1)$. In particular the class of exponent $E+1$ is an omitted dyadic cylinder, of modulus $2^{E+1}$. Incoming residues can coincide for distinct branches. The same argument below permits any nonempty finite subset of the exponents by assigning zero weights to the other branches.

For a field $K$ let $C_e(X)=\sum_{n\ge0}c_e(n)X^n$. Equality of the outgoing and incoming edge weights at every physical vertex becomes
$$
 \sum_{e=1}^E X^{r_e} C_e(X^{2^e})
       =\sum_{f=1}^E X^{d_f} C_f(X^3).                              \tag{2}
$$

**Theorem.** Over every field, if the coordinates of a solution to (2) are all rational functions regular at zero, they are all polynomials. The polynomial solution space is exactly the span of finite directed cycle indicators. In characteristic zero the same conclusion holds if the joint binary kernel has finite-dimensional span. Over any finite field of characteristic two it holds if the coordinates are jointly algebraic over $K(X)$.

### Section transfer at every depth

Write $L_{m,r}w(n)=w(mn+r)$, $0\le r<m$. At the vertex $2^e(3n+j)+r_e$, the outgoing coefficient is exactly $c_e(3n+j)$. Write $2^ej+r_e=3h+\ell$, $0\le\ell<3$. The incoming side of (2) now gives
$$
 L_{3,j}c_e=\sum_{f:\ d_f=\ell} L_{2^e,h}c_f,\qquad 0\le h<2^e .   \tag{3}
$$
This calculation retains the whole sum, including cases of total cancellation.

A depth-$k$ ternary section of any $c_e$ is a finite sum of binary sections of the original coordinates at depths $k\le l\le Ek$. More generally, applying one ternary section to a binary section of depth $b$ gives a sum at depths between $b+1$ and $b+E$. For $m=2^b$, write $mj+c=3h+\ell$ to commute $L_{3,j}L_{m,c}=L_{m,h}L_{3,\ell}$. Apply (3) to the inner factor and compose binary sections. Induct on the number of ternary digits. In particular the joint binary span contains its ternary images.

### Elimination of all nonzero finite poles

Pass to an algebraic closure. Let $S$ be the finite union of the nonzero finite poles of the rational coordinates. Two elementary facts hold for rational sequences and all bases $m\ge1$.

* If $\alpha$ is a pole of $F$, then $\alpha^m$ is a pole of some $L_{m,r}F$. This follows from $F(X)=\sum_r X^r (L_{m,r}F)(X^m)$.
* Every pole of $L_{m,r}F$ is the $m$th power of a pole of $F$. Beyond the finite polynomial part, the coefficients of $F$ have a companion-matrix realization $u^{\mathsf T}T^n v$. The section uses $T^m$ in place of $T$, whose nonzero eigenvalues are the $m$th powers of those of $T$. Taking reciprocal eigenvalues gives the assertion in every characteristic.

For each $\alpha\in S$ and $k\ge1$, choose a depth-$k$ ternary section retaining the pole $\alpha^{3^k}$. Its expression from (3) gives $\alpha^{3^k}=\beta^{2^l}$ for some $\beta\in S$ and $k\le l\le Ek$. The finite set $S$ repeats one $\beta$ for two different $k$. Raising the two equalities to opposite powers of three gives
$$
 \beta^{\,2^{l_1}3^{k_2}}=\beta^{\,2^{l_2}3^{k_1}} .
$$
The exponents are different by their 3-adic valuations. Hence $\beta$ and $\alpha$ are roots of unity.

In characteristic zero partial fractions now make every coefficient sequence eventually quasipolynomial for a common quasi-period $M$. In characteristic $p>0$ the sequences are eventually periodic. Indeed the denominators, including all pole multiplicities, divide $1-X^{Mp^h}$ for sufficiently large $M,h$. In the next paragraph an ordinary periodic sequence counts as a quasipolynomial with constant constituent polynomials.

Write $M=2^a m$ with $m$ odd. Each binary section at depth $l\ge a$ of an eventually quasipolynomial sequence with period $M$ has quasi-period $m$. Take $k\ge a$ in (3) and its iterates. Every depth-$k$ ternary section has quasi-period $m$, so each original sequence has quasi-period $3^k m$, which is odd. For characteristic zero this follows by substituting $n=(N-j)/3^k$ into the constituent polynomial on each residue class of $N$. In positive characteristic the constituent functions are constant and no division in the field is needed.

Let $P$ be this odd common quasi-period. For $d=0,2$ set $I_d(n)=\sum_{f:d_f=d}c_f(n)$. Each $I_d$ is eventually quasipolynomial with period $P$. Fix a residue $n\bmod P$. The condition $3n+d\equiv r_{E+1}\pmod{2^{E+1}}$ has infinitely many arbitrarily large solutions in this residue by the Chinese remainder theorem. At each such $n$ the outgoing side is empty and (2) gives $I_d(n)=0$. In characteristic zero an infinite arithmetic progression of zeros makes the constituent polynomial zero. In positive characteristic the constituent is constant. Hence both incoming sums vanish eventually on every residue, and disjointness of outgoing supports makes every $C_e$ polynomial.

For finite support, take the finite directed graph of nonzero edge weights. Every vertex has at most one outgoing edge. On any weak component with an incoming leaf, the edge out of this leaf has weight zero by balance. Removing leaves shows that any nonzero component must be a directed cycle, with constant weight all around it. Equivalently, in a finite nonzero graph every vertex has an incoming edge and outdegree at most one, forcing exactly one incoming and one outgoing edge at every vertex. This proof applies to signed coefficients and to all characteristics.

### Automatic and regular consequences

In characteristic zero, finite-dimensionality of the joint binary section span gives finite-dimensionality of the ternary span by (3). Splitting the series of a basis into residue classes gives the corresponding Mahler equations in both bases, as detailed in the [two-branch argument](MIXED_MAHLER.md). Adamczewski–Bell give rationality of every coordinate, so the theorem gives polynomiality. In characteristic two over a finite field, joint algebraicity gives binary automaticity by Christol's theorem. The finite joint binary span over a finite field contains the whole ternary kernel, hence each coordinate is automatic in both bases. Cobham gives eventual periodicity, followed by rational rigidity. More generally the automatic conclusion holds for any common finite alphabet of field elements when the joint binary kernel is finite: in a finite-dimensional sequence space one can select finitely many coordinate evaluations that separate all vectors, so only finitely many vectors can take values in the prescribed finite alphabet. [Adamczewski–Bell](https://arxiv.org/abs/1303.2019) · [Christol et al.](https://www.numdam.org/item/BSMF_1980__108__401_0/) · [Cobham](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata)

For nonnegative real weights there is an additional D-finite consequence. Every active vertex survives an arbitrary number $k$ of future legal steps. From (1) a prescribed $k$-word requires a single residue class modulo $2^{\sum e_i}$. Thus the active vertices have upper natural density at most $(\sum_{e=1}^E2^{-e})^k=(1-2^{-E})^k$ for every $k$, and each coordinate support has density zero. If all coordinates are D-finite, each eventually satisfies a fixed-order polynomial coefficient recurrence. Arbitrarily long blocks of zeros beyond its finitely many singular indices propagate to the entire tail. Hence all coordinates are polynomial. This last argument uses positivity to carry activity forward through a merged incoming fiber.

### An unrestricted finite-cycle consequence

For a finite nontrivial ordinary positive cycle, choose $E$ equal to its largest exponent and let $N$ be the maximum coefficient index of any nonzero edge. If $x_{\max}$ is the maximum odd Collatz value, then
$$
 N=\left\lfloor\frac{x_{\max}-1}{6}\right\rfloor
$$
by the endpoint $t'=3v+d_e$ in (1). Let $V_2$ be the joint binary section span over any coefficient field. For each $M=2^i3^j\le\sqrt N/2$, the mixed section containing degree $N$ belongs to $V_2$ by (3). Its generating polynomial has degree $\lfloor N/M\rfloor$. Distinct $M$ give distinct degrees and therefore linearly independent vectors. Unique factorization gives $\gg(\log N)^2$ such $M$. Thus every nontrivial ordinary cycle has
$$
 \dim V_2\gg (\log x_{\max})^2
$$
with an absolute asymptotic implied constant independent of the largest exponent. Finite indicators are polynomial before taking any sections. Their classification still contains the positive-cycle problem.

### Explicit infinite signed circulations at ceiling five

The rational and [holonomic](HOLONOMIC_RIGIDITY.md) conclusions impose a genuine restriction on formal solutions. Take the infinitely many odd roots $y=469+576j$, $j\ge0$. They obey $y\equiv1\pmod9$ and $64\mid3y+1$, so each is a sink in the ordinary graph with $E=5$. Both $x=(4y-1)/3$ and $x'=(16y-1)/3$ are larger positive odd ternary units and map to $y$ with the indicated exponents. For instance, the first sink has predecessors 625 and 2501.

Every odd ternary unit $z>1$ has a larger ternary-unit predecessor at this ceiling. Use candidate exponents $2,4$ when $z\equiv1\pmod3$, or $3,5$ when $z\equiv2\pmod3$. Both candidates give integer odd predecessors $(2^e z-1)/3>z$. Their factors $2^e$ differ by 4 modulo 9, so at most one predecessor is divisible by 3. Selecting the first available unit recursively gives a strictly increasing backward ray. Do this separately above the two predecessors of each sink. The two rays never meet because forward evolution is deterministic. Rays belonging to different sinks likewise have disjoint supports.

Put edge weight $+1$ along one ray and $-1$ along the other. These weights balance at the sink and throughout both rays, and all remaining edges have weight zero. Distinct sinks give linearly independent nonpolynomial solutions over any field, including characteristic two. The supports are unions of two sequences growing at least geometrically, since $(4z-1)/(3z)\ge11/9$ for $z\ge3$. In particular these bounded signed formal solutions coexist with the classification of all holonomic solutions as polynomial. A single uniform reduction to a finite-dimensional space of standard scalar Mahler solutions would miss this infinite-dimensional signed kernel. Each constructed vertex has a finite forward path to its sink in the ceiling-five graph.

Over the integers, each coordinate of these explicit two-ray solutions that has infinite support has the unit circle as a natural boundary. Its coefficients belong to $\{-1,0,1\}$, so its radius is one. The $O(\log X)$ support bound supplies arbitrarily long zero blocks, excluding a rational power series by its linear recurrence. Pólya–Carlson gives the natural boundary. Bell and Lagarias used the same analytic theorem for ordinary inverse-orbit generating functions. [Bell and Lagarias, Acta Arithmetica 170 (2015)](https://arxiv.org/abs/1408.6884)
