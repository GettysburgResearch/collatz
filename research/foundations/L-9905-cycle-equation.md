# L-9905 — The cycle equation and master Diophantine constraints on Syracuse cycles

```text
Claim ID:      L-9905
Title:         The cycle equation and master Diophantine constraints on Syracuse cycles
Status:        PROVED
Authoring agent:   fable-02-p4
Reviewing agents:  fable-02-v4 (adversarial review 2026-07-21: PASS)
Created:       2026-07-21
Last updated:  2026-07-21 (fable-02-v4 review; minor documentation fixes)
Dependencies:  research/foundations/NOTATION.md (D-9904, D-9908; also D-9903, D-9905 for
               the trivial cycle, and the empty-sum/empty-product conventions)
Scope:         All S-cycles on the positive odd integers (D-9908), every m >= 1,
               including the trivial cycle. L-9905.1 and the product-formula display of
               L-9905.3 are algebraic identities valid for cycles of the same formula
               on any nonzero odd integers; the inequality chain of .3, the corollary
               of .4, and sub-claims .2, .5, .6 use x_i > 0. The A- and c-bounds of .4
               are composition-level facts using only a_i >= 1, A_0 = 0, sum a_i = K.
Related counterexample candidates: none
```

---

## Statement

Throughout, fix an $S$-cycle in the notation of D-9904/D-9908:
$x_1 \to x_2 \to \dots \to x_m \to x_1$ with least period $m \ge 1$, all $x_i$ positive
odd integers, exponents $a_i := \nu_2(3x_i+1) \ge 1$, partial sums $A_0 := 0$,
$A_i := a_1 + \dots + a_i$, and $K := A_m$. Define
$$c \;:=\; \sum_{i=1}^{m} 3^{\,m-i}\, 2^{\,A_{i-1}} \;\in\; \mathbb{Z}^+ .$$
Let $x_{\min} := \min_{1 \le i \le m} x_i$.

**L-9905.1 (cycle equation).** For every $S$-cycle and every choice of starting element
$x_1$ (see the anchoring convention in Definitions):
$$x_1 \left(2^K - 3^m\right) \;=\; c .$$

**L-9905.2 (positivity).** $c \ge 1$ always (indeed $c \ge m$); hence
$2^K - 3^m \ge 1$, so
$$2^K > 3^m, \qquad\text{equivalently}\qquad K > m \log_2 3,$$
for **every** $S$-cycle on the positive odd integers, including the trivial cycle
($m = 1$, $K = 2$).

**L-9905.3 (product formula).** For every $S$-cycle,
$$2^K \;=\; \prod_{i=1}^{m} \left(3 + \frac{1}{x_i}\right).$$
Consequently
$$3^m \;<\; 2^K \;\le\; \left(3 + \frac{1}{x_{\min}}\right)^{\!m},$$
and therefore
$$0 \;<\; K\ln 2 - m\ln 3 \;\le\; m \ln\!\left(1 + \frac{1}{3\,x_{\min}}\right) \;\le\; \frac{m}{3\,x_{\min}} .$$

**L-9905.4 (bounds on $c$).** For every $S$-cycle and every $1 \le i \le m$,
$$i - 1 \;\le\; A_{i-1} \;\le\; K - (m - i + 1),$$
and consequently
$$3^m - 2^m \;\le\; c \;\le\; 2^{K-m}\left(3^m - 2^m\right).$$
Moreover, the **anchored** refinement, which uses $A_0 = 0$ exactly: for $m \ge 2$,
$$c \;\le\; 3^{m-1} + 2^{K-m}\left(2 \cdot 3^{m-1} - 2^m\right),$$
where $2\cdot 3^{m-1} - 2^m > 0$ for $m \ge 2$. (For $m = 1$ the same expression equals
$1 = c$, so the inequality holds — with equality — for all $m \ge 1$.)

**Corollary (element bounds).** Every element $x$ of every $S$-cycle satisfies
$$\frac{3^m - 2^m}{2^K - 3^m} \;\le\; x \;\le\; \frac{2^{K-m}\left(3^m - 2^m\right)}{2^K - 3^m},$$
and the refined upper bound
$x \le \bigl(3^{m-1} + 2^{K-m}(2\cdot 3^{m-1} - 2^m)\bigr)/\bigl(2^K - 3^m\bigr)$.

**L-9905.5 (approximation corollary).** For every $S$-cycle,
$$0 \;<\; \frac{K}{m} - \log_2 3 \;\le\; \frac{1}{3\, x_{\min}\, \ln 2}.$$
Thus any cycle with large minimal element forces the rational $K/m$ to approximate
$\log_2 3$ from above with error $O(1/x_{\min})$, uniformly in $m$.
*(Remark: the continued-fraction/convergent consequence — that good approximations force
$K/m$ near convergents of $\log_2 3$ — is deferred to a planned L-9910.)*

**L-9905.6 ($m = 1$).** The only $S$-cycle with $m = 1$ is the trivial fixed point
$x = 1$ (with $a_1 = 2$, $K = 2$). Equivalently: $x(2^K - 3) = 1$ forces
$x = 1$ and $2^K - 3 = 1$, i.e. $K = 2$.

---

## Definitions

All notation is from `NOTATION.md`; the following conventions are fixed for this file.

- **Syracuse map (D-9904).** $S(x) = (3x+1)/2^{\nu_2(3x+1)}$ on the positive odd
  integers, with step exponent $a(x) = \nu_2(3x+1) \ge 1$. The defining relation of one
  step, used constantly below, is
  $$2^{a(x)}\, S(x) \;=\; 3x + 1. \tag{$\ast$}$$

- **Cycle data (D-9908).** An $S$-cycle is written $x_1 \to \dots \to x_m \to x_1$ with
  $m \ge 1$ its **least** period, i.e. $x_{i+1} = S(x_i)$ for $1 \le i \le m-1$ and
  $S(x_m) = x_1$, with $x_1, \dots, x_m$ pairwise distinct positive odd integers.
  $a_i := a(x_i)$, $A_0 := 0$, $A_i := a_1 + \dots + a_i$, $K := A_m$.

- **Cyclic index convention.** Indices are extended $m$-periodically to all integers:
  $x_{i+m} := x_i$ and $a_{i+m} := a_i$ for all $i$. With this convention the step
  relation
  $$2^{a_i}\, x_{i+1} \;=\; 3 x_i + 1 \tag{$\ast_i$}$$
  holds for **every** integer $i$; in particular $x_{m+1} = x_1$.

- **Anchoring (rotation).** "Anchoring the cycle at $x_r$" means relabelling
  $y_i := x_{r+i-1}$, $b_i := a_{r+i-1}$ ($1 \le i \le m$, cyclic convention), with
  partial sums $B_0 := 0$, $B_i := b_1 + \dots + b_i$. Then $y_1 \to \dots \to y_m \to
  y_1$ is the same $S$-cycle with the same least period $m$, and
  $$\sum_{i=1}^m b_i \;=\; \sum_{i=1}^m a_{r+i-1} \;=\; K,$$
  because both sides sum one full period of the $m$-periodic sequence $(a_i)_{i \in
  \mathbb{Z}}$. Thus $m$ and $K$ are anchor-independent; the quantity $c$ and the
  individual $A_i$ are **not** (each anchor produces its own $c$, and L-9905.1 holds for
  each anchor with its own $c$).

- **$x_{\min} := \min_{1\le i\le m} x_i$**, anchor-independent.

- **Empty sums are $0$, empty products are $1$** (NOTATION.md conventions). In
  particular, for $m = 1$: $c = 3^0 2^{A_0} = 1$, and $\sum_{i=2}^{1}(\cdots) = 0$.

- **Period vs. least period.** All proofs below use only $x_{m+1} = x_1$, i.e.
  $S^m(x_1) = x_1$. Hence every identity and inequality in this file remains valid
  verbatim if $m$ is replaced by any period of the cycle (any positive multiple of the
  least period), with $a_i, A_i, K, c$ recomputed for that period length. The standing
  convention, per D-9908, is that $m$ is the least period. (L-9905.6 concerns least
  period $1$, i.e. fixed points.)

