# L-9909 — Syracuse preimages, counterexample closure, and the uniform-descent survivor sieve

```text
Claim ID: L-9909
Title: Backward-tree structure of S, closure properties of the counterexample set,
       minimal-counterexample properties, and the uniform-descent survivor sieve
       mod 2^k with exact computation for k <= 8
Status: PROVED
Authoring agent: fable-02-p7
Reviewing agents: fable-02-v7 (adversarial review 2026-07-22: PASS)
Created: 2026-07-21
Last updated: 2026-07-22 (status upgraded after independent adversarial review)
Dependencies: research/foundations/NOTATION.md (D-9901..D-9910).
              Related but NOT depended on: L-9902 (parity-word/residue bijection),
              L-9903 (sharp bounds on the affine constants rho_j) — the pieces of
              those results needed here are re-derived inline in Lemmas B and C,
              so this file has no forward dependence.
Scope: Classical foundational layer. Sub-claims L-9909.1–L-9909.3 and L-9909.5 are
       fully proved, self-contained results about the maps C, T, S of D-9901,
       D-9902, D-9904. Sub-claim L-9909.4 is an exact finite computation plus a
       theorem whose hypothesis is discharged by the finite verification X-9901
       (role labeled precisely in the Proof section). No novelty is claimed; this
       is an adversarially checkable in-repo proof of load-bearing folklore.
Related counterexample candidates: none
```

Notation is exactly that of `research/foundations/NOTATION.md`: $C$ (D-9901), $T$ (D-9902),
$\mathrm{odd}(\cdot)$ (D-9903), $S$ (D-9904), orbits $O_M(n)$ and "reaches 1" (D-9905),
parity vector $v_i(n) = T^i(n) \bmod 2$ and odd-step counts $a_k(n) = \sum_{i<k} v_i(n)$
(D-9906), counterexample (D-9909), stopping time $\sigma$ (D-9910),
$\gamma := \log_3 2 = \ln 2/\ln 3 \approx 0.6309298$, $\nu_2$ = 2-adic valuation,
$\mathbb{Z}^+ = \{1,2,3,\dots\}$.

---

## Statement

Terms in small capitals (admissible exponent, leaf, class word, $\rho_j$, failing index,
$k$-survivor, $B_k$, $K$, $\mu$) are defined in the Definitions section.

### L-9909.1 (Syracuse preimages)

Let $n \in \mathbb{Z}^+$ be odd and let
$$A(n) := \{k \in \mathbb{Z} : k \ge 1,\ 2^k n \equiv 1 \pmod 3\}$$
be the set of *admissible exponents* of $n$. Then:

1. **(Parametrization.)** The set $S^{-1}(n)$ of odd $x \in \mathbb{Z}^+$ with $S(x) = n$
   is exactly $\{\,x_k := (2^k n - 1)/3 : k \in A(n)\,\}$, and $k \mapsto x_k$ is a
   strictly increasing bijection $A(n) \to S^{-1}(n)$. For every $k \in A(n)$:
   $x_k \in \mathbb{Z}^+$ (integrality and positivity hold), $x_k$ is **automatically odd**, and
   **automatically** $\nu_2(3x_k + 1) = k$ exactly.
2. **(Case analysis.)**
   $A(n) = \varnothing$ if $n \equiv 0 \pmod 3$ (so $n$ is a **leaf**: no $S$-preimages);
   $A(n) = \{k \text{ even},\ k \ge 2\}$ if $n \equiv 1 \pmod 3$;
   $A(n) = \{k \text{ odd},\ k \ge 1\}$ if $n \equiv 2 \pmod 3$.
   Consequently every odd $n$ with $3 \nmid n$ has **infinitely many** $S$-preimages, one
   for each admissible $k$.
3. **(Bonus: leaf distribution mod 3.)** Suppose $3 \nmid n$ and enumerate
   $A(n) = \{k_0 < k_1 < k_2 < \dots\}$ (so $k_i = k_0 + 2i$ with $k_0 = 2$ if
   $n \equiv 1 \bmod 3$, $k_0 = 1$ if $n \equiv 2 \bmod 3$). Then
   $$x_{k_i} \equiv e_0(n) + i \pmod 3, \qquad
     e_0(n) := \begin{cases} 1 & n \equiv 1 \pmod 9\\ 2 & n \equiv 4 \pmod 9\\ 0 & n \equiv 7 \pmod 9\\ 1 & n \equiv 2 \pmod 9\\ 0 & n \equiv 5 \pmod 9\\ 2 & n \equiv 8 \pmod 9. \end{cases}$$
   In particular the preimage residues mod 3 cycle through $0 \to 1 \to 2 \to 0$ with
   period 3 in $i$: in every 3 consecutive preimages of a non-leaf node, exactly one is a
   leaf ($\equiv 0 \bmod 3$), one is $\equiv 1$, and one is $\equiv 2 \pmod 3$.

### L-9909.2 (counterexample closure and the smallest counterexample)

Let $K := \{n \in \mathbb{Z}^+ : 1 \notin O_C(n)\}$ be the set of counterexamples (D-9909).

* **(F) Forward closure.** If $n \in K$ then $C(n) \in K$; hence every element of
  $O_C(n)$ lies in $K$.
* **(B) Backward closure.** If $n \in K$ and $m \in \mathbb{Z}^+$ satisfies $n \in O_C(m)$,
  then $m \in K$.
