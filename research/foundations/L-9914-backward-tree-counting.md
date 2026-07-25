# L-9914 — Backward-tree counting: an explicit-exponent lower bound on the reaching-1 census

```text
Claim ID: L-9914
Title: Growing a leaf-avoiding S-preimage tree from the root 5: mod-9 leaf control,
       two-child branching with explicit size bounds, and the explicit lower bounds
       #(R ∩ [1,x]) >= (1/3) x^(1/(6-log2 3)) and #(R ∩ [1,x]) >= (1/5) x^(3/10),
       with a root-independent form for the issue #25 rooted-forest program
Status: PROVED
Authoring agent: fable-02-p7
Reviewing agents: fable-02-v15 (adversarial review 2026-07-25: PASS)
Created: 2026-07-21
Last updated: 2026-07-25 (status upgraded after independent adversarial review;
              certificate (C7) repaired — see Verification note)
Dependencies: research/foundations/NOTATION.md (D-9901, D-9903–D-9907, D-9909).
              L-9909 (this author): only L-9909.1 (Syracuse preimage parametrization)
              is used; L-9909 was PROPOSED and under independent re-verification
              (fable-02-v7) when this file was written and is now PROVED, but the
              exact statement used is restated AND re-proved inline (Lemma P) — the
              citation is attributive, not load-bearing. L-9901 (fable-02-p1, then
              PROPOSED, now PROVED): its L-9901.1 contains the C/S reaching-1
              equivalence; here only one implication is needed and it is proved
              inline (Lemma E), so L-9901 is cited as related, not load-bearing.
              Neither status change affects any argument here. See Dependency audit.
Scope: Fully proved, self-contained counting theorems (given NOTATION.md). All
       computations in this file are adversarial tests or worked examples, not proof
       inputs: unlike L-9909.4, NO statement below depends on a computer run. The
       bounds are density-zero lower bounds; see the boxed honesty remark (L-9914.5b).
Related counterexample candidates: none
```

Notation is that of `research/foundations/NOTATION.md`: $C$ (D-9901), $T$ (D-9902),
$\mathrm{odd}(\cdot)$ (D-9903), $S$ and the exponent $a(x) = \nu_2(3x+1)$ (D-9904),
orbits $O_M(n)$ and "reaches 1" (D-9905, with $M^0(n) = n$), counterexample (D-9909),
$\nu_2$ = 2-adic valuation, $\mathbb{Z}^+ = \{1, 2, 3, \dots\}$. Logarithms: $\ln$ is
natural, $\log_2 3 = \ln 3/\ln 2$.

---

## Statement

Let
$$R := \{\, n \in \mathbb{Z}^+ \text{ odd} \ :\ 1 \in O_S(n) \,\}$$
(the odd integers whose Syracuse orbit reaches 1), and for real $x \ge 1$ let
$\#(R \cap [1,x]) := \#\{n \in R : n \le x\}$. Terms in italics (*admissible exponent*,
*leaf*, *children*, *admissible root*, the tree $\mathcal{T}(\rho)$, $N_\rho$,
$\mathrm{cens}_C$, $c_A$, $c^*$, *$S$-periodic*) are defined in the Definitions section.

### L-9914.1 (inputs: preimage parametrization and mod-9 leaf control)

Let $n \in \mathbb{Z}^+$ be odd.

1. **(Preimage parametrization; = L-9909.1, restated and re-proved inline as Lemma P.)**
   The odd $x \in \mathbb{Z}^+$ with $S(x) = n$ are exactly $x_k := (2^k n - 1)/3$ for
   $k$ in the admissible set $A(n) := \{k \ge 1 : 2^k n \equiv 1 \pmod 3\}$; each such
   $x_k$ is an odd positive integer with $\nu_2(3x_k + 1) = k$ exactly, and
   $k \mapsto x_k$ is strictly increasing. Moreover $A(n) = \varnothing$ if $3 \mid n$;
   $A(n) = \{2, 4, 6, \dots\}$ if $n \equiv 1 \pmod 3$; $A(n) = \{1, 3, 5, \dots\}$ if
   $n \equiv 2 \pmod 3$. In particular $x_k < 2^k n/3$, and the minimal admissible
   exponent is $k_0(n) = 2$ resp. $1$ in the last two cases — so $k_0(n) \le 2$
   whenever $3 \nmid n$.
2. **(Leaf criterion.)** For $3 \nmid n$ and $k \in A(n)$: the preimage $x_k$ is a
   *leaf* (i.e. $x_k \equiv 0 \pmod 3$) $\iff 2^k n \equiv 1 \pmod 9$.
3. **(Window lemma / leaf control.)** For $3 \nmid n$ and any three **consecutive**
   admissible exponents $k, k+2, k+4 \in A(n)$: the three residues
   $2^k n,\ 2^{k+2} n,\ 2^{k+4} n \pmod 9$ are pairwise distinct — indeed they are
   $u, 4u, 7u \bmod 9$ with $u := 2^k n \bmod 9$ a unit, and as a set they equal
   $\{1, 4, 7\}$. Hence **exactly one** of the three preimages
   $x_k, x_{k+2}, x_{k+4}$ is a leaf; in particular **at least two are non-leaves**
   (this strengthens the "at most one leaf" step of the task route: it is exactly one).

### L-9914.2 (branching lemma and the preimage tree)

1. **(Two-child branching.)** Every odd $n \in \mathbb{Z}^+$ with $3 \nmid n$ has a
   well-defined pair of *children* $y_1(n) < y_2(n)$: the two smallest **non-leaf**
   $S$-preimages of $n$. They satisfy: both are odd positive integers with
   $3 \nmid y_i$; $S(y_i) = n$; they are the preimages $x_{k}$ for two exponents
   $k \le k_0(n) + 4 \le 6$; and
   $$y_1(n) < \frac{2^{k_0 + 2}}{3}\, n \le \frac{16}{3}\, n, \qquad
     y_2(n) < \frac{2^{k_0 + 4}}{3}\, n \le \frac{64}{3}\, n .$$
2. **(Tree.)** Call $\rho$ an *admissible root* if $\rho$ is odd, $3 \nmid \rho$, and
   $\rho$ is not $S$-periodic. For an admissible root, the complete binary tree
   $\mathcal{T}(\rho)$ (value $\rho$ at the root, and the two children of L-9914.2.1
   below every node) satisfies:
   * every node value is an odd positive integer not divisible by 3, so the
     construction never halts;
   * **all node values are pairwise distinct** (across all generations);
   * generation $g$ carries exactly $2^g$ values, each $\le \rho\,(64/3)^g$;
   * every node value $m$ of generation $g$ satisfies $S^g(m) = \rho$;
   * if $\rho \in R$, then every node value is in $R$.
3. **(Root 5.)** $\rho = 5$ is an admissible root, $5 \in R$ (indeed $S(5) = 1$), and
   $5 = x_4(1) = (2^4 \cdot 1 - 1)/3$ is a non-leaf $S$-preimage of $1$ distinct from
   the degenerate preimage $x_2(1) = 1$ of $1$ (the self-loop that forces us not to
   root at 1). Hence all values of $\mathcal{T}(5)$ lie in $R$. Its first generations:
   children of 5 are $(13, 53)$; generation 2 is $\{17, 277, 35, 565\}$.

### L-9914.3 (Theorem A: generation counting)

Let $c_A := \dfrac{\ln 2}{\ln(64/3)} = \dfrac{1}{6 - \log_2 3}$. Then
$\tfrac{12}{53} < c_A < \tfrac{5}{22}$, with the certified decimal enclosure
$$0.2264985 \;<\; c_A \;<\; 0.2264990$$
(certificates (C1), (C7′) in the Proof; note $c_A \approx 0.22650$, **not** $0.2266$ as
in the task-route parenthetical — flagged, difference $\approx 1.0\cdot 10^{-4}$
[corrected from "$1.4\cdot10^{-4}$" by fable-02-v15: $0.2266 - c_A = 1.0136\cdot10^{-4}$]).
For **all real $x \ge 1$**:
$$\#(R \cap [1, x]) \;\ge\; \tfrac{1}{3}\, x^{\,c_A} \;\ge\; \tfrac{1}{3}\, x^{12/53}.$$

### L-9914.4 (Theorem B, main result: branching functional inequality)

Let $N_5(x) := \#\{\text{node values of } \mathcal{T}(5) \le x\}$. Then:

1. **(Functional inequality.)** For all real $x \ge 5$:
   $$N_5(x) \;\ge\; N_5\!\big(\tfrac{3x}{16}\big) + N_5\!\big(\tfrac{3x}{64}\big) + 1 .$$
2. **(Main bound.)** For **all real $x \ge 1$**:
   $$\#(R \cap [1, x]) \;\ge\; N_5(x)\ \text{ for } x\ge 5, \qquad\text{and}\qquad
     \#(R \cap [1, x]) \;\ge\; \tfrac{1}{5}\, x^{3/10}. $$
   The exponent $3/10$ is an exact rational; no numerically-solved exponent enters the
   theorem. (This realizes the "optional sharper version" of the task route in fully
   rigorous form; it is a THEOREM here, not PARTIAL.)
3. **(Root-independent form, for issue #25.)** For **every** admissible root $\rho$ and
   all real $x \ge \rho$:
   $$\#\{\, m \le x \ :\ m \text{ odd},\ \exists g \ge 0:\ S^g(m) = \rho \,\}
     \;\ge\; \Big(\tfrac{9}{256\,\rho}\Big)^{3/10} x^{3/10}
     \;\ge\; \tfrac{1}{3}\Big(\tfrac{x}{\rho}\Big)^{3/10}.$$
4. **(Method supremum, remark.)** The two-child method of this file supports any
   exponent $c$ with $(3/16)^c + (3/64)^c \ge 1$; the supremum of these is the unique
   root $c^*$ of $(3/16)^{c} + (3/64)^{c} = 1$, with certified enclosure
   $0.3020 < c^* < 0.3021$ (float value $\approx 0.302013$; certificates (C3), (C8)).
   Since $3/10 < c^*$, the rational exponent $3/10$ used above is admissible. This
   matches the task route's "$c^* \approx 0.30$".

### L-9914.5 (corollaries and scope)

Let $\mathrm{cens}_C(x) := \#\{ n \in \mathbb{Z}^+ : n \le x,\ 1 \in O_C(n)\}$.

* **(a) Transfer to $C$, and even multiples.** For all real $x \ge 1$:
  $\mathrm{cens}_C(x) \ge \#(R \cap [1,x]) \ge \tfrac15 x^{3/10}$; and for all real
  $x \ge 16$, adding the disjoint even layers $2^j \cdot R$ ($j = 1, \dots, 4$):
  $$\mathrm{cens}_C(x) \;\ge\; \tfrac{171}{250}\, x^{3/10} \;\ge\; \tfrac{17}{25}\, x^{3/10}.$$
  (One implication of the $C$/$S$ equivalence is needed and is proved inline as
  Lemma E; the full equivalence is L-9901.1, PROPOSED, cited as related.)

* **(b) Honesty box.**

  > **What this does NOT prove.** $x^{3/10}$ (and even the method's supremum
  > $x^{c^*}$, $c^* < 0.31$) is a **density-zero** quantity: $x^{c}/x \to 0$. These
  > theorems are compatible with the Collatz conjecture being true AND with it being
  > false; they say **nothing against the existence of counterexamples** (a
  > counterexample set can perfectly well coexist with $\gg x^{0.3}$ integers reaching
  > 1 — indeed with density-1 many). The literature contains far stronger census
  > bounds (e.g. Krasikov–Lagarias-type $x^{0.84}$ for the $3x+1$ census — literature
  > pointer only, neither used nor re-proved here). The value of this file is (i) the
  > first fully in-repo PROVED lower bound of this kind, and (ii) the reusable,
  > root-independent tree-growth machinery for issue #25. Per D-9909, the file is
  > neutral about which way the conjecture resolves.

* **(c) Root-independence separation (the file's chief service to issue #25).** In the
  proof, the following are **root-independent**: Lemma P (preimage structure), Lemma L
  (leaf control), Lemma B (branching + size bounds), the tree construction, the
  distinctness argument (given non-$S$-periodicity of the root), the functional
  inequality, and the entire counting induction — none of them uses any arithmetic
  property of the root beyond "odd, $3 \nmid \rho$, not $S$-periodic". The **only**
  root-dependent inputs are: (i) the root's size $\rho$ (entering the constant
  $(9/(256\rho))^{3/10}$ only), and (ii) the root's membership in $R$ — used **only**
  to conclude that the counted integers lie in $R$. Consequently issue #25 may apply
  L-9914.4.3 to arbitrary targets: e.g. every element $n$ of a hypothetical nontrivial
  $S$-cycle satisfies $3 \nmid n$ (Lemma L, remark (iv)), so $n$ has a non-leaf,
  non-cycle preimage $m$ which is an admissible root, and the tree from $m$ gives
  $\ge \tfrac13 (x/m)^{3/10}$ odd integers $\le x$ whose orbits enter the cycle;
  likewise any element of a divergent orbit is automatically non-periodic and can
  serve as a root. Observed survivor of the L-9909 sieve is irrelevant here; the two
  files constrain counterexamples from complementary directions.

---

## Definitions

* **$R$**: the set of odd $n \in \mathbb{Z}^+$ whose $S$-orbit reaches 1 (D-9905 with
  $M = S$; $k = 0$ allowed, so $1 \in R$).
* **Admissible exponent / $A(n)$ / $x_k$ / $k_0(n)$**: as in L-9914.1.1 (and
  L-9909.1). $k_0(n) := \min A(n) \in \{1, 2\}$ for $3 \nmid n$ odd.
* **Leaf**: an odd $m \in \mathbb{Z}^+$ with $m \equiv 0 \pmod 3$ — equivalently (by
  Lemma P) an odd $m$ with no $S$-preimage.
* **Children $y_1(n) < y_2(n)$**: the two smallest non-leaf $S$-preimages of $n$
  (well-defined by L-9914.2.1, for $n$ odd, $3 \nmid n$).
* **$S$-periodic**: $x$ with $S^p(x) = x$ for some $p \ge 1$.
* **Admissible root**: odd $\rho \in \mathbb{Z}^+$, $3 \nmid \rho$, not $S$-periodic.
* **Tree $\mathcal{T}(\rho)$**: the map $\nu$ from finite addresses
  $w \in \{1, 2\}^{<\omega}$ to $\mathbb{Z}^+$ with $\nu(\varepsilon) = \rho$ and
  $\nu(w i) = y_i(\nu(w))$ ($i = 1, 2$). *Generation* $g$ = addresses of length $g$.
  "Node values" = the multiset $\{\nu(w)\}$ — proved to be a set (distinctness) for
  admissible roots.
* **$N_\rho(x)$**: $\#\{\text{distinct node values of } \mathcal{T}(\rho) \le x\}$,
  $x$ real.
* **$\mathrm{cens}_C(x)$**: as in L-9914.5.
* **$c_A := \ln 2/\ln(64/3) = 1/(6 - \log_2 3)$**; **$c^*$**: the unique positive root
  of $(3/16)^c + (3/64)^c = 1$ (uniqueness: the left side is strictly decreasing in
  $c$, $2 \to 0$).
* **Certificates (C1)–(C9)**: the explicit integer inequalities listed in the Proof
  and verified (exactly, in integers) by `l9914_certs.py` in Adversarial tests. Each
  is also provable by hand; the script is a check, not a proof input, except that we
  record which hand-checkable inequality each step uses.

---

## Motivation

1. **First in-repo proved lower bound on the reaching-1 census.** The repository so
   far proves structural facts (foundations packet) but no quantitative census bound.
   This file turns L-9909.1's backward-tree structure into an explicit, fully
   quantified counting theorem with rational exponent $3/10$.
2. **Base layer for issue #25 (rooted backward-forest density program).** That program
   wants: "from any root, the $S$-preimage forest grows at a provable polynomial
   rate", with the root's arithmetic isolated from the growth machinery. L-9914.4.3
   and L-9914.5(c) deliver exactly that separation, including the cycle-element and
   divergent-element root cases that matter on the counterexample side. The program's
   eventual target (exponent $\approx 0.84$ via weighted/deeper branching) needs the
   same skeleton with more children per node and sharper leaf bookkeeping; the
   two-child version here is the minimal fully rigorous instance.
3. **Complement to L-9908 (in progress).** L-9908 bounds from above the density of
   integers that avoid early descent (survivor decay); this file bounds from below
   the count of integers that provably reach 1. Together they squeeze the middle
   ground where any counterexample must live.

---

## Proof

Throughout, $S$ maps positive odd integers to positive odd integers (D-9903/D-9904).
We repeatedly use: for odd $x$, $3x + 1$ is even and $\ge 4$, so $a(x) = \nu_2(3x+1) \ge 1$.

### Lemma P (preimage parametrization; restatement and re-proof of L-9909.1)

*Statement:* as in L-9914.1.1.

*Proof (compact; a fuller version with the same content is L-9909.1, PROPOSED, under
independent re-verification — the overlap is intentional per the packet convention in
NOTATION.md).*

($\subseteq$) If $x$ is odd, positive, with $S(x) = n$, put $k := \nu_2(3x+1) \ge 1$.
Then $3x + 1 = 2^k n$ by D-9904 (the odd part times the 2-power), so
$3x = 2^k n - 1$, forcing $2^k n \equiv 1 \pmod 3$ (i.e. $k \in A(n)$) and
$x = (2^k n - 1)/3 = x_k$.

($\supseteq$) If $k \in A(n)$: **integrality** — $3 \mid 2^k n - 1$ by definition of
$A(n)$, so $x_k \in \mathbb{Z}$; **positivity** — $2^k n - 1 \ge 2 \cdot 1 - 1 = 1 > 0$,
so $x_k \ge 1/3$, and being an integer, $x_k \ge 1$; **oddness** — $3 x_k = 2^k n - 1$
is odd (as $k \ge 1$), so $x_k$ is odd; **valuation** — $3 x_k + 1 = 2^k n$ with $n$
odd gives $\nu_2(3x_k + 1) = k$ exactly; hence $S(x_k) = 2^k n / 2^k = n$.

$k \mapsto x_k$ is strictly increasing (numerator strictly increasing in $k$), and
$x_k = (2^k n - 1)/3 < 2^k n / 3$. Since $2 \equiv -1 \pmod 3$,
$2^k n \equiv (-1)^k n \pmod 3$, and $1 \not\equiv -1 \pmod 3$, the case analysis of
$A(n)$ follows: empty if $3 \mid n$; even $k$ (so $k_0 = 2$) if $n \equiv 1$; odd $k$
(so $k_0 = 1$) if $n \equiv 2 \pmod 3$. $\square$

### Lemma L (leaf control mod 9)

*Statement:* L-9914.1.2–3. Additionally: *(iv)* $3 \nmid S(x)$ for every odd $x$
(equivalently: leaves have no preimages — the $3 \mid n$ case of Lemma P).

*Proof.* (ii) $x_k = (2^k n - 1)/3$, so $3 \mid x_k \iff 9 \mid 2^k n - 1 \iff
2^k n \equiv 1 \pmod 9$.

(iii) Let $k, k+2, k+4$ be consecutive admissible exponents (consecutive because
$A(n)$ is exactly an arithmetic progression of step 2 by Lemma P). Put
$u := 2^k n \bmod 9$. Since $\gcd(2, 9) = 1$ and $3 \nmid n$, $u$ is a unit mod 9; and
since $k$ is admissible, $u \equiv 1 \pmod 3$, so $u \in \{1, 4, 7\}$. The other two
residues are $2^{k+2} n \equiv 4u$ and $2^{k+4} n \equiv 16u \equiv 7u \pmod 9$.
*Pairwise distinct:* $4u - u = 3u$ and $7u - 4u = 3u$ are $\not\equiv 0 \pmod 9$
(else $9 \mid 3u$, i.e. $3 \mid u$, contradicting that $u$ is a unit), and
$7u - u = 6u \not\equiv 0 \pmod 9$ (else $3 \mid 2u$, again $3 \mid u$). *The set is
$\{1,4,7\}$:* multiplication by 4 maps $1 \mapsto 4 \mapsto 16 \equiv 7 \mapsto 28
\equiv 1 \pmod 9$, i.e. it acts on $\{1, 4, 7\}$ as the 3-cycle $(1\,4\,7)$; the orbit
of any $u \in \{1,4,7\}$ under it is all of $\{1,4,7\}$, and $\{u, 4u, 7u\}$ is exactly
that orbit. Hence exactly one of the three residues equals $1 \bmod 9$, which by (ii)
says exactly one of $x_k, x_{k+2}, x_{k+4}$ is a leaf; the other two are non-leaves.
(The route memo asked for "at most one"; "exactly one" holds and is what the scripts
test.)

(iv) $2^{a(x)} S(x) = 3x + 1 \equiv 1 \pmod 3$; since $2^{a(x)}$ is a unit mod 3,
$3 \nmid S(x)$. $\square$

### Lemma B (branching)

*Statement:* L-9914.2.1.

*Proof.* Let $n$ be odd, $3 \nmid n$, $k_0 = k_0(n) \le 2$ (Lemma P). The three
smallest preimages are $x_{k_0} < x_{k_0+2} < x_{k_0+4}$, corresponding to the three
smallest (consecutive) admissible exponents. By Lemma L(iii), at least two of them are
non-leaves. Every other preimage $x_k$ ($k \ge k_0 + 6$) exceeds $x_{k_0+4}$, hence
exceeds at least two non-leaf preimages; therefore the two smallest non-leaf preimages
exist and lie in $\{x_{k_0}, x_{k_0+2}, x_{k_0+4}\}$ — children are well defined, with
exponents $\le k_0 + 4 \le 6$. Size bounds, by cases on which candidate (if any) is
the single possible leaf:

* $y_1 \le x_{k_0+2}$: if $x_{k_0}$ is a non-leaf then $y_1 = x_{k_0} \le x_{k_0+2}$;
  otherwise $x_{k_0}$ is the (unique) leaf among the three, so $x_{k_0+2}, x_{k_0+4}$
  are both non-leaves and $y_1 = x_{k_0+2}$. Either way
  $y_1 \le x_{k_0+2} < 2^{k_0+2} n/3 \le 16n/3$ (using $k_0 \le 2$ and Lemma P's
  strict bound). *(Worst case for the route's bookkeeping: leaf $= x_{k_0}$ — this is
  the case that forces the $16/3$ and $64/3$ constants.)*
* $y_2 \le x_{k_0+4} < 2^{k_0+4} n/3 \le 64 n/3$: the two smallest non-leaves are
  among the three candidates, so the larger of them is at most the largest candidate.

Both children are odd, positive, non-leaf ($3 \nmid y_i$) $S$-preimages of $n$ by
construction and Lemma P. $\square$

### Tree construction and its properties (proof of L-9914.2.2–3)

Fix an admissible root $\rho$. Since $\rho$ is odd with $3 \nmid \rho$, Lemma B
applies; since children are again odd non-leaves, by induction on the address length
every $\nu(w)$ is defined, odd, positive, $3 \nmid \nu(w)$ — the construction never
halts. Each child satisfies $S(\text{child value}) = \text{parent value}$, so by
induction on $g$: $S^g(\nu(w)) = \rho$ for $|w| = g$.

**Size bound.** By induction: $\nu(\varepsilon) = \rho \le \rho (64/3)^0$; and
$\nu(wi) \le y_2(\nu(w)) < (64/3)\nu(w) \le \rho(64/3)^{|w|+1}$ by Lemma B.

**Distinctness.** Suppose $\nu(p) = \nu(q) = m$ for addresses $p \neq q$.

* *Different lengths* $g = |p| < g' = |q|$: then $S^{g}(m) = \rho = S^{g'}(m)$, so
  $\rho = S^{g'}(m) = S^{g'-g}(S^{g}(m)) = S^{g'-g}(\rho)$ with $g' - g \ge 1$ — i.e.
  $\rho$ is $S$-periodic, contradicting admissibility.
* *Equal lengths*, by induction on $g = |p| = |q|$: $g = 0$ has a single address. For
  $g \ge 1$ write $p = p'i$, $q = q'j$. Then $\nu(p') = S(m) = \nu(q')$ (children are
  preimages), so by the induction hypothesis $p' = q'$; but then $i \neq j$ would make
  $\nu(p) = y_i(\nu(p'))$ and $\nu(q) = y_j(\nu(p'))$ the two **distinct** children
  ($y_1 < y_2$, Lemma B) — impossible. So $p = q$, a contradiction.

Hence $\nu$ is injective: generation $g$ carries exactly $2^g$ distinct values.

**$R$-membership.** $R$ is closed under $S$-preimages: if $S(x) = n$ and
$S^t(n) = 1$, then $S^{t+1}(x) = 1$. By induction along addresses, $\rho \in R$
implies every node value is in $R$.

**Root 5.** $5$ is odd; $5 \equiv 2 \pmod 3$; $S(5) = \mathrm{odd}(16) = 1$, so
$5 \in R$; and $S^t(5) = 1 \neq 5$ for all $t \ge 1$ (since $S(1) = \mathrm{odd}(4) =
1$), so 5 is not $S$-periodic: 5 is an admissible root with $\mathcal{T}(5) \subseteq
R$. The degeneracy avoided: $1$'s own preimage list starts $x_2(1) = (4-1)/3 = 1$ (a
fixed point — rooting at 1 would repeat values), while $x_4(1) = (16-1)/3 = 5$ is the
first non-degenerate choice; $5$ is moreover a non-leaf. First generations (worked by
hand; the script re-derives them): $5 \equiv 2 \bmod 3$, $k_0 = 1$: candidates
$x_1 = 3$ (leaf), $x_3 = 13$, $x_5 = 53$, so children$(5) = (13, 53)$. For $13 \equiv
1$: $x_2 = 17$, $x_4 = 69 = 3\cdot 23$ (leaf), $x_6 = 277$: children $(17, 277)$. For
$53 \equiv 2$: $x_1 = 35$, $x_3 = 141 = 3 \cdot 47$ (leaf), $x_5 = 565$: children
$(35, 565)$. $\square$

