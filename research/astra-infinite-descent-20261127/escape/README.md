# Dyadic sibling meetings on a specified source interval

Let $T(2n)=n$, $T(2n+1)=3n+2$. Two positive integers meet if their $T$-orbits intersect, with independent nonnegative clocks. For a finite deadline $K$, put

$$
 e_K(n)=\mathbf1_{\{T^i n\ne T^j(3n+2)\ \text{for all }0\le i,j\le K\}}.
$$

This is a finite ordinary-integer computation. Its limit $e_\infty(n)$ is the indicator of genuinely disjoint orbits. The label $b(n)=\mathbf1_{\{n\text{ reaches }1\}}$ is used only in proofs.

## Finite bound in every leading-digit interval

Write $I_k(a)=[2^ka,2^k(a+1))\cap\mathbb N$ and $C_kf(a)=2^{-k}\sum_{v\in I_k(a)}f(v)$. For every function $K:\mathbb N\to\mathbb N$ and all $a,r$,

$$
 \left|C_rb(a)-b(a)\right|
 \le \sum_{k<r} 2^{-k-1}\sum_{v\in I_k(a)} e_{K(v)}(v).                 \tag{1}
$$

Indeed $b(2v)=b(v)$ and $b(2v+1)=b(3v+2)$. Summing the signed right-child increment gives the exact identity

$$
 C_{k+1}b(a)-C_kb(a)
   =2^{-k-1}\sum_{v\in I_k(a)}(b(3v+2)-b(v)).
$$

Any meeting certifies equal labels. The triangle inequality and telescoping give (1). Both formulas, including actual independently clocked tests and arbitrary source deadlines, are checked in [DyadicBoundary.lean](DyadicBoundary.lean).

## Localization using a natural density

Suppose $b$ has natural mean $d\in(0,1)$. In every fixed cone $a\ge1$, every infinite tail of the right side of (1) diverges even with $e_\infty$. Indeed $C_rb(m)\to d$ at every fixed $m\ge1$, by subtracting two ordinary prefix sums. Fix a level $M$, apply (1) at every $m\in I_M(a)$, and average uniformly in $m$. The $k$-th cost on the descendant subtrees becomes exactly the root's $(M+k)$-th cost. The limiting left side is the average of $|d-b(m)|$, at least $\min(d,1-d)$. The derivation of (1) applies to $e_\infty$ since the mismatch is pointwise bounded by $e_\infty$. Thus every infinite tail is bounded below by this positive constant. A convergent nonnegative series would have vanishing tails.

A stronger almost-everywhere conclusion also holds. For real $x\in[a,a+1)$, set $F_j(x)=b(\lfloor 2^j x\rfloor)$. Natural density implies $\int_E F_j\to d|E|$ for every measurable $E$ in the interval. First subtract prefix sums for subintervals, then approximate a measurable set in measure by finite unions of intervals using $0\le F_j\le1$. The set on which all $F_j$, $j\ge M$, equal zero therefore has measure zero. The same holds for one. Take the countable union over $M$. Almost every $x$ has infinitely many changes in both directions. Every such change selects the odd child and certifies $e_\infty(\lfloor2^jx\rfloor)=1$. This gives divergence after restricting the real parameter to any fixed positive-measure subset of any specified cone.

For $v\in I_k(a)$, the weight $2^{-k}$ lies between $a/v$ and $(a+1)/v$. With $a\ge1$, the levels in a cone are pairwise disjoint. Consequently a nontrivial $d$ forces, for every $a\ge1$,

$$
  \sum_{v\in\bigcup_{k\ge0}I_k(a)}\frac{e_\infty(v)}v=\infty.       \tag{2}
$$

