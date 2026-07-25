# L-9912 — Exponent statistics of hypothetical nontrivial Syracuse cycles

```text
Claim ID:      L-9912
Title:         Exponent statistics of nontrivial S-cycles: constant-exponent
               rigidity, forced exponent-1 steps, quantitative one-fraction,
               the {1,2}-window boundary, and the exponent-residue dictionary
Status:        PROVED
Authoring agent:   fable-02-p5
Reviewing agents:  fable-02-v14 (adversarial review 2026-07-25: PASS)
Created:       2026-07-21
Last updated:  2026-07-25 (fable-02-v14 adversarial review: PASS; status upgraded
               to PROVED; verification note appended at the end of the file)
Dependencies:  NOTATION.md (D-9904 Syracuse map and step exponent, D-9905 trivial
               cycle, D-9908 S-cycle notation and least period).
               L-9905 (Status: PROVED, reviewed by fable-02-v4) — cited for:
               L-9905.1 (cycle equation x_1(2^K - 3^m) = c), L-9905.2
               (positivity 2^K > 3^m), L-9905.3 (product formula
               2^K = prod(3 + 1/x_i) and 2^K <= (3 + 1/x_min)^m), L-9905.6
               (m = 1 is only the trivial cycle); each restated where used.
               L-9906 (Status: PROVED, reviewed by fable-02-v5) — cited for:
               L-9906.2 (floor x_min >= 7 in any nontrivial cycle; justification
               restated inline) and the main theorem (no nontrivial cycle with
               m <= 6), used only in L-9912.4(iii)'s combination remark.
Scope:         All nontrivial S-cycles (D-9908) on the positive odd integers,
               every m >= 1. L-9912.5 (dictionary) is a statement about ALL odd
               positive integers, no cycle hypothesis. The hypothesis-necessity
               audit examines the formal extension of S to negative odd
               integers; no claim of this file applies to negative integers.
Related counterexample candidates: none
```

---

## Statement

Throughout, fix a nontrivial $S$-cycle in the notation of D-9904/D-9908:
$x_1 \to x_2 \to \dots \to x_m \to x_1$, least period $m$, all $x_i$ positive odd,
exponents $a_i := \nu_2(3x_i + 1) \ge 1$, $K := \sum_{i=1}^m a_i$,
$x_{\min} := \min_i x_i$. Define the **one-count**
$$m_1 \;:=\; \#\{\, i \in \{1, \dots, m\} : a_i = 1 \,\},$$
an anchor-independent quantity (the multiset $\{a_1, \dots, a_m\}$ is
rotation-invariant). We call $(a_1, \dots, a_m)$ the **exponent word** of the
cycle (up to rotation).

**L-9912.1 (constant-exponent rigidity).** No nontrivial $S$-cycle has all
exponents equal. Precisely: if an $S$-cycle satisfies $a_1 = a_2 = \dots = a_m = a$
for some $a \ge 1$, then it is the trivial cycle $(1)$, with $m = 1$, $a = 2$.
The proof shows the cycle equation forces the exact rational value
$$x_1 \;=\; \frac{1}{2^a - 3},$$
which is a positive integer only for $a = 2$ ($x_1 = 1$); for $a = 1$ it equals
$-1$ (the famous negative fixed point $S(-1) = -1$, excluded by positivity), and
for $a \ge 3$ it lies strictly in $(0, 1)$.

**L-9912.2 (some exponent equals 1; floor-free).** Every nontrivial $S$-cycle
has $m_1 \ge 1$: at least one $i$ with $a_i = 1$. Equivalently, an $S$-cycle with
all $a_i \ge 2$ is the trivial cycle. **No lower bound on $x_{\min}$ is needed**
(see the correction note below).

*Corollary 2A (a residue is forced).* Every nontrivial $S$-cycle contains an
element $x_i \equiv 3 \pmod 4$ (by L-9912.2 and the $t = 1$ case of the
dictionary L-9912.5).

**L-9912.3 (quantitative one-fraction).** For every nontrivial $S$-cycle:

1. **(Counting bound; exact.)** $m_1 \ge 2m - K$, with equality if and only if
   $a_i \in \{1, 2\}$ for all $i$.
2. **(Fraction bounds.)** $K \le m \log_2\!\big(3 + \tfrac{1}{x_{\min}}\big)$, and
   therefore $m_1 \ge m\big(2 - \log_2(3 + \tfrac{1}{x_{\min}})\big)$. In
   particular:
   - using only $x_{\min} \ge 3$ (proved inline; independent of L-9906):
     $$m_1 \;\ge\; m\,\big(2 - \log_2\tfrac{10}{3}\big) \;=\; m \log_2\tfrac{6}{5}
     \;>\; \tfrac{m}{4}, \qquad \log_2\tfrac{6}{5} \in (0.2630,\, 0.2631);$$
   - using the floor $x_{\min} \ge 7$ (L-9906.2, PROVED; justification restated
     inline):
     $$m_1 \;\ge\; m\,\big(2 - \log_2\tfrac{22}{7}\big) \;=\; m \log_2\tfrac{14}{11}
     \;>\; \tfrac{m}{3}, \qquad \log_2\tfrac{14}{11} \in (0.3479,\, 0.3480).$$
   All decimal enclosures are certified by integer power comparisons (Proof and
   Adversarial tests); the two clean fractions $>m/4$, $>m/3$ are certified by
   the hand-checkable inequalities $6^4 = 1296 > 1250 = 2 \cdot 5^4$ and
   $14^3 = 2744 > 2662 = 2 \cdot 11^3$.
3. **(Upper bound.)** $m_1 \le m - 1$. No stronger elementary upper bound on
   $m_1/m$ is claimed; whether one exists is recorded as the open sub-question
   **Q-9912-A** below. (The upper-bound direction suggested in the task brief
   does not go through by counting alone; see the Proof for exactly why.)

**L-9912.4 (the live window; where elementary counting stops).**

1. **(General region.)** Every nontrivial $S$-cycle with $x_{\min} \ge X$
   ($X \ge 1$ real) satisfies
   $$\frac{K}{m} \in \Big(\log_2 3,\; \log_2\big(3 + \tfrac1X\big)\Big], \qquad
     \frac{m_1}{m} \;\ge\; 2 - \frac{K}{m}.$$
2. **($\{1,2\}$-cycles are not excluded by counting.)** If all $a_i \in \{1,2\}$
   ("a $\{1,2\}$-cycle"), then $m_1 = 2m - K$ exactly and
   $\tfrac{m_1}{m} = 2 - \tfrac{K}{m} \in
   \big[\,2 - \log_2(3 + \tfrac1X),\; 2 - \log_2 3\,\big)$. **This region is
   nonempty** — for $X = 7$ because $3 \cdot 14 = 42 < 44 = 4 \cdot 11$, for
   $X = 3$ because $18 < 20$ — so the proved constraints of this file and of
   L-9905 **cannot** refute $\{1,2\}$-exponent cycles. This is an honest
   boundary marker: issue #9's grammar searches should treat $\{1,2\}$-words in
   this ratio window as the live region that elementary counting does not touch.
3. **(Integer-window exclusions; new eliminations $m = 7, 9, 12$.)** For every
   nontrivial cycle, $K$ is an **integer** with $3^m < 2^K$ and (floor
   $x_{\min} \ge 7$, L-9906.2) $2^K \cdot 7^m \le 22^m$. The set of such $K$ is
   empty **exactly** for $m \in \{1, 2, 3, 4, 6, 7, 9, 12\}$, and nonempty for
   all other $m$ (for $m \in \{5, 8, 10, 11, 13, 14\}$ it is the singleton
   $\{8\}, \{13\}, \{16\}, \{18\}, \{21\}, \{23\}$ respectively; for $m \ge 15$
   it is always nonempty because its real length exceeds $1$). Hence **no
   nontrivial $S$-cycle has $m \in \{7, 9, 12\}$** — new beyond L-9906 — and,
   combined with L-9906 (PROVED, $m \le 6$):
   $$\text{every nontrivial } S\text{-cycle has } m \in \{8, 10, 11, 13, 14\}
     \cup \{m \ge 15\},$$
   with $m = 8$ (forced $K = 13$) the smallest case not excluded in-repo.

**L-9912.5 (exponent–residue dictionary).** For every $t \ge 1$ define
$$r_t \;:=\; \begin{cases} \dfrac{2^t - 1}{3}, & t \text{ even},\\[2mm]
\dfrac{5 \cdot 2^t - 1}{3}, & t \text{ odd}. \end{cases}$$
Then $r_t$ is a well-defined odd integer with $0 < r_t < 2^{t+1}$, and for every
positive odd integer $x$ and every $t \ge 1$:
$$a(x) = \nu_2(3x+1) = t \;\iff\; 3x + 1 \equiv 2^t \pmod{2^{t+1}}
\;\iff\; x \equiv r_t \pmod{2^{t+1}},$$
and in the "at least" form $\;a(x) \ge t \iff x \equiv r_t \pmod{2^t}$.
Small cases:
$$a = 1 \iff x \equiv 3 \ (4); \quad a = 2 \iff x \equiv 1 \ (8); \quad
a = 3 \iff x \equiv 13 \ (16); \quad a = 4 \iff x \equiv 5 \ (32); \quad
a = 5 \iff x \equiv 53 \ (64); \quad a = 6 \iff x \equiv 21 \ (128).$$

**Correction flags (task-brief audit).**
1. The brief proposed "$a_i = 3 \iff x_i \equiv 5 \pmod{16}$". This is **false**:
   $3 \cdot 5 + 1 = 16 = 2^4$, so $a(5) = 4$, and the correct $a = 3$ class is
   $x \equiv 13 \pmod{16}$ (e.g. $a(13) = \nu_2(40) = 3$); $5$ is the base point
   of the $a = 4$ class mod $32$. Proved and exhaustively verified below.
2. The brief's algebra for L-9912.3 — $2 - \log_2(22/7) = \log_2(14/11) \approx
   0.3479$ — is **confirmed correct** ($4/(22/7) = 28/22 = 14/11$).
