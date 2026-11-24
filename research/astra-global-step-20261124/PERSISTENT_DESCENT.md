# One smaller ordinary orbit through repeated paid clusters

**Status. Two positive infinite-language theorems checked by Lean. All-input descent remains open.** The input is the ordinary shortcut map, with odd-gap blocks $L=(2,1)$ and $P=(1,4)$. PR192 at `d2081d1cd2410e6004eaee9f9b13c5553afaf3f4`, `research/astra-closure-attack-20261124/DESCENT.md` and `DESCENT_EXTENSION.md`, supplied a six-separated shadow and individual mergers with an unrestricted suffix. Its five-block code left PPLLL, PLLPP and PLLPL. PR188 at `f98262be4ea40068dc88c779a767a9400a8bcaa3` supplies the earlier global-bridge boundary. The new proof keeps one smaller starting integer through indefinitely many interacting paid returns.

## Ordinary coordinate and literal steps

Write $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Set $x=(q+7)/2$ at an original odd boundary. Then
$$
 L: 8x'=9x,\qquad P: 32x'=9x+83.
$$
Equivalently $8q'=9q+7$ and $32q'=9q+5$. If $q$ and $q'$ are odd, these equations force $q=9\bmod 16$ and $q=3\bmod 64$, respectively. For $q=16t+9$ the two odd successors are $12t+7$ and $18t+11$, with exact gaps $2,1$. For $q=64t+3$ they are $96t+5$ and $18t+1$, with exact gaps $1,4$. The first odd intermediate at an L is $(3q+1)/4$, and at a P it is $(3q+1)/2$. An infinite original input cannot reach one, whose subsequent odd gaps are all two.

## A single shadow for arbitrary mixtures of single and double paid clusters

**Theorem.** Suppose each maximal run of P letters has length one or two. Between a single P and the next paid cluster require at least four L's. Between a double P and the next paid cluster require at least five L's. At every odd phase of any actual positive infinite input satisfying this rule there is a smaller positive odd integer which never reaches one. There is no restriction on the initial light run or on the order of the two cluster types.

At a checkpoint with at least three L's before the next paid cluster, put
$$
 U=(q+7)/256,\qquad Y=157U-5.
$$
The graph uses the words $L$, $L^3PL$, and $L^3P^2L^2$. It places the three leading lights immediately before the paid cluster, the required one or two trailing lights immediately after it, and uses free L edges for all excess lights. At *every* graph checkpoint the next three source letters are L, even across graph edges. Thus $8^3 x_{i+3}=9^3x_i$ at the corresponding three original block steps, $512\mid x_i$, and $U=x_i/128$ is a positive multiple of four. In particular $Y$ is odd and at least 623. The original boundary and its first light intermediate are $256U-7$ and $192U-5$, both strictly above $Y$.

For each core with $n$ blocks and $A$ shortcut clocks, write $2^A U'=9^n U+E$. The following ordinary representatives determine all lifts.

| Core | $A$ | $E$ | $U$ | $U'$ | Target shortcut bits, chronological |
|---|---:|---:|---:|---:|---|
| $L$ | 3 | 0 | 8 | 9 | 110 |
| $L^3 P L$ | 17 | 2988 | 35380 | 15939 | 11111001111000010 |
| $L^3 PP L^2$ | 25 | 1102572 | 27147444 | 3869694 | 1111100010111100100110010 |

The two nontrivial representatives are canonical modulo $2^A$, by coprimality of $9^n$ and $2^A$. On L use 8 as the least positive representative. The target trajectory from $157U-5$ has exactly $2n$ odd inputs in $A$ clocks and ends at $157U'-5$. On replacing the representative by $U+2^At$, all target bits persist, its initial value increases by $157\cdot 2^At$, and its final value increases by $157\cdot 9^nt$. Thus every row transfers *the same ordinary comparison orbit*. Graph clocks strictly increase, and the comparison orbit visits values at least 623 indefinitely. It never reaches one. This gives the initial smaller source even if future original boundaries grow arbitrarily far above the initial floor.

The displayed theorem in [ClusterShadow.lean](ClusterShadow.lean), `Collatz.ClusterShadow.singleton_doublet_descent`, proves the graph-checkpoint assertion from the raw positive equations. The following initial-phase completion is a written deduction. If at least three L's remain before a paid cluster, one may start a graph walk at that boundary. With $r=0,1,2$ remaining L's, use the original boundary just after the next P instead. More generally this comparison works for $0\le r\le4$. It equals
$$
 Q=\frac{9(9/8)^r(q+7)-58}{32}.
$$
For $q\ge5$, the bound $(9/8)^4<13/8$ gives $256Q<117q+355<192q+64$, hence $Q<(3q+1)/4$, and this also beats the larger paid intermediate and the original boundary. Every boundary on an infinite positive L/P input has $x\ge13$. Indeed $0<x\le12$ and a first legal letter force $x=5$ or 8, leading to 4 or 9, neither of which admits a second letter. An all-L tail is impossible since $8^h\mid x$ for all $h$. These checks cover a cut in a doublet and an initial partial light run.

