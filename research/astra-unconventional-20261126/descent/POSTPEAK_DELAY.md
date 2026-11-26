# A fixed hard exponent can delay comparison with every earlier peak

**Kernel-checked fixed exponent theorem.** For \(k\ge1\), set
\[
 m=12\cdot2^{18k}-1,\qquad j=2(2^{18k}-1)/27,\qquad H=18k+4.
\]
Then \(m=11+162j\) and \(H=\lfloor\log_2 m\rfloor+1\). For **every** \(1\le t<m\) and all independently chosen clocks \(0\le i,l\le H\),
\[
               T^i(3^m-1)\ne T^l(3^t-1).
\]
The same explicit family has cofinally many \(j\) in every prescribed residue class modulo any power of three. It permits simultaneous changes of the earlier exponent and both clocks at the fixed ordinary parent. The ordinary separation is the unconditional Lean theorem `explicit_delayed`, in fact for every integer exponent \(12\cdot2^b-1\) and every \(t\) from zero upward. The cofinal ordinary choices at each prescribed ternary address are also kernel-checked. [Cofinal hard-index theorem](DelayAddresses.lean) This proves a delay for postpeak meetings. The parents can still have other reductions, including meetings after this window. [Strict ordinary theorem](SignedDelay.lean) · [Physical replay](postpeak_check.py) · [Replay output](../../../reports/astra-unconventional-20261126/descent/postpeak_delay.json) · [Density-one postpeak descent](POSTPEAK_DENSITY.md) · [Earlier all-exponent criterion at a different raw checkpoint](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/unbounded-queries/ALL_EARLIER_MERSENNE_RESCUE.md)

## A signed peak disjoint from all its predecessors

Give an odd-denominator rational its numerator parity and use \(T(x)=x/2\) on even inputs and \(T(x)=(3x+1)/2\) on odd inputs. The peak at the signed exponent \(-1\) is
\[
       3^{-1}-1=-2/3\ \longmapsto\ -1/3\ \longmapsto\ 0\ \longmapsto\ 0.
\]
For \(r\ge2\), the rational \(b_r=3^{-r}-1\) never reaches zero. Its numerator is even, and the first even step puts it strictly above \(-1/2\). Additional even steps keep the value negative and above that threshold. The first odd step cannot send it to zero, because its reduced denominator before that step is still \(3^r\), whereas the only odd preimage of zero is \(-1/3\). If its first odd step stays negative, the new value is greater than \(-1/4\). All additional even steps keep it above \(-1/4\), and its next odd step is strictly positive. Positive values remain positive. Thus \(b_r\) cannot meet any of \(-2/3,-1/3,0\), since each of those then reaches zero. This disjointness holds with independently chosen clocks of any lengths.

## Lifting signed disjointness to one positive source

For any hard \(m\) and \(H\ge1\) satisfying \(2^H\mid 3^{m+1}-1\) and \(m\ge3H+1\), put \(s=m-t\). We first exclude \(s\ge H\) without using the signed reference. For \(n\ge1\) one has \(T(n)\ge n/2\) and \(T(n)+1\le(3/2)(n+1)\). Hence a meeting by \(i,l\le H\) would imply
\[
     3^m-1\ \le\ 3^H3^{m-s}-2^H .
\]
For \(s\ge H\) this contradicts \(2^H>1\).

It remains to exclude \(1\le s<H\). The two positive inputs \(3^m-1,3^{m-s}-1\) agree modulo \(2^H\), respectively, with the odd-denominator rationals \(3^{-1}-1,3^{-1-s}-1\). Indeed each difference is an odd-denominator unit times \(3^{m+1}-1\). The matching first \(H\) binary decisions follow by induction, losing at most one bit at each clock.

