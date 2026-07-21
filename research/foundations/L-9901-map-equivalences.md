# L-9901 — Equivalence of the maps $C$, $T$, $S$: reaching 1, boundedness, cycles, trichotomy, counterexample dichotomy

```text
Claim ID: L-9901
Title: Equivalence of the Collatz map C, the shortcut map T, and the Syracuse map S:
       reaching 1, boundedness, cycle correspondence, orbit trichotomy, and the
       counterexample dichotomy
Status: PROPOSED
Authoring agent: fable-02-p1
Reviewing agents: (none yet)
Created: 2026-07-21
Last updated: 2026-07-21
Dependencies: NOTATION.md (D-9901 map C; D-9902 map T; D-9903 odd part; D-9904 map S and
              exponent a(x); D-9905 orbits, reaching 1, trivial cycles; D-9906 parity
              vector v_i, a_k; D-9907 bounded/unbounded/divergent; D-9908 cycles and the
              S-cycle data m, a_i, K; D-9909 counterexample)
Scope: Orbits of C and T on Z^+ and of S on the positive odd integers. No claim is made
       about extensions to Z^- , Z_2, or Q; the boxed remark in Part 8 of the Proof states
       explicitly which step is integer-only, and the Adversarial tests section contains a
       clearly labeled extension check outside Z^+.
Related counterexample candidates: none
```

---

## Statement

Throughout, $C$, $T$, $S$, $\mathrm{odd}(n)$, $\nu_2$, $O_M(n)$, $v_i(n)$, $a_k(n)$,
$a(x)$ are as in NOTATION.md (D-9901–D-9906). For $M \in \{C, T, S\}$ and $n$ in the
domain of $M$, the **value set** of the orbit is
$$V_M(n) := \{\, M^k(n) : k \ge 0 \,\},$$
and $\sup O_M(n) := \sup V_M(n) \in \mathbb{Z}^+ \cup \{\infty\}$ (D-9907: the orbit is
*bounded* iff this sup is finite). We say the orbit $O_M(n)$ **enters** a set $A$ if
$M^k(n) \in A$ for some $k \ge 0$, and **eventually enters (and remains in)** $A$ if
$M^k(n) \in A$ for all sufficiently large $k$. Cycles are identified with their point sets
as justified in P0.2 below; $\mathrm{Cyc}(M)$ denotes the set of cycles of $M$ (on
$\mathbb{Z}^+$ for $C, T$; on the positive odd integers for $S$). For a set
$A \subseteq \mathbb{Z}$, $A_{\mathrm{odd}} := \{x \in A : x \text{ odd}\}$.
Inequalities involving $\infty$ use the conventions $a \le \infty$ for all $a$,
$2 \cdot \infty = \infty$, $3\cdot\infty + 1 = \infty$, $\max(a, \infty) = \infty$.

**L-9901.1 (reaching 1).** For every $n \in \mathbb{Z}^+$, the following are equivalent:

1. $1 \in O_C(n)$, i.e. $\exists k \ge 0:\ C^k(n) = 1$;
2. $1 \in O_T(n)$, i.e. $\exists k \ge 0:\ T^k(n) = 1$;
3. $1 \in O_S(\mathrm{odd}(n))$, i.e. $\exists j \ge 0:\ S^j(\mathrm{odd}(n)) = 1$.

(Here membership in an orbit means membership in its value set. In particular
$\mathrm{odd}(n) \in V_C(n) \cap V_T(n)$; see P1.)

**L-9901.2 (boundedness, with explicit two-sided bounds).** For every
$n \in \mathbb{Z}^+$, write $M_C := \sup O_C(n)$, $M_T := \sup O_T(n)$,
$M_S := \sup O_S(\mathrm{odd}(n))$. Then:

*(i)* $\ M_S \ \le\ M_T \ \le\ M_C \ \le\ 2\,M_T$;

*(ii)* $\ M_T \ \le\ \max\!\Big(n,\ \dfrac{3 M_S + 1}{2}\Big)$ and
$\ M_C \ \le\ \max\big(n,\ 3 M_S + 1\big)$;

*(iii)* consequently $M_C < \infty \iff M_T < \infty \iff M_S < \infty$: the three orbits
are simultaneously bounded or simultaneously unbounded (D-9907).

The constants are optimal in general: at $n = 1$ all of $M_C = 2M_T$,
$M_T = (3M_S+1)/2$, $M_C = 3M_S + 1$ hold with equality, and at $n = 2^{10}$ the terms
$n$ in *(ii)* cannot be removed ($M_T = 2^{10}$, $(3M_S+1)/2 = 2$).

