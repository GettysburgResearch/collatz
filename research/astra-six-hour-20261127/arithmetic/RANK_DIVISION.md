# Short positive integer relations across one ordered cycle

Let an ordered three-band rational Collatz cycle have odd period \(p\), total shortcut clock \(h\), odd minimum \(s\), and complete reduced denominator \(d\) coprime to six. Use the lifted ranks and marks of the [window theorem](../../astra-unconventional-20261126/arithmetic/README.md). Thus \(4s\le Z_r<8s\) and \(c_r\in\{1,2,4\}\) on \(0\le r<p\), both quantities double on adding \(p\), and
\[
 Z_{r+h}=3Z_r+c_r .
\]
Here \(Z_r\) is rational and \(d Z_r\) is coprime to \(d\). The bounded ordinary least-disagreement case has \(d=1\). Its rank rotation is transitive. Assume \(1<h/p<2\), as on this branch.

Put \(B_j=\lfloor jh/p\rfloor,\ b_j=B_{j+1}-B_j,\ r_j=jh-pB_j\). For every \(n\ge1\), there are explicit integers \(-2\le e_j\le3\), \(0\le j\le n\), common to **all** starting ranks, for which
\[
 V_r=\sum_{j=0}^n e_j Z_{r+r_j}
 \quad\text{satisfies}\quad
 0<V_r\le Z_r2^{-B_n}+8n,\qquad
 \operatorname{den}(V_r)=d.                                      \tag{1}
\]
The labels in the sum come from \(n+1\) consecutive chronological phases. A term which crosses the rank seam uses the doubled label. All the coefficients, including those at both endpoints, are fixed before choosing \(r\).

Taking the least positive \(n\) with \(2^{B_n}\ge8s\) gives \(n=O(\log(s+2))\). On an ordinary candidate, every \(V_r\) is an integer between 1 and \(1+8n\). Some single value occurs on at least \(p/(1+8n)\) starting phases. If \(2n<p\), greedily keeping disjoint chronological windows leaves at least \(p/[(1+8n)(2n+1)]\) with that common value. The finitely many wrap choices change at no more than \(n+1\) cut points as \(r\) increases. One can consequently also fix the coefficient vector on *fundamental folded labels* throughout a subfamily of relative size at least \(1/(n+2)\). The bounds involve one candidate and its own full denominator.

## Common dyadic division coefficients

Write \(B=B_n\). For \(0\le j<n\), take the least nonnegative inverse
\[
 k_j\equiv 3^{-(j+1)}\pmod{2^{B-B_j}},\qquad
 u_j=k_j/2^{B-B_j}\in[0,1).
\]
Set \(v_0=2^{-B}\), \(v_{j+1}=2^{b_j}u_j\), \(e_j=v_j-3u_j\) for \(j<n\), and \(e_n=v_n\). The initial coefficient is \((1-3k_0)/2^B\). The interior coefficients have numerator \(k_{j-1}-3k_j\) over denominator \(2^{B-B_j}\). Multiplication by the unit \(3^j\) makes that numerator zero modulo the denominator. At the last site \(e_n=k_{n-1}\). The bounds \(0\le u_j<1\) and \(b_j\in\{1,2\}\) give the asserted integral range.

For \(Y_j=Z_{r+r_j}\), lifting first gives the same clock \(2^{b_j}Y_{j+1}=3Y_j+c_{r+r_j}\) for every \(r\). Summation yields
\[
 V_r=2^{-B}Z_r+\sum_{j<n}u_j c_{r+r_j}.                           \tag{2}
\]
Every lifted mark here is at most eight. On clearing denominators,
\[
     2^B dV_r=dZ_r+d\sum_{j<n}2^{B_j}k_j c_{r+r_j}.
\]
The integer \(dV_r\) is therefore coprime to \(d\). This gives (1) at each prime power. Substitution of the homogeneous solution gives the exact rational identity
\[
                \sum_{j=0}^n e_j 3^j2^{-B_j}=2^{-B}.                \tag{3}
\]
The [Lean module](RankDivision.lean) checks the finite summation identity, adjacent-coefficient divisibility and complete-denominator argument.

## The induced integer forcing takes both signs on every short arc

In the ordinary case extend \(V_{r+p}=2V_r\). Put \(J_r=V_{r+h}-3V_r=\sum e_jc_{r+r_j}\), an integer. With the above choice of \(n\), let \(M=1+8n\). On every sufficiently large bounded ordinary candidate, each chronological interval of length \(O(M\log(2M))\), with a sufficiently large absolute implied constant, contains both a positive and a negative \(J\).

