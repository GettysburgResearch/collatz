# L-9911 — Structure theorem for the minimal Collatz counterexample (conditional)

```text
Claim ID:      L-9911
Title:         Structure theorem for the minimal counterexample: closure, congruences,
               record-word disjunction, mode dichotomy, and the preimage tree
Status:        PROPOSED
Authoring agent:   fable-02-p6
Reviewing agents:  (none yet)
Created:       2026-07-21
Last updated:  2026-07-21
Dependencies:  NOTATION.md (D-9901, D-9902, D-9905, D-9906, D-9907, D-9908, D-9909,
               D-9910). L-9902 (PROVED; word realization, non-load-bearing remark),
               L-9903 (PROVED; iteration formula and word-remainder bounds, load-bearing
               in L-9911.3), L-9907 (PROPOSED, under review by fable-02-v6;
               load-bearing in L-9911.4 mode (b) — status inherited),
               L-9905 (PROVED per its header — the assignment's "PROPOSED under review"
               is stale; cited as related only, non-load-bearing),
               L-9906 (PROPOSED; related only, non-load-bearing).
               L-9909 (preimages and sieve): NOT YET PRESENT in
               research/foundations/ at time of writing — the small pieces needed here
               (mod-4 descent, T-preimage characterization) are derived inline; overlap
               recorded in the Dependency audit. L-9901 (trichotomy): NOT YET PRESENT —
               the needed dichotomy is re-proved inline (compressed) and in full in
               L-9907.3.
Scope:         The set X of Collatz counterexamples (D-9909) and, under the Standing
               Hypothesis (H) below, its minimum mu. Part 0 (U1-U3) is unconditional;
               sub-claims L-9911.1-.6 are conditional on (H) exactly as marked.
Related counterexample candidates: none yet; this file constrains every future K-candidate
               claiming to be (or to generate) a counterexample.
```

---

## Standing hypothesis

> **(H)** — **ASSUME** the set
> $$X \;:=\; \{\, n \in \mathbb{Z}^+ : 1 \notin O_C(n) \,\}$$
> of Collatz counterexamples (D-9909) is **nonempty**, and let $\mu := \min X$
> (well-defined by the well-ordering of $\mathbb{Z}^+$).
>
> Every sub-claim below tagged **[H]** is conditional on (H). This file does **not**
> assert, and must not be cited as evidence or suggestion, that $X \neq \emptyset$
> (per the neutrality requirement of D-9909). The unconditional statements U1–U3 are
> about the set $X$ as a possibly-empty set and about the maps $T$, $C$ themselves;
> they are true whether or not (H) holds.

---

## Statement