* **(E) Explicit backward edges (issue #25 correspondence).** If $n \in K$ then
  $2n \in K$; and if moreover $n \equiv 2 \pmod 3$, then $(2n-1)/3$ is an odd element of
  $\mathbb{Z}^+$ and $(2n-1)/3 \in K$. Thus $K$ satisfies **exactly** the closure
  hypotheses "closed under $n \mapsto 2n$ and under $n \mapsto (2n-1)/3$ whenever the
  latter is integral" of the rooted backward-tree density program (issue #25).
* **(M) Minimal counterexample.** If $K \neq \varnothing$, let $\mu := \min K$. Then:
  1. $\mu$ is odd and $\mu \ge 3$;
  2. $\mu \equiv 3 \pmod 4$;
  3. $T^j(\mu) \ge \mu$ for **all** $j \ge 1$; equivalently $\sigma(\mu) = \infty$ (D-9910).

### L-9909.3 (uniform-descent sieve)

Fix $k \ge 1$ and a residue class $r \bmod 2^k$ ($0 \le r < 2^k$). All $n \in \mathbb{Z}^+$
with $n \equiv r \pmod{2^k}$ share the same length-$k$ parity word
$(v_0, \dots, v_{k-1})$ (the *class word*, well defined by Lemma B below), hence the same
counts $a_j$ and the same affine constants $\rho_j$ (Lemma C) for $0 \le j \le k$.
Then, for every $j$ with $1 \le j \le k$:

* **(a)** If $3^{a_j} \ge 2^j$, then **every** $n \in \mathbb{Z}^+$ with
  $n \equiv r \pmod{2^k}$ satisfies $T^j(n) > n$ (in particular $T^j(n) \ge n$).
* **(b)** If $3^{a_j} < 2^j$, put $d_j := 2^j - 3^{a_j} \ge 1$. Then **every**
  $n \in \mathbb{Z}^+$ with $n \equiv r \pmod{2^k}$ and $n > \rho_j / d_j$ satisfies
  $T^j(n) < n$. (Moreover $T^j(n) = n$ if $n = \rho_j/d_j$ and $T^j(n) > n$ if
  $n < \rho_j/d_j$; the threshold $\rho_j/d_j$ is an explicitly computable constant of
  the class.)

Furthermore, for integers $a \ge 0$ and $j \ge 1$:
$3^{a} \ge 2^j \iff a \ge \lceil j\gamma \rceil$ (Lemma D, via irrationality of
$\log_2 3$), so condition (a) at level $j$ reads $a_j \ge \lceil j\gamma\rceil$.

**Corollary (sieve).** With the $k$-survivor classes and the constant $B_k$ as in the
Definitions:

1. If $r$ is a $k$-survivor, then **every** $n \in \mathbb{Z}^+$ in the class satisfies
   $T^j(n) > n$ for $1 \le j \le k$; hence $\sigma(n) > k$ uniformly on the class.
2. If $n \in \mathbb{Z}^+$ has $\sigma(n) > k$, then either $n \bmod 2^k$ is a
   $k$-survivor, or $n \le B_k$. ($B_k$ is a finite, explicitly computable rational.)
3. $B_k \le B_{k+1}$ for all $k \ge 1$.
4. If $K \neq \varnothing$ then, since $\sigma(\mu) = \infty$ by L-9909.2(M)(iii): for
   **every** $k \ge 1$ with $\mu > B_k$, the class $\mu \bmod 2^k$ is a $k$-survivor.

### L-9909.4 (exact survivor computation for $k \le 8$, and X-9901)

Exact computation (finitely many classes, exact integer arithmetic; script
`l9909_sieve.py` in the Adversarial tests section) gives:

| $k$ | $\lceil k\gamma\rceil$ | # $k$-survivors | density | $B_k$ (exact) | $B_k$ (approx.) |
|----|----|----|--------|---------|----------|
| 1 | 1 | 1 | $1/2$ | $0$ | $0$ |
| 2 | 2 | 1 | $1/4$ | $2$ | $2$ |
| 3 | 2 | 2 | $1/4$ | $2$ | $2$ |
| 4 | 3 | 3 | $3/16$ | $20/7$ | $2.857$ |
| 5 | 4 | 4 | $1/8$ | $76/5$ | $15.2$ |
| 6 | 4 | 8 | $1/8$ | $76/5$ | $15.2$ |
| 7 | 5 | 13 | $13/128$ | $76/5$ | $15.2$ |
| 8 | 6 | 19 | $19/256$ | $1688/13$ | $129.846$ |

Survivor classes, explicitly:

* mod 2: $\{1\}$
* mod 4: $\{3\}$
* mod 8: $\{3, 7\}$
* mod 16: $\{7, 11, 15\}$
* mod 32: $\{7, 15, 27, 31\}$
* mod 64: $\{7, 15, 27, 31, 39, 47, 59, 63\}$
* mod 128: $\{27, 31, 39, 47, 63, 71, 79, 91, 95, 103, 111, 123, 127\}$
* mod 256: $\{27, 31, 47, 63, 71, 91, 103, 111, 127, 155, 159, 167, 191, 207, 223, 231, 239, 251, 255\}$

**X-9901 (finite verification).** Every $n \le 10^6$ reaches 1 under $C$. The exact bound
used is $N_0 := \max(B_8, 10^6) = 10^6$ (since $B_8 = 1688/13 < 130$). The maximum total
$C$-stopping time observed for $n \le 10^6$ is $524$, attained at $n = 837799$.

**Theorem (unconditional given the recorded finite verification X-9901).** If a
counterexample exists, then $\mu > 10^6$, and for every $k \le 8$ the class
$\mu \bmod 2^k$ is a $k$-survivor. In particular
$$\mu \equiv 1 \ (2);\quad \mu \equiv 3\ (4);\quad \mu \in \{3,7\} \ (8);\quad
\mu \in \{7,11,15\}\ (16);\quad \mu \in \{7,15,27,31\}\ (32);$$
$$\mu \in \{7,15,27,31,39,47,59,63\}\ (64);\quad \mu \in \{27,\dots,127\}\ (128) \text{ and }
\mu \in \{27,\dots,255\}\ (256) \text{ per the lists above.}$$
**Cross-check:** the mod-2 and mod-4 restrictions recover L-9909.2(M)(i)–(ii)
($\mu$ odd, $\mu \equiv 3 \bmod 4$) exactly; no discrepancy (see Proof of L-9909.4).

### L-9909.5 (packaging corollary for search programs)

Any counterexample-search program may unconditionally restrict attention, at each level
$k \le 8$, to the $k$-survivor classes of L-9909.4 (and, for any larger $k$, to the
$k$-survivor classes it computes itself, for candidates $> B_k$). Observed survivor
densities: $1/2,\ 1/4,\ 1/4,\ 3/16,\ 1/8,\ 1/8,\ 13/128,\ 19/256$ — **nonincreasing**
(proved below), but *not strictly* decreasing (equalities at $k = 2\to3$ and $5\to6$;
this minimally corrects the naive expectation "$1/2, 1/4, \dots$ strictly decreasing").
A planned lemma **L-9908** is expected to prove exponential decay of the survivor density
as $k \to \infty$; that is a forward pointer only and is **not** proved here.

---

## Definitions

All items below are local to this file unless they carry a D-number from NOTATION.md.

* **Admissible exponent** (for odd $n \in \mathbb{Z}^+$): $k \ge 1$ with
  $2^k n \equiv 1 \pmod 3$; the set of these is $A(n)$.
* **Leaf**: an odd $n \in \mathbb{Z}^+$ with $S^{-1}(n) = \varnothing$. (By L-9909.1 these
  are exactly the odd multiples of 3.)
* **Counterexample set**: $K := \{n \in \mathbb{Z}^+ : 1 \notin O_C(n)\}$ (D-9909); membership
  of $1$ in the orbit is membership as a term of the sequence $O_C(n)$, which includes the
  index-0 term $n$ itself (D-9905 allows $k = 0$).
* **Minimal counterexample**: $\mu := \min K$, defined only under the hypothesis
  $K \neq \varnothing$ (well defined: a nonempty subset of $\mathbb{Z}^+$ has a least element).
* **Class word**: for a residue class $r \bmod 2^k$, the common parity word
  $(v_0, \dots, v_{k-1})$ of all its positive members (well defined by Lemma B); $a_j$
  ($0 \le j \le k$) its partial sums (D-9906), constant on the class.
* **Affine constants** $\rho_j$: defined from a word by
  $\rho_0 := 0$, $\rho_{i+1} := 3^{v_i}\rho_i + v_i 2^i$ ($0 \le i < k$). They depend only
  on the word, hence are constants of the class.
* **Failing index** of a class $r \bmod 2^k$: any $j$ with $1 \le j \le k$ and
  $3^{a_j} < 2^j$ (equivalently $a_j < \lceil j\gamma\rceil$, Lemma D); then
  $d_j := 2^j - 3^{a_j} \ge 1$.
* **$k$-survivor**: a class $r \bmod 2^k$ with no failing index, i.e.
  $a_j \ge \lceil j\gamma \rceil$ for all $1 \le j \le k$
  (equivalently $3^{a_j} \ge 2^j$ for all $j \le k$).
* **Class constant / sieve bound**:
  $$B_k := \max\Bigl\{\ \tfrac{\rho_j(r)}{2^j - 3^{a_j(r)}} \ :\ 0 \le r < 2^k,\ 1 \le j \le k,\ 3^{a_j(r)} < 2^j \Bigr\} \in \mathbb{Q}_{\ge 0},$$
  a maximum over a finite nonempty set (for $k \ge 1$ the class $r = 0$ has $a_1 = 0$, so
  $j = 1$ is failing for it), hence finite and explicitly computable. (Taking, per class,
  the *minimum* over failing $j$ would give a sharper bound; the coarser max-over-all
  version suffices here and is what the corollary uses.)
* **Total $C$-stopping time** (used only in X-9901): the least $t \ge 0$ with $C^t(n) = 1$,
  when it exists.

---

## Motivation

This file is the base layer for two active needs of the project:

1. **Issue #25 (rooted backward-tree density program).** That program studies sets
   $E \subseteq \mathbb{Z}^+$ closed under $n \mapsto 2n$ and under
   $n \mapsto (2n-1)/3$ whenever the latter is integral, and derives density
   consequences. L-9909.2(E) proves that the counterexample set $K$ satisfies **exactly
   these two closure hypotheses** (with the integrality condition characterized as
   $n \equiv 2 \bmod 3$, and the image automatically odd and positive). So every theorem
   of the issue #25 program about such sets $E$ applies verbatim to $K$: the
   correspondence is literal, not analogical. L-9909.1 supplies the finer backward-tree
   structure at the Syracuse level (which odd nodes branch, which are leaves, and how
   leaves distribute mod 3), which that program needs for density bookkeeping.
2. **All search programs (survivor restriction).** L-9909.3/4 turn the trivial remark
   "a minimal counterexample never drops below itself" into a **uniform, per-residue-class**
   sieve with explicitly computable exceptional bounds $B_k$: a search for
   counterexamples, cycles, or high-excursion orbits may provably discard all non-survivor
   classes mod $2^k$ (above $B_k$, and unconditionally for $k \le 8$ after X-9901).
   The sieve is also the standard on-ramp to stopping-time density results (planned
   L-9908), and the survivor lists computed here are reusable test vectors for L-9902 and
   L-9903.

Neutrality note (D-9909): nothing here assumes the conjecture true or false; all
statements are conditional on the existence or nonexistence of counterexamples in the
proper logical direction.

---

## Proof

Throughout, $T: \mathbb{Z}^+ \to \mathbb{Z}^+$ (if $n$ is even then $T(n) = n/2 \ge 1$; if $n$
is odd then $T(n) = (3n+1)/2 \ge 2$, an integer since $3n + 1$ is even). Similarly
$C: \mathbb{Z}^+ \to \mathbb{Z}^+$ and $S$ maps positive odds to positive odds (D-9903/D-9904:
$\mathrm{odd}(3x+1)$ is a positive odd integer).

### Inline lemmas

**Lemma A (one-step perturbation).** Let $n, n' \in \mathbb{Z}^+$ with $n' = n + 2^j m$ for
some integers $j \ge 1$ and $m$ (positive or negative). Then
$$T(n') = T(n) + 3^{v_0(n)}\, 2^{j-1} m .$$

*Proof.* Since $j \ge 1$, $n' \equiv n \pmod 2$, so $n$ and $n'$ have the same parity and
$v_0(n') = v_0(n)$. Also $2^{j-1}m \in \mathbb{Z}$.
If $n$ is even: $T(n') = (n + 2^j m)/2 = n/2 + 2^{j-1} m = T(n) + 3^0 2^{j-1} m$, and
$v_0(n) = 0$.
If $n$ is odd: $T(n') = \bigl(3(n + 2^j m) + 1\bigr)/2 = (3n+1)/2 + 3 \cdot 2^{j-1} m
= T(n) + 3^1 2^{j-1} m$, and $v_0(n) = 1$. $\square$

**Lemma B (transport / parity-word locality).** Let $k \ge 1$ and $n, n' \in \mathbb{Z}^+$
with $n' = n + 2^k m$, $m \in \mathbb{Z}$. Then for all $0 \le l \le k$:
$$T^l(n') = T^l(n) + 3^{a_l(n)}\, 2^{k-l} m,$$
and $v_l(n') = v_l(n)$ for all $0 \le l \le k - 1$. Consequently:

* $v_i(n)$ depends only on $n \bmod 2^{i+1}$ (take $k = i + 1$);
* the parity word of length $k$, the counts $a_j$ ($j \le k$), and the constants
  $\rho_j$ ($j \le k$) are well-defined functions of the class $n \bmod 2^k$.

*Proof.* Induction on $l$. For $l = 0$: $a_0 = 0$ (empty sum, D-9906), and the claim is
$n' = n + 2^k m$, true. Assume the displayed identity for some $l < k$. Since
$k - l \ge 1$, Lemma A applies to the pair $T^l(n)$, $T^l(n') = T^l(n) + 2^{k-l}(3^{a_l(n)} m)$
(both in $\mathbb{Z}^+$ because $T$ maps $\mathbb{Z}^+$ to itself), with $j = k - l$ and
perturbation integer $3^{a_l(n)}m$; first, parity equality gives
$v_l(n') = v_l(n) =: v$. Then
$$T^{l+1}(n') = T^{l+1}(n) + 3^{v}\, 2^{k-l-1}\, 3^{a_l(n)} m
            = T^{l+1}(n) + 3^{a_{l+1}(n)}\, 2^{k-(l+1)} m,$$
using $a_{l+1} = a_l + v_l$ (D-9906). This completes the induction; the parity statement
was obtained for every $l < k$ along the way. The two consequences are immediate: any two
positive members of a class $r \bmod 2^{i+1}$ (resp. $r \bmod 2^k$) differ by $2^{i+1}m$
(resp. $2^k m$) for some $m \in \mathbb{Z}$, and $\rho_j$ is defined from the word alone. $\square$

*Relation to L-9902:* Lemma B is the "residue determines word" direction of the full
parity-word bijection, which a parallel file proves as L-9902; nothing from L-9902 is
used here.

**Lemma C (iteration formula).** For all $n \in \mathbb{Z}^+$ and $j \ge 0$:
$$T^j(n) = \frac{3^{a_j(n)}\, n + \rho_j}{2^j},$$
where $\rho_0 = 0$ and $\rho_{i+1} = 3^{v_i(n)}\rho_i + v_i(n)\,2^i$. Moreover
$\rho_j \ge 0$, and $\rho_j$ depends only on the word $(v_0, \dots, v_{j-1})$; explicitly
$\rho_j = \sum_{0 \le i < j} v_i\, 3^{\,a_j - a_{i+1}}\, 2^i$.

*Proof.* Induction on $j$. Base $j = 0$: $T^0(n) = n = (3^0 n + 0)/2^0$. Step: assume
$2^i\, T^i(n) = 3^{a_i} n + \rho_i$.
If $v_i = 0$ ($T^i(n)$ even): $T^{i+1}(n) = T^i(n)/2$, so
$2^{i+1} T^{i+1}(n) = 2^i T^i(n) = 3^{a_i} n + \rho_i$, and indeed $a_{i+1} = a_i$,
$\rho_{i+1} = 3^0 \rho_i + 0 = \rho_i$.
If $v_i = 1$ ($T^i(n)$ odd): $T^{i+1}(n) = (3\,T^i(n) + 1)/2$, so
$2^{i+1} T^{i+1}(n) = 3 \cdot 2^i\, T^i(n) + 2^i = 3^{a_i + 1} n + (3\rho_i + 2^i)$, and
indeed $a_{i+1} = a_i + 1$, $\rho_{i+1} = 3\rho_i + 2^i$.
Nonnegativity: $\rho_0 = 0$ and the recursion has nonnegative coefficients.
Word-dependence: the recursion consumes only $(v_0, \dots, v_{j-1})$.
Closed form: induction again; if
$\rho_j = \sum_{i<j} v_i 3^{a_j - a_{i+1}} 2^i$ then
$\rho_{j+1} = 3^{v_j}\rho_j + v_j 2^j
= \sum_{i<j} v_i 3^{(a_j + v_j) - a_{i+1}} 2^i + v_j 3^{a_{j+1}-a_{j+1}} 2^j
= \sum_{i<j+1} v_i 3^{a_{j+1} - a_{i+1}} 2^i$. $\square$

*Relation to L-9903:* only existence, nonnegativity and word-dependence of $\rho_j$ are
needed here; sharp upper/lower bounds are L-9903's business and are not used.

**Lemma D (irrationality and the ceiling criterion).**
$2^s = 3^t$ has no solution with $s, t \in \mathbb{Z}$, $s \ge 1$, $t \ge 0$. Hence
$\gamma = \log_3 2$ is irrational, $j\gamma \notin \mathbb{Z}$ for every integer $j \ge 1$,
and for all integers $a \ge 0$, $j \ge 1$:
$$3^a \ge 2^j \iff 3^a > 2^j \iff a > j\gamma \iff a \ge \lceil j\gamma \rceil .$$

*Proof.* If $2^s = 3^t$ with $s \ge 1$ then the left side is even and the right side is
odd — impossible (equivalently: unique factorization). If $\gamma = t/s$ with
$s \ge 1, t \ge 0$ integers, then $2 = 3^{\gamma}$ gives $2^s = 3^{t}$, impossible; and
$\gamma > 0$, so $\gamma$ is irrational. If $j\gamma = a \in \mathbb{Z}$ for some $j \ge 1$
then $\gamma = a/j$ would be rational. For the chain: taking $\log_3$ (strictly
increasing) gives $3^a \ge 2^j \iff a \ge j\gamma$, and $a = j\gamma$ is impossible
($j\gamma \notin \mathbb{Z}$), so $a \ge j\gamma \iff a > j\gamma$; finally, for an integer
$a$ and any real $\beta \notin \mathbb{Z}$, $a > \beta \iff a \ge \lceil \beta \rceil$ by
definition of the ceiling. $\square$

### Proof of L-9909.1

**Part 1 (parametrization).**

($\subseteq$) Let $x \in \mathbb{Z}^+$ be odd with $S(x) = n$, and put
$k := \nu_2(3x+1)$. Since $x$ is odd, $3x + 1$ is even and $\ge 4$, so $k \ge 1$. By
D-9904, $n = S(x) = (3x+1)/2^k$, i.e. $3x + 1 = 2^k n$, i.e. $3x = 2^k n - 1$. Hence
$3 \mid 2^k n - 1$, i.e. $2^k n \equiv 1 \pmod 3$, so $k \in A(n)$; and
$x = (2^k n - 1)/3 = x_k$.

($\supseteq$) Let $k \in A(n)$ and $x_k := (2^k n - 1)/3$. Check every required property:

* *Integrality*: $2^k n \equiv 1 \pmod 3$ means $3 \mid 2^k n - 1$, so $x_k \in \mathbb{Z}$.
* *Positivity*: $k \ge 1$ and $n \ge 1$ give $2^k n - 1 \ge 1$, so $x_k \ge 1/3$; being
  an integer, $x_k \ge 1$, i.e. $x_k \in \mathbb{Z}^+$.
* *Automatic oddness*: $3x_k = 2^k n - 1$ is odd (as $k \ge 1$ makes $2^k n$ even), and
  $3x_k$ odd forces $x_k$ odd.
* *Automatic exact valuation*: $3x_k + 1 = 2^k n$ with $n$ odd, so
  $\nu_2(3x_k + 1) = \nu_2(2^k) + \nu_2(n) = k + 0 = k$ exactly.
* *It is a preimage*: $S(x_k) = (3x_k+1)/2^{\nu_2(3x_k+1)} = 2^k n / 2^k = n$.

(*Bijectivity.*) The map $k \mapsto x_k = (2^k n - 1)/3$ is strictly increasing in $k$
(for fixed $n \ge 1$, $2^k n - 1$ is strictly increasing), hence injective on $A(n)$; it
is surjective onto $S^{-1}(n)$ by ($\subseteq$), which also shows the inverse map is
$x \mapsto \nu_2(3x+1)$. So it is a strictly increasing bijection.

**Part 2 (case analysis).** Since $2 \equiv -1 \pmod 3$, we have
$2^k n \equiv (-1)^k n \pmod 3$. As $(-1)^k \in \{1, -1\}$ and $1 \not\equiv -1 \pmod 3$:

* $n \equiv 0$: $2^k n \equiv 0 \not\equiv 1$ for every $k$, so $A(n) = \varnothing$ and $n$
  is a leaf.
* $n \equiv 1$: $(-1)^k n \equiv (-1)^k \equiv 1 \iff k$ even; with $k \ge 1$,
  $A(n) = \{2, 4, 6, \dots\}$.
* $n \equiv 2 \equiv -1$: $(-1)^k n \equiv (-1)^{k+1} \equiv 1 \iff k$ odd;
  $A(n) = \{1, 3, 5, \dots\}$.

In the last two cases $A(n)$ is infinite, so $S^{-1}(n)$ is infinite by Part 1.

**Part 3 (bonus, leaf distribution).** Let $3 \nmid n$, $k \in A(n)$, and write
$u := 2^k n \bmod 9 $. Since $2^k n \equiv 1 \pmod 3$, $u \in \{1, 4, 7\}$. Writing
$2^k n = 9t + u$ ($t \in \mathbb{Z}_{\ge 0}$) we get
$$x_k = \frac{9t + u - 1}{3} = 3t + \frac{u-1}{3}, \qquad \text{so} \qquad
x_k \equiv \frac{u - 1}{3} \pmod 3,$$
where $(u-1)/3 \in \{0, 1, 2\}$ for $u \in \{1, 4, 7\}$ respectively. Consecutive
admissible exponents differ by exactly 2 (Part 2), and
$2^{k+2} n \equiv 4 \cdot 2^k n \pmod 9$; the map $u \mapsto 4u \bmod 9$ acts on
$\{1, 4, 7\}$ as the 3-cycle $1 \to 4 \to 7 \to 1$ (check: $4\cdot1 = 4$,
$4\cdot4 = 16 \equiv 7$, $4\cdot 7 = 28 \equiv 1 \pmod 9$). Hence along
$k_0 < k_1 < k_2 < \dots$ the value $(u-1)/3$, i.e. $x_{k_i} \bmod 3$, increases by
$1 \pmod 3$ at each step: $x_{k_i} \equiv e_0 + i \pmod 3$ with
$e_0 = (u_0 - 1)/3$, $u_0 = 2^{k_0} n \bmod 9$. It remains to evaluate $u_0$ from
$n \bmod 9$ (which determines $2^{k_0} n \bmod 9$ since $k_0$ is determined by
$n \bmod 3$):

| $n \bmod 9$ | $k_0$ | $u_0 = 2^{k_0} n \bmod 9$ | $e_0 = (u_0-1)/3$ |
|---|---|---|---|
| 1 | 2 | $4$ | 1 |
| 4 | 2 | $16 \equiv 7$ | 2 |
| 7 | 2 | $28 \equiv 1$ | 0 |
| 2 | 1 | $4$ | 1 |
| 5 | 1 | $10 \equiv 1$ | 0 |
| 8 | 1 | $16 \equiv 7$ | 2 |

This is the table in the Statement. The "exactly one leaf in three" phrasing follows since
$x \equiv 0 \pmod 3$ occurs for exactly one residue of the 3-cycle. $\square$

### Proof of L-9909.2

First note $1 \notin K$: $O_C(1)$ contains its index-0 term $1$ (D-9905 with $k = 0$).

**(F) Forward closure.** Let $n \in K$ and suppose toward a contradiction
$C(n) \notin K$, i.e. $C^i(C(n)) = 1$ for some $i \ge 0$. Then $C^{i+1}(n) = 1$, so
$1 \in O_C(n)$, contradicting $n \in K$. Hence $C(n) \in K$. By induction on $j$,
$C^j(n) \in K$ for every $j \ge 0$; these are exactly the elements of $O_C(n)$.

**(B) Backward closure.** Let $n = C^j(m)$ ($j \ge 0$) and $n \in K$; suppose toward a
contradiction $m \notin K$, i.e. $C^i(m) = 1$ for some $i \ge 0$. Two cases.

* If $i \ge j$: $C^{i-j}(n) = C^{i-j}(C^j(m)) = C^i(m) = 1$, so $1 \in O_C(n)$ —
  contradiction.
* If $i < j$: $n = C^j(m) = C^{j-i}(C^i(m)) = C^{j-i}(1)$. By direct computation
  $C(1) = 4$, $C(4) = 2$, $C(2) = 1$, so by induction $C^t(1) \in \{1, 2, 4\}$ for all
  $t \ge 0$; thus $n \in \{1, 2, 4\}$. Each of these reaches 1 ($1$ in $0$ steps, $2$ in
  $1$ step, $4$ in $2$ steps), so $1 \in O_C(n)$ — contradiction.

Hence $m \in K$.

**(E) Explicit backward edges.** Let $n \in K$.

* $2n$: $C(2n) = n$ (as $2n$ is even), so $n \in O_C(2n)$; by (B) with $m = 2n$,
  $2n \in K$.
* $(2n-1)/3$ for $n \equiv 2 \pmod 3$: put $x := (2n-1)/3$.
  *Integrality*: $2n - 1 \equiv 2\cdot 2 - 1 = 3 \equiv 0 \pmod 3$.
  *Positivity*: $n \equiv 2 \pmod 3$ forces $n \ge 2$, so $x \ge (4-1)/3 = 1$, i.e.
  $x \in \mathbb{Z}^+$. *Oddness*: $3x = 2n - 1$ is odd, so $x$ is odd.
  *Edge*: $x$ odd gives $C(x) = 3x + 1 = 2n$, and $C(2n) = n$; hence
  $n = C^2(x) \in O_C(x)$, and (B) gives $x \in K$.

This is verbatim the pair of closure hypotheses of issue #25, with the integrality
condition for the second map characterized by $2n - 1 \equiv 0 \pmod 3
\iff n \equiv 2 \pmod 3$ (multiply $2n \equiv 1$ by $2$, the inverse of $2$ mod 3).

**(M) Minimal counterexample.** Assume $K \neq \varnothing$ and let $\mu = \min K$.

*(i) $\mu$ odd, $\mu \ge 3$.* Since $1 \notin K$, $\mu \ge 2$. If $\mu$ were even, then
$C(\mu) = \mu/2 \in \mathbb{Z}^+$ belongs to $K$ by (F), and $\mu/2 < \mu$ — contradicting
minimality. So $\mu$ is odd; with $\mu \ge 2$ this gives $\mu \ge 3$.

*(ii) $\mu \equiv 3 \pmod 4$.* By (i), $\mu$ is odd, so $\mu \equiv 1$ or $3 \pmod 4$.
Suppose $\mu \equiv 1 \pmod 4$. By (i) $\mu \ge 3$ and $\mu \neq 1$, so $\mu \ge 5$.
Follow the $C$-orbit three steps, verifying each step's legality:

* $\mu$ odd $\Rightarrow C(\mu) = 3\mu + 1$. From $\mu \equiv 1 \pmod 4$:
  $3\mu + 1 \equiv 3 + 1 = 4 \equiv 0 \pmod 4$, so $4 \mid 3\mu + 1$ — this is the
  **integrality** fact making the next two halvings exact.
* $3\mu + 1$ even $\Rightarrow C^2(\mu) = (3\mu+1)/2$; and $4 \mid 3\mu+1$ makes
  $(3\mu+1)/2$ **even**.
* Hence $C^3(\mu) = (3\mu+1)/4 \in \mathbb{Z}^+$ (positivity: $\ge (3\cdot 5 + 1)/4 = 4$).

So $(3\mu+1)/4 \in O_C(\mu)$, whence $(3\mu+1)/4 \in K$ by (F). **Size comparison:**
$(3\mu+1)/4 < \mu \iff 3\mu + 1 < 4\mu \iff 1 < \mu$, which holds ($\mu \ge 5$). So
$(3\mu+1)/4$ is an element of $K$ strictly smaller than $\mu$ — contradiction. Hence
$\mu \equiv 3 \pmod 4$.

*(iii) $\sigma(\mu) = \infty$.* First, an inline sub-lemma:

> **Sub-lemma (T-orbit inside C-orbit).** For every $n \in \mathbb{Z}^+$ and $j \ge 0$,
> $T^j(n) \in O_C(n)$.
> *Proof.* Induction on $j$; $j = 0$ is the index-0 term. Suppose $T^j(n) = C^t(n)$.
> If $T^j(n)$ is even, $T^{j+1}(n) = T^j(n)/2 = C(T^j(n)) = C^{t+1}(n)$. If $T^j(n)$ is
> odd, then $C(T^j(n)) = 3T^j(n)+1$ is even and
> $T^{j+1}(n) = (3T^j(n)+1)/2 = C(C(T^j(n))) = C^{t+2}(n)$. $\square$

Now suppose toward a contradiction that $T^j(\mu) < \mu$ for some $j \ge 1$. By the
sub-lemma, $T^j(\mu) \in O_C(\mu)$; by (F) every element of $O_C(\mu)$ is in $K$; so
$T^j(\mu) \in K$. Also $T^j(\mu) \in \mathbb{Z}^+$ ($T$ maps $\mathbb{Z}^+$ to itself). Thus
$T^j(\mu)$ is an element of $K$ strictly smaller than $\mu$ — contradicting minimality.
Hence $T^j(\mu) \ge \mu$ for **all** $j \ge 1$, so the set $\{k \ge 1 : T^k(\mu) < \mu\}$
is empty and $\sigma(\mu) = \inf \varnothing = \infty$ per D-9910. $\square$

### Proof of L-9909.3

Fix $k \ge 1$ and the class $r \bmod 2^k$. By Lemma B, all positive members of the class
share the word $(v_0,\dots,v_{k-1})$, hence the counts $a_j$ and (Lemma C) the constants
$\rho_j$, for $0 \le j \le k$: these are class constants, and the reasoning below never
uses anything about $n$ beyond $n \equiv r \pmod{2^k}$ and $n \in \mathbb{Z}^+$ — this is the
required **uniformity**.

Let $n \equiv r \pmod{2^k}$, $n \in \mathbb{Z}^+$, and $1 \le j \le k$. Lemma C gives the
exact identity
$$2^j\bigl(T^j(n) - n\bigr) = \bigl(3^{a_j} - 2^j\bigr)\,n + \rho_j. \tag{$\ast$}$$

**(a)** Assume $3^{a_j} \ge 2^j$. If $a_j = 0$ then $3^{a_j} = 1 < 2 \le 2^j$, impossible;
so $a_j \ge 1$, and then $3^{a_j}$ is odd while $2^j$ is even (as $j \ge 1$), so
$3^{a_j} \neq 2^j$ (this is Lemma D's strictness; unique factorization/parity). Hence
$3^{a_j} - 2^j \ge 1$, and ($\ast$) gives
$$2^j\bigl(T^j(n) - n\bigr) \ \ge\ n + \rho_j \ \ge\ n \ \ge\ 1 > 0,$$
using $\rho_j \ge 0$ (Lemma C). So $T^j(n) > n$ for **every** $n$ in the class. Note the
hypothesis $3^{a_j} \ge 2^j$ is equivalent to $a_j \ge \lceil j\gamma\rceil$ by Lemma D.

**(b)** Assume $3^{a_j} < 2^j$ and set $d_j := 2^j - 3^{a_j} \ge 1$. Then ($\ast$) reads
$$2^j\bigl(T^j(n) - n\bigr) = \rho_j - d_j\, n,$$
so, comparing $n$ with the class constant $\rho_j / d_j$ (an explicitly computable
nonnegative rational, by the recursions of Lemma C):
$$T^j(n) < n \iff n > \rho_j/d_j, \qquad
T^j(n) = n \iff n = \rho_j/d_j, \qquad
T^j(n) > n \iff n < \rho_j/d_j.$$
In particular **every** $n$ in the class with $n > \rho_j/d_j$ satisfies $T^j(n) < n$.

**Corollary.**

1. If $r$ is a $k$-survivor, then by definition no $j \le k$ is failing, i.e.
   $3^{a_j} \ge 2^j$ for all $1 \le j \le k$; by (a), every $n$ in the class satisfies
   $T^j(n) > n$ for all $1 \le j \le k$. Hence no $j \le k$ witnesses descent and
   $\sigma(n) > k$ (D-9910) — uniformly on the class.
2. Let $\sigma(n) > k$, i.e. $T^j(n) \ge n$ for all $1 \le j \le k$, and suppose the class
   $r = n \bmod 2^k$ is **not** a $k$-survivor. Pick any failing index $j \le k$. If
   $n > \rho_j/d_j$ then (b) gives $T^j(n) < n$, so $\sigma(n) \le j \le k$ —
   contradiction. Hence $n \le \rho_j/d_j \le B_k$ (the quotient for the pair $(r, j)$
   participates in the maximum defining $B_k$). Finiteness and computability of $B_k$:
   it is a maximum of at most $k\,2^k$ explicitly computable rationals; nonemptiness of
   the index set was noted in the Definitions.
3. Monotonicity $B_k \le B_{k+1}$: every pair (class $r \bmod 2^k$, failing $j \le k$)
   contributing to $B_k$ lifts to (class $r \bmod 2^{k+1}$, same $j$) — the lifted class
   has the same length-$k$ word prefix (Lemma B: $v_i$ depends on $n \bmod 2^{i+1}$,
   $i+1 \le k$, determined by $r \bmod 2^k$), hence the same $a_j, \rho_j, d_j$, hence
   contributes the same quotient to the (larger) index set defining $B_{k+1}$. So the
   defining set for $B_k$ is a subset of that for $B_{k+1}$.
4. By L-9909.2(M)(iii), $\sigma(\mu) = \infty > k$ for every $k$. Apply item 2: for each
   $k$, either $\mu \bmod 2^k$ is a $k$-survivor or $\mu \le B_k$. So whenever
   $\mu > B_k$, the class $\mu \bmod 2^k$ is a $k$-survivor. $\square$

*Boundary remark (adversarially relevant).* The strictness "$n > \rho_j/d_j$" in (b)
cannot be weakened to "$\ge$": $n = 1$ lies in the class $1 \bmod 4$ with word $(1,0)$,
$a_2 = 1$, $\rho_2 = 1$, $d_2 = 4 - 3 = 1$, threshold $\rho_2/d_2 = 1$, and indeed
$T^2(1) = 1 = n$ exactly (no descent). This is why $\sigma(1) = \infty$ coexists with
$1$ lying in a non-survivor class — $1 \le B_2 = 2$, consistent with Corollary item 2.

### Proof of L-9909.4

**Role of computation, stated precisely.** L-9909.4 has three ingredients with different
epistemic statuses:

* (a) The survivor lists, counts, densities, and the exact values $B_1, \dots, B_8$.
  These are **exact finite evaluations** of quantities that L-9909.3 *proved* to be
  well-defined class constants: for each of the $2^k \le 256$ classes, the word is read
  off a representative via $k \le 8$ iterations of $T$ (legitimate by Lemma B), and
  $a_j, \rho_j$ follow the proved recursions in exact integer arithmetic; $B_k$ is an
  exact `Fraction` maximum. There is no sampling and no extrapolation: the computed
  objects are precisely the finitely many objects the theorem speaks about. (Script
  `l9909_sieve.py`, code and full output in Adversarial tests.)
* (b) **X-9901** is a *finite verification* (per NOTATION.md conventions, labeled as
  such, never as "proof of the conjecture on an infinite set"): for every
  $n \le N_0 = \max(B_8, 10^6) = 10^6$ — note $B_8 = 1688/13 < 130 < 10^6$, so the
  binding bound is $10^6$ — the script verifies **directly** that the $C$-orbit of $n$
  descends strictly below $n$ (with a hard iteration cap that was never hit), and then
  concludes "every $n \le 10^6$ reaches 1" by strong induction on $n$: base $n = 1$
  ($C^0(1)=1$); step: if every $m < n$ reaches 1 and the orbit of $n$ reaches some
  $m < n$, then the orbit of $n$ reaches 1 by composing the two orbit segments
  ($C^{t'}(C^{t}(n)) = C^{t+t'}(n)$). Recorded observables: max total $C$-stopping time
  $524$ at $n = 837799$. This finite, decidable hypothesis is exactly what the theorem
  below consumes — using a finite computation to discharge an explicitly finite
  hypothesis is legitimate proof material.
* (c) The **theorem**: *if a counterexample exists then $\mu > 10^6$ and $\mu \bmod 2^k$
  is a $k$-survivor for every $k \le 8$.* Proof: X-9901 shows every $n \le 10^6$ reaches
  1 under $C$, so no $n \le 10^6$ is in $K$; since $\mu \in K$, $\mu > 10^6$. By (a) and
  Corollary item 3 (or directly from the table), $B_k \le B_8 = 1688/13 < 10^6 < \mu$ for
  every $k \le 8$; Corollary item 4 then forces $\mu \bmod 2^k$ to be a $k$-survivor for
  each $k \le 8$. The congruence lists in the Statement are then just the computed
  survivor lists. $\square$

**Computed values.** As tabulated in the Statement: $\lceil k\gamma\rceil$ for
$k = 1..8$ is $1, 2, 2, 3, 4, 4, 5, 6$ (computed as $\min\{a \ge 0 : 3^a \ge 2^k\}$,
pure integer comparisons — no floating point; equality with $\lceil k\gamma\rceil$ is
Lemma D); survivor counts $1, 1, 2, 3, 4, 8, 13, 19$; densities
$1/2, 1/4, 1/4, 3/16, 1/8, 1/8, 13/128, 19/256$;
$B_k = 0,\ 2,\ 2,\ 20/7,\ 76/5,\ 76/5,\ 76/5,\ 1688/13$. The maximizing datum for $B_8$
is the class $r = 248 \bmod 256$ (word $(0,0,0,1,1,1,1,1)$, $a_8 = 5$, $\rho_8 = 1688$,
$d_8 = 256 - 243 = 13$). Hand check of that class: $T^8(n) = (243 n + 1688)/256$; for
$n = 248$: $(243 \cdot 248 + 1688)/256 = 61952/256 = 242$, matching the direct orbit
$248 \to 124 \to 62 \to 31 \to 47 \to 71 \to 107 \to 161 \to 242$, and $242 < 248$
(consistent: $248 > B_8 \approx 129.85$, class not a survivor).

**Cross-check against L-9909.2 (required consistency audit).** The 1-survivor list
$\{1\} \bmod 2$ says: $\mu \equiv 1 \pmod 2$ — this is L-9909.2(M)(i) ($\mu$ odd),
re-derived independently through the sieve. The 2-survivor list $\{3\} \bmod 4$ says:
$\mu \equiv 3 \pmod 4$ — this is **exactly** L-9909.2(M)(ii), reappearing as predicted.
Additionally, every $k$-survivor class for $k \ge 2$ reduces mod 4 to $3$ (verified in
the script's reduction-consistency check), so the higher-$k$ restrictions refine, and
never contradict, the low-$k$ ones. **No discrepancy anywhere**; had the mod-4 survivor
list contained $1$, or a survivor class reduced to a non-survivor, that would have
falsified either L-9909.2(ii), Lemma B, or the script — it did not occur.

### Proof of L-9909.5

By L-9909.4(c), a program searching for counterexamples may discard every non-survivor
class mod $2^k$ ($k \le 8$) outright; more generally, for arbitrary $k$, any candidate
$n > B_k$ in a non-survivor class mod $2^k$ is provably not a minimal counterexample
(Corollary item 4), and — via Corollary item 2 — is provably not an integer with
$\sigma(n) > k$ at all, which also prunes searches for high-stopping-time or divergent
orbits. (For non-minimal counterexamples in general position no congruence restriction
is claimed; the restriction is on $\mu$, which suffices: $K \neq \varnothing$ iff
$\mu$ exists.)

*Densities are nonincreasing.* If $r' \bmod 2^{k+1}$ is a $(k+1)$-survivor then its
reduction $r' \bmod 2^k$ is a $k$-survivor (same word prefix by Lemma B, and the survivor
condition for $k+1$ includes all conditions $j \le k$). Each class mod $2^k$ has exactly
two lifts mod $2^{k+1}$, so $\#\mathrm{Surv}(k{+}1) \le 2\,\#\mathrm{Surv}(k)$ and the
density $\#\mathrm{Surv}(k)/2^k$ is nonincreasing in $k$. The computed sequence
$1/2, 1/4, 1/4, 3/16, 1/8, 1/8, 13/128, 19/256$ confirms this, and shows the decay is
**not strict** at $k = 2 \to 3$ and $5 \to 6$ (these are exactly the levels where
$\lceil k\gamma \rceil = \lceil (k-1)\gamma \rceil$ fails to add a fresh constraint —
observation, not needed for any claim).

*Forward pointer (not proved here).* A planned lemma **L-9908** is expected to prove that
the survivor density tends to 0 exponentially in $k$ (Terras-style: survivor words
require $a_j \ge \lceil j\gamma\rceil$ for all $j \le k$ with $\gamma > 1/2$, a
large-deviation event for the count $a_k$ among the $2^k$ equidistributed words). This
file deliberately proves nothing in that direction and no later file may cite L-9909 for
it. $\square$

---

## Dependency audit

Used from `NOTATION.md` (definitions only, no external lemmas):

* D-9901 ($C$): L-9909.2 throughout (orbit steps, closure).
* D-9902 ($T$): Lemmas A–C, L-9909.2(M)(iii), L-9909.3.
* D-9903/D-9904 ($\mathrm{odd}$, $S$, exponent $a(x) = \nu_2(3x+1)$): L-9909.1.
* D-9905 (orbits, "reaches 1", index-0 convention $M^0(n) = n$, trivial cycles):
  L-9909.2 — the $k = 0$ convention is load-bearing in "$1 \notin K$" and in backward
  closure case $i < j$.
* D-9906 ($v_i$, $a_k$, empty sum $a_0 = 0$): Lemmas B, C; survivor definition.
* D-9909 (counterexample): definition of $K$; neutrality framing.
* D-9910 ($\sigma$, with $\inf \varnothing = \infty$): L-9909.2(M)(iii), Corollary
  items 1–2.
* $\gamma = \log_3 2$: Lemma D and the survivor criterion.

Internal dependency order (acyclic): Lemma A → Lemma B → (class words well defined);
Lemma C independent of A–B except sharing D-9906; Lemma D independent;
L-9909.1 independent of the lemmas; L-9909.2 independent of L-9909.1;
L-9909.3 uses B, C, D; Corollary item 4 uses L-9909.2(M)(iii);
L-9909.4 uses L-9909.3 + L-9909.2 + finite computations (a), (b);
L-9909.5 uses L-9909.3/4 + Lemma B.

Related files, explicitly **not** relied on: L-9902 (full word↔residue bijection; here
only the "residue determines word" direction is needed and is re-proved as Lemma B),
L-9903 (sharp bounds on $\rho_j$; here only $\rho_j \ge 0$ and word-dependence are
needed and are re-proved as Lemma C). Overlap is intentional per the packet convention
(NOTATION.md, Conventions): whichever file lands first, neither cites the other for a
needed step. No dependence on CURRENT_STATE/CLAIMS ledgers. Issue #25 is a *consumer*
of L-9909.2(E), not a dependency.

## Gap audit

Deliberate search against the README §8 checklist:

* *Hidden finiteness assumptions*: the only finiteness used is in L-9909.4 — and it is
  explicit: the class enumeration is finite by construction ($2^k$ classes, $k \le 8$),
  and X-9901's hypothesis is finite by design ($n \le 10^6$). Nothing infinite is
  concluded from it beyond the stated implication about $\mu$.
* *Unjustified induction*: the inductions (Lemma B on $l$; Lemma C on $j$; sub-lemma on
  $j$; $C^t(1) \in \{1,2,4\}$ on $t$; X-9901's strong induction on $n$) all have explicit
  bases and steps written out.
* *Boundary cases*: $n = 1$ (non-survivor class yet $\sigma = \infty$) is treated
  explicitly and shown consistent via the strict inequality in (b) and $B_2 = 2 \ge 1$;
  $k$-vs-$j$ index edges ($j = 0$ trivial, $j \ge 1$ required for parity of $2^j$;
  $l = k$ endpoint in Lemma B has no parity claim); $r = 0$ class handled via positive
  representative $2^k$; $\mu = 1$ excluded before (ii) uses $\mu \ge 5$; the case
  $i < j$ in backward closure (orbit already past 1) is fully argued — omitting it is
  the classic error in this closure proof.
* *Empirical vs universal*: every computational statement is fenced inside L-9909.4/
  Adversarial tests and labeled finite verification / exact finite evaluation; the
  universal statements (L-9909.1–3, 5) have computation-free proofs.
* *Nonuniform estimates*: the sieve's whole content is uniformity; the proof of (a)/(b)
  manipulates the single identity ($\ast$) whose coefficients are class constants, and no
  step branches on $n$ beyond its class membership. No "for $n$ large enough" is used
  anywhere except through the explicit constant $\rho_j/d_j$.
* *Assumptions equivalent to the conjecture*: L-9909.2 and Corollary item 4 are
  conditional on $K \neq \varnothing$ in the correct direction (they constrain a
  counterexample; they do not assert or deny its existence). X-9901 is strictly weaker
  than the conjecture (finite range).
* *Circular dependence*: none; see the acyclic order above. In particular the file never
  cites L-9902/L-9903.
* *Symbolic object vs integer trajectory*: all preimages and orbit elements are proved to
  be positive integers at their point of use (integrality/positivity checks in
  L-9909.1 Part 1, L-9909.2(E), L-9909.2(M)(ii)).
* *Finite computation extrapolated to infinite behavior*: the only place a computation
  feeds a theorem is L-9909.4(c), where the computation's finite scope ($n \le 10^6$;
  $256$ classes) exactly matches the hypothesis consumed. The $k > 8$ and $n > 10^6$
  regimes are covered only by the proved, computation-free Corollary (with the explicit
  caveat $\mu > B_k$).
* *Known deliberate weakenings*: $B_k$ uses max over all failing $j$ (not the sharper
  per-class min) — stated openly in Definitions; statement (a) proves the stronger
  strict inequality; neither weakening/strengthening affects any downstream claim.

## Adversarial tests

Three scripts, Python 3 (stdlib only; exact integer / `Fraction` arithmetic; no floats in
any decision), stored in the session scratchpad and reproduced in full here.
Environment: CPython 3 on Linux; deterministic, no seeds. All tests **PASS**.

### Script 1: `l9909_sieve.py` — survivors, $B_k$, and class-uniformity brute force

Checks performed: (1) exact survivor lists/counts and $B_k$ for $k \le 8$;
(2) reduction consistency (every $(k{+}1)$-survivor reduces to a $k$-survivor);
(3) brute force over $n = r + 2^k t$, $t = 0..199$ (i.e. all $n \le 2^k \cdot 200$),
$k \le 6$: word constancy on each class, the exact identity
$2^j T^j(n) = 3^{a_j} n + \rho_j$, prediction (a) on survivor classes (strict), and
prediction (b) on non-survivor classes including the equality boundary; (4) that the
brute-force-identified set $\{r : T^j(n) \ge n\ \forall j \le k, \forall$ sampled
$n\}$ coincides with the survivor list.

```python
#!/usr/bin/env python3
# l9909_sieve.py -- L-9909.3 / L-9909.4: exact k-survivor classes mod 2^k (k<=8),
# exact class constants B_k, and adversarial brute-force check of class uniformity.
# Agent: fable-02-p7. Python 3 stdlib only; all arithmetic exact (int / Fraction).
from fractions import Fraction

def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def class_data(r, k):
    """Word (v_0..v_{k-1}), counts a[0..k], constants rho[0..k] of the class r mod 2^k.
    Computed from the positive representative r (or 2^k if r == 0); by locality
    (proved in L-9909.3) these depend only on the class."""
    n = r if r > 0 else 2 ** k
    v, a, rho = [], [0], [0]
    x = n
    for i in range(k):
        vi = x & 1
        v.append(vi)
        a.append(a[-1] + vi)
        rho.append(3 ** vi * rho[-1] + vi * 2 ** i)
        x = T(x)
    return v, a, rho

def ceil_j_gamma(j):
    """ceil(j * log_3 2) = min{a >= 0 : 3^a >= 2^j} for j >= 1 (exact integers)."""
    a = 0
    while 3 ** a < 2 ** j:
        a += 1
    return a

KMAX = 8
print("j -> ceil(j*gamma):", {j: ceil_j_gamma(j) for j in range(1, KMAX + 1)})
print()

survivors = {}
for k in range(1, KMAX + 1):
    surv = []
    best = Fraction(0)
    arg = None
    for r in range(2 ** k):
        v, a, rho = class_data(r, k)
        ok = True
        for j in range(1, k + 1):
            if 3 ** a[j] < 2 ** j:          # failing j (equiv. a_j < ceil(j*gamma))
                ok = False
                val = Fraction(rho[j], 2 ** j - 3 ** a[j])
                if val > best:
                    best, arg = val, (r, j, rho[j], 2 ** j - 3 ** a[j])
        if ok:
            surv.append(r)
    survivors[k] = surv
    print(f"k={k}: survivors={len(surv)}/{2**k}  density={len(surv)/2**k:.6f}  "
          f"B_{k} = {best} = {float(best):.6f}  argmax (r, j, rho_j, 2^j-3^a_j) = {arg}")
    if k <= 6:
        print(f"   survivor classes mod {2**k}: {surv}")
        for r in surv:
            v, a, rho = class_data(r, k)
            print(f"     r={r:3d}: word={tuple(v)}  (a_1..a_{k})=({','.join(map(str, a[1:]))})")
    else:
        print(f"   survivor classes mod {2**k}: {surv}")
print()

# consistency: reductions of (k+1)-survivors are k-survivors
for k in range(1, KMAX):
    red = sorted(set(r % 2 ** k for r in survivors[k + 1]))
    assert set(red) <= set(survivors[k]), k
print("reduction consistency: every (k+1)-survivor reduces to a k-survivor: PASS")
print()

print("== Adversarial test 1: class uniformity, k <= 6, n = r + 2^k*t, t = 0..199 ==")
for k in range(1, 7):
    checked = 0
    sigma_gt_k_all = []          # classes where ALL sampled n have T^j(n) >= n, j <= k
    for r in range(2 ** k):
        v, a, rho = class_data(r, k)
        fail_js = [j for j in range(1, k + 1) if 3 ** a[j] < 2 ** j]
        bounds = {j: Fraction(rho[j], 2 ** j - 3 ** a[j]) for j in fail_js}
        all_sigma_gt = True
        for t in range(200):
            n = r + 2 ** k * t
            if n == 0:
                continue
            traj = [n]
            x = n
            for _ in range(k):
                x = T(x)
                traj.append(x)
            # word constancy across the class
            assert tuple(traj[i] & 1 for i in range(k)) == tuple(v), (k, r, n)
            # exact affine formula 2^j * T^j(n) = 3^{a_j} n + rho_j
            for j in range(k + 1):
                assert traj[j] * 2 ** j == 3 ** a[j] * n + rho[j], (k, r, n, j)
            # theorem predictions
            if not fail_js:                     # survivor class: (a) uniformly
                for j in range(1, k + 1):
                    assert traj[j] > n, (k, r, n, j)
            else:                               # (b) above the class constant
                for j in fail_js:
                    if n > bounds[j]:
                        assert traj[j] < n, (k, r, n, j)
                    elif n == bounds[j]:
                        assert traj[j] == n, (k, r, n, j)   # boundary case
            if any(traj[j] < n for j in range(1, k + 1)):
                all_sigma_gt = False
            checked += 1
        if all_sigma_gt:
            sigma_gt_k_all.append(r)
    # brute-force survivor identification must reproduce the survivor list
    assert sigma_gt_k_all == survivors[k], (k, sigma_gt_k_all, survivors[k])
    print(f"k={k}: {checked} integers checked; class predictions exact; "
          f"brute-force survivor set matches: PASS")

print()
print("boundary example: n=1 lies in class 1 mod 4 (not a 2-survivor), "
      "bound rho_2/(2^2-3^1) = 1/1 = 1, and T^2(1) = 1 = n exactly (no descent).")
```

Output (verbatim):

```text
j -> ceil(j*gamma): {1: 1, 2: 2, 3: 2, 4: 3, 5: 4, 6: 4, 7: 5, 8: 6}

k=1: survivors=1/2  density=0.500000  B_1 = 0 = 0.000000  argmax (r, j, rho_j, 2^j-3^a_j) = None
   survivor classes mod 2: [1]
     r=  1: word=(1,)  (a_1..a_1)=(1)
k=2: survivors=1/4  density=0.250000  B_2 = 2 = 2.000000  argmax (r, j, rho_j, 2^j-3^a_j) = (2, 2, 2, 1)
   survivor classes mod 4: [3]
     r=  3: word=(1, 1)  (a_1..a_2)=(1,2)
k=3: survivors=2/8  density=0.250000  B_3 = 2 = 2.000000  argmax (r, j, rho_j, 2^j-3^a_j) = (2, 2, 2, 1)
   survivor classes mod 8: [3, 7]
     r=  3: word=(1, 1, 0)  (a_1..a_3)=(1,2,2)
     r=  7: word=(1, 1, 1)  (a_1..a_3)=(1,2,3)
k=4: survivors=3/16  density=0.187500  B_4 = 20/7 = 2.857143  argmax (r, j, rho_j, 2^j-3^a_j) = (12, 4, 20, 7)
   survivor classes mod 16: [7, 11, 15]
     r=  7: word=(1, 1, 1, 0)  (a_1..a_4)=(1,2,3,3)
     r= 11: word=(1, 1, 0, 1)  (a_1..a_4)=(1,2,2,3)
     r= 15: word=(1, 1, 1, 1)  (a_1..a_4)=(1,2,3,4)
k=5: survivors=4/32  density=0.125000  B_5 = 76/5 = 15.200000  argmax (r, j, rho_j, 2^j-3^a_j) = (28, 5, 76, 5)
   survivor classes mod 32: [7, 15, 27, 31]
     r=  7: word=(1, 1, 1, 0, 1)  (a_1..a_5)=(1,2,3,3,4)
     r= 15: word=(1, 1, 1, 1, 0)  (a_1..a_5)=(1,2,3,4,4)
     r= 27: word=(1, 1, 0, 1, 1)  (a_1..a_5)=(1,2,2,3,4)
     r= 31: word=(1, 1, 1, 1, 1)  (a_1..a_5)=(1,2,3,4,5)
k=6: survivors=8/64  density=0.125000  B_6 = 76/5 = 15.200000  argmax (r, j, rho_j, 2^j-3^a_j) = (28, 5, 76, 5)
   survivor classes mod 64: [7, 15, 27, 31, 39, 47, 59, 63]
     r=  7: word=(1, 1, 1, 0, 1, 0)  (a_1..a_6)=(1,2,3,3,4,4)
     r= 15: word=(1, 1, 1, 1, 0, 0)  (a_1..a_6)=(1,2,3,4,4,4)
     r= 27: word=(1, 1, 0, 1, 1, 1)  (a_1..a_6)=(1,2,2,3,4,5)
     r= 31: word=(1, 1, 1, 1, 1, 0)  (a_1..a_6)=(1,2,3,4,5,5)
     r= 39: word=(1, 1, 1, 0, 1, 1)  (a_1..a_6)=(1,2,3,3,4,5)
     r= 47: word=(1, 1, 1, 1, 0, 1)  (a_1..a_6)=(1,2,3,4,4,5)
     r= 59: word=(1, 1, 0, 1, 1, 0)  (a_1..a_6)=(1,2,2,3,4,4)
     r= 63: word=(1, 1, 1, 1, 1, 1)  (a_1..a_6)=(1,2,3,4,5,6)
k=7: survivors=13/128  density=0.101562  B_7 = 76/5 = 15.200000  argmax (r, j, rho_j, 2^j-3^a_j) = (28, 5, 76, 5)
   survivor classes mod 128: [27, 31, 39, 47, 63, 71, 79, 91, 95, 103, 111, 123, 127]
k=8: survivors=19/256  density=0.074219  B_8 = 1688/13 = 129.846154  argmax (r, j, rho_j, 2^j-3^a_j) = (248, 8, 1688, 13)
   survivor classes mod 256: [27, 31, 47, 63, 71, 91, 103, 111, 127, 155, 159, 167, 191, 207, 223, 231, 239, 251, 255]

reduction consistency: every (k+1)-survivor reduces to a k-survivor: PASS

== Adversarial test 1: class uniformity, k <= 6, n = r + 2^k*t, t = 0..199 ==
k=1: 399 integers checked; class predictions exact; brute-force survivor set matches: PASS
k=2: 799 integers checked; class predictions exact; brute-force survivor set matches: PASS
k=3: 1599 integers checked; class predictions exact; brute-force survivor set matches: PASS
k=4: 3199 integers checked; class predictions exact; brute-force survivor set matches: PASS
k=5: 6399 integers checked; class predictions exact; brute-force survivor set matches: PASS
k=6: 12799 integers checked; class predictions exact; brute-force survivor set matches: PASS

boundary example: n=1 lies in class 1 mod 4 (not a 2-survivor), bound rho_2/(2^2-3^1) = 1/1 = 1, and T^2(1) = 1 = n exactly (no descent).
```

Hand-checks against the output: class $3 \bmod 4$ has word $(1,1)$, $\rho_1 = 1$,
$\rho_2 = 3\cdot1 + 2 = 5$, so $T^2(n) = (9n+5)/4$: $n = 3 \Rightarrow 8$
($3 \to 5 \to 8$ ✓), $n = 7 \Rightarrow 17$ ($7 \to 11 \to 17$ ✓). The $B_8$ argmax
class $248 \bmod 256$ was hand-checked in the Proof of L-9909.4.

### Script 2: `l9909_preimages.py` — L-9909.1 and L-9909.2 identity checks

Checks performed: (1) **complete** cross-validation of the preimage parametrization: the
formula's predicted preimage set of every odd $n \le 199$ is compared against the set
obtained by exhaustively applying $S$ to **every** odd $x \le 10^6$ — including
integrality, oddness, exact valuation $\nu_2(3x_k+1) = k$, and $S(x_k) = n$ for each
generated preimage; (1b) leaves: odd multiples of 3 have no preimages in that range;
(2) the mod-3 start table and the $0\to1\to2$ cycle for odd $n \le 2000$, 12 admissible
exponents each; (3a) backward-edge identities $C(2n) = n$ and, for $n \equiv 2 \bmod 3$,
$x = (2n-1)/3$ odd positive with $C^2(x) = n$, for $n \le 10^5$; (3b) the descent step of
L-9909.2(M)(ii) for every $\mu' \equiv 1 \bmod 4$, $5 \le \mu' \le 10^5$; (3c) the
sub-lemma $T^j(n) \in O_C(n)$, sampled for $n \le 3000$, $j \le 200$.

```python
#!/usr/bin/env python3
# l9909_preimages.py -- adversarial checks for L-9909.1 (Syracuse preimages,
# mod-3 leaf distribution) and L-9909.2 (closure/descent identities).
# Agent: fable-02-p7. Python 3 stdlib only; exact integer arithmetic.

def nu2(m):
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k

def S(x):
    y = 3 * x + 1
    return y >> nu2(y)

def C(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

# -- Test 1: preimage characterization, complete cross-validation up to X ------
X = 10 ** 6
pre = {}
for x in range(1, X + 1, 2):
    pre.setdefault(S(x), []).append(x)

bad = 0
for n in range(1, 200, 2):
    formula = []
    if n % 3 != 0:
        k0, step = (2, 2) if n % 3 == 1 else (1, 2)   # admissible k: parity class
        k = k0
        while (2 ** k * n - 1) // 3 <= X:
            assert (2 ** k * n) % 3 == 1, (n, k)      # admissibility
            xx = (2 ** k * n - 1) // 3
            assert (2 ** k * n - 1) % 3 == 0, (n, k)  # integrality
            assert xx % 2 == 1, (n, k)                # automatic oddness
            assert nu2(3 * xx + 1) == k, (n, k)       # automatic exact valuation
            assert S(xx) == n, (n, k)                 # it is a preimage
            formula.append(xx)
            k += step
    brute = sorted(pre.get(n, []))
    if brute != sorted(formula):
        bad += 1
        print("MISMATCH n =", n, brute[:5], sorted(formula)[:5])
print(f"Test 1 (preimage formula == brute force, odd n in [1,199], all odd x <= {X}):",
      "PASS" if bad == 0 else "FAIL")

leaf_bad = [n for n in range(3, 200, 6) if pre.get(n)]
print("Test 1b (odd n with 3|n have NO preimages among odd x <= 1e6):",
      "PASS" if not leaf_bad else ("FAIL " + str(leaf_bad)))

# -- Test 2: mod-3 residue of preimages cycles 0 -> 1 -> 2 ---------------------
# start_table: n mod 9 -> x mod 3 at the smallest admissible k; then +1 per step.
start_table = {1: 1, 4: 2, 7: 0, 2: 1, 5: 0, 8: 2}
ok = True
for n in range(1, 2001, 2):
    if n % 3 == 0:
        continue
    k0, step = (2, 2) if n % 3 == 1 else (1, 2)
    e0 = start_table[n % 9]
    for idx in range(12):
        k = k0 + step * idx
        xx = (2 ** k * n - 1) // 3
        if xx % 3 != (e0 + idx) % 3:
            ok = False
            print("mod-3 cycle FAIL", n, k, xx % 3, (e0 + idx) % 3)
print("Test 2 (preimage mod-3 start table + cycle 0->1->2, odd n<=2000, 12 k's):",
      "PASS" if ok else "FAIL")

# -- Test 3: closure/descent identities of L-9909.2 ----------------------------
ok = True
for n in range(1, 100001):
    if C(2 * n) != n:
        ok = False
    if n % 3 == 2:
        xx = (2 * n - 1) // 3
        if not ((2 * n - 1) % 3 == 0 and xx >= 1 and xx % 2 == 1 and C(C(xx)) == n):
            ok = False
            print("backward-edge FAIL", n)
print("Test 3a (C(2n)=n; and for n=2 mod 3: x=(2n-1)/3 odd positive, C(C(x))=n; n<=1e5):",
      "PASS" if ok else "FAIL")

ok = True
for mu in range(5, 100001, 4):        # mu = 1 (mod 4), mu > 1
    a = 3 * mu + 1
    if not (a % 4 == 0 and C(mu) == a and C(a) == a // 2 and (a // 2) % 2 == 0
            and C(a // 2) == a // 4 and 1 <= a // 4 < mu):
        ok = False
        print("descent FAIL", mu)
print("Test 3b (mu=1 mod 4, mu>1: C^3(mu) = (3mu+1)/4 integer, positive, < mu; mu<=1e5):",
      "PASS" if ok else "FAIL")

ok = True
for n in range(1, 3001):
    cset = set()
    x = n
    for _ in range(500):
        cset.add(x)
        x = C(x)
    cset.add(x)
    y = n
    for j in range(200):
        y = T(y)
        if y not in cset:
            ok = False
            print("T-orbit-in-C-orbit FAIL", n, j)
            break
print("Test 3c (T^j(n) lies in the C-orbit of n; n<=3000, 200 T-steps vs 500 C-steps):",
      "PASS" if ok else "FAIL")
```

Output (verbatim):

```text
Test 1 (preimage formula == brute force, odd n in [1,199], all odd x <= 1000000): PASS
Test 1b (odd n with 3|n have NO preimages among odd x <= 1e6): PASS
Test 2 (preimage mod-3 start table + cycle 0->1->2, odd n<=2000, 12 k's): PASS
Test 3a (C(2n)=n; and for n=2 mod 3: x=(2n-1)/3 odd positive, C(C(x))=n; n<=1e5): PASS
Test 3b (mu=1 mod 4, mu>1: C^3(mu) = (3mu+1)/4 integer, positive, < mu; mu<=1e5): PASS
Test 3c (T^j(n) lies in the C-orbit of n; n<=3000, 200 T-steps vs 500 C-steps): PASS
```

Small worked example for Test 1 (visible in the data): $n = 5 \equiv 2 \bmod 3$,
admissible $k$ odd: $k=1: x = 3$ ($S(3) = \mathrm{odd}(10) = 5$ ✓, and $3$ is a leaf,
$e_0(5 \bmod 9 = 5) = 0$ ✓); $k=3: x = 13$ ($S(13)=\mathrm{odd}(40)=5$ ✓, $13 \equiv 1$);
$k=5: x = 53 \equiv 2$; residues cycle $0,1,2$ ✓.

### Script 3: `l9909_x9901.py` — X-9901

```python
#!/usr/bin/env python3
# l9909_x9901.py -- X-9901: finite verification that every n <= 10^6 reaches 1
# under C, with max total C-stopping time. Agent: fable-02-p7. Python 3 stdlib.
#
# Method: for each n from 2 to N, iterate C until the orbit first drops below n
# (this DESCENT is what is verified directly, with a hard iteration cap);
# "reaches 1" then follows for all n <= N by strong induction on n
# (base n = 1: C^0(1) = 1). Total stopping time is accumulated via memoization.
N = 10 ** 6
CAP = 10 ** 5
steps = [0] * (N + 1)      # steps[n] = least k >= 0 with C^k(n) = 1
maxs, argmax = 0, 1
for n in range(2, N + 1):
    x, c = n, 0
    while x >= n:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        c += 1
        assert c < CAP, f"no descent below n within {CAP} C-steps at n = {n}"
    steps[n] = c + steps[x]
    if steps[n] > maxs:
        maxs, argmax = steps[n], n
print(f"X-9901: every n <= {N} was verified to descend strictly below itself under C;")
print(f"by strong induction, every n <= {N} reaches 1 under C.")
print(f"max total C-stopping time for n <= {N}: {maxs}, attained at n = {argmax}")
```

Output (verbatim; runtime about 1.3 s):

```text
X-9901: every n <= 1000000 was verified to descend strictly below itself under C;
by strong induction, every n <= 1000000 reaches 1 under C.
max total C-stopping time for n <= 1000000: 524, attained at n = 837799
```

Interpretation and limitations: X-9901 is **finite verification** of the finite statement
"every $n \le 10^6$ reaches 1 under $C$" (bound used: $\max(B_8, 10^6) = 10^6$). It is
used *only* to discharge that finite hypothesis in L-9909.4(c). It says nothing about
$n > 10^6$ and is not evidence about the truth of the conjecture in either direction.
(The literature reports verification to beyond $2^{68}$; this file relies only on its own
reproducible in-repo computation.)

## Remaining uncertainty

* The proofs of L-9909.1–L-9909.3 and L-9909.5 are elementary and, to the author's best
  adversarial reading, complete; the most error-prone spots (index bookkeeping in
  Lemma B; the $i < j$ case of backward closure; strict-vs-weak inequalities at the
  threshold $\rho_j/d_j$; the $k = 0$ orbit-index convention) were each given explicit
  treatment and matching computational probes. Residual risk is low but a reviewer
  should re-derive Lemma B's exponent $3^{a_l}2^{k-l}$ independently.
* L-9909.4's unconditional conclusion inherits the trustworthiness of two exact
  computations (Scripts 1 and 3). Both are short, deterministic, exact-arithmetic, and
  rerunnable; a reviewer should rerun them (and ideally reimplement Script 1
  independently, e.g. over words instead of residues, using L-9902's bijection as a
  cross-check).
* The survivor sequence $1, 1, 2, 3, 4, 8, 13, 19$ and the extremal datum
  $B_8 = 1688/13$ agree with the author's independent hand analysis (word
  $(0,0,0,1,1,1,1,1)$ maximizing $\rho_8$ among $a_8 = 5$ words), but no external
  literature value was consulted in-session for these exact constants; treat the table
  as in-repo computed truth pending independent recomputation.
* $B_k$ here is the coarse max-over-failing-$j$ constant; nothing downstream is
  sensitive to this choice, but a reviewer comparing against other files' "$B_k$" should
  check which convention those use.

## Suggested next attack

1. **L-9908 (survivor density decay).** Prove $\#\mathrm{Surv}(k) / 2^k \le c\,\theta^k$
   for explicit $c, \theta < 1$: survivor words satisfy $a_j \ge \lceil j\gamma\rceil$
   for all $j \le k$, a ballot-type constraint with drift $\gamma > 1/2$; a
   Chernoff/reflection count of $\{0,1\}$-words should give
   $\theta = 2 H^{-1}$-type constants. Use the $k \le 8$ lists here as test vectors.
   (The equalities at $k \in \{3, 6\}$ show any proof must handle the staircase of
   $\lceil j\gamma \rceil$, not per-step decay.)
2. **Extend the computation** to $k = 20$–$30$ (the class count $2^k$ is the only cost;
   enumerate survivor words instead, extending only surviving prefixes — the reduction
   consistency proved in L-9909.5 justifies the pruned tree search). Record $B_k$ growth;
   combined with a verification bound $N$, each $k$ with $B_k < N$ yields unconditional
   congruences for $\mu$.
3. **Feed L-9909.2(E) into issue #25**: the backward-tree density machinery applies to
   $K$ verbatim; combining its density-zero conclusions (if/when proved) with the
   survivor sieve's mod-$2^k$ restrictions is the natural pincer.
4. **Refutation surface**: the sharpest falsifiable claims are the exact identity
   ($\ast$), the survivor lists, and the boundary trichotomy in (b). A verifier should
   attack Lemma B with adversarial residues (e.g. $r$ near $2^k$), attempt a class whose
   sampled words disagree, and try to construct $n > B_k$ in a non-survivor class with
   $\sigma(n) > k$ — by Corollary item 2 any success refutes this file.

---

*Signed: fable-02-p7, 2026-07-21.*
