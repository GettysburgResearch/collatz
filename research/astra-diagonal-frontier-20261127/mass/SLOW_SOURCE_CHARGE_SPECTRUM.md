# The escaping charge spectrum from slowly growing ordinary source sets

For odd inputs \(x\le X\), run the actual first \(n\) odd steps. At each pair \((y,s)\) count sources first reaching their odd endpoint \(y=U^nx\) at this depth with native clock \(s\). Divide each count by \(p=y2^s/3^n\) to obtain \(m^{\le X}_{n,s}(y)\). Define \(S_q(n,X)=\sum_{y,s} (m^{\le X}_{n,s}(y))^q\). All sums at finite \(n,X\) use only the stated finite set of ordinary inputs. Put \(D=\log(4/3)\) and \(A_q=q^{-1/2}(4\pi)^{-(q-1)/2}\).

On the source-qualified inputs and with the component charges \(H_C\) of [the common-depth cubic law](COMMON_DEPTH_CUBIC_RESIDUE.md), for \(1\le q<3\) one has
\[
 \lim_{\substack{X,n\to\infty\\ n\ge300\log X}}
   \frac{S_q(n,X)}{(\log X)^{(3-q)/2}}
     =\frac{2 A_q D^{-(3-q)/2}}{3-q}\sum_{C\ {\rm escaping}} H_C^q . \tag{1}
\]
At the cubic exponent both original limits may be entirely independent:
\[
 \lim_{n,X\to\infty}
  \frac{S_3(n,X)}{\log(\min\{n,\log X\})}
      =\frac1{4\pi\sqrt3}\sum_{C\ {\rm escaping}}H_C^3 .               \tag{2}
\]
With all positive sources, including initial halvings in each native clock, replace \(H_C\) with \(2H_C\) in (1)–(2). In particular \(X=n\), or any arbitrarily slowly diverging \(X\le n\), suffices. No source above this cutoff enters the finite calculation. The \(q=2\) coefficient is \((2\pi D)^{-1/2}\sum_C H_C^2\). The self-pair contribution \(\sum_x(f_n(x)/x)^2\le\sum_x x^{-2}\) is bounded, so the square-root growth there comes from genuine coincidences of distinct starting integers.

## Corrected-height crop for a signed clock source

In the full corrected table of an escaping component, write \(j=-v\), \(p^*=P_0 3^{-j}2^l\). Let \(a_q(L)=L^{(3-q)/2}\) for \(q<3\) and \(a_3(L)=\log L\). Then for each component
\[
 \lim_{R\to\infty}\frac{\sum_{p^*\le R} M_{C,v}(l)^q}{a_q(\log R)}
 =\begin{cases}
   H_C^q\, 2 A_q D^{-(3-q)/2}/(3-q),&1\le q<3,\\
   H_C^3/(4\pi\sqrt3),&q=3.
 \end{cases}                                                          \tag{3}
\]
In the convolution from [PR 195, LOCAL_HEIGHT_LAW (4)–(5)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/LOCAL_HEIGHT_LAW.md), each signed source has physical height \(p_0\ge2/3\), and the source coefficients are absolutely summable. A translate of the geometric kernel contributes at lag \(b\ge0\), elapsed native time \(t\), corrected height \(p^*=p_0 2^t/3^b\). In the kernel measure, \(t\) is a sum of \(b\) independent positive geometric increments of mean 2. The log-height increment then has mean \(Db\), with exponential concentration for a fixed proportional departure. This is a fact about the convolution kernel; the original physical source weights and signed impulse coefficients have not been resampled.

The local Gaussian law gives \(\sum_t g_b(t)^q\sim A_q b^{-(q-1)/2}\) for every \(1\le q\le3\). The tails outside \(|t-2b|\le B\sqrt b\) are bounded by \(\|g_b\|_\infty^{q-1}\Pr(|S_b-2b|>B\sqrt b)\), and Chebyshev suffices to pass \(B\to\infty\). For fixed \(p_0\) and \(\varepsilon>0\), all these central terms through \(b\le(1-\varepsilon)\log R/D\) are in the crop for large \(R\). Above \(b\ge(1+\varepsilon)\log R/D\) the cropped sum is exponentially small in \(b\), by the geometric lower-tail Chernoff bound, for all sufficiently large \(R\). Summing the row asymptotic on both sides and shrinking \(\varepsilon\) gives (3) for a single kernel with net one. Uniformly for *all* \(p_0\ge2/3\) the cropped \(q\)-norm is \(O_q(a_q(\log R)^{1/q})\), using \(b\le (2/D)\log R\) and the same lower-tail bound above it.

