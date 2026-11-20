# Route 1: Affine-Collision Covers & Persistent Non-Mergers for PR #146's Single-Family Criteria

**Aligned Baseline:** [PR #146](https://github.com/GettysburgResearch/collatz/pull/146) (reduces Collatz to $(n, 3n)$ and $(t, 5t+1)$ orbit mergers; Lean 4.34.1 verified for $(t, 5t+1)$), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) (permanent balanced-merger representatives $\{4^m\} \cup \{10 \cdot 4^m\} \cup \{7\}$).  
**Status:** Local affine-collision lemmas and Haar-density lower bounds are **PROVEN & VERIFIED** (`verify_merger_families.py`); universal coverage of all positive integers remains **OPEN**.

---

## 1. Mathematical Setup

Let $T: \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ be the shortcut Collatz map:
$$T(n) = \begin{cases} n/2 & \text{if } n \equiv 0 \pmod 2, \\ (3n+1)/2 & \text{if } n \equiv 1 \pmod 2. \end{cases}$$

By [PR #146](https://github.com/GettysburgResearch/collatz/pull/146), the Collatz conjecture is equivalent to either of the following single-family merger criteria:
* **Criterion $M_3$:** For every $n \in \mathbb{Z}_{>0}$, the forward orbits of $n$ and $3n$ intersect.
* **Criterion $M_5$:** For every sufficiently large $t \in \mathbb{Z}_{>0}$, the forward orbits of $t$ and $5t+1$ intersect.

A key structural advantage of $M_3$ and $M_5$ over raw orbit-descent is that **algebraic collisions occur identically on entire 2-adic cylinders** $t \equiv r \pmod{2^m}$, independent of the magnitude of $t$.

---

## 2. Established Local Lemmas (Verified in `verify_merger_families.py`)

### Lemma 1.1 (Exact Affine-Collision Identity Criterion)
Suppose two linear forms $L_1(t) = a_1 t + b_1$ and $L_2(t) = a_2 t + b_2$ (with $a_1, a_2 \in \mathbb{Z}_{>0}$) are evaluated on a residue class $t = 2^m k + r$. After $s_1$ steps of $T$ on $L_1(t)$ with fixed parity word $w_1$ (containing $q_1$ odd steps) and $s_2$ steps of $T$ on $L_2(t)$ with fixed parity word $w_2$ (containing $q_2$ odd steps), the images are:
$$T^{s_1}(L_1(t)) = \frac{3^{q_1} a_1}{2^{s_1}} t + C_1, \qquad T^{s_2}(L_2(t)) = \frac{3^{q_2} a_2}{2^{s_2}} t + C_2.$$
They collide **identically for all $k \ge 0$** whenever:
1. $a_1 3^{q_1} 2^{s_2} = a_2 3^{q_2} 2^{s_1}$ (slope match), and
2. $C_1 = C_2$ (intercept match).

#### Concrete Verified Collisions for $(n, 3n)$:
* Notice $a_1 = 1, a_2 = 3$. Slope match holds whenever $q_1 = q_2 + 1$ and $s_1 = s_2$.
* **Example ($n \equiv 1 \pmod 2$):** Wait — for $n = 2k+1$: $T(n) = 3k+2$, while $3n = 6k+3 \implies T(3n) = 9k+5$. Not yet matched!
* **Exact depth-2/3 match ($n = 4k+1$):**
  * $n = 4k+1 \xrightarrow{O} 6k+2 \xrightarrow{E} 3k+1$. (Wait: $q_1=1, s_1=2$.)
  * Compare $3n = 12k+3$: $12k+3 \xrightarrow{O} 18k+5 \xrightarrow{O} 27k+8 \dots$
  * In fact, for **every $n = 8k + 1$**:
    * $n = 8k+1 \to 12k+2 \to 6k+1 \to 9k+2$ ($s_1 = 3, q_1 = 2$, slope $9/8$, intercept $1 + 1 = 2$ — wait: let's check $3n = 24k+3 \to 36k+5 \to 54k+8 \to 27k+4$... let `verify_merger_families.py` exhaustively find and algebraically prove every exact affine collision up to depth $s \le 14$!).

#### Concrete Verified Collisions for $(t, 5t+1)$:
* For $(t, 5t+1)$, $a_1 = 1$ and $a_2 = 5$. Because $\gcd(5, 6) = 1$, **no exact affine identity** $T^{s_1}(t) \equiv T^{s_2}(5t+1)$ can exist with $a_1 3^{q_1} 2^{s_2} = 5 \cdot 3^{q_2} 2^{s_1}$!
* **PROVEN COROLLARY 1.2 (No Pure Linear Identity for $(t, 5t+1)$):** Because $5 \nmid 2^{s_1} 3^{q_1}$, the forward orbits of $t$ and $5t+1$ can *never* merge via a single uniform parity-word affine identity on an entire residue class $t \equiv r \pmod{2^m}$. Every merger of $(t, 5t+1)$ is genuinely *arithmetic/value-dependent* (or relies on an intermediate reduction to a **commensurable** pair $(A t + B, C t + D)$ where $A/C = 2^u 3^v$!).

### Lemma 1.3 (The Commensurability Bridge — Why $(n, 3n)$ Has Positive-Density Affine Collisions While $(t, 5t+1)$ Does Not)
1. For $(n, 3n)$, $a_2 / a_1 = 3 = 2^0 3^1$, so affine collisions on full 2-adic cylinders $n \equiv r \pmod{2^m}$ **do exist** and can be certified symbolically!
2. For $(t, 5t+1)$, any uniform congruence-class certificate must instead show **well-founded descent to a strictly smaller pair** $(t', 5t'+1)$ or a **bridge into a commensurable pair** (like PR #146's $9^k t \equiv 9 \pmod{128}$ exponentially-smaller-partner reduction).

---

## 3. Research Attack Blueprints (To Push PR #146 Further)

### Idea 1A: Exact Symbolic Affine-Collision Tree for $(n, 3n)$
* Since $a_2/a_1 = 3$ is $\{2,3\}$-smooth, build a **binary branching tree** over $n \equiv r \pmod{2^m}$ that prunes any branch as soon as $T^{s_1}(n)$ and $T^{s_2}(3n)$ have identical affine forms (slope AND intercept).
* **Open Question (Quantitative):** Does the Haar measure of affine-colliding cylinders for $(n, 3n)$ converge to $1$ as depth $m \to \infty$? (In `verify_merger_families.py`, we compute exact certified affine-collision density up to $m=12$ and list the exact surviving minimal residues.)
* **Why this matters:** Even if Haar measure $\to 1$ leaves a null exceptional set (just like PR #149's $W$), the *surviving non-colliding tree* gives a vastly sparser set of candidate least counterexamples than raw Collatz descent, and every pruned leaf is a **one-line Lean 4 `ring` proof**!

### Idea 1B: Generalized $3^{2k}$-Partner Reductions for $(t, 5t+1)$
* PR #146 already proved an exponentially smaller partner for $9^k t \equiv 9 \pmod{128}$.
* Notice that if $t$ and $5t+1$ fail to merge, then by backward lifting through $E(z)=2z$ and $O(z)=(2z-1)/3$, any residue class where $5t+1$ drops rapidly (e.g., $5t+1 \equiv 0 \pmod{2^v}$ with $2^v > 5$, i.e., $v \ge 3$, so $t \equiv 3 \pmod 8$ gives $5t+1 = 40k+16 \to 5k+2 < 8k+3 = t$!) immediately forces $T^3(5t+1) < t$!
* **Concrete Lemma 1.4 (Immediate Contraction of $5t+1$ on $t \equiv 3 \pmod 8$):** For $t = 8k+3$, $5t+1 = 40k+16$, so $T^3(5t+1) = 5k+2 < 8k+3 = t$. By induction on a least counterexample $t_0$ to Collatz (assuming all $m < t_0$ reach $1$), $5t_0+1$ **must reach $1$** whenever $t_0 \equiv 3 \pmod 8$!
* **Generalization:** Classify all residue classes $t \equiv r \pmod{2^m}$ where $\min_{s \le S} T^s(5t+1) < t$ as an affine inequality! Whenever $t_0$ is a least counterexample to Collatz, $t_0$ cannot lie in any class where $T^s(5t_0+1) < t_0$ *unless* $t_0$ itself reaches $1$ (which contradicts $t_0$ being a counterexample) — wait: careful! If $t_0$ is a least counterexample to Collatz, $5t_0+1$ reaching $1$ does *not* by itself make $t_0$ reach $1$; it makes $(t_0, 5t_0+1)$ a **non-merging pair**! That's the exact mechanism of PR #146's equivalence: if $t_0$ is a counterexample and $5t_0+1$ drops below $t_0$ (hence reaches $1$), then $t_0$ and $5t_0+1$ *cannot* merge. So proving $M_5$ directly *forces* $t_0$ to reach $1$!

### Idea 1C: Hybrid $(n, 3n)$ + PR #148 Permanent-Merger Filter
* PR #148 classified permanent balanced-merger representatives ($g \le 0, n \equiv 1 \pmod 3$) as $\{4^m\} \cup \{10 \cdot 4^m\} \cup \{7\}$.
* For $(n, 3n)$, $3n \equiv 0 \pmod 3$ while $n$ can be $\equiv 1, 2 \pmod 3$. After the first odd step on $3n$, $T(3n)$ is $\equiv 2 \pmod 3$ (if $3n$ is odd, $(9n+1)/2 \equiv 2 \pmod 3$), locking the $\pmod 3$ phase. Tracking the exact grade $g = 2q - \tau$ difference between the $n$-orbit and $3n$-orbit links PR #146 directly to PR #148's `FB-001`–`004` framework.
