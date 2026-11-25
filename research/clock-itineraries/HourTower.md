# Delayed lower-base mergers at a prescribed tower rank

Let $T$ be the shortcut Collatz map. At a supplied source $3^r w$, a lower comparison can start at any $2^a3^s b$ with $b<w$, or with $b=w$ and $s<r$. Each trajectory can use its own clock. This is the ordinary comparison required by the least-tower argument. [PR 192, smooth-core reduction](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-universal-closure-20261124/global/SmoothCore.lean)

## A full lower-cone search can miss for $10^{243}$ steps

**At rank 512, arbitrarily large bases $w\equiv1\bmod6$ have both of the following properties.**

* The actual positive source $3^{512}w$ reaches 1.
* No lower comparison meets it with both clocks at most $10^{243}$. The competing base, its ternary exponent, and its initial power of two are unrestricted within the lower cone.

The center is an ordinary integer constructed by congruence and a final one-gap hit of 1. The result gives a lower bound on the search horizon at one fixed rank. The constructed bases can be much larger than that horizon. [Lean theorem `rank512_delayed_merger`](HourTowerLag.lean)

More generally, prescribe $r,H,L$. Lean constructs $w>L$ in the same unit class with $3^r w$ converging. If
$$
T^h(3^r w)=T^k(2^a3^s b),\qquad h,k\le H
$$
is any lower comparison, there are nonnegative integers $d,g$ satisfying
$$
\begin{aligned}
k&=a+h+d, &
2^d&<3^g, &
3^r(3^g-2^d)&<2^d,\\
3^g(b-1)&=2^d(w-1), &&
3^r(w-1)&<(3^r+1)(b-1).
\end{aligned}
$$
Thus any successful competitor has a positive effective clock lead and a uniquely determined base for each admissible power pair. The base must lie in the upper $1/(3^r+1)$ portion of the interval from 1 to $w$. The elementary inequality $3^r<2^d$ already excludes the entire cone whenever $2^H\le3^r$. [Lean theorems `prescribed_cone_resonance` and `no_lower_cone`](HourTower.lean)

