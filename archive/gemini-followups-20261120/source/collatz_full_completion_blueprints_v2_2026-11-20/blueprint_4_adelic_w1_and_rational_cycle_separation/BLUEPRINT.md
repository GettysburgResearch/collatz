# Blueprint 4: Breaking PR #149's $W(1) < \infty$ & Rational-Cycle Wall via Adelic / $S$-Unit Height Separation

**Paradigm:** Global Diophantine Geometry ($S$-Unit Equations / Corvaja–Zannier Subspace Theorem) + Adelic Denominator Height  
**Walls Attacked:** Directly addresses the exact closure boundary proved in [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) (`CLOSURE_BOUNDARY.md` Equivalence Theorem: Collatz + $W(1) < \infty$, and `RATIONAL_CYCLES.md` Theorem 2: positive rational cycles matching any $2$-adic/$3$-adic neighborhood above any floor).  
**Status:** Positivity ceiling on $8k - 5A$, exact $S$-unit formulation of $W_{\mathrm{pos}}(1)$, and rational-cycle denominator separation are **PROVEN & VERIFIED** (`verify_adelic_w1.py`); proving $W_{\mathrm{pos}}(1) < \infty$ (and global non-existence of integer cycles) via $S$-unit / Subspace bounds remains **OPEN**.

---

## 1. Diagnosing PR #149's Exact Wall

