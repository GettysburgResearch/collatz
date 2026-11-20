# Cross-Route Barrier Audit: What Cannot Close Collatz (and What Must Enter)

- **Status:** `VERIFIED_EXACT` (structural diagnosis grounded in [STATE.md](https://github.com/GettysburgResearch/collatz/blob/main/STATE.md) and [PR #149](https://github.com/GettysburgResearch/collatz/pull/149))

## 1. The PR #149 Rational-Cycle Barrier (The Single Most Important Guardrail)

In [PR #149](https://github.com/GettysburgResearch/collatz/pull/149), the repo establishes a decisive structural obstruction: **one can construct positive noninteger rational cycles of the shortcut map $T$ matching arbitrary fixed finite-depth binary ($2$-adic) and ternary ($3$-adic) observations above an arbitrary real floor $M > 0$.**

Algebraically, any finite parity word $w = (w_0, \dots, w_{K-1}) \in \{0, 1\}^K$ with $L = \sum w_i$ odd steps defines a unique rational periodic point
$$x_0(w) = \frac{C(w)}{2^K - 3^L}, \qquad C(w) = \sum_{i : w_i = 1} 3^{L_i} 2^{i},$$
where $L_i = \#\{j > i : w_j = 1\}$. Notice two critical facts:
1. Whenever $2^K > 3^L$ (i.e., $K/L > \log_2 3 \approx 1.58496$), $x_0(w) > 0$ is **strictly positive**.
2. Because $\gcd(2^K - 3^L, 6) = 1$, we have $x_0(w) \in \mathbb{Z}_{(6)} = \mathbb{Z}_2 \cap \mathbb{Z}_3$ **automatically**!

For example (verified in `route3_global_integrality_and_cube4/rational_barrier_and_diophantine.py`):
- `1110` ($K=4, L=3, D=-11$): $x_0 = -19/11$ (the `STATE.md` negative ghost).
- `11010` ($K=5, L=3, D=5$): $x_0 = 23/5 = 4.6 \in \mathbb{Z}_2 \cap \mathbb{Z}_3$.
- `11111000` ($K=8, L=5, D=13$): $x_0 = 211/13 \approx 16.23 \in \mathbb{Z}_2 \cap \mathbb{Z}_3$.

### Consequence for Every Proof Route
**Any argument that uses ONLY:**
- finite-depth $2$-adic congruences (parity cylinders),
- finite-depth $3$-adic congruences (unit tails / inverse compilers),
- Haar-measure / probabilistic drift bounds on $\mathbb{Z}_2$ or $\mathbb{Z}_3$, and
- archimedean positivity / lower-floor bounds ($x_n > M$),

**is provably incapable of ruling out nontrivial positive cycles** unless it explicitly invokes **global integrality at primes $p \ge 5$** (i.e., $v_p(x_0) \ge 0$ for all primes $p \mid (2^K - 3^L)$, or equivalently the global product formula $\prod_{v \le \infty} |x|_v = 1$).

## 2. The Second Barrier: Same-Slope vs. Asynchronous Coalescence (PR #145 & #146)

Our exact sieve computation in `route1_tripling_and_sibling_mergers/algebraic_coalescence_sieve.py` demonstrates a second sharp barrier:
- For tripling pairs $(n, 3n)$ ([PR #146](https://github.com/GettysburgResearch/collatz/pull/146)), exact algebraic coalescence $T^{k_1}(2^M m + r) = T^{k_2}(3(2^M m + r))$ excludes only **20.87%** of odd residue classes at $M = 13$ (box-dimension estimate $\approx 0.97185$, creeping upward toward $1$).
- For sibling pairs $(2n, 2n+1)$ ([PR #145](https://github.com/GettysburgResearch/collatz/pull/145)), exact algebraic coalescence excludes **52.66%** of residue classes at $M = 12$ (box-dimension estimate $\approx 0.91009$).
- Because PR #146's counterexample lower bound is $D(X) \ge c X^{0.84}$ (and $X^{0.164}$ eventually), **synchronous/same-slope $2$-adic algebraic coalescence cannot contradict $D(X)$**. Any upper bound on $D(X)$ beating $X^{0.84}$ MUST capture **asynchronous** coalescence (different odd-step counts $(a_1, a_2)$) or **archimedean-coupled** Tao mixing.

## 3. Summary: Where Global Rigidity Must Enter in Each Route

1. **Route 1 (PR #146/#145):** Global archimedean size + $3$-adic equidistribution (Tao-style Syracuse coupling on pairs) + well-ordering of $\mathbb{N}$ (minimality of $x_{\min}$).
2. **Route 2 (PR #147/#148):** Deterministic Bellman–Isaacs potentials close the **inverse-compiler** sub-problem (slope $< 2$, eliminating the stationarity hypothesis), which feeds into global predecessor density bounds—but inverse compilation alone does not force $W(1) < \infty$ without an asynchronous merger bridge.
3. **Route 3 (PR #149/#148):** Explicit $p$-adic divisibility ($p \ge 5 \mid 2^K - 3^L$) + effective linear forms in archimedean and $p$-adic logarithms (LMN + Bugeaud–Laurent) to make `CUBE-4` effective and separate integer orbits from rational ghosts.
4. **Route 4 (`STATE.md` / PR #145):** Adelic/anisotropic Banach norms that penalize prime denominators $p \ge 5$ so rational cycles are excluded from the spectrum at $\lambda = 1$.
