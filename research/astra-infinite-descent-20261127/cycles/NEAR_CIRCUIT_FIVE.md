# A positive density of excess divisions or an exponential denominator at five odd-rotation mismatches

Let a primitive positive rational shortcut cycle have $p$ odd departures, with odd division exponents $e_i\ge1$, shortcut period $h=\sum e_i$, and complete reduced denominator $q$. Fix $\varepsilon=1/4096$. For all sufficiently large $p$, the following two properties imply $\log_2 q>\varepsilon p$:

* For some departure $j$, $\sum_{i\ne j}(e_i-1)\le\varepsilon p$.
* Some nonidentity rotation of the odd word $(e_i)$ has at most five unequal positions.

In particular, among ordinary positive integer cycles with at most five mismatches at a proper odd rotation, every sufficiently long one has more than $p/4096$ excess divisions outside **each** specified departure. The number of nontrivial ordinary cycles violating this condition is finite; the onset is ineffective. The result permits arbitrarily many smaller nonunit exponents and arbitrary rotation order. The later [arbitrary-clock denominator theorem](ROTATION_DENOMINATORS.md) removes the excess hypothesis through six mismatches.

Armstrong's project proposed the ordinary near-circuit restriction and supplied a floating-point model, the two local expansion identities in the half-period case, and the Evertse normalization. The argument below uses one inequality for each mismatch, ten small exact certificates, and an explicit allowance for a moving rational denominator. The general at-most-four ordinary finiteness and half-period six-mismatch finiteness are prior work. [Proposed near-circuit argument](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/results/near-circuit-rotation-forced-relation/README.md) · [Prior Evertse normalization](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/results/half-period-six-mismatch-finiteness.md) · [Prior finite-exception frontier](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-finite-exceptions.md)

## A local inequality for every rational cycle and every mismatch

Write $y_i=q x_i$ for the positive odd integer numerators, so $2^{e_i}y_{i+1}=3y_i+q$. Both $q$ and every $y_i$ are coprime to three, since $q\mid 2^h-3^p$ and every $y_i$ has an incoming odd step. Let $\gamma=\log_2 3$. Compare the odd trace to its proper rotation. Index its mismatches cyclically by $k$. A block ends with the mismatched step, contains all the matched steps since the last mismatch, and has odd length $L_k\ge1$. Put $A_k$ equal to the division sum on its common interior plus the **smaller** final division count. At the end let $y,z$ be the two states *after* the mismatch, and let the final divisions exceed their minimum by $u,v$, respectively. One of $u,v$ equals zero, and $D_k=|u-v|\ge1$. We have
\[
 \gamma L_k+A_{k+1}
 \le \log_2 y+\log_2 z+\min\{D_k,\log_2\min(y,z)\}+o(h) .            \tag{1}
\]
The error is uniform over the actual rational cycles, proper shifts and selected mismatches as $h\to\infty$. It uses Evertse's fixed three- and four-term inequalities. Separately, $A_{k+1}<\log_2\max(y,z)$ by elementary nonzero spacing. No near-circuit hypothesis enters these local bounds.

Let $a,b$ be the two starting numerators of block $k$. Subtract and unroll the common interior and then the mismatched final step to get
\[
 3^{L_k}(b-a)=2^{A_k}(2^v z-2^u y).
\]
The reduced bracket is odd. Since two and three are coprime and $a,b$ are distinct by primitivity, $b-a=2^{A_k}g_k$ for a nonzero odd integer $g_k$ and $3^{L_k}g_k=2^v z-2^u y$. At the next block $z-y=2^{A_{k+1}}g_{k+1}$. For either choice $w\in\{y,z\}$ this gives
\[
               3^{L_k}g_k=2^c g_{k+1}+(2^v-2^u)w,                     \tag{2}
\]
where $c=v+A_{k+1}$ for $w=y$ and $c=u+A_{k+1}$ for $w=z$.

