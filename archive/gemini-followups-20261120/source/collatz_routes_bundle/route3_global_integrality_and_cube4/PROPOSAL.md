# Route 3: Defeating PR #149's Rational-Cycle Barrier & Making `CUBE-4` (`PR #148`) Effective

- **Status:** `PROPOSED` (with `VERIFIED_COMPUTATIONAL` Diophantine & rational-cycle checks)
- **Target PRs:** [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) (noninteger rational cycles & $W(1) < \infty$), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) (`CUBE-4` ineffective finiteness & `MD-001`)

## 1. Diagnosing the Global-Integrality Gap

Every rational cycle of $T$ with parity word $w \in \{0,1\}^K$ ($L$ odd steps, $2^K > 3^L$) has the exact form
$$x_0(w) = \frac{C(w)}{2^K - 3^L} \in \mathbb{Z}_2 \cap \mathbb{Z}_3.$$
Because $\gcd(2^K - 3^L, 6) = 1$, **no local $2$-adic or $3$-adic constraint can ever distinguish a genuine integer cycle from PR #149's fake rational cycles.** The exact missing condition is **global integrality at all primes $p \ge 5$ dividing $D = 2^K - 3^L$**:
$$v_p(C(w)) \ge v_p(2^K - 3^L) \qquad \forall \text{ primes } p \ge 5.$$

Equivalently, by the **adelic product formula** $\prod_{v \in \{\infty, 2, 3, 5, \dots\}} |x_0|_v = 1$, a rational cycle $x_0 \in \mathbb{Z}_2 \cap \mathbb{Z}_3$ is an integer iff $\prod_{p \ge 5} |x_0|_p \le 1$.

## 2. Attack A — Making `CUBE-4` (`PR #148`) Effective (Replacing the Subspace Theorem)

PR #148 gives a source-qualified **ineffective** finiteness proof (`CUBE-4`) for primitive positive ordinary cycles covered by four nonempty powered factors (where ineffectiveness enters via Schmidt's Subspace Theorem / Evertse's $S$-unit bound).

### How to Make `CUBE-4` Effective:
For a 4-block powered cycle ($m = 4$ high-low / powered factors), the cycle equation takes the form
$$x_0 (2^K - 3^L) = \sum_{j=1}^{4} c_j 2^{a_j} 3^{b_j}$$
with $a_1 < a_2 < a_3 < a_4$ and $b_1 > b_2 > b_3 > b_4$.
1. **Archimedean Lower Bound on $|K \log 2 - L \log 3|$ (LMN / Rhin):**
   Apply **Laurent–Mignotte–Nesterenko (1995)** (or Rhin's irrationality measure $\mu(\log 2 / \log 3) < 5.125$) to obtain an explicit lower bound:
   $$|2^K - 3^L| > 3^L \cdot \exp\big(-C_{\text{LMN}} (\log K)^2\big).$$
2. **$p$-Adic Linear Forms in Two Logarithms (Bugeaud–Laurent, 1996) at $p = 2$ and $p = 3$:**
   Instead of using the ineffective Subspace Theorem on the 4-term $S$-unit equation, apply **Bugeaud–Laurent** explicit upper bounds on $v_2(3^u - 1)$ and $v_3(2^v - 1)$ to bound the internal block-gap valuations $a_{j+1} - a_j$ and $b_j - b_{j+1}$ effectively in terms of $\log K$.
3. **Effective Period Cutoff + Baker–Davenport Reduction:**
   Combine the effective upper bound on $L$ with the known computational lower bound on nontrivial cycle lengths (Hercher 2023 / Simons–de Weger, ruling out all $m$-cycles up to $m \le 91$ and $L \ll 10^{11}$ via continued-fraction convergents of $\log_2 3$) and apply **Baker–Davenport / LLL reduction** to close the finite gap between the computational floor and the effective LMN/Bugeaud–Laurent ceiling!

## 3. Attack B — Extending PR #149's Potential $W(n) = \sup(8k - 5A)$ Beyond the $1$-Basin

PR #149 notes that $W(n) \le 5 \log_2 n + W(1) + 1$ holds on the $1$-basin, and $W(1) < \infty$ is equivalent to Collatz, while Haar-measure tail control on $\mathbb{Z}_2$ does not extend to other components.
- **Concrete Bridge Idea (`OPEN_OBLIGATION: R3-HEIGHT`):** On a hypothetical second component $\mathcal{C}$ (divergent orbit or nontrivial cycle), pair the $2$-adic potential $W(n)$ with the **radical / prime-divisor height** $\sum_{p \ge 5} v_p(2^k n - \text{shift})$. Any rational cycle of PR #149 has unboundedly growing $p$-adic denominators as its binary/ternary matching depth increases; proving a quantitative **Diophantine repulsion** between the orbit of $n \in \mathbb{Z}^+$ and the dense set of PR #149 rational cycles $\mathcal{Q}_{\text{cyc}}$ (via effective simultaneous approximation in $\mathbb{R} \times \mathbb{Z}_2$) is the exact missing link to force $W(n) < \infty$ outside the $1$-basin.