### Certificates

All are exact integer statements; each is verified by `l9914_certs.py` (Adversarial
tests), and (C1)–(C6) are small enough to check by hand.

* **(C1)** $3^5 = 243 < 256 = 2^8$ and $3^{12} = 531441 > 524288 = 2^{19}$. Hence
  $19/12 < \log_2 3 < 8/5$, so $22/5 < 6 - \log_2 3 < 53/12$, so
  $12/53 < c_A < 5/22$.
* **(C2)** $3125 \cdot 2^{22} = 13\,107\,200\,000 \le 31\,381\,059\,609 = 3^{22}$,
  i.e. $5^5 \le (3/2)^{22}$, i.e. $5^{5/22} \le 3/2$; with (C1),
  $5^{c_A} \le 5^{5/22} \le 3/2$.
* **(C3)** $4096 \cdot 121^{10} \le 27 \cdot 200^{10}$ and
  $262144 \cdot 199^{10} \le 27 \cdot 500^{10}$: raising to the 10th power is monotone
  on positives, and $\big((3/16)^{3/10}\big)^{10} = (3/16)^3 = 27/4096$, so these say
  $$(3/16)^{3/10} \ge \tfrac{121}{200}, \qquad (3/64)^{3/10} \ge \tfrac{199}{500},
    \qquad \tfrac{121}{200} + \tfrac{199}{500} = \tfrac{1003}{1000} \ge 1,$$
  hence $\boxed{(3/16)^{3/10} + (3/64)^{3/10} \ge 1}$ — the load-bearing inequality of
  Theorem B (float value $\approx 1.00449$, so the margin is comfortable).
* **(C4)** $1280^3 = 2\,097\,152\,000 \le 7\,119\,140\,625 = 729 \cdot 5^{10}$, i.e.
  $(1280/9)^3 \le 5^{10}$, i.e. $(1280/9)^{3/10} \le 5$.
* **(C5)** $256^3 = 16\,777\,216 \le 43\,046\,721 = 729 \cdot 3^{10}$, i.e.
  $(256/9)^{3/10} \le 3$.
* **(C6)** $8 \cdot 3^{40} \le 100^{10}$, $64 \cdot 13^{10} \le 20^{10}$,
  $512 \cdot 53^{10} \le 100^{10}$, $4096 \cdot 43^{10} \le 100^{10}$: as in (C3)
  these certify $2^{-3/10} \ge \tfrac{81}{100}$, $2^{-6/10} \ge \tfrac{13}{20}$,
  $2^{-9/10} \ge \tfrac{53}{100}$, $2^{-12/10} \ge \tfrac{43}{100}$; and
  $1 + \tfrac{81}{100} + \tfrac{13}{20} + \tfrac{53}{100} + \tfrac{43}{100} =
  \tfrac{342}{100}$.
* **(C7)** $2^{158496} < 3^{100000} < 2^{158497}$ (big-int, script-verified), i.e.
  $1.58496 < \log_2 3 < 1.58497$, giving
  $\tfrac{100000}{441504} < c_A < \tfrac{100000}{441503}$, i.e.
  $0.22649851\ldots < c_A < 0.22649903\ldots$
  > **Reviewer correction (fable-02-v15, 2026-07-25).** (C7) as stated does **not**
  > imply the upper endpoint $0.2264990$ quoted in L-9914.3: its own upper bound is
  > $\tfrac{100000}{441503} = 0.2264990271\ldots > 0.2264990$. (The author's script
  > printed the enclosure with `{:.7f}`, which rounds an *upper* bound **down** —
  > the wrong direction.) The quoted enclosure is nevertheless **true**
  > ($c_A = 0.2264986424\ldots$) and is certified by (C7′) below, which replaces
  > (C7) as the load-bearing certificate for the decimal enclosure of L-9914.3.

* **(C7′)** (reviewer-supplied repair, fable-02-v15) $3^{665} > 2^{1054}$ and
  $3^{306} < 2^{485}$ — two exact integer comparisons on 318- resp. 146-digit numbers
  (these are the continued-fraction convergents $1054/665$ and $485/306$ of
  $\log_2 3$). They give
  $$\tfrac{1054}{665} < \log_2 3 < \tfrac{485}{306}
    \ \Longrightarrow\ \tfrac{665}{2936} < c_A < \tfrac{306}{1351},
    \qquad\text{i.e.}\qquad 0.2264986376 < c_A < 0.2264988898,$$
  which implies $0.2264985 < c_A < 0.2264990$ as stated in L-9914.3 (and more).
  Equivalently, the $P = 10^6$ version of (C7), $2^{1584962} < 3^{10^6} < 2^{1584963}$,
  gives $0.2264986167 < c_A < 0.2264986681$. Both are verified in the Verification
  note. Nothing in Theorems A or B depends on (C7)/(C7′): the theorem-grade exponent
  facts are (C1) ($12/53 < c_A < 5/22$) and (C2).
* **(C8)** Certified rational minorants/majorants of $(3/16)^c + (3/64)^c$ at
  $c = 151/500$ and $c = 3021/10000$ (produced by exact binary search for 10th/500th/
  10000th-root floors, every comparison an integer inequality) give
  $0.302 < c^* < 0.3021$; a coarse hand-scale version, $c^* < 31/100$, follows from
  majorants $149/250$ and $97/250$ with $\tfrac{149+97}{250} = \tfrac{246}{250} < 1$.
* **(C9)** (Not an inequality — the exhaustive window check of Lemma L for all
  $n < 10^4$ with $3 \nmid n$; test only.)

### Proof of L-9914.3 (Theorem A)

All node values of $\mathcal{T}(5)$ lie in $R$ and are distinct. Let real $x \ge 5$
and $g := \lfloor \log_{64/3}(x/5)\rfloor \ge 0$. Every node of generation $g' \le g$
has value $\le 5(64/3)^{g'} \le 5(64/3)^{g} \le x$ (size bound; the last step is the
definition of $g$). Summing generations $0, \dots, g$:
$$\#(R \cap [1,x]) \;\ge\; \sum_{g'=0}^{g} 2^{g'} \;=\; 2^{g+1} - 1 \;\ge\; 2^{g}.$$
Since $g > \log_{64/3}(x/5) - 1$ and $2^{\log_{64/3} y} = y^{\ln 2/\ln(64/3)} =
y^{c_A}$ for $y > 0$ (rewrite via $e^{(\ln 2)(\ln y)/\ln(64/3)}$),
$$2^g \;>\; \tfrac12 (x/5)^{c_A} \;=\; \tfrac12\, 5^{-c_A} x^{c_A} \;\ge\;
  \tfrac12 \cdot \tfrac23\, x^{c_A} \;=\; \tfrac13 x^{c_A},$$
using $5^{c_A} \le 3/2$ (C2; note $c_A < 5/22$ by (C1), so $5^{c_A} < 5^{5/22}$).
This proves the bound for $x \ge 5$. For
$1 \le x < 5$: $1 \in R$ and $1 \le x$, so $\#(R \cap [1,x]) \ge 1$, while
$\tfrac13 x^{c_A} \le \tfrac13 \cdot 5^{c_A} \le \tfrac13 \cdot \tfrac32 = \tfrac12
< 1$ (C2 again). Finally $x^{c_A} \ge x^{12/53}$ for $x \ge 1$ by (C1). The rational
enclosure of $c_A$ is (C1); the decimal enclosure is (C7′). $\square$

### Proof of L-9914.4 (Theorem B)

**1. Functional inequality.** Fix real $x \ge 5$. Write $V$ for the set of node
values of $\mathcal{T}(5)$ (distinct, so "value" $\leftrightarrow$ "node" is a
bijection). Define
$$\varphi_1: \{v \in V : v \le \tfrac{3x}{16}\} \to V,\ v \mapsto y_1(v), \qquad
  \varphi_2: \{v \in V : v \le \tfrac{3x}{64}\} \to V,\ v \mapsto y_2(v).$$
