# Pointwise spacing of cycle ranks through amplitude \(p^{11/20}\)

**PROPOSED written theorem with external analytic inputs.** Put \(e(t)=\exp(2\pi it)\), \(\lambda=\log 2\), and let \(p\) be a positive integer. For fixed \(C_0,C_1,c>0\) and every \(\epsilon>0\),
\[
 \#\{0\le i,j<p:\ \|R(2^{j/p}-2^{i/p})\|\le C_0/p\}
       \ll_{\epsilon,c,C_0,C_1}p^{1+\epsilon},
 \qquad c\le R\le C_1p^{11/20}.                                    \tag{1}
\]
The norm is distance to the nearest integer. The amplitude is fixed throughout the count. The analytic inputs are the Lindelöf bound for the Riemann zeta function and Robert–Sargos's fourth derivative estimate. The November 2026 MIT verification record supplies RH, which implies Lindelöf. The external formalization was not independently replayed here. [MIT verification record](https://math.mit.edu/~drew/grh/) · [Ivić, equation (5.1)](https://www.impan.pl/shop/en/publication/transaction/download/product/83063) · [Robert and Sargos, Theorem 1, equation (1.6)](https://perso.univ-st-etienne.fr/rool6510/compositiorobertsargos.pdf)

## Smooth dual sums

Choose a fixed nonnegative smooth compactly supported \(w\) on the real line with \(w\ge1\) on \([0,1]\). Take \(J=\lfloor\kappa p\rfloor\) for a sufficiently small fixed \(\kappa=\kappa(C_0)>0\). The kernel \(J^{-2}|\sum_{0\le u<J}e(ut)|^2\) is nonnegative and bounded below on \(\|t\|\le C_0/p\). Its Fourier coefficients are at most \(1/J\). Enlarging the weighted pair population to all integer indices gives the upper bound
\[
        O\left(p+\frac1p\sum_{h=1}^{J}|S_h|^2\right),\qquad
 S_h=\sum_{i\in\mathbb Z}w(i/p)e(hR\exp(\lambda i/p)).
\]
The nonnegativity of the kernel justifies enlargement even though the terms in \(S_h\) have varying arguments.

Put \(T=hR\). Poisson summation gives the integrals \(p\int w(u)e(T\exp(\lambda u)-kpu)\,du\). Their only stationary frequencies have \(k>0,\ k\asymp T/p\). With \(u_k=\lambda^{-1}\log(kp/(\lambda T))\), the stationary main term is
\[
 \sqrt{\frac{p}{\lambda k}}\ w(u_k)e(1/8)\,
 e\left(\frac{pk}{\lambda}\left[1-\log\frac{pk}{\lambda R}\right]\right)
 h^{2\pi i pk/\lambda}.                                           \tag{2}
\]
The phase and second derivative at the saddle are \(kp/\lambda-kpu_k\) and \(\lambda kp\). Uniform one-dimensional stationary phase on a fixed enlarged range \(k\asymp T/p\) has integral error \(O_w(T^{-3/2})\) before the factor \(p\). Indeed translating by \(u_k\) gives a normalized phase with uniformly positive quadratic part and bounded derivatives near zero, and translated smooth amplitudes with uniform seminorms. A smooth cutoff isolates the saddle, including when the amplitude vanishes there. Outside the enlarged positive derivative range integration by parts gives \(O_{A,w}((T+p|k|)^{-A})\) for \(T\ge1\). Hence for \(T/p\gg1\) the total error in \(S_h\) is \(O_w(1)\).

There are \(O_c(1)\) frequencies with \(T\le1\), each with \(|S_h|\ll p\). For \(1\le T\ll p\), the zero frequency contributes \(O_w(p(1+T)^{-2})\). There are \(O_w(1)\) possible nonzero stationary frequencies, and these occur only for \(T\asymp p\), when each integral times \(p\) is \(O_w(\sqrt p)\). For \(T\) a sufficiently small multiple of \(p\) the nonzero frequencies sum to \(O_w(1)\) by integration by parts. The contribution from \(T\ll p\) to the Fejér bound is therefore \(O_c(p)\).

Group the other \(h\) in possibly truncated dyadic intervals \(H\le h<2H\). Put \(K=HR/p\gg1\). All dual indices in (2) can be restricted to a fixed interval \([c_wK,C_wK]\) for that entire block. After squaring and dividing by \(p\), the diagonal \(k=\ell\) contributes \(O(H)\). For a fixed nonzero difference \(d=k-\ell\), the \(h\)-oscillation is \(h^{2\pi i p d/\lambda}\). Ivić's Lindelöf estimate bounds every subinterval sum on this block by \(O_\epsilon(\sqrt H\,(p|d|)^\epsilon)\), since \(H\ll p|d|\). Partial summation permits the bounded-variation weights in (2). Summing \(k,\ell\) separately gives \(O_\epsilon(p^\epsilon K\sqrt H)\) for the off-diagonal part of a block, after rescaling \(\epsilon\). This settles the blocks \(K\le\sqrt p\).

