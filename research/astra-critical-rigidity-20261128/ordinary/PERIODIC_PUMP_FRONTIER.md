# When exactly periodic shadows beat the logarithmic grade scale

**Proposed equivalence.** Use the positive ordinary source pair $(s,3s)$ under the shortcut map. Among all its unmerged finite prefixes of combined odd grade at most $G$, let $P(G)$ be the maximum length $LR$ of a final segment consisting of $R\ge1$ complete copies of the same length-$L$ word, subject to the following exact centering requirement. On the prefix cylinder at entry the two actual affine slopes differ; the intersection of their graph with the diagonal is the periodic rational state of that word. The grade budget includes the entire entry history, whereas $P(G)$ counts only the time after it. Set $P(G)=0$ if no instance exists. Then
$$
 P(G)=O(G\log(2+G))\quad\Longleftrightarrow\quad
 \sup_{\text{positive rational cycles}}\;
 \frac{L}{p\log(2+p+\operatorname{ord}_q(3))}<\infty .                 \tag{1}
$$
Here $p$ is the odd grade per period and $q$ the full reduced denominator. Use one primitive period and put $\operatorname{ord}_1(3)=1$. The logarithm may have any fixed base greater than one. Nonprimitive words yield identical full-period lengths and grades after grouping additional laps of the primitive word.

For the subclass of periods with one odd departure, (1) becomes
$$
 P_{1}(G)=O(G\log(2+G))\quad\Longleftrightarrow\quad
 \inf_{L\ge3}\frac{\log(2+\operatorname{ord}_{2^L-3}(3))}{L}>0.         \tag{2}
$$
Thus a super-$G\log G$ sequence of exactly centered, one-odd tails exists precisely when $\operatorname{ord}_{2^L-3}(3)=\exp(o(L))$ along some $L\to\infty$. The earlier [Corvaja–Zannier application](RATIONAL_PERIODIC_SHADOWS.md) gives $\operatorname{ord}_{2^L-3}(3)/L\to\infty$, compatible with either side of this exponential-order question.

## From a physical tail to the order bound

If the normalized entry slope exponent gap is $j>0$, integrality of its affine translation gives $q\mid3^j-1$. Since $j=|h+1-g|$ for entry grades $(g,h)$, $\operatorname{ord}_q(3)\le j\le G+1$. Also $2pR\le G$. A nonzero rational periodic state has $p\ge1$; the all-even periodic state zero cannot be an unequal-slope physical merger by its non-unit numerator. A negative center has $2^L<3^p$, since the affine offset is positive. It gives $LR<(\log_2 3)G/2$. For a positive center satisfying the right side of (1),
$$
            LR\le \frac{G}{2}\frac{L}{p}
                =O\big(G\log(2+G)\big).
$$

## Realizing every cycle at a comparable budget

Consider any primitive positive cycle. Each phase is a rational ternary unit of odd denominator, since the closing equation on any rotation has both denominator and offset prime to three and odd denominator. Cycles with $2^L<2\cdot3^p$ already have $L/p\le1+\log_2 3$. Otherwise, at each phase the word offset $C$ is at most $2^L3^p$, so $z=C/(2^L-3^p)\le2\cdot3^p$. Take $j=\operatorname{ord}_q(3)$. Then $a=(3^j-1)z$ has $\log(2+a)=O(j+p)$. The [universal physical construction](UNIVERSAL_RATIONAL_MERGERS.md) enters this center at a true unequal-slope line with combined grade at most $C_0(j+p)$ for an absolute $C_0$. Its positive integer lifts realize any number of full laps without same-date merger.

Choose $R=\lceil(j+p)/p\rceil$. The total grade for this actual family is at most $(C_0+4)(j+p)$ and $LR\ge(L/p)(j+p)$. If the left side of (1) holds, it bounds the latter by $O((j+p)\log(2+j+p))$, proving the reverse implication uniformly over all periods. Finally a one-odd period rotated to its odd input has center $1/(2^L-3)$, proving (2). Its small periods $L=1,2$ have bounded efficiency.

These equivalences concern exactly centered full laps. An estimate for the complete unmatched clock would also have to bound all entry clocks and schedules with no long periodic tail.