---

## Motivation

This is the master Diophantine constraint displayed — so far without an in-repo proof —
in issue #9's cycle-synthesis program. Since a nontrivial $S$-cycle is (via D-9903/D-9905
and the standard correspondence between $C$-, $T$- and $S$-cycles) one of the valid
counterexample forms of D-9909, every candidate nontrivial cycle the project synthesizes
must satisfy L-9905.1–.5 exactly; the equation converts "find a cycle" into "find
$(m, a_1, \dots, a_m)$ with $a_i \ge 1$ such that $2^K - 3^m$ divides
$c = \sum_i 3^{m-i} 2^{A_{i-1}}$ **and** the resulting orbit closes up with least period
$m$". The bounds here feed directly into:

- **L-9906 (parallel agent, small-$m$ eliminations):** the element bounds of L-9905.4
  and the positivity constraint $2^K > 3^m$ reduce each fixed $m$ to finitely many
  $(K, \text{composition})$ candidates;
- **planned L-9910 (convergent constraints):** L-9905.5 shows large-$x_{\min}$ cycles
  force $K/m$ to be an exceptionally good upper rational approximation to $\log_2 3$,
  which is where continued-fraction and Baker-type input enters;
- **cycle-synthesis searches:** any synthetic candidate failing these (cheaply checkable)
  constraints can be discarded before expensive verification.

For counterexample construction the direction of use is: these constraints are
*necessary*, so they carve out the (small) region of parameter space where a nontrivial
cycle could still live; they do not by themselves exclude one.

---

## Proof

### Step 0: setup

Fix an $S$-cycle as in Definitions, with the cyclic index convention, so that
$(\ast_i)$: $2^{a_i} x_{i+1} = 3x_i + 1$ holds for all $i$. All $x_i$ are positive odd
integers, all $a_i \ge 1$ are integers, $0 = A_0 < A_1 < \dots < A_m = K$, and $K \ge m$
(sum of $m$ integers each $\ge 1$). Fix an anchor; by the anchoring convention it
suffices to prove every claim for the anchor $x_1$, since any other anchor produces the
same situation after relabelling, with the same $m$ and $K$.

### Step 1: telescoping identity (proof of L-9905.1)

**Lemma 1.1 (telescoping along any orbit).** Let $x_1$ be any positive odd integer, let
$x_{j+1} := S^j(x_1)$ for $j \ge 0$, and let $a_j, A_j$ be as above (no cycle assumption).
Then for every $j \ge 0$:
$$2^{A_j}\, x_{j+1} \;=\; 3^j x_1 \;+\; \sum_{i=1}^{j} 3^{\,j-i}\, 2^{\,A_{i-1}}. \tag{1}$$

*Proof of Lemma 1.1.* Induction on $j$.

- **Base $j = 0$:** LHS $= 2^{A_0} x_1 = x_1$; RHS $= 3^0 x_1 + (\text{empty sum}) =
  x_1$. ✓
- **Inductive step:** assume (1) for some $j \ge 0$. Using $A_{j+1} = A_j + a_{j+1}$ and
  the step relation $(\ast_{j+1})$: $2^{a_{j+1}} x_{j+2} = 3x_{j+1} + 1$,
  $$
  2^{A_{j+1}} x_{j+2}
  \;=\; 2^{A_j}\bigl(2^{a_{j+1}} x_{j+2}\bigr)
  \;=\; 2^{A_j}\bigl(3 x_{j+1} + 1\bigr)
  \;=\; 3\cdot 2^{A_j} x_{j+1} \;+\; 2^{A_j}.
  $$
  Substituting the inductive hypothesis for $2^{A_j} x_{j+1}$:
  $$
  2^{A_{j+1}} x_{j+2}
  \;=\; 3^{\,j+1} x_1 \;+\; \sum_{i=1}^{j} 3^{\,(j+1)-i}\, 2^{\,A_{i-1}} \;+\; 3^0\, 2^{\,A_{(j+1)-1}}
  \;=\; 3^{\,j+1} x_1 \;+\; \sum_{i=1}^{j+1} 3^{\,(j+1)-i}\, 2^{\,A_{i-1}},
  $$
  which is (1) for $j+1$. $\square$

**Proof of L-9905.1.** Apply Lemma 1.1 with $j = m$ along the cycle. By cyclicity
$x_{m+1} = x_1$ and $A_m = K$, so (1) reads
$$2^{K} x_1 \;=\; 3^m x_1 \;+\; \sum_{i=1}^{m} 3^{\,m-i}\, 2^{\,A_{i-1}} \;=\; 3^m x_1 + c,$$
i.e. $x_1(2^K - 3^m) = c$. By the anchoring convention the same argument applied to the
relabelled cycle gives, for every anchor $x_r$, the equation $x_r(2^K - 3^m) = c_r$ with
$c_r := \sum_{i=1}^m 3^{m-i} 2^{B_{i-1}}$ built from the rotated exponents. $\blacksquare$

*Remark 1.2 (sign-agnostic identity).* Lemma 1.1 and L-9905.1 use only the step
relation $(\ast_i)$ and integer arithmetic — never the positivity of the $x_i$. Hence
the cycle equation holds verbatim for cycles of the formula
$x \mapsto (3x+1)/2^{\nu_2(3x+1)}$ on **negative** odd integers as well (equivalently,
$3x-1$-cycles on positive odds under $x \mapsto -x$); there $2^K - 3^m$ and $x_1$ are
both negative. This is exploited in the Adversarial tests. Positivity of the $x_i$ is
used only from L-9905.2 onward.

*Remark 1.3 (parity consistency check).* $c$ is odd: the $i = 1$ term is $3^{m-1} 2^{A_0}
= 3^{m-1}$ (odd), while for $i \ge 2$, $A_{i-1} \ge a_1 \ge 1$ makes the term even. This
is consistent with L-9905.1, since $x_1$ and $2^K - 3^m$ are both odd.

### Step 2: proof of L-9905.2

Each summand of $c$ is $3^{m-i} 2^{A_{i-1}} \ge 3^0 2^0 = 1$ (a positive integer, since
$m - i \ge 0$ and $A_{i-1} \ge 0$), and there are $m \ge 1$ summands; hence $c \ge m \ge
1$. By L-9905.1, $x_1 (2^K - 3^m) = c \ge 1 > 0$; since $x_1 \ge 1 > 0$, this forces
$2^K - 3^m > 0$. As $2^K - 3^m$ is an integer, $2^K - 3^m \ge 1$, i.e. $2^K \ge 3^m + 1
> 3^m$. Taking base-$2$ logarithms (strictly increasing) gives $K > m\log_2 3$.

This applies to every $S$-cycle on positive odds; for the trivial cycle (D-9905:
$m = 1$, $x_1 = 1$, $a_1 = \nu_2(4) = 2$, $K = 2$) it reads $4 > 3$ and $2 > \log_2 3
\approx 1.585$. $\blacksquare$

### Step 3: proof of L-9905.3

Since every $x_i \ge 1 > 0$, we may divide $(\ast_i)$ by $x_{i+1} \ne 0$ and factor:
$$2^{a_i} \;=\; \frac{3x_i + 1}{x_{i+1}} \;=\; \left(3 + \frac{1}{x_i}\right)\frac{x_i}{x_{i+1}}.$$
Multiplying over one full period $i = 1, \dots, m$ and using the cyclic convention
$x_{m+1} = x_1$:
$$2^K \;=\; \prod_{i=1}^m 2^{a_i}
\;=\; \prod_{i=1}^m \left(3 + \frac{1}{x_i}\right) \cdot \prod_{i=1}^m \frac{x_i}{x_{i+1}}
\;=\; \prod_{i=1}^m \left(3 + \frac{1}{x_i}\right),$$
because the second product telescopes cyclically to
$(x_1 x_2 \cdots x_m)/(x_2 \cdots x_m x_1) = 1$. (For $m = 1$ this is the single
identity $2^K = 3 + 1/x_1$; trivial cycle: $4 = 3 + 1$.)

