# A logarithmic Stieltjes lower bound forced by one ordinary escaping orbit

**PROPOSED, source-qualified.** Let $\mu$ be the positive [ordinary escape distortion measure](HARMONIC_OFFSET_CONE.md) on $(0,1]$, in the mean-one ternary normalization. Set
$$
 L(c)=\int_{(0,1]}(1+cr)^{-1}\,d\mu(r).
$$
For every fixed escaping ordinary component $C$, its submeasure satisfies
$$
 \mu_C((0,r])\ge c_0 r\quad(0<r<r_C)
$$
with an absolute $c_0>0$ and an onset depending on the component. Consequently, if $K$ distinct escaping components exist, then
$$
 \liminf_{c\to\infty}\frac{cL(c)}{\log c}\ge c_0 K.
$$
This holds for every finite number $K$ of selected components; infinitely many escaping components force this quotient to tend to infinity. Thus along any unbounded sequence an upper bound $L(c)=o(\log c/c)$ suffices to exclude escape. This strengthens the $cL(c)\to0$ test from the [positive Stieltjes sum rules](STATIONARY_ZERO_FLUX.md) (source commit `a47e553`). An ordinary proof of this spatial error rate remains open.

## Disjoint entrants on one component

Fix a positive escaping odd-unit spine $y_i$ and let $S_j=\sum_{i\ge j}1/y_i$. Simple-orbit packing gives $S_j<\infty$ and $S_j\downarrow0$. At each $y_{i+1}$ take the distinct unit sibling $s_i=4y_i+1$ when it is a unit, and $s_i=16y_i+5$ otherwise. The latter is a unit in the remaining case; both have $U(s_i)=y_{i+1}$, and $y_i<s_i\le21y_i$. No $s_i$ lies on the spine, and their predecessor basins are disjoint, since once an orbit leaves $s_i$ it stays on the spine.

There are absolute $B,b>0$ such that at every unit $s$ and every sufficiently large inverse depth $k$ there is total word weight at least $b$ with real offset $\beta\le B$. This is the [bounded-real finite word floor](../terminal-residue/ENDPOINT_ODOMETER.md), from the bounded-offset event of paper 12, summed over central totals, followed by one bounded outer exponent to spread to all unit residues. The floor concerns compatible words; at a positive odd root they all have actual positive odd source numerators.

For $l\ge i+1$ extend these words at $s_i$ by the path $s_i,y_{i+1},\ldots,y_l$. Its multiplier divided by $y_l$ is at least $c_1/s_i$ by the uniform simple-path reciprocal product. The resulting full relative offset $r$ satisfies
$$
 (3s_i+1)^{-1}\le r\le B/s_i+\tfrac13(s_i^{-1}+S_{i+1})\le C_1 S_i.
$$
The lower bound uses the first edge out of $s_i$. For the upper bound compose $1-r$ as the product of the pre-entry distortion factor $1-\beta/s_i$ and the subsequent ordinary factors, then bound their total loss by the sum of their losses. Every such full path is simple. For a fixed finite list $j\le i\le M$, these contributions remain disjoint at each common target $y_l$, by their incomparable entrants.

In the length-$Q$ marked harmonic sum take $M+1\le l\le Q-k_0$ with $k_0$ a common onset for the floor. The required input depth is $Q-(l-i)$, which is at least $k_0$. For large $Q$ all the $y_l$ fit under the physical cutoff $2\cdot3^Q$. Each such $l$ contributes at least $c_1 b\sum_{i=j}^M 1/s_i$ before division by $Q$. The finitely selected marks belong to a compact interval in $(0,1]$ with upper endpoint $C_1S_j$ and strictly positive lower endpoint depending on $M$. The compact-set bound for vague convergence of the component-marked cone measures gives
$$
 \mu_C((0,C_1 S_j])\ge c_1 b\sum_{i\ge j}1/s_i\ge (c_1 b/21)S_j
$$
after $M\to\infty$, for $j$ large. Equivalently the same finite-entrant construction can be made simultaneously on finitely many components, with no disintegration assumption. For the component-marked limit, restrict the original finite visit-indicator proof to low states in $C$; every nonempty monomial remains in that component and has the same canonical trace.

Since $y_{j+1}\le 2y_j$, $S_j\le3S_{j+1}$. The tail-sum scales therefore have bounded successive ratios, giving a uniform lower linear mass at every sufficiently small radius. Finally, $1/(1+cr)=\int_r^\infty c(1+cu)^{-2}\,du$. Integrating the small-radius floor yields $(c_0/c)(\log(1+cr_C)+1/(1+cr_C)-1)$. Sum over any fixed number of components before sending $c$ to infinity. Also $d[cL(c)]/d\log c=\int c(1+cr)^{-2}\,d\mu$ has strictly positive lower limit under escape, by restricting to $r\le1/c$. Thus even a vanishing subsequence of this local logarithmic-scale slope excludes escape.

## Sharpness for a nondiagonal lift of the same coupled affine system