By Lemma B, $\varphi_1(v) < \tfrac{16}{3} v \le x$ and $\varphi_2(v) < \tfrac{64}{3}
v \le x$: both maps land in $\{w \in V : w \le x\}$. $\varphi_1$ is injective (from
$y_1(v) = y_1(v')$ apply $S$: $v = v'$), likewise $\varphi_2$; their ranges are
disjoint (if $y_1(v) = y_2(w)$, applying $S$ gives $v = w$, and then $y_1(v) \ne
y_2(v)$ — contradiction); and no image equals the root value 5 (an image is a child
value, i.e. the value of a non-root address; if it equaled 5 = the root's value, two
distinct addresses would share a value, contradicting distinctness). Since $5 \le x$,
counting the two disjoint image sets plus the root:
$$N_5(x) \;\ge\; N_5\!\big(\tfrac{3x}{16}\big) + N_5\!\big(\tfrac{3x}{64}\big) + 1.$$

**2. Main bound.** Let $A := (1280/9)^{-3/10}$ and $m(x) := \lfloor \log_{16/3}(x/5)
\rfloor$ for $x \ge 5$. We prove by strong induction on $m \ge 1$ the statement
$$P(m):\quad \text{for all real } y \ge 5 \text{ with } m(y) \le m:\quad
  N_5(y) \ge A\, y^{3/10}.$$

*Base $P(1)$:* $m(y) \le 1$ means $5 \le y < 5(16/3)^2 = \tfrac{1280}{9}$. Then
$N_5(y) \ge 1$ (the root, $5 \le y$), while $A y^{3/10} \le A (1280/9)^{3/10} = 1$.

*Step $P(m-1) \Rightarrow P(m)$, $m \ge 2$:* let $m(y) = m \ge 2$; then
$y \ge 5(16/3)^2 = \tfrac{1280}{9}$, so $\tfrac{3y}{64} \ge \tfrac{3}{64} \cdot
\tfrac{1280}{9} = \tfrac{20}{3} \ge 5$ and $\tfrac{3y}{16} \ge \tfrac{80}{3} \ge 5$:
both recursion arguments are in the domain. Their indices:
$m(3y/16) = \lfloor \log_{16/3}(y/5) - 1\rfloor = m - 1$ exactly (the floor of a real
minus an integer), and $m(3y/64) \le m(3y/16) = m - 1$ (monotonicity of $m(\cdot)$,
as $3y/64 < 3y/16$). By the functional inequality and $P(m-1)$:
$$N_5(y) \;\ge\; A\Big(\tfrac{3y}{16}\Big)^{3/10} + A\Big(\tfrac{3y}{64}\Big)^{3/10}
  \;=\; A\, y^{3/10}\Big[\big(\tfrac{3}{16}\big)^{3/10} +
  \big(\tfrac{3}{64}\big)^{3/10}\Big] \;\ge\; A\, y^{3/10},$$
by the boxed certificate (C3). (The "$+1$" of the functional inequality is simply
dropped.) This closes the induction; hence $N_5(x) \ge A x^{3/10}$ for **all** real
$x \ge 5$.

Now $\#(R \cap [1,x]) \ge N_5(x)$ for $x \ge 5$ ($\mathcal{T}(5) \subseteq R$,
distinct values), and $A \ge 1/5$ by (C4), giving $\#(R \cap [1,x]) \ge \tfrac15
x^{3/10}$ for $x \ge 5$. For $1 \le x < 5$: $\#(R \cap [1,x]) \ge 1$ (as $1 \in R$)
while $\tfrac15 x^{3/10} < \tfrac15 \cdot 5^{3/10} < \tfrac15 \cdot 5 = 1$ (since
$5^{3/10} < 5^1$). Done.

**3. Root-independent form.** Repeat parts 1–2 verbatim for an admissible root
$\rho$ (all tree properties of L-9914.2.2 hold for any admissible root):
$N_\rho(x) \ge N_\rho(3x/16) + N_\rho(3x/64) + 1$ for $x \ge \rho$, and the same
induction with base interval $[\rho, \rho(16/3)^2)$ and constant $A_\rho :=
(256\rho/9)^{-3/10}$ (base: $A_\rho y^{3/10} \le A_\rho (\rho(16/3)^2)^{3/10} = 1$;
step: $y \ge \rho(16/3)^2 \Rightarrow 3y/64 \ge \tfrac43 \rho \ge \rho$) gives
$N_\rho(x) \ge A_\rho x^{3/10}$ for all $x \ge \rho$. Every node value $m$ is odd
with $S^g(m) = \rho$ for its generation $g$, so
$$\#\{m \le x : m \text{ odd},\ \exists g \ge 0:\ S^g(m) = \rho\} \;\ge\; N_\rho(x)
  \;\ge\; \Big(\tfrac{9}{256\rho}\Big)^{3/10} x^{3/10} \;\ge\; \tfrac13
  \Big(\tfrac{x}{\rho}\Big)^{3/10},$$
the last step by (C5): $(256/9)^{3/10} \le 3$.

**4. Method supremum (remark).** $c \mapsto (3/16)^c + (3/64)^c$ is strictly
decreasing (both bases lie in $(0,1)$), equals $2$ at $c = 0$ and $\to 0$; so it
crosses 1 at a unique $c^* > 0$, and the induction above works verbatim for every
exponent $c \in (0, c^*]$ in place of $3/10$ (with $A = (1280/9)^{-c}$). (C3) shows
$3/10 \le c^*$; (C8) gives $0.3020 < c^* < 0.3021$. Nothing in Theorems A/B depends
on the value of $c^*$; the remark records what this two-child method can and cannot
reach — in particular it can NOT reach the issue-#25 target $0.84$ without more
children per node (see Suggested next attack). $\square$

### Lemma E (the needed $S \to C$ implication) and proof of L-9914.5(a)

**Lemma E.** *(i)* For odd $x \in \mathbb{Z}^+$ and $0 \le i \le a(x)$:
$C^{1+i}(x) = (3x+1)/2^i$; in particular $S(x) = C^{1 + a(x)}(x) \in O_C(x)$.
*(ii)* For odd $n$ and all $t \ge 0$: $S^t(n) \in O_C(n)$. *(iii)* If odd $n$ reaches
1 under $S$, then $n$ reaches 1 under $C$ — i.e. $R \subseteq \{n : 1 \in O_C(n)\}$.
*(iv)* For $j \ge 0$ and any $m \in \mathbb{Z}^+$: $C^j(2^j m) = m$; hence if $m$
reaches 1 under $C$, so does $2^j m$.

*Proof.* (i) Induction on $i$: $C(x) = 3x + 1$ ($x$ odd). If $C^{1+i}(x) =
(3x+1)/2^i$ with $i < a(x)$, then $\nu_2((3x+1)/2^i) = a(x) - i \ge 1$, so the value
is even and $C$ halves it: $C^{1+i+1}(x) = (3x+1)/2^{i+1}$. At $i = a(x)$ the value
is $S(x)$ (D-9904). (ii) Induction on $t$: $t = 0$ is the index-0 term; if $S^t(n) =
C^s(n)$ (an odd positive integer, as $S$ preserves odd positives), then by (i)
applied at $S^t(n)$: $S^{t+1}(n) = C^{s + 1 + a(S^t(n))}(n)$. (iii) If $S^t(n) = 1$
then $1 \in O_C(n)$ by (ii). (iv) Induction on $j$: $C(2^j m) = 2^{j-1} m$ for
$j \ge 1$ ($2^j m$ even); compose. If $C^u(m) = 1$ then $C^{j+u}(2^j m) = 1$.
$\square$

**Proof of L-9914.5(a).** First bound: every $r \in R \cap [1,x]$ reaches 1 under $C$
(Lemma E(iii)) and is $\le x$, so $\mathrm{cens}_C(x) \ge \#(R \cap [1,x]) \ge
\tfrac15 x^{3/10}$ for $x \ge 1$ (Theorem B). Second bound: for $0 \le j \le 4$ let
$D_j := \{2^j r : r \in R,\ 2^j r \le x\}$. Each element of $D_j$ reaches 1 under $C$
(Lemma E(iv) then (iii): $C^j(2^j r) = r$, then $r$ reaches 1), and the $D_j$ are
pairwise disjoint since every element of $D_j$ has 2-adic valuation exactly $j$ ($r$
odd). Hence for real $x \ge 16$ (so that $x/2^j \ge 1$ for $j \le 4$, allowing
Theorem B at each scale):
$$\mathrm{cens}_C(x) \;\ge\; \sum_{j=0}^{4} \#\big(R \cap [1, x/2^j]\big)
  \;\ge\; \tfrac15 x^{3/10} \sum_{j=0}^{4} 2^{-3j/10}
  \;\ge\; \tfrac15 x^{3/10}\cdot \tfrac{342}{100} \;=\; \tfrac{171}{250} x^{3/10}
  \;\ge\; \tfrac{17}{25} x^{3/10},$$
using the four minorants and the sum of (C6), and $171/250 \ge 170/250 = 17/25$.
(The route memo suggested this "if clean" — it is; the infinite geometric sum is
deliberately truncated at 5 terms to keep every step certified.) $\square$

### Proof of L-9914.5(b), (c)

(b) is a statement of scope, not a mathematical claim; the mathematical content
("the bounds are $o(x)$") is immediate since $3/10 < 1$ and $c^* < 1$.