Throughout: $C$ is the Collatz map (D-9901), $T$ the shortcut map (D-9902),
$O_M(n)$ the $M$-orbit including $n$ itself (D-9905), $v_i(n)$, $a_k(n)$ the parity
data (D-9906), $\sigma(n)$ the stopping time (D-9910),
$\gamma = \log_3 2 = 1/\log_2 3 \approx 0.6309298$, and $\rho(w)$ the word-level
remainder of L-9903 (for a word $w \in \{0,1\}^j$; the assignment's notation
"$\rho_j(w)$" is L-9903's $\rho(w)$ with $|w| = j$). For $w \in \{0,1\}^j$ write
$|w|_1$ for its number of ones and $D(w) := 2^j - 3^{|w|_1}$.

### Part 0 — unconditional toolkit (no hypothesis on $X$)

**U1 (orbit comparison).** For every $n \in \mathbb{Z}^+$:
(a) $T^k(n) = C^{\,k + a_k(n)}(n)$ for all $k \ge 0$; in particular
$O_T(n) \subseteq O_C(n)$.
(b) $O_C(n) = O_T(n) \cup \{\, 3x + 1 : x \in O_T(n),\ x \text{ odd} \,\}$.
(c) $1 \in O_C(n) \iff 1 \in O_T(n)$. Consequently
$X = \{ n \in \mathbb{Z}^+ : 1 \notin O_T(n) \}$: membership in $X$ can be tested on
the $T$-orbit.

**U2 (two-sided closure).** For every $n \in \mathbb{Z}^+$:
$$n \in X \iff T(n) \in X, \qquad n \in X \iff C(n) \in X .$$
Hence $X$ is closed under images **and** preimages of both maps; equivalently, $X$ is a
union of complete grand orbits of $T$ (and of $C$).

**U3 ($T$-preimage characterization).** For every $n \in \mathbb{Z}^+$:
$$T^{-1}(n) \cap \mathbb{Z}^+ \;=\; \{\,2n\,\} \;\cup\;
\begin{cases} \left\{ \dfrac{2n-1}{3} \right\} & \text{if } n \equiv 2 \pmod 3,\\[2pt]
\emptyset & \text{otherwise,}\end{cases}$$
where $n \equiv 2 \pmod 3 \iff 3 \mid 2n - 1$; when present, $(2n-1)/3$ is an **odd**
positive integer, distinct from $2n$ (which is even). So every $n$ has exactly one
even $T$-preimage, and exactly one further (odd) $T$-preimage iff $n \equiv 2 \pmod 3$.

### Conditional structure theorem

**L-9911.1 [H] (closure and orbit floor).** Every element of $O_T(\mu)$ and of
$O_C(\mu)$ lies in $X$; consequently $O_T(\mu) \subseteq [\mu, \infty)$ — $\mu$ is the
minimum of its own $T$-orbit — and therefore $\sigma(\mu) = \infty$ (D-9910), i.e.
$T^k(\mu) \ge \mu$ for every $k \ge 1$.

**L-9911.2 [H] (congruence facts).** $\mu \ge 3$, $\mu$ is odd, and
$\mu \equiv 3 \pmod 4$; equivalently $v_0(\mu) = v_1(\mu) = 1$.

**L-9911.3 [H] (record-word disjunction).** For **every** $j \ge 1$, exactly one of
the following holds, where $w = (v_0(\mu), \dots, v_{j-1}(\mu))$ is $\mu$'s length-$j$
parity word and $a_j = a_j(\mu) = |w|_1$:
1. $a_j \ge \lceil j\gamma \rceil$ (equivalently $3^{a_j} > 2^j$, equivalently
   $D(w) < 0$) — call such a $w$ a **$j$-survivor word**; or
2. $a_j \le \lfloor j\gamma \rfloor$ (equivalently $D(w) > 0$), and then
   $$\mu \;\le\; \frac{\rho(w)}{2^j - 3^{a_j}} = \frac{\rho(w)}{D(w)} .$$

($D(w) = 0$ is impossible for $j \ge 1$; $j\gamma \notin \mathbb{Z}$ for $j \ge 1$ by
the irrationality of $\log_2 3$, proved inline, which is what makes
$\lceil j\gamma\rceil$/$\lfloor j\gamma\rfloor$ the exact thresholds.)

**Corollary (uniform bound $B_j$).** Define, for $j \ge 1$,
$$B_j \;:=\; \max\left\{ \frac{\rho(w)}{D(w)} \;:\; w \in \{0,1\}^j,\ D(w) > 0 \right\}
\;=\; \max_{\substack{0 \le a \le \lfloor j\gamma \rfloor}}
\frac{2^{\,j-a}\left(3^a - 2^a\right)}{2^j - 3^a}
\quad\text{(the } a{=}0 \text{ term is } 0\text{)},$$
the second equality by L-9903.3 (ones-last words maximize $\rho$ at fixed $a$, and
$D(w)$ depends only on $a$). Then for each $j \ge 1$: **either** $\mu$'s length-$j$
parity word is a $j$-survivor word, **or** $\mu \le B_j$. Contrapositive search form:
for every $j$ with $B_j < \mu$, necessarily $a_j(\mu) \ge \lceil j\gamma \rceil$, hence
$a_j(\mu)/j \ge \gamma$ at every such $j$.

**L-9911.4 [H] (mode dichotomy with constraints).** Exactly one of:
- **(a)** $O_T(\mu)$ eventually enters a **nontrivial** $T$-cycle $\Gamma_0$
  (D-9908; nontrivial because $1 \notin O_T(\mu)$), and then
  $\mu \le x_{\min}(\Gamma_0) := \min \Gamma_0$;
- **(b)** $T^k(\mu) \to \infty$, and then $\liminf_{k} a_k(\mu)/k \ge \gamma$
  (via L-9907.2; status inherited from L-9907, currently PROPOSED under review).

Moreover, **independently of the mode** (and with (H) automatic from the cycle's
existence): *if any nontrivial $T$-cycle $\Gamma$ exists, then $\Gamma \subseteq X$
(so $X \neq \emptyset$) and $\mu \le x_{\min}(\Gamma)$.* Thus $\mu$ is a lower bound
for every element of every nontrivial $T$-cycle that exists, not merely of the one
(if any) that $\mu$'s orbit enters.

**L-9911.5 (the counterexample tree).** Unconditional part: by U2 + U3, $X$ is closed
under
$$n \longmapsto 2n \quad (\text{always}), \qquad\qquad
n \longmapsto \frac{2n-1}{3} \quad (\text{when } n \equiv 2 \bmod 3),$$
and these two maps produce **all** $T$-preimages, so no further backward closure
exists to exploit. Conditional part [H]: the full $T$-preimage set
$P^*(\mu) := \{ x \in \mathbb{Z}^+ : T^t(x) = \mu \text{ for some } t \ge 0 \}$
satisfies $P^*(\mu) \subseteq X$ and is infinite (it contains $2^t\mu$ for every
$t \ge 0$); organized by the branching rule above it is an infinite
binary-branching-where-permitted structure above $\mu$ (a genuine tree when $\mu$ is
not $T$-periodic; see the proof for the precise caveat when $\mu$ lies on a cycle).
This matches issue #25's hypotheses as quoted ("closed under $n \to 2n$ and
$n \to (2n-1)/3$ when $n \equiv 2 \bmod 3$") exactly; see the correspondence note in
the proof.

**L-9911.6 [H] (packaging — practical search corollary).** Stated in the proof
section; one paragraph, no new mathematics.

---

## Definitions

- $C(n)$: D-9901. $T(n)$: D-9902. $O_M(n) = (n, M(n), M^2(n), \dots)$, treated as a
  set where convenient; "$n$ reaches 1 under $M$" means $M^k(n) = 1$ for some
  $k \ge 0$: D-9905. Trivial cycles: under $C$: $(1,4,2)$; under $T$: $(1,2)$
  (D-9905). A cycle of $M$ is a purely periodic orbit; nontrivial = not the trivial
  cycle of $M$ (D-9908).
- $v_i(n) = T^i(n) \bmod 2$, $a_k(n) = \sum_{i<k} v_i(n)$: D-9906. $a_0 = 0$.
- Counterexample, $X$: D-9909. $\sigma(n) = \inf\{k \ge 1 : T^k(n) < n\}$: D-9910.
- $\gamma = \log_3 2$; $\gamma \log_2 3 = 1$.
- $\rho(w)$ for $w \in \{0,1\}^j$: the L-9903 word remainder
  ($r_0 = 0$, $r_{i+1} = 3^{w_i} r_i + w_i 2^i$, $\rho(w) = r_j$), with
  $\rho_k(n) = \rho(v_0(n),\dots,v_{k-1}(n))$ and the exact identity
  $2^k T^k(n) = 3^{a_k(n)} n + \rho_k(n)$ (L-9903.1–.2, PROVED).
- $D(w) := 2^{|w|} - 3^{|w|_1}$; $B_j$ as in the L-9911.3 corollary;
  **$j$-survivor word**: $w \in \{0,1\}^j$ with $|w|_1 \ge \lceil j\gamma\rceil$
  (terminology local to this file).
- **Eventually periodic / enters a cycle:** $O_T(n)$ eventually enters the cycle
  $\Gamma$ if there are $k_1 \ge 0$, $p \ge 1$ with $T^{k+p}(n) = T^k(n)$ for all
  $k \ge k_1$ and $\Gamma = \{T^k(n) : k \ge k_1\}$.
- $x_{\min}(\Gamma) := \min \Gamma$ for a cycle $\Gamma$ (a finite nonempty set).

---

## Motivation

This is the packet's synthesis file for search and construction programs: it converts
the individual foundations lemmas into a single conditional structure theorem — "what
a counterexample must look like" — intended as the citable interface for issues #9,
#10, #21, #25, and #4:

- **#25 (preimage-tree program):** U2 + U3 + L-9911.5 prove exactly the closure
  hypotheses that program assumes, and additionally prove completeness (there are no
  other $T$-preimages to add).
- **#21 (supercritical foundry) and #10, #4/M1 (divergence programs):** L-9911.4(b)
  packages the density obstruction (L-9907) as it applies to the minimal
  counterexample; L-9911.3 gives the finite-window record constraints that any
  candidate parity word must satisfy at every prefix length.
- **#9 (cycle synthesis):** L-9911.4's cycle-mode statement pins the correct logical
  form of "the minimal counterexample bounds every nontrivial cycle from below", and
  routes element-size questions to L-9905/L-9906 (with the $T$/$S$ translation
  explicitly flagged as an open packet item, not silently assumed).
- Any future **K-candidate** must be consistent with every [H]-claim here, since a
  verified counterexample would make (H) true; L-9911.6 lists the checklist.

---

## Proof or construction

### U1 (orbit comparison) — unconditional

**(a).** Fix $n$. We show by induction on $k \ge 0$ that
$T^k(n) = C^{\,k + a_k(n)}(n)$.

*Base $k = 0$:* both sides are $n$ ($a_0 = 0$).

*Step:* assume $T^k(n) = C^{j}(n)$ with $j = k + a_k(n)$, and write $x := T^k(n)$.
- If $x$ is even ($v_k = 0$): $C^{j+1}(n) = C(x) = x/2 = T^{k+1}(n)$, and
  $j + 1 = (k+1) + a_{k+1}(n)$ since $a_{k+1} = a_k$.
- If $x$ is odd ($v_k = 1$): $C^{j+1}(n) = C(x) = 3x + 1$, which is even
  ($3\cdot\text{odd}+1$), so $C^{j+2}(n) = (3x+1)/2 = T^{k+1}(n)$, and
  $j + 2 = (k+1) + a_{k+1}(n)$ since $a_{k+1} = a_k + 1$.

Induction complete; in particular every $T$-iterate of $n$ is a $C$-iterate:
$O_T(n) \subseteq O_C(n)$.

**(b).** ($\subseteq$ of the right side into $O_C(n)$:) $O_T(n) \subseteq O_C(n)$ by
(a); and if $x \in O_T(n)$ is odd, say $x = T^k(n) = C^{j}(n)$ with $j = k + a_k$,
then $3x + 1 = C^{j+1}(n) \in O_C(n)$.
($\supseteq$: every $C$-iterate is of one of the two forms:) by induction on $j$ we
show every $j \ge 0$ satisfies exactly one of:
(i) $j = k + a_k(n)$ for some $k \ge 0$, and then $C^j(n) = T^k(n) \in O_T(n)$;
(ii) $j = k + a_k(n) + 1$ for some $k \ge 0$ with $v_k(n) = 1$, and then
$C^j(n) = 3\,T^k(n) + 1$ with $T^k(n) \in O_T(n)$ odd.
*Base $j = 0$:* form (i) with $k = 0$. *Step:* if $j$ has form (i) with witness $k$:
when $T^k(n)$ is even, $j + 1 = (k+1) + a_{k+1}$ has form (i); when $T^k(n)$ is odd,
$j+1 = k + a_k + 1$ has form (ii) (witness $k$, $v_k = 1$). If $j$ has form (ii) with
witness $k$: $C^j(n) = 3T^k(n)+1$ is even, so
$C^{j+1}(n) = (3T^k(n)+1)/2 = T^{k+1}(n)$ and $j + 1 = (k+1) + a_{k+1}$ has form (i).
This proves (b).

**(c).** ($\Leftarrow$) by (a). ($\Rightarrow$) if $1 \in O_C(n)$ then by (b) either
$1 \in O_T(n)$ (done) or $1 = 3x + 1$ for some odd $x \in O_T(n)$, forcing $x = 0
\notin \mathbb{Z}^+$ — impossible. Hence $1 \in O_T(n)$. Consequently
$1 \notin O_C(n) \iff 1 \notin O_T(n)$, i.e. $X = \{n : 1 \notin O_T(n)\}$.
$\blacksquare$

*(Finite check: Test 7 verifies (a)'s index law $T^k(n) = C^{k+a_k}(n)$ on 1000 random
$(n,k)$.)*

### U2 (two-sided closure) — unconditional

First the tail relation: for $M \in \{C, T\}$ and any $n$,
$M^k(n) = M^{k-1}(M(n))$ for all $k \ge 1$ (induction on $k$; base $k=1$ trivial), so
$$O_M(n) = \{n\} \cup O_M(M(n)). \tag{U2.1}$$

**Forward ($n \in X \Rightarrow M(n) \in X$), for $M = T$ using U1(c):** if
$1 \in O_T(T(n))$ then $1 \in O_T(n)$ by (U2.1), contradicting $n \in X$. So
$T(n) \in X$. Identically for $M = C$ with $O_C$ (using the $C$-form of D-9909
directly).

**Backward ($M(n) \in X \Rightarrow n \in X$):** suppose $1 \in O_T(n)$. By (U2.1)
either $n = 1$ or $1 \in O_T(T(n))$. The second contradicts $T(n) \in X$ (U1(c)).
The first is also impossible: $n = 1$ gives $T(n) = 2$ and
$O_T(2) = (2, 1, 2, \dots) \ni 1$, so $T(n) \notin X$, contradiction. Hence
$1 \notin O_T(n)$: $n \in X$. For $M = C$: either $n = 1$ or $1 \in O_C(C(n))$; the
second contradicts $C(n) \in X$; the first gives $C(1) = 4$ and
$O_C(4) = (4, 2, 1, \dots) \ni 1$, so $C(n) \notin X$, contradiction.

Both equivalences of U2 are proved. By induction along orbits and preimage chains, $X$
is a union of complete grand orbits of each map. $\blacksquare$

### U3 ($T$-preimage characterization) — unconditional

Fix $n \in \mathbb{Z}^+$ and let $x \in \mathbb{Z}^+$ with $T(x) = n$.
- If $x$ is even: $T(x) = x/2 = n \iff x = 2n$. Conversely $2n$ is even and
  $T(2n) = n$: the even preimage always exists and is unique.
- If $x$ is odd: $T(x) = (3x+1)/2 = n \iff 3x = 2n - 1 \iff x = (2n-1)/3$. Such an
  integer $x$ exists iff $3 \mid 2n - 1$. Since $2n - 1 \equiv 2n - 1 \pmod 3$ and
  $2 \cdot 2 \equiv 1 \pmod 3$: $3 \mid 2n-1 \iff 2n \equiv 1 \pmod 3 \iff n \equiv 2
  \pmod 3$. When this holds, $3x = 2n - 1$ is odd, so $x$ is odd (an even $x$ would
  make $3x$ even), and $x \ge 1 \iff 2n - 1 \ge 3 \iff n \ge 2$, which is automatic
  for $n \equiv 2 \pmod 3$, $n \in \mathbb{Z}^+$ (least case $n = 2$, giving $x = 1$,
  and indeed $T(1) = 2$). Conversely such $x$ is odd and $T(x) = n$ by construction.

The two candidate preimages are distinct ($2n$ even, $(2n-1)/3$ odd). This proves U3.
$\blacksquare$ *(Test 1 verifies U3 exhaustively for $n \le 10^5$, both soundness and —
via the elementary bound $T(x) \ge x/2$, so any preimage of $n$ is $\le 2n$ —
completeness.)*

### L-9911.1 [H] — closure and orbit floor

By U2 (forward direction) and induction on $k$: $T^k(\mu) \in X$ and $C^k(\mu) \in X$
for every $k \ge 0$, i.e. $O_T(\mu) \cup O_C(\mu) \subseteq X$. By minimality of
$\mu$, every element of $X$ is $\ge \mu$; hence $O_T(\mu) \subseteq [\mu, \infty)$:
$T^k(\mu) \ge \mu$ for all $k \ge 0$, so $\mu = \min O_T(\mu)$, and no $k \ge 1$ has
$T^k(\mu) < \mu$. By D-9910, $\sigma(\mu) = \inf \emptyset = \infty$. $\blacksquare$

### L-9911.2 [H] — congruence facts

**$\mu \ge 3$.** $O_C(1) = (1, 4, 2, 1, \dots) \ni 1$ and $O_C(2) = (2, 1, \dots) \ni
1$ (both by direct computation, using "reaches 1" with $k \ge 0$ per D-9905), so
$1, 2 \notin X$ and $\mu \ge 3$.

**$\mu$ is odd.** If $\mu$ were even, then $T(\mu) = \mu/2 \in X$ by U2 (forward),
and $\mu/2 < \mu$ — contradicting minimality. So $\mu$ is odd; equivalently
$v_0(\mu) = 1$.

**$\mu \equiv 3 \pmod 4$.** Suppose instead $\mu \equiv 1 \pmod 4$; write
$\mu = 4t + 1$ ($t \ge 1$ since $\mu \ge 3$ is odd and $\ne 1$). Explicitly:
$$C(\mu) = 3\mu + 1 = 12t + 4, \qquad
C^2(\mu) = \frac{3\mu+1}{2} = 6t + 2 \ \ (\text{even}), \qquad
C^3(\mu) = \frac{3\mu+1}{4} = 3t + 1 .$$
All steps are legitimate: $3\mu + 1$ is even; $6t+2$ is even; and
$(3\mu+1)/4 = 3t + 1 \in \mathbb{Z}^+$ exactly because $4 \mid 3\mu + 1$ when
$\mu \equiv 1 \pmod 4$ ($3\mu + 1 \equiv 3 + 1 = 4 \equiv 0 \pmod 4$). By U2
(forward, three times), $3t + 1 \in X$. But
$$\frac{3\mu + 1}{4} < \mu \iff 3\mu + 1 < 4\mu \iff \mu > 1,$$
which holds. So $3t+1$ is a counterexample smaller than $\mu$ — contradicting
minimality. Hence $\mu \not\equiv 1 \pmod 4$; being odd, $\mu \equiv 3 \pmod 4$.
(In $T$-form: $T^2(\mu) = (3\mu+1)/4 < \mu$ would give $\sigma(\mu) \le 2$,
contradicting L-9911.1.)

**Parity-word form.** $\mu$ odd gives $v_0(\mu) = 1$. For $\mu = 4t + 3$:
$T(\mu) = (12t + 10)/2 = 6t + 5$, odd, so $v_1(\mu) = 1$; for $\mu = 4t+1$:
$T(\mu) = 6t + 2$, even, so $v_1 = 0$. Hence, for odd $\mu$,
$\mu \equiv 3 \pmod 4 \iff v_0(\mu) = v_1(\mu) = 1$ (this is L-9907.5 with $j = 2$,
re-derived directly). $\blacksquare$

**Machine-checked finite floor (labeled).** Test 5 below verifies, by direct
iteration, that every $2 \le n \le 10^6$ has some $T$-iterate below itself. By strong
induction on $n$ this implies every $n \le 10^6$ reaches $1$ under $T$ (base:
$T(2) = 1$; step: follow the orbit down to a value $< n$, which reaches 1 by the
induction hypothesis, or is 1 itself), hence under $C$ by U1(c). Therefore
$X \cap [1, 10^6] = \emptyset$ — a **finite, machine-checked fact** (rerunnable code
below; not a hand proof) — and conditionally on (H), $\mu > 10^6$. No external
verification ranges (literature/BOINC) are imported anywhere in this file.

### L-9911.3 [H] — record-word disjunction

**Irrationality of $\log_2 3$ (inline).** If $\log_2 3 = p/q$ with $p, q \in
\mathbb{Z}^+$, then $2^p = 3^q$, an even number equal to an odd number — impossible.
So $\log_2 3 \notin \mathbb{Q}$, hence $\gamma = 1/\log_2 3 \notin \mathbb{Q}$, and
for every $j \ge 1$, $j\gamma \notin \mathbb{Z}$ (else $\gamma = z/j$ would be
rational). Consequently, for integers $a$ and $j \ge 1$:
$$3^a \ge 2^j \iff a \log_2 3 \ge j \iff a \ge j\gamma \iff a > j\gamma
\iff a \ge \lceil j\gamma \rceil,$$
and $3^a = 2^j$ never holds (so $D(w) \neq 0$ for every $w \in \{0,1\}^j$, $j \ge 1$).
*(Test 2 confirms $\min\{a : 3^a > 2^j\} = \lceil j\gamma\rceil$ by pure integer
comparison for $j \le 60$.)*

**The disjunction.** Fix $j \ge 1$; let $w$, $a_j$, $D(w) = 2^j - 3^{a_j}$ be as in
the statement. By L-9911.1, $T^j(\mu) \ge \mu$. By L-9903.1 (PROVED),
$2^j\,T^j(\mu) = 3^{a_j}\mu + \rho(w)$. Therefore
$$T^j(\mu) \ge \mu
\iff 3^{a_j}\mu + \rho(w) \ge 2^j \mu
\iff \mu\,\big(2^j - 3^{a_j}\big) \le \rho(w)
\iff \mu\, D(w) \le \rho(w). \tag{3.1}$$
*(Test 6 checks the chain (3.1) on 2000 random integer trajectories.)* Split on the
sign of $D(w)$ (nonzero, as shown):
- $D(w) < 0$: then $\mu D(w) < 0 \le \rho(w)$ (L-9903.3: $\rho \ge 0$), so (3.1)
  holds automatically and imposes **no** constraint on $\mu$. By the equivalence
  above, $D(w) < 0 \iff a_j \ge \lceil j\gamma\rceil$: branch 1 ($j$-survivor word).
- $D(w) > 0$: dividing (3.1) by $D(w) > 0$ gives $\mu \le \rho(w)/D(w)$: branch 2.
  And $D(w) > 0 \iff a_j \le \lfloor j\gamma \rfloor$ (again since
  $j\gamma \notin \mathbb{Z}$).

The two branches are mutually exclusive and exhaustive (determined by the sign of
$D(w)$). $\blacksquare$

**Corollary ($B_j$).** In branch 2, $\mu \le \rho(w)/D(w) \le B_j$ by definition of
$B_j$ (a maximum over a finite nonempty set — it contains $w = 0^j$ with ratio $0$, so
$B_j \ge 0$ and is well-defined). For the closed form: group words with $D(w) > 0$ by
$a := |w|_1$, which ranges over $0 \le a \le \lfloor j\gamma\rfloor$; at fixed $a$ the
denominator $2^j - 3^a$ is a positive constant and, by L-9903.3 (PROVED), the maximum
of $\rho(w)$ over $|w|_1 = a$ is $2^{j-a}(3^a - 2^a)$, attained exactly at the
ones-last word $0^{j-a}1^a$ (for $a \ge 1$; for $a = 0$, $\rho = 0$). Maximizing over
$a$ gives the displayed closed form. *(Test 3 confirms brute force $=$ closed form for
$j \le 12$.)* Every maximizing word is realized by an actual residue class mod $2^j$
(L-9902.2 / R-9903-A, PROVED), so $B_j$ cannot be improved by discarding
"unrealizable" words — there are none. $\blacksquare$

**Worked examples and consistency.** $B_1 = 0$ (only $a = 0$), so branch 2 at $j=1$
would force $\mu \le 0$, impossible: hence $a_1(\mu) \ge \lceil\gamma\rceil = 1$,
i.e. $\mu$ odd — recovering L-9911.2. $B_2 = 2$ and $\mu \ge 3$: hence
$a_2(\mu) \ge \lceil 2\gamma\rceil = 2$, i.e. $v_0 = v_1 = 1$, i.e.
$\mu \equiv 3 \pmod 4$ — recovering L-9911.2 again. $B_4 = 20/7 < 3 \le \mu$: hence
$a_4(\mu) \ge \lceil 4\gamma \rceil = 3$ — at least three of $\mu$'s first four
parities are 1, a fact strictly beyond L-9911.2. Computed table (Test 3, exact):
$$B_1{=}0,\ B_2{=}2,\ B_3{=}\tfrac45,\ B_4{=}\tfrac{20}{7},\ B_5{=}\tfrac{76}{5},\
B_6{=}\tfrac{152}{37},\ B_7{=}\tfrac{520}{47},\ B_8{=}\tfrac{1688}{13},\
B_9{=}\tfrac{3376}{269},\ B_{10}{=}\tfrac{2128}{59},\
B_{11}{=}\tfrac{21280}{1319},\ B_{12}{=}\tfrac{65888}{1909}.$$
Note the spike at $j = 8$ ($B_8 \approx 129.85$): $2^8 - 3^5 = 13$ is small because
$8/5$ is a continued-fraction convergent of $\log_2 3$ — the same rational-approximation
phenomenon as L-9905.5. $B_j$ is not monotone and is unbounded along convergent-driven
subsequences; the usable form is the contrapositive: at every $j$ with $B_j < \mu$,
$a_j(\mu) \ge \lceil j\gamma\rceil$, so $a_j(\mu)/j \ge \gamma$ **at those $j$**.
(Combined with the machine floor $\mu > 10^6$: this holds at least for all
$j \le 12$, and for every larger $j$ with $B_j \le 10^6$.)

### L-9911.4 [H] — mode dichotomy with constraints

**Dichotomy.** Compressed inline re-proof (full version: L-9907.3, this packet; the
planned L-9901 file had not landed at time of writing): if $T^k(\mu) \not\to \infty$,
then some bound $B$ has $T^k(\mu) \le B$ infinitely often; the values lie in the
finite set $\{1, \dots, B\}$, so some value recurs: $T^{k_1}(\mu) = T^{k_2}(\mu)$
with $k_1 < k_2$; determinism of $T$ propagates this forward
($T^{k_1+t} = T^{k_2+t}$ for all $t \ge 0$), so the orbit is eventually periodic with
period $p = k_2 - k_1$, entering the cycle
$\Gamma_0 := \{T^k(\mu) : k \ge k_1\}$ (a purely periodic orbit from index $k_1$ on).
So: either the orbit eventually enters a $T$-cycle, or $T^k(\mu) \to \infty$; these
are mutually exclusive (an eventually periodic orbit is bounded, a divergent one is
not).

**Mode (a): the entered cycle is nontrivial and bounds $\mu$.** Since $\mu \in X$,
U1(c) gives $1 \notin O_T(\mu) \supseteq \Gamma_0$, so $1 \notin \Gamma_0$; the
trivial $T$-cycle is $(1,2)$ (D-9905), which contains 1, so
$\Gamma_0 \neq \{1,2\}$: $\Gamma_0$ is nontrivial (D-9908). Moreover
$\Gamma_0 \subseteq O_T(\mu) \subseteq [\mu, \infty)$ by L-9911.1, so
$\mu \le x_{\min}(\Gamma_0)$.

**Every existing nontrivial cycle bounds $\mu$ (mode-independent).** Let $\Gamma$ be
*any* nontrivial $T$-cycle (assumed to exist; this is a hypothesis about $\Gamma$,
and it *implies* (H), as we now show). Let $x \in \Gamma$. Since $\Gamma$ is a purely
periodic orbit (D-9908), $O_T(x) = \Gamma$ as a set. If $1 \in \Gamma$, then $\Gamma$
is the periodic orbit through 1, and $O_T(1) = (1, 2, 1, 2, \dots)$, so
$\Gamma = \{1, 2\}$ — the trivial cycle, contradiction. Hence $1 \notin O_T(x)$, so
by U1(c) $x \in X$. Thus $\Gamma \subseteq X$; in particular $X \neq \emptyset$, (H)
holds, $\mu$ is defined, and by minimality $\mu \le x$ for every $x \in \Gamma$:
$\mu \le x_{\min}(\Gamma)$. (Note the two routes: for the *entered* cycle
$\Gamma_0$ the bound also follows from the orbit floor; for an *arbitrary* existing
cycle only the minimality route is available — its elements need not lie on
$O_T(\mu)$.)

**Mode (b): density.** If $T^k(\mu) \to \infty$, then L-9907.2 (applied to $n = \mu$;
its hypothesis is exactly divergence) gives
$\liminf_k a_k(\mu)/k \ge \gamma$. This conclusion inherits L-9907's current status
(PROPOSED, under adversarial review by fable-02-v6); every other part of L-9911.4
rests only on PROVED dependencies or inline proofs.

**Combined theorem.** Under (H), exactly one of:
(a) $O_T(\mu)$ enters a nontrivial $T$-cycle $\Gamma_0$, with
$\mu \le x_{\min}(\Gamma_0)$ — and simultaneously $\mu \le x_{\min}(\Gamma)$ for
every nontrivial $T$-cycle $\Gamma$ in existence; or
(b) $T^k(\mu) \to \infty$ with $\liminf_k a_k(\mu)/k \ge \gamma$.
In both modes, all of L-9911.1–.3 and .5 hold as well. $\blacksquare$

*Related, non-load-bearing:* element-size constraints on nontrivial cycles (hence,
via mode (a), on $\mu$) are the business of L-9905/L-9906 — but those files treat
**$S$-cycles**, and the translation between nontrivial $T$-cycles and nontrivial
$S$-cycles is **not** proved in this file nor in L-9906 (whose Scope note explicitly
excludes it). Until a packet lemma supplies that translation, do not chain
L-9911.4(a) with L-9905/L-9906 numerics. Flagged as Suggested next attack item 1.

### L-9911.5 — the counterexample tree

**Unconditional closure.** Let $n \in X$. By U3, the $T$-preimages of $n$ are $2n$
and — exactly when $n \equiv 2 \pmod 3$ — the odd integer $(2n-1)/3$. By U2
(backward), every $T$-preimage of an element of $X$ is in $X$. Hence $X$ is closed
under $n \mapsto 2n$ and, when $n \equiv 2 \pmod 3$, under $n \mapsto (2n-1)/3$; and
by U3's completeness there are **no other** $T$-preimages, so this branching rule
generates the entire backward closure. (These statements are implications about the
possibly-empty set $X$; they are unconditional.)

**Conditional structure [H].** Define
$P^*(\mu) := \{x \in \mathbb{Z}^+ : \exists\, t \ge 0,\ T^t(x) = \mu\}$.
By induction on $t$ using U2 (backward): every $x \in P^*(\mu)$ is in $X$ (base
$t = 0$: $\mu \in X$; step: $T^t(x) = \mu$ with $t \ge 1$ means $T(x) \in P^*(\mu)$
at depth $t - 1$, so $T(x) \in X$, so $x \in X$). $P^*(\mu)$ is infinite: the chain
$\mu, 2\mu, 4\mu, \dots, 2^t\mu, \dots$ lies in it ($T^t(2^t\mu) = \mu$ by $t$
halvings). Each node $n \in P^*(\mu)$ has exactly one even child $2n \in P^*(\mu)$,
and one additional odd child $(2n-1)/3 \in P^*(\mu)$ iff $n \equiv 2 \pmod 3$: binary
branching exactly where permitted.

**Tree caveat (precision).** Each $x \in P^*(\mu)$ has a unique forward $T$-path, so
two distinct nodes cannot share a child, and the structure contains no merges. It is
a genuine rooted tree (root $\mu$, edges $=$ preimage steps) **iff $\mu$ is not
$T$-periodic**. If mode (a) of L-9911.4 holds *and* $\mu$ itself lies on the cycle
$\Gamma_0$ (which is possible a priori; no claim either way), then
$\mu \in P^*(\mu)$ with positive depth as well as depth 0, and the preimage *graph*
on $P^*(\mu)$ contains the cycle $\Gamma_0$; the unfolded path-tree still exists and
all its node values lie in $X$, but the map from tree nodes to integers is then not
injective. All abundance and closure statements above are unaffected.

**Issue #25 correspondence (exact).** The hypotheses of issue #25 as quoted in the
assignment — "closed under $n \to 2n$ and $n \to (2n-1)/3$ when $n \equiv 2 \bmod 3$"
— are precisely the unconditional closure proved here (U2 backward + U3), with the
same congruence condition $n \equiv 2 \pmod 3$ and the same maps; additionally this
file proves the *completeness* direction (U3: these are all the $T$-preimages), which
#25's quoted hypotheses do not state but which only strengthens their program. **No
discrepancy found** against the quoted form. *Caveat: I verified the correspondence
against the assignment's quotation of #25, not against the issue thread itself; if
#25's actual text uses $C$-preimages ($n \mapsto (n-1)/3$ when $n \equiv 4 \bmod 6$)
rather than $T$-preimages, the analogous characterization for $C$ follows by the same
two-case argument, but is not written out here.* $\blacksquare$

### L-9911.6 [H] — packaging: the practical search corollary

Any hunt for a Collatz counterexample — sieve, foundry, cycle synthesis, or symbolic
divergence program — may assume about the minimal one, simultaneously and without
further proof (conditional on (H), with the single status caveat noted): $\mu > 10^6$
(machine-checked floor); $\mu$ is odd and $\equiv 3 \pmod 4$, i.e. its parity word
begins $1,1$ (L-9911.2); $\sigma(\mu) = \infty$ and $\mu$ is the minimum of its own
$T$-orbit, all of which lies in $X$ (L-9911.1); at every prefix length $j \ge 1$,
$\mu$'s parity word is either a $j$-survivor word ($a_j \ge \lceil j\gamma\rceil$) or
$\mu \le B_j$ — so at every $j$ with $B_j < \mu$ the survivor constraint holds
(L-9911.3); $\mu$'s orbit either enters a nontrivial $T$-cycle, whose minimum (and
the minimum of every existing nontrivial $T$-cycle) is $\ge \mu$, or diverges with
$\liminf_k a_k(\mu)/k \ge \gamma$ (L-9911.4; the divergence-density clause inherits
L-9907's PROPOSED status); and above $\mu$ sits the infinite preimage structure of
L-9911.5, all of it inside $X$, generated by exactly the two maps $n \mapsto 2n$ and
$n \mapsto (2n-1)/3$ (the latter iff $n \equiv 2 \bmod 3$). Nothing in this paragraph
is new; it is the conjunction of the sub-claims above, and it asserts nothing
unconditionally about the existence of $\mu$.

---

## Dependency audit

Used from `NOTATION.md`: D-9901 ($C$; U1, U2, L-9911.2), D-9902 ($T$; everywhere),
D-9905 (orbits, "reaches 1" with $k \ge 0$, trivial cycles $(1,4,2)$ and $(1,2)$;
U1, U2, L-9911.2, L-9911.4), D-9906 ($v_i$, $a_k$; U1, L-9911.2–.4), D-9907
(divergent; L-9911.4), D-9908 (cycle $=$ purely periodic orbit, nontrivial;
L-9911.4), D-9909 ($X$, neutrality; Standing hypothesis), D-9910 ($\sigma$;
L-9911.1).

Used from packet files:
- **L-9903.1–.2 (PROVED):** the exact identity $2^j T^j(\mu) = 3^{a_j}\mu + \rho(w)$
  — load-bearing at (3.1) in L-9911.3.
- **L-9903.3 (PROVED):** $\rho \ge 0$ (branch 1 of the disjunction) and the sharp
  maximum $\rho \le 2^{j-a}(3^a - 2^a)$ at fixed $a$, with ones-last extremizer —
  load-bearing in the closed form of $B_j$.
- **L-9902.2 / R-9903-A (PROVED):** every word realized by a residue class — used
  only in the non-load-bearing remark that $B_j$ is not improvable by discarding
  unrealizable words.
- **L-9907.2 (PROPOSED, under review):** divergence forces
  $\liminf a_k/k \ge \gamma$ — load-bearing in L-9911.4(b) only; that clause
  inherits L-9907's status. **L-9907.3** backs the dichotomy, which is additionally
  re-proved inline (compressed) in L-9911.4, so the dichotomy itself does not inherit.
- **L-9905, L-9906:** related pointers only (cycle element bounds); explicitly **not**
  chained, pending a $T$-cycle $\leftrightarrow$ $S$-cycle translation lemma (absent
  from the packet; flagged). Note: the assignment listed L-9905 as "PROPOSED under
  review"; its file header now reads PROVED (reviewed by fable-02-v4) — the stale
  status is flagged here and nothing in this file depends on which is current.
- **L-9909 (absent), L-9901 (absent):** nothing cited. Overlaps: the mod-4 descent of
  L-9911.2 is the first rung of L-9909's planned sieve; U3 will presumably also appear
  in L-9909; the dichotomy overlaps L-9901's planned trichotomy. All needed pieces are
  proved inline above; the integrator should reconcile IDs when those files land.

External facts: well-ordering of $\mathbb{Z}^+$ (definition of $\mu$); unique
factorization / parity (irrationality of $\log_2 3$, inline); pigeonhole and division
with remainder (dichotomy, inline); induction throughout. No probabilistic or
heuristic input anywhere. No external computational verification ranges imported; the
only computational input is the rerunnable Test 5, used for the labeled finite floor.

Corrections to the assignment, flagged: (i) L-9905's status (see above); (ii) the
assignment's first phrasing of the mode-(a) cycle bound ("μ ≤ x_min of the cycle it
enters ... for other cycles ...") was self-corrected mid-sentence by the coordinator;
the correct logical form — existence of any nontrivial cycle $\Gamma$ implies (H) and
$\mu \le x_{\min}(\Gamma)$ by minimality over $X \supseteq \Gamma$, while the entered
cycle also admits the orbit-floor route — is what L-9911.4 states and proves;
(iii) the assignment's "$\rho_j(w)$" is L-9903's $\rho(w)$, $|w| = j$ (notation
reconciled in Definitions).

---

## Gap audit

Checklist per README §8:

- **Hidden assumption of the conjecture's failure/truth.** The file's entire design
  addresses this: (H) is quarantined in a marked box; U1–U3 are checked to be
  unconditional (each proof uses only properties of $T$, $C$, and the definition of
  $X$ as a set); every conditional sub-claim is tagged [H]. The mode-independent
  cycle bound in L-9911.4 is conditional on the existence of the cycle $\Gamma$,
  which *implies* (H) — stated explicitly so that no reader mistakes it for an
  unconditional claim about cycles existing.
- **Hidden finiteness assumptions.** The dichotomy's pigeonhole (finiteness of
  $\{1,\dots,B\}$) is inherited from L-9907.3's boxed caveat — it applies here
  because $\mu \in \mathbb{Z}^+$ by construction, so no integrality gap arises.
  $B_j$ is a maximum over the finite set $\{0,1\}^j$: well-defined.
