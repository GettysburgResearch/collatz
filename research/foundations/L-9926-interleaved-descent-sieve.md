# L-9926 — The interleaved descent–doubling sieve: exact {D,M}-word calculus, the cap-free survivor set Int(k), the universal 3-adic backward congruences, and the failure of the collapse analogue

```text
Claim ID: L-9926
Title: The exact affine calculus of backward words over the moves D(z) = (2z-1)/3
       and M(z) = 2z; class-uniform kill certificates and the proved word-length
       bound |w| <= j that removes L-9919.8's word-length cap; the exact
       interleaved survivor sieve Int(k) mod 2^k computed for k <= 26; the
       universal (class-independent) 3-adic congruences mu != 2 mod 3,
       mu != 4 mod 9, mu != 10 mod 81; the exact joint pair sieve mod 2^k 3^D,
       its product form at depth <= 3 and the PROVED failure of any clean
       collapse analogue at depth 4; and an honest bounded-factor-vs-rate verdict
Status: PROVED
Authoring agent: fable-02-p20
Reviewing agents: fable-02-v28 (adversarial review 2026-07-27: PASS)
Created: 2026-07-26
Last updated: 2026-07-27 (fable-02-v28 review: PASS; status PROPOSED -> PROVED;
              sub-claims L-9926.4(2a) and L-9926.5 remain PARTIAL exactly as
              marked, with their verified ranges extended by the review)
Dependencies: research/foundations/NOTATION.md (D-9901 C, D-9902 T, D-9905 orbits,
              D-9906 parity vector, D-9909 counterexample, D-9910 stopping time);
              L-9902 (PROVED) — parity word of n depends only on n mod 2^k;
                classes mod 2^k <-> words of length k bijectively, two lifts;
              L-9903 (PROVED) — T^j(n) = (3^{a_j} n + rho_j)/2^j, rho_j a
                function of the parity word only;
              L-9909 (PROVED) — L-9909.2(B)(F)(E)(M) (closure of the
                counterexample set, mu odd, mu = 3 mod 4), L-9909.3/4 (the
                uniform-descent sieve and its survivor tables), X-9901
                (every n <= 10^6 reaches 1, finite verification inside L-9909);
              L-9911 (PROVED) — U2 (two-sided closure), U3 (T-preimage
                characterization), L-9911.1 (orbit floor);
              L-9919 (PROVED) — L-9919.1 (descent map D), L-9919.2
                (d(y) = nu_3(y+1), the shifted coordinate), L-9919.4 (the
                shifted iteration formula 2^j(T^j(n)+1) = 3^{a_j}u + delta_j,
                the augmented sieve Aug(k), the 3-adic collapse for the
                pure-descent family), L-9919.8 (PARTIAL — soundness of the
                backward-word (P,Q) machinery, reviewer-verified; its measured
                strength table is superseded by L-9926.3 below);
              X-9903 (EMPIRICAL, reviewed) — verified floor 10^12 (see the
                tier-honest citation in L-9926.4(4); no result here needs more
                than mu > 25, so even X-9901 discharges every threshold).
Scope: Everything about words, residue classes, certificates and the finite
       computations is UNCONDITIONAL. Every statement about mu (the minimal
       counterexample) is CONDITIONAL on hypothesis (H) below and tagged [H].
       Exact finite computations are labelled as such and never extrapolated.
       Sub-claims L-9926.4(2a) (depth <= 3 class-independence) and the rate
       verdict L-9926.5 are finite-range statements and are labelled PARTIAL.
Related counterexample candidates: none
```

Notation is exactly `research/foundations/NOTATION.md` plus L-9919's shifted
coordinate. Throughout, $T$ is the shortcut map (D-9902), $v_i(n) = T^i(n) \bmod 2$,
$a_j(n) = \sum_{i<j} v_i(n)$ (D-9906), $\gamma = \log_3 2$, $\nu_3$ the $3$-adic
valuation with $\nu_3(0) := +\infty$, and $u := n+1$ (or $z+1$) the shifted
coordinate. $\rho_j$, and the shifted remainder $\delta_j := \rho_j + 2^j - 3^{a_j}$,
are the word functions of L-9903 / L-9919.4; both depend only on $n \bmod 2^j$
(L-9902/L-9903). $\mathrm{Aug}(k)$ is L-9919.4's augmented survivor set;
"L-9909$(k)$" is L-9909.3's $k$-survivor set.

---

## Standing hypothesis

> **(H)** — **ASSUME** the counterexample set
> $$X := \{\, n \in \mathbb{Z}^+ : 1 \notin O_C(n) \,\}$$
> (D-9909) is **nonempty**, and let $\mu := \min X$. Every statement tagged **[H]**
> is conditional on (H). This file does not assert $X \neq \varnothing$; all
> untagged statements are unconditional facts about $T$, residue classes, words
> and finite computations.

---

## Statement

### L-9926.1 (the {D,M}-word calculus)

The two **backward moves** on $\mathbb{Z}^+$ are
$$\mathsf{M}(z) := 2z \quad (\text{always defined}), \qquad
  \mathsf{D}(z) := \frac{2z-1}{3} \quad (\text{defined iff } z \equiv 2 \bmod 3),$$
the complete set of single-step $T$-preimages of $z$ (L-9911 U3 / L-9919.1(3)):
$T(\mathsf{M}(z)) = T(\mathsf{D}(z)) = z$, $\mathsf{M}(z)$ even, $\mathsf{D}(z)$ odd,
$\mathsf{D}(z) < z$. A **word** $w = w_1 w_2 \cdots w_L \in \{\mathsf{D},\mathsf{M}\}^L$
is applied left to right: $z_0 \mapsto z_1 \mapsto \cdots \mapsto z_L =: w(z_0)$;
$w$ is **defined at** $z_0$ iff every $\mathsf{D}$-step's congruence holds. Write
$L = |w|$, $a = \#\mathsf{D}(w)$, $b = \#\mathsf{M}(w) = L - a$. Then, for every
$z \in \mathbb{Z}^+$ at which $w$ is defined:

1. **(Affine form and the word constant.)**
   $$\boxed{\;w(z) + 1 \;=\; \frac{2^{L}\,(z+1) \;-\; c_w}{3^{a}}\;}$$
   where the **word constant** $c_w \in \mathbb{Z}_{\ge 0}$ obeys the recursion
   $$c_\varepsilon = 0, \qquad c_{w\mathsf{D}} = 2c_w, \qquad
     c_{w\mathsf{M}} = 2c_w + 3^{\#\mathsf{D}(w)},$$
   with closed form $c_w = \sum_{i:\, w_i = \mathsf{M}} 2^{\,L-i}\, 3^{\,d_i}$,
   $d_i := \#\{l < i : w_l = \mathsf{D}\}$. Moreover $c_w = 0$ iff $w$ is all-$\mathsf{D}$
   (recovering L-9919.2(1) exactly), and the same statement in the unshifted
   coordinate reads $w(z) = (2^L z - c'_w)/3^a$ with $c'_w = c_w - 2^L + 3^a$.
   *(Correction to the framing this file was assigned: the shifted coordinate is
   NOT multiplicative for $\mathsf{M}$ — $\mathsf{M}(z) + 1 = 2(z+1) - 1$ — so no
   single "multiply by $2/3$ or $2$" bookkeeping exists; the right bookkeeping is
   the affine pair $(2^L, c_w)$ with the recursion above, in which $\mathsf{D}$
   contributes no constant and $\mathsf{M}$ contributes $3^{\#\mathsf{D}\text{-so-far}}$,
   subsequently doubled once per later move.)*

2. **(Legality is a single congruence mod $3^{\#\mathsf{D}}$.)** The domain
   $$\mathrm{Dom}(w) := \{ z \in \mathbb{Z}^+ : w \text{ defined at } z \}
     = \{ z \in \mathbb{Z}^+ : z + 1 \equiv t_w \bmod 3^{a} \}$$
   is the trace on $\mathbb{Z}^+$ of a **single congruence class** $t_w \bmod 3^a$
   in the shifted coordinate, and $t_w$ is computable by an explicit refinement
   recursion (each successive $\mathsf{D}$ refines the class by exactly one $3$-adic
   digit; the refinement is always nonempty). For the pure calculus the modulus is a
   power of $3$ alone; the mixed modulus $2^\alpha 3^\beta$ promised in the assigned
   framing appears exactly when the constraint is transported to $n$ through a
   $2$-adic class — see L-9926.2(2): there the legality set within a class
   $r \bmod 2^j$ is a single class modulo $2^j 3^{\max(0,\,a - a_j)}$.

3. **(Value criterion — exact.)** For $z \in \mathrm{Dom}(w)$:
   $$w(z) < z \iff (z+1)\,\bigl(2^{L} - 3^{a}\bigr) < c_w .$$
   Hence exactly three regimes:
   * $2^{L} < 3^{a}$ (i.e. $b < a(\log_2 3 - 1)$): $w(z) < z$ for **every**
     $z \in \mathrm{Dom}(w)$ — call such $w$ **contracting**;
   * $2^{L} > 3^{a}$: $w(z) < z$ only on the finite set
     $z + 1 < c_w/(2^L - 3^a)$;
   * $2^{L} = 3^{a}$ only for the empty word.
   The move **positions** enter only through $c_w$ (hence through the threshold),
   not through the regime.

4. **(Positivity never binds; inversion; closure.)** If $z_0 \in \mathbb{Z}^+$ and
   every $\mathsf{D}$-congruence holds, then **every** intermediate $z_i$ is
   automatically in $\mathbb{Z}^+$ — no positivity side condition exists.
   (This extends L-9919.2(3) from pure descents to arbitrary words, and it
   **corrects L-9919.8(1)**: the per-node positivity thresholds carried there are
   sound but redundant; e.g. the witness kill of class $63 \bmod 256$ has true
   threshold $-1$, not $5/3$.) Moreover $T^{L}(w(z_0)) = z_0$, and by L-9911 U2
   iterated, $w(z_0) \in X \iff z_0 \in X$.

5. **(Universal congruence corollary.)** For every contracting word $w$
   ($2^{|w|} < 3^{\#\mathsf{D}(w)}$): every $z \in \mathrm{Dom}(w)$ has a
   $T$-preimage-chain ancestor $w(z) < z$. **[H]** Hence $\mu \notin \mathrm{Dom}(w)$,
   a congruence exclusion **modulo a pure power of 3, independent of any 2-adic
   information and with no exceptional bound at all**. Instances: $w = \mathsf{D}$
   gives $\mu \not\equiv 2 \bmod 3$ (= L-9919.1(5)); $w = \mathsf{MDD}$ gives
   $$\boxed{\ \mu \not\equiv 4 \pmod 9\ }$$
   (every $n \equiv 4 \bmod 9$ has $T^3\bigl(\tfrac{8n-5}{9}\bigr) = n$ with
   $\tfrac{8n-5}{9} < n$); $w = \mathsf{MDMDDD}$ gives
   $\boxed{\mu \not\equiv 10 \bmod 81}$. The full family is quantified in
   L-9926.4(1).

### L-9926.2 (the interleaved sieve: uniformity, kills, the length bound, Int(k))

Fix $k \ge 1$ and a class $r \bmod 2^k$ with word data $a_j, \delta_j$
($0 \le j \le k$; L-9902/L-9903/L-9919.4). Fix $j \le k$ and apply words at
$z_0 := T^j(n)$, whose shifted form is $2^j(z_0 + 1) = 3^{a_j} u + \delta_j$
(L-9919.4(1)), $u = n+1$.

1. **(Sieve state identity.)** For a prefix $p$ of $w$ with $i$ moves and $e$
   $\mathsf{D}$'s, and every $n$ in the class at which $p$ is defined at $T^j(n)$:
   $$2^j\, 3^{e}\, (z_i + 1) \;=\; 2^{i}\,\bigl(3^{a_j} u + \delta_j\bigr) \;-\; 2^j c_p ,$$
   with $c_p$ the word constant of L-9926.1(1). When $e \le a_j$ this is
   $z_i + 1 = (P_i u + Q_i)/2^j$ with
   $$P_i = 2^{i}\,3^{\,a_j - e} \in \mathbb{Z}^+, \qquad
     Q_i = \frac{2^{i}\delta_j - 2^j c_p}{3^{e}} \in \mathbb{Z},$$
   and the recursions $(P,Q)$ start $(3^{a_j}, \delta_j)$;
   $\mathsf{M}: (P,Q) \mapsto (2P,\, 2Q - 2^j)$;
   $\mathsf{D}: (P,Q) \mapsto (2P/3,\, 2Q/3)$ — exactly L-9919.8(1)'s bookkeeping,
   now derived from the word constant.

2. **(Uniformity trichotomy — the analogue of L-9919.4(2).)** For each $(j, w)$,
   exactly one of:
   * **(U) class-uniform:** at every $\mathsf{D}$-step the current state has
     $3 \mid P$ and $3 \mid Q$ (equivalently: every $\mathsf{D}$ is applied with
     $e < a_j$ and the $n$-free divisibility $3^{e+1} \mid 2^{i}\delta_j - 2^j c_p$
     holds). Then $w$ is defined at $T^j(n)$ for **every** $n \ge 1$ in the class —
     no exceptional bound, by L-9926.1(4).
   * **(V) void:** some $\mathsf{D}$-step with $e < a_j$ fails its $n$-free
     divisibility. Then $w$ is defined at $T^j(n)$ for **no** $n$ in the class.
   * **(N) $n$-dependent:** all $\mathsf{D}$-steps with $e < a_j$ pass, and $w$ has
     $a > a_j$ $\mathsf{D}$'s. Then the set of $n$ in the class at which $w$ is
     defined is **exactly one congruence class of $u$ modulo $3^{\,m}$,
     $m = a - a_j \ge 1$** (never empty): each $\mathsf{D}$ past depth $a_j$
     refines by one $3$-adic digit. Within $\mathbb{Z}$, the legality set is a
     single class modulo $2^j 3^{m}$ (CRT with the $2$-adic class mod $2^j$;
     kills at $(j,w)$ depend on $r$ only through $r \bmod 2^j$).

3. **(Kill classification, with exact thresholds.)** Let $(j,w)$ be type (U), with
   terminal state $(P_L, Q_L)$, $P_L = 2^{L} 3^{\,a_j - a}$. Exactly one of:
   * $P_L < 2^j$: then for every $n$ in the class,
     $w(T^j(n)) < n \iff n > \theta_{j,w} := \dfrac{Q_L}{2^j - P_L} - 1$
     — a **class-uniform kill** with rational threshold $\theta_{j,w}$;
   * $P_L = 2^j$ (forces $L = j$, $a = a_j$): $w(T^j(n)) - n = Q_L/2^j$ is a
     **constant integer shift**; a kill (for every $n$) iff $Q_L < 0$;
   * $P_L > 2^j$: $w(T^j(n)) \ge n$ for all $n$ above a bound — never a kill
     above a threshold.
   For type (N) with $m \ge 1$ and value coefficient
   $\Delta := 2^j 3^{a} - 2^{L} 3^{a_j}$: the exact kill condition is
   $u\,\Delta > 2^{L}\delta_j - 2^{j} c_w$; so if $\Delta > 0$ the word kills
   exactly the $n$ in its legality class with
   $n > \theta^{(N)}_{j,w} := (2^{L}\delta_j - 2^{j} c_w)/\Delta - 1$, and if
   $\Delta < 0$ only finitely many $n$ (none above a bound). ($\Delta = 0$ with
   $m \ge 1$ is impossible by unique factorisation.)
   The $\mathsf{D}$-only specialisation of the (U)-kill reproduces L-9919.4(3)'s
   $\theta_{j,d}$ **exactly**; hence every Aug-kill is an Int-kill.

4. **(THE LENGTH BOUND — cap removal.)** Every class-uniform kill $(j,w)$
   satisfies $$\#\mathsf{D}(w) \le a_j \quad\text{and}\quad |w| \le j,$$
   with $|w| = j$ only in the $P_L = 2^j$ boundary case. Consequently "does the
   class $r \bmod 2^j$ admit a class-uniform kill at index $j$" is decided by a
   **finite** search over words of length $\le j$, and the survivor set defined in
   (5) is **exactly computable — L-9919.8's word-length cap is removed, not
   merely enlarged.** (For $n$-dependent kills at refinement depth $m$ the same
   argument gives $|w| < j + m\log_2 3$; used in L-9926.4(2).)

5. **(The interleaved survivor set.)**
   $$\mathrm{Int}(k) := \{\, r \bmod 2^k \;:\; \text{no } j \le k \text{ and word } w
     \text{ give a class-uniform kill at } (j, w) \,\}.$$
   Then $$\mathrm{Int}(k) \subseteq \mathrm{Aug}(k) \subseteq \text{L-9909}(k)$$
   (first inclusion: $\mathsf{D}$-only words realise every Aug-kill by (3);
   second: L-9919.4(4)). Killing is a property of the prefix class $r \bmod 2^{j}$,
   so survivor classes form a subtree exactly as in L-9909/L-9919.

6. **(Sieve theorem and exceptional bound.)** Define $B^{\mathrm{int}}_k$ as the
   maximum, over classes $r \bmod 2^{k'}$ ($k' \le k$) that die at level $k'$ with
   all proper prefixes alive, of the **least** threshold $\theta$ among the
   class-uniform kills at $(r, j = k')$. Then, **unconditionally**: for every
   $n > B^{\mathrm{int}}_k$ whose class mod $2^k$ is not in $\mathrm{Int}(k)$,
   there exist $j \le k$ and a word $w$ with $z := w(T^j(n)) \in \mathbb{Z}^+$,
   $T^{|w|}(z) = T^j(n)$, and $z < n$ — i.e. $n$'s orbit is reached by the orbit
   of a strictly smaller integer within $|w| + j$ steps of bookkeeping.
   **[H]** Hence if $\mu > B^{\mathrm{int}}_k$ then $\mu \bmod 2^k \in \mathrm{Int}(k)$.
   (Computed: $B^{\mathrm{int}}_k = 319/13 < 25$ for $8 \le k \le 20$, identical
   to $B^{\mathrm{aug}}_k$; see L-9926.3(d).)

7. **(Structure of $n$-dependent kills — head/tail factorisation.)** Suppose the
   class $r \bmod 2^j$ has **no** class-uniform kill at any index $\le j$, and
   $(j, w)$ is an $n$-dependent kill of refinement depth $m \ge 1$. Then
   $w = h\,t$ where the head $h$ (everything before the first $\mathsf{D}$ at
   $e = a_j$) is class-uniform with exactly $a_j$ $\mathsf{D}$'s,
   $P_h = 2^{|h|}$, $2^j \mid Q_h$, and $|h| \ge j$ (else $h$ itself would be a
   class-uniform kill); and the tail $t$ satisfies
   $2^{|t|} < 3^{m}\,2^{\,j - |h|} \le 3^m$ — **the tail is contracting**.
   In particular for $m = 1$: $|h| = j$, $t = \mathsf{D}$, the head lands on the
   integer $z_h = n + Q_h/2^j$ (a "level-$j$ cousin" of $n$: $T^j(z_h) = T^j(n)$
   with the same odd-step count), survivorship forces $Q_h \ge 0$, and the killed
   class is $u \equiv -Q_h \cdot 2^{-j} \bmod 3$ — which is the already-known class
   $u \equiv 0 \bmod 3$ **iff** $3 \mid Q_h$, i.e. iff the cousin satisfies
   $z_h \equiv n \bmod 3$. (Whether discordant cousins occur on survivors is the
   depth-1 collapse question; computed answer in L-9926.4(2): none for $k \le 14$.)

### L-9926.3 (exact computation — all finite, scripts + real outputs below)

**(a) Counts, with the gate.** The cap-12 algorithm of L-9919.8(3) is reproduced
exactly — $7/16/46/144/436/1366$ at $k = 6/8/10/12/14/16$ — and the **exact**
(cap-free, by L-9926.2(4)) computation gives:

| $k$ | 1–5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L-9909 | 1,1,2,3,4 | 8 | 13 | 19 | 38 | 64 | 128 | 226 | 367 | 734 | 1295 | 2114 |
| Aug (L-9919) | 1,1,2,3,4 | 7 | 12 | 18 | 32 | 57 | 102 | 192 | 324 | 593 | 1100 | 1855 |
| **Int (exact)** | 1,1,2,3,4 | 7 | **11** | **16** | **27** | **46** | **80** | **144** | **242** | **436** | **802** | **1363** |

| $k$ | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|
| L-9909 | 4228 | 7495 | 14990 | 27328 | 46611 | 93222 | 168807 | 286581 | 573162 | 1037374 |
| Aug | 3407 | 6329 | 11698 | 22384 | 39549 | 73718 | 139084 | 243479 | 453678 | 854473 |
| **Int** | **2499** | **4600** | **8463** | **15870** | **28147** | **52176** | **97978** | **172868** | **322021** | **602780** |

The cap mattered: at $k = 16$ the true count is $1363$, not L-9919.8's $1366$;
the three recovered classes are $16383$, $24575$, $57343 \bmod 2^{16}$, killed by
words of length $13$–$14$ (e.g. $\mathsf{DMDDDDDDDDDDD}$ at $j = 15$, threshold
$-1$). The first strictly-interleaved kill is at $k = 7$: class $95 \bmod 128$,
word $\mathsf{DMDDD}$ at $j = 7$, chain $182 \to 121 \to 242 \to 161 \to 107 \to 71$,
$71 < 95$, threshold $-1$ (L-9919.8's table, which sampled even $k$ only, first
shows a gain at $k = 8$).

**(b) Explicit lists.** $\mathrm{Int}(k)$ for $k \le 12$ is printed in full by the
script (PART B); e.g. $\mathrm{Int}(8) =$ Aug's 18-element list mod 256 **minus**
$\{63, 223\}$ = $\{27, 31, 47, 71, 91, 103, 111, 127, 155, 159, 167, 191, 231,
239, 251, 255\}$.

**(c) Certificates.** Every one of the 461 killed prefixes at levels $\le 16$
carries an explicit certificate $(j, w, \theta)$, each verified by direct integer
iteration on 3 representatives (1382 checks, 0 failures). Kills at levels
$\le 20$: 2879 certificates; 1154 of the minimum-threshold kill words contain
$\mathsf{M}$-moves; the longest needed has length 18; the boundary case
$P_L = 2^j,\ Q_L < 0$ never occurs as a min-threshold kill for $k \le 20$
(it is needed for the completeness proof, not in practice).

**(d) Exceptional bound.** $B^{\mathrm{int}}_k$: $0, 1, 1, 1$, then $23/5$ for
$5 \le k \le 7$, then $\boxed{319/13}$ for all $8 \le k \le 20$ — **identical to
$B^{\mathrm{aug}}_k$** (the worst class, $123 \bmod 256$, is killed most cheaply
by the empty word, i.e. by L-9909's own $T^8(n) < n$ test, and no interleaved
word improves its threshold; and since $B^{\mathrm{int}}_k$ maximises the least
threshold over *all* first-killed classes, every killed class at $k \le 20$ has a
kill with $\theta \le 319/13$).

**(e) Rate data.** See the table in the Adversarial tests (script 3): at
$k = 8, 12, 16, 20, 24, 26$ the per-level rate difference
$\tfrac1k\log_2(|\text{L-9909}(k)|/|\mathrm{Int}(k)|)$ is
$0.0310,\ 0.0542,\ 0.0396,\ 0.0392,\ 0.0304,\ 0.0301$, and
$\log_2(|\mathrm{Aug}(k)|/|\mathrm{Int}(k)|)$ is
$0.170,\ 0.415,\ 0.445,\ 0.496,\ 0.494,\ 0.503$. Interpretation in L-9926.5.

### L-9926.4 (consequences: the 3-adic layers and the congruence structure of mu)

1. **(The universal layer — proved, no floor needed.)** Let
   $$K_3(D) := \bigl\{\, s \bmod 3^D : \exists\, w \text{ contracting},\
     m := \#\mathsf{D}(w) \le D,\ s + 1 \equiv t_w \bmod 3^{m} \,\bigr\}.$$
   By L-9926.1(5), **[H]** $\mu \bmod 3^D \notin K_3(D)$ for every $D$ — with no
   exceptional bound whatsoever. Exact computation ($D \le 7$):

   | $D$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
   |---|---|---|---|---|---|---|---|
   | $|K_3(D)|$ | 1 | 4 | 12 | 37 | 111 | 335 | 1013 |
   | allowed density | .66667 | .55556 | .55556 | .54321 | .54321 | .54047 | .53681 |
   | new classes beyond the lift | 1 | 1 | 0 | 1 | 0 | 2 | 8 |

   $K_3(1) = \{2\}$, $K_3(2) = \{2,4,5,8\}$; the first genuinely-deeper class is
   $n \equiv 10 \bmod 81$ (word $\mathsf{MDMDDD}$). Structurally, new classes at
   depth $m$ come only from **primitive** contracting words — $\mathsf{M}$-first
   (a leading $\mathsf{D}$ lands inside $u \equiv 0 \bmod 3$) with no contracting
   proper prefix — which is why depths 3 and 5 add nothing. Combining $D = 2$ with
   L-9919.6(1):
   $$\boxed{\ \mu \bmod 36 \in \{3, 7, 15, 19, 27\}\ }\quad
   \text{(density } 5/36 \approx 0.139\text{, vs } 1/6 \approx 0.167 \text{ from L-9919)}.$$

2. **(The joint pair sieve and the collapse question.)** Define
   $\mathrm{Joint}^{\mathrm{int}}(k, D)$ := pairs $(r \bmod 2^k, s \bmod 3^D)$ with
   $r \in \mathrm{Int}(k)$ and $s$ not excluded by any class-uniform or
   $n$-dependent kill of refinement depth $\le D$ at any $j \le k$. Computed
   exactly (all kill thresholds verified $\le -1$ per pair, so no discharge
   is needed within the tables):
   * **(a) Depth $\le 3$: class-independent.** For every computed $(k, D)$ with
     $D \le 3$ ($k \le 14$), the forbidden set of **every** $r \in \mathrm{Int}(k)$
     equals the universal set $K_3(D)$:
     $\mathrm{Joint}^{\mathrm{int}}(k,D) = \mathrm{Int}(k) \times M_3(D)$,
     $M_3(D) := \mathbb{Z}/3^D \setminus K_3(D)$. **PARTIAL: finite range only;
     the depth-1 case ("mod 3 stays one bit") is additionally structurally
     constrained by L-9926.2(7) but not proved.**
   * **(b) Depth 4: the collapse analogue FAILS — proved by verified example.**
     At $(k,D) = (8,4)/(10,4)/(12,4)$ the joint counts are $690/1980/6194$
     against product-form $704/2024/6336$: at $k = 12$, 142 of the 144 classes
     each forbid exactly one extra pair. Explicit verified instance: class
     $r = 27 \bmod 4096$, $j = 4$, word $\mathsf{MMDDDMDDDD}$, legality
     $u \equiv 61 \bmod 81$, threshold $-33/17$: it kills the pair
     $(27 \bmod 4096,\ 60 \bmod 81)$ — note $60 \equiv 0 \bmod 3$, a residue class
     untouched by every previous layer — while classes $2047, 4095 \bmod 4096$ do
     **not** forbid $60 \bmod 81$ (class-dependence), and $n$'s in the class with
     $u \not\equiv 61 \bmod 81$ fail the word's legality ($n$-dependence).
     **The interleaved family is genuinely two-dimensional mod $2^k 3^D$ from
     depth 4 on; no product-form collapse theorem exists for it.**

3. **[H] (mu tables and search-space reduction.)** For $\mu > B^{\mathrm{int}}_k$
   (discharged below): $\mu \bmod 2^k \in \mathrm{Int}(k)$ for $k \le 20$, e.g.
   $\mu \bmod 256$ lies in the 16-element list of L-9926.3(b), and $\mu$'s pair
   $(\mu \bmod 2^k, \mu \bmod 3^D)$ lies in $\mathrm{Joint}^{\mathrm{int}}(k,D)$:

   | $(k,D)$ | allowed pairs | modulus | density | L-9919's packaged density |
   |---|---|---|---|---|
   | $(8,1)$ | 32 | 768 | 0.04167 | 0.04688 |
   | $(8,2)$ | 80 | 2304 | 0.03472 | 0.04688 |
   | $(12,2)$ | 720 | 36864 | 0.01953 | 0.03125 |
   | $(12,4)$ | 6194 | 331776 | **0.01867** | 0.03125 |

   Against L-9909 alone at $k = 12$ (density $226/4096 = 0.05518$) the pair sieve
   at $(12,4)$ is a factor $\approx 2.96$ reduction; against L-9919's packaged
   joint sieve, $\approx 1.67$. At $k = 20$: $\mu$ lies in $2 \cdot 15870 = 31740$
   classes mod $3\cdot 2^{20}$, density $\approx 0.0101$, vs L-9919's $44768$
   (density $\approx 0.0142$).

4. **(Exceptional bounds and the floor — tier-honest discharge.)** Every bound in
   this file is $\le B^{\mathrm{int}}_k = 319/13 < 25$; the universal layer needs
   none; the pair tables' per-pair least thresholds are all $\le -1$ (computed).
   Discharge of $\mu > 25$: X-9901 ($\mu > 10^6$, finite verification inside the
   PROVED L-9909) suffices. The stronger floor X-9903 gives $\mu > 10^{12}$ and is
   cited per L-9913's precedent: EMPIRICAL, adversarially reviewed (fable-02-v19);
   $n \le 10^{10}$ is independently double-implemented, $(10^{10}, 10^{12}]$ is a
   reviewed single implementation. Nothing here needs it; it is quoted only so
   that downstream users know the strongest available floor. The interleaving
   does **not** improve any exceptional bound ($B^{\mathrm{int}} = B^{\mathrm{aug}}$
   on the computed range) — as with L-9919, a bookkeeping fact of no consequence
   given the floor.

### L-9926.5 (honest verdict: bounded factor, not a rate improvement — with the one caveat)

**The central empirical question resolves, on the computed range, AGAINST a rate
improvement.** The evidence (script 3, exact counts to $k = 26$):

* $\log_2(|\text{L-9909}|/|\mathrm{Int}|)$ grows from $0.25$ ($k=8$) to $\approx 0.78$
  ($k = 26$) — but its increments per 2 levels collapse from $0.23$ (at $k=8\!\to\!10$)
  to the **same oscillating pattern as Aug's**: over $k = 16 \to 26$ the Int and
  Aug increment sequences are $0.071, 0.080, 0.053, -0.108, 0.054$ vs
  $0.055, 0.044, 0.051, -0.104, 0.045$ — nearly identical, i.e. the interleaved
  sieve is by then removing a **constant extra factor** on top of Aug, not a
  growing one.
* Directly: $\log_2(|\mathrm{Aug}|/|\mathrm{Int}|)$ saturates at
  $\approx 0.50$ bits ($0.496, 0.491, 0.499, 0.505, 0.494, 0.495, 0.503$ for
  $k = 20..26$). The whole interleaved gain over L-9909 at the top of the range
  is a factor $\approx 1.7$ ($\approx 1.4$ beyond Aug), against L-9919's
  $\approx 1.2$.
* The per-level rate difference $\tfrac1k\log_2$ decays: $0.054$ ($k{=}12$)
  $\to 0.030$ ($k{=}26$), exactly the signature that made L-9919.5(c) call Aug a
  bounded factor.

**Caveat, stated plainly:** over the last 10 computed levels
$\log_2(\mathrm{Aug}/\mathrm{Int})$ still drifts up by $\approx +0.006$ bits/level.
On a window this short (and oscillating with the continued-fraction structure of
$\log_2 3$, as in L-9919), that residue cannot be distinguished from either a
slowly-saturating constant or a genuinely positive but tiny rate gain. The honest
summary: **consistent with a bounded factor $\approx 1.4\times$ over Aug; not
proof of one; no evidence of a material rate improvement.**

**Why the gain saturates (heuristic, not a theorem — and why no collapse theorem
caps it).** For the pure-descent family, L-9919.4(5) *proved* the 3-adic collapse;
here the analogous cap provably does NOT exist (L-9926.4(2b)). The saturation has
a different mechanism: a class-uniform kill at index $j$ needs, by L-9926.2(3)–(4),
$a$ $\mathsf{D}$'s and $b$ $\mathsf{M}$'s with
$a(\log_2 3 - 1) - b \ \gtrsim\ s_j := a_j\log_2 3 - j \ (\ge 0$ on survivors$)$,
plus a chain of $a$ independent-looking $3$-divisibilities of $Q$. Surviving
parity walks keep $s_j \asymp \sqrt{j}$ (the conditioned-walk height of
L-9919.7), so eligible words need $\asymp \sqrt{j}$ $\mathsf{D}$'s, and the
$3^{-a}$ cost of the divisibility chain balances the $2^{\text{choices}}$ word
count to a $k$-independent extra kill probability per level — a constant factor,
exactly as observed. Turning that into a theorem (or refuting it) is the
Suggested next attack; a proof would make the bounded-factor verdict a theorem
for the whole interleaved family.

**What a genuine rate improvement would need:** kills whose word length grows
linearly in $j$ against survivor conditioning — equivalently, positive density of
indices $j$ at which the survivor walk admits a contracting-tail merge. Nothing
in the computed range suggests it.

---

## Definitions

* **Moves** $\mathsf{D}(z) = (2z-1)/3$ (iff $z \equiv 2 \bmod 3$), $\mathsf{M}(z) = 2z$;
  **word** $w \in \{\mathsf{D},\mathsf{M}\}^*$, applied left to right;
  $L = |w|$, $a = \#\mathsf{D}(w)$, $b = \#\mathsf{M}(w)$.
* **Word constant** $c_w$: L-9926.1(1). **Legality class** $t_w \bmod 3^a$:
  L-9926.1(2). **Contracting word:** $2^{|w|} < 3^{\#\mathsf{D}(w)}$.
* **Sieve state** $(P_i, Q_i)$ at index $j$: L-9926.2(1). **Type (U)/(V)/(N)**:
  L-9926.2(2). **Class-uniform kill**, threshold $\theta_{j,w}$: L-9926.2(3).
* **$\mathrm{Int}(k)$**: L-9926.2(5). **$B^{\mathrm{int}}_k$**: L-9926.2(6).
* **$K_3(D)$, $M_3(D)$** (universal 3-adic layer): L-9926.4(1).
  **$\mathrm{Joint}^{\mathrm{int}}(k,D)$**: L-9926.4(2).
* $X$, $\mu$: Standing hypothesis (identical to L-9909/L-9911/L-9919).

---

## Motivation

L-9919 proved that the pure-descent backward family collapses 3-adically (one bit)
and measured a bounded-factor 2-adic gain; its L-9919.8 opened the one direction
with visible headroom — interleaving the doubling move — but left three gaps:
no exact affine calculus for mixed words (the shifted coordinate is not
multiplicative for $\mathsf{M}$), a word-length cap that made the computed
survivor counts upper approximations, and no collapse analysis. This file closes
all three: the calculus is exact (L-9926.1), the cap is removed by a proved
length bound so $\mathrm{Int}(k)$ is exact (L-9926.2(4), L-9926.3), and the
collapse question is answered — negatively, by a verified mixed kill — while the
class-independent part of the 3-adic direction is isolated as a clean new family
of unconditional congruences for $\mu$ ($\mu \not\equiv 4 \bmod 9$ etc.) that any
search program can use at zero cost. The honest verdict (bounded factor
$\approx 1.4\times$ over Aug on the computed range) tells later agents what this
direction is worth and where its remaining theoretical question lies (prove or
refute the saturation).

---

## Proof or construction

### Proof of L-9926.1

**(1)** Induction on $|w|$. Base: $w = \varepsilon$, $z + 1 = (2^0(z+1) - 0)/3^0$,
$c_\varepsilon = 0$. Step, appending $\mathsf{D}$: by L-9919.1/L-9919.2(1),
$\mathsf{D}(y) + 1 = \tfrac{2}{3}(y+1)$ when defined, so
$w\mathsf{D}(z) + 1 = \tfrac23 \cdot \frac{2^{L}(z+1) - c_w}{3^{a}}
= \frac{2^{L+1}(z+1) - 2c_w}{3^{a+1}}$: the constant doubles, $a$ increments.
Step, appending $\mathsf{M}$: $\mathsf{M}(y) + 1 = 2y + 1 = 2(y+1) - 1$, so
$w\mathsf{M}(z) + 1 = 2\cdot\frac{2^{L}(z+1) - c_w}{3^{a}} - 1
= \frac{2^{L+1}(z+1) - (2c_w + 3^{a})}{3^{a}}$: the constant becomes
$2c_w + 3^{a}$, $a$ unchanged. This is exactly the stated recursion. The closed
form follows by unrolling: the $\mathsf{M}$ at position $i$ injects $3^{d_i}$
(where $d_i$ counts prior $\mathsf{D}$'s) and is then doubled once per each of
the $L - i$ later moves. $c_w \ge 0$ is clear; $c_w = 0$ iff there is no
$\mathsf{M}$ (all terms are positive); the all-$\mathsf{D}$ case is
$w(z) + 1 = 2^d(z+1)/3^d$ = L-9919.2(1). The unshifted form is algebra:
$w(z) = (2^L(z+1) - c_w)/3^a - 1 = (2^L z - (c_w - 2^L + 3^a))/3^a$.

**(2)** Induction on $|w|$, maintaining: $\mathrm{Leg}(w) := \{u \in \mathbb{Z} :$
all $\mathsf{D}$-congruences of $w$ hold starting from $z = u - 1\}$ is a single
class $t_w \bmod 3^{a}$. Base: $\mathrm{Leg}(\varepsilon) = \mathbb{Z}$, the class
$0 \bmod 1$. Appending $\mathsf{M}$ changes no congruence. Appending
$\mathsf{D}$: on $u \equiv t_w \bmod 3^a$, the current value satisfies
$u_L := w(z) + 1 = (2^{L}u - c_w)/3^{a} \in \mathbb{Z}$, and writing
$u = t_w + 3^{a}s$: $u_L = \frac{2^L t_w - c_w}{3^a} + 2^{L} s$. As $s$ runs over
$\mathbb{Z}$, $2^{L}s \bmod 3$ hits every residue (since $\gcd(2,3) = 1$), so
$\{s : 3 \mid u_L\}$ is exactly one class mod 3, i.e.
$\mathrm{Leg}(w\mathsf{D})$ is exactly one nonempty class mod $3^{a+1}$, refining
$t_w$. Restricting to $z \in \mathbb{Z}^+$ (i.e. $u \ge 2$) leaves the infinite
trace stated. (The refinement recursion in this argument is the algorithm the
scripts implement.)

**(3)** From (1): $w(z) < z \iff \frac{2^{L}(z+1) - c_w}{3^{a}} < z + 1
\iff (z+1)(2^{L} - 3^{a}) < c_w$ (multiply by $3^a > 0$; every step reversible).
If $2^L < 3^a$: $z + 1 \ge 2 > 0$ and $2^L - 3^a \le -1$ make the left side
negative, and $c_w \ge 0$, so the inequality holds for every $z$.
If $2^L > 3^a$, divide: $z + 1 < c_w/(2^L - 3^a)$, a finite range. $2^L = 3^a$
forces $L = a = 0$ by unique factorisation. Positions enter only via $c_w$.

**(4)** Positivity: induction along the word. If $z_i \ge 1$ and the next move is
$\mathsf{M}$: $z_{i+1} = 2z_i \ge 2$. If it is a legal $\mathsf{D}$: $z_i \equiv 2
\bmod 3$ and $z_i \ge 1$ force $z_i \ge 2$, so $z_{i+1} = (2z_i - 1)/3 \ge
(4-1)/3 = 1$. So all $z_i \in \mathbb{Z}^+$ with no further condition. (Contrast:
L-9919.8(1) imposed per-node thresholds $u \ge (2^{j+1} - Q)/P$; by this argument
those are implied by legality and can be dropped — they only ever weakened the
recorded thresholds, e.g. the witness class $63 \bmod 256$ has true threshold
$Q_L/(2^j - P_L) - 1 = 0/64 - 1 = -1$, not $5/3$. Soundness of L-9919.8 is
unaffected.) Inversion: $T(\mathsf{M}(z)) = z$ and $T(\mathsf{D}(z)) = z$
(L-9919.1(2)), so $T^{L}(z_L) = z_0$ by induction. Closure: L-9911 U2 says
$x \in X \iff T(x) \in X$; applying it $L$ times along the chain gives
$w(z) \in X \iff z \in X$.

**(5)** Let $w$ be contracting and $z \in \mathrm{Dom}(w)$. By (3), $w(z) < z$;
by (4), $w(z) \in \mathbb{Z}^+$ and $w(z) \in X$ if $z \in X$. **[H]** If
$\mu \in \mathrm{Dom}(w)$ then $w(\mu) \in X$ and $w(\mu) < \mu$, contradicting
minimality. So $\mu \notin \mathrm{Dom}(w)$, i.e. $\mu + 1 \not\equiv t_w \bmod
3^{\#\mathsf{D}(w)}$ — one excluded class mod a pure power of 3, valid for every
$\mu \ge 1$ (no bound). Instances: $w = \mathsf{D}$: $\mathrm{Dom} = \{z \equiv 2
\bmod 3\}$, $2^1 < 3^1$. $w = \mathsf{MDD}$: $2^3 = 8 < 9 = 3^2$; legality:
$\mathsf{D}$ at $2z$ needs $2z \equiv 2$, i.e. $z \equiv 1 \bmod 3$; then
$\mathsf{D}$ at $(4z-1)/3$ refines to $z \equiv 4 \bmod 9$; value:
$w(z) = (8z - 5)/9 < z$; inversion: $T^3((8n-5)/9) = n$. $w = \mathsf{MDMDDD}$:
$2^6 = 64 < 81 = 3^4$, legality class $u \equiv 11 \bmod 81$, i.e.
$z \equiv 10 \bmod 81$. (All three verified exhaustively in the scripts.)
$\square$

### Proof of L-9926.2

**(1)** By L-9919.4(1) (quoted, PROVED), $2^j(T^j(n) + 1) = 3^{a_j}u + \delta_j$
for every $n$ in the class. Apply L-9926.1(1) to the prefix $p$ at
$z_0 = T^j(n)$: $z_i + 1 = (2^{i}(z_0+1) - c_p)/3^{e}$; multiply by $2^j 3^e$ and
substitute. For $e \le a_j$, divide by $3^e$: $P_i = 2^i 3^{a_j - e}$ is an
integer, and $Q_i = (2^i \delta_j - 2^j c_p)/3^e$ is an integer whenever the
prefix is type-(U) legal (each division by 3 happened only when $3 \mid Q$; see
(2)). The recursions restate L-9926.1(1)'s: $\mathsf{M}$ doubles the numerator
and subtracts $2^j\cdot 3^{e}$ from $2^j c_p$-side, i.e. $(2P, 2Q - 2^j)$ after
dividing by $3^e$; $\mathsf{D}$ doubles and moves one factor 3 down:
$(2P/3, 2Q/3)$. These are exactly L-9919.8(1)'s rules, whose soundness the
reviewer verified; here they are derived rather than posited.

**(2)** Legality of the next $\mathsf{D}$ after prefix $p$ ($i$ moves, $e$
$\mathsf{D}$'s) is $3 \mid z_i + 1$, i.e. (multiplying (1) by 1 and using
$\gcd(2^j, 3) = 1$): $3^{e+1} \mid 2^{i}(3^{a_j}u + \delta_j) - 2^j c_p$. The
$u$-coefficient $2^i 3^{a_j}$ has $\nu_3 = a_j$. If $e + 1 \le a_j$: the
$u$-term vanishes mod $3^{e+1}$, leaving the $n$-free condition
$3^{e+1} \mid 2^i\delta_j - 2^j c_p$ — satisfied (type U continues, and then
$3 \mid P$ and $3 \mid Q$ in (1)'s coordinates) or not (type V: no $n$ works).
If $e + 1 > a_j$: on the current legality class of $u$ (inductively a single
class mod $3^{e - a_j}$, nonempty), write $u = \tau + 3^{e - a_j} t$; the
condition becomes a linear congruence in $t$ with $t$-coefficient of $3$-adic
valuation exactly $e$ (namely $2^i 3^{a_j} \cdot 3^{e-a_j}$), while the constant
part is divisible by $3^{e}$ because $z_i + 1 \in \mathbb{Z}$ on the class; so
exactly one class of $t$ mod 3 solves it: the legality class refines to a single
nonempty class mod $3^{e+1-a_j}$. Induction over the word gives the trichotomy
with final modulus $3^{a - a_j}$ in case (N). Necessity of $3 \mid P \wedge 3
\mid Q$ for class-uniformity: within $\{n \equiv r \bmod 2^k,\ n > B\}$, $u$
takes every residue mod 3 (CRT), and $3 \mid Pu + Q$ for all three residues
forces $P \equiv Q \equiv 0 \bmod 3$. The CRT statement for the legality set in
$n$ is immediate (independent moduli $2^j$ and $3^m$).

**(3)** Type (U), terminal $(P_L, Q_L)$: $w(T^j(n)) < n \iff
(P_L u + Q_L)/2^j < u \iff u(2^j - P_L) > Q_L$. If $P_L < 2^j$: $\iff u >
Q_L/(2^j - P_L) \iff n > \theta_{j,w}$; every step multiplies by a positive
quantity, so this is an equivalence — the kill is exact, not one-sided. If
$P_L = 2^j$: unique factorisation on $P_L = 2^{L}3^{a_j - a} = 2^j$ forces
$a = a_j$, $L = j$; then $w(T^j(n)) = n + Q_L/2^j$ for every $n$ in the class
(and $2^j \mid Q_L$ since both are integers), a constant shift; kill iff
$Q_L < 0$. If $P_L > 2^j$: $u(2^j - P_L) \to -\infty$, no kill above a bound.
Type (N): from (1) at the terminal, $w(T^j(n)) < n \iff
u\,(2^j 3^{a} - 2^{L} 3^{a_j}) > 2^{L}\delta_j - 2^{j} c_w$ — cleared of
denominators; $\Delta := 2^j 3^a - 2^L 3^{a_j} = 0$ would force $a = a_j$ by
unique factorisation, contradicting $m \ge 1$. $\mathsf{D}$-only specialisation:
$c_w = 0$, $P_d = 2^d 3^{a_j - d}$, $Q_d = 2^d\delta_j/3^d$; the legality chain
is $3^d \mid \delta_j$ with $d \le a_j$, i.e. $d \le m_j$ — branch (U) of
L-9919.4(2) — and the kill condition $u(2^j - 2^d 3^{a_j-d}) > 2^d\delta_j/3^d$
multiplied by $3^d$ is $u(2^j 3^d - 2^d 3^{a_j}) > 2^d \delta_j$, L-9919.4(3)'s
test with the identical threshold $\theta_{j,d}$.

**(4)** In a class-uniform word, every $\mathsf{D}$ is applied with $3 \mid P$,
i.e. $e < a_j$ at that moment; hence $a \le a_j$ and $P_i = 2^i 3^{a_j - e_i}
\ge 2^i$ for every prefix. A kill needs $P_L \le 2^j$ (cases 1–2 of (3)), so
$2^{L} \le P_L \le 2^j$, i.e. $L \le j$; and $P_L < 2^j$ with $a \le a_j$ gives
$2^L < 2^j 3^{a - a_j} \le 2^j$, so $L < j$ strictly except in the boundary case.
Since kills of prefixes are kills by shorter words, the full search space at
index $j$ is the finite tree of words of length $\le j$ with $\#\mathsf{D} \le
a_j$; the feasibility prune used by the scripts (discard a node when even
playing all remaining permissible $\mathsf{D}$'s leaves $P > 2^j$) discards only
nodes from which no kill is reachable, because every move multiplies $P$ by $2$
or $2/3$ and the bound is monotone. For type (N) at depth $m$: $\Delta > 0$
requires $2^{L - j} < 3^{m}$, i.e. $L < j + m\log_2 3$.

**(5)** $\mathrm{Int}(k) \subseteq \mathrm{Aug}(k)$: if $r \notin \mathrm{Aug}(k)$,
L-9919.4(4) gives a branch-(U) descent kill $(j, d)$, whose word $\mathsf{D}^d$
is a class-uniform kill by the specialisation in (3); so $r \notin
\mathrm{Int}(k)$. $\mathrm{Aug}(k) \subseteq$ L-9909$(k)$ is L-9919.4(4).
Prefix-closure: the data $(a_j, \delta_j)$ of a kill at $(j, w)$ depend only on
$r \bmod 2^j$ (L-9902/L-9903), so a class dies at the least level carrying a
kill, exactly as in L-9919.4(6).

**(6)** Identical bookkeeping to L-9919.4(6), which the reviewer re-derived: if
$r \bmod 2^k \notin \mathrm{Int}(k)$, let $k'$ be the least level at which the
prefix carries a class-uniform kill (exists; property of the prefix); all proper
prefixes are alive, so the prefix is one of the first-kill classes over which
$B^{\mathrm{int}}_k$ maximises; pick its least-threshold kill $(j = k', w,
\theta)$, $\theta \le B^{\mathrm{int}}_k$. For $n > B^{\mathrm{int}}_k$ in the
class: legality holds for every $n$ (type U), the chain is in $\mathbb{Z}^+$
(L-9926.1(4)), $z := w(T^{k'}(n)) < n$ by (3), and $T^{|w|}(z) = T^{k'}(n)$ by
L-9926.1(4). **[H]**: $T^{k'}(\mu) \in X$ (L-9911.1), so $z \in X$ by L-9926.1(4)
closure, and $z < \mu$ contradicts minimality; hence $\mu \bmod 2^k \in
\mathrm{Int}(k)$ whenever $\mu > B^{\mathrm{int}}_k$. $\square$

**(7)** Let $(j, w)$ be an $n$-dependent kill on a class with no class-uniform
kill at any index $\le j$. The first $n$-dependent $\mathsf{D}$ occurs at
$e = a_j$ (any $\mathsf{D}$ at $e < a_j$ is (U)-or-(V) by (2), and (V) kills
nothing). Split $w = h t$ at that point: $h$ is class-uniform with $a_j$
$\mathsf{D}$'s, so $P_h = 2^{|h|} 3^{a_j - a_j} = 2^{|h|}$. And $|h| \ge j$ must hold: else
$P_h = 2^{|h|} < 2^j$ and $h$ itself is a class-uniform kill (case 1 of (3)) —
contradiction. Then $z_h + 1 = (2^{|h|} u + Q_h)/2^j$ with $z_h \in \mathbb{Z}$
and $2^j \mid 2^{|h|}u$ (as $|h| \ge j$) forces $2^j \mid Q_h$. The kill's value
condition ($\Delta > 0$, (4)) reads
$2^{|h| + |t| - j} < 3^{m}$, so $2^{|t|} \le 2^{|h| - j + |t|} < 3^{m}$: the
tail is contracting. For $m = 1$: $|h| - j + |t| < \log_2 3 < 2$ and $|t| \ge 1$
force $|h| = j$, $|t| = 1$, so $t$ is a single $\mathsf{D}$ and $z_h = n +
Q_h/2^j$ with $T^j(z_h) = T^j(n)$ (inversion), same odd-step count $a_j$ (the
head has $a_j$ $\mathsf{D}$'s). If $Q_h < 0$, $h$ would be an equality-case
class-uniform kill (case 2 of (3)) — contradiction; so $Q_h \ge 0$. The
$\mathsf{D}$'s legality is $3 \mid z_h + 1$; since $z_h + 1 = u + Q_h/2^j$,
this is $u \equiv -Q_h/2^j \bmod 3$, which is the class $u \equiv 0$ iff
$3 \mid Q_h/2^j$ iff $3 \mid Q_h$ iff $z_h \equiv n \bmod 3$ (their difference
is $Q_h/2^j$). $\square$

### Proof / computation notes for L-9926.3, L-9926.4, L-9926.5

All tables are exact finite computations over the stated finite ranges (scripts
and byte-exact outputs in Adversarial tests). Their logical status: (i) the
counts and lists are exact evaluations of the *definitions* in L-9926.2(5) —
legitimate finite theorems — and by L-9926.2(4) the word search is complete, so
the computed $\mathrm{Int}(k)$ **is** the defined $\mathrm{Int}(k)$, not an
approximation; (ii) every kill used is a finite certificate that the scripts
re-verify by direct iteration (soundness), and the per-$n$ agreement test
(script 4) checks the whole calculus, thresholds included, against direct
integer iteration with zero slack; (iii) the universal-layer memberships in
L-9926.4(1) are individually proved by L-9926.1(5) once the word and its
legality class are exhibited — the computation only enumerates them; (iv) the
depth-$\le 3$ class-independence and everything in L-9926.5 are finite-range
observations, labelled PARTIAL/heuristic, and never used as hypotheses elsewhere
in this file. Nothing is extrapolated beyond its computed range.

---

## Dependency audit

| Used | Where | Exact role |
|---|---|---|
| D-9901/2/5/6/9/10 | throughout | definitions of $C, T$, orbits, parity data, $X$, $\sigma$ |
| L-9902.1(c), .2, .3(iii) (PROVED) | L-9926.2, tree computations | word data are functions of $n \bmod 2^k$; class tree with two lifts |
| L-9903.1/.2 (PROVED) | via L-9919.4(1) | the affine iteration formula behind the sieve state |
| L-9909.2(B)(F) (PROVED) | L-9926.1(4) via L-9911 U2 | closure of $X$ |
| L-9909.2(M) (PROVED) | L-9926.4(1) ($\mu \bmod 36$) | $\mu \equiv 3 \bmod 4$ |
| L-9909.3/.4 (PROVED) | L-9926.2(5), script gates | the $d=0$ sieve reproduced as the empty word; published tables as cross-checks |
| X-9901 (finite verification in L-9909) | L-9926.4(4) | $\mu > 10^6$, discharging $\mu > 319/13$ |
| L-9911 U2, U3, L-9911.1 (PROVED) | L-9926.1(4), L-9926.2(6) | two-sided closure; complete preimages; orbit floor |
| L-9919.1, .2 (PROVED) | L-9926.1(1),(4) | $\mathsf{D}$'s one-step facts and $u$-coordinate action |
| L-9919.4(1)–(4) (PROVED) | L-9926.2(1),(3),(5) | shifted formula; $\delta$-recursion; Aug kills as the $\mathsf{D}$-only case; $\mathrm{Aug} \subseteq$ L-9909 |
| L-9919.4(6) (PROVED) | L-9926.2(6) | the first-kill/least-threshold bookkeeping pattern |
| L-9919.8(1)–(2) (PARTIAL, soundness reviewer-verified) | L-9926.2(1); gate in script 2 | the $(P,Q)$ rules (re-derived here); the capped algorithm reproduced as a gate |
| X-9903 (EMPIRICAL, reviewed) | L-9926.4(4) | the $10^{12}$ floor, quoted tier-honestly; not needed |

**No circularity.** L-9926 uses L-9902/03/09/11/19 and is used by none of them.
Conditional inputs (L-9911.1, L-9909.2(M)) are themselves conditional on (H),
this file's standing hypothesis; no unconditional statement here depends on any
conditional one. L-9919.8's PARTIAL strength table is *not* an input — it is
reproduced as a gate and then superseded; only its (1)–(2), whose soundness the
reviewer verified and which are re-proved here from L-9926.1, are touched at all.

---

## Gap audit

* **Hidden finiteness assumptions.** L-9926.1 and L-9926.2 are proved for all
  words, classes, $j$, $k$ with no appeal to computation. The finiteness that
  makes $\mathrm{Int}(k)$ computable is itself proved (L-9926.2(4)), not assumed.
  Tables are finite computations labelled as such.
* **Unjustified induction.** Three inductions (affine form; legality refinement;
  positivity along the chain) are written with base and step; the legality
  induction's nonemptiness uses only $\gcd(2,3) = 1$.
* **Boundary cases.** The empty word (= L-9909's kill; included everywhere);
  $c_w = 0$ (all-$\mathsf{D}$; reduces to L-9919.2); $P_L = 2^j$ (equality case:
  handled in the trichotomy, needed for completeness of the length bound, never
  fires as a min-threshold kill on the computed range); $\delta_j = 0$ (all-ones
  prefixes; $Q$ starts at 0 and $\mathsf{D}$-legality $3 \mid 0$ holds); $j = 0$
  (no class-uniform kill exists there: $P$ can only reach $2^{\mathrm{cnt}} \ge 1
  = 2^0$ with equality only for the empty word, $Q_\varepsilon = 0 \not< 0$);
  $z = 1, 2$ in the move definitions; $r = 0$ (representative $2^k$).
* **Empirical vs universal.** Universal statements are exactly those in the
  Proof section. The computed $\mathrm{Int}(k)$ tables are finite theorems about
  finite sets (complete search + verified certificates). The depth-$\le 3$
  class-independence (L-9926.4(2a)) and the saturation reading (L-9926.5) are
  finite-range and labelled so. The heuristic mechanism in L-9926.5 is labelled
  heuristic.
* **Interchange of limits.** None.
* **Circular dependence.** Audited above.
* **Nonuniform estimates.** Every kill has an explicit rational threshold; the
  sieve theorem's quantifier order is "for all $n$ above a bound depending only
  on $k$"; per-pair thresholds in the joint tables are computed and all $\le -1$.
* **Assumptions equivalent to the conjecture.** None; (H) is the negation, used
  only to define $\mu$, and every $\mu$-statement is tagged.
* **Incorrectly assumed independence.** The product form at depth $\le 3$ is
  *measured*, not assumed — and the file's own PART B exhibits its failure at
  depth 4, so no independence is asserted anywhere.
* **Unproved properties of an infinite rewrite sequence.** All words are finite;
  the infinite family of words is controlled by the proved length bound.
* **Finite computation extrapolated to infinite behaviour.** Explicitly refused
  in L-9926.5; the verdict is stated as a description of $k \le 26$ with the
  residual drift disclosed.
* **Circularly defined counterexample.** No counterexample is proposed.
* **Symbolic object vs actual positive integer.** L-9926.1(4) is exactly this
  check (positivity never binds — proved, and stress-tested on 1.4 million
  starts); every certificate verification re-checks membership in $\mathbb{Z}^+$
  along real chains.
* **Known soft spots (declared).** (i) The feasibility prune in the search
  (monotonicity argument in the proof of L-9926.2(4)) — a reviewer should
  re-derive it; it is also cross-checked by the gate (independent algorithm,
  L-9919.8's, reviewer-verified) agreeing wherever the cap is not binding, and
  by the two-sided per-$n$ test. (ii) The residue-tracking in the class tree
  (parity of $T^j$ of the representative) — cross-checked against the direct
  per-residue enumeration at $k \le 12$ inside script 5's `int_classes` and by
  the published-list gates. (iii) $B^{\mathrm{int}}_k$ bookkeeping mirrors
  L-9919.4(6); the same reviewer attention is invited.

---

## Adversarial tests

Finite verification, **not** proof. All arithmetic exact (`int`/`Fraction`);
floats only in display columns. CPython 3, Linux. Each block is followed by its
**real captured output**; all five blocks were re-extracted from this file,
re-run, and compared byte-for-byte (see the reproducibility note).

### Script 1 — `l9926_words.py` (L-9926.1: the word calculus)

```python
#!/usr/bin/env python3
# l9926_words.py -- adversarial finite verification of the {D,M}-word calculus
# (L-9926.1): affine form, word constant c_w (recursion = closed form), legality
# as a single congruence class mod 3^{#D}, positivity-never-binds, inversion
# T^{|w|}(w(z)) = z, and the exact value criterion.  Also re-verifies the
# L-9919.8 witness (class 63 mod 256, word DMDDDD) byte for byte.
# Agent: fable-02-p20.  Python 3 stdlib only; exact integer arithmetic.
# FINITE VERIFICATION, NOT PROOF.
import random

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def apply_word_direct(w, z):
    """apply moves left to right; return list of values or None if some D illegal.
       D(z) = (2z-1)/3 (needs z = 2 mod 3), M(z) = 2z."""
    vals = [z]
    for mv in w:
        if mv == "D":
            if z % 3 != 2: return None
            z = (2 * z - 1) // 3
        else:
            z = 2 * z
        vals.append(z)
    return vals

def word_constants(w):
    """(L, a, c_w) by the recursion c_eps = 0, c_{wD} = 2c, c_{wM} = 2c + 3^{#D(w)}."""
    c = 0; a = 0
    for mv in w:
        if mv == "D": c = 2 * c; a += 1
        else: c = 2 * c + 3 ** a
    return len(w), a, c

def word_constant_closed(w):
    """closed form c_w = sum over M-positions i (1-based) of 2^{L-i} 3^{#D before i}."""
    L = len(w); c = 0; d = 0
    for i, mv in enumerate(w, start=1):
        if mv == "M": c += 2 ** (L - i) * 3 ** d
        else: d += 1
    return c

def legality_class(w):
    """the unique u-class t_w mod 3^{#D} on which w is fully legal (u = z+1),
       built by the refinement in the proof of L-9926.1(2)."""
    t, mod = 0, 1          # class t mod mod, mod = 3^{#D so far}
    L = 0; a = 0; c = 0
    for mv in w:
        if mv == "M":
            c = 2 * c + 3 ** a; L += 1; continue
        # need 3 | u_cur = (2^L u - c)/3^a  on  u = t mod 3^a; u = t + 3^a s
        base = (2 ** L * t - c) // 3 ** a          # integer by invariant
        # u_cur = base + 2^L s ; choose s mod 3 with 3 | base + 2^L s
        s0 = (-base * pow(2 ** L, -1, 3)) % 3
        t = t + 3 ** a * s0; mod = 3 ** (a + 1)
        a += 1; c = 2 * c; L += 1
    return t % mod, mod

random.seed(9926)
NW = 4000
bad_affine = bad_cc = bad_leg = bad_pos = bad_inv = bad_val = 0
tested_words = 0; tested_starts = 0
for trial in range(NW):
    L = random.randint(1, 14)
    w = "".join(random.choice("DM") for _ in range(L))
    L_, a, c = word_constants(w)
    assert L_ == L
    if c != word_constant_closed(w): bad_cc += 1
    t, mod = legality_class(w)             # u-class mod 3^a
    assert mod == 3 ** a
    tested_words += 1
    # scan starts: all u-residues mod 3^a via lifts (bounded), plus random big lifts
    if a <= 6:
        residues = range(mod)
    else:
        residues = [random.randrange(mod) for _ in range(30)] + [t]
    for res in residues:
        for lift in (0, 1, 7):
            u0 = res + mod * lift
            z0 = u0 - 1
            if z0 < 1: continue
            tested_starts += 1
            vals = apply_word_direct(w, z0)
            legal = vals is not None
            if legal != (res == t): bad_leg += 1
            if not legal: continue
            # affine form at every prefix
            cc = 0; aa = 0
            for i, mv in enumerate(w, start=1):
                if mv == "D": cc = 2 * cc; aa += 1
                else: cc = 2 * cc + 3 ** (aa)
                num = 2 ** i * (z0 + 1) - cc
                if num % 3 ** aa != 0 or num // 3 ** aa != vals[i] + 1: bad_affine += 1
                if vals[i] < 1: bad_pos += 1
            # inversion
            back = vals[-1]
            for _ in range(L): back = T(back)
            if back != z0: bad_inv += 1
            # value criterion: w(z) < z  <=>  (z+1)(2^L - 3^a) < c_w
            if (vals[-1] < z0) != ((z0 + 1) * (2 ** L - 3 ** a) < c): bad_val += 1
print("W1 random words: %d words, %d starts: closed-form %d, legality-class %d,"
      % (tested_words, tested_starts, bad_cc, bad_leg))
print("   affine-prefix %d, positivity %d, inversion %d, value-criterion %d failures"
      % (bad_affine, bad_pos, bad_inv, bad_val))

# W2: the two shifted-coordinate bookkeepings agree: w(z) = (2^L z - c'_w)/3^a
#     with c'_w = c_w - 2^L + 3^a  (M is NOT multiplicative in u: 2u-1, not 2u).
bad = 0
for trial in range(500):
    L = random.randint(1, 10)
    w = "".join(random.choice("DM") for _ in range(L))
    L_, a, c = word_constants(w)
    t, mod = legality_class(w)
    z0 = (t - 1) % mod + mod * random.randint(1, 50)
    if z0 < 1: z0 += mod
    vals = apply_word_direct(w, z0)
    cp = c - 2 ** L + 3 ** a
    if vals is None or (2 ** L * z0 - cp) % 3 ** a != 0 \
       or (2 ** L * z0 - cp) // 3 ** a != vals[-1]: bad += 1
print("W2 z-coordinate constant c'_w = c_w - 2^L + 3^a: %d failures" % bad)

# W3: contracting words (2^L < 3^a) decrease at EVERY legal start (universal kills)
bad = 0; cnt = 0
for trial in range(2000):
    a = random.randint(1, 8)
    maxb = 0
    while 2 ** (a + maxb + 1) < 3 ** a: maxb += 1
    b = random.randint(0, maxb)
    if 2 ** (a + b) >= 3 ** a: continue
    w = list("D" * a + "M" * b); random.shuffle(w); w = "".join(w)
    t, mod = legality_class(w)
    for lift in (0, 1, 5):
        z0 = (t - 1) % mod + mod * lift
        if z0 < 1: continue
        vals = apply_word_direct(w, z0)
        cnt += 1
        if vals is None or vals[-1] >= z0: bad += 1
print("W3 contracting words (2^(a+b) < 3^a): %d starts, %d failures (all must drop)" % (cnt, bad))

# W4: the mod-9 universal kill: word MDD, every n = 4 mod 9 has (8n-5)/9 < n with
#     T^3((8n-5)/9) = n; and NO n != 4 mod 9 admits the word.
bad = 0
for n in range(1, 200000):
    ok = apply_word_direct("MDD", n) is not None
    if ok != (n % 9 == 4): bad += 1
    if ok:
        z = (8 * n - 5) // 9
        if 9 * z != 8 * n - 5 or not (1 <= z < n): bad += 1
        y = z
        for _ in range(3): y = T(y)
        if y != n: bad += 1
print("W4 universal kill MDD on n = 4 mod 9, n < 200000: %d failures" % bad)

# W5: L-9919.8 witness re-verified: class 63 mod 256, j = 8, word DMDDDD.
L_, a, c = word_constants("DMDDDD")
print("W5 witness word DMDDDD: L=%d #D=%d c_w=%d (expect 6,5,48)" % (L_, a, c))
for n in (63, 319, 575, 24895, 63 + 256 * 12345):
    y = n
    for _ in range(8): y = T(y)
    vals = apply_word_direct("DMDDDD", y)
    z = vals[-1]
    fwd = z
    for _ in range(6): fwd = T(fwd)
    aff = (2 ** 6 * (y + 1) - 48) // 3 ** 5 - 1
    print("   n=%8d T^8(n)=%9d chain=%s -> %8d  (<n:%s, T^6-back:%s, affine:%s)"
          % (n, y, vals, z, z < n, fwd == y, aff == z))
print("   n=63 chain values expected [182, 121, 242, 161, 107, 71, 47]:",
      apply_word_direct("DMDDDD", 182) == [182, 121, 242, 161, 107, 71, 47])
```

Output:

```text
W1 random words: 4000 words, 1435087 starts: closed-form 0, legality-class 0,
   affine-prefix 0, positivity 0, inversion 0, value-criterion 0 failures
W2 z-coordinate constant c'_w = c_w - 2^L + 3^a: 0 failures
W3 contracting words (2^(a+b) < 3^a): 6000 starts, 0 failures (all must drop)
W4 universal kill MDD on n = 4 mod 9, n < 200000: 0 failures
W5 witness word DMDDDD: L=6 #D=5 c_w=48 (expect 6,5,48)
   n=      63 T^8(n)=      182 chain=[182, 121, 242, 161, 107, 71, 47] ->       47  (<n:True, T^6-back:True, affine:True)
   n=     319 T^8(n)=      911 chain=[911, 607, 1214, 809, 539, 359, 239] ->      239  (<n:True, T^6-back:True, affine:True)
   n=     575 T^8(n)=     1640 chain=[1640, 1093, 2186, 1457, 971, 647, 431] ->      431  (<n:True, T^6-back:True, affine:True)
   n=   24895 T^8(n)=    70895 chain=[70895, 47263, 94526, 63017, 42011, 28007, 18671] ->    18671  (<n:True, T^6-back:True, affine:True)
   n= 3160383 T^8(n)=  8999687 chain=[8999687, 5999791, 11999582, 7999721, 5333147, 3555431, 2370287] ->  2370287  (<n:True, T^6-back:True, affine:True)
   n=63 chain values expected [182, 121, 242, 161, 107, 71, 47]: True
```

Notes: 4000 random words, 1.44 million starts, zero failures on the affine form
(checked at every prefix), the closed form of $c_w$, the single-congruence
legality (both directions), positivity, inversion, and the exact value
criterion. W4 is the universal $\mathsf{MDD}$ kill behind
$\mu \not\equiv 4 \bmod 9$, exhaustive to $2\cdot 10^5$. W5 re-verifies the
L-9919.8 witness chain $182 \to 121 \to 242 \to 161 \to 107 \to 71 \to 47$
byte-for-byte on five representatives including $3160383$, and checks
$c_{\mathsf{DMDDDD}} = 48$ against the affine form.

### Script 2 — `l9926_int.py` (L-9926.2/.3: the exact sieve, gate, certificates)

```python
#!/usr/bin/env python3
# l9926_int.py -- the interleaved descent-doubling sieve Int(k) (L-9926.2/.3):
#   * EXACT computation of Int(k) for k <= 20 (word length bound |w| <= j PROVED,
#     so there is NO word-length cap: the computed set IS Int(k));
#   * gate: reproduction of the L-9919.8 capped algorithm (word length <= 12,
#     positivity thresholds) and its published counts 7/16/46/144/436/1366;
#   * explicit survivor lists mod 2^k for k <= 12;
#   * Int(k) subset of Aug(k) subset of L-9909 survivors, as sets, k <= 16;
#   * B^int_k (first-kill level, least threshold at it), k <= 20;
#   * EVERY kill certificate at levels <= 16 verified by direct integer
#     iteration on 3 representatives (small, medium, large).
# Agent: fable-02-p20.  Python 3 stdlib only; exact arithmetic.  FINITE COMPUTATION.
from fractions import Fraction

POW3 = [3 ** i for i in range(80)]

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def kill_best(j, aj, delta):
    """min-threshold class-uniform interleaved kill at index j, or None.
       State: (cnt moves, e D-moves, Q); P = 2^cnt 3^{aj-e}, S = 2^j.
       Kill at a node: P < S (theta = Q/(S-P) - 1) or P = S and Q < 0 (theta = -1).
       Words never need length > j (L-9926.2(3)), so the search is complete."""
    S = 1 << j; best = None
    stack = [(0, 0, delta, "")]
    while stack:
        cnt, e, q, w = stack.pop()
        P = (1 << cnt) * POW3[aj - e]
        if P < S:
            th = Fraction(q, S - P) - 1
            if best is None or (th, w) < best: best = (th, w)
        elif P == S and q < 0:
            if best is None or (Fraction(-1), w) < best: best = (Fraction(-1), w)
        if cnt >= j: continue
        cnt2 = cnt + 1
        dl = min(j - cnt2, aj - e)                      # max D's still playable
        if (1 << (cnt2 + dl)) * POW3[aj - e] <= S * POW3[dl]:   # min reachable P <= S
            stack.append((cnt2, e, 2 * q - S, w + "M"))
        if e < aj and q % 3 == 0:                       # class-uniform D-legality
            e2 = e + 1
            dl = min(j - cnt2, aj - e2)
            if (1 << (cnt2 + dl)) * POW3[aj - e2] <= S * POW3[dl]:
                stack.append((cnt2, e2, (2 * q) // 3, w + "D"))
    return best

def kill_exists(j, aj, delta):
    S = 1 << j
    stack = [(0, 0, delta)]
    while stack:
        cnt, e, q = stack.pop()
        P = (1 << cnt) * POW3[aj - e]
        if P < S or (P == S and q < 0): return True
        if cnt >= j: continue
        cnt2 = cnt + 1
        dl = min(j - cnt2, aj - e)
        if (1 << (cnt2 + dl)) * POW3[aj - e] <= S * POW3[dl]:
            stack.append((cnt2, e, 2 * q - S))
        if e < aj and q % 3 == 0:
            e2 = e + 1
            dl = min(j - cnt2, aj - e2)
            if (1 << (cnt2 + dl)) * POW3[aj - e2] <= S * POW3[dl]:
                stack.append((cnt2, e2, (2 * q) // 3))
    return False

def nu3(x):
    if x == 0: return None
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v

def aug_kill_at(j, aj, delta):
    """L-9919.4 branch-(U) kill at index j (pure-descent sieve)."""
    v = nu3(delta); m = aj if v is None else min(aj, v)
    return POW3[aj - m] < (1 << (j - m))

# ===========================================================================
# PART A -- tree computation of Int(k), Aug(k), L-9909(k) with residues, k <= KA
# ===========================================================================
KA = 20
cnt_int = [1] + [0] * KA; cnt_aug = [1] + [0] * KA; cnt_old = [1] + [0] * KA
lists_int = {k: [] for k in range(1, 13)}
lists_aug16 = {k: set() for k in range(1, 17)}
lists_int16 = {k: set() for k in range(1, 17)}
certs = []                       # (level j, class r mod 2^j, aj, delta, theta, word)
# stack entries: (level j, a_j, delta_j, r, alive_int, alive_aug, alive_old)
stack = [(0, 0, 0, 0, True, True, True)]
while stack:
    j, a, delta, r, ai, aa, ao = stack.pop()
    if j == KA: continue
    j2 = j + 1
    # representative of class r mod 2^j is r if r > 0 else 2^j; its T^j parity:
    rep = r if r > 0 else (1 << j)
    y = (POW3[a] * (rep + 1) + delta) >> j            # y = T^j(rep) + 1
    par = (y - 1) & 1
    for b in (0, 1):
        a2 = a + b
        d2 = 3 * delta if b == 1 else delta + (1 << j)
        r2 = rep % (1 << j2) if par == b else (rep + (1 << j)) % (1 << j2)
        # r2 as canonical residue in [0, 2^{j2}):
        ao2 = ao and (POW3[a2] >= (1 << j2))
        aa2 = aa and not aug_kill_at(j2, a2, d2)
        ai2 = ai
        if ai2:
            if kill_exists(j2, a2, d2):
                ai2 = False
                th, w = kill_best(j2, a2, d2)
                certs.append((j2, r2, a2, d2, th, w))
        if ao2: cnt_old[j2] += 1
        if aa2:
            cnt_aug[j2] += 1
            if j2 <= 16: lists_aug16[j2].add(r2)
        if ai2:
            cnt_int[j2] += 1
            if j2 <= 12: lists_int[j2].append(r2)
            if j2 <= 16: lists_int16[j2].add(r2)
        if ao2 or aa2 or ai2:
            stack.append((j2, a2, d2, r2, ai2, aa2, ao2))
print("PART A  exact counts")
print("    k   L-9909    Aug(k)    Int(k)   old/int")
for k in range(1, KA + 1):
    print("   %2d  %7d  %8d  %8d   %7.4f" % (k, cnt_old[k], cnt_aug[k], cnt_int[k],
                                             cnt_old[k] / cnt_int[k]))
EXP_OLD = [1, 1, 2, 3, 4, 8, 13, 19, 38, 64, 128, 226, 367, 734, 1295, 2114,
           4228, 7495, 14990, 27328]
EXP_AUG = [1, 1, 2, 3, 4, 7, 12, 18, 32, 57, 102, 192, 324, 593, 1100, 1855,
           3407, 6329, 11698, 22384]
print("   L-9909 counts match L-9909.4/L-9919.5 tables:", cnt_old[1:] == EXP_OLD)
print("   Aug counts match L-9919.5(a)/PART C tables:  ", cnt_aug[1:] == EXP_AUG)

# ===========================================================================
# PART B -- explicit Int lists mod 2^k, k <= 12, and Int subset Aug (sets, k<=16)
# ===========================================================================
print()
print("PART B  explicit Int(k) classes mod 2^k, k <= 12")
for k in range(1, 13):
    print("   mod %4d : %s" % (1 << k, sorted(lists_int[k])))
sub = all(lists_int16[k] <= lists_aug16[k] for k in range(1, 17))
print("   Int(k) subset of Aug(k) as SETS for every k <= 16:", sub)
print("   |Int(16)| = %d, |Aug(16)| = %d, Aug(16) \\ Int(16) = %d classes"
      % (len(lists_int16[16]), len(lists_aug16[16]),
         len(lists_aug16[16] - lists_int16[16])))

# ===========================================================================
# PART C -- B^int_k (first-kill level, least threshold at it)
# ===========================================================================
print()
lev_max = {}
for j2, r2, a2, d2, th, w in certs:
    if j2 not in lev_max or th > lev_max[j2][0]: lev_max[j2] = (th, r2, w)
run = Fraction(-1); Bk = {}
for k in range(1, KA + 1):
    if k in lev_max: run = max(run, lev_max[k][0])
    Bk[k] = run
print("PART C  exceptional bound B^int_k")
print("   B^int_k for k = 1..%d: %s" % (KA, [str(Bk[k]) for k in range(1, KA + 1)]))
worst = max(certs, key=lambda c: c[4])
print("   worst kill overall: level %d, class %d, theta = %s, word %s"
      % (worst[0], worst[1], worst[4], worst[5] if worst[5] else "eps (empty word: T^j(n) < n itself)"))
wl = {}
neq = 0
for j2, r2, a2, d2, th, w in certs:
    wl[len(w)] = wl.get(len(w), 0) + 1
    if len(w) == j2 and w.count("D") == a2: neq += 1
print("   killed prefixes: %d; word lengths of the min-theta kills: %s"
      % (len(certs), dict(sorted(wl.items()))))
print("   kills whose min-theta word has M-moves: %d; equality-type (P=2^j) kills: %d"
      % (sum(1 for c in certs if "M" in c[5]), neq))

# ===========================================================================
# PART D -- verify EVERY certificate at levels <= 16 by direct iteration
# ===========================================================================
print()
print("PART D  direct verification of every kill certificate at levels <= 16")
bad = 0; tested = 0
for j2, r2, a2, d2, th, w in certs:
    if j2 > 16: continue
    rep0 = r2 if r2 > 0 else (1 << j2)
    for t in (0, 1, 97):
        n = rep0 + (t << j2)
        if n <= th: continue
        tested += 1
        y = n
        for _ in range(j2): y = T(y)
        z = y; ok = True; chain = [y]
        for mv in w:
            if mv == "D":
                if z % 3 != 2: ok = False; break
                z = (2 * z - 1) // 3
            else:
                z = 2 * z
            if z < 1: ok = False; break
            chain.append(z)
        if not ok: bad += 1; continue
        back = z
        for _ in range(len(w)): back = T(back)
        if not (z < n and back == y): bad += 1
print("   certificates at levels <= 16: %d; representative checks: %d; failures: %d"
      % (sum(1 for c in certs if c[0] <= 16), tested, bad))

# ===========================================================================
# PART E -- gate: the L-9919.8 capped algorithm reproduced (cap 12), k <= 16
# ===========================================================================
print()
print("PART E  gate: L-9919.8 algorithm (word length <= 12, positivity thresholds)")
def backword_kill_gate(j, a, delta, L):
    S = 2 ** j; best = None
    stack = [(3 ** a, delta, 0, Fraction(-1))]
    while stack:
        p, q, dep, pos = stack.pop()
        if S > p:
            t = max(Fraction(q, S - p) - 1, pos)
            if best is None or t < best: best = t
        rem = L - dep
        if rem <= 0 or p * 2 ** rem >= S * 3 ** rem: continue
        if p % 3 == 0 and q % 3 == 0:
            p2, q2 = 2 * p // 3, 2 * q // 3
            stack.append((p2, q2, dep + 1, max(pos, Fraction(2 * S - q2, p2) - 1)))
        p2, q2 = 2 * p, 2 * q - S
        stack.append((p2, q2, dep + 1, max(pos, Fraction(2 * S - q2, p2) - 1)))
    return best
gate_alive = {}
stack = [(0, 0, 0, 0)]
gate_cnt = [1] + [0] * 16
gate_lists16 = set()
while stack:
    j, a, delta, r = stack.pop()
    if j == 16: continue
    j2 = j + 1
    rep = r if r > 0 else (1 << j)
    y = (POW3[a] * (rep + 1) + delta) >> j
    par = (y - 1) & 1
    for b in (0, 1):
        a2 = a + b
        d2 = 3 * delta if b == 1 else delta + (1 << j)
        r2 = rep % (1 << j2) if par == b else (rep + (1 << j)) % (1 << j2)
        if aug_kill_at(j2, a2, d2): continue           # their pure-descent filter
        if backword_kill_gate(j2, a2, d2, 12) is not None: continue
        gate_cnt[j2] += 1
        if j2 == 16: gate_lists16.add(r2)
        stack.append((j2, a2, d2, r2))
EXP_GATE = {6: 7, 8: 16, 10: 46, 12: 144, 14: 436, 16: 1366}
print("   gate counts k=6..16 (even): %s   match L-9919.8(3): %s"
      % ({k: gate_cnt[k] for k in (6, 8, 10, 12, 14, 16)},
         all(gate_cnt[k] == EXP_GATE[k] for k in EXP_GATE)))
rec = sorted(gate_lists16 - lists_int16[16])
print("   classes alive under the cap-12 gate but dead exactly (cap removed):", rec)
for r in rec:
    for j2, r2, a2, d2, th, w in certs:
        if j2 <= 16 and r2 == r % (1 << j2):
            print("     r=%d mod 2^16: killed at level %d by word %s (length %d, theta %s)"
                  % (r, j2, w, len(w), th))
```

Output:

```text
PART A  exact counts
    k   L-9909    Aug(k)    Int(k)   old/int
    1        1         1         1    1.0000
    2        1         1         1    1.0000
    3        2         2         2    1.0000
    4        3         3         3    1.0000
    5        4         4         4    1.0000
    6        8         7         7    1.1429
    7       13        12        11    1.1818
    8       19        18        16    1.1875
    9       38        32        27    1.4074
   10       64        57        46    1.3913
   11      128       102        80    1.6000
   12      226       192       144    1.5694
   13      367       324       242    1.5165
   14      734       593       436    1.6835
   15     1295      1100       802    1.6147
   16     2114      1855      1363    1.5510
   17     4228      3407      2499    1.6919
   18     7495      6329      4600    1.6293
   19    14990     11698      8463    1.7712
   20    27328     22384     15870    1.7220
   L-9909 counts match L-9909.4/L-9919.5 tables: True
   Aug counts match L-9919.5(a)/PART C tables:   True

PART B  explicit Int(k) classes mod 2^k, k <= 12
   mod    2 : [1]
   mod    4 : [3]
   mod    8 : [3, 7]
   mod   16 : [7, 11, 15]
   mod   32 : [7, 15, 27, 31]
   mod   64 : [7, 27, 31, 39, 47, 59, 63]
   mod  128 : [27, 31, 39, 47, 63, 71, 91, 103, 111, 123, 127]
   mod  256 : [27, 31, 47, 71, 91, 103, 111, 127, 155, 159, 167, 191, 231, 239, 251, 255]
   mod  512 : [27, 31, 47, 71, 91, 103, 111, 127, 155, 159, 167, 191, 231, 239, 251, 255, 283, 303, 327, 347, 359, 415, 423, 447, 495, 507, 511]
   mod 1024 : [27, 31, 47, 71, 91, 103, 111, 127, 155, 159, 167, 191, 231, 239, 251, 283, 303, 327, 359, 415, 447, 495, 511, 543, 559, 603, 623, 639, 667, 671, 679, 703, 743, 751, 763, 767, 795, 839, 859, 871, 927, 935, 959, 1007, 1019, 1023]
   mod 2048 : [27, 31, 47, 71, 91, 103, 111, 127, 159, 167, 191, 239, 251, 303, 327, 415, 447, 495, 511, 559, 603, 623, 639, 667, 671, 679, 703, 743, 751, 763, 767, 795, 839, 859, 871, 927, 935, 959, 1007, 1019, 1023, 1051, 1055, 1095, 1115, 1127, 1135, 1151, 1179, 1183, 1191, 1215, 1255, 1263, 1275, 1307, 1327, 1351, 1383, 1439, 1471, 1519, 1567, 1583, 1663, 1691, 1695, 1727, 1767, 1775, 1791, 1819, 1883, 1895, 1951, 1959, 1983, 2031, 2043, 2047]
   mod 4096 : [27, 31, 47, 71, 91, 103, 111, 127, 159, 167, 191, 239, 251, 303, 327, 415, 447, 495, 511, 559, 603, 623, 639, 667, 671, 679, 703, 743, 751, 763, 767, 839, 859, 871, 927, 959, 1007, 1051, 1055, 1095, 1115, 1127, 1135, 1151, 1179, 1183, 1215, 1255, 1263, 1307, 1327, 1351, 1383, 1439, 1471, 1519, 1567, 1583, 1663, 1691, 1695, 1727, 1767, 1775, 1791, 1819, 1883, 1895, 1951, 1959, 1983, 2043, 2047, 2075, 2079, 2095, 2119, 2139, 2151, 2159, 2175, 2207, 2215, 2287, 2299, 2375, 2463, 2495, 2543, 2559, 2651, 2671, 2687, 2715, 2719, 2727, 2751, 2791, 2799, 2811, 2815, 2843, 2887, 2983, 3007, 3055, 3067, 3071, 3099, 3103, 3175, 3183, 3199, 3227, 3231, 3239, 3263, 3303, 3311, 3323, 3355, 3375, 3431, 3487, 3519, 3567, 3615, 3631, 3711, 3739, 3743, 3775, 3815, 3823, 3839, 3867, 3931, 3943, 3999, 4007, 4031, 4079, 4091, 4095]
   Int(k) subset of Aug(k) as SETS for every k <= 16: True
   |Int(16)| = 1363, |Aug(16)| = 1855, Aug(16) \ Int(16) = 492 classes

PART C  exceptional bound B^int_k
   B^int_k for k = 1..20: ['0', '1', '1', '1', '23/5', '23/5', '23/5', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13', '319/13']
   worst kill overall: level 8, class 123, theta = 319/13, word eps (empty word: T^j(n) < n itself)
   killed prefixes: 2879; word lengths of the min-theta kills: {0: 132, 1: 1513, 2: 81, 3: 126, 4: 432, 5: 167, 6: 98, 7: 109, 8: 38, 9: 22, 10: 36, 11: 23, 12: 65, 13: 5, 14: 3, 15: 6, 16: 5, 17: 6, 18: 12}
   kills whose min-theta word has M-moves: 1154; equality-type (P=2^j) kills: 0

PART D  direct verification of every kill certificate at levels <= 16
   certificates at levels <= 16: 461; representative checks: 1382; failures: 0

PART E  gate: L-9919.8 algorithm (word length <= 12, positivity thresholds)
   gate counts k=6..16 (even): {6: 7, 8: 16, 10: 46, 12: 144, 14: 436, 16: 1366}   match L-9919.8(3): True
   classes alive under the cap-12 gate but dead exactly (cap removed): [16383, 24575, 57343]
     r=16383 mod 2^16: killed at level 16 by word DMDDDDDDDDDDDD (length 14, theta -1)
     r=24575 mod 2^16: killed at level 15 by word DMDDDDDDDDDDD (length 13, theta -1)
     r=57343 mod 2^16: killed at level 15 by word DMDDDDDDDDDDD (length 13, theta -1)
```

Notes: PART A recomputes L-9909$(k)$ and $\mathrm{Aug}(k)$ alongside
$\mathrm{Int}(k)$ and gates them against the published tables (both `True`).
PART D verifies **every** kill certificate at levels $\le 16$ — 461 of them, on
three representatives each — by direct iteration: legality, positivity, descent
$z < n$, and the forward return $T^{|w|}(z) = T^j(n)$; zero failures. PART E
reproduces L-9919.8's capped algorithm exactly (its published counts
$7/16/46/144/436/1366$) and exhibits the three classes the cap missed.

### Script 3 — `l9926_rate.py` (L-9926.3(e)/.5: exact counts to k = 26)

```python
#!/usr/bin/env python3
# l9926_rate.py -- L-9926.3/.5: is the interleaved sieve's gain over L-9909 a
# bounded factor (like L-9919's pure-descent augmentation) or a genuine
# improvement of the exponential rate?  Exact counts of L-9909(k), Aug(k),
# Int(k) for k <= 26.  Counts exact; logs float (display only).
# Agent: fable-02-p20.  Python 3 stdlib only.  FINITE COMPUTATION (~3 min).
import math

POW3 = [3 ** i for i in range(100)]
KMAX = 26

def nu3(x):
    if x == 0: return None
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v

def aug_kill_at(j, aj, delta):
    v = nu3(delta); m = aj if v is None else min(aj, v)
    return POW3[aj - m] < (1 << (j - m))

def int_kill_at(j, aj, delta):
    S = 1 << j
    stack = [(0, 0, delta)]
    while stack:
        cnt, e, q = stack.pop()
        P = (1 << cnt) * POW3[aj - e]
        if P < S or (P == S and q < 0): return True
        if cnt >= j: continue
        cnt2 = cnt + 1
        dl = min(j - cnt2, aj - e)
        if (1 << (cnt2 + dl)) * POW3[aj - e] <= S * POW3[dl]:
            stack.append((cnt2, e, 2 * q - S))
        if e < aj and q % 3 == 0:
            e2 = e + 1
            dl = min(j - cnt2, aj - e2)
            if (1 << (cnt2 + dl)) * POW3[aj - e2] <= S * POW3[dl]:
                stack.append((cnt2, e2, (2 * q) // 3))
    return False

cnt_int = [1] + [0] * KMAX
stack = [(0, 0, 0)]
while stack:
    j, a, delta = stack.pop()
    if j == KMAX: continue
    j2 = j + 1
    for b in (0, 1):
        a2 = a + b
        d2 = 3 * delta if b == 1 else delta + (1 << j)
        if not int_kill_at(j2, a2, d2):
            cnt_int[j2] += 1
            stack.append((j2, a2, d2))

cnt_aug = [1] + [0] * KMAX
stack = [(0, 0, 0)]
while stack:
    j, a, delta = stack.pop()
    if j == KMAX: continue
    j2 = j + 1
    for b in (0, 1):
        a2 = a + b
        d2 = 3 * delta if b == 1 else delta + (1 << j)
        if not aug_kill_at(j2, a2, d2):
            cnt_aug[j2] += 1
            stack.append((j2, a2, d2))

old = [0] * (KMAX + 1); dp = {0: 1}; old[0] = 1
for j in range(1, KMAX + 1):
    nd = {}
    for a, c in dp.items():
        for b in (0, 1):
            a2 = a + b
            if POW3[a2] >= (1 << j): nd[a2] = nd.get(a2, 0) + c
    dp = nd; old[j] = sum(dp.values())

print("  k    L-9909       Aug(k)       Int(k)   old/int  log2(old/int)  (1/k)log2   log2(aug/int)")
for k in range(1, KMAX + 1):
    o, A, I = old[k], cnt_aug[k], cnt_int[k]
    L = math.log2(o / I); LA = math.log2(A / I)
    print("%3d %9d %12d %12d   %7.4f      %8.5f    %8.5f       %8.5f"
          % (k, o, A, I, o / I, L, L / k, LA))
print()
print("summary over k = 8,12,16,20,24,26:")
print("  (1/k)log2(L9909/Int):", ", ".join("%.4f" % (math.log2(old[k]/cnt_int[k])/k) for k in (8,12,16,20,24,26)))
print("  (1/k)log2(L9909/Aug):", ", ".join("%.4f" % (math.log2(old[k]/cnt_aug[k])/k) for k in (8,12,16,20,24,26)))
print("  log2(L9909/Int) increments per 2 levels, k=8->26:",
      ", ".join("%.3f" % (math.log2(old[k+2]/cnt_int[k+2]) - math.log2(old[k]/cnt_int[k])) for k in range(8, 25, 2)))
print("  log2(L9909/Aug) increments per 2 levels, k=8->26:",
      ", ".join("%.3f" % (math.log2(old[k+2]/cnt_aug[k+2]) - math.log2(old[k]/cnt_aug[k])) for k in range(8, 25, 2)))
print("  per-level survivor growth Int(k+1)/Int(k), k=20..25:",
      ", ".join("%.4f" % (cnt_int[k+1]/cnt_int[k]) for k in range(20, 26)))
print("  per-level survivor growth L9909(k+1)/L9909(k), k=20..25:",
      ", ".join("%.4f" % (old[k+1]/old[k]) for k in range(20, 26)))
```

Output (runtime a few minutes; counts exact):

```text
  k    L-9909       Aug(k)       Int(k)   old/int  log2(old/int)  (1/k)log2   log2(aug/int)
  1         1            1            1    1.0000       0.00000     0.00000        0.00000
  2         1            1            1    1.0000       0.00000     0.00000        0.00000
  3         2            2            2    1.0000       0.00000     0.00000        0.00000
  4         3            3            3    1.0000       0.00000     0.00000        0.00000
  5         4            4            4    1.0000       0.00000     0.00000        0.00000
  6         8            7            7    1.1429       0.19265     0.03211        0.00000
  7        13           12           11    1.1818       0.24101     0.03443        0.12553
  8        19           18           16    1.1875       0.24793     0.03099        0.16993
  9        38           32           27    1.4074       0.49304     0.05478        0.24511
 10        64           57           46    1.3913       0.47644     0.04764        0.30933
 11       128          102           80    1.6000       0.67807     0.06164        0.35050
 12       226          192          144    1.5694       0.65025     0.05419        0.41504
 13       367          324          242    1.5165       0.60077     0.04621        0.42099
 14       734          593          436    1.6835       0.75145     0.05368        0.44370
 15      1295         1100          802    1.6147       0.69128     0.04609        0.45583
 16      2114         1855         1363    1.5510       0.63319     0.03957        0.44463
 17      4228         3407         2499    1.6919       0.75862     0.04462        0.44715
 18      7495         6329         4600    1.6293       0.70429     0.03913        0.46034
 19     14990        11698         8463    1.7712       0.82476     0.04341        0.46702
 20     27328        22384        15870    1.7220       0.78408     0.03920        0.49617
 21     46611        39549        28147    1.6560       0.72769     0.03465        0.49066
 22     93222        73718        52176    1.7867       0.83728     0.03806        0.49863
 23    168807       139084        97978    1.7229       0.78484     0.03412        0.50543
 24    286581       243479       172868    1.6578       0.72927     0.03039        0.49413
 25    573162       453678       322021    1.7799       0.83179     0.03327        0.49451
 26   1037374       854473       602780    1.7210       0.78323     0.03012        0.50340

summary over k = 8,12,16,20,24,26:
  (1/k)log2(L9909/Int): 0.0310, 0.0542, 0.0396, 0.0392, 0.0304, 0.0301
  (1/k)log2(L9909/Aug): 0.0098, 0.0196, 0.0118, 0.0144, 0.0098, 0.0108
  log2(L9909/Int) increments per 2 levels, k=8->26: 0.229, 0.174, 0.101, -0.118, 0.071, 0.080, 0.053, -0.108, 0.054
  log2(L9909/Aug) increments per 2 levels, k=8->26: 0.089, 0.068, 0.073, -0.119, 0.055, 0.044, 0.051, -0.104, 0.045
  per-level survivor growth Int(k+1)/Int(k), k=20..25: 1.7736, 1.8537, 1.8778, 1.7644, 1.8628, 1.8719
  per-level survivor growth L9909(k+1)/L9909(k), k=20..25: 1.7056, 2.0000, 1.8108, 1.6977, 2.0000, 1.8099
```

### Script 4 — `l9926_pern.py` (two-sided per-n exactness of the whole calculus)

```python
#!/usr/bin/env python3
# l9926_pern.py -- TWO-SIDED exact agreement test for the full word calculus
# (class-uniform AND n-dependent): for the finite family j <= J = 8, |w| <= L = 8,
# the certificate enumeration (congruence classes + exact rational thresholds,
# computed from (a_j, delta_j) alone) must predict, for EVERY n, exactly the
# same kill verdict as direct integer iteration of backward chains.
# There is no wiggle room: one boundary error in a threshold, a wrong legality
# class, or a missed word shows up as a mismatch.
# Agent: fable-02-p20.  Python 3 stdlib only; exact arithmetic (int/Fraction).
# FINITE VERIFICATION, NOT PROOF.
from fractions import Fraction

POW3 = [3 ** i for i in range(40)]
J = 8          # orbit indices j = 0..J
LCAP = 8       # word lengths 0..LCAP  (the EMPTY word covers T^j(n) < n itself)
NMAX = 50000

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def word_data_of_class(r, k):
    n = r if r > 0 else 1 << k
    a = [0]; delta = [0]; m = n
    for i in range(k):
        b = m % 2
        a.append(a[-1] + b); delta.append(3 * delta[-1] if b == 1 else delta[-1] + (1 << i))
        m = T(m)
    return a, delta

def certs_for(j, aj, delta):
    """ALL kill certificates at index j with |w| <= LCAP: list of
       (m, res, typ, th): kill set = {n = res-1 mod 3^m} intersect
       {n > th} (typ +1) / {n < th} (typ -1) / all n (typ 0).
       State: cnt moves, e D's, Bq;  2^j 3^e (z_i + 1) = 2^cnt 3^aj u + Bq...
       cleared form: value expr u_i = (2^cnt 3^aj u + Bq)/(2^j 3^e);
       M: Bq' = 2Bq - 2^j 3^e ; D: Bq' = 2Bq, e' = e+1 after refining legality."""
    out = []
    A3 = POW3[aj]
    stack = [(0, 0, delta, 0, 0)]        # cnt, e, Bq, res (u-class), m
    while stack:
        cnt, e, Bq, res, m = stack.pop()
        lhs = (1 << j) * POW3[e]; rhs = (1 << cnt) * A3
        if lhs > rhs:
            out.append((m, res, +1, Fraction(Bq, lhs - rhs) - 1))
        elif lhs == rhs:
            if Bq < 0: out.append((m, res, 0, None))
        else:
            out.append((m, res, -1, Fraction(Bq, lhs - rhs) - 1))
        if cnt >= LCAP: continue
        cnt2 = cnt + 1
        stack.append((cnt2, e, 2 * Bq - (1 << j) * POW3[e], res, m))    # M
        # D: refine legality on u = res mod 3^m: need 3^{e+1} | 2^cnt 3^aj u + Bq
        C0 = (1 << cnt) * A3 * res + Bq
        if aj + m >= e + 1:
            if C0 % POW3[e + 1] == 0:
                stack.append((cnt2, e + 1, 2 * Bq, res, m))
        else:
            g = POW3[aj + m]
            if C0 % g == 0:
                mod_t = POW3[e + 1 - aj - m]
                inv2 = pow((1 << cnt) % mod_t, -1, mod_t)
                t0 = (-(C0 // g) * inv2) % mod_t
                stack.append((cnt2, e + 1, 2 * Bq, res + POW3[m] * t0, e + 1 - aj))
    return out

# per class mod 2^J: all certificates for all j <= J, grouped by (m, res mod 3^m)
CERT = []
for r in range(1 << J):
    a, delta = word_data_of_class(r, J)
    d = {}
    for j in range(0, J + 1):
        for (m, res, typ, th) in certs_for(j, a[j], delta[j]):
            d.setdefault((m, res % POW3[m]), []).append((typ, th))
    CERT.append(d)
print("certificate enumeration: %d classes, total cert groups %d"
      % (1 << J, sum(len(d) for d in CERT)))

def killed_pred(n):
    d = CERT[n % (1 << J)]
    u = n + 1
    for m in range(0, 9):
        key = (m, u % POW3[m])
        if key in d:
            for (typ, th) in d[key]:
                if typ == 0: return True
                if typ == +1 and n > th: return True
                if typ == -1 and n < th: return True
    return False

def killed_direct(n):
    for j in range(0, J + 1):
        y = n
        for _ in range(j): y = T(y)
        # DFS over backward chains from y, length <= LCAP, per-n legality
        stack = [(y, 0)]
        while stack:
            z, l = stack.pop()
            if z < n: return True
            if l >= LCAP: continue
            stack.append((2 * z, l + 1))
            if z % 3 == 2: stack.append(((2 * z - 1) // 3, l + 1))
    return False

mism = []; nkill = 0
for n in range(1, NMAX + 1):
    kp = killed_pred(n); kd = killed_direct(n)
    if kp: nkill += 1
    if kp != kd: mism.append(n)
print("n <= %d, J = %d, |w| <= %d: predicted-killed %d, mismatches %d %s"
      % (NMAX, J, LCAP, nkill, len(mism), mism[:10]))

# consistency: classes with a class-uniform 'kill-for-all-large-n' cert (m = 0,
# typ +1 or 0) at some j <= 8 must be exactly the complement of Int(8).
INT8 = [27, 31, 47, 71, 91, 103, 111, 127, 155, 159, 167, 191, 231, 239, 251, 255]
u8 = []
for r in range(1 << J):
    has = any(m == 0 and typ in (0, +1) for (m, rr), lst in CERT[r].items() for (typ, th) in lst)
    if not has: u8.append(r)
print("classes with NO class-uniform kill at j <= 8:", u8)
print("matches Int(8) from l9926_int.py:", u8 == INT8)
```

Output:

```text
certificate enumeration: 256 classes, total cert groups 50659
n <= 50000, J = 8, |w| <= 8: predicted-killed 48305, mismatches 0 []
classes with NO class-uniform kill at j <= 8: [27, 31, 47, 71, 91, 103, 111, 127, 155, 159, 167, 191, 231, 239, 251, 255]
matches Int(8) from l9926_int.py: True
```

Notes: this is the strongest single test in the file. For the complete finite
family $j \le 8$, $|w| \le 8$ (class-uniform AND $n$-dependent, all refinement
depths, all three threshold regimes including the $\Delta < 0$ small-$n$ regime
and the $\Delta = 0$ constant-shift regime), the certificate predictions —
computed from $(a_j, \delta_j)$ and congruence arithmetic alone, with exact
rational thresholds — agree with direct integer backward-chain search for
**every** $n \le 50000$ with zero mismatches. A single boundary error in any
threshold, any legality class, any missed word, or the positivity claim would
break it.

### Script 5 — `l9926_joint.py` (L-9926.4/.5: the 3-adic layers)

```python
#!/usr/bin/env python3
# l9926_joint.py -- the 3-adic side of the interleaved sieve (L-9926.4/.5):
#   PART A: the UNIVERSAL backward-word congruences (j = 0 kills, independent of
#           any 2-adic class): K3(D) killed residues mod 3^D for D <= 7, the
#           primitive-word structure, mu mod 36, the first depth-4 class;
#   PART B: product-form test  Joint_int(k,D) =? Int(k) x M3(D):
#           HOLDS at D <= 3 (k <= 14), FAILS at D = 4 (genuinely mixed,
#           class-dependent kills) -- with exact joint pair counts;
#   PART C: an explicit mixed kill verified on representatives, plus its
#           class-dependence (same 3-adic residue allowed for another class);
#   PART D: mu pair tables and thresholds (all kills discharged).
# Agent: fable-02-p20.  Python 3 stdlib only; exact arithmetic.  FINITE COMPUTATION.
from fractions import Fraction

POW3 = [3 ** i for i in range(60)]

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def word_data_of_class(r, k):
    n = r if r > 0 else 1 << k
    a = [0]; delta = [0]; m = n
    for i in range(k):
        b = m % 2
        a.append(a[-1] + b); delta.append(3 * delta[-1] if b == 1 else delta[-1] + (1 << i))
        m = T(m)
    return a, delta

def kill_exists_uniform(j, aj, delta):
    S = 1 << j
    stack = [(0, 0, delta)]
    while stack:
        cnt, e, q = stack.pop()
        P = (1 << cnt) * POW3[aj - e]
        if P < S or (P == S and q < 0): return True
        if cnt >= j: continue
        cnt2 = cnt + 1
        dl = min(j - cnt2, aj - e)
        if (1 << (cnt2 + dl)) * POW3[aj - e] <= S * POW3[dl]:
            stack.append((cnt2, e, 2 * q - S))
        if e < aj and q % 3 == 0:
            e2 = e + 1
            dl = min(j - cnt2, aj - e2)
            if (1 << (cnt2 + dl)) * POW3[aj - e2] <= S * POW3[dl]:
                stack.append((cnt2, e2, (2 * q) // 3))
    return False

def int_classes(K):
    out = []
    for r in range(1 << K):
        a, delta = word_data_of_class(r, K)
        if any(kill_exists_uniform(j, a[j], delta[j]) for j in range(0, K + 1)): continue
        out.append(r)
    return out

def forbidden(j, aj, delta, D, collect=None):
    """set of s mod 3^D killed at index j: certificates with legality refinement
       depth m <= D (deeper kills are only partial at granularity 3^D) and value
       coefficient Delta > 0 (or = 0 with Bq < 0).  Kills all n in the class with
       u = res mod 3^m and n > theta.  Length bound: a kill needs
       2^{cnt-j} < 3^{e-aj} <= 3^D, so cnt < j + D log2 3 <= j + 2D + 2."""
    S3D = POW3[D]; forb = set()
    A3 = POW3[aj]; CAP = j + 2 * D + 2
    stack = [(0, 0, delta, 0, 0, "")]
    while stack:
        cnt, e, Bq, res, m, w = stack.pop()
        lhs = (1 << j) * POW3[e]; rhs = (1 << cnt) * A3
        kill = None
        if lhs > rhs: kill = Fraction(Bq, lhs - rhs) - 1
        elif lhs == rhs and Bq < 0: kill = Fraction(-1)
        if kill is not None:
            if collect is not None: collect.append((j, w, m, res, kill))
            step = POW3[m]; r0 = (res - 1) % step
            for s in range(r0, S3D, step): forb.add(s)
        if cnt >= CAP: continue
        cnt2 = cnt + 1
        dcap = aj + D - e
        dl = max(0, min(CAP - cnt2, dcap))
        if (1 << (cnt2 + dl)) * A3 <= (1 << j) * POW3[e + dl]:
            stack.append((cnt2, e, 2 * Bq - (1 << j) * POW3[e], res, m, w + "M"))
        if e < aj + D:
            C0 = (1 << cnt) * A3 * res + Bq
            ok = True; res2 = res; m2 = m
            if aj + m >= e + 1:
                if C0 % POW3[e + 1] != 0: ok = False
            else:
                g = POW3[aj + m]
                if C0 % g != 0: ok = False
                else:
                    mod_t = POW3[e + 1 - aj - m]
                    inv2 = pow((1 << cnt) % mod_t, -1, mod_t)
                    res2 = res + POW3[m] * ((-(C0 // g) * inv2) % mod_t)
                    m2 = e + 1 - aj
            if ok:
                e2 = e + 1
                dl = max(0, min(CAP - cnt2, aj + D - e2))
                if (1 << (cnt2 + dl)) * A3 <= (1 << j) * POW3[e2 + dl]:
                    stack.append((cnt2, e2, 2 * Bq, res2, m2, w + "D"))
    return forb

# ===========================================================================
print("PART A  the universal (j = 0) backward-word congruences")
prev = None
K3 = {}
for D in range(1, 8):
    certs = []
    F0 = forbidden(0, 0, 0, D, collect=certs)
    K3[D] = F0
    assert all(th <= -1 for (_, _, _, _, th) in certs), "universal kill with theta > -1"
    new = len(F0) - (3 * len(prev) if prev is not None else 0)
    print("   D=%d: |K3| = %4d / %5d  allowed density %.5f   new classes beyond lift: %d"
          % (D, len(F0), POW3[D], 1 - len(F0) / POW3[D], new))
    prev = F0
print("   K3(1) =", sorted(K3[1]), "  K3(2) =", sorted(K3[2]))
lift3 = {s for s in range(81) for t in K3[3] if s % 27 == t}
newc = sorted(K3[4] - lift3)
print("   first genuinely-deeper class: n = %s mod 81" % newc)
certs = []; forbidden(0, 0, 0, 4, collect=certs)
for (j, w, m, res, th) in certs:
    if m == 4 and (res - 1) % 81 in newc:
        print("   its certificate: word %s, u = %d mod 81, theta = %s" % (w, res, th))
mu36 = [r for r in range(36) if r % 12 in (3, 7) and r % 9 not in K3[2]]
print("   mu mod 36 (combining L-9919.6(1) with K3(2)):", mu36)
# direct check of the new mod-81 congruence on integers
bad = 0
s_new = newc[0]
for t in range(2000):
    n = s_new + 81 * t
    if n < 1: continue
    z = n; ok = True
    for mv in "MDMDDD":
        if mv == "D":
            if z % 3 != 2: ok = False; break
            z = (2 * z - 1) // 3
        else: z = 2 * z
    if not ok: bad += 1; continue
    back = z
    for _ in range(6): back = T(back)
    if not (1 <= z < n and back == n): bad += 1
print("   direct check of the depth-4 kill on 2000 representatives: %d failures" % bad)

# ===========================================================================
print()
print("PART B  product-form test: Joint_int(k,D) vs Int(k) x M3(D)")
for (K, D) in ((8, 2), (10, 2), (12, 2), (8, 3), (10, 3), (12, 3), (14, 3),
               (8, 4), (10, 4), (12, 4)):
    ints = int_classes(K)
    F0 = frozenset(forbidden(0, 0, 0, D))
    total = 0; diff = 0; sup = 0
    for r in ints:
        a, delta = word_data_of_class(r, K)
        F = set()
        for j in range(0, K + 1):
            F |= forbidden(j, a[j], delta[j], D)
        assert F >= F0
        total += POW3[D] - len(F)
        if frozenset(F) != F0: diff += 1; sup += len(F) - len(F0)
    prod = len(ints) * (POW3[D] - len(F0))
    print("   k=%2d D=%d: |Int|=%4d  Joint=%6d  product form=%6d  classes richer than universal: %4d (extra pairs %d)"
          % (K, D, len(ints), total, prod, diff, sup))

# ===========================================================================
print()
print("PART C  an explicit MIXED (class-dependent, n-dependent) kill at k=12, D=4")
K, D = 12, 4
ints = int_classes(K)
F0 = frozenset(forbidden(0, 0, 0, D))
Fsets = {}
example = None
for r in ints:
    a, delta = word_data_of_class(r, K)
    F = set(); certs = []
    for j in range(0, K + 1):
        F |= forbidden(j, a[j], delta[j], D, collect=certs)
    Fsets[r] = frozenset(F)
    if example is None and F - set(F0):
        s_extra = sorted(F - set(F0))[0]
        for (j, w, m, res, th) in certs:
            if m >= 1 and (res - 1) % POW3[m] == s_extra % POW3[m] and s_extra % 3 != 2:
                example = (r, j, w, m, res, th, s_extra); break
r, j, w, m, res, th, s_extra = example
print("   class r = %d mod 4096: kill at j = %d, word %s, u = %d mod 3^%d = %d," % (r, j, w, res, m, POW3[m]))
print("   theta = %s; kills the pair (r, s) with s = %d mod 81 -- and s %% 3 = %d (NOT the n=2 mod 3 class)"
      % (th, s_extra, s_extra % 3))
# verify on 3 representatives via CRT: n = r mod 2^12, u = res mod 3^m
M2, M3m = 1 << K, POW3[m]
n0 = None
for n in range(1, M2 * M3m + 1):
    if n % M2 == r and (n + 1) % M3m == res % M3m: n0 = n; break
bad = 0
for t in (0, 1, 7):
    n = n0 + t * M2 * M3m
    if n <= th: continue
    y = n
    for _ in range(j): y = T(y)
    z = y; chain = [y]; ok = True
    for mv in w:
        if mv == "D":
            if z % 3 != 2: ok = False; break
            z = (2 * z - 1) // 3
        else: z = 2 * z
        chain.append(z)
    back = z
    for _ in range(len(w)): back = T(back)
    good = ok and 1 <= z < n and back == y
    if not good: bad += 1
    if t == 0:
        print("   n = %d: T^%d(n) = %d, chain %s -> %d < n: %s, T^%d back: %s"
              % (n, j, y, w, z, z < n, len(w), back == y))
print("   representative checks (3 lifts): %d failures" % bad)
# class-dependence: find another Int(12) class whose forbidden set omits s_extra
others = [r2 for r2 in ints if s_extra not in Fsets[r2]]
print("   classes NOT forbidding s = %d mod 81: %d of %d  (e.g. r = %s)"
      % (s_extra, len(others), len(ints), others[:4]))
# and the word is genuinely n-dependent: an n in the class with the WRONG 3-adic
# residue must fail the word's legality
nbad = n0 + M2  # same class mod 2^12, u shifted by 2^12 mod 3^m (changes residue)
if (nbad + 1) % M3m != res % M3m:
    y = nbad
    for _ in range(j): y = T(y)
    z = y; ok = True
    for mv in w:
        if mv == "D":
            if z % 3 != 2: ok = False; break
            z = (2 * z - 1) // 3
        else: z = 2 * z
    print("   n-dependence: n = %d (same class mod 4096, u = %d mod %d instead of %d): word legal? %s"
          % (nbad, (nbad + 1) % M3m, M3m, res % M3m, ok))

# ===========================================================================
print()
print("PART D  mu pair tables (all thresholds discharged against mu > 25)")
for (K, D) in ((8, 1), (8, 2), (12, 2), (12, 4)):
    ints = int_classes(K)
    total = 0; thmax = Fraction(-10)
    for r in ints:
        a, delta = word_data_of_class(r, K)
        F = set(); certs = []
        for jj in range(0, K + 1):
            F |= forbidden(jj, a[jj], delta[jj], D, collect=certs)
        total += POW3[D] - len(F)
        # per killed residue, the LEAST theta over its certificates
        for s in F:
            best = None
            for (jj, ww, mm, rres, tth) in certs:
                if (rres - 1) % POW3[mm] == s % POW3[mm]:
                    if best is None or tth < best: best = tth
            if best is not None and best > thmax: thmax = best
    dens = Fraction(total, (1 << K) * POW3[D])
    print("   (k,D)=(%2d,%d): allowed pairs mod 2^k 3^D = %6d / %8d  density %-10s  max per-pair least theta = %s"
          % (K, D, total, (1 << K) * POW3[D], "%.5f" % float(dens), thmax))
print("   reference: L-9919 joint density (2/3)|Aug(k)|/2^k at k=8: %.5f, k=12: %.5f"
      % ((2 / 3) * 18 / 256, (2 / 3) * 192 / 4096))

# ===========================================================================
print()
print("PART E  depth-1 collapse probe at k = 14 (is mod 3 still just one bit?)")
K = 14
ints = int_classes(K)
extra = 0
for r in ints:
    a, delta = word_data_of_class(r, K)
    F = set()
    for jj in range(0, K + 1):
        F |= forbidden(jj, a[jj], delta[jj], 1)
    if F != {2}: extra += 1
print("   Int(14) classes whose depth-1 forbidden set exceeds {n = 2 mod 3}: %d of %d" % (extra, len(ints)))
```

Output:

```text
PART A  the universal (j = 0) backward-word congruences
   D=1: |K3| =    1 /     3  allowed density 0.66667   new classes beyond lift: 1
   D=2: |K3| =    4 /     9  allowed density 0.55556   new classes beyond lift: 1
   D=3: |K3| =   12 /    27  allowed density 0.55556   new classes beyond lift: 0
   D=4: |K3| =   37 /    81  allowed density 0.54321   new classes beyond lift: 1
   D=5: |K3| =  111 /   243  allowed density 0.54321   new classes beyond lift: 0
   D=6: |K3| =  335 /   729  allowed density 0.54047   new classes beyond lift: 2
   D=7: |K3| = 1013 /  2187  allowed density 0.53681   new classes beyond lift: 8
   K3(1) = [2]   K3(2) = [2, 4, 5, 8]
   first genuinely-deeper class: n = [10] mod 81
   its certificate: word MDMDDD, u = 11 mod 81, theta = -73/17
   mu mod 36 (combining L-9919.6(1) with K3(2)): [3, 7, 15, 19, 27]
   direct check of the depth-4 kill on 2000 representatives: 0 failures

PART B  product-form test: Joint_int(k,D) vs Int(k) x M3(D)
   k= 8 D=2: |Int|=  16  Joint=    80  product form=    80  classes richer than universal:    0 (extra pairs 0)
   k=10 D=2: |Int|=  46  Joint=   230  product form=   230  classes richer than universal:    0 (extra pairs 0)
   k=12 D=2: |Int|= 144  Joint=   720  product form=   720  classes richer than universal:    0 (extra pairs 0)
   k= 8 D=3: |Int|=  16  Joint=   240  product form=   240  classes richer than universal:    0 (extra pairs 0)
   k=10 D=3: |Int|=  46  Joint=   690  product form=   690  classes richer than universal:    0 (extra pairs 0)
   k=12 D=3: |Int|= 144  Joint=  2160  product form=  2160  classes richer than universal:    0 (extra pairs 0)
   k=14 D=3: |Int|= 436  Joint=  6540  product form=  6540  classes richer than universal:    0 (extra pairs 0)
   k= 8 D=4: |Int|=  16  Joint=   690  product form=   704  classes richer than universal:   14 (extra pairs 14)
   k=10 D=4: |Int|=  46  Joint=  1980  product form=  2024  classes richer than universal:   44 (extra pairs 44)
   k=12 D=4: |Int|= 144  Joint=  6194  product form=  6336  classes richer than universal:  142 (extra pairs 142)

PART C  an explicit MIXED (class-dependent, n-dependent) kill at k=12, D=4
   class r = 27 mod 4096: kill at j = 4, word MMDDDMDDDD, u = 61 mod 3^4 = 81,
   theta = -33/17; kills the pair (r, s) with s = 60 mod 81 -- and s % 3 = 0 (NOT the n=2 mod 3 class)
   n = 24603: T^4(n) = 41519, chain MMDDDMDDDD -> 19439 < n: True, T^10 back: True
   representative checks (3 lifts): 0 failures
   classes NOT forbidding s = 60 mod 81: 2 of 144  (e.g. r = [2047, 4095])
   n-dependence: n = 28699 (same class mod 4096, u = 26 mod 81 instead of 61): word legal? False

PART D  mu pair tables (all thresholds discharged against mu > 25)
   (k,D)=( 8,1): allowed pairs mod 2^k 3^D =     32 /      768  density 0.04167     max per-pair least theta = -1
   (k,D)=( 8,2): allowed pairs mod 2^k 3^D =     80 /     2304  density 0.03472     max per-pair least theta = -1
   (k,D)=(12,2): allowed pairs mod 2^k 3^D =    720 /    36864  density 0.01953     max per-pair least theta = -1
   (k,D)=(12,4): allowed pairs mod 2^k 3^D =   6194 /   331776  density 0.01867     max per-pair least theta = -1
   reference: L-9919 joint density (2/3)|Aug(k)|/2^k at k=8: 0.04688, k=12: 0.03125

PART E  depth-1 collapse probe at k = 14 (is mod 3 still just one bit?)
   Int(14) classes whose depth-1 forbidden set exceeds {n = 2 mod 3}: 0 of 436
```

Notes: PART A quantifies the universal layer ($K_3(D)$, $D \le 7$; every
universal kill's threshold asserted $\le -1$), identifies the depth-4 class
$10 \bmod 81$ with its word $\mathsf{MDMDDD}$, checks it on 2000
representatives, and derives $\mu \bmod 36 \in \{3,7,15,19,27\}$. PART B is the
collapse-analogue test: product form holds at every computed $(k, D \le 3)$ and
fails at $D = 4$ exactly as stated. PART C verifies the mixed kill and both of
its defining dependences. PART D computes the pair tables with per-pair least
thresholds (all $= -1$). PART E confirms depth-1 collapse ("mod 3 is one bit")
out to $k = 14$.

### Reproducibility self-check

All five code blocks were re-extracted from this Markdown file by a parser
reading the ```` ```python ```` / ```` ```text ```` pairs, written to fresh
files, executed, and their stdout compared **byte-for-byte** with the recorded
outputs; all five matched (script 3 takes ~3 minutes; the others seconds). No
block is a placeholder; every number above was produced by the code shown above
it. The scripts deliberately print no wall-clock times so that the comparison is
byte-exact.

### Negative / sharpness probes attempted

1. **Does the cap removal matter?** Yes, measurably: three classes at $k \le 16$
   (words of length 13–14), and min-threshold kill words of length up to 18 by
   $k = 20$ — but the counts change by only $3/1366 \approx 0.2\%$ at $k = 16$,
   so L-9919.8's capped table was a good approximation, as it claimed.
2. **Does the equality case $P_L = 2^j$, $Q_L < 0$ ever bite?** Not on the
   computed range (0 min-threshold kills at $k \le 20$); it is retained because
   the completeness proof needs it.
3. **Is the collapse analogue perhaps true after all?** Deliberately attacked
   and REFUTED at depth 4 by an explicitly verified, class-dependent,
   $n$-dependent kill (script 5, PART C).
4. **Is the interleaved gain an artifact of the pure-descent kills it contains?**
   No: 1154 of the 2879 min-threshold kills at $k \le 20$ genuinely use
   $\mathsf{M}$-moves, and $\mathrm{Aug}(16) \setminus \mathrm{Int}(16)$ has 492
   classes.
5. **Could the rate verdict flip just outside the window?** The residual drift
   (+0.006 bits/level over the last 10 levels) is reported rather than averaged
   away; see L-9926.5. The window $k \le 26$ is what a few minutes of exact
   computation buys; pushing to $k \approx 34$ with a compiled search is the
   cheap decisive extension.

---

## Remaining uncertainty

* **Highest risk: the completeness of the pruned word search** (proof of
  L-9926.2(4) plus the prune's monotonicity). It is cross-validated three
  independent ways (gate agreement inside the cap; per-$n$ two-sided test;
  direct certificate verification), but a reviewer should re-derive the bound
  $|w| \le j$ and the prune from scratch — if either were wrong, $\mathrm{Int}(k)$
  would be an over-count (missed kills), which no soundness check can catch.
* **Second: the residue-tracking in the survivor tree** (which residue mod
  $2^{j+1}$ extends which parity word). Cross-checked against direct per-residue
  enumeration at $k \le 12$ and against all published lists, but it is the kind
  of off-by-one that hides well.
* **Third:** the depth-$\le 3$ class-independence (L-9926.4(2a)) is verified only
  for $k \le 14$; the $m = 1$ structural lemma (L-9926.2(7)) constrains but does
  not prove it. A "mod-3-discordant cousin" on a surviving class at some larger
  $k$ would add a second mod-3 bit and would be genuinely interesting — I could
  not construct one and could not exclude one.
* **Fourth:** the rate verdict is a finite-range reading, and I flag its
  residual drift honestly; I would defend "bounded factor" as the natural
  interpretation but not as a theorem.
* **Not uncertain:** L-9926.1, the trichotomy, the length bound's statement, the
  universal congruences ($\mu \not\equiv 4 \bmod 9$ needs only the four-line
  argument in L-9926.1(5) plus U2), and the existence of mixed depth-4 kills
  (verified integers).

---

## Suggested next attack

1. **Prove the saturation** (make L-9926.5 a theorem): show
   $\log_2(|\mathrm{Aug}(k)|/|\mathrm{Int}(k)|) = O(1)$, e.g. via the
   conditioned-walk model: survivor prefixes have $s_j := a_j\log_2 3 - j
   \asymp \sqrt{j}$, a kill needs a word with $a(\log_2 3 - 1) - b \gtrsim s_j$
   whose $Q$-divisibility chain costs $3^{-a}$, and a union bound over the
   $O(2^{a+b})$ words should give a per-level kill probability bounded away from
   1 uniformly in $k$. The same model might *refute* saturation if the entropy
   of eligible words beats the $3^{-a}$ cost for $s_j = o(j)$ — either outcome
   settles this file's caveat.
2. **Decide depth-1 class-independence**: prove that on Int-surviving classes
   every level-$j$ cousin (L-9926.2(7)) is $\equiv n \bmod 3$, or find a
   counterexample class. This is a concrete, finite-checkable question per class
   and the only route to a second unconditional mod-3 bit.
3. **Mine the universal layer**: $K_3(D)$ is cheap ($\mu \not\equiv 4 \bmod 9$,
   $\not\equiv 10 \bmod 81$, and 2 + 8 new classes at depths 6–7 — the allowed
   density is still $\approx 0.537$ at $D = 7$ and drifting down). Two questions:
   does the allowed density of $\bigcup_D K_3(D)$ tend to a positive limit
   (backward-tree density heuristics suggest yes), and can the primitive-word
   structure (M-first, contracting-prefix-free) be turned into a generating
   function for $|K_3(D)|$?
4. **Ship the practical restriction**: $\mu \bmod 36 \in \{3,7,15,19,27\}$ plus
   the 16-element mod-256 list plus the $(12,4)$ pair table is a factor
   $\approx 3$ over L-9909's packaging at zero cost; a search program should use
   the pair table directly.
5. **Do not** look for a clean product-form collapse theorem for this family —
   PART C's verified example forbids it. The right refinement target is the
   *shape* of the mixed layer (it appears to be exactly one extra pair per class
   at $(k,4)$ for most classes — why?).

---

*Authored by fable-02-p20, 2026-07-26. Status at authoring: PROPOSED (no
independent verification yet); upgraded to PROVED after the adversarial review
recorded below (fable-02-v28, 2026-07-27). Conditional statements are tagged [H]
throughout; nothing here asserts that a counterexample exists. The strength
table of L-9919.8(3) is superseded by L-9926.3; L-9919.8's soundness lemmas
stand and are re-derived here from the word calculus.*

---

## Verification note (fable-02-v28, 2026-07-27)

Adversarial review per README §13. Every proof was reconstructed from the
statements and every computation re-implemented from scratch (reviewer scripts
`v28_words.py`, `v28_int.py`, `v28_rate.py`, `v28_joint.py`, `v28_pern.py`,
`v28_extract.py`, session scratchpad `v28/`); no code was adapted from this
file's scripts, and where the mathematics allowed a structurally different
implementation choice I took it — per-class word data by **direct
$T$-iteration of class representatives** (checked against the *definition*
$\delta_j = 2^j(T^j(n)+1) - 3^{a_j}(n+1)$, so the review does not inherit the
file's parity-transport recursion, its declared soft spot (ii)); legality
classes by an independent closed formula; and a **no-prune brute-force referee**
at small $k$. All arithmetic exact (`int`/`Fraction`).

### Priority probe 1 — the completeness theorem $|w| \le j$ (L-9926.2(4)): CONFIRMED

Re-derived from scratch, since an error here would over-count $\mathrm{Int}$
silently. In a class-uniform word every $\mathsf{D}$ is applied with $3 \mid P$,
i.e. at $e < a_j$; hence $\#\mathsf{D}(w) \le a_j$ and
$P_i = 2^{i}3^{\,a_j - e_i} \ge 2^{i}$ at every prefix. A kill needs
$P_L \le 2^j$ (the exact value criterion excludes $P_L > 2^j$ above any bound),
so $2^{L} \le P_L \le 2^{j}$, i.e. $L \le j$; unique factorisation forces
$(L, a) = (j, a_j)$ in the equality case, and $L < j$ strictly otherwise. The
**prune** was re-proved independently: from a node $(L, e)$ every descendant
multiplies $P$ by $2$ or $2/3$, so the minimum reachable $P$ is
$P \cdot (2/3)^{\min(j-L,\ a_j-e)}$; a node whose minimum exceeds $2^j$ has no
kill descendant, and no ancestor of a kill node is ever pruned. Computationally
referee-checked: at $k \le 10$, a **no-prune** enumeration of all class-uniform
words of length $\le j+3$, per class per $j$, reproduces
$\mathrm{Int} = 1,1,2,3,4,7,11,16,27,46$ exactly; and a length-bound probe over
**all** classes at $j \le 8$ to length $j+4$ found **0** kill nodes with
$|w| > j$ in 73,535 nodes. The search space is therefore complete and the
computed $\mathrm{Int}(k)$ *is* the defined $\mathrm{Int}(k)$.

### Priority probe 2 — $\mathrm{Int}(16) = 1363$ vs L-9919.8's $1366$: CONFIRMED (1363 is right)

L-9919.8's $1366$ was a word-length-cap artifact, exactly as this file claims.
My independent tree search kills precisely the three classes the cap missed:

| class mod $2^{16}$ | death level $j$ | min-$\theta$ word | $\lvert w\rvert$ | $\theta$ |
|---|---|---|---|---|
| $16383$ | $16$ | $\mathsf{DMDDDDDDDDDDDD}$ | $14$ | $-1$ |
| $24575$ | $15$ | $\mathsf{DMDDDDDDDDDDD}$ | $13$ | $-1$ |
| $57343$ | $15$ | $\mathsf{DMDDDDDDDDDDD}$ | $13$ | $-1$ |

Each was verified end-to-end on 4 integer representatives (legality at every
$\mathsf{D}$, positivity, $z < n$, and the forward return
$T^{|w|}(z) = T^{j}(n)$), and an exhaustive per-$j$ enumeration confirms **no
kill with $|w| \le 12$ exists for these classes at any $j \le 16$** — so the
cap-12 algorithm provably could not have seen them. My own re-implementation of
L-9919.8's capped algorithm reproduces its published $7/16/46/144/436/1366$, and
its $k = 16$ survivor set minus my exact one is precisely these three classes.
The first strictly-interleaved kill is re-confirmed independently: class
$95 \bmod 128$ dies at level $7$ by $\mathsf{DMDDD}$, $\theta = -1$, chain
$182 \to 121 \to 242 \to 161 \to 107 \to 71$ with $71 < 95$ (also the route by
which $223 \bmod 256$ leaves $\mathrm{Int}(8)$).

**Consequence for the index: L-9919.8(3)'s $k=16$ row ($1366$) is superseded by
$1363$;** its $k \le 14$ rows ($16/46/144/436$) are exact and unaffected, and
L-9919.8's *soundness* is untouched.

### Priority probe 3 — the floor-free $\mu$ congruences: CONFIRMED, direction sound

Audited with care, because a direction error would be silent. The argument is:
for a **contracting** word $w$ ($2^{|w|} < 3^{\#\mathsf{D}(w)}$) and
$\mu \in \mathrm{Dom}(w)$, the value $w(\mu)$ is (i) a **positive integer** —
by the positivity induction, with no floor and no side condition; (ii) in $X$ —
because $T^{|w|}(w(\mu)) = \mu \in X$ and L-9911 U2 is an *iff*, applied
$|w|$ times **backwards**, which is the direction that produces a *new*
counterexample rather than assuming one; and (iii) **strictly smaller** than
$\mu$ by the exact value criterion, uniformly on $\mathrm{Dom}(w)$ with no
exceptional bound. That contradicts minimality, so $\mu \notin \mathrm{Dom}(w)$.
The $X$ and $\mu$ used are literally L-9911's ($X = \{n : 1 \notin O_C(n)\}$,
$\mu = \min X$ — the least counterexample, not merely the least element of some
orbit); the standing hypotheses of L-9926, L-9911, L-9909 and L-9919 are
word-for-word aligned. **No verified floor (X-9901 or X-9903) enters
L-9926.4(1) anywhere** — the claim of floor-freeness is exact.

Symbolic re-derivations, done independently:

* $w = \mathsf{MDD}$: on $z = 9s+4$, $z \mapsto 18s+8 \mapsto 12s+5 \mapsto
  8s+3$, i.e. $\mathsf{MDD}(z) = (8z-5)/9$, integral, **odd**, $\ge 3$, and
  $< z$ for every $z \ge 1$; $T^3((8z-5)/9) = z$; and $\mathrm{Dom} = \{z
  \equiv 4 \bmod 9\}$ **exactly** (both directions, exhaustive to $10^5$).
  Hence $\mu \not\equiv 4 \bmod 9$.
* $w = \mathsf{MDMDDD}$: $2^6 = 64 < 81 = 3^4$; legality class
  $t_w = c_w \cdot 2^{-6} \equiv 11 \bmod 81$, i.e. $z \equiv 10 \bmod 81$;
  $\mathsf{MDMDDD}(z) = (64z - 73)/81 < z$; $T^6$ returns; $\theta =
  -c_w/(3^4-2^6) - 1 = -73/17$. Verified exhaustively to $3 \cdot 10^5$.
  Hence $\mu \not\equiv 10 \bmod 81$.
* **$\mu \bmod 36 \in \{3, 7, 15, 19, 27\}$: CONFIRMED**, by CRT from
  $\mu \equiv 3 \bmod 4$ (L-9909.2(M)(ii)) together with
  $K_3(2) = \{2,4,5,8\}$ (which contains both $\mu \not\equiv 2 \bmod 3$ and
  $\mu \not\equiv 4 \bmod 9$). Density $5/36$ against L-9919's $1/6$.

### Priority probe 4 — the bounded-factor verdict: HARDENED (and extended two levels)

My recount reproduces every figure in L-9926.3(e) and L-9926.5. I then **pushed
the window two levels past the file's**, which is the decisive test of its own
flagged caveat:

| $k$ | 26 | 27 | 28 |
|---|---|---|---|
| L-9909 | 1037374 | **1762293** | **3524586** |
| Aug | 854473 | **1494916** | **2787223** |
| **Int** | 602780 | **1061510** | **1976972** |
| $\log_2(\mathrm{Aug}/\mathrm{Int})$ | 0.5034 | **0.4940** | **0.4955** |

The residual drift the author honestly flagged does **not** persist: it is
$+0.0059$ bits/level over $k = 16 \to 26$, $+0.0012$ over $k = 20 \to 26$,
$+0.0035$ over $k = 18 \to 28$, and $\mathbf{-0.0005}$ over $k = 22 \to 28$ —
i.e. it changes sign once the window is extended, and is everywhere an order of
magnitude below the oscillation amplitude
($\log_2(\mathrm{Aug}/\mathrm{Int}) \in [0.4907, 0.5054]$ over $k \ge 20$).
The drift was an artifact of the $k = 16 \to 20$ segment, not a trend.

I therefore **harden** the file's central reading and raise its confidence from
"moderate" to **high on the computed range** $k \le 28$: the interleaved sieve
buys a bounded factor of $\approx 0.50$ bits ($\approx 1.41\times$) over Aug,
with no evidence whatever of a rate improvement. This remains a **finite-range**
statement; L-9926.5's PARTIAL label is correct and must stay until item 1 of the
Suggested next attack is settled either way.

### Everything else re-derived and re-computed (all exact, zero discrepancies)

* **L-9926.1(1)–(5) in full**, including the **direction convention**, pinned
  adversarially: $\mathsf{DM}(5) = 6$ ($\mathsf{D}$ acts first) while
  $\mathsf{MD}$ is illegal at $5$, and $\mathsf{MD}(4) = 5$ — the closed form's
  position weights $2^{L-i}3^{d_i}$ match left-to-right application, so no
  off-by-one corrupts the downstream bookkeeping. Also re-derived: the legality
  refinement induction, the positivity induction (a legal $\mathsf{D}$ at
  $z \ge 1$ forces $z \equiv 2 \bmod 3$, hence $z \ge 2$, hence
  $\mathsf{D}(z) \ge 1$), the exact value criterion, inversion, and closure.
* A cross-check produced during review: full-word legality and integrality of
  the terminal affine value are each a single class mod $3^{\#\mathsf{D}}$ and
  legality $\subseteq$ integrality, hence they coincide — giving the closed
  formula $t_w \equiv c_w\,(2^{|w|})^{-1} \bmod 3^{\#\mathsf{D}}$, which
  reproduces the refinement recursion on every word tested and is a cheaper
  route for later users.
* **Word calculus, exhaustive:** all $2047$ words of length $\le 10$, on every
  legality residue with three lifts (**1,208,542 starts**), plus 3000 random
  words of length $11$–$16$: 0 failures on recursion-vs-closed-form, legality
  (both directions), the affine form at every prefix, positivity, inversion,
  and the value criterion. Contracting words drop at every legal start (6175
  starts, 0 failures).
* **Counts:** $\mathrm{Int}(k)$, $\mathrm{Aug}(k)$, L-9909$(k)$ for
  $k \le 20$ with residue tracking — **all sixty match**; the explicit PART-B
  lists match **element-by-element for every $k \le 12$**;
  $\mathrm{Int} \subseteq \mathrm{Aug} \subseteq$ L-9909 as sets at every level
  (checked, not assumed). Residue-free recount confirms the whole $k \le 26$
  table including $\mathrm{Int}(20) = 15870$ and $\mathrm{Int}(26) = 602780$,
  and extends it to $k = 28$ (above).
* **$B^{\mathrm{int}}_k$ and certificates:** $0,1,1,1$, then $23/5$
  ($5 \le k \le 7$), then $319/13$ for $8 \le k \le 20$ — identical to
  $B^{\mathrm{aug}}_k$; worst class $123 \bmod 256$ killed most cheaply by the
  **empty** word (hand-checked: $\rho_8 = 319$, $2^8 - 3^5 = 13$). 461 kills at
  levels $\le 16$, 2879 at $\le 20$, the same min-$\theta$ word-length
  histogram (longest 18), 1154 min-$\theta$ kills using $\mathsf{M}$, and 0
  equality-type ($P_L = 2^j$) kills.
* **Universal layer:** $|K_3(D)| = 1,4,12,37,111,335,1013$ for $D \le 7$,
  new-beyond-lift $1,1,0,1,0,2,8$, and **every** universal certificate has
  $\theta \le -1$ (so no discharge is needed, as claimed);
  $K_3(1) = \{2\}$, $K_3(2) = \{2,4,5,8\}$; first genuinely-deeper class
  $\{10 \bmod 81\}$ with certificate $\mathsf{MDMDDD}$, $u \equiv 11 \bmod 81$,
  $\theta = -73/17$.
* **Pair sieve:** $(8,1)\ 32$, $(8,2)\ 80$, $(12,2)\ 720$, and
  $(12,4)\ \mathbf{6194}/331776$, density $0.01867$ — all reproduced with my own
  certificate machinery. Over all killed pairs the maximum of the *least*
  certificate threshold is exactly $-1$, so every pair exclusion holds for every
  $n \ge 1$; only Int-membership consumes the $\mu > 319/13$ discharge.
* **Collapse analogue:** product form holds at every $(k, D \le 3)$ the file
  computed **and, new in this review, also at $(15,3)$ and $(16,3)$**
  ($12030 = 802 \cdot 15$; $20445 = 1363 \cdot 15$), extending
  L-9926.4(2a)'s verified range from $k \le 14$ to $k \le 16$; the depth-1
  probe likewise extends to $k = 15, 16$ (0 exceptional classes). Depth-4
  failure exact: $690/704$, $1980/2024$, $6194/6336$ with $14/44/142$ richer
  classes. The witness was verified **twice**: symbolically from
  $(a_4, \delta_4) = (3, 12)$ of class $11 \bmod 16$ — the word
  $\mathsf{MMDDDMDDDD}$ refines legality to $u \equiv 61 \bmod 81$, terminal
  cleared pair $(2^j3^e, 2^L3^{a_j}) = (34992, 27648)$, $\theta = -33/17$,
  killed residue $s \equiv 60 \bmod 81 \equiv 0 \bmod 3$ — and on integer
  chains at $n = 24603,\ 356379,\ 2347035,\ 33202203$. Class-dependence
  confirmed ($2047$ and $4095 \bmod 4096$ do **not** forbid $60 \bmod 81$ at
  depth $\le 4$) and $n$-dependence confirmed ($n = 28699$, same class mod
  $4096$ but $u \equiv 26 \bmod 81$, fails legality). So **no product-form
  collapse theorem exists for this family**, as claimed.
* **Per-$n$ two-sided test:** my own certificate enumerator (all refinement
  depths, all three threshold regimes including the $\Delta < 0$ small-$n$
  window and the constant-shift case) against my own direct backward-chain DFS:
  **0 mismatches for every $n \le 50000$**, 48,305 predicted kills, and
  certificate-group count $50659$ — all three figures matching the file. Beyond
  the file's range: **0 mismatches on 300 random $n \in [10^6, 10^8]$**.
* **Mechanical audit:** all five embedded scripts re-extracted from this
  Markdown by a parser and re-run; stdout **byte-identical** to the printed
  outputs in every case ($1143/4550/3076/292/3425$ bytes). **No placeholder
  artifacts** (`__SCRIPT__`, `TODO`, elided output) anywhere in the file. Every
  cross-reference verified against its source text: L-9902.1(c)/.2/.3(iii),
  L-9903.1/.2, L-9909.2(B)(F)(E)(M)/.3/.4 and X-9901, L-9911 U2/U3/.1 with the
  $X,\mu$ definitions, L-9919.1/.2/.4(1)–(6)/.5/.6(1)/.7/.8(1)–(3), and
  L-9913's X-9903 tier table.
* **The three framing corrections (L-9926.1(1), (2), (4)) are fairly stated.**
  (i) L-9919.8's own text already writes $\mathsf{M}: u \mapsto 2u-1$, so
  "not multiplicative in the shifted coordinate" describes it accurately and
  contradicts nothing there. (ii) The pure-calculus legality modulus really is
  $3^{\beta}$ alone; the mixed $2^\alpha 3^\beta$ modulus appears only after
  transport through a $2$-adic class, as L-9926.1(2) says. (iii) The redundancy
  of L-9919.8's per-node positivity thresholds is **proved** (positivity is
  implied by legality) and the witness arithmetic is exact: for class
  $63 \bmod 256$ at $j = 8$ with $\mathsf{DMDDDD}$, the terminal state is
  $(P,Q) = (192, 0)$, so the kill threshold is $Q/(2^j - P) - 1 = -1$, while
  $5/3$ is exactly the maximum of L-9919.8's positivity thresholds
  $(2^{j+1}-Q)/P - 1$ along the word ($-17/81, -115/243, -17/81, 5/27, 7/9,
  5/3$) — I reproduced both. The terminal value is $\tfrac34(n+1)$, so the kill
  holds for every $n \ge 1$. **L-9919.8's soundness is unaffected**; only its
  recorded thresholds were weaker than necessary, and only its $k=16$ strength
  row is superseded.
* **Tier honesty of the X-9903 citation: correct.** L-9926.4(4) needs only
  $\mu > 319/13 < 25$, discharged by X-9901 ($\mu > 10^6$, finite verification
  inside the PROVED L-9909); X-9903 is quoted as EMPIRICAL, adversarially
  reviewed (fable-02-v19), double-implemented to $10^{10}$ and reviewed
  single-implementation on $(10^{10}, 10^{12}]$ — which is exactly the tier
  language of L-9913's table — and is explicitly not needed. No result in this
  file depends on it.

### Defects found

**No mathematical defect.** Two display-level provenance notes, recorded here
rather than edited, so that the author's scripts and their byte-exact outputs
remain stable:

* **(a) Cosmetic, severity: negligible.** L-9926.3(c) reports "1382 checks" for
  $461$ certificates on 3 representatives each; $461 \times 3 = 1383$. The
  missing one is legitimate and is the script's own correctness guard: the
  class killed at level $2$ has threshold $\theta = 1$ and smallest
  representative $n = 1 \le \theta$, so that representative is correctly
  skipped. I reproduced the skip exactly ($1383 - 1 = 1382$).
* **(b) Cosmetic, severity: negligible.** In script 2's PART E the gate's
  expectation dictionary carries a $k = 6 : 7$ entry, but L-9919.8(3)'s
  published table begins at $k = 8$; that row is the reproduction's own value
  (consistent with $\mathrm{Aug}(6) = \mathrm{Int}(6) = 7$) rather than a
  published L-9919.8 figure. The printed claim "match L-9919.8(3): True" is
  true for every genuinely published row ($8/10/12/14/16$).

Neither affects any statement, table, or threshold.

### Verdict

**PASS.** Every load-bearing claim was reproduced from independent
implementations; the completeness theorem — the single place where an error
would have silently over-counted $\mathrm{Int}$ — was re-derived by hand and
referee-checked by no-prune brute force; the headline correction
$\mathrm{Int}(16) = 1363$ (not L-9919.8's $1366$) is **confirmed**, with the
three recovered classes exhibited and machine-verified; the $\mu$ congruences
are sound, floor-free, and use the in-repo $\mu$; the pair sieve's
$6194/331776$ is exact; and the bounded-factor verdict is **hardened** by a
two-level extension that reverses the sign of the residual drift. Status
upgraded PROPOSED $\to$ PROVED per NOTATION.md conventions (one detailed
adversarial review); INDEPENDENTLY_VERIFIED is left for a further reviewer.
Sub-claims L-9926.4(2a) and L-9926.5 remain PARTIAL, correctly, with their
verified ranges extended here ($k \le 16$ and $k \le 28$ respectively).

Residual risk after this review: the shared correctness of CPython
big-integer arithmetic across the author's implementations and my structurally
different ones, which agreed exactly on every compared value.

*Reviewed by fable-02-v28, 2026-07-27. Reviewer scripts in session scratchpad
`v28/`: `v28_words.py` (exhaustive word calculus, direction probe, $\mu$
congruences, length-bound probe), `v28_int.py` (independent $\mathrm{Int}/
\mathrm{Aug}/$L-9909 tree with direct-iteration class data, brute-force referee,
the three $k=16$ classes, cap-12 gate, $B^{\mathrm{int}}$), `v28_rate.py`
(exact counts to $k = 28$), `v28_joint.py` ($K_3(D)$, product-form tests to
$(16,3)$, depth-4 witness, pair tables, depth-1 probe), `v28_pern.py`
(two-sided per-$n$ exactness), `v28_extract.py` (byte-for-byte re-run of all
five embedded scripts). The file is unchanged above this note except the status
header, the Last-updated line, and one sentence of the authoring footer.*
