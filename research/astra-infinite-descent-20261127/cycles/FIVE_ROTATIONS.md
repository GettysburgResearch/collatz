# Finiteness of five odd-valuation mismatches at arbitrary rotation order

The [full denominator theorem](ROTATION_DENOMINATORS.md) strengthens the rational estimate below to $q>2^{p/4096}$ through six mismatches using the actual common block clocks.

Let a primitive positive rational Collatz cycle have $p$ odd steps, $h$ shortcut steps, full reduced denominator $q$, actual odd division exponents $e_j$, and $\Lambda=h-p\log_2 3$. If some proper rotation of $(e_j)$ differs in at most five positions, then for all sufficiently large $p$,
\[
             \boxed{\max\{\log_2q,\Lambda\}>p/4096,\qquad q>p/65536.}     \tag{1}
\]
In particular, only finitely many primitive positive **integer** cycles can have a proper odd rotation with at most five mismatches. The onset is ineffective. No assumption on the rotation order, the sizes of the individual valuations, the overall physical spread or the concentration of the excess divisions is needed.

Armstrong's project proved the previous finite-exception result for four mismatches under its stated inputs, and identified five mismatches at arbitrary order as open. Its fixed-order and near-circuit computations for five were explicitly heuristic. The new reduction uses the already derived three/four-term local Diophantine inequality and keeps growth estimates for two chronological lists separately. In particular it requires no enumeration of possible rotation orders, marker ranks or interleavings between the lists. The lower bound tending to infinity with period that Armstrong asks for remains open, as does general cycle exclusion. [Prior arbitrary-order question and results](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-finite-exceptions.md) · [Prior five-mismatch experiments](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/results/few-mismatch-rotation-orders-sweep/README.md)

## Two lists of post-mismatch states

Suppose contrary to (1) that $p\to\infty$, $\log_2 q\le\eta p$ and $\Lambda\le\eta p$ with $\eta=1/4096$. Then $h=(\gamma+O(\eta))p$, where $\gamma=\log_2 3$, and $\beta=\gamma-1$. Root the chronological odd circle at its actual minimum $m$. Write $y_n=qx_n$ for each positive odd numerator, with period $p$. The initial height satisfies $p^{-1}\log_2 y_0\le\eta+o(1)$ since $m\ll h^{14.3}$. For every contiguous arc of at most one lap,
\[
 \log_2 y_{b}-\log_2 y_a
  =\beta(b-a)-\sum_{a\le j<b}(e_j-1)+C_{a,b},\quad
              0\le C_{a,b}\le\Lambda.                                 \tag{2}
\]
Here indices are unwrapped so $0\le b-a\le p$. Indeed the corrections are $\log_2(1+q/(3y_j))$, positive and summing to $\Lambda$ in one full lap. This identity holds for the rational orbit over its common reduced denominator. [Minimum estimate](ALL_SHIFT_HEIGHTS.md)