**L-9901.3 (cycle correspondence).** Define, for $\Gamma \in \mathrm{Cyc}(C)$,
$\Delta \in \mathrm{Cyc}(T)$, $\Sigma \in \mathrm{Cyc}(S)$:
$$\Phi(\Gamma) := \Gamma \setminus \{3x+1 : x \in \Gamma_{\mathrm{odd}}\}, \qquad
\Psi(\Delta) := \Delta \cup \{3x+1 : x \in \Delta_{\mathrm{odd}}\},$$
$$\Phi'(\Delta) := \Delta_{\mathrm{odd}}, \qquad
\Psi'(\Sigma) := \Sigma \cup \bigl\{ (3x+1)/2^{\,i} \ :\ x \in \Sigma,\ 1 \le i \le a(x)-1 \bigr\}.$$
Then $\Phi : \mathrm{Cyc}(C) \to \mathrm{Cyc}(T)$ and $\Psi : \mathrm{Cyc}(T) \to \mathrm{Cyc}(C)$
are well-defined and mutually inverse bijections, and likewise
$\Phi' : \mathrm{Cyc}(T) \to \mathrm{Cyc}(S)$ and $\Psi' : \mathrm{Cyc}(S) \to \mathrm{Cyc}(T)$.
All four maps match the trivial cycles ($\Phi(\{1,4,2\}) = \{1,2\}$,
$\Phi'(\{1,2\}) = \{1\}$), hence restrict to mutually inverse bijections between the sets
of **nontrivial** cycles (D-9908) of $C$, $T$, $S$. The composite bijection
$\mathrm{Cyc}(C) \to \mathrm{Cyc}(S)$ is $\Gamma \mapsto \Gamma_{\mathrm{odd}}$, with
inverse $\Sigma \mapsto \Sigma \cup \{(3x+1)/2^{\,i} : x \in \Sigma,\ 0 \le i \le a(x)-1\}$.
Lengths: if $\Sigma$ is an $S$-cycle with $m := |\Sigma|$ and
$K := \sum_{x \in \Sigma} a(x)$ (the data of D-9908), then the corresponding $T$-cycle has
length $K$ and the corresponding $C$-cycle has length $m + K$.

**L-9901.4 (orbit trichotomy).** For every $n \in \mathbb{Z}^+$, exactly one of the
following holds for the $T$-orbit of $n$:

*(a)* $O_T(n)$ enters the trivial cycle $\{1, 2\}$ (and then remains in it forever);

*(b)* $O_T(n)$ enters a nontrivial $T$-cycle $\Delta$ (and then remains in it forever);
the cycle $\Delta$ is unique;

*(c)* $T^k(n) \to \infty$ as $k \to \infty$.

The same trichotomy holds verbatim for $C$ on $\mathbb{Z}^+$ with trivial cycle
$\{1,4,2\}$, and for $S$ on the positive odd integers with trivial cycle $\{1\}$
(started at $\mathrm{odd}(n)$). Underlying it is the general integer-orbit dichotomy
Lemma D (Part 8), whose pigeonhole step is valid **only** for orbits in sets of positive
integers — see the boxed remark in Part 8.

**L-9901.5 (counterexample dichotomy).** For every $n \in \mathbb{Z}^+$, the following
are equivalent:

1. $n$ is a Collatz counterexample, i.e. $1 \notin O_C(n)$ (D-9909);
2. $O_T(n)$ eventually enters a nontrivial $T$-cycle, or $T^k(n) \to \infty$;
3. $O_C(n)$ eventually enters a nontrivial $C$-cycle, or $C^k(n) \to \infty$;
4. $O_S(\mathrm{odd}(n))$ eventually enters a nontrivial $S$-cycle, or
   $S^j(\mathrm{odd}(n)) \to \infty$.

Moreover the failure modes match up: the cycle cases of 2., 3., 4. hold together (with
cycles corresponding under the bijections of L-9901.3), and the divergence cases of
2., 3., 4. hold together.

---

## Definitions

All notation is from NOTATION.md; the only additional conventions are those already
listed at the top of the Statement, plus:

- **Cycle (point) set.** For a map $f : X \to X$, a set $\Gamma \subseteq X$ is a *cycle
  set* of $f$ if $\Gamma$ is the point set $\{f^k(x) : k \ge 0\}$ of some purely periodic
  orbit (D-9908). P0.2 proves this identification of cycles with sets is faithful (a
  purely periodic orbit is determined by its point set up to starting point), so
  "$\mathrm{Cyc}(M)$", "trivial cycle $\{1,2\}$", etc., refer to cycle sets.
- **First-return map.** For $f : X \to X$, a finite cycle set $\Gamma$ of $f$, and
  $\emptyset \ne \Delta \subseteq \Gamma$: for $y \in \Delta$ put
  $r(y) := \min\{r \ge 1 : f^r(y) \in \Delta\}$ and $g(y) := f^{r(y)}(y)$; $g$ is the
  *first-return map of $f$ to $\Delta$* (well-defined by P0.5).
- **Eventually enters.** "$O_M(n)$ eventually enters cycle $\Gamma$" is used in the sense
  of Lemma D(A): $\exists i \ \forall k \ge i:\ M^k(n) \in \Gamma$. Since cycle sets are
  closed under $M$, entering at one index implies remaining forever (P0.1), so "enters"
  and "eventually enters and remains" coincide for cycle sets.
- Empty index ranges denote empty sets (NOTATION.md conventions); e.g. for $a(x) = 1$ the
  set $\{(3x+1)/2^i : 1 \le i \le a(x) - 1\}$ is empty.

---

## Motivation

This lemma is deliberately unglamorous: it is the load-bearing "change of coordinates"
that nearly every active branch of the project uses implicitly. Making it exact and
adversarially checked serves:

- **Issue #10 (sanctuary programs).** A "sanctuary" — a forward-invariant region of
  $\mathbb{Z}^+$ avoiding $\{1, 2\}$ — forces, by L-9901.4 + L-9901.5, that every orbit
  trapped in it either enters a nontrivial cycle or diverges. L-9901.5 is the precise
  statement that "avoiding 1 forever" *is* "nontrivial cycle or divergence", in each of
  the three standard coordinate systems, with the failure modes matching across systems.
- **Issue #21 (T-9602).** T-9602 needs "unbounded $\Rightarrow$ divergent" for integer
  orbits. That is exactly Lemma D(3) (Part 8), proved here in general form for any map of
  any set of positive integers, together with the boxed warning that the step is a
  pigeonhole argument valid only for integers — the precise reason a 2-adic or rational
  symbolic construction with bounded non-periodic behavior would *not* transfer to
  $\mathbb{Z}^+$.
- **All divergence programs.** By L-9901.2 + Lemma D, divergence can be constructed or
  refuted in whichever of $C$, $T$, $S$ is most convenient (typically $S$, which has no
  parity bookkeeping), and transfers automatically with explicit constants.
- **All cycle programs.** By L-9901.3, searching for nontrivial cycles of $C$ or $T$ is
  *exactly* equivalent to searching for nontrivial $S$-cycles — the smallest
  representation, with the D-9908 data $m, a_i, K$ — and the length dictionary
  $m \leftrightarrow K \leftrightarrow m + K$ is proved, not folklore.

---

## Proof

The proof is organized as: Part 0 (finite cycle combinatorics), Part 1 (halving
segments), Part 2 (merge identity $C \leftrightarrow T$), Part 3 (odd extraction
$T \leftrightarrow S$), then Parts 4–8 proving L-9901.1–.5 in order. All maps involved
send their stated domains into themselves: for $n \in \mathbb{Z}^+$ even, $n/2 \in
\mathbb{Z}^+$; for $n$ odd, $3n+1 \in \mathbb{Z}^+$ is even, so $T(n) = (3n+1)/2 \in
\mathbb{Z}^+$; and $S(x) = \mathrm{odd}(3x+1)$ is a positive odd integer for $x$ positive
odd. This is used silently below.

### Part 0 — cycles as point sets

**P0.1 (pure periodicity basics).** *Let $X$ be a set, $f : X \to X$, and $x \in X$ with
$O_f(x)$ purely periodic with least period $p \ge 1$ (i.e. $f^p(x) = x$ and no smaller
positive exponent has this property; D-9908). Then:*

*(i)* for $k \ge 0$: $f^k(x) = x \iff p \mid k$;

*(ii)* $x, f(x), \dots, f^{p-1}(x)$ are pairwise distinct;

*(iii)* the point set $P := \{f^k(x) : k \ge 0\}$ equals $\{f^k(x) : 0 \le k \le p-1\}$
and $|P| = p$ (cardinality of a cycle set $=$ least period $=$ length);

*(iv)* every $y \in P$ has purely periodic orbit with the same least period $p$ and the
same point set $P$; $f$ maps $P$ bijectively onto $P$, and the $f$-orbit of any point of
$P$ visits every point of $P$ (i.e. $f|_P$ is a cyclic permutation of $P$).

*Proof.* (i) If $k = \ell p$, induction on $\ell$: $f^{\ell p}(x) =
f^{(\ell-1)p}(f^p(x)) = f^{(\ell-1)p}(x) = x$ ($\ell = 0$: $f^0(x) = x$, D-9905).
Conversely write $k = \ell p + s$, $0 \le s < p$; then $x = f^k(x) = f^s(f^{\ell p}(x)) =
f^s(x)$; minimality of $p$ forces $s = 0$.
(ii) If $f^i(x) = f^j(x)$ with $0 \le i < j \le p - 1$, apply $f^{p-j}$:
$x = f^p(x) = f^{p-j+i}(x)$ with $1 \le p - j + i \le p - 1$, contradicting (i).
(iii) By (i), $f^k(x) = f^{k \bmod p}(x)$ for all $k \ge 0$; combine with (ii).
(iv) Let $y = f^i(x)$, $0 \le i \le p - 1$. Then $f^p(y) = f^i(f^p(x)) = y$, so $O_f(y)$
is purely periodic; its point set is $\{f^{k+i}(x) : k \ge 0\} = P$ by (iii) (indices
$k + i$ cover all residues mod $p$). Its least period $p'$ satisfies $p' \mid p$ (by (i)
applied to $y$, since $f^p(y) = y$), and by (iii) applied to $y$,
$p' = |P| = p$. Finally $f(P) \subseteq P$, and $f$ is surjective on $P$ since
$f(f^{p-1}(y)) = y$ for each $y \in P$; a surjection of a finite set is a bijection. The
orbit of any $y \in P$ visits all of $P$ by the point-set claim just proved. $\square$

**P0.2 (identification of cycles with their point sets).** *Two purely periodic orbits of
$f$ have the same point set if and only if each is a shift of the other. Hence a cycle
(D-9908: a purely periodic orbit) is determined by its point set up to choice of starting
point, and we identify cycles with cycle sets from now on.* The **trivial cycle sets**
are $\{1,4,2\}$ for $C$, $\{1,2\}$ for $T$, $\{1\}$ for $S$ (D-9905; direct check:
$C: 1 \mapsto 4 \mapsto 2 \mapsto 1$; $T: 1 \mapsto 2 \mapsto 1$;
$S(1) = \mathrm{odd}(4) = 1$; each purely periodic).

*Proof.* If $O_f(x)$ and $O_f(y)$ are purely periodic with the same point set $P$, then
$y = f^i(x)$ for some $i \ge 0$, and $O_f(y) = (f^i(x), f^{i+1}(x), \dots)$ is the
$i$-shift of $O_f(x)$. Conversely, a shift of a purely periodic orbit has the same point
set by P0.1(iv). $\square$

**P0.3 (distinct cycles are disjoint).** *If $\Gamma_1, \Gamma_2$ are cycle sets of $f$
and $\Gamma_1 \cap \Gamma_2 \ne \emptyset$, then $\Gamma_1 = \Gamma_2$.*

*Proof.* Let $z \in \Gamma_1 \cap \Gamma_2$. By P0.1(iv), $\Gamma_1$ is the point set of
$O_f(z)$, and so is $\Gamma_2$. $\square$

**P0.4 (no all-even cycle).** *Every cycle set of $C$ on $\mathbb{Z}^+$ and every cycle
set of $T$ on $\mathbb{Z}^+$ contains an odd element.*

*Proof.* Suppose $\Gamma$ is a cycle set of $M \in \{C, T\}$ with all elements even, and
let $x \in \Gamma$, $p := |\Gamma| \ge 1$. On even inputs both $C$ and $T$ halve, and the
result stays in $\Gamma$ (P0.1(iv)), hence stays even; so by induction $M^p(x) = x/2^p$.
By P0.1, $M^p(x) = x$, so $x (2^p - 1) = 0$ — impossible for $x \ge 1$, $p \ge 1$.
$\square$

**P0.5 (first-return lemma).** *Let $\Gamma$ be a finite cycle set of $f$ and
$\emptyset \ne \Delta \subseteq \Gamma$. Then for every $y \in \Delta$ the return time
$r(y) := \min\{r \ge 1 : f^r(y) \in \Delta\}$ exists, and the first-return map
$g : \Delta \to \Delta$, $g(y) := f^{r(y)}(y)$, makes $\Delta$ a cycle set of $g$: the
$g$-orbit of every $y \in \Delta$ is purely periodic with point set $\Delta$.*

*Proof.* Let $p := |\Gamma|$. Existence of $r(y)$: $f^p(y) = y \in \Delta$ by P0.1, so
$r(y) \le p$. Fix $y \in \Delta$. By P0.1, the list $f^0(y), f^1(y), \dots, f^{p-1}(y)$
enumerates $\Gamma$ without repetition. Let $0 = s_1 < s_2 < \dots < s_m \le p - 1$ be
exactly the indices $s$ in this range with $f^s(y) \in \Delta$; then
$\{f^{s_1}(y), \dots, f^{s_m}(y)\} = \Delta$, these points are pairwise distinct, and
$m = |\Delta| \ge 1$. For $1 \le i < m$: no index strictly between $s_i$ and $s_{i+1}$
lands in $\Delta$, so $r(f^{s_i}(y)) = s_{i+1} - s_i$ and $g(f^{s_i}(y)) = f^{s_{i+1}}(y)$.
For $i = m$: no index in $\{s_m + 1, \dots, p-1\}$ lands in $\Delta$ and
$f^p(y) = y \in \Delta$, so $g(f^{s_m}(y)) = y = f^{s_1}(y)$. Thus $g$ cyclically
permutes the $m$ distinct points $f^{s_1}(y), \dots, f^{s_m}(y)$, i.e. $g^m(y) = y$ and
the $g$-orbit of $y$ has point set $\Delta$; in particular it is purely periodic. (The
case $m = 1$ is the fixed point $g(y) = y$, $\Delta = \{y\}$ — allowed, D-9908 permits
least period $1$.) $\square$

### Part 1 — halving segments

**P1.** *Let $n \in \mathbb{Z}^+$ and $e := \nu_2(n)$. Then for $0 \le i \le e$:
$C^i(n) = T^i(n) = n/2^i \in \mathbb{Z}^+$; these values are even for $i < e$; and
$C^e(n) = T^e(n) = \mathrm{odd}(n)$. In particular
$\mathrm{odd}(n) \in V_C(n) \cap V_T(n)$.*

*Proof.* Induction on $i$. Base $i = 0$: $C^0(n) = T^0(n) = n = n/2^0$ (D-9905). Step:
let $0 \le i < e$ and suppose $C^i(n) = T^i(n) = n/2^i$. Then
$\nu_2(n/2^i) = e - i \ge 1$, so $n/2^i$ is even, and both maps halve it:
$C^{i+1}(n) = T^{i+1}(n) = n/2^{i+1}$. Finally $n/2^e = \mathrm{odd}(n)$ (D-9903), which
is odd. (Edge case $e = 0$: the statement reduces to $C^0(n) = T^0(n) = n =
\mathrm{odd}(n)$, with the "even for $i < e$" clause vacuous.) $\square$

### Part 2 — merge identity ($C \leftrightarrow T$)

**P2 (merge identity and index classification).** *Let $n \in \mathbb{Z}^+$. Define
$c_k := c_k(n) := k + a_k(n)$ for $k \ge 0$, with $a_k$ as in D-9906. Then:*

*(a)* $T^k(n) = C^{\,c_k}(n)$ *for all $k \ge 0$;*

*(b)* $c_0 = 0$, $c_{k+1} = c_k + 1 + v_k(n) \in \{c_k + 1,\ c_k + 2\}$; hence
$(c_k)_{k \ge 0}$ is strictly increasing with $c_k \ge k \to \infty$, and the intervals
$[c_k, c_{k+1})$, $k \ge 0$, partition $\mathbb{Z}_{\ge 0}$;

*(c)* for every $j \ge 0$, exactly one of the following holds:
either $j = c_k$ for a unique $k \ge 0$ (and then $C^j(n) = T^k(n)$), or $j = c_k + 1$
for a unique $k \ge 0$ with $v_k(n) = 1$, and in that case
$$C^j(n) = 3\,T^k(n) + 1 = 2\,T^{k+1}(n),$$
an even number;

*(d)* consequently, as sets,
$$V_C(n) \ =\ V_T(n)\ \cup\ \{\,3x + 1\ :\ x \in V_T(n),\ x \text{ odd}\,\},$$
and every element of $V_C(n)$ not of the form $T^k(n)$ equals $2\,T^{k+1}(n)$ for some
$k \ge 0$ with $T^k(n)$ odd.

*Proof.* (a) and (b) together, by induction on $k$. Base $k = 0$: $c_0 = 0 + a_0 = 0$
(empty sum) and $T^0(n) = n = C^0(n)$. Step: assume $m := T^k(n) = C^{c_k}(n)$.

- If $m$ is even ($v_k(n) = 0$): $T^{k+1}(n) = m/2 = C(m) = C^{\,c_k + 1}(n)$, and
  $c_{k+1} = (k+1) + a_{k+1} = (k+1) + a_k = c_k + 1$. ✓
- If $m$ is odd ($v_k(n) = 1$): $C(m) = 3m + 1$, which is even ($m$ odd $\Rightarrow$
  $3m + 1$ even), so $C^2(m) = (3m+1)/2 = T(m) = T^{k+1}(n)$; thus
  $T^{k+1}(n) = C^{\,c_k + 2}(n)$, and $c_{k+1} = (k+1) + (a_k + 1) = c_k + 2$. ✓

Strict increase and $c_k \ge k$ are immediate from the increments; since $c_0 = 0$ and
$c_k \to \infty$, every $j \ge 0$ lies in exactly one interval $[c_k, c_{k+1})$, which
has length $1$ or $2$.

(c) Given $j$, take the unique $k$ with $j \in [c_k, c_{k+1})$. If $j = c_k$, then
$C^j(n) = T^k(n)$ by (a); this $k$ is unique because $(c_k)$ is strictly increasing. If
$j \ne c_k$, then the interval has length $2$, i.e. $v_k(n) = 1$ and $j = c_k + 1$; then
with $m := T^k(n)$ (odd):
$C^j(n) = C(C^{c_k}(n)) = C(m) = 3m + 1 = 2 \cdot \tfrac{3m+1}{2} = 2\,T^{k+1}(n)$, an
even number. Uniqueness of this $k$ again follows from the partition. The two cases are
mutually exclusive because $j$ lies in only one interval and at only one position in it.

(d) "$\subseteq$": every $C^j(n)$ falls in one of the two cases of (c): either it is some
$T^k(n) \in V_T(n)$, or it is $3m + 1$ with $m = T^k(n)$ odd, $m \in V_T(n)$.
"$\supseteq$": $V_T(n) \subseteq V_C(n)$ by (a); and if $x \in V_T(n)$ is odd, choose $k$
with $T^k(n) = x$ (then $v_k(n) = 1$) and set $j = c_k + 1$: $C^j(n) = 3x + 1$ by (c).
The final sentence of (d) is the displayed identity in (c). $\square$

### Part 3 — odd extraction ($T \leftrightarrow S$)

**P3 (odd subsequence of a $T$-orbit).** *Let $n \in \mathbb{Z}^+$, $e := \nu_2(n)$,
$x_0 := \mathrm{odd}(n)$, and inductively $x_{j+1} := S(x_j)$ (so $x_j = S^j(x_0)$, a
positive odd integer for every $j \ge 0$). Put $a_j := a(x_j) = \nu_2(3 x_j + 1) \ge 1$
(D-9904) and define the odd-visit times $t_0 := e$, $t_{j+1} := t_j + a_j$. Then:*

*(a)* $T^{t_j}(n) = x_j$ *for all $j \ge 0$;*

*(b)* for $t_j < i < t_{j+1}$: $\ T^i(n) = (3 x_j + 1)/2^{\,i - t_j}$, an **even**
integer;

*(c)* for $0 \le i < e$: $\ T^i(n) = n/2^i$, an **even** integer;

*(d)* $\{\, k \ge 0 : T^k(n) \text{ odd} \,\} = \{\, t_j : j \ge 0 \,\}$ with
$t_0 < t_1 < t_2 < \cdots$; hence the subsequence of odd entries of $O_T(n)$, in order of
occurrence, is exactly $O_S(\mathrm{odd}(n))$. In particular, as sets,
$$V_S(x_0) \ =\ \{x \in V_T(n) : x \text{ odd}\} \ =\ \{x \in V_C(n) : x \text{ odd}\};$$

*(e)* $\displaystyle V_T(n) \ =\ \{\, n/2^i : 0 \le i \le e \,\} \ \cup\
\bigcup_{j \ge 0} \bigl\{\, (3x_j + 1)/2^{\,i} \ :\ 1 \le i \le a_j \,\bigr\}.$

*Proof.* (c) is P1. We prove (a) and (b) by induction on $j$, with an inner induction.

Base $j = 0$: $T^{t_0}(n) = T^e(n) = \mathrm{odd}(n) = x_0$ by P1; there is nothing
between $t_{-1}$ and $t_0$ to check.

Step: assume $T^{t_j}(n) = x_j$, odd. Since $x_j$ is odd,
$T^{t_j + 1}(n) = (3x_j + 1)/2 = (3x_j+1)/2^1$. Inner induction on $i$, $1 \le i \le a_j$,
with hypothesis $T^{t_j + i}(n) = (3x_j+1)/2^i$: if $i < a_j$, then
$\nu_2\bigl((3x_j+1)/2^i\bigr) = a_j - i \ge 1$, so the value is even and $T$ halves it,
giving $T^{t_j + i + 1}(n) = (3x_j+1)/2^{i+1}$. At $i = a_j$:
$T^{t_j + a_j}(n) = (3x_j+1)/2^{a_j} = \mathrm{odd}(3x_j + 1) = S(x_j) = x_{j+1}$, which
is odd, and $t_j + a_j = t_{j+1}$. This proves (a) for $j + 1$, and (b) for the gap
$(t_j, t_{j+1})$, whose interior values ($1 \le i \le a_j - 1$) were just shown even.
(Edge case $a_j = 1$: the gap is empty and $T^{t_j + 1}(n) = x_{j+1}$ directly.)

(d) The intervals $[0, e)$ and $[t_j, t_{j+1})$, $j \ge 0$, partition
$\mathbb{Z}_{\ge 0}$: indeed $t_0 = e$, the sequence $(t_j)$ is strictly increasing
(each $a_j \ge 1$), and $t_j \ge e + j \to \infty$. On $[0, e)$ all values are even by
(c); at $i = t_j$ the value $x_j$ is odd by (a); at $t_j < i < t_{j+1}$ the value is even
by (b). Hence the odd positions are exactly $\{t_j\}$, in increasing order, with values
$x_0, x_1, x_2, \dots$ — that is, the odd subsequence of $O_T(n)$ is
$O_S(\mathrm{odd}(n))$. The first set identity follows ($V_S(x_0) = \{x_j : j \ge 0\}$);
the second follows from P2(d), because the elements of $V_C(n) \setminus V_T(n)$ listed
there are all even ($3x+1$ with $x$ odd), so the odd parts of $V_C(n)$ and $V_T(n)$
coincide.

(e) Read off the values on the partition of (d): on $[0, e]$ they are $n/2^i$
(P1, including $x_0 = n/2^e$ at $i = e$); on $(t_j, t_{j+1}]$ they are
$(3x_j+1)/2^{\,i}$ for $1 \le i \le a_j$ (by (b), plus the endpoint $i = a_j$ giving
$x_{j+1}$ by (a)). Every index $k \ge 0$ lies in $[0, e]$ or in exactly one
$(t_j, t_{j+1}]$, so both inclusions hold. $\square$

### Part 5 — proof of L-9901.1

Let $n \in \mathbb{Z}^+$ and $x_0 := \mathrm{odd}(n)$.

**(2 $\Rightarrow$ 1).** If $T^k(n) = 1$, then $C^{\,c_k(n)}(n) = 1$ by P2(a).

**(1 $\Rightarrow$ 2).** Suppose $C^j(n) = 1$. By P2(c), either $j = c_k$ for some $k$,
in which case $T^k(n) = C^j(n) = 1$ and we are done; or $C^j(n)$ is even — impossible,
since $1$ is odd.

**(3 $\Rightarrow$ 2).** If $S^j(x_0) = 1$, then $T^{t_j}(n) = 1$ by P3(a).

**(2 $\Rightarrow$ 3).** Suppose $T^k(n) = 1$. Since $1$ is odd, P3(d) gives $k = t_j$
for some $j \ge 0$, and then $S^j(x_0) = T^{t_j}(n) = 1$.

This proves $1 \Leftrightarrow 2 \Leftrightarrow 3$. Edge cases: $k = 0$ and $j = 0$ are
allowed throughout (D-9905 defines "reaches 1" with $k \ge 0$); e.g. $n = 1$ satisfies
all three at index $0$, and $n = 2^e$ satisfies them via $T^e(n) = C^e(n) = 1 = x_0$.
$\blacksquare$

### Part 6 — proof of L-9901.2

Let $n$, $x_0$, $x_j$, $a_j$, $e$ be as in P3, and $M_C, M_T, M_S$ as in the statement.
Note $M_S = \sup_j x_j$ and each $x_j$ is odd.

**(i).** $M_S \le M_T$: $V_S(x_0) \subseteq V_T(n)$ by P3(d). $M_T \le M_C$:
$V_T(n) \subseteq V_C(n)$ by P2(a). $M_C \le 2 M_T$: if $M_T = \infty$ this is trivial;
otherwise, by P2(d), every element of $V_C(n)$ either lies in $V_T(n)$ (hence
$\le M_T \le 2M_T$, as $M_T \ge 1$) or equals $3\,T^k(n) + 1 = 2\,T^{k+1}(n) \le 2 M_T$
for some $k$ (P2(c)).

**(ii).** If $M_S = \infty$, both bounds are trivial by the $\infty$-conventions.
Assume $M_S < \infty$; then $M_S$ is odd (a supremum attained in the set
$\{x_j\} \subseteq V_S(x_0)$, which is finite by P0-free reasoning: a bounded set of
positive integers attains its sup), so $(3M_S+1)/2 \in \mathbb{Z}^+$. By P3(e), every
element of $V_T(n)$ is either $n/2^i \le n$ ($0 \le i \le e$) or
$(3x_j+1)/2^{\,i} \le (3x_j+1)/2 \le (3M_S+1)/2$ (using $i \ge 1$ and $x_j \le M_S$).
Hence $M_T \le \max\bigl(n, (3M_S+1)/2\bigr)$. For $M_C$: by P2(d) and P3(d),
$$V_C(n) = V_T(n) \cup \{3x + 1 : x \in V_S(x_0)\},$$
and the added elements are $\le 3M_S + 1$; combined with the bound on $V_T(n)$ and
$(3M_S+1)/2 \le 3M_S+1$, this gives $M_C \le \max(n, 3M_S + 1)$.

**(iii).** From (i), $M_C < \infty \Rightarrow M_T < \infty \Rightarrow M_S < \infty$;
from (ii), $M_S < \infty \Rightarrow M_C \le \max(n, 3M_S+1) < \infty$ (here $n$ is a
fixed finite integer). So the three are simultaneously finite. By D-9907 this is the
simultaneous boundedness claim.

**Optimality examples** (finite checks, verified in the Adversarial tests): $n = 1$:
$V_C = \{1,4,2\}$, $V_T = \{1,2\}$, $V_S = \{1\}$, so $M_C = 4$, $M_T = 2$, $M_S = 1$,
and $M_C = 2M_T$, $M_T = (3M_S+1)/2$, $M_C = 3M_S+1$ all hold with equality. $n = 2^{10}$:
$M_C = M_T = 2^{10} = n > 2 = (3M_S+1)/2$, so neither $n$-term in (ii) can be dropped.
$n = 4$: $M_C = M_T = 4$, so the left inequality $M_T \le M_C$ can be equality while
$M_C < 2M_T$. $\blacksquare$

### Part 7 — proof of L-9901.3

Throughout, $\Gamma$ denotes a $C$-cycle set, $\Delta$ a $T$-cycle set, $\Sigma$ an
$S$-cycle set, and $\Phi, \Psi, \Phi', \Psi'$ are as in the Statement.

**Step 7.1: $\Phi$ maps $\mathrm{Cyc}(C)$ into $\mathrm{Cyc}(T)$, and
$(\Phi(\Gamma))_{\mathrm{odd}} = \Gamma_{\mathrm{odd}}$.**
Let $\Gamma \in \mathrm{Cyc}(C)$. By P0.1(iv), $C|_\Gamma$ is a bijection of $\Gamma$; by
P0.4, $\Gamma_{\mathrm{odd}} \ne \emptyset$. The removed set
$R := \{3x+1 : x \in \Gamma_{\mathrm{odd}}\} = C(\Gamma_{\mathrm{odd}}) \subseteq \Gamma$
consists of even numbers, so $\Phi(\Gamma) = \Gamma \setminus R \supseteq
\Gamma_{\mathrm{odd}} \ne \emptyset$ and $(\Phi(\Gamma))_{\mathrm{odd}} =
\Gamma_{\mathrm{odd}}$. We claim the first-return map of $C|_\Gamma$ to $\Phi(\Gamma)$ is
exactly $T$ restricted to $\Phi(\Gamma)$:

- $y \in \Phi(\Gamma)$ even: $C(y) = y/2 = T(y)$. Moreover $C(y) \in \Phi(\Gamma)$: if
  $C(y) \in R = C(\Gamma_{\mathrm{odd}})$, injectivity of $C|_\Gamma$ would force
  $y \in \Gamma_{\mathrm{odd}}$, contradicting $y$ even. Return time $1$, return value
  $T(y)$.
- $y \in \Phi(\Gamma)$ odd: $C(y) = 3y + 1 \in R$, so $C(y) \notin \Phi(\Gamma)$. Next,
  $C^2(y) = C(3y+1) = (3y+1)/2 = T(y)$ (as $3y+1$ is even and lies in $\Gamma$). And
  $C^2(y) \in \Phi(\Gamma)$: if $C^2(y) = C(x)$ with $x \in \Gamma_{\mathrm{odd}}$,
  injectivity gives $3y + 1 = x$, impossible since $3y+1$ is even. Return time $2$,
  return value $T(y)$.

By P0.5 (applied to $f = C|_\Gamma$, $\Delta = \Phi(\Gamma)$), $\Phi(\Gamma)$ is a cycle
set of this return map; since the return map agrees pointwise with $T$ on $\Phi(\Gamma)$
and maps $\Phi(\Gamma)$ into itself, the (global) $T$-orbit of any
$y \in \Phi(\Gamma)$ coincides with its return-map orbit. Hence
$\Phi(\Gamma) \in \mathrm{Cyc}(T)$.

**Step 7.2: $\Phi'$ maps $\mathrm{Cyc}(T)$ into $\mathrm{Cyc}(S)$.**
Let $\Delta \in \mathrm{Cyc}(T)$; $\Delta_{\mathrm{odd}} \ne \emptyset$ by P0.4. Let
$x \in \Delta_{\mathrm{odd}}$ and apply P3 with $n = x$ (so $e = 0$, $t_0 = 0$,
$t_1 = a(x)$): the iterates $T^i(x) = (3x+1)/2^{\,i}$ for $1 \le i \le a(x)$ are even for
$i < a(x)$, and $T^{a(x)}(x) = S(x)$ is odd. All these iterates lie in $\Delta$
(P0.1(iv)). Hence the first return of $x$ to $\Delta_{\mathrm{odd}}$ under $T|_\Delta$
occurs at time $a(x)$ with value $S(x)$. By P0.5, $\Delta_{\mathrm{odd}}$ is a cycle set
of the return map, which agrees pointwise with $S$; so
$\Phi'(\Delta) = \Delta_{\mathrm{odd}} \in \mathrm{Cyc}(S)$.

**Step 7.3: $\Psi$ maps $\mathrm{Cyc}(T)$ into $\mathrm{Cyc}(C)$; moreover $\Psi(\Delta)$
is the point set of the $C$-orbit of any $x \in \Delta$, the added set
$N := \{3x+1 : x \in \Delta_{\mathrm{odd}}\}$ is disjoint from $\Delta$, and
$|\Psi(\Delta)| = |\Delta| + |\Delta_{\mathrm{odd}}|$.**
Let $\Delta \in \mathrm{Cyc}(T)$, $p := |\Delta|$,
$r := |\Delta_{\mathrm{odd}}| \ge 1$ (P0.4), and fix $x \in \Delta$. By P0.1,
$T^p(x) = x$ and $k \mapsto T^k(x)$, $0 \le k \le p-1$, is a bijection onto $\Delta$;
hence $a_p(x) = \#\{0 \le k < p : T^k(x) \text{ odd}\} = r$ (D-9906). By P2(a) applied
with $n = x$:
$$C^{\,p + r}(x) = C^{\,c_p(x)}(x) = T^p(x) = x,$$
so the $C$-orbit of $x$ is purely periodic; let $\Gamma$ be its point set, a $C$-cycle
set. By P2(d) with $n = x$, using $V_T(x) = \Delta$ and
$\{z \in V_T(x): z \text{ odd}\} = \Delta_{\mathrm{odd}}$:
$$\Gamma = V_C(x) = \Delta \cup \{3z+1 : z \in \Delta_{\mathrm{odd}}\} = \Psi(\Delta).$$
So $\Psi(\Delta) \in \mathrm{Cyc}(C)$. Disjointness $N \cap \Delta = \emptyset$: if
$3z + 1 \in \Delta$ for some $z \in \Delta_{\mathrm{odd}}$, then
$T(3z+1) = (3z+1)/2 = T(z)$ (the first equality because $3z+1$ is even, the second by
definition of $T$ on the odd $z$), while $3z+1 \ne z$ (opposite parities); this
contradicts injectivity of $T|_\Delta$ (P0.1(iv)). Since $z \mapsto 3z+1$ is injective,
$|N| = r$ and $|\Psi(\Delta)| = p + r$; by P0.1(iii) this is also the least $C$-period of
each of its points.

**Step 7.4: $\Psi'$ maps $\mathrm{Cyc}(S)$ into $\mathrm{Cyc}(T)$; moreover $\Psi'(\Sigma)$
is the point set of the $T$-orbit of any $x \in \Sigma$, and $|\Psi'(\Sigma)| = K :=
\sum_{x \in \Sigma} a(x)$.**
Let $\Sigma \in \mathrm{Cyc}(S)$, $m := |\Sigma|$, and fix $x \in \Sigma$; then
$S^m(x) = x$ and $j \mapsto S^j(x) =: x_j$, $0 \le j \le m - 1$, is a bijection onto
$\Sigma$ (P0.1). Apply P3 with $n = x$ (so $e = 0$): $t_m = \sum_{j=0}^{m-1} a(x_j) = K
\ge m \ge 1$, and $T^{t_m}(x) = S^m(x) = x$ by P3(a). So the $T$-orbit of $x$ is purely
periodic; let $\Delta$ be its point set, a $T$-cycle set. By P3(e) with $n = x$,
$e = 0$, and $\{x_j : j \ge 0\} = \Sigma$:
$$\Delta = V_T(x) = \{x\} \cup \bigcup_{j \ge 0} \{(3x_j+1)/2^{\,i} : 1 \le i \le a(x_j)\}
= \Sigma \cup \{(3z+1)/2^{\,i} : z \in \Sigma,\ 1 \le i \le a(z) - 1\} = \Psi'(\Sigma).$$
(For the middle equality: the $i = a(x_j)$ term is $x_{j+1} \in \Sigma$, and $x = x_0 \in
\Sigma$; conversely every $z \in \Sigma$ equals some $x_j$ with $j \ge 0$, so $z = x_0$
or $z = x_j = (3x_{j-1}+1)/2^{a(x_{j-1})}$ appears, and every intermediate term appears
at time $t_j + i$.) Hence $\Psi'(\Sigma) \in \mathrm{Cyc}(T)$.
Least period: let $p$ be the least $T$-period of $x$. Since $T^p(x) = x$ is odd, P3(d)
(with $n = x$) forces $p = t_j$ for some $j \ge 0$, and then $S^j(x) = x$, so $m \mid j$
by P0.1(i) (the least $S$-period of $x$ is $m$, by P0.1(iii)-(iv) applied to $\Sigma$).
The least positive choice is $j = m$, giving $p = t_m = K$. By P0.1(iii),
$|\Psi'(\Sigma)| = |\Delta| = K$. (Byproduct: the $K - m$ listed intermediate elements
are pairwise distinct and disjoint from $\Sigma$; disjointness from $\Sigma$ also follows
directly since $(3z+1)/2^{\,i}$ has $\nu_2 = a(z) - i \ge 1$ for $i \le a(z)-1$, i.e. is
even, while $\Sigma$ is a set of odd numbers.)

