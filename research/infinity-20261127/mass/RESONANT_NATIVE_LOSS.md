# Same-source loss at the native height of the dyadic odd-clock gate

**Status.** Proposed written estimates on the positive odd map. The local arithmetic construction has a separate Lean implementation. The full first-moment loss of PR200 remains open.

Use the accelerated map \(U(x)=(3x+1)/2^{v_2(3x+1)}\), the actual positive exponents \(e_i\), their prefix sums \(A_i\), and \(a=7/4\). A word passes when \(A_i\le ai\) for every prefix. Its principal source is its unique positive odd representative below \(2^{A+1}\), where \(A\) is the complete exponent sum. At odd depth \(r\), write \(P_r\) for passing probability under the original independent law \(\Pr(e)=2^{-e}\), and \(J_r\) for the sum of the reciprocals of the actual principal sources of passing words. For old sources already counted in \(J_n\), let \(D_{n,n+1}\) be the reciprocal mass failing for the first time at \(n+1\). When \(4\mid n\), set
\[
 L_n=\sum_{\substack{m\text{ principal and passing at } n\\m\ge 2^{an-4}}}1/m,
 \qquad
 L_n^{\rm die}=\sum_{\substack{m\text{ in this same sum}\\A_{n+1}(m)>a(n+1)}}1/m.
\]

## The estimate

Put \(\gamma=(7/8)(7/6)^{3/4}<1\). For \(n=2^k,\ k\ge55\), absolute constants give
\[
 c\,n^{-3/2}\gamma^n \le L_n^{\rm die}\le L_n\le C\,n^{-3/2}\gamma^n,\qquad
 D_{n,n+1}\ge L_n^{\rm die}\ge c' P_n.                                  \tag{1}
\]
A fixed fraction of the **entire passing reciprocal population in these five native octaves** dies on the very next actual ordinary odd step. A fixed fraction of the original passing word probability also lies on the witnesses in (1). If \(B_r\) denotes actual new reciprocal mass born from depth \(r\) to \(r+1\), then
\[
                  D_{n,n+1}\ge c''\sum_{r\ge n}B_r.                       \tag{2}
\]
The sum in (2) accounts for births after the selected dyadic depth. The next exponent is calculated on each same old ordinary source.

## Three suffixes for every boundary parent

Fix any passing word of \(p=n-32\) gaps with \(A=7p/4\). Let \(m<2^{A+1}\) and \(y=U^p(m)\) denote its true principal source and endpoint. The sources \(m_j=m+2^{A+1}j\) follow the same prefix to \(y_j=y+2\cdot3^p j\). For a 32-gap suffix \(w\) of total 56, put
\[
 C_w=\sum_{i=0}^{31}3^{31-i}2^{A_i(w)},\qquad Q=2^{56}.
\]
The suffix is a legal path to a positive odd \(z\) precisely when
\[
                   Qz=3^{32}y+C_w+2\cdot3^n j.                           \tag{3}
\]
Integer compositional inversion from an odd terminal recovers every intermediate positive odd state and its exact valuation by the earlier OrdinaryGapWord.path_of_affine theorem. The interval \(0\le j<Q\) selects a principal source of the full word. In the table a superscript on a parenthesized word means repetition.

| Chronological suffix \(w\) | \(C_w\) | \(C_w/Q\), approximate |
|---|---:|---:|
| \((1)^{31},25\) | 1,853,015,893,884,545 | 0.0257 |
| \((1)^{27},22,1,2,2,2\) | 58,710,943,741,132,417 | 0.8148 |
| \((1,2,2,2)^8\) | 150,865,148,058,652,885 | 2.0937 |

Each row passes its entire local gate and ends exactly on its boundary. Factoring successive squares gives \(2^{k+2}\mid 3^{2^k}-1\) for \(k\ge1\). For \(k\ge55\) it follows that \(2\cdot3^n\equiv2\pmod{4Q}\). Put \(s=3^{32}y\), which is odd. We need
\[
 (s+C_w+2j)\bmod 4Q=Q,\quad Q/32\le j<Q.                              \tag{4}
\]
On the circle of circumference \(4Q\), the three listed integers have every successive circular gap strictly less than \(31Q/16\), including the wraparound gap. Hence their translates of the half-open interval \([Q/16,2Q)\) cover the circle. Apply the cover to \(Q-s\). The selected residue \(2j\) is even, since \(s\) and \(C_w\) are odd. This proves (4) for every parent phase.

