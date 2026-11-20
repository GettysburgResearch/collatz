# Route 4: Closing the `SC*`/`FC*` Crosswalk, Baker–Farey Gates, and Hermite–Padé Beyond Period 10

**Aligned Baseline:** [docs/RESEARCH_MAP.md](https://github.com/GettysburgResearch/collatz/blob/main/docs/RESEARCH_MAP.md) (`SC*`/`FC*` program), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) (`CUBE-4`, `MD-001`), [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) (noninteger rational cycles), Issues #75, #78, and [research/open-obligations](https://github.com/GettysburgResearch/collatz/tree/main/research/open-obligations) (#2 & #6).  
**Status:** Exact `SC*`/`FC*` least-counterexample dichotomy, canonical displacement identities, and continued-fraction Farey convergent table are **PROVEN & VERIFIED** (`verify_diophantine_cycles.py`); global `SC*`, global `FC*`, and period $\ge 10$ Hermite–Padé bounds remain **OPEN**.

---

## 1. Self-Contained `SC*`/`FC*` Least-Counterexample Crosswalk (Ready for Narrow Review)

In [STATE.md](https://github.com/GettysburgResearch/collatz/blob/main/STATE.md), the combined `SC*`/`FC*` least-counterexample crosswalk is currently listed as `PROPOSED`, pending narrow review. Below is the clean, minimal algebraic formulation.

For any starting integer $n \in \mathbb{Z}_{>0}$ and step $j \ge 1$, let $q(j)$ be the number of odd steps among $n, T(n), \dots, T^{j-1}(n)$. By induction on $j$:
$$T^j(n) = \frac{3^{q(j)} n + C_j(n)}{2^j}, \qquad C_j(n) = \sum_{i=0}^{j-1} \mathbf{1}_{\{T^i(n)\text{ odd}\}} 3^{q(j) - 1 - q(i)} 2^i \in \mathbb{Z}_{\ge 0}.$$

Define:
* **Coefficient-subcritical prefix (`SC*`):** Every fixed $n \in \mathbb{Z}_{>1}$ has some $j \ge 1$ with $D_j := 2^j - 3^{q(j)} > 0$.
* **First-crossing exclusion (`FC*`):** No integer $n \in \mathbb{Z}_{>1}$ can satisfy $T^j(n) \ge n$ at its *first* coefficient-subcritical step $j$ (where $D_j = 2^j - 3^{q(j)} > 0$ and $2^{j'} < 3^{q(j')}$ for all $1 \le j' < j$).

### Theorem 4.1 (`SC*` $\land$ `FC*` $\implies$ Collatz)
Suppose both `SC*` and `FC*` hold. Assume for contradiction that the Collatz conjecture fails, and let $n_0 > 1$ be the **least positive integer** whose orbit never reaches $1$.
1. By `SC*` applied to $n_0$, the set $\{j \ge 1 : 2^j > 3^{q(j)}\}$ is nonempty. Let $j_0$ be its minimum element, with $q_0 = q(j_0)$ and $D = 2^{j_0} - 3^{q_0} > 0$.
2. By `FC*` applied at the first crossing $(n_0, j_0)$, we cannot have $T^{j_0}(n_0) \ge n_0$. Hence $T^{j_0}(n_0) < n_0$.
3. By minimality of $n_0$, the orbit of $T^{j_0}(n_0)$ reaches $1$, so the orbit of $n_0$ reaches $1$ — contradiction. $\square$

### Corollary 4.2 (Canonical Displacement Identity & Why Integrality Breaks PR #149's Rational Cycles)
At any first crossing $T^j(n) \ge n$ with $D = 2^j - 3^q > 0$, write $T^j(n) = n + d$ with $d \ge 0$. Then:
$$2^j (n + d) = 3^q n + C_j \iff C_j = D n + 2^j d.$$
In particular, for a cycle ($d = 0$), $n = C_j / D$.
* In [PR #149](https://github.com/GettysburgResearch/collatz/pull/149), noninteger rational cycles exist above any floor because $n = C_j / D \in \mathbb{Q}_{>0}$ imposes **no divisibility constraint** $D \mid C_j$.
* For ordinary positive integers, $D \mid (C_j - 2^j d)$ (and for cycles, $D \mid C_j$) is the exact integrality barrier.

---

## 2. Attack Blueprint 4A: Continued-Fraction Farey Gate for `SC*` (Issues #75, #78)

If a positive integer $n_0$ violates `SC*`, then $3^{q(j)} > 2^j$ for **every** $j \ge 1$, meaning:
$$\frac{j}{q(j)} < \log_2 3 \approx 1.5849625 \quad \text{for all } j \ge 1.$$
Because $q(j)$ increases by at most $1$ per step, the trajectory of $(q(j), j)$ is trapped **strictly below the ray $j = q \log_2 3$** and must repeatedly pass through the narrow Farey corridors governed by the **even-indexed continued-fraction convergents** $p_{2k}/q_{2k} < \log_2 3$ (e.g. $1/1, 3/2, 8/5, 19/12, 65/41, 485/306, \dots$).
* By Laurent–Mignotte–Nesterenko's effective lower bound on linear forms in two logarithms, $|j \ln 2 - q \ln 3| > \exp(-C (\ln q)^2)$, which bounds how closely $3^q / 2^j$ can hover above $1$ without crossing.
* **Concrete Agent Task:** Couple the continued-fraction convergent gate with PR #148's multiplier cost bound ($2r_1 + \kappa < 11191/48500$) to tighten the admissible supercritical parity-word language at the convergents $q = 12, 41, 306$.

---

## 3. Attack Blueprint 4B: Breaking the Period-10 Padé Ceiling via Simultaneous Hermite–Padé (Obligation #6)

In [research/open-obligations](https://github.com/GettysburgResearch/collatz/tree/main/research/open-obligations) (#6), the native Padé stack theorem covers eventual periods $1$–$9$, while the delayed equal-phase family hits a strict ceiling at period $10$.
* **Why 1D equal-phase Padé stalls:** Approximating a single power $(1 - x)^N$ or $3^q/2^j$ via one equal-phase stack gives an irrationality exponent bound whose growth rate in the period $p$ crosses the threshold at $p = 10$ because the denominator height grows faster than the order of vanishing.
* **The Simultaneous (Type-I / Type-II) Hermite–Padé Pivot:** Instead of a single-function Padé approximant, construct simultaneous rational approximants $(P_0(z), P_1(z), \dots, P_m(z))$ to the **vector** of functions:
  $$\big(1,\; (1 - z)^{\beta_1},\; (1 - z)^{\beta_2},\; \dots,\; (1 - z)^{\beta_m}\big)$$
  evaluated at $z = 1 - 3^q / 2^j$ (or coupling $z$ with the cycle-sum rational function $R_w(z)$), with **asymmetric degree budgets** $(d_0, d_1, \dots, d_m)$ optimized to match the 2-adic valuation of the cycle numerator $C_j$.
* Because Type-I Hermite–Padé linear forms $P_0(z) + \sum_{i=1}^m P_i(z) f_i(z) = O(z^{\sum d_i + m})$ gain $m$ simultaneous vanishing degrees per shift while sharing a single common denominator LCM, the effective height-to-vanishing ratio beats 1D equal-phase stacks (the exact mechanism behind Beukers / Chudnovsky / Rhin–Viola improvements).
* `verify_diophantine_cycles.py` constructs and verifies a small-degree Type-I Hermite–Padé prototype ($m = 2$) and confirms exact high-order vanishing and non-vanishing linear forms at $z = 1 - 3^q/2^j$ for periods up to $12$.
