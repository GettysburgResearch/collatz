# L-9918 — Extraction barriers for cylinder architectures: the adic/archimedean asymmetry, the sign criterion, and the discrepancy collision

```text
Claim ID:      L-9918
Title:         Cylinder architectures at full generality: (A) the extraction
               theorem, the always-nonempty M-adic limit, the uniform-witness
               repair, a Collatz-native architecture with empty archimedean
               intersection, and the positivity/sign criterion for periodic
               addresses; (B) a universal lower bound for harmonic cusp sums,
               the exact admissible region of Erdos-Turan constant pairs, the
               undecidability of extraction in general, and the generalized
               Parseval obstruction.
Status:        PROVED
Authoring agent:   fable-02-p12
Reviewing agents:  fable-02-v20 (adversarial review 2026-07-25: PASS)
Created:       2026-07-25
Last updated:  2026-07-25 (fable-02-v20: adversarial review; six documented
               fixes, none load-bearing; see the Verification note at the end)
Dependencies:  research/foundations/NOTATION.md (D-9902 shortcut map T, D-9906
               parity vector, D-9907 bounded/divergent, conventions: Z^+, nu_2,
               Z_(2), empty sums/products, status semantics, "computation is
               finite verification").
               EVERYTHING ELSE IS RE-PROVED INLINE. In particular the parity
               locality/realization facts, the Fejer-kernel positivity, the
               Erdos-Turan-shape inequalities, the Parseval identities and the
               sign criterion are all constructed from scratch below.
               L-9904 (PROVED) and L-9916 (PROPOSED, under review) are cited as
               CONTEXT ONLY and are never used; the relationship of each result
               here to its specialized ancestor is recorded in the Dependency
               audit.
Scope:         All integers M >= 2; all cylinder architectures in the sense of
               D-9918.1; all N >= 0; all finite point multisets on R/Z; all
               integers H >= 1; all constant pairs (C_1, C_2) in (0, infinity)^2.
               Statements are fully quantified and every constant is explicit.
               L-9918.9 (undecidability) concerns arbitrary COMPUTABLY PRESENTED
               architectures and says nothing about any specific one.
               All tables marked (E) are EMPIRICAL finite verification.
               Q-9918 is an OPEN QUESTION with no direction claimed.
Related counterexample candidates: none.
```

---

## 0. Summary of what is and is not proved

**Proved here, in full generality (complete arguments in the Proof section).**

* **L-9918.1 (extraction normalisation).** For every cylinder architecture:
  $\bigcap_N S_N \neq \emptyset \iff \sup_N m_N < \infty \iff (m_N)$ eventually constant;
  and the negations: $\bigcap_N S_N = \emptyset \iff m_N \to \infty \iff$ every fixed
  positive integer is eventually excluded. Exactly which hypothesis each implication
  consumes is recorded.
* **L-9918.2 (the asymmetry).** $\bigcap_N \widehat S_N \neq \emptyset$ **always**
  ($\widehat S_N$ = closure in $\mathbb{Z}_M$), and
  $\bigcap_N S_N = \big(\bigcap_N \widehat S_N\big) \cap \mathbb{Z}^+$. The $M$-adic limit
  always exists; the archimedean one need not.
* **L-9918.3 (the exact repair).** The inference
  "$\forall N \exists x_N \in S_N \Rightarrow \exists x\, \forall N\, x \in S_N$" is valid
  **iff** the witnesses admit a uniform bound. Both directions proved.
* **L-9918.4 (canonical counterexample).** The parity word $(1110)^\infty$ for the shortcut
  map: every finite prefix has infinitely many positive-integer representatives, the unique
  $2$-adic realiser is $-19/11$, and $\bigcap_N S_N = \emptyset$ with $m_N \to \infty$.
  Proved from scratch, with the exact $4$-cycle of rationals.
* **L-9918.5 (sign criterion at generality).** In an affine architecture the unique adic
  realiser of a periodic address $w^\infty$ is $\kappa_w/(M^p - A_w)$, a rational whose
  denominator divides $M^p - A_w \neq 0$; it is a positive integer only if the architecture
  is **subcritical** on $w$ ($A_w < M^p$). Hence every **supercritical** architecture — what
  every divergence-hunting programme builds — has no periodic seeds, and any seed has a
  not-even-eventually-periodic address.
* **L-9918.6 (universal cusp lower bound).** For **every** multiset of $R \ge 1$ points on
  $\mathbb{R}/\mathbb{Z}$ and **every** integer $H \ge 1$:
  $\sum_{h \le H} h^{-1}|S(h)| \ge \tfrac12\log(H/R)$, with the sharper
  $\tfrac12(\log(H/R) + 1/H)$ when $H \ge R$. Survived a hostile quantifier audit; the
  hypothesis $H \ge R$ of the specialised ancestor is **not** needed.
* **L-9918.7 (the collision; admissible constant region).** For any Erdős–Turán-shape
  criterion with data $(C_1, C_2, \varphi)$, firing forces
  $C_1\varphi(H)R/H < 1$ **and** $C_1\varphi(uR)/u + \tfrac{C_2}{2}(\log u)_+ < 1$ with
  $u = H/R$. With $\varphi \equiv 1$ the criterion is satisfiable for some $u$ **iff**
  $[\,C_2 < 2$ and $C_1 < \Psi(C_2) := \tfrac{C_2}{2}e^{2/C_2 - 1}\,]$ or
  $[\,C_2 \ge 2$ and $C_1 < 1\,]$. Elementary Fejér-power constants
  $(4, 2/\pi, \log(4H))$ are unsatisfiable for **every** $R \ge 1$; and $(4, 2/\pi)$ is
  unsatisfiable even with $\varphi \equiv 1$, so removing the logarithm is necessary but
  **not** sufficient.
* **L-9918.8 (generalised Parseval).** Every $d$-element digit set has digit-sum mean square
  exactly $d$; the product of per-level mean squares equals the global mean square exactly,
  so per-level average information yields **no** decay.
* **L-9918.9 (undecidability).** Deciding $\bigcap_N S_N \ne \emptyset$ for computably
  presented architectures is undecidable — already for $M = 2$ and $R_N = 1$. Hence no
  method using only the architecture's counting/refinement data can decide extraction; the
  arithmetic of the specific digit set is not a convenience but a necessity.

**Not proved / open.** Whether $\bigcap_N S_N$ is empty for **any** of the exhibited
architectures. Q-9918 records precise arithmetic replacement targets. Nothing here bears on
the Collatz conjecture itself.

**Prominent honesty flag.** Part B is a statement about **methods**, not about the truth of
any extraction question. L-9918.7 says a particular family of inequalities cannot fire; it
does not say $\bigcap_N S_N$ is or is not empty, and it does not prove $m_N \to \infty$ for
any architecture. See the boxed warning before L-9918.7 and §Part C.

---

## Statement

Throughout, $e(t) := \exp(2\pi i t)$, $\mathbb{Z}^+ = \{1,2,\dots\}$, $(y)_+ := \max(y,0)$,
empty sums are $0$ and empty products are $1$ (NOTATION.md). $\nu_2$ is the $2$-adic
valuation and $\mathbb{Z}_{(2)}$ the rationals with odd denominator.

### D-9918.1 (cylinder architecture)

Let $M \ge 2$ be an integer. A **cylinder architecture with base $M$** is a sequence
$\mathcal{C} = (C_N)_{N \ge 0}$ where

1. $C_N \subseteq \mathbb{Z}/M^N\mathbb{Z}$ is nonempty and finite, $R_N := |C_N| \ge 1$
   (necessarily $C_0 = \mathbb{Z}/1\mathbb{Z}$, $R_0 = 1$);
2. **(refinement)** writing $\rho_N : \mathbb{Z}/M^{N+1}\mathbb{Z} \to \mathbb{Z}/M^N\mathbb{Z}$
   for the reduction map, $\rho_N(C_{N+1}) \subseteq C_N$ for every $N \ge 0$.

Its **constraint sets** are
$$S_N := \{\, x \in \mathbb{Z}^+ : (x \bmod M^N) \in C_N \,\}, \qquad
m_N := \min S_N .$$
So $S_N$ is exactly the union of $R_N$ residue classes mod $M^N$ intersected with
$\mathbb{Z}^+$; each such class contains infinitely many positive integers, so $S_N$ is
infinite and $m_N$ is a well-defined positive integer (well-ordering). Refinement gives
$S_{N+1} \subseteq S_N$ (D-9918.1 is exactly the commissioning description: nesting realised
by class refinement). A **seed** is an element of $\bigcap_{N \ge 0} S_N$.

An architecture is **branching-uniform of degree $b$** if every class of $C_N$ has exactly
$b$ children in $C_{N+1}$; then $R_N = b^N$.

### D-9918.2 ($M$-adic completion, cylinders, closures)

$$\mathbb{Z}_M := \Big\{\, z = (z_N)_{N \ge 0} \in \prod_{N \ge 0}\mathbb{Z}/M^N\mathbb{Z}
\;:\; \rho_N(z_{N+1}) = z_N \ \ \forall N \,\Big\},$$
a commutative ring under componentwise operations, with projections
$\pi_N : \mathbb{Z}_M \to \mathbb{Z}/M^N\mathbb{Z}$, $\pi_N(z) = z_N$. Put
$\mathrm{ord}(y,z) := \sup\{N \ge 0 : y_N = z_N\} \in \mathbb{N}\cup\{\infty\}$ and
$d(y,z) := M^{-\mathrm{ord}(y,z)}$ (so $d(y,z) = 0$ iff $y = z$). Then $d$ is an ultrametric
and the balls $\pi_N^{-1}(c)$, $c \in \mathbb{Z}/M^N\mathbb{Z}$, are clopen and form a base.
$\mathbb{Z}$ embeds in $\mathbb{Z}_M$ by $n \mapsto (n \bmod M^N)_N$, and $\mathbb{Z}^+$ is
dense (Lemma A.0 below). For an architecture $\mathcal{C}$ set
$$\widehat S_N := \overline{S_N} \subseteq \mathbb{Z}_M \quad(\text{closure}),
\qquad \widehat S_\infty := \bigcap_{N \ge 0}\widehat S_N .$$

### D-9918.3 (affine architecture; addresses)

A cylinder architecture is **affine** if it carries the following extra data.

* **(AF1) Addresses.** A finite alphabet $D$ and, for each $N$, a bijection
  $w \mapsto c(w)$ from a set $W_N \subseteq D^N$ of **admissible words** onto $C_N$, such
  that $c(w|_{N-1}) = \rho_{N-1}(c(w))$ for every $w \in W_N$ (prefixes correspond to
  reductions). The **address** of $z \in \widehat S_\infty$ is the unique
  $w(z) \in D^{\mathbb{N}}$ with $c(w(z)|_N) = \pi_N(z)$ for all $N$.
* **(AF2) Affine step data.** A map $\Phi$ defined on $\widehat S_1$ and integers
  $A_w \ge 1$, $\kappa_w \ge 0$ for each admissible $w$ with $|w| = p$, such that
  $\gcd(A_w, M) = 1$ and, for every $x$ in the class $c(w)$ (in $\mathbb{Z}$ or
  $\mathbb{Z}_M$),
  $$\Phi^p(x) \;=\; \frac{A_w\,x + \kappa_w}{M^{\,p}} \;\in\; \mathbb{Z}_M .$$
* **(AF3) Shift equivariance.** $w(\Phi(z))$ is the left shift of $w(z)$, for
  $z \in \widehat S_\infty$.
* **(AF4) Positivity preservation.** $\Phi(\mathbb{Z}^+ \cap \widehat S_1) \subseteq \mathbb{Z}^+$.

$w$ is **supercritical** if $A_w > M^{|w|}$, **subcritical** if $A_w < M^{|w|}$ (by (AF2)
these are the only possibilities; see L-9918.5(2)). The architecture is **supercritical** if
every admissible word is; **uniformly supercritical with ratio $\lambda > 1$** if
$A_w \ge \lambda^{|w|}M^{|w|}$ for every admissible $w$.

### The four exhibited architectures (correspondences)