Equation (3) gives a positive integer \(z\equiv1\bmod4\). Its true next exponent is at least two. The word ends at \(A_n=7n/4\), so the gate at \(n+1\) allows at most one. The bounds on \(j\) and \(m\) give
\[
                2^{an-4}\le m_j < 2^{an+1}.
\]
Different parents yield different integers by forward determinism. The same selected source is counted in \(J_n\) and removed in the step to \(J_{n+1}\).

## Counting the parents and the full original gate

For \(4\mid p\), there are at least \(p^{-1}\binom{7p/4-1}{p-1}\) passing \(p\)-gap words of total \(7p/4\). Among the positive compositions, rotation to a maximum of \(A_i-7i/4\) supplies a passing word, and each image has at most \(p\) preimages. Multiplication by \(2^{-an-1}\) and Stirling's inequalities prove the lower bound in (1). Each selected word itself has original mass \(2^{-an}\).

For every \(r\ge1\), the original gate satisfies
\[
                             P_r\ll (1+r)^{-3/2}\gamma^r.                \tag{5}
\]
Encode each odd gap by one \(+3\) step followed by \(e-1\) steps of \(-4\). The encoded walk stays nonnegative precisely when the original word passes. At length \(E=A_r\) its terminal height is \(h=7r-4E\ge0\). Tilt the encoded steps to probabilities \(4/7,3/7\), giving centered independent bounded increments.

For either this centered walk or its negative, the probability starting at \(v\ge0\) of staying nonnegative for \(l\) steps is \(O((v+4)/\sqrt{l+1})\). Take integral \(M\asymp\sqrt l\). For \(v<M\), stop at the first departure from \([0,M)\) or at time \(l\). The stopped position lies in \([-4,M+4]\). Optional stopping of the position bounds the upper-exit probability by \((v+4)/(M+4)\). The pointwise inequality \((X+4)(M+4-X)\ge0\) and optional stopping of \(X_t^2-t\operatorname{Var}(X_1-X_0)\) give expected stopped time \(O((M+4)(v+4))\). Markov's inequality bounds the probability of no exit by time \(l\). For \(v\ge M\) the result is immediate.

Split a bridge of \(E\) steps into three consecutive pieces with lengths within one of \(E/3\). Its first piece stays nonnegative from zero, and its last piece in reverse stays nonnegative from \(h\) with sign-reversed increments. Upon fixing these independent pieces, the specified terminal height determines the displacement of the middle piece. Its greatest point mass is \(O((1+E)^{-1/2})\) by the binomial formula and Stirling. The constrained endpoint probability under the tilt is consequently \(O((1+h)(1+E)^{-3/2})\).

On words with terminal clock \(E\), recovering the original weight multiplies by
\[
       \frac{2^{-E}}{(4/7)^r(3/7)^{E-r}}
          =\gamma^r(6/7)^{7r/4-E}.
\]
Since \(E\ge r\), summing the geometrically weighted linear bound in \(h=4(7r/4-E)\) proves (5), including nonintegral \(7r/4\). Every source in \(L_n\) has \(1/m\le16\cdot2^{-an}\le16\cdot2^{-A_n}\), giving \(L_n\le16P_n\). The original principal sibling inequality bounds \(B_r\le P_r\). Summing (5) and applying the lower bound of (1) proves (2).

## The sub-native head

At \(J_n\) a fixed passing source contributes precisely \(1/m\). It can lie below \(2^{an-4}\) at every large depth. The lower bound in (1) is summable even over every positive integer \(n\), whereas PR200 requires a divergent cumulative fractional loss relative to \(J_{2^k}\). Formula (2) compares the loss to all future births, whose total is itself finite. It gives no comparable fraction of a fixed old atom. The estimate \(D_{2^k,2^{k+1}}\ge c J_{2^k}/(k+1)\) remains open.

[PR200 quantitative target](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/NEXT_FIRST_MOMENT_TARGET.md) · [PR200 original joint gate](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/JOINT_GATE_FRACTIONAL_PRESSURE.md) · [PR201 principal sources](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md) · [PR201 sibling inequality](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/escape/HarmonicBirth.lean).
