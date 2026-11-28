# The ordinary finite clock envelope on one fixed irrational source

Let $T$ be the native shortcut map on the $2$-adic integers. Let $X$ denote its closed set of odd sources $s$ for which the two branch maps from $s,3s$ have distinct affine formulas at every finite date. At a date $k$, let $G_k(s)$ count both tracks' odd letters. As in the [master equation](ADJACENT_CYCLE_CLOSURE.md), $K(G)$ is the largest native date achieved by a positive ordinary odd integer, different from its triple at every synchronized orbit date through that horizon, using at most $G$ odd letters.

**Proposed variational formula.** Take a nondecreasing $F:\mathbb N\to(0,\infty)$ tending to infinity and satisfying $F(G+c)/F(G)\to1$ at every fixed integer $c\ge0$. Write $D=\limsup_{G\to\infty}K(G)/F(G)$, allowing infinity. For every $s\in X$,
$$
        \limsup_{k\to\infty} k/F(G_k(s))\le D.
$$
Equality holds for a dense $G_\delta$ subset of $X$. Consequently the uniform assertion $K(G)=O(F(G))$ is equivalent to the assertion that **each fixed $s\in X$** satisfies $k=O_s(F(G_k(s)))$. It suffices to require this pointwise assertion on any nonmeager subset of $X$.

For the particular scale $F(G)=(G+1)\log_2(G+2)$, every nonempty relative cylinder in $X$ also contains continuum many fixed $2$-adic irrationals such that
$$
             \liminf_{k\to\infty}\frac{k}{(G_k(s)+1)\log_2(G_k(s)+2)}\ge\frac12.       \tag{1}
$$
Their two native trajectories are value-distinct at every date. The odd density of each track tends to zero.

## Appending ordinary records

A finite prefix from $X$ is a dyadic cylinder on which none of the same-date affine differences vanishes identically. Choose a positive odd integer in this cylinder outside the finitely many roots of those differences. Its native prefix realizes the same $G_k$ with value-distinct endpoints at every date. Thus $k\le K(G_k)$. The elementary [finite clock bound](PAIRED_SOURCE_GRADES.md) forces $G_k\to\infty$ for every source of $X$, proving the upper inequality.

From any such prescribed cylinder, the [constructive signed return](SignedReturnRouter.lean) appends a fixed finite refinement to the adjacent relation $A-B=1$, in the original ordering. An even/odd letter pair then gives $B'=3A'-1$, the genuine relation after the first odd/odd departure on every odd ordinary input and its triple. The varying lower coordinate is an affine progression with odd step after dividing out the cylinder modulus. A prescribed lower word of length $t$ fixes one lower residue modulo $2^t$. One representative of that residue already supplies the original paired record. Every other representative has the same companion residue $3A'-1$ modulo $2^t$, so it supplies the same upper word, regardless of which final arm has the larger grade. The [native word divisibility theorem](AdjacentWordClosure.lean) gives the residue characterization.

Fix the initial cylinder. After this fixed entrance, append all but the first date of an ordinary record of length $K(G)\ge1$. Its length changes by a fixed additive constant and its new total grade is at most $G+c$ with $c$ fixed independently of the record. At the terminal date the two branch maps are distinct because the record has a value-distinct representative. The [primitive closure theorem](PRIMITIVE_SPARSE_PAIR_CLOSURES.md) guarantees a further continuation inside $X$. The resulting record cylinder is therefore nonempty relative to $X$.

If $0<d<D$, every nonempty relative cylinder thus contains, for each $N$, a subcylinder realizing $k/F(G_k)>d$ at some $k>N$. Indeed choose a record whose original ratio exceeds a fixed $d'>d$ at an arbitrarily large budget, and use $F(G+c)/F(G)\to1$. Each union of the qualifying relative cylinders is open and dense. Intersect over $N$ and rational $d\uparrow D$, or $d\to\infty$. Baire's theorem applies to the closed nonempty set $X$. When $D=0$ the upper bound already gives equality everywhere. This proves the formula and its nonmeager-set consequence. A countable collection of specified scales may be realized simultaneously by intersecting their residual sets.

## Thin at every sufficiently late date

The [exact-grade primitive construction](PRIMITIVE_SPARSE_PAIR_CLOSURES.md) supplies, for each large $p$, an adjacent return word pair of common grade $p$ and length $L_p\ge(1-o(1))p\log_2p$. These pairs can be concatenated at translation one without any connecting cost. Each finite concatenation has a nonempty full dyadic cylinder, and nested increasing prefixes specify a unique $2$-adic source. The two values differ by exactly one after every completed return, excluding an earlier synchronized value merger by forward determinism.

Starting from the adjacent relation reached from the prescribed cylinder, at stage $m$ append $m$ copies of the pair of exact grade $2^m$. Before each copy one may insert either of two fixed adjacent return pairs with opposite initial lower letters. For an even initial lower letter use lower $(0,1)$, upper $(1,0)$, satisfying the ordered equation. For an odd initial lower letter start from the ordinary adjacent input $(3,2)$ with first letters $(1,0)$; its endpoints $(5,1)$ are distinct ternary units, so the [adjacent-prefix closure](PrefixCarryClosure.lean) supplies a fixed return beginning with those letters. Different infinite choices yield different source bits at their earliest differing marker.

At every position in stage $m$, the accumulated common grade of the completed main pairs is between constant multiples of $m2^m$, using just the preceding stage for the lower bound. The contribution from stages $j<m-\lfloor\sqrt m\rfloor$ is $O(m2^{m-\sqrt m})$. Thus all but an $o(1)$ fraction of this accumulated grade came from pairs of clock at least $(1-o(1))p(m-\sqrt m)$. All markers so far use $O(m^2)$ grade, and the still-incomplete main copy uses at most $2^{m+1}$ combined grade. Both are $o(m2^m)$. Writing $P$ for the accumulated common grade of completed main pairs, we have $G_k=(2+o(1))P$, $\log_2 G_k=m+O(\log m)$, and $k\ge(1-o(1))Pm$, uniformly even within an entrance or exit of a long pair. This proves (1) at every sufficiently late date. The markers give continuum many choices in every prescribed relative cylinder.

Finally, if $w=a/q$ is a nonzero rational $2$-adic source in lowest terms with $q>0$ odd, the numerator on any nonzero native orbit remains a nonzero integer over denominator $q$. An odd step satisfies $2|w'|\le(3+q)|w|$, and an even step gives equality with factor one. If the orbit avoids zero, then
$$
                     2^k\le |a|(3+q)^{g_k(w)}.
$$
If it reaches zero it has only finitely many odd letters. Every constructed main copy has increasingly many odd letters on each arm, while (1) forces $G_k/k\to0$. Therefore the constructed sources are irrational. In particular, the fixed-path formulation does not transfer its superlinear witnesses to a fixed positive integer or resolve whether the uniform logarithmic upper bound holds.