**Consequences.** For each $i$: $x_i \ge x_{\min} \ge 1$, so
$3 < 3 + \tfrac{1}{x_i} \le 3 + \tfrac{1}{x_{\min}}$. Multiplying these $m$ inequalities
(all factors positive):
$$3^m \;<\; 2^K \;\le\; \left(3 + \frac{1}{x_{\min}}\right)^{\!m},$$
where the left inequality is strict (each factor strictly exceeds $3$) and the right one
admits equality iff $x_i = x_{\min}$ for all $i$, which by distinctness of cycle elements
forces $m = 1$ (and indeed holds for the trivial cycle).

Taking natural logarithms (strictly increasing) and using
$\ln\!\left(3 + \tfrac{1}{x_{\min}}\right) = \ln 3 + \ln\!\left(1 + \tfrac{1}{3 x_{\min}}\right)$:
$$0 \;<\; K \ln 2 - m \ln 3 \;\le\; m \ln\!\left(1 + \frac{1}{3 x_{\min}}\right).$$
Finally, the elementary inequality $\ln(1+t) \le t$ for all $t > -1$ — proof: $e^u \ge
1 + u$ for all real $u$ (the function $e^u - 1 - u$ has derivative $e^u - 1$, negative
for $u<0$ and positive for $u>0$, so its minimum value, at $u = 0$, is $0$); substitute
$u = \ln(1+t)$ to get $1 + t \ge 1 + \ln(1+t)$ — applied with $t = 1/(3x_{\min}) > 0$
gives
$$m \ln\!\left(1 + \frac{1}{3 x_{\min}}\right) \;\le\; \frac{m}{3 x_{\min}}. \qquad\blacksquare$$

### Step 4: proof of L-9905.4

**The $A$-bounds.** Fix $1 \le i \le m$. Since every $a_j \ge 1$:
- $A_{i-1} = \sum_{j=1}^{i-1} a_j \ge i - 1$ (a sum of $i-1$ terms each $\ge 1$; for
  $i = 1$ this is the empty sum $A_0 = 0 \ge 0$);
- $A_{i-1} = K - \sum_{j=i}^{m} a_j \le K - (m - i + 1)$ (the subtracted sum has
  $m - i + 1 \ge 1$ terms each $\ge 1$).

Both are equalities in the extreme composition $a_1 = \dots = a_m = 1$ (then $K = m$ and
$A_{i-1} = i-1 = K - m + i - 1$); more precisely the lower bound is an equality iff
$a_1 = \dots = a_{i-1} = 1$ and the upper iff $a_i = \dots = a_m = 1$.

**Geometric-sum evaluation.** For any integer $m \ge 1$:
$$\sum_{i=1}^{m} 3^{\,m-i}\, 2^{\,i-1}
\;=\; \sum_{j=0}^{m-1} 3^{\,m-1-j}\, 2^{\,j}
\;=\; 3^{m-1} \sum_{j=0}^{m-1} \left(\frac{2}{3}\right)^{\!j}
\;=\; 3^{m-1} \cdot \frac{1 - (2/3)^m}{1 - 2/3}
\;=\; 3^m - 2^m. \tag{2}$$
(Equivalently: $(3-2)\sum_{j=0}^{m-1} 3^{m-1-j} 2^j = 3^m - 2^m$ by telescoping —
an integer identity requiring no division.)

**Lower bound on $c$.** Term-by-term, $2^{A_{i-1}} \ge 2^{i-1}$ (monotonicity of
$t \mapsto 2^t$ and the $A$-bound), so by (2):
$$c \;=\; \sum_{i=1}^{m} 3^{\,m-i} 2^{\,A_{i-1}} \;\ge\; \sum_{i=1}^{m} 3^{\,m-i} 2^{\,i-1} \;=\; 3^m - 2^m.$$

**Plain upper bound on $c$.** Term-by-term, $2^{A_{i-1}} \le 2^{K-m+i-1} =
2^{K-m} \cdot 2^{i-1}$, so by (2):
$$c \;\le\; 2^{K-m} \sum_{i=1}^{m} 3^{\,m-i}\, 2^{\,i-1} \;=\; 2^{K-m}\left(3^m - 2^m\right).$$

**Anchored upper bound.** The plain upper bound wastes the $i = 1$ term: there
$A_0 = 0$ **exactly**, while the bound used $A_0 \le K - m$ (weak whenever $K > m$,
which by L-9905.2 always holds: $K > m \log_2 3 > m$). Keeping $i = 1$ exact and
bounding only $i \ge 2$:
$$c \;=\; 3^{m-1} + \sum_{i=2}^{m} 3^{\,m-i} 2^{\,A_{i-1}}
\;\le\; 3^{m-1} + 2^{K-m} \sum_{i=2}^{m} 3^{\,m-i}\, 2^{\,i-1},$$
and by (2),
$$\sum_{i=2}^{m} 3^{\,m-i}\, 2^{\,i-1} \;=\; \left(3^m - 2^m\right) - 3^{m-1}
\;=\; 3^{m-1}(3 - 1) - 2^m \;=\; 2\cdot 3^{m-1} - 2^m .$$
Hence for $m \ge 2$ (where the $i \ge 2$ range is nonempty):
$$c \;\le\; 3^{m-1} + 2^{K-m}\left(2\cdot 3^{m-1} - 2^m\right),$$
with $2 \cdot 3^{m-1} - 2^m = 2\,(3^{m-1} - 2^{m-1}) > 0$ for $m \ge 2$. For $m = 1$ the
$i \ge 2$ sum is empty, $c = 1$, and the displayed expression equals $3^0 + 2^{K-1}\cdot
(2 - 2) = 1$, so the inequality holds (with equality) for all $m \ge 1$. Since $K \ge m$
gives $3^{m-1} \le 2^{K-m} 3^{m-1}$, the anchored bound is $\le$ the plain bound, and
strictly sharper whenever $K > m$ — i.e. always, by L-9905.2.

**Corollary (element bounds).** Let $x = x_r$ be any element of the cycle. Anchor the
cycle at $x_r$ (Definitions): by L-9905.1, $x_r(2^K - 3^m) = c_r$, where $c_r$ is built
from the rotated exponent sequence $(b_i) = (a_{r+i-1})$, which again satisfies
$b_i \ge 1$, $B_0 = 0$, $\sum b_i = K$. The three bounds just proved used **only** these
properties, so they apply to $c_r$:
$$3^m - 2^m \;\le\; c_r \;\le\; \min\Bigl\{\,2^{K-m}(3^m - 2^m),\;\; 3^{m-1} + 2^{K-m}\bigl(2\cdot 3^{m-1} - 2^m\bigr)\Bigr\}.$$
Dividing by the positive integer $2^K - 3^m \ge 1$ (L-9905.2):
$$\frac{3^m - 2^m}{2^K - 3^m} \;\le\; x \;\le\; \frac{2^{K-m}\left(3^m - 2^m\right)}{2^K - 3^m},$$
together with the refined upper bound from the anchored estimate. $\blacksquare$

*Check on the trivial cycle:* $m = 1$, $K = 2$: bounds read $\tfrac{1}{1} \le 1 \le
\tfrac{2 \cdot 1}{1} = 2$ (refined: $1 \le 1$). ✓

### Step 5: proof of L-9905.5

Divide the chain of L-9905.3,
$$0 \;<\; K\ln 2 - m\ln 3 \;\le\; m\ln\!\left(1 + \frac{1}{3x_{\min}}\right) \;\le\; \frac{m}{3\,x_{\min}},$$
by the positive quantity $m \ln 2$:
$$0 \;<\; \frac{K}{m} - \log_2 3 \;\le\; \frac{1}{\ln 2}\,\ln\!\left(1 + \frac{1}{3x_{\min}}\right) \;\le\; \frac{1}{3\, x_{\min}\, \ln 2}.$$
(This is the bound displayed in the Statement of L-9905.5.)
So $K/m$ is a rational strictly above $\log_2 3$ within distance
$\frac{1}{3\ln 2}\cdot\frac{1}{x_{\min}} < \frac{0.481}{x_{\min}}$ — an $O(1/x_{\min})$
one-sided approximation, uniform in $m$. Since a nontrivial cycle is known (by finite
verification of the conjecture up to large bounds, external to this file) to require
huge $x_{\min}$, this pins $K/m$ extremely close to $\log_2 3$; the precise
continued-fraction consequence (which convergents/denominators $m$ are admissible) is
deferred to the planned L-9910 and is **not** claimed here. $\blacksquare$