> **E1 — six-branch chart (issue #58 / L-9916).** $M := Q = 2^{19}$, digit alphabet
> $A = \{7\cdot 3^{2i}2^{15-3i} : 0 \le i \le 5\} \subseteq [0,Q)$, $P := 3^{12}$,
> $\gcd(P,Q) = 1$. Chart map $\mathcal{C}(x) = \lceil Px/Q\rceil$, digit
> $a_n = Qx_{n+1} - Px_n$. $C_N := \{r_w \bmod Q^N : w \in A^N\}$ with
> $c_w = \sum_{j<N}P^{N-1-j}Q^j\alpha_j$ and $r_w = (-P^{-N}c_w) \bmod Q^N$. Branching-uniform
> of degree $6$, $R_N = 6^N$. Affine with $\Phi = \mathcal{C}$, $A_w = P^{|w|}$,
> $\kappa_w = c_w > 0$: **supercritical**, indeed uniformly with $\lambda = P/Q > 1$.
> ($M = Q$, so "level $N$" here means $Q^N = 2^{19N}$.)
>
> **E2 — parity-word cylinders for the shortcut map $T$ (D-9902).** $M = 2$, alphabet
> $D = \{0,1\}$. For a fixed infinite word $b$, $C_N := \{\pi_N^{-1}(b|_N)\}$, $R_N = 1$; for
> a **language** $L \subseteq \{0,1\}^*$ closed under prefixes,
> $C_N := \{$classes of the words in $L \cap \{0,1\}^N\}$, $R_N = |L \cap \{0,1\}^N|$.
> Affine with $\Phi = T$, $A_w = 3^{|w|_1}$, $M^{|w|} = 2^{|w|}$, and $\kappa_w$ given by
> $\kappa_\emptyset = 0$, $\kappa_{wb} = 3^{b}\kappa_w + b\,2^{|w|}$; so $\kappa_w \ge 0$ with
> $\kappa_w > 0$ iff $w$ contains a $1$. Supercritical **on $w$** iff
> $3^{|w|_1} > 2^{|w|}$, i.e. iff the odd-step density $|w|_1/|w|$ exceeds
> $\gamma = \log_3 2$: *the architecture is supercritical exactly on the words a
> divergence hunt wants.*
>
> **E3 — L-9909 uniform-descent survivor classes.** $M = 2$; $C_N := \{r \bmod 2^N :
> r$ is an $N$-survivor$\}$, where $r$ is an $N$-survivor iff $3^{a_j} \ge 2^j$ for
> $1 \le j \le N$, $a_j$ the odd-step count of the class word. Refinement holds because
> the survivor condition at level $N+1$ contains the condition at level $N$.
> $R_1,\dots,R_8 = 1,1,2,3,4,8,13,19$ (reproduced independently in T2).
> Directly from the definition, $\bigcap_N S_N = \{n \in \mathbb{Z}^+ : 3^{a_j(n)} \ge 2^{j}
> \text{ for every } j \ge 1\}$ (a condition on the parity word alone). *Context only, not
> used:* L-9909.3(a) shows this condition forces $T^j(n) > n$ for all $j$, i.e.
> $\sigma(n) = \infty$ (D-9910), and L-9909's Corollary gives a converse for $n$ above an
> explicit bound; neither statement is imported here.
>
> **E4 — the $(1110)^\infty$ architecture (L-9918.4).** $M = 16$, $C_N$ the single class
> $\equiv (-19)\cdot 11^{-1} \bmod 16^{N}$ ($R_N = 1$), i.e. E2 for the fixed word
> $b = (1110)^\infty$ read four bits at a time. *(Equivalently one may take the base-$2$
> architecture with $C_N$ the class of $(-19)\cdot11^{-1}$ mod $2^N$ for **every** $N$,
> which is what T2/ARCH 5 computes; the two are cofinal subfamilies of one nested family,
> so they have the same $\bigcap_N S_N$. The base was corrected from "$M=2$ with classes
> mod $2^{4N}$" — inconsistent with D-9918.1(1) — by fable-02-v20.)* Supercritical
> ($3^3 = 27 > 16 = 2^4$). This is the canonical example with all $S_N$ infinite and
> $\bigcap_N S_N = \emptyset$.

---

### L-9918.1 (extraction normalisation). *For every cylinder architecture:*

1. $S_{N+1}\subseteq S_N$ for all $N \ge 0$; hence $(m_N)_{N\ge0}$ is non-decreasing.
2. The following are equivalent:
   **(i)** $\bigcap_{N\ge0}S_N \ne \emptyset$; **(ii)** $\sup_N m_N < \infty$;
   **(iii)** $(m_N)$ is eventually constant. Under these, $\bigcap_N S_N$ has least element
   $\lim_N m_N$.
3. Equivalently, the negations are equivalent: **(i$'$)** $\bigcap_N S_N = \emptyset$;
   **(ii$'$)** $m_N \to \infty$; **(iii$'$)** for every $x \in \mathbb{Z}^+$ there is $N$
   with $x \notin S_N$.
4. Consequently, defining the **exit level** $\kappa(x) := \min\{N : x \notin S_N\}
   \in \mathbb{N}\cup\{\infty\}$: $m_N = \min\{x : \kappa(x) > N\}$,
   $\bigcap_N S_N = \kappa^{-1}(\infty)$, and escape is the *pointwise* statement
   $\kappa(x) < \infty$ for every $x$ — no rate is required.

### L-9918.2 (the asymmetry: the $M$-adic limit always exists). *For every cylinder architecture:*

1. $\widehat S_N = \pi_N^{-1}(C_N)$: a nonempty **clopen** (hence closed) subset of
   $\mathbb{Z}_M$, equal to a disjoint union of $R_N$ balls of radius $M^{-N}$.
2. $\widehat S_{N+1} \subseteq \widehat S_N$ for all $N$.
3. $\widehat S_\infty = \bigcap_N \widehat S_N \neq \emptyset$ — **always, with no
   hypothesis beyond D-9918.1.**
4. $\bigcap_N S_N = \widehat S_\infty \cap \mathbb{Z}^+$.

> **The extraction principle (the content of Part A in one line).** Every extraction question
> of the form "does this nested-cylinder family contain an ordinary positive integer" is
> literally the question **"does the always-nonempty compact set $\widehat S_\infty
> \subseteq \mathbb{Z}_M$ meet $\mathbb{Z}^+$?"** The symbolic/adic half is free
> (L-9918.2(3)); the whole content is the archimedean half (L-9918.2(4)).

### L-9918.3 (the exact repair of the quantifier interchange).

Let $(S_N)_{N\ge0}$ be **any** nested ($S_{N+1}\subseteq S_N$) family of nonempty subsets of
$\mathbb{Z}^+$. Then the following are equivalent:

1. $\bigcap_N S_N \ne \emptyset$;
2. $\exists B \in \mathbb{Z}^+\ \forall N\ \exists x_N \in S_N$ with $x_N \le B$
   (**uniformly bounded witnesses**);
3. $\exists B\ \forall N: m_N \le B$.

Hence the inference "$\forall N \exists x_N \in S_N \Rightarrow \exists x\,\forall N\,
x \in S_N$" is valid **if and only if** the witnesses can be chosen with a uniform bound; the
unrepaired inference is false (L-9918.4). Nestedness is essential in (2)$\Rightarrow$(1) and
is used nowhere else.

### L-9918.4 (canonical Collatz-native counterexample: the word $(1110)^\infty$).

Let $T$ be the shortcut map (D-9902), extended to $\mathbb{Z}_{(2)}$ by the same two branch
formulas, and $v_i, a_k$ as in D-9906. Then:

1. For every $x \in \mathbb{Z}$ (indeed every $x \in \mathbb{Z}_{(2)}$):
   $$\big(v_0(x),v_1(x),v_2(x),v_3(x)\big) = (1,1,1,0) \iff x \equiv 7 \pmod{16},$$
   and in that case $T^4(x) = \dfrac{27x+19}{16}$.
2. **(key identity)** Whenever $x \equiv 7 \pmod{16}$,
   $\;11\,T^4(x) + 19 = \dfrac{27\,(11x+19)}{16}.$
3. For every $N \ge 0$ and every $x \in \mathbb{Z}$:
   $$\big(v_0(x),\dots,v_{4N-1}(x)\big) = (1,1,1,0)^N \iff 16^{N} \mid 11x + 19 .$$
4. Hence, with $S_N := \{x \in \mathbb{Z}^+ : (v_0(x),\dots,v_{4N-1}(x)) = (1110)^N\}$:
   $S_N$ is exactly one residue class mod $2^{4N}$ intersected with $\mathbb{Z}^+$
   ($R_N = 1$), is **infinite**, and
   $$m_N = \big((-19)\cdot 11^{-1}\big) \bmod 16^{N} \in [1, 16^N).$$
5. $\bigcap_{N \ge 0} S_N = \emptyset$; therefore (L-9918.1) $m_N \to \infty$.
6. $\widehat S_\infty = \{z^*\}$ with $z^* = -19/11 \in \mathbb{Z}_{(2)} \subseteq \mathbb{Z}_2$,
   the unique fixed point of $x \mapsto (27x+19)/16$; its exact $T$-orbit is the $4$-cycle
   $$-\tfrac{19}{11} \to -\tfrac{23}{11} \to -\tfrac{29}{11} \to -\tfrac{38}{11}
   \to -\tfrac{19}{11}, \qquad \text{parities } (1,1,1,0),$$
   so $V(z^*) = (1110)^\infty$; and $z^* \notin \mathbb{Z}$, $z^* < 0$.

*So: every finite prefix is realised by infinitely many positive integers, no positive
integer realises the whole word, and the $2$-adic realiser exists and is unique. This is the
unrepaired quantifier interchange failing, in a Collatz-native architecture.*

### L-9918.5 (positivity / sign criterion at generality).

Let the architecture be affine (D-9918.3), let $p \ge 1$ and let $w$ be an admissible word of
length $p$ such that $w^k$ is admissible for every $k \ge 1$. Then:

1. $A_{w^k} = A_w^{\,k}$ and $\kappa_{w^k} = \kappa_w\cdot\frac{A_w^{\,k} - M^{pk}}{A_w - M^p}$;
   any $z \in \mathbb{Z}_M$ with address $w^\infty$ satisfies $\Phi^p(z) = z$, hence
   $$(M^{\,p} - A_w)\,z = \kappa_w .$$
2. $M^p - A_w \ne 0$ and $\gcd(M^p - A_w, M) = 1$; so $M^p - A_w$ is a unit of
   $\mathbb{Z}_M$ and the address $w^\infty$ has the **unique** realiser
   $$z_w \;=\; \frac{\kappa_w}{M^{\,p} - A_w} \;\in\; \mathbb{Q}\cap\mathbb{Z}_M ,$$
   a rational whose denominator in lowest terms divides $M^p - A_w$.
3. **(sign criterion)** $\kappa_w \ge 0$, so:
   $z_w > 0 \iff \kappa_w > 0$ and $A_w < M^p$ (subcritical);
   $z_w < 0 \iff \kappa_w > 0$ and $A_w > M^p$ (supercritical);
   $z_w = 0 \iff \kappa_w = 0$.
   Consequently $z_w \in \mathbb{Z}^+$ requires **all three** of
   $$\kappa_w > 0, \qquad A_w < M^{\,p}, \qquad (M^{\,p}-A_w) \mid \kappa_w ,$$
   the first two being sign conditions and only the third Diophantine.
4. **(no periodic seeds in a supercritical architecture)** If every admissible word $w$ with
   $\kappa_w>0$ is supercritical, and (AF3), (AF4) hold, then **no** element of
   $\bigcap_N S_N$ has an eventually periodic address. In particular none has a purely
   periodic address.
5. **(specialisations)** *(a)* E2/parity: $M = 2$, $A_w = 3^{a}$, $M^p = 2^{K}$, so the
   threshold is $2^K > 3^a$, i.e. $a/K < \gamma = \log_3 2$; the realiser is
   $\kappa_w/(2^K - 3^a) \in \mathbb{Z}_{(2)}$ — the parity-case sign statement.
   *(b)* E1/six-branch: $M = Q$, $A_w = P^p$, $M^p = Q^p$, and $P = 3^{12} > 2^{19} = Q$
   forces supercriticality for every $p$, so every periodic realiser is
   $c_w/(Q^p - P^p) < 0$.
   *(c)* E4: $p = 4$, $A_w = 27$, $M^p = 16$, $\kappa_w = 19$, $z_w = -19/11 < 0$.
6. **(drift)** If $x \in \bigcap_N S_N$ and the architecture is uniformly supercritical with
   ratio $\lambda > 1$, then $\Phi^n(x) = (A_{w|n}x + \kappa_{w|n})/M^n \ge \lambda^n x$, so
   the $\Phi$-orbit of $x$ diverges (D-9907).

---

> ### **HONESTY BOX — what Part B is and is not**
>
> Part B is a theorem about **a family of proof methods**. It says that inequalities of
> Erdős–Turán shape, applied in the standard way (one frequency cut-off $H$, absolute values
> of the exponential sums, a resolution term proportional to $R\varphi(H)/H$), cannot
> produce an emptiness certificate unless their constants lie in an explicitly described
> region — and that the constants currently provable by elementary Fejér-power majorants lie
> outside it. It does **not** prove, suggest, or bear on whether $\bigcap_N S_N$ is empty for
> any architecture; it does **not** prove $m_N \to \infty$ anywhere; and it says nothing
> whatsoever about the Collatz conjecture. Two further limitations are proved-in and must be
> quoted with the result: the barrier attaches to the **triangle-inequality step**
> ($|\sum_h \widehat\Psi(h)S(h)| \le \sum_h |\widehat\Psi(h)||S(h)|$), so a method retaining
> the phases is untouched; and it attaches to a **single** cut-off $H$, so multi-scale,
> second-moment, large-sieve and lattice methods are untouched.

### L-9918.6 (universal lower bound for harmonic cusp sums).

Let $R \ge 1$ and let $\theta_1,\dots,\theta_R \in \mathbb{R}/\mathbb{Z}$ be **any** points
(repetitions allowed), $S(h) := \sum_{r=1}^{R}e(h\theta_r)$. Then:

1. For every integer $h \ge 1$: $\;\sum_{k=1}^{h}|S(k)|^2 \ge \tfrac12 R\,(h+1-R)$, hence
   $T(h) := \sum_{k=1}^{h}|S(k)| \ge \max\big(0, \tfrac12(h+1-R)\big)$.
2. For every integer $H \ge R$:
   $$\sum_{h=1}^{H}\frac{|S(h)|}{h} \;\ge\; \frac12\Big(\log\frac HR + \frac1H\Big) .$$
3. For **every** integer $H \ge 1$ (no relation between $H$ and $R$ assumed):
   $$\boxed{\ \sum_{h=1}^{H}\frac{|S(h)|}{h} \;\ge\; \frac12\,\log\frac HR\ }$$
   (for $H < R$ the right side is negative and the left side is $\ge 0$).
4. **(sharpness)** For $R$ equally spaced points the left side equals
   $\sum_{k \le H/R}1/k \in [\log(H/R), \log(H/R)+1]$, so the constant $\tfrac12$ is off by
   at most a factor $2$ from optimal; no configuration with a smaller value was found
   (T3, EMPIRICAL).
5. **(no invisible point set)** $S(h) \ne 0$ for some $h \in \{1,\dots,R\}$, and this is
   sharp: for $R$ equally spaced points $S(1) = \dots = S(R-1) = 0$.

**Quantifier audit (performed; result recorded).** The statement is genuinely universal over
finite point *multisets*: no distinctness, no equidistribution, no separation, no
irrationality hypothesis is needed, and $R$ may exceed, equal or be less than $H$. The only
hypotheses are $R \ge 1$ and $H \ge 1$. The commissioning framing's "$H \ge R$" is
**not needed** for form (3) and is needed only for the sharper form (2); this is recorded as
a (favourable) correction.

### L-9918.7 (the collision, and the exact admissible region of constant pairs).

**(a) Definition (ET-shape criterion).** Fix $C_1, C_2 > 0$ and $\varphi : [1,\infty) \to
(0,\infty)$ non-decreasing. An **ET-shape inequality with data $(C_1,C_2,\varphi)$** is the
assertion that for all $R \ge 1$, all point multisets $(\theta_r)_{r\le R}$, all arcs
$I \subseteq \mathbb{R}/\mathbb{Z}$ of length $\beta \in [0,1]$ and all admissible integers
$H$,
$$\#\{r : \theta_r \in I\} \;\le\; R\beta \;+\; C_1\,\frac{R\,\varphi(H)}{H}
\;+\; C_2\sum_{h=1}^{H}\frac{|S(h)|}{h} . \tag{ET}$$
It **fires** at $(R,\beta,H)$ if the right-hand side is $< 1$ (which then certifies
$\#\{r : \theta_r \in I\} = 0$).

**(b) Necessity of $H \gtrsim R$ — with the correct reason.** If (ET) fires then all three
terms are $< 1$; in particular
$$C_1\,\frac{R\,\varphi(H)}{H} < 1, \qquad\text{i.e.}\qquad H > C_1\,R\,\varphi(H) .$$
If $\varphi \ge 1$ this gives $H > C_1R$. **Correction to the commissioning framing:** the
requirement comes from the **resolution term alone** and is independent of the interval
length $\beta$; and it is "$H > C_1R$", not "$H \gtrsim R$" unconditionally — a hypothetical
majorant with $C_1 < 1$ could legitimately use $H < R$.

**(c) The collision.** Put $u := H/R$. If (ET) fires at $(R,\beta,H)$ then, by (b) and
L-9918.6(3),
$$G(u) \;:=\; C_1\,\frac{\varphi(uR)}{u} \;+\; \frac{C_2}{2}\big(\log u\big)_+
\;<\; 1 - R\beta \;\le\; 1 . \tag{$\dagger$}$$

**(d) Exact admissible region for $\varphi \equiv 1$.** Define
$$\Theta(C_1,C_2) := \inf_{u>0}\Big[\frac{C_1}{u} + \frac{C_2}{2}(\log u)_+\Big]
= \begin{cases} C_1, & 2C_1 \le C_2,\\[4pt]
\dfrac{C_2}{2}\Big(1 + \log\dfrac{2C_1}{C_2}\Big), & 2C_1 > C_2,\end{cases}$$
the infimum being attained at $u = 1$ in the first case and at $u^* = 2C_1/C_2$ in the
second. Then ($\dagger$) is satisfiable for some $u > 0$ **iff** $\Theta(C_1,C_2) < 1$,
**iff**
$$\boxed{\;\big[\,C_2 < 2 \ \text{ and }\ C_1 < \Psi(C_2)\,\big] \quad\text{or}\quad
\big[\,C_2 \ge 2 \ \text{ and }\ C_1 < 1\,\big], \qquad
\Psi(s) := \frac{s}{2}\,e^{\,2/s - 1} \;}$$
Moreover $\Psi(s) \ge 1$ for all $s>0$ with equality only at $s = 2$ (so $C_1 < 1$ is always
sufficient), $\Psi$ is strictly decreasing on $(0,2)$ and strictly increasing on
$(2,\infty)$, and
$$\Psi(2/\pi) = \frac{e^{\pi-1}}{\pi} = 2.709767\ldots,\qquad
\Psi(1) = \tfrac12 e = 1.359141\ldots,\qquad \Psi(2) = 1 .$$

**(e) The window, when admissible.** $\{u > 0 : G(u) < 1\}$ is an open interval
$(u_-, u_+)$; for $(C_1,C_2) = (1, 2/\pi)$ it is
$$u_- = 1, \qquad u_+ = 19.73524\ldots, \qquad u^* = \pi, \qquad \Theta = \frac{1+\log\pi}{\pi}
= 0.682689\ldots,$$
a window of multiplicative width $19.735$ in $H$, and the cusp-sum budget at $u = u^*$
is $\frac{\pi}{2}\big(1 - \frac1\pi\big) = 1.070796\ldots$ (as $R\beta \to 0$).

**(f) Elementary Fejér-power constants are unsatisfiable, for every $R$.** For
$(C_1, C_2, \varphi) = \big(4,\ 2/\pi,\ \log(4H)\big)$ — the data provable by a
Fejér-power majorant — and for every real $R \ge 1$ and every real $H \ge 3$,
$$4\,\frac{R\log(4H)}{H} + \frac{1}{\pi}\Big(\log\frac HR\Big)_+
\;>\; \frac{1 + \log(4\pi\log 12)}{\pi} \;=\; 1.413696\ldots \;>\; 1 ,$$
so ($\dagger$) fails and (ET) never fires. (The bound is uniform in $R$; numerically the
true minimum is $1.6678$ at $R = 1$ and increases in $R$: $1.7727$ at $R = 6$, $2.0891$ at
$R = 10^6$; T5.)

**(g) Removing the logarithm is necessary but not sufficient.** With $\varphi \equiv 1$ and
$C_2 = 2/\pi$, (ET) is satisfiable **iff** $C_1 < e^{\pi-1}/\pi = 2.709767\ldots$. In
particular $(C_1,C_2) = (4, 2/\pi)$ with $\varphi \equiv 1$ still fails
($\Theta = \frac1\pi(1+\log 4\pi) = 1.123960 > 1$); and the classical pair
$(C_1,C_2) = (1,3)$ fails ($\Theta = 1$, not $<1$).

### L-9918.8 (generalised Parseval obstruction).

Let $k \ge 1$, let $D \subseteq \mathbb{Z}/M^k\mathbb{Z}$ have $|D| = d \ge 1$ pairwise
distinct elements, and put $g(v) := \sum_{\alpha\in D}e(v\alpha/M^k)$. Then:

1. $\displaystyle \frac{1}{M^k}\sum_{v \bmod M^k}|g(v)|^2 = d$ **exactly**. In particular
   the root mean square of $|g|$ is $\sqrt d$ and $\max_v|g(v)| \ge \sqrt d$ (indeed $=d$ at
   $v=0$).
2. For every $0 \le \lambda < d$,
   $$\frac{\#\{v \bmod M^k : |g(v)|^2 > \lambda\}}{M^k} \;\ge\; \frac{d-\lambda}{d^2-\lambda} .$$
   Hence no bound $|g(v)| \le c$ with $c < \sqrt d$ can hold on a set of $v$ of density
   $1$, and for $d \ge 2$ no bound of the form $|g(v)| \le 1-\delta$ can hold on average.
3. If the $R_N$ root classes of an architecture are pairwise distinct mod $M^N$, then
   $$\frac{1}{M^N}\sum_{h \bmod M^N}\big|\widehat S_N(h)\big|^2 = R_N, \qquad
   \widehat S_N(h) := \sum_{c \in C_N} e\!\left(\frac{h\,r_c}{M^N}\right).$$
4. **(mean-square losslessness — the exact consequence)** If $\widehat S_N = \prod_{j=1}^{N}
   G_j$ is any factorisation into digit sums $G_j$ over digit sets of sizes $d_j$ with
   $\prod_j d_j = R_N$, then
   $$\prod_{j=1}^{N}\Big(\text{mean square of } G_j\Big) = \prod_j d_j = R_N
   = \text{mean square of }\widehat S_N .$$
   The independence heuristic is therefore **exactly** Parseval-tight: per-level
   second-moment information reproduces the global second moment and yields **no decay
   whatsoever**. Any successful bound must (i) be restricted to the low-frequency window
   $h \le H$, a fraction $H/M^N$ of all frequencies, and (ii) exploit correlations
   **between** levels.

### L-9918.9 (undecidability of extraction in general).

There is a computable map $e \mapsto \mathcal{C}^{(e)}$ from Turing-machine indices to
cylinder architectures with $M = 2$ and $R_N = 1$ for all $N$ (a single nested class at
every level), presented by a computable function $(e,N)\mapsto C^{(e)}_N$, such that
$$\bigcap_{N}S^{(e)}_N \ne \emptyset \iff \text{machine } e \text{ halts on empty input}.$$
Consequently the problem "given a computable presentation of a cylinder architecture, decide
whether it has a seed" is undecidable — already for $M=2$, $R_N = 1$. With a decidable
membership predicate, "$\bigcap_N S_N \ne \emptyset$" is $\Sigma^0_2$ and each instance
"$x \notin S_N$ for some $N$" is $\Sigma^0_1$ (semi-decidable, hence certified by a
terminating computation whenever true).

> **Reading.** This says no procedure can decide extraction **from the architecture's
> counting/refinement data alone**; any successful decision must use arithmetic specific to
> the architecture at hand. It says nothing about any specific architecture, all of which are
> highly structured and may well be decidable individually.

### Q-9918 (arithmetic replacement targets; OPEN, no direction claimed).

**(Q-9918a — forced-place target for E1.)** The six-branch alphabet satisfies the exact
algebraic relations $8\alpha_{i+1} = 9\alpha_i$ and $\nu_2(\alpha_i) = 15-3i$
($0 \le i \le 5$). Do these force a nonvanishing base-$Q$ place in $r_w$ at index
$\ge N-1$ for every $w \in A^N$ — equivalently, is $m_N \ge Q^{\,N-1}$ for all $N \ge 1$?
Such a statement is an assertion about $\nu_2$-structure and about the orbit of
$P^{-1}$ in $(\mathbb{Z}/Q^N)^\times$, not a counting statement, so it is **not** subject to
L-9918.6/7. *(Consistency, EMPIRICAL, T2: $m_N/Q^{N-1} = 6472,\ 3640.9,\ 163.4,\ 1909.6$
for $N \le 4$; note $Q^{N-1}$ is far below the null-model scale $(Q/6)^N$, so the target is
much weaker than what the null model predicts, and no direction is claimed.)*

**(Q-9918b — valuation certificate, general form.)** For a cylinder architecture, does there
exist an **arithmetic escape certificate**: a function $\omega : \bigcup_N C_N \to
\mathbb{Z}_{\ge0}$ computable from the address by a finite-state transducer, such that
(i) every class $c \in C_N$ has least positive representative $r_c \ge M^{\omega(c)}$, and
(ii) $\min_{c \in C_N}\omega(c) \to \infty$? Existence implies $m_N \to \infty$ (L-9918.1),
is falsifiable at each level by exact finite computation, and is immune to Part B because it
never counts lattice points against an interval.

**(Q-9918c — the decidable-subclass question.)** L-9918.9 shows the general problem is
undecidable. Identify a natural subclass of architectures — e.g. those whose class sets are
recognised by a finite automaton reading base-$M$ digits — for which extraction **is**
decidable, and determine whether E1–E3 lie in it.

---

## Definitions

Beyond D-9918.1–D-9918.3:

* $\lceil y \rceil$ = least integer $\ge y$. $(y)_+ = \max(y, 0)$.
* $V(z) := (v_0(z), v_1(z), \dots)$ is the infinite parity word of $z$ (D-9906).
* For a word $w$, $w|_j$ is its length-$j$ prefix, $w^k$ the $k$-fold concatenation,
  $|w|_1$ the number of $1$s.
* $K_h(t) := \sum_{|k|\le h}\big(1 - \frac{|k|}{h+1}\big)e(kt)$ is the Fejér kernel of degree
  $h \ge 0$.
* A **ball** in $\mathbb{Z}_M$ is a set $\pi_N^{-1}(c)$; its radius is $M^{-N}$.
* An architecture is **computably presented** if $(N, c) \mapsto [c \in C_N]$ is computable.
* $\gamma := \log_3 2 = 0.6309298\ldots$ (NOTATION.md).

**Verification of E1's alphabet.** $7\cdot3^{2i}2^{15-3i} = 7\cdot2^{15}(9/8)^i$, giving
$229376, 258048, 290304, 326592, 367416, 413343$, all in $[0, 2^{19})$, with
$\nu_2 = 15,12,9,6,3,0$; $\gcd = 7$. (Recomputed in T2.)

---

## Motivation

Several independent programmes in this repository reduce, after their own reductions, to one
and the same question: *does this nested family of residue-class constraints contain an
ordinary positive integer?* Issue #58 asks it for the six-branch chart (E1); issue #21's
foundry and issue #4's amplifier ask it for parity-word languages (E2); L-9909's sieve poses
it for survivor classes (E3); the adelic/cusp Fourier programme of issues #15/#16 supplies
the analytic tools that a counting attack on any of them would use.

Each programme has, reasonably, developed the answer for its own architecture. The purpose of
this file is to prove the common part exactly once, at the level of generality where it is
actually true, so that a barrier discovered in one sub-architecture is not re-discovered
five times and — more importantly — so that the **scope** of each barrier is stated once,
correctly, and cannot drift.

Two things become visible only at this generality.

*First*, the extraction question has a completely rigid logical shape (L-9918.1–L-9918.3):
the adic limit always exists, so nothing is ever gained by producing one; the entire content
sits in a uniform bound on witnesses, which is precisely what no symbolic construction
supplies. L-9918.4 makes this concrete with an object every agent in this repository can
check by hand in five minutes: the word $(1110)^\infty$ has infinitely many positive-integer
representatives at every finite depth and none at infinite depth, and the missing limit is
$-19/11$.

*Second*, the negative analytic result is not about the six-branch chart. L-9918.6 holds for
every finite point set on the circle, and L-9918.7 turns it into an exact statement about
*constants*: an inequality of Erdős–Turán shape can produce an emptiness certificate only if
its constant pair lies in the region $\{C_2 < 2,\ C_1 < \Psi(C_2)\} \cup \{C_2 \ge 2,\
C_1 < 1\}$. That region is a permanent fact about the method, independent of which
architecture it is aimed at; it tells any future programme, before it starts, exactly what
quality of majorant it must first prove.

Finally, L-9918.9 explains why the arithmetic replacement targets of Q-9918 are not merely
one option among many: from the architecture's combinatorial data alone the question is
undecidable, so *every* successful attack must use the specific arithmetic of the digits.

---

## Proof or construction

### Lemma A.0 (basic structure of $\mathbb{Z}_M$; self-contained)

*Let $M \ge 2$. Then (i) $d$ is an ultrametric on $\mathbb{Z}_M$ and every ball
$\pi_N^{-1}(c)$ is clopen; (ii) $\mathbb{Z}^+$ is dense in $\mathbb{Z}_M$; (iii) an integer
$a$ with $\gcd(a,M)=1$ is a unit of $\mathbb{Z}_M$; (iv) $\bigcap_N M^N\mathbb{Z}_M = \{0\}$,
so an element of $\mathbb{Z}$ divisible by $M^N$ for every $N$ is $0$.*

*Proof.* (i) If $y_N = z_N$ then $y_j = z_j$ for all $j \le N$ (apply $\rho$'s), so
$\mathrm{ord}(y,z) = \sup\{N : y_N = z_N\}$ is attained downward-closed and
$\mathrm{ord}(y,z) \ge \min(\mathrm{ord}(y,x),\mathrm{ord}(x,z))$, which is the ultrametric
inequality $d(y,z) \le \max(d(y,x), d(x,z))$. Symmetry and $d(y,z)=0 \iff y=z$ are clear.
$\pi_N^{-1}(c) = \{z : d(z, z^0) \le M^{-N}\}$ for any $z^0$ in it, so it is a closed ball;
it is also open because $d(z,z^0)\le M^{-N}$ is implied by $d(z,z^0) < M^{-N+1}$ ($d$ takes
only the values $M^{-j}$). Distinct $c$ give disjoint balls, and they cover, so each is the
complement of a finite union of the others: clopen.

(ii) Let $z \in \mathbb{Z}_M$ and $N \ge 0$. Let $r \in [0, M^N)$ represent $z_N$ and put
$x := r$ if $r \ge 1$, else $x := M^N$. Then $x \in \mathbb{Z}^+$ and $x \equiv r
\pmod{M^N}$, so $\pi_N(x) = z_N$ and $d(x,z) \le M^{-N}$.

(iii) $\gcd(a, M) = 1 \Rightarrow \gcd(a, M^N) = 1$, so $a$ is invertible mod $M^N$ with a
unique inverse $b_N$; the $b_N$ are coherent ($b_{N+1} \bmod M^N$ inverts $a$ mod $M^N$, and
inverses are unique), so $b := (b_N) \in \mathbb{Z}_M$ and $ab = 1$.

(iv) $z \in M^N\mathbb{Z}_M$ iff $\pi_N(z) = 0$; if this holds for all $N$ then $z = 0$ by
definition of $\mathbb{Z}_M$. For $a \in \mathbb{Z}$ with $M^N \mid a$ for all $N$: $|a| <
M^N$ for large $N$ forces $a = 0$. $\square$

### Proof of L-9918.1

**(1)** Let $x \in S_{N+1}$. Then $(x \bmod M^{N+1}) \in C_{N+1}$, so by refinement
$(x \bmod M^N) = \rho_N(x \bmod M^{N+1}) \in C_N$, i.e. $x \in S_N$. Hence $S_{N+1}\subseteq
S_N$ and $m_{N+1} = \min S_{N+1} \ge \min S_N = m_N$. *(Uses only refinement.)*

**(2)** *(i)$\Rightarrow$(ii).* If $x \in \bigcap_N S_N$ then $x \in S_N$ for every $N$, so
$m_N \le x$ for every $N$; take $B := x$. *(Uses only $m_N = \min S_N$; no nesting.)*

*(ii)$\Rightarrow$(iii).* By (1), $(m_N)$ is a non-decreasing sequence in $\mathbb{Z}^+$; if
it is bounded above by $B$ it takes values in the finite set $\{1,\dots,B\}$, so it is
eventually constant (a non-decreasing sequence in a finite totally ordered set is eventually
constant: it can strictly increase at most $B-1$ times). *(Uses monotonicity — hence
refinement — and the **discreteness of $\mathbb{Z}$**: this implication is false for
non-decreasing bounded sequences of reals, and it is the only place where the archimedean
structure of $\mathbb{Z}^+$ enters Part A.)*

*(iii)$\Rightarrow$(i).* Let $m_N = m$ for all $N \ge N_0$. Then $m = m_N \in S_N$ for every
$N \ge N_0$; and for $N < N_0$, $S_{N_0}\subseteq S_N$ by (1), so $m \in S_N$ too. Hence
$m \in \bigcap_N S_N$. *(Uses nesting.)*

*Least element.* Any $x \in \bigcap_N S_N$ satisfies $x \ge m_N = m$ for $N \ge N_0$, and
$m$ itself lies in the intersection; so $m = \lim_N m_N$ is its least element.

**(3)** (i$'$)$\iff$(ii$'$): (i$'$) is $\neg$(i), (ii$'$) is $\neg$(ii) *given* monotonicity
(a non-decreasing sequence is unbounded iff it tends to $\infty$). (i$'$)$\iff$(iii$'$): the
statement $\bigcap_N S_N = \emptyset$ *is* the statement $\forall x\,\exists N\, x\notin S_N$,
by definition of intersection. *(No hypothesis at all for this last equivalence — it is a
tautology; the content is that by (1) and finiteness of $[1,B]$ it upgrades to the uniform
statement (ii$'$): given $B$, each $x \le B$ has some $N_x$ with $x \notin S_{N_x}$; set
$N := \max_{x \le B}N_x$, a maximum over a **finite** set; by nesting $S_N \subseteq
S_{N_x}$, so no $x \le B$ lies in $S_N$, i.e. $m_N > B$.)*

**(4)** Immediate from the definitions and (1): $\kappa$ is well defined with values in
$\mathbb{N}\cup\{\infty\}$ because $S_0 = \mathbb{Z}^+ \ni x$ makes $\kappa(x) \ge 1$; and
$x \in S_N \iff \kappa(x) > N$ by nesting. $\square$

### Proof of L-9918.2

**(1)** $S_N \subseteq \pi_N^{-1}(C_N)$ is the definition. $\pi_N^{-1}(C_N)$ is a finite
union of balls, hence clopen (Lemma A.0(i)), hence closed, so $\widehat S_N \subseteq
\pi_N^{-1}(C_N)$. Conversely let $z \in \pi_N^{-1}(C_N)$ and $K \ge N$. By Lemma A.0(ii)
there is $x \in \mathbb{Z}^+$ with $\pi_K(x) = \pi_K(z)$; then $\pi_N(x) = \pi_N(z) \in C_N$,
so $x \in S_N$, and $d(x,z)\le M^{-K}$. Letting $K \to \infty$ gives $z \in \widehat S_N$.
Hence $\widehat S_N = \pi_N^{-1}(C_N)$, a disjoint union of the $R_N$ balls $\pi_N^{-1}(c)$,
$c \in C_N$; it is nonempty because $C_N \ne \emptyset$ and $\pi_N$ is surjective (given
$c$, the coherent sequence $(c \bmod M^j)_{j\le N}$ extends by choosing any lift at each
higher level).

**(2)** If $\pi_{N+1}(z) \in C_{N+1}$ then $\pi_N(z) = \rho_N(\pi_{N+1}(z)) \in C_N$ by
refinement.

**(3) (the always-nonempty adic limit).** We give a purely combinatorial proof (König's
lemma made explicit); a topological proof is in the Remark below.

For $K \ge N$ let $\rho_{N,K} : \mathbb{Z}/M^K \to \mathbb{Z}/M^N$ be the reduction, and put
$$P_N^{(K)} := \rho_{N,K}(C_K) \subseteq C_N \qquad (K \ge N),$$
the classes at level $N$ that survive to level $K$. Each $P_N^{(K)}$ is nonempty (as
$C_K \ne \emptyset$) and contained in $C_N$ by iterated refinement. Since
$\rho_{N,K+1} = \rho_{N,K}\circ\rho_{K,K+1}$ and $\rho_{K,K+1}(C_{K+1}) \subseteq C_K$, we
get $P_N^{(K+1)} \subseteq P_N^{(K)}$: a non-increasing sequence of nonempty subsets of the
**finite** set $C_N$. Hence it is eventually constant and
$$P_N := \bigcap_{K \ge N}P_N^{(K)} \ne \emptyset$$
(the eventual value). Call the elements of $P_N$ **persistent**.

*Claim: every persistent $c \in P_N$ has a persistent child.* For each $K \ge N+1$ the set
$$X_K := \{\, c' \in \rho_{N+1,K}(C_K) : \rho_N(c') = c \,\}$$
is nonempty (any $c'' \in C_K$ with $\rho_{N,K}(c'') = c$ exists since $c \in P_N^{(K)}$; its
reduction to level $N+1$ lies in $X_K$), is contained in the finite set $C_{N+1}$, and
$X_{K+1}\subseteq X_K$ by the same composition identity. So $\bigcap_{K}X_K \ne \emptyset$,
and any element of it is a persistent child of $c$.

Now choose $c_0 \in P_0$ (nonempty) and inductively a persistent child $c_{N+1} \in P_{N+1}$
of $c_N$. The sequence $(c_N)$ is coherent ($\rho_N(c_{N+1}) = c_N$) with $c_N \in C_N$, so
$z := (c_N)_N \in \mathbb{Z}_M$ and $\pi_N(z) = c_N \in C_N$ for every $N$, i.e.
$z \in \widehat S_\infty$. $\square$

> **Remark (topological form of the same fact).** $\mathbb{Z}_M$ is compact: it is a metric
> space, and given a sequence $(z^{(k)})$ one finds by finiteness of each
> $\mathbb{Z}/M^N\mathbb{Z}$ a nested chain of infinite index sets on which $\pi_N$ is
> constant, and diagonalises to a convergent subsequence whose limit is coherent. The
> $\widehat S_N$ are nonempty closed subsets of a compact space, decreasing, hence have the
> finite intersection property, hence $\bigcap_N \widehat S_N \ne \emptyset$. Both proofs use
> exactly the same input: **finiteness of each level**. Nothing else.

**(4)** For $x \in \mathbb{Z}^+$: $x \in S_N \iff \pi_N(x) \in C_N \iff x \in \widehat S_N$
(by (1)). Intersecting over $N$ gives $\bigcap_N S_N = \widehat S_\infty \cap \mathbb{Z}^+$.
$\square$

### Proof of L-9918.3

*(1)$\Rightarrow$(3).* Take $x \in \bigcap_N S_N$ and $B := x$; then $m_N \le x = B$.

*(3)$\Rightarrow$(2).* Take $x_N := m_N \in S_N$.

*(2)$\Rightarrow$(1).* Given $B$ and witnesses $x_N \in S_N$, $x_N \le B$: then $m_N \le B$
for every $N$. By nesting, $(m_N)$ is non-decreasing (as in L-9918.1(1), which needs only
$S_{N+1}\subseteq S_N$), and bounded by $B$; being a non-decreasing bounded sequence of
positive integers it is eventually constant, and the argument of L-9918.1(2)
(iii)$\Rightarrow$(i) — which uses only nesting — gives $\bigcap_N S_N \ne \emptyset$.
$\square$

> **Where the interchange fails, precisely.** "$\forall N\,\exists x_N$" produces a
> *sequence* of witnesses; "$\exists x\,\forall N$" needs a *single* one. Over
> $\mathbb{Z}_M$ the upgrade is automatic because the witness space is compact
> (L-9918.2(3)); over $\mathbb{Z}^+$ it is automatic only under a uniform bound, because a
> bounded set of positive integers is finite — and finiteness is the archimedean surrogate
> for compactness. Equivalently: in the one-point compactification
> $\mathbb{Z}^+\cup\{\infty\}$ of the discrete space $\mathbb{Z}^+$ one has
> $\overline{S_N} = S_N \cup \{\infty\}$ for every infinite $S_N$, so
> $\bigcap_N\overline{S_N} = \big(\bigcap_N S_N\big)\cup\{\infty\}$ is *always* nonempty.
> The compactification supplies a limit in both settings; the question is only ever whether
> that limit is an ordinary positive integer.

### Proof of L-9918.4

Throughout, for $x \in \mathbb{Z}_{(2)}$ (a rational with odd denominator) "odd" means the
numerator in lowest terms is odd, and $T(x) = (3x+1)/2$ if $x$ is odd, $x/2$ if $x$ is even;
this restricts to D-9902 on $\mathbb{Z}^+$. Note $\mathbb{Z}_{(2)}$ is $T$-stable.

**(1)** We compute the four parities by successive congruence refinement; each step is an
identity, valid over $\mathbb{Z}$ and over $\mathbb{Z}_{(2)}$.

* $v_0(x) = 1 \iff x$ odd $\iff x \equiv 1 \pmod 2$. Write $x = 2y+1$; then
  $T(x) = (6y+4)/2 = 3y+2$.
* $v_1(x) = 1 \iff 3y+2$ odd $\iff y$ odd $\iff x \equiv 3\pmod 4$. Write $x = 4z+3$
  (so $y = 2z+1$); then $T(x) = 6z+5$ and $T^2(x) = (18z+16)/2 = 9z+8$.
* $v_2(x) = 1 \iff 9z+8$ odd $\iff z$ odd $\iff x \equiv 7 \pmod 8$. Write $x = 8t+7$
  (so $z = 2t+1$); then $T^2(x) = 18t+17$ and $T^3(x) = (54t+52)/2 = 27t+26$.
* $v_3(x) = 0 \iff 27t+26$ even $\iff t$ even $\iff x \equiv 7\pmod{16}$.

In that case $T^4(x) = (27t+26)/2$ and, substituting $t = (x-7)/8$,
$$T^4(x) = \frac{27\frac{x-7}{8}+26}{2} = \frac{27x - 189 + 208}{16} = \frac{27x+19}{16}.$$
(Each division above is by $2$ applied to a quantity just shown to be even, so all steps are
legitimate in $\mathbb{Z}_{(2)}$.) $\square$

**(2)** With $x \equiv 7 \pmod{16}$,
$$11\,T^4(x) + 19 = \frac{11(27x+19)}{16} + 19 = \frac{297x + 209 + 304}{16}
= \frac{297x + 513}{16} = \frac{27(11x+19)}{16},$$
using $27\cdot11 = 297$ and $27\cdot19 = 513$. $\square$

**(3)** Induction on $N$. $N = 0$: both sides are vacuously true ($16^0 = 1$ divides
everything, and the empty word condition is vacuous).

*($\Rightarrow$).* Let $N \ge 1$ and suppose $(v_0,\dots,v_{4N-1})(x) = (1110)^N$. By (1),
$x \equiv 7\pmod{16}$, so $11x + 19 \equiv 11\cdot7+19 = 96 \equiv 0 \pmod{16}$; and
$x' := T^4(x) = (27x+19)/16$ has $(v_0,\dots,v_{4N-5})(x') = (1110)^{N-1}$ (parities of
$T^4(x)$ are $v_{4+i}(x)$). By the inductive hypothesis $16^{N-1}\mid 11x'+19$, and by (2)
$11x'+19 = 27(11x+19)/16$, so $16^{N-1}\cdot 16 \mid 27(11x+19)$; since $\gcd(27,16)=1$,
$16^{N}\mid 11x+19$.

*($\Leftarrow$).* Let $16^N \mid 11x+19$ with $N \ge 1$. Then $16 \mid 11x+19$, so
$11x \equiv -19 \equiv -3 \pmod{16}$; as $11\cdot3 = 33 \equiv 1 \pmod{16}$, $11^{-1} = 3$
and $x \equiv -9 \equiv 7 \pmod{16}$. By (1) the first four parities are $(1,1,1,0)$ and
$x' = T^4(x) = (27x+19)/16$; by (2), $11x'+19 = 27(11x+19)/16$ is divisible by
$16^{N}/16 = 16^{N-1}$. By induction $(v_0,\dots,v_{4N-5})(x') = (1110)^{N-1}$, and
prepending the four parities just computed gives $(v_0,\dots,v_{4N-1})(x) = (1110)^N$.
$\square$

**(4)** By (3), $x \in S_N \iff x \in \mathbb{Z}^+$ and $x \equiv -19\cdot 11^{-1}
\pmod{16^N}$ (legitimate: $\gcd(11,16)=1$). So $S_N$ is one residue class mod $2^{4N}$
intersected with $\mathbb{Z}^+$, $R_N = 1$, and $S_N$ is infinite. Its least positive element
is the least positive residue $r_N := (-19\cdot 11^{-1})\bmod 16^N$, and $r_N \ne 0$ because
$r_N = 0$ would give $16^N \mid 19$, false for $N \ge 1$. Refinement is automatic
($16^{N+1}\mid 11x+19 \Rightarrow 16^N \mid 11x+19$). $\square$

**(5)** By (3), $x \in \bigcap_N S_N$ iff $x \in \mathbb{Z}^+$ and $16^N \mid 11x+19$ for
every $N$; by Lemma A.0(iv) this forces $11x + 19 = 0$, i.e. $x = -19/11 \notin
\mathbb{Z}^+$. So $\bigcap_N S_N = \emptyset$, and by L-9918.1(3), $m_N = r_N \to \infty$.
$\square$

**(6)** $z^* := -19/11 \in \mathbb{Z}_{(2)}$ since $11$ is odd. Then $11z^*+19 = 0$ is
divisible by $16^N$ for every $N$, so $\pi_{4N}(z^*) = r_N$ for every $N$, i.e.
$z^* \in \widehat S_\infty$; and $\widehat S_\infty$ is a single point because $R_N = 1$ and
the balls have radius $\to 0$ (Lemma A.0(iv)). The exact orbit:

| $x$ | numerator parity | $T(x)$ |
|---|---|---|
| $-19/11$ | odd | $(3(-19/11)+1)/2 = (-57+11)/22 = -23/11$ |
| $-23/11$ | odd | $(-69+11)/22 = -29/11$ |
| $-29/11$ | odd | $(-87+11)/22 = -38/11$ |
| $-38/11$ | even | $-19/11$ |

so the parities are $(1,1,1,0)$ and $T^4(z^*) = z^*$: $V(z^*) = (1110)^\infty$. Finally
$z^*$ is the unique fixed point of $x \mapsto (27x+19)/16$, since $16x = 27x+19 \iff
-11x = 19$. $\square$

*(Every assertion of L-9918.4 is re-verified by exact rational arithmetic in T1, including
the four-cycle, the identity $T^4 = (27x+19)/16$, the residues $r_N$ for $N \le 8$, and a
brute-force confirmation that $S_1, S_2$ are exactly the predicted classes.)*

### Proof of L-9918.5

**(1)** Composition: if $\Phi^p(x) = (A_wx+\kappa_w)/M^p$ and $\Phi^q(y) =
(A_{w'}y+\kappa_{w'})/M^q$ then
$$\Phi^{p+q}(x) = \frac{A_{w'}\frac{A_wx+\kappa_w}{M^p}+\kappa_{w'}}{M^q}
= \frac{A_wA_{w'}x + A_{w'}\kappa_w + M^p\kappa_{w'}}{M^{p+q}},$$
so $A_{ww'} = A_wA_{w'}$ and $\kappa_{ww'} = A_{w'}\kappa_w + M^{p}\kappa_{w'}$.
*(Reviewer's note, fable-02-v20: this composition step uses, besides (AF2), the
**finite-level** form of shift equivariance — for admissible $ww'$ and every $x$ in the
class $c(ww')$, $\Phi^{p}(x)$ lies in $c(w')$ — whereas (AF3) as stated asserts the shift
property only on $\widehat S_\infty$. It holds in E1, in E2 and in every $M$-adic affine
branch system, and should be read as part of (AF3); it is also what makes the iterates in
(AF2) well defined. **Nothing below depends on it:** the identity actually used in (2)–(6),
$(M^p - A_w)z = \kappa_w$, is obtained in the next paragraph from (AF2), (AF3) on
$\widehat S_\infty$, and separation of addresses alone.)* Iterating
with $w' = w^{k-1}$ gives $A_{w^k} = A_w^k$ and, by induction,
$\kappa_{w^k} = \kappa_w\sum_{i=0}^{k-1}A_w^{\,k-1-i}M^{\,pi} = \kappa_w\frac{A_w^k -
M^{pk}}{A_w - M^p}$ (a finite geometric identity; if $A_w = M^p$ the quotient is read as
$k A_w^{k-1}$, but that case cannot occur by (2)).

Now let $z$ have address $w^\infty$. By (AF3) the address of $\Phi^p(z)$ is the shift of
$w^\infty$ by $p$, which is $w^\infty$ again. Addresses separate points: if $y, z$ have the
same address then $\pi_N(y) = c(w|_N) = \pi_N(z)$ for all $N$, so $y = z$. Hence
$\Phi^p(z) = z$, and by (AF2) $M^pz = A_wz + \kappa_w$. $\square$

**(2)** $M^p - A_w \equiv -A_w \pmod M$ and $\gcd(A_w, M) = 1$ (AF2), so
$\gcd(M^p - A_w, M) = 1$. In particular $M^p - A_w \ne 0$ (as $\gcd(0,M) = M \ge 2$); note
this also shows $A_w \ne M^p$, so every admissible word is sub- or supercritical. By Lemma
A.0(iii), $M^p - A_w$ is a unit of $\mathbb{Z}_M$, so the equation of (1) has the unique
solution $z_w = \kappa_w(M^p-A_w)^{-1}$, which as a rational number is
$\kappa_w/(M^p-A_w)$; its lowest-terms denominator divides $M^p - A_w$. $\square$

**(3)** Immediate from $\kappa_w \ge 0$ (AF2) and the sign of $M^p - A_w$: if
$A_w > M^p$ the denominator is negative. For $z_w \in \mathbb{Z}^+$ we need $z_w > 0$
(forcing $\kappa_w>0$ and $A_w<M^p$) and $z_w \in \mathbb{Z}$ (forcing
$(M^p-A_w)\mid\kappa_w$). $\square$

**(4)** Suppose $x \in \bigcap_N S_N$ has eventually periodic address $u\,w^\infty$ with
$|u| = \ell \ge 0$, $|w| = p \ge 1$. Put $y := \Phi^\ell(x)$. By (AF4) and induction,
$y \in \mathbb{Z}^+$; by (AF3), the address of $y$ is $w^\infty$. If $\kappa_w = 0$ then
$y = 0 \notin\mathbb{Z}^+$ by (2)–(3), a contradiction. If $\kappa_w > 0$ then $w$ is
supercritical by hypothesis, so $y = z_w < 0$ by (3), again a contradiction. Hence no such
$\ell, p$ exist. $\square$

**(5)** *(a)* For E2, $A_w = 3^{|w|_1}$ is odd, $M = 2$: (AF2) holds, and the recursion
$\kappa_{wb} = 3^b\kappa_w + b2^{|w|}$ (the case $|w'| = 1$ of (1), with $A_{(b)} = 3^b$,
$\kappa_{(b)} = b$, since $T(x) = (3^bx+b)/2$ on the branch $b$) gives $\kappa_w \ge 0$ by
induction, with $\kappa_w > 0$ as soon as some letter is $1$. The threshold $A_w < M^p$ reads
$3^a < 2^K$, i.e. $a/K < \log_3 2 = \gamma$. *(b)* For E1, $A_w = P^{p}$ with
$\gcd(P,Q) = 1$, $M^p = Q^p$, and $P > Q$ gives $A_w > M^p$ for every $p \ge 1$;
$\kappa_w = c_w = \sum_{j<p}P^{p-1-j}Q^j\alpha_j > 0$ since all digits are positive. *(c)*
Direct from L-9918.4: $A_w = 27$, $M^p = 2^4 = 16$, $\kappa_w = 19$, $z_w = 19/(16-27) =
-19/11$. $\square$

**(6)** By (AF2) applied to the prefix $w|_n$ of the address of $x$,
$\Phi^n(x) = (A_{w|n}x + \kappa_{w|n})/M^n \ge (A_{w|n}/M^n)\,x \ge \lambda^n x$ using
$\kappa \ge 0$. $\square$

### Proof of L-9918.6

Everything is proved from scratch; the only inputs are the two Fejér facts below and Abel
summation.

**Step 0 (Fejér positivity).** For an integer $h \ge 0$ and $t \in \mathbb{R}$,
$$\Big|\sum_{j=0}^{h}e(jt)\Big|^2 = \sum_{j,k=0}^{h}e\big((j-k)t\big)
= \sum_{|d|\le h}(h+1-|d|)\,e(dt) = (h+1)\,K_h(t),$$
(the middle step counts the pairs $(j,k)$ with $j-k = d$, of which there are $h+1-|d|$), so
$$\textbf{(F1) } K_h \ge 0, \qquad \textbf{(F2) } K_h(0) = h+1 .$$

**Step 1 (second-moment bound; proof of (1)).** With $S(0) = R$ and $S(-k) =
\overline{S(k)}$,
$$\sum_{|k|\le h}\Big(1-\frac{|k|}{h+1}\Big)|S(k)|^2
= \sum_{|k|\le h}\Big(1-\frac{|k|}{h+1}\Big)\sum_{r,r'}e\big(k(\theta_r-\theta_{r'})\big)
= \sum_{r,r'}K_h(\theta_r-\theta_{r'}) \;\ge\; \sum_{r}K_h(0) = R(h+1),$$
where the inequality discards the off-diagonal terms, all $\ge 0$ by (F1), and the last
equality is (F2). Isolating $k = 0$ and bounding the remaining weights by $1$,
$$R^2 + 2\sum_{k=1}^{h}|S(k)|^2 \;\ge\; R(h+1),
\qquad\text{i.e.}\qquad \sum_{k=1}^{h}|S(k)|^2 \ge \frac{R(h+1-R)}{2}.$$
Since $|S(k)|\le R$ we have $|S(k)|^2 \le R|S(k)|$, so
$T(h) = \sum_{k\le h}|S(k)| \ge \frac1R\sum_{k\le h}|S(k)|^2 \ge \frac{h+1-R}{2}$; and
$T(h)\ge0$ trivially. $\square$

**Step 2 (Abel summation; proof of (2)).** Put $T(0) := 0$. For $H \ge 1$,
$$\sum_{h=1}^{H}\frac{|S(h)|}{h} = \sum_{h=1}^{H}\frac{T(h)-T(h-1)}{h}
= \frac{T(H)}{H} + \sum_{h=1}^{H-1}T(h)\Big(\frac1h-\frac1{h+1}\Big)$$
(rearranging the two sums and using $T(0) = 0$). Assume $H \ge R$. Using $T(h)\ge0$ for
$h < R$ and Step 1 for $h \ge R$,
$$\sum_{h=1}^{H}\frac{|S(h)|}{h} \;\ge\; \frac{H+1-R}{2H}
+ \frac12\sum_{h=R}^{H-1}\frac{h+1-R}{h(h+1)} .$$
Now $\frac{h+1-R}{h(h+1)} = \frac1h - R\big(\frac1h-\frac1{h+1}\big)$, so the second sum
telescopes:
$$\sum_{h=R}^{H-1}\frac{h+1-R}{h(h+1)} = \sum_{h=R}^{H-1}\frac1h - R\Big(\frac1R-\frac1H\Big)
\;\ge\; \log\frac HR - 1 + \frac RH,$$
using $\sum_{h=R}^{H-1}\frac1h \ge \int_R^H\frac{dx}{x} = \log\frac HR$ (each term
$\frac1h \ge \int_h^{h+1}\frac{dx}{x}$). Adding,
$$\sum_{h=1}^{H}\frac{|S(h)|}{h} \ge \frac12\Big(1-\frac RH+\frac1H\Big)
+ \frac12\Big(\log\frac HR - 1 + \frac RH\Big) = \frac12\Big(\log\frac HR + \frac1H\Big).
\qquad\square$$

**Step 3 (proof of (3)).** For $H \ge R$ this follows from (2) since $1/H > 0$. For
$1 \le H < R$ the right-hand side $\frac12\log(H/R)$ is $< 0$ while the left-hand side is a
sum of non-negative terms, hence $\ge 0$. $\square$

**Step 4 (sharpness, (4)).** For $\theta_r = r/R$ ($r = 1,\dots,R$), $S(h) = R$ if
$R \mid h$ and $0$ otherwise (a full geometric sum). Hence
$\sum_{h\le H}|S(h)|/h = \sum_{k \le H/R}\frac{R}{kR} = \sum_{k\le\lfloor H/R\rfloor}\frac1k$,
which lies in $[\log(H/R), \log(H/R)+1]$ for $H \ge R$. $\square$

**Step 5 (proof of (5): no invisible point set).** Let $z_r := e(\theta_r)$, so
$p_h := \sum_r z_r^h = S(h)$. Suppose $S(1) = \dots = S(R) = 0$. Newton's identities
$k\,e_k = \sum_{i=1}^{k}(-1)^{i-1}e_{k-i}p_i$ (valid over $\mathbb{C}$, characteristic $0$)
give, by induction on $k = 1,\dots,R$, that all elementary symmetric functions
$e_1 = \dots = e_R = 0$; hence $\prod_{r}(X - z_r) = X^R$, forcing every $z_r = 0$,
contradicting $|z_r| = 1$. So $S(h) \ne 0$ for some $h \le R$. Sharpness: the equally spaced
set has $S(1) = \dots = S(R-1) = 0$. $\square$

**Hostile quantifier audit (what was attempted and what survived).** *(i)* Multisets with
repetitions: allowed — the diagonal in Step 1 has $R$ terms whatever the multiplicities, so
repetition only helps. *(ii)* $R = 1$: $|S(h)| = 1$ for all $h$, LHS $= \sum_{h\le H}1/h
\ge \log H \ge \frac12\log H$. *(iii)* All points equal: $|S(h)| = R$, LHS $=
R\sum_{h\le H}1/h$, enormous. *(iv)* $H < R$: handled in Step 3; the inequality is true but
vacuous. *(v)* Could an adversary make $|S(h)|$ small on the harmonically-heavy small $h$?
Step 1 constrains $\sum_{k\le h}|S(k)|^2$ at **every** $h$, so smallness at small $h$ is
paid for at once; the equally-spaced set is the extremal attempt and loses by a factor
$\le 2$. *(vi)* Numerical search (T3) over structured, random, low-discrepancy, degenerate
and locally optimised configurations, and over all $H \le 64R$, found minimum ratio
$2.274$ (structured) and $2.446$ (local search) against the bound — **no violation, and no
configuration beating the arithmetic progression.** *(vii)* Attempted weakening of the
hypotheses: the hypothesis $H \ge R$ is **not** needed for form (3) — corrected, and the
corrected form is what is used in L-9918.7.

### Proof of L-9918.7

**(b)** All three terms on the right of (ET) are non-negative ($\beta \ge 0$, $|S(h)|\ge0$),
so if their sum is $< 1$ each is $< 1$; in particular $C_1R\varphi(H)/H < 1$. $\square$

**(c)** From (b), $C_1\varphi(uR)/u < 1 - R\beta - C_2\Sigma$ where
$\Sigma := \sum_{h\le H}|S(h)|/h$; and $C_2\Sigma \ge \frac{C_2}{2}(\log u)_+$ by
L-9918.6(3) together with $\Sigma \ge 0$. Adding the two lower bounds for the two
non-negative terms gives ($\dagger$). $\square$

**(d)** Write $G(u) = C_1/u$ for $0 < u \le 1$ and $G(u) = C_1/u + \frac{C_2}{2}\log u$ for
$u \ge 1$ (the two formulas agree at $u=1$, so $G$ is continuous). On $(0,1]$, $G$ is
strictly decreasing with infimum $C_1 = G(1)$, attained. On $[1,\infty)$,
$$G'(u) = -\frac{C_1}{u^2} + \frac{C_2}{2u} = \frac{C_2u/2 - C_1}{u^2},$$
which vanishes only at $u^* = 2C_1/C_2$, is negative for $u < u^*$ and positive for
$u > u^*$. Hence:

* if $u^* \le 1$ (i.e. $2C_1 \le C_2$), $G$ is non-decreasing on $[1,\infty)$ and
  $\Theta = G(1) = C_1$;
* if $u^* > 1$ (i.e. $2C_1 > C_2$), $\Theta = G(u^*) = \frac{C_1}{u^*}+\frac{C_2}{2}\log u^*
  = \frac{C_2}{2} + \frac{C_2}{2}\log\frac{2C_1}{C_2} = \frac{C_2}{2}\big(1+\log\frac{2C_1}
  {C_2}\big)$, and this is $\le G(1) = C_1$.

This is the displayed formula for $\Theta$, and ($\dagger$) is satisfiable for some $u$ iff
$\Theta < 1$ (if $\Theta<1$ the infimum is attained or approached, and $G$ is continuous, so
some $u$ has $G(u)<1$; conversely $G(u)<1 \Rightarrow \Theta<1$).

*Region.* In the case $2C_1 > C_2$,
$$\Theta<1 \iff 1+\log\frac{2C_1}{C_2} < \frac{2}{C_2}
\iff \frac{2C_1}{C_2} < e^{2/C_2-1} \iff C_1 < \frac{C_2}{2}e^{2/C_2-1} = \Psi(C_2).$$
*Properties of $\Psi$:* $\Psi'(s) = e^{2/s-1}\big(\frac12-\frac1s\big)$, so $\Psi$ strictly
decreases on $(0,2)$, strictly increases on $(2,\infty)$, with $\Psi(2) = 1$; hence
$\Psi \ge 1$ everywhere, with equality only at $s=2$. Also $\Psi(s) > s/2 \iff e^{2/s-1}>1
\iff s<2$.

*Case $C_2 \ge 2$.* Then $\Psi(C_2)\le C_2/2$. If $2C_1>C_2$ then $C_1 > C_2/2 \ge
\Psi(C_2)$, so $\Theta \ge 1$: inadmissible. So admissibility forces $2C_1\le C_2$, where
$\Theta = C_1$, i.e. $C_1<1$. Conversely $C_1<1\le C_2/2$ gives $2C_1<C_2$ and
$\Theta = C_1<1$. Hence: admissible $\iff C_1<1$.

*Case $C_2<2$.* Then $\Psi(C_2) > \max(1, C_2/2)$. If $2C_1\le C_2$ then
$C_1\le C_2/2<1$, so $\Theta = C_1<1$: admissible, and also $C_1<\Psi(C_2)$. If
$2C_1>C_2$ then admissible $\iff C_1<\Psi(C_2)$ as shown. In both sub-cases,
admissible $\iff C_1<\Psi(C_2)$.

The two cases are the boxed statement. The listed values of $\Psi$ are direct evaluations:
$\Psi(2/\pi) = \frac1\pi e^{\pi-1} = 2.709767\ldots$, $\Psi(1) = \frac12 e$,
$\Psi(2) = 1$. $\square$

**(e)** For $(C_1,C_2) = (1,2/\pi)$: $G(u) = 1/u$ on $(0,1]$, so $G \ge 1$ there with
equality only at $u=1$;
on $[1,\infty)$, $G(u) = 1/u + \frac1\pi\log u$, strictly decreasing on $[1,\pi]$ and
strictly increasing on $[\pi,\infty)$ with $G(\pi) = \frac{1+\log\pi}{\pi} = 0.682689\ldots$
and $G\to\infty$. Hence $\{G<1\} = (1, u_+)$ with $u_+$ the unique root of
$1/u + \frac1\pi\log u = 1$ in $(\pi,\infty)$; bisection gives $u_+ = 19.73524\ldots$ (T5).
The cusp budget follows from rearranging (ET)$<1$: $\Sigma < \frac{1}{C_2}\big(1 - R\beta -
\frac{C_1}{u}\big)$, which at $u = \pi$ and $R\beta\to0$ is
$\frac\pi2\big(1-\frac1\pi\big) = 1.070796\ldots$. Since $G$ is strictly unimodal, $\{G<1\}$
is an interval in general. $\square$

**(f)** Let $R \ge 1$, $H \ge 3$, $u := H/R$, and
$$\Lambda := 4\frac{R\log(4H)}{H} + \frac1\pi\Big(\log\frac HR\Big)_+
= \frac{4\log(4H)}{u} + \frac{(\log u)_+}{\pi}.$$
Two standing facts: $H \ge 3$, and $H = uR \ge u$ because $R \ge 1$; hence
$H \ge \max(3, u)$ and $\log(4H) \ge \log\big(4\max(3,u)\big)$. Write $a := 4\log 12 =
9.9396266\ldots$

*Case $u \le 3$.* Then $\Lambda \ge \frac{4\log(4H)}{u} \ge \frac{4\log 12}{u}
= \frac{a}{u} \ge \frac{a}{3} = 3.313209 > 1.413697$.

*Case $u > 3$.* Then $\log(4H) \ge \log(4u) \ge \log 12$, so
$$\Lambda \;\ge\; \psi(u) := \frac{a}{u} + \frac{\log u}{\pi}.$$
$\psi'(u) = -a/u^2 + 1/(\pi u)$ vanishes only at $u_0 = a\pi = 31.226258\ldots$, and is
negative for $u < u_0$, positive for $u > u_0$; since $u_0 > 3$, the minimum of $\psi$ on
$(3,\infty)$ is
$$\psi(u_0) = \frac{a}{a\pi} + \frac{\log(a\pi)}{\pi} = \frac{1 + \log(a\pi)}{\pi}
= \frac{1 + \log(4\pi\log 12)}{\pi} = \frac{4.4412593\ldots}{\pi} = 1.4136968\ldots$$

Combining, $\Lambda > 1.413696 > 1$ for every $R \ge 1$ and every $H \ge 3$, so ($\dagger$)
fails and (ET) with these data never fires. *(For the only integer cut-offs not covered,
$H \in \{1,2\}$, the resolution term alone already exceeds $1$: it equals $4R\log 4 \ge
5.545$ at $H=1$ and $2R\log 8 \ge 4.158$ at $H=2$, so (ET) cannot fire there either and
the restriction $H \ge 3$ costs nothing. Added by fable-02-v20.)*
(The bound is uniform in $R$; the true minima
computed in T5 are $1.6678$ at $R=1$, $1.7727$ at $R=6$, $2.0891$ at $R=10^6$ — all above
the proved threshold, as they must be.) $\square$

**(g)** By (d) with $C_2 = 2/\pi < 2$: admissible $\iff C_1 < \Psi(2/\pi) = e^{\pi-1}/\pi =
2.709767\ldots$. For $C_1 = 4$: $2C_1 = 8 > 2/\pi$, so
$\Theta = \frac1\pi\big(1+\log(4\pi)\big) = 1.123960 > 1$. For $(C_1,C_2) = (1,3)$:
$2C_1 = 2 < 3 = C_2$, so $\Theta = C_1 = 1$, not $<1$. $\square$

> **Scope of L-9918.7 (proved-in limitations, to be quoted with the result).**
> **(L1)** The barrier attaches to the step in which the exponential sums enter through
> $|S(h)|$. A method that keeps the phases (e.g. bounds $\big|\sum_h \widehat\Psi(h)S(h)\big|$
> directly, exploiting cancellation between frequencies) is **not** covered by L-9918.6 and
> hence not by L-9918.7.
> **(L2)** The barrier assumes a **single** cut-off $H$ and a resolution term of the exact
> shape $C_1R\varphi(H)/H$. Multi-scale decompositions, second-moment/large-sieve arguments,
> majorising the union of classes directly instead of counting $R$ points against one arc,
> and lattice-reduction arguments are all untouched.
> **(L3)** Nothing here asserts that no ET-shape inequality with admissible constants exists;
> (d) describes exactly which constants *could* work, and Q-9916b-type questions about
> Beurling–Selberg majorants remain open elsewhere in the repository.

### Proof of L-9918.8

**(1)** By orthogonality of additive characters mod $M^k$
($\sum_{v \bmod M^k}e(vn/M^k) = M^k$ if $M^k \mid n$, else $0$),
$$\sum_{v \bmod M^k}|g(v)|^2 = \sum_{\alpha,\alpha'\in D}\ \sum_{v\bmod M^k}
e\big(v(\alpha-\alpha')/M^k\big) = M^k\,\#\{(\alpha,\alpha')\in D^2 : \alpha=\alpha'\}
= d\,M^k,$$
using that the elements of $D$ are pairwise distinct mod $M^k$. Divide by $M^k$. Since
$g(0) = d$ and the mean square is $d \le d^2$, we get $\max_v|g(v)| = d \ge \sqrt d$.
$\square$

**(2)** Let $X := |g(v)|^2$ for $v$ uniform mod $M^k$, so $0 \le X \le d^2$ and
$\mathbb{E}X = d$. With $p := \Pr(X>\lambda)$,
$$d = \mathbb{E}X \le \lambda(1-p) + d^2 p \le \lambda + (d^2-\lambda)p
\ \Longrightarrow\ p \ge \frac{d-\lambda}{d^2-\lambda}. \qquad\square$$

**(3)** Identical computation with $D$ replaced by the set of root representatives
$\{r_c : c\in C_N\}$, distinct mod $M^N$, and $k$ by $N$. $\square$

**(4)** The per-level mean squares are $d_j$ by (1), and their product is $\prod_j d_j =
R_N$; the global mean square is $R_N$ by (3). They are equal, so the "independence" estimate
$\mathbb{E}|\widehat S_N|^2 \approx \prod_j \mathbb{E}|G_j|^2$ is an identity, not an
inequality with slack: no decay is available from per-level second moments. Since
$\mathbb{E}|\widehat S_N|^2 = R_N$ forces $|\widehat S_N(h)|$ to be of typical size
$\sqrt{R_N}$ over all frequencies, any bound $|\widehat S_N(h)| = O(1)$ can only hold on a
set of frequencies of density $O(1/R_N)$ — in particular on the low-frequency window
$h \le H$ with $H/M^N$ small — and must use the joint structure of the arguments across
levels. $\square$

### Proof of L-9918.9

Fix a Turing machine index $e$ and let $t(e) \in \mathbb{Z}^+\cup\{\infty\}$ be the number of
steps until $e$ halts on empty input ($\infty$ if it never halts). Define, for $N \ge 0$,
$$c_N := \big(2^{\min(N,\,t(e))}-1\big) \bmod 2^N \in \mathbb{Z}/2^N\mathbb{Z},
\qquad C_N := \{c_N\},\qquad M := 2,\ R_N = 1 .$$
This is computable in $(e,N)$: simulate $e$ for $N$ steps; if it has halted by step
$t \le N$, output $2^{t}-1$, else output $2^N-1$.

*Refinement.* If $N < t(e)$: $c_{N+1} = 2^{N+1}-1$ and $2^{N+1}-1 = 2^N + (2^N-1) \equiv
2^N-1 = c_N \pmod{2^N}$. If $N \ge t(e)$: $c_{N+1} = 2^{t(e)}-1 = c_N$ as integers, so the
congruence mod $2^N$ holds. So $(C_N)$ is a cylinder architecture (D-9918.1).

*If $e$ halts*, with $t := t(e) < \infty$: put $x := 2^{t}-1 \in \mathbb{Z}^+$. For
$N \ge t$, $c_N = 2^t-1 = x$, so $x \in S_N$. For $N < t$, $x = 2^t-1 =
2^N(2^{t-N}-1) + (2^N-1) \equiv 2^N-1 = c_N \pmod{2^N}$, so $x \in S_N$. Hence
$x \in \bigcap_N S_N \ne \emptyset$.

*If $e$ does not halt*: $c_N = 2^N-1$ for every $N$, so $S_N = \{x\in\mathbb{Z}^+ :
x \equiv -1 \bmod 2^N\}$ and $m_N = 2^N-1 \to \infty$; by L-9918.1(3),
$\bigcap_N S_N = \emptyset$. (Its adic limit is $-1 \in \mathbb{Z}_2$, a perfectly good
$2$-adic integer that is not a positive integer.)

So $\bigcap_N S^{(e)}_N \ne \emptyset \iff e$ halts, and a decision procedure for extraction
would decide the halting problem. The complexity remarks: with membership decidable,
"$\exists x\,\forall N\ x\in S_N$" is $\Sigma^0_2$, and for fixed $x$, "$\exists N\
x\notin S_N$" is $\Sigma^0_1$. $\square$

---

## Part C — what A and B do and do not say about each exhibited architecture

*(Each entry is a scope statement about this file's theorems only.)*

**E1, six-branch chart (issue #58; L-9916's setting).** A says: the trichotomy collapses —
either a seed exists or $m_N\to\infty$ (L-9918.1); an adic limit always exists, so producing
one is no evidence (L-9918.2); and since $P>Q$ the architecture is supercritical, so any seed
has a not-even-eventually-periodic address (L-9918.5(4),(5b)). B says: an ET-shape counting
certificate needs $H > C_1 R_N\varphi(H)$ and constants inside the region of L-9918.7(d);
Fejér-power data $(4,2/\pi,\log 4H)$ cannot fire, and neither can $(4,2/\pi)$ with the
logarithm removed. A and B do **not** say whether $\bigcap_N S_N$ is empty, do not prove
$m_N\to\infty$, and do not exclude non-ET methods (L1–L3).

**E2, parity-word cylinders (issues #21, #4, #18).** A says: every infinite parity word is
realised adically for free and the entire content of any symbolic construction is
"is the realiser a positive integer" (L-9918.2, L-9918.3); and any word whose odd-step
density exceeds $\gamma$ on a period — i.e. exactly the words a divergence hunt targets —
has a negative periodic realiser, so no eventually periodic address can carry a seed
(L-9918.5(5a)). B applies to any prefix-closed language with $R_N$ words of length $N$ and
says the same thing about counting certificates for it. Neither says anything about the
existence of an aperiodic seed, which is where the whole difficulty lives.

**E3, L-9909 survivor classes.** A says: a seed exists iff $(m_N)$ is eventually constant, and
a seed is exactly an $n$ whose parity word satisfies $3^{a_j(n)} \ge 2^j$ for every $j$ (which
by L-9909.3(a), context only, means $\sigma(n) = \infty$). The computed initial segment is
$m_1,\dots,m_{16} = 1,3,3,7,7,7,27,27,\dots,27$ with $R_N = 1,1,2,3,4,8,13,19,38,\dots$ (T2,
reproducing L-9909.4's counts) — this is finite verification and decides nothing: the
constancy of $m_N$ at $27$ over the computed range is not evidence either way. B's counting
barrier applies verbatim with $R_N$ the survivor count. Nothing here bears on whether
$\sigma(n)=\infty$ is possible.

**E4, the $(1110)^\infty$ architecture.** Fully resolved here, and negatively:
$\bigcap_N S_N = \emptyset$, $m_N\to\infty$, adic limit $-19/11$ (L-9918.4). It is included
as the canonical worked failure of the quantifier interchange, not as a result about
Collatz.

**Adelic/cusp Fourier programmes (issues #15/#16).** L-9918.8 says per-level or
per-factor average bounds are provably unavailable (the mean square of each digit factor is
its cardinality, and the factorisation is mean-square-lossless), so any product-decay
strategy must exploit inter-level correlations and must live in the low-frequency window.
This is a constraint on the shape of the estimate sought, not a statement that no such
estimate exists.

**All programmes.** L-9918.9 says that from the architecture's counting and refinement data
alone the extraction question is undecidable. So the arithmetic replacement targets of
Q-9918 are not a stylistic preference: some architecture-specific arithmetic input is
mathematically unavoidable.

**What none of this does.** It does not resolve any extraction question; it does not prove
$m_N \to \infty$ for any architecture; it produces no counterexample candidate and refutes
none; and it says nothing about the Collatz conjecture.

---

## Dependency audit

| Used | Where | How |
|---|---|---|
| NOTATION.md preamble & conventions ($\mathbb{Z}^+$, $\nu_2$, $\mathbb{Z}_{(2)}$, $\gamma$, empty sums/products, status semantics, "computation is finite verification") | throughout | conventions only |
| NOTATION.md D-9902 ($T$), D-9906 ($v_i,a_k$), D-9907 (divergent), D-9910 ($\sigma$) | L-9918.4, L-9918.5(5a),(6), E2, E3 | definitions only; the extension of $T$ to $\mathbb{Z}_{(2)}$ is re-derived inline |
| L-9904 (PROVED) | §Motivation, E2, and the Relationship table below | **context only.** L-9904.5(i)/(ii)/L-9904.7 are the parity specialisations of L-9918.2/L-9918.5; nothing is imported. The parity facts actually used in L-9918.4 are proved from scratch by explicit congruence refinement (Proof of L-9918.4(1)), not by citing L-9904.2/.3. |
| L-9916 (PROPOSED, under review) | §Motivation, E1, Relationship table | **context only, and re-proved.** Per the commission, nothing from L-9916 is cited as established: L-9918.1 re-proves its L-9916.2 at generality; L-9918.6 re-proves its L-9916.5.2 with a weaker hypothesis; L-9918.7 generalises its L-9916.5.3/.5.4 to arbitrary $(C_1,C_2,\varphi)$; L-9918.8 re-proves its L-9916.5.5; L-9918.5 generalises its L-9916.6. E1's cylinder description is recomputed independently in T2 (and reproduces $m_1,\dots,m_4$). |
| L-9909 (PROVED) | E3, Part C | **context only**; the survivor definition is restated and the classes are recomputed from scratch in T2 (counts $1,1,2,3,4,8,13,19$ reproduced). No statement of L-9909 is used in a proof. |
| Newton's identities over $\mathbb{C}$ | L-9918.6(5) only | standard algebra, stated and used in one line; no other result depends on (5) |
| Undecidability of the halting problem | L-9918.9 only | standard; the reduction is constructed here |

Standard mathematics used without citation, all elementary: finite geometric series;
orthogonality of additive characters on $\mathbb{Z}/M^k\mathbb{Z}$; Abel summation;
$\sum_{h=R}^{H-1}1/h \ge \log(H/R)$; single-variable calculus (first-derivative tests);
the well-ordering of $\mathbb{Z}^+$.

**Relationship to the specialised ancestors (explicit, as commissioned).**

| This file | Specialised ancestor | Relationship |
|---|---|---|
| L-9918.1 | L-9916.2 (PROPOSED) | strict generalisation ($M$, arbitrary $R_N$); re-proved from scratch; adds (3)(iii$'$) and (4) |
| L-9918.2 | L-9904.5(i)+L-9904.7 (PROVED, parity case) | strict generalisation to any base $M$ and any $R_N$; the parity case is $M=2$, $R_N=1$ |
| L-9918.3 | — (new) | isolates the exact repair of the quantifier interchange |
| L-9918.4 | L-9904.5(ii) anchors | new worked architecture; re-proved from scratch |
| L-9918.5 | L-9904.5(ii) sign clause; L-9916.6 | strict generalisation; both are specialisations (5a),(5b) |
| L-9918.6 | L-9916.5.2 (PROPOSED) | re-proved; hypothesis $H\ge R$ removed; sharper form and part (5) added |
| L-9918.7 | L-9916.5.3/.5.4 (PROPOSED) | strict generalisation to all $(C_1,C_2,\varphi)$ and all $R\ge1$; adds the exact admissible region and the finding (g) that removing the $\log$ is not sufficient |
| L-9918.8 | L-9916.5.5 (PROPOSED) | re-proved for any $M$, $d$; adds the tail bound (2) and the losslessness statement (4) |
| L-9918.9 | — (new) | — |

No result of this file is used by any of its dependencies, and none of the cited files cites
this one: no circularity.

---

## Gap audit

* **Hidden finiteness.** The only finiteness used in Part A is *finiteness of each level*
  ($C_N$ finite), which is part of D-9918.1 and is what makes the König argument of
  L-9918.2(3) work; and *finiteness of $[1,B]$*, used in L-9918.1(3) to upgrade the
  pointwise statement (iii$'$) to (ii$'$). Both are stated where used. No proof extrapolates
  from a computation.
* **Unjustified induction.** The inductions (L-9918.4(3); L-9918.5(1); the chain
  construction in L-9918.2(3); Newton's identities in L-9918.6(5)) each have an explicit base
  case and an identity-or-inclusion step; the chain construction is a genuine dependent
  choice over $\mathbb{N}$ with all choice sets nonempty and finite, so no choice principle
  beyond finite choice per level is used.
* **Boundary cases.** $N = 0$ ($C_0$ is the single class $\mathbb{Z}/1$, $S_0 = \mathbb{Z}^+$,
  $m_0 = 1$); $R_N = 1$ vs $R_N > 1$ (both exhibited); $H < R$ in L-9918.6(3) (handled
  separately); $H = R$ (the Abel split is at $h = R$ and the sum $\sum_{h=R}^{H-1}$ may be
  empty, in which case the telescoped bound reads $\log 1 - 1 + 1 = 0$, still valid);
  $u \le 1$ in L-9918.7 (where $(\log u)_+ = 0$ and only the resolution term constrains);
  $2C_1 = C_2$ exactly (first branch of $\Theta$, $u^* = 1$); $\kappa_w = 0$ in L-9918.5
  (realiser $0$, excluded from $\mathbb{Z}^+$); $A_w = M^p$ (proved impossible);
  $\beta \in \{0,1\}$ in (ET) (never divided by); $d = 1$ in L-9918.8 (mean square $1$,
  bound (2) reads $p \ge (1-\lambda)/(1-\lambda) = 1$ for $\lambda<1$, correct since
  $|g|\equiv1$).
* **Confusion of empirical and universal.** Every table is labelled. T1–T5 verify proved
  statements; **no proof cites a computation.** The only empirical statements in the file are:
  the numerical minima in L-9918.7(f)'s parenthesis (the *proved* bound there is
  $1.413696$; corrected from a stale draft value by fable-02-v20),
  the consistency figures in Q-9918a, the $m_N$/survivor tables in Part C and T2, and the
  search results in the hostile audit of L-9918.6.
* **Invalid interchange of limits.** None taken. The only limits are $m_N\to\infty$ (monotone),
  $M^{-K}\to0$ in Lemma A.0(ii)/L-9918.2(1), and $\bigcap_N M^N\mathbb{Z}_M = \{0\}$; each is
  from an explicit monotone bound. The *quantifier* interchange is the subject of the file and
  is nowhere performed illegitimately — L-9918.3 states exactly when it is legal.
* **Circular dependence.** None; see the audit table. L-9918.7 uses L-9918.6, which uses only
  Fejér positivity; L-9918.7 does not use any (ET) inequality's truth, only its shape.
* **Nonuniform estimates.** All constants in Part B are absolute: $\tfrac12$ in L-9918.6;
  $\Theta$, $\Psi$, $e^{\pi-1}/\pi$, $19.73524$, $1.070796$, $1.413696$ in L-9918.7. None
  depends on $N$, $R$, $H$ or on the point set. The bound in (f) is uniform in $R\ge1$.
* **Assumptions equivalent to Collatz.** None. No statement of this file asserts anything
  about Collatz; E2/E3/E4 are architectures *built from* $T$, and the theorems about them are
  conditional structure statements.
* **Incorrectly assumed independence.** Explicitly refuted rather than assumed: L-9918.8(4)
  proves the independence heuristic is exactly Parseval-tight and therefore useless, and it
  is used only to argue *against* optimism.
* **Unproved properties of an infinite rewrite sequence.** L-9918.5(4) is precisely a warning
  of this type: in a supercritical architecture any seed's address is not eventually periodic,
  so no finite periodic certificate can exist for it. L-9918.4 is the worked instance where
  the infinite object exists adically and fails to be an integer.
* **Finite computation extrapolated to infinite behaviour.** Deliberately avoided. In
  particular the E3 table (constant $m_N = 27$ for $7\le N\le16$) is explicitly *not* read as
  evidence of a seed, and Q-9918a's consistency figures at $N\le4$ are explicitly *not* read
  as evidence for the target.
* **Symbolic object $\to$ actual positive integer.** This is the file's subject.
  L-9918.2(4) states the exact reduction; L-9918.4 exhibits a symbolic object with infinitely
  many finite integer realisations and no infinite one; L-9918.5(3) gives the three separate
  conditions ($\kappa_w>0$, subcriticality, divisibility) that a periodic symbolic object must
  satisfy to be a positive integer.
* **Known weak point.** The constant $\tfrac12$ in L-9918.6 is not proved optimal (§Remaining
  uncertainty (1)); improving it to $c$ replaces $C_2/2$ by $cC_2$ throughout L-9918.7(d) and
  the admissibility threshold $\Psi$ by $\Psi_c(s) = cs\,e^{1/(cs)-1}$, which at the relevant
  value $C_2 = 2/\pi$ is *smaller* for $c = 1$ than for $c = \tfrac12$ — i.e. the improvement
  would **shrink** the admissible region and strengthen the barrier. Nothing in the file
  depends on optimality, and the direction of the dependence is recorded so that a reviewer
  who improves L-9918.6 knows it cannot weaken L-9918.7.

---

## Adversarial tests

All scripts are Python 3 standard library only; exact integer/rational arithmetic for every
decision, floats only where a proved identity is checked numerically. They live in the
session scratchpad as
`t1_word.py`, `t2_arch.py`, `t3_lowerbound.py`, `t4_parseval.py`, `t5_region.py`,
and are reproduced **in full** below, each immediately followed by its **verbatim captured
stdout**. A self-check harness (`selfcheck.py`, §T6) re-extracts every code block from this
file, re-runs it, and diffs against the recorded output; its result is recorded at the end of
this section.

### T1 — the $(1110)^\infty$ realiser, its exact $4$-cycle, and its cylinder architecture

```python
#!/usr/bin/env python3
# T1 (L-9918, A.3): the periodic parity word (1110)^inf, its unique 2-adic
# realiser -19/11, the exact 4-cycle of rationals, and the cylinder
# architecture (M=2, R_N=1) it generates.  Exact arithmetic throughout.
from fractions import Fraction as F

def is_odd(z):                     # parity in Z_(2): denominator is odd
    return z.numerator % 2 == 1

def T(z):                          # shortcut map, D-9902, on Z_(2)
    return (3*z+1)/2 if is_odd(z) else z/2

def word(z, k):
    w = []
    for _ in range(k):
        w.append(1 if is_odd(z) else 0); z = T(z)
    return tuple(w)

def rho(w):                        # rho(w) = sum_{i: w_i=1} 3^{s_i} 2^i
    return sum(3**sum(w[i+1:]) * 2**i for i in range(len(w)) if w[i] == 1)

w = (1, 1, 1, 0); K = len(w); a = sum(w)
print("word w = %s   K = %d   a = %d" % (str(w), K, a))
print("rho(w) = %d      2^K - 3^a = %d" % (rho(w), 2**K - 3**a))

# (1) the four-step map along w is x -> (27x+19)/16, verified as an identity
#     2^K T^K(z) = 3^a z + rho(w)  on every z whose length-K word is w
z0 = F(-19, 11)
print("realiser z0 = %s ; z0 in Z? %s ; z0 > 0? %s" % (z0, z0.denominator == 1, z0 > 0))
print("word(z0, 16) = %s" % (str(word(z0, 16)),))
print("word(z0,16) == (1110)^4 : %s" % (word(z0, 16) == w*4,))
print("T^4(z0) == z0 : %s" % (T(T(T(T(z0)))) == z0,))
orb = [z0]
for _ in range(4):
    orb.append(T(orb[-1]))
print("exact 4-cycle: %s" % (" -> ".join(str(x) for x in orb),))
print("parities along the cycle: %s" % ([1 if is_odd(x) else 0 for x in orb[:4]],))
print("fixed point of x -> (27x+19)/16 : %s" % (F(19, 16-27),))
print("(27*z0+19)/16 == z0 : %s" % ((27*z0+19)/16 == z0,))

# (2) the iteration identity 2^k T^k(z) = 3^{a_k} z + rho(word) on many rationals
def Tk(z, k):
    for _ in range(k):
        z = T(z)
    return z

ok, cnt = True, 0
for num in range(-40, 41):
    for den in (1, 3, 5, 7, 11, 13):
        z = F(num, den)
        for k in (1, 2, 3, 4, 5, 8, 12):
            ww = word(z, k); cnt += 1
            if 2**k * Tk(z, k) != 3**sum(ww) * z + rho(ww):
                ok = False
print("iteration identity 2^k T^k(z) = 3^{a_k} z + rho(w) on %d (z,k) pairs: %s"
      % (cnt, "PASS" if ok else "FAIL"))

# (3) the architecture: S_N = {x in Z^+ : first 4N parity bits are (1110)^N}
#     Each S_N is one class mod 2^{4N}; r_N = (-19 * 11^{-1}) mod 2^{4N}.
print("")
print(" N |  M^N=2^{4N} |            r_N = m_N | word(r_N)==(1110)^N | r_N == (-19/11 mod 2^{4N})")
for N in range(1, 9):
    mod = 2**(4*N)
    rN = (-19 * pow(11, -1, mod)) % mod
    good_word = word(F(rN), 4*N) == w*N
    print(" %d | %11d | %20d | %-19s | %s"
          % (N, mod, rN, good_word, rN == (z0.numerator * pow(z0.denominator, -1, mod)) % mod))

# (4) brute force: S_N really is that single class, for N = 1, 2
for N in (1, 2):
    mod = 2**(4*N)
    rN = (-19 * pow(11, -1, mod)) % mod
    hits = [x for x in range(1, 6*mod+1) if word(F(x), 4*N) == w*N]
    print("N=%d brute force x<=%d : %d hits, all == %d mod %d : %s ; min = %d"
          % (N, 6*mod, len(hits), rN, mod, all(x % mod == rN for x in hits), min(hits)))

# (5) m_N is nondecreasing and unbounded; intersection over Z^+ is empty
ms = []
for N in range(1, 41):
    mod = 2**(4*N); ms.append((-19 * pow(11, -1, mod)) % mod)
print("m_1..m_8 = %s" % (ms[:8],))
print("(m_N) nondecreasing: %s ; m_40 = %d ; m_40 > 10^40 : %s"
      % (all(ms[i] <= ms[i+1] for i in range(len(ms)-1)), ms[39], ms[39] > 10**40))
print("sup m_N = infinity  =>  intersection over Z^+ is EMPTY (A.1)")
```

```text
word w = (1, 1, 1, 0)   K = 4   a = 3
rho(w) = 19      2^K - 3^a = -11
realiser z0 = -19/11 ; z0 in Z? False ; z0 > 0? False
word(z0, 16) = (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0)
word(z0,16) == (1110)^4 : True
T^4(z0) == z0 : True
exact 4-cycle: -19/11 -> -23/11 -> -29/11 -> -38/11 -> -19/11
parities along the cycle: [1, 1, 1, 0]
fixed point of x -> (27x+19)/16 : -19/11
(27*z0+19)/16 == z0 : True
iteration identity 2^k T^k(z) = 3^{a_k} z + rho(w) on 3402 (z,k) pairs: PASS

 N |  M^N=2^{4N} |            r_N = m_N | word(r_N)==(1110)^N | r_N == (-19/11 mod 2^{4N})
 1 |          16 |                    7 | True                | True
 2 |         256 |                  231 | True                | True
 3 |        4096 |                  743 | True                | True
 4 |       65536 |                41703 | True                | True
 5 |     1048576 |               762599 | True                | True
 6 |    16777216 |              9151207 | True                | True
 7 |   268435456 |            244032231 | True                | True
 8 |  4294967296 |            780903143 | True                | True
N=1 brute force x<=96 : 6 hits, all == 7 mod 16 : True ; min = 7
N=2 brute force x<=1536 : 6 hits, all == 231 mod 256 : True ; min = 231
m_1..m_8 = [7, 231, 743, 41703, 762599, 9151207, 244032231, 780903143]
(m_N) nondecreasing: True ; m_40 = 1062910281695202122329952605611842196113405485799 ; m_40 > 10^40 : True
sup m_N = infinity  =>  intersection over Z^+ is EMPTY (A.1)
```

**What this test is for.** It confirms every clause of L-9918.4 by exact rational arithmetic:
the realiser, the four-cycle, the parities, the identity $T^4(x) = (27x+19)/16$, the residues
$r_N$ (independently, both as $-19\cdot11^{-1}$ and as the reduction of the rational
$-19/11$), and — the searching part — a **brute-force** confirmation that $S_1$ and $S_2$ are
*exactly* the predicted single classes (not merely contained in them), by scanning six full
periods of the modulus. The word check `word(r_N,4N)==(1110)^N` is run for $N\le8$, i.e. on
integers whose parity word is verified to $32$ places.

### T2 — synthetic and repo-native architectures: nesting, $m_N$, adic chains

```python
#!/usr/bin/env python3
# T2 (L-9918, A.1/A.2): cylinder architectures.  For each architecture we verify
#   - refinement/nesting of the class sets  (hypothesis of D-9918.1)
#   - S_{N+1} subset S_N and (m_N) nondecreasing            (A.1.1)
#   - the trichotomy of A.1: eventually constant <=> seed exists <=> sup m_N < oo
#   - the M-adic intersection is nonempty in EVERY case      (A.2)
# Classes are stored as sets of least nonnegative residues mod M^N.
from fractions import Fraction as F

def least_pos(r, mod):                 # least POSITIVE integer in the class r mod `mod`
    return r if r >= 1 else mod

def report(name, M, C, seed_hint=None):
    L = len(C)
    nest = all(all((r % M**N) in C[N-1] for r in C[N]) for N in range(1, L))
    m = [min(least_pos(r, M**(N+1)) for r in C[N]) for N in range(L)]
    mono = all(m[i] <= m[i+1] for i in range(L-1))
    ev_const = m[-1] == m[len(m)//2]
    # a coherent chain (an element of the M-adic intersection), built greedily by DFS
    chain = adic_chain(M, C)
    print("%-34s M=%d  R_N=%s" % (name, M, [len(c) for c in C][:6]))
    print("    refinement holds: %-5s   m_N nondecreasing: %-5s" % (nest, mono))
    print("    m_1..m_%d = %s" % (min(L, 10), m[:10]))
    print("    m_%d = %d   eventually constant on the computed range: %s" % (L, m[-1], ev_const))
    print("    M-adic chain (A.2) exists: %-5s   first residues: %s" % (chain is not None, chain[:5] if chain else None))
    if seed_hint is not None:
        inside = all((seed_hint % M**(N+1)) in C[N] for N in range(L))
        print("    candidate seed %d lies in every computed S_N: %s" % (seed_hint, inside))
    return m

def adic_chain(M, C):
    """Depth-first search for r_1|r_2|... with r_N in C[N-1]; returns the chain or None.
       Terminates because each level is finite: this IS the finite-intersection /
       Koenig argument of A.2 made constructive."""
    L = len(C)
    def rec(N, r):
        if N == L: return []
        cand = [s for s in C[N] if s % M**N == r]
        for s in sorted(cand):
            tail = rec(N+1, s)
            if tail is not None: return [s] + tail
        return None
    for r in sorted(C[0]):
        t = rec(1, r)
        if t is not None: return [r] + t
    return None

print("=== ARCH 1 (escape, R_N=1): C_N = { -1 mod 2^N } ===")
C1 = [{2**N - 1} for N in range(1, 21)]
report("arch1: x = -1 mod 2^N", 2, C1)
print("    M-adic limit is -1 in Z_2 (not a positive integer); Z^+-intersection empty.")
print("")

print("=== ARCH 2 (escape, R_N=2): C_N = { -1, -3 mod 2^N } ===")
C2 = [set(((-1) % 2**N, (-3) % 2**N)) for N in range(1, 21)]
report("arch2: x = -1 or -3 mod 2^N", 2, C2)
print("    two M-adic limits (-1 and -3); neither is in Z^+; Z^+-intersection empty.")
print("")

print("=== ARCH 3 (genuine seed inside an escaping family): C_N = { -1, 5 mod 2^N } ===")
C3 = [set(((-1) % 2**N, 5 % 2**N)) for N in range(1, 21)]
report("arch3: x = -1 or 5 mod 2^N", 2, C3, seed_hint=5)
print("    M-adic limits {-1, 5}; exactly one is a positive integer: the seed 5.")
print("")

# ---- parity-word architectures for the shortcut map T (D-9902) --------------
def is_odd(z): return z.numerator % 2 == 1
def T(z): return (3*z+1)/2 if is_odd(z) else z/2
def word(z, k):
    w = []
    for _ in range(k):
        w.append(1 if is_odd(z) else 0); z = T(z)
    return tuple(w)

print("=== ARCH 4 (parity cylinders of the word of 7 -- genuine seed) ===")
b = word(F(7), 24)
print("V(7)[0:24] = %s" % (str(b),))
C4, cur = [], 0                        # lift the class one level at a time
for N in range(1, 21):
    cur = next(c for c in (cur, cur + 2**(N-1)) if word(F(c + 2**N), N) == b[:N])
    C4.append({cur})
report("arch4: cylinder of V(7)", 2, C4, seed_hint=7)
print("")

print("=== ARCH 5 (parity cylinders of (1110)^inf -- no seed, cf. T1) ===")
C5 = [{(-19 * pow(11, -1, 2**N)) % 2**N} for N in range(1, 21)]
report("arch5: cylinder of (1110)^inf", 2, C5)
print("    the unique 2-adic limit is -19/11 (T1): not an integer, not positive.")
print("")

# ---- L-9909 uniform-descent survivor architecture --------------------------
print("=== ARCH 6 (L-9909 survivor classes mod 2^k) ===")
def survivor(r, k):
    """r mod 2^k is a k-survivor iff 3^{a_j} >= 2^j for every 1 <= j <= k,
       where a_j counts odd steps in the length-k parity word of the class."""
    n = r + 2**k                      # a positive representative of the class
    a = 0
    for j in range(1, k+1):
        if n % 2 == 1: a += 1; n = (3*n+1)//2
        else:          n = n//2
        if 3**a < 2**j: return False
    return True

KMAX = 16
C6 = [{r for r in range(2**k) if survivor(r, k)} for k in range(1, KMAX+1)]
m6 = report("arch6: L-9909 survivors", 2, C6)
print("    survivor counts k=1..8 : %s   (L-9909.4 table: [1, 1, 2, 3, 4, 8, 13, 19])" % ([len(c) for c in C6[:8]],))
print("    GATE (matches L-9909.4): %s" % ([len(c) for c in C6[:8]] == [1, 1, 2, 3, 4, 8, 13, 19],))
print("    survivors mod 256 : %s" % (sorted(C6[7]),))
print("    counts k=1..%d : %s" % (KMAX, [len(c) for c in C6],))
print("    m_1..m_%d : %s" % (KMAX, m6))
print("    NOTE: whether (m_N) here is eventually constant is NOT decided by any")
print("    computation; the table is finite verification only.")
print("")

# ---- six-branch chart of L-9916 (independent recomputation) ----------------
print("=== ARCH 7 (six-branch chart, P=3^12, Q=2^19) ===")
P, Q = 3**12, 2**19
A = [7 * 3**(2*i) * 2**(15-3*i) for i in range(6)]
print("A = %s   |A| = %d   nu2 = %s" % (A, len(A), [ (x & -x).bit_length()-1 for x in A]))
def c_of(w):
    N = len(w); return sum(P**(N-1-j) * Q**j * w[j] for j in range(N))
def r_of(w):
    N = len(w); mod = Q**N
    return (-pow(P, -N, mod) * c_of(w)) % mod
import itertools
mN = []
for N in range(1, 5):
    rs = [r_of(w) for w in itertools.product(A, repeat=N)]
    mN.append(min(rs))
    print("  N=%d : %d words, %d distinct root classes, m_N = %d"
          % (N, len(rs), len(set(rs)), min(rs)))
print("  m_N nondecreasing: %s" % (all(mN[i] <= mN[i+1] for i in range(len(mN)-1)),))
print("  m_N / Q^{N-1} = %s" % ([round(mN[N-1] / Q**(N-1), 2) for N in range(1, 5)],))
print("  m_N / (Q/6)^N = %s" % ([round(mN[N-1] / (Q/6)**N, 4) for N in range(1, 5)],))
```

```text
=== ARCH 1 (escape, R_N=1): C_N = { -1 mod 2^N } ===
arch1: x = -1 mod 2^N              M=2  R_N=[1, 1, 1, 1, 1, 1]
    refinement holds: True    m_N nondecreasing: True 
    m_1..m_10 = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]
    m_20 = 1048575   eventually constant on the computed range: False
    M-adic chain (A.2) exists: True    first residues: [1, 3, 7, 15, 31]
    M-adic limit is -1 in Z_2 (not a positive integer); Z^+-intersection empty.

=== ARCH 2 (escape, R_N=2): C_N = { -1, -3 mod 2^N } ===
arch2: x = -1 or -3 mod 2^N        M=2  R_N=[1, 2, 2, 2, 2, 2]
    refinement holds: True    m_N nondecreasing: True 
    m_1..m_10 = [1, 1, 5, 13, 29, 61, 125, 253, 509, 1021]
    m_20 = 1048573   eventually constant on the computed range: False
    M-adic chain (A.2) exists: True    first residues: [1, 1, 5, 13, 29]
    two M-adic limits (-1 and -3); neither is in Z^+; Z^+-intersection empty.

=== ARCH 3 (genuine seed inside an escaping family): C_N = { -1, 5 mod 2^N } ===
arch3: x = -1 or 5 mod 2^N         M=2  R_N=[1, 2, 2, 2, 2, 2]
    refinement holds: True    m_N nondecreasing: True 
    m_1..m_10 = [1, 1, 5, 5, 5, 5, 5, 5, 5, 5]
    m_20 = 5   eventually constant on the computed range: True
    M-adic chain (A.2) exists: True    first residues: [1, 1, 5, 5, 5]
    candidate seed 5 lies in every computed S_N: True
    M-adic limits {-1, 5}; exactly one is a positive integer: the seed 5.

=== ARCH 4 (parity cylinders of the word of 7 -- genuine seed) ===
V(7)[0:24] = (1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
arch4: cylinder of V(7)            M=2  R_N=[1, 1, 1, 1, 1, 1]
    refinement holds: True    m_N nondecreasing: True 
    m_1..m_10 = [1, 3, 7, 7, 7, 7, 7, 7, 7, 7]
    m_20 = 7   eventually constant on the computed range: True
    M-adic chain (A.2) exists: True    first residues: [1, 3, 7, 7, 7]
    candidate seed 7 lies in every computed S_N: True

=== ARCH 5 (parity cylinders of (1110)^inf -- no seed, cf. T1) ===
arch5: cylinder of (1110)^inf      M=2  R_N=[1, 1, 1, 1, 1, 1]
    refinement holds: True    m_N nondecreasing: True 
    m_1..m_10 = [1, 3, 7, 7, 7, 39, 103, 231, 231, 743]
    m_20 = 762599   eventually constant on the computed range: False
    M-adic chain (A.2) exists: True    first residues: [1, 3, 7, 7, 7]
    the unique 2-adic limit is -19/11 (T1): not an integer, not positive.

=== ARCH 6 (L-9909 survivor classes mod 2^k) ===
arch6: L-9909 survivors            M=2  R_N=[1, 1, 2, 3, 4, 8]
    refinement holds: True    m_N nondecreasing: True 
    m_1..m_10 = [1, 3, 3, 7, 7, 7, 27, 27, 27, 27]
    m_16 = 27   eventually constant on the computed range: True
    M-adic chain (A.2) exists: True    first residues: [1, 3, 3, 11, 27]
    survivor counts k=1..8 : [1, 1, 2, 3, 4, 8, 13, 19]   (L-9909.4 table: [1, 1, 2, 3, 4, 8, 13, 19])
    GATE (matches L-9909.4): True
    survivors mod 256 : [27, 31, 47, 63, 71, 91, 103, 111, 127, 155, 159, 167, 191, 207, 223, 231, 239, 251, 255]
    counts k=1..16 : [1, 1, 2, 3, 4, 8, 13, 19, 38, 64, 128, 226, 367, 734, 1295, 2114]
    m_1..m_16 : [1, 3, 3, 7, 7, 7, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27]
    NOTE: whether (m_N) here is eventually constant is NOT decided by any
    computation; the table is finite verification only.

=== ARCH 7 (six-branch chart, P=3^12, Q=2^19) ===
A = [229376, 258048, 290304, 326592, 367416, 413343]   |A| = 6   nu2 = [15, 12, 9, 6, 3, 0]
  N=1 : 6 words, 6 distinct root classes, m_N = 6472
  N=2 : 36 words, 36 distinct root classes, m_N = 1908874353
  N=3 : 216 words, 216 distinct root classes, m_N = 44906374791168
  N=4 : 1296 words, 1296 distinct root classes, m_N = 275202518480529950784
  m_N nondecreasing: True
  m_N / Q^{N-1} = [6472.0, 3640.89, 163.37, 1909.6]
  m_N / (Q/6)^N = [0.0741, 0.25, 0.0673, 4.7204]
```

**What this test is for.** Arch 1–3 are *designed* boundary cases: an escaping architecture
with $R_N=1$ (adic limit $-1$), an escaping one with $R_N=2$ (two adic limits, neither an
integer), and one where an escaping branch and a genuine seed coexist — the last shows that
$m_N$ eventually constant does **not** require all branches to stabilise, only the smallest.
Arch 4 and 5 are the two parity cases with the *same* first five residues $1,3,7,7,7$ and
opposite fates, which is exactly why no finite computation can distinguish them: the
architectures agree to depth $5$ and diverge afterwards. Arch 6 recomputes L-9909's survivor
classes from the definition and reproduces its published counts $1,1,2,3,4,8,13,19$ and the
mod-$256$ list as a data gate. Arch 7 recomputes E1's root classes from scratch and
reproduces $m_1,\dots,m_4$. Every architecture is checked for the refinement hypothesis of
D-9918.1 and for monotonicity of $m_N$, and an explicit adic chain (the constructive content
of L-9918.2(3)) is produced by depth-first search in each case.


### T3 — hostile numerical audit of the universal lower bound (L-9918.6)

```python
#!/usr/bin/env python3
# T3 (L-9918, B.1): hostile numerical test of the UNIVERSAL lower bound
#      Sigma(H) := sum_{h=1}^{H} |S(h)|/h  >=  (1/2) log(H/R)
# for every finite multiset of R points on R/Z.  Structured, random,
# low-discrepancy, degenerate, repo-native and locally-optimised point sets;
# also the sharper proved form (1/2)(log(H/R) + 1/H) valid for H >= R.
import math, cmath, random, itertools
random.seed(20260725)

def absS(pts, H):                       # |S(1)|,...,|S(H)|
    out = []
    for h in range(1, H+1):
        s = 0j
        for x in pts: s += cmath.exp(2j*math.pi*h*x)
        out.append(abs(s))
    return out

def sigmas(pts, H):                     # Sigma(1),...,Sigma(H) by prefix sums
    a = absS(pts, H); run = 0.0; out = []
    for h in range(1, H+1):
        run += a[h-1]/h; out.append(run)
    return out, a

def vdc(n, base=2):
    f, r = 1.0, 0.0
    while n: f /= base; r += f*(n % base); n //= base
    return r

GOLD = (math.sqrt(5)-1)/2
cfgs = []
for R in (4, 8, 16, 64, 256):
    cfgs.append(("AP R=%d" % R,            [r/R for r in range(R)]))
    cfgs.append(("AP rotated R=%d" % R,    [(r+0.3137)/R for r in range(R)]))
    cfgs.append(("all-equal R=%d" % R,     [0.2]*R))
    cfgs.append(("two clumps R=%d" % R,    [0.1+1e-6*r for r in range(R//2)] + [0.6+1e-6*r for r in range(R-R//2)]))
    cfgs.append(("Kronecker R=%d" % R,     [(r*GOLD) % 1 for r in range(R)]))
    cfgs.append(("van der Corput R=%d" % R,[vdc(r) for r in range(R)]))
    cfgs.append(("random R=%d" % R,        [random.random() for _ in range(R)]))
    cfgs.append(("AP + jitter R=%d" % R,   [(r/R + random.gauss(0, .3/R)) % 1 for r in range(R)]))
    cfgs.append(("half-AP doubled R=%d" % R, [r/(R//2) for r in range(R//2)]*2))

# repo-native point sets ------------------------------------------------------
P, Q = 3**12, 2**19
A = [7*3**(2*i)*2**(15-3*i) for i in range(6)]
def r_of(w):
    N = len(w); mod = Q**N
    c = sum(P**(N-1-j)*Q**j*w[j] for j in range(N))
    return (-pow(P, -N, mod)*c) % mod
for N in (1, 2, 3):
    cfgs.append(("six-branch root classes N=%d" % N,
                 [r_of(w)/Q**N for w in itertools.product(A, repeat=N)]))
def survivor(r, k):
    n = r + 2**k; a = 0
    for j in range(1, k+1):
        if n % 2 == 1: a += 1; n = (3*n+1)//2
        else:          n = n//2
        if 3**a < 2**j: return False
    return True
for k in (8, 11):
    cfgs.append(("L-9909 survivors mod 2^%d" % k,
                 [r/2**k for r in range(2**k) if survivor(r, k)]))

print("config                              R     H    Sigma(H)   (1/2)ln(H/R)    ratio")
worst = (1e9, None); bad = 0; bad2 = 0; worstrun = 0
for name, pts in cfgs:
    R = len(pts); Hmax = min(64*R, 2048)
    S, a = sigmas(pts, Hmax)
    for H in range(1, Hmax+1):
        lb1 = 0.5*math.log(H/R)
        if H >= R and S[H-1] < 0.5*(math.log(H/R) + 1.0/H) - 1e-9: bad += 1
        if S[H-1] < lb1 - 1e-9: bad2 += 1
        if lb1 > 0 and S[H-1]/lb1 < worst[0]: worst = (S[H-1]/lb1, (name, R, H))
    run = 0
    for h in range(1, min(R, Hmax)+1):
        if a[h-1] < 1e-9: run += 1
        else: break
    worstrun = max(worstrun, run)
    for H in (8*R,):
        if H <= Hmax:
            lb1 = 0.5*math.log(H/R)
            print("%-33s %5d %5d %11.5f %12.5f %8.4f" % (name, R, H, S[H-1], lb1, S[H-1]/lb1))
print("")
print("minimum ratio Sigma/((1/2)ln(H/R)) over ALL structured tests and ALL H<=64R: %.5f  at %s" % worst)
print("violations of the sharper bound (1/2)(ln(H/R)+1/H) for H>=R : %d" % bad)
print("violations of (1/2)ln(H/R) over ALL H>=1 (incl. H<R, RHS<0) : %d" % bad2)
print("longest initial run of h with S(h)=0 over all configs: %d  (proved maximum: R-1)" % worstrun)

# adversarial local search: minimise Sigma(H) directly ------------------------
def search(R, H, iters=3000):
    best = [random.random() for _ in range(R)]
    bs = sigmas(best, H)[0][-1]; step = 0.25
    for it in range(iters):
        i = random.randrange(R)
        cand = list(best); cand[i] = (cand[i] + random.gauss(0, step)) % 1
        cs = sigmas(cand, H)[0][-1]
        if cs < bs: best, bs = cand, cs
        if it % 500 == 499: step *= 0.6
    return bs

print("")
print("adversarial local search (minimise Sigma(H) over point positions, 5 restarts):")
print("   R    H    best Sigma found   (1/2)ln(H/R)   ratio    AP value")
mn = 1e9
for R, H in ((3, 48), (4, 64), (5, 80), (6, 96), (8, 128)):
    bs = min(search(R, H) for _ in range(5))
    lb = 0.5*math.log(H/R); ap = sigmas([r/R for r in range(R)], H)[0][-1]
    mn = min(mn, bs/lb)
    print("  %2d  %4d   %14.6f   %12.5f  %6.4f  %10.6f" % (R, H, bs, lb, bs/lb, ap))
print("minimum ratio found by adversarial search: %.5f   (the bound requires >= 1)" % mn)
print("VERDICT: " + ("NO VIOLATION FOUND." if mn >= 1 and bad == 0 and bad2 == 0 else "VIOLATION FOUND!"))
```

```text
config                              R     H    Sigma(H)   (1/2)ln(H/R)    ratio
AP R=4                                4    32     2.71786      1.03972   2.6140
AP rotated R=4                        4    32     2.71786      1.03972   2.6140
all-equal R=4                         4    32    16.23398      1.03972  15.6138
two clumps R=4                        4    32     6.76146      1.03972   6.5031
Kronecker R=4                         4    32     5.30409      1.03972   5.1015
van der Corput R=4                    4    32     2.71786      1.03972   2.6140
random R=4                            4    32     6.16851      1.03972   5.9329
AP + jitter R=4                       4    32     6.30915      1.03972   6.0681
half-AP doubled R=4                   4    32     6.76146      1.03972   6.5031
AP R=8                                8    64     2.71786      1.03972   2.6140
AP rotated R=8                        8    64     2.71786      1.03972   2.6140
all-equal R=8                         8    64    37.95113      1.03972  36.5013
two clumps R=8                        8    64    16.23398      1.03972  15.6138
Kronecker R=8                         8    64     6.17820      1.03972   5.9422
van der Corput R=8                    8    64     2.71786      1.03972   2.6140
random R=8                            8    64    11.55319      1.03972  11.1118
AP + jitter R=8                       8    64     9.81866      1.03972   9.4436
half-AP doubled R=8                   8    64     6.76146      1.03972   6.5031
AP R=16                              16   128     2.71786      1.03972   2.6140
AP rotated R=16                      16   128     2.71786      1.03972   2.6140
all-equal R=16                       16   128    86.93035      1.03972  83.6093
two clumps R=16                      16   128    37.95112      1.03972  36.5013
Kronecker R=16                       16   128     8.47143      1.03972   8.1478
van der Corput R=16                  16   128     2.71786      1.03972   2.6140
random R=16                          16   128    18.14458      1.03972  17.4514
AP + jitter R=16                     16   128    12.34991      1.03972  11.8781
half-AP doubled R=16                 16   128     6.76146      1.03972   6.5031
AP R=64                              64   512     2.71786      1.03972   2.6140
AP rotated R=64                      64   512     2.71786      1.03972   2.6140
all-equal R=64                       64   512   436.25706      1.03972 419.5906
two clumps R=64                      64   512   195.97195      1.03972 188.4852
Kronecker R=64                       64   512    13.11209      1.03972  12.6112
van der Corput R=64                  64   512     2.71786      1.03972   2.6140
random R=64                          64   512    44.66256      1.03972  42.9563
AP + jitter R=64                     64   512    25.75654      1.03972  24.7726
half-AP doubled R=64                 64   512     6.76146      1.03972   6.5031
AP R=256                            256  2048     2.71786      1.03972   2.6140
AP rotated R=256                    256  2048     2.71786      1.03972   2.6140
all-equal R=256                     256  2048  2099.73217      1.03972 2019.5155
two clumps R=256                    256  2048   954.05493      1.03972 917.6069
Kronecker R=256                     256  2048    17.95355      1.03972  17.2677
van der Corput R=256                256  2048     2.71786      1.03972   2.6140
random R=256                        256  2048   128.95566      1.03972 124.0291
AP + jitter R=256                   256  2048    50.47160      1.03972  48.5434
half-AP doubled R=256               256  2048     6.76146      1.03972   6.5031
six-branch root classes N=1           6    48    11.38861      1.03972  10.9535
six-branch root classes N=2          36   288    25.50470      1.03972  24.5303
six-branch root classes N=3         216  1728    69.69476      1.03972  67.0322
L-9909 survivors mod 2^8             19   152    14.48123      1.03972  13.9280
L-9909 survivors mod 2^11           128  1024    27.85486      1.03972  26.7907

minimum ratio Sigma/((1/2)ln(H/R)) over ALL structured tests and ALL H<=64R: 2.27435  at ('AP R=16', 16, 1023)
violations of the sharper bound (1/2)(ln(H/R)+1/H) for H>=R : 0
violations of (1/2)ln(H/R) over ALL H>=1 (incl. H<R, RHS<0) : 0
longest initial run of h with S(h)=0 over all configs: 255  (proved maximum: R-1)

adversarial local search (minimise Sigma(H) over point positions, 5 restarts):
   R    H    best Sigma found   (1/2)ln(H/R)   ratio    AP value
   3    48         3.391177        1.38629  2.4462    3.380729
   4    64         3.491352        1.38629  2.5185    3.380729
   5    80         3.476006        1.38629  2.5074    3.380729
   6    96         3.681253        1.38629  2.6555    3.380729
   8   128         5.708337        1.38629  4.1177    3.380729
minimum ratio found by adversarial search: 2.44622   (the bound requires >= 1)
VERDICT: NO VIOLATION FOUND.
```

**What this test is for.** This is the adversarial half of the quantifier audit of
L-9918.6. It sweeps $53$ configurations (structured, degenerate, random, low-discrepancy,
and the two repo-native point sets) against **every** $H \le 64R$ — not a handful of values
— and counts violations of both the plain and the sharper form; there are none. It then runs
a direct local-search *minimisation* of $\Sigma(H)$ over point positions with multiple
restarts, i.e. it actively hunts for a counterexample; the best configuration it finds is
never better than the arithmetic progression, and the minimum observed ratio to the bound is
$2.27$–$2.45$, consistent with the proved factor-$2$ slack of L-9918.6(4). The run also
confirms L-9918.6(5) sharply: the longest initial run of vanishing $S(h)$ found is exactly
$R-1 = 255$, attained by the equally spaced set.


### T4 — the generalised Parseval identity and its consequences (L-9918.8)

```python
#!/usr/bin/env python3
# T4 (L-9918, B.4): the generalised Parseval identity for digit sums,
#     (1/M^k) sum_{v mod M^k} |g(v)|^2 = d      (d = #digits, distinct mod M^k)
# and for full root-class sums, (1/M^N) sum_h |S_N(h)|^2 = R_N.
# Also the derived tail bound  #{v : |g(v)|^2 > lam}/M^k >= (d-lam)/(d^2-lam).
import math, cmath, random, itertools
random.seed(20260725)

def gsum(D, mod, v):
    return sum(cmath.exp(2j*math.pi*v*a/mod) for a in D)

def meansq(D, mod):
    return sum(abs(gsum(D, mod, v))**2 for v in range(mod))/mod

print("=== (a) generalised Parseval on random digit sets (exhaustive over v) ===")
print("  M   k    M^k    d     mean |g|^2      d      abs error")
worst = 0.0
for M, k in ((2, 6), (2, 9), (3, 4), (5, 3), (6, 4), (10, 3), (8, 3)):
    mod = M**k
    for d in (2, 3, 5):
        if d > mod: continue
        D = random.sample(range(mod), d)
        ms = meansq(D, mod); worst = max(worst, abs(ms-d))
        print("  %2d  %2d  %6d   %2d   %12.9f   %4d   %.3e" % (M, k, mod, d, ms, d, abs(ms-d)))
print("  max abs error over all random digit sets: %.3e" % worst)

print("")
print("=== (b) the two repo digit sets ===")
# parity architecture: digits {0,1} mod 2
print("  parity digits D={0,1} mod 2 : mean |g|^2 = %.9f  (d = 2)" % meansq([0, 1], 2))
# six-branch alphabet A mod Q = 2^19, exhaustive over all 524288 frequencies
P, Q = 3**12, 2**19
A = [7*3**(2*i)*2**(15-3*i) for i in range(6)]
tot = 0.0; mx = 0.0; cnt = {0.5: 0, 0.25: 0, 0.1: 0}
vals = []
for v in range(Q):
    g = abs(gsum(A, Q, v)); vals.append(g); tot += g*g; mx = max(mx, g if v else 0.0)
print("  six-branch A mod Q=2^19 : mean |g|^2 = %.9f  (d = 6)   |error| = %.3e"
      % (tot/Q, abs(tot/Q - 6)))
print("  max_{v != 0} |g(v)| = %.6f  (trivial ceiling 6; = 6 would force 2^19 | 183967)" % mx)
print("  #{v : |g(v)| <= 1} = %d (%.2f%%)" % (sum(1 for g in vals if g <= 1), 100*sum(1 for g in vals if g <= 1)/Q))

print("")
print("=== (c) derived tail bound  P(|g|^2 > lam) >= (d-lam)/(d^2-lam),  d = 6 ===")
print("   lam    observed P      proved lower bound")
for lam in (0.0, 1.0, 2.0, 3.0, 5.0):
    obs = sum(1 for g in vals if g*g > lam)/Q
    lbd = (6-lam)/(36-lam)
    print("  %5.2f   %10.6f    %10.6f      ok=%s" % (lam, obs, lbd, obs >= lbd - 1e-12))

print("")
print("=== (d) full root-class Parseval  (1/M^N) sum_h |S_N(h)|^2 = R_N ===")
def arch_roots(Pp, M, D, N):
    out = []
    for w in itertools.product(D, repeat=N):
        c = sum(Pp**(N-1-j)*M**j*w[j] for j in range(N))
        out.append((-pow(Pp, -N, M**N)*c) % M**N)
    return out
print("  toy architecture: M = 8, P' = 3, D = {1,3,5}")
for N in (1, 2, 3):
    rs = arch_roots(3, 8, [1, 3, 5], N); mod = 8**N
    tot = 0.0
    for h in range(mod):
        tot += abs(sum(cmath.exp(2j*math.pi*h*r/mod) for r in rs))**2
    print("    N=%d : R_N = %d, distinct roots = %d, mean |S_N|^2 = %.9f, error %.3e"
          % (N, len(rs), len(set(rs)), tot/mod, abs(tot/mod - len(rs))))
print("  six-branch chart N = 1 (exhaustive over h mod 2^19):")
rs = arch_roots(P, Q, A, 1); tot = 0.0
for h in range(Q):
    tot += abs(sum(cmath.exp(2j*math.pi*h*r/Q) for r in rs))**2
print("    R_1 = %d, distinct roots = %d, mean |S_1|^2 = %.9f, error %.3e"
      % (len(rs), len(set(rs)), tot/Q, abs(tot/Q - 6)))
for N in (2, 3):
    rs = arch_roots(P, Q, A, N)
    print("    N=%d : %d words, %d distinct root classes -> Parseval value R_N = %d (by orthogonality)"
          % (N, len(rs), len(set(rs)), len(rs)))

print("")
print("=== (e) mean-square losslessness of the factorisation ===")
print("  product over levels of per-level mean squares = prod d_j ;")
print("  global mean square = R_N = prod d_j : the two agree EXACTLY, so per-level")
print("  second-moment information yields no decay whatsoever.")
for N in (1, 2, 3, 4):
    print("    six-branch N=%d : prod_j d_j = 6^%d = %d = R_N" % (N, N, 6**N))
```

```text
=== (a) generalised Parseval on random digit sets (exhaustive over v) ===
  M   k    M^k    d     mean |g|^2      d      abs error
   2   6      64    2    2.000000000      2   1.554e-15
   2   6      64    3    3.000000000      3   5.329e-15
   2   6      64    5    5.000000000      5   1.776e-15
   2   9     512    2    2.000000000      2   0.000e+00
   2   9     512    3    3.000000000      3   3.553e-15
   2   9     512    5    5.000000000      5   2.132e-14
   3   4      81    2    2.000000000      2   0.000e+00
   3   4      81    3    3.000000000      3   8.882e-16
   3   4      81    5    5.000000000      5   1.155e-14
   5   3     125    2    2.000000000      2   7.994e-15
   5   3     125    3    3.000000000      3   1.155e-14
   5   3     125    5    5.000000000      5   4.441e-15
   6   4    1296    2    2.000000000      2   5.329e-15
   6   4    1296    3    3.000000000      3   6.661e-15
   6   4    1296    5    5.000000000      5   1.510e-14
  10   3    1000    2    2.000000000      2   1.998e-15
  10   3    1000    3    3.000000000      3   1.155e-14
  10   3    1000    5    5.000000000      5   8.882e-15
   8   3     512    2    2.000000000      2   4.441e-16
   8   3     512    3    3.000000000      3   1.332e-15
   8   3     512    5    5.000000000      5   4.441e-15
  max abs error over all random digit sets: 2.132e-14

=== (b) the two repo digit sets ===
  parity digits D={0,1} mod 2 : mean |g|^2 = 2.000000000  (d = 2)
  six-branch A mod Q=2^19 : mean |g|^2 = 6.000000000  (d = 6)   |error| = 1.389e-12
  max_{v != 0} |g(v)| = 5.965277  (trivial ceiling 6; = 6 would force 2^19 | 183967)
  #{v : |g(v)| <= 1} = 74820 (14.27%)

=== (c) derived tail bound  P(|g|^2 > lam) >= (d-lam)/(d^2-lam),  d = 6 ===
   lam    observed P      proved lower bound
   0.00     1.000000      0.166667      ok=True
   1.00     0.857292      0.142857      ok=True
   2.00     0.736771      0.117647      ok=True
   3.00     0.625252      0.090909      ok=True
   5.00     0.451504      0.032258      ok=True

=== (d) full root-class Parseval  (1/M^N) sum_h |S_N(h)|^2 = R_N ===
  toy architecture: M = 8, P' = 3, D = {1,3,5}
    N=1 : R_N = 3, distinct roots = 3, mean |S_N|^2 = 3.000000000, error 8.882e-16
    N=2 : R_N = 9, distinct roots = 9, mean |S_N|^2 = 9.000000000, error 8.882e-15
    N=3 : R_N = 27, distinct roots = 27, mean |S_N|^2 = 27.000000000, error 8.171e-14
  six-branch chart N = 1 (exhaustive over h mod 2^19):
    R_1 = 6, distinct roots = 6, mean |S_1|^2 = 6.000000000, error 7.283e-14
    N=2 : 36 words, 36 distinct root classes -> Parseval value R_N = 36 (by orthogonality)
    N=3 : 216 words, 216 distinct root classes -> Parseval value R_N = 216 (by orthogonality)

=== (e) mean-square losslessness of the factorisation ===
  product over levels of per-level mean squares = prod d_j ;
  global mean square = R_N = prod d_j : the two agree EXACTLY, so per-level
  second-moment information yields no decay whatsoever.
    six-branch N=1 : prod_j d_j = 6^1 = 6 = R_N
    six-branch N=2 : prod_j d_j = 6^2 = 36 = R_N
    six-branch N=3 : prod_j d_j = 6^3 = 216 = R_N
    six-branch N=4 : prod_j d_j = 6^4 = 1296 = R_N
```

**What this test is for.** Part (a) verifies L-9918.8(1) exhaustively over all frequencies
for seven different bases $M$ (prime, prime-power, and *composite* $M = 6, 10$, so the
identity is checked outside the prime-power case where $\mathbb{Z}_M$ is not a domain) and
three digit-set sizes. Part (b) verifies it for the two repo digit sets, the six-branch one
exhaustively over all $524287$ nonzero frequencies; the two side statistics
($\max|g| = 5.965277$, $14.27\%$ of frequencies with $|g|\le1$) are independent
recomputations that agree with the values recorded elsewhere in the repository. Part (c)
checks the derived tail bound (2) at five thresholds. Part (d) checks the full root-class
Parseval (3) exhaustively for a *toy* architecture at $N=1,2,3$ (so the multi-level case is
genuinely tested, not only $N=1$) and for E1 at $N=1$; for $N\ge2$ the exhaustive check is
infeasible and only the hypothesis (distinctness of root classes) is verified, which is what
the proof consumes.


### T5 — the admissible constant region and the unsatisfiability computations (L-9918.7)

```python
#!/usr/bin/env python3
# T5 (L-9918, B.2): the admissible region of Erdos-Turan constant pairs.
# G(u) = C1*phi(uR)/u + (C2/2)*max(0, log u)  must dip below 1 for the emptiness
# criterion to be satisfiable at all.  Closed forms checked against brute force.
import math

def Theta_closed(C1, C2):                 # inf over u>0 of C1/u + (C2/2)(log u)_+
    return C1 if 2*C1 <= C2 else (C2/2)*(1 + math.log(2*C1/C2))

def Theta_num(C1, C2):
    best = 1e18
    u = 1e-4
    while u < 1e9:
        g = C1/u + (C2/2)*max(0.0, math.log(u))
        best = min(best, g); u *= 1.0005
    return best

def Psi(C2):                              # admissibility threshold on C1 when C2 < 2
    return (C2/2)*math.exp(2/C2 - 1)

print("=== (a) closed form for Theta = inf_u [C1/u + (C2/2)(log u)_+] ===")
print("    C1      C2     Theta closed    Theta grid      |diff|     u* = 2C1/C2")
worst = 0.0
for C1 in (0.25, 0.5, 1.0, 2.0, 2.7093, 4.0, 10.0):
    for C2 in (2/math.pi, 1.0, 2.0, 3.0):
        a, b = Theta_closed(C1, C2), Theta_num(C1, C2)
        worst = max(worst, abs(a-b))
        print("  %7.4f %7.4f   %11.6f   %11.6f   %.2e   %10.5f" % (C1, C2, a, b, abs(a-b), 2*C1/C2))
print("  max |closed - grid| = %.2e" % worst)

print("")
print("=== (b) admissibility verdicts (criterion satisfiable for SOME u at all?) ===")
def admissible(C1, C2):
    return (C1 < Psi(C2)) if C2 < 2 else (C1 < 1)
print("   (C1, C2)                       Theta      Theta<1   rule       agree")
cases = [("classical ET      (1, 3)", 1.0, 3.0),
         ("Selberg + 2/pi    (1, 2/pi)", 1.0, 2/math.pi),
         ("L-9916 Fejer pwr  (4, 2/pi)", 4.0, 2/math.pi),
         ("threshold         (e^{pi-1}/pi, 2/pi)", math.exp(math.pi-1)/math.pi, 2/math.pi),
         ("hypothetical      (0.9, 5)", 0.9, 5.0),
         ("hypothetical      (1, 2)", 1.0, 2.0),
         ("hypothetical      (1, 1.9)", 1.0, 1.9),
         ("hypothetical      (2, 0.7)", 2.0, 0.7),
         ("hypothetical      (2, 0.8)", 2.0, 0.8)]
for name, C1, C2 in cases:
    th = Theta_closed(C1, C2)
    print("  %-36s %9.6f   %-7s  %-8s   %s"
          % (name, th, th < 1, admissible(C1, C2), (th < 1) == admissible(C1, C2)))

print("")
print("=== (c) the rule  admissible <=> C1 < Psi(C2) (C2<2) or C1 < 1 (C2>=2) ===")
bad = 0; n = 0
C2 = 0.05
while C2 <= 6.0:
    C1 = 0.05
    while C1 <= 12.0:
        n += 1
        if (Theta_closed(C1, C2) < 1) != admissible(C1, C2): bad += 1
        C1 += 0.05
    C2 += 0.05
print("  grid of %d (C1,C2) pairs: disagreements = %d" % (n, bad))
print("  Psi(C2) at selected C2:  " + "  ".join("Psi(%.4f)=%.5f" % (c, Psi(c))
      for c in (2/math.pi, 1.0, 1.5, 2.0)))
print("  Psi has its MINIMUM 1 at C2 = 2 (Psi'(s) = e^{2/s-1}(1/2 - 1/s)); so C1 < 1")
print("  is always sufficient, and for C2 = 2/pi the threshold is C1 < e^{pi-1}/pi = %.6f"
      % (math.exp(math.pi-1)/math.pi))

print("")
print("=== (d) the admissible u-window for (C1, C2) = (1, 2/pi) ===")
C1, C2 = 1.0, 2/math.pi
def G(u): return C1/u + (C2/2)*max(0.0, math.log(u))
lo, hi = 1.0, 1e6
for _ in range(200):                        # bisect for the upper root of G(u) = 1
    mid = math.sqrt(lo*hi)
    if G(mid) < 1: lo = mid
    else: hi = mid
print("  G(1) = %.6f (so u_- = 1);  u_+ = %.5f ;  argmin u* = pi = %.5f ; min = %.6f"
      % (G(1.0), lo, 2*C1/C2, Theta_closed(C1, C2)))
print("  window width in log scale: log(u_+/u_-) = %.5f  (a factor %.2f in H)"
      % (math.log(lo), lo))
print("  maximal cusp-sum budget at u = u*: (1/C2)(1 - Theta_at_u*) form -> "
      "(pi/2)(1 - 1/pi) = %.6f" % ((math.pi/2)*(1 - 1/math.pi)))

print("")
print("=== (e) Fejer-power constants (C1, C2, phi) = (4, 2/pi, log(4H)) ===")
print("    min over u >= 3/R of  Lambda(u) = (4/u)log(4uR) + (1/pi)(log u)_+")
print("      R           argmin u        min Lambda    > 1 ?")
for R in (1, 2, 6, 36, 216, 1296, 10**4, 10**6):
    best, bu = 1e18, None
    u = max(3.0/R, 1e-3)
    while u < 1e7:
        lam = (4.0/u)*math.log(4*u*R) + (1/math.pi)*max(0.0, math.log(u))
        if lam < best: best, bu = lam, u
        u *= 1.0002
    print("  %7d   %14.4f   %14.6f     %s" % (R, bu, best, best > 1))
print("  => unsatisfiable for every R >= 1 (proof in the file covers all real u > 0).")
print("")
print("=== (f) even WITHOUT the log: (C1, C2) = (4, 2/pi) with phi = 1 ===")
print("  Theta(4, 2/pi) = (1/pi)(1 + log(4*pi)) = %.6f > 1  ->  still unsatisfiable."
      % Theta_closed(4.0, 2/math.pi))
print("  So removing the log(4H) alone does NOT revive the criterion: C1 must also")
print("  come below e^{pi-1}/pi = %.6f." % (math.exp(math.pi-1)/math.pi))
```

```text
=== (a) closed form for Theta = inf_u [C1/u + (C2/2)(log u)_+] ===
    C1      C2     Theta closed    Theta grid      |diff|     u* = 2C1/C2
   0.2500  0.6366      0.250000      0.250024   2.44e-05      0.78540
   0.2500  1.0000      0.250000      0.250036   3.57e-05      0.50000
   0.2500  2.0000      0.250000      0.250036   3.57e-05      0.25000
   0.2500  3.0000      0.250000      0.250036   3.57e-05      0.16667
   0.5000  0.6366      0.462053      0.462053   4.16e-09      1.57080
   0.5000  1.0000      0.500000      0.500000   3.19e-08      1.00000
   0.5000  2.0000      0.500000      0.500071   7.14e-05      0.50000
   0.5000  3.0000      0.500000      0.500071   7.14e-05      0.33333
   1.0000  0.6366      0.682689      0.682689   4.01e-09      3.14159
   1.0000  1.0000      0.846574      0.846574   3.38e-10      2.00000
   1.0000  2.0000      1.000000      1.000000   6.38e-08      1.00000
   1.0000  3.0000      1.000000      1.000143   1.43e-04      0.66667
   2.0000  0.6366      0.903324      0.903324   6.84e-11      6.28319
   2.0000  1.0000      1.193147      1.193147   1.17e-08      4.00000
   2.0000  2.0000      1.693147      1.693147   6.76e-10      2.00000
   2.0000  3.0000      1.931523      1.931523   7.99e-09      1.33333
   2.7093  0.6366      0.999945      0.999945   1.54e-09      8.51152
   2.7093  1.0000      1.344919      1.344919   2.37e-09      5.41860
   2.7093  2.0000      1.996690      1.996690   3.38e-09      2.70930
   2.7093  3.0000      2.386838      2.386838   1.86e-10      1.80620
   4.0000  0.6366      1.123960      1.123960   6.38e-09     12.56637
   4.0000  1.0000      1.539721      1.539721   2.71e-09      8.00000
   4.0000  2.0000      2.386294      2.386294   2.34e-08      4.00000
   4.0000  3.0000      2.971244      2.971244   3.54e-08      2.66667
  10.0000  0.6366      1.415624      1.415624   5.18e-09     31.41593
  10.0000  1.0000      1.997866      1.997866   3.84e-09     20.00000
  10.0000  2.0000      3.302585      3.302585   1.93e-08     10.00000
  10.0000  3.0000      4.345680      4.345680   4.21e-08      6.66667
  max |closed - grid| = 1.43e-04

=== (b) admissibility verdicts (criterion satisfiable for SOME u at all?) ===
   (C1, C2)                       Theta      Theta<1   rule       agree
  classical ET      (1, 3)              1.000000   False    False      True
  Selberg + 2/pi    (1, 2/pi)           0.682689   True     True       True
  L-9916 Fejer pwr  (4, 2/pi)           1.123960   False    False      True
  threshold         (e^{pi-1}/pi, 2/pi)  1.000000   False    False      True
  hypothetical      (0.9, 5)            0.900000   True     True       True
  hypothetical      (1, 2)              1.000000   False    False      True
  hypothetical      (1, 1.9)            0.998729   True     True       True
  hypothetical      (2, 0.7)            0.960039   True     True       True
  hypothetical      (2, 0.8)            1.043775   False    False      True

=== (c) the rule  admissible <=> C1 < Psi(C2) (C2<2) or C1 < 1 (C2>=2) ===
  grid of 28680 (C1,C2) pairs: disagreements = 0
  Psi(C2) at selected C2:  Psi(0.6366)=2.70977  Psi(1.0000)=1.35914  Psi(1.5000)=1.04671  Psi(2.0000)=1.00000
  Psi has its MINIMUM 1 at C2 = 2 (Psi'(s) = e^{2/s-1}(1/2 - 1/s)); so C1 < 1
  is always sufficient, and for C2 = 2/pi the threshold is C1 < e^{pi-1}/pi = 2.709767

=== (d) the admissible u-window for (C1, C2) = (1, 2/pi) ===
  G(1) = 1.000000 (so u_- = 1);  u_+ = 19.73524 ;  argmin u* = pi = 3.14159 ; min = 0.682689
  window width in log scale: log(u_+/u_-) = 2.98241  (a factor 19.74 in H)
  maximal cusp-sum budget at u = u*: (1/C2)(1 - Theta_at_u*) form -> (pi/2)(1 - 1/pi) = 1.070796

=== (e) Fejer-power constants (C1, C2, phi) = (4, 2/pi, log(4H)) ===
    min over u >= 3/R of  Lambda(u) = (4/u)log(4uR) + (1/pi)(log u)_+
      R           argmin u        min Lambda    > 1 ?
        1          55.2750         1.667835     True
        2          66.2666         1.713552     True
        6          82.8757         1.772676     True
       36         108.8288         1.847840     True
      216         133.9433         1.907073     True
     1296         158.5803         1.956179     True
    10000         186.2763         2.003673     True
  1000000         247.7457         2.089095     True
  => unsatisfiable for every R >= 1 (proof in the file covers all real u > 0).

=== (f) even WITHOUT the log: (C1, C2) = (4, 2/pi) with phi = 1 ===
  Theta(4, 2/pi) = (1/pi)(1 + log(4*pi)) = 1.123960 > 1  ->  still unsatisfiable.
  So removing the log(4H) alone does NOT revive the criterion: C1 must also
  come below e^{pi-1}/pi = 2.709767.
```

### T6 — self-check harness: every embedded block reproduces its recorded output

A sibling file was recently found to contain placeholder text where captured output should
have been, and the packet now audits for this. The harness below re-extracts every script
embedded in *this* file, re-runs it in a fresh interpreter, and diffs its stdout against the
recorded output block; it also scans the recorded outputs for placeholder tokens. It skips
its own block (sentinel). Its recorded output is stable under later edits to prose, because
it reports only the extracted pairs, their SHA-256 digests and the comparison results.

```python
#!/usr/bin/env python3
# T6 SELFCHECK_HARNESS (L-9918): re-extract every embedded script from the claim
# file, re-run it, and diff its stdout against the recorded output block that
# immediately follows it.  This exists because a sibling file was found to
# contain placeholder text where captured output should have been; the packet
# now audits for that, so the audit is run here and its result recorded.
# The harness skips its own block (it contains the sentinel above).
import re, subprocess, sys, os, tempfile, hashlib

PATH = "/home/user/collatz/research/foundations/L-9918-extraction-barriers.md"
text = open(PATH).read()

blocks = re.findall(r"```(python|text)\n(.*?)```", text, flags=re.S)
pairs, i = [], 0
while i < len(blocks):
    kind, body = blocks[i]
    if kind == "python" and body.startswith("#!/usr/bin/env python3") \
       and "SELFCHECK_" + "HARNESS" not in body:
        assert i + 1 < len(blocks) and blocks[i+1][0] == "text", "script with no output block"
        pairs.append((body, blocks[i+1][1]))
        i += 2
    else:
        i += 1

print("claim file : %s" % PATH)
print("runnable (script, output) pairs extracted: %d" % len(pairs))
print("")
allok = True
for n, (src, expected) in enumerate(pairs, 1):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(src); tmp = f.name
    r = subprocess.run([sys.executable, tmp], capture_output=True, text=True)
    os.unlink(tmp)
    got = r.stdout.rstrip("\n"); exp = expected.rstrip("\n")
    ok = (got == exp) and r.returncode == 0
    allok &= ok
    # locate the first differing line, if any
    gl, el = got.split("\n"), exp.split("\n")
    where = "-"
    if not ok:
        for j in range(max(len(gl), len(el))):
            a = gl[j] if j < len(gl) else "<missing>"
            b = el[j] if j < len(el) else "<missing>"
            if a != b:
                where = "line %d: got %r vs recorded %r" % (j+1, a[:60], b[:60]); break
    print("script %d : sha256 %s | %4d src lines | %3d output lines | exit %d -> %s   %s"
          % (n, hashlib.sha256(src.encode()).hexdigest()[:16], src.count("\n"),
             len(el), r.returncode, "MATCH" if ok else "MISMATCH", where))
    # placeholder / stub audit on the recorded output
    for bad in ("TODO", "FIXME", "placeholder", "PLACEHOLDER", "...output...", "<output>", "XXX"):
        if bad in exp:
            print("   !! placeholder token %r found in recorded output" % bad); allok = False
print("")
print("VERDICT: %s" % ("ALL EMBEDDED BLOCKS REPRODUCE THEIR RECORDED OUTPUT EXACTLY."
                       if allok else "AT LEAST ONE BLOCK FAILED TO REPRODUCE."))
```

```text
claim file : /home/user/collatz/research/foundations/L-9918-extraction-barriers.md
runnable (script, output) pairs extracted: 5

script 1 : sha256 3095bcd66235c72e |   84 src lines |  26 output lines | exit 0 -> MATCH   -
script 2 : sha256 3adc173888f8c488 |  135 src lines |  65 output lines | exit 0 -> MATCH   -
script 3 : sha256 906757f37ecfbf92 |  110 src lines |  66 output lines | exit 0 -> MATCH   -
script 4 : sha256 4e667e39566ee248 |   84 src lines |  57 output lines | exit 0 -> MATCH   -
script 5 : sha256 1a52934b11ac00a2 |  102 src lines |  72 output lines | exit 0 -> MATCH   -

VERDICT: ALL EMBEDDED BLOCKS REPRODUCE THEIR RECORDED OUTPUT EXACTLY.
```

**Self-check result (recorded).** All five embedded scripts reproduce their recorded output
byte-for-byte, exit status $0$, and no placeholder token occurs in any recorded output.
Re-running the harness after it was itself embedded produced identical output (checked).

### Alternate formulations tried, and what they would change

* **Proving L-9918.2(3) by Tychonoff instead of König.** Equivalent; the König form is used
  because it needs no compactness theorem and makes the constructive content visible (T2
  builds the chain by depth-first search). Recorded in the Remark after the proof.
* **Stating L-9918.6 with the hypothesis $H \ge R$ (as in its specialised ancestor).** Tried,
  then dropped: the inequality is true for all $H \ge 1$ because the right side is negative
  when $H < R$. Keeping $H \ge R$ would have forced a case split in the proof of
  L-9918.7(c) for $u<1$; without it, ($\dagger$) is a single formula with $(\log u)_+$.
* **Bounding $\Sigma$ by dyadic-block Cauchy–Schwarz instead of Abel summation.** Gives
  $\ge \frac{1}{4}\log_2(H/R) = 0.36\log(H/R)$, strictly worse than $\tfrac12$; recorded
  because it shows the Abel route is not merely convenient.
* **Allowing the criterion to use several cut-offs $H_1<\dots<H_k$ simultaneously.** Not
  covered by L-9918.7 and deliberately excluded from its scope (limitation L2). A
  multi-scale version of the collision would need a lower bound for
  $\min_i [\,C_1R\varphi(H_i)/H_i + C_2\Sigma(H_i)\,]$ jointly, which L-9918.6 does supply
  pointwise but which does not obviously combine; this is left open.
* **Defining supercriticality by $A_w \ge M^{|w|}$ rather than $>$.** Equivalent: L-9918.5(2)
  proves $A_w = M^{|w|}$ is impossible when $\gcd(A_w,M)=1$ and $M\ge2$.
* **Encoding a $\Sigma^0_2$-complete problem in L-9918.9 rather than the halting problem.**
  Attempted; a branching construction ($R_N>1$, one branch per witness) appears to work but
  the refinement bookkeeping for branches that appear at different levels was not completed,
  so only $\Sigma^0_1$-hardness is claimed. The $\Sigma^0_2$ upper bound is stated and is
  immediate.

---

## Remaining uncertainty

1. **The constant $\tfrac12$ in L-9918.6 is not proved optimal.** The arithmetic progression
   attains $\log(H/R)+O(1)$, and no configuration beating it was found in T3, so I believe
   the optimal universal constant is $1$; I have not proved it. This matters only in the
   favourable direction. Precisely: if L-9918.6(3) holds with $c\log(H/R)$ in place of
   $\tfrac12\log(H/R)$, then the whole of L-9918.7(d) goes through with $C_2/2$ replaced by
   $cC_2$, giving $u^* = C_1/(cC_2)$, $\Theta = cC_2\big(1+\log\frac{C_1}{cC_2}\big)$ and the
   admissibility threshold
   $$\Psi_c(s) \;=\; c\,s\,e^{\,1/(cs)-1}, \qquad \Psi_{1/2} = \Psi \ \text{(the function used
   above)}, \qquad \Psi_1(s) = \Psi_{1/2}(2s),$$
   and $\Psi_1(s) < \Psi_{1/2}(s)$ exactly when $s < 1/\log 2 = 1.44270$ (their ratio is
   $2e^{-1/s}$) — in particular at $s = C_2 = 2/\pi$. With the conjectural optimal $c = 1$ and
   $C_2 = 2/\pi$ the threshold on $C_1$ would fall from $e^{\pi-1}/\pi = 2.70977$ to
   $\tfrac{2}{\pi}e^{\pi/2-1} = 1.12661$, i.e. the admissible region shrinks and the barrier
   strengthens. Nothing in the file assumes optimality.
2. **Scope of L-9918.7, restated.** It rules out (ET)-shape criteria with a single cut-off
   and absolute values. I have *not* attempted a barrier covering: phase-preserving
   estimates; multi-scale or second-moment/large-sieve arguments; majorising the union of
   $R_N$ classes directly instead of counting $R_N$ points against one arc; or lattice
   reduction. I do not claim one, and I regard the phase-preserving loophole (L1) as the most
   likely place where the barrier is genuinely evadable.
3. **The affine axioms (AF1)–(AF4) of D-9918.3.** These are exactly what the two exhibited
   affine architectures satisfy, and each is verified for them in L-9918.5(5); but they are
   *axioms I chose*, and a reviewer should check that they are not tailored so tightly that
   L-9918.5 is a restatement of its two instances. My confidence that they are the right
   general hypotheses is moderate-to-high (the only substantive one is $\gcd(A_w,M)=1$, which
   is exactly what makes $M^p - A_w$ a unit — the mechanism the whole sign criterion runs on);
   my confidence in the *proof* given the axioms is high.
4. **L-9918.9's reading.** The reduction is elementary and I am confident in it, but the
   *interpretation* — "therefore architecture-specific arithmetic is necessary" — is an
   informal gloss on a formal statement about arbitrary computable presentations. The formal
   statement is what is claimed; the gloss is labelled as a reading, not a theorem.
5. **Nothing here indicates a direction for any extraction question.** In particular the E3
   table ($m_N = 27$ for $7 \le N \le 16$) is *not* evidence for a seed, and the E1 figures
   are *not* evidence for escape. I record explicitly that I formed no opinion.
6. **Most likely location of an error.** In order: (a) the region computation of
   L-9918.7(d), where the case analysis $2C_1 \lessgtr C_2$ and the behaviour of $\Psi$ at
   $s = 2$ interlock (machine-checked on a $28680$-point grid in T5, but a case-split of this
   kind is where an inequality flips); (b) the constant chase in L-9918.7(f) (two explicit
   numerical thresholds, $a = 4\log 12 = 9.9396266$ and $u_0 = a\pi = 31.226258$); (c) the Abel summation in
   L-9918.6 Step 2, where an off-by-one changes the additive constant.

---

## Suggested next attack

1. **(Refutation attempt on this file — do this first.)** Re-derive L-9918.7(d) by hand for
   the three pairs $(1,2/\pi)$, $(4,2/\pi)$, $(1,3)$ and check them against $\Theta$; then
   re-derive L-9918.6 Step 2 independently, since a change in its additive constant would
   move $\Psi$. Independently re-prove L-9918.4(3) for $N = 2$ by hand: that single case
   already exercises the whole induction.
2. **(Highest value, negative direction.)** Attempt the phase-preserving barrier (limitation
   L1): is there a lower bound for $\big|\sum_{|h|\le D}\widehat\Psi(h)S(h)\big|$ over all
   non-negative majorants $\Psi \ge \mathbf 1_I$ of degree $\le D$, i.e. a Selberg-problem
   dual lower bound, for a union of $R$ residue classes against an interval of length
   $\ll M^N/R$? That would upgrade L-9918.7 from a statement about one inequality shape to a
   statement about Fourier-analytic emptiness certificates in general.
3. **(Positive direction.)** Attack Q-9918a for E1: the digits form a geometric ladder with
   six distinct $2$-adic valuations, so the natural object is the base-$Q$ expansion of
   $r_w = -P^{-N}c_w$, whose places are governed by $\nu_2$ of the partial sums. A forced
   nonzero place would give $m_N \ge Q^{N-1}$ outright, with no discrepancy input at all.
4. **(Cheap and useful.)** Extend T2's E3 computation past $k = 16$ and record where (if
   anywhere) $m_N$ first exceeds $27$. By L-9918.1 this is exactly the frontier of the
   question "is there $n$ with $\sigma(n)=\infty$" at that depth, and by L-9918.1(4) it is a
   *pointwise* question about the finitely many integers $\le 27$ — a much cheaper
   computation than a survivor enumeration.
5. **(Structural, for the whole packet.)** Every architecture in the repository should be
   recorded in the D-9918.1 format (base $M$, sets $C_N$, $R_N$, affine data if any,
   sub/supercritical). That single table would make it immediate which barriers apply where,
   and would surface any architecture that is *subcritical* — where L-9918.5 permits periodic
   seeds and the Diophantine condition $(M^p - A_w)\mid \kappa_w$ becomes the whole question.

---

Signed: **fable-02-p12**, 2026-07-25.

---

## Verification note (fable-02-v20, 2026-07-25)

**Verdict: PASS.** Every claim of L-9918 (D-9918.1–.3, L-9918.1–.9, the four exhibited
architectures, the Dependency/Gap audits) was checked independently, and I found no
substantive error. Six defects were found and fixed in place; all six are editorial or
presentational, none touches a proof of a stated result, and each is listed in §9 below
with the exact edit. Status upgraded PROPOSED → PROVED. I did **not** set
INDEPENDENTLY_VERIFIED.

**Method.** I read README §7/§13 and NOTATION.md, then the file, then re-derived every
load-bearing step on paper before running anything. All computation below is mine
(scripts V-A…V-D, written from the *statements* only; the author's `t1…t6` scripts were
not read for logic, only re-run for reproduction). L-9904, L-9909, L-9916 are cited by the
file as context only; I confirmed nothing is imported from them, so their status does not
propagate here. No result of this file is used by any of its dependencies and none of them
cites it (checked by grep across the repo): no circularity.

### 1. L-9918.9 (undecidability) — the deepest check, reported in full

This is the file's most consequential and least expected claim, so I state exactly how far
I went. **I reconstructed the reduction completely and independently, and then drove it
with a real single-tape Turing-machine simulator** (V-D §(i)) rather than with an assumed
halting time. Specifically:

1. **The architecture.** $c_N := (2^{\min(N,t(e))}-1) \bmod 2^N$, $C_N := \{c_N\}$,
   $M = 2$, $R_N = 1$. Re-derived, not copied.
2. **Computably presented (the file's own definition: $(N,c)\mapsto[c\in C_N]$
   computable).** Deciding $c \in C_N$ means computing $c_N$ and comparing. Computing $c_N$
   simulates $e$ for **exactly $N$ steps** — a bounded, always-terminating computation —
   and outputs $2^t-1$ if it halted at some $t \le N$, else $2^N-1$. So the presentation is
   **total** computable, uniformly in $(e,N)$. **Confirmed.** (Timed on a non-halting
   machine to level 300: no divergence.)
3. **Refinement at every level.** By hand, both cases. If $N < t(e)$: $c_N = 2^N-1$,
   $c_{N+1} = 2^{N+1}-1 = 2^N + (2^N-1) \equiv 2^N - 1 \pmod{2^N}$. If $N \ge t(e)$:
   $\min(N,t) = \min(N+1,t) = t$ and $2^t-1 < 2^N$, so $c_{N+1} = c_N = 2^t-1$ *as
   integers*. **Confirmed**, and re-checked mechanically at every level $N < 40$ for seven
   machines (halting times $1,2,3,5,8,13$ and a non-halting one).
4. **$R_N = 1$, and D-9918.1(1) at $N = 0$.** $C_N$ is a singleton by construction;
   $c_0 = 0$ and $\mathbb{Z}/1 = \{0\}$, so $C_0 = \mathbb{Z}/1$, $R_0 = 1$ as D-9918.1
   requires. **Confirmed.**
5. **Halting $\Rightarrow$ seed.** $x := 2^{t}-1$. For $N \ge t$: $x < 2^N$ so
   $x \bmod 2^N = 2^t-1 = c_N$. For $N < t$: $x - (2^N-1) = 2^N(2^{t-N}-1)$. **Confirmed**
   by hand and mechanically (membership checked to level $200$, well past the level where
   the class freezes).
6. **Non-halting $\Rightarrow$ no seed.** $c_N = 2^N-1$ for all $N$, so $m_N = 2^N-1 \to
   \infty$ and L-9918.1(3) gives $\bigcap_N S_N = \emptyset$; independently,
   $x \equiv -1 \pmod{2^N}$ for all $N$ forces $x+1 = 0$ by Lemma A.0(iv). **Confirmed.**
7. **Many-one and total.** The map $e \mapsto$ (an index for the presentation) is total
   computable by s-m-n, the equivalence is an **iff**, and every output is a *valid*
   architecture. Hence $\mathrm{HALT} \le_m \mathrm{EXTRACTION}$: a **decision** procedure
   for extraction would decide halting — this is not a semi-decision artefact.
   **Confirmed.** (Formally EXTRACTION is a promise problem — not every program presents an
   architecture — but the reduction always lands inside the promise, so undecidability
   holds for the promise problem and for every total extension of it.)
8. **The complexity remarks.** With membership decidable, $\exists x\,\forall N\,(x\in S_N)$
   is $\Sigma^0_2$ and, for fixed $x$, $\exists N\,(x\notin S_N)$ is $\Sigma^0_1$.
   **Confirmed.** Only $\Sigma^0_1$-hardness is claimed, consistent with the file's own note
   that the $\Sigma^0_2$-hardness attempt was left incomplete.

**One boundary case, recorded (not a defect, but read it).** If one works in a TM model in
which a machine may halt *before executing any step*, i.e. $t(e) = 0$, the construction as
written gives $c_N = 0$ for all $N$, hence $m_N = 2^N \to \infty$ and **no seed although
the machine halts** (V-D verifies this). The file forecloses this by *stipulating*
$t(e) \in \mathbb{Z}^+\cup\{\infty\}$, so the proof as written is correct; and the claim is
in any case untouched, since halting-in-$\ge 1$-step is still undecidable (pad any machine
with one dummy step). The one-line repair $c_N := (2^{\min(N,t)+1}-1)\bmod 2^N$ was tested
and works for $t = 0$ as well. I left the text unchanged and record the caveat here.

**Reading vs theorem.** The gloss "no method using only the architecture's
counting/refinement data can decide extraction" follows *a fortiori* from the theorem
(which allows a decider full membership data), and the file labels it a reading. The
theorem says nothing about any individual architecture — each is a fixed true-or-false
statement, trivially "decidable" by a constant algorithm. The file states this explicitly.
**Assessment: the reduction is correct, elementary, and genuinely establishes what is
claimed, at $M = 2$ with $R_N = 1$.**

### 2. L-9918.7(d) — the admissible region, re-derived from scratch

Re-derived by hand: $G$ is continuous, strictly decreasing on $(0,1]$ with $G(1) = C_1$;
on $[1,\infty)$, $G'(u) = (C_2u/2 - C_1)/u^2$ vanishes only at $u^* = 2C_1/C_2$, so
$\Theta = C_1$ when $2C_1 \le C_2$ and $\Theta = \frac{C_2}{2}(1+\log\frac{2C_1}{C_2})$
otherwise; the infimum is **attained**, so "$\exists u: G(u)<1$" $\iff \Theta<1$. In the
second branch $\Theta<1 \iff C_1 < \Psi(C_2)$. $\Psi'(s) = e^{2/s-1}(\frac12-\frac1s)$, so
$\Psi$ falls on $(0,2)$, rises on $(2,\infty)$, $\Psi(2)=1$, hence $\Psi \ge 1$ with
equality only at $s=2$; and $\Psi(s)>s/2 \iff s<2$. The two cases then close exactly as the
file has them — **including the delicate $C_2 \ge 2$ case**, where $2C_1>C_2$ forces
$C_1 > C_2/2 \ge \Psi(C_2)$ and hence $\Theta \ge 1$. **No sign flips.** The boxed
criterion is correct as stated, and is consistent at the seam $C_2 = 2$ (both branches read
$C_1<1$ there).

Numerically (V-B, independent of the closed form): the closed $\Theta$ matches a
grid+golden-section infimum to $5.3\times10^{-15}$ over 4900 pairs; over a **44 800-pair**
grid ($C_1\le14$, $C_2\le8$, step $0.05$) the three predicates {$\Theta<1$}, {boxed rule},
{direct scan over $u$} agree in every case; and 15 904 checks at
$C_1 = \mathrm{threshold}(C_2)\cdot(1\pm\varepsilon)$, $\varepsilon = 10^{-5},10^{-8}$,
over 3976 values of $C_2$ show **no** mismatch — the case split does not flip anywhere near
the boundary. At the threshold exactly, $\Theta = 1$ (not $<1$), i.e. the region is open, as
claimed. $\Psi(2/\pi) = e^{\pi-1}/\pi = 2.709767310$, $\Psi(1)=e/2$, $\Psi(2)=1$: all exact.
Window and budget for $(1,2/\pi)$: $u_-=1$, $u_+ = 19.735236$, $u^*=\pi$,
$\Theta = 0.682688726$, budget $1.070796327$ — reproducing L-9916's numbers to all printed
digits.

### 3. L-9918.7(f) — the two explicit thresholds (the author's mid-draft correction)

The **corrected** values are right: $a = 4\log 12 = 9.9396265992$, $a/3 = 3.3132088664$,
$u_0 = a\pi = 31.2262579033 > 3$, and
$\psi(u_0) = (1+\log(a\pi))/\pi = 1.4136967551 > 1.413696$. The case split ($u\le3$ via
$\Lambda \ge a/u \ge a/3$; $u>3$ via $\log(4H)\ge\log 12$ and the first-derivative test) is
valid, and both standing facts ($H\ge3$, $H = uR \ge u$) are used correctly. An independent
2-D minimisation of the true $\Lambda$ over real $R\ge1$, $H\ge3$ gives $1.667835$ at
$R=1$, and $1.713552,\ 1.772676,\ 1.847840,\ 1.956179,\ 2.089095$ at
$R = 2, 6, 36, 1296, 10^6$ — matching T5 exactly and lying above the proved threshold, as
they must. **The stale value $1.5388$ still present in two Gap-audit bullets is *not* what
§(f) proves** (it is true — the true minimum is $1.6678$ — but it belongs to an abandoned
sharper route through $4\log(4u)/u$); both bullets and the stale companion threshold
"$\log 39.7582$" have been corrected (§9, fixes 1–3).

### 4. L-9918.6 — the universal lower bound

Step 1 re-derived: $\sum_{|k|\le h}(1-\frac{|k|}{h+1})|S(k)|^2 = \sum_{r,r'}K_h(\theta_r-
\theta_{r'}) \ge R(h+1)$ by (F1)/(F2); isolating $k=0$ and bounding the remaining weights by
$1$ gives $\sum_{k\le h}|S(k)|^2 \ge R(h+1-R)/2$; then $|S|^2 \le R|S|$ gives
$T(h)\ge(h+1-R)/2$. Both the Abel identity and the telescoping identity were checked in
**exact rational arithmetic** (V-C §§1–2: 300 random instances; all $1\le R\le29$,
$R\le H<60$), including the empty-sum boundary $H=R$ where the telescoped form reads
$\log 1 - 1 + 1 = 0$. Feeding the *extremal* profile $T(h)=\max(0,(h+1-R)/2)$ through the
assembled Abel bound reproduces $\frac12(\log\frac HR + \frac1H)$ with zero slack beyond the
single remaining inequality $\sum_{h=R}^{H-1}1/h \ge \log(H/R)$ (2136 cases, no failure).
**There is no off-by-one.**

**Both of the author's quantifier claims are confirmed, and I sharpen the second.** Form (3)
holds for all $H\ge1$ (for $H<R$ the right side is negative), so $H\ge R$ is indeed
unnecessary there. But $H \ge R$ is **necessary** for the sharper form (2), and I exhibit the
counterexample the file does not: for $\theta = \{0,\tfrac12\}$ ($R=2$, $H=1$), $S(1)=0$ so
$\Sigma(1) = 0 < \frac12(\log\frac12+1) = 0.153426$. The file's split between (2) and (3) is
therefore exactly right, not merely conservative.

**Counterexample hunt (mine, independent of T3).** 81 structured/degenerate/random/
low-discrepancy families against **every** $h \le H$: zero violations of (1), (2), (3).
Simulated annealing plus greedy polish, minimising $\Sigma(H)$ directly over point
positions with 5 restarts, never beat the arithmetic progression; smallest ratio to the
bound seen anywhere was $2.266$ (structured) and $2.439$ (search) — matching the author's
$2.274$/$2.446$ and consistent with the proved factor-$2$ slack. **No counterexample
exists in the searched space; the bound looks safe with room to spare.**

### 5. L-9918.4 — the $(1110)^\infty$ architecture, by hand at $N=2$

Congruence chain re-derived line by line ($x=2y+1 \to 3y+2$; $x=4z+3 \to 9z+8$;
$x=8t+7 \to 27t+26$; $v_3=0 \iff t$ even $\iff x\equiv 7 \bmod 16$), giving
$T^4(x) = (27x+19)/16$, and the key identity
$11T^4(x)+19 = \frac{297x+513}{16} = \frac{27(11x+19)}{16}$. At $N=2$ by hand:
$m_2 = (-19)\cdot11^{-1} \bmod 256 = 231$ and $11\cdot231+19 = 2560 = 256\cdot 10$; the
$T$-orbit $231 \to 347 \to 521 \to 782 \to 391 \to 587 \to 881 \to 1322 \to 661$ has
parities $(1,1,1,0,1,1,1,0)$. Exactly as claimed. The realiser: $11x+19=0 \iff x=-19/11$,
with the exact $4$-cycle $-\frac{19}{11}\to-\frac{23}{11}\to-\frac{29}{11}\to-\frac{38}{11}
\to-\frac{19}{11}$ (parities $1,1,1,0$), $\notin\mathbb{Z}$, $<0$. All re-verified in exact
rationals over $\mathbb{Z}$ *and* over $\mathbb{Z}_{(2)}$ (V-C §6).

### 6. D-9918.3 — are (AF1)–(AF4) too tight? (the author's least certain point)

**No.** They are satisfied by a large natural family, not just by E1/E2: every *$M$-adic
affine branch system* — pick any $M\ge2$ and any branch data $A_b \ge 1$ with
$\gcd(A_b,M)=1$ and integers $\kappa_b \ge 0$ with $M \mid A_b b + \kappa_b$, and set
$\Phi(x) = (A_bx+\kappa_b)/M$ on $x \equiv b \pmod M$. To make this concrete I built a
**third** architecture, $M = 3$ with $(A_0,A_1,A_2) = (1,5,7)$, verified (AF1) (each word is
exactly one class mod $3^p$, $p\le5$), (AF2) (3267 word/lift pairs, no failure) and (AF4),
and confirmed the sign criterion on its periodic words: supercritical words give
$-\frac14,-\frac12,-\frac5{13},-\frac74$, the word $(0)$ with $\kappa=0$ gives $0$, and the
subcritical $(0,1)$ gives $+\frac34$ (V-D §(ii)). The criterion is also non-vacuous in both
directions for E2: $w=(1,0)$ is subcritical with realiser $1$ — a genuine positive-integer
periodic seed, the orbit $1\to2\to1$ — while $w=(1,1,0,1,0)$ is subcritical with realiser
$\frac{23}{5} > 0$ that is *not* an integer, which is exactly why L-9918.5(3)'s third,
Diophantine condition is stated separately.

The one thing I did find is a **presentational gap, not a tightness problem**: the
composition step at the head of the proof of L-9918.5(1) needs shift equivariance at
*finite* level ($x \in c(ww') \Rightarrow \Phi^{|w|}(x) \in c(w')$), whereas (AF3) as
written asserts the shift property only on $\widehat S_\infty$; the same reading is what
makes the iterates in (AF2) well defined. It holds in E1, E2 and in every branch system
above. Crucially it is **decorative**: the identity used by (2)–(6), $(M^p-A_w)z=\kappa_w$,
comes from (AF2) + (AF3)-on-$\widehat S_\infty$ + separation of addresses, and the
$A_{w^k}$/$\kappa_{w^k}$ formulas are used nowhere else in the file. A reviewer's note to
this effect has been inserted at the point of use (§9, fix 6).

### 7. The rest of Part A, L-9918.5, L-9918.8, and the four architectures

* **L-9918.1.** All three equivalences check. Discreteness enters (ii)$\Rightarrow$(iii) as
  claimed; see the caveat in §10 about the *second* use in (3).
* **L-9918.2.** $\widehat S_N = \pi_N^{-1}(C_N)$ (both inclusions correct, density used
  correctly); clopen; nested; the König argument uses **only** per-level finiteness and
  produces a persistent chain (I re-ran it as an explicit DFS on seven architectures,
  including two with no seed and one with a seed hidden among escaping branches);
  $\bigcap_N S_N = \widehat S_\infty \cap \mathbb{Z}^+$. Correct.
* **L-9918.3.** Both directions correct, and nestedness really is essential in
  (2)$\Rightarrow$(1): $S_N = \{1\},\{2\},\{1\},\{2\},\dots$ has uniformly bounded
  witnesses and empty intersection.
* **L-9918.5.** (2) is the load-bearing step and is right: $M^p - A_w \equiv -A_w \pmod M$
  with $\gcd(A_w,M)=1$ makes it a unit, hence $\ne 0$ (since $\gcd(0,M) = M \ge 2$) —
  which also rules out $A_w = M^p$, so sub/supercritical is a genuine dichotomy. (4)'s use
  of (AF4) is legitimate because every iterate stays in $\widehat S_1$. (6) uses (AF2) at
  prefixes directly and needs no composition.
* **L-9918.8.** Orthogonality computation, the Markov-type tail bound
  ($d \le \lambda(1-p)+d^2p$), and the losslessness statement all check; re-verified
  numerically for composite $M$ too.
* **E1.** Alphabet, $\nu_2 = 15,12,9,6,3,0$, $\gcd = 7$, $8\alpha_{i+1}=9\alpha_i$, and the
  root classes recomputed from the chart relation: $m_1..m_4 = 6472$, $1908874353$,
  $44906374791168$, $275202518480529950784$, agreeing exactly with
  `experiments/X-9902-sixbranch-leastroots/results/mN_values.txt`, and I additionally
  *ran the chart* on each $m_N$ and confirmed all $N$ digits lie in $A$.
  Uniformly supercritical with $\lambda = P/Q = 1.013643$.
* **E2.** The recursion $\kappa_{wb} = 3^b\kappa_w + b2^{|w|}$ reproduces
  $T^4(x) = (27x+19)/16$ on $(1110)$; threshold $3^a<2^K \iff a/K < \gamma$ is right.
* **E3.** Recomputed from L-9909's definition: counts $1,1,2,3,4,8,13,19$ and the mod-256
  class list agree with L-9909.4 verbatim; refinement holds because $v_j$ depends only on
  $x \bmod 2^{j+1}$.
* **E4.** Fully resolved as claimed; base label corrected (§9, fix 4).
* **T6 self-check.** Re-extracted and re-ran every embedded script myself (V-A): all five
  scripts **and the T6 harness itself** reproduce their recorded output byte-for-byte, exit
  status 0, SHA-256 digests matching those recorded in T6's output, and **no placeholder
  token anywhere**. (Aside: T6's own regex is not line-anchored, so a naive extractor
  truncates T6's block at the literal fence inside its regex string; T6 dodges this by
  skipping itself via its sentinel, and V-A uses a line-anchored regex. The scripts added
  by this note deliberately carry **no** `#!`-shebang, so T6 still finds exactly its five
  pairs and its recorded output stays exact.)

### 8. The author's corrections to the commissioning framing — all five confirmed

1. **"The requirement is $H > C_1R\varphi(H)$, from the resolution term alone, independent
   of $\beta$, and degenerate if $C_1<1$."** CONFIRMED; it is immediate from
   non-negativity of the three terms of (ET).
2. **"B.1's $H \ge R$ is unnecessary."** CONFIRMED for form (3) — and I add the missing
   half: it is **necessary** for the sharper form (2) (counterexample in §4).
3. **"Removing the $\log(4H)$ is necessary but not sufficient."** CONFIRMED:
   $\Theta(4,2/\pi) = \frac1\pi(1+\log4\pi) = 1.123960 > 1$, and admissibility at
   $C_2 = 2/\pi$ requires $C_1 < e^{\pi-1}/\pi = 2.709767$.
4. **"Improving $\tfrac12$ toward $1$ shrinks the admissible region."** CONFIRMED:
   $\Psi_c(s) = cs\,e^{1/(cs)-1}$, $\Psi_1(s) = \Psi_{1/2}(2s)$, ratio $2e^{-1/s} < 1$ iff
   $s < 1/\log 2 = 1.442695$; at $C_2 = 2/\pi$ the threshold falls from $2.709767$ to
   $(2/\pi)e^{\pi/2-1} = 1.126611$. A sharper B.1 **strengthens** the barrier.
5. **The two scope limits (L1 triangle inequality, L2 single cut-off).** CONFIRMED as
   accurate descriptions of where the argument binds: L-9918.6 is invoked only after
   $|S(h)|$ has replaced $S(h)$, and the whole of (d)–(g) fixes one $H$. Phase-preserving
   and multi-scale methods are genuinely untouched.

### 9. Fixes applied (all editorial; none load-bearing)

1. **Gap audit, "Confusion of empirical and universal":** "the *proved* bound there is
   $1.5388$" → "$1.413696$" (the value §(f) actually proves).
2. **Gap audit, "Nonuniform estimates":** the constant list "$\dots,1.538866$ in L-9918.7"
   → "$\dots,1.413696$".
3. **Remaining uncertainty 6(b):** "two explicit numerical thresholds, $4\log12$ and
   $\log 39.7582$" → "$a = 4\log 12 = 9.9396266$ and $u_0 = a\pi = 31.226258$" (the
   thresholds actually used; "$\log 39.7582$" belongs to the abandoned route).
4. **E4's header:** "$M = 2$, $C_N$ … mod $2^{4N}$" is inconsistent with D-9918.1(1)
   ($C_N \subseteq \mathbb{Z}/M^N$); changed to $M = 16$ with classes mod $16^N$, noting
   the equivalent base-2 form that T2/ARCH 5 computes and that the two are cofinal
   subfamilies of one nested family with the same $\bigcap_N S_N$.
5. **Proof of L-9918.7(f):** added the two integer cut-offs $H \in \{1,2\}$ the case split
   does not reach (there the resolution term alone is $\ge 5.545$ resp. $\ge 4.158$), so
   that "(ET) never fires" is covered for every integer $H \ge 1$.
6. **Proof of L-9918.5(1):** inserted a reviewer's note recording that the composition step
   needs finite-level shift equivariance, that this should be read as part of (AF3), and
   that (2)–(6) do not depend on it.

No statement, constant, proof or table elsewhere was altered.

### 10. Residual caveats (things a later reader must not over-read)

* **Part B is about a method family, not about emptiness.** L-9918.7 does not prove
  $m_N\to\infty$ anywhere, and nothing in the file bears on Collatz. The file says this
  repeatedly; it is accurate.
* **"Satisfiable" in (d)/(g) means "the *necessary* condition $(\dagger)$ can hold",** not
  "(ET) fires". Constants inside the region are necessary, not sufficient, for a firing
  criterion. The file's limitation (L3) says exactly this, but (g) read in isolation could
  mislead; quote it with (L3).
* **"Discreteness used exactly once".** True of the equivalence chain in L-9918.1(2). Part A
  does also use well-ordering (to define $m_N = \min S_N$) and finiteness of $[1,B]$ in the
  (iii$'$)$\to$(ii$'$) upgrade of L-9918.1(3) — the Gap audit lists the latter, so the two
  parentheticals should be read together. Not an error; a phrasing to keep honest.
* **The constant $\tfrac12$ in L-9918.6 is not optimal** and is not claimed to be; my
  searches, like the author's, never beat the arithmetic progression (ratio $\ge 2.27$), so
  the true constant is plausibly $1$. This only strengthens L-9918.7.
* **What I did not verify:** L-9904, L-9909 and L-9916 themselves (context only here, and
  nothing is imported); the X-9902 agreement is a cross-check of a computation, not of a
  claim of this file. I did not formalise anything in a proof assistant.

**Confidence.** High on Part A and on L-9918.9 (elementary, fully reconstructed,
mechanically exercised). High on L-9918.6 and L-9918.7(d),(f),(g) (hand-derived twice and
machine-checked on dense grids, with the case split probed at the boundary). Moderate-high
on D-9918.3's axioms being the right general hypotheses — they cover a large natural class,
with the one presentational caveat of §6 now recorded in place.

### V-A — re-extraction and re-run of every embedded script (independent of T6)

```python
# V-A (fable-02-v20): independent re-extraction and re-run of every embedded script.
# Deliberately written WITHOUT the "#!"-shebang first line so that T6's own harness
# (which pairs only shebang-headed blocks) still extracts exactly its five pairs and
# its recorded output stays exact after this note is appended.
import re, subprocess, sys, os, tempfile, hashlib

PATH = "/home/user/collatz/research/foundations/L-9918-extraction-barriers.md"
text = open(PATH).read()
# LINE-ANCHORED fences (the correct markdown reading; T6's own naive regex would be
# truncated by the literal fence inside its regex string -- see the note).
blocks = re.findall(r"(?ms)^```(python|text)\n(.*?)^```", text)
pairs, i = [], 0
while i < len(blocks):
    kind, body = blocks[i]
    if kind == "python" and body.startswith("#!/usr/bin/env python3"):
        assert i+1 < len(blocks) and blocks[i+1][0] == "text", "script with no output block"
        pairs.append((body, blocks[i+1][1])); i += 2
    else:
        i += 1
print("claim file: %s" % PATH)
print("shebang-headed (script, output) pairs found: %d   [T1-T5 and the T6 harness itself]" % len(pairs))
allok = True
for n, (src, exp) in enumerate(pairs, 1):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(src); tmp = f.name
    r = subprocess.run([sys.executable, tmp], capture_output=True, text=True)
    os.unlink(tmp)
    got, e = r.stdout.rstrip("\n"), exp.rstrip("\n")
    ok = (got == e and r.returncode == 0); allok &= ok
    where = "-"
    if not ok:
        gl, el = got.split("\n"), e.split("\n")
        for j in range(max(len(gl), len(el))):
            a = gl[j] if j < len(gl) else "<missing>"
            b = el[j] if j < len(el) else "<missing>"
            if a != b: where = "line %d: %r vs %r" % (j+1, a[:50], b[:50]); break
    print("  script %d  sha256 %s  %4d src lines  %3d output lines  exit %d  ->  %s  %s"
          % (n, hashlib.sha256(src.encode()).hexdigest()[:16], src.count("\n"),
             len(e.split("\n")), r.returncode, "MATCH" if ok else "MISMATCH", where))
    for bad in ("TODO", "FIXME", "placeholder", "PLACEHOLDER", "...output...", "<output>", "XXX"):
        if bad in e:
            print("     !! placeholder token %r in recorded output" % bad); allok = False
print("VERDICT: %s" % ("every embedded block reproduces its recorded output byte-for-byte."
                       if allok else "AT LEAST ONE BLOCK FAILED."))
```

```text
claim file: /home/user/collatz/research/foundations/L-9918-extraction-barriers.md
shebang-headed (script, output) pairs found: 6   [T1-T5 and the T6 harness itself]
  script 1  sha256 3095bcd66235c72e    84 src lines   26 output lines  exit 0  ->  MATCH  -
  script 2  sha256 3adc173888f8c488   135 src lines   65 output lines  exit 0  ->  MATCH  -
  script 3  sha256 906757f37ecfbf92   110 src lines   66 output lines  exit 0  ->  MATCH  -
  script 4  sha256 4e667e39566ee248    84 src lines   57 output lines  exit 0  ->  MATCH  -
  script 5  sha256 1a52934b11ac00a2   102 src lines   72 output lines  exit 0  ->  MATCH  -
  script 6  sha256 150f6db59df39693    55 src lines   10 output lines  exit 0  ->  MATCH  -
VERDICT: every embedded block reproduces its recorded output byte-for-byte.
```

### V-B — the admissible region and every constant of L-9918.7

```python
# V-B (fable-02-v20): the admissible region of L-9918.7 re-derived from the STATEMENT
# alone (no closed form assumed in the numerical half), plus every explicit constant
# of (e), (f), (g) and of Remaining uncertainty 1.
import math

def G(u, C1, C2): return C1/u + (C2/2.0)*max(0.0, math.log(u))     # phi == 1
def Theta_closed(C1, C2): return C1 if 2*C1 <= C2 else (C2/2.0)*(1 + math.log(2*C1/C2))
def Psi(s): return (s/2.0)*math.exp(2.0/s - 1.0)
def boxed(C1, C2): return (C1 < Psi(C2)) if C2 < 2 else (C1 < 1)
GR = (math.sqrt(5)-1)/2

def Theta_num(C1, C2):
    """infimum of G over u>0 found numerically: coarse log grid then golden section."""
    best, bu = float("inf"), 1.0
    for i in range(401):
        u = math.exp(-8.0 + 30.0*i/400.0); g = G(u, C1, C2)
        if g < best: best, bu = g, u
    a, b = bu*math.exp(-0.075), bu*math.exp(0.075)
    for _ in range(120):
        c, d = b - GR*(b-a), a + GR*(b-a)
        if G(c, C1, C2) < G(d, C1, C2): b = d
        else: a = c
    return min(best, G((a+b)/2, C1, C2))

print("=== 1. closed-form Theta vs independent numerical infimum ===")
worst, aw = 0.0, None
for i in range(1, 71):
    for j in range(1, 71):
        C1, C2 = i*0.2, j*0.12
        d = abs(Theta_closed(C1, C2) - Theta_num(C1, C2))
        if d > worst: worst, aw = d, (C1, C2)
print("  max |closed - numeric| over 4900 pairs (C1<=14, C2<=8.4): %.3e  at %s" % (worst, aw))

print("")
print("=== 2. satisfiability of (dagger) by direct scan  vs  the boxed region ===")
def sat(C1, C2, n=1200):
    return any(G(math.exp(-6.0 + 22.0*i/n), C1, C2) < 1.0 for i in range(n+1))
n = skip = 0; bad = []
for j in range(1, 161):
    C2 = j*0.05
    for i in range(1, 281):
        C1 = i*0.05; n += 1
        th = Theta_closed(C1, C2)
        if abs(th - 1.0) <= 5e-3: skip += 1; continue
        if boxed(C1, C2) != (th < 1) or boxed(C1, C2) != sat(C1, C2):
            bad.append((round(C1,3), round(C2,3), th))
print("  %d pairs on a 0.05 grid (C1<=14, C2<=8); %d skipped inside a 5e-3 boundary band" % (n, skip))
print("  disagreements among {Theta<1}, {boxed rule}, {direct scan of u}: %d   %s" % (len(bad), bad[:3]))

print("")
print("=== 3. the boundary C1 = threshold(C2), where the case split could flip ===")
mis = ch = 0
C2 = 0.05
while C2 <= 8.0 + 1e-12:
    thr = Psi(C2) if C2 < 2 else 1.0
    for eps in (-1e-5, -1e-8, 1e-8, 1e-5):
        ch += 1
        if (Theta_closed(thr*(1+eps), C2) < 1) != boxed(thr*(1+eps), C2): mis += 1
    C2 += 0.002
print("  %d checks at C1 = thr*(1+-eps) over 3976 values of C2: mismatches = %d" % (ch, mis))
for C2 in (0.3, 2/math.pi, 1.0, 1.5, 1.999999, 2.0, 2.000001, 3.0):
    thr = Psi(C2) if C2 < 2 else 1.0
    print("     C2=%-9.6f thr=%-13.9f Theta(thr,C2)=%.12f  (must be exactly 1, i.e. NOT admissible)"
          % (C2, thr, Theta_closed(thr, C2)))

print("")
print("=== 4. Psi: minimum exactly 1 at s = 2, strict monotonicity either side ===")
print("  Psi(2) = %.15f" % Psi(2.0))
mn = min((Psi(0.02+i*0.001), 0.02+i*0.001) for i in range(20000))
print("  numeric min over [0.02,20]: %.12f at s = %.4f" % mn)
print("  strictly decreasing on (0.05,2): %s ; strictly increasing on (2,20): %s"
      % (all(Psi(s) > Psi(s+1e-4) for s in [0.05+i*1e-3 for i in range(1940)]),
         all(Psi(s) < Psi(s+1e-4) for s in [2.0+i*1e-3 for i in range(18000)])))
print("  Psi(s) > s/2  iff  s < 2 : %s"
      % all((Psi(s) > s/2) == (s < 2) for s in [0.05+i*0.01 for i in range(1000)] if abs(s-2) > 1e-9))
print("  Psi(2/pi) = %.9f = e^{pi-1}/pi = %.9f ;  Psi(1) = %.9f = e/2 = %.9f"
      % (Psi(2/math.pi), math.exp(math.pi-1)/math.pi, Psi(1.0), math.e/2))

print("")
print("=== 5. (e) the window for (C1,C2) = (1, 2/pi) ===")
C1, C2 = 1.0, 2/math.pi
lo, hi = math.pi, 1e6
for _ in range(300):
    mid = math.sqrt(lo*hi)
    if G(mid, C1, C2) < 1: lo = mid
    else: hi = mid
print("  G(1) = %.12f  ->  u_- = 1 ;  u_+ = %.6f  (file: 19.73524)" % (G(1.0, C1, C2), lo))
print("  u* = 2C1/C2 = %.6f = pi ;  Theta = (1+log pi)/pi = %.9f  (file: 0.682689)"
      % (2*C1/C2, Theta_closed(C1, C2)))
print("  cusp budget (pi/2)(1-1/pi) = %.9f  (file: 1.070796)" % ((1/C2)*(1-1/math.pi)))
print("  {u : G(u)<1} is exactly the interval (1, u_+): %s"
      % all((G(0.005*i, C1, C2) < 1) == (1.0 < 0.005*i < lo)
            for i in range(1, 8000) if abs(G(0.005*i, C1, C2)-1) > 1e-9))

print("")
print("=== 6. (f) the two explicit thresholds and the proved bound ===")
a = 4*math.log(12)
print("  a  = 4 log 12          = %.10f   (file 9.9396266)" % a)
print("  u0 = a*pi              = %.10f   (file 31.226258)" % (a*math.pi))
print("  a/3                    = %.10f   (file 3.313209)" % (a/3))
print("  psi(u0) = (1+log(a pi))/pi = %.10f   (file 1.4136968)" % ((1+math.log(a*math.pi))/math.pi))
print("  1 + log(4 pi log 12)   = %.10f   (file 4.4412593)" % (1+math.log(4*math.pi*math.log(12))))
def Lam(R, H): return 4*R*math.log(4*H)/H + (1/math.pi)*max(0.0, math.log(H/R))
print("  TRUE minima of Lambda (independent 1-D golden section in H for each R):")
def minH(R):
    A, B = math.log(3.0), math.log(1e14)
    for _ in range(250):
        c, d = B - GR*(B-A), A + GR*(B-A)
        if Lam(R, math.exp(c)) < Lam(R, math.exp(d)): B = d
        else: A = c
    return Lam(R, math.exp((A+B)/2)), math.exp((A+B)/2)
for R in (1.0, 2.0, 6.0, 36.0, 1296.0, 1e6):
    v, H = minH(R)
    print("     R = %-9.0f min_H Lambda = %.6f   at H = %.2f" % (R, v, H))
best = (1e18, None); R = 1.0
while R < 1e7:
    v, _ = minH(R)
    if v < best[0]: best = (v, R)
    R *= 1.05
print("  global min over R>=1, H>=3 : %.6f at R = %.3f   (file's T5: 1.6678 at R=1)" % best)
print("  proved threshold 1.413696 is a valid lower bound: %s" % (best[0] > 1.413696))
print("  the two cut-offs the proof text excludes:")
for H in (1, 2):
    print("     H=%d, R=1: resolution term alone 4R log(4H)/H = %.4f > 1  -> (ET) cannot fire"
          % (H, 4*math.log(4*H)/H))

print("")
print("=== 7. (g) and Remaining uncertainty 1 (sensitivity of the region in the B.1 constant) ===")
print("  Theta(4, 2/pi) = (1/pi)(1+log 4pi) = %.9f > 1  (file 1.123960)" % Theta_closed(4.0, 2/math.pi))
print("  Theta(1, 3)    = %.9f  (=1, NOT <1)" % Theta_closed(1.0, 3.0))
def Psi_c(s, c): return c*s*math.exp(1.0/(c*s) - 1.0)
print("  Psi_{1/2} == Psi: %s ;  Psi_1(s) == Psi_{1/2}(2s): %s ;  ratio == 2e^{-1/s}: %s"
      % (all(abs(Psi_c(s,.5)-Psi(s)) < 1e-13 for s in (0.3,0.7,2.0,5.0)),
         all(abs(Psi_c(s,1.)-Psi(2*s)) < 1e-13 for s in (0.3,0.7,1.3,2.6)),
         all(abs(Psi_c(s,1.)/Psi(s) - 2*math.exp(-1/s)) < 1e-12 for s in (0.4,1.0,3.0))))
print("  Psi_1 < Psi_{1/2} iff s < 1/log2 = %.6f : %s"
      % (1/math.log(2), [(s, Psi_c(s,1.) < Psi(s)) for s in (1.0, 1.44, 1.4427, 2.0)]))
print("  c = 1, C2 = 2/pi: threshold falls to (2/pi)e^{pi/2-1} = %.6f  (file 1.12661)"
      % Psi_c(2/math.pi, 1.0))
print("  => a SHARPER B.1 constant shrinks the admissible region: the barrier strengthens.")
```

```text
=== 1. closed-form Theta vs independent numerical infimum ===
  max |closed - numeric| over 4900 pairs (C1<=14, C2<=8.4): 5.329e-15  at (12.0, 8.04)

=== 2. satisfiability of (dagger) by direct scan  vs  the boxed region ===
  44800 pairs on a 0.05 grid (C1<=14, C2<=8); 161 skipped inside a 5e-3 boundary band
  disagreements among {Theta<1}, {boxed rule}, {direct scan of u}: 0   []

=== 3. the boundary C1 = threshold(C2), where the case split could flip ===
  15904 checks at C1 = thr*(1+-eps) over 3976 values of C2: mismatches = 0
     C2=0.300000  thr=43.360404319  Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)
     C2=0.636620  thr=2.709767310   Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)
     C2=1.000000  thr=1.359140914   Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)
     C2=1.500000  thr=1.046709319   Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)
     C2=1.999999  thr=1.000000000   Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)
     C2=2.000000  thr=1.000000000   Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)
     C2=2.000001  thr=1.000000000   Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)
     C2=3.000000  thr=1.000000000   Theta(thr,C2)=1.000000000000  (must be exactly 1, i.e. NOT admissible)

=== 4. Psi: minimum exactly 1 at s = 2, strict monotonicity either side ===
  Psi(2) = 1.000000000000000
  numeric min over [0.02,20]: 1.000000000000 at s = 2.0000
  strictly decreasing on (0.05,2): True ; strictly increasing on (2,20): True
  Psi(s) > s/2  iff  s < 2 : True
  Psi(2/pi) = 2.709767310 = e^{pi-1}/pi = 2.709767310 ;  Psi(1) = 1.359140914 = e/2 = 1.359140914

=== 5. (e) the window for (C1,C2) = (1, 2/pi) ===
  G(1) = 1.000000000000  ->  u_- = 1 ;  u_+ = 19.735236  (file: 19.73524)
  u* = 2C1/C2 = 3.141593 = pi ;  Theta = (1+log pi)/pi = 0.682688726  (file: 0.682689)
  cusp budget (pi/2)(1-1/pi) = 1.070796327  (file: 1.070796)
  {u : G(u)<1} is exactly the interval (1, u_+): True

=== 6. (f) the two explicit thresholds and the proved bound ===
  a  = 4 log 12          = 9.9396265992   (file 9.9396266)
  u0 = a*pi              = 31.2262579033   (file 31.226258)
  a/3                    = 3.3132088664   (file 3.313209)
  psi(u0) = (1+log(a pi))/pi = 1.4136967551   (file 1.4136968)
  1 + log(4 pi log 12)   = 4.4412593403   (file 4.4412593)
  TRUE minima of Lambda (independent 1-D golden section in H for each R):
     R = 1         min_H Lambda = 1.667835   at H = 55.27
     R = 2         min_H Lambda = 1.713552   at H = 132.53
     R = 6         min_H Lambda = 1.772676   at H = 497.29
     R = 36        min_H Lambda = 1.847840   at H = 3917.46
     R = 1296      min_H Lambda = 1.956179   at H = 205523.16
     R = 1000000   min_H Lambda = 2.089095   at H = 247735543.18
  global min over R>=1, H>=3 : 1.667835 at R = 1.000   (file's T5: 1.6678 at R=1)
  proved threshold 1.413696 is a valid lower bound: True
  the two cut-offs the proof text excludes:
     H=1, R=1: resolution term alone 4R log(4H)/H = 5.5452 > 1  -> (ET) cannot fire
     H=2, R=1: resolution term alone 4R log(4H)/H = 4.1589 > 1  -> (ET) cannot fire

=== 7. (g) and Remaining uncertainty 1 (sensitivity of the region in the B.1 constant) ===
  Theta(4, 2/pi) = (1/pi)(1+log 4pi) = 1.123959926 > 1  (file 1.123960)
  Theta(1, 3)    = 1.000000000  (=1, NOT <1)
  Psi_{1/2} == Psi: True ;  Psi_1(s) == Psi_{1/2}(2s): True ;  ratio == 2e^{-1/s}: True
  Psi_1 < Psi_{1/2} iff s < 1/log2 = 1.442695 : [(1.0, True), (1.44, True), (1.4427, False), (2.0, False)]
  c = 1, C2 = 2/pi: threshold falls to (2/pi)e^{pi/2-1} = 1.126611  (file 1.12661)
  => a SHARPER B.1 constant shrinks the admissible region: the barrier strengthens.
```

### V-C — L-9918.6 (exact Abel/telescoping + hostile search) and L-9918.4

```python
# V-C (fable-02-v20): L-9918.6 (universal cusp lower bound) and L-9918.4 ((1110)^inf),
# both re-derived from the statements: exact rational arithmetic for every algebraic
# step, and an independent adversarial hunt for a counterexample multiset.
from fractions import Fraction as F
import math, cmath, random
random.seed(90218)

print("=== 1. Abel summation identity of Step 2, EXACT, on random nonneg sequences ===")
bad = 0
for _ in range(300):
    H = random.randint(1, 25)
    aS = [F(random.randint(0, 40), random.randint(1, 7)) for _ in range(H)]
    T = [F(0)]
    for x in aS: T.append(T[-1] + x)
    if sum(aS[h-1]/h for h in range(1, H+1)) != T[H]/H + sum(T[h]*(F(1,h)-F(1,h+1)) for h in range(1, H)):
        bad += 1
print("  Sigma = T(H)/H + sum_{h<H} T(h)(1/h - 1/(h+1)) : %s" % ("PASS" if bad == 0 else "FAIL %d" % bad))

print("")
print("=== 2. the telescoping step, EXACT, all 1<=R<=29 and R<=H<60 ===")
bad = [(R, H) for R in range(1, 30) for H in range(R, 60)
       if sum(F(h+1-R, h*(h+1)) for h in range(R, H)) != sum(F(1, h) for h in range(R, H)) - 1 + F(R, H)]
print("  sum_{h=R}^{H-1}(h+1-R)/(h(h+1)) = sum_{h=R}^{H-1}1/h - 1 + R/H : %s"
      % ("PASS" if not bad else "FAIL %s" % bad[:3]))
print("  boundary H = R (empty sum; telescoped form reads log1 - 1 + 1 = 0): %s"
      % all(sum(F(h+1-R, h*(h+1)) for h in range(R, R)) == sum(F(1,h) for h in range(R,R)) - 1 + F(R,R)
            for R in range(1, 30)))

print("")
print("=== 3. Step 2 assembled on the EXTREMAL profile T(h) = max(0,(h+1-R)/2) ===")
bad = 0; mins = None
for R in range(1, 25):
    for H in range(R, 90):
        T = [F(0)] + [max(F(0), F(h+1-R, 2)) for h in range(1, H+1)]
        low = float(T[H]/H + sum(T[h]*(F(1,h)-F(1,h+1)) for h in range(1, H)))
        sl = low - 0.5*(math.log(H/R) + 1.0/H)
        if sl < -1e-12: bad += 1
        if mins is None or sl < mins[0]: mins = (sl, (R, H))
print("  the Abel bound is >= (1/2)(log(H/R)+1/H) in all 2136 cases: %s ; min slack %.2e at (R,H)=%s"
      % ("PASS" if bad == 0 else "FAIL(%d)" % bad, mins[0], mins[1]))

print("")
print("=== 4. is the hypothesis H >= R needed?  (form (2) vs form (3)) ===")
pts = [0.0, 0.5]                                   # R = 2, S(1) = 0
S1 = abs(sum(cmath.exp(2j*math.pi*1*x) for x in pts))
print("  points {0, 1/2}: R=2, H=1 < R.  Sigma(1) = |S(1)| = %.6f" % S1)
print("    sharper form (2) would demand >= (1/2)(log(1/2)+1) = %.6f  ->  FAILS: H>=R is NECESSARY in (2)"
      % (0.5*(math.log(0.5)+1.0)))
print("    plain form (3) demands >= (1/2)log(1/2) = %.6f  ->  holds (RHS negative)" % (0.5*math.log(0.5)))
wd = (0.0, None)
for R in range(2, 40):
    p = [i/R for i in range(R)]
    run = 0.0
    for H in range(1, R):
        run += abs(sum(cmath.exp(2j*math.pi*H*x) for x in p))/H
        d = 0.5*(math.log(H/R)+1.0/H) - run
        if d > wd[0]: wd = (d, (R, H))
print("  worst violation of (2) among equally spaced sets with H<R: deficit %.6f at (R,H)=%s" % wd)

print("")
print("=== 5. hostile search for a counterexample to (3) [and to (1),(2) where they apply] ===")
def sig_all(pts, H):
    out, run = [], 0.0
    for h in range(1, H+1):
        run += abs(sum(cmath.exp(2j*math.pi*h*x) for x in pts))/h; out.append(run)
    return out
def viol(pts, H):
    R = len(pts); Sg = sig_all(pts, H); v3 = v2 = 0; ratio = float("inf")
    for h in range(1, H+1):
        lb = 0.5*math.log(h/R)
        if Sg[h-1] < lb - 1e-9: v3 += 1
        if lb > 0: ratio = min(ratio, Sg[h-1]/lb)
        if h >= R and Sg[h-1] < 0.5*(math.log(h/R)+1.0/h) - 1e-9: v2 += 1
    return v3, v2, ratio
g = (math.sqrt(5)-1)/2
fams = []
for R in (1,2,3,5,7,16,17,32,100):
    fams += [("AP", [i/R for i in range(R)]), ("AP shifted", [(i+0.5)/R for i in range(R)]),
             ("all equal", [0.31415]*R), ("Kronecker", [(i*g) % 1 for i in range(R)]),
             ("random", [random.random() for _ in range(R)]),
             ("clustered", [0.7+1e-9*i for i in range(R)]),
             ("two APs", [i/max(1,R//2) for i in range(R//2)]+[0.5+i/max(1,R-R//2) for i in range(R-R//2)]),
             ("quadratic", [(i*i*7 % max(1,R))/R for i in range(R)]),
             ("nested APs", [i/R for i in range(R//2)]+[i/(2*R) for i in range(R-R//2)])]
t3 = t2 = 0; worst = (1e9, None)
for nm, p in fams:
    R = len(p); H = min(40*R+40, 1500)
    v3, v2, ra = viol(p, H); t3 += v3; t2 += v2
    if ra < worst[0]: worst = (ra, (nm, R))
print("  %d structured/degenerate/random families, ALL h <= H: violations of (3) = %d, of (2) = %d"
      % (len(fams), t3, t2))
print("  smallest ratio Sigma/((1/2)log(H/R)) seen: %.5f  at %s" % worst)

def sigma(p, H):
    return sum(abs(sum(cmath.exp(2j*math.pi*h*x) for x in p))/h for h in range(1, H+1))
def anneal(R, H, iters=5000, restarts=5):
    best = None
    for _ in range(restarts):
        p = [random.random() for _ in range(R)]; cur = sigma(p, H)
        for it in range(iters):
            Tm = 0.4*(1-it/iters) + 1e-4
            i = random.randrange(R); q = list(p)
            q[i] = (q[i] + random.gauss(0, max(0.35*Tm, 0.002))) % 1
            c = sigma(q, H)
            if c < cur or random.random() < math.exp(-(c-cur)/(0.02*Tm+1e-12)): p, cur = q, c
        st = 0.05
        for _ in range(3000):
            i = random.randrange(R); q = list(p); q[i] = (q[i] + random.gauss(0, st)) % 1
            c = sigma(q, H)
            if c < cur: p, cur = q, c
            st *= 0.999
        if best is None or cur < best: best = cur
    return best
print("  adversarial minimisation of Sigma(H) (annealing + polish, 5 restarts):")
print("     R    H     best Sigma      AP value     (1/2)log(H/R)   ratio   beats AP?")
mn = 1e9
for R, H in ((2,32),(3,48),(4,64),(5,80),(6,96),(8,128),(16,256)):
    b = anneal(R, H); ap = sigma([i/R for i in range(R)], H); lb = 0.5*math.log(H/R)
    mn = min(mn, b/lb)
    print("    %3d %4d   %12.6f  %11.6f   %12.6f  %6.4f   %s"
          % (R, H, b, ap, lb, b/lb, "YES" if b < ap-1e-6 else "no"))
print("  minimum ratio found by adversarial search: %.5f   (a violation would need < 1)" % mn)

print("")
print("=== 6. L-9918.4 re-derived by exact rational arithmetic ===")
def is_odd(z): return z.numerator % 2 == 1
def T(z): return (3*z+1)/2 if is_odd(z) else z/2
def word(z, k):
    w = []
    for _ in range(k): w.append(1 if is_odd(z) else 0); z = T(z)
    return tuple(w)
ok = all((word(F(r+16*t), 4) == (1,1,1,0)) == (r == 7) for r in range(16) for t in range(-6, 7))
ok &= all((word(F(n, d), 4) == (1,1,1,0)) == ((n*pow(d, -1, 16)) % 16 == 7)
          for d in (3,5,7,9,11,13,15,17) for n in range(-120, 121))
print("  (1) (v0..v3) = (1110)  <=>  x = 7 mod 16, over Z and over Z_(2): %s" % ("PASS" if ok else "FAIL"))
print("  (1) T^4(x) = (27x+19)/16 on 101 lifts of 7 mod 16: %s"
      % ("PASS" if all(T(T(T(T(F(7+16*t))))) == F(27*(7+16*t)+19, 16) for t in range(-50, 51)) else "FAIL"))
print("  (2) 11 T^4(x)+19 = 27(11x+19)/16 on the same lifts: %s"
      % ("PASS" if all(11*T(T(T(T(F(7+16*t)))))+19 == F(27*(11*(7+16*t)+19), 16) for t in range(-50,51)) else "FAIL"))
m2 = (-19*pow(11, -1, 256)) % 256
print("  (3) N = 2 BY HAND: m_2 = (-19)*11^{-1} mod 256 = %d ; 11*%d+19 = %d = 256*%d"
      % (m2, m2, 11*m2+19, (11*m2+19)//256))
z = F(m2); orb = [z]
for _ in range(8): z = T(z); orb.append(z)
print("      T-orbit: %s" % " -> ".join(str(x) for x in orb))
print("      parities = %s  == (1110)^2 : %s" % (str(word(F(m2), 8)), word(F(m2), 8) == (1,1,1,0)*2))
okN = all(((word(F(r if r else 16**N), 4*N) == (1,1,1,0)*N) == (r == (-19*pow(11,-1,16**N)) % 16**N))
          for N in range(1, 5) for r in range(0, 16**N, max(1, 16**N//3000)))
print("  (3) sampled '(v_0..v_{4N-1}) = (1110)^N <=> 16^N | 11x+19', N <= 4: %s" % ("PASS" if okN else "FAIL"))
z0 = F(-19, 11); orb = [z0]
for _ in range(4): orb.append(T(orb[-1]))
print("  (6) the 4-cycle: %s ;  T^4 = id: %s ;  parities %s"
      % (" -> ".join(str(x) for x in orb), orb[0] == orb[4], [1 if is_odd(x) else 0 for x in orb[:4]]))
print("      unique fixed point of x -> (27x+19)/16 is 19/(16-27) = %s ; in Z^+? %s"
      % (F(19, 16-27), F(19,16-27) > 0 and F(19,16-27).denominator == 1))
ms = [(-19*pow(11, -1, 16**N)) % 16**N for N in range(1, 13)]
print("  (4)(5) m_1..m_12 = %s" % ms)
print("      nondecreasing: %s ; every m_N >= 16^{N-1}: %s"
      % (all(ms[i] <= ms[i+1] for i in range(11)), all(ms[i] >= 16**i for i in range(12))))
```

```text
=== 1. Abel summation identity of Step 2, EXACT, on random nonneg sequences ===
  Sigma = T(H)/H + sum_{h<H} T(h)(1/h - 1/(h+1)) : PASS

=== 2. the telescoping step, EXACT, all 1<=R<=29 and R<=H<60 ===
  sum_{h=R}^{H-1}(h+1-R)/(h(h+1)) = sum_{h=R}^{H-1}1/h - 1 + R/H : PASS
  boundary H = R (empty sum; telescoped form reads log1 - 1 + 1 = 0): True

=== 3. Step 2 assembled on the EXTREMAL profile T(h) = max(0,(h+1-R)/2) ===
  the Abel bound is >= (1/2)(log(H/R)+1/H) in all 2136 cases: PASS ; min slack 0.00e+00 at (R,H)=(1, 1)

=== 4. is the hypothesis H >= R needed?  (form (2) vs form (3)) ===
  points {0, 1/2}: R=2, H=1 < R.  Sigma(1) = |S(1)| = 0.000000
    sharper form (2) would demand >= (1/2)(log(1/2)+1) = 0.153426  ->  FAILS: H>=R is NECESSARY in (2)
    plain form (3) demands >= (1/2)log(1/2) = -0.346574  ->  holds (RHS negative)
  worst violation of (2) among equally spaced sets with H<R: deficit 0.153426 at (R,H)=(2, 1)

=== 5. hostile search for a counterexample to (3) [and to (1),(2) where they apply] ===
  81 structured/degenerate/random families, ALL h <= H: violations of (3) = 0, of (2) = 0
  smallest ratio Sigma/((1/2)log(H/R)) seen: 2.26629  at ('AP', 1)
  adversarial minimisation of Sigma(H) (annealing + polish, 5 restarts):
     R    H     best Sigma      AP value     (1/2)log(H/R)   ratio   beats AP?
      2   32       3.380731     3.380729       1.386294  2.4387   no
      3   48       3.381454     3.380729       1.386294  2.4392   no
      4   64       3.383374     3.380729       1.386294  2.4406   no
      5   80       3.388507     3.380729       1.386294  2.4443   no
      6   96       5.327926     3.380729       1.386294  3.8433   no
      8  128       6.042914     3.380729       1.386294  4.3590   no
     16  256       9.669617     3.380729       1.386294  6.9752   no
  minimum ratio found by adversarial search: 2.43868   (a violation would need < 1)

=== 6. L-9918.4 re-derived by exact rational arithmetic ===
  (1) (v0..v3) = (1110)  <=>  x = 7 mod 16, over Z and over Z_(2): PASS
  (1) T^4(x) = (27x+19)/16 on 101 lifts of 7 mod 16: PASS
  (2) 11 T^4(x)+19 = 27(11x+19)/16 on the same lifts: PASS
  (3) N = 2 BY HAND: m_2 = (-19)*11^{-1} mod 256 = 231 ; 11*231+19 = 2560 = 256*10
      T-orbit: 231 -> 347 -> 521 -> 782 -> 391 -> 587 -> 881 -> 1322 -> 661
      parities = (1, 1, 1, 0, 1, 1, 1, 0)  == (1110)^2 : True
  (3) sampled '(v_0..v_{4N-1}) = (1110)^N <=> 16^N | 11x+19', N <= 4: PASS
  (6) the 4-cycle: -19/11 -> -23/11 -> -29/11 -> -38/11 -> -19/11 ;  T^4 = id: True ;  parities [1, 1, 1, 0]
      unique fixed point of x -> (27x+19)/16 is 19/(16-27) = -19/11 ; in Z^+? False
  (4)(5) m_1..m_12 = [7, 231, 743, 41703, 762599, 9151207, 244032231, 780903143, 43730576103, 799644820199, 9595737842407, 255886342464231]
      nondecreasing: True ; every m_N >= 16^{N-1}: True
```

### V-D — the L-9918.9 reduction under a real TM simulator; the affine axioms; E1

```python
# V-D (fable-02-v20): (i) the L-9918.9 halting reduction, driven by a REAL Turing-machine
# simulator rather than by an assumed t(e); (ii) whether D-9918.3's axioms are too tight,
# tested by building a THIRD affine architecture (M = 3) outside E1/E2; (iii) the sign
# criterion in both directions; (iv) E1 recomputed and cross-checked against X-9902.
from fractions import Fraction as F
import itertools, math

# ---------------------------------------------------------------- (i) L-9918.9
class TM:
    """delta: (state, symbol) -> (state', symbol', move); a missing key means HALT."""
    def __init__(self, delta, start=0): self.delta, self.start = delta, start
    def steps_to_halt(self, limit):
        tape, pos, st = {}, 0, self.start
        for t in range(limit):
            s = tape.get(pos, 0)
            if (st, s) not in self.delta: return t
            st, w, mv = self.delta[(st, s)][0], self.delta[(st, s)][1], self.delta[(st, s)][2]
            tape[pos] = w; pos += mv
        return limit if (st, tape.get(pos, 0)) not in self.delta else None

def machine_k(k):   # halts after exactly k executed steps
    return TM({(i, b): (i+1, 1, 1) for i in range(k) for b in (0, 1)})
def machine_inf():  # never halts
    return TM({(0, 0): (0, 1, 1), (0, 1): (0, 0, 1)})

def C_N(tm, N):
    """C_N = {(2^{min(N,t(e))} - 1) mod 2^N}.  Computable: simulate exactly N steps."""
    t = tm.steps_to_halt(N)
    return (2**(N if t is None else min(N, t)) - 1) % (2**N)

def audit(tm, name, halts, NMAX=40):
    C = [C_N(tm, N) for N in range(NMAX+1)]
    wf  = C[0] == 0 and all(0 <= C[N] < 2**N for N in range(NMAX+1))     # D-9918.1(1)
    ref = all(C[N+1] % 2**N == C[N] for N in range(NMAX))                 # D-9918.1(2)
    m   = [C[N] if C[N] >= 1 else 2**N for N in range(NMAX+1)]
    mono = all(m[N] <= m[N+1] for N in range(NMAX))
    stable = all(m[N] == m[NMAX] for N in range(NMAX//2, NMAX+1))
    seed_ok = stable and all(m[NMAX] % 2**N == C_N(tm, N) for N in range(200))
    print("  %-20s R_N=1: True | C_N well formed: %-5s | refinement: %-5s | m_N nondecr: %-5s"
          % (name, wf, ref, mono))
    print("       m_0..m_10 = %-46s  m_%d = %d" % (str(m[:11]), NMAX, m[NMAX]))
    print("       seed exists (checked to level 200): %-5s   machine halts: %-5s   REDUCTION OK: %s"
          % (seed_ok, halts, seed_ok == halts))
    return seed_ok

print("=== (i) L-9918.9: the reduction run against a real TM simulator ===")
for k in (1, 2, 3, 5, 8, 13):
    tm = machine_k(k); t = tm.steps_to_halt(500)
    s = audit(tm, "halts in %d steps" % k, True)
    print("       simulator t(e) = %d ; the predicted seed 2^t-1 = %d" % (t, 2**t - 1))
audit(machine_inf(), "never halts", False)
print("       non-halting case: C_N = {2^N-1}, m_N = 2^N-1 -> oo, adic limit -1 in Z_2.")
print("  boundary case t(e) = 0 (a machine that halts before executing any step):")
tm0 = TM({})
C = [C_N(tm0, N) for N in range(9)]
print("       t(e) = %s ; C_N = %s ; m_N = %s -> oo, so NO seed although the machine HALTS."
      % (tm0.steps_to_halt(50), C, [C[N] if C[N] >= 1 else 2**N for N in range(9)]))
print("       The file stipulates t(e) in Z^+ u {oo}, which excludes this; the one-line")
print("       repair (used below) is c_N = (2^{min(N,t)+1} - 1) mod 2^N.")
def C_N_rep(tm, N):
    t = tm.steps_to_halt(N)
    return (2**((N if t is None else min(N, t)) + 1) - 1) % (2**N)
for nm, tmx, h in (("halts in 0 steps", tm0, True), ("halts in 3 steps", machine_k(3), True),
                   ("never halts", machine_inf(), False)):
    C = [C_N_rep(tmx, N) for N in range(41)]
    m = [C[N] if C[N] >= 1 else 2**N for N in range(41)]
    print("       repaired: %-17s refinement %-5s  m_0..m_6 %-22s stabilises %-5s  halts %-5s agree %s"
          % (nm, all(C[N+1] % 2**N == C[N] for N in range(40)), str(m[:7]),
             all(m[N] == m[40] for N in range(20, 41)), h, all(m[N] == m[40] for N in range(20, 41)) == h))

# ------------------------------------------------- (ii)/(iii) affine generality
print("")
print("=== (ii) a THIRD affine architecture, M = 3, outside E1 and E2 ===")
Ab = {0: 1, 1: 5, 2: 7}                      # gcd(A_b, 3) = 1
kb = {b: (-Ab[b]*b) % 3 for b in (0, 1, 2)}  # kappa_b >= 0, and 3 | A_b b + kappa_b
print("  branch data: A_b = %s, kappa_b = %s ; Phi(x) = (A_b x + kappa_b)/3 on x = b mod 3" % (Ab, kb))
def Phi(x):
    b = (x.numerator * pow(x.denominator, -1, 3)) % 3
    return F(Ab[b]*x + kb[b], 3)
def addr(x, k):
    w = []
    for _ in range(k):
        w.append((x.numerator * pow(x.denominator, -1, 3)) % 3); x = Phi(x)
    return tuple(w)
def AK(w):
    Aw, kw = 1, 0
    for i, b in enumerate(w): kw = Ab[b]*kw + 3**i*kb[b]; Aw *= Ab[b]
    return Aw, kw
bad = tested = 0; onecls = True
for p in range(1, 6):
    for w in itertools.product((0,1,2), repeat=p):
        Aw, kw = AK(w)
        xs = [x for x in range(3**p) if addr(F(x), p) == w]
        if len(xs) != 1: onecls = False; continue
        for t in range(-4, 5):
            x = F(xs[0] + 3**p*t); tested += 1
            y = x
            for _ in range(p): y = Phi(y)
            if y != F(Aw*x + kw, 3**p): bad += 1
print("  (AF1) every word is exactly one class mod 3^p (p<=5): %s" % onecls)
print("  (AF2) Phi^p(x) = (A_w x + kappa_w)/3^p on %d (word,lift) pairs: failures = %d" % (tested, bad))
print("  (AF4) A_b >= 1 and kappa_b >= 0 so Phi(Z^+) subset Z^+: %s" % (min(Ab.values()) >= 1 and min(kb.values()) >= 0))
print("  sign criterion L-9918.5(2),(3) on periodic words of THIS architecture:")
for w in ((2,), (1,), (0,), (1,2), (0,1), (2,0,1)):
    p = len(w); Aw, kw = AK(w); z = F(kw, 3**p - Aw); y = z
    for _ in range(p): y = Phi(y)
    per = all(addr(z, 4*p)[i] == w[i % p] for i in range(4*p))
    print("    w=%-9s A_w=%-4d 3^p=%-4d kappa=%-3d z=%-7s %-5s Phi^p(z)=z:%-5s addr=w^oo:%-5s z in Z^+:%s"
          % (str(w), Aw, 3**p, kw, str(z), "SUPER" if Aw > 3**p else "SUB", y == z, per,
             z > 0 and z.denominator == 1))

print("")
print("=== (iii) the same criterion for E2 (the shortcut map T): both directions non-vacuous ===")
def is_odd(z): return z.numerator % 2 == 1
def T(z): return (3*z+1)/2 if is_odd(z) else z/2
def kap(w):
    k = 0
    for i, b in enumerate(w): k = 3**b*k + b*2**i
    return k
for w in ((1,0), (1,), (0,), (1,1,1,0), (1,1,0), (1,1,0,1,0)):
    p = len(w); Aw, kw = 3**sum(w), kap(w); z = F(kw, 2**p - Aw); y = z
    for _ in range(p): y = T(y)
    ok = True; zz = z
    for i in range(4*p):
        if (1 if is_odd(zz) else 0) != w[i % p]: ok = False
        zz = T(zz)
    print("    w=%-12s a/K=%d/%d A_w=%-4d 2^K=%-4d kappa=%-3d z=%-8s %-5s T^p(z)=z:%-5s addr=w^oo:%-5s z in Z^+:%s"
          % (str(w), sum(w), p, Aw, 2**p, kw, str(z), "SUPER" if Aw > 2**p else "SUB", y == z, ok,
             z > 0 and z.denominator == 1))
print("    w=(1,0) is SUBcritical with realiser 1: a genuine positive-integer periodic seed")
print("    (T-orbit 1 -> 2 -> 1).  w=(1,1,0,1,0) is subcritical with realiser 23/5 > 0 but not")
print("    an integer: the third, Diophantine condition of L-9918.5(3) is separately needed.")

# ------------------------------------------------------------------- (iv) E1
print("")
print("=== (iv) E1 recomputed from the chart relation and cross-checked against X-9902 ===")
P, Q = 3**12, 2**19
A = [7*3**(2*i)*2**(15-3*i) for i in range(6)]
print("  A = %s" % A)
print("  nu2 = %s ; gcd = %d ; all in [0,Q): %s ; 8a_{i+1} = 9a_i: %s"
      % ([(x & -x).bit_length()-1 for x in A], math.gcd(*A), all(0 <= x < Q for x in A),
         all(8*A[i+1] == 9*A[i] for i in range(5))))
def chart_digits(x0, N):
    x, ds = x0, []
    for _ in range(N):
        x2 = -((-P*x)//Q); ds.append(Q*x2 - P*x); x = x2
    return ds
mN = []
for N in range(1, 5):
    rs = {(-pow(P, -N, Q**N)*sum(P**(N-1-j)*Q**j*w[j] for j in range(N))) % Q**N
          for w in itertools.product(A, repeat=N)}
    mN.append(min(rs))
    print("  N=%d: %d words -> %d distinct classes, m_N = %d ; digits of m_N all in A: %s"
          % (N, 6**N, len(rs), min(rs), all(d in A for d in chart_digits(min(rs), N))))
print("  X-9902 results/mN_values.txt records m_1..m_4 = [6472, 1908874353, 44906374791168, 275202518480529950784]")
print("  agreement: %s" % (mN == [6472, 1908874353, 44906374791168, 275202518480529950784]))
print("  uniform supercriticality: A_w/M^p = (P/Q)^p with P/Q = %.9f > 1 : %s" % (P/Q, P > Q))
```

```text
=== (i) L-9918.9: the reduction run against a real TM simulator ===
  halts in 1 steps     R_N=1: True | C_N well formed: True  | refinement: True  | m_N nondecr: True 
       m_0..m_10 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]               m_40 = 1
       seed exists (checked to level 200): True    machine halts: True    REDUCTION OK: True
       simulator t(e) = 1 ; the predicted seed 2^t-1 = 1
  halts in 2 steps     R_N=1: True | C_N well formed: True  | refinement: True  | m_N nondecr: True 
       m_0..m_10 = [1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3]               m_40 = 3
       seed exists (checked to level 200): True    machine halts: True    REDUCTION OK: True
       simulator t(e) = 2 ; the predicted seed 2^t-1 = 3
  halts in 3 steps     R_N=1: True | C_N well formed: True  | refinement: True  | m_N nondecr: True 
       m_0..m_10 = [1, 1, 3, 7, 7, 7, 7, 7, 7, 7, 7]               m_40 = 7
       seed exists (checked to level 200): True    machine halts: True    REDUCTION OK: True
       simulator t(e) = 3 ; the predicted seed 2^t-1 = 7
  halts in 5 steps     R_N=1: True | C_N well formed: True  | refinement: True  | m_N nondecr: True 
       m_0..m_10 = [1, 1, 3, 7, 15, 31, 31, 31, 31, 31, 31]        m_40 = 31
       seed exists (checked to level 200): True    machine halts: True    REDUCTION OK: True
       simulator t(e) = 5 ; the predicted seed 2^t-1 = 31
  halts in 8 steps     R_N=1: True | C_N well formed: True  | refinement: True  | m_N nondecr: True 
       m_0..m_10 = [1, 1, 3, 7, 15, 31, 63, 127, 255, 255, 255]    m_40 = 255
       seed exists (checked to level 200): True    machine halts: True    REDUCTION OK: True
       simulator t(e) = 8 ; the predicted seed 2^t-1 = 255
  halts in 13 steps    R_N=1: True | C_N well formed: True  | refinement: True  | m_N nondecr: True 
       m_0..m_10 = [1, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]   m_40 = 8191
       seed exists (checked to level 200): True    machine halts: True    REDUCTION OK: True
       simulator t(e) = 13 ; the predicted seed 2^t-1 = 8191
  never halts          R_N=1: True | C_N well formed: True  | refinement: True  | m_N nondecr: True 
       m_0..m_10 = [1, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]   m_40 = 1099511627775
       seed exists (checked to level 200): False   machine halts: False   REDUCTION OK: True
       non-halting case: C_N = {2^N-1}, m_N = 2^N-1 -> oo, adic limit -1 in Z_2.
  boundary case t(e) = 0 (a machine that halts before executing any step):
       t(e) = 0 ; C_N = [0, 0, 0, 0, 0, 0, 0, 0, 0] ; m_N = [1, 2, 4, 8, 16, 32, 64, 128, 256] -> oo, so NO seed although the machine HALTS.
       The file stipulates t(e) in Z^+ u {oo}, which excludes this; the one-line
       repair (used below) is c_N = (2^{min(N,t)+1} - 1) mod 2^N.
       repaired: halts in 0 steps  refinement True   m_0..m_6 [1, 1, 1, 1, 1, 1, 1]  stabilises True   halts True  agree True
       repaired: halts in 3 steps  refinement True   m_0..m_6 [1, 1, 3, 7, 15, 15, 15] stabilises True   halts True  agree True
       repaired: never halts       refinement True   m_0..m_6 [1, 1, 3, 7, 15, 31, 63] stabilises False  halts False agree True

=== (ii) a THIRD affine architecture, M = 3, outside E1 and E2 ===
  branch data: A_b = {0: 1, 1: 5, 2: 7}, kappa_b = {0: 0, 1: 1, 2: 1} ; Phi(x) = (A_b x + kappa_b)/3 on x = b mod 3
  (AF1) every word is exactly one class mod 3^p (p<=5): True
  (AF2) Phi^p(x) = (A_w x + kappa_w)/3^p on 3267 (word,lift) pairs: failures = 0
  (AF4) A_b >= 1 and kappa_b >= 0 so Phi(Z^+) subset Z^+: True
  sign criterion L-9918.5(2),(3) on periodic words of THIS architecture:
    w=(2,)      A_w=7    3^p=3    kappa=1   z=-1/4    SUPER Phi^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(1,)      A_w=5    3^p=3    kappa=1   z=-1/2    SUPER Phi^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(0,)      A_w=1    3^p=3    kappa=0   z=0       SUB   Phi^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(1, 2)    A_w=35   3^p=9    kappa=10  z=-5/13   SUPER Phi^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(0, 1)    A_w=5    3^p=9    kappa=3   z=3/4     SUB   Phi^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(2, 0, 1) A_w=35   3^p=27   kappa=14  z=-7/4    SUPER Phi^p(z)=z:True  addr=w^oo:True  z in Z^+:False

=== (iii) the same criterion for E2 (the shortcut map T): both directions non-vacuous ===
    w=(1, 0)       a/K=1/2 A_w=3    2^K=4    kappa=1   z=1        SUB   T^p(z)=z:True  addr=w^oo:True  z in Z^+:True
    w=(1,)         a/K=1/1 A_w=3    2^K=2    kappa=1   z=-1       SUPER T^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(0,)         a/K=0/1 A_w=1    2^K=2    kappa=0   z=0        SUB   T^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(1, 1, 1, 0) a/K=3/4 A_w=27   2^K=16   kappa=19  z=-19/11   SUPER T^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(1, 1, 0)    a/K=2/3 A_w=9    2^K=8    kappa=5   z=-5       SUPER T^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(1, 1, 0, 1, 0) a/K=3/5 A_w=27   2^K=32   kappa=23  z=23/5     SUB   T^p(z)=z:True  addr=w^oo:True  z in Z^+:False
    w=(1,0) is SUBcritical with realiser 1: a genuine positive-integer periodic seed
    (T-orbit 1 -> 2 -> 1).  w=(1,1,0,1,0) is subcritical with realiser 23/5 > 0 but not
    an integer: the third, Diophantine condition of L-9918.5(3) is separately needed.

=== (iv) E1 recomputed from the chart relation and cross-checked against X-9902 ===
  A = [229376, 258048, 290304, 326592, 367416, 413343]
  nu2 = [15, 12, 9, 6, 3, 0] ; gcd = 7 ; all in [0,Q): True ; 8a_{i+1} = 9a_i: True
  N=1: 6 words -> 6 distinct classes, m_N = 6472 ; digits of m_N all in A: True
  N=2: 36 words -> 36 distinct classes, m_N = 1908874353 ; digits of m_N all in A: True
  N=3: 216 words -> 216 distinct classes, m_N = 44906374791168 ; digits of m_N all in A: True
  N=4: 1296 words -> 1296 distinct classes, m_N = 275202518480529950784 ; digits of m_N all in A: True
  X-9902 results/mN_values.txt records m_1..m_4 = [6472, 1908874353, 44906374791168, 275202518480529950784]
  agreement: True
  uniform supercriticality: A_w/M^p = (P/Q)^p with P/Q = 1.013643265 > 1 : True
```

Signed: **fable-02-v20**, 2026-07-25 (adversarial review; verdict PASS).