Apply Evertse's Corollary 1, inequality (12), at primes two and three: for each $\delta>0$ the product of the parts coprime to six of a primitive nondegenerate vanishing tuple of three or four nonzero integers is at least $c_\delta H^{1-\delta}$, where $H$ is its largest absolute entry. The positive constant absorbs the finitely many exceptions. [Evertse (1984), Corollary 1, pp. 227–228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

In (2) the three signed nonzero summands form such a nondegenerate tuple after division by their common gcd $d_0$: no proper two-term sum can vanish. The gcd is odd since $(2^v-2^u)w$ is odd. Its power of three is at most $3D_k$, because $3\nmid w$ and $v_3(2^{D_k}-1)$ is zero for odd $D_k$ and $1+v_3(D_k)$ for even $D_k$. Write $d_0=3^a d'$ with $d'$ coprime to six. Before normalization the product of the three prime-free parts is at most $|g_k g_{k+1}|(2^{D_k}-1)w$. Dividing the entries by $d_0$ divides this product by exactly $(d')^3$. Consequently its unnormalized upper bound is at least $c_\delta H_{\rm raw}^{1-\delta}/(3D_k)$, using $(d')^3/d_0^{1-\delta}\ge1/(3D_k)$.

Split $(2^v-2^u)w$ into its two signed terms for the four-term alternative. Those terms do not cancel each other, and the two complementary terms then cannot cancel either. The term divisible by $3^{L_k}$ cannot cancel either power of two times $w$ since $3\nmid w$. These exhaust the possible pairs, and a singleton or a triple cannot vanish. The four-term gcd divides $w$ and is coprime to six. The unnormalized product is at most $|g_k g_{k+1}|w^2$ and at least $c_\delta H_{\rm raw}^{1-\delta}$ by the same normalization.

