# An unbounded rational family at the lower angular clock threshold

The elementary angular lower bound is sharp on positive native rational cycles even under the binary exponents and physical ceiling. Write \(\gamma=\log_2 3\), \(\lambda=\log2\), and take the upper continued-fraction convergents \(A/p>\gamma\) with \(p\to\infty\). For each sufficiently large such convergent the construction below gives a genuine positive odd rational cycle of primitive odd period \(p\), complete reduced denominator \(q\), minimum \(s\), and maximum \(X\), satisfying
\[
 X<16s/3,\qquad X/s\longrightarrow16/3,\qquad
 24\lambda^2s(A/p-\gamma)\longrightarrow3/2,\qquad
 qX\ \ge\ \tfrac12 3^{\lfloor(p-8)/2\rfloor}.
\]
Any classical finite irrationality measure for the fixed logarithmic ratio gives \(X\le p^{O(1)}\), so the **complete reduced denominator** grows at least exponentially. The exponent-three assumption in the separate ordinary weighted-clock corollary is unnecessary here. The family is adversarial to a denominator-free version of that conclusion. [Elementary angular clock inequality](ROTATION_CUTS.md) · [Ordinary weighted result and its dependencies](WEIGHTED_CLOCK.md)

## One edited cluster in a mechanical word

Set \(r_i=\{iA/p\}\), \(b_i=\lfloor(i+1)A/p\rfloor-\lfloor iA/p\rfloor\), initially \(j_i=b_i-1\). Replace the six sites \(i=-3,-2,-1,0,1,2\) of the periodic tag sequence by \((1,2,2,2,2,1)\). Define \(e_i=b_i+j_{i+1}-j_i\). Outside the seven-edge cluster \(-4\le i\le2\) these are exactly \(b_{i+1}\). At those seven edges the unedited \(b_{i+1}\) are \((1,2,2,1,2,1,2)\) and the resulting \(e_i\) are \((2,2,2,2,1,1,1)\). These floors are stable for slopes sufficiently close to \(\gamma\). Thus all exponents are one or two, four edges change, and the sum remains \(A\).

The native word has \(D=2^A-3^p>0\) and \(K=\sum_{i<p}3^{p-1-i}2^{\sum_{k<i}e_k}\). Its first phase is \(K/D\) and its denominator is \(q=D/\gcd(D,K)\). Every rotation gives the same positive native orbit. All rotated carries and \(D\) are odd, so the odd quotients are literal. The denominator is unchanged on every edge since it is coprime to six. A shorter period of the phases would give a shorter period of the native word, impossible since \(A/p\) is reduced.

## The real profile, including the strict physical ceiling

Write \(\sigma=2^{A/p}\), \(a=3/\sigma<1\), \(c_i=2^{j_i}\), \(Y_i=c_i x_i\), \(W_i=Y_i2^{-r_i}\). Then
\[
          W_{i+1}=aW_i+d_i,\qquad d_i=c_i2^{-r_i}/\sigma .
\]
The mean satisfies \(\bar W=\bar d/(1-a)\asymp(A/p-\gamma)^{-1}\gg p^2\), since \(d_i\) is uniformly bounded above and below and convergents have error below \(1/p^2\).

Uniformly on every cyclic prefix of length at most \(p\),
\[
        \left|\sum_{h<k}(d_{i+h}-\bar d)\right|=o(p).
\]
The unedited summand is a bounded piecewise continuous function of the rotation \(r_i\), with one moving threshold \(2-A/p\) tending to \(2-\gamma\); the six edits cost \(O(1)\). For fixed nonzero Fourier index \(m\), every consecutive exponential sum is bounded by \(2/|1-e^{2\pi i m A/p}|=O_m(1)\) for large \(p\). Continuous approximation above and below the fixed limiting function, including an arbitrarily small interval covering the moving jump, gives the displayed \(o(p)\) bound uniformly in the start and prefix length. The average over all phases obeys the same approximation. This also applies to reversed cyclic sums.

The periodic solution has
\[
       W_i-\bar W
       ={\sum_{k=1}^p a^{k-1}(d_{i-k}-\bar d)\over1-a^p}.
\]
Abel summation and the zero total centered sum bound the numerator by \((1-a^{p-1})o(p)\). Therefore \(Y_i=\bar W2^{r_i}+o(p)\) uniformly. Only four tags are two, at chronological sites \(-2,-1,0,1\). Their phases away from zero have positive limiting separation from zero, and all lower tags give \(x_i\ge (\bar W-o(p))/2\). Thus the minimum is the actual phase \(s=x_0=\bar W/4+o(p)\).

A site with \(j_i=0\) has \(b_i=1\), hence \(r_i\le2-A/p-1/p\) because the ranks are on the \(1/p\) grid. Its height is at most \(\bar W(4/3-\Omega(1/p))+o(p)\), strictly below \(16s/3\) since \(\bar W\gg p^2\). Sites with \(j_i\ge1\) have height at most \(\bar W+o(p)\). Conversely there are unedited zero tags approaching \(r=2-\gamma\) from below, by the uniform rank mesh and only six edits. This gives \(X/s\to16/3\).

Finally the mean of \(c_i2^{-r_i}\) tends to
\[
  \int_0^{2-\gamma}2^{-t}\,dt+
     2\int_{2-\gamma}^1 2^{-t}\,dt = \frac{3}{4\lambda}.
\]
The native product and the displayed uniform profile give \(24\lambda^2s(A/p-\gamma)=2\lambda\,p^{-1}\sum_i c_i2^{-r_i}+o(1)\to3/2\). Equivalently this follows from \(s\sim\bar d/[4(1-a)]\) and \(1-a\sim\lambda(A/p-\gamma)\).

## Two matching native futures force the complete denominator

Take \(k=\lfloor(p-8)/2\rfloor\). At most \(k+6\) starts have a length-\(k\) window touching the seven-edge altered cluster. The remaining starts read the unedited shift of the mechanical word. There are at most \(k+1\) possible length-\(k\) words, by cutting the starting angle at the \(k+1\) breakpoints \(\{-jA/p\}\), \(0\le j\le k\). The floor convention assigns a breakpoint to the interval on its right. As \(p-k-6>k+1\), two distinct clean starts have the same literal future of native clock \(B\ge kA/p-1>k\gamma-1\). Subtract their actual affine equations. Since \(3\) is a dyadic unit, the difference of their distinct integer numerators over \(q\) is divisible by \(2^B\). It has absolute value at most \(qX\), proving the displayed bound. Any finite classical two-logarithm estimate gives \((A/p-\gamma)^{-1}\le p^{O(1)}\); the profile therefore gives the asserted exponential denominator. The two-sided packing source uses the same native future divisibility for genuine rational cycles; here the repeated windows are forced by a single localized edit cluster. [Matched native windows at the complete denominator, PR191](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md)

The exact control constructs the genuine cycles at periods 41, 306 and 15,601, checks every literal valuation, computes the complete reduced denominator, and exhibits the repeated windows and their integer numerator spacing. The final control has denominator bit length 24,709, ratio below \(16/3\), and clock observable strictly between 1.500805 and 1.500806. [Exact replay](check_sparse_rational_clock.py) · [Integer output](sparse_rational_clock_controls.json)