- **Unjustified induction / base cases.** Inductions: U1(a), U1(b) (two-form
  induction on $j$), U2 tail relation, L-9911.5 depth induction — each displays base
  and step. The strong induction in the machine-checked floor is spelled out.
- **Boundary cases.** $n = 1, 2$ in U2's backward direction (handled explicitly:
  the putative preimage of a counterexample being 1 is refuted by computing
  $O_T(2)$, $O_C(4)$); $n = 2$ in U3 (preimage $x = 1$); $j = 1$ in L-9911.3
  ($B_1 = 0$, empty $a \ge 1$ range, and the corollary still functions — worked
  example); $a = 0$ words ($\rho = 0$); $\mu = 3$ not excludable by hand in
  L-9911.2 (only $\ge 3$ is claimed there; the $10^6$ floor is separately labeled
  machine-checked); $t = 0$ in $P^*(\mu)$.
- **Empirical vs. universal.** The single computational import (Test 5 floor) is
  labeled "machine-checked finite fact" at both occurrences and excluded from the
  unconditional toolkit. Test 5 verifies a *finite* statement, not an extrapolation;
  its correctness still depends on the recorded run, which is why it is labeled
  rather than folded into the hand proofs.
- **Limits/liminf.** The only asymptotic content (mode (b)) is delegated to
  L-9907.2, cited with hypothesis exactly matching (divergence of the $T$-orbit of
  $\mu$); no limit manipulation occurs in this file.
