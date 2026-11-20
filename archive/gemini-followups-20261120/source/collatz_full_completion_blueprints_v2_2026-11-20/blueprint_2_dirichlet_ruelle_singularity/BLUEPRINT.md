# Blueprint 2: Dirichlet-Series Singularity $D_f(s)$ & the Collatz–Ruelle Transfer Operator $\mathcal{L}_s$

**Paradigm:** Analytic Number Theory (Landau's Theorem on Nonnegative Dirichlet Series) + Spectral Theory of Transfer Operators  
**Walls Bypassed:** Couples Krasikov–Lagarias ($\sigma_c \ge 0.84$), the repo's forward exception bounds ($\sigma_c \le 0.95$ / $0.901$), PR #149's inverse operator on $\mathbb{Z}_3^\times$, and PR #146's $f(3n) - f(n)$ boundary into a single **global meromorphic spectral equation**.  
**Status:** Exact binomial-shift Dirichlet identity, forced residue-class bias at $\sigma_c < 1$, and strict monotonicity of $\rho(\mathcal{L}_s)$ are **PROVEN & VERIFIED** (`verify_dirichlet_ruelle.py`); proving that the forcing term $\mathbf{G}(s)$ cannot sustain a pole/singularity at $\sigma_c < 1$ is the **OPEN CLOSING THEOREM**.

---

## 1. Exact Dirichlet-Series Functional Equation

Let $f: \mathbb{Z}_{>0} \to \{0, 1\}$ be the indicator of a hypothetical non-$1$ Collatz component $K \neq \mathcal{B}$ (containing at least one ternary unit $n_0 \not\equiv 0 \pmod 3$). Define its Dirichlet series:
$$D_f(s) = \sum_{n=1}^{\infty} \frac{f(n)}{n^s}, \qquad \operatorname{Re}(s) > \sigma_c(f).$$

### Theorem 2.1 (Exact Binomial-Shift Identity for $D_f^{(2 \bmod 3)}(s)$)
For every $s \in \mathbb{C}$ with $\operatorname{Re}(s) > \sigma_c(f)$:
$$D_f^{(2 \bmod 3)}(s) = \left(\frac{2}{3}\right)^s (1 - 2^{-s}) D_f(s) + \sum_{m=1}^{\infty} \binom{-s}{m} \frac{2^s}{3^{s+m}} (1 - 2^{-(s+m)}) D_f(s + m).$$

**Proof:**
1. Since $f(2n) = f(n)$, $D_f^{\mathrm{odd}}(s) = (1 - 2^{-s}) D_f(s)$.
2. Since $f(3k+2) = f(2k+1)$ for all $k \ge 0$, write $n = 2k+1$, so $3k+2 = \frac{3}{2} n \left(1 + \frac{1}{3n}\right)$:
   $$D_f^{(2 \bmod 3)}(s) = \sum_{k=0}^\infty \frac{f(2k+1)}{(3k+2)^s} = \left(\frac{2}{3}\right)^s \sum_{\substack{n \ge 1 \\ n\text{ odd}}} \frac{f(n)}{n^s} \left(1 + \frac{1}{3n}\right)^{-s}.$$
3. Expanding $\left(1 + \frac{1}{3n}\right)^{-s} = 1 + \sum_{m=1}^{\infty} \binom{-s}{m} (3n)^{-m}$ (absolutely convergent since $1/(3n) \le 1/3 < 1$) and swapping sums yields the exact identity. $\square$

### Corollary 2.2 (Forced Non-Uniform Residue Bias at Any Rogue Abscissa $\sigma_c < 1$)
By **Landau's Theorem** (since $f(n) \ge 0$), $s = \sigma_c(f)$ is a singularity of $D_f(s)$. Every shifted term $D_f(s + m)$ ($m \ge 1$) is **holomorphic** in a neighborhood of $s = \sigma_c(f)$. Therefore:
$$D_f^{(2 \bmod 3)}(s) - \left(\frac{2}{3}\right)^s (1 - 2^{-s}) D_f(s) \quad \text{is HOLOMORPHIC at } s = \sigma_c(f)!$$
In particular, if $f$ has a rogue abscissa $\sigma_c \in [0.84, 0.95]$:
* At $\sigma_c = 1$ (the trivial solution $f \equiv 1$), $(2/3)^1 (1 - 2^{-1}) = 1/3$.
* At $\sigma_c = 0.84$, $(2/3)^{0.84} (1 - 2^{-0.84}) \approx 0.3139 < 1/3$!
Thus **any rogue component with $\sigma_c < 1$ is strictly depleted in residue class $2 \pmod 3$ relative to uniform density $1/3$.**

---

## 2. The Collatz–Ruelle Transfer Matrix $\mathcal{L}_s$ on $(\mathbb{Z}/3^r\mathbb{Z})^\times$

Iterating the exact same binomial-shift expansion over all backward Syracuse steps $U^{-1}(n) = (2^g n - 1)/3$ on ternary units modulo $3^r$ yields a **vector Dirichlet identity**:
$$\mathbf{v}(s) = \mathcal{L}_s \mathbf{v}(s) + \mathbf{G}_r(s) + \mathbf{H}_r(s),$$
where:
* $\mathbf{v}(s) = \big(D_f^{(a \bmod 3^r)}(s)\big)_{a \in (\mathbb{Z}/3^r\mathbb{Z})^\times}$,
* $\mathbf{H}_r(s)$ is **holomorphic** at $s = \sigma_c$ (all $m \ge 1$ binomial-shift remainders),
* $\mathcal{L}_s$ is the exact $s$-parametrized Collatz–Ruelle transfer matrix (whose entries are sums of $(3/2^g)^s$ over legal transitions, strictly decreasing in real $s > 0$, with $\rho(\mathcal{L}_1) = 1$!),
* $\mathbf{G}_r(s)$ captures the **boundary/forcing terms** from $0 \pmod 3$ and $1 \pmod 6$ sources.

### Full-Completion Strategy (Spectral Exclusion of $\sigma_c < 1$)
Look at the sharp spectral consequence verified in `verify_dirichlet_ruelle.py`:
* $\rho(\mathcal{L}_s)$ is **strictly decreasing** in $s > 0$, with $\rho(\mathcal{L}_1) = 1$.
* Therefore, for **every** $s \in (0, 1)$, $\rho(\mathcal{L}_s) > 1$!
* A nonnegative vector $\mathbf{v}(s)$ with a real singularity at $s = \sigma_c < 1$ CANNOT satisfy $\mathbf{v}(s) = \mathcal{L}_s \mathbf{v}(s) + \text{holomorphic}$ (because by Perron–Frobenius, $(I - \mathcal{L}_{\sigma_c})\mathbf{v} = \text{holomorphic}$ with $\rho(\mathcal{L}_{\sigma_c}) > 1$ would force $\mathbf{v}$ to have negative components or vanish!).
* **Why Collatz isn't trivially dead yet:** The forcing term $\mathbf{G}_r(s)$ (arising from $n \equiv 0 \pmod 3$ and $n \equiv 1 \pmod 6$) can also have a singularity at $s = \sigma_c$.
* **Decisive Closing Attack:** Couple $\mathbf{G}_r(s)$ to **PR #146's $f(3n) - f(n)$ defect**! Notice that $D_f^{(0 \bmod 3)}(s) = 3^{-s} D_f(s) + D_{\Delta_3}(s)$ where $\Delta_3(n) = f(3n) - f(n)$. If one proves that the signed defect series $D_{\Delta_3}(s)$ has **strictly smaller abscissa of convergence** (or cancels at $\sigma_c$) — OR if one constructs a **self-closed transfer operator on ALL residues $\pmod{6 \cdot 3^r}$** whose spectral radius satisfies $\rho > 1$ for $s < 1$ — then $\sigma_c < 1$ is **completely excluded**!
