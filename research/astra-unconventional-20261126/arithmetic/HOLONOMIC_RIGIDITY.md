# Every formal D-finite solution is a finite sum of ordinary cycle indicators

Fix any finite division-exponent ceiling $E$. Use the physical coordinates and incidence equation (2) of [the arbitrary-gap theorem](ALL_GAPS_MAHLER.md), with coefficients in $\mathbb C$. An ordinary formal D-finite series satisfies a homogeneous linear differential equation with polynomial coefficients. Divergent formal series are included.

**Theorem.** If all the $C_e$ are D-finite, they are polynomial. Thus the space of holonomic solutions is exactly the complex span of the finite ordinary directed cycles at this ceiling. Every finite ordinary positive cycle is covered by taking $E$ equal to its largest exponent. The result classifies a class of series without deciding which nontrivial cycles exist.

The only arithmetic input is that each ternary section of depth $k$ is a sum of binary sections of depths $k\le l\le Ek$ on the same ordinary graph. That input retains all the incoming branches when their residues coincide. [Section theorem](ALL_GAPS_MAHLER.md) · [Lean section proof](AllGapSections.lean)

## Convergence at the origin

For a D-finite formal series $F$, let $M(F)$ denote the finite-dimensional $\mathbb C(X)$-span of its Euler derivatives $(X\partial_X)^i F$ inside $\mathbb C((X))$. Take the formal slopes at zero of the resulting differential module after scalar extension to $\mathbb C((X))$. Use the empty set of slopes for the zero module. We use three facts of local differential equation theory.