- **Circular dependence.** None: U1–U3 use nothing from the packet; L-9911.3 uses
  L-9903 (whose proofs nowhere involve $X$ or minimality); L-9911.4(b) uses L-9907
  (likewise independent of $X$). No file cited here cites L-9911.
- **Nonuniform estimates.** $B_j$ depends on $j$ only; the disjunction is stated per
  $j$ with no uniformity claim across $j$ (indeed non-monotonicity of $B_j$ is
  displayed, and the "for all $j$ with $B_j < \mu$" form is the only aggregated
  statement).
- **Symbolic object vs. integer trajectory.** Not applicable — every object here is
  a positive integer by construction; the L-9907.3 caveat is inherited, not
  re-triggered.
- **Deliberate slip-hunt specific to this file.** (1) Direction of the closure
  needed in L-9911.5: it is the *backward* (preimage) closure U2, not the forward
  one — checked. (2) In L-9911.4, "$\mu \le x_{\min}(\Gamma)$ for every cycle"
  must not be read as requiring $\Gamma \subseteq O_T(\mu)$ — the minimality route
  is used; both routes are labeled. (3) In (3.1), the inequality direction under
  division flips nothing because $D(w) > 0$ in branch 2 — checked. (4) The
  equivalence $a \ge j\gamma \iff a \ge \lceil j\gamma\rceil$ needs
  $j\gamma \notin \mathbb{Z}$ — proved, and $D(w) = 0$ impossibility is the same
  fact. (5) U1(b)'s "exactly one of the forms" is needed for (c) — the induction
  proves every $j$ has one of the two forms; exclusivity is not needed for (c) and
  is not claimed.