Use the shorter of the supplied lag and its inverse, which have equal Hamming distance. Write $r=\ell/p\in(0,1/2]$. Let $s$ be the number of mismatches, so $2\le s\le5$. Zero would contradict primitivity and one is impossible since the two rotated words have the same multiset of letters. List their **post-departure times** on the original track as $0<t_0<\dots<t_{s-1}\le1$ in units of $p$; a mismatch immediately preceding the chosen minimum is recorded at time 1. At original cut $i$ the translated cut is at
\[
 t_i'=t_i+r-\mathbf 1_{t_i+r>1}.
\]
These also lie in $(0,1]$. Equality $t_i+r=1$ stays at 1. If $w$ cuts wrap, their chronological order on the translated list, starting at the same actual minimum, is exactly $s-w,\ldots,s-1,0,\ldots,s-w-1$, including $w=0,s$. Write $l_i=t_i-t_{i-1}$ for the forward cyclic distances, adding one at $i=0$. The normalized height pair $(U_i,V_i)$ is $(\log_2 y_{pt_i},\log_2 y_{pt'_i})/p$.

Let $u_i,v_i$ be the two final letter excesses above their common smaller value, divided by $p$. Exactly one is zero. In particular the normalized absolute mismatch difference is $u_i+v_i$, the original departure's excess over one is at least $pu_i$, and the translated one's excess over one is at least $pv_i$. All these variables, all cut times and the lag lie in $[0,1]$ eventually: each excess is at most $(h-p)/p\le\beta+\eta$, and (2) bounds either height by $\eta+\beta+\eta+o(1)<1$. For each fixed $s$ these are $5s+1$ real variables.

## Finite affine inequalities

Here and below normalized errors refer to an actual candidate; the verifier tests the displayed affine expressions. Define
\[
 a_i=\gamma l_i+U_{i-1}-U_i-u_i .
\]
Between consecutive post-mismatches the two tracks have identical interior valuations. The total divisions in the original arc equal $A_i+pu_i$, and in the translated arc $A_i+pv_i$, where $A_i$ includes the smaller last letter. Both arcs have exactly $pl_i$ odd steps and $A_i\ge pl_i$. By (2), with $c_i,c_i'$ the two normalized arc corrections in $[0,\eta]$,
\[
 A_i/p=a_i+c_i,\qquad
 (v_i-u_i)-[(V_{i-1}-U_{i-1})-(V_i-U_i)]=c_i'-c_i.                   \tag{3}
\]
Thus $a_i-l_i\ge-\eta$, and the absolute value of the second expression is at most $\eta$. This includes the wrap at either track's seam; the lengths of the two actual arcs are equal.

By the [local mismatch inequality, equation (1)](NEAR_CIRCUIT_FIVE.md),
\[
 \gamma l_i+A_{i+1}/p\le U_i+V_i+\min\{u_i+v_i,U_i,V_i\}+o(1).
\]
The uniform $o(h)$ there becomes $o(p)$ here. Since $a_{i+1}\le A_{i+1}/p$, each of the three affine rows
\[
 U_i+V_i-a_{i+1}-\gamma l_i+z,\qquad z\in\{u_i+v_i,U_i,V_i\},        \tag{4}
\]
is at least $-o(1)$. The underlying local proof unrolls the actual common interiors, proves nondegeneracy of the signed tuples, and applies Evertse's fixed-dimensional theorem. [Evertse, Theorem 2, p. 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

For each of the two lists **separately**, read its cuts in increasing physical time $T_j$. Let $H_j$ be its selected normalized height and $d_j$ its selected final normalized excess ($U_i,u_i$ on the first list, $V_i,v_i$ on the other). The following are genuine prefix and consecutive-interval rows:
\[
 \begin{split}
  \beta T_j-\sum_{k\le j}d_k-H_j &\ge-2\eta-o(1),\\
  H_{j-1}+\beta(T_j-T_{j-1})-H_j-d_j&\ge-\eta\quad(j\ge1).
 \end{split}                                                           \tag{5}
\]
For the first row, apply (2) from the actual minimum through $T_j$. Each selected excess occurs at a distinct intervening departure in this one list. For the second use (2) between successive selected cuts; the departing step just before $T_j$ lies in that half-open interval. A possible minimum at time 1 poses no extra cost. Even when two positions from different lists are the identical physical cut, no sum in (5) adds the selections from both lists. The model may forget their equality without invalidating a necessary inequality. Positivity of time gaps, $T_{\rm last}\le1$ and $r\le1/2$ give the remaining geometric rows.

## Eighteen exact certificates

The [verifier](check_five_rotations.py) constructs (3) with both signs and the native lower bound, (4), (5), and those geometric rows directly from $s,w$. It permits both $u_i,v_i$ to be positive in the relaxed cube. Every true pair, for which one vanishes, is still included. It requires neither the true ordering between the two lists nor a choice of which of their state heights is larger.

For every $s=2,3,4,5$ and $w=0,\ldots,s$, a [nonnegative integer dual](five_rotation_duals.json) gives a weighted sum whose greatest value over the full cube, divided by its total weight, is at most
\[
                 -806849/100000100 < -1/128.
\]
For any fixed assignment the sum is affine in $\gamma$. The verifier checks both rational endpoints $15849/10000$ and $15850/10000$ bracketing $\gamma$ by exact powering. At either endpoint the weighted form is affine in the cut variables, and the maximum of $c+\sum a_jx_j$ on the unit cube is $c+\sum\max(0,a_j)$. By (3)–(5) every row in a genuine candidate is at least $-2\eta-o(1)$. Since $2/4096<1/128$, the finite certificate contradicts any growing sequence. The 18 certificates include all six wrap counts for the new case $s=5$. [Archived exact output](../../../reports/astra-infinite-descent-20261127/cycles/FIVE_ROTATIONS.json)

Finally, the odd numerators are pairwise distinct. The sum of their complete positive corrections is at most $p[(1+a)\log_2(1+a)-a\log_2a]$ with $a=q/(3p)$, by integrating the decreasing function $\log_2(1+q/(3x))$ over $0<x<p$. If $q\le p/65536$ then $a<2^{-17}$, hence $\Lambda/p\le20\cdot2^{-17}<1/4096$ by $\ln(1+a)\le a$ and monotonicity of $-a\log_2a$ in this range. Also $\log_2q\le p/4096$ eventually, contradicting the first conclusion. Ordinary cycles of bounded odd period have $h\le2p$ by the positive branch product and therefore form a finite set. This proves (1) and the stated finite-exception result. The proof does not give a bound on the sizes of those exceptions.

The [real cube and weighted-row theorem](CubeDual.lean), [twenty-five two-endpoint matrices](RotationDuals.lean), and [interpolation certificate](RotationInterpolation.lean) compile in Lean 4.34.1; each numerical check uses kernel reduction. The Lean theorem `certified_interior` produces a row below the stated margin at every real interpolation and every real cube point. The [exporter](export_rotation_duals.py) reproduces the named sparse matrices from the rational row definitions, including all six-cut chain rows chosen by the duals. The [native cut replay](check_rotation_cuts.py) verifies 22,850 paired clocks and 45,700 chronological prefix rows in 2,033 primitive positive rational cycles, including 4,592 exact translated seams. [Physical control counts](../../../reports/astra-infinite-descent-20261127/cycles/NATIVE_ROTATION_CUTS.json)
