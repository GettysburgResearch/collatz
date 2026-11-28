# Interlacing of the two odd calendars in the adjacent-cycle equation

Let \(U=(u_1<\cdots<u_p)\) and \(V=(v_1<\cdots<v_p)\) be two lists of odd dates in \([0,L)\). Suppose they solve the [ordered carry equation](../ordinary/ADJACENT_CYCLE_CLOSURE.md),
\[
       \sum_{i=1}^{p}3^{p-i}(2^{u_i}-2^{v_i})=2^L-3^p .
\]
Write \(\gamma=\log_2 3\). Count unequal ranks \(M=\#\{i:u_i\ne v_i\}\), unequal native letters \(H=|U\mathbin\triangle V|\), and ordered crossings with multiplicity
\[
 I=\sum_{i=1}^p\bigl(\#\{k\ge i:u_k<v_i\}+\#\{k\ge i:v_k<u_i\}\bigr).
\]
The two comparisons are strict. A rank where the dates differ contributes one from \(k=i\). Later ranks count when they have already occurred on the leading arm by the time the lagging arm reaches rank \(i\).

**Proposed bounds.** For every such solution,
\[
   L-\gamma p\le \gamma I-\tfrac{H}{2}\log_2(9/8).                    \tag{1}
\]
More strongly, for each \(\epsilon>0\) there is an absolute \(C_\epsilon\) such that at every positive determinant,
\[
                   L-\gamma p\le\epsilon I+C_\epsilon M .           \tag{2}
\]
The coefficient in front of \(I\) can be arbitrarily small. Its accompanying constant comes from the rational Subspace Theorem and is ineffective. The case \(2^L<3^p\) has negative left side in (2). The bounds allow repetitions of a nonprimitive paired calendar.

In particular, along any growing family with \(L\ge c p\log_2p\) for a fixed \(c>0\), one must have \(I/(p\log_2p)\to\infty\). If \(J=\max_{0\le t\le L}|\#\{u_i<t\}-\#\{v_i<t\}|\), then
\[
          I\le MJ,\qquad I\le M(M+1)/2,\qquad J\le H/2.              \tag{3}
\]
Thus \(MJ/(p\log p)\to\infty\) and \(M/\sqrt{p\log p}\to\infty\) on every such family. When \(I=O(p\log p)\), (2) actually gives \(L=o(p\log p)\) as \(p\to\infty\). Without a restriction on the crossings, the uniform \(O(p\log p)\) upper bound remains open.

## The integer difference along the closed pair

The two periodic rational starting phases \(X_0,Y_0\) satisfy \(X_0-Y_0=1\). They are both positive when \(D=2^L-3^p>0\) and both negative when \(D<0\), since they have positive carries and share this raw determinant. Each has odd denominator prime to three, and the integer numerator over its reduced denominator is a ternary unit at every phase. Indeed \(D\) is nonzero modulo three and the final odd-date contribution in every rotated carry is nonzero modulo three. The two reduced denominators agree by the unit starting translation and remain constant.

At time \(t\) write \(g,h\) for the counts so far, \(m=\min(g,h)\), \(j=|g-h|\), and put
\[
                    A_t=3^{g-m}Y_t-3^{h-m}X_t .
\]
This is an integer. Modulo the common reduced denominator, \(qX_t\) and \(qY_t\) are congruent to \(2^{-t}3^g qX_0\) and \(2^{-t}3^h qY_0\). Equality of the starting residues gives the required divisibility. Moreover \(A_t\ne0\) always. Unequal grades would force one ternary-unit numerator to be divisible by three. Equal grades would give equal physical states. Both arms have period dividing \(L\), so this would imply equal starting phases. At the ends \(A_0=A_L=-1\).

Let \(a,b\in\{0,1\}\) be the two native letters at \(t\), and \(m'=\min(g+a,h+b)\). The exact recurrence is
\[
 2A_{t+1}=3^{c_t}A_t+B_t,\qquad
 c_t=a+b-(m'-m)\in\{0,1\},\quad
 B_t=b3^{g+a-m'}-a3^{h+b-m'}.                                      \tag{4}
\]
In particular \(\sum_{t<L}c_t=2p-p=p\). Call a date marked when \(B_t\ne0\). Besides the \(H\) single-odd dates, these are precisely the double-odd dates with \(j>0\). At every other date each odd departure, if present, occurs at the same ordinal rank on both tracks. Thus the number \(W\) of marks lies between \(M\) and \(2M\). At each mark \(B_t\) is a signed sum of at most two powers of three with absolute value at most \(3^{j+1}\).

The level \(j\) starts and ends at zero. A single-odd date either increases it by one (an outward step) or decreases it by one (an inward step). Each type occurs \(H/2\) times. At an inward step the lagging arm arrives at a rank whose copy and \(j-1\) later ranks have already occurred on the leading arm. At a marked double-odd date the same count is \(j\), with the current leading-arm departure excluded by the strict comparison. There is no contribution at other dates. Therefore
\[
 I=\sum_{\rm inward}j+\sum_{\text{marked double odd}}j,\qquad
 \sum_{\rm marked}j\le2I.                                             \tag{5}
\]
For the latter inequality, telescoping \(j^2\) gives \(\sum_{\rm outward}j=\sum_{\rm inward}(j-1)\). There is at most one later occurrence per unequal rank \(i\), so (5) gives \(I\le MJ\). Each pair counted in \(I\) has both its indices in the unequal ranks: if \(u_k<v_i\) and \(k\ge i\), then \(u_i\le u_k<v_i\le v_k\), and the reverse case is symmetric. For fixed \(i,k\) at most one orientation occurs. This proves the other crossing bound in (3), and the total number of outward steps bounds \(J\).

## The finite real bound

Taking absolute values in (4) and using \(A_0=A_L\) gives the exact signed-log telescope
\[
  L-\gamma p=\sum_{t<L}\log_2\left|1+\frac{B_t}{3^{c_t}A_t}\right|.  \tag{6}
\]
Every summand is well-defined by nonvanishing. An outward step has \(c_t=1, |B_t|=1\), costing at most \(\log_2(4/3)\). An inward step from level \(j\ge1\) has \(c_t=0, |B_t|=3^{j-1}\), costing at most \(\gamma j+\log_2(2/3)\). A marked double odd has \(c_t=1, |B_t|=3^j-1\), costing at most \(\gamma j\). Otherwise the cost is zero. Equation (5) gives (1) including the saving \(\log_2(9/8)\) per outward/inward pair.

## Removing a fixed proportion of the crossing cost

Use the [two-endpoint chronological sum estimate, equation (3)](../ordinary/SPARSE_DISCREPANCY_BLOCKS.md) with prime set \(\{2,3\}\) and fixed \(\kappa=2\). Its coarser consequence for a zero sum with at most \(r\) interior pure two-three terms and its two nonzero integer endpoint coefficients is
\[
   d\le 2(\log_2|A_{\rm start}|+\log_2|A_{\rm end}|)+C_r .          \tag{7}
\]
It assumes that each strictly earlier chronological partial sum is nonzero. For a native interval \([s,e)\) in (4), unroll the recurrence by multiplying its \(t\)-th impulse by \(2^{t-s}3^{\sum_{t<k<e}c_k}\). The terminal term is \(-2^{e-s}A_e\). The sum strictly before the relative date \(d'\), including the initial term, is \(2^{d'}3^{\sum_{s+d'\le k<e}c_k}A_{s+d'}\), which is nonzero. A marked date needs at most two interior terms. Thus (7) applies to every interval between marked dates, independently of the number of neutral odd departures inside.

Fix an integer \(r\ge1\). Take packets of \(r\) consecutive marked dates in chronological order, except possibly the last packet. Within a packet let \(j_*\) be the greatest imbalance at its marks. Call a marked date low when \(|A_t|\le3^{j_*+1}\). Every other mark contributes at most one to (6). If a packet has at least two low marks, let \(s,e\) be the first and last. Its interior \([s,e)\) has at most \(2r\) pure terms and both endpoints have the low bound. Hence (7) implies
\[
          e-s\le 4\gamma(j_*+1)+C_{2r}.
\]
By (4), the sum of the **signed** corrections in (6) on this interval is
\[
       (e-s)-\gamma\sum_{s\le t<e}c_t+
                         \log_2|A_e/A_s|
       \le 5\gamma(j_*+1)+C_{2r}.
\]
Outside the interval there remains at most one low mark, whose contribution is at most \(1+\gamma(j_*+1)\). The same last bound covers the only low mark when there are fewer than two. Thus the total signed correction of a packet is at most \(6\gamma(j_*+1)+C_{2r}+r+1\), using a constant made nonnegative. This argument never bounds a sum of positive parts by a signed telescope.

The imbalance changes by at most one per marked date. In a complete packet its maximum is at most the average of its marked imbalances plus \(r\). In the final incomplete packet the maximum is at most \(r\), since the level returns to zero by its end and no subsequent unmarked step can change it. By (5) the sum of packet maxima is at most \(2I/r+O(W+r)\). Because a solution has \(M\ge1\), all terms independent of the calendar can be absorbed into \(O_r(M)\). Summing (6) therefore gives
\[
                   L-\gamma p \le (12\gamma/r)I+O_r(M).
\]
Choosing \(r\) gives (2), and dividing it by \(p\log p\) proves the stated consequences. The argument only uses the original adjacent-cycle correspondence, the earlier discrepancy lemma and the complete measured calendars. It supplies no uniform upper bound for \(I\) on all solutions.

The [exact finite control](check_ordered_crossings.py) enumerated every ordered carry solution through native length 15. All 510 had positive determinant. It checked the sharp factor in (1) using integer powers, 4,403 ordered crossings, 5,682 trimmed low-endpoint packets and all 12,545 internal cuts of those packets. In 82 solutions some ordinal ranks coincide. Normal and optimized Python produced identical output. These finite checks cover the recurrence and counting interfaces, rather than the ineffective interval estimate (7).
