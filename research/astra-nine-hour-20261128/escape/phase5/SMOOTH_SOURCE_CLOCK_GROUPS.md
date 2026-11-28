# Smooth source convergence and growing clock moduli on the actual components

Use the setup of [native Mellin rigidity](NATIVE_MELLIN_RIGIDITY.md). For every \(\Phi\in C_c^\infty((0,\infty))\), fixed \(A>0\), and every real \(\tau\) with the two branch phases prescribed there, one has
\[
 \left|X^{-1}\sum_n n^{-i\tau} f(n)\Phi(n/X)-c(f)\int_0^\infty\Phi(v)\,dv\right|
       \ll_{A,\Phi}(1+|\tau|)(1+\log X)^{-A}.                         \tag{1}
\]
The constants are uniform on the unit ball of exact eigenfunctions. A second conclusion concerns *all* pairs of \(M\)-th root branch phases except the trivial pair. Some absolute \(\delta>0\) has, uniformly for \(2\le M\le(\log X)^\delta\) and all these unit-ball functions,
\[
             \left|X^{-1}\sum_n f(n)\Phi(n/X)\right|
                          \ll_{A,\Phi}(1+\log X)^{-A}.                 \tag{2}
\]
The second formula has no compensating real source character. The published two-logarithm estimate below permits \(\delta=1/11\).

## The Fourier estimate on physical log scale

Continue to write \(a=\log2\), \(L=\log3\), \(b=L-a\). Set \(U(x)=e^{-x}\sum_{n\le e^x} n^{-i\tau}f(n)\) for (1), respectively omit \(n^{-i\tau}\) for (2). For (1) the real size operator is \(P U=[U(x-a)+U(x+b)]/2\). For (2) it is \(P U=[u_0^{-1}U(x-a)+u_1^{-1}U(x+b)]/2\). In both cases \(r=(I-P)U\) is zero on \(x<-b\), bounded on the finite negative interval, and \(r(x)\ll_B C(1+x)^{-B}\) at all positive \(x\), for every \(B\). Here \(C=1+|\tau|\) in (1), \(C=1\) in (2). The latter claim follows by the genuine first step as in (8) of the preceding note: the odd sum is multiplied by \(u_1^{-1}\), and its difference from one third of the full sum is a signed original-trit count plus one cutoff error. The trit bound is uniform in both phases.

