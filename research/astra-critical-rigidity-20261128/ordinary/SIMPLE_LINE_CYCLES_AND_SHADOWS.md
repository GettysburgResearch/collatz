# Vertex-simple cycles and the rational segments in an arbitrary unmatched clock

Use the native shortcut on a lower arm and an upper arm in their original order. On a physical pair cylinder let $d$ be the signed upper-minus-lower exponent of its affine slope ratio, including the factor three at entry for $(s,3s)$. Write its normalized line as
$$
             3^{d^-}B=3^{d^+}A-\Delta,\qquad
             d^+=\max(d,0),\quad d^-=\max(-d,0).
$$
At an adjacent initial pair $A-B=1$ the state is $(0,1)$. After the mandatory odd/odd departure on an odd ordinary source and its triple the state is $(1,1)$. At each noncollapsed physical state $\Delta$ is a nonzero integer and $3\nmid\Delta$ when $d\ne0$. For $d<0$ exchanging the arms gives the usual orientation $j=|d|$, $a=-\Delta$; for $d\ge0$ put $j=d$, $a=\Delta$. Use the native paired branch transitions in the [signed routing theorem](UNIVERSAL_RATIONAL_MERGERS.md), returning to the fixed original ordering after every step. The possible next states and their two letter labels depend only on $(d,\Delta)$. Every finite legal walk from a physical state has a nonempty dyadic cylinder. We remove the diagonal state $(0,0)$.

A directed cycle is **vertex-simple** if its initial state is its only repetition, at its final date. Put
$$
                 H(d,\Delta)=1+|d|+\log_2(2+|\Delta|).
$$

**Proposed irreducible-cycle criterion.** The uniform ordinary bound $K(G)=O(G\log(2+G))$ holds if and only if every vertex-simple directed cycle in this line graph satisfies
$$
              L\ll p\log_2(2+p+H_*),\qquad
              H_*=\min_{(d,\Delta)\ \text{on the cycle}}H(d,\Delta),        \tag{1}
$$
with a uniform constant. Here $L$ is its native length and $p$ is its common odd grade, which is always positive. All phases of either slope orientation are allowed. The affine graph controls an entire cylinder even when its special periodic rational phases coincide.

A cycle changes $d$ by the difference of the arm grades and hence has equal grades. A cycle of zero grade would consist of common-even steps, which divide the nonzero integer $\Delta$ by two at each date, so no such cycle exists. By the [universal entrance](UNIVERSAL_RATIONAL_MERGERS.md), a minimizing state can be reached from the ordinary entry at cost $O(H_*)$ native steps and grade. Repeat its walk $R=\lceil H_*/p\rceil+1$ times. A finite positive ordinary lift avoiding the at most one collision root of each nonidentical affine pair stays distinct at every date. The lifted clock is at least $RL$, and its grade is $O(H_*+Rp)=O(Rp)$. A global logarithmic bound gives (1).

In the other direction, take any complete static [adjacent return word](ADJACENT_CYCLE_CLOSURE.md) of common grade $P$. Deleting a subwalk between two occurrences of the same vertex splices the remaining legal edges exactly, preserving their labels and states. Iterating partitions the dated edges and their grades into vertex-simple cycles with $\sum L_i=L$, $\sum p_i=P$. Every surviving vertex already occurred in the original walk. At every date $|d|\le P$ and $|\Delta|\le 3^{P+1}$. Indeed the oriented prefix starting from either signed unit translation has native numerator bound $C_U\le2^t3^{|U|_1}$; the resulting [normalized shift bound](PrefixCarryClosure.lean) is $3^{1+\max(|U|_1,|V|_1)}$. Thus $H_{*,i}=O(P+1)$ for each cycle, and summing (1) gives $L=O(P\log(2+P))$. The [checked finite-maximum equivalence](ClockCarryEquivalence.lean) finishes the argument. In particular an unbounded ratio on the master equation forces an unbounded ratio on a family of vertex-simple cycles, whatever the nesting depth of the original words.

## How much clock can lie near balanced grades?

On any true unmatched prefix from an odd positive $s$ and $3s$ of total grade $G$, or on any adjacent return word of total grade $G$, let $N_J$ count dates before a step whose genuine normalized slope gap obeys $|d|\le J$. For all $J\ge0$,
$$
                          N_J\ll (G+1)(J+1).                             \tag{2}
$$
The constant is absolute and independent of the maximum gap reached outside this band. In particular the entire time at equal slopes is $O(G+1)$.

