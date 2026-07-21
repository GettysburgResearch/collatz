# L-9903 — Exact affine iteration formula for $T$ with sharp remainder bounds

```text
Claim ID:      L-9903
Title:         Exact affine iteration formula for T with sharp two-sided remainder bounds
Status:        PROVED
Authoring agent:   fable-02-p3
Reviewing agents:  fable-02-v3 (adversarial review 2026-07-21: PASS)
Created:       2026-07-21
Last updated:  2026-07-21 (status upgraded after independent adversarial review)
Dependencies:  NOTATION.md (D-9902 shortcut map T, D-9906 parity vector v_i and a_k)
Scope:         All n in Z^+ and all k >= 0; word-level statements over all of {0,1}^k.
Related counterexample candidates: none
```

---

## Statement

Throughout, $T$ is the shortcut map (D-9902), $v_i(n) := T^i(n) \bmod 2$ and
$a_k(n) := \sum_{i=0}^{k-1} v_i(n)$ are as in D-9906, and empty sums are $0$
(so $a_0(n) = 0$). Define the **remainder sequence** of $n \in \mathbb{Z}^+$ by
$$\rho_0(n) := 0, \qquad \rho_{i+1}(n) := 3^{v_i(n)}\,\rho_i(n) + v_i(n)\,2^{i} \quad (i \ge 0).$$

More generally, for an arbitrary finite binary word $w = (w_0, \dots, w_{k-1}) \in \{0,1\}^k$
define the **word-level remainder** $\rho(w)$ by the same recursion with $w_i$ in place of
$v_i(n)$: set $r_0 := 0$, $r_{i+1} := 3^{w_i} r_i + w_i 2^i$, and $\rho(w) := r_k$. Write
$|w|_1 := \sum_{i<k} w_i$ for the number of ones, and for $0 \le i < k$
$$s_i(w) := \#\{\, j : i < j < k,\ w_j = 1 \,\} = \sum_{j=i+1}^{k-1} w_j$$
for the number of ones **strictly after** position $i$. The empty word $\varepsilon$ (case
$k = 0$) has $\rho(\varepsilon) = 0$.

**L-9903.1 (iteration formula).** For all $n \in \mathbb{Z}^+$ and all integers $k \ge 0$:
$$T^k(n) \;=\; \frac{3^{a_k(n)}\, n + \rho_k(n)}{2^k}.$$
Equivalently (denominator cleared, an identity between positive integers):
$2^k\, T^k(n) = 3^{a_k(n)} n + \rho_k(n)$.

**L-9903.2 (closed form; word-dependence).** For all $k \ge 0$ and all
$w \in \{0,1\}^k$:
$$\rho(w) \;=\; \sum_{\substack{0 \le i < k \\ w_i = 1}} 3^{\,s_i(w)}\, 2^{i},$$
and consequently, for all $n \in \mathbb{Z}^+$,
$$\rho_k(n) \;=\; \rho\big(v_0(n), \dots, v_{k-1}(n)\big)
\;=\; \sum_{\substack{0 \le i < k \\ v_i(n) = 1}} 3^{\,a_k(n) - a_{i+1}(n)}\, 2^{i}.$$
In particular $\rho_k(n)$ depends only on the parity word $(v_0(n), \dots, v_{k-1}(n))$;
the exponent $a_k - a_{i+1} = \sum_{j=i+1}^{k-1} v_j = s_i$ counts the odd steps occurring
strictly **after** step $i$.

**L-9903.3 (sharp two-sided bounds; equality characterization).** Fix $k \ge 0$ and
$0 \le a \le k$, and let $W_{k,a} := \{ w \in \{0,1\}^k : |w|_1 = a \}$.

1. If $a = 0$ then $W_{k,0} = \{0^k\}$ and $\rho(0^k) = 0$.
2. If $a \ge 1$ then for every $w \in W_{k,a}$:
$$3^a - 2^a \;\le\; \rho(w) \;\le\; 2^{\,k-a}\,\big(3^a - 2^a\big),$$
with **equality on the left exactly for** $w = 1^a 0^{\,k-a}$ (all ones first) and
**equality on the right exactly for** $w = 0^{\,k-a} 1^a$ (all ones last). (When $a = k$
these two words coincide and the two bounds agree: $\rho(1^k) = 3^k - 2^k$.)

Consequently, for every $n \in \mathbb{Z}^+$ and $k \ge 0$, writing $a = a_k(n)$:
$\rho_k(n) = 0$ if $a = 0$, and $3^a - 2^a \le \rho_k(n) \le 2^{k-a}(3^a - 2^a)$ if
$a \ge 1$. In particular $\rho_k(n) \ge 0$ always, and $\rho_k(n) = 0 \iff a_k(n) = 0$.

**L-9903.4 (growth envelope).** For all $n \in \mathbb{Z}^+$ and $k \ge 0$:
$$\frac{3^{a_k(n)}}{2^k}\, n \;\le\; T^k(n) \;\le\; \frac{3^{a_k(n)}}{2^k}\, n
\;+\; \left(\tfrac{3}{2}\right)^{a_k(n)} - 1.$$
(Sharper lower-bound form: $T^k(n) \ge 3^{a_k} n/2^k + (3^{a_k} - 2^{a_k})/2^k$.)

