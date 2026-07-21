# L-9906 — Finite-window elimination template; no nontrivial $S$-cycle has at most six odd elements

```text
Claim ID:      L-9906
Title:         Finite-window cycle-elimination template and the absence of
               nontrivial Syracuse cycles with m <= 6 odd elements
Status:        PROVED
Authoring agent:   fable-02-p5
Reviewing agents:  fable-02-v5 (adversarial review 2026-07-21: PASS)
Created:       2026-07-21
Last updated:  2026-07-21 (fable-02-v5 review: PASS; status upgraded to PROVED)
Dependencies:  NOTATION.md (D-9904 Syracuse map and step exponent, D-9905 trivial
               cycles, D-9908 S-cycle notation: a_i, A_i, K, least period m).
               L-9905 (cycle equation) is listed as a logical dependency but the
               needed statement is RE-DERIVED INLINE in Step 1 below, so nothing
               in this file relies on L-9905 having landed; see Dependency audit.
Scope:         S-cycles only (positive odd integers under the Syracuse map S).
               The template L-9906.1 holds for every m >= 2 and every real
               X > (3/2)^(m-1) - 1. The elimination results cover every S-cycle
               of least period m <= 6. Translation of C- and T-cycles to
               S-cycles is L-9905's business and is NOT used or claimed here.
Related counterexample candidates: none
```

---

## Statement

Throughout, $S$ is the Syracuse map (D-9904) on positive odd integers,
$S(x) = (3x+1)/2^{\nu_2(3x+1)}$, with step exponent $a(x) := \nu_2(3x+1) \ge 1$.
An $S$-cycle of least period $m \ge 1$ is written as in D-9908:
$x_1 \to x_2 \to \dots \to x_m \to x_1$ (all $x_i$ positive odd, $x_{m+1} := x_1$,
$S(x_i) = x_{i+1}$), exponents $a_i := \nu_2(3x_i+1) \ge 1$, partial sums $A_0 := 0$,
$A_i := a_1 + \dots + a_i$, and $K := A_m = \sum_{i=1}^m a_i$. The trivial cycle is the
fixed point $(1)$ (D-9905). For a given cycle and a given anchoring (choice of which
element is called $x_1$), define
$$D := 2^K - 3^m, \qquad c := \sum_{i=1}^{m} 3^{\,m-i}\, 2^{A_{i-1}} .$$

**Main Theorem (L-9906).** No nontrivial $S$-cycle has least period $m \le 6$.
Equivalently: if $x$ is a positive odd integer with $S^m(x) = x$ for some
$1 \le m \le 6$, then $x = 1$.

The proof is organized around a reusable template plus applications:

**L-9906.1 (finite-window elimination template).** Let
$x_1 \to \dots \to x_m \to x_1$ be an $S$-cycle of least period $m \ge 1$, in the
notation above. Then:

1. **(Cycle equation; holds for every anchoring.)**
   $x_1 \cdot D = c$, and $c \ge 1$; hence $D \ge 1$, i.e. $2^K > 3^m$
   (so $K > m \log_2 3$).
2. **(Anchored upper bound.)** If $m \ge 2$ then
   $$c \;\le\; 3^{m-1} \;+\; 2^{K-m}\left(2 \cdot 3^{m-1} - 2^{m}\right)
     \;=\; 3^{m-1} \;+\; 2^{K}\left(\left(\tfrac{3}{2}\right)^{m-1} - 1\right),$$
   with equality if and only if $(a_1, \dots, a_m) = (K-m+1, 1, 1, \dots, 1)$.
3. **(Finite window.)** Let $m \ge 2$ and let $X$ be a real number with
   $X > \left(\tfrac{3}{2}\right)^{m-1} - 1$, equivalently
   $2^{m-1}(X+1) > 3^{m-1}$. If $\min_i x_i \ge X$, then
   $$2^K \;\le\; \frac{3^{m-1} + X \cdot 3^m}{\,X + 1 - \left(\tfrac{3}{2}\right)^{m-1}}
     \;=\; \frac{6^{m-1} + 3^m\, 2^{m-1} X}{\,2^{m-1}(X+1) - 3^{m-1}} .$$
   Hence $K$ lies in the finite (possibly empty) **window**
   $$W(m, X) := \left\{ K \in \mathbb{Z} \;:\; 3^m < 2^K
     \;\text{ and }\; 2^K \left(2^{m-1}(X+1) - 3^{m-1}\right)
     \le 6^{m-1} + 3^m\, 2^{m-1} X \right\}.$$
4. **(Reduction to a finite enumeration.)** Fix $m \ge 2$ and $X$ as in item 3.
   If some $S$-cycle of least period $m$ with all elements $\ge X$ exists, then
   there exist $K \in W(m, X)$ and a composition $(a_1, \dots, a_m)$ of $K$ into
   $m$ parts $a_i \ge 1$ such that, with $D = 2^K - 3^m$ and
   $c = \sum_{i=1}^m 3^{m-i} 2^{A_{i-1}}$: $D \mid c$; the quotient $x := c/D$ is an
   odd integer $\ge X$; and iterating $S$ from $x$ for $m$ steps produces step
   exponents exactly $(a_1, \dots, a_m)$ and returns to $x$. Consequently, if for
   **every** $K \in W(m,X)$ and **every** such composition at least one of these
   conditions fails, then no $S$-cycle of least period $m$ has all elements $\ge X$.

**L-9906.2 (floor on the minimal element).** Every nontrivial $S$-cycle has
$x_{\min} := \min_i x_i \notin \{1, 3, 5\}$; since all elements are positive odd,
$x_{\min} \ge 7$ (hence **all** elements are $\ge 7$).

**L-9906.3 ($m = 1$).** The only $S$-cycle of least period $1$ is the trivial
cycle $(1)$ (with $a_1 = K = 2$).

**L-9906.4 ($m = 2$).** There is no $S$-cycle of least period $2$.

**L-9906.5 ($m = 3, 4, 5, 6$).** There is no $S$-cycle of least period
$m \in \{3, 4, 5, 6\}$. For $m = 3$ and $m = 4$ the complete case analysis is
written out by hand in this file ($6$ and $20$ cases); for $m = 5, 6$ it is an
exact finite verification of $105 + 1632$ cases, script and full output included.

*Guide-statement audit note.* The template inequality and the anchored bound were
independently re-derived here and agree exactly with the forms proposed in the
task brief; no correction was needed. The equality characterization in item 2 and
the fully integer form of the window in item 3 are additions.

---

## Definitions

- $S$, $a(x) = \nu_2(3x+1)$ — D-9904. $S$-cycle notation $x_i, a_i, A_i, K$, least
  period $m$ — D-9908. Trivial cycle $(1)$ — D-9905.
- **Anchoring / rotation.** A cycle of least period $m$ has $m$ rotations
  (relabelings $x_1 \mapsto x_{j}, x_{j+1}, \dots$); $K$, $m$, $D$ are
  rotation-invariant, while $(a_1, \dots, a_m)$, the $A_i$, and $c$ depend on the
  anchoring. "Anchored at $x_{\min}$" means the rotation with $x_1 = x_{\min}$.
- **Composition.** A composition of $K$ into $m$ parts is a tuple
  $(a_1, \dots, a_m) \in (\mathbb{Z}^+)^m$ with $\sum a_i = K$. Compositions of $K$
  into $m$ parts are in bijection with $(m-1)$-element subsets
  $\{A_1 < A_2 < \dots < A_{m-1}\} \subseteq \{1, \dots, K-1\}$ via partial sums
  ($a_i = A_i - A_{i-1}$, $A_0 = 0$, $a_m = K - A_{m-1}$); there are
  $\binom{K-1}{m-1}$ of them. (Both directions are immediate: strict increase of
  the $A_i$ is equivalent to $a_i \ge 1$ for $i \le m-1$, and $A_{m-1} \le K-1$ is
  equivalent to $a_m \ge 1$.)
