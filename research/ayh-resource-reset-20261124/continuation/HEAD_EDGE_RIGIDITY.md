# Power-sparse truncation failures on one ternary head would settle Collatz

**Status.** Written theorem, with the published ordinary predecessor lower bound identified below. The power-sparse upper bound needed for universal convergence is open. The proof uses the standard shortcut map on positive integers and allows independent clocks in a common future.

Use only one of the four exponent classes of the fixed-head section. Put
$$
 I=[7,8),\qquad R_j=81^j,\qquad H_j=[7R_j,8R_j)\cap\mathbb N \quad(j\ge1).
$$
Let $D_j$ count $x\in H_j$ whose physical orbit and that of $\lfloor x/81\rfloor$ have no common future. If every positive integer reaches one then $D_j=0$ for every $j$.

**Theorem.** If Collatz fails, then
$$
               \limsup_{j\to\infty} D_j/R_j^{0.84}>0.
$$
Equivalently, $D_j=o(R_j^{0.84})$ already suffices for universal convergence. An eventual bound $D_j=O(R_j^\delta)$ for any $\delta<0.84$ suffices, as does a bound of that size for a *superset* of the forever-failed edges, such as those missed by a finite certificate. The statement uses every sufficiently high level for the upper bound; a low-failure subsequence alone does not give the conclusion. The argument works with any $0<\alpha<1$ in place of $0.84$ for which the two distinct colors have cumulative ordinary counts $\gg X^\alpha$ at all large $X$. In particular, a finite set of failed edges anywhere in this single head cannot support a bad component.

## The digit identity and the limiting color

Write $f(n)=1$ when $n$ reaches one, and $f(n)=0$ otherwise. Then $f(2n)=f(n)$ for all positive $n$. Any two starts with a common future have the same color because the orbit of one lies on the closed cycle $1,2$. Define $F_j(t)=f(\lfloor R_j t\rfloor)$ for $t\in I$, with ordinary Lebesgue measure. The identity
$$
 \left\lfloor\frac{\lfloor R_j t\rfloor}{81}\right\rfloor
       =\lfloor R_{j-1}t\rfloor
$$
gives $\|F_j-F_{j-1}\|_{L^1(I)}\le D_j/R_j$: there is one interval of length $1/R_j$ for each possible child. For the contradiction assume $D_j=o(R_j^\alpha)$. The geometric series then makes $F_j$ converge in $L^1(I)$ to $g$, with
$$
 \|F_j-g\|_1\le \sum_{i>j} D_i/R_i=o(R_j^{\alpha-1}).
$$
For the last little-o, bound the normalized tail by $\sup_{i>j}D_i/R_i^\alpha$ times the geometric sum. The limit is binary almost everywhere, for example by taking an almost-everywhere convergent subsequence.

## Recovering an irrational rotation from exact integer doublings

Fix $k\ge0$ and $l\in\mathbb Z$. Let $M=2^k$, $c=M/81^l$, and $U=I\cap c^{-1}I$. All indices $j+l$ below are nonnegative once $j$ is large. On the part of $U$ with $\{R_j t\}<1/M$, ordinary integrality gives
$$
 \lfloor R_{j+l} c t\rfloor=\lfloor M R_j t\rfloor=M\lfloor R_j t\rfloor.
$$
Thus $F_{j+l}(ct)=F_j(t)$ there. For $A_j(t)=\mathbf1_{\{R_jt\}<1/M}$, the functions $A_j$ tend weakly against every integrable function on $I$ to the constant $1/M$. Indeed on each full cell of length $1/R_j$ the average is exactly $1/M$, the error for the integral over a single interval is at most $2/R_j$, and interval step functions are dense in $L^1(I)$.

Integrate $A_j(t)|g(t)-g(ct)|$ over $U$. By the preceding exact agreement its integral is at most $\|F_j-g\|_1+c^{-1}\|F_{j+l}-g\|_1$. This tends to zero. Weak convergence of $A_j$ against the **fixed** integrable difference yields $g(t)=g(ct)$ almost everywhere on $U$. This argument works for each fixed $k,l$. Their countability permits removing the union of all exceptional null sets. No regularity or bounded variation of $g$ is required.