**L-9903.5 (periodicity bridge).** For all $n \in \mathbb{Z}^+$ and $K \ge 1$:
$$T^K(n) = n \quad\Longleftrightarrow\quad n\,\big(2^K - 3^{a_K(n)}\big) = \rho_K(n).$$

**Remark R-9903-A (word realization; classical, proved below).** For every $k \ge 0$, the
map $n \bmod 2^k \mapsto (v_0(n), \dots, v_{k-1}(n))$ is a well-defined bijection
$\mathbb{Z}/2^k\mathbb{Z} \to \{0,1\}^k$. Hence every word in L-9903.3 — in particular each
extremizer — is realized by exactly one residue class of positive integers, so the bounds in
L-9903.3 are attained by actual trajectories and are genuinely sharp at the integer level.

---

## Definitions

- $T(n) = n/2$ ($n$ even), $(3n+1)/2$ ($n$ odd) — D-9902. $T^0(n) = n$.
- $v_i(n) = T^i(n) \bmod 2$, $a_k(n) = \sum_{i<k} v_i(n)$ — D-9906. $a_0 = 0$; $a_k - a_{i+1} = \sum_{j=i+1}^{k-1} v_j$ for $0 \le i < k$.
- $\rho_k(n)$, word-level $\rho(w)$, $|w|_1$, $s_i(w)$: defined in the Statement above. These are the only nonstandard notations in this file.
- $1^a 0^{k-a}$ denotes the word with $w_i = 1$ for $0 \le i \le a-1$ and $w_i = 0$ for $a \le i \le k-1$; $0^{k-a} 1^a$ the word with $w_i = 0$ for $0 \le i \le k-a-1$ and $w_i = 1$ for $k-a \le i \le k-1$.
- Empty sums are $0$; empty products are $1$ (NOTATION.md conventions).

---

## Motivation

This is the workhorse identity used across the project: essentially every quantitative
statement about $T$-trajectories factors through the affine form
$T^k(n) = (3^{a_k} n + \rho_k)/2^k$.

- Issue #9 displays the $S$-form of this identity for cycle synthesis; L-9903.5 is exactly
  the $T$-form cycle equation feeding that program (the $S$-form Diophantine treatment is
  L-9905, in progress by another agent).
- Issue #4's amplifier algebra and issue #21's foundry both build on affine parity-block
  formulas: a parity block of length $k$ acts on inputs as $n \mapsto (3^a n + \rho)/2^k$
  with $(a, \rho)$ determined by the block's word, which is precisely L-9903.1–.2 together
  with R-9903-A (each block realized on one residue class mod $2^k$).
- The sharp two-sided bounds on $\rho_k$ (L-9903.3) and the resulting envelope (L-9903.4)
  feed the divergence-density threshold (L-9907) and the planned stopping-time density
  lemma (L-9908): the envelope shows $T^k(n)/n$ is controlled by $3^{a_k}/2^k$ up to an
  additive error at most $(3/2)^{a_k} - 1$, uniformly in $n$, so density arguments about
  $a_k$ transfer to growth statements about trajectories. The equality characterization
  identifies which parity words extremize the remainder — the "ones-first" and "ones-last"
  blocks — which is exactly the structural information a counterexample-construction agent
  needs when engineering blocks with maximal or minimal drift.

---

## Proof

### L-9903.1 (iteration formula)

Fix $n \in \mathbb{Z}^+$. We prove by induction on $k \ge 0$ the cleared-denominator form
$$P(k): \qquad 2^k\, T^k(n) = 3^{a_k(n)}\, n + \rho_k(n).$$

**Base $k = 0$.** $2^0 T^0(n) = n$ and $3^{a_0} n + \rho_0 = 3^0 n + 0 = n$ (using
$a_0 = 0$ as an empty sum and $\rho_0 = 0$ by definition). So $P(0)$ holds.

**Inductive step.** Assume $P(k)$ and write $m := T^k(n)$, $a := a_k(n)$,
$\rho := \rho_k(n)$, $v := v_k(n) = m \bmod 2$. By D-9906,
$a_{k+1}(n) = a + v$; by the defining recursion, $\rho_{k+1}(n) = 3^v \rho + v\,2^k$.

*Case $v = 0$ ($m$ even).* Then $T^{k+1}(n) = m/2$, so
$$2^{k+1} T^{k+1}(n) = 2^k m = 3^a n + \rho = 3^{a_{k+1}(n)} n + \rho_{k+1}(n),$$
since $a_{k+1} = a$ and $\rho_{k+1} = 3^0\rho + 0 = \rho$.

*Case $v = 1$ ($m$ odd).* Then $T^{k+1}(n) = (3m+1)/2$, so
$$2^{k+1} T^{k+1}(n) = 2^k (3m + 1) = 3\,(2^k m) + 2^k
= 3\,(3^a n + \rho) + 2^k = 3^{a+1} n + \big(3\rho + 2^k\big)
= 3^{a_{k+1}(n)} n + \rho_{k+1}(n).$$

