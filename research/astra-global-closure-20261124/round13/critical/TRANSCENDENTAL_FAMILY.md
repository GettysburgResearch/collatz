# A positive-dimensional compact set of transcendental critical coordinates

**PROPOSED written corollary of PR210, S2.** Put $\alpha=\log_2 3$. The critical record tree in $\mathbb Z_3$ contains an explicit compact set $K$ consisting entirely of elements transcendental over $\mathbb Q$, with

$$\dim_H K=\frac{(2-\alpha)\ln2}{2\ln3}>0.$$

Every point of $K$ has positive ordinary realizations at every finite prefix depth. The construction prescribes backwards odd-gap words. It supplies no fixed ordinary escaping trajectory with a limit in $K$. [PR210, S2, frozen 592328fe](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/SUBSPACE.md) · [Three-place hypotheses and ordinary realization](README.md)

## Explicit scripts

For $i\ge1$ let $p_i=2^i$. Start with the length-$p_i$ prefix of the same infinite mechanical word $b_j=\lfloor j\alpha\rfloor-\lfloor(j-1)\alpha\rfloor$. At each occurrence of `21` wholly contained in that prefix, independently choose whether to exchange it for `12`. The candidate occurrences in the *original* prefix are disjoint. Call the resulting word $V_i$. Use the same chosen word twice, and concatenate

$$ V_1 V_1\, V_2 V_2\, V_3 V_3\,\cdots . $$

Each switch lowers the clock of exactly one interior prefix by one. It preserves the total clock of a full copy. Since $\alpha$ is irrational, every nonempty prefix of a copy has clock strictly below its length times $\alpha$, with deficit less than two in binary-log units. A full copy has deficit less than one. For the concatenated sequence of clocks $S_j$, it follows that $0<j\alpha-S_j=O(\ln(j+1))$ for every $j\ge1$. Thus all prefixes are strictly critical, the script is balanced, and its irrational gap mean excludes eventual periodicity.

The number of gaps before $V_i V_i$ is $r_i=2\sum_{t<i}p_t<2p_i$. The two actual copies therefore meet S2 with the fixed values $w=2$, $L=2$ and unbounded $p_i$. For **every** choice sequence the ternary sum $z=\sum_{j\ge1}3^{j-1}2^{-S_j}$ is transcendental by that theorem. The proof uses no independence assumption on any actual Collatz orbit.

For ordinary realization at depth $n$, write $\beta_j=\sum_{t\le j}3^{t-1}2^{-S_t}$. Choose an odd integer $q>\beta_n$ in the residue class $\beta_n\bmod3^n$. Then the backwards states $y_j=(2^{S_j}/3^j)(q-\beta_j)$ are positive odd integers strictly below $q$, and $3y_j+1=2^{e_j}y_{j-1}$ gives the exact valuations. This uses a separately chosen $q$ for each prefix and does not use the singleton example's special bound $\beta_n<2n/3$.

## Exact ternary scale and dimension

On the binary gap alphabet $\{1,2\}$ the residue of the first term identifies the first gap, since $2^{-1}$ and $2^{-2}$ differ modulo 3. Removing it gives the next tail by $z\mapsto(2^{e_1}z-1)/3$. More generally, if two scripts first differ at gap $j$, their ternary coordinates differ by exactly $3^{j-1}$ times a ternary unit. Thus the first $n$ gaps specify different residue classes modulo $3^n$ whenever their words differ. Agreement through $n$ fixes the residue. The map from switch choices to $\mathbb Z_3$ is continuous, so its image $K$ is compact by compactness of the product of finite binary choice sets.

Let $D(n)$ count distinct free switch bits first exposed in the initial $n$ gaps; a switch is exposed at the first letter of its occurrence in the first copy. There are exactly $2^{D(n)}$ occupied residue balls at this depth. With $d=2-\alpha$, the number of ones in the first $t$ mechanical gaps is $2t-\lfloor t\alpha\rfloor=dt+O(1)$. Two successive ones are impossible since $\lfloor (j+2)\alpha\rfloor-\lfloor j\alpha\rfloor\ge3$. Except for the first one, each one ends one of the available `21` pairs. Consequently a prefix of length $t$ in a first copy exposes $dt+O(1)$ independent choices, uniformly in the copy length and $t$; the two boundary positions cost at most two. A whole double copy exposes $dp_i+O(1)$ choices in $2p_i$ positions. During its second copy none are new. Summing shows

$$D(n)\ge (d/2)n-O(\ln(n+1)),$$

with equality up to the same error at the endpoints of all double copies. Indeed within a first copy the new-bit count has slope $d$ up to bounded error, and within a second it stays at $dp_i+O(1)\ge(d/2)(p_i+t)-O(1)$ for $0\le t\le p_i$.

Covers by the occupied radius-$3^{-n}$ balls at these endpoints give the upper dimension bound. Conversely put independent fair mass on the bits. Every occupied residue ball of radius $3^{-n}$ has mass exactly $2^{-D(n)}$, so for every $s<d\ln2/(2\ln3)$ it is at most $C_s3^{-ns}$. Any nonempty subset of $\mathbb Z_3$ of such a diameter is contained in a ball of that same diameter. Therefore every sufficiently fine cover of $K$ has total $s$-power diameter bounded below by a positive constant, proving the matching lower bound. This is the dimension of this explicit compact subset, and gives only a lower bound for the entire critical trace.
