# Spatial profiles and the exact boundary coefficient of native unit eigenfunctions

Let \(T(2m)=m\), \(T(2m+1)=3m+2\). Fix complex units \(u_0,u_1\). Consider every bounded function on positive integers obeying the **pointwise** equations
\[
                 f(Tn)=u_{n\bmod2}f(n),\qquad \|f\|_\infty\le1.       \tag{1}
\]
The two phases need not agree. The only pair that can retain a nonzero macroscopic source profile has the form
\[
                u_0=2^{-i\tau},\qquad u_1=(3/2)^{i\tau}                 \tag{2}
\]
for a real \(\tau\), unique when it exists. For every continuous compactly supported \(\Phi\) on \((0,\infty)\), if (2) fails then
\[
          \sup_f\left|X^{-1}\sum_n f(n)\Phi(n/X)\right|\to0.           \tag{3}
\]
If (2) holds, there is a bounded linear functional \(c(f)\), with \(|c(f)|\le1\) on the indicated unit ball, such that uniformly over these \(f\)
\[
 X^{-1}\sum_n f(n)\Phi(n/X)
       =X^{i\tau}c(f)\int_0^\infty v^{i\tau}\Phi(v)\,dv+o(1).        \tag{4}
\]
The source-weighted ordinary mean defining \(c(f)\) exists without assuming it in advance. On writing \(b(n)=n^{-i\tau}f(n)\), \(\kappa=\tfrac12\log(4/3)\), its exact boundary formula is
\[
 \boxed{\quad \kappa c(f)=\sum_{y\ge1} b(y)
   \left[\frac{3\mathbf1_{y\equiv2\ (3)}}{2y-1}
           \left(\frac{2y}{2y-1}\right)^{i\tau}-\frac1{2y}\right].\quad}       \tag{5}
\]
The sum is in physical increasing order. The sum of the absolute values of its **octave sums** beyond \(Y\) is \(O_A((1+|\tau|)(1+\log Y)^{-A})\) for every fixed \(A\). The corresponding claim for the absolute values of individual terms is unnecessary and generally false. The only Collatz-specific external analytic input is the signed native starting-trit estimate for the complete endpoint and odd count. [Precise input (3), with original-source pins](../phase2/NATIVE_BINOMIAL_TRANSFER.md)

## Macroscopic rigidity

Put \(a=\log2\), \(L=\log3\). For any mean-zero bounded ternary periodic \(\psi\), any subinterval of \([Y,2Y]\), and functions (1),
\[
       \left|\sum_{n\in I}\psi(n)f(n)\right|\ll_A Y(1+\log Y)^{-A}. \tag{6}
\]
Indeed \(f(n)=u_0^{-(t-F_t(n))}u_1^{-F_t(n)} f(T^tn)\) for every positive \(t\). This is a unit-ball test of the complete joint law; send the free terminal date to infinity in the signed trit bound. Taking prefix differences gives the interval statement. The constants in (6) are uniform over the phases. Multiplying by \(n^{-i\tau}\) costs at most a factor \(1+O(|\tau|)\) by partial summation on that octave.

Along any sequence \(X\to\infty\) and choices of the unit-ball functions (1) with the prescribed phases, take a vague subsequential limit of \(X^{-1}\sum_n f(n)\delta_{n/X}\) on \((0,\infty)\). Absolute domination by the ordinary grid gives a limit \(g(v)\,dv\), \(|g|\le1\). Split by the exact first parity and use (6) at the genuine odd image \(y\equiv2\pmod3\). In a compact continuous test the difference between \((2y-1)/(3X)\) and \(2y/(3X)\) costs \(o(1)\); step approximation justifies the use of (6). The result, almost everywhere, is
\[
       g(v)=\tfrac12u_0^{-1}g(v/2)+\tfrac12u_1^{-1}g(3v/2).           \tag{7}
\]
For \(G(x)=g(e^x)\), iterate this equality \(j\) times. With \(p_{j,k}=2^{-j}\binom jk\), extended by zero off \([0,j]\),
\[
 G(x)=u_0^{-j}\sum_k p_{j,k}(u_0/u_1)^kG(x-ja+kL).
\]
Shift by \(L\) and reindex. The essential supremum of \(G(x+L)-(u_1/u_0)G(x)\) is at most \(\sum_k|p_{j,k}-p_{j,k-1}|=2\max_k p_{j,k}\to0\). Thus \(G(x+L)=(u_1/u_0)G(x)\), and (7) gives \(G(x-a)=u_0G(x)\). Multiply by a character \(e^{-i\tau_0x}\) with \(e^{i\tau_0 L}=u_1/u_0\) to obtain an \(L\)-periodic bounded function. Its circle Fourier expansion can retain a coefficient only at a frequency \(\tau=\tau_0+2\pi k/L\) with \(e^{-i\tau a}=u_0\). Irrationality of \(a/L\) permits at most one. This proves (3), including uniformity by the original moving choice of \(f\), and the shape of every limit in the remaining case.

## Existence and normalization of the resonant amplitude

