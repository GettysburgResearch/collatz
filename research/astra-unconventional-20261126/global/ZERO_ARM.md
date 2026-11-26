# Rational persistent interfaces with a signed reference reaching zero

Use the [positive dyadic boundary construction](DYADIC_BOUNDARY.md) for a Boolean label $c$ invariant under the ordinary shortcut $T$. At precision $k$, a non-dyadic rational endpoint $t$ has fractional part $r/q=\{2^k t\}$, where $q$ is its reduced odd denominator after the initial dyadic prefix has been removed. The two signed rational references for the adjacent positive cells are $-r/q$ and $1-r/q$. The positive reference always stays positive. If the negative reference ever reaches zero, an ordinary affine branch identity $2^d T^d(x)=3^u x+B$ with $B$ integral gives $q\mid3^u$. Thus $q=3^h$. Doubling permutes the units modulo $3^h$ transitively: $2$ has order $2\cdot3^{h-1}$, since $v_3(4^{3^s}-1)=s+1$ follows by induction from $(1+v)^3-1=3v+3v^2+v^3$ for $3\mid v$. Some later fractional part is therefore $1/3^h$. Every sufficiently late binary tail of a persistent non-dyadic cell has no $00$, so its value is at least $1/3$. This leaves **$q=3$**. A dyadic interface, where a reference may be zero from the start, is the other case.

## Denominator three

Dyadically rescale the spatial point to $p/3$ with $p$ positive odd and $3\nmid p$. This preserves all colors of dyadic endpoints and merely shifts the resolution index. At all large depths the ordinary left endpoint has color $c(p)$. Indeed if $2^k p$ leaves remainder one modulo three then the left index $n=(2^k p-1)/3$ is odd and $3n+1=2^kp$. If the remainder is two then $n=2(2^{k-1}p-1)/3$ has the same color by halving.

For the right endpoints use the exact identity $c(4^h a+1)=c(3^h a+1)$ for every positive integer $a$, obtained by applying $T^2(4u+1)=3u+1$ repeatedly. Write $j\ge2$.

* If $p\equiv1\bmod3$, at depth $2j$ the right index is $x=(4^jp+2)/3$. Its half $u$ is odd and $T(u)=4^{j-1}p+1$. Consequently $c(x)=c(3^{j-1}p+1)=c(3^{j-2}p)$, using oddness of $3^{j-2}p$ at the final step. At depth $2j+1$, the odd right index $(2\cdot4^jp+1)/3$ has shortcut $4^jp+1$, so its color is $c(3^{j-1}p)$.
* If $p\equiv2\bmod3$, at depth $2j$ the odd right index $x=(4^jp+1)/3$ has $T(x)=2\cdot4^{j-1}p+1$. Its color is $c(2\cdot3^{j-1}p+1)=c(3^jp+2)$. At depth $2j+1$ the right index is $2x$, of the same color.

Thus the true dyadic cells of $p/3$ form an eventually persistent boundary if and only if **one particular ordinary ray eventually has the color opposite to $c(p)$**. The ray is $3^jp$ for $p\equiv1\bmod3$, and $3^jp+2$ for $p\equiv2\bmod3$. This keeps the unbounded positive original indices. Signed rational nonfusion alone would not establish persistence.

## Dyadic endpoints

Normalize the point to a positive odd $p$. If the nested cells approach it from the left then they have left index $2^k p-1$ and right color $c(p)$. The exact identity $c(2^kp-1)=c(3^kp-1)$ from the [Lean kernel](DyadicBoundary.lean) gives an equivalence with eventual opposite color on the single ray $3^kp-1$.

If the cells approach from the right then their right index is $2^k p+1$ and their left color is $c(p)$. At even depths $2j$ the right color is $c(3^jp+1)$. At odd depths $2j+1$ it is $c(2\cdot3^jp+1)=c(3^{j+1}p+2)$. Thus both of these ordinary rays must eventually have the opposite color; conversely those two conditions give persistence from the right. An all-left tail cannot follow an earlier right move on a persistent path because it would contain $100$. This endpoint case can still start at an already divisible left integer in the original cell.

## What fixed-gap coalescence supplies