### Step 6: proof of L-9905.6

Let $m = 1$; the cycle is a fixed point $x = x_1$ of $S$, with $a_1 = \nu_2(3x+1)$ and
$K = a_1$. Here $c = \sum_{i=1}^{1} 3^{0} 2^{A_0} = 1$, so L-9905.1 reads
$$x\,(2^K - 3) \;=\; 1 .$$
By L-9905.2, $2^K - 3 \ge 1$; so $x$ and $2^K - 3$ are positive integers with product
$1$, forcing $x = 1$ and $2^K - 3 = 1$, i.e. $K = 2$. (Alternatively, without invoking
L-9905.2: $x \ge 1$ is a positive integer dividing $1$, so $x = 1$, and then $2^K - 3 =
1$.) Conversely, $x = 1$ is indeed a fixed point: $3 \cdot 1 + 1 = 4$, $\nu_2(4) = 2$,
$S(1) = 4/4 = 1$, with least period $m = 1$ and $K = a_1 = 2$ — the trivial cycle of
D-9905. Hence the trivial fixed point is the **only** $S$-cycle with $m = 1$.
$\blacksquare$

---

## Dependency audit

| Dependency | Where used |
|---|---|
| D-9904 (Syracuse map, exponent $a(x) = \nu_2(3x+1) \ge 1$) | Step relation $(\ast)$/$(\ast_i)$, used in Lemma 1.1, Step 3; $a_i \ge 1$ used in Steps 2 and 4. |
| D-9908 (cycle notation: $m$, $a_i$, $A_i$, $K$) | Throughout; cyclicity $x_{m+1} = x_1$ used at the end of Step 1 and in the telescoping product of Step 3. |
| D-9905 (trivial cycle of $S$ is the fixed point $1$) | Statement of L-9905.2; converse direction of Step 6. |
| D-9903 (odd part) | Only via D-9904. |
| NOTATION.md conventions (empty sum $= 0$, empty product $= 1$) | Base case of Lemma 1.1; $m = 1$ cases of L-9905.1 and the anchored bound. |
| Elementary facts proved inline | Geometric sum (2) in Step 4; $e^u \ge 1 + u$, hence $\ln(1+t) \le t$ ($t > -1$), in Step 3; strict monotonicity of $\log$ in Steps 2–3. |

No result from any other claim file is used; the file is self-contained modulo
NOTATION.md. In particular there is no dependence on L-9906 or L-9910 (which will depend
on **this** file, not conversely), so no circularity is possible. Nothing here assumes
the Collatz conjecture or its negation.

## Gap audit

Deliberate search against the README §8 checklist:

- **Hidden finiteness assumptions:** none — every statement quantifies over all
  $S$-cycles, and each proof is a finite manipulation of one arbitrary fixed cycle. No
  claim is made that nontrivial cycles exist or not.
- **Unjustified induction:** the only induction is Lemma 1.1, over $j \le m$ with an
  explicit base case and step; it runs along a genuine $S$-orbit, so each $(\ast_{j+1})$
  is an instance of D-9904.
- **Boundary cases:** $m = 1$ is handled explicitly in L-9905.1 (empty-sum base case,
  $c = 1$), L-9905.3 (single-factor product), L-9905.4 (anchored bound degenerates to
  equality $1 = 1$; the statement is asserted for $m \ge 2$ precisely to keep the
  "refinement" claim honest), and L-9905.6. $i = 1$ in the $A$-bounds is the empty-sum
  case $0 \le 0 \le K - m$. The trivial cycle is checked numerically at every step.
- **Empirical vs. universal confusion:** the Adversarial tests section is labeled finite
  verification and is not cited in any proof.
- **Limit interchanges:** none occur.
- **Circular dependence:** see Dependency audit — none.
- **Nonuniform estimates:** the constant in L-9905.5 is explicit ($1/(3\ln 2)$) and
  uniform in $m$ and in the cycle.
- **Assumptions equivalent to Collatz:** none; all results are consistent both with
  existence and nonexistence of nontrivial cycles.
- **Division-by-zero / sign errors:** Step 3 divides by $x_{i+1} \ne 0$ and by
  $x_{\min} \ne 0$; Step 4's corollary divides by $2^K - 3^m$, shown $\ge 1$ in Step 2
  **before** it is used as a positive denominator. Remark 1.2 records exactly where
  positivity enters (Step 2 onward), and the negative-cycle tests confirm the
  conclusions of Step 2 genuinely fail without it.
- **Least-period subtleties:** proofs use only $S^m(x_1) = x_1$; the Definitions section
  records that all statements hold for non-least periods too, so nothing silently relies
  on minimality except L-9905.6 (where $m = 1$ *means* fixed point) and the equality
  discussion after L-9905.3 (which uses distinctness of elements only to characterize the
  equality case, not for the inequality itself).
- **Anchor-dependence:** $c$ depends on the anchor; the file never treats $c$ as
  anchor-invariant. The element-bounds corollary re-derives the bounds for each rotated
  $c_r$ from the rotation-invariant hypotheses ($b_i \ge 1$, $B_0 = 0$, $\sum b_i = K$).

No gaps found; all six sub-claims are asserted as fully proved above.

## Adversarial tests

**Finite verification, not proof.** Exact integer/rational arithmetic (Python
`int` / `fractions.Fraction`); no floating point except the labeled illustration of the
L-9905.5 chain. Script kept at
`scratchpad/l9905_tests.py` (session-local); full code inline below for
reproducibility. Run: `python3 l9905_tests.py` (Python ≥ 3.8; stdlib only).

Design notes:
1. **Test 1** attacks Lemma 1.1 where it is strongest — as an identity along *arbitrary*
   orbit segments (206 odd starts including $27$, $703$, $871$, $6171$, $2^{40}{+}1$,
   $3^{25}{+}2$, and a 17-digit odd; $j = 0..60$), independent of any cycle structure.
2. **Test 2** checks L-9905.1/.3 on all four known cycles of the same formula over the
   odd integers — the trivial positive cycle and the negative-domain cycles through
   $-1$, $-5$, $-17$ (the $3x{-}1$ analogues; no sign conventions needed, since $S$'s
   formula applies verbatim to negative odds) — at **every** anchor/rotation, and checks
   all positivity consequences (L-9905.2/.4/.5) on the positive cycle while confirming
   they **fail** on the negative cycles exactly as Remark 1.2 predicts ($2^K < 3^m$
   there).
3. **Test 3** checks the $A$-bounds and all three $c$-bounds of L-9905.4 over **all**
   6475 exponent compositions with $m \le 6$, $K \le 14$ (the bounds are proved for
   arbitrary compositions with $a_i \ge 1$, so this is the correct adversarial domain —
   it is much larger than the set of realizable cycles), plus anchored $\le$ plain.
   Equality counts match the characterizations in Step 4: lower bound tight iff
   $a_1 = \dots = a_{m-1} = 1$ (69 compositions), plain upper tight iff all $a_i = 1$
   (6 compositions, one per $m$), anchored tight in 69 compositions.
4. **Test 4** supports L-9905.6: $x(2^K - 3) = 1$ has the unique solution $(1, 2)$ for
   $K \le 30$, and $S$ has no odd fixed point in $[1, 10^6]$ other than $1$.

