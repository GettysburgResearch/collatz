# A ternary-unit obstruction to smaller visitors with unequal clocks

**Reconstruction of a prior elementary barrier.** Let $C$ be the shortcut Collatz map on positive integers. Suppose $k,h\ge1$ and
\[
                      x=-1\bmod 2^k,\qquad x=1\bmod3^h .
\]
For every $0\le i\le k$, every positive $z<x$ reaching $C^i x$ at any native clock must use **more than $i+h$ odd departures** before that visit. These two constraints apply to one ordinary source. The visitor has no upper bound on its number of even steps.

The unit barrier is already proved in [PR146, ADJACENT_DESCENT.md, “A congruence that prevents descent”](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/ADJACENT_DESCENT.md). That manuscript also supplies obstructed families whose two arms reach any supplied unit, including 1. [PR211, Theorem D1 and its credit correction](https://github.com/GettysburgResearch/collatz/blob/46da133cff8eb10bfd936656dad23f39b347c168/research/astra-reciprocal-rigidity-20261127/descent/README.md) gives the unified formalization. The proof below is an alternative rational comparison and the displayed family is an explicit terminating control; neither is a claim of priority for the barrier or the existence of terminating examples.

Let $O(u)=(2u-1)/3$ and $E(u)=2u$ be the real affine inverse letters. The initial $i$ native steps from $x$ are all odd, so
\[
 Y=(3/2)^i(x+1)-1,\qquad Y_* = 2(3/2)^i-1 .
\]
The comparison value $Y_*$ need not be an integer. Take a legal inverse path from $Y$ with length $\ell$ and $a\le i+h$ odd inverses, ending at $z$. For $\ell<i$, every inverse word is at least its all-$O$ counterpart as long as the all-$O$ states stay positive. Here $O^\ell Y=(3/2)^{i-\ell}(x+1)-1\ge x$, so $z\ge x$.

For $\ell\ge i$ apply the same affine word to $Y_*$. Through its first $i$ inverse steps every resulting value is at least $O^j(Y_*)=2(3/2)^{i-j}-1\ge1$, using monotonicity and $E(u)\ge O(u)$ on positive $u$. After $j$ inverse letters with $a_j$ odd inverses, the difference between the actual and the comparison values is
\[
                     2^{j-i}3^{i-a_j}(x-1).
\]
For every $j\ge i$ this is an integer, since $a_j\le i+h$ and $3^h\mid x-1$. Thus the remaining comparison path from date $i$ is an ordinary legal positive integer inverse path. At an integer $u\ge1$, any integral $O(u)$ is positive and odd, and $E(u)$ is its positive even inverse. Write $w\ge1$ for the final comparison integer and put $R=2^{\ell-i}3^{i-a}$. The actual source is
\[
                       z=w+R(x-1).
\]
The comparison endpoint is at most $2^\ell3^{-a}Y_*<2R$, since inverse odd letters subtract a positive offset. If $w\ge2$, this forces $R>1$, so $z\ge x$.

If $w=1$, its first $\ell-i$ forward moves are ordinary and end at $1$ or $2$ on the known cycle. The last $i$ forward affine letters, whose virtual states are all at least one, must reach $Y_*$. Write the forward letters as $A(u)=(3u+1)/2$ and $B(u)=u/2$. An $A$ multiplies $u+1$ by $3/2$. A $B$ multiplies it by $(u+2)/(2u+2)$, at most $1/2$ of the all-$A$ factor when $u\ge1$. Starting at $1$, the value $Y_*+1=2(3/2)^i$ requires every one of these last letters to be $A$. Starting at $2$, all $A$ gives $3(3/2)^i$, while any $B$ gives at most $(3/2)(3/2)^i$, so equality is impossible. The initial ordinary part is consequently a whole number $p$ of cycle laps at $1$, followed by $i$ all-odd letters. This gives $R=(4/3)^p\ge1$ and again $z\ge x$. It also handles $i=0$. The asserted obstruction follows.

**Genuinely terminating examples.** For any prescribed $k,h\ge1$, choose an integer $j\ge2k+2$ in the residue class determined by
\[
                 2^j\equiv 2^{1-k}3^k-1\pmod{3^{k+h}} .
\]
The right side is a ternary unit, and $2$ generates the unit group modulo $3^{k+h}$ (equivalently $v_3(2^{2\cdot3^u}-1)=u+1$). Then
\[
                 x=2^k(2^j+1)/3^k-1
\]
is a positive integer with $v_2(x+1)=k$ and $x=1\bmod3^h$. Its first $k$ shortcuts are all odd and end at $2^j$. The next $j$ shortcuts reach $1$. One can take $j<2k+2+2\cdot3^{k+h-1}$. For $h=k$ this upper bound guarantees $k\gg\log\log x$ in the explicit terminating family. Separately, ordinary CRT places a shielded unit in the interval $[2^k3^h,2\cdot2^k3^h)$, without any condition on its later orbit. With $h=k$ these CRT choices have both horizons proportional to $\log x$; that construction alone gives no assurance of later termination. The previously proved [individual mixed-CRT floor](suffix_horizon.md) additionally puts many terminating sources in those individual cells at linear logarithmic precision under its analytic inputs.

Three exact instances show the true prefix and its subsequent halving endpoint. The [integer replay](check_unequal_clock_shield.py) verifies every displayed step and the exact remaining halvings down to 1.

| $k$ | $h$ | $j$ | Initial native states through $C^k x$ |
|---:|---:|---:|---|
| 1 | 1 | 7 | $85,\ 128$ |
| 3 | 1 | 9 | $151,\ 227,\ 341,\ 512$ |
| 2 | 2 | 15 | $14563,\ 21845,\ 32768$ |

Paper 1, Theorem 6, excludes smaller sources through $r+k$ odd depths along a wider permitted family of $\{1,2\}$ words when $3^k$ divides the original source. It also gives a shifted nonunit family and examples where advancing the original endpoint produces a later meeting. Mahler's Paper 148 treats general valuation words, including ternary shielding and families that remain minimal through all matched and shallower odd depths. The argument here uses units close to $1$ in base three, a virtual rational comparison and all-odd original prefixes. Its conclusion concerns any native visitor clock through the supplied initial endpoints. [Weaver, Paper 1, Theorem 6 and Proposition 9](https://rstation.ai/problems/collatz/papers/1) · [Mahler, Paper 148 v1, §§1–2](https://rstation.ai/problems/collatz/papers/148/v1)

For a fixed proposed bound on the visitor's extra odd departures one can choose $h$ to exceed that bound, and $k$ to cover any supplied finite horizon on the original path. General unequal-clock descent is compatible with the obstruction. The explicit terminating family eventually reaches $1$, where the smaller source $1$ is present at time zero.
