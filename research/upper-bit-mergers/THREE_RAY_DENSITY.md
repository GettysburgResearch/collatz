# A counterexample forces at least a power 0.84 of tripling failures along a sequence

**PROPOSED.** Let $D(X)$ count odd positive $x\le X$ for which $x$ and $3x$ never meet under the ordinary shortcut map. If Collatz is false, then
$$
 \limsup_{X\to\infty}\frac{D(X)}{X^{0.84}}>0.
 \tag{1}
$$
Consequently $D(X)=o(X^{0.84})$ would settle the conjecture, as would convergence of the sum of $x^{-0.84}$ over all failed odd parameters. The bound is on an unbounded sequence of cutoffs. The separate all-scale result gives a smaller positive exponent. [Every-scale estimate](THREE_RAY_VARIATION.md)

The numerical exponent comes from the published theorem of Krasikov and Lagarias: for any fixed positive $a$ prime to three, at least $X^{0.84}$ starts up to $X$ reach $a$ for all sufficiently large $X$. Every component contains an odd ternary unit, by stripping powers of two and taking an odd step followed by any required halvings. Thus, if there are two components, each has at least this many members up to $X$. The proof below applies with any exponent $0<\alpha<1$ for which these two lower bounds hold with positive constants. The elementary inverse tree gives $\alpha=\log 2/\log(64/3)$ independently of the 0.84 theorem. [Krasikov and Lagarias, *Bounds for the 3x+1 problem using difference inequalities*](https://arxiv.org/abs/math/0205002) · [Elementary inverse tree](THREE_RAY_VARIATION.md#mass-of-two-components-on-a-coarser-grid)

## Passing to a limit under doubling

Suppose for contradiction that there is a second component and $D(X)=o(X^\alpha)$. Let $f$ indicate the component of 1. Write $g_R(t)=f(\lfloor R2^t\rfloor)$ for $0\le t<1$, extended periodically, with $R$ a positive power of two. There are $o(R^\alpha)$ changes of $f$ between adjacent integers in $[R,7R]$, by the [finite chain of comparisons](TRIPLING_VARIATION.md). Always $f(2n)=f(n)$. For $n=\lfloor R2^t\rfloor$, the integer $\lfloor 2R2^t\rfloor$ equals $2n$ or $2n+1$. A disagreement between $g_R$ and $g_{2R}$ therefore requires a change at $2n$. Each $n$ occupies a set of measure at most $1/(R\log 2)$. It follows that
$$
 \|g_{2R}-g_R\|_1=o(R^{\alpha-1}).
$$
Since $\alpha<1$, these successive differences are summable along dyadic scales. There is an $L^1$ limit $g$, and summing the geometric tail gives $\|g_R-g\|_1=o(R^{\alpha-1})$. The limit is binary almost everywhere, for example by taking an almost-everywhere convergent subsequence.

Set $\theta=\log_2 3$. Rotation by $\theta$ on the circle sends $x=R2^t$ to $3x/2^j\in[R,2R)$ for $j=1$ or 2. The difference between the integers $3\lfloor x\rfloor$ and $2^j\lfloor 3x/2^j\rfloor$ is at most four. A change of color caused by this rounding requires an adjacent change within four of $3\lfloor x\rfloor$. Each adjacent change can affect only boundedly many $\lfloor x\rfloor$. Meanwhile differing labels at $\lfloor x\rfloor$ and $3\lfloor x\rfloor$ require a failed odd part, each with at most two dyadic lifts in $[R,2R]$. Consequently
$$
 \|g_R(\cdot+\theta)-g_R\|_1=o(R^{\alpha-1}).
$$
Passing to the limit gives $g(\cdot+\theta)=g$. The number $\theta$ is irrational by unique factorization. Every nonconstant-frequency Fourier coefficient of $g$ vanishes since it equals itself times $e^{2\pi i k\theta}\ne1$. Hence $g$ equals a constant almost everywhere, and this constant is either zero or one.

## Counting the minority color

The other color now has logarithmic measure $o(R^{\alpha-1})$ at each dyadic scale $R$. Every integer $n\in[R,2R)$ contributes $\log_2(1+1/n)\gg 1/R$ to the measure of its color. Thus the number of integers of the other color in that shell is $o(R^\alpha)$. Summing dyadic shells, including one full shell covering the upper endpoint if necessary, gives $o(X^\alpha)$ such starts up to $X$. If $g=0$, this contradicts the lower bound for the component of 1. If $g=1$, it contradicts the lower bound for the second component. This proves (1). It also gives infinitely many dyadic intervals $[R,2R)$ with at least $cR^{0.84}$ odd defects for some $c>0$: a little-o count in every such interval would sum to a little-o cumulative count. Convergence of the displayed critical moment would imply $D(X)=o(X^{0.84})$ by discarding a finite initial segment and bounding its remaining counting function by $X^{0.84}$ times the tail of the moment.

For the five-ray let $B(X)$ count $t\le X$ for which $t$ and $5t+1$ never meet. Every failed odd $x\le X/4$ has an $a\ge2$ with $4X/3<2^a x\le 8X/3$. At least one of $2^a x$ and $3\cdot2^{a-2}x$ fails the five-ray test. Both lie in $(X,8X/3]$, and any integer occurs for at most two odd $x$. Hence
$$
 B(8X/3)-B(X)\ \ge\ \tfrac12D(X/4).
$$
In particular the same exponent 0.84 is forced along a sequence of five-ray intervals, and the smaller all-scale power bound also holds in every sufficiently large such interval. This transfer uses the ordinary identity $T^2(20u+1)=15u+1$. [Five-ray comparison](THREE_RAY_WINDOWS.md)

## A separate criterion when both components have positive upper density

If the failed odd parameters have finite reciprocal sum, the same dyadic limit exists and is constant for the indicator of each component. Indeed
$$
 \sum_{j\ge0} 2^{-j}D(C2^j)<\infty
$$
by summing the geometric series for each failed parameter separately. The variation and rotation bounds above now give summable successive $L^1$ differences and vanishing rotation error. The minority color has $o(R)$ points in each dyadic shell and thus $o(X)$ up to $X$. In particular, two different components of positive upper density force divergence of the reciprocal sum of the failed odd parameters. This implication holds without any lower bound on inverse trees.

The repository's separately source-qualified first-landing estimate supplies positive upper density for the basin of every fixed odd ternary unit. If that external estimate is assumed, a single counterexample would force the reciprocal sum to diverge. The results with exponent 0.84 above use only the published predecessor theorem. [Exact first-landing input and dependencies](https://github.com/GettysburgResearch/collatz/blob/4e94f656236485ebf854711528b06c18b91d4ad3/research/critical-orbit-mellin/LOCAL_FIRST_LANDING.md#consequence-for-separating-ordinary-basins)
