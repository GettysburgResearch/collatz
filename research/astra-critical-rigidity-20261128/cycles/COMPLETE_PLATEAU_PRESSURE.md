# Complete rotation plateaus of the integer tripling ceiling

**PROPOSED.** Let `N` be an odd positive integer. On all dyadic lifts of odd integers at most `N`, let \(H_N(v)\) be the least grid point at least \(3v\). Write \(\rho_N=A/p\) for its reduced lift rotation, in octaves per step, and \(\gamma=\log_2 3\). Each periodic component at the cutoff has period \(p\). All logarithms below other than \(\log_2\) are natural.

For any consecutive plateau of odd cutoffs \([L,U]\) with \(L\to\infty\), including plateaus on which all components are replaced,
\[
           \limsup U/L\ \le\
           \frac{122508662755342816370953}{3227093020657183629047}<38.       \tag{1}
\]
More strongly, a plateau of relative length \(U/L\to\kappa>1\) forces a strict exponent loss in its reduced clock denominator. Define \(a=2-\gamma\),
\[
 b(f)=1+\mathbf1_{f\ge a},\qquad w(f)=2\log 2\,2^{-f},\qquad
 \Phi(t)=\int_0^1\log\left(\sum_{j=0}^{2^{b(f)}-1}e^{t w(f) j}\right)df.
\]
Then
\[
 \limsup\frac{\log p}{\log L}\le
 \frac1{\log3}\inf_{t\le0}\left(\Phi(t)-\frac{2t}{1+\kappa}\right)<1.    \tag{2}
\]
In particular every sequence with \(p=L^{1-o(1)}\) has \(U/L\to1\). The full-plateau conclusion uses the two endpoint components only. They may have no vertex in common. It gives no constant shorter than the previously proven factor two for an *individual unchanged* component.

## The angular cost of a prescribed clock

For a periodic component, normalize every lift to \(N/2<Z\le N\). These representatives are integers. At time \(i\),
\[
  2^{b_i} Z_{i+1}=3 Z_i+d_i,\qquad
  0\le d_i<2^{b_i},\qquad b_i\in\{1,2\}.
\]
Indeed each new octave consists of the multiples of its unit spacing. The first output at or above the seam belongs to that octave. The increasing lift restricts to a strictly ordered permutation on the component, so on the infinite rank list it adds \(A\) at every step. To see the shift, sum its octave windings around the orbit, which telescope the changes of base rank. If the starting rank is \(r\in\{0,\ldots,p-1\}\), the total winding after \(k\) steps is \(\lfloor r/p+k\rho_N\rfloor\). The single winding is therefore one or two with boundary at \(2-\rho_N\). The same increasing-lift argument gives one rotation across all components by interleaving any two lifted orbits. Adding eligible rays makes the rotation nonincreasing.

The lap identity and \(Z>N/2\) give
\[
  0<\rho_N-\gamma=\frac1p\sum_i\log_2(1+d_i/(3Z_i))\ll 1/N.
\]
Zero is impossible by unique factorization. In particular the reduced periods tend to infinity. The angles \(\log_2(2Z/N)\bmod1\) advance by \(\gamma+O(1/N)\). Every weak limiting empirical law is invariant under the irrational rotation by \(\gamma\). Its nonconstant Fourier coefficients vanish, proving Haar convergence, uniformly over cuts of the circle by approximation with a fixed mesh. In increasing order, this gives \(2Z_r/N=2^{r/p}+o(1)\) uniformly. If \(Z=N\), its displayed real coordinate is 1 and its circle coordinate is 0; this endpoint changes the unwrapped empirical distribution by at most \(1/p\).

Put \(c_N=3(\log2)^2 N(\rho_N-\gamma)\). Taylor expansion with uniform second-order error gives
\[
                      c_N=\frac1p\sum_{r=0}^{p-1}w(r/p)d_r+o(1).          \tag{3}
\]
The integer digits on the right are the actual rounding errors, indexed by spatial rank. No uniform law of these digits is posited.

## Entropy with angle retained

Take a uniform initial rank and observe \(k=\lceil\log_3(2N)\rceil+1\) steps. The word of pairs \((b_i,d_i)\) identifies its initial label: two starts with the same word have difference divisible by \(2^{\sum b_i}\), by subtracting the iterated affine laws and using coprimality with \(3^k\). The modulus exceeds \(N\) by \(\sum b_i>k\gamma-1\). Thus the entropy of the word is exactly \(\log p\).

