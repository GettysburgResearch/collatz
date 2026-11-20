# GettysburgResearch/collatz — Full-Completion Research Blueprints (v2)

**Date:** 2026-11-20  
**Target Repository:** [GettysburgResearch/collatz](https://github.com/GettysburgResearch/collatz)  
**Deep-Dive Baseline:** Direct response to the exact closure boundaries proved in [PR #146](https://github.com/GettysburgResearch/collatz/pull/146) (`THREE_RAY.md`, `EVENTUAL_FIVE_RAY.md`), [PR #147](https://github.com/GettysburgResearch/collatz/pull/147), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148), and [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) (`PROOF.md`, `CLOSURE_BOUNDARY.md`, `LOGLOG_GROWTH.md`, `RATIONAL_CYCLES.md`).

---

## Why Incremental Hill Climbs Cannot Close Collatz

Reading PRs #146–#149 in full exposes **three hard structural walls** that no parameter tightening (e.g., pushing the inverse compiler slope from $25/12 \to 23/12$, or checking deeper mod-$2^m$ trees) can cross by itself:

1. **The $2$-adic/$3$-adic vs. Integrality Wall (PR #149 `RATIONAL_CYCLES.md`):** Because positive rational cycles with reduced denominator $D_{\mathrm{red}} > 1$ coprime to $6$ exist in *every* $2$-adic/$3$-adic neighborhood above *any* real floor with $W(r) = \infty$, **no purely local $2$-adic/$3$-adic or finite-horizon potential can ever prove Collatz.** A full completion *must* inject global integrality ($\mathbb{Z} \hookrightarrow \mathbb{R} \times \prod_p \mathbb{Z}_p$).
2. **The Measure-Zero / Basin-Only Wall (PR #149 `CLOSURE_BOUNDARY.md`):** Haar-a.e. finiteness of $W$ and single-policy inverse compilers only control the connected component $\mathcal{B}$ of $1$ (and leave a dense $G_\delta$ exceptional set $E = \{W = \infty\}$). A full completion *must* include a **rigidity / amplification mechanism** that forces any hypothetical disjoint component $K \neq \mathcal{B}$ to collide with $\mathcal{B}$ or violate a global analytic/spectral law.
3. **The $L^1$ / First-Moment Wall (`open-obligations` #4):** Linear height sits on the exact critical boundary $\Lambda(1) = \frac{1}{2}(1/2 + 3/2) = 1$.

---

## Four Full-Completion Architectures (Beyond Hill Climbing)

| Blueprint Directory | Paradigm Shift | Exact Wall Attacked | Verified Local Theorems & Scripts |
| :--- | :--- | :--- | :--- |
| `blueprint_1_mahler_generating_function/` | **Complex Analysis / Mahler Functional Equation + Boolean Parseval** | Injects global integrality & $\{0,1\}$ rigidity simultaneously via $F(z) = \sum f(n)z^n$. | Exact $(w^2 \leftrightarrow w^3)$ functional equation, Pólya–Carlson natural-boundary exclusion of rational $F$, exact Boolean Parseval identity $\|F_r\|_{L^2}^2 = F(r^2)$ (`verify_mahler_functional.py`). |
| `blueprint_2_dirichlet_ruelle_singularity/` | **Dirichlet Series $D_f(s)$ & Collatz–Ruelle Transfer Operator $\mathcal{L}_s$** | Turns a rogue component $K$ into a Landau real singularity at $\sigma_c \in [0.84, 0.95]$ and couples it to $\mathcal{L}_s$. | Exact binomial-shift Dirichlet identity, forced residue-class bias $(2/3)^{\sigma_c}(1-2^{-\sigma_c}) < 1/3$, strict monotonicity $\rho(\mathcal{L}_s) > 1$ for $s < 1$ (`verify_dirichlet_ruelle.py`). |
| `blueprint_3_krasikov_lagarias_exponent_crossing/` | **Two-Sided Exponent Crossing ($\gamma_{\text{back}} > \gamma_{\text{surv}}$) + PR #146 Boundary Amplification** | Crosses the tiny $0.84$ vs. $0.901$ exponent gap and amplifies PR #146's $B(X)/\log X \to \infty$ to polynomial scale. | Krasikov–Lagarias difference-inequality LP prototype on $(\mathbb{Z}/3^r\mathbb{Z})^\times$, exact polynomial boundary-vs-invariance dichotomy for PR #146 (`verify_exponent_crossing.py`). |
| `blueprint_4_adelic_w1_and_rational_cycle_separation/` | **Adelic / $S$-Unit Height & Corvaja–Zannier Subspace Attack on PR #149's $W(1) < \infty$** | Breaks PR #149's `RATIONAL_CYCLES.md` obstruction by coupling $8k - 5A$ to $D_{\mathrm{red}}(r)$ and the $S$-unit equation $3^k y + C_w = 2^A$. | Exact positivity ceiling $8k - 5A \le \delta k + 5\log_2 z - 5\log_2(4/3)$, explicit rational-cycle denominator separation, $S$-unit formulation of $W_{\mathrm{pos}}(1)$ (`verify_adelic_w1.py`). |

---

## Explicit Non-Claim Notice

In strict accordance with [GettysburgResearch/collatz](https://github.com/GettysburgResearch/collatz): **this archive does NOT claim a completed proof of the Collatz conjecture.** Each blueprint establishes exact, machine-verified local identities and isolates the single decisive global theorem (e.g., Mahler–Parseval rigidity, Dirichlet forcing-term cancellation, $\gamma_{\text{back}} > \gamma_{\text{surv}}$ crossing, or $S$-unit finiteness of $W_{\mathrm{pos}}(1)$) whose proof would settle Collatz completely.

Run all verifiers and generate the SHA-256 receipt with:

```bash
python3 -X utf8 -B run_all_v2_verifiers.py
```
