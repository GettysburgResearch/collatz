# Consequences and a higher-difference control for strict rank convexity

Consider the ordinary canonical-height-one cycle of STRICT_CONVEX_RANKS.md, with primitive odd period $P$, maximal odd state $X$, and integral labels $L_r$ satisfying $L_{r+P}=2L_r$. The statements about growing cycles below concern this full class with all positive valuations. In particular valuation three is permitted.

## Every gap can serve as the terminal label, with no population estimate

Let $1\le t<P$ and $G_r^{(t)}=L_{r+t}-L_r$. For uniform rank $r$ the entropy of $G_r^{(t)}$ is exactly $\log P$ by strict convexity. Also $0<G_r^{(t)}\le4X$ because all fundamental labels are at most $2X$. This holds for the complementary offset $P-t$ as well. Take $b=\lceil\log_3(8X+1)\rceil$, independently of either offset. In the signed gap recurrence of ALL_LAG_LINEAR_DEFECTS.md, a length-$b$ mechanical and drift word fixes the terminal gap modulo $3^b$, and hence exactly. Applying the conditional entropy count of ALL_LAG_TWO_ORIENTATIONS.md gives
$$
 \log P\le O(\log(b+1))+b(h+\beta\log2)+O(1).
$$
Here $h$ is any of its valid conditional $w$-word entropy upper rates and $\beta$ is the chosen orientation's ambiguous-site fraction. This holds even when $t/P\to0$. For any finite irrationality exponent upper bound $M$ for $\log_2 3$, the geometric cycle bound gives $\limsup\log X/\log P\le M$. Therefore every limiting orientation requires $h+\limsup\beta\log2\ge(\log3)/M$. At $t/P\to0$, choose the smaller offset, whose ambiguity is at most $t/P$, giving $h\ge(\log3)/M$ outright. At positive limiting offset the existing two-orientation numerical comparisons apply verbatim. Thus the all-lag mismatch lower limits $>1/1000$ using Bondareva–Luchin–Salikhov (2018), or $>1/36$ using the source-qualified Chudnovsky bound $M=3$, both follow without an integral Subspace Theorem or a previous lower bound on $X$. The corresponding fixed-sum window proportions are at least half the mismatch proportions by successive differences. The orientation entropy estimates and those constants previously appeared in ALL_LAG_TWO_ORIENTATIONS.md.

A related elementary scale identity will apply to gap-based arguments irrespective of those numerical estimates. Write $g_r=L_{r+1}-L_r$. Strict convexity and doubling give $g_0\le g_r<2g_0$ on the fundamental period. Since $\sum_{r<P}g_r=L_0$, all these gaps are comparable to $L_0/P$, which is comparable to $X/P$ by the octave ordering. Also $g_0\ge P$ from $P$ strictly increasing integers in $[g_0,2g_0)$. In particular $L_0\ge P g_0+P(P-1)/2\ge(3P^2-P)/2$.

## The third finite difference can reverse sign on one ordinary orbit segment

For a common mechanical letter $m$ let each label $v$ advance to $(3v+\operatorname{lowbit}(v))/2^m$. The following six rows are ordered left to right and have strictly positive first and second differences. Their third differences are shown in the last column.

| Step | Four simultaneous labels | Third difference |
|---|---|---|
| 0 | 83, 94, 107, 121 | −1 |
| 1 | 125, 142, 161, 182 | 0 |
| 2 | 94, 107, 121, 137 | 1 |
| 3 | 142, 161, 182, 206 | 1 |
| 4 | 107, 121, 137, 155 | 0 |
| 5 | 161, 182, 206, 233 | 0 |

The calendar is $(1,2,1,2,1)$, realized at intercept $1/100$ and slope $\log_2 3$. Every row uses only labels of lowbit one or two. The odd parts in each column advance by the actual positive accelerated Collatz map. Each succeeding column starts two chronological steps farther along the very same orbit from 83, as the overlapping rows verify. Thus any purely local sign induction for third differences fails even with this extra physical orbit condition. An occurrence of zero here means four values are quadratic in their index, which does not force the lowbits to agree. These rows are a finite local example, with no assertion that they occur at consecutive ranks of an actual cycle.

The accompanying exact-integer replay also tests a sign reversal across five letters for every one of the six possible length-five calendars at this slope. All four input and output labels in all controls are coprime to three, have lowbit at most two and advance by ordinary trajectories on odd parts. Only the displayed example is claimed to consist of overlapping segments of a single trajectory. At both rational slope-bracket endpoints the order of the six calendar cuts agrees; the integer lifts of these cuts are constant within the bracket, directly since no $j\alpha$ crosses an integer for $1\le j\le5$. Both midpoint and single-point faces are evaluated. The underlying global strict-convexity theorem and the entropy estimates are written proofs.

- https://doi.org/10.22405/2226-8383-2018-19-1-15-25
- https://arxiv.org/html/2610.28079v1#S11