* The Levelt–Turrittin decomposition has finitely many nonnegative rational slopes. Its pure-slope decomposition is functorial and exact, so a subquotient has only slopes already present in the original module.
* Pullback by $X\mapsto X^m$ multiplies slopes by $m$. Rotating $X\mapsto\zeta X$ preserves them. In the ramified decomposition these assertions follow by transforming the pole degrees of the exponential parts.
* A module with only slope zero is regular singular. The formal power-series solutions of a regular-singular complex meromorphic linear system converge near zero (Fuchs's theorem).

See Sabbah, Lecture 2, §2.2.b, Theorem 3, for the formal decomposition and its slope convention. Kedlaya gives the regular-singular convergence theorem in Chapter 7. [Sabbah](https://perso.pages.math.cnrs.fr/users/claude.sabbah/livres/sabbah_chicago1205.pdf) · [Kedlaya](https://doi.org/10.1017/9781009127684.012)

The module $M(F(X^m))$ is the full pullback of $M(F)$. Indeed the Euler derivation scales by $m$ on pullback, and independent derivative basis elements remain independent. Decompose the rational coefficients of a putative relation as $\sum_{r=0}^{m-1}X^r R_r(X^m)$. Terms in different residue classes of exponents do not cancel, and each class would give a relation in the original module. This point concerns ordinary Laurent series with integer exponents.

Write $F_{m,r}$ for the generating series of the coefficient section $L_{m,r}F$. The projection and reconstruction identities are
$$
 mX^r F_{m,r}(X^m)=\sum_{\zeta^m=1}\zeta^{-r}F(\zeta X),\qquad
 F(X)=\sum_{r=0}^{m-1}X^r F_{m,r}(X^m).                              \tag{1}
$$
The sections are D-finite. For example the projection makes $F_{m,r}(X^m)$ D-finite, and splitting rational differential relations by exponents modulo $m$ descends an equation to $F_{m,r}$. A sum of series generates a submodule of the sum of their derivative spans. This latter sum is a quotient of their direct sum. Multiplication by a nonzero rational function preserves the derivative span. The slope facts and (1) therefore give, with $\sigma$ denoting the finite slope set,
$$
 m\,\sigma(F_{m,r})\subseteq\sigma(F),\qquad
 \sigma(F)=\bigcup_{r=0}^{m-1}m\,\sigma(F_{m,r}).                      \tag{2}
$$

Let $S$ be the union of the slopes of the finitely many original coordinates. For $s\in S$ with $s>0$, take depth $k$ in base three. Some ternary section has slope $s/3^k$ by (2). Its binary expansion therefore gives $s/3^k=t/2^l$ for some $t\in S$ and $k\le l\le Ek$. Two different $k$ repeat a $t>0$, which would make a nonzero power of three equal an integral power of two. Thus $S$ has no positive slope. The formal series converge by regular singularity: the vector of basis series is a formal Laurent solution of the rational system given by the Euler derivatives, whose connection (or its dual) is regular singular.

## Elimination of finite nonzero singularities

D-finite analytic germs admit continuation along every path off a finite exceptional set. For each germ use the **actual** nonzero singularities, i.e. points at which some continuation of the original germ along an admissible path fails to extend holomorphically. Poles, branching and irregular singularities count. An apparent singularity at which all continuations extend contributes nothing. Write $T$ for the union of these sets over the original coordinates.

For $\alpha\in T$, projection and reconstruction in (1), together with the fact that $X\mapsto X^m$ is unramified at $\alpha\ne0$, show that $\alpha^m$ is an actual singularity of at least one section, and every actual singularity of a section is an $m$th power of an original one. To see the latter inclusion, lift a continuation path by $X\mapsto X^m$ and use the projection. If all its rotated endpoints have holomorphic continuations then the section extends. To see retention, use reconstruction along a path reaching a singular branch of the original germ. Paths may be perturbed around the finitely many auxiliary preimages and rotated points without changing the selected continuation of the original germ.

By the exact ternary-to-binary expansion, for every $k$ and $\alpha\in T$ there are $\beta\in T$ and $k\le l\le Ek$ with $\alpha^{3^k}=\beta^{2^l}$. Finiteness and multiplicative independence force every $\alpha$ to be a root of unity by the same two-depth argument as for rational poles. Choose $k$ at least the largest 2-adic valuation of these orders. The equality then shows that $\alpha^{3^k}$, hence $\alpha$, has odd order.

Set $I_d(X)=\sum_{e:d_e=d} C_e(X)$ for the two incoming residues $d=0,2$. All its actual singularities are among $T$. The missing outgoing cylinder of exponent $E+1$ makes $L_{q,r}I_d=0$ at the following residue. Take $q=2^{E+1}$ and the unique $r\bmod q$ with $3r+d\equiv r_{E+1}\pmod q$. Thus (1) gives
$$
 \sum_{\zeta^q=1}\zeta^{-r}I_d(\zeta X)=0.                            \tag{3}
$$
If a continuation of $I_d$ had a nonzero finite singularity at $\alpha$, it would have odd multiplicative order. All $\zeta\alpha$ with $\zeta\ne1$ have even order and every continuation there is regular. Continuing (3) along a path reaching that singular branch would express it as a sum of holomorphic germs. Consequently $I_d$ has no finite nonzero singularity. Its original germ is holomorphic at zero, and a generator of $\pi_1(\mathbb C^\times)$ around zero fixes that germ. Analytic continuation and monodromy now give an entire, single-valued function.

The incoming series $I_0(X^3)+X^2 I_2(X^3)$ is entire. By the incidence identity and disjointness of outgoing residue classes, each $C_e$ is a coefficient section of this entire series at modulus $2^e$, hence entire as well.

## Finite mass removes cancellation

Entire coordinates give finite total variation $M=\sum_{e,n}|c_e(n)|$. At each physical vertex the absolute outgoing weight is at most the sum of the absolute incoming weights. Summing over the vertices gives $M$ on both sides. Each local triangle inequality is therefore an equality. Absolute edge weights constitute a nonnegative circulation at the same ceiling.

If a vertex has a positive outgoing weight, its successor has at least that much outgoing weight. Infinite forward survival follows. Indeed its future must eventually repeat a vertex, since infinitely many distinct edges of at least that weight would exceed $M$. After reaching a cycle there can be no positive incoming edge from outside: the nondecreasing weights on a cycle are constant and already supplied by its cyclic predecessor. All nonzero edges therefore belong to finite ordinary cycles.

At any fixed ceiling, the set of vertices surviving $k$ steps has upper natural density at most $(1-2^{-E})^k$ by the dyadic cylinders. The support of each $c_e$ has upper density zero. D-finiteness gives a polynomial-coefficient recurrence valid away from finitely many initial indices, with nonzero leading coefficient beyond a finite threshold. An arbitrarily long zero block beyond this threshold exists by zero density and propagates forever. This proves that every coordinate is polynomial.

The last two sections also show that any solution consisting of analytic germs admitting continuation off finite sets of singularities is entire and supported on finite cycles. D-finiteness is used to conclude that the union of active cycles in such a solution is finite. An infinite weighted union of distinct cycles, if those cycles existed, could have entire coordinates through sufficiently fast decay of its weights.

## Weighted branches and the holonomic spectrum

The slope-transfer argument works at infinity as well: the modules and the pullback identification above are global over $\mathbb C(X)$, and the coordinate $1/X$ again transforms by its $m$th power. Thus all the coordinate modules are regular singular at infinity. An entire solution of a differential system regular singular there has polynomial growth. For example, the local regular-singular solutions on finitely many sectors are combinations of powers, logarithms and convergent series in $1/X$. Cauchy's estimates now make a single-valued entire coordinate a polynomial. [Deligne, II, §1.19](https://publications.ias.edu/node/355)

This yields a weighted extension. Put arbitrary fixed nonzero factors $A_e,B_e$ on the outgoing and incoming branch terms, respectively. The one-step section rule carries factors $B_f/A_e$ on each contributing incoming term. All section coefficients remain constants. The slope arguments at zero and infinity and the singularity argument at finite nonzero points apply verbatim, with weighted incoming totals. The omitted cylinder again makes a dyadic section of every incoming total zero. Hence **every formal complex D-finite solution of the weighted equation is a polynomial solution**.

As before, the finite nonzero edge graph has indegrees and outdegrees exactly one. Around a cycle with successive labels $e_j$ the weights satisfy $A_{e_j}c_j=B_{e_{j-1}}c_{j-1}$. Such a cycle supports a one-dimensional solution precisely when $\prod_j B_{e_j}/A_{e_j}=1$. Consequently the holonomic spectrum for a common ratio $\lambda=B_e/A_e$ consists precisely of the roots of unity whose orders divide an actual cycle period. At ratios $3/2^e$ the holonomic kernel is zero, since $3^p\ne 2^h$ for every nonempty closed word. Multiplying a cycle indicator by its ordinary height introduces the affine carry into this weighted identity. Its resulting equation is inhomogeneous, and injectivity of the weighted homogeneous operator gives no contradiction for the original cycle.
