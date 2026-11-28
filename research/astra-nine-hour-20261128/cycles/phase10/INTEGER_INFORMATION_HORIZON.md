# A matching upper bound on the length of extreme rounding strings

Write \(F_K\) for the upward grid update in [the exact rotation theorem](../phase8/DIGITAL_ROTATION.md). In the fundamental octave it has integer edges
\[
                   2^{b_t}x_{t+1}=3x_t+r_t,\qquad K\le x_t<2K .
\]
Here \(b_t\) is the **total** winding including a possible upper-seam carry. Its value is one or two. The residual \(r_t\) is unchanged by a seam carry, lies between zero and \(2^{b_t}-1\), and need not attain the latter maximum when a carry occurs. Put \(\gamma=\log_2 3\) and \(L=\lceil\log_3(2K)\rceil\). For every sufficiently large \(K\), on every integer orbit, including its transient part, each run of dates on which \(r_t=0\) throughout or \(r_t=2^{b_t}-1\) throughout has length at most \(2L\). At the pre-seam convention for the maximal digit the bound is \(4L+1\). Thus the genuine CRT realizations through \(\log_3K+O(1)\) dates have the right order of information horizon. The proof uses a finite irrationality exponent for \(\gamma\); the classical effective Bondareva–Luchin–Salikhov bound already gives ratio exponent less than six. [Bondareva–Luchin–Salikhov, 2018](https://www.mathnet.ru/eng/cheb619) · [Exponent conventions and source review](../../phase6/RECENT_LOGARITHM_INPUT.md)

### Arithmetic injectivity of short windows

At any date, let \(\theta_t=\log_2(x_t/K)\). Then
\[
   \theta_{t+1}=\theta_t+\gamma+\epsilon_t-b_t,\qquad
                 0\le\epsilon_t=\log_2(1+r_t/(3x_t))=O(1/K).
\]
For any \(L\)-step interval, \(\sum b_t> L\gamma-1\), so \(2^{\sum b_t}>3^L/2\ge K\). If two starts have the same \((b,r)\) string, iteration and subtraction imply \(2^{\sum b_t}\mid3^L(x-y)\). Thus \(x=y\). An equality of representatives at distinct dates less than \(O(\log K)\) apart is impossible, for then the intervening periodic return would have rational clock \(a/q=\gamma+O(1/K)\) with \(q=O(\log K)\). The irrationality bound gives \(|a/q-\gamma|\gg q^{-6}\) for instance, contradicting the error estimate. The assertion also holds when the fraction has not first been reduced.

Every winding string of length \(L\) on an actual orbit belongs to the **same irrational mechanical language**: its partial sums have the form \(\lfloor\theta+j\gamma\rfloor\), \(1\le j\le L\), for a suitable phase \(0\le\theta<1\). Indeed the cumulative angular error by any such time lies in \([0,C L/K]\). The \(L+1\) endpoints \(-j\gamma\bmod1\), \(0\le j\le L\), are separated by \(\gg L^{-5}\) by the same irrationality bound. Hence at most one endpoint lies within \(2CL/K\) of the initial phase. If none of the ideal floors changes no modification is needed. Otherwise increasing the initial phase by the cumulative error at that single changed endpoint reproduces every actual floor, since no other endpoint can be crossed. The endpoint at zero prevents loss of the initial octave normalization in the changed case. This language has at most \(L+1\) words, one on each interval between the endpoints, with the right-continuous floor convention.

Consequently any consecutive \(2L+1\) dates of an extreme string would contain \(L+2\) successive length-\(L\) starts but at most \(L+1\) winding words. Since the extreme residual is determined by the winding, a duplicate forces the forbidden short return. This proves the first upper bound. On a pre-seam-maximal run, any difference from the total-winding maximum must be a step rounded to the seam with next representative \(K\). Two such steps less than \(4L+2\) apart already force a forbidden short return. Thus any \(4L+2\) consecutive dates have at most one exception; one of the two remaining extreme subruns would have length at least \(2L+1\). This proves the pre-seam assertion. The same reasoning applies to any prescribed deterministic assignment of the residual as a function of the winding letter.

A small correction to the sharp average cannot be deduced from run lengths alone. A sequence can distribute defects at arbitrarily small fixed density while keeping its constant runs short.