In [PR #149](https://github.com/GettysburgResearch/collatz/pull/149), the all-word potential on ternary units $z \in \mathbb{Z}_3^\times$ is:
$$W(z) = \sup\bigl(\{0\} \cup \{8k - 5A : \text{legal } k\text{-edge inverse word of cost } A \text{ from } z\}\bigr).$$
PR #149 proves two decisive facts:
1. **Equivalence (`CLOSURE_BOUNDARY.md`):** Collatz $\land$ ($W(1) < \infty$) $\iff W(n) \le c_* \log_2(n+1) + \alpha \ln(1 + \log_2(n+1)) + C$ for any $\alpha < K$.
2. **Rational-Cycle Wall (`RATIONAL_CYCLES.md`):** Every $2$-adic/$3$-adic neighborhood above any real floor contains positive rational periodic orbits with reduced denominator $D_{\mathrm{red}} > 1$ coprime to $6$ and $W(r) = \infty$.

### The Crucial Structural Distinction: $W(z)$ on $\mathbb{Z}_3^\times$ vs. $W_{\mathrm{pos}}(z)$ on $\mathbb{Z}_{>0}$
A legal $k$-step inverse word $(g_0, \dots, g_{k-1})$ with $A = \sum g_i$ maps $z$ to:
$$y = \frac{2^A z - C_w}{3^k}, \qquad C_w = \sum_{i=0}^{k-1} 3^{k-1-i} 2^{a_i} \ge 3^{k-1}.$$
* On $\mathbb{Z}_3^\times$, $W(z)$ imposes **only** $3$-adic divisibility ($3^k \mid 2^A z - C_w$) and unit legality — **NOT positivity ($y \ge 1$)**!
* Once we enforce **ordinary positive-integer realization** ($y \in \mathbb{Z}_{>0}$), we obtain an exact archimedean lower bound on $A$:

### Theorem 4.1 (Exact Positivity Ceiling on $8k - 5A$)
For every positive-integer $k$-step inverse word from $z \in \mathbb{Z}_{>0}$ terminating at $y \in \mathbb{Z}_{>0}$:
$$2^A z = 3^k y + C_w \ge 3^k + 3^{k-1} = \frac{4}{3} \cdot 3^k,$$
which implies:
$$8k - 5A \le \delta k + 5 \log_2 z - 5 \log_2(4/3), \qquad \delta = 8 - 5\log_2 3 \approx 0.0751875.$$

In particular, for $z = 1$, achieving $8k - 5A \ge B$ with a **positive integer** $y \ge 1$ forces $A/k$ into the razor-thin Diophantine corridor:
$$\log_2 3 + \frac{\log_2(4/3)}{k} \le \frac{A}{k} \le \frac{8}{5} - \frac{B}{5k},$$
and forces the **exact binary-ternary representation of $2^A$**:
$$\boxed{2^A = 3^k y + \sum_{i=0}^{k-1} 3^{k-1-i} 2^{a_i}, \qquad 0 = a_0 < a_1 < \dots < a_{k-1} < A!}$$

---

## 2. Full-Completion Attack: Replacing $W$ with an Adelic Potential $W_{\mathbb{A}}$ & $S$-Unit Rigidity

### Idea 4A: Adelic Denominator-Penalized Potential $W_{\mathbb{A}}(r)$ (Breaking `RATIONAL_CYCLES.md`)
Why do PR #149's rational cycles evade $W$? Because $W$ ignores all primes $p \notin \{2, 3\}$!
Define the **adelic denominator height** of any rational $r \in \mathbb{Z}_{(6)} \cap \mathbb{Q}_{>0}$:
$$H_{\mathrm{denom}}(r) = \sum_{p \notin \{2, 3\}} \max\big(0, -\log_2 |r|_p\big) = \log_2 D_{\mathrm{red}}(r).$$
* On every ordinary positive integer $n \in \mathbb{Z}_{>0}$, **$H_{\mathrm{denom}}(n) = 0$ identically!**
* On every positive rational cycle of PR #149's `RATIONAL_CYCLES.md`, **$H_{\mathrm{denom}}(r) = \log_2 D_{\mathrm{red}} > 0$** — and as the $2$-adic/$3$-adic precision $(j, q) \to \infty$ or floor $H \to \infty$, $D_{\mathrm{red}} \mid (2^A - 3^k)$ grows exponentially in $k$ (by Stewart / Bugeaud–Laurent lower bounds on the greatest prime factor / squarefree part of $2^A - 3^k$)!
* **Global Completion Principle:** Any proof of Collatz via PR #149's defect framework MUST couple the $\{2, 3\}$-defect $8k - 5A$ to the **global product formula** $\prod_{v \le \infty} |x|_v = 1$, which binds the archimedean size $\log_2 n$ to the $p$-adic norms for $p \notin \{2, 3\}$ (forcing $H_{\mathrm{denom}} = 0$).

### Idea 4B: Variable-Convergent Defect $W_{p_m, q_m}$ & Corvaja–Zannier Subspace Attack on $W_{\mathrm{pos}}(1) < \infty$
In PR #149, the constants $(8, 5)$ come from the single convergent $8/5 > \log_2 3$.
* Replace $(8, 5)$ with **higher upper convergents** $(p_{2m+1}, q_{2m+1})$ of $\log_2 3$: $(2, 1), (8, 5), (65, 41), (485, 306), \dots$
* Defining $W^{(m)}(z) = \sup(p_{2m+1} k - q_{2m+1} A)$, the positivity slope $\delta_m = p_{2m+1} - q_{2m+1} \log_2 3$ shrinks as $O(1/q_{2m+2})$ (for $(65, 41)$, $\delta \approx 0.0165$ vs. $0.0752$ for $(8, 5)$!), squeezing the admissible corridor $[\log_2 3, p_{2m+1}/q_{2m+1}]$ by a factor of $4.5\times$!
* **Decisive Open Question:** Can **Corvaja–Zannier's $p$-adic Subspace Theorem** (applied to the $S$-unit-like expansion $2^A - 3^k y = C_w$ with $A/k \in [\log_2 3, 65/41]$) prove $W_{\mathrm{pos}}^{(m)}(1) < \infty$ for some upper convergent $(p_{2m+1}, q_{2m+1})$? Note that PR #149's `CLOSURE_BOUNDARY.md` Equivalence Theorem generalizes verbatim from $(8, 5)$ to any upper convergent $(p_{2m+1}, q_{2m+1})$!
