# The complete unmatched clock reduces to one ordered carry equation

**Proposed theorem.** Let $K(G)$ be the largest $k$ for which a positive odd $s$ satisfies $T^i(s)\ne T^i(3s)$ at every date $0\le i\le k$ and the two shortcut prefixes have total odd grade at most $G$. Let $M(P)$ be the largest $L$ for which there are an integer $1\le p\le P$ and two increasing calendars
$$
 0\le u_1<\cdots<u_p<L,\qquad 0\le v_1<\cdots<v_p<L
$$
satisfying the single static integer equation
$$
 \sum_{i=1}^p3^{p-i}(2^{u_i}-2^{v_i})=2^L-3^p.                         \tag{1}
$$
Use zero for an empty maximum. For integer $P\ge1$, $G\ge2$,
$$
       M(P)+2\le K(2P+3),\qquad K(G)\le M(16(G+1)).                    \tag{2}
$$
Consequently $K(G)=O(G\log(2+G))$ if and only if every solution of (1) has $L=O(p\log(2+p))$. This captures arbitrary unmerged finite schedules, including ones without periodic blocks. It is independent of the finite covering calculation in [the universal rational merger theorem](UNIVERSAL_RATIONAL_MERGERS.md).

The same upper bound on $K$ is equivalent to an assertion about **positive rational cycles**: every pair of adjacent periodic shortcut phases $z,z-1$, over rationals of odd denominator, has $L=O((p_1+p_2)\log(2+p_1+p_2))$ at a common period $L$ with respective odd grades $p_1,p_2$. It suffices to test the subfamily with $p_1=p_2$. Arbitrary equal multiples of a common primitive pair period are allowed.

## Physical meaning of the equation

Write $C_U=\sum3^{p-i}2^{u_i}$ and similarly for $C_V$. The respective forward word maps are $(3^p A+C_U)/2^L$ and $(3^p B+C_V)/2^L$. Equation (1) says that the initial relation $A-B=1$ is carried to itself on the entire pair of word cylinders. To see physical compatibility, prescribe the lower word $U$ on $A$; the divisibility $2^L\mid3^p A+C_U$, combined with (1), gives $2^L\mid3^p(A-1)+C_V$. The unique word residue for $V$ therefore supplies its actual branches.

The source cylinder $s\equiv3\pmod4$ starts with OO on the lower arm and OE on the upper arm. At date two,
$$
              A=(9s+5)/4,\qquad B=(9s+1)/4=A-1 .
$$
As $s$ runs through this odd-source class, $A$ runs through every residue modulo every power of two. Append $U,V$ as above. The endpoints differ by one, excluding any earlier same-date merger by determinism. Thus every solution (1) yields positive ordinary unmerged prefixes of clock $L+2$ and total grade $2p+3$. If $M(P)=0$, the first inequality of (2) follows from this initial two-step cylinder alone. Finiteness of $M(P)$ follows from the [elementary finite clock bound](PAIRED_SOURCE_GRADES.md).

## Closing every ordinary prefix at linear extra grade

At any intermediate date orient the two physical arms so that their true affine slope ratio is $3^j$, $j\ge0$, and write the relation $B=3^j A-a$ on that cylinder. The sign of $a$ is unrestricted. If the original lower arm is $A$, the signed slope exponent is $h+1-g$ with entry odd grades $(g,h)$, and the other ordering reverses this sign. Each additional prescribed lower parity is attainable by a dyadic refinement, because the coordinate varies by an odd multiple of the source class parameter. For $j>0$, the integer $a$ is prime to three: take any ordinary representative after the first odd departure, where both arms are ternary units. At the end of a physically unmerged prefix of budget $G$,
$$
             j\le G+1,\qquad |a|\le3^{G+1}.                              \tag{3}
$$
The magnitude follows by dividing the native [signed determinant](PAIRED_SOURCE_GRADES.md) by $3^{\min(g,h+1)}$. For equal slopes an unmerged endpoint gives $a\ne0$.

Begin the loop at $A-B=1$ in original arm order. An even/odd refinement U gives the relation $(j,a)=(1,1)$, identical to the relation after the mandatory first odd step of the given $(s,3s)$ prefix. Append the given two calendars from date 1 onward. They are compatible: at matching relation the lower coordinate can be prescribed in its original residue class to the remaining dyadic precision, which fixes the upper word as well. The loop so far has length exactly $k$ for $k\ge1$. Its two endpoint slopes and its affine translation agree with the original terminal relation. It cost $G_{\rm prefix}-1$ combined odd departures, since the replaced original first step had two and U has one.