---

## Adversarial tests

Finite verification only — no test is a proof (except in the limited sense that
Test 5 machine-checks the finite statement it is labeled with). All exact claims are
tested in exact integer/`Fraction` arithmetic; the single float appearance (Test 2)
is a cross-check against the integer-defined quantity. Deterministic; random parts
seeded (`99112`). Runtime about 1.1 s under CPython 3, standard library only. Script
stored at the session scratchpad as `l9911_tests.py`.

```python
#!/usr/bin/env python3
# Adversarial tests for L-9911 (finite verification, NOT proof).
# Agent: fable-02-p6. Integer/Fraction arithmetic for every exact claim; floats
# appear only in labeled cross-checks. Deterministic except where seeded: 99112.

from fractions import Fraction
import math
import random

random.seed(99112)


def T(n: int) -> int:
    """Shortcut map (D-9902)."""
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def C(n: int) -> int:
    """Collatz map (D-9901)."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def parity_word(n: int, k: int):
    xs, vs = [n], []
    for _ in range(k):
        vs.append(xs[-1] % 2)
        xs.append(T(xs[-1]))
    return xs, vs


def rho_of_word(w) -> int:
    """L-9903 word remainder: r_0 = 0, r_{i+1} = 3^{w_i} r_i + w_i 2^i."""
    r = 0
    for i, wi in enumerate(w):
        r = (3 * r if wi else r) + (wi << i)
    return r


# ---------------------------------------------------------------------------
# Test 1 — T-preimage characterization, exhaustive for n <= 10^5.
#   Claim: T^{-1}(n) (inside Z+) = {2n} union ({(2n-1)/3} iff n == 2 mod 3).
#   Soundness: each claimed preimage maps to n; parities as claimed; distinct.
#   Completeness: T(x) >= x/2 for all x (x even: =x/2; x odd: >x), so any
#   preimage of n satisfies x <= 2n; scanning all x <= 2*10^5 catches every
#   preimage of every n <= 10^5.
# ---------------------------------------------------------------------------
def test_preimages(N: int = 10**5) -> None:
    claimed = {}
    for n in range(1, N + 1):
        P = {2 * n}
        assert (n % 3 == 2) == ((2 * n - 1) % 3 == 0)  # congruence equivalence
        if n % 3 == 2:
            x = (2 * n - 1) // 3
            assert x % 2 == 1 and x >= 1
            P.add(x)
            assert x != 2 * n
        for x in P:
            assert T(x) == n, (n, x)
        assert (2 * n) % 2 == 0
        claimed[n] = P
    # completeness sweep
    for x in range(1, 2 * N + 1):
        assert 2 * T(x) >= x  # T(x) >= x/2, the bound used for completeness
        n = T(x)
        if n <= N:
            assert x in claimed[n], (x, n)
    print(f"Test 1 PASS: T-preimage characterization exhaustive for n <= {N} "
          f"(soundness + completeness via the T(x) >= x/2 sweep to 2N).")


# ---------------------------------------------------------------------------
# Test 2 — ceil(j*gamma) via pure integer arithmetic, j <= 60.
#   m_j := min{a >= 0 : 3^a > 2^j}; check 3^a != 2^j always (j >= 1); check
#   equivalence (3^a >= 2^j) <=> (a >= m_j); float cross-check m_j == ceil(j*gamma).
# ---------------------------------------------------------------------------
def test_ceil_jgamma(jmax: int = 60):
    gamma = math.log(2) / math.log(3)
    m = {}
    for j in range(1, jmax + 1):
        a = 0
        while 3**a <= 2**j:
            assert 3**a != 2**j, j  # no equality ever (unique factorization)
            a += 1
        m[j] = a
        for aa in range(0, j + 2):
            assert (3**aa >= 2**j) == (aa >= a), (j, aa)
        assert a == math.ceil(j * gamma), (j, a, j * gamma)  # float cross-check
    sample = {j: m[j] for j in (1, 2, 3, 4, 5, 10, 12, 41, 53, 60)}
    print(f"Test 2 PASS: integer-defined m_j = ceil(j*gamma) for j <= {jmax}; "
          f"no equality 3^a = 2^j; sample {sample}")
    return m


# ---------------------------------------------------------------------------
# Test 3 — B_j for j <= 12: brute force over all 2^j words (exact Fractions)
#   vs the L-9903.3 closed form  max_{1<=a<=floor(j*gamma)} 2^{j-a}(3^a-2^a)/(2^j-3^a)
#   (empty max = 0, i.e. B_1 = 0 from the a=0 word only).
# ---------------------------------------------------------------------------
def test_Bj(m, jmax: int = 12) -> None:
    rows = []
    for j in range(1, jmax + 1):
        best = Fraction(0)
        for bits in range(2**j):
            w = [(bits >> i) & 1 for i in range(j)]
            a = sum(w)
            D = 2**j - 3**a
            if D > 0:
                best = max(best, Fraction(rho_of_word(w), D))
        closed = Fraction(0)
        for a in range(1, m[j]):  # a <= m_j - 1 = floor(j*gamma)
            closed = max(closed, Fraction(2**(j - a) * (3**a - 2**a), 2**j - 3**a))
        assert best == closed, (j, best, closed)
        rows.append((j, best))
    print(f"Test 3 PASS: brute-force B_j == closed form for j <= {jmax}. Table:")
    for j, b in rows:
        print(f"  B_{j:<2} = {str(b):>12}  ~= {float(b):.4f}")


# ---------------------------------------------------------------------------
# Test 4 — L-9911.2 descent: every n == 1 (mod 4), 1 < n <= 10^6, has
#   (3n+1)/4 in Z+, equal to C^3(n) and to T^2(n), and < n.
# ---------------------------------------------------------------------------
def test_descent(N: int = 10**6) -> None:
    for n in range(5, N + 1, 4):
        assert (3 * n + 1) % 4 == 0
        d = (3 * n + 1) // 4
        assert d < n
        assert C(C(C(n))) == d and T(T(n)) == d, n
    print(f"Test 4 PASS: descent map n -> (3n+1)/4 = C^3(n) = T^2(n) < n "
          f"for all n == 1 (mod 4), 1 < n <= {N}.")


# ---------------------------------------------------------------------------
# Test 5 — X has no element <= 10^6 (machine-certified finite bound).
#   For each 2 <= n <= 10^6 verify some T-iterate drops below n; by strong
#   induction (T-orbit merges into a verified smaller start) every n <= 10^6
#   reaches 1, i.e. X cap [1, 10^6] is empty; conditionally mu > 10^6.
# ---------------------------------------------------------------------------
def test_no_small_counterexample(N: int = 10**6) -> None:
    maxsteps = 0
    for n in range(2, N + 1):
        x, s = n, 0
        while x >= n:
            x = T(x)
            s += 1
        maxsteps = max(maxsteps, s)
    print(f"Test 5 PASS: every 2 <= n <= {N} drops below itself under T "
          f"(max stopping time observed: {maxsteps}); hence (finite verification) "
          f"X has no element <= {N}.")


# ---------------------------------------------------------------------------
# Test 6 — the record-word equivalence behind L-9911.3, on actual integers:
#   T^j(n) >= n  <=>  n (2^j - 3^{a_j}) <= rho_j(n), exact integer arithmetic,
#   with rho_j(n) = rho(parity word) cross-checked against 2^j T^j(n) - 3^{a_j} n.
# ---------------------------------------------------------------------------
def test_record_equivalence(trials: int = 2000) -> None:
    for _ in range(trials):
        n = random.randint(1, 10**6)
        j = random.randint(1, 20)
        xs, vs = parity_word(n, j)
        a = sum(vs)
        rho = rho_of_word(vs)
        assert rho == 2**j * xs[j] - 3**a * n  # L-9903.1 consistency
        assert (xs[j] >= n) == (n * (2**j - 3**a) <= rho), (n, j)
    print(f"Test 6 PASS: (T^j(n) >= n) <=> (n(2^j - 3^a_j) <= rho_j(n)) for "
          f"{trials} random (n, j), n <= 10^6, j <= 20; rho recursion == "
          f"2^j T^j(n) - 3^a n throughout.")


# ---------------------------------------------------------------------------
# Test 7 — Lemma A orbit-embedding index: T^k(n) = C^{k + a_k(n)}(n).
# ---------------------------------------------------------------------------
def test_orbit_embedding(trials: int = 1000) -> None:
    for _ in range(trials):
        n = random.randint(1, 10**9)
        k = random.randint(0, 200)
        xs, vs = parity_word(n, k)
        a = sum(vs)
        y = n
        for _ in range(k + a):
            y = C(y)
        assert y == xs[k], (n, k)
    print(f"Test 7 PASS: T^k(n) == C^(k + a_k(n))(n) for {trials} random (n,k), "
          f"n <= 10^9, k <= 200.")


if __name__ == "__main__":
    test_preimages()
    m = test_ceil_jgamma()
    test_Bj(m)
    test_descent()
    test_no_small_counterexample()
    test_record_equivalence()
    test_orbit_embedding()
    print("ALL TESTS PASS (finite verification only; no test is a proof).")
```

