# Odd-height occupation and reciprocal loss at every cycle width

Let \(x_i\) be the distinct odd phases of a primitive ordinary positive cycle, \(p\) its odd period, \(s=\min x_i\), \(2^{a_i}x_{i+1}=3x_i+1\), and \(A=\sum_i a_i\). Set \(\lambda=\log2,\ \gamma=\log_2 3,\ \alpha=\gamma-1,\ \mu_0=5.116201\). The exponents and the ratio \(\max x_i/s\) are unrestricted. All limits below are along any sequence of such cycles with \(p\to\infty\).

For \(2\le R<4\) put \(\eta=\log_2(R/2)\) and \(H_R=\#\{i:x_i>Rs\}\). Then
\[
 \liminf \frac{H_R}{p}
 \ \ge\
 \sup_{0<t<1/3}
 \frac{(\log3)/\mu_0+\alpha\log(1-t)-\eta\log(2-t)}{-\log t}.       \tag{1}
\]
At \(R=2\) the right side is the root \(h=0.066497246\ldots\) of
\[
 (\alpha+h)\log(\alpha+h)-\alpha\log\alpha-h\log h=(\log3)/\mu_0 .
\]
The optimizer \(t=h/(\alpha+h)\) lies below \(1/3\). Rational lower bounds from (1) are \(6.649\%\) above \(2s\), \(2.38\%\) above \(9s/4\), \(1.31\%\) above \(7s/3\), and \(0.60\%\) above \(12s/5\).

Write \(g_i=\lfloor\log_2(x_i/s)\rfloor\) and \(\phi_i=\{\log_2(x_i/s)\}\). An angular version of the count gives
\[
 \liminf \frac1p\sum_i(1-2^{-g_i})2^{-\phi_i}>\frac{263}{10000}.
                                                                    \tag{2}
\]
For the balanced rational cycle of the same odd period and total valuation, let \(s_{\rm bal}\) denote its minimum. Consequently
\[
 \limsup 3\lambda s(A/p-\gamma)\ <\frac1{2\lambda}-\frac{263}{10000},
 \qquad
 \limsup \frac{s}{s_{\rm bal}} <0.96355.                             \tag{3}
\]

The classical linear-form input is Bondareva, Luchin and Salikhov, Theorem 1, page 18. Applying their three-coefficient form with constant term zero gives \(|A\log2-p\log3|>(\max(A,p))^{-4.116201}\) for sufficiently large coefficients. Since \(0<A\log2-p\log3\le p/(3s)\) and \(A\le2p\), this proves \(s\ll p^{\mu_0}\). The integer minimum tends to infinity since each minimum determines at most one cycle. No stronger irrationality-measure hypothesis or Subspace Theorem is used. [Primary theorem](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

The folded height and integer-word method are those of *Odd heights of positive Collatz cycles*, which gives \(6.35\%\) at \(2s\) and the balanced ratio \(0.972186\). Here the exact positive-grade transfer, multi-threshold inequality and direct angular loss improve its asymptotic estimates. The preceding work's explicit bound at every finite period is a different conclusion. Weaver's shortcut-clock occupation result has an eventual positive fraction at higher thresholds with an unspecified constant and counts a different set of departures. [Odd heights, §§2–6](https://rstation.ai/problems/collatz/papers/210/v1) · [Shortcut occupation, Theorem 2](https://rstation.ai/problems/collatz/papers/181/v1)

## Integer words and the finite-window count

On a window let \(E_j=\sum_{i<j}a_i\) and \(J_j=E_j+g_j\). With \(z=\log_2(x_0/s)\),
\[
 J_j=\left\lfloor z+j\gamma+\epsilon_j\right\rfloor,\qquad
 0\le\epsilon_j=\sum_{i<j}\log_2(1+1/(3x_i))
 \le j/(3s\lambda).
\]
Thus \(b_i=J_{i+1}-J_i\in\{1,2\}\) for \(s>1\), and
\[
        0\le g_{i+1}\le g_i+b_i-1,\qquad a_i=g_i+b_i-g_{i+1}.       \tag{4}
\]
The integer calendar \(b\) and grades determine every native exponent.

Use observations in a window of \(n=\lceil\log_3s\rceil+2\) successive dates. If the two retained endpoints are at most \(Rs\), a fixed length-\(L\) valuation word gives \(2^T x_L=3^L x_0+B\), with \(T,B\) fixed. Since \(x_L\) is odd, \(x_0\) is fixed modulo \(2^{T+1}\). Also \(2^T\ge3^L/R\). Thus there are \(O_R(1+s3^{-L})\) possible integer starts. For fixed left and right trims, distinct origins give distinct retained starts by cyclic injectivity. Since \(n=O(\log p)\), windows do not need more than one lap eventually.

At such low starting dates \(z\) is bounded. The uncorrected floors have \(O_R(n)\) patterns. A correction can change a floor only at distance \(O(n/s)\) below a breakpoint. For \(1\le d\le n/2+1\), subtract the unequal integers \(3^d,2^k\) with \(k\) nearest \(d\gamma\). Integration of \(1/u\) between them gives \(\|d\gamma\|>c\,3^{-d}\) for an absolute \(c>0\). In any consecutive group of at most \(\lceil n/2\rceil\) dates, at most one can be close enough. Recording the changed dates costs \(O(n^2)\). Consequently all possible actual calendars cost only a polynomial factor. Refining the initial phase at finitely many additional angular boundaries and their \(O(n)\) rotated copies preserves this conclusion.

For any fixed finite angular partition, ideal phases \(\{z+i\gamma\}\) visit each cell at frequency its length, uniformly in \(z\). The same holds for every fixed stride by the geometric-sum proof of equidistribution. Corrected phases differ on the circle by \(O(n/s)\), so only \(o(n)\) observations can change sides of any fixed boundary. This assertion is uniform for every retained length \(L\le n\), with an \(o(n)\) error, by first taking the discrepancy for long prefixes and treating short prefixes absolutely. When estimating a sum over grade paths, one may fix the ideal cell schedule first. The intervals of initial phases where each date is ambiguous have \(O(n)\) endpoints, hence polynomially many joint patterns. Apply the larger weight or operator norm at an ambiguous site. This costs \(\exp(o(n))\).

## A common eigenfunction for positive grades

Given arrivals \(d_i=b_i-1\), a transition from grade \(g\) can end at any \(0\le k\le g+d_i\) in the enlarged path family (4). Fix \(0<t<1\), \(C=(1-t)^{-1}\). For every integer \(m\ge0\),
\[
    \sum_{k=0}^m t^{\mathbf1_{k>0}} C^k
          =1+t\sum_{k=1}^m C^k=C^m.                               \tag{5}
\]
It follows by backward iteration that the sum over all admissible grade paths, weighted by \(t\) per positive arrival and with terminal weight \(C^{g_L}\), is exactly \(C^{g_0+\sum d_i}\). No cyclic or independence hypothesis appears in this finite identity.

For the threshold \(R\), grade zero is always free. Grade one is free when the next angle belongs to \([0,\eta]\). Replacing its penalty \(t\) by one adds \((1-t)C=1\) to (5) when \(m\ge1\). Since \(C^m\ge C\) there, the increase is by a factor of at most \(2-t\). For \(m=0\) the row is unchanged. On a low-start window \(g_0\le1\). The total arrivals \(\sum d_i=\alpha L+O_R(1+n/s)\) and at most \(\eta L+o(n)\) sites allow the extra free grade. Thus the threshold-weighted count is at most
\[
 O_R(1)\exp(o(n))(1-t)^{-\alpha L}(2-t)^{\eta L}.
\]

If a full \(n\)-date window has at most \(qn\) high observations, trim its initial and final high runs, in total \(k\) dates. The retained endpoints are low, \(L=n-k-1\), and the remaining count of highs is at most \(qn-k\). There are \(k+1\) trim pairs. The preceding count, the polynomial environment cost, and the integer capacity yield at most
\[
 \exp(o(n))\ t^{-qn}(1-t)^{-\alpha n}(2-t)^{\eta n}
   \sum_{k\ge0}(k+1)(3t)^k
\]
possible sparse origins. Here \(q<1\), so a sparse window has a low observation. If this exponential growth rate is strictly below \((\log3)/\mu_0\), the count is \(o(p)\), since \(\log p\ge n(\log3)/\mu_0-O(1)\). Any cycle with high fraction bounded strictly below \(q\) has a positive fraction of such windows by averaging. This proves (1).

## Direct weighted reciprocal cost

For \(g\ge0,\ \phi\in[0,1)\), define \(D(g,\phi)=(1-2^{-g})2^{-\phi}\). We bound the partition sum with weight \(w_k(\phi)=\exp(-6D(k,\phi))\) at each arriving grade. Again conjugate by \(C^g\), now with \(C=5/4\). For a single step with \(d=b-1\) and normalized future bounds \(F(k)\), its weighted row is
\[
  C^{-g}\sum_{k=0}^{g+d}w_k(\phi) C^k F(k).                       \tag{6}
\]
A 32-step block uses 1,024 equal cells for its incoming phase. For each cell and each of its 32 dates the checker bounds the angle and \(d\) outwards using
\[
 0.58496250<\alpha<0.58496251,\qquad
 0\le\epsilon_j\le 10^{-8}
\]
on a fixed block for sufficiently large \(s\). A possible angular seam has upper phase one for the weight bound. The upper \(d\) is one if an octave crossing is possible. Taking the larger allowed \(d\) enlarges (6). Sixty-four equal angular weight bins use alternation through degree nine to bound \(2^{-\phi}\) from below and a positive degree-24 exponential polynomial to bound \(w_k(\phi)\) from above.

For \(0\le g<G=12\) the checker sums (6) directly, rounding every value up on the mesh \(2^{-28}\). Its additional coordinate bounds every \(g\ge G\). For this tail replace \(w_k F(k)\) at \(k\ge G\) by \(w_G F_{\rm tail}\). After summation, (6) is affine in \(C^{-(g-G)}\). Its supremum is bounded by the larger of the value at \(G\) and \(w_GF_{\rm tail}C^{d+1}/(C-1)\). The terminal normalized vector is one, corresponding to physical terminal weight \(C^{g_L}\ge1\). Taking the maximum of the final normalized rows gives the block norm for each entry cell.

The exact arithmetic mean of these 1,024 outward block norms is
\[
 \overline M=\frac{209707481425}{34359738368}.
\]
By submultiplicativity of positive row bounds, uniform equidistribution at stride 32 and concavity of the logarithm, the total weighted count on a low-start \(L\)-edge segment is at most \(\exp(o(n))\overline M^{L/32}\). Partial blocks and ambiguous cell boundaries have the uniform finite bounds just described. Conditioning on the true calendar and ideal bin schedule before summing prevents choices from different input phases from multiplying.

A high grade costs at least \(1/4\). If the total cost on the original window is at most \(qn\), trimming \(k\) high observations reduces that budget by at least \(k/4\). At the retained endpoints the height is in \([s,2s)\). The previous integer capacity costs \(O(3^k)\), and the sum of trim penalties converges since \(3e^{-6/4}<1\). As before there are only \(o(p)\) windows below any budget with
\[
                 6q+\frac{\log\overline M}{32}<\frac{\log3}{\mu_0}.
\]
The exact control verifies the strict inequality at \(q=263/10000\), with positive margin. Taking the limiting budget up to equality and using cyclic averaging proves (2).

Finally the true phases approach uniformity on the circle because their one-step angles are \(\gamma+O(1/s)\) modulo one. Telescoping each nonconstant Fourier character around the lap gives this directly. The exact cycle product and Taylor expansion give
\[
 3\lambda s(A/p-\gamma)
   =p^{-1}\sum_i s/x_i+O(1/s)
   =\frac1{2\lambda}-p^{-1}\sum_iD(g_i,\phi_i)+o(1).
\]
The positive balanced solution at the same two clocks lies in \([s_{\rm bal},2s_{\rm bal})\), by its mechanical prefix sums in the positive rational cycle formula. Its minimum tends to infinity since its clock tends to \(\gamma\). The same angular average with all grades zero therefore gives \(3\lambda s_{\rm bal}(A/p-\gamma)\to1/(2\lambda)\). Division yields (3). The strict reciprocal loss is a full-denominator-one restriction through the integer word capacity. No contradiction for all ordinary cycles follows from the resulting asymptotic interval.

[Finite symbolic kernel](GradePressure.lean) · [Exact numerical certificate and literal paths](check_odd_height_pressure.py) · [Recorded controls](odd_height_pressure_controls.json)
