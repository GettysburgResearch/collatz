# L-9923 — Affine-alphabet cycle collapse (sharp threshold), the cycle-minimum target sieve, and the supercritical sign obstruction

```text
Claim ID:      L-9923
Title:         Integral cycles of finite affine alphabets Q x' = P x + C_i:
               (1) zero-carry collapse for narrow alphabets, with the SHARP
               width threshold W < P + Q (the source spec's W < Q is true but
               not sharp, and its claimed W = Q sharpness example is refuted);
               (2) the cycle-minimum finite target sieve E = D m + Q k, its
               divisibility refinement g | (m + k), and the height gate
               E_max < g D; (3) packet links: constant-word Syracuse rigidity
               re-derived, and the two-line supercritical sign obstruction.
Status:        PROVED
Authoring agent:   fable-02-p17
Reviewing agents:  fable-02-v25 (adversarial review 2026-07-26: PASS)
Created:       2026-07-26
Last updated:  2026-07-26 (status upgraded after independent review, see
               Verification note at end of file)
Dependencies:  research/foundations/NOTATION.md only (conventions: Z^+, empty
               sums/products, status semantics, "computation is finite
               verification"; D-9904/D-9905/D-9908 are used solely to NAME the
               Syracuse objects in L-9923.3(i)). L-9905, L-9912.1, L-9916,
               L-9918.5 are cited as CONTEXT ONLY and are never used; every
               argument below is self-contained.
Scope:         L-9923.1, .1C, .1S, .2a-.2c: all pairs of integers Q > P >= 1,
               all finite alphabets C_1..C_s in Z (s >= 1), all words of all
               lengths R >= 1, all INTEGER states. Positivity of states is
               assumed exactly where stated (L-9923.2, and the range-restricted
               clauses of .1C); L-9923.1 itself needs no positivity.
               L-9923.3(ii): all integers P > Q >= 1, all alphabets with all
               C_i >= 0. The hypothesis P >= 1 is essential for the sharp
               threshold of .1S (the degenerate case P = 0 is flagged and
               excluded). No coprimality of P and Q, and no factorization
               property of D = Q - P, is assumed anywhere.
Related counterexample candidates: none
```

---

## Provenance

The statements and the proof mechanism of L-9923.1 and L-9923.2 are due to an
**external, unpushed session report** supplied by the repository owner. That
session drafted them as "L-9608" and "L-9609", targeting the 96xx namespace
(per the owner, for the PR #47 program; NOTATION.md's reservation list records
96xx against issue #21 — the discrepancy is immaterial here and noted only for
the record). Its branch was never pushed, so no artifact of it exists in this
repository; nothing below cites it as a dependency. This file **re-derives and
proves everything independently** inside the 99xx foundations packet, with the
full README §8 apparatus, and claims no 96xx ID.

Two substantive corrections to the source specification were found during the
re-derivation; the derivations in this file are the authority:

1. **The source's sharpness claim for the collapse theorem is wrong.** It
   asserted that the hypothesis $W < Q$ is sharp, witnessed by an alphabet of
   width exactly $W = Q$ ("two constants differing by exactly $Q$") carrying a
   genuine 2-cycle. No such example exists when $P \ge 1$: any genuine 2-cycle
   forces $(P+Q) \mid (C_{i_0} - C_{i_1})$ with $|C_{i_0}-C_{i_1}| \ge P+Q$,
   and more generally every non-constant integral cycle forces
   $W \ge D(M-m) + 2P \ge P + Q$ (L-9923.1S). The true sharp threshold is
   $W < P + Q$ — strictly weaker as a hypothesis than the source's $W < Q$ —
   attained by the alphabet $\{Q, -P\}$ with the 2-cycle $0 \leftrightarrow 1$.
   The source's example is valid only in the degenerate case $P = 0$, which
   its own setting (and ours) excludes.
2. **No sign hypothesis on the alphabet is needed in the sieve** (the source
   left this unexamined; the task brief asked it to be settled). The floor
   $E \ge D > 0$ on the minimum-edge constant is *derived* from positivity of
   the states, not assumed of the alphabet; alphabets containing negative
   constants do carry positive cycles (explicit family in the Proof and
   Adversarial tests), and the sieve applies to them verbatim.

Credit for the mechanism goes to the source session; responsibility for every
statement and proof below rests with this file.

---

## Statement

### Setting (used throughout)

Fix integers $Q > P \ge 1$ and set the **drift** $D := Q - P \ge 1$. A finite
**affine alphabet** is a list of integers $C_1, \dots, C_s$ ($s \ge 1$), the
**block constants**; block $i$ is the partial map $x \mapsto x'$ on $\mathbb{Z}$
defined by the relation
$$Q\,x' \;=\; P\,x + C_i .$$
A **word** of length $R \ge 1$ is a sequence $w = (i_0, i_1, \dots, i_{R-1})$
of block indices. An **integral cycle on $w$** is a sequence of *integers*
$x_0, x_1, \dots, x_R$ with $x_R = x_0$ and
$$Q\,x_{t+1} \;=\; P\,x_t + C_{i_t} \qquad (0 \le t \le R-1).$$
It is **positive** if every $x_t \ge 1$, **constant** if $x_0 = x_1 = \dots =
x_{R-1}$, and **moving** (non-constant) otherwise. Write
$$C_- := \min_i C_i, \qquad C_+ := \max_i C_i, \qquad W := C_+ - C_- \quad (\text{the width}),$$
$$c_w := \sum_{t=0}^{R-1} P^{\,R-1-t} Q^{\,t}\, C_{i_t}, \qquad
G_R := \sum_{t=0}^{R-1} P^{\,R-1-t} Q^{\,t} .$$
For the states of a fixed cycle put $m := \min_t x_t$, $M := \max_t x_t$.
(Least periods play no role: every statement holds for every closed length-$R$
loop, whether or not $R$ is minimal.)

### L-9923.1 (zero-carry collapse for narrow alphabets)

Let an integral cycle of length $R \ge 1$ exist on some word $w$. Then:

**(a) (cycle equation and convex combination).**
$$\left(Q^R - P^R\right) x_0 \;=\; c_w, \qquad Q^R - P^R \;=\; D\, G_R,
\qquad G_R \ge R \ge 1,$$
and therefore
$$D\,x_0 \;=\; \frac{\sum_{t=0}^{R-1} P^{\,R-1-t} Q^{\,t}\, C_{i_t}}
{\sum_{t=0}^{R-1} P^{\,R-1-t} Q^{\,t}}
\;=\; \sum_{t=0}^{R-1} \omega_t\, C_{i_t},
\qquad \omega_t := \frac{P^{\,R-1-t} Q^{\,t}}{G_R} \in (0,1],
\quad \sum_t \omega_t = 1,$$
a convex combination with strictly positive rational weights of the constants
used along the word. Hence
$$D\,x_0 \;\in\; \big[\min_t C_{i_t},\ \max_t C_{i_t}\big] \;\subseteq\; [C_-,\, C_+],$$
with $\min_t C_{i_t} < D\,x_0 < \max_t C_{i_t}$ strictly as soon as two
distinct constant values occur in $w$. (In particular $G_R \mid c_w$.)

**(b) (edge identity and invariance at every position).** For every
$0 \le t \le R-1$,
$$Q\,(x_{t+1} - x_t) \;=\; C_{i_t} - D\,x_t ,$$
and — because each $x_t$ is the start of the rotated cycle, so (a) applies at
every anchor —
$$D\,x_t \in [C_-, C_+] \ \text{ for every } t, \qquad\text{hence}\qquad
\big|\,Q\,(x_{t+1} - x_t)\,\big| \;\le\; W \ \text{ at every edge.}$$

**(c) (collapse for $W < Q$).** If $W < Q$, then every edge forces
$x_{t+1} = x_t$; the cycle is constant, $x_t = x_0$ for all $t$, and
$$C_{i_t} \;=\; D\,x_0 \qquad \text{for every } t.$$
So every constant used in $w$ equals the single value $D x_0$: the cycle
collapses to a one-block fixed point with $D \mid C_{i_t}$ and quotient
$x_0 = C_{i_t}/D$.

### Corollary L-9923.1C (alphabet-level exclusion)

Assume $W < P + Q$ (in particular whenever $W < Q$; see L-9923.1S for why the
larger bound is available). Let $X \subseteq \mathbb{Z}$ be any set of allowed
states (e.g. $X = \mathbb{Z}^+$, or $X = \{x \ge x_{\mathrm{floor}}\}$). Then:

1. The integral cycles with states in $X$ are **exactly** the constant cycles
   at the values $x = C_i/D$ over those $i$ with $D \mid C_i$ and
   $C_i/D \in X$ (any length, any word using only indices whose constant
   equals $D x$).
2. Consequently, if **no** $C_i$ is divisible by $D$ with quotient in $X$,
   then **no** integral cycle with states in $X$ exists, on any word of any
   length. And regardless of $X$, no moving cycle exists at all.

No coprimality of $P$ and $Q$, no primality or factorization property of $D$,
and no positivity of states is used anywhere in L-9923.1 or .1C.

### L-9923.1S (the sharp threshold; correction of the source spec)

**(i) (span bound).** Every **moving** integral cycle satisfies
$$C_+ \;\ge\; D\,M + P, \qquad C_- \;\le\; D\,m - P, \qquad\text{hence}\qquad
W \;\ge\; D\,(M - m) + 2P \;\ge\; D + 2P \;=\; P + Q .$$
Equivalently: every integral cycle has diameter $M - m \le (W - 2P)/D$
whenever it is moving.

**(ii) (collapse under the weaker hypothesis).** If $W \le P + Q - 1$, every
integral cycle is constant and the full conclusion of L-9923.1(c) holds
verbatim. Since $P \ge 1$, this strictly extends (c): the entire regime
$Q \le W \le P + Q - 1$, which the source hypothesis $W < Q$ does not cover,
also collapses.

**(iii) (sharpness).** The threshold cannot be improved: for every
$Q > P \ge 1$ the two-letter alphabet
$$\{\,C_1, C_2\,\} \;=\; \{\,Q,\ -P\,\}, \qquad W = P + Q,$$
carries the genuine integral 2-cycle $x_0 = 0 \mapsto x_1 = 1 \mapsto x_0$
(blocks in the order $C_1$ then $C_2$): $Q \cdot 1 = P \cdot 0 + Q$ and
$Q \cdot 0 = P \cdot 1 + (-P)$.