- Empty sums are $0$ (NOTATION.md conventions); for $m = 1$, $c = 3^0 2^{A_0} = 1$.
- $x_{\min} := \min_i x_i$; note $x_{\min} \ge X$ iff all elements are $\ge X$.

---

## Motivation

This file gives the cycle-synthesis program (issue #9) a proved, self-contained
floor: any nontrivial $S$-cycle — the second listed counterexample mode in
D-9909/README — must have at least $7$ odd elements. More importantly for the
program, L-9906.1 is a **reusable elimination template** exhibiting exactly how
verified small-orbit computations feed cycle elimination: a lower bound $X$ on
$x_{\min}$ (from any verified-convergence sweep) confines $K$ to an explicit
finite window above $m \log_2 3$, and the window reduces "no cycle with $m$ odd
elements" to a finite, exact, auditable enumeration of exponent compositions.
Conversely, for the constructive direction, the template says precisely where a
genuine cycle must hide: $K/m \to \log_2 3$ forcibly as $x_{\min}$ grows, and any
synthesis attempt must fight the window inequality of item 3.

*Context note (not a dependency).* The literature reports far stronger floors on
$m$ via Baker-type transcendence bounds combined with very large verified
computations. None of that is used, cited as evidence, or needed here; the value
of this file is complete in-repo rigor by elementary means.

---

## Proof

### Step 0 — Preliminaries on periodic orbits

**P0 (least period divides every period; distinctness).** Let $x$ be a positive
odd integer, let $y_k := S^k(x)$ ($k \ge 0$), and suppose the sequence
$(y_k)_{k \ge 0}$ is purely periodic with least period $m \ge 1$ (i.e.
$y_{k+m} = y_k$ for all $k \ge 0$, and $m$ is minimal with this property). Then:

(a) If $q \ge 1$ satisfies $y_{k+q} = y_k$ for all $k \ge 0$, then $m \mid q$.

(b) The elements $y_0, y_1, \dots, y_{m-1}$ (equivalently $x_1, \dots, x_m$ in the
D-9908 labeling) are pairwise distinct.

(c) If some single index $i \ge 0$ and some $d \ge 1$ satisfy $y_{i+d} = y_i$,
then $d$ is a period of the whole sequence, hence $m \mid d$.

*Proof.* (c) first: from $y_{i+d} = y_i$ and $y_{k+1} = S(y_k)$, induction on
$k \ge i$ gives $y_{k+d} = y_k$ for all $k \ge i$ (base $k = i$; step: apply $S$
to both sides). For arbitrary $k \ge 0$ choose an integer $t \ge 0$ with
$k + tm \ge i$; then using $m$-periodicity twice and the $k \ge i$ case once,
$y_{k+d} = y_{k + d + tm} = y_{k+tm} = y_k$. So $d$ is a period of the full
sequence. (a): let $q$ be any period and write $q = sm + r$ with $0 \le r < m$,
$s \ge 0$. For every $k \ge 0$: $y_{k+r} = y_{k+r+sm} = y_{k+q} = y_k$ (first
equality is $m$-periodicity applied $s$ times, second is $q$-periodicity). If
$r \ge 1$ this makes $r < m$ a period, contradicting minimality; so $r = 0$ and
$m \mid q$. This also finishes (c). (b): if $y_{i} = y_{j}$ with
$0 \le i < j \le m-1$, then $d := j - i$ satisfies $1 \le d \le m-1$ and
$y_{i+d} = y_i$, so by (c) $m \mid d$ — impossible for $1 \le d \le m-1$. $\square$

**P1 (orbits of cycle elements stay in the cycle).** If $x_j$ is an element of an
$S$-cycle $\{x_1, \dots, x_m\}$, then $S^k(x_j) \in \{x_1, \dots, x_m\}$ for every
$k \ge 0$, and $S^m(x_j) = x_j$.

*Proof.* Induction on $k$: $S^0(x_j) = x_j$; and $S(x_i) = x_{i+1}$ (indices mod
$m$, per D-9908), so $S$ maps the cycle set to itself. $S^m(x_j) = x_j$ is P0
applied to the rotation starting at $x_j$ (or directly: following the cycle $m$
steps returns to the start). $\square$

**Equivalence of the two forms of the Main Theorem.** If $S^m(x) = x$ with
$1 \le m \le 6$, then the orbit of $x$ is purely periodic and its least period
$m'$ divides $m$ (P0(a)), so $m' \le 6$; if no nontrivial cycle has least period
$\le 6$, the cycle through $x$ is trivial, i.e. $x = 1$. Conversely, a nontrivial
cycle of least period $m \le 6$ contains an $x \ne 1$ with $S^m(x) = x$. $\square$

### Step 1 — Proof of L-9906.1

**(i) Cycle equation.** We prove by induction on $i$, $0 \le i \le m$, the identity
$$2^{A_i}\, x_{i+1} \;=\; 3^{i}\, x_1 \;+\; \sum_{j=1}^{i} 3^{\,i-j}\, 2^{A_{j-1}}
\tag{1.1}$$
(with $x_{m+1} := x_1$ and the empty sum $= 0$).

*Base $i = 0$:* $2^{A_0} x_1 = x_1$, and the right side is $3^0 x_1 + 0 = x_1$. ✓

*Step.* By D-9904, $S(x_{i+1}) = (3x_{i+1}+1)/2^{\nu_2(3x_{i+1}+1)}$; since the
cycle has $S(x_{i+1}) = x_{i+2}$ and $a_{i+1} = \nu_2(3x_{i+1}+1)$, this is exactly
$$2^{a_{i+1}}\, x_{i+2} \;=\; 3 x_{i+1} + 1. \tag{1.2}$$
Multiply (1.2) by $2^{A_i}$ and use $A_{i+1} = A_i + a_{i+1}$ and the induction
hypothesis (1.1):
$$2^{A_{i+1}} x_{i+2}
= 3 \cdot 2^{A_i} x_{i+1} + 2^{A_i}
= 3^{i+1} x_1 + \sum_{j=1}^{i} 3^{\,i+1-j} 2^{A_{j-1}} + 3^0\, 2^{A_i}
= 3^{i+1} x_1 + \sum_{j=1}^{i+1} 3^{\,i+1-j} 2^{A_{j-1}},$$
which is (1.1) at $i+1$. ✓

Setting $i = m$ in (1.1) and using $x_{m+1} = x_1$, $A_m = K$:
$2^K x_1 = 3^m x_1 + c$, i.e.
$$x_1 \left(2^K - 3^m\right) = x_1 D = c. \tag{1.3}$$
Every summand of $c$ is a positive integer, and the $i = 1$ summand is
$3^{m-1} 2^{A_0} = 3^{m-1} \ge 1$, so $c \ge 1$. Since $x_1 \ge 1$ and
$x_1 D = c \ge 1$ with $x_1, D$ integers, $D \ge 1$, i.e. $2^K > 3^m$ and
$K > m\log_2 3$. This proves (i). (Nothing here used which rotation was chosen,
so (i) holds for **every** anchoring, each with its own $c$.)

**(ii) Anchored upper bound.** Let $m \ge 2$. For $2 \le i \le m$,
$$K - A_{i-1} \;=\; a_i + a_{i+1} + \dots + a_m \;\ge\; m - i + 1
\tag{1.4}$$
since the sum has $m - i + 1$ terms, each $\ge 1$ (D-9904). Hence
$A_{i-1} \le K - (m - i + 1) = K - m + i - 1$ and (monotonicity of $2^t$, and
$3^{m-i} > 0$)
$$c \;=\; 3^{m-1}\, 2^{A_0} + \sum_{i=2}^{m} 3^{\,m-i}\, 2^{A_{i-1}}
\;\le\; 3^{m-1} + \sum_{i=2}^{m} 3^{\,m-i}\, 2^{\,K-m+i-1},
\tag{1.5}$$
using $A_0 = 0$ **exactly** in the first term (this is the point of anchoring: the
first term contributes $3^{m-1}$, not $3^{m-1}2^{K-m}$). The geometric sum
evaluates exactly: substituting $j = i - 1$ ($1 \le j \le m-1$),
$$\sum_{i=2}^{m} 3^{\,m-i}\, 2^{\,K-m+i-1}
= 2^{K-m}\, 3^{m-1} \sum_{j=1}^{m-1} \left(\tfrac{2}{3}\right)^{j}
= 2^{K-m}\, 3^{m-1} \cdot \frac{\tfrac{2}{3}\left(1 - (\tfrac{2}{3})^{m-1}\right)}{1 - \tfrac{2}{3}}
= 2^{K-m} \left(2 \cdot 3^{m-1} - 2^{m}\right).$$
(The last step: $3^{m-1} \cdot 2 \left(1 - (2/3)^{m-1}\right)
= 2 \cdot 3^{m-1} - 2 \cdot 2^{m-1} = 2\cdot 3^{m-1} - 2^m$.) Also
$2^{K-m}(2 \cdot 3^{m-1} - 2^m) = 2^K \cdot \frac{2 \cdot 3^{m-1} - 2^m}{2^m}
= 2^K \left((3/2)^{m-1} - 1\right)$, giving both displayed forms. Note
$2 \cdot 3^{m-1} > 2^m$ for $m \ge 2$ (equivalent to $(3/2)^{m-1} > 1$), so the
bound exceeds $3^{m-1}$, as it must.

*Equality characterization.* Equality in (1.5) holds iff every term with
$i \ge 2$ is tight, i.e. $A_{i-1} = K - m + i - 1$ for all $2 \le i \le m$. By
(1.4), tightness at index $i$ means $a_j = 1$ for all $j \ge i$; tightness at
$i = 2$ (i.e. $a_2 = \dots = a_m = 1$, forcing $a_1 = K - m + 1$) already implies
tightness at every $i \ge 2$. So equality holds iff
$(a_1, \dots, a_m) = (K-m+1, 1, \dots, 1)$. This proves (ii).

**(iii) Finite window.** Assume $m \ge 2$, $x_{\min} \ge X$, and
$X > (3/2)^{m-1} - 1 > 0$. Anchor the cycle at $x_{\min}$ (i.e. relabel so
$x_1 = x_{\min}$; $K, m, D$ are unchanged, and (i), (ii) hold for this
anchoring). Since $D \ge 1 > 0$ (by (i)) and $x_1 = x_{\min} \ge X$:
$$X\left(2^K - 3^m\right) \;\le\; x_{\min} D \;=\; c
\;\underset{\text{(ii)}}{\le}\; 3^{m-1} + 2^{K}\left(\left(\tfrac{3}{2}\right)^{m-1} - 1\right).$$
Collect the $2^K$ terms on the left and the constants on the right — all
rearrangements are additions of equals to both sides, so the direction $\le$ is
preserved:
$$2^K \left(X - \left(\tfrac{3}{2}\right)^{m-1} + 1\right) \;\le\; 3^{m-1} + X \cdot 3^m.
\tag{1.6}$$
By hypothesis the coefficient $X + 1 - (3/2)^{m-1}$ is **strictly positive**, so
dividing (1.6) by it preserves $\le$:
$$2^K \;\le\; \frac{3^{m-1} + X \cdot 3^m}{X + 1 - \left(\tfrac{3}{2}\right)^{m-1}} .$$
Multiplying numerator and denominator by $2^{m-1} > 0$ gives the second
(denominator-cleared) form
$\;2^K \le \left(6^{m-1} + 3^m 2^{m-1} X\right) / \left(2^{m-1}(X+1) - 3^{m-1}\right)$;
cross-multiplying by the positive quantity $2^{m-1}(X+1) - 3^{m-1}$ gives exactly
the second defining inequality of $W(m, X)$. Together with $2^K > 3^m$ from (i), $K$
lies in $W(m, X)$. Finiteness of $W(m,X)$: $2^K \le B$ bounds $K \le \log_2 B$
above, and $2^K > 3^m$ bounds $K$ below; an integer interval is finite. This
proves (iii). (For rational $X$ — e.g. $X = 7$ below — membership in $W(m,X)$ is
decidable by exact integer arithmetic.)

**(iv) Reduction to a finite enumeration.** Suppose an $S$-cycle of least period
$m \ge 2$ with all elements $\ge X$ exists; anchor it at $x_{\min}$. Then:
its exponent tuple $(a_1, \dots, a_m)$ is a composition of $K$ into $m$ parts
$\ge 1$ (D-9904 gives $a_i \ge 1$; $K = \sum a_i$ by D-9908); $K \in W(m,X)$ by
(iii); $x_{\min} D = c$ by (i), so $D \mid c$ and $x := c/D = x_{\min}$, which is
an odd integer (a cycle element) with $x \ge X$; and by the cycle relations
(1.2), iterating $S$ from $x = x_1$ produces exponents exactly
$a_1, a_2, \dots, a_m$ and $S^m(x) = x_{m+1} = x$. Thus the anchored cycle
appears in the finite list of pairs $(K, \text{composition})$,
$K \in W(m, X)$, and passes all the stated tests. The contrapositive is the
elimination statement. $\blacksquare$ *(L-9906.1)*

**Remark 1 (degenerate "retracing" solutions).** For the composition
$(2, 2, \dots, 2)$ of $K = 2m$, the geometric identity
$(4-3)\sum_{i=1}^{m} 3^{m-i} 4^{\,i-1} = 4^m - 3^m$ gives $c = 4^m - 3^m = 2^{2m} - 3^m = D$,
so $x = c/D = 1$ always solves the divisibility test — it is the trivial fixed
point $S(1) = 1$ (exponent $2$) retraced $m$ times, with least period $1$, not
$m$. This is why (iv) demands $x \ge X$ **and** the orbit test, and why the
least-period bookkeeping of P0 matters. In the windowed enumeration of L-9906.5
these retracing solutions arise exactly when $2m \in W(m, 7)$ — for $m \le 6$
only at $m = 6$, $K = 12$ — and in the hand analysis of L-9906.4 at
$K = 4 = 2 \cdot 2$ (which lies in the hand-derived range $\{4\}$ but outside
$W(2,7) = \varnothing$; no inconsistency, since the window hypothesis assumes all
elements $\ge 7$ while the retracing solution has $x = 1$). That the enumeration
output reproduces exactly this predicted pattern is an internal consistency check.

### Step 2 — Proof of L-9906.2 ($x_{\min} \ge 7$)

The three explicit Syracuse values used here (each a one-line computation from
D-9904):
$$S(1) = \tfrac{3\cdot 1 + 1}{2^{\nu_2(4)}} = \tfrac{4}{4} = 1 \;(a = 2), \qquad
S(3) = \tfrac{10}{2} = 5 \;(a = 1), \qquad
S(5) = \tfrac{16}{16} = 1 \;(a = 4).$$
So the $S$-orbits are $3 \to 5 \to 1 \to 1 \to \cdots$ and $5 \to 1 \to 1 \to \cdots$.

**(a) A cycle containing $1$ is the trivial cycle $(1)$.** If $x_i = 1$ for some
element of a cycle of least period $m$, then $x_{i+1} = S(1) = 1 = x_i$; by
P0(b) (distinctness), $m = 1$, and the cycle is the fixed point $(1)$, which is
the trivial cycle (D-9905). Hence **a nontrivial cycle does not contain $1$.**

**(b) $3$ lies on no cycle.** $S^2(3) = 1$ and $S(1) = 1$, so $S^k(3) = 1$ for all
$k \ge 2$. If $3$ were an element of a cycle of least period $m$, then
$S^m(3) = 3$ (P1). For $m = 1$: $S(3) = 5 \ne 3$. For $m \ge 2$:
$S^m(3) = 1 \ne 3$. Contradiction either way.

**(c) $5$ lies on no cycle.** $S^k(5) = 1$ for all $k \ge 1$. If $5$ were in a
cycle of least period $m$: $m = 1$ gives $S(5) = 1 \ne 5$; $m \ge 2$ gives
$S^m(5) = 1 \ne 5$. Contradiction.

Now let a nontrivial $S$-cycle be given. Its elements are positive odd integers
(D-9908); none equals $1$ (a), $3$ (b), or $5$ (c). The positive odd integers
outside $\{1,3,5\}$ are exactly those $\ge 7$. Hence every element, in particular
$x_{\min}$, is $\ge 7$. $\blacksquare$ *(L-9906.2)*

### Step 3 — Proof of L-9906.3 ($m = 1$)

Let $x_1$ be a cycle of least period $1$: $S(x_1) = x_1$, $K = a_1 \ge 1$. The
cycle equation (i) with $m = 1$ reads $x_1 (2^K - 3) = c = 3^0 2^{A_0} = 1$. Both
factors on the left are integers, $x_1 \ge 1$, and the product is $1 > 0$, so
both factors are positive and each equals $1$: $x_1 = 1$ and $2^K = 4$, $K = 2$.
This is consistent ($S(1) = 1$ with $a = 2$), so the unique period-$1$ cycle is
the trivial cycle $(1)$. In particular there is **no nontrivial** cycle with
$m = 1$. $\blacksquare$ *(L-9906.3)*

### Step 4 — Proof of L-9906.4 ($m = 2$)

Suppose an $S$-cycle $x_1 \to x_2 \to x_1$ of least period $2$ exists (it is
automatically nontrivial: the trivial cycle has least period $1$). Anchor it
anywhere; the cycle equation (i) with $m = 2$ reads
$$x_1 \left(2^K - 9\right) \;=\; c \;=\; 3 \cdot 2^{A_0} + 2^{A_1} \;=\; 3 + 2^{a_1},
\qquad K = a_1 + a_2, \quad a_1, a_2 \ge 1,$$
so $1 \le a_1 \le K - 1$.

*Lower bound on $K$.* By (i), $2^K > 9$; since $2^3 = 8 < 9 < 16 = 2^4$, this
forces $K \ge 4$.

*Upper bound on $K$.* Since $x_1 \ge 1$ and $2^K - 9 \ge 1 > 0$:
$$2^K - 9 \;\le\; x_1\left(2^K - 9\right) \;=\; 3 + 2^{a_1} \;\le\; 3 + 2^{K-1}$$
(using $a_1 \le K-1$ and monotonicity of $2^t$). Hence
$2^{K-1} = 2^K - 2^{K-1} \le 12$, and since $2^4 = 16 > 12$ we get $K - 1 \le 3$,
i.e. $K \le 4$.

*Exact enumeration at $K = 4$.* Then $D = 2^4 - 9 = 7$ and
$(a_1, a_2) \in \{(1,3), (2,2), (3,1)\}$, giving $c = 3 + 2^{a_1} \in \{5, 7, 11\}$
respectively. Divisibility $7 \mid c$:

| $(a_1, a_2)$ | $c = 3 + 2^{a_1}$ | $c \bmod 7$ | $x_1 = c/7$ |
|---|---|---|---|
| $(1,3)$ | $5$  | $5$ | not an integer |
| $(2,2)$ | $7$  | $0$ | $1$ |
| $(3,1)$ | $11$ | $4$ | not an integer |

The only integer solution is $(a_1, a_2) = (2,2)$, $x_1 = 1$. But then
$x_2 = S(x_1) = S(1) = 1 = x_1$, contradicting P0(b) for least period $2$. (This
is exactly the retracing solution of Remark 1 with $m = 2$, $K = 4$; it is also
excluded by L-9906.2, since $x_1 = 1 < 7$.) The other two cases give no integer
$x_1$ at all. Hence no $S$-cycle of least period $2$ exists.
$\blacksquare$ *(L-9906.4)*

**Remark 2 (template cross-check for $m=2$).** L-9906.1(iii)–(iv) with $X = 7$
(legitimate by L-9906.2) gives an **empty** window: $\mathrm{den} =
2^1 \cdot 8 - 3 = 13$, $\mathrm{num} = 6 + 3^2 \cdot 2 \cdot 7 = 132$;
$2^3 \cdot 13 = 104 \le 132 < 208 = 2^4 \cdot 13$ forces $K \le 3$, while (i)
forces $K \ge 4$. So $W(2,7) = \varnothing$ and the template alone re-proves
L-9906.4. The hand proof above is retained because it does not need L-9906.2.

### Step 5 — Proof of L-9906.5 ($m = 3, 4, 5, 6$)

Fix $m \in \{3,4,5,6\}$ and suppose an $S$-cycle of least period $m$ exists. It
is nontrivial (trivial has least period $1$), so by L-9906.2 all its elements are
$\ge 7$. We apply the template L-9906.1 with $X = 7$. The template's hypothesis
$2^{m-1}(X+1) > 3^{m-1}$, i.e. $2^{m-1} \cdot 8 > 3^{m-1}$, holds for each $m$:
$$m=3:\; 32 > 9; \quad m=4:\; 64 > 27; \quad m=5:\; 128 > 81; \quad m=6:\; 256 > 243.$$
(It **fails** for $m = 7$: $2^6 \cdot 8 = 512 < 729 = 3^6$; this is the exact
reason the method with $X = 7$ stops at $m = 6$.)

**5.1 Window computation (exact integer arithmetic).** With
$\mathrm{den}_m := 2^{m-1}\cdot 8 - 3^{m-1}$ and
$\mathrm{num}_m := 6^{m-1} + 7 \cdot 3^m \cdot 2^{m-1}$, the window is
$W(m,7) = \{K : 3^m < 2^K \text{ and } 2^K \mathrm{den}_m \le \mathrm{num}_m\}$.
Note $2^K \mathrm{den}_m$ is strictly increasing in $K$, so each window is an
interval of integers, computed exactly:

| $m$ | $\mathrm{den}_m$ | $\mathrm{num}_m$ | upper cut (exact) | lower cut (exact) | $W(m,7)$ | $\#$comps $\sum_K \binom{K-1}{m-1}$ |
|---|---|---|---|---|---|---|
| $3$ | $23$ | $36 + 756 = 792$    | $23\cdot 2^5 = 736 \le 792 < 1472 = 23\cdot 2^6 \Rightarrow K \le 5$ | $2^4 = 16 \le 27 < 32 = 2^5 \Rightarrow K \ge 5$ | $\{5\}$ | $\binom{4}{2} = 6$ |
| $4$ | $37$ | $216 + 4536 = 4752$ | $37\cdot 2^7 = 4736 \le 4752 < 9472 = 37\cdot 2^8 \Rightarrow K \le 7$ | $2^6 = 64 \le 81 < 128 = 2^7 \Rightarrow K \ge 7$ | $\{7\}$ | $\binom{6}{3} = 20$ |
| $5$ | $47$ | $1296 + 27216 = 28512$ | $47\cdot 2^9 = 24064 \le 28512 < 48128 = 47\cdot 2^{10} \Rightarrow K \le 9$ | $2^7 = 128 \le 243 < 256 = 2^8 \Rightarrow K \ge 8$ | $\{8, 9\}$ | $\binom{7}{4} + \binom{8}{4} = 35 + 70 = 105$ |
| $6$ | $13$ | $7776 + 163296 = 171072$ | $13\cdot 2^{13} = 106496 \le 171072 < 212992 = 13\cdot 2^{14} \Rightarrow K \le 13$ | $2^9 = 512 \le 729 < 1024 = 2^{10} \Rightarrow K \ge 10$ | $\{10,11,12,13\}$ | $126{+}252{+}462{+}792 = 1632$ |

(Note the near miss at $m = 4$: $4736 \le 4752$ admits $K = 7$ by a margin of
$16$; exact arithmetic matters. Note also $\mathrm{den}_6 = 256 - 243 = 13$ is
tiny, which is what blows the $m=6$ window up to four values of $K$.)

By L-9906.1(iv), the hypothesized cycle yields some $K \in W(m,7)$ and a
composition $(a_1, \dots, a_m)$ of $K$ (parts $\ge 1$) with $D \mid c$,
$x = c/D$ odd, $x \ge 7$, and the $S$-orbit of $x$ closing with exponents
$(a_1, \dots, a_m)$. We now check **every** pair $(K, \text{composition})$ —
$6 + 20 + 105 + 1632 = 1763$ cases in total — and show none passes.

**5.2 Hand enumeration, $m = 3$ ($K = 5$, $D = 2^5 - 27 = 5$, $6$ cases).**
Using the $A$-set bijection (Definitions): the composition corresponds to
$1 \le A_1 < A_2 \le 4$ and $c = 9 + 3 \cdot 2^{A_1} + 2^{A_2}$:

| $(A_1, A_2)$ | $(a_1,a_2,a_3)$ | $c$ | $c \bmod 5$ |
|---|---|---|---|
| $(1,2)$ | $(1,1,3)$ | $9+6+4 = 19$  | $4$ |
| $(1,3)$ | $(1,2,2)$ | $9+6+8 = 23$  | $3$ |
| $(1,4)$ | $(1,3,1)$ | $9+6+16 = 31$ | $1$ |
| $(2,3)$ | $(2,1,2)$ | $9+12+8 = 29$ | $4$ |
| $(2,4)$ | $(2,2,1)$ | $9+12+16 = 37$| $2$ |
| $(3,4)$ | $(3,1,1)$ | $9+24+16 = 49$| $4$ |

No $c$ is divisible by $5$; there is not even a divisibility survivor. (Sanity:
the largest $c$ is $49 = 3^2 + 2^{5-3}(2\cdot 9 - 8)$, attained at
$(3,1,1) = (K{-}m{+}1, 1, 1)$, exactly as the equality case of L-9906.1(ii)
predicts.) **No cycle with $m = 3$.**

**5.3 Hand enumeration, $m = 4$ ($K = 7$, $D = 2^7 - 81 = 47$, $20$ cases).**
Composition $\leftrightarrow$ $1 \le A_1 < A_2 < A_3 \le 6$,
$c = 27 + 9\cdot 2^{A_1} + 3\cdot 2^{A_2} + 2^{A_3}$:

| $(A_1,A_2,A_3)$ | $(a_1,a_2,a_3,a_4)$ | $c$ | $c \bmod 47$ |
|---|---|---|---|
| $(1,2,3)$ | $(1,1,1,4)$ | $27{+}18{+}12{+}8 = 65$   | $18$ |
| $(1,2,4)$ | $(1,1,2,3)$ | $27{+}18{+}12{+}16 = 73$  | $26$ |
| $(1,2,5)$ | $(1,1,3,2)$ | $27{+}18{+}12{+}32 = 89$  | $42$ |
| $(1,2,6)$ | $(1,1,4,1)$ | $27{+}18{+}12{+}64 = 121$ | $27$ |
| $(1,3,4)$ | $(1,2,1,3)$ | $27{+}18{+}24{+}16 = 85$  | $38$ |
| $(1,3,5)$ | $(1,2,2,2)$ | $27{+}18{+}24{+}32 = 101$ | $7$  |
| $(1,3,6)$ | $(1,2,3,1)$ | $27{+}18{+}24{+}64 = 133$ | $39$ |
| $(1,4,5)$ | $(1,3,1,2)$ | $27{+}18{+}48{+}32 = 125$ | $31$ |
| $(1,4,6)$ | $(1,3,2,1)$ | $27{+}18{+}48{+}64 = 157$ | $16$ |
| $(1,5,6)$ | $(1,4,1,1)$ | $27{+}18{+}96{+}64 = 205$ | $17$ |
| $(2,3,4)$ | $(2,1,1,3)$ | $27{+}36{+}24{+}16 = 103$ | $9$  |
| $(2,3,5)$ | $(2,1,2,2)$ | $27{+}36{+}24{+}32 = 119$ | $25$ |
| $(2,3,6)$ | $(2,1,3,1)$ | $27{+}36{+}24{+}64 = 151$ | $10$ |
| $(2,4,5)$ | $(2,2,1,2)$ | $27{+}36{+}48{+}32 = 143$ | $2$  |
| $(2,4,6)$ | $(2,2,2,1)$ | $27{+}36{+}48{+}64 = 175$ | $34$ |
| $(2,5,6)$ | $(2,3,1,1)$ | $27{+}36{+}96{+}64 = 223$ | $35$ |
| $(3,4,5)$ | $(3,1,1,2)$ | $27{+}72{+}48{+}32 = 179$ | $38$ |
| $(3,4,6)$ | $(3,1,2,1)$ | $27{+}72{+}48{+}64 = 211$ | $23$ |
| $(3,5,6)$ | $(3,2,1,1)$ | $27{+}72{+}96{+}64 = 259$ | $24$ |
| $(4,5,6)$ | $(4,1,1,1)$ | $27{+}144{+}96{+}64 = 331$| $2$  |

No $c$ is divisible by $47$. (Sanity: max $c = 331 = 3^3 + 2^{7-4}(2\cdot 27 - 16)
= 27 + 8 \cdot 38$, attained at $(4,1,1,1) = (K{-}m{+}1,1,1,1)$ — again the exact
equality case of L-9906.1(ii).) **No cycle with $m = 4$.**

This completes a fully hand-written proof of the Main Theorem for $m \le 4$.

**5.4 Exact enumeration, $m = 5, 6$ ($105 + 1632$ cases).** These cases are
verified by the following exact-integer-arithmetic script. **Epistemic status,
stated plainly:** the mathematical reduction (L-9906.1(iv) with the windows of
5.1) is proved above; what remains is a *finite, decidable, exhaustive* case
check — a conjunction of $1737$ concrete integer divisibility/orbit statements.
The script is an **exact finite verification integral to this finite case
analysis** (it is not open-ended sampling and involves no floating point, no
randomness, and no unverified search cutoff: composition generation is exhaustive
and is cross-checked against the binomial count $\binom{K-1}{m-1}$). Per the
packet convention (NOTATION.md), it is labeled as finite verification; a reviewer
upgrading this file's status should re-run it or re-implement it independently —
each individual case is also checkable by hand.

Script (verbatim; also run for $m = 2, 3, 4$ as a cross-check of Steps 4, 5.2,
5.3):

```python
#!/usr/bin/env python3
# L-9906 exact finite enumeration (PROOF-INTEGRAL: exact finite verification
# forming the case analysis of L-9906.5; exact integer arithmetic throughout).
#
# For each m in {2,...,6}:
#   window W(m) = { K : 2^K > 3^m  and  2^K * den_m <= num_m }, where
#   den_m = 2^(m-1)*(X+1) - 3^(m-1),  num_m = 6^(m-1) + 3^m * 2^(m-1) * X,  X = 7.
#   (This is L-9906.1(iii) with X = 7, cleared of denominators.)
# For every K in W(m) and EVERY composition (a_1,...,a_m) of K with a_i >= 1:
#   c = sum_{i=1}^m 3^(m-i) * 2^(A_{i-1}),  D = 2^K - 3^m;
#   record (K, comp, x=c/D) whenever D | c  ["divisibility survivor"];
#   for survivors with x odd and x >= 7, iterate S from x and test whether the
#   orbit reproduces exponents (a_1,...,a_m) and returns to x ["orbit-closing"].
# A genuine nontrivial S-cycle with least period m would appear (anchored at its
# minimum) as an orbit-closing survivor with x odd, x >= 7.  Empty output = none exist.

from math import comb

X = 7

def S_step(x):
    """One Syracuse step on odd x: return (S(x), nu_2(3x+1))."""
    y = 3 * x + 1
    a = 0
    while y % 2 == 0:
        y //= 2
        a += 1
    return y, a

def compositions(K, m):
    """All tuples (a_1,...,a_m), a_i >= 1, sum = K, in lexicographic order."""
    if m == 1:
        if K >= 1:
            yield (K,)
        return
    for a1 in range(1, K - m + 2):
        for rest in compositions(K - a1, m - 1):
            yield (a1,) + rest

def c_of(comp):
    """c = sum_{i=1}^m 3^(m-i) 2^(A_{i-1}), A_0 = 0."""
    m = len(comp)
    c, A = 0, 0
    for i in range(1, m + 1):
        c += 3 ** (m - i) * (1 << A)
        A += comp[i - 1]
    return c

def window(m):
    """Exact K-window from L-9906.1(iii) with X = 7 plus 2^K > 3^m."""
    den = 2 ** (m - 1) * (X + 1) - 3 ** (m - 1)
    num = 6 ** (m - 1) + 3 ** m * 2 ** (m - 1) * X
    assert den > 0, (m, den)          # needs X > (3/2)^(m-1) - 1, true for m <= 6
    K = 1
    while 2 ** K <= 3 ** m:           # least K with 2^K > 3^m
        K += 1
    Ks = []
    while 2 ** K * den <= num:        # LHS strictly increasing in K, so this
        Ks.append(K)                  # loop captures the entire window
        K += 1
    return Ks, den, num

print(f"L-9906.5 exact enumeration, X = {X}")
print(f"{'m':>2} {'den_m':>6} {'num_m':>8} {'window W(m)':>16} {'#comps':>7} "
      f"{'div-survivors':>40} orbit-closing")
grand_total = 0
any_cycle = False
for m in range(2, 7):
    Ks, den, num = window(m)
    total = 0
    survivors = []
    for K in Ks:
        D = 2 ** K - 3 ** m
        assert D > 0
        comps = list(compositions(K, m))
        assert len(comps) == comb(K - 1, m - 1), (m, K)   # exhaustiveness cross-check
        for comp in comps:
            total += 1
            c = c_of(comp)
            # anchored bound (L-9906.1(ii)) sanity check, exact:
            assert c <= 3 ** (m - 1) + 2 ** (K - m) * (2 * 3 ** (m - 1) - 2 ** m), (m, K, comp)
            if c % D == 0:
                survivors.append((K, comp, c // D))
    closing = []
    for (K, comp, x) in survivors:
        if x % 2 == 1 and x >= X:
            y, ok = x, True
            for a in comp:
                y2, av = S_step(y)
                if av != a:
                    ok = False
                    break
                y = y2
            if ok and y == x:
                closing.append((K, comp, x))
    grand_total += total
    if closing:
        any_cycle = True
    print(f"{m:>2} {den:>6} {num:>8} {str(Ks if Ks else 'EMPTY'):>16} {total:>7} "
          f"{str(survivors):>40} {closing}")
print(f"total compositions checked: {grand_total}")
print("RESULT:", "NONTRIVIAL CYCLE FOUND (!!)" if any_cycle
      else "no orbit-closing survivor with x odd >= 7 for any m in {2,...,6}")

# Independent hand-window cross-check (values derived in the file by hand):
expected = {2: [], 3: [5], 4: [7], 5: [8, 9], 6: [10, 11, 12, 13]}
for m in range(2, 7):
    assert window(m)[0] == expected[m], (m, window(m)[0])
print("hand-computed windows confirmed:", expected)
```

Output (verbatim; Python 3.11.15, integers only, no external packages):

```text
L-9906.5 exact enumeration, X = 7
 m  den_m    num_m      window W(m)  #comps                            div-survivors orbit-closing
 2     13      132            EMPTY       0                                       [] []
 3     23      792              [5]       6                                       [] []
 4     37     4752              [7]      20                                       [] []
 5     47    28512           [8, 9]     105                                       [] []
 6     13   171072 [10, 11, 12, 13]    1632            [(12, (2, 2, 2, 2, 2, 2), 1)] []
total compositions checked: 1763
RESULT: no orbit-closing survivor with x odd >= 7 for any m in {2,...,6}
hand-computed windows confirmed: {2: [], 3: [5], 4: [7], 5: [8, 9], 6: [10, 11, 12, 13]}
```

**5.5 Reading the output.** For $m = 5$ (all $105$ cases) there is no
divisibility survivor at all. For $m = 6$ (all $1632$ cases) there is exactly
**one** divisibility survivor: $K = 12$, composition $(2,2,2,2,2,2)$, quotient
$x = 1$. This is precisely the retracing solution predicted by Remark 1
($2m = 12 \in W(6,7)$), and can be confirmed by hand:
$$c = 243 + 81\cdot 4 + 27 \cdot 16 + 9 \cdot 64 + 3 \cdot 256 + 1024
= 243 + 324 + 432 + 576 + 768 + 1024 = 3367 = 4096 - 729 = D .$$
It fails the test $x \ge 7$ (and indeed it is the trivial fixed point retraced
six times, of least period $1 \ne 6$; it is also excluded by L-9906.2). No case
with $x$ odd and $x \ge 7$ exists, let alone an orbit-closing one. By
L-9906.1(iv), no $S$-cycle of least period $m$ with all elements $\ge 7$ exists
for $m \in \{3,4,5,6\}$; by L-9906.2 every cycle of least period $m \ge 2$ (being
nontrivial) has all elements $\ge 7$. Hence no $S$-cycle of least period
$m \in \{3,4,5,6\}$ exists. $\blacksquare$ *(L-9906.5)*

### Step 6 — Proof of the Main Theorem

By L-9906.3 the only cycle of least period $1$ is the trivial cycle; by L-9906.4
and L-9906.5 there is no cycle of least period $2, 3, 4, 5$, or $6$ at all. So no
**nontrivial** cycle has least period $\le 6$. The equivalent fixed-point form
was proved in Step 0. $\blacksquare$ *(L-9906)*

---

## Dependency audit

Used results and exactly where:

- **D-9904** (definition of $S$; $a(x) = \nu_2(3x+1) \ge 1$): equation (1.2) in
  Step 1 (the only dynamical input to the cycle equation); the fact $a_i \ge 1$
  in (1.4), in L-9906.1(iv) (compositions have parts $\ge 1$), and in Step 4.
- **D-9905** (trivial cycle of $S$ is the fixed point $(1)$): Steps 2(a), 3, 6.
- **D-9908** (cycle notation, least period, $a_i, A_i, K$): throughout.
- **NOTATION.md conventions** (empty sums are $0$): base case of (1.1); $m=1$
  value $c = 1$ in Step 3.
- **L-9905** (cycle equation for $S$-cycles): listed as the canonical home of
  equation (1.3), but this file was authored in parallel with L-9905, so per the
  packet convention the statement is **re-derived inline** (Step 1, equations
  (1.1)–(1.3)) and nothing here depends on the L-9905 file itself. L-9905 landed
  during authoring; a statement-level comparison confirms agreement: same
  equation $x_1(2^K - 3^m) = c$ with the same $c$, same positivity
  $2^K > 3^m$, and the same anchored refinement
  $c \le 3^{m-1} + 2^{K-m}(2 \cdot 3^{m-1} - 2^m)$. A reviewer should still
  cross-check the two independent derivations; overlap is intentional and
  confined to Step 1(i)–(ii).
- **Internal order.** P0/P1 → used by Steps 2, 4, 5, 6. L-9906.2 → used by
  L-9906.5 (and Remark 2 only). L-9906.1 → used by L-9906.5 (and Remark 2).
  L-9906.3/4/5 → used by Step 6. No circularity: no statement in this file
  assumes anything about global Collatz behavior; Steps 2's orbit facts are
  three explicit one-step computations.
- **Not used:** any transcendence bound, any literature computation, any result
  from other packets or branches, floating-point arithmetic.

## Gap audit

- **Hidden finiteness assumptions.** The finiteness of the enumeration is not
  assumed: it is proved in L-9906.1(iii) ($2^K$ trapped between $3^m$ and an
  explicit rational), with the windows computed by exact integer inequalities in
  5.1. The composition count per $(m, K)$ is the standard bijection (Definitions)
  and is additionally asserted per-window in the script.
- **Exhaustiveness of the case analysis.** A hypothetical cycle *anchored at its
  minimum* is shown in L-9906.1(iv) to appear in the enumerated list; the list
  ranges over **all** $K \in W(m,7)$ and **all** compositions, so no case is
  skipped. (We do not rely on every rotation appearing — one rotation suffices.)
- **Direction of every inequality.** (1.4): sum of $\ge 1$ terms, direction
  $\ge$; (1.5): termwise $2^{A_{i-1}} \le 2^{K-m+i-1}$ times positive weights,
  direction $\le$; (1.6): additions to both sides only; the final division is by
  a quantity proved strictly positive from the hypothesis
  $X > (3/2)^{m-1} - 1$ — this hypothesis is verified for $X = 7$, $m \le 6$ at
  the start of Step 5 and fails at $m = 7$, which is flagged, not hidden. Step 4:
  $x_1 \ge 1$ is used with $D > 0$ (proved in (i)), preserving $\le$.
- **Boundary cases.** $m = 1$ handled separately (the anchored bound (ii)
  requires $m \ge 2$ and is never applied to $m = 1$); $x = 1$ degenerate
  solutions handled by the least-period argument (P0) and independently by the
  $x \ge 7$ filter; the retracing family of Remark 1 is identified in closed form
  and its appearances match the outputs exactly: within the windows,
  $2m \in W(m,7)$ holds only for $m = 6$ ($6 \notin \{5\}$, $8 \notin \{7\}$,
  $10 \notin \{8,9\}$, $12 \in \{10,\dots,13\}$), and the script found exactly
  the one survivor $(m,K) = (6,12)$; the hand analysis of L-9906.4 found the
  $m = 2$ instance at its hand-derived $K = 4$.
- **Empirical vs. universal.** The universal statements are Steps 0–4 plus the
  reduction L-9906.1(iv); the finite case check in 5.4 is exact and complete for
  the stated finite set, and is labeled as exact finite verification. The
  $n \le 10^5$ sweep in Adversarial tests is a cross-check only and carries no
  weight in the proof.
- **Spurious-solution risk.** Divisibility alone does not certify a cycle
  (Remark 1 exhibits actual spurious solutions); the elimination logic only ever
  uses the *necessity* direction (cycle $\Rightarrow$ survivor), so spurious
  survivors can only make the check more conservative, never unsound. The orbit
  test is included so that even a hypothetical odd survivor $\ge 7$ would not be
  miscounted as a cycle without closing.
- **Least-period bookkeeping.** A survivor closing with least period $d < m$,
  $d \mid m$, would not witness a period-$m$ cycle; this cannot cause a false
  elimination (we only eliminate), and the one observed closing-type solution
  ($x = 1$) is explicitly resolved. Distinctness of cycle elements is proved
  (P0(b)), not assumed.
- **What is NOT claimed.** Nothing about $m \ge 7$; nothing about $C$- or
  $T$-cycles (translation is L-9905's scope); no assertion that the trivial cycle
  is the only cycle overall.

## Adversarial tests

The following cross-checks were run in addition to the proof-integral
enumeration of 5.4. Script (verbatim):

```python
#!/usr/bin/env python3
# L-9906 adversarial tests (cross-checks; NOT part of the proof).
#
# Test A: random symbolic stress of the template algebra (L-9906.1(ii)/(iii)):
#   for random m, K and random compositions (a_i >= 1), verify with exact
#   rational arithmetic (Fraction) that
#     (A1) c <= 3^(m-1) + 2^(K-m)*(2*3^(m-1) - 2^m),
#     (A2) 2^(K-m)*(2*3^(m-1)-2^m) == 2^K*((3/2)^(m-1) - 1)   [algebraic identity],
#     (A3) equality in (A1) holds iff comp = (K-m+1, 1, 1, ..., 1),
#     (A4) window contrapositive: for random rational X > (3/2)^(m-1)-1 and any K
#          with 2^K * (X - (3/2)^(m-1) + 1) > 3^(m-1) + X*3^m, EVERY composition
#          of K has X*(2^K - 3^m) > c  (so no cycle element >= X can exist).
#
# Test B: brute-force sweep: every odd n <= 10^5 reaches 1 under S (finite,
#   exact, terminating check), hence no odd n <= 10^5 lies on a nontrivial
#   S-cycle. Cross-checks L-9906.2 (x_min not in {1,3,5}) and the m = 2 hand
#   analysis far beyond the proved range.

import random
from fractions import Fraction

random.seed(99060)

def S_step(x):
    y = 3 * x + 1
    a = 0
    while y % 2 == 0:
        y //= 2
        a += 1
    return y, a

def c_of(comp):
    m = len(comp)
    c, A = 0, 0
    for i in range(1, m + 1):
        c += 3 ** (m - i) * (1 << A)
        A += comp[i - 1]
    return c

def random_composition(K, m):
    cuts = sorted(random.sample(range(1, K), m - 1))
    parts = []
    prev = 0
    for c in cuts + [K]:
        parts.append(c - prev)
        prev = c
    return tuple(parts)

# ---- Test A ----
TRIALS = 20000
eq_seen = 0
for _ in range(TRIALS):
    m = random.randint(2, 12)
    K = random.randint(m, m + random.randint(0, 30))
    comp = random_composition(K, m) if m > 1 else (K,)
    assert len(comp) == m and all(a >= 1 for a in comp) and sum(comp) == K
    c = c_of(comp)
    bound = 3 ** (m - 1) + 2 ** (K - m) * (2 * 3 ** (m - 1) - 2 ** m)
    assert c <= bound, ("A1 FAIL", m, K, comp)                       # (A1)
    assert (Fraction(2) ** (K - m) * (2 * 3 ** (m - 1) - 2 ** m)
            == Fraction(2) ** K * (Fraction(3, 2) ** (m - 1) - 1)), "A2 FAIL"  # (A2)
    extremal = (K - m + 1,) + (1,) * (m - 1)
    if c == bound:
        eq_seen += 1
        assert comp == extremal, ("A3 FAIL", m, K, comp)             # (A3) only-if
    if comp == extremal:
        assert c == bound, ("A3 FAIL(if)", m, K, comp)               # (A3) if
    # (A4): window contrapositive with exact rationals
    Xr = Fraction(3, 2) ** (m - 1) - 1 + Fraction(random.randint(1, 40), random.randint(1, 7))
    lhs = Fraction(2) ** K * (Xr - Fraction(3, 2) ** (m - 1) + 1)
    rhs = 3 ** (m - 1) + Xr * 3 ** m
    if lhs > rhs:  # K strictly above the L-9906.1(iii) window for this X
        assert Xr * (2 ** K - 3 ** m) > c, ("A4 FAIL", m, K, comp, Xr)
print(f"Test A: {TRIALS} random (m,K,comp) trials passed "
      f"(A1-A4; {eq_seen} equality cases hit, all at the extremal composition)")

# explicit equality-attainment check for every m,K in a grid
for m in range(2, 10):
    for K in range(m, m + 12):
        comp = (K - m + 1,) + (1,) * (m - 1)
        assert c_of(comp) == 3 ** (m - 1) + 2 ** (K - m) * (2 * 3 ** (m - 1) - 2 ** m)
print("Test A': equality attained at (K-m+1,1,...,1) for all 2<=m<=9, m<=K<m+12")

# ---- Test B ----
N = 10 ** 5
max_steps = 0
worst = None
for n in range(1, N + 1, 2):
    x, steps = n, 0
    while x != 1:
        x, _ = S_step(x)
        steps += 1
        assert steps < 10 ** 6   # safety; never triggered
    if steps > max_steps:
        max_steps, worst = steps, n
print(f"Test B: every odd n <= {N} reaches 1 under S "
      f"(max odd-steps {max_steps} at n = {worst}); "
      f"hence no odd n <= {N} lies on a nontrivial S-cycle")

# ---- explicit small orbits used in L-9906.2 / L-9906.3 ----
assert S_step(1) == (1, 2)
assert S_step(3) == (5, 1)
assert S_step(5) == (1, 4)
print("Test C: S(1)=1 (a=2), S(3)=5 (a=1), S(5)=1 (a=4) confirmed")
```

Output (verbatim):

```text
Test A: 20000 random (m,K,comp) trials passed (A1-A4; 3332 equality cases hit, all at the extremal composition)
Test A': equality attained at (K-m+1,1,...,1) for all 2<=m<=9, m<=K<m+12
Test B: every odd n <= 100000 reaches 1 under S (max odd-steps 129 at n = 77031); hence no odd n <= 100000 lies on a nontrivial S-cycle
Test C: S(1)=1 (a=2), S(3)=5 (a=1), S(5)=1 (a=4) confirmed
```

Interpretation and further hand-level tests:

- **Test A/A'** stress the two load-bearing algebraic facts of the template with
  exact rational arithmetic over 20000 random $(m, K, \text{composition})$
  triples well outside the proved range ($m$ up to $12$, $K$ up to $m + 30$),
  including the equality characterization and the contrapositive of the window
  inequality (A4: above the window, *no* composition can support an element
  $\ge X$). Zero failures. (Random here stresses an already-proved universal
  statement; it is not evidence *for* the theorem, which rests on Steps 1–6.)
- **Test B** independently confirms the $m = 2$ hand analysis and the floor
  L-9906.2 far beyond their needs: no odd $n \le 10^5$ is on any nontrivial
  cycle (each such orbit provably reaches $1$ in a terminating, exact
  computation). This is a finite verification, no part of the proof.
- **Test C** re-verifies the three explicit orbit values used in Step 2.
- **Internal consistency hits worth noting:** the equality case of L-9906.1(ii)
  is attained in both hand tables (at $(3,1,1)$ with $c = 49$ and $(4,1,1,1)$
  with $c = 331$), the retracing family of Remark 1 appears exactly when
  $2m \in W(m,7)$ predicts it should ($m = 2$: $c = 3 + 4 = 7 = 2^4 - 3^2$;
  $m = 6$: $c = 3367 = 2^{12} - 3^6$), and the script's window computation is
  asserted against the hand computation of 5.1. An error in any one of the
  window algebra, the $c$ formula, or the enumeration would almost certainly
  break one of these coincidences.
- **Near-miss audit:** the tightest exact comparison in the whole proof is
  $37 \cdot 128 = 4736 \le 4752$ ($m = 4$, margin $16$); a reviewer should
  re-verify it first.

## Remaining uncertainty

1. For $m = 5, 6$ the case analysis ($105 + 1632$ cases) was executed by the
   included script rather than by hand. The reduction to those cases is fully
   proved, the arithmetic is exact integer arithmetic, and the run is
   reproducible; per the packet convention it is nevertheless labeled *finite
   verification*, and an independent reviewer should re-run or re-implement it
   (ideally in a different language) before any status upgrade. For $m \le 4$
   the entire argument, including all $3 + 6 + 20$ cases, is written out by hand
   in this file.
2. The author double-derived the geometric-sum evaluation in (ii) and the
   rearrangement (1.6), and stress-tested both exactly (Test A); residual risk
   of an algebra slip is low but a reviewer should redo (1.5)–(1.6) on paper.
3. P0 (period divisibility/distinctness) is standard but written from scratch
   here; a reviewer should check the index bookkeeping in P0(c) (the shift
   $k + tm \ge i$ trick).
4. No uncertainty is attached to the direction of the main inequalities; each is
   itemized in the Gap audit.

## Suggested next attack

- **Verification path.** Independently re-derive (1.3) (or compare with L-9905
  once landed), re-run the enumeration in an independent implementation
  (e.g. PARI/GP or a hand-rolled bignum in another language), and re-check the
  $m = 4$ near-miss $4736 \le 4752$. This file is then a candidate for
  PROVED status.
- **Pushing past $m = 6$.** The binding constraint is
  $X > (3/2)^{m-1} - 1$: with the floor $X = 7$ the template dies at $m = 7$
  (since $3^6 > 8 \cdot 2^6$). Any *proved* floor $X$ on $x_{\min}$ of a
  nontrivial cycle unlocks every $m$ with $(3/2)^{m-1} < X + 1$. E.g. Test B, if
  promoted from cross-check to a proof-integral exact finite verification (it is
  one: terminating, exact), gives the floor $x_{\min} > 10^5$ for any nontrivial
  cycle, which would unlock the template for all $m \le 29$ (since
  $(3/2)^{28} \approx 8.5 \times 10^4 < 10^5 + 1 < (3/2)^{29}$), at the price of
  much larger (but still explicit and finite)
  windows and enumeration sizes growing roughly like $\binom{K-1}{m-1}$ with
  $K \approx 1.585\,m$. A follow-up file (next free ID in this packet; L-9907 is
  already taken by the divergence-density file, and L-9905 reserves L-9910 for
  convergent constraints) could industrialize this: verified sweep to $N$ +
  template $\Rightarrow$ no cycle with $m \le M(N)$ odd elements, with the
  enumeration sizes tabulated.
- **Exploiting the template constructively (issue #9).** For synthesis, the
  window inequality quantifies the tension a genuine cycle must survive:
  $x_{\min} \le \left(3^{m-1} + \text{tail}\right)/D$ with $D = 2^K - 3^m$, so a
  candidate cycle needs $2^K/3^m - 1$ *extremely* small (of order
  $(3/2)^{m-1}/x_{\min}$). This converts cycle-hunting into a question about
  exceptionally good rational approximations $K/m \approx \log_2 3$ — the
  continued-fraction convergents of $\log_2 3$ ($K/m = 8/5, 19/12, 65/41,
  84/53, \dots$) are the only candidate shapes; a follow-up could enumerate
  convergent-shaped windows directly.
- **Refutation surface.** To refute this file one must exhibit either an error
  in Steps 0–4 (all hand-checkable), an error in the window table 5.1 (eight
  exact integer comparisons), or a composition among the $1763$ with $D \mid c$,
  $x = c/D$ odd, $x \ge 7$ — a single concrete counterexample the enumeration
  says does not exist.

---

*Authored by fable-02-p5, 2026-07-21. Scripts were run with Python 3.11.15;
both scripts and outputs are included verbatim above; no external packages,
no floating point, fixed seed for the (non-proof) randomized stress test.*
