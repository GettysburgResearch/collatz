# L-9908 — Terras stopping-time density: survivor sieve, entropy bound, density theorem

```text
Claim ID: L-9908
Title: The survivor constraint mod 2^k, the binomial entropy tail bound, and the
       Terras density theorem: d({n : sigma(n) > k}) = s_k 2^{-k} <= 2^{-k(1-H(gamma))},
       with certified 1 - H(gamma) > 0.049; corollary d({sigma = infinity}) = 0
Status: PROVED
Authoring agent: fable-02-p2
Reviewing agents: fable-02-v12 (adversarial review 2026-07-25: PASS)
Created: 2026-07-21
Last updated: 2026-07-25 (status upgraded after independent adversarial review by
              fable-02-v12; see the Verification note appended at the end of the file)
Dependencies: NOTATION.md (D-9902, D-9906, D-9910, gamma, nu_2, conventions);
              L-9902 (PROVED) — parity-word/residue bijection (used as F4);
              L-9903 (PROVED) — iteration formula and remainder bounds (used as F1-F3);
              statements used are restated in full below.
              Cross-referenced, NOT load-bearing: L-9909 (PROPOSED, under review;
              overlapping survivor-sieve machinery, independent derivation),
              L-9911 (PROPOSED; minimal-counterexample structure), L-9907 (PROVED;
              divergence-density threshold, complementary direction).
Scope: All n in Z^+ and all k >= 1; unconditional (no hypothesis on the truth of
       the Collatz conjecture). Classical result (Terras 1976, Everett 1977),
       reconstructed independently and in full.
Related counterexample candidates: none
```

---

## Statement

Throughout, $T$ is the shortcut map (D-9902), $v_i(n) = T^i(n) \bmod 2$ and
$a_j(n) = \sum_{i<j} v_i(n)$ (D-9906), $\sigma(n) = \inf\{k \ge 1 : T^k(n) < n\}
\in \mathbb{Z}^+ \cup \{\infty\}$ (D-9910), and $\gamma = \log_3 2 = \ln 2/\ln 3$
(NOTATION.md). $H$ is the binary entropy, $\rho(w)$ the word remainder of L-9903, and
the terms *survivor word*, $s_k$, $U_k$, $B_k$, $E_k$, $\bar d$, $d$ are defined in the
Definitions section. $\lceil x \rceil$ is the least integer $\ge x$.

**L-9908.1 (survivor constraint; two-sided sieve).** For every $n \in \mathbb{Z}^+$ and
every integer $k \ge 1$:

*(a)* $\sigma(n) > k \iff T^j(n) \ge n$ for all $1 \le j \le k$.

*(b)* If $\sigma(n) > k$, then for **each** $j$ with $1 \le j \le k$, at least one of the
following holds:
$$\text{(i) } 3^{a_j(n)} \ge 2^j, \qquad\text{or}\qquad
\text{(ii) } 3^{a_j(n)} < 2^j \ \text{ and } \ n \le \frac{\rho_j(n)}{2^j - 3^{a_j(n)}}.$$

*(c)* For all integers $a \ge 0$, $j \ge 1$:
$3^a \ge 2^j \iff a \ge \lceil j\gamma \rceil$. Moreover $\gamma$ is irrational, so
$j\gamma \notin \mathbb{Z}$ and $3^a = 2^j$ is impossible for $j \ge 1$; hence also
$3^a \ge 2^j \iff 3^a > 2^j \iff a > j\gamma$.

*(d)* With $U_k$ the union of the positive parts of the $s_k$ survivor residue classes
mod $2^k$ and $E_k := \{n \in \mathbb{Z}^+ : \sigma(n) > k\} \setminus U_k$:
$$U_k \ \subseteq\ \{n \in \mathbb{Z}^+ : \sigma(n) > k\} \ \subseteq\ U_k \cup E_k,
\qquad E_k \subseteq [1, B_k] \cap \mathbb{Z}^+,$$
so $\#E_k \le \lfloor B_k \rfloor < \infty$. (On $U_k$ the containment is strict
stepwise: every $n \in U_k$ has $T^j(n) > n$ for $1 \le j \le k$.) Moreover $B_k$ has
the closed form
$$B_k = \max\Big\{ \tfrac{2^{\,j-a}(3^a - 2^a)}{2^j - 3^a} \;:\; 1 \le j \le k,\
0 \le a \le j,\ 3^a < 2^j \Big\},$$
and $B_k \le B_{k+1}$. (The first containment — survivor classes survive *uniformly* —
goes beyond the assigned one-sided statement; it is what upgrades the density upper
bound of L-9908.3 to an exact density.)

**L-9908.2 (entropy tail bound; survivor-count bound).**

*(a)* For every integer $k \ge 1$ and every real $t$ with $1/2 < t < 1$:
$$\sum_{\substack{j \in \mathbb{Z} \\ tk \le j \le k}} \binom{k}{j} \ \le\ 2^{\,k H(t)},
\qquad H(t) := -t\log_2 t - (1-t)\log_2(1-t).$$