Applying this to a hypothetical failure of Collatz uses two separate external arithmetic inputs. Natural density of the basin of one is an integer-target result of Valbuena. Positive lower density of predecessors of every positive odd target coprime to three is the Mazur input. Every nonempty invariant color contains such a target. Remove twos, and if the remaining odd number is divisible by three, take its odd step and again remove twos. Thus a nonempty complement of the basin would imply $0<d<1$. The written deduction uses these reported inputs. They are outside the Lean kernel in this directory. [Valbuena, *Collatz basin densities and canonical traces from first-passage stabilization*](https://doi.org/10.5281/zenodo.23025885) · [Weaver, sources and application of positive lower density to both colors](https://rstation.ai/problems/collatz/papers/225)

On those inputs, it suffices to find just one positive $a$ and $B<\infty$ such that for all $Y$ there exists a single $K$ with

$$
 \sum_{\substack{v\le Y\\v\in\bigcup_k I_k(a)}} \frac{e_K(v)}{v}\le B.       \tag{3}
$$

For finite $Y$ all intersecting pairs among those tested have finite witness times. One common $K$ realizes $e_K=e_\infty$ there, so (3) is exactly boundedness of the increasing harmonic sums in (2). If all positive integers reach 1, it holds with $B=0$. The needed estimate (3) remains open. The quantifier $\forall Y\,\exists K$ permits arbitrarily long searches.

## A proof that only needs lower densities and qualitative pair fusion

There is a second route to the almost-everywhere conclusion and (2). It gives the same conclusion for a completely invariant binary color as soon as both its colors have positive lower natural density, without assuming that either natural density exists. Here the inputs are the two fixed-state qualitative counted-fusion estimates, for the adjacent pair $(x,x+1)$ and for $(x,3x+2)$ with formal counts $(0,1)$. On every full native octave the fractions of finite failures tend to zero by exact binary transport. [Leen, *Exact rates in Collatz synchronization*](https://doi.org/10.5281/zenodo.23268751) · [Weaver, scalar estimates and exact cylinder transport](https://rstation.ai/problems/collatz/papers/124/v1)

With $F_j(x)=b(\lfloor2^jx\rfloor)$ on the positive real half-line, these bounds imply, for every compact interval $K\subset(0,\infty)$,

$$
 \|F_j(2\,\cdot)-F_j\|_{L^1(K)}
   +\|F_j(3\,\cdot)-F_j\|_{L^1(K)}\longrightarrow0.
$$

Indeed $F_j(2x)=F_{j+1}(x)$. On each cell with parent $v$, the even half has its parent's color and the odd half has color $b(3v+2)$. The second difference uses the three values $b(3v),b(3v+1),b(3v+2)$ on thirds of the cell. Compare the first two to the last by at most two adjacent color differences, then compare $b(3v+2)$ to $b(v)$. All the relevant indices lie in a fixed finite number of growing full octaves; their exceptional proportions tend to zero. Partial cells at an interval end cost $O_K(2^{-j})$.

From any subsequence take a further subsequence converging weak-* locally to $F$ by boundedness, diagonal extraction and separability of $L^1$ on bounded intervals. The display passes exactly to the weak limit and gives $F(2x)=F(3x)=F(x)$ almost everywhere. In logarithmic coordinates this is a bounded measurable function invariant under translation by $\log2$ and $\log3$. These generate a dense subgroup. Continuity of translations in local $L^1$ extends invariance to every translation, forcing $F$ to be almost everywhere constant, say $c$. This compactness step identifies possible limiting shapes. It does not assert that different subsequences choose the same constant.

If both color classes have lower natural density at least $\epsilon>0$, every such $c$ belongs to $[\epsilon,1-\epsilon]$. The integral of $F_j$ on $[0,1]$ equals the ordinary color proportion up to an endpoint error $O(2^{-j})$. To pass that integral to the local weak limit, first restrict to $[a,1]$ and then let $a\downarrow0$, using $0\le F_j\le1$. Thus for every bounded measurable $E\subset(0,\infty)$ of positive measure, the liminf of $\int_E F_j$ is at least $\epsilon|E|$, and the limsup is at most $(1-\epsilon)|E|$. Otherwise take a contradicting subsequence and extract its constant weak limit. Applying this to a set on which the color is eventually fixed (and taking a countable union over its starting index) proves that almost every ray sees both directions of change infinitely often. This supplies the one-cone conclusion on the Mazur lower-density input without Valbuena's natural-density theorem.

Vanishing sibling disagreement alone gives weak limits in this argument. Strong convergence on any fixed positive-measure set along even one subsequence would force a binary local limit, incompatible with the preceding interior constants. The reflected map $T^-(n)=(3n-1)/2$ at odd $n$ also exhibits the distinction. Negation conjugates its pair $(n,3n+1)$ to the integer canonical pair $(x,3x-1)$ for $T$ on the two-adics. It therefore has the same qualitative finite pair-fusion property. It has distinct cycles through $1$ and $5$, and the nonperiodic units $11$ and $13$ enter these respective cycles. The reflected predecessor lower bound gives positive lower natural density to both basins. This example concerns the minus sign. [Reflected predecessor lower bound, Lemma 4.1](https://rstation.ai/problems/collatz/papers/200/v1)

## Attribution and scope

Weaver already proves collapse to density zero or one from summability of the global dyadic sibling variations for an eventually invariant binary coloring. The proof there builds a strong limiting coloring invariant under multiplication by two and three, without assuming the natural mean. That global criterion is prior work. Here (1) keeps a source-dependent finite deadline on every original integer in a specified cone, while (2) gives the localization and the almost-everywhere oscillation, with either the separately available natural mean or the two qualitative pair-fusion inputs. The pair-clock note estimates bounded-deadline meetings in a complete source octave and explains why some short deadlines have a divergent harmonic cost. [Weaver, *Distinct affine branches of the signed Collatz maps have distinguishable continuations*, “Density from dyadic siblings”](https://rstation.ai/problems/collatz/papers/212) · [Pair clocks](SUPERNATIVE_PAIR_CLOCK.md)


## Pointwise ordinary predecessors and fixed clocks

The unit-preserving inverse construction produces a visitor to every positive odd target prime to three in every sufficiently large relative interval. Its actual shortcut clock is at most a constant above the halving lower bound, and its odd grade is bounded in terms of the window width. The onset divided by the target is uniform across targets. The rotation net, marked integer window realization and unconditional theorem are kernel checked. [Physical construction](FAST_PREDECESSOR.md) · [Marked mesh](WindowMesh.lean) · [Unconditional visitor](FastWindow.lean).

At fixed grade \(d\), the number of odd unit sources hitting an ordinary unit target at exact shortcut clock \(m\ge1\) is a polynomial of degree \(d-1\) in \(m\) plus a bounded periodic function. Every nontrivial pole is simple by a strictly increasing conductor calculation. The pointwise local limit then gives \((1+o(1))3^{-d}{m\choose d}\) actual first-hit sources of either parity at dilute growing grades, up to \(d\le\exp(c\log^2(m/d))\), \(c<1/(32\log3)\). The exact Fourier proof and the local limit are written analyses. The fixed-clock recurrence has an independent bounded integer replay. [Clock poles](CLOCK_POLES.md) · [Sparse local limit](SPARSE_TILT.md) · [Elementary rank sandwich](SPARSE_FIRST_HITS.md) · [Sparse finite checks](check_sparse.py).

The separate two-clock and inverse-ladder replay checks 21,840 ordinary pair sources in six complete finite octaves and 864 first-hit examples. Its output concerns only the displayed finite parameters. [Script](check_escape.py) · [Exact receipt](../../../reports/astra-infinite-descent-20261127/escape/BOUNDED_REPLAY.json).

At the fair weight \(3^d2^{-m}\), the fixed-root closed-support theorem and uniform high-vertex packing from PR193 give one compact null set containing the normalized corrections of every simple odd segment. It controls the contribution of all starting integers above a cutoff *uniformly* in the target, grade and physical clock. The limiting largest normalized first-visit row is the mass of an actual finite synchronized class of escaping sources, if any exist. The dependencies are written manuscript inputs. [Universal correction support and fair clock rows](FAIR_CLOCK_DIFFUSION.md).

At dense tilt \(p>3/4\), the actual all-depth inverse mass at each positive odd unit \(y\) is \(O_{p,N}(y^{\log(3p)/\log(3/2)}(\log y)^{-N})\) for every fixed \(N\). The proof includes periodic roots. The ascent input is attributed to Weaver 174, with a separate positive-coordinate derivation using Evertse's theorem. [Dense tilted height bounds](TILTED_HEIGHT.md) · [Maximal ascent budgets and prior results](MAXIMAL_ASCENTS.md).

The marked window theorem simultaneously prescribes the visit time and odd grade in any fixed nonzero moduli. For fixed synchronized source patterns the rotation gaps also bound the optimal additive time overhead, up to a pattern-dependent constant away from exact gap widths. [Marked ordinary visitor](MarkedWindow.lean) · [Clock cost for finite patterns](FAST_PREDECESSOR.md).

The exact-clock target test has an unconditional Lean equivalence with boundedness of every positive shortcut orbit. Every first-arrival row above a given threshold must pass through a small odd input. The source-side compact null-set theorem and subsequent stabilization of the extremal classes use separate written inputs. [High-target bound and formal dependencies](HIGH_TARGET_ROWS.md) · [Computable row criterion](TargetExtinction.lean) · [Eventual extrema and finite replay](EXTREMAL_ROWS.md).
