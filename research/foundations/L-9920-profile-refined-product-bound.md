# L-9920 — The profile-refined product bound: injecting the exponent–residue dictionary into the sorted-element bound, and the exact ceiling of the element-set method

```text
Claim ID:      L-9920
Title:         Per-class (mod 2^{t+1}) spacing of same-exponent cycle elements, the
               profile-refined product bound 2^K <= Q(m,K), the exact 48-value
               elimination set (L-9917's 46 plus m = 13 and m = 79), the exact
               threshold m0' = 208, and the NULL verdict in the large-floor regime
Status:        PROPOSED
Authoring agent:   fable-02-p14
Reviewing agents:  (none yet)
Created:       2026-07-25
Last updated:  2026-07-25
Dependencies:  NOTATION.md (D-9903 odd part, D-9904 Syracuse map S and step exponent
               a(x) = nu_2(3x+1) >= 1, D-9905 trivial cycle (1), D-9908 S-cycle
               notation x_1 -> ... -> x_m -> x_1, least period m, a_i, K = sum a_i,
               x_min; empty-product convention).
               L-9905 (Status: PROVED, fable-02-v4) — L-9905.2 (2^K > 3^m) and
               L-9905.3 (2^K = prod (3 + 1/x_i)).  BOTH RE-DERIVED INLINE (Step 1).
               L-9906 (Status: PROVED, fable-02-v5) — L-9906.2 (every element of a
               nontrivial S-cycle is >= 7).  RE-DERIVED INLINE (Step 3b).
               L-9912 (Status: PROVED, fable-02-v14) — L-9912.5 (exponent-residue
               dictionary).  RE-PROVED INDEPENDENTLY INLINE (Step 2) and verified
               exhaustively in test T1; this file therefore does not inherit any
               other content of L-9912.
               L-9917 (Status: PROVED, author fable-02-p11 / reviewer fable-02-v17)
               — LOAD-BEARING in two places only: (i) L-9917.1(1) (elements of a
               least-period-m cycle are pairwise distinct), restated with a one-line
               proof sketch in Step 3a; (ii) the numbers P(m) = N(m)/D(m), the
               window W*(m), the 46-value set E and the threshold m_0 = 196, all of
               which are RECOMPUTED here from scratch (tests T4, T6) and used only
               for comparison.  No statement of this file rests on an unverified
               L-9917 claim.
               L-9913 (Status: PROVED, fable-02-v18) — used ONLY in L-9920.5, as the
               target of a comparison; its hypothesis (V_F) is not assumed anywhere
               else in this file.
               L-9915 (Status: PROVED, fable-02-v10) — comparison only.
Scope:         All nontrivial S-cycles (D-9908) on the POSITIVE odd integers, every
               least period m >= 1.  L-9920.1(floor part), .2, .3, .4 require
               positivity and the floor x_i >= 7; they are FALSE for the trivial
               cycle (1) and for the negative cycles (-1), (-5,-7), (-17,...), for
               which test T2 identifies the exact failing hypothesis (positivity /
               floor — the congruence and spacing halves of L-9920.1 survive there
               verbatim).  L-9920.5 is stated for a general verified floor F and is
               a NULL result (no improvement).  The elimination set of L-9920.4 and
               the threshold m0' = 208 are EXACT integer computations, complete over
               ALL m >= 1 (not artefacts of a search range).
Related counterexample candidates: none
```

---

## Statement

Throughout, $S$ is the Syracuse map (D-9904) on the positive odd integers,
$S(x) = (3x+1)/2^{\nu_2(3x+1)}$, with step exponent $a(x) := \nu_2(3x+1) \ge 1$. An
$S$-cycle is written as in D-9908: $x_1 \to x_2 \to \dots \to x_m \to x_1$, least period
$m \ge 1$, all $x_i$ positive odd, $x_{i+m} := x_i$, $a_i := a(x_i)$,
$K := \sum_{i=1}^m a_i$. The **trivial** cycle is the fixed point $(1)$ (D-9905). For
$t \ge 1$ put
$$m_t \;:=\; \#\{\, i \in \{1,\dots,m\} : a_i = t \,\},$$
so that the **exponent profile** $\pi = (m_1, m_2, m_3, \dots)$ satisfies
$$\sum_{t \ge 1} m_t \;=\; m, \qquad \sum_{t \ge 1} t\, m_t \;=\; K .$$

**Residue base points and class floors.** For $t \ge 1$ define (as in L-9912.5)
$$r_t \;:=\;\begin{cases}\dfrac{2^t-1}{3}, & t \text{ even},\\[2mm] \dfrac{5\cdot 2^t-1}{3}, & t \text{ odd},\end{cases}
\qquad\text{and}\qquad
\boxed{\;\beta_t \;:=\; \min\{\,x \in \mathbb{Z} : x \ge 7,\ x \equiv r_t \ (\mathrm{mod}\ 2^{t+1})\,\}.\;}$$
Then $\beta_t = r_t$ for every $t \notin \{1,2,4\}$ and $\beta_t = r_t + 2^{t+1}$ for
$t \in \{1,2,4\}$; explicitly
$$(\beta_1,\dots,\beta_{14}) = (7,\;9,\;13,\;37,\;53,\;21,\;213,\;85,\;853,\;341,\;3413,\;1365,\;13653,\;5461).$$

**The refined bounds.** For a profile $\pi$ with finite support put
$$P(\pi) \;:=\; \prod_{t \ge 1} \ \prod_{j=0}^{m_t - 1}\Bigl(3 + \frac{1}{\beta_t + 2^{t+1} j}\Bigr) \;\in\; \mathbb{Q}_{>0},$$
and for integers $m \ge 1$, $K \ge m$,
$$\boxed{\;Q(m,K) \;:=\; \max\Bigl\{\,P(\pi)\ :\ \textstyle\sum_t m_t = m,\ \sum_t t\,m_t = K,\ m_t \in \mathbb{Z}_{\ge 0}\Bigr\}.\;}$$
(The maximum is over a finite nonempty set — L-9920.3(3) — hence exists.) Finally let
$$W'(m) \;:=\; \bigl\{\,K \in \mathbb{Z}\ :\ 3^m < 2^K \le Q(m,K)\,\bigr\}$$
be the **refined $K$-window**, to be compared with L-9917's
$W^*(m) = \{K : 3^m < 2^K \le P(m)\}$, $P(m) = \prod_{j<m}\bigl(3+\frac1{7+2j}\bigr) = N(m)/D(m)$.

---

**L-9920.1 (per-class spacing and the correct class floor).** Let
$x_1 \to \dots \to x_m \to x_1$ be a nontrivial $S$-cycle. Fix $t \ge 1$ with $m_t \ge 1$
and let $x^{(t)}_{(0)} < x^{(t)}_{(1)} < \dots < x^{(t)}_{(m_t-1)}$ be the increasing
enumeration of $\{x_i : a_i = t\}$. Then:

1. the $m_t$ elements are **pairwise distinct** positive odd integers, all $\ge 7$, and
   all lie in the **single** residue class $x \equiv r_t \pmod{2^{t+1}}$;
2. consequently consecutive ones differ by at least $2^{t+1}$, and
   $$\boxed{\;x^{(t)}_{(j)} \;\ge\; \beta_t + 2^{t+1} j \qquad (0 \le j \le m_t - 1);\;}$$
3. $\beta_t$ is exactly as displayed above: $r_t < 7$ holds **only** for
   $t \in \{1,2,4\}$ (where $r_t = 3, 1, 5$), so $\beta_1 = 3+4 = 7$, $\beta_2 = 1+8 = 9$,
   $\beta_4 = 5+32 = 37$, and $\beta_t = r_t$ otherwise.

> **Correction flag (C1), against the assigning sketch.** The sketch proposed the
> starting point $\max(7, r_t)$. That is **wrong for $t = 2$ and $t = 4$**: $\max(7,r_2) = 7$
> but $a(7) = 1 \ne 2$ ($7 \not\equiv 1 \bmod 8$), and $\max(7,r_4) = 7 \ne 37$ ($a(7) = 1 \ne 4$;
> the smallest $x \ge 7$ with $a(x) = 4$ is $37$). The correct floor is
> $\beta_t = r_t + 2^{t+1}\cdot[\,r_t < 7\,]$, which is **larger**, so the corrected bound is
> **stronger** than the sketch's, not weaker. Verified exhaustively in test T1.

**L-9920.2 (profile-refined product bound, and its exact set-theoretic meaning).** Let
$x_1 \to \dots \to x_m \to x_1$ be a nontrivial $S$-cycle with profile $\pi$ and exponent
sum $K$. Then
$$\boxed{\;3^m \;<\; 2^K \;=\; \prod_{i=1}^m\Bigl(3+\frac1{x_i}\Bigr) \;\le\; P(\pi) \;\le\; Q(m,K) \;\le\; P(m).\;}$$
Moreover, writing $A_t := \{x \text{ odd}, x \ge 7 : a(x) = t\} = \{\beta_t + 2^{t+1} j : j \ge 0\}$
and
$$\mathcal{Y}(m,K) \;:=\; \Bigl\{\,Y \subseteq \{\text{odd } x \ge 7\} \ :\ |Y| = m,\ \sum_{x \in Y} a(x) = K \,\Bigr\},$$
one has the **exact identification**
$$\boxed{\;Q(m,K) \;=\; \max_{Y \in \mathcal{Y}(m,K)} \ \prod_{x \in Y}\Bigl(3+\frac1x\Bigr),\;}$$
the maximum being attained at the "greedy" set $G(\pi^\star) := \bigcup_t \{\beta_t + 2^{t+1}j : j < m^\star_t\}$
of the optimal profile. **Consequently $Q(m,K)$ is the sharpest possible bound obtainable
from the four inputs {product formula, positivity, floor $x_i \ge 7$, exponent–residue
dictionary} together with distinctness — no further exploitation of these inputs alone can
improve it.**

**L-9920.3 (the elimination question as an exact finite optimisation).** Let $m \ge 1$.

1. **(Elimination criterion.)** If a nontrivial $S$-cycle of least period $m$ exists, then
   its profile $\pi$ satisfies $3^m < 2^{K(\pi)} \le P(\pi)$ where $K(\pi) = \sum_t t\,m_t$.
   Hence
   $$W'(m) = \varnothing \;\Longrightarrow\; \textbf{no nontrivial } S\textbf{-cycle has least period } m .$$
   Note that $K$ is **determined by the profile**, not a free parameter.
2. **($K$ is confined to L-9917's window.)** $W'(m) \subseteq W^*(m)$; and for every
   $m \le 12\,679$, $|W^*(m)| \le 1$ (L-9917.4(5); recomputed here for $m \le 208$ in T9),
   so at most one $K$ per $m$ has to be examined and the refinement can only turn a
   singleton window into an empty one.
3. **(Finiteness, exactly.)** Put $E := K - m$. Every profile with $\sum_t m_t = m$,
   $\sum_t t\,m_t = K$ satisfies $E = \sum_{t\ge2}(t-1)m_t \ge 0$, $m_t = 0$ for $t \ge E+2$,
   and $m_t \le \lfloor E/(t-1)\rfloor$ for $t \ge 2$. The profile set is therefore finite
   and (for $K \ge m$) nonempty, so $Q(m,K)$ is a maximum over a finite nonempty set.
4. **(Exact evaluation.)** $Q(m,K)$ is computed by the $0/1$ knapsack recursion
   $$Q(m,K) \;=\; \max_{0 \le n \le \min(m,E)} \Bigl[\, D(n,E)\cdot\prod_{j=0}^{m-n-1}\Bigl(3+\frac1{7+4j}\Bigr)\Bigr],$$
   where $D(n,e)$ is the maximum of $\prod_{x \in Z}(3+1/x)$ over $n$-element subsets $Z$
   of $\bigcup_{t\ge2} A_t$ with $\sum_{x\in Z}(a(x)-1) = e$, itself a two-dimensional
   knapsack over the items $\{(t-1,\ \beta_t+2^{t+1}j)\}_{t \ge 2,\ j < \lfloor E/(t-1)\rfloor}$.
5. **(Monotonicity, which makes the search terminate.)** Let $\kappa(m) := \mathrm{bl}(3^m)$
   be the least integer $K$ with $2^K > 3^m$. Then
   $$\mathcal{W}(m) \;:=\; \frac{Q(m,\kappa(m))}{3^m} \quad\text{is \textbf{strictly increasing} in } m .$$
6. **(What is NOT true — correction flag (C2).)** The trade-off is *not* governed by any
   "move mass from a high class to a low class" monotonicity, because moving one element
   from class $t$ to class $s$ changes $K$ by $s-t$ and therefore leaves the admissible
   set. In particular the maximiser does **not** maximise $m_1$: at $(m,K) = (8,13)$ all
   seven profiles are
   $$\{1^7 6^1\},\{1^6 3^1 4^1\},\{1^6 2^1 5^1\},\{1^5 2^1 3^2\},\{1^5 2^2 4^1\},\{1^4 2^3 3^1\},\{1^3 2^5\},$$
   with $m_1 = 7,6,6,5,5,4,3$; the maximum of $P$ is attained at $\{1^4 2^3 3^1\}$
   ($m_1 = 4$, $P = 8094.9096\ldots$), while the largest-$m_1$ profile gives only
   $7767.8167\ldots$ (test T7). The optimisation is genuinely two-constraint and is solved
   here exactly, not by a greedy rule.

**L-9920.4 (the refined elimination set; complete over all $m$).** Define
$\mathcal{E}' := \{ m \ge 1 : W'(m) = \varnothing\}$. Then $\mathcal{E}'$ is **finite** and
equals **exactly** the following $48$-element set:
$$\mathcal{E}' = \{1,2,3,4,6,7,8,9,11,12,\mathbf{13},14,16,18,19,21,23,24,26,28,31,33,36,38,43,45,48,50,53,55,$$
$$\qquad\ \ 60,62,65,67,72,77,\mathbf{79},84,89,96,101,106,113,118,130,142,159,171\},\qquad \max\mathcal{E}' = 171,$$
i.e. $\mathcal{E}' = \mathcal{E} \cup \{13,\,79\}$ where $\mathcal{E}$ is L-9917.3's $46$-element
set. Consequently **no nontrivial $S$-cycle has least period $m \in \mathcal{E}'$.**
Furthermore:

1. **(Strictly stronger than L-9917, and by exactly two values.)** $\mathcal{E} \subsetneq \mathcal{E}'$.
   The $46$ old values are re-obtained because $W^*(m) = \varnothing$ already; the two new
   values are the two $m$ at which L-9917's window is a singleton that the refinement
   closes:
   $$m = 13:\ W^*(13) = \{21\},\quad 2^{21}\,\mathrm{den}\,Q = 42\,160\,477\,185\,047\,789\,568\,000 \;>\; 41\,941\,581\,246\,154\,670\,080\,000 = \mathrm{num}\,Q,$$
   $$m = 79:\ W^*(79) = \{126\},\quad 2^{126} > Q(79,126) \text{ by the exact factor } 1.008058932\ldots$$
   (at $m = 13$ the factor is $1.005219067\ldots$; L-9917's own ratios at the same $K$ are
   $0.999507595\ldots$ and $0.999916890\ldots$, i.e. both were near-misses). The maximising
   profiles are $\{m_1{=}7, m_2{=}4, m_3{=}2\}$ at $m=13$ (element set
   $\{7,9,11,13,15,17,19,23,25,27,29,31,33\}$) and
   $\{m_1{=}50,m_2{=}18,m_3{=}7,m_4{=}2,m_5{=}1,m_6{=}1\}$ at $m=79$.