```python
#!/usr/bin/env python3
"""
Adversarial tests for L-9905 (research/foundations/L-9905-cycle-equation.md).
FINITE VERIFICATION ONLY -- not a proof.
Agent: fable-02-p4.  Date: 2026-07-21.  All arithmetic exact (Python ints / Fraction).
"""
from fractions import Fraction
from itertools import product as iproduct
import math

def v2(n):
    assert n != 0
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k

def S(x):
    """Syracuse step for any odd integer x (3x+1 != 0): returns (S(x), a(x))."""
    y = 3 * x + 1
    e = v2(y)
    return y // 2**e, e

fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

# ---------------------------------------------------------------- Test 1
# Telescoping identity (proof step of L-9905.1) along ARBITRARY S-orbit
# segments, not just cycles:
#   2^{A_j} x_{j+1} = 3^j x_1 + sum_{i=1}^{j} 3^{j-i} 2^{A_{i-1}},  j = 0..60.
starts = list(range(1, 400, 2)) + [703, 871, 6171, 2**40 + 1, 3**25 + 2,
                                   12345678901234567]
n_tele = 0
for x1 in starts:
    xs = [x1]; a = []
    for _ in range(60):
        nxt, e = S(xs[-1]); xs.append(nxt); a.append(e)
    A = [0]
    for e in a:
        A.append(A[-1] + e)
    for j in range(len(a) + 1):
        lhs = 2**A[j] * xs[j]                     # xs[j] = x_{j+1} = S^j(x_1)
        rhs = 3**j * x1 + sum(3**(j - i) * 2**A[i - 1] for i in range(1, j + 1))
        check(f"telescope x1={x1} j={j}", lhs == rhs)
        n_tele += 1
print(f"Test 1: telescoping identity checked at {n_tele} (x1, j) pairs "
      f"({len(starts)} start values, j = 0..60).")

# ---------------------------------------------------------------- Test 2
# Cycle equation + product formula on ACTUAL S-cycles over the odd integers.
# S extends verbatim to negative odds; its known cycles there are the
# 3x-1-analogue loops through -1, -5, -17.  The cycle equation and product
# formula are sign-agnostic identities and must hold on all of them; the
# POSITIVITY conclusions (L-9905.2/.4/.5) must hold exactly on the positive
# (trivial) cycle and must FAIL on the negative ones -- confirming the proof
# of L-9905.2 genuinely uses x_i > 0.
def find_cycle(x0):
    seen = {}; x = x0; path = []
    while x not in seen:
        seen[x] = len(path); path.append(x)
        x, _ = S(x)
    return path[seen[x]:]

for x0 in (1, -1, -5, -17):
    cyc = find_cycle(x0)
    m = len(cyc)
    for r in range(m):                       # every rotation = every anchor
        xs = cyc[r:] + cyc[:r]
        a = [S(x)[1] for x in xs]
        A = [0]
        for e in a:
            A.append(A[-1] + e)
        K = A[m]
        c = sum(3**(m - i) * 2**A[i - 1] for i in range(1, m + 1))
        tag = f"x1={xs[0]} m={m} K={K}"
        # L-9905.1 (identity, all cycles, every anchor):
        check(f"cycle-eq {tag}", xs[0] * (2**K - 3**m) == c)
        # L-9905.3 product formula, exact rationals (all cycles):
        prod = math.prod([Fraction(3) + Fraction(1, x) for x in xs],
                         start=Fraction(1))
        check(f"product {tag}", prod == 2**K)
        if all(x > 0 for x in xs):
            xmin = min(xs)
            check(f"c>=1 {tag}", c >= 1)
            check(f"2^K>3^m {tag}", 2**K > 3**m)
            check(f"2^K<=(3+1/xmin)^m {tag}",
                  Fraction(2**K) <= (Fraction(3) + Fraction(1, xmin))**m)
            check(f"c-lower {tag}", 3**m - 2**m <= c)
            check(f"c-upper {tag}", c <= 2**(K - m) * (3**m - 2**m))
            check(f"c-anchored {tag}",
                  c <= 3**(m - 1) + 2**(K - m) * (2 * 3**(m - 1) - 2**m))
            for x in xs:                     # element bounds (L-9905.4 cor.)
                check(f"elem-lower {tag} x={x}",
                      3**m - 2**m <= x * (2**K - 3**m))
                check(f"elem-upper {tag} x={x}",
                      x * (2**K - 3**m) <= 2**(K - m) * (3**m - 2**m))
            # L-9905.5 numeric chain (floats, illustration only; the exact
            # equivalent 2^K <= (3+1/xmin)^m was checked above):
            gap = K / m - math.log2(3)
            check(f"K/m gap {tag}",
                  0 < gap <= 1 / (3 * xmin * math.log(2)) + 1e-15)
        else:
            check(f"neg: 2^K<3^m {tag}", 2**K < 3**m)
    print(f"Test 2: cycle through x0={x0}: m={m}, "
          f"a={tuple(S(x)[1] for x in cyc)}, K={sum(S(x)[1] for x in cyc)}, "
          f"cycle={tuple(cyc)}  -- all applicable checks passed so far.")

# ---------------------------------------------------------------- Test 3
# c-bounds (L-9905.4) for ALL exponent compositions a_i >= 1, m <= 6, K <= 14
# (the bounds are proved for arbitrary such compositions, so this is the
# right adversarial domain).  Also A-bounds and anchored <= plain.
count = 0; eq_lo = eq_hi = eq_anch = 0
for m in range(1, 7):
    for a in iproduct(range(1, 15), repeat=m):
        K = sum(a)
        if K > 14:
            continue
        A = [0]
        for e in a:
            A.append(A[-1] + e)
        c = sum(3**(m - i) * 2**A[i - 1] for i in range(1, m + 1))
        lo = 3**m - 2**m
        hi = 2**(K - m) * (3**m - 2**m)
        anch = 3**(m - 1) + 2**(K - m) * (2 * 3**(m - 1) - 2**m)
        for i in range(1, m + 1):
            check(f"A-bounds m={m} a={a} i={i}",
                  i - 1 <= A[i - 1] <= K - (m - i + 1))
        check(f"lo m={m} a={a}", lo <= c)
        check(f"hi m={m} a={a}", c <= hi)
        check(f"anch m={m} a={a}", c <= anch)
        check(f"anch<=hi m={m} a={a}", anch <= hi)
        eq_lo += (c == lo); eq_hi += (c == hi); eq_anch += (c == anch)
        count += 1
print(f"Test 3: {count} compositions (m<=6, K<=14) checked; "
      f"equality attained: lower {eq_lo}, plain-upper {eq_hi}, "
      f"anchored-upper {eq_anch} times.")

# ---------------------------------------------------------------- Test 4
# L-9905.6 support: (a) x(2^K - 3) = 1 over K = 1..30 has the sole solution
# (x, K) = (1, 2) in positive integers; (b) no odd fixed point of S in
# [1, 10^6] other than x = 1.
sols = [(1, K) for K in range(1, 31) if 2**K - 3 == 1]
check("m=1 solutions", sols == [(1, 2)])
fixed = [x for x in range(1, 10**6, 2) if S(x)[0] == x]
check("S fixed points <= 1e6", fixed == [1])
print(f"Test 4: x(2^K-3)=1 solutions for K<=30: {sols}; "
      f"odd fixed points of S below 10^6: {fixed}.")

print("RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-21, CPython 3, Linux):**

```text
Test 1: telescoping identity checked at 12566 (x1, j) pairs (206 start values, j = 0..60).
Test 2: cycle through x0=1: m=1, a=(2,), K=2, cycle=(1,)  -- all applicable checks passed so far.
Test 2: cycle through x0=-1: m=1, a=(1,), K=1, cycle=(-1,)  -- all applicable checks passed so far.
Test 2: cycle through x0=-5: m=2, a=(1, 2), K=3, cycle=(-5, -7)  -- all applicable checks passed so far.
Test 2: cycle through x0=-17: m=7, a=(1, 1, 1, 2, 1, 1, 4), K=11, cycle=(-17, -25, -37, -55, -41, -61, -91)  -- all applicable checks passed so far.
Test 3: 6475 compositions (m<=6, K<=14) checked; equality attained: lower 69, plain-upper 6, anchored-upper 69 times.
Test 4: x(2^K-3)=1 solutions for K<=30: [(1, 2)]; odd fixed points of S below 10^6: [1].
RESULT: ALL CHECKS PASSED
```

Worked negative-cycle instance (hand-checkable): the cycle through $-17$ has $m = 7$,
$a = (1,1,1,2,1,1,4)$, $K = 11$; here $2^{11} - 3^7 = 2048 - 2187 = -139$ and indeed
$x_1(2^K - 3^m) = (-17)(-139) = 2363 = c$, while $2^K < 3^m$ — positivity fails exactly
because the elements are negative.

## Remaining uncertainty

All six sub-claims are, in the author's assessment, fully proved; no statement required
correction. Points a verifier should nevertheless probe:

1. **Index bookkeeping in Lemma 1.1** (the single most error-prone spot): that the
   $i$-th summand carries $2^{A_{i-1}}$ (not $2^{A_i}$) and $3^{m-i}$, and that the
   inductive step's new term is $3^0 2^{A_j}$ with $j = (j{+}1) - 1$. Test 1 checks this
   at 12,566 instances, but an independent hand-derivation is the real check.
2. **Anchor-invariance of $K$** in the element-bounds corollary — the one-line "full
   period of an $m$-periodic sequence" argument in Definitions.
3. **Equality discussions** (after L-9905.3 and in Step 4) are side remarks with lighter
   scrutiny than the main chain; they are not used by any downstream claim.
4. The floating-point check of the L-9905.5 chain in Test 2 uses a $10^{-15}$ tolerance;
   the rigorous content is carried entirely by the exact-rational check
   $2^K \le (3 + 1/x_{\min})^m$, so nothing depends on float behavior.
5. This file deliberately does **not** claim the $C$-cycle/$T$-cycle $\leftrightarrow$
   $S$-cycle correspondence (used informally in Motivation); if downstream work needs it
   as a lemma, it should be proved separately.

## Suggested next attack

- **L-9906 (small-$m$ elimination, parallel agent):** combine L-9905.2 with the element
  bounds. For fixed $m$, admissible $K$ is the least integer with $2^K > 3^m$ **at
  most** a bounded range above it (larger $K$ makes the upper element bound
  $2^{K-m}(3^m - 2^m)/(2^K - 3^m)$ collapse toward $2^{K-m}\cdot$const while the
  divisibility $(2^K - 3^m) \mid c$ becomes very restrictive); enumerate compositions
  and refute closure. The anchored bound strictly shrinks the search box.
- **L-9910 (convergents):** from L-9905.5, a nontrivial cycle with
  $x_{\min} > N$ forces $0 < K/m - \log_2 3 < 1/(3N\ln 2)$; combine with the theory of
  continued fractions of $\log_2 3$ (and, later, Baker–Rhin-type lower bounds on
  $|K\ln 2 - m\ln 3|$) to force $m$ to be astronomically large.
- **Refutation attempts:** try to break the anchored bound with adversarial compositions
  at larger $m, K$ than Test 3 covers (the author expects it to hold — Step 4's proof is
  composition-general — but the test range $m \le 6$, $K \le 14$ is small); try to
  construct a non-cycle composition where $(2^K - 3^m) \mid c$ yet the orbit fails to
  close, to calibrate how far the Diophantine constraints are from sufficient.
- **Strengthening:** prove the exact rotation-invariance structure of the $m$ values
  $c_r$ (e.g. $\sum_r c_r$ and $\prod_r$ relations), which may feed a sharper
  cycle-synthesis sieve.

---
*File authored by fable-02-p4, 2026-07-21. Status PROPOSED per NOTATION.md conventions;
an independent reviewing agent may upgrade after verification.*

---

## Verification note (fable-02-v4, 2026-07-21)

Independent adversarial review per README §13, performed without relying on the
author's confidence or reusing the author's test code. **Verdict: PASS.** All six
sub-claims (and the element-bounds corollary) verified; three documentation-only
fixes applied (§3 below); no mathematical content changed. Status upgraded
PROPOSED → PROVED. Per protocol, this review does **not** set
INDEPENDENTLY_VERIFIED.

### 1. Independent reconstruction of the arguments

- **Telescoping identity (L-9905.1), re-derived from scratch.** Set
  $P_j := 2^{A_j} x_{j+1}$. Then $P_0 = 2^{A_0} x_1 = x_1$, and $(\ast_{j+1})$ gives
  $$P_{j+1} = 2^{A_j}\bigl(2^{a_{j+1}} x_{j+2}\bigr) = 2^{A_j}(3x_{j+1} + 1)
  = 3P_j + 2^{A_j}.$$
  Unrolling this affine recursion:
  $P_j = 3^j x_1 + \sum_{k=0}^{j-1} 3^{\,j-1-k}\, 2^{A_k}$, which after $i = k+1$
  is exactly the file's (1). The author-flagged off-by-one bookkeeping is
  **correct**: the $i$-th summand carries $2^{A_{i-1}}$ (not $2^{A_i}$), the $i = 1$
  term is $3^{j-1} 2^{A_0} = 3^{j-1}$ with $A_0 = 0$ exact, and the term appended at
  the inductive step is $3^0 2^{A_j}$. At $j = m$, cyclicity ($x_{m+1} = x_1$,
  $A_m = K$) yields $x_1(2^K - 3^m) = c$. The worked $-17$ instance was recomputed
  by hand: $a = (1,1,1,2,1,1,4)$, $K = 11$, $c = 729 + 486 + 324 + 216 + 288 + 192 +
  128 = 2363 = (-17)(-139)$. ✓
- **Anchor-invariance of $K$** (load-bearing for the element-bounds corollary):
  $\{r, r+1, \dots, r+m-1\}$ meets each residue class mod $m$ exactly once, and
  $(a_i)_{i \in \mathbb{Z}}$ is $m$-periodic, so $\sum_{i=1}^m b_i = \sum_{i=1}^m
  a_{r+i-1} = \sum_{i=1}^m a_i = K$. Sound. The corollary then needs only
  $b_i \ge 1$, $B_0 = 0$, $\sum b_i = K$ — which is all Step 4's bound proofs use —
  plus $2^K - 3^m \ge 1$ (L-9905.2) as a positive denominator. No gap.
- **Anchored-bound algebra re-verified:** $(3^m - 2^m) - 3^{m-1} = 2 \cdot 3^{m-1}
  - 2^m$; and plain $-$ anchored $= 3^{m-1}(2^{K-m} - 1) \ge 0$, strict iff
  $K > m$, exactly as claimed at the end of Step 4.
- **Equality side remarks** (author flagged lighter scrutiny) — all re-derived,
  and confirmed computationally as exact iff's (Test 3 below): lower $c$-bound
  tight iff $a_1 = \dots = a_{m-1} = 1$ ($a_m$ free); plain upper tight iff all
  $a_i = 1$; anchored tight iff $m = 1$ or $a_2 = \dots = a_m = 1$ ($a_1$ free);
  the per-$i$ $A$-bound equality cases as stated in Step 4. The equality case of
  $2^K \le (3 + 1/x_{\min})^m$ (all $x_i = x_{\min}$, hence $m = 1$) is the **one**
  place least-periodicity/distinctness is genuinely used — correctly recorded in
  the Gap audit. It is genuinely needed there: for the non-least period $m' = 2$ of
  the trivial cycle, $2^4 = (3 + 1)^2$ attains equality with $m' > 1$.
- **Hypothesis usage map** (checked line by line): positivity of the $x_i$ first
  enters in Step 2 ($x_1 \ge 1$ converts $c > 0$ into $2^K > 3^m$) and is needed in
  the inequality chain of .3, the corollary of .4, and in .5 and .6; L-9905.1 and
  the product-formula display of .3 are sign-agnostic, and the $A$-/$c$-bounds of
  .4 are composition-level. Remark 1.2 states this correctly; the Scope header was
  slightly coarser and has been fixed (§3). The separation is airtight: the
  negative-domain cycles through $-1, -5, -17$ satisfy the equation and product
  formula at every rotation while $2^K < 3^m$; in Step 6 the factorization
  $(x, 2^K - 3) = (-1, -1)$ also solves $x(2^K - 3) = 1$, so $x \ge 1$ is exactly
  the hypothesis that forces uniqueness.
- **Period vs. least period:** confirmed every proof uses only $S^m(x_1) = x_1$,
  so .1–.5 hold verbatim for any period multiple (checked computationally, Test
  2b). The file claims exactly this — neither over- nor under-claimed.
- **L-9905.5:** division of the .3 chain by $m \ln 2 > 0$ re-checked;
  $1/(3 \ln 2) = 0.4809\ldots < 0.481$ confirmed.

First unsupported inference: **none found.** The only defects were the two
wording items fixed in §3.

### 2. Independent computational refutation attempt

Script written from the Statement section alone (not adapted from the author's
inline tests); exact integer/`Fraction` arithmetic, with `decimal` at 60 digits
for the log chain — and the potentially *tight* middle step of that chain checked
in exact rational form ($2^K \le (3+1/x_{\min})^m$), so no conclusion depends on
rounding. Kept at `scratchpad/l9905_verify_fable02v4.py` (session-local); full
code:

```python
#!/usr/bin/env python3
"""
INDEPENDENT adversarial verification of L-9905 (fable-02-v4, 2026-07-21).
Written from the Statement section of L-9905-cycle-equation.md alone, without
reusing the author's test code. FINITE VERIFICATION ONLY -- not a proof.
Exact arithmetic: Python int / fractions.Fraction; the log-chain uses
decimal.Decimal at 60 significant digits (near-equality steps are instead
checked in exact rational form).
"""
from fractions import Fraction
from itertools import product as iproduct
from decimal import Decimal, getcontext
import random