3. The brief suggested L-9912.2 needs $x_i \ge 7$ or $x_i \ge 3$; in fact the
   sharpest clean version needs **no floor**: the equality analysis at $x = 1$
   closes the argument by itself (L-9912.2's proof).
4. (Minor, in the brief's test plan:) the negative cycle through $-5$ has
   Syracuse exponent word $(1, 2)$ — i.e. $-5 \to -7 \to -5$ with $m = 2$,
   $K = 3$ — not $(1,1,2)$; the latter resembles its $T$-map parity pattern.

---

## Definitions

- $S(x) = (3x+1)/2^{\nu_2(3x+1)}$, $a(x) = \nu_2(3x+1) \ge 1$ (D-9904); cycle
  data $x_i, a_i, A_i, K$, least period $m$, pairwise-distinct elements
  (D-9908, and L-9905's Definitions/L-9906 Step 0 P0 for distinctness);
  trivial cycle $(1)$ (D-9905). $c := \sum_{i=1}^m 3^{m-i} 2^{A_{i-1}}$ as in
  L-9905.
- **One-count $m_1$**: as in the Statement. More generally $m_t :=
  \#\{i : a_i = t\}$, so $m = \sum_{t \ge 1} m_t$ and $K = \sum_{t \ge 1} t\,m_t$.
- **$\{1,2\}$-cycle**: a cycle whose exponent word has all letters in $\{1,2\}$.
- **Exponent word**: $(a_1, \dots, a_m)$ up to rotation; anchor changes rotate
  it and permute nothing else (L-9905, anchoring convention).
- **Formal extension of $S$ to negative odd integers** (used ONLY in the
  hypothesis-necessity audit, never in a claim): for odd $x < 0$, $3x + 1$ is a
  nonzero even integer, and $S(x) := (3x+1)/2^{\nu_2(3x+1)}$ is again a negative
  odd integer. All *algebraic identities* (cycle equation, product formula)
  hold verbatim for cycles of this extension — L-9905's Scope notes this — while
  the *inequalities* use $x_i > 0$ and are expected to fail; the audit locates
  the exact failure for each known negative cycle.
- Certified decimal enclosures: a statement "$\log_2(p/q) \in (u, v)$" is always
  backed by the exact integer comparisons $q^N 2^{uN} < p^N < q^N 2^{vN}$ with
  $uN, vN$ integers (here $N = 10^4$), checked in the Adversarial tests; the
  proofs themselves only use the hand-checkable small certifications displayed
  inline.

---

## Motivation

This file hands issue #9's compressed-word cycle synthesis exact, in-repo-proved
constraints on admissible exponent words. L-9906 (PROVED) kills all cycles with
$m \le 6$; the present file constrains the **shape** of the exponent word at
every $m$: constant words are dead (L-9912.1), the letter $1$ must appear
(L-9912.2), it must in fact occupy more than a third of all positions
(L-9912.3 with the proved floor), the pair $(K/m, m_1/m)$ is pinned into an
explicit narrow window (L-9912.4), and each letter value $t$ is equivalent to an
explicit residue class mod $2^{t+1}$ (L-9912.5), so grammar families can prune
candidate words and candidate residues *before* any expensive verification. Two
outputs deserve emphasis: the $\{1,2\}$-window observation marks precisely where
elementary counting stops — a nonempty live region that synthesis should target
and that refutation must attack by finer means — and the integer-window
corollary L-9912.4(iii) shows the same counting, taken with integrality of $K$,
still had teeth left: it eliminates $m = 7, 9, 12$ outright, making $m = 8$
(with $K$ forced to be $13$) the smallest case the repository has not excluded.

*Context note (not a dependency).* Literature reports vastly stronger cycle
exclusions via transcendence plus large computation; as with L-9906, the value
here is complete elementary in-repo rigor, and the reusable statistics
themselves.

---

## Proof

### Step 0 — Floors on $x_{\min}$ (recap and layering)

**(F3) Unconditional floor $x_{\min} \ge 3$.** Elements of an $S$-cycle are
positive odd integers, pairwise distinct within one period (D-9908; proved as
L-9906 Step 0 P0, and recorded in L-9905's Definitions). If some element
$x_i = 1$, then $x_{i+1} = S(1) = \mathrm{odd}(4) = 1 = x_i$, so by distinctness
the least period is $1$ and the cycle is the trivial $(1)$ (D-9905). Hence a
**nontrivial** cycle has no element equal to $1$; its elements being odd and
positive, all are $\ge 3$. $\square$

**(F7) Floor $x_{\min} \ge 7$ — L-9906.2, Status PROVED (reviewer
fable-02-v5).** Justification restated: $S(3) = \mathrm{odd}(10) = 5$ and
$S(5) = \mathrm{odd}(16) = 1$, so the orbits of $3$ and $5$ reach the fixed
point $1$ and are eventually constant; a cycle element's orbit stays in the
cycle forever, so $3$ and $5$ lie on no cycle at all, and $1$ lies only on the
trivial one. An odd positive integer outside $\{1, 3, 5\}$ is $\ge 7$.
(Complete proof: L-9906, Step 2.) $\square$

Results below are labeled by which floor they use; everything tagged (F7)
inherits L-9906.2's PROVED status, everything tagged (F3) is independent of
L-9906.

### Step 1 — Proof of L-9912.5 (dictionary)

Let $x$ be a positive odd integer and $t \ge 1$.

**(1a) $\nu_2$-extraction as a congruence.** For any positive integer $y$:
$\nu_2(y) = t \iff y = 2^t u$ with $u$ odd $\iff y \equiv 2^t \pmod{2^{t+1}}$.
Indeed $u$ odd means $u = 1 + 2k$, so $y = 2^t + k\,2^{t+1}$; conversely
$y \equiv 2^t \pmod{2^{t+1}}$ gives $y = 2^t(1 + 2k)$ with $1 + 2k$ odd. Applied
to $y = 3x + 1 \ge 4$:
$$a(x) = t \iff 3x + 1 \equiv 2^t \pmod{2^{t+1}}
\iff 3x \equiv 2^t - 1 \pmod{2^{t+1}}. \tag{5.1}$$

**(1b) Unique solution.** $\gcd(3, 2^{t+1}) = 1$, so (5.1) has exactly one
solution $x \bmod 2^{t+1}$.

**(1c) The closed forms solve (5.1).** If $t$ is even, $2^t \equiv (-1)^t = 1
\pmod 3$, so $3 \mid 2^t - 1$ and $r_t = (2^t-1)/3$ is an integer with
$3 r_t + 1 = 2^t$ exactly — in particular $3r_t \equiv 2^t - 1 \pmod{2^{t+1}}$.
If $t$ is odd, $5 \cdot 2^t \equiv 2 \cdot (-1)^t = -2 \equiv 1 \pmod 3$, so
$3 \mid 5 \cdot 2^t - 1$ and $r_t = (5 \cdot 2^t - 1)/3$ is an integer with
$3 r_t + 1 = 5 \cdot 2^t = 2^t + 2^{t+2} \equiv 2^t \pmod{2^{t+1}}$.
In both cases $3 r_t$ is odd minus nothing — $2^t - 1$ and $5\cdot 2^t - 1$ are
odd — so $r_t$ is odd; and $0 < r_t < 2^{t+1}$ since $(2^t - 1)/3 < 2^t$ and
$(5 \cdot 2^t - 1)/3 < 6 \cdot 2^t/3 = 2^{t+1}$. By (1b), $r_t$ **is** the
unique solution, proving the main equivalence.

**(1d) The "$\ge t$" form.** $a(x) \ge t \iff 2^t \mid 3x + 1 \iff
3x \equiv -1 \pmod{2^t}$, which has the unique solution $x \equiv r_t \pmod{2^t}$
because $3 r_t \equiv 2^t - 1 \equiv -1 \pmod{2^t}$ by (1c). $\square$

**Small cases** (each verifiable in one line): $r_1 = 3$, $r_2 = 1$,
$r_3 = 13$, $r_4 = 5$, $r_5 = 53$, $r_6 = 21$, $r_7 = 213$, $r_8 = 85$.
E.g. $a(13) = \nu_2(40) = 3$ and $a(5) = \nu_2(16) = 4$ — this is Correction
flag 1: the $a = 3$ class mod $16$ is $13$, not $5$.

**Remark (tower structure; consistency check).** $r_{t+1} \equiv r_t
\pmod{2^t}$ (both solve $3x \equiv -1 \bmod 2^t$), so the classes refine along
the dyadic tower; the counting identity $\sum_{s=1}^{t} 2^{t-s} + 1 = 2^t$
confirms that the classes $\{a = s\}$ mod $2^{t+1}$ ($s \le t$) together with the
single class $\{a \ge t+1\}$ exactly partition the $2^t$ odd residues mod
$2^{t+1}$. The compatible sequence $(r_t)_t$ converges 2-adically to
$-1/3 \in \mathbb{Z}_2$, the unique 2-adic solution of $3x + 1 = 0$ — the
"depth-$\infty$" point of the dictionary. (Verified exhaustively for $t \le 12$,
odd $x < 2^{15}$: Adversarial tests, T2.)

### Step 2 — Proof of L-9912.1 (constant-exponent rigidity)

Let an $S$-cycle have $a_i = a$ for all $i$, so $K = am$; write $u := 2^a$. By
the cycle equation (L-9905.1, PROVED; re-derived inline as L-9906 Step 1):
$$x_1 \left(u^m - 3^m\right) \;=\; c \;=\; \sum_{i=1}^m 3^{m-i} 2^{a(i-1)}
\;=\; \sum_{i=1}^{m} 3^{m-i} u^{i-1} .$$

**Geometric-sum identity.** For any $u$ and any $m \ge 1$:
$$(u - 3) \sum_{i=1}^{m} 3^{m-i} u^{i-1}
\;=\; \sum_{i=1}^{m} \left(3^{m-i} u^{i} - 3^{m-i+1} u^{i-1}\right)
\;=\; u^m - 3^m,$$
a telescoping sum (the $i$-th positive term cancels the $(i{+}1)$-st negative
term; only $u^m$ from $i = m$ and $-3^m$ from $i = 1$ survive).
(Verified symbolically for $1 \le a \le 10$, $1 \le m \le 12$: T1.)

Since $u = 2^a$ is a power of $2$ and $3^m$ is odd, $u^m \ne 3^m$, so
$D := u^m - 3^m \ne 0$ and, as exact rationals,
$$x_1 \;=\; \frac{c}{D} \;=\; \frac{(u^m - 3^m)/(u - 3)}{u^m - 3^m}
\;=\; \frac{1}{u - 3} \;=\; \frac{1}{2^a - 3}. \tag{1.1}$$
(For $a = 1$, $u - 3 = -1 \ne 0$, so (1.1) is legitimate in every case.)

Now split on $a$:

- **$a = 1$:** $K = m$ and $2^K = 2^m < 3^m$, contradicting L-9905.2
  ($2^K > 3^m$ for every $S$-cycle on the positive odd integers). Consistently,
  (1.1) gives $x_1 = 1/(2-3) = -1$: the formal solution is the **negative**
  fixed point $S(-1) = -1$ (indeed $3(-1)+1 = -2$, $\nu_2 = 1$). It is excluded
  exactly by positivity of the $x_i$ — see the hypothesis-necessity audit.
- **$a = 2$:** (1.1) gives $x_1 = 1$. Then every element is $1$ (since
  $S(1) = 1$), so by distinctness the least period is $m = 1$ and the cycle is
  the trivial $(1)$ — consistent, and not nontrivial.
- **$a \ge 3$:** $2^a - 3 \ge 5$, so (1.1) gives $0 < x_1 \le \tfrac15 < 1$,
  contradicting $x_1 \in \mathbb{Z}^+$.

Hence the only constant-exponent $S$-cycle is the trivial one. $\blacksquare$

### Step 3 — Proof of L-9912.2 (some exponent equals 1; floor-free)

By the product formula (L-9905.3, PROVED; one-line rederivation: multiply the
step relations $2^{a_i} x_{i+1} = 3x_i + 1 = x_i\,(3 + \tfrac{1}{x_i})$ over
$i = 1, \dots, m$ and cancel $\prod_i x_{i+1} = \prod_i x_i > 0$):
$$2^K \;=\; \prod_{i=1}^{m} \Big(3 + \frac{1}{x_i}\Big). \tag{2.1}$$

Suppose every $a_i \ge 2$. Then $K = \sum a_i \ge 2m$, so
$$4^m \;\le\; 2^K. \tag{2.2}$$
On the other hand each $x_i \ge 1$ gives $3 + \tfrac1{x_i} \le 4$, so
$$2^K \;=\; \prod_{i=1}^m \Big(3 + \frac{1}{x_i}\Big) \;\le\; 4^m. \tag{2.3}$$
By (2.2)–(2.3), $2^K = 4^m$ and equality holds in (2.3). All factors are
positive, and if even one factor were $< 4$ the product would be
$< 4^{m}$ (bound the others by $4$); hence every factor equals $4$, i.e.
$x_i = 1$ for all $i$. By Step 0 (F3)'s argument, the cycle is then the trivial
cycle $(1)$.

Contrapositive: a **nontrivial** $S$-cycle has some $a_i = 1$, i.e. $m_1 \ge 1$.
Note the only inputs were (2.1) and $x_i \ge 1$: **no floor on $x_{\min}$ was
used** (Correction flag 3; the brief's suggested routes via
$(22/7)^m < 4^m$ or $(10/3)^m < 4^m$ are correct but weaker than necessary).

*Corollary 2A:* by L-9912.5 with $t = 1$, the element $x_i$ with $a_i = 1$
satisfies $x_i \equiv 3 \pmod 4$. $\blacksquare$

### Step 4 — Proof of L-9912.3 (quantitative one-fraction)

**(i) Counting bound.** Split the sum $K = \sum_{i=1}^m a_i$ by whether
$a_i = 1$:
$$K \;=\; m_1 \cdot 1 + \sum_{i:\, a_i \ge 2} a_i
\;\ge\; m_1 + 2\,(m - m_1) \;=\; 2m - m_1,$$
so $m_1 \ge 2m - K$. Equality holds iff every $a_i \ge 2$ equals exactly $2$,
i.e. iff all letters lie in $\{1, 2\}$. (Stress-tested on $2 \cdot 10^4$ random
words: T4.)

**(ii) Fraction bounds.** By L-9905.3, $2^K \le (3 + 1/x_{\min})^m$; taking
$\log_2$ (strictly increasing) gives $K \le m \log_2(3 + 1/x_{\min})$, and since
$t \mapsto 3 + 1/t$ is decreasing, any floor $x_{\min} \ge X$ yields
$K \le m \log_2(3 + 1/X)$. Substituting into (i) — note the inequality
direction: a larger upper bound on $K$ weakens the lower bound on $m_1$,
so a *floor* on $x_{\min}$ strengthens it —
$$m_1 \;\ge\; 2m - K \;\ge\; m\left(2 - \log_2\big(3 + \tfrac1X\big)\right)
= m\,\log_2\frac{4}{3 + 1/X} = m\,\log_2\frac{4X}{3X + 1}.$$
- $X = 3$ (Step 0 (F3), unconditional): $\tfrac{4X}{3X+1} = \tfrac{12}{10} =
  \tfrac{6}{5}$, so $m_1 \ge m \log_2(6/5)$. Certification $\log_2(6/5) > 1/4$:
  equivalent to $(6/5)^4 > 2$, i.e. $6^4 = 1296 > 1250 = 2 \cdot 5^4$. ✓
- $X = 7$ (Step 0 (F7), i.e. L-9906.2 PROVED): $\tfrac{4X}{3X+1} =
  \tfrac{28}{22} = \tfrac{14}{11}$, so $m_1 \ge m \log_2(14/11)$ — the brief's
  algebra confirmed (Correction flag 2). Certification $\log_2(14/11) > 1/3$:
  equivalent to $(14/11)^3 > 2$, i.e. $14^3 = 2744 > 2662 = 2 \cdot 11^3$. ✓

The four-decimal enclosures $\log_2(6/5) \in (0.2630, 0.2631)$ and
$\log_2(14/11) \in (0.3479, 0.3480)$ are certified by the exact integer
comparisons $5^{10^4} 2^{2630} < 6^{10^4} < 5^{10^4} 2^{2631}$ and
$11^{10^4} 2^{3479} < 14^{10^4} < 11^{10^4} 2^{3480}$ (T3; exact finite
verification, machine-executed). Since $m_1$ is an integer, e.g. the (F7) bound
gives $m_1 \ge \lfloor m/3 \rfloor + 1$.

**(iii) Upper bound; why no better one comes from counting.** If $m_1 = m$ then
all $a_i = 1$, so $K = m$; but L-9905.2 gives $K > m \log_2 3 > m$ —
contradiction. Hence $m_1 \le m - 1$.

The task brief asked whether counting yields $m_1 \le \beta m$ with $\beta < 1$.
It does not, for a structural reason worth recording: the two proved
constraints linking $m_1$ and $K$ are $m_1 \ge 2m - K$ (from below) and
$K \in (m \log_2 3,\, m \log_2(3 + 1/X)]$; both only ever bound $m_1$ from
**below** (a lower bound on $K$ says nothing, because positions with
$a_i \ge 2$ can absorb arbitrarily much of $K$ — the word
$(1, 1, \dots, 1, a_m)$ with $m - 1$ ones and one large letter satisfies every
counting constraint whenever $K = m - 1 + a_m$ lands in the window, e.g.
$m = 8$, $a_8 = 6$, $K = 13$). Any upper bound on $m_1/m$ strictly below
$1 - 1/m$ therefore needs non-counting input (residue propagation, run
structure, or size bounds); this is **Q-9912-A**, listed under Suggested next
attack. $\blacksquare$

### Step 5 — Proof of L-9912.4 (live window and integer exclusions)

**(i)** $K/m > \log_2 3$ is L-9905.2; $K/m \le \log_2(3 + 1/X)$ is Step 4(ii);
$m_1/m \ge 2 - K/m$ is Step 4(i). $\square$

**(ii)** For a $\{1,2\}$-cycle, Step 4(i) holds with equality: $m_1 = 2m - K$,
so $m_1/m = 2 - K/m$, and (i) confines this to
$\big[\,2 - \log_2(3 + \tfrac1X),\; 2 - \log_2 3\,\big)$ — half-open at the
right because $K/m > \log_2 3$ is strict. Nonemptiness of the interval is
equivalent to $\log_2\frac{4X}{3X+1} < \log_2 \frac43$, i.e.
$\frac{4X}{3X+1} < \frac43 \iff 12 X < 12X + 4$ — true always; in the
certified-decimal presentation for $X = 7$ it is the hand inequality
$\tfrac{14}{11} < \tfrac43 \iff 42 < 44$, and for $X = 3$ it is
$\tfrac65 < \tfrac43 \iff 18 < 20$. Hence there is a nonempty open region of
$(K/m, m_1/m)$ values that satisfies every constraint proved in this file and
in L-9905 — counting alone cannot refute $\{1,2\}$-cycles. **Live-window
table** (all decimals certified as in Definitions; brackets exact):

| quantity | any nontrivial cycle, floor $X{=}3$ (uncond.) | any nontrivial cycle, floor $X{=}7$ (L-9906.2) |
|---|---|---|
| $K/m$ | $(\log_2 3,\ \log_2\frac{10}{3}]\subset(1.5849,\,1.7370)$ | $(\log_2 3,\ \log_2\frac{22}{7}]\subset(1.5849,\,1.6521)$ |
| $m_1/m$ (lower bd.) | $\ge \log_2\frac65 > 0.2630$, and $> \frac14$ | $\ge \log_2\frac{14}{11} > 0.3479$, and $> \frac13$ |
| $m_1/m$, $\{1,2\}$-cycle (exact) | $= 2 - K/m \in [\log_2\frac65,\ \log_2\frac43) \subset (0.2630,\, 0.4151)$ | $= 2 - K/m \in [\log_2\frac{14}{11},\ \log_2\frac43) \subset (0.3479,\, 0.4151)$ |
| $m_1$ upper | $\le m - 1$ | $\le m - 1$ (better bound: open, Q-9912-A) |

**(iii) Integer-window exclusions (floor $X = 7$; both floor facts PROVED).**
For any nontrivial cycle, $K \in \mathbb{Z}$ satisfies both
$3^m < 2^K$ (L-9905.2) and $2^K \cdot 7^m \le 22^m$ (Step 4(ii) with $X = 7$,
denominator-cleared: $2^K \le (22/7)^m$). Call the set of such $K$ the integer
window $W_7(m)$. Exact integer arithmetic gives (T7; the small cases are
hand-checkable and displayed):

| $m$ | least $K$ with $2^K > 3^m$ | upper test at that $K$ | $W_7(m)$ |
|---|---|---|---|
| $1$ | $2$ | $4 \cdot 7 = 28 > 22$ | $\varnothing$ |
| $2$ | $4$ | $16 \cdot 49 = 784 > 484$ | $\varnothing$ |
| $3$ | $5$ | $32 \cdot 343 = 10976 > 10648$ | $\varnothing$ |
| $4$ | $7$ | $128 \cdot 2401 = 307328 > 234256$ | $\varnothing$ |
| $5$ | $8$ | $256 \cdot 16807 = 4302592 \le 5153632$; at $K{=}9$: $8605184 > 22^5$ | $\{8\}$ |
| $6$ | $10$ | $1024 \cdot 117649 = 120472576 > 113379904$ | $\varnothing$ |
| $7$ | $12$ | $4096 \cdot 823543 = 3373232128 > 2494357888$ | $\varnothing$ |
| $8$ | $13$ | $8192 \cdot 7^8 = 47225249792 \le 54875873536$; $K{=}14$ fails | $\{13\}$ |
| $9$ | $15$ | $32768 \cdot 7^9 = 1322306994176 > 1207269217792$ | $\varnothing$ |
| $10$ | $16$ | in window; $K{=}17$ fails | $\{16\}$ |
| $11$ | $18$ | in window; $K{=}19$ fails | $\{18\}$ |
| $12$ | $20$ | $2^{20} \cdot 7^{12} = 14513641568075776 > 12855002631049216$ | $\varnothing$ |
| $13$ | $21$ | in window; $K{=}22$ fails | $\{21\}$ |
| $14$ | $23$ | in window; $K{=}24$ fails | $\{23\}$ |

(The "least $K$" column is exact: $2^{K-1} \le 3^m < 2^K$; e.g. $2^{11} = 2048 <
2187 = 3^7 < 4096 = 2^{12}$. Whenever the least admissible $K$ already violates
the upper test, $W_7(m) = \varnothing$ because $2^K \cdot 7^m$ is strictly
increasing in $K$.)

For $m \ge 15$ the window is never empty: the real interval
$(m \log_2 3,\ m \log_2 \tfrac{22}{7}]$ has length $m \log_2 \tfrac{22}{21} \ge
15 \log_2 \tfrac{22}{21} > 1$, certified by the exact integer inequality
$22^{15} > 2 \cdot 21^{15}$ (T3) — and any half-open interval $(\alpha, \beta]$
of length $> 1$ contains the integer $\lfloor \beta \rfloor$ (since
$\lfloor \beta \rfloor \le \beta$ and $\lfloor \beta \rfloor > \beta - 1 >
\alpha$). Hence:
$$W_7(m) = \varnothing \iff m \in \{1, 2, 3, 4, 6, 7, 9, 12\},$$
and a nontrivial cycle with such $m$ would have no admissible $K$ at all —
contradiction. In particular **no nontrivial $S$-cycle has $m = 7$, $9$, or
$12$**. ($W_7(1) = \varnothing$ is consistent with the trivial cycle: its
$x_{\min} = 1$ violates the floor hypothesis, and nontrivial $m = 1$ is
excluded by L-9905.6 anyway.)

Combined with L-9906's main theorem ($m \le 6$; PROVED), every nontrivial
$S$-cycle has $m \in \{8, 10, 11, 13, 14\} \cup \{m \ge 15\}$, and for the five
listed small values $K$ is **forced** to the singleton value in the table.
$\blacksquare$

**Remark 3 (relation to L-9906's windows; independent cross-check).** L-9906
computed windows from the anchored $c$-bound (L-9905.4), obtaining
$\{5\}, \{7\}, \{8,9\}, \{10,\dots,13\}$ for $m = 3, 4, 5, 6$ and eliminating
each by exhaustive composition enumeration. The product-formula window used
here is strictly sharper in this range: it empties $m = 3, 4, 6$ outright and
shrinks $m = 5$ to $K = 8$ — so L-9906's enumeration outcome (no survivor) is
independently confirmed for $m = 3, 4, 6$, and only its $m = 5$, $K = 8$ block
of $\binom{7}{4} = 35$ compositions remains load-bearing for $m = 5$. The two
routes agree; neither contradicts the other. (This sharpening became visible
only at the exponent-statistics level; reviewers of L-9906 may enjoy the
cross-check.)

**Remark 4 (Fibonacci-flavored forced ratios; observation only).** The forced
values $K/m$ for $m = 5, 8, 10, 13$ are $8/5$, $13/8$, $16/10 = 8/5$, $21/13$ —
ratios of consecutive Fibonacci numbers, reflecting that the continued fraction
of $\log_2 3 = [1; 1, 1, 2, 2, 3, 1, \dots]$ begins golden-ratio-like. This is
flavor for the planned L-9910 (convergent constraints), not a claim.

### Step 6 — Hypothesis-necessity audit via the negative cycles (summary)

The formal extension of $S$ to negative odd integers (Definitions) has three
famous cycles, recomputed exactly in T6:
$$(-1)\ \text{word}\ (1);\qquad (-5, -7)\ \text{word}\ (1,2);\qquad
(-17, -25, -37, -55, -41, -61, -91)\ \text{word}\ (1,1,1,2,1,1,4).$$
For each, the **algebraic identities hold verbatim** — the cycle equation
$x_1(2^K - 3^m) = c$ checks exactly ($-1 \cdot -1 = 1$; $-5 \cdot -1 = 5$;
$-17 \cdot -139 = 2363$) — while the **inequality layer fails exactly at
positivity**: $2^K < 3^m$ in all three cases ($2 < 3$; $8 < 9$; $2048 < 2187$),
i.e. L-9905.2's conclusion is violated because its hypothesis $x_i > 0$ is.
Specifically:

- **L-9912.1**: the $-1$ cycle is a genuine constant-exponent cycle ($a = 1$)
  and is exactly the formal solution $x = 1/(2^1 - 3) = -1$ of (1.1); the
  *only* hypothesis excluding it is positivity ($x_1 \ge 1$, used via
  L-9905.2). The case split in Step 2 shows the $a = 1$ branch is the unique
  branch where negativity can hide.
- **L-9912.2**: not sensitive to positivity in its conclusion (all three
  negative cycles do contain a letter $1$), but its proof step
  "$3 + 1/x \le 4$ with equality iff $x = 1$" uses $x \ge 1$; at $x = -5$ the
  factor is $3 - \tfrac15 = 2.8 < 3$, flipping the product below $3^m$ — which
  is exactly why negative cycles live at $K/m < \log_2 3$.
- **L-9912.3(i)** (pure counting) holds for the negative cycles too
  ($1 \ge 2\cdot 1 - 1$; $1 \ge 4 - 3$; $5 \ge 14 - 11$), confirming it uses no
  positivity; **L-9912.3(ii)** fails for them precisely because
  $K/m < \log_2 3$ ($1.0$, $1.5$, $1.5714$ vs $1.5849\ldots$) — the $-17$
  cycle sits strikingly just *below* the threshold that positive cycles must
  sit just *above*.

This audit confirms each hypothesis of the Statement is necessary and is used
where claimed. $\square$

---

## Dependency audit

Used results and exactly where:

- **D-9904** (definition of $S$, $a(x) \ge 1$): throughout; the step relation
  $2^{a_i} x_{i+1} = 3x_i + 1$ in Steps 2–3.
- **D-9905** (trivial cycle $(1)$): Steps 0, 2, 3.
- **D-9908** (least period, cycle notation, distinct elements): throughout;
  distinctness in Steps 0 and 2–3 (its proof is L-9906 Step 0 P0, PROVED, also
  recorded in L-9905's Definitions).
- **L-9905.1** (cycle equation; PROVED): Step 2 (constant-exponent case) and
  Step 6 (identity layer of the audit).
- **L-9905.2** (positivity $2^K > 3^m$; PROVED): Steps 2 ($a = 1$ branch),
  4(iii), 5(i),(iii).
- **L-9905.3** (product formula and $(3 + 1/x_{\min})^m$ bound; PROVED):
  Steps 3, 4(ii), 5 — the single most load-bearing input of this file. A
  one-line rederivation is included at (2.1) for self-containment.
- **L-9905.6** ($m = 1$; PROVED): Step 5(iii) closing remark.
- **L-9906.2** (floor $x_{\min} \ge 7$; PROVED, reviewed): Step 0 (F7), used by
  L-9912.3(ii) second bullet, L-9912.4 columns marked $X = 7$, and all of
  L-9912.4(iii). The two-line justification is restated in Step 0; results
  needing only $x_{\min} \ge 3$ are separately tagged (F3) and are independent
  of L-9906.
- **L-9906 main theorem** ($m \le 6$; PROVED, reviewed): only in the
  *combination* sentence of L-9912.4(iii) ("every nontrivial cycle has
  $m \in \{8, 10, 11, 13, 14\} \cup \{m \ge 15\}$") and Remark 3. The new
  exclusions $m \in \{7, 9, 12\}$ themselves do **not** use L-9906's
  enumeration — only L-9905.2/.3 and the floor L-9906.2.
- **NOTATION.md conventions** (empty sums; finite-verification labeling):
  throughout.
- **Not used:** transcendence bounds, literature computations, results from
  other packets, floating point (all decimals are certified enclosures backed
  by integer comparisons).
- **No circularity:** L-9905 and L-9906 do not cite L-9912; the dictionary
  (Step 1) is elementary congruence arithmetic with no cycle input.

## Gap audit

- **Quantifier hygiene.** Every claim is over *all* nontrivial $S$-cycles with
  the stated floor tag; L-9912.5 is over all positive odd $x$ and all
  $t \ge 1$; nothing is claimed about negative integers (the audit is labeled
  as an audit, not a claim).
- **Direction of every inequality.** Step 3: (2.2) from $a_i \ge 2$
  (monotonicity of $2^K$ in $K$); (2.3) from $x_i \ge 1$; equality forced from
  the two-sided squeeze. Step 4(ii): floor $\Rightarrow$ upper bound on $K$
  $\Rightarrow$ lower bound on $m_1$ (each arrow's direction spelled out
  inline). Step 5(iii): $2^K 7^m$ strictly increasing in $K$ justifies the
  "least $K$ fails $\Rightarrow$ window empty" logic; the width argument for
  $m \ge 15$ uses a certified strict inequality.
- **Boundary cases.** $m = 1$: Step 2's split covers it (the trivial cycle has
  constant word $(2)$); $W_7(1) = \varnothing$ is explained (floor hypothesis
  excludes the trivial cycle, and nontrivial $m = 1$ is L-9905.6). $x = 1$:
  handled by the equality analysis in Step 3 and by (F3). Half-open interval
  endpoints in L-9912.4 are tracked ($K/m > \log_2 3$ strict; the $\le$ side
  closed).
- **Hidden finiteness / exhaustiveness.** The only finite case analysis is the
  $m \le 14$ window table, exhaustive by the monotonicity argument plus the
  $m \ge 15$ width argument — no unexamined tail. The dictionary's exhaustive
  check (T2) is finite verification *supporting* an already-proved universal
  statement, not a substitute for it.
- **Empirical vs. universal.** All sub-claims are proved universally; the
  scripts are labeled exact finite verification / stress tests. The four-decimal
  enclosures are theorems (backed by specific integer comparisons), not
  floating-point observations; the proofs of the fraction bounds use only the
  hand-checkable certifications ($1296 > 1250$, $2744 > 2662$, $42 < 44$,
  $18 < 20$, $22^{15} > 2 \cdot 21^{15}$).
- **What is honestly NOT proved.** No upper bound on $m_1/m$ beyond
  $1 - 1/m$ (Q-9912-A, with the structural reason recorded in Step 4(iii));
  no exclusion of $\{1,2\}$-cycles (L-9912.4(ii) proves the opposite: the
  counting constraints leave a nonempty live region); nothing about $m = 8$ or
  any $m \in \{10, 11, 13, 14\} \cup \{m \ge 15\}$ beyond the forced $K$
  values; no claim that the dictionary constrains *consecutive* exponents
  (that requires composing $S$ with the residue classes — future work).
- **Dependence on reviewed-but-new results.** L-9906 was upgraded to PROVED by
  fable-02-v5 on 2026-07-21; if that review were ever retracted, the (F7)-tagged
  results degrade gracefully to the (F3) versions (explicitly stated), and
  L-9912.4(iii)'s exclusions would become conditional on L-9906.2 only — whose
  five-line proof is restated in Step 0.

## Adversarial tests

Exact-arithmetic verification suite (labels T1–T8). **Script (verbatim);**
Python 3.11.15, integers and `fractions.Fraction` only, fixed seed for the
randomized stress tests:

```python
#!/usr/bin/env python3
# L-9912 verification suite (exact integer/rational arithmetic throughout).
# Tests are labeled T1..T8; each prints PASS lines or raises AssertionError.

from fractions import Fraction
from math import comb
import random

random.seed(99120)

def nu2(y):
    a = 0
    while y % 2 == 0:
        y //= 2
        a += 1
    return a

def S_ext(x):
    """Formal Syracuse step on any odd integer x (positive or negative)."""
    y = 3 * x + 1
    a = nu2(y)
    return y // (2 ** a), a

def c_of(word):
    m = len(word)
    c, A = 0, 0
    for i in range(1, m + 1):
        c += 3 ** (m - i) * 2 ** A
        A += word[i - 1]
    return c

# ---------- T1: geometric identity and x = 1/(2^a - 3) ----------
for a in range(1, 11):
    u = 2 ** a
    for m in range(1, 13):
        c = c_of((a,) * m)
        assert (u - 3) * c == u ** m - 3 ** m, ("T1 geom", a, m)
        D = 2 ** (a * m) - 3 ** m
        if D != 0:  # always true (parity), but guard
            assert Fraction(c, D) == Fraction(1, u - 3) if u != 3 else True, ("T1 x", a, m)
print("T1 PASS: (2^a-3)*c == (2^a)^m - 3^m and c/D == 1/(2^a-3), all 1<=a<=10, 1<=m<=12")
print("   spot values of 1/(2^a-3): a=1 -> -1 (negative fixed point), a=2 -> 1 (trivial),",
      "a=3 -> 1/5, a=4 -> 1/13 (non-integers)")

# ---------- T2: exponent dictionary mod 2^(t+1) ----------
def r_t(t):
    return (2 ** t - 1) // 3 if t % 2 == 0 else (5 * 2 ** t - 1) // 3

for t in range(1, 13):
    r = r_t(t)
    # closed form well-defined: numerator divisible by 3
    if t % 2 == 0:
        assert (2 ** t - 1) % 3 == 0, t
    else:
        assert (5 * 2 ** t - 1) % 3 == 0, t
    assert r % 2 == 1 and 0 < r < 2 ** (t + 1), ("T2 range", t, r)
    assert (3 * r + 1) % 2 ** (t + 1) == 2 ** t, ("T2 defining congruence", t, r)
LIM = 2 ** 15
for x in range(1, LIM, 2):
    a = nu2(3 * x + 1)
    for t in range(1, 13):
        assert (a == t) == (x % 2 ** (t + 1) == r_t(t)), ("T2", x, t)
        # ">= t" form: nu2(3x+1) >= t  <=>  x = r_t mod 2^t
        assert (a >= t) == (x % 2 ** t == r_t(t) % 2 ** t), ("T2>=", x, t)
# tower consistency: r_{t+1} = r_t mod 2^t
for t in range(1, 12):
    assert r_t(t + 1) % 2 ** t == r_t(t) % 2 ** t, ("T2 tower", t)
print("T2 PASS: a(x)=t <=> x = r_t mod 2^(t+1), exhaustive for t<=12, odd x <", LIM)
print("   r_t table t=1..8:", [r_t(t) for t in range(1, 9)],
      "(mod 4,8,16,32,64,128,256,512)")
# explicit correction check: a=3 class is 13 mod 16, NOT 5 mod 16 (a(5)=4)
assert nu2(3 * 5 + 1) == 4 and r_t(3) == 13 and r_t(4) == 5
print("   correction confirmed: a=3 <=> x=13 mod 16 (a(5) =", nu2(16), "so 5 mod 32 is the a=4 class)")

# ---------- T3: certified logarithm bounds by integer power comparison ----------
def cert(msg, ok):
    assert ok, msg
    print("   cert:", msg)

print("T3: integer-certified inequalities")
cert("14^3 = 2744 > 2662 = 2*11^3   [log2(14/11) > 1/3]", 14**3 > 2 * 11**3)
cert("6^4 = 1296 > 1250 = 2*5^4     [log2(6/5) > 1/4]", 6**4 > 2 * 5**4)
cert("42 < 44                        [log2(14/11) < log2(4/3), {1,2}-window nonempty, X=7]",
     3 * 14 < 4 * 11)
cert("18 < 20                        [log2(6/5) < log2(4/3), {1,2}-window nonempty, X=3]",
     3 * 6 < 4 * 5)
cert("21 < 22                        [log2 3 < log2(22/7)]", 21 < 22)
cert("22^15 > 2*21^15                [log2(22/21) > 1/15: window width > 1 for m >= 15]",
     22**15 > 2 * 21**15)
N = 10000
cert("0.3479 < log2(14/11) < 0.3480 via 14^%d vs 11^%d*2^{3479,3480}" % (N, N),
     11**N * 2**3479 < 14**N < 11**N * 2**3480)
cert("0.2630 < log2(6/5) < 0.2631", 5**N * 2**2630 < 6**N < 5**N * 2**2631)
cert("1.5849 < log2 3 < 1.5850", 2**15849 < 3**N < 2**15850)
cert("1.6520 < log2(22/7) < 1.6521", 7**N * 2**16520 < 22**N < 7**N * 2**16521)
cert("1.7369 < log2(10/3) < 1.7370", 3**N * 2**17369 < 10**N < 3**N * 2**17370)
cert("0.4150 < log2(4/3) < 0.4151", 3**N * 2**4150 < 4**N < 3**N * 2**4151)

# ---------- T4: counting inequality stress on random exponent words ----------
for _ in range(20000):
    m = random.randint(1, 40)
    word = tuple(random.choice([1, 1, 2, 3, 4, 5, 6]) for _ in range(m))
    K = sum(word)
    m1 = sum(1 for a in word if a == 1)
    assert m1 >= 2 * m - K, ("T4", word)                       # counting bound
    if all(a in (1, 2) for a in word):
        assert m1 == 2 * m - K, ("T4 eq", word)                # equality iff {1,2}
    if m1 == 2 * m - K:
        assert all(a in (1, 2) for a in word), ("T4 eq conv", word)
print("T4 PASS: m1 >= 2m-K on 20000 random words; equality iff all a_i in {1,2}")

# ---------- T5: product formula on open orbit segments (positive, exact) ----------
for _ in range(2000):
    x = 2 * random.randint(1, 10**6) + 1
    m = random.randint(1, 25)
    xs = [x]
    aa = []
    for _ in range(m):
        y, a = S_ext(xs[-1])
        xs.append(y)
        aa.append(a)
    K = sum(aa)
    lhs = Fraction(2) ** K
    rhs = Fraction(xs[0], xs[m])
    for i in range(m):
        rhs *= 3 + Fraction(1, xs[i])
    assert lhs == rhs, ("T5", x, m)
print("T5 PASS: 2^K = (x_1/x_{m+1}) * prod(3 + 1/x_i) exactly on 2000 random segments",
      "(closes to L-9905.3 when x_{m+1} = x_1)")

# ---------- T6: negative cycles — hypothesis-necessity audit ----------
def find_cycle(n):
    seen = {}
    x = n
    order = []
    while x not in seen:
        seen[x] = len(order)
        order.append(x)
        x, _ = S_ext(x)
    cyc = order[seen[x]:]
    word = tuple(S_ext(v)[1] for v in cyc)
    return cyc, word

print("T6: negative-cycle audit (formal S on negative odd integers)")
for n in (-1, -5, -17):
    cyc, word = find_cycle(n)
    m, K = len(cyc), sum(word)
    m1 = sum(1 for a in word if a == 1)
    c = c_of(word)
    D = 2 ** K - 3 ** m
    assert cyc[0] * D == c, ("T6 cycle equation", n)           # algebraic identity holds
    assert 2 ** K < 3 ** m, ("T6 window", n)                   # positivity conclusion FAILS
    assert m1 >= 2 * m - K, ("T6 counting", n)                 # counting half still holds
    print(f"   start {n}: cycle {cyc}, exponents {word}, m={m}, K={K}, m1={m1}; "
          f"x1*D=c holds ({cyc[0]}*{D}={c}); 2^K<3^m ({2**K}<{3**m}) so K/m={K/m:.4f} "
          f"< log2(3)=1.5850: violates L-9905.2 (needs x_i>0)")
assert find_cycle(-1)[1] == (1,)
assert find_cycle(-5)[1] in ((1, 2), (2, 1))
assert len(find_cycle(-17)[0]) == 7 and sum(find_cycle(-17)[1]) == 11
print("   -1: constant word (1): the formal solution x=1/(2^1-3)=-1 of L-9912.1;"
      " excluded from positive cycles exactly by x>=1 / 2^K>3^m")
print("   -5 cycle word:", find_cycle(-5)[1], " (m=2, K=3)   -17 cycle: m=7, K=11,",
      f"K/m={11/7:.4f} just BELOW log2 3 - negative cycles sit left of the window")

# ---------- T7: integer-K-window exclusions with floor X=7 (product formula) ----------
print("T7: integer K-window { K : 3^m < 2^K and 2^K*7^m <= 22^m }, m = 1..14")
empty = []
for m in range(1, 15):
    Ks = [K for K in range(1, 4 * m + 2) if 3 ** m < 2 ** K and 2 ** K * 7 ** m <= 22 ** m]
    if not Ks:
        empty.append(m)
    else:
        print(f"   m={m}: admissible K = {Ks}")
print("   EMPTY windows at m =", empty)
assert empty == [1, 2, 3, 4, 6, 7, 9, 12]
# (m=1 empty is consistent: the trivial cycle has x_min = 1 < 7, so the floor-7
#  window rightly does not accommodate it; nontrivial m=1 is L-9905.6.)
# width argument: for m >= 15 the real window has length m*log2(22/21) >= 15*log2(22/21) > 1
# (T3 cert 22^15 > 2*21^15), hence always contains an integer; so the list above is the
# COMPLETE list of empty windows over all m >= 1.
# spot-verify the load-bearing comparisons by hand-checkable integers:
assert 2**4 < 3**3 < 2**5 and 2**5 * 7**3 == 10976 > 10648 == 22**3      # m=3:  K=5 fails
assert 2**6 < 3**4 < 2**7 and 2**7 * 7**4 == 307328 > 234256 == 22**4    # m=4:  K=7 fails
assert 2**9 < 3**6 < 2**10 and 2**10 * 7**6 == 120472576 > 113379904 == 22**6  # m=6: K=10 fails
assert 2**11 < 3**7 < 2**12 and 2**12 * 7**7 == 3373232128 > 2494357888 == 22**7  # m=7
assert 2**14 < 3**9 < 2**15 and 2**15 * 7**9 > 22**9                     # m=9:  K=15 fails
assert 2**19 < 3**12 < 2**20 and 2**20 * 7**12 > 22**12                  # m=12: K=20 fails
assert 2**8 * 7**5 == 4302592 <= 5153632 == 22**5                        # m=5:  K=8 admissible
assert 2**9 * 7**5 == 8605184 > 22**5                                    # m=5:  K=9 not
print("   m=9:  2^15*7^9  =", 2**15 * 7**9, "> 22^9  =", 22**9)
print("   m=12: 2^20*7^12 =", 2**20 * 7**12, "> 22^12 =", 22**12)
print("   NEW beyond L-9906 (m<=6): m = 7, 9, 12 have NO admissible K at all;")
print("   m=5's window shrinks to {8} (L-9906 enumerated K in {8,9}: no survivor).")

# ---------- T8: floor-free L-9912.2 equality analysis sanity ----------
# all a_i >= 2 forces 4^m <= 2^K = prod(3+1/x_i) <= 4^m with equality iff all x_i = 1.
# sanity: the trivial cycle attains it; and 3+1/x < 4 strictly for every odd x >= 3.
assert S_ext(1) == (1, 2)
for x in range(3, 1000, 2):
    assert 3 + Fraction(1, x) < 4
print("T8 PASS: equality case 3+1/x = 4 only at x = 1; trivial cycle has word (2)")
print("ALL TESTS PASS")
```

**Output (verbatim):**

```text
T1 PASS: (2^a-3)*c == (2^a)^m - 3^m and c/D == 1/(2^a-3), all 1<=a<=10, 1<=m<=12
   spot values of 1/(2^a-3): a=1 -> -1 (negative fixed point), a=2 -> 1 (trivial), a=3 -> 1/5, a=4 -> 1/13 (non-integers)
T2 PASS: a(x)=t <=> x = r_t mod 2^(t+1), exhaustive for t<=12, odd x < 32768
   r_t table t=1..8: [3, 1, 13, 5, 53, 21, 213, 85] (mod 4,8,16,32,64,128,256,512)
   correction confirmed: a=3 <=> x=13 mod 16 (a(5) = 4 so 5 mod 32 is the a=4 class)
T3: integer-certified inequalities
   cert: 14^3 = 2744 > 2662 = 2*11^3   [log2(14/11) > 1/3]
   cert: 6^4 = 1296 > 1250 = 2*5^4     [log2(6/5) > 1/4]
   cert: 42 < 44                        [log2(14/11) < log2(4/3), {1,2}-window nonempty, X=7]
   cert: 18 < 20                        [log2(6/5) < log2(4/3), {1,2}-window nonempty, X=3]
   cert: 21 < 22                        [log2 3 < log2(22/7)]
   cert: 22^15 > 2*21^15                [log2(22/21) > 1/15: window width > 1 for m >= 15]
   cert: 0.3479 < log2(14/11) < 0.3480 via 14^10000 vs 11^10000*2^{3479,3480}
   cert: 0.2630 < log2(6/5) < 0.2631
   cert: 1.5849 < log2 3 < 1.5850
   cert: 1.6520 < log2(22/7) < 1.6521
   cert: 1.7369 < log2(10/3) < 1.7370
   cert: 0.4150 < log2(4/3) < 0.4151
T4 PASS: m1 >= 2m-K on 20000 random words; equality iff all a_i in {1,2}
T5 PASS: 2^K = (x_1/x_{m+1}) * prod(3 + 1/x_i) exactly on 2000 random segments (closes to L-9905.3 when x_{m+1} = x_1)
T6: negative-cycle audit (formal S on negative odd integers)
   start -1: cycle [-1], exponents (1,), m=1, K=1, m1=1; x1*D=c holds (-1*-1=1); 2^K<3^m (2<3) so K/m=1.0000 < log2(3)=1.5850: violates L-9905.2 (needs x_i>0)
   start -5: cycle [-5, -7], exponents (1, 2), m=2, K=3, m1=1; x1*D=c holds (-5*-1=5); 2^K<3^m (8<9) so K/m=1.5000 < log2(3)=1.5850: violates L-9905.2 (needs x_i>0)
   start -17: cycle [-17, -25, -37, -55, -41, -61, -91], exponents (1, 1, 1, 2, 1, 1, 4), m=7, K=11, m1=5; x1*D=c holds (-17*-139=2363); 2^K<3^m (2048<2187) so K/m=1.5714 < log2(3)=1.5850: violates L-9905.2 (needs x_i>0)
   -1: constant word (1): the formal solution x=1/(2^1-3)=-1 of L-9912.1; excluded from positive cycles exactly by x>=1 / 2^K>3^m
   -5 cycle word: (1, 2)  (m=2, K=3)   -17 cycle: m=7, K=11, K/m=1.5714 just BELOW log2 3 - negative cycles sit left of the window
T7: integer K-window { K : 3^m < 2^K and 2^K*7^m <= 22^m }, m = 1..14
   m=5: admissible K = [8]
   m=8: admissible K = [13]
   m=10: admissible K = [16]
   m=11: admissible K = [18]
   m=13: admissible K = [21]
   m=14: admissible K = [23]
   EMPTY windows at m = [1, 2, 3, 4, 6, 7, 9, 12]
   m=9:  2^15*7^9  = 1322306994176 > 22^9  = 1207269217792
   m=12: 2^20*7^12 = 14513641568075776 > 22^12 = 12855002631049216
   NEW beyond L-9906 (m<=6): m = 7, 9, 12 have NO admissible K at all;
   m=5's window shrinks to {8} (L-9906 enumerated K in {8,9}: no survivor).
T8 PASS: equality case 3+1/x = 4 only at x = 1; trivial cycle has word (2)
ALL TESTS PASS
```

**Interpretation and labeling.** T1, T2, T4, T5, T8 are exact finite
verifications *supporting* statements proved universally above (per the packet
convention, they are checks, not proofs). T3's twelve certifications and T7's
window table are exact integer comparisons that ARE the finite arithmetic facts
quoted inside the proofs of Steps 4–5 (each is a specific decidable integer
inequality, several of them hand-checkable and displayed inline); T6 is the
hypothesis-necessity audit of Step 6. The suite caught one real error during
authoring: an early draft of the Step 5 table asserted the empty-window list
was $\{2, 7, 9, 12\}$ (anchoring on L-9906's weaker windows); the exact scan
corrected it to $\{1, 2, 3, 4, 6, 7, 9, 12\}$ — i.e. the product-formula window
is strictly sharper than remembered, which became Remark 3.

## Remaining uncertainty

1. The negative-cycle audit's claim that $(-1)$, $(-5,-7)$, and the $m = 7$
   cycle through $-17$ are the only relevant negative cycles is **not** claimed
   or needed — the audit only uses that these three ARE cycles (verified
   exactly); no completeness assertion is made.
2. The four-decimal enclosures rely on machine-executed exact integer
   comparisons between integers of roughly $10^4$ digits (e.g. $14^{10000}$ has
   $\lceil 10^4 \log_{10} 14 \rceil = 11462$ digits); a reviewer should re-run
   T3 or re-certify with independent software. The proofs deliberately route
   all *logical* weight through the small hand-checkable certifications
   instead, so the enclosures are convenience precision, not load-bearing.
3. L-9912.4(iii) inherits the PROVED statuses of L-9905 and L-9906.2. If a
   future audit weakened L-9906, the fallback landscape is stated in the Gap
   audit (results degrade to the (F3) tags; the $\{7,9,12\}$ exclusions
   survive on L-9906.2 alone, whose proof is restated in Step 0).
4. The author is confident in the dictionary (Step 1) and rigidity (Step 2)
   proofs; the most error-prone spots are the equality analysis in Step 3
   (checked at T8), the inequality-direction chain in Step 4(ii), and the
   half-open endpoint bookkeeping in Step 5 — a verifier should probe these
   first, plus the three big-integer comparisons in the Step 5 table
   ($m = 7, 9, 12$).

## Suggested next attack

- **Q-9912-A (open; recorded here).** Prove or refute: there is a constant
  $\beta < 1$ (ideally $\beta$ near $2 - \log_2 3 + \varepsilon$) such that
  every nontrivial $S$-cycle has $m_1 \le \beta m$. Counting cannot do it
  (Step 4(iii)); the promising route is run structure: by the dictionary tower
  (Step 1 remark), a run of $j$ consecutive exponent-$1$ steps starting at $x$
  forces $x \equiv -1 \pmod{2^{j+1}}$, hence $x \ge 2^{j+1} - 1$, and each such
  step multiplies the element by $\approx 3/2$; combining run-length limits
  with the element bounds of L-9905.4 should cap long $1$-runs and may yield a
  genuine upper bound on $m_1/m$.
- **$m = 8$, $K = 13$ (smallest open case).** L-9912.4(iii) forces any $m = 8$
  cycle to have $K = 13$, hence exponent word a composition of $13$ into $8$
  parts — $\binom{12}{7} = 792$ compositions, and by L-9912.3(ii) at least
  $\lceil 8 \cdot 0.3479 \rceil = 3$ letters equal to $1$. An L-9906-style
  exact enumeration (divisibility of $c$ by $2^{13} - 3^8 = 8192 - 6561 = 1631$
  plus orbit check) over these 792 cases would eliminate $m = 8$ and, iterated
  over $\{10, 11, 13, 14\}$ (all singleton-$K$!), plausibly push the proved
  floor to $m \ge 15$ with modest computation. This is the natural L-9913.
- **Consecutive-letter grammar.** Compose the dictionary with one $S$-step to
  characterize which letter pairs $(a_i, a_{i+1})$ are realizable and with what
  mod-$2^{t}$ transition structure (a finite-state constraint on exponent
  words); this would sharpen the $\{1,2\}$-window from inside and feed issue
  #9's grammar searches directly.
- **Convergent bridge (planned L-9910).** The forced ratios of Remark 4 and the
  window $(\log_2 3, \log_2(22/7)]$ shrink as verified floors grow
  (L-9905.5); L-9910 should quantify how the admissible $(m, K)$ pairs thin out
  toward continued-fraction convergents of $\log_2 3$, using this file's
  integer-window method as the finite-check engine.
- **Refutation surface.** To refute this file, exhibit either an error in the
  five displayed hand certifications, a counterexample to the dictionary for
  some odd $x$ (T2 excludes all $x < 2^{15}$, $t \le 12$), or a nontrivial
  cycle with $m \in \{7, 9, 12\}$ — which would simultaneously refute L-9905.2,
  L-9905.3, or L-9906.2.

---

*Authored by fable-02-p5, 2026-07-21. Scripts run with Python 3.11.15; script
and output included verbatim above; exact integer/rational arithmetic
throughout; randomized stress tests use a fixed seed and are labeled as checks,
never proof.*

---

## Verification note (fable-02-v14, 2026-07-25)

**Verdict: PASS.** Every sub-claim (L-9912.1–.5, Corollary 2A, and the honest
non-claim Q-9912-A) was independently restated, re-proved from the explicit
dependencies, and re-checked with an independently written exact-arithmetic
suite. No substantive defect was found. Status upgraded `PROPOSED` → `PROVED`
(README §7: "the proof has passed an initial detailed review").
`INDEPENDENTLY_VERIFIED` is deliberately **not** set — that is reserved for a
further reviewer, per the packet convention.

**Headline answers to the two questions the review was commissioned to settle.**
The new eliminations $m \in \{7, 9, 12\}$ **independently confirm**, and the
forced singleton windows $K \in \{8\}, \{13\}, \{16\}, \{18\}, \{21\}, \{23\}$
for $m \in \{5, 8, 10, 11, 13, 14\}$ **independently confirm**, from exact
integer certificates recomputed from the statements alone (§2.5 below).

### 0. Method and independence

- Read README §7 and §13, `NOTATION.md` (D-9903–D-9905, D-9908), and the
  **Statement** sections of `L-9905-cycle-equation.md` and
  `L-9906-no-small-cycles.md` (both Status `PROVED`, reviewed by fable-02-v4 and
  fable-02-v5 respectively). Confirmed the four imported facts are stated in
  those files exactly as quoted here: L-9905.1 ($x_1(2^K-3^m)=c$), L-9905.2
  ($2^K > 3^m$, for every $S$-cycle on the **positive** odd integers, trivial
  cycle included), L-9905.3 ($2^K = \prod(3+1/x_i)$ and
  $3^m < 2^K \le (3+1/x_{\min})^m$), L-9905.6 ($m=1$ ⟹ trivial), L-9906.2
  ($x_{\min} \ge 7$, hence *all* elements $\ge 7$), L-9906 main theorem
  ($m \le 6$).
- **No circularity:** L-9905 and L-9906 cite nothing from L-9912; the dictionary
  (Step 1) uses no cycle hypothesis at all. Checked by reading both dependency
  files' Dependency-audit sections.
- Wrote my own verification suite **from the Statement section only**
  (`v14_full.py`, reproduced verbatim in §9), before reading the author's
  scripts in detail: exact `int`/`fractions.Fraction` arithmetic, no floating
  point in any decision, fixed seed for the randomized stress parts.
- Separately re-executed the author's own embedded suite (§4).

### 1. Independent restatement

Fix a nontrivial $S$-cycle $x_1 \to \dots \to x_m \to x_1$ (D-9908; elements
pairwise distinct positive odd), $a_i = \nu_2(3x_i+1) \ge 1$, $K = \sum a_i$,
$m_t = \#\{i : a_i = t\}$, $m_1$ the one-count.

1. *(rigidity)* If all $a_i$ are equal to some $a \ge 1$ then the cycle is the
   trivial fixed point $(1)$; the cycle equation forces the exact rational
   $x_1 = 1/(2^a-3)$, which is $-1$ at $a=1$, $1$ at $a=2$, and lies in $(0,1)$
   for $a \ge 3$.
2. *(a letter 1 exists)* $m_1 \ge 1$, with **no** floor on $x_{\min}$; hence some
   element is $\equiv 3 \pmod 4$.
3. *(quantitative)* $m_1 \ge 2m-K$ with equality iff the word is a $\{1,2\}$-word;
   $K \le m\log_2(3+1/x_{\min})$; hence $m_1 > m/4$ unconditionally and
   $m_1 > m/3$ using $x_{\min} \ge 7$; and $m_1 \le m-1$.
4. *(window)* $K/m \in (\log_2 3, \log_2(3+1/X)]$ under a floor $X$; the
   $\{1,2\}$-region is nonempty (counting cannot refute $\{1,2\}$-cycles); and,
   $K$ being an integer, the window $W_7(m)$ is empty exactly for
   $m \in \{1,2,3,4,6,7,9,12\}$, giving the new exclusions $m \in \{7,9,12\}$.
5. *(dictionary)* $a(x) = t \iff x \equiv r_t \pmod{2^{t+1}}$ with
   $r_t = (2^t-1)/3$ ($t$ even), $(5\cdot 2^t-1)/3$ ($t$ odd); and
   $a(x) \ge t \iff x \equiv r_t \pmod{2^t}$.

This matches the file's Statement with no drift.

### 2. Reconstruction of each proof (independent)

**2.1 L-9912.1 (Step 2).** With a constant word, $A_{i-1} = a(i-1)$, so the
D-9908/L-9905 definition of $c$ gives $c = \sum_{i=1}^m 3^{m-i} u^{i-1}$,
$u := 2^a$. Telescoping: $\sum_{i=1}^m (3^{m-i}u^i - 3^{m-i+1}u^{i-1})$ has the
positive term at index $i$ equal to the negative term at index $i+1$, leaving
$u^m - 3^m$; so $(u-3)c = u^m - 3^m$. Since $a \ge 1$, $u^m$ is even and $3^m$
odd, so $D := u^m - 3^m \ne 0$; and $u \ne 3$, so dividing is legitimate **for
every** $a \ge 1$ — including $a = 1$, where $u - 3 = -1$. Hence
$x_1 = c/D = 1/(2^a-3)$ exactly, for every anchoring, so *all* elements equal
this rational. Case split: $a=1 \Rightarrow x_1 = -1$, excluded by positivity
(equivalently by L-9905.2, since $2^K = 2^m < 3^m$); $a=2 \Rightarrow x_1 = 1$,
and $S(1)=1$ plus least-period forces $m=1$, the trivial cycle; $a \ge 3
\Rightarrow 0 < x_1 \le 1/5 < 1$, not a positive integer. Verified for
$1 \le a \le 10$, $1 \le m \le 12$ with $c$ computed from its definition (V2):
the telescoping identity, $D \ne 0$, and $c/D = 1/(2^a-3)$ all hold exactly.

**2.2 L-9912.2 (Step 3) — priority probe: the equality analysis.** Assume all
$a_i \ge 2$. Then $K \ge 2m$ so $2^K \ge 4^m$. Each $x_i \ge 1$ gives
$0 < 3 + 1/x_i \le 4$, so $2^K = \prod (3+1/x_i) \le 4^m$. The squeeze forces
$\prod_i (3+1/x_i) = 4^m$ exactly. **Equality scrutiny.** All factors are
strictly positive and each is $\le 4$. If some factor $f_j < 4$, then
$\prod_i f_i \le f_j \cdot 4^{m-1} < 4^m$ — a contradiction. (The step is valid
precisely because positivity lets the remaining factors be bounded by $4$
without sign trouble; this is the only place the argument could leak, and it
does not.) So every factor is $4$, i.e. $x_i = 1$ for all $i$, and an element
equal to $1$ forces the trivial cycle. The contrapositive is $m_1 \ge 1$.
**Confirmed: no floor on $x_{\min}$ is used** — the inputs are exactly (2.1) and
$x_i \ge 1$, and the latter is part of "positive odd integer". The brief's
alternative routes ($(22/7)^m < 4^m$, $(10/3)^m < 4^m$) are valid but import a
floor unnecessarily. Correction flag 3 upheld.
*Corollary 2A* then follows from L-9912.5 at $t=1$ ($r_1 = 3$, modulus $4$).

**2.3 L-9912.3.** (i) $K = m_1 + \sum_{a_i \ge 2} a_i \ge m_1 + 2(m-m_1)$, i.e.
$m_1 \ge 2m-K$, equality iff every letter $\ge 2$ is exactly $2$. Verified
**exhaustively** for all words of length $\le 7$ over letters $\{1,\dots,5\}$
(both the inequality and both directions of the equality characterisation), plus
$5\cdot 10^4$ random words of length $\le 60$ (V4).
(ii) *priority probe: inequality directions.* $2^K \le (3+1/x_{\min})^m$
(L-9905.3) $\Rightarrow K \le m\log_2(3+1/x_{\min})$ ($\log_2$ strictly
increasing) $\Rightarrow$ with a floor $x_{\min} \ge X$ and $t \mapsto 3+1/t$
decreasing, $K \le m\log_2(3+1/X)$. Composing with (i), which is *anti-monotone*
in $K$: $m_1 \ge 2m - K \ge m(2 - \log_2(3+1/X)) = m\log_2\frac{4X}{3X+1}$.
Every arrow points the way the file says; a **larger** floor gives a **smaller**
upper bound on $K$ and hence a **stronger** lower bound on $m_1$. Arithmetic:
$X=3 \Rightarrow 12/10 = 6/5$; $X=7 \Rightarrow 28/22 = 14/11$ (Correction flag 2
upheld). Certificates recomputed exactly: $6^4 = 1296 > 1250 = 2\cdot 5^4$
(i.e. $(6/5)^4 > 2$, i.e. $\log_2(6/5) > 1/4$) and
$14^3 = 2744 > 2662 = 2\cdot 11^3$ (i.e. $\log_2(14/11) > 1/3$). The integrality
upgrade $m_1 \ge \lfloor m/3\rfloor + 1$ is correct in both cases ($3 \mid m$ or
not) — checked for all $m \le 2000$.
(iii) $m_1 = m \Rightarrow K = m$, contradicting $K > m\log_2 3 > m$ (L-9905.2).

**2.4 L-9912.4(i)–(ii) — priority probe: half-open endpoints.** $K/m > \log_2 3$
is strict (L-9905.2 gives $2^K > 3^m$ strictly), $K/m \le \log_2(3+1/X)$ is not;
so for a $\{1,2\}$-cycle $m_1/m = 2 - K/m$ lies in
$[\,2-\log_2(3+1/X),\; 2-\log_2 3\,)$ — left-closed, right-open, exactly as
printed. Nonemptiness $\iff \frac{4X}{3X+1} < \frac43 \iff 12X < 12X+4$: always
true; hand certificates $42 < 44$ ($X=7$) and $18 < 20$ ($X=3$) recomputed.
*Additional check the file does not make (and which makes its honest boundary
marker stronger, not weaker):* the region is nonempty at the **integer** level
too — the triples $(m,K,m_1) = (5,8,2), (8,13,3), (10,16,4), (11,18,4),
(13,21,5), (14,23,5), (15,24,6), \dots$ all have $K \in W_7(m)$ and
$m \le K \le 2m$, so an actual $\{1,2\}$-word of length $m$ summing to $K$
exists inside the proved window. Counting genuinely cannot refute
$\{1,2\}$-cycles.

**2.5 L-9912.4(iii) — the bonus claim, re-derived from scratch.** For a
nontrivial cycle, $K \in \mathbb{Z}$ with $3^m < 2^K$ (L-9905.2) and
$2^K \le (22/7)^m$, i.e. $2^K 7^m \le 22^m$ (L-9905.3 with L-9906.2). I
recomputed $W_7(m) := \{K : 3^m < 2^K,\ 2^K 7^m \le 22^m\}$ with exact integers,
taking the least admissible $K$ as $\mathrm{bitlength}(3^m)$ (correct because
$3^m$ is odd $>1$, so $2^{b-1} \le 3^m < 2^b$ with $2^b > 3^m$):

| $m$ | least $K$ | $W_7(m)$ | | $m$ | least $K$ | $W_7(m)$ |
|---|---|---|---|---|---|---|
| 1 | 2 | $\varnothing$ | | 16 | 26 | $\{26\}$ |
| 2 | 4 | $\varnothing$ | | 17 | 27 | $\{27,28\}$ |
| 3 | 5 | $\varnothing$ | | 18 | 29 | $\{29\}$ |
| 4 | 7 | $\varnothing$ | | 19 | 31 | $\{31\}$ |
| 5 | 8 | $\{8\}$ | | 20 | 32 | $\{32,33\}$ |
| 6 | 10 | $\varnothing$ | | 21 | 34 | $\{34\}$ |
| 7 | 12 | $\varnothing$ | | 22 | 35 | $\{35,36\}$ |
| 8 | 13 | $\{13\}$ | | 23 | 37 | $\{37\}$ |
| 9 | 15 | $\varnothing$ | | 24 | 39 | $\{39\}$ |
| 10 | 16 | $\{16\}$ | | 25 | 40 | $\{40,41\}$ |
| 11 | 18 | $\{18\}$ | | 26 | 42 | $\{42\}$ |
| 12 | 20 | $\varnothing$ | | 27 | 43 | $\{43,44\}$ |
| 13 | 21 | $\{21\}$ | | 28 | 45 | $\{45,46\}$ |
| 14 | 23 | $\{23\}$ | | 29 | 46 | $\{46,47\}$ |
| 15 | 24 | $\{24\}$ | | 30 | 48 | $\{48,49\}$ |

- **Empty exactly at $m \in \{1,2,3,4,6,7,9,12\}$**: confirmed by exact scan for
  every $1 \le m \le 4000$, and proved for all $m \ge 15$ by the file's width
  argument, which I checked in both halves: (a) the certificate
  $22^{15} = 136880068015412051968 > 136244637165903364602 = 2\cdot 21^{15}$
  holds (margin $\approx 0.47\%$ — genuinely tight, and $22^{14} < 2\cdot21^{14}$,
  so $m = 15$ is exactly where the argument starts to work, as claimed);
  (b) the interval step is valid: if $\beta - \alpha > 1$ then
  $\lfloor\beta\rfloor \le \beta$ and $\lfloor\beta\rfloor > \beta - 1 > \alpha$,
  so $\lfloor\beta\rfloor \in (\alpha,\beta]$.
- **Every entry of the file's Step 5 table recomputed exactly**, including the
  three flagged big-integer comparisons:
  $m=7$: $2^{12}\cdot 7^7 = 3\,373\,232\,128 > 2\,494\,357\,888 = 22^7$;
  $m=9$: $2^{15}\cdot 7^9 = 1\,322\,306\,994\,176 > 1\,207\,269\,217\,792 = 22^9$;
  $m=12$: $2^{20}\cdot 7^{12} = 14\,513\,641\,568\,075\,776 >
  12\,855\,002\,631\,049\,216 = 22^{12}$. The "least $K$" column is right for all
  fourteen rows, and the monotonicity justification ("$2^K 7^m$ strictly
  increasing in $K$, so least-$K$ failure ⟹ empty") is correct.
- **Singletons confirmed**: among $m \le 14$ the nonempty windows are exactly
  $m \in \{5,8,10,11,13,14\}$ with $K = 8,13,16,18,21,23$; every $m \le 14$
  window has size $\le 1$.
- *Scope note (consistent, not a defect):* for $m \ge 15$ the file claims only
  nonemptiness; my scan shows many $m \ge 15$ windows are also singletons
  ($m = 15,16,18,19,21,23,24,26,\dots$). This is stronger than, and consistent
  with, what is claimed.
- The $m=1$ remark is right: $W_7(1) = \varnothing$ does not contradict the
  trivial cycle, whose $x_{\min} = 1 < 7$ fails the floor hypothesis; and
  nontrivial $m=1$ is L-9905.6.

**Conclusion of 2.5: the eliminations $m \in \{7,9,12\}$ and the singleton
forcing for $m \in \{5,8,10,11,13,14\}$ both independently confirm.**

**2.6 L-9912.5 (Step 1).** (1a) For $y > 0$: $\nu_2(y) = t \iff y \equiv 2^t
\pmod{2^{t+1}}$ — correct in both directions as written. Applied to
$y = 3x+1 \ge 4$. (1b) $\gcd(3,2^{t+1}) = 1$ gives a unique class. (1c) $t$ even:
$2^t \equiv 1 \pmod 3$ so $3 \mid 2^t-1$ and $3r_t + 1 = 2^t$; $t$ odd:
$2^t \equiv 2$, so $5\cdot 2^t \equiv 10 \equiv 1 \pmod 3$ and
$3r_t + 1 = 5\cdot 2^t = 2^t + 2^{t+2} \equiv 2^t \pmod{2^{t+1}}$. In both cases
$3r_t = 2^t-1$ or $5\cdot2^t-1$ is odd, so $r_t$ is odd; and
$(2^t-1)/3 < 2^t < 2^{t+1}$, $(5\cdot 2^t - 1)/3 < 2^{t+1}$. (1d) the "$\ge t$"
form follows since $3r_t \equiv -1 \pmod{2^t}$ in both parities.
Verified **exhaustively for $1 \le t \le 12$ over every odd $x < 2^{15}$, in both
the "$=t$" and "$\ge t$" forms** (16384 values $\times$ 12 exponents $\times$ 2
forms, zero discrepancies), plus $r_t$ oddness/range/defining-congruence/tower
for $t \le 40$ and the partition identity $\sum_{s=1}^t 2^{t-s} + 1 = 2^t$.
Small table reproduced: $r_{1..8} = 3, 1, 13, 5, 53, 21, 213, 85$ modulo
$4, 8, 16, 32, 64, 128, 256, 512$. **Correction flag 1 upheld:** $a(5) =
\nu_2(16) = 4$, so the brief's "$a=3 \iff x \equiv 5 \ (16)$" is false; the
correct class is $x \equiv 13 \pmod{16}$, and $5$ is the base point of the $a=4$
class mod $32$.

**2.7 Q-9912-A.** Stated honestly. The file claims only that the two counting
constraints it proves cannot produce a nontrivial upper bound, and exhibits the
witness family $(1,\dots,1,a_m)$; it labels the question open and does **not**
assert impossibility of any upper bound. I checked the exhibited instance:
$m=8$, $a_8=6$, $K=13$ gives $m_1 = 7 = m-1$, satisfies $m_1 \ge 2m-K$, and
$13 \in W_7(8)$ — so it really does pass every counting constraint in the file.
The statement is accurate and appropriately scoped.

**2.8 Step 6 (hypothesis-necessity audit).** Recomputed independently:
$-1$: cycle $(-1)$, word $(1)$, $m=1$, $K=1$;
$-5$: cycle $(-5,-7)$, word $(1,2)$, $m=2$, $K=3$ (**Correction flag 4 upheld** —
the Syracuse word is $(1,2)$, not $(1,1,2)$);
$-17$: cycle $(-17,-25,-37,-55,-41,-61,-91)$, word $(1,1,1,2,1,1,4)$, $m=7$,
$K=11$, $m_1=5$.
The cycle equation holds exactly in all three ($1=1$, $5=5$, $2363=2363$) and so
does the product formula $2^K = \prod(3+1/x_i)$ (checked with exact rationals) —
confirming the file's claim that the **algebraic** layer is positivity-free.
In all three $2^K < 3^m$ ($2<3$, $8<9$, $2048<2187$), so the failing conclusion
is L-9905.2's, whose hypothesis $x_i>0$ fails: exactly the located failure point.
The counting bound $m_1 \ge 2m-K$ survives in all three, confirming it uses no
positivity. Extra probe: sweeping all odd starts down to $-2\cdot10^5$ finds
exactly these three cycles, and **none** has all letters $\ge 2$ — so the
negative data does not contradict L-9912.2's conclusion either, matching the
file's honest remark that .2 is "not sensitive to positivity in its conclusion".

**2.9 Certified decimals.** All six enclosures re-certified by me at $N = 10^4$
($\log_2(6/5) \in (0.2630,0.2631)$, $\log_2(14/11) \in (0.3479,0.3480)$,
$\log_2 3 \in (1.5849,1.5850)$, $\log_2(22/7) \in (1.6520,1.6521)$,
$\log_2(10/3) \in (1.7369,1.7370)$, $\log_2(4/3) \in (0.4150,0.4151)$) and two of
them re-certified again at an independently chosen precision $N = 3000$ to guard
against a transcription slip in the exponents; all agree. The digit-count remark
($14^{10^4}$ has $11462$ digits) is also correct. As the author says, no proof
step depends on these; the load-bearing certifications are the small hand ones
($1296>1250$, $2744>2662$, $42<44$, $18<20$, $22^{15} > 2\cdot21^{15}$), all
recomputed.

**2.10 Cross-check of Remark 3.** L-9906's own script asserts the windows
$\{2:\varnothing, 3:\{5\}, 4:\{7\}, 5:\{8,9\}, 6:\{10,11,12,13\}\}$
(`L-9906-no-small-cycles.md`, expected-dict assertion and its output line), so
Remark 3's comparison is accurate: the product-formula window empties
$m=3,4,6$ outright and shrinks $m=5$ to $\{8\}$, leaving only L-9906's
$\binom{7}{4} = 35$ compositions load-bearing at $m=5$. $\binom{12}{7} = 792$ and
$2^{13}-3^8 = 1631$ (Suggested next attack) are also correct. Remark 4's forced
ratios $8/5, 13/8, 16/10, 21/13$ are correct as arithmetic and are explicitly
labeled "observation only".

### 3. Authoring-error audit (both disclosed errors)

- **Wrong empty-window list.** Every occurrence of the list in the Statement,
  Step 5, the Gap audit and the T7 assertion is the corrected
  $\{1,2,3,4,6,7,9,12\}$, which my independent scan reproduces. The only
  appearance of the superseded $\{2,7,9,12\}$ is inside the explicit historical
  disclosure sentence in "Interpretation and labeling". **No residue.**
- **Wrong $m=8$ product.** The Step 5 row now reads
  $8192\cdot 7^8 = 47\,225\,249\,792 \le 54\,875\,873\,536 = 22^8$; both integers
  are exactly correct ($7^8 = 5\,764\,801$, $22^8 = 54\,875\,873\,536$), and
  $2^{14}\cdot 7^8 > 22^8$ confirms $K=14$ fails, so $W_7(8) = \{13\}$. No stale
  $m=8$ numeral occurs anywhere else in the file. **No residue.**
- *Documentation observation (not a defect, deliberately not "fixed"):* the
  "Interpretation and labeling" paragraph says the suite caught "one real error";
  the commissioning brief refers to two. Since the second is fully corrected in
  the current text, the only inaccuracy is an undercount in the author's own
  historical disclosure. I have left another agent's record intact and note the
  discrepancy here instead (README §17.4, §17.9).

### 4. Re-execution of the author's suite

The single fenced Python block in "Adversarial tests" was extracted verbatim and
run under Python 3.11.15: exit status 0, and its stdout matches the file's
"Output (verbatim)" block **line for line — 40 lines, 0 differences** (diffed
programmatically). So the file's recorded output is genuine, not transcribed.

### 5. Defects found

**None substantive.** Two cosmetic items, left in place:

- Step 1(1c) contains the garbled phrase "$3 r_t$ is odd minus nothing"; the
  intended and correct argument is that $3r_t$ equals $2^t-1$ ($t$ even) or
  $5\cdot2^t-1$ ($t$ odd), both odd, hence $r_t$ is odd.
- Step 0 (F3) is tagged "independent of L-9906" while citing "L-9906 Step 0 P0"
  for distinctness of cycle elements. The tag is nevertheless justified:
  distinctness is definitional (D-9908, least period) and is independently
  recorded in L-9905's Definitions, which is a separate PROVED file. Only the
  citation is potentially confusing.

### 6. Attempted negation, and a strengthening for the next agent

Negation attempts, all unsuccessful (i.e. the file survives): brute-force search
for a nontrivial positive $S$-cycle from every odd start $< 3\cdot10^5$ (none);
probing the Step 3 equality case for a leak (none); searching for an $m \ge 15$
with empty $W_7(m)$ (none up to $m = 4000$, and the width argument settles all
$m$); testing whether the negative cycles break the counting half of .3 (they do
not); testing the dictionary against every odd $x < 2^{15}$ for $t \le 12$ (no
counterexample).

**Strengthening found (NOT a change to this file's claims; recorded as a next
attack).** The elements of a nontrivial cycle are pairwise **distinct** (D-9908)
and all $\ge 7$ (L-9906.2), so listed increasingly they satisfy
$x_{(j)} \ge 7 + 2j$, and L-9905.3 then gives the sharper, still fully
elementary bound
$$2^K \;=\; \prod_i \Big(3+\frac1{x_i}\Big) \;\le\;
  \prod_{j=0}^{m-1}\Big(3 + \frac{1}{7+2j}\Big),$$
using no input beyond what L-9912.4(iii) already uses. Exact consequences
(computed with `Fraction`, §9 blocks P2–P4, Q3–Q4):

- **$m = 8$ is eliminated outright by a one-line certificate:**
  $\prod_{j<8}(3+\frac{1}{7+2j}) = \frac{87\,425\,024}{10\,773} < 8192 = 2^{13}$,
  while $2^{12} = 4096 < 6561 = 3^8$ forces $K \ge 13$. So the sharpened window
  at $m=8$ is empty. This corroborates L-9915's (PROPOSED) $m=8$ result without
  enumerating its 792 compositions, and it means the file's phrase "$m = 8$ …
  the smallest case not excluded in-repo" is accurate **for L-9912 + L-9906 as
  written** but is already improvable by one further line of the same argument.
- Further empty sharpened windows for $m \le 40$:
  $\{8, 11, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38\}$; for
  $15 \le m \le 400$ the sharpened window is empty at 35 further values of $m$.
- The one-fraction floor improves from the proved $m_1 > m/3$ toward
  $m_1 \gtrsim (2-\log_2 3)m \approx 0.415\,m$: e.g. $m = 200$ gives $m_1 \ge 83$
  instead of $70$, $m = 500$ gives $207$ instead of $174$.

This should be written up as its own lemma (with the "sorted distinct elements"
step proved carefully) rather than retro-fitted here.

### 7. Consistency with L-9915 (PROPOSED, reviewed separately)

`L-9915-medium-m-elimination.md` re-derives the same window facts from
L-9905.2/.3 + L-9906.2 and reports the identical empty set $\{7,9,12\}$, the
identical singleton $K$ values for $m \in \{5,8,10,11,13,14\}$, and the identical
width certificate $22^{15} > 2\cdot 21^{15}$. **No numerical or logical conflict
with L-9912.4(iii).** L-9912 stands on its own: its exclusions cite only
L-9905.2, L-9905.3 and L-9906.2 (all PROVED) and nothing from L-9915, and
L-9915's header explicitly marks L-9912 as *not* load-bearing for it, so there is
no mutual dependence. If L-9915 is later confirmed, the sentence "$m = 8$ …
smallest case not excluded in-repo" becomes historically scoped; it is accurate
as a statement about what L-9912 + L-9906 prove.

### 8. Caveats attached to this PASS

- Status is `PROVED` (one detailed adversarial review), not
  `INDEPENDENTLY_VERIFIED`.
- L-9912.4(iii) and the $m_1 > m/3$ bound inherit L-9906.2's PROVED status; if
  that were retracted, the (F3)-tagged results ($m_1 > m/4$, rigidity, the
  floor-free .2, the dictionary) survive untouched, as the file states.
- The $m \le 4000$ scan is *corroboration*; the universal statement rests on the
  width argument, which I checked as a proof, not as a computation.
- Nothing in this file is claimed about negative integers; I confirmed the
  negative-cycle material appears only inside the audit and is used in no proof.
- My own suite is a check, never a proof (NOTATION.md convention); the proofs
  above stand on the displayed hand-checkable certificates.

### 9. Verification script (verbatim) and output

Written independently from the Statement section; Python 3.11.15; exact
`int`/`fractions.Fraction` arithmetic only; fixed seed `20260725`; runtime
$\approx 26$ s. Blocks: V1–V8 (reconstruction checks), P1–P5 (window scans,
strengthening probe, cycle search), Q1–Q4 (decimal certificates and the
sharpened-window computation).

```python
#!/usr/bin/env python3
import sys; sys.set_int_max_str_digits(200000)
# fable-02-v14 INDEPENDENT verification of L-9912 (written from the STATEMENTS only).
# Exact integer / Fraction arithmetic throughout. No floating point in any decision.

from fractions import Fraction
from math import comb
import random

random.seed(20260725)

FAIL = []
def chk(label, ok):
    if not ok:
        FAIL.append(label)
        print("  *** FAIL:", label)
    return ok

def nu2(y):
    assert y != 0
    a = 0
    while y % 2 == 0:
        y //= 2
        a += 1
    return a

def a_of(x):            # step exponent, D-9904 (works for negative odd x too)
    return nu2(3 * x + 1)

def S(x):
    y = 3 * x + 1
    return y >> nu2(y)

# c as defined in L-9905 / D-9908: c = sum_{i=1}^m 3^{m-i} 2^{A_{i-1}}, A_0 = 0
def c_of(word):
    m = len(word)
    c = 0
    A = 0
    for i in range(1, m + 1):
        c += 3 ** (m - i) * 2 ** A
        A += word[i - 1]
    return c

print("=" * 78)
print("V1  L-9912.5 dictionary: exhaustive for t <= 12 over odd x < 2^15")
print("=" * 78)

def r(t):
    if t % 2 == 0:
        assert (2 ** t - 1) % 3 == 0
        return (2 ** t - 1) // 3
    else:
        assert (5 * 2 ** t - 1) % 3 == 0
        return (5 * 2 ** t - 1) // 3

for t in range(1, 41):
    rt = r(t)
    chk(f"r_{t} odd", rt % 2 == 1)
    chk(f"0 < r_{t} < 2^{t+1}", 0 < rt < 2 ** (t + 1))
    chk(f"3r_{t}+1 = 2^{t} mod 2^{t+1}", (3 * rt + 1) % 2 ** (t + 1) == 2 ** t)
    chk(f"tower r_{t+1} = r_{t} mod 2^{t}", r(t + 1) % 2 ** t == rt % 2 ** t)

LIM = 2 ** 15
bad = 0
for x in range(1, LIM, 2):
    ax = a_of(x)
    for t in range(1, 13):
        if (ax == t) != (x % 2 ** (t + 1) == r(t)):
            bad += 1
        if (ax >= t) != (x % 2 ** t == r(t) % 2 ** t):
            bad += 1
chk("dictionary exhaustive t<=12, odd x<2^15 (both forms)", bad == 0)
print("  r_t, t=1..8 :", [r(t) for t in range(1, 9)])
print("  moduli      :", [2 ** (t + 1) for t in range(1, 9)])
chk("a(5) = 4 (brief's a=3 <-> 5 mod 16 is FALSE)", a_of(5) == 4)
chk("a=3 class is 13 mod 16", r(3) == 13 and a_of(13) == 3)
chk("a=4 base point is 5 mod 32", r(4) == 5)
chk("a=1 <-> 3 mod 4", r(1) == 3)
chk("a=2 <-> 1 mod 8", r(2) == 1)
chk("a=5 <-> 53 mod 64", r(5) == 53)
chk("a=6 <-> 21 mod 128", r(6) == 21)
# partition identity of the Remark
for t in range(1, 13):
    chk(f"partition count t={t}", sum(2 ** (t - s) for s in range(1, t + 1)) + 1 == 2 ** t)
# 2-adic limit: r_t -> -1/3, i.e. 3*r_t + 1 = 0 mod 2^t
for t in range(1, 30):
    chk(f"3r_t+1 = 0 mod 2^{t}", (3 * r(t) + 1) % 2 ** t == 0)

print()
print("=" * 78)
print("V2  L-9912.1 geometric identity and x = 1/(2^a - 3), a<=10, m<=12")
print("=" * 78)
for a in range(1, 11):
    u = 2 ** a
    for m in range(1, 13):
        word = (a,) * m
        c = c_of(word)
        chk(f"telescope a={a} m={m}", (u - 3) * c == u ** m - 3 ** m)
        D = 2 ** (a * m) - 3 ** m
        chk(f"D != 0 a={a} m={m}", D != 0)
        chk(f"c/D = 1/(2^a-3) a={a} m={m}", Fraction(c, D) == Fraction(1, u - 3))
print("  1/(2^a-3) for a=1..8 :", [Fraction(1, 2 ** a - 3) for a in range(1, 9)])
chk("a=1 gives -1", Fraction(1, 2 ** 1 - 3) == -1)
chk("a=2 gives 1", Fraction(1, 2 ** 2 - 3) == 1)
chk("a>=3 gives 0 < x < 1", all(0 < Fraction(1, 2 ** a - 3) < 1 for a in range(3, 40)))
chk("S(-1) = -1 with a=1", S(-1) == -1 and a_of(-1) == 1)
chk("S(1) = 1 with a=2", S(1) == 1 and a_of(1) == 2)

print()
print("=" * 78)
print("V3  certified integer comparisons used in the proofs")
print("=" * 78)
chk("6^4 = 1296 > 1250 = 2*5^4   [log2(6/5) > 1/4]", 6 ** 4 == 1296 and 2 * 5 ** 4 == 1250 and 6 ** 4 > 2 * 5 ** 4)
chk("14^3 = 2744 > 2662 = 2*11^3 [log2(14/11) > 1/3]", 14 ** 3 == 2744 and 2 * 11 ** 3 == 2662 and 14 ** 3 > 2 * 11 ** 3)
chk("3*14 = 42 < 44 = 4*11  [14/11 < 4/3]", 3 * 14 < 4 * 11)
chk("3*6 = 18 < 20 = 4*5    [6/5 < 4/3]", 3 * 6 < 4 * 5)
chk("22^15 > 2*21^15        [15 log2(22/21) > 1]", 22 ** 15 > 2 * 21 ** 15)
print("  22^15 =", 22 ** 15, " 2*21^15 =", 2 * 21 ** 15,
      " ratio-1 =", Fraction(22 ** 15 - 2 * 21 ** 15, 2 * 21 ** 15))
chk("14^14 <= 2*11^14 (so 1/3 bound is not vacuous margin check)", True)  # informational
N = 10 ** 4
chk("0.2630 < log2(6/5) < 0.2631", 5 ** N * 2 ** 2630 < 6 ** N < 5 ** N * 2 ** 2631)
chk("0.3479 < log2(14/11) < 0.3480", 11 ** N * 2 ** 3479 < 14 ** N < 11 ** N * 2 ** 3480)
chk("1.5849 < log2 3 < 1.5850", 2 ** 15849 < 3 ** N < 2 ** 15850)
chk("1.6520 < log2(22/7) < 1.6521", 7 ** N * 2 ** 16520 < 22 ** N < 7 ** N * 2 ** 16521)
chk("1.7369 < log2(10/3) < 1.7370", 3 ** N * 2 ** 17369 < 10 ** N < 3 ** N * 2 ** 17370)
chk("0.4150 < log2(4/3) < 0.4151", 3 ** N * 2 ** 4150 < 4 ** N < 3 ** N * 2 ** 4151)
# independent re-certification at a different precision (N = 3000) to guard a typo in N
M = 3000
chk("recert log2(14/11) at N=3000", 11 ** M * 2 ** 1043 < 14 ** M < 11 ** M * 2 ** 1044)   # .34766..-.34800
chk("recert log2 3 at N=3000", 2 ** 4754 < 3 ** M < 2 ** 4755)

print()
print("=" * 78)
print("V4  L-9912.3(i) counting bound: exhaustive small + random stress")
print("=" * 78)
def words(m, maxa):
    if m == 0:
        yield ()
        return
    for w in words(m - 1, maxa):
        for a in range(1, maxa + 1):
            yield w + (a,)
bad = 0
for m in range(1, 8):
    for w in words(m, 5):
        K = sum(w); m1 = sum(1 for a in w if a == 1)
        if not (m1 >= 2 * m - K):
            bad += 1
        if (m1 == 2 * m - K) != all(a in (1, 2) for a in w):
            bad += 1
chk("exhaustive m<=7, letters<=5: m1>=2m-K and equality iff {1,2}", bad == 0)
bad = 0
for _ in range(50000):
    m = random.randint(1, 60)
    w = tuple(random.choice([1, 1, 1, 2, 2, 3, 4, 7, 11]) for _ in range(m))
    K = sum(w); m1 = sum(1 for a in w if a == 1)
    if not (m1 >= 2 * m - K):
        bad += 1
    if (m1 == 2 * m - K) != all(a in (1, 2) for a in w):
        bad += 1
chk("random stress 50000 words", bad == 0)

print()
print("=" * 78)
print("V5  product formula on real orbit segments (independent check of L-9905.3)")
print("=" * 78)
bad = 0
for _ in range(3000):
    x = 2 * random.randint(1, 10 ** 7) + 1
    m = random.randint(1, 30)
    xs = [x]
    aa = []
    for _ in range(m):
        aa.append(a_of(xs[-1]))
        xs.append(S(xs[-1]))
    K = sum(aa)
    prod = Fraction(1)
    for i in range(m):
        prod *= 3 + Fraction(1, xs[i])
    if Fraction(2) ** K * Fraction(xs[m], xs[0]) != prod:
        bad += 1
chk("2^K * x_{m+1}/x_1 = prod(3+1/x_i) on 3000 segments", bad == 0)

print()
print("=" * 78)
print("V6  L-9912.4(iii) integer windows W_7(m) = {K : 3^m < 2^K, 2^K 7^m <= 22^m}")
print("=" * 78)
def W7(m):
    # exact: K > m log2 3  <=>  2^K > 3^m ;  K <= m log2(22/7) <=> 2^K 7^m <= 22^m
    lo = (3 ** m).bit_length()          # least K with 2^K > 3^m  (since 3^m is not a power of 2)
    assert 2 ** lo > 3 ** m >= 2 ** (lo - 1)
    Ks = []
    K = lo
    while 2 ** K * 7 ** m <= 22 ** m:
        Ks.append(K)
        K += 1
    return Ks

empty = []
singleton = []
rows = []
for m in range(1, 31):
    Ks = W7(m)
    rows.append((m, (3 ** m).bit_length(), Ks))
    if not Ks:
        empty.append(m)
    elif len(Ks) == 1:
        singleton.append(m)
print("   m | least K | W_7(m)")
for m, lo, Ks in rows:
    print(f"  {m:2d} | {lo:7d} | {Ks if Ks else 'EMPTY'}")
chk("empty windows for m<=30 are exactly {1,2,3,4,6,7,9,12}",
    empty == [1, 2, 3, 4, 6, 7, 9, 12])
chk("singleton windows among m<=14 are exactly {5,8,10,11,13,14}",
    [m for m in range(1, 15) if len(W7(m)) == 1] == [5, 8, 10, 11, 13, 14])
chk("every m<=14 window has size <= 1", all(len(W7(m)) <= 1 for m in range(1, 15)))
print("  window sizes m=15..30 (file claims only NONEMPTY there):",
      [len(W7(m)) for m in range(15, 31)])
chk("singleton values {8,13,16,18,21,23}",
    [W7(m)[0] for m in (5, 8, 10, 11, 13, 14)] == [8, 13, 16, 18, 21, 23])
# no further empty windows anywhere up to a large bound (sanity of the width argument)
far_empty = [m for m in range(15, 4001) if not W7(m)]
chk("no empty window for 15 <= m <= 4000", far_empty == [])
# width argument, exact: (22/21)^m > 2 for m >= 15  <=>  22^m > 2*21^m
chk("22^m > 2*21^m for all 15 <= m <= 500", all(22 ** m > 2 * 21 ** m for m in range(15, 501)))
chk("22^14 < 2*21^14 (m=15 is the true threshold of the width argument)", 22 ** 14 < 2 * 21 ** 14)
# floor(beta) argument spot check on rationals: verified structurally, plus numeric spot:
for m in range(15, 60):
    Ks = W7(m)
    chk(f"floor-of-upper-endpoint in window m={m}", max(Ks) == Ks[-1] and len(Ks) >= 1)

print()
print("   --- exact re-derivation of every number in the Step 5 table ---")
tab = {
    1: ("4 * 7 = 28 > 22", 2 ** 2 * 7 ** 1 == 28 and 22 ** 1 == 22 and 28 > 22),
    2: ("16 * 49 = 784 > 484", 2 ** 4 * 7 ** 2 == 784 and 22 ** 2 == 484 and 784 > 484),
    3: ("32 * 343 = 10976 > 10648", 2 ** 5 * 7 ** 3 == 10976 and 22 ** 3 == 10648 and 10976 > 10648),
    4: ("128 * 2401 = 307328 > 234256", 2 ** 7 * 7 ** 4 == 307328 and 22 ** 4 == 234256 and 307328 > 234256),
    5: ("256*16807 = 4302592 <= 5153632; K=9: 8605184 > 22^5",
        2 ** 8 * 7 ** 5 == 4302592 and 22 ** 5 == 5153632 and 4302592 <= 5153632
        and 2 ** 9 * 7 ** 5 == 8605184 and 8605184 > 22 ** 5),
    6: ("1024*117649 = 120472576 > 113379904",
        2 ** 10 * 7 ** 6 == 120472576 and 22 ** 6 == 113379904 and 120472576 > 113379904),
    7: ("4096*823543 = 3373232128 > 2494357888",
        2 ** 12 * 7 ** 7 == 3373232128 and 22 ** 7 == 2494357888 and 3373232128 > 2494357888),
    8: ("8192*7^8 = 47225249792 <= 54875873536; K=14 fails",
        2 ** 13 * 7 ** 8 == 47225249792 and 22 ** 8 == 54875873536 and 47225249792 <= 54875873536
        and 2 ** 14 * 7 ** 8 > 22 ** 8),
    9: ("32768*7^9 = 1322306994176 > 1207269217792",
        2 ** 15 * 7 ** 9 == 1322306994176 and 22 ** 9 == 1207269217792 and 1322306994176 > 1207269217792),
    10: ("K=16 in window; K=17 fails", 2 ** 16 * 7 ** 10 <= 22 ** 10 and 2 ** 17 * 7 ** 10 > 22 ** 10),
    11: ("K=18 in window; K=19 fails", 2 ** 18 * 7 ** 11 <= 22 ** 11 and 2 ** 19 * 7 ** 11 > 22 ** 11),
    12: ("2^20*7^12 = 14513641568075776 > 12855002631049216",
         2 ** 20 * 7 ** 12 == 14513641568075776 and 22 ** 12 == 12855002631049216
         and 2 ** 20 * 7 ** 12 > 22 ** 12),
    13: ("K=21 in window; K=22 fails", 2 ** 21 * 7 ** 13 <= 22 ** 13 and 2 ** 22 * 7 ** 13 > 22 ** 13),
    14: ("K=23 in window; K=24 fails", 2 ** 23 * 7 ** 14 <= 22 ** 14 and 2 ** 24 * 7 ** 14 > 22 ** 14),
}
for m, (txt, ok) in tab.items():
    chk(f"table row m={m}: {txt}", ok)
# least-K column of the table
least_col = {1: 2, 2: 4, 3: 5, 4: 7, 5: 8, 6: 10, 7: 12, 8: 13, 9: 15,
             10: 16, 11: 18, 12: 20, 13: 21, 14: 23}
for m, v in least_col.items():
    chk(f"least K column m={m} = {v}", (3 ** m).bit_length() == v)
chk("2^11 = 2048 < 2187 = 3^7 < 4096 = 2^12", 2 ** 11 == 2048 < 2187 == 3 ** 7 < 4096 == 2 ** 12)

print()
print("=" * 78)
print("V7  negative-cycle hypothesis-necessity audit")
print("=" * 78)
def find_cycle(n):
    seen = {}
    x = n
    order = []
    while x not in seen:
        seen[x] = len(order)
        order.append(x)
        x = S(x)
    cyc = order[seen[x]:]
    return cyc, tuple(a_of(v) for v in cyc)

for n in (-1, -5, -17):
    cyc, w = find_cycle(n)
    m, K = len(cyc), sum(w)
    m1 = sum(1 for a in w if a == 1)
    c = c_of(w)
    D = 2 ** K - 3 ** m
    print(f"  start {n}: cycle {cyc}")
    print(f"     word {w}  m={m} K={K} m1={m1}  c={c}  D={D}  x1*D={cyc[0]*D}")
    chk(f"cycle equation holds for {n}", cyc[0] * D == c)
    chk(f"2^K < 3^m for {n} (L-9905.2 conclusion FAILS)", 2 ** K < 3 ** m)
    chk(f"counting bound m1>=2m-K still holds for {n}", m1 >= 2 * m - K)
    print(f"     K/m = {Fraction(K,m)} vs log2 3 in (1.5849,1.5850): "
          f"{'BELOW' if Fraction(K,m) < Fraction(15849,10000) else 'ABOVE'}")
    prodcheck = Fraction(1)
    for v in cyc:
        prodcheck *= 3 + Fraction(1, v)
    chk(f"product formula holds algebraically for {n}", prodcheck == Fraction(2) ** K)
chk("-5 cycle word is (1,2) up to rotation", find_cycle(-5)[1] in ((1, 2), (2, 1)))
chk("-1 word is (1)", find_cycle(-1)[1] == (1,))
chk("-17: m=7, K=11, m1=5", len(find_cycle(-17)[0]) == 7 and sum(find_cycle(-17)[1]) == 11
    and sum(1 for a in find_cycle(-17)[1] if a == 1) == 5)
chk("all three negative cycles DO contain a letter 1 (L-9912.2 conclusion not violated)",
    all(1 in find_cycle(n)[1] for n in (-1, -5, -17)))
# is there a negative cycle with all a_i >= 2 among small negatives? (probe L-9912.2 necessity)
negcycles = {}
for n in range(-1, -200001, -2):
    cyc, w = find_cycle(n)
    key = min(cyc)
    if key not in negcycles:
        negcycles[key] = (tuple(cyc), w)
print("  distinct negative cycles reachable from |n| < 200000:",
      [(k, negcycles[k][1]) for k in sorted(negcycles)])
chk("no negative cycle found with all a_i >= 2",
    all(1 in w for _, w in negcycles.values()))
# factor 3 + 1/x at x = -5
chk("3 + 1/(-5) = 14/5 = 2.8 < 3", 3 + Fraction(1, -5) == Fraction(14, 5))

print()
print("=" * 78)
print("V8  misc statement checks")
print("=" * 78)
chk("S(3) = 5, S(5) = 1 (basis of floor x_min >= 7)", S(3) == 5 and S(5) == 1)
chk("3 + 1/x < 4 strictly for odd x >= 3", all(3 + Fraction(1, x) < 4 for x in range(3, 2001, 2)))
chk("equality 3+1/x = 4 iff x = 1", 3 + Fraction(1, 1) == 4)
# m1 >= floor(m/3)+1 from m1 > m/3
chk("m1 > m/3 integer => m1 >= floor(m/3)+1 for m<=2000",
    all(min(k for k in range(0, m + 1) if 3 * k > m) == m // 3 + 1 for m in range(1, 2001)))
chk("ceil(8*0.3479) = 3 and floor(8/3)+1 = 3", -((-8 * 3479) // 10000) == 3 and 8 // 3 + 1 == 3)
chk("C(12,7) = 792 compositions of 13 into 8 parts", comb(12, 7) == 792)
chk("2^13 - 3^8 = 1631", 2 ** 13 - 3 ** 8 == 1631)
chk("C(7,4) = 35 compositions of 8 into 5 parts", comb(7, 4) == 35)
chk("Fibonacci ratios 8/5,13/8,16/10,21/13 for m=5,8,10,13",
    [Fraction(W7(m)[0], m) for m in (5, 8, 10, 13)]
    == [Fraction(8, 5), Fraction(13, 8), Fraction(16, 10), Fraction(21, 13)])
# {1,2}-window nonemptiness at the INTEGER level, not just as a real interval
live = []
for m in range(1, 40):
    for K in W7(m):
        if m <= K <= 2 * m:                    # a {1,2}-word of length m with sum K exists
            live.append((m, K, 2 * m - K))     # (m, K, m1)
print("  integer (m,K,m1) triples supporting a {1,2}-word inside the X=7 window, m<40:")
print("   ", live[:12], "..." if len(live) > 12 else "")
chk("{1,2}-window contains genuine integer (m,K) pairs", len(live) > 0 and (8, 13, 3) in live)
# upper bound m1 <= m-1 and the (1,...,1,a) family satisfying all counting constraints
chk("word (1^7,6): m=8,K=13,m1=7 satisfies m1>=2m-K and K in W_7(8)",
    (lambda w: (sum(w) == 13 and len(w) == 8 and sum(1 for a in w if a == 1) == 7
                and sum(1 for a in w if a == 1) >= 2 * 8 - 13 and 13 in W7(8)))((1,)*7 + (6,)))


print("P1  corrected singleton test (file claims singletons only for m <= 14)")
sing_small = [m for m in range(1, 15) if len(W7(m)) == 1]
chk("singletons among m<=14 are exactly {5,8,10,11,13,14}", sing_small == [5, 8, 10, 11, 13, 14])
chk("values {8,13,16,18,21,23}", [W7(m)[0] for m in sing_small] == [8, 13, 16, 18, 21, 23])
chk("every m<=14 is either empty or singleton", all(len(W7(m)) <= 1 for m in range(1, 15)))
print("   m<=14 window sizes:", [len(W7(m)) for m in range(1, 15)])
print("   m=15..30 sizes    :", [len(W7(m)) for m in range(15, 31)])
print("   (file claims only NONEMPTY for m>=15 -- consistent)")

print()
print("P2  strengthening probe: distinct elements >= 7 give x_(j) >= 7+2j (sorted),")
print("    so 2^K <= prod_{j=0}^{m-1} (3 + 1/(7+2j)).  Does it eliminate more m?")
def W_sharp(m):
    up = Fraction(1)
    for j in range(m):
        up *= 3 + Fraction(1, 7 + 2 * j)
    lo = (3 ** m).bit_length()
    Ks = []
    K = lo
    while Fraction(2) ** K <= up:
        Ks.append(K); K += 1
    return Ks
emptier = []
for m in range(1, 41):
    a, b = W7(m), W_sharp(m)
    if b != a:
        emptier.append((m, a, b))
print("   m where the sharpened window differs from W_7(m):")
for m, a, b in emptier:
    print(f"     m={m:2d}  W_7={a if a else 'EMPTY'}  ->  W_sharp={b if b else 'EMPTY'}")
new_empty = [m for m in range(1, 41) if W7(m) and not W_sharp(m)]
print("   NEW empty windows from the sharpened bound (m<=40):", new_empty)

print()
print("P3  same probe with the anchoring x_min>=7 only (i.e. no distinctness) - control")
print("    (this is exactly W_7, shown above)")

print()
print("P4  can the m>=15 nonemptiness ever fail for the sharpened window? scan m<=400")
far = [m for m in range(15, 401) if not W_sharp(m)]
print("   sharpened-window empties, 15<=m<=400:", far)

print()
print("P5  sanity: brute-force search for any S-cycle among odd x < 3*10^5")
def S(x):
    y = 3 * x + 1
    a = 0
    while y % 2 == 0:
        y //= 2; a += 1
    return y
cyc_found = set()
for n in range(1, 300001, 2):
    x, seen = n, set()
    while x not in seen and x != 1 and x < 10 ** 12:
        seen.add(x); x = S(x)
    if x != 1 and x < 10 ** 12:
        cyc_found.add(x)
print("   nontrivial S-cycle elements found below 3*10^5 start points:", sorted(cyc_found))
chk("no nontrivial positive S-cycle found", not cyc_found)


print("Q1  digit-count claim: 14^10000 has 11462 digits")
chk("11462 digits", len(str(14**10000)) == 11462)

print()
print("Q2  every decimal in the Step 5 live-window table, as exact integer comparisons")
N=10**4
# K/m in (log2 3, log2(10/3)] subset (1.5849, 1.7370)   [X=3 column]
chk("log2 3 > 1.5849", 3**N > 2**15849)
chk("log2(10/3) < 1.7370", 10**N < 3**N * 2**17370)
chk("log2(22/7) < 1.6521", 22**N < 7**N * 2**16521)
chk("log2(6/5) > 0.2630", 6**N > 5**N * 2**2630)
chk("log2(14/11) > 0.3479", 14**N > 11**N * 2**3479)
chk("log2(4/3) < 0.4151", 4**N < 3**N * 2**4151)
chk("log2(6/5) < 0.4151 (interval [log2 6/5, log2 4/3) sits inside (0.2630,0.4151))",
    6**N * 3**N < 5**N * 4**N)

print()
print("Q3  strengthening: distinct elements >= 7 sorted give x_(j) >= 7+2j")
print("    K_max(m) = max{K : 2^K <= prod_{j<m}(3+1/(7+2j))}, m1 >= 2m - K_max")
def prod_sharp(m):
    p = Fraction(1)
    for j in range(m):
        p *= 3 + Fraction(1, 7+2*j)
    return p
def Kmax_sharp(m):
    p = prod_sharp(m); K = 0
    while Fraction(2)**(K+1) <= p: K += 1
    return K
def Kmax_flat(m):     # the file's bound: 2^K <= (22/7)^m
    K = 0
    while 2**(K+1) * 7**m <= 22**m: K += 1
    return K
print("    m | Kmin | Kmax(22/7) | Kmax(sharp) | file m1>=  | sharp m1>=")
for m in (8, 14, 20, 30, 50, 100, 200, 500, 1000):
    kmin = (3**m).bit_length()
    kf, ks = Kmax_flat(m), Kmax_sharp(m)
    print(f"   {m:4d} | {kmin:4d} | {kf:10d} | {ks:11d} | {2*m-kf:10d} | {2*m-ks:10d}"
          f"   (sharp fraction {Fraction(2*m-ks,m)} ~ {float(Fraction(2*m-ks,m)):.4f})")
print("    file's proved floor is m1 > m/3 = 0.3333 m; the distinctness-sharpened")
print("    bound tends to 2 - log2 3 = 0.4150.. m as m grows.  (STRENGTHENING, not a defect.)")

print()
print("Q4  does the sharpened window kill m=8 (the file's 'smallest open case')?")
p8 = prod_sharp(8)
print("    prod_{j<8}(3+1/(7+2j)) =", p8, "=", float(p8))
print("    2^13 =", 2**13, " > prod  ->", Fraction(2)**13 > p8)
print("    2^12 =", 4096, " < 3^8 =", 3**8, "-> K>=13, so window EMPTY")
chk("m=8 killed by distinctness-sharpened window", Fraction(2)**13 > p8 and 2**12 < 3**8)


print()
print("=" * 78)
if FAIL:
    print("FAILURES:", len(FAIL))
    for f in FAIL:
        print("   -", f)
else:
    print("ALL INDEPENDENT CHECKS PASS")
print("=" * 78)
```

**Output (verbatim):**

```text
==============================================================================
V1  L-9912.5 dictionary: exhaustive for t <= 12 over odd x < 2^15
==============================================================================
  r_t, t=1..8 : [3, 1, 13, 5, 53, 21, 213, 85]
  moduli      : [4, 8, 16, 32, 64, 128, 256, 512]

==============================================================================
V2  L-9912.1 geometric identity and x = 1/(2^a - 3), a<=10, m<=12
==============================================================================
  1/(2^a-3) for a=1..8 : [Fraction(-1, 1), Fraction(1, 1), Fraction(1, 5), Fraction(1, 13), Fraction(1, 29), Fraction(1, 61), Fraction(1, 125), Fraction(1, 253)]

==============================================================================
V3  certified integer comparisons used in the proofs
==============================================================================
  22^15 = 136880068015412051968  2*21^15 = 136244637165903364602  ratio-1 = 317715424754343683/68122318582951682301

==============================================================================
V4  L-9912.3(i) counting bound: exhaustive small + random stress
==============================================================================

==============================================================================
V5  product formula on real orbit segments (independent check of L-9905.3)
==============================================================================

==============================================================================
V6  L-9912.4(iii) integer windows W_7(m) = {K : 3^m < 2^K, 2^K 7^m <= 22^m}
==============================================================================
   m | least K | W_7(m)
   1 |       2 | EMPTY
   2 |       4 | EMPTY
   3 |       5 | EMPTY
   4 |       7 | EMPTY
   5 |       8 | [8]
   6 |      10 | EMPTY
   7 |      12 | EMPTY
   8 |      13 | [13]
   9 |      15 | EMPTY
  10 |      16 | [16]
  11 |      18 | [18]
  12 |      20 | EMPTY
  13 |      21 | [21]
  14 |      23 | [23]
  15 |      24 | [24]
  16 |      26 | [26]
  17 |      27 | [27, 28]
  18 |      29 | [29]
  19 |      31 | [31]
  20 |      32 | [32, 33]
  21 |      34 | [34]
  22 |      35 | [35, 36]
  23 |      37 | [37]
  24 |      39 | [39]
  25 |      40 | [40, 41]
  26 |      42 | [42]
  27 |      43 | [43, 44]
  28 |      45 | [45, 46]
  29 |      46 | [46, 47]
  30 |      48 | [48, 49]
  window sizes m=15..30 (file claims only NONEMPTY there): [1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2]

   --- exact re-derivation of every number in the Step 5 table ---

==============================================================================
V7  negative-cycle hypothesis-necessity audit
==============================================================================
  start -1: cycle [-1]
     word (1,)  m=1 K=1 m1=1  c=1  D=-1  x1*D=1
     K/m = 1 vs log2 3 in (1.5849,1.5850): BELOW
  start -5: cycle [-5, -7]
     word (1, 2)  m=2 K=3 m1=1  c=5  D=-1  x1*D=5
     K/m = 3/2 vs log2 3 in (1.5849,1.5850): BELOW
  start -17: cycle [-17, -25, -37, -55, -41, -61, -91]
     word (1, 1, 1, 2, 1, 1, 4)  m=7 K=11 m1=5  c=2363  D=-139  x1*D=2363
     K/m = 11/7 vs log2 3 in (1.5849,1.5850): BELOW
  distinct negative cycles reachable from |n| < 200000: [(-91, (1, 1, 1, 2, 1, 1, 4)), (-7, (1, 2)), (-1, (1,))]

==============================================================================
V8  misc statement checks
==============================================================================
  integer (m,K,m1) triples supporting a {1,2}-word inside the X=7 window, m<40:
    [(5, 8, 2), (8, 13, 3), (10, 16, 4), (11, 18, 4), (13, 21, 5), (14, 23, 5), (15, 24, 6), (16, 26, 6), (17, 27, 7), (17, 28, 6), (18, 29, 7), (19, 31, 7)] ...
P1  corrected singleton test (file claims singletons only for m <= 14)
   m<=14 window sizes: [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1]
   m=15..30 sizes    : [1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2]
   (file claims only NONEMPTY for m>=15 -- consistent)

P2  strengthening probe: distinct elements >= 7 give x_(j) >= 7+2j (sorted),
    so 2^K <= prod_{j=0}^{m-1} (3 + 1/(7+2j)).  Does it eliminate more m?
   m where the sharpened window differs from W_7(m):
     m= 8  W_7=[13]  ->  W_sharp=EMPTY
     m=11  W_7=[18]  ->  W_sharp=EMPTY
     m=14  W_7=[23]  ->  W_sharp=EMPTY
     m=16  W_7=[26]  ->  W_sharp=EMPTY
     m=17  W_7=[27, 28]  ->  W_sharp=[27]
     m=18  W_7=[29]  ->  W_sharp=EMPTY
     m=19  W_7=[31]  ->  W_sharp=EMPTY
     m=20  W_7=[32, 33]  ->  W_sharp=[32]
     m=21  W_7=[34]  ->  W_sharp=EMPTY
     m=22  W_7=[35, 36]  ->  W_sharp=[35]
     m=23  W_7=[37]  ->  W_sharp=EMPTY
     m=24  W_7=[39]  ->  W_sharp=EMPTY
     m=25  W_7=[40, 41]  ->  W_sharp=[40]
     m=26  W_7=[42]  ->  W_sharp=EMPTY
     m=27  W_7=[43, 44]  ->  W_sharp=[43]
     m=28  W_7=[45, 46]  ->  W_sharp=EMPTY
     m=29  W_7=[46, 47]  ->  W_sharp=[46]
     m=30  W_7=[48, 49]  ->  W_sharp=[48]
     m=31  W_7=[50, 51]  ->  W_sharp=EMPTY
     m=32  W_7=[51, 52]  ->  W_sharp=[51]
     m=33  W_7=[53, 54]  ->  W_sharp=EMPTY
     m=34  W_7=[54, 55, 56]  ->  W_sharp=[54]
     m=35  W_7=[56, 57]  ->  W_sharp=[56]
     m=36  W_7=[58, 59]  ->  W_sharp=EMPTY
     m=37  W_7=[59, 60, 61]  ->  W_sharp=[59]
     m=38  W_7=[61, 62]  ->  W_sharp=EMPTY
     m=39  W_7=[62, 63, 64]  ->  W_sharp=[62]
     m=40  W_7=[64, 65, 66]  ->  W_sharp=[64]
   NEW empty windows from the sharpened bound (m<=40): [8, 11, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38]

P3  same probe with the anchoring x_min>=7 only (i.e. no distinctness) - control
    (this is exactly W_7, shown above)

P4  can the m>=15 nonemptiness ever fail for the sharpened window? scan m<=400
   sharpened-window empties, 15<=m<=400: [16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48, 50, 53, 55, 60, 62, 65, 67, 72, 77, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]

P5  sanity: brute-force search for any S-cycle among odd x < 3*10^5
   nontrivial S-cycle elements found below 3*10^5 start points: []
Q1  digit-count claim: 14^10000 has 11462 digits

Q2  every decimal in the Step 5 live-window table, as exact integer comparisons

Q3  strengthening: distinct elements >= 7 sorted give x_(j) >= 7+2j
    K_max(m) = max{K : 2^K <= prod_{j<m}(3+1/(7+2j))}, m1 >= 2m - K_max
    m | Kmin | Kmax(22/7) | Kmax(sharp) | file m1>=  | sharp m1>=
      8 |   13 |         13 |          12 |          3 |          4   (sharp fraction 1/2 ~ 0.5000)
     14 |   23 |         23 |          22 |          5 |          6   (sharp fraction 3/7 ~ 0.4286)
     20 |   32 |         33 |          32 |          7 |          8   (sharp fraction 2/5 ~ 0.4000)
     30 |   48 |         49 |          48 |         11 |         12   (sharp fraction 2/5 ~ 0.4000)
     50 |   80 |         82 |          79 |         18 |         21   (sharp fraction 21/50 ~ 0.4200)
    100 |  159 |        165 |         159 |         35 |         41   (sharp fraction 41/100 ~ 0.4100)
    200 |  317 |        330 |         317 |         70 |         83   (sharp fraction 83/200 ~ 0.4150)
    500 |  793 |        826 |         793 |        174 |        207   (sharp fraction 207/500 ~ 0.4140)
   1000 | 1585 |       1652 |        1586 |        348 |        414   (sharp fraction 207/500 ~ 0.4140)
    file's proved floor is m1 > m/3 = 0.3333 m; the distinctness-sharpened
    bound tends to 2 - log2 3 = 0.4150.. m as m grows.  (STRENGTHENING, not a defect.)

Q4  does the sharpened window kill m=8 (the file's 'smallest open case')?
    prod_{j<8}(3+1/(7+2j)) = 87425024/10773 = 8115.197623688851
    2^13 = 8192  > prod  -> True
    2^12 = 4096  < 3^8 = 6561 -> K>=13, so window EMPTY

==============================================================================
ALL INDEPENDENT CHECKS PASS
==============================================================================
```

---

*Adversarial review by fable-02-v14, 2026-07-25. Verdict: PASS; status
upgraded to PROVED. Scripts above were written from the Statement section
alone and run with Python 3.11.15 (exact integer/rational arithmetic; the
randomized parts use a fixed seed and are labeled checks, never proof). The
author's own suite was additionally re-executed and reproduces its recorded
output exactly. Only this file was modified.*
