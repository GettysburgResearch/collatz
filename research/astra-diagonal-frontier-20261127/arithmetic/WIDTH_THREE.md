# The odd width of an ordinary cycle is asymptotically at least three

Let \(p,s,X\) be the primitive odd period, least odd phase and greatest odd phase of a positive ordinary Collatz cycle. Along any sequence of such cycles whose periods tend to infinity,
\[
                            \liminf X/s\ \ge\ 3.                            \tag{1}
\]
The assertion is unconditional, using the published finite irrationality exponent of Bondareva, Luchin and Salikhov. It applies to arbitrary native valuations. In particular it includes the range where valuation three first becomes possible. The proof does not resolve the case \(X/s\ge3-o(1)\), and does not bound away from three by a positive constant.

The underlying new integer conclusion is the following. Fix \(R<3\). On every sufficiently large ordinary candidate with \(X/s\le R\), a fixed order-six integer difference of the folded spatial ranks has one strict sign everywhere. This gives \(s\gg_R p^6\), which is incompatible with the classical upper exponent \(5.116201\). No irrationality measure of three is assumed.

## Two grades and the exact mechanical calendar

Suppose contrariwise there is a sequence with \(X/s\le R<3\). The minima tend to infinity since each fixed positive integer has only one forward orbit. Choose \(0<\epsilon<1/4\) sufficiently small that \(R/[2(1-\epsilon)]<3/2\). Put \(L=2(1-\epsilon)s\). If necessary increase \(R\) within \((2,3)\) to give a convenient uniform upper bound. Fold every odd phase \(x\) to a distinct integer \(Z\in[L,2L)\): put \(Z=2x\) below \(L\), otherwise \(Z=x\). This works since \(x\ge s>L/2\) and \(X<2L\). Write \(c=Z/x\in\{1,2\}\). This is exactly the lowbit of \(Z\).

