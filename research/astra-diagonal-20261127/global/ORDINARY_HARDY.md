# The integer Hardy equation and its differentiated boundary

**PROPOSED.** Let \(U\) be the accelerated odd map on positive odd integers. On one escaping component \(C\) of the positive shortcut map \(T\), put
\[
 F(x)=\prod_{w\text{ odd on the forward path from }x}\frac{3w}{3w+1},
 \qquad P(x)=x/F(x),\qquad m_x=P(x)^{-2}.
\]
Extend \(m\) by zero off \(C\), and set \(b(x)=x^2m_x=F(x)^2\) on \(C\), zero elsewhere. The ordinary simple-path reciprocal bound gives \(c\le F(x)<1\) on \(C\) with absolute \(c>0\), and the contribution of vertices above \(M\) to the reciprocal sum tends uniformly to zero. In particular \(m\) is summable. Direct transport gives
\[
  P(2x)=2P(x),\qquad P(3x+1)=3P(x)\quad(x\ {\rm odd})
\]
on supported vertices. [Simple-path estimate](../../astra-unconventional-20261126/boundary/TILTED_TRACE.md).

## The exact coefficient kernel

Write \(M(z)=\sum_{x\ {\rm odd}}m_xz^x\), and let \(M_r\) retain exponents congruent to \(r\pmod 3\). Among complex power series supported on positive odd exponents, the single equation
\[
 16zM(z^3)-z^4M(z^{12})=36M_2(z^2)+9M_1(z^4)                         \tag{1}
\]
is equivalent, coefficient by coefficient, to \(4^e m_x=9m_{U x}\) at every positive odd \(x\), where \(e=v_2(3x+1)\).

All displayed exponents are \(1\bmod3\) and even. At degree \(3x+1\) the first right-hand term applies exactly for \(e=1\), giving \(4m_x=9m_{Ux}\). The second applies exactly for \(e=2\), giving \(16m_x=9m_{Ux}\). For \(e\ge3\) the remaining row reads \(16m_x=m_{(x-1)/4}\). Here \((x-1)/4\) is odd, has the same odd successor and division exponent \(e-2\). Iteration proves the assertion, including its converse. Scaling one supported mass to one makes all masses in that component rational. The [Lean kernel](OrdinaryHardy.lean) proves both directions for the three rational coefficient rows, including the existence of the true odd factor and the strict increase of \(x^2m_x\) on a positive odd edge.

On a periodic component each complete odd lap has gain \(\prod 3x/(3x+1)<1\); thus (1) forces zero on its cycle and then on the whole component. On an escaping component, \(m_xP(x)^2\) is constant along every edge and hence on the full class. Conversely all these component vectors solve (1). Their supports are disjoint and each has summable coefficients. Normalizing each nonzero component vector to have coefficient norm one therefore identifies the kernel in the Wiener algebra isometrically with \(\ell^1\) of the actual escaping components. Its nonnegative extreme rays are their individual masses. This extends the forward calculation in [Critical conformal atoms](../../astra-six-hour-20261127/global/CONFORMAL_ATOMS.md).

## A strong natural boundary on every arc

For the full positive-integer series \(M^+(z)=\sum_{x\ge1}m_x z^x\), the series \((z\,d/dz)^2M^+(z)=\sum b(x)z^x\) has a strong natural boundary on the unit circle. Explicitly, its radial \(L^1\) norms on every nonempty open arc are unbounded. The same holds for the odd series \(M\) after applying the same differential operator. In particular neither the full nor the odd series can continue analytically across a single arc. The masses themselves have absolutely summable coefficients and extend continuously to the circle.