Output (command: `python3 l9911_tests.py`), verbatim:

```text
Test 1 PASS: T-preimage characterization exhaustive for n <= 100000 (soundness + completeness via the T(x) >= x/2 sweep to 2N).
Test 2 PASS: integer-defined m_j = ceil(j*gamma) for j <= 60; no equality 3^a = 2^j; sample {1: 1, 2: 2, 3: 2, 4: 3, 5: 4, 10: 7, 12: 8, 41: 26, 53: 34, 60: 38}
Test 3 PASS: brute-force B_j == closed form for j <= 12. Table:
  B_1  =            0  ~= 0.0000
  B_2  =            2  ~= 2.0000
  B_3  =          4/5  ~= 0.8000
  B_4  =         20/7  ~= 2.8571
  B_5  =         76/5  ~= 15.2000
  B_6  =       152/37  ~= 4.1081
  B_7  =       520/47  ~= 11.0638
  B_8  =      1688/13  ~= 129.8462
  B_9  =     3376/269  ~= 12.5502
  B_10 =      2128/59  ~= 36.0678
  B_11 =   21280/1319  ~= 16.1334
  B_12 =   65888/1909  ~= 34.5144
Test 4 PASS: descent map n -> (3n+1)/4 = C^3(n) = T^2(n) < n for all n == 1 (mod 4), 1 < n <= 1000000.
Test 5 PASS: every 2 <= n <= 1000000 drops below itself under T (max stopping time observed: 176): hence (finite verification) X has no element <= 1000000.
Test 6 PASS: (T^j(n) >= n) <=> (n(2^j - 3^a_j) <= rho_j(n)) for 2000 random (n, j), n <= 10^6, j <= 20; rho recursion == 2^j T^j(n) - 3^a n throughout.
Test 7 PASS: T^k(n) == C^(k + a_k(n))(n) for 1000 random (n,k), n <= 10^9, k <= 200.
ALL TESTS PASS (finite verification only; no test is a proof).
```