**Step 7.5: the four compositions are identities.**

- $\Psi \circ \Phi = \mathrm{id}_{\mathrm{Cyc}(C)}$: with
  $R = \{3x+1 : x \in \Gamma_{\mathrm{odd}}\} \subseteq \Gamma$ (Step 7.1) and
  $(\Phi(\Gamma))_{\mathrm{odd}} = \Gamma_{\mathrm{odd}}$:
  $\Psi(\Phi(\Gamma)) = (\Gamma \setminus R) \cup \{3x+1 : x \in \Gamma_{\mathrm{odd}}\}
  = (\Gamma \setminus R) \cup R = \Gamma$.
- $\Phi \circ \Psi = \mathrm{id}_{\mathrm{Cyc}(T)}$: with
  $N = \{3x+1 : x \in \Delta_{\mathrm{odd}}\}$, $N \cap \Delta = \emptyset$ (Step 7.3),
  and $(\Psi(\Delta))_{\mathrm{odd}} = \Delta_{\mathrm{odd}}$ ($N$ consists of even
  numbers): $\Phi(\Psi(\Delta)) = (\Delta \cup N) \setminus
  \{3x + 1 : x \in \Delta_{\mathrm{odd}}\} = (\Delta \cup N) \setminus N = \Delta$.
- $\Phi' \circ \Psi' = \mathrm{id}_{\mathrm{Cyc}(S)}$: the elements of
  $\Psi'(\Sigma) \setminus \Sigma$ are even (end of Step 7.4) and the elements of
  $\Sigma$ are odd, so $(\Psi'(\Sigma))_{\mathrm{odd}} = \Sigma$.
- $\Psi' \circ \Phi' = \mathrm{id}_{\mathrm{Cyc}(T)}$: let $\Delta \in \mathrm{Cyc}(T)$
  and pick $x \in \Delta_{\mathrm{odd}}$ (P0.4). By Step 7.2,
  $\Sigma := \Delta_{\mathrm{odd}} \in \mathrm{Cyc}(S)$ and $x \in \Sigma$. By Step 7.4,
  $\Psi'(\Sigma)$ is the point set of the $T$-orbit of $x$ — which is $\Delta$, by
  P0.1(iv) applied to $x \in \Delta$. So $\Psi'(\Phi'(\Delta)) = \Delta$.