For this conclusion it suffices that for every fixed \(L\) there is a dyadic cylinder on which all starts \(n,\ldots,n+L\) have merged by a common shortcut time. The cited counted-synchronization theorem gives such a cylinder. This use requires neither a fixed-target density bound nor an assumed ordinary basin density. Indeed the basin of one meets every dyadic cylinder, at arbitrarily large sites. A specified length-\(k\) shortcut word of odd weight \(u\) maps its positive source progression into the endpoint progression \(y_0+3^u j\). For \(u>0\), \(y_0\) is a ternary unit. Powers of two hit this progression arbitrarily far out, since 2 is a primitive root modulo every \(3^u\), by \(v_3(4^{3^h}-1)=h+1\). For \(u=0\) the endpoint progression has step one. A dyadic cylinder is a parity cylinder by the parity-word bijection. Choosing a point of the one-basin in the merging cylinder produces a whole interval of \(L+1\) successive zeros of \(b\).

The component has arbitrarily large supported indices (also arbitrarily large odd indices). After such a zero interval choose the first supported index \(n_L\). Its preceding \(L\) coefficients are zero and \(b(n_L)\ge c^2\). The argument works for the odd-supported series by setting all its even coefficients to zero. Breuer and Simon's Theorem 1.6 now applies to these bounded coefficients. It gives the claimed divergence on every arc. Their result concerns the second differentiated series here. Bell and Lagarias proved classical natural boundaries for unweighted generating functions of the inverse orbit of a fixed target, including all \(m\ne1,2,4,8\). [Breuer–Simon, Theorem 1.6](https://arxiv.org/abs/1002.0823) · [Bell–Lagarias, Theorem 1.2](https://doi.org/10.4064/aa170-2-1) · [Weaver, counted synchronization, eq. (18)](https://rstation.ai/problems/collatz/papers/124/v1).

## The fixed-frequency mean-square test sees only a point mass

For the full integer sequence \(b\), counted synchronization of \(n,n+h\) for any fixed integer \(h\) gives
\[
     \frac1X\sum_{n\le X}|b(n+h)-b(n)|^2\longrightarrow0.              \tag{2}
\]
On a successful pair the components coincide. On \(C\) their common time and odd count give exactly the same corrected height, so the two normalized values differ by \(O_h(1/n)\). Boundedness treats the density-zero exceptional pairs. Initial indices below one may be omitted.

Take any subsequence along which the first two moments tend to \(\beta,\sigma_2\). By (2), every fixed-lag autocorrelation tends to \(\sigma_2\). Equivalently the nonnegative measures \(\big|\sum_{n\le X} b(n)e(nt)\big|^2\,dt/X\) on \(\mathbb R/\mathbb Z\) converge weakly along this subsequence to \(\sigma_2\delta_0\), where \(e(t)=\exp(2\pi it)\). This follows by computing every Fourier coefficient. It gives no uniform \(L^1\) estimate on any complementary open arc.

With the fixed-target positive lower predecessor densities at 1 and at a unit of \(C\), the variance \(\sigma_2-\beta^2\) is uniformly positive over all such subsequences. Indeed the empirical variance is the mean of squared pairwise differences divided by two, and a uniformly positive fraction of ordered pairs has one value zero and the other at least \(c^2\). In fact if a bounded sequence \(v(n)\) has a uniform interval mean \(m\), meaning \(\sup_N|H^{-1}\sum_{h<H}v(N+h)-m|\to0\), then (2) gives
\[
 X^{-1}\sum_{n\le X} b(n)\overline{v(n)}\ \longrightarrow\ \beta\bar m
\]
along the same subsequence. Average the translated sum over \(0\le h<H\) with \(H\) fixed, use (2) by Cauchy–Schwarz, and then take \(H\to\infty\). Therefore the liminf of the mean-square approximation error by any such \(v\) is at least the uniform variance lower bound: expand \(|b-v|^2\), use the correlation identity, and bound the second moment of \(v\) below by \(|m|^2\). This applies in particular to each fixed continuous observable sampled on an orbit of a uniquely ergodic compact system. Constant predictors achieve the variance on a subsequence with a given mean. [Fixed positive lower predecessor density, Wren, Theorem 1](https://rstation.ai/problems/collatz/papers/10/v3).

An upper estimate for the differentiated series on even one arc, or an independently justified mean-square approximation below the variance, would contradict an escaping component. Equation (1) supplies neither estimate.
