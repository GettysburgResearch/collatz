# Exponential denominator growth through six odd-valuation mismatches

For every primitive positive rational cycle with odd period $p$, complete reduced denominator $q$, and a proper odd-valuation rotation with at most six mismatches, one has, for all sufficiently large $p$,
\[
                            \boxed{\log_2 q>p/4096.}                 \tag{1}
\]
The onset is ineffective. There is no upper bound assumption on the clock error $\Lambda=h-p\log_2 3$, on the largest valuation, or on the order of the rotation. This strengthens the rational denominator conclusion of [the six-mismatch theorem](SIX_ROTATIONS.md). The at-most-six restriction is essential to the present certificates. No bound on every rotation of an arbitrary ordinary cycle follows.

Put $\varepsilon=1/4096$ and suppose instead that $q\le2^{\varepsilon p}$ along an unbounded sequence. Use the [two chronological cut lists](FIVE_ROTATIONS.md), with the same $\gamma=\log_2 3$, $\beta=\gamma-1$, $l_i,U_i,V_i,u_i,v_i$. Here $U,V$ are still the **unshifted** logarithms of the true integer numerators divided by $p$. Write $A_i$ in this note for the actual common divisions in arc $i$ **divided by $p$**. Let $B_i=\min(U_i,V_i)$ and $E_i=\min(u_i+v_i,U_i,V_i)$.

## Heights and chronological growth without a clock error bound

Odd numerators obey $2^{e_j}y_{j+1}=3y_j+q$. For every odd step,
\[
 y_{j+1}+q\le (3/2)(y_j+q).
\]
At a selected step of exponent $e_j$, one also has
\[
 y_{j+1}+q\le(1+q)y_{j+1}\le(1+q)(3/2)(y_j+q)2^{-(e_j-1)},
\]
because $y_{j+1}$ is a positive integer. On each list, charging its selected excess only at its distinct selected departures gives for the prefix rows of the five-mismatch proof the lower bound $-(j+2)\varepsilon-o(1)$ at the $(j+1)$st chronological cut, $j=0,\ldots,s-1$. In fact the initial log height is $\log_2(q(m+1))\le\varepsilon p+O(\log p)$, and at most $(j+1)\log_2(q+1)$ is lost at its selected dates. At a consecutive-interval row, at most $2\log_2(q+1)$ is lost: one cost at the selected terminal step, and the initial shift from $y$ to $y+q\le(1+q)y$. The terminal unshifted height is always bounded by the shifted one. As before each list separately charges its own distinct dates. A cut at the minimum is at time 1.

For the initial bound, the classical minimum estimate gives $m\ll h^{14.3}$. Crude bounds suffice to avoid circularity. Since $m\ge1/q$, the complete lap correction is at most $p\log_2(1+q/3)$, so $h=O(p(1+\log q))=O(p^2)$. Thus $\log_2(m+1)=O(\log p)$. Along the actual lap $\log_2(y_j+q)\le \beta p+\log_2(q(m+1))$. All $U_i,V_i,u_i,v_i$ are consequently in the unit cube for large $p$, since $e_j\le\log_2(3y_j+q)$ and $\beta+\varepsilon<1$. At an arc start the difference of the two distinct numerators is a nonzero multiple of $2^{p A_i}$, by the exact common-prefix and smaller-final-exponent relation. Hence
\[
         l_i\le A_i\le \max(U_{i-1},V_{i-1})\le1.
\]
Since $s$ is bounded, summing the true $p(A_i+u_i)$ also gives the sharper $h=O_s(p)$. In particular every fixed-length Evertse chain error $o(h)$ is $o(p)$. [Minimum and physical root](ALL_SHIFT_HEIGHTS.md) · [Native mismatch quotients](NEAR_CIRCUIT_FIVE.md)

## The higher start pays a bounded total correction

Let a common arc have $L=pl_i$ odd steps, common division sum $A=pA_i$ including the smaller final exponent, and actual higher starting numerator $Y$. Its division excess at the final step is $d$. The exact common carry $C$ only involves exponents **strictly before** that step. If $F_j$ is the sum of the first $j$ exponents, $0\le j<L$, then $F_j<A$ and
\[
  2^{A+d}Y_{\rm end}=3^L Y+qC,\qquad
   \frac{C}{3^LY}=\sum_{j=0}^{L-1}\frac{2^{F_j}}{3^{j+1}Y}
       \le \sum_{j=0}^{L-1}3^{-j-1}<1/2 .
\]
Indeed $Y\ge|Y-Z|\ge2^A$. Therefore the entire unnormalized logarithmic correction on this track is at most $\log_2(1+q/2)$. The other track may have a much larger correction. No upper bound on its correction is needed.