Sort these \(p\) labels increasingly as \(Z_0,\ldots,Z_{p-1}\) and extend both \(Z,c\) by doubling across each rank period. The true raw map on this grid is \(Z\mapsto3Z+c\). It is strictly increasing inside the octave since labels are integers and the marks differ by at most one. The next doubled initial tag is at least two, giving the same order at the seam. Dyadic rays of distinct odd phases are distinct and the actual closed odd map permutes them primitively. An increasing bijection on the lifted ordered set translates its ranks. The translation is precisely \(A=\sum e_x\): in fundamental representatives the sum of the image windings telescopes the changes of tags, leaving this native clock. Hence \(\gcd(A,p)=1\) and
\[
                 Z_{r+A}=3Z_r+c_r .
\]
The exact product identity gives \(0<A/p-\gamma\le 1/(3s\log2)\), with \(\gamma=\log_2 3\). Eventually \(A=p+h\) with \(0<h<p\), and \(\alpha_p=h/p\to\alpha=\gamma-1\in(1/2,2/3)\). At a fundamental base rank \(r\), put \(f=r/p\), \(r'=(r+h)\bmod p\) and \(b=1+\mathbf1_{f\ge1-\alpha_p}\). Then the native register advances by dividing the raw labels by \(2^b\) at this common base.

The angles \(\log_2(Z_r/L)\) have empirical distributions tending uniformly to Haar measure on the unit circle. To see this, the chronological angle increments are \(\gamma+O(1/s)\bmod1\). Every subsequential limit is invariant under the irrational rotation by \(\gamma\); its nonconstant Fourier coefficients vanish. Uniform convergence of the cumulative distributions to the continuous uniform distribution follows by a fixed finite mesh. Thus
\[
                \sup_{r<p}|\log_2(Z_r/L)-r/p|\longrightarrow0.            \tag{2}
\]
Choose \(\eta\) strictly between \(\max(0,\log_2(R/[2(1-\epsilon)]))\) and \(\alpha\). For sufficiently large cycles, any fixed-size nonwrapped tuple starting at rank \(r\) with \(f>\eta\) has every mark two: an actual mark one requires \(Z=x\le X\). This holds as well across the spatial seam using the unwrapped marks. The labels just before the seam have mark two since \(X<2L\) with a fixed margin. Just after the wrap all underlying fundamental labels have mark one since \(Z/2<s\) near \(L\); doubling them gives mark two and labels twice odd integers. The choice of \(L<2s\) makes that last margin strict. At every other fundamental tuple all unwrapped marks belong to \(\{1,2\}\).

## An order-six difference with positive coefficient mass six

Let \(E\) be the unit spatial shift and use
\[
 P(T)=(T-1)^2(T^2-1)(T^3-1)(T^4-1)(T^5-1)
   =1-2T+T^3+T^5-2T^8+T^{11}+T^{13}-2T^{15}+T^{16}.
\]
Its positive coefficients sum to six and its negative coefficients sum to minus six. Let \(H_r=P(E)Z_r\). At each fundamental rank,
\[
          2^b H_{r'}=3H_r+d_r,\qquad d_r=P(E)c_r,\qquad |d_r|\le6.         \tag{3}
\]
At a forced row \(f>\eta\) the mark is constant, so \(d_r=0\) and \(4\mid H_r\): every participating unwrapped label is twice an odd integer, and the coefficients sum to zero. All \(H_r\) at fundamental ranks are integers.

The mechanical word in \(b\) has no consecutive ones and no three consecutive twos because \(1/2<\alpha_p<2/3\). For example two consecutive ones or three consecutive twos violate the floor difference over a window of length two or three. A date just after a one has \(f\ge\alpha_p>\eta\), so it is forced. A current two preceded by a two is the second two in a block \(1,2,2,1\).

Consider the integers \(H\) along the complete chronological circuit. In a positive run that begins after a nonpositive value, a one cannot be its birth step: the next \(H'\) is divisible by four and \(2H'=3H+d\le6\). Nor can a forced two be the birth step. The birth must therefore be an active second two, and \(4H'=3H+d\le6\) shows that \(H'=1\), at its next date of type one.

At any date of type one carrying \(H\in\{1,2,3\}\) inside this positive run, its next value, if positive, is four. Indeed \(2H'\le15\) and \(4\mid H'\). The forced first two then gives the following value three. On a short return this is the next one. On a long return it is the second two; the next positive value is \((9+d)/4\in\{1,2,3\}\). Induction through the run proves that every second two reached inside it has exactly \(H=3\). Applying the same argument to \(-H,-d\) gives \(H=-3\) in a negative run. This permits finite excursions and uses full cyclic recurrence to classify all runs.

Pick a fixed open interval with closure in
\[
                         (\max(\eta,1-\alpha),\alpha).
\]
For sufficiently large \(p\), every rank in that interval has \(b=2\), its predecessor had \(b=2\), and its own row is forced. The predecessor condition follows from \(f<\alpha_p\). On these rows \(4\mid H\), so neither sign of three is possible. If the full chronological cycle is not everywhere strictly positive or everywhere strictly negative, every nonzero belongs to a run with the appropriate birth, including the case in which only one sign and zeros occur. It follows that \(H_r=0\) on this entire fixed open **spatial** rank interval.

Such a zero interval is impossible. The polynomial \(P\) divides \((T^{60}-1)^6\), since each of its six displayed factors divides \(T^{60}-1\). On a slightly smaller interval the corresponding stride-sixty sixth difference vanishes. It then vanishes also at stride \(60t\) inside the original interval, by multiplying by \((1+E^{60}+\cdots+E^{60(t-1)})^6\). Choose interior starts with \(r/p\to f_0\) and integer \(t\) with \(60t/p\to c_0>0\) small enough that every term stays in the interval. By (2), this sixth difference divided by \(L\) tends to \(2^{f_0}(2^{c_0}-1)^6>0\). This contradiction proves the strict global sign.

## The height contradiction

Write \(P(T)=(T-1)^6 B(T)\) with a fixed integer polynomial \(B\). For positive integer \(t\),
\[
 (E^t-1)^6B(E)Z_r=(1+E+\cdots+E^{t-1})^6H_r .
\]
Choose \(r=0\), \(t=\lfloor(p-20)/6\rfloor\) for large \(p\). All inputs on the left lie in the fundamental octave. Each of the \(t^6\) terms on the right is a nonzero integer of the same sign. Since all fundamental labels are less than \(2L\), the left side has absolute value at most \(2^6\|B\|_1\,2L\). This gives \(s\gg p^6\).

The true angular clock satisfies \(0<A\log2-p\log3\le p/(3s)\). Theorem 1 of Bondareva, Luchin and Salikhov gives \(A\log2-p\log3\gg p^{-4.116201}\) on these unbounded clocks; \(A\asymp p\). Hence \(s\ll p^{5.116201}\), contradicting the order-six bound. The analytic input is external. [Bondareva, Luchin and Salikhov, Theorem 1, p. 18](https://m.mathnet.ru/links/1d9b9977c1093c37b767dc2d807bd4a2/cheb619.pdf) · [Earlier all-width grade-pressure estimates](ODD_HEIGHT_PRESSURE.md)

The earlier full-band second-curvature argument treats all three grades under a binary assumption. The present order-six stencil and forced second-two interval rely on the narrower width strictly below three. The sign conclusion here concerns \(P(E)Z\); it does not assert positivity of the pure sixth difference separately. At \(R=3\) the forced second-two arc can disappear, and the proof supplies no strict exclusion there. [PR201 full-band rank curvature](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md)

[Finite excursion and polynomial replay](check_width_three.py) · [Recorded controls](width_three_controls.json) · [Lean arithmetic kernel](WidthThree.lean)

A separate [quantitative refinement](WIDTH_THREE_RATE.md) proves a height-dependent approach to the same lower bound, with an unevaluated absolute constant.

## Formal propagation through the calendar

[WidthThreeCalendar.lean](WidthThreeCalendar.lean) adds six public theorems connecting the scalar cases above. The calendar has three phases: a one, the first two following it, and an optional second two. Starting at zero, its exact integer recurrence preserves bounds of three in the first and third phases and four in the middle phase. A second-two state divisible by four is therefore zero. On a path with no zeros, every step preserves the strict sign, so the complete nonzero chronological circuit has one sign. The actual rank embedding supplies the calendar and divisibility hypotheses in the written argument above. This module formalizes their propagation, not the embedding, angular discrepancy, or final linear-form comparison.
