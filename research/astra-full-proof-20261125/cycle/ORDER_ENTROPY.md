# Two actual rank orders permit more than one third of a ternary digit per odd step

**PROPOSED written obstruction to an order-only entropy proof.** There are positive rational cycles with the two actual rank orders, odd valuations one and two, and maximum odd height below $3.3s$. At the same upper-convergent pair $(p,h)$, the family realizes $\exp((c+o(1))p)$ distinct physical odd-gap words based at the minimum, where
$$
 \delta_0=\log_2(3/2),\quad
 c=(1-\delta_0)\ln2+(2\delta_0-1)\ln(3/2)+\tfrac3{25}\ln(4/3)
   >\tfrac13\ln3.
$$
They can simultaneously have more than $p/50$ odd heights above $3s$, more than $p/83$ band mismatches at every nonzero rank shift, and reduced denominator greater than $\exp(p/10)$. The size estimate $s\ll p^6$ does hold; polynomial height for the *integer numerators* does not. This distinguishes an upper count using the two geometric orders from one using the ordinary integer lattice.

## Four-site count

Take any sufficiently large reduced upper convergent $h/p$ of $\log_23$. Put $\delta=(h-p)/p$, $\lambda=1-\delta$, and use ranks normalized to $u=r/p\in[0,1)$. The time advance is $R(u)=u+\delta\bmod1$. Put $b_r=\lfloor(r+h)/p\rfloor$. A binary assignment $j_r\in\{0,1\}$ gives physical gaps $a_r=b_r+j_r-j_{Rr}$. On a nonwrapping edge $b=1$ and $j_{Rr}\le j_r$ is required. On a wrapping edge $b=2$ and $j_{Rr}\ge j_r$ is required. Take the following open intervals of ranks:
$$
 F=(0,\lambda),\qquad I=(\lambda,\delta),\qquad J=(3/5,18/25).
$$
Every rank outside their union gets zero. A rank in $F$ has a wrapping incoming edge and a nonwrapping outgoing edge, so it may be elevated when all other ranks are zero. Each $i\in I$ has a wrapping incoming edge and a wrapping outgoing edge to $i-\lambda\in F$. Give the pair $(j_i,j_{i-\lambda})$ any of the three assignments with $j_i\le j_{i-\lambda}$. These pairs are disjoint.

For each $v\in J$, write $P=v-\delta,\ N=v-\lambda,\ S=P+\lambda$. Then $P\in(0,2\delta-1)$ is already paired with $S\in I$, and $N\in(2\delta-1,\lambda)$ is a free singleton of $F$. This follows from $0.58<\delta<0.59$ for large convergents (all limiting interval endpoints are strictly separated). The incoming edge $P\to v$ is nonwrapping and $v\to N$ wraps. In each resulting four-site block the complete set of constraints is
$$
                          j_S\le j_P,\qquad j_v\le j_P,\qquad j_v\le j_N.
$$
The four-site blocks are disjoint since the four rank intervals are pairwise disjoint and all the maps on them are translations. With $j_v=0$ a block has six choices. With $j_v=1$ it has two. This accounts for every edge constraint: an elevated target reached by a nonwrapping edge must lie in $J$, and an elevated source on a wrapping edge belongs to $I$ or $J$. Endpoints outside the open intervals remain zero.

Thus the number of assignments is exactly $2^{|F|}(3/2)^{|I|}(4/3)^{|J|}$, with cardinalities counting integer ranks in the open intervals. Its natural logarithm divided by $p$ tends to $c$. For an exact lower comparison,
$$
 c>.41\ln2+.16\ln(3/2)+.12\ln(4/3)>\tfrac13\ln3.
$$
The first inequality follows from $2^{158}<3^{100}<2^{159}$. The second is $2^{147}>3^{88}$ after clearing denominators. This is a count of complete, compatible assignments for each supplied slope. Different assignments give different physical words at rank zero since $j_0=0$ and $j_{Rr}=b_r+j_r-a_r$ recovers them along the single rank orbit.

## Ordinary sizes of the rational phases and both orderings

Use independently uniform choices in each block of size four, two or one. We verify that the conditions needed in the existing two-order realization proof persist. For each assignment, the periodic positive solution of
$$
 2^{b_r}t_{Rr}=3t_r+2^{-j_r},\qquad x_r=2^{j_r}t_r
$$
exists because its lap slope is $3^p/2^h<1$. Thus $2^{a_r}x_{Rr}=3x_r+1$. The fixed-point carry at each rotation is odd and nonzero modulo three, giving actual odd rational phases with exact valuations. Coprimality of $h,p$ makes the physical word primitive. [Positive rational realization at the parent revision](../../astra-ultra-closure-20261125/cycle/RATIONAL_ORDERS.md)

As there, set $v_r=2^{-r/p}t_r,\ \rho=3\,2^{-h/p},\ B_r=2^{-(r+h)/p-j_r}$. Then $v_{Rr}=\rho v_r+B_r$. Put $\bar B=p^{-1}\sum B_r$, $V=\bar B/(1-\rho)$. Since $h/p$ is an upper convergent and $\bar B$ is bounded above and below by positive constants, $V\gg p^2$. The supremum of the absolute values of cyclic partial sums of $B_r-\bar B$ in time order is $o(p)$ with probability tending to one, for the following two reasons.

