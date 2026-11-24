# Uniform dependence of the first-fusion moment on three initial profiles

**PROPOSED written theorem, conditional on the pair estimates and the uniform mixed-clock estimate identified below.** The fixed-triple subcritical moment and the two-gap potentials are due to PR197. To restart that argument on a growing collection selected by an earlier prefix, its implicit constant must be uniform in the entire new triple. This note gives that dependence.

Take three arms \(3^{a_i}n+c_i\), \(a_i\ge0\), \(c_i\in\mathbb Z\), on the fair binary parameter. The physical clock counts positive shortcut steps when the forms are realized on ordinary positive integers. Symbolic equality means equality of the two entire affine profiles in the unexposed quotient. For each pair order the forms by initial exponent, writing the upper as \(3^s z+D\) in terms of the lower \(z\), \(s\ge0\). At equal exponents either order yields the same \(|D|\). Put

\[
 A=\max_i a_i-\min_i a_i,\qquad
 Z_* =\max_{\rm pairs}|D|/3^s,\qquad
 Q=1+A^2+\log(2+Z_*).
\]

If \(\sigma\) is the first symbolic fusion of any two arms, then for every fixed \(0<p<3/2\),

\[
  \mathbb E(1+\sigma)^p\le C_p Q^p,\qquad
  \Pr(\sigma>h)\le C_p\min\{1,(Q/(1+h))^p\}.                 \tag{U1}
\]

The constant is independent of all six coefficients and of any common grade. An already fused pair gives \(\sigma=0\). All future uses of (U1) condition on the entire *one* parameter prefix before specifying the new coefficients. On that prefix each arm has slope \(3^{a_i+p_i}\) in the same remaining binary quotient. An odd change of parameter preserves the fair suffix. No independent future for different arms is needed.

## Inputs with their uniformity

