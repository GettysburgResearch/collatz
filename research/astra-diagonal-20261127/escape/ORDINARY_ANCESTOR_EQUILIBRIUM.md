# Individual-depth equilibrium for the actual ancestors of each positive integer

Write \(M=m_2\otimes m_3\) for normalized odd binary Haar times full ternary Haar. For a positive odd target \(a\), let \(e_i(x)\) be the actual odd valuation sequence and \(S_n(x)\) its first-\(n\) sum. The ordinary inverse law has unnormalized word weight \(\omega_n(x)=3^n2^{-S_n(x)}\). For every such fixed \(a\),
\[
     \sum_{U^n x=a}\omega_n(x)\delta_{(x_2,x_3)}\ \Rightarrow\ h(a)M.
                                                                            \tag{1}
\]
The sum is over all actual positive odd ancestors, including terminal multiples of three. The result is an individual-depth limit on the original measure. For a unit target its normalization by \(\rho_n(a)\) gives a probability converging weakly to \(M\). For a nonunit target there are no positive-depth words and \(h(a)=0\).

For a unit \(a\), also attach the real affine inverse-word intercept \(R_n=a-\omega_n(x)x\). If \(\sigma_a\) is the canonical real fibre at that positive integer, then
\[
 \frac1{\rho_n(a)}\sum_{U^nx=a}\omega_n(x)\delta_{(x_2,x_3,R_n)}
                    \ \Rightarrow\ M\otimes\sigma_a .                       \tag{2}
\]
The real mark here uses the original finite prefix, while both local coordinates record the same terminal integer. The earlier word/fibre theorem shows \(\sigma_a\) is singular continuous and exact-dimensional of dimension one under its named counted-synchronization input. Thus (2) distinguishes the singular real coordinate from its two independent Haar local coordinates. [Fixed-root real fibre and its cited hypotheses](../../astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md) · [Weaver, joint law, §9.2](https://rstation.ai/problems/collatz/papers/19).

## Proof with original weights

The measure in (1) is exactly \((\widehat L^*)^n\delta_{(a,a)}\). Its mass \(\rho_n(a)\) tends to the finite \(h(a)\) by Weaver 176, Theorem 2. Any translated subsequential limits at all offsets have constant mass \(h(a)\) and obey the inverse entrance recursion. The [product-Haar entrance theorem](FIRST_POWER_HAAR.md) identifies them with \(h(a)M\). This proves (1). [Weaver, *Ternary harmonic moments and Collatz orbit occupation*, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1).

For (2), fix a finite outward prefix \(w\) of length \(t\) from the true root \(a\) and write \(b=I_w(a)\) for its ordinary terminal and \(\omega_w=3^t2^{-S_w}\). Its unnormalized endpoint measure for the remaining \(n-t\) steps equals \(\omega_w(\widehat L^*)^{n-t}\delta_{(b,b)}\). Thus (1) gives limiting measure \(\omega_w h(b)M\). Dividing by \(h(a)>0\) gives the canonical prefix probability, by harmonicity \(Lh=h\). All these probabilities sum to one at a fixed length \(t\). Since prefix lengths are fixed and the words form a countable discrete set, convergence on every prefix and conservation of total mass give uniform tightness over prefixes. In particular the joint law of \((x_2,x_3,R_t)\) converges to the product of \(M\) with the canonical law of \(R_t\).

It remains to check the growth in \(t\) of the *original finite* mark. Under the original depth-\(n\) law, the first \(n-1\) inverse letters have Radon–Nikodym derivative
\[
 \frac{h(a)}{\rho_n(a)}\frac{\rho_1(X_{n-1})}{h(X_{n-1})}
\]
against the canonical path law at \(a\). The ratio is uniformly bounded for all large \(n\), because \(0\le\rho_1\le2\) and \(h\) is bounded below at units. Histories ending at nonunits at time \(n-1\) have no possible last letter. This truncation by one step preserves the nonunit leaves at the true terminal time. Write \(\omega_j=3^j2^{-S_j}\) along outward letters. Under the canonical law \(R_j\uparrow R_\infty\le a\), \(\omega_j\to0\) almost surely by the canonical mean of two divisions per step, and the law of \(R_\infty\) is \(\sigma_a\). In the original law the additional last intercept is at most \(\omega_{n-1}/2\). Thus for each \(\epsilon>0\),
\[
 \lim_{t\to\infty}\limsup_{n\to\infty}
  \Pr_{a,n}(R_n-R_t>\epsilon)=0 .                                         \tag{3}
\]
Indeed bound the event by the union of \(R_{n-1}-R_t>\epsilon/2\) and \(\omega_{n-1}>\epsilon\) in the uniformly dominated canonical histories. Uniform continuity on the compact product then passes the finite-prefix result to (2). [Canonical inverse path law and its clock theorem](../../astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

## The same depth scale at a moving ordinary target

Let \(a_j=U^j a_0\) lie on an ordinary escaping ray. For depths \(n_j\) with \(n_j-j\to+\infty\),
\[
 \frac1{\rho_{n_j}(a_j)}\sum_{U^{n_j}x=a_j}\omega_{n_j}(x)
                  \delta_{(x_2,x_3,\,1-R_{n_j}/a_j)}
        \ \Rightarrow\ M\otimes\lambda_C.                                  \tag{4}
\]
In the proof, the original weight at the target equals \(P(a_j)/P(x)\). All its sources have grade \(v_j=j-n_j\); by the [uniform physical trace profile](../../astra-unconventional-20261126/boundary/TRACE_PROFILE.md), the omitted mass in that grade in weights \(1/P(x)\) tends to zero uniformly in \(n_j\). Both the full mass and the included mass tend to \(H_C>0\). The real coordinate \(1-R_{n_j}/a_j=(P(a_j)/a_j)F(x)\) differs uniformly from \(F(x)\) by \(o(1)\). Apply [the marked past-grade theorem](CORRECTED_PHASE.md). In its canonical path construction \(\lambda_C\) is exactly the law of the full path product \(J=\prod_{v\in\mathbb Z}3Z_v/(3Z_v+1)\), already described by the [moving fibre theorem](../../astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md). Indeed \(F(Z_v)=\prod_{u\ge v}3Z_u/(3Z_u+1)\) decreases to \(J\) as \(v\to-\infty\). Thus the singular continuous, dimension-one real component law in (4) has the prior geometric identification as well.

At each fixed \(v=j-n_j\), the same omitted-mass bound yields convergence in total variation before the real rescaling to the atomic normalized full grade in weights \(1/P(x)\), provided \(Z_v>0\). In particular this holds at \(n_j=j\), where the fixed seed retains positive posterior mass. Formula (4) holds with any positive overshoot tending to infinity, however slowly. Weak convergence of these countably supported measures to Haar does not hold in total variation, and passage from this long-depth result to the finite grade at zero would change the source measure.
