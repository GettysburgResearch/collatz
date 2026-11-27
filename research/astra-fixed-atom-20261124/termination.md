# An adaptive ordinary descent attempt at a fixed source

The attempted termination argument uses exact moves in the ordinary component graph and chooses the next comparison from the *actual integer*. Its affirmative result is a bounded way to reach a state with a smaller partner. The smaller partner is below the **reached state**. The comparison with the original source, needed for termination, fails in the fixed-input test below.

## Shifted integers and the two choices

Write \(a=n+1\), so the positive ordinary shortcut sends an even \(a\) to \(3a/2\), and an odd \(a\) to \((a+1)/2\). Thus \(2x\sim3x\), and \(2x-1\sim x\) whenever the corresponding positive ordinary starts exist. Here \(\sim\) means the shifted states have common ordinary future. For even \(a\ge2\), another exact identity is \(a\sim4a-2\): the latter goes to \(6a-3\), then \(3a-1\), then \(3a/2\), which is the immediate image of \(a\).

Factor a shifted integer into powers of two and three and its remaining positive cofactor. Interchanging one factor of two with one of three preserves its component. If the total exponent \(h\) is positive, the least representative is the even ternary unit \(a=2^h u\), \(\gcd(u,6)=1\). Its other representatives are \(x_i=2^{h-i}3^iu\). If the total exponent is zero, successive odd shifted halvings \((x+1)/2\) decrease until a representative of positive total exponent is reached.

The resulting forward map \(F\) on canonical representatives first runs from \(a\) to its odd representative \(3^h u\); it next takes \(z=(3^h u+1)/2\), and if \(z\) is odd takes one more such halving. In this latter case the result \((3^h u+3)/4\) is divisible by three. Finally replace all factors of three by factors of two. This is an exact component transition. The replacement itself can point backward in the ordinary graph.

For completeness, the full positive-height canonical predecessors are explicit. Let \(j=v_3(2a-1)\). There is a predecessor \(p_0=(2/3)^j(2a-1)\) when \(j>0\). There is always \(p_1=2(2/3)^j(2a-1)\), and for \(2\le i\le h\) there is \(p_i=2^{h-i+3}3^{i-1}u-2\). To see completeness, reverse the odd shifted halvings from \(x_i\) until the first odd shifted value divisible by three. For \(i=0\) this occurs immediately when \(a\equiv2\bmod3\), and never when \(a\equiv1\bmod3\). For \(i\ge1\) it occurs at \(4x_i-3\), after two reverse halvings. Canonicalizing these odd endpoints gives the displayed list. Every side parent \(i\ge2\) is \(1\bmod3\).

Call a canonical representative critical when \(a\equiv2\bmod3\), and write \(a=6k+2\). At \(k=3m\) or \(3m+1\) the exponent \(j\) is one. Of the two parents \(p_0,p_1\), one is critical; alternatively, use the other parent \(p\) and its critical neighbor \(4p-2\). In the \(k\) coordinate the exact choices are
\[
 3m\longrightarrow 4m\ \text{or}\ 32m+2,\qquad
 3m+1\longrightarrow 8m+3\ \text{or}\ 16m+6 .
\]
At \(k=3m+2\), \(2a-1=9(4m+3)\), so replace two factors of three by two factors of two. This gives the same-component positive state \(b=16m+12<18m+14=a\). This contraction does not require knowing the full ternary valuation.

**Theorem.** Every critical input \(6k+2\) can steer in at most three of the displayed choices to a critical \(6z+2\) with \(z\equiv2\bmod3\), then obtain a positive same-component \(b<6z+2\).

**Proof.** The residues for which *every* choice misses the target throughout the first \(d\) states are, in order for \(d=1,2,3,4\),
\[
 \{0,1\}\pmod3,\quad\{1,3\}\pmod9,\quad
 \{21\}\pmod{27},\quad\varnothing\pmod{81}.
\]
To compute each line, take each non-target residue at the new precision and retain it exactly when both successors belong to the preceding line. A switch consumes at most one ternary digit of precision, so each line applies to every nonnegative integer, including fixed ordinary inputs of arbitrary size. The Lean theorem **steer_to_smaller_neighbor** combines this periodicity and finite check with a bounded route and proofs of component preservation and strict local size decrease.

## The original floor survives arbitrary inverse depth

For \(n=703\), every forward endpoint \(T^i(703)\) at \(0\le i<81\) has **no** smaller positive ordinary ancestor at any depth. The first possible smaller-source contact is \(T^{81}(703)=628\). In particular an unlimited inverse search after any of those 81 endpoints cannot pay the earlier growth relative to 703. This source converges; it tests the candidate mechanism on an actual input.

In the quotient the same original source is \(a=704\), already critical. For every \(0\le i<22\), no canonical source \(b<704\) reaches \(F^i(704)\) by any number of directed quotient transitions. The first contact is \(F^{22}(704)=140\). This is a statement about the directed quotient map, distinct from its symmetric component closure.

The finite verification follows every positive smaller start forward, stopping at the first state already in the accumulated union. The result contains all smaller starts and is closed under the appropriate forward map. It therefore contains every forward iterate of those starts, and its first intersection with the specified source proves the all-inverse-depth assertion. The companion Python program checks these complete forward unions and both first contacts, and independently computes the four steering tables. The fixed-source computation does not bound what can happen after the stated clocks.

I also tested a reserve designed to pay for a growing run on a fixed finite input. For the physical canonical step \(L(a)=(9a+4)/8\), \(L(a)+4=9(a+4)/8\), so each consecutive such step spends one unit of \(v_8(a+4)=\lfloor v_2(a+4)/3\rfloor\). The reserve can refill before the original floor is crossed. For any \(H\ge1\), choose positive odd \(u\) prime to three with \(v_2(3u+1)=3H+3\); such a residue exists by the Chinese remainder theorem. The shifted start \(8u\) moves through its odd representative \(27u\) to the canonical \(a'=(27u+1)/2>8u\), while \(a'+4=9(3u+1)/2\) has binary valuation \(3H+2\). The old reserve was zero. The next \(H\) canonical steps are all \(L\): at each such input \(v_2(a)=2\) and \(a/4\equiv3\bmod4\), as follows from the remaining valuation of \(a+4\) being at least five. This example changes the source with \(H\); the separate 703 computation is the single-source test.

Neither the reserve nor the adaptive choices establish a return below the original minimum on every putative nonconvergent path. The earlier half-size merger at the first run, when \(3^hu\equiv1\bmod4\), is recorded in [PR196](https://github.com/GettysburgResearch/collatz/blob/27d03cfe902660e06604eb55bb28ca3d2754ff48/research/astra-orbit-cycle-20261124/mergers/TWO_ANCHOR_MERGERS.md). No new claim about termination of the full mixed-base rewriting system is made here.