For any fixed integer $d$, the colors of $3^jp+d$ and $3^jp$ agree for a natural-density-one set of large exponents $j$, on the source-qualified Haar-almost-sure **counted** fusion theorem for the fixed gap $d$. Indeed the success cylinders have full additive Haar measure in $\mathbb Z_2$ and consist of congruences giving equal true affine endpoints for *every* represented pair. The powers $3^j p$ are equidistributed on their clopen multiplicative orbit, which carries normalized additive Haar there: each parity of $j$ is equidistributed on one coset of $p(1+8\mathbb Z_2)$, by the orders of $9$ modulo powers of two. Approximate the full-measure open success set from below by finitely many dyadic cylinders. The actual starts are positive for all sufficiently large $j$. The same argument applies simultaneously to finitely many fixed shifts. [Leen, *Quantitative synchronization of Collatz trajectories*](https://doi.org/10.5281/zenodo.23268755)

Consequently every zero-reference persistent interface would force the color of $3^jp$ to be opposite to that of its fixed ordinary source $p$ for density-one exponents $j$. The unshifted ray may even be opposite at every large exponent in the first residue case above. Changing an exponent by any fixed amount does not test a return to exponent zero. A proof of a positive upper frequency of returns to $c(p)$ on every such actual ray would exclude these cases. The fixed-gap input alone gives no such recurrence.

The ordinary identities for all plus-shifted powers and the even-depth right residue-two endpoint are also checked in [DyadicBoundary.lean](DyadicBoundary.lean). The necessity of an ordinary positive source for the geometric recurrence test is visible on a signed rational control. On rationals with odd denominator, take the exact invariant label of eventually reaching zero and the source $p=-1/3$. Its first shortcut reaches zero. For every $j\ge1$, $3^jp$ is a nonzero negative integer, and the set of nonzero negative integers is forward invariant under the shortcut. Every one of these tripled sources has the opposite color. This control uses a different source domain from the positive-integer question.

## The isolated central source after dyadic magnification

Write $A=c(p)$ and let $B\ne A$ be the density-one color of $3^jp$ in the conclusion above. For every fixed nonzero signed integer $d$ whose signed shortcut orbit eventually enters a nonzero cycle,
\[
  c(2^k p+d)=B \quad\text{for a density-one set of }k. \tag{1}
\]
Here the displayed starts are positive for all sufficiently large $k$, and $c$ is used only on positive integers. Let $Q_k(d)$ count the odd departures of the signed reference in its first $k$ shortcuts. The positive and signed inputs agree modulo $2^k$ and thus have the very same first $k$ physical parities. Unfolding their affine maps gives the exact positive endpoint
\[
 T^k(2^kp+d)=3^{Q_k(d)}p+T^k(d).
\]
On each phase of the fixed nonzero cycle, the additive offset is fixed and $Q_k(d)$ runs in an arithmetic progression with positive increment. A finite union of such progressions, sampled in their phase clocks, meets any zero-density exponent set in zero density. The preceding fixed-shift geometric fusion and the opposite-ray assumption prove (1). Intersecting finitely many density-one sets works for any prescribed finite collection of such offsets. At $d=0$, $c(2^kp)=A$ exactly at every depth.

If all nonzero signed reference offsets in a fixed symmetric window are verified eventual nonzero-cycle points, the window at $2^kp$ therefore consists of the single central $A$ surrounded by $B$ at density-one depths. In the limiting signed-integer equations the single central exception is consistent: the indicator of $\{0\}$ is exactly invariant under the signed integer shortcut, since no nonzero integer has a forward iterate equal to zero. This explains why checking only the limiting local edge equations cannot eliminate the isolated positive center. The identity (1) never assumes that all positive or signed integers are periodic.

The signed displacement identity at the precise physical clock $k$ is formalized for all integer $p,d$ in `DyadicBoundary.magnifiedEndpoint`. The limit statements use the separate stated full-measure fixed-gap input.

A more restrictive sampling consequence holds when color $A$ contains a positive-lower-density family $E$ of eventually periodic positive integers, as happens when $A$ is the basin of 1. There are increasing exponents $k_j$ and increasing ordinary offsets $d_i\in E$ such that the actual positive-integer colors obey
\[
 c(d_i+2^{k_j}p)=\begin{cases}B,&i\le j,\\ A,&i>j.\end{cases} \tag{2}
\]
To choose $d_i$, each of the finitely many previously fixed translations $2^{k_j}p$ preserves the color of a density-one set of positive inputs by fixed-gap counted fusion. Their intersection still meets $E$ at arbitrarily large integers. Next choose $k_i$ large enough to satisfy (1) for $d_1,\ldots,d_i$ simultaneously. These are density-one sets of exponents. The resulting two iterated limits of the array (2) are different. In particular its sampling violates the double-limit property necessary for weak almost periodicity under addition. The restriction of one sampling sequence to powers of two times the *same* root is the extra conclusion here. Without this restriction, two thick colors already allow an upper-triangular color array by successively translating each finite row or column into a monochromatic interval. [Grothendieck's double-limit characterization, summarized by Ben Yaacov](https://doi.org/10.1017/bsl.2014.33)