In logarithmic coordinates, $I$ identifies with the arc $J=[\log_{81}7,\log_{81}8)$ of $\mathbb R/\mathbb Z$. Lebesgue measures before and after this change have exactly the same null sets. Let $S$ be rotation by $\log_{81}2$, irrational by unique factorization. The previous equality states that the color on $J$ is preserved almost everywhere on $J\cap S^{-k}J$ for every nonnegative integer $k$, including wrap-around by $l$. This forces the color to be constant almost everywhere. Indeed if its two color classes $P,Q\subset J$ had positive measure, then $Q\cap S^k P$ would be null for every $k\ge0$. The positive-measure union $V=\bigcup_{k\ge0}S^kP$ satisfies $SV\subset V$ and $|SV|=|V|$. It is invariant modulo null sets, hence conull by ergodicity of irrational circle rotation. For completeness, the Fourier coefficient of its indicator at integer frequency $h$ is unchanged by multiplication by $e^{2\pi i h\log_{81}2}$. This factor differs from one at every nonzero $h$, so Fourier uniqueness in $L^2$ makes the indicator constant almost everywhere. Its positive measure forces that constant to be one. This contradicts the positive measure of $Q$. This uses only returns to this one arc.

## Transport to actual starts

Call the color different from the constant the minority color. Its number in $H_j$ is precisely $R_j\|F_j-g\|_1=o(R_j^\alpha)$. Summing the geometric sequence of levels shows that the total number of this color in $\bigcup_{j\ge1}H_j$ below $Y$ is $o(Y^\alpha)$ for all large $Y$; a partial last interval can be counted in full.

Every sufficiently large ordinary integer $n$ has a dyadic multiple $2^k n$ in some $H_j$, with $0\le k\le K$ for one absolute $K$. In logarithmic coordinates the backward translates by the nonnegative rotation iterates of the *interior* of $J$ cover the circle by density, and compactness supplies a finite subcover. Apply this to $\log_{81} n$ modulo one. At sufficiently large $n$ the resulting exponent $j$ is at least one. The passage preserves the color and increases size by at most $2^K$. Every selected multiple has at most $K+1$ possible starts, one per clock. Hence the total number of minority-colored starts up to $X$ is $o(X^\alpha)$.

If a nonconvergent start exists, its orbit contains a positive $b$ prime to three. In fact one can halve to an odd value and take the odd-input shortcut step, whose result is prime to three. Every start reaching $b$ fails to reach one, and every start reaching one has the opposite color. For each fixed $b$ prime to three the published theorem of Krasikov and Lagarias gives at least $c_bX^{0.84}$ starts up to $X$ that reach $b$, at all sufficiently large $X$, and it applies also to $b=1$. This contradicts the minority bound for either choice of its color. The conditional argument with a different predecessor exponent changes only this final input.

## Relation to the earlier results

PR 146 previously used a limiting color and an irrational rotation for **tripling comparisons on all odd integers**. Its argument bounds adjacent variation via separate finite merger chains. Here the limit lives on one proper arc, the comparison is actual deletion of four terminal ternary digits, and exact doubling recovers the return action by positive-density subcells. No adjacent-variation estimate, synchronous-fusion estimate, fresh law on transported partners, or independence hypothesis enters the rigidity proof.

The existing estimate of order $X/\sqrt{\log X}$ for unsuccessfully certified fixed-depth edges is above $X^{0.84}$. Controlling the number of actual or possibly failed edges at this sharper power remains open. The theorem is a conditional closing criterion for the actual fixed head, not an unconditional proof of universal convergence.

[Krasikov and Lagarias, Theorem 6.1](https://arxiv.org/pdf/math/0205002) · [PR 146 tripling comparison at the frozen source](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_DENSITY.md) · [Fixed-head construction](FIXED_HEAD.md)
