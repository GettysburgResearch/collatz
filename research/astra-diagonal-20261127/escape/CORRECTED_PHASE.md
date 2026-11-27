# The corrected real height and both local coordinates on each past grade

Assume an escaping component \(C\) with ordinary odd grade \(g(Ux)=g(x)+1\), corrected height \(P\), grade measures \(\mu_v\), and limiting mass \(H=H_C>0\) as in [the first-power transfer theorem](FIRST_POWER_HAAR.md). Put \(F(x)=x/P(x)\) and \(M=m_2\otimes m_3\). The uniform distinct-path reciprocal bound gives \(0<\eta\le F(x)\le1\) on \(C\). There is a probability \(\lambda_C\) on \([\eta,1]\) satisfying the individual-grade convergence
\[
 \sum_{g(x)=v}\frac1{P(x)}\delta_{(x_2,x_3,F(x))}
     \ \Rightarrow\ H M\otimes\lambda_C\qquad(v\to-\infty).              \tag{1}
\]
Here \(x_2,x_3\) are the original positive integer at both places. For grade zero based at \(a\), the corrected height has the deterministic angle \(\log_2P(x)\equiv\log_2P(a)+v\log_2 3\bmod1\), since \(P(Ux)=3\,2^{-e(x)}P(x)\). Hence the ordinary mantissa angle \(\log_2x\bmod1\) is the rotation of \(\log_2 F(x)\bmod1\) by this grade-dependent angle. Its limits along convergent angle subsequences follow from (1).

## Independence of the exact additive correction

The true edge identity is
\[
               F(Ux)-F(x)=\frac1{3P(x)}.                                  \tag{2}
\]
At grades tending to negative infinity the smallest ordinary positive vertex tends to infinity. Thus all one-edge changes there tend uniformly to zero, including across the full inverse tree. Take a subsequence \(v_i\to-\infty\) along which every fixed translate of the marked grade measures has a weak limit. Equation (2) and uniform continuity of bounded tests on the compact mark interval pass the transfer recursion to the limit, where the transfer leaves the mark fixed. Every unmarked limit equals \(HM\) by the [joint local theorem](FIRST_POWER_HAAR.md).

For a continuous mark test \(0\le u\le1\), write \(\nu_t\) for the \(u\)-weighted local marginal of the limiting translate \(t\). Then \(0\le\nu_t\le HM\) and \(\widehat L^*\nu_{t+1}=\nu_t\). These masses are constant even without assuming it. For all \(n\ge1\),
\[
 |\nu_t(1)-\nu_{t+1}(1)|
   =\left|\int(\rho_n-\rho_{n-1})\,d\nu_{t+n}\right|
   \le H\|\rho_n-\rho_{n-1}\|_{L^1(m_3)}\to0 .                        \tag{3}
\]
Indeed \(\widehat L^n1=\rho_n\) and \(\rho_n\) are the conditional expectations of the integrable stationary ternary density. By the earlier positive entrance uniqueness, each \(\nu_t\) is the same scalar multiple of \(M\). Testing all continuous \(u\) proves that every full cluster law is a product with a common mark marginal at all its translates.

## Identifying a unique marginal from a positive ordinary flow

Let \(h\) denote Valbuena's nonnegative lower-semicontinuous stationary density on all of \(\mathbb Z_3\), of Haar integral one, whose values at positive odd integers agree with their canonical traces. At nonunit sites \(h=0\). Fix \(v\). Ordinary harmonicity gives a canonical forward flow
\[
 \chi_v=\sum_{g(x)=v}\frac{h(x)}{P(x)}\delta_x,\qquad U_*\chi_v=\chi_{v+1}.
\]
Its mass equals \(H\). In detail the ordinary estimate \(h(x)/x\le\kappa d_x\) on these nonperiodic unit sites and the grade antichain give summability. The original positive trace bound \(\rho_n(x)\le C h(x)\) for \(n\ge1\) and the fixed-positive-site limit \(\rho_n(x)\to h(x)\) then give
\[
 \int h\,d\mu_v=\lim_{n\to\infty}\int\rho_n\,d\mu_v
                 =\lim_{n\to\infty} Z_{v-n}=H.                         \tag{4}
\]
These pointwise facts concern the specified representative; an arbitrary choice on Haar-null points would be insufficient. [Valbuena, *A positive stationary envelope*, envelope theorem and integer corollary](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/positive-stationary-envelope.tex) · [Weaver, *Ternary harmonic moments and Collatz orbit occupation*, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1) · [Ordinary trace and natural predecessor comparison](../../astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md).

Bounded continuous functions \(h_j\uparrow h\) exist by lower semicontinuity on the compact metric group. Since the local marginal tends to \(HM\),
\[
 \lim_{v\to-\infty}\int(h-h_j)\,d\mu_v=H\big(1-\int h_j\,dm_3\big)
 \longrightarrow0\qquad(j\to\infty).                                    \tag{5}
\]
Consequently weighting any marked cluster law by \(h\) commutes with taking its limit. The normalized \(F\)-law of \(\chi_v\) increases in stochastic order as \(v\) increases, by (2) and its forward-flow identity. Its past limit exists on the compact interval. By (3) and (5) the \(F\)-marginal of every unweighted cluster equals this same canonical probability; this defines \(\lambda_C\) and proves (1). The \(h\)-weighted local marginal in this conclusion is \(H m_2\otimes(hm_3)\).

Every forward path from a point in a fixed grade agrees eventually with the component ray, so under \(\chi_v/H\) the future \(F\)-law converges to \(\delta_1\). This follows by pushing forward any one fixed probability under the deterministic map and using \(F(U^j x)\to1\) on its atoms. For every continuous \(G\), the telescoping identity holds with the outer sum in the order of physical grades,
\[
 H\left[G(1)-\int G(f)\,d\lambda_C(f)\right]
 =\sum_{v\in\mathbb Z}\sum_{g(x)=v}\frac{h(x)}{P(x)}
                   [G(F(Ux))-G(F(x))].                                 \tag{6}
\]
The outer series converges by its two endpoint limits and converges absolutely for monotone or Lipschitz \(G\). In particular
\[
 H\int(1-f)\,d\lambda_C(f)=\frac13\sum_{x\in C}\frac{h(x)}{P(x)^2},
 \qquad H\int f^{-1}\,d\lambda_C(f)=\kappa d_C^{\rm ord}.                \tag{7}
\]
For the second identity \(h(x)P(x)^{-1}(F(x)^{-1}-F(Ux)^{-1})=h(x)/[x(3x+1)]\), and the earlier component budget identifies the sum as \(\kappa d_C^{\rm ord}-H\). These identities constrain the real phase and distinguish the real factor from both local Haar marginals. They allow the nonzero entering mass of a hypothetical component.
