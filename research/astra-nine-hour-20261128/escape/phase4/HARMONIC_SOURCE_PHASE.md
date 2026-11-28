# One source and one true endpoint through the whole critical window

On the positive integers \(X<n\le3X\), give \(n\) weight \(1/n\) divided by the finite sum of those weights. At a single shortcut date \(t\), set
\[
          \Theta_{X,t}(n)=\{\log_3(2^t T^t(n)/n)\}\in[0,1).
\]
Use \(\mu=2/\log(4/3)\), \(b_X=\sigma\sqrt{\log X}\) with \(\sigma^2=2(\log3)^2/(\log(4/3))^3\), and \(u_X(t)=(t-\mu\log X)/b_X\). On the stated ordinary source inputs, the following formula holds uniformly over all nonnegative physical dates:
\[
 \sup_{t\ge0}\left|\Pr(\Theta_{X,t}\in[0,1/4])-1+
       \frac34\Phi(u_X(t))(1-d_{\rm esc})\right|\longrightarrow0.       \tag{1}
\]
Here \(d_{\rm esc}\) is the total natural density of unbounded positive orbits. Thus any supercritical choice of one native clock recovers \(d_{\rm esc}\) from one explicitly computable rational frequency. The indicator can be tested exactly with integers. Locate \(k\) such that \(3^k n\le2^t T^t n<3^{k+1}n\), then test \((2^t T^t n)^4\le 3^{4k+1}n^4\). The index \(k\) is nonnegative because every shortcut step multiplies a state by at least \(1/2\).

Write \(W\) for the fixed finite union of the true forward orbits through the published verification floor \(2^{68}\). If the endpoint is nonperiodic and lies outside \(W\), its whole prefix is simple and stays above that floor. The exact affine identity gives
\[
       \Theta_{X,t}=\left\{\frac{1}{\log3}
               \sum_{\substack{j<t\\T^j n\text{ odd}}}
                       \log(1+1/(3T^j n))\right\}.
\]
Weaver 175 (23) places this sum between 0 and \(0.21645\). Its normalized value belongs to \([0,1/4]\) and has no wrap. The remaining nonperiodic endpoints in \(W\) have aggregate probability \(O_W((\log X)^{-1/2})\) at every date, by the all-clock atom bound. The harmonic octave sampling costs only an absolute constant relative to the uniform prefix through \(3X\). [High simple-segment bound and its finite-computation attribution](https://rstation.ai/problems/collatz/papers/175/v1) · [Uniform atom and periodic-phase theorems](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md)

For a sequence \(u_X(t)\to u\in[-\infty,+\infty]\), the joint subprobability law restricted to periodic endpoints,
\[
       (\log_3(n/X),T^tn)\big|_{T^t n\;{\rm periodic}},
\]
converges weakly on \([0,1]\times\mathbb N_{\rm discrete}\) to the product of Lebesgue measure on \([0,1]\) and \(\Phi(u)\pi\), where \(\pi=\sum_{C\ {\rm bounded}}d_C\operatorname{Unif}(\Gamma_C)\). Indeed the uniform-prefix periodic-phase theorem at every proportional endpoint supplies the rectangular counts by subtraction, and Riemann approximation by step functions gives the continuous harmonic weight. Finite component exhaustion controls all remaining endpoints. Consequently the circular restriction of the source–endpoint phase to periodic endpoints converges to \(\Phi(u)(1-d_{\rm esc})\) times Haar. To see this even for moving \(t\log_3 2-\log_3X\), pass to a further subsequence on which that shift converges modulo 1. Each fixed endpoint adds only its constant \(\log_3 y\), and the independent initial uniform angle already makes the difference circular Haar. The limit is independent of the extracted shift, and arcs have null boundary under this periodic limit. Adding the nonperiodic sector proves (1) on every convergent sequence of \(u_X(t)\). Compactness of the extended line gives the stated uniformity.

More generally every fixed arc \(A\) whose closure is disjoint from \([0,0.21645/\log3]\) satisfies
\[
        \Pr(\Theta_{X,t}\in A)= |A|\Phi(u_X(t))(1-d_{\rm esc})+o(1)
\]
uniformly in \(t\), with arc length normalized to one full turn. The same reasoning produces a single Mellin coefficient. Set \(M_{X,t}=\mathbb E e^{2\pi i\Theta_{X,t}}\). Its periodic contribution tends uniformly to zero. After multiplication by \(e^{-\pi i/4}\), its real part on the common nonperiodic arc is at least \(1/\sqrt2\). Hence
\[
 \frac{1-\Phi(u_X(t))(1-d_{\rm esc})}{\sqrt2}-o(1)
 \ \le\ |M_{X,t}|\ \le\ 1-\Phi(u_X(t))(1-d_{\rm esc})+o(1).
\]
In particular vanishing along one supercritical sequence is equivalent to the absence of an escaping component, using positive ordinary predecessor density at each supplied ternary unit. The circle test uses both the physical source and its endpoint at one native date. It uses neither the bilateral inverse-mark measure nor a computation of the odd count. A proof of cancellation of this source-weighted Mellin coefficient at a supercritical time remains open. The [one-endpoint unweighted difference](../phase3/ONE_ENDPOINT_CHARACTER.md) and [two-source total-variation profile](FINITE_SHELL_DETECTOR.md) give different tests.

The [exact control](check_shell_phase.py) compared 21,760 raw source–endpoint fourth-power tests against independent counted correction reconstructions. Among the 8,886 tested prefixes whose states all exceeded twice the physical duration, every phase lay in the designated quarter arc. Both ordinary and optimized Python runs use explicit checks.
