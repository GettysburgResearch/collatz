# T-9925 — Contracting-phase classification for the fixed-weight pulse grammars: the suffix phase floor, complete cycle-freeness for every row $a \le 448$, and the parameter-uniform floor problem

```text
Claim ID:      T-9925
Title:         Toward the parameter-uniform contracting-phase floor: exact
               contracting-region characterization, target-set stabilization,
               the 3-adic suffix phase invariant and its floor certificates,
               complete cycle-freeness of every fixed-weight packet (a,b) with
               a <= 448 (all b, both phases), partial rows 449..469 with the
               27 exceptional packets listed exactly, the supercritical sign
               closure for the entire region Q < P, and the open floor
               problem Q-9925 whose positive answer closes the complete
               contracting phase.
Status:        PROPOSED
Authoring agent:   fable-02-p19
Reviewing agents:  (none yet)
Created:       2026-07-26
Last updated:  2026-07-27
Dependencies:  NOTATION.md (conventions; D-9902/D-9904/D-9905 only to name the
               physical objects via T-9924);
               L-9923 (PROVED): L-9923.2 (2a-2c) cycle-minimum sieve with the
               g-refinement, and L-9923.3(ii) supercritical sign obstruction —
               each restated below in <= 10 lines where used;
               T-9924 (PROVED): D-9924.1-.2 (blocks, macros, packets),
               T-9924.2 (fixed-weight macro algebra), T-9924.4 (automatic
               positivity + sieve instantiation), T-9924.1(e)/.7 (physical
               reduction; the a <= 5 theorem this file extends) — each used
               piece restated in <= 10 lines.
               External, branch-qualified, NOT dependencies: the source
               program's T-9609/T-9610/T-9611 (see Provenance).
Scope:         The complete fixed-weight (a,b) macro family of T-9924's pulse
               grammar, all a >= 0, all b >= 0, both phases (contracting
               Q > P and supercritical Q < P), arbitrary word length,
               arbitrary branch orders, arbitrary repetition, all INTEGER
               states.  Fully closed here: every row a <= 448 (all b); rows
               449..469 except 27 explicitly listed packets; the entire
               supercritical region (no cycle with a state >= 0).  NOT
               closed: the 27 listed packets and the rows a >= 470 of the
               contracting phase (the exact resisting set), entirely negative
               supercritical cycles, and everything in the Honest scope box.
Related counterexample candidates: none
```

---

## Provenance, supersession event, and corrections to the commissioning analysis

**Commission.** This file was commissioned (2026-07-26) as the extension of
T-9924's cycle-freeness theorem beyond its $a \le 5$ scope, with the complete
contracting phase as the ambition. On 2026-07-27, mid-work, the coordinator
relayed fresh reconnaissance: the external source program (the PR #47/#46
line whose unpushed drafts seeded L-9923 and T-9924) had on 2026-07-26 pushed
its own extensions on **its own branch, not present in this working tree**:
"T-9609" ($a \le 13$), "T-9610" ($a \le 243$), "T-9611" ($a \le 375$), via
depth-10/15 CRT phase tables, and stated as its open request *"a
parameter-uniform lower bound for $H_d$"* — a phase-floor bound uniform in
$a$. Those claims are **unverifiable from this repository** and nothing below
cites or uses them; they are recorded here as branch-qualified context, with
this consequence for status honesty: where the results below overlap their
reported coverage ($6 \le a \le 375$), this file is an **independent in-tree
derivation of the same conclusions** (cycle-freeness of those rows), by a
different mechanism (a single 3-adic suffix invariant rather than CRT
tables); where it goes beyond ($376 \le a \le 448$, the exact
region/stabilization/floor theorems, the supercritical completion, and the
precise resisting set), it is new in-tree territory. The re-aimed target
requested by the coordinator — state and attack the parameter-uniform floor —
is Q-9925 below, formulated exactly in this file's machinery.

**Corrections to the coordinator's structural analysis.** The commission
sketched a route (mod-9 parity split, mod-7 hunts for even rows) that the
derivations below verify, correct, and largely supersede:

1. *Verified:* $\rho(a,b) = E_{\max}/D$ strictly decreasing in $b$ with limit
   $\tau_a = 3((9/8)^a - 1)$; $Q/D \downarrow 1$; targets $\equiv 3sQ \bmod
   9$; $Q \equiv (-1)^a \bmod 3$; $b_0(a) = \lceil a\theta\rceil$ exactly.
2. *Corrected:* the mod-9 classification of targets is by $s \bmod 3$, not by
   the parity of $s$ ($3sQ \bmod 9$ has period $3$ in $s$).
3. *Corrected:* mod 9 does **not** fail for even $a$. The constants' classes
   for even $a$ are $\{0, 6\} \bmod 9$ (the sign rule $3(-1)^{a-1}$), not
   $\{0, 3\}$; the $s \equiv 1 \bmod 3$ targets ($\equiv 3 \bmod 9$ for even
   $a$) are separated exactly as for odd $a$. There is **no parity asymmetry
   anywhere**: the obstruction to closing a row is the size $S_a$ of its
   stable target family, never the parity of $a$. The commissioned "hunt for
   even-row congruences" is thereby unnecessary; and the specific suggestion
   (mod 7) is provably fruitless as a full-block kill: killing a complete
   $s$-block mod 7 would need $2^a \equiv 3 \pmod 7$, which has no solution
   ($2^a \in \{1,2,4\}$) — Step 6 Remark.
4. *Corrected/refined:* the "surviving trio $\{3D,\, 2D+Q,\, D+2Q\}$" is the
   stable target family exactly for $6 \le a \le 9$ ($S_a = 1$); in general
   the stable family is $\mathcal{T}_\infty(a)$ of size $3S_a(S_a+1)/2$ with
   $S_a = \lfloor (9/8)^a \rfloor - 1$ (T-9925.3).
5. *Superseded:* the per-row congruence hunts are replaced by one mechanism —
   the 3-adic suffix invariant $\sigma$ and its floor certificates — which
   kills all rows $a \le 448$ at once, including every small-$b$ packet, with
   no per-row casework at all.

**Relation to T-9924's review.** T-9924 was upgraded to PROVED by reviewer
fable-02-v26 (2026-07-26) while this file was being drafted; its verification
note V.4 records that packet $(6,2)$ is closable by 168 elementary
divisibility checks in the confinement box $[3,8]$. That observation is
subsumed here (packet $(6,2)$ falls to the general row theorem, and the 168
checks are reproduced as a cross-check in the Adversarial tests, T12).

Responsibility for every statement and proof below rests with this file.

---

## Statement