To bring the terminal relation back to translation one, use the following finite operations. Their parities are those of the oriented arms $A,B$.

1. For $j>0$, use common even steps to divide $a$ by its full power of two, then choose D (odd, even). On an odd translation $a$ this gives $(j-1,(a+3^{j-1})/2)$. At levels $j-1>0$ the result is still a ternary unit. At $(1,-1)$ replace the D by U, E, D, D; the successive states are $(2,-2),(2,-1),(1,1),(0,1)$. Here U (even, odd) gives $(j+1,(3a-1)/2)$, and E only halves an even translation. Thus the entire descent to level zero costs at most $j+2$ **odd** departures, irrespective of the number of intervening common evens. The final nonzero translation $b$ has $|b|\le3^{G+1}$ by (3), since each standard decrease maps $|a|$ to at most $\max(|a|,3^{j-1})$. Restore original arm order at level zero, changing only the sign of $b$ if needed.
2. At level zero, an even $b\ne0$ can be halved by one E. For odd $|b|>1$, choose two length-two, grade-one words with offsets 1 and 2 in the order giving $4\mid3b+C_U-C_V$. Exactly one of $3b+1,3b-1$ is divisible by four. Prescribing the lower word then forces the upper one by the same word-divisibility argument as above. The new translation $(3b\pm1)/4$ is nonzero with the same sign. At $|b|\ge2$ either operation reduces its magnitude to at most $7|b|/8$. There are at most $9(G+1)+1$ such operations, because $(8/7)^9>3$ and $|b|\le3^{G+1}$. They cost at most $18(G+1)+2$ combined odd departures.
3. If the result in original arm order is $-1$, exchange it for $+1$ using a fixed equal-grade word pair. At dates 2 and 11 from $s=7$ the original state pairs are $(17,16)$ and $(1,2)$. From date 2 to date 11 each arm has three odd departures. Reversing the arm order in these nine steps consequently changes a translation $-1$ to $+1$ on an entire refined cylinder. If the result was already $+1$, no extra word is needed.

The completed loop changes $A-B=1$ into itself. Its combined odd grade is at most
$$
       (G-1)+(G+3)+18(G+1)+2+6\le32(G+1).
$$
The initial and final slope ratios both equal one, so the complete two words have the same grade $p\le16(G+1)$. There is at least one odd departure by the initial U. Their length $L$ is at least $k$ and their offsets satisfy (1), proving the second inequality of (2). For $k=0$ that inequality is immediate. All route choices concern actual native parities on nonempty positive source cylinders. In particular the loop cannot include an affine merger: its final translation is one.

## Adjacent rational cycles

An equal-grade solution of (1) has rational centers $z=C_U/(2^L-3^p)$ and $z-1=C_V/(2^L-3^p)$. Their common denominator is odd, and each realizes its periodic word by the unique native word cylinder. Since $p\ge1$ both offsets are positive. Hence both phases are positive when $L>p\log_2 3$; in the other case the clock is already $O(p)$. The loop obtained from any physical source therefore supplies positive adjacent cycles whenever its period-to-grade ratio is large. This proves sufficiency of the equal-density positive-cycle assertion for the complete $K$ bound.

Conversely let $z,z-1$ be positive periodic states with a common period $L$ and arbitrary grades $p_1,p_2$. The rational $s_*=(4z-5)/9$ lies in the OO/OE source cylinder and maps to this exact pair at date two. Every corresponding pair of rational states stays distinct throughout the entire loop: an equal state would propagate around to equality of its initial phases. On the source cylinder with the next $L$ paired parities prescribed, each finite-date state difference is affine in the source and nonzero at $s_*$. Avoiding the at most finitely many roots gives infinitely many positive odd integer lifts separated at all dates through $L+2$, of total grade $3+p_1+p_2$. Applying any global bound on $K$ yields the stated necessary condition even without equal densities.

The [unconditional physical lower bound](UNIVERSAL_RATIONAL_MERGERS.md) now forces solutions of (1) with $L\gg p\log p$ in the sense of a fixed positive lower constant along an unbounded sequence, and positive adjacent rational cycles with the same property. The unresolved question is whether the quotient $L/(p\log(2+p))$ is unbounded. The equivalence (2) does not imply convergence or divergence of any particular positive source.