At chronological start rank \(r\), reduce at time \(i\) to \(r_i^*=(r+ih)\bmod p\), and let \(A_i=\lfloor(r+ih)/p\rfloor\). Fundamental values \(V_i^*=V_{r_i^*}, J_i^*=J_{r_i^*}\) obey
\[
 \frac{2^{A_k}}{3^k}V_k^*=V_0^*+\sum_{i<k}\frac{2^{A_i}}{3^{i+1}}J_i^*. \tag{4}
\]
Since \(3<2^{h/p}\le3+1/s\) and \(p/s\to0\), the factors \(2^{A_k}/3^k\) are between \(1/2\) and 3 uniformly for \(k\le p\) once \(p\) is large. A run of \(l\) zero defects forces \(2^l\mid V_i^*\) at the run's beginning. Indeed each mechanical letter costs at least one factor of two, and 3 is odd. Thus no zero run is longer than \(\log_2 M\). On an interval where all defects have the same weak sign, every nonzero term on the right of (4) has absolute value at least \(1/6\). Their number is at most \(18M\) by (4). The zero-run bound then gives length at most \((18M+1)(1+\lfloor\log_2 M\rfloor)\). For growing ordinary candidates this is less than \(p\), as \(s\le p^{O(1)}\). In particular the positive linear combinations in (1) cannot themselves follow ordinary positive Collatz edges around the same circle. Their small sizes place all of them below the least bad integer \(s\) in the minimum branch.

## An effective lower bound on the number of nonzero terms

For **any** clock \(b_j\in\{1,2\}\) and any identity (3) with \(|e_j|\le3\), let \(k\) be the number of nonzero coefficients. There is an absolute effective constant \(C\) such that
\[
        k\ \ge\ 1+\frac{\log(n+1)}{\log(C\log^2(2n+2))}.             \tag{5}
\]
In particular a fixed number of bounded coefficients cannot realize the full dyadic division at increasing depths.

Multiply (3) by \(2^B\). Reduction modulo 3 forces the first nonzero index to be zero. Reduction modulo 2 forces the last to be \(n\). For consecutive nonzero indices \(a<b\), write
\[
 U=\sum_{j\le a}e_j3^j2^{B_a-B_j},\qquad v=B-B_a>0.
\]
Then \(2^vU\equiv1\bmod 3^b\), \(3\nmid U\), and \(\log(2|U|)\ll a+1\) since \(|U|\le3(a+1)12^a\). The integer \(2^vU-1\) is nonzero because the product is even.

If \(|U|=2^w\), squaring and the lifting-the-exponent identity at 3 give \(b\le1+v_3(v+w)\ll\log(2n+2)\). Otherwise \(4,U^{-2}\) are multiplicatively independent positive rational 3-adic units congruent to 1 modulo 3. Apply the two-logarithm bound to \(4^v-U^{-2}\), with \(p=3,\ g=E=1,\ b_1=v,\ b_2=1\). Its 3-adic valuation is at least \(b\). One may take \(\log A_1=\log4\) and \(\log A_2=\max\{2\log|U|,\log3\}\). Since \(v\le2n\), the displayed bound gives \(b\ll(a+1)\log^2(2n+2)\) with effective constants. Iteration from 0 to \(n\) proves (5). [Bugeaud and Laurent, Théorème 3](https://irma.math.unistra.fr/~bugeaud/travaux/logpadicdef.pdf) · [Bennett, Bugeaud and Mignotte, Theorem 6, equation (2.2)](https://irma.math.unistra.fr/~bugeaud/travaux/BBM-Cambridge.pdf)

The [exact replay](check_rank_division.py) checks (3) on all 8,190 binary mechanical calendars through length twelve and (1) at every rank of the three earlier positive rational controls. On the 41-phase control its nine-step image retains denominator 44,835,377,399 at every rank and has integer defects ranging from \(-14\) to 16. [Replay output](../../../reports/astra-six-hour-20261127/arithmetic/RANK_DIVISION.json) · [Rational control source](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/reports/astra-unconventional-20261126/cycle/control.json)

The native denominator persists exactly in (1), and an ordinary candidate would have many repeated short integer relations. The signed forcing in (4) prevents identifying those positive values with a smaller cycle by the same affine dynamics. The calculation provides no contradiction to the original cycle.