In both cases $P(k+1)$ holds. By induction, $P(k)$ holds for all $k \ge 0$, and dividing
by $2^k$ gives the displayed formula. $\blacksquare$

*(Edge case note: for $k = 0$ the formula reads $T^0(n) = (n + 0)/1 = n$, correct. The
formula also shows a posteriori that $3^{a_k} n + \rho_k$ is always divisible by $2^k$,
since $T^k(n)$ is a positive integer.)*

### L-9903.2 (closed form; word-dependence)

We prove, by induction on $k \ge 0$, that for every word $w \in \{0,1\}^k$,
$$Q(k): \qquad \rho(w) = \sum_{\substack{0 \le i < k \\ w_i = 1}} 3^{\,s_i(w)}\, 2^i .$$

**Base $k = 0$.** $w = \varepsilon$, $\rho(\varepsilon) = r_0 = 0$, and the right side is an
empty sum $= 0$. $Q(0)$ holds.

**Inductive step.** Let $w = (w_0, \dots, w_k) \in \{0,1\}^{k+1}$ and let
$w' := (w_0, \dots, w_{k-1})$ be its length-$k$ prefix. The recursion computes
$r_0, \dots, r_k$ identically for $w$ and $w'$ (it only consults $w_0, \dots, w_{k-1}$ up
to step $k$), so $r_k = \rho(w')$ and
$$\rho(w) = r_{k+1} = 3^{w_k}\, \rho(w') + w_k\, 2^k .$$
For $0 \le i < k$, the count of ones strictly after $i$ satisfies
$s_i(w) = s_i(w') + w_k$ (position $k$ is strictly after every $i < k$, and positions
$i+1, \dots, k-1$ agree between $w$ and $w'$); also $s_k(w) = 0$ (no positions after $k$
in $w$). Applying $Q(k)$ to $w'$:
$$3^{w_k}\rho(w')
= \sum_{\substack{i < k \\ w_i = 1}} 3^{\,s_i(w') + w_k}\, 2^i
= \sum_{\substack{i < k \\ w_i = 1}} 3^{\,s_i(w)}\, 2^i,$$
and the extra term $w_k 2^k$ equals $3^{\,s_k(w)} 2^k = 2^k$ when $w_k = 1$ and $0$ when
$w_k = 0$, i.e., it is exactly the $i = k$ term of the claimed sum. Adding gives $Q(k+1)$.
By induction, $Q(k)$ holds for all $k$. $\blacksquare$

**Word-dependence and the integer-level formula.** The recursions defining $\rho_k(n)$ and
$\rho(w)$ coincide upon substituting $w_i = v_i(n)$; a trivial induction on $k$ gives
$\rho_k(n) = \rho(v_0(n), \dots, v_{k-1}(n))$ for all $k$. Thus $\rho_k(n)$ is a function
of the parity word alone. Finally, for $w_i = v_i(n)$ we have
$s_i(w) = \sum_{j=i+1}^{k-1} v_j(n) = a_k(n) - a_{i+1}(n)$ (telescoping the definition of
$a_k$), which yields the displayed integer-level closed form. $\blacksquare$

### L-9903.3 (sharp bounds; equality characterization)

Throughout this subsection, fix $k \ge 0$ and work with the word-level function
$\rho : \{0,1\}^k \to \mathbb{Z}_{\ge 0}$ in its closed form (L-9903.2):
$\rho(w) = \sum_{i : w_i = 1} 3^{s_i(w)} 2^i$. Nonnegativity of every term is immediate.

**(0) Case $a = 0$.** The unique word with no ones is $0^k$, and $\rho(0^k) = 0$ (empty
sum). Conversely, if $|w|_1 \ge 1$, say $w_i = 1$, then $\rho(w) \ge 3^{s_i(w)} 2^i \ge 1 > 0$.
So $\rho(w) = 0 \iff |w|_1 = 0$. (For $k = 0$ this is the statement $\rho(\varepsilon)=0$.)

Now fix $1 \le a \le k$ and restrict to $W_{k,a}$.

**(i) Values at the two extreme words.**

*Ones-first word $u := 1^a 0^{k-a}$.* The ones sit at positions $0, \dots, a-1$, and for
$0 \le i \le a-1$ the ones strictly after $i$ are exactly positions $i+1, \dots, a-1$, so
$s_i(u) = a - 1 - i$. Hence, by the geometric sum
$\sum_{i=0}^{a-1} 3^{a-1-i} 2^i = 3^{a-1} \sum_{i=0}^{a-1} (2/3)^i
= 3^{a-1} \cdot \frac{1 - (2/3)^a}{1/3} = 3^a\big(1 - (2/3)^a\big) = 3^a - 2^a$:
$$\rho(u) = \sum_{i=0}^{a-1} 3^{\,a-1-i}\, 2^i = 3^a - 2^a.$$
(Equivalently: $(3-2)\sum_{i=0}^{a-1} 3^{a-1-i}2^i$ telescopes to $3^a - 2^a$; no
non-integer manipulation is needed.)

*Ones-last word $z := 0^{k-a} 1^a$.* The ones sit at positions $k-a, \dots, k-1$. Writing
$i = k - a + j$ with $0 \le j \le a-1$, the ones strictly after $i$ are positions
$i+1, \dots, k-1$, so $s_i(z) = a - 1 - j$. Hence
$$\rho(z) = \sum_{j=0}^{a-1} 3^{\,a-1-j}\, 2^{\,k-a+j}
= 2^{\,k-a} \sum_{j=0}^{a-1} 3^{\,a-1-j}\, 2^{j} = 2^{\,k-a}\,\big(3^a - 2^a\big).$$

When $a = k$, $u = z = 1^k$ and both formulas give $3^k - 2^k$, consistently.

**(ii) Adjacent-swap lemma.** *Let $w \in W_{k,a}$ have a "$01$" factor: $w_p = 0$,
$w_{p+1} = 1$ for some $0 \le p \le k-2$. Let $w'$ be $w$ with these two entries swapped
($w'_p = 1$, $w'_{p+1} = 0$, $w'_q = w_q$ for $q \notin \{p, p+1\}$; the one moves one
position earlier). Then $w' \in W_{k,a}$ and*
$$\rho(w') = \rho(w) - 3^{\,s}\, 2^{\,p} \;<\; \rho(w),
\qquad \text{where } s := \#\{\, j > p+1 : w_j = 1 \,\}.$$

*Proof.* $|w'|_1 = |w|_1 = a$ since the swap permutes entries. Compare the closed-form
sums term by term over positions $q$ carrying a one.

- *Positions $q < p$ with $w_q = 1$.* Then $w'_q = w_q = 1$. The count $s_q$ ranges over
  positions $j > q$; the swap changes entries only at $p, p+1$, both $> q$, and it
  preserves the total number of ones on $\{p, p+1\}$ (namely one). Hence
  $s_q(w') = s_q(w)$ and the term $3^{s_q} 2^q$ is unchanged.
- *Positions $q > p+1$ with $w_q = 1$.* Then $w'_q = w_q = 1$, and $s_q$ depends only on
  entries at positions $> q > p+1$, which are untouched. Term unchanged.
- *The moved one.* In $w$ it contributes at position $p+1$ with exponent
  $s_{p+1}(w) = \#\{ j > p+1 : w_j = 1 \} = s$. In $w'$ it contributes at position $p$
  with exponent $s_p(w') = \#\{ j > p : w'_j = 1 \} = [\,w'_{p+1} = 1\,] +
  \#\{ j > p+1 : w'_j = 1 \} = 0 + s = s$, using $w'_{p+1} = 0$ and $w'_j = w_j$ for
  $j > p+1$. So this term changes from $3^{s} 2^{p+1}$ to $3^{s} 2^{p}$.
- *Position $p$ in $w$ and position $p+1$ in $w'$ carry zeros* and contribute to neither sum.

Summing: $\rho(w') - \rho(w) = 3^s 2^p - 3^s 2^{p+1} = -3^s 2^p < 0$. $\square$

By symmetry (reading the same computation in reverse), swapping a "$10$" factor to "$01$"
(moving a one one position **later**) **strictly increases** $\rho$, by the same amount
$3^s 2^p$ where $p$ is the position of the factor and $s$ the number of ones strictly
after position $p+1$.

**(iii) Extremality and uniqueness via sorting.**

*Structure of swap-terminal words.* If $w \in W_{k,a}$ has **no** "$01$" factor, then
$w = 1^a 0^{k-a}$: indeed, "no $01$ factor" means $w_p = 0 \Rightarrow w_{p+1} = 0$ for
all $p \le k-2$, so the set of positions carrying $0$ is upward closed; with exactly $a$
ones this forces $w = 1^a 0^{k-a}$. Dually, if $w$ has no "$10$" factor, the set of
positions carrying $1$ is upward closed and $w = 0^{k-a} 1^a$.

*Termination.* Define the moment $\mu(w) := \sum_{i : w_i = 1} i \in \mathbb{Z}_{\ge 0}$.
Each "$01 \to 10$" swap decreases $\mu$ by exactly $1$ and keeps $|w|_1 = a$. Since $\mu$
is a nonnegative integer, any maximal sequence of such swaps starting from
$w \in W_{k,a}$ is finite and terminates at a word of $W_{k,a}$ with no "$01$" factor,
i.e., at $1^a 0^{k-a}$.

*Minimum.* Let $w \in W_{k,a}$ with $w \ne 1^a 0^{k-a}$. Then $w$ has a "$01$" factor (by
the structure claim), so a maximal swap sequence from $w$ has length $\ge 1$; by the
adjacent-swap lemma each swap strictly decreases $\rho$, and the sequence ends at
$1^a 0^{k-a}$. Hence
$$\rho(w) > \rho(1^a 0^{k-a}) = 3^a - 2^a .$$
Thus $\rho \ge 3^a - 2^a$ on $W_{k,a}$ with equality **only** at $1^a 0^{k-a}$, and
equality does hold there by (i). Minimum value and uniqueness of the minimizer are proved.

*Maximum.* Dually, each "$10 \to 01$" swap increases $\mu$ by $1$ (bounded above by the
moment of $0^{k-a}1^a$, namely $\sum_{i=k-a}^{k-1} i$, since $\mu$ on $W_{k,a}$ is
maximized there — or simply: $\mu \le k a$ always, so termination again holds) and
strictly increases $\rho$; a maximal sequence of such swaps terminates at the unique
"$10$"-free word $0^{k-a} 1^a$. Hence for $w \ne 0^{k-a} 1^a$,
$\rho(w) < \rho(0^{k-a} 1^a) = 2^{k-a}(3^a - 2^a)$, giving the upper bound with equality
exactly at $0^{k-a} 1^a$. $\blacksquare$

*(Edge cases: $a = k$ makes $W_{k,k} = \{1^k\}$ a singleton; both characterizations hold
vacuously-uniquely and the bounds coincide. $a \ge 1$ with $k - a \ge 1$ gives
$2^{k-a} \ge 2$ and $3^a - 2^a \ge 1$, so the minimum is strictly below the maximum and
the two extremizers are distinct words, as they must be.)*

**Integer-level consequence.** For $n \in \mathbb{Z}^+$ and $k \ge 0$, the word
$w = (v_0(n), \dots, v_{k-1}(n))$ lies in $W_{k, a_k(n)}$ and $\rho_k(n) = \rho(w)$
(L-9903.2), so the stated bounds on $\rho_k(n)$ follow. $\blacksquare$

### Remark R-9903-A (word realization — every word occurs)

*For each $k \ge 0$, the map $\varphi_k : \mathbb{Z}/2^k\mathbb{Z} \to \{0,1\}^k$,
$n \bmod 2^k \mapsto (v_0(n), \dots, v_{k-1}(n))$, is well-defined and bijective.*

*Proof (induction on $k$).* $k = 0$ is trivial (one residue, one empty word). Assume
$\varphi_k$ is well-defined and bijective. Let $m \equiv n \pmod{2^{k+1}}$ with
$m, n \in \mathbb{Z}^+$. Then $m \equiv n \pmod{2^k}$, so by the inductive hypothesis
their length-$k$ words agree; write $a := a_k(m) = a_k(n)$ and
$\rho := \rho_k(m) = \rho_k(n)$ (equal because $\rho_k$ depends only on the word,
L-9903.2). By L-9903.1,
$$T^k(m) - T^k(n) = \frac{3^a (m - n)}{2^k},$$
an integer times $3^a$: precisely, $m - n = 2^{k+1} t$ gives
$T^k(m) - T^k(n) = 3^a \cdot 2t$, which is **even**, so $v_k(m) = v_k(n)$ and
$\varphi_{k+1}$ is well-defined. For injectivity: if $m \equiv n \pmod{2^k}$ but
$m \not\equiv n \pmod{2^{k+1}}$, then $m - n \equiv 2^k \pmod{2^{k+1}}$, so
$T^k(m) - T^k(n) = 3^a (m-n)/2^k$ is an **odd** integer, whence $v_k(m) \ne v_k(n)$;
combined with injectivity of $\varphi_k$ on the first $k$ coordinates, $\varphi_{k+1}$ is
injective, and bijective by cardinality ($\#\mathbb{Z}/2^{k+1}\mathbb{Z} = 2^{k+1} =
\#\{0,1\}^{k+1}$). $\square$

*(Positive representatives: every residue class mod $2^k$ contains positive integers, e.g.
its representative in $\{1, \dots, 2^k\}$, so "realized by exactly one residue class of
positive integers" is justified. This remark is classical (Terras 1976 / Everett 1977); it
is re-proved here inline to keep the file self-contained, and is used in this file only
for the sharpness commentary, not for L-9903.3 itself.)*

### L-9903.4 (growth envelope)

Fix $n, k$ and write $a := a_k(n)$. By L-9903.1,
$T^k(n) = 3^a n / 2^k + \rho_k(n)/2^k$.

*Lower bound.* $\rho_k(n) \ge 0$ by L-9903.3 (it is $0$ if $a = 0$ and
$\ge 3^a - 2^a \ge 1 > 0$ if $a \ge 1$), so $T^k(n) \ge 3^a n / 2^k$. The sharper form
$T^k(n) \ge 3^a n/2^k + (3^a - 2^a)/2^k$ follows from $\rho_k(n) \ge 3^a - 2^a$, which
holds for $a \ge 1$ by L-9903.3 and for $a = 0$ trivially ($3^0 - 2^0 = 0 = \rho_k$).

*Upper bound.* If $a = 0$ then $\rho_k(n) = 0$ and $(3/2)^0 - 1 = 0$, so the bound holds
with equality in the $\rho$-term. If $a \ge 1$, L-9903.3 gives
$\rho_k(n) \le 2^{k-a}(3^a - 2^a)$, hence
$$\frac{\rho_k(n)}{2^k} \;\le\; \frac{2^{\,k-a}\,(3^a - 2^a)}{2^k}
\;=\; \frac{3^a - 2^a}{2^a} \;=\; \left(\tfrac32\right)^{a} - 1 .$$
(Equivalently $(3/2)^a\big(1 - (2/3)^a\big) = (3/2)^a - 1$; the two expressions in the
Statement above agree.) Therefore
$T^k(n) \le 3^a n/2^k + (3/2)^a - 1$. $\blacksquare$

*(Note the upper bound is uniform in $k$ for fixed $a$: the additive error depends only on
the number of odd steps, not on the trajectory length. Sharpness: by R-9903-A the word
$0^{k-a}1^a$ is realized by a residue class, and on it $\rho_k/2^k = (3/2)^a - 1$ exactly,
so the additive constant $(3/2)^{a} - 1$ cannot be improved.)*

### L-9903.5 (periodicity bridge)

Fix $n \in \mathbb{Z}^+$ and $K \ge 1$, and write $a := a_K(n)$, $\rho := \rho_K(n)$. By
L-9903.1 (cleared form), $2^K\, T^K(n) = 3^{a} n + \rho$. Hence
$$T^K(n) = n
\;\Longleftrightarrow\; 2^K n = 3^{a} n + \rho
\;\Longleftrightarrow\; n\,(2^K - 3^{a}) = \rho . \qquad \blacksquare$$

*Remark (no further proof claimed beyond the equivalence above).* This is the cycle
equation in $T$-form. Two immediate observations: since $n \ge 1$ and (by L-9903.3)
$\rho > 0$ whenever $a \ge 1$, a $T$-periodic $n$ with at least one odd step forces
$2^K > 3^{a}$, i.e. $a < \gamma K$ with $\gamma = \log_3 2$ as in NOTATION.md; and then
$n = \rho_K(n)/(2^K - 3^{a_K(n)})$, so a $T$-cycle is completely determined by its parity
word. The $S$-form Diophantine treatment (exponent tuples $(a_1, \dots, a_m)$ of D-9908)
is the subject of L-9905, in progress by another agent. Trivial-cycle check: $n = 1$,
$K = 2$, word $(1,0)$, $a_2 = 1$, $\rho_2 = 1$, and $1 \cdot (2^2 - 3^1) = 1 = \rho_2$. ✓

---

## Dependency audit

- **D-9902** (shortcut map $T$): used in the case split of the induction in L-9903.1 and
  in the definition of trajectories throughout.
- **D-9906** (parity vector $v_i$, count $a_k$): used to define $\rho_k$, in the identity
  $a_{k+1} = a_k + v_k$ (inductive step of L-9903.1), and in the telescoping
  $a_k - a_{i+1} = \sum_{j=i+1}^{k-1} v_j$ (L-9903.2).
- **NOTATION.md conventions**: empty sums $= 0$ (base cases $k = 0$, $a_0 = 0$).
- No other repository claims are used. R-9903-A is classical (Terras 1976, Everett 1977)
  but is fully re-proved inline from L-9903.1–.2; nothing is imported from literature
  without proof. No dependency on L-9905/L-9907/L-9908 (those depend on this file, not
  conversely — no circularity).

## Gap audit

- *Hidden finiteness assumptions:* none; every statement is for a fixed finite $k$ and is
  proved by finite induction. No infinite limits are taken anywhere.
- *Unjustified induction:* both inductions (L-9903.1 over $k$ for fixed $n$; L-9903.2 over
  word length) have explicit bases at $k = 0$ and steps that consult only the inductive
  hypothesis plus one application of the recursion/definition.
- *Boundary cases:* $k = 0$ ($\rho_0 = 0$, $a_0 = 0$, empty word) checked in every base
  case; $a_k = 0$ handled separately in L-9903.3(0) and in both bounds of L-9903.4;
  $a_k = k$ (all-ones word) noted: $W_{k,k}$ is a singleton, both extremizers coincide,
  bounds agree at $3^k - 2^k$. The swap lemma requires $k \ge 2$ to have a factor at all;
  for $k \le 1$ every $W_{k,a}$ is a singleton and (iii) is vacuous, which the sorting
  argument handles automatically (no word $\ne$ extremizer exists).
- *Division safety:* L-9903.1 is proved in cleared-denominator form; divisibility of
  $3^{a_k} n + \rho_k$ by $2^k$ is a consequence, not an assumption. L-9903.5 does not
  divide by $2^K - 3^{a_K}$ (which can be zero only if $2^K = 3^{a_K}$, impossible for
  $K \ge 1$; but the equivalence as stated needs no such discussion).
- *Empirical vs universal:* the Adversarial tests section is labeled finite verification
  and carries no probative weight; all universal claims are proved symbolically above.
- *Word-level vs integer-level:* L-9903.3's equality characterization is a statement about
  the function $\rho$ on all of $\{0,1\}^k$. That every word (hence each extremizer) is
  realized by an integer is *not needed* for the bounds on $\rho_k(n)$ (a trajectory's
  word is *some* word, so the universal word-level bounds apply); realization is proved
  separately in R-9903-A and used only to assert attainment/sharpness at integer level.
- *Circularity:* R-9903-A uses L-9903.1 and L-9903.2 only; L-9903.1–.5 do not use
  R-9903-A. No cycle.
- *Nonuniform estimates:* the constants in L-9903.4 depend only on $a_k$, uniformly in $n$
  and $k$; this uniformity is exactly what the proof delivers ($2^{k-a}(3^a-2^a)/2^k$
  collapses to a $k$-free expression).
- *Assumptions equivalent to Collatz:* none; every statement is an unconditional identity
  or inequality about finitely many steps of $T$.

## Adversarial tests

**Finite verification only — not proof.** Script (exact integer arithmetic throughout; no
floating point):
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/verify_L9903.py`,
run with `python3 verify_L9903.py` (Python 3, standard library only). Reproduced in full:

```python
#!/usr/bin/env python3
# Adversarial finite verification for L-9903 (exact integer arithmetic only).
# Agent: fable-02-p3. Date: 2026-07-21.
#
# Part 1: L-9903.1 (iteration formula), L-9903.2 (closed form), L-9903.4
#         (envelope), L-9903.5 (cycle equivalence) for all 1 <= n <= 3000,
#         0 <= k <= 40.
# Part 2: word-level checks for all words of length k <= 14:
#         recursion == closed form, sharp bounds of L-9903.3, uniqueness of
#         both extremizers, and realization of every word by exactly one
#         residue class mod 2^k (Terras bijection, finite check).

import sys

def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def word_of(n, k):
    w = []
    m = n
    for _ in range(k):
        w.append(m & 1)
        m = T(m)
    return tuple(w)

def rho_rec(w):
    """rho via the recursion rho_{i+1} = 3^{w_i} rho_i + w_i 2^i."""
    r = 0
    for i, wi in enumerate(w):
        r = (3 ** wi) * r + wi * (2 ** i)
    return r

def rho_closed(w):
    """rho via the closed form: sum over i with w_i=1 of 3^{s_i} 2^i,
    s_i = number of ones strictly after position i."""
    total = 0
    for i in range(len(w)):
        if w[i] == 1:
            s = sum(w[i + 1:])
            total += (3 ** s) * (2 ** i)
    return total

# ---------------- Part 1 ----------------
N_MAX, K_MAX = 3000, 40
checks1 = 0
for n in range(1, N_MAX + 1):
    m, a, rho = n, 0, 0
    wlist = []
    for k in range(0, K_MAX + 1):
        # L-9903.1 in cleared-denominator form: 2^k * T^k(n) = 3^a n + rho
        assert (2 ** k) * m == (3 ** a) * n + rho, (n, k)
        # L-9903.2: recursion value equals closed form on the realized word
        assert rho == rho_closed(tuple(wlist)), (n, k)
        # L-9903.3 lower bound at integer level, and rho == 0 iff a == 0
        assert rho >= (3 ** a) - (2 ** a), (n, k)
        assert (rho == 0) == (a == 0), (n, k)
        # L-9903.4 envelope, exact form: 0 <= rho and rho*2^a <= 2^k(3^a-2^a)
        assert rho >= 0 and rho * (2 ** a) <= (2 ** k) * ((3 ** a) - (2 ** a)), (n, k)
        # L-9903.5: T^k(n) == n  <=>  n(2^k - 3^a) == rho   (k >= 1)
        if k >= 1:
            assert (m == n) == (n * ((2 ** k) - (3 ** a)) == rho), (n, k)
        checks1 += 1
        # advance one T-step
        v = m & 1
        wlist.append(v)
        rho = (3 ** v) * rho + v * (2 ** k)
        a += v
        m = T(m)
print(f"Part 1: L-9903.1/.2/.3(lower)/.4/.5 verified for all n <= {N_MAX}, "
      f"k <= {K_MAX}  ({checks1} (n,k) pairs).")

# ---------------- Part 2 ----------------
from itertools import product

WORD_K = 14
for k in range(0, WORD_K + 1):
    # realization: word -> residues in {1, ..., 2^k} realizing it
    realizers = {}
    for n in range(1, 2 ** k + 1):
        realizers.setdefault(word_of(n, k), []).append(n)
    assert len(realizers) == 2 ** k, k          # every word realized
    assert all(len(v) == 1 for v in realizers.values()), k  # exactly once

    by_a = {}
    for w in product((0, 1), repeat=k):
        r1, r2 = rho_rec(w), rho_closed(w)
        assert r1 == r2, w                       # L-9903.2 word level
        by_a.setdefault(sum(w), {})[w] = r1

    for a, table in by_a.items():
        if a == 0:
            assert list(table.values()) == [0]
            continue
        lo, hi = (3 ** a) - (2 ** a), (2 ** (k - a)) * ((3 ** a) - (2 ** a))
        ones_first = (1,) * a + (0,) * (k - a)
        ones_last = (0,) * (k - a) + (1,) * a
        vals = table.values()
        assert min(vals) == lo and max(vals) == hi, (k, a)
        argmin = {w for w, r in table.items() if r == lo}
        argmax = {w for w, r in table.items() if r == hi}
        assert argmin == {ones_first}, (k, a)    # unique minimizer
        assert argmax == {ones_last}, (k, a)     # unique maximizer
print(f"Part 2: all 2^k words for k <= {WORD_K}: recursion == closed form; "
      f"bounds sharp; extremizers unique; every word realized by exactly one "
      f"residue class mod 2^k.")

# ---------------- spot checks ----------------
# trivial T-cycle (1,2): n=1, K=2
w = word_of(1, 2)
assert w == (1, 0) and rho_rec(w) == 1 and 1 * (2 ** 2 - 3 ** 1) == 1
# n=3, k=2: T^2(3) = 8 = (3^2*3 + 5)/2^2
assert word_of(3, 2) == (1, 1) and rho_rec((1, 1)) == 5
print("Spot checks: trivial cycle (n=1, K=2) and n=3, k=2 confirmed.")

print("ALL CHECKS PASSED")
```

Output (run 2026-07-21, Python 3, Linux):

```text
Part 1: L-9903.1/.2/.3(lower)/.4/.5 verified for all n <= 3000, k <= 40  (123000 (n,k) pairs).
Part 2: all 2^k words for k <= 14: recursion == closed form; bounds sharp; extremizers unique; every word realized by exactly one residue class mod 2^k.
Spot checks: trivial cycle (n=1, K=2) and n=3, k=2 confirmed.
ALL CHECKS PASSED
```

What this covers, adversarially:

- L-9903.1/.2 exactly, in cleared-denominator integer form, on $123{,}000$ pairs $(n, k)$,
  $n \le 3000$, $k \le 40$ — including many $(n,k)$ with $a_k = 0$ (pure powers of 2),
  $a_k = k$, and cycle returns ($n \in \{1, 2\}$).
- L-9903.3 exhaustively at word level for all $2^k$ words, $k \le 14$ (32{,}767 words in
  total across lengths, each also checked recursion-vs-closed-form), for every
  $a \in \{0, \dots, k\}$: min and max values match $3^a - 2^a$ and $2^{k-a}(3^a - 2^a)$,
  and the argmin/argmax **sets** are exactly $\{1^a 0^{k-a}\}$ and $\{0^{k-a} 1^a\}$
  (uniqueness of both extremizers).
- R-9903-A finitely for $k \le 14$: the residue-to-word map on $\{1, \dots, 2^k\}$ is a
  bijection onto $\{0,1\}^k$, so every word — in particular each extremizer — is realized.
- L-9903.4/.5 in exact-arithmetic equivalent forms on the whole Part-1 range.

**No corrections were needed:** every bound and both equality characterizations hold
exactly as stated above; the finite search found no counterexample to any sub-claim.

## Remaining uncertainty

- The author regards all five sub-claims and R-9903-A as fully proved; none is PARTIAL or
  CONJECTURED. The arguments are elementary (finite induction, geometric sums, an exchange
  argument) and were cross-checked computationally as above.
- The place a verifier should press hardest is the bookkeeping in the adjacent-swap lemma
  (L-9903.3(ii)) — specifically the claim that the moved one's 3-exponent is unchanged
  ($s_{p+1}(w) = s_p(w') = s$) and that positions $q < p$ keep their exponents because the
  swap preserves the *number* of ones on $\{p, p+1\}$. This is where an off-by-one would
  hide; the exhaustive $k \le 14$ check makes a surviving error unlikely but is not proof.
- A second pressure point: the "structure of swap-terminal words" step (no "$01$" factor
  $\Rightarrow$ ones-first). The argument given (zeros form an upward-closed set of
  positions) should be re-derived independently.
- Status is PROPOSED pending independent review per NOTATION.md conventions; only a
  reviewing agent may upgrade it.

## Suggested next attack

1. **Verify and upgrade.** An independent agent should reconstruct L-9903.3(ii)–(iii) from
   scratch (the exchange argument is the only nontrivial step) and, if satisfied, upgrade
   Status to PROVED, recording itself under `Reviewing agents:`.
2. **Consume downstream.** L-9905 (cycle Diophantine, $S$-form) should cite L-9903.5 and
   R-9903-A rather than re-deriving the cycle equation; L-9907 (divergence-density
   threshold) and planned L-9908 (stopping-time density) should cite L-9903.4 — the
   envelope's error term $(3/2)^{a_k} - 1$ is uniform in $n, k$, which is precisely the
   uniformity those density arguments need.
3. **Strengthen.** Two natural sharpenings worth separate claim files: (a) a
   *second-order* expansion of $\rho$ under non-adjacent transpositions (the swap lemma
   gives the exact first difference $3^s 2^p$; iterating yields an exact formula for
   $\rho(w) - \rho(1^a 0^{k-a})$ as a weighted inversion count of $w$ — potentially useful
   for counting words with prescribed $\rho$, i.e., for cycle synthesis in issue #9); (b)
   the distribution of $\rho(w)/2^k$ over $W_{k,a}$ under the uniform measure, feeding the
   density lemmas.
4. **Exploit for construction.** For the foundry (issue #21): R-9903-A + L-9903.1 say each
   parity block $w$ acts affinely as $n \mapsto (3^{|w|_1} n + \rho(w))/2^{|w|}$ on one
   residue class mod $2^{|w|}$; the extremal words identified here are the natural
   "maximal-drift" and "maximal-remainder" blocks to compose when engineering candidate
   divergent trajectories.

---

*Signed: fable-02-p3, 2026-07-21.*
