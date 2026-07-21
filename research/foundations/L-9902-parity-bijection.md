# L-9902 — The Terras/Everett parity-vector bijection

```text
Claim ID: L-9902
Title: Locality of T mod powers of 2 and the parity-vector bijection pi_k : Z/2^k Z -> {0,1}^k
Status: PROVED
Authoring agent: fable-02-p2
Reviewing agents: fable-02-v2 (adversarial review 2026-07-21: PASS)
Created: 2026-07-21
Last updated: 2026-07-21 (adversarial review by fable-02-v2)
Dependencies: NOTATION.md (D-9902 shortcut map T; D-9906 parity vector v_i, a_k)
Scope: All k >= 1 (bijection), all j >= 1 / k >= 0 (equivariance); positive-integer
       representatives of residue classes mod 2^k. Classical result (Terras 1976,
       Everett 1977), reconstructed here independently and in full.
Related counterexample candidates: none
```

---

## Statement

Throughout, $T$ is the shortcut map (D-9902) and $v_i(n) := T^i(n) \bmod 2$,
$a_k(n) := \sum_{i=0}^{k-1} v_i(n)$ (D-9906). All variables are quantified explicitly.

**L-9902.1 (locality / equivariance of $T$ modulo powers of $2$).**

*(a) One step.* For every integer $j \ge 1$, every $m \in \mathbb{Z}$, and every
$n \in \mathbb{Z}^+$ such that $n + 2^j m \in \mathbb{Z}^+$:
$$T(n + 2^j m) \;=\; T(n) + 3^{v_0(n)}\, 2^{\,j-1}\, m, \qquad\text{and}\qquad v_0(n + 2^j m) = v_0(n).$$

*(b) Iterated.* For every integer $k \ge 0$, every $m \in \mathbb{Z}$, and every
$n \in \mathbb{Z}^+$ such that $n + 2^k m \in \mathbb{Z}^+$:
$$T^i(n + 2^k m) \;=\; T^i(n) + 3^{\,a_i(n)}\, 2^{\,k-i}\, m \qquad \text{for all } 0 \le i \le k,$$
$$v_i(n + 2^k m) \;=\; v_i(n) \qquad \text{for all } 0 \le i \le k-1.$$

*(c) Well-definedness on residues.* For every $i \ge 0$, the bit $v_i(n)$ of
$n \in \mathbb{Z}^+$ depends only on $n \bmod 2^{\,i+1}$. Consequently, for every
$k \ge 1$ the length-$k$ parity word $(v_0(n), \dots, v_{k-1}(n))$ depends only on
$n \bmod 2^k$, and the map
$$\pi_k : \mathbb{Z}/2^k\mathbb{Z} \longrightarrow \{0,1\}^k, \qquad
\pi_k(n + 2^k\mathbb{Z}) := \bigl(v_0(n), \dots, v_{k-1}(n)\bigr)
\ \text{ for any representative } n \in \mathbb{Z}^+,$$
is well-defined.

**L-9902.2 (bijection).** For every integer $k \ge 1$, the map $\pi_k$ of L-9902.1(c)
is a bijection from $\mathbb{Z}/2^k\mathbb{Z}$ onto $\{0,1\}^k$.

**L-9902.3 (corollaries).** For every integer $k \ge 1$:

*(i) Realization.* Every word $w \in \{0,1\}^k$ is realized as the length-$k$ parity
word of exactly one residue class mod $2^k$; writing $n_w \in \{1, \dots, 2^k\}$ for the
least positive representative of that class, the set of positive integers whose
length-$k$ parity word equals $w$ is exactly $\{\, n_w + 2^k t : t \in \mathbb{Z}_{\ge 0} \,\}$,
which is infinite.

*(ii) Independence.* On the probability space $\Omega = \mathbb{Z}/2^k\mathbb{Z}$ with the
uniform measure $\mathbb{P}(\{r\}) = 2^{-k}$, the coordinate random variables
$V_i(r) := \bigl(\pi_k(r)\bigr)_i$ for $0 \le i \le k-1$ are mutually independent and
each uniform on $\{0,1\}$.

*(iii) Two-lifts / flip structure.* Let $r \in \mathbb{Z}/2^k\mathbb{Z}$ and let $n \in \mathbb{Z}^+$
be any positive representative of $r$. The two residue classes mod $2^{k+1}$ lying over $r$
are $n + 2^{k+1}\mathbb{Z}$ and $(n + 2^k) + 2^{k+1}\mathbb{Z}$. These two lifts share their
first $k$ parity bits (both equal to $\pi_k(r)$), their $k$-th iterates satisfy the exact identity
$$T^k(n + 2^k) \;=\; T^k(n) + 3^{\,a_k(n)},$$
and since $3^{\,a_k(n)}$ is odd, their $(k{+}1)$-st bits differ:
$v_k(n + 2^k) = 1 - v_k(n)$. Hence of the two extensions $(w,0)$ and $(w,1)$ of the word
$w = \pi_k(r)$, each is realized by exactly one of the two lifts.

---

## Definitions

All notation is from `NOTATION.md`; nothing nonstandard is introduced. For convenience:

- $T : \mathbb{Z}^+ \to \mathbb{Z}^+$, $T(n) = n/2$ ($n$ even), $T(n) = (3n+1)/2$ ($n$ odd) (D-9902),
  with $T^0(n) = n$.
- $v_i(n) = T^i(n) \bmod 2 \in \{0,1\}$ and $a_k(n) = \sum_{i=0}^{k-1} v_i(n)$, so $a_0(n) = 0$
  (empty sum) and $a_{i+1}(n) = a_i(n) + v_i(n)$ (D-9906).
- A *residue class* $r \in \mathbb{Z}/2^k\mathbb{Z}$ is the set $n + 2^k\mathbb{Z}$ for any $n \in r$;
  every residue class mod $2^k$ contains infinitely many positive integers (e.g. the unique
  representative in $\{1, \dots, 2^k\}$, plus arbitrary positive multiples of $2^k$). Since
  $T$ is defined on $\mathbb{Z}^+$ (D-9902), all parity words below are computed at
  positive representatives; L-9902.1(c) shows the choice does not matter.
- A closed-form for one step that unifies the two parity cases: for $n \in \mathbb{Z}^+$,
  $$T(n) \;=\; \frac{3^{\,v_0(n)}\, n + v_0(n)}{2}.$$
  (Check: $n$ even gives $(3^0 n + 0)/2 = n/2$; $n$ odd gives $(3n+1)/2$.) This identity
  is used only as an occasional shorthand; both proofs below split into the two cases
  explicitly.

---

## Motivation

This is the load-bearing classical lemma beneath essentially every parity-word or symbolic
direction in this repository. Specifically:

- **Issue #21 explicitly requests an independent reconstruction of exactly this
  flip/two-lifts structure** (their claim L-9601). The present file provides that
  reconstruction from a separate agent (fable-02-p2), from scratch, with full proofs, so
  that the `96xx` packet can cite an independently authored in-repo source instead of
  literature.
- The bijection $\pi_k$ is the standard entry point to **stopping-time density results**
  (planned L-9908 in this foundations packet): the density of $\{n : \sigma(n) = k\}$
  is computed by counting parity words, which is only legitimate once each word is known
  to correspond to exactly one residue class mod $2^k$.
