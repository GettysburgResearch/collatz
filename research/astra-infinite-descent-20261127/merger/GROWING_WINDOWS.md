# Growing first-hit blocks with logarithmic additive overhead

This written corollary uses one quantitative input from PR146. Its whole-interval theorem supplies a binary cylinder of clock $h\le A\log^2(2n)$ on which all $n$ consecutive translates have the same endpoint and odd count. The earlier affine-rays note proves a polynomial bound; the sharper whole-interval note first compresses the representative list in $O(\log n)$ clocks, then sums the conditional merger tails to prove that **all** representatives in each group have fused by $O(\log^2 n)$ with positive probability. Only the ordinary additive group is needed here. The quantitative input has not been replayed in Lean in this packet. [PR146 whole-interval theorem and equation (4)](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md)

Fix $\delta>0$ and positive time and grade moduli $M,Q$. Put $L=\log_2(X/y)$ for a positive ternary-unit target $y$. There exists an absolute $c>0$ such that, for sufficiently large $L$ and $n=\lfloor\exp(c\sqrt{\log L})\rfloor$, **each** $[X,(1+\delta)X]$ contains $n$ consecutive positive integers first visiting $y$ at one common clock
$$
               L\le D\le L+O_{\delta,M,Q}(\log L)
$$
with one common grade $g=O_{\delta,M,Q}(\log L)$. Both $D\bmod M$ and $g\bmod Q$ can be prescribed independently. Within a single interval of $2n-1$ such starts, blocks of length $n$ begin in all residue classes of any given modulus $1\le m\le n$, with the same dates and grades. Using the cylinder for $2n-1$ in place of $n$ only changes absolute constants.

## Tracking the elementary costs

Choose the canonical $R<2^h$ of the successful dyadic cylinder and let its shared endpoint and grade be $a,p$ at free parameter zero. The affine upper bound gives
$$
         2^h a\le3^p(R+2^h)\le2^{h+1}3^p,
         \qquad a\le2\cdot3^p,\qquad p\le h .
$$
All $R+2^h u+i$ have endpoint $a+3^p u$ and grade $p$. Closing this profile at any supplied unit waypoint requires a two-gap tail of length $B$ exceeding $6\cdot3^p$ and at least $16(a+1)$. One may take the same integer $h_0=h+B=O(h+3^h)$ for every waypoint, with fixed grade $g_0=p+2$. This is the elementary closure used in the ordinary block proof. [BlockClock.lean](BlockClock.lean)

For fixed $\delta,M,Q$, the unconditional marked phase ladder gives constants $P,V,J$ and width $\varepsilon=\min(\delta/8,1)$. The physical transfer proof uses the following explicit threshold, clock multiplier and grade bound, with $d$ the largest offset:
$$
 C_0=1024\frac{2^{h_0}}{3^{g_0}}P+\frac{2^{h_0}+d}{\varepsilon}+1,
 \qquad
 K_0=4096V3^{g_0}(1+\varepsilon)^2,
 \qquad g\le g_0+J+1 .
$$
At $X\ge C_0 y$ it yields $2^D y\le K_0 X$ and the requested marks. The actual ordinary starts all lie inside the requested interval. [FastPairs.rows_of_marked_visitors](FastPairs.lean) and [MarkedWindow.lean](../escape/MarkedWindow.lean)

Thus $\log_2 C_0=O_{\delta,M,Q}(h+3^h+\log(2n))$, while $\log_2 K_0=O_{\delta,M,Q}(h+1)$. Choose $c$ small enough that the quantitative cylinder bound implies $3^h\le L^{\theta}$ for one fixed $\theta<1$. Then $\log_2 C_0=o(L)$, so $X/y=2^L\ge C_0$ for all sufficiently large $L$. The height formula yields the claimed $O(\log L)$ grade and additive clock estimates. Each ordinary shortcut step maps a start to at least half its value, giving $D\ge L$. All constants are uniform over $y$.

## Many growing blocks at a common date

Fix small $\eta>0$. The exponential lower and upper rates for disjoint patterns with one clock $D\le(1+\eta)L$ and one grade from the counting theorem still apply to these growing consecutive blocks. In its inverse-branch construction replace the fixed baseline by the above $n$-member baseline at every leaf. It admits exactly the same window because $\log_2 C_0=o(L)$. Its grade and additive clock overhead are $O(\log L)=o(L)$. The first-branch budget $l=\lfloor(\eta L-O(\log L))/\log_2 3\rfloor$ keeps the same limiting ratio, and the number of clock and grade bins remains polynomial in $L$. Prescribe each leaf's remaining clock and grade classes after subtracting its physical suffix data. First-visit decoding still keeps the blocks from different branches disjoint. The entropy squeeze and its two leading small-$\eta$ terms therefore persist, with $n$ as above. [Near-minimum-time counting theorem](FAST_COUNTING.md)

PR146 placed growing blocks in $[1,X]$ using a ratio-five comparison. PR202 and PR203 establish stronger length or density conclusions in windows under specified analytic inputs, including near-linear or joint modular routing. The argument here retains PR146's quantitative prefix input, uses the elementary two-odd-step terminal router and unconditional rotation net, and obtains additive clock and grade bounds for the first visit of every individual member. [PR202](https://github.com/GettysburgResearch/collatz/pull/202) · [PR203](https://github.com/GettysburgResearch/collatz/pull/203)
