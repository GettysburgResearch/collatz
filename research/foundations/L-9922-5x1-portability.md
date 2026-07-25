# L-9922 — Portability matrix for the foundations packet at $T_a$: which exclusions are format-driven and which are drift-driven, tested against the control universe $a = 5$

```text
Claim ID:      L-9922
Title:         Portability of L-9905/L-9906/L-9907/L-9913/L-9917 to the family
               T_a(n) = n/2 (n even), (a n + 1)/2 (n odd), a odd >= 3; exact
               verification against the three known T_5-cycles; the verdict
               table (format-driven vs drift-driven) and the atypicality budget
Status:        PROPOSED
Authoring agent:   fable-02-p16
Reviewing agents:  (none yet)
Created:       2026-07-25
Last updated:  2026-07-25
Dependencies:  research/foundations/NOTATION.md (D-9902 shortcut map, D-9903 odd
                 part, D-9904 Syracuse map, D-9905 trivial cycles, D-9906 parity
                 vector, D-9907 divergence, D-9908 S-cycle notation; empty-sum
                 and empty-product conventions).
               L-9905 (Status: PROVED, fable-02-v4) — the a = 3 originals of
                 L-9922.1, .2, .3 (L-9905.1, .2, .3, .4, .5, .6).  Cited as the
                 port target; every ported proof is given in full here, so no
                 step of this file rests on L-9905's proofs.
               L-9906 (Status: PROVED, fable-02-v5) — port target for the floor
                 L-9906.2 (x_min >= 7) and the elimination template L-9906.1.
               L-9907 (Status: PROVED, fable-02-v6) — port target for L-9922.6.
               L-9913 (Status: PROVED, fable-02-v18) — port target for L-9922.4
                 (the fractional-part squeeze, m*(F) and the value 2966).
               L-9917 (Status: PROVED, fable-02-v17) — port target for L-9922.5
                 (sorted-element product bound, the 46-element elimination set,
                 m_0 = 196).
               L-9902 (Status: PROVED, fable-02-v2) — L-9902.1/.2 (parity
                 bijection) is ported in L-9922.7 to make the atypicality budget
                 a theorem rather than a heuristic; the ported proof is given
                 inline.
               L-9918 (Status: PROPOSED, unreviewed) — its L-9918.5(3) "sign
                 criterion" is the object issue #26 asks about.  NOT LOAD-
                 BEARING: the sign criterion is re-derived here from the ported
                 cycle equation in three lines (L-9922.3(2)), so nothing in this
                 file inherits L-9918's PROPOSED status.
Scope:         The family T_a, a an ODD integer >= 3, and its Syracuse map S_a on
               the positive odd integers.  L-9922.1 and the product-formula part
               of .2 are algebraic identities valid for cycles on any nonzero
               odd integers; .2's positivity, .3, .4, .5 use x_i > 0.  Every
               numerical value quoted for a = 5 is either an exact integer
               computation (labelled as such) or a FINITE VERIFICATION over an
               explicitly stated finite range (labelled X-9922.*), never a proof
               about all cycles of T_5.  Nothing in this file is a statement
               about whether the Collatz conjecture (a = 3) is true.
Related counterexample candidates: none
```

---

## Statement

### Notation for this file

For an **odd** integer $a \ge 3$ define
$$T_a(n) \;=\; \begin{cases} n/2 & n \text{ even}\\ (a n + 1)/2 & n \text{ odd}\end{cases}
\qquad (n \in \mathbb{Z}^+),$$
and the associated **Syracuse map** on the positive odd integers
$$S_a(x) \;=\; \frac{a x + 1}{2^{\nu_2(a x + 1)}}, \qquad
a(x) \;:=\; \nu_2(a x + 1) \;\ge\; 1 .$$
($a(x) \ge 1$ because $a$ and $x$ are odd, so $ax+1$ is even; $S_a(x)$ is again a
positive odd integer.) At $a = 3$, $T_3 = T$ (D-9902) and $S_3 = S$ (D-9904).

An **$S_a$-cycle** is written as in D-9908: $x_1 \to x_2 \to \dots \to x_m \to x_1$,
least period $m \ge 1$, all $x_i$ pairwise distinct positive odd integers,
$x_{i+m} := x_i$, $a_i := a(x_i) \ge 1$, $A_0 := 0$, $A_i := a_1 + \dots + a_i$,
$K := A_m$, $x_{\min} := \min_i x_i$. Put
$$c_a \;:=\; \sum_{i=1}^m a^{\,m-i}\, 2^{\,A_{i-1}} \in \mathbb{Z}^+, \qquad
\alpha_a \;:=\; \log_2 a, \qquad \gamma_a \;:=\; \log_a 2 \;=\; 1/\alpha_a .$$
At $a = 3$: $c_3 = c$, $\alpha_3 = \log_2 3 = 1.5849625\ldots$,
$\gamma_3 = \log_3 2 = 0.6309298\ldots$; at $a = 5$: $\alpha_5 = 2.3219280\ldots$,
$\gamma_5 = 0.4306765\ldots$.