- Every **parity-word / symbolic-dynamics direction** (issues #4, #18, #8) implicitly
  identifies finite $0$–$1$ words with residue classes; corollary (ii) is the precise
  statement licensing "random-bits" heuristics, and corollary (iii) is the tree/extension
  structure those directions build on. For the counterexample program specifically:
  any attempted construction of a divergent orbit via an infinite parity word needs (i)
  and (iii) to know that every finite prefix is realized by an actual arithmetic
  progression of positive integers — and needs the *warning* (recorded in the Gap audit)
  that realizability of all finite prefixes does **not** by itself produce a positive
  integer realizing the infinite word.

---

## Proof

### Preliminary P0 ($T$ maps $\mathbb{Z}^+$ into $\mathbb{Z}^+$, so all iterates are defined)

Let $n \in \mathbb{Z}^+$. If $n$ is even then $n \ge 2$ and $T(n) = n/2$ is an integer with
$T(n) \ge 1$. If $n$ is odd then $3n + 1$ is even, so $T(n) = (3n+1)/2$ is an integer, and
$n \ge 1$ gives $T(n) \ge 2$. In both cases $T(n) \in \mathbb{Z}^+$. By induction on $i \ge 0$
(base $i = 0$: $T^0(n) = n \in \mathbb{Z}^+$; step: apply the above to $T^i(n)$), $T^i(n) \in
\mathbb{Z}^+$ for all $i \ge 0$. Hence $v_i(n)$ and $a_k(n)$ are defined for all $i, k \ge 0$. $\square$

### Proof of L-9902.1(a) (one-step equivariance)

Fix $j \ge 1$, $m \in \mathbb{Z}$, $n \in \mathbb{Z}^+$ with $n' := n + 2^j m \in \mathbb{Z}^+$.
Both $T(n)$ and $T(n')$ are defined by P0. Since $j \ge 1$, the integer $2^j m$ is even,
so $n' \equiv n \pmod 2$ and therefore
$$v_0(n') = n' \bmod 2 = n \bmod 2 = v_0(n).$$
Also $j \ge 1$ guarantees $2^{\,j-1} m \in \mathbb{Z}$, so the right-hand side of the claimed
identity is an integer. Two cases, exhausting all possibilities:

**Case $v_0(n) = 0$** ($n$ even, hence $n'$ even). Then
$$T(n') = \frac{n'}{2} = \frac{n + 2^j m}{2} = \frac{n}{2} + 2^{\,j-1} m
       = T(n) + 3^0 \cdot 2^{\,j-1} m .$$

**Case $v_0(n) = 1$** ($n$ odd, hence $n'$ odd). Then
$$T(n') = \frac{3n' + 1}{2} = \frac{3n + 1 + 3 \cdot 2^j m}{2}
       = \frac{3n+1}{2} + 3 \cdot 2^{\,j-1} m = T(n) + 3^1 \cdot 2^{\,j-1} m .$$

In both cases $T(n + 2^j m) = T(n) + 3^{v_0(n)} 2^{\,j-1} m$. $\square$

### Proof of L-9902.1(b) (iterated equivariance), by induction on $i$

Fix $k \ge 0$, $m \in \mathbb{Z}$, and $n \in \mathbb{Z}^+$ with $n + 2^k m \in \mathbb{Z}^+$.
By P0, $T^i(n) \in \mathbb{Z}^+$ and $T^i(n + 2^k m) \in \mathbb{Z}^+$ for all $i \ge 0$.
We prove, by induction on $i$ over the range $0 \le i \le k$, the statement
$$P(i): \qquad T^i(n + 2^k m) = T^i(n) + 3^{\,a_i(n)}\, 2^{\,k-i}\, m .$$

**Base $i = 0$.** $T^0$ is the identity and $a_0(n) = 0$ (empty sum), so the right-hand
side is $n + 3^0\, 2^{k}\, m = n + 2^k m = T^0(n + 2^k m)$. Thus $P(0)$ holds — note this
covers the edge case $k = 0$, for which $P(0)$ is the only instance and the lemma is the
trivial identity $n + m = n + 3^0 2^0 m$.

**Inductive step.** Let $0 \le i \le k - 1$ (so this step occurs only when $k \ge 1$) and
assume $P(i)$. Put
$$N := T^i(n) \in \mathbb{Z}^+, \qquad j := k - i \ge 1, \qquad M := 3^{\,a_i(n)} m \in \mathbb{Z}.$$
Then $P(i)$ says exactly $T^i(n + 2^k m) = N + 2^{\,j} M$, and this quantity lies in
$\mathbb{Z}^+$ (it equals $T^i$ of the positive integer $n + 2^k m$, by P0). So L-9902.1(a)
applies with the triple $(N, j, M)$ and yields two conclusions:

1. $v_0(N + 2^j M) = v_0(N)$; since $v_0(T^i(x)) = v_i(x)$ by D-9906, this reads
   $$v_i(n + 2^k m) = v_i(n).$$
2. $T(N + 2^j M) = T(N) + 3^{\,v_0(N)}\, 2^{\,j-1} M$, i.e.
   $$T^{i+1}(n + 2^k m) \;=\; T^{i+1}(n) + 3^{\,v_i(n)}\, 2^{\,k-i-1}\, 3^{\,a_i(n)}\, m
   \;=\; T^{i+1}(n) + 3^{\,a_{i+1}(n)}\, 2^{\,k-(i+1)}\, m,$$
   using $a_{i+1}(n) = a_i(n) + v_i(n)$ (D-9906). This is $P(i+1)$.

By induction, $P(i)$ holds for all $0 \le i \le k$. Moreover conclusion 1 was obtained for
every $i$ with $0 \le i \le k-1$, which is precisely the claimed bit preservation
$v_i(n + 2^k m) = v_i(n)$ for $0 \le i \le k - 1$. (For $i = k$ no such claim is made, and
indeed it can fail: $P(k)$ gives $T^k(n + 2^k m) = T^k(n) + 3^{\,a_k(n)} m$, whose increment
is odd whenever $m$ is odd.) $\square$

### Proof of L-9902.1(c) (well-definedness on residues)

Fix $i \ge 0$ and suppose $n, n' \in \mathbb{Z}^+$ satisfy $n' \equiv n \pmod{2^{\,i+1}}$.
Write $n' = n + 2^{\,i+1} m$ with $m \in \mathbb{Z}$. Apply L-9902.1(b) with $k := i + 1 \ge 1$:
the bit-preservation part gives $v_\ell(n') = v_\ell(n)$ for all $0 \le \ell \le k - 1 = i$;
in particular $v_i(n') = v_i(n)$. So $v_i$ is constant on each residue class mod $2^{\,i+1}$
intersected with $\mathbb{Z}^+$; that is, $v_i(n)$ depends only on $n \bmod 2^{\,i+1}$.

Now fix $k \ge 1$ and suppose $n, n' \in \mathbb{Z}^+$ with $n' \equiv n \pmod{2^k}$. For each
$0 \le i \le k - 1$ we have $i + 1 \le k$, hence $2^{\,i+1} \mid 2^k \mid (n' - n)$, hence
$n' \equiv n \pmod{2^{\,i+1}}$, hence $v_i(n') = v_i(n)$ by the previous paragraph. So the
whole word $(v_0(n), \dots, v_{k-1}(n))$ is the same for every positive representative $n$ of
a given class $r \in \mathbb{Z}/2^k\mathbb{Z}$. Since every class contains a positive
representative (Definitions), the map $\pi_k$ is well-defined on $\mathbb{Z}/2^k\mathbb{Z}$. $\square$

### Proof of L-9902.2 (bijection)

Fix $k \ge 1$. $\pi_k$ is well-defined by L-9902.1(c).

**Injectivity.** Let $r, r' \in \mathbb{Z}/2^k\mathbb{Z}$ with $r \ne r'$; we show
$\pi_k(r) \ne \pi_k(r')$. Choose positive representatives $n \in r$, $n' \in r'$ (possible:
Definitions). Since $r \ne r'$, we have $2^k \nmid (n - n')$; in particular $n \ne n'$, so
the 2-adic valuation $j := \nu_2(n - n')$ is a well-defined nonnegative integer, and
$2^k \nmid (n - n')$ forces
$$0 \le j \le k - 1 .$$
Write $n = n' + 2^{\,j} m$ where $m := (n - n')/2^{\,j}$ is an **odd** integer (possibly
negative), by definition of $\nu_2$. Apply L-9902.1(b) with base point $n' \in \mathbb{Z}^+$,
exponent $k := j \ge 0$ (allowed: L-9902.1(b) was proved for all $k \ge 0$, so the edge case
$j = 0$ is covered), and this odd $m$; note $n' + 2^j m = n \in \mathbb{Z}^+$ as required.
The instance $i = j$ of $P(i)$ gives
$$T^{\,j}(n) \;=\; T^{\,j}(n') + 3^{\,a_j(n')}\, 2^{\,j - j}\, m \;=\; T^{\,j}(n') + 3^{\,a_j(n')}\, m .$$
The increment $3^{\,a_j(n')} m$ is a product of two odd integers, hence odd. Therefore
$T^{\,j}(n)$ and $T^{\,j}(n')$ have opposite parities:
$$v_j(n) \;=\; 1 - v_j(n') \;\ne\; v_j(n') .$$
Since $0 \le j \le k-1$, the words $\pi_k(r)$ and $\pi_k(r')$ differ in coordinate $j$.
(For orientation, though not needed for the conclusion: the same lemma at $i < j$ gives
$T^i(n) - T^i(n') = 3^{\,a_i(n')} 2^{\,j-i} m$, of exact 2-adic valuation $j - i$ — the
valuation of the orbit difference decreases by exactly $1$ per step until it reaches $0$
at step $j$, where the parities split.) Hence $\pi_k$ is injective.

**Surjectivity.** Both $\mathbb{Z}/2^k\mathbb{Z}$ and $\{0,1\}^k$ are finite sets of
cardinality exactly $2^k$. Since $\pi_k$ is injective, its image
$\pi_k(\mathbb{Z}/2^k\mathbb{Z}) \subseteq \{0,1\}^k$ has cardinality
$|\mathbb{Z}/2^k\mathbb{Z}| = 2^k$. A subset of a $2^k$-element set having $2^k$ elements is
the whole set; hence the image is all of $\{0,1\}^k$ and $\pi_k$ is surjective. (This is a
purely finite counting argument; no limit or infinite process is involved.)

Therefore $\pi_k$ is a bijection. $\square$

*Edge case $k = 1$, checked directly:* $\pi_1(0 + 2\mathbb{Z}) = (v_0(2)) = (0)$ and
$\pi_1(1 + 2\mathbb{Z}) = (v_0(1)) = (1)$; a bijection $\mathbb{Z}/2\mathbb{Z} \to \{0,1\}$,
consistent with the general proof.

### Proof of L-9902.3(i) (realization)

Fix $k \ge 1$ and $w \in \{0,1\}^k$. By surjectivity of $\pi_k$ (L-9902.2) there exists
$r \in \mathbb{Z}/2^k\mathbb{Z}$ with $\pi_k(r) = w$, and by injectivity this $r$ is unique.
Let $n_w$ be the unique representative of $r$ in $\{1, \dots, 2^k\}$ (each residue class mod
$2^k$ meets $\{1, \dots, 2^k\}$ in exactly one point; for the class of $0$ that point is $2^k$).
Then the positive integers belonging to $r$ are exactly $n_w + 2^k t$ for $t \in \mathbb{Z}_{\ge 0}$:
indeed $n_w + 2^k t \ge n_w \ge 1$ for $t \ge 0$, while $n_w + 2^k t \le n_w - 2^k \le 0$ for
$t \le -1$. By L-9902.1(c), every such positive integer has length-$k$ parity word
$\pi_k(r) = w$; and conversely any positive integer whose length-$k$ word is $w$ lies in a
class mapping to $w$ under $\pi_k$, which by uniqueness is $r$. The set
$\{n_w + 2^k t : t \ge 0\}$ is infinite since $t \mapsto n_w + 2^k t$ is injective. $\square$

### Proof of L-9902.3(ii) (independence and uniformity)

Fix $k \ge 1$; let $\Omega = \mathbb{Z}/2^k\mathbb{Z}$ carry the uniform measure
$\mathbb{P}(A) = |A| / 2^k$ for $A \subseteq \Omega$, and let $V_i(r) = (\pi_k(r))_i$,
$0 \le i \le k-1$. We prove the full factorization over arbitrary sub-collections, which is
the definition of mutual independence for finitely many discrete random variables.

Let $S \subseteq \{0, \dots, k-1\}$ be any subset and $(b_i)_{i \in S} \in \{0,1\}^S$ any
assignment of bits. Since $\pi_k$ is a bijection (L-9902.2),
$$\#\{\, r \in \Omega : V_i(r) = b_i \ \forall i \in S \,\}
   \;=\; \#\{\, w \in \{0,1\}^k : w_i = b_i \ \forall i \in S \,\}
   \;=\; 2^{\,k - |S|},$$
the last count because the $|S|$ coordinates in $S$ are pinned and the remaining $k - |S|$
coordinates range freely over $\{0,1\}$. Hence
$$\mathbb{P}\Bigl[\,\bigcap_{i \in S} \{V_i = b_i\}\Bigr] \;=\; \frac{2^{\,k-|S|}}{2^k} \;=\; 2^{-|S|}.$$
Taking $S = \{i\}$ a singleton gives the marginals $\mathbb{P}[V_i = 0] = \mathbb{P}[V_i = 1] = 1/2$,
so each $V_i$ is uniform on $\{0,1\}$; and then for every $S$ and every bit assignment,
$$\mathbb{P}\Bigl[\,\bigcap_{i \in S} \{V_i = b_i\}\Bigr] \;=\; 2^{-|S|} \;=\; \prod_{i \in S} \mathbb{P}[V_i = b_i],$$
which is exactly mutual independence. (Empty $S$: both sides equal $1$, the empty product
convention of `NOTATION.md`.) $\square$

*Scope warning (recorded again in the Gap audit):* this is a statement about the uniform
measure on the finite set $\mathbb{Z}/2^k\mathbb{Z}$ — nothing more. It does not assert any
independence along the orbit of a single fixed integer.

### Proof of L-9902.3(iii) (two lifts and the flip)

Fix $k \ge 1$, $r \in \mathbb{Z}/2^k\mathbb{Z}$, and a positive representative
$n \in r \cap \mathbb{Z}^+$. Reduction mod $2^k$ maps $\mathbb{Z}/2^{k+1}\mathbb{Z}$ onto
$\mathbb{Z}/2^k\mathbb{Z}$, and the fiber over $r$ consists of exactly the two classes
$$r_0 := n + 2^{k+1}\mathbb{Z}, \qquad r_1 := (n + 2^k) + 2^{k+1}\mathbb{Z},$$
which are distinct because $(n + 2^k) - n = 2^k \not\equiv 0 \pmod{2^{k+1}}$, and exhaust
the fiber because any $x \equiv n \pmod{2^k}$ satisfies $x \equiv n$ or $x \equiv n + 2^k
\pmod{2^{k+1}}$ (write $x = n + 2^k s$ and split by the parity of $s$). Note
$n + 2^k \in \mathbb{Z}^+$ since $n \ge 1$.

**Shared prefix.** Both $n$ and $n + 2^k$ are positive representatives of $r$ modulo $2^k$,
so by L-9902.1(c) their length-$k$ parity words coincide and both equal $w := \pi_k(r)$.
Consequently $a_k(n + 2^k) = a_k(n)$ (sums of identical bits).

**Exact increment.** Apply L-9902.1(b) with this $n$, with exponent $k$, and with $m = 1$
(so $n + 2^k m = n + 2^k \in \mathbb{Z}^+$); the instance $i = k$ gives precisely
$$T^k(n + 2^k) \;=\; T^k(n) + 3^{\,a_k(n)}\, 2^{\,k-k} \cdot 1 \;=\; T^k(n) + 3^{\,a_k(n)}.$$
(The loose paraphrase "$T^k(n) + 3^{a_k}\cdot(\text{odd})$" is here made exact: the
increment is exactly $3^{\,a_k(n)}$, since $m = 1$.)

**Flip.** $3^{\,a_k(n)}$ is odd (a power of $3$; this includes $3^0 = 1$ when $a_k(n) = 0$,
i.e. when $w$ is the all-zeros word). An odd increment reverses parity, so
$$v_k(n + 2^k) \;=\; T^k(n + 2^k) \bmod 2 \;=\; \bigl(T^k(n) + 1\bigr) \bmod 2 \;=\; 1 - v_k(n).$$
By L-9902.1(c) applied at level $k + 1$, the bit $v_k$ is constant on each class mod
$2^{k+1}$, so this computation at the chosen representatives is a statement about the two
classes $r_0, r_1$ themselves: their length-$(k{+}1)$ words are $(w, v_k(n))$ and
$(w, 1 - v_k(n))$ in some order. These are exactly the two extensions of $w$, one per lift. $\square$

*Remark (alternative route to L-9902.2, not used above).* L-9902.3(iii) yields an
induction on $k$: $\pi_1$ is a bijection (checked above), and if $\pi_k$ is a bijection then
the $2^{k+1}$ classes mod $2^{k+1}$, grouped in $2^k$ fibers of two lifts each, realize each
of the $2^{k+1}$ words $(w, 0), (w, 1)$ exactly once — so $\pi_{k+1}$ is a bijection. The
direct valuation proof was preferred in L-9902.2 because it needs no case grouping, but a
reviewer may check this second route as independent confirmation; note it is not circular,
since the proof of L-9902.3(iii) uses only L-9902.1, never L-9902.2.

*Remark (2-adic extension; informational only, not used by anything above).* All statements
and proofs of L-9902.1–L-9902.3 go through verbatim with $\mathbb{Z}^+$ replaced by the
2-adic integers $\mathbb{Z}_2$ (D-9906 already permits $n \in \mathbb{Z}_2$), with "parity"
meaning the last 2-adic digit; the representative-selection step in L-9902.1(c) then becomes
unnecessary. This file's claims are asserted, and verified, only in the $\mathbb{Z}^+$
formulation above.

---

## Dependency audit

- **D-9902 (shortcut map $T$)** — used everywhere; the two-case definition is used verbatim
  in P0 and in the case split of L-9902.1(a).
- **D-9906 (parity vector $v_i$, odd-step count $a_k$)** — used in L-9902.1(b)
  (the identities $v_0(T^i(x)) = v_i(x)$ and $a_{i+1} = a_i + v_i$, both immediate from
  D-9906's defining formulas), and throughout the statements.
- **Empty-sum convention** (`NOTATION.md`, Conventions: empty sums are $0$, empty products
  are $1$) — used for $a_0(n) = 0$ in the induction base of L-9902.1(b) and for the empty-$S$
  case of L-9902.3(ii).
- **Elementary number theory / set theory**, used without citation: existence and basic
  property of the 2-adic valuation $\nu_2$ on nonzero integers (`NOTATION.md` preamble
  defines $\nu_2$); odd $\times$ odd $=$ odd; an injection between finite sets of equal
  cardinality is a surjection (proved inline by counting the image); the fiber structure of
  $\mathbb{Z}/2^{k+1}\mathbb{Z} \to \mathbb{Z}/2^k\mathbb{Z}$ (proved inline).
- **No other claim files are used.** In particular this file does not depend on issue #21's
  L-9601 (it is an independent reconstruction of that content) nor on any `L-99xx` file.
  There is no circularity: L-9902.1 uses only D-9902/D-9906; L-9902.2 uses only L-9902.1;
  L-9902.3 uses only L-9902.1 and L-9902.2 (and part (iii) uses only L-9902.1).

---

## Gap audit

Deliberate search for the failure modes listed in README §8:

- **Hidden finiteness assumptions:** none needed — every statement is about a fixed finite
  $k$ (or fixed $i, j$). The surjectivity argument is finite pigeonhole, stated as such.
- **Unjustified induction:** the induction in L-9902.1(b) has an explicit base ($i = 0$,
  valid for every $k \ge 0$ including $k = 0$) and an explicit step valid exactly for
  $0 \le i \le k-1$ (the step needs $j = k - i \ge 1$ so that $2^{\,j-1} m \in \mathbb{Z}$
  and $2^j m$ is even; this is why the bit-preservation conclusion stops at $i = k-1$).
- **Boundary cases:** $k = 1$ (bijection checked directly), $j = 0$ in the injectivity proof
  (covered because L-9902.1(b) was deliberately stated for $k \ge 0$), $a_k(n) = 0$
  (all-even word; $3^0 = 1$ is still odd, flip still holds), residue class $0 \bmod 2^k$
  (positive representative $2^k$ exists; its word is the all-zeros word since
  $T^i(2^k) = 2^{k-i}$ is even for $0 \le i \le k-1$), negative $m$ (allowed throughout;
  positivity of $n + 2^j m$ is an explicit hypothesis, and the injectivity proof uses a
  possibly negative odd $m$).
- **Domain hygiene:** $T$ is only defined on $\mathbb{Z}^+$ (D-9902), so $\pi_k$ on
  $\mathbb{Z}/2^k\mathbb{Z}$ requires a representative choice; this is exactly the
  well-definedness step L-9902.1(c), proved *before* bijectivity is discussed. P0 ensures
  all iterates remain in the domain.
- **Empirical vs. universal:** the python run below is labeled finite verification and
  supports, but is not part of, the proofs.
- **Incorrectly assumed independence:** corollary (ii) *proves* independence, but only for
  the uniform measure on $\mathbb{Z}/2^k\mathbb{Z}$ at a fixed finite $k$. It does **not**
  say that the bits along the orbit of any *fixed* integer behave randomly, and it does not
  transfer to natural density statements about $\mathbb{Z}^+$ without a separate (easy but
  distinct) equidistribution-of-residues argument. Any use of (ii) as a heuristic for a
  single orbit must be flagged as heuristic.
- **Finite prefixes vs. infinite objects:** (i) and (iii) show every finite word is realized
  and every word has both extensions realized. The inverse limit of the $\pi_k^{-1}$ along
  extensions produces only a 2-adic integer, not necessarily a positive one; nothing in this
  file asserts that an infinite parity word is realized by a positive integer. Counterexample
  constructions must not silently take that step.
- **Circular dependence:** none; see Dependency audit (the alternative-route remark in
  L-9902.3(iii) is explicitly checked non-circular).
- **Assumptions equivalent to Collatz:** none anywhere — no statement here mentions
  reaching 1, cycles, or boundedness.

No gaps found; all three claims are asserted with complete proofs at status PROPOSED
(pending independent review). No PARTIAL or CONJECTURED labels are needed, and no
correction to the task's stated claims was required — all statements checked out as given
(the one loose phrase, "$3^{a_k}\cdot(\text{odd})$" for the lift increment, is sharpened to
the exact value $3^{\,a_k(n)}$ in L-9902.3(iii)).

---

## Adversarial tests

**Finite verification** (not proof). Exact integer arithmetic, python3, seed fixed for
reproducibility. Script kept at the authoring session's scratchpad as `verify_L9902.py`;
reproduced in full here.

```python
#!/usr/bin/env python3
"""Finite verification for L-9902 (parity-vector bijection), agent fable-02-p2.

Exact integer arithmetic only. Verifies:
  (A) one-step equivariance  T(n + 2^j m) = T(n) + 3^{v0(n)} 2^{j-1} m   (random trials)
  (B) iterated equivariance  T^i(n + 2^k m) = T^i(n) + 3^{a_i(n)} 2^{k-i} m, 0 <= i <= k,
      and bit preservation   v_i(n + 2^k m) = v_i(n) for 0 <= i <= k-1   (random trials)
  (C) pi_k is a bijection Z/2^k Z -> {0,1}^k for k = 1..14 (direct enumeration),
      plus well-definedness on residues (random lifts) and uniform marginals
  (D) two-lifts flip property for k = 1..12: lifts n, n + 2^k share the first k bits,
      v_k differs, and T^k(n + 2^k) = T^k(n) + 3^{a_k(n)} exactly.
"""
import random

random.seed(99022026)


def T(n):
    assert n >= 1
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def orbit(n, k):
    """[n, T(n), ..., T^k(n)]"""
    out = [n]
    for _ in range(k):
        out.append(T(out[-1]))
    return out


def word(n, k):
    """(v_0(n), ..., v_{k-1}(n))"""
    return tuple(x % 2 for x in orbit(n, k)[:k])


def a(n, k):
    """a_k(n) = number of odd steps among the first k."""
    return sum(word(n, k))


# ---- (A) one-step equivariance, random trials -------------------------------
trials_A = 0
for _ in range(20000):
    j = random.randint(1, 40)
    n = random.randint(1, 10**12)
    m = random.randint(-10**6, 10**6)
    if n + 2**j * m < 1:
        continue
    lhs = T(n + 2**j * m)
    rhs = T(n) + 3 ** (n % 2) * 2 ** (j - 1) * m
    assert lhs == rhs, (n, j, m)
    trials_A += 1
print(f"(A) one-step equivariance: OK on {trials_A} random (n, j, m) triples")

# ---- (B) iterated equivariance + bit preservation, random trials ------------
trials_B = 0
for _ in range(2000):
    k = random.randint(0, 30)
    n = random.randint(1, 10**12)
    m = random.randint(-10**6, 10**6)
    if n + 2**k * m < 1:
        continue
    O1, O2 = orbit(n, k), orbit(n + 2**k * m, k)
    for i in range(k + 1):
        assert O2[i] == O1[i] + 3 ** a(n, i) * 2 ** (k - i) * m, (n, k, m, i)
    for i in range(k):  # bits 0..k-1 preserved
        assert O2[i] % 2 == O1[i] % 2, (n, k, m, i)
    trials_B += 1
print(f"(B) iterated equivariance (0<=i<=k) + bit preservation: OK on {trials_B} random (n, k, m)")

# ---- (C) bijection pi_k for k = 1..14, direct enumeration -------------------
for k in range(1, 15):
    # positive representatives 1..2^k cover every residue class mod 2^k exactly once
    words = [word(n, k) for n in range(1, 2**k + 1)]
    assert len(set(words)) == 2**k, f"pi_{k} not injective"
    # uniform marginals: each bit position is 1 on exactly 2^(k-1) residues
    for i in range(k):
        assert sum(w[i] for w in words) == 2 ** (k - 1), (k, i)
print("(C) pi_k bijective on Z/2^k Z for k = 1..14 (enumeration); all marginals exactly 1/2")

# well-definedness: word depends only on the residue class mod 2^k
for _ in range(3000):
    k = random.randint(1, 14)
    n = random.randint(1, 2**k)
    t = random.randint(0, 10**9)
    assert word(n, k) == word(n + 2**k * t, k), (n, k, t)
print("(C') well-definedness of pi_k on residues mod 2^k: OK on 3000 random lifts")

# ---- (D) two-lifts flip property, k = 1..12, exhaustive ---------------------
for k in range(1, 13):
    for n in range(1, 2**k + 1):
        n2 = n + 2**k
        assert word(n, k) == word(n2, k), (k, n)                       # first k bits shared
        Tk1, Tk2 = orbit(n, k)[k], orbit(n2, k)[k]
        assert Tk2 == Tk1 + 3 ** a(n, k), (k, n)                       # exact increment 3^{a_k}
        assert word(n2, k + 1)[k] == 1 - word(n, k + 1)[k], (k, n)     # bit v_k flips
print("(D) two-lifts flip: OK exhaustively for k = 1..12 (both lifts, exact 3^{a_k} increment)")

print("ALL CHECKS PASSED")
```

**Observed output** (python3, single run, 2026-07-21; the sub-20000/2000 trial counts in
(A)/(B) reflect random draws rejected by the positivity hypothesis $n + 2^j m \ge 1$, which
is an explicit hypothesis of the lemma):

```text
(A) one-step equivariance: OK on 14824 random (n, j, m) triples
(B) iterated equivariance (0<=i<=k) + bit preservation: OK on 1612 random (n, k, m)
(C) pi_k bijective on Z/2^k Z for k = 1..14 (enumeration); all marginals exactly 1/2
(C') well-definedness of pi_k on residues mod 2^k: OK on 3000 random lifts
(D) two-lifts flip: OK exhaustively for k = 1..12 (both lifts, exact 3^{a_k} increment)
ALL CHECKS PASSED
```

**What the tests would have caught.** (A)/(B) test the exact coefficients $3^{a_i} 2^{k-i}$
(a wrong exponent or an off-by-one in $j - 1$ fails immediately, including for negative $m$);
(C) tests injectivity *and* surjectivity by exhaustion for $k \le 14$ (i.e. over
$2 + 4 + \dots + 2^{14} = 32766$ residue classes) and the exactly-$1/2$ marginals of (ii);
(C') tests representative-independence with lifts up to $\sim 2^{14} \cdot 10^9$; (D) tests
all three assertions of (iii) exhaustively for $k \le 12$, including the all-zeros word
($n = 2^k$, where $a_k = 0$) and both orders of the flip.

**Hand-checked micro-examples** (worked by hand, independent of the script):
$k = 2$: representatives $1, 2, 3, 4$ have orbits $1 \to 2 \to 1$, $2 \to 1 \to 2$,
$3 \to 5 \to 8$, $4 \to 2 \to 1$, hence words $(1,0), (0,1), (1,1), (0,0)$ — all four words,
each once. Two-lifts at $k = 2$, $n = 3$: $a_2(3) = 2$, $T^2(3) = 8$,
$T^2(3 + 4) = T^2(7) = T(11) = 17 = 8 + 3^2$ — exact increment $3^{a_2}$, and
$v_2(3) = 0 \ne 1 = v_2(7)$. Flip confirmed.

---

## Remaining uncertainty

- I am confident in all three proofs; they are short, classical, and were finitely verified
  from multiple angles. The points a reviewer should probe hardest: (1) the well-definedness
  step L-9902.1(c) — specifically that defining $\pi_k$ via positive representatives is
  fully squared with D-9902's domain $\mathbb{Z}^+$; (2) the injectivity argument's edge case
  $j = \nu_2(n - n') = 0$, which relies on L-9902.1(b) having been stated for $k \ge 0$
  (base case only) rather than $k \ge 1$; (3) the sign/positivity bookkeeping when $m < 0$.
- The independence corollary (ii) is exactly as strong as stated and no stronger; misuse
  (applying it to a single orbit, or to natural density without an equidistribution step)
  is the main downstream risk, flagged in the Gap audit.
- Status is PROPOSED per the packet convention: the author does not self-upgrade to PROVED.

## Suggested next attack

1. **Independent review to PROVED / INDEPENDENTLY_VERIFIED:** a reviewing agent should
   reconstruct L-9902.2 via the *other* route (induction on $k$ through the flip structure,
   sketched in the remark after L-9902.3(iii)) and confirm the two routes agree; this
   simultaneously discharges issue #21's request for an independent check of the flip
   structure (their L-9601) against this file.
2. **Build L-9908 (stopping-time density) on this file:** define the coefficient-word
   correspondence $T^k(n) = (3^{a_k(n)} n + \rho_k)/2^k$ with $\rho_k$ determined by the
   parity word, and count words with $a_k < \gamma^{-1}\dots$ — the bijection here is the
   counting license.
3. **Extension worth writing separately (do not fold in here):** the 2-adic version
   $\pi_\infty : \mathbb{Z}_2 \to \{0,1\}^\infty$ as the inverse limit of the $\pi_k$
   (a homeomorphism), plus the precise statement of *why* surjectivity onto infinite words
   does not produce positive-integer counterexamples for free. That file would be the
   correct place to attack the "infinite parity word $\Rightarrow$ candidate object" step
   that issues #4/#18/#8 need, and the correct place to look for a loophole in it.

---

*File authored by fable-02-p2, 2026-07-21. Finite verification script: `verify_L9902.py`
(scratchpad; full text above).*

---

## Verification note (fable-02-v2, 2026-07-21)

**Verdict: PASS.** Adversarial review per README §13, performed independently of the
author's confidence and without reusing the author's script. Status upgraded
PROPOSED → PROVED (not INDEPENDENTLY_VERIFIED — that upgrade is reserved for
cross-session review per this repository's conventions). **No fixes were required:**
no substantive gap was found, and no minor slip (typo, misquantification, boundary
omission) was found either. The only edits made by the reviewer are the header fields
(Status, Reviewing agents, Last updated) and this appended section.

### 1. Independent reconstruction of every proof

Each proof was re-derived by hand from D-9902/D-9906 and elementary number theory
alone, before re-reading the author's prose:

- **P0:** even $n \ge 2 \Rightarrow n/2 \in \mathbb{Z}^+$; odd $n \ge 1 \Rightarrow
  (3n+1)/2 \in \mathbb{Z}, \ge 2$. Induction on $i$ is anchored at $T^0 = \mathrm{id}$. Sound.
- **L-9902.1(a):** $j \ge 1$ makes $2^j m$ even (parity preserved) *and* $2^{\,j-1}m$
  an integer; the two-case algebra ($n'/2 = T(n) + 2^{\,j-1}m$;
  $(3n' + 1)/2 = T(n) + 3\cdot 2^{\,j-1}m$) was redone and matches
  $3^{v_0(n)}2^{\,j-1}m$ in both cases. Sound; both hypotheses are necessary
  (see negation probes below).
- **L-9902.1(b):** the induction was reconstructed. The one point where a hidden gap
  could live — positivity of $N + 2^j M$ for negative $m$ before invoking (a) — is
  correctly discharged: that quantity *equals* $T^i(n + 2^k m)$, an iterate of a
  positive integer, by $P(i)$ + P0, so no separate sign argument is needed. The
  exponent bookkeeping $3^{v_i}\cdot 3^{a_i} = 3^{a_{i+1}}$ and $2^{k-i-1} = 2^{k-(i+1)}$
  checks out. The base $i = 0$ genuinely covers $k = 0$ (the range of the inductive
  step is then empty), which is exactly what the injectivity proof later needs. Sound.
- **L-9902.1(c):** direct consequence of (b) with $k := i+1$; the divisibility chain
  $2^{\,i+1} \mid 2^k \mid (n'-n)$ for $i \le k-1$ was checked. The exponent $i+1$ is
  sharp (probe T8 below: $v_i$ is *not* determined by $n \bmod 2^i$), so the statement
  is as strong as possible. Sound.
- **L-9902.2 (injectivity):** reconstructed the valuation argument. $r \ne r'$ gives
  $2^k \nmid (n - n')$ hence $n \ne n'$ hence $j := \nu_2(n-n') \in \{0, \dots, k-1\}$
  well-defined; $m = (n-n')/2^j$ odd, possibly negative — the positivity hypothesis of
  (b) holds because $n' + 2^j m = n \in \mathbb{Z}^+$ by construction. The flagged edge
  $j = 0$ was probed specifically: instance $P(0)$ of (b)-with-$k := 0$ is the identity
  $n = n' + m$ with $m$ odd, so $v_0$ differs — no appeal to an inductive step with
  $j = k - i \ge 1$ is made, and the argument is airtight. Odd $\times$ odd $=$ odd
  gives the parity split at coordinate $j \le k-1$. **Surjectivity** is finite counting
  (injection between equal finite cardinalities); no infinite process. Sound.
- **L-9902.3(i):** uniqueness from bijectivity; the least-representative window
  $\{1, \dots, 2^k\}$ (class of $0 \mapsto 2^k$) and the inequality
  $n_w + 2^k t \le n_w - 2^k \le 0$ for $t \le -1$ were verified; both inclusions of
  the set equality were reconstructed. Sound.
- **L-9902.3(ii):** the count $2^{\,k-|S|}$ transfers through the bijection; marginals
  and the product formula follow; the empty-$S$ convention matches `NOTATION.md`.
  Crucially the statement is *only* about the uniform measure on
  $\mathbb{Z}/2^k\mathbb{Z}$, and both the statement and the Gap audit say so
  explicitly — the scope is exactly right and no density claim about
  naturally-sampled integers is smuggled in. Sound.
- **L-9902.3(iii):** fiber structure of $\mathbb{Z}/2^{k+1} \to \mathbb{Z}/2^k$
  (distinctness + exhaustion via parity of $s$ in $x = n + 2^k s$) reconstructed;
  exact increment is (b) at $i = k$, $m = 1$; $3^{a_k}$ odd including $a_k = 0$;
  the promotion from chosen representatives to residue classes correctly cites (c)
  at level $k+1$. The alternative-route remark was checked non-circular: (iii) uses
  only L-9902.1, never L-9902.2. Sound.
- **Hand micro-examples in the file** (orbits of $1,2,3,4$ at $k=2$;
  $T^2(7) = 17 = 8 + 3^2$) were recomputed by hand and are correct.
- **Dependency audit cross-checked** against `NOTATION.md`: $\nu_2$ is defined in the
  preamble, empty sums/products in Conventions, D-9902/D-9906 as cited. No claim file
  is used; no circularity.

### 2. The four risk spots specifically probed

1. *Well-definedness via positive representatives (T only on $\mathbb{Z}^+$):* every
   application of $T$ in the file is at a point certified in $\mathbb{Z}^+$ (by
   hypothesis, by P0, or by construction $n' + 2^j m = n$); every residue class has a
   positive representative; (c) is proved before $\pi_k$ is used. No gap.
2. *$j = 0$ in injectivity:* handled by the base case of (b) alone; verified above.
3. *Sign/positivity for $m < 0$:* the only place a negative $m$ meets $T$'s domain is
   through quantities equal to iterates of positive integers; verified above and
   stress-tested computationally at the boundary $n + 2^j m = 1$.
4. *Scope of the independence corollary:* the statement fixes
   $\Omega = \mathbb{Z}/2^k\mathbb{Z}$ with uniform measure and asserts nothing about
   single orbits or natural density; the Gap audit repeats the warning. Scope correct.

### 3. Independent computational refutation attempt

Script written from the statements alone (author's script not consulted for
implementation), exact integer arithmetic, seed 20260721, kept at the reviewing
session's scratchpad as `refute_L9902_v2.py`. Coverage beyond the author's tests:
crafted boundary triples with $n + 2^j m = 1$ exactly, $k$ up to $16$ for the
bijection (vs. 14), lifts $t \sim 10^{30}$ (vs. $10^9$), big-integer flip identities
up to $k = 64$, independence over *all* $3^k$ pairs $(S, b)$ for $k \le 8$
(vs. marginals only), a converse test for realization, and explicit negation probes.

```python
#!/usr/bin/env python3
"""Independent adversarial verification of L-9902 (agent fable-02-v2, 2026-07-21).

Written from the STATEMENTS in research/foundations/L-9902-parity-bijection.md and
the definitions D-9902/D-9906 in research/foundations/NOTATION.md only; the author's
verify_L9902.py was deliberately not reused. Exact integer arithmetic throughout.

Checks (any AssertionError = refutation found):
  T1  L-9902.1(a) one-step equivariance, crafted adversarial edges + random trials
      (n small, j = 1, m large negative with n + 2^j m = 1, m = 0, huge m > 0).
  T2  L-9902.1(b) iterated equivariance for ALL 0 <= i <= k and bit preservation for
      0 <= i <= k-1, including k = 0, negative odd m, and the author's side remark
      that the increment at i = k is odd when m is odd (so v_k genuinely can flip).
  T3  L-9902.2 bijectivity of pi_k for k = 1..16 by exhaustive enumeration of the
      positive representatives 1..2^k (injectivity + cardinality => surjectivity;
      for k <= 10 the image is additionally compared with all of {0,1}^k directly).
  T4  L-9902.1(c) well-definedness: word(n,k) invariant under huge lifts n + 2^k t,
      t up to ~10^30 (bigint), k up to 16.
  T5  L-9902.3(iii) flip: exhaustive for k = 1..12 over both lifts, plus random
      large-k (k up to 64) big-integer spot checks of the EXACT identity
      T^k(n + 2^k) = T^k(n) + 3^{a_k(n)} and the flip v_k(n + 2^k) = 1 - v_k(n).
  T6  L-9902.3(i) realization/least representative: for k = 1..10 build the inverse
      of pi_k by enumeration; check n_w in {1..2^k} is unique per word, that
      n_w + 2^k t realizes w for random t >= 0, and that random positive integers
      with word w are ~ n_w (mod 2^k) (set equality of realizers).
  T7  L-9902.3(ii) independence: for k = 1..8, for ALL subsets S of {0..k-1} and
      ALL bit assignments b on S, the count of residues with matching bits is
      exactly 2^(k-|S|). Random spot checks for k = 9..14.
  T8  Necessity/sharpness probes (attempted negations):
      - j = 0 with odd m breaks parity preservation (hypothesis j >= 1 necessary);
      - v_i is NOT determined by n mod 2^i (the exponent i+1 in 1(c) is sharp);
      - valuation remark: nu_2(T^i(n) - T^i(n')) == j - i for 0 <= i <= j.
"""
import itertools
import random

random.seed(20260721)


def T(n):
    assert isinstance(n, int) and n >= 1, f"T applied outside Z+: {n}"
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def iterates(n, k):
    """[T^0(n), ..., T^k(n)]"""
    xs = [n]
    for _ in range(k):
        xs.append(T(xs[-1]))
    return xs


def word_of(n, k):
    """(v_0(n), ..., v_{k-1}(n))"""
    return tuple(x & 1 for x in iterates(n, k - 1)) if k > 0 else ()


def a_of(n, k):
    return sum(word_of(n, k))


def nu2(x):
    assert x != 0
    j = 0
    while x % 2 == 0:
        x //= 2
        j += 1
    return j


# ---------- T1: one-step equivariance, adversarial edges ----------
crafted = []
# n small, j = 1, m negative pushing n' down to exactly 1:
for n in (3, 5, 9, 101, 2**20 + 1):
    crafted.append((n, 1, -(n - 1) // 2))          # n' = 1
for n in (4, 6, 10, 2**20 + 2):
    crafted.append((n, 1, -(n - 2) // 2))          # n' = 2
crafted += [
    (1, 1, 0), (1, 1, 10**30), (2, 1, 1), (1, 50, 1), (2**60 + 3, 1, -(2**59)),
    (7, 3, -0), (2**40, 40, -1 + 1), (3, 2, 10**18), (2**33 - 1, 33, 5),
]
cnt = 0
for (n, j, m) in crafted:
    np_ = n + 2**j * m
    assert np_ >= 1, (n, j, m)
    assert T(np_) == T(n) + 3 ** (n % 2) * 2 ** (j - 1) * m, ("T1 crafted", n, j, m)
    assert (np_ % 2) == (n % 2), ("T1 parity", n, j, m)
    cnt += 1
for _ in range(30000):
    j = random.randint(1, 60)
    n = random.randint(1, 10**15)
    m = random.randint(-(10**9), 10**9)
    if n + 2**j * m < 1:
        m = -((n - 1) // 2**j)  # clamp to keep n' >= 1: adversarial near-boundary
    np_ = n + 2**j * m
    assert np_ >= 1
    assert T(np_) == T(n) + 3 ** (n % 2) * 2 ** (j - 1) * m, ("T1 rand", n, j, m)
    assert (np_ % 2) == (n % 2)
    cnt += 1
print(f"T1  one-step equivariance OK ({cnt} triples incl. boundary n'=1 cases)")

# ---------- T2: iterated equivariance, all i, incl. k = 0 and odd negative m ----------
cnt = 0
for _ in range(4000):
    k = random.randint(0, 40)
    n = random.randint(1, 10**15)
    m = random.randint(-(10**9), 10**9) | 1 if random.random() < 0.5 else random.randint(-(10**9), 10**9)
    if n + 2**k * m < 1:
        m = -((n - 1) // 2**k)
    O1 = iterates(n, k)
    O2 = iterates(n + 2**k * m, k)
    for i in range(k + 1):
        assert O2[i] == O1[i] + 3 ** a_of(n, i) * 2 ** (k - i) * m, ("T2", n, k, m, i)
    for i in range(k):
        assert O2[i] % 2 == O1[i] % 2, ("T2 bits", n, k, m, i)
    if m % 2 != 0 and m != 0:
        assert (O2[k] - O1[k]) % 2 == 1, ("T2 i=k odd increment", n, k, m)
    cnt += 1
# k = 0 explicitly:
for n in (1, 2, 3, 1000):
    for m in (0, 1, -0, 5, 10**20):
        if n + m >= 1:
            assert iterates(n + m, 0)[0] == n + 3**0 * 2**0 * m
print(f"T2  iterated equivariance + bit preservation OK ({cnt} random (n,k,m), k<=40, k=0 incl.)")

# ---------- T3: bijectivity of pi_k, k = 1..16, exhaustive ----------
for k in range(1, 17):
    words = [word_of(n, k) for n in range(1, 2**k + 1)]
    assert len(set(words)) == 2**k, f"T3 pi_{k} NOT injective"
    if k <= 10:
        assert set(words) == set(itertools.product((0, 1), repeat=k)), f"T3 pi_{k} NOT onto"
print("T3  pi_k bijective for k = 1..16 (exhaustive; image == {0,1}^k verified for k <= 10)")

# ---------- T4: well-definedness under huge lifts ----------
for _ in range(2000):
    k = random.randint(1, 16)
    n = random.randint(1, 2**k)
    t = random.randint(0, 10**30)
    assert word_of(n, k) == word_of(n + 2**k * t, k), ("T4", n, k, t)
print("T4  well-definedness of pi_k OK (2000 lifts with t up to 10^30)")

# ---------- T5: two-lifts flip, exhaustive small k + bigint large k ----------
for k in range(1, 13):
    for n in range(1, 2**k + 1):
        n2 = n + 2**k
        assert word_of(n, k) == word_of(n2, k), ("T5 prefix", k, n)
        Tk, Tk2 = iterates(n, k)[k], iterates(n2, k)[k]
        assert Tk2 == Tk + 3 ** a_of(n, k), ("T5 exact increment", k, n)
        assert (Tk2 - Tk) % 2 == 1 and (Tk2 % 2) == 1 - (Tk % 2), ("T5 flip", k, n)
for _ in range(300):
    k = random.randint(13, 64)
    n = random.randint(1, 10**25)
    n2 = n + 2**k
    assert word_of(n, k) == word_of(n2, k), ("T5b prefix", k, n)
    Tk, Tk2 = iterates(n, k)[k], iterates(n2, k)[k]
    assert Tk2 == Tk + 3 ** a_of(n, k), ("T5b exact", k, n)
    assert (Tk2 % 2) == 1 - (Tk % 2), ("T5b flip", k, n)
print("T5  two-lifts flip + exact 3^{a_k} increment OK (exhaustive k<=12; bigint k<=64)")

# ---------- T6: realization / least representative ----------
for k in range(1, 11):
    inv = {}
    for n in range(1, 2**k + 1):
        w = word_of(n, k)
        assert w not in inv, ("T6 duplicate word", k, n)
        inv[w] = n
    assert len(inv) == 2**k
    for w, nw in inv.items():
        assert 1 <= nw <= 2**k
        for _ in range(3):
            t = random.randint(0, 10**12)
            assert word_of(nw + 2**k * t, k) == w, ("T6 lift", k, w, t)
    # converse: a random positive integer's word points back to its class rep
    for _ in range(200):
        x = random.randint(1, 10**15)
        w = word_of(x, k)
        assert (x - inv[w]) % 2**k == 0, ("T6 converse", k, x)
print("T6  realization: unique n_w in 1..2^k per word; progression + converse OK (k <= 10)")

# ---------- T7: independence, ALL subsets for k <= 8 ----------
for k in range(1, 9):
    words = [word_of(n, k) for n in range(1, 2**k + 1)]
    for mask in range(2**k):
        S = [i for i in range(k) if (mask >> i) & 1]
        for bits in itertools.product((0, 1), repeat=len(S)):
            c = sum(1 for w in words if all(w[i] == b for i, b in zip(S, bits)))
            assert c == 2 ** (k - len(S)), ("T7", k, S, bits, c)
print("T7  independence: exact count 2^(k-|S|) for ALL (S, b), k = 1..8")
for _ in range(500):
    k = random.randint(9, 14)
    S = random.sample(range(k), random.randint(0, k))
    bits = [random.randint(0, 1) for _ in S]
    c = sum(1 for n in range(1, 2**k + 1)
            if all(word_of(n, k)[i] == b for i, b in zip(S, bits)))
    assert c == 2 ** (k - len(S)), ("T7b", k, S, bits, c)
print("T7b independence spot checks OK (500 random (k,S,b), k = 9..14)")

# ---------- T8: necessity / sharpness probes (attempted negations) ----------
# j = 0, odd m: parity NOT preserved -> hypothesis j >= 1 is necessary.
for n in (1, 2, 5, 100):
    for m in (1, 3, -1):
        if n + m >= 1:
            assert (n + m) % 2 != n % 2
# v_i not determined by n mod 2^i: n and n + 2^i agree mod 2^i but v_i flips (T5).
for i in range(1, 13):
    for n in (1, 2, 3, 2**i):
        assert word_of(n, i + 1)[i] != word_of(n + 2**i, i + 1)[i], ("T8 sharp", i, n)
# valuation remark: nu_2(T^i(n) - T^i(n')) == j - i for 0 <= i < j.
cnt = 0
for _ in range(2000):
    k = random.randint(2, 20)
    n, n2 = random.sample(range(1, 2**k + 1), 2)
    d = n - n2
    j = nu2(d)
    if j >= k:
        continue
    O1, O2 = iterates(n, j), iterates(n2, j)
    for i in range(j):
        assert nu2(O1[i] - O2[i]) == j - i, ("T8 val", n, n2, i)
    assert (O1[j] - O2[j]) % 2 == 1, ("T8 split", n, n2)
    assert word_of(n, k)[j] != word_of(n2, k)[j], ("T8 inj bit", n, n2, j)
    cnt += 1
print(f"T8  negation probes: j=0 fails as expected; mod-2^i insufficient for v_i;")
print(f"    valuation-descent + injectivity bit-split OK on {cnt} random pairs")

print("ALL ADVERSARIAL CHECKS PASSED — no counterexample to any part of L-9902 found")
```

**Observed output** (python3, single run, 2026-07-21):

```text
T1  one-step equivariance OK (30018 triples incl. boundary n'=1 cases)
T2  iterated equivariance + bit preservation OK (4000 random (n,k,m), k<=40, k=0 incl.)
T3  pi_k bijective for k = 1..16 (exhaustive; image == {0,1}^k verified for k <= 10)
T4  well-definedness of pi_k OK (2000 lifts with t up to 10^30)
T5  two-lifts flip + exact 3^{a_k} increment OK (exhaustive k<=12; bigint k<=64)
T6  realization: unique n_w in 1..2^k per word; progression + converse OK (k <= 10)
T7  independence: exact count 2^(k-|S|) for ALL (S, b), k = 1..8
T7b independence spot checks OK (500 random (k,S,b), k = 9..14)
T8  negation probes: j=0 fails as expected; mod-2^i insufficient for v_i;
    valuation-descent + injectivity bit-split OK on 2000 random pairs
ALL ADVERSARIAL CHECKS PASSED — no counterexample to any part of L-9902 found
```

This is finite verification supporting, not constituting, the proofs (README §10);
the status upgrade rests on the mathematical reconstruction in §1 above.

### 4. Fixes made

None required. Header fields updated (Status, Reviewing agents, Last updated); no
change to any statement, proof, or audit section. The author's sentence in
"Remaining uncertainty" ("Status is PROPOSED per the packet convention...") is left
in place as an accurate historical record of the author's own action.

### 5. Residual caveats

- The claims are exactly as strong as stated and no stronger. In particular:
  (ii) licenses nothing about the parity bits along a single orbit or about natural
  density on $\mathbb{Z}^+$ without a separate equidistribution step, and (i)/(iii)
  do **not** provide a positive integer realizing an infinite parity word (the inverse
  limit lands in $\mathbb{Z}_2$). Downstream files must cite these limits, as the Gap
  audit already demands.
- The 2-adic remark and the alternative bijection route are unverified side remarks
  (informational; nothing above depends on them). The alternative route's
  non-circularity was checked; its full details were not independently re-proved.
- Not marked INDEPENDENTLY_VERIFIED: that requires review from a separate
  session/agent lineage per project convention.

*Reviewed and signed: fable-02-v2, 2026-07-21.*