For ordinary source prefixes start the argument after their first common odd departure; the omitted step costs at most one date. Within the band use $\log_2|\Delta|$ as potential. A common even always subtracts one. At a step whose input and output are in the band and at least one letter is odd,
$$
                  2|\Delta'|\le 3|\Delta|+3^{J+1}+1
                            \le (4+3^{J+1})|\Delta|.
$$
This follows from the four oriented integer updates, using the reversed ordering at negative signed levels. An edge from zero slope gap to a negative signed level is the same increase with the old arms exchanged. Since $|\Delta|\ge1$, such an edge can pay $O(J+1)$ in clock plus positive potential change.

Treat each complete excursion outside the band as a single transition between two occurrences of the *same* boundary $d=J$ or $d=-J$; the signed exponent changes by at most one per step. In its fixed starting orientation both arms therefore have the same grade $r\ge1$ on the entire excursion, which includes the exit and reentry steps. If its length is $t$, its signed starting and ending translations in that orientation obey
$$
             2^t a'=3^r a+3^J C_U-C_V .
$$
The native numerator bounds $0\le C_U,C_V\le2^t3^r$ give $|a'|\le3^r(2+3^J)|a|$. The resulting potential gain is $O(r+J+1)$; the excursion contains just one date counted by $N_J$, namely the exit date. Excursions are disjoint and there are at most $G$ of them. An unfinished final excursion contributes only its exit date. If the initial state is outside the band, discard its initial portion until first entry: the entering logarithmic potential is $O(G+1)$ by the [ordinary determinant bound](PAIRED_SOURCE_GRADES.md). Otherwise the initial potential is zero. Sum along the remaining path and drop the nonnegative final potential. Ordinary odd dates consume at most $G$ distinct positions, and the sum of the excursion grades is at most $G$. This proves (2) without any estimate depending on the cost of higher-level common-even steps.

## The scalar rational orbit at a long common run

Consider a maximal interval of $\ell$ consecutive dates at which the two parities agree. Its signed slope exponent is constant. At a positive oriented gap $j$ write $B=3^jA-a$. The two actual starting coordinates are congruent modulo $2^\ell$, since identical native words are equivalent to identical residues at that precision. Let $v=v_2(3^j-1)$. If $\ell>v$, then $2^v\mid a$, the rational
$$
                     z=\frac{a}{3^j-1}
$$
has odd denominator, and the first $\ell-v$ native letters on each arm equal the actual native letters of $z$. Indeed $(3^j-1)A\equiv a\bmod 2^\ell$ gives $A\equiv z\bmod 2^{\ell-v}$. The same holds for $B$. At all of these dates the current center follows the scalar map exactly. The center is a ternary unit of either sign. It cannot reach zero: a nonzero rational with denominator prime to three cannot first map to zero except from $-1/3$. In a vertex-simple cycle containing a mismatch these scalar subsegments are free of repeated native rational states within each segment, since a repetition would repeat the same line vertex at its fixed signed gap.

The discarded terminal portion has at most $v\le 2+\log_2 j$ dates; the elementary valuation identity gives $v=1$ for odd $j$ and $v=2+v_2(j)$ for even $j$. A run of length at most $v$ can all be discarded. On a prefix with at most $G$ odd departures there are at most $G$ mismatches and $G+1$ common runs. Equation (2) disposes of the entire $j=0$ clock. Since $j\le G+1$, all but $O((G+1)\log(2+G))$ dates of the full horizon are accounted for by genuine scalar rational segments of this form; no periodicity assumption on the copied rational orbit enters.

For example, suppose positive ordinary unmatched prefixes have $k/(G\log(2+G))\to\infty$. Fix any $C>0$. A proportion tending to one of their native dates lies on the retained scalar segments with $j>C\log_2(2+G)$ and with segment length exceeding $C(h+1)\log_2(2+G)$, where $h$ is that segment's own number of odd departures. Indeed delete the low band by (2), the discarded tails and mismatches by the preceding count, and all short segments by summing $C(h+1)\log_2(2+G)$ over their at most $G+1$ starts. The total deletion is $O_C((G+1)\log(2+G))=o(k)$. Zero-grade scalar segments are included and can be long. Thus hypothetical superlogarithmic efficiency must persist for most dates on high-slope rational shadows, including possible nonperiodic initial portions. The proof does not exclude such families or assert the ordinary logarithmic bound.