**(iv) (2-cycle obstruction; refutation of the source's example).** Any
integral 2-cycle $x_0 \mapsto x_1 \mapsto x_0$ on blocks $i_0, i_1$ satisfies
$$(P + Q)\,(x_1 - x_0) \;=\; C_{i_0} - C_{i_1} .$$
Hence a genuine 2-cycle ($x_1 \ne x_0$) forces $(P+Q) \mid (C_{i_0}-C_{i_1})$
and $|C_{i_0} - C_{i_1}| \ge P + Q$. In particular **two constants differing
by exactly $Q$ can never form a 2-cycle** when $P \ge 1$ (since
$0 < Q < P+Q$), and by (ii) an alphabet of width exactly $Q$ carries no moving
cycle of *any* length. The source's claimed sharpness example at $W = Q$ is
therefore impossible in the stated setting; it is correct only in the
degenerate case $P = 0$ (blocks $Qx' = C_i$, excluded here), where
$\{0, Q\}$ does carry the 2-cycle $0 \leftrightarrow 1$ and the threshold
degenerates to $W < Q = P + Q$ — consistent with, and explaining, the
source's intuition.

### L-9923.2 (cycle-minimum finite target sieve)

Same setting; write the constants as $E_1, \dots, E_s \in \mathbb{Z}$ (no sign
or size hypotheses on the $E_i$), $D = Q - P \ge 1$, and let
$E_{\max} := \max_i E_i$.

**(2a) (minimum-edge law and finite target).** Suppose a **positive** integral
cycle of some length $R \ge 1$ exists on some word. Let $m := \min_t x_t \ge 1$.
Then for **every** position $t$ with $x_t = m$, the successor satisfies
$x_{t+1} = m + k_t$ with an integer $k_t \ge 0$, and the block constant used
there is exactly
$$E_{i_t} \;=\; D\,m + Q\,k_t .$$
Consequently:
1. $E_{i_t} \ge D \ge 1$ — the alphabet **must contain a constant $\ge D$**
   (this positivity is *derived*, not assumed);
2. $E_{i_t}$ lies in the **finite target set**
   $$T(E_{\max}) \;:=\; \{\, D\mu + Q\kappa \;:\; \mu, \kappa \in \mathbb{Z},\
   \mu \ge 1,\ \kappa \ge 0,\ D\mu + Q\kappa \le E_{\max} \,\}
   \;\subseteq\; [\,D,\ E_{\max}\,],$$
   which has at most $\max(0,\, E_{\max} - D + 1)$ elements and is **empty**
   iff $E_{\max} < D$.

*Corollary.* If no alphabet constant lies in $T(E_{\max})$ — in particular if
$E_{\max} < D$, e.g. if all $E_i \le 0$ — then no positive integral cycle
exists on any word of any length.

Hypothesis usage, exactly: positivity of states enters only as $m \ge 1$
(integer states + positivity give the floor $1$); minimality of $m$ enters
only as $k_t \ge 0$; integrality of states enters as $k_t \in \mathbb{Z}$
(needed for (2b)) and via $m \in \mathbb{Z}$. **No constraint on the signs of
the $E_i$ is needed or implicitly used**: for every $m \ge 1$, $k \ge 1$ the
alphabet $\{Dm + Qk,\ Dm - Pk\}$ — whose second constant is negative whenever
$Pk > Dm$ — carries the positive 2-cycle $(m, m+k)$, and the law above holds
on it (Proof, Step 5; Test 4).

**(2b) (divisibility refinement).** Let additionally $g \ge 1$ be an integer
with
$$g \mid P, \qquad \gcd(g, Q) = 1, \qquad g \mid E_i \ \text{ for all } i.$$
Then every minimum-edge datum $(m, k_t)$ of every positive integral cycle
satisfies
$$m + k_t \equiv 0 \pmod g, \qquad\text{hence}\qquad m + k_t \ge g,
\qquad\text{and}\qquad
E_{i_t} \;=\; D\,(m + k_t) + P\,k_t \;\ge\; g\,D .$$

**(2c) (height gate and survivor list).**
1. **(Gate.)** Under the hypotheses of (2b): if $E_{\max} < g\,D$, then no
   positive integral cycle exists on any word of any length.
2. **(Gate sharpness.)** The gate cannot be widened: for every such $g, P, Q$
   the one-letter alphabet $\{gD\}$ (which satisfies all hypotheses of (2b))
   has the positive fixed point $x = g$, i.e. $E_{\max} = gD$ does admit a
   positive cycle.
3. **(Survivors.)** If the gate narrowly fails ($E_{\max} \ge gD$), then some
   alphabet constant must equal one of the **finitely many** values in
   $$T_g(E_{\max}) \;:=\; \{\, D\mu + Q\kappa \;:\; \mu \ge 1,\ \kappa \ge 0,\
   g \mid (\mu + \kappa),\ D\mu + Q\kappa \le E_{\max} \,\}
   \;\subseteq\; g\mathbb{Z} \cap [\,gD,\ E_{\max}\,] .$$
   Verifying that no $E_i$ equals any element of $T_g(E_{\max})$ — finitely
   many equality checks, each typically dischargeable by a single
   alphabet-wide congruence that all $E_i$ satisfy and the survivor violates —
   excludes every positive cycle on every word of every length.

### L-9923.3 (relation to the packet)

**(i) (constant-word Syracuse rigidity re-derived; cf. L-9912.1, context
only).** For $a \ge 1$, an $S$-cycle (D-9904/D-9908) whose exponent word is
constant, $a_1 = \dots = a_m = a$, is in particular a positive integral cycle
of the one-letter affine alphabet $(P, Q, C_1) = (3,\, 2^a,\, 1)$. For
$a \ge 2$ this alphabet is subcritical ($2^a > 3$) with $W = 0$, and
L-9923.1(a) alone forces $(2^a - 3)\,x_t = 1$ for every $t$; integrality
forces $2^a - 3 = 1$, i.e. $a = 2$ and $x_t = 1$ — the trivial cycle. For
$a = 1$ the alphabet is supercritical ($P = 3 > 2 = Q$) with positive
constant, so L-9923.3(ii) below excludes every positive cycle. Hence **no
nontrivial $S$-cycle has a constant exponent word** — exactly the rigidity
statement L-9912.1 (PROVED there by computing the same rational value
$x = 1/(2^a-3)$; re-derived here independently, cited for consistency only).

**(ii) (supercritical sign obstruction; the mechanism that kills cycles in
the six-branch chart, cf. L-9916.2 and L-9918.5, context only).**
**Lemma.** Let $P > Q \ge 1$ be integers and let $C_1, \dots, C_s \in
\mathbb{Z}$ with $C_i \ge 0$ for all $i$ (the spec's $C_i > 0$ is not needed).
Then no integral cycle of any length on any word has $x_0 \ge 1$;
consequently (rotation) no integral cycle contains any positive state, and in
particular no positive integral cycle exists. *Two-line proof:* the cycle
equation of Step 1 (valid for all $P, Q$) gives $(Q^R - P^R)\,x_0 = c_w =
\sum_t P^{R-1-t}Q^t\,C_{i_t} \ge 0$; but $P > Q \ge 1$ makes
$Q^R - P^R \le -1$, so $x_0 \ge 1$ would force the left side $\le -1 < 0$,
a contradiction. $\square$ — The sign of $Q^R - P^R$ has flipped relative to
L-9923.1(a), where it equals $D\,G_R \ge 1$. In the six-branch chart
($P = 3^{12} > Q = 2^{19}$, all six digit constants positive; L-9916) this is
precisely why no seed word is periodic: any chart cycle on positive integers
would be a positive integral cycle of that alphabet. Consistent with
L-9916.2(3) (orbits in $\bigcap_N S_N$ diverge) and with the general sign
criterion L-9918.5; both cited as context, neither used.

---

## Definitions

All conventions are from `NOTATION.md` ($\mathbb{Z}^+ = \{1,2,\dots\}$; empty
sums are $0$, empty products are $1$; computational checks are finite
verification, never proof). The following are fixed for this file.

- **Block relation.** Block $i$ relates $x$ to $x'$ by $Qx' = Px + C_i$. Over
  the integers this is a partial map ($x'$ exists iff $Q \mid Px + C_i$) and,
  where defined, $x' = (Px + C_i)/Q$ is unique because $Q \ge 1$. Nothing
  below assumes a block is defined anywhere; integral cycles are *given* as
  hypotheses.
- **Integral cycle, index conventions.** As in the Statement. Indices of a
  length-$R$ cycle are extended $R$-periodically: $x_{j+R} := x_j$ and
  $i_{j+R} := i_j$ for all $j \ge 0$; the defining relation then holds for
  every $j \ge 0$ (for $0 \le j \le R-1$ by definition, and its
  $R$-translates repeat it verbatim). "Positive" means all states in
  $\mathbb{Z}^+$; no evolution or reachability is assumed beyond the $R$
  displayed relations.
- **Rotation (anchoring).** For $0 \le r \le R-1$, the $r$-rotation of the
  cycle is $y_j := x_{r+j}$, $j = 0, \dots, R$, on the word
  $w^{(r)} := (i_r, i_{r+1}, \dots, i_{r+R-1})$ (periodic indices). Lemma C
  below proves it is again an integral cycle of length $R$, with $y_0 = x_r$,
  the same state multiset, and the same multiset of used constants.
- **Subcritical / supercritical.** The alphabet (chart) is *subcritical* when
  $Q > P$ (drift $D = Q - P \ge 1$; the affine maps contract toward
  $C_i/D$) and *supercritical* when $P > Q$. L-9923.1/.1C/.1S/.2 live in the
  subcritical case; L-9923.3(ii) in the supercritical case.
- **Width** $W = C_+ - C_-$; **used constants** of a word $w$: the multiset
  $\{C_{i_t}\}_{t=0}^{R-1}$; $C_-^w \le C_+^w$ its min and max.
- **Target sets** $T(B)$, $T_g(B)$ as displayed in L-9923.2. Note
  $T_g(B) \subseteq T(B)$ and both are finite for every real bound $B$.
- **Fixed point.** A length-1 integral cycle: $Qx = Px + C_i$, i.e.
  $Dx = C_i$; it exists iff $D \mid C_i$, with $x = C_i/D$.

Relation to the packet's objects (context, not dependency): the six-branch
chart of L-9916 is the supercritical alphabet $P = 3^{12}$, $Q = 2^{19}$,
$C_i$ ranging over its six digits; the "affine architectures" of L-9918 have
the same block shape with $M$-power moduli; and the constant-exponent
Syracuse relation $2^a x' = 3x + 1$ is the one-letter alphabet
$(P, Q, C) = (3, 2^a, 1)$.

---

## Motivation

Cylinder-chart programs in this repository (issue #58; L-9916, L-9918) build
exactly this object: a fixed pair $(P, Q)$ and a finite list of admissible
integer "digits" $C_i$, with legality $Qx_{t+1} = Px_t + C_{i_t}$. For
divergence hunting those charts are supercritical, and L-9923.3(ii) is the
two-line reason their orbits can never close up on positive integers. But any
*cycle*-hunting chart must be subcritical, and there this file gives two
extremely cheap necessary conditions:

- **L-9923.1/.1S:** if the digit alphabet is narrower than $P + Q$, the chart
  has *no* moving cycles at all — the only closed orbits are the forced fixed
  points $C_i/D$. A candidate "nontrivial cycle synthesized from blocks" can
  be discarded by one subtraction ($W < P+Q$?) before any search. The sharp
  threshold tells the constructive side of the project exactly how wide an
  alphabet must be before nontrivial closure is even conceivable.
- **L-9923.2:** in the interesting wide-alphabet regime, a positive cycle
  still forces an exact Diophantine event at its minimum: some alphabet
  constant equals $Dm + Qk$. Scanning the finite target set $T(E_{\max})$ —
  and, with the common-divisor refinement, the much thinner $T_g(E_{\max})$,
  empty below the height $gD$ — eliminates whole alphabets on all words of
  all lengths at once, or else pins the finitely many $(m, k)$ data any cycle
  must realize (a synthesis hint, not only an obstruction: Test 4's
  constructor realizes each admissible datum).

Mechanically, L-9923.1(a) is the convex-combination generalization of the
mechanism of L-9905.1 (cycle equation; PROVED): there the multiplier $2^{a_i}$
varies while the additive constant is fixed; here the modulus $Q$ is fixed
while the constant varies. The two families intersect exactly in the
constant-exponent case, which is why L-9923.3(i) recovers L-9912.1's rigidity.
Neither result is used; the overlap is recorded in the Dependency audit.

---

## Proof

### Step 0: three lemmas (all P, Q; no order hypothesis yet)

**Lemma A (iterate identity).** Let $P, Q$ be any integers, and let integers
$x_0, \dots, x_j$ and constants $C_{i_0}, \dots, C_{i_{j-1}}$ satisfy
$Q x_{t+1} = P x_t + C_{i_t}$ for $0 \le t \le j-1$. Then
$$Q^{\,j} x_j \;=\; P^{\,j} x_0 \;+\; \sum_{t=0}^{j-1} P^{\,j-1-t} Q^{\,t}\, C_{i_t}. \tag{A}$$

*Proof.* Induction on $j$. Base $j = 0$: $x_0 = x_0$ (empty sum). Step:
assume (A) for $j$. Multiply the relation $Q x_{j+1} = P x_j + C_{i_j}$ by
$Q^{\,j}$:
$$Q^{\,j+1} x_{j+1} = P \,\big(Q^{\,j} x_j\big) + Q^{\,j} C_{i_j}
= P^{\,j+1} x_0 + \sum_{t=0}^{j-1} P^{\,j-t} Q^{\,t} C_{i_t} + P^{0} Q^{\,j} C_{i_j}
= P^{\,j+1} x_0 + \sum_{t=0}^{j} P^{\,j-t} Q^{\,t} C_{i_t},$$
which is (A) for $j+1$ (the appended term is the $t = j$ summand). $\square$

**Lemma B (telescoped geometric sum).** For all integers $P, Q$ and all
$R \ge 1$, with $G_R = \sum_{t=0}^{R-1} P^{R-1-t} Q^{t}$:
$$(Q - P)\, G_R \;=\; Q^R - P^R . \tag{B}$$
If moreover $P \ge 1$ and $Q \ge 1$, then every summand of $G_R$ is a
positive integer, so $G_R \ge R \ge 1$.

*Proof.* $(Q-P) G_R = \sum_{t=0}^{R-1} P^{R-1-t} Q^{t+1} - \sum_{t=0}^{R-1}
P^{R-t} Q^{t}$; substituting $u = t+1$ in the first sum leaves exactly the
$u = R$ term of the first minus the $t = 0$ term of the second:
$Q^R - P^R$. The positivity claim is immediate from $P^{R-1-t} \ge 1$,
$Q^t \ge 1$. $\square$

**Lemma C (rotation legitimacy).** Let $x_0, \dots, x_R = x_0$ be an integral
cycle on $w = (i_0, \dots, i_{R-1})$ and fix $0 \le r \le R-1$. With periodic
indices (Definitions), set $y_j := x_{r+j}$ for $0 \le j \le R$. Then
$(y_j)$ is an integral cycle of length $R$ on
$w^{(r)} = (i_r, \dots, i_{r+R-1})$, with $y_0 = x_r$ and $y_R = y_0$, whose
multiset of states and multiset of used constants equal those of the original
cycle.

*Proof.* Each required relation $Q y_{j+1} = P y_j + C_{i_{r+j}}$
($0 \le j \le R-1$) is the relation of the original cycle at index $r + j$,
which holds by the periodic extension (Definitions). Closure:
$y_R = x_{r+R} = x_r = y_0$. The index sets $\{r, \dots, r+R-1\}$ reduce mod
$R$ to $\{0, \dots, R-1\}$ bijectively, so states and used constants are the
same multisets. $\square$

### Step 1: proof of L-9923.1(a)

Now let $Q > P \ge 1$, $D = Q - P \ge 1$, and let an integral cycle of length
$R \ge 1$ on $w$ be given. Lemma A at $j = R$, with $x_R = x_0$, gives the
**cycle equation**
$$\big(Q^R - P^R\big)\, x_0 \;=\; c_w . \tag{1}$$
By Lemma B, $Q^R - P^R = D\,G_R$ with $G_R \ge R \ge 1$; so (1) reads
$$D\, G_R\, x_0 \;=\; c_w . \tag{2}$$
Bounding $c_w$ term by term with $C_-^w \le C_{i_t} \le C_+^w$ (min/max of the
used constants) and $P^{R-1-t}Q^t > 0$:
$$G_R\, C_-^w \;\le\; c_w \;\le\; G_R\, C_+^w ,$$
and dividing (2) and this chain by the positive integer $G_R$:
$$D\,x_0 \;=\; \frac{c_w}{G_R} \;=\; \sum_{t=0}^{R-1} \omega_t\, C_{i_t}
\in \big[C_-^w,\ C_+^w\big] \subseteq [C_-, C_+],
\qquad \omega_t = \frac{P^{R-1-t}Q^t}{G_R} .$$
The weights are positive ($P \ge 1$ is used exactly here) and sum to $1$ by
the definition of $G_R$, which is the displayed convex-combination form.
Strictness: if two distinct values occur among the $C_{i_t}$, then at least
one summand of $c_w$ is strictly below its upper bound and one strictly above
its lower bound, so both inequalities are strict. Since $D x_0 = c_w/G_R$ is
an integer (both $D$ and $x_0$ are), $G_R \mid c_w$. For $R = 1$ the
statement degenerates correctly: $G_1 = 1$, $D x_0 = C_{i_0}$. $\blacksquare$

### Step 2: proof of L-9923.1(b)

Subtract $Q x_t$ from both sides of the defining relation:
$$Q\,(x_{t+1} - x_t) \;=\; P x_t + C_{i_t} - Q x_t \;=\; C_{i_t} - D\,x_t . \tag{3}$$
Fix $t$. By Lemma C, the $t$-rotation is an integral cycle of the same length
with start $y_0 = x_t$; Step 1 applied to it yields $D x_t \in [C_-, C_+]$.
(This holds for every $t$.) Then, since also $C_{i_t} \in [C_-, C_+]$,
$$Q\,(x_{t+1} - x_t) \;=\; C_{i_t} - D x_t \;\in\; [\,C_- - C_+,\ C_+ - C_-\,]
= [-W, W],$$
i.e. $|Q(x_{t+1} - x_t)| \le W$ at every edge. $\blacksquare$

### Step 3: proof of L-9923.1(c) and of Corollary L-9923.1C

**(c).** Let $W < Q$. For each edge, Step 2 gives
$|x_{t+1} - x_t| \le W/Q < 1$; since $x_{t+1} - x_t$ is an **integer**
(integrality of states is used exactly here), $x_{t+1} = x_t$. By induction
along $t = 0, \dots, R-1$, all states equal $x_0$. The edge identity (3) then
reads $0 = C_{i_t} - D x_0$, i.e. $C_{i_t} = D x_0$ for every $t$; in
particular $D \mid C_{i_t}$ with quotient $x_0$, and every index used in $w$
carries the same constant value $D x_0$. $\blacksquare$

**(1C).** Assume $W < P + Q$. By L-9923.1S(ii) — proved in Step 4 below,
independently of this corollary — every integral cycle is constant, and by
the computation just made, a constant cycle at value $x$ on word $w$ exists
iff $C_{i_t} = Dx$ for all $t$, which for a given $x$ is possible iff some
$i$ has $C_i = Dx$ (then any word over $\{i : C_i = Dx\}$ of any length
works, and conversely). So the integral cycles with states in $X$ are exactly
the constant cycles at values $x = C_i/D \in X$ with $D \mid C_i$; if no such
$i$ exists there are none at all. The final sentence (no moving cycles
regardless of $X$) is L-9923.1S(ii). Nowhere in Steps 0–4 is any divisor
condition between $P$ and $Q$, any factorization of $D$, or any sign of the
states invoked. $\blacksquare$

### Step 4: proof of L-9923.1S

**(iv) first (it is one subtraction).** For a 2-cycle, $Q x_1 = P x_0 +
C_{i_0}$ and $Q x_0 = P x_1 + C_{i_1}$; subtracting,
$Q(x_1 - x_0) = -P(x_1 - x_0) + C_{i_0} - C_{i_1}$, i.e.
$$(P+Q)(x_1 - x_0) = C_{i_0} - C_{i_1}. \tag{4}$$
If $x_1 \ne x_0$ then $|x_1 - x_0| \ge 1$, so $(P+Q) \mid (C_{i_0}-C_{i_1})$
and $|C_{i_0} - C_{i_1}| \ge P+Q$; hence $W \ge P + Q$. Two constants with
$|C_{i_0}-C_{i_1}| = Q$ cannot occur in (4) with $x_1 \neq x_0$, because
$0 < Q < P + Q$ when $P \ge 1$. $\square$

**(i) (span bound).** Let the cycle be moving: $M > m$. The set
$J := \{t \bmod R : x_t = M\}$ is a nonempty proper subset of
$\mathbb{Z}/R\mathbb{Z}$ (nonempty since $M$ is attained; proper since some
state is $m < M$). Hence there is an index $u$ with $x_u \ne M$ and
$x_{u+1} = M$: take any $t^\ast \in J$ and walk backwards
$t^\ast, t^\ast - 1, \dots$ (periodic indices) to the first index $u$ with
$x_u \notin \{M\}$ — it exists within $R$ steps because $J$ is proper — and
then $x_{u+1} = M$ by the choice of "first". Since $M$ is the maximum,
$x_u \le M - 1$. The defining relation at $u$ gives
$$C_{i_u} \;=\; Q x_{u+1} - P x_u \;=\; Q M - P x_u \;\ge\; QM - P(M-1)
\;=\; D M + P ,$$
using $P \ge 1$ (so that decreasing $x_u$ only increases the value) and
$x_u \le M - 1$. Hence $C_+ \ge DM + P$. Symmetrically, there is an index
$u'$ with $x_{u'} \ne m$, $x_{u'+1} = m$, and $x_{u'} \ge m + 1$; then
$$C_{i_{u'}} \;=\; Q m - P x_{u'} \;\le\; Qm - P(m+1) \;=\; D m - P ,$$
so $C_- \le Dm - P$. Subtracting,
$$W \;=\; C_+ - C_- \;\ge\; (DM + P) - (Dm - P) \;=\; D(M - m) + 2P
\;\ge\; D + 2P \;=\; (Q - P) + 2P \;=\; P + Q ,$$
using $M - m \ge 1$ and $D \ge 1$. Rearranged, $M - m \le (W - 2P)/D$.
$\square$

**(ii).** Contrapositive of (i): if $W \le P + Q - 1$ then no moving cycle
exists, so every integral cycle is constant; the constant-cycle computation
of Step 3 (which used only the edge identity at equal states, not $W < Q$)
gives $C_{i_t} = D x_0$ and $D \mid C_{i_t}$ verbatim. Since $P \ge 1$,
$P + Q - 1 \ge Q$, so the hypothesis range strictly contains $W < Q$; the
regime $Q \le W \le P+Q-1$ is genuinely new relative to (c). $\square$

**(iii).** Check the displayed 2-cycle directly: with $C_1 = Q$, $C_2 = -P$:
block $C_1$ at $x_0 = 0$: $Q \cdot 1 = P \cdot 0 + Q$ ✓, so $x_1 = 1$; block
$C_2$ at $x_1 = 1$: $Q \cdot 0 = P \cdot 1 + (-P)$ ✓, so $x_2 = 0 = x_0$.
Both states are integers, $x_1 \ne x_0$, and $W = Q - (-P) = P + Q$. By (4),
$W = P+Q$ is the least width any genuine 2-cycle permits, and by (ii) no
smaller width permits a moving cycle of any length; so the threshold
$W < P + Q$ in (ii)/(1C) cannot be weakened to $W < P + Q + 1$ (i.e.
$W \le P+Q$). Equality analysis of (i): $W = P + Q$ forces $M - m = 1$ — the
example attains this. $\blacksquare$

*Remark (degenerate $P = 0$).* If $P = 0$ were allowed, (A) still holds, the
weights $\omega_t$ vanish for $t < R-1$ (so (a) degenerates to
$D x_0 = C_{i_{R-1}}$, still in $[C_-, C_+]$), but the span bound's edge
estimates lose the $+P$ terms and give only $W \ge D(M-m) = Q(M-m)$; the
alphabet $\{0, Q\}$ then realizes a 2-cycle $0 \leftrightarrow 1$ at
$W = Q = P + Q$. So the sharp threshold is $W < P + Q$ in *both* cases; the
source's " $W = Q$ example" is the $P = 0$ shadow of the correct
$W = P + Q$ example. All claims of this file keep the standing hypothesis
$P \ge 1$.

### Step 5: proof of L-9923.2a

Let a positive integral cycle of length $R \ge 1$ be given; all $x_t \ge 1$
are integers, so $m = \min_t x_t \ge 1$ ($m \in \mathbb{Z}$: positivity and
integrality are used exactly here). Fix any $t$ with $x_t = m$ (at least one
exists). Its successor $x_{t+1}$ is a state of the cycle, so
$x_{t+1} \ge m$ by minimality (used exactly here); write
$x_{t+1} = m + k_t$ with $k_t := x_{t+1} - m \in \mathbb{Z}_{\ge 0}$. The
defining relation at $t$ gives
$$E_{i_t} \;=\; Q x_{t+1} - P x_t \;=\; Q(m + k_t) - P m \;=\; (Q-P)m + Qk_t
\;=\; D\,m + Q\,k_t . \tag{5}$$
(For $R = 1$ this is the fixed-point case $k_t = 0$, $E_{i_t} = Dm$.)
Consequences: $E_{i_t} = Dm + Qk_t \ge D \cdot 1 + Q \cdot 0 = D \ge 1$,
proving 1; and $E_{i_t} \le E_{\max}$ because $E_{i_t}$ is an alphabet
constant, so $E_{i_t} \in T(E_{\max})$ by (5) with $(\mu, \kappa) =
(m, k_t)$, proving 2. Finiteness of $T(B)$: its elements lie in
$[D, B] \cap \mathbb{Z}$ (each is $\ge D\mu \ge D$), so
$|T(B)| \le \max(0, B - D + 1)$, with $T(B) = \emptyset$ iff no value fits,
i.e. iff $B < D$ (and conversely $D = D\cdot 1 + Q \cdot 0 \in T(B)$ when
$B \ge D$). The Corollary is the contrapositive of 2 (and of 1 for the
$E_{\max} < D$ clause: if all $E_i \le 0 < D$ then certainly
$E_{\max} < D$).

*No sign hypothesis on the $E_i$:* the argument above never uses one. That
none is secretly needed is witnessed by an explicit family: for any
$m \ge 1$, $k \ge 1$, the alphabet $\{E_1, E_2\} = \{Dm + Qk,\ Dm - Pk\}$
carries the positive 2-cycle $(x_0, x_1) = (m, m+k)$ — check:
$Q(m+k) = Pm + (Dm + Qk)$ ✓ and $Qm = P(m+k) + (Dm - Pk)$ ✓ — and
$E_2 = Dm - Pk < 0$ whenever $Pk > Dm$. The law (5) holds at the unique
minimal state $m$ with constant $E_1 = Dm + Qk$, exactly as the theorem
says; the negative constant $E_2$ is used on the down-edge, where no claim is
made. (This family also realizes *every* admissible datum $(m, k)$ with
$k \ge 1$, and $k = 0$ is realized by the fixed point $\{Dm\}$ — the sieve's
necessary condition is thus optimal as a condition on single constants:
every element of $T(\cdot)$ actually occurs as a minimum-edge constant of
some positive cycle.) $\blacksquare$

### Step 6: proof of L-9923.2b and L-9923.2c

**(2b).** Work modulo $g$. From $g \mid P$: $D = Q - P \equiv Q \pmod g$.
From $g \mid E_{i_t}$ and (5):
$$0 \;\equiv\; E_{i_t} \;=\; Dm + Qk_t \;\equiv\; Q\,(m + k_t) \pmod g .$$
Since $\gcd(g, Q) = 1$, $Q$ is invertible mod $g$ (used exactly here), so
$m + k_t \equiv 0 \pmod g$. Now $m + k_t \ge m \ge 1$ ($k_t \ge 0$ from
minimality, $m \ge 1$ from positivity), and a positive integer divisible by
$g$ is at least $g$: $m + k_t \ge g$. Finally, using $Q = D + P$,
$$E_{i_t} \;=\; Dm + Qk_t \;=\; Dm + (D+P)k_t \;=\; D\,(m + k_t) + P\,k_t
\;\ge\; D\,g + P \cdot 0 \;=\; g\,D ,$$
where $P k_t \ge 0$ needs $k_t \ge 0$ (minimality again) and $P \ge 1 > 0$.
$\blacksquare$

**(2c).1 (Gate).** If a positive cycle existed, (2b) would give an alphabet
constant $E_{i_t} \ge gD$, contradicting $E_{\max} < gD$. $\square$

**(2c).2 (Gate sharpness).** The alphabet $\{gD\}$ satisfies the hypotheses
of (2b): $g \mid gD$ (and $g \mid P$, $\gcd(g,Q) = 1$ are hypotheses on
$g, P, Q$ alone). The fixed point $x = g$: $Q g = P g + D g$ ✓, a positive
integral cycle with $E_{\max} = gD$. So the strict inequality in the gate is
exactly right. $\square$

**(2c).3 (Survivors).** By (5) and (2b), the minimum-edge constant is a value
$D\mu + Q\kappa$ with $\mu \ge 1$, $\kappa \ge 0$, $g \mid (\mu+\kappa)$, and
it is $\le E_{\max}$; that is membership in $T_g(E_{\max})$. Each element of
$T_g$ is $\equiv Q(\mu + \kappa) \equiv 0 \pmod g$ and $\ge gD$ (by the
computation in (2b)), giving the displayed inclusion
$T_g(E_{\max}) \subseteq g\mathbb{Z} \cap [gD, E_{\max}]$; finiteness as in
Step 5. If no $E_i$ equals any element of $T_g(E_{\max})$, no positive cycle
can supply the required minimum-edge constant, so none exists. The
"single alphabet-wide congruence" remark is a usage note, not a theorem: in
practice each survivor $\tau$ is discharged by exhibiting any congruence all
$E_i$ satisfy and $\tau$ violates (e.g. all $E_i \equiv 0 \bmod g^2$ while
$g^2 \nmid \tau$), or by the $s$ direct comparisons $E_i \ne \tau$. A worked
instance is in the Adversarial tests (Test 5iv): $P = 3$, $Q = 5$, $g = 3$,
$D = 2$, $E_{\max} = 21$: $T_g(21) = \{6, 9, 12, 15, 18, 21\}$, and the
alphabet $\{21, -3\}$ realizes the survivor $21 = D\cdot3 + Q\cdot3$ on the
2-cycle $(3, 6)$ — the gate $E_{\max} < 6$ fails and must fail, since a
cycle exists. $\blacksquare$

### Step 7: proof of L-9923.3(i)

Let an $S$-cycle (D-9908: positive odd $x_1 \to \dots \to x_m \to x_1$,
exponents $a_i = \nu_2(3x_i + 1)$) have constant exponent word,
$a_i = a$ for all $i$. Each step then satisfies $2^a x_{i+1} = 3 x_i + 1$
(D-9904's step relation with exponent $a$), so the states form a positive
integral cycle of length $R = m$ on the one-letter alphabet
$(P, Q, C_1) = (3, 2^a, 1)$, word $(1, 1, \dots, 1)$. (Only this forgetful
direction is used; oddness and exactness of the exponent are simply
discarded.)

*Case $a \ge 2$:* $Q = 2^a \ge 4 > 3 = P$, so the alphabet is subcritical
with $D = 2^a - 3 \ge 1$ and $W = 0$. Step 1 (L-9923.1(a)) plus Lemma C give,
for every $t$, $D x_t = C_1 = 1$ (a convex combination of the single value
$1$). So $x_t = 1/(2^a - 3)$, and integrality of $x_t$ forces
$2^a - 3 = 1$: $a = 2$ and $x_t = 1$ for all $t$. This is the trivial cycle
(D-9905): indeed $S(1) = (3+1)/4 = 1$ with $\nu_2(4) = 2 = a$. (Collapse was
free here: $W = 0 < Q$; but (a) alone already pinned every state.)

*Case $a = 1$:* $P = 3 > 2 = Q$ and $C_1 = 1 \ge 0$; L-9923.3(ii) (Step 8,
whose proof does not use this step) says no integral cycle of this alphabet
has a positive state. So no $S$-cycle has constant exponent word $a = 1$.

Combining: the only $S$-cycle with constant exponent word is the trivial
cycle ($a = 2$, all states $1$). This is precisely L-9912.1, whose own proof
computes the same value $x = 1/(2^a - 3)$; agreement is recorded as
consistency, and nothing from L-9912 is used. $\blacksquare$

### Step 8: proof of L-9923.3(ii)

Let $P > Q \ge 1$, all $C_i \ge 0$, and suppose an integral cycle of length
$R \ge 1$ on some word has $x_0 \ge 1$. Lemma A at $j = R$ with $x_R = x_0$
gives $(Q^R - P^R)\,x_0 = c_w$ (Lemmas A and B never used $Q > P$). Every
summand of $c_w = \sum_t P^{R-1-t} Q^t C_{i_t}$ is $\ge 0$ (here $C_i \ge 0$,
$P, Q \ge 1$), so $c_w \ge 0$. But $P > Q \ge 1$ gives $P^R > Q^R$, i.e.
$Q^R - P^R \le -1$, so $(Q^R - P^R) x_0 \le -x_0 \le -1 < 0 \le c_w$ —
a contradiction. Hence no integral cycle has $x_0 \ge 1$; by Lemma C
(rotation moves any state into the anchor position), no integral cycle
contains any positive state, and a fortiori no positive integral cycle
exists, on any word of any length. (The spec's hypothesis $C_i > 0$ is
weakened to $C_i \ge 0$; strict positivity is not needed because the
contradiction $-1 < 0$ already has slack.) $\blacksquare$

---

## Dependency audit

| Dependency | Where used |
|---|---|
| NOTATION.md conventions ($\mathbb{Z}^+$; empty sum $= 0$; finite verification labeling; status semantics) | Base case of Lemma A; positivity floor $m \ge 1$ in Step 5; Adversarial tests labeling; header. |
| D-9904 (Syracuse map, step relation $2^{a}S(x) = 3x+1$), D-9908 ($S$-cycle notation), D-9905 (trivial cycle) | Step 7 only, and only to *name* the Syracuse objects; the constant-word step relation is re-displayed there. |
| Lemma A, Lemma B, Lemma C | Proved inline in Step 0 from ring arithmetic; used in Steps 1, 2, 4–8. |

Cited as **context only, never used**: L-9905 (cycle equation; the mechanism
generalized here), L-9912.1 (constant-exponent rigidity; re-derived
independently in Step 7 and cross-checked), L-9916 (six-branch chart; its
parameters appear only inside Test 6iii as data), L-9918.5 (sign criterion;
Step 8 is its self-contained specialization to fixed-modulus alphabets).
No statement of this file depends on any other claim file; no circularity is
possible. Nothing assumes the Collatz conjecture or its negation.

Overlap note (per NOTATION.md's convention on overlapping derivations):
Step 7 re-proves a special case of L-9912.1 (PROVED) rather than citing it,
to keep this file's dependency set equal to NOTATION.md alone; Step 8
re-proves, for constant-modulus alphabets, the periodic-address half of
L-9918.5 (PROVED). Both overlaps are deliberate and recorded here.

## Gap audit

Deliberate search against the README §8 checklist:

- **Hidden finiteness assumptions:** none. All claims quantify over all words
  of all lengths $R \ge 1$ and all integral cycles; each proof manipulates
  one arbitrary fixed cycle. $T(B)$, $T_g(B)$ are proved finite, not assumed.
- **Unjustified induction:** the only inductions are Lemma A (explicit base
  and step) and the trivial propagation "all $\Delta_t = 0 \Rightarrow$ all
  states equal" in Step 3.
- **Boundary cases:** $R = 1$ checked in Steps 1 ($G_1 = 1$), 5 ($k = 0$,
  fixed point); $s = 1$ (then $W = 0 < Q$: vacuously narrow, collapse applies);
  $k_t = 0$ and multiple minima handled in Step 5 ("for every position with
  $x_t = m$"); $g = 1$ in (2b) degenerates to the base floor $E \ge D$
  (statement remains true; the refinement adds nothing, as expected);
  $M - m = 1$ equality case of the span bound attained by the sharpness
  example; empty $T(E_{\max})$ iff $E_{\max} < D$ proved both ways.
- **Quantifier order:** in .2a the datum $(m, k_t)$ depends on the cycle and
  the chosen minimal position; the theorem asserts the law at *every* minimal
  position, and membership of the resulting constant in the *fixed* finite
  set $T(E_{\max})$ — no hidden dependence of the target set on the cycle.
- **Empirical vs. universal confusion:** the Adversarial tests are labeled
  finite verification and are cited by no proof step.
- **Limit interchanges / analysis:** none occur; everything is finite integer
  arithmetic (the only divisions are by $G_R \ge 1$, $Q \ge 1$, and the
  inversion of $Q$ mod $g$, each justified where used).
- **Circular dependence:** Step 3's corollary (1C) cites Step 4's (ii); Step
  4 does not use (1C). Step 7 cites Step 8; Step 8 uses only Lemmas A–C.
  No cycle.
- **Sign errors under the flipped regime:** Step 8's inequality chain was
  checked at the boundary $Q = 1$, $R = 1$ ($Q^R - P^R = 1 - P \le -1$
  needs $P \ge 2 = Q + 1$ ✓ since $P > Q$).
- **Assumptions equivalent to Collatz:** none; all statements are
  unconditional theorems about hypothetical cycles of abstract alphabets.
- **Least-period subtleties:** no statement mentions least periods; Lemma C
  produces length-$R$ cycles from length-$R$ cycles regardless of primitivity.
- **Where each hypothesis bites** (also flagged inline): $P \ge 1$ — weight
  positivity (Step 1), the $+P$/$-P$ edge estimates (Step 4(i)), $Pk_t \ge 0$
  (Step 6); integrality of states — Step 3's $\Delta_t = 0$, Step 5's
  $m \ge 1$ and $k_t \in \mathbb{Z}$; positivity — Step 5's $m \ge 1$ only;
  minimality — Step 5's $k_t \ge 0$ only; $g \mid P$, $\gcd(g,Q) = 1$,
  $g \mid E_i$ — each used at one named line of Step 6.
- **Source-spec deviations:** all corrections are flagged in Provenance and
  proved in Steps 4–6; nothing from the unpushed report is relied on.

No gaps found; all sub-claims are asserted as fully proved above.

## Adversarial tests

**Finite verification, not proof.** Exact integer arithmetic (Python `int`;
`fractions.Fraction` only to *represent* the exact rational root in Test 7).
Deterministic (fixed seed 99230). Script kept at
`scratchpad/l9923_tests.py` (session-local); full code inline below,
byte-identical to the executed file. Run: `python3 l9923_tests.py`
(Python ≥ 3.8, stdlib only; ~3.5 s).

Design notes — each test is aimed at the step it could most plausibly break:

1. **Test 1** attacks Lemmas A and B as identities, on random trajectories
   whose constants are *defined from* freely chosen integer states (so
   arbitrary $P, Q \ge 1$ with no order and no alphabet structure are
   exercised, including $P = Q$ and $P > Q$).
2. **Test 2** attacks the strengthened collapse (Step 4(ii)) on its exact
   boundary: 400 random subcritical alphabets with $W \le P+Q-1$, of which
   164 have $W \ge Q$ — the regime the source hypothesis does not cover.
   The search is **exhaustive and complete** over all words of length
   $\le 6$: `cycle_on_word` computes the unique rational root
   $x_0 = c_w/(Q^R - P^R)$ of each word map (the cycle equation has exactly
   one solution since $Q^R \ne P^R$), so *every* integral cycle of length
   $\le 6$ is found — none is moving, and the found fixed points match
   $\{C_i/D : D \mid C_i\}$ exactly (completeness, not just soundness).
3. **Test 3** does three things per $(P,Q)$ pair: verifies the sharpness
   2-cycle of $\{Q, -P\}$; refutes the source's example shape by exhaustively
   checking all width-$Q$ pairs $\{C, C+Q\}$, $C \in [-30,30]$ (all cycles
   constant); and runs a **threshold scan** — the minimum width of any
   2-constant alphabet (bases in $[-15,15]$, words $\le 5$; 3-constant
   alphabets with arbitrary middle constant scanned at widths $\le 8$,
   words $\le 4$) that admits a moving cycle — expecting exactly $P + Q$.
   All ten pairs — including the non-coprime $(P,Q) = (2,4)$ and $(6,9)$,
   since no coprimality is claimed anywhere — return $P+Q$ on the nose.
4. **Test 4** attacks the sieve law (Step 5): (i) 300 constructed 2-cycles
   $\{Dm+Qk, Dm-Pk\}$ — in 104 of them the down-constant is *negative*,
   witnessing that no sign hypothesis on the alphabet is needed; (ii) 250
   random alphabets (constants in $[-25, 40]$), exhaustive positive-cycle
   search, 1246 positive cycles found (150 moving): the law
   $E = Dm + Qk$, the floor $E \ge D$, and $T(E_{\max})$-membership hold at
   every minimal state of every one.
5. **Test 5** attacks the refinement and the gate (Step 6): (i) 200 random
   $g$-divisible alphabets ($g \mid P$, $\gcd(g,Q)=1$ enforced): $g \mid
   (m+k)$ and $E \ge gD$ at every minimum; (ii) 200 alphabets built to sit
   just *below* the gate ($E_i$ multiples of $g$ up to $g(D-1)$, i.e.
   $E_{\max} \le gD - g$, adversarially close): exhaustively no positive
   cycle; (iii) gate sharpness fixed points $x = g$ at $E = gD$; (iv) the
   worked survivor instance of Step 6 verified in full
   ($T_g(21) = \{6,9,12,15,18,21\}$, realized survivor $21$ on the 2-cycle
   $(3,6)$).
6. **Test 6** attacks the sign obstruction (Step 8): the one-letter
   supercritical alphabet $(P,Q,C) = (3,2,1)$ — the shortcut-map odd-step
   relation — has all its cycles (words $\le 8$) at the famous $x = -1$;
   200 random supercritical alphabets with $C_i \ge 0$ produce 1198 integral
   cycles, none containing a positive state (the sign flip is real: negative
   cycles abound); and the **actual six-branch chart** $P = 3^{12}$,
   $Q = 2^{19}$ with L-9916's alphabet $A$ (values re-derived and checked)
   has $c_w > 0 > Q^R - P^R$ for every word of length $\le 3$ — no positive
   cycle on any of them.
7. **Test 7** verifies Step 7's exact rational root $1/(2^a - 3)$ for
   $a = 2..9$ and all word lengths $\le 6$, with integrality exactly at
   $a = 2$ (all states $1$).
8. **Test 8** stress-tests the *universal* parts (Steps 1–2) where they are
   strongest — on wide alphabets with 706 genuinely moving cycles among 3021:
   $D x_t \in [\min$ used$, \max$ used$]$ at every position, the edge
   identity, $|Q\,\Delta_t| \le W$, and $G_R \mid c_w$.

```python
#!/usr/bin/env python3
"""
Adversarial tests for L-9923 (research/foundations/L-9923-affine-cycle-collapse.md).
FINITE VERIFICATION ONLY -- not a proof.
Agent: fable-02-p17.  Date: 2026-07-26.  Exact integer arithmetic throughout
(Python ints; fractions.Fraction only for the exact rational root in Test 7).
Deterministic: fixed seed, no environment dependence.  Run: python3 l9923_tests.py
"""
from fractions import Fraction
from itertools import product as iproduct
from math import gcd
import random

rng = random.Random(99230)
fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

# ------------------------------------------------------------- machinery
def cw(P, Q, consts):
    """c_w = sum_t P^(R-1-t) Q^t C_{i_t} over the word's constant sequence."""
    R = len(consts)
    return sum(P**(R - 1 - t) * Q**t * consts[t] for t in range(R))

def geom(P, Q, R):
    """G_R = sum_t P^(R-1-t) Q^t."""
    return sum(P**(R - 1 - t) * Q**t for t in range(R))

def cycle_on_word(P, Q, C, word):
    """The unique rational root x_0 = c_w / (Q^R - P^R) of the word map,
    returned as the integral cycle [x_0..x_{R-1}] iff x_0 AND every
    intermediate state is an integer; else None.  Needs Q != P only."""
    R = len(word)
    consts = [C[i] for i in word]
    den = Q**R - P**R
    num = cw(P, Q, consts)
    if num % den != 0:
        return None
    xs = [num // den]
    for t in range(R):
        y = P * xs[-1] + consts[t]
        if y % Q != 0:
            return None
        xs.append(y // Q)
    assert xs[R] == xs[0]          # Lemma A closes the loop exactly
    return xs[:R]

def all_cycles(P, Q, C, Rmax):
    """ALL integral cycles on ALL words of length 1..Rmax (exhaustive)."""
    out = []
    for R in range(1, Rmax + 1):
        for word in iproduct(range(len(C)), repeat=R):
            xs = cycle_on_word(P, Q, C, word)
            if xs is not None:
                out.append((word, xs))
    return out

def target_set(D, Q, B):
    """T(B) = {D*mu + Q*ka : mu >= 1, ka >= 0, value <= B}."""
    T = set()
    mu = 1
    while D * mu <= B:
        ka = 0
        while D * mu + Q * ka <= B:
            T.add(D * mu + Q * ka)
            ka += 1
        mu += 1
    return T

def target_set_g(D, Q, g, B):
    """T_g(B): same with the extra congruence g | (mu + ka)."""
    T = set()
    mu = 1
    while D * mu <= B:
        ka = 0
        while D * mu + Q * ka <= B:
            if (mu + ka) % g == 0:
                T.add(D * mu + Q * ka)
            ka += 1
        mu += 1
    return T

# ------------------------------------------------------------- Test 1
# Lemma A (iterate identity) on random integral trajectories -- constants are
# DEFINED from freely chosen integer states, so ANY P, Q >= 1 (no order, no
# alphabet) is exercised -- and Lemma B (telescoped geometric sum).
n1a = n1b = 0
for trial in range(300):
    P = rng.randint(1, 30); Q = rng.randint(1, 30)
    xs = [rng.randint(-50, 50) for _ in range(9)]
    consts = [Q * xs[t + 1] - P * xs[t] for t in range(8)]
    for j in range(9):
        lhs = Q**j * xs[j]
        rhs = P**j * xs[0] + sum(P**(j - 1 - t) * Q**t * consts[t]
                                 for t in range(j))
        check(f"T1A P={P} Q={Q} j={j}", lhs == rhs)
        n1a += 1
    for R in range(1, 9):
        check(f"T1B P={P} Q={Q} R={R}",
              (Q - P) * geom(P, Q, R) == Q**R - P**R)
        n1b += 1
print(f"Test 1: Lemma A at {n1a} (trajectory, j) instances; "
      f"Lemma B at {n1b} (P,Q,R) triples.")

# ------------------------------------------------------------- Test 2
# L-9923.1(c) + .1S collapse: random subcritical alphabets with width
# W <= P+Q-1 -- including the regime Q <= W (beyond the source spec's W < Q).
# Exhaustive over ALL words of length <= 6: only constant fixed-point cycles
# x = C_i/D occur, and ALL predicted fixed points occur.
n_alpha = n_cyc = n_moving = n_wide = 0
for trial in range(400):
    P = rng.randint(1, 9); Q = rng.randint(P + 1, 12); D = Q - P
    s = rng.randint(1, 4)
    base = rng.randint(-40, 40)
    C = [base] + [base + rng.randint(0, P + Q - 1) for _ in range(s - 1)]
    W = max(C) - min(C)
    if W >= Q:
        n_wide += 1
    predicted = {C[i] // D for i in range(s) if C[i] % D == 0}
    got_states = set()
    for word, xs in all_cycles(P, Q, C, 6):
        n_cyc += 1
        if len(set(xs)) > 1:
            n_moving += 1
            print("MOVING CYCLE (refutes L-9923.1S):", P, Q, C, word, xs)
        check(f"T2 const trial={trial}", len(set(xs)) == 1)
        check(f"T2 divis trial={trial}", all(C[i] == D * xs[0] for i in word))
        got_states.add(xs[0])
    check(f"T2 complete trial={trial}", got_states == predicted)
    n_alpha += 1
check("T2 no moving cycles", n_moving == 0)
print(f"Test 2: {n_alpha} alphabets with W <= P+Q-1 ({n_wide} of them with "
      f"W >= Q); {n_cyc} cycles found, all constant with C_i = D*x; "
      f"fixed-point sets match exactly; moving cycles: {n_moving}.")

# ------------------------------------------------------------- Test 3
# .1S sharpness and the source-spec refutation.
# (i)   {Q, -P} carries the integral 2-cycle 0 <-> 1 (width exactly P+Q).
# (ii)  Width-Q pairs {C, C+Q} (the source's claimed sharpness shape) admit NO
#       non-constant cycle: words <= 6, C in [-30, 30].
# (iii) Threshold scan: minimum width of ANY 2-constant alphabet (base in
#       [-15,15], words <= 5) -- and of 3-constant alphabets (base in [-8,8],
#       middle anywhere in the gap, words <= 4) at widths <= 8 -- admitting a
#       non-constant cycle equals P+Q exactly.
for (P, Q) in [(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (3, 5), (2, 4), (6, 9),
               (5, 8), (7, 12)]:
    check(f"T3i P={P} Q={Q}", cycle_on_word(P, Q, [Q, -P], (0, 1)) == [0, 1])
    n_narrow = 0
    for Cb in range(-30, 31):
        for word, xs in all_cycles(P, Q, [Cb, Cb + Q], 6):
            check(f"T3ii P={P} Q={Q} C={Cb}", len(set(xs)) == 1)
            n_narrow += 1
    minw = None
    for w in range(0, P + Q + 1):
        moving = False
        for b in range(-15, 16):
            if any(len(set(xs)) > 1 for _, xs in all_cycles(P, Q, [b, b + w], 5)):
                moving = True
                break
        if not moving and w <= 8:
            for b in range(-8, 9):
                for mid in range(b, b + w + 1):
                    if any(len(set(xs)) > 1
                           for _, xs in all_cycles(P, Q, [b, mid, b + w], 4)):
                        moving = True
                        break
                if moving:
                    break
        if moving:
            minw = w
            break
    check(f"T3iii P={P} Q={Q}", minw == P + Q)
    print(f"Test 3: (P,Q)=({P},{Q}): {{Q,-P}} 2-cycle OK; width-Q pairs: "
          f"{n_narrow} cycles, all constant; minimal moving width = {minw} "
          f"= P+Q.")

# ------------------------------------------------------------- Test 4
# L-9923.2a minimum-edge law E = D*m + Q*k.
# (i)  Constructed 2-cycles {D*m+Q*k, D*m-P*k} on states {m, m+k}; the down
#      constant is often NEGATIVE (no sign hypothesis on the alphabet).
# (ii) Random alphabets, exhaustive positive cycles: the law holds at EVERY
#      minimal state, with k >= 0 and membership in T(E_max).
n_con = n_negdown = 0
for trial in range(300):
    P = rng.randint(1, 9); Q = rng.randint(P + 1, 12); D = Q - P
    m = rng.randint(1, 30); k = rng.randint(1, 12)
    C = [D * m + Q * k, D * m - P * k]
    if C[1] < 0:
        n_negdown += 1
    check(f"T4i cycle trial={trial}", cycle_on_word(P, Q, C, (0, 1)) == [m, m + k])
    check(f"T4i law trial={trial}", C[0] == D * m + Q * k)
    check(f"T4i target trial={trial}", C[0] in target_set(D, Q, max(C)))
    n_con += 1
print(f"Test 4i: {n_con} constructed 2-cycles (down-constant negative in "
      f"{n_negdown}): min-edge law and target membership hold in all.")
n_alpha4 = n_pos = n_posmov = 0
for trial in range(250):
    P = rng.randint(1, 6); Q = rng.randint(P + 1, 9); D = Q - P
    s = rng.randint(2, 4)
    C = [rng.randint(-25, 40) for _ in range(s)]
    Emax = max(C)
    T = target_set(D, Q, Emax)
    for word, xs in all_cycles(P, Q, C, 5):
        if min(xs) < 1:
            continue
        n_pos += 1
        if len(set(xs)) > 1:
            n_posmov += 1
        m = min(xs); R = len(xs)
        for t in range(R):
            if xs[t] == m:
                kt = xs[(t + 1) % R] - m
                check(f"T4ii k>=0 trial={trial}", kt >= 0)
                check(f"T4ii law trial={trial}", C[word[t]] == D * m + Q * kt)
                check(f"T4ii inT trial={trial}", C[word[t]] in T)
                check(f"T4ii floor trial={trial}", C[word[t]] >= D)
    n_alpha4 += 1
print(f"Test 4ii: {n_alpha4} random alphabets; {n_pos} positive cycles found "
      f"({n_posmov} non-constant): law E = D*m + Q*k, floor E >= D, and "
      f"T(E_max) membership verified at every minimal state.")

# ------------------------------------------------------------- Test 5
# L-9923.2b/2c: g | P, gcd(g, Q) = 1, g | E_i for all i.
# (i)   Random such alphabets: every positive cycle has g | (m + k) and
#       min-edge constant >= g*D.
# (ii)  Height gate: E_max < g*D (multiples of g up to g*(D-1)) -> NO
#       positive cycle, exhaustively (words <= 5).
# (iii) Gate sharpness: alphabet {g*D} has the positive fixed point y = g.
# (iv)  Worked narrow-fail instance P=3, Q=5, g=3 from the file text.
n5 = n5cyc = 0
for trial in range(200):
    g = rng.randint(2, 5)
    P = g * rng.randint(1, 4)
    Q = rng.randint(P + 1, P + 9)
    while gcd(g, Q) != 1:
        Q += 1
    D = Q - P
    C = [g * rng.randint(-8, 12) for _ in range(rng.randint(2, 3))]
    for word, xs in all_cycles(P, Q, C, 5):
        if min(xs) < 1:
            continue
        n5cyc += 1
        m = min(xs); R = len(xs)
        for t in range(R):
            if xs[t] == m:
                kt = xs[(t + 1) % R] - m
                check(f"T5i g|(m+k) trial={trial}", (m + kt) % g == 0)
                check(f"T5i floor trial={trial}", C[word[t]] >= g * D)
    n5 += 1
print(f"Test 5i: {n5} g-divisible alphabets, {n5cyc} positive-cycle "
      f"instances: g | (m+k) and min-edge >= g*D everywhere.")
n_gate = 0
for trial in range(200):
    g = rng.randint(2, 5)
    P = g * rng.randint(1, 4)
    Q = rng.randint(P + 1, P + 9)
    while gcd(g, Q) != 1:
        Q += 1
    D = Q - P
    C = [g * rng.randint(-8, D - 1) for _ in range(rng.randint(2, 3))]
    pos = [xs for _, xs in all_cycles(P, Q, C, 5) if min(xs) >= 1]
    check(f"T5ii gate trial={trial}", pos == [])
    n_gate += 1
print(f"Test 5ii: {n_gate} alphabets with E_max <= g*(D-1) < g*D: "
      f"no positive cycle on any word of length <= 5.")
for (g, P, Q) in [(2, 2, 3), (3, 3, 5), (5, 5, 7), (3, 6, 7)]:
    D = Q - P
    check(f"T5iii g={g}", cycle_on_word(P, Q, [g * D], (0,)) == [g])
Tg = sorted(target_set_g(2, 5, 3, 21))
check("T5iv cycle", cycle_on_word(3, 5, [21, -3], (0, 1)) == [3, 6])
check("T5iv survivors", Tg == [6, 9, 12, 15, 18, 21])
check("T5iv gate-min", min(Tg) == 3 * 2)
check("T5iv realized", 21 == 2 * 3 + 5 * 3)   # (m, k) = (3, 3), m + k = 6
print(f"Test 5iii/iv: gate sharpness fixed points OK; worked instance "
      f"P=3,Q=5,g=3: survivors T_g(21) = {Tg}; alphabet {{21,-3}} realizes "
      f"E = 21 = D*3 + Q*3 on the 2-cycle (3, 6).")

# ------------------------------------------------------------- Test 6
# L-9923.3(ii) supercritical sign obstruction (P > Q, all C_i >= 0).
# (i)   P=3, Q=2, alphabet {1}: all integral cycles on words <= 8 sit at -1.
# (ii)  Random supercritical alphabets with C_i >= 0: every integral cycle
#       found has max state <= 0 (no positive state at all).
# (iii) The actual six-branch chart P = 3^12, Q = 2^19, alphabet A of L-9916:
#       every word of length <= 3 has c_w > 0 > Q^R - P^R, so its unique
#       rational root is negative -- no positive cycle on any of them.
states6 = set()
for word, xs in all_cycles(3, 2, [1], 8):
    check("T6i", set(xs) == {-1})
    states6 |= set(xs)
print(f"Test 6i: P=3,Q=2,C={{1}}: cycle states on words <= 8: "
      f"{sorted(states6)}.")
n6 = n6cyc = 0
for trial in range(200):
    Q = rng.randint(1, 9); P = rng.randint(Q + 1, 12)
    C = [rng.randint(0, 30) for _ in range(rng.randint(1, 3))]
    for word, xs in all_cycles(P, Q, C, 5):
        check(f"T6ii trial={trial}", max(xs) <= 0)
        n6cyc += 1
    n6 += 1
print(f"Test 6ii: {n6} supercritical alphabets (C_i >= 0): {n6cyc} integral "
      f"cycles found, none containing a positive state.")
Pb, Qb = 3**12, 2**19
A = [7 * 3**(2 * i) * 2**(15 - 3 * i) for i in range(6)]
check("T6iii alphabet", sorted(A) == [229376, 258048, 290304, 326592, 367416, 413343])
nw = 0
for R in range(1, 4):
    for word in iproduct(range(6), repeat=R):
        num = cw(Pb, Qb, [A[i] for i in word])
        check("T6iii sign", num > 0 and Qb**R - Pb**R < 0)
        nw += 1
print(f"Test 6iii: six-branch chart: all {nw} words of length <= 3 have "
      f"c_w > 0 > Q^R - P^R: no positive cycle exists on any of them.")

# ------------------------------------------------------------- Test 7
# L-9923.3(i) one-letter Syracuse blocks (P,Q,C) = (3, 2^a, 1), a >= 2:
# exact rational root 1/(2^a - 3) for every length; integral iff a = 2 (x=1).
for a in range(2, 10):
    Q = 2**a; D = Q - 3
    for R in range(1, 7):
        check(f"T7 root a={a} R={R}",
              Fraction(cw(3, Q, [1] * R), Q**R - 3**R) == Fraction(1, D))
        xs = cycle_on_word(3, Q, [1], tuple([0] * R))
        check(f"T7 integral a={a} R={R}",
              (xs == [1] * R) if a == 2 else (xs is None))
print("Test 7: one-letter Syracuse blocks a = 2..9, R <= 6: root always "
      "1/(2^a - 3); integral cycle only at a = 2, all states 1 (L-9912.1).")

# ------------------------------------------------------------- Test 8
# Universal parts of L-9923.1 on WIDE alphabets (genuine moving cycles):
# (a) D*x_t inside [min used constant, max used constant] at EVERY t, and
#     G_R | c_w;  (b) edge identity and |Q(x_{t+1} - x_t)| <= W.
n8 = n8mov = 0
for trial in range(300):
    P = rng.randint(1, 6); Q = rng.randint(P + 1, 9); D = Q - P
    C = [rng.randint(-30, 30) for _ in range(rng.randint(2, 4))]
    W = max(C) - min(C)
    for word, xs in all_cycles(P, Q, C, 5):
        n8 += 1
        if len(set(xs)) > 1:
            n8mov += 1
        used = [C[i] for i in word]
        lo, hi = min(used), max(used)
        R = len(xs)
        for t in range(R):
            dq = Q * (xs[(t + 1) % R] - xs[t])
            check(f"T8a trial={trial}", lo <= D * xs[t] <= hi)
            check(f"T8edge trial={trial}", dq == used[t] - D * xs[t])
            check(f"T8b trial={trial}", abs(dq) <= W)
        check(f"T8G trial={trial}", cw(P, Q, used) % geom(P, Q, R) == 0)
print(f"Test 8: {n8} cycle instances on wide alphabets ({n8mov} with >= 2 "
      f"distinct states): D*x_t in used-range, edge identity, |Q dx| <= W, "
      f"and G_R | c_w all hold.")

print("RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-26, CPython 3, Linux; identical across
reruns — fixed seed, no float arithmetic):**

```text
Test 1: Lemma A at 2700 (trajectory, j) instances; Lemma B at 2400 (P,Q,R) triples.
Test 2: 400 alphabets with W <= P+Q-1 (164 of them with W >= Q); 10920 cycles found, all constant with C_i = D*x; fixed-point sets match exactly; moving cycles: 0.
Test 3: (P,Q)=(1,2): {Q,-P} 2-cycle OK; width-Q pairs: 732 cycles, all constant; minimal moving width = 3 = P+Q.
Test 3: (P,Q)=(1,3): {Q,-P} 2-cycle OK; width-Q pairs: 366 cycles, all constant; minimal moving width = 4 = P+Q.
Test 3: (P,Q)=(2,3): {Q,-P} 2-cycle OK; width-Q pairs: 732 cycles, all constant; minimal moving width = 5 = P+Q.
Test 3: (P,Q)=(3,4): {Q,-P} 2-cycle OK; width-Q pairs: 732 cycles, all constant; minimal moving width = 7 = P+Q.
Test 3: (P,Q)=(2,5): {Q,-P} 2-cycle OK; width-Q pairs: 246 cycles, all constant; minimal moving width = 7 = P+Q.
Test 3: (P,Q)=(3,5): {Q,-P} 2-cycle OK; width-Q pairs: 366 cycles, all constant; minimal moving width = 8 = P+Q.
Test 3: (P,Q)=(2,4): {Q,-P} 2-cycle OK; width-Q pairs: 372 cycles, all constant; minimal moving width = 6 = P+Q.
Test 3: (P,Q)=(6,9): {Q,-P} 2-cycle OK; width-Q pairs: 252 cycles, all constant; minimal moving width = 15 = P+Q.
Test 3: (P,Q)=(5,8): {Q,-P} 2-cycle OK; width-Q pairs: 246 cycles, all constant; minimal moving width = 13 = P+Q.
Test 3: (P,Q)=(7,12): {Q,-P} 2-cycle OK; width-Q pairs: 150 cycles, all constant; minimal moving width = 19 = P+Q.
Test 4i: 300 constructed 2-cycles (down-constant negative in 104): min-edge law and target membership hold in all.
Test 4ii: 250 random alphabets; 1246 positive cycles found (150 non-constant): law E = D*m + Q*k, floor E >= D, and T(E_max) membership verified at every minimal state.
Test 5i: 200 g-divisible alphabets, 623 positive-cycle instances: g | (m+k) and min-edge >= g*D everywhere.
Test 5ii: 200 alphabets with E_max <= g*(D-1) < g*D: no positive cycle on any word of length <= 5.
Test 5iii/iv: gate sharpness fixed points OK; worked instance P=3,Q=5,g=3: survivors T_g(21) = [6, 9, 12, 15, 18, 21]; alphabet {21,-3} realizes E = 21 = D*3 + Q*3 on the 2-cycle (3, 6).
Test 6i: P=3,Q=2,C={1}: cycle states on words <= 8: [-1].
Test 6ii: 200 supercritical alphabets (C_i >= 0): 1198 integral cycles found, none containing a positive state.
Test 6iii: six-branch chart: all 258 words of length <= 3 have c_w > 0 > Q^R - P^R: no positive cycle exists on any of them.
Test 7: one-letter Syracuse blocks a = 2..9, R <= 6: root always 1/(2^a - 3); integral cycle only at a = 2, all states 1 (L-9912.1).
Test 8: 3021 cycle instances on wide alphabets (706 with >= 2 distinct states): D*x_t in used-range, edge identity, |Q dx| <= W, and G_R | c_w all hold.
RESULT: ALL CHECKS PASSED
```

A byte-for-byte self-check was performed after embedding: the fenced code
block above was extracted from this file and `diff`-compared against the
executed `scratchpad/l9923_tests.py`, and the fenced output block against the
captured run log; both diffs are empty (checker:
`scratchpad/l9923_embed_check.py`).

## Remaining uncertainty

All sub-claims are, in the author's assessment, fully proved; the two
source-spec defects were corrected rather than inherited. Points a verifier
should probe first:

1. **Step 4(i), existence of the entering edges** (the single most delicate
   spot): the backwards-walk argument that a moving cycle has an edge
   $x_u \ne M \to x_{u+1} = M$ (and dually for $m$), including its behavior
   when the maximum is attained at several consecutive positions. Test 3's
   threshold scan corroborates the resulting bound at 10 parameter pairs, but
   the argument itself is the thing to re-derive.
2. **Anchor bookkeeping in Lemma C / Step 2** — that "each $x_t$ is a cycle
   start after rotation" is exactly what upgrades (a) from $x_0$ to all $t$;
   an index slip here would silently weaken (b).
3. **The claim that (5) holds at *every* minimal position** (not just one),
   used implicitly when (2b) is applied "at each minimum-edge datum".
4. **Scope hygiene in Step 7**: only the forgetful direction ($S$-cycle
   $\Rightarrow$ integral cycle) is used; the file nowhere claims the
   converse (an integral cycle of $(3, 2^a, 1)$ need not be an $S$-cycle),
   and a verifier should confirm no later sentence slips into using it.
5. The tests, while exhaustive within their windows (words $\le 6$, bounded
   constant ranges), are finite verification; no proof cites them. The
   threshold scan's 3-constant sweep is bounded (widths $\le 8$, words
   $\le 4$) and is corroboration, not a completeness claim.

## Suggested next attack

- **Use downstream (cheap sieves for chart programs):** package L-9923.1C +
  .2c as a preflight check for any proposed subcritical cycle chart (issue
  #58 successors): compute $W$, then $T_g(E_{\max})$; most candidate
  alphabets die in microseconds, and survivors come with their exact
  admissible $(m, k)$ data — a synthesis target list, in the spirit of the
  project's constructive mission.
- **Strengthen .1S to a full census at width $P+Q$:** classify *all* moving
  cycles of width exactly $P + Q$ (the span bound forces $M - m = 1$; the
  edge analysis then confines states to $\{x, x+1\}$ with both constants
  pinned — conjecturally exactly the two-state cycles of the sharpness
  family, up to shift by multiples of $D$). This would turn the threshold
  into a rigidity theorem.
- **Multi-anchor sieve:** Step 5 uses only the edge leaving the minimum;
  edges leaving the maximum give dually $E = DM - Qk'$, $k' \ge 0$, i.e. a
  second finite condition from above; for moving cycles Step 4(i) gives
  $C_+ \ge DM + P$, so the constant used when *leaving* the maximum
  ($\le DM$) is strictly below $C_+$ — an asymmetry not yet exploited.
  Combining min- and max-anchored laws should thin $T_g$ further.
- **Port to varying-modulus alphabets:** L-9905's cycle equation has fixed
  constant and varying $2$-power; this file fixes the modulus and varies the
  constant. The common generalization (blocks $Q_i x' = P_i x + C_i$) has
  cycle equation $\big(\prod_t Q_{i_t} - \prod_t P_{i_t}\big)x_0 = \sum_t
  \big(\prod_{u>t} P_{i_u}\big)\big(\prod_{u<t} Q_{i_u}\big)C_{i_t}$ (later
  steps contribute their $P$, earlier steps their $Q$, matching Lemma A's
  $P^{R-1-t}Q^t$); which parts of the
  collapse/sieve survive (with $D$ replaced by what?) is a concrete open
  follow-up that would subsume both files.
- **Refute attempts:** search for a moving cycle at $W = P+Q$ *not* of the
  two-state form (would refute the census conjecture above, not this file);
  push the threshold scan to 4-constant alphabets and longer words.

---
*File authored by fable-02-p17, 2026-07-26. Status PROPOSED per NOTATION.md
conventions; an independent reviewing agent may upgrade after verification.*

---

## Verification note (fable-02-v25, 2026-07-26)

**Verdict: PASS.** Independent adversarial review per README §13: the claims
were restated and every proof step reconstructed from `NOTATION.md` alone;
every quantifier and boundary case audited; the central strengthening
subjected to a counterexample hunt that is *exhaustive* — over all alphabets,
all word lengths, all cycle lengths — for every pair $1 \le P < Q \le 30$;
the sieve, refinement, gate, and sign lemma checked on independently
generated cycles; and the embedded test block audited byte-for-byte. No
substantive gap found; the first unsupported inference (README §13.9) does
not exist. Status upgraded PROPOSED → PROVED and this reviewer recorded in
the header. Per README §7 the file is **not** marked INDEPENDENTLY_VERIFIED —
that requires a further reviewer beyond this first independent review. Two
cosmetic wording points are recorded in §V.5; neither affects any statement
or proof, and the author's text was left untouched.

### V.1 Reconstruction of the strengthening $W < P+Q$ (L-9923.1S)

The file's main novelty over its source spec is the sharp threshold, and its
load-bearing new step is Step 4(i). My independent reconstruction, in full:

Let a **moving** integral cycle be given, so $M > m$, hence $R \ge 2$; read
indices in $\mathbb{Z}/R\mathbb{Z}$.

*Existence of an edge entering the maximum.* $J = \{t : x_t = M\}$ is
nonempty (the max is attained) and proper (some $x_t = m \ne M$). Fix
$t^* \in J$ and let $j^* \in \{1, \dots, R\}$ be **minimal** with
$x_{t^*-j^*} \ne M$; it exists because the $R$ predecessor indices
$t^*-1, \dots, t^*-R$ cover all residues and $J$ is proper. Set
$u := t^* - j^*$. Then $x_u \ne M$ and $x_{u+1} = M$: for $j^* = 1$ because
$u+1 = t^*$; for $j^* \ge 2$ because minimality of $j^*$ forces
$x_{t^*-(j^*-1)} = M$. This disposes of every degenerate configuration
probed: the maximum attained once, many times, or in consecutive runs (the
walk skips a run to its entry edge); $R = 1$ and $M = m$ cannot occur for a
moving cycle, so no vacuous case is hit.

*The inequality.* $x_u$ is an integer below the maximum, so $x_u \le M - 1$.
The defining relation at $u$ gives $C_{i_u} = Qx_{u+1} - Px_u = QM - Px_u$,
and since the coefficient of $-x_u$ is $P \ge 1 > 0$,
$$C_+ \ \ge\ C_{i_u} \ =\ QM - Px_u \ \ge\ QM - P(M-1) \ =\ DM + P .$$
Dually an edge $x_{u'} \to m$ with $x_{u'} \ge m + 1$ exists, and
$C_- \le C_{i_{u'}} = Qm - Px_{u'} \le Dm - P$. Subtracting,
$$W \ \ge\ C_{i_u} - C_{i_{u'}} \ \ge\ (DM + P) - (Dm - P) \ =\ D(M-m) + 2P
\ \ge\ D + 2P \ =\ P + Q ,$$
using $M - m \ge 1$ (integer states). Remarks from the audit: the two
entering edges are automatically distinct ($u = u'$ would force
$M = x_{u+1} = m$), and the two used constants are forced to differ
($C_{i_u} - C_{i_{u'}} \ge D + 2P > 0$) — but the proof needs neither fact,
only $C_{i_u} \le C_+$ and $C_{i_{u'}} \ge C_-$, so no hidden distinctness
assumption is present.

(ii) is the contrapositive plus the constant-cycle computation (edge
identity at equal states, which never used $W < Q$ — checked). (iii) is the
direct check of $\{Q, -P\}$ on $0 \leftrightarrow 1$; the equality analysis
($W = P + Q$ forces $M - m = 1$ and pins the entering constants to
$C_+ = DM + P$, $C_- = Dm - P$) yields a sharp testable prediction used in
§V.2. (iv) is one subtraction, and $0 < Q < P + Q$ for $P \ge 1$ refutes the
source's $W = Q$ example; I verified the $P = 0$ remark separately
($\{0, Q\}$ does carry $0 \leftrightarrow 1$ when $P = 0$; excluded here).

All remaining steps were reconstructed and found correct: Lemma A
(induction; machine-checked at 4000 random $(P, Q, \text{trajectory})$
instances with arbitrary $P, Q \ge 1$, no order), Lemma B (telescoping),
Lemma C (the $r$-rotation's relation at $j$ is the original relation at
index $r+j$, which the $R$-periodic extension satisfies at every index —
including the wrap, where it is exactly the closure $x_R = x_0$ substituted
into the relation at $R-1$), Step 1's convex combination (weight positivity
is exactly where $P \ge 1$ enters; $G_R \mid c_w$ from integrality of
$Dx_0$; strictness when two constant values occur), Step 2's all-anchor
upgrade (each $x_t$ is $y_0$ of its rotation — precisely what turns (a) into
the position-uniform bound; no index slip found), Step 3's integrality
pinch, Step 5 (positivity of states enters **only** as $m \ge 1$, minimality
**only** as $k_t \ge 0$; the law is derived at an *arbitrary* minimal
position, hence holds at every one — the quantifier (2b) consumes), Step 6
(mod $g$: $D \equiv Q$ from $g \mid P$; invertibility of $Q$ from
$\gcd(g, Q) = 1$; $m + k_t \ge g$ from divisibility plus positivity), Step 7
(**only** the forgetful direction $S$-cycle $\Rightarrow$ integral cycle is
used; I confirmed no sentence anywhere uses the converse), and Step 8 (see
§V.3). The Dependency and Gap audits' assertions were each spot-checked and
are accurate; the citation structure is acyclic ((1C) cites 4(ii), Step 4
does not use (1C); Step 7 cites Step 8, Step 8 uses only Lemmas A–C).

### V.2 Counterexample hunt — scope and outcome

The fatal object would be a moving integral cycle with $W < P + Q$. Two
elementary closure facts make a *complete* hunt possible:

- **Superset closure.** Every cycle of an alphabet is a cycle of any
  super-alphabet, and any alphabet of width $\le P+Q-1$ is a subset of the
  full integer interval $\{b, b+1, \dots, b+P+Q-1\}$ with $b = C_-$. So it
  suffices to test full intervals.
- **Shift closure.** $Q(x'+s) = P(x+s) + (C + Ds)$ iff $Qx' = Px + C$:
  shifting all constants by $Ds$ shifts all cycles by $s$ and preserves
  moving-ness. So only $b \bmod D$ matters.
- **Complete state window.** Every integral cycle of every length satisfies
  $C_- \le Dx_t \le C_+$ by the elementary predecessor bound: the maximal
  state $M$ has a within-cycle predecessor $x_u \le M$, so
  $QM = Px_u + C_{i_u} \le PM + C_+$, i.e. $DM \le C_+$; dually
  $Dm \ge C_-$. (This is Step 4(i)'s mechanism *without* moving-ness,
  derived independently here so the search's completeness does not rest on
  the claims under test.) Hence the digraph on
  $[\lfloor C_-/D \rfloor - 5,\ \lceil C_+/D \rceil + 5]$ with edges
  $x \to (Px + C_i)/Q$ (where integral) contains every integral cycle of
  **every length** as a closed walk, and a moving cycle exists iff some
  strongly connected component has $\ge 2$ vertices.

Outcome (`v25_complete_narrow.py`, §V.6): for **all 435 pairs**
$1 \le P < Q \le 30$ — coprime and non-coprime — and all $D$ base residues,
the width-$(P+Q-1)$ intervals carry **no moving cycle**. Within this
parameter range that settles the narrow regime for *every* alphabet of every
size and constant range, on *every* word of *every* length: the hunt has no
cap other than $Q \le 30$. Additionally, at width exactly $P + Q$ the
interval $\{b, \dots, b+P+Q\}$ carries a moving cycle **iff**
$D \mid (b + P)$ — precisely the prediction extracted from the span bound's
equality analysis plus the witness family $\{Q, -P\} + Ds$ — verified in
both directions at 5510 instances ($Q \le 20$).

Independent randomized/structured hunts (`v25_verify.py`, §V.6; seed
20260726, machinery disjoint from the author's) corroborate: a threshold
scan at 15 pairs including non-coprime $(2,4), (6,9), (4,10), (2,8),
(3,12)$ finds minimal moving 2-letter width $= P + Q$ on the nose (all
cycle lengths); 5334 exhaustive-in-a-box narrow 3-letter alphabets and 6000
random narrow alphabets with $s \le 6$, $Q \le 20$ (3195 of them in the
beyond-spec regime $Q \le W \le P+Q-1$, the file's genuinely new range) —
none moving, and the constant cycles found are exactly the predicted fixed
points $C_i/D$, $D \mid C_i$; 1040 adversarial "near-entering-edge"
alphabets built from $\{Dm-P+1, DM+P-1, \dots\}$ (widths just below
threshold with both edge estimates nearly tight) — none moving; 915
width-$Q$ pairs (the source's refuted sharpness shape) at 15 pairs — none
moving at any length, refuting the source's example independently. On the
wide side, 1314 moving cycles were found (words $\le 6$) and every one
satisfies $C_+ \ge DM + P$, $C_- \le Dm - P$, and $W \ge D(M-m) + 2P$; the
edges entering the maximum and the minimum were located explicitly in each
and their identities/inequalities confirmed edge by edge; every moving cycle
at $W = P + Q$ exactly has $M - m = 1$. **The strengthening survives; no
counterexample was found in any regime.** (Finite verification per
NOTATION.md, never proof — but note the narrow sweep's completeness within
its $Q \le 30$ frontier.)

### V.3 Sign hypothesis (L-9923.2) and the $C_i \ge 0$ edge (L-9923.3(ii))

**No sign hypothesis on the $E_i$ — confirmed.** (2a)'s proof uses
positivity of *states* exactly once ($m \ge 1$) and minimality exactly once
($k_t \ge 0$); no sign property of the alphabet is used anywhere, and the
floor $E_{i_t} \ge D$ is a conclusion, not an assumption. The witness family
$\{Dm + Qk,\ Dm - Pk\}$ genuinely carries the positive 2-cycle $(m, m+k)$:
verified by direct iteration at 840 grid instances over 15 $(P,Q)$ pairs,
**429 with a negative down-constant**, the min-edge law holding in all. On
independently generated data the law $E = Dm + Qk_t$, the floor, and
$T(E_{\max})$-membership hold at *every minimal position* of 2153 positive
cycles (615 moving); 400 alphabets with all $E_i \le 0$ carry no positive
cycle of **any** length (complete positive-window graph search: positive
cycles satisfy $1 \le x_t \le C_+/D$ by the same predecessor bound); the
$g$-refinement ($g \mid (m + k_t)$, $m + k_t \ge g$, $E \ge gD$) holds at
1293 instances; 400 below-gate alphabets ($E_{\max} \le g(D-1) < gD$) carry
no positive cycle of **any** length — strengthening the author's
length-$\le 5$ gate check to all lengths; gate sharpness $x = g$ at
$E = gD$ holds for all tested $(g, P, Q)$; and the worked survivor instance
$T_g(21) = \{6, 9, 12, 15, 18, 21\}$ with $\{21, -3\}$ on $(3, 6)$ was
re-derived from scratch.

**The $\ge 0$ edge — correct as stated.** The two-line proof needs only
$c_w \ge 0$; the contradiction $(Q^R - P^R)x_0 \le -x_0 \le -1 < 0 \le c_w$
has slack, so a zero constant nowhere breaks strictness — strictness comes
from $x_0 \ge 1$, not from $C_i > 0$ (the spec's $C_i > 0$ is indeed not
needed). The probed configuration — a cycle through the zero-constant fixed
point — is handled correctly: $x = 0$ *is* a legal integral cycle when
$0$ is in the alphabet, and it contains no positive state, consistent with
the lemma's exact conclusion (which forbids positive *states on cycles*,
not cycles). Sharper derived fact, confirmed computationally and provable in
two lines from the same display: any supercritical $C_i \ge 0$ cycle
visiting $0$ has $(Q^R - P^R)\cdot 0 = c_w = 0$, and the strictly positive
coefficients force every used constant and every state to be $0$. In 1929
cycles of 300 random supercritical alphabets (112 containing the constant
$0$), no positive state occurred and every $0$-visiting cycle was
identically $0$; $(P, Q, C) = (3, 2, \{1\})$ sits at $x = -1$ for all
lengths $\le 8$; the six-branch alphabet was recomputed from
$7 \cdot 3^{2i} 2^{15-3i}$, matches D-9916.2 of L-9916 exactly, and has
$c_w > 0 > Q^R - P^R$ at all 258 words of length $\le 3$. The Syracuse
one-letter check (Step 7's numbers) was repeated independently for
$a = 2..10$, $R \le 6$: root always $1/(2^a - 3)$, integral exactly at
$a = 2$ with all states $1$.

### V.4 Embedded-block audit

The file's single embedded `python` block (357 lines) was extracted,
executed unmodified (CPython 3, Linux, ~3.8 s), and its output compared
against the recorded output block: **byte-for-byte identical** (empty
`diff`), including every count (164, 10920, 732/366/…, 104, 1246/150,
623, 1198, 258, 3021/706). The script is deterministic as claimed (seed
99230, exact integer arithmetic; a second run reproduced it again). Its
logic was audited: `cycle_on_word` is sound *and* complete per word (unique
rational root since $Q^R \ne P^R$; per-step divisibility checks), Python `%`
semantics are safe at the negative dividends/divisors it encounters
(including the supercritical negative denominator in Test 6), and Test 2's
completeness assertion (found fixed points $=$ predicted $\{C_i/D\}$) is
implemented correctly for negative constants.

### V.5 Cosmetic points (documented; author's text left unchanged)

1. **Step 4(i), index range of the backwards walk.** The walk
   "$t^*, t^*-1, \dots$" can reach indices below $0$, while the Definitions
   extend indices periodically only for $j \ge 0$. The intended reading
   (indices in $\mathbb{Z}/R\mathbb{Z}$, as the definition of $J$ already
   uses) is unambiguous and correct; a fully pedantic phrasing anchors the
   walk at $t^* + R$: take $j^* \in \{1, \dots, R\}$ minimal with
   $x_{t^* + R - j^*} \ne M$, so every index touched lies in the defined
   range.
2. **Statement L-9923.3(i)** says "L-9923.1(a) alone forces
   $(2^a - 3)x_t = 1$ for every $t$"; reaching *every* $t$ uses (a)
   together with Lemma C (rotation), exactly as Step 7 then does. "Alone"
   should be read as "without the collapse clause (c)".

Neither point weakens any claim; both are wording-level only.

### V.6 Verification code and output

Independent implementation (different seed, different machinery — notably
the all-lengths SCC search over a provably complete state window, versus
the author's word-length-capped enumeration; found cycles are re-verified
relation-by-relation with exact integers). Scripts kept session-local at
`scratchpad/v25_verify.py`, `scratchpad/v25_complete_narrow.py`; full code
inline, byte-identical to the executed files.

```python
#!/usr/bin/env python3
"""
Independent adversarial verification of L-9923 (fable-02-v25, 2026-07-26).
Written from the STATEMENTS alone; implementation independent of the file's
embedded script (different seed, different enumeration methods).

Two complete cycle-search methods:
  (1) word method: for each word, the cycle equation (Q^R - P^R) x_0 = c_w has
      a unique rational root (Q != P); integrality of x_0 and of every
      intermediate state is checked BY DIRECT ITERATION of Q x' = P x + C.
      Complete over all words of length <= Rmax, states unbounded.
  (2) state-graph method: every integral cycle's states satisfy
      C_- <= D m <= D x_t <= D M <= C_+  by the elementary predecessor bound
      (max state M has a predecessor x_u <= M: QM = P x_u + C <= PM + C_+, so
      DM <= C_+; dually for m).  Hence the digraph on the integer window
      [floor(C_-/D) - slack, ceil(C_+/D) + slack] with edges x -> (Px+C_i)/Q
      (when integral and in-window) contains EVERY integral cycle of EVERY
      length as a closed walk.  A moving cycle exists  <=>  some SCC has >= 2
      vertices.  Complete for ALL R (no length cap).
For positive cycles: same graph restricted to x >= 1 (window [1, C_+/D + slack]);
any cycle there (self-loop included) is a positive integral cycle and vice versa.
"""
import sys, random
from fractions import Fraction
from itertools import product as iprod, combinations
from math import gcd

rng = random.Random(20260726)
FAILS = []
def chk(label, cond):
    if not cond:
        FAILS.append(label)
        print("FAIL:", label)

def exact_div(a, b):
    """a/b as int if b | a, else None. b != 0, any signs."""
    q, r = divmod(a, b)
    return q if r == 0 else None

def word_cycle(P, Q, C, word):
    """Unique cycle on this word, verified by direct iteration; else None."""
    R = len(word)
    den = Q**R - P**R
    if den == 0:
        return None
    num = 0
    for t, i in enumerate(word):           # c_w = sum P^(R-1-t) Q^t C_it
        num += P**(R - 1 - t) * Q**t * C[i]
    x0 = exact_div(num, den)
    if x0 is None:
        return None
    xs = [x0]
    for i in word:
        nxt = exact_div(P * xs[-1] + C[i], Q)
        if nxt is None:
            return None
        xs.append(nxt)
    if xs[-1] != xs[0]:
        return None                        # cannot happen; belt & braces
    for t, i in enumerate(word):           # re-verify every relation exactly
        assert Q * xs[t + 1] == P * xs[t] + C[i]
    return xs[:R]

def word_cycles(P, Q, C, Rmax):
    out = []
    for R in range(1, Rmax + 1):
        for word in iprod(range(len(C)), repeat=R):
            xs = word_cycle(P, Q, C, word)
            if xs is not None:
                out.append((word, xs))
    return out

def graph_edges(P, Q, C, lo, hi):
    adj = {x: [] for x in range(lo, hi + 1)}
    for x in range(lo, hi + 1):
        for c in C:
            y = exact_div(P * x + c, Q)
            if y is not None and lo <= y <= hi:
                adj[x].append(y)
    return adj

def sccs(adj):
    """Iterative Tarjan."""
    index = {}; low = {}; onstk = {}; stk = []; out = []; ctr = [0]
    for root in adj:
        if root in index:
            continue
        work = [(root, iter(adj[root]))]
        index[root] = low[root] = ctr[0]; ctr[0] += 1
        stk.append(root); onstk[root] = True
        while work:
            v, it = work[-1]
            advanced = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = ctr[0]; ctr[0] += 1
                    stk.append(w); onstk[w] = True
                    work.append((w, iter(adj[w])))
                    advanced = True
                    break
                elif onstk.get(w):
                    low[v] = min(low[v], index[w])
            if advanced:
                continue
            work.pop()
            if work:
                pv = work[-1][0]
                low[pv] = min(low[pv], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stk.pop(); onstk[w] = False; comp.append(w)
                    if w == v:
                        break
                out.append(comp)
    return out

def window(P, Q, C, slack=4):
    D = Q - P
    lo = min(C); hi = max(C)
    a = lo // D - slack               # floor
    b = -((-hi) // D) + slack         # ceil
    return a, b

def moving_exists(P, Q, C, slack=4):
    """ALL cycle lengths: True iff a moving integral cycle exists."""
    a, b = window(P, Q, C, slack)
    adj = graph_edges(P, Q, C, a, b)
    return any(len(c) >= 2 for c in sccs(adj))

def const_states(P, Q, C, slack=4):
    """All fixed-point states (self-loops) in the provable window."""
    a, b = window(P, Q, C, slack)
    adj = graph_edges(P, Q, C, a, b)
    return {x for x in adj if x in adj[x]}

def pos_cycle_exists(P, Q, C, slack=4):
    """ALL lengths: True iff a POSITIVE integral cycle exists."""
    D = Q - P
    hi = max(C)
    if hi < D:                        # even the elementary bound kills it
        return False
    b = -((-hi) // D) + slack
    adj = graph_edges(P, Q, C, 1, b)
    if any(x in adj[x] for x in adj):
        return True
    return any(len(c) >= 2 for c in sccs(adj))

def T_set(D, Q, B):
    """T(B), built by scanning candidate values (independent structure)."""
    out = set()
    for v in range(D, B + 1):
        mu = 1
        while D * mu <= v:
            if (v - D * mu) % Q == 0:
                out.add(v); break
            mu += 1
    return out

def Tg_set(D, Q, g, B):
    out = set()
    for mu in range(1, B // D + 1):
        ka = 0
        v = D * mu
        while v <= B:
            if (mu + ka) % g == 0:
                out.add(v)
            ka += 1; v += Q
    return out

# =====================================================================
print("== A. Lemma A / Lemma B (independent random spot check) ==")
nA = 0
for _ in range(500):
    P = rng.randint(1, 25); Q = rng.randint(1, 25)
    xs = [rng.randint(-60, 60) for _ in range(8)]
    cs = [Q * xs[t + 1] - P * xs[t] for t in range(7)]
    for j in range(8):
        rhs = P**j * xs[0] + sum(P**(j - 1 - t) * Q**t * cs[t] for t in range(j))
        chk("A.iterate", Q**j * xs[j] == rhs); nA += 1
    for R in range(1, 8):
        G = sum(P**(R - 1 - t) * Q**t for t in range(R))
        chk("A.geom", (Q - P) * G == Q**R - P**R)
print(f"   {nA} iterate-identity instances, geometric sums OK")

# =====================================================================
print("== B. THRESHOLD SCAN (all cycle lengths, SCC method) ==")
PAIRS = [(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (2, 4),
         (6, 9), (4, 10), (2, 8), (5, 8), (7, 12), (9, 10), (3, 12)]
for (P, Q) in PAIRS:
    D = Q - P
    minw = None
    for w in range(0, P + Q + 1):
        found = False
        for b in range(-(P + Q) - 15, (P + Q) + 16):
            if moving_exists(P, Q, [b, b + w]):
                found = True; break
        if found:
            minw = w; break
    chk(f"B.minwidth P={P} Q={Q}", minw == P + Q)
    print(f"   (P,Q)=({P},{Q}) D={D}: minimal 2-letter moving width = {minw} "
          f"(claim: {P+Q})")

# 3-letter exhaustive-in-a-box, all widths below threshold, ALL R
print("== B2. 3-letter narrow alphabets: exhaustive box, ALL R ==")
tot3 = 0
for (P, Q) in [(1, 2), (2, 3), (3, 4), (2, 4), (3, 5), (6, 9), (2, 5)]:
    for b in range(-10, 11):
        for w in range(0, P + Q):
            for u in range(0, w + 1):
                C = [b, b + u, b + w]
                if moving_exists(P, Q, C):
                    chk(f"B2 moving P={P} Q={Q} C={C}", False)
                tot3 += 1
print(f"   {tot3} narrow 3-letter alphabets: no moving cycle of ANY length")

# random narrow alphabets, s up to 6, wider (P,Q), beyond-spec regime flagged
print("== B3. random narrow alphabets (s<=6, Q<=20), ALL R ==")
n_beyond = 0
for trial in range(6000):
    P = rng.randint(1, 15); Q = rng.randint(P + 1, 20); D = Q - P
    s = rng.randint(1, 6)
    b = rng.randint(-60, 60)
    C = [b] + [b + rng.randint(0, P + Q - 1) for _ in range(s - 1)]
    W = max(C) - min(C)
    if W >= Q:
        n_beyond += 1
    if moving_exists(P, Q, C):
        chk(f"B3 moving P={P} Q={Q} C={C}", False)
    # constant cycles must be exactly the predicted fixed points
    pred = {c // D for c in C if c % D == 0}
    chk(f"B3 fixpoints P={P} Q={Q} C={C}", const_states(P, Q, C) == pred)
print(f"   6000 random narrow alphabets ({n_beyond} in beyond-spec regime "
      f"Q <= W <= P+Q-1): zero moving cycles, fixed points exactly C_i/D")

# adversarial near-equality shapes: C_+ = DM+P-1, C_- = Dm-P+1 (just miss)
print("== B4. adversarial near-entering-edge alphabets, ALL R ==")
n4 = 0
for (P, Q) in PAIRS:
    D = Q - P
    for m in range(-6, 7):
        for M in range(m + 1, m + 4):
            Cm = D * m - P + 1
            CM = D * M + P - 1
            if CM - Cm >= P + Q:      # only widths below threshold
                continue
            for extra in (None, (Cm + CM) // 2, D * m, D * M):
                C = [Cm, CM] + ([extra] if extra is not None else [])
                if max(C) - min(C) >= P + Q:
                    continue
                if moving_exists(P, Q, C):
                    chk(f"B4 moving P={P} Q={Q} C={C}", False)
                n4 += 1
print(f"   {n4} near-equality alphabets: no moving cycle of any length")

# =====================================================================
print("== C. width-Q pairs (source's refuted sharpness shape), ALL R ==")
nc = 0
for (P, Q) in PAIRS:
    for b in range(-30, 31):
        if moving_exists(P, Q, [b, b + Q]):
            chk(f"C moving P={P} Q={Q} b={b}", False)
        nc += 1
print(f"   {nc} width-Q pairs: no moving cycle of any length (source refuted)")

# =====================================================================
print("== D. sharpness at W = P+Q, span bound, entering edges ==")
for (P, Q) in PAIRS:
    D = Q - P
    xs = word_cycle(P, Q, [Q, -P], (0, 1))
    chk(f"D.sharp P={P} Q={Q}", xs == [0, 1])
    chk(f"D.width P={P} Q={Q}", Q - (-P) == P + Q)
# span bound + entering-edge reconstruction on wide random alphabets
n_mov = n_cyc = 0
for trial in range(400):
    P = rng.randint(1, 6); Q = rng.randint(P + 1, 9); D = Q - P
    s = rng.randint(2, 4)
    C = [rng.randint(-30, 30) for _ in range(s)]
    W = max(C) - min(C)
    for word, xs in word_cycles(P, Q, C, 6):
        n_cyc += 1
        M, m = max(xs), min(xs)
        if M == m:
            continue
        n_mov += 1
        R = len(xs)
        chk("D.span W", W >= D * (M - m) + 2 * P)
        chk("D.Cplus", max(C) >= D * M + P)
        chk("D.Cminus", min(C) <= D * m - P)
        # reconstruct Step 4(i): edges entering the max / the min
        ent_max = [t for t in range(R) if xs[(t + 1) % R] == M and xs[t] != M]
        ent_min = [t for t in range(R) if xs[(t + 1) % R] == m and xs[t] != m]
        chk("D.entmax exists", len(ent_max) >= 1)
        chk("D.entmin exists", len(ent_min) >= 1)
        for t in ent_max:
            cu = C[word[t]]
            chk("D.entmax id", cu == Q * M - P * xs[t])
            chk("D.entmax ge", cu >= D * M + P)
        for t in ent_min:
            cu = C[word[t]]
            chk("D.entmin id", cu == Q * m - P * xs[t])
            chk("D.entmin le", cu <= D * m - P)
        if W == P + Q:
            chk("D.diam1", M - m == 1)
print(f"   {n_cyc} cycles on wide alphabets, {n_mov} moving: span bound "
      f"W >= D(M-m)+2P, entering edges exist with the claimed inequalities")
chk("D.some moving", n_mov > 0)

# 2-cycle identity (iv)
n_iv = 0
for trial in range(300):
    P = rng.randint(1, 9); Q = rng.randint(P + 1, 14)
    C = [rng.randint(-40, 40), rng.randint(-40, 40)]
    xs = word_cycle(P, Q, C, (0, 1))
    if xs is not None:
        chk("D.iv", (P + Q) * (xs[1] - xs[0]) == C[0] - C[1])
        if xs[1] != xs[0]:
            chk("D.iv div", (C[0] - C[1]) % (P + Q) == 0)
            chk("D.iv size", abs(C[0] - C[1]) >= P + Q)
        n_iv += 1
print(f"   {n_iv} 2-cycles: (P+Q)(x1-x0) = C0-C1 identity holds")

# =====================================================================
print("== E. sieve law E = D m + Q k at EVERY minimal position ==")
n_pos = n_posmov = 0
for trial in range(300):
    P = rng.randint(1, 6); Q = rng.randint(P + 1, 9); D = Q - P
    s = rng.randint(2, 5)
    C = [rng.randint(-25, 40) for _ in range(s)]
    Emax = max(C)
    T = T_set(D, Q, Emax) if Emax >= D else set()
    for word, xs in word_cycles(P, Q, C, 5):
        if min(xs) < 1:
            continue
        n_pos += 1
        if len(set(xs)) > 1:
            n_posmov += 1
        m = min(xs); R = len(xs)
        for t in range(R):
            if xs[t] != m:
                continue
            kt = xs[(t + 1) % R] - m
            chk("E.k>=0", kt >= 0)
            chk("E.law", C[word[t]] == D * m + Q * kt)
            chk("E.floor", C[word[t]] >= D)
            chk("E.T", C[word[t]] in T)
print(f"   {n_pos} positive cycles ({n_posmov} moving): law, floor E >= D, "
      f"T(E_max) membership at every minimal position")

# corollary: all E_i <= 0 => no positive cycle (ALL R)
n_e0 = 0
for trial in range(400):
    P = rng.randint(1, 8); Q = rng.randint(P + 1, 12)
    C = [rng.randint(-40, 0) for _ in range(rng.randint(1, 4))]
    chk("E.nonpos", not pos_cycle_exists(P, Q, C))
    n_e0 += 1
print(f"   {n_e0} alphabets with all E_i <= 0: no positive cycle of ANY length")

# witness family with negative constants
print("== F. witness family {Dm+Qk, Dm-Pk} (no sign hypothesis needed) ==")
n_wit = n_neg = 0
for (P, Q) in PAIRS:
    D = Q - P
    for m in range(1, 9):
        for k in range(1, 8):
            C = [D * m + Q * k, D * m - P * k]
            if C[1] < 0:
                n_neg += 1
            xs = word_cycle(P, Q, C, (0, 1))
            chk("F.cycle", xs == [m, m + k])
            chk("F.positive", min(xs) >= 1 if xs else False)
            chk("F.law", C[0] == D * m + Q * k)
            n_wit += 1
print(f"   {n_wit} witness 2-cycles verified positive; negative down-constant "
      f"in {n_neg} of them")

# =====================================================================
print("== G. g-refinement, gate (ALL R), gate sharpness ==")
n_g = n_gcyc = 0
for trial in range(300):
    g = rng.randint(2, 6)
    P = g * rng.randint(1, 4)
    Q = P + rng.randint(1, 9)
    while gcd(g, Q) != 1:
        Q += 1
    D = Q - P
    C = [g * rng.randint(-8, 14) for _ in range(rng.randint(2, 4))]
    n_g += 1
    for word, xs in word_cycles(P, Q, C, 5):
        if min(xs) < 1:
            continue
        n_gcyc += 1
        m = min(xs); R = len(xs)
        for t in range(R):
            if xs[t] != m:
                continue
            kt = xs[(t + 1) % R] - m
            chk("G.mod", (m + kt) % g == 0)
            chk("G.sum>=g", m + kt >= g)
            chk("G.floor", C[word[t]] >= g * D)
print(f"   {n_g} g-divisible alphabets, {n_gcyc} positive-cycle instances: "
      f"g|(m+k), m+k >= g, E >= gD")

n_gate = 0
for trial in range(400):
    g = rng.randint(2, 6)
    P = g * rng.randint(1, 4)
    Q = P + rng.randint(1, 9)
    while gcd(g, Q) != 1:
        Q += 1
    D = Q - P
    C = [g * rng.randint(-9, D - 1) for _ in range(rng.randint(1, 4))]
    chk("G.gate", not pos_cycle_exists(P, Q, C))   # ALL cycle lengths
    n_gate += 1
print(f"   {n_gate} below-gate alphabets (E_max <= g(D-1)): no positive "
      f"cycle of ANY length")

for g in range(1, 7):
    for pp in range(1, 4):
        P = g * pp
        for Q in range(P + 1, P + 8):
            if gcd(g, Q) != 1:
                continue
            D = Q - P
            chk(f"G.sharp g={g} P={P} Q={Q}",
                word_cycle(P, Q, [g * D], (0,)) == [g])
print("   gate sharpness x = g at E = gD: all tested (g,P,Q)")

# worked instance from the file, re-derived
Tg = sorted(Tg_set(2, 5, 3, 21))
chk("G.Tg", Tg == [6, 9, 12, 15, 18, 21])
chk("G.inst", word_cycle(3, 5, [21, -3], (0, 1)) == [3, 6])
print(f"   worked instance P=3 Q=5 g=3: T_g(21) = {Tg}; {{21,-3}} cycle (3,6)")

# =====================================================================
print("== H. supercritical sign lemma (C_i >= 0, zeros probed) ==")
n_sc = n_sccyc = n_zero_alpha = 0
for trial in range(300):
    Q = rng.randint(1, 9); P = Q + rng.randint(1, 8)
    s = rng.randint(1, 3)
    C = [rng.randint(0, 30) for _ in range(s)]
    if trial % 3 == 0:
        C[rng.randrange(s)] = 0        # force a zero constant often
    if 0 in C:
        n_zero_alpha += 1
    n_sc += 1
    for word, xs in word_cycles(P, Q, C, 5):
        n_sccyc += 1
        chk("H.nopos", max(xs) <= 0)
        if 0 in xs:                    # cycle through the zero fixed point?
            chk("H.zerocycle", set(xs) == {0})
            chk("H.zeroconsts", all(C[i] == 0 for i in word))
print(f"   {n_sc} supercritical alphabets ({n_zero_alpha} containing 0): "
      f"{n_sccyc} integral cycles, none with a positive state; every cycle "
      f"visiting 0 is identically 0 on all-zero constants")
# the (3,2,{1}) shortcut alphabet
for R in range(1, 9):
    xs = word_cycle(3, 2, [1], tuple([0] * R))
    chk("H.312", xs == [-1] * R)
print("   (P,Q,C)=(3,2,{1}): every cycle length 1..8 sits at x = -1")

# =====================================================================
print("== I. one-letter Syracuse (3, 2^a, 1) ==")
for a in range(2, 11):
    Q = 2**a; D = Q - 3
    for R in range(1, 7):
        num = sum(3**(R - 1 - t) * Q**t for t in range(R))
        chk("I.root", Fraction(num, Q**R - 3**R) == Fraction(1, D))
        xs = word_cycle(3, Q, [1], tuple([0] * R))
        chk("I.integral", (xs == [1] * R) if a == 2 else xs is None)
print("   a = 2..10, R <= 6: root 1/(2^a-3); integral only at a = 2 (all 1)")

# =====================================================================
print("== J. six-branch chart data ==")
Pb, Qb = 3**12, 2**19
A = [7 * 3**(2 * i) * 2**(15 - 3 * i) for i in range(6)]
chk("J.vals", sorted(A) == [229376, 258048, 290304, 326592, 367416, 413343])
chk("J.super", Pb > Qb)
nw = 0
for R in range(1, 4):
    for word in iprod(range(6), repeat=R):
        num = sum(Pb**(R - 1 - t) * Qb**t * A[i] for t, i in enumerate(word))
        chk("J.sign", num > 0 > Qb**R - Pb**R)
        nw += 1
print(f"   alphabet matches L-9916; {nw} words length <= 3: c_w > 0 > Q^R-P^R")

# =====================================================================
print()
if FAILS:
    print(f"VERDICT: {len(FAILS)} FAILURES"); sys.exit(1)
print("VERDICT: ALL INDEPENDENT CHECKS PASSED")
```

Output (verbatim, run 2026-07-26, CPython 3, Linux; identical across
reruns — fixed seed, exact integer arithmetic; ~3 s):

```text
== A. Lemma A / Lemma B (independent random spot check) ==
   4000 iterate-identity instances, geometric sums OK
== B. THRESHOLD SCAN (all cycle lengths, SCC method) ==
   (P,Q)=(1,2) D=1: minimal 2-letter moving width = 3 (claim: 3)
   (P,Q)=(1,3) D=2: minimal 2-letter moving width = 4 (claim: 4)
   (P,Q)=(2,3) D=1: minimal 2-letter moving width = 5 (claim: 5)
   (P,Q)=(3,4) D=1: minimal 2-letter moving width = 7 (claim: 7)
   (P,Q)=(2,5) D=3: minimal 2-letter moving width = 7 (claim: 7)
   (P,Q)=(3,5) D=2: minimal 2-letter moving width = 8 (claim: 8)
   (P,Q)=(4,5) D=1: minimal 2-letter moving width = 9 (claim: 9)
   (P,Q)=(2,4) D=2: minimal 2-letter moving width = 6 (claim: 6)
   (P,Q)=(6,9) D=3: minimal 2-letter moving width = 15 (claim: 15)
   (P,Q)=(4,10) D=6: minimal 2-letter moving width = 14 (claim: 14)
   (P,Q)=(2,8) D=6: minimal 2-letter moving width = 10 (claim: 10)
   (P,Q)=(5,8) D=3: minimal 2-letter moving width = 13 (claim: 13)
   (P,Q)=(7,12) D=5: minimal 2-letter moving width = 19 (claim: 19)
   (P,Q)=(9,10) D=1: minimal 2-letter moving width = 19 (claim: 19)
   (P,Q)=(3,12) D=9: minimal 2-letter moving width = 15 (claim: 15)
== B2. 3-letter narrow alphabets: exhaustive box, ALL R ==
   5334 narrow 3-letter alphabets: no moving cycle of ANY length
== B3. random narrow alphabets (s<=6, Q<=20), ALL R ==
   6000 random narrow alphabets (3195 in beyond-spec regime Q <= W <= P+Q-1): zero moving cycles, fixed points exactly C_i/D
== B4. adversarial near-entering-edge alphabets, ALL R ==
   1040 near-equality alphabets: no moving cycle of any length
== C. width-Q pairs (source's refuted sharpness shape), ALL R ==
   915 width-Q pairs: no moving cycle of any length (source refuted)
== D. sharpness at W = P+Q, span bound, entering edges ==
   6084 cycles on wide alphabets, 1314 moving: span bound W >= D(M-m)+2P, entering edges exist with the claimed inequalities
   3 2-cycles: (P+Q)(x1-x0) = C0-C1 identity holds
== E. sieve law E = D m + Q k at EVERY minimal position ==
   2153 positive cycles (615 moving): law, floor E >= D, T(E_max) membership at every minimal position
   400 alphabets with all E_i <= 0: no positive cycle of ANY length
== F. witness family {Dm+Qk, Dm-Pk} (no sign hypothesis needed) ==
   840 witness 2-cycles verified positive; negative down-constant in 429 of them
== G. g-refinement, gate (ALL R), gate sharpness ==
   300 g-divisible alphabets, 1293 positive-cycle instances: g|(m+k), m+k >= g, E >= gD
   400 below-gate alphabets (E_max <= g(D-1)): no positive cycle of ANY length
   gate sharpness x = g at E = gD: all tested (g,P,Q)
   worked instance P=3 Q=5 g=3: T_g(21) = [6, 9, 12, 15, 18, 21]; {21,-3} cycle (3,6)
== H. supercritical sign lemma (C_i >= 0, zeros probed) ==
   300 supercritical alphabets (112 containing 0): 1929 integral cycles, none with a positive state; every cycle visiting 0 is identically 0 on all-zero constants
   (P,Q,C)=(3,2,{1}): every cycle length 1..8 sits at x = -1
== I. one-letter Syracuse (3, 2^a, 1) ==
   a = 2..10, R <= 6: root 1/(2^a-3); integral only at a = 2 (all 1)
== J. six-branch chart data ==
   alphabet matches L-9916; 258 words length <= 3: c_w > 0 > Q^R-P^R

VERDICT: ALL INDEPENDENT CHECKS PASSED
```

```python
#!/usr/bin/env python3
"""
Conclusive finite check of L-9923.1S(ii) per (P,Q), over ALL alphabets and ALL
cycle lengths, via two reductions:

  (R1) superset closure: any alphabet with W <= P+Q-1 is a subset of the full
       integer interval I_b = {b, b+1, ..., b+P+Q-1} with b = C_-; every
       integral cycle of the subset is an integral cycle of I_b.  So if no I_b
       carries a moving cycle, no narrow alphabet does.
  (R2) shift closure: replacing C by C + D*s bijects cycles with states
       shifted by s (Q(x'+s) = P(x+s) + C + D s), preserving moving-ness.
       So only b mod D matters; testing D consecutive bases covers ALL b.

  Combined with the SCC search (complete for all cycle lengths inside the
  provable state window C_-/D <= x <= C_+/D, by the elementary predecessor
  bound: the max state M has a predecessor x_u <= M, so QM <= PM + C_+,
  i.e. DM <= C_+; dually Dm >= C_-), a clean sweep verifies: for this (P,Q),
  NO moving integral cycle exists for ANY alphabet of width <= P+Q-1 on ANY
  word of ANY length.  (Finite verification per (P,Q).)

Also: at width exactly P+Q, the interval I_b = {b, ..., b+P+Q} carries a
moving cycle IFF D | (b+P) -- the prediction extracted from the equality
analysis of the span bound (C_+ = DM+P and C_- = Dm-P are forced at
W = P+Q) plus the witness family {Q,-P} shifted by multiples of D.
Both directions are tested.
"""
import sys

def exact_div(a, b):
    q, r = divmod(a, b)
    return q if r == 0 else None

def graph_edges(P, Q, C, lo, hi):
    adj = {x: [] for x in range(lo, hi + 1)}
    for x in range(lo, hi + 1):
        for c in C:
            y = exact_div(P * x + c, Q)
            if y is not None and lo <= y <= hi:
                adj[x].append(y)
    return adj

def sccs(adj):
    index = {}; low = {}; onstk = {}; stk = []; out = []; ctr = [0]
    for root in adj:
        if root in index:
            continue
        work = [(root, iter(adj[root]))]
        index[root] = low[root] = ctr[0]; ctr[0] += 1
        stk.append(root); onstk[root] = True
        while work:
            v, it = work[-1]
            advanced = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = ctr[0]; ctr[0] += 1
                    stk.append(w); onstk[w] = True
                    work.append((w, iter(adj[w])))
                    advanced = True
                    break
                elif onstk.get(w):
                    low[v] = min(low[v], index[w])
            if advanced:
                continue
            work.pop()
            if work:
                pv = work[-1][0]
                low[pv] = min(low[pv], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stk.pop(); onstk[w] = False; comp.append(w)
                    if w == v:
                        break
                out.append(comp)
    return out

def moving_exists(P, Q, C, slack=5):
    D = Q - P
    lo = min(C) // D - slack
    hi = -((-max(C)) // D) + slack
    return any(len(c) >= 2 for c in sccs(graph_edges(P, Q, C, lo, hi)))

FAILS = 0
print("== Conclusive narrow-regime sweep (ALL alphabets via interval supersets,")
print("   ALL bases via shift closure, ALL cycle lengths via SCC) ==")
n_pairs = 0
for Q in range(2, 31):
    for P in range(1, Q):
        D = Q - P
        for b in range(D):                         # (R2): all bases mod D
            I = list(range(b, b + P + Q))          # width P+Q-1
            if moving_exists(P, Q, I):
                print(f"FAIL: moving cycle, P={P} Q={Q} interval base {b}")
                FAILS += 1
        n_pairs += 1
print(f"   all (P,Q), 1 <= P < Q <= 30: {n_pairs} pairs swept clean -- no")
print("   moving cycle for ANY alphabet of width <= P+Q-1, ANY word length")

print("== Width exactly P+Q: interval carries a moving cycle iff D | (b+P) ==")
n_eq = 0
for Q in range(2, 21):
    for P in range(1, Q):
        D = Q - P
        for b in range(-2 * D, 2 * D + 1):
            I = list(range(b, b + P + Q + 1))      # width P+Q
            got = moving_exists(P, Q, I)
            want = ((b + P) % D == 0)
            if got != want:
                print(f"FAIL: P={P} Q={Q} b={b}: moving={got} predicted={want}")
                FAILS += 1
            n_eq += 1
print(f"   {n_eq} width-(P+Q) intervals: existence matches the equality-")
print("   analysis prediction D | (b+P) exactly, both directions")

print()
print("RESULT:", "ALL CHECKS PASSED" if FAILS == 0 else f"{FAILS} FAILURES")
sys.exit(0 if FAILS == 0 else 1)
```

Output (verbatim, same environment; ~1 s):

```text
== Conclusive narrow-regime sweep (ALL alphabets via interval supersets,
   ALL bases via shift closure, ALL cycle lengths via SCC) ==
   all (P,Q), 1 <= P < Q <= 30: 435 pairs swept clean -- no
   moving cycle for ANY alphabet of width <= P+Q-1, ANY word length
== Width exactly P+Q: interval carries a moving cycle iff D | (b+P) ==
   5510 width-(P+Q) intervals: existence matches the equality-
   analysis prediction D | (b+P) exactly, both directions

RESULT: ALL CHECKS PASSED
```

### V.7 Confidence and status action

High confidence. Every proof is short, elementary integer arithmetic,
reconstructed here independently; the computational corroboration is
complete within stated windows, and its completeness rests on the closure
facts and the predecessor window bound of §V.2 — derived in this note, not
on the claims under test. Header updated: Status PROPOSED → PROVED,
reviewer recorded. Not marked INDEPENDENTLY_VERIFIED (requires a further
independent reviewer per README §7 / NOTATION.md conventions).

*Reviewed by fable-02-v25, 2026-07-26.*