Under (2), \(b(2m)=b(m)\). At an odd input \(n=(2y-1)/3\) with positive \(y\equiv2\pmod3\),
\[
                 b(n)=\left(\frac{2y}{2y-1}\right)^{i\tau}b(y).
\]
For real \(x\) put \(U(x)=e^{-x}\sum_{n\le e^x} b(n)\), zero for \(x<0\). Write \((PU)(x)=\tfrac12 U(x-a)+\tfrac12 U(x+L-a)\). The *exact* residual \(r=U-PU\) at \(Y=e^x\) is
\[
 Y r(\log Y)=\sum_{\substack{2y-1\le3Y\\y\equiv2\ (3)}}
       b(y)\left(\frac{2y}{2y-1}\right)^{i\tau}
      -\tfrac13\sum_{2y\le3Y}b(y).                                    \tag{8}
\]
The even part canceled identically. The two cutoffs differ by at most one integer, and the sum of the costs of replacing the physical factors by one is \(O(|\tau|\log(2+Y))\). Equation (6) on dyadic octaves yields
\[
  |r(x)|\ll_A(1+|\tau|)(1+x)^{-A}\quad(x\ge0),\qquad
  r(x)=0\quad(x<a-L).                                                  \tag{9}
\]
On every fixed compact interval \(r\) has finitely many jumps at fixed locations and is a constant combination of \(e^{-x}\) on each intervening interval.

Let the fair increments be \(-a,L-a\) with mean \(-\kappa\). For their partial sums \(S_j\), telescope (8), use \(x+S_j\to-\infty\) almost surely, and obtain \(U(x)=\sum_{j\ge0}\mathbb E r(x+S_j)\). The uniform unit-strip occupation bound and (9) justify absolute summation. The sign-reversed walk is nonlattice in Blackwell's sense: a common lattice through zero for \(a,a-L\) would make \(a/L\) rational. Blackwell's theorem for increments of either sign implies that its occupation of each fixed translated interval of length \(h\) tends to \(h/\kappa\) as the center goes to positive infinity. Step approximation on a compact interval and the uniform unit-strip tail thus give
\[
            U(x)\longrightarrow \kappa^{-1}\int_{\mathbb R} r(v)\,dv=:c(f).
\]
This is uniform over \(f\) at fixed \(\tau\). On a fixed compact interval the residuals form a bounded subset of a fixed finite-dimensional space of piecewise functions, because only finitely many values of \(b\) enter. The compact subsequence argument or a finite supremum-norm net makes the step approximation uniform. Taking differences on proportional cutoffs and approximating the compact test \(v^{i\tau}\Phi(v)\) now proves (4). [Blackwell, *Extension of a renewal theorem*, Theorem 1 (1953)](https://msp.org/pjm/1953/3-2/pjm-v3-n2-p03-p.pdf) · [Elementary uniform unit-strip bound (5)](../phase2/NATIVE_BINOMIAL_TRANSFER.md)

Integrate (8) up to \(x=\log(2N/3)\). Both inner sums involve exactly \(y\le N\) or their ternary restriction. Direct integration of \(e^{-x}\) gives the truncation of (5) plus the boundary term
\[
   -\frac{3}{2N}\sum_{y\le N} b(y)
       \left[\mathbf1_{y\equiv2\ (3)}(2y/(2y-1))^{i\tau}-1/3\right].
\]
It tends to zero by (6) and the harmonic bound on the physical factors' differences from one. For a single octave in (5), summation by parts bounds its signed leading term by \(O_A((1+|\tau|)(1+\log Y)^{-A})\), and its remaining absolute terms by \(O((1+|\tau|)/Y)\). Sum using a larger logarithmic exponent to obtain the stated full grouped-tail bound.

## The surviving positive-source mode

On a fixed escaping component put \(R(n)=\prod_{j:T^jn\text{ odd}}(1+1/(3T^jn))\) and \(P(n)=nR(n)\). All products converge by simple-path reciprocal packing. Then \(P(Tn)=3^{\mathbf1_{n\text{ odd}}}P(n)/2\). Extending \(P(n)^{i\tau}\) by zero off that component gives (1)–(2) for every \(\tau\). At \(\tau=2\pi/\log3\) both branches even have the same phase. In this case \(b=\mathbf1_C R^{i\tau}\) has all its nonzero values on one arc of angular length less than \(\pi/2\) by the verified simple-trajectory bound. It follows that \(|c(f)|\ge d_C/\sqrt2\) for the ordinary component density \(d_C\). This gives source regularity and an explicit height-ordered series for precisely the possible nonzero resonance. Its summands have both signs already at \(\tau=0\). The theorem supplies no identity assigning that resonant coefficient zero. [Verified correction arc and its origin](../phase4/HARMONIC_SOURCE_PHASE.md)

## Relation to the odd-map spectral results

PR212 studies the weighted all-parent odd-map operator on the Hilbert space with weights \(h(x)/x\). Its two-sided killing-weight Green operator has a gap, counts positive cycles by the multiplicity at one, and detects individual nonperiodic odd unit sites in its spectrum. Its annulus theorem realizes the irrational height-rotation character on part of a weak symbolic limit of uniformly rooted cycles. The argument above concerns unit-valued branch multipliers on the shortcut graph and their profiles under an ordinary spatial dilation. The signed starting-trit estimate and the physical increasing-order flux determine those source profiles. [Positive Green-operator theorem](https://github.com/GettysburgResearch/collatz/blob/0e4b428211b0bce432efc7d9d19ff4ea552248ec/research/astra-global-20261128/cycles/POSITIVE_GREEN_SPECTRUM.md) · [Odd-unit spectral grid](https://github.com/GettysburgResearch/collatz/blob/0e4b428211b0bce432efc7d9d19ff4ea552248ec/research/astra-global-20261128/cycles/ODD_SPECTRAL_GRID.md) · [Annulus spectral factor](https://github.com/GettysburgResearch/collatz/blob/0e4b428211b0bce432efc7d9d19ff4ea552248ec/research/astra-global-20261128/cycles/ANNULUS_SPECTRAL_FACTOR.md)