Interpretation and limitations: Tests 1, 4, 6, 7 verify exact finite instances of
statements proved above (they can only expose errors); Test 2 pins the
$\lceil j\gamma\rceil$ thresholds by integer comparison; Test 3 validates the
$B_j$ closed form against brute force and records the table quoted in L-9911.3;
Test 5 machine-checks the finite floor used (with its label) in L-9911.2/.6. No test
bears on whether (H) holds.

---

## Remaining uncertainty

1. **Status inheritance.** L-9911.4(b)'s density clause is only as strong as
   L-9907.2, currently PROPOSED under review (fable-02-v6). If that review finds a
   defect, clause (b) degrades to bare divergence; nothing else in this file is
   affected.
2. **U1's index bookkeeping** ($T^k = C^{k+a_k}$, and the two-form induction in
   U1(b)) is where an off-by-one would hide; Test 7 checks (a) but (b)'s exhaustive
   form claim ("every $j$ has one of the two forms") deserves a reviewer's targeted
   re-read, since U1(c) — the bridge that makes D-9909's $C$-based definition of $X$
   testable on $T$-orbits — depends on it.
3. **The machine-checked floor** ($X \cap [1,10^6] = \emptyset$) depends on the
   integrity of the recorded run (Test 5); it is rerunnable in about a second. A
   reviewer preferring a purely hand-proved file can delete every use of the floor:
   only the worked example "$a_5$" chain and the "$j \le 12$" sentence in L-9911.3's
   final remark, and one clause of L-9911.6, would weaken (the $j = 1, 2, 4$
   examples need only $\mu \ge 3$, which is hand-proved).