(c) Inspection of the proofs above: Lemmas P, L, B and the tree construction use only
"$n$ odd, $3 \nmid n$" at each node; distinctness uses only non-$S$-periodicity of
the root; the functional inequality and induction use only the tree properties. The
root's size enters only through the base interval (constant $A_\rho$), and $\rho \in
R$ is used only in the final sentence of Theorem B ("values lie in $R$"), which
L-9914.4.3 drops. The two supplementary facts claimed in the Statement: (i) every
element $n$ of a nontrivial $S$-cycle satisfies $3 \nmid n$, because $n = S(n')$ for
its cycle predecessor $n'$ and Lemma L(iv) applies; then $n$ has children (Lemma B),
of which at most one can be the cycle predecessor, so a non-cycle non-leaf preimage
$m$ exists; $m$ is not $S$-periodic (an $S$-periodic point's forward orbit is exactly
its cycle, which would force $m$ to lie on the cycle through $n$ — it does not, since
$S(m) = n$ and $m$ is not the cycle predecessor of $n$... more directly: if
$S^p(m) = m$ then $m$ lies on an $S$-cycle, and applying $S$: $n = S(m)$ lies on the
same cycle, whose element mapping to $n$ is unique on the cycle — namely the cycle
predecessor $n' \ne m$; but on a cycle, $S(m) = n = S(n')$ with $m, n'$ both on the
cycle forces $m = n'$ by injectivity of $S$ restricted to a cycle — contradiction).
Injectivity of $S$ on a cycle: on a cycle of period $p$, $S^{p-1}$ is a two-sided
inverse of $S$. So $m$ is an admissible root. (ii) An element of a divergent
$S$-orbit (D-9907) is not $S$-periodic, since periodic orbits are finite, hence
bounded. If additionally $3 \mid$ such an element, pass to any of its non-leaf
preimages? — no: a divergent-orbit element $x$ with $3 \mid x$ has NO preimages
(Lemma P) but is itself a valid *starting point*; to use it as a tree root one
instead roots at $x$'s successor's other preimages; simplest correct statement: every
element of the FORWARD orbit $S^t(x)$, $t \ge 1$, satisfies $3 \nmid S^t(x)$ (Lemma
L(iv)) and is non-periodic (its orbit is a tail of a divergent orbit, still
divergent, hence unbounded, hence non-periodic), so all of them are admissible roots.
$\square$

---

## Dependency audit

Used from `NOTATION.md` (definitions only): D-9901 ($C$; Lemma E, $\mathrm{cens}_C$),
D-9903/D-9904 ($\mathrm{odd}$, $S$, $a(x)$; everywhere), D-9905 (orbits, reaches 1,
$M^0 = \mathrm{id}$; definitions of $R$, $\mathrm{cens}_C$, Lemma E), D-9906 (not
essentially used; parity language only), D-9907 (divergent — only in L-9914.5(c)'s
remark), D-9909 (neutrality framing only). D-9902 ($T$) is not used.

In-repo results:

* **L-9909.1** (author: fable-02-p7 = this author; status PROPOSED, under independent
  re-verification by fable-02-v7): the preimage parametrization. **Choice made:** the
  exact statement used is restated as L-9914.1.1 and fully re-proved inline as Lemma
  P; therefore L-9914 remains valid regardless of the outcome of L-9909's review, and
  the citation is for provenance and cross-checking only. (L-9909.1's Part 3 mod-9
  cycle overlaps Lemma L; Lemma L is re-proved here from scratch.)
* **L-9901.1** (author: fable-02-p1; status PROPOSED, not yet reviewed): the full
  three-way reaching-1 equivalence for $C/T/S$. **Choice made (as invited by the
  coordinator): the inline one-implication proof (Lemma E) is load-bearing**; L-9901.1
  is cited as the stronger related statement. If/when L-9901 reaches
  INDEPENDENTLY_VERIFIED, a reviewer may replace Lemma E by a citation; nothing else
  changes.
* No other repo file is used. No literature result is used (the $x^{0.84}$ mention in
  the honesty box is a pointer, not an input). The certificates (C1)–(C8) are proved
  by the stated integer inequalities; the scripts merely re-verify them.

Internal order (acyclic): Lemma P → Lemma L → Lemma B → tree properties → Theorems
A, B → root-independent form; Lemma E independent; corollary (a) uses Theorem B +
Lemma E; (c) uses Lemmas P, L, B + tree properties.

## Gap audit

Search against README §8:

* *Hidden finiteness / extrapolation*: none — Theorems A and B are proved for all
  real $x \ge 1$ by induction, with no computational input; every computation in this
  file is a test. (Contrast deliberately drawn with L-9909.4, which does consume a
  finite verification.)
* *Unjustified induction*: the three inductions (tree properties over address
  length; distinctness over equal address length; $P(m)$ over the scale index $m$)
  have explicit bases and steps. The scale induction's well-foundedness is exactly
  the identity $m(3y/16) = m(y) - 1$ — proved via $\lfloor t - 1 \rfloor = \lfloor t
  \rfloor - 1$, an exact integer shift, not an approximation — plus monotonicity for
  the second argument.
* *Boundary cases*: $x$ real (not just integer) throughout; base intervals
  $[5, 1280/9)$ and $[\rho, \rho(16/3)^2)$ include their left endpoint where
  $N \ge 1$ needs the root counted ($\rho \le x$); the extension to $1 \le x < 5$ is
  written out with certificates; the degenerate preimage $x_2(1) = 1$ of the node 1
  (self-loop) is excluded by the choice of root 5 together with distinctness (a value
  repeat at two depths forces $S$-periodicity of the root); $k_0 \in \{1,2\}$ is
  proved, not assumed; the "which candidate is the leaf" case split in Lemma B covers
  all three positions (worst case: leaf $= x_{k_0}$).
* *Nonuniform estimates*: the constants $16/3$, $64/3$, $A$, $A_\rho$ are uniform
  over all nodes/roots as marked; no "for large $x$" step occurs anywhere.
* *Assumptions equivalent to the conjecture*: none; the theorems are unconditional.
  The honesty box states explicitly that the results do not bear on the existence of
  counterexamples.
* *Circularity*: Lemma P re-proves the cited L-9909.1; Lemma E re-proves the needed
  direction of L-9901.1; hence no dependence on unreviewed files. Within the file the
  dependency order is acyclic (see audit).
* *Symbolic object vs integer*: integrality, positivity, oddness of every constructed
  preimage are proved in Lemma P and re-checked per node by the scripts; tree values
  are integers by construction.
* *Route corrections (obligations from the task)*: (1) $c_A \approx 0.22650$, not
  $0.2266$ — certified enclosure (C7); (2) "at most one leaf per window" is actually
  "exactly one" (Lemma L(iii)); (3) "count $\ge 2^g$ per generation" is exactly
  $2^g$; (4) the optional sharper version is delivered as a full theorem with the
  RATIONAL exponent $3/10$ ($\le c^*$), avoiding any numerically-defined exponent in
  a theorem statement; (5) the geometric-sum improvement is delivered in truncated,
  fully certified form ($171/250$, $x \ge 16$).

## Adversarial tests

Two scripts, Python 3 (stdlib only; every decision is an exact integer or `Fraction`
comparison; floats appear only in display strings). Stored in the session scratchpad;
full code and verbatim output below. All tests PASS.

### Script 1: `l9914_tree.py` — the tree itself, and the theorems against the census

Checks: (1) builds $\mathcal{T}(5)$ to generation 12 (8191 nodes), verifying per node:
admissibility/integrality/oddness/valuation/preimage identity for all three
candidates, **exactly one leaf** among them, children = two smallest non-leaf
preimages re-derived by an independent wider $k$-scan, size bounds $3y_1 < 16n$,
$3y_2 < 64n$, exponents $\le k_0 + 4$; (2) exactly $2^g$ values per generation, all
odd non-leaves, none $= 1$, globally distinct, and $3^g v \le 5 \cdot 64^g$ (exact
form of $v \le 5(64/3)^g$); (3) every one of the 8191 node values has $S$-orbit
reaching 1 (full check, not a sample — this exceeds the task's "full to generation
~8"); (4) the functional inequality in restricted-depth form $N_{\le 12}(x) \ge
N_{\le 11}(3x/16) + N_{\le 11}(3x/64) + 1$ (the faithful finite-tree consequence of
the injection argument — the unrestricted form is a statement about the infinite
tree) at 101 scales $x = 5(6/5)^i \le 5(64/3)^6$; (5) the true census: verifies by
$S$-descent + strong induction that EVERY odd $n \le 10^6$ is in $R$, and by
$C$-descent that every $n \le 10^6$ reaches 1 under $C$, then checks the three proved
bounds against the true counts at $x = 10^3, \dots, 10^6$ **as exact integer
inequalities** (e.g. $x^{12} < (3\,\mathrm{cens})^{53}$), confirming the required
huge slack.

```python
#!/usr/bin/env python3
# l9914_tree.py -- L-9914: build the preimage tree from root 5 to generation 12;
# verify every structural claim of L-9914.1/2/3/4 on it; verify the restricted-depth
# functional inequality; verify the counting theorems against the true census.
# Agent: fable-02-p7. Python 3 stdlib only; exact arithmetic in all decisions.
import bisect
from fractions import Fraction

def nu2(m):
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k

def S(x):
    y = 3 * x + 1
    return y >> nu2(y)

def k0(n):                       # minimal admissible exponent (n odd, 3 must not divide n)
    return 2 if n % 3 == 1 else 1

def pre(n, k):
    return (2 ** k * n - 1) // 3

def children(n):
    """Two smallest non-leaf S-preimages of n, with full per-node verification."""
    a = k0(n)
    ks = [a, a + 2, a + 4]
    cand = [pre(n, k) for k in ks]
    for k, x in zip(ks, cand):
        assert (2 ** k * n) % 3 == 1, (n, k)          # admissibility
        assert (2 ** k * n - 1) % 3 == 0, (n, k)      # integrality
        assert x % 2 == 1 and x >= 1, (n, k)          # odd, positive
        assert nu2(3 * x + 1) == k, (n, k)            # exact valuation
        assert S(x) == n, (n, k)                      # really a preimage
    assert sum(1 for x in cand if x % 3 == 0) == 1, (n, cand)   # EXACTLY one leaf
    nl = [(x, k) for x, k in zip(cand, ks) if x % 3 != 0]
    # independent wider-scan check: the two smallest non-leaf preimages overall
    allnl, k = [], a
    while len(allnl) < 6:
        x = pre(n, k)
        if x % 3 != 0:
            allnl.append(x)
        k += 2
    assert [x for x, _ in nl] == allnl[:2], (n, nl, allnl[:2])
    (y1, kk1), (y2, kk2) = nl
    assert y1 < y2
    assert 3 * y1 < 16 * n and 3 * y2 < 64 * n        # size bounds (Lemma B)
    assert kk1 <= a + 2 and kk2 <= a + 4
    return y1, y2

# ---- build tree from root 5 --------------------------------------------------
GMAX = 12
root = 5
assert root % 2 == 1 and root % 3 == 2 and S(root) == 1        # 5 in R, non-leaf
assert S(root) != root and S(S(root)) == 1                     # 5 not S-periodic
gens = [[root]]
values = {root}
for g in range(GMAX):
    nxt = []
    for n in gens[g]:
        y1, y2 = children(n)
        for y in (y1, y2):
            assert y not in values, ("duplicate value", y)      # global distinctness
            values.add(y)
            nxt.append(y)
    gens.append(nxt)

for g, lst in enumerate(gens):
    assert len(lst) == 2 ** g                                  # exactly 2^g per generation
    for v in lst:
        assert v != 1
        assert v % 2 == 1 and v % 3 != 0
        assert 3 ** g * v <= 5 * 64 ** g                       # v <= 5*(64/3)^g, exact

# every node's S-orbit reaches 1 (full check, all 8191 nodes to generation 12)
for g, lst in enumerate(gens):
    for v in lst:
        x, c = v, 0
        while x != 1:
            x = S(x)
            c += 1
            assert c < 10 ** 4, (g, v)
print(f"tree OK: {sum(len(l) for l in gens)} nodes to generation {GMAX}; "
      f"all odd, non-leaf, distinct, size-bounded; all S-orbits reach 1")
print("children(5) =", children(5), "; generation 2 =", sorted(gens[2]))
print("largest node at generation 12 =", max(gens[12]))

# ---- restricted-depth functional inequality  N(x) >= N(3x/16) + N(3x/64) + 1 --
sorted12 = sorted(values)
sorted11 = sorted(v for g in range(GMAX) for v in gens[g])
def N12(x): return bisect.bisect_right(sorted12, x)
def N11(x): return bisect.bisect_right(sorted11, x)
cnt = 0
x = Fraction(5)
top = 5 * Fraction(64, 3) ** 6
while x <= top:
    lhs = N12(x)
    rhs = N11(x * Fraction(3, 16)) + N11(x * Fraction(3, 64)) + 1
    assert lhs >= rhs, (float(x), lhs, rhs)
    cnt += 1
    x *= Fraction(6, 5)
print(f"functional inequality N(x) >= N(3x/16) + N(3x/64) + 1: verified at {cnt} scales "
      f"(x = 5*(6/5)^i up to 5*(64/3)^6)")

# ---- true census vs the proved bounds ---------------------------------------
LIM = 10 ** 6
for n in range(3, LIM + 1, 2):        # S-descent for every odd n: orbit dips below n
    x, c = S(n), 0
    while x >= n:
        x = S(x)
        c += 1
        assert c < 10 ** 4, n
# by strong induction over odd n (base 1), every odd n <= LIM is in R
def censR(x): return (x + 1) // 2 if x % 2 == 1 else x // 2   # #odd <= x

for n in range(2, LIM + 1):           # C-descent for every n (as in X-9901)
    x, c = n, 0
    while x >= n:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        c += 1
        assert c < 10 ** 5, n
# so every n <= LIM reaches 1 under C: censC(x) = floor(x) for x <= LIM

print(f"{'x':>8} | {'#R∩[1,x]':>9} | {'ThmA (1/3)x^(12/53)':>19} | "
      f"{'ThmB (1/5)x^(3/10)':>18} | {'censC':>8} | {'Cor (17/25)x^(3/10)':>18}")
for e in (3, 4, 5, 6):
    x = 10 ** e
    cR, cC = censR(x), x
    assert x ** 12 < (3 * cR) ** 53               # ThmA bound < censR  (exact)
    assert x ** 3 < (5 * cR) ** 10                # ThmB bound < censR  (exact)
    assert 17 ** 10 * x ** 3 <= 25 ** 10 * cC ** 10   # Cor bound <= censC (exact)
    print(f"{x:>8} | {cR:>9} | {x**(12/53)/3:>19.2f} | {x**0.3/5:>18.2f} | "
          f"{cC:>8} | {17/25*x**0.3:>18.2f}")
print("census comparisons: all proved bounds hold with large slack (exact integer checks)")
```

Output (verbatim; runtime ~1.6 s):

```text
tree OK: 8191 nodes to generation 12; all odd, non-leaf, distinct, size-bounded; all S-orbits reach 1
children(5) = (13, 53) ; generation 2 = [17, 35, 277, 565]
largest node at generation 12 = 43086887646773
functional inequality N(x) >= N(3x/16) + N(3x/64) + 1: verified at 101 scales (x = 5*(6/5)^i up to 5*(64/3)^6)
       x |  #R∩[1,x] | ThmA (1/3)x^(12/53) | ThmB (1/5)x^(3/10) |    censC | Cor (17/25)x^(3/10)
    1000 |       500 |                1.59 |               1.59 |     1000 |               5.40
   10000 |      5000 |                2.68 |               3.17 |    10000 |              10.78
  100000 |     50000 |                4.52 |               6.32 |   100000 |              21.50
 1000000 |    500000 |                7.61 |              12.62 |  1000000 |              42.91
census comparisons: all proved bounds hold with large slack (exact integer checks)
```

Interpretation: the true census in this range is $\sim x/2$ (every odd $n \le 10^6$
is in $R$ — a finite verification consistent with L-9909's X-9901), vastly above the
proved bounds, as required ("any violation = fatal bug": none). The generation-2
values and children of 5 match the hand computation in the Proof. The largest
generation-12 node $43{,}086{,}887{,}646{,}773 \approx 4.3\cdot 10^{13}$ sits well
under the proved ceiling $5(64/3)^{12} \approx 4.4 \cdot 10^{16}$.

### Script 2: `l9914_certs.py` — certificates and exhaustive leaf control

Checks: the integer certificates (C1)–(C8) exactly as stated in the Proof (including
the big-int comparison $2^{158496} < 3^{100000} < 2^{158497}$ and the exact
binary-search enclosure of $c^*$), and (C9): for **every** $n < 10^4$ with
$3 \nmid n$ (even $n$ included for the pure mod-9 arithmetic; odd $n$ additionally
for the preimage statement), for each of the 10 windows of three consecutive
admissible exponents $k < 25$: $\{2^k n \bmod 9\} = \{1, 4, 7\}$ (pairwise distinct),
exactly one leaf per window, and the leaf criterion $x_k \equiv 0 \bmod 3
\iff 2^k n \equiv 1 \bmod 9$.

```python
#!/usr/bin/env python3
# l9914_certs.py -- L-9914: all integer certificates for the exponent/constant
# inequalities, exhaustive mod-9 leaf-control check, and rigorous enclosures of
# c_A = 1/(6 - log2 3) and of the branching exponent c* with (3/16)^c*+(3/64)^c* = 1.
# Agent: fable-02-p7. Python 3 stdlib only; every decision is an exact integer test.
from fractions import Fraction

ok = True
def chk(name, cond):
    global ok
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

print("== C1: enclosure 12/53 < c_A < 5/22  (via 3^12 > 2^19, 3^5 < 2^8) ==")
chk("3^5 = 243 < 256 = 2^8         (=> log2 3 < 8/5  => c_A < 5/22)", 3**5 < 2**8)
chk("3^12 = 531441 > 524288 = 2^19 (=> log2 3 > 19/12 => c_A > 12/53)", 3**12 > 2**19)

print("== C2: 5^(c_A) <= 5^(5/22) <= 3/2  (beta = 1/3 in Theorem A; also x<5 extension) ==")
chk("3125 * 2^22 <= 3^22", 3125 * 2**22 <= 3**22)

print("== C3: (3/16)^(3/10) + (3/64)^(3/10) >= 1  via minorants 121/200 and 199/500 ==")
chk("4096 * 121^10 <= 27 * 200^10   (=> (3/16)^(3/10) >= 121/200)",
    4096 * 121**10 <= 27 * 200**10)
chk("262144 * 199^10 <= 27 * 500^10 (=> (3/64)^(3/10) >= 199/500)",
    262144 * 199**10 <= 27 * 500**10)
chk("121/200 + 199/500 = 1003/1000 >= 1",
    Fraction(121, 200) + Fraction(199, 500) == Fraction(1003, 1000))

print("== C4: (1280/9)^(3/10) <= 5  (constant A >= 1/5 in Theorem B) ==")
chk("1280^3 <= 729 * 5^10", 1280**3 <= 729 * 5**10)

print("== C5: (256/9)^(3/10) <= 3  (root-independent constant 1/3) ==")
chk("256^3 <= 729 * 3^10", 256**3 <= 729 * 3**10)

print("== C6: corollary minorants for 2^(-3j/10), j = 1..4, and the 342/100 sum ==")
chk("8 * 3^40 <= 100^10      (=> 2^(-3/10) >= 81/100)", 8 * 3**40 <= 100**10)
chk("64 * 13^10 <= 20^10     (=> 2^(-6/10) >= 13/20)", 64 * 13**10 <= 20**10)
chk("512 * 53^10 <= 100^10   (=> 2^(-9/10) >= 53/100)", 512 * 53**10 <= 100**10)
chk("4096 * 43^10 <= 100^10  (=> 2^(-12/10) >= 43/100)", 4096 * 43**10 <= 100**10)
s = 1 + Fraction(81,100) + Fraction(13,20) + Fraction(53,100) + Fraction(43,100)
chk(f"1 + 81/100 + 13/20 + 53/100 + 43/100 = {s} = 342/100; (1/5)*(342/100) = 171/250 >= 17/25",
    s == Fraction(342,100) and Fraction(1,5)*s >= Fraction(17,25))

print("== C7: tight enclosure of c_A = 1/(6 - log2 3) ==")
t = 3 ** 100000
chk("3^100000 > 2^158496  (=> log2 3 > 1.58496)", t > 2**158496)
chk("3^100000 < 2^158497  (=> log2 3 < 1.58497)", t < 2**158497)
lo, hi = Fraction(10**5, 6*10**5 - 158496), Fraction(10**5, 6*10**5 - 158497)
print(f"     => {float(lo):.7f} < c_A < {float(hi):.7f}   "
      f"(so c_A = 0.226498..., i.e. ~0.22650, NOT 0.2266)")

print("== C8: enclosure of the branching exponent c* ==")
def pow_lower(num, den, p, q, prec=10**6):
    """Largest integer a <= prec with (a/prec)^q <= (num/den)^p, for num < den.
    Certificate of the returned bound: a^q * den^p <= prec^q * num^p (exact)."""
    lo_, hi_ = 0, prec
    R = prec**q * num**p
    while lo_ < hi_:
        mid = (lo_ + hi_ + 1) // 2
        if mid**q * den**p <= R:
            lo_ = mid
        else:
            hi_ = mid - 1
    return lo_

PREC = 10**6
def f_bounds(p, q):
    a1 = pow_lower(3, 16, p, q, PREC)
    a2 = pow_lower(3, 64, p, q, PREC)
    lower = Fraction(a1, PREC) + Fraction(a2, PREC)          # certified lower bd of f(p/q)
    upper = Fraction(a1 + 1, PREC) + Fraction(a2 + 1, PREC)  # certified upper bd
    return lower, upper

lowf, upf = f_bounds(3, 10)
chk(f"f(3/10) >= {float(lowf):.6f} > 1 (independent re-check of C3)", lowf > 1)
lowf, upf = f_bounds(151, 500)
chk(f"f(151/500 = 0.302) >= {float(lowf):.7f} > 1  (=> c* > 0.302)", lowf > 1)
lowf, upf = f_bounds(3021, 10000)
chk(f"f(3021/10000 = 0.3021) <= {float(upf):.7f} < 1  (=> c* < 0.3021)", upf < 1)
lowf, upf = f_bounds(31, 100)
chk(f"f(31/100) <= {float(upf):.6f} < 1  (coarse: c* < 0.31)", upf < 1)
print("     => 0.3020 < c* < 0.3021 (f strictly decreasing in c); float root ~ 0.302013")

print("== C9: exhaustive mod-9 leaf control, all n < 10^4 with 3 not dividing n ==")
bad = 0
for n in range(1, 10**4):
    if n % 3 == 0:
        continue
    adm = [k for k in range(1, 25) if (2**k * n) % 3 == 1]
    if adm != list(range(adm[0], 25, 2)):
        bad += 1
    for i in range(len(adm) - 2):
        tr = adm[i:i+3]
        us = [(2**k * n) % 9 for k in tr]
        if len(set(us)) != 3 or set(us) != {1, 4, 7} or sum(u == 1 for u in us) != 1:
            bad += 1
        if n % 2 == 1:                       # preimage statement (odd n only)
            xs = [(2**k * n - 1) // 3 for k in tr]
            if sum(x % 3 == 0 for x in xs) != 1:
                bad += 1
            for k, x in zip(tr, xs):
                if (x % 3 == 0) != ((2**k * n) % 9 == 1):
                    bad += 1
chk("windows of 3 consecutive admissible k: {2^k n mod 9} = {1,4,7}, exactly one leaf; "
    "leaf <=> 2^k n = 1 mod 9   (all n < 10^4, 3 not dividing n; 10 windows each)",
    bad == 0)

print()
print("ALL CERTIFICATES:", "PASS" if ok else "FAIL")
```

Output (verbatim; runtime ~0.3 s):

```text
== C1: enclosure 12/53 < c_A < 5/22  (via 3^12 > 2^19, 3^5 < 2^8) ==
  [PASS] 3^5 = 243 < 256 = 2^8         (=> log2 3 < 8/5  => c_A < 5/22)
  [PASS] 3^12 = 531441 > 524288 = 2^19 (=> log2 3 > 19/12 => c_A > 12/53)
== C2: 5^(c_A) <= 5^(5/22) <= 3/2  (beta = 1/3 in Theorem A; also x<5 extension) ==
  [PASS] 3125 * 2^22 <= 3^22
== C3: (3/16)^(3/10) + (3/64)^(3/10) >= 1  via minorants 121/200 and 199/500 ==
  [PASS] 4096 * 121^10 <= 27 * 200^10   (=> (3/16)^(3/10) >= 121/200)
  [PASS] 262144 * 199^10 <= 27 * 500^10 (=> (3/64)^(3/10) >= 199/500)
  [PASS] 121/200 + 199/500 = 1003/1000 >= 1
== C4: (1280/9)^(3/10) <= 5  (constant A >= 1/5 in Theorem B) ==
  [PASS] 1280^3 <= 729 * 5^10
== C5: (256/9)^(3/10) <= 3  (root-independent constant 1/3) ==
  [PASS] 256^3 <= 729 * 3^10
== C6: corollary minorants for 2^(-3j/10), j = 1..4, and the 342/100 sum ==
  [PASS] 8 * 3^40 <= 100^10      (=> 2^(-3/10) >= 81/100)
  [PASS] 64 * 13^10 <= 20^10     (=> 2^(-6/10) >= 13/20)
  [PASS] 512 * 53^10 <= 100^10   (=> 2^(-9/10) >= 53/100)
  [PASS] 4096 * 43^10 <= 100^10  (=> 2^(-12/10) >= 43/100)
  [PASS] 1 + 81/100 + 13/20 + 53/100 + 43/100 = 171/50 = 342/100; (1/5)*(342/100) = 171/250 >= 17/25
== C7: tight enclosure of c_A = 1/(6 - log2 3) ==
  [PASS] 3^100000 > 2^158496  (=> log2 3 > 1.58496)
  [PASS] 3^100000 < 2^158497  (=> log2 3 < 1.58497)
     => 0.2264985 < c_A < 0.2264990   (so c_A = 0.226498..., i.e. ~0.22650, NOT 0.2266)
== C8: enclosure of the branching exponent c* ==
  [PASS] f(3/10) >= 1.004486 > 1 (independent re-check of C3)
  [PASS] f(151/500 = 0.302) >= 1.0000270 > 1  (=> c* > 0.302)
  [PASS] f(3021/10000 = 0.3021) <= 0.9998060 < 1  (=> c* < 0.3021)
  [PASS] f(31/100) <= 0.982407 < 1  (coarse: c* < 0.31)
     => 0.3020 < c* < 0.3021 (f strictly decreasing in c); float root ~ 0.302013
== C9: exhaustive mod-9 leaf control, all n < 10^4 with 3 not dividing n ==
  [PASS] windows of 3 consecutive admissible k: {2^k n mod 9} = {1,4,7}, exactly one leaf; leaf <=> 2^k n = 1 mod 9   (all n < 10^4, 3 not dividing n; 10 windows each)

ALL CERTIFICATES: PASS
```

Note on the earlier draft of this script: its first run printed a hand-typed
annotation "$c_A = 0.2264963...$" alongside the certified enclosure
$(0.2264985, 0.2264990)$ — the annotation (a display string, not a certificate) was
wrong and has been corrected to $0.226498...$; the certified enclosure itself was
produced by the integer comparisons and was correct on both runs. Recorded here per
the preserve-false-starts rule; it is also a live illustration of why decimals in
this file are only trusted when certified.

## Remaining uncertainty

* The author's confidence in Lemmas P, L, B, E, the tree properties, and Theorem A is
  high: all steps are short, and every one has a matching exhaustive or structural
  machine check. The most intricate argument is Theorem B's scale induction; its two
  delicate points — the exact floor shift $m(3y/16) = m(y) - 1$ and the domain checks
  $3y/64 \ge 5$ (resp. $\ge \rho$) at the induction step — are each written out, but
  a reviewer should re-derive both independently.
* The functional inequality's injection argument tacitly identifies nodes with values
  via distinctness; a reviewer should confirm no circularity between distinctness and
  the child maps (there is none: distinctness is proved before and independently of
  the counting).
* The certificates (C7), (C8) rely on big-integer machine arithmetic (a
  ~47,000-digit comparison; exact $n$-th-root binary search). They are conceptually
  trivial but not hand-checkable; (C1)–(C6) are hand-checkable and suffice for every
  theorem statement — (C7)/(C8) support only the decimal enclosures quoted for $c_A$
  and $c^*$. A reviewer wanting theorem-grade decimals should rerun or reimplement
  them.
* The route memo's constant $16/3$ for the smaller child is used at face value; note
  it is NOT claimed that $y_1 < 4n/3$ (that fails exactly when $x_{k_0}$ is the
  leaf), and the file's bounds only ever use $y_1 < 16n/3$, $y_2 < 64n/3$. A sharper
  treatment (three candidate positions for the leaf give a better average) is
  possible and deliberately not attempted here — see next attack.

## Suggested next attack

1. **More children (toward issue #25's $x^{0.84}$).** Use $W$ consecutive admissible
   exponents ($W$ large): Lemma L generalizes — among any $W$ consecutive admissible
   preimages, exactly $\lceil W/3 \rceil$-ish are leaves (the mod-9 residues cycle
   with period 3, by the same $(1\,4\,7)$-cycle argument), so $\approx \tfrac23 W$
   children of sizes $< 2^{k_0 + 2W - 2} n/3$ are available. The branching equation
   becomes $\sum_{i \in I} (3 \cdot 2^{-k_0-2i})^{c} \ge 1$ with $|I| = \lceil 2W/3
   \rceil$; already $W = 4$ should push $c$ past $0.34$ (unverified — compute first).
   The correct target of optimization is the FULL admissible fan: heuristically the
   density-weighted equation $\sum_{i \ge 1,\ i \not\equiv i_0 (3)} (3 \cdot
   4^{-i})^{c} = 1$; determine its root rigorously with the (C8) machinery.
2. **Average-case leaf position.** Track the mod-9 state of each node (which
   candidate is the leaf) and run a 3-state weighted branching recursion; this
   replaces the worst case (leaf $= x_{k_0}$) by the true distribution and improves
   $c^*$ at zero structural cost. The state transition table is computable from
   L-9909.1's Part 3 table.
3. **Verifier probes.** Attack the floor-shift step with $x$ an exact power of
   $16/3$ times 5; attack distinctness by searching two addresses with equal values
   in $\mathcal{T}(5)$ beyond generation 12; attack Lemma B by hunting an $n$ whose
   two smallest non-leaf preimages do NOT lie among the first three candidates (by
   Lemma L none exists — any hit refutes Lemma L); recompute (C3) by an independent
   method (e.g. interval arithmetic).
4. **Merge layer for issue #25.** Combine L-9914.4.3 (this file) with L-9909.2's
   closure of the counterexample set: if a counterexample exists, its forward orbit
   supplies infinitely many admissible roots, each spawning $\gg (x/\rho)^{3/10}$
   odd integers that also fail to reach 1 — a quantitative lower bound on the
   counterexample census, i.e. the same machinery cuts BOTH ways. Writing that dual
   statement (with the root-size bookkeeping done honestly) is the natural next
   lemma, and is exactly the shape issue #25 needs.

---

*Signed: fable-02-p7, 2026-07-21.*

---

## Verification note (fable-02-v15, 2026-07-25)

**Verdict: PASS — the mathematics is sound; status upgraded PROPOSED → PROVED.**
One genuine (non-load-bearing) defect was found and repaired: certificate **(C7) does
not imply the upper endpoint of the decimal enclosure it is cited for**. The endpoint
is nevertheless true, and a replacement certificate (C7′) is supplied above. Two
further cosmetic corrections are recorded. No theorem statement changes.

This review was conducted independently per README §13: every statement was restated
and re-proved from NOTATION.md before the author's proof was read line-by-line, and
every computation below comes from scripts I wrote from the *statements alone*
(`v15_verify.py`, `v15_probe2.py`; full code and verbatim output at the end of this
note). L-9909 and L-9901 are now both PROVED, but neither is load-bearing here —
Lemma P and Lemma E are self-contained re-proofs, and I checked them as such.

### 1. Independent restatement and reconstruction

**Lemma P (L-9914.1.1).** Reconstructed. For odd $x$ with $S(x)=n$, put
$k:=\nu_2(3x+1)\ge1$; D-9904 gives $3x+1=2^kn$, hence $3\mid 2^kn-1$ and $x=x_k$.
Conversely for $k\in A(n)$: $x_k\in\mathbb{Z}$ by definition of $A(n)$;
$2^kn-1\ge1$ forces $x_k\ge1/3$, so $x_k\ge1$ as an integer; $3x_k=2^kn-1$ is odd
(as $k\ge1$) so $x_k$ is odd; $3x_k+1=2^kn$ with $n$ odd gives $\nu_2(3x_k+1)=k$
*exactly*, hence $S(x_k)=n$. Monotonicity in $k$ and $x_k<2^kn/3$ are immediate.
$2\equiv-1\pmod 3$ gives $2^kn\equiv(-1)^kn$, so $A(n)=\varnothing$ / even $k$ /
odd $k$ according to $3\mid n$ / $n\equiv1$ / $n\equiv2 \pmod 3$, and $k_0\le2$.
**Verified independently** by brute force: for every odd $n\le4000$ the *set of all*
odd $x\le2\cdot10^5$ with $S(x)=n$ (computed by forward iteration, with no use of the
formula) equals $\{x_k:k\in A(n),\,x_k\le2\cdot10^5\}$, and $A(n)$ has exactly the
claimed shape.

**Lemma L (L-9914.1.2–3) — the mod-9 leaf control, checked in full.**
*(ii)* $3\mid x_k\iff 9\mid 2^kn-1\iff 2^kn\equiv1\pmod9$: correct, since
$x_k=(2^kn-1)/3$.
*(iii)* By Lemma P, $A(n)$ is an arithmetic progression of step 2, so "three
consecutive admissible exponents" are $k,k+2,k+4$. With $u:=2^kn\bmod 9$:
admissibility gives $u\equiv1\pmod3$, and $\{r\bmod 9: r\equiv1 \bmod 3\}=\{1,4,7\}$,
so $u\in\{1,4,7\}$ — **in particular $\gcd(u,3)=1$, which is exactly $\gcd(u,9)=1$**,
so the task's remark is right that $\gcd(v,3)=1$ suffices (the two conditions coincide
mod 9). The hypothesis $3\nmid n$ is what delivers this, together with $\gcd(2,9)=1$;
the author's hypothesis handling is correct and the "unit mod 9" step is in fact
*redundant* given $u\equiv1\pmod3$ (harmless).
$2^{k+2}n\equiv4u$, $2^{k+4}n\equiv16u\equiv7u$. **Order of $4$ mod $9$ is exactly 3**
($4,\,16\equiv7,\,64\equiv1$) — machine-confirmed — so multiplication by 4 acts on
$\{1,4,7\}$ as the 3-cycle $(1\,4\,7)$, and $\{u,4u,7u\}=\{u,4u,4^2u\}$ is the full
orbit $\{1,4,7\}$. Pairwise distinctness also follows directly: $4u-u=3u$ and
$7u-u=6u$ are $\not\equiv0\pmod9$ because $3\nmid u$.
Since $\{u,4u,7u\}=\{1,4,7\}$ **as a set**, exactly one member is $\equiv1\pmod 9$;
by (ii) **exactly one** of $x_k,x_{k+2},x_{k+4}$ is a leaf. The author's
strengthening from "at most one" to **"exactly one" is correct and is what the proof
actually establishes** — the set equality is doing the work, not just injectivity.
*(iv)* $2^{a(x)}S(x)=3x+1\equiv1\pmod3$ and $2^{a(x)}$ is a unit mod 3, so
$3\nmid S(x)$. Correct.
**Exhaustive machine check (mine, independent):** all $n<10^4$ with $3\nmid n$,
**83 325 windows** of three consecutive admissible exponents: residues are exactly
$(u,4u,7u)=\{1,4,7\}$, **exactly one** $\equiv1\pmod 9$ in every single window (never
zero, never two), and for odd $n$ the leaf criterion $x_k\equiv0\pmod3\iff
2^kn\equiv1\pmod9$ holds in every case. **0 exceptions.**

**Lemma B (L-9914.2.1) — two-child branching.** Reconstructed: the three smallest
preimages are $x_{k_0}<x_{k_0+2}<x_{k_0+4}$; Lemma L(iii) makes exactly one a leaf,
so exactly two of the three are non-leaves; every further preimage ($k\ge k_0+6$)
exceeds $x_{k_0+4}$, hence exceeds both of them — so the two smallest non-leaf
preimages exist and lie among the first three. The worst-case bookkeeping is as the
author states: if the leaf is $x_{k_0}$ then $y_1=x_{k_0+2}$, otherwise
$y_1=x_{k_0}\le x_{k_0+2}$; either way $y_1\le x_{k_0+2}<2^{k_0+2}n/3\le 16n/3$ and
$y_2\le x_{k_0+4}<2^{k_0+4}n/3\le 64n/3$, using $k_0\le2$.
**Independently checked** with my own selection rule (a wide $k$-scan that assumes
nothing about *where* the two smallest non-leaves sit): for all odd $n\le20000$ with
$3\nmid n$ the wide-scan children coincide with the first-three-candidates children,
are odd non-leaves, satisfy $S(y_i)=n$, $3y_1<16n$, $3y_2<64n$, and have exponents
$\le k_0+4\le6$. **0 exceptions.** All three leaf positions genuinely occur, with
essentially equal frequency (pos 0: 2222, pos 1: 2222, pos 2: 2223 out of 6667), and
**pos 0 (leaf $=x_{k_0}$) is the worst case that forces the constants $16/3$, $64/3$**
— confirmed by exhibiting $n\in\{5,7,23,25,41,\dots\}$ where $y_1\ge 4n/3$, i.e. the
naive $4n/3$ bound is genuinely false. The file's "Remaining uncertainty" note on
this point is accurate.

**Tree properties (L-9914.2.2–3).** All four inductions re-derived:
never-halting (children are odd non-leaves, so Lemma B reapplies); $S^g(\nu(w))=\rho$;
the size bound $\nu(w)\le\rho(64/3)^{|w|}$; and **distinctness**, whose two cases I
re-derived: *different lengths* $g<g'$ give
$\rho=S^{g'}(m)=S^{g'-g}(S^g(m))=S^{g'-g}(\rho)$ with $g'-g\ge1$, i.e. $\rho$ is
$S$-periodic — excluded by admissibility; *equal lengths* by induction on $g$, since
$S(\nu(p'i))=\nu(p')$ forces $p'=q'$ and then $y_1\ne y_2$ forces $i=j$. Correct.
Root 5: $5$ odd, $5\equiv2\ (3)$, $S(5)=\mathrm{odd}(16)=1$ so $5\in R$, and
$S^t(5)=1\ne5$ for all $t\ge1$ since $S(1)=1$ — so **non-$S$-periodicity of 5 is
unconditional**; no appeal to "there are no nontrivial cycles" is made anywhere
(I checked this specifically, as it would be an assumption equivalent to part of the
conjecture). Hand values $(13,53)$ and $\{17,35,277,565\}$ reproduce.

**Theorem A (L-9914.3).** Reconstructed with $g=\lfloor\log_{64/3}(x/5)\rfloor\ge0$
for $x\ge5$: generations $0..g$ contribute $2^{g+1}-1\ge2^g$ distinct values, all
$\le5(64/3)^g\le x$; $g>\log_{64/3}(x/5)-1$ gives $2^g>\tfrac12(x/5)^{c_A}\ge
\tfrac13x^{c_A}$ via $5^{c_A}\le5^{5/22}\le3/2$. The $1\le x<5$ tail is handled.
Correct.

**Theorem B (L-9914.4).** *Functional inequality:* the two maps $\varphi_i$ land in
$\{w\in V:w\le x\}$ by the $16/3$ / $64/3$ bounds; each is injective **because $S$ is
a left inverse** ($S(y_i(v))=v$); the ranges are disjoint because $y_1(v)=y_2(w)$
would give $v=w$ after applying $S$ and then $y_1(v)=y_2(v)$, contradicting
$y_1<y_2$; and **the "+1" is legitimate** because every image is the value of a
*non-empty* address while $5=\nu(\varepsilon)$, so an image equal to 5 would give two
distinct addresses with equal value — excluded by distinctness, which is proved
*before and independently of* any counting (no circularity: I traced the dependency
order Lemma P → L → B → tree/distinctness → functional inequality → induction, and it
is acyclic). Hence the two images and $\{5\}$ are three pairwise-disjoint subsets of
$\{w\in V:w\le x\}$, of sizes $N_5(3x/16)$, $N_5(3x/64)$, $1$. Correct.
*Scale induction:* $A=(1280/9)^{-3/10}$, $m(y)=\lfloor\log_{16/3}(y/5)\rfloor$.
Base $P(1)$: $m(y)\le1\iff 5\le y<5(16/3)^2=1280/9$, where $N_5(y)\ge1\ge Ay^{3/10}$.
Step: $m(y)=m\ge2\Rightarrow y\ge5(16/3)^2=1280/9$, so $3y/16\ge80/3\ge5$ and
$3y/64\ge20/3\ge5$ (both domain checks hold, with slack); **the floor shift**
$m(3y/16)=\lfloor\log_{16/3}(y/5)-1\rfloor=m-1$ is an exact integer shift of the
floor argument, not an approximation, and $m(3y/64)\le m(3y/16)=m-1$ by monotonicity.
Then (C3) closes the step. Correct.
**I re-verified the floor shift adversarially at 443 exact rational points**,
including $y=5(16/3)^j$ *exactly* on the boundary for $j=0..8$ and
$\pm10^{-6}$, $\pm1/3$ perturbations of those boundaries (the author's own suggested
probe), plus 400 geometric samples: $m(3y/16)=m(y)-1$ and $m(3y/64)\le m(y)-1$ and
$3y/64\ge5$ hold **without exception**, and $m(y)\le1\iff y<1280/9$ exactly.
*Root-independent form:* base interval $[\rho,\rho(16/3)^2)=[\rho,256\rho/9)$,
$A_\rho=(256\rho/9)^{-3/10}$, step domain $3y/64\ge\tfrac43\rho\ge\rho$. Correct; the
final $(256/9)^{3/10}\le3$ is (C5).
*$c^*$ remark:* $c\mapsto(3/16)^c+(3/64)^c$ is strictly decreasing from 2 to 0, so
$c^*$ is unique; $3/10<c^*$ by (C3). Correct.

**Corollary L-9914.5(a) and Lemma E.** Lemma E(i)–(iv) re-derived (the induction
$C^{1+i}(x)=(3x+1)/2^i$ for $i\le a(x)$ is valid because $\nu_2((3x+1)/2^i)=a(x)-i\ge1$
keeps the value even). The layers $D_j=2^j\cdot R$, $j=0..4$, are pairwise disjoint
since $\nu_2$ is exactly $j$, and $x\ge16$ is exactly what makes $x/2^j\ge1$ so
Theorem B applies at each scale. $\sum_{j=0}^42^{-3j/10}\ge342/100$ by (C6), and
$\tfrac15\cdot\tfrac{342}{100}=\tfrac{171}{250}\ge\tfrac{17}{25}$. Correct.

**Honesty box L-9914.5(b): present, accurate, and correctly scoped.** It is a boxed
remark inside the Statement (not buried), it states that $x^{3/10}$ and even
$x^{c^*}$ are **density-zero** ($x^c/x\to0$, true since $c^*<0.3021<1$), that the
theorems are compatible with the conjecture being true *and* with it being false, and
that they say **nothing against the existence of counterexamples**. I confirm all of
that is mathematically accurate: nothing in the file constrains the complement of $R$
in any way, and the Krasikov–Lagarias $x^{0.84}$ mention is explicitly flagged as a
literature pointer that is neither used nor re-proved. D-9909 neutrality is respected.

**Root-independence separation L-9914.5(c).** What the proofs support is exactly what
is claimed, with one precision caveat (see §4). The cycle-element argument is correct:
every element $n$ of a nontrivial $S$-cycle has $3\nmid n$ by Lemma L(iv) applied to
its cycle predecessor $n'$; $n$ has two children, at most one of which is $n'$, so
some child $m\ne n'$ exists; $m$ is not $S$-periodic, because otherwise $n=S(m)$ would
lie on $m$'s cycle — the same cycle as $n$'s, since a point lies on at most one cycle
— and $S$ restricted to a cycle of period $p$ is a bijection (inverse $S^{p-1}$),
forcing $m=n'$. So $m$ is an admissible root. The divergent-orbit case, after the
author's own visible self-correction, ends at the correct statement: every
$S^t(x)$ with $t\ge1$ satisfies $3\nmid S^t(x)$ (Lemma L(iv)) and is non-periodic
(a tail of a divergent orbit is unbounded), hence is an admissible root.

### 2. Independent computation

Scripts written by me from the statements only; exact integer / `Fraction`
comparisons in every decision (floats only in display strings). Scratchpad:
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/`.

**Tree statistics ($\mathcal{T}(5)$, my own wide-scan selection rule).**

| quantity | generation 12 | generation 14 | generation 17 |
|---|---|---|---|
| nodes ($=2^{g+1}-1$) | 8 191 | 32 767 | 262 143 |
| distinct values | 8 191 | 32 767 | 262 143 |
| duplicates found | 0 | 0 | 0 |
| all odd, $3\nmid v$, $v\ne1$ | yes | yes | yes |
| $3^g v\le 5\cdot64^g$ (exact size bound) | holds | holds | holds |
| $S^g(v)=5$ for every node | holds | holds | holds |
| $S$-orbit of every node reaches 1 | all 8 191 | all 32 767 | — |
| step bounds $3y_1<16n$, $3y_2<64n$ | 0 violations | 0 violations | 0 violations |

Largest generation-12 value $=43\,086\,887\,646\,773$ (reproduces the author's), well
under the proved ceiling $5(64/3)^{12}\approx4.44\cdot10^{16}$. Longest $S$-orbit to 1
among all 32 767 nodes: 15 steps. Children of 5 $=(13,53)$; generation 2
$=\{17,35,277,565\}$ — both reproduce the hand computation.
Minimum value per generation $g=0..17$:
$5,13,17,11,7,19,25,65,43,59,79,203,139,185,127,169,239,295$ — **note this is not
monotone** (generation 4 contains 7 < the root 5), so the finiteness of $N_5(x)$ does
*not* follow from the size bound; it follows from distinctness (distinct positive
integers $\le x$ number at most $\lfloor x\rfloor$). See caveat §4(c).

**Functional inequality.** Verified in the faithful depth-truncated form
$N_{\le14}(x)\ge N_{\le13}(3x/16)+N_{\le13}(3x/64)+1$ at **225 exact rational scales**
$x=5(11/10)^i$ up to $5(64/3)^7$ — 0 failures (the task asked for $\ge100$).

**Theorem bounds against the tree itself.** $N_5(x)\ge Ax^{3/10}$,
$N_5(x)\ge\tfrac15x^{3/10}$ and $N_5(x)\ge\tfrac13x^{12/53}$ verified at 65 scales
$x=5(3/2)^i$ up to $10^{12}$, as exact integer inequalities, using only the depth-14
truncation as a lower bound for $N_5$. Root-independent form verified for **20 other
admissible roots** ($\rho=7,11,\dots,97$): trees to generation 11 have all-distinct
values and $N_\rho(x)\ge(9/(256\rho))^{3/10}x^{3/10}\ge\tfrac13(x/\rho)^{3/10}$ at
every scale up to $10^{10}$ — 0 failures.

**CENSUS COMPARISON (the fatal-if-violated check).** I recomputed $R$ below $10^6$
from scratch ($S$-descent for every odd $n$, no reuse of the author's code) and
$\mathrm{cens}_C$ by $C$-descent. Every odd $n\le10^6$ is in $R$ and every $n\le10^6$
reaches 1 under $C$ (finite verification, **not** a proof input). All three proved
bounds hold, as exact integer inequalities, with enormous slack:

| $x$ | true $\#(R\cap[1,x])$ | Thm A $\tfrac13x^{12/53}$ | slack | Thm B $\tfrac15x^{3/10}$ | slack | $\mathrm{cens}_C(x)$ | Cor $\tfrac{17}{25}x^{3/10}$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $10^3$ | 500 | 1.59 | 314× | 1.59 | 315× | 1 000 | 5.40 |
| $10^4$ | 5 000 | 2.68 | 1 864× | 3.17 | 1 577× | 10 000 | 10.78 |
| $10^5$ | 50 000 | 4.52 | 11 067× | 6.32 | 7 906× | 100 000 | 21.50 |
| $10^6$ | 500 000 | 7.61 | 65 705× | 12.62 | 39 622× | 1 000 000 | 42.91 |

Exact forms checked: $x^{12}<(3\,\mathrm{cens}_R)^{53}$,
$x^{3}<(5\,\mathrm{cens}_R)^{10}$, $17^{10}x^{3}\le25^{10}\mathrm{cens}_C^{10}$.
**No violation anywhere; the bounds are far below the truth, exactly as a
density-zero lower bound should be.**

**Exponent enclosures, re-certified with my own big integers.**
(C1)–(C6), (C8) all reproduce exactly. $(3/16)^{3/10}+(3/64)^{3/10}\in
[1.004486,1.004488]>1$, so $3/10<c^*$; $f(0.302)>1$ and $f(0.3021)<1$ give
$0.3020<c^*<0.3021$ — confirmed. **(C7) fails to certify what it is cited for** —
see §3.

### 3. Fixes applied

* **(C7) — genuine defect, repaired.** L-9914.3 states the "certified decimal
  enclosure" $0.2264985<c_A<0.2264990$ and cites (C7). But (C7)
  ($2^{158496}<3^{100000}<2^{158497}$) yields only
  $\tfrac{100000}{441504}<c_A<\tfrac{100000}{441503}$, i.e.
  $0.2264985141\ldots<c_A<0.2264990271\ldots$ — the upper bound
  $0.22649902718\ldots$ is **larger** than the quoted $0.2264990$, so the quoted
  upper endpoint is *not implied*. Root cause: the author's script printed the
  enclosure with `{:.7f}`, which rounds an **upper** bound **down** (the wrong
  direction) — the same class of display error the file's own "Note on the earlier
  draft" warns about. The quoted enclosure is nonetheless **true**
  ($c_A=0.2264986424607\ldots$), so this is a certificate gap, not a false claim, and
  no theorem is affected (Theorems A/B use only (C1)–(C6)). **Fix:** a new
  certificate **(C7′)** has been added to the Certificates section —
  $3^{665}>2^{1054}$ and $3^{306}<2^{485}$ (the continued-fraction convergents
  $1054/665$ and $485/306$ of $\log_2 3$; 318- and 146-digit comparisons), giving
  $\tfrac{665}{2936}<c_A<\tfrac{306}{1351}$, i.e.
  $0.2264986376<c_A<0.2264988898$, which implies the quoted enclosure with room to
  spare. A second independent repair is recorded: the $P=10^6$ version of the
  author's own certificate, $2^{1584962}<3^{10^6}<2^{1584963}$, giving
  $0.2264986167<c_A<0.2264986681$. (C7) is retained with a boxed reviewer
  correction; the author's verbatim script and output are left untouched per the
  preserve-false-starts rule.
* **Arithmetic slip, corrected.** L-9914.3's parenthetical said the gap to the task
  route's $0.2266$ is "$\approx1.4\cdot10^{-4}$"; it is
  $0.2266-c_A=1.01358\cdot10^{-4}\approx1.0\cdot10^{-4}$. Corrected in place.
* **Two clarifications added** (no mathematical change): the (C2) step in the proof of
  Theorem A now records explicitly that $5^{c_A}<5^{5/22}$ needs $c_A<5/22$ from (C1);
  and the proof of Theorem A now cites (C1) for the rational enclosure and (C7′) for
  the decimal one.
* **Header refreshed.** Dependencies now record that L-9909 and L-9901 have since
  reached PROVED; this changes nothing, since Lemma P and Lemma E are self-contained
  re-proofs and the citations remain attributive.

### 4. Caveats and non-defects (recorded, no action needed)

(a) **The "exactly one leaf" strengthening is fully justified.** It rests on the *set
equality* $\{u,4u,7u\}=\{1,4,7\}$, not merely on pairwise distinctness; I confirmed
the orbit argument and checked all 83 325 windows below $10^4$. Note the strengthening
is not needed for any downstream step — Lemma B only consumes "at least two
non-leaves" — so even if it failed the file's theorems would survive. It does not
fail.

(b) **Root-independence, precise scope.** L-9914.5(c) says the "only root-dependent
inputs" are the root's size and its membership in $R$. Strictly there is a third:
the root's **non-$S$-periodicity**, without which distinctness (hence everything)
collapses. The file does name it — it is folded into "admissible root" and is
explicitly listed two sentences earlier ("the distinctness argument (given
non-$S$-periodicity of the root)") — so the passage is not misleading, but a reader
of L-9914.4.3 alone should note that admissibility is a genuine hypothesis on $\rho$.
Concretely: the degeneracy is real. My run confirms $\mathrm{children}(1)=(1,5)$, so
rooting at the $S$-periodic point 1 puts the value 1 at both depth 0 and depth 1,
distinctness fails, and the entire count collapses. The exclusion via "$\rho$ not
$S$-periodic" is exactly the right hypothesis, and for $\rho=5$ it is verified
unconditionally from $S(5)=1$, $S(1)=1$ — **no hidden assumption equivalent to
"no nontrivial cycles" enters anywhere.** For the issue-#25 applications the
hypothesis is likewise discharged (a non-predecessor child of a cycle element, or any
forward iterate of a divergent orbit), so the separation claimed for issue #25 is
exactly what the proofs support.

(c) **Finiteness of $N_\rho(x)$ is implicit but immediate.** Node values are *not*
monotone in the generation (generation 4 of $\mathcal{T}(5)$ contains 7, below the
root 5), so finiteness of $N_\rho(x)$ does not follow from the size bound. It follows
at once from distinctness: distinct positive integers $\le x$ number at most
$\lfloor x\rfloor$. Worth one sentence in a future revision; the proofs as written are
not affected (the functional inequality compares finite cardinalities either way).

(d) **The two child subtrees are genuinely disjoint** in the sense the proof needs —
the argument is about the *images* of $\varphi_1,\varphi_2$ (single child steps), not
about whole subtrees, and disjointness there is a one-line consequence of $S$ being a
left inverse plus $y_1\ne y_2$. Global distinctness of the whole tree is proved
separately and is not used circularly.

(e) **(C8) is script-only, as the author states.** I reproduced it with my own exact
$n$-th-root bisection at precision $10^{-6}$; it supports only the decimal enclosure
of $c^*$, which no theorem uses.

(f) **Not re-checked, and not needed:** the "Suggested next attack" estimates
($W=4$ pushing $c$ past $0.34$, the density-weighted equation) are explicitly flagged
"unverified" by the author and are not claims of this file.

### 5. Attempts to negate

I looked specifically for: a window with zero or two leaves below $10^4$ (none);
an $n\le20000$ whose two smallest non-leaf preimages escape the first three candidates
(none — by Lemma L none can exist, and a hit would have refuted Lemma L); a duplicate
value in $\mathcal{T}(5)$ out to generation 17 / 262 143 nodes (none); a boundary $y$
where the floor shift $m(3y/16)=m(y)-1$ or the domain condition $3y/64\ge5$ fails
(none, over 443 exact rational points including exact powers of $16/3$); a scale where
the functional inequality fails (none in 225); a root $\rho$ among 20 admissible ones
where the root-independent constant fails (none); and — the fatal test — a
$x\in\{10^3,\dots,10^6\}$ where a proved bound exceeds the true census (none; the
slack is $3\cdot10^2$ to $6.6\cdot10^4$). The only thing that broke was the (C7)
certificate arithmetic, repaired above. **Strengthening available but correctly not
claimed:** the same induction runs for any $c\le c^*$, so $x^{0.302}$ is reachable
with a certified-rational $c$ such as $151/500$; the file deliberately keeps the
clean rational $3/10$ and records $c^*$ only as a remark. That is the right call.

### 6. Verbatim code and output

**Script 1 — `v15_verify.py`** (fable-02-v15; reconstruction of every claim from the
statements alone).

```python
#!/usr/bin/env python3
# fable-02-v15 -- INDEPENDENT adversarial verification of L-9914.
# Written from the STATEMENTS only (no reuse of the author's scripts).
# Every decision is an exact integer / Fraction comparison. Floats only in display.
import bisect
from fractions import Fraction

FAIL = []
def chk(name, cond, extra=""):
    if not cond:
        FAIL.append(name)
    print(f"  [{'PASS' if cond else '*** FAIL ***'}] {name}{(' ' + extra) if extra else ''}")

def nu2(m):
    k = 0
    while m % 2 == 0:
        m //= 2; k += 1
    return k

def S(x):                      # D-9904
    y = 3 * x + 1
    return y >> nu2(y)

# ---------------------------------------------------------------- Lemma P probes
print("== Lemma P: preimage parametrisation (independent brute-force cross-check) ==")
# Brute force: for each odd n <= 4000, find ALL odd x <= 200000 with S(x)=n, and
# compare with the parametrised list {x_k : k in A(n), x_k <= 200000}.
XMAX = 200000
inv = {}
for x in range(1, XMAX + 1, 2):
    inv.setdefault(S(x), []).append(x)
bad = 0
for n in range(1, 4001, 2):
    brute = sorted(inv.get(n, []))
    param = []
    k = 1
    while True:
        v = 2 ** k * n
        if (v - 1) // 3 > XMAX and k > 2:
            break
        if v % 3 == 1:
            xk = (v - 1) // 3
            if xk <= XMAX:
                param.append(xk)
            else:
                break
        k += 1
    param.sort()
    if brute != param:
        bad += 1
    # A(n) shape
    A = [k for k in range(1, 40) if (2 ** k * n) % 3 == 1]
    if n % 3 == 0:
        if A != []:
            bad += 1
    else:
        k0 = 2 if n % 3 == 1 else 1
        if A != list(range(k0, 40, 2)):
            bad += 1
        # per-k properties
        for k in A[:6]:
            xk = (2 ** k * n - 1) // 3
            if not (xk >= 1 and xk % 2 == 1 and nu2(3 * xk + 1) == k and S(xk) == n
                    and 3 * xk < 2 ** k * n):
                bad += 1
chk("all odd n<=4000: brute-force S-preimage set == {x_k : k in A(n)}; A(n) is the "
    "step-2 AP starting at k0 in {1,2} (empty iff 3|n); each x_k odd, positive, "
    "nu2(3x_k+1)=k, S(x_k)=n, x_k < 2^k n/3", bad == 0)

# ---------------------------------------------------------- Lemma L: mod-9 control
print("== Lemma L: mod-9 leaf control, exhaustive for all n < 10^4 with 3 nmid n ==")
# order of 4 mod 9
ord4 = 1
t = 4 % 9
while t != 1:
    t = (t * 4) % 9; ord4 += 1
chk("multiplicative order of 4 mod 9 equals 3", ord4 == 3, f"(4,16=7,64=1 mod 9)")
chk("16 = 7 mod 9 and 4^2 = 7 mod 9", 16 % 9 == 7 and (4 * 4) % 9 == 7)
chk("{u,4u,7u} = {1,4,7} for every u in {1,4,7}",
    all(set([u % 9, 4 * u % 9, 7 * u % 9]) == {1, 4, 7} for u in (1, 4, 7)))
# the residues mod 9 that are = 1 mod 3 are exactly {1,4,7}
chk("residues r mod 9 with r = 1 mod 3 are exactly {1,4,7}",
    {r for r in range(9) if r % 3 == 1} == {1, 4, 7})
# and each is a unit mod 9 (gcd(.,3)=1 suffices)
chk("each of 1,4,7 is a unit mod 9 (gcd with 3 is 1)",
    all(__import__("math").gcd(u, 9) == 1 for u in (1, 4, 7)))

bad = 0
wins = 0
for n in range(1, 10 ** 4):
    if n % 3 == 0:
        continue
    k0 = 2 if n % 3 == 1 else 1
    A = list(range(k0, 30, 2))
    for i in range(len(A) - 2):
        k1, k2, k3 = A[i], A[i + 1], A[i + 2]
        us = [(2 ** k * n) % 9 for k in (k1, k2, k3)]
        wins += 1
        if len(set(us)) != 3 or set(us) != {1, 4, 7}:
            bad += 1
        if sum(1 for u in us if u == 1) != 1:
            bad += 1
        if us[1] != (4 * us[0]) % 9 or us[2] != (7 * us[0]) % 9:
            bad += 1
        if n % 2 == 1:
            xs = [(2 ** k * n - 1) // 3 for k in (k1, k2, k3)]
            if sum(1 for x in xs if x % 3 == 0) != 1:      # EXACTLY one leaf
                bad += 1
            for k, x in zip((k1, k2, k3), xs):
                if (x % 3 == 0) != ((2 ** k * n) % 9 == 1):   # leaf criterion
                    bad += 1
chk(f"all n<10^4 with 3 nmid n, all {wins} windows of 3 consecutive admissible k: "
    "residues = (u,4u,7u) = {1,4,7}; EXACTLY one = 1 mod 9; leaf <=> 2^k n = 1 mod 9",
    bad == 0)
# adversarial: is "at most one" ever strict (i.e. zero leaves in a window)?
chk("no window with ZERO leaves and no window with TWO leaves was found "
    "(strengthening 'exactly one' confirmed)", bad == 0)

# ------------------------------------------------- Lemma B: my own selection rule
print("== Lemma B: two-child selection by an INDEPENDENT wide scan ==")
def children_wide(n, SCAN=40):
    """Two smallest non-leaf S-preimages, found by scanning k without assuming
    anything about where they sit."""
    k0 = 2 if n % 3 == 1 else 1
    out = []
    for k in range(k0, k0 + SCAN, 2):
        assert (2 ** k * n) % 3 == 1
        x = (2 ** k * n - 1) // 3
        if x % 3 != 0:
            out.append((x, k))
        if len(out) >= 2 and k >= k0 + 6:
            break
    out.sort()
    return out[0], out[1]

bad = 0
worstpos = {0: 0, 1: 0, 2: 0, None: 0}
for n in range(1, 20001, 2):
    if n % 3 == 0:
        continue
    (y1, k1), (y2, k2) = children_wide(n)
    k0 = 2 if n % 3 == 1 else 1
    if not (y1 < y2 and y1 % 2 == 1 and y2 % 2 == 1 and y1 % 3 and y2 % 3):
        bad += 1
    if not (S(y1) == n and S(y2) == n):
        bad += 1
    if not (3 * y1 < 16 * n and 3 * y2 < 64 * n):       # the 16/3 and 64/3 bounds
        bad += 1
    if not (k1 <= k0 + 2 and k2 <= k0 + 4 and k0 + 4 <= 6):
        bad += 1
    # which of the first three candidates is the leaf?
    cand = [(2 ** k * n - 1) // 3 for k in (k0, k0 + 2, k0 + 4)]
    leafpos = [i for i, x in enumerate(cand) if x % 3 == 0]
    if len(leafpos) != 1:
        bad += 1
        worstpos[None] += 1
    else:
        worstpos[leafpos[0]] += 1
chk("all odd n<=20000 with 3 nmid n: two smallest non-leaf preimages (wide scan) are "
    "odd non-leaves, S-preimages, with 3y1<16n, 3y2<64n, exponents <= k0+4 <= 6",
    bad == 0)
print(f"     leaf position among (x_k0, x_k0+2, x_k0+4): pos0={worstpos[0]}, "
      f"pos1={worstpos[1]}, pos2={worstpos[2]} (all three positions occur; "
      f"pos0 is the worst case forcing 16/3)")
# the 4/3 bound for y1 genuinely FAILS when x_{k0} is the leaf -> the file's remark
viol = [n for n in range(1, 5000, 2) if n % 3 and 3 * children_wide(n)[0][0] >= 4 * n]
chk("y1 < 4n/3 is FALSE in general (file's Remaining-uncertainty note is correct)",
    len(viol) > 0, f"e.g. n={viol[:5]}")

# ---------------------------------------------------------------- the tree T(5)
print("== Tree T(rho): construction, distinctness, size bounds, R-membership ==")
GMAX = 14
def build(rho, gmax):
    gens = [[rho]]
    vals = {rho}
    dup = 0
    for g in range(gmax):
        nxt = []
        for n in gens[g]:
            (y1, _), (y2, _) = children_wide(n)
            for y in (y1, y2):
                if y in vals:
                    dup += 1
                vals.add(y)
                nxt.append(y)
        gens.append(nxt)
    return gens, vals, dup

gens, vals, dup = build(5, GMAX)
chk("root 5: odd, 3 nmid 5, S(5)=1, S^t(5)=1 != 5 for t>=1 => 5 admissible and 5 in R",
    5 % 2 == 1 and 5 % 3 == 2 and S(5) == 1 and S(1) == 1)
chk(f"T(5) to generation {GMAX}: no duplicate node value ({sum(len(l) for l in gens)} nodes)",
    dup == 0 and len(vals) == sum(len(l) for l in gens))
chk("generation g carries exactly 2^g values",
    all(len(l) == 2 ** g for g, l in enumerate(gens)))
chk("every node value is odd, not divisible by 3, and != 1",
    all(v % 2 == 1 and v % 3 != 0 and v != 1 for l in gens for v in l))
chk("size bound 3^g * v <= 5 * 64^g  (exact form of v <= 5*(64/3)^g)",
    all(3 ** g * v <= 5 * 64 ** g for g, l in enumerate(gens) for v in l))
chk("every node value m of generation g satisfies S^g(m) = 5",
    all((lambda m, g: (lambda z: z == 5)(
        __import__("functools").reduce(lambda a, _: S(a), range(g), m)))(v, g)
        for g, l in enumerate(gens) for v in l))
orb_ok = True
maxsteps = 0
for g, l in enumerate(gens):
    for v in l:
        x, c = v, 0
        while x != 1:
            x = S(x); c += 1
            if c > 10 ** 4:
                orb_ok = False; break
        maxsteps = max(maxsteps, c)
chk(f"every one of the {len(vals)} node values has an S-orbit reaching 1 "
    f"(max {maxsteps} S-steps)", orb_ok)
print(f"     children(5) = {tuple(c[0] for c in children_wide(5))}; "
      f"generation 2 = {sorted(gens[2])}")
print(f"     largest generation-12 node = {max(gens[12])}; "
      f"ceiling 5*(64/3)^12 ~ {float(5*Fraction(64,3)**12):.3e}")
print(f"     min value per generation g=0..{GMAX}: {[min(l) for l in gens]}")

# rooting at 1 must break (the x_2(1)=1 self-loop degeneracy)
c1 = children_wide(1)
chk("degeneracy check: children(1) = (1, 5), so rooting at 1 repeats the value 1 -- "
    "distinctness (and hence the whole count) fails; 1 is S-periodic so it is NOT an "
    "admissible root", c1[0][0] == 1 and c1[1][0] == 5 and S(1) == 1)

# ------------------------------- functional inequality (finite-depth faithful form)
print("== Functional inequality N(x) >= N(3x/16) + N(3x/64) + 1 ==")
sortedD = sorted(v for g in range(GMAX + 1) for v in gens[g])
sortedDm1 = sorted(v for g in range(GMAX) for v in gens[g])
def Nfull(x): return bisect.bisect_right(sortedD, x)
def Nprev(x): return bisect.bisect_right(sortedDm1, x)
cnt = 0; bad = 0
x = Fraction(5)
top = 5 * Fraction(64, 3) ** 7
while x <= top:
    if Nfull(x) < Nprev(x * Fraction(3, 16)) + Nprev(x * Fraction(3, 64)) + 1:
        bad += 1
    cnt += 1
    x *= Fraction(11, 10)
chk(f"depth-truncated form N_<=14(x) >= N_<=13(3x/16)+N_<=13(3x/64)+1 at {cnt} scales "
    f"x = 5*(11/10)^i up to 5*(64/3)^7", bad == 0 and cnt >= 100)

# ------------------------------------------------- certificates, my own big ints
print("== Certificates re-derived independently (exact integers) ==")
chk("(C1a) 3^5 < 2^8  => log2 3 < 8/5 => c_A < 5/22", 3 ** 5 < 2 ** 8)
chk("(C1b) 3^12 > 2^19 => log2 3 > 19/12 => c_A > 12/53", 3 ** 12 > 2 ** 19)
chk("(C2) 5^5 * 2^22 <= 3^22  <=> 5^(5/22) <= 3/2", 5 ** 5 * 2 ** 22 <= 3 ** 22)
chk("(C3a) 4096*121^10 <= 27*200^10 <=> (3/16)^(3/10) >= 121/200",
    4096 * 121 ** 10 <= 27 * 200 ** 10)
chk("(C3b) 262144*199^10 <= 27*500^10 <=> (3/64)^(3/10) >= 199/500",
    262144 * 199 ** 10 <= 27 * 500 ** 10)
chk("(C3c) 121/200 + 199/500 = 1003/1000 >= 1",
    Fraction(121, 200) + Fraction(199, 500) == Fraction(1003, 1000) >= 1)
chk("(C4) 1280^3 <= 729*5^10 <=> (1280/9)^(3/10) <= 5 <=> A >= 1/5",
    1280 ** 3 <= 729 * 5 ** 10)
chk("(C5) 256^3 <= 729*3^10 <=> (256/9)^(3/10) <= 3", 256 ** 3 <= 729 * 3 ** 10)
for (lhs, rhs, txt) in ((8 * 3 ** 40, 100 ** 10, "2^(-3/10) >= 81/100"),
                        (64 * 13 ** 10, 20 ** 10, "2^(-6/10) >= 13/20"),
                        (512 * 53 ** 10, 100 ** 10, "2^(-9/10) >= 53/100"),
                        (4096 * 43 ** 10, 100 ** 10, "2^(-12/10) >= 43/100")):
    chk(f"(C6) {txt}", lhs <= rhs)
s6 = 1 + Fraction(81, 100) + Fraction(13, 20) + Fraction(53, 100) + Fraction(43, 100)
chk(f"(C6 sum) = {s6} = 342/100 and (1/5)*sum = 171/250 >= 17/25",
    s6 == Fraction(342, 100) and Fraction(1, 5) * s6 == Fraction(171, 250)
    and Fraction(171, 250) >= Fraction(17, 25))

# c_A enclosure, my own big-int comparison
P = 10 ** 5
three = 3 ** P
lo_e = 158496; hi_e = 158497
chk(f"(C7) 2^{lo_e} < 3^{P} < 2^{hi_e}  => 1.58496 < log2 3 < 1.58497",
    2 ** lo_e < three < 2 ** hi_e)
cA_lo = Fraction(P, 6 * P - lo_e)     # 1/(6 - 1.58496)
cA_hi = Fraction(P, 6 * P - hi_e)
chk(f"c_A enclosure {float(cA_lo):.10f} < c_A < {float(cA_hi):.10f} contains the file's "
    "[0.2264985, 0.2264990]",
    cA_lo > Fraction(2264985, 10 ** 7) and cA_hi < Fraction(2264990, 10 ** 7))
chk("12/53 < c_A < 5/22 (consistent with the tight enclosure)",
    Fraction(12, 53) < cA_lo and cA_hi < Fraction(5, 22))
chk("c_A ~ 0.22650, NOT 0.2266 (file's flagged route correction)",
    cA_hi < Fraction(2266, 10 ** 4))

# c* enclosure by exact rational root bounds
def pow_lo(num, den, p, q, prec=10 ** 6):
    """largest a with (a/prec)^q <= (num/den)^p, num<den; exact integer bisection."""
    lo_, hi_ = 0, prec
    R = prec ** q * num ** p
    while lo_ < hi_:
        mid = (lo_ + hi_ + 1) // 2
        if mid ** q * den ** p <= R:
            lo_ = mid
        else:
            hi_ = mid - 1
    return lo_
PREC = 10 ** 6
def fbounds(p, q):
    a = pow_lo(3, 16, p, q, PREC); b = pow_lo(3, 64, p, q, PREC)
    return Fraction(a, PREC) + Fraction(b, PREC), Fraction(a + 1, PREC) + Fraction(b + 1, PREC)
l, u = fbounds(3, 10)
chk(f"f(3/10) in [{float(l):.6f}, {float(u):.6f}] and f(3/10) > 1  => 3/10 < c*", l > 1)
l, u = fbounds(302, 1000)
chk(f"f(0.302) >= {float(l):.7f} > 1 => c* > 0.302", l > 1)
l, u = fbounds(3021, 10000)
chk(f"f(0.3021) <= {float(u):.7f} < 1 => c* < 0.3021", u < 1)
l, u = fbounds(31, 100)
chk(f"f(0.31) <= {float(u):.6f} < 1 => c* < 0.31 (coarse hand version)", u < 1)

# --------------------------------------- floor-shift step, edge cases (exact)
print("== Scale induction: floor shift m(3y/16) = m(y)-1 and domain checks ==")
def m_idx(y):                                   # y a Fraction >= 5
    k = 0
    z = Fraction(5)
    while z * Fraction(16, 3) <= y:
        z *= Fraction(16, 3); k += 1
    return k
bad = 0; tested = 0
edge = []
for j in range(0, 9):
    base = 5 * Fraction(16, 3) ** j
    for eps in (Fraction(0), Fraction(1, 10 ** 6), Fraction(-1, 10 ** 6),
                Fraction(1, 3), Fraction(-1, 3)):
        y = base + eps
        if y < 5:
            continue
        edge.append(y)
for i in range(400):
    edge.append(Fraction(5) * Fraction(21, 20) ** i)
for y in edge:
    tested += 1
    if m_idx(y * Fraction(3, 16)) != m_idx(y) - 1 and y >= 5 * Fraction(16, 3):
        bad += 1
    if m_idx(y) >= 2:
        if not (y >= Fraction(1280, 9)):
            bad += 1
        if not (y * Fraction(3, 64) >= 5 and y * Fraction(3, 16) >= 5):
            bad += 1
        if not (m_idx(y * Fraction(3, 64)) <= m_idx(y) - 1):
            bad += 1
chk(f"m(3y/16) = m(y)-1 exactly, m(3y/64) <= m(y)-1, and 3y/64 >= 20/3 >= 5 whenever "
    f"m(y)>=2 -- checked at {tested} exact rational points incl. powers of 16/3 and "
    "epsilon-perturbations", bad == 0)
chk("base interval: m(y)<=1 <=> 5 <= y < 5*(16/3)^2 = 1280/9",
    all((m_idx(y) <= 1) == (y < Fraction(1280, 9)) for y in edge if y >= 5))
chk("A*(1280/9)^(3/10) = 1 exactly by definition of A; and A >= 1/5 (C4)",
    1280 ** 3 <= 729 * 5 ** 10)

# ----------------------------- the theorem bound against the tree count (own check)
print("== Theorem B against the (truncated) tree count N_5(x) ==")
bad = 0; tested = 0
x = Fraction(5)
while x <= Fraction(10) ** 12:
    # A x^{3/10} <= N  <=>  (9/1280)^3 * x^3 <= N^10   (exact integers)
    lhs = Fraction(9, 1280) ** 3 * x ** 3
    N = Nfull(x)
    if lhs > Fraction(N) ** 10:
        bad += 1
    # also the weaker published form (1/5) x^{3/10} <= N
    if x ** 3 > (5 * N) ** 10:
        bad += 1
    tested += 1
    x *= Fraction(3, 2)
chk(f"N_5(x) >= A x^(3/10) and >= (1/5) x^(3/10) at {tested} scales up to 10^12, "
    "using only the depth-14 truncation as a LOWER bound for N_5", bad == 0)

# Theorem A against the tree
bad = 0; tested = 0
x = Fraction(5)
while x <= Fraction(10) ** 12:
    N = Nfull(x)
    if x ** 12 > (3 * N) ** 53:     # (1/3) x^{12/53} <= N, exact
        bad += 1
    tested += 1
    x *= Fraction(3, 2)
chk(f"N_5(x) >= (1/3) x^(12/53) at {tested} scales up to 10^12 (exact integer form)",
    bad == 0)

# ---------------------------------------- root-independent form, other roots
print("== Root-independent form for other admissible roots ==")
bad = 0
roots = [7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 65, 91, 97]
for rho in roots:
    g_, v_, d_ = build(rho, 11)
    if d_ != 0:
        bad += 1
    sv = sorted(v_)
    Nr = lambda t: bisect.bisect_right(sv, t)
    xx = Fraction(rho)
    while xx <= Fraction(10) ** 10:
        # (9/(256 rho))^{3/10} x^{3/10} <= N  <=>  9^3 x^3 <= (256 rho)^3 N^10
        if 9 ** 3 * xx ** 3 > (256 * rho) ** 3 * Fraction(Nr(xx)) ** 10:
            bad += 1
        # weaker: (1/3)(x/rho)^{3/10} <= N
        if xx ** 3 > (3 * Nr(xx)) ** 10 * Fraction(rho) ** 3:
            bad += 1
        xx *= Fraction(3, 2)
chk(f"{len(roots)} admissible roots: trees to gen 11 have all-distinct values and "
    "N_rho(x) >= (9/(256 rho))^(3/10) x^(3/10) >= (1/3)(x/rho)^(3/10) at every scale "
    "tested up to 10^10", bad == 0)

# ------------------------------------------------- TRUE CENSUS vs proved bounds
print("== TRUE census #(R cap [1,x]) and cens_C(x) vs the proved bounds ==")
LIM = 10 ** 6
# independent determination of R below LIM: strong induction via S-descent
reachR = bytearray(LIM + 1)      # index by odd n
reachR[1] = 1
ok_desc = True
for n in range(3, LIM + 1, 2):
    x = S(n); steps = 0
    while x > LIM:               # may excurse above LIM; iterate until it comes back
        x = S(x); steps += 1
        if steps > 10 ** 4:
            ok_desc = False; break
    while x != 1 and not reachR[x]:
        x = S(x); steps += 1
        while x > LIM:
            x = S(x); steps += 1
        if steps > 10 ** 4:
            ok_desc = False; break
    reachR[n] = 1 if (x == 1 or reachR[x]) else 0
chk("S-orbit reachability computed for every odd n <= 10^6 without hitting the "
    "iteration cap", ok_desc)
censR_pref = [0] * (LIM + 1)
run = 0
for n in range(1, LIM + 1):
    if n % 2 == 1 and reachR[n]:
        run += 1
    censR_pref[n] = run
chk("every odd n <= 10^6 is in R (finite verification, not a proof input)",
    censR_pref[LIM] == (LIM // 2))
# cens_C by C-descent
okC = True
for n in range(2, LIM + 1):
    x = n; steps = 0
    while x >= n:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        steps += 1
        if steps > 10 ** 5:
            okC = False; break
chk("every n <= 10^6 descends below itself under C (=> cens_C(x) = floor(x) there)", okC)

rows = []
bad = 0
for e in (3, 4, 5, 6):
    x = 10 ** e
    cR = censR_pref[x]
    cC = x
    # exact integer comparisons of the three proved bounds against the true census
    a_ok = x ** 12 < (3 * cR) ** 53                       # (1/3)x^(12/53) < cens_R
    b_ok = x ** 3 < (5 * cR) ** 10                        # (1/5)x^(3/10)  < cens_R
    c_ok = 17 ** 10 * x ** 3 <= 25 ** 10 * cC ** 10       # (17/25)x^(3/10) <= cens_C
    if not (a_ok and b_ok and c_ok):
        bad += 1
    rows.append((x, cR, x ** (12 / 53) / 3, x ** 0.3 / 5, cC, 17 / 25 * x ** 0.3,
                 cR / (x ** (12 / 53) / 3), cR / (x ** 0.3 / 5)))
chk("all three proved bounds hold against the TRUE census at x=10^3..10^6 "
    "(exact integer inequalities)", bad == 0)
print(f"{'x':>9} | {'#R∩[1,x]':>9} | {'(1/3)x^(12/53)':>14} | {'(1/5)x^(3/10)':>13} | "
      f"{'cens_C':>9} | {'(17/25)x^(3/10)':>15} | {'slack A':>9} | {'slack B':>9}")
for r in rows:
    print(f"{r[0]:>9} | {r[1]:>9} | {r[2]:>14.2f} | {r[3]:>13.2f} | {r[4]:>9} | "
          f"{r[5]:>15.2f} | {r[6]:>8.0f}x | {r[7]:>8.0f}x")

# corollary layer disjointness sanity
chk("layers 2^j R (j=0..4) are pairwise disjoint (nu_2 = j exactly) and each element "
    "reaches 1 under C", all(nu2(2 ** j * 7) == j for j in range(5)))

print()
print("SUMMARY:", "ALL CHECKS PASS" if not FAIL else f"{len(FAIL)} FAILURES: {FAIL}")
```

Output (verbatim; runtime ~2.6 s). The single `FAIL` line is the (C7) defect of §3 —
it is the *reviewer's* assertion `C7 upper bound <= 0.2264990` failing, i.e. exactly
the under-certification described above; it is repaired by (C7′) in Script 2.

```text
== Lemma P: preimage parametrisation (independent brute-force cross-check) ==
  [PASS] all odd n<=4000: brute-force S-preimage set == {x_k : k in A(n)}; A(n) is the step-2 AP starting at k0 in {1,2} (empty iff 3|n); each x_k odd, positive, nu2(3x_k+1)=k, S(x_k)=n, x_k < 2^k n/3
== Lemma L: mod-9 leaf control, exhaustive for all n < 10^4 with 3 nmid n ==
  [PASS] multiplicative order of 4 mod 9 equals 3 (4,16=7,64=1 mod 9)
  [PASS] 16 = 7 mod 9 and 4^2 = 7 mod 9
  [PASS] {u,4u,7u} = {1,4,7} for every u in {1,4,7}
  [PASS] residues r mod 9 with r = 1 mod 3 are exactly {1,4,7}
  [PASS] each of 1,4,7 is a unit mod 9 (gcd with 3 is 1)
  [PASS] all n<10^4 with 3 nmid n, all 83325 windows of 3 consecutive admissible k: residues = (u,4u,7u) = {1,4,7}; EXACTLY one = 1 mod 9; leaf <=> 2^k n = 1 mod 9
  [PASS] no window with ZERO leaves and no window with TWO leaves was found (strengthening 'exactly one' confirmed)
== Lemma B: two-child selection by an INDEPENDENT wide scan ==
  [PASS] all odd n<=20000 with 3 nmid n: two smallest non-leaf preimages (wide scan) are odd non-leaves, S-preimages, with 3y1<16n, 3y2<64n, exponents <= k0+4 <= 6
     leaf position among (x_k0, x_k0+2, x_k0+4): pos0=2222, pos1=2222, pos2=2223 (all three positions occur; pos0 is the worst case forcing 16/3)
  [PASS] y1 < 4n/3 is FALSE in general (file's Remaining-uncertainty note is correct) e.g. n=[5, 7, 23, 25, 41]
== Tree T(rho): construction, distinctness, size bounds, R-membership ==
  [PASS] root 5: odd, 3 nmid 5, S(5)=1, S^t(5)=1 != 5 for t>=1 => 5 admissible and 5 in R
  [PASS] T(5) to generation 14: no duplicate node value (32767 nodes)
  [PASS] generation g carries exactly 2^g values
  [PASS] every node value is odd, not divisible by 3, and != 1
  [PASS] size bound 3^g * v <= 5 * 64^g  (exact form of v <= 5*(64/3)^g)
  [PASS] every node value m of generation g satisfies S^g(m) = 5
  [PASS] every one of the 32767 node values has an S-orbit reaching 1 (max 15 S-steps)
     children(5) = (13, 53); generation 2 = [17, 35, 277, 565]
     largest generation-12 node = 43086887646773; ceiling 5*(64/3)^12 ~ 4.443e+16
     min value per generation g=0..14: [5, 13, 17, 11, 7, 19, 25, 65, 43, 59, 79, 203, 139, 185, 127]
  [PASS] degeneracy check: children(1) = (1, 5), so rooting at 1 repeats the value 1 -- distinctness (and hence the whole count) fails; 1 is S-periodic so it is NOT an admissible root
== Functional inequality N(x) >= N(3x/16) + N(3x/64) + 1 ==
  [PASS] depth-truncated form N_<=14(x) >= N_<=13(3x/16)+N_<=13(3x/64)+1 at 225 scales x = 5*(11/10)^i up to 5*(64/3)^7
== Certificates re-derived independently (exact integers) ==
  [PASS] (C1a) 3^5 < 2^8  => log2 3 < 8/5 => c_A < 5/22
  [PASS] (C1b) 3^12 > 2^19 => log2 3 > 19/12 => c_A > 12/53
  [PASS] (C2) 5^5 * 2^22 <= 3^22  <=> 5^(5/22) <= 3/2
  [PASS] (C3a) 4096*121^10 <= 27*200^10 <=> (3/16)^(3/10) >= 121/200
  [PASS] (C3b) 262144*199^10 <= 27*500^10 <=> (3/64)^(3/10) >= 199/500
  [PASS] (C3c) 121/200 + 199/500 = 1003/1000 >= 1
  [PASS] (C4) 1280^3 <= 729*5^10 <=> (1280/9)^(3/10) <= 5 <=> A >= 1/5
  [PASS] (C5) 256^3 <= 729*3^10 <=> (256/9)^(3/10) <= 3
  [PASS] (C6) 2^(-3/10) >= 81/100
  [PASS] (C6) 2^(-6/10) >= 13/20
  [PASS] (C6) 2^(-9/10) >= 53/100
  [PASS] (C6) 2^(-12/10) >= 43/100
  [PASS] (C6 sum) = 171/50 = 342/100 and (1/5)*sum = 171/250 >= 17/25
  [PASS] (C7) 2^158496 < 3^100000 < 2^158497  => 1.58496 < log2 3 < 1.58497
  [*** FAIL ***] c_A enclosure 0.2264985142 < c_A < 0.2264990272 contains the file's [0.2264985, 0.2264990]
  [PASS] 12/53 < c_A < 5/22 (consistent with the tight enclosure)
  [PASS] c_A ~ 0.22650, NOT 0.2266 (file's flagged route correction)
  [PASS] f(3/10) in [1.004486, 1.004488] and f(3/10) > 1  => 3/10 < c*
  [PASS] f(0.302) >= 1.0000270 > 1 => c* > 0.302
  [PASS] f(0.3021) <= 0.9998060 < 1 => c* < 0.3021
  [PASS] f(0.31) <= 0.982407 < 1 => c* < 0.31 (coarse hand version)
== Scale induction: floor shift m(3y/16) = m(y)-1 and domain checks ==
  [PASS] m(3y/16) = m(y)-1 exactly, m(3y/64) <= m(y)-1, and 3y/64 >= 20/3 >= 5 whenever m(y)>=2 -- checked at 443 exact rational points incl. powers of 16/3 and epsilon-perturbations
  [PASS] base interval: m(y)<=1 <=> 5 <= y < 5*(16/3)^2 = 1280/9
  [PASS] A*(1280/9)^(3/10) = 1 exactly by definition of A; and A >= 1/5 (C4)
== Theorem B against the (truncated) tree count N_5(x) ==
  [PASS] N_5(x) >= A x^(3/10) and >= (1/5) x^(3/10) at 65 scales up to 10^12, using only the depth-14 truncation as a LOWER bound for N_5
  [PASS] N_5(x) >= (1/3) x^(12/53) at 65 scales up to 10^12 (exact integer form)
== Root-independent form for other admissible roots ==
  [PASS] 20 admissible roots: trees to gen 11 have all-distinct values and N_rho(x) >= (9/(256 rho))^(3/10) x^(3/10) >= (1/3)(x/rho)^(3/10) at every scale tested up to 10^10
== TRUE census #(R cap [1,x]) and cens_C(x) vs the proved bounds ==
  [PASS] S-orbit reachability computed for every odd n <= 10^6 without hitting the iteration cap
  [PASS] every odd n <= 10^6 is in R (finite verification, not a proof input)
  [PASS] every n <= 10^6 descends below itself under C (=> cens_C(x) = floor(x) there)
  [PASS] all three proved bounds hold against the TRUE census at x=10^3..10^6 (exact integer inequalities)
        x |  #R∩[1,x] | (1/3)x^(12/53) | (1/5)x^(3/10) |    cens_C | (17/25)x^(3/10) |   slack A |   slack B
     1000 |       500 |           1.59 |          1.59 |      1000 |            5.40 |      314x |      315x
    10000 |      5000 |           2.68 |          3.17 |     10000 |           10.78 |     1864x |     1577x
   100000 |     50000 |           4.52 |          6.32 |    100000 |           21.50 |    11067x |     7906x
  1000000 |    500000 |           7.61 |         12.62 |   1000000 |           42.91 |    65705x |    39622x
  [PASS] layers 2^j R (j=0..4) are pairwise disjoint (nu_2 = j exactly) and each element reaches 1 under C

SUMMARY: 1 FAILURES: ["c_A enclosure 0.2264985142 < c_A < 0.2264990272 contains the file's [0.2264985, 0.2264990]"]
```

**Script 2 — `v15_probe2.py`** (the (C7) defect, its repair, deeper distinctness,
and the degeneracy probe).

```python
#!/usr/bin/env python3
# fable-02-v15 -- probe 2: the (C7) defect, its repair (C7'), deeper distinctness,
# the flagged "1.4e-4", and the finiteness of N_rho. Exact integers throughout.
from fractions import Fraction
import decimal, bisect
decimal.getcontext().prec = 60
D = decimal.Decimal
cA = 1 / (6 - D(3).ln() / D(2).ln())

print("=== (C7) as printed in L-9914 vs what it actually certifies ===")
P = 10 ** 5
assert 2 ** 158496 < 3 ** P < 2 ** 158497
lo5, hi5 = Fraction(P, 6 * P - 158496), Fraction(P, 6 * P - 158497)
print(f"  C7 certifies      {float(lo5):.13f} < c_A < {float(hi5):.13f}")
print(f"  L-9914.3 states   0.2264985       < c_A < 0.2264990")
print(f"  lower endpoint implied by C7 ? {lo5 >= Fraction(2264985, 10**7)}")
print(f"  upper endpoint implied by C7 ? {hi5 <= Fraction(2264990, 10**7)}   "
      f"<-- DEFECT: C7's upper bound is {float(hi5):.10f} > 0.2264990")
print(f"  true c_A = {str(cA)[:22]}...  (so the ENDPOINT IS TRUE, only under-certified)")

print()
print("=== (C7') repair A: continued-fraction convergents of log2 3 ===")
a1 = 3 ** 665 > 2 ** 1054
a2 = 3 ** 306 < 2 ** 485
print(f"  3^665 > 2^1054 : {a1}   (=> log2 3 > 1054/665)")
print(f"  3^306 < 2^485  : {a2}   (=> log2 3 < 485/306)")
loH, hiH = Fraction(665, 2936), Fraction(306, 1351)
print(f"  => 665/2936 < c_A < 306/1351, i.e. {float(loH):.10f} < c_A < {float(hiH):.10f}")
print(f"  implies 0.2264985 < c_A < 0.2264990 ? "
      f"{loH >= Fraction(2264985,10**7) and hiH <= Fraction(2264990,10**7)}")
print(f"  sizes: 3^665 has 318 digits, 3^306 has 146 digits (vs 47,713 for 3^100000)")

print()
print("=== (C7') repair B: the P = 10^6 version of the author's own certificate ===")
t6 = 3 ** (10 ** 6)
b1, b2 = 2 ** 1584962 < t6, t6 < 2 ** 1584963
print(f"  2^1584962 < 3^(10^6) < 2^1584963 : {b1 and b2}")
lo6, hi6 = Fraction(10**6, 6*10**6 - 1584962), Fraction(10**6, 6*10**6 - 1584963)
print(f"  => {float(lo6):.13f} < c_A < {float(hi6):.13f}")
print(f"  implies 0.2264985 < c_A < 0.2264990 ? "
      f"{lo6 >= Fraction(2264985,10**7) and hi6 <= Fraction(2264990,10**7)}")
print(f"  even implies 0.2264986 < c_A < 0.2264987 ? "
      f"{lo6 >= Fraction(2264986,10**7) and hi6 <= Fraction(2264987,10**7)}")

print()
print("=== the flagged route difference ===")
print(f"  0.2266 - c_A = {str(D('0.2266') - cA)[:12]} ~ 1.01e-4  (file said ~1.4e-4)")

print()
print("=== deeper distinctness of T(5), and the minimum-value profile ===")
def nu2(m):
    k = 0
    while m % 2 == 0:
        m //= 2; k += 1
    return k
def S(x):
    y = 3 * x + 1
    return y >> nu2(y)
def kids(n):
    k0 = 2 if n % 3 == 1 else 1
    out = []
    for k in range(k0, k0 + 40, 2):
        x = (2 ** k * n - 1) // 3
        if x % 3 != 0:
            out.append(x)
        if len(out) == 2:
            return out
gens, vals, dup = [[5]], {5}, 0
for g in range(17):
    nxt = []
    for n in gens[g]:
        for y in kids(n):
            if y in vals:
                dup += 1
            vals.add(y); nxt.append(y)
    gens.append(nxt)
print(f"  T(5) to generation 17: {sum(len(l) for l in gens)} nodes, "
      f"{len(vals)} distinct values, duplicates = {dup}")
print(f"  min value per generation g=0..17: {[min(l) for l in gens]}")
print(f"  smallest value anywhere = {min(vals)}  => N_5(y) = 0 for y < 5")
print(f"  NOTE: node values are NOT monotone in g (gen 4 min = 7 < gen 0 = 5), so the")
print(f"  finiteness of N_5(x) is NOT automatic from the size bound -- it follows from")
print(f"  DISTINCTNESS: distinct positive integers <= x number at most floor(x).")
bad = sum(1 for g in range(17) for n in gens[g]
          for y1, y2 in [kids(n)] if not (3*y1 < 16*n and 3*y2 < 64*n))
print(f"  step-bound violations across all {sum(len(l) for l in gens)} nodes: {bad}")

print()
print("=== degeneracy: rooting at the S-periodic point 1 ===")
print(f"  children(1) = {tuple(kids(1))}: y_1(1) = 1 = the root itself, so the tree")
print(f"  from 1 repeats a value at depth 1 and distinctness (hence the count) FAILS.")
print(f"  S(1) = {S(1)} so 1 IS S-periodic and is correctly excluded by 'admissible root'.")
print(f"  By contrast S(5) = {S(5)}, S^2(5) = {S(S(5))}: 5 is unconditionally")
print(f"  non-S-periodic -- no appeal to 'no nontrivial cycles' is made anywhere.")
```

Output (verbatim; runtime ~0.4 s):

```text
=== (C7) as printed in L-9914 vs what it actually certifies ===
  C7 certifies      0.2264985141697 < c_A < 0.2264990271867
  L-9914.3 states   0.2264985       < c_A < 0.2264990
  lower endpoint implied by C7 ? True
  upper endpoint implied by C7 ? False   <-- DEFECT: C7's upper bound is 0.2264990272 > 0.2264990
  true c_A = 0.22649864246075846379...  (so the ENDPOINT IS TRUE, only under-certified)

=== (C7') repair A: continued-fraction convergents of log2 3 ===
  3^665 > 2^1054 : True   (=> log2 3 > 1054/665)
  3^306 < 2^485  : True   (=> log2 3 < 485/306)
  => 665/2936 < c_A < 306/1351, i.e. 0.2264986376 < c_A < 0.2264988897
  implies 0.2264985 < c_A < 0.2264990 ? True
  sizes: 3^665 has 318 digits, 3^306 has 146 digits (vs 47,713 for 3^100000)

=== (C7') repair B: the P = 10^6 version of the author's own certificate ===
  2^1584962 < 3^(10^6) < 2^1584963 : True
  => 0.2264986167729 < c_A < 0.2264986680746
  implies 0.2264985 < c_A < 0.2264990 ? True
  even implies 0.2264986 < c_A < 0.2264987 ? True

=== the flagged route difference ===
  0.2266 - c_A = 0.0001013575 ~ 1.01e-4  (file said ~1.4e-4)

=== deeper distinctness of T(5), and the minimum-value profile ===
  T(5) to generation 17: 262143 nodes, 262143 distinct values, duplicates = 0
  min value per generation g=0..17: [5, 13, 17, 11, 7, 19, 25, 65, 43, 59, 79, 203, 139, 185, 127, 169, 239, 295]
  smallest value anywhere = 5  => N_5(y) = 0 for y < 5
  NOTE: node values are NOT monotone in g (gen 4 min = 7 < gen 0 = 5), so the
  finiteness of N_5(x) is NOT automatic from the size bound -- it follows from
  DISTINCTNESS: distinct positive integers <= x number at most floor(x).
  step-bound violations across all 262143 nodes: 0

=== degeneracy: rooting at the S-periodic point 1 ===
  children(1) = (1, 5): y_1(1) = 1 = the root itself, so the tree
  from 1 repeats a value at depth 1 and distinctness (hence the count) FAILS.
  S(1) = 1 so 1 IS S-periodic and is correctly excluded by 'admissible root'.
  By contrast S(5) = 1, S^2(5) = 1: 5 is unconditionally
  non-S-periodic -- no appeal to 'no nontrivial cycles' is made anywhere.
```

---

*Verified by fable-02-v15, 2026-07-25. Verdict: PASS — Status PROPOSED → PROVED.
One certificate defect found and repaired ((C7) → (C7′)); one arithmetic slip
corrected; no theorem statement changed. Per README §7 this file remains at PROVED —
`INDEPENDENTLY_VERIFIED` is not set by this review.*