getcontext().prec = 60
LN2 = Decimal(2).ln()
LN3 = Decimal(3).ln()
LOG2_3 = LN3 / LN2
EPS = Decimal(10) ** -50          # slack for Decimal comparisons w/ strict gap

failures = []
def chk(label, ok):
    if not ok:
        failures.append(label)
        print("FAIL:", label)

def v2(n):
    assert n != 0
    k = 0
    while n % 2 == 0:
        n //= 2; k += 1
    return k

def S(x):
    """Syracuse formula on any odd integer x (3x+1 is even, nonzero)."""
    y = 3 * x + 1
    e = v2(y)
    return y // 2**e, e

def cycle_data(xs):
    """Given the element list of one period (in orbit order), return (a, A, K, c)."""
    m = len(xs)
    a = [S(x)[1] for x in xs]
    A = [0]
    for e in a:
        A.append(A[-1] + e)
    K = A[m]
    c = sum(3**(m - i) * 2**A[i - 1] for i in range(1, m + 1))
    return a, A, K, c

# ------------------------------------------------------------------ Test 1
# Lemma 1.1 along arbitrary orbit segments (my own start set, j = 0..50):
#   2^{A_j} x_{j+1} = 3^j x_1 + sum_{i=1}^{j} 3^{j-i} 2^{A_{i-1}}.
starts = list(range(1, 202, 2)) + [27, 447, 639, 703, 871, 6171, 77671,
                                   2**50 + 1, 3**30 + 2, 10**18 + 1]
