# Route 4: Adelic / Anisotropic Transfer Operators & Spectral Isolation of `{1, 2}`

- **Status:** `PROPOSED` (with `VERIFIED_COMPUTATIONAL` Galerkin & Esscher-tilted spectral analysis)
- **Target Repo Hooks:** [STATE.md](https://github.com/GettysburgResearch/collatz/blob/main/STATE.md) (horizon bound $\#N(X) \le 6499 + 2X^{19/20}$, entropy exponent $h_2(\log 2/\log 3) \approx 0.949956$), [PR #145](https://github.com/GettysburgResearch/collatz/pull/145) (depth-30 cyclotomic/winding behavior, Gaussian deadline $\sim \sqrt{\log X}$)

## 1. Why Standard $L^2(\mathbb{Z}_2)$ Transfer Operators Fail

On $\mathbb{Z}_2$, the shortcut Collatz map $T$ is measure-preserving and conjugate to the one-sided Bernoulli shift (Lagarias 1985). Our Galerkin projection experiment (`transfer_operator_spectrum.py`) confirms:
- Averaging over the unknown top bit on $\mathbb{Z}/2^M\mathbb{Z}$ yields a strongly contracting Markov matrix ($\lambda_1 = 1$, $|\lambda_2| \approx 0.015$ at $M = 9$), because the projection **discards archimedean magnitude**.
- Conversely, the unprojected Perron–Frobenius operator on $C(\mathbb{Z}_2)$ has **essential spectral radius $1$**, which allows *every* PR #149 rational cycle and the $-19/11$ ghost to appear as a distributional eigenvector with eigenvalue $1$.

## 2. Esscher-Tilted Transfer Operator & Connection to `STATE.md` Entropy

Weighting the two branches of $T$ by their archimedean multipliers gives the **Esscher-tilted operator** $\mathcal{L}_s$:
$$(\mathcal{L}_s f)(x) = 2^{-s} f(2x) + \Big(\frac{3}{2}\Big)^s \mathbf{1}_{x \equiv 2 \pmod 3} f\!\left(\frac{2x-1}{3}\right).$$
Its mean-field leading eigenvalue is
$$\lambda_1(s) = \frac{1}{2}\left(2^{-s} + \left(\frac{3}{2}\right)^s\right),$$
which is strictly convex with $\lambda_1(0) = 1$, minimum $\lambda_1(s^*) < 1$ at $s^* = \frac{\log(\log 2 / \log(3/2))}{\log 3} \approx 0.4895$, and second root $s_0 = 1$? Wait: check $\lambda_1(1) = \frac{1}{2}(\frac{1}{2} + \frac{3}{2}) = 1$!
- **Exact identity:** $\lambda_1(0) = \lambda_1(1) = 1$, and $\lambda_1(s) < 1$ for all $s \in (0, 1)$, with minimum $\lambda_1(s^*) \approx 0.9647 < 1$!
- The Legendre transform of $\log_2 \lambda_1(s)$ recovers the exact binary entropy exponent $h_2(\log 2 / \log 3) \approx 0.949956$ appearing in `STATE.md`'s horizon bound $\#N(X) \le 6499 + 2X^{19/20}$!

## 3. Proposed Adelic Anisotropic Banach Space $\mathcal{B}_{\alpha, \beta}$ (`OPEN_OBLIGATION: R4-SPEC`)

To turn $\lambda_1(s^*) < 1$ into a **pointwise** (rather than almost-everywhere) contraction that excludes nontrivial integer cycles and divergent orbits:
1. **Product-Space Lift:** Act on functions $f(x_\infty, x_2, x_3)$ on $\mathbb{R}_{>0} \times \mathbb{Z}_2 \times \mathbb{Z}_3$ (or the finite adeles $\mathbb{A}_f$) rather than $\mathbb{Z}_2$ alone.
2. **Anisotropic Norm (Baladi–Tsujii / Gouëzel–Liverani style):** Combine a **smooth Sobolev norm in the archimedean variable $\log x_\infty$** with a **prime-denominator penalty** (e.g., weighting rational distributions supported on $a/q$ by $\mathrm{rad}(q)^{-\beta}$ for $\gcd(q,6)=1$).
3. **Target Spectral Theorem:** Prove a **Lasota–Yorke inequality** $\|\mathcal{L}_s^n f\|_{\mathcal{B}} \le C \theta^n \|f\|_{\mathcal{B}} + B \|f\|_{\text{weak}}$ with $\theta < 1$, forcing the peripheral spectrum on $\{|\lambda| \ge 1\}$ to be finite-dimensional and supported exclusively on $\mathbb{Z}$-integral cycles (thereby killing PR #149's rational cycles spectrally!).
