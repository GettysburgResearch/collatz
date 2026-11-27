# What a prescribed tower exponent can evade

**PROPOSED.** For every deadline $H$ and lower exponent bound $L$, there is an actual $r=3m+1\ge L$ such that $3^r$ misses **every** earlier power of three through $H$ ordinary shortcuts on each arm. The clocks may differ. In a second construction, the parity-prefix condition imposed by a first bad tower admits at least $2^k$ distinct words of length $8+3k$. Every finite word in this family occurs at cofinally many pure powers with exponent $3m+1$.

Both theorems concern the ordinary shortcut $T(2v)=v, T(2v+1)=3v+2$. The exponent restriction is the rank-one slice from PR192, where $Z_m=(2^{6(m+1)}-1)/9$ and the orbit of $Z_m$ reaches 1 precisely when the orbit of $3^{3m+1}$ does. The results here do not exhibit an actual first bad exponent. [PR192 at 570476be, rank-one characterization and physical merger](https://github.com/GettysburgResearch/collatz/blob/570476be82f706122cdd23ebd7a00f3d4ff90cd8/research/astra-ultra-closure-20261125/bridge/README.md)

## All earlier powers, at both clocks

Let $H\ge2$, $24^H<3^r$ and $2^H\mid 3^r+5$. Then, for all $s<r$ and $i,l\le H$,
$$
                       T^i(3^r)\ne T^l(3^s).
$$
The proof uses exact unsigned affine coefficients. For a word of length $t$ with $p$ odd inputs write its affine map as $(A x+B)/Q$, with $A=3^p, Q=2^t$. Every word satisfies $0\le B\le3^t$ and $A\le B+Q$. The latter inequality follows by applying its affine maps to the real input $-1$, since both branches preserve $[-1,\infty)$.

Suppose the two positive orbits meet. Put $M=3^s$ and $k=3^{r-s}$. Each shortcut on a positive input lies between half and twice that input. Therefore $3^r\le4^H M$, whence $6^H<M$. Scale the two affine formulas to denominator $2^{i+l}$, with numerators $a kM+e$ and $b M+f$. Both carries satisfy $0\le e,f\le6^H<M$. Equality forces $e=f$ and $ak=b$. Consequently the very same two affine words would give equal **real** values on $-5$ and $-5/k$. This conclusion follows from equality of the complete affine functions after input scaling.

The actual upper word shadows the signed cycle $-5,-7,-10,-5$ through its given clock, since the starting inputs agree modulo $2^H$. Its signed value is at most $-5$. For $k\ge9$, both branches keep the lower reference in $[-1,\infty)$. For $k=3$, $M\equiv1\pmod4$, so its actual word begins odd, even whenever it has length at least two. Those steps send $-5/3$ to $-2$ and then $-1$. At every admitted clock the lower reference is at least $-2$. This contradicts the affine equality.

For $H,L\ge0$ the construction gives such an obstruction in the explicit exponent window
$$
  6(H+L+3)+1\le r\le6(H+L+3)+1+6(2^H-1),\qquad r\equiv1\pmod3 .
$$
The actual divisibility in this construction is even $2^{H+3}\mid 3^r+5$. To lift the congruence by one bit, either keep the exponent or increase it by $6\cdot2^j$, since $3^{6\cdot2^j}=1+2^{j+3}(2u+1)$ for some $u$. Squaring proves the latter identity inductively. The initial exponent exceeds the required size threshold. In particular, a universal fixed deadline already fails at base one on the specified rank-one slice. [Kernel proofs of the pointwise exclusion and exponent window](TowerDeadline.lean)

## Exponential branching under the maximum-weight condition

For a first bad $3^rw$ over its least base, every prefix through clock $r$ must have maximum odd count among words of the same length and carry. A heavier word with the same carry would give a physical merger at the earlier exponent $r-d$, where $d$ is its weight advantage. PR195 also rules out every literal lower-base meeting through $H$ if $2H\le r$ and this maximum condition holds through $H$. [PR195 at 5b2bdcb6, criterion and its exact quantifiers](https://github.com/GettysburgResearch/collatz/blob/5b2bdcb6e4e60da15c29eadff8bd08b3991c5b57/research/astra-global-closure-20261124/round10/closure/README.md)

Start with the chronological parity bits $11011111$. Append any sequence of blocks $110$ and $111$. At every prefix of every resulting word the odd count is maximal even among words of arbitrary length whose carry is **at most** the given carry.

Write $A=3^p$, $Q=2^h$ and $B$ for the prefix data. Every word of weight $q$ has carry at least $F(q)=3^q-2^q$. Indeed, moving any odd letter left over an even letter can only decrease its contribution to the carry. Equivalently, the recursion $F(q+1)=3F(q)+2^q$ and the bound $q\le h$ prove this directly. For $p\ge2$, $F(p+1)>2\cdot3^p$. Thus $B\le2A$ keeps out every heavier competitor.

At the end of the eight-bit seed, $(A,Q,B)=(2187,256,2903)$, so $B+5Q\le2A$. This stronger inequality survives every whole block. The update for $110$ is $(9A,8Q,9B+5Q)$. For $111$ it is $(27A,8Q,27B+19Q)$. A single appended odd letter also preserves it, covering both partial blocks. In the initial seed the first two letters already have full weight. After $110$ and $t$ further ones the carry is $13\cdot3^t-8\cdot2^t<2(9\cdot3^t)$, covering each remaining initial prefix. Distinct block choices give distinct words. Injectivity and the bounds for every complete and incomplete appended block compile in Lean. [Kernel proof](MaximalWords.lean)

The finite ordinary attachment uses the binary parity-word bijection. A supplied $h$-bit word determines one residue modulo $2^h$. To verify the induction, adding $2^h$ to the start preserves the first $h$ bits and adds $3^p$ to the endpoint there. Exactly one of the two lifts has the requested next bit. In our family, the first three bits $110$ give residue $3\pmod8$. Let $c$ be a positive additive offset taking the required residue to zero modulo $2^h$. Then $c\equiv5\pmod8$. The same exponent lifting proved in `TowerDeadline.lift_class` supplies $3^r+c\equiv0\pmod{2^h}$ with $r\equiv1\pmod3$ and arbitrarily large $r$. This is a single ordinary source realizing each prescribed finite word. The binary coding attachment now compiles through the actual parity trace at the pure power for every supplied block sequence and exponent floor. The following count is a written consequence. [Ordinary binary attachment](PowerRealization.lean)

At $h=8+3k$ there are exactly $2^k$ such residue classes. The powers $3^{3m+1}$ have period $2^{h-2}$ modulo $2^h$ and are distinct across each period. Indeed $27\equiv3\bmod8$, and $27^{2^{j+1}}=3^{6\cdot2^j}$ differs from one by exactly $j+3$ binary factors, as in the exponent lift. Each of the $2^k$ classes occurs, hence exactly $2^k$ indices per full period realize this family. For $M\ge256$, take $k=\lfloor(\log_2 M-8)/3\rfloor$. A block of $M$ consecutive indices then intersects only a bounded number of periods, and at most $O(M^{1/3})$ indices in it realize the prescribed family through $h$ clocks. This count concerns the displayed family alone.

## First unsupported step

For the supplied first bad exponent $r$, the induction needs an actual merger with an earlier power at this same base, or with a power over a smaller positive base. The 116-exponent simultaneous lower-base result supplies other bases in long ordinary intervals, while a merger may have to wait beyond any preassigned pair of deadlines already at $w=1$. The prefix maximum requirement itself permits exponential branching and aperiodic symbolic completions. Every finite prefix having large ordinary power representatives does not provide one exponent whose orbit follows an infinite such path, or even a path of that exponent's own length. Establishing a source-dependent mandatory exit or merger at the prescribed $r$ is open. [PR209 at 2d0230aa, simultaneous lower-base coverage](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/fixed_source/README.md)