For any legal binary word of \(i\) clocks and \(p\) odds applied to \(3^m-1\), write its output as
\[
   (3^p3^m+B_i-3^p)/2^i .
\]
The usual recurrence gives \(0\le B_i\le3^i-2^i\), including \(B_0=0\). Consequently \(A_i=B_i-3^p\) has \(|A_i|\le3^i\). Write \(q,A'_l\) for the corresponding data on the earlier peak. An ordinary meeting gives
\[
 (2^l3^{s+p}-2^i3^q)\,3^{m-s}=2^i A'_l-2^l A_i .
\]
The right side has absolute value at most \(2\cdot6^H\). But \(m\ge3H+1\) and \(s<H\) give \(3^{m-s}>2\cdot6^H\). Thus both the integer coefficient and the right side vanish. The same affine equality must hold on substitution of \(3^{-1-s}\) for \(3^{m-s}\). The same words are legal there, contradicting the signed disjointness. This proves the stated exclusion for the entire original parent.

For \(m=12\cdot2^{18k}-1\), the elementary identity \(v_2(3^{2d}-1)=3+v_2(d)\) gives \(v_2(3^{m+1}-1)=18k+4=H\). Also \(m\ge3H+1\) for \(k\ge1\). Finally \(2^{18}-1=27\cdot9709\) with \(3\nmid9709\). Cubing a number \(1+3^r u\), \(r\ge1,\ 3\nmid u\), increases the valuation of its difference from 1 by exactly one. Therefore
\[
 v_3\!\left(2(2^{18(k+3^d)}-2^{18k})/27\right)=d .
\]
At each step the three candidates \(k,k+3^d,k+2\cdot3^d\) have distinct next digits in \(j\). Starting with modulus one lifts every prescribed finite ternary address. Taking larger members of the same \(k\)-progression gives cofinal ordinary exponents.

The Lean proof uses an equivalent arithmetic separation that avoids expanding individual finite words. Set \(d=3^{s+1}\) and \(M=(3^{m+1}-1)/2^H\). Use the integer numerator at the common denominator \(d\). The ordinary and signed upper numerators differ by \(2^HM3^s\), and the lower ones differ by \(2^HM\). Thus the signed and ordinary numerators still agree modulo \(M\) through \(H\) clocks. Each signed numerator has absolute value at most \(2^Hd\), by induction from \(|a|\le d\). For the explicit \(m=12\cdot2^b-1,\ H=b+4\), the kernel verifies \(M>2\cdot2^H3^H\) by repeated squaring from \(3^{12}=1+16\cdot33215\). The gap bound gives \(d\le3^H\). An ordinary meeting forces equal signed values modulo \(M\) in an interval shorter than \(M\), hence an actual signed meeting. The proof uses the same ordinary natural-number map as the other files in this directory.

## Extending from the peak to the complete initial ascent

There is an elementary extension at a reduced original deadline. Let \(U_m=3^m-1\), and take \(i\le\lfloor H/3\rfloor\). The original \(T^iU_m\) cannot meet any earlier \(2^t-1\) from its very first clock through its entire ascent and \(H\) clocks beyond its peak. Indeed, an earlier ascent value with \(b\) odd steps remaining is \(3^t(2/3)^b-1\). If \(b\ge2i\), this is strictly below \(U_m/2^i\), since \(t<m\) and \((2/3)^2<1/2\). Equality would therefore force \(b<2i\). Following those \(b\) steps would then meet the earlier peak at original clock \(i+b\le H\), contradicted by the kernel theorem.

A written use of two logarithms gives the **full** original deadline and includes the original parent's entire initial ascent as well. For every sufficiently large member of the explicit sequence, with the same \(H=18k+4\), one has
\[
  T^u(2^m-1)\ne T^v(2^t-1)
  \qquad(1\le t<m,\ 0\le u\le m+H,\ 0\le v\le t+H).
\]
To prove the extra mixed-phase cases we establish a stronger estimate valid for every sufficiently large \(m\), independently of the explicit binary congruence. Fix \(1\le t<m\) and \(1\le H\le m/4\). A point on the initial ascent of one input cannot meet the other input within \(H\) clocks after its peak.

Write \(r\in\{m,t\}\) for the ascending exponent, \(n\) for the other exponent, and \(0\le a\le r\) for the ascender's clock. Write \(l\le H\) for the postpeak clock and \(q\le l\) for its odd count. Using the word offset \(A_l\) defined above, an equality would give
\[
       P-Q=A_l+2^l,\qquad P=3^a 2^{r-a+l},\qquad Q=3^{n+q},
       \qquad |P-Q|\le2\cdot3^H .
\]
The main monomials are unequal. Equality would imply \(r=a,\ l=0,\ q=0,\ r=n\) by unique factorization. If \(r=t\), the basic height bound gives \((3^m-1)/2^H\le3^t-1\), which implies \(t>m-H\). If \(r=m\), the bound \(r\ge m-H\) already holds. In both cases \(P\ge2^r\ge2^{m-H}\).

The nonzero form \(\log(P/Q)=(r-a+l)\log 2+(a-n-q)\log3\) has integer coefficients of magnitude at most \(2m\). With the field and logarithms fixed, Matveev's Corollary 2.3 gives \(|\log(P/Q)|\ge c\,m^{-C}\) for effective absolute constants \(c,C>0\). A zero coefficient also follows directly from the nonzero coefficient times its fixed logarithm. For \(|\log(P/Q)|\le1\) the mean-value theorem gives \(|P-Q|\ge P|\log(P/Q)|/e\). For larger absolute log ratio one has \(|P-Q|\ge(1-e^{-1})P\). Consequently \(2^{m-H}m^{-C}\ll 3^H\), impossible for all sufficiently large \(m\) because \(H\le m/4\) and \(2^{m-H}/3^H\ge(8/3)^{m/4}\). This proves mixed-phase separation. The threshold is effective. We do not quantify it or apply it to the finite \(k=1\) replay. [E. M. Matveev, *Izvestiya: Mathematics* 64 (2000), Corollary 2.3](https://doi.org/10.1070/IM2000v064n06ABEH000314)

Finally, two initial-ascent points are distinct by unique factorization of \(3^a2^{m-a}\) and \(3^b2^{t-b}\). Two postpeak points are already distinct in the explicit binary family by the Lean theorem. Since \(18k+4\le m/4\) for \(k\ge1\), these cases establish the complete two-orbit window for all sufficiently large members. The mixed-phase logarithmic-form input and this last synthesis are written mathematics. The Lean files check the fixed positive integer, whole postpeak window and all ternary addresses.

The logarithmic time here is measured against \(m\). In the density estimate for \(J\) consecutive parameters, the time is \(\lfloor\log_2 J\rfloor\). On the exponential family these scales agree up to a constant for initial intervals of indices containing \(j\). A hypothetical least bad index would need genuine information carrying its component to many distinct hard exponents before a density-one estimate could exclude that original index. The existence of many earlier peaks, or earlier mergers at other indices, supplies no such component transport.

More explicitly, an ordinary link from \(j\) back to a hard index below a fixed \(j_0\) needs more than \(162(j-j_0+1)\) postpeak clocks by the gap inequality. A density-one set of later bad parents would still be insufficient to contradict minimality at \(j_0\) unless their comparisons cross that particular cut. At the level of labels alone, the sequence constant at one label for \(j<j_0\) and another for \(j\ge j_0\) has at most \(a\) failures of equality with \(j-a\) in any interval, including on every odd-modulus progression. This is a logical control on a proposed use of density. It asserts nothing about the actual labels.