n1 = 0
for x1 in starts:
    xs = [x1]
    a = []
    for _ in range(50):
        nxt, e = S(xs[-1]); xs.append(nxt); a.append(e)
    A = [0]
    for e in a:
        A.append(A[-1] + e)
    for j in range(51):
        lhs = 2**A[j] * xs[j]
        rhs = 3**j * x1 + sum(3**(j - i) * 2**A[i - 1] for i in range(1, j + 1))
        chk(f"T1 telescope x1={x1} j={j}", lhs == rhs)
        n1 += 1
print(f"Test 1: {n1} (x1, j) instances of the telescoping identity "
      f"({len(starts)} starts, j=0..50) -- OK so far.")

# ------------------------------------------------------------------ Test 2
# All four known cycles of the same formula on the odd integers, every
# rotation: cycle equation, c odd, c >= m, exact product formula; positivity
# consequences on the positive cycle, and their FAILURE (2^K < 3^m) on the
# negative cycles.
def find_cycle(x0):
    seen = {}; x = x0; path = []
    while x not in seen:
        seen[x] = len(path); path.append(x); x = S(x)[0]
    return path[seen[x]:]

for x0 in (1, -1, -5, -17):
    cyc = find_cycle(x0)
    m = len(cyc)
    for r in range(m):
        xs = cyc[r:] + cyc[:r]
        a, A, K, c = cycle_data(xs)
        tag = f"x1={xs[0]} m={m} K={K}"
        chk(f"T2 eq {tag}", xs[0] * (2**K - 3**m) == c)          # L-9905.1
        chk(f"T2 c-odd {tag}", c % 2 == 1)                       # Rmk 1.3
        chk(f"T2 c>=m {tag}", c >= m)                            # L-9905.2
        prod = Fraction(1)
        for x in xs:
            prod *= Fraction(3) + Fraction(1, x)
        chk(f"T2 prod {tag}", prod == 2**K)                      # L-9905.3 id.
        if all(x > 0 for x in xs):
            xmin = min(xs)
            chk(f"T2 2^K>3^m {tag}", 2**K > 3**m)                # L-9905.2
            chk(f"T2 2^K<=(3+1/xmin)^m {tag}",                   # .3 chain, exact
                Fraction(2)**K <= (Fraction(3) + Fraction(1, xmin))**m)
            # log chain, Decimal (only genuinely-strict steps; the possibly
            # tight middle step was just checked exactly above):
            lhs = K * LN2 - m * LN3
            mid = m * (Decimal(3 * xmin + 1) / Decimal(3 * xmin)).ln()
            chk(f"T2 chain>0 {tag}", lhs > 0)
            chk(f"T2 mid<=m/3xmin {tag}",
                mid <= Decimal(m) / (3 * xmin) + EPS)
            chk(f"T2 L9905.5 {tag}",                             # L-9905.5
                Decimal(K) / m - LOG2_3
                <= 1 / (3 * xmin * LN2) + EPS)
            lo = 3**m - 2**m
            hi = 2**(K - m) * (3**m - 2**m)
            anch = 3**(m - 1) + 2**(K - m) * (2 * 3**(m - 1) - 2**m)
            chk(f"T2 c-bounds {tag}", lo <= c <= min(hi, anch))  # L-9905.4
            for x in xs:                                         # element bds
                lhsx = x * (2**K - 3**m)
                chk(f"T2 elem {tag} x={x}",
                    lo <= lhsx <= hi and lhsx <= anch)
        else:
            chk(f"T2 neg 2^K<3^m {tag}", 2**K < 3**m)            # .2 fails
    print(f"Test 2: cycle({x0}): elements {tuple(cyc)}, m={m}, "
          f"a={tuple(S(x)[1] for x in cyc)}, K={sum(S(x)[1] for x in cyc)} "
      f"-- OK so far.")

# ------------------------------------------------------------------ Test 2b
# Non-least periods: the file claims L-9905.1/.3 hold verbatim when m is any
# period (multiple of the least period).  Traverse each cycle t times.
for x0, ts in ((1, (2, 3, 4)), (-1, (2, 3)), (-5, (2, 3)), (-17, (2,))):
    cyc = find_cycle(x0)
    for t in ts:
        xs0 = cyc * t
        mm = len(xs0)
        for r in range(mm):
            xs = xs0[r:] + xs0[:r]
            a, A, K, c = cycle_data(xs)
            tag = f"x0={x0} t={t} r={r}"
            chk(f"T2b eq {tag}", xs[0] * (2**K - 3**mm) == c)
            prod = Fraction(1)
            for x in xs:
                prod *= Fraction(3) + Fraction(1, x)
            chk(f"T2b prod {tag}", prod == 2**K)
            if all(x > 0 for x in xs):
                chk(f"T2b pos {tag}", 2**K > 3**mm)
print("Test 2b: non-least-period equation/product checks done -- OK so far.")

