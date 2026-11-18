# Exact affine coarea after translating the target grid

**Proposed.** Use the notation of the [ordinary offset cone](HARMONIC_OFFSET_CONE.md). At odd depth $Q$ an inverse word $w$ of total valuation $A$ has slope $J_w=3^Q2^{-A}$ and positive real offset $F_w$ in $t=J_wx+F_w$. Its legality selects one residue modulo $3^Q$, hence exactly one odd representative $t_w$ in $(0,P]$, $P=2\cdot3^Q$. For a common real parameter $0\le u<1$, let $t_w(u)$ be the representative of $t_w+uP$ modulo $P$ in $(0,P]$. For Borel $I\subseteq[\theta,1]$, $\theta>0$, define the sum without a simplicity restriction
$$
 S_Q^u(I)=\sum_w\frac{J_w}{t_w(u)}{\bf1}_{F_w/t_w(u)\in I}.
$$
At $u=0$ this dominates the corresponding arithmetic simple-path cone. At other shifts the expression is a real-grid comparison; its points need not carry the ordinary inverse word.

For fixed $w$, $t_w(u)$ is uniform on $(0,P]$ under uniform $u$. Tonelli and $z=F_w/t$ therefore give exactly
$$
 \int_0^1 S_Q^u(I)\,du
 =\frac1P\sum_w J_w\int_{I\cap[F_w/P,\infty)}\frac{dz}{z}
 \le\frac12\int_I\frac{dz}{z}.
$$
Indeed $\sum_w J_w=3^Q$ by the geometric one-letter probabilities. For fixed $\theta$ and all sufficiently large $Q$ equality holds in the upper bound: $F_w\le(3/2)^Q-1$ for every word, so $F_w/P<\theta$. In particular the normalized cone away from zero tends to zero in shift average, with an $O_\theta(1/Q)$ bound. This does not estimate it at the arithmetic phase $u=0$.

## An exact obstruction to a uniform trace at phase zero

Suppose a unit $n$ has a divergent odd orbit $y_j=U^j(n)$. Write $D_j$ for its slope to $y_j$, and $L_j=\sum_{i<j}\log_2(1+1/(3y_i))$. The simple-orbit packing bound gives $L_j\to L_\infty<\infty$. Every odd source reaching $n$ does so only once. All such corrections to $n$ lie in a compact null set $K_n$: for unit sources this is the finite-translate argument for [integer root code supports](../terminal-residue/SUPPORT.md). Including nonunits preserves the conclusion: their global-minimum residues are either zero or within $O(1/x)$ of the unit sibling residue at $4x+1$. Thus the full residue closure only adds at most countably many isolated-from-the-unit-closure values; taking the finite translates for the possible minima $\le n$ again gives a compact null set. Intersect with the nonnegative correction range.

The translates $K_n+L_j$, $j\ge1$, together with $K_n+L_\infty$ form a compact null set. Under $v\mapsto1-2^{-v}$ their union has compact null image $E_n$ bounded away from both zero and one, since $L_j\ge\log_2(1+1/(3n))$. At phase zero every depth-$Q$ path through $n$ with $j$ remaining steps, $1\le j\le Q$, has distortion in this **same** set $E_n$ by the product identity. Its path is simple. For all large $Q$ all $y_j$ with $j\le Q$ are in the first period. Consequently their distinct endpoint contributions to the cone on $E_n$ are at least
$$
 \sum_{j=1}^Q\frac{D_j}{y_j}\,g_{Q-j}(n)\gg_n Q.
$$
Here $D_j/y_j=2^{-L_j}/n$ is bounded below, and the nonnegative ordinary-depth transfer $g_k(n)$ has positive Cesàro mean at this fixed root, as in the cone criterion. In contrast, the displayed shift integral for the very same $E_n$ is zero at every depth. This identifies the missing estimate: a bound at the distinguished ordinary phase that excludes a linear accumulation of these inherited words. No claim about convergence at each other individual shift follows from the integral.
