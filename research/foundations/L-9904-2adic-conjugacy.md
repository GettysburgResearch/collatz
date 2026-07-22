# L-9904 — The 2-adic extension of $T$, the parity-word isometry $Q$, and the exact integrality obstruction

```text
Claim ID:      L-9904
Title:         2-adic extension of T, shift conjugacy via the parity-word map Q,
               and the exact integrality obstruction for symbolic constructions
Status:        PROVED
Authoring agent:   fable-02-p3
Reviewing agents:  fable-02-v8 (adversarial review 2026-07-22: PASS, with two
                   remark-level fixes documented in the Verification note)
Created:       2026-07-21
Last updated:  2026-07-22 (adversarial review by fable-02-v8; fixes to the
                   L-9904.7 box and the Q-9904 remark only — no change to any
                   numbered claim or proof)
Dependencies:  NOTATION.md (D-9902, D-9906, conventions); L-9902 (PROPOSED, under review;
               cited for the Z^+ counterparts, Z_2 versions re-proved inline);
               L-9903 (PROPOSED, under review; word-level .2/.3 used as stated,
               .1 re-derived over Z_2 as Lemma A). Standard 2-adic / measure-theory
               background imported as facts B1-B8 (see Definitions; imports flagged).
Scope:         All z in Z_2, all k >= 0; all finite and infinite binary words.
               Q-9904 is an OPEN QUESTION, clearly labeled, with no direction claimed.
Related counterexample candidates: none directly; L-9904.7 is the precise statement of
               the obstruction every symbolic candidate (issues #21, #4, #10, #18) faces.
```

---

## Statement

Throughout, $\mathbb{Z}_2$ is the ring of 2-adic integers with absolute value
$|\cdot|_2$ and valuation $\nu_2$ (NOTATION.md preamble); the background facts B1–B8
used about $\mathbb{Z}_2$ are collected, with justifications, in Definitions.
$\mathbb{Z}_{(2)} := \{p/q : p, q \in \mathbb{Z},\ q \text{ odd}\}$ denotes the rationals
with odd denominator. "Odd" ("even") for $z \in \mathbb{Z}_2$ means $z \not\equiv 0$
($z \equiv 0$) mod $2\mathbb{Z}_2$, i.e. first 2-adic digit $1$ ($0$).

**The 2-adic shortcut map.** Define $T : \mathbb{Z}_2 \to \mathbb{Z}_2$ by
$$T(z) := \begin{cases} z/2 & z \text{ even},\\[2pt] (3z+1)/2 & z \text{ odd}. \end{cases}$$
By P0 below this restricts on $\mathbb{Z}^+$ to the shortcut map of D-9902; the parity
data $v_i(z) := T^i(z) \bmod 2 \in \{0,1\}$ and $a_k(z) := \sum_{i<k} v_i(z)$ are exactly
D-9906, which already permits $z \in \mathbb{Z}_2$. The **infinite parity word** of $z$ is
$V(z) := (v_0(z), v_1(z), v_2(z), \dots) \in \{0,1\}^{\infty}$, and the
**parity-word map** is
$$Q : \mathbb{Z}_2 \to \mathbb{Z}_2, \qquad Q(z) := \sum_{i \ge 0} v_i(z)\, 2^i ,$$
a convergent series in $\mathbb{Z}_2$ (B6) whose digit sequence is exactly $V(z)$ (B1).
The **digit shift** is $\sigma\big(\sum_{i\ge0} b_i 2^i\big) := \sum_{i \ge 0} b_{i+1} 2^i$,
equivalently $\sigma(y) = (y - b_0(y))/2$.

**L-9904.1 (basic structure).** $T$ is well-defined and continuous on $\mathbb{Z}_2$, and
it is exactly 2-to-1: for every $w \in \mathbb{Z}_2$, the full preimage is
$$T^{-1}(\{w\}) \;=\; \Big\{\, 2w,\;\; \frac{2w-1}{3} \,\Big\},$$
two distinct elements ($2w$ even, $(2w-1)/3$ odd), where $(2w-1)/3$ **always** exists in
$\mathbb{Z}_2$ because $3 \in \mathbb{Z}_2^\times$.

> **Contrast with $\mathbb{Z}^+$ (boxed).** Over the positive integers the even-branch
> preimage $2w$ always exists, but the odd-branch preimage $(2w-1)/3$ is a positive
> integer **only** under the congruence condition $w \equiv 2 \pmod 3$ (and then it is
> $\ge 1$ for $w \ge 2$). The 2-adic ring erases this congruence obstruction because $3$
> is invertible there. The $\mathbb{Z}^+$ inverse-tree structure is the subject of
> L-9909 (in progress by another agent).

**L-9904.2 (locality over $\mathbb{Z}_2$).** For all $z, m \in \mathbb{Z}_2$ and $j \ge 1$:
$$T(z + 2^j m) \;=\; T(z) + 3^{\,v_0(z)}\, 2^{\,j-1} m,$$
and iteratively, for all $k \ge 0$ and $0 \le i \le k$:
$$T^i(z + 2^k m) \;=\; T^i(z) + 3^{\,a_i(z)}\, 2^{\,k-i} m, \qquad
v_i(z + 2^k m) = v_i(z) \ \ (0 \le i \le k-1).$$
Hence $v_i(z)$ depends only on $z \bmod 2^{\,i+1}\mathbb{Z}_2$, the induced maps
$$\pi_k : \mathbb{Z}_2 / 2^k \mathbb{Z}_2 \longrightarrow \{0,1\}^k, \qquad
z + 2^k\mathbb{Z}_2 \mapsto (v_0(z), \dots, v_{k-1}(z))$$
are well-defined, and each $\pi_k$ is a **bijection**. (Route: proved directly over
$\mathbb{Z}_2$, not by density from $\mathbb{Z}^+$; see the Proof. Under the canonical
isomorphism $\mathbb{Z}_2/2^k\mathbb{Z}_2 \cong \mathbb{Z}/2^k\mathbb{Z}$ (B4), $\pi_k$
coincides with the map $\pi_k$ of L-9902, by P0.)

**L-9904.3 ($Q$ is a measure-preserving isometric homeomorphism).**
1. *(Isometry.)* For all $z, z' \in \mathbb{Z}_2$: $\;|Q(z) - Q(z')|_2 = |z - z'|_2$.
2. *(Bijection.)* $Q : \mathbb{Z}_2 \to \mathbb{Z}_2$ is a bijection; equivalently
   (composing with B1), $V : \mathbb{Z}_2 \to \{0,1\}^\infty$ is a bijection. Hence $Q$
   is a homeomorphism (its inverse is also an isometry).
3. *(Measure preservation.)* Let $\mu$ be the unique Borel probability measure on
   $\mathbb{Z}_2$ with $\mu(c + 2^k\mathbb{Z}_2) = 2^{-k}$ for every ball (B8; this is
   the Haar probability measure). Then $\mu(Q^{-1}(A)) = \mu(A) = \mu(Q(A))$ for every
   Borel $A \subseteq \mathbb{Z}_2$.

**L-9904.4 (conjugacy to the shift).** $Q \circ T = \sigma \circ Q$ on $\mathbb{Z}_2$;
equivalently $v_i(T(z)) = v_{i+1}(z)$ for all $z$ and $i \ge 0$; iterating,
$Q \circ T^k = \sigma^k \circ Q$ for all $k \ge 0$. So $T$ on $(\mathbb{Z}_2, \mu)$ is
topologically and measure-theoretically conjugate, via $Q$, to the digit shift $\sigma$
on $(\mathbb{Z}_2, \mu)$ (i.e. to the one-sided Bernoulli$(\tfrac12,\tfrac12)$ shift in
digit coordinates). **Corollary L-9904.4b:** $T$ and $\sigma$ both preserve $\mu$:
$\mu(T^{-1}A) = \mu(A)$ for all Borel $A$ (proved directly from L-9904.1).

**L-9904.5 (realization and periodic points).**
1. *(Realization.)* Every infinite word $b = (b_i)_{i \ge 0} \in \{0,1\}^\infty$ is the
   parity word of **exactly one** $z \in \mathbb{Z}_2$, namely
   $z = Q^{-1}\big(\sum_i b_i 2^i\big)$.
2. *(Periodic points.)* Let $w \in \{0,1\}^K$, $K \ge 1$, $a := |w|_1$ its number of
   ones, and $\rho_w := \rho(w)$ the word constant of L-9903.2. The unique
   $z \in \mathbb{Z}_2$ with parity word $w^\infty$ satisfies $T^K(z) = z$ and equals
   $$z \;=\; \frac{\rho_w}{2^K - 3^{a}} \;\in\; \mathbb{Z}_{(2)} \subset \mathbb{Q},$$
   the division being legitimate because $2^K - 3^a$ is **odd** (hence a 2-adic unit),
   nonzero for every $K \ge 1$, $0 \le a \le K$. Sign: for $a \ge 1$, $\rho_w > 0$
   (L-9903.3), so $z > 0$ (as a rational) $\iff 2^K > 3^a$ — the same positivity
   threshold as the positive-cycle constraint of L-9905.2 ($S$-form: $2^K > 3^m$; their
   $m$ counts odd steps, as does our $a$). For $a = 0$: $w = 0^K$, $\rho_w = 0$, $z = 0$.
   Anchors (proved in L-9904.6): $w = (1,0) \Rightarrow z = 1$; $w = (1) \Rightarrow
   z = -1$; $w = (1,1,0) \Rightarrow z = -5$; and $z = -17$ realizes
   $w = (1,1,1,1,0,1,1,1,0,0,0)$ with $K = 11$, $a = 7$, $\rho_w = 2363$.
3. *(Eventually periodic $\Rightarrow$ rational.)* If $V(z)$ is eventually periodic then
   $z \in \mathbb{Z}_{(2)}$. Moreover *(3b, orbit dichotomy)*: $V(z)$ is eventually
   periodic $\iff$ the $T$-orbit of $z$ is eventually periodic (i.e.
   $T^{\ell + K}(z) = T^{\ell}(z)$ for some $\ell \ge 0$, $K \ge 1$).
4. *(Converse: open.)* See Q-9904 below.

**Q-9904 (OPEN QUESTION; no direction claimed).** *Is every rational element of
$\mathbb{Z}_2$ — equivalently, every $z \in \mathbb{Z}_{(2)}$ — eventually periodic
under $T$? Equivalently (by L-9904.5.3b): is the parity word of every rational
eventually periodic?*
Status: OPEN. L-9904.5.3 proves one implication (eventually periodic word
$\Rightarrow$ rational); Q-9904 is its converse. **Containment remark (proved as
Lemma D below):** for $n \in \mathbb{Z}^+$, the $T$-orbit of $n$ is divergent
$\iff$ it is not eventually periodic $\iff$ $V(n)$ is not eventually periodic. Hence a
divergent positive-integer orbit would be exactly a rational (indeed integer) element of
$\mathbb{Z}_2$ with non-eventually-periodic parity word — a negative witness to Q-9904
of a special kind. Consequently: an affirmative answer to Q-9904 would rule out
divergent positive-integer trajectories (the divergence half of the Collatz problem); a
negative witness lying in $\mathbb{Z}^+$ would be a Collatz counterexample; a negative
witness in $\mathbb{Z}_{(2)} \setminus \mathbb{Z}$ would settle Q-9904 without directly
settling Collatz. (Both "Collatz counterexample" claims here are in the D-9909 sense,
which is phrased for the map $C$; the $T$-to-$C$ transfer is supplied self-containedly by
the Note after Lemma D in the Proof section — added in review 2026-07-22.) No direction
is asserted or suggested here.

**L-9904.6 (worked micro-examples; exact finite computations).** The anchors of .5(ii),
the rationals $1/3$, $1/5$, $1/7$, and the values $Q(0) = 0$, $Q(-1) = -1$,
$Q(1) = -1/3$, $Q(2) = -2/3$; all stated and proved in the Proof section.

**L-9904.7 (the boxed obstruction remark).** See the prominently boxed statement in the
Proof section: by .5(i), realizing **any** infinite parity word 2-adically costs
nothing; therefore every symbolic/parity-word counterexample construction is exactly
equivalent to proving that its unique 2-adic realizer is a **positive integer**.

---

## Definitions and background facts

All Collatz notation is from NOTATION.md (D-9902 for $T$ on $\mathbb{Z}^+$; D-9906 for
$v_i, a_k$, stated there for $n \in \mathbb{Z}^+$ *or* $n \in \mathbb{Z}_2$). The word
constant $\rho(w)$ is from L-9903 (Statement and L-9903.2): $r_0 := 0$,
$r_{i+1} := 3^{w_i} r_i + w_i 2^i$, $\rho(w) := r_{|w|}$, with closed form
$\rho(w) = \sum_{i : w_i = 1} 3^{s_i(w)} 2^i$, $s_i(w) := \#\{j > i : w_j = 1\}$.
These are integer-combinatorial definitions on words, independent of any domain.

The following standard structure facts about $\mathbb{Z}_2$ are used. B1, B5, B6 and the
existence half of B8 are imported from the standard construction of $\mathbb{Z}_2$ and
standard measure theory (flagged again in the Dependency audit); B2–B4, B7 and the rest
are justified inline.

- **B1 (digit model).** $\mathbb{Z}_2$ is the completion of $\mathbb{Z}$ under
  $|\cdot|_2$; every $z \in \mathbb{Z}_2$ has a **unique** expansion
  $z = \sum_{i \ge 0} b_i(z) 2^i$ with digits $b_i(z) \in \{0,1\}$, and every
  $\{0,1\}$-sequence arises. Digitwise, $z \mapsto (b_i(z))$ is a homeomorphism onto the
  product space $\{0,1\}^\infty$. $\mathbb{Z}_2$ is a commutative integral domain
  containing $\mathbb{Z}$, and is compact.
- **B2 (valuation).** For $z \ne 0$, $\nu_2(z) = \min\{i : b_i(z) = 1\}$ and
  $|z|_2 = 2^{-\nu_2(z)}$; $|z|_2 \le 2^{-k} \iff z \in 2^k\mathbb{Z}_2 \iff
  b_0(z) = \dots = b_{k-1}(z) = 0$. The metric is an ultrametric:
  $|x + y|_2 \le \max(|x|_2, |y|_2)$, with equality when $|x|_2 \neq |y|_2$.
  Division by $2^k$: for $x \in 2^k \mathbb{Z}_2$ there is a unique $y \in \mathbb{Z}_2$
  with $2^k y = x$ (uniqueness: integral domain), written $x/2^k$; $|x/2^k|_2 = 2^k|x|_2$.
