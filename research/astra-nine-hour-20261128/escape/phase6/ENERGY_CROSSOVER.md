# Pointwise Fourier decay and the moving-root energy

The [uniform ordinary-source Fourier bound](LOCAL_TRIT_AND_RAJCHMAN.md) and the [moving-root energy lower bound](https://github.com/GettysburgResearch/collatz/blob/ca48af42546268771e34297872783631f61e8f02/research/astra-global-rigidity-20261128/mass/MACROSCOPIC_REAL_ENERGY.md) hold at compatible scales. The following family exhibits their compatibility even with exact interior stabilization at every sufficiently large root. Its prototype comes from a genuine positive ordinary basin. The scaled family is a family of measures; no integer inverse genealogy is assigned to it.

Take the base-two first-minimum correction law from the basin of one, normalized by its positive mass, and put its coordinate in natural logs. Its support is bounded. Apply a fixed affine map with positive slope to place the support in \([b,2b]\subset(0,0.216)\). Call the new variable \(B\), and let \(J=e^{-B}\). Its Fourier transform in the \(B\)-coordinate satisfies \(O_\epsilon((1+\log(2+|\tau|))^{-1/2+\epsilon})\) by the high-frequency theorem. Weaver's marked first-hit law gives its singularity and the finite quantitative covers below under that paper's named assumptions. [Weaver, Paper 175, Theorem 1 and §7](https://rstation.ai/problems/collatz/papers/175)

At every integer \(y\) sufficiently large take \(F_y=1-1/y\), \(h_y=y/F_y\), and set
\[
  R_y=y(1-J/F_y),\qquad \mu_y=\mathcal L(R_y),\qquad
  T_y(r)=F_y(1-r/y).
\]
Now \(0<R_y<y\), \(M_y=h_yF_y/y=1\), and \((T_y)_*\mu_y=\mathcal L(J)\) exactly. Every relative interior restriction therefore stabilizes. On every one of these measures the log first-arrival coordinate is exactly \(-\log(1-R_y/y)=B+\log F_y\). Its Fourier magnitudes are identical across all \(y\), so the target-uniform pointwise estimate persists. Choose a fixed rational \(0<t<1-e^{-b}\); then \(R_y\ge ty\) almost surely for every sufficiently large \(y\).

The quantitative cover in Paper 175 §7 is at mesh \(r_N=2^{-8N}\). For a positive-mass subset of the prototype law, there are fixed \(i,N_0\) such that for every \(N\ge N_0\) that subset lies in a union of \(O(i/(r_N\sqrt N))\) cells of length \(r_N\). This follows by countable exhaustion from its eventual membership in \(V_{N,1/i}\), and the finite-root terminal log coordinate is bi-Lipschitz on its supported interval. The further changes to \(B,J\) are Lipschitz there. Choose \(r_N\asymp1/y\) within the fixed factor \(2^8\). Each original cover cell maps to \(O(1)\) physical unit bins for \(R_y\). Thus a fixed positive mass lies in \(O(y/\sqrt{\log y})\) bins in \([ty,y]\), and Cauchy–Schwarz gives
\[
       \frac{h_y^2}{y}\sum_{k\ge0}
          \mu_y\big([k,k+1)\cap[ty,y]\big)^2
               \gg\sqrt{\log y}.
\]
The normalization \(h_y^2/y\asymp y\) is essential. The ordinary unweighted first-arrival law and the canonical inverse law are related by weighting by \(e^{-B}\) with a controlled scalar on a fixed escaping component. On the common compact interval for \(B\), multiplying by this smooth weight, or its reciprocal, preserves the stated Fourier bound. Extend the weight there to a compactly supported smooth function and convolve with its Schwartz Fourier transform. Splitting that convolution at \(|u|=|\tau|/2\) gives the same bound uniformly. Thus either weighting convention in the model gives the same collision order and Fourier decay. [PR213, weighted ordinary trace identity (4)](https://github.com/GettysburgResearch/collatz/blob/ca48af42546268771e34297872783631f61e8f02/research/astra-global-rigidity-20261128/mass/REAL_OFFSET_ORDINARY_TRACE.md)

This construction uses a single fixed original law throughout. There is no exchange of the high-root and high-frequency limits. At physical resolution one, the relative log resolution is comparable to \(1/y\) on this interior strip. An upper estimate for collision energy requires integrated control through frequencies of order \(y\). The uniform bound at each individual frequency allows a much larger integral than \(\sqrt{\log y}\). Any forcing argument using this crossover must supply additional information from the ordinary genealogy or a stronger integrated law.