* The mean of $2^{-j_r}$ is constant on each rank role (including the four positions of a block, the residual pair roles, ordinary singletons and fixed zero). Each role is a union of boundedly many intervals given explicitly by $F,I,J$ and their translates. Their endpoints differ from the fixed limiting endpoints by $O(p^{-2})$ before rank rounding. The means are therefore samples of a fixed bounded piecewise smooth function of $r/p$, times $2^{-h/p}$, except at $O(1)$ ranks. Upper and lower continuous trigonometric approximations after smoothing the finitely many jumps give uniform $o(p)$ discrepancy over segments, since for each fixed nonzero frequency $n$ the geometric sums are bounded by $2/|1-\exp(2\pi i n\delta)|=O_n(1)$. Use the limiting irrational $\delta_0$ and then let the smoothing error tend to zero.
* Each block is an independent draw affecting at most four terms of any prefix sum; each affected term varies by at most one. The bounded-differences estimate bounds deviation from the individual prefix mean by $p^{3/4}$ with failure probability at most $2\exp(-c_1\sqrt p)$, for an absolute $c_1>0$. A union bound over the $p$ prefixes also controls all cyclic segments and the observed mean. The estimate follows by exposing each block in turn and applying the exponential moment bound $\mathbb E e^{t(Z-\mathbb EZ)}\le e^{t^2(b-a)^2/8}$ for a variable in $[a,b]$ to the increments of the conditional-mean martingale.

Solving backward and summing by parts now gives $v_r=V+o(p)$ uniformly. Indeed the centered forcing has uniformly $o(p)$ partial sums even over repeated laps, and the summation-by-parts coefficients are nonnegative and sum to one. Thus $t_r=2^{r/p}(V+o(p))$. The nominal spacing of consecutive mantissas, including the upper virtual seam, is $\gg p$. They are strictly ordered and $s=t_0$. The true dyadic octaves are exactly $j_r$. With the largest elevated rank below $.72p$, all odd heights are less than $2^{1.72}(1+o(1))s<3.3s$.

To verify the physical ternary order, label each odd state $L=r+p j_r$, and each intervening even state by the label of its odd successor plus $p$. At an odd shortcut step the label adds $h-p$, and at an even step it subtracts $p$. Its residues modulo $h$ are all distinct since $\gcd(h,p)=1$. Each value is $2^{L/p}(V+o(p))$, with $0\le L<2.72p<2h$. Write $L=\sigma+\ell h$, $0\le\sigma<h$, $\ell\in\{0,1\}$. After division by $3^\ell$, the physical value is $2^{\sigma/p}(V+o(p))$, since $(2^{h/p}/3-1)V=\bar B/\rho=O(1)$. At $\sigma=0$ the state is $s$; the virtual upper endpoint $3s$ has the same asymptotic expression at $\sigma=h$. Again nominal spacings $\gg p$ imply strict ordering in $\sigma$ and show that these are the actual ternary mantissas.

## Simultaneous tests and physical window complexity

At every $v\in J$, two of its eight block assignments elevate $v$. Different four-site blocks are independent, so with probability tending to one more than $p/50$ ranks there are elevated. Each such height exceeds $3s$ since $2^{1.6}>3$. There are $(\lambda-(2\delta-1)-.12+o(1))p>.10p$ remaining fair *singleton* source bits. For any fixed nonzero shift the target of such a bit is in a different independent block and the mismatch probability is $1/2$. Changing a block changes at most eight comparisons for that shift. The same concentration bound, followed by a union over $p-1$ shifts, proves $E_t>p/83$ at every nonzero shift with probability tending to one. These are the physical unlifted bands in their actual sorted dyadic order.

The options at a fixed slope are equiprobable, so retaining an event with probability tending to one preserves the exponential count $\exp((c+o(1))p)$. Distinct assignments satisfying the order property give distinct minima: a rational minimum determines the physical forward orbit and the sorted bands then recover the assignment. Its full-lap product bound and Wu–Wang give $s=O(p^6)$. Thus the number of minima with reduced denominator at most $\exp(p/10)$ is $O(p^6\exp(p/5))$, negligible at rate $c$. All stated properties can be imposed simultaneously.

For $k\to\infty$ with $k=o(p)$, let $W_p(k)$ be the union of all physical $k$-gap windows from the retained cycles with that common $(p,h)$. Cutting their different $p$-gap words into consecutive $k$-blocks and one remainder gives
$$
 \exp((c+o(1))p)\ \le\ |W_p(k)|^{\lfloor p/k\rfloor}2^k.
$$
Therefore $\liminf \ln|W_p(k)|/k\ge c>\ln3/3$. A fixed finite partition into initial log-height bins leaves the maximal bin's exponential rate unchanged. The count is over windows in a family of actual cycles; it does not claim an individual cycle has this many distinct windows. It excludes a uniform low-entropy cover based only on their two orders, the valuation alphabet, the numerical width ceiling and the stated occupation and mismatch tests. All cycles retained here have exponentially large reduced denominator, and no least-disagreement predecessor-basin condition was imposed. In particular the lower bound does not exclude a narrower cover proved using $d=1$, small numerator height, or the least-source arithmetic. The earlier ordinary $p\ll s^{.479}$ constraint has not been imposed on this family. [Finite local edge checks](check.py)

Polynomially many *whole* words would still leave an unresolved quantifier at the required window length. For example, take just one binary de Bruijn cycle at each period $p=2^n$. It has $p$ distinct windows of every length $k\ge n$, because the initial $n$ bits distinguish all cyclic positions. Such a cycle comes from an Euler circuit on $(n-1)$-bit strings with one edge for each $n$-bit string: the graph is connected and each vertex has indegree and outdegree two. At $k=\lceil3\ln p/\ln3\rceil$ its window rate tends to $\ln3/3$ despite there being only one full word per period. This is a combinatorial example of the inference error. The missing small-denominator estimate must constrain windows within physical laps, not only the total number of candidate laps of each period.
