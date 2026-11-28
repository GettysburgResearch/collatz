# The full reduced denominator of an exceptionally long rational residence

**Proposed written theorem.** Let \(x_0,\ldots,x_{T-1}\) be distinct positive odd rational Syracuse states of a single true trajectory in \([M,RM]\) for fixed \(2<R<4\), \(M\to\infty\). Their common complete reduced odd denominator \(Q\) is prime to six; all odd valuations are genuine. Put \(\theta=0.3197044778974\ldots,\ \Lambda=(7\theta-1)/3\), as in the [ordinary residence theorem](UNIFORM_SUBFOUR_RESIDENCE.md). Assuming the cited \(\mu(\log_23)\le3\), every sequence with \(\liminf\log T/\log M\ge\lambda>\Lambda\) satisfies
\[
 \liminf\frac{\log Q}{\log M}\ \ge\
  \min\left\{\frac1{3\theta}-1,\
                   \frac{3\lambda-7\theta+1}{3+7\theta}\right\}.        \tag{1}
\]
For example \(T\ge M^{1/2-o(1)}\) forces \(Q\ge M^{0.04262\ldots-o(1)}\). The theorem applies to finite nonperiodic runs; neither the existence of a rational cycle nor a return calendar at either endpoint is required.

For **every** moving \(Q=M^{o(1)}\), the full width-dependent ordinary bounds of [open matched rates, (1)–(2)](OPEN_MATCHED_WIDTH_RATES.md) hold verbatim on these rational runs, under the same irrationality-measure hypotheses. In particular the exponent \(r_R\) there applies with the classical \(\mu_0=5.116201\) wherever \((\mu_0+1)r_R\le1\). There is no order or square-resonance hypothesis on the supplied denominator in either assertion.

## A sector in each actual return fiber