2. **(The threshold moves from $196$ to $208$.)** Let
   $m_0' := \min\{\,m : \mathcal{W}(m) \ge 2\,\}$, the refined analogue of L-9917's
   $m_0 = 196$. Then
   $$\boxed{\;m_0' \;=\; 208,\;}$$
   certified by the two exact comparisons
   $$Q(207,\kappa(207)) \;<\; 2\cdot 3^{207} \quad(\text{ratio } 0.9995490918\ldots), \qquad
     Q(208,\kappa(208)) \;\ge\; 2\cdot 3^{208} \quad(\text{ratio } 1.0001626886\ldots),$$
   together with the strict monotonicity of $\mathcal{W}$ (L-9920.3(5)). For **every**
   $m \ge 208$ we then have $2^{\kappa(m)} \le 2\cdot3^m \le Q(m,\kappa(m))$, so
   $\kappa(m) \in W'(m) \ne \varnothing$: **the refined method eliminates no $m \ge 208$,
   ever.** Combined with the exhaustive exact evaluation of $1 \le m \le 207$, this proves
   $\mathcal{E}'$ is exactly the $48$-element set above — a statement about all $m$.
3. **(Size of the gain.)** The refined window width
   $\mathrm{Wd}'(m) := \log_2\bigl(Q(m,\kappa(m))/3^m\bigr)$ falls short of L-9917's
   $\mathrm{Wd}(m) = \log_2(P(m)/3^m)$ by only
   $$\mathrm{Wd}(m) - \mathrm{Wd}'(m) \;=\; 0.0036\ (m{=}8),\ 0.0082\ (m{=}13),\ 0.0117\ (m{=}79),\
       0.0144\ (m{=}171),\ 0.0150\ (m{=}208)$$
   bits (exact rationals, displayed to four places; test T9). **Observation (finite
   verification, not proved):** the deficit appears to converge to $\approx 0.0157$ bits, so
   the refined width keeps L-9917's $\tfrac16\log_2 m$ rate with the additive constant
   lowered by about $0.015$; this is why the elimination set grows by only two values and
   $\max\mathcal{E}'$ does not move at all.

**L-9920.5 (interaction with a general verified floor: NULL).** Let $F \ge 2$ be an integer
with the property that every $n \le F$ reaches $1$ under $C$ (L-9913's hypothesis
$(\mathrm{V}_F)$), so that every element of a nontrivial cycle satisfies $x_i \ge F+1$
(L-9913.1). Write $\beta_t(F) := \min\{x \ge F+1 : x \equiv r_t \pmod{2^{t+1}}\}$ and
$P_F(\pi) := \prod_t\prod_{j<m_t}\bigl(3 + 1/(\beta_t(F) + 2^{t+1}j)\bigr)$. Then the proof of
L-9920.2 gives verbatim
$$3^m < 2^K \le P_F(\pi) \le Q_F(m,K) \le P_{F+1}(m) \le \Bigl(3+\frac1{F+1}\Bigr)^m ,$$
the last two bounds being L-9917's (distinctness only) and L-9913's (floor only). However:

1. **At $F = 10^6$, $m = 2966$** (L-9913's bound, with $K = \kappa(2966) = 4701$) the explicit
   profile $\pi = \{m_1{=}1814,\, m_2{=}737,\, m_3{=}283,\, m_4{=}100,\, m_5{=}28,\, m_6{=}4\}$
   satisfies $3^m < 2^K \le P_F(\pi)$ **exactly**. Hence $m = 2966$ survives the refined
   constraint and $m^*(10^6) = 2966$ is **unchanged**.
2. **At $F = 10^9$, $m = 47468$** ($K = 75235$) the explicit profile
   $\{m_1{=}29026,\,m_2{=}11797,\,m_3{=}4539,\,m_4{=}1591,\,m_5{=}456,\,m_6{=}59\}$ likewise
   satisfies $3^m < 2^K \le P_F(\pi)$; $m^*(10^9) = 47468$ is **unchanged**.
3. **(Quantified non-gain.)** In bits, the available window widths at $F = 10^6$, $m = 2966$
   are $0.001426343$ (crude, L-9913), $0.001422130$ (distinctness, L-9917) and
   $0.001421757$ (per-class, this file), against the requirement
   $\kappa(m) - m\log_2 3 = 0.001222861$. The per-class width is $99.68\%$ of the crude one;
   eliminating $m = 2966$ would require losing $13.99\%$. At $F = 10^9$ the corresponding
   numbers are $99.9948\%$ and $30.92\%$. **Verdict: NULL — the per-class refinement gives
   no improvement whatsoever to L-9913's $m \ge 2966$ / $m \ge 47468$.** The structural
   reason is that for $m \ll F$ every admissible element set has
   $\sum_{x\in Y} 1/x = m/B\,(1 + O(m/B))$ with $B = F+1$, so all three bounds agree to
   relative order $m/B$ ($3\cdot10^{-3}$ resp. $4.7\cdot10^{-5}$), while a change of the
   conclusion needs a relative change of order $10^{-1}$. The author's prior expectation
   ("probably yields nothing") is **confirmed**, and is here proved rather than assumed.

**L-9920.6 (honest assessment).**

1. **What was gained.** (i) Two new values of $m$ ($13$ and $79$) are eliminated with no
   enumeration of exponent words; $m = 13$ was explicitly listed in L-9917.5(2) as a case
   "the elimination genuinely requires L-9906/L-9915's composition enumeration", and that
   statement is now superseded. (ii) The exact threshold analogue moves $196 \to 208$.
   (iii) Most importantly, the **ceiling of the whole approach** is now pinned: $Q(m,K)$ is
   by L-9920.2 the *best possible* bound extractable from distinctness $+$ floor $7$ $+$ the
   full exponent–residue dictionary, and it eliminates exactly $48$ values, all $\le 171$,
   and provably none beyond $m = 207$.
2. **Is it subsumed by L-9917?** No: $\mathcal{E} \subsetneq \mathcal{E}'$ strictly, and
   L-9920.2's bound is $\le$ L-9917.2's for every profile (Step 4d). But the improvement is
   **marginal** — $\approx 0.015$ bit of window width, two extra values of $m$, and no change
   at all to $\max\mathcal{E}' = 171$. In elimination power both are dominated by L-9913
   ($m \ge 2966$), which however is conditional on the finite verification $(\mathrm{V}_F)$;
   L-9917 and L-9920 use no computation beyond their own exact arithmetic.
3. **Residual open direction.** The bound $Q(m,K)$ discards *all* order information: it
   maximises over element **sets** and never uses that the set must be closed under $S$
   ($S(\mathcal{C}) = \mathcal{C}$, i.e. $x \in \mathcal{C} \Rightarrow (3x+1)/2^{a(x)} \in \mathcal{C}$).
   Every maximiser found here is wildly non-$S$-closed (e.g. at $m = 13$ the maximiser
   contains $7$ but $S(7) = 11 \in$ set, $S(11) = 17 \in$ set, $S(17) = 13 \in$ set,
   $S(13) = 5 \notin$ set — so it is not closed). The next real gain must come from
   closure, not from finer floors. This is recorded as **Q-9920-A** below.

**Correction flags (audit of the assigning sketch).**

- **(C1)** $\max(7, r_t)$ is wrong for $t \in \{2,4\}$; the correct class floor is
  $\beta_t = r_t + 2^{t+1}[r_t<7]$, giving $\beta_2 = 9$, $\beta_4 = 37$ (Statement, L-9920.1).
  The correction strengthens the bound.
- **(C2)** The sketch's suggested structural fact ("monotonicity in moving an element from a
  high-$t$ class to a low-$t$ class") does **not** hold in the form needed, because such a move
  changes $K$ and leaves the constraint set; the maximiser does not maximise $m_1$ (T7).
  The finite optimisation is made exact here by the support/multiplicity caps of
  L-9920.3(3) plus an exact knapsack, and made terminating by the exchange lemma
  L-9920.3(5) — not by any greedy monotonicity.
- **(C3)** The sketch's optimisation ("for fixed $m$, maximise $P$ subject to
  $\sum t\,m_t = K$ and compare with $3^m$") must be stated with the comparison against
  $2^{K}$, with $K$ *determined by the profile*: the correct criterion is
  "$\exists\,\pi$ with $\sum_t m_t = m$ and $3^m < 2^{K(\pi)} \le P(\pi)$". Comparing $P$
  with $3^m$ alone is vacuous ($P(\pi) > 3^m$ always).
- **(C4)** The sketch expected "a substantial unexploited constraint" from
  $m_1 > 0.415\,m$. The constraint is real but its numerical value is small: it is worth
  $\approx 0.015$ bit (L-9920.4(3)). The reason is quantified in Step 6c: the sorted union of
  the per-class floors is only mildly more spread out than the raw odd integers $\ge 7$
  (largest element $543$ against $421$ at $m = 208$), and $\sum 1/x$ is insensitive to that.
  Note also that the *maximiser's* $m_1/m \approx 0.65$, far above the $0.415$ forced by
  counting — the counting bound is not what binds.
- **(C5)** The sketch's expectation for L-9920.5 is confirmed (NULL), and quantified.

---

## Definitions

- $S$, $a(x) = \nu_2(3x+1)$ — D-9904; cycle data $x_i, a_i, K$, least period $m$ — D-9908;
  trivial cycle $(1)$ — D-9905.
- **Cycle set.** $\mathcal{C} := \{x_1,\dots,x_m\}$; $S(\mathcal{C}) = \mathcal{C}$.
- **Exponent profile.** $\pi = (m_t)_{t\ge1}$, $m_t = \#\{i : a_i = t\}$; rotation invariant.
  $\sum_t m_t = m$, $\sum_t t\,m_t = K$, and $E := K - m = \sum_{t\ge2}(t-1)m_t \ge 0$ is the
  **excess**.
- **Class.** $A_t := \{x \text{ odd},\ x \ge 7 : a(x) = t\}$. By L-9920.1,
  $A_t = \{\beta_t + 2^{t+1}j : j \ge 0\}$; the $A_t$ are pairwise disjoint with union all
  odd $x \ge 7$.
- **Greedy set of a profile.** $G(\pi) := \bigcup_{t}\{\beta_t + 2^{t+1}j : 0 \le j < m_t\}$;
  $|G(\pi)| = m$, $\sum_{x \in G(\pi)}a(x) = K$, $P(\pi) = \prod_{x\in G(\pi)}(3+1/x)$.
- **$P(\pi)$, $Q(m,K)$, $W'(m)$, $\mathcal{W}(m)$** — as in the Statement.
- **$\kappa(m) := \mathrm{bl}(3^m)$**, the bit length of $3^m$, i.e. the least $K$ with
  $2^K > 3^m$; **$\lambda(m) := \max\{K : 2^K D(m) \le N(m)\} = \lfloor\log_2 P(m)\rfloor$.
  $W^*(m) = \{\kappa(m),\dots,\lambda(m)\}$.**
- **Widths.** $\mathrm{Wd}(m) = \log_2 P(m) - m\log_2 3$ (L-9917);
  $\mathrm{Wd}'(m) = \log_2 Q(m,\kappa(m)) - m\log_2 3$.
- Empty products are $1$ (NOTATION.md). All arithmetic in the proofs and scripts is exact
  (`int`, `fractions.Fraction`); floating point appears only in clearly labelled display
  ratios, never in a decision.

---

## Motivation

L-9917 replaced the crude bound $2^K \le (3+1/x_{\min})^m$ by the sorted-element bound
$2^K \le \prod_{j<m}(3+1/(7+2j))$, using one fact about a cycle's elements: they are
**distinct** odd integers $\ge 7$. It then showed the resulting method has a hard finite
ceiling — $46$ values of $m$, none beyond $171$, nothing at all beyond $m_0 = 196$ — and
asked where further leverage could come from.

L-9912.5 supplies an obvious candidate: an element's exponent *pins down its residue class*.
An element with $a_i = t$ lies in one class mod $2^{t+1}$, so the $m_t$ elements sharing
exponent $t$ are spaced $\ge 2^{t+1}$ apart, not $2$. Since a cycle's exponent profile is
constrained ($\sum m_t = m$, $\sum t m_t = K$ with $K/m$ pinned into a window of width
$\approx 0.07$ around $\log_2 3$), and since the *natural* mean exponent of odd integers is
$\sum_t t 2^{-t} = 2$ while a cycle needs $K/m \approx 1.585$, a cycle's element set must be
sharply atypical: it must be over-weighted towards class $1$, and therefore its class-$1$
elements must run further out than the $m$ smallest odd numbers do. That is a genuine,
previously unused arithmetic constraint, and it is exactly what this file injects.

The payoff for the counterexample-construction program of issue #9 is twofold. First, two
more values of $m$ ($13$, $79$) need no exponent-word search — small, but $m = 13$ was
explicitly flagged in L-9917.5(2) as requiring enumeration. Second, and more valuable for
planning: L-9920.2 shows that $Q(m,K)$ is the **exact optimum** of this family of arguments,
so the answer to "how much is the dictionary worth?" is now known to the last bit —
$\approx 0.015$ bit of window width, two values of $m$, threshold $196 \to 208$ — and no agent
need re-investigate it. The next increment must come from the one structural fact that all
of L-9905/L-9912/L-9913/L-9917/L-9920 throw away: that the element set is closed under $S$.

---

## Proof or construction

### Step 0 — standing setup

Fix an $S$-cycle $x_1 \to \dots \to x_m \to x_1$ of least period $m \ge 1$ on the positive
odd integers, cyclic indices $x_{i+m} = x_i$. The defining relation is
$$2^{a_i}\,x_{i+1} \;=\; 3x_i + 1 \qquad (i \in \mathbb{Z}). \tag{$\ast_i$}$$

### Step 1 — product formula and positivity (re-derived inline)

Divide $(\ast_i)$ by $x_i \neq 0$: $2^{a_i}x_{i+1}/x_i = 3 + 1/x_i$. Multiply over
$i = 1,\dots,m$; the left side telescopes to $2^{K}\cdot x_{m+1}/x_1 = 2^K$. Hence
$$2^K \;=\; \prod_{i=1}^m\Bigl(3+\frac1{x_i}\Bigr). \tag{PF}$$
Each $x_i > 0$ gives $3 + 1/x_i > 3$, so
$$2^K \;>\; 3^m. \tag{POS}$$
(These are L-9905.3 and L-9905.2. (POS) is the only place positivity is used; it is exactly
the hypothesis that fails for the negative cycles — test T2.) $\square$

### Step 2 — the exponent–residue dictionary, re-proved independently

**(2a)** For any nonzero integer $y$ and $t \ge 1$: $\nu_2(y) = t \iff y \equiv 2^t \pmod{2^{t+1}}$.
Indeed $\nu_2(y) = t$ means $y = 2^t u$ with $u$ odd, i.e. $u = 1+2k$, i.e.
$y = 2^t + k2^{t+1}$; conversely $y = 2^t(1+2k)$ has $\nu_2 = t$ since $1+2k$ is odd.

**(2b)** Applying this to $y = 3x+1$ (nonzero for every odd $x$):
$$a(x) = t \iff 3x + 1 \equiv 2^t \ (\mathrm{mod}\ 2^{t+1}) \iff 3x \equiv 2^t - 1 \ (\mathrm{mod}\ 2^{t+1}).$$
Since $\gcd(3, 2^{t+1}) = 1$, this congruence has exactly one solution modulo $2^{t+1}$.

**(2c)** $r_t$ is that solution. If $t$ is even then $2^t \equiv 1 \pmod 3$, so $3 \mid 2^t - 1$,
$r_t = (2^t-1)/3 \in \mathbb{Z}$ and $3r_t = 2^t - 1$ exactly. If $t$ is odd then
$5\cdot2^t \equiv 5\cdot 2 = 10 \equiv 1 \pmod 3$, so $3 \mid 5\cdot 2^t - 1$,
$r_t = (5\cdot2^t-1)/3 \in \mathbb{Z}$ and $3r_t + 1 = 5\cdot2^t = 2^t + 2^{t+2} \equiv 2^t \pmod{2^{t+1}}$.
In both cases $3r_t$ is odd, so $r_t$ is odd; and $0 < r_t < 2^{t+1}$ because
$(2^t-1)/3 < 2^t$ and $(5\cdot2^t-1)/3 < 2^{t+1}$. Hence, for **every** integer $x$ (positive
or not) and every $t \ge 1$,
$$\boxed{\;a(x) = t \iff x \equiv r_t \pmod{2^{t+1}}.\;} \tag{DICT}$$
$\square$

*(This is L-9912.5; the six lines above are its whole content, so this file does not inherit
anything else from L-9912. Note that (DICT) uses no positivity — which is why it survives on
the negative cycles in test T2. Exhaustively verified for $t \le 12$ over all odd $x < 2^{15}$
in test T1.)*

**(2d) The class floors.** $\beta_t := \min\{x \ge 7 : x \equiv r_t \pmod{2^{t+1}}\}$. Since
$0 < r_t < 2^{t+1}$, the class members $\ge 7$ are $r_t, r_t+2^{t+1}, \dots$ if $r_t \ge 7$,
and $r_t + 2^{t+1}, r_t + 2^{t+2},\dots$ if $r_t < 7$ (note $r_t + 2^{t+1} \ge 7$ always:
for $t=1$, $3+4=7$; for $t \ge 2$, $2^{t+1} \ge 8$). Now $r_1 = 3$, $r_2 = 1$, $r_3 = 13$,
$r_4 = 5$, $r_5 = 53$, $r_6 = 21$; and for even $t \ge 6$, $r_t = (2^t-1)/3 \ge 21 > 7$, while
for odd $t \ge 3$, $r_t = (5\cdot2^t-1)/3 \ge 13 > 7$. Hence $r_t < 7$ **exactly** for
$t \in \{1,2,4\}$, and
$$\beta_t = r_t + 2^{t+1}\cdot[\,t \in \{1,2,4\}\,] : \quad \beta_1 = 7,\ \beta_2 = 9,\ \beta_4 = 37,\ \beta_t = r_t \text{ otherwise}.$$
Finally, by (DICT), $A_t = \{x \text{ odd} \ge 7 : a(x) = t\} = \{\beta_t + 2^{t+1}j : j \ge 0\}$,
the $A_t$ ($t \ge 1$) are pairwise disjoint (as $a$ is a function) and
$\bigcup_{t\ge1}A_t = \{\text{odd } x \ge 7\}$ (as $a(x) \ge 1$ is finite for every odd $x$).
$\square$

### Step 3 — proof of L-9920.1

**(3a) Distinctness.** $x_1,\dots,x_m$ are pairwise distinct. *(This is L-9917.1(1), Status
PROVED. One-line reason: if $x_i = x_j$ with $p := j-i \in [1,m-1]$ then applying $S$
repeatedly shows $p$ is a period of $(x_i)_{i\in\mathbb{Z}}$; the periods form a subgroup of
$\mathbb{Z}$ generated by the least period $m$, so $m \mid p$, contradiction.)*

**(3b) Floor.** Every element of a nontrivial cycle is $\ge 7$. *(This is L-9906.2; argument
restated: $S(1) = 1$, $S(3) = 5$, $S(5) = 1$, so $1$ lies only on the trivial cycle and $3,5$
reach $1$ hence lie on no cycle; a cycle set is $S$-invariant, so
$\mathcal{C}\cap\{1,3,5\} = \varnothing$, and every positive odd integer outside $\{1,3,5\}$
is $\ge 7$.)*

**(3c) One class per exponent.** If $a_i = t$ then $x_i \equiv r_t \pmod{2^{t+1}}$ by (DICT).

**(3d) Spacing and floor per class.** Fix $t$ with $m_t \ge 1$ and let
$y_0 < y_1 < \dots < y_{m_t-1}$ enumerate $\{x_i : a_i = t\}$ (a set of size $m_t$ by (3a)).
All $y_j \ge 7$ by (3b) and all $y_j \equiv r_t \pmod{2^{t+1}}$ by (3c), so $y_j \in A_t$,
i.e. $y_0 \ge \beta_t$ by minimality of $\beta_t$. For $j \ge 1$, $y_j > y_{j-1}$ and
$y_j \equiv y_{j-1} \pmod{2^{t+1}}$ force $y_j \ge y_{j-1} + 2^{t+1}$. Induction on $j$ gives
$y_j \ge \beta_t + 2^{t+1}j$. $\square$

### Step 4 — proof of L-9920.2 (the rearrangement, done carefully)

**(4a) Block factorisation.** The index set $\{1,\dots,m\}$ is the disjoint union of the
finitely many nonempty blocks $I_t := \{i : a_i = t\}$, $|I_t| = m_t$ (finitely many because
$a_i \le K$ for each $i$). Since $(\mathbb{R}_{>0},\times)$ is a commutative monoid, a finite
product over an index set equals the product of the products over the blocks of any
partition:
$$\prod_{i=1}^m\Bigl(3+\frac1{x_i}\Bigr) \;=\; \prod_{t \ge 1}\ \prod_{i \in I_t}\Bigl(3+\frac1{x_i}\Bigr).$$

**(4b) Within a block.** Fix $t$ with $m_t \ge 1$. By (3a) the map $i \mapsto x_i$ is injective
on $I_t$, so $\{x_i : i \in I_t\}$ is a set of exactly $m_t$ elements and its increasing
enumeration $y_0 < \dots < y_{m_t-1}$ is a bijective relabelling of the block; therefore
$$\prod_{i \in I_t}\Bigl(3+\frac1{x_i}\Bigr) \;=\; \prod_{j=0}^{m_t-1}\Bigl(3+\frac1{y_j}\Bigr).$$
By Step 3d, $y_j \ge \beta_t + 2^{t+1}j > 0$. The function $f(u) := 3+1/u$ is strictly
decreasing and strictly positive on $(0,\infty)$, so
$$0 \;<\; 3+\frac1{y_j} \;\le\; 3 + \frac1{\beta_t + 2^{t+1}j} \qquad (0 \le j < m_t).$$
A finite product of positive reals is monotone in each factor (induction: if $0 < u_j \le v_j$
for $j < r+1$ then $\prod_{j\le r}u_j \le (\prod_{j<r}v_j)u_r \le \prod_{j\le r}v_j$), hence
$$\prod_{i \in I_t}\Bigl(3+\frac1{x_i}\Bigr) \;\le\; \prod_{j=0}^{m_t-1}\Bigl(3+\frac1{\beta_t+2^{t+1}j}\Bigr).$$

**(4c) Assembling.** Multiplying the block bounds (all factors positive) and using (PF):
$$2^K \;=\; \prod_{i=1}^m\Bigl(3+\frac1{x_i}\Bigr) \;\le\; \prod_{t\ge1}\prod_{j<m_t}\Bigl(3+\frac1{\beta_t+2^{t+1}j}\Bigr) \;=\; P(\pi) \;\le\; Q(m,K),$$
the last step because $\pi$ is one of the profiles competing in the maximum defining
$Q(m,K)$ (its constraints $\sum m_t = m$, $\sum t m_t = K$ hold by definition of $\pi$).
Together with (POS) this proves the chain of L-9920.2 up to $Q(m,K)$. $\square$

**(4d) Identification with the set maximum, and domination by L-9917.**
Recall $G(\pi) = \bigcup_t\{\beta_t + 2^{t+1}j : j < m_t\}$.

*(i) $G(\pi) \in \mathcal{Y}(m,K)$.* Its members are odd integers $\ge 7$; by Step 2d,
$a(\beta_t+2^{t+1}j) = t$ exactly, so the members drawn from different $t$ are distinct
(disjoint classes) and those from the same $t$ are distinct (distinct $j$). Hence
$|G(\pi)| = \sum_t m_t = m$ and $\sum_{x\in G(\pi)}a(x) = \sum_t t\,m_t = K$. Also
$P(\pi) = \prod_{x\in G(\pi)}(3+1/x)$ by construction.

*(ii) Every $Y \in \mathcal{Y}(m,K)$ is dominated by the $P$ of its own profile.* Let
$\pi_Y$ be the profile of $Y$ (i.e. $(\pi_Y)_t = |Y \cap A_t|$); then
$\sum_t(\pi_Y)_t = m$, $\sum_t t(\pi_Y)_t = K$, and the argument of (4b) — which used only
distinctness, the floor, and the congruence, all of which hold for the members of
$Y \cap A_t$ — gives $\prod_{x\in Y}(3+1/x) \le P(\pi_Y)$.

By (i) and (ii), $\max_{Y \in \mathcal{Y}(m,K)}\prod_{x\in Y}(3+1/x) = \max_\pi P(\pi) = Q(m,K)$,
which is L-9920.2's identification; the maxima are attained because the profile set is finite
(L-9920.3(3), proved in Step 5).

*(iii) Domination $Q(m,K) \le P(m)$.* Let $\pi$ be any competing profile and sort $G(\pi)$
increasingly as $g_0 < g_1 < \dots < g_{m-1}$. These are $m$ distinct odd integers $\ge 7$, so
by the elementary induction of L-9917.1(1d), $g_k \ge 7 + 2k$. Since $f$ is decreasing and
positive,
$$P(\pi) = \prod_{k<m}\Bigl(3+\frac1{g_k}\Bigr) \le \prod_{k<m}\Bigl(3+\frac1{7+2k}\Bigr) = P(m).$$
Hence $Q(m,K) \le P(m)$: **the refined bound is never weaker than L-9917's.** $\square$

*(Remark on the last inequality: it is what guarantees, a priori, that the refined
elimination set contains L-9917's $46$ values. Test T4 verifies the inequality numerically for
every $m \le 208$ and every $K \in W^*(m)$ — $0$ violations — and verifies the containment.)*

### Step 5 — proof of L-9920.3 (finite, exact optimisation)

**(5a) Elimination criterion (L-9920.3(1)).** By Step 4, a nontrivial cycle of least period
$m$ has a profile $\pi$ with $\sum_t m_t = m$ and $3^m < 2^{K(\pi)} \le P(\pi) \le Q(m,K(\pi))$,
so $K(\pi) \in W'(m)$. Contrapositive: $W'(m) = \varnothing$ implies no such cycle. Note the
logical shape: $K$ is a *function of* $\pi$, so the existential is over profiles only.

**(5b) $K$ lies in L-9917's window (L-9920.3(2)).** If $K \in W'(m)$ then
$3^m < 2^K \le Q(m,K) \le P(m)$ by (4d)(iii), i.e. $K \in W^*(m)$.

**(5c) Finiteness (L-9920.3(3)).** Let $\pi$ satisfy $\sum_t m_t = m$, $\sum_t t\,m_t = K$.
Then $E := K-m = \sum_t (t-1)m_t = \sum_{t\ge2}(t-1)m_t \ge 0$ since every term is
$\ge 0$. If $m_t \ge 1$ for some $t \ge 2$ then $(t-1) \le (t-1)m_t \le E$, so $t \le E+1$;
and $(t-1)m_t \le E$ gives $m_t \le \lfloor E/(t-1)\rfloor$. Thus every competing profile is
supported on $\{1,\dots,E+1\}$ with entries bounded by $m$, so there are finitely many; the
set is nonempty whenever $K \ge m$ (take $m_1 = m-1$, $m_{E+1} = 1$ if $E \ge 1$; $m_1 = m$ if
$E = 0$). Hence $Q(m,K)$ is a genuine maximum. $\square$

**(5d) Exact evaluation (L-9920.3(4)).** Fix $(m,K)$, $E = K-m \ge 0$. Split any competing
configuration $Y \in \mathcal{Y}(m,K)$ (equivalently, by (4d), any profile) into its class-$1$
part and the rest. If $n := |Y \setminus A_1|$ then $|Y \cap A_1| = m-n$ and, because class-$1$
elements carry excess $a-1 = 0$, the excess is carried entirely by $Y\setminus A_1$:
$\sum_{x \in Y\setminus A_1}(a(x)-1) = E$. For a fixed $n$, the class-$1$ part contributes at
most $\prod_{j<m-n}(3+1/(7+4j))$ (its members are $m-n$ distinct elements of
$A_1 = \{7,11,15,\dots\}$, so Step 4b applies with $t=1$), with equality for the prefix. The
remaining part is exactly an optimisation over $n$-element subsets $Z \subseteq \bigcup_{t\ge2}A_t$
with total excess $E$, whose maximum is the quantity $D(n,E)$ of L-9920.3(4). This proves the
displayed recursion. $D$ itself is a two-dimensional $0/1$ knapsack over the items
$(t-1,\ \beta_t + 2^{t+1}j)$, $t \ge 2$; by (5c) only $t \le E+1$ and $j < \lfloor E/(t-1)\rfloor$
can occur, so the item list is finite (in the computation: $609$ items for $E \le 122$). Two
independent implementations of this recursion — one in the log domain with certified
$128$-bit integer upper bounds, one in exact rational arithmetic with cross-multiplied
comparisons — agree on every value tested, and both agree with brute-force enumeration over
all admissible sets for $m \le 7$ (tests T3, T4). $\square$

*(Correctness note: the knapsack may select a non-prefix subset of a class's items, but every
such subset is still a legitimate set of distinct class-$t$ elements $\ge 7$, so no
overestimate arises; and all prefixes are available, so no underestimate arises. Hence the DP
value equals $Q(m,K)$ exactly.)*

**(5e) Monotonicity (L-9920.3(5); the exchange lemma).** Let $\alpha := \log_2 3$. For $m \ge 1$,
$m\alpha \notin \mathbb{Z}$ (else $3^m = 2^{m\alpha}$ with $3^m$ odd $>1$), so
$\kappa(m) = \lfloor m\alpha\rfloor + 1$ and
$$\delta := \kappa(m+1)-\kappa(m) = \lfloor (m+1)\alpha\rfloor - \lfloor m\alpha\rfloor \in \{1,2\}$$
because $1 < \alpha < 2$. By (5c) with $K = \kappa(m) \ge m$, $\mathcal{Y}(m,\kappa(m))$ is
nonempty and the maximum $Q(m,\kappa(m))$ is attained, say at $Y$. The class $A_\delta$ is
infinite while $Y$ is finite, so pick $x^\ast \in A_\delta \setminus Y$. Then
$Y' := Y \cup \{x^\ast\}$ has $m+1$ elements, all distinct odd $\ge 7$, and
$\sum_{x\in Y'}a(x) = \kappa(m)+\delta = \kappa(m+1)$, i.e. $Y' \in \mathcal{Y}(m+1,\kappa(m+1))$.
Therefore
$$Q(m+1,\kappa(m+1)) \;\ge\; \Bigl(3+\frac1{x^\ast}\Bigr)\,Q(m,\kappa(m)) \;>\; 3\,Q(m,\kappa(m)),$$
and dividing by $3^{m+1}$ gives $\mathcal{W}(m+1) > \mathcal{W}(m)$. $\square$

**(5f) No naive monotonicity (L-9920.3(6)).** See the worked $(m,K) = (8,13)$ enumeration in
the Statement and in test T7: all seven competing profiles are listed with their exact
$P$ values; the maximiser has $m_1 = 4$, whereas $m_1$ ranges up to $7$. So neither
"maximise $m_1$" nor "push mass to the lowest classes" identifies the optimum, and no
one-parameter greedy rule can replace the exact knapsack. $\square$

### Step 6 — proof of L-9920.4 (computation, completeness, size of the gain)

**(6a) The scan.** For every $m \le 208$ and every $K \in W^*(m)$ (computed exactly from
$N(m), D(m)$), the value $Q(m,K)$ was computed by both implementations of (5d), and $m$ was
declared eliminated iff $2^K > Q(m,K)$ for every such $K$ (including vacuously, when
$W^*(m) = \varnothing$). The two implementations return the same $48$-element set; it contains
all $46$ values of L-9917.3 and adds exactly $\{13, 79\}$ (test T4).

**(6b) Completeness over all $m$.** By (5e), $\mathcal{W}$ is strictly increasing. The exact
comparison $Q(208,\kappa(208)) \ge 2\cdot3^{208}$ (test T6; ratio $1.0001626886\ldots$) gives
$\mathcal{W}(m) \ge \mathcal{W}(208) \ge 2$ for every $m \ge 208$. For such $m$,
$$2^{\kappa(m)} \;\le\; 2\cdot 3^m \;\le\; Q(m,\kappa(m)),$$
using $2^{\kappa(m)-1} \le 3^m$ (definition of $\kappa$), and $3^m < 2^{\kappa(m)}$ holds by
definition; hence $\kappa(m) \in W'(m) \ne \varnothing$ and $m \notin \mathcal{E}'$.
The complementary exact comparison $Q(207,\kappa(207)) < 2\cdot3^{207}$ (ratio
$0.9995490918\ldots$) shows $208$ is the least such threshold, i.e. $m_0' = 208$. Combined
with (6a)'s exhaustive evaluation of $m \le 207$, $\mathcal{E}'$ is exactly the $48$-element
set — a statement about **all** $m \ge 1$. $\square$

**(6c) Why the gain is small.** At $m = 208$ the maximising profile is
$\{m_1{=}135, m_2{=}45, m_3{=}17, m_4{=}6, m_5{=}2, m_6{=}2, m_8{=}1\}$ (so $m_1/m = 0.649$,
$K/m = 1.5865$), and its greedy set runs up to $543$, against L-9917's largest sorted floor
$7+2\cdot207 = 421$. The two element sets therefore differ only in their tail, and since
$\log P = m\log 3 + \sum_x \log(1+1/(3x))$ with $\sum_x 1/(3x)$ a slowly varying functional of
the spread, the resulting width deficit is $\approx 0.015$ bit — reported exactly at thirteen
values of $m$ in test T9. That is enough to close the two near-miss windows at $m = 13$ and
$m = 79$ (where L-9917's margins were $0.05\%$ and $0.008\%$) and to move the threshold
$196 \to 208$, and it is not enough to do anything else.

### Step 7 — proof of L-9920.5 (general floor $F$: no improvement)

**(7a) The bound transfers verbatim.** Assume $(\mathrm{V}_F)$, so every cycle element
satisfies $x_i \ge F+1$ (L-9913.1: cycle elements are counterexamples, hence exceed $F$).
Replacing "$\ge 7$" by "$\ge F+1$" throughout Steps 3–4 (the only properties used were:
distinctness, a common lower bound, and the congruence (DICT)) gives, with
$\beta_t(F) := \min\{x \ge F+1 : x \equiv r_t \bmod 2^{t+1}\}$,
$$3^m < 2^K \le P_F(\pi) \le Q_F(m,K) \le P_{F+1}(m) \le \Bigl(3+\frac1{F+1}\Bigr)^m,$$
the last two being L-9917's floor-$B$ bound with $B = F+1$ (odd for $F \in \{10^6, 10^9\}$)
and L-9913's crude bound.

**(7b) The verdict.** L-9913's conclusion $m \ge m^*(F)$ comes from the least $m$ for which
the constraint can be met. To show the refinement does not raise $m^*(F)$ it suffices to
exhibit, at $m = m^*(F)$ and $K = \kappa(m)$, **one** profile $\pi$ with
$3^m < 2^K \le P_F(\pi)$ — because $P_F(\pi) \le Q_F(m,K)$ makes the refined constraint
satisfied. This is done exactly in test T8 for $(F,m) = (10^6, 2966)$ and
$(10^9, 47468)$ with the profiles displayed in L-9920.5. Since the refined constraint is
*implied by* (strictly stronger than) the crude one, every $m < m^*(F)$ remains excluded;
hence $m^*_{\text{refined}}(F) = m^*(F)$ exactly, for both floors. $\square$

**(7c) Why (the quantitative reason).** For $m \ll B := F+1$, every $Y \in \mathcal{Y}_B(m,K)$
has $\sum_{x\in Y}1/x = m/B - \Theta(m^2/B^2)$: writing $Y$'s sorted elements as
$B + 2c_k$ with distinct integers $0 \le c_0 < c_1 < \dots$, the second-order term is
$-(2/B^2)\sum_k c_k$, and the per-class structure only changes which $\sum_k c_k$ is
achievable. Distinctness alone forces $\sum_k c_k \ge \binom{m}{2}$; the per-class floors
force $\sum_k c_k \ge \tfrac12\sum_t 2^t m_t(m_t-1) \ (\ge \binom m2$, by the domination of
Step 4d(iii)$)$. Either way the correction is a **relative** $O(m/B)$ effect: $3\cdot10^{-3}$
at $F = 10^6$, $4.7\cdot10^{-5}$ at $F = 10^9$. The measured widths (test T8) are
$$F = 10^6:\quad 0.001426343 \ \text{(crude)} \;>\; 0.001422130 \ \text{(distinct)} \;>\; 0.001421757 \ \text{(per-class)}
\;>\; 0.001222861 = \kappa(m) - m\log_2 3,$$
so the constraint is met with $14\%$ to spare and the refinement removes $0.32\%$; at
$F = 10^9$ it removes $0.0052\%$ against $31\%$ of spare. **NULL, as expected.** $\square$

### Step 8 — L-9920.6 (assessment)

Nothing further to prove; the three items of L-9920.6 are, respectively: (i) a restatement of
L-9920.4; (ii) the strict inclusion $\mathcal{E}\subsetneq\mathcal{E}'$ from (6a) together with
$Q \le P(m)$ from (4d)(iii); (iii) the observation that $Q(m,K)$ is a maximum over sets, with
the explicit non-closure of the $m = 13$ maximiser: its element set is
$\{7,9,11,13,15,17,19,23,25,27,29,31,33\}$ and $S(13) = 5 \notin$ set (indeed $5 < 7$), so it
is not $S$-closed and cannot be a cycle set. $\square$

**Q-9920-A (open).** Define
$Q^{\mathrm{cl}}(m,K) := \max\{\prod_{x\in Y}(3+1/x)\}$ over $Y \in \mathcal{Y}(m,K)$ that are
in addition **$S$-closed** ($S(Y) = Y$). Then $Q^{\mathrm{cl}} \le Q$ and every cycle still
satisfies $2^K \le Q^{\mathrm{cl}}(m,K)$. How much smaller is $Q^{\mathrm{cl}}$, and is it
computable without enumerating exponent words? Any bound of the form
$Q^{\mathrm{cl}}(m,\kappa(m)) < 2\cdot3^m$ for $m$ in a long range would extend the
elimination set past $171$; the present file proves that no set-level (order-free) argument
can.

---

## Dependency audit

| Used where | Statement used | Source | Status | Re-derived inline? |
|---|---|---|---|---|
| Step 0 | $S$, $a(x) = \nu_2(3x+1) \ge 1$, step relation $(\ast_i)$ | NOTATION D-9904 | definition | n/a |
| Step 0, 3a | $S$-cycle notation, least period, $K = \sum a_i$ | NOTATION D-9908 | definition | n/a |
| Step 3b | trivial cycle is $(1)$ | NOTATION D-9905 | definition | n/a |
| Step 1 (PF) | $2^K = \prod(3+1/x_i)$ | L-9905.3 | PROVED (fable-02-v4) | **Yes**, 3 lines |
| Step 1 (POS) | $2^K > 3^m$ | L-9905.2 | PROVED (fable-02-v4) | **Yes**, 1 line |
| Step 3b | every element of a nontrivial cycle is $\ge 7$ | L-9906.2 | PROVED (fable-02-v5) | **Yes**, 3 lines |
| Step 2 | dictionary $a(x) = t \iff x \equiv r_t \ (2^{t+1})$ | L-9912.5 | PROVED (fable-02-v14) | **Yes**, proved from scratch + T1 |
| Step 3a | cycle elements pairwise distinct | L-9917.1(1) | PROVED (fable-02-v17) | sketch only (2 lines) — **the one imported proof** |
| Step 4d(iii) | sorted distinct odd $\ge 7$ satisfy $g_k \ge 7+2k$ | L-9917.1(1d) | PROVED | **Yes**, one-line induction |
| Step 4d(iii), 6a | $P(m) = N(m)/D(m)$, $W^*(m)$, $\mathcal{E}$ (46 values), $m_0 = 196$ | L-9917.2–.4 | PROVED | **recomputed** here (T4, T6) |
| L-9920.3(2) | $|W^*(m)| \le 1$ for $m \le 12679$ | L-9917.4(5) | PROVED | recomputed for $m \le 208$ (T9) |
| Step 7a | cycle elements exceed a verified floor $F$ | L-9913.1 + $(\mathrm{V}_F)$ | PROVED (fable-02-v18) | cited, used only in L-9920.5 |
| L-9920.5, .6 | $m^*(10^6) = 2966$, $m^*(10^9) = 47468$ | L-9913.5, .10 | PROVED | cited for comparison only |
| L-9920.6 | $m \le 21$ settled by enumeration | L-9915 | PROVED (fable-02-v10) | comparison only |

**Circularity.** L-9905, L-9906, L-9912, L-9913, L-9915, L-9917 do not cite L-9920. The only
imported *proof* is L-9917.1(1) (distinctness), which is independent of everything proved here
and is itself a two-line group-theoretic fact. Nothing in this file is used to justify any of
its dependencies.

**Not used.** Transcendence/Baker bounds, literature computations, continued fractions, any
result from other packets, floating point in any decision, and — deliberately — the $S$-closure
of the cycle set (see Q-9920-A).

---

## Gap audit

- **Quantifier hygiene.** L-9920.1–.4 are universally quantified over all nontrivial
  $S$-cycles on the positive odd integers of the stated least period; L-9920.1(1,3) and Step 2
  are statements about all integers with no cycle hypothesis; L-9920.5 is conditional on
  $(\mathrm{V}_F)$ and is a *negative* (no-improvement) statement, proved by exhibiting
  explicit witnesses. Nothing is claimed about negative integers (T2 is an audit, not a claim).
- **Hidden finiteness.** The only two places where infinitude could hide are (i) the maximum
  defining $Q(m,K)$ — settled by the explicit support and multiplicity caps of L-9920.3(3),
  which are proved, not assumed; and (ii) the tail $m \ge 208$ — settled by the exchange lemma
  L-9920.3(5) plus one exact integer comparison, so no search range is extrapolated. The item
  list in the knapsack is capped by the same proved bounds, and the cap $\lfloor E/(t-1)\rfloor$
  is an over-estimate (only more items than needed), so no admissible configuration is missed.
- **Empirical vs. universal.** $\mathcal{E}'$ and $m_0' = 208$ are exact integer computations
  backed by proofs of completeness; the only empirical statement in the file is the
  parenthetical asymptotic observation in L-9920.4(3) ("the deficit appears to converge to
  $\approx 0.0157$ bits"), which is explicitly labelled as a finite verification and is used
  nowhere.
- **Boundary cases.** $m = 1$: $W^*(1) = \varnothing$, so $1 \in \mathcal{E}'$ vacuously (and
  the trivial cycle is excluded by the floor, as in L-9917). $K = m$: then $2^K = 2^m < 3^m$,
  excluded by (POS). $E = 0$: the profile is $m_1 = m$ and the knapsack is empty
  ($D(0,0) = 1$). $m_t = 0$: empty products are $1$. The half-open nature of the window
  ($3^m < 2^K \le Q$) is preserved everywhere: strict on the left, non-strict on the right,
  and the elimination test is the strict inequality $2^K > Q(m,K)$.
- **Floating point.** No decision anywhere uses a float. Implementation A works with integers
  scaled by $2^{128}$ and rational enclosures of $\ln 2, \ln 3$ certified by explicit
  alternating-series tail bounds; implementation B uses only integer cross-multiplication.
  Both give the same $48$ values. (This matters: L-9917's reviewer found naive floats
  overflow to NaN around $m \approx 142$, and here the decisive margins at $m = 207, 208$ are
  $4.5\cdot10^{-4}$ and $1.6\cdot10^{-4}$ — well inside what a careless float pipeline would
  get wrong.)
- **Confusion of "not eliminated" with "exists".** $m \notin \mathcal{E}'$ asserts only that
  this method does not exclude $m$; it is not evidence for a cycle. L-9913 excludes every
  $m \le 2965$ under $(\mathrm{V}_{10^6})$.
- **Interchange of limits / infinite processes.** None occur: every product is finite, every
  maximum is over a finite set, and no infinite rewrite sequence is involved.
- **Assumptions equivalent to the conjecture.** None. The only external input beyond
  elementary arithmetic is the floor $x_i \ge 7$ (a three-line fact) and, in L-9920.5 only,
  the finite verification $(\mathrm{V}_F)$ — which is explicitly flagged and confined.
- **What is honestly NOT proved.** (i) The asymptotic constant of $\mathrm{Wd}'(m)$ (only the
  exact values for $m \le 208$ and a numerical observation beyond). (ii) That
  $\mathrm{Wd}'(m)$ has the $\tfrac16\log_2 m$ rate — plausible and numerically clear, but the
  file needs only the monotonicity of $\mathcal{W}$, which *is* proved. (iii) Anything about
  $Q^{\mathrm{cl}}$ (Q-9920-A). (iv) Any improvement in the large-floor regime — L-9920.5 is a
  proved NULL, not an unfinished attempt.

---

## Adversarial tests

Exact-arithmetic verification suite, labels T1–T9. Python 3; integers and
`fractions.Fraction` only; every test asserts. **Script (verbatim):**

```python
#!/usr/bin/env python3
# =====================================================================
# L-9920 verification suite  (author: fable-02-p14)
# Exact integer / Fraction arithmetic only; no floating point is used in
# any decision (floats appear only in clearly labelled display ratios).
# Tests T1..T9; every test asserts, and prints PASS lines.
# =====================================================================
from fractions import Fraction
import itertools, time

# ------------------------------------------------------------ basics
def nu2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c

def aval(x):                                   # a(x) = nu_2(3x+1)
    return nu2(3*x + 1)

def r_of(t):                                   # L-9912.5 base point r_t
    return (2**t - 1)//3 if t % 2 == 0 else (5*2**t - 1)//3

def beta(t, floor=7):                          # least class-t element >= floor
    r = r_of(t); M = 2**(t+1)
    return r if r >= floor else r + ((floor - r + M - 1)//M)*M

def kappa(m):                                  # least K with 2^K > 3^m
    return (3**m).bit_length()

def NmDm(m):                                   # L-9917: P(m) = N(m)/D(m)
    N = D = 1
    for j in range(m):
        N *= 22 + 6*j; D *= 7 + 2*j
    return N, D

def lam(m):                                    # greatest K with 2^K <= P(m)
    N, D = NmDm(m); K = kappa(m) - 1
    while 2**(K+1)*D <= N: K += 1
    return K

# ------------------------------------- certified logarithm enclosures
def atanh_bounds(p, q, N):
    z = Fraction(p, q); z2 = z*z
    s = Fraction(0); term = z
    for k in range(N):
        s += term/(2*k+1); term *= z2
    return s, s + term/((2*N+1)*(1-z2))        # tail < term/((2N+1)(1-z^2))

_l2 = atanh_bounds(1, 3, 200); _l32 = atanh_bounds(1, 5, 200)
LN2_LO, LN2_HI = 2*_l2[0], 2*_l2[1]
LN3_LO, LN3_HI = LN2_LO + 2*_l32[0], LN2_HI + 2*_l32[1]
P_SCALE = 128; TWO_P = 1 << P_SCALE

def u_up(x):
    """integer >= 2^128 * ln(1+1/(3x)) ; ln(1+z) <= z - z^2/2 + z^3/3 (0<z<=1)"""
    z = Fraction(1, 3*x)
    v = (z - z*z/2 + z*z*z/3) * TWO_P
    return -((-v.numerator)//v.denominator)

# ============================================================== T1
def T1():
    print("=== T1  exponent-residue dictionary (L-9912.5) and the class floors beta_t ===")
    for t in range(1, 13):
        r = r_of(t); M = 2**(t+1)
        assert 0 < r < M and r % 2 == 1 and (3*r + 1 - 2**t) % M == 0
        for x in range(1, 2**15, 2):
            assert (aval(x) == t) == (x % M == r), (t, x)
    print("  t=1..12, ALL odd x < 2^15 :  a(x)=t  <=>  x = r_t (mod 2^(t+1))     PASS")
    print("  r_t   , t=1..12 :", [r_of(t) for t in range(1, 13)])
    for t in range(1, 60):
        assert r_of(t+1) % 2**t == r_of(t) % 2**t
    print("  tower r_{t+1} = r_t (mod 2^t) for t <= 59                            PASS")
    print("  beta_t, t=1..14 :", [beta(t) for t in range(1, 15)])
    for t in range(1, 300):
        b = beta(t)
        assert aval(b) == t and b >= 7
        assert (b == r_of(t)) or (r_of(t) < 7 and b == r_of(t) + 2**(t+1))
    small = [(t, r_of(t), beta(t), max(7, r_of(t))) for t in (1, 2, 3, 4, 5, 6)]
    print("  (t, r_t, beta_t, max(7,r_t)) :", small)
    assert beta(2) == 9 and beta(4) == 37
    assert aval(7) != 2 and aval(7) != 4
    print("  CORRECTION: beta_2 = 9 (not 7: a(7)=1) and beta_4 = 37 (not 7);")
    print("              max(7,r_t) is WRONG for t in {2,4}; beta_t = r_t + 2^(t+1)[r_t<7]  PASS")
    S = set()
    for t in range(1, 20):
        b = beta(t); M = 2**(t+1); x = b
        while x < 4000:
            S.add(x); x += M
    assert S == set(range(7, 4000, 2))
    print("  {beta_t + 2^(t+1) j : t>=1, j>=0}  ==  {odd x >= 7}   (checked < 4000)  PASS")

# ============================================================== T2
def Sneg(x):
    y = 3*x + 1; return y // 2**nu2(y)

def T2():
    print()
    print("=== T2  hypothesis-necessity audit on the three negative-domain cycles ===")
    for start in (-1, -5, -17):
        cyc = [start]; x = Sneg(start)
        while x != start: cyc.append(x); x = Sneg(x)
        m = len(cyc); A = [aval(x) for x in cyc]; K = sum(A)
        prof = {}
        for t in A: prof[t] = prof.get(t, 0) + 1
        prod = Fraction(1)
        for x in cyc: prod *= Fraction(3*x+1, x)
        assert prod == 2**K                     # product formula: algebraic, sign-free
        distinct = len(set(cyc)) == m
        dict_ok = all((x - r_of(aval(x))) % 2**(aval(x)+1) == 0 for x in cyc)
        spacing = all(sorted(y for y in cyc if aval(y) == t)[i] -
                      sorted(y for y in cyc if aval(y) == t)[i-1] >= 2**(t+1)
                      for t in prof for i in range(1, prof[t]))
        floor_ok = all(x >= 7 for x in cyc)
        pos = all(x > 0 for x in cyc)
        print("  cycle %-42s m=%d K=%d profile %s" %
              (str(cyc), m, K, {t: prof[t] for t in sorted(prof)}))
        print("     prod(3+1/x_i) = 2^K : True |  2^K > 3^m : %-5s (%d vs %d)"
              % (2**K > 3**m, 2**K, 3**m))
        print("     distinct %s | dictionary %s | per-class spacing %s | positivity %s | floor x>=7 %s"
              % (distinct, dict_ok, spacing, pos, floor_ok))
        assert distinct and dict_ok and spacing
        assert not pos and not floor_ok and not (2**K > 3**m)
    print("  L-9920.1's congruence+spacing half survives verbatim on all three;")
    print("  the FAILING hypotheses are exactly positivity and the floor (as in L-9917).  PASS")

# ==================================== profile-bound machinery (shared)
def build_items(Emax):
    """0/1 items for classes t >= 2 : (excess d=t-1, element x).  Class t supplies
       its first floor(Emax/d) elements; no admissible configuration with excess
       <= Emax can use more than that many elements of class t."""
    items = []; t = 2
    while t - 1 <= Emax:
        d = t - 1; b = beta(t); st = 2**(t+1)
        for j in range(Emax//d): items.append((d, b + st*j))
        t += 1
    return items

def dpA(Emax):                                  # certified log-domain upper bound
    dp = [[None]*(Emax+1) for _ in range(Emax+1)]; dp[0][0] = 0
    for (d, x) in build_items(Emax):
        g = u_up(x)
        for n in range(Emax, 0, -1):
            prev = dp[n-1]; row = dp[n]
            for e in range(Emax, d-1, -1):
                v = prev[e-d]
                if v is not None and (row[e] is None or v + g > row[e]): row[e] = v + g
    return dp

def dpB(Emax, trace=False):                     # exact rational maximum
    dp = [[None]*(Emax+1) for _ in range(Emax+1)]
    dp[0][0] = (1, 1, ()) if trace else (1, 1)
    for (d, x) in build_items(Emax):
        gn, gd = 3*x+1, x
        for n in range(Emax, 0, -1):
            prev = dp[n-1]; row = dp[n]
            for e in range(Emax, d-1, -1):
                v = prev[e-d]
                if v is None: continue
                wn, wd = v[0]*gn, v[1]*gd
                cur = row[e]
                if cur is None or wn*cur[1] > cur[0]*wd:
                    row[e] = (wn, wd, v[2]+(x,)) if trace else (wn, wd)
    return dp

# ============================================================== T3
def brute_Q(m, K, xmax):
    best = None
    for comb in itertools.combinations(range(7, xmax+1, 2), m):
        if sum(aval(x) for x in comb) != K: continue
        p = Fraction(1)
        for x in comb: p *= Fraction(3*x+1, x)
        if best is None or p > best: best = p
    return best

def Qexact(B, preB, m, K, Emax, trace=False):
    E = K - m
    if E < 0 or E > Emax: return None
    best = None
    for n2 in range(0, min(m, E)+1):
        v = B[n2][E]
        if v is None: continue
        wn, wd = v[0]*preB[m-n2][0], v[1]*preB[m-n2][1]
        if best is None or wn*best[1] > best[0]*wd:
            best = (wn, wd, tuple(sorted(v[2] + tuple(7+4*j for j in range(m-n2))))) \
                   if trace else (wn, wd)
    return best

def T3(B, preB, Emax):
    print()
    print("=== T3  the profile DP reproduces brute force over ALL admissible sets ===")
    cases = [(3,5,40),(4,6,60),(4,7,40),(5,8,45),(5,9,45),(5,12,90),
             (6,10,50),(6,11,50),(6,13,70),(7,12,60)]
    for (m, K, xmax) in cases:
        b = brute_Q(m, K, xmax)
        q = Qexact(B, preB, m, K, Emax)
        assert b == Fraction(q[0], q[1]), (m, K, b, q)
    print("  10 cases (m<=7): exhaustive search over subsets of {7,9,...,xmax}")
    print("  agrees with the profile DP in every case                              PASS")

# ============================================================== T4
L9917 = [1,2,3,4,6,7,8,9,11,12,14,16,18,19,21,23,24,26,28,31,33,36,38,43,45,48,50,53,
         55,60,62,65,67,72,77,84,89,96,101,106,113,118,130,142,159,171]

def T4(A, B, preA, preB, Emax, MSTOP):
    print()
    print("=== T4  the refined elimination set, two independent implementations ===")
    elimA = []; elimB = []
    for m in range(1, MSTOP+1):
        ka, la = kappa(m), lam(m)
        if la < ka:
            elimA.append(m); elimB.append(m); continue
        okA = okB = True
        for K in range(ka, la+1):
            E = K - m
            # ---- A: certified upper bound U >= 2^128 * ln(Q/3^m);
            #      eliminate iff  K ln2 - m ln3 > 2^-128 U
            U = None
            for n2 in range(0, min(m, E)+1):
                v = A[n2][E]
                if v is None: continue
                w = v + preA[m-n2]
                if U is None or w > U: U = w
            if U is not None and not ((K*LN2_LO - m*LN3_HI)*TWO_P > U): okA = False
            # ---- B: exact maximum; eliminate iff 2^K > Q(m,K)
            q = Qexact(B, preB, m, K, Emax)
            if q is not None and not (2**K * q[1] > q[0]): okB = False
        if okA: elimA.append(m)
        if okB: elimB.append(m)
    assert elimA == elimB
    print("  implementation A (certified 128-bit log-domain upper bound): %d values" % len(elimA))
    print("  implementation B (exact rational maximum, cross-multiplied): %d values" % len(elimB))
    print("  A == B : True")
    print("  E' =", elimB)
    assert set(L9917) <= set(elimB)
    print("  L-9917's 46 values are all present : True")
    print("  NEW  (E' minus L-9917) :", sorted(set(elimB) - set(L9917)))
    print("  LOST (L-9917 minus E') :", sorted(set(L9917) - set(elimB)))
    print("  max E' = %d ; |E'| = %d" % (max(elimB), len(elimB)))
    # domination Q(m,K) <= P(m)
    bad = 0
    for m in range(1, MSTOP+1):
        N, D = NmDm(m)
        for K in range(kappa(m), lam(m)+1):
            q = Qexact(B, preB, m, K, Emax)
            if q and q[0]*D > N*q[1]: bad += 1
    assert bad == 0
    print("  domination Q(m,K) <= P(m) verified for every m <= %d, every K in W*(m)  PASS" % MSTOP)
    return elimB

# ============================================================== T5
def T5(Bt, preB, Emax):
    print()
    print("=== T5  explicit certificates, and P(profile) computed two ways ===")
    for m in (8, 13, 79, 171):
        K = kappa(m)
        q = Qexact(Bt, preB, m, K, Emax, trace=True)
        num, den, S = q
        prof = {}
        for x in S: prof[aval(x)] = prof.get(aval(x), 0) + 1
        p_set = Fraction(1)
        for x in S: p_set *= Fraction(3*x+1, x)          # way 1: over the element set
        p_pro = Fraction(1)                              # way 2: per-class prefix formula
        for t in sorted(prof):
            b = beta(t); st = 2**(t+1)
            for j in range(prof[t]): p_pro *= Fraction(3*(b+st*j)+1, b+st*j)
        assert p_set == p_pro == Fraction(num, den)
        assert sum(prof.values()) == m and sum(t*c for t, c in prof.items()) == K
        Nm, Dm = NmDm(m)
        print("  m=%-4d K=%-4d profile %s" % (m, K, {t: prof[t] for t in sorted(prof)}))
        print("        2^K*den(Q) = %s" % (2**K*den))
        print("        num(Q)     = %s" % num)
        print("        2^K > Q : %-5s   ratio 2^K/Q = %.9f    [L-9917 at same K: 2^K > P(m) is %s, ratio %.9f]"
              % (2**K*den > num, float(Fraction(2**K*den, num)),
                 2**K*Dm > Nm, float(Fraction(2**K*Dm, Nm))))
    print("  two independent evaluations of P(profile) agree exactly in all cases  PASS")

# ============================================================== T6
def T6(Bt, preB, Emax, MSTOP):
    print()
    print("=== T6  the threshold m0' : Q(m,kappa(m)) >= 2*3^m , and monotonicity ===")
    prev = None; mono = True
    first_fail = 0
    vals = {}
    for m in range(1, MSTOP+1):
        q = Qexact(Bt, preB, m, kappa(m), Emax)
        if q is None: continue
        w = Fraction(q[0], q[1]*3**m)                    # Q(m,kappa(m))/3^m
        vals[m] = w
        if prev is not None and not (w > prev): mono = False
        prev = w
        if w < 2: first_fail = m
    print("  Q(m,kappa(m))/3^m is strictly increasing on 1..%d : %s" % (MSTOP, mono))
    assert mono
    m0 = first_fail + 1
    print("  last m with Q(m,kappa(m)) < 2*3^m : %d   ==>   m0' = %d" % (first_fail, m0))
    for m in (206, 207, 208):
        q = Qexact(Bt, preB, m, kappa(m), Emax)
        print("    m=%d : num(Q)=%s...  2*3^m*den(Q)=%s...  Q>=2*3^m : %-5s ratio %.10f"
              % (m, str(q[0])[:14], str(2*3**m*q[1])[:14], q[0] >= 2*3**m*q[1],
                 float(Fraction(q[0], 2*3**m*q[1]))))
    assert vals[207] < 2 <= vals[208]
    for m in (195, 196):
        N, D = NmDm(m)
        print("    [L-9917] m=%d : N(m) >= 2*3^m*D(m) : %-5s ratio %.10f"
              % (m, N >= 2*3**m*D, float(Fraction(N, 2*3**m*D))))
    print("  m0' = 208  vs  L-9917's m0 = 196                                      PASS")
    return m0

# ============================================================== T7
def T7(Bt, preB, Emax):
    print()
    print("=== T7  structure of the optimisation: the naive 'push mass to low t'")
    print("        heuristic is FALSE (m=8, K=13, all 7 profiles listed) ===")
    m, K = 8, 13
    rows = []
    def gen(t, left_n, left_e, cur):
        if left_e == 0:
            prof = dict(cur); prof[1] = left_n
            if left_n >= 0: rows.append(prof)
            return
        if t - 1 > left_e or left_n == 0: return
        for c in range(0, min(left_n, left_e//(t-1)) + 1):
            gen(t+1, left_n - c, left_e - c*(t-1), cur + ([(t, c)] if c else []))
    gen(2, m, K-m, [])
    best = None
    for prof in rows:
        p = Fraction(1)
        for t in sorted(prof):
            if prof[t] == 0: continue
            b = beta(t); st = 2**(t+1)
            for j in range(prof[t]): p *= Fraction(3*(b+st*j)+1, b+st*j)
        rows_p = (p, prof)
        if best is None or p > best[0]: best = rows_p
        print("    profile %-34s  m_1=%d   P = %.6f" %
              ({t: prof[t] for t in sorted(prof) if prof[t]}, prof[1], float(p)))
    print("  maximiser: %s  (m_1 = %d)" %
          ({t: best[1][t] for t in sorted(best[1]) if best[1][t]}, best[1][1]))
    print("  the profile with the LARGEST m_1 is {1:7, 6:1} and it is NOT the maximiser;")
    print("  the exact maximum is attained at an interior profile.                 PASS")
    q = Qexact(Bt, preB, m, K, Emax)
    assert Fraction(q[0], q[1]) == best[0]
    print("  DP value equals the enumerated maximum                                PASS")

# ============================================================== T8
def beta_floor(t, B):
    r = r_of(t); M = 2**(t+1)
    return r if r >= B else r + ((B - r + M - 1)//M)*M

def prof_product(prof, B):
    num = den = 1
    for t, mt in sorted(prof.items()):
        b = beta_floor(t, B); st = 2**(t+1)
        for j in range(mt):
            x = b + st*j; num *= 3*x+1; den *= x
    return num, den

def T8():
    print()
    print("=== T8  general floor B (L-9920.5): interaction with L-9913 ===")
    import math
    for (F, mstar, prof_extra) in [(10**6, 2966, {1:1814, 2:737, 3:283, 4:100, 5:28, 6:4}),
                                   (10**9, 47468, {1:29026, 2:11797, 3:4539, 4:1591, 5:456, 6:59})]:
        B = F + 1; m = mstar; K = kappa(m)
        assert B % 2 == 1
        assert sum(prof_extra.values()) == m and sum(t*c for t, c in prof_extra.items()) == K
        n12, d12 = prof_product({1: 2*m-K, 2: K-m}, B)
        ng, dg = prof_product(prof_extra, B)
        npl = dpl = 1
        for j in range(m):
            x = B + 2*j; npl *= 3*x+1; dpl *= x
        def l2(nu, de):
            v = nu.bit_length() - de.bit_length()
            return v + math.log2(float(Fraction(nu, de)/Fraction(2)**v))
        print("  F = %d :  m = %d , K = kappa(m) = %d , x_i >= %d" % (F, m, K, B))
        print("    3^m < 2^K                                : %s" % (3**m < 2**K))
        print("    crude   (L-9913)  2^K <= (3+1/B)^m       : %s" % (2**K*B**m <= (3*B+1)**m))
        print("    distinct(L-9917)  2^K <= P_B(m)          : %s" % (2**K*dpl <= npl))
        print("    per-class {1,2}   2^K <= P(profile)      : %s" % (2**K*d12 <= n12))
        print("    per-class greedy  2^K <= P(profile)      : %s" % (2**K*dg <= ng))
        assert 2**K*dg <= ng and 2**K*d12 <= n12 and 2**K*dpl <= npl
        assert 2**K*dpl <= npl and ng*dpl <= npl*dg          # Q <= plain distinctness
        # widths, display only
        wc = l2((3*B+1)**m, B**m) - m*math.log2(3)
        wp = l2(npl, dpl) - m*math.log2(3)
        wg = l2(ng, dg) - m*math.log2(3)
        f = K - m*math.log2(3)
        print("    [display] width of the K-window in bits:  crude %.9f | distinct %.9f | per-class %.9f"
              % (wc, wp, wg))
        print("              needed: K - m*log2(3) = %.9f  (must be <= width)" % f)
        print("              per-class width is %.4f%% of the crude width; the constraint"
              % (100*wg/wc))
        print("              would have to lose %.2f%% to eliminate m = %d." % (100*(1-f/wg), m))
        print("    ==> m = %d still admissible: NO improvement to L-9913's bound." % m)
    print("  L-9920.5 verdict: NULL in the large-floor regime                      PASS")

# ============================================================== T9
def T9(Bt, preB, Emax, MSTOP):
    print()
    print("=== T9  how much narrower is the refined window?  (exact values, float display) ===")
    import math
    def l2(n, d):
        v = n.bit_length()-d.bit_length()
        return v + math.log2(float(Fraction(n, d)/Fraction(2)**v))
    sizes = [lam(m)-kappa(m)+1 for m in range(1, MSTOP+1)]
    print("  |W*(m)| for m <= %d takes only the values %s : the L-9917 window is a"
          % (MSTOP, sorted(set(max(s, 0) for s in sizes))))
    print("  singleton or empty throughout the scan range, so the refinement can only")
    print("  turn a singleton into the empty set -- it never removes a second K.")
    print("    m     Wd(m)=log2(P(m)/3^m)   Wd'(m)=log2(Q(m,kappa)/3^m)    gain (bits)   m_1/m of maximiser")
    for m in (8, 13, 20, 40, 79, 100, 171, 195, 196, 200, 206, 207, 208):
        N, D = NmDm(m); K = kappa(m)
        q = Qexact(Bt, preB, m, K, Emax, trace=True)
        prof = {}
        for x in q[2]: prof[aval(x)] = prof.get(aval(x), 0)+1
        print("  %4d     %12.6f          %14.6f          %10.6f        %6.4f"
              % (m, l2(N, D)-m*math.log2(3), l2(q[0], q[1])-m*math.log2(3),
                 (l2(N, D)-l2(q[0], q[1])), prof.get(1, 0)/m))
    q = Qexact(Bt, preB, 208, kappa(208), Emax, trace=True)
    print("  at m=208 the maximiser's largest element is %d, against L-9917's largest"
          % max(q[2]))
    print("  sorted floor 7+2*207 = %d : the per-class floors are only mildly more spread." % (7+2*207))
    print("  the gain is ~0.015 bit and (numerically) tends to a constant: the refined")
    print("  width keeps L-9917's (1/6)log2(m) rate, with the constant lowered by ~0.015.")

# ============================================================== main
def main():
    t0 = time.time()
    MSTOP = 208
    Emax = max(lam(m) - m for m in range(1, MSTOP+1))
    T1(); T2()
    A = dpA(Emax); Bx = dpB(Emax); Bt = dpB(Emax, trace=True)
    preA = [0]; preB = [(1, 1)]
    for j in range(MSTOP+2):
        x = 7+4*j
        preA.append(preA[-1] + u_up(x))
        preB.append((preB[-1][0]*(3*x+1), preB[-1][1]*x))
    print()
    print("scan parameters: m <= %d, Emax = K-m <= %d, items (classes t>=2) = %d, "
          "largest class t = %d" % (MSTOP, Emax, len(build_items(Emax)), Emax+1))
    T3(Bx, preB, Emax)
    T4(A, Bx, preA, preB, Emax, MSTOP)
    T5(Bt, preB, Emax)
    T6(Bx, preB, Emax, MSTOP)
    T7(Bx, preB, Emax)
    T8()
    T9(Bt, preB, Emax, MSTOP)
    print()
    print("ALL TESTS PASSED   (total %.1f s)" % (time.time()-t0))

main()
```

**Captured output (verbatim):**

```text
=== T1  exponent-residue dictionary (L-9912.5) and the class floors beta_t ===
  t=1..12, ALL odd x < 2^15 :  a(x)=t  <=>  x = r_t (mod 2^(t+1))     PASS
  r_t   , t=1..12 : [3, 1, 13, 5, 53, 21, 213, 85, 853, 341, 3413, 1365]
  tower r_{t+1} = r_t (mod 2^t) for t <= 59                            PASS
  beta_t, t=1..14 : [7, 9, 13, 37, 53, 21, 213, 85, 853, 341, 3413, 1365, 13653, 5461]
  (t, r_t, beta_t, max(7,r_t)) : [(1, 3, 7, 7), (2, 1, 9, 7), (3, 13, 13, 13), (4, 5, 37, 7), (5, 53, 53, 53), (6, 21, 21, 21)]
  CORRECTION: beta_2 = 9 (not 7: a(7)=1) and beta_4 = 37 (not 7);
              max(7,r_t) is WRONG for t in {2,4}; beta_t = r_t + 2^(t+1)[r_t<7]  PASS
  {beta_t + 2^(t+1) j : t>=1, j>=0}  ==  {odd x >= 7}   (checked < 4000)  PASS

=== T2  hypothesis-necessity audit on the three negative-domain cycles ===
  cycle [-1]                                       m=1 K=1 profile {1: 1}
     prod(3+1/x_i) = 2^K : True |  2^K > 3^m : False (2 vs 3)
     distinct True | dictionary True | per-class spacing True | positivity False | floor x>=7 False
  cycle [-5, -7]                                   m=2 K=3 profile {1: 1, 2: 1}
     prod(3+1/x_i) = 2^K : True |  2^K > 3^m : False (8 vs 9)
     distinct True | dictionary True | per-class spacing True | positivity False | floor x>=7 False
  cycle [-17, -25, -37, -55, -41, -61, -91]        m=7 K=11 profile {1: 5, 2: 1, 4: 1}
     prod(3+1/x_i) = 2^K : True |  2^K > 3^m : False (2048 vs 2187)
     distinct True | dictionary True | per-class spacing True | positivity False | floor x>=7 False
  L-9920.1's congruence+spacing half survives verbatim on all three;
  the FAILING hypotheses are exactly positivity and the floor (as in L-9917).  PASS

scan parameters: m <= 208, Emax = K-m <= 122, items (classes t>=2) = 609, largest class t = 123

=== T3  the profile DP reproduces brute force over ALL admissible sets ===
  10 cases (m<=7): exhaustive search over subsets of {7,9,...,xmax}
  agrees with the profile DP in every case                              PASS

=== T4  the refined elimination set, two independent implementations ===
  implementation A (certified 128-bit log-domain upper bound): 48 values
  implementation B (exact rational maximum, cross-multiplied): 48 values
  A == B : True
  E' = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48, 50, 53, 55, 60, 62, 65, 67, 72, 77, 79, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]
  L-9917's 46 values are all present : True
  NEW  (E' minus L-9917) : [13, 79]
  LOST (L-9917 minus E') : []
  max E' = 171 ; |E'| = 48
  domination Q(m,K) <= P(m) verified for every m <= 208, every K in W*(m)  PASS

=== T5  explicit certificates, and P(profile) computed two ways ===
  m=8    K=13   profile {1: 4, 2: 3, 3: 1}
        2^K*den(Q) = 8939234304000
        num(Q)     = 8833287823360
        2^K > Q : True    ratio 2^K/Q = 1.011994003    [L-9917 at same K: 2^K > P(m) is True, ratio 1.009464018]
  m=13   K=21   profile {1: 7, 2: 4, 3: 2}
        2^K*den(Q) = 42160477185047789568000
        num(Q)     = 41941581246154670080000
        2^K > Q : True    ratio 2^K/Q = 1.005219067    [L-9917 at same K: 2^K > P(m) is False, ratio 0.999507595]
  m=79   K=126  profile {1: 50, 2: 18, 3: 7, 4: 2, 5: 1, 6: 1}
        2^K*den(Q) = 27531751118714442729680749173846310350282825372488638506607635604712922709396452617988791978784349212490963612006100178888925291913969614612067275681941380407945592832000000000000000000
        num(Q)     = 27311648409449808818672556454648251479953886401170579020794000006327675221220091655062325761512384912598124553268407660657927235701761510124111161269091470062020198400000000000000000000
        2^K > Q : True    ratio 2^K/Q = 1.008058932    [L-9917 at same K: 2^K > P(m) is False, ratio 0.999916890]
  m=171  K=272  profile {1: 110, 2: 38, 3: 14, 4: 5, 5: 2, 6: 1, 8: 1}
        2^K*den(Q) = 28510867684359004384469725314638957013370435637913156402094555714769294329602623425168085450793244838447509638726534006326334324569434778202928374860151779040777288772876111184038372541066931523655748528052179823983147702721346550178179425315263647800693481634286207449684289626297069802502030301569796683567339115674894938505035267567462132914391948095492805752756019271340795188798612688584151958686374297600000000000000000000000000000000000000000000
        num(Q)     = 28178373584817045630830816691522672983448059390341916460317621447392064575769570901938581382092296074072235506356354738620922488288607894247822437755496599262191670597927308021353715887937511106516032149586808587063668877433873566671192208087272240575276749934443669068687799269646810789104783658724057674543576214396365608196726537824088662210352058202480791865950253667802150766185278164781691046011777056768000000000000000000000000000000000000000000
        2^K > Q : True    ratio 2^K/Q = 1.011799620    [L-9917 at same K: 2^K > P(m) is True, ratio 1.001777194]
  two independent evaluations of P(profile) agree exactly in all cases  PASS

=== T6  the threshold m0' : Q(m,kappa(m)) >= 2*3^m , and monotonicity ===
  Q(m,kappa(m))/3^m is strictly increasing on 1..208 : True
  last m with Q(m,kappa(m)) < 2*3^m : 207   ==>   m0' = 208
    m=206 : num(Q)=38180901428110...  2*3^m*den(Q)=38233395935954...  Q>=2*3^m : False ratio 0.9986269986
    m=207 : num(Q)=41388097148071...  2*3^m*den(Q)=41406767798638...  Q>=2*3^m : False ratio 0.9995490918
    m=208 : num(Q)=67462598351356...  2*3^m*den(Q)=67451624743982...  Q>=2*3^m : True  ratio 1.0001626886
    [L-9917] m=195 : N(m) >= 2*3^m*D(m) : False ratio 0.9999345218
    [L-9917] m=196 : N(m) >= 2*3^m*D(m) : True  ratio 1.0007740974
  m0' = 208  vs  L-9917's m0 = 196                                      PASS

=== T7  structure of the optimisation: the naive 'push mass to low t'
        heuristic is FALSE (m=8, K=13, all 7 profiles listed) ===
    profile {1: 7, 6: 1}                        m_1=7   P = 7767.816706
    profile {1: 6, 3: 1, 4: 1}                  m_1=6   P = 7828.977912
    profile {1: 6, 2: 1, 5: 1}                  m_1=6   P = 7894.629718
    profile {1: 5, 2: 1, 3: 2}                  m_1=5   P = 8039.682111
    profile {1: 5, 2: 2, 4: 1}                  m_1=5   P = 7972.752542
    profile {1: 4, 2: 3, 3: 1}                  m_1=4   P = 8094.909630
    profile {1: 3, 2: 5}                        m_1=3   P = 7898.504350
  maximiser: {1: 4, 2: 3, 3: 1}  (m_1 = 4)
  the profile with the LARGEST m_1 is {1:7, 6:1} and it is NOT the maximiser;
  the exact maximum is attained at an interior profile.                 PASS
  DP value equals the enumerated maximum                                PASS

=== T8  general floor B (L-9920.5): interaction with L-9913 ===
  F = 1000000 :  m = 2966 , K = kappa(m) = 4701 , x_i >= 1000001
    3^m < 2^K                                : True
    crude   (L-9913)  2^K <= (3+1/B)^m       : True
    distinct(L-9917)  2^K <= P_B(m)          : True
    per-class {1,2}   2^K <= P(profile)      : True
    per-class greedy  2^K <= P(profile)      : True
    [display] width of the K-window in bits:  crude 0.001426343 | distinct 0.001422130 | per-class 0.001421757
              needed: K - m*log2(3) = 0.001222861  (must be <= width)
              per-class width is 99.6785% of the crude width; the constraint
              would have to lose 13.99% to eliminate m = 2966.
    ==> m = 2966 still admissible: NO improvement to L-9913's bound.
  F = 1000000000 :  m = 47468 , K = kappa(m) = 75235 , x_i >= 1000000001
    3^m < 2^K                                : True
    crude   (L-9913)  2^K <= (3+1/B)^m       : True
    distinct(L-9917)  2^K <= P_B(m)          : True
    per-class {1,2}   2^K <= P(profile)      : True
    per-class greedy  2^K <= P(profile)      : True
    [display] width of the K-window in bits:  crude 0.000022827 | distinct 0.000022826 | per-class 0.000022826
              needed: K - m*log2(3) = 0.000015768  (must be <= width)
              per-class width is 99.9948% of the crude width; the constraint
              would have to lose 30.92% to eliminate m = 47468.
    ==> m = 47468 still admissible: NO improvement to L-9913's bound.
  L-9920.5 verdict: NULL in the large-floor regime                      PASS

=== T9  how much narrower is the refined window?  (exact values, float display) ===
  |W*(m)| for m <= 208 takes only the values [0, 1] : the L-9917 window is a
  singleton or empty throughout the scan range, so the refinement can only
  turn a singleton into the empty set -- it never removes a second K.
    m     Wd(m)=log2(P(m)/3^m)   Wd'(m)=log2(Q(m,kappa)/3^m)    gain (bits)   m_1/m of maximiser
     8         0.306711                0.303099            0.003611        0.5000
    13         0.396198                0.387978            0.008221        0.5385
    20         0.483060                0.471297            0.011763        0.6500
    40         0.633093                0.622710            0.010383        0.6250
    79         0.788082                0.776382            0.011700        0.6329
   100         0.842857                0.829821            0.013036        0.6300
   171         0.968851                0.954489            0.014362        0.6433
   195         0.999906                0.985190            0.014716        0.6513
   196         1.001116                0.986123            0.014993        0.6531
   200         1.005900                0.990780            0.015119        0.6550
   206         1.012901                0.998018            0.014883        0.6505
   207         1.014048                0.999349            0.014699        0.6473
   208         1.015190                1.000235            0.014955        0.6490
  at m=208 the maximiser's largest element is 543, against L-9917's largest
  sorted floor 7+2*207 = 421 : the per-class floors are only mildly more spread.
  the gain is ~0.015 bit and (numerically) tends to a constant: the refined
  width keeps L-9917's (1/6)log2(m) rate, with the constant lowered by ~0.015.

ALL TESTS PASSED   (total 29.2 s)
```

*(The final wall-clock figure is the only line that varies between runs; every other line
above is reproduced byte-for-byte by the script as printed.)*

**What each test could have exposed, and did not.**

- **T1** — a wrong dictionary or a wrong class floor. It *did* expose the sketch's
  $\max(7,r_t)$ (correction C1), and it confirms the classes partition the odd integers
  $\ge 7$, which is what makes $Q$ a maximum over *sets* (Step 4d).
- **T2** — a hypothesis smuggled in without being used. The congruence and spacing halves of
  L-9920.1 hold on all three negative cycles; what fails is positivity (hence
  $2^K > 3^m$) and the floor, exactly as in L-9917. The product formula holds there verbatim,
  confirming it is sign-free.
- **T3** — an error in the reduction from "sets" to "profiles" or in the knapsack. Brute force
  over *all* subsets of $\{7,9,\dots,x_{\max}\}$ reproduces the DP in every case.
- **T4** — a wrong elimination set. Two implementations with disjoint failure modes (certified
  scaled-integer logs vs. exact rational cross-multiplication) agree exactly, and the
  containment of L-9917's $46$ values — which is *forced* by Step 4d(iii) — holds; had it
  failed, either this file or L-9917 would have contained an error, and the file would have
  reported it loudly. It did not fail.
- **T5** — a mis-stated certificate. $P(\text{profile})$ is computed both from the profile
  formula and from the explicit element list; they agree as exact rationals.
- **T6** — the threshold. The two decisive comparisons at $m = 207, 208$ differ from equality
  by $4.5\cdot10^{-4}$ and $1.6\cdot10^{-4}$ relative — floats in double precision would be
  numerically adequate here but *not* obviously so, and the file uses none.
- **T7** — the structural assumption behind the optimisation. It refutes the greedy heuristic.
- **T8** — the large-floor claim. Explicit exact witnesses at both floors.
- **T9** — over-claiming the size of the improvement. It shows the gain is $\approx 0.015$ bit.

---

## Remaining uncertainty

1. **The one imported proof.** Distinctness of a least-period-$m$ cycle's elements
   (L-9917.1(1), PROVED) is used but only sketched here. It is elementary and independently
   re-checked in L-9906 Step 0 P0; if it failed, L-9917 would fall with this file.
2. **Asymptotics of $\mathrm{Wd}'$.** The claim that the refinement is worth a *constant*
   ($\approx 0.0157$ bit) rather than a growing amount is a numerical observation over
   $m \le 1000$, explicitly labelled as such and used nowhere. The proved facts are: the
   exact values for $m \le 208$; monotonicity of $\mathcal{W}$; and $Q \le P(m)$ (so the
   deficit is $\ge 0$).
3. **Optimality of the maximisers.** Implementation B computes an exact maximum, but its
   correctness rests on the reduction of Step 5d (class-$1$ prefix + knapsack over classes
   $\ge 2$). That reduction is proved, and independently checked against brute force for
   $m \le 7$ (T3) and against implementation A for all $m \le 208$ (T4). A reviewer wanting a
   third route could enumerate all profiles directly for, say, $m \le 30$ (as T7 does at
   $m = 8$) — this is cheap and I recommend it.
4. **$\mathcal{E}'$ is not a new theorem about cycles.** Every $m \in \mathcal{E}'$ is already
   excluded by L-9913 under $(\mathrm{V}_{10^6})$. The value of $\mathcal{E}'$ is that it is
   unconditional and enumeration-free, and that it pins the ceiling of the method.
5. **I am confident** in: L-9920.1, .2, .3 (all proofs are short and elementary), the
   computation of $\mathcal{E}'$ and $m_0'$ (two implementations, exact arithmetic, proved
   completeness), and the NULL of L-9920.5. I am **least** confident in the calibration
   sentence of L-9920.4(3) (asymptotic constant), which is flagged as an observation.

---

## Suggested next attack

1. **Attack the order structure (Q-9920-A).** The single largest unexploited fact is
   $S(\mathcal{C}) = \mathcal{C}$. A tractable first step: for each $x \in \mathcal{C}$ with
   $a(x) = t$, the successor is $(3x+1)/2^t$, so $\mathcal{C}$ is closed under an explicit
   *map*, not just a set of congruence conditions. Even the weak consequence "for every
   $x \in \mathcal{C}$ with $a(x) = t$, the integer $(3x+1)/2^t$ also lies in $\mathcal{C}$
   and hence is $\ge 7$ and lies in one of the classes" prunes the maximisers found here
   massively (the $m=13$ maximiser fails it at $x = 13$). Quantifying how much
   $Q^{\mathrm{cl}}$ drops is the natural sequel and is the only route by which a set-product
   argument could pass $m = 171$.
2. **A second-order dictionary.** L-9912's Gap audit notes that the dictionary says nothing
   about *consecutive* exponents. Composing $S$ with the residue classes gives conditions on
   pairs $(a_i, a_{i+1})$ — e.g. $a_i = 1$ forces $x_{i+1} = (3x_i+1)/2$ with an explicit
   class mod $2^{a_{i+1}+1}$, which is a condition on $x_i$ mod $2^{a_i + a_{i+1}+1}$. Turning
   that into a floor for *pairs* would strengthen $Q$ in a way that is still order-free enough
   to be computable.
3. **Verification targets in this file (for the reviewer).** (i) Step 4d(ii) — the claim that
   *every* $Y \in \mathcal{Y}(m,K)$ is dominated by $P(\pi_Y)$, which is where a subtle
   multiset/set confusion would hide; (ii) Step 5c — the multiplicity cap
   $m_t \le \lfloor E/(t-1)\rfloor$ and the support cap $t \le E+1$, which are what make the
   knapsack finite and complete; (iii) Step 5e — the exchange lemma, in particular the
   $\delta = 2$ case and the existence of an unused element $x^\ast \in A_\delta$; (iv) the
   two razor-thin comparisons at $m = 207$ and $m = 208$ (recompute independently); (v) the
   two new eliminations $m = 13$ and $m = 79$, ideally by direct enumeration of all profiles
   at $(13,21)$ and $(79,126)$ rather than through the knapsack.
4. **Cheap extension.** Raising the proved floor from $7$ to any *proved* (not verified-sweep)
   value $B$ would move $m_0'$ linearly in $B$ (L-9917.4(6) applies verbatim to $Q$, since
   $Q \le P_B(m)$). No such improvement of the floor is currently available in-repo without
   invoking a finite verification.