Hence $\Phi, \Psi$ are mutually inverse bijections between $\mathrm{Cyc}(C)$ and
$\mathrm{Cyc}(T)$, and $\Phi', \Psi'$ between $\mathrm{Cyc}(T)$ and $\mathrm{Cyc}(S)$.

**Step 7.6: trivial matches trivial; restriction to nontrivial cycles; composite.**
Direct computation: $\Phi(\{1,4,2\}) = \{1,4,2\} \setminus \{3 \cdot 1 + 1\} = \{1,2\}$
and $\Phi'(\{1,2\}) = \{1\}$; equivalently $\Psi(\{1,2\}) = \{1,2,4\}$,
$\Psi'(\{1\}) = \{1\} \cup \{(3 \cdot 1 + 1)/2^{\,i} : 1 \le i \le a(1) - 1\}
= \{1, 2\}$ (here $a(1) = \nu_2(4) = 2$; this is the $m = 1$ cycle case). Since $\Phi$ is
a bijection sending the trivial $C$-cycle to the trivial $T$-cycle, a $C$-cycle $\Gamma$
is nontrivial iff $\Phi(\Gamma)$ is nontrivial ($\Phi(\Gamma) = \{1,2\}$ would force
$\Gamma = \Psi(\{1,2\}) = \{1,4,2\}$); similarly for $\Phi'$. So each of $\Phi, \Psi,
\Phi', \Psi'$ restricts to a bijection between the sets of nontrivial cycles. The
composite $\Phi' \circ \Phi : \mathrm{Cyc}(C) \to \mathrm{Cyc}(S)$ is
$\Gamma \mapsto (\Phi(\Gamma))_{\mathrm{odd}} = \Gamma_{\mathrm{odd}}$ (Step 7.1), and
its inverse $\Psi \circ \Psi'$ sends $\Sigma$ to
$\Psi'(\Sigma) \cup \{3x+1 : x \in \Sigma\} = \Sigma \cup \{(3x+1)/2^{\,i} : x \in \Sigma,
\ 0 \le i \le a(x)-1\}$ (using $(\Psi'(\Sigma))_{\mathrm{odd}} = \Sigma$ and
$3x + 1 = (3x+1)/2^0$).

**Step 7.7: lengths.** For $\Sigma \in \mathrm{Cyc}(S)$ with $m = |\Sigma|$,
$K = \sum_{x \in \Sigma} a(x)$: Step 7.4 gives $|\Psi'(\Sigma)| = K$, and Step 7.3
applied to $\Delta = \Psi'(\Sigma)$ (with $\Delta_{\mathrm{odd}} = \Sigma$, so $r = m$)
gives $|\Psi(\Psi'(\Sigma))| = K + m$. By P0.1(iii) these cardinalities are the cycle
lengths (least periods). Sanity check on the trivial cycles: $m = 1$, $K = a(1) = 2$:
$T$-length $2$, $C$-length $3$. ✓ $\blacksquare$

*(Neutrality note: nothing above presupposes that nontrivial cycles exist in
$\mathbb{Z}^+$. If none exist for one of the maps, the bijections show none exist for the
other two, and all statements hold with the nontrivial-cycle sets empty. Per D-9909 the
file stays neutral on which situation obtains.)*

### Part 8 — the integer-orbit dichotomy and proof of L-9901.4

**Lemma D (dichotomy for integer orbits).** *Let $X \subseteq \mathbb{Z}^+$ be nonempty,
$f : X \to X$, and $n \in X$. Then exactly one of the following holds:*

*(A)* $O_f(n)$ is bounded; in this case $V_f(n)$ is finite, the orbit is eventually
periodic, and there are $i \ge 0$ and a cycle set $\Gamma$ of $f$ with $f^k(n) \in
\Gamma$ for all $k \ge i$; this $\Gamma$ is unique;

*(B)* $f^k(n) \to \infty$ as $k \to \infty$ (D-9907 divergence).

*Moreover, (A) is equivalent to each of: $V_f(n)$ finite; $O_f(n)$ eventually periodic;
$O_f(n)$ enters some cycle set of $f$.*

*Proof.*

**(1) Bounded $\Rightarrow$ enters a cycle.** Let $B := \sup V_f(n) < \infty$. Then
$V_f(n) \subseteq X \cap [1, B] \subseteq \{1, 2, \dots, B\}$, a **finite** set (this is
the integrality step; see the boxed remark). The infinite sequence $(f^k(n))_{k \ge 0}$
takes finitely many values, so there exist $0 \le i < j$ with $f^i(n) = f^j(n) =: z$.
Then $f^{\,j-i}(z) = z$ with $j - i \ge 1$, so $O_f(z)$ is purely periodic; let $\Gamma$
be its point set, a cycle set of $f$ (P0.2). For every $k \ge i$:
$f^k(n) = f^{\,k-i}(z) \in \Gamma$ (P0.1(iii)–(iv)).

**(2) Enters a cycle $\Rightarrow$ bounded, $V_f(n)$ finite, eventually periodic.** If
$f^k(n) \in \Gamma$ for all $k \ge i$, then
$V_f(n) \subseteq \{f^k(n) : 0 \le k < i\} \cup \Gamma$ is finite, hence the orbit is
bounded; and $f^{k + |\Gamma|}(n) = f^k(n)$ for $k \ge i$ by P0.1(i),(iv) (applied to the
point $f^i(n) \in \Gamma$: its least period is $|\Gamma|$, and every point of $\Gamma$
returns to itself after $|\Gamma|$ steps), so the orbit is eventually periodic.
Conversely, if the orbit is eventually periodic — $\exists i \ge 0, q \ge 1$ with
$f^{k+q}(n) = f^k(n)$ for all $k \ge i$ — then $z := f^i(n)$ satisfies $f^q(z) = z$, so
the orbit enters the cycle through $z$ as in (1). This proves the equivalences in the
"moreover" clause, given (1) and (3).

**(3) Unbounded $\Rightarrow$ divergent.** Suppose $O_f(n)$ is unbounded but *not*
divergent. Non-divergence means: there is $B \in \mathbb{Z}^+$ such that $f^k(n) \le B$
for infinitely many $k$. The values at those infinitely many indices lie in
$X \cap [1, B]$, a **finite** set, so by the pigeonhole principle some single value $z$
occurs at two distinct indices $i < j$ (indeed at infinitely many indices). As in (1),
the orbit is then eventually periodic and enters a cycle, hence bounded by (2) —
contradicting unboundedness. Therefore an unbounded orbit is divergent.

**(4) Exactly one of (A), (B).** If the orbit is divergent, it is unbounded: were
$f^k(n) \le B$ for all $k$, divergence ($f^k(n) > B$ for all large $k$) would fail. So
(A) and (B) are mutually exclusive; and every orbit is bounded or unbounded, with the
unbounded case forced into (B) by (3). Uniqueness of $\Gamma$ in (A): if the tail of the
orbit lies in cycle sets $\Gamma$ and $\Gamma'$, any tail point lies in
$\Gamma \cap \Gamma'$, so $\Gamma = \Gamma'$ by P0.3. $\square$

> **⚠ BOXED REMARK — the pigeonhole in Lemma D is valid ONLY for integer orbits.**
>
> Steps (1) and (3) rest on a single fact: *for every $B$, the set
> $\{x \in X : x \le B\} \subseteq \{1, \dots, B\}$ is finite*, because $X$ consists of
> positive integers. This is the only place integrality enters the trichotomy, and
> without it the implications "bounded $\Rightarrow$ eventually periodic" and
> "unbounded $\Rightarrow$ divergent" are unsupported **and in general false**:
>
> - **In $\mathbb{Z}_2$:** every orbit is bounded in the $2$-adic metric
>   ($|x|_2 \le 1$ for all $x \in \mathbb{Z}_2$), yet a $T$-orbit in $\mathbb{Z}_2$ is
>   eventually periodic only if its parity vector (D-9906) is eventually periodic, while
>   every infinite $0$–$1$ sequence — in particular every aperiodic one — occurs as the
>   parity vector of some $x \in \mathbb{Z}_2$ (parity-vector bijection; cf. L-9902,
>   cited as context only — nothing in the present file uses this). So
>   "bounded $\Rightarrow$ eventually periodic" fails badly in $\mathbb{Z}_2$.
> - **In $\mathbb{Q}$** (say rationals with odd denominator, where parity is defined
>   $2$-adically): an archimedean bound $B$ leaves infinitely many available values in
>   $[0, B]$, so the pigeonhole yields nothing; denominators may grow forever inside a
>   bounded interval.
>
> **Consequence for this project's symbolic-construction directions:** a symbolic,
> $2$-adic, or rational object with a bounded, $1$-avoiding, non-periodic orbit is *not*
> a Collatz counterexample and does *not* contradict L-9901.4. A genuine counterexample
> must be a positive integer, and for positive integers L-9901.4 leaves exactly two
> failure modes: a nontrivial cycle, or divergence $T^k(n) \to \infty$. In particular,
> "unbounded but non-divergent" behavior (e.g. $\liminf < \infty = \limsup$) is
> **impossible** for integer orbits and can only live in extensions; any construction
> exhibiting it has, for that very reason, left $\mathbb{Z}^+$.

**Proof of L-9901.4.** Apply Lemma D with $X = \mathbb{Z}^+$, $f = T$. Exactly one of:
(A) the orbit eventually enters a unique $T$-cycle set $\Gamma$; (B) $T^k(n) \to \infty$.
In case (A), $\Gamma$ is either the trivial cycle $\{1,2\}$ or a nontrivial $T$-cycle
(D-9908), and not both; by uniqueness of $\Gamma$ the two sub-cases are mutually
exclusive. This yields exactly one of (a), (b), (c). "Remains in it forever" is P0.1(iv)
(cycle sets are $T$-invariant). Edge cases: $n = 1$ and $n = 2$ are in the trivial cycle
at $k = 0$ (case (a) with entry time $0$).

The $C$-analogue is Lemma D with $X = \mathbb{Z}^+$, $f = C$, trivial cycle $\{1,4,2\}$.
The $S$-analogue is Lemma D with $X = \{\text{positive odd integers}\}$, $f = S$
(well-defined: $S$ maps $X$ into $X$), trivial cycle $\{1\}$, started at
$\mathrm{odd}(n)$. $\blacksquare$

### Part 9 — proof of L-9901.5

Fix $n \in \mathbb{Z}^+$ and $x_0 := \mathrm{odd}(n)$.

**Step 9.1 (case (a) is "reaching 1", for each map).** For each
$M \in \{C, T, S\}$ (with start $n$, $n$, $x_0$ respectively):
$$O_M \text{ enters the trivial cycle of } M \iff 1 \in O_M.$$
($\Leftarrow$) is immediate since $1$ lies in each trivial cycle. ($\Rightarrow$): for
$T$: if $T^k(n) \in \{1,2\}$, then $T^k(n) = 1$ or $T^{k+1}(n) = T(2) = 1$. For $C$: if
$C^k(n) \in \{1,4,2\}$, then one of $C^k(n), C^{k+1}(n), C^{k+2}(n)$ equals $1$ (follow
$4 \mapsto 2 \mapsto 1$). For $S$: $S^j(x_0) \in \{1\}$ means $S^j(x_0) = 1$.

**Step 9.2 (main dichotomy).** By D-9909, $n$ is a counterexample iff $1 \notin O_C(n)$.
By L-9901.1 this is equivalent to $1 \notin O_T(n)$, and to $1 \notin O_S(x_0)$. By Step
9.1, each of these says that case (a) of the corresponding trichotomy (L-9901.4 and its
$C$-, $S$-analogues) fails; and by the "exactly one" clause, failure of (a) is equivalent
to "(b) or (c)". This proves the equivalence of statements 1.–4. of L-9901.5.

**Step 9.3 (the failure modes match across the three maps).**

*Divergence cases match:* by Lemma D applied to each map, divergence is equivalent to
unboundedness of the respective orbit; by L-9901.2(iii) the three orbits are
simultaneously unbounded. Hence
$T^k(n) \to \infty \iff C^k(n) \to \infty \iff S^j(x_0) \to \infty$.

*Cycle cases match, with corresponding cycles:* suppose $O_T(n)$ eventually enters the
nontrivial $T$-cycle $\Delta$, say $T^k(n) \in \Delta$ for all $k \ge i$.

- ($T \Rightarrow C$.) For $j \ge c_i(n)$: locate $j \in [c_k, c_{k+1})$ with $k \ge i$
  (P2(b)); by P2(c), $C^j(n)$ equals $T^k(n) \in \Delta$ or $3\,T^k(n) + 1$ with
  $T^k(n) \in \Delta$ odd; either way $C^j(n) \in \Psi(\Delta)$. So the $C$-orbit
  eventually lies in $\Psi(\Delta)$. The $C$-orbit is bounded (Step 9.3 first part plus
  Lemma D, or directly L-9901.2), so by Lemma D it eventually enters a unique $C$-cycle
  $\Gamma$; a common tail point lies in $\Gamma \cap \Psi(\Delta)$, and both are cycle
  sets, so $\Gamma = \Psi(\Delta)$ by P0.3 — a nontrivial $C$-cycle (Step 7.6).
- ($T \Rightarrow S$.) The odd entries of the $T$-orbit at times $t_j \ge i$ lie in
  $\Delta_{\mathrm{odd}} = \Phi'(\Delta)$; by P3(d) these are exactly the entries
  $S^j(x_0)$ for all large $j$. As above, the $S$-orbit eventually enters a unique
  $S$-cycle, which by P0.3 must equal $\Phi'(\Delta)$ — nontrivial (Step 7.6).
- (Conversely.) If $O_C(n)$ eventually enters a nontrivial $C$-cycle $\Gamma$, then the
  $T$-orbit is bounded (L-9901.2(iii)) and, being non-(a) (Steps 8.1–8.2 applied via
  L-9901.1: $1 \in O_C(n)$ would follow from case (a) for $C$), it eventually enters a
  nontrivial $T$-cycle $\Delta'$ by the trichotomy; by the forward direction just proved
  and uniqueness (Lemma D(A) + P0.3), $\Psi(\Delta') = \Gamma$, i.e.
  $\Delta' = \Phi(\Gamma)$. The same argument links $S$ to $T$ via $\Psi'$, $\Phi'$.

$\blacksquare$

---

## Dependency audit

Used from NOTATION.md, with exact points of use:

- **D-9901 ($C$), D-9902 ($T$)**: definitions used throughout; the identities
  $T(m) = C^2(m)$ for odd $m$ and $T(m) = C(m)$ for even $m$ are re-derived, not assumed
  (P2 proof).
- **D-9903 ($\mathrm{odd}$), D-9904 ($S$, $a(x)$)**: P1, P3; $a(x) \ge 1$ is used in P3
  (strict increase of $t_j$) and Step 7.4.
- **D-9905 (orbits, $M^0 = \mathrm{id}$, reaching 1 with $k \ge 0$, trivial cycles)**:
  Part 4 edge cases; P0.2; Steps 6.6, 8.1.
- **D-9906 ($v_i$, $a_k$)**: P2 (definition of $c_k$); Step 7.3 ($a_p(x) = r$).
- **D-9907 (bounded/divergent)**: L-9901.2(iii), Lemma D.
- **D-9908 (cycles, least period, nontrivial, $S$-cycle data $m, a_i, K$)**: P0.1–P0.3
  (pure periodicity and least period), Part 7 (nontriviality, lengths $m$, $K$, $m+K$).
- **D-9909 (counterexample)**: Part 9.

External results: **none**. All finite-dynamics facts (P0.1–P0.5, Lemma D) are proved
inline. The boxed remark cites L-9902 (parity-vector bijection over $\mathbb{Z}_2$) as
*context only* for the claim that bounded non-periodic $T$-orbits exist in
$\mathbb{Z}_2$; no proof in this file depends on that claim, and the remark's normative
content ("the pigeonhole step requires finiteness of bounded integer sets") is
self-contained. No statement in this file assumes the Collatz conjecture or its negation;
all results are neutral (see the neutrality note at the end of Part 7).

Intra-file dependency order: P0 → P1 → P2 → P3 → Parts 4, 5 → Part 6 (uses P0, P2, P3) →
Part 7 (uses P0 only) → Part 8 (uses everything). No circularity: each part uses only
earlier parts.

## Gap audit

Checked deliberately against the README §8 list:

- **Hidden finiteness assumptions.** The single finiteness step (bounded sets of positive
  integers are finite) is isolated in Lemma D(1),(3) and flagged in the boxed remark. The
  value-set decompositions P2(d), P3(e) are proved for infinite orbits directly (index
  partitions), not by finite truncation.
- **Unjustified induction / missing bases.** All inductions have explicit bases: P0.1(i)
  ($\ell = 0$), P1 ($i = 0$), P2 ($k = 0$, $c_0 = 0$ via the empty-sum convention), P3
  ($j = 0$ via P1; inner induction base $i = 1$).
- **Boundary cases.** $n = 1$, $n = 2$, $n = 2^e$ (Part 4, Part 5, Part 7); $k = 0$ /
  $j = 0$ orbit membership (D-9905 allows it; used for $n = 1$); $e = \nu_2(n) = 0$
  (empty halving segment, P1/P3); $a(x) = 1$ (empty gap in P3, empty intermediate set in
  $\Psi'$); $m = 1$ cycles (fixed points; P0.5 explicitly allows $m = 1$; Step 7.6
  computes the $m = 1$ trivial $S$-cycle case end-to-end).
- **Empirical vs universal.** The Adversarial tests section is labeled finite
  verification; optimality examples in Part 6 are finite computations used only to show
  the stated constants cannot be improved, never to prove an inequality.
- **Limit interchanges.** None performed. "Divergent $\iff$ unbounded" is proved
  combinatorially (Lemma D(3),(4)), not by a limit argument.
- **Circular dependence.** None; see dependency order above. In particular Part 9 uses
  the trichotomy and the cycle bijections but neither uses Part 9.
- **Nonuniform estimates.** The bounds in L-9901.2(ii) contain the start-dependent term
  $\max(n, \cdot)$; this is displayed explicitly and shown necessary ($n = 2^{10}$). The
  bounds in (i) are uniform in $n$.
- **Assumptions equivalent to the conjecture.** None: every statement is an equivalence
  or bound valid for all $n$, whether or not counterexamples exist; the cycle bijections
  are proved without assuming nontrivial cycles exist (they may all be bijections between
  empty sets of nontrivial cycles).
- **Symbolic object vs integer trajectory.** All objects here are integer trajectories by
  construction; the boxed remark warns exactly about the non-integer case.
- **Subtle points double-checked.** (1) In Step 7.3 the disjointness
  $N \cap \Delta = \emptyset$ is *proved* (via injectivity of $T$ on a cycle), not
  assumed; without it $\Phi \circ \Psi = \mathrm{id}$ would fail. (2) In Step 7.4 the
  least $T$-period is shown to be exactly $K$ (not a proper divisor) via the odd-time
  classification P3(d); this is what makes the length claims exact. (3) The
  identification of cycles with point sets (P0.2) is proved, so the bijections of
  L-9901.3 are genuinely between cycles in the sense of D-9908 (up to starting point).
  (4) $(3M_S+1)/2$ in L-9901.2(ii) is an integer because a finite $M_S$ is attained and
  odd; for $M_S = \infty$ the conventions handle it.

## Adversarial tests

**Finite verification, not proof.** The following script (exact integer arithmetic,
deterministic, no dependencies) was run with `python3`
(script stored at `scratchpad/verify_L9901.py` during authoring; reproduced in full
here). It checks: the reach-1 equivalence for all $n \le 10^4$; the merge identity and
skipped-index classification (P2) stepwise for $n \le 2000$, $k \le 300$; the interleave
reconstruction of the $C$-orbit from the $T$-orbit; the odd-subsequence and return-time
formulas (P3) for $n \le 2000$; the value-set identities and the full inequality chain of
L-9901.2 for all $n \le 10^4$, including attainment of $M_C = 2M_T$; the action of
$\Phi, \Psi, \Phi', \Psi'$ on the trivial cycles; and — as a clearly labeled **extension
check outside the lemma's domain** — the mutual inverseness of the four cycle maps and
the length dictionary $m / K / m{+}K$ on the three known nontrivial cycles of the same
formulas over the negative integers (seeds $-1$, $-5$, $-17$), where nontrivial cycles
actually exist. L-9901 makes no claim about $\mathbb{Z}^-$; that test only exercises the
cycle-correspondence formulas on genuinely nontrivial cycles, which are unavailable (or
unknown) in $\mathbb{Z}^+$.

```python
#!/usr/bin/env python3
"""Finite verification for L-9901 (equivalence of C, T, S).
Exact integer arithmetic only.  Finite verification, NOT proof.
Agent: fable-02-p1.  2026-07-21.
Run: python3 verify_L9901.py
"""

def nu2(n):
    assert n != 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e

def oddpart(n):
    return n // (2 ** nu2(n))

def C(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def S(x):
    assert x % 2 != 0
    return oddpart(3 * x + 1)

def value_set(f, n):
    """Exact value set of the (eventually periodic) orbit of n under f.
    Iterates until the first repeated value; at that point the orbit has
    entered and fully traversed its cycle, so `seen` is the whole value set.
    Also returns the ordered sequence up to and incl. the first repeat."""
    seen, seq, x = set(), [], n
    while x not in seen:
        seen.add(x)
        seq.append(x)
        x = f(x)
    seq.append(x)
    return seen, seq

def prefix(f, n, k):
    out, x = [], n
    for _ in range(k):
        out.append(x)
        x = f(x)
    return out

N = 10 ** 4
NP = 2000     # bound for the more expensive stepwise checks
PLEN = 300    # prefix length for stepwise checks

# ---------- Test 1: reaching 1 is equivalent for C, T, S (n <= N) ----------
for n in range(1, N + 1):
    VC, _ = value_set(C, n)
    VT, _ = value_set(T, n)
    VS, _ = value_set(S, oddpart(n))
    rc, rt, rs = (1 in VC), (1 in VT), (1 in VS)
    assert rc == rt == rs, (n, rc, rt, rs)
    assert rc, n  # all n <= 10^4 in fact reach 1 (finite observation)
print(f"PASS test1: reach-1 equivalence (and reach-1 itself) for all n <= {N}")

# ---------- Test 2: merge identity T^k(n) = C^(k+a_k)(n), and skipped-index
# ----------          classification C^(c(k)+1)(n) = 3 T^k(n)+1 = 2 T^(k+1)(n) ----------
for n in range(1, NP + 1):
    Torb = prefix(T, n, PLEN + 1)
    a = 0
    Corb = prefix(C, n, 2 * PLEN + 3)
    for k in range(PLEN + 1):
        ck = k + a
        assert Corb[ck] == Torb[k], (n, k)
        if Torb[k] % 2 == 1 and k < PLEN:
            assert Corb[ck + 1] == 3 * Torb[k] + 1 == 2 * Torb[k + 1], (n, k)
            a += 1
print(f"PASS test2: merge identity and skipped-index classification, n <= {NP}, k <= {PLEN}")

# ---------- Test 3: C-prefix reconstructed by interleaving from T-prefix ----------
for n in range(1, NP + 1):
    Torb = prefix(T, n, PLEN)
    rec = []
    for m in Torb:
        rec.append(m)
        if m % 2 == 1:
            rec.append(3 * m + 1)
    Corb = prefix(C, n, len(rec))
    assert rec[:len(Corb)] == Corb, n
print(f"PASS test3: C-orbit prefix = interleaving of T-orbit prefix, n <= {NP}")

# ---------- Test 4: odd subsequence of O_T(n) = O_S(odd(n)); return times ----------
for n in range(1, NP + 1):
    # collect first 60 odd elements of the T-orbit with their times
    odds, times, x, k = [], [], n, 0
    while len(odds) < 60:
        if x % 2 == 1:
            odds.append(x)
            times.append(k)
        x = T(x)
        k += 1
        assert k < 10 ** 6
    Sorb = prefix(S, oddpart(n), 60)
    assert odds == Sorb, n
    assert times[0] == nu2(n) if n % 2 == 0 else times[0] == 0
    for j in range(59):
        assert times[j + 1] - times[j] == nu2(3 * odds[j] + 1), (n, j)
print(f"PASS test4: odd subsequence of O_T = O_S(odd(n)); t_(j+1)-t_j = a(x_j); t_0 = nu2(n); n <= {NP}")

# ---------- Test 5: value-set identities and sup inequalities (n <= N) ----------
eq_2MT = 0
for n in range(1, N + 1):
    VC, _ = value_set(C, n)
    VT, _ = value_set(T, n)
    VS, _ = value_set(S, oddpart(n))
    assert VS == {x for x in VT if x % 2 == 1}, n
    assert VS == {x for x in VC if x % 2 == 1}, n
    assert VC == VT | {3 * x + 1 for x in VT if x % 2 == 1}, n
    MC, MT, MS = max(VC), max(VT), max(VS)
    assert MS <= MT <= MC <= 2 * MT, n
    assert MT <= max(n, (3 * MS + 1) // 2), n   # (3*MS+1)/2 is an integer: MS odd
    assert MC <= max(n, 3 * MS + 1), n
    if MC == 2 * MT:
        eq_2MT += 1
print(f"PASS test5: value-set identities and sup chain for all n <= {N}; "
      f"MC = 2*MT attained for {eq_2MT} of {N} starts (bound optimal)")

# ---------- Test 6: cycle maps on the trivial cycles ----------
def Phi(G):   # C-cycle -> T-cycle
    return G - {3 * x + 1 for x in G if x % 2 != 0}
def Psi(D):   # T-cycle -> C-cycle
    return D | {3 * x + 1 for x in D if x % 2 != 0}
def PhiP(D):  # T-cycle -> S-cycle
    return {x for x in D if x % 2 != 0}
def PsiP(Sig):  # S-cycle -> T-cycle
    out = set(Sig)
    for x in Sig:
        ax = nu2(3 * x + 1)
        for i in range(1, ax):
            out.add((3 * x + 1) // 2 ** i)
    return out

assert Phi({1, 4, 2}) == {1, 2}
assert Psi({1, 2}) == {1, 4, 2}
assert PhiP({1, 2}) == {1}
assert PsiP({1}) == {1, 2}
assert PhiP(Phi({1, 4, 2})) == {1}          # composite C -> S is odd restriction
assert Psi(PsiP({1})) == {1, 4, 2}
print("PASS test6: Phi/Psi/Phi'/Psi' exchange the trivial cycles {1,4,2} <-> {1,2} <-> {1}")

# ---------- Test 7 (EXTENSION CHECK, outside the lemma's domain Z+): ----------
# The known nontrivial cycles of the same formulas on negative integers.
# L-9901 makes NO claim about Z-; this only exercises the cycle-correspondence
# formulas on genuinely nontrivial cycles, which are unavailable in Z+.
for seed in (-1, -5, -17):
    GC, seqC = value_set(C, seed)
    GT, seqT = value_set(T, seed)
    GS, seqS = value_set(S, seed)
    assert seqC[-1] == seed and seqT[-1] == seed and seqS[-1] == seed  # purely periodic
    assert Phi(GC) == GT, seed
    assert Psi(GT) == GC, seed
    assert PhiP(GT) == GS, seed
    assert PsiP(GS) == GT, seed
    m = len(GS)
    K = sum(nu2(3 * x + 1) for x in GS)
    assert len(GT) == K and len(GC) == m + K, seed
    print(f"PASS test7: seed {seed}: |S-cycle| m = {m}, |T-cycle| = K = {K}, "
          f"|C-cycle| = m+K = {m + K}; Phi/Psi/Phi'/Psi' are mutually inverse on it")

print("ALL TESTS PASSED")
```

**Observed output** (python3, single run, ~2 s wall time, 2026-07-21):

```text
PASS test1: reach-1 equivalence (and reach-1 itself) for all n <= 10000
PASS test2: merge identity and skipped-index classification, n <= 2000, k <= 300
PASS test3: C-orbit prefix = interleaving of T-orbit prefix, n <= 2000
PASS test4: odd subsequence of O_T = O_S(odd(n)); t_(j+1)-t_j = a(x_j); t_0 = nu2(n); n <= 2000
PASS test5: value-set identities and sup chain for all n <= 10000; MC = 2*MT attained for 7436 of 10000 starts (bound optimal)
PASS test6: Phi/Psi/Phi'/Psi' exchange the trivial cycles {1,4,2} <-> {1,2} <-> {1}
PASS test7: seed -1: |S-cycle| m = 1, |T-cycle| = K = 1, |C-cycle| = m+K = 2; Phi/Psi/Phi'/Psi' are mutually inverse on it
PASS test7: seed -5: |S-cycle| m = 2, |T-cycle| = K = 3, |C-cycle| = m+K = 5; Phi/Psi/Phi'/Psi' are mutually inverse on it
PASS test7: seed -17: |S-cycle| m = 7, |T-cycle| = K = 11, |C-cycle| = m+K = 18; Phi/Psi/Phi'/Psi' are mutually inverse on it
ALL TESTS PASSED
```

**Interpretation and limitations.** All checks passed. Test 7 is particularly meaningful:
on the negative-integer extension the formulas $\Phi, \Psi, \Phi', \Psi'$ are exercised
on *nontrivial* cycles of lengths up to 18 (including an $m = 1$ nontrivial fixed point
at $-1$ with $a(-1) = 1$, exercising the empty-intermediate edge case) and behave exactly
as L-9901.3 predicts, including the length dictionary $m / K / m{+}K$. None of this is
proof; the ranges are finite ($n \le 10^4$, prefixes $\le 300$, 60 odd terms) and the
$\mathbb{Z}^-$ check lies outside the lemma's stated scope.

## Remaining uncertainty

- I am confident in Parts 0–5 and 7–8; they are elementary and were checked line by line
  against the edge cases listed in the Gap audit.
- The part a verifier should probe hardest is **Part 7** (cycle bijections): the
  disjointness argument $N \cap \Delta = \emptyset$ in Step 7.3, the least-period
  argument $p = t_m = K$ in Step 6.4, and the use of P0.5 (first-return) in Steps
  6.1–6.2, since these carry the "mutually inverse" claims. Each is short but
  load-bearing; an independent reconstruction (e.g. via the alternative route
  $\Phi(\Gamma) = C(\Gamma_{\mathrm{even}})$) would be valuable.
- The boxed remark's first bullet asserts existence of bounded non-periodic $T$-orbits in
  $\mathbb{Z}_2$ by appeal to the parity-vector bijection (L-9902, context only). If a
  reviewer wants the remark fully self-contained, that sentence can be weakened to "the
  pigeonhole argument is unavailable in $\mathbb{Z}_2$" without affecting anything else
  in this file.
- The statement assigned to me suggested the bound $\sup O_C \le 3 \sup O_T + 1$ as an
  example; the constants proved here ($\sup O_C \le 2 \sup O_T$, with equality attained)
  are sharper, and no correction of the assigned statements was needed — all five claims
  are proved as stated (with the constants of .2 made explicit and shown optimal).

## Suggested next attack

1. **Independent verification** (any reviewer agent): reconstruct Part 7 from scratch,
   ideally via the return-map-free route (direct index bookkeeping with P2/P3), and
   re-run/extend the script (larger $n$, longer prefixes, randomized large starts). On
   success, upgrade Status per README §7 and record under `Reviewing agents:`.
2. **Issue #10:** restate the sanctuary condition using L-9901.5: a forward-invariant
   $A \subseteq \mathbb{Z}^+$ with $A \cap \{1, 2\} = \emptyset$ (for $T$) forces every
   orbit entering $A$ into "nontrivial cycle inside the bounded case, or divergence";
   combining with L-9901.2 lets the sanctuary be designed in $S$-coordinates where the
   bookkeeping is lightest.
3. **Issue #21 / T-9602:** cite Lemma D(3) directly for "unbounded $\Rightarrow$
   divergent for integer orbits"; the boxed remark is the exact statement of where that
   step's validity ends, which T-9602's 2-adic limiting arguments must respect.
4. **Extension lemma (new file, e.g. L-99xx):** the proofs of P1–P3 and Part 7 use
   positivity only through P0.4's "$x(2^p - 1) = 0$" step and Lemma D; formalize the
   verbatim extension of the cycle bijections to $\mathbb{Z} \setminus \{0\}$ (test 7
   passes on it), giving cycle programs three extra genuinely nontrivial worked examples
   and a cross-check target for any proposed $\mathbb{Z}^+$ cycle equation (cf. the
   D-9908 data $m, K$ and L-9905).
5. **Exploit for divergence programs:** L-9901.2 shows any divergence construction may be
   carried out for $S$ alone; combine with P3(e) to translate an $S$-growth certificate
   into explicit $C$/$T$ orbit envelopes with the constants of L-9901.2.

---

*File authored and signed by agent `fable-02-p1`, 2026-07-21. Status PROPOSED; not yet
independently reviewed.*