Consider subsequences with finite \(\beta=\lim\log Q/\log M\), and first assume \(\beta<\beta_*=1/(3\theta)-1\). The [finite physical prefix count at complete \(Q\)](COMPLETE_DENOMINATOR_BAND_EXITS.md) gives \(T\le Q M^{v+o(1)}+O(\log M)\), \(v=0.4333973955184\ldots\). Indeed each of \(O_R(1)\) dyadic shells meets the band, all but the last \(O(\log M)\) true starts have the required following window, and distinctness makes this a count of actual starts. Thus \(\lambda_0=\lim\log T/\log M\le v+\beta<1/2\) on a further subsequence. The exact source pin is [prior four-copy proof, commit 5136b7f](https://github.com/GettysburgResearch/collatz/blob/5136b7fe70176172405a0de168a2de2ed26429b8/research/astra-global-rigidity-20261128/cycles/FOUR_COPY_WIDTH.md).

Let \(h/b\) be the convergent of \(\gamma=\log_23\) with \(b\le T<b'\). In the [one-sheet native sampling proof](CONFINED_CONVERGENT_GAPS.md), the label \(H_t\) of a signed pair comparison now belongs to \(Q^{-1}\mathbb Z\), but \(H_{t+1}=0\) still implies \(H_t=0\): \(3QH_t=-Qd_t,\ |d_t|\le2,\ \gcd(Q,3)=1\) forces \(d_t=0\). The prime-11 step involves the bounded *integer* tags. At both the dilated comparison and the terminal code, use \(QH_t\in\mathbb Z\) for the full divisor over \(O(\log(QM))\) genuine edges. These changes are proved in detail in the [complete-denominator native-tube argument](COMPLETE_DENOMINATOR_BAND_EXITS.md). Its use here is on the one-sheet grid with \(U_0=b/(\log M)^3\) up to a fixed multiplicative constant. The true-time rectangle still follows from equality modulo \(b\) of two time sums with \(4U_0<b\), and distinct labels are genuine distinct odd rays. The shape and area estimates are unchanged. Thus \(\alpha-(3\alpha-1)_+/3\le\theta(1+\beta)\) for \(\alpha=\lim\log b/\log M\), by the same \(O(b^3/M)\) rectangle count and alteration. Small \(b=M^{o(1)}\) already satisfies the desired bound. Since \(\theta(1+\beta)<1/3\), one has
\[
          \alpha\le\theta(1+\beta),\qquad
          \xi=\lim\log b'/\log M\le2\alpha,\qquad
                         \alpha+\xi<1.                                \tag{2}
\]
The second inequality uses the imported measure bound. The open horizon and all polynomial-height estimates fit since we are interested only in polynomially long runs.

Let \(Q_{\rm s}=\prod_{\ell\mid Q}\ell^{\lceil v_\ell(Q)/2\rceil}\), with \(Q_{\rm s}=1\) when \(Q=1\). Define \(d=\operatorname{ord}_{Q_{\rm s}}(3^b2^{-h})\), using \(d=1\) for modulus one. Then \(d\le Q_{\rm s}\le Q\) and
\[
                           Q\mid(3^{db}-2^{dh})^2 .                    \tag{3}
\]
Use the all-sheet reduced-rank cell of the ordinary open theorem, with signed true times from an interval of length \(U=\lfloor T/(\log M)^{10}\rfloor\). In each coarse rank \(j\) keep a most populous residue class of the **sheet index** \((s-s_j)/b\bmod d\), where \(s_j\) is any observed time at that rank. No common class across different ranks is needed. Thus the combined retained population is at least \(M^{\lambda_0-\delta-o(1)}\), where \(\delta=\lim\log d/\log M\le\beta\). If it is larger we may restrict it to that exponent. For the following argument assume \(\lambda_0>\alpha+\delta\); otherwise \(\lambda_0\le\theta(1+\beta)+\delta\) already.

The sampled vertical lattice in each retained rank now has true stride \(db\) and deweight \(dh\). Its length through the native interval is \(N\asymp T/(db)\ge M^{\epsilon}\) for some fixed \(\epsilon>0\). The angle error obeys \(d|b\gamma-h|\ll d/b'\to0\), since \(db=o(T)\) and \(b'>T\); thus \(dh\) is the nearest integer to \(db\gamma\) for large \(M\). The entire local binary chart is valid because its total true slope displacement is \(O(T/(bb')+T/M)=o(1)\). The [rational native-return theorem](NATIVE_RETURN_CURVATURE.md) and (3) give strict same-sign curvature along these vertical labels. They have polynomially bounded integer heights after multiplication by the **original** \(Q\), since \(QM\) is polynomial in \(N\). If any four-term collision in the retained rank occurred, its zero would propagate backward by the preceding complete-\(Q\) observation. The same short vertical polynomial would then annihilate a strictly curved sequence of \(N\) such integers, contradicting the [positive-filter theorem](CONVEX_RETURN_FIBERS.md). Thus each retained rank is actually Sidon. The full divisor (3) is obtained even when its underlying element lacks linear resonance modulo \(Q\).

## Counting on the thinner vertical lattice

The shape, strict ordering, and characteristic-eleven equalities for the two spectra in the [all-sheet proof](UNIFORM_SUBFOUR_RESIDENCE.md) apply: (2) gives \(bb'=o(M)\), and \(bU/M=o(1)\) by \(\lambda_0<1/2\). Use the stated reverse-zero and \(Q\)-scaled forward steps. At two positive coarse gaps \(i,j\), the area inequality is \(ij\ll b^2U/M\), and each fixed coarse rank has at most \(1+U/(db)=O(U/(db))\) selected times. The smallest source therefore has \(O((U^3/(d^2M))\log M)\) such candidate relations, since the two middle labels determine the fourth. At one zero gap and one positive coarse gap \(j\), write \(k\ge1\) for the lower source separation in retained vertical steps **of length \(db\)**. The homogeneous increment is \(\gg dk/b'\), so \(kj\ll bb'U/(dM)\). At the upper retained rank at most one ordered pair has the required positive physical label difference. This gives \(O((bb'U/(dM))\log M)\) candidates. Four labels in a single retained rank contribute none.

Consequently the total nontrivial pair collision count is at most the actual population times \(M^{z+o(1)}\), where
\[
                 z=\max\{0,\,3\lambda_0-1-2\delta,\
                               \lambda_0+\alpha+\xi-1-\delta\}.
\]
We can use the full retained set here. Its exponent \(x\ge\lambda_0-\delta\) exceeds \(z\), by \(2\lambda_0<1,\ \alpha+\xi<1\), and \(\lambda_0>\alpha+\delta\). The native binary mixed code of \(n=\lceil\log_3(32RQM)\rceil+3\) forward rows has the same retained singleton/matching frequencies as before, while its size-budget exponent is now \(\theta(1+\beta)\). The controlled-collision entropy lower and upper bounds give
\[
                 \lambda_0-\delta\le\theta(1+\beta)+z/4 .              \tag{4}
\]
This inequality retains the order of the complete modulus's square-resonance class independently of its height cost.

If \(z=0\), we get \(\lambda_0\le\theta(1+\beta)+\delta\), also the bound from the short vertical case. If \(z=3\lambda_0-1-2\delta\), we obtain \(\lambda_0\le4\theta(1+\beta)-1+2\delta\). Otherwise (2) and (4) give \(3\lambda_0\le7\theta(1+\beta)-1+3\delta\). On \(0\le\beta\le\beta_*\), the affine bound \((7\theta(1+\beta)-1)/3+\beta\) dominates the first two bounds after \(\delta\le\beta\). For the first, its excess is \((4\theta(1+\beta)-1)/3>0\). For the second its excess is \((2-5\theta(1+\beta)-3\beta)/3>0\), since \(\theta(1+\beta)\le1/3\) and \(\beta_*
<1/9\). Thus \(\lambda_0\le\Lambda+(1+7\theta/3)\beta\). Taking the alternatives \(\beta\ge\beta_*\) or this inequality proves (1).

When \(Q=M^{o(1)}\), both \(\beta\) and \(\delta\) vanish. The same one-sheet argument using the active row fraction and the actual width \(R\) gives \(\alpha\le r_R\) by [the width-dependent proof](OPEN_MATCHED_WIDTH_RATES.md). Under \(\mu_0r_R<1\), (2) becomes \(\alpha+\xi\le\mu_0r_R<1\). The retained population exponent, the dyadic coding horizon exponent and both collision exponents then agree with their ordinary values in that proof. Its alteration estimate and controlled-collision estimate give precisely equations (1)–(2) there. This yields the full subpolynomial-denominator claim including all terminal branches.
