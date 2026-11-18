# One finite array separates escape from additional positive cycles

**Proposed, source-qualified.** For each $Q\ge1$ enumerate the reverse words $w=(a_1,\ldots,a_Q)$ with $1\le a_i\le2Q$. Their slope is $J_w=3^Q 2^{-\sum a_i}$. Their affine map from an odd start $x$ to its endpoint is $t=J_wx+F_w$. There is exactly one legal odd representative $t=t_w$ in $(0,2\cdot3^Q]$ for each word. For rational $0<\theta<1$, compute the nonnegative rational number
$$
 D_Q(\theta)=\sum_{w:\ t_w>1,\ F_w/t_w\ge\theta}\frac{J_w}{t_w}.
$$
There is no cycle detection in this prescription. The full positive-integer Collatz conjecture is equivalent to the conjunction of two limits of this same array:

1. For every integer $k\ge2$, $\liminf_{Q\to\infty} D_Q(1/k)/Q=0$.
2. For at least one integer $k\ge2$, $\liminf_{Q\to\infty} D_Q(1-1/k)=0$.

The first condition holds precisely when every positive orbit is eventually periodic. The second holds precisely when the only positive odd cycle is $\{1\}$, including in the presence of escaping orbits. No estimate here proves either required vanishing. The two normalizations and different threshold quantifiers are essential to this argument.

## Comparing the finite array with the full inverse sum

Let $S_Q(\theta)$ be the same sum without the upper cutoff on the exponents, still omitting $t=1$. Under independent geometric exponents with probabilities $2^{-a}$, the weight of a word is $J_w/3^Q$. The union bound over its $Q$ letters gives
$$
 0\le S_Q(\theta)-D_Q(\theta)\le Q3^Q2^{-2Q}=Q(3/4)^Q ,
$$
uniformly in the threshold. At a positive representative each compatible inverse letter gives a positive odd parent, so the sum observes true ordinary paths. The omitted target $1$ has uniformly bounded raw weight by the fixed-root bound for $g_Q(1)$. Condition 1 now follows from the [raw ordinary cone criterion](TRIADIC_OFFSET.md) at phase zero, using monotonicity in $\theta$.

## What the upper endpoint measures

There exists an absolute $c_0\in(0,1)$ such that every path whose odd input states are pairwise distinct has reciprocal distortion at least $c_0$. This includes a first-hit segment and one complete traversal of a primitive cycle: the ending vertex is not one of the inputs on that traversal for a second time. The bound follows from uniform reciprocal summability on simple orbit segments and cycles. Write $p_C$ for the density of the basin of a cycle $C$, $d_C$ for its odd period, and $J_C$ for its lap multiplier. Then $c_0\le J_C<1$. At any $0<\epsilon<c_0$,
$$
 c\sum_{C\ne\{1\}}\frac{d_C p_C}{1-J_C}
 \ \le\ \liminf_Q\frac{D_Q(1-\epsilon)}{\epsilon}
 \ \le\ \limsup_Q\frac{D_Q(1-\epsilon)}{\epsilon}
 \ \le\ C'\sum_{C\ne\{1\}}\frac{d_C p_C}{1-J_C}.
 \tag{1}
$$
The constants are absolute and an infinite sum is allowed. The fact that a fixed periodic fibre has mass of order $\epsilon$ at this endpoint was already proved in paper 19. Formula (1) sums the contributions of *all* cycle vertices with their basin weights and suppresses the known fixed point by its target label. [Prior periodic real-fibre endpoint law](https://rstation.ai/problems/collatz/papers/19/v2) · [Reciprocal sum and scope of packing estimates](PRIOR_WORK.md)

For the proof, $1-F_w/t_w$ is the reciprocal distortion. If it is less than $c_0$, the path has repeated a state and its target belongs to a cycle. Fix $t$ on such a cycle $C$. Every word ending there consists of a first hit at $t$ followed by a number of whole laps. Let $g^*_q(t)$ be the first-hit slope total and $g_q(t)$ the unrestricted one. The [ordinary first-hit and all-depth estimates](../unsafe-return-weights/INVERSE_AGE_LAWS.md) give
$$
 g^*_q(t)/t\le A p_C,\qquad
 \lim_q g_q(t)/t\asymp \frac{p_C}{1-J_C},
$$
with absolute comparison constants. If a marked path has $j$ trailing laps, its initial first-hit distortion is at least $c_0$, hence $J_C^j\le\epsilon/c_0$. Summing $J_C^j g^*_{Q-jd_C}(t)/t$ from this threshold upward bounds the marked contribution by $A p_C\epsilon/[c_0(1-J_C)]$. Summing over vertices and cycles proves the upper bound.

For the lower bound take the first $j$ with $J_C^j\le\epsilon$. Then $J_C^j>c_0\epsilon$. Every word ending in those $j$ laps qualifies, and for large $Q$ its total at $t$ is $J_C^j g_{Q-jd_C}(t)/t$. Each fixed $t$ belongs to the sampled period eventually. Pass to the lower limit for any finite set of cycles and then take the supremum, proving (1).

Finally let $m_C$ be the cycle minimum. The first-landing lower bound gives $p_C\gg1/m_C$, while
$$
 1-J_C\le\sum_{u\in C}(3u+1)^{-1}\le d_C/(3m_C).
$$
Consequently each cycle contributes at least an absolute positive constant to the sum in (1). Infinitely many cycles force $D_Q(1-\epsilon)\to\infty$ at every sufficiently small fixed $\epsilon>0$. If any nontrivial cycle exists, the lower-bound lap argument gives strictly positive lower limit for **every** $0<\epsilon<1$. If there is none, $D_Q(1-\epsilon)$ is identically zero at every depth as soon as $\epsilon<c_0$. This proves condition 2 and the claimed equivalence.