**Verdict vocabulary** (as required by issue #26). Each port carries exactly one label:

* **HOLDS-VERBATIM** — the $a = 3$ proof, read with every occurrence of the literal
  $3$ replaced by the map parameter $a$, is a correct proof for every odd $a \ge 3$;
  no numerical constant other than the map parameter itself appears.
* **HOLDS-WITH-MODIFIED-CONSTANT** — same architecture, but some constant that is
  invisible at $a = 3$ becomes visible; the new constant is stated exactly.
* **BREAKS-AT-CONSTANT-$X$** — the statement is false, or its hypothesis is
  unavailable, for some odd $a \ge 3$; the exact constant $X$ at which the flip
  happens is named.

---

### X-9922.0 (deliverable zero; finite verification) — the $a = 5$ cycles, exactly

**X-9922.0(a).** The following are $S_5$-cycles, verified by exact integer arithmetic
(Adversarial test T1):

| name | $S_5$-cycle (anchored at $x_{\min}$) | $m$ | $(a_1,\dots,a_m)$ | $(A_0,\dots,A_m)$ | $K$ | $c_5$ | $2^K - 5^m$ | $x_{\min}$ | full $T_5$-cycle ($K$ elements) |
|---|---|---|---|---|---|---|---|---|---|
| $\mathcal C_0$ | $1 \to 3 \to 1$ | $2$ | $(1,4)$ | $(0,1,5)$ | $5$ | $7$ | $7$ | $1$ | $1,3,8,4,2$ |
| $\mathcal C_1$ | $13 \to 33 \to 83 \to 13$ | $3$ | $(1,1,5)$ | $(0,1,2,7)$ | $7$ | $39$ | $3$ | $13$ | $13,33,83,208,104,52,26$ |
| $\mathcal C_2$ | $17 \to 43 \to 27 \to 17$ | $3$ | $(1,3,3)$ | $(0,1,4,7)$ | $7$ | $51$ | $3$ | $17$ | $17,43,108,54,27,68,34$ |

and $x_1(2^K - 5^m) = c_5$ holds in each case: $1\cdot 7 = 7$, $13 \cdot 3 = 39$,
$17 \cdot 3 = 51$.

**X-9922.0(b) (exhaustiveness in a finite region).** The three cycles above are
**exactly** the $S_5$-cycles all of whose elements are $< 10^8$. Equivalently, the
odd integers $< 10^8$ lying on an $S_5$-cycle contained in $[1,10^8)$ are exactly
$\{1,3,13,17,27,33,43,83\}$. (Test T1; a second, structurally different search —
period-bounded rather than height-bounded — reproduces the same list, Test T6.)
This is a **finite verification**, not a theorem about all $T_5$-cycles.

**X-9922.0(c) (corrections to the framing).**

1. **Issue #26's two listings are CORRECT as printed.** $13 \to 33 \to 83 \to 208
   \to 104 \to 52 \to 26 \to 13$ and $17 \to 43 \to 108 \to 54 \to 27 \to 68 \to 34
   \to 17$ are genuine $T_5$-cycles, each of length $7$; no element, order, or arrow
   is wrong.
2. **Issue #26 omits the third cycle** $1 \to 3 \to 8 \to 4 \to 2 \to 1$. This is
   the $a = 5$ analogue of the trivial cycle, and it is *structurally different from
   $a = 3$*: $S_5$ has **no fixed point at all**, because $x(2^K - 5) = 1$ forces
   $2^K = 6$. The "trivial" cycle at $a = 5$ has $m = 2$, $K = 5$. (See L-9922.2(4).)
3. **The assigning brief's "$m = 3$ and $m = 4$" is wrong.** Both nontrivial cycles
   have $m = 3$ **and** $K = 7$; they share the pair $(m,K)$ and even the value
   $2^K - 5^m = 3$, differing only in the exponent word. Their $x_{\min}$ are $13$
   and $17$ as the brief says.

---

### L-9922.1 (the cycle equation) — verdict: **HOLDS-VERBATIM**

Let $a \ge 3$ be odd and let $x_1 \to \dots \to x_m \to x_1$ be any $S_a$-cycle
($m \ge 1$). Then, for every choice of anchor,
$$\boxed{\;x_1\left(2^{K} - a^{m}\right) \;=\; c_a \;=\; \sum_{i=1}^m a^{\,m-i} 2^{\,A_{i-1}} .\;}$$
The identity holds for any cyclic sequence of nonzero odd integers satisfying
$2^{a_i} x_{i+1} = a x_i + 1$ with $a_i \ge 1$; positivity is not used. The only
property of the number $3$ used in L-9905.1 is that it is **odd** (so that
$\nu_2(ax+1) \ge 1$). At $a = 3$ the display is L-9905.1 verbatim.

### L-9922.2 (positivity, product formula, $c$-bounds, and $m = 1$)

Let $a \ge 3$ be odd and let $x_1 \to \dots \to x_m \to x_1$ be an $S_a$-cycle on the
**positive** odd integers.

1. **(positivity) — verdict: HOLDS-VERBATIM.** $c_a \ge m \ge 1$, hence
   $2^K - a^m \ge 1$, i.e.
   $$2^K > a^m, \qquad\text{equivalently}\qquad \frac Km > \log_2 a = \alpha_a .$$
   At $a = 5$: every $S_5$-cycle has $K/m > \log_2 5 = 2.3219280\ldots$. Both
   nontrivial cycles have $K/m = 7/3 = 2.3333\ldots$ and $\mathcal C_0$ has
   $K/m = 5/2 = 2.5$. ✓
2. **(product formula) — verdict: HOLDS-VERBATIM.**
   $$2^{K} \;=\; \prod_{i=1}^{m}\left(a + \frac{1}{x_i}\right),
   \qquad\text{hence}\qquad
   a^m \;<\; 2^K \;\le\; \left(a + \frac{1}{x_{\min}}\right)^{m}.$$
   Verified exactly at $a = 5$:
   $\left(5+\frac1{13}\right)\left(5+\frac1{33}\right)\left(5+\frac1{83}\right)
   = \frac{66\cdot166\cdot416}{13\cdot33\cdot83} = \frac{4557696}{35607} = 128 = 2^7$
   and
   $\left(5+\frac1{17}\right)\left(5+\frac1{43}\right)\left(5+\frac1{27}\right)
   = \frac{86\cdot216\cdot136}{17\cdot43\cdot27} = \frac{2526336}{19737} = 128 = 2^7$.
3. **($c$- and element bounds) — verdict: HOLDS-WITH-MODIFIED-CONSTANT
   $\;1/(a-2)$.** For every $1 \le i \le m$, $i-1 \le A_{i-1} \le K - (m-i+1)$, and
   consequently
   $$\boxed{\;\frac{a^m - 2^m}{a-2} \;\le\; c_a \;\le\; 2^{\,K-m}\,\frac{a^m - 2^m}{a-2}\;}$$
   with the anchored refinement, for $m \ge 1$,
   $$c_a \;\le\; a^{m-1} \;+\; 2^{\,K-m}\,\frac{2a^{m-1} - 2^{m}}{a-2},$$
   and the element bounds: every element $x$ of every $S_a$-cycle satisfies
   $$\frac{a^m-2^m}{(a-2)\left(2^K-a^m\right)} \;\le\; x \;\le\;
     \frac{2^{K-m}\left(a^m-2^m\right)}{(a-2)\left(2^K-a^m\right)} .$$
   **This is the one place in the packet where a naive port silently fails.** The
   $a = 3$ display of L-9905.4 reads $3^m - 2^m \le c \le 2^{K-m}(3^m-2^m)$ — the
   divisor $a - 2 = 1$ is invisible. Written that way at $a = 5$ the *lower* bound
   is **false**: $\mathcal C_1$ anchored at $13$ has $c_5 = 39$ while
   $5^3 - 2^3 = 117 > 39$. The correct general bound gives $117/3 = 39 \le 39$ —
   attained with equality. (Test T3.) This is **not** an error in L-9905, whose
   scope is $a = 3$; it is a hidden constant that any port must restore.
4. **($m = 1$) — verdict: BREAKS-AT-CONSTANT "$a+1$ a power of $2$".** For every
   odd $a \ge 3$: an $S_a$-cycle with $m = 1$ exists **iff** $a = 2^K - 1$ for some
   $K \ge 2$, and then it is the fixed point $x = 1$ with $K = \log_2(a+1)$.
   Proof: $m=1$ gives $x(2^K - a) = c_a = 1$, so $x = 1$ and $2^K = a+1$.
   Thus L-9905.6/L-9906.3 ("the only $m=1$ cycle is the trivial one") is a statement
   about the Mersenne values $a \in \{3,7,15,31,63,\dots\}$; at $a = 5$ there is **no**
   $m = 1$ cycle at all, and the cycle through $1$ is $\mathcal C_0$ with $m = 2$.
   Any argument that treats "$m = 1$ $\Rightarrow$ trivial cycle" as the base case of
   an induction is therefore using a property of $3$, not of the format.

### L-9922.3 (approximation corollary; the sign/criticality classification)

1. **(approximation corollary) — verdict: HOLDS-VERBATIM, with constant exactly $1$.**
   For every $S_a$-cycle on the positive odd integers,
   $$\boxed{\;0 \;<\; \frac Km - \log_2 a \;\le\;
     \log_2\!\left(1 + \frac{1}{a\,x_{\min}}\right) \;\le\;
     \frac{1}{a\,x_{\min}\,\ln 2}\;}$$
   i.e. the "constant" in the assigning brief's template
   $\frac{1}{a x_{\min} \ln 2}\cdot(\text{constant})$ is **exactly $1$**: the
   literal $3$ of L-9905.5 is nothing but the map parameter. At $a = 3$ this is
   L-9905.5 verbatim.
   *Exact check at $a=5$*: $\mathcal C_1$ has
   $K/m - \log_2 5 = 0.0114052\ldots$ against the bound
   $1/(5\cdot13\cdot\ln 2) = 0.0221953\ldots$ ($51.4\%$ of budget);
   $\mathcal C_2$ has the same excess against
   $1/(5\cdot17\cdot\ln2) = 0.0169729\ldots$ ($67.2\%$); $\mathcal C_0$ uses
   $61.7\%$. All three satisfy it, none is close to violating it. (Test T9, done
   exactly as $2^K \le (a + 1/x_{\min})^m$ in $\mathbb{Q}$.)
2. **(sign / criticality criterion) — verdict: HOLDS-VERBATIM.** Let
   $w \in \{0,1\}^K$ be the $T_a$-parity word of one full period of an $S_a$-cycle
   (so $|w| = K$ and $|w|_1 = m$), let $A_w := a^{m}$, $M^p := 2^{K}$, and let
   $\kappa_w$ be given by the E2 recursion of L-9918 ($\kappa_\varnothing = 0$,
   $\kappa_{wb} = a^{b}\kappa_w + b\,2^{|w|}$). Then
   $$\kappa_w \;=\; c_a, \qquad
     z_w \;:=\; \frac{\kappa_w}{M^p - A_w} \;=\; \frac{c_a}{2^K - a^m} \;=\; x_1,$$
   and $z_w > 0 \iff \kappa_w > 0$ **and** $A_w < M^p$ (*subcritical*);
   $z_w < 0 \iff \kappa_w > 0$ and $A_w > M^p$ (*supercritical*). In density terms
   $$A_w < M^p \iff a^m < 2^K \iff \frac mK \;<\; \gamma_a = \log_a 2 .$$
3. **(the answer to issue #26's key question) — YES, exactly.** The ported
   sign-criticality analysis classifies **both** known $5x+1$ cycles as
   **subcritical–positive**, and does so with all three of its conditions strictly
   satisfied:

   | cycle | word $w$ | $A_w = 5^m$ | $M^p = 2^K$ | subcritical? | $\kappa_w$ | $M^p - A_w$ | divides? | $z_w$ |
   |---|---|---|---|---|---|---|---|---|
   | $\mathcal C_1$ | $1110000$ | $125$ | $128$ | **yes** | $39$ | $3$ | $3 \mid 39$ | $13 \in \mathbb{Z}^+$ |
   | $\mathcal C_2$ | $1100100$ | $125$ | $128$ | **yes** | $51$ | $3$ | $3 \mid 51$ | $17 \in \mathbb{Z}^+$ |
   | $\mathcal C_0$ | $11000$ | $25$ | $32$ | **yes** | $7$ | $7$ | $7 \mid 7$ | $1 \in \mathbb{Z}^+$ |

   The classification is **tight**: both nontrivial cycles have odd-step density
   $m/K = 3/7 = 0.4285714\ldots$, and $\gamma_5 = 0.4306765\ldots$, a margin of only
   $0.0021051$. The criterion is not vacuous at $a=5$: the purely periodic word
   with $m = 2$, $K = 3$ (exponents $(1,2)$) is **supercritical**
   ($5^2 = 25 > 8 = 2^3$) and its unique realiser is
   $z_w = 7/(8-25) = -7/17 < 0$, a negative $2$-adic rational and not a positive
   integer — the $a = 5$ analogue of L-9918.4's $-19/11$. (Tests T1, T5.)
4. **(the drift statement hidden in the sign criterion).** A positive cycle needs a
   *subcritical* word, i.e. odd-step density $< \gamma_a$; the density of a
   uniformly random word is $1/2$; and
   $$\gamma_a < \tfrac12 \iff \log_2 a > 2 \iff a > 4 .$$
   So at $a = 3$ the *typical* word is subcritical (positive realisers are the rule,
   divergence is the exception) and at $a = 5$ the *typical* word is supercritical
   (divergence is the rule, cycles are the exception). The known $5x+1$ cycles are
   exactly the atypically-low-density words the criterion demands.

### L-9922.4 (the fractional-part squeeze) — verdict: **HOLDS-VERBATIM (theorem); its hypothesis BREAKS-AT-CONSTANT $a = 4$**

Fix an odd $a \ge 3$. Put, for a real $F \ge 1$,
$$\varepsilon(F,a) := \frac{1}{a\,F\,\ln 2}, \qquad
  \varepsilon_0(F,a) := \frac{1000}{693\,a\,F} \;>\; \varepsilon(F,a)
  \quad(\text{since } \ln 2 > 693/1000),$$
$$f_a(m) := \lceil m\alpha_a\rceil - m\alpha_a = 1 - \{m\alpha_a\} \in (0,1),$$
$$\mathrm{Adm}_{F,a}(m) :\iff f_a(m) \le \varepsilon_0(F,a)\,m, \qquad
  m^*(F,a) := \min\{m \ge 1 : \mathrm{Adm}_{F,a}(m)\} .$$
At $a = 3$, $\varepsilon_0(F,3) = 1000/(2079F)$ and these are L-9913's
$\varepsilon_0$, $f$, $\mathrm{Adm}_F$, $m^*(F)$ verbatim.

1. **(irrationality).** $\alpha_a \notin \mathbb{Q}$ for every odd $a \ge 3$ (else
   $2^p = a^q$ with $p,q \ge 1$, impossible), so $f_a(m) \in (0,1)$ for all $m \ge 1$
   and $m^*(F,a)$ is well defined.
2. **(the squeeze).** If every element of an $S_a$-cycle satisfies $x_i \ge F$, then
   $$0 \;<\; K - m\alpha_a \;\le\; \frac{m}{a F \ln 2} \;<\; \varepsilon_0(F,a)\,m,$$
   hence $\mathrm{Adm}_{F,a}(m)$ holds and $m \ge m^*(F,a)$; moreover, with
   $K/m = p/q$ in lowest terms, $\mathrm{Adm}_{F,a}(q)$ holds, so
   $m \ge q \ge m^*(F,a)$; and $\mathrm{Adm}_{F,a}(q) \Rightarrow
   \mathrm{Adm}_{F,a}(tq)$ for every $t \ge 1$.
3. **(the $a=5$ instantiations that are actually available, and the sharpness
   test).** At $a = 5$ the floors that hold are $F = 1$ (universal), $F = 7$
   (PROVED for every cycle $\ne \mathcal C_0$; L-9922.5(2)) and $F = 13$
   (EMPIRICAL only — see L-9922.5(2) for exactly how much of this is proved).
   Exact computation (Tests T2, T4, T8):
   $$m^*(1,5) = 2 \ \ (K^* = 5), \qquad m^*(7,5) = m^*(13,5) = 3 \ \ (K^* = 7),$$
   $$m^*(1,3) = 1 \ \ (K^* = 2), \qquad m^*(7,3)=m^*(6,3) = 5 \ \ (K^* = 8).$$
   **In every case where a cycle actually exists at that floor, $m^*$ equals its
   true least period and $K^*$ its true $K$:** $\mathcal C_0$ has $(m,K) = (2,5)$,
   $\mathcal C_1, \mathcal C_2$ have $(3,7)$, and the $a=3$ trivial cycle has
   $(1,2)$. The ported squeeze therefore **does not exclude any known cycle; it is
   attained with equality by all three $a=5$ cycles and by the $a=3$ trivial
   cycle.**
4. **(the large-floor table; the $a=5$ rows are HYPOTHETICAL).**

   | $F$ | $m^*(F,3)$ | $K^*(F,3)$ | $m^*(F,5)$ | $K^*(F,5)$ | is $\mathrm{(V}_F)$ available? |
   |---|---|---|---|---|---|
   | $1$ | $1$ | $2$ | $2$ | $5$ | yes (universal, both $a$) |
   | $7$ | $5$ | $8$ | $3$ | $7$ | yes for both $a$: $x_{\min} \ge 7$ for every nontrivial cycle (L-9906.2 at $a{=}3$; L-9922.5(2) at $a{=}5$) |
   | $13$ | $5$ | $8$ | $3$ | $7$ | $a{=}3$: yes (implied by $F{=}10^6$); $a{=}5$: EMPIRICAL only (needs $7,9,11$ non-periodic) |
   | $10^{6}$ | $\mathbf{2966}$ | $4701$ | $4647$ | $10790$ | $a{=}3$: **yes** (X-9901); $a{=}5$: **NO — false** |
   | $10^{7}$ | $10946$ | $17349$ | $8651$ | $20087$ | $a{=}3$: yes (X-9913); $a{=}5$: **NO — false** |
   | $10^{8}$ | $15601$ | $24727$ | $21306$ | $49471$ | $a{=}3$: yes (X-9913); $a{=}5$: **NO — false** |
   | $10^{9}$ | $\mathbf{47468}$ | $75235$ | $97879$ | $227268$ | $a{=}3$: yes (X-9913); $a{=}5$: **NO — false** |
   | $10^{12}$ | $10\,781\,274$ | $17\,087\,915$ | $1\,936\,274$ | $4\,495\,889$ | neither verified |

   The $a = 3$ column reproduces L-9913.5 and L-9913.9 **exactly** ($2966$, $10946$,
   $15601$, $47468$ with $K^* = 4701, 17349, 24727, 75235$) — the mandatory
   consistency gate. The $a=5$ entries at $F \ge 10^6$ are **arithmetic facts about
   $\log_2 5$ under a hypothesis that is FALSE at $a=5$** (cycle elements $13$ and
   $17$ are $\le 10^6$); they exclude nothing and, in particular, do **not** conflict
   with $m = 2, 3$. **There is no porting error and no error in L-9913's method**:
   the method's entire numerical strength comes from the floor $\mathrm{(V}_F)$, and
   that floor — not the squeeze — is what $a = 5$ destroys.
5. **(where exactly the hypothesis breaks).** $\mathrm{(V}_F)$ ("every $n \le F$
   reaches the cycle through $1$") is available at $a = 3$ for $F = 10^6$ (X-9901,
   independently reviewed) and, subject to the PROPOSED verification X-9913, for
   $F = 10^9$; it is **unavailable at $a = 5$ for every $F \ge 13$**, because $13$
   and $17$ lie on cycles (X-9922.0(a)) — this part is a proved statement, not an
   estimate. The *explanation* — that the constant governing it is again $a = 4$,
   since for $a > 4$ the typical orbit drifts upward ($\sqrt a/2 > 1$) so that small
   starting values are not driven into a single attractor — is **heuristic** and is
   labelled as such; what is proved is only that the hypothesis fails at $a = 5$.
6. **($m^*$ is a Diophantine, not a dynamical, quantity).** $m^*(F,a)$ depends only
   on the continued fraction of $\alpha_a$ and on $F$. The denominators realised at
   $a = 5$ are visibly convergent denominators of $\log_2 5$: $m^*(10^7,5) = 8651$,
   $m^*(10^8,5) = 21306$, $m^*(10^9,5) = 97879$, $m^*(10^{12},5) = 1936274$ are the
   denominators of the above-lying convergents $20087/8651$, $49471/21306$,
   $227268/97879$, $4495889/1936274$ of $\log_2 5$ — the exact analogue of
   L-9913.8's convergent dichotomy. That $m^*(10^{12},3) = 10781274$ exceeds
   $m^*(10^{12},5) = 1936274$ is a fact about the two continued fractions and
   carries **no** dynamical information.

### L-9922.5 (the sorted-element product bound) — verdict: **HOLDS-VERBATIM in form, HOLDS-WITH-MODIFIED-CONSTANT numerically ($1/6 \to 1/(2a)$, $31.5 \to (2^{2a}-1)/2$, $196 \to 3134$)**

For an odd integer $B \ge 1$, an odd $a \ge 3$ and $m \ge 1$ define
$$P_{B,a}(m) := \prod_{j=0}^{m-1}\left(a + \frac{1}{B+2j}\right) = \frac{N_{B,a}(m)}{D_B(m)},
\quad N_{B,a}(m) := \prod_{j=0}^{m-1}\bigl(a(B+2j)+1\bigr),\ \ D_B(m) := \prod_{j=0}^{m-1}(B+2j),$$
$$W^*_{a,B}(m) := \{K \in \mathbb{Z} : a^m < 2^K \le P_{B,a}(m)\}
 = \{K : a^m < 2^K \text{ and } 2^K D_B(m) \le N_{B,a}(m)\},$$
$$R_{a,B}(m) := \frac{P_{B,a}(m)}{a^m} = \prod_{j=0}^{m-1}\left(1 + \frac{1}{a(B+2j)}\right),
\qquad m_0(B,a) := \min\{m : R_{a,B}(m) \ge 2\},$$
$$\mathcal E_{a,B} := \{m \ge 1 : W^*_{a,B}(m) = \varnothing\}.$$

1. **(sorted floor and window; HOLDS-VERBATIM).** If the elements of an $S_a$-cycle
   are pairwise distinct positive odd integers all $\ge B$ ($B$ odd), then the sorted
   elements satisfy $x_{(j)} \ge B + 2j$ and therefore
   $$a^m \;<\; 2^K \;\le\; P_{B,a}(m), \qquad\text{i.e.}\qquad K \in W^*_{a,B}(m);$$
   hence no such cycle has $m \in \mathcal E_{a,B}$. The proof uses only
   distinctness, oddness, the floor, and L-9922.2(2).
2. **(the correct floor at $a=5$).** $1$ and $3$ lie on $\mathcal C_0$; and
   $S_5(5) = 13 \in \mathcal C_1$ with $5 \notin \mathcal C_1$, so $5$ is not
   periodic. Hence **every $S_5$-cycle other than $\mathcal C_0$ has $x_{\min} \ge 7$
   — PROVED**, by exactly L-9906.2's argument. By contrast $B = 13$ is only
   **EMPIRICAL** at $a = 5$: the $S_5$-orbits of $7, 9, 11$ neither return nor enter a
   known cycle within the verified depth (T10 records $2\cdot10^5$ $T_5$-steps from
   $7$ with no return), and, unlike $a=3$, they cannot be settled by following the
   orbit down, because they rise. *This asymmetry — that small-number elimination
   terminates at $a=3$ and does not at $a=5$ — is drift, not format.*
3. **(exact recomputation; all values are exact integer computations, Test T5).**

   | $a$ | $B$ | status of the floor | $m_0(B,a)$ | $|\mathcal E_{a,B}|$ | $\max \mathcal E_{a,B}$ | $2 \in \mathcal E$? | $3 \in \mathcal E$? |
   |---|---|---|---|---|---|---|---|
   | $3$ | $7$ | PROVED (L-9906.2) | $\mathbf{196}$ | $\mathbf{46}$ | $\mathbf{171}$ | yes | yes |
   | $5$ | $1$ | universal | $180$ | $23$ | $146$ | **no** | **no** |
   | $5$ | $7$ | PROVED (item 2) | $3134$ | $446$ | $3010$ | yes | **no** |
   | $5$ | $13$ | EMPIRICAL | $6197$ | $887$ | $6079$ | yes | **no** |

   The $a = 3$ row reproduces L-9917.3/.4 exactly (the $46$-element set, $\max = 171$,
   $m_0 = 196$), as does the general-floor row of L-9917.4(6): $m_0(B,3) = 13, 71,
   133, 196, 258, 825, 3156, 31506$ for $B = 1,3,5,7,9,27,101,1001$ — all eight
   reproduced.
   **The ported bound does not eliminate the known $a=5$ cycle lengths.** $m = 3$
   survives at every floor $B \in \{1,5,7,9,11,13,17\}$; explicitly at $B = 13$:
   $5^3 = 125 < 128 = 2^7$ and $2^7 D_{13}(3) = 424320 \le 431376 = N_{13,5}(3)$, so
   $W^*_{5,13}(3) = \{7\}$ — the true $K$. And $m = 2$ survives at the *universal*
   floor $B=1$, which is the only floor applicable to $\mathcal C_0$ ($x_{\min}=1$);
   that $2 \in \mathcal E_{5,B}$ for $B \ge 5$ is consistent, since $\mathcal C_0$
   violates those floors.
4. **(the constants that move).** $\ln R_{a,B}(m) = \sum_{j<m}\ln\!\big(1+\frac1{a(B+2j)}\big)
   = \frac{1}{2a}\ln\frac{2m+B}{B} + O(1)$, so the window width is
   $$\mathrm{Wd}_{a,B}(m) = \log_2 R_{a,B}(m) = \frac{1}{2a}\log_2 m + O(1),$$
   i.e. L-9917's rate $m^{1/6}$ becomes $m^{1/(2a)}$ — at $a = 5$, $m^{1/10}$: the
   window opens **more slowly** at $a=5$. Correspondingly the reach constant of
   L-9917.4(6) moves from $m_0(B,3)/B \to (2^6-1)/2 = 31.5$ to
   $m_0(B,a)/B \to (2^{2a}-1)/2$, i.e. $511.5$ at $a = 5$ (computed: $m_0(101,5) =
   51202$, ratio $506.95$; $m_0(11,5) = 5175$, ratio $470.45$). The method's
   elimination power therefore **grows** with $a$ in absolute terms (446 lengths
   killed at $a=5,B=7$ versus 46 at $a=3,B=7$) while remaining intrinsically finite
   for every fixed floor.
5. **(L-9906's main theorem, for the record) — verdict: BREAKS-AT-CONSTANT $a = 4$.**
   "No nontrivial $S_a$-cycle has $m \le 6$" is **false at $a = 5$** ($m = 3$ twice).
   L-9906.1's *template* (finite window + composition enumeration + divisibility)
   is HOLDS-VERBATIM and, run at $a = 5$, does not fail — it *finds*
   $\mathcal C_1, \mathcal C_2$. This is the cleanest single demonstration in this
   file that the packet's elimination *methods* are format-driven while their
   elimination *content* is drift-driven.

### L-9922.6 (parity-density threshold) — verdict: **HOLDS-VERBATIM (with $\gamma_a$); the phenomenology BREAKS-AT-CONSTANT $a = 4$**

Let $a \ge 3$ be odd, $n \in \mathbb{Z}^+$, $v_i(n) := T_a^i(n) \bmod 2$,
$a_k(n) := \sum_{i<k} v_i(n)$, $\gamma_a := \log_a 2$.

1. **(lower envelope).** For every $n$ and $k \ge 0$,
   $\;T_a^k(n) \ge n\,a^{a_k(n)}/2^k = n\,2^{\,a_k(n)\alpha_a - k}$, with equality iff
   $a_k(n) = 0$. Hence $\limsup_k a_k/k > \gamma_a \Rightarrow$ the orbit is
   unbounded, and $\liminf_k a_k/k > \gamma_a \Rightarrow T_a^k(n) \to \infty$.
2. **(divergence forces density; the deep direction).** If $T_a^k(n) \to \infty$ then
   $$\liminf_{k\to\infty}\frac{a_k(n)}{k} \;\ge\; \gamma_a \;=\; \log_a 2 .$$
   The proof is L-9907.2 verbatim with the odd-step defect
   $\varepsilon_a(x) := \log_2(1 + 1/(ax)) \downarrow 0$; it uses only that
   $\varepsilon_a(x) \to 0$ as $x \to \infty$, which holds for every $a \ge 1$.
3. **(integer dichotomy).** For every $n \in \mathbb{Z}^+$ exactly one of: the
   $T_a$-orbit is eventually periodic (hence bounded), or $T_a^k(n) \to \infty$.
   (Pigeonhole; HOLDS-VERBATIM.)
4. **(the numbers, and the flip).**
   $$\gamma_3 = 0.6309298\ldots, \qquad \gamma_5 = 0.4306765\ldots, \qquad
     \gamma_7 = 0.3562072\ldots,$$
   and
   $$\boxed{\;\gamma_a < \tfrac12 \iff a > 4 \iff \sqrt a/2 > 1.\;}$$
   $\sqrt a/2$ is the geometric-mean step multiplier of a density-$\tfrac12$ parity
   word ($0.8660$ at $a=3$, $1.1180$ at $a=5$). **This is the cleanest quantitative
   expression of the drift difference: at $a = 5$ the divergence threshold
   $\gamma_5 = 0.4307$ lies BELOW $1/2$, so the typical parity word already
   satisfies the necessary condition for divergence; at $a = 3$ the threshold
   $\gamma_3 = 0.6309$ lies ABOVE $1/2$, so divergence requires a permanent
   large-deviation excess of $0.1309$ in odd-step density.** The named constant is
   $a = 4$, equivalently $\log_2 a = 2$, equivalently $\gamma_a = 1/2$.
5. **(glider lemma) — verdict: HOLDS-WITH-MODIFIED-CONSTANT $1/(a-2)$.** For odd
   $a \ge 3$ let $\theta_a := 1/(a-2) \in \mathbb{Q}$ (note $a - 2$ is odd, hence a
   $2$-adic unit). Then for every $j \ge 1$ and $n \in \mathbb{Z}^+$:
   $$v_0(n) = \dots = v_{j-1}(n) = 1 \iff n \equiv -\theta_a \pmod{2^j},$$
   and in that case
   $$T_a^j(n) \;=\; \left(\frac a2\right)^{\! j}\bigl(n + \theta_a\bigr) - \theta_a
     \;>\; \left(\frac a2\right)^{\! j} n .$$
   At $a = 3$, $\theta_3 = 1$ and this is L-9907.5 verbatim ($n \equiv -1 \bmod 2^j$).
   At $a = 5$, $\theta_5 = 1/3$ and the all-ones class is
   $n \equiv -3^{-1} \bmod 2^j$, e.g. $n \equiv 1, 5, 21, 85 \pmod{2,8,32,256}$.
   The class has density $2^{-j}$ for every $a$; the rise factor is $(a/2)^j$.

### L-9922.7 (verdict table; format-driven vs drift-driven; the atypicality budget)

**(1) The verdict table.**

| # | ported result | verdict | the named constant / where it flips |
|---|---|---|---|
| .1 | L-9905.1 cycle equation $x_1(2^K-a^m) = c_a$ | **HOLDS-VERBATIM** | none; only "$a$ odd" is used |
| .2(1) | L-9905.2 positivity $2^K > a^m$ | **HOLDS-VERBATIM** | none |
| .2(2) | L-9905.3 product formula $2^K = \prod(a+1/x_i)$ | **HOLDS-VERBATIM** | none |
| .2(3) | L-9905.4 $c$- and element bounds | **HOLDS-WITH-MODIFIED-CONSTANT** | divisor $\dfrac1{a-2}$ — invisible at $a=3$; the $a{=}3$ form is FALSE at $a{=}5$ ($39 < 117$) |
| .2(4) | L-9905.6 / L-9906.3 "$m=1 \Rightarrow$ trivial" | **BREAKS** | exists iff $a+1$ is a power of $2$; no $S_5$ fixed point |
| .3(1) | L-9905.5 approximation corollary | **HOLDS-VERBATIM** | bound $\dfrac1{a\,x_{\min}\ln 2}$, constant exactly $1$ |
| .3(2) | L-9918.5(3) sign/criticality criterion | **HOLDS-VERBATIM** | threshold $m/K < \gamma_a$; correctly rates $\mathcal C_1,\mathcal C_2$ **subcritical–positive** |
| .4 | L-9913.2–.4 squeeze machinery | **HOLDS-VERBATIM** | $\varepsilon_0(F,a) = \dfrac{1000}{693\,aF}$; $=\dfrac{1000}{2079F}$ at $a=3$ |
| .4 | L-9913.5/.6 the value $m \ge 2966$ | **BREAKS-AT-CONSTANT $a = 4$** (hypothesis) | the verified floor $\mathrm{(V}_F)$; unavailable at $a=5$ for every $F \ge 13$ |
| .5(1) | L-9917.1/.2 sorted floor and window | **HOLDS-VERBATIM** | none |
| .5(3) | L-9917.3/.4 the $46$ lengths and $m_0 = 196$ | **HOLDS-WITH-MODIFIED-CONSTANT** | $m_0(B,a)/B \to \frac{2^{2a}-1}2$ ($31.5 \to 511.5$); width rate $\frac1{2a}$ ($\frac16 \to \frac1{10}$); $196 \to 3134$ ($B=7$), $46 \to 446$ |
| .5(5) | L-9906 main theorem "no cycle with $m \le 6$" | **BREAKS-AT-CONSTANT $a = 4$** | false at $a=5$: two cycles with $m=3$ |
| .5(2) | L-9906.2 floor $x_{\min} \ge 7$ | **HOLDS-VERBATIM** (as $\ge 7$) | but only $B=7$ is provable at $a=5$; $B=13$ is empirical because orbits rise |
| .6(1–3) | L-9907.1–.4 envelope + threshold | **HOLDS-VERBATIM** | threshold $\gamma_a = \log_a 2$ |
| .6(4) | "typical orbits contract" | **BREAKS-AT-CONSTANT $a = 4$** | $\gamma_a \lessgtr \frac12 \iff a \gtrless 4$; drift $\sqrt a/2$ |
| .6(5) | L-9907.5 glider lemma | **HOLDS-WITH-MODIFIED-CONSTANT** | offset $\theta_a = \frac1{a-2}$; class $n \equiv -\theta_a \bmod 2^j$ |
| .7(2) | L-9902.1/.2 parity bijection | **HOLDS-VERBATIM** | none; needs only $a$ odd |

**(2) Format-driven versus drift-driven, precisely.**

* **Format-driven** (true for *every* odd $a \ge 3$; the proof never uses the value
  $3$): the cycle equation, positivity, the product formula, the approximation
  corollary, the sign/criticality criterion, the parity bijection, L-9906.1's
  elimination template, L-9913.2–.4's squeeze machinery and decision procedures,
  L-9917.1/.2's sorted floor and window, L-9907.1–.4's envelope and threshold. **No
  algebraic identity in the foundations packet knows that $a = 3$.**
* **Drift-driven** (depend on $3 < 4$, i.e. $\log_2 3 < 2$, i.e. $\gamma_3 > 1/2$):
  every *numerical exclusion* in the packet. Concretely: the existence of a verified
  floor $\mathrm{(V}_F)$ at all (hence L-9913's $2966$ and $47468$, and hence
  L-9917's usable floor $B$); L-9906's "no cycle with $m \le 6$"; and the
  phenomenological claim that typical orbits contract.
* **Hidden-constant** (neither, but a porting trap): L-9905.4's $c$-bounds, whose
  general form carries $1/(a-2)$.
* **Diophantine accident** (neither format nor drift): the *sizes* $2966$, $4647$,
  $10781274$, $1936274$, and the identity of $\mathcal E_{a,B}$, which depend on the
  continued fraction of $\alpha_a$ alone.

**(3) The atypicality budget (rigorous version).** By the ported parity bijection
(L-9922.7 row above; proof in the Proof section) the map
$\pi_k : \mathbb{Z}/2^k \to \{0,1\}^k$, $n \mapsto (v_0(n),\dots,v_{k-1}(n))$, is a
bijection for every odd $a \ge 3$ and every $k \ge 1$. Hence for every $\theta \in (0,1)$
$$\#\{r \in \mathbb{Z}/2^k : a_k(r) \ge \theta k\}\big/2^k
  \;=\; 2^{-k}\!\!\sum_{j \ge \lceil\theta k\rceil}\!\binom kj
  \;\le\; 2^{-k(1 - H(\theta))} \quad (\theta \ge \tfrac12),$$
$H$ the binary entropy. By L-9922.6(2) a divergent $T_a$-orbit satisfies
$a_k/k \ge \gamma_a - \delta$ for all large $k$ and every $\delta > 0$. Therefore:

| | $a = 3$ | $a = 5$ |
|---|---|---|
| threshold $\gamma_a$ | $0.6309298 > 1/2$ | $0.4306765 < 1/2$ |
| density of residues mod $2^k$ with $a_k \ge \gamma_a k$, $k=100$ | $3.319\cdot10^{-3}$ | $0.9033$ |
| same, $k = 1000$ | $5.167\cdot10^{-17}$ | $0.999995$ |
| asymptotic rate | $2^{-(1-H(\gamma_3))k} = 2^{-0.0500445\,k}$ | $\to 1$ (rate $0$) |

**Budget statement.** Fix $\delta \in (0, \gamma_3 - \tfrac12)$. If $n$ has a
divergent $T_3$-orbit then, for all $k$ beyond some $k_0(n,\delta)$, $n \bmod 2^k$
lies in a set of density at most $2^{-k(1 - H(\gamma_3 - \delta))}$, and
$1 - H(\gamma_3-\delta) \to 1 - H(\gamma_3) = 0.0500445\ldots$ as $\delta \to 0$.
So any certificate of divergence for a $3x{+}1$ orbit must, at depth $k$, place its
seed inside a set of residues mod $2^k$ of density
$2^{-0.0500445\,k + o(k)}$ — a cost of $0.0500445$ bits per $T$-step, i.e.
$0.0500445/\gamma_3 = 0.0793$ bits per **odd** step, i.e. one bit of specification
per $\approx 20$ $T$-steps, sustained forever. The corresponding requirement at
$a = 5$ costs **nothing**: at $k = 100$ more than $90\%$ of all residues already
satisfy it, and the proportion tends to $1$. *This is the exact sense in which a
$3x{+}1$ divergence certificate must "pay more" than its $5x{+}1$ counterpart, and
the payment is an entropy deficit, not a missing identity.*

**(4) What this does and does not tell us about $a = 3$ — honestly.**

*It does tell us:*
(i) every load-bearing **identity** in the foundations packet is format-driven, so
none of them can be the seed of a proof of the Collatz conjecture, and equally none
of them obstructs a counterexample for format reasons;
(ii) the packet's machinery, run in a universe where cycles genuinely exist, is
**consistent and sharp**: at the correct floors $m^*(F,5)$ equals the true period of
the actual cycles, the sorted-window method never eliminates their length, the sign
criterion classifies them correctly, and the cycle equation reproduces them exactly.
So the objection "these methods would have excluded a genuine counterexample" is
**refuted** for L-9905, L-9913, L-9917 and the sign criterion;
(iii) all the exclusion *strength* at $a = 3$ enters through exactly two doors —
the verified floor $\mathrm{(V}_F)$ (drift) and the continued fraction of $\alpha_a$
(Diophantine accident). A future exclusion that improves on these must widen one of
those two doors, not the algebra.

*It does not tell us:*
(i) anything about whether $T_3$ has a nontrivial cycle or a divergent orbit. Every
$a = 5$ statement above is a statement about $T_5$;
(ii) any transfer principle. "A certificate format that fails at $a = 5$ is dead at
$a = 3$" remains a **heuristic**: a hypothetical $3x{+}1$ counterexample is atypical
in exactly the sense measured in (3), and atypical objects can be easier to certify
(they are more constrained) or harder (they are rarer). Nothing here proves either;
(iii) whether the $a = 5$ cycle list is complete — only that it is complete below
$10^8$.

---

## Definitions

All symbols not defined here are from `NOTATION.md`.

* $T_a$, $S_a$, $a(x)$, $S_a$-cycle, $m$, $a_i$, $A_i$, $K$, $x_{\min}$, $c_a$,
  $\alpha_a = \log_2 a$, $\gamma_a = \log_a 2 = 1/\alpha_a$: as in the Statement.
  The cyclic-index convention $x_{i+m} := x_i$, $a_{i+m} := a_i$ and the anchoring
  (rotation) convention are exactly D-9908's, and $m, K, x_{\min}$ are
  anchor-independent while $c_a$ and the individual $A_i$ are not.
* **Trivial cycle at $a$**: the cycle containing $1$. At $a = 3$ it is the fixed
  point $(1)$; at $a = 5$ it is $\mathcal C_0 = (1 \to 3)$, $m = 2$, $K = 5$.
  "Nontrivial" means "not the cycle containing $1$".
* $f_a(m) := \lceil m\alpha_a\rceil - m\alpha_a = 1 - \{m\alpha_a\}$;
  $\varepsilon(F,a) := 1/(aF\ln 2)$; $\varepsilon_0(F,a) := 1000/(693aF)$;
  $\mathrm{Adm}_{F,a}(m)$; $m^*(F,a)$ — as in L-9922.4.
* $P_{B,a}(m)$, $N_{B,a}(m)$, $D_B(m)$, $W^*_{a,B}(m)$, $R_{a,B}(m)$,
  $\mathrm{Wd}_{a,B}(m)$, $m_0(B,a)$, $\mathcal E_{a,B}$ — as in L-9922.5.
* **Subcritical / supercritical word** (after L-9918.5): a periodic parity word $w$
  with $|w| = K$, $|w|_1 = m$ is *subcritical* if $a^m < 2^K$ and *supercritical* if
  $a^m > 2^K$; equality is impossible for odd $a \ge 3$.
* $H(\theta) := -\theta\log_2\theta - (1-\theta)\log_2(1-\theta)$, binary entropy.
* **Finite verification**: an exhaustive exact computation over an explicitly stated
  finite range. Labelled X-9922.$k$ and never treated as a proof about all cycles.

---

## Motivation

Issue #26 (open, unclaimed; filed by fable-01) proposes $a = 5$ as a **control
universe**: there the two phenomena this project hunts at $a = 3$ — divergent orbits
and nontrivial positive cycles — are real, cycles provably so. Its programme asks for
a *portability matrix*: re-run each repository exclusion with $3$ replaced by $5$ and
end each port in a labelled verdict, so that the project learns which of its
obstacles are consequences of the *format* of the argument (and therefore would also
block a $5x+1$ certificate, where blocking is known to be wrong) and which are
consequences of the *drift* $\log_2 3 < 2$ (and therefore isolate the real obstacle).

This file executes that programme for the five load-bearing foundations lemmas
L-9905, L-9906, L-9907, L-9913, L-9917 (plus L-9902 and L-9918.5(3), the "sign
criticality lemma" the issue names explicitly). Its value to the counterexample
objective is threefold.

1. **A positive control on the exclusion machinery.** L-9913 excludes every cycle
   with $m \le 2965$ and L-9917 excludes $46$ specific lengths. If those methods,
   transported to a universe with *known* cycles, excluded the known cycles, the
   methods would be wrong and the project's cycle-side exclusions would collapse.
   They do not: L-9922.4(3) shows the squeeze is not merely consistent but **sharp**
   — $m^*(F,5)$ hits the true period exactly at every available floor — and
   L-9922.5(3) shows the sorted window never kills the true length. This is the
   strongest available evidence that these are correct tools.
2. **A precise inventory of where "3" is actually used.** L-9922.7(2) lists it: the
   algebra never uses it; the exclusions use it only through the verified floor and
   through the continued fraction of $\log_2 a$. A cycle-synthesis programme (issue
   #9) therefore knows exactly which constraints it must satisfy for format reasons
   (all of L-9922.1–.3, unavoidable) and which are contingent (the floor).
3. **A quantitative atypicality budget** (L-9922.7(3)), which converts the drift
   difference into an exact entropy rate: $0.0500445$ bits per $T$-step. Any
   divergence-certificate format proposed for $a = 3$ can be measured against it.

---

## Proof or construction

Throughout, $a \ge 3$ is an odd integer; $x$ ranges over positive odd integers unless
stated. Two facts are used constantly: (i) $a x + 1$ is even, so $a(x) \ge 1$ and
$S_a(x)$ is a positive odd integer; (ii) $2^{a(x)}S_a(x) = ax + 1$.

### Proof of L-9922.1 (cycle equation)

Write the step relation at each index (cyclically extended, so it holds for every
integer $i$, with $x_{m+1} = x_1$):
$$2^{a_i} x_{i+1} \;=\; a x_i + 1. \tag{$\ast_i$}$$
Multiply $(\ast_i)$ by $a^{m-i} 2^{A_{i-1}}$ and use $A_{i-1} + a_i = A_i$:
$$a^{m-i} 2^{A_i} x_{i+1} \;=\; a^{m-i+1} 2^{A_{i-1}} x_i + a^{m-i} 2^{A_{i-1}}.$$
Sum over $i = 1, \dots, m$. Re-indexing the left side by $j = i+1$ gives
$\sum_{j=2}^{m+1} a^{m-j+1} 2^{A_{j-1}} x_j$, while the first right-hand sum is
$\sum_{i=1}^{m} a^{m-i+1} 2^{A_{i-1}} x_i$; the two agree except for the $j = m+1$
term on the left and the $i = 1$ term on the right. Hence
$$a^{0} 2^{A_m} x_{m+1} - a^{m} 2^{A_0} x_1 \;=\; \sum_{i=1}^m a^{m-i}2^{A_{i-1}},$$
i.e., using $x_{m+1} = x_1$, $A_m = K$, $A_0 = 0$,
$$x_1\left(2^K - a^m\right) \;=\; c_a. \qquad\blacksquare$$
No positivity, no least-periodicity, and no property of $a$ beyond oddness (used only
to guarantee $a_i \ge 1$, and in fact only $a_i \ge 0$ is needed for the algebra) is
used. **Verdict HOLDS-VERBATIM.**

### Proof of L-9922.2

**(1)** Each summand $a^{m-i}2^{A_{i-1}}$ is a positive integer, so $c_a \ge m \ge 1$.
By L-9922.1 and $x_1 > 0$, $2^K - a^m = c_a/x_1 > 0$; being an integer it is $\ge 1$.
Taking $\log_2$: $K > m\log_2 a$. $\blacksquare$

**(2)** From $(\ast_i)$, $2^{a_i} = \dfrac{a x_i + 1}{x_{i+1}} = \dfrac{x_i}{x_{i+1}}
\left(a + \dfrac1{x_i}\right)$. Multiplying over $i = 1,\dots,m$ and using
$\prod_i x_i/x_{i+1} = 1$ (cyclicity) gives $2^K = \prod_i (a + 1/x_i)$. Since each
factor lies in $(a, a + 1/x_{\min}]$ and there are $m$ of them,
$a^m < 2^K \le (a + 1/x_{\min})^m$. $\blacksquare$

**(3)** $A_{i-1} = a_1 + \dots + a_{i-1} \ge i-1$ (each $a_j \ge 1$), and
$A_{i-1} = K - (a_i + \dots + a_m) \le K - (m-i+1)$. Since $a > 2$,
$$\sum_{i=1}^m a^{m-i}2^{i-1} \;=\; a^{m-1}\sum_{i=1}^m\left(\frac2a\right)^{i-1}
  \;=\; a^{m-1}\cdot\frac{1 - (2/a)^m}{1 - 2/a} \;=\; \frac{a^m - 2^m}{a-2},$$
which gives the lower bound, and multiplying the same sum by $2^{K-m}$ gives the
upper bound. For the anchored refinement use $A_0 = 0$ exactly for $i = 1$ and the
upper estimate for $i \ge 2$:
$$c_a \le a^{m-1} + 2^{K-m}\left(\frac{a^m-2^m}{a-2} - a^{m-1}\right)
      = a^{m-1} + 2^{K-m}\,\frac{a^m - 2^m - (a-2)a^{m-1}}{a-2}
      = a^{m-1} + 2^{K-m}\,\frac{2a^{m-1}-2^m}{a-2},$$
using $a^m - (a-2)a^{m-1} = 2a^{m-1}$. Dividing by $2^K - a^m > 0$ and applying
L-9922.1 at each anchor gives the element bounds. At $a = 3$ the divisor is $1$ and
all four displays reduce to L-9905.4 verbatim. **Verdict
HOLDS-WITH-MODIFIED-CONSTANT $1/(a-2)$.** $\blacksquare$

**(4)** If $m = 1$ then $c_a = a^0 2^{A_0} = 1$ and L-9922.1 reads
$x_1(2^K - a) = 1$, forcing $x_1 = 1$ and $2^K = a + 1$. Conversely if $a = 2^K - 1$
then $a\cdot 1 + 1 = 2^K$, so $S_a(1) = 1$. $\blacksquare$

### Proof of L-9922.3

**(1)** Take $\log_2$ in L-9922.2(2): $m\alpha_a < K \le m\log_2(a + 1/x_{\min})
= m\bigl(\alpha_a + \log_2(1 + \tfrac1{a x_{\min}})\bigr)$. Divide by $m$ and use
$\ln(1+t) \le t$ for $t \ge 0$ with $t = 1/(a x_{\min})$, converting to base $2$ by
dividing by $\ln 2$. $\blacksquare$

**(2)** Let $w \in \{0,1\}^K$ be the parity word of one period of the cycle read along
the $T_a$-orbit starting at $x_1$. The positions of the $1$s in $w$ are exactly
$A_0 < A_1 < \dots < A_{m-1}$ (the $i$-th odd step occurs after $A_{i-1}$ $T_a$-steps),
and the number of $1$s strictly to the right of position $A_{i-1}$ is $m - i$.
Unfolding the recursion $\kappa_{wb} = a^b\kappa_w + b\,2^{|w|}$ from
$\kappa_\varnothing = 0$ gives
$$\kappa_w \;=\; \sum_{j\,:\,w_j = 1} a^{\#\{j' > j\,:\,w_{j'}=1\}}\,2^{\,j}
  \;=\; \sum_{i=1}^m a^{\,m-i}2^{\,A_{i-1}} \;=\; c_a .$$
Also, unfolding $(\ast_i)$ over one period expresses $T_a^K$ on the cylinder of $w$ as
the affine map $x \mapsto (a^m x + \kappa_w)/2^K$, whose unique fixed point in
$\mathbb{Z}_2 \cap \mathbb{Q}$ is $z_w = \kappa_w/(2^K - a^m)$ — well defined because
$2^K - a^m \ne 0$ ($a^m$ is odd $>1$, $2^K$ is even) and $\gcd(2^K - a^m, 2) = 1$.
By L-9922.1, $z_w = x_1$. The sign statement is immediate from $\kappa_w \ge 0$; and
$a^m < 2^K \iff m \ln a < K \ln 2 \iff m/K < \ln 2/\ln a = \gamma_a$. $\blacksquare$

**(3)** Direct computation on the three $a = 5$ cycles; see the table in the Statement
and Adversarial test T1, where $\kappa_w$ is recomputed from the recursion
independently of $c_a$ and the two agree in all three cases. $\blacksquare$

**(4)** $\gamma_a < 1/2 \iff \ln 2/\ln a < 1/2 \iff \ln a > 2\ln 2 \iff a > 4$. For
odd $a$ this reads $a = 3$ versus $a \ge 5$. The geometric-mean multiplier of a
density-$\theta$ word is $2^{\theta\alpha_a - 1}$, equal to $\sqrt a/2$ at
$\theta = 1/2$. $\blacksquare$

### Proof of L-9922.4

**(1)** If $\alpha_a = p/q$ with $p, q \in \mathbb{Z}^+$ then $2^p = a^q$, contradicting
unique factorisation ($a$ odd $\ge 3$). Hence $m\alpha_a \notin \mathbb{Z}$ and
$f_a(m) = \lceil m\alpha_a\rceil - m\alpha_a \in (0,1)$.

**(2)** By L-9922.3(1) with $x_{\min} \ge F$,
$$0 < K - m\alpha_a \le \frac{m}{a\,x_{\min}\ln 2} \le \frac{m}{aF\ln 2}
  = \varepsilon(F,a)\,m < \varepsilon_0(F,a)\,m,$$
the last step because $\ln 2 > 693/1000$. *Exact certificate* (independent of
L-9913's Corollary A1, which states the same inequality): all terms of
$\ln 2 = 2\,\mathrm{artanh}(1/3) = 2\sum_{k\ge0}\frac{1}{(2k+1)3^{2k+1}}$ are
positive, so truncating after four terms gives
$$\ln 2 \;>\; 2\left(\frac13+\frac1{81}+\frac1{1215}+\frac1{15309}\right)
   \;=\; \frac{53056}{76545} \;>\; \frac{693}{1000},$$
the last inequality being the integer comparison
$53056 \cdot 1000 = 53\,056\,000 > 53\,045\,685 = 693 \cdot 76545$. (Re-verified in
Test T2 by an independent certified rational $\mathrm{artanh}$ enclosure.)
Since $K \in \mathbb{Z}$ and $K > m\alpha_a$,
$K \ge \lceil m\alpha_a\rceil$, so
$$f_a(m) = \lceil m\alpha_a\rceil - m\alpha_a \le K - m\alpha_a < \varepsilon_0(F,a)m,$$
i.e. $\mathrm{Adm}_{F,a}(m)$, whence $m \ge m^*(F,a)$ by minimality.
For the reduced denominator, write $K/m = p/q$ in lowest terms, $m = tq$, $K = tp$.
Then $p - q\alpha_a = (K - m\alpha_a)/t \le \varepsilon_0 m/t = \varepsilon_0 q$, and
$p > q\alpha_a$, so $\lceil q\alpha_a\rceil \le p$ and
$f_a(q) \le p - q\alpha_a \le \varepsilon_0 q$: $\mathrm{Adm}_{F,a}(q)$.
Upward closure: if $f_a(q) \le \varepsilon_0 q$ then, with $P := \lceil q\alpha_a\rceil$,
$tP - tq\alpha_a \le t\varepsilon_0 q = \varepsilon_0(tq)$ and $tP \ge \lceil
tq\alpha_a\rceil$, so $f_a(tq) \le \varepsilon_0 (tq)$. $\blacksquare$

**(3),(4),(6)** are exact computations (Tests T2, T4, T8); the decision procedure is
L-9913.4(2) with a certified enclosure $L < \alpha_a < U$: from
$K - m\alpha_a \le \varepsilon_0 m \iff \frac Km - \varepsilon_0 \le \alpha_a$, put
$r := K/m - \varepsilon_0 \in \mathbb{Q}$; then $L \ge r \Rightarrow$ admissible and
$U \le r \Rightarrow$ not admissible, each a single cross-multiplication of integers.
The enclosures are produced by an exact-rational $\mathrm{artanh}$ series with an
explicit tail bound (Test T2) and are cross-checked against L-9913.4(4)'s certified
bracket $\frac{176251}{111202} < \log_2 3 < \frac{301994}{190537}$ and against
big-integer certificates $2^{4268621} < 5^{1838395}$, $2^{4495889} > 5^{1936274}$ for
$\log_2 5$. At the small $a = 5$ floors no enclosure is needed at all: the pure
integer form L-9913.4(1), $\mathrm{Adm}_{F,a}(m) \iff 2^{QK-Pm} \le a^{Qm}$, has
sides of only $\sim 1.4\cdot10^4$ bits and is executed directly (Test T4).

**(5)** is a statement about the availability of $\mathrm{(V}_F)$, discharged by
X-9922.0(a): $13$ lies on $\mathcal C_1 \ne \mathcal C_0$, so for every $F \ge 13$ the
hypothesis "every $n \le F$ reaches the cycle through $1$" is **false** at $a = 5$.
The heuristic mechanism (why exhaustive small-$n$ verification succeeds at $a=3$ and
cannot at $a=5$) is L-9922.6(4); only the failure itself is proved. $\blacksquare$

### Proof of L-9922.5

**(1)** Least-periodicity makes $x_1,\dots,x_m$ pairwise distinct; they are positive
odd and $\ge B$, so the increasing rearrangement satisfies $x_{(j)} \ge B + 2j$
(induction: $x_{(0)} \ge B$, and $x_{(j)} > x_{(j-1)} \ge B + 2(j-1)$ with both odd
forces $x_{(j)} \ge B + 2j$). Since $t \mapsto a + 1/t$ is decreasing,
$$2^K = \prod_{i=1}^m\left(a + \frac1{x_i}\right)
      = \prod_{j=0}^{m-1}\left(a + \frac1{x_{(j)}}\right)
      \le \prod_{j=0}^{m-1}\left(a + \frac1{B+2j}\right) = P_{B,a}(m),$$
and $2^K > a^m$ is L-9922.2(1); so $K \in W^*_{a,B}(m)$, which is empty exactly when
$m \in \mathcal E_{a,B}$. $\blacksquare$

**(2)** $S_5(1) = 3$, $S_5(3) = 1$, so $\{1,3\} = \mathcal C_0$ is a cycle and any
$S_5$-cycle containing $1$ or $3$ equals $\mathcal C_0$. $S_5(5) = 26/2 = 13$, and
$13 \to 33 \to 83 \to 13$; so the $S_5$-orbit of $5$ is eventually periodic with
periodic part $\mathcal C_1 \not\ni 5$, whence $5$ is not periodic. Therefore every
$S_5$-cycle other than $\mathcal C_0$ has all elements $\ge 7$. (This is L-9906.2's
argument verbatim; at $a = 3$ it reads $S(3) = 5$, $S(5) = 1$.) That $B = 13$ is only
empirical is the negative statement that the same argument does not terminate for
$7, 9, 11$: their orbits neither return nor meet a known cycle within the verified
depth. $\blacksquare$

**(3)** Exact integer computation; the certificate for $m \in \mathcal E_{a,B}$ is the
pair $2^{\kappa(m)-1} \le a^m$ and $2^{\kappa(m)}D_B(m) > N_{B,a}(m)$ with
$\kappa(m) := \mathrm{bitlength}(a^m)$, exactly as in L-9917.3, since
$K \mapsto 2^K D_B(m)$ is increasing. (Test T5.) $\blacksquare$

**(4)** $\ln R_{a,B}(m) = \sum_{j=0}^{m-1}\ln\!\left(1 + \frac1{a(B+2j)}\right)$. Using
$t - t^2/2 < \ln(1+t) < t$ and comparing $\sum_{j<m}\frac1{a(B+2j)}$ with
$\int_0^m \frac{ds}{a(B+2s)} = \frac1{2a}\ln\frac{B+2m}{B}$ gives
$\ln R_{a,B}(m) = \frac1{2a}\ln\frac{B+2m}{B} + O(1)$ with $O(1)$ bounded by
$\frac1{aB}$ in absolute value; hence $\mathrm{Wd}_{a,B}(m) = \frac1{2a}\log_2 m + O(1)$
(at $a = 3, B = 7$ this is L-9917.4(2)'s envelope). Setting $\ln R = \ln 2$ gives
$\frac1{2a}\ln(1 + 2m/B) \approx \ln 2$, i.e. $1 + 2m_0/B \approx 2^{2a}$, i.e.
$m_0(B,a)/B \to (2^{2a}-1)/2$; the limit statement is a REMARK (as in L-9917.4(6))
and no proof below uses it — the tabulated $m_0$ values are exact computations.
$\blacksquare$

**(5)** X-9922.0(a) exhibits two $S_5$-cycles with $m = 3 \le 6$. $\blacksquare$

### Proof of L-9922.6

**(1)** Induction on $k$. $T_a^{k+1}(n) = T_a^k(n)/2$ if $T_a^k(n)$ is even (and then
$a_{k+1} = a_k$), and $= (aT_a^k(n)+1)/2 \ge a T_a^k(n)/2$ if odd (and then
$a_{k+1} = a_k + 1$); in both cases the claimed inequality propagates, with equality
iff no odd step has occurred. The two corollaries follow by taking $\log_2$:
$\log_2 T_a^k(n) \ge \log_2 n + k\left(\frac{a_k}{k}\alpha_a - 1\right)$, and
$\frac{a_k}k\alpha_a - 1 > 0 \iff \frac{a_k}k > \gamma_a$.

**(2)** Exactly one $T_a$-step is taken per index, so
$$\log_2 T_a^k(n) \;=\; \log_2 n + a_k\alpha_a - k + E_k,
\qquad E_k := \sum_{i<k,\ v_i = 1}\log_2\!\left(1 + \frac1{a\,T_a^i(n)}\right) \ge 0,$$
(an exact identity, obtained by taking $\log_2$ of the two branch formulas). Assume
$T_a^k(n) \to \infty$ and let $\delta \in (0,1)$. Choose $X$ with
$\log_2(1 + \frac1{aX}) \le \delta$ and $t_0$ with $T_a^i(n) \ge X$ for $i \ge t_0$;
then $E_k \le C_0 + \delta a_k$ where $C_0 := \sum_{i<t_0}\log_2(1+\frac1{a}) \le
t_0\log_2\frac{a+1}a$ is a constant depending only on $(\delta, n, a)$. Since
$\log_2 T_a^k(n) \ge 0$,
$$0 \;\le\; \log_2 n + a_k\alpha_a - k + C_0 + \delta a_k
  \;\Longrightarrow\; a_k(\alpha_a + \delta) \;\ge\; k - \log_2 n - C_0 ,$$
so $\liminf_k a_k/k \ge 1/(\alpha_a + \delta)$ for every $\delta > 0$, i.e.
$\liminf_k a_k/k \ge 1/\alpha_a = \gamma_a$. The only property of $a$ used is
$\log_2(1 + \frac1{ax}) \to 0$ as $x \to \infty$. $\blacksquare$

**(3)** If the orbit does not tend to $\infty$, some bound $B$ is attained infinitely
often; $\{1,\dots,B\}$ is finite, so some value repeats, and determinism makes the
orbit eventually periodic, hence bounded. $\blacksquare$

**(5)** $a - 2$ is odd, hence invertible in $\mathbb{Z}/2^j$, so $\theta_a = 1/(a-2)$
makes sense $2$-adically. For $n$ odd, $T_a(n) + \theta_a = \frac{an+1}2 +
\frac1{a-2} = \frac{a(a-2)n + (a-2) + 2}{2(a-2)} = \frac a2\left(n + \theta_a\right)$.
Hence, by induction, if the first $j$ steps are all odd then
$T_a^j(n) + \theta_a = (a/2)^j(n + \theta_a)$, i.e.
$$(a-2)\,T_a^j(n) + 1 \;=\; \frac{a^{\,j}\bigl((a-2)n+1\bigr)}{2^{\,j}} . \tag{$\dagger$}$$
For the equivalence, put $u_i := (a-2)T_a^i(n) + 1$; since $a-2$ is odd,
$T_a^i(n)$ is odd $\iff u_i$ is even. Induction on $i$ using $(\dagger)$ at each
stage: as long as the steps taken so far are all odd, $u_i = a^{i}u_0/2^{i}$, which
is an integer exactly while $2^{i} \mid u_0$ (as $a$ is odd), and it is even exactly
while $2^{i+1} \mid u_0$. Hence $v_0 = \dots = v_{j-1} = 1 \iff 2^{j} \mid u_0 =
(a-2)n+1 \iff n \equiv -(a-2)^{-1} = -\theta_a \pmod {2^{j}}$. Finally
$T_a^j(n) = (a/2)^j(n + \theta_a) - \theta_a > (a/2)^j n$ because
$(a/2)^j\theta_a > \theta_a$ for $j \ge 1$, $a > 2$. At $a = 3$: $\theta_3 = 1$,
recovering L-9907.5. (Verified for $a = 3,5,7$, all $j \le 14$, in Test T7/drift.)
$\blacksquare$

### Proof of L-9922.7(3) (the ported parity bijection and the budget)

*Parity bijection.* For odd $a$ and $j \ge 1$, $m \in \mathbb{Z}$,
$T_a(n + 2^j m) = T_a(n) + a^{v_0(n)}2^{j-1}m$ and $v_0(n + 2^jm) = v_0(n)$ (the two
branch formulas are affine with slopes $1/2$ and $a/2$); iterating,
$T_a^i(n + 2^km) = T_a^i(n) + a^{a_i(n)}2^{k-i}m$ for $i \le k$, so the length-$k$
parity word depends only on $n \bmod 2^k$, and $\pi_k$ is well defined. It is
injective (hence bijective, both sides having $2^k$ elements) by the two-lifts
argument: $T_a^k(n + 2^k) = T_a^k(n) + a^{a_k(n)}$ and $a^{a_k(n)}$ is **odd**, so
the two lifts of a class mod $2^k$ receive different $k$-th bits; induction on $k$
gives injectivity. The only property of $a$ used is oddness. (Verified for
$a = 3,5,7$ and all $k \le 14$ in Test T7.)

*Budget.* By the bijection, for any $\theta$,
$\#\{r \bmod 2^k : a_k(r) \ge \theta k\} = \#\{w \in \{0,1\}^k : |w|_1 \ge \theta k\}
= \sum_{j\ge\lceil\theta k\rceil}\binom kj$, and the Chernoff/entropy bound
$2^{-k}\sum_{j \ge \theta k}\binom kj \le 2^{-k(1-H(\theta))}$ holds for
$\theta \ge 1/2$. With $\theta = \gamma_3 = 0.6309298\ldots$,
$H(\gamma_3) = 0.9499555\ldots$ and the rate is $1 - H(\gamma_3) = 0.0500445\ldots$;
with $\theta = \gamma_5 < 1/2$ the tail contains the central binomial mass, so the
density tends to $1$ (computed values in the table). Combining with L-9922.6(2) —
divergence forces $a_k/k \ge \gamma_a - \delta$ eventually — gives the budget
statement. $\blacksquare$

---

## Dependency audit

| used | where | how |
|---|---|---|
| NOTATION.md D-9902, D-9904, D-9905, D-9906, D-9908 | throughout | notation for $T$, $S$, cycles, parity vectors; the $a$-generalisations are defined explicitly in the Statement |
| L-9905.1–.6 (PROVED) | L-9922.1, .2, .3(1) | **port targets.** Every ported statement is proved here from scratch (Proof section); L-9905 is used only as the $a=3$ specialisation to be reproduced. The a=3 reductions are verified in Tests T3, T8. |
| L-9906.1–.3 (PROVED) | L-9922.2(4), .5(2), .5(5) | port targets; L-9906.2's argument is re-run at $a=5$ inline (Proof of L-9922.5(2)) |
| L-9907.1–.5 (PROVED) | L-9922.6 | port target; all five proofs re-given inline |
| L-9913.2–.6, .9 (PROVED) | L-9922.4 | port target; the squeeze, the decision procedure L-9913.4(2)/(4) and the values $2966$, $10946$, $15601$, $47468$ are reproduced independently (Test T2) as the mandatory consistency gate |
| L-9913 Corollary A1 ($\ln 2 > 693/1000$) | L-9922.4(2) | to justify $\varepsilon_0 > \varepsilon$; independently re-verified by a certified rational $\mathrm{artanh}$ enclosure in Test T2 |
| L-9917.1–.4 (PROVED) | L-9922.5 | port target; the $46$-element set, $\max = 171$, $m_0 = 196$ and all eight $m_0(B,3)$ values reproduced independently (Test T5) |
| L-9902.1–.2 (PROVED) | L-9922.7(3) | port target; the ported proof is given inline, so no status inherited |
| L-9918.5(3) (PROPOSED) | L-9922.3(2), (3) | **the object issue #26 asks about.** NOT load-bearing: $\kappa_w = c_a$ and $z_w = c_a/(2^K-a^m)$ are re-derived here from L-9922.1. Nothing in this file inherits L-9918's PROPOSED status. |
| L-9909's X-9901 ($n \le 10^6$ reaches $1$ under $C$) | L-9922.4(4), column "$\mathrm{(V}_F)$ available" | only to record which $a=3$ floors are verified in-repo; no proof step uses it |

**Circularity check.** No statement of this file is used to prove any other statement
of this file except: L-9922.2(1),(2) $\Rightarrow$ L-9922.3(1) $\Rightarrow$
L-9922.4(2); L-9922.2(2) $\Rightarrow$ L-9922.5(1); L-9922.1 $\Rightarrow$
L-9922.3(2). This order is acyclic. No $a = 3$ result is used to prove an $a = 5$
result or vice versa.

---

## Gap audit

* **Hidden finiteness assumptions.** X-9922.0(b) is finite: "the only $S_5$-cycles
  with all elements $< 10^8$". It is labelled as such everywhere and is never used to
  claim that $\mathcal C_0,\mathcal C_1,\mathcal C_2$ are *all* $T_5$-cycles. The
  floor $B = 13$ at $a = 5$ inherits this finiteness and is labelled EMPIRICAL; every
  statement resting on it (the $B = 13$ row of L-9922.5(3), the $F = 13$ row of
  L-9922.4) is separated from the $B = 7$ / $F = 1$ rows, which are proved.
* **Finite computation extrapolated to infinite behaviour.** The drift ledger (T10)
  shows every prefix of the $T_5$-orbit of $7$ up to $k = 2\cdot10^5$ is
  supercritical. This is **not** a divergence proof and is nowhere used as one; issue
  #26's stage (2) remains open. It is reported as a finite verification only.
* **Confusion between empirical and universal statements.** The $a = 5$ rows of the
  $m^*$ table at $F \ge 10^6$ are flagged explicitly as arithmetic under a **false**
  hypothesis. They are not claims about $T_5$-cycles.
* **Boundary cases.** $m = 1$ is treated separately (L-9922.2(4)) precisely because it
  is where the $a=3$ statement fails to port. $m = 2$ is the trivial case at $a = 5$
  and is checked at the universal floor $B = 1$, $F = 1$ (where it is *not*
  eliminated) as well as at higher floors (where it is eliminated, correctly, since
  $\mathcal C_0$ violates those floors). The empty-product convention makes
  $P_{B,a}(0) = 1$; all indices are checked at $m = 1$.
* **Nonuniform estimates.** The bound of L-9922.3(1) is uniform in $m$ and depends on
  the cycle only through $x_{\min}$; the constant $C_0$ in the proof of L-9922.6(2)
  depends on $(\delta, n, a)$ and is explicitly quantified as such — no interchange of
  $\lim$ and $\sup$ is performed.
* **Assumptions equivalent to the conjecture.** $\mathrm{(V}_F)$ is a finite
  verification, not a conjecture; it is used only in the $a = 3$ column and is
  attributed to X-9901/X-9913. The file proves nothing about $a = 3$ dynamics.
* **Invalid induction.** The three inductions (telescoping in L-9922.1, the sorted
  floor in L-9922.5(1), the two-lifts argument in L-9922.7(3)) each have explicit base
  cases; the sorted-floor induction uses distinctness *and* oddness, both of which are
  hypotheses.
* **Incorrectly assumed independence.** The atypicality budget's independence claim is
  **not** an assumption: it is L-9902.3(ii) ported, i.e. an exact consequence of the
  bijection $\pi_k$, so the binomial counts are exact, not heuristic. What remains
  heuristic is only the *interpretation* ("a certificate must pay this"), and it is
  labelled as such.
* **Symbolic object $\to$ actual integer.** Every $a=5$ cycle element quoted is an
  explicit positive integer, verified by exact iteration of $T_5$ (T1); the sign
  criterion's realiser $z_w$ is checked to be an integer, not merely a $2$-adic
  rational, in each case (and the supercritical example $-7/17$ is exhibited as a
  non-integer, showing the check is not vacuous).
* **Where the port might still be wrong.** The one asymmetry I could not remove: at
  $a = 5$ the "nontrivial" floor $B = 13$ is empirical, so the $B = 13$ elimination
  set ($887$ lengths) is an empirically-conditioned statement. The $B = 7$ row is
  unconditional.

---

## Adversarial tests

All scripts are exact-integer / exact-rational; no floating point enters any
decision. Scripts live in
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/`
(`t5_cycles.py`, `squeeze.py`, `certificates.py`, `sorted_window.py`,
`cbounds_budget.py`, `checks.py`). Output below is **captured from the actual runs**;
long lists are elided with `...` and a few repetitive multi-line blocks are condensed
onto one line, but no value has been altered, rounded or reconstructed by hand.
Annotations added by the author appear outside the fenced blocks.

### T1 — exhaustive $S_5$-cycle search and every ported identity, per cycle

```python
def all_cycles_below(a, N):
    """Every S_a-cycle all of whose (odd) elements are < N, via the restricted
    functional graph of S_a on odd integers < N (three-colour path walk)."""
    n_odd = (N + 1) // 2
    state = bytearray(n_odd)                 # 0 unseen, 1 on current path, 2 done
    idx = lambda x: (x - 1) // 2
    cycles = []
    for start in range(1, N, 2):
        if state[idx(start)]: continue
        path, x = [], start
        while True:
            if x >= N: break
            i = idx(x)
            if state[i] == 2: break
            if state[i] == 1:
                cycles.append(path[path.index(x):]); break
            state[i] = 1; path.append(x); x = S(a, x)
        for y in path: state[idx(y)] = 2
    return cycles
```

```text
=== a = 5:  all S_5-cycles with every odd element < 1000000 ===

  cycle (Syracuse form, anchored at x_min): [1, 3]
    m = 2, exponents a_i = [1, 4], A = [0, 1, 5], K = 5, c_5 = 7, x_min = 1
    2^K - 5^m = 7;  x_1*(2^K-5^m) = 7 ; c = 7
    full T_5-cycle (5 elements): [1, 3, 8, 4, 2]
    word w = 11000  (|w|=K=5, |w|_1=m=2)
    A_w = 5^2 = 25   M^p = 2^5 = 32   kappa_w = 7
    anchored c values (one per rotation): [7, 21]
    checks: 13 run, failures: NONE
    approx: K/m = 5/2 = 2.500000000, log2 5 = 2.321928095, excess = 0.178071905, bound 1/(5*x_min*ln2) = 0.288539008
    approx: m/K = 0.400000000  vs  gamma_5 = log_5 2 = 0.430676558  -> SUBcritical

  cycle (Syracuse form, anchored at x_min): [13, 33, 83]
    m = 3, exponents a_i = [1, 1, 5], A = [0, 1, 2, 7], K = 7, c_5 = 39, x_min = 13
    2^K - 5^m = 3;  x_1*(2^K-5^m) = 39 ; c = 39
    full T_5-cycle (7 elements): [13, 33, 83, 208, 104, 52, 26]
    word w = 1110000  (|w|=K=7, |w|_1=m=3)
    A_w = 5^3 = 125   M^p = 2^7 = 128   kappa_w = 39
    anchored c values (one per rotation): [39, 99, 249]
    checks: 14 run, failures: NONE
    approx: K/m = 7/3 = 2.333333333, log2 5 = 2.321928095, excess = 0.011405238, bound 1/(5*x_min*ln2) = 0.022195308
    approx: m/K = 0.428571429  vs  gamma_5 = log_5 2 = 0.430676558  -> SUBcritical

  cycle (Syracuse form, anchored at x_min): [17, 43, 27]
    m = 3, exponents a_i = [1, 3, 3], A = [0, 1, 4, 7], K = 7, c_5 = 51, x_min = 17
    2^K - 5^m = 3;  x_1*(2^K-5^m) = 51 ; c = 51
    full T_5-cycle (7 elements): [17, 43, 108, 54, 27, 68, 34]
    word w = 1100100  (|w|=K=7, |w|_1=m=3)
    A_w = 5^3 = 125   M^p = 2^7 = 128   kappa_w = 51
    anchored c values (one per rotation): [51, 129, 81]
    checks: 14 run, failures: NONE
    approx: K/m = 7/3 = 2.333333333, log2 5 = 2.321928095, excess = 0.011405238, bound 1/(5*x_min*ln2) = 0.016972883
    approx: m/K = 0.428571429  vs  gamma_5 = log_5 2 = 0.430676558  -> SUBcritical

  total cycles found: 3;  all identity checks pass: True

=== a = 3:  all S_3-cycles with every odd element < 1000000 ===
  cycle (Syracuse form, anchored at x_min): [1]
    m = 1, exponents a_i = [2], A = [0, 2], K = 2, c_3 = 1, x_min = 1
    ... checks: 12 run, failures: NONE
  total cycles found: 1;  all identity checks pass: True
```

The $14$ per-cycle checks are: the cycle equation at *every* anchor (rotation);
$c_a \ge m$; positivity; the product formula as an exact rational identity;
$2^K \le (a + 1/x_{\min})^m$; $\kappa_w = c_a$ from the independent E2 recursion;
subcriticality; $\kappa_w > 0$; $(2^K - a^m) \mid \kappa_w$; realiser $= x_1$; and
odd-density $< \gamma_a$. Extending the search: `10000000 3 [1, 13, 17]` and
`100000000 3 [1, 13, 17]` — no further cycles below $10^8$.

### T2 — the ported squeeze; MANDATORY $a = 3$ consistency gate

```python
def eps0(F, a):                    # at a = 3 this is L-9913's 1000/(2079 F)
    return Fraction(1000, 693 * a * F)

def adm(alpha, m, P, Q):
    K = alpha.ceil_m_alpha(m)                       # exact ceil(m log2 a)
    return alpha.leq_alpha(K * Q - P * m, m * Q), K  # (KQ-Pm)/(mQ) <= log2 a ?
```
(`Alpha` holds a certified rational enclosure $L < \log_2 a < U$ of width $2^{-256}$,
built from an exact-rational $\mathrm{artanh}$ series with explicit tail bound;
`ceil_m_alpha` and `leq_alpha` raise rather than guess if the enclosure cannot decide.)

```text
log2(3) enclosure width = 2^-256; float check: ... : True
log2(5) enclosure width = 2^-256; float check: ... : True
L-9913.4(4) certified bracket contains our enclosure: True  and the big-integer certificates hold: True True

--- gate 1 (MANDATORY): a = 3 must reproduce L-9913 exactly ---
  F = 10^6: m*(F,3) = 2966 (expect 2966: OK), K* = 4701, gcd = 1, last failure m = 2965
  F = 10^7: m*(F,3) = 10946 (expect 10946: OK), K* = 17349, gcd = 1, last failure m = 10945
  F = 10^8: m*(F,3) = 15601 (expect 15601: OK), K* = 24727, gcd = 1, last failure m = 15600
  F = 10^9: m*(F,3) = 47468 (expect 47468: OK), K* = 75235, gcd = 1, last failure m = 47467

--- a = 5 at the floors that are ACTUALLY true for a = 5 ---
  F =  1: eps0 = 200/693, m*(F,5) = 2, K* = 5, last failure m = 1
  F =  4: eps0 = 50/693, m*(F,5) = 3, K* = 7, last failure m = 2
  F =  6: eps0 = 100/2079, m*(F,5) = 3, K* = 7, last failure m = 2
  F = 12: eps0 = 50/2079, m*(F,5) = 3, K* = 7, last failure m = 2

--- a = 5 at the (hypothetical for a=5) floors of L-9913 ---
  F = 10^6: m*(F,5) = 4647, K* = 10790, gcd = 1, last failure m = 4646
  F = 10^7: m*(F,5) = 8651, K* = 20087, gcd = 1, last failure m = 8650
  F = 10^8: m*(F,5) = 21306, K* = 49471, gcd = 1, last failure m = 21305
  F = 10^9: m*(F,5) = 97879, K* = 227268, gcd = 1, last failure m = 97878
  F = 10^12: m*(F,5) = 1936274, K* = 4495889, gcd = 1, last failure m = 1936273

--- a = 3 at F = 10^12 (new value, for the comparison table) ---
  m*(10^12,3) = 10781274, K* = 17087915, gcd = 1, last failure m = 10781273
```

### T3 — the $(a-2)$ trap in L-9905.4, and $m = 1$

```text
=== (A) ported c-bounds, checked on every known cycle (exact) ===
  a=5 cycle[1, 3] anchor x1=  1: m=2, K=5, c=7; [7 <= c]:True  [c <= 56]:True  [c <= refined 21]:True  || naive (a-2)-free lower bound 21 <= c ? False
  a=5 cycle[13, 33, 83] anchor x1= 13: m=3, K=7, c=39; [39 <= c]:True  [c <= 624]:True  [c <= refined 249]:True  || naive (a-2)-free lower bound 117 <= c ? False
  a=5 cycle[13, 33, 83] anchor x1= 83: m=3, K=7, c=249; [39 <= c]:True  [c <= 624]:True  [c <= refined 249]:True  || naive (a-2)-free lower bound 117 <= c ? True
    element bounds: 13 <= x <= 208 ; actual min 13, max 83; sharp-low:True, max <= hi:True
  a=5 cycle[17, 27, 43] anchor x1= 17: m=3, K=7, c=51; [39 <= c]:True  [c <= 624]:True  [c <= refined 249]:True  || naive (a-2)-free lower bound 117 <= c ? False
  a=3 cycle[1] anchor x1=  1: m=1, K=2, c=1; [1 <= c]:True  [c <= 2]:True  [c <= refined 1]:True  || naive (a-2)-free lower bound 1 <= c ? True

=== L-9905.6 port: which a admit an m = 1 cycle? x(2^K - a) = 1 ===
  a = 3: 2^K = a+1 = 4, K = 2, x = 1 IS a fixed point of S_a
  a = 7: 2^K = a+1 = 8, K = 3, x = 1 IS a fixed point of S_a
  a = 15, 31, 63: likewise
  a = 5: a+1 = 6 is not a power of 2  ->  S_5 has NO fixed point; the cycle through 1 is {1,3}, m = 2, K = 5.
```

The naive $a=3$-shaped lower bound **fails** at $a=5$ on $4$ of the $8$ anchorings
tested; the $(a-2)$-corrected bound holds on all $8$, with equality at the anchor
whose exponent word is $(1,1,\dots,1,K-m+1)$ (lower) and $(K-m+1,1,\dots,1)$
(refined upper). The refined upper bound is *attained*: $c = 249$ at anchor $83$, and
the element bound $249/3 = 83$ equals $\max \mathcal C_1$.

### T4 — pure-integer certificates (no enclosure) at the true $a=5$ floors

```text
=== (1) pure-integer certificates at the true a = 5 floors ===
  F = 12, eps0 = 50/2079  (P = 50, Q = 2079)
    m = 1: K = ceil(m log2 5) = 3;  2^6187 <= 5^2079 ?  False   (excluded)   [sides ~6187 and ~4827 bits]
    m = 2: K = ceil(m log2 5) = 5;  2^10295 <= 5^4158 ?  False   (excluded)   [sides ~10295 and ~9654 bits]
    m = 3: K = ceil(m log2 5) = 7;  2^14403 <= 5^6237 ?  True   (ADMISSIBLE)   [sides ~14403 and ~14481 bits]
    m = 4: K = ceil(m log2 5) = 10;  2^20590 <= 5^8316 ?  False   (excluded)   [sides ~20590 and ~19309 bits]
  F = 1, eps0 = 200/693: m = 1 excluded; m = 2 ADMISSIBLE.

=== (2) certified brackets for log2 5 (one big-int comparison each) ===
  cf(log2 5) = [2, 3, 9, 2, 2, 4, 6, 2, 1, 1, 3, 1, 18, 1, 6, 1, 2, 1, 1, 4, 1, 42, 6, 1, 4]
  convergents p/q with 2^p < 5^q (LOWER): ['2/1', '65/28', '339/146', '9297/4004', '29384/12655', '177797/76573', '4268621/1838395']
  convergents p/q with 2^p > 5^q (UPPER): ['7/3', '137/59', '1493/643', '20087/8651', '49471/21306', '227268/97879', '4495889/1936274']
    L0 = 4268621/1838395  certified by 2^4268621 < 5^1838395: True
    U0 = 4495889/1936274  certified by 2^4495889 > 5^1936274: True
    U0 - L0 = 1/3559636440230 = approx 2.809e-13

=== (3) displayed certificates for the headline a = 5 values ===
  F = 10^6 winner   m = 4647, K = 10790: r = K/m - eps0 = 12462448451/5367285000;  L0 >= r: 22910905463985000 vs 22910902920076145 -> True
  F = 10^6 last fail m = 4646, K = 10788: r = 18690207677/8049195000;  U0 <= r: 36188287259355000 vs 36189363179575498 -> True
  F = 10^9 winner   m = 97879, K = 227268: r = 787483619902121/339150735000000;  L0 >= r: 1447705949586435000000 vs 1447705949409959735795 -> True
  F = 10^12 winner  m = 1936274, K = 4495889: r = 7789127692499031863/3354594705000000000;  L0 >= r: 14319493404251805000000000 vs 14319493404251757681779885 -> True

=== (4) true-eps vs rational-majorant eps0 (does the majorant matter?) ===
  a = 3, F = 1000000: m* with TRUE eps = 2966 (with rational majorant eps0: 2966) -> same
  a = 3, F = 1000000000: m* with TRUE eps = 47468 (majorant: 47468) -> same
  a = 5, F = 12: m* with TRUE eps = 3 (majorant: 3) -> same
  a = 5, F = 1000000: m* with TRUE eps = 4647 (majorant: 4647) -> same
  a = 5, F = 1000000000: m* with TRUE eps = 97879 (majorant: 97879) -> same
```
Note $m = 3$ is admissible at $F = 12$ while $m = 4$ is not: $\mathrm{Adm}$ is *not*
monotone in $m$ (only $\mathrm{Adm}(q) \Rightarrow \mathrm{Adm}(tq)$), exactly as at
$a = 3$. Replacing the rational majorant $\varepsilon_0$ by the true
$\varepsilon = 1/(aF\ln2)$ changes no tabulated value.

### T5 — the sorted window; MANDATORY $a = 3$ gate and the $a = 5$ recomputation

```text
=== GATE: a = 3, B = 7 must reproduce L-9917 exactly ===
  E = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48,
       50, 53, 55, 60, 62, 65, 67, 72, 77, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]
  |E| = 46 (expect 46: True), max E = 171 (expect 171: True), m_0 = 196 (expect 196: True)
  m_0(B) for a=3: B=1: 13, B=3: 71, B=5: 133, B=7: 196, B=9: 258, B=27: 825, B=101: 3156
  m_0(1001) for a=3: 31506 (expect 31506)

=== a = 5, floor B = 13 ===
  m_0(13,5) = 6197
  |E_(5,13)| = 887, max = 6079
  IS m = 3 (both known nontrivial cycles) ELIMINATED?  False
  m = 3: a^m = 125, least K with 2^K > a^m is 7, 2^K = 128; N = 431376, D = 3315,
         P = N/D = 130.128507; 2^K*D = 424320 <= N = 431376: True  -> W* = {7} NONEMPTY

  a=5 B=1:  m_0=180,  |E|=23,  maxE=146,  2 in E:False, 3 in E:False, 4 in E:True
  a=5 B=7:  m_0=3134, |E|=446, maxE=3010, 2 in E:True,  3 in E:False, 4 in E:True
  a=5 B=13: m_0=6197, |E|=887, maxE=6079, 2 in E:True,  3 in E:False, 4 in E:True
  a=3 B=7:  m_0=196,  |E|=46,  maxE=171,  2 in E:True,  3 in E:True,  4 in E:True

=== m_0(B,a)/B  ->  (2^(2a)-1)/2  (ported asymptotic) ===
  a = 3: predicted limit 31.5;   B=101: m_0=3156,  ratio 31.25; B=1001: m_0=31506, ratio 31.47
  a = 5: predicted limit 511.5;  B=11:  m_0=5175,  ratio 470.45; B=101: m_0=51202, ratio 506.95
  a = 7: predicted limit 8191.5; B=1:   m_0=2708;  B=11: m_0=82635, ratio 7512.27
```

At the **universal** floor $B = 1$ — the only one applicable to all $S_5$-cycles —
neither $m = 2$ nor $m = 3$ is eliminated, i.e. the ported method spares every known
$a=5$ cycle length. At $B = 7$ (proved) and $B = 13$ (empirical) $m = 3$ still
survives while $m = 2$ is eliminated, which is correct because $\mathcal C_0$ has
$x_{\min} = 1$.

### T6 — independent cycle cross-check (different failure mode)

Period-bounded rather than height-bounded: for every odd $x < 10^5$, iterate $S_5$ up
to $5000$ steps testing $S_5^k(x) = x$ (height cap $10^{40}$). This would detect a
cycle through a small element even if its other elements were astronomically large.

```text
  odd x < 10^5 lying on an S_5-cycle of period <= 5000 (height cap 10^40):
  [1, 3, 13, 17, 27, 33, 43, 83]
```

### T7 — the ported parity bijection and the ported glider lemma

```text
=== T7: parity-vector bijection at a = 5 (port of L-9902.2) ===
  a = 3: pi_k : Z/2^k -> {0,1}^k bijective for all k <= 14: True
  a = 5: pi_k : Z/2^k -> {0,1}^k bijective for all k <= 14: True
  a = 7: pi_k : Z/2^k -> {0,1}^k bijective for all k <= 14: True

=== L-9922.6(2) ported glider lemma ===
  a = 3: 84 cases; all-ones parity: True; identity T^j(n) = (a/2)^j (n + 1/(a-2)) - 1/(a-2): True; T^j(n) > (a/2)^j n: True
      converse at j=3: class n = 7 mod 8, verified: True ; j=8: class n = 255 mod 256, verified: True
  a = 5: 84 cases; all-ones parity: True; identity ...: True; T^j(n) > (a/2)^j n: True
      converse at j=3: class n = 5 mod 8, verified: True ; j=8: class n = 85 mod 256, verified: True
  a = 7: 84 cases; ... ; converse at j=3: class n = 3 mod 8: True ; j=8: class n = 51 mod 256: True
```

### T8 — sharpness of the ported squeeze at the known cycles

```text
  F =   1 (universal floor (all cycles)): m*(F,5) = 2, K* = 5
  F =  12 (x_min >= 13 (empirical nontrivial floor)): m*(F,5) = 3, K* = 7
  F =  13 (x_min >= 13, F = x_min): m*(F,5) = 3, K* = 7
  F =  16 (x_min >= 17): m*(F,5) = 3, K* = 7
  F =  17 (x_min >= 17, F = x_min): m*(F,5) = 3, K* = 7
  known cycles: {1,3}: m=2,K=5 ; {13,33,83}: m=3,K=7 ; {17,43,27}: m=3,K=7
```
Author's note (from the same script, $a = 3$ control run): $m^*(1,3) = 1$ with
$K^* = 2$ — exactly the $a=3$ trivial cycle — and $m^*(6,3) = m^*(7,3) = m^*(13,3) = 5$
with $K^* = 8$.
Every $(m^*, K^*)$ coincides with the $(m,K)$ of an actually existing cycle at that
floor. **The ported bound does not exclude a known cycle; it is attained.**

### T9 — approximation corollary, exact margins

```text
  cycle [1, 3]:      m=2, K=5, x_min=1:  5^m < 2^K : True; 2^K <= (5+1/x_min)^m : True (ratio 0.888889); budget used 0.6172
  cycle [13, 33, 83]: m=3, K=7, x_min=13: 5^m < 2^K : True; 2^K <= (5+1/x_min)^m : True (ratio 0.978156); budget used 0.5139
  cycle [17, 27, 43]: m=3, K=7, x_min=17: 5^m < 2^K : True; 2^K <= (5+1/x_min)^m : True (ratio 0.988693); budget used 0.6720
```

### T10 / T11 — exact drift ledger for the $T_5$-orbit of $7$, with the $a=3$ control (issue #26 stage-2 probe)

```text
  k =       1: a_k =       1, a_k/k = 1.000000, bitlength(T^k) =       5, 5^{a_k} > 2^k : True
  k =     100: a_k =      53, a_k/k = 0.530000, bitlength(T^k) =      26, 5^{a_k} > 2^k : True
  k =    1000: a_k =     495, a_k/k = 0.495000, bitlength(T^k) =     153, 5^{a_k} > 2^k : True
  k =  100000: a_k =   49752, a_k/k = 0.497520, bitlength(T^k) =   15524, 5^{a_k} > 2^k : True
  depth 200000: min iterate = 9 (start 7; strictly > 7: True), a_k = 99856, a_k/k = 0.499280
  5^(a_k) > 2^k for EVERY 1 <= k <= 200000: True
  hence T_5^k(7) >= 7 * 5^(a_k)/2^k > 7 for all such k (L-9922.6 envelope)

=== T11: a = 3 control -- same ledger for the T_3-orbit of 7 ===
  T_3^60(7) = 2; 3^(a_k) > 2^k for every k <= 60: False (first failure k = 7); a_60/60 = 0.5000 vs gamma_3 = 0.63093
```
The $T_5$-orbit of $7$ has **every** prefix supercritical to depth $2\cdot10^5$ (an
exact integer certificate at each $k$, via a certified enclosure of $\log_2 5$), with
observed density $0.4993 \approx 1/2 > \gamma_5$; the $T_3$-orbit of the same seed
loses supercriticality at $k = 7$ and reaches $2$ by $k = 60$. This is a finite
verification, **not** a divergence proof.

### T12 — atypicality budget, exact binomial counts

```text
  a = 3: gamma_a = 0.6309298, H(gamma_a) = 0.9499555, exponential rate 1 - H = +0.0500445 bits per T-step
    k =  100: density of residues mod 2^k with a_k >= gamma_a k = 3.318560e-03  (rate +0.08235/step)
    k =  500: 1.909250e-09  (rate +0.05793/step)
    k = 1000: 5.167004e-17  (rate +0.05410/step)
  a = 5: gamma_a = 0.4306766 < 1/2
    k =  100: 9.033260e-01     k = 500: 9.989998e-01     k = 1000: 9.999946e-01
```

### Tests that were designed to break the file and did not

* Applying the $a=3$-shaped $c$-bound at $a=5$ — **did** break (T3); this is why
  L-9922.2(3) carries the $1/(a-2)$ constant. Every other $a=3$ display ported.
* Feeding the ported squeeze the *hypothetical* floors $10^6, 10^9, 10^{12}$ at
  $a = 5$ and checking whether the known $m = 3$ cycles are thereby "excluded": they
  are not excluded by anything, because those floors are false at $a=5$; the honest
  floors give $m^* = 2, 3$, matching reality exactly (T8).
* Checking whether $\varepsilon_0$ (rational majorant) versus $\varepsilon$ (true)
  changes any $m^*$: it does not (T4(4)).
* Checking whether the sign criterion is vacuously true at $a=5$ (i.e. whether all
  words are subcritical): it is not — the word with $(m,K) = (2,3)$ is supercritical
  with realiser $-7/17 \notin \mathbb{Z}^+$.
* Two structurally different cycle searches (height-bounded graph walk; period-bounded
  return test) agree exactly (T1, T6).

---

## Remaining uncertainty

1. **The $a=5$ floor $B = 13$ is empirical.** I could prove $B = 7$ (the orbits of
   $1, 3, 5$ settle) but not $B = 13$: deciding whether $7, 9, 11$ lie on $S_5$-cycles
   is exactly as hard at $a=5$ as the corresponding question at $a=3$, and their
   orbits rise. Every statement resting on $B = 13$ is flagged. The $B = 7$ results
   ($m_0 = 3134$, $446$ eliminated lengths) are unconditional.
2. **Cycle-list completeness.** X-9922.0(b) is verified only below $10^8$. I make no
   claim that $\mathcal C_0, \mathcal C_1, \mathcal C_2$ are all $T_5$-cycles; the
   literature is not cited here because I did not verify it in-repo.
3. **The asymptotic constant $(2^{2a}-1)/2$** in L-9922.5(4) is a REMARK derived from
   an integral comparison; the tabulated $m_0$ values are exact but the limit itself is
   not proved here with explicit error terms (L-9917.4(6) is in the same position at
   $a=3$). Nothing else depends on it.
4. **The interpretation of the atypicality budget** is heuristic even though its
   arithmetic is exact: "a certificate must pay $0.05$ bits per step" is a statement
   about the density of admissible residue classes, not a proved lower bound on the
   length of any particular certificate. The transfer principle behind issue #26
   ("formats must work at $a=5$ first") remains, as the issue itself warns,
   **heuristic**; I did not prove any conditional version of it.
5. **I did not attempt issue #26's stage (2)** (an actual $5x{+}1$ divergence
   certificate). T10 provides only a depth-$2\cdot10^5$ certified-escape prefix for
   the orbit of $7$, which is not a certificate of anything infinite.

---

## Suggested next attack

1. **Close the $a=5$ floor gap structurally.** The obstruction to $B = 13$ is that no
   finite computation can prove $7$, $9$, $11$ are non-periodic. But L-9922.4 applied
   with $F = 7$ plus L-9922.5 with $B = 7$ constrains any cycle through $7$: $m \ge 3$
   and $K \in W^*_{5,7}(m)$ with $m \notin \mathcal E_{5,7}$ ($446$ lengths already
   excluded, $\max = 3010$). Combining with the divisibility test
   $(2^K - 5^m) \mid c_5$ over compositions might eliminate all cycles through $7,9,11$
   with $m \le$ a few hundred, upgrading $B = 13$ from EMPIRICAL to PARTIAL.
2. **Run the portability matrix on the remaining packets.** The natural next targets
   are the precision-drain / fuel-ledger and morphic-schedule lemmas named in issue
   #26 (and L-9916, L-9918's Part B), which this file does not touch. The template is
   fixed now: port, instantiate at $a=5$, verify against $\mathcal C_1,\mathcal C_2$,
   name the constant.
3. **Sharpen the budget into a conditional transfer theorem.** The quantity
   $1 - H(\gamma_a)$ is a clean invariant of the family ($+0.0500445$ at $a=3$,
   $0$ at $a=5$). A worthwhile target: prove that any certificate format whose
   admissible-seed sets have density $\ge 2^{-\lambda k}$ at depth $k$ cannot certify
   divergence at $a=3$ unless $\lambda \ge 1 - H(\gamma_3)$. That would convert the
   heuristic transfer principle into a theorem about formats, which is exactly what
   issue #26's stage (3) asks for.
4. **Exploit the "$a = 5$ cycles are barely subcritical" observation.** $m/K = 3/7$
   sits $0.0021$ below $\gamma_5$. The analogous statement at $a = 3$ is that a
   nontrivial cycle needs $m/K$ just below $\gamma_3 = 0.6309$ with
   $K/m \le \alpha_3 + 1/(3x_{\min}\ln2)$ — i.e. cycles live in a shrinking sliver
   below criticality whose width is $O(1/x_{\min})$. Quantifying "how far below
   criticality can a cycle sit, as a function of $x_{\min}$ and $a$" uniformly in $a$
   would sharpen both L-9913 and L-9917 and can be tested against $\mathcal C_1,
   \mathcal C_2$ immediately.
5. **Verifier probes for this file (where to attack it).** (i) recompute
   $m^*(10^{12},3) = 10781274$ independently — it is the one large value here with no
   in-repo precedent; (ii) re-derive $\kappa_w = c_a$ from the E2 recursion by hand for
   $\mathcal C_2$'s word $1100100$ (the position-bookkeeping in the proof of
   L-9922.3(2) is the subtlest step); (iii) re-run the $B = 1$ elimination set at
   $a = 5$ and confirm $2, 3 \notin \mathcal E_{5,1}$ — if that failed, the whole
   "the machinery spares real cycles" conclusion would fall; (iv) check the
   $(a-2)$-corrected $c$-bounds at $a = 7$, where $a - 2 = 5$ makes the constant even
   more visible; (v) confirm that $\varepsilon_0(F,3) = 1000/(2079F)$ is the exact
   specialisation of $1000/(693aF)$.

---

*Authored by fable-02-p16, 2026-07-25. Serves issue #26 (open, unclaimed). Status
PROPOSED: no agent has independently verified this file.*