* PR146 `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/THREE_RAY_UPPER.md`, pair transitions and boundary excursions, and `GROWING_ADDITIVE_GAPS.md`, (1). The remaining pair tail is bounded by \(C(1+s+\sqrt{\log(2+|D|/3^s)})/\sqrt{1+t}\) from each specified state. The scalar version of the same dependence is Lemma 2 of Lyapunov Weaver's [paper 124](https://rstation.ai/problems/collatz/papers/124).
* PR197 `9ab91d964b38fc870d1034bac628d62f59488467`, `research/ayh-resource-reset-20261124/joint-renewal/KILLED_GRADE_OCCUPATION.md`, (3), (5), `TRIPLE_FIRST_FUSION.md`, (2)–(5), and `TRIPLE_SUBCRITICAL_MOMENTS.md`, (3)–(11). The first two are used through the uniform occupation and elementary gap identities below. For the last, the coefficient-uniform interior covariance is obtained from [paper 13 v1, proof of Theorem 6, (21)](https://rstation.ai/problems/collatz/papers/13/v1), an **unconditioned** quota bound uniform over integer offsets and initial levels up to the specified maximum. The paper's result conditional on the length of an entire excursion would by itself be insufficient. The source identifies the scalar chain and underlying synchronization work of Said Duran and David Leen.

## Burn-in and a uniform reciprocal tail

It suffices to take \(p=1+\gamma/2\), \(0<\gamma<1\). Smaller moments follow by the power-mean inequality. Write \(P(t)=\Pr(\sigma>t)\), and use the killed indicator \(1_t=\mathbf1_{\sigma>t}\). Choose a dyadic \(H_0\) with

\[
   C_\gamma Q\le H_0<2 C_\gamma Q .                              \tag{U2}
\]

The fixed \(C_\gamma\) covers the universal thresholds below. In particular \(A\le\sqrt{H_0}\). The scalar bound gives \(P(t)\ll\sqrt{H_0}/\sqrt{1+t}\). For each pair put \(B_t=\mathbb E[\sqrt{|D_t|/3^{s_t}}\,1_t]\). Its update has \(B_{t+1}\le\rho B_t+P(t)\) with absolute \(\rho=(1/\sqrt2+\sqrt{3/2})/2<1\). Splitting the convolution in half gives for \(H\ge H_0\)

\[
 B_H\ll P(\lfloor H/2\rfloor)+e^{-cH}.
\]

Indeed \(\rho^H B_0\le e^{-cH}\) by (U2), and the earlier half of the convolution is bounded by a geometric tail. The all-state expected lifetime occupation at pair level \(\le K\) is \(O((1+K)^2+(1+K)(1+\sqrt{|D|/3^s}))\). Apply it at \(H\) to the three actual pair states on the triple-live event. If \(g_t\) is the smallest pair grade gap, then for every \(K\ge0\),

\[
 \sum_{t\ge H}\Pr(\sigma>t,\ g_t\le K)
 \ll (1+K)^2\{P(\lfloor H/2\rfloor)+e^{-cH}\}.                \tag{U3}
\]

Sort the grades at a clock, let \(u,v\) be their adjacent gaps, \(U=u+v\), and \(F=uv\). At strict order the killed product has nonpositive mean drift, because the two centered gap increments have product zero or minus one. At a tie its upward increment is at most \(1+U\). Initial signed pairwise grade differences have modulus at most \(A\) and centered increments of modulus at most one. Hence \(\mathbb EF_{H_0}\ll A^2+H_0\ll H_0\), by the second-moment bound for these martingales. This use of the unconditioned moment bounds the killed cost from above.

For dyadic \(H\ge H_0\), Azuma at each fixed \(t\in[H,2H)\) gives \(U_t\ll\sqrt{H\log(2H)}\) except with probability \(O(H^{-6})\). On the exceptional set \(U_t\le A+t\ll H\). From (U3) the total positive product drift in such a shell is at most

\[
 C\sqrt{H\log(2H)}\{P(\lfloor H/2\rfloor)+e^{-cH}\}+O(H^{-3}). \tag{U4}
\]

The scalar tail first yields \(\mathbb E[F_t1_t]\ll H_0(1+\log(2t))^{3/2}\) for \(t\ge H_0\), by summing (U4) over dyadic shells, including a partial last shell. In \([H,2H)\), the event \(g_t>K\) has \(F_t>K^2\). Use (U3) on its complement, divide the sum on the shell by \(H\), and use monotonicity of \(P\). With \(K=H^{3/8}\) this gives

\[
 P(t)\ll H_0(1+t)^{-3/4}(1+\log(2t))^{3/2}.                   \tag{U5}
\]

Dyadic monotonicity extends the bound to all \(t\ge 4H_0\). At smaller times the right side dominates an absolute constant. Substituting (U5) in (U4) now gives total positive drift \(O(H_0)\), since \(\sum_{H=2^k}H^{-1/4}(1+\log(2H))^2<\infty\). Thus \(\sup_{t\ge H_0}\mathbb E[F_t1_t]\ll H_0\). Repeat the small-gap split, this time with \(K=\lfloor\sqrt{\varepsilon H}\rfloor\) and fixed small \(\varepsilon>0\). For every dyadic \(H\ge H_0\),

\[
 P(2H)\le C H_0/H + P(H/2)/8.
\]

Here the coefficient of \(P(H/2)\) is \(O((1+K)^2/H)\), with an absolute constant by (U3). Increasing \(C_\gamma\) in (U2) handles the floor once and for all. Multiplying by \(2H\) leaves coefficient \(1/2\) on \((H/2)P(H/2)\). Start from the trivial bound for \(t\le2H_0\) and interpolate between dyadic endpoints to get

\[
                         P(t)\ll H_0/(1+t).                      \tag{U6}
\]

## Subcritical moment with the same initial scale

Set \(G=uvU^\gamma\), killed at fusion. Its expected value at \(H_0\) is \(O_\gamma(H_0^{1+\gamma/2})\) since \(G\le U^{2+\gamma}\) and integration of the three Azuma tails at \(H_0\), with \(A\le\sqrt{H_0}\), gives that unconditioned moment. Recheck the two estimates of the fixed-triple argument for \(H\ge H_0\).

1. Partition a dyadic shell into blocks of \(b=2^{\lfloor\log_2(H)/4\rfloor}\) clocks. If the triple is live at block start and both gaps exceed \(K_1b\) for a fixed large \(K_1\), then the order stays strict. Every pair's starting level is at most \(A+2H\le3H\). The two quotas \((1/2\pm\eta/4)b+O(1)\) in the uniform paper-13 estimate are attained before the pair could reach level one. Their elapsed times bracket the block except with probability \(o(1)\), uniformly since the log of the maximum initial level is \(O(\log H)\). Each pair therefore has expected mixed count \((1/2+O(\eta))b\). The mean accumulated covariance per step of the two ordered gaps is consequently within \(O(\eta)\) of the matrix with diagonal \(1/2\) and off-diagonal \(-1/4\). Applying half this matrix to the Hessian of \(G\) gives \((\gamma-1)(U^\gamma+\gamma uvU^{\gamma-2})/4\). The replacement of the Hessian by its block-start value and the discrete Taylor remainders cost at most \(C_\gamma bU_{\rm start}^\gamma(\eta+b/U_{\rm start})\), as in PR197 (7). Fix \(\eta,K_1,H_0\)'s absolute lower threshold in that order. Negative mean drift on the block then pays \(c_\gamma\sum U_t^\gamma\) in conditional expectation throughout it. All estimates depend on \(\gamma\) and the uniform inputs only.
2. In a live block starting outside that region, some pair gap stays \(\le (K_1+1)b\). At a strict step the positive mean drift is at most \(C_\gamma(1+U)^\gamma\), by the centered increments and the bounded Hessian. At a tie it is at most \((1+U)^{1+\gamma}\), as the next smallest gap is at most one. Include the cost \(U^\gamma\) at each such live clock. Apply the same concentration bound as in (U4) and (U3) first with \(K=(K_1+1)b\), then with \(K=0\) for the ties. Using (U6), the summed shell charge is

\[
 \ll_\gamma H_0 H^{(\gamma-1)/2}(1+\log(2H))^{(1+\gamma)/2}+O_\gamma(H^{-2}).
\]

This is summable in dyadic \(H\). Telescoping from \(H_0\), the nonnegative terminal potential and the initial bound give \(\sum_{t\ge H_0}\mathbb E[U_t^\gamma1_t]\ll_\gamma H_0^{1+\gamma/2}\). On \(t<H_0\) the unconditioned moments of \(U_t\) give the same bound for their total. For completeness, split each dyadic shell at \(U_t=\sqrt{\varepsilon H}\). Large spread pays \(H^{\gamma/2}1_t\) from this occupation. Small spread has \(g_t\le\sqrt{\varepsilon H}\), so (U3) costs at most \(C\varepsilon H^{1+\gamma/2}P(H/2)\) plus an exponentially decaying term. The displayed term is at most \(C'\varepsilon\) times the weighted survival sum over \([H/4,H/2]\), by monotonicity. Choose \(\varepsilon\) so small that these bounded-overlap charges can be absorbed in the sum up to any finite dyadic cutoff. The initial clocks through \(4H_0\) cost \(O_\gamma(H_0^{1+\gamma/2})\) simply using \(P\le1\). This proves

\[
 \sum_{t\ge0}(1+t)^{\gamma/2}P(t)\ll_\gamma H_0^{1+\gamma/2}.
\]

Tail summation, (U2), and Markov's inequality give (U1). The endpoint \(p=3/2\) would lose strict negative curvature and dyadic summability in this proof.
