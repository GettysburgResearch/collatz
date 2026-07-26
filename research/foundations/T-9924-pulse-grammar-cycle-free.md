# T-9924 — Pulse-grammar block macros: exact cycle-freeness for every repetition word over the fixed-weight $(a,b)$ alphabets, $a \le 5$

```text
Claim ID:      T-9924
Title:         Pulse-grammar block macros: exact all-repetition cycle-freeness for the
               infinite family of fixed-weight (a,b) Collatz block grammars, a <= 5
Status:        PROVED
Authoring agent:   fable-02-p18
Reviewing agents:  fable-02-v26 (adversarial review 2026-07-26: PASS)
Created:       2026-07-26
Last updated:  2026-07-26 (status upgraded after independent adversarial review;
               see Verification note at end of file)
Dependencies:  NOTATION.md (D-9901, D-9902, D-9904, D-9905, D-9907, D-9908);
               L-9916.1-.2 (PROVED) and X-9902 (EMPIRICAL) are used ONLY in the
               cross-reference results T-9924.8C1/C2 and in the Step-6 positioning,
               never in the main theorem; L-9923 (landed 2026-07-26, PROPOSED,
               independent verification in progress -- see note below) is cited for
               the three general lemmas, all re-proved inline here (T-9924.3,
               T-9924.4, and the sign argument in Step 4(vi)) so that this file
               stands alone.
Scope:         All integers; the two specific affine blocks A, B defined below; all
               finite words over the complete fixed-weight (a,b) macro alphabets with
               b >= 1 and 0 <= a <= 5 (plus the supercritical remark covering b = 0 and
               general Q < P); arbitrary word length, arbitrary branch order at every
               macro, arbitrary repetition.  Physical statements concern the shortcut
               map T (D-9902) on positive integers.  NOT covered: contracting packets
               with a >= 6, dynamics not expressible in the {A,B} letter grammar, and
               the six-branch least-root decision (issue #58).  See the Honest scope box.
Related counterexample candidates: none (no K-#### candidate is created by this file)
```