## The correlated sum over dual ranks

For \(K>\sqrt p\) keep the phase of \(\ell\) after the \(h\)-sum. Fourier inversion separates each \(w(u_k)\) into imaginary powers of \(k\) and \(h\) with rapidly decreasing transform. Do this for both factors before summing. Truncating the two transform variables at \(p^{1/10}\) costs \(O_A(p^{-A})\) after the sums by rapid decay, with the decay order chosen for the polynomial parameter range. The \(h\)-frequency is changed by \(O(p^{1/10})\), so its magnitude is still comparable to \(p|d|\). Use the Ivić estimate at this shifted frequency. In the remaining \(\ell\)-sum the extra powers have partial-summation cost \(O(1+|t_1|+|t_2|)\) relative to the \(O(1/K)\) size of \(1/\sqrt{\ell(\ell+d)}\). This cost is integrable against the two transforms. Both index intervals \(\ell,\ell+d\in[c_wK,C_wK]\) are fixed for the whole \(h\)-block.

Take \(d>0\), the other orientation giving the conjugate contribution before Fourier separation. Up to a constant depending only on \(d\), the remaining phase is
\[
 f_d(v)=-\frac p\lambda\big((v+d)\log(v+d)-v\log v\big).
\]
On the interval \(v,v+d\asymp K\) one has \(|f_d^{(4)}(v)|\asymp pd/K^4=\Lambda_d\), with constant sign. This follows from \((v\log v)^{(4)}=2/v^3\) and the mean value theorem. Here \(d\ll K\) and \(K>\sqrt p\) imply \(\Lambda_d\ll p/K^3=o(1)\). On every subinterval, Robert–Sargos give
\[
 \left|\sum_\ell e(f_d(\ell))\right|
 \ll_\epsilon K^\epsilon\left(K\Lambda_d^{1/13}+\Lambda_d^{-7/13}\right).
\]
Lengths below a fixed constant satisfy this estimate trivially. Multiplying by the weighted \(h\)-bound, dividing the square by \(p\), and summing over \(d\ll K\) bounds the block's off-diagonal contribution by
\[
 \ll_\epsilon p^\epsilon\sqrt H\,
 \left(p^{1/13}K^{10/13}+p^{-7/13}K^{21/13}\right).              \tag{3}
\]
In particular \(\sum_{d\ll K}d^{-7/13}\ll K^{6/13}\). Since \(H\ll p\) and \(K\ll R\ll p^{11/20}\), the two powers of \(p\) on the right of (3), before \(p^\epsilon\), are at most \(1\) and \(17/20\), respectively. Summing the logarithmically many blocks and adjusting \(\epsilon\) proves (1).

## The three-band cycle consequence

Use the exact hypotheses from the [previous inverse-wrap bound](../../astra-unconventional-20261126/arithmetic/INVERSE_WRAP.md). Thus \(p\) is the primitive odd period, \(s\) the real minimum, \(d\) the complete reduced denominator, the gaps are one or two, the physical phases are in \([s,(16s+7)/3]\), and the folded phases have the ordered dyadic rotation. For rational cycles this ordering is a hypothesis; the indicated ordinary bounded branch supplies it. Write \(\delta=479/1000\).

The incoming-word count allows \(O(Q^\delta)\) residues of the integer folded numerators \(N_r\) modulo \(Q=3^b\). The rank envelope is \(N_r=4ds\,2^{r/p}+O(dp)\), uniformly in the octave choices. At \(s\le p^2\) the earlier elementary terminal count already gives \(p\ll(ds)^\delta\). For \(s>p^2\), take the least power of three
\[
                 Q\ \ge\ d\max\{p^2,s/p^{11/20}\}.
\]
Then \(R=4ds/Q\) lies between a fixed positive constant and \(4p^{11/20}\); the normalized envelope has error \(O(1/p)\). Every pair with the same literal residue obeys the inequality in (1). By Cauchy–Schwarz at least \(p^{1-o(1)}\) residue classes are occupied. Their incoming-word upper bound implies
\[
 d\max\{p^2,s/p^{11/20}\}\ \ge\ p^{1000/479-o(1)}.
\]
In particular an unbounded sequence in the ordinary bounded least-disagreement branch would satisfy
\[
       \liminf \frac{\log s}{\log p}\ \ge\ \frac{1000}{479}+\frac{11}{20}
       =2.63768\ldots .
\]
This strengthens the earlier \(1000/479+1/3\) threshold. Taking the source-qualified irrationality measure three for \(\log_2 3\) still permits \(s\) as large as \(p^{3+o(1)}\). In that remaining range the long dual correlations at \(d\asymp K\) in (3) cost too much. Neither this census nor its rational-denominator version excludes every cycle or an escaping ordinary orbit.