# ------------------------------------------------------------------ Test 3
# L-9905.4 over ALL compositions a_i >= 1 with m <= 6, K <= 15 (bounds are
# composition-level facts).  Also: A-bounds, anchored <= plain, and the
# exact iff equality characterizations from Step 4 / the test notes.
count = 0; n_lo = n_hi = n_anch = 0
for m in range(1, 7):
    for a in iproduct(range(1, 16), repeat=m):
        K = sum(a)
        if K > 15:
            continue
        A = [0]
        for e in a:
            A.append(A[-1] + e)
        c = sum(3**(m - i) * 2**A[i - 1] for i in range(1, m + 1))
        for i in range(1, m + 1):
            chk(f"T3 A m={m} a={a} i={i}",
                i - 1 <= A[i - 1] <= K - (m - i + 1))
        lo = 3**m - 2**m
        hi = 2**(K - m) * (3**m - 2**m)
        anch = 3**(m - 1) + 2**(K - m) * (2 * 3**(m - 1) - 2**m)
        chk(f"T3 lo m={m} a={a}", lo <= c)
        chk(f"T3 hi m={m} a={a}", c <= hi)
        chk(f"T3 anch m={m} a={a}", c <= anch)
        chk(f"T3 anch<=hi m={m} a={a}", anch <= hi)
        chk(f"T3 anch<hi iff K>m m={m} a={a}", (anch < hi) == (K > m))
        # iff characterizations of equality:
        chk(f"T3 lo-iff m={m} a={a}",
            (c == lo) == all(e == 1 for e in a[:m - 1]))
        chk(f"T3 hi-iff m={m} a={a}",
            (c == hi) == all(e == 1 for e in a))
        chk(f"T3 anch-iff m={m} a={a}",
            (c == anch) == (m == 1 or all(e == 1 for e in a[1:])))
        n_lo += (c == lo); n_hi += (c == hi); n_anch += (c == anch)
        count += 1
print(f"Test 3: {count} compositions (m<=6, K<=15); equalities: "
      f"lower {n_lo}, plain-upper {n_hi}, anchored {n_anch}.")

# ------------------------------------------------------------------ Test 3b
# Random larger compositions beyond the author's range: m in 7..12, a_i in
# 1..6 (so K up to 72), 20000 samples, fixed seed.
rng = random.Random(99053)
for trial in range(20000):
    m = rng.randint(7, 12)
    a = [rng.randint(1, 6) for _ in range(m)]
    K = sum(a)
    A = [0]
    for e in a:
        A.append(A[-1] + e)
    c = sum(3**(m - i) * 2**A[i - 1] for i in range(1, m + 1))
    lo = 3**m - 2**m
    hi = 2**(K - m) * (3**m - 2**m)
    anch = 3**(m - 1) + 2**(K - m) * (2 * 3**(m - 1) - 2**m)
    chk(f"T3b m={m} a={tuple(a)}", lo <= c <= anch <= hi)
print("Test 3b: 20000 random compositions m in 7..12 -- OK so far.")

# ------------------------------------------------------------------ Test 4
# L-9905.6: (a) x(2^K - 3) = 1 in positive integers, K <= 40: only (1, 2);
# (b) odd fixed points of S in [1, 1e6]: only 1; (c) in [-1e6, -1]: only -1
# (localizes exactly why positivity is needed in Step 6).
sols = [(1, K) for K in range(1, 41) if 2**K - 3 == 1]
chk("T4 unique sol", sols == [(1, 2)])
fix_pos = [x for x in range(1, 10**6, 2) if S(x)[0] == x]
fix_neg = [x for x in range(-1, -10**6, -2) if S(x)[0] == x]
chk("T4 pos fixed", fix_pos == [1])
chk("T4 neg fixed", fix_neg == [-1])
print(f"Test 4: x(2^K-3)=1 (K<=40): {sols}; fixed pts of S in [1,1e6]: "
      f"{fix_pos}; in [-1e6,-1]: {fix_neg}.")

# ------------------------------------------------------------------ Test 5
# ln(1+t) <= t at t = 1/(3x), x = 1..1000, Decimal 60 digits (strict).
for x in range(1, 1001):
    t = Decimal(1) / (3 * x)
    chk(f"T5 x={x}", (Decimal(3 * x + 1) / Decimal(3 * x)).ln() < t)
print("Test 5: ln(1+t) < t at 1000 sample points -- OK so far.")

print("RESULT:", "ALL CHECKS PASSED" if not failures
      else f"{len(failures)} FAILURES")
```

**Output (verbatim, run 2026-07-21, CPython 3, Linux):**

```text
Test 1: 5661 (x1, j) instances of the telescoping identity (111 starts, j=0..50) -- OK so far.
Test 2: cycle(1): elements (1,), m=1, a=(2,), K=2 -- OK so far.
Test 2: cycle(-1): elements (-1,), m=1, a=(1,), K=1 -- OK so far.
Test 2: cycle(-5): elements (-5, -7), m=2, a=(1, 2), K=3 -- OK so far.
Test 2: cycle(-17): elements (-17, -25, -37, -55, -41, -61, -91), m=7, a=(1, 1, 1, 2, 1, 1, 4), K=11 -- OK so far.
Test 2b: non-least-period equation/product checks done -- OK so far.
Test 3: 9948 compositions (m<=6, K<=15); equalities: lower 75, plain-upper 6, anchored 75.
Test 3b: 20000 random compositions m in 7..12 -- OK so far.
Test 4: x(2^K-3)=1 (K<=40): [(1, 2)]; fixed pts of S in [1,1e6]: [1]; in [-1e6,-1]: [-1].
Test 5: ln(1+t) < t at 1000 sample points -- OK so far.
RESULT: ALL CHECKS PASSED
```

Cross-check against the author's Test 3 counts: my range is $K \le 15$ vs the
author's $K \le 14$; my equality counts 75/6/75 equal the author's 69/6/69 plus
exactly the six $K = 15$ members of each tight family ($(1,\dots,1,16-m)$ for
the lower bound, $(16-m,1,\dots,1)$ for the anchored bound, $m = 1..6$; the
plain-upper family all have $K = m \le 6 < 15$). Consistent. Test 3b extends the
$c$-bounds beyond the author's range ($m \le 12$, $K \le 72$); the suggested
refutation attempt at larger $(m, K)$ found nothing, as expected from the
composition-general proof.

### 3. Fixes applied by the reviewer (documentation only)

1. **Scope header:** previously listed all of .3 as a sign-agnostic identity and
   all of .4 as positivity-dependent. Corrected: only the product-formula
   display of .3 is sign-agnostic (its inequality chain uses $x_i > 0$, as Step 3
   and Remark 1.2 already said), and the $A$-/$c$-bounds of .4 are
   composition-level (only the corollary uses positivity). The proofs were always
   correct on this point; only the header summary was coarse.
2. **Step 5:** replaced the stray phrase "as in the task statement" (a dangling
   reference to the authoring context, contrary to README §17.3's spirit) with a
   reference to the Statement of L-9905.5.
3. Header: Status PROPOSED → PROVED; Reviewing agents and Last updated fields
   filled in.

### 4. Caveats

- Only one positive $S$-cycle (the trivial one) exists as test data, so the
  positivity-dependent chain (.3 consequences, .5) is computationally exercised
  on a single genuine positive cycle plus its non-least-period repetitions; its
  proof, however, is a complete deduction from the product formula and does not
  rest on that computation.
- Useful spare observation (not needed for the verdict): equality in the plain
  upper bound of .4 requires $K = m$, which L-9905.2 forbids for actual positive
  cycles ($K > m \log_2 3 > m$); so for genuine cycles the anchored bound is
  always strictly sharper, as the file notes.
- The floating-point remark in the author's Remaining uncertainty item 4 is
  moot for this review: my script checks the possibly-tight step of the log
  chain in exact rationals and uses 60-digit `Decimal` only where the inequality
  is strict with large margin.
- Item 5 of Remaining uncertainty stands: the $C$/$T$-cycle $\leftrightarrow$
  $S$-cycle correspondence used informally in Motivation remains unproved in
  this packet and must not be cited from this file.

*Reviewed and upgraded by fable-02-v4, 2026-07-21.*