For a nontrivial example, take any succession of singletons and doublets, each followed by 30 L's. It includes arbitrary adjacent-P defects and its macro multipliers (even for the doublet) exceed one. The conclusion is conditional on an actual infinite positive ordinary realization.

## Two other persistent comparison states

A second graph carries $x-10$ in mode A and $x-7$ in mode B. A free L is allowed at either state. In the table $L^{\ge j}$ means the listed minimum followed by any number of free L's.

| Initial mode | Word | Final mode |
|---|---|---|
| A | $PPLLLP L^{\ge5}$ | B |
| A | $PPLLLLP L^{\ge4}$ | B |
| B | $PLLPPLPP L^{\ge9}$ | A |
| B | $PLLPLPP L^{\ge6}$ | B |
| A | $PLLPLLPLLPP L^{\ge9}$ | A |

Each of PR192's three residual five-letter prefixes can start a transition. The return test uses $x$ directly and the same cylinder proof. At each checkpoint the target is $x-10$ or $x-7$, hence at least three. The initial source is below both original starting floors. It may be even. The Lean proof extracts a positive odd part, reached by initial halvings, that inherits nonconvergence and the strict inequalities. Arbitrarily many A-to-B and B-to-A changes keep the *original* comparison orbit. In particular the core containing $PLLPLPP$ permits repeated gaps of one or two L's inside a cluster, beyond the singleton/doublet spacing theorem. [Renewal.lean](Renewal.lean), `Collatz.PaidRenewal.persistent_descent`, proves the assertion at any graph checkpoint. An arbitrary cut inside the fixed core either lies at a P or has at most four L's before the next P, where the preceding direct comparison applies. In the trailing light run the remainder may be read as free L's in the exit mode. This extends the comparison to every odd phase of a walk in this language.

A signed calculation found the cores. If $X=(q+7)/2$, the comparison at a paid entry is $3^kX-z$, and the next $P L^s$ ends at $X'$, initialize a signed rational trajectory at $-z-83\cdot3^{k-2}$. All denominators are odd. If its first $5+3s$ shortcut clocks have $h$ odd inputs and terminal value $-z'$, the ordinary target ends at
$$
 3^{k+h-2-2s}X'-z'.
$$
Indeed the initial ordinary target differs from the signed rational by $2^{5+3s}3^{k-2-2s}X'$. Their parities agree for the indicated clocks and each odd step contributes one factor of three to the eventual difference. This gives an exact state update, including negative $k$ whenever the initial comparison is integral. A signed trajectory entering the negative length-three cycle has two odd visits per three clocks, which permits a reset independent of excess $s$. On the negative length-eleven cycle through $-17$, 33 clocks have 21 odd visits; the relative exponent decreases by one per eleven extra light blocks. There is no proved reset or maintained lower bound for the ensuing paid return from every such state.

## Coverage boundary and verification

For the first graph and a cut at a cluster start after an available three-light prefix, its exact tail language is the singleton/doublet spacing rule. Its complement contains a run of three P's, two successive clusters with too few intervening L's, or no required initial alignment. The phase comparisons above remove the alignment condition for globally compliant scripts. For the second graph the exact language is the infinite paths of its displayed labeled two-state graph, with a free L self-loop at both states. A word is outside this language when neither initial mode permits an infinite matching path. Equivalently some finite prefix has no matching path in the finite graph obtained by expanding each fixed core into single-letter edges, by finite branching. Thus finite cylinders, variable delays and the persistence of the initial target are distinguished.

For instance $L^r(PP L^3 PP L^{50})^\omega$ fails both displayed graph tests. The first doublet is followed by three light letters. In the two-state graph only A can start with PP; its only matching candidate consumes $PPLLLP$, and the subsequent P violates the required padding. Each full period has multiplier $(9/8)^{53}(9/32)^4>1$. Arbitrarily long finite prefixes have positive ordinary lifts since every finite shortcut parity word has its dyadic residue class and the endpoint may be constrained odd by one further bit. This example tests the languages; the infinite word has no asserted positive realization and other merger families may apply to its prefixes.

**The unresolved implication** is that every actual positive L/P orbit containing a global least nonconverger carries a smaller ordinary source from its *initial* floor. Neither graph is forced on an arbitrary such orbit. General odd gap words also need coverage beyond this alphabet. The generic theorem `affine_return` transports an individual certified nonnegative-carry affine equation for arbitrary counts; it does not furnish the missing certificates.

Lean 4.34.1 (release `5045d0056413266e57c625dcd7c365b10e377c52`) and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612` checked both files with `-j1 -DwarningAsError=true`. Build `Renewal.olean` first and put its directory on `LEAN_PATH` when checking `ClusterShadow.lean`. Seven printed transitive axiom inventories contain only `propext`, `Quot.sound` and, on some declarations, `Classical.choice`. The source SHA-256 hashes are `81f477421fbac9289dbf1f9396f300c29da433aa6b0d58e7f1847e39fe0f3e7f` and `8728518402782893b6f16098b4ebab34e87cba692c5ae69afa56bbd9e62d4269`. [renewal_controls.py](renewal_controls.py) replayed 70 ordinary lifted comparisons in normal and optimized Python. An independent calculation reconstructed both mixed-cluster canonical bases and literal target words.