For a fixed lattice shift the difference of the two kernels is negligible in this norm. In rows \(b\to\infty\) a spatial or grade shift has sum norm \(O(b^{-1/2})\) and point norm \(O(b^{-1})\), as shown in [the clock spectrum](FIRST_ARRIVAL_ROW_SPECTRUM.md). Its \(q\)-power sum through \(b\le K\log R\) is therefore \(O(\sum_{1\le b\le K\log R} b^{-q+1/2}+1)=o(a_q(\log R))\). For \(q=3\) that left side is bounded. Beyond this grade cutoff use the sum of the two exponentially small cropped kernels, choosing any fixed sufficiently large \(K\). Thus finitely many impulse translates have the profile of their net multiple. The \(\ell^1\) tail of impulses contributes at most its norm times \(O_q(a_q(\log R)^{1/q})\) by Minkowski and the uniform translated bound. This proves (3). The initial halving convolution in the all-positive table multiplies each source height by \(2^e\), preserving the lower height bound, and multiplies the net by two.

## The original finite-source limits

Assume first \(n\ge300\log X\). Each retained true row containing an input \(x\le X\) has \(p\le X/c_0\) by the simple-path correction bound. Truncate at a fixed large landing height \(r\). For each octave \(2^k\le p<2^{k+1}\) beyond a fixed \(k_r\), the source-level duration estimate (2) in the common-depth note excludes total mass \(O_B((\log r)^{-B})\) from inputs that have failed to reach at most \(r\) by depth \(n/2\). The source octaves needed to cover \([c_0 2^k,2^{k+1}]\) extend only to a fixed multiple of \(X\); \(101\log(CX)<n/2\) for large \(X\). This remains true after removing all \(x>X\), including partially filled top octaves. The total \(q\)-power error per octave is bounded by \(q\max m^{q-1}\) times this excluded mass, hence \(O_{q,B}((1+k)^{-(q-1)/2}(\log r)^{-B})\). Its sum is \(O_{q,B}(a_q(\log X)(\log r)^{-B})\). The low octaves contribute \(O_r(1)\) altogether.

As in the common-depth proof, every retained first-hit row beyond finitely many delays comes from a finite list of escaping spines \(y_N\) meeting the sites at most \(r\), with \(N\ge n/2-O_r(1)\). Its full-cell weight increases by at most \(1/f_N=1+o_r(1)\), where \(f_N=y_N/P(y_N)\to1\). Its corrected height \(p^*=p/f_N\) is at most a fixed multiple of \(X\). Distinct rows in that component have different corrected cell indices. Apply (3) at this height cutoff. Take \(n,X\to\infty\) first and \(r\to\infty\) afterwards. This gives the claimed upper coefficients.

Conversely, retain any finite list of distinct escaping components and one spine in each. At native totals \(s=A_{n-k}+l\), \(|l-2k|\le B\sqrt k\), and target \(y_{n-k}\), take
\(k\le (1-\varepsilon)(\log X)/D\). For large \(X\) all the resulting central full cells have \(p^*=P_0 3^{-k}2^l\le X\), hence all their physical first-arrival members satisfy \(x\le p=f_{n-k}p^*\le X\). Their distinct rows have actual masses \(H_C g_k(l)+o(k^{-1/2})\) by [the moving local law](MOVING_FIRST_ARRIVAL_LOCAL_LAW.md), uniformly as both \(k\) and \(n-k\) grow; \(n\ge300\log X\) ensures the latter condition. Their summed \(q\)-power over \(l\) has leading coefficient \(H_C^q\int_{-B}^{B}\phi^q\) at order \(k^{-(q-1)/2}\). Summing over \(k\), letting \(B\to\infty,\varepsilon\downarrow0\), then taking the supremum over finite component lists gives (1) and (2) in this range.

For the remaining cubic regime \(n<300\log X\), one has \(\log\min(n,\log X)=\log n+O(1)\). The upper is the full common-depth cubic theorem by positivity. The same lower proof now uses \(k\le c\min(n,\log X)\) with a sufficiently small fixed \(c>0\) to retain all central sources and keep \(n-k\ge n/2\). Its harmonic sum again has leading term \(\log\min(n,\log X)\). Combining the two regimes proves the independent joint limit (2).

## Information recovered and the unresolved arithmetic estimate

For \(1<q<3\) the left side of (1) recovers \(\sum_C H_C^q\) without a component test in the finite calculation. These values on any open subinterval determine the multiset of positive charges: the finite measure \(\mu=\sum_C H_C\delta_{H_C}\) has bounded support, and its Mellin transform \(\int t^{q-1}\,d\mu(t)\) is analytic for \(\Re q>1\). Equality on an interval gives equality at all integer \(q\ge2\), hence equality of the measures on positive support by polynomial approximation; neither measure has an atom at zero. The multiplicity at a positive \(h\) is \(\mu(\{h\})/h\).

The sharp task left by the square moment is to prove \(S_2(n,n)=o(\sqrt{\log n})\) independently from the original integer dynamics. It is equivalent to exclusion of escape on the stated sources. A proof would need to control the off-diagonal simultaneous first-arrival collisions, including those whose ordinary paths merged long before observation. Removing realized diagonal pairs alone subtracts only \(O(1)\).
