# Polynomially many odd tripling failures in every fixed-ratio window

**PROPOSED.** Use the ordinary positive shortcut map. There is an absolute $C>1$ with the following property. Fix any two distinct merger components $A$ and $B$. For every sufficiently large $R$ and **every** partition of the components separating $A$ from $B$, at least $c_{A,B} R^{0.164}$ odd $y$ in $(R,CR]$ have $y$ and $3y$ on opposite sides. In particular, a Collatz counterexample forces this many permanent failures in each such interval. The constant $C$ in the proof can be large. The earlier factor 27 remains the narrower interval in which a single failure is guaranteed. [Factor-27 theorem](THREE_RAY_WINDOWS.md)

The dependence on the partition matters. Build the finite undirected multigraph of true components with an edge for each odd $y\in(R,CR]$ between the components of $y$ and $3y$, and include $A$ and $B$ as vertices. Every cut separating $A$ and $B$ extends to a partition as above. By the undirected integral max-flow/min-cut theorem, this graph contains at least $c_{A,B}R^{0.164}$ edge-disjoint paths from $A$ to $B$. The paths may share vertices. Each edge counts an actual comparison at a distinct odd parameter.

## A localized comparison on either side of a multiple of 16

Let $f$ be any ordinary step-invariant label and put $g(t)=f(t-1)$, $J(t)=f(t+1)$. Call an odd $d$ a failure when $f(d)\ne f(3d)$. For any fixed $b>1$, the number of multiples $t_0$ of 16 in $[R,bR]$ with $g(t_0)\ne J(t_0)$ is bounded by $O_b(\log(2R))$ times the number of failures in $[aR,AR]$, for fixed $0<a<A$ depending only on $b$.