Fix an angular partition with \(m\) equal bins, augmented by the single true boundary \(2-\rho_N\). The date-wise bin labels determine every \(b_i\). At time \(i\) the rank fraction is the original rank fraction plus \(i\rho_N\bmod1\), so there are at most \((m+1)k+1\) words of bin labels. Conditional entropy subadditivity and stationarity now give, with \(C\) the current bin and \(d\) the current digit,
\[
       \log p\le\log((m+1)k+1)+ k H(d\mid C).
\]
At a given bin choose any representative \(f_C\), and let \(b_C\) be its constant calendar value. Nonnegativity of relative entropy with respect to the finite distribution proportional to \(e^{t w(f_C)j}\) gives, for any fixed real \(t\),
\[
 H(d\mid C)\le
 \mathbb E\left[\log\sum_{j=0}^{2^{b_C}-1}e^{t w(f_C)j}-t w(f_C)d\right].
\]
The weights can be replaced by \(w(r/p)\) at cost \(O_t(1/m)\), since every digit is at most three. The ranks form the exact uniform \(p\)-grid, and the moving calendar boundary converges to \(a\). Pass first to \(N\to\infty\), then \(m\to\infty\). On every subsequence with \((\log p/\log N,c_N)\to(\sigma,c)\) this proves
\[
                \sigma\log3\ \le\ \Phi(t)-tc\quad(t\in\mathbb R).          \tag{4}
\]
Taking subsequences is harmless since both coordinates stay bounded. This is a necessary bound at every cutoff and uses one full component at a time.

The identities \(\Phi(0)=\log3\), \(\Phi'(0)=1\) and \(\Phi(t)=2t+\Phi(-t)\) follow by reflecting the digit \(j\mapsto2^{b(f)}-1-j\). The two intervals \([0,a]\) and \([a,1]\) have equal \(w(f)df\)-mass \(1/2\), as \(2^{-a}=3/4\). In particular the allowable interval in (4) is symmetric about one. On a plateau the endpoints satisfy \(c_U=(U/L)c_L\) exactly. If \(U/L\to\kappa<\infty\), their limiting log-period exponents agree. Either \(c_L\le2/(1+\kappa)\) in the limit, or \(2-c_U\le2/(1+\kappa)\). Apply (4) at the corresponding endpoint, reflect in the latter case, and take \(t\le0\). This proves (2). Strictness follows by taking a small negative \(t\), since \(\Phi'(0)=1>2/(1+\kappa)\).

## A uniform finite ratio independent of replacements

Theorem 1 of Bondareva, Luchin and Salikhov gives, at \((h_1,h_2,h)=(A,-p,0)\), the lower bound \(|A\log2-p\log3|\gg p^{-4.116201}\). Since \(A\asymp p\) and \(\rho_N-\gamma\ll1/N\), (4) applies with every limiting \(\sigma\ge1/5.116201\). [BLS, Theorem 1, printed p. 18](https://www.mathnet.ru/php/getFT.phtml?jrnid=cheb&option_lang=eng&paperid=619&what=fullt)

Put \(t=-3\). The substitution \(v=2^{1-f}\) gives
\[
 \Phi(-3)=\frac1{\log2}\left[
  \int_1^{3/2}\frac{\log(1+2^{-3v}+2^{-6v}+2^{-9v})}{v}\,dv+
  \int_{3/2}^2\frac{\log(1+2^{-3v})}{v}\,dv\right].
\]
Both integrands are decreasing on their pieces. A directed rational upper sum with mesh \(1/8192\) gives \(\Phi(-3)\le248780987952353/4096000000000000\). The finite certificate uses the positive power series for \(2\operatorname{atanh}((x-1)/(x+1))=\log x\) at \(x=2,3\), then \(e^{-u}\le1-u+u^2/2\) for the mesh multiplier and \(\log(1+s)\le s-s^2/2+s^3/3\) for each integrand. All intermediate upper approximations round upwards. Thus (4) and reflection put every limit of \(c_N\) in \([c_*,2-c_*]\), where
\[
 c_* = 3227093020657183629047/62867877888000000000000>2/39 .
\]
This gives (1) directly from the exact endpoint ratio, including subsequences not initially known to have bounded ratio. The analytic theorem supplies the large-clock threshold, which is not evaluated here. [Directed certificate and native calendar replay](check_complete_plateaus.py)

## Physical scope and source handoff

A positive ordinary Collatz cycle with least and greatest odd states \(s,X\), total valuation \(A_0\) and odd period \(p_0\) induces this same rotation \(A_0/p_0\) at every odd cutoff \((X+1)/2\le N\le4s-1\), by the explicit upper bundle of PR213. Thus for a sequence with \(X/s\to R<8\), (2) applies at \(\kappa=8/R\) to the **reduced denominator** of \(A_0/p_0\). The unconditional ratio 38 by itself yields no improvement on the previously proved lower width three. The new restriction concerns the complete rotation plateau even when the comparison components differ. An upper ratio tending to one, or a bound below \(8/R\) at a surviving ordinary width, is open.

Frozen predecessor: PR213, `5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128`, `research/astra-diagonal-frontier-20261127/arithmetic/`. `HOMOGENEOUS_MEETINGS.md` provides the lift, the angular weighted drift bound and a finite-window entropy deficit at one cutoff under its stated irrationality assumption. `PERIODIC_GRID_DENSITY.md` proves vanishing density of periodic vertices at each cutoff. `PLATEAU_COMPONENTS.md` bounds the lifetime ratio of an unchanged component by two asymptotically and exhibits same-clock replacements. `UPPER_BUNDLE.md` is the ordinary-cycle transfer, including its component-replacement endpoint qualifications. The new step here keeps the full angle-conditioned rounding alphabet in the entropy bound and applies its two-sided pressure constraint at both ends of a complete plateau. No conclusion about full rational Collatz denominators follows from a homogeneous-ceiling clock alone.