For the two affine expressions
\[
 a_i^L=\gamma l_i+U_{i-1}-U_i-u_i,\qquad
 a_i^R=\gamma l_i+V_{i-1}-V_i-v_i
\]
both $A_i-a_i^L$ and $A_i-a_i^R$ are nonnegative, by the positive carry. On the higher starting side, additionally $a_i^{\rm high}-A_i\ge-\varepsilon-o(1)$. The verifier uses a branch for this higher side only when its certificate needs one. The order row and $\text{higher height}-A_i$ in that branch are nonnegative. Without branching the weaker separation row $U_{i-1}+V_{i-1}-B_{i-1}-A_i$ holds exactly.

## Consecutive arc certificates

Retain all time, low-height and terminal-cost rows from [the chronological proof](SIX_ROTATIONS.md) as well as its chain inequality for every consecutive chain (including singletons). In each chain row use the **actual** normalized $A_{b+1}$, justified by the native theorem itself. The resulting rows in the $8s+1$ cube coordinates are affine at any fixed value of $\gamma$, and affine in $\gamma$ at each fixed point. For all true candidates they are at least $-7\varepsilon-o(1)$, including every charged prefix.

The verifier splits into higher-side alternatives only where the branch-free rows do not suffice. Among the 25 pairs $(s,w)$, 23 require no split; the two pairs $(6,2)$ and $(6,3)$ each use three leaves. Give each prefix row at index $j$ its error cost $j+2$, each consecutive step row cost two, each high-start upper clock cost one, and all other rows cost zero. Adding $\varepsilon$ times the corresponding cost to each affine row leaves every true row at least $-o(1)$.

At each of the 29 leaves an exact positive integer combination of these **error-adjusted** rows has strictly negative supremum on the entire unit cube at both rational endpoints bracketing $\gamma$. Interpolation in the slope preserves the upper bound. For example the tightest ratio of the magnitude of an unadjusted cap to its error weight is $761279/2992487400>1/4096$. This contradicts every unbounded sequence violating (1). The rational computation uses fixed exact matrices and multipliers, with both children checked at each internal node. The Diophantine chain inequality and the logarithmic minimum estimate are the external written inputs. [Evertse, Theorem 2, p. 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf) · [Exact verifier](check_rotation_denominators.py) · [Tree and multipliers](rotation_denominator_duals.json) · [Exact output](../../../reports/astra-infinite-descent-20261127/cycles/ROTATION_DENOMINATORS.json)

## Positive rate in the full shortcut period

Along any such family with $h\to\infty$, including families with $h/p$ unbounded,
\[
    \liminf \frac{\log_2q}{h}\ \ge\
       \frac1{9[1+4096(\log_2 3-1)]}\ >\frac1{21600}.
\]
For this corollary only, write $A_i^{\rm int}=pA_i$ and $D_i=p(u_i+v_i)$. Set $F=\log_2q+\log_2(m+1)+\beta p$; this bounds every unshifted numerator logarithm by the elementary shifted growth inequality. Hence $A_i^{\rm int}\le F$ and $D_i\le F+\gamma$ by $e_j\le\log_2(3y_j+q)$. Both aligned tracks traverse one complete lap, so $h=\sum A_i^{\rm int}+\tfrac12\sum D_i$. It follows that $h\le(3s/2)F+s\gamma/2$. When $p\to\infty$, inequality (1) gives $p<4096\log_2q$; when $p$ stays bounded its term in $F$ is bounded. Use $s\le6$ and $\log_2(m+1)=O(\log h)$ in both cases. Any sequence has the required bounded or diverging $p$ subsequence after passing to a lower-limit subsequence.

[Exact native control](check_rotation_charge.py) verifies 22,850 higher-side carry bounds and 45,700 charged prefixes in 2,033 primitive positive rational cycles. It includes 4,595 rotations with $\Lambda>1$ and 5,115 whose minimum lies at a selected cut. Three cases violate the proposed higher-side carry bound at the **lower** start. [Native control counts](../../../reports/astra-infinite-descent-20261127/cycles/ROTATION_CHARGES.json)

[PhysicalCharges.lean](PhysicalCharges.lean) proves the higher-start carry and both shifted step bounds with integer arithmetic. [DenominatorDuals.lean](DenominatorDuals.lean) checks all 29 error-adjusted endpoint matrices in the Lean kernel, proves that the 25 geometries are covered, and gives an offending row on every sign-tree path and every real interpolated slope and cube point. Its [deterministic exporter](export_denominator_duals.py) uses the full rational row definitions above. The inference from a periodic orbit to all Diophantine chain rows remains the written Evertse argument.
