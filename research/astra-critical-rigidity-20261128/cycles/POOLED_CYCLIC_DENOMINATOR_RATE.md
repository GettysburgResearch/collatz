# The full chronological exponent for the near-octave denominator

**Proposed written theorem.** Consider a sequence of positive primitive rational odd cycles with minimum \(m\to\infty\), maximum \(X\), primitive odd period \(p\), total valuation \(A\), and complete reduced common denominator \(q\). Let \(r\) be the minimum degree of a nonzero rational polynomial in the chronological shift annihilating \(V_i=2^{E_i}x_i\), where \(E_i\) is the unfolded cumulative valuation. Suppose \(X/m\le 2^{1+\eta}\) and
\[
        \eta\ll(\log D)^{-\alpha},\qquad
        D=\min(r,m),\qquad \alpha>\mu_0-1,\quad
        \mu_0\ge \mu(\log_2 3).
\]
Then
\[
                    \liminf\frac{\log_3 q}{D}\ \ge\ 1.                 \tag{1}
\]
The same implication holds with \(D=\min(P,m)\), \(P=p/\gcd(A,p)\), under the width hypothesis at that scale. More generally the proof works for \(P\le R\le r\) with \(D=\min(R,m)\). In particular, along coprime clocks with \(\liminf m/p\ge1\) one has \(\log_3 q/p\to1\). Along prime-power sheet counts \(g=\gcd(A,p)>1\), the lower bound with \(D=\min(p,m)\) is at least \(1/4\) under the corresponding width hypothesis. These percentages refer to the logarithm of the complete denominator. They allow subexponential common factors of the closure numerator and determinant. The classical published two-logarithm bound suffices for every \(\alpha>4.116201\). The separately audited modern input gives every \(\alpha>2\). [Chronological rank](NEAR_OCTAVE_CYCLE_DENOMINATORS.md) · [Uniform physical drift and all-cell construction](POOLED_CYCLIC_DENOMINATOR.md) · [Classical logarithm input](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [Modern logarithm input](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

## One active cell on average

Retain the preceding construction with \(x=\log D\), \(u>1\), \(\kappa'>\mu_0-1\), \(u\kappa'<c<\alpha\), \(L=\lfloor x^u\rfloor,\ b=\lceil x^c\rceil,\ v=1/b\). This time use *all*
\(s\in S=\{0,\ldots,\lfloor D\rfloor-1\}\), still strictly below \(r\) and within the uniform-in-origin physical drift range \(s\le m\). The size of the common multiset and the true coding horizon are
\[
               h=\left\lceil\exp(x^{(1+u)/2})\right\rceil,\qquad
                  n=\lceil\log_3(64hqm)\rceil+4 .
\]
Then \(\log D=o(\log h)\), \(\log h=o(L)\), \(h<3^L\) and \(\log h=o(D)\). All native calendars, tags, binary code and \(B_h\) arguments in the [all-cell proof](POOLED_CYCLIC_DENOMINATOR.md) apply unchanged on this whole shift interval: their inputs were \(s\le m\), shift polynomial degree \(<r\) and \(h<3^L\). In particular one uses signed complete integer \(qH_i\), and the true coding window may wrap any number of full laps.

Write \(K_j\) for the cardinality of cell \(j\), and \(k_j\) for its number of active rows over the common horizon. In each nonempty cell choose a reference word. Give each of its other \(K_j-1\) words a multiplicity independently chosen in \(\{0,\ldots,\lfloor h/K_j\rfloor\}\), and fill the remaining positions with the reference. Different vectors give different padded multisets of total size \(h\). By multiset injectivity they produce different integer coordinate sums. Each variable binary coordinate has at most \(h+1\) values, so
\[
        k_j\log(h+1)\ \ge\ (K_j-1)\log(1+\lfloor h/K_j\rfloor)
                    \ \ge\ (K_j-1)(\log h-\log K_j).
\]
The right coefficient divided by \(\log(h+1)\) is \(1-o(1)\) uniformly over \(K_j\le D\). Empty cells cost nothing; the total number of nonempty cells is at most \(b=o(D)\). Consequently
\[
                         \sum_j k_j\ \ge\ (1-o(1))D.                  \tag{2}
\]

For a sharp upper bound let \(t_i=\{\log_2(V_i/J)\}\), \(J=m\sqrt{2^{1+\eta}}\), and \(t_*=\log_2(2m/J)\), which tends to \(1/2\). Within cell \(j\) the *signed* normalized log-label displacement from \(\{t_i+jv\}\) belongs to \([-e,v+e]\), where \(e=C(\eta+m^{-\delta})=o(v)\) by the true uniform drift estimate, with a fixed \(\delta>0\). If both tags occur then some label is at least \(2m\) and some is at most \(2^{1+\eta}m\). Hence an active cell satisfies
\[
                 \{t_i+jv\}\in[t_*-v-e,\ t_*+\eta+e].                 \tag{3}
\]
This interval lies inside \((0,1)\) at large \(D\). It is one grid step plus \(o(v)\). No more than two cell centers can qualify at any date, giving \(2n\ge\sum k_j\) and \(n\gg D\) from (2). If two qualify, one is in the upper strip \([t_*-e,t_*+\eta+e]\), since all grid spacings are exactly \(v\). The exceptional \(t_i\) thus belong to a union of at most \(2b\) intervals on \([0,1)\) of total length \(O(b(\eta+e))=o(1)\), allowing for wraparound.

On the actual \(n\)-row window the interval discrepancy of \(t_i\) is \(O(D^{-\delta'})\) for a fixed \(\delta'>0\). To see this take blocks of length \(H=\lfloor\sqrt D\rfloor\). Each full block shadows the rotation of slope \(\log_2 3\) with displacement \(O(H/m)\le O(D^{-1/2})\). For consecutive continued-fraction denominators \(b_1\le\sqrt H<b_1'\), one has \(b_1\gg H^{1/(2\kappa')}\). As in the all-cell proof, comparison in successive \(b_1\)-point blocks with a translated rational grid gives discrepancy \(O(1/b_1+b_1/H+H/m)\) on each full block. The terminal tail costs \(O(H/n)=O(D^{-1/2})\). The constants hold at every starting angle, so the bound survives arbitrary wraps or arbitrarily large \(q\). Summing over at most \(2b\) intervals adds \(O(bD^{-\delta'})=o(1)\) to the exceptional proportion. At only \(o(n)\) dates can a second cell qualify. This proves \(\sum_j k_j\le(1+o(1))n\). Together with (2) and \(\log m=O(\log D)\) from the reduced clock estimate, subtraction in the formula for \(n\) proves (1).

Finally, the complete denominator divides the ordinary closure determinant \(2^A-3^p>0\). The physical clock gives
\(A/p=\log_2 3+p^{-1}\sum_i\log_2(1+1/(3x_i))=\log_2 3+O(1/m)\).
It follows that \(\limsup\log_3 q/p\le1\). When \(\gcd(A,p)=1\), \(r=p\), and \(\liminf m/p\ge1\) gives \(D/p\to1\), proving the asserted limiting rate. The prime-power comparison uses the established \(r\ge p/4\).