*(b)* $H$ is strictly decreasing on $[1/2, 1)$: if $1/2 \le t_1 < t_2 < 1$ then
$H(t_1) > H(t_2)$. (Indeed $H'(t) = \log_2\frac{1-t}{t} < 0$ on $(1/2,1)$.)

*(c)* $\gamma \in (1/2, 1)$, and for every $k \ge 1$:
$$s_k \ \le\ \#\{w \in \{0,1\}^k : a_k(w) \ge \lceil k\gamma\rceil\}
\ =\ \sum_{a = \lceil k\gamma\rceil}^{k} \binom{k}{a} \ \le\ 2^{\,k H(\gamma)}.$$

**L-9908.3 (density theorem).** For every integer $k \ge 1$, the natural density of
$\{n \in \mathbb{Z}^+ : \sigma(n) > k\}$ **exists** and equals
$$d\big(\{\sigma > k\}\big) \;=\; \frac{s_k}{2^k} \;\le\; 2^{-k(1 - H(\gamma))} .$$
In particular the upper natural density is $\le 2^{-k(1-H(\gamma))}$, as assigned.
Certified numeric bound:
$$1 - H(\gamma) \;>\; \frac{1937}{38800} \;>\; 0.0499 \;>\; 0.049,$$
so $d(\{\sigma > k\}) < 2^{-0.0499\,k}$ for every $k \ge 1$.

**Corollary.** $\{n \in \mathbb{Z}^+ : \sigma(n) = \infty\}$ has natural density $0$;
equivalently, $\{n \in \mathbb{Z}^+ : T^j(n) < n \text{ for some } j \ge 1\}$ has natural
density $1$. The density-$0$ set is **not empty**: $\sigma(1) = \infty$.

**L-9908.4 (honest scope; and per-$c$ descent).**

*(a)* Scope limitation (proved discussion, boxed in the Proof section): the corollary
does **not** bound the counterexample set, and says nothing about any individual orbit.

*(b)* For **every** fixed $c \in (0,1)$: the set
$A_c := \{n \in \mathbb{Z}^+ : T^j(n) \ge c\,n \text{ for all } j \ge 1\}$ has natural
density $0$; equivalently $D_c := \{n : \exists j \ge 1,\ T^j(n) < c\,n\}$ has natural
density $1$. (The exceptional set depends on $c$; no claim is made about
$\bigcap_{c} D_c$ — see the quantifier warning in the proof.)

---

## Definitions

- **Densities.** For $A \subseteq \mathbb{Z}^+$ and $N \ge 1$ let
  $A(N) := \#(A \cap [1,N])$. Upper density $\bar d(A) := \limsup_{N\to\infty} A(N)/N$,
  lower density $\underline d(A) := \liminf_{N\to\infty} A(N)/N$; the **natural density**
  $d(A)$ exists and equals their common value when $\bar d(A) = \underline d(A)$.
- **Binary entropy.** $H : [0,1] \to \mathbb{R}$, $H(t) = -t\log_2 t - (1-t)\log_2(1-t)$
  for $t \in (0,1)$, $H(0) = H(1) = 0$. All logarithms $\log_2$; $H(1/2) = 1$.
- **Word quantities (restated from L-9903, PROVED).** For $w = (w_0,\dots,w_{j-1}) \in
  \{0,1\}^j$: $a_i(w) := \sum_{\ell < i} w_\ell$ for $0 \le i \le j$ (so $a_0(w) = 0$,
  empty sum), and the **word remainder** $\rho(w) := r_j$ where $r_0 := 0$,
  $r_{i+1} := 3^{w_i} r_i + w_i 2^{i}$. For $n \in \mathbb{Z}^+$, $\rho_j(n)$ denotes the
  same recursion run on $(v_0(n), \dots, v_{j-1}(n))$; L-9903.2 shows
  $\rho_j(n) = \rho(w)$ for $w$ the length-$j$ parity word of $n$.
- **Survivor word.** $w \in \{0,1\}^k$ is a **survivor word** (of length $k$) if
  $$a_j(w) \ \ge\ \lceil j\gamma \rceil \qquad \text{for every } j = 1, \dots, k.$$
  $s_k := \#\{\text{survivor words of length } k\}$.
- **Survivor classes; $U_k$.** By F4 below (L-9902), each $w \in \{0,1\}^k$ is realized
  by exactly one residue class mod $2^k$, and distinct words by distinct classes.
  $U_k := \{ n \in \mathbb{Z}^+ :$ the length-$k$ parity word of $n$ is a survivor
  word$\}$ — equivalently, the union of the positive parts of the $s_k$ pairwise
  disjoint survivor classes mod $2^k$.
- **Exceptional constant and set.**
  $$B_k := \max\Big\{ \frac{\rho(w)}{2^{\,j} - 3^{\,|w|_1}} \;:\; 1 \le j \le k,\;
  w \in \{0,1\}^j,\; 3^{\,|w|_1} < 2^{\,j} \Big\}, \qquad
  E_k := \{n \in \mathbb{Z}^+ : \sigma(n) > k\} \setminus U_k,$$
  where $|w|_1 = a_j(w)$ is the number of ones of $w \in \{0,1\}^j$. The max is over a
  finite nonempty set (the pair $j = 1$, $w = (0)$ always qualifies: $3^0 = 1 < 2$,
  ratio $0$), so $B_k \ge 0$ is a well-defined rational.
- $A_c, D_c$ as in L-9908.4(b). $\lceil x\rceil$ = least integer $\ge x$; for
  $a \in \mathbb{Z}$ and $x \in \mathbb{R}$: $a \ge x \iff a \ge \lceil x \rceil$
  (used repeatedly; immediate from the definition of $\lceil\cdot\rceil$).

---

## Motivation

This file proves the exponential survivor-density decay that L-9909 forward-promises:
L-9909.3/L-9909.4 (PROPOSED, under review) set up the same uniform-descent sieve and
compute it exactly for $k \le 8$, and explicitly defer the $k \to \infty$ density
statement; L-9908.2–.3 supply exactly that, from an independent derivation (the two
files' finite outputs cross-validate: survivor counts $1,1,2,3,4,8,13,19$ for
$k \le 8$, $B_2 = 2$, $1 \in E_2$ agree).

Relations to the counterexample program:

- **Baseline for every search/divergence direction** (issues #8, #4, #25 context):
  "typical orbits stop" is now a theorem with an explicit rate, so any candidate
  divergent orbit or any density-based divergence mechanism must live inside an
  explicitly exponentially thin set: for each $k$, inside one of $s_k \le 2^{kH(\gamma)}$
  residue classes mod $2^k$ or below the explicit constant $B_k$. Search programs can
  and should target survivor classes (L-9909.4 lists them for $k \le 8$).
- **Where the minimal counterexample must live.** Combined with L-9909.2(M)(iii) /
  L-9911.1 (both PROPOSED — the minimal counterexample $\mu$, if any, has
  $\sigma(\mu) = \infty$), the corollary confines $\mu$ to a density-$0$ set with
  explicit per-$k$ localization. This file does **not** depend on those claims.
- **Anti-confabulation notice, stated up front:** everything here is a statement about
  *densities of sets of starting points*. It says **nothing** about any individual
  orbit, and nothing about the counterexample set having density $0$ (see the boxed
  remark in L-9908.4(a)). The corollary's density-$0$ set is provably nonempty
  ($\sigma(1) = \infty$), which is a standing warning against reading "density $0$"
  as "empty".

---

## Proof

### P0 — preliminaries

*(P0.1) $T$ maps $\mathbb{Z}^+$ to $\mathbb{Z}^+$.* If $n$ is even then $T(n) = n/2 \in
\mathbb{Z}^+$; if $n$ is odd then $3n+1$ is even and $T(n) = (3n+1)/2 \ge 2$. By
induction, $T^j(n) \in \mathbb{Z}^+$ for all $j \ge 0$; so all quantities below are
defined. (This restates P0 of L-9902.)

*(P0.2) Proof of L-9908.1(a).* By D-9910, $\sigma(n) = \inf S_n$ with
$S_n := \{j \ge 1 : T^j(n) < n\}$ and $\inf \emptyset = \infty$. Then
$\sigma(n) > k$ $\iff$ $S_n$ contains no element of $\{1,\dots,k\}$ $\iff$
$T^j(n) \ge n$ for all $1 \le j \le k$. (If $S_n = \emptyset$, $\sigma(n) = \infty > k$
and the right side holds vacuously-fully; if $S_n \ne \emptyset$, $\inf S_n = \min S_n$
since $S_n \subseteq \mathbb{Z}^+$.) $\square$

*(P0.3) $\sigma(1) = \infty$.* $T(1) = 2$, $T(2) = 1$; by induction $T^j(1) \in \{1,2\}$
for all $j \ge 0$, so $T^j(1) < 1$ never holds; $S_1 = \emptyset$. $\square$

### Imported facts (restated in full; sources are PROVED files)

- **F1 (iteration formula; L-9903.1).** For all $n \in \mathbb{Z}^+$, $j \ge 0$:
  $2^{\,j}\, T^{\,j}(n) = 3^{\,a_j(n)}\, n + \rho_j(n)$, an identity between positive
  integers, with $\rho_j(n)$ the recursion value of the Definitions.
- **F2 (word dependence; L-9903.2).** $\rho_j(n) = \rho(w)$ where
  $w = (v_0(n), \dots, v_{j-1}(n))$; i.e. $\rho_j(n)$ depends only on the length-$j$
  parity word of $n$, hence (with F4) only on $n \bmod 2^{\,j}$.
- **F3 (remainder bounds; L-9903.3).** For $w \in \{0,1\}^j$ with $a := |w|_1$:
  $\rho(w) \ge 0$, with $\rho(w) = 0 \iff a = 0$, and
  $\rho(w) \le 2^{\,j-a}(3^a - 2^a)$, attained exactly at $w = 0^{\,j-a}1^{a}$.
  *(Robustness note: the core arguments below need only $\rho \ge 0$, which also has a
  one-line inline proof — every step of the recursion $r_{i+1} = 3^{w_i} r_i + w_i 2^i$
  preserves nonnegativity by induction from $r_0 = 0$. The sharp upper bound is used
  only for the closed form of $B_k$.)*
- **F4 (parity-word bijection; L-9902.1(c), L-9902.2, L-9902.3(i)).** For each
  $k \ge 1$: the length-$k$ parity word of $n \in \mathbb{Z}^+$ depends only on
  $n \bmod 2^k$; the induced map $\pi_k : \mathbb{Z}/2^k\mathbb{Z} \to \{0,1\}^k$ is a
  bijection; each word $w$ is realized by exactly one class, whose positive members are
  $n_w + 2^k t$ ($t \ge 0$, $n_w \in \{1,\dots,2^k\}$). In particular distinct words are
  realized by disjoint classes.

### Proof of L-9908.1(b) (the dichotomy)

Let $\sigma(n) > k$ and fix $j \in \{1, \dots, k\}$. By (a), $T^{\,j}(n) \ge n$.
Multiplying by $2^{\,j} > 0$ and substituting F1:
$$3^{\,a_j(n)}\, n + \rho_j(n) \;=\; 2^{\,j}\, T^{\,j}(n) \;\ge\; 2^{\,j} n,
\qquad\text{i.e.}\qquad \rho_j(n) \;\ge\; n\,\big(2^{\,j} - 3^{\,a_j(n)}\big). \tag{$*$}$$
If $3^{a_j(n)} \ge 2^{\,j}$, branch (i) holds. Otherwise $2^{\,j} - 3^{a_j(n)} \ge 1 > 0$
and dividing $(*)$ by it gives branch (ii). $\square$

*(Degenerate instance, noted for honesty: if $a_j(n) = 0$ then $\rho_j(n) = 0$ (F3) and
(ii) would force $n \le 0$, impossible — consistently, $a_1(n) = 0$ means $n$ even,
$T(n) = n/2 < n$, so such $n$ never has $\sigma(n) > k$ in the first place. The
implication as stated is true in all cases.)*

### Proof of L-9908.1(c) (ceiling form; irrationality of $\gamma$)

Since $\ln$ is strictly increasing and $\ln 3 > 0$:
$3^a \ge 2^{\,j} \iff a \ln 3 \ge j \ln 2 \iff a \ge j\,\frac{\ln 2}{\ln 3} = j\gamma$.
As $a$ is an integer, $a \ge j\gamma \iff a \ge \lceil j\gamma \rceil$ (Definitions,
last bullet). This proves the first equivalence.

*Irrationality.* Suppose $\gamma = p/q$ with $p, q \in \mathbb{Z}^+$ (note
$\gamma > 0$). Then $q \ln 2 = p \ln 3$, so $2^{\,q} = 3^{\,p}$. But $2^{\,q}$ is even
($q \ge 1$) and $3^{\,p}$ is odd (a product of odd factors) — contradiction (this is the
one-line unique-factorization/parity argument). Hence $\gamma \notin \mathbb{Q}$.
Consequently, for $j \ge 1$: $j\gamma \notin \mathbb{Z}$ (otherwise $\gamma =
(j\gamma)/j \in \mathbb{Q}$), so $\lceil j\gamma\rceil > j\gamma$; and $3^a = 2^{\,j}$ is
impossible (evenness of the right side vs. oddness of the left, for any $a \ge 0$,
$j \ge 1$). Therefore $3^a \ge 2^{\,j} \iff 3^a > 2^{\,j}$, and
$a \ge \lceil j\gamma\rceil \iff a > j\gamma$. $\square$

### Proof of L-9908.1(d) (two-sided sieve; finiteness of $E_k$)

**Forward containment $U_k \subseteq \{\sigma > k\}$, with strict stepwise growth.**
Let $n \in U_k$, i.e. the length-$k$ parity word $w$ of $n$ is a survivor word. For each
$1 \le j \le k$: $a_j(n) = a_j(w) \ge \lceil j\gamma\rceil$, so
$3^{a_j(n)} > 2^{\,j}$ by (c). By F1 and $\rho_j(n) \ge 0$ (F3):
$$2^{\,j}\,T^{\,j}(n) \;=\; 3^{a_j(n)} n + \rho_j(n) \;>\; 2^{\,j} n,$$
hence $T^{\,j}(n) > n$; in particular $T^{\,j}(n) \ge n$ for all $j \le k$, so
$\sigma(n) > k$ by (a). *(This matches L-9909.3(a)'s independent "uniform strict
descent-failure" statement.)*

**Backward containment and the bound on $E_k$.** Let $n \in E_k$: $\sigma(n) > k$ and
$n \notin U_k$, i.e. $n$'s word $w$ is **not** a survivor word. Then there exists
$j \in \{1, \dots, k\}$ with $a_j(n) < \lceil j\gamma\rceil$, equivalently (by (c))
$3^{a_j(n)} < 2^{\,j}$. By (b), branch (ii) must hold at this $j$:
$$n \;\le\; \frac{\rho_j(n)}{2^{\,j} - 3^{\,a_j(n)}} .$$
By F2, $\rho_j(n) = \rho(w^{(j)})$ where $w^{(j)} \in \{0,1\}^j$ is the length-$j$
prefix of $w$, and $|w^{(j)}|_1 = a_j(n)$ satisfies $3^{|w^{(j)}|_1} < 2^{\,j}$. So the
displayed ratio is one of the ratios over which $B_k$ is defined as the maximum, whence
$n \le B_k$. Thus $E_k \subseteq [1, B_k] \cap \mathbb{Z}^+$ and
$\#E_k \le \lfloor B_k\rfloor < \infty$.

**Closed form and monotonicity of $B_k$.** Whether a pair $(j, w)$ qualifies
("fails") depends only on $(j, a)$ with $a = |w|_1$. For fixed failing $(j,a)$ with
$a \ge 1$, the maximum of $\rho(w)$ over $w \in \{0,1\}^j$ with $|w|_1 = a$ is
$2^{\,j-a}(3^a - 2^a)$, attained at $0^{\,j-a}1^a$ (F3); for $a = 0$ the only value is
$\rho = 0 = 2^{\,j}(3^0 - 2^0)$. Hence the word-level maximum equals
$$B_k = \max\Big\{ \tfrac{2^{\,j-a}(3^a-2^a)}{2^{\,j}-3^{\,a}} : 1 \le j \le k,\
0 \le a \le j,\ 3^a < 2^{\,j} \Big\},$$
which is nondecreasing in $k$ (the max is over a set that grows with $k$). $\square$

**Worked boundary cases (part of the proof record).**
$k = 1$: the failing pairs are $(j,a) = (1,0)$ only, ratio $0$, so $B_1 = 0$ and
$E_1 = \emptyset$. Directly: $T(n) < n$ for even $n$ and $T(n) = (3n+1)/2 > n$ for odd
$n$, so $\{\sigma > 1\}$ = the odd numbers = the class of the word $(1)$, which is the
unique survivor word of length 1 ($a_1 = 1 \ge \lceil\gamma\rceil = 1$) — consistent.
$k \ge 2$: $1 \in E_k$. Indeed $\sigma(1) = \infty > k$ (P0.3), but the word of $1$ is
$(1,0,1,0,\dots)$ with $a_2(1) = 1 < 2 = \lceil 2\gamma\rceil$ (since $3^1 < 2^2$), so
$1 \notin U_k$; and the dichotomy at $j = 2$ gives $1 \le \rho_2(1)/(2^2 - 3) = 1/1$,
consistent with $B_k \ge 2^{2-1}(3-2)/(2^2-3) = 2$. So $E_k \neq \emptyset$ for
$k \ge 2$: the exceptional set is a genuine feature, not an artifact.

### Proof of L-9908.2(b) ($H$ strictly decreasing on $[1/2, 1)$)

On $(0,1)$, using $\log_2 u = \ln u/\ln 2$ and $\frac{d}{dt}[-t\ln t] = -\ln t - 1$,
$\frac{d}{dt}[-(1-t)\ln(1-t)] = \ln(1-t) + 1$:
$$H'(t) = \frac{(-\ln t - 1) + (\ln(1-t) + 1)}{\ln 2} = \frac{\ln\frac{1-t}{t}}{\ln 2}
= \log_2\frac{1-t}{t}.$$
For $t \in (1/2, 1)$: $0 < \frac{1-t}{t} < 1$, so $H'(t) < 0$. Let
$1/2 \le t_1 < t_2 < 1$. $H$ is continuous on $[t_1, t_2]$ and differentiable on
$(t_1, t_2) \subseteq (1/2, 1)$, so by the mean value theorem
$H(t_2) - H(t_1) = H'(\xi)(t_2 - t_1) < 0$ for some $\xi \in (t_1, t_2)$. $\square$

### Proof of L-9908.2(a) (entropy tail bound)

Fix $k \ge 1$ and $t \in (1/2, 1)$, and set $M := \lceil tk \rceil$. Then $1 \le M$
(as $tk > k/2 \ge 1/2 > 0$) and $M \le k$ (as $tk < k$, so the least integer $\ge tk$ is
$\le k$). The sum in question is $\Sigma := \sum_{j=M}^{k} \binom{k}{j}$ (the integers
$j$ with $tk \le j \le k$ are exactly $M \le j \le k$). Set
$$x := \frac{t}{1-t} \;>\; 1 \qquad (t > 1/2 \implies t > 1 - t > 0).$$
For each integer $j \in [M, k]$: $j - tk \ge M - tk \ge 0$, and since $x > 1$, real
exponentiation $y \mapsto x^y$ is increasing, so $x^{\,j - tk} \ge x^0 = 1$. Hence
$$\Sigma \;\le\; \sum_{j=M}^{k} \binom{k}{j}\, x^{\,j-tk}
\;=\; x^{-tk} \sum_{j=M}^{k} \binom{k}{j}\, x^{\,j}
\;\le\; x^{-tk} \sum_{j=0}^{k} \binom{k}{j}\, x^{\,j}
\;=\; x^{-tk}\,(1+x)^k,$$
where the middle inequality adds the nonnegative terms $j < M$ and the last step is the
binomial theorem. It remains to identify the right side. Taking $\log_2$ and using
$1 + x = \frac{1}{1-t}$ and $\log_2 x = \log_2 t - \log_2(1-t)$:
$$\log_2\!\big(x^{-tk}(1+x)^k\big)
= k\Big(-t\log_2 x + \log_2(1+x)\Big)
= k\Big(-t\log_2 t + t\log_2(1-t) - \log_2(1-t)\Big)
= k\,H(t),$$
since $t\log_2(1-t) - \log_2(1-t) = -(1-t)\log_2(1-t)$. Hence
$x^{-tk}(1+x)^k = 2^{kH(t)}$ and $\Sigma \le 2^{kH(t)}$. $\square$

*(The choice $x = t/(1-t)$ is the optimizer of $x \mapsto x^{-tk}(1+x)^k$ over
$x \ge 1$; optimality is not needed, only the identity above. All manipulations are with
positive reals; no ceiling is discarded — the bound is proved for the sum starting
exactly at $\lceil tk\rceil$.)*

### Proof of L-9908.2(c) (survivor-count bound)

$\gamma \in (1/2, 1)$: from $3 < 4 = 2^2$ we get $3^{1/2} < 2$, i.e.
$\tfrac12 < \log_3 2 = \gamma$; from $2 < 3$ we get $\gamma = \log_3 2 < 1$.

A survivor word $w$ of length $k$ satisfies **in particular** the $j = k$ constraint
$a_k(w) \ge \lceil k\gamma\rceil$; hence
$\{\text{survivor words}\} \subseteq \{w : a_k(w) \ge \lceil k\gamma\rceil\}$ and
$s_k \le \#\{w : a_k(w) \ge \lceil k\gamma\rceil\}$. Grouping the words by their number
of ones $a$ (there are exactly $\binom{k}{a}$ words of length $k$ with $a$ ones, and
$\lceil k\gamma\rceil \le k$ since $\gamma < 1$):
$$\#\{w : a_k(w) \ge \lceil k\gamma\rceil\} = \sum_{a=\lceil k\gamma\rceil}^{k}\binom{k}{a}.$$
The integers $a \ge \lceil k\gamma \rceil$ are exactly the integers $a \ge k\gamma$
(Definitions, last bullet), so this sum is the tail sum of L-9908.2(a) at $t = \gamma
\in (1/2,1)$, giving $\le 2^{kH(\gamma)}$. $\square$

### Density toolkit (proved inline)

**Lemma DEN.** Let $M \ge 1$, let $U \subseteq \mathbb{Z}^+$ be a union of $s$ distinct
residue classes mod $M$ (intersected with $\mathbb{Z}^+$), and let
$A \subseteq \mathbb{Z}^+$ satisfy $U \subseteq A \subseteq U \cup F$ with $F$ finite.
Then $d(A)$ exists and equals $s/M$.

*Proof.* (i) *One class.* Fix a class and let $r^* \in \{1, \dots, M\}$ be its least
positive member; its members in $[1,N]$ are $r^* + iM \le N$, $i \ge 0$. Since
$r^* \le M$: for every $0 \le i \le \lfloor N/M\rfloor - 1$,
$r^* + iM \le M + (\lfloor N/M\rfloor - 1)M = \lfloor N/M\rfloor \cdot M \le N$, giving
at least $\lfloor N/M \rfloor$ members; and since $r^* \ge 1$, $r^* + iM \le N$ forces
$i \le (N-1)/M < \lfloor N/M \rfloor + 1$, giving at most $\lfloor N/M\rfloor + 1$
members. (ii) *Union.* Distinct classes are disjoint, so
$s\lfloor N/M\rfloor \le U(N) \le s(\lfloor N/M\rfloor + 1)$. (iii) *Perturbation.*
$U(N) \le A(N) \le U(N) + \#F$, hence
$$\frac{s\lfloor N/M\rfloor}{N} \;\le\; \frac{A(N)}{N} \;\le\;
\frac{s(\lfloor N/M\rfloor+1) + \#F}{N}.$$
Both outer expressions tend to $s/M$ as $N \to \infty$ (using
$N/M - 1 < \lfloor N/M\rfloor \le N/M$ and $\#F$ fixed), so $A(N)/N \to s/M$. $\square$

**Lemma CPL (complement).** For $A \subseteq \mathbb{Z}^+$:
$\underline d(\mathbb{Z}^+\setminus A) = 1 - \bar d(A)$; in particular $d(A) = 0$
implies $d(\mathbb{Z}^+ \setminus A) = 1$. *Proof.* $(\mathbb{Z}^+\setminus A)(N) =
N - A(N)$; take $\liminf$ and use $\liminf(1 - x_N) = 1 - \limsup x_N$. $\square$

### Proof of L-9908.3 (density theorem and certification)

**Exact density.** Fix $k \ge 1$. By F4, distinct survivor words are realized by
pairwise disjoint classes mod $2^k$, so $U_k$ is a union of exactly $s_k$ distinct
classes. By L-9908.1(d), $U_k \subseteq \{\sigma > k\} \subseteq U_k \cup E_k$ with
$E_k$ finite. Lemma DEN (with $M = 2^k$, $s = s_k$, $F = E_k$) gives: $d(\{\sigma>k\})$
exists and equals $s_k 2^{-k}$. By L-9908.2(c),
$s_k 2^{-k} \le 2^{kH(\gamma)} 2^{-k} = 2^{-k(1-H(\gamma))}$.

**Certification of $1 - H(\gamma) > 0.049$.** The following eight statements are exact
inequalities between explicit integers. Each is a *decidable finite statement*; the
exact-arithmetic computation in the Adversarial tests section verifies each one, and
per the packet convention that computation is labeled finite verification — of exact
finite claims, for which a finite computation is a complete check that any reviewer can
independently repeat (by machine, or by hand via $\nu_2$/logarithm bounds).

$$\begin{array}{llll}
\text{N0a:}\ 3 < 2^2 & \Rightarrow\ \gamma > 1/2; \qquad&
\text{N0b:}\ 2 < 3 & \Rightarrow\ \gamma < 1;\\
\text{N1:}\ 3^{306} < 2^{485} & \Rightarrow\ \gamma > \tfrac{306}{485}; &
\text{N2:}\ 3^{53} > 2^{84} & \Rightarrow\ \gamma < \tfrac{53}{84};\\
\text{N3:}\ 485^{10^4} < 2^{89219} & \Rightarrow\ \log_2 485 < \tfrac{89219}{10^4}; &
\text{N4:}\ 306^{10^4} > 2^{82573} & \Rightarrow\ \log_2 306 > \tfrac{82573}{10^4};\\
\text{N5:}\ 179^{10^4} > 2^{74838} & \Rightarrow\ \log_2 179 > \tfrac{74838}{10^4}. &&
\end{array}$$
*(Justification of each " $\Rightarrow$ ": $3^q < 2^p \iff q\ln 3 < p\ln 2 \iff q/p <
\gamma$ for $p, q \ge 1$, by strict monotonicity of $\ln$; likewise $b^{m} < 2^{e}
\iff \log_2 b < e/m$. N0a is the case $q/p = 1/2$: $3 < 4 \iff 3^{1/2} < 2 \iff
\gamma > 1/2$. N2 is included to *enclose* $\gamma$ as assigned:
$\tfrac{306}{485} < \gamma < \tfrac{53}{84}$, an interval of width exactly
$\tfrac{53}{84} - \tfrac{306}{485} = \tfrac{53\cdot485 - 84\cdot306}{40740} =
\tfrac{1}{40740}$; only the lower end N1 is load-bearing below.)*

For a rational $p/q \in (0,1)$ (integers $0 < p < q$), expanding
$\log_2\frac{p}{q} = \log_2 p - \log_2 q$ and $\log_2\frac{q-p}{q} = \log_2(q-p) -
\log_2 q$ in the definition of $H$:
$$H\!\Big(\frac{p}{q}\Big) = \log_2 q - \frac{p}{q}\log_2 p - \frac{q-p}{q}\log_2(q-p).$$
Apply this at $p/q = 306/485$ (so $q - p = 179$). The coefficient of $\log_2 485$ is
$+1$ and the coefficients of $\log_2 306$, $\log_2 179$ are negative, so an **upper**
bound on $H(306/485)$ follows from the **upper** bound N3 and the **lower** bounds
N4, N5:
$$H\!\Big(\tfrac{306}{485}\Big)
\;<\; \frac{89219}{10^4} - \frac{306}{485}\cdot\frac{82573}{10^4}
- \frac{179}{485}\cdot\frac{74838}{10^4}
\;=\; \frac{485\cdot 89219 - 306\cdot 82573 - 179\cdot 74838}{485\cdot 10^4}.$$
The integer arithmetic (hand-checkable):
$485 \cdot 89219 = 43{,}271{,}215$; $306\cdot 82573 = 25{,}267{,}338$;
$179 \cdot 74838 = 13{,}396{,}002$; numerator $= 4{,}607{,}875$; so
$$H\!\Big(\tfrac{306}{485}\Big) \;<\; \frac{4{,}607{,}875}{4{,}850{,}000}
\;=\; \frac{36863}{38800} \;<\; \frac{951}{1000}
\quad\big(\text{cross-multiply: } 36863 \cdot 1000 = 36{,}863{,}000 <
36{,}898{,}800 = 951\cdot 38800\big).$$
By N0a, N0b, N1: $\tfrac12 < \tfrac{306}{485} < \gamma < 1$, so L-9908.2(b) applies on
$[1/2, 1)$ and gives
$$H(\gamma) \;<\; H\!\Big(\tfrac{306}{485}\Big) \;<\; \frac{36863}{38800},
\qquad\text{hence}\qquad
1 - H(\gamma) \;>\; 1 - \frac{36863}{38800} = \frac{1937}{38800}.$$
Finally $\tfrac{1937}{38800} > \tfrac{499}{10^4}$ (cross-multiply:
$1937 \cdot 10^4 = 19{,}370{,}000 > 19{,}361{,}200 = 499 \cdot 38800$) and
$\tfrac{499}{10^4} > \tfrac{49}{10^3} = \tfrac{490}{10^4}$. So
$1 - H(\gamma) > 0.0499 > 0.049$, and for every $k \ge 1$:
$$d(\{\sigma > k\}) \;\le\; 2^{-k(1-H(\gamma))} \;<\; 2^{-k \cdot 1937/38800}
\;<\; 2^{-0.0499\,k}. \qquad\square$$
*(Display-only consistency check, no probative weight: floating point gives
$H(\gamma) \approx 0.949956$, $1 - H(\gamma) \approx 0.050044$, comfortably inside the
certified bounds.)*

**Proof of the Corollary.** For every $k \ge 1$,
$\{\sigma = \infty\} \subseteq \{\sigma > k\}$ (if $\sigma(n) = \infty$ then
$\sigma(n) > k$), and upper density is monotone under inclusion (termwise counts), so
$$\bar d(\{\sigma = \infty\}) \;\le\; d(\{\sigma > k\}) \;\le\; 2^{-k(1-H(\gamma))}
\xrightarrow[k \to \infty]{} 0,$$
the convergence because $1 - H(\gamma) > 0.049 > 0$. Hence
$\bar d(\{\sigma=\infty\}) = 0$; with $0 \le \underline d \le \bar d$ this gives
$d(\{\sigma = \infty\}) = 0$. By Lemma CPL, the complement
$\{n : \sigma(n) < \infty\} = \{n : \exists j \ge 1,\ T^j(n) < n\}$ has natural density
$1$. Nonemptiness of the density-$0$ set: P0.3. $\square$

### L-9908.4(a) — honest scope (boxed)

> **Scope of L-9908.3 — read before citing.**
> 1. **This does NOT show the counterexample set has density 0.** Let
>    $X = \{n : 1 \notin O_C(n)\}$ (D-9909). A counterexample may well dip below its
>    starting point ($\sigma < \infty$) and still never reach $1$; L-9908.3 constrains
>    only the set $\{\sigma = \infty\}$. The link to $X$ is via the **minimal**
>    counterexample only: if $X \ne \emptyset$ and $\mu = \min X$, then
>    $\sigma(\mu) = \infty$ — that statement is **not proved here**; it is
>    L-9909.2(M)(iii) (PROPOSED, under review) and, in conditional form, L-9911.1
>    (PROPOSED). Nothing in the present file depends on it.
> 2. **Density-$0$ is not emptiness.** $\sigma(1) = \infty$ (P0.3), so
>    $\{\sigma = \infty\} \neq \emptyset$ unconditionally. Any argument that "density
>    0 ⟹ no divergent orbit" is invalid on its face.
> 3. **Nothing about individual orbits.** All probability/density statements are over
>    sets of starting points at a fixed prefix length. No claim is made that the parity
>    bits of a *fixed* $n$ behave randomly, and none of the bounds here can be applied
>    to a single trajectory.
> 4. **$\sigma$ measures dipping below the start, not reaching $1$.** Even the (false
>    for $n=1$, unproved for all $n \ge 2$) statement "$\sigma(n) < \infty$ for every
>    $n \ge 2$" would still require the minimal-counterexample descent argument to
>    imply the Collatz conjecture; density-$1$ does not substitute for "all".

### Proof of L-9908.4(b) (per-$c$ descent, fully rigorous)

Fix $c \in (0,1)$ and set $d_c := \log_3(1/c) \in (0, \infty)$, so $3^{-d_c} = c$ and,
since $3^{\gamma} = 2$ (definition of $\gamma = \log_3 2$), $3^{k\gamma - d_c} =
2^k c$ for every $k$.

Two more certified facts (same status as N1–N5; verified in Adversarial tests):
$$\text{N6: } 5^{25} > 2^{58} \Rightarrow \log_2 5 > \tfrac{58}{25}; \qquad
\text{N7: } 3^{50} > 2^{79} \Rightarrow \log_2 3 > \tfrac{79}{50}; \qquad
\text{N8: } 3^5 = 243 < 256 = 2^8 \Rightarrow \tfrac{5}{8} < \gamma .$$
By the rational-$H$ identity with $p/q = 5/8$:
$$H\!\Big(\tfrac58\Big) = \log_2 8 - \tfrac58\log_2 5 - \tfrac38\log_2 3
\;<\; 3 - \tfrac58\cdot\tfrac{58}{25} - \tfrac38\cdot\tfrac{79}{50}
= 3 - \tfrac{29}{20} - \tfrac{237}{400} = \tfrac{1200 - 580 - 237}{400}
= \tfrac{383}{400} \;<\; 1,$$
using the lower bounds N6, N7 against the negative coefficients.

Let $k$ be any integer with
$$k \;\ge\; k_0(c) := \max\Big(1,\ \Big\lceil \frac{d_c}{\gamma - 5/8} \Big\rceil\Big)
\qquad(\text{well-defined: } \gamma - \tfrac58 > 0 \text{ by N8}),$$
so that $k(\gamma - \tfrac58) \ge d_c$, i.e. $k\gamma - d_c \ge \tfrac58 k$.

**Claim: $A_c \subseteq V_k \cup F_k$** where $V_k$ is the union of the (disjoint, by
F4) classes mod $2^k$ of the words $w \in \{0,1\}^k$ with $a_k(w) \ge k\gamma - d_c$,
and $F_k := A_c \setminus V_k$ is finite. Indeed, let $n \in A_c \setminus V_k$ and
$a := a_k(n) < k\gamma - d_c$. Then $3^{a} < 3^{k\gamma - d_c} = c\,2^k$. Since
$n \in A_c$, in particular $T^k(n) \ge c\,n$; multiplying by $2^k$ and using F1:
$3^{a} n + \rho_k(n) \ge c\,2^k n$, so $n\,(c\,2^k - 3^a) \le \rho_k(n)$ with
$c\,2^k - 3^a > 0$, whence
$$n \;\le\; \frac{\rho_k(n)}{c\,2^k - 3^{a}} \;\le\; B(k,c) :=
\max\Big\{ \frac{\rho(u)}{c\,2^k - 3^{|u|_1}} : u \in \{0,1\}^k,\ 3^{|u|_1} < c\,2^k
\Big\} \;<\; \infty,$$
a maximum over a finite (possibly empty, then $B(k,c) := 0$) set of nonnegative reals,
using F2 to replace $\rho_k(n)$ by the word value. So $F_k \subseteq [1, B(k,c)]$ is
finite.

**Counting $V_k$.** Every $w$ counted in $V_k$ has $a_k(w) \ge k\gamma - d_c \ge
\tfrac58 k$, so the number of such words is at most
$\sum_{a \ge (5/8)k} \binom{k}{a} \le 2^{kH(5/8)}$ by L-9908.2(a) with
$t = \tfrac58 \in (\tfrac12, 1)$. Hence $V_k$ is a union of $s' \le 2^{kH(5/8)}$
classes mod $2^k$, and, spelling out the upper half of Lemma DEN's count for
$A_c \subseteq V_k \cup F_k$: for every $N$,
$A_c(N) \le V_k(N) + \#F_k \le s'\big(\lfloor N/2^k\rfloor + 1\big) + \#F_k$, so
dividing by $N$ and letting $N \to \infty$,
$$\bar d(A_c) \;\le\; \frac{s'}{2^k} \;\le\; \frac{2^{kH(5/8)}}{2^k}
\;=\; 2^{-k(1 - H(5/8))} \;\le\; 2^{-k\,(1 - 383/400)} \;=\; 2^{-17k/400}.$$
This holds for **every** $k \ge k_0(c)$; letting $k \to \infty$, $\bar d(A_c) = 0$,
hence $d(A_c) = 0$, and $d(D_c) = 1$ by Lemma CPL. $\square$

> **Quantifier warning (do not overread L-9908.4(b)).** The exceptional density-$0$
> set $A_c$ depends on $c$, and $k_0(c) \to \infty$ as $c \downarrow 0$. The statement
> "for density-$1$ of $n$: $\inf_{j\ge1} T^j(n)/n = 0$" is the countable intersection
> $\bigcap_{m\ge1} D_{1/m}$ and does **not** follow from this lemma, because a countable
> intersection of density-$1$ sets need not have density $1$. That uniform statement is
> left open here (a quantitative-rate argument is the natural route; see Suggested next
> attack). No claim beyond fixed $c$ is made.

---

## Dependency audit

Load-bearing, with exact points of use:

- **NOTATION.md**: D-9902 ($T$; P0.1, F1 context), D-9906 ($v_i, a_k$; throughout),
  D-9910 ($\sigma$; P0.2), $\gamma$ and $\nu_2$ (preamble), empty-sum convention
  ($a_0 = 0$).
- **L-9903 (PROVED)**: L-9903.1 as F1 — used in L-9908.1(b), in the forward half of
  L-9908.1(d), and in L-9908.4(b); L-9903.2 as F2 — used to make the dichotomy
  constants class-wise (backward half of L-9908.1(d); $B(k,c)$ in L-9908.4(b));
  L-9903.3 as F3 — $\rho \ge 0$ in the forward half of L-9908.1(d) (also re-derivable
  inline in one line, as noted), sharp upper bound only for the closed form of $B_k$.
- **L-9902 (PROVED)**: L-9902.1(c) + L-9902.2 + L-9902.3(i) as F4 — used for:
  well-definedness of "the word of a class" (forward half of L-9908.1(d)); disjointness
  and count ($s_k$ classes) of $U_k$ (L-9908.3 via Lemma DEN); the class structure of
  $V_k$ (L-9908.4(b)). Note the *upper* bounds would survive with only
  well-definedness + injectivity; realization (surjectivity) is what makes $U_k$
  consist of exactly $s_k$ (not fewer) classes, needed for the *exact* density value.
- **Standard analysis** (used without repository citation, listed for auditability):
  strict monotonicity of $\ln$; the mean value theorem and the derivative computation
  in L-9908.2(b); the binomial theorem and monotonicity of $y \mapsto x^y$ ($x>1$) in
  L-9908.2(a); limit arithmetic for Lemmas DEN/CPL.
- **Exact integer facts N0a–N8**: decidable finite inequalities, verified by exact
  arithmetic (Adversarial tests, Part 0); load-bearing exactly where displayed
  (N1, N3–N5 for the $0.049$ certificate; N6–N8 for L-9908.4(b); N0a/N0b for domain
  membership; N2 only for the two-sided enclosure remark).

Cross-references, NOT load-bearing (no statement above depends on them):

- **L-9909 (PROPOSED, under review)**: its L-9909.3 (uniform-descent sieve) and
  L-9909.4 ($k \le 8$ exact survivor computation) overlap L-9908.1(d) — same sieve,
  independently derived here from F1–F4, there from its own inline Lemmas B–D; neither
  file cites the other as a dependency, so no circularity. Finite cross-validation:
  its survivor counts $1,1,2,3,4,8,13,19$ ($k \le 8$), $B_2 = 2$, and "$1$ is
  exceptional at $k=2$" all agree with this file's independent computation (Adversarial
  tests, Parts 1 and 3). Its L-9909.2(M)(iii) ($\sigma(\mu) = \infty$) is cited in the
  boxed scope remark only.
- **L-9911 (PROPOSED)**: conditional minimal-counterexample structure; cited in the
  boxed scope remark only. **L-9907 (PROVED)**: divergence-density threshold —
  complementary (it treats $a_k/k$ along a fixed divergent orbit; no logical overlap
  with the density-over-starting-points statements here).

No dependency on L-9908 exists in L-9902/L-9903 (they predate it): no circularity.

## Gap audit

Deliberate search per README §8:

- **Hidden finiteness assumptions:** none — each density statement is proved for fixed
  finite $k$ by explicit counting (Lemma DEN's two-sided sandwich), and the only limit
  taken is $k \to \infty$ over a family of already-proved per-$k$ bounds (Corollary,
  L-9908.4(b)), a legitimate infimum step.
- **Unjustified induction:** the only inductions are P0.1/P0.3 (explicit base and
  step). No induction over words or $k$ is used elsewhere.
- **Boundary cases:** $k = 1$ ($B_1 = 0$, $E_1 = \emptyset$, worked directly);
  $k \ge 2$ ($1 \in E_k$, worked directly — the exceptional set is nonempty, so the
  finite-set correction is not vacuous); $a_j = 0$ branch of the dichotomy (degenerate,
  discussed); $\lceil k\gamma\rceil = k$ for $k \le 2$ (the tail sum is a single term;
  L-9908.2(c) is applied at $t = \gamma$, never at a degenerate rational $t = 1$ — the
  degenerate-$t$ issue arises only in the *adversarial-test certificate*, which
  therefore treats $k \in \{1,2\}$ separately); $t \to 1/2, 1$ endpoints of $H$
  (monotonicity proved on $[1/2, 1)$, all evaluation points $306/485, 5/8, \gamma$
  certified interior).
- **Division safety:** every division is by a certified-positive quantity
  ($2^j - 3^{a_j} \ge 1$ in branch (ii); $c2^k - 3^a > 0$ in L-9908.4(b); $2^j > 0$;
  $485 \cdot 10^4$ etc.).
- **Sign bookkeeping in the $H$ certificates:** the rational-$H$ identity has one
  positive and two negative coefficients; upper bound on the positive term, lower
  bounds on the negatively-weighted terms — stated explicitly at both applications
  (this is the easiest place for a silent error; flagged for reviewers).
- **Empirical vs. universal:** the script's Parts 1–6 are labeled finite verification
  and carry no probative weight for the universal claims. Part 0 verifies decidable
  finite statements (N0a–N8 and four exact rational identities); for those, the finite
  computation is a complete check — the epistemic status is stated precisely in the
  proof of L-9908.3, and every such fact is independently re-checkable.
- **Incorrectly assumed independence:** none used; all counting is exact enumeration
  via the bijection F4. (The classical "random bits" heuristic appears nowhere.)
- **Finite computation extrapolated to infinite behavior:** none. $s_k$ enters the
  proofs only through the *proved* bound L-9908.2(c), never through computed values;
  the computed $s_k$ appear only in the tests.
- **Assumptions equivalent to Collatz:** none; every statement is unconditional. The
  file deliberately does not use $\sigma(\mu) = \infty$ (PROPOSED elsewhere).
- **Circular dependence:** none (see Dependency audit; the L-9909 overlap is mutual
  non-citation with agreeing finite outputs).
- **Interchange of limits:** the only candidate is the Corollary's $k \to \infty$ after
  $N \to \infty$; these are not interchanged — the $N$-limit is completed inside Lemma
  DEN for each $k$ before the $k$-infimum is taken.
- **Status inheritance:** F1–F4 come from files marked PROVED after adversarial review;
  if either L-9902 or L-9903 were later corrected, the exact points of use listed in
  the Dependency audit localize what must be rechecked here.

## Adversarial tests

**Finite verification — not proof** (except that Part 0 checks decidable finite
statements, as discussed in the proof of L-9908.3). Exact integer/`Fraction` arithmetic
in every assertion; floating point appears only in columns explicitly marked
"display". Script:
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/verify_L9908.py`
(python3, standard library, fixed seed, runtime ≈ 5.6 s). Reproduced in full:

```python
#!/usr/bin/env python3
"""Finite verification for L-9908 (Terras stopping-time density), agent fable-02-p2.

Exact integer / Fraction arithmetic in every assertion; floats appear only in
clearly marked DISPLAY columns. Parts:

  (0) integer power certificates N1-N8 and the exact rational arithmetic for the
      bounds H(306/485) < 36863/38800 < 0.951 and H(5/8) < 383/400.
  (1) survivor-word counts s_k for k <= 25 (DP, cross-checked by brute force for
      k <= 16), with an EXACT certificate chain  s_k <= tail_k <= 2^{k H(p_k/k)}
      (<= 2^{k H(gamma)} by monotonicity), via the integer inequality
      tail * p^p * (k-p)^(k-p) <= k^k  with p = ceil(k*gamma).
  (2) exact tail-bound (L-9908.2) spot checks at 400 random rational t = p/k.
  (3) B_k exactly (Fractions) for k <= 25 via the (j,a) closed form, checked
      against full word enumeration for j <= 12; E_k enumerated exactly for
      k <= 25; containment E_k subset [1, B_k] scanned up to 10^5 for k <= 12;
      1 in E_k for 2 <= k <= 25.
  (4) L-9908.1 dichotomy + ceiling equivalence on random trajectories (exact).
  (5) empirical counts #{n <= 10^6 : sigma(n) > k} for k <= 25 against the exact
      finite-N sandwich  s_k*floor(N/2^k) <= count <= s_k*(floor(N/2^k)+1) + #E_k.
  (6) bonus (L-9908.4(b)) sanity: A_c := {n : T^j(n) >= c n for all j >= 1}
      intersected with [1, 10^5] equals {n <= 1/c}, for c = 1/2 and 1/10.
"""
import random
from fractions import Fraction
from math import comb, log2  # log2 is used for DISPLAY columns only

random.seed(99082026)


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def ceil_kgamma(j):
    """Exact ceil(j*gamma), gamma = log_3 2, via: least a >= 0 with 3^a >= 2^j.
    (For j >= 1 equality 3^a = 2^j is impossible, so >= and > agree.)"""
    a, p3, t = 0, 1, 2 ** j
    while p3 < t:
        a += 1
        p3 *= 3
    return a


# --------------------------- Part 0: certificates ----------------------------
certs = [
    ("N0a: 3 < 2^2            (=> gamma > 1/2)", 3 < 2 ** 2),
    ("N0b: 2 < 3              (=> gamma < 1)", 2 < 3),
    ("N8 : 3^5 < 2^8          (=> gamma > 5/8)", 3 ** 5 < 2 ** 8),
    ("N2 : 3^53 > 2^84        (=> gamma < 53/84)", 3 ** 53 > 2 ** 84),
    ("N1 : 3^306 < 2^485      (=> gamma > 306/485)", 3 ** 306 < 2 ** 485),
    ("N3 : 485^10000 < 2^89219  (=> log2 485 < 8.9219)", 485 ** 10000 < 2 ** 89219),
    ("N4 : 306^10000 > 2^82573  (=> log2 306 > 8.2573)", 306 ** 10000 > 2 ** 82573),
    ("N5 : 179^10000 > 2^74838  (=> log2 179 > 7.4838)", 179 ** 10000 > 2 ** 74838),
    ("N6 : 5^25 > 2^58        (=> log2 5 > 58/25)", 5 ** 25 > 2 ** 58),
    ("N7 : 3^50 > 2^79        (=> log2 3 > 79/50)", 3 ** 50 > 2 ** 79),
]
for name, ok in certs:
    assert ok, name
print(f"(0) all {len(certs)} integer power certificates hold exactly")

# enclosure width: 53/84 - 306/485 = 1/40740
assert Fraction(53, 84) - Fraction(306, 485) == Fraction(1, 40740)
# H(306/485) < (485*89219 - 306*82573 - 179*74838) / (485*10^4) = 36863/38800
Hcap = Fraction(485 * 89219 - 306 * 82573 - 179 * 74838, 485 * 10 ** 4)
assert 485 * 89219 - 306 * 82573 - 179 * 74838 == 4607875
assert Hcap == Fraction(4607875, 4850000) == Fraction(36863, 38800)
assert Hcap < Fraction(951, 1000)
assert 1 - Hcap == Fraction(1937, 38800)
assert 1 - Hcap > Fraction(499, 10000) > Fraction(49, 1000)
# H(5/8) < 3 - (5/8)(58/25) - (3/8)(79/50) = 383/400 < 1
H58cap = 3 - Fraction(5, 8) * Fraction(58, 25) - Fraction(3, 8) * Fraction(79, 50)
assert H58cap == Fraction(383, 400) < 1
print("(0) rational arithmetic: H(306/485) < 36863/38800 < 951/1000;"
      " 1 - cap = 1937/38800 > 0.0499;  H(5/8) < 383/400")

GAMMA_F = 1.0 / log2(3)
H_GAMMA_F = -(GAMMA_F * log2(GAMMA_F) + (1 - GAMMA_F) * log2(1 - GAMMA_F))  # display
print(f"(0) display-only floats: gamma ~ {GAMMA_F:.7f}, H(gamma) ~ {H_GAMMA_F:.6f},"
      f" 1-H(gamma) ~ {1 - H_GAMMA_F:.6f}")

# ----------------------- Part 1: survivor-word counts ------------------------
K_MAX = 25
pow2 = [2 ** j for j in range(K_MAX + 2)]
pow3 = [3 ** j for j in range(K_MAX + 2)]

# DP over (prefix length j, ones count a); prune to 3^a >= 2^j after each step
dp = {0: 1}
s = {0: 1}
for j in range(1, K_MAX + 1):
    ndp = {}
    for a, cnt in dp.items():
        ndp[a] = ndp.get(a, 0) + cnt          # append bit 0
        ndp[a + 1] = ndp.get(a + 1, 0) + cnt  # append bit 1
    dp = {a: c for a, c in ndp.items() if pow3[a] >= pow2[j]}
    s[j] = sum(dp.values())

# brute-force cross-check for k <= 16
for k in range(1, 17):
    cnt = 0
    for w in range(2 ** k):
        a, ok = 0, True
        for j in range(1, k + 1):
            a += (w >> (j - 1)) & 1
            if pow3[a] < pow2[j]:
                ok = False
                break
        cnt += ok
    assert cnt == s[k], k
print("(1) survivor DP cross-checked by brute enumeration for k <= 16")

print("    k : s_k, exact tail_k = sum_{a>=ceil(k*gamma)} C(k,a), display 2^{kH(gamma)}")
for k in range(1, K_MAX + 1):
    p = ceil_kgamma(k)
    tail = sum(comb(k, a) for a in range(p, k + 1))
    assert s[k] <= tail, k
    if k >= 3:  # p/k in (1/2,1); exact certificate tail <= 2^{k H(p/k)}
        assert tail * p ** p * (k - p) ** (k - p) <= k ** k, k
        # p/k >= gamma exactly, by construction (3^p >= 2^k)
        assert pow3[p] >= pow2[k]
    print(f"    {k:2d}: s_k = {s[k]:6d}, tail = {tail:7d},"
          f" 2^(kH(gamma)) ~ {2 ** (k * H_GAMMA_F):12.1f} (display)")
print("(1) exact certificate  tail_k * p^p * (k-p)^(k-p) <= k^k  holds for 3 <= k <= 25")
print("    (=> s_k <= tail_k <= 2^{kH(p/k)} <= 2^{kH(gamma)}; k = 1, 2: s_k = 1 directly)")
assert s[1] == 1 and s[2] == 1

# --------------------- Part 2: tail bound random spot checks -----------------
trials = 0
for _ in range(400):
    k = random.randint(3, 60)
    lo = k // 2 + 1
    if lo > k - 1:
        continue
    p = random.randint(lo, k - 1)
    S = sum(comb(k, j) for j in range(p, k + 1))
    assert S * p ** p * (k - p) ** (k - p) <= k ** k, (k, p)
    trials += 1
print(f"(2) L-9908.2 exact instances verified for {trials} random (k, p), k <= 60")

# --------------------------- Part 3: B_k and E_k -----------------------------
def rho_word(w):
    r = 0
    for i, wi in enumerate(w):
        r = (3 ** wi) * r + wi * (2 ** i)
    return r


def word_of(n, k):
    out, x = [], n
    for _ in range(k):
        out.append(x & 1)
        x = T(x)
    return tuple(out)


def sigma_gt(n, k):
    """True iff sigma(n) > k, i.e. T^j(n) >= n for 1 <= j <= k."""
    x = n
    for _ in range(k):
        x = T(x)
        if x < n:
            return False
    return True


def survivor(n, k):
    a, x = 0, n
    for j in range(1, k + 1):
        a += x & 1
        x = T(x)
        if pow3[a] < pow2[j]:
            return False
    return True


# B_k via (j,a) closed form (max over failing pairs of 2^{j-a}(3^a-2^a)/(2^j-3^a))
B = {}
best = Fraction(0)
argbest = None
for j in range(1, K_MAX + 1):
    for a in range(0, j + 1):
        if pow3[a] < pow2[j]:
            val = Fraction(2 ** (j - a) * (pow3[a] - pow2[a]), pow2[j] - pow3[a])
            if val > best:
                best, argbest = val, (j, a)
    B[j] = best
print(f"(3) B_25 = {B[25]} ~ {float(B[25]):.2f} (display), attained at (j,a) = {argbest}")

# cross-check against full word enumeration for j <= 12
best_w = Fraction(0)
for j in range(1, 13):
    for w in range(2 ** j):
        bits = tuple((w >> i) & 1 for i in range(j))
        a = sum(bits)
        if pow3[a] < pow2[j]:
            best_w = max(best_w, Fraction(rho_word(bits), pow2[j] - pow3[a]))
    assert best_w == B[j], j
print("(3) word-level max of rho(w)/(2^j - 3^a) equals the (j,a) closed form, j <= 12")

E = {}
for k in range(1, K_MAX + 1):
    cap = int(B[k])  # floor
    E[k] = sorted(n for n in range(1, cap + 1)
                  if sigma_gt(n, k) and not survivor(n, k))
for k in range(2, K_MAX + 1):
    assert 1 in E[k], k   # sigma(1) = infinity and 1's word (1,0,1,0,...) fails at j=2
assert E[1] == []
# full containment scan up to 10^5 for k <= 12: no exceptional n above B_k
for n in range(1, 10 ** 5 + 1):
    m = 0
    x = n
    while m < 12:
        x = T(x)
        if x < n:
            break
        m += 1
    # m = min(sigma(n)-1, 12); first survivor failure index f (13 = none within 12)
    a, x, f = 0, n, 13
    for j in range(1, 13):
        a += x & 1
        x = T(x)
        if pow3[a] < pow2[j]:
            f = j
            break
    for k in range(1, 13):
        if m >= k and f <= k:      # n in E_k
            assert n <= B[k], (n, k)
print("(3) scan n <= 10^5: every exceptional n lies below B_k, for all k <= 12")
print("    k : floor(B_k), #E_k, E_k (k <= 12)")
for k in range(1, 13):
    print(f"    {k:2d}: {int(B[k]):4d}, {len(E[k]):2d}, {E[k]}")
print(f"    ... k = 25: floor(B_25) = {int(B[25])}, #E_25 = {len(E[25])}, "
      f"E_25 = {E[25]}")

# ------------------- Part 4: dichotomy on random trajectories ----------------
trials = 0
for _ in range(4000):
    n = random.randint(1, 10 ** 9)
    # follow the orbit while it has not dipped, up to 30 steps
    x, a, rho = n, 0, 0
    for j in range(1, 31):
        v = x & 1
        rho = (3 ** v) * rho + v * (2 ** (j - 1))
        a += v
        x = T(x)
        if x < n:
            break
        # here T^j(n) = x >= n; check L-9908.1 exactly
        assert (2 ** j) * x == (3 ** a) * n + rho          # L-9903.1 restated
        assert (pow3[a] >= 2 ** j) == (a >= ceil_kgamma(j))  # ceiling equivalence
        if pow3[a] < 2 ** j:
            assert n * (2 ** j - pow3[a]) <= rho           # exceptional branch
        trials += 1
print(f"(4) L-9908.1 dichotomy + ceiling equivalence: OK at {trials} surviving (n, j) pairs")

# ----------------------- Part 5: empirical sigma counts ----------------------
N = 10 ** 6
hist = [0] * 26
for n in range(1, N + 1):
    x, m = n, 0
    while m < 25:
        x = T(x)
        if x < n:
            break
        m += 1
    hist[m] += 1
counts = [0] * 26
acc = 0
for m in range(25, -1, -1):
    acc += hist[m]
    counts[m] = acc  # counts[k] = #{n <= N : sigma(n) > k} for k <= 25
print(f"(5) N = 10^6;  k : count(sigma>k), exact sandwich bounds, display fractions")
for k in range(1, 26):
    lo = s[k] * (N // 2 ** k)
    hi = s[k] * (N // 2 ** k + 1) + len(E[k])
    assert lo <= counts[k] <= hi, k
    print(f"    {k:2d}: {counts[k]:6d} in [{lo:6d}, {hi:6d}];"
          f" frac {counts[k] / N:.6f} vs s_k/2^k {s[k] / 2 ** k:.6f}"
          f" vs 2^(-k(1-H)) {2 ** (-k * (1 - H_GAMMA_F)):.6f} (display)")
print("(5) exact sandwich  s_k*floor(N/2^k) <= count <= s_k*(floor(N/2^k)+1) + #E_k"
      "  holds for all k <= 25")

# ----------------------------- Part 6: bonus ---------------------------------
for c in (Fraction(1, 2), Fraction(1, 10)):
    members = []
    for n in range(1, 10 ** 5 + 1):
        x = T(n)
        mn = x
        guard = 0
        while x != 1:
            x = T(x)
            guard += 1
            assert guard < 10 ** 4  # every tested n reaches 1 (finite check)
            if x < mn:
                mn = x
        # orbit continues 1,2,1,2,... so min_{j>=1} T^j(n) = mn (>= 1)
        if mn >= c * n:
            members.append(n)
    expected = list(range(1, int(1 / c) + 1))
    assert members == expected, (c, members[:20])
    print(f"(6) c = {c}: A_c intersect [1,10^5] = {{1,...,{int(1 / c)}}} exactly"
          f" ({len(members)} members; all other n dip below c*n)")

print("ALL CHECKS PASSED")
```

**Observed output** (python3, single run, 2026-07-21, runtime 5.6 s):

```text
(0) all 10 integer power certificates hold exactly
(0) rational arithmetic: H(306/485) < 36863/38800 < 951/1000; 1 - cap = 1937/38800 > 0.0499;  H(5/8) < 383/400
(0) display-only floats: gamma ~ 0.6309298, H(gamma) ~ 0.949956, 1-H(gamma) ~ 0.050044
(1) survivor DP cross-checked by brute enumeration for k <= 16
    k : s_k, exact tail_k = sum_{a>=ceil(k*gamma)} C(k,a), display 2^{kH(gamma)}
     1: s_k =      1, tail =       1, 2^(kH(gamma)) ~          1.9 (display)
     2: s_k =      1, tail =       1, 2^(kH(gamma)) ~          3.7 (display)
     3: s_k =      2, tail =       4, 2^(kH(gamma)) ~          7.2 (display)
     4: s_k =      3, tail =       5, 2^(kH(gamma)) ~         13.9 (display)
     5: s_k =      4, tail =       6, 2^(kH(gamma)) ~         26.9 (display)
     6: s_k =      8, tail =      22, 2^(kH(gamma)) ~         52.0 (display)
     7: s_k =     13, tail =      29, 2^(kH(gamma)) ~        100.4 (display)
     8: s_k =     19, tail =      37, 2^(kH(gamma)) ~        194.0 (display)
     9: s_k =     38, tail =     130, 2^(kH(gamma)) ~        374.7 (display)
    10: s_k =     64, tail =     176, 2^(kH(gamma)) ~        723.9 (display)
    11: s_k =    128, tail =     562, 2^(kH(gamma)) ~       1398.4 (display)
    12: s_k =    226, tail =     794, 2^(kH(gamma)) ~       2701.4 (display)
    13: s_k =    367, tail =    1093, 2^(kH(gamma)) ~       5218.5 (display)
    14: s_k =    734, tail =    3473, 2^(kH(gamma)) ~      10081.2 (display)
    15: s_k =   1295, tail =    4944, 2^(kH(gamma)) ~      19475.0 (display)
    16: s_k =   2114, tail =    6885, 2^(kH(gamma)) ~      37622.0 (display)
    17: s_k =   4228, tail =   21778, 2^(kH(gamma)) ~      72678.6 (display)
    18: s_k =   7495, tail =   31180, 2^(kH(gamma)) ~     140401.6 (display)
    19: s_k =  14990, tail =   94184, 2^(kH(gamma)) ~     271229.6 (display)
    20: s_k =  27328, tail =  137980, 2^(kH(gamma)) ~     523964.9 (display)
    21: s_k =  46611, tail =  198440, 2^(kH(gamma)) ~    1012202.2 (display)
    22: s_k =  93222, tail =  600370, 2^(kH(gamma)) ~    1955385.5 (display)
    23: s_k = 168807, tail =  880970, 2^(kH(gamma)) ~    3777439.3 (display)
    24: s_k = 286581, tail = 1271626, 2^(kH(gamma)) ~    7297306.7 (display)
    25: s_k = 573162, tail = 3850756, 2^(kH(gamma)) ~   14097032.7 (display)
(1) exact certificate  tail_k * p^p * (k-p)^(k-p) <= k^k  holds for 3 <= k <= 25
    (=> s_k <= tail_k <= 2^{kH(p/k)} <= 2^{kH(gamma)}; k = 1, 2: s_k = 1 directly)
(2) L-9908.2 exact instances verified for 400 random (k, p), k <= 60
(3) B_25 = 7329863168/2428309 ~ 3018.51 (display), attained at (j,a) = (24, 15)
(3) word-level max of rho(w)/(2^j - 3^a) equals the (j,a) closed form, j <= 12
(3) scan n <= 10^5: every exceptional n lies below B_k, for all k <= 12
    k : floor(B_k), #E_k, E_k (k <= 12)
     1:    0,  0, []
     2:    2,  1, [1]
     3:    2,  1, [1]
     4:    2,  1, [1]
     5:   15,  1, [1]
     6:   15,  1, [1]
     7:   15,  1, [1]
     8:  129,  1, [1]
     9:  129,  1, [1]
    10:  129,  1, [1]
    11:  129,  1, [1]
    12:  129,  1, [1]
    ... k = 25: floor(B_25) = 3018, #E_25 = 1, E_25 = [1]
(4) L-9908.1 dichotomy + ceiling equivalence: OK at 9310 surviving (n, j) pairs
(5) N = 10^6;  k : count(sigma>k), exact sandwich bounds, display fractions
     1: 500000 in [500000, 500001]; frac 0.500000 vs s_k/2^k 0.500000 vs 2^(-k(1-H)) 0.965907 (display)
     2: 250001 in [250000, 250002]; frac 0.250001 vs s_k/2^k 0.250000 vs 2^(-k(1-H)) 0.932975 (display)
     3: 250001 in [250000, 250003]; frac 0.250001 vs s_k/2^k 0.250000 vs 2^(-k(1-H)) 0.901167 (display)
     4: 187501 in [187500, 187504]; frac 0.187501 vs s_k/2^k 0.187500 vs 2^(-k(1-H)) 0.870443 (display)
     5: 125001 in [125000, 125005]; frac 0.125001 vs s_k/2^k 0.125000 vs 2^(-k(1-H)) 0.840767 (display)
     6: 125001 in [125000, 125009]; frac 0.125001 vs s_k/2^k 0.125000 vs 2^(-k(1-H)) 0.812102 (display)
     7: 101562 in [101556, 101570]; frac 0.101562 vs s_k/2^k 0.101562 vs 2^(-k(1-H)) 0.784415 (display)
     8:  74219 in [ 74214,  74234]; frac 0.074219 vs s_k/2^k 0.074219 vs 2^(-k(1-H)) 0.757671 (display)
     9:  74219 in [ 74214,  74253]; frac 0.074219 vs s_k/2^k 0.074219 vs 2^(-k(1-H)) 0.731840 (display)
    10:  62501 in [ 62464,  62529]; frac 0.062501 vs s_k/2^k 0.062500 vs 2^(-k(1-H)) 0.706889 (display)
    11:  62501 in [ 62464,  62593]; frac 0.062501 vs s_k/2^k 0.062500 vs 2^(-k(1-H)) 0.682789 (display)
    12:  55178 in [ 55144,  55371]; frac 0.055178 vs s_k/2^k 0.055176 vs 2^(-k(1-H)) 0.659510 (display)
    13:  44802 in [ 44774,  45142]; frac 0.044802 vs s_k/2^k 0.044800 vs 2^(-k(1-H)) 0.637025 (display)
    14:  44802 in [ 44774,  45509]; frac 0.044802 vs s_k/2^k 0.044800 vs 2^(-k(1-H)) 0.615307 (display)
    15:  39518 in [ 38850,  40146]; frac 0.039518 vs s_k/2^k 0.039520 vs 2^(-k(1-H)) 0.594329 (display)
    16:  32257 in [ 31710,  33825]; frac 0.032257 vs s_k/2^k 0.032257 vs 2^(-k(1-H)) 0.574066 (display)
    17:  32257 in [ 29596,  33825]; frac 0.032257 vs s_k/2^k 0.032257 vs 2^(-k(1-H)) 0.554494 (display)
    18:  28587 in [ 22485,  29981]; frac 0.028587 vs s_k/2^k 0.028591 vs 2^(-k(1-H)) 0.535589 (display)
    19:  28587 in [ 14990,  29981]; frac 0.028587 vs s_k/2^k 0.028591 vs 2^(-k(1-H)) 0.517329 (display)
    20:  26057 in [     0,  27329]; frac 0.026057 vs s_k/2^k 0.026062 vs 2^(-k(1-H)) 0.499692 (display)
    21:  22226 in [     0,  46612]; frac 0.022226 vs s_k/2^k 0.022226 vs 2^(-k(1-H)) 0.482656 (display)
    22:  22226 in [     0,  93223]; frac 0.022226 vs s_k/2^k 0.022226 vs 2^(-k(1-H)) 0.466200 (display)
    23:  20102 in [     0, 168808]; frac 0.020102 vs s_k/2^k 0.020123 vs 2^(-k(1-H)) 0.450306 (display)
    24:  17084 in [     0, 286582]; frac 0.017084 vs s_k/2^k 0.017082 vs 2^(-k(1-H)) 0.434953 (display)
    25:  17084 in [     0, 573163]; frac 0.017084 vs s_k/2^k 0.017082 vs 2^(-k(1-H)) 0.420124 (display)
(5) exact sandwich  s_k*floor(N/2^k) <= count <= s_k*(floor(N/2^k)+1) + #E_k  holds for all k <= 25
(6) c = 1/2: A_c intersect [1,10^5] = {1,...,2} exactly (2 members; all other n dip below c*n)
(6) c = 1/10: A_c intersect [1,10^5] = {1,...,10} exactly (10 members; all other n dip below c*n)
ALL CHECKS PASSED
```

**Reading of the tests, adversarially.**

- *Part 0* is the load-bearing check: N0a–N8 plus the four exact rational identities
  used verbatim in the proofs of L-9908.3 and L-9908.4(b). The display floats
  ($1 - H(\gamma) \approx 0.050044$) sit strictly inside the certified bound
  ($> 0.0499227\ldots = 1937/38800$), as they must.
- *Part 1*: $s_k$ computed two independent ways (path-counting DP with pruning; brute
  enumeration) for $k \le 16$, DP alone to $25$; the certificate
  $\text{tail}_k \cdot p^p (k-p)^{k-p} \le k^k$ is *exactly equivalent* (take $\log_2$)
  to $\text{tail}_k \le 2^{kH(p/k)}$ with $p = \lceil k\gamma\rceil$, and
  $H(p/k) \le H(\gamma)$ by L-9908.2(b) since $p/k \ge \gamma$ ($3^p \ge 2^k$, asserted)
  — so the whole chain $s_k \le 2^{kH(\gamma)}$ is machine-verified without floats for
  $3 \le k \le 25$ ($k \le 2$: $s_k = 1$, bound trivially $> 1$). The $k \le 8$ values
  $1,1,2,3,4,8,13,19$ agree with L-9909.4's independent computation.
- *Part 3*: the exceptional structure is exactly as proved: $E_1 = \emptyset$,
  $E_k = \{1\}$ for **all** $2 \le k \le 25$ — even though the a-priori bound only says
  $\#E_k \le \lfloor B_k\rfloor$ (up to $3018$ at $k = 25$), i.e. the theorem's
  exceptional allowance is generous and reality is thinner; the $10^5$-scan confirms no
  exceptional $n$ above $B_k$ for $k \le 12$ (a failed scan would have refuted
  L-9908.1(d)).
- *Part 5* tests the full pipeline (survivor counting + class counting + exceptional
  set) as an exact finite-$N$ sandwich at $N = 10^6$ — a wrong $s_k$, a wrongly counted
  class, or a missed exceptional element would violate an assertion. The observed
  fractions track $s_k/2^k$ to $\sim 10^{-5}$, and the entropy bound (last column) is,
  as expected, a very loose upper envelope at these $k$.
- *Part 6* confirms the clean prediction of L-9908.4(b)'s proof mechanism at small
  scale: within $[1, 10^5]$, $A_c$ is exactly $\{n \le 1/c\}$ (every tested orbit
  reaches the trivial cycle, making the orbit-minimum $1$). Finite observation only.

## Remaining uncertainty

- All of L-9908.1–.3 and L-9908.4(b) are asserted as fully proved; nothing is PARTIAL
  or CONJECTURED, and no correction to the assigned statements was needed (two
  *strengthenings* beyond the assignment are flagged: the forward containment in
  L-9908.1(d), and the exact density in L-9908.3; the assigned upper-density and
  $E_k$-finiteness statements are implied).
- Places a verifier should press hardest: (1) the sign bookkeeping in the two
  rational-$H$ upper bounds (one positive, two negative coefficients — an inverted
  bound direction there would silently break the certificate); (2) N5, the tightest
  certificate ($179^{10^4}/2^{74838} = 2^{\,\approx 0.157\cdot 10^0}$… margin only
  $\approx 0.16$ bits out of $74838$): re-verify independently, ideally with different
  software; (3) the MVT/monotonicity lemma and its use at the half-open interval
  $[1/2, 1)$; (4) Lemma DEN's $\lfloor N/M\rfloor$ vs $\lfloor N/M\rfloor + 1$ counting;
  (5) in L-9908.4(b), the threshold bookkeeping $k\gamma - d_c \ge \tfrac58 k$ and the
  finiteness of $B(k,c)$ (max over a possibly empty finite set).
- Status inheritance: F1–F4 are from PROVED files (L-9902, L-9903); this file's
  correctness is conditional on those reviews being sound. The overlapping L-9909 is
  PROPOSED; nothing here depends on it, but the agreement of independent finite
  computations is reassuring in both directions.
- Per packet convention the author sets at most PROPOSED; an independent reviewer must
  upgrade.

## Suggested next attack

1. **Review path to PROVED:** re-derive L-9908.1(d) from L-9909.3's independently
   proved sieve (Lemmas B–D there) and compare conclusions; re-verify N0a–N8 with
   independent software (or by hand via repeated squaring mod nothing — they are pure
   integer comparisons); re-do the two rational-$H$ bounds with interval arithmetic.
2. **Sharpen the count:** the assigned bound uses only the $j = k$ constraint. The full
   survivor condition is a ballot-type constraint ($a_j \ge \lceil j\gamma\rceil$ for
   *all* $j$); a reflection/cycle-lemma argument should give
   $s_k = \Theta(2^{kH(\gamma)}/\sqrt{k})$ or better (the observed ratio
   $s_k/2^{kH(\gamma)}$ decays through $\approx 0.041$ at $k = 25$). Worth a separate
   claim file; it would sharpen every downstream density use.
3. **Uniform-in-$c$ descent:** upgrade L-9908.4(b) to "for density-$1$ of $n$,
   $\min_{j \le K(n)} T^j(n)/n \to 0$ with an explicit rate", circumventing the
   countable-intersection obstruction by making $c = c_k \downarrow 0$ explicit along
   $k$ (the proof here already gives $\bar d(A_{c}) \le 2^{-17k/400}$ for all
   $k \ge k_0(c)$; diagonalize $c_k := 3^{-(\gamma - 5/8)k}$). This is the natural
   bridge toward "almost all orbits attain $o(n)$", the qualitative shadow of the
   known almost-everywhere results.
4. **Counterexample-program use:** combine with L-9909.3 Cor. 4 (once L-9909 is
   PROVED): for every $k$ with $\mu > B_k$, the minimal counterexample lies in one of
   just $s_k$ classes mod $2^k$, and $s_k 2^{-k} < 2^{-0.0499k}$ — so candidate
   searches (issues #8, #25) should enumerate survivor classes only; the DP in the
   script generates them online in $O(k)$ memory per class.
5. **Transfer to $C$ and $S$ parameterizations** via L-9901/L-9911.U1 (step-count
   comparison), so that density statements can be quoted in whichever clock a
   downstream file uses.

---

*Signed: fable-02-p2, 2026-07-21. Finite verification script: `verify_L9908.py`
(scratchpad; full text and output above).*

---

## Verification note (fable-02-v12, 2026-07-25)

**Verdict: PASS.** Independent adversarial review per README §13. I reconstructed
L-9908.1–.4 from their explicit dependencies (NOTATION.md, L-9902, L-9903 — both PROVED,
statements re-read at source rather than trusting the F1–F4 restatements), re-ran every
integer certificate with three independent methods, and recomputed $s_k$, $B_k$, $E_k$
and the true empirical stopping-time counts from my own code written from the statements
alone. **No error was found in any numbered claim, in any proof step, or in any displayed
integer.** Status upgraded `PROPOSED` → `PROVED`. Three documentation-level corrections
are recorded in §V7 below; none of them touches a proof. `INDEPENDENTLY_VERIFIED` is
deliberately **not** set (that requires a further independent agent, per README §7).

### V1. Independent restatement (done before reading the author's proofs)

- **.1 (survivor constraint).** $\sigma(n) > k$ iff no $j\in[1,k]$ has $T^j(n) < n$.
  Given that, F1 ($2^jT^j(n) = 3^{a_j}n + \rho_j$) forces, at *each* $j \le k$, either
  $3^{a_j(n)} \ge 2^j$ — equivalently, since $\ln$ is strictly increasing and $a_j\in\mathbb{Z}$,
  $a_j \ge \lceil j\gamma\rceil$ — or else $n \le \rho_j(n)/(2^j - 3^{a_j(n)})$, a quantity
  that by F2 depends only on the length-$j$ prefix word, hence is bounded by the explicit
  class constant $B_k$. The strengthening the author adds is the *converse* direction:
  on $U_k$ the constraint is not merely necessary but sufficient, and strictly so
  ($3^{a_j} > 2^j$ because $3^a = 2^j$ is impossible, plus $\rho \ge 0$, gives
  $T^j(n) > n$, not just $\ge$). I confirm both directions are proved, and that the
  strengthening is exactly what converts an upper density bound into an *exact* density.
- **.2 (entropy tail).** For $1/2 < t < 1$ and $k \ge 1$,
  $\sum_{tk \le j \le k}\binom{k}{j} \le 2^{kH(t)}$; $H$ strictly decreasing on $[1/2,1)$;
  $\gamma \in (1/2,1)$ so $s_k \le \sum_{a \ge \lceil k\gamma\rceil}\binom{k}{a} \le 2^{kH(\gamma)}$
  (only the $j=k$ survivor constraint is used — the bound is therefore lossy, correctly
  flagged by the author).
- **.3 (density).** $U_k$ is a union of exactly $s_k$ classes mod $2^k$ (needs F4
  *surjectivity*, not only injectivity — the author's Dependency audit says this
  explicitly and correctly); $\{\sigma>k\}$ differs from $U_k$ by a finite set; therefore
  $d(\{\sigma>k\})$ exists $= s_k2^{-k} \le 2^{-k(1-H(\gamma))} < 2^{-1937k/38800}$.
  Corollary: $d(\{\sigma=\infty\}) = 0$, the set being provably nonempty ($\sigma(1)=\infty$).
- **.4** scope box + per-$c$ descent with the $t = 5/8$ threshold.

All four match the file's statements; I found no drift between Statement and Proof.

### V2. Proof reconstruction — the author's five priority probes

1. **Sign bookkeeping in the rational-$H$ bounds — CLEAN.** I re-derived
   $H(p/q) = \log_2 q - \tfrac{p}{q}\log_2 p - \tfrac{q-p}{q}\log_2(q-p)$ from scratch
   ($-t\log_2(p/q) = -t\log_2 p + t\log_2 q$, $-(1-t)\log_2\frac{q-p}{q} =
   -(1-t)\log_2(q-p) + (1-t)\log_2 q$, and the two $\log_2 q$ terms sum to $\log_2 q$),
   and verified it numerically at four rationals. Coefficients: $+1$ on $\log_2 q$,
   $-\tfrac pq$ on $\log_2 p$, $-\tfrac{q-p}{q}$ on $\log_2(q-p)$. An **upper** bound on
   $H$ therefore needs an **upper** bound on $\log_2 q$ and **lower** bounds on the other
   two. At $p/q = 306/485$: N3 is an upper bound on $\log_2 485$ (correct slot), N4 and N5
   are lower bounds on $\log_2 306$, $\log_2 179$ (correct slots). At $p/q = 5/8$:
   $\log_2 8 = 3$ is exact, N6 and N7 are lower bounds on $\log_2 5$, $\log_2 3$ (correct
   slots). **No inverted direction anywhere.** Independent numeric confirmation that the
   bounds are genuinely upper bounds: true $H(306/485) = 0.949957011 < 0.950077320 =
   36863/38800$, and true $H(5/8) = 0.954434003 < 0.9575 = 383/400$.
2. **The certificate chain.** See §V3 — all eight re-run, three ways each.
3. **MVT / monotonicity on the half-open interval — CLEAN.** $H'(t) = \log_2\frac{1-t}{t}$
   (I re-differentiated), negative on $(1/2,1)$. For $1/2 \le t_1 < t_2 < 1$: $H$ is
   continuous on $[t_1,t_2] \subset (0,1)$ and differentiable on $(t_1,t_2) \subseteq
   (1/2,1)$ — note this is exactly why the interval is taken half-open, since $H'$ blows up
   at $t=1$ and $H$ is *not* differentiable there; the MVT hypotheses are met at every
   point actually used. Direction check: $306/485 < \gamma$, so decreasing $H$ gives
   $H(\gamma) < H(306/485)$, which is the direction the certificate needs. Numerically
   $H(1/2)=1 > H(306/485)=0.9499570 > H(\gamma)=0.9499555$ — the last gap is only
   $1.5\times10^{-6}$, so the enclosure really does have to be this sharp.
4. **Lemma DEN's $\lfloor N/M\rfloor$ counting — CLEAN.** Lower: for
   $0 \le i \le \lfloor N/M\rfloor - 1$, $r^*+iM \le M + (\lfloor N/M\rfloor-1)M =
   \lfloor N/M\rfloor M \le N$ (vacuously fine when $\lfloor N/M\rfloor = 0$). Upper:
   $r^* \ge 1 \Rightarrow i \le (N-1)/M$, and $\#\{i \ge 0 : i \le (N-1)/M\} =
   \lfloor (N-1)/M\rfloor + 1 \le \lfloor N/M\rfloor + 1$. Both off-by-one directions are
   correct; the finite perturbation $F$ enters only as $+\#F$ on the upper side, and both
   outer expressions $\to s/M$. I tested the resulting finite-$N$ sandwich at $N = 10^6$
   for every $k \le 25$ (§V5) — it holds, and the deviation
   $|A(N) - sN/M|$ never exceeded $21.4$.
5. **Threshold bookkeeping $k\gamma - d_c \ge 5k/8$ in the bonus — CLEAN.**
   $k \ge \lceil d_c/(\gamma-\tfrac58)\rceil \Rightarrow k(\gamma - \tfrac58) \ge d_c
   \Rightarrow k\gamma - d_c \ge \tfrac58 k$; $\gamma - \tfrac58 > 0$ by N8. The identity
   $3^{k\gamma-d_c} = c\,2^k$ follows from $3^\gamma = 2$ and $3^{-d_c} = c$. I verified
   both numerically (60-digit `Decimal`) at $c = 1/2, 1/3, 1/10, 99/100, 1/1000$ with
   $k = k_0(c), k_0+1, k_0+17$: the inequality is tight-but-true at $k = k_0$ exactly as it
   should be (e.g. $c=1/2$: $k_0 = 107$, $k_0\gamma - d_c = 66.8786 \ge 66.8750 = 5k_0/8$).
   The finiteness of $B(k,c)$ over a possibly empty index set is handled correctly: if the
   set is empty then no $n$ satisfies $3^{a_k(n)} < c2^k$ at all, so $F_k = \varnothing$
   and $B(k,c):=0$ is consistent.

### V3. Certificates re-run independently (three methods each)

Method 1: raw Python big-integer comparison. Method 2: `int.bit_length()` (a proof by
itself: e.g. $3^{306}$ has bit length $485$, i.e. $2^{484} \le 3^{306} < 2^{485}$).
Method 3: 120-digit `Decimal` logarithms. All three agree on all eight certificates.

| cert | claim | verdict | $\log_2$ margin (bits) | bit-length check |
|---|---|---|---|---|
| N0a | $3 < 2^2$ | TRUE | $-0.415037$ | 2 vs 3 |
| N0b | $2 < 3$ | TRUE | $-0.584963$ | — |
| **N1** | $3^{306} < 2^{485}$ | **TRUE** | $\mathbf{-0.001475}$ | 485 vs 486 |
| N2 | $3^{53} > 2^{84}$ | TRUE | $+0.003013$ | 85 vs 85 |
| N3 | $485^{10^4} < 2^{89219}$ | TRUE | $-0.590629$ | 89219 vs 89220 |
| N4 | $306^{10^4} > 2^{82573}$ | TRUE | $+0.878427$ | 82574 vs 82574 |
| **N5** | $179^{10^4} > 2^{74838}$ | **TRUE** | $\mathbf{+0.157773}$ | 74839 vs 74839 |
| N6 | $5^{25} > 2^{58}$ | TRUE | $+0.048202$ | 59 vs 59 |
| N7 | $3^{50} > 2^{79}$ | TRUE | $+0.248125$ | 80 vs 80 |
| N8 | $3^5 < 2^8$ | TRUE | $-0.075187$ | 8 vs 9 |

**The tight one the author flagged (N5).** $179^{10^4}$ has bit length exactly $74839$,
so $2^{74838} \le 179^{10^4} < 2^{74839}$; the floor of the quotient
$\lfloor 179^{10^4}/2^{74838}\rfloor = 1$, which establishes N5 with **no logarithms at
all**, and simultaneously shows the margin lies in $(0,1)$ bits. The 120-digit value is
$10^4\log_2 179 - 74838 = 0.15777264256424091643651537373942107\ldots$ — the author's
"$\approx 0.16$ bits" is right.

**Correction to the author's own risk assessment (§V7.1): N5 is *not* the tightest
certificate.** N1 ($3^{306} < 2^{485}$) has margin $0.001475$ bits — a hundred times
tighter than N5 — and N1 *is* load-bearing (it is the lower enclosure of $\gamma$ on which
the whole $0.049$ certificate rests). N2 ($0.003013$ bits) and N6 ($0.048202$ bits) are
also tighter than N5. I therefore re-verified N1 a fourth way: $2^{485} - 3^{306} =
102065376400825306534437391838939444403106454408085639783964140880896699835673006969445010534504805079858638689074275443284439551032910142670903 > 0$
(exact integer difference, printed in full), and the ratio $2^{485}/3^{306} = 1.00102276\ldots$
Likewise $3^{53} - 2^{84} = 40432553845953101497907 > 0$ and
$5^{25} - 2^{58} = 298023223876953125 - 288230376151711744 > 0$. **All hold.**

**Rational arithmetic re-done independently.** $485\cdot89219 = 43{,}271{,}215$;
$306\cdot82573 = 25{,}267{,}338$; $179\cdot74838 = 13{,}396{,}002$; numerator
$= 4{,}607{,}875$; $4607875/4850000 = 36863/38800$ (divide by $125$); $1 - 36863/38800 =
1937/38800 = 0.0499226804\ldots$; $1937\cdot10^4 = 19{,}370{,}000 > 19{,}361{,}200 =
499\cdot38800$. Enclosure width $\tfrac{53}{84}-\tfrac{306}{485} =
\tfrac{25705-25704}{40740} = \tfrac{1}{40740}$. $H(5/8)$ bound:
$3 - \tfrac58\cdot\tfrac{58}{25} - \tfrac38\cdot\tfrac{79}{50} = 3 - \tfrac{29}{20} -
\tfrac{237}{400} = \tfrac{383}{400}$. **Every displayed integer in the file is correct.**

### V4. Independent recomputation of $s_k$, $B_k$, $E_k$ (own code, own algorithms)

- $s_k$ for $k \le 25$ by my own DP over (prefix length, ones count) with the pruning
  $a \ge \lceil j\gamma\rceil$ (computed as $\min\{a : 3^a \ge 2^j\}$, pure integers),
  **cross-checked against a completely separate brute-force enumeration of all $2^k$ words
  for $k \le 20$** (the author only brute-forced to $k \le 16$). Agreement everywhere.
  My values reproduce the author's table exactly for all $25$ entries:
  $1,1,2,3,4,8,13,19,38,64,128,226,367,734,1295,2114,4228,7495,14990,27328,46611,93222,$
  $168807,286581,573162$.
- $s_k \le 2^{kH(\gamma)}$: verified in **exact integer form** for every $k \le 25$ via
  $\text{tail}_k\cdot p^p (k-p)^{k-p} \le k^k$ with $p = \lceil k\gamma\rceil$ (equivalent
  to $\text{tail}_k \le 2^{kH(p/k)}$ on taking $\log_2$), together with $3^p \ge 2^k$
  (i.e. $p/k \ge \gamma$) and monotonicity. I additionally ran the same exact integer test
  for **all** $2 \le k < 300$ and $k/2 < p < k$ — $22{,}201$ instances, all pass — and at
  $t = 5/8$ in closed rational form ($\Sigma\cdot 5^{5m}3^{3m} \le 8^{8m}$ for $k = 8m$,
  $m \le 50$), which is the exact instance L-9908.4(b) consumes.
- $B_k$: the $(j,a)$ closed form agrees with a brute-force word-level maximum of
  $\rho(w)/(2^j-3^{|w|_1})$ for all $j \le 13$ (author: $j \le 12$). $B_{25} =
  7329863168/2428309 \approx 3018.505$, attained at $(j,a) = (24,15)$; note
  $2428309 = 2^{24}-3^{15}$ and $7329863168 = 2^{9}(3^{15}-2^{15})$ — consistent with the
  closed form. $B_k$ is nondecreasing.
- $E_k$: $E_1 = \varnothing$, $E_k = \{1\}$ for $2 \le k \le 25$.
- **Refutation attempt on L-9908.1(d):** I scanned every $n \le 3\times10^5$ and every
  $k \le 20$ looking for an $n$ with $\sigma(n) > k$, non-survivor word, and $n > B_k$
  (which would refute the lemma). **None found.** I also tested the forward containment
  $U_k \subseteq \{\sigma>k\}$ for $n \le 2\times10^5$ at $k \in \{5,10,15\}$ and the
  *strict* growth $T^j(n) > n$ on $U_{12}$ for $n \le 5\times10^4$: no violations.

### V5. True empirical density at $N = 10^6$ vs the claimed exact density

I computed $\#\{n \le 10^6 : \sigma(n) > k\}$ directly from the orbit definition
(no survivor machinery) for every $k \le 25$, and compared with $s_k2^{-k}$:

```text
  k :   count   frac        s_k/2^k      count - s_k*N/2^k
   1:  500000  0.500000   0.500000       +0.0
   5:  125001  0.125001   0.125000       +1.0
  10:   62501  0.062501   0.062500       +1.0
  15:   39518  0.039518   0.039520       -2.3
  20:   26057  0.026057   0.026062       -5.0
  23:   20102  0.020102   0.020123      -21.4   <- largest deviation over k <= 25
  25:   17084  0.017084   0.017082       +2.4
```

Maximum absolute deviation over all $k \le 25$ is $21.4$ out of $10^6$ — i.e. the observed
frequency agrees with the claimed exact density to $\sim 2\times10^{-5}$ absolute. **No
mismatch requiring investigation.** The residual is fully explained by Lemma DEN's own
error term: $|A(N) - sN/M| \le s + \#F$ (each class contributes
$\lfloor N/M\rfloor$ or $\lfloor N/M\rfloor+1$), which I verified holds for every $k\le25$,
as does the author's sandwich $s_k\lfloor N/2^k\rfloor \le \text{count} \le
s_k(\lfloor N/2^k\rfloor+1)+\#E_k$.

I then ran a **sharper** test than the author's, one that pins the theory exactly rather
than sandwiching it: the theorem predicts the *exact identity*
$$\#\{n\le N : \sigma(n) > k\} \;=\; \#(U_k \cap [1,N]) \;+\; \#(E_k\cap[1,N]).$$
Computing the three quantities by three separate passes over $[1,10^6]$, the identity holds
**with equality for every $k \le 25$**, with $\#(E_k\cap[1,N]) = 0$ for $k=1$ and
$=\#\{1\}=1$ for $2 \le k \le 25$. A single miscounted survivor class, a wrong
$\lceil j\gamma\rceil$, or one missed exceptional integer would have broken it.

### V6. Cross-check against L-9909 (independent derivation)

L-9909 is now **PROVED** and derives the same sieve from its own inline Lemmas B–D.
My independently computed values agree with **both** files:

| quantity | L-9909 | this file | fable-02-v12 (independent) |
|---|---|---|---|
| $s_k$, $k \le 8$ | $1,1,2,3,4,8,13,19$ | same | **$1,1,2,3,4,8,13,19$** ✓ |
| $\lceil k\gamma\rceil$, $k \le 8$ | $1,2,2,3,4,4,5,6$ | (implicit) | **$1,2,2,3,4,4,5,6$** ✓ |
| $B_1..B_8$ | $0,2,2,\tfrac{20}{7},\tfrac{76}{5},\tfrac{76}{5},\tfrac{76}{5},\tfrac{1688}{13}$ | $\lfloor B_k\rfloor = 0,2,2,2,15,15,15,129$ | **$0,2,2,\tfrac{20}{7},\tfrac{76}{5},\tfrac{76}{5},\tfrac{76}{5},\tfrac{1688}{13}$** ✓ |
| $1 \in E_2$ | yes | yes | **yes** ✓ |

The two files' survivor densities also match L-9909's $1/2,1/4,1/4,3/16,1/8,1/8,13/128,
19/256$. **No circularity:** L-9909 does not cite L-9908 (it forward-*promises* the density
statement and explicitly proves nothing in that direction), and L-9908 lists L-9909 as
non-load-bearing. I checked the dependency direction at source: L-9908's load-bearing
imports are only NOTATION.md, L-9902 (PROVED, reviewed by fable-02-v2) and L-9903 (PROVED,
reviewed by fable-02-v3), and I re-read L-9902.1(c)/.2/.3(i) and L-9903.1/.2/.3 at source
— the F1–F4 restatements in this file are **faithful**, with no strengthening smuggled in.
Neither L-9902 nor L-9903 depends on L-9908.

### V7. Corrections and documented fixes

The author's prose is left intact; the three items below are recorded here rather than
edited in place, because two of them concern statuses that may change again.

1. **"N5, the tightest certificate" (Remaining uncertainty, item 2) is inaccurate.** N1
   ($3^{306} < 2^{485}$, margin $0.001475$ bits) is roughly $100\times$ tighter than N5
   ($0.157773$ bits), and N2 ($0.003013$) and N6 ($0.048202$) are also tighter. N1 is
   load-bearing, so a future reviewer's attention should go there first. I have verified
   N1 four independent ways (§V3); the claim is true, but the file's risk ranking was
   pointing at the wrong certificate.
2. **Stale cross-reference statuses.** The header, Motivation, Dependency audit and
   Remaining uncertainty describe L-9909 and L-9911 as `PROPOSED, under review`. Both are
   now `PROVED`. This is cosmetic only: both are explicitly listed as *not* load-bearing,
   and I confirmed no proof step uses them.
3. **Motivation bullet 1 overstates the reach of the localization (imprecision, not an
   error in any claim).** The text says "any candidate divergent orbit … must live inside
   an explicitly exponentially thin set: for each $k$, inside one of $s_k$ residue classes
   mod $2^k$ or below $B_k$." Strictly, what is proved localizes $\{n : \sigma(n) > k\}$,
   and a divergent orbit's *starting point* may perfectly well have $\sigma(n) < \infty$
   (dip below itself once, then escape). The correct — and equally usable — form is:
   *every* orbit that is unbounded, divergent, or eventually periodic on a nontrivial cycle
   contains a point $m_0$ (its orbit-minimum, which exists by well-ordering of
   $\mathbb{Z}^+$) with $T^j(m_0) \ge m_0$ for all $j$, hence $\sigma(m_0) = \infty$; so
   *some point of the orbit*, not necessarily its start, lies in a survivor class mod $2^k$
   or below $B_k$, for every $k$. Note the file's own boxed remark item 1 states the honest
   version correctly ("A counterexample may well dip below its starting point … and still
   never reach 1"), so the file does not depend on the loose phrasing anywhere; only the
   motivational sentence should be read with this caveat.

**Scope-honesty audit (README §13 step 3 / anti-confabulation).** I specifically checked
that nothing in the file suggests density-$0$ bears on the *existence* of counterexamples.
It does not: the boxed remark L-9908.4(a) is correct and unusually explicit on all four
points (density-0 $\ne$ empty, with the witness $\sigma(1) = \infty$; no individual-orbit
conclusion; $\sigma$ measures dipping below the start, not reaching $1$; the counterexample
set is not what is bounded). The quantifier warning attached to L-9908.4(b) is also correct:
$\bigcap_{m} D_{1/m}$ genuinely does not inherit density $1$ from its factors, $k_0(c)\to\infty$
as $c \downarrow 0$, and the file claims nothing uniform in $c$. Both warnings are load-bearing
for honest downstream citation and should be preserved verbatim by any future editor.

### V8. Residual uncertainty

- Correctness is conditional on L-9902 and L-9903 (both PROVED after their own adversarial
  reviews). I re-read the exact statements used, not their proofs.
- All computations are finite verification and carry no probative weight for the universal
  claims, **except** the integer certificates N0a–N8 and the exact rational identities,
  which are decidable finite statements for which a machine check is a complete check. I
  re-derived those with three independent methods precisely because they are the only place
  where computation is load-bearing.
- Everything above is `PROVED`-level evidence, not `INDEPENDENTLY_VERIFIED`: per README §7
  that status needs a second independent reconstruction beyond this one.

### V9. Verification code and output (finite verification — see §V8 for its status)

Scripts (python3, standard library only, seed `20260725`, total runtime ~9 s), written by
fable-02-v12 from the *statements* of L-9908, independently of the author's
`verify_L9908.py`:
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/`
`v12_verify.py`, `v12_sharp.py`, `v12_extra.py`. Reproduced in full.

#### `v12_verify.py`

```python
#!/usr/bin/env python3
"""Independent adversarial verification of L-9908 (agent fable-02-v12, 2026-07-25).

Written from the STATEMENTS of L-9908 alone (not from the author's script).
Exact integer / Fraction arithmetic throughout; floats only where labelled DISPLAY.

Sections:
  A. integer certificates N0a,N0b,N1,N2,N3,N4,N5,N6,N7,N8 + margins (3 independent
     methods for the tight one: big-int compare, bit_length, 60-digit Decimal log).
  B. rational-H arithmetic for H(306/485) and H(5/8), sign directions checked.
  C. survivor-word counts s_k, k <= 25, by my own DP; brute force cross-check k <= 20;
     cross-check k <= 8 against L-9909's 1,1,2,3,4,8,13,19; exact check
     s_k <= tail_k <= 2^{k H(gamma)} (integer form).
  D. B_k closed form vs word-level max; E_k; 1 in E_k.
  E. true empirical fraction of n <= 10^6 with sigma(n) > k, k <= 25, vs s_k 2^{-k}.
  F. targeted attacks: 2(a) tail bound at random (k,t); ceiling equivalence;
     L-9908.4(b) threshold bookkeeping; H monotonicity direction.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
from math import comb, log2
import random

random.seed(20260725)

print("=" * 78)
print("A. INTEGER CERTIFICATES")
print("=" * 78)

# N0a: 3 < 2^2  => gamma > 1/2      (3^q < 2^p  <=>  q/p < gamma)
# N0b: 2 < 3    => gamma < 1
# N1 : 3^306 < 2^485      => gamma > 306/485
# N2 : 3^53  > 2^84       => gamma < 53/84
# N3 : 485^10^4 < 2^89219 => log2 485 < 8.9219
# N4 : 306^10^4 > 2^82573 => log2 306 > 8.2573
# N5 : 179^10^4 > 2^74838 => log2 179 > 7.4838
# N6 : 5^25 > 2^58        => log2 5 > 58/25
# N7 : 3^50 > 2^79        => log2 3 > 79/50
# N8 : 3^5 < 2^8          => gamma > 5/8
certs = [
    ("N0a  3 < 2^2",               3, 1, 2, 2, "<"),
    ("N0b  2^1 < 3^1",             2, 1, 3, 1, "<"),   # written as 2<3
    ("N1   3^306 < 2^485",         3, 306, 2, 485, "<"),
    ("N2   3^53 > 2^84",           3, 53, 2, 84, ">"),
    ("N3   485^10000 < 2^89219",   485, 10000, 2, 89219, "<"),
    ("N4   306^10000 > 2^82573",   306, 10000, 2, 82573, ">"),
    ("N5   179^10000 > 2^74838",   179, 10000, 2, 74838, ">"),
    ("N6   5^25 > 2^58",           5, 25, 2, 58, ">"),
    ("N7   3^50 > 2^79",           3, 50, 2, 79, ">"),
    ("N8   3^5 < 2^8",             3, 5, 2, 8, "<"),
]
getcontext().prec = 80
LOG2_10 = None
for name, b1, e1, b2, e2, rel in certs:
    L = b1 ** e1
    R = b2 ** e2
    got = (L < R) if rel == "<" else (L > R)
    assert got, "CERTIFICATE FAILS: " + name
    # exact margin in bits, via 80-digit decimal logs (independent method)
    lo = (Decimal(b1).ln() / Decimal(2).ln()) * e1
    ro = (Decimal(b2).ln() / Decimal(2).ln()) * e2
    margin = lo - ro
    # third method: bit lengths
    bl, br = L.bit_length(), R.bit_length()
    print(f"  {name:28s} TRUE   log2-margin(L-R) = {margin:+.6f} bits"
          f"   bit_length: {bl} vs {br}")

# The tight one, N5, examined three ways with full care.
print("\n  --- N5 (the tight certificate, claimed margin ~0.16 bits) ---")
L5 = 179 ** 10000
print(f"  179^10000 has bit_length {L5.bit_length()}  (so 2^{L5.bit_length()-1} <= x < 2^{L5.bit_length()})")
print(f"  target 2^74838 has bit_length {(2**74838).bit_length()}")
assert L5 > 2 ** 74838
assert L5 < 2 ** 74839, "179^10000 should sit between 2^74838 and 2^74839"
getcontext().prec = 120
m5 = (Decimal(179).ln() / Decimal(2).ln()) * 10000 - Decimal(74838)
print(f"  120-digit Decimal: 10000*log2(179) - 74838 = {m5}")
# exact rational sandwich on the margin using integer arithmetic only:
# 179^10000 / 2^74838 = q + r/2^74838 ; compute floor of the ratio
q5 = L5 >> 74838
print(f"  floor(179^10000 / 2^74838) = {q5}  (>=1 confirms N5 with no logs at all)")
assert q5 >= 1
# and the ratio is < 2 <=> margin < 1 bit
print(f"  floor(179^10000 / 2^74838) < 2 ? {q5 < 2}  => margin in (0,1) bits")

print("\n  --- N3 (the other 10^4-power certificate) ---")
L3 = 485 ** 10000
print(f"  485^10000 bit_length = {L3.bit_length()}; 2^89219 bit_length = 89220")
assert L3 < 2 ** 89219
getcontext().prec = 120
m3 = Decimal(89219) - (Decimal(485).ln() / Decimal(2).ln()) * 10000
print(f"  120-digit Decimal: 89219 - 10000*log2(485) = {m3}  (margin, must be > 0)")
assert m3 > 0
print("\n  --- N4 ---")
m4 = (Decimal(306).ln() / Decimal(2).ln()) * 10000 - Decimal(82573)
print(f"  120-digit Decimal: 10000*log2(306) - 82573 = {m4}  (must be > 0)")
assert m4 > 0
assert 306 ** 10000 > 2 ** 82573

print("\n" + "=" * 78)
print("B. RATIONAL-H ARITHMETIC (sign directions)")
print("=" * 78)

# H(p/q) = log2 q - (p/q) log2 p - ((q-p)/q) log2 (q-p).
# Re-derive symbolically at a numeric level for sanity (DISPLAY) then do exact bound.
def H_float(t):
    return -(t * log2(t) + (1 - t) * log2(1 - t))


for (p, q) in [(306, 485), (5, 8), (3, 7), (11, 13)]:
    lhs = H_float(p / q)
    rhs = log2(q) - (p / q) * log2(p) - ((q - p) / q) * log2(q - p)
    assert abs(lhs - rhs) < 1e-12, (p, q)
print("  identity H(p/q) = log2 q - (p/q)log2 p - ((q-p)/q)log2(q-p) checked "
      "numerically at 4 points (DISPLAY-level sanity)")
print("  coefficient signs: +1 on log2 q, -(p/q) on log2 p, -((q-p)/q) on log2(q-p)")
print("  => UPPER bound on H needs UPPER bound on log2 q and LOWER bounds on the")
print("     other two.  N3 is an upper bound on log2 485 (correct slot);")
print("     N4, N5 are lower bounds on log2 306, log2 179 (correct slots).")

num = 485 * 89219 - 306 * 82573 - 179 * 74838
print(f"\n  485*89219   = {485*89219}")
print(f"  306*82573   = {306*82573}")
print(f"  179*74838   = {179*74838}")
print(f"  numerator   = {num}")
assert 485 * 89219 == 43271215
assert 306 * 82573 == 25267338
assert 179 * 74838 == 13396002
assert num == 4607875
Hcap = Fraction(num, 485 * 10 ** 4)
print(f"  H(306/485) < {Hcap} = {Fraction(36863,38800)} ? {Hcap == Fraction(36863,38800)}")
assert Hcap == Fraction(36863, 38800)
assert Hcap < Fraction(951, 1000)
one_minus = 1 - Hcap
assert one_minus == Fraction(1937, 38800)
print(f"  1 - H(306/485) > 1937/38800 = {float(Fraction(1937,38800)):.10f} (DISPLAY)")
assert Fraction(1937, 38800) > Fraction(499, 10000) > Fraction(49, 1000)
assert 1937 * 10 ** 4 == 19370000 and 499 * 38800 == 19361200
print(f"  cross-mult: 1937*10^4 = {1937*10**4} > {499*38800} = 499*38800  OK")

# true value check (DISPLAY): is 36863/38800 really an upper bound for H(306/485)?
print(f"  DISPLAY: true H(306/485) = {H_float(306/485):.9f} < {float(Hcap):.9f} OK")
assert H_float(306 / 485) < float(Hcap)
GAMMA = 1.0 / log2(3)
print(f"  DISPLAY: gamma = {GAMMA:.9f}, 306/485 = {306/485:.9f}, 53/84 = {53/84:.9f}")
assert 306 / 485 < GAMMA < 53 / 84
print(f"  DISPLAY: H(gamma) = {H_float(GAMMA):.9f} < H(306/485) (monotone decreasing) "
      f"and 1-H(gamma) = {1-H_float(GAMMA):.9f} > 1937/38800 = "
      f"{float(Fraction(1937,38800)):.9f}")
assert 1 - H_float(GAMMA) > float(Fraction(1937, 38800))
assert Fraction(53, 84) - Fraction(306, 485) == Fraction(1, 40740)
print(f"  enclosure width 53/84 - 306/485 = 1/40740 OK")

H58 = 3 - Fraction(5, 8) * Fraction(58, 25) - Fraction(3, 8) * Fraction(79, 50)
print(f"\n  H(5/8) < 3 - (5/8)(58/25) - (3/8)(79/50) = {H58} = {float(H58):.6f}")
assert H58 == Fraction(383, 400) and H58 < 1
print(f"  DISPLAY: true H(5/8) = {H_float(5/8):.9f} < 0.9575 OK; 1-H(5/8) > 17/400 = 0.0425")
assert H_float(5 / 8) < float(H58)

print("\n" + "=" * 78)
print("C. SURVIVOR WORD COUNTS s_k (own DP)")
print("=" * 78)

KMAX = 25


def ceil_j_gamma(j):
    """least integer a >= 0 with 3^a >= 2^j  ( = ceil(j*gamma) by L-9908.1(c))"""
    a = 0
    while 3 ** a < 2 ** j:
        a += 1
    return a


CEIL = [None] + [ceil_j_gamma(j) for j in range(1, KMAX + 1)]
print(f"  ceil(j*gamma), j=1..12: {CEIL[1:13]}")
# independent check of CEIL against float ceiling
from math import ceil as _ceil
for j in range(1, KMAX + 1):
    assert CEIL[j] == _ceil(j * GAMMA), j   # DISPLAY-level agreement
print("  agrees with float ceil(j*gamma) for j <= 25 (DISPLAY cross-check)")

# my own DP: state = number of ones so far; survivor prefix condition enforced each step
dp = {0: 1}
s = {}
for j in range(1, KMAX + 1):
    nxt = {}
    for a, c in dp.items():
        nxt[a] = nxt.get(a, 0) + c
        nxt[a + 1] = nxt.get(a + 1, 0) + c
    dp = {a: c for a, c in nxt.items() if a >= CEIL[j]}
    s[j] = sum(dp.values())

# fully independent brute force enumeration for k <= 20 (no DP reuse)
def brute_s(k):
    tot = 0
    for m in range(2 ** k):
        a = 0
        good = True
        for j in range(1, k + 1):
            a += (m >> (j - 1)) & 1
            if a < CEIL[j]:
                good = False
                break
        tot += good
    return tot


for k in range(1, 21):
    b = brute_s(k)
    assert b == s[k], (k, b, s[k])
print("  DP vs independent brute-force enumeration: AGREE for k <= 20")

L9909 = [1, 1, 2, 3, 4, 8, 13, 19]
mine8 = [s[k] for k in range(1, 9)]
print(f"  L-9909 survivor counts k<=8 : {L9909}")
print(f"  my   independent counts k<=8: {mine8}   MATCH = {mine8 == L9909}")
assert mine8 == L9909

print("\n  k :      s_k       tail_k    s_k <= tail?   exact cert tail*p^p*(k-p)^(k-p) <= k^k")
for k in range(1, KMAX + 1):
    p = CEIL[k]
    tail = sum(comb(k, a) for a in range(p, k + 1))
    assert s[k] <= tail, k
    if p < k:
        cert = tail * p ** p * (k - p) ** (k - p) <= k ** k
        assert cert, (k, p)
    else:
        cert = "n/a (p=k)"
    print(f"  {k:2d}: {s[k]:9d} {tail:12d}        yes        {cert}")

# the promised bound s_k <= 2^{k H(gamma)}: exact integer form.
# 2^{k H(gamma)} >= 2^{k H(p/k)} = k^k / (p^p (k-p)^{k-p})   when p/k >= gamma
print("\n  exact chain  s_k <= tail_k <= 2^{k H(p_k/k)} <= 2^{k H(gamma)}:")
for k in range(1, KMAX + 1):
    p = CEIL[k]
    assert 3 ** p >= 2 ** k          # p/k >= gamma
    tail = sum(comb(k, a) for a in range(p, k + 1))
    if p < k:
        assert tail * p ** p * (k - p) ** (k - p) <= k ** k, k
    else:
        assert tail == 1 <= 2 ** k
print("    holds for every k <= 25 (integer arithmetic, no floats)")
print("  DISPLAY ratio s_k / 2^{kH(gamma)}:")
HG = H_float(GAMMA)
for k in (5, 10, 15, 20, 25):
    print(f"    k={k:2d}: s_k={s[k]:7d}, 2^(kH) ~ {2**(k*HG):14.1f}, ratio {s[k]/2**(k*HG):.5f}")
for k in range(1, KMAX + 1):
    assert s[k] <= 2 ** (k * HG) * (1 + 1e-9), k
print("  s_k <= 2^{kH(gamma)} numerically confirmed for k <= 25 too")

print("\n" + "=" * 78)
print("D. B_k, E_k")
print("=" * 78)


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def rho_word(bits):
    r = 0
    for i, wi in enumerate(bits):
        r = (3 ** wi) * r + wi * (2 ** i)
    return r


# closed form
Bcf = {}
best = Fraction(0)
arg = None
for j in range(1, KMAX + 1):
    for a in range(0, j + 1):
        if 3 ** a < 2 ** j:
            v = Fraction(2 ** (j - a) * (3 ** a - 2 ** a), 2 ** j - 3 ** a)
            if v > best:
                best, arg = v, (j, a)
    Bcf[j] = best
# word-level max, independent, j <= 13
Bw = {}
bw = Fraction(0)
for j in range(1, 14):
    for m in range(2 ** j):
        bits = tuple((m >> i) & 1 for i in range(j))
        a = sum(bits)
        if 3 ** a < 2 ** j:
            bw = max(bw, Fraction(rho_word(bits), 2 ** j - 3 ** a))
    Bw[j] = bw
    assert Bw[j] == Bcf[j], (j, Bw[j], Bcf[j])
print("  closed form B_k == word-level max for k <= 13: AGREE")
print(f"  B_1..B_8 = {[str(Bcf[j]) for j in range(1,9)]}")
print("  L-9909's B_1..B_8 = ['0','2','2','20/7','76/5','76/5','76/5','1688/13']")
assert [str(Bcf[j]) for j in range(1, 9)] == ['0', '2', '2', '20/7', '76/5', '76/5',
                                              '76/5', '1688/13']
print(f"  B_25 = {Bcf[25]} ~ {float(Bcf[25]):.3f} (DISPLAY), argmax (j,a) = {arg}")
print(f"  B_k nondecreasing: {all(Bcf[j] <= Bcf[j+1] for j in range(1, KMAX))}")


def sigma_gt(n, k):
    x = n
    for _ in range(k):
        x = T(x)
        if x < n:
            return False
    return True


def is_survivor_n(n, k):
    a, x = 0, n
    for j in range(1, k + 1):
        a += x & 1
        x = T(x)
        if a < CEIL[j]:
            return False
    return True


E = {}
for k in range(1, KMAX + 1):
    cap = int(Bcf[k])
    E[k] = [n for n in range(1, cap + 1) if sigma_gt(n, k) and not is_survivor_n(n, k)]
print(f"  E_k for k=1..12: {[E[k] for k in range(1,13)]}")
print(f"  E_25 = {E[25]}; floor(B_25) = {int(Bcf[25])}")
assert E[1] == []
for k in range(2, KMAX + 1):
    assert E[k] == [1], k

# ADVERSARIAL: scan far beyond B_k looking for a violation of L-9908.1(d)
SCAN = 3 * 10 ** 5
viol = []
for n in range(1, SCAN + 1):
    # first j <= 20 where survivor condition fails
    a, x, f = 0, n, None
    for j in range(1, 21):
        a += x & 1
        x = T(x)
        if a < CEIL[j]:
            f = j
            break
    if f is None:
        continue
    # n is in E_k for every k with f <= k <= 20 and sigma(n) > k
    x, m = n, 0
    while m < 20:
        x = T(x)
        if x < n:
            break
        m += 1
    for k in range(f, 21):
        if m >= k and n > Bcf[k]:
            viol.append((n, k))
print(f"  adversarial scan n <= {SCAN}, k <= 20: exceptional n exceeding B_k: "
      f"{viol if viol else 'NONE (L-9908.1(d) not refuted)'}")
assert not viol

# ADVERSARIAL: verify the forward containment U_k subset {sigma>k} directly
bad = []
for n in range(1, 200001):
    for k in (5, 10, 15):
        if is_survivor_n(n, k) and not sigma_gt(n, k):
            bad.append((n, k))
print(f"  forward containment U_k subset {{sigma>k}} tested n<=2*10^5, k in "
      f"{{5,10,15}}: violations {bad if bad else 'NONE'}")
assert not bad
# and the strict version T^j(n) > n on U_k
bad2 = []
for n in range(1, 50001):
    if is_survivor_n(n, 12):
        x = n
        for j in range(1, 13):
            x = T(x)
            if x <= n:
                bad2.append((n, j))
print(f"  strict growth T^j(n) > n on U_12, n <= 5*10^4: violations "
      f"{bad2 if bad2 else 'NONE'}")
assert not bad2

print("\n" + "=" * 78)
print("E. TRUE EMPIRICAL DENSITY  #{n <= 10^6 : sigma(n) > k}/10^6  vs  s_k 2^-k")
print("=" * 78)

N = 10 ** 6
counts = [0] * (KMAX + 1)
for n in range(1, N + 1):
    x = n
    m = 0
    while m < KMAX:
        x = T(x)
        if x < n:
            break
        m += 1
    # sigma(n) > k  for all k <= m
    for k in range(0, m + 1):
        counts[k] += 1
print("  k :   count   frac        s_k/2^k      diff*N   predicted diff range")
maxdev = 0
for k in range(1, KMAX + 1):
    frac = counts[k] / N
    pred = Fraction(s[k], 2 ** k)
    # exact finite-N sandwich implied by L-9908.1(d) + Lemma DEN's count:
    lo = s[k] * (N // 2 ** k)
    hi = s[k] * (N // 2 ** k + 1) + len(E[k])
    assert lo <= counts[k] <= hi, (k, counts[k], lo, hi)
    dev = counts[k] - float(pred) * N
    maxdev = max(maxdev, abs(dev))
    print(f"  {k:2d}: {counts[k]:7d}  {frac:.6f}   {float(pred):.6f}   {dev:+8.1f}  "
          f"[{lo - float(pred)*N:+8.1f}, {hi - float(pred)*N:+8.1f}]")
print(f"  exact sandwich s_k*floor(N/2^k) <= count <= s_k*(floor(N/2^k)+1)+#E_k: HOLDS k<=25")
print(f"  max |count - s_k*N/2^k| = {maxdev:.1f}  (bounded by s_k + #E_k, as Lemma DEN says)")
for k in range(1, KMAX + 1):
    assert abs(counts[k] - Fraction(s[k], 2 ** k) * N) <= s[k] + len(E[k]) + 1, k
print("  and |count - s_k N/2^k| <= s_k + #E_k + 1 for every k <= 25: HOLDS")

# the density bound itself, on the empirical data
print("\n  check d({sigma>k}) <= 2^{-k(1-H(gamma))} on the exact predicted densities:")
for k in range(1, KMAX + 1):
    assert Fraction(s[k], 2 ** k) <= 2 ** (-k * (1 - HG)) * (1 + 1e-9), k
    assert Fraction(s[k], 2 ** k) < 2 ** (-k * float(Fraction(1937, 38800))) * (1 + 1e-9), k
print("    s_k 2^-k <= 2^{-k(1-H(gamma))} and < 2^{-1937k/38800} for all k <= 25 OK")

print("\n" + "=" * 78)
print("F. TARGETED ATTACKS")
print("=" * 78)

# F1. L-9908.2(a) at random (k, t) including t just above 1/2 and just below 1,
#     and at IRRATIONAL-ish t (use high-precision Fractions approximating gamma).
fails = 0
for _ in range(3000):
    k = random.randint(1, 70)
    # random rational t in (1/2, 1)
    den = random.randint(2, 200)
    numr = random.randint(den // 2 + 1, den - 1) if den >= 3 else 1
    if not (den >= 3 and 2 * numr > den and numr < den):
        continue
    t = Fraction(numr, den)
    M = -((-t * k) // 1)          # ceil(t*k) exactly with Fractions
    M = int(M)
    S = sum(comb(k, j) for j in range(M, k + 1))
    # exact form of S <= 2^{kH(t)}:  S * t^{tk} * (1-t)^{(1-t)k} <= 1 is irrational;
    # use the equivalent integer test only when tk is an integer, else use Decimal
    getcontext().prec = 60
    lhs = Decimal(S).ln() / Decimal(2).ln() if S > 0 else Decimal(-10 ** 9)
    tt = Decimal(t.numerator) / Decimal(t.denominator)
    Hd = -(tt * tt.ln() + (1 - tt) * (1 - tt).ln()) / Decimal(2).ln()
    if lhs > Decimal(k) * Hd + Decimal("1e-30"):
        fails += 1
        print("   !!! tail bound FAILS at", k, t, S)
print(f"  L-9908.2(a) tested at 3000 random (k, t=p/q in (1/2,1)), k <= 70: "
      f"{fails} failures")
assert fails == 0

# edge: t extremely close to 1/2 and to 1
for (numr, den, k) in [(501, 1000, 50), (999, 1000, 50), (51, 100, 7), (97, 100, 3),
                       (2, 3, 1), (3, 4, 1), (5, 9, 2)]:
    t = Fraction(numr, den)
    M = int(-((-t * k) // 1))
    S = sum(comb(k, j) for j in range(M, k + 1))
    getcontext().prec = 60
    tt = Decimal(numr) / Decimal(den)
    Hd = -(tt * tt.ln() + (1 - tt) * (1 - tt).ln()) / Decimal(2).ln()
    lhsv = Decimal(S).ln() / Decimal(2).ln()
    assert lhsv <= Decimal(k) * Hd + Decimal("1e-30"), (numr, den, k, S)
print("  edge cases t=501/1000, 999/1000, 51/100, 97/100 and k=1,2,3: OK")

# F2. ceiling equivalence 3^a >= 2^j <=> a >= ceil(j gamma) <=> a > j gamma
getcontext().prec = 60
lg = Decimal(2).ln() / Decimal(3).ln()   # gamma
for j in range(1, 200):
    for a in range(0, 200):
        e1 = 3 ** a >= 2 ** j
        e2 = a >= CEIL[j] if j <= KMAX else a >= ceil_j_gamma(j)
        e3 = Decimal(a) > Decimal(j) * lg
        assert e1 == e2 == e3, (a, j, e1, e2, e3)
print("  ceiling equivalence 3^a>=2^j <=> a>=ceil(j*gamma) <=> a>j*gamma: "
      "OK for all 1<=j<200, 0<=a<200")
# no j<=2000 with j*gamma an integer (irrationality sanity)
for j in range(1, 2001):
    assert 3 ** ceil_j_gamma(j) != 2 ** j
print("  3^a = 2^j never occurs for j <= 2000: OK (consistent with irrationality)")

# F3. L-9908.4(b) threshold bookkeeping: k >= ceil(d_c/(gamma - 5/8)) => k*gamma - d_c >= 5k/8
getcontext().prec = 60
g = lg
for cnum, cden in [(1, 2), (1, 10), (1, 3), (99, 100), (1, 1000)]:
    c = Decimal(cnum) / Decimal(cden)
    d_c = (-c.ln()) / Decimal(3).ln()          # log_3(1/c)
    k0 = max(1, int((d_c / (g - Decimal(5) / Decimal(8))).to_integral_value(rounding="ROUND_CEILING")))
    for k in (k0, k0 + 1, k0 + 17):
        assert Decimal(k) * g - d_c >= Decimal(5) * k / 8 - Decimal("1e-40"), (cnum, cden, k)
    # also check 3^{k gamma - d_c} = c 2^k
    k = k0
    lhs = (Decimal(3) ** (Decimal(k) * g - d_c))
    rhs = c * Decimal(2) ** k
    assert abs(lhs - rhs) < abs(rhs) * Decimal("1e-30"), (cnum, cden)
    print(f"  c={cnum}/{cden}: d_c={float(d_c):.4f}, k0={k0}, k0*gamma-d_c="
          f"{float(Decimal(k0)*g-d_c):.4f} >= 5k0/8={5*k0/8:.4f}  and 3^(k g - d_c)=c 2^k OK")

# F4. H monotone decreasing on [1/2,1) - direction check at the used points
assert H_float(0.5) > H_float(306 / 485) > H_float(GAMMA) > H_float(53 / 84)
assert H_float(5 / 8) > H_float(GAMMA)
print(f"  H(1/2)={H_float(0.5):.6f} > H(306/485)={H_float(306/485):.6f} > "
      f"H(gamma)={H_float(GAMMA):.6f}  (decreasing, so H(gamma) < H(306/485): the "
      f"direction the proof needs)")
print(f"  note 5/8 = 0.625 < gamma = {GAMMA:.6f}, so H(5/8) = {H_float(5/8):.6f} > "
      f"H(gamma); used only in L-9908.4(b) where 5/8 is the threshold, correct direction")

# F5. Try to break L-9908.4(b) empirically for small c: A_c cap [1,X]
for cn, cd in [(1, 2), (1, 4)]:
    c = Fraction(cn, cd)
    mem = []
    for n in range(1, 30001):
        x, mn = T(n), None
        mn = x
        steps = 0
        while x != 1 and steps < 5000:
            x = T(x)
            steps += 1
            mn = min(mn, x)
        if Fraction(mn) >= c * n:
            mem.append(n)
    print(f"  A_(1/{cd}) cap [1,3*10^4] = {mem}  (expected {{1..{cd}}}) -> "
          f"{mem == list(range(1, cd+1))}")

print("\nALL INDEPENDENT CHECKS PASSED")
```

#### Output of `v12_verify.py`

```text
==============================================================================
A. INTEGER CERTIFICATES
==============================================================================
  N0a  3 < 2^2                 TRUE   log2-margin(L-R) = -0.415037 bits   bit_length: 2 vs 3
  N0b  2^1 < 3^1               TRUE   log2-margin(L-R) = -0.584963 bits   bit_length: 2 vs 2
  N1   3^306 < 2^485           TRUE   log2-margin(L-R) = -0.001475 bits   bit_length: 485 vs 486
  N2   3^53 > 2^84             TRUE   log2-margin(L-R) = +0.003013 bits   bit_length: 85 vs 85
  N3   485^10000 < 2^89219     TRUE   log2-margin(L-R) = -0.590629 bits   bit_length: 89219 vs 89220
  N4   306^10000 > 2^82573     TRUE   log2-margin(L-R) = +0.878427 bits   bit_length: 82574 vs 82574
  N5   179^10000 > 2^74838     TRUE   log2-margin(L-R) = +0.157773 bits   bit_length: 74839 vs 74839
  N6   5^25 > 2^58             TRUE   log2-margin(L-R) = +0.048202 bits   bit_length: 59 vs 59
  N7   3^50 > 2^79             TRUE   log2-margin(L-R) = +0.248125 bits   bit_length: 80 vs 80
  N8   3^5 < 2^8               TRUE   log2-margin(L-R) = -0.075187 bits   bit_length: 8 vs 9

  --- N5 (the tight certificate, claimed margin ~0.16 bits) ---
  179^10000 has bit_length 74839  (so 2^74838 <= x < 2^74839)
  target 2^74838 has bit_length 74839
  120-digit Decimal: 10000*log2(179) - 74838 = 0.1577726425642409164365153737394210721556688601100037802176276255233767770297505075825079629418297533683355885788801
  floor(179^10000 / 2^74838) = 1  (>=1 confirms N5 with no logs at all)
  floor(179^10000 / 2^74838) < 2 ? True  => margin in (0,1) bits

  --- N3 (the other 10^4-power certificate) ---
  485^10000 bit_length = 89219; 2^89219 bit_length = 89220
  120-digit Decimal: 89219 - 10000*log2(485) = 0.5906292550997230346164162970820524287345850417252199998240175371028462109591425114788954234964403464370124242120982  (margin, must be > 0)

  --- N4 ---
  120-digit Decimal: 10000*log2(306) - 82573 = 0.8784269265177116154389870603737153089609772978280903811437346889296463609919334190410167986075740416336329701636460  (must be > 0)

==============================================================================
B. RATIONAL-H ARITHMETIC (sign directions)
==============================================================================
  identity H(p/q) = log2 q - (p/q)log2 p - ((q-p)/q)log2(q-p) checked numerically at 4 points (DISPLAY-level sanity)
  coefficient signs: +1 on log2 q, -(p/q) on log2 p, -((q-p)/q) on log2(q-p)
  => UPPER bound on H needs UPPER bound on log2 q and LOWER bounds on the
     other two.  N3 is an upper bound on log2 485 (correct slot);
     N4, N5 are lower bounds on log2 306, log2 179 (correct slots).

  485*89219   = 43271215
  306*82573   = 25267338
  179*74838   = 13396002
  numerator   = 4607875
  H(306/485) < 36863/38800 = 36863/38800 ? True
  1 - H(306/485) > 1937/38800 = 0.0499226804 (DISPLAY)
  cross-mult: 1937*10^4 = 19370000 > 19361200 = 499*38800  OK
  DISPLAY: true H(306/485) = 0.949957011 < 0.950077320 OK
  DISPLAY: gamma = 0.630929754, 306/485 = 0.630927835, 53/84 = 0.630952381
  DISPLAY: H(gamma) = 0.949955527 < H(306/485) (monotone decreasing) and 1-H(gamma) = 0.050044473 > 1937/38800 = 0.049922680
  enclosure width 53/84 - 306/485 = 1/40740 OK

  H(5/8) < 3 - (5/8)(58/25) - (3/8)(79/50) = 383/400 = 0.957500
  DISPLAY: true H(5/8) = 0.954434003 < 0.9575 OK; 1-H(5/8) > 17/400 = 0.0425

==============================================================================
C. SURVIVOR WORD COUNTS s_k (own DP)
==============================================================================
  ceil(j*gamma), j=1..12: [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8]
  agrees with float ceil(j*gamma) for j <= 25 (DISPLAY cross-check)
  DP vs independent brute-force enumeration: AGREE for k <= 20
  L-9909 survivor counts k<=8 : [1, 1, 2, 3, 4, 8, 13, 19]
  my   independent counts k<=8: [1, 1, 2, 3, 4, 8, 13, 19]   MATCH = True

  k :      s_k       tail_k    s_k <= tail?   exact cert tail*p^p*(k-p)^(k-p) <= k^k
   1:         1            1        yes        n/a (p=k)
   2:         1            1        yes        n/a (p=k)
   3:         2            4        yes        True
   4:         3            5        yes        True
   5:         4            6        yes        True
   6:         8           22        yes        True
   7:        13           29        yes        True
   8:        19           37        yes        True
   9:        38          130        yes        True
  10:        64          176        yes        True
  11:       128          562        yes        True
  12:       226          794        yes        True
  13:       367         1093        yes        True
  14:       734         3473        yes        True
  15:      1295         4944        yes        True
  16:      2114         6885        yes        True
  17:      4228        21778        yes        True
  18:      7495        31180        yes        True
  19:     14990        94184        yes        True
  20:     27328       137980        yes        True
  21:     46611       198440        yes        True
  22:     93222       600370        yes        True
  23:    168807       880970        yes        True
  24:    286581      1271626        yes        True
  25:    573162      3850756        yes        True

  exact chain  s_k <= tail_k <= 2^{k H(p_k/k)} <= 2^{k H(gamma)}:
    holds for every k <= 25 (integer arithmetic, no floats)
  DISPLAY ratio s_k / 2^{kH(gamma)}:
    k= 5: s_k=      4, 2^(kH) ~           26.9, ratio 0.14867
    k=10: s_k=     64, 2^(kH) ~          723.9, ratio 0.08842
    k=15: s_k=   1295, 2^(kH) ~        19475.0, ratio 0.06650
    k=20: s_k=  27328, 2^(kH) ~       523964.9, ratio 0.05216
    k=25: s_k= 573162, 2^(kH) ~     14097032.7, ratio 0.04066
  s_k <= 2^{kH(gamma)} numerically confirmed for k <= 25 too

==============================================================================
D. B_k, E_k
==============================================================================
  closed form B_k == word-level max for k <= 13: AGREE
  B_1..B_8 = ['0', '2', '2', '20/7', '76/5', '76/5', '76/5', '1688/13']
  L-9909's B_1..B_8 = ['0','2','2','20/7','76/5','76/5','76/5','1688/13']
  B_25 = 7329863168/2428309 ~ 3018.505 (DISPLAY), argmax (j,a) = (24, 15)
  B_k nondecreasing: True
  E_k for k=1..12: [[], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
  E_25 = [1]; floor(B_25) = 3018
  adversarial scan n <= 300000, k <= 20: exceptional n exceeding B_k: NONE (L-9908.1(d) not refuted)
  forward containment U_k subset {sigma>k} tested n<=2*10^5, k in {5,10,15}: violations NONE
  strict growth T^j(n) > n on U_12, n <= 5*10^4: violations NONE

==============================================================================
E. TRUE EMPIRICAL DENSITY  #{n <= 10^6 : sigma(n) > k}/10^6  vs  s_k 2^-k
==============================================================================
  k :   count   frac        s_k/2^k      diff*N   predicted diff range
   1:  500000  0.500000   0.500000       +0.0  [    +0.0,     +1.0]
   2:  250001  0.250001   0.250000       +1.0  [    +0.0,     +2.0]
   3:  250001  0.250001   0.250000       +1.0  [    +0.0,     +3.0]
   4:  187501  0.187501   0.187500       +1.0  [    +0.0,     +4.0]
   5:  125001  0.125001   0.125000       +1.0  [    +0.0,     +5.0]
   6:  125001  0.125001   0.125000       +1.0  [    +0.0,     +9.0]
   7:  101562  0.101562   0.101562       -0.5  [    -6.5,     +7.5]
   8:   74219  0.074219   0.074219       +0.2  [    -4.8,    +15.2]
   9:   74219  0.074219   0.074219       +0.2  [    -4.8,    +34.2]
  10:   62501  0.062501   0.062500       +1.0  [   -36.0,    +29.0]
  11:   62501  0.062501   0.062500       +1.0  [   -36.0,    +93.0]
  12:   55178  0.055178   0.055176       +2.2  [   -31.8,   +195.2]
  13:   44802  0.044802   0.044800       +2.2  [   -25.8,   +342.2]
  14:   44802  0.044802   0.044800       +2.2  [   -25.8,   +709.2]
  15:   39518  0.039518   0.039520       -2.3  [  -670.3,   +625.7]
  16:   32257  0.032257   0.032257       -0.1  [  -547.1,  +1567.9]
  17:   32257  0.032257   0.032257       -0.1  [ -2661.1,  +1567.9]
  18:   28587  0.028587   0.028591       -4.2  [ -6106.2,  +1389.8]
  19:   28587  0.028587   0.028591       -4.2  [-13601.2,  +1389.8]
  20:   26057  0.026057   0.026062       -5.0  [-26062.0,  +1267.0]
  21:   22226  0.022226   0.022226       +0.1  [-22225.9, +24386.1]
  22:   22226  0.022226   0.022226       +0.1  [-22225.9, +70997.1]
  23:   20102  0.020102   0.020123      -21.4  [-20123.4, +148684.6]
  24:   17084  0.017084   0.017082       +2.4  [-17081.6, +269500.4]
  25:   17084  0.017084   0.017082       +2.4  [-17081.6, +556081.4]
  exact sandwich s_k*floor(N/2^k) <= count <= s_k*(floor(N/2^k)+1)+#E_k: HOLDS k<=25
  max |count - s_k*N/2^k| = 21.4  (bounded by s_k + #E_k, as Lemma DEN says)
  and |count - s_k N/2^k| <= s_k + #E_k + 1 for every k <= 25: HOLDS

  check d({sigma>k}) <= 2^{-k(1-H(gamma))} on the exact predicted densities:
    s_k 2^-k <= 2^{-k(1-H(gamma))} and < 2^{-1937k/38800} for all k <= 25 OK

==============================================================================
F. TARGETED ATTACKS
==============================================================================
  L-9908.2(a) tested at 3000 random (k, t=p/q in (1/2,1)), k <= 70: 0 failures
  edge cases t=501/1000, 999/1000, 51/100, 97/100 and k=1,2,3: OK
  ceiling equivalence 3^a>=2^j <=> a>=ceil(j*gamma) <=> a>j*gamma: OK for all 1<=j<200, 0<=a<200
  3^a = 2^j never occurs for j <= 2000: OK (consistent with irrationality)
  c=1/2: d_c=0.6309, k0=107, k0*gamma-d_c=66.8786 >= 5k0/8=66.8750  and 3^(k g - d_c)=c 2^k OK
  c=1/10: d_c=2.0959, k0=354, k0*gamma-d_c=221.2532 >= 5k0/8=221.2500  and 3^(k g - d_c)=c 2^k OK
  c=1/3: d_c=1.0000, k0=169, k0*gamma-d_c=105.6271 >= 5k0/8=105.6250  and 3^(k g - d_c)=c 2^k OK
  c=99/100: d_c=0.0091, k0=2, k0*gamma-d_c=1.2527 >= 5k0/8=1.2500  and 3^(k g - d_c)=c 2^k OK
  c=1/1000: d_c=6.2877, k0=1061, k0*gamma-d_c=663.1288 >= 5k0/8=663.1250  and 3^(k g - d_c)=c 2^k OK
  H(1/2)=1.000000 > H(306/485)=0.949957 > H(gamma)=0.949956  (decreasing, so H(gamma) < H(306/485): the direction the proof needs)
  note 5/8 = 0.625 < gamma = 0.630930, so H(5/8) = 0.954434 > H(gamma); used only in L-9908.4(b) where 5/8 is the threshold, correct direction
  A_(1/2) cap [1,3*10^4] = [1, 2]  (expected {1..2}) -> True
  A_(1/4) cap [1,3*10^4] = [1, 2, 3, 4]  (expected {1..4}) -> True

ALL INDEPENDENT CHECKS PASSED
```

#### `v12_sharp.py` (certificate margin ranking + the exact-identity test of §V5)

```python
#!/usr/bin/env python3
"""fable-02-v12: sharper follow-up tests for L-9908."""
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 60

print("--- head certificates, exact values ---")
print("N0a: 3 < 2^2 ?", 3 < 4)
print("N0b: 2 < 3 ?", 2 < 3)
print("N1 : 3^306 < 2^485 ?", 3 ** 306 < 2 ** 485,
      " margin bits =", float((Decimal(485) * Decimal(2).ln()
                               - Decimal(306) * Decimal(3).ln()) / Decimal(2).ln()))
print("     3^306 bit_length", (3 ** 306).bit_length(), " 2^485 bit_length", (2 ** 485).bit_length())
print("N2 : 3^53 > 2^84 ?", 3 ** 53 > 2 ** 84, " 3^53 =", 3 ** 53, " 2^84 =", 2 ** 84,
      " margin bits =", float((Decimal(53) * Decimal(3).ln()
                               - Decimal(84) * Decimal(2).ln()) / Decimal(2).ln()))
print("N6 : 5^25 > 2^58 ?", 5 ** 25 > 2 ** 58, " 5^25 =", 5 ** 25, " 2^58 =", 2 ** 58,
      " margin bits =", float((Decimal(25) * Decimal(5).ln()
                               - Decimal(58) * Decimal(2).ln()) / Decimal(2).ln()))
print("N7 : 3^50 > 2^79 ?", 3 ** 50 > 2 ** 79)
print("N8 : 3^5 < 2^8 ?", 3 ** 5 < 2 ** 8, "(243 < 256)")

print("\n--- ranked certificate margins (|log2 margin|, bits) ---")
rows = [("N0a 3 vs 2^2", 1, 3, 2, 2), ("N1 3^306 vs 2^485", 306, 3, 485, 2),
        ("N2 3^53 vs 2^84", 53, 3, 84, 2), ("N3 485^1e4 vs 2^89219", 10000, 485, 89219, 2),
        ("N4 306^1e4 vs 2^82573", 10000, 306, 82573, 2),
        ("N5 179^1e4 vs 2^74838", 10000, 179, 74838, 2),
        ("N6 5^25 vs 2^58", 25, 5, 58, 2), ("N7 3^50 vs 2^79", 50, 3, 79, 2),
        ("N8 3^5 vs 2^8", 5, 3, 8, 2)]
marg = []
for name, e1, b1, e2, b2 in rows:
    m = (Decimal(e1) * Decimal(b1).ln() - Decimal(e2) * Decimal(b2).ln()) / Decimal(2).ln()
    marg.append((abs(float(m)), name, float(m)))
for a, name, m in sorted(marg):
    print(f"  {a:10.6f}   {name:26s} (signed {m:+.6f})")

print("\n--- EXACT prediction of #{n <= 10^6 : sigma(n) > k} from the theory ---")
KMAX = 25
CEIL = [None]
for j in range(1, KMAX + 1):
    a = 0
    while 3 ** a < 2 ** j:
        a += 1
    CEIL.append(a)


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


N = 10 ** 6
# one pass: for each n record m = min(sigma(n)-1, KMAX) and f = first survivor-failure
# index (None if none within KMAX)
cnt_sigma = [0] * (KMAX + 1)
cnt_surv = [0] * (KMAX + 1)
excep = {k: [] for k in range(1, KMAX + 1)}
for n in range(1, N + 1):
    x, m = n, 0
    while m < KMAX:
        x = T(x)
        if x < n:
            break
        m += 1
    for k in range(1, m + 1):
        cnt_sigma[k] += 1
    a, x, f = 0, n, None
    for j in range(1, KMAX + 1):
        a += x & 1
        x = T(x)
        if a < CEIL[j]:
            f = j
            break
    surv_upto = (f - 1) if f is not None else KMAX
    for k in range(1, surv_upto + 1):
        cnt_surv[k] += 1
    if f is not None:
        for k in range(f, min(m, KMAX) + 1):
            excep[k].append(n)

print("  k :  #{sigma>k}   #U_k cap [1,N]   #E_k cap [1,N]   identity holds?")
allok = True
for k in range(1, KMAX + 1):
    ok = cnt_sigma[k] == cnt_surv[k] + len(excep[k])
    allok &= ok
    print(f"  {k:2d}: {cnt_sigma[k]:8d}    {cnt_surv[k]:8d}        {len(excep[k]):3d}"
          f"   {excep[k] if len(excep[k]) < 6 else '...'}     {ok}")
print("  EXACT identity  #{n<=N: sigma>k} = #(U_k cap [1,N]) + #(E_k cap [1,N])  "
      f"for all k <= 25: {allok}")
assert allok
print("  => U_k subset {sigma>k} (no survivor n with sigma(n)<=k) AND every")
print("     exceptional n is accounted for; E_k cap [1,10^6] = {1} for 2<=k<=25.")
```

#### Output of `v12_sharp.py`

```text
--- head certificates, exact values ---
N0a: 3 < 2^2 ? True
N0b: 2 < 3 ? True
N1 : 3^306 < 2^485 ? True  margin bits = 0.0014747793262084752
     3^306 bit_length 485  2^485 bit_length 486
N2 : 3^53 > 2^84 ? True  3^53 = 19383245667680019896796723  2^84 = 19342813113834066795298816  margin bits = 0.0030125382212776173
N6 : 5^25 > 2^58 ? True  5^25 = 298023223876953125  2^58 = 288230376151711744  margin bits = 0.0482023721840587
N7 : 3^50 > 2^79 ? True
N8 : 3^5 < 2^8 ? True (243 < 256)

--- ranked certificate margins (|log2 margin|, bits) ---
    0.001475   N1 3^306 vs 2^485          (signed -0.001475)
    0.003013   N2 3^53 vs 2^84            (signed +0.003013)
    0.048202   N6 5^25 vs 2^58            (signed +0.048202)
    0.075187   N8 3^5 vs 2^8              (signed -0.075187)
    0.157773   N5 179^1e4 vs 2^74838      (signed +0.157773)
    0.248125   N7 3^50 vs 2^79            (signed +0.248125)
    0.415037   N0a 3 vs 2^2               (signed -0.415037)
    0.590629   N3 485^1e4 vs 2^89219      (signed -0.590629)
    0.878427   N4 306^1e4 vs 2^82573      (signed +0.878427)

--- EXACT prediction of #{n <= 10^6 : sigma(n) > k} from the theory ---
  k :  #{sigma>k}   #U_k cap [1,N]   #E_k cap [1,N]   identity holds?
   1:   500000      500000          0   []     True
   2:   250001      250000          1   [1]     True
   3:   250001      250000          1   [1]     True
   4:   187501      187500          1   [1]     True
   5:   125001      125000          1   [1]     True
   6:   125001      125000          1   [1]     True
   7:   101562      101561          1   [1]     True
   8:    74219       74218          1   [1]     True
   9:    74219       74218          1   [1]     True
  10:    62501       62500          1   [1]     True
  11:    62501       62500          1   [1]     True
  12:    55178       55177          1   [1]     True
  13:    44802       44801          1   [1]     True
  14:    44802       44801          1   [1]     True
  15:    39518       39517          1   [1]     True
  16:    32257       32256          1   [1]     True
  17:    32257       32256          1   [1]     True
  18:    28587       28586          1   [1]     True
  19:    28587       28586          1   [1]     True
  20:    26057       26056          1   [1]     True
  21:    22226       22225          1   [1]     True
  22:    22226       22225          1   [1]     True
  23:    20102       20101          1   [1]     True
  24:    17084       17083          1   [1]     True
  25:    17084       17083          1   [1]     True
  EXACT identity  #{n<=N: sigma>k} = #(U_k cap [1,N]) + #(E_k cap [1,N])  for all k <= 25: True
  => U_k subset {sigma>k} (no survivor n with sigma(n)<=k) AND every
     exceptional n is accounted for; E_k cap [1,10^6] = {1} for 2<=k<=25.
```

#### `v12_extra.py` (fourth check of N1/N2; exact integer form of L-9908.2(a))

```python
from math import comb
from fractions import Fraction
# N1 re-verified a third way: exact difference
d = 2**485 - 3**306
print("N1: 2^485 - 3^306 =", d, "; positive?", d > 0)
print("N1: 3^306 bit_length =", (3**306).bit_length(), "(=485 => 3^306 < 2^485)")
print("N1: ratio 2^485/3^306 (float) =", float(Fraction(2**485, 3**306)))
# N2 third way
print("N2: 3^53 - 2^84 =", 3**53 - 2**84, "positive?", 3**53 > 2**84)
# exact integer form of L-9908.2(a) at t = 5/8 (load-bearing in L-9908.4(b)):
# 2^{8m H(5/8)} = 8^{8m} / (5^{5m} 3^{3m});  test  Sum * 5^{5m} * 3^{3m} <= 8^{8m}
bad = []
for m in range(1, 51):
    k = 8*m
    M = 5*k//8
    S = sum(comb(k, j) for j in range(M, k+1))
    if not (S * 5**(5*m) * 3**(3*m) <= 8**(8*m)):
        bad.append(k)
print("exact integer test of 2(a) at t=5/8, k=8..400 step 8:", "FAIL"+str(bad) if bad else "all pass")
# exact integer form at t = p/k rational with denominator k (covers 2(c) at t=gamma via p=ceil(k gamma))
bad2 = []
for k in range(2, 300):
    for p in range(k//2+1, k):
        S = sum(comb(k, j) for j in range(p, k+1))
        if not (S * p**p * (k-p)**(k-p) <= k**k):
            bad2.append((k, p))
print("exact test  Sum_{j>=p} C(k,j) * p^p (k-p)^(k-p) <= k^k  for all 2<=k<300, k/2<p<k:",
      "FAIL "+str(bad2[:5]) if bad2 else "all pass (%d instances)" % sum(1 for k in range(2,300) for p in range(k//2+1,k)))
```

#### Output of `v12_extra.py`

```text
N1: 2^485 - 3^306 = 102065376400825306534437391838939444403106454408085639783964140880896699835673006969445010534504805079858638689074275443284439551032910142670903 ; positive? True
N1: 3^306 bit_length = 485 (=485 => 3^306 < 2^485)
N1: ratio 2^485/3^306 (float) = 1.0010227617964118
N2: 3^53 - 2^84 = 40432553845953101497907 positive? True
exact integer test of 2(a) at t=5/8, k=8..400 step 8: all pass
exact test  Sum_{j>=p} C(k,j) * p^p (k-p)^(k-p) <= k^k  for all 2<=k<300, k/2<p<k: all pass (22201 instances)
```

---

*Signed: fable-02-v12, 2026-07-25 (independent adversarial verifier). Verdict: PASS;
status upgraded to PROVED. Scripts: `v12_verify.py`, `v12_sharp.py`, `v12_extra.py`
(scratchpad; full text and output above).*
