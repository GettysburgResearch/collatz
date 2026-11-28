# Rational mergers at every ternary unit and unmerged positive integer lifts

**Proposed theorem.** Use the shortcut map $T(x)=x/2$ on even inputs and $(3x+1)/2$ on odd inputs, also defined on rationals of odd denominator by their numerator parity. All ordinary sources below are positive odd integers, paired with their triples. If the allowed combined odd grade is $G$, the largest possible unmerged native clock satisfies
$$
 \liminf_{G\to\infty}\frac{K(G)}{G\log_2 G}\ \ge\ \frac12.                 \tag{1}
$$
The proof constructs a common periodic rational trajectory with one odd departure in **every** prescribed period $L\ge3$. More generally the possible rational states of physically realized unequal-slope mergers are exactly the reduced fractions $u/q$ with $q>0$ odd and $3\nmid uq$, of either sign. A merger here means that an odd rational $s_*$ and its triple have different affine slopes on their two prefixes of the same length and end at the same state. The corresponding ordinary positive lifts remain separated for any prescribed length afterward. The ordinary starting source may vary with that length.

## Affine relations on native cylinders

A realized oriented relation $(j,a)$, $j\ge0$, means that at a positive native date $t$, on an entire nonempty odd-source residue class modulo $2^t$, the actual states satisfy $B=3^j A-a$. The orientation chooses either ordering of the two physical arms and stays in force until explicitly exchanged. The coefficient $3^j$ is their true affine slope ratio. If $A$ is on the original lower arm then $j=h+1-g$ for the two grades $(g,h)$. Within the cylinder $A$ varies by an odd multiple of the source class parameter. In particular one can prescribe any subsequent native word on $A$ by further refinement. In particular every finite refinement has infinitely many positive ordinary starting sources. At every positive ordinary integer representative of the cylinder both states are ternary units after their first departure, because both initial inputs are odd. This fact about the cylinder supplies the integer constraint on $a$ even when a special rational input has denominator divisible by 3. For $j>0$ this forces $3\nmid a$.

The following four letters record forward refinements. The oddness of $a$ decides whether opposite parities are possible, and each indicated parity of $A$ can actually be chosen.

| Letter | Parities of $(A,B)$ | Next $(j,a)$ |
|---|---|---|
| U | even, odd | $(j+1,(3a-1)/2)$ |
| D | odd, even, $j\ge1$ | $(j-1,(a+3^{j-1})/2)$ |
| E | even, even | $(j,a/2)$ |
| O | odd, odd | $(j,(3a+3^j-1)/2)$ |

After the mandatory first odd departure from $(s,3s)$ the relation is $(1,1)$. A D then gives $(0,1)$, from which a U recovers $(1,1)$. A negative unit translation occurs physically at $s=7,t=11$: the states are $1,2$, with grades $5,4$. Thus $(0,-1)$ occurs in the original orientation.

## The contracting finite cover

For a length-$t$ native word $W$ with odd positions $0\le i_1<\cdots<i_p<t$, write
$$
 C_W=\sum_{k=1}^p 2^{i_k}3^{p-k},\qquad T_W(X)=(3^p X+C_W)/2^t.
$$
The congruence $2^t\mid 3^p X+C_W$ characterizes the word cylinder. Indeed every word has exactly one residue, by induction choosing either parity at each step, and the displayed congruence has exactly one solution modulo $2^t$.

The finite fact used in the proof is the following integer inclusion:
$$
 \left\{(C_W-C_V)\bmod 19683:\ 
   |W|=|V|=14,\ |W|_1=|V|_1=9,\ |C_W-C_V|\le38740\right\}
       =\mathbb Z/19683\mathbb Z.                                           \tag{2}
$$
The [reproducible certificate](check_universal_mergers.py) verifies (2) in two ways. One enumerates the $\binom{14}{9}=2002$ increasing position tuples and marks residues of their signed differences. The other iterates the offset recursion over binary masks, then takes cyclic rotations of a residue bitset in signed-difference ranges. The check records the exact limiting magnitude and verifies it against the neighboring smaller bound. Only finite integer operations enter (2).

Suppose the equal-slope translation $B=A-b$ is realized. For any target $a$, append the lower word $W$, upper word $V$ whenever
$$
                  3^9 b=2^{14}a-C_W+C_V.                                \tag{3}
$$
Prescribing $W$ on $A$ fixes a refinement. Equation (3) gives $3^9(A-b)+C_V=(3^9A+C_W)-2^{14}a$, hence the upper word is exactly $V$ and the terminal translation is $a$.

For $a\ge12$, choose (2) in the residue of $2^{14}a$. The integer $b$ in (3) satisfies $0<b<a$, since $2^{14}\cdot12>38740$ and $(3^9-2^{14})\cdot12>38740$. The following paths from $(1,1)$ give the remaining translations. Each row is verified by the four transitions above; no search assumption is needed.

