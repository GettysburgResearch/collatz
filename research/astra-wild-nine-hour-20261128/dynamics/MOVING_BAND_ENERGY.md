# Vanishing energy on a moving band of ordinary component frequencies

**PROPOSED, source-qualified written theorem.** Let \(f:\mathbb N_{>0}\to\mathbb C\), \(|f|\le1\), satisfy \(f(Tn)=f(n)\) for every \(n>M\), where \(M\) is fixed and \(T\) is the ordinary positive shortcut map. Define the log-height profile and its circle Fourier coefficients by
\[
  F_X(z)=f(\lfloor X2^z\rfloor),\quad 0\le z<1,\qquad
  \widehat F_X(\ell)=\int_0^1 F_X(z)e^{-2\pi i\ell z}\,dz .
\]
For \(K\) sufficiently large in terms of \(M\), \(K^{1/2}\le k\le K\), and any fixed \(0<\epsilon<1/2\),
\[
 \boxed{\quad
  \sup_{X\ge2}\sum_{k\le|\ell|\le K}|\widehat F_X(\ell)|^2
     \ll_\epsilon
  \sqrt{\frac{\log(K/k)}{\log K}}+(\log K)^{-1/2+\epsilon}.
 \quad}                                                               \tag{1}
\]
Constants are uniform over all such \(f\). In particular an entire moving band \(K^{1-o(1)}\le|\ell|\le K\) loses its energy. This is a sum of squared coefficients, with no division by the number of frequencies. The [half-density construction](ORDINARY_COLOUR_OBSTRUCTION.md) with a nondecaying single mode at stage boundaries therefore cannot satisfy exact invariance beyond finitely many odd edges.

There is an actual plus-map control for the limit of this theorem. The indicator of ever visiting 5 has only the exceptional departure \(5\to8\). Its total nonconstant spectral energy tends to \(d(1-d)>0\), although (1) holds throughout. Capturing half this energy requires a number of ordinary dyadic frequency bands tending to infinity. Any argument forcing *total* energy to vanish from hypotheses stable under finitely many edge defects would contradict this example.

## The two original-source inputs

At every fixed positive clock \(t\), let \(q_t\) be the number of odd departures. For a mean-zero function \(\psi\) modulo three with \(|\psi|\le1\), the signed incoming law obeys
\[
 {1\over Y}\Big\|\sum_{n\in I}\psi(n)\delta_{(q_t(n),T^tn)}\Big\|_1
 \ll_A (1+\log Y)^{-A}+(1+t)^{-A}                                    \tag{2}
\]
on every integer subinterval \(I\subset[Y,2Y]\). This is the signed native joint estimate of PR215, equation (3); taking the difference of two cumulative laws gives the stated interval form. Its underlying marked physical-fibre estimate is a separate source input. [PR215, fixed head, signed estimate and source pins](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase2/NATIVE_BINOMIAL_TRANSFER.md)

