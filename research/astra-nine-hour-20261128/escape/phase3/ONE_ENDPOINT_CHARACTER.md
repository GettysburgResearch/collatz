# A single endpoint character detects positive escape

**PROPOSED, source-qualified written theorem.** Take \(\omega=2\pi/\log3\), \(\lambda=\log_3 2\), and any native clock with \((t-\mu\log X)/b_X\to+\infty\). With \(n\) uniform through \(X\), set
\[
 Z_X=e^{i\omega(t\log2-\log X)}
           \mathbb E_X\!\left[(T^{t+1}n)^{i\omega}-(T^t n)^{i\omega}\right],
 \quad y^{i\omega}=\exp(i\omega\log y).
\]
The limit exists. If \(d_{\rm esc}\) is the total natural density of escaping positive sources, then
\[
              d_{\rm esc}/6\ \le\ |\lim Z_X|\ \le\ 2d_{\rm esc}.       \tag{1}
\]
This uses the fixed-clock local transform of the [endpoint spectrum](ENDPOINT_CLOCK_SPECTRUM.md), and the published verification floor and finite simple-segment residue certificate specified below. The extra compact-null support hypothesis used for the [infinitesimal variation identity](ESCAPE_DILATION_VARIATION.md) is unnecessary for (1). The test itself uses two ordinary finite sums with no basin labels, thresholds, or moving targets.

Let \(K_C\) be the ordinary escape clock profile from (2) of the endpoint spectrum. On the ray \(y_j=T^ja\),
\[
   \log_3 y_j+j\lambda
          =\log_3 P(a)+F_j(a)+\log_3F(y_j),
\]
where \(F_j(a)\) counts the odd departures and \(F(y_j)\) is the remaining infinite product of the physical correction factors. Along the ray this product tends to one. On the contributing part with \(|t-j-\mu\log X|\le B b_X\) we have \(j\to\infty\) uniformly at these supercritical clocks. Thus the baseline co-rotated character at \(y_j\) is \(e^{2\pi i\theta}+o(1)\), with \(\theta=\log_3(P(a)2^{t-j}/X)\). At clock \(t+1\), the same evaluation contributes the extra prefactor \(e^{-2\pi i\lambda}\) when using its own local-clock phase. Compact truncation in the signed clock, irrational rotation, and then finite component exhaustion are justified exactly as for (1) of the dilation-variation note. On each finite cycle the ordinary endpoint distributions at the two dates converge to the same uniform phase law; their difference contributes zero even after the original unit-modulus prefactor. The result is
\[
 \lim Z_X=(e^{-2\pi i\lambda}-1)\sum_{C\ {\rm escaping}}
                         \int_0^1e^{2\pi i\theta}K_C(\theta)\,d\theta . \tag{2}
\]
The integral equals
\[
       d_C\frac{\log3}{\log3+2\pi i}
                 \int e^{2\pi i v}\,d\rho_C(v),
\]
where \(\rho_C\) is the probability on \(v=-\log_3 u\bmod1\) obtained from the actual bilateral mark \(u\) after weighting by \(u^{-1}\). This follows by integrating the geometric periodization in (2) of the endpoint spectrum over the whole real line through \(-\log_3u\). The equality uses only atomlessness and the positive source limit, independently of any null-support conclusion.

All escaping trajectories stay above \(2^{68}\), under Bařina's published certified verification through that floor. Weaver's exact finite bound (23) for **every finite distinct shortcut segment** above the floor gives
\[
        \sum_{w\ {\rm odd\ departure}}\log(1+1/(3w))
                            \le 216449006435109/10^{15}.
\]
Every finite inverse prefix used for the mark, appended to any finite piece of its escaping forward ray, is such a simple segment. All sites exceed the verified floor, including the inverse prefix, since they belong to that component. Pass through the fixed-root and along-ray mark limits to get \(0\le v\le0.21645/\log3<1/4\) with no circle wrapping. Thus all the complex averages over all components lie in the same arc's convex hull. After rotation by \(-\pi/4\) their real parts are at least \(\cos(\pi/4)>7/10\). Also \(1/2<\lambda<2/3\), so \(|e^{-2\pi i\lambda}-1|\ge\sqrt3>5/3\), and \(\log3/|\log3+2\pi i|>1/7\). These bounds give (1), including the case of no escape. The circle histogram kernel, its Fourier multiplier, and the verified correction ceiling are previous results for first-minimum laws; the observable in (1) concerns the whole native endpoint population after entry. [Weaver 175 v1, §§10–11, particularly (19) and (23), with verification source](https://rstation.ai/problems/collatz/papers/175/v1)

A related direct arithmetic restriction holds at **every** clock. If two escaping sources \(x,x'\) meet at the same native date, there is an integer \(k\) for which
\[
                   |\log(x'/x)-k\log3|\le 0.21645 .
\]
Subtract their two exact affine log identities at that date. Each accumulated correction is between zero and the preceding ceiling. For example \(x'=5x+c\), at fixed integer \(c\), cannot meet \(x\) after the same number of native steps in any escaping component once \(x\) is sufficiently large. A finite parity-cylinder meeting identity between two affine forms also requires their slopes to have ratio \(2^j3^k\) at specified clock displacement \(j\), by comparing their exact lift slopes; at equal clock it must be a power of three. [Sylve Recursions 204 v1, Proposition 1](https://rstation.ai/problems/collatz/papers/204/v1)

The phase of a single escaping trajectory rotates by \(-\lambda\) per time step up to a vanishing error. This gives equidistribution when its **time** varies. It does not give vanishing of the single-date **source** average in (2), which keeps that rotation synchronized. The unconditional time-one stationarity of the tested Mellin moment remains open.
