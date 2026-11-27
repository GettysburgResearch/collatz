# A monotone integer chart for full ordinary cycles of width below nine

Let \(p\) count the odd states of a primitive positive ordinary Collatz cycle, \(A\) its total halving valuation, and \(s,X\) its minimum and maximum **odd** states. Use the unaccelerated dynamics that triples an odd input and adds one, and halves an even input. The primitive full circuit has \(Q=p+A\) states. For each positive integer \(c\le s\) with
\[
                              X<9c+2,                                      \tag{1}
\]
the complete circuit embeds into both of two explicitly specified monotone maps on the integers in \([6c,36c)\), identifying the endpoints by a scale of six. Both rotations are exactly
\[
                               A/(p+A).
\]
In particular \(\gcd(A,p)=1\) for every ordinary cycle with \(X<9s+2\), for arbitrary native valuations and finite periods. As \(c\) varies, every integer in \(((X-2)/9,s]\) gives the same two rotations. On the full branch \(X\le(16s+7)/3\) this includes at least \((11s-1)/27-O(1)\) consecutive integers. The claim gives necessary rotations as functions of height, and does not bound the common plateau's possible width.

## The two maps

Given a fundamental grid vertex \(W\), let \(Y=3W+d(W)\), with
\[
 d(W)=\begin{cases}
   6 & W\equiv6\pmod{12},\\
   3 & W\equiv7\pmod{12},\\
   1 & W\equiv1,5,11\pmod{12},\\
   0 & \text{otherwise}.
 \end{cases}                                                               \tag{2}
\]
Below the wrap \(Y<36c\), send \(W\) to \(Y\). Above it, use \(\lfloor Y/6\rfloor\) for the first map and \(\lceil Y/6\rceil\) for the second, counting one sixfold wind. Extend by scaling to lifts. On the lifted line the maps are nondecreasing. The raw sequence \(3W+d(W)\) has no descent; its values at consecutive residues \(6,7,8\) agree. Rounding to lower or upper multiples of six after \(Y\ge36c\) preserves order at this inner boundary. At the outer seam \(W=36c-1\) the raw value is \(108c-2\), whose upward rounding is \(108c\). At \(W=6c\) the raw value is at least \(18c\), so six times the initial image bounds the final lifted image. Both maps preserve the fundamental grid after normalization.

## Native embedding

Every full state \(x\) is prime to three. Indeed the odd successor of any odd state has numerator \(3x+1\), and doubling intermediate states preserves this unit property. Every state lies between \(s\) and \(3X+1<36c\). The latter strict inequality follows from (1) for integer \(c\ge1\). Put
\[
 W(x)=\begin{cases}6x,&x<6c,\\x,&x\ge6c.\end{cases}
\]
This is an injective map into the indicated fundamental interval: the lower-level images are divisible by six, the upper-level images are prime to three, and within each level there is no collision. Their extended sixfold rays are distinct as well.

For a lower-level odd state the corresponding label has residue six modulo twelve, so the raw correction is six. At a lower even state it is zero. At an upper even state it is again zero because its label is a unit modulo three. An upper odd state could have residue \(1,5,7,11\pmod{12}\). Residue seven cannot occur: if \(x=6u+1\equiv7\pmod{12}\), then \(u\) is odd, \(u\ge c\), and its literal successor as an **odd** phase is \((3x+1)/2=9u+2\ge9c+2>X\). Thus (2) gives exactly one on the remaining upper odd states.

Write \(J(x)=1\) at lower-level states and zero at upper-level states. If \(x'\) is its ordinary unaccelerated successor and \(e=1\) if \(x\) is even, zero otherwise, then
\[
          3W(x)+d(W(x))=6^{J(x)+e-J(x')}W(x').
\]
The raw image before normalization is between \(18c\) and \(108c+O(1)\) and its normalized target lies in \([6c,36c)\). The exponent is exactly zero or one, as the raw value belongs to \([6c,216c)\). In the latter case the raw integer is divisible by six. Both rounding maps consequently take the true state to its prescribed true successor. The sum of the exponents telescopes to \(A\), the number of native even steps. The \(Q\) distinct states therefore form a primitive circuit with winding \(A\). On an ordered circle a nondecreasing map permutes a periodic orbit by an order-preserving cyclic translation; the translation and period are coprime on a primitive orbit. This proves the reduced-clock assertion and the forced plateau.

For \(X<6c\) there is a smaller chart with labels \(Z=W/2\) and \(d_0(Z)=\mathbf1_{Z\equiv3\pmod6}\): every upper-level state is even, so the labels are integers. Divide \(3(Z+d_0)\) by six at the wrap, with either floor or ceiling. A true label is never divisible by nine. On the upper branch it also avoids odd 3-free values, since \(Z+d_0\) is then even. These are additional exact necessary restrictions.

Ordinary integrality is essential. The positive rational cycle of odd phases \(5/7,11/7\) has valuations \(1,3\), clock \(A=4\), period \(p=2\) and width \(11/5\). Its complete reduced denominator is seven. Thus a bounded ratio and an affine return over positive rationals do not give the primitive reduced clock. The test here depends on all integer phases of the same circuit, not on checking a proper factor of the word determinant. A uniform separation of the two completions, or a bound ruling out a common avoiding orbit on every required cutoff, remains open.

[Exact chart, interval endpoint and ordinary path replay](check_full_step_chart.py) · [Recorded controls](full_step_chart_controls.json)