We transport both labels $(g(t),J(t))$ together. The ordinary identities give $g(2u)=g(3u)$ and $J(4u)=J(3u)$. The comparison $g(4u)=g(8u)$ holds if $8u-1$ passes the tripling test, and $J(16u)=J(32u)$ holds if $16u+1$ passes. These follow respectively from the ordinary trajectories of $3(8u-1)$ and $3(16u+1)$. [Exact trajectories](TRIPLING_VARIATION.md#two-comparisons-with-a-neighbor-of-a-multiple)

* For $32\mid t$, both labels can move from $t$ to $t/2$, testing $t-1$ and $t/2+1$.
* For $64\mid t$, both labels can move from $t$ to $3t/2$, testing $3t/4+1$. Indeed the minus label moves directly; for the plus label first use $J(t)=J(3t/4)$, then double its argument.
* Either comparison can be traversed in reverse, with the same tests.

While $v_2(t)>5$, choose the halving move if $t>t_0$ and the $3/2$ move otherwise. Each move removes one factor of two, and $t$ remains in $[t_0/2,3t_0/2]$. If the binary valuation is now five, halve once more. We reach $t_*=16u$, $u$ odd, with $t_*\in[t_0/4,3t_0/2]$. If the initial valuation was four, take $t_*=t_0$.

At any such $t_*$ we can multiply the center by three while keeping both labels, using the centers
$$
 t_*,\quad 2t_*,\quad 4t_*,\quad 6t_*,\quad 3t_* .
$$
Use two reverse halvings, a $3/2$ move and a halving. For each odd $u$ there is $0\le j<128$ with $w=3^ju$ congruent to 49 modulo 256 or 197 modulo 512. Powers of three modulo 512 have order 128 and make up the units congruent to 1 or 3 modulo 8; the two targets represent opposite cosets. In the first class the starts $16w-1,16w+1$ both have endpoint 47 and five odd inputs at clock 12 for the base $w=49$. In the second class they have endpoint 281 and six odd inputs at clock 13 for the base $w=197$. The ordinary affine iterate formula therefore makes the meetings valid on every positive lift at the respective clock.

Every test argument in this construction is odd and comparable to $t_0$, with absolute factors because at most 127 final triplings are needed. A single failed argument can arise for only $O_b(\log(2R))$ choices of $t_0$. During an initial move the current center is $t=3^j2^{-i}t_0$, where $i$ is the number of preceding moves and $i=O_b(\log(2R))$. For each $i$ there are only boundedly many possible $j$ since $t/t_0$ stays between two absolute constants. Each test is an injective affine function of $t$. The last halving and boundedly many subsequent moves preserve this counting bound. If the pair at $t_0$ has different labels, at least one of the listed tests must fail. This proves the localized comparison.

## Consecutive odd integers

There exist constants $a_b,A_b,K_b>0$ such that
$$
 \#\{R\le n\le bR:f(2n+1)\ne f(2n+3)\}
 \le K_b\log(2R)\,\#\{a_bR\le d\le A_bR:d\text{ is a failure}\}. \tag{1}
$$
A finite certificate connects the offsets 1152 and 3456 of $2304n+p$. Its complete list is in [the checker](check_odd_shells.py). Here is how to verify the proof by integer arithmetic. For each of its 67 edges take a scale $s$ dividing $2304=2^8 3^2$. At the ten indices marked as crossings, divide both arguments by $s$ to obtain $16h-1,16h+1$ in either order. The preceding comparison applies to these centers, since $h$ is a positive affine function of $n$ with fixed nonzero slope. For the other 57 edges the normalized arguments are $3h,3h+1$, with $h$ odd, so the ordinary odd step and the test at $h$ suffice. In both cases the integer divisibility and parity conditions hold identically in $n$.

At a junction of consecutive scales $s,s'$ the two normalized arguments have smooth ratio $s'/s$. If $v_2(p)<8$, the binary valuation of $2304n+p$ is fixed, and clearing this ratio costs only tripling tests at odd inputs comparable to $R$. Each is an injective function of $n$. If $v_2(p)\ge8$, the certificate guarantees $v_3(s)=v_3(s')$, so the ratio is a pure power of two and no tripling test is needed. This last condition prevents a test from being made at an arbitrarily small odd part. Include the scale 1152 at both endpoints, yielding $2n+1$ and $2n+3$. The union bound proves (1).

## Moving an arbitrary set of low failures into one high window

There are absolute constants $a,A,K>0$ so that for every ordinary step-invariant label, writing $D_f(X)$ for all its odd failures up to $X$, one has
$$
 D_f(R)\le K\log^2(2R)\,\#\{aR\le d\le AR:d\text{ is an odd failure}\}. \tag{2}
$$
Let $W(y)=4y+1$ for odd $y$. Then $T^2(W(y))=3y+1$ is in the component of $y$, so $f(W(y))=f(y)$. For each odd failure $x\le R$ take the least $i\ge0$ for which $Y=W^i(x)\ge R$. We have $Y\le4R+1$ and there are $O(\log(2R))$ possible $i$. If $Y$ fails, count it directly. Otherwise
$$
 f(3Y)=f(Y)=f(x)\ne f(3x)=f(W^i(3x)).
$$
Both arguments are odd. Since $W^i(x)=4^i x+(4^i-1)/3$, the two arguments differ by $2(4^i-1)/3$. Both are between $R$ and $12R+3$. A pair with distinct labels therefore contains an adjacent change on the odd lattice. For each fixed $i$ the comparison intervals are disjoint as $x$ varies: their left endpoints have spacing at least $6\cdot4^i$, strictly greater than this interval length. Also $x\mapsto W^i(x)$ is injective. Summing over $i$ bounds $D_f(R)$ by $O(\log(2R))$ times the sum of the high-window failures and the number of high-window odd-neighbor changes. Apply (1) to those changes to conclude (2).

## From cumulative estimates to cuts of the component graph

Apply (2) to the indicator of a partition separating $A,B$. The [cumulative quantitative estimate](THREE_RAY_VARIATION.md) applies uniformly to this indicator: every failure test there uses the indicator itself, and the two mass lower bounds use fixed positive ternary-unit targets in the components $A$ and $B$, with constants independent of the other component assignments. In particular it gives $D_f(R)\gg_{A,B}R^{\alpha/(\kappa+1)}$ at every large $R$ with $\alpha=0.8399$ and $\kappa=4.117$. The exponent follows from the predecessor estimate of Krasikov and Lagarias and the linear-form bound of Wu and Wang. Its value exceeds $0.164$, allowing the logarithms in (2) to be absorbed. Rescale the argument of (2) by an absolute factor so its closed shell lies in $(R,CR]$. This proves the claimed local lower bound for every cut. At the prescribed scales $R=q^2$ for convergent denominators of $\log_2 3$, the same transfer gives $\gg_{A,B,\alpha} q^\alpha/\log^2 q$ failed edges in $[aR,AR]$ for any $\alpha<0.84$ without the linear-form input. [Krasikov–Lagarias, Theorem 6.1](https://arxiv.org/abs/math/0205002) · [Wu and Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

For a fixed partition, the [dyadic limit argument](THREE_RAY_DENSITY.md) also applies to its indicator with targets in $A$ and $B$. Thus an unbounded sequence of dyadic shells contains $\gg R^{0.84}$ crossing edges for that partition. Those particular shells may depend on the partition. The min-cut bound in every sufficiently large shell is simultaneous over all partitions.

Producing an unbounded sequence of such fixed-ratio shells with $o(R^{0.164})$ permanent failures would suffice for full Collatz. The upper bound on those failures remains open.