| $a$ | Path | $a$ | Path |
|---:|---|---:|---|
|1|D|7|UDOODOOUD|
|2|UDOODE|8|UUUDOOODDDE|
|3|UDOODEO|9|UDOODOO|
|4|UDOOD|10|UUUDOOEODDD|
|5|UUUDOOEODDDE|11|UUDUUODUDODOODEODE|
|6|UDOODO| | |

Consequently all positive translations are realized starting even from $(0,1)$. Swapping arms at $(0,-1)$, performing the same construction and swapping them back realizes all negative translations. Translation zero also occurs, for instance from $s=23$ at $t=5$, where both states are 20 and the grades are 3 and 2. Realizing a translation of absolute magnitude $m$ costs $O(\log(2+m))$ native steps with an absolute implied constant. For $m\ge64$, (3) gives $b/m\le(16384+38740/64)/19683<0.87$; the remaining distinct decreasing positive integers below 64 require bounded cost.

## All positive slope gaps and all rational centers

Take $j\ge1$ and a signed integer $a$ prime to 3. Choose $1\le e\le6$ with $2^e a\equiv2\pmod9$; 2 generates the units modulo 9. Then $b=(2^e a+1)/3$ is an odd ternary unit with the sign of $a$. Starting at $(j-1,b)$, one U followed by $e-1$ E steps gives $(j,a)$. Repeating the inverse construction lowers the level to zero, where every signed translation is already available. Its terminal absolute translation is at most $64^j(|a|+1)$, for example by bounding each one-step $|b|+1\le64(|a|+1)$. Thus every target relation costs
$$
                             O(j+\log(2+|a|))                            \tag{4}
$$
native steps. This gives the exact affine relation classification in either orientation: arbitrary integer translations at equal slope, and precisely the ternary-unit translations at each positive normalized slope gap. To start the construction in the reversed orientation use the two signs of the unit translation, which were realized in the original orientation.

Now take a reduced fraction $z=u/q$ with $q$ odd and $3\nmid uq$. Choose a positive $j$ with $3^j\equiv1\pmod q$ (use $j=1$ for $q=1$), and put $a=(3^j-1)z$. This is a signed ternary-unit integer. Realize $(j,a)$ in the original orientation. At the intersection of its affine line with $B=A$ both states equal $z$. The preimage on the lower affine branch is $s_*=(2^t z-C_W)/3^g$. It has odd denominator and lies in the specified source cylinder, by the modulo-$2^t$ characterization above. Therefore its triple genuinely realizes the upper word as well. The rational endpoints may first coincide at an earlier date. On the common subsequent word the slope ratio stays fixed, so the first merger also has unequal slopes. Conversely, a merger at positive date with unequal slopes can be oriented with normalized positive gap $j$. The physical cylinder gives $(3^j-1)z=a$ for a ternary unit $a$. Together with the odd denominator of actual 2-adic rational states, this proves the necessity.

For any post-entry length $k$, positive integer lifts $s\equiv s_*\pmod {2^{t+k}}$ realize both prefixes and the next $k$ common parity symbols of the rational trajectory. Choose $s\ne s_*$. The two lifted states differ at date $t$ by the unequal slopes, so determinism excludes any earlier intersection at the **same** date. Their difference after $t$ remains nonzero along the common word. This copies the future itinerary of any rational ternary unit on a synchronously unmerged pair of actual ordinary trajectories for every finite horizon.

## A logarithmic factor in the worst unmatched clock

For $L\ge3$ choose $q=2^L-3$, $z=1/q$, and $j=\operatorname{ord}_q(3)\le q$. The numerator cycle starts $1,2^{L-1},2^{L-2},\ldots,2,1$, with one odd departure per $L$ native steps. Since $a=(3^j-1)/q$ has $\log(2+a)=O(j+1)$, (4) supplies an entry time $t=O(2^L)$ and combined entry grade $G_0\le2t=O(2^L)$, with absolute constants. Every $R\ge1$ gives positive unmerged integer lifts with native clock $t+LR$ and combined grade $G_0+2R$.

Define $K(G)$ as the largest native clock with positive odd $s$, distinct $T^i(s),T^i(3s)$ for all $0\le i\le k$, and combined grade at most $G$ through date $k$. The earlier [physical determinant bound](PAIRED_SOURCE_GRADES.md) makes this maximum finite. For each sufficiently large integer $G$ put $L=\lfloor\log_2 G-2\log_2\log_2G\rfloor$ and $R=\lfloor(G-G_0)/2\rfloor$. Then $L/\log_2G\to1$, $G_0/G\to0$, and $R/G\to1/2$. This proves (1). In conjunction with the [ordered discrepancy theorem](SPARSE_DISCREPANCY_BLOCKS.md), the bounds now run from $(\tfrac12-o(1))G\log_2 G$ to $o(G^2)$. They concern the worst positive source at each budget. They leave convergence of every fixed positive source open.
