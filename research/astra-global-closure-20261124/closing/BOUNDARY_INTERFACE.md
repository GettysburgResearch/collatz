# Rational-affine Poisson boundaries and the ordinary source

**Status: SOURCE-QUALIFIED application and elementary written comparison.**
This note applies a primary boundary-classification theorem to the independent
gap model, then checks what would be required to transfer it to the actual
ordinary inverse flow. It supplies neither an escape-exclusion theorem nor
an independence assertion for Collatz gaps.

## 1. The exact independent model

For an integer gap \(g\ge1\), set
\[
\phi_g(x)=\frac{3x+1}{2^g}.
\]
Let \(p\) be a probability law on the positive gaps, supported at two or more
distinct gaps, with finite mean \(b\). Distinct maps have distinct fixed
points \(1/(2^g-3)\), so the subgroup they generate is not abelian. The
logarithmic moment in Brofferio's theorem is finite because the contributions
from the slopes and translations are bounded by a constant times \(g+1\).
The local mean logarithmic slopes, with \(|p|_p=p^{-1}\), are
\[
\lambda_\infty=\log3-b\log2,\qquad
\lambda_2=b\log2,\qquad
\lambda_3=-\log3,\qquad
\lambda_\ell=0\quad(\ell\ne2,3).
\]

Brofferio's theorem identifies the Poisson boundary with the product of the
completions having negative drift, equipped with its unique joint stationary
probability. Therefore the boundary of this independent rational-affine walk is
\[
\begin{cases}
\mathbb Q_3,&b\le\log_2 3,\\
\mathbb R\times\mathbb Q_3,&b>\log_2 3.
\end{cases}
\]
The measure in the second line is a joint stationary measure; it is not
asserted to be the product of its marginals. In either case the boundary is
nontrivial, because the ternary drift is negative. Its bounded harmonic
functions therefore need not be constant.

For example, the geometric law with mean \(2\) has both a real and a ternary
boundary. At the critical mean \(\log_2 3\), the real factor is absent.
This matches the real-series obstruction already proved in PR #180:
the same stationary positive-gap process cannot have both mean at most
\(\log_2 3\) and an almost surely finite positive real coding series.
The theorem does not create such a real factor for the actual process.

Primary source: Sara Brofferio, *The Poisson boundary of random rational
affinities*, Annales de l'Institut Fourier **56** (2006), 499–515,
[main theorem, pages 500–501](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf).
The random increments in that theorem are independent and identically
distributed. A stationary dependent sequence of actual gaps does not satisfy
that assumption merely because its one-coordinate marginal is \(p\).

## 2. A quantitative obstruction to a root-by-root iid comparison

Retain the qualified ordinary harmonic flow from PR #185. On one injective
ordinary odd orbit \(q_j\), put
\[
\nu(q)=\sum_{Ux=q}\nu(x),\qquad
v_j=\nu(q_j)\uparrow C>0,\qquad
K(q,x)=\mathbf1_{Ux=q}\frac{\nu(x)}{\nu(q)}.
\]
The flow is positive and bounded on the states in question. For \(M,r\ge1\),
sample \(J\) uniformly from \(\{0,\ldots,M\}\), start at \(q_{J+r}\), and take
\(r\) inverse steps with \(K\). Let \(P_{M,r}\) be the joint law of \(J\) and
the reversed gap word. Compare it with
\[
Q_{M,r}=\operatorname{Unif}\{0,\ldots,M\}\otimes p^{\otimes r}.
\]
Let \(\rho=\sup_g p_g<1\), and let \(E\) be the event that the word exactly
retraces the actual segment from \(q_{J+r}\) to \(q_J\). The source theorem
gives
\[
P_{M,r}(E)=\frac1{M+1}\sum_{j=0}^M\frac{v_j}{v_{j+r}}
\ge1-\varepsilon_M,\qquad
\varepsilon_M=\frac1{M+1}\sum_{j=0}^M(1-v_j/C)\longrightarrow0.
\]
On the independent reference law, each prescribed length-\(r\) word has
probability at most \(\rho^r\), so \(Q_{M,r}(E)\le\rho^r\). It follows that
\[
\|P_{M,r}-Q_{M,r}\|_{\rm TV}
\ge 1-\varepsilon_M-\rho^r,
\]
where total variation is the supremum over events. Binary coarse-graining
and the bound on binary entropy also give
\[
D(P_{M,r}\Vert Q_{M,r})
\ge(1-\varepsilon_M)r\log(1/\rho)-\log2.
\]
If \(f=dP_{M,r}/dQ_{M,r}\) exists, Hölder's inequality on \(E\) gives, for
\(1<p\le\infty\),
\[
\|f\|_{L^p(Q_{M,r})}
\ge(1-\varepsilon_M)\rho^{-r(1-1/p)}.
\]
If absolute continuity fails, there is no finite density bound to begin with.
These estimates rule out a subexponential likelihood comparison in the
inverse depth for these **labelled path laws**.

The source-bound retracing identity is inherited, not a new discovery.
The displayed comparison with a fixed iid law is an immediate consequence
and is recorded to test a proposed use of random-affine boundary theory.
Sources: [PR #185, sections 1–3](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md)
and [PR #180, sections 2–3 and 9](https://github.com/GettysburgResearch/collatz/blob/7cfd911d35382d9d3bc988060ba88ade78a4267e/research/whole-source-20261123/COLLISION_CORE.md).

## 3. What this comparison does and does not decide

The root label is essential. Forgetting it can leave positive entropy in the
empirical distribution of the actual words. A deterministic sequence can
have iid finite-word frequencies, despite complete determinism conditional
on its time index. The estimates above therefore do not disprove iid
unlabelled subsequential gap limits, nor do they disprove comparison of a
specific projected endpoint law with a stationary boundary law. Such a
comparison would require its own proof.

The source theorem already identifies the actual moving inverse endpoint
law with the ordinary time law up to an error tending to zero, uniformly
in inverse depth. Its stationary backward-gap limits have mean at most
\(\log_2 3\), and their ternary collision dimension is strictly below the
stated critical exponent. A closing result would need an opposing estimate
for that same marginal, or finite real-series tightness for the same
stationary process. Brofferio's classification determines what happens
after independence and moment hypotheses have been established. It
supplies neither missing hypothesis for a fixed ordinary Collatz orbit.

This note is a written literature interface check. No new Lean
formalization of probability or Poisson boundaries is claimed.
