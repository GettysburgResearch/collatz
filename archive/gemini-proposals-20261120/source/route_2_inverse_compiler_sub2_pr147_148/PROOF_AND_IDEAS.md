# Route 2: Breaking the Slope-2 Barrier in the Physical Inverse Compiler (PR #147 / PR #148)

**Aligned Baseline:** [PR #147](https://github.com/GettysburgResearch/collatz/pull/147) ($13/6$ finite-credit compiler, Bellman potential $FV \le V$, cap-6 stationary mean exponent $1.937 < A < 1.938$), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) ($25/12$ finite-credit inverse certificate), [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) (basin-only / $W(1) < \infty$ closure audit).  
**Status:** Max-plus / Bellman contraction framework and modular Karp min-cycle-mean solver are **PROVEN & VERIFIED** (`verify_inverse_compiler.py`); global slope $< 2$ physical certificate and forward-closure bridge remain **OPEN**.

---

## 1. Context: The Progression Toward Slope 2

The repository's physical inverse compiler uses the exact inverse actions of the shortcut map $T$:
$$E(z) = 2z, \qquad O(z) = \frac{2z - 1}{3} \quad (\text{legal iff } z \equiv 2 \pmod 3).$$

Across recent PRs, the certified uniform slope $\alpha$ in $k \le \lfloor \alpha t + C \rfloor$ (where $k$ counts total inverse actions $E, O$ and $t$ counts odd lifts $O$, or equivalently total steps per odd lift) has dropped steadily:
* PR #141: $\alpha = 7/3 \approx 2.3333$
* [PR #147](https://github.com/GettysburgResearch/collatz/pull/147): $\alpha = 13/6 \approx 2.1667$ (354,294 states, max credit 66)
* [PR #148](https://github.com/GettysburgResearch/collatz/pull/148): $\alpha = 25/12 \approx 2.0833$ (1,872,249-byte policy, 202 iterations)
* Meanwhile, [PR #147](https://github.com/GettysburgResearch/collatz/pull/147) proved a source-qualified equivalence between the infimum robust-credit slope and the stationary mean exponent, and rebuilt a cap-6 stationary policy with $1.937 < A < 1.938 < 2$.

---

## 2. Established Local Lemmas (Verified in `verify_inverse_compiler.py`)

### Lemma 2.1 (Why $\alpha = 2$ Is the Sharp Algebraic Threshold & Exact Bellman Form)
Consider a finite directed state graph $G = (S, \mathcal{A})$ representing modular residue classes (e.g., $\pmod{3^r}$ or $\pmod{2^s 3^r}$ together with a bounded action cap) where each transition $u \xrightarrow{a} v$ consumes $k(a)$ total inverse steps and $t(a)$ odd lifts ($O$). Define the $\alpha$-penalized Bellman operator on potentials $V: S \to \mathbb{R}$:
$$(F_\alpha V)(u) = \min_{u \xrightarrow{a} v} \Big( k(a) - \alpha t(a) + V(v) \Big).$$

1. **Certificate Equivalence (Karp / Max-Plus Duality):** There exists a bounded potential $V: S \to \mathbb{R}$ satisfying $F_\alpha V \le V$ (equivalently, a uniform finite-credit compiler with slope $\alpha$ and credit bound $\max V - \min V$) **if and only if** the minimum cycle mean of $G$,
   $$\alpha^*(G) = \min_{\text{cycle } \gamma \subset G} \frac{\sum_{a \in \gamma} k(a)}{\sum_{a \in \gamma} t(a)},$$
   satisfies $\alpha^*(G) \le \alpha$ (or for adversarial / robust branching where the adversary picks the worst residue lift among children, the corresponding minimax game value $\alpha_{\text{rob}}^*(G) \le \alpha$).
2. **Sharpness of $\alpha = 2$:** Under a policy with $k \le \alpha t + C$, the asymptotic branching/height ratio per odd lift is $2^\alpha / 3$. Note that:
   * At $\alpha = \log_2 3 \approx 1.58496$, $2^\alpha / 3 = 1$ (neutral height).
   * At $\alpha = 2$, $2^\alpha / 3 = 4/3$, which is the exact threshold for PR #148's balanced grade $g = 2q - \tau \le 0$ and PR #149's stopping defect $\kappa = d - 2a$.
   * Crossing $\alpha < 2$ (e.g. $\alpha = 23/12 \approx 1.9167$ or $31/16 = 1.9375$) proves that the compiled inverse tree achieves **strictly negative average defect** $\kappa/t = \alpha - 2 < 0$ uniformly across all states in the finite-credit machine!

### Lemma 2.2 (Explicit Honesty Check Against PR #149's Closure Boundary)
Even if an explicit finite-credit inverse compiler breaks $\alpha < 2$ (matching PR #147's $1.937 < A < 1.938$), [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) proves this **alone does not close Collatz**:
* An inverse compiler starting from $1$ only certifies rapid growth/coverage inside the **connected component (basin) of $1$**.
* Closing forward Collatz additionally requires ruling out disjoint components (cycles and divergent orbits), which in PR #149's language requires proving $W(1) < \infty$ (or pairing the sub-2 inverse compiler with a forward covering/density bridge that leaves no room for a second component).

---

## 3. Research Attack Blueprints (Concrete Ideas for the Agent)

### Idea 2A: Minimax Policy Iteration (Howard's Algorithm) Instead of Value Iteration
* PR #148 required 202 value-iteration rounds to reconstruct the $25/12$ policy.
* On a deterministic or 2-player minimax credit graph (where the compiler chooses an inverse macro-action $a$ and the adversary chooses the worst mod-$3^r$ lift), **minimax policy iteration** (solving the exact cycle-mean / linear potential $V$ for a fixed policy, then greedily improving actions) converges in $\sim 10$–$20$ outer iterations and directly outputs the **exact rational critical slope** $\alpha_{\text{rob}}^*(G)$ without guessing $\alpha = 25/12$ vs. $23/12$ in advance!

### Idea 2B: Variable-Length Macro-Actions Targeting $z \equiv 2 \pmod 3$
* In the raw inverse tree, $z \equiv 0 \pmod 3$ is a dead end for $O(z)$ (you can only apply $E(z) = 2z$, which stays $\equiv 0 \pmod 3$ forever!).
* Therefore, any admissible inverse state must satisfy $z \not\equiv 0 \pmod 3$, and applying $O(z) = (2z-1)/3$ requires $z \equiv 2 \pmod 3$ AND avoiding $O(z) \equiv 0 \pmod 3$ (which happens iff $2z - 1 \equiv 0 \pmod 9$, i.e., $z \equiv 5 \pmod 9$).
* **Key Optimization:** Compress the state space modulo $3^r$ to *only* units $(\mathbb{Z}/3^r\mathbb{Z})^\times$, and emit only **safe macro-actions** ($O$, $EO$, $E^2 O$, etc.) that land back in $(\mathbb{Z}/3^r\mathbb{Z})^\times$. As `verify_inverse_compiler.py` demonstrates on small $r$, this immediately reveals the exact optimal cyclic slopes and shows how quickly the minimax slope drops below $2$ as macro-action cap $L$ increases.

### Idea 2C: Dual-Side Certificate (Sub-2 Inverse Compiler + Route 3 Forward Contraction)
* To bridge PR #149's basin-only obstruction, don't ask the inverse compiler to prove Collatz alone. Instead, use a sub-2 inverse compiler to prove that the inverse basin of $1$ hits every residue class mod $2^m$ with explicit polynomial-size witnesses, and pair it with Route 1's $(n, 3n)$ / $(t, 5t+1)$ merger reductions to rule out disjoint components.
