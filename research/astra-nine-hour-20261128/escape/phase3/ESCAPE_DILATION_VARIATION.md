# Total variation of complete ordinary endpoints under dilation

Let \(\mu_{X,t}\) be the entire law of \(T^t n\) for the uniform positive integer \(n\le X\). Suppose \((t-\mu\log X)/b_X\to+\infty\), with the ordinary first-arrival center and window in the [endpoint spectrum](ENDPOINT_CLOCK_SPECTRUM.md). For every fixed integer \(r\) and fixed \(\alpha>0\), the following source-qualified written deduction gives
\[
 \lim_{X\to\infty}\|\mu_{\alpha X,t+r}-\mu_{X,t}\|_{\rm TV}
    =\tfrac12\sum_{C\ {\rm escaping}}\int_0^1
          |K_C(\theta+\Delta)-K_C(\theta)|\,d\theta ,
 \qquad \Delta=r\log_3 2-\log_3\alpha .                              \tag{1}
\]
All sources and endpoints here are positive ordinary integers. At these clocks periodic phases give zero to the variation. The canonical profiles \(K_C\) are defined by the marked first-arrival and ordinary sampling argument in the endpoint spectrum.

For the proof, choose finitely many fixed periodic components and escaping waypoints \(a_i\) whose full finite-orbit components and predecessor basins \(B_{a_i}\) have total density above \(1-\epsilon\). This is possible by full component coverage and \(d_{a_j}\uparrow d_C\) along each escaping ray. By the fixed-target first-clock Gaussian, all but an upper limiting \(\epsilon\) of the population have entered the selected finite cycles or the selected escaping futures by the tested dates. This holds for both source cutoffs because their center difference is bounded and \(b_{\alpha X}/b_X\to1\). On the selected finite cycles the endpoint masses converge to uniform phase at their individual basin weights, by the previously established fixed-clock residue law. [PR213, periodic-phase limit and finite coverage](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md)

On a selected escaping ray, for \(j\ge0\) the coordinate \(z_j=(t-j-\mu\log X)/b_X\) at the baseline source differs by \(o(1)\) uniformly on compact intervals from the coordinate at \(\alpha X,t+r\). The phase at the second cutoff differs **exactly** by \(\Delta\). Use the uniform local profile, tail removal and moving-waypoint replacement of the endpoint spectrum, now in the sum of absolute differences over the \(O_B(b_X)\) central ray points. The error per point is \(o(1/b_X)\) plus \(C(d_C-d_{a_J})/b_X\), with the latter arbitrarily small after fixing a far waypoint. The Gaussian integrates to one and irrational rotation averages the phase difference. This gives the summand of (1) on that ray. The factor \(1/2\) uses the probability convention for total variation. The omitted mass in the two measures and omitted profile integrals cost \(O(\epsilon)\). Release the truncation.

## A strict variation coefficient from the real mark

For this section impose in addition the cited compact-null support theorem for all finite simple positive correction products. Its hypotheses include the fixed-root closed-support and synchronization inputs. Then the total ordinary escaped density \(d_{\rm esc}=\sum_C d_C\) is exactly the following infinitesimal dilation variation:
\[
 d_{\rm esc}=\lim_{h\downarrow0}\frac1h\lim_{X\to\infty}
                 \|\mu_{e^hX,t}-\mu_{X,t}\|_{\rm TV}.                 \tag{2}
\]
For each fixed irrational \(\Delta\) there are constants \(c_\Delta>0\), independent of all components and their weights, such that the right side of (1) belongs to \([c_\Delta d_{\rm esc},d_{\rm esc}]\). In particular this holds at \(r=1,\alpha=1\). At a pure factor-three dilation the right side of (1) vanishes. These assertions concern the total escaped fraction, including all possible distinct escaping components. They permit every bounded cycle. [PR212, uniform compact-null real correction support and its exact dependencies](https://github.com/GettysburgResearch/collatz/blob/e082b95a503d622bbbd121801f6bcadcab50df05/research/astra-infinite-descent-20261127/escape/FAIR_CLOCK_DIFFUSION.md)

Indeed the canonical bilateral product mark has support in that same compact null set \(K\subset[c,1]\). For fixed \(w\) on an escaping ray its law is a limit of genuine inverse finite prefixes ending at \(w\) followed by longer and longer pieces of the true forward path from \(w\). Each concatenation is simple: any repetition would put the forward orbit on a cycle. Taking the finite-prefix row limit, the forward-tail limit, and finally the total-variation limit along \(w\) preserves the common closed support. The image \(E=\{-\log_3 u\bmod1:u\in K\}\) is a proper compact null subset of the circle, because the logarithm is Lipschitz on \([c,1]\).

The following periodization and variation calculation is the exponential-kernel formula already given by Weaver for Leen's clock histograms at the first orbit minimum, in units of \(\log_2\). We apply it to the complete postcritical positive endpoint population on escaping rays, with period one in \(\log_3\). [Weaver 175 v1, §10, (19), and Leen attribution](https://rstation.ai/problems/collatz/papers/175/v1)

For \(u\in[c,1]\), the one-periodic function \(A(\theta,u)\) grows at rate \((\log3)A\) between its jumps of size \(-1/u\) at \(\theta=-\log_3u\bmod1\). Consequently its distributional derivative as a finite signed measure is \((\log3)A(\theta,u)d\theta-u^{-1}\delta_{-\log_3u}\). Integrating (2) of the endpoint spectrum gives for each escaping component
\[
  dK_C=(\log3)K_C(\theta)d\theta-(\log3)d_C\rho_C,
\]
where \(\rho_C\) is the probability obtained from \(u^{-1}\eta_C(du)\) by normalization and the displayed circle map. The two terms are mutually singular since \(\rho_C(E)=1\). Thus \(\operatorname{Var}(K_C)=2(\log3)d_C\). For a periodic function of bounded variation,
\[
 \|K_C(\cdot+h')-K_C\|_1/|h'|\longrightarrow\operatorname{Var}(K_C).
\]
The upper bound by the variation follows by integrating translated variation measures over the increment interval. For the lower bound the signed difference quotients converge weakly as measures to the distributional derivative, and its total variation is lower semicontinuous. In (1) take \(\Delta=-h/\log3\); dominated convergence uses that same upper bound and \(\sum_C d_C\le1\). This proves (2).

For the uniform fixed-shift lower bound, every normalized \(K_C/d_C\) is the circle convolution \(k*\rho_C\) with the same probability density \(k\), a translated-periodic choice of \((\log3)A(\theta,1)\). Equivalently this convolution is the periodic solution of \(df=(\log3)(f\,d\theta-\rho_C)\) with integral one. The map \(\rho\mapsto k*\rho\) from probabilities on \(E\) to \(L^1\) is continuous in weak convergence: approximate the integrable kernel in \(L^1\) by trigonometric polynomials and use their finitely many Fourier coefficients. The image is compact. If one of these functions were invariant under an irrational \(\Delta\), all its nonzero Fourier modes would vanish. Its derivative equation would force \(\rho\) to be circle Haar measure, impossible on \(E\). The translation difference therefore has a strictly positive minimum on this compact family. Its norm is at most two. Sum the resulting bounds in (1).

The same argument makes each \(K_C\) nonconstant on this additional support input. Hence the raw \(q\)-collision coefficient in the endpoint spectrum strictly exceeds its growing-window time average whenever any positive ordinary orbit escapes and the Gaussian integral is positive. Neither (1) nor (2) bounds the real dilation derivative below one escaped component's possible mass. An independent time-one stationarity theorem would force the right side to zero; the genuine native source recurrence itself preserves the circle phase and does not supply it.
