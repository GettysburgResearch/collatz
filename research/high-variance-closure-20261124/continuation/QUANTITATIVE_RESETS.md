# Growing relative reset losses paid by the same physical clock

**Status.** Written quantitative strengthening of the weighted-frequency and finite-attractor implications in RESET_COSTS.md. The proposed global debit (4) remains OPEN. The only Diophantine input is an established two-logarithm lower bound for the fixed rational integers 2 and 3. No stationary law for an exceptional ordinary source is assumed.

Put $\alpha=\log_3 2$. Fix effective constants $c_0>0,\kappa\ge1$ such that $\|h\alpha\|\ge c_0 h^{-\kappa}$ for every integer $h\ge1$. These exist by Baker–Wüstholz applied to $h\log 2-r\log 3$, $r$ the nearest integer to $h\alpha$. The form is nonzero by unique factorization, the two logarithms are fixed real logarithms of algebraic numbers, and $|r|=O(h)$. Only existence of a positive exponent below is claimed; no favorable numerical irrationality measure is assumed. [Gouillon, 2006, Corollary 2.3](https://www.numdam.org/item/JTNB_2006__18_1_125_0.pdf), a fixed two-logarithm bound with the same required consequence

## A covering and crowding estimate for the same rotation

For $H\ge2$ Dirichlet approximation supplies $p_0/q$ in lowest terms with $1\le q\le H$ and $|q\alpha-p_0|\le1/H$ (reduce the fraction if needed). Then $q\ge (c_0 H)^{1/\kappa}$. In any consecutive block of $q$ rotation dates, the points are within $1/H\le1/q$ of a translated grid of mesh $1/q$: use the block's first actual phase as the grid origin and compare the $j$th increments for $0\le j<q$. Every arc of length larger than $4/q$ is visited in that block. Its upper number of visits to an arc $I$ is at most $q|I|+4$, by widening the grid arc. Cover $H$ dates by at most $2H/q$ complete blocks, enlarging the last partial block for the upper count. Uniformly in the starting angle, any arc longer than $C H^{-1/\kappa}$ is visited, and
$$\#\{0\le j<H:\theta-j\alpha\in I\}\le C H (|I|+H^{-1/\kappa}).\tag{1}$$
Endpoint conventions are absorbed by increasing the absolute grid rounding constant.

## The given selector is quantitatively thin in physical time

Use exactly the selector and image $S$ of ../SPARSE_RESET_MEASURE.md. At large input $n$ its search length $H$ is comparable to $\sqrt{\log n}$. Throughout that single true prefix the actual phases $\log_3(T^j n)$ differ from the ideal rotation by at most $O(H2^H/n)$ modulo one, and $\log(T^jn+2)=\log(n+2)+O(H)$. The error follows by summing the positive correction at the odd source states, each at least $n/2^H$.

For $t$ choose a ternary width $3^{-t}$ between $A H^{-1/\kappa}$ and $3A H^{-1/\kappa}$, where $A$ is a sufficiently large fixed constant. For large $n$, $0\le t\le\lfloor\log_2 n\rfloor$. The projected interior strip from $7+3^{-t}/4$ to $7+3^{-t}/2$ has length at least a constant times $3^{-t}$ and a margin of the same order inside the full strip. The first assertion of (1) gives a hit whose actual phase remains in the full strip. All involved heights are large, so the ternary scale index is nonnegative. The selected largest depth is at least $t$. Since $S$ is the image of the selector and unbounded outputs must arise from unbounded inputs, its large elements $z$ satisfy
$$\operatorname{dist}_{\mathbf R/\mathbf Z}(\log_3 z,\log_3 7)\ll (\log z)^{-p},\qquad p=1/(2\kappa)>0.\tag{2}$$
The comparison of logarithmic heights on the searched prefix transfers the bound from source to selected output. This is an estimate for the actual prescribed image, not a replacement by independently sampled hits.

Return to any sufficiently large positive ordinary start $n$, and now take a fresh length $J=\lfloor\sqrt{\log(n+2)}\rfloor$ actual block. Every member of $S$ in that block lies in an arc of length $O((\log n)^{-p})$ by (2), since all block logarithmic heights are comparable. The finite phase error is $o((\log n)^{-p})$. The upper bound in (1) with $H=J$ shows
$$\#\{0\le j<J:T^j n\in S\}\ll J(\log n)^{-p}.\tag{3}$$
The estimate is uniform over every sufficiently large ordinary starting point. It has no conditional-independence requirement.

## One-source summation, including the uncompleted final block

Fix $0<\delta<p$, $w(n)=1/\log(n+2)$, and let $L(n)=(\log(n+2))^\delta$. On any complete block in (3), the total cost from reset sites, weighted by $w L$, divided by the total $w$ cost of the block, is $O((\log n)^{\delta-p})$. For an escaping orbit, concatenate these prescribed dynamic blocks along its own successive states. The weight sum diverges because $T^i n+2\le2^i(n+2)$. All sufficiently late complete-block ratios tend to zero. An unfinished final block has absolute $w L$ cost $O((\log n)^{\delta-1/2})=o(1)$ from its starting height $n$, even if every one of its dates is charged. This proves
$$\sum_{i<N:X_i\in S}w(X_i)L(X_i)=o\left(\sum_{i<N} w(X_i)\right)$$
on the same escaping ordinary source, without any reciprocal-summability input.

In particular, let $y$ run over odd valley starts, let $\ell$ be its actual full shortcut length and $z=T^\ell y$. Suppose there were a finite nonnegative ordinary potential and constants $c>0,0\le C<\infty$ such that for all large $y$
$$V(y)-V(z)\ \ge\ \sum_{j<\ell}w(T^j y)\,[c-C L(T^j y){\bf1}_S(T^j y)].\tag{4}$$
This permits an unbounded relative loss at every actual reset. It would force every positive orbit to enter a fixed finite interval. Indeed choose $B$ beyond the hypothesis cutoffs so every complete block started above $B$ has reset cost ratio below $c/(2C)$ (if $C=0$ dispense with the toll). An orbit staying wholly above $B$ has divergent total cost and an unfinished block with uniformly bounded absolute toll, contradicting the telescoping lower bound on $V$. The conclusion includes cycles entirely above $B$; cycles visiting the interval still require identification. Although this improves the sufficient reset allowance, the first-hit clock's exact loss equals the next inter-reset credits. (3) is an upper frequency estimate and supplies no bound realizing (4) for that rank or for a multiscale sum.