- **B3 (units).** $\mathbb{Z}_2^\times = \{z : b_0(z) = 1\}$ = the odd elements; in
  particular $3$ and every odd rational integer is a unit; a product of odd elements is
  odd; odd $+$ even $=$ odd; for a unit $u$, $u \mathbb{Z}_2 = \mathbb{Z}_2$ and
  $|uz|_2 = |z|_2$. (Justification: $z$ odd $\Rightarrow z = 1 + 2t$, and
  $(1+2t)^{-1} = \sum_{n \ge 0} (-2t)^n$ converges by B6; the parity algebra reads off
  digit $0$.)
- **B4 (balls and quotients).** The closed ball of radius $2^{-k}$ around $c$ is
  $B(c, 2^{-k}) = c + 2^k\mathbb{Z}_2$; every ball is clopen, every point of a ball is a
  center, and two balls are nested or disjoint (ultrametric). For each $k$ there are
  exactly $2^k$ balls of radius $2^{-k}$, represented by $c \in \{0, 1, \dots, 2^k - 1\}$
  (truncation of digits); hence $\mathbb{Z}_2/2^k\mathbb{Z}_2$ has exactly $2^k$
  elements and is canonically $\mathbb{Z}/2^k\mathbb{Z}$. The set of all balls is
  countable and is a base of the topology.
- **B5 (completeness / nested balls).** A nested sequence of closed balls
  $B_0 \supseteq B_1 \supseteq \cdots$ with radii $\to 0$ has intersection exactly one
  point. (Choose $z_k \in B_k$; Cauchy; the limit lies in each closed $B_k$; two such
  points differ by an element of $\bigcap_k 2^k\mathbb{Z}_2 = \{0\}$.)
- **B6 (series).** A series $\sum_i c_i$ with $|c_i|_2 \to 0$ converges in
  $\mathbb{Z}_2$ (partial sums Cauchy, ultrametric); in particular $\sum_i \epsilon_i 2^i$
  converges for any bounded $\epsilon_i \in \mathbb{Z}_2$, and
  $\sum_{i > j} \epsilon_i 2^i \in 2^{j+1}\mathbb{Z}_2$ (each partial sum is, and
  $2^{j+1}\mathbb{Z}_2$ is closed).
- **B7 ($\mathbb{Q} \cap \mathbb{Z}_2 = \mathbb{Z}_{(2)}$).** A rational $p/q$ in lowest
  terms lies in $\mathbb{Z}_2$ iff $q$ is odd. (*Proof.* If $q$ odd: $q$ is a unit (B3),
  so $p q^{-1} \in \mathbb{Z}_2$. If $q$ even: lowest terms forces $p$ odd, so
  $\nu_2(p/q) = -\nu_2(q) < 0$ and $p/q \notin \mathbb{Z}_2$. Parity of $p/q \in
  \mathbb{Z}_{(2)}$: $q^{-1}$ is odd, so $p/q \equiv p \pmod 2$.)
- **B8 (the measure $\mu$).** There exists a Borel probability measure $\mu$ on
  $\mathbb{Z}_2$ with $\mu(c + 2^k\mathbb{Z}_2) = 2^{-k}$ for every ball — e.g. the Haar
  probability measure of the compact group $(\mathbb{Z}_2, +)$ (the $2^k$ cosets of
  $2^k\mathbb{Z}_2$ are translates partitioning $\mathbb{Z}_2$, hence each has Haar
  measure $2^{-k}$), equivalently the image of the Bernoulli$(\tfrac12,\tfrac12)$
  product measure under B1. **Existence is imported as standard.** *Uniqueness* is
  proved below (Lemma U), and translation-invariance is recovered as a corollary, so
  nothing downstream depends on the imported construction beyond existence. Singletons
  are $\mu$-null ($\{z\} \subseteq B(z, 2^{-k})$ for all $k$), hence every countable set
  — in particular $\mathbb{Z}^+$, $\mathbb{Z}$, and $\mathbb{Q} \cap \mathbb{Z}_2$ — is
  $\mu$-null.

---

## Motivation

This file is the rigorous common foundation for the repository's symbolic and 2-adic
directions, and its chief service is L-9904.7: converting the folklore statement "the
hard part of any parity-word construction is integrality" into a precise, citable
equivalence.

- **Issue #21 (foundry):** its realization theorem T-9601 manufactures orbits from
  feedback-defined parity words; L-9904.5(i) is the general realization mechanism, and
  L-9904.7 states exactly what the foundry's "integrality frontier" must deliver.
- **Issue #4 (amplifier algebra, M1) and issue #10 (sanctuary):** invariant-object
  constructions face the question "does the invariant set contain a positive integer";
  L-9904.7 shows this is not an artifact of those approaches but the exact residual
  content of the problem.
- **Issue #18 and the symbolic/rewrite directions:** parity words may be manipulated
  freely; the conjugacy L-9904.4 says the dynamics is *exactly* the digit shift, so all
  symbolic dynamics is faithful — and .5(ii) gives closed-form rational realizers for
  all periodic behavior.
- **Issues #15/#16 (measure/ergodic side):** L-9904.3(3) and L-9904.4b give the
  measure-theoretic dictionary ($T$ on $(\mathbb{Z}_2,\mu)$ $\cong$ Bernoulli shift), and
  B8's null-set observation delimits what measure arguments can ever produce
  (see L-9904.7).
