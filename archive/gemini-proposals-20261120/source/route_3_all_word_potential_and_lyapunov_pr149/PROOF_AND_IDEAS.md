# Route 3: Fractional-Moment ($L^\alpha$) & $\log$-Foster–Lyapunov Potentials for Unsafe Transport

**Aligned Baseline:** [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) (all-word potential $W = \sup(8k - 5A)$, Haar tail vs. pointwise escape, quantified log-log growth, rational cycles), Issue #89 (`Astra: critical-mass and survivor-fiber attack`), [research/open-obligations](https://github.com/GettysburgResearch/collatz/tree/main/research/open-obligations) (#3 survivor-specific transfer & #4 unsafe transport / first-moment explosion).  
**Status:** Exact Cramér–Chernoff window $\alpha \in (0, 1)$ and finite-state Markov transfer spectral-radius contraction $\rho(M_\alpha) < 1$ are **PROVEN & VERIFIED** (`verify_lyapunov_potential.py`); lifting spectral contraction from Haar/Markov measures to pointwise positive integers remains **OPEN**.

---

## 1. Diagnosis: Why Unsafe First-Moment Explosion Happens

In [research/open-obligations](https://github.com/GettysburgResearch/collatz/tree/main/research/open-obligations) (#4), safe contraction leaves a retained resonance/unsafe process that suffers from **unsafe first-moment explosion**. There is an exact algebraic reason why $L^1$ (linear height $V(x) = x$) fails on the shortcut map $T$:

For a random parity bit (Haar measure on $\mathbb{Z}_2$), a single shortcut step multiplies $x$ asymptotically by $1/2$ (even, prob $1/2$) or $3/2$ (odd, prob $1/2$). The $L^\alpha$ one-step moment generating function is:
$$\Lambda(\alpha) = \frac{1}{2} \left( 2^{-\alpha} + \left(\frac{3}{2}\right)^\alpha \right).$$

Evaluate $\Lambda(\alpha)$ at $\alpha = 1$:
$$\Lambda(1) = \frac{1}{2}\left(\frac{1}{2} + \frac{3}{2}\right) = 1.$$

**$L^1$ sits on the exact critical boundary $\Lambda(1) = 1$!** Any conditioning on a "retained unsafe / non-descending" set tilts the parity probability slightly toward odd steps ($p_{\text{odd}} > 1/2$), immediately pushing the first-moment multiplier above $1$ and causing exponential explosion of $\mathbb{E}[x]$ on re-entry!

---

## 2. Established Local Lemmas (Verified in `verify_lyapunov_potential.py`)

### Lemma 3.1 (Exact Strict-Contraction Window for $V_\alpha(x) = x^\alpha$)
$\Lambda(\alpha)$ is strictly convex on $\mathbb{R}$, with $\Lambda(0) = 1$, $\Lambda'(0) = \frac{1}{2}\ln(3/4) < 0$, and $\Lambda(1) = 1$. Therefore:
1. $\Lambda(\alpha) < 1$ on the **exact open interval $\alpha \in (0, 1)$**.
2. The unique minimum is achieved at $\alpha_{\min} = \frac{\ln(\ln 2 / \ln(3/2))}{\ln 3} \approx 0.488077$, where $\Lambda(\alpha_{\min}) \approx 0.965907 < 1$.
3. At the clean rational exponent $\alpha = 1/2$:
   $$\Lambda(1/2) = \frac{1 + \sqrt{3}}{2\sqrt{2}} \approx 0.965926 < 1.$$
4. **Consequence for Unsafe Re-Entry Tilt:** Even if an unsafe/resonance conditioning tilts the odd-step probability from $1/2$ up to $p = 0.55$, at $\alpha = 1/2$ the tilted multiplier is:
   $$(1-p)2^{-1/2} + p(3/2)^{1/2} \approx 0.991808 < 1,$$
   whereas at $\alpha = 1$ the same tilt gives $0.45(0.5) + 0.55(1.5) = 1.05 > 1$ (exponential explosion!).

### Lemma 3.2 (Exact Finite-State Markov Transfer Contraction on $\mathbb{Z}/2^m\mathbb{Z}$)
Let $M_\alpha^{(m)}$ be the $2^m \times 2^m$ weighted transition matrix on $\mathbb{Z}/2^m\mathbb{Z}$ where each residue $r \pmod{2^m}$ transitions with probability $1/2$ to each of its two lifts $r_0, r_1 \pmod{2^m}$ under $T$, weighted by $2^{-\alpha}$ if $r$ is even and $(3/2)^\alpha$ if $r$ is odd.
* For every $m \ge 1$ and every $\alpha \in (0, 1)$, the spectral radius satisfies $\rho(M_\alpha^{(m)}) = \Lambda(\alpha) < 1$ (e.g., $\approx 0.965926$ at $\alpha = 1/2$).
* For the **killed** operator $K_{1/2}^{(m)}$ (deleting residue classes that certify immediate descent $T^s(x) < x$ within horizon $m$), $\rho(K_{1/2}^{(m)}) \approx 0.612372 < 0.965926 < 1$ across $m = 3, \dots, 7$, giving an explicit exponential decay rate for the surviving unsafe fiber mass in $L^{1/2}$!

---

## 3. Research Attack Blueprints (Bridging to Pointwise Control)

### Idea 3A: Swap $L^1$ for $L^{1/2}$ (or $L^{\alpha_{\min}}$) in `open-obligations` #4
* Replace the first-moment energy in the unsafe-transport / renewal inequality with $V(x) = x^{1/2}$.
* Because $\Lambda(1/2) = \frac{1+\sqrt{3}}{2\sqrt{2}} \approx 0.965926$, the operator has a **3.4% spectral gap buffer** that absorbs moderate resonance tilt on unsafe re-entry without exploding.
* **Exact Sub-Task for the Agent:** Re-run the repository's existing fresh-shell and transported-distribution counterexamples (referenced in `open-obligations` #4) under $V(x) = x^{1/2}$ and $V(x) = \log(1+x)$ to test which counterexamples survive and which collapse.

### Idea 3B: Foster–Lyapunov Drift + Return-Time Tails on $\log x$
* For the additive potential $\Phi(x) = \log_2 x$, one step changes $\Phi$ by $-1$ (even) or $+\log_2(3/2) \approx +0.585$ (odd), with mean drift $\mu = \frac{1}{2}(-1 + \log_2(3/2)) \approx -0.2075 < 0$.
* Pair $\Phi(x)$ with a finite-state parity-word automaton $\mathcal{A}_m$ on $\mathbb{Z}/2^m\mathbb{Z}$ and define a **killed return-time potential** $U(x, s) = \Phi(x) + \psi(s)$ where $\psi(s)$ solves the Poisson equation on the safe automaton states.
* **Connection to PR #149:** PR #149's noninteger rational cycles (which match arbitrary finite binary/ternary observations above any real floor) prove that **no purely $2$-adic / finite-horizon Markov potential can rule out all cycles without an integrality constraint**. Therefore, any pointwise closure from $V_\alpha$ or $\Phi$ must inject integrality (either via Route 4's Diophantine denominator lower bounds $D = 2^j - 3^q \mid A_w$, or via Route 1/5's merger reductions).