Throughout, the two-letter pulse grammar of T-9924 (D-9924.1, PROVED) is
fixed: letters act on the centered coordinate $y$ by
$$\mathsf{A}:\ 8y' = 9y + 3, \qquad \mathsf{B}:\ 16y' = 9y,$$
a **word** $w = \ell_1\cdots\ell_L$ of weight $(a,b) = (\#\mathsf{A},
\#\mathsf{B})$, $L = a + b$, composes to $Q\,y_L = P\,y_0 + E_w$ with
$$Q = Q_{a,b} = 8^a 16^b = 2^{e}, \quad e := 3a+4b, \qquad P = 9^{L} =
3^{2L}, \qquad E_w = 3 \sum_{j:\,\ell_j = \mathsf{A}} 9^{\,L-j} Q_{<j},$$
$Q_{<j} := \prod_{i<j} q_{\ell_i}$ (T-9924.2, PROVED, restated in Step 0).
The **packet** $(a,b)$ is the nondeterministic affine system with alphabet
$\mathcal{E}_{a,b} = \{E_w : w \text{ of weight } (a,b)\}$ (all
$\binom{L}{b}$ branch orders); an **integral cycle** is
$(y_t)_{t \in \mathbb{Z}/R}$, $y_t \in \mathbb{Z}$, with $Q y_{t+1} = P y_t +
E_{w_t}$ for arbitrary independent weight-$(a,b)$ words $w_t$.  $D := Q - P$;
$E_{\min} = 3\cdot 9^b(9^a - 8^a)$, $E_{\max} = 3 \cdot 16^b (9^a - 8^a)$
(for $a \ge 1$).  The packet is **contracting** if $Q > P$, **supercritical**
if $Q < P$ ($Q = P$ is impossible).  All arithmetic is exact.

### The sub-claims

* **T-9925.1 (exact contracting region).** Let $\theta :=
  \log(9/8)/\log(16/9) = 0.20469\ldots$ Then $a\theta \notin \mathbb{Z}$ for
  every $a \ge 1$, and for $a \ge 1$:
  $$(a,b) \text{ contracting} \iff b \ge b_0(a) := \lfloor a\theta \rfloor + 1
  = \lceil a\theta \rceil ,$$
  and the contracting set of each row is exactly the tail $b \ge b_0(a)$
  (upward closed).  $b_0(a) \ge 1$ always ($b = 0$ is supercritical for every
  $a \ge 1$).  Each value $b_0(a)$ carries the integer certificate
  $8^a16^{b_0} > 9^{a+b_0} > \cdots$, verified for $a \le 60$ in the tests.
* **T-9925.2 ($\rho$-monotonicity and limits).** On the contracting range,
  $$\rho(a,b) := \frac{E_{\max}}{D} = \frac{3\,(9^a - 8^a)}{8^a - 9^a
  (9/16)^b}$$
  is strictly decreasing in $b$ with $\rho(a,b) \downarrow \tau_a :=
  3\big((9/8)^a - 1\big)$ and $\rho > \tau_a$ always; $Q/D$ is strictly
  decreasing with limit $1$; consequently $s_{\max}(a,b) := \lfloor
  \rho(a,b)/3\rfloor$ is nonincreasing in $b$, $\ge S_a$, with eventual value
  $S_a := \lfloor (9/8)^a \rfloor - 1$.
* **T-9925.3 (target-set stabilization).** For a contracting packet with
  $a \ge 1$, the $g{=}3$ sieve data (L-9923.2, restated in Step 1) of any
  positive integral cycle is a pair $(m,k)$, $m \ge 1$, $k \ge 0$,
  $3 \mid m+k$, with $E := Dm + Qk \in \mathcal{E}_{a,b}$; writing $s :=
  (m+k)/3 \ge 1$ one has $E = 3sD + Pk$, $k \le 3s-1$, and $s \le
  s_{\max}(a,b)$.  Let $b_1(a) :=$ least $b \ge b_0(a)$ with $E_{\max} <
  3(S_a{+}1)D$ (exists; for $a \le 5$ it is exactly T-9924.5's gate row
  threshold and the admissible set is empty).  Then for **every** $b \ge
  b_1(a)$ the admissible $(m,k)$ set is exactly the stable family
  $$\mathcal{T}_\infty(a) := \{(m,k) : m+k = 3s,\ 1 \le s \le S_a,\ m \ge 1,\
  k \ge 0\}, \qquad |\mathcal{T}_\infty(a)| = \tfrac{3}{2}S_a(S_a+1),$$
  by the exact identity $E_{\max} - 3sD - (3s{-}1)P = 3\cdot 16^b\,(9^a -
  (s{+}1)8^a) + 9^{a+b} > 0$ for $s \le S_a$ (every pair fits below
  $E_{\max}$, at every contracting $b$), and by $3(S_a{+}1)D > E_{\max}$ (no
  larger $s$ fits) for $b \ge b_1(a)$.
* **T-9925.4 (3-adic structure of the constants; the general mod-9 rule).**
  For $a \ge 1$, with $\ell_B(w)$, $t_B(w)$ the leading/trailing
  $\mathsf{B}$-run lengths: $E(\mathsf{B}w) = 16\,E(w)$ and $E(w\mathsf{B}) =
  9\,E(w)$, hence $E_w = 16^{\ell_B} 9^{t_B} E_{w_0}$ with $w_0$ starting and
  ending in $\mathsf{A}$; $\nu_2(E_w) = 4\ell_B(w)$ and $\nu_3(E_w) = 1 +
  2\,t_B(w)$ exactly; and
  $$E_w \equiv 3^{\,1+2t_B}\cdot 2^{\,e - 4t_B - 3} \pmod{3^{\,3+2t_B}} .$$
  In particular the **general mod-9 rule**: $E_w \equiv 3(-1)^{a-1} \bmod 9$
  when $\ell_L = \mathsf{A}$ (any $b$), and $27 \mid E_w$ when $\ell_L =
  \mathsf{B}$ — T-9924.2's rule with its sign now exhibited as the first
  digit of a full 3-adic expansion.  (Also restated: mod-21 packet rigidity,
  all $E_w \equiv E_{\min} \bmod 21$.)
* **T-9925.5 (master phase congruence).** Define $\sigma(w) := (E_w/3)\,
  Q^{-1} \bmod 3^{2L-1}$.  If $E_w = Dm + Qk$ with $3 \mid m+k$, $s =
  (m+k)/3$, then
  $$s \equiv \sigma(w) \pmod{3^{2L-1}}, \qquad m \equiv E_w D^{-1}
  \pmod{2^{e}} ,$$
  and $\sigma$ is **suffix-local**: for $1 \le t \le L$, $\sigma(w) \bmod
  3^{2t}$ depends only on the last $t$ letters of $w$, via
  $\sigma \equiv \sum_{\delta < t,\ r_{\delta+1} = \mathsf{A}}
  9^{\delta}\,\big(q_{r_1}\cdots q_{r_{\delta+1}}\big)^{-1} \bmod 3^{2t}$
  ($r_1 =$ last letter).  Dually $E_w D^{-1} \bmod 2^d$ is prefix-local.
* **T-9925.6 (phase floor and certificates).** Let $H_d$ ($d \ge 2$) be the
  minimum over all length-$\lceil d/2\rceil$ suffixes $u$ of the least
  **positive** residue of $\sigma(u) \bmod 3^d$.  Then $H_d$ is
  nondecreasing in $d$; $H_2 = 8$, $H_3 = 17$, $H_4 = 45$, $H_{10} = 3690$,
  $H_{24} = 131271758$, $H_{40} = 26048632820598$, etc. (exact finite
  evaluations, Step 5).  **Certificate lemma:** the alive-set recursion of
  Step 5, run with threshold $T$, terminates with an empty set at depth
  $t_c(T)$; this proves: for every word $w$ of length $L \ge t_c$, no $s \in
  [1, T]$ has $s \equiv \sigma(w) \bmod 3^{2t_c}$ (i.e. $H_{2t_c} > T$).
  The certified ladder (Step 5, machine-verified):
  $$(T, t_c) \in \{(2,1), (8,2), (60,5), (4\cdot10^3,9), (10^6,10),
  (10^8,12), (10^{10},16), (10^{12},19), (10^{14},22),$$
  $$(10^{16},25), (10^{18},28), (10^{20},31), (10^{22},33), (10^{24},37)\}.$$
  **Kill theorem:** if a contracting packet $(a,b)$, $a \ge 1$, has
  $s_{\max}(a,b) \le T$ for a ladder rung with $t_c \le a+b-1$, then the
  packet has **no integral cycle whatsoever** (any sign, any length, any
  branch orders).
* **T-9925.7 (MAIN THEOREM: complete rows $a \le 448$ and the
  classification).** For every $(a,b)$ with $1 \le a \le 448$ and $b \ge 0$:
  if $b < b_0(a)$ (supercritical), no integral cycle of the packet contains
  a state $y \ge 0$; if $b \ge b_0(a)$ (contracting), the packet has no
  integral cycle at all.  For $a = 0$: the unique cycle is $y \equiv 0$.
  Combined with T-9924.7 (PROVED, $a \le 5$; independently re-derived here —
  the same ladder closes rows $1..5$): **the only cycle of the entire
  fixed-weight family with any state $y \ge 0$, over all $0 \le a \le 448$
  and all $b$, is the all-$\mathsf{B}$ fixed point $y = 0$, physically
  $n = 1$.**  Moreover rows $449 \le a \le 469$ are closed for every $b \ge
  b_2(a)$ (a computed threshold $\le b_0(a)+6$), leaving exactly the **27
  exceptional packets**
  $$(449,92),\ (453,93),\ (454,93),\ (457,94),\ (458,94),\ (459,94),\
  (461,95),\ (462,95),\ (463,95),$$
  $$(464,95),\ (464,96),\ (465,96),\ (466,96),\ (466,97),\ (467,96),\
  (467,97),\ (467,98),\ (468,96),$$
  $$(468,97),\ (468,98),\ (468,99),\ (469,97),\ (469,98),\ (469,99),\
  (469,100),\ (469,101),\ (469,102)$$
  (machine-listed in T7 of the tests).  The **exact resisting set** of the
  contracting phase at this ladder is those 27 packets together with all
  contracting $(a,b)$ with $a \ge 470$.
  **Corollary (physical form, via T-9924.1(e)).** If legal Collatz blocks
  applied at an odd $n_0 \ge 1$ form a concatenation of complete
  weight-$(a,b)$ macros with $a \le 448$ returning to $n_0$, then $a = 0$
  and $n_0 = 1$ (the trivial cycle).
  **Corollary (letter level, extending T-9924 Corollary 2).** Any integral
  cycle of the letter system with some state $y_t \ge 0$, other than
  $y \equiv 0$, has per-period letter totals $(\alpha, \beta)$ lying in the
  resisting set: $\alpha \ge 449$, $\beta \ge b_0(\alpha)$, and
  $(\alpha,\beta)$ not covered by the ladder.
* **T-9925.8 (supercritical completion).** For **every** $(a,b)$ with
  $a \ge 1$ and $Q < P$ (equivalently $b < b_0(a)$, including all $b = 0$):
  no integral cycle of the packet contains a state $y \ge 0$; consequently
  no positive and no physical cycle exists, and every forward-integral orbit
  from $y_0 > 0$ diverges ($y_{t+1} > (P/Q) y_t$).  This generalizes
  T-9924's packet-$(5,1)$ closure verbatim to the whole supercritical
  region.
* **Q-9925 (the re-aimed open problem: the parameter-uniform floor).**
  (A) Is $\sup_d H_d = \infty$?  Equivalently (König's lemma on the alive
  tree): is there **no** infinite letter sequence $u \in
  \{\mathsf{A},\mathsf{B}\}^{\mathbb{N}}$ (read as ever-longer suffixes)
  whose 3-adic phase $\sigma(u) = \sum_{\delta:\, r_{\delta+1} =
  \mathsf{A}} 9^\delta (q_{r_1}\cdots q_{r_{\delta+1}})^{-1} \in
  \mathbb{Z}_3$ is a **positive rational integer**?  A positive answer
  closes the **complete contracting phase** (formulation (i) of the
  commission): every row $a$ closes at depth $d$ with $H_d > S_a$, whose
  window requirement $t_c \le a + b_0(a) - 1$ is asymptotically free
  ($t_c \approx \log_9 S_a \approx 0.054\,a \ll a$).  (B) Effective rate:
  prove $H_d \ge c\,\lambda^d$ for some $\lambda > 1$.  Empirically
  (labelled EMPIRICAL: the certified depths give $t_c(T) - \lceil \log_9 T
  \rceil \in [3, 11]$ over $T \in [60, 10^{24}]$) the floor grows like
  $H_{2t} \gtrsim 9^{\,t - 12}$ at computed depths.  This is this file's
  formulation of the external program's requested "parameter-uniform lower
  bound for $H_d$" (Provenance), stated entirely in in-tree objects.

### Honest scope box

> **This theorem is strictly weaker than the Collatz conjecture.** It
> excludes cycles realizable inside the fixed-weight $\{\mathsf{A},
> \mathsf{B}\}$ macro grammar, nothing more.  Outside its scope:
> (i) the 27 listed packets and all contracting rows $a \ge 470$ — the exact
> resisting set, whose closure is Q-9925;
> (ii) entirely negative integral cycles of supercritical packets (no
> physical meaning; not excluded);
> (iii) dynamics not expressible as fixed-weight $\{\mathsf{A},\mathsf{B}\}$
> words: unrestricted valuation words, other block pairs, non-fixed-weight
> (mixed-weight) grammars beyond the per-period-total reduction of the
> letter-level corollary, and the source program's scale-varying summaries;
> (iv) the six-branch least-root decision (the $m_N$ dichotomy of issue
> #58): T-9924.8 positions packet $(5,1)$ as that chart, and nothing here
> touches the extraction question;
> (v) physical legality refinements beyond T-9924.1's
> legality-=-integrality, which this file inherits, not re-proves.
> No K-#### candidate is created.

### Verification summary (commission vs. outcome)

| Commissioned deliverable | Outcome here |
|---|---|
| Exact contracting region, $b_0(a)$ with integer certificates | **PROVED** (T-9925.1; $b_0 = \lceil a\theta\rceil$, no ties) |
| $\rho$ decreasing, $\tau_a$ limit, $Q/D \to 1$ | **PROVED** (T-9925.2) |
| Exact eventual target set + stabilization threshold | **PROVED** (T-9925.3: $\mathcal{T}_\infty(a)$, $b_1(a)$) |
| General mod-9 constant rule | **PROVED** (T-9925.4, as digit 1 of the full 3-adic law) |
| Row closures $a \ge 6$ with complete small-$b$ handling | **PROVED for all $6 \le a \le 448$** (T-9925.6/.7; no small-$b$ exceptions remain below $a = 449$) |
| Resisting set stated exactly | **DONE** (27 packets + rows $a \ge 470$) |
| Supercritical sign generalization | **PROVED** (T-9925.8) |
| Mod-9 parity route for odd $a$ / mod-7 hunts for even $a$ | **SUPERSEDED** (no parity asymmetry; corrections 2–5 in Provenance) |
| Parameter-uniform floor (redirect target) | **FORMULATED EXACTLY + PARTIAL** (Q-9925; certified floor to $10^{24}$; uniformity open) |

---

## Definitions

All conventions of NOTATION.md (exact arithmetic; empty sums $0$; finite
computation is verification, with the epistemic note below).  Beyond the
Statement's setting:

- **Suffix/prefix coordinates.** For $w = \ell_1\cdots\ell_L$ write $r_\delta
  := \ell_{L+1-\delta}$ (the $\delta$-th letter from the end, $r_1$ = last)
  and say the letter $r_{\delta+1}$ sits at **end-distance** $\delta$.
  $q_\mathsf{A} = 8$, $q_\mathsf{B} = 16$.
- **$\sigma$, suffix form.** For a finite word (or suffix) $u = (r_1, \dots,
  r_t)$ and a modulus $3^d$:
  $\sigma(u) := \sum_{\delta=0}^{t-1} [r_{\delta+1} = \mathsf{A}]\;
  9^{\delta}\, (q_{r_1} q_{r_2} \cdots q_{r_{\delta+1}})^{-1} \bmod 3^d$
  (inverses exist: the $q$'s are powers of $2$).  For a full word,
  $\sigma(w) = (E_w/3) Q^{-1} \bmod 3^{2L-1}$ (Step 4 proves the two forms
  agree).
- **$\mu$, prefix form** (secondary): $\mu(w) := E_w D^{-1} \bmod 2^{e}$;
  equals $-3\sum_{j:\ \ell_j = \mathsf{A}} 9^{-j} Q_{<j} \bmod 2^e$.
- **Alive-set recursion at threshold $T$.** States at level $t$ are pairs
  $(\sigma(u) \bmod 3^{2t_g},\ \#\mathsf{A}(u))$ over suffixes $u$ of length
  $t$ (working modulus $3^{2t_g}$ with guard $t_g$ exceeding the terminal
  depth; the second coordinate determines the prefix-product needed to
  extend).  Level $0$ is $\{(0,0)\}$; a level-$t$ state is **alive** iff its
  residue $r = \sigma \bmod 9^t$ satisfies ($r \ne 0$ and $r \le T$) or
  ($r = 0$ and $9^t \le T$).  $t_c(T)$ is the first level with no alive
  states.
- **$s_{\max}$, $S_a$, $b_0$, $b_1$, $b_2$.** $s_{\max}(a,b) = \lfloor
  E_{\max}/(3D)\rfloor$; $S_a = \lfloor (9/8)^a\rfloor - 1$; $b_0, b_1$ as
  in the Statement; $b_2(a) :=$ least $b \ge b_0(a)$ such that some ladder
  rung $(T, t_c)$ has $s_{\max}(a,b) \le T$ and $t_c \le a + b - 1$.
- **Epistemic note (finite exact evaluations).** Several lemmas below assert
  values of explicitly defined finite minima ($H_d$; the certificate depths
  $t_c(T)$; the coverage scan).  Each is a statement about a finite,
  explicitly enumerated set of integers, established by exact integer
  computation embedded in the Adversarial tests — the same epistemic status
  as T-9924's displayed gate-boundary evaluations, only larger.  Per
  NOTATION.md these computations are labelled as what they are: **finite
  exact evaluation**, reproducible deterministically from the embedded
  code; they are not sampling-style "empirical" evidence, and every
  *universally quantified* statement below is proved by argument, with the
  finite evaluations entering only as evaluations of the finitely many
  constants named in the theorem statements.  The smallest instances
  ($H_2 = 8$, $H_3 = 17$, $H_4 = 45$, $t_c(2) = 1$, $t_c(8) = 2$) are also
  verified by hand in Step 5.

## Motivation

T-9924 (PROVED) closed the cycle side of the pulse grammar for $a \le 5$ and
had to stop there: its gate fails for all $a \ge 6$ ($(9/8)^a > 2$), and its
per-packet congruence closures do not scale in $b$, let alone in $a$.  This
file replaces the per-packet view with three uniform mechanisms:

1. the **stabilization theorem** (T-9925.3), which reduces each row's
   infinite $b$-tail to one finite family $\mathcal{T}_\infty(a)$ of
   candidate sieve data;
2. the **suffix phase invariant** (T-9925.5): the single congruence $s
   \equiv \sigma(w) \bmod 3^{2L-1}$, whose depth-$2t$ truncation sees only
   $t$ letters — turning "which packets admit sieve data" into a
   packet-independent question about a finitely branching tree of 3-adic
   phases;
3. the **floor certificates** (T-9925.6): finite computations that push the
   least realizable phase above $10^{24}$, killing every candidate $s$ in
   every packet with $s_{\max} \le 10^{24}$ at once.

The result is the largest cycle-free region of the family so far
($a \le 448$, both phases, classification form), the exact frontier beyond
it, and a clean statement (Q-9925) equivalent to closing the contracting
phase entirely: a single question about integer values of a 3-adic series
over the letter tree.  The supercritical half (T-9925.8) is the two-line
sign argument of L-9923.3(ii), quantified over the whole region for the
first time; with it, the family's classification is complete on $y \ge 0$
for every $a \le 448$.

---

## Proof

### Step 0 — imported statements, restated (T-9924.2, T-9924.4, L-9923.2, L-9923.3(ii))

**(T-9924.2, PROVED; restatement.)** For every word $w$ of weight $(a,b)$:
$Q = 8^a16^b$ and $P = 9^{a+b}$ independent of order; $E_w = 3\sum_{j:
\ell_j = \mathsf{A}} 9^{L-j} Q_{<j} \ge 0$, positive iff $a \ge 1$, always
$\equiv 0 \bmod 3$; $E_{\min} = 3\cdot9^b(9^a - 8^a)$ (only by
$\mathsf{A}^a\mathsf{B}^b$) and $E_{\max} = 3\cdot16^b(9^a - 8^a)$ (only by
$\mathsf{B}^b\mathsf{A}^a$); adjacent-swap increments are positive multiples
of $21$, hence all constants of a packet are congruent mod $21$.

**(T-9924.4(a), PROVED; restatement — automatic positivity.)** If all
constants are positive (true for $a \ge 1$) and $Q > P$, every integral
cycle satisfies $\lceil E_{\min}/D\rceil \le y_t \le \lfloor
E_{\max}/D\rfloor$; in particular $y_t \ge 1$: integral cycles are
automatically positive.  (Proof sketch, 3 lines: at an edge entering the
maximum $M$, $QM = Py_t + E \le PM + E_{\max}$, so $DM \le E_{\max}$; at an
edge entering the minimum $\mu$, $Q\mu \ge P\mu + E_{\min}$, so $D\mu \ge
E_{\min} \ge 1$.)

**(L-9923.2 (2a)+(2b), PROVED; restatement — the sieve.)** If a positive
integral cycle exists, anchor at a position of minimum $\mu \ge 1$; the
successor is $\mu + \kappa$, $\kappa \ge 0$, and the constant used there is
exactly $E = D\mu + Q\kappa$.  If moreover $g \mid P$, $\gcd(g, Q) = 1$, and
$g$ divides every constant, then $g \mid \mu + \kappa$.  Here $g = 3$
qualifies: $3 \mid P = 3^{2L}$, $\gcd(3, 2^e) = 1$, $3 \mid E_w$.  (We
rename $(\mu, \kappa)$ to $(m, k)$.)

**(L-9923.3(ii), PROVED; restatement — supercritical sign.)** If $P > Q \ge
1$ and all constants are $\ge 0$, no integral cycle has $x_0 \ge 1$… in the
form needed here (constants $> 0$, excluding also $0$): the cycle equation
$(Q^R - P^R)y_0 = \sum_t P^{R-1-t}Q^t E_{w_t} > 0$ forces $y_0 < 0$; by
rotation every state is $< 0$.

### Step 1 — the region (T-9925.1)

Both sides positive, take logarithms: $8^a16^b > 9^{a+b} \iff b\log(16/9) >
a\log(9/8) \iff b > a\theta$.  If $a\theta = c \in \mathbb{Z}$ for some
$a \ge 1$, then $(9/8)^a = (16/9)^c$, i.e. $9^{a+c} = 8^a 16^c$ — impossible
for $a \ge 1$ ($9^{a+c}$ odd, $8^a16^c$ even).  Hence $b > a\theta \iff b
\ge \lfloor a\theta\rfloor + 1 = \lceil a\theta\rceil =: b_0(a)$, and
$b_0(a) \ge 1$ since $b = 0$ gives $8^a < 9^a$.  Upward closure directly:
$8^a16^{b+1} = 16\cdot 8^a16^b > 16 \cdot 9^{a+b} > 9^{a+b+1}$.  $Q = P$ is
impossible (parity).  $\square$

### Step 2 — $\rho$-monotonicity, limits, $s_{\max}$ (T-9925.2)

Divide numerator and denominator of $\rho = 3\cdot16^b(9^a-8^a)/D$ by
$16^b$: $\rho = 3(9^a-8^a)/g_b$ with $g_b := 8^a - 9^a(9/16)^b = D/16^b >
0$ on the contracting range.  $(9/16)^b$ is strictly decreasing in $b$, so
$g_b$ is strictly increasing, so $\rho$ is strictly decreasing; $g_b \to
8^a$ gives $\rho \downarrow 3(9^a-8^a)/8^a = \tau_a$, and $g_b < 8^a$ gives
$\rho > \tau_a$ for every finite $b$.  $Q/D = 1/(1 - P/Q)$ with $P/Q =
(9/8)^a(9/16)^b$ strictly decreasing to $0$: $Q/D$ strictly decreases to
$1$.  Hence $s_{\max} = \lfloor\rho/3\rfloor$ is nonincreasing; and $\rho/3
> \tau_a/3 = (9/8)^a - 1$, which is never an integer ($(9/8)^a \notin
\mathbb{Z}$ for $a \ge 1$: $8^a \nmid 9^a$), so $s_{\max} \ge \lfloor
(9/8)^a - 1\rfloor = \lfloor (9/8)^a\rfloor - 1 = S_a$.  Once $\rho <
3(S_a + 1)$ (see Step 3), $s_{\max} = S_a$ exactly.  $\square$

### Step 3 — target-set stabilization (T-9925.3)

Let a positive integral cycle of a contracting packet ($a \ge 1$) be given.
By Step 0 (L-9923.2 with $g = 3$) some constant satisfies $E = Dm + Qk$,
$m \ge 1$, $k \ge 0$, $3 \mid m + k$; put $s = (m+k)/3 \ge 1$.  Using $Q =
D + P$: $E = D(m+k) + Pk = 3sD + Pk$, and $m \ge 1$ gives $k \le 3s - 1$.
From $E \le E_{\max}$ and $Pk \ge 0$: $3sD \le E_{\max}$, so $s \le
\rho/3$, i.e. $s \le s_{\max}(a,b)$.

*Existence and characterization of $b_1(a)$.* $3(S_a+1) = 3\lfloor
(9/8)^a\rfloor > 3((9/8)^a - 1) = \tau_a$ (strictly, since $\lfloor x
\rfloor > x - 1$).  As $\rho \downarrow \tau_a$ strictly (Step 2), the
condition $\rho < 3(S_a+1)$, i.e. $E_{\max} < 3(S_a+1)D$, holds for all
sufficiently large $b$ and, once true, stays true; $b_1(a)$ is its first
$b$.  For $a \le 5$, $S_a = 0$ ($(9/8)^a < 2 \iff a \le 5$, by $9^5\cdot
16 < 2\cdot 8^5\cdot 16 \iff (9/8)^5 < 2$, the same integers as T-9924.5's
$a$-cutoff), and $E_{\max} < 3D$ is precisely T-9924.5's gate $G(a,b)$: the
admissible set is empty and $b_1$ is the gate row threshold — this file's
machinery degenerates to T-9924's exactly.

*For $b \ge b_1(a)$ the admissible set is exactly $\mathcal{T}_\infty(a)$.*
No pair with $s > S_a$ is admissible: $E \ge 3sD \ge 3(S_a+1)D > E_{\max}$.
Every pair with $s \le S_a$ is admissible at **every** contracting $b$: the
largest value in its block is $3sD + (3s-1)P$, and expanding $D = 8^a16^b -
9^{a+b}$, $P = 9^{a+b}$, $E_{\max} = 3\cdot16^b(9^a - 8^a)$:
$$E_{\max} - 3sD - (3s-1)P = 3\cdot16^b\big(9^a - (s+1)8^a\big) +
9^{a+b},$$
an exact identity (collect the $16^b$ and $9^{a+b}$ terms; verified
symbolically in T8).  For $s \le S_a$: $(s+1) \le \lfloor (9/8)^a\rfloor$,
so $(s+1)8^a \le \lfloor (9/8)^a\rfloor 8^a \le 9^a$, with equality
impossible ($8^a \nmid 9^a$); hence $9^a - (s+1)8^a \ge 0$, indeed $\ge 1$
— wait, $\ge 0$ suffices: both summands are then $> 0$ or $\ge 0 + 9^{a+b}
> 0$.  So every $(m,k)$ with $s \le S_a$, $k \le 3s-1$ has $Dm + Qk \le
E_{\max}$.  The count is $\sum_{s=1}^{S_a} 3s = \tfrac32 S_a(S_a+1)$.
$\square$

*(Remark: for $b_0(a) \le b < b_1(a)$ the admissible set is
$\mathcal{T}_\infty(a)$ enlarged by the pairs with $S_a < s \le s_{\max}$
and $k \le (E_{\max} - 3sD)/P$; the Main Theorem's mechanism needs no case
distinction, so no separate small-$b$ analysis occurs anywhere below.)*

### Step 4 — 3-adic structure and the master congruence (T-9925.4, T-9925.5)

**(a) Reductions.** Prepending $\mathsf{B}$: the new word $\mathsf{B}w$ has
letters $\ell'_1 = \mathsf{B}$ (contributing no term) and $\ell'_{j+1} =
\ell_j$ with $Q'_{<j+1} = 16\,Q_{<j}$ and the same $9$-exponents
($L' - (j+1) = L - j$): $E(\mathsf{B}w) = 16\,E(w)$.  Appending
$\mathsf{B}$: every $9$-exponent rises by one and prefix products are
unchanged: $E(w\mathsf{B}) = 9\,E(w)$.  Peeling all leading/trailing
$\mathsf{B}$'s: $E_w = 16^{\ell_B} 9^{t_B} E_{w_0}$, $w_0$ starting and
ending in $\mathsf{A}$.

**(b) Valuations.** For $w_0$ ending in $\mathsf{A}$: the $j = L_0$ term is
$3\,Q_{<L_0}$ ($\nu_3 = 1$); every $j < L_0$ term is $3\cdot 9^{L_0-j}
Q_{<j}$ ($\nu_3 \ge 3$); so $\nu_3(E_{w_0}) = 1$.  For $w_0$ starting with
$\mathsf{A}$: the $j = 1$ term is $3\cdot 9^{L_0-1}$ (odd); every $j \ge 2$
term has $\nu_2(Q_{<j}) \ge 3$; so $E_{w_0}$ is odd.  With (a):
$\nu_3(E_w) = 1 + 2t_B$, $\nu_2(E_w) = 4\ell_B$, exactly.

**(c) Units mod $3^{3+2t_B}$ and the mod-9 rule.** For $w$ ending in
$\mathsf{A}$: mod $27$, all $j < L$ terms vanish ($3 \cdot 9^{L-j} \equiv 0$
for $L - j \ge 1$), leaving $E_w \equiv 3\,Q_{<L} = 3\,(Q/8) =
3\cdot2^{e-3} \pmod{27}$ — one value for the whole packet.  With (a), for
general $w$: $E_w \equiv 9^{t_B}\cdot 3\cdot 2^{\,e - 4t_B - 3} =
3^{1+2t_B}\, 2^{\,e-4t_B-3} \pmod{3^{3+2t_B}}$ (the $16^{\ell_B}$ factor is
absorbed into $2^{e - 4t_B - 3}$, which is the full remaining $2$-power).
Reducing the last-$\mathsf{A}$ case mod $9$: $E_w \equiv 3\cdot 2^{e-3}
\equiv 3(-1)^{e-3} \equiv 3(-1)^{a-1} \pmod 9$ since $e - 3 = 3a + 4b - 3
\equiv a - 1 \bmod 2$; and $\ell_L = \mathsf{B}$ gives $t_B \ge 1$, so
$27 \mid E_w$.  This is T-9924.2's mod-9 rule, now with its general-$a$
derivation and its extension to all depths.  Mod-21 rigidity is Step 0.

**(d) The master congruence (T-9925.5).** $P = 9^L = 3^{2L}$ exactly.  If
$E_w = Dm + Qk$ then, mod $3^{2L}$, $D = Q - P \equiv Q$, so $E_w \equiv
Q(m + k) = 3sQ$.  Both sides are divisible by $3$; dividing, $E_w/3 \equiv
sQ \bmod 3^{2L-1}$, and multiplying by $Q^{-1}$ (a unit mod any $3$-power):
$s \equiv (E_w/3)Q^{-1} = \sigma(w) \bmod 3^{2L-1}$.  The suffix form:
$$\frac{E_w}{3Q} = \sum_{j: \ell_j = \mathsf{A}} 9^{\,L-j}\,
\frac{Q_{<j}}{Q} = \sum_{j: \ell_j = \mathsf{A}} 9^{\,L-j} \Big(\prod_{i
\ge j} q_{\ell_i}\Big)^{-1} = \sum_{\delta:\ r_{\delta+1} = \mathsf{A}}
9^{\delta}\,\big(q_{r_1}\cdots q_{r_{\delta+1}}\big)^{-1}$$
(reindex $\delta = L - j$; the equality is an identity of elements of
$\mathbb{Z}[\tfrac12] \subset \mathbb{Z}_3$, hence of residues mod any
$3$-power).  Mod $3^{2t}$ every term with $\delta \ge t$ vanishes ($9^t =
3^{2t}$), so $\sigma(w) \bmod 3^{2t}$ depends only on $(r_1, \dots, r_t)$ —
the last $t$ letters — for every $t \le L$; the congruence $s \equiv
\sigma(w)$ holds mod $3^{2t}$ whenever $2t \le 2L - 1$, i.e. $t \le L - 1$.
The dual: mod $2^e = Q$, $E_w \equiv Dm$, and $D = Q - P \equiv -P$ is odd,
so $m \equiv E_w D^{-1} \bmod 2^e$; $E_w D^{-1} \equiv -E_w P^{-1} =
-3\sum_j 9^{-j} Q_{<j}$, and $\nu_2(Q_{<j}) \ge 3(j-1)$ makes the reduction
mod $2^d$ depend only on the first $\lceil d/3\rceil + 1$ letters.
$\square$

### Step 5 — the phase floor, its certificates, and the kill theorem (T-9925.6)

**(a) $H_d$ well-defined and monotone.** $\sigma(w) \bmod 3^d$ depends only
on the last $\lceil d/2\rceil$ letters (Step 4(d): terms with $9^\delta
\equiv 0 \bmod 3^d$, i.e. $2\delta \ge d$, vanish), so the minimum defining
$H_d$ ranges over the $2^{\lceil d/2\rceil}$ suffixes and is attained.
Monotonicity: let $v$ be the least positive residue mod $3^{d+1}$ attaining
$H_{d+1}$, from suffix $u'$.  Then $v \ge v \bmod 3^d$; if $v \bmod 3^d \ne
0$ it is the least positive residue mod $3^d$ of $\sigma$ of (a suffix of)
$u'$, hence $\ge H_d$; if $v \equiv 0 \bmod 3^d$ then $v \ge 3^d > H_d$
(every $H_d < 3^d$ trivially).  So $H_{d+1} \ge H_d$.

**(b) Hand evaluations.** $d = 2$ (suffix length 1, mod 9): suffix
$\mathsf{A}$: $\sigma = 8^{-1} \equiv 8$; suffix $\mathsf{B}$: $\sigma = 0$.
So $H_2 = 8$.  $d = 3$ (length 2, mod 27; $8^{-1} \equiv 17$, $64^{-1}
\equiv 17^2 \equiv 19$, $128^{-1} \equiv 20^{-1} \equiv 23$):
$\sigma(\mathsf{AA}) = 17 + 9\cdot19 \equiv 26$, $\sigma(\mathsf{BA}) = 17$,
$\sigma(\mathsf{AB}) = 9\cdot23 \equiv 18$, $\sigma(\mathsf{BB}) = 0$:
$H_3 = 17$.  $d = 4$ (length 2, mod 81; $8^{-1} \equiv 71$, $64^{-1} \equiv
19$, $128^{-1} \equiv 50$): values $\{71 + 9\cdot19 \equiv 80,\ 71,\
9\cdot50 \equiv 45,\ 0\}$: $H_4 = 45$.  These agree with the machine table
(T5), which continues to $H_{40} = 26048632820598$.

**(c) Certificate lemma.** *Claim: if the alive-set recursion at threshold
$T$ has no alive states at level $t_c$, then no word $w$ of length $L \ge
t_c$ and no integer $s \in [1, T]$ satisfy $s \equiv \sigma(w) \bmod
3^{2t_c}$; in particular $H_{2t_c} > T$, and (a) extends this to every $d
\ge 2t_c$.*  Proof.  Suppose such $(w, s)$ exist.  For $1 \le t \le t_c$
let $u_t$ be the last $t$ letters of $w$ and $\sigma_t := \sigma(u_t)$; by
suffix locality, $s \equiv \sigma(w) \equiv \sigma_t \pmod{9^{t}}$ for
every $t \le t_c$ (reduce the mod-$3^{2t_c}$ congruence).  Let $r_t =
\sigma_t \bmod 9^t$.  If $r_t \ne 0$: $s \equiv r_t$ and $s \ge 1$ force
$s \ge r_t$, so $r_t \le T$.  If $r_t = 0$: $9^t \mid s$, so $9^t \le s \le
T$.  Either way the state of $u_t$ (with its $\#\mathsf{A}$ count, which
together with $t$ determines the product $q_{r_1}\cdots q_{r_t}$ needed to
extend — the recursion loses no information by keeping only the pair)
satisfies the alive condition at level $t$.  By induction the recursion
retains it for $t = 1, \dots, t_c$; so the level-$t_c$ alive set contains
$u_{t_c}$'s state and is nonempty — contradiction.  For the "$H_{2t_c} >
T$" reading, take $s$ = the least positive residue of $\sigma(u) \bmod
3^{2t_c}$ over suffixes $u$ of length $t_c$: if some $s \le T$ existed, pad
$u$ to a word (any letters in front; locality ignores them) and contradict
the claim.  $\blacksquare$

**(d) The certified ladder.** Running the recursion (Adversarial tests T6;
deterministic, exact) terminates with empty alive sets at
$$t_c(2) = 1,\ t_c(8) = 2,\ t_c(60) = 5,\ t_c(4{\cdot}10^3) = 9,\
t_c(10^6) = 10,\ t_c(10^8) = 12,\ t_c(10^{10}) = 16,$$
$$t_c(10^{12}) = 19,\ t_c(10^{14}) = 22,\ t_c(10^{16}) = 25,\
t_c(10^{18}) = 28,\ t_c(10^{20}) = 31,\ t_c(10^{22}) = 33,\
t_c(10^{24}) = 37.$$
Hand check of the two smallest: $T = 2$, level 1: state $\mathsf{A}$ has
$r = 8 > 2$, dead; state $\mathsf{B}$ has $r = 0$ with $9 > 2$, dead — empty
at $t = 1$.  $T = 8$, level 1: $\mathsf{A}$ alive ($8 \le 8$),
$\mathsf{B}$ dead; level 2: $\mathsf{AA} \mapsto 80$, $\mathsf{BA} \mapsto
71$ (mod 81), both $> 8$, dead — empty at $t = 2$.  Consistency: whenever
$2t_c \le 40$, the table value $H_{2t_c}$ indeed exceeds $T$ ($H_{10} =
3690 > 60$, $H_{18} = 336302 > 4000$, $H_{20} = 24213780 > 10^6$, $H_{24}
= 131271758 > 10^8$, $H_{32} = 35219204676 > 10^{10}$, $H_{38} =
4160427700707 > 10^{12}$) — two independent computations of the same floor.

**(e) Kill theorem.** Let $(a,b)$ be contracting, $a \ge 1$, and let a
ladder rung $(T, t_c)$ satisfy $s_{\max}(a,b) \le T$ and $t_c \le a + b -
1$.  Suppose an integral cycle existed.  By automatic positivity (Step 0)
it is positive; by the sieve (Step 0 with $g = 3$) some word $w$ of the
packet has $E_w = Dm + Qk$ with $m \ge 1$, $k \ge 0$, $3 \mid m + k$; by
Step 3, $s = (m+k)/3 \in [1, s_{\max}] \subseteq [1, T]$; by Step 4(d),
$s \equiv \sigma(w) \bmod 3^{2t_c}$ (legitimate since $2t_c \le 2L - 1$).
This contradicts the certificate (c).  Hence **no integral cycle of any
sign exists in the packet** — any length $R \ge 1$, arbitrary branch orders
(the sieve quantifies over arbitrary constant sequences from the complete
alphabet), arbitrary repetition, no least-period assumption.
$\blacksquare$

### Step 6 — coverage: the Main Theorem (T-9925.7)

**(a) Row-coverage monotonicity.** If rung $(T, t_c)$ covers $(a, b')$ for
some contracting $b'$ — i.e. $s_{\max}(a, b') \le T$ and $t_c \le a + b' -
1$ — then it covers $(a, b)$ for every $b \ge b'$: $s_{\max}(a,b) \le
s_{\max}(a, b')$ (Step 2) and $a + b - 1 \ge a + b' - 1 \ge t_c$.  So one
check at $b' = b_0(a)$ closes the entire row, and one check at $b' = b_2(a)$
closes the row's tail in the partial rows $449..469$.

**(b) The scan.** The finite exact evaluation T7 verifies, for every $1 \le
a \le 448$, that some ladder rung covers $(a, b_0(a))$.  With Step 5(e)
this closes **every contracting packet with $1 \le a \le 448$** — no
integral cycle at all.  The same scan shows rows $449 \le a \le 469$ are
covered for all $b \ge b_2(a)$, where $b_2(a) \le b_0(a) + 6$, with
exactly the 27 packets listed in the Statement uncovered; and for $a \ge
470$, $S_a > 10^{24}$ (exactly: $S_{470} = 1100742031687924597138952
\approx 1.10\cdot10^{24}$, and $S_a$ is nondecreasing in $a$ there —
$9\cdot 9^a\,8^a \ge 8\cdot 8^a\,9^a$ gives $\lfloor(9/8)^{a+1}\rfloor \ge
\lfloor(9/8)^a\rfloor$), so
$s_{\max}(a,b) \ge S_a > 10^{24}$ for every $b$: no rung of the present
ladder covers any packet of those rows.

**(c) The supercritical side and $a = 0$.** For $b < b_0(a)$, $a \ge 1$:
Step 7 below.  For $a = 0$: the single constant is $E = 0$, and a cycle
satisfies $(16^{bR} - 9^{bR})\,y_0 = 0$ with $16^{bR} \ne 9^{bR}$, so
$y_0 = 0$; $y \equiv 0$ is indeed fixed ($16\cdot0 = 9\cdot0$), physically
the trivial cycle at $n = 1$ (T-9924 Step 4(vii)).

**(d) Assembly and classification.** Fix $0 \le a \le 448$ and any $b \ge
0$.  If $a = 0$: only $y \equiv 0$.  If $a \ge 1$, $b \ge b_0(a)$: no
integral cycle at all by (b).  If $a \ge 1$, $b < b_0(a)$: supercritical
by T-9925.1, and by Step 7 every integral cycle (if any) has all states
$< 0$.  Since the physical domain is $y \ge 0$ ($n = 2y + 1 \ge 1$), the
only cycle of the family meeting it is $y = 0$ under all-$\mathsf{B}$.
For rows $1 \le a \le 5$ this re-derives T-9924.7's contracting closures
by the present mechanism (T7 verifies: the gate packets have $s_{\max} =
0$, i.e. an empty sieve target set — L-9923.2c's gate — and the five
exceptional contracting packets $(3,1), (4,1), (4,2), (5,2), (5,3)$ are
covered by the rungs $(2,1)$ and $(8,2)$); agreement with T-9924's own
proofs is recorded as consistency, and T-9924.7 is also available as the
citation for $a \le 5$, so nothing rests on this re-derivation.

**(e) Physical corollary.** By T-9924.1(e) (PROVED; legality $=$
integrality and the reduction of legal macro concatenations to integral
cycles with $y \ge 0$), a legal Collatz realization of a cycle by complete
weight-$(a,b)$ macros, $a \le 448$, forces the all-$\mathsf{B}$ fixed
point: $a = 0$, $n_0 = 1$.

**(f) Letter-level corollary.** A cyclic letter word with per-period totals
$(\alpha, \beta)$, read from any starting point, is one complete
weight-$(\alpha, \beta)$ macro cycling with $R = 1$ (T-9924's Corollary 2
mechanism, restated).  If it has a state $y \ge 0$ and is not $y \equiv 0$:
$\beta = 0$ or supercritical totals die by Step 7 ($E = 3(9^\alpha -
8^\alpha) > 0$ resp. $E_{w} > 0$); contracting totals with $\alpha \le
448$ die by (b); contracting totals with $\alpha \ge 449$ covered by the
ladder die by Step 5(e).  What survives is exactly: per-period totals in
the resisting set of the Statement.  $\blacksquare$

### Step 7 — supercritical completion (T-9925.8)

Let $a \ge 1$, $Q < P$ (by T-9925.1 exactly the packets with $b < b_0(a)$,
which include every $(a, 0)$), and let $(y_t)$ be an integral cycle on
words $w_0, \dots, w_{R-1}$.  Unrolling the macro relation $R$ times
(induction identical to T-9924 Step 4(vi), which is L-9923's Lemma A):
$$\big(Q^R - P^R\big)\, y_0 \;=\; \sum_{t=0}^{R-1} P^{\,R-1-t} Q^{\,t}\,
E_{w_t} \;\ge\; G_R\,E_{\min} \;>\; 0,$$
because every $E_w \ge E_{\min} = 3\cdot9^b(9^a - 8^a) > 0$ for $a \ge 1$
and the coefficients are positive.  But $Q < P$ makes $Q^R - P^R < 0$, so
$y_0 < 0$; anchoring at any position (rotation, as in L-9923's Lemma C)
gives $y_t < 0$ for every $t$.  So no integral cycle contains a state
$\ge 0$: no positive, zero-touching, or physical cycle exists in any
supercritical packet.  Along any forward-integral orbit with $y_0 > 0$:
$y_{t+1} = (P y_t + E_{w_t})/Q > (P/Q)\,y_t$, so $y_t > (P/Q)^t y_0 \to
\infty$ (divergence).  This is T-9924 Step 4(vi) with $(5,1)$ replaced by
an arbitrary supercritical $(a,b)$; nothing in the argument used the
specific packet.  $\blacksquare$

### Step 8 — Q-9925: the parameter-uniform floor problem (formulation and reductions)

**(a) König reduction.** The alive tree at threshold $T$ is finitely
branching.  If $H_d \le C$ for every $d$, then for every $t$ the level-$t$
alive set at threshold $C$ is nonempty (a suffix attaining $H_{2t} \le C$
traces an alive path, as in Step 5(c)); by König's lemma there is an
infinite path, i.e. an infinite sequence $u = (r_1, r_2, \dots)$ all of
whose truncations are alive.  The partial sums $\sigma(u_t)$ converge in
$\mathbb{Z}_3$ (the $\delta$-term has $\nu_3 = 2\delta$) to $\sigma(u) \in
\mathbb{Z}_3$, and the alive conditions force: the residues $r_t$ of
$\sigma(u)$ mod $9^t$ form a nondecreasing-in-information chain with
least representatives bounded by $C$ (or $\equiv 0$ with $9^t \le C$,
which fails for large $t$) — hence they are eventually constant, equal to
some integer $s^* \in [1, C]$, and $\sigma(u) = s^* \in \mathbb{Z}^+$.
Conversely if $\sigma(u) = s^* \in \mathbb{Z}^+$ for some infinite $u$,
then for every $t$ with $9^t > s^*$ the length-$t$ truncation realizes the
least positive residue $s^*$, so $H_{2t} \le s^*$ for all large $t$, and
$\sup_d H_d \le s^*$ by monotonicity of the tail.  **Hence: $\sup_d H_d = \infty
\iff$ no infinite letter sequence has $\sigma(u) \in \mathbb{Z}^+$.**

**(b) Consequence of a positive answer.** If $\sup_d H_d = \infty$, then
for every $a \ge 1$ pick $d(a)$ with $H_{d(a)} > S_a$ and a certificate
depth; the window condition $t_c \le a + b_0(a) - 1$ holds for all large
$a$ automatically (the alive tree at threshold $T$ dies within $t_c(T)
\approx \log_9 T + O(\log\log T)$ levels empirically, and in any case
$t_c$ may be taken $\le$ any depth at which the certificate lands, while
$L \ge a$); small-$b$ packets are covered by rungs at $T \ge
s_{\max}(a, b_0(a))$, which is finite for every fixed $(a, b_0)$.  Modulo
the (finite, effective, per-$a$) certificate computations, **a positive
answer to Q-9925(A) closes the complete contracting phase**, which with
Step 7 would be the full classification of the fixed-weight family on
$y \ge 0$.  A quantitative floor $H_d \ge c\lambda^d$ (Q-9925(B)) would
make the whole scheme uniform-effective with explicit row-by-depth
bookkeeping.

**(c) What the problem is really asking (structural remark).** $\sigma(u)$
is a 3-adically convergent series of rationals with denominators powers of
$2$, indexed by the letter tree; Q-9925(A) asks that it avoid the positive
integers.  This is the same *"does a $p$-adic phase path hit an integer"*
shape as the $m_N$ dichotomy of the six-branch chart (L-9916, issue #58),
now on the cycle side and 3-adic instead of 2-adic — the two frontiers of
the program are structurally twin questions.  Note the asymmetry proved
here: the **2-adic** analogue ($\mu$, prefix-local) genuinely admits small
integer values at all computed depths (the prefix floor table, `H2` in
T5, grows much more slowly: $2697188693$ at $d = 45$ against
$26048632820598$ at $d = 40$ on the suffix side), which is why the suffix
(3-adic) side, not the prefix side, carries the theorem.

---

## Dependency audit

| Dependency | Status | Where used |
|---|---|---|
| NOTATION.md conventions | — | exact arithmetic, empty sums, status semantics; epistemic note (Definitions). |
| T-9924 D-9924.1–.2 (blocks, macros, packets, integral cycles) | PROVED | the setting (Statement); nothing re-proved. |
| T-9924.2 (macro algebra: $Q, P$ order-free; $E_w$ formula; extrema; $3 \mid E_w$; swap increments $\equiv 0 \bmod 21$) | PROVED | Step 0 (restated); Steps 3–5 use the $E_w$ formula throughout. |
| T-9924.4(a) (automatic positivity) | PROVED | Step 0 (restated with 3-line proof sketch); Step 5(e). |
| T-9924.1(e), T-9924.7 (physical reduction; the $a \le 5$ theorem) | PROVED | Step 6(d)–(f): citation for $a \le 5$ and the physical corollary. |
| L-9923.2 (2a)+(2b) (minimum-edge sieve, $g$-refinement) | PROVED | Step 0 (restated); Steps 3, 5(e). |
| L-9923.3(ii) (supercritical sign) | PROVED | Step 0 (restated); Step 7 re-derives inline via the unrolled cycle equation, so Step 7 is self-contained. |
| External "T-9609/9610/9611" (source program's branch) | UNVERIFIED, external | Provenance only.  **Not used anywhere.** |

No cited claim is below PROVED status; no circularity (this file cites only
L-9923 and T-9924, neither of which cites T-9925).  Nothing assumes the
Collatz conjecture or its negation.

## Gap audit

Deliberate search per README §8:

- **Hidden finiteness assumptions:** none.  All cycle statements quantify
  over all lengths, branch orders, repetitions; the only finite objects are
  the explicitly finite evaluations flagged in the Definitions (epistemic
  note), each entering as the value of a named constant ($H_d$, $t_c(T)$,
  the coverage scan over $1 \le a \le 470$, the $b_0/b_1$ tables).
- **Quantifier order:** the kill theorem fixes the packet, then the cycle,
  then extracts $(w, m, k, s)$; the certificate is a universally quantified
  statement over words proved before any cycle is assumed.  $H_d$ does not
  depend on $(a,b)$ — that is the point — and the suffix superset argument
  (suffixes not realizable inside a given packet only add kill obligations,
  never remove any) is spelled out in Step 5(c)'s padding remark.
- **Window bookkeeping (the delicate spot):** the congruence $s \equiv
  \sigma(w)$ holds mod $3^{2L-1}$, one factor of $3$ short of $P = 3^{2L}$;
  certificates are used only at depth $2t_c \le 2L - 1$, i.e. $t_c \le L -
  1$, and this inequality is checked packet-by-packet in the coverage scan
  (T7) and proved monotone along rows (Step 6(a)).  An off-by-one here
  would invalidate rows with the shortest words; the re-closure of rows
  $1..5$ (independent of T-9924) exercises exactly the tightest windows
  ($t_c = 1$ at $L = 4$, $t_c = 2$ at $L = 5$).
- **Boundary cases:** $a = 0$ (Step 6(c)); $b = 0$ (supercritical, Step 7);
  $R = 1$ fixed points (included; the sieve's $k = 0$); multiple minima
  (any anchor works — L-9923.2 as restated); $s$-blocks at $s = S_a$
  (equality case of $F_s > 0$ handled via $8^a \nmid 9^a$); $\rho$ at
  $b = b_0$ (contracting guaranteed, denominators positive); ties $Q = P$
  impossible (parity).
- **Sign errors under the flipped regime:** Step 7's inequality chain
  checked at $R = 1$: $(Q - P)y_0 = E > 0$ with $Q - P < 0$ forces $y_0 <
  0$ ✓.
- **Least-period subtleties:** none used anywhere.
- **Empirical vs. exact:** the only EMPIRICAL-labelled statement is the
  floor growth-rate remark in Q-9925(B); no theorem cites it.
- **Assumptions equivalent to Collatz:** none; all statements are theorems
  about the abstract affine family, physical corollaries route through
  T-9924.1(e).
- **The 27 exceptions and rows $\ge 470$:** stated as NOT closed everywhere
  they appear (Scope, Statement, Honest scope box); no sentence claims
  more than the ladder proves.

No gaps found by the author; the verifier probe list is in Remaining
uncertainty.

## Adversarial tests

**Finite verification and finite exact evaluation — see the epistemic note
in Definitions.**  Exact integer arithmetic only (`fractions.Fraction` for
exact rational monotonicity; no floats anywhere).  Deterministic (fixed
seed 99250 for the one randomized identity spot-check; everything else is
enumeration).  Script kept at `scratchpad/p19/t9925_tests.py`
(session-local); full code inline below, byte-identical to the executed
file; runtime $\approx 4$ minutes on CPython 3, dominated by the
$T = 10^{24}$ certificate (T6).  Design notes — what each test attacks:

1. **T1** attacks T-9925.1: every $b_0(a)$, $a \le 60$, is certified by the
   two defining integer inequalities, and no tie $8^a16^b = 9^{a+b}$ exists
   near the boundary.
2. **T2** attacks T-9925.2 where a slip would be silent: strict decrease of
   $\rho$ and of $Q/D$, $\rho > \tau_a$, and the approach to $\tau_a$, all
   in exact rational arithmetic, 25 consecutive $b$ per row, $a = 6..12$;
   also $s_{\max}$ nonincreasing.
3. **T3** enumerates **all** 1013 words with $a+b \le 9$, $a \ge 1$, and
   checks every constant law of T-9925.4 exactly: $\nu_2 = 4\ell_B$,
   $\nu_3 = 1 + 2t_B$, the $16/9$-reduction, the mod-8 unit, the
   $\bmod\,3^{3+2t_B}$ law, the mod-9 sign rule $3(-1)^{a-1}$ (the
   commissioned all-constants mod-9 enumeration), $27 \mid E$ for trailing
   $\mathsf{B}$, and mod-21 packet rigidity on every full alphabet.
4. **T4** attacks T-9925.5: on the same 1013 words, the defining identities
   $E_w \equiv 3\sigma Q \bmod 3^{2L}$ and $E_w \equiv D\mu \bmod 2^e$, the
   suffix/prefix locality windows, and 64 synthetic $(m,k)$ target
   congruences $Dm + Qk \equiv 3sQ \bmod 3^{2L}$, $\equiv Dm \bmod 2^e$.
5. **T5** recomputes the $H_3$ (suffix, $d \le 40$) and $H_2$ (prefix,
   $d \le 45$) tables by direct dynamic programming over all suffixes /
   prefixes and asserts the tabulated values and monotonicity — the direct
   computation is structurally different from T6's pruned recursion, so the
   two implementations cross-check each other.
6. **T6** runs the fourteen floor certificates of Step 5(d) — the
   load-bearing computation of the file — and verifies each against the
   direct $H_3$ table wherever both exist, plus the two hand-checked rungs.
7. **T7** performs the coverage scan of Step 6: $A_{\text{complete}} =
   448$, $A_{\text{tail}} = 469$, the exact 27 exceptional packets, the
   re-closure of rows $1..5$ (with the covering rungs printed), and
   $s_{\max} = 0$ for sample gate packets.
8. **T8** attacks T-9925.3: the $F_s$ identity on 200 random $(a,b,s)$; the
   $(S_a, b_1)$ table for $a = 6..12$; and the exact equality of the
   admissible $(m,k)$ set with $\mathcal{T}_\infty(a)$ at $b = b_1(a)
   \ldots b_1(a)+3$, plus its strict enlargement at $b_1(a) - 1$ where
   contracting.
9. **T9** is the commissioned direct-separation check, strengthened: for
   $a = 6..12$ and the first three contracting $b$ of each row, the full
   alphabet (up to 6188 constants) is intersected with the full sieve
   target set — empty every time.  (The kill is $b$-uniform, so "periods in
   $b$" degenerate; three consecutive $b$ per row are shown.)
10. **T10** is the mandatory $a \le 5$ gate: every packet datum of T-9924
    Step 4 — $Q, P, D$, the constants (counts $4, 5, 15, 21, 56, 6$),
    extrema, widths, target sets $\{4893, 9786\}$, $\{1551405\}$,
    $\{10816917, 15599886\}$, $\{273513021, 316559742\}$, and the residue
    verdicts mod 7/9/8 — reproduced byte-exactly from this file's
    independent code.
11. **T11** verifies the supercritical region: all 188 packets with $b <
    b_0(a)$, $a \le 40$, have $Q < P$ and $E_{\min} > 0$ (the two
    hypotheses of Step 7), and the $a = 0$ row's rigidity.
12. **T12** hunts for cycles directly where the theorem says none exist:
    exhaustive confined-box graph searches in eight packets with $a \ge 6$
    — including the commissioned $(6,2), (7,2), (6,3)$ — each box carrying
    **zero** integral macro edges (reproducing T-9924 V.4's 168
    divisibility failures at $(6,2)$); and cycle-equation enumerations over
    all constant sequences at small $R$ (2328 more sequences), all with no
    integral solution.

```python
#!/usr/bin/env python3
"""
Adversarial tests for T-9925 (research/foundations/T-9925-contracting-phase-classification.md).
FINITE VERIFICATION AND FINITE EXACT EVALUATION -- see the file's epistemic note.
Agent: fable-02-p19.  Date: 2026-07-27.  Exact integer arithmetic throughout
(Python ints; fractions.Fraction only for exact rational monotonicity checks).
Deterministic: fixed seed 99250 for the one randomized identity spot-check.
Run: python3 t9925_tests.py   (CPython >= 3.8, stdlib only; ~4-5 minutes,
dominated by the T = 10^24 phase-floor certificate).
"""
import random, time
from fractions import Fraction
from itertools import combinations, product as iproduct

rng = random.Random(99250)
fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label, flush=True)

QA, CA, QB, CB = 8, 3, 16, 0     # letters: A: 8y'=9y+3, B: 16y'=9y

def word_QPE(w):
    Q, P, E = 1, 1, 0
    for ch in w:
        q, c = (QA, CA) if ch == 'A' else (QB, CB)
        Q, P, E = Q * q, 9 * P, 9 * E + c * Q
    return Q, P, E

def packQPD(a, b):
    Q = 8**a * 16**b; P = 9**(a + b)
    return Q, P, Q - P

def Emin(a, b): return 3 * 9**b * (9**a - 8**a)
def Emax(a, b): return 3 * 16**b * (9**a - 8**a)

def alphabet(a, b):
    L = a + b
    return sorted(word_QPE(''.join('A' if i in S else 'B' for i in range(L)))[2]
                  for S in combinations(range(L), a))

def b0(a):
    b = 0
    while 8**a * 16**b <= 9**(a + b):
        b += 1
    return b

def S_a(a): return 9**a // 8**a - 1

def b1(a):
    Sa = S_a(a); b = b0(a)
    while not (Emax(a, b) < 3 * (Sa + 1) * packQPD(a, b)[2]):
        b += 1
    return b

def smax(a, b):
    return Emax(a, b) // (3 * packQPD(a, b)[2])

def rho(a, b):
    return Fraction(Emax(a, b), packQPD(a, b)[2])

def v2(n):
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k
def v3(n):
    k = 0
    while n % 3 == 0: n //= 3; k += 1
    return k
def ceildiv(x, y): return -((-x) // y)

# ---------------------------------------------------------------- T1: region
B0 = {a: b0(a) for a in range(0, 31)}
print("T1 b0 table (a: least contracting b):", B0, flush=True)
for a in range(1, 61):
    bb = b0(a)
    check(f"T1 cert a={a}", 8**a * 16**bb > 9**(a + bb)
          and (bb == 0 or 8**a * 16**(bb - 1) < 9**(a + bb - 1)))
    check(f"T1 notie a={a}", all(8**a * 16**b != 9**(a + b) for b in range(bb + 2)))
print("T1: b0 certificates and no-tie checks pass for a <= 60", flush=True)

# ------------------------------------------------- T2: rho / tau / Q/D limits
for a in range(6, 13):
    tau = Fraction(3 * (9**a - 8**a), 8**a)
    prev = None
    for b in range(b0(a), b0(a) + 25):
        r = rho(a, b)
        Q, P, D = packQPD(a, b)
        check(f"T2 rho>tau a={a} b={b}", r > tau)
        if prev is not None:
            check(f"T2 rho dec a={a} b={b}", r < prev)
            check(f"T2 smax dec a={a} b={b}", smax(a, b) <= smax(a, b - 1))
            Qp, Pp, Dp = packQPD(a, b - 1)
            check(f"T2 Q/D dec a={a} b={b}", Fraction(Q, D) < Fraction(Qp, Dp))
        check(f"T2 Q/D>1 a={a} b={b}", Fraction(Q, D) > 1)
        prev = r
    check(f"T2 limit a={a}", rho(a, b0(a) + 40) - tau < Fraction(1, 10**6))
print("T2: rho strictly decreasing to tau_a; Q/D strictly decreasing to 1 (a=6..12)", flush=True)

# ------------------------- T3: constant laws on ALL words with a+b <= 9, a >= 1
nw = 0
for L in range(1, 10):
    for wt in iproduct('AB', repeat=L):
        w = ''.join(wt)
        a, b = w.count('A'), w.count('B')
        if a == 0:
            continue
        Q, P, E = word_QPE(w)
        e = 3 * a + 4 * b
        lB = len(w) - len(w.lstrip('B'))
        tB = len(w) - len(w.rstrip('B'))
        core = w.strip('B')
        check(f"T3 v2 {w}", v2(E) == 4 * lB)
        check(f"T3 v3 {w}", v3(E) == 1 + 2 * tB)
        check(f"T3 red {w}", E == 16**lB * 9**tB * word_QPE(core)[2])
        check(f"T3 unit2 {w}", (E // 16**lB) % 8 == 3)
        M27 = 3**(3 + 2 * tB)
        check(f"T3 mod27 {w}", E % M27 == (3**(1 + 2 * tB) * pow(2, e - 4 * tB - 3, M27)) % M27)
        if w[-1] == 'A':
            check(f"T3 mod9 {w}", E % 9 == (3 * (-1)**(a - 1)) % 9)
        else:
            check(f"T3 27|E {w}", E % 27 == 0)
        check(f"T3 mod8 {w}", E % 8 == (3 if w[0] == 'A' else 0))
        nw += 1
# mod-21 packet rigidity, full alphabets a+b <= 9
for L in range(2, 10):
    for a in range(1, L + 1):
        b = L - a
        Es = alphabet(a, b)
        check(f"T3 mod21 ({a},{b})", len({E % 21 for E in Es}) == 1
              and Es[0] % 21 == Emin(a, b) % 21)
print(f"T3: valuation/unit/mod-9/mod-27/mod-8/mod-21 laws verified on {nw} words (a+b<=9)", flush=True)

# ---------------------------- T4: master phase congruences sigma / mu, locality
def sigma_of(w, mod):
    Q, P, E = word_QPE(w)
    return (E // 3 * pow(Q, -1, mod)) % mod

def sigma_suffix(u, mod):
    tot, qp = 0, 1
    for delta in range(len(u)):
        ch = u[len(u) - 1 - delta]
        qp *= QA if ch == 'A' else QB
        if ch == 'A':
            tot += 9**delta * pow(qp, -1, mod)
    return tot % mod

def mu_of(w, mod):
    Q, P, E = word_QPE(w)
    return (E * pow((Q - P) % mod, -1, mod)) % mod

def mu_prefix(v, mod):
    tot, qp = 0, 1
    for j, ch in enumerate(v, start=1):
        if ch == 'A':
            tot += pow(9, -j, mod) * qp
        qp *= QA if ch == 'A' else QB
    return (-3 * tot) % mod

nchk = 0
for L in range(1, 10):
    for wt in iproduct('AB', repeat=L):
        w = ''.join(wt)
        a, b = w.count('A'), w.count('B')
        if a == 0:
            continue
        e = 3 * a + 4 * b
        Q, P, E = word_QPE(w)
        # defining identities: E = 3*sigma*Q mod 3^{2L}; E = D*mu mod 2^e
        sg = sigma_of(w, 3**(2 * L - 1))
        check(f"T4 sigdef {w}", (3 * sg * Q - E) % 3**(2 * L) == 0)
        mu = mu_of(w, 2**e)
        check(f"T4 mudef {w}", ((Q - P) * mu - E) % 2**e == 0)
        # locality windows
        for t in (1, 2, 3, 4):
            if t <= L - 1:
                check(f"T4 sigloc {w} t={t}", sigma_of(w, 9**t) == sigma_suffix(w[-t:], 9**t))
        for d in (3, 6, 8):
            J = d // 3 + 1
            if J <= L:
                check(f"T4 muloc {w} d={d}", mu_of(w, 2**d) == mu_prefix(w[:J], 2**d))
        nchk += 1
# synthetic min-edge data: E := D*m + Q*k  ==>  s == sigma-form, m == mu-form
nsyn = 0
for _ in range(200):
    a = rng.randint(1, 9); b = rng.randint(b0(a), b0(a) + 3)
    Q, P, D = packQPD(a, b)
    L = a + b; e = 3 * a + 4 * b
    m = rng.randint(1, 50); k = rng.randint(0, 30)
    if (m + k) % 3:
        continue
    s = (m + k) // 3
    tau = D * m + Q * k
    check("T4 tau3", tau % 3**(2 * L) == (3 * s * Q) % 3**(2 * L))
    check("T4 tau2", tau % 2**e == (D * m) % 2**e)
    nsyn += 1
print(f"T4: sigma/mu defining identities + locality on {nchk} words; "
      f"{nsyn} synthetic (m,k) target congruences", flush=True)

# ----------------------------------------- T5: H tables by direct enumeration
def H3_table(dmax):
    out = {}
    M = 3**dmax
    states = [(0, 1)]
    D = 0
    for d in range(2, dmax + 1):
        need = (d + 1) // 2
        while D < need:
            p9 = pow(9, D, M)
            states = [((sg + p9 * pow(qp * q, -1, M)) % M if q == QA else sg, qp * q)
                      for sg, qp in states for q in (QA, QB)]
            D += 1
        m3 = 3**d
        out[d] = min(sg % m3 for sg, _ in states if sg % m3)
    return out

def H2_table(dmax):
    out = {}
    M = 2**dmax
    states = [(0, 1)]
    J = 0
    for d in range(3, dmax + 1):
        need = d // 3 + 1
        while J < need:
            i9 = pow(9, -(J + 1), M)
            states = [((sm + i9 * qp) % M if q == QA else sm, qp * q)
                      for sm, qp in states for q in (QA, QB)]
            J += 1
        m2 = 2**d
        vals = [(-3 * sm) % m2 for sm, _ in states]
        out[d] = min(v for v in vals if v)
    return out

t0 = time.time()
H3 = H3_table(40)
H2 = H2_table(45)
expect3 = {2: 8, 3: 17, 4: 45, 10: 3690, 18: 336302, 24: 131271758,
           32: 35219204676, 38: 4160427700707, 40: 26048632820598}
for d, v in expect3.items():
    check(f"T5 H3[{d}]", H3[d] == v)
expect2 = {3: 5, 9: 189, 18: 5629, 27: 30677, 36: 110085376, 45: 2697188693}
for d, v in expect2.items():
    check(f"T5 H2[{d}]", H2[d] == v)
check("T5 H3 monotone", all(H3[d] <= H3[d + 1] for d in range(2, 40)))
check("T5 H2 monotone", all(H2[d] <= H2[d + 1] for d in range(3, 45)))
print(f"T5: H3 (d<=40) and H2 (d<=45) tables match; monotone; {time.time()-t0:.1f}s", flush=True)
print("    H3:", {d: H3[d] for d in (2, 3, 4, 10, 18, 24, 32, 40)}, flush=True)
print("    H2:", {d: H2[d] for d in (3, 9, 18, 27, 36, 45)}, flush=True)

# --------------------------------------------- T6: phase-floor certificates
def cert(T, margin=35, tcap=200):
    tstar = 0
    while 9**tstar <= T:
        tstar += 1
    tg = tstar + margin
    M = 3**(2 * tg)
    inv8 = pow(8, -1, M); inv16 = pow(16, -1, M)
    states = {(0, 0)}
    maxa = 1
    for t in range(1, tcap + 1):
        if t > tg - 2:
            return None
        p9 = pow(9, t - 1, M)
        mod9t = 9**t
        addA = {iA: (p9 * pow(inv8, iA + 1, M) * pow(inv16, t - 1 - iA, M)) % M
                for iA in range(t)}
        new = set()
        for (sg, iA) in states:
            r = sg % mod9t
            if (r and r <= T) or (r == 0 and mod9t <= T):
                new.add((sg, iA))
            sg2 = (sg + addA[iA]) % M
            r2 = sg2 % mod9t
            if (r2 and r2 <= T) or (r2 == 0 and mod9t <= T):
                new.add((sg2, iA + 1))
        states = new
        maxa = max(maxa, len(states))
        if not states:
            return (t, maxa)
    return None

LADDER = []
print("T6 certificate ladder (each line proves H_(2t) > T):", flush=True)
for T in (2, 8, 60, 4000, 10**6, 10**8, 10**10, 10**12, 10**14, 10**16,
          10**18, 10**20, 10**22, 10**24):
    t0 = time.time()
    res = cert(T)
    check(f"T6 cert {T}", res is not None)
    tc, ma = res
    LADDER.append((T, tc))
    print(f"    T={T}: depth t={tc}, max_alive={ma}, {time.time()-t0:.1f}s", flush=True)
# consistency with the H3 table where both exist
for (T, tc) in LADDER:
    if 2 * tc in H3:
        check(f"T6 cons {T}", H3[2 * tc] > T)
# hand-checkable smallest rungs
check("T6 hand d2", H3[2] == 8 and 8 > 2)          # cert(2) at t=1
check("T6 hand d4", H3[4] == 45 and 45 > 8)        # cert(8) at t=2
print("T6: ladder consistent with H3 table and hand values", flush=True)

# --------------------------------------------------- T7: coverage of the rows
def covering(a, b):
    sm = smax(a, b); L = a + b
    for (T, tc) in LADDER:
        if sm <= T and tc <= L - 1:
            return (T, tc)
    return None

A_complete = None
exceptions = []
for a in range(1, 471):
    bb = b0(a)
    if covering(a, bb) is not None:
        continue
    bad = []
    b = bb
    while covering(a, b) is None and b < bb + 500:
        bad.append(b); b += 1
    if A_complete is None:
        A_complete = a - 1
    exceptions.append((a, bad))
check("T7 A_complete", A_complete == 448)
bestT = max(T for T, _ in LADDER)
a = 6
while S_a(a) <= bestT:
    a += 1
A_tail = a - 1
check("T7 A_tail", A_tail == 469)
exc_flat = [(a, b) for (a, bad) in exceptions if a <= 469 for b in bad]
check("T7 exc count", len(exc_flat) == 27)
print(f"T7: A_complete={A_complete}, A_tail={A_tail}; "
      f"exceptional packets in rows 449..469 ({len(exc_flat)}):", flush=True)
print("   ", exc_flat, flush=True)
check("T7 row470", exceptions[-1][0] == 470 or any(a == 470 for a, _ in exceptions))
# rows 1..5 re-closure by the same ladder (T-9924's exceptional contracting packets)
for (a, b) in [(3, 1), (4, 1), (4, 2), (5, 2), (5, 3)]:
    cov = covering(a, b)
    check(f"T7 reclose ({a},{b})", cov is not None)
    print(f"    packet ({a},{b}): smax={smax(a,b)}, covered by rung {cov}", flush=True)
# gate packets have empty target sets (smax = 0)
for (a, b) in [(1, 1), (2, 1), (3, 2), (4, 3), (5, 4)]:
    check(f"T7 gate ({a},{b})", smax(a, b) == 0)
print("T7: rows 1..5 re-closed independently (gate rows have smax=0)", flush=True)

# ------------------------------- T8: stabilization of the target set (a=6..12)
def targets_mk(a, b):
    Q, P, D = packQPD(a, b)
    EM = Emax(a, b)
    out = set()
    m = 1
    while D * m <= EM:
        k = 0
        while D * m + Q * k <= EM:
            if (m + k) % 3 == 0:
                out.add((m, k))
            k += 1
        m += 1
    return out

for _ in range(200):
    a = rng.randint(1, 15); b = rng.randint(1, 12); s = rng.randint(1, 9)
    check("T8 Fs", Emax(a, b) - 3 * s * packQPD(a, b)[2] - (3 * s - 1) * 9**(a + b)
          == 3 * 16**b * (9**a - (s + 1) * 8**a) + 9**(a + b))
SB = {a: (S_a(a), b1(a)) for a in range(6, 13)}
print("T8 (S_a, b1):", SB, flush=True)
for a in range(6, 13):
    Sa, bb1 = SB[a]
    Tinf = {(3 * s - k, k) for s in range(1, Sa + 1) for k in range(3 * s)}
    for b in range(bb1, bb1 + 4):
        check(f"T8 stab a={a} b={b}", targets_mk(a, b) == Tinf)
    if bb1 - 1 >= b0(a):
        check(f"T8 pre a={a}", targets_mk(a, bb1 - 1) != Tinf)
print("T8: F_s identity; exact target-set stabilization T=T_inf(a) at b1(a) for a=6..12", flush=True)

# ------------------- T9: direct alphabet-vs-target separation (b-uniform kill)
for a in range(6, 13):
    for b in range(b0(a), b0(a) + 3):
        Q, P, D = packQPD(a, b)
        Es = set(alphabet(a, b))
        T = {D * m + Q * k for (m, k) in targets_mk(a, b)}
        check(f"T9 sep ({a},{b})", not (Es & T))
    print(f"T9: rows a={a}: alphabet-target intersection empty at b={b0(a)}..{b0(a)+2} "
          f"(|E|={len(Es)}, |T|={len(T)})", flush=True)

# --------------------------- T10: a <= 5 cross-check gate (T-9924 packet data)
def targets_val(a, b):
    Q, P, D = packQPD(a, b)
    return sorted({D * m + Q * k for (m, k) in targets_mk(a, b)})

Q, P, D = packQPD(3, 1); Es = alphabet(3, 1)
check("T10 (3,1)", (Q, P, D) == (8192, 6561, 1631) and Es == [5859, 7203, 8715, 10416]
      and Es[-1] - Es[0] == 4557 and targets_val(3, 1) == [4893, 9786]
      and all(E % D for E in Es))
Q, P, D = packQPD(4, 1); Es = alphabet(4, 1)
check("T10 (4,1)", (Q, P, D) == (65536, 59049, 6487)
      and Es == [66555, 77307, 89403, 103011, 118320] and all(E % D for E in Es))
Q, P, D = packQPD(4, 2); Es = alphabet(4, 2)
check("T10 (4,2)", (Q, P, D) == (1048576, 531441, 517135) and len(Es) == 15
      and (Es[0], Es[-1]) == (598995, 1893120)
      and targets_val(4, 2) == [1551405] == [3 * D]
      and all(E % 7 == 5 for E in Es) and (3 * D) % 7 == 2)
Q, P, D = packQPD(5, 2); Es = alphabet(5, 2)
t52 = targets_val(5, 2)
check("T10 (5,2)", (Q, P, D) == (8388608, 4782969, 3605639) and len(Es) == 21
      and (Es[0], Es[-1]) == (6386283, 20183808)
      and t52 == [10816917, 15599886] == [3 * D, 2 * D + Q]
      and all(t % 9 == 6 for t in t52) and sorted({E % 9 for E in Es}) == [0, 3])
Q, P, D = packQPD(5, 3); Es = alphabet(5, 3)
t53 = targets_val(5, 3)
check("T10 (5,3)", (Q, P, D) == (134217728, 43046721, 91171007) and len(Es) == 56
      and (Es[0], Es[-1]) == (57476547, 322940928)
      and t53 == [273513021, 316559742] == [3 * D, 2 * D + Q]
      and [t % 8 for t in t53] == [5, 6] and sorted({E % 8 for E in Es}) == [0, 3])
Q, P, D = packQPD(5, 1); Es = alphabet(5, 1)
check("T10 (5,1)", Q == 2**19 == 524288 and P == 3**12 == 531441 and Q < P
      and Es == [709587, 795603, 892371, 1001235, 1123707, 1261488])
print("T10: a<=5 packet data reproduces T-9924 exactly (mandatory gate)", flush=True)

# ------------------------------------------ T11: supercritical region + a = 0
nsup = 0
for a in range(1, 41):
    for b in range(0, b0(a)):
        Q, P, D = packQPD(a, b)
        check(f"T11 ({a},{b})", Q < P and Emin(a, b) > 0)
        nsup += 1
check("T11 a0", all(16**b != 9**b for b in range(1, 9)))
print(f"T11: {nsup} supercritical packets (b < b0(a), a <= 40): Q < P, E_min > 0; "
      f"a=0 row forces y=0", flush=True)

# ----------------------- T12: brute-force confined searches, a >= 6 packets
def confined(a, b):
    Q, P, D = packQPD(a, b)
    Es = alphabet(a, b)
    lo, hi = ceildiv(Es[0], D), Es[-1] // D
    adj = {y: [ (P * y + E) // Q for E in Es
                if (P * y + E) % Q == 0 and lo <= (P * y + E) // Q <= hi ]
           for y in range(lo, hi + 1)}
    WHITE, GREY, BLACK = 0, 1, 2
    col = {y: WHITE for y in adj}
    found = []
    def dfs(u, st):
        col[u] = GREY; st.append(u)
        for v in adj[u]:
            if col[v] == GREY:
                found.append(v)
            elif col[v] == WHITE:
                dfs(v, st)
        st.pop(); col[u] = BLACK
    for y in adj:
        if col[y] == WHITE:
            dfs(y, [])
    return lo, hi, sum(len(x) for x in adj.values()), found

for (a, b) in [(6, 2), (6, 3), (7, 2), (7, 3), (8, 2), (9, 2), (10, 3), (12, 3)]:
    lo, hi, ne, cyc = confined(a, b)
    check(f"T12 ({a},{b})", cyc == [])
    print(f"T12 confined ({a},{b}): box [{lo},{hi}], edges {ne}, cycles {len(cyc)}", flush=True)
Q, P, D = packQPD(6, 2); Es = alphabet(6, 2)
check("T12 (6,2) box", (ceildiv(Es[0], D), Es[-1] // D) == (3, 8) and len(Es) == 28)
check("T12 (6,2) 168", sum((P * y + E) % Q == 0 for y in range(3, 9) for E in Es) == 0)
def cyc_eq(a, b, Rmax):
    Q, P, D = packQPD(a, b)
    Es = alphabet(a, b)
    sols = 0; nseq = 0
    for R in range(1, Rmax + 1):
        den = Q**R - P**R
        for seq in iproduct(Es, repeat=R):
            nseq += 1
            if sum(P**(R-1-t) * Q**t * seq[t] for t in range(R)) % den == 0:
                sols += 1
    return nseq, sols
for (a, b, Rm) in [(6, 2, 2), (7, 2, 2), (6, 3, 1), (8, 2, 1), (9, 2, 1)]:
    nseq, sols = cyc_eq(a, b, Rm)
    check(f"T12 eq ({a},{b})", sols == 0)
    print(f"T12 cycle-eq ({a},{b}) R<={Rm}: {nseq} sequences, 0 integral solutions", flush=True)

print("RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES", flush=True)
```

**Output (verbatim, run 2026-07-27, CPython 3, Linux; identical across
reruns — deterministic):**

```text
T1 b0 table (a: least contracting b): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 13: 3, 14: 3, 15: 4, 16: 4, 17: 4, 18: 4, 19: 4, 20: 5, 21: 5, 22: 5, 23: 5, 24: 5, 25: 6, 26: 6, 27: 6, 28: 6, 29: 6, 30: 7}
T1: b0 certificates and no-tie checks pass for a <= 60
T2: rho strictly decreasing to tau_a; Q/D strictly decreasing to 1 (a=6..12)
T3: valuation/unit/mod-9/mod-27/mod-8/mod-21 laws verified on 1013 words (a+b<=9)
T4: sigma/mu defining identities + locality on 1013 words; 64 synthetic (m,k) target congruences
T5: H3 (d<=40) and H2 (d<=45) tables match; monotone; 4.9s
    H3: {2: 8, 3: 17, 4: 45, 10: 3690, 18: 336302, 24: 131271758, 32: 35219204676, 40: 26048632820598}
    H2: {3: 5, 9: 189, 18: 5629, 27: 30677, 36: 110085376, 45: 2697188693}
T6 certificate ladder (each line proves H_(2t) > T):
    T=2: depth t=1, max_alive=1, 0.0s
    T=8: depth t=2, max_alive=1, 0.0s
    T=60: depth t=5, max_alive=2, 0.0s
    T=4000: depth t=9, max_alive=8, 0.0s
    T=1000000: depth t=10, max_alive=64, 0.0s
    T=100000000: depth t=12, max_alive=256, 0.0s
    T=10000000000: depth t=16, max_alive=1024, 0.0s
    T=1000000000000: depth t=19, max_alive=4096, 0.0s
    T=100000000000000: depth t=22, max_alive=16384, 0.0s
    T=10000000000000000: depth t=25, max_alive=78733, 0.2s
    T=1000000000000000000: depth t=28, max_alive=388257, 1.1s
    T=100000000000000000000: depth t=31, max_alive=1916523, 5.9s
    T=10000000000000000000000: depth t=33, max_alive=8388608, 34.6s
    T=1000000000000000000000000: depth t=37, max_alive=33554432, 158.5s
T6: ladder consistent with H3 table and hand values
T7: A_complete=448, A_tail=469; exceptional packets in rows 449..469 (27):
    [(449, 92), (453, 93), (454, 93), (457, 94), (458, 94), (459, 94), (461, 95), (462, 95), (463, 95), (464, 95), (464, 96), (465, 96), (466, 96), (466, 97), (467, 96), (467, 97), (467, 98), (468, 96), (468, 97), (468, 98), (468, 99), (469, 97), (469, 98), (469, 99), (469, 100), (469, 101), (469, 102)]
    packet (3,1): smax=2, covered by rung (2, 1)
    packet (4,1): smax=6, covered by rung (8, 2)
    packet (4,2): smax=1, covered by rung (2, 1)
    packet (5,2): smax=1, covered by rung (2, 1)
    packet (5,3): smax=1, covered by rung (2, 1)
T7: rows 1..5 re-closed independently (gate rows have smax=0)
T8 (S_a, b1): {6: (1, 3), 7: (1, 4), 8: (1, 5), 9: (1, 7), 10: (2, 5), 11: (2, 7), 12: (3, 6)}
T8: F_s identity; exact target-set stabilization T=T_inf(a) at b1(a) for a=6..12
T9: rows a=6: alphabet-target intersection empty at b=2..4 (|E|=210, |T|=3)
T9: rows a=7: alphabet-target intersection empty at b=2..4 (|E|=330, |T|=3)
T9: rows a=8: alphabet-target intersection empty at b=2..4 (|E|=495, |T|=4)
T9: rows a=9: alphabet-target intersection empty at b=2..4 (|E|=715, |T|=8)
T9: rows a=10: alphabet-target intersection empty at b=3..5 (|E|=3003, |T|=9)
T9: rows a=11: alphabet-target intersection empty at b=3..5 (|E|=4368, |T|=13)
T9: rows a=12: alphabet-target intersection empty at b=3..5 (|E|=6188, |T|=19)
T10: a<=5 packet data reproduces T-9924 exactly (mandatory gate)
T11: 188 supercritical packets (b < b0(a), a <= 40): Q < P, E_min > 0; a=0 row forces y=0
T12 confined (6,2): box [3,8], edges 0, cycles 0
T12 confined (6,3): box [1,4], edges 0, cycles 0
T12 confined (7,2): box [5,13], edges 0, cycles 0
T12 confined (7,3): box [2,6], edges 0, cycles 0
T12 confined (8,2): box [8,24], edges 0, cycles 0
T12 confined (9,2): box [21,65], edges 0, cycles 0
T12 confined (10,3): box [3,15], edges 0, cycles 0
T12 confined (12,3): box [7,34], edges 0, cycles 0
T12 cycle-eq (6,2) R<=2: 812 sequences, 0 integral solutions
T12 cycle-eq (7,2) R<=2: 1332 sequences, 0 integral solutions
T12 cycle-eq (6,3) R<=1: 84 sequences, 0 integral solutions
T12 cycle-eq (8,2) R<=1: 45 sequences, 0 integral solutions
T12 cycle-eq (9,2) R<=1: 55 sequences, 0 integral solutions
RESULT: ALL CHECKS PASSED
```

A byte-for-byte self-check was performed after embedding: the fenced code
block above was extracted from this file and `diff`-compared against the
executed `scratchpad/p19/t9925_tests.py`, and the fenced output block
against the captured run log; both diffs are empty (checker:
`scratchpad/p19/embed_check.py`).

## Remaining uncertainty

All sub-claims are, in the author's assessment, fully proved (with the
epistemic status of the finite exact evaluations stated plainly in the
Definitions, and the single EMPIRICAL label on Q-9925(B)'s growth remark).
Points a verifier should probe first, in order:

1. **The certificate lemma (Step 5(c))** — the heart of the file.  Probe:
   the claim that keeping only $(\sigma \bmod 3^{2t_g}, \#\mathsf{A})$
   loses nothing (the extension increment at level $t$ depends only on
   those data); the least-representative inequality $s \ge r_t$; the
   $r_t = 0$ branch; and the padding remark that converts the word
   statement into the $H_{2t_c} > T$ statement.
2. **The window bookkeeping**: $s \equiv \sigma(w)$ holds mod $3^{2L-1}$
   (one factor of 3 is lost dividing $E \equiv 3sQ$ by 3), certificates
   are applied at depth $2t_c \le 2L-1$; T7's tightest instances are rows
   $1..5$.  Check no use of depth $2L$ anywhere.
3. **Step 3's identity** $E_{\max} - 3sD - (3s-1)P = 3\cdot16^b(9^a -
   (s+1)8^a) + 9^{a+b}$ and the equality-impossibility $8^a \nmid 9^a$ at
   $s = S_a$.
4. **The coverage scan's soundness** (T7): that covering $(a, b_0(a))$
   suffices for the whole row rests on $s_{\max}$ nonincreasing (Step 2)
   — verify the floor interacts correctly with strict decrease of $\rho$
   (T2 checks $s_{\max}$ directly).
5. **Independence of the two floor computations** (T5's DP vs T6's pruned
   recursion): confirm they are genuinely different code paths, and rerun
   both.
6. The **runtime-heavy rung** $T = 10^{24}$ (33.5M alive states): a
   verifier with limited budget can independently confirm any prefix of
   the ladder (each rung is a standalone proof for its own $T$) and scale
   $A_{\text{complete}}$ accordingly — e.g. stopping at $10^{18}$ still
   proves every row $a \le 326$.
7. What is *not* claimed: the 27 packets and rows $a \ge 470$; negative
   supercritical cycles; anything physical beyond T-9924.1(e)'s reduction.

## Suggested next attack

- **Q-9925 itself.** Two concrete routes: (i) a self-similarity /
  automaton argument on the alive tree — the extension increments
  $9^\delta(q\text{-prod})^{-1}$ have a rational generating structure, and
  the alive dynamics may be recognizable enough for a transfer-operator or
  automatic-sequence argument that alive paths die within $O(\log T)$
  levels; (ii) a $p$-adic transcendence/irrationality result for
  $\sigma(u)$ along eventually-periodic $u$ (for *periodic* tails the sum
  is an explicit rational whose integrality can be decided — worth doing
  first: it would close all "eventually periodic" phase paths and turn
  Q-9925 into a statement about aperiodic paths only).
- **Close the 27 packets.** Each needs one deeper certificate ($T \approx
  10^{26}$, projected $\sim$25 minutes and $\sim$130M states with the
  embedded code; memory, not time, is the constraint — a bit-packed or
  disk-backed alive set would do it) — a cheap follow-up file could
  retire rows 449–469 entirely and push $A_{\text{complete}}$ to
  $\sim$490.
- **The 2-adic side.** $H'_d$ (prefix floor) grows too slowly to carry
  rows alone, but jointly constraining $(s, m)$ (same word realizes both
  phases) was not needed here and remains unexploited; it is the natural
  second lever if the 3-adic floor ever stalls.
- **Port the mechanism.** The suffix-phase construction used only: fixed
  letter moduli $q_\ell$ coprime to $3$, $P$ an exact power of $3$, and
  constants $c_\ell \in \{0, 3\}$.  Any block grammar with $P = 3^{2L}$
  and 2-power moduli (L-9922's portability program) inherits the whole
  theory verbatim; drafting the general statement would make T-9925 the
  template rather than a one-off.
- **Independent verification targets:** rerun the ladder with an
  independent implementation (ideally in a different language with native
  big integers); spot-verify $H_{40}$ by the direct DP at $d = 40$;
  re-derive the 27-packet list from scratch.

---
*File authored by fable-02-p19, 2026-07-26/27, on commission as the
extension of T-9924 beyond $a \le 5$, re-aimed mid-work per the
coordinator's supersession notice toward the parameter-uniform floor
(Q-9925).  Status PROPOSED per NOTATION.md conventions; an independent
reviewing agent may upgrade after verification.*
