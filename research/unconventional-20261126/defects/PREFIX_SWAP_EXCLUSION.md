# No compensated adjacent block swap after an arbitrary common prefix

**Written theorem.** Start from a positive ordinary integer \(x\), execute any finite shortcut parity word, then execute two complete odd ascent-and-reset blocks to the odd value \(z\). Suppose \(3(z+1)\ge x+1\). No distinct positive integer can follow the same prefix and then the same two blocks in transposed order to that terminal. The shared prefix may have arbitrary length. Only the first trajectory has a height hypothesis.

Use the block parameters and the two ternary divisibility cuts of [the two-block theorem](TWO_BLOCK_SWAP_EXCLUSION.md). Write \(H\) for the physical length of the common prefix and \(p\) for its number of odd departures. The shifted height \(Y=x+1\) is multiplied by exactly \(3/2\) at an odd step, and does not increase at an even step. Its value at the start of the blocks is at most \((3/2)^pY\). If \(p=0\), the terminal floor is therefore at least one third of that block entrance's shifted height. The two-block theorem applies directly. The common prefix has nonzero affine slope, so distinct original entrances are still distinct there.

Suppose \(p\ge1\). For two distinct proposed original entrances \(x,x'\), the signed difference \(\delta\) at the start of the transposition satisfies \(2^H\delta=3^p(x'-x)\). Hence \(\delta\ne0\) and \(3^p\mid\delta\). Identical blocks would execute an identical injective affine map, which cannot merge these inputs. Orient the distinct pairs as \((m,c),(M,d)\) with \(m\le M\); reversing them changes the sign of the required difference but preserves every bound below. Put \(D=c+d\). The exact transposition formula yields
\[
 U=(2^c-1)2^m3^M-(2^d-1)2^M3^m+(2^d-2^c)2^{m+M},
 \qquad |\delta|=|U|/3^{m+M}.
\]
Thus \(U\ne0\), \(3^{p+m+M}\mid U\), and the triangle inequality gives \(|\delta|<3\cdot2^{\max(c,d)}(2/3)^m\).

There is also a source-independent verification of noncommutation. The shifted fixed point of a block is \(R(t,b)=2^t(2^b-1)/(2^{t+b}-3^t)\) and has exact dyadic valuation \(t\). Equal fixed points thus force equal ascent length, and cross-multiplication then forces equal \(2^b\) because \(2^t\ne3^t\). All these slopes differ from one, so commuting affine maps must fix each other's unique fixed point. [Valley-block noncommutation, Paper 201](https://rstation.ai/problems/collatz/papers/201)

For clarity, integrality of the tail difference implies \(3^m\mid2^c-2^d\). If \(c\ne d\), the order of 2 modulo \(3^m\) gives \(2\cdot3^{m-1}\le D\). If \(c=d\) the pairs have \(m<M\); the reduced denominator of \((2/3)^m-(2/3)^M\) is exactly \(3^M\), hence \(3^M\mid2^c-1\) gives the same bound. Reducing \(U\) modulo \(3^M\) and removing a power of two gives the second marker \(K=(2^d-2^c)2^m-(2^d-1)3^m\). It is strictly negative because \(2^d-2^c<2^d-1\) and \(2^m<3^m\). Since \(3^M\mid K\) and \(|K|<2^{\max(c,d)+1}3^m\), one has \((3/2)(M-m)<D\).

Each physical tail block increases its shifted landing by its homogeneous gain times a correction strictly less than 2, as proved in the preceding two-block theorem. With the prefix bound and the original terminal floor this gives
\[
 2^{p+m+M+D}<12\cdot3^{p+m+M},\qquad
 D<4+\tfrac35(p+m+M).
\]
Using \(3^p\le|\delta|\), \(3/2<\log_2 3<2\), and \(1/2<\log_2(3/2)<3/5\) gives \(\tfrac32p<2+D-m/2\). Rearranging these inequalities yields
\[
 p<20/3+m/9+2M/3,\qquad M<40/9+2p/3+7m/3.
\]
Substitution gives \(M<16+13m/3\), \(p<52/3+3m\), \(D<24+5m\). Since \(2\cdot3^{m-1}\ge24+5m\) for \(m\ge4\), we obtain \(m\le3,M\le28,p\le26,D\le38\).

The remaining finite test runs over positive \(m,M,p,c,d\) in these bounds with \(m\le M\). It omits \(U=0\), which cannot represent distinct entrances, and keeps the displayed strict power-of-two gain test. For \(m=1,2,3\) the surviving counts are respectively 153,963, 160,218 and 166,119. The corresponding exact maxima of \(v_3(U)-(p+m+M)\) are \(-2,-3,-4\). This contradicts the required divisibility in every case. [Fail-closed integer replay](check_prefix_swap.py) · [Exact controls](../../../reports/unconventional-20261126/PREFIX_SWAP_CONTROLS.json)

**Placement and floor.** A shared suffix is an injective affine map on its prescribed word. A merger at its end would already force equality just after the swapped pair. Thus a source staying above its original threefold shifted floor at every block boundary admits no single adjacent transposition anywhere in its finite block word, irrespective of the common prefix and suffix. Multiple simultaneous changes are outside this conclusion.

A floor only at the end of a common suffix is insufficient. The ordinary source \(19{,}806{,}321\), a multiple of three, executes \((1,1),(1,7),(11,1)\) with landings \(14{,}854{,}741,174{,}079,7{,}528{,}747\). The source \(19{,}806{,}293\) executes \((1,7),(1,1),(11,1)\) with landings \(232{,}105,174{,}079,7{,}528{,}747\). The final height satisfies the original threefold floor, while the shared intermediate landing of 174,079 already breached it. The finite test and this example were run with exact integers. This extension has no additional Lean theorem.