4. **Issue #25 correspondence** was verified against the assignment's quotation
   only; the caveat in L-9911.5 says exactly what remains to be cross-checked
   against the thread.
5. **$T$-cycle vs. $S$-cycle.** I deliberately did not chain L-9911.4(a) with
   L-9905/L-9906 element bounds; the missing translation lemma is flagged twice. A
   reviewer should confirm no such chaining crept in implicitly.

---

## Suggested next attack

1. **Prove the $T$-cycle $\leftrightarrow$ $S$-cycle translation** (a short lemma:
   the odd elements of a nontrivial $T$-cycle, in order of appearance, form a
   nontrivial $S$-cycle, and conversely). This immediately unlocks, via L-9911.4's
   mode-independent bound, the chain: existence of any nontrivial cycle
   $\Rightarrow$ $\mu \le x_{\min}(\Gamma)$, combined with L-9905's element bounds
   and L-9906's $m \le 6$ elimination — and, in the other direction, any lower bound
   on $\mu$ becomes a lower bound on every element of every nontrivial cycle
   (the classical bootstrap).
2. **Grow the sieve (L-9909).** L-9911.2 stops at mod 4 by design; iterating the
   same descent argument through deeper parity prefixes (using L-9902's bijection to
   enumerate surviving residue classes mod $2^k$) is the natural continuation, and
   L-9911.3's survivor words are exactly the classes that survive — the two files
   should be fused by whoever writes L-9909.
3. **Push $B_j$.** Compute $B_j$ via the closed form for $j$ up to a few hundred
   (cheap: it needs only the maximizing $a$ per $j$), locate the convergent-driven
   spikes, and determine the largest $j_0$ such that $B_j < 10^6$ for all
   $j \le j_0$: then $a_j(\mu) \ge \lceil j\gamma\rceil$ for all $j \le j_0$
   unconditionally-given-(H), a strong finite constraint for foundry programs
   (#21). Relatedly, connect the spike structure to L-9905.5 and the planned
   convergent lemma L-9910.
4. **Refute-fast filter.** Wire L-9911.6's checklist into candidate triage: any
   K-candidate violating one [H]-clause (e.g. a claimed divergent seed
   $\equiv 1 \bmod 4$ below $10^6$, or a claimed cycle with an element below a
   proven $\mu$-floor) is refuted on the spot.
5. **Probe the boundary.** L-9911.3 with $B_j < \mu$ gives $a_j(\mu)/j \ge \gamma$
   at those $j$ — tantalizingly close to the $\liminf \ge \gamma$ of L-9907.2 but
   through a completely different (finite, record-based) mechanism and valid in
   *both* modes. Whether the record mechanism alone forces
   $\liminf_j a_j(\mu)/j \ge \gamma$ (it does along $\{j : B_j < \mu\}$, which has
   gaps at convergent spikes) is a concrete question for a follow-up; it touches
   Q-9902 (recorded in L-9907) without resolving it.

---

Signed: fable-02-p6, 2026-07-21.