The scalar counted-fusion bound for an integer shift \(h\ge0\), applied at half the native binary horizon, gives on \(W\le n\le2W\)
\[
 W^{-1}\sum_{W\le n\le 2W}|f(n+h)-f(n)|
       \ll \sqrt{\frac{1+\log(2+h)}{\log W}} \qquad(W\gg_M1).          \tag{3}
\]
Indeed take \(t=\lfloor\frac12\log_2 W\rfloor\). The clock-\(t\) Haar bound in the cited proof is \(O((1+\sqrt{\log(2+h)})/\sqrt{t})\). Complete binary periods and one remainder of size \(2^t\) give the same order here. Both positive paths start at least \(W\), hence stay above \(W2^{-t}>M\) through \(t\). A counted fusion therefore gives equal starting values of \(f\), even in the finitely defective case. We only need the estimate averaged over fixed shifts \(0\le h\le H+1\), for which summing (3) loses no factor \(H\) after normalization. [PR146, fixed head, growing additive gaps](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

## Carrying the whole test through the signed-trit estimate

Let \(g\) be a complex differentiable function on the real line with \(\|g\|_\infty\le1\), \(\|g'\|_\infty\le K\), admitting a primitive \(G\) with \(\|G\|_\infty\le1/k\). Absolute constant factors in these three bounds only change absolute constants below. All translates have the same bounds. For any real \(b\), any fixed \(I\subset[Y,2Y]\), and \(Y\ge2K,\ K>M+2\), one has
\[
 Y^{-1}\left|\sum_{n\in I}\psi(n)f(n)g(\log_2 n+b)\right|
             \ll_A (1+\log(Y/K))^{-A}.                                \tag{4}
\]
Take \(t=\lfloor\frac13\log_2(Y/K)\rfloor\), using the trivial estimate for bounded \(t\). Since \(T^i n\ge n2^{-i}\), the exact log-product gives
\[
 0\le \log_2(T^tn/n)-q_t(n)\log_2 3+t
       \le {2^t-1\over3Y\log2}.                                       \tag{5}
\]
All the departures exceed \(M\). In (4) replace the factor after \(\psi\) by
\(f(T^tn)g(\log_2 T^tn+t-q_t(n)\log_2 3+b)\). The normalized error is \(O(K2^t/Y)\). The replacement is a single bounded test of the *actual joint label* in (2). This proves (4), with no Fourier cardinality loss or cost linear in \(K\) outside the physical error. For fixed \(n,Y,t\), (5) follows by summing \(\log_2(1+1/(3T^i n))\) over odd departures and using \(\sum_{i<t} 2^i=2^t-1\).

## A renewal with a moving lower cutoff

Put \(U_g(S)=S^{-1}\sum_{1\le n\le S}f(n)g(\log_2(n/S))\). For \(S\ge2K\),
\[
 U_g(S)=\tfrac12 U_g(S/2)+\tfrac12 U_g(3S/2)+r_g(S),\qquad
             |r_g(S)|\ll_A (1+\log(S/K))^{-A}.                         \tag{6}
\]
An even input \(2y\) gives the first term exactly, apart from a total \(O(M/S)\) from small exceptions. Odd inputs are \(n=(2y-1)/3,\ y\equiv2\bmod3\), with \(y\le(3S+1)/2\). Replacing the cutoff by \(3S/2\) costs \(O(1/S)\). Replace the test argument by \(\log_2(2y/(3S))\) at total normalized cost
\(O((K/S)(1+\log(S/K)))\), summing \(\min(1,CK/y)\). The mean-zero trit \(1_{y\equiv2(3)}-1/3\) can then be removed using (4). Values \(y\le2\sqrt{SK}\) cost \(O(\sqrt{K/S})\); on the remaining dyadic intervals \(\log(y/K)\gg\log(S/K)\), and the relative interval weights have bounded sum. The odd exceptions of \(f\) cost a further \(O(M/S)\), bounded here by \(O(K/S)\). This proves (6).

Set \(J=\log K\) and \(L=\exp(J^\epsilon)\). For \(X\ge KL\), iterate (6) until the positive scale first falls to \(KL\) or below under independent equiprobable multipliers \(1/2,3/2\). It stops almost surely because the log drift is \(\frac12\log(3/4)<0\). Its overshoot lies in \((KL/2,KL]\). The expected number of visits to a fixed unit log interval is bounded by an absolute constant uniformly in its location and in the starting scale. After the first entrance, a revisit \(t\) steps later requires the independent log increment sum to be at least \(-1\). The exponential moment at any sufficiently small positive parameter has base strictly below one; the resulting bounds sum. Telescoping to the stopped date is justified by this bound and boundedness of \(U_g\). Consequently
\[
 |U_g(X)|\le\sup_{KL/2\le S\le KL}|U_g(S)|+O_A((1+\log L)^{1-A}).     \tag{7}
\]
This renewal retains the same test at each scale. A phasewise proof followed by summation of pointwise error bounds would not give (1).

## Terminal averaging on consecutive genuine sources

For \(S\asymp KL\), replacing the sum in \(U_g(S)\) by
\(S^{-1}\int_1^S f(\lfloor y\rfloor)g(\log_2(y/S))\,dy\) costs \(O((1+\log L)/L)\) by the same \(\min(1,CK/y)\) estimate, including rounding of the final cell. Discard \(y<S/\sqrt L\) at cost \(O(L^{-1/2})\). On each remaining octave \(y\asymp W\), set \(H=\lceil(K/k)L^2\rceil\); then \(H/W=o(1)\) uniformly for \(k\ge\sqrt K\). One may also use any subinterval of this octave, with the following errors normalized by \(W\).

Replace the product \(f(\lfloor y\rfloor)g(\log_2(y/S))\) by its average evaluated at \(y+s,\ 0\le s\le H\). Integration changes only endpoint strips, for an error \(O(H/W)\). Inside the average replace \(f(\lfloor y+s\rfloor)\) by \(f(\lfloor y\rfloor)\). For each fixed \(s\), their indices differ by either \(\lfloor s\rfloor\) or \(\lfloor s\rfloor+1\). Applying (3) to both possibilities and integrating their nonnegative discrepancies gives an error
\(O(\sqrt{(1+\log H)/\log W})\), with no independence assumption. At a fixed \(y\), integration by parts gives
\[
 {1\over H}\left|\int_0^H g(\log_2((y+s)/S))\,ds\right|
       \ll {W+H\over H k}.
\]
Indeed the derivative of \(G(\log_2((y+s)/S))\) is the integrand divided by \((y+s)\log2\). Since \(W\le S\ll KL\), this last error is \(O(1/L)\). Sum with weights \(W/S\). Because \(\log W\asymp\log K\), the total is
\[
 O\left(\sqrt{\frac{\log(K/k)}{\log K}}+J^{-1/2+\epsilon}\right).      \tag{8}
\]
Here \(H/W\ll L^{3/2}/k\) on this range, and \(\sqrt{\log L/J}=J^{-1/2+\epsilon/2}\). In (7) choose \(A\) sufficiently large in terms of \(\epsilon\). Formula (8) follows for every \(U_g(X)\) with \(X\ge KL\), and for all translates of \(g\). The same primitive argument works for a single complex exponential on the real line. In particular for every \(\tau\to\infty,\ X/\tau\to\infty\), the normalized discrete average of \(f(n)n^{i\tau}\) tends uniformly to zero: when \(X\ge KL\) take \(k=K\asymp\tau\) (adjusting the constants of the test), and when \(X/\tau\to\infty\) more slowly use the continuous smoothing argument below on fixed proportional subintervals, with sum-to-integral error \(O((\tau/X)(1+\log(X/\tau)))\) on the full prefix. Discarding a fixed small initial proportion and then decreasing it proves the stated prefix conclusion.

## Returning to the circle and taking all frequencies together

For \(X\ge KL\), partial summation on \(X\le S\le2X\) gives the same (8) for
\(\int_0^1F_X(z)g(z)\,dz\). In fact the discrete test at every partial cutoff \(S\) uses \(g\) translated by \(\log_2(S/X)\); the measure \(dz=dy/(y\log2)\) has bounded rescaled variation here. Replacing its integer sum by the continuous profile costs \(O((K+1)/X)\).

For \(K^{1/3}\le X<KL\), apply the terminal continuous averaging proof directly to \(y\in[X,2X]\), now with \(H=\lceil L(1+X/k)\rceil\). The weight \(1/y\) costs \(O(H/X)\) under translation. One has \(H/X\ll L/X+L/k=o(1)\) at polynomial rate, \(X/(kH)\le1/L\), and \(\log H\le O(1)+\log(K/k)+2\log L\). Since \(\log X\ge J/3\), this proves (8) here too. Finally if \(2\le X<K^{1/3}\), integrate \(g\) against the step function \(F_X\) directly. There are \(O(X)\) intervals of constancy, each with integral of \(g\) at most \(2/k\), so \(O(X/k)\ll K^{-1/6}\). These direct estimates are for the continuous log profile and require no statement about aliasing in arbitrary high-frequency integer samples.

To obtain (1), take a smooth nonnegative low-pass multiplier \(\chi\) equal to one on \([-1,1]\), supported on \([-2,2]\), and at most one. Set
\[
 m(\ell)=\chi(\ell/K)\,[1-\chi(2\ell/k)],\qquad
                       g=\overline{m(D)F_X}.
\]
The multiplier equals one on the target band, including its endpoints by continuity. Its convolution kernel on the circle has \(L^1\) norm bounded independently of both cutoffs. Thus \(\|g\|_\infty\ll1\) and \(\|g'\|_\infty\ll K\). It has a primitive of supremum norm \(O(1/k)\): decompose its support \(k/2\le|\ell|\le2K\) into smooth dyadic bands of scales \(A\). On each band the antiderivative multiplier has kernel \(L^1\) norm \(O(1/A)\); summing this geometric series and composing with \(m(D)\) gives the claim. The kernel estimates follow by periodizing the inverse Fourier transforms of fixed smooth compactly supported multipliers, after rescaling; on each annulus division by the frequency is smooth. Applying (8) with a fixed rescaling of this bounded test and using Parseval gives (1). The chosen test may depend on the source profile since every bound is uniform over tests satisfying the displayed norms.

## What the one-edge observable proves about summation

Take \(b(n)=1_{\{\exists t:T^tn=5\}}\). Its unique exceptional edge is \(5\to8\). The predecessors of 5 have natural density \(d>0\), and the predecessors of 85 have positive lower density and all miss 5, so \(d<1\). These statements use the named fixed-target existence and positivity inputs; the finite paths from 5 and 85 can be checked directly. [Lean Assurance Lab, Paper 212 v1, last application](https://rstation.ai/problems/collatz/papers/212/v1) · [Leen's fixed-target density input and Mazur positivity, pinned comparison](https://rstation.ai/problems/collatz/papers/179/v1)

Natural density and partial summation give \(F_X\rightharpoonup d\) against each fixed continuous log-profile test. Since \(F_X^2=F_X\), Parseval gives
\[
  \sum_{\ell\ne0}|\widehat F_X(\ell)|^2\longrightarrow d(1-d)>0,
       \qquad \widehat F_X(\ell)\longrightarrow0\quad(\ell\ne0\ \hbox{fixed}).
\]
For every fixed number \(N\), the combined energy in *any* \(N\) dyadic bands \(2^j\le|\ell|<2^{j+1}\) tends to zero uniformly in their choice. First discard the finitely many low bands by the fixed-frequency limit, then use (1) uniformly on each remaining band. In contrast the total over all bands has a strictly positive limit. This is a statement about a true positive-integer orbit observable with one finite exceptional edge, without any nontrivial positive cycle or escape assumption.

**Open.** An everywhere invariant positive-map colour has no exceptional edge. The signed high-height argument above cannot use this distinction. A full proof by spectral energy must use the exact finite-height boundary data or another input which fails for the visit-to-five observable. It must also handle energy distributed over arbitrarily many separated frequency bands.

## Branch twists and simultaneous component grades

The same bound (1) holds, with the same constants, for every pair of unit complex numbers \(v_0,v_1\) and every \(f\) satisfying \(f(Tn)=v_{n\bmod2}f(n)\) at \(n>M\). In (4) the reconstructed terminal test receives the factor \(v_0^{-(t-q_t)}v_1^{-q_t}\), a unit determined by the joint label. In (3) symbolic absorption for two translates started at level zero gives equal counts as well as equal endpoints; this follows from the equal affine slopes in PR146's absorbing state. Thus the starting values still agree there. In (6) the two coefficients acquire the factors \(v_0^{-1},v_1^{-1}\) respectively. Stopping multiplies the boundary terms and residuals by products of units with modulus one. Equations (7)–(8) and the multiplier proof carry over. The twists may depend on \(X,k,K\) because all bounds are uniform.

On every component with an escaping orbit choose a reference vertex \(r\). For an ordinary vertex \(n\) of this component let \(a_C(n)\in\mathbb Z^2\) be the two branch counts from the reference to a common endpoint, minus the corresponding counts from \(n\) to that endpoint. If a later common endpoint is chosen, the two added tails cancel. Every common endpoint lies on the unique nonrepeating future of the reference and so these choices are consistent. One has \(a_C(Tn)=a_C(n)+e_{n\bmod2}\). For each such component and \(b\in\mathbb Z^2\) write \(E_{C,b}=1_{\{n\in C:a_C(n)=b\}}\). Then (1) gives the stronger simultaneous bound
\[
 \sum_{C,b}\ \sum_{k\le|\ell|\le K}
 \left|\widehat{(E_{C,b})_X}(\ell)\right|^2
 \ll_\epsilon \sqrt{\log(K/k)/\log K}+(\log K)^{-1/2+\epsilon}.
\]
Indeed apply the twisted estimate to \(f(n)=\eta_C e^{2\pi i\langle\theta,a_C(n)\rangle}\) on escaping components and zero elsewhere. Average over independent uniform unit circle labels \(\eta_C\) and \(\theta\) uniform on the two-torus. Orthogonality deletes all cross terms between distinct component/grade pairs; each finite source shell involves only finitely many of them. The untwisted variant sums over every ordinary component, cyclic ones included, using just random labels \(\eta_C\). This concerns genuine spatial energy in the original shell, distinct from a scalar limit of an eigenfunction.

## Relation to the scalar theorem and the half-density example

PR215 phase 6 already proves uniform high-frequency cancellation for the limiting scalar Mellin amplitude with resonant branch twists. It also proves a stronger relative trit estimate on translated short intervals, stops the fair size walk at frequency times a subexponential buffer, and uses genuine terminal block fusion. The new estimate transports a general smooth test through the true endpoint and count, uses pairwise counted fusion in a continuous sliding average, and bounds the *sum* of spatial Fourier energies uniformly in the original shell. The spectral spread of the finitely defective visit-to-five observable uses this simultaneous estimate. Neither energy statement follows by summing the scalar error over all frequencies. [PR215 phase 6, fixed head](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase6/LOCAL_TRIT_AND_RAJCHMAN.md)

For the earlier half-density colour, take real \(X_j\) with \(L(X_j)=j^2\). Its frozen profile is exactly \(B(k_j\log_2 n)\). On the log shell the freezing estimate there changes the profile in \(L^1\) by \(O(R_{X_j})\), since a single exceptional integer occupies length \(O(1/X_j)\). Replacing \(\log_2\lfloor X_j2^z\rfloor\) by \(\log_2 X_j+z\) crosses a step of the square wave on a set of measure \(O(k_j/X_j)\). Consequently its Fourier coefficient at \(k_j\) has magnitude tending to \(1/\pi\), the first Fourier magnitude of \(1_{[0,1/2)}\). Thus even the single-frequency conclusion of (1) detects those infinitely repeated defects.