Positivity and additional levels of side ancestry do not alone force a second logarithm. Here the real and local phase coordinates follow the exact Syracuse branches but are not identified with one common ordinary integer. Take real $y_0>0$ and $y_i=-1+(y_0+1)(3/2)^i$, with ternary and dyadic phases fixed at $-1$; the dyadic phase has valuation one throughout. At the ternary phase $-1$, all legal incoming exponents except the cycle exponent $1$ form exactly the inverse family at the even rational $-2$ with its outer exponent increased by one. This multiplies real offsets and weights by $1/2$. By the [rational trace theorem](RATIONAL_PHASE_TRACE.md), $-2$ has finite positive trace (the cutoff removes the unique incoming cycle edge). Thus its [unnormalized compact real fibre](FINITE_TRACE_FIBRES.md) gives a fixed nonzero finite compact side measure $D$ after the factor-$1/2$ dilation and mass factor. This measure includes the full further inverse ancestry of all those side entrances.

Choose an initial $i_0$ large enough that all offsets $B$ in the support of $D$ are below $y_{i_0}$. Inserting one such entrance at $y_i$, then following the spine for $k$ steps, sends its real offset to $-1+(3/2)^k(B+1)$ and its endpoint to $-1+(3/2)^k(y_i+1)$. The limiting relative mark and weight are exactly $(B+1)/(y_i+1)$ and $D(dB)/(y_i+1)$. The resulting finite summed entrant measure has
$$
 \widetilde\mu=\sum_{i\ge i_0}\alpha_i(B\mapsto\alpha_i(B+1))_*D,
 \qquad \alpha_i=(y_i+1)^{-1}.
$$
Because $1\le B+1\le C_D$ on its support and $\alpha_i$ decreases geometrically, $\widetilde\mu((0,r])\asymp r$. In fact its transform satisfies
$$
 c\widetilde L(c)=\frac{\log c}{\log(3/2)}\int\frac{dD(B)}{1+B}+O(1).
$$
For $c\alpha_i\ge1$ replace $c\alpha_i/(1+c\alpha_i(B+1))$ by $1/(B+1)$ with total bounded error from the geometric sum of $(c\alpha_i)^{-1}$. The remaining terms are bounded by the geometric sum of $c\alpha_i$. This shows sharp single-logarithm behavior for the full inward side measure in this specific lift. It supplies no positive integer orbit and no upper bound for the ordinary Stieltjes transform. Any stronger ordinary lower bound needs information beyond this elimination of nested side families.

## The same mechanism at each physical target

At every finite-trace ternary unit $t$ let $F_t$ denote its unnormalized canonical real fibre, and let $M(t)=\sup_{w\ {\rm legal\ at}\ t}\beta_w=(G(t)-1)/3$. Uniformly in $t$ and $T>0$,
$$
 F_t([0,T])\gg\min\{T,M(t)\}.
$$
In particular at all $s\ge1$,
$$
 \int\frac{F_t(dB)}{s+B}\gg \log(1+M(t)/s).
$$
The first estimate includes phases that are not ordinary targets. On every fixed escaping positive spine it gives the pointwise lower bound $\int(1+B)^{-1}F_{y_j}(dB)\gg_n\log y_j$, since the prefix from the fixed source has $\beta_w\gg_n y_j$ once a single source step is included. More generally, for every positive ordinary odd unit $t$ its least positive odd ancestor $m_{\leftarrow}(t)$ satisfies $M(t)\gg t/m_{\leftarrow}(t)-O(1)$: on a simple first-hit path the full multiplier is $\gg t/m_{\leftarrow}(t)$, and its contribution to $\beta_w$ is one third of that multiplier.

To prove the estimates, each legal prefix at $t$ gives a sequence $P_i$ and offsets $r_i=\sum_{j\le i}P_j/3$. The unit siblings at the first changed letter $i$ give mutually disjoint contributions of mass $\gg P_i$ and real offset at most $r_{i-1}+C P_i\le C' r_i$, by the [bounded-real floor](FINITE_TRACE_FIBRES.md). For $i\ge2$ one has $P_i\le(3/2)P_{i-1}$, so $r_i/r_{i-1}\le5/2$. Also $r_1\le1/2$. For $T$ larger than a fixed constant, stop the prefix at its last $i$ with $C'r_i\le T$. Retain all contributions up to this index. Their total is $\gg\min(T,r_{\rm final})$ whether or not the next letter crosses the threshold. Take the supremum over prefixes. For smaller $T$, use the uniform small-offset floor established for the compact support theorem, adjusting constants on the intervening bounded interval. Finally integrate the distribution function against $(s+T)^{-2}$. The integral of $\min(T,M)/(s+T)^2$ on the positive half-line is exactly $\log(1+M/s)$.

This proof gives a finite-depth variant at arbitrary ternary phases. At total inverse depth $q$ use the finite-word bounded-offset floor after every chosen sibling, and maximize $\beta_w$ over prefixes of length at most $q$. For $T$ above an absolute constant the same CDF lower bound applies to the truncated real-offset word mass; with boundedly many remaining letters one enlarges the fixed offset cutoff to obtain the uniform unit floor. This statement uses $\beta_w$ itself at total depth $q$, keeping the independent stationary tail out of the truncation.