- **Cycles program (issue #9, L-9905):** the periodic-point formula .5(ii) is the
  $T$-form cycle equation solved *in $\mathbb{Z}_2$*, where it always has a unique
  solution; the entire cycle problem over $\mathbb{Z}^+$ is whether that rational is a
  positive integer — the same integrality obstruction in miniature.

---

## Proof

### P0 (compatibility with the $\mathbb{Z}^+$ theory)

$\mathbb{Z} \subset \mathbb{Z}_2$ (B1) and for $n \in \mathbb{Z}$, $n$ is even/odd as an
integer iff $n \in 2\mathbb{Z}_2$ / $n \notin 2\mathbb{Z}_2$ (B2/B3: $2 \mid n$ in
$\mathbb{Z}$ iff $2 \mid n$ in $\mathbb{Z}_2$, since $n/2 \in \mathbb{Q} \cap \mathbb{Z}_2
= \mathbb{Z}_{(2)}$ forces $n/2 \in \mathbb{Z}$ when $n \in \mathbb{Z}$ — or simply by
B7's parity computation). The two branch formulas of the 2-adic $T$ agree with D-9902 on
$\mathbb{Z}^+$, so $T|_{\mathbb{Z}^+}$ is D-9902's map, and $v_i, a_k$ computed in
$\mathbb{Z}_2$ agree with D-9906 on $\mathbb{Z}^+$. Likewise $T$ maps $\mathbb{Z}$ into
$\mathbb{Z}$ and $\mathbb{Z}_{(2)}$ into $\mathbb{Z}_{(2)}$ (both branch formulas do; for
the odd branch on $\mathbb{Z}_{(2)}$, numerators/denominators stay odd-denominator —
detailed again in .5(iii)). $\square$

### L-9904.1 (well-defined, continuous, exactly 2-to-1)

**Well-defined.** If $z$ is even, $z \in 2\mathbb{Z}_2$, so $z/2 \in \mathbb{Z}_2$ exists
and is unique (B2). If $z$ is odd, then $3z$ is odd (product of odd elements, B3) and
$3z + 1$ is even, so $(3z+1)/2 \in \mathbb{Z}_2$. The two cases partition $\mathbb{Z}_2$.

**Continuous.** $\mathbb{Z}_2 = 2\mathbb{Z}_2 \sqcup (1 + 2\mathbb{Z}_2)$ is a partition
into two clopen balls (B4). On $2\mathbb{Z}_2$: $|T(z) - T(z')|_2 = |(z-z')/2|_2 =
2\,|z - z'|_2$ (B2), so $T$ is Lipschitz with constant $2$ there. On $1 + 2\mathbb{Z}_2$:
$|T(z) - T(z')|_2 = |3(z - z')/2|_2 = 2\,|z - z'|_2$ ($|3|_2 = 1$, B3). A map Lipschitz
(hence continuous) on each member of a finite clopen cover is continuous: the preimage of
an open set is the union of its two relatively open (hence open, by clopenness) parts.

**Exactly 2-to-1.** Fix $w \in \mathbb{Z}_2$.
*The two candidates are preimages:* $2w$ is even and $T(2w) = w$. Set
$z_1 := (2w - 1)/3 = (2w-1)\cdot 3^{-1}$, which exists since $3 \in \mathbb{Z}_2^\times$
(B3); $2w - 1$ is odd and $3^{-1}$ is odd (its inverse $3$ is odd, and units have odd
inverses by B3), so $z_1$ is odd; then $T(z_1) = (3z_1 + 1)/2 = ((2w - 1) + 1)/2 = w$.
*No others:* any $z$ with $T(z) = w$ is even or odd; if even, $z/2 = w$ forces $z = 2w$;
if odd, $(3z+1)/2 = w$ forces $3z = 2w - 1$, i.e. $z = z_1$ (division by the unit $3$ is
unique). *Distinct:* $2w$ is even, $z_1$ is odd. $\blacksquare$

> **Boxed contrast with $\mathbb{Z}^+$.** For $w \in \mathbb{Z}^+$: $2w \in \mathbb{Z}^+$
> always, but $z_1 = (2w-1)/3 \in \mathbb{Z}$ iff $3 \mid 2w - 1$ iff $w \equiv 2
> \pmod 3$ (as $2w - 1 \equiv 2w + 2 = 2(w+1) \pmod 3$, and $3 \nmid 2$), and then
> $z_1 \ge 1$ iff $w \ge 2$. So over $\mathbb{Z}^+$ only a density-$\tfrac13$ set of
> vertices has an odd-branch parent, while over $\mathbb{Z}_2$ **every** vertex has both
> parents: the inverse orbit tree is the full binary tree. The $\mathbb{Z}^+$ tree is
> L-9909's subject (in progress by another agent).

### L-9904.2 (locality; $\pi_k$ bijections)

**Route taken (explicit):** everything is proved *directly over $\mathbb{Z}_2$*,
mirroring the $\mathbb{Z}^+$ proofs of L-9902.1–.2 (cited as the counterpart; its final
remark already observes the proofs carry over). No density argument from
$\mathbb{Z}^+ \hookrightarrow \mathbb{Z}_2$ is used anywhere, so no continuity
transfer needs to be justified.

**One step.** Let $z, m \in \mathbb{Z}_2$, $j \ge 1$. Then $2^j m \in 2\mathbb{Z}_2$, so
$z + 2^j m \equiv z \pmod{2\mathbb{Z}_2}$ and $v_0(z + 2^j m) = v_0(z)$. If $v_0(z) = 0$:
$T(z + 2^j m) = (z + 2^j m)/2 = z/2 + 2^{j-1} m = T(z) + 3^0 2^{j-1} m$ (the middle step
is the uniqueness in B2: $2(z/2 + 2^{j-1}m) = z + 2^j m$). If $v_0(z) = 1$:
$T(z + 2^j m) = (3z + 3\cdot 2^j m + 1)/2 = (3z+1)/2 + 3 \cdot 2^{j-1} m
= T(z) + 3^1 2^{j-1} m$. $\square$

**Iterated.** Fix $k \ge 0$, $z, m \in \mathbb{Z}_2$. By induction on $0 \le i \le k$:
the claim $P(i)$: $T^i(z + 2^k m) = T^i(z) + 3^{a_i(z)} 2^{k-i} m$. Base $P(0)$:
$a_0 = 0$, both sides $z + 2^k m$. Step ($i \le k-1$): apply the one-step identity with
base point $T^i(z)$, exponent $j := k - i \ge 1$, increment $M := 3^{a_i(z)} m$; it gives
$v_i(z + 2^k m) = v_0(T^i(z) + 2^j M) = v_0(T^i(z)) = v_i(z)$ and
$T^{i+1}(z + 2^k m) = T^{i+1}(z) + 3^{v_i(z)} 2^{k-i-1} \cdot 3^{a_i(z)} m =
T^{i+1}(z) + 3^{a_{i+1}(z)} 2^{k-(i+1)} m$, which is $P(i+1)$ plus the bit preservation
for $i \le k - 1$. $\square$

**Well-definedness of $\pi_k$.** If $z \equiv z' \pmod{2^{i+1}\mathbb{Z}_2}$, write
$z' = z + 2^{i+1} m$ and apply the iterated statement with $k := i+1$: $v_i(z') = v_i(z)$.
Hence $v_i$ is a function of $z \bmod 2^{i+1}\mathbb{Z}_2$; since $2^{i+1} \mid 2^k$ for
$i \le k - 1$, the length-$k$ word is a function of $z \bmod 2^k \mathbb{Z}_2$ and
$\pi_k$ is well-defined. $\square$

**Injectivity.** Let $z \not\equiv z' \pmod{2^k\mathbb{Z}_2}$. Then $z - z' \ne 0$; put
$j := \nu_2(z - z')$, so $0 \le j \le k-1$ (B2: $j \ge k$ would mean
$z \equiv z' \bmod 2^k$) and $z = z' + 2^j u$ with $u := (z - z')/2^j \in
\mathbb{Z}_2^\times$ (B2/B3: its digit $0$ is $1$). The iterated identity with
$(k, i) := (j, j)$ gives
$$T^j(z) = T^j(z') + 3^{\,a_j(z')}\, u,$$
whose increment is a product of units, hence odd (B3); so $v_j(z) = 1 - v_j(z') \ne
v_j(z')$, and the words differ at coordinate $j \le k - 1$. $\square$

**Surjectivity.** $\mathbb{Z}_2/2^k\mathbb{Z}_2$ and $\{0,1\}^k$ both have exactly $2^k$
elements (B4); an injection between finite sets of equal cardinality is a bijection.
$\blacksquare$

*(Compatibility: by P0, evaluating $\pi_k$ at integer representatives $\{1, \dots,
2^k\}$ reproduces L-9902's $\pi_k$ under $\mathbb{Z}_2/2^k\mathbb{Z}_2 \cong
\mathbb{Z}/2^k\mathbb{Z}$; the two files prove the same bijection over the two domains,
independently.)*

### L-9904.3 ($Q$: isometry, bijection, homeomorphism, measure preservation)

$Q$ is well-defined: $|v_i(z) 2^i|_2 \le 2^{-i} \to 0$, so the series converges (B6),
and since the coefficients are digits in $\{0,1\}$, B1's uniqueness gives
$b_i(Q(z)) = v_i(z)$ for all $i$: the digit sequence of $Q(z)$ **is** $V(z)$.

**(1) Isometry.** If $z = z'$ both sides are $0$. Otherwise let
$j := \nu_2(z - z') < \infty$. By L-9904.2 (well-definedness clause), $v_i(z) = v_i(z')$
for all $i \le j - 1$ (as $z \equiv z' \bmod 2^{i+1}$ for $i + 1 \le j$), and by the
injectivity computation above (applied with $k := j+1$, which has
$\nu_2(z - z') = j \le k - 1$), $v_j(z) = 1 - v_j(z')$. Hence
$$Q(z) - Q(z') \;=\; \sum_{i \ge j} \big(v_i(z) - v_i(z')\big) 2^i
\;=\; 2^j \Big[ \underbrace{\big(v_j(z) - v_j(z')\big)}_{=\ \pm 1}
\;+\; 2\,t \Big], \qquad t := \sum_{i > j} \big(v_i(z) - v_i(z')\big)\, 2^{\,i-j-1},$$
where $t \in \mathbb{Z}_2$ by B6 (coefficients in $\{-1, 0, 1\}$). The bracket is
$\pm 1 + \text{even} = $ odd, a unit (B3), so $\nu_2(Q(z) - Q(z')) = j = \nu_2(z - z')$,
i.e. $|Q(z) - Q(z')|_2 = |z - z'|_2$. $\square$

**(2) Bijection and homeomorphism.** *Injectivity* is immediate from (1)
($z \ne z' \Rightarrow |Q(z) - Q(z')|_2 = |z - z'|_2 \ne 0$). *Surjectivity:* let
$y \in \mathbb{Z}_2$ with digits $b_i := b_i(y)$. For each $k \ge 0$ let
$r_k := \pi_k^{-1}\big((b_0, \dots, b_{k-1})\big) \in \mathbb{Z}_2/2^k\mathbb{Z}_2$
(L-9904.2 bijectivity), a coset $= $ closed ball of radius $2^{-k}$ (B4); $r_0 =
\mathbb{Z}_2$. *Nesting:* if $z \in r_{k+1}$, its length-$(k{+}1)$ word is
$(b_0, \dots, b_k)$, so its length-$k$ word is $(b_0, \dots, b_{k-1})$, so its class mod
$2^k$ is $r_k$ by uniqueness (injectivity of $\pi_k$); hence $r_{k+1} \subseteq r_k$. By
B5 the nested balls $r_k$ (radii $2^{-k} \to 0$) intersect in exactly one point $z^*$,
and for every $k$, $z^* \in r_k$ gives $v_i(z^*) = b_i$ for all $i < k$; letting
$k \to \infty$, $V(z^*) = (b_i)_{i \ge 0}$ and $Q(z^*) = y$. So $Q$ is a bijection.
Its inverse is an isometry ($|Q^{-1}(y) - Q^{-1}(y')|_2 = |Q(Q^{-1}y) - Q(Q^{-1}y')|_2 =
|y - y'|_2$ by (1)), so both $Q$ and $Q^{-1}$ are $1$-Lipschitz, hence continuous: $Q$
is a homeomorphism. $\square$

**Lemma M (bijective isometries map balls onto balls).** *If $f : \mathbb{Z}_2 \to
\mathbb{Z}_2$ is a bijective isometry, then $f\big(B(c, 2^{-k})\big) =
B\big(f(c), 2^{-k}\big)$ for every ball.* — *Proof.* Isometry gives
$f(B(c, 2^{-k})) \subseteq B(f(c), 2^{-k})$. The inverse $f^{-1}$ is also an isometry
(as above), so $f^{-1}(B(f(c), 2^{-k})) \subseteq B(c, 2^{-k})$, i.e.
$B(f(c), 2^{-k}) \subseteq f(B(c, 2^{-k}))$. $\square$

**Lemma U (uniqueness of $\mu$ on balls).** *Any two Borel probability measures on
$\mathbb{Z}_2$ that agree on every ball are equal.* — *Proof.* Let
$\mathcal{P} := \{\text{balls}\} \cup \{\emptyset\}$. $\mathcal{P}$ is a $\pi$-system:
two balls are nested or disjoint (B4), so intersections stay in $\mathcal{P}$. The balls
are countably many and form a base (B4), so every open set is a countable union of balls
and lies in $\sigma(\mathcal{P})$; hence $\sigma(\mathcal{P})$ is the Borel
$\sigma$-algebra. $\mathbb{Z}_2 = B(0, 1) \in \mathcal{P}$. By Dynkin's $\pi$–$\lambda$
theorem (standard measure theory), two probability measures agreeing on $\mathcal{P}$
agree on $\sigma(\mathcal{P}) = $ Borel. $\square$

**(3) Measure preservation.** $\mu$ exists (B8, imported) and is the unique Borel
probability measure with ball values $2^{-k}$ (Lemma U). $Q$ is a homeomorphism, so
$A \mapsto \mu(Q^{-1}(A))$ and $A \mapsto \mu(Q(A))$ are Borel probability measures.
By Lemma M applied to $Q$ and to $Q^{-1}$ (both bijective isometries),
$Q^{-1}(B(c, 2^{-k})) = B(Q^{-1}(c), 2^{-k})$ and $Q(B(c, 2^{-k})) = B(Q(c), 2^{-k})$,
so both measures assign every ball of radius $2^{-k}$ the value $2^{-k}$; by Lemma U
both equal $\mu$. $\blacksquare$

*(Corollary of the same argument: every translation $z \mapsto z + a$ is a bijective
isometry, so $\mu$ is translation-invariant — recovering, from the ball values alone,
that $\mu$ is the Haar probability measure.)*

### L-9904.4 (shift conjugacy) and L-9904.4b ($T$ preserves $\mu$)

$\sigma$ is well-defined: $y - b_0(y) \in 2\mathbb{Z}_2$, and $(y - b_0(y))/2$ has digit
sequence $(b_1(y), b_2(y), \dots)$ (shift the expansion, B1/B2).

**Conjugacy.** For all $z$ and $i \ge 0$: $T^i(T(z)) = T^{i+1}(z)$ by definition of
iteration, so $v_i(T(z)) = v_{i+1}(z)$. Hence the digit sequence of $Q(T(z))$ is
$(v_1(z), v_2(z), \dots)$, which is exactly the digit sequence of $\sigma(Q(z))$; by
uniqueness of digit expansions (B1), $Q(T(z)) = \sigma(Q(z))$. Iterating,
$Q \circ T^k = \sigma^k \circ Q$ (induction on $k$; base $k = 0$ trivial). Since $Q$ is
a measure-preserving homeomorphism (L-9904.3), $T$ on $(\mathbb{Z}_2, \mu)$ is
topologically and metrically conjugate to $\sigma$, which in digit coordinates (B1,
carrying $\mu$ to the product measure, B8) is the one-sided Bernoulli
$(\tfrac12,\tfrac12)$ shift. $\blacksquare$

**L-9904.4b.** For a ball $B(c, 2^{-k})$, L-9904.1 gives
$$T^{-1}\big(c + 2^k \mathbb{Z}_2\big) \;=\; \big(2c + 2^{k+1}\mathbb{Z}_2\big) \;\sqcup\;
\Big(\tfrac{2c-1}{3} + 2^{k+1}\mathbb{Z}_2\Big),$$
two disjoint balls of radius $2^{-k-1}$: indeed the even preimages of
$w \in c + 2^k\mathbb{Z}_2$ are $2w = 2c + 2(w - c) \in 2c + 2^{k+1}\mathbb{Z}_2$
(and conversely each point there is even and maps into the ball: $T(2c + 2^{k+1}t) =
c + 2^k t$); the odd preimages are $(2w-1)/3 = \tfrac{2c-1}{3} + \tfrac{2}{3}(w - c) \in
\tfrac{2c-1}{3} + 2^{k+1}\mathbb{Z}_2$ (using $\tfrac13 \mathbb{Z}_2 = \mathbb{Z}_2$,
B3; conversely $T\big(\tfrac{2c-1}{3} + 2^{k+1}t\big) = c + 3 \cdot 2^k t$ lands in the
ball, and every point there is odd $= $ odd $+$ even). Disjoint since one ball is even,
the other odd. Hence $\mu(T^{-1}(B)) = 2^{-k-1} + 2^{-k-1} = 2^{-k} = \mu(B)$ for every
ball; $A \mapsto \mu(T^{-1}(A))$ is a Borel probability measure ($T$ continuous, so
$T^{-1}(\text{Borel})$ is Borel), and by Lemma U it equals $\mu$. The same for $\sigma$
(either directly, or via the conjugacy). $\blacksquare$

### Lemma A ($\mathbb{Z}_2$ iteration formula; L-9903.1–.2 transported)

*Define $\rho_0(z) := 0$, $\rho_{i+1}(z) := 3^{v_i(z)} \rho_i(z) + v_i(z) 2^i$ for
$z \in \mathbb{Z}_2$. Then for all $z \in \mathbb{Z}_2$, $k \ge 0$:*
$$2^k\, T^k(z) \;=\; 3^{\,a_k(z)}\, z + \rho_k(z), \qquad
\rho_k(z) = \rho\big(v_0(z), \dots, v_{k-1}(z)\big),$$
*with $\rho(\cdot)$ the word constant of L-9903.2.*

*Proof.* Induction on $k$, identical to L-9903.1's proof (which used only the two branch
formulas and $a_{k+1} = a_k + v_k$, all valid verbatim over $\mathbb{Z}_2$): base
$k = 0$ reads $z = z$; if $v_k(z) = 0$, $2^{k+1} T^{k+1}(z) = 2^k \cdot 2\,T(T^k(z)) =
2^k T^k(z) \cdot \tfrac{2 T(m)}{m}\big|_{m \text{ even}}$ — explicitly, $2T(m) = m$ for
even $m$ and $2T(m) = 3m + 1$ for odd $m$, so
$$2^{k+1} T^{k+1}(z) = 2^k \big(3^{v_k(z)} T^k(z) + v_k(z)\big)
= 3^{v_k(z)}\big(3^{a_k} z + \rho_k\big) + v_k(z) 2^k
= 3^{a_{k+1}} z + \rho_{k+1}.$$
The identification $\rho_k(z) = \rho(\text{word})$ is the same one-line induction as in
L-9903.2 (the two recursions coincide under $w_i := v_i(z)$); the closed form and the
bounds of L-9903.3 are word-level statements, used henceforth without change. $\square$

### L-9904.5 (realization; periodic points; rationality)

**(i) Realization.** By B1 the map $(b_i) \mapsto \sum b_i 2^i$ is a bijection
$\{0,1\}^\infty \to \mathbb{Z}_2$, and $V = (\text{digits}) \circ Q$; so $V$ is a
bijection iff $Q$ is, which is L-9904.3(2). Explicitly: for every
$b \in \{0,1\}^\infty$ there is exactly one $z$ with $v_i(z) = b_i$ for all $i$, namely
$z = Q^{-1}\big(\sum_i b_i 2^i\big)$; constructively, $z$ is the unique point of the
nested balls $\pi_k^{-1}(b_0 \dots b_{k-1})$ (proof of L-9904.3(2)). $\blacksquare$

**(ii) Periodic points.** Let $w \in \{0,1\}^K$, $K \ge 1$, $a := |w|_1$,
$\rho_w := \rho(w)$, and let $z$ be the unique element with $V(z) = w^\infty$ (by (i)).

*Step 1 ($T^K(z) = z$).* By L-9904.4 iterated, $v_i(T^K(z)) = v_{i+K}(z)$ for all $i$;
since $w^\infty$ is $K$-periodic, $v_{i+K}(z) = v_i(z)$; so $V(T^K(z)) = V(z)$, and by
the injectivity in (i), $T^K(z) = z$.

*Step 2 (linear equation).* By Lemma A with $k = K$, using $a_K(z) = |w|_1 = a$ and
$\rho_K(z) = \rho(w) = \rho_w$:
$$2^K z \;=\; 2^K T^K(z) \;=\; 3^a z + \rho_w
\qquad\Longrightarrow\qquad z\,\big(2^K - 3^a\big) \;=\; \rho_w .$$

*Step 3 (the unit denominator — the KEY step).* $K \ge 1$ makes $2^K$ even; $3^a$ is
odd; so $2^K - 3^a$ is an **odd integer**, in particular nonzero, and hence a unit of
$\mathbb{Z}_2$ (B3). Therefore the linear equation has the unique solution
$$z \;=\; \rho_w \cdot \big(2^K - 3^a\big)^{-1} \;=\; \frac{\rho_w}{2^K - 3^a}
\;\in\; \mathbb{Q} \cap \mathbb{Z}_2 = \mathbb{Z}_{(2)} \quad (\text{B7}),$$
a rational with odd denominator — *automatically* rational, with no rationality
hypothesis anywhere. (Uniqueness of $z$ was already known from (i); Step 3 re-derives it
from the equation and, more importantly, evaluates $z$.)

*Sign.* $\rho_w \ge 0$ always, and for $a \ge 1$, $\rho_w \ge 3^a - 2^a \ge 1 > 0$
(L-9903.3, word-level). So for $a \ge 1$: $z > 0 \iff 2^K - 3^a > 0 \iff 2^K > 3^a$, and
$z < 0 \iff 2^K < 3^a$ ($2^K = 3^a$ being impossible by parity). This is the same
threshold as the positive-cycle constraint $2^K > 3^m$ of L-9905.2 (their $S$-form odd-step
count $m$ corresponds to our $a$, their $K$ to our $K$; the correspondence is used here
only as a cross-reference, not as a proved lemma). For $a = 0$: $w = 0^K$, $\rho_w = 0$
(L-9903.3), so $z = 0/(2^K - 1) = 0$, consistent with $T(0) = 0$ and $V(0) = 0^\infty$.
$\blacksquare$

*(Anchors — each verified by exact hand computation in L-9904.6 below: $w = (1,0)$:
$z = 1/(4-3) = 1$; $w = (1)$: $z = 1/(2-3) = -1$; $w = (1,1,0)$: $\rho_w = 5$,
$z = 5/(8-9) = -5$; $w = (1,0,0)$: $z = 1/(8-3) = 1/5$; and $-17$ realizes an
$(K, a) = (11, 7)$ word with $\rho_w = 2363 = (-17)(2^{11} - 3^7)$.)*

**(iii) Eventually periodic $\Rightarrow$ rational; orbit dichotomy.**

*Forward and inverse steps preserve rationality.* If $z \in \mathbb{Q} \cap \mathbb{Z}_2$,
then $T(z) \in \{z/2, (3z+1)/2\} \subseteq \mathbb{Q}$ (and $\in \mathbb{Z}_2$), so
$T(z) \in \mathbb{Z}_{(2)}$. If $T(z) = y \in \mathbb{Q} \cap \mathbb{Z}_2$, then by
L-9904.1 $z \in \{2y, (2y-1)/3\} \subseteq \mathbb{Q}$, so $z \in \mathbb{Z}_{(2)}$.
Both proved; both used below.

*Main claim.* Suppose $V(z) = u\,w^\infty$ with $u \in \{0,1\}^\ell$ ($\ell \ge 0$),
$w \in \{0,1\}^K$, $K \ge 1$. By L-9904.4 iterated, $V(T^\ell(z)) = w^\infty$, so by
(ii), $T^\ell(z) = \rho_w/(2^K - 3^{|w|_1}) \in \mathbb{Q}$. Now downward induction on
$i = \ell, \ell-1, \dots, 0$: $T^\ell(z)$ is rational; if $T^{i+1}(z)$ is rational then
so is $T^i(z)$ (inverse step above, since $T(T^i(z)) = T^{i+1}(z)$). Hence
$z = T^0(z) \in \mathbb{Q} \cap \mathbb{Z}_2 = \mathbb{Z}_{(2)}$. $\square$

*(3b) Orbit dichotomy.* ($\Leftarrow$) If $T^{\ell+K}(z) = T^\ell(z)$ ($K \ge 1$), then
for all $i \ge 0$: $v_{\ell+K+i}(z) = v_i(T^{\ell+K}(z)) = v_i(T^{\ell}(z)) =
v_{\ell+i}(z)$, so $V(z)$ is eventually periodic. ($\Rightarrow$) If
$V(z) = u\,w^\infty$ as above, then $V(T^\ell(z)) = w^\infty = V(T^{\ell+K}(z))$ (both
are the $\ell$-shift resp. $(\ell{+}K)$-shift of $V(z)$, and $w^\infty$ is
$K$-periodic), so by injectivity of $V$ (part (i)), $T^{\ell+K}(z) = T^\ell(z)$.
$\blacksquare$

**Lemma D (divergence dichotomy on $\mathbb{Z}^+$; used by Q-9904's remark and
L-9904.7).** *For $n \in \mathbb{Z}^+$, exactly one of the following holds: (a) the
$T$-orbit of $n$ is eventually periodic (equivalently, $V(n)$ is eventually periodic;
equivalently the orbit is bounded), or (b) $T^k(n) \to \infty$ (divergent, D-9907), and
then $V(n)$ is not eventually periodic.*

*Proof.* The orbit stays in $\mathbb{Z}^+$ (P0 / L-9902's P0). If two iterates coincide,
$T^{k_1}(n) = T^{k_2}(n)$ with $k_1 < k_2$, the orbit is eventually periodic, hence takes
finitely many values from step $k_1$ on: bounded, and $V(n)$ is eventually periodic by
(3b). Otherwise all iterates are pairwise distinct positive integers; then for every
bound $B$ there are at most $B$ indices $k$ with $T^k(n) \le B$ (distinct values in
$\{1, \dots, B\}$), so $T^k(n) > B$ for all large $k$: $T^k(n) \to \infty$. In case (b),
$V(n)$ eventually periodic would give case (a) via (3b), contradiction. The two cases
are exclusive (a bounded orbit does not tend to $\infty$). $\blacksquare$

**Note (C/T transfer for D-9909; added in review by fable-02-v8, 2026-07-22).**
D-9909 defines "counterexample" through the map $C$ ($1 \notin O_C(n)$), while Lemma D
and the boxed remark L-9904.7 classify $T$-orbits. The transfer is the content of
L-9901.1/.5 (currently PROPOSED, under separate review); to keep this file
self-contained it is proved here in two lines. *The $T$-iterates of $n \in \mathbb{Z}^+$
are a subsequence of the $C$-iterates:* $T(m) = C(m)$ for even $m$ and $T(m) = C(C(m))$
for odd $m$ (as $C(m) = 3m+1$ is then even), so by induction every $T$-iterate is a
$C$-iterate, and the $C$-values skipped between consecutive $T$-iterates are exactly the
numbers $C(m) = 3m + 1$ at odd $m = T^i(n)$ — all even. *Hence
$1 \in O_C(n) \iff 1 \in O_T(n)$:* ($\Leftarrow$) subsequence; ($\Rightarrow$) $1$ is
odd, so it is never a skipped value, and every $C$-iterate is a $T$-iterate or a skipped
value. Consequently: a $T$-divergent $n \in \mathbb{Z}^+$ never reaches $1$ under $T$
(reaching $1$ traps the orbit in the bounded set $\{1,2\}$, contradicting
$T^k(n) \to \infty$), hence $1 \notin O_C(n)$ — a D-9909 counterexample; and a positive
integer on a nontrivial $T$-cycle (D-9908) likewise, since a $T$-cycle containing $1$
would equal the orbit of $1$, i.e. the trivial cycle $\{1, 2\}$. $\square$

**(iv) Q-9904.** Stated in full in the Statement section, labeled OPEN, with the
containment remark; nothing further is claimed, and the author deliberately records no
guess about its truth value. (One calibration, proved: by B8 the set
$\mathbb{Q} \cap \mathbb{Z}_2$ that Q-9904 quantifies over is $\mu$-null, so
measure-theoretic statements about $\mu$-generic $z$ — e.g. ergodic consequences of
L-9904.4 — say nothing about Q-9904 in either direction.)

### L-9904.6 (worked micro-examples — exact finite computations, also machine-checked)

Each item is a finite exact computation, hence proved; all are re-checked by the script.

1. **$z = 1$** (trivial cycle): $1 \to 2 \to 1$ under $T$, so
   $V(1) = (1,0)^\infty$; formula: $w = (1,0)$, $K = 2$, $a = 1$, $\rho_w = 1$
   ($\rho_1 = 1$, $\rho_2 = 3^0 \cdot 1 + 0 = 1$), $z = 1/(4 - 3) = 1$. ✓
2. **$z = -1$:** $T(-1) = (3(-1)+1)/2 = -1$, fixed point; $V(-1) = (1)^\infty$;
   formula: $K = 1$, $a = 1$, $\rho_w = 1$, $z = 1/(2-3) = -1$. ✓ (Negative because
   $2^1 < 3^1$.)
3. **$z = -5$:** $-5 \to -7 \to -10 \to -5$; $V(-5) = (1,1,0)^\infty$; formula:
   $\rho_{(1,1,0)} = 5$ ($\rho_1 = 1$, $\rho_2 = 3 + 2 = 5$, $\rho_3 = 5$),
   $z = 5/(8 - 9) = -5$. ✓
4. **$z = -17$:** the exact $T$-orbit is the 11-cycle
   $-17 \to -25 \to -37 \to -55 \to -82 \to -41 \to -61 \to -91 \to -136 \to -68 \to
   -34 \to -17$, with parity word $w = (1,1,1,1,0,1,1,1,0,0,0)$, $K = 11$, $a = 7$.
   Closed form (L-9903.2): ones at $i = 0,1,2,3,5,6,7$ with after-counts
   $s_i = 6,5,4,3,2,1,0$:
   $\rho_w = 729 + 486 + 324 + 216 + 288 + 192 + 128 = 2363$, and indeed
   $(-17)(2^{11} - 3^7) = (-17)(-139) = 2363$, so the formula recovers
   $z = 2363/(-139) = -17$. ✓ (Negative because $2^{11} = 2048 < 2187 = 3^7$.
   Cross-check: L-9905's Adversarial tests found the same object as the negative
   $S$-cycle through $-17$ with $m = 7$, $K = 11$ — consistent.)
5. **$z = 1/5$** (non-obvious rational, purely periodic): $1/5$ is odd (B7:
   numerator odd), and exactly $1/5 \to 4/5 \to 2/5 \to 1/5$:
   $T(1/5) = (3/5 + 1)/2 = 4/5$ (even, $\nu_2 = 2$), $T(4/5) = 2/5$ (even),
   $T(2/5) = 1/5$. So $V(1/5) = (1,0,0)^\infty$; formula: $\rho_{(1,0,0)} = 1$,
   $z = 1/(2^3 - 3^1) = 1/5$. ✓
6. **$z = 1/3$** (eventually periodic, not purely): $1/3$ odd,
   $T(1/3) = (3 \cdot \tfrac13 + 1)/2 = 1$, so $V(1/3) = (1) \,(1,0)^\infty$ —
   preperiod length $1$, then the trivial cycle. ✓ Similarly $1/7 \to 5/7$ and $5/7$ is
   $4$-periodic ($5/7 \to 11/7 \to 20/7 \to 10/7 \to 5/7$), $V(1/7) = (1)(1,1,0,0)^\infty$,
   with $5/7 = 5/(2^4 - 3^2)$ from $w = (1,1,0,0)$, $\rho_w = 5$. ✓
7. **Values of $Q$:** $Q(0) = 0$ and $Q(-1) = \sum_{i \ge 0} 2^i = -1$ (geometric:
   $(1 - 2)\sum_{i < k} 2^i = 1 - 2^k \to 1$, so the sum is $(1-2)^{-1} = -1$);
   $Q(1) = \sum_{i \ge 0} 4^i = (1 - 4)^{-1} = -\tfrac13$ (word $(1,0)^\infty$; same
   geometric argument, $|4|_2 < 1$); $Q(2)$: directly, word
   $(0,1)^\infty$ gives $Q(2) = \sum 2^{2i+1} = 2 \cdot (-\tfrac13) = -\tfrac23$; and
   $\sigma(Q(1)) = (-\tfrac13 - 1)/2 = -\tfrac23 = Q(T(1))$, illustrating L-9904.4. ✓

### L-9904.7 — the obstruction remark (the file's chief service)

> ### **The exact integrality obstruction**
>
> **Every infinite parity word is realized in $\mathbb{Z}_2$, for free.** By
> L-9904.5(i) (equivalently L-9904.3(2)), for every $b \in \{0,1\}^\infty$ — however
> exotic: feedback-defined, substitution-generated, non-eventually-periodic by
> construction, tuned for any prescribed symbolic drift — there is **exactly one**
> $z_b \in \mathbb{Z}_2$ whose parity word is $b$, obtained constructively as the
> unique point of the nested residue balls $\pi_k^{-1}(b_0 \cdots b_{k-1})$
> (L-9904.2). By L-9904.4 its $T$-dynamics is *faithfully* the shift on $b$: nothing
> about the symbolic behavior is lost or approximated.
>
> **Therefore the entire content of any symbolic counterexample construction is one
> statement:** $\;z_b \in \mathbb{Z}^+$ (integrality **and** positivity).
> Precisely:
> - if $b$ is **not eventually periodic** and $z_b \in \mathbb{Z}^+$, then by Lemma D
>   the orbit of $z_b$ diverges — a counterexample of divergence type (D-9909, via the
>   C/T-transfer Note after Lemma D);
> - if $b = u w^\infty$ is **eventually periodic**, then $z_b$ is the explicit rational
>   reachable from the periodic realizer $z_w := \rho_w/(2^K - 3^{|w|_1})$ by $|u|$
>   inverse steps (L-9904.5(ii)–(iii)), and $z_b$ is a counterexample **iff**
>   $z_b \in \mathbb{Z}^+$ *and* $z_w \notin \{1, 2\}$ (equivalently: the tail
>   $w^\infty$ is not a shift of $(1,0)^\infty$) — then $z_b$'s orbit enters the
>   nontrivial $T$-cycle through $z_w$ and never meets $1$. [Sharpened in review
>   2026-07-22: the earlier wording "iff that rational is a positive integer
>   $\notin\{$trivial-cycle orbit$\}$" was ambiguous, and reading "that rational" as
>   $z_b$ makes it false — $z_b = 4 \in \mathbb{Z}^+\setminus\{1,2\}$ has eventually
>   periodic word $(0,0)(1,0)^\infty$ yet reaches $1$. Note also: $z_w \in
>   \mathbb{Z}^+ \setminus \{1,2\}$ *alone* would already exhibit a counterexample,
>   namely $z_w$ itself on a nontrivial $T$-cycle, whether or not
>   $z_b \in \mathbb{Z}^+$.] This is the nontrivial-cycle route, whose Diophantine
>   side is L-9905.
>
> **What cannot substitute for integrality.** (a) *Finite prefixes:* every finite
> prefix of $b$ is realized by an infinite arithmetic progression of positive integers
> (L-9902.3(i) / L-9904.2), yet the inverse limit of those progressions is exactly the
> single point $z_b$, integer or not — finite realizability never produces the integer
> (this repeats, now with the limit object identified, the warning in L-9902's Gap
> audit). (b) *Density:* $\mathbb{Z}^+$ is dense in $\mathbb{Z}_2$, so approximate
> realizers exist for every $b$; density arguments cannot separate
> $z_b \in \mathbb{Z}^+$ from $z_b \notin \mathbb{Z}^+$. (c) *Measure:*
> $\mathbb{Z}^+$ (indeed all of $\mathbb{Q} \cap \mathbb{Z}_2$) is $\mu$-null (B8),
> and $Q$ is measure-preserving (L-9904.3(3)), so "random-word" or ergodic arguments
> concern $\mu$-a.e. $z$ and say nothing about membership in the null set
> $\mathbb{Z}^+$.
>
> **Cross-references.** Issue #21's foundry theorem T-9601 is this realization
> mechanism specialized to feedback-defined words; its "integrality frontier" is
> exactly the statement $z_b \in \mathbb{Z}^+$ above. Issue #4's amplifier M1 and
> issue #10's sanctuary face the same obstruction in the form "does the invariant
> object contain a positive integer". Established by: L-9904.2 ($\pi_k$), L-9904.3
> ($Q$ bijective isometry, measure), L-9904.4 (faithful dynamics), L-9904.5(i)–(iii)
> (realization, explicit periodic realizers), Lemma D (divergence dichotomy).

---

## Dependency audit

| Dependency | Status | Where used |
|---|---|---|
| D-9902 (shortcut $T$ on $\mathbb{Z}^+$) | canonical | P0 (restriction compatibility); boxed contrast in L-9904.1. |
| D-9906 ($v_i$, $a_k$; explicitly allows $\mathbb{Z}_2$) | canonical | throughout; $a_{k+1} = a_k + v_k$ in L-9904.2 and Lemma A. |
| NOTATION.md conventions (empty sums; statuses) | canonical | $a_0 = 0$; status discipline. |
| L-9902 (PROPOSED, under review) | cited, not load-bearing | Z$^+$ counterpart of L-9904.2; its P0 cited in Lemma D (re-derivable from P0 here); compatibility remark. All $\mathbb{Z}_2$ claims re-proved inline, so no proof here *depends* on L-9902; overlap noted per packet convention. |
| L-9903 (PROPOSED, under review) | load-bearing for .5(ii) | word-level $\rho$: definition and closed form (L-9903.2) and bounds/positivity (L-9903.3) used as **word-level** (domain-free) facts; the iteration formula L-9903.1 is **re-derived over $\mathbb{Z}_2$** as Lemma A rather than imported. |
| L-9905 (PROPOSED, in progress) | cross-reference only | consistency remarks in .5(ii) and L-9904.6.4 (positivity threshold; $-17$); **no logical dependence**, no circularity (L-9905 does not cite this file). |
| L-9901 (PROPOSED, under review) | cross-reference only (row added in review 2026-07-22) | the C/T transfer used by the D-9909 phrasing in the Q-9904 remark and L-9904.7 is L-9901.1/.5's content, but is **re-proved inline** in the Note after Lemma D, so no proof here depends on L-9901; no circularity (L-9901 does not cite this file). |
| B1, B5, B6; existence half of B8 | **imported standard facts** | construction/completeness of $\mathbb{Z}_2$; existence of the ball-measure (Haar / product measure). Flagged here and in Gap audit. |
| Dynkin $\pi$–$\lambda$ theorem | imported standard fact | Lemma U only. |
| B2–B4, B7, uniqueness half of B8 | proved/justified inline | valuation algebra, units, balls, $\mathbb{Q} \cap \mathbb{Z}_2 = \mathbb{Z}_{(2)}$, Lemma U. |

No result of this file is used by any of its own dependencies: no circularity.
Nothing assumes the Collatz conjecture or its negation; Q-9904 is quantified as a
question, never as a hypothesis.

## Gap audit

- **Hand-waved topology/measure (this file's flagged chief risk):** deliberately
  eliminated. Surjectivity of $Q$ is a nested-ball/completeness argument (B5) with the
  nesting proved, not asserted; measure preservation goes through Lemma M (balls to
  balls, both directions, via the inverse isometry) and Lemma U ($\pi$–$\lambda$
  uniqueness on an explicitly verified $\pi$-system with an explicitly verified
  generating property). The only measure-theoretic import is the *existence* of $\mu$
  and the $\pi$–$\lambda$ theorem, both standard and flagged.
- **Hidden finiteness assumptions:** the only passage from finite to infinite is
  B5/inverse-limit in L-9904.3(2), stated and proved as such. L-9904.7 explicitly warns
  against the finite-prefix fallacy rather than committing it.
- **Unjustified induction:** the inductions (L-9904.2 iterated; Lemma A; downward
  induction in .5(iii)) have explicit bases and steps; the downward induction is over a
  finite range $\ell, \dots, 0$.
- **Boundary cases:** $j \ge 1$ required in one-step locality (and used: $2^j m$ even);
  $i = k$ excluded from bit preservation (the increment $3^{a_k} m$ need not be even);
  $k = 0$: $\pi_0$ trivial bijection onto $\{()\}$; $a = 0$ and $a = K$ in .5(ii)
  ($z = 0$, resp. $2^K - 3^K < 0$ for $K \ge 2$ and $= -1$ for $K = 1$); $\ell = 0$
  (purely periodic) in .5(iii); $w$ over-periodic (e.g. $w = (1,0,1,0)$ vs $(1,0)$)
  is consistent: both give the same $z$ (the equation for the longer word is implied by
  the shorter one's; uniqueness in (i) forces agreement).
- **Confusion of domains:** word-level facts (L-9903.2/.3) are used only as
  combinatorial statements about words; every statement about $\mathbb{Z}_2$ elements
  is proved over $\mathbb{Z}_2$ (P0, L-9904.1–.4, Lemma A). Lemma D is stated and used
  **only** for $n \in \mathbb{Z}^+$ (its pigeonhole needs positivity and integrality);
  no analogue is claimed for rationals or for $\mathbb{Z}_2$.
- **Circular dependence:** none (see audit table). In particular Q-9904's remark does
  not use Q-9904.
- **Assumptions equivalent to Collatz:** none. Q-9904 is labeled OPEN; the file proves
  only the containment relations around it, each direction stated conditionally.
- **Empirical vs universal:** the Adversarial tests are labeled finite verification;
  no proof cites them. Truncation-based tests inspect only finitely many digits; this
  limitation is stated there.
- **Symbolic object vs integer trajectory:** the file's central point (L-9904.7) is
  precisely to make this distinction exact; nothing here claims any $z_b$ is a positive
  integer.

## Adversarial tests

**Finite verification only — not proof.** Exact arithmetic throughout: Python integers
and `fractions.Fraction` restricted to odd denominators (i.e. elements of
$\mathbb{Z}_{(2)} \subset \mathbb{Z}_2$; the parity of $p/q$, $q$ odd, is $p \bmod 2$
by B7, which the code uses). 2-adic elements are exercised through integers of both
signs, odd-denominator rationals, and residues/truncations mod $2^{60}$ — finitely many
digits, as flagged in the Gap audit. Script:
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/verify_L9904.py`,
run with `python3 verify_L9904.py` (Python 3, stdlib only; fixed seed 99042026;
runtime ~3 s). Reproduced in full:

```python
#!/usr/bin/env python3
# Adversarial finite verification for L-9904 (2-adic extension and shift conjugacy).
# Agent: fable-02-p3. Date: 2026-07-21.
# Exact arithmetic only: Python ints and fractions.Fraction (odd denominators = Z_(2)).
#
# Tests:
#  A. one-step locality T(z + 2^j m) = T(z) + 3^{v0(z)} 2^{j-1} m  (ints & rationals, signs)
#  B. iterated locality + bit preservation, k <= 40 (ints & rationals)
#  B'. residue-determinacy: word depends only on z mod 2^60 (integer and rational lifts)
#  C. conjugacy v_i(T z) = v_{i+1}(z) and truncated Q-arithmetic Q_59(Tz) = (Q_60(z)-b0)/2
#  D. isometry: ALL pairs of residues mod 2^12 (exhaustive), plus per-level
#     bijectivity and exact ball-preimage counts (finite shadow of measure preservation);
#     random large-scale isometry checks at 60-bit truncation
#  E. periodic-point formula z_w = rho_w/(2^K - 3^a) for ALL words of length K <= 6:
#     denominator odd (2-adic unit), T^K(z_w) = z_w exactly, parity word = w^infty
#     through 42 bits, injectivity per length, anchor values
#  F. the -17 cycle: word, K=11, a=7, rho=2363, formula recovers -17
#  G. rationals 1/3, 1/5, 1/7: exact orbits, eventual periodicity, match with .5(ii)
#  H. preimage structure: T(2w) = w, T((2w-1)/3) = w with (2w-1)/3 odd; over Z+ the
#     odd preimage is integral exactly for w = 2 mod 3
#  I. Q anchor values: Q(0)=0, Q(-1)=-1, Q(1)=-1/3, Q(2)=-2/3 (truncations mod 2^60)

from fractions import Fraction
from itertools import product
import random

random.seed(99042026)

def par(x):
    if isinstance(x, int):
        return x % 2
    assert x.denominator % 2 == 1, x   # stays inside Z_(2) = Q cap Z_2
    return x.numerator % 2

def T(x):
    if isinstance(x, int):
        return x // 2 if x % 2 == 0 else (3 * x + 1) // 2
    y = x / 2 if par(x) == 0 else (3 * x + 1) / 2
    assert y.denominator % 2 == 1, x   # T preserves odd denominators
    return y

def word(x, k):
    w = []
    for _ in range(k):
        w.append(par(x))
        x = T(x)
    return tuple(w)

def Qtrunc(x, k):
    return sum(b << i for i, b in enumerate(word(x, k)))

def v2i(n):
    assert n != 0
    return (n & -n).bit_length() - 1

def v2(x):
    if isinstance(x, int):
        return v2i(x)
    return v2i(x.numerator) - v2i(x.denominator)

def rho_rec(w):
    r = 0
    for i, wi in enumerate(w):
        r = (3 ** wi) * r + wi * (2 ** i)
    return r

def rho_closed(w):
    return sum((3 ** sum(w[i+1:])) * (2 ** i) for i in range(len(w)) if w[i] == 1)

def rand_frac():
    return Fraction(random.randint(-10**9, 10**9), 2 * random.randint(0, 499) + 1)

def rand_elt():
    return random.choice([random.randint(-10**12, 10**12), rand_frac()])

# ---------------- A. one-step locality ----------------
nA = 0
for _ in range(4000):
    z, m = rand_elt(), rand_elt()
    j = random.randint(1, 50)
    lhs = T(z + 2**j * m)
    rhs = T(z) + 3**par(z) * 2**(j - 1) * m
    assert lhs == rhs, (z, j, m)
    nA += 1
print(f"A: one-step locality exact on {nA} random (z, j, m), ints and odd-denominator rationals, both signs.")

# ---------------- B. iterated locality ----------------
nB = 0
for _ in range(400):
    z, m = rand_elt(), rand_elt()
    k = random.randint(0, 40)
    x, y = z, z + 2**k * m
    aa = 0
    for i in range(k + 1):
        assert y == x + 3**aa * 2**(k - i) * m, (z, k, m, i)
        if i < k:
            assert par(y) == par(x), (z, k, m, i)
        if i < k:
            aa += par(x)
            x, y = T(x), T(y)
    nB += 1
print(f"B: iterated locality T^i(z+2^k m) = T^i(z) + 3^(a_i) 2^(k-i) m, i<=k<=40: {nB} random cases.")

# ---------------- B'. residue-determinacy mod 2^60 ----------------
for _ in range(300):
    r = random.randint(0, 2**60 - 1)
    t = random.choice([random.randint(-10**9, 10**9), rand_frac()])
    assert word(r, 60) == word(r + 2**60 * t, 60), (r, t)
print("B': length-60 parity word depends only on the residue mod 2^60 (300 random integer and rational lifts).")

# ---------------- C. conjugacy ----------------
for _ in range(300):
    z = rand_elt()
    w61 = word(z, 61)
    assert word(T(z), 60) == w61[1:], z                       # v_i(Tz) = v_{i+1}(z)
    q61 = sum(b << i for i, b in enumerate(w61))
    assert Qtrunc(T(z), 60) == (q61 - (q61 & 1)) >> 1, z      # Q(Tz) = sigma(Q z) truncated
print("C: conjugacy v_i(Tz) = v_(i+1)(z) and truncated Q(Tz) = sigma(Q(z)) on 300 random elements.")

# ---------------- D. isometry, exhaustive mod 2^12 ----------------
KD = 12
W = [Qtrunc(x, KD) for x in range(2**KD)]
pairs = 0
for x in range(2**KD):
    Wx, dx = W[x], x
    for y in range(x + 1, 2**KD):
        d1 = dx - y
        d2 = Wx - W[y]
        assert (d1 & -d1) == (d2 & -d2), (x, y)   # v2 equality via lowest set bit
        pairs += 1
print(f"D1: isometry |Q(x)-Q(y)|_2 = |x-y|_2 exhaustively on all {pairs} pairs of residues mod 2^{KD}.")

for j in range(KD + 1):
    level = {}
    for x in range(2**KD):
        r, q = x % 2**j, W[x] % 2**j
        assert level.setdefault(r, q) == q, (j, x)   # Q mod 2^j well-defined on x mod 2^j
    assert len(set(level.values())) == 2**j, j       # and bijective at level j
    counts = {}
    for x in range(2**KD):
        counts[W[x] % 2**j] = counts.get(W[x] % 2**j, 0) + 1
    assert all(c == 2**(KD - j) for c in counts.values()), j  # ball preimages have exact size
print(f"D2: for every level j <= {KD}: Q induces a bijection mod 2^j and every ball's preimage has exactly 2^({KD}-j) residues (measure shadow).")

for _ in range(300):
    z = rand_elt()
    jj = random.randint(0, 55)
    u = random.choice([1, -1, 3, -3, 5]) * (2 * random.randint(0, 10**6) + 1)
    zp = z + 2**jj * Fraction(u, 2 * random.randint(0, 200) + 1)
    d = Fraction(z) - Fraction(zp)
    dq = Qtrunc(z, 60) - Qtrunc(zp, 60)
    assert v2(d) == jj and v2i(dq) == jj, (z, jj)
print("D3: isometry at 60-bit truncation on 300 random pairs with prescribed v2 (ints and rationals).")

# ---------------- E. periodic-point formula, all |w| <= 6 ----------------
total_words = 0
for K in range(1, 7):
    zs = set()
    for w in product((0, 1), repeat=K):
        a = sum(w)
        rho = rho_rec(w)
        assert rho == rho_closed(w), w
        D = 2**K - 3**a
        assert D % 2 == 1 and D != 0, w               # odd => 2-adic unit
        z = Fraction(rho, D)
        assert z.denominator % 2 == 1, w              # z in Z_(2) subset Z_2
        x = z
        for _ in range(K):
            x = T(x)
        assert x == z, w                              # T^K(z_w) = z_w exactly
        reps = (42 // K) + 1
        assert word(z, 42) == (w * reps)[:42], w      # parity word is w^infty (42 bits)
        zs.add(z)
        total_words += 1
    assert len(zs) == 2**K, K                         # distinct words, distinct realizers
anchors = {(1, 0): Fraction(1), (1,): Fraction(-1), (1, 1, 0): Fraction(-5),
           (1, 0, 0): Fraction(1, 5), (0,): Fraction(0), (1, 1, 0, 0): Fraction(5, 7)}
for w, zexp in anchors.items():
    assert Fraction(rho_rec(w), 2**len(w) - 3**sum(w)) == zexp, w
print(f"E: periodic-point formula z_w = rho_w/(2^K-3^a) verified for all {total_words} words with 1 <= K <= 6"
      " (unit denominator, exact fixed point, 42-bit word check, per-length injectivity);"
      " anchors (1,0)->1, (1)->-1, (1,1,0)->-5, (1,0,0)->1/5, (0)->0, (1,1,0,0)->5/7.")

# ---------------- F. the -17 cycle ----------------
orbit = [-17]
while True:
    nxt = T(orbit[-1])
    if nxt == orbit[0]:
        break
    orbit.append(nxt)
K17 = len(orbit)
w17 = tuple(x % 2 for x in orbit)
a17 = sum(w17)
rho17 = rho_rec(w17)
assert K17 == 11 and w17 == (1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0) and a17 == 7
assert rho17 == rho_closed(w17) == 2363
assert (-17) * (2**11 - 3**7) == rho17               # cycle equation in T-form
assert Fraction(rho17, 2**11 - 3**7) == -17          # .5(ii) recovers -17
assert word(-17, 44) == (w17 * 4)
print(f"F: T-orbit of -17: cycle length K=11, word {w17}, a=7, rho=2363;"
      " -17 = 2363/(2^11-3^7) = 2363/(-139). Consistent with L-9905's S-cycle (m=7, K=11).")

# ---------------- G. rationals 1/3, 1/5, 1/7 ----------------
assert T(Fraction(1, 3)) == 1
assert word(Fraction(1, 3), 41) == (1,) + word(1, 40)
x = Fraction(1, 5)
assert T(T(T(x))) == x
assert word(x, 42) == ((1, 0, 0) * 14)
assert Fraction(rho_rec((1, 0, 0)), 2**3 - 3**1) == Fraction(1, 5)
y = T(Fraction(1, 7))
assert y == Fraction(5, 7)
assert T(T(T(T(y)))) == y
assert word(Fraction(1, 7), 41) == (1,) + ((1, 1, 0, 0) * 10)
assert Fraction(rho_rec((1, 1, 0, 0)), 2**4 - 3**2) == Fraction(5, 7)
print("G: 1/3 -> 1 (word (1)+(1,0)^inf); 1/5 is 3-periodic, word (1,0,0)^inf, = rho/(8-3);"
      " 1/7 -> 5/7, 4-periodic tail (1,1,0,0)^inf with 5/7 = 5/(16-9). All exact.")

# ---------------- H. preimage structure ----------------
for _ in range(2000):
    w = rand_elt()
    assert T(2 * w) == w
    z1 = (2 * Fraction(w) - 1) / 3
    assert z1.denominator % 2 == 1 and par(z1) == 1
    assert T(z1) == Fraction(w)
good = [w for w in range(1, 3001) if (2 * w - 1) % 3 == 0]
assert good == [w for w in range(1, 3001) if w % 3 == 2]
print(f"H: both 2-adic preimages verified on 2000 random w (2w even, (2w-1)/3 odd, both map to w);"
      f" over Z+ the odd preimage is integral exactly for w = 2 (mod 3): {len(good)} of 3000 values.")

# ---------------- I. Q anchor values ----------------
M = 2**60
assert Qtrunc(0, 60) == 0
assert Qtrunc(-1, 60) % M == (-1) % M                       # Q(-1) = -1
assert (3 * Qtrunc(1, 60)) % M == (-1) % M                  # Q(1) = -1/3
assert (3 * Qtrunc(2, 60)) % M == (-2) % M                  # Q(2) = -2/3
q1, q2 = Qtrunc(1, 61), Qtrunc(2, 60)
assert ((q1 - (q1 & 1)) >> 1) % M == q2 % M                 # sigma(Q(1)) = Q(T(1)) = Q(2)
print("I: Q(0)=0, Q(-1)=-1, Q(1)=-1/3, Q(2)=-2/3 (all mod 2^60), and sigma(Q(1)) = Q(2).")

print("ALL CHECKS PASSED")
```

**Output (verbatim, single run, 2026-07-21, CPython 3, Linux; runtime 3.3 s):**

```text
A: one-step locality exact on 4000 random (z, j, m), ints and odd-denominator rationals, both signs.
B: iterated locality T^i(z+2^k m) = T^i(z) + 3^(a_i) 2^(k-i) m, i<=k<=40: 400 random cases.
B': length-60 parity word depends only on the residue mod 2^60 (300 random integer and rational lifts).
C: conjugacy v_i(Tz) = v_(i+1)(z) and truncated Q(Tz) = sigma(Q(z)) on 300 random elements.
D1: isometry |Q(x)-Q(y)|_2 = |x-y|_2 exhaustively on all 8386560 pairs of residues mod 2^12.
D2: for every level j <= 12: Q induces a bijection mod 2^j and every ball's preimage has exactly 2^(12-j) residues (measure shadow).
D3: isometry at 60-bit truncation on 300 random pairs with prescribed v2 (ints and rationals).
E: periodic-point formula z_w = rho_w/(2^K-3^a) verified for all 126 words with 1 <= K <= 6 (unit denominator, exact fixed point, 42-bit word check, per-length injectivity); anchors (1,0)->1, (1)->-1, (1,1,0)->-5, (1,0,0)->1/5, (0)->0, (1,1,0,0)->5/7.
F: T-orbit of -17: cycle length K=11, word (1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0), a=7, rho=2363; -17 = 2363/(2^11-3^7) = 2363/(-139). Consistent with L-9905's S-cycle (m=7, K=11).
G: 1/3 -> 1 (word (1)+(1,0)^inf); 1/5 is 3-periodic, word (1,0,0)^inf, = rho/(8-3); 1/7 -> 5/7, 4-periodic tail (1,1,0,0)^inf with 5/7 = 5/(16-9). All exact.
H: both 2-adic preimages verified on 2000 random w (2w even, (2w-1)/3 odd, both map to w); over Z+ the odd preimage is integral exactly for w = 2 (mod 3): 1000 of 3000 values.
I: Q(0)=0, Q(-1)=-1, Q(1)=-1/3, Q(2)=-2/3 (all mod 2^60), and sigma(Q(1)) = Q(2).
ALL CHECKS PASSED
```

What the tests attack, and their limits: A/B/B′ target the exact coefficients and the
$j \ge 1$ / $i \le k-1$ boundary structure of L-9904.2, on integers of both signs *and*
genuinely non-integer elements of $\mathbb{Z}_{(2)}$; D1 is the isometry checked on
**all** $8{,}386{,}560$ pairs mod $2^{12}$ (an off-by-one in the flip position would
fail on the first sweep); D2 is the finite shadow of measure preservation (exact ball
preimage counts at every level); E attacks .5(ii) on **all** 126 words of length
$\le 6$, including $a = 0$, $a = K$, and both signs of $2^K - 3^a$, with the parity word
of the resulting rational re-computed by exact iteration through 42 bits; F/G are the
required anchors. Limits: only finitely many digits and finitely many elements are ever
inspected; irrational elements of $\mathbb{Z}_2$ are exercised only through their
residues; none of this bears on Q-9904.

**No corrections were needed:** every statement in the assignment checked out as given
(the only sharpenings made are explicit hypotheses: $j \ge 1$ in locality, $K \ge 1$ in
.5(ii), and the restriction of Lemma D to $\mathbb{Z}^+$).

## Remaining uncertainty

- All of L-9904.1–.7 and Lemmas A, D, M, U are, in the author's assessment, fully
  proved from B1–B8; no PARTIAL or CONJECTURED labels are needed. Q-9904 is OPEN by
  design and carries no claim.
- The imports to probe: (1) B8 existence of the ball-measure — standard (Haar on a
  compact group / Bernoulli product measure), but it is an import, and a reviewer should
  confirm the file never uses more of it than existence plus the ball values;
  (2) the $\pi$–$\lambda$ theorem in Lemma U.
- Proof spots a verifier should press hardest: the surjectivity nesting step in
  L-9904.3(2) (that $r_{k+1} \subseteq r_k$ genuinely follows from $\pi_k$-injectivity);
  the valuation bookkeeping in the isometry (that the tail $t$ lies in $\mathbb{Z}_2$
  and the bracket is a unit — B6/B3); the two-ball preimage computation in L-9904.4b
  (both inclusions for the odd ball); and the parity claim $b_0(p/q) = p \bmod 2$ for
  odd $q$ (B7), which the test code relies on throughout.
- The task statement's phrase "$z > 0$ in $\mathbb{Z}$-terms iff $2^K > 3^a$" is proved
  here **for $a \ge 1$** (for $a = 0$, $z = 0$); this is a completion of a boundary
  case, not a correction.
- Status is PROPOSED; only an independent reviewing agent may upgrade.

## Suggested next attack

1. **Review to PROVED:** reconstruct L-9904.3 from scratch (it is the riskiest part by
   design); independently re-derive the isometry from L-9902.2's flip structure as a
   cross-check; verify Lemma U against a textbook statement of $\pi$–$\lambda$.
2. **Consume downstream:** issue #21's T-9601 should cite L-9904.5(i) and L-9904.7
   instead of re-deriving realization; #4/#10/#18 can now state their integrality
   frontiers as "$z_b \in \mathbb{Z}^+$" with a citation; the #15/#16 measure side
   gets L-9904.3(3)/.4b as its dictionary.
3. **Attack the obstruction where it is thinnest:** L-9904.7(a) shows finite prefixes
   determine nested arithmetic progressions of positive integers converging to $z_b$;
   the open territory is *quantitative*: how fast can the least positive representative
   of $\pi_k^{-1}(b_0 \dots b_{k-1})$ grow, relative to $2^k$, for words $b$ engineered
   to keep it small? A word family whose least representatives are $o(2^k)$ **and**
   stabilize infinitely often would be exactly a divergence candidate. Making this
   precise (and probably refuting naive versions) is a natural L-9911.
4. **Q-9904 structure theory:** for fixed odd denominator $q$, $T$ maps
   $\{p/q\} \cap \mathbb{Z}_2$ to itself (denominators divide $q$); the induced map on
   numerators mod $q$-classes is a finite-data object; classifying eventual periodicity
   for small $q$ (e.g. $q \le 25$) is a well-posed finite-flavored subproblem and would
   calibrate Q-9904 (note $q = 1$ is the full Collatz divergence half — do **not**
   expect closure there).

---

*Signed: fable-02-p3, 2026-07-21. Finite verification script `verify_L9904.py`
(scratchpad; full text and output above).*

---

## Verification note (fable-02-v8, 2026-07-22)

**Verdict: PASS (with two remark-level fixes, documented below).** Independent
adversarial review per README §13, performed without relying on the author's
confidence and without consulting the author's script for implementation. Status
upgraded PROPOSED → PROVED. Not INDEPENDENTLY_VERIFIED — per this packet's
convention that upgrade is reserved for a further cross-session review. **No gap was
found in any numbered claim: L-9904.1–.6, Lemmas A, D, M, U, P0, and the inline
justifications B2–B4, B7 and Lemma U (uniqueness half of B8) are all correct as
stated.** The two fixes are confined to remark-level text (the L-9904.7 box and the
Q-9904 containment remark); no statement or proof of a numbered claim was changed.

### 1. Independent reconstruction (all proofs re-derived before re-reading the author's)

- **L-9904.1.** Well-definedness: both branches land in $\mathbb{Z}_2$ ($z/2$ unique
  by the integral-domain property; $3z$ odd for odd $z$ since odd·odd = odd, so
  $3z+1$ even). Continuity: $T$ is affine on each of the two clopen balls
  $2\mathbb{Z}_2$, $1 + 2\mathbb{Z}_2$ with exact 2-adic Lipschitz constant $2$ on
  each ($|1/2|_2 = 2$, $|3/2|_2 = 2$); a map continuous on each member of a finite
  clopen cover is continuous. Exactly 2-to-1: the case split $z$ even / odd is
  exhaustive and each case forces $z = 2w$ resp. $z = (2w-1)\cdot 3^{-1}$ (division
  by the unit $3$ is unique); $(2w-1)/3$ exists in $\mathbb{Z}_2$ for **every** $w$
  because $3 \in \mathbb{Z}_2^\times$, is odd (odd·odd), and $2w$ is even, so the two
  preimages always exist and are always distinct. Sound.
- **L-9904.2.** One-step and iterated locality re-derived (the $j \ge 1$ hypothesis
  is used exactly where needed: $2^j m$ even and $2^{j-1} m \in \mathbb{Z}_2$); the
  induction's bit-preservation stops at $i = k-1$ because the $i = k$ increment
  $3^{a_k} m$ can be odd — correctly excluded. Injectivity: $j := \nu_2(z - z') \le
  k-1$, $u := (z-z')/2^j$ a unit, and the $(k,i) = (j,j)$ instance gives an odd orbit
  increment $3^{a_j(z')} u$ at step $j$, flipping $v_j$; the $j = 0$ edge is covered
  by the $k = 0$ base alone. Surjectivity: finite counting via $|\mathbb{Z}_2 /
  2^k\mathbb{Z}_2| = 2^k$ (B4). The route is genuinely direct over $\mathbb{Z}_2$ —
  no density transfer from $\mathbb{Z}^+$ is used anywhere. Sound.
- **L-9904.3(1) isometry — pressure point checked.** With $j = \nu_2(z - z')$: bits
  $< j$ agree (locality), bit $j$ flips (injectivity computation at $k = j+1$), and
  the tail $t = \sum_{i > j} (v_i(z) - v_i(z'))\, 2^{i-j-1}$ converges in
  $\mathbb{Z}_2$ by B6 (coefficients in $\{-1,0,1\}$); the bracket $\pm 1 + 2t$ is
  odd, hence a unit, so $\nu_2(Q(z) - Q(z')) = j$ exactly. Sound, including $j = 0$.
- **L-9904.3(2) surjectivity — the author-flagged riskiest step.** The nesting
  $r_{k+1} \subseteq r_k$ **does** follow from injectivity of $\pi_k$: a point of
  $r_{k+1}$ has length-$(k{+}1)$ word $(b_0,\dots,b_k)$, hence length-$k$ word
  $(b_0,\dots,b_{k-1})$, and $r_k$ is *the unique* class with that word. B5
  (completeness / nested closed balls with radii $\to 0$) then yields exactly one
  point $z^*$, and $z^* \in r_k$ for every $k$ pins every bit of $V(z^*)$. Airtight;
  this is a legitimate inverse-limit argument with the compatibility proved, not
  asserted.
- **L-9904.3(3) measure — pressure point checked.** Lemma M genuinely needs
  bijectivity (the reverse inclusion comes from the inverse isometry) — used
  correctly. Lemma U checked against the $\pi$–$\lambda$ theorem: the balls plus
  $\emptyset$ form a $\pi$-system (nested-or-disjoint, B4) containing the whole
  space; countably many balls form a base, so they generate the Borel
  $\sigma$-algebra; two probability measures agreeing there agree on Borel. The two
  set functions $A \mapsto \mu(Q^{-1}A)$, $A \mapsto \mu(QA)$ are Borel probability
  measures because $Q$ is a homeomorphism ($QA = (Q^{-1})^{-1}(A)$). Only existence
  + ball values of $\mu$ are ever used from B8 — confirmed by a pass over every use
  of $\mu$ in the file. Sound.
- **L-9904.4 / .4b — pressure point checked.** $v_i(T(z)) = v_{i+1}(z)$ is
  definitional ($T^i \circ T = T^{i+1}$); B1-uniqueness converts it to
  $Q \circ T = \sigma \circ Q$. The two-ball preimage computation of .4b was redone
  from scratch, including **both** inclusions for the odd ball: $z = \tfrac{2c-1}{3}
  + 2^{k+1} t \Rightarrow T(z) = c + 3 \cdot 2^k t \in c + 2^k \mathbb{Z}_2$, and
  conversely $(3z+1)/2 \in c + 2^k\mathbb{Z}_2$ with $z$ odd forces $z \in
  \tfrac{2c-1}{3} + 2^{k+1}\mathbb{Z}_2$ (multiply out; $\tfrac13$ a unit). The two
  balls have radius $2^{-k-1}$, are disjoint by parity, so $\mu(T^{-1}B) = \mu(B)$
  on balls, and Lemma U finishes. Sound.
- **Lemma A.** Re-derived: $2T(m) = 3^{v_0(m)} m + v_0(m)$ in both branches; the
  induction matches $a_{k+1} = a_k + v_k$ and $\rho_{k+1} = 3^{v_k}\rho_k + v_k 2^k$;
  identification with L-9903.2's word-level $\rho$ is the same recursion. The
  L-9903.1 iteration formula (a $\mathbb{Z}^+$ statement) is correctly **not**
  imported — this re-proof over $\mathbb{Z}_2$ is exactly the required lifting.
- **L-9904.5(ii) — sign convention re-derived.** From Lemma A at $k = K$ and
  $T^K(z) = z$: $2^K z = 3^a z + \rho_w$, i.e. $z\,(2^K - 3^a) = \rho_w$, so
  $z = \rho_w/(2^K - 3^a)$ — the file's convention. Checked against every anchor by
  hand: $(1,0) \mapsto 1/(4-3) = 1$; $(1) \mapsto 1/(2-3) = -1$; $(1,1,0) \mapsto
  5/(8-9) = -5$; and the $-17$ orbit recomputed by hand
  ($-17 \to -25 \to -37 \to -55 \to -82 \to -41 \to -61 \to -91 \to -136 \to -68
  \to -34 \to -17$, word $(1,1,1,1,0,1,1,1,0,0,0)$, $a = 7$,
  $\rho = 729+486+324+216+288+192+128 = 2363 = (-17)(-139)$). $2^K - 3^a$ is odd
  (even − odd), nonzero, hence a unit — the division is legitimate and lands in
  $\mathbb{Q} \cap \mathbb{Z}_2 = \mathbb{Z}_{(2)}$ (B7, whose proof, including the
  parity rule $p/q \equiv p \bmod 2$ for odd $q$, I re-derived). Positivity
  threshold $z > 0 \iff 2^K > 3^a$ for $a \ge 1$ uses $\rho_w \ge 3^a - 2^a \ge 1$,
  a word-level fact of L-9903.3 (PROVED) — in scope. Consistency under
  over-periodic $w$ checked: $(1)^K \mapsto (3^K - 2^K)/(2^K - 3^K) = -1$ for all $K$.
- **L-9904.5(iii) — backward rationality re-derived.** The inverse step preserves
  rationality because the *full* preimage $\{2y, (2y-1)/3\}$ of a rational $y$ is
  rational, and membership in $\mathbb{Z}_2$ plus B7 upgrades rational to
  odd-denominator. The downward induction runs over the finite range
  $\ell, \dots, 0$. (3b) uses injectivity of $V$ — proved in (i). Sound over all of
  $\mathbb{Z}_2$.
- **Lemma D.** Pigeonhole (distinct positive integers $\le B$ number at most $B$)
  is valid exactly because the orbit lies in $\mathbb{Z}^+$ (L-9902's P0, a PROVED
  $\mathbb{Z}^+$ statement — in scope); the file correctly claims no analogue for
  rationals or $\mathbb{Z}_2$.
- **Citation-scope audit (the assigned characteristic risk).** L-9902 (PROVED):
  cited only as non-load-bearing counterpart plus its P0 for $\mathbb{Z}^+$-orbits in
  Lemma D — within proved scope. L-9903 (PROVED): only the word-level facts .2
  (closed form) and .3 (bounds/positivity), both quantified over all
  $w \in \{0,1\}^k$ with no domain reference — within proved scope; the
  domain-dependent L-9903.1 is re-proved as Lemma A. L-9905: cross-reference only,
  and the file says so. **No $\mathbb{Z}^+$ statement is silently applied to
  $\mathbb{Z}_2$.** One sourcing gap existed at remark level (Fix 2 below).
- **Q-9904 labeling.** The question is stated neutrally, labeled OPEN, with no
  direction asserted; .5(iii) proves one implication and Q-9904 is its converse. The
  relation to Collatz is stated as **containment**, not equivalence: affirmative
  ⟹ no divergent positive trajectories (it would *not* settle cycles); negative
  witness in $\mathbb{Z}^+$ ⟹ counterexample; negative witness in
  $\mathbb{Z}_{(2)} \setminus \mathbb{Z}$ settles only Q-9904. All three
  conditionals are now fully sourced (Fix 2). Correct.

### 2. Fixes made (documented; remark-level only)

1. **L-9904.7 box, second bullet (substantive).** Old text: "the construction
   yields a counterexample iff that rational is a positive integer
   $\notin \{$trivial-cycle orbit$\}$". Under the natural reading ("that rational"
   $= z_b$, trivial-cycle orbit $= \{1,2\}$) the "iff" is **false**: $z_b = 4 \in
   \mathbb{Z}^+ \setminus \{1,2\}$ realizes the eventually periodic word
   $(0,0)(1,0)^\infty$ and reaches $1$ (machine-checked, V9). Replaced by the
   precise criterion: $z_b$ is a counterexample iff $z_b \in \mathbb{Z}^+$ **and**
   the tail's periodic realizer $z_w \notin \{1,2\}$. Proof of the sharpened iff:
   ($\Leftarrow$) $z_w = T^{|u|}(z_b) \in \mathbb{Z}^+$; if $1$ appeared in the
   pre-period the orbit would be trapped in $\{1,2\}$, forcing $z_w \in \{1,2\}$;
   if $1$ appeared in the terminal cycle, that cycle would equal the cycle of $1$,
   i.e. $\{1,2\} \ni z_w$ — both contradictions; so $1 \notin O_T(z_b)$, and the
   C/T Note gives $1 \notin O_C(z_b)$. ($\Rightarrow$) a counterexample has
   $1 \notin O_T(z_b)$, while $z_w \in \{1,2\}$ would put $1$ in the orbit. The
   criterion is independent of the decomposition $b = u\,w^\infty$ chosen, since any
   two tail realizers lie on the same terminal cycle. (Also recorded in the box:
   $z_w \in \mathbb{Z}^+ \setminus \{1,2\}$ alone would already exhibit $z_w$ itself
   as a counterexample.)
2. **C/T transfer for D-9909 (substantive sourcing).** The box and the Q-9904
   remark call $T$-orbit outcomes "Collatz counterexamples (D-9909)", but D-9909 is
   phrased for the map $C$, and the bridge ($1 \in O_C(n) \iff 1 \in O_T(n)$) was
   neither proved in-file nor cited — it is L-9901.1/.5's content, and L-9901 is
   only PROPOSED. Added a self-contained two-line proof as the **Note (C/T
   transfer)** after Lemma D ($T$-iterates are a subsequence of $C$-iterates; the
   skipped values $3m+1$, $m$ odd, are all even, and $1$ is odd), pointers at the
   two usage sites, and an L-9901 cross-reference row in the Dependency audit. The
   file now has no dependence, even remark-level, on unreviewed material.
3. **Cosmetic.** Dangling fragment "$Q(2) = 2 Q(1) \cdot$ —" in L-9904.6.7 repaired
   to introduce the direct computation (no content change). Header updated (Status,
   Reviewing agents, Last updated).

The Statement-section headline of L-9904.7 ("…exactly equivalent to proving that its
unique 2-adic realizer is a **positive integer**") is retained as the correct slogan
for the divergence route and for any construction whose tail is not the trivial
word; the fixed box bullet now carries the precise cycle-route criterion.

### 3. Independent computational refutation attempt (finite verification, not proof)

Script written from the statements alone (author's `verify_L9904.py` not consulted;
different implementation structure, different seed), exact arithmetic only
(Python ints and `fractions.Fraction` with odd denominators; parity of $p/q$ via
$p \bmod 2$ per B7):
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/refute_L9904_v8.py`,
`python3 refute_L9904_v8.py`, seed 20260722, runtime ≈ 4.0 s. Coverage beyond the
author's tests: Lemma A checked *along the orbit* of every periodic realizer and on
random rationals/negative integers to $k \le 40$; the cycle-equation **iff** on 400
random elements; the fresh eventually-periodic example $7/5$ (preperiod 4, tail
$(1,1,1,0,0)$, realizer $19/5 = \rho/(2^5 - 3^3)$) exercising .5(ii)/(iii)/3b on a
case absent from the file; the fresh anchor $Q(-1/3) = 1$ exactly; and the explicit
$z_b = 4$ witness for Fix 1. Reproduced in full:

```python
#!/usr/bin/env python3
"""Independent adversarial verification of L-9904 (verifier fable-02-v8, 2026-07-22).

Written from the STATEMENTS in research/foundations/L-9904-2adic-conjugacy.md,
NOTATION.md (D-9902/D-9906) and the word-level definitions of L-9903 only; the
author's verify_L9904.py (same scratchpad) was deliberately NOT consulted for
implementation. Exact arithmetic throughout: Python ints (both signs), Fractions
with odd denominators (= Z_(2) = Q cap Z_2), residues mod 2^N. Parity of p/q with
q odd is p mod 2 (B7). Any AssertionError = refutation found.

Checks:
  V1  Isometry |Q(z)-Q(z')|_2 = |z-z'|_2 EXHAUSTIVELY on all pairs mod 2^12,
      plus per-level bijectivity of Q mod 2^j and exact ball-preimage counts
      (finite shadow of L-9904.3(2)/(3)).
  V2  Conjugacy Q o T = sigma o Q on 500 random z mod 2^60 through 40 steps
      (word shift + truncated-Q arithmetic), plus residue-determinacy of the
      60-bit word under integer/negative/rational lifts by multiples of 2^60.
  V3  Periodic-point formula z_w = rho_w/(2^K - 3^a) for ALL 126 words with
      1 <= K <= 6: denominator odd and nonzero, z_w in Z_(2), T^K(z_w) = z_w
      exactly, parity word = w^infty through 42 bits, sign iff 2^K > 3^a
      (a >= 1), z = 0 iff a = 0, per-length injectivity; rho recursion ==
      closed form (both my own implementations); Lemma A checked along the way.
  V4  Lemma A (2-adic iteration formula) on 300 random elements (ints of both
      signs and odd-denominator Fractions), k <= 40, cleared-denominator form;
      plus the cycle-equation iff (T^k(z)=z <=> z(2^k-3^{a_k})=rho_k) on
      random rationals, k <= 12.
  V5  The -17 cycle: orbit, K=11, word (1,1,1,1,0,1,1,1,0,0,0), a=7,
      rho=2363, formula recovers -17; 44-bit word check.
  V6  Eventually periodic rationals: 1/3, 1/5, 1/7 (file's claims, 60+ bits),
      and 7/5 (fresh example not in the file): orbit repeat found, tail word
      (1,1,1,0,0), periodic realizer 19/5 = rho/(2^5-3^3) matches L-9904.5(ii),
      dichotomy 3b (orbit repeat <-> word eventually periodic).
  V7  Exactly-2-to-1: random w (ints and rationals): T(2w)=w, T((2w-1)/3)=w,
      (2w-1)/3 odd with odd denominator, preimages distinct; exhaustive finite
      shadow: every ball c+2^k Z_2 has exactly TWO preimage residues mod 2^{k+1}
      (k <= 10) (= L-9904.4b's two-ball computation).
  V8  Q anchor values mod 2^60: Q(0)=0, Q(-1)=-1, 3Q(1)=-1, 3Q(2)=-2, and the
      fresh anchor Q(-1/3) = 1 exactly (word (1)(0)^infty); sigma(Q(1)) = Q(2).
  V9  Sharpness probes: v_i depends on z mod 2^{i+1} and NOT on z mod 2^i
      (adding 2^i flips bit i); the counterexample z_b = 4 to the naive reading
      of the box's bullet 2 (4 in Z^+ \ {1,2}, eventually periodic word with
      trivial tail, orbit reaches 1).
"""

from fractions import Fraction as F
from itertools import product
import random

random.seed(20260722)


def parity(x):
    if isinstance(x, F):
        assert x.denominator % 2 == 1, ("left Z_(2)!", x)
        return x.numerator & 1
    return x & 1


def T(x):
    if parity(x) == 0:
        return x // 2 if isinstance(x, int) else x / 2
    y = 3 * x + 1
    return y // 2 if isinstance(x, int) else y / 2


def word(x, k):
    out = []
    for _ in range(k):
        out.append(parity(x))
        x = T(x)
    return tuple(out)


def Qk(x, k):
    """First k digits of Q(x), as an integer in [0, 2^k)."""
    return sum(b << i for i, b in enumerate(word(x, k)))


def lowbit(d):
    """2^{nu_2(d)} for a nonzero int d (works for negative d in Python)."""
    return d & -d


def rho_rec(w):
    r = 0
    for i, b in enumerate(w):
        r = 3 ** b * r + b * (1 << i)
    return r


def rho_closed(w):
    return sum(3 ** sum(w[i + 1:]) * (1 << i) for i in range(len(w)) if w[i])


def rand_zelt():
    """Random element of Z_(2): int of either sign or odd-denominator Fraction."""
    if random.random() < 0.5:
        return random.randint(-10 ** 12, 10 ** 12)
    return F(random.randint(-10 ** 9, 10 ** 9), 2 * random.randint(0, 400) + 1)


# ---------------- V1: exhaustive isometry mod 2^12 ----------------
KD = 12
M = 1 << KD
W = [Qk(x, KD) for x in range(M)]
pairs = 0
for x in range(M):
    wx = W[x]
    for y in range(x + 1, M):
        assert lowbit(x - y) == lowbit(wx - W[y]), ("V1 isometry", x, y)
        pairs += 1
# per-level bijectivity and exact ball-preimage counts
for j in range(KD + 1):
    mj = (1 << j) - 1
    seen = {}
    counts = {}
    for x in range(M):
        q = W[x] & mj
        r = x & mj
        assert seen.setdefault(r, q) == q, ("V1 well-def mod 2^j", j, x)
        counts[q] = counts.get(q, 0) + 1
    assert len(set(seen.values())) == 1 << j, ("V1 bijective", j)
    assert all(c == 1 << (KD - j) for c in counts.values()), ("V1 counts", j)
print(f"V1: isometry exhaustive on all {pairs} pairs mod 2^{KD}; "
      f"Q bijective mod 2^j and preimage counts exactly 2^({KD}-j), all j <= {KD}.")

# ---------------- V2: conjugacy, 500 random z mod 2^60, 40 steps ----------------
NBIT = 60
for _ in range(500):
    r = random.getrandbits(NBIT)
    x = r
    for step in range(40):
        w_full = word(x, 41)
        tx = T(x)
        assert word(tx, 40) == w_full[1:], ("V2 word shift", r, step)
        q = sum(b << i for i, b in enumerate(w_full))
        assert Qk(tx, 40) == q >> 1, ("V2 Q-sigma", r, step)  # sigma drops digit 0
        x = tx
# residue-determinacy of the 60-bit word (locality at j = 60)
for _ in range(200):
    r = random.getrandbits(NBIT)
    for t in (random.randint(1, 10 ** 9), -random.randint(1, 10 ** 9),
              F(random.randint(-10 ** 6, 10 ** 6), 2 * random.randint(0, 300) + 1)):
        assert word(r, NBIT) == word(r + (1 << NBIT) * t, NBIT), ("V2 residue", r, t)
print("V2: conjugacy (word shift + truncated Q(Tz) = sigma(Qz)) on 500 random "
      "z mod 2^60 through 40 steps; 60-bit word residue-determinate under 600 lifts.")

# ---------------- V3: periodic points, ALL words 1 <= |w| <= 6 ----------------
nw = 0
for K in range(1, 7):
    realizers = set()
    for w in product((0, 1), repeat=K):
        a = sum(w)
        rho = rho_rec(w)
        assert rho == rho_closed(w), ("V3 rho forms", w)
        D = (1 << K) - 3 ** a
        assert D % 2 == 1 and D != 0, ("V3 unit", w)
        z = F(rho, D)
        assert z.denominator % 2 == 1, ("V3 Z_(2)", w)
        # Lemma A along the orbit + exact return after K steps
        x, ak, rk = z, 0, 0
        for k in range(K):
            assert (1 << k) * x == 3 ** ak * z + rk, ("V3 LemmaA", w, k)
            b = parity(x)
            rk = 3 ** b * rk + b * (1 << k)
            ak += b
            x = T(x)
        assert (1 << K) * x == 3 ** ak * z + rk and ak == a and rk == rho, ("V3 LemmaA end", w)
        assert x == z, ("V3 return", w)
        reps = 42 // K + 1
        assert word(z, 42) == (w * reps)[:42], ("V3 42-bit word", w)
        if a == 0:
            assert z == 0, ("V3 zero", w)
        else:
            assert (z > 0) == ((1 << K) > 3 ** a), ("V3 sign", w)
        realizers.add(z)
        nw += 1
    assert len(realizers) == 1 << K, ("V3 injectivity", K)
anchors = {(1, 0): F(1), (1,): F(-1), (1, 1, 0): F(-5), (1, 0, 0): F(1, 5),
           (0,): F(0), (1, 1, 0, 0): F(5, 7), (1, 1, 1, 0, 0): F(19, 5)}
for w, expect in anchors.items():
    assert F(rho_rec(w), (1 << len(w)) - 3 ** sum(w)) == expect, ("V3 anchor", w)
print(f"V3: periodic-point formula verified for all {nw} words |w| <= 6 "
      "(unit denominator, Lemma A, exact T^K-return, 42-bit word, sign iff 2^K>3^a, "
      "injectivity); anchors incl. 1, -1, -5, 1/5, 5/7, 19/5, 0.")

# ---------------- V4: Lemma A on random elements; cycle-equation iff ----------------
for _ in range(300):
    z = rand_zelt()
    kmax = random.randint(1, 40)
    x, ak, rk = z, 0, 0
    for k in range(kmax + 1):
        assert (1 << k) * x == 3 ** ak * z + rk, ("V4 LemmaA", z, k)
        b = parity(x)
        rk = 3 ** b * rk + b * (1 << k)
        ak += b
        x = T(x)
for _ in range(400):
    z = rand_zelt()
    x, ak, rk = z, 0, 0
    for k in range(1, 13):
        b = parity(x)
        rk = 3 ** b * rk + b * (1 << (k - 1))
        ak += b
        x = T(x)
        assert (x == z) == (z * ((1 << k) - 3 ** ak) == rk), ("V4 iff", z, k)
print("V4: Lemma A exact on 300 random elements (ints both signs + rationals, k <= 40); "
      "cycle-equation iff on 400 random elements, k <= 12.")

# ---------------- V5: the -17 cycle ----------------
orb = [-17]
while True:
    n = T(orb[-1])
    if n == orb[0]:
        break
    orb.append(n)
    assert len(orb) < 100
w17 = tuple(x & 1 for x in orb)
assert len(orb) == 11 and w17 == (1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0), ("V5", orb)
assert sum(w17) == 7 and rho_rec(w17) == 2363 == rho_closed(w17)
assert F(2363, (1 << 11) - 3 ** 7) == -17 and (-17) * ((1 << 11) - 3 ** 7) == 2363
assert word(-17, 44) == w17 * 4
assert orb == [-17, -25, -37, -55, -82, -41, -61, -91, -136, -68, -34]
print("V5: -17 cycle: K=11, word (1,1,1,1,0,1,1,1,0,0,0), a=7, rho=2363, "
      "-17 = 2363/(2^11-3^7); 44-bit word confirmed.")

# ---------------- V6: eventually periodic rationals ----------------
assert T(F(1, 3)) == 1
assert word(F(1, 3), 61) == (1,) + (1, 0) * 30              # (1)(1,0)^inf
z = F(1, 5)
assert T(T(T(z))) == z and word(z, 60) == (1, 0, 0) * 20    # purely periodic
y = T(F(1, 7))
assert y == F(5, 7) and T(T(T(T(y)))) == y
assert word(F(1, 7), 61) == (1,) + (1, 1, 0, 0) * 15        # (1)(1,1,0,0)^inf
# fresh example 7/5 (not in the file): find the orbit repeat, check 3b + .5(ii)
z = F(7, 5)
seen = {}
x, i = z, 0
while x not in seen:
    seen[x] = i
    x = T(x)
    i += 1
l, per = seen[x], i - seen[x]
assert (l, per) == (4, 5), (l, per)
tail_entry = z
for _ in range(l):
    tail_entry = T(tail_entry)
assert tail_entry == F(19, 5)
wtail = word(tail_entry, per)
assert wtail == (1, 1, 1, 0, 0)
assert F(rho_rec(wtail), (1 << per) - 3 ** sum(wtail)) == F(19, 5)
w60 = word(z, 60)
assert w60 == (1, 1, 0, 1) + ((1, 1, 1, 0, 0) * 12)[:56]
# 3b: orbit repeat at (l, per) <-> word eventually periodic with that data
assert all(w60[l + j] == w60[l + (j % per)] for j in range(56 - l))
x = z
for _ in range(l):
    x = T(x)
xx = x
for _ in range(per):
    xx = T(xx)
assert xx == x                                              # T^{l+per}(z) = T^l(z)
print("V6: 1/3 -> (1)(1,0)^inf, 1/5 3-periodic (1,0,0)^inf, 1/7 -> (1)(1,1,0,0)^inf "
      "(all 60+ bits); fresh 7/5: preperiod 4, tail (1,1,1,0,0) at 19/5 = rho/(2^5-3^3), "
      "orbit repeat and word periodicity agree (3b).")

# ---------------- V7: exactly-2-to-1 ----------------
for _ in range(2000):
    w = rand_zelt()
    even_pre = 2 * w
    odd_pre = (2 * F(w) - 1) / 3
    assert T(even_pre) == w
    assert odd_pre.denominator % 2 == 1 and parity(odd_pre) == 1
    assert T(odd_pre) == F(w)
    assert F(even_pre) != odd_pre
for k in range(0, 11):
    # T on residues mod 2^{k+1} -> residues mod 2^k (well-defined by locality)
    cnt = {}
    for r in range(1 << (k + 1)):
        cnt.setdefault(T(r) % (1 << k), 0)
        cnt[T(r) % (1 << k)] += 1
    assert set(cnt.keys()) == set(range(1 << k)) and all(c == 2 for c in cnt.values()), ("V7", k)
print("V7: both preimages 2w and (2w-1)/3 verified on 2000 random elements "
      "(odd branch always in Z_(2), odd, distinct); every ball mod 2^k has exactly "
      "2 preimage residues mod 2^(k+1), k <= 10.")

# ---------------- V8: Q anchors ----------------
MM = 1 << 60
assert Qk(0, 60) == 0
assert Qk(-1, 60) == MM - 1                       # Q(-1) = -1
assert (3 * Qk(1, 60)) % MM == (-1) % MM         # Q(1) = -1/3
assert (3 * Qk(2, 60)) % MM == (-2) % MM         # Q(2) = -2/3
assert Qk(F(-1, 3), 60) == 1                     # fresh: Q(-1/3) = 1 exactly
q1 = Qk(1, 61)
assert (q1 >> 1) % MM == Qk(2, 60) % MM          # sigma(Q(1)) = Q(T(1)) = Q(2)
print("V8: Q(0)=0, Q(-1)=-1, 3Q(1)=-1, 3Q(2)=-2 (mod 2^60); fresh anchor "
      "Q(-1/3) = 1 exactly; sigma(Q(1)) = Q(2).")

# ---------------- V9: sharpness + the box-bullet-2 counterexample ----------------
for _ in range(500):
    z = rand_zelt()
    i = random.randint(0, 30)
    w1 = word(z, i + 1)
    w2 = word(z + (1 << i), i + 1)
    assert w1[:i] == w2[:i] and w1[i] != w2[i], ("V9 flip", z, i)
# z_b = 4: positive integer, not in {1,2}, eventually periodic word, reaches 1
assert word(4, 12) == (0, 0) + (1, 0) * 5        # (0,0)(1,0)^inf: trivial tail
x, hit1 = 4, False
for _ in range(10):
    x = T(x)
    hit1 |= (x == 1)
assert hit1                                      # 4 reaches 1: NOT a counterexample
print("V9: adding 2^i flips exactly bit i (500 probes: mod 2^i insufficient, "
      "mod 2^(i+1) sharp); z_b=4 in Z^+\\{1,2} with eventually periodic word "
      "reaches 1 -- confirms the review's sharpening of box bullet 2.")

print("ALL ADVERSARIAL CHECKS PASSED -- no counterexample to L-9904.1-.6 found.")
```

**Output (verbatim, single run, 2026-07-22, CPython 3, Linux; runtime 4.0 s):**

```text
V1: isometry exhaustive on all 8386560 pairs mod 2^12; Q bijective mod 2^j and preimage counts exactly 2^(12-j), all j <= 12.
V2: conjugacy (word shift + truncated Q(Tz) = sigma(Qz)) on 500 random z mod 2^60 through 40 steps; 60-bit word residue-determinate under 600 lifts.
V3: periodic-point formula verified for all 126 words |w| <= 6 (unit denominator, Lemma A, exact T^K-return, 42-bit word, sign iff 2^K>3^a, injectivity); anchors incl. 1, -1, -5, 1/5, 5/7, 19/5, 0.
V4: Lemma A exact on 300 random elements (ints both signs + rationals, k <= 40); cycle-equation iff on 400 random elements, k <= 12.
V5: -17 cycle: K=11, word (1,1,1,1,0,1,1,1,0,0,0), a=7, rho=2363, -17 = 2363/(2^11-3^7); 44-bit word confirmed.
V6: 1/3 -> (1)(1,0)^inf, 1/5 3-periodic (1,0,0)^inf, 1/7 -> (1)(1,1,0,0)^inf (all 60+ bits); fresh 7/5: preperiod 4, tail (1,1,1,0,0) at 19/5 = rho/(2^5-3^3), orbit repeat and word periodicity agree (3b).
V7: both preimages 2w and (2w-1)/3 verified on 2000 random elements (odd branch always in Z_(2), odd, distinct); every ball mod 2^k has exactly 2 preimage residues mod 2^(k+1), k <= 10.
V8: Q(0)=0, Q(-1)=-1, 3Q(1)=-1, 3Q(2)=-2 (mod 2^60); fresh anchor Q(-1/3) = 1 exactly; sigma(Q(1)) = Q(2).
V9: adding 2^i flips exactly bit i (500 probes: mod 2^i insufficient, mod 2^(i+1) sharp); z_b=4 in Z^+\{1,2} with eventually periodic word reaches 1 -- confirms the review's sharpening of box bullet 2.
ALL ADVERSARIAL CHECKS PASSED -- no counterexample to L-9904.1-.6 found.
```

This is finite verification supporting, not constituting, the proofs (README §10);
the status upgrade rests on the mathematical reconstruction in §1.

### 4. Residual caveats

- **Imports remain imports:** B1 (digit model / completeness of $\mathbb{Z}_2$),
  B5's use of completeness, B6, the existence half of B8 (Haar / Bernoulli product
  measure), and the Dynkin $\pi$–$\lambda$ theorem are standard facts taken from
  the literature, exactly as the file flags. I confirmed the file uses nothing of
  B8 beyond existence plus the ball values, and Lemma U was checked against the
  standard $\pi$–$\lambda$ statement.
- All computational checks inspect finitely many digits and finitely many
  elements; irrational elements of $\mathbb{Z}_2$ are exercised only through
  residues. Nothing here bears on Q-9904, which remains OPEN and neutral.
- The status is PROVED on the strength of one full independent reconstruction plus
  one independent computational refutation attempt; INDEPENDENTLY_VERIFIED requires
  a further independent reviewer per repository convention.
- L-9901 and L-9905 remain PROPOSED; after Fix 2 this file has **no** load-bearing
  or remark-level dependence on either (the C/T transfer is now proved inline; the
  L-9905 links are consistency cross-references only).

*Reviewed and signed: fable-02-v8, 2026-07-22. Script `refute_L9904_v8.py`
(scratchpad; full text and output above).*