The construction arranges $2^{H+1}\mid 3^r w+1$ and $3^{2H+r+3}\mid w-1$. All source departures through $H$ use the odd branch and every endpoint through $H$ is odd. Hence an initial power of two on the competing side must have been removed by the meeting. If its remaining clock is shorter, the competitor's actual parity carry gives $s+p\le k'$ at its effective clock $k'$, where $p$ counts its odd departures. Comparing the two affine formulas then gives $3^{h-k'}(3^r w+1)\le2^{h-k'}(b+1)$, which forces $b>3^r w$. For a longer competing arm, remove its first $d$ steps and compare the two remaining equal-length words. The deep ternary congruence permits replacing $w$ by 1 in the affine identity. The resulting competitor intercept is a positive multiple of $3^s$. The strict lower-cone inequality and the carry bound force that multiple to equal $3^s$ exactly. Cancelling the common powers yields the displayed identities. A further congruence-preserving lift makes the source reach 1. [Physical and positivity proofs](HourTower.lean) · [One-gap terminal lift](SynchronousShadow.lean)

At rank 512 the lag inequality requires an exceptionally close power of three above $2^d$. The kernel certificate brackets $\log_3 2$ by two rational numbers with determinant one. Every earlier upper approximation has at least the multiplicative gap of the certified upper bracket until the sum of the two denominators, which exceeds $4.75\cdot10^{243}$. Lean proves the determinant comparison with integer powers and verifies the two bracket inequalities by repeated squaring with outward-rounded integer endpoints. No floating-point result enters the theorem. [Integer bracket and rounding proof](HourTowerLag.lean)

## Positive captures at the original exponents

There are also explicit classes on which a comparison succeeds. In each row put $t=t_0+2^h u>0$, $w=1+3^g t$ and $b=1+2^d t$. Then $0<b<w$ and $T^h(3^r w)=T^{h+d}(3^s b)$ for every nonnegative $u$ satisfying the stated positivity.

| Supplied rank $r$ | Supplied clock $h$ | Competitor clock $h+d$ | Competitor rank $s$ | $g$ | $t_0$ |
|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 10 | 6 | 4 | 4 |
| 2 | 1 | 20 | 9 | 12 | 0 |
| 3 | 2 | 105 | 21 | 65 | 0 |
| 4 | 1 | 1139 | 174 | 718 | 0 |
| 5 | 1 | 1055 | 138 | 665 | 0 |

These are physical meetings at the supplied rank. Lean checks one endpoint and one affine slope on each arm, then proves the equality on every lift. PR 208's sibling construction gives a different sufficient ternary class at every rank. [Lean theorem `supplied_captures`](HourTowerCapture.lean) · [PR 208 positive siblings](https://github.com/GettysburgResearch/collatz/blob/72635b2a3af2f5b6cbf4eeff7ce1c89b6e6a5f7f/research/openai-machinery-20261125/tensor/README.md)

Every prescribed positive progression $a+2^H3^K t$, at each supplied rank $r$, contains arbitrarily large centers $w$ whose $3^r w$ reaches 1 at a clock $m\ge H$. On the entire refinement $W=w+2^m3^K t$, the actual endpoint satisfies $T^m(3^r W)<W$. To obtain such a center, transport the original prefix to an odd endpoint, then use a ternary lift that reaches 1 in one odd gap. If the initial rank plus odd count on the resulting prefix equals $E$, appending $4E$ laps of the $1,2$ cycle gives enough contraction since $3^5\le2^8$. Successive refinements yield uniform descent at every rank of any prescribed finite list, with a clock for each rank. [Lean theorems `dense_capture` and `finite_dense_capture`](HourTowerDensity.lean)

There is also a single explicit clock for all ranks $0\le r\le R$. Set $E=R+H+1$ and $m=H+80E$. Every progression $a+2^H3^Kj$ contains arbitrarily large centers $w$ such that all lifts $W=w+2^m3^Ku$ satisfy $T^m(3^rW)<W$ simultaneously. The bound depends only on the number of prescribed binary digits and the largest rank. [Lean theorem `Counting.common_clock`](HourTowerCounting.lean)

For the proof, fix the first $H$ steps. Each remaining input, as its base varies in the progression, runs through an odd-stride progression. Over a packet of $2^k$ parameters the sum of $2^P$, where $P$ counts odd departures in the next $k$ steps, is exactly $3^k$. The even and odd parameter branches have multipliers 1 and 2. With $k=80E$ the sum over all ranks is at most $2^k2^{48E}$, so one parameter has $P\le48E$ at every rank. Its full grade, including its starting rank, is at most $H+R+48E$. The inequality $3^{49}\le2^{80}$ gives strict contraction of each slope. A starting base above $3^m$ absorbs the affine carry, and adding any multiple of $2^m3^K$ preserves all the tested parities. [Exact moment and contraction proof](HourTowerCounting.lean)

Lean also counts how many parameters work in each packet. Start at any $v>3^m$ and take $w_t=v+2^H3^Kt$ for $0\le t<2^k$. At least half of these $t$ simultaneously give descent for every rank and every further lift. More precisely, the number $B$ outside the certified set satisfies $2^{48E}B\le(R+1)3^{80E}$. Each excluded parameter consumes at least $2^{48E}$ of the total weight. Its excluded fraction is therefore at most $(R+1)(3^{80}/2^{128})^E$, where the base is less than $7/16$. [Lean theorem `Counting.majority_packet`](HourTowerCounting.lean)

Consequently, for fixed $R,H,K,a$ the parameter set for which the ranks $0,\ldots,R$ never all descend below $a+2^H3^Kt$ at a common clock has upper Banach density zero. To see this written consequence, take any $J\ge H$ and split the parameter progression into its $2^{J-H}$ classes. Apply the packet theorem at binary depth $J$ to each class. Every sufficiently high consecutive block of $2^{J-H+80(R+J+1)}$ parameters consists of one full packet per class, so its exceptional fraction is at most $(R+1)(7/16)^{R+J+1}$. The finite starting segment and two boundary blocks contribute a vanishing fraction uniformly as interval length grows. Taking $J$ arbitrarily large gives the claim.

## Comparison with the finite-class bound

PR 195 round 12 gives a written uniform estimate $\log D\le160M^{-1/80}$ for the multiplicative correction $D$ on a finite simple prefix whose states are all at least $M$. Its bounded-lag theorem permits arbitrary individual clocks. A direct consequence of that estimate is a quantitative restriction across different fixed unit bases. Suppose simple prefixes from $3^r w$ and $3^s b$ meet, with $w,b$ positive and coprime to 6. Put $W=\max(w,b)$ and $B=|h-k|$. If $M>(320W2^B)^{80}$, the two clocks, the two bases, and both initial-rank-plus-odd-count totals must agree. [PR 195 path estimate](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/arithmetic/README.md) · [PR 195 bounded-lag result](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/arithmetic/HIGH_GATE.md)

Indeed, orient the merger with $h\ge k$ and write $g=r+P_h-s-P_k$. The exact endpoint identity makes $2^{h-k}b/(3^g w)$ a quotient of the two corrections. After clearing a negative $g$, the smaller of the two positive integers in this ratio is at most $W2^B$. If they differ, the absolute log ratio is at least $\log(1+1/(W2^B))\ge1/(2W2^B)$. The source estimate makes it strictly smaller. Equality of the integers forces equal clocks by oddness and equal grades by the ternary-unit assumptions, followed by $w=b$. This paragraph uses the written simple-path estimate. The preceding Lean theorems have independent finite proofs.

The full conjecture still requires a merger for the particular least bad base and rank if one exists. The positive theorems locate actual successful refinements. The delayed examples show that a lower-base witness can occur very late even when the supplied source converges.
