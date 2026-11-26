# The persistent dyadic boundary and its actual tripling defects

Let $c$ be a Boolean label on the positive integers, constant on every ordinary Collatz edge. The basin indicator of 1 is one such label. Any nonconstant label has adjacent positive integers of different colors. From every such edge the following arguments construct a single nested path, with exact positive-integer labels on both sides at every resolution. No asymptotic density input enters the construction.

## Dyadic refinement

Give each positive dyadic rational $n/2^k$ the color $c(n)$. This is well-defined by $c(2n)=c(n)$. Suppose the endpoints of an interval $[n/2^k,(n+1)/2^k]$ have colors $A$ and $B$, with $A\ne B$. Precisely one of its two halves again has endpoints of different colors, since the midpoint has color either $A$ or $B$. Its orientation remains $A$ on the left and $B$ on the right. Iterate, and write $t$ for the unique point in the intersection of the closed intervals. If $t$ is not dyadic, the left endpoint at every depth is uniquely $n_k/2^k$, where $n_k=\lfloor2^k t\rfloor$.

The equalities $c(8q+4)=c(2q+1)=c(8q+5)$ exclude a left endpoint with binary suffix $100$. The first identity uses two halvings. For the second, the odd shortcut sends $8q+5$ to $12q+8$, whose two halvings give $3q+2$, also the odd shortcut of $2q+1$. Thus after a right move the path can never make two successive left moves. In particular a non-dyadic persistent path eventually has no consecutive zero digits. The resulting restriction applies to the tail after a particular edge has begun its path. Newly born edges can lie in previously constant-endpoint intervals.

## An exact dilation on left endpoints

For a positive integer $n$, write $d(n)=2^{v_2(n)}$ and $H(n)=(3n+d(n))/2$. If $n=d(n)u$ with $u$ odd, then $H(n)=d(n)(3u+1)/2$, so $c(H(n))=c(n)$. Along the above non-dyadic path, all sufficiently late $n_k$ have $d(n_k)=1$ or $2$. On these same indices,
\[
 H(n_k)=\lfloor 2^k(3t/2)\rfloor. \tag{1}
\]
Indeed write $2^k t=n_k+\tau$ with $0<\tau<1$. If the last digit of $n_k$ is one, the no-$00$ tail gives $\tau\ge(0.010101\ldots)_2=1/3$. The difference between $3(n_k+\tau)/2$ and $H(n_k)$ is $(3\tau-1)/2\in[0,1)$. If the last digit is zero, the next digit must be one, giving $\tau\ge2/3$ and the difference $(3\tau-2)/2\in[0,1)$. This proves (1), including equality at the lower endpoints.

Writing the next digit of $n_k$ and using (1), the binary output digit of $3t/2$ is the logical AND of two consecutive input digits. The three possible transitions $01,10,11$ give output $0,0,1$ respectively. At a late input zero, $n_k=4q+2$. Then $H(n_k)=6q+4$ and $H(n_k+1)=6q+5$. Thus the true dyadic cell of $3t/2$ at that resolution has the same two endpoint colors $A,B$ as the source cell. In particular this happens at arbitrarily fine resolutions whenever the source is non-dyadic.

## Long runs really prevent the proposed persistence

Suppose a late source zero ends a run of at least three ones. Then $n_k\equiv6\pmod8$, and $b=n_k+1=8u+7$ is an ordinary positive odd integer of color $B$. Here an actual tripling disagreement is forced,
\[
 c(3b)=c(b-1)=A\ne c(b). \tag{2}
\]
For a direct calculation, $3b=24u+21=4(6u+5)+1$. The odd integers $4x+1$ and $x$ have the same odd successor. Also $b-1=2(4u+3)$ and the shortcut of $4u+3$ is $6u+5$. This proves (2) with no assumption about the colors away from this one source edge.

Set $j=H(n_k)$. By (1) the left end of the target cell has index $j$. Its midpoint at the next depth has index $2j+1=3b$ and color $A$. The unique persistent target child is therefore the **right** half. The next source digit is one, so the $01$ input transition sends $3t/2$ into the **left** half. The two paths diverge at an explicitly identified midpoint. This calculation compares the very same ordinary endpoint $b$ on both sides of the tripling test.

If such source runs occur infinitely often, the persistent paths starting in the corresponding target cells give infinitely many distinct points strictly to the right of $s=3t/2$, converging to $s$. Each has orientation $A$ to $B$. There are also $B$ to $A$ persistent paths approaching $s$ from the right. To see this, choose a later target cell of sufficiently small width that its right endpoint of color $B$ lies strictly between $s$ and the earlier target midpoint of color $A$. Subdivide the intervening interval on their common dyadic grid. At least one adjacent edge has orientation $B$ to $A$, and its persistent path remains between the two selected endpoints. Repeating at successively smaller widths proves accumulation in the opposite orientation as well.

The [companion boundary branch](../boundary/) sharpens no-$00$ to the eventual restriction that successive zero digits have an odd number of ones between them. On that result a non-dyadic path is either eventually alternating or has infinitely many of the long runs used above. The alternating tail gives a dyadic $3t/2$ and is a separate case.

## The topological obstruction

The tail shift limit points of every non-dyadic persistent path lie in a common proper no-$00$ subshift. One may therefore take the closure of the union of these *tail limit sets*, without reinstating an arbitrary discarded prefix from each newly born edge. The map $x\mapsto 3x\bmod1$ would preserve that closed set if $3t/2$ were eventually a persistent path for every source path. Forward invariance under doubling is automatic on the tail limit sets. Furstenberg's topological theorem would force a closed proper set with both invariances to be finite. Even that conclusion would initially bound only the odd denominators of the tails, with dyadic preperiods still unrestricted. Equation (2) exhibits an obstruction to the proposed tripling argument: a point can be approached from the right by infinitely many genuine paths while its own true sequence of cells repeatedly takes the wrong child. Closure of the spatial boundary points and closure of their shift limit sets are different operations. [Furstenberg, *Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation* (1967)](https://doi.org/10.1007/BF01692494)

The iterated test $c(2^h b-1)=c(3^h b-1)$ also holds for every positive $b$ and every $h\ge0$. The single transition is $T(2b-1)=3b-1$; move one factor of two at a time. Thus a path whose right endpoint eventually stays at a fixed dyadic rational samples the same true color on these two integer rays. The status of those rays cannot be settled by the no-$00$ argument. Earlier work already reduces the least tripling disagreement to difficult ordinary bounded or unbounded branches. Here the disagreements in (2) arise at specified moving right endpoints and need not be least. [Earlier tripling reduction](../../astra-closure-20261125/descent/ATTEMPT.md)

The [Lean kernel](DyadicBoundary.lean) checks orientation and uniqueness of the dyadic child, the forbidden residue, both endpoint identities at an input zero, the binary digit transitions, the wrong-midpoint integer and color, and the two shifted power rays. The real-floor calculation, accumulation statement and topological discussion are written arguments. A positive counterexample or a proof that the basin label is constant remains open.