**Provenance.** This file is the 99xx foundations packet's *independent reconstruction*
of a theorem drafted in an external, unpushed working session supplied by the
repository owner (draft ID "T-9608", intended for the PR #47 program, alongside that
program's L-9607 on aligned Christoffel mixtures). The draft was treated as a *spec
whose numbers had never been independently verified*: every object, formula, table and
packet closure below is re-derived from scratch and adversarially tested here, and this
file's derivations are the authority. **Outcome: every numerical claim of the source
spec verified exactly; no numbers required correction.** One toolkit-level item was
superseded rather than corrected — the spec's collapse threshold $W < Q$ is true but
not sharp; see the Companion-file note and the Verification-summary table. Additions
that go beyond the spec are explicitly flagged as additions. Credit
for the discovery of the statement and the proof route belongs to the source session;
responsibility for correctness of everything below rests with this file.

**Companion-file note (honest citation).** The general lemmas used here — the
narrow-alphabet collapse, the cycle-minimum sieve, and the supercritical sign
obstruction — were being written concurrently by agent fable-02-p17 and landed as
`research/foundations/L-9923-affine-cycle-collapse.md` **during the drafting of this
file** (status at time of writing: **PROPOSED, independent verification in
progress**). Citations below use that file's final numbering: **L-9923.1/.1C/.1S**
(collapse; sharp threshold $W < P + Q$), **L-9923.2** (2a–2c: minimum-edge law,
$g$-refinement, gate, survivors — with *no sign hypothesis on the constants*),
**L-9923.3(ii)** (supercritical sign obstruction, under $C_i \ge 0$). All three are
**re-proved inline in full** (T-9924.3, T-9924.4, Step 4(vi)), so no statement in
this file depends on L-9923's status. Notably, L-9923 *corrected the source spec's
toolkit*: the collapse threshold $W < Q$ is true but not sharp — the sharp threshold
is $W < P + Q$, and the source's claimed $W = Q$ sharpness example is impossible for
$P \ge 1$. The inline proof of T-9924.3 below re-derives the sharp version
independently (the span-bound argument), and the improvement has a real consequence
here: **packet $(4,2)$ now closes by collapse as well** (Step 4(iii)).

---

## Statement

Throughout, $T$ is the shortcut map (D-9902) and $S$ the Syracuse map (D-9904);
$\nu_2$ is the 2-adic valuation; empty sums are $0$, empty products are $1$
(NOTATION.md). All arithmetic is exact integer arithmetic.

### D-9924.1 (the two blocks; three coordinate systems)

Two affine **blocks** are given in an auxiliary integer coordinate $h$, with
**physical coordinate** $n = 2h - 5$ (so $h = (n+5)/2$, and $h \in \mathbb{Z}
\iff n$ odd) and **centered coordinate** $y = h - 3$ (so $n = 2y + 1$, and
$y \ge 0 \iff n \ge 1$):

$$\mathsf{A}:\; 8h' = 9h, \qquad \mathsf{B}:\; 16h' = 9h + 21 ;$$
$$\text{physically}\quad \mathsf{A}:\; n' = \frac{9n+5}{8}, \qquad
\mathsf{B}:\; n' = \frac{9n+7}{16};$$
$$\text{centered}\quad \mathsf{A}:\; 8y' = 9y + 3, \qquad \mathsf{B}:\; 16y' = 9y .$$

A **word** $w = \ell_1\ell_2\cdots\ell_k \in \{\mathsf{A},\mathsf{B}\}^k$ ($k \ge 1$)
is applied $\ell_1$ first. Its **weight** is $(a,b) = (\#\mathsf{A}, \#\mathsf{B})$,
$k = a + b$. Write $(q_\mathsf{A}, c_\mathsf{A}) = (8,3)$,
$(q_\mathsf{B}, c_\mathsf{B}) = (16,0)$, so each letter acts on $y$ by
$q_\ell\, y' = 9y + c_\ell$. The name *pulse grammar*: in centered coordinates
$\mathsf{A}$ injects the pulse $+3$ and $\mathsf{B}$ is pure $9/16$ decay.

### D-9924.2 (macros, packets, integral cycles)

For a word $w$ of weight $(a,b)$ define (T-9924.2 proves the composite has this form)
$$Q := Q_{a,b} := 8^a 16^b, \qquad P := P_{a+b} := 9^{a+b}, \qquad
Q\, y_k = P\, y_0 + E_w \quad (E_w \in \mathbb{Z}_{\ge 0}),$$
$$D := Q - P, \qquad
\mathcal{E}_{a,b} := \{ E_w : w \text{ of weight } (a,b) \}
\quad (\text{the \textbf{complete macro alphabet}: all } \tbinom{a+b}{b} \text{ branch orders}),$$
$$E_{\min} := \min \mathcal{E}_{a,b}, \quad E_{\max} := \max \mathcal{E}_{a,b}, \quad
W := E_{\max} - E_{\min}.$$
The **packet** $(a,b)$ is the nondeterministic affine system on $\mathbb{Z}$ whose one
step from $y$ is $y \mapsto (Py + E)/Q$ for **any** $E \in \mathcal{E}_{a,b}$ making the
quotient an integer. An **integral cycle** of length $R \ge 1$ is a pair of sequences
$(w_t)_{t=0}^{R-1}$ (weight-$(a,b)$ words, arbitrary and independent — different branch
orders may be mixed freely) and $(y_t)_{t=0}^{R-1} \in \mathbb{Z}^R$ with
$$Q\, y_{t+1 \bmod R} = P\, y_t + E_{w_t} \qquad (0 \le t < R).$$
No least-period or distinctness assumption is made. The packet is **contracting** if
$Q > P$ and **supercritical** if $Q < P$ ($Q = P$ is impossible: a nontrivial power of
$2$ never equals a power of $9$).

### The sub-claims

* **T-9924.1 (chart validity).** (a) The displayed $n$- and $y$-forms are exactly
  equivalent to the $h$-forms. (b) $\mathsf{A}$ is the exact composite of two Syracuse
  steps (D-9904) with exponents $(1,2)$ — equivalently three $T$-steps with parity word
  $(1,1,0)$ — and it is a legal Collatz composite at the odd $n \ge 1$ **exactly** when
  $n \equiv 11 \pmod{16}$; $\mathsf{B}$ is the exact composite of two Syracuse steps
  with exponents $(2,2)$ — four $T$-steps, parity word $(1,0,1,0)$ — legal **exactly**
  when $n \equiv 1 \pmod{32}$. Outputs of legal blocks are automatically odd and
  $\ge 1$. (c) *Legality $=$ integrality*: for $h \in \mathbb{Z}$, $9h/8 \in
  \mathbb{Z} \iff 8 \mid h \iff n \equiv 11 \pmod{16}$, and $(9h+21)/16 \in \mathbb{Z}
  \iff h \equiv 3 \pmod{16} \iff n \equiv 1 \pmod{32}$; in $y$: $\mathsf{A}$ integral
  $\iff y \equiv 5 \pmod 8$, $\mathsf{B}$ integral $\iff y \equiv 0 \pmod{16}$. Hence a
  word applies as a legal $T$-composite at odd $n \ge 1$ iff its centered orbit from
  $y = (n-1)/2$ stays integral, and the values agree. (d) *Unit-slope lift*: for every
  word $w$, the single top-level congruence $Q \mid P y_0 + E_w$ already forces the
  integrality of **all** intermediate letter states; consequently the set of legal
  starting states of $w$ is exactly one residue class mod $Q$ (intersected with
  $y \ge 0$ for physicality). (e) *Reduction logic, made explicit*: any Collatz cycle
  realized by legal blocks yields an integral cycle of the unrestricted affine system
  with all $y_t \ge 0$; the theorems below refute the latter, which is **stronger**
  than needed — legality restrictions only shrink the set of realizable cycles. By
  (c)–(d) nothing is in fact lost: on $y \ge 0$, integrality and legality coincide.
* **T-9924.2 (fixed-weight macro algebra).** For every word of weight $(a,b)$,
  $Q = 8^a16^b$ and $P = 9^{a+b}$ **independent of order**, while
  $$E_w = 3 \sum_{j:\ \ell_j = \mathsf{A}} 9^{\,k-j} \prod_{i<j} q_{\ell_i}$$
  depends on the order. Swapping an adjacent $\mathsf{AB}$ (positions $j, j{+}1$) to
  $\mathsf{BA}$ changes $E$ by $+21 \cdot 9^{\,k-j-1} \prod_{i<j} q_{\ell_i} > 0$.
  Consequently, for $a \ge 1$:
  $$E_{\min} = 3 \cdot 9^b (9^a - 8^a) \ \text{(attained \textbf{only} by } \mathsf{A}^a\mathsf{B}^b\text{)}, \qquad
  E_{\max} = 3 \cdot 16^b (9^a - 8^a) \ \text{(only by } \mathsf{B}^b\mathsf{A}^a\text{)},$$
  ($(a,b) = (1,1)$: $\mathcal{E} = \{27, 48\}$); moreover $3 \mid E_w$ always,
  $E_w > 0$ for $a \ge 1$, $E_w = 0$ for $a = 0$, and:
  (mod 21) all $E_w$ of one packet are congruent mod $21$, hence
  $E_w \equiv 3 \cdot 2^b(2^a - 1) \pmod 7$;
  (mod 9) $E_w \equiv 3(-1)^{a-1}$ if $\ell_k = \mathsf{A}$, and $27 \mid E_w$ if
  $\ell_k = \mathsf{B}$;
  (mod 8) $E_w \equiv 3$ if $\ell_1 = \mathsf{A}$, and $8 \mid E_w$ if
  $\ell_1 = \mathsf{B}$.
* **T-9924.3 (narrow-alphabet collapse at the sharp threshold; $=$
  L-9923.1/.1C/.1S re-proved).** Let $Q > P \ge 1$, let $\mathcal{C} \subset
  \mathbb{Z}$ be finite nonempty with $W := \max\mathcal{C} - \min\mathcal{C} <
  P + Q$, $D := Q - P$. Then **every** integral cycle of the system
  $Qy_{t+1} = Py_t + C_t$ ($C_t \in \mathcal{C}$) is a one-block fixed point:
  $y_t \equiv y^*$ and $C_t = D y^*$ for all $t$ — in particular a single constant
  is used and $D$ divides it. The threshold is **sharp**: at $W = P + Q$ the
  alphabet $\{Q, -P\}$ carries the moving 2-cycle $0 \leftrightarrow 1$ (the test
  instance $Q = 3, P = 2, \mathcal{C} = \{0,5\}$, cycle $3 \to 2 \to 3$, is this
  witness shifted by $+2$). *(Provenance note: the source spec stated the weaker
  threshold $W < Q$ — true, and sufficient for packets $(3,1)$, $(4,1)$ — with a
  sharpness claim at $W = Q$ that is impossible for $P \ge 1$; the sharp form
  $W < P+Q$ is L-9923's correction, re-derived independently below, and is what
  closes packet $(4,2)$ by collapse.)*
* **T-9924.4 (automatic positivity and the cycle-minimum sieve; $=$ L-9923.2
  re-proved).** Let $Q > P \ge 1$, $D = Q - P$, and let all constants be **positive**
  (L-9923.2 needs no sign hypothesis on the constants — positivity of the *cycle* is
  its hypothesis; here positive constants *supply* that hypothesis via (a), so all
  integral cycles are covered).
  Then: (a) every integral cycle is confined to
  $\lceil E_{\min}/D \rceil \le y_t \le \lfloor E_{\max}/D \rfloor$; in particular
  $y_t \ge 1$ (there are no zero, negative, or mixed-sign cycles). (b) The constant
  applied at a cycle minimum $\mu$ satisfies $E = D\mu + Q\kappa$ with
  $\kappa \ge 0$. (c) If also $g \ge 2$, $g \mid P$, $\gcd(g, Q) = 1$, and
  $g \mid E$ for every constant, then $g \mid (\mu + \kappa)$, so $\mu + \kappa \ge g$
  and $E \ge D(\mu+\kappa) \ge gD$. (d) **Gate:** $E_{\max} < gD$ excludes all integral
  cycles. (e) **Targets:** in general every integral cycle forces
  $\mathcal{E} \cap \mathcal{T} \ne \emptyset$, where
  $\mathcal{T} := \{Dm + Qk \le E_{\max} : m \ge 1,\, k \ge 0,\, g \mid m+k\}$ is
  finite and enumerable.
* **T-9924.5 (the main gate; exact row structure).** For $a \ge 1$ take $g = 3$
  (legitimately: $3 \mid P$, $\gcd(3, Q) = 1$, $3 \mid E_w$). The gate
  $E_{\max} < 3D$ is equivalent to
  $$G(a,b):\qquad 9^a\,(16^b + 9^b) \;<\; 2 \cdot 8^a \cdot 16^b,$$
  and $G(a,b)$ automatically implies $Q > P$. $G$ is monotone in $b$
  ($G(a,b) \Rightarrow G(a,b{+}1)$), fails for **all** $b$ when $a \ge 6$ (because
  $9^6 > 2\cdot 8^6$, the same integers as $3^{12} > 2^{19}$), and holds exactly on the
  rows
  $$a \in \{1,2\},\ b \ge 1; \qquad a = 3,\ b \ge 2; \qquad a = 4,\ b \ge 3; \qquad
  a = 5,\ b \ge 4 .$$
  The exceptional pairs with $1 \le a \le 5$, $b \ge 1$ are exactly
  $(3,1), (4,1), (4,2), (5,1), (5,2), (5,3)$, of which $(5,1)$ is supercritical and
  the other five contracting.
* **T-9924.6 (the six exceptional packets, each closed exactly).**
  $(3,1)$: $D = 1631 = 7 \cdot 233$, $W = 3\cdot 7\cdot(9^3{-}8^3) = 4557 < Q = 8192$,
  and none of the $4$ constants is divisible by $D$ — no integral cycle.
  $(4,1)$: $D = 6487 = 13 \cdot 499$, $W = 51765 < Q = 65536$, none of the $5$
  constants divisible by $D$ — no integral cycle.
  $(4,2)$: $Q = 1048576 < W = 1294125 < P + Q = 1580017$, so the **sharp** collapse
  threshold applies (the spec's $W < Q$ does not): any cycle is a fixed point with
  $D \mid E$; the only multiples of $D = 517135$ in $[E_{\min}, E_{\max}]$ are
  $2D, 3D \equiv 6, 2 \pmod 7$ while all $15$ constants are $\equiv 5 \pmod 7$ —
  no integral cycle. Independent second closure (the source's route): the sieve
  target set is $\mathcal{T} = \{3D\} = \{1551405\}$, again $\equiv 2 \ne 5
  \pmod 7$.
  $(5,2)$: $W = 13797525 > P + Q = 13171577$ (collapse genuinely inapplicable even
  at the sharp threshold, excess $625948$); the sieve gives
  $\mathcal{T} = \{3D, 2D{+}Q\} = \{10816917, 15599886\}$, both
  $\equiv 6 \pmod 9$, while every one of the $21$ constants is $\equiv 0$ or
  $3 \pmod 9$ — no integral cycle.
  $(5,3)$: $W = 265464381 > P + Q = 177264449$ (excess $88199932$; sieve needed);
  $\mathcal{T} = \{3D, 2D{+}Q\} = \{273513021, 316559742\}$,
  $\equiv 5, 6 \pmod 8$, while every one of the $56$ constants is $\equiv 0$ or
  $3 \pmod 8$ — no integral cycle.
  $(5,1)$: $Q = 2^{19} = 524288 < 531441 = 3^{12} = P$ (supercritical); by sign, no
  integral cycle contains a state $y_t \ge 0$, and any forward-integral path from
  $y_0 > 0$ diverges. $a = 0$ (all-$\mathsf{B}$): the unique integral cycle is
  $y \equiv 0$, i.e. $h = 3$, $n = 1$.
* **T-9924.7 (MAIN THEOREM).** *For every $b \ge 1$ and $0 \le a \le 5$, no finite
  word over the complete fixed-weight $(a,b)$ macro alphabet — arbitrary length
  $R \ge 1$, arbitrary branch order at each macro (orders may differ from macro to
  macro), arbitrary repetition — has a nontrivial positive integral cycle. Precisely,
  in the notation of D-9924.2: for $1 \le a \le 5$, $(a,b) \ne (5,1)$, there is no
  integral cycle at all (any sign); for $(a,b) = (5,1)$ every integral cycle, if any,
  has all $y_t < 0$; for $a = 0$ the unique cycle is $y \equiv 0$. The sole cycle
  meeting the physical domain $y \ge 0$ ($\iff n = 2y+1 \ge 1$) in the entire family
  is the all-$\mathsf{B}$ fixed point $y = 0$, $h = 3$, $n = 1$.*
  **Corollary 1 (physical form).** If legal blocks applied at an odd $n_0 \ge 1$ form
  a concatenation of complete weight-$(a,b)$ macros ($0 \le a \le 5$, $b \ge 1$)
  returning to $n_0$, then $a = 0$ and $n_0 = 1$: the trivial cycle (D-9905).
  **Corollary 2 (letter-level closure — an addition beyond the source spec).** Any
  integral cycle of the letter system other than the all-$\mathsf{B}$ fixed point
  $y = 0$, with per-period letter counts $(\alpha, \beta)$ and **some** state
  $y_t \ge 0$, must have $\beta \ge 1$, $\alpha \ge 6$, and $8^\alpha 16^\beta >
  9^{\alpha+\beta}$; every other $(\alpha,\beta)$ — including all mixed
  concatenations of complete macros of different covered weights, via their
  per-period totals — is cycle-free on $y \ge 0$.
* **T-9924.8 (the $(5,1)$ packet IS the six-branch chart).** Let $\mathcal{C}(x) =
  \lceil Px/Q \rceil$, digits $\mathrm{a}(x) = Q\,\mathcal{C}(x) - Px$, and alphabet
  $A = \{\alpha_i = 7 \cdot 3^{2i} 2^{15-3i} : i = 0..5\}$ be the six-branch chart of
  L-9916 (D-9916.1–.2) and X-9902, with the same $P = 3^{12}$, $Q = 2^{19}$. Then
  under $y = 3(x-1)$ — equivalently $h = 3x$, $n = 6x - 5$ — the $(5,1)$ macro system
  is **exactly** the chart restricted to digits in $A$: the six branch constants are
  $$E = 3\,(\alpha_i + 7153) = 21 \cdot 9^{\,i}\, 8^{\,5-i} + 21459
  \qquad (\alpha_i \leftrightarrow \mathsf{B} \text{ in position } p = 6 - i),$$
  pairwise distinct mod $Q$ (so at each state at most one branch is integral — the
  grammar is deterministic, like the chart), and one macro step at $y = 3(x-1)$ is
  integral iff $\mathrm{a}(x) \in A$, in which case $y' = 3(\mathcal{C}(x) - 1)$.
  Integral $(5,1)$-cycles correspond to chart cycles with all digits in $A$, and
  all-time forward-integral $(5,1)$-paths to $\bigcap_N S_N$ (D-9916.3).
  **C1 (PROVED cross-ref).** By L-9916.2.3 — or directly, $y_{t+1} > (P/Q)\,y_t$ —
  any all-time path from a physical state diverges.
  **C2 (EMPIRICAL cross-ref).** By X-9902 (reviewer-extended), any all-time root
  satisfies $x > m_{16} \approx 4.63\times10^{78}$, hence physically
  $n = 6x - 5 > 6\,m_{16} - 5 > 2.77\times10^{79}$.

### Honest scope box

> **This theorem is strictly weaker than the Collatz conjecture.** It excludes
> *cycles realizable inside this grammar*, nothing more. Outside its scope:
> (i) contracting packets with $a \ge 6$ — the first open packet is $(6,2)$ — where
> the gate fails and neither inline lemma applies as instantiated;
> (ii) dynamics not expressible as $\{\mathsf{A},\mathsf{B}\}$ letter words at all:
> unrestricted valuation words, other block pairs, and the source program's
> scale-varying summaries and nonaligned repairs (note: mixtures of *complete* macros
> of different covered weights ARE covered, via Corollary 2's per-period totals; what
> is not covered is anything leaving the two-letter grammar or landing on per-period
> totals with $\alpha \ge 6$ in the contracting regime);
> (iii) the six-branch least-root decision — the $m_N$ dichotomy of issue #58 — which
> this file positions but does not touch;
> (iv) entirely negative cycles in supercritical packets (they correspond to
> $3x{-}1$-type dynamics, not to positive Collatz states).
> No K-#### candidate is created. The complementary result in the source program is
> PR #47's L-9607 (aligned Christoffel mixtures), external to this repository.

### Verification summary (source spec vs. this file)

| Source-spec claim | Verdict here |
|---|---|
| Block forms $(9n{+}5)/8$, $(9n{+}7)/16$; exponents $(1,2)$, $(2,2)$ | **VERIFIED** (T-9924.1a–b) |
| Legality residues "mod 16 and mod 32" | **VERIFIED & PINNED**: $n \equiv 11 \ (16)$ for $\mathsf{A}$, $n \equiv 1\ (32)$ for $\mathsf{B}$ |
| Centering $8y' = 9y{+}3$, $16y' = 9y$; all-$\mathsf{B}$ fixed point $(h,n) = (3,1)$ | **VERIFIED** |
| $(Q,P)$ order-independence; $E_{\min}, E_{\max}$ formulas; $(1,1)$: $\{27,48\}$ | **VERIFIED** (+ uniqueness of extremal orders added) |
| Gate $9^a(16^b{+}9^b) < 2\cdot8^a16^b$; rows $a{\in}\{1,2\}$ all $b$; $(3,b{\ge}2)$; $(4,b{\ge}3)$; $(5,b{\ge}4)$ | **VERIFIED EXACTLY** (T-9924.5; monotonicity + boundary failures proved) |
| $(3,1)$: $D = 1631 = 7\cdot233$; $W = 3(16{-}9)(9^3{-}8^3)$; $W < Q$; no $D \mid E$ | **VERIFIED** ($W = 4557$) |
| $(4,1)$: $D = 6487 = 13\cdot499$; same route | **VERIFIED** |
| $(4,2)$: only target $3D$; all 15 constants $\equiv 5$, $3D \equiv 2 \pmod 7$ | **VERIFIED** (and $(4,2)$ *additionally* closes by collapse under the sharp threshold — see next row) |
| (toolkit) collapse threshold $W < Q$ | **TRUE BUT NOT SHARP — SUPERSEDED**: the sharp threshold is $W < P + Q$ (L-9923.1S; re-derived inline as T-9924.3); the spec's $W = Q$ sharpness example is impossible for $P \ge 1$. Consequence verified here: $Q < W_{(4,2)} = 1294125 < P+Q$, so $(4,2)$ closes by collapse as primary route; $W_{(5,2)}, W_{(5,3)}$ exceed even $P + Q$, so the sieve remains genuinely necessary there |
| $(5,2)$: two targets, both $\equiv 6 \pmod 9$; constants $\equiv 0, 3 \pmod 9$ | **VERIFIED** |
| $(5,3)$: two targets $\equiv 5, 6 \pmod 8$; constants $\equiv 0, 3 \pmod 8$ | **VERIFIED** |
| $(5,1)$: $Q < P$; positive cycles die by sign; all-time positivity $\Rightarrow$ divergence | **VERIFIED** (+ exact chart conjugacy $y = 3(x{-}1)$, $E = 3(\alpha{+}7153)$ established) |

**No numerical claim of the source spec required correction** — the gate table, both
extrema, all six packet closures, and every packet constant verified exactly. One
*toolkit-level* item was superseded rather than corrected: the spec's collapse
threshold $W < Q$ is true but not sharp (its $W = Q$ sharpness claim was impossible);
the sharp threshold $W < P + Q$ (L-9923's correction, re-derived here) strictly
extends the collapse regime and upgrades $(4,2)$ to a collapse-closed packet, with the
spec's sieve route retained as an independent second closure. Additions beyond the
spec, all flagged in situ: automatic positivity upgrading every contracting closure
from "no positive cycle" to "no integral cycle of any sign" (T-9924.4a); exact
legality classes and legality$\,=\,$integrality (T-9924.1c–d); the letter-level
Corollary 2; the supercritical sign closure for arbitrary $(a,b)$ with $Q < P$
including $b = 0$; the exact $(5,1)\leftrightarrow$chart dictionary with the physical
anchor $n = 6x-5$; and the pairwise-distinctness mod $Q$ of the $(5,1)$ constants
(determinism).

---

## Definitions

All notation of D-9924.1–.2 above, plus:

- **Legal application.** Block $\mathsf{A}$ *applies legally* at $n$ if $n \ge 1$ is
  odd, $\nu_2(3n+1) = 1$, and $\nu_2(3n_1+1) = 2$ for $n_1 = (3n+1)/2$; then its value
  is $S^2$ restricted to those exponents, $= (9n+5)/8$. Block $\mathsf{B}$ applies
  legally at $n$ if $n \ge 1$ is odd, $\nu_2(3n+1) = 2$, and $\nu_2(3n_1+1) = 2$ for
  $n_1 = (3n+1)/4$; value $(9n+7)/16$. A word applies legally if each successive
  letter does.
- **$Q_{<j}$** $:= \prod_{i<j} q_{\ell_i}$ (prefix product; $Q_{<1} = 1$).
- **Anchoring.** As in L-9905: an integral cycle may be re-indexed to start at any
  $t_0$; all hypotheses are rotation-invariant, so every claim may be proved at a
  convenient anchor.
- **Confinement interval** of a contracting packet:
  $I_{a,b} := [\lceil E_{\min}/D\rceil, \lfloor E_{\max}/D \rfloor]$.
- $m_N$, $S_N$, $\mathrm{a}(x)$, $A$: the six-branch chart objects of
  L-9916 (D-9916.1–.3) and X-9902.

## Motivation

The project constructs and stress-tests counterexample architectures (D-9909). A
counterexample is a nontrivial cycle or a divergent/bounded-nonreturning orbit. This
file closes the **cycle half exactly** for an infinite two-parameter family of block
grammars built from the two smallest "physical" Collatz macro-blocks, with *all*
branch orders and repetitions allowed — the natural cycle-side complement to the
six-branch escape work (issue #58, L-9916, X-9902):

1. Every macro word here is an *exact* composite of shortcut-map steps on its legality
   class (T-9924.1), so the theorem genuinely excludes Collatz cycles of a definite
   infinite family of shapes — not merely cycles of a model system.
2. The $(5,1)$ packet **is** the six-branch chart (T-9924.8): the same $P/Q =
   3^{12}/2^{19}$, the same six digits after an explicit affine dictionary. The
   family therefore *explains the chart's position*: within its row $b = 1$ it is the
   first supercritical packet, where cycles die by sign and only the extraction
   question (the $m_N$ dichotomy) remains — i.e. exactly the frontier where the
   counterexample program must switch from cycle-hunting to divergence-hunting.
3. The macro cycle equation $(Q^R - P^R)y_0 = \sum_t P^{R-1-t}Q^t E_t$ is the block
   analogue of the master cycle equation L-9905.1; the collapse/sieve pair
   (T-9924.3/.4) is a reusable template for other block grammars (cf. L-9922's
   portability program).

## Proof

### Step 0 — chart validity (T-9924.1)

**(a) Coordinate translations.** With $n = 2h - 5$, i.e. $h = (n+5)/2$:
$\mathsf{A}$: $n' = 2h' - 5 = \tfrac{9h}{4} - 5 = \tfrac{9(n+5) - 40}{8} =
\tfrac{9n+5}{8}$. $\mathsf{B}$: $n' = 2\cdot\tfrac{9h+21}{16} - 5 =
\tfrac{9(n+5)/2 + 21 - 40/… }{8}$ — computed cleanly:
$16h' = 9h + 21$ gives $8(n'+5) = \tfrac{9(n+5)}{2} + 21$, so
$16(n'+5) = 9(n+5) + 42 = 9n + 87$, so $16n' = 9n + 7$. With $y = h - 3$:
$\mathsf{A}$: $8(y'+3) = 9(y+3) \iff 8y' = 9y + 3$; $\mathsf{B}$:
$16(y'+3) = 9(y+3) + 21 = 9y + 48 \iff 16y' = 9y$. And $n = 2h - 5 = 2(y+3) - 5 =
2y + 1$. The all-$\mathsf{B}$ fixed point $y = 0$ is $h = 3$, $n = 1$. **(Step 1 of
the commission is subsumed here.)**

**(b) Blocks as exact $T$-composites.** For odd $n$ with $\nu_2(3n+1) = 1$:
$T(n) = (3n+1)/2 =: n_1$ is odd; if moreover $\nu_2(3n_1+1) = 2$ then
$T(n_1) = (3n_1+1)/2$ is even and $T^2(n_1) = (3n_1+1)/4$ is odd; so three $T$-steps
with parity word $(1,1,0)$ compute
$$\frac{3\cdot\frac{3n+1}{2} + 1}{4} = \frac{\frac{9n+5}{2}}{4} = \frac{9n+5}{8},$$
which is Syracuse exponents $(1,2)$ — exactly block $\mathsf{A}$. For odd $n$ with
$\nu_2(3n+1) = 2$: $T(n)$ even, $T^2(n) = (3n+1)/4 =: n_1$ odd; if
$\nu_2(3n_1+1) = 2$, two more $T$-steps give
$$\frac{3\cdot\frac{3n+1}{4} + 1}{4} = \frac{\frac{9n+7}{4}}{4} = \frac{9n+7}{16},$$
parity word $(1,0,1,0)$, Syracuse exponents $(2,2)$ — block $\mathsf{B}$. A weight-
$(a,b)$ word therefore spans $3a + 4b$ $T$-steps of which $2(a+b)$ are odd steps,
consistent with $P/Q = 3^{2(a+b)}/2^{3a+4b} = 9^{a+b}/(8^a16^b)$.

**Exact legality classes.** $\nu_2(3n+1) = 1 \iff 3n + 1 \equiv 2 \pmod 4 \iff n
\equiv 3 \pmod 4$. Writing $n = 4m + 3$: $n_1 = 6m + 5$ and $3n_1 + 1 = 2(9m + 8)$,
so $\nu_2(3n_1+1) = 2 \iff 9m + 8 \equiv 2 \pmod 4 \iff m \equiv 2 \pmod 4 \iff n
\equiv 11 \pmod{16}$: **$\mathsf{A}$ legal $\iff n \equiv 11 \pmod{16}$** (a mod-16
condition). $\nu_2(3n+1) = 2 \iff 3n+1 \equiv 4 \pmod 8 \iff n \equiv 1 \pmod 8$.
Writing $n = 8m + 1$: $n_1 = 6m + 1$ and $3n_1 + 1 = 2(9m+2)$, so the second
condition is $9m + 2 \equiv 2 \pmod 4 \iff 4 \mid m \iff n \equiv 1 \pmod{32}$:
**$\mathsf{B}$ legal $\iff n \equiv 1 \pmod{32}$** (a mod-32 condition). Outputs:
$n = 16s + 11 \mapsto (9n+5)/8 = 18s + 13$ (odd, $\ge 13$); $n = 32s + 1 \mapsto
(9n+7)/16 = 18s + 1$ (odd, $\ge 1$). The two legality classes are disjoint
($11 \not\equiv 1 \bmod 16$), so at each odd $n$ at most one letter applies: the
letter grammar is deterministic — as it must be, since blocks merely package the
$T$-orbit's own valuations.

**(c) Legality $=$ integrality.** $9h/8 \in \mathbb{Z} \iff 8 \mid h$ (as
$\gcd(9,8) = 1$), and $8 \mid h \iff n = 2h - 5 \equiv -5 \equiv 11 \pmod{16}$.
$(9h+21)/16 \in \mathbb{Z} \iff 9h \equiv -21 \equiv 11 \pmod{16} \iff h \equiv
9 \cdot 11 \equiv 3 \pmod{16}$ (as $9^{-1} \equiv 9 \bmod 16$), and $h \equiv 3
\pmod{16} \iff n = 2h-5 \equiv 1 \pmod{32}$. In $y = h-3$: $8 \mid h \iff y \equiv 5
\pmod 8$; $h \equiv 3\ (16) \iff 16 \mid y$. So for each letter, *the affine map has
an integer output precisely on the letter's legality class*. By induction along a
word, a word applies legally at odd $n \ge 1$ iff the $y$-orbit from $y_0 = (n-1)/2$
is integral at every step, and then the physical and affine values coincide at every
stage ($n_t = 2y_t + 1$; note $y_0 \ge 0$ and both letter maps preserve $y \ge 0$, so
all intermediate $n_t \ge 1$ and the $T$-steps are genuinely inside $\mathbb{Z}^+$).

**(d) Unit-slope lift.** Fix a word $w = \ell_1\cdots\ell_k$ and let
$(Q_j, 9^j, E_j)$ be the composite data of the prefix $\ell_1\cdots\ell_j$ (Step 2
below; $Q_j = \prod_{i\le j} q_{\ell_i}$). Splitting $w$ into the prefix of length
$j$ and the suffix of length $k - j$ with data $(Q_s, 9^{k-j}, E_s)$, the composition
identity of Step 2 gives
$$9^k y_0 + E_k \;=\; 9^{\,k-j}\bigl(9^j y_0 + E_j\bigr) \;+\; Q_j E_s .$$
If $Q_k \mid 9^k y_0 + E_k$ then in particular $Q_j \mid 9^{k-j}(9^j y_0 + E_j)$,
and since $Q_j$ is a power of $2$ and $9$ is odd, $Q_j \mid 9^j y_0 + E_j$: the
top-level congruence forces every intermediate integrality. Hence the legal starting
states of $w$ form exactly the class $y_0 \equiv -E_w P^{-1} \pmod{Q}$ (the inverse
exists, $P$ odd), intersected with $y_0 \ge 0$. This is the same unit-slope mechanism
as L-9916.1(3)/X-9902's incremental lift.

**(e) Reduction logic.** Suppose a Collatz cycle is realized by legal blocks forming
complete $(a,b)$-macros $w_0, \dots, w_{R-1}$ from $n_0$ back to $n_0$. By (c) the
centered states $y_t = (n_t - 1)/2$ at macro boundaries are integers $\ge 0$
satisfying $Q y_{t+1} = P y_t + E_{w_t}$ cyclically — an integral cycle of the
unrestricted system of D-9924.2 with all $y_t \ge 0$. The theorems below refute those
without ever using the residue restrictions, which is stronger and suffices;
conversely, by (c)–(d), every integral orbit on $y \ge 0$ *is* legal, so the affine
model neither loses nor invents physical orbits. $\blacksquare$

### Step 2 — fixed-weight macro algebra (T-9924.2)

**Composition.** By induction on $i$: $Q_{\le i}\, y_i = 9^i y_0 + \sum_{j\le i}
c_{\ell_j} 9^{\,i-j} Q_{<j}$, where $Q_{\le i} := \prod_{t \le i} q_{\ell_t}$. Base
$i = 1$ is the letter relation; the step multiplies by $q_{\ell_{i+1}}$ and inserts
$q_{\ell_{i+1}} y_{i+1} = 9y_i + c_{\ell_{i+1}}$. At $i = k$:
$Q = \prod q_{\ell} = 8^a 16^b$ and $P = 9^k$ — products are order-independent —
while $E_w = \sum_j c_{\ell_j} 9^{k-j} Q_{<j} = 3\sum_{j: \ell_j = \mathsf{A}}
9^{\,k-j} Q_{<j}$ (only $\mathsf{A}$'s contribute, $c_\mathsf{B} = 0$). Each term is
positive, so $E_w > 0 \iff a \ge 1$, and $E_w = 0$ for $a = 0$; each term is
divisible by $3$, so $3 \mid E_w$. (Coherence, used only as a remark: concatenating
macros of weights $(a_1,b_1), (a_2,b_2)$ with data $(Q_1,P_1,E_1), (Q_2,P_2,E_2)$
yields the weight-$(a_1{+}a_2, b_1{+}b_2)$ macro with constant $P_2 E_1 + Q_1 E_2$.)

**Adjacent swap.** Let $w$ have $\mathsf{A}$ at position $j$, $\mathsf{B}$ at $j+1$,
and let $w'$ swap them. Positions $\ne j, j{+}1$ contribute identically ($9$-exponents
unchanged; prefix products of positions $> j{+}1$ contain $q_\mathsf{A} q_\mathsf{B}
= 128$ either way; positions $< j$ are untouched). The $\mathsf{A}$'s own term moves
from $3\cdot 9^{\,k-j} Q_{<j}$ to $3 \cdot 9^{\,k-j-1}\, Q_{<j}\, q_\mathsf{B}$, so
$$E_{w'} - E_w = 3\, \cdot 9^{\,k-j-1} Q_{<j}\, (16 - 9) = 21 \cdot 9^{\,k-j-1}
Q_{<j} > 0 .$$

**Extrema, with uniqueness (à la L-9903.3's all-ones-first/last characterization).**
Any weight-$(a,b)$ word other than $\mathsf{A}^a\mathsf{B}^b$ contains an adjacent
$\mathsf{BA}$; swapping it to $\mathsf{AB}$ strictly decreases $E$ (previous
paragraph, read backwards) and strictly decreases the inversion count, so a chain of
such swaps reaches $\mathsf{A}^a\mathsf{B}^b$ with strict overall decrease:
$E_w > E(\mathsf{A}^a\mathsf{B}^b)$ for every $w \ne \mathsf{A}^a\mathsf{B}^b$.
Dually $E_w < E(\mathsf{B}^b\mathsf{A}^a)$ for every $w \ne
\mathsf{B}^b\mathsf{A}^a$. The values (for $a \ge 1$), by the telescoping identity
$(9-8)\sum_{j=1}^{a} 9^{a-j}8^{j-1} = 9^a - 8^a$:
$$E(\mathsf{A}^a\mathsf{B}^b) = 3\sum_{j=1}^{a} 9^{\,k-j} 8^{\,j-1}
= 3 \cdot 9^b \sum_{j=1}^a 9^{\,a-j}8^{\,j-1} = 3\cdot 9^b\,(9^a - 8^a),$$
$$E(\mathsf{B}^b\mathsf{A}^a) = 3\cdot 16^b \sum_{j=1}^{a} 9^{\,a-j} 8^{\,j-1}
= 3\cdot 16^b\,(9^a - 8^a).$$
Check $(a,b) = (1,1)$: $E(\mathsf{AB}) = 3\cdot 9 = 27$, $E(\mathsf{BA}) =
3\cdot 16 = 48$ — matching the direct compositions $128y' = 81y + 27$ and
$128y' = 81y + 48$. Hence $W = E_{\max} - E_{\min} = 3\,(16^b - 9^b)(9^a - 8^a)$.

**Congruences.** *(mod 21)* Every adjacent swap changes $E$ by a multiple of $21$,
and adjacent transpositions connect all orders of the multiset; so all $E_w$ of one
packet are congruent mod $21$, in particular mod $7$:
$E_w \equiv E_{\min} = 3 \cdot 9^b(9^a - 8^a) \equiv 3\cdot 2^b(2^a - 1) \pmod 7$
(using $9 \equiv 2$, $8 \equiv 1$). *(mod 9)* In $E_w = 3\sum 9^{k-j}Q_{<j}$, every
term with $j < k$ is divisible by $27$; so if $\ell_k = \mathsf{B}$ (no $j = k$ term)
then $27 \mid E_w$, while if $\ell_k = \mathsf{A}$ then $E_w \equiv 3\,Q_{<k} = 3
\cdot 8^{a-1}16^b \equiv 3\,(-1)^{a-1} \pmod 9$ (as $8 \equiv -1$, $16 \equiv 1
\bmod 3$ and $3x \bmod 9$ depends only on $x \bmod 3$). *(mod 8)* Every term with
$j \ge 2$ has $Q_{<j}$ containing $q_{\ell_1} \in \{8, 16\} \equiv 0 \pmod 8$; the
$j = 1$ term exists iff $\ell_1 = \mathsf{A}$ and is $3\cdot 9^{k-1} \equiv 3
\pmod 8$. So $E_w \equiv 3$ if $\ell_1 = \mathsf{A}$ and $E_w \equiv 0$ if $\ell_1 =
\mathsf{B} \pmod 8$. $\blacksquare$

### Step 3a — narrow-alphabet collapse at the sharp threshold (T-9924.3; $=$ L-9923.1/.1C/.1S)

Let $Q > P \ge 1$, $D = Q - P \ge 1$, constants $C_t \in \mathcal{C}$,
$W = C_{\max} - C_{\min} < P + Q$, and let $(y_t)_{t \in \mathbb{Z}/R}$ be an
integral cycle of $Qy_{t+1} = Py_t + C_t$. The ten-line rederivation (span-bound
argument):

1. If $y_{t+1} = y_t$ for every $t$, the cycle is a single fixed point $y^*$ and
   each step reads $Qy^* = Py^* + C_t$, i.e. $C_t = Dy^*$ for all $t$ — one
   constant, divisible by $D$ — as claimed. Otherwise the cycle is **moving**:
   $M := \max_t y_t > \mu := \min_t y_t$.
2. *(An edge enters the max from strictly below.)* Walk backwards from an
   occurrence of $M$: if every predecessor of every occurrence were again $M$,
   one full backward period would make all states $M$ — constant, excluded. So
   some edge has $y_{s+1} = M$, $y_s \le M - 1$, giving
   $QM = Py_s + C_s \le P(M-1) + C_{\max}$, i.e. $C_{\max} \ge DM + P$.
3. *(An edge enters the min from strictly above.)* Symmetrically, some edge has
   $y_{s+1} = \mu$, $y_s \ge \mu + 1$, giving $Q\mu \ge P(\mu+1) + C_{\min}$,
   i.e. $C_{\min} \le D\mu - P$.
4. Subtracting: $W = C_{\max} - C_{\min} \ge D(M - \mu) + 2P \ge D + 2P = P + Q$
   (as $M - \mu \ge 1$, $P \ge 1$) — contradicting $W < P + Q$.
5. So only case 1 occurs: every integral cycle is a one-block fixed point with
   $C_t = Dy^*$ for all $t$. $\square$

*Sharpness.* At $W = P + Q$ the conclusion genuinely fails: the alphabet
$\{Q, -P\}$ carries the moving 2-cycle $0 \to 1 \to 0$
($Q\cdot1 = P\cdot0 + Q$; $Q\cdot0 = P\cdot1 - P$). The instance
$Q = 3, P = 2, \mathcal{C} = \{0,5\}$ with cycle $3 \to 2 \to 3$ (tests T6a$'$)
is this witness shifted by $+2$ (for $D = 1$, shifting all constants by $c$
shifts all states by $c$), and it satisfies the 2-cycle identity
$(P+Q)(y_1 - y_0) = C_{\text{first}} - C_{\text{second}}$: $5 = 5 \cdot 1$.
Conversely a width of **exactly $Q$** carries no moving cycle for $P \ge 1$
(steps 2–4 with $W = Q < P + Q$) — the source spec's claimed $W = Q$ sharpness
example cannot exist; tests T6a$''$ probe this regime. *(The name "zero-carry"
attaches to the weaker $W < Q$ version, whose one-line proof is: repeating steps
2–3 **without** strictness — an edge into the max with $y_s \le M$ gives $DM \le
C_{\max}$, an edge into the min gives $D\mu \ge C_{\min}$, so $Dy_t \in [C_{\min},
C_{\max}]$ for all $t$ — makes $e_t := Dy_t - C_t = Q(y_t - y_{t+1})$ a multiple
of $Q$ trapped in $[-W, W]$, hence $0$. The span-bound argument above strengthens
the threshold to the sharp $W < P + Q$; both appear in L-9923 as .1(c) and .1S.)*

### Step 3b — automatic positivity and the cycle-minimum sieve (T-9924.4; $=$ L-9923.2 (2a)–(2c))

Same setting, now with **all constants positive** ($E_t \in \mathcal{E} \subset
\mathbb{Z}^+$). Alignment with the landed companion file: L-9923.2 proves items
2–5 below with *no sign hypothesis on the constants*, taking positivity of the
**cycle** as its hypothesis; item 1 below (this file's packaging) derives that
positivity from the positivity of the constants, which every packet here with
$a \ge 1$ supplies — so for these packets the sieve covers **all** integral
cycles, not only the positive ones. The ten-line rederivation:

1. *(Confinement.)* With $M := \max_t y_t$, $\mu := \min_t y_t$: an edge into the
   max ($y_{t+1} = M$, $y_t \le M$) gives $QM = Py_t + E_t \le PM + E_{\max}$, so
   $DM \le E_{\max}$; an edge into the min gives $Q\mu \ge P\mu + E_{\min}$, so
   $D\mu \ge E_{\min} \ge 1$. Hence every state satisfies
   $\lceil E_{\min}/D\rceil \le y_t \le \lfloor E_{\max}/D\rfloor$; in particular
   $y_t \ge 1$ — an integral cycle is automatically entirely positive.
2. *(Minimum equation.)* Anchor at $t^*$ with $y_{t^*} = \mu$; then $y_{t^*+1} \ge
   \mu$, and $E_{t^*} = Q y_{t^*+1} - P\mu = D\mu + Q\kappa$ with
   $\kappa := y_{t^*+1} - \mu \ge 0$: *some alphabet constant equals
   $D\mu + Q\kappa$, $\mu \ge 1$, $\kappa \ge 0$.*
3. *(g-sieve.)* Assume $g \ge 2$, $g \mid P$, $\gcd(g,Q) = 1$, $g \mid E$ for all
   $E \in \mathcal{E}$. Then $D = Q - P \equiv Q \pmod g$, so $0 \equiv E_{t^*} =
   D\mu + Q\kappa \equiv Q(\mu + \kappa) \pmod g$, and since $\gcd(Q, g) = 1$,
   $g \mid \mu + \kappa$. As $\mu + \kappa \ge 1$, $\mu + \kappa \ge g$; and $Q > D$
   gives $E_{t^*} = D\mu + Q\kappa \ge D(\mu+\kappa) \ge gD$.
4. *(Gate.)* If $E_{\max} < gD$, item 3 is contradictory: **no integral cycle**.
5. *(Targets.)* Unconditionally, items 2–3 force $\mathcal{E} \cap \mathcal{T} \ne
   \emptyset$ for $\mathcal{T} = \{Dm + Qk \le E_{\max}: m \ge 1, k \ge 0,
   g \mid m + k\}$, a finite set ($m \le E_{\max}/D$, $k \le E_{\max}/Q$). $\square$

### Step 3c — the gate and its exact rows (T-9924.5)

Fix a packet $(a,b)$ with $a \ge 1$ and take $g = 3$: indeed $3 \mid P = 9^{a+b}$,
$\gcd(3, Q) = 1$ ($Q$ a $2$-power), and $3 \mid E_w$ for every constant
(T-9924.2). The gate of Step 3b(4) is $E_{\max} < 3D$, i.e.
$$3\cdot16^b(9^a - 8^a) \;<\; 3\,(8^a16^b - 9^{a+b})
\;\iff\; 9^a16^b - 8^a16^b \;<\; 8^a16^b - 9^{a+b}
\;\iff\; G(a,b):\ 9^a(16^b + 9^b) \;<\; 2\cdot 8^a\cdot16^b,$$
the last step by adding $8^a16^b + 9^{a+b}$ to both sides and collecting
$9^a16^b + 9^a9^b = 9^a(16^b + 9^b)$. Three structural facts:

1. **$G \Rightarrow$ contracting.** $9^a \ge 8^a$ gives $9^a16^b \ge Q$, so from $G$:
   $9^{a+b} < 2Q - 9^a16^b \le Q$, i.e. $P < Q$. (So applying Step 3b under $G$ is
   legitimate.)
2. **$b$-monotonicity.** If $G(a,b)$ then
   $9^a(16^{b+1} + 9^{b+1}) < 16\cdot 9^a(16^b + 9^b) < 16 \cdot 2\cdot 8^a 16^b =
   2\cdot 8^a 16^{b+1}$, using $9\cdot 9^b < 16\cdot 9^b$. So each row of the table
   is upward closed in $b$.
3. **$a \ge 6$ kills all rows.** $9^a(16^b + 9^b) > 9^a 16^b \ge 2\cdot 8^a 16^b$
   whenever $9^a \ge 2 \cdot 8^a$; and $(9/8)^a$ is increasing with
   $9^6 = 531441 > 524288 = 2\cdot8^6$, so this holds for all $a \ge 6$. (These are
   the *same integers* as $3^{12} > 2^{19}$, margin $7153$ — the identical
   near-commensurability that makes $(5,1)$ supercritical. The family's $a$-cutoff
   and the $(5,1)$ frontier are one inequality.)

Exact boundary evaluations (each an integer comparison):
$$G(1,1):\ 225 < 256\ \checkmark\qquad G(2,1):\ 2025 < 2048\ \checkmark$$
$$G(3,1):\ 18225 \ge 16384\ \times\qquad G(3,2):\ 245673 < 262144\ \checkmark$$
$$G(4,1):\ 164025 \ge 131072\ \times\qquad G(4,2):\ 2211057 \ge 2097152\ \times
\qquad G(4,3):\ 31656825 < 33554432\ \checkmark$$
$$G(5,1):\ 1476225 \ge 1048576\ \times\qquad G(5,2):\ 19899513 \ge 16777216\ \times$$
$$G(5,3):\ 284911425 \ge 268435456\ \times\qquad
G(5,4):\ 4257255753 < 4294967296\ \checkmark$$
With monotonicity (2), $G$ holds exactly on $a \in \{1,2\}, b \ge 1$; $a = 3, b \ge
2$; $a = 4, b \ge 3$; $a = 5, b \ge 4$ — **the source's table rows, verified**. The
exceptional pairs in $\{1 \le a \le 5,\ b \ge 1\}$ are exactly $(3,1), (4,1), (4,2),
(5,1), (5,2), (5,3)$. Of these, $(5,1)$ has $Q = 2^{19} < 3^{12} = P$
(supercritical); the other five are contracting ($8192 > 6561$; $65536 > 59049$;
$1048576 > 531441$; $8388608 > 4782969$; $134217728 > 43046721$).

**Conclusion for every gate packet** ($G(a,b)$ true): by Step 3b(4), the packet has
**no integral cycle whatsoever** — any length $R \ge 1$, any branch orders (the
lemma quantifies over arbitrary constant sequences from $\mathcal{E}_{a,b}$, which
contains all $\binom{a+b}{b}$ orders), any starting integer, any sign.

### Step 4 — the six exceptional packets (T-9924.6)

All numbers below are recomputed from scratch and machine-verified (Adversarial
tests T4/T5); margins are displayed so every enumeration is transparently finite.

**(i) Packet $(3,1)$** — $Q = 8192$, $P = 6561$, $D = 1631 = 7\cdot233$,
$\mathcal{E} = \{5859,\ 7203,\ 8715,\ 10416\}$ (orders
$\mathsf{AAAB}, \mathsf{AABA}, \mathsf{ABAA}, \mathsf{BAAA}$),
$W = 3\,(16-9)(9^3 - 8^3) = 21\cdot217 = 4557 < 8192 = Q$. T-9924.3 applies: any
integral cycle is a fixed point $y^*$ with $Dy^* \in \mathcal{E}$. But
$\mathcal{E} \bmod D = \{966,\ 679,\ 560,\ 630\}$ — no constant is divisible by
$D$. **No integral cycle exists** (any sign — in particular the trivial $y = 0$ is
*not* a cycle of this packet, as $0 \notin \mathcal{E}$). Independent double-check
by the sieve route: $\mathcal{T} = \{3D, 6D\} = \{4893, 9786\}$ (here $6D = 9786
\le E_{\max} = 10416 < 9D$, and $2D + Q = 11454 > E_{\max}$), disjoint from
$\mathcal{E}$.

**(ii) Packet $(4,1)$** — $Q = 65536$, $P = 59049$, $D = 6487 = 13\cdot499$,
$\mathcal{E} = \{66555,\ 77307,\ 89403,\ 103011,\ 118320\}$,
$W = 21\,(9^4 - 8^4) = 21\cdot2465 = 51765 < 65536 = Q$. T-9924.3 applies;
$\mathcal{E} \bmod D = \{1685,\ 5950,\ 5072,\ 5706,\ 1554\}$ — none $0$. **No
integral cycle.** (Sieve double-check: the nine targets $\{3D, 6D, \dots, 18D,
2D{+}Q, 5D{+}Q, 8D{+}Q\}$ are disjoint from $\mathcal{E}$; tests T4.)

**(iii) Packet $(4,2)$** — $Q = 2^{20} = 1048576$, $P = 9^6 = 531441$,
$D = 517135 = 5\cdot59\cdot1753$, $|\mathcal{E}| = \binom{6}{2} = 15$,
$E_{\min} = 3\cdot81\cdot2465 = 598995$, $E_{\max} = 768\cdot2465 = 1893120$.
The gate fails narrowly ($2211057$ vs $2097152$, a $5.4\%$ miss), and
$W = 1294125 > Q$, so the *spec's* collapse threshold $W < Q$ does not reach this
packet — but the **sharp** threshold does:
$$Q = 1048576 \;<\; W = 1294125 \;<\; P + Q = 1580017 \qquad (\text{margin } 285892).$$
*Primary closure (collapse, T-9924.3).* Every integral cycle is a one-block fixed
point $y^*$ with $Dy^* \in \mathcal{E}$. The multiples of $D$ inside
$[E_{\min}, E_{\max}]$ are exactly $2D = 1034270$ and $3D = 1551405$ (as
$D < E_{\min} < 2D$ and $4D = 2068540 > E_{\max}$). By T-9924.2, all $15$
constants are $\equiv 3\cdot2^2(2^4-1) = 180 \equiv 5 \pmod 7$; while $Q = 2^{20}
\equiv 4$ and $P = 9^6 \equiv 1 \pmod 7$ give $D \equiv 3$, so $2D \equiv 6$ and
$3D \equiv 2 \pmod 7$. Neither residue is $5$, so no constant is a multiple of
$D$ (equivalently: $\mathcal{E} \bmod D$ is nowhere $0$ — verified directly in
tests T4). **No integral cycle.**
*Independent second closure (the source's sieve route).* Targets with the $3 \mid
(m+k)$ refinement: within $m + k = 3$ the values $Dm + Qk$ increase in $k$ (as
$Q > D$):
$$3D = 1551405 \le E_{\max}; \quad 2D + Q = 2082846 > E_{\max}\ (\text{margin }
189726); \quad D + 2Q = 2614287 > E_{\max};$$
and $m + k \ge 6$ forces $Dm + Qk \ge 6D = 3102810 > E_{\max}$ (margin $1209690$).
So $\mathcal{T} = \{3D\}$ — *only the target $3D$ survives*, as the source
claimed — and $3D \equiv 2 \ne 5 \pmod 7$: $\mathcal{E} \cap \mathcal{T} =
\emptyset$. Same conclusion by an independent mechanism.

**(iv) Packet $(5,2)$** — $Q = 2^{23} = 8388608$, $P = 9^7 = 4782969$,
$D = 3605639 = 79\cdot45641$, $|\mathcal{E}| = \binom{7}{2} = 21$,
$E_{\min} = 3\cdot81\cdot26281 = 6386283$, $E_{\max} = 768\cdot26281 = 20183808$
(here $9^5 - 8^5 = 26281$). Collapse is inapplicable **even at the sharp
threshold**: $W = 13797525 > P + Q = 13171577$ (excess $625948$); the sieve is
genuinely needed. Targets: $3D = 10816917$ and $2D + Q = 15599886$ are
$\le E_{\max}$; $D + 2Q = 20382855 > E_{\max}$ (margin $199047$ — the tightest
margin in the file); $m + k \ge 6$ gives $\ge 6D = 21633834 > E_{\max}$ (margin
$1450026$). So $\mathcal{T} = \{3D,\ 2D + Q\}$ — *two targets survive*. Mod 9:
$Q = 2^{23} \equiv 2^{23 \bmod 6} = 2^5 \equiv 5 \pmod 9$ and $9 \mid P$, so
$D \equiv 5$ and $3D \equiv 15 \equiv 6$, $2D + Q \equiv 15 \equiv 6 \pmod 9$ —
*both targets $\equiv 6 \pmod 9$*. By T-9924.2 (mod-9 rule, $a = 5$ odd), every
constant is $\equiv 0 \pmod 9$ (last letter $\mathsf{B}$: the $6$ words) or
$\equiv 3 \pmod 9$ (last letter $\mathsf{A}$: the $15$ words). Since
$6 \notin \{0, 3\}$: **no integral cycle.**

**(v) Packet $(5,3)$** — $Q = 2^{27} = 134217728$, $P = 9^8 = 43046721$,
$D = 91171007 = 257\cdot354751$, $|\mathcal{E}| = \binom{8}{3} = 56$,
$E_{\min} = 3\cdot729\cdot26281 = 57476547$, $E_{\max} = 12288\cdot26281 =
322940928$. Collapse inapplicable even at the sharp threshold:
$W = 265464381 > P + Q = 177264449$ (excess $88199932$). Targets: $3D = 273513021$ and $2D + Q = 316559742$ are $\le E_{\max}$;
$D + 2Q = 359606463 > E_{\max}$ (margin $36665535$); $m+k \ge 6$ gives $\ge 6D =
547026042 > E_{\max}$. So $\mathcal{T} = \{3D,\ 2D+Q\}$. Mod 8: $8 \mid Q$ and
$P = 9^8 \equiv 1 \pmod 8$, so $D \equiv -1 \equiv 7$, $3D \equiv 21 \equiv 5$,
$2D + Q \equiv 14 \equiv 6 \pmod 8$ — *targets $\equiv 5, 6 \pmod 8$*. By
T-9924.2 (mod-8 rule), every constant is $\equiv 3 \pmod 8$ (first letter
$\mathsf{A}$: $35$ words) or $\equiv 0 \pmod 8$ (first letter $\mathsf{B}$: $21$
words). Since $\{5,6\} \cap \{0,3\} = \emptyset$: **no integral cycle.**

**(vi) Packet $(5,1)$ — the six-branch chart; supercritical.** $Q = 8^5\cdot16 =
2^{19} = 524288 < 531441 = 3^{12} = 9^6 = P$; $P - Q = 7153 = 23\cdot311$;
$\mathcal{E} = \{709587,\ 795603,\ 892371,\ 1001235,\ 1123707,\ 1261488\}$
(closed form: $\mathsf{B}$ in position $p$ gives $E(p) = 21\cdot9^{\,6-p}8^{\,p-1}
+ 21459$; note $21459 = 3\cdot7153$). Unrolling $R$ macros (the same induction as
Step 2, at macro level — the block-grammar analogue of the cycle equation
L-9905.1):
$$Q^R y_R = P^R y_0 + \sum_{t=0}^{R-1} P^{\,R-1-t} Q^{\,t} E_t, \qquad\text{so for a
cycle}\qquad (Q^R - P^R)\, y_0 = \sum_{t=0}^{R-1} P^{\,R-1-t}Q^{\,t}E_t .$$
The right side is $> 0$ (every $E_t \ge E_{\min} = 709587 > 0$, coefficients
positive); the left side is $\le 0$ whenever $y_0 \ge 0$, since $Q < P$ makes
$Q^R - P^R < 0$. Anchoring at any nonnegative state (rotation invariance): **no
integral $(5,1)$-cycle contains a state $y_t \ge 0$** — in particular no positive
or trivial cycle exists. (This is the supercritical sign obstruction, stated in
general as L-9923.3(ii), which needs only $C_i \ge 0$; here the constants are
strictly positive, which is what also excludes states $y_t = 0$.) A hypothetical
cycle would have to be entirely negative
(out of physical scope; none was found for $R \le 5$ in tests T5, but no claim is
made). Furthermore, along any forward-integral path with $y_0 > 0$:
$y_{t+1} = (Py_t + E_t)/Q > (P/Q)\,y_t$, so $y_t > (P/Q)^t y_0 \to \infty$: **an
all-time positive $(5,1)$-path is divergent** (D-9907). This is the macro-side
twin of L-9916.2.3 (PROVED), which proves divergence for the chart's seeds — see
Step 6 and T-9924.8 for the exact identification.

**(vii) Packet $a = 0$ (all-$\mathsf{B}$).** Single letter, $E \equiv 0$: a cycle
satisfies $(16^R - 9^R)\,y_0 = 0$ with $16^R > 9^R$, so $y_0 = 0$, and $y = 0$ is
indeed fixed ($16\cdot0 = 9\cdot0$). Physically $n = 1$, where $\mathsf{B}$ is legal
($1 \equiv 1 \bmod 32$) and computes $T^4(1) = 1$ through $1 \to 2 \to 1 \to 2 \to
1$: the trivial cycle of D-9905. $\blacksquare$

### Step 5 — assembly of the Main Theorem (T-9924.7)

Fix $b \ge 1$, $0 \le a \le 5$, $R \ge 1$, weight-$(a,b)$ words $w_0, \dots,
w_{R-1}$ (arbitrary, independent), and $(y_t) \in \mathbb{Z}^R$ with
$Qy_{t+1 \bmod R} = Py_t + E_{w_t}$.

- If $a = 0$: Step 4(vii) forces $y \equiv 0$.
- If $1 \le a \le 5$ and $G(a,b)$ holds (all pairs except the six exceptional, by
  T-9924.5): T-9924.4(d) with $g = 3$ (hypotheses verified in Step 3c) shows no
  such data exist.
- If $(a,b) \in \{(3,1), (4,1), (4,2), (5,2), (5,3)\}$: Step 4(i)–(v) shows no such
  data exist.
- If $(a,b) = (5,1)$: Step 4(vi) shows every such cycle has all $y_t < 0$.

**Quantifier audit (the load-bearing point).** A "word over the macro alphabet" is
an arbitrary element of $W_{a,b}^{\,R}$, i.e. each of the $R$ macros independently
uses any of the $\binom{a+b}{b}$ branch orders; the corresponding constant sequence
$(E_{w_t})$ is an arbitrary element of $\mathcal{E}_{a,b}^{\,R}$. Every lemma
invoked (T-9924.3, T-9924.4, the sign argument) quantifies over **arbitrary
sequences of constants from the alphabet** — nothing assumes the same order is
reused, so switching between different branch orders at each macro is covered
*because the alphabet is complete*. No least-period or distinctness assumption is
made anywhere; rotations and repetitions are automatically included. Since
$n = 2y + 1$, the physical domain $n \ge 1$ is exactly $y \ge 0$, and the only
cycle meeting it is $y = 0$ under all-$\mathsf{B}$, i.e. $h = 3$, $n = 1$.
$\blacksquare$

**Proof of Corollary 1.** By T-9924.1(e), the legal realization yields an integral
macro cycle with all $y_t \ge 0$; by the Theorem it is the all-$\mathsf{B}$ fixed
point $y = 0$, $n_0 = 1$. $\square$

**Proof of Corollary 2** *(addition beyond the source spec)*. A cyclic letter word
with per-period counts $(\alpha, \beta)$, read from any starting point, is a
*single* complete weight-$(\alpha,\beta)$ macro whose cycle has $R = 1$; and a
concatenation of complete macros of several weights is such a letter cycle with
$(\alpha, \beta)$ the totals. If $\beta = 0$, $\alpha \ge 1$: $Q = 8^\alpha <
9^\alpha = P$ and the single constant $3(9^\alpha - 8^\alpha)$ is positive, so the
sign argument of Step 4(vi) applies verbatim: no cycle with a state $\ge 0$.
If $\beta \ge 1$ and $Q_{\alpha,\beta} < P$: same sign argument. If $\beta \ge 1$,
$Q > P$, $\alpha \le 5$: the Main Theorem (case $R = 1$ suffices, but any $R$ is
covered) gives no integral cycle at all. The only remaining possibility with a
state $y \ge 0$ is $\beta \ge 1$, $\alpha \ge 6$, $Q_{\alpha,\beta} > P$ — and
then T-9924.4(a) confines it to $I_{\alpha,\beta}$. (The all-$\mathsf{B}$ fixed
point is the excluded trivial case $\alpha = 0$.) $\square$

### Step 6 — the six-branch correspondence, the phase transition, and positioning (T-9924.8)

**The dictionary.** The six-branch chart (L-9916 D-9916.1–.3; X-9902) has the same
$P = 3^{12}$, $Q = 2^{19}$ as packet $(5,1)$, digits $\mathrm{a}(x) = Q\lceil
Px/Q\rceil - Px$, and alphabet $A = \{\alpha_i = 7\cdot3^{2i}2^{15-3i}\} =
\{229376, 258048, 290304, 326592, 367416, 413343\}$.

*(1) Constants $\leftrightarrow$ digits.* For $\mathsf{B}$ in position $p$ and
$i := 6 - p$:
$$E(p) = 21\cdot9^{\,6-p}8^{\,p-1} + 21459 = 3\cdot7\cdot3^{2i}\,2^{15-3i} +
3\cdot7153 = 3\,(\alpha_i + 7153),$$
using $9^{\,i} 8^{\,5-i} = 3^{2i}2^{15-3i}$ and $21459 = 3\cdot7153$
— explicitly, $7153 = P - Q$. This is a bijection between the six branch orders and
the six chart digits: larger digits $\leftrightarrow$ earlier $\mathsf{B}$.
*(The derivation of $E(p)$: moving $\mathsf{B}$ one step left is one adjacent swap,
so $E(p) - E(p{+}1) = 21\cdot9^{\,5-p}8^{\,p-1}$ by T-9924.2, and $E(6) = E_{\min}
= 27\cdot26281 = 709587 = 21\cdot8^5 + 21459$; summing the telescope gives the
closed form.)*

*(2) Distinctness mod $Q$ / determinism.* For $p < p'$, $E(p) - E(p') = 21
\sum_{q=p}^{p'-1} 9^{\,5-q}8^{\,q-1}$; the summands have pairwise distinct 2-adic
valuations $3(q-1) \le 12$, so $\nu_2(E(p) - E(p')) = 3(p-1) \le 12 < 19$; hence no
difference is divisible by $Q = 2^{19}$: the six constants are pairwise distinct
mod $Q$, and at each $y$ at most one branch is integral — matching the chart's
determinism.

*(3) Conjugacy.* Let $x \in \mathbb{Z}$ and $y := 3(x - 1)$ (equivalently $h = 3x$,
$n = 6x - 5$). For any digit value $\alpha \in [0, Q)$ with $Q \mid Px + \alpha$
(i.e. $\alpha = \mathrm{a}(x)$, L-9916.1(1)) and $x' := (Px + \alpha)/Q =
\mathcal{C}(x)$:
$$Q\cdot3(x' - 1) = 3(Px + \alpha) - 3Q = P\cdot3(x-1) + 3\,(\alpha + P - Q),$$
i.e. $Q y' = P y + 3(\alpha + 7153)$ with $y' = 3(x'-1)$. If $\alpha =
\alpha_i \in A$ then $3(\alpha_i + 7153) = E(6-i) \in \mathcal{E}_{5,1}$: the chart
step *is* one $(5,1)$-macro step, with the branch order dictated by the digit.
Conversely, if $3 \mid y$ and $Q \mid Py + E$ for some $E \in \mathcal{E}_{5,1}$,
put $x := y/3 + 1$ and $\alpha := E/3 - 7153 \in A$; then $Px + \alpha = (Py + E)/3
+ Q$, so $Q \mid Px + \alpha$, forcing $\alpha = \mathrm{a}(x)$ and $\mathcal{C}(x)
= ((Py+E)/Q)/3 + 1$. Finally, the restriction $3 \mid y$ is *free on cycles and
tails*: after any macro step, $Qy' = Py + E \equiv 0 + 0 \pmod 3$ and
$\gcd(Q,3) = 1$ give $3 \mid y'$; on a cycle every state has a predecessor, so all
states are $\equiv 0 \pmod 3$. Hence: **integral $(5,1)$-macro cycles $=$ chart
cycles with all digits in $A$; all-time forward-integral $(5,1)$-paths from $y$
$=$ chart seeds $x = y/3 + 1 \in \bigcap_N S_N$; physically $n = 2y + 1 = 6x - 5$.**

*(4) Worked instance (machine-verified, tests T7).* $x = 6472 = m_1$ (X-9902's
least level-1 root): $Px = 3439486152$, $\mathcal{C}(x) = 6561 = 3^8$, digit
$= 524288\cdot6561 - 3439486152 = 367416 = \alpha_4$, so the branch is
$\mathsf{ABAAAA}$ ($p = 2$), $E = 3(367416 + 7153) = 1123707$. Physically:
$n = 6\cdot6472 - 5 = 38827$ runs $\mathsf{ABAAAA}$ legally under $T$ (19
$T$-steps) and lands at $6\cdot6561 - 5 = 39361$; in $y$: $19413 \mapsto 19680 =
3(6561 - 1)$. ✓

**C1 (divergence; PROVED cross-ref).** By the dictionary, an all-time positive
$(5,1)$-path is a chart seed; L-9916.2.3 (PROVED) gives $x_n \ge (P/Q)^n x \to
\infty$. (The direct one-line proof was given in Step 4(vi); the two are the same
statement under (3).)

**C2 (empirical floor; EMPIRICAL, clearly labelled).** X-9902 (reviewer-extended,
finite computation, *not proof*) gives $m_{16} =
4629285799073801695890071893291563216294381998435632568233291338101143197194568
\approx 4.63\times10^{78}$ and $m_N$ non-decreasing; so any all-time root of the
$(5,1)$ grammar — hence any positive integer with $n \equiv 1 \pmod 6$ whose
$T$-orbit runs complete $(5,1)$-macros forever — satisfies $x > m_{16}$, physically
$$n = 6x - 5 \;>\; 6\,m_{16} - 5 \;=\;
27775714794442810175340431359749379297766291990613795409399748028606859183167403
\;\approx\; 2.78\times10^{79}.$$
*(Reviewer's clarification, fable-02-v26 — the residue qualifier above: the
dictionary of (3) defines $x$ only where $3 \mid y$, i.e. $n \equiv 1 \pmod 6$;
that is automatic for every state from the first macro image on (Step 6(3)), but
not for a seed, whose one legality class mod $Q = 2^{19}$ carries no mod-3
information. A hypothetical all-time seed in another odd residue class inherits
the floor at its first macro image $n_1 > 6m_{16} - 5$, hence itself satisfies
$n_0 = (Qn_1 - 2E - (Q - P))/P > \bigl(Q\,(6m_{16}{-}5) - 2E_{\max} +
(P{-}Q)\bigr)/P > 2.74\times10^{79}$ — marginally weaker. Separately, the strict
$x > m_{16}$ is finite-verified: $a_{16}(m_{16}) = 13249 \notin A$, so $m_{16}
\notin S_{17}$ and $m_{17} > m_{16}$ (monotonicity alone gives only $\ge$). Both
points are EMPIRICAL-level bookkeeping; no theorem cites C2. See Verification
note V.2–V.3.)*

**Phase transition and positioning (the commission's Step 6).** Within the row
$b = 1$: packets $(0,1)$–$(4,1)$ are contracting ($16\cdot8^a > 9^{a+1}$ for
$a \le 4$) and fully cycle-free by Steps 3–4; $(5,1)$ is the **first supercritical
packet** — $2^{19} < 3^{12}$ — where cycles die by sign instead of by arithmetic,
and the surviving question is no longer cycles but *ordinary extraction*: does any
positive integer satisfy the $(5,1)$ digit condition forever? By L-9916.2 that is
precisely the $m_N$ dichotomy of issue #58 ($m_N \to \infty$, i.e. no seed, versus
$m_N$ eventually constant, i.e. a divergent-orbit candidate seed — L-9916 also
proves the "bounded nonempty" branch empty and that no seed word is eventually
periodic). That is why the six-branch chart is the natural frontier object of this
program: it is the unique packet of the family sitting exactly at the
supercriticality threshold, and the threshold inequality $3^{12} > 2^{19}$ is
simultaneously what terminates the family at $a = 5$ (Step 3c(3)). The
complementary cycle-side result in the source program is PR #47's L-9607 (aligned
Christoffel mixtures; external). $\blacksquare$

---

## Dependency audit

| Dependency | Where used |
|---|---|
| D-9901/D-9902 ($C$, $T$), D-9903/D-9904 ($S$, exponents) | Step 0: blocks as $T$/$S$-composites; legality classes. |
| D-9905 (trivial cycles) | Step 4(vii), Corollary 1: identification of $n = 1$'s cycle. |
| D-9907 (divergence) | Step 4(vi), T-9924.8 C1. |
| D-9908 (cycle conventions) | Cycle notation and anchoring (with L-9905's rotation convention re-stated inline). |
| NOTATION.md conventions (empty sum/product) | Step 2 induction base; $Q_{<1} = 1$. |
| **L-9923.1/.1C/.1S, .2(2a–2c), .3(ii) (landed 2026-07-26; PROPOSED, verification in progress)** | *Cited for attribution and cross-checking only*; all three statements re-proved inline (Steps 3a, 3b, 4(vi)), including the sharp threshold $W < P+Q$. **No logical dependence** — this file is unaffected by L-9923's review outcome. |
| L-9916.1(1),(3) (PROVED) | T-9924.8(3): digit uniqueness in $[0,Q)$; the unit-slope-lift mechanism is also re-proved inline (Step 0(d)), so the only true import is the digit-range fact, itself one line. |
| L-9916.2.3 (PROVED) | T-9924.8 C1 (cross-reference; a direct one-line proof is also given in Step 4(vi)). |
| L-9916.2.1–.2 (PROVED) | Step 6 positioning (the $m_N$ dichotomy) — positioning only, not used in any proof. |
| X-9902 (EMPIRICAL) | T-9924.8 C2 and the worked instance $m_1 = 6472$ — clearly labelled empirical; no theorem depends on it. |
| L-9905.1, L-9903.3 (PROVED) | Analogy/attribution only (macro cycle equation; extremal-word characterization style). Not used logically. |
| External: source draft "T-9608", PR #47 L-9607 | Provenance only. Nothing is imported. |

**The Main Theorem T-9924.7 depends only on NOTATION.md definitions and the inline
proofs of this file.** No circularity is possible; whatever the outcome of L-9923's
independent review, this file is unaffected (see Companion-file note).

## Gap audit

Deliberate search per README §8:

- **Hidden finiteness assumptions:** none. The infinite family ($b$ unbounded) is
  handled by the algebraic row structure of $G$ (monotonicity proved for all $b$),
  not by the $b \le 12$ table check (which is verification only). Each exceptional
  packet is closed by a finite, displayed computation with margins.
- **Unjustified induction:** the only inductions are the prefix-composition formula
  (Step 2) and its macro-level unrolling (Step 4(vi)), both with explicit base and
  step.
- **Boundary cases:** $a = 0$ (Step 4(vii)); $b = 0$ and general supercritical
  weights (Corollary 2 — flagged as an addition); $R = 1$ (fixed points — included,
  no distinctness assumed); $(a,b) = (0,0)$ excluded ($k \ge 1$); $\mu = $ minimum
  attained at several $t$ (any choice works); $\kappa = 0$ allowed; the target
  enumerations include their boundary members and display the excluded margins.
- **Empirical vs. universal:** X-9902 material appears only in C2/worked instance,
  labelled EMPIRICAL; the Adversarial tests are labelled finite verification and no
  proof cites them.
- **Invalid limit interchanges:** none occur.
- **Circular dependence:** none (see Dependency audit; L-9923 re-proved inline).
- **Nonuniform estimates:** all bounds are exact integer comparisons with displayed
  margins.
- **Assumptions equivalent to Collatz:** none; all results are consistent with both
  truth values of D-9909's question, and the Honest scope box states exactly what is
  *not* excluded.
- **Sign errors / division by zero:** T-9924.3 is valid for constants of any sign;
  T-9924.4 requires positive constants — supplied by $E_w > 0$ for $a \ge 1$
  (T-9924.2); every division is by a displayed nonzero quantity ($D \ge 1$ in
  contracting packets — including the implication $G \Rightarrow Q > P$, proved,
  which legitimizes the gate's use of $D > 0$; $Q^R - P^R \ne 0$ since $Q \ne P$).
- **Least-period subtleties:** no proof uses least periods or distinct states;
  cycles may revisit states with different branch choices — the graph-theoretic
  searches in the tests treat exactly this generality, and the lemmas only ever use
  one minimum-anchored step.
- **Physical-correspondence gaps:** legality $\iff$ integrality is proved in both
  directions (Step 0(c)–(d)), including oddness/positivity of all intermediate
  states; the reduction direction actually used is stated separately (Step 0(e)) so
  the theorem does not silently rely on the (stronger) equivalence.
- **Nondeterminism:** the affine systems are treated as nondeterministic relations;
  all cycle-freeness statements quantify over all branch sequences, which covers the
  deterministic physical dynamics a fortiori.

No gaps found by the author. The single deliberate weakening: for $(5,1)$ (and
general supercritical weights) *entirely negative* integral cycles are not excluded
— they have no physical meaning here (Honest scope (iv)), and none exist for
$R \le 5$ (tests T5), but no universal claim is made.

## Adversarial tests

**Finite verification, not proof.** Exact integer arithmetic only (Python ints; no
floats). Deterministic (fixed seed). Script kept at
`scratchpad/t9924_tests.py` (session-local); full code inline below; runs in
$\approx 5$ s on CPython 3 (stdlib only). Design notes — what each test attacks:

1. **T1** attacks Step 0 where it could silently fail: (a) the legality classes are
   verified *as biconditionals* against direct $T$-iteration with valuation checks
   for every odd $n < 4\cdot10^5$ (both directions of "legality $=$ residue class
   $=$ $h$-integrality"); (b) every word of length $\le 4$ is run at 50,000 seeds
   through both the legal-$T$ composite and the centered affine orbit, requiring
   agreement of *failure stage* as well as values; (c) the unit-slope lift is
   exercised at length 6: the single top-level residue class must make the entire
   26-to-24-$T$-step composite legal (192 instances).
2. **T2** enumerates **all** 510 words with $a + b \le 8$: order-independence of
   $(Q, P)$, the closed constant formula, positivity, $3 \mid E$, the mod-21/9/8
   rules, the adjacent-swap identity term-by-term, extremal values *and their
   uniqueness*, and $(1,1) = \{27, 48\}$. (Constants were pairwise distinct in every
   packet tested — observed, never used.)
3. **T3** checks the gate table exactly for $a \le 8$, $b \le 12$ against the
   claimed rows, monotonicity in $b$, the equivalence $G \iff (E_{\max} < 3D)$, the
   implication $G \Rightarrow Q > P$, and the $a \ge 6$ threshold identity
   $9^6 - 2\cdot8^6 = 3^{12} - 2^{19}$.
4. **T4** recomputes every exceptional-packet quantity from scratch: $D$ with full
   factorization, all constants (counts $4, 5, 15, 21, 56, 6$), $W$ vs $Q$ (including
   the honest $W > Q$ flags where the collapse lemma must *not* be used), the exact
   target sets with the $3 \mid (m{+}k)$ refinement, all residue claims with counts,
   and the $(5,1)$ closed form $E(p)$.
5. **T5** hunts for cycles directly, three ways: (i) exhaustive directed-cycle search
   on the confinement interval $I_{a,b}$ (complete for **all** integral cycles of the
   contracting packets, by T-9924.4(a) — the observed edge count is $0$, i.e. not
   even one integral macro step exists inside the box); (ii) raw window search
   $|y| \le 5\cdot10^4$ including negatives for $(3,1)$ and $(4,2)$; (iii)
   cycle-equation enumeration over **all** constant sequences up to length
   $R \le 6/5/3/3/2/5$ per packet — none admits an integral solution; for $(5,1)$
   none exists at all up to $R = 5$ (even negative), and the all-$\mathsf{B}$ fixed
   point is confirmed legal at $n = 1$.
6. **T6** attacks the inline lemmas on 698 random synthetic systems: T6a probes
   the collapse at the **sharp** threshold, deliberately generating widths in the
   extension regime $Q \le W < P + Q$ that the spec's $W < Q$ missed (84 of 300
   systems landed there; all collapsed); T6a$'$ verifies the sharpness witness at
   $W = P + Q$ exactly (a genuine moving 2-cycle, with the identity
   $(P{+}Q)(y_1{-}y_0) = \Delta C$); T6a$''$ confirms on 100 systems that width
   exactly $Q$ carries no moving cycle (the spec's old sharpness claim is
   impossible); T6b checks the sieve gate on 298 systems.
7. **T7** verifies the six-branch dictionary: the digit-ladder identity, the exact
   bijection $E = 3(\alpha + 7153)$, distinctness mod $Q$, and 24 dynamic
   conjugacy instances checking simultaneously the chart step, the unique integral
   branch, $y' = 3(x'-1)$, and the *physical* $T$-run at $n = 6x - 5$; it also
   reproduces X-9902's $m_1 = 6472$ and computes the exact physical floor
   $6m_{16} - 5$.

```python
#!/usr/bin/env python3
"""
Adversarial tests for T-9924 (research/foundations/T-9924-pulse-grammar-cycle-free.md).
FINITE VERIFICATION ONLY -- not a proof.
Agent: fable-02-p18.  Date: 2026-07-26.  Exact integer arithmetic throughout
(Python ints; no floats anywhere).  Deterministic: random uses a fixed seed.
"""
import random
from itertools import combinations, product as iproduct

random.seed(99240)
fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

def v2(m):
    assert m != 0
    k = 0
    while m % 2 == 0:
        m //= 2; k += 1
    return k

def T(n):                       # shortcut map, D-9902
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def ceildiv(a, b):
    return -((-a) // b)

# ---- block maps in physical n-coordinates, legality via direct T-iteration ----
def blockA_T(n):
    """Legal block A at odd n>=1: Syracuse exponents (1,2), parity word (1,1,0).
    Returns T^3(n) if legal (with all internal checks), else None."""
    if n < 1 or n % 2 == 0 or v2(3 * n + 1) != 1:
        return None
    n1 = (3 * n + 1) // 2
    if v2(3 * n1 + 1) != 2:
        return None
    t0, t1 = n, T(n); t2 = T(t1); t3 = T(t2)
    assert (t0 % 2, t1 % 2, t2 % 2) == (1, 1, 0)
    assert (9 * n + 5) % 8 == 0 and t3 == (9 * n + 5) // 8 and t3 % 2 == 1
    return t3

def blockB_T(n):
    """Legal block B at odd n>=1: Syracuse exponents (2,2), parity word (1,0,1,0).
    Returns T^4(n) if legal, else None."""
    if n < 1 or n % 2 == 0 or v2(3 * n + 1) != 2:
        return None
    n1 = (3 * n + 1) // 4
    if v2(3 * n1 + 1) != 2:
        return None
    t = n; par = []
    for _ in range(4):
        par.append(t % 2); t = T(t)
    assert par == [1, 0, 1, 0]
    assert (9 * n + 7) % 16 == 0 and t == (9 * n + 7) // 16 and t % 2 == 1
    return t

BLK = {'A': blockA_T, 'B': blockB_T}
QC = {'A': (8, 3), 'B': (16, 0)}     # centered y-coordinates: q*y' = 9*y + c

def y_step(y, ch):
    q, c = QC[ch]
    num = 9 * y + c
    return num // q if num % q == 0 else None

def word_QPE(word):
    """Compose letters left-to-right: returns (Q,P,E) with Q*y_k = P*y_0 + E."""
    Q, P, E = 1, 1, 0
    for ch in word:
        q, c = QC[ch]
        Q, P, E = Q * q, 9 * P, 9 * E + c * Q
    return Q, P, E

def E_closed(word):
    """Closed formula: E = 3 * sum over A-positions j (1-indexed) of
    9^(k-j) * prod_{i<j} q_i."""
    k = len(word); tot = 0; pref = 1
    for j, ch in enumerate(word, start=1):
        if ch == 'A':
            tot += 3 * 9 ** (k - j) * pref
        pref *= QC[ch][0]
    return tot

# =====================================================================
print("== T1: chart validity (Step 0) ==")
# T1a: exact legality classes, n odd in [1, 400000].
badA = badB = 0; cntA = cntB = 0
for n in range(1, 400000, 2):
    la = blockA_T(n) is not None
    lb = blockB_T(n) is not None
    if la != (n % 16 == 11): badA += 1
    if lb != (n % 32 == 1):  badB += 1
    cntA += la; cntB += lb
    # h-chart equivalences: h=(n+5)/2, integrality of the h-map == legality
    h = (n + 5) // 2
    if la != ((9 * h) % 8 == 0): badA += 1
    if lb != ((9 * h + 21) % 16 == 0): badB += 1
check("T1a A-legality == (n=11 mod 16) == 8|h", badA == 0)
check("T1a B-legality == (n=1 mod 32) == (h=3 mod 16)", badB == 0)
print(f"T1a: scanned n odd < 400000: A legal at {cntA} points, B at {cntB}; "
      f"class mismatches: {badA + badB}.")

# T1b: word-level agreement between legal-T-composite and y-affine orbit,
# all words of length <= 4 (30 words), n odd < 100000.
words_le4 = [''.join(w) for k in range(1, 5) for w in iproduct('AB', repeat=k)]
n_agree = n_paths = 0; bad = 0
for n in range(1, 100000, 2):
    y0 = (n - 1) // 2
    for w in words_le4:
        nn, yy, ok_T, ok_y = n, y0, True, True
        for ch in w:
            r = BLK[ch](nn) if ok_T else None
            if r is None: ok_T = False
            else: nn = r
            if ok_y:
                ry = y_step(yy, ch)
                if ry is None: ok_y = False
                else: yy = ry
            if ok_T != ok_y:
                bad += 1; break
        else:
            if ok_T:
                n_paths += 1
                if nn == 2 * yy + 1: n_agree += 1
                else: bad += 1
check("T1b legality == integrality at every stage; values agree", bad == 0)
print(f"T1b: {len(words_le4)} words x 50000 seeds: {n_paths} fully legal paths, "
      f"{n_agree} value-agreements, {bad} mismatches.")

# T1c: unit-slope lift at length 6: for every word w (64), the class
# y = -E*P^{-1} mod Q gives a fully legal T-composite (top-level integrality
# forces all intermediate legality).  3 representatives each.
lift_ok = lift_bad = 0
for w in (''.join(t) for t in iproduct('AB', repeat=6)):
    Q, P, E = word_QPE(w)
    r = (-E * pow(P, -1, Q)) % Q
    for j in (0, 1, 2):
        y0 = r + j * Q
        n0 = 2 * y0 + 1
        nn, ok = n0, True
        for ch in w:
            nn = BLK[ch](nn)
            if nn is None: ok = False; break
        if ok and (P * y0 + E) % Q == 0 and nn == 2 * ((P * y0 + E) // Q) + 1:
            lift_ok += 1
        else:
            lift_bad += 1
check("T1c unit-slope lift: top-level class => fully legal composite", lift_bad == 0)
print(f"T1c: 64 length-6 words x 3 lifted seeds: {lift_ok} OK, {lift_bad} bad.")

# =====================================================================
print("== T2: macro algebra (Step 2) -- ALL orders for a+b <= 8 ==")
tested = 0; tie_packets = []
for k in range(1, 9):
    for a in range(0, k + 1):
        b = k - a
        Es = []
        for Apos in combinations(range(k), a):
            w = ''.join('A' if i in Apos else 'B' for i in range(k))
            Q, P, E = word_QPE(w)
            check(f"T2 Q order-indep {w}", Q == 8 ** a * 16 ** b)
            check(f"T2 P order-indep {w}", P == 9 ** k)
            check(f"T2 closed formula {w}", E == E_closed(w))
            check(f"T2 3|E {w}", E % 3 == 0)
            if a >= 1: check(f"T2 E>0 {w}", E > 0)
            else:      check(f"T2 E=0 all-B {w}", E == 0)
            # mod-9 rule (last letter) and mod-8 rule (first letter):
            if a >= 1:
                m9 = (3 * (-1) ** (a - 1)) % 9 if w[-1] == 'A' else 0
                check(f"T2 mod9 {w}", E % 9 == m9)
                check(f"T2 mod8 {w}", E % 8 == (3 if w[0] == 'A' else 0))
            # adjacent-swap identity:
            for j in range(k - 1):
                if w[j] == 'A' and w[j + 1] == 'B':
                    w2 = w[:j] + 'BA' + w[j + 2:]
                    pref = 1
                    for i in range(j): pref *= QC[w[i]][0]
                    dE = word_QPE(w2)[2] - E
                    check(f"T2 swap {w}@{j}", dE == 21 * 9 ** (k - j - 2) * pref)
            Es.append((E, w))
            tested += 1
        Es.sort()
        if a >= 1:
            check(f"T2 Emin ({a},{b})", Es[0] == (3 * 9 ** b * (9 ** a - 8 ** a),
                                                  'A' * a + 'B' * b))
            check(f"T2 Emax ({a},{b})", Es[-1] == (3 * 16 ** b * (9 ** a - 8 ** a),
                                                   'B' * b + 'A' * a))
            if len(Es) > 1:
                check(f"T2 Emin unique ({a},{b})", Es[0][0] < Es[1][0])
                check(f"T2 Emax unique ({a},{b})", Es[-2][0] < Es[-1][0])
            check(f"T2 mod21 const ({a},{b})",
                  len({e % 21 for e, _ in Es}) == 1)
        if len({e for e, _ in Es}) != len(Es):
            tie_packets.append((a, b))
check("T2 no E-ties observed (report only)", tie_packets == [])
q11, p11, es11 = 8 * 16, 81, sorted(word_QPE(w)[2] for w in ('AB', 'BA'))
check("T2 (1,1) constants {27,48}", es11 == [27, 48])
print(f"T2: {tested} words tested over all (a,b), a+b<=8; (1,1) constants {es11}; "
      f"E-tie packets: {tie_packets}.")

# =====================================================================
print("== T3: gate table (Step 3), exact, a<=8, b<=12 ==")
def gate(a, b):  # E_max < 3D, in the equivalent integer form
    return 9 ** a * (16 ** b + 9 ** b) < 2 * 8 ** a * 16 ** b
expected_b0 = {1: 1, 2: 1, 3: 2, 4: 3, 5: 4}
for a in range(1, 9):
    row = [gate(a, b) for b in range(1, 13)]
    # b-monotonicity within the table:
    check(f"T3 monotone a={a}", all(row[i] <= row[i + 1] for i in range(11)))
    if a <= 5:
        b0 = expected_b0[a]
        check(f"T3 row a={a}", row == [b + 1 >= b0 for b in range(12)])
    else:
        check(f"T3 row a={a} empty", not any(row))
    # gate == (E_max < 3D) with D = Q - P, and gate => Q > P:
    for b in range(1, 13):
        Q, P = 8 ** a * 16 ** b, 9 ** (a + b)
        Emax = 3 * 16 ** b * (9 ** a - 8 ** a)
        check(f"T3 equiv ({a},{b})", gate(a, b) == (Emax < 3 * (Q - P)))
        if gate(a, b): check(f"T3 gate=>contract ({a},{b})", Q > P)
check("T3 a=6 threshold: 9^6 > 2*8^6 iff 3^12 > 2^19",
      (9 ** 6 > 2 * 8 ** 6) and (3 ** 12 > 2 ** 19) and 9**6 - 2*8**6 == 3**12 - 2**19)
print("T3: rows verified: a=1,2: all b>=1; a=3: b>=2; a=4: b>=3; a=5: b>=4; "
      "a>=6: none (b<=12; all-b proof in file).  Failing pairs with a<=5: "
      "(3,1) (4,1) (4,2) (5,1) (5,2) (5,3).")

# =====================================================================
print("== T4: exceptional packets (Step 4) ==")
def packet(a, b):
    k = a + b
    Q, P = 8 ** a * 16 ** b, 9 ** k
    Es = sorted(word_QPE(''.join('A' if i in Apos else 'B' for i in range(k)))[2]
                for Apos in combinations(range(k), a))
    return Q, P, Q - P, Es

def targets(D, Q, Emax, g=3):
    """All values Dm+Qk <= Emax with m>=1, k>=0, g | (m+k)."""
    out = set()
    m = 1
    while D * m <= Emax:
        kk = 0
        while D * m + Q * kk <= Emax:
            if (m + kk) % g == 0:
                out.add(D * m + Q * kk)
            kk += 1
        m += 1
    return sorted(out)

def factor(n):
    f, p = [], 2
    while p * p <= n:
        while n % p == 0: f.append(p); n //= p
        p += 1
    if n > 1: f.append(n)
    return f

# ---- (3,1) ----
Q, P, D, Es = packet(3, 1)
W = Es[-1] - Es[0]
check("T4 (3,1) D", D == 8192 - 6561 == 1631 and factor(D) == [7, 233])
check("T4 (3,1) constants", Es == [5859, 7203, 8715, 10416])
check("T4 (3,1) W", W == 3 * (16 - 9) * (9 ** 3 - 8 ** 3) == 4557 and W < Q)
check("T4 (3,1) no D|E", all(E % D != 0 for E in Es))
t31 = targets(D, Q, Es[-1])
check("T4 (3,1) sieve targets", t31 == [3 * D, 6 * D] == [4893, 9786]
      and not set(t31) & set(Es))
print(f"T4 (3,1): Q={Q} P={P} D={D}={factor(D)}; constants {Es}; W={W}<Q; "
      f"E mod D = {[E % D for E in Es]}; sieve targets {t31} (no overlap).")

# ---- (4,1) ----
Q, P, D, Es = packet(4, 1)
W = Es[-1] - Es[0]
check("T4 (4,1) D", D == 65536 - 59049 == 6487 and factor(D) == [13, 499])
check("T4 (4,1) constants", Es == [66555, 77307, 89403, 103011, 118320])
check("T4 (4,1) W", W == 3 * 7 * (9 ** 4 - 8 ** 4) == 51765 and W < Q)
check("T4 (4,1) no D|E", all(E % D != 0 for E in Es))
t41 = targets(D, Q, Es[-1])
check("T4 (4,1) sieve targets no overlap", not set(t41) & set(Es))
print(f"T4 (4,1): Q={Q} P={P} D={D}={factor(D)}; constants {Es}; W={W}<Q; "
      f"E mod D = {[E % D for E in Es]}; {len(t41)} sieve targets, no overlap.")

# ---- (4,2) ----
Q, P, D, Es = packet(4, 2)
W = Es[-1] - Es[0]
check("T4 (4,2) D", D == 1048576 - 531441 == 517135)
check("T4 (4,2) count", len(Es) == 15 and Es[0] == 598995 and Es[-1] == 1893120)
# sharp collapse threshold (L-9923.1S / T-9924.3): W < P+Q even though W > Q
check("T4 (4,2) W window", W == 1294125 and Q < W < P + Q
      and (P + Q) - W == 285892)
check("T4 (4,2) no D|E", all(E % D != 0 for E in Es))
mults = [x for x in range(((Es[0] + D - 1) // D) * D, Es[-1] + 1, D)]
check("T4 (4,2) D-multiples in range", mults == [2 * D, 3 * D] == [1034270, 1551405])
check("T4 (4,2) mod7 kills multiples",
      all(E % 7 == 5 for E in Es) and (2 * D) % 7 == 6 and (3 * D) % 7 == 2)
t42 = targets(D, Q, Es[-1])
check("T4 (4,2) only target 3D", t42 == [3 * D] == [1551405])
check("T4 (4,2) no constant hits target", 1551405 not in Es)
print(f"T4 (4,2): Q={Q} P={P} D={D}={factor(D)}; 15 constants "
      f"[{Es[0]}..{Es[-1]}], all = 5 mod 7; W={W}: Q < W < P+Q = {P+Q} "
      f"(margin {P+Q-W}) -- collapse applies; D-multiples in range "
      f"{mults} are 6,2 mod 7 -- no fixed point; E mod D all nonzero; "
      f"second closure: sieve targets {t42}, 3D = 2 mod 7 -- eliminated.")

# ---- (5,2) ----
Q, P, D, Es = packet(5, 2)
check("T4 (5,2) D", D == 8388608 - 4782969 == 3605639)
check("T4 (5,2) count", len(Es) == 21 and Es[0] == 6386283 and Es[-1] == 20183808)
check("T4 (5,2) W beyond sharp threshold",           # collapse genuinely inapplicable
      Es[-1] - Es[0] == 13797525 and Es[-1] - Es[0] - (P + Q) == 625948)
t52 = targets(D, Q, Es[-1])
check("T4 (5,2) two targets", t52 == [3 * D, 2 * D + Q] == [10816917, 15599886])
check("T4 (5,2) targets mod 9", all(t % 9 == 6 for t in t52))
r9 = sorted({E % 9 for E in Es})
check("T4 (5,2) constants mod 9", r9 == [0, 3])
c0 = sum(E % 9 == 0 for E in Es); c3 = sum(E % 9 == 3 for E in Es)
check("T4 (5,2) mod-9 counts", (c0, c3) == (6, 15))
check("T4 (5,2) no overlap", not set(t52) & set(Es))
print(f"T4 (5,2): Q={Q} P={P} D={D}={factor(D)}; 21 constants "
      f"[{Es[0]}..{Es[-1]}]; targets {t52} = 6 mod 9; constants mod 9: "
      f"{c0} are 0, {c3} are 3 -- eliminated.  (D+2Q = {D + 2 * Q} > Emax "
      f"by {D + 2 * Q - Es[-1]}.)")

# ---- (5,3) ----
Q, P, D, Es = packet(5, 3)
check("T4 (5,3) D", D == 134217728 - 43046721 == 91171007)
check("T4 (5,3) count", len(Es) == 56 and Es[0] == 57476547 and Es[-1] == 322940928)
check("T4 (5,3) W beyond sharp threshold",           # collapse genuinely inapplicable
      Es[-1] - Es[0] == 265464381 and Es[-1] - Es[0] - (P + Q) == 88199932)
t53 = targets(D, Q, Es[-1])
check("T4 (5,3) two targets", t53 == [3 * D, 2 * D + Q] == [273513021, 316559742])
check("T4 (5,3) targets mod 8", [t % 8 for t in t53] == [5, 6])
r8 = sorted({E % 8 for E in Es})
check("T4 (5,3) constants mod 8", r8 == [0, 3])
c0 = sum(E % 8 == 0 for E in Es); c3 = sum(E % 8 == 3 for E in Es)
check("T4 (5,3) mod-8 counts", (c0, c3) == (21, 35))
check("T4 (5,3) no overlap", not set(t53) & set(Es))
print(f"T4 (5,3): Q={Q} P={P} D={D}={factor(D)}; 56 constants "
      f"[{Es[0]}..{Es[-1]}]; targets {t53} = 5,6 mod 8; constants mod 8: "
      f"{c0} are 0, {c3} are 3 -- eliminated.")

# ---- (5,1) ----
Q, P, D, Es = packet(5, 1)
check("T4 (5,1) supercritical", Q == 2 ** 19 == 524288 and P == 3 ** 12 == 531441
      and Q < P and P - Q == 7153 and factor(7153) == [23, 311])
check("T4 (5,1) six constants",
      Es == [709587, 795603, 892371, 1001235, 1123707, 1261488])
check("T4 (5,1) closed form E(p)",
      sorted(21 * 9 ** (6 - p) * 8 ** (p - 1) + 21459 for p in range(1, 7)) == Es)
check("T4 (5,1) distinct mod Q", len({E % Q for E in Es}) == 6)
print(f"T4 (5,1): Q=2^19={Q} < P=3^12={P}; P-Q=7153=23*311; constants {Es}; "
      f"E(p)=21*9^(6-p)*8^(p-1)+21459 verified; distinct mod Q (deterministic).")

# =====================================================================
print("== T5: brute-force integral cycle searches (Step 4/5) ==")
def confined_graph_cycles(a, b, lo=None, hi=None):
    """Exhaustive cycle detection.  For contracting packets any integral cycle
    lies in [ceil(Emin/D), floor(Emax/D)] (T-9924.4a); searching that node set
    with all branch edges is complete for ALL integral cycles."""
    Q, P, D, Es = packet(a, b)
    if lo is None:
        lo, hi = ceildiv(Es[0], D), Es[-1] // D
    adj = {}
    for y in range(lo, hi + 1):
        succ = [(P * y + E) // Q for E in Es if (P * y + E) % Q == 0
                and lo <= (P * y + E) // Q <= hi]
        adj[y] = succ
    # DFS 3-colour cycle detection
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {y: WHITE for y in adj}
    found = []
    def dfs(u, stack):
        colour[u] = GREY; stack.append(u)
        for v in adj[u]:
            if colour[v] == GREY:
                found.append(stack[stack.index(v):] + [v])
            elif colour[v] == WHITE:
                dfs(v, stack)
        stack.pop(); colour[u] = BLACK
    for y in adj:
        if colour[y] == WHITE:
            dfs(y, [])
    n_edges = sum(len(s) for s in adj.values())
    return (lo, hi, n_edges, found)

for (a, b) in [(1, 1), (2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (5, 2), (5, 3)]:
    lo, hi, ne, cyc = confined_graph_cycles(a, b)
    check(f"T5 confined ({a},{b}) no cycles", cyc == [])
    print(f"T5 confined ({a},{b}): nodes [{lo},{hi}], {ne} edges, cycles: {len(cyc)}.")

# raw window search (adversarial, includes negatives; completeness follows from
# the confinement bound, which the window contains):
for (a, b, B) in [(3, 1, 50000), (4, 2, 50000)]:
    Q, P, D, Es = packet(a, b)
    lo, hi = -B, B
    adj = {}
    edges = 0
    for y in range(lo, hi + 1):
        succ = [(P * y + E) // Q for E in Es if (P * y + E) % Q == 0]
        succ = [s for s in succ if lo <= s <= hi]
        if succ:
            adj[y] = succ; edges += len(succ)
    # detect any cycle
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {y: WHITE for y in adj}
    found = []
    def dfs2(u, stack):
        colour[u] = GREY; stack.append(u)
        for v in adj.get(u, []):
            if v in colour:
                if colour[v] == GREY: found.append(v)
                elif colour[v] == WHITE: dfs2(v, stack)
        stack.pop(); colour[u] = BLACK
    for y in list(adj):
        if colour[y] == WHITE: dfs2(y, [])
    check(f"T5 raw window ({a},{b})", found == [])
    print(f"T5 raw window ({a},{b}), y in [-{B},{B}]: {edges} edges, cycles: {len(found)}.")

# word-length-bounded cycle-equation search: (Q^R - P^R) y0 = sum P^(R-1-t) Q^t E_t
def cycle_eq_solutions(a, b, Rmax):
    Q, P, D, Es = packet(a, b)
    sols = []
    for R in range(1, Rmax + 1):
        lhs = Q ** R - P ** R
        for seq in iproduct(Es, repeat=R):
            C = sum(P ** (R - 1 - t) * Q ** t * seq[t] for t in range(R))
            if C % lhs == 0:
                sols.append((R, seq, C // lhs))
    return sols

for (a, b, Rmax) in [(3, 1, 6), (4, 1, 5), (4, 2, 3), (5, 2, 3), (5, 3, 2)]:
    sols = cycle_eq_solutions(a, b, Rmax)
    check(f"T5 cycle-eq ({a},{b}) R<={Rmax}", sols == [])
    print(f"T5 cycle-eq ({a},{b}), R<={Rmax}: {sum(len(packet(a,b)[3])**R for R in range(1,Rmax+1))} "
          f"sequences, integral solutions: {len(sols)}.")
sols51 = cycle_eq_solutions(5, 1, 5)
check("T5 (5,1) no y0>=0 solutions", all(y < 0 for (_, _, y) in sols51))
print(f"T5 cycle-eq (5,1), R<=5: 9330 sequences, integral solutions: {len(sols51)} "
      f"(all would need y0<0; none with y0>=0).")
# all-B packet: (16^R - 9^R) y = 0 with 16^R != 9^R forces y = 0; and y=0 is
# genuinely a fixed point (16*0 = 9*0), physical n = 2*0+1 = 1:
check("T5 all-B", all(16 ** R != 9 ** R for R in range(1, 9))
      and y_step(0, 'B') == 0 and blockB_T(1) == 1)
print("T5 all-B (a=0): 16^R y = 9^R y forces y=0 (R<=8 checked, all-R in file); "
      "y=0 <-> n=1 is a legal fixed point of block B (T-run verified).")

# =====================================================================
print("== T6: inline lemma checks on synthetic systems ==")
# T6a: narrow-alphabet collapse at the SHARP threshold (T-9924.3 = L-9923.1S):
# random contracting systems with W < P + Q (probing also the extension regime
# Q <= W < P+Q that the source spec's W < Q missed) -- every integral cycle
# must be a one-step fixed point y* with D*y* in the constant alphabet.
n_sys = n_fp = n_wide = 0
for trial in range(300):
    Qs = random.randint(20, 2000)
    Ps = random.randint(1, Qs - 1)
    Ds = Qs - Ps
    s = random.randint(1, 5)
    Cmin = random.randint(-2 * Qs, 2 * Qs)
    Ws = 0 if s == 1 else random.randint(s - 1, Ps + Qs - 1)  # s-1 <= W < P+Q
    n_wide += (Ws >= Qs)
    Cs = {Cmin, Cmin + Ws}
    while len(Cs) < s:
        Cs.add(Cmin + random.randint(0, Ws))
    Cs = sorted(Cs)
    lo, hi = ceildiv(Cs[0], Ds), Cs[-1] // Ds
    adj = {y: [(Ps * y + C) // Qs for C in Cs
               if (Ps * y + C) % Qs == 0 and lo <= (Ps * y + C) // Qs <= hi]
           for y in range(lo, hi + 1)}
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {y: WHITE for y in adj}
    cyc_found = []
    def dfs6(u, stack):
        colour[u] = GREY; stack.append(u)
        for v in adj[u]:
            if colour[v] == GREY:
                cyc_found.append(stack[stack.index(v):] + [v])
            elif colour[v] == WHITE:
                dfs6(v, stack)
        stack.pop(); colour[u] = BLACK
    for y in adj:
        if colour[y] == WHITE:
            dfs6(y, [])
    ok = True
    for cy in cyc_found:            # collapse: every cycle is a self-loop y->y
        states = set(cy)            # with D*y equal to a constant
        if len(states) != 1: ok = False
        y = cy[0]
        if Ds * y not in Cs: ok = False
        n_fp += 1
    check(f"T6a collapse trial {trial}", ok)
    n_sys += 1
print(f"T6a: {n_sys} random contracting systems with W < P+Q ({n_wide} of them "
      f"in the extension regime Q <= W < P+Q): every integral cycle found is a "
      f"one-step fixed point with D*y in the alphabet "
      f"({n_fp} fixed points seen, 0 moving cycles).")
# T6a': SHARPNESS at W = P+Q: Q=3, P=2, C={0,5} (= {-P,Q} shifted by +2, D=1)
# has the genuine moving cycle 3 -> 2 -> 3; and the 2-cycle identity
# (P+Q)(y1-y0) = C_first - C_second holds (L-9923.1S(iv) / T-9924.3 remark).
c1 = (2 * 3 + 0) % 3 == 0 and (2 * 3 + 0) // 3 == 2
c2 = (2 * 2 + 5) % 3 == 0 and (2 * 2 + 5) // 3 == 3
check("T6a' sharpness witness", c1 and c2 and 5 - 0 == (2 + 3) * (3 - 2))
print("T6a': Q=3,P=2,C={0,5} (W=5=P+Q exactly): moving cycle 3->2->3 exists, "
      "and C_+-C_- = (P+Q)*(step) -- the threshold W < P+Q is sharp.")
# T6a'': width EXACTLY Q carries no moving cycle (refutes the source spec's
# W = Q sharpness claim; the regime Q <= W < P+Q still collapses):
for trial in range(100):
    Qs = random.randint(5, 400)
    Ps = random.randint(1, Qs - 1)
    Ds = Qs - Ps
    base = random.randint(-2 * Qs, 2 * Qs)
    Cs = [base, base + Qs]                       # width exactly Q < P+Q
    lo, hi = ceildiv(Cs[0], Ds), Cs[-1] // Ds
    moving = False
    for y in range(lo, hi + 1):
        for C in Cs:
            if (Ps * y + C) % Qs == 0:
                y2 = (Ps * y + C) // Qs
                if y2 != y and lo <= y2 <= hi:
                    # a moving edge inside the box could only close via a cycle;
                    # follow it exhaustively (box is tiny)
                    seen = {y2}; frontier = {y2}
                    while frontier:
                        nxt = set()
                        for u in frontier:
                            for C2 in Cs:
                                if (Ps * u + C2) % Qs == 0:
                                    v = (Ps * u + C2) // Qs
                                    if lo <= v <= hi: nxt.add(v)
                        if y in nxt: moving = True
                        frontier = nxt - seen; seen |= nxt
    check(f"T6a'' width-Q trial {trial}", not moving)
print("T6a'': 100 random alphabets of width exactly Q: no moving cycle "
      "(the old W = Q sharpness claim is indeed impossible for P >= 1).")

# T6b: cycle-minimum sieve (T-9924.4 = L-9923.2) with g=3: random contracting
# systems, 3|P, gcd(3,Q)=1, all constants positive multiples of 3, Emax < 3D:
# no integral cycle at all (positivity is automatic).
n_sys = 0
for trial in range(300):
    while True:
        Qs = random.randint(30, 3000)
        if Qs % 3 != 0: break
    Ps = 3 * random.randint(1, (Qs - 1) // 3)
    Ds = Qs - Ps
    if 3 * Ds <= 3: continue
    s = random.randint(1, 5)
    Cs = sorted({3 * random.randint(1, (3 * Ds - 1) // 3) for _ in range(s)})
    lo, hi = ceildiv(Cs[0], Ds), Cs[-1] // Ds
    ok = True
    for y in range(lo, hi + 1):
        for C in Cs:
            if (Ps * y + C) % Qs == 0 and lo <= (Ps * y + C) // Qs <= hi:
                # sieve says NO closed structure can exist; even edges back into
                # the box must not close.  Deep-check: no cycle through y.
                seen, frontier = set(), {y}
                for _ in range(hi - lo + 2):
                    nxt = set()
                    for u in frontier:
                        for C2 in Cs:
                            if (Ps * u + C2) % Qs == 0:
                                v = (Ps * u + C2) // Qs
                                if lo <= v <= hi: nxt.add(v)
                    if y in nxt: ok = False
                    frontier = nxt - seen; seen |= nxt
                    if not frontier: break
    check(f"T6b sieve trial {trial}", ok)
    n_sys += 1
print(f"T6b: {n_sys} random systems with 3|P, 3|C, gcd(3,Q)=1, Emax<3D: "
      f"no integral cycles found (matches the sieve gate).")

# =====================================================================
print("== T7: (5,1) == six-branch chart of L-9916/X-9902 ==")
Q, P, D, Es = packet(5, 1)
ALPHA = [7 * 3 ** (2 * i) * 2 ** (15 - 3 * i) for i in range(6)]
check("T7 alphabet", ALPHA == [229376, 258048, 290304, 326592, 367416, 413343])
# digit-ladder identity and exact bijection E(p) = 3*(alpha_{6-p} + 7153):
for i in range(6):
    p = 6 - i
    Ep = word_QPE('A' * (p - 1) + 'B' + 'A' * (6 - p))[2]
    check(f"T7 ladder i={i}", 21 * 9 ** i * 8 ** (5 - i) + 21459 == 3 * (ALPHA[i] + 7153)
          and Ep == 3 * (ALPHA[i] + 7153))
check("T7 set equality", sorted(3 * (al + 7153) for al in ALPHA) == Es)
# dynamics: chart step at legal x  <->  macro step at y = 3(x-1):
Pinv = pow(P, -1, Q)
n_dyn = 0
m1_candidates = []
for i, al in enumerate(ALPHA):
    r = (-al * Pinv) % Q
    m1_candidates.append(r if r > 0 else r + Q)
    for j in range(4):
        x = r + j * Q
        if x <= 0: continue
        xp = ceildiv(P * x, Q)
        check(f"T7 digit x={x}", Q * xp - P * x == al)
        y = 3 * (x - 1)
        legal = [E for E in Es if (P * y + E) % Q == 0]
        check(f"T7 unique branch x={x}", legal == [3 * (al + 7153)])
        yp = (P * y + legal[0]) // Q
        check(f"T7 conjugacy x={x}", yp == 3 * (xp - 1))
        # full physical run: n = 6x-5 through the letter word (B at p=6-i):
        wrd = 'A' * (5 - i) + 'B' + 'A' * i
        nn = 6 * x - 5
        for ch in wrd:
            nn = BLK[ch](nn)
            if nn is None: break
        check(f"T7 physical x={x}", nn == 6 * xp - 5)
        n_dyn += 1
check("T7 m_1 = 6472 (X-9902)", min(m1_candidates) == 6472)
m16 = 4629285799073801695890071893291563216294381998435632568233291338101143197194568
print(f"T7: ladder identity + bijection E=3(alpha+7153) verified; {n_dyn} dynamic "
      f"conjugacy checks (chart digit / unique branch / y'=3(x'-1) / physical "
      f"T-run at n=6x-5) all pass; min class rep = {min(m1_candidates)} = m_1.")
print(f"T7: physical floor from X-9902 (EMPIRICAL): all-time (5,1)-roots have "
      f"n = 6x-5 > 6*m_16 - 5 = {6 * m16 - 5}")

print("RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-26, CPython 3, Linux; pasted byte-for-byte from the
run and re-diffed against the live run before commit):**

```text
== T1: chart validity (Step 0) ==
T1a: scanned n odd < 400000: A legal at 25000 points, B at 12500; class mismatches: 0.
T1b: 30 words x 50000 seeds: 11520 fully legal paths, 11520 value-agreements, 0 mismatches.
T1c: 64 length-6 words x 3 lifted seeds: 192 OK, 0 bad.
== T2: macro algebra (Step 2) -- ALL orders for a+b <= 8 ==
T2: 510 words tested over all (a,b), a+b<=8; (1,1) constants [27, 48]; E-tie packets: [].
== T3: gate table (Step 3), exact, a<=8, b<=12 ==
T3: rows verified: a=1,2: all b>=1; a=3: b>=2; a=4: b>=3; a=5: b>=4; a>=6: none (b<=12; all-b proof in file).  Failing pairs with a<=5: (3,1) (4,1) (4,2) (5,1) (5,2) (5,3).
== T4: exceptional packets (Step 4) ==
T4 (3,1): Q=8192 P=6561 D=1631=[7, 233]; constants [5859, 7203, 8715, 10416]; W=4557<Q; E mod D = [966, 679, 560, 630]; sieve targets [4893, 9786] (no overlap).
T4 (4,1): Q=65536 P=59049 D=6487=[13, 499]; constants [66555, 77307, 89403, 103011, 118320]; W=51765<Q; E mod D = [1685, 5950, 5072, 5706, 1554]; 9 sieve targets, no overlap.
T4 (4,2): Q=1048576 P=531441 D=517135=[5, 59, 1753]; 15 constants [598995..1893120], all = 5 mod 7; W=1294125: Q < W < P+Q = 1580017 (margin 285892) -- collapse applies; D-multiples in range [1034270, 1551405] are 6,2 mod 7 -- no fixed point; E mod D all nonzero; second closure: sieve targets [1551405], 3D = 2 mod 7 -- eliminated.
T4 (5,2): Q=8388608 P=4782969 D=3605639=[79, 45641]; 21 constants [6386283..20183808]; targets [10816917, 15599886] = 6 mod 9; constants mod 9: 6 are 0, 15 are 3 -- eliminated.  (D+2Q = 20382855 > Emax by 199047.)
T4 (5,3): Q=134217728 P=43046721 D=91171007=[257, 354751]; 56 constants [57476547..322940928]; targets [273513021, 316559742] = 5,6 mod 8; constants mod 8: 21 are 0, 35 are 3 -- eliminated.
T4 (5,1): Q=2^19=524288 < P=3^12=531441; P-Q=7153=23*311; constants [709587, 795603, 892371, 1001235, 1123707, 1261488]; E(p)=21*9^(6-p)*8^(p-1)+21459 verified; distinct mod Q (deterministic).
== T5: brute-force integral cycle searches (Step 4/5) ==
T5 confined (1,1): nodes [1,1], 0 edges, cycles: 0.
T5 confined (2,1): nodes [2,2], 0 edges, cycles: 0.
T5 confined (3,1): nodes [4,6], 0 edges, cycles: 0.
T5 confined (3,2): nodes [1,2], 0 edges, cycles: 0.
T5 confined (4,1): nodes [11,18], 0 edges, cycles: 0.
T5 confined (4,2): nodes [2,3], 0 edges, cycles: 0.
T5 confined (5,2): nodes [2,5], 0 edges, cycles: 0.
T5 confined (5,3): nodes [1,3], 0 edges, cycles: 0.
T5 raw window (3,1), y in [-50000,50000]: 48 edges, cycles: 0.
T5 raw window (4,2), y in [-50000,50000]: 4 edges, cycles: 0.
T5 cycle-eq (3,1), R<=6: 5460 sequences, integral solutions: 0.
T5 cycle-eq (4,1), R<=5: 3905 sequences, integral solutions: 0.
T5 cycle-eq (4,2), R<=3: 3615 sequences, integral solutions: 0.
T5 cycle-eq (5,2), R<=3: 9723 sequences, integral solutions: 0.
T5 cycle-eq (5,3), R<=2: 3192 sequences, integral solutions: 0.
T5 cycle-eq (5,1), R<=5: 9330 sequences, integral solutions: 0 (all would need y0<0; none with y0>=0).
T5 all-B (a=0): 16^R y = 9^R y forces y=0 (R<=8 checked, all-R in file); y=0 <-> n=1 is a legal fixed point of block B (T-run verified).
== T6: inline lemma checks on synthetic systems ==
T6a: 300 random contracting systems with W < P+Q (84 of them in the extension regime Q <= W < P+Q): every integral cycle found is a one-step fixed point with D*y in the alphabet (18 fixed points seen, 0 moving cycles).
T6a': Q=3,P=2,C={0,5} (W=5=P+Q exactly): moving cycle 3->2->3 exists, and C_+-C_- = (P+Q)*(step) -- the threshold W < P+Q is sharp.
T6a'': 100 random alphabets of width exactly Q: no moving cycle (the old W = Q sharpness claim is indeed impossible for P >= 1).
T6b: 298 random systems with 3|P, 3|C, gcd(3,Q)=1, Emax<3D: no integral cycles found (matches the sieve gate).
== T7: (5,1) == six-branch chart of L-9916/X-9902 ==
T7: ladder identity + bijection E=3(alpha+7153) verified; 24 dynamic conjugacy checks (chart digit / unique branch / y'=3(x'-1) / physical T-run at n=6x-5) all pass; min class rep = 6472 = m_1.
T7: physical floor from X-9902 (EMPIRICAL): all-time (5,1)-roots have n = 6x-5 > 6*m_16 - 5 = 27775714794442810175340431359749379297766291990613795409399748028606859183167403
RESULT: ALL CHECKS PASSED
```

## Remaining uncertainty

The author asserts all sub-claims T-9924.1–.8 as fully proved (with the EMPIRICAL
label on T-9924.8 C2 and the worked $m_1$ instance). Points a verifier should probe
hardest:

1. **The target enumerations (Step 4(iii)–(v)).** Their completeness rests on two
   monotonicity observations (values increase in $k$ within $m + k = 3$ because
   $Q > D$; $m + k \ge 6$ forces $\ge 6D$ because $Q > D$) plus displayed margins.
   Re-derive independently; the margins make each a single subtraction.
2. **Index bookkeeping in Step 2** (the constant formula $E_w = 3\sum 9^{k-j}Q_{<j}$
   and the swap identity's claim that *later* prefix products are unchanged): T2
   checks this exhaustively for $a+b \le 8$, but a hand check of, say,
   $\mathsf{ABAA}$ in $(3,1)$ is the real verification.
3. **The mod-9 rule's sign** $3(-1)^{a-1}$ (T-9924.2): only the parity of $a$
   enters the $(5,2)$ closure ($a = 5$ odd $\Rightarrow$ residue 3); T2 verifies the
   rule for all tested words, but confirm the derivation $8 \equiv -1, 16 \equiv 1
   \pmod 3$.
4. **The sieve's anchor step** (T-9924.4(b)): that $\kappa \ge 0$ needs only
   "successor of a minimum is $\ge$ the minimum", and the congruence step needs
   $D \equiv Q \pmod g$; both are one-liners but they carry the whole gate.
5. **Companion-file status:** L-9923 landed while this file was being drafted and
   the citations here use its final numbering (.1/.1C/.1S/.2/.3), but its status
   was still PROPOSED (verifier running) at the time of writing; this file's
   correctness is unaffected either way — the inline proofs are self-contained —
   yet a verifier should confirm the pointers still match the reviewed L-9923.
   Extra care spot: the sharp-threshold proof (Step 3a, items 2–3): the
   walk-backwards existence of a strictly-below (resp. strictly-above) entering
   edge is where "moving" is used; check no off-by-one in $y_s \le M - 1$.
6. **What is *not* claimed:** no statement about entirely negative supercritical
   cycles, about $a \ge 6$ contracting packets, or about any dynamics outside the
   two-letter grammar; and C2's floor is empirical, inheriting X-9902's status.

## Suggested next attack

- **The first open packet $(6,2)$** ($Q = 2^{26} = 67108864$, $P = 9^8 = 43046721$,
  $D = 24062143$, $E_{\max} = 768\cdot(9^6 - 8^6) = 206820096 \approx 8.6\,D$): the
  gate fails and $W = 525\cdot269297 = 141380925 > P + Q = 110155585$, so even the
  sharp collapse threshold does not reach it; but T-9924.4(e) still yields a finite
  target set ($m + k \in \{3, 6\}$, five members), and the packet has
  $\binom{8}{2} = 28$ constants; a bespoke residue system (mod 7/9/8 as here, or
  mod small primes of $D$) might close it and, iterated, extend the theorem to a
  $\le 6$-pulse family. The mod-21 rigidity (all constants congruent) is the most
  promising lever.
- **Negative-cycle closure for $(5,1)$:** extend the T5 search or find an algebraic
  obstruction (the constants are $\not\equiv 0 \bmod 23$ and $311$?) to prove even
  negative integral cycles absent, tying off the one deliberate weakening.
- **Port to other block pairs** (L-9922 program): the entire Step 2–4 machinery used
  only $(q_\mathsf{A}, c_\mathsf{A}) = (8,3)$, $(q_\mathsf{B}, c_\mathsf{B}) =
  (16,0)$ through the derived constants; re-run it for other exponent pairs (e.g.
  exponents $(1,1)$/$(2,2)$ blocks) to map which grammars are cycle-free by the same
  three tools.
- **The extraction frontier:** the only surviving $(5,1)$ question is issue #58's
  $m_N$ dichotomy; L-9916.5/Q-9916 already show generic equidistribution cannot
  decide it — the dictionary here adds that any decision transfers verbatim to the
  pulse grammar at $n = 6x - 5$.

---
*File authored by fable-02-p18, 2026-07-26, as the 99xx packet's independent
reconstruction of the owner-supplied draft T-9608 (PR #47 program), with provenance
credit as stated. Status PROPOSED per NOTATION.md conventions; an independent
reviewing agent may upgrade after verification.*

---

## Verification note (fable-02-v26, 2026-07-26)

**Verdict: PASS.** Independent adversarial review per README §13, conducted
without reliance on the author's confidence or code: every sub-claim
T-9924.1–.8 was restated and re-derived from NOTATION.md and the file's inline
arguments alone; every quantifier and boundary case audited; all numerical
content recomputed from scratch with independently written exact-integer code
(structure deliberately different from the embedded tests, larger ranges); the
embedded test block audited byte-for-byte. **No substantive gap found; the
first unsupported inference (README §13.9) does not exist in the main theorem
or its proof.** One quantifier imprecision in the EMPIRICAL cross-reference C2
(Step 6) was found and fixed in place, flagged as a reviewer's clarification
(§V.3); it touches no theorem. Status upgraded PROPOSED → PROVED and this
reviewer recorded in the header. Per README §7 the file is **not** marked
INDEPENDENTLY_VERIFIED — that requires a further reviewer beyond this first
independent review.

### V.1 Proof reconstruction (§13.2–.3, .6–.8)

- **Step 0 (chart validity).** All coordinate translations re-derived by hand
  ($8h' = 9h \Leftrightarrow 8n' = 9n+5$; $16h' = 9h+21 \Leftrightarrow 16n' =
  9n+7$; centering $8y' = 9y+3$, $16y' = 9y$; $n = 2y+1$). Both legality chains
  recomputed exactly: $\nu_2(3n{+}1) = 1 \wedge \nu_2(3n_1{+}1) = 2
  \Leftrightarrow n \equiv 11 \ (16) \Leftrightarrow 8 \mid h \Leftrightarrow
  y \equiv 5\ (8)$, and the $\mathsf{B}$-chain to $n \equiv 1\ (32)
  \Leftrightarrow h \equiv 3\ (16) \Leftrightarrow 16 \mid y$. Legality $=$
  integrality re-proved in both directions, letterwise and wordwise, including
  oddness/positivity of all intermediates; the unit-slope-lift identity
  $9^k y_0 + E_k = 9^{k-j}(9^j y_0 + E_j) + Q_j E_s$ re-derived from the
  coherence formula, with the 2-power/odd coprimality step checked. *Reading
  note (no error):* the gloss "three $T$-steps with parity word $(1,1,0)$"
  describes the legal composite; the parity word alone characterizes the
  strictly larger class $n \equiv 3 \pmod 8$ (the exact second valuation cuts
  it to $n \equiv 11 \pmod{16}$). The file defines legality by valuations and
  derives the parity word, never the converse, so nothing is affected; my scan
  quantified it (odd $n < 2\cdot10^6$: 250000 states carry $(1,1,0)$, exactly
  the 125000 with $n \equiv 11 \bmod 16$ are legal). Same structure for
  $\mathsf{B}$.
- **Step 2 (macro algebra).** Composition induction, closed constant formula
  (hand-checked $\mathsf{ABAA} \mapsto 3(729 + 1152 + 1024) = 8715$), swap
  identity (positions $> j{+}1$ unchanged because their prefix products contain
  $q_\mathsf{A}q_\mathsf{B} = 128$ in either order), extremal chain with
  uniqueness, telescoping evaluations, and all congruence rules re-derived —
  including the flagged mod-9 sign: a last-$\mathsf{A}$ word has $E \equiv
  3\cdot8^{a-1}16^b \pmod 9$, and $8 \equiv -1$, $16 \equiv 1 \pmod 3$ give
  $3(-1)^{a-1}$; at $a = 5$ this is $3$, exactly what the $(5,2)$ closure
  consumes.
- **Steps 3a/3b (inline lemmas).** Sharp-threshold collapse re-proved; the
  walk-backwards edge existence checked for the off-by-one the author flagged
  (integer states make "strictly below $M$" $=$ "$\le M - 1$"; the minimal
  back-step argument handles runs of maxima); moving cycles force $W \ge
  D(M-\mu) + 2P \ge P + Q$. Sharpness witness $\{Q, -P\}$ and its $+2$ shift
  to $\{0,5\}$ at $D = 1$ verified, as is the impossibility of the source
  spec's $W = Q$ example. Sieve re-proved: $\kappa \ge 0$ from
  successor-of-minimum $\ge$ minimum, $D \equiv Q \pmod g$, and the point
  where $Q > D$ (i.e. $P \ge 1$) enters $E \ge D(\mu + \kappa)$ is present in
  Step 3b(3). The companion L-9923 has meanwhile been upgraded to PROVED
  (fable-02-v25); cited numbering .1/.1C/.1S/.2/.3(ii) matches the landed
  text, and the inline re-proofs keep this file self-contained as claimed.
- **Step 3c (gate).** The equivalence $E_{\max} < 3D \Leftrightarrow G(a,b)$
  is sign-free algebra (re-derived); $G \Rightarrow Q > P$, $b$-monotonicity,
  and the $a \ge 6$ kill re-derived. The claimed identity of frontiers
  reconstructed: $9^6 = 3^{12}$ and $2\cdot8^6 = 2^{19} = 8^5\cdot16 =
  Q_{5,1}$, so the gate's $a$-cutoff and $(5,1)$-supercriticality are
  literally the same integer inequality $3^{12} > 2^{19}$, margin $7153$.
- **Step 4 (packets).** All six closures re-derived; $(4,2)$ checked through
  both routes; the $(5,1)$ sign argument re-proved via the unrolled cycle
  equation with rotation anchoring (strict positivity of the constants also
  excludes $y_t = 0$, as claimed).
- **Step 5 and corollaries.** The quantifier audit is correct: the lemmas
  quantify over arbitrary constant sequences from the complete alphabet,
  which is exactly "arbitrary branch order at each macro, arbitrary length,
  arbitrary repetition"; no least-period or distinctness assumptions. The
  beyond-spec strengthening "no integral cycle of any sign" checked per case:
  gate packets and $(5,2)/(5,3)$ via automatic positivity (edge into the
  minimum gives $D\mu \ge E_{\min} \ge 1$); $(3,1)/(4,1)/(4,2)$ via the
  sign-free collapse. Corollary 2's case split audited, including the
  correctly excluded per-period totals $\alpha \ge 6$ (e.g. a
  $(2,1){+}(4,1)$ macro mixture lands on totals $(6,2)$ and is *not*
  claimed — the Honest scope box's qualifier is accurate).
- **Step 6 (correspondence).** The dictionary re-derived in both directions
  ($Q\cdot3(x'{-}1) = P\cdot3(x{-}1) + 3(\alpha + P - Q)$); the only true
  import, digit uniqueness in $[0,Q)$, checked against L-9916.1(1) (PROVED);
  distinctness mod $Q$ via $\nu_2(E(p) - E(p')) = 3(p-1) \le 12 < 19$
  re-derived. The $3 \mid y$ bookkeeping at the seed is where §V.3 applies.
- **Dependency and Gap audits:** spot-checked and accurate; citation
  structure acyclic; X-9902 material confined to EMPIRICAL positions.

### V.2 Independent computation (own code; exact integers only)

Script `scratchpad/v26_verify.py` (session-local, written from scratch). All
checks passed:

1. **Chart:** legality biconditionals (valuation definition vs. mod-16/32 vs.
   $h$- and $y$-integrality) for all odd $n < 2\cdot10^6$; word legality $=$
   orbit integrality with value agreement for all 62 words of length $\le 5$
   at $10^5$ odd seeds; unit-slope lift at length 7 (all 128 words).
2. **Algebra:** all 1022 words with $a + b \le 9$ (file: $\le 8$): $(Q,P)$
   invariance, closed formula, extrema with uniqueness, $W$ formula, swap
   identity, and the mod-21/9/8/7 rules exact.
3. **Gate:** full table $a \le 10$, $b \le 14$ against the claimed rows; all
   11 displayed boundary integers digit-exact; monotonicity; cutoff identity.
4. **Packets:** every constant list regenerated (counts 4/5/15/21/56/6); every
   factorization confirmed ($1631 = 7\cdot233$, $6487 = 13\cdot499$, $517135 =
   5\cdot59\cdot1753$, $3605639 = 79\cdot45641$, $91171007 = 257\cdot354751$,
   $7153 = 23\cdot311$); every $W$-window and displayed margin digit-exact.
   **Target-set completeness** (the author's probe spot 1) verified by
   exhaustive double loop over all $(m, k)$ with $Dm + Qk \le E_{\max}$, no
   monotonicity shortcuts: $(3,1)$: $\{3D, 6D\}$; $(4,1)$: the nine listed;
   $(4,2)$: $\{3D\}$ only; $(5,2)$ and $(5,3)$: $\{3D, 2D{+}Q\}$ — exactly as
   claimed; all residue verdicts and the counts $6{+}15$ (mod 9) and $21{+}35$
   (mod 8) reproduced.
5. **Cycle hunts (must find none; found none):** confined-interval exhaustive
   searches for $(1,1), (2,1), (3,1), (3,2), (4,1), (4,2), (5,2), (5,3)$ —
   every confinement box carries **zero** integral macro edges, even before
   the landing restriction; raw windows $|y| \le 6\cdot10^4$ (resp.
   $3\cdot10^4$) including negatives for $(3,1), (4,1), (4,2), (5,2), (5,3),
   (5,1)$; cycle-equation enumeration over all constant sequences at the
   file's $R$-bounds — zero integral solutions everywhere, including $(5,1)$
   to $R = 5$ with negative $y_0$ allowed.
6. **Correspondence:** alphabet, bijection $E = 3(\alpha_i + 7153)$ with
   $p = 6 - i$, distinctness mod $Q$; 18 dynamic conjugacy instances (chart
   digit, unique integral branch, $y' = 3(x'-1)$, physical $T$-run at
   $n = 6x-5$); $m_1 = 6472$ reproduced by independent brute scan; $n = 38827$
   iterated directly under $T$: 19 steps, parity word $(110)(1010)(110)^4 =
   \mathsf{ABAAAA}$, landing at $39361 = 6\cdot3^8 - 5$; the $C$-map odd
   milestones agree; the floor $6m_{16} - 5 = 27775\ldots67403$ reproduced
   digit-exactly, and $m_{16}$'s digit word `4450023324032350` re-derived by
   direct chart iteration.
7. **Inline-lemma stress:** 500 fresh random subcritical systems with
   $W < P + Q$: zero moving cycles; the $W = P + Q$ witness verified.
8. **Placeholder audit:** the file's single embedded python block extracted
   and rerun on CPython 3 — output **byte-for-byte identical** to the embedded
   output block.
9. **New finite verification (strictness):** $a_{16}(m_{16}) = 13249 \notin
   A$, so $m_{16} \notin S_{17}$ and $m_{17} > m_{16}$: the strict
   $x > m_{16}$ used by C2 (and by X-9902's own phrasing) is thereby
   justified; monotonicity alone gives only $x \ge m_{16}$.

### V.3 The one fix applied (EMPIRICAL C2, Step 6)

C2's parenthetical identified "any positive integer whose $T$-orbit runs
complete $(5,1)$-macros forever" with the roots $x$ of the dictionary. But $x$
is defined only where $3 \mid y$ ($n \equiv 1 \bmod 6$): automatic for every
state from the first macro image on, **not** for a seed — first-macro legality
is one class mod $2^{19}$ and carries no mod-3 information. A hypothetical
all-time seed in another odd residue class inherits the floor at its first
macro image, giving for itself the marginally weaker $n_0 >
(Q(6m_{16}-5) - 2E_{\max} + (P-Q))/P > 2.74\times10^{79}$ (exact value
$27401863909914425234802892657398060317640704603474187290034782966354182284438853$,
ratio $Q/P \approx 0.98654$ of the displayed floor). The C2 sentence now
carries the residue qualifier plus a flagged clarification. Impact on the
theorems: none — C2 is EMPIRICAL and cited by nothing.

### V.4 Observations (no action required)

- **$(6,2)$ is closable by elementary finite means**, though not by the two
  lemmas *as instantiated* (so the Honest scope statement stands): by
  T-9924.4(a) any integral $(6,2)$-cycle is confined to $y \in [3, 8]$, and
  my computation shows **no** pair $(y, E) \in [3,8] \times \mathcal{E}_{6,2}$
  has $Q \mid Py + E$ at all — $6 \times 28 = 168$ elementary divisibility
  failures. A future claim file recording those 168 facts (or a residue system
  organizing them) would extend the theorem to the packet $(6,2)$; the
  suggested-next-attack framing stays right for whole rows at $a \ge 6$.
- Cosmetic: Step 0(a) contains a visibly abandoned mid-derivation fragment
  ("$- 40/\ldots$") superseded by the clean computation that follows; left
  untouched.
- The provenance and verification-summary tables were cross-checked line by
  line against my recomputation; every "VERIFIED" row is accurate, and the
  superseded-threshold row matches the landed L-9923.

### V.5 Confidence and status action

High confidence. The main theorem rests on three short elementary integer
arguments (collapse, sieve, sign) re-proved inline and reconstructed here,
one exact algebraic identity per packet, and finite displayed enumerations
whose completeness I re-established by exhaustive search; the physical layer
(blocks $=$ exact $T$-composites, legality $=$ integrality) was re-verified
against raw $T$-iteration in both directions. Header updated: Status
PROPOSED → PROVED, reviewer recorded. Not marked INDEPENDENTLY_VERIFIED
(a further independent reviewer is required per README §7 / NOTATION.md
conventions).

*Reviewed by fable-02-v26, 2026-07-26.*
