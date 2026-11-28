# A nontrivial ordinary cut accumulates variation in each sufficiently long dyadic range

For a binary invariant coloring \(c(Tn)=c(n)\), put \(d=\operatorname{dens}\{c=1\}\) and
\[
 d_j=2^{-j}\#\{2^j\le n<2^{j+1}:c(2n+1)\ne c(2n)\}.
\]
Weaver's Paper 212 already proves \(\sum_j d_j=\infty\) when both colors occur and proves distinguishability of arbitrary distinct finite affine branches. Its summability argument even applies under eventual invariance before assuming existence of density. We locate a definite amount of this variation between a prescribed sufficiently large \(j\) and \(\lceil2^{12j}\rceil\):
\[
               \sum_{j\le i<\lceil2^{12j}\rceil}d_i
                         \ \ge\ 4d(1-d)-o(1).                         \tag{1}
\]
The error tends to zero uniformly over all the colorings. This grows only very slowly when iterated across disjoint ranges. Neither the earlier divergence nor (1) implies a contradiction with the actual \(O(j^{-1/2})\) upper bound from counted fusion. [Weaver, rStation Paper 212, “Density from dyadic siblings” and branch separation](https://rstation.ai/problems/collatz/papers/212)

## A sharp prefix estimate

With the notation of the [smooth source proof](../phase5/SMOOTH_SOURCE_CLOCK_GROUPS.md), take \(u_0=u_1=1\) and write \(U(x)=e^{-x}\sum_{n\le e^x}c(n)\). The integrated forcing is \(\kappa d\). Let \(s_0\) be the smooth step there and put \(R=r-d(I-P)s_0\). Its Fourier transform and all derivatives are bounded uniformly in the coloring, from the finite negative support and rapid decay of \(r\) at positive \(x\). At zero \(\widehat R(0)=0\), canceling the simple zero of \(D=1-\tfrac12(e^{-ia\xi}+e^{ib\xi})\). Choose a fixed smooth probability mollifier supported in \([-1,1]\), and dilate it to the log width \(0<\eta\le1\). In the Fourier proof, derivatives of its multiplier \(\widehat m(\eta\xi)\) are bounded by \(C_{N,B}(1+\eta|\xi|)^{-B}\) through each fixed order \(N\).

The reciprocal estimate at \(|\xi|\ge1\) uses \(K=10.232402\) from the published fixed-logarithm bound. Each derivative of \(1/D\) up to order \(N\) is bounded by \(C_N(1+|\xi|)^{K(N+1)}\). The order-\(N\) derivative of \(\widehat R\widehat m(\eta\xi)/D\) thus has integral norm \(O_N(\eta^{-K(N+1)-1})\), after taking \(B>K(N+1)+2\); on a fixed neighborhood of zero use smooth cancellation. Fourier inversion and the uniqueness of the bounded solution vanishing at minus infinity, as in the smooth proof, give
\[
       |U*m_\eta(x)-d|\ll_N x^{-N}\eta^{-K(N+1)-1}\quad(x\ge3).
\]
Counting the grid points between two cutoffs gives \(|U(x+h)-U(x)|\ll |h|+e^{-x}\) for \(|h|\le1,x\ge3\). Set \(\eta=x^{-1/11}\) and take fixed \(N\) sufficiently large. Consequently
\[
       \sup_c|U(x)-d|\ll (1+x)^{-1/11}.                                \tag{2}
\]
The same proof works for any exponent less than \(1/K\). This sharp prefix rate follows here from the signed-trit source input and the Fourier small-denominator bound.

## The two mantissa profiles

On \([1,2)\) put \(F_j(v)=c(\lfloor 2^j v\rfloor)\). Exact doubling gives \(\|F_{i+1}-F_i\|_1=d_i/2\). The elementary finite count identity is formalized in [DyadicMidpoint.lean](DyadicMidpoint.lean). Choose \(k=\lceil2^{12j}\rceil\). By (2), the integral of \(F_k-d\) on any subinterval of \([1,2)\) is \(O(k^{-1/11}+2^{-k})\), uniformly in its endpoints and in the coloring. The function \(F_j\) is constant on \(2^j\) such intervals, so
\[
             \int F_k F_j=d\int F_j+O(2^jk^{-1/11})=d^2+o(1).
\]
Both integrals of the individual profiles equal \(d+o(1)\) by (2). The profiles are binary, and therefore \(\|F_k-F_j\|_1=2d(1-d)+o(1)\). The triangle inequality through the intermediate levels proves (1).

Every nonconstant true coloring has \(0<d<1\) under the named positive lower predecessor-density input. In the special case of any one cut, qualitative divergence also follows directly from the native density and the exact midpoint identity: finite total variation would give a binary strong limit, whereas the ordinary density forces the weak limit to be the constant \(d\) on each proportional subinterval. The underlying summability criterion has the priority stated above.