There is a direct alternative using Evertse's Theorem 2, p. 228. For the signed integer vector of right-hand terms $V$ in (2), compact or split, every nonempty subsum is nonzero by the same checks. At $S=\{\infty,2,3\}$ and $T=\{3\}$ the theorem gives
\[
 \left(\prod_i [V_i]\right)\left|\sum_i V_i\right|_3
       \ge c_{n,\delta}\max_i |V_i|_3\,\|V\|_\infty^{-\delta},
\]
where $[v]=|v|\,|v|_2|v|_3$. Here the sum has ternary absolute value at most $3^{-L_k}$. The maximum on the right is at least $1/(3D_k)$ for the compact correction and is one after splitting it. The same bound on $\log_2|g_{k+1}|+\log_2 w+\min(D_k,\log_2w)$ follows directly, without a gcd normalization. This is also the formulation used in the consecutive-mismatch extension. [Evertse, Theorem 2](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

In either tuple $H_{\rm raw}\ge3^{L_k}|g_k|$ and $\log_2 H_{\rm raw}=O(h)$ uniformly: $q\le 2^h$, the rational minimum $m\ll h^{14.3}$, and each odd step takes $q(x+1)$ to at most $(3/2)q(x+1)$. All displayed exponents are at most $2h$ and $D_k\le h$. Divide each product bound by $|g_k|$. Taking logarithms, then arbitrary fixed $\delta>0$, gives
\[
 \gamma L_k\le \log_2|g_{k+1}|+\log_2 w+\min(D_k,\log_2 w)+o(h)
\]
uniformly. Choose the smaller of $y,z$ and use $\log_2 |g_{k+1}|<\log_2\max(y,z)-A_{k+1}$. This proves (1) and also explains the elementary spacing bound. [Minimum estimate and denominator normalization](ALL_SHIFT_HEIGHTS.md)

## Heights away from the exceptional departure

Suppose, towards contradiction, that $p\to\infty$, $q\le2^{\varepsilon p}$, and the total excess outside the chosen departure is $B\le\varepsilon p$. Root the circle immediately after that departure, with positive numerator $y_0$, followed by $p-1$ ordinary departures then the designated one. Set $\beta=\gamma-1$. At any phase $y_i\le q(m+1)(3/2)^p$. The designated exponent $e_*$ satisfies $2^{e_*}\le 3y_{p-1}+q$, hence
\[
 h=p-1+B+e_*\le (1+\beta+2\varepsilon)p+O(\log(2h)).
\]
Thus $h=O(p)$ and the minimum bound gives $\log_2(m+1)=O(\log(2p))$. Before the exceptional step, unrolling the positive homogeneous part gives $y_i\ge 2^{\beta i-B}y_0$. Apply this at the globally least odd numerator to obtain $y_0\le 2^B qm$. The forward upper bound $y_i+q\le(3/2)^i(y_0+q)$ now yields **uniformly** for $0\le i<p$
\[
       \beta i-\varepsilon p
          \le \log_2 y_i\le \beta i+2\varepsilon p+O(\log(2p)).        \tag{3}
\]
At the last departure $2^{e_*}y_0=3y_{p-1}+q$. In particular $e_*/p\ge\beta-3\varepsilon-o(1)$, while every other exponent is at most $1+\varepsilon p$. The designated exponent is uniquely largest for all sufficiently large $p$. Its two comparisons in a proper rotation are therefore genuine mismatches. The smaller post-mismatch numerator at each of those comparisons is at most $y_0\le2^{2\varepsilon p+O(\log(2p))}$. At every remaining mismatch the exponent difference is at most $B$. Thus the extra minimum term in (1) costs at most $2\varepsilon p+O(\log(2p))$ at any mismatch.

## The exact finite contradiction

Replace the shift by its inverse if needed, so its normalized representative is $0<r\le1/2$. Let $s$ be the Hamming distance. Primitivity and equal multisets give $2\le s\le5$. Regard each cut as the normalized post-mismatch time in $(0,1]$, representing the unshifted exceptional return by 1. Its paired return is $1-r$. The other $s-2$ cuts are ordinary times. Put them in increasing order $t_i$ together with $1-r$ and $1$. Let $l_i$ be the gap from the previous cut to this cut, using zero as the previous cut for the first one; $l_i=L_i/p$. Write $z_i=\beta(t_i\bmod1)$ and $z'_i=\beta((t_i+r)\bmod1)$. These heights concern the proposed piecewise-linear profile, including its exact post-return zero. By (3), the true normalized logarithms are bounded above by these values plus $2\varepsilon+o(1)$. Also $A_{i+1}\ge L_{i+1}$ for all $i$.

Equations (1) and (3) then force the following rows at every cut:
\[
 \max(z_i,z'_i)-l_{i+1}\ge-2\varepsilon-o(1),\qquad
 z_i+z'_i-l_{i+1}-\gamma l_i\ge-6\varepsilon-o(1).                    \tag{4}
\]
The bound uses only an upper estimate for a paired difference. It also applies when the two limiting logarithmic heights tie. For all sufficiently large $p$, each right-hand error in (4) is less than $1/32$.

Fix the number $j$, $0\le j\le s-2$, of ordinary cuts before $1-r$. On that order type the $z_i,z'_i$ and their maximum have the fixed affine expressions in the verifier: below $1-r$ the rotated height is the larger one, above it the original height is larger. At $1-r$ the rotated state returns to zero; at 1 the original state returns to zero. There are ten order types in total. For each one, the [exact verifier](check_near_circuit.py) takes nonnegative integer weights for the rows in (4), with $1/32$ already added, and for the valid geometric rows. At $15849/10000$ and $15850/10000$, which bracket $\gamma$ by exact powering, each resulting weighted affine form has strictly negative maximum over the full unit cube of lag and ordinary times. For an affine form $c+\sum a_i x_i$ this maximum is $c+\sum\max(0,a_i)$. With the variables fixed, each weighted form is affine in $\gamma$, so the endpoint bounds certify the true slope. The weakest upper bound divided by the sum of weights is less than $-1/20$. Thus the proposed rows cannot all hold. This contradiction proves the theorem with the stated $1/4096$ allowances. Only the onset from the fixed-dimensional Diophantine inequality is ineffective.


[Ten exact dual certificates](near_circuit_duals.json) · [Archived rational maxima](../../../reports/astra-infinite-descent-20261127/cycles/NEAR_CIRCUIT_FIVE.json) · [Consecutive-mismatch extension through eight](MISMATCH_CHAINS.md)
