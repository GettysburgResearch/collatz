# Uniform interval counts for ordinary residue avoiders

Let \(S_D\) denote the **odd forward** dimer survivors, and \(S_5\) the **odd bi-infinite** ordinary avoid-5 states, as in [AVOIDER_COUNTS.md](AVOIDER_COUNTS.md). For every real interval \(I\) of length \(X\ge2\),
\[
 \#(I\cap S_D)\ll\frac{X^{h_D}}{\sqrt{\log X}},\qquad
 \#(I\cap S_5)\ll\frac{X^{h_5}}{\sqrt{\log X}},                      \tag{1}
\]
uniformly in its location. The exponents are \(h_D=0.3208518\ldots\) and \(h_5=0.6177244\ldots\). This proof also yields the initial-interval estimates without a separate bound on accumulated logarithmic correction. The two different history requirements stay in force.

Write \(A_D(t)=\sup_{a}\#(S_D\cap[a,a+2^t))\) for integer \(t\ge0\), with \(a\) real, and \(A_5(b)=\sup_a\#(S_5\cap[a,a+3^b))\) similarly. The half-open convention makes the equal-modulus parity or ternary cylinder have at most one representative. Intervals with other endpoint conventions can be embedded in an interval of twice the length. Rounding a subsidiary positive length \(Y\ge1\) up to \(d^{\lceil\log_dY\rceil}\), for \(d=2\) or 3, multiplies it by at most \(d\).

### Forward images

Fix \([a,a+2^t)\). Its sources with \(q\ge p_*t-L\) odd departures in \(t\) steps number \(O_L(2^{h_Dt}/\sqrt t)\) by the parity-cylinder injection and formula (4) of [AVOIDER_COUNTS.md](AVOIDER_COUNTS.md). For every smaller integer \(q\), the affine formula puts their endpoints in a translated interval of length at most
\[
                       Y_q=3^q+(3/2)^t+1 .
\]
Indeed the term \(3^qx/2^t\) varies by at most \(3^q\), while \(0\le C(w)<3^t\) contributes less than \((3/2)^t\). Distinct odd sources have distinct endpoints at this common physical time by the no-\(00\) inversion proved in [AVOIDER_COUNTS.md](AVOIDER_COUNTS.md). Odd endpoints belong to \(S_D\); halving any even endpoints puts them in a single interval of half the length and in \(S_D\). Thus the \(q\)-class contributes at most \(2A_D(\lceil\log_2Y_q\rceil)\).

Set \(h=h_D\) and inductively assume \(A_D(j)\le M 2^{hj}/\sqrt{j+1}\) for \(j<t\). When \(q<2t/5\), \(Y_q=O(2^{\xi t})\) for \(\xi=\max((2/5)\log_23,\log_2(3/2))<1\). The \(O(t)\) such classes contribute \(O(Mt2^{h\xi t})=o(M2^{ht}/\sqrt t)\), uniformly in \(L\). For \(q\ge2t/5\), \(Y_q\le3\cdot3^q\) for all large \(t\), since \(3^{2/5}>3/2\). Its rounded scale index is comparable to \(t\). If \(q<p_*t-L\) and \(L\) is sufficiently large, this index is strictly less than \(t\). The induction bound and the geometric sum give the combined contribution
\[
                 O\!\left(M 3^{-hL}\frac{2^{ht}}{\sqrt{t+1}}\right),
\]
with the implicit constant independent of \(L\). Choose fixed \(L\) so that this is at most one quarter of the target. Take \(t\) sufficiently large for the small-\(q\) share to be another quarter. Then take \(M\) sufficiently large for the high-\(q\) bound and the finitely many initial scales. This closes the induction uniformly in \(a\).

### Backward predecessors

For \(y\in[a,a+3^b)\cap S_5\) choose \(b\) preceding odd steps and write \(s\) for their total division exponent. For a fixed gap word \(\mathbf a\in\{1,2\}^b\), its target satisfies one congruence modulo \(3^b\), so there is at most one integer target in the interval. Words with \(s\ge\alpha b-L\) number \(O_L(3^{h_5 b}/\sqrt b)\) by the critical binomial upper tail in [AVOIDER_COUNTS.md](AVOIDER_COUNTS.md).

For fixed smaller \(s\), all corresponding predecessors \(z=(2^s y-C(\mathbf a))/3^b\) lie in an interval of length
\[
                           Y_s=2^s+(4/3)^b+1\le3\cdot2^s .
\]
Here the partial gaps satisfy \(a_1+\cdots+a_j\le2j\), giving \(C(\mathbf a)\le\sum_{j=0}^{b-1}3^{b-1-j}4^j=4^b-3^b\). Also \(s\ge b\). Each predecessor belongs to \(S_5\) and determines its target after \(b\) forward odd steps. The \(s\)-class therefore contributes at most \(A_5(\lceil\log_3Y_s\rceil)\). All rounded indices are comparable to \(b\); for sufficiently large fixed \(L\) all are strictly smaller than \(b\).

Inductively insert \(A_5(j)\le M3^{h_5j}/\sqrt{j+1}\) and sum \(2^{h_5s}\) over \(s<\alpha b-L\). This costs at most \(O(M2^{-h_5L}3^{h_5 b}/\sqrt{b+1})\) with absolute implied constant independent of \(L\). Choose \(L\) and then \(M\) as in the forward proof. This proves the second estimate. Arbitrary lengths in (1) follow by rounding once more.

For comparison, Weaver's unrestricted labelled-image compression already implies a uniform power saving for any one orbit, and also for the union of all cyclic points by injectivity at the common endpoint time. Its unrestricted exponent is near \(H_2(\log_3 2)\). The present interval counts exploit the dimer or two-gap word language and the distinct history hypotheses in (1). [Weaver 28 v3, Theorem A and §8.1](https://rstation.ai/problems/collatz/papers/28)