Put \(h(s)=-e^{-2s}\Phi'(e^{-s})\). It is smooth compactly supported, \(\int h=\int\Phi\), and
\(U*h(x)=X^{-1}\sum_n n^{-i\tau}f(n)\Phi(n/X)\) at \(X=e^x\) in case (1); omit the twist in case (2). This is checked by integrating \(e^sh(s)\) up to \(x-\log n\). The smooth forcing \(r*h\) is Schwartz with every seminorm \(O_\Phi(C)\), where the implied constant may depend on the seminorm. Derivatives fall on the compact smoothing factor. The Fourier symbol, using \(\widehat H(\xi)=\int H(x)e^{-i\xi x}dx\), is
\[
 D(\xi)=1-\tfrac12(\bar u_0e^{-ia\xi}+\bar u_1e^{ib\xi}),
\]
with both units replaced by one for (1).

There are constants \(K,C_0>0\) such that for \(M\)-th root phases other than the trivial pair,
\[
       |D(\xi)|^{-1}\le C_0 M^K(1+|\xi|)^K\qquad(\xi\in\mathbb R).   \tag{3}
\]
For trivial phases take \(M=1\) and restrict to \(|\xi|\ge1\). To verify this, set \(\eta=\max(|1-\bar u_0e^{-ia\xi}|,|1-\bar u_1e^{ib\xi}|)\); then \(\Re D\ge\eta^2/4\). Clearing the root phases gives integers \(j,k\) within \(O(M\eta)\) of \(Ma\xi/(2\pi),Mb\xi/(2\pi)\), respectively, in prescribed residue classes modulo \(M\). For nontrivial phases these integers cannot both vanish. Hence \(bj-ak=Lj-a(j+k)\ne0\). The fixed-base logarithm estimate gives its absolute value at least \(c(1+|j|+|k|)^{-B}\), while the approximations give an upper bound \(O(M\eta)\). The integer sizes are \(O(M(1+|\xi|))\), proving (3) with \(K=2B+2\), enlarged if desired. For the trivial pair at sufficiently large frequencies the same argument applies; the remaining compact interval away from zero is handled by nonvanishing and continuity. [Matveev, explicit lower bounds for fixed logarithms, Theorem 2.1 and ensuing fixed-base bounds](https://doi.org/10.1070/IM2000v064n06ABEH000314)

A concrete published choice is \(B=4.116201\), by setting the integer constant term to zero in Bondareva–Luchin–Salikhov, Theorem 1. Thus \(K=10.232402\) works, and one may take \(\delta=1/11\). PR212 previously identified this input for a different counting application. [Bondareva, Luchin and Salikhov, Theorem 1, printed p. 18](https://www.mathnet.ru/eng/cheb619) · [PR212, translated cycle-period bounds](https://github.com/GettysburgResearch/collatz/blob/0e4b428211b0bce432efc7d9d19ff4ea552248ec/research/astra-global-20261128/cycles/PERIOD_SPECTRUM.md)

In (1) the symbol has a simple zero at zero, since \(D'(0)=i\kappa\ne0\). Choose a smooth real step \(s_0\), zero at \(x\le-1\) and one at \(x\ge1\). Its residual \((I-P)s_0\) is compactly supported with integral \(\kappa\), by integrating a translated step difference. For \(z=c(f)\int h\), set \(R=r*h-z(I-P)s_0\); it is Schwartz, has integral zero, and its seminorms have the preceding bounds. Thus \(\widehat R/D\) extends smoothly across zero and is Schwartz. At large frequencies use (3), the bounded derivatives of \(D\), and differentiation of its reciprocal. Its inverse transform \(V\) solves \((I-P)V=R\) and is rapidly decreasing, with seminorms \(O_{\Phi}(1+|\tau|)\). The bounded homogeneous difference \(U*h-zs_0-V\) vanishes at minus infinity, so it vanishes everywhere by iterating the negative-drift size walk and using bounded convergence. This proves (1).

For (2) there is no real zero. Set \(R=r*h\) and take \(V\) to be the inverse transform of \(\widehat R/D\). For each integer \(N\ge1\), the \(L^1\) norm of its \(N\)-th Fourier derivative is at most \(C_{N,\Phi}M^{K(N+1)}\): reciprocal derivatives of order \(j\) cost at most \(C_j M^{K(j+1)}(1+|\xi|)^{K(j+1)}\), and the remaining factors are uniformly Schwartz. The homogeneous difference \(U*h-V\) again vanishes by iterating, since the extra walk phases have modulus one. Integration by parts bounds the answer by \(C_{N,\Phi} M^{K(N+1)}(1+x)^{-N}\) for \(x\ge1\). Any fixed \(0<\delta<1/K\) works in (2) on increasing \(N\), even with an additional fixed polynomial in \(M\) on the left.

## The physical and odd clocks modulo a growing integer

Choose any positive reference \(a_C\) in each true ordinary component. For a bounded component take its native cycle period \(\ell_C\) and number of odd departures \(q_C\) in one least lap. Put
\[
 G_{C,M}=(\mathbb Z/M)^2/H_C,\qquad
 H_C=\begin{cases}\langle(\ell_C,q_C)\rangle,& C\text{ bounded},\\
                         0,&C\text{ escaping}.\end{cases}
\]
If \(T^s n=T^j a_C\), let \(D_{C,M}(n)\) be the coset of \((s-j,F_s(n)-F_j(a_C))\). It is independent of the chosen meeting. Indeed align the two meetings at a later clock on the reference trajectory. Any remaining difference is a return to the same state on the other trajectory, hence either zero or an integral number of full laps with the indicated odd counts. The coset decreases by \((1,0)\) on an even departure and by \((1,1)\) on an odd departure.

For any nonnegative smooth compact source weight \(\Phi(n/X)\) with positive integral, sample with its genuine finite normalization. If \(M\le(\log X)^\delta\), then for every \(A>0\), uniformly in the choices of references,
\[
 \left\|\mathcal L(C(n),D_{C(n),M}(n))-
       \sum_C d_C\delta_C\otimes\operatorname{Unif}(G_{C,M})\right\|_{\rm TV}
                 \ll_{A,\Phi}(1+\log X)^{-A}.                          \tag{4}
\]
Here \(d_C\) are the ordinary component densities. They also follow from the preceding argument with no separately imported minimum law: uniform convergence of the ordinary prefix mean at \(\tau=0\) over *all* bounded invariant functions implies that the countably supported finite component laws are Cauchy in \(\ell^1\). Their limit is a probability with these coordinates. The same uniformity in (1) shows that smooth component marginals have the rates stated in (4).

For the joint result take any character \(\chi\) of \((\mathbb Z/M)^2\). For each component where it annihilates \(H_C\) define \(f(n)=c_C\chi(D_{C,M}(n))\), with arbitrary coefficients \(|c_C|\le1\); put zero on the other components. This is an exact eigenfunction of the two branch phases prescribed by the character. If \(\chi\ne1\), the phases are not both one because \((1,0),(1,1)\) generate the group. Taking the supremum in the independent \(c_C\)'s in (2) bounds the sum of the absolute Fourier coefficients across all allowed components. Fourier inversion on each quotient bounds its total discrepancy by the mass discrepancy plus the sum of its nontrivial coefficient magnitudes. Summing the at most \(M^2\) characters is allowed by the rate just proved. The mass normalization is \(\int\Phi+O_\Phi(1/X)\) after dividing by \(X\). This proves (4). The corresponding total variation tends to zero for a fixed sharp proportional interval as well: approximate its indicator from above and below by fixed smooth cutoffs in ordinary mass, then let the approximation error decrease. No such rapid convergence rate for sharp cutoffs is asserted here.

## A square-root support limit on a genuine escape

If one fixed component \(C\) escapes, its two signed comparisons with the reference are honest integers \((s,p)\). The exact corrected-height equation is \(P(n)=P(a_C)2^s3^{-p}\). On a fixed proportional source interval, \(P(n)/n\) stays between two absolute positive constants. Therefore each \(s\) permits only a bounded number of integer grades \(p\), independently of source size. On a set of relative mass \(1-o_B(1)\) in this fixed component, \(|s-\mu\log X|\le B\sqrt{\log X}\), by the fixed-ray signed-clock tightness. It suffices here to fix a waypoint capturing arbitrarily nearly the component and apply the ordinary fixed-target Gaussian. Thus at most \(O_B(\sqrt{\log X})\) residue pairs carry arbitrarily nearly all of the mass. If \(M/(\log X)^{1/4}\to\infty\), their mass under uniform measure on \((\mathbb Z/M)^2\) tends to zero. The relative conditional law in this component then has TV distance tending to **one** from uniform. This last result also holds for the fixed positive smooth source windows above. An estimate proving (4) beyond the one-quarter scale for all components would consequently exclude escape. The proven small \(\delta\) does not reach that scale. [Fixed-ray signed-clock law and its original-source assumptions](../phase2/MOVING_CLOCKS.md)

[ClockQuotient.lean](ClockQuotient.lean) proves independence on a simple reference and independence modulo a periodic reference lap from the orbit and marked-count composition laws, using an explicit least-phase hypothesis on the rooted cycle. [Finite controls](check_native_spectrum.py) compare every observed meeting for six genuine reference orbits and check the signed residual, its integrated boundary flux and the binomial shift identity with integer or rational arithmetic.
