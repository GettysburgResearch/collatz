# L-9913 — An unconditional lower bound on the length of a nontrivial Collatz cycle

```text
Claim ID:      L-9913
Title:         Unconditional lower bounds for nontrivial Syracuse cycles: every
               nontrivial cycle has at least 2966 odd elements (elementary, no
               Baker-type input), with the verified floor F as a free parameter
Status:        PROPOSED
Authoring agent:   fable-02-p8
Reviewing agents:  (none yet)
Created:       2026-07-25
Last updated:  2026-07-25
Dependencies:  research/foundations/NOTATION.md (D-9901, D-9902, D-9903, D-9904,
                 D-9905, D-9908, D-9909; empty-sum conventions).
               L-9905 (Status: PROVED, fable-02-v4) — LOAD-BEARING: L-9905.2
                 (2^K > 3^m) and the inequality chain of L-9905.3
                 (0 < K ln2 - m ln3 <= m/(3 x_min)), equivalently L-9905.5.
                 Both are restated verbatim where used.
               L-9909 (Status: PROVED, fable-02-v7) — LOAD-BEARING: only its
                 finite-verification record X-9901 ("every n <= 10^6 reaches 1
                 under C"). Nothing else from L-9909 is used.
               L-9906 (Status: PROVED, fable-02-v5) and L-9915 (Status: PROVED,
                 fable-02-v10; its header read PROPOSED when this file was
                 assigned) — used ONLY in the combination remark of L-9913.6,
                 which is strictly weaker than this file's own bound; no proof
                 here depends on them.
               L-9910 (Status: PROVED, fable-02-v13) — used ONLY in the optional
                 dichotomy corollary L-9913.8 (its certified continued fraction
                 of log2 3 and Legendre's criterion). The Main Theorem does not
                 use continued-fraction theory at all.
               L-9911 (Status: PROVED, fable-02-v9) — related only. The single
                 fact needed here ("cycle elements are counterexamples") is
                 proved inline in L-9913.1, so no status is inherited.
Scope:         All S-cycles on the positive odd integers (D-9908). Everything is
               stated for an arbitrary integer floor F >= 2 such that every
               n <= F reaches 1 under C; the Main Theorem instantiates F = 10^6
               (the in-repo verified value, X-9901). The bound is on the least
               period m of the S-cycle, on K = sum of exponents, and on the
               induced C- and T-cycle lengths. NO transcendence (Baker-type)
               input is used, and no claim whatsoever is made about the bounds
               reachable in the literature.
Related counterexample candidates: none
```

---

## Statement

Throughout, $S$ is the Syracuse map (D-9904) on the positive odd integers,
$S(x) = (3x+1)/2^{\nu_2(3x+1)}$; an $S$-cycle is written as in D-9908,
$x_1 \to x_2 \to \dots \to x_m \to x_1$ with **least** period $m \ge 1$, exponents
$a_i := \nu_2(3x_i+1) \ge 1$, $K := \sum_{i=1}^m a_i$, and
$x_{\min} := \min_i x_i$. "Nontrivial" means: not the trivial cycle $(1)$ of D-9905.
Set
$$\alpha \;:=\; \log_2 3 \;=\; \frac{\ln 3}{\ln 2}, \qquad
f(m) \;:=\; \lceil m\alpha\rceil - m\alpha \;=\; 1 - \{m\alpha\} \in (0,1)
\quad (m \in \mathbb{Z}^{+}),$$
and, for an integer $F \ge 2$,
$$\varepsilon_0(F) \;:=\; \frac{1000}{3 \cdot 693 \cdot F} \;=\; \frac{1000}{2079\,F}
\;\;>\;\; \varepsilon(F) \;:=\; \frac{1}{3F\ln 2}$$
(the displayed inequality $\varepsilon_0 > \varepsilon$ is Corollary A1 below,
i.e. $\ln 2 > 693/1000$).

> **Standing floor hypothesis $\mathrm{(V}_F)$.** $F \ge 2$ is an integer such that
> **every** $n \in \mathbb{Z}^{+}$ with $n \le F$ reaches $1$ under $C$ (D-9905).
> This is a *finite verification*, never a theorem of this file; the value
> $F = 10^6$ is discharged by X-9901 (recorded in L-9909, PROVED), and larger
> values are discharged by the finite verification X-9913 of L-9913.10 below.
> Every statement tagged $\mathrm{(V}_F)$ is unconditional once the corresponding
> finite verification is accepted; nothing else in this file is conditional.

**L-9913.1 (counterexample floor).** Let $x_1 \to \dots \to x_m \to x_1$ be a
nontrivial $S$-cycle. Then $x_i \neq 1$ for every $i$, and **every** $x_i$ is a
Collatz counterexample (D-9909), i.e. $1 \notin O_C(x_i)$. Consequently, under
$\mathrm{(V}_F)$, $x_{\min} \ge F+1 > F$; in particular $x_{\min} > 10^6$ by X-9901.

**L-9913.2 (the squeeze).** Assume $\mathrm{(V}_F)$. Then **every** nontrivial
$S$-cycle satisfies
$$0 \;<\; K - m\alpha \;<\; \varepsilon_0(F)\, m .$$

**L-9913.3 (reduction to a fractional-part condition).** For an integer $m \ge 1$
define the **admissibility predicate**
$$\mathrm{Adm}_F(m) \;:\Longleftrightarrow\; \lceil m\alpha \rceil - m\alpha \;\le\; \varepsilon_0(F)\,m
\;\Longleftrightarrow\; 1 - \{m\alpha\} \;\le\; \varepsilon_0(F)\, m .$$
Then:

1. **(unconditional, every integer $m \ge 1$.)** $m\alpha \notin \mathbb{Z}$, so
   $\lceil m\alpha\rceil = \lfloor m\alpha\rfloor + 1$ and
   $f(m) = 1 - \{m\alpha\} \in (0,1)$; moreover
   $\mathrm{Adm}_F(q) \Rightarrow \mathrm{Adm}_F(tq)$ for all integers
   $q, t \ge 1$ (upward closure), and
   $$m^*(F) \;:=\; \min\{\, m \ge 1 : \mathrm{Adm}_F(m)\,\}$$
   is well defined, with $m^*(F) \ge 2$ for every $F \ge 2$;
2. **(assuming $\mathrm{(V}_F)$, every nontrivial $S$-cycle.)** $\mathrm{Adm}_F(m)$
   holds; moreover if $m < 1/\varepsilon_0(F)$ then $K = \lceil m\alpha\rceil$
   exactly;
3. **(scale invariance / reduced denominator; same hypotheses as 2.)** Writing
   $K/m = p/q$ in lowest terms ($q = m/\gcd(K,m)$), $\mathrm{Adm}_F(q)$ also holds
   — the constraint sees only the reduced denominator;
4. consequently every nontrivial $S$-cycle satisfies
   $$m \;\ge\; q \;\ge\; m^*(F).$$

**L-9913.4 (exact decision procedures).** Let $\varepsilon_0 = P/Q$ with
$P, Q \in \mathbb{Z}^{+}$, and let $m \ge 1$, $K$ be integers.

1. **(Pure integer form.)**
   $\;K - m\alpha \le \varepsilon_0 m \iff 2^{\,QK - Pm} \le 3^{\,Qm}$
   (an inequality between positive rationals; both sides are integers when
   $QK \ge Pm$).
2. **(Enclosure form.)** Let $L < \alpha < U$ be rationals and put
   $r := \dfrac{K}{m} - \varepsilon_0 \in \mathbb{Q}$. Then
   $L \ge r \Rightarrow K - m\alpha < \varepsilon_0 m$, and
   $U \le r \Rightarrow K - m\alpha > \varepsilon_0 m$.
3. **(Ceiling.)** If $\lceil mL \rceil = \lceil mU \rceil$ then
   $\lceil m\alpha\rceil$ equals this common value.
4. **(Certified enclosure.)** $\;3^{111202} > 2^{176251}$ and
   $3^{190537} < 2^{301994}$; hence
   $$L_0 := \frac{176251}{111202} \;<\; \alpha \;<\; \frac{301994}{190537} =: U_0,
     \qquad U_0 - L_0 = \frac{1}{21188095474} < 4.721 \cdot 10^{-11}.$$

> **Correction flag (against the assigning sketch).** Item 1 is exactly the
> "pure big-integer comparison" proposed in the assignment, and it is **correct**;
> but it is **not executable** at the parameters of this problem. For $F = 10^6$
> one has $\varepsilon_0 = 1/2079000$ in lowest terms, so $Q = 2079000$, and at
> $m \approx 3000$ the number $3^{Qm}$ has $Qm\log_2 3 \approx 9.8 \cdot 10^{9}$
> binary digits ($\approx 1.2$ GB per side, per candidate $m$). The operative test
> in this file is therefore item 2 with the enclosure of item 4: **equally exact**,
> with the entire theorem resting on exactly **two** big-integer inequalities
> (item 4, $\approx 3\cdot 10^{5}$ bits each, checked in milliseconds) plus
> small-integer cross-multiplications ($< 10^{16}$) for each $m$.

**L-9913.5 (the computation; exhaustive finite verification).** For $F = 10^6$
(so $\varepsilon_0 = 1/2079000$):
$$\boxed{\,m^*(10^6) \;=\; 2966\,}, \qquad \lceil 2966\,\alpha\rceil = 4701,
\qquad \gcd(4701, 2966) = 1 .$$
Explicitly: $\mathrm{Adm}_{10^6}(m)$ is **false** for every $1 \le m \le 2965$ and
**true** for $m = 2966$. Displayed certificates (both reduce to one
cross-multiplication of integers $< 10^{16}$, given L-9913.4(4)):

* **Winner $m = 2966$, $K = 4701$:**
  $r = \frac{4701}{2966} - \frac{1}{2079000} = \frac{4886688017}{3083157000}$ and
  $$L_0 \ge r \iff 176251 \cdot 3083157000 \;\ge\; 4886688017 \cdot 111202
  \iff 543\,409\,504\,407\,000 \;\ge\; 543\,409\,480\,866\,434 . \checkmark$$
* **Runner-up $m = 2301$, $K = 3647$** (the last and closest failure):
  $r = \frac{3647}{2301} - \frac{1}{2079000} = \frac{2527370233}{1594593000}$ and
  $$U_0 \le r \iff 301994 \cdot 1594593000 \;\le\; 2527370233 \cdot 190537
  \iff 481\,557\,518\,442\,000 \;\le\; 481\,557\,542\,085\,121 . \checkmark$$

**Main Theorem (L-9913.6).** Assume $\mathrm{(V}_{10^6})$, i.e. X-9901. Then every
nontrivial $S$-cycle satisfies
$$m \;\ge\; 2966, \qquad q := \frac{m}{\gcd(K,m)} \;\ge\; 2966, \qquad K \;\ge\; 4701,$$
its elements are $\ge 2966$ distinct odd integers each $> 10^6$, the induced
$T$-cycle has least period $K \ge 4701$, and the induced $C$-cycle has least
period $K + m \ge 7667$. Combining with L-9906 and L-9915 (no nontrivial
$S$-cycle with $m \le 21$) changes nothing: $\max(22, m^*) = 2966$; and the
"PROVED-dependencies-only" version of the combination — which at assignment time
meant $\max(7, m^*)$ using L-9906 alone — is likewise $2966$. **L-9913 subsumes
both.**

**L-9913.7 ($C$- and $T$-cycle lengths).** Let $x_1 \to \dots \to x_m \to x_1$ be
any $S$-cycle. Then
$$\mathcal{O}_C \;:=\; \{x_1, \dots, x_m\} \;\cup\;
\Bigl\{ \tfrac{3x_i+1}{2^{\,j}} \;:\; 1 \le i \le m,\ 0 \le j \le a_i - 1 \Bigr\}$$
consists of exactly $K + m$ distinct positive integers and is a $C$-cycle of
least period $K+m$; removing the $m$ elements $3x_i + 1$ leaves a $T$-cycle of
least period $K$. Conversely every nontrivial $C$-cycle arises this way from a
nontrivial $S$-cycle.

**L-9913.8 (convergent dichotomy; optional, uses L-9910).** Assume
$\mathrm{(V}_{10^6})$. For every nontrivial $S$-cycle, with $K/m = p/q$ in lowest
terms, exactly one of the following holds:

* **(a)** $p/q$ is a convergent of the continued fraction of $\alpha$. Then it is
  an **odd-index** convergent (those lie above $\alpha$), so by L-9910.3
  $q \in \{1, 5, 41, 306, 15601, 79335, 190537, \dots\}$; combined with
  $q \ge 2966$ (L-9913.6) this forces
  $$q \ge 15601, \qquad m \ge 15601, \qquad K \ge 24727 .$$
* **(b)** $p/q$ is not a convergent of $\alpha$. Then Legendre's criterion
  (L-9910.1) gives $|\alpha - p/q| \ge 1/(2q^2)$, whence
  $q^2 > 1/(2\varepsilon_0) = 1\,039\,500$ and $q \ge 1020$ — **weaker** than the
  unconditional $q \ge 2966$ of L-9913.6, which therefore governs.

In both cases $m \ge 2966$; the Legendre route alone would give only $m \ge 1020$.

**L-9913.9 (floor sensitivity).** With $m^*(F)$ as in L-9913.3(1) and
$K^*(F) := \lceil m^*(F)\,\alpha\rceil$:

| $F$ | status of $\mathrm{(V}_F)$ | $m^*(F)$ | $K^*(F)$ | $C$-length $\ge K^*+m^*$ |
|---|---|---|---|---|
| $10^6$ | **verified in-repo, independently reviewed** (X-9901, L-9909 PROVED) | $2966$ | $4701$ | $7667$ |
| $10^7$ | verified in this file (X-9913, PROPOSED) | $10946$ | $17349$ | $28295$ |
| $10^8$ | verified in this file (X-9913, PROPOSED) | $15601$ | $24727$ | $40328$ |
| $10^9$ | verified in this file (X-9913, PROPOSED) | $47468$ | $75235$ | $122703$ |
| $2^{68}$ | **not verified anywhere in this repository** — HYPOTHETICAL, literature-scale | $8\,961\,554\,427 \le m^* \le 72\,057\,431\,991$ | — | — |

The $m^*(F)$ column is an exact, purely arithmetic function of $F$ (it does not
depend on any Collatz input); only the second column records what has actually
been verified. The $F = 2^{68}$ row is **HYPOTHETICAL**: it says what the bound
*would* become at a literature-scale floor, not what is proved, and for it only a
certified bracket is given (see L-9913.10 and Remaining uncertainty); its
endpoints are exact. **The Main Theorem uses only the first row.**

**L-9913.10 (stretch: raised in-repo floor).**
**X-9913 (finite verification, this file, PROPOSED).** For every integer $n$ with
$1 \le n \le 10^{9}$, the $T$-orbit of $n$ reaches $1$; hence every such $n$
reaches $1$ under $C$. (Method, runtime and code: Adversarial tests, Test 14;
$4.6 \cdot 10^{2}$ s of exact integer arithmetic, $O(1)$ memory.)
Consequently $\mathrm{(V}_{10^{9}})$ holds, and every nontrivial $S$-cycle
satisfies
$$m \ge 47468, \qquad K \ge 75235, \qquad C\text{-length} \ge 122703,$$
with all elements $> 10^{9}$. **This corollary inherits the PROPOSED status of
X-9913** and is kept strictly separate from the Main Theorem, which rests only on
the independently reviewed X-9901. (Intermediate values are also recorded:
$\mathrm{(V}_{10^{7}})$ gives $m \ge 10946$ and $\mathrm{(V}_{10^{8}})$ gives
$m \ge 15601$, so a reviewer who only wants to re-run the cheap $3.5$ s sweep
still gets $m \ge 10946$.)

**L-9913.11 (efficient search; one-sided best approximations).** Let $\alpha$ be
any irrational number, $f(m) := \lceil m\alpha\rceil - m\alpha$,
$g(m) := \{m\alpha\}$. Run the Stern–Brocot recursion
$$(u,P,v,Q) := (1, \lceil\alpha\rceil, 1, \lfloor\alpha\rfloor); \qquad
\text{repeat: } \begin{cases} (u,P) \leftarrow (u+v, P+Q) & \text{if } A > B,\\
(v,Q) \leftarrow (u+v, Q+P) & \text{if } A < B,\end{cases}$$
where $A := P - u\alpha$ and $B := v\alpha - Q$ (recomputed after each update).
Then at every stage: $Pv - Qu = 1$, $A, B \in (0,1)$, $A = f(u)$, $B = g(v)$, and
$$\textbf{(Invariant)}\qquad f(m) \ge A \ \text{ and }\ g(m) \ge B
\qquad\text{for every } 1 \le m < u+v .$$
Consequently, if $u_1 < u_2 < \dots$ are the successive values taken by $u$ (the
*one-sided records*), then $f(m) \ge f(u_j)$ for all $m < u_{j+1}$, so the whole
block $[u_j, u_{j+1})$ can be discarded from the search for $m^*(F)$ as soon as
$f(u_j) > \varepsilon_0(F)\,(u_{j+1}-1)$. For $F = 10^6$ this discards every
$m < 2674$ using $15$ record evaluations instead of $2673$ tests, and the
brute-force search is only needed on $[2674, 2966]$ — where it terminates at
$2966$. (This lemma is a *speed-up*, not a load-bearing step: L-9913.5 was
verified by exhaustive enumeration of **all** $m \le 3000$.)

---

## Definitions

All symbols not listed here are from `NOTATION.md`.

* $\alpha := \log_2 3$; $\{t\}$ and $\lfloor t\rfloor$, $\lceil t\rceil$ are the
  fractional part, floor and ceiling of a real $t$.
* $f(m) := \lceil m\alpha\rceil - m\alpha$ for $m \in \mathbb{Z}^{+}$; by
  L-9913.3(1), $f(m) = 1 - \{m\alpha\} \in (0,1)$.
  $f(m)$ is small exactly when $m\alpha$ sits just *below* an integer, i.e. when
  $\lceil m\alpha \rceil / m$ approximates $\alpha$ well **from above**.
* $\varepsilon(F) := 1/(3F\ln 2)$ (the true bound of L-9905.5 at $x_{\min} = F$)
  and its rational majorant $\varepsilon_0(F) := 1000/(2079F)$.
* $\mathrm{Adm}_F(m)$: the admissibility predicate of L-9913.3.
  $m^*(F) := \min\{m \ge 1: \mathrm{Adm}_F(m)\}$.
* **Verified floor** $F$: any integer $\ge 2$ for which the finite verification
  $\mathrm{(V}_F)$ ("every $n \le F$ reaches $1$ under $C$") has been carried out.
  $F$ is a *parameter* everywhere below; no proof step uses its value.
* $q := m/\gcd(K,m)$ is the **reduced denominator** of the rational $K/m$; $p := K/\gcd(K,m)$.
* $\ln$, $\exp$ have their standard meaning; the only analytic facts used are
  $\ln$ is the primitive of $1/t$ with $\ln 1 = 0$ (used in Lemma A), and strict
  monotonicity of $t \mapsto 2^t$ (used in Lemma B).
* Continued-fraction vocabulary is used **only** in L-9913.8 and L-9913.11;
  L-9913.11 is proved self-containedly from scratch, and L-9913.8 cites L-9910.

---

## Motivation

The cycle mode is one of the two counterexample modes of this project (D-9909, and
see L-9911's mode dichotomy): a nontrivial $S$-cycle *is* a set of counterexamples
(proved here in L-9913.1). Issue #9's cycle-synthesis program searches for the
data $(m; a_1, \dots, a_m)$; L-9906 and L-9915 eliminated $m \le 21$ by exhaustive
enumeration of compositions, and that route dies quickly: the number of
compositions is $\binom{K-1}{m-1}$, already $\approx 1.8 \cdot 10^{9}$ for
$m \le 21$.

This file replaces enumeration by a *single* arithmetic obstruction. Because a
cycle's minimal element must exceed every verified floor (L-9913.1), the
approximation corollary L-9905.5 forces the rational $K/m$ to approximate
$\log_2 3$ from above with error $< \varepsilon_0(F)$ — and rationals that good,
with small denominator, simply do not exist. The exact statement of "do not exist"
is a finite, decidable check, and it yields $m \ge 2966$ at the currently verified
floor. For the synthesis program this means: **every candidate with $m \le 2965$
is dead on arrival**, without touching its composition; and the search may be
organised along the admissible $m$ (multiples of one-sided best-approximation
denominators of $\log_2 3$), which L-9913.11 enumerates cheaply. Each additional
decade of verified floor buys a further jump in the bound (L-9913.9), so
verification effort converts directly into search-space elimination.

**Honesty statement (prominent, per the assignment).** This argument is
*elementary*: it uses only the cycle equation, one finite verification, and exact
rational arithmetic. It does **not** use Baker-type transcendence bounds (lower
bounds for the linear form $|K\ln 2 - m\ln 3|$), which is the mechanism by which
the literature obtains much larger bounds. **No claim of any kind is made here
about the literature's numbers, methods, or priority**; the value $2966$ is what
*this* repository can certify end-to-end today, and it is certainly not a record.
Every constant in the file is explicit and every inequality is exact.

---

## Proof

### Lemma A (an elementary certified lower bound for $\ln 2$)

**Lemma A.** For every real $x$ with $0 < x < 1$ and every integer $n \ge 1$,
$$\sum_{k=0}^{n-1} \frac{x^{2k+1}}{2k+1}
\;<\; \frac12 \ln\frac{1+x}{1-x}
\;\le\; \sum_{k=0}^{n-1} \frac{x^{2k+1}}{2k+1} \;+\; \frac{x^{2n+1}}{(2n+1)(1-x^2)} .$$

*Proof.* For $t^2 \ne 1$ the finite geometric identity
$$\frac{1}{1-t^2} \;=\; \sum_{k=0}^{n-1} t^{2k} \;+\; \frac{t^{2n}}{1-t^2}$$
holds — multiply by $1 - t^2$ and telescope:
$(1-t^2)\sum_{k=0}^{n-1} t^{2k} = 1 - t^{2n}$. This is an algebraic identity; no
convergence question arises. Integrate over $[0,x] \subset [0,1)$:
$$\int_0^x \frac{dt}{1-t^2} \;=\; \sum_{k=0}^{n-1}\frac{x^{2k+1}}{2k+1} \;+\; R_n,
\qquad R_n := \int_0^x \frac{t^{2n}}{1-t^2}\,dt .$$
The function $h(x) := \frac12\bigl(\ln(1+x) - \ln(1-x)\bigr)$ satisfies $h(0) = 0$
and $h'(x) = \frac12\left(\frac{1}{1+x} + \frac{1}{1-x}\right) = \frac{1}{1-x^2}$
on $(-1,1)$, so by the fundamental theorem of calculus
$\int_0^x dt/(1-t^2) = h(x) = \frac12\ln\frac{1+x}{1-x}$. Finally, on $(0,x]$ the
integrand $t^{2n}/(1-t^2)$ is positive and $\le t^{2n}/(1-x^2)$, so
$$0 \;<\; R_n \;\le\; \frac{1}{1-x^2}\int_0^x t^{2n}dt \;=\; \frac{x^{2n+1}}{(2n+1)(1-x^2)} . \qquad\square$$

**Corollary A1 ($\ln 2 > 693/1000$).** Take $x = 1/3$, so
$\frac{1+x}{1-x} = 2$ and $\ln 2 = 2\cdot\frac12\ln\frac{1+x}{1-x}$. With $n = 4$,
Lemma A's strict left inequality gives
$$\ln 2 \;>\; 2\left(\frac13 + \frac{1}{3\cdot 3^3} + \frac{1}{5 \cdot 3^5}
+ \frac{1}{7\cdot 3^7}\right)
= 2\left(\frac13 + \frac1{81} + \frac1{1215} + \frac1{15309}\right)
= 2\cdot\frac{26528}{76545} = \frac{53056}{76545},$$
(common denominator $76545 = 5\cdot 7\cdot 3^7$:
$\frac{25515 + 945 + 63 + 5}{76545} = \frac{26528}{76545}$), and
$$\frac{53056}{76545} > \frac{693}{1000}
\iff 53056\cdot 1000 = 53\,056\,000 \;>\; 53\,045\,685 = 693 \cdot 76545 . \checkmark$$
Hence $\ln 2 > 693/1000$, and therefore for every real $F > 0$
$$\varepsilon(F) = \frac{1}{3F\ln 2} \;<\; \frac{1000}{3\cdot 693\cdot F} = \varepsilon_0(F). \qquad\blacksquare$$

*(Remark: taking $x = 1/5$ in Lemma A gives $\ln\frac32 = 2\,\mathrm{artanh}(1/5)$
and hence, via $\ln 3 = \ln 2 + \ln\frac32$, certified rational enclosures of
$\alpha$ of any desired width. This route is used in the Adversarial tests as an
independent check of L-9913.4(4), but is not needed for the Main Theorem.)*

### Lemma B (irrationality; comparison principle; the two certificates)

**B(i).** $\alpha = \log_2 3$ is irrational, and $m\alpha \notin \mathbb{Z}$ for
every $m \in \mathbb{Z}^{+}$.

*Proof.* $\alpha > 0$ since $3 > 1$. If $\alpha = a/b$ with $a, b \in
\mathbb{Z}^{+}$, then $b\alpha = a$, so $3^b = 2^{b\alpha} = 2^{a}$; but $3^b$ is
odd ($b \ge 1$) and $2^a$ is even ($a \ge 1$) — contradiction. If $m\alpha = k \in
\mathbb{Z}$ for some $m \ge 1$ then $k \ge 1$ (as $m\alpha > 0$) and $\alpha = k/m$
is rational, contradiction. $\square$

**B(ii) (comparison principle).** For $a, b \in \mathbb{Z}^{+}$:
$\alpha > a/b \iff 3^b > 2^a$ and $\alpha < a/b \iff 3^b < 2^a$.

*Proof.* $\alpha > a/b \iff b\alpha > a \iff 2^{b\alpha} > 2^{a}$ (strict
monotonicity of $t\mapsto 2^t$), and $2^{b\alpha} = (2^{\alpha})^{b} = 3^{b}$.
Same for $<$. $\square$

**B(iii) (certificates).** The exact integer comparisons
$$3^{111202} \;>\; 2^{176251}, \qquad 3^{190537} \;<\; 2^{301994}$$
hold (Adversarial tests, Test 2; each side has $176\,252$ resp. $301\,995$ bits and
the comparison takes milliseconds). By B(ii),
$$L_0 = \frac{176251}{111202} \;<\; \alpha \;<\; \frac{301994}{190537} = U_0 ,$$
and $U_0 - L_0 = \frac{301994\cdot 111202 - 176251 \cdot 190537}{190537\cdot 111202}
= \frac{1}{21\,188\,095\,474} < 4.721\cdot 10^{-11}$. $\blacksquare$

*(These two fractions are the $12$th and $13$th convergents of $\alpha$
(L-9910.3), but nothing here uses that: they are used purely as two verified
integer inequalities.)*

### Proof of L-9913.1 (counterexample floor)

**Step 1 ($S$-orbits sit inside $C$-orbits).** Let $x$ be a positive odd integer
and $a := \nu_2(3x+1) \ge 1$. Then $C(x) = 3x+1$ (as $x$ is odd), and for
$0 \le j \le a-1$ the integer $(3x+1)/2^{j}$ is even (because $j < a = \nu_2(3x+1)$
implies $\nu_2((3x+1)/2^j) = a - j \ge 1$), so $C\bigl((3x+1)/2^{j}\bigr) =
(3x+1)/2^{j+1}$. Chaining, $C^{1+a}(x) = (3x+1)/2^{a} = S(x)$. Hence, by induction
on $j$, $S^{j}(x) = C^{\,t_j}(x)$ with $t_0 = 0$ and
$t_{j+1} = t_j + 1 + a(S^{j}(x)) \ge t_j + 2$; in particular $t_j \ge 2j \to \infty$.

**Step 2 ($1$ is not on a nontrivial cycle).** $S(1) = (3+1)/2^{2} = 1$. If some
$x_i = 1$, then every element of the cycle equals $S^{\,j}(x_i) = S^{\,j}(1) = 1$
for the appropriate $j$; since the $m$ elements are pairwise distinct (D-9908),
$m = 1$ and the cycle is the fixed point $(1)$, i.e. the trivial cycle of D-9905 —
contradicting nontriviality. Hence $x_i \ne 1$ for all $i$.

**Step 3 (every element is a counterexample).** Fix $i$ and suppose, for
contradiction, $1 \in O_C(x_i)$, say $C^{t}(x_i) = 1$ with $t \ge 0$. Since
$C(1) = 4$, $C(4) = 2$, $C(2) = 1$, an immediate induction gives
$C^{s}(x_i) \in \{1,4,2\}$ for **every** $s \ge t$. Choose $j$ with $t_j \ge t$
(possible by Step 1). Then $S^{\,j}(x_i) = C^{\,t_j}(x_i) \in \{1,2,4\}$. But
$S^{\,j}(x_i)$ is an element of the cycle, hence odd, so $S^{\,j}(x_i) = 1$ —
contradicting Step 2. Therefore $1 \notin O_C(x_i)$: $x_i$ is a counterexample
(D-9909).

**Step 4 (floor).** Assume $\mathrm{(V}_F)$: every $n \le F$ reaches $1$ under $C$,
i.e. no $n \le F$ is a counterexample. By Step 3 every $x_i > F$, so
$x_{\min} \ge F+1$. With $F = 10^6$ discharged by X-9901 (L-9909, PROVED):
$x_{\min} > 10^6$. $\blacksquare$

*(This re-derives, for cycle elements only, the substance of L-9911's closure
statement; it is proved inline precisely so that L-9913 inherits no status from
L-9911.)*

### Proof of L-9913.2 (the squeeze)

Let a nontrivial $S$-cycle be given and assume $\mathrm{(V}_F)$. L-9905.3 (PROVED)
states, for **every** $S$-cycle on positive odds,
$$0 \;<\; K\ln 2 - m \ln 3 \;\le\; m\ln\!\left(1 + \frac{1}{3x_{\min}}\right)
\;\le\; \frac{m}{3\,x_{\min}} .$$
Divide by $\ln 2 > 0$ and use $\ln 3/\ln 2 = \alpha$:
$$0 \;<\; K - m\alpha \;\le\; \frac{m}{3\,x_{\min}\ln 2} .$$
By L-9913.1, $x_{\min} \ge F + 1 > F > 0$, so $\frac{m}{3x_{\min}\ln 2} <
\frac{m}{3F\ln 2} = \varepsilon(F)\,m$; and by Corollary A1,
$\varepsilon(F) < \varepsilon_0(F)$. Chaining,
$$0 \;<\; K - m\alpha \;<\; \varepsilon_0(F)\, m . \qquad\blacksquare$$

Both inequalities are strict; the left one is L-9905.2 ($2^K > 3^m$), the right one
is strict because $x_{\min} > F$ strictly and $\varepsilon < \varepsilon_0$ strictly.

### Proof of L-9913.3 (reduction)

**(1)** By Lemma B(i), $m\alpha \notin\mathbb{Z}$; hence
$\lceil m\alpha\rceil = \lfloor m\alpha\rfloor + 1$ and
$f(m) = \lceil m\alpha\rceil - m\alpha = 1 - (m\alpha - \lfloor m\alpha\rfloor)
= 1 - \{m\alpha\} \in (0,1)$.
*Upward closure:* assume $\mathrm{Adm}_F(q)$ and let $t \ge 1$. Since
$t\lceil q\alpha\rceil$ is an integer $\ge tq\alpha$, we have
$\lceil tq\alpha\rceil \le t \lceil q\alpha\rceil$, so
$$f(tq) = \lceil tq\alpha\rceil - tq\alpha \;\le\; t\bigl(\lceil q\alpha\rceil - q\alpha\bigr)
= t f(q) \;\le\; t\,\varepsilon_0 q = \varepsilon_0 (tq),$$
i.e. $\mathrm{Adm}_F(tq)$.
*Well-definedness:* $\mathrm{Adm}_F(m)$ holds for every integer
$m \ge 1/\varepsilon_0(F)$ (then $\varepsilon_0 m \ge 1 > f(m)$), so the set is
nonempty and $m^*(F)$ exists. For $F \ge 2$: $\varepsilon_0(F) \le 1000/4158 <
0.2406$ while $f(1) = 2 - \alpha > 2 - U_0 > 0.415$ (Lemma B(iii)), so
$\mathrm{Adm}_F(1)$ is false and $m^*(F) \ge 2$.

**(2)** By L-9905.2, $2^K > 3^m$, i.e. $K > m\alpha$. As $K$ is an integer strictly
greater than the non-integer $m\alpha$, $K \ge \lceil m\alpha\rceil$. Hence
$$f(m) \;=\; \lceil m\alpha\rceil - m\alpha \;\le\; K - m\alpha \;<\; \varepsilon_0 m$$
by L-9913.2 — i.e. $\mathrm{Adm}_F(m)$ holds. If moreover $m < 1/\varepsilon_0$ and
$K \ge \lceil m\alpha \rceil + 1$, then $K - m\alpha \ge 1 + f(m) > 1 > \varepsilon_0 m$,
contradicting L-9913.2; so $K = \lceil m\alpha\rceil$ in that range.

**(3)** Write $d := \gcd(K,m)$, $p := K/d$, $q := m/d$, so $K/m = p/q$ in lowest
terms and $q \ge 1$. Dividing L-9913.2 by $m > 0$:
$0 < \frac{K}{m} - \alpha < \varepsilon_0$, i.e. $0 < \frac{p}{q} - \alpha <
\varepsilon_0$ — **the common factor $d$ cancels**: the constraint depends only
on the reduced fraction. Multiplying by $q$: $0 < p - q\alpha < \varepsilon_0 q$. Since
$p > q\alpha$ and $p$ is an integer while $q\alpha \notin \mathbb{Z}$, we get
$p \ge \lceil q\alpha\rceil$, hence
$$f(q) = \lceil q\alpha\rceil - q\alpha \;\le\; p - q\alpha \;<\; \varepsilon_0 q,$$
i.e. $\mathrm{Adm}_F(q)$.

**(4)** By (3) the reduced denominator $q$ of any nontrivial cycle satisfies
$\mathrm{Adm}_F(q)$, hence $q \ge m^*(F)$ by minimality; and
$m = q\cdot\gcd(K,m) \ge q$. $\blacksquare$

> **Note on the trap flagged by the coordinator.** Part (3) is exactly the
> scale-invariance point: the squeeze constrains the *reduced* denominator $q$,
> not $m$ per se. This file never assumes $m$ is an approximation denominator.
> Two independent routes are available and both are proved above: applying
> $\mathrm{Adm}_F$ directly to $m$ (legitimate, by (2)), and applying it to $q$
> (by (3)). They give the same numerical bound here because
> $\mathrm{Adm}_F$ is closed upward under multiples (part (1)), so
> $\min\{m : \mathrm{Adm}_F(m)\} = \min\{q : \mathrm{Adm}_F(q)\}$ trivially — the
> two minima are over the same set. The stronger of the two conclusions,
> $q \ge m^*(F)$, is the one recorded in the Main Theorem. It is genuinely
> stronger: it also says $m$ is a multiple of some admissible $q \ge 2966$.
> *(Verified computationally: the minimiser $2966$ is itself reduced,
> $\gcd(4701, 2966) = 1$, and the admissible set below $3000$ is exactly
> $\{2966\}$ — Adversarial tests, Test 9.)*

### Proof of L-9913.4 (decision procedures)

**(1)** With $\varepsilon_0 = P/Q$, $Q \ge 1$:
$$K - m\alpha \le \frac{P}{Q} m
\iff QK - Pm \le Qm\alpha
\iff 2^{\,QK-Pm} \le 2^{\,Qm\alpha} = \bigl(2^{\alpha}\bigr)^{Qm} = 3^{\,Qm},$$
using that $t \mapsto 2^{t}$ is strictly increasing on $\mathbb{R}$ (so it
preserves and reflects $\le$) and $2^\alpha = 3$. The exponent $QK - Pm$ may be
negative, in which case $2^{QK-Pm}$ is the rational $1/2^{Pm-QK}$ and the
comparison is still exact. $\square$

**(2)** If $L \ge r = K/m - \varepsilon_0$ then $\alpha > L \ge r$, so
$K/m - \alpha < \varepsilon_0$, i.e. $K - m\alpha < \varepsilon_0 m$. If
$U \le r$ then $\alpha < U \le r$, so $K/m - \alpha > \varepsilon_0$, i.e.
$K - m\alpha > \varepsilon_0 m$. $\square$

**(3)** $mL < m\alpha < mU$ and $\lceil\cdot\rceil$ is nondecreasing, so
$\lceil mL\rceil \le \lceil m\alpha\rceil \le \lceil mU\rceil$; if the two outer
values coincide, so does the middle one. $\square$

**(4)** Lemma B(iii). $\blacksquare$

**Cost note.** (2) decides one $m$ by a single comparison of two integers obtained
by cross-multiplying $L_0$ (or $U_0$) with $r$; for $m \le 3000$ and
$\varepsilon_0 = 1/2079000$ these integers are below $10^{16}$. The procedure is
*conclusive* for a given $m$ unless $|\alpha - r| \le U_0 - L_0 = 4.721\cdot
10^{-11}$; Test 4 records that over the whole range $m \le 3000$ the smallest
occurring $|\alpha - r|$ is $6.871\cdot 10^{-8}$, larger by a factor $1456$, so
every instance is decided.

### Proof of L-9913.5 (the computation)

This is a **finite verification** (labelled as such), carried out in exact integer
arithmetic; the code and its verbatim output are in the Adversarial tests (Test 4)
and the certificates are displayed in the Statement. The logical content is:

1. For each $m \in \{1, 2, \dots, 2965\}$: compute $K_m := \lceil m\alpha\rceil$ by
   L-9913.4(3) with the enclosure $L_0 < \alpha < U_0$ (this succeeded for every
   such $m$, so each $K_m$ is exactly determined), then verify the strict
   inequality $U_0 < K_m/m - \varepsilon_0$; by L-9913.4(2),
   $K_m - m\alpha > \varepsilon_0 m$, i.e. $\mathrm{Adm}_{10^6}(m)$ is **false**.
2. For $m = 2966$: $K_{2966} = 4701$ and $L_0 > 4701/2966 - \varepsilon_0$; by
   L-9913.4(2), $\mathrm{Adm}_{10^6}(2966)$ is **true**.

Hence $m^*(10^6) = 2966$. Two independent certifications of $\alpha$ were used and
agree (Tests 4 and 5): the convergent certificates $L_0, U_0$ of Lemma B(iii), and
the Lemma-A series enclosure of width $< 10^{-78}$. An independent structural
route (L-9913.11) reproduces the same answer while testing only $15$ record values
plus the block $[2674, 2966]$ (Test 8). $\blacksquare$

*Numerical margins (for orientation only; the decisions above are exact):*
$f(2966) = 0.001222861\ldots$ versus $\varepsilon_0 \cdot 2966 = 0.001426647\ldots$
(admissible), and $f(2301) = 0.001287246\ldots$ versus $\varepsilon_0\cdot 2301 =
0.001106782\ldots$ (not admissible).

### Proof of the Main Theorem (L-9913.6)

Assume $\mathrm{(V}_{10^6})$ (X-9901) and let a nontrivial $S$-cycle be given.

* By L-9913.3(4) and L-9913.5, $q \ge m^*(10^6) = 2966$ and $m \ge q \ge 2966$.
* $K > m\alpha \ge 2966\alpha$ (L-9905.2 and $m \ge 2966$, $\alpha>0$); since
  $2966\alpha \notin \mathbb{Z}$ and $K$ is an integer, $K \ge
  \lceil 2966\alpha\rceil = 4701$ (the value of the ceiling is certified in Test 4
  via L-9913.4(3): $\lceil 2966 L_0\rceil = \lceil 2966 U_0\rceil = 4701$).
* The $m \ge 2966$ elements are pairwise distinct positive odd integers (D-9908)
  and each exceeds $10^6$ (L-9913.1).
* The $C$- and $T$-cycle lengths are $K+m \ge 4701 + 2966 = 7667$ and
  $K \ge 4701$ by L-9913.7.

Finally, L-9906 (PROVED) and L-9915 (PROVED) give "no nontrivial $S$-cycle has
$m \le 21$"; the combined statement $m \ge \max(22, m^*) = \max(22, 2966) = 2966$
is exactly the above. Had L-9915 remained PROPOSED (its status when this file was
assigned), the PROVED-only combination would read $m \ge \max(7, 2966) = 2966$ —
the same. In other words the small-$m$ eliminations are *subsumed*; they remain
valuable as independent confirmations at small $m$ and because they need no
verified floor at all. $\blacksquare$

### Proof of L-9913.7 ($C$- and $T$-cycle lengths)

Let $x_1 \to \dots \to x_m \to x_1$ be an $S$-cycle, indices cyclic. By Step 1 of
L-9913.1, the $C$-orbit from $x_i$ passes through
$$x_i \to 3x_i + 1 = \tfrac{3x_i+1}{2^0} \to \tfrac{3x_i+1}{2^{1}} \to \dots \to
\tfrac{3x_i+1}{2^{a_i}} = x_{i+1},$$
which is $1 + a_i$ steps of $C$. Concatenating over $i = 1, \dots, m$:
$C^{\,K+m}(x_1) = x_1$, so the $C$-orbit of $x_1$ is periodic with period $K+m$,
and the listed values are exactly the points visited.

*Distinctness.* The values $x_1, \dots, x_m$ are distinct and odd. The values
$y_{i,j} := (3x_i+1)/2^{j}$ with $0 \le j \le a_i - 1$ are even (Step 1 of
L-9913.1). If $y_{i,j} = y_{i',j'}$, taking odd parts (D-9903) gives
$\mathrm{odd}(3x_i+1) = \mathrm{odd}(3x_{i'}+1)$, i.e. $x_{i+1} = x_{i'+1}$, hence
$i = i'$ by distinctness of the cycle elements, and then $j = j'$. So there are
exactly $m + \sum_i a_i = m + K$ distinct values, and the least period of the
$C$-orbit is $K+m$ (a periodic orbit visiting exactly $N$ distinct points has least
period $N$).

For $T$ (D-9902): $T(x_i) = (3x_i+1)/2 = y_{i,1}$ and $T(y_{i,j}) = y_{i,j+1}$ for
$1 \le j \le a_i - 1$ (each such $y_{i,j}$ with $j < a_i$ is even), reaching
$y_{i,a_i} = x_{i+1}$ in $a_i$ steps. Summing, $T^{K}(x_1) = x_1$, and the visited
set is $\{x_i\} \cup \{y_{i,j} : 1 \le j \le a_i-1\}$, of cardinality
$m + \sum_i (a_i - 1) = K$, distinct by the same argument; so the least period is
$K$.

*Converse.* If $\mathcal{O}$ is a nontrivial $C$-cycle, it contains an odd element
(a cycle of positive integers cannot consist of even numbers only: repeated
halving strictly decreases), and the odd elements of $\mathcal{O}$, in $C$-order,
form an $S$-cycle: from an odd $x \in \mathcal{O}$ the next odd element of the
$C$-orbit is reached after exactly $1 + \nu_2(3x+1)$ steps and equals $S(x)$, by
the computation above. It is nontrivial because $\mathcal{O} \ne (1,4,2)$. $\blacksquare$

### Proof of L-9913.8 (convergent dichotomy)

Let $K/m = p/q$ in lowest terms. By L-9905.2, $p/q > \alpha$. Either $p/q$ is a
convergent of $\alpha$ or it is not.

**(a)** If it is, then since the convergents lying **above** $\alpha$ are exactly
the odd-index ones (L-9910.3, PROVED), $p/q = p_i/q_i$ with $i$ odd. L-9910.3/.4(ii)
certifies that the odd-index convergent denominators $\le 10^{5}$ are exactly
$1, 5, 41, 306, 15601, 79335$, and all convergent denominators beyond $q_{11} =
79335$ are $\ge q_{12} = 111202$ (denominators strictly increase). By L-9913.6,
$q \ge 2966$; the smallest odd-index denominator $\ge 2966$ is $15601$. Hence
$q \ge 15601$, so $m \ge q \ge 15601$ and (as in the Main Theorem)
$K > m\alpha \ge 15601\alpha$ gives $K \ge \lceil 15601\alpha\rceil = 24727$.

**(b)** If it is not a convergent, then by the contrapositive of Legendre's
criterion (L-9910.1, PROVED) $|\alpha - p/q| \ge \frac{1}{2q^2}$. Combined with
$0 < p/q - \alpha < \varepsilon_0$ (proof of L-9913.3(3)) this gives
$\frac{1}{2q^2} < \varepsilon_0 = \frac{1}{2079000}$, i.e.
$q^2 > 1\,039\,500$ and $q \ge 1020$ (since $1019^2 = 1\,038\,361 < 1\,039\,500 \le
1\,040\,400 = 1020^2$). This is weaker than L-9913.6's $q \ge 2966$, which
therefore governs. $\blacksquare$

*Remark (why Legendre cannot replace L-9913.5).* The minimiser $m^* = 2966 = 306 +
4\cdot 665$ is a **semiconvergent** (intermediate fraction), not a convergent, so
Legendre's criterion does not exclude it — correctly, since the argument must not
prove more than is true. The coordinator relays from the L-9910 review that the
semiconvergent $569/359$ attains $q^2|\alpha - p/q| \in [0.5520, 0.5533]$, i.e. the
Legendre threshold $1/2$ is cleared by only about $10\%$ for $\log_2 3$; this file
reconfirms $q\,|q\alpha - p| = 0.5521\ldots$ for that pair (Test 12). It is a good
reminder that the convergent-only picture is genuinely lossy here.

### Proof of L-9913.11 (one-sided best approximations)

Let $\alpha$ be irrational, and consider a state $(u, P, v, Q)$ of the recursion
with $u, v \ge 1$, $A := P - u\alpha \in (0,1)$, $B := v\alpha - Q \in (0,1)$ and
$$Pv - Qu = 1. \tag{$\dagger$}$$

**Initialisation.** $u = v = 1$, $P = \lceil \alpha\rceil = \lfloor\alpha\rfloor+1$,
$Q = \lfloor\alpha\rfloor$: then $A = \lceil\alpha\rceil - \alpha \in (0,1)$,
$B = \alpha - \lfloor\alpha\rfloor \in (0,1)$, and $Pv - Qu = P - Q = 1$. ✓

**Preservation.** $A \ne B$ (else $P + Q = (u+v)\alpha$ would make $\alpha$
rational). If $A > B$: $(u+v)\alpha = (P - A) + (Q + B) = (P+Q) - (A-B)$ with
$A - B \in (0,1)$, so the new $A' = (P+Q) - (u+v)\alpha = A - B \in (0,1)$, the new
$B$ is unchanged, and $(P+Q)v - Q(u+v) = Pv - Qu = 1$. If $A < B$: symmetrically
$B' = B - A \in (0,1)$, $A$ unchanged, and $P(u+v) - (Q+P)u = Pv - Qu = 1$. So
$(\dagger)$ and $A,B \in (0,1)$ persist, and $u+v$ strictly increases at every
step (each of $u, v$ is nondecreasing). Also, by construction $A = P - u\alpha$ with $P$ an integer and
$A \in (0,1)$, which forces $P = \lceil u\alpha\rceil$ and $A = f(u)$; similarly
$Q = \lfloor v\alpha\rfloor$ and $B = g(v) = \{v\alpha\}$.

**The Invariant.** Let $1 \le m < u+v$ and let $N$ be any integer. By $(\dagger)$
the matrix $\begin{pmatrix} u & v\\ P & Q\end{pmatrix}$ has determinant
$uQ - vP = -1$, so it is unimodular and the map $(s,t)\mapsto (su+tv,\, sP+tQ)$ is
a bijection $\mathbb{Z}^2 \to \mathbb{Z}^2$. Write $(m, N) = (su+tv,\ sP+tQ)$. Then
$$N - m\alpha \;=\; s(P - u\alpha) + t(Q - v\alpha) \;=\; sA - tB .$$
Now $m = su + tv$ with $1 \le m < u + v$ excludes both $s,t \ge 1$ (which forces
$m \ge u+v$) and $s,t \le 0$ (which forces $m \le 0$). The remaining sign patterns:

| $s$ | $t$ | $N - m\alpha = sA - tB$ |
|---|---|---|
| $\ge 1$ | $\le -1$ | $\ge A + B > A$ |
| $\ge 1$ | $=0$ | $= sA \ge A$ |
| $\le 0$ | $\ge 1$ | $\le -B < 0$ |
| $\le -1$ | $\le 0$ | $m = su+tv \le -u < 0$: excluded |
| $=0$ | $\le 0$ | $m \le 0$: excluded |

(The five rows are exhaustive: of the nine sign combinations, $(s\ge1, t\ge1)$ and
$(s\le -1,t\le -1)$, $(s\le-1,t=0)$, $(s=0,t\le 0)$, $(s\le -1, t\ge 1)$ are all
listed or excluded above.) Hence every **positive** value of $N - m\alpha$ is
$\ge A$; as $f(m) = \min\{N - m\alpha : N \in \mathbb{Z},\ N - m\alpha > 0\}$
(the minimum is attained at $N = \lceil m\alpha\rceil$), we get $f(m) \ge A$.

The same bookkeeping for $m\alpha - N = tB - sA$ gives the second half: a value
$tB - sA$ can be positive only when $t \ge 1$ and $s \le 0$ (if $t \le 0$ and
$s \ge 1$ it is $\le -A < 0$; if $t\le 0$ and $s \le 0$ then $m \le 0$; if
$t \ge 1$ and $s \ge 1$ then $m \ge u+v$), and in that case
$tB - sA = tB + |s|A \ge B$. Since
$g(m) = \min\{m\alpha - N : N \in \mathbb{Z},\ m\alpha - N > 0\}$, this gives
$g(m) \ge B$ for all $1 \le m < u+v$.

**Consequence (block skipping).** Let $u_1 < u_2 < \dots$ be the successive values
of $u$. When $u$ is about to be replaced by $u_{j+1} = u_j + v$, the Invariant at
that moment says $f(m) \ge A = f(u_j)$ for all $m < u_{j+1}$; in particular
$$\min_{u_j \le m < u_{j+1}} f(m) \;\ge\; f(u_j).$$
Therefore, if $f(u_j) > \varepsilon_0\,(u_{j+1}-1)$, then for every
$m \in [u_j, u_{j+1})$ one has $f(m) \ge f(u_j) > \varepsilon_0 (u_{j+1}-1) \ge
\varepsilon_0 m$, i.e. $\mathrm{Adm}_F(m)$ fails on the entire block. Blocks that
survive this test are searched directly. $\blacksquare$

*(Applied with $F = 10^6$: the records are $1, 3, 5, 17, 29, 41, 94, 147, 200,
253, 306, 971, 1636, 2301, 2966, \dots$; every block **below** $2301$ is
discarded outright, and inside the block $[2301, 2966)$ $\mathrm{Adm}$ needs
$m \ge f(2301)/\varepsilon_0 = 2673.3\ldots$, leaving only $m \in [2674, 2965]$ to
test individually — all of which fail. This reproduces $m^* = 2966$ with $15$
record evaluations and $292$ direct tests instead of $2965$; the Main Theorem
nevertheless quotes the fully exhaustive computation.)*

### Proof of L-9913.9 and L-9913.10

L-9913.9's $m^*(F)$ column is the same exhaustive computation as L-9913.5 with
$\varepsilon_0(F)$ in place of $\varepsilon_0(10^6)$ (Test 11); for $F = 2^{68}$
only the certified bracket
$$8\,961\,554\,427 \;\le\; m^*(2^{68}) \;\le\; 72\,057\,431\,991$$
is established: the lower endpoint is the block-skipping bound of L-9913.11 (every
$m$ below it fails $\mathrm{Adm}$, certified), the upper endpoint is an explicit
admissible $m$ (certified by L-9913.4(2)); the exact value inside the bracket is
**not determined here** (see Remaining uncertainty). L-9913.10 is L-9913.6 with
$F = 10^{9}$ in place of $10^6$, the floor hypothesis $\mathrm{(V}_{10^{9}})$ being
discharged by the finite verification X-9913 (Test 14), whose inductive
justification is:

> **Drop lemma.** Suppose that for every odd $n$ with $3 \le n \le N$ there is
> $k \ge 1$ with $T^{k}(n) < n$. Then every $n \le N$ reaches $1$ under $T$, hence
> under $C$ (Step 1 of L-9913.1 gives $O_T(n) \subseteq O_C(n)$: $T(n) = C(n)$ for
> even $n$ and $T(n) = C^2(n)$ for odd $n$).
> *Proof:* strong induction on $n$. $n = 1$: immediate. $n = 2$: $T(2) = 1$.
> $n \ge 2$ even: $T(n) = n/2 < n$ reaches $1$ by induction, and $1 \in O_T(T(n))
> \subseteq O_T(n)$. $n \ge 3$ odd: by hypothesis some $y = T^{k}(n)$ satisfies
> $1 \le y < n$; $y$ reaches $1$ by induction, hence so does $n$. $\square$

$\blacksquare$

---

## Dependency audit

| Dependency | Status | Where used | Load-bearing? |
|---|---|---|---|
| D-9904 (Syracuse map, $a(x) = \nu_2(3x+1) \ge 1$) | — | throughout; Step 1 of L-9913.1; L-9913.7 | yes |
| D-9908 ($S$-cycle notation $m, a_i, K$; least period; distinct elements) | — | throughout | yes |
| D-9905 (trivial cycles; "reaches 1") | — | L-9913.1 Steps 2–4 | yes |
| D-9909 (counterexample) | — | L-9913.1 Step 3 | yes |
| D-9901, D-9902, D-9903 ($C$, $T$, odd part) | — | L-9913.1 Step 1; L-9913.7; drop lemma | yes |
| **L-9905.2** ($2^K > 3^m$) | PROVED | L-9913.2 (left inequality), L-9913.3(2), L-9913.6 ($K \ge 4701$), L-9913.8 ($p/q > \alpha$) | yes |
| **L-9905.3** ($0 < K\ln2 - m\ln3 \le m/(3x_{\min})$) | PROVED | L-9913.2 | yes |
| **X-9901** (every $n \le 10^6$ reaches 1), recorded in L-9909 | PROVED (host file) | L-9913.1 Step 4; Main Theorem | yes (as a finite verification, explicitly flagged) |
| L-9906, L-9915 ($m \le 21$ elimination) | PROVED | combination remark inside L-9913.6 only | **no** |
| L-9910.1 (Legendre), L-9910.3/.4(ii) (certified CF of $\log_2 3$) | PROVED | L-9913.8 only | **no** (optional corollary) |
| L-9911 | PROVED | not used; its cycle-elements-are-counterexamples content is re-proved inline in L-9913.1 | **no** |
| Lemma A (proved inline) | — | $\ln 2 > 693/1000$, hence $\varepsilon < \varepsilon_0$ | yes |
| Lemma B (proved inline) | — | irrationality; $3^b$ vs $2^a$ comparison; the two certificates | yes |
| Standard calculus: FTC, monotonicity of $t\mapsto 2^t$, geometric identity | — | Lemmas A, B | yes |
| X-9913 (this file, finite verification) | PROPOSED | L-9913.10 **only** | separated from the Main Theorem |

**Circularity check.** L-9905 and L-9909 do not cite L-9913 (L-9905 forward-refers
to a planned L-9910; L-9910.5 mentions "a planned L-9913" as a *suggestion*, not as
a dependency). L-9910 depends on L-9905/L-9906, not on this file. No cycle exists.
Nothing here assumes the Collatz conjecture or its negation: the statements are
implications about hypothetical cycles and remain true (vacuously or not) in both
worlds.

---

## Gap audit

Deliberate search against the README §8 checklist.

* **Hidden finiteness assumptions.** The only finite inputs are the explicitly
  labelled verifications $\mathrm{(V}_F)$ (X-9901 for the Main Theorem, X-9913 for
  the stretch corollary) and the exhaustive computation of $m^*(F)$. The latter is
  *not* an extrapolation: it is a finite decision about a purely arithmetic
  quantity ($m^*(F)$ depends only on $\alpha$ and $F$), and the theorem quantifies
  over all cycles, deriving a bound from it. The former is quarantined into a
  hypothesis that appears in every affected statement.
* **Finite computation extrapolated to infinite behaviour.** Explicitly avoided:
  "$\mathrm{Adm}_F(m)$ fails for $m \le 2965$" is not used to guess anything about
  larger $m$; the theorem only needs failure below the minimum.
* **Unjustified induction.** Three inductions appear: (i) $C^{1+j}(x) =
  (3x+1)/2^{j}$ (finite, base and step explicit); (ii) $C^{s}(x)\in\{1,2,4\}$ for
  $s \ge t$ (immediate from $C$ on $\{1,2,4\}$); (iii) the drop lemma's strong
  induction (base $n \in \{1,2\}$, both parities handled). The Stern–Brocot
  invariant of L-9913.11 is proved by an explicit state-preservation argument, not
  by hand-waving "standard CF theory".
* **Boundary cases.** $m = 1$: $\mathrm{Adm}_F(1)$ is false for every $F \ge 2$
  (shown in L-9913.3(1)), so the trivial cycle would *violate* the squeeze — as it
  must, since its $x_{\min} = 1 \le F$ makes $\mathrm{(V}_F)$ inapplicable to it;
  this is checked explicitly in Test 10. $F$ small: $\varepsilon_0(1) = 0.481\ldots
  > f(1)$, which is why $F \ge 2$ is required in the Standing hypothesis.
  $j = 0$ in Step 1 of L-9913.1 (empty chain) is the identity $C^{1}(x) = 3x+1$.
  Negative or zero exponents in L-9913.4(1) are addressed explicitly.
* **Empirical vs universal.** Every computational statement is labelled *finite
  verification*; the Main Theorem's dependence on one such statement (X-9901) is
  stated in its hypothesis, in the header, and in the Motivation. The
  literature-scale row of L-9913.9 is labelled HYPOTHETICAL in two places.
* **Invalid limit interchange.** None: no limits, series or infinite products
  occur. Lemma A deliberately uses a *finite* geometric identity plus an integral
  remainder, so no convergence argument is needed anywhere in the file.
* **Nonuniform estimates.** $\varepsilon_0(F)$ is an explicit rational depending
  only on $F$; the squeeze is uniform in $m$ and in the cycle. All constants
  ($1000/2079$, $L_0$, $U_0$, $53056/76545$) are displayed exactly.
* **Assumptions equivalent to Collatz.** None. $\mathrm{(V}_F)$ is a finite
  statement, verified, not assumed. The results are compatible with the existence
  of a nontrivial cycle (they only constrain its size).
* **Incorrectly assumed independence / reduced-denominator trap.** Addressed
  head-on in L-9913.3(1),(3) and the boxed note: the squeeze constrains $q =
  m/\gcd(K,m)$, and the file proves both directions ($\mathrm{Adm}_F(m)$ directly,
  by (2); $\mathrm{Adm}_F(q)$ by (3); upward closure by (1)), so no step assumes
  $m$ itself is a best-approximation denominator. Test 9 checks the closure
  computationally.
* **Division-by-zero / sign errors.** Divisions are by $\ln 2 > 0$, $m \ge 1$,
  $q \ge 1$, $x_{\min} \ge 1$, $1 - x^2 > 0$ on $(0,1)$, $\varepsilon_0 > 0$. The
  direction of every inequality after division by a positive quantity was checked
  twice; the two "safe direction" arguments (using $\varepsilon_0 \ge \varepsilon$
  and using $L_0, U_0$ on the correct sides) are isolated in L-9913.2 and
  L-9913.4(2).
* **The "safe direction" of $\varepsilon_0$.** Replacing $\varepsilon$ by a larger
  $\varepsilon_0$ *enlarges* the admissible set, hence *decreases* (weakly)
  $m^*$: formally, $\varepsilon \le \varepsilon_0 \Rightarrow
  \{m : f(m) \le \varepsilon m\} \subseteq \{m : f(m) \le \varepsilon_0 m\}
  \Rightarrow \min$ of the larger set $\le \min$ of the smaller. Since every cycle
  satisfies the *true* condition (with $\varepsilon$), it satisfies the relaxed one,
  so $m \ge m^*(\varepsilon_0)$ is valid — possibly weaker than $m
  \ge m^*(\varepsilon)$, never wrong. Test 6 confirms that here the two coincide:
  $m^* = 2966$ for every $\varepsilon \in [4.12293\cdot 10^{-7},\,
  5.588182\cdot 10^{-7})$, an interval containing both $\varepsilon_0 =
  4.810005\cdot10^{-7}$ and the true $\varepsilon = 4.808983\cdot 10^{-7}$ with
  slack factors $\approx 1.17$ on both sides.
* **Least-period subtleties.** $m$ is the least period throughout (D-9908); the
  distinctness of the $x_i$ is used in L-9913.1 Step 2 and L-9913.7. Note that
  L-9905's results hold for non-least periods too, so if a reader prefers to let
  $m$ be *any* period, the squeeze and hence $m \ge 2966$ still hold — the bound
  is then weaker information, since a period is a multiple of the least period.
* **Symbolic object $\to$ actual integer.** Not applicable: no object is
  constructed; the file only constrains hypothetical ones.

**No gaps found** in L-9913.1–.8 and .11. One item is deliberately **PARTIAL**:
the $F = 2^{68}$ entry of L-9913.9 is a certified bracket, not an exact value.

---

## Adversarial tests

**Finite verification, not proof.** All arithmetic is exact (`int`,
`fractions.Fraction`); floating point appears only inside display strings, never
in a decision. Scripts kept at
`scratchpad/l9913_verify.py` and `scratchpad/sieve.py` (session-local); full code
below. Run: `python3 l9913_verify.py` (Python $\ge 3.8$, stdlib only; $\approx 1$ s)
and `python3 sieve.py 1000000000` ($\approx 456$ s; the $10^7$ sweep, which alone
already gives $m \ge 10946$, takes $3.5$ s).

Design notes.
1. **Test 2 vs Test 3/5** deliberately certify $\alpha$ by two logically
   independent routes (big-integer comparison; Lemma-A series with rigorous
   remainder) and check that they agree and that both produce $m^* = 2966$.
2. **Test 4** is exhaustive over $m \le 3000$, i.e. it does not rely on the
   record theory of L-9913.11; **Test 8** re-derives the same answer *through*
   that theory. A bug in either would show as a disagreement.
3. **Test 7** attacks the equivalence of L-9913.4(1) — the form that cannot be
   evaluated at the real parameters — on 400 randomly drawn *feasible* surrogate
   parameters, where the big-integer sides are computable.
4. **Test 6** probes exactly the sensitivity the assignment asked about: how much
   $\varepsilon_0$ may shrink toward $\varepsilon$ (or grow) before $m^*$ moves.
5. **Test 10** checks that the trivial cycle is excluded by the *hypothesis*
   ($x_{\min} > F$) and not silently by the squeeze.

```python
#!/usr/bin/env python3
"""
Adversarial tests / finite verification for L-9913
(research/foundations/L-9913-cycle-length-lower-bound.md).
Agent: fable-02-p8.  Date: 2026-07-25.
FINITE VERIFICATION ONLY -- not a proof.
All arithmetic is exact: Python int / fractions.Fraction.  No floating point is
used in any decision (floats appear only inside f-strings, for display).
Run: python3 l9913_verify.py   (Python >= 3.8, stdlib only)
"""
from fractions import Fraction as Fr
from math import gcd

fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

# ============================================================ Test 1
# Lemma A certificate:  ln 2 > 53056/76545 > 693/1000, from
#   artanh(1/3) > 1/3 + 1/(3*3^3) + 1/(5*3^5) + 1/(7*3^7),  ln 2 = 2 artanh(1/3).
S4 = 2*sum(Fr(1, (2*k+1) * 3**(2*k+1)) for k in range(4))
check("A: partial sum equals 53056/76545", S4 == Fr(53056, 76545))
check("A: 53056/76545 > 693/1000", 53056*1000 > 693*76545)
print(f"Test 1: 2*sum_{{k<4}} 3^-(2k+1)/(2k+1) = {S4} ; "
      f"53056*1000 = {53056*1000} > {693*76545} = 693*76545 -> ln 2 > 693/1000.")

# ============================================================ Test 2
# The two big-integer certificates that carry the whole theorem:
#   C1: 3^111202 > 2^176251   <=>  alpha > L := 176251/111202
#   C2: 3^190537 < 2^301994   <=>  alpha < U := 301994/190537
L = Fr(176251, 111202)
U = Fr(301994, 190537)
check("C1", 3**111202 > 2**176251)
check("C2", 3**190537 < 2**301994)
check("L < U", L < U)
print(f"Test 2: C1 (3^111202 > 2^176251): {3**111202 > 2**176251}; "
      f"C2 (3^190537 < 2^301994): {3**190537 < 2**301994}; "
      f"enclosure width U-L = 1/{(U-L).denominator} ~ {float(U-L):.3e}.")

# ============================================================ Test 3
# Independent, much tighter enclosure of alpha from the same finite-remainder
# lemma used for ln 2 (Lemma A):  for 0<x<1, n>=1,
#   T_n(x) < artanh(x) <= T_n(x) + x^(2n+1)/((2n+1)(1-x^2)),  T_n = sum_{k<n}.
# ln 2 = 2 artanh(1/3), ln(3/2) = 2 artanh(1/5), ln 3 = ln 2 + ln(3/2),
# alpha = ln 3 / ln 2.
def artanh_iv(x, n):
    s = sum(x**(2*k+1) / (2*k+1) for k in range(n))
    return s, s + x**(2*n+1) / ((2*n+1) * (1 - x*x))
def alpha_iv(n):
    a, b = artanh_iv(Fr(1, 3), n); ln2_lo, ln2_hi = 2*a, 2*b
    c, d = artanh_iv(Fr(1, 5), n); l32_lo, l32_hi = 2*c, 2*d
    return (ln2_lo + l32_lo) / ln2_hi, (ln2_hi + l32_hi) / ln2_lo
ALO, AHI = alpha_iv(80)
check("T3: series enclosure inside convergent enclosure", L < ALO < AHI < U)
print(f"Test 3: series enclosure of alpha has width ~{float(AHI-ALO):.2e}; "
      f"consistent with C1/C2 ({L} < alpha < {U}): {L < ALO < AHI < U}")

# ============================================================ Test 4
# Exhaustive determination of m*(F) for F = 10^6, using ONLY C1 and C2.
def eps0(F):
    return Fr(1000, 3*693*F)          # >= eps = 1/(3 F ln 2), since ln2 > .693

def ceil_m_alpha(m, lo, hi):
    """ceil(m*alpha), decided by the enclosure lo < alpha < hi."""
    a, b = m*lo, m*hi
    ka = -((-a.numerator)//a.denominator)
    kb = -((-b.numerator)//b.denominator)
    assert ka == kb, ("ceil undecided", m)
    return ka

def decide(m, F, lo, hi):
    """True/False for Adm_F(m):  ceil(m alpha) - m alpha <= eps0(F)*m,
    decided by the enclosure; asserts if the enclosure is too coarse."""
    K = ceil_m_alpha(m, lo, hi)
    r = Fr(K, m) - eps0(F)            # Adm <=> alpha >= r
    if lo > r:  return True, K
    if hi < r:  return False, K
    raise AssertionError(("enclosure too coarse", m))

F0 = 10**6
first = None
margins = []
for m in range(1, 3001):
    ok, K = decide(m, F0, L, U)
    margins.append((abs(ALO - (Fr(K, m) - eps0(F0))), m, ok))
    if ok and first is None:
        first = (m, K)
    if ok and m <= 2965:
        check(f"no m<=2965 admissible (m={m})", False)
check("m*(10^6) = 2966", first == (2966, 4701))
check("gcd(4701,2966)=1", gcd(4701, 2966) == 1)
tight = min(margins)
print(f"Test 4: exhaustive m = 1..3000 with F = 10^6, eps0 = 1/{eps0(F0).denominator}: "
      f"Adm fails for every m <= 2965 and holds at m = 2966 (K = 4701).  "
      f"Tightest alpha-margin over that range: {float(tight[0]):.3e} at m = {tight[1]} "
      f"(enclosure width {float(U-L):.3e} -- smaller by a factor "
      f"{float(tight[0]/(U-L)):.0f}).")

# displayed certificates for the winner and the runner-up
m1, K1 = 2966, 4701
r1 = Fr(K1, m1) - eps0(F0)
check("cert winner: L >= r1", L >= r1)
m2, K2 = 2301, 3647
r2 = Fr(K2, m2) - eps0(F0)
check("cert runner-up: U <= r2", U <= r2)
print(f"  winner    m=2966: r = K/m - eps0 = {r1};  "
      f"cross-mult {176251*r1.denominator} >= {r1.numerator*111202}: "
      f"{176251*r1.denominator >= r1.numerator*111202}")
print(f"  runner-up m=2301: r = K/m - eps0 = {r2};  "
      f"cross-mult {301994*r2.denominator} <= {r2.numerator*190537}: "
      f"{301994*r2.denominator <= r2.numerator*190537}")

# ============================================================ Test 5
# Same exhaustive computation with the independent series enclosure (Test 3),
# i.e. a completely different certification route for alpha.
first2 = None
for m in range(1, 3001):
    ok, K = decide(m, F0, ALO, AHI)
    if ok:
        first2 = (m, K); break
check("T5: series route reproduces m* = 2966", first2 == (2966, 4701))
print(f"Test 5: independent series enclosure gives the same m* = {first2[0]} "
      f"(K = {first2[1]}).")

# ============================================================ Test 6
# Stability of m* as eps0 shrinks toward the true eps = 1/(3 F ln 2), and the
# exact interval of eps for which m* = 2966.
lo_needed = Fr(ceil_m_alpha(2966, ALO, AHI), 2966) - ALO      # >= f(2966)/2966
hi_allowed = min(Fr(ceil_m_alpha(m, ALO, AHI), m) - AHI for m in range(1, 2966))
print(f"Test 6: m* = 2966 for every eps in [{float(lo_needed):.6e}, "
      f"{float(hi_allowed):.6e}) ; eps0 = {float(eps0(F0)):.6e} lies strictly inside "
      f"(slack factors {float(eps0(F0)/lo_needed):.4f} below, "
      f"{float(hi_allowed/eps0(F0)):.4f} above).")
check("T6: eps0 inside the stability interval",
      lo_needed <= eps0(F0) < hi_allowed)
# and with eps0 replaced by a much sharper rational upper bound for eps:
ln2_lo = 2*artanh_iv(Fr(1, 3), 40)[0]
eps_sharp = Fr(1, 3*F0) / ln2_lo          # > eps, but much closer
check("T6: sharper eps0 still gives 2966", lo_needed <= eps_sharp < hi_allowed)
print(f"        sharper eps0' = 1/(3F * 0.693147...) = {float(eps_sharp):.9e} "
      f"-> same m* = 2966: {lo_needed <= eps_sharp < hi_allowed}")

# ============================================================ Test 7
# The pure-integer form of the test, verified on feasible surrogate parameters.
# Lemma D:  K - m*alpha <= (P/Q)*m   <=>   2^(QK-Pm) <= 3^(Qm).
import random
random.seed(20260725)
bad = 0
for _ in range(400):
    Q = random.choice([1, 2, 3, 5, 7, 10, 50, 100, 1000])
    P = random.randint(1, 3*Q)
    m = random.randint(1, 12)
    K = random.randint(1, 25)
    lhs = 2**(Q*K - P*m) if Q*K - P*m >= 0 else Fr(1, 2**(P*m - Q*K))
    intform = lhs <= 3**(Q*m)
    r = Fr(K, m) - Fr(P, Q)         # rational form: Adm <=> alpha >= r
    assert ALO > r or AHI < r, "enclosure too coarse"
    ratform = (ALO > r)
    if intform != ratform:
        bad += 1
check("T7: integer form == rational form on all samples", bad == 0)
print(f"Test 7: integer-comparison form 2^(QK-Pm) <= 3^(Qm) agreed with the "
      f"enclosure-based rational test on 400/400 random (Q,P,m,K) samples "
      f"(mismatches: {bad}).")

# ============================================================ Test 8
# Independent reduction: Stern-Brocot one-sided best approximations (L-9913.11).
# Records u of f(m) = ceil(m alpha) - m alpha, and interval skipping.
def sb_records(limit, lo, hi):
    u, P, v, Q = 1, 2, 1, 1
    out = []
    while u + v <= limit:
        Alo, Ahi = P - u*hi, P - u*lo
        Blo, Bhi = v*lo - Q, v*hi - Q
        assert Alo > 0 and Blo > 0
        if Alo > Bhi:
            out.append((u, Alo, Ahi, u + v)); u, P = u + v, P + Q
        elif Ahi < Blo:
            v, Q = u + v, Q + P
        else:
            raise AssertionError("undecided SB comparison")
    return out

recs = sb_records(10**14, ALO, AHI)
# skipping: on [u, next_u) every m has f(m) >= A, so Adm needs m >= A/eps0
def sb_lower_bound(F):
    e0 = eps0(F)
    for (u, Alo, Ahi, nu) in recs:
        t = Alo / e0
        if t < nu:
            return u, nu, t
    raise AssertionError("record list exhausted")
u_, nu_, t_ = sb_lower_bound(F0)
check("T8: skipping bound consistent with m*=2966", t_ <= 2966 <= nu_)
print(f"Test 8: Stern-Brocot record reduction for F = 10^6 skips every m < "
      f"{u_} outright and every m < {float(t_):.6g} in the interval "
      f"[{u_}, {nu_}); brute force then finds m* = 2966 inside "
      f"[{-(-t_.numerator//t_.denominator)}, {nu_}).  Records <= 3000: "
      f"{[u for (u,_,_,_) in recs if u <= 3000]}")

# ============================================================ Test 9
# Scale invariance / upward closure (L-9913.3(1)):  Adm(q) => Adm(tq).
viol = 0
adm = {}
for m in range(1, 3001):
    adm[m], _ = decide(m, F0, ALO, AHI)
for q in range(1, 3001):
    if adm[q]:
        for t in range(1, 3001//q + 1):
            if not adm[t*q]:
                viol += 1
check("T9: Adm(q) => Adm(tq)", viol == 0)
print(f"Test 9: scale invariance Adm(q) => Adm(tq) verified for all q,t with "
      f"tq <= 3000 (violations: {viol}).  Admissible m <= 3000: "
      f"{[m for m in range(1,3001) if adm[m]]}")

# ============================================================ Test 10
# Trivial cycle sanity: m = 1, K = 2 must NOT satisfy the squeeze -- the
# hypothesis x_min > F is what excludes it (its x_min = 1).
K, flo, fhi = 2, 2 - AHI, 2 - ALO
check("T10: trivial cycle violates the squeeze", flo > eps0(F0)*1)
check("T10: trivial cycle satisfies L-9905 with x_min = 1",
      1 * (2**2 - 3**1) == 1)
print(f"Test 10: trivial cycle (m=1, K=2, x_min=1): 2 - alpha = "
      f"{float(flo):.6f} > eps0 = {float(eps0(F0)):.3e}, so Adm(1) is false; "
      f"it is excluded by the hypothesis x_min > 10^6, not by the squeeze "
      f"(and x(2^K-3^m) = 1 holds).")

# ============================================================ Test 11
# Sensitivity table.
def mstar(F, cap, lo, hi):
    for m in range(1, cap + 1):
        ok, K = decide(m, F, lo, hi)
        if ok:
            return m, K
    return None
rows = []
for F, cap, lab in ((10**6, 5000, "10^6"), (10**7, 20000, "10^7"),
                    (10**8, 20000, "10^8"), (10**9, 60000, "10^9")):
    m, K = mstar(F, cap, ALO, AHI)
    rows.append((lab, m, K))
    print(f"Test 11: F = {lab:6s} -> m* = {m:6d}, K* = ceil(m* alpha) = {K:6d}, "
          f"K*+m* = {K+m:6d}")
check("T11 F=10^6", rows[0][1:] == (2966, 4701))
check("T11 F=10^7", rows[1][1:] == (10946, 17349))
check("T11 F=10^8", rows[2][1:] == (15601, 24727))
check("T11 F=10^9", rows[3][1:] == (47468, 75235))
# F = 2^68: certified bracket only
F = 2**68
u_, nu_, t_ = sb_lower_bound(F)
ub = None
for (u, Alo, Ahi, nu) in recs:
    if Ahi <= eps0(F)*u:
        ub = u; break
lb = -(-t_.numerator//t_.denominator)
okub, Kub = decide(ub, F, ALO, AHI)
check("T11: bracket endpoints", okub and not decide(lb-1, F, ALO, AHI)[0])
print(f"Test 11: F = 2^68  -> {lb} <= m*(2^68) <= {ub} "
      f"(upper endpoint admissible: {okub}, K = {Kub}); exact value not "
      f"determined here.")

# ============================================================ Test 12
# Legendre near-miss datum (coordinator's report from the L-9910 review) and the
# odd-index convergent list used in the dichotomy corollary L-9913.8.
q, p = 359, 569
val_lo = q*abs(q*ALO - p); val_hi = q*abs(q*AHI - p)
check("T12: 569/359 near-miss ~0.552", Fr(55,100) < val_lo and val_hi < Fr(56,100))
print(f"Test 12: q|q alpha - p| for 569/359 lies in "
      f"({float(val_lo):.4f}, {float(val_hi):.4f}) -- confirms the reported "
      f"near-miss 0.5520..0.5533 against Legendre's 1/2.")
# odd-index convergents (above alpha) with q <= 10^5, recomputed independently
def convergents(lo, hi, n=20):
    a = []; x, y = lo, hi
    for _ in range(n):
        i1, i2 = x.numerator//x.denominator, y.numerator//y.denominator
        if i1 != i2: break
        a.append(i1); x, y = x - i1, y - i2
        if x <= 0: break
        x, y = 1/y, 1/x
    p0, q0, p1, q1 = 1, 0, a[0], 1
    out = [(a[0], 1)]
    for t in a[1:]:
        p0, q0, p1, q1 = p1, q1, t*p1 + p0, t*q1 + q0
        out.append((p1, q1))
    return a, out
digits, conv = convergents(ALO, AHI)
above = [(p, q) for i, (p, q) in enumerate(conv) if i % 2 == 1 and q <= 10**5]
check("T12: CF digits match L-9910.3",
      digits[:15] == [1,1,1,2,2,3,1,5,2,23,2,2,1,1,55])
check("T12: odd-index convergents q<=1e5",
      [q for _, q in above] == [1, 5, 41, 306, 15601, 79335])
print(f"Test 12: CF(alpha) digits {digits[:17]} (first 15 match L-9910.3; "
      f"a_15 = {digits[15]}, a_16 = {digits[16]} confirm L-9910's uncertified "
      f"guess); odd-index (above-alpha) convergent denominators <= 10^5: "
      f"{[q for _, q in above]}.")

# ============================================================ Test 13
# What a cycle at the bound would need: element bounds of L-9905.4 at
# (m, K) = (2966, 4701).
m, K = 2966, 4701
lowbnd = Fr(3**m - 2**m, 2**K - 3**m)
print(f"Test 13: at (m,K) = (2966,4701), L-9905.4 forces every element "
      f">= (3^m-2^m)/(2^K-3^m) ~ {float(lowbnd):.4g}; consistent with (and much "
      f"weaker than) x_min > 10^6 -- so the bound m >= 2966 is not vacuous "
      f"and is not self-contradictory.")
check("T13: 2^K > 3^m at the bound", 2**K > 3**m)

print("RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-25, CPython 3.11, Linux; 0.8 s):**

```text
Test 1: 2*sum_{k<4} 3^-(2k+1)/(2k+1) = 53056/76545 ; 53056*1000 = 53056000 > 53045685 = 693*76545 -> ln 2 > 693/1000.
Test 2: C1 (3^111202 > 2^176251): True; C2 (3^190537 < 2^301994): True; enclosure width U-L = 1/21188095474 ~ 4.720e-11.
Test 3: series enclosure of alpha has width ~7.95e-79; consistent with C1/C2 (176251/111202 < alpha < 301994/190537): True
Test 4: exhaustive m = 1..3000 with F = 10^6, eps0 = 1/2079000: Adm fails for every m <= 2965 and holds at m = 2966 (K = 4701).  Tightest alpha-margin over that range: 6.871e-08 at m = 2966 (enclosure width 4.720e-11 -- smaller by a factor 1456).
  winner    m=2966: r = K/m - eps0 = 4886688017/3083157000;  cross-mult 543409504407000 >= 543409480866434: True
  runner-up m=2301: r = K/m - eps0 = 2527370233/1594593000;  cross-mult 481557518442000 <= 481557542085121: True
Test 5: independent series enclosure gives the same m* = 2966 (K = 4701).
Test 6: m* = 2966 for every eps in [4.122930e-07, 5.588182e-07) ; eps0 = 4.810005e-07 lies strictly inside (slack factors 1.1666 below, 1.1618 above).
        sharper eps0' = 1/(3F * 0.693147...) = 4.808983470e-07 -> same m* = 2966: True
Test 7: integer-comparison form 2^(QK-Pm) <= 3^(Qm) agreed with the enclosure-based rational test on 400/400 random (Q,P,m,K) samples (mismatches: 0).
Test 8: Stern-Brocot record reduction for F = 10^6 skips every m < 2301 outright and every m < 2673.26 in the interval [2301, 2966); brute force then finds m* = 2966 inside [2674, 2966).  Records <= 3000: [1, 3, 5, 17, 29, 41, 94, 147, 200, 253, 306, 971, 1636, 2301, 2966]
Test 9: scale invariance Adm(q) => Adm(tq) verified for all q,t with tq <= 3000 (violations: 0).  Admissible m <= 3000: [2966]
Test 10: trivial cycle (m=1, K=2, x_min=1): 2 - alpha = 0.415037 > eps0 = 4.810e-07, so Adm(1) is false; it is excluded by the hypothesis x_min > 10^6, not by the squeeze (and x(2^K-3^m) = 1 holds).
Test 11: F = 10^6   -> m* =   2966, K* = ceil(m* alpha) =   4701, K*+m* =   7667
Test 11: F = 10^7   -> m* =  10946, K* = ceil(m* alpha) =  17349, K*+m* =  28295
Test 11: F = 10^8   -> m* =  15601, K* = ceil(m* alpha) =  24727, K*+m* =  40328
Test 11: F = 10^9   -> m* =  47468, K* = ceil(m* alpha) =  75235, K*+m* = 122703
Test 11: F = 2^68  -> 8961554427 <= m*(2^68) <= 72057431991 (upper endpoint admissible: True, K = 114208327604); exact value not determined here.
Test 12: q|q alpha - p| for 569/359 lies in (0.5521, 0.5521) -- confirms the reported near-miss 0.5520..0.5533 against Legendre's 1/2.
Test 12: CF(alpha) digits [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4] (first 15 match L-9910.3; a_15 = 1, a_16 = 4 confirm L-9910's uncertified guess); odd-index (above-alpha) convergent denominators <= 10^5: [1, 5, 41, 306, 15601, 79335].
Test 13: at (m,K) = (2966,4701), L-9905.4 forces every element >= (3^m-2^m)/(2^K-3^m) ~ 1179; consistent with (and much weaker than) x_min > 10^6 -- so the bound m >= 2966 is not vacuous and is not self-contradictory.
RESULT: ALL CHECKS PASSED
```

### Test 14 — X-9913: the raised floor (separate script)

**Method.** Exact integer arithmetic, no memoisation, no floating point: for every
odd $n$ with $3 \le n \le N$, iterate $T$ from $n$ until the value drops strictly
below $n$ (even $n$ drop in one step and need no test). The drop lemma of
L-9913.10 then gives "every $n \le N$ reaches 1". Peak memory: $O(1)$.

```python
#!/usr/bin/env python3
"""Exact verification: every n <= N reaches 1 under C.
Induction: if every 1 <= k < n reaches 1 and the T-orbit of n drops below n,
then n reaches 1.  Only odd n need checking (even n drop in one step).
All arithmetic is exact Python int."""
import sys, time
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
t0 = time.time()
maxdrop = 0; argmax = 1; checked = 0
for n in range(3, N+1, 2):
    x = (3*n+1)//2          # first T-step from odd n
    steps = 1
    while x >= n:
        if x & 1: x = (3*x+1)//2
        else:     x >>= 1
        steps += 1
    checked += 1
    if steps > maxdrop: maxdrop, argmax = steps, n
print(f"N = {N}: {checked} odd n checked; every one drops below itself under T.")
print(f"max T-steps to first drop: {maxdrop} at n = {argmax}; {time.time()-t0:.1f}s")
```

**Output (verbatim, same machine):**

```text
N = 1000000: 499999 odd n checked; every one drops below itself under T.
max T-steps to first drop: 176 at n = 626331; 0.4s
N = 10000000: 4999999 odd n checked; every one drops below itself under T.
max T-steps to first drop: 246 at n = 8088063; 3.5s
N = 100000000: 49999999 odd n checked; every one drops below itself under T.
max T-steps to first drop: 376 at n = 63728127; 38.3s
N = 1000000000: 499999999 odd n checked; every one drops below itself under T.
max T-steps to first drop: 395 at n = 217740015; 456.1s
```

**Cross-check against the repository's existing data.** An independent
memoised computation of the *total* $C$-stopping time for all $n \le 10^6$
(script `crosscheck.py`, same session) returns
`max total C-stopping time for n <= 1000000: 524 at n = 837799`, reproducing
X-9901's recorded statistic exactly. This is evidence that the present code and
L-9909's agree on the overlapping range; it is **not** a re-verification of
X-9901 by an independent implementation of a different algorithm, and is not
treated as one.

---

## Remaining uncertainty

1. **The floor is a finite verification, not a theorem.** The Main Theorem is only
   as strong as X-9901. If X-9901 were wrong (i.e. some $n \le 10^6$ did not reach
   $1$), the bound would collapse to L-9915's $m \ge 22$. X-9901 sits in a PROVED
   file, and Test 14's cross-check agrees with its recorded statistic, but a
   reviewer who wants full independence should re-run a sweep from scratch.
2. **X-9913 (the raised floor) is unreviewed.** L-9913.10's $m \ge 47468$ inherits
   PROPOSED status: it rests on a single-implementation, single-run sweep to
   $10^{9}$ with no independent cross-implementation (only the $10^6$ statistic was
   cross-checked, against X-9901). The parallel experiment X-9903 (agent
   fable-02-p10) targets the same quantity; whichever floor it certifies,
   L-9913.9's table converts it into a bound with no further proof. Note that a
   reviewer rejecting X-9913 entirely still keeps the Main Theorem's $m \ge 2966$.
3. **$F = 2^{68}$ row is a bracket, deliberately.** The block-skipping bound gives
   $m^*(2^{68}) \ge 8\,961\,554\,427$ and an explicit admissible $m$ gives
   $m^*(2^{68}) \le 72\,057\,431\,991$; roughly $8$ candidates lie between (a
   heuristic count $\varepsilon_0 M^2$), and pinning the exact value needs an
   Ostrowski-style enumeration of $\{m \le M : f(m) \le \delta\}$ that I did not
   want to state without a full proof. Labelled **PARTIAL**. This affects only an
   illustrative row of a hypothetical table.
4. **Delicacy of $2966$.** $m^*$ is stable under a $\pm 16\%$ perturbation of
   $\varepsilon_0$ (Test 6) — comfortable, but not enormous. If $\varepsilon$ were
   about $1.163\times$ larger, $m^*$ would drop to $2301$. The exact arithmetic and
   the two independent $\alpha$-certifications are what make me confident; a
   reviewer should not accept any float-based re-derivation of this number.
5. **The dichotomy L-9913.8 leans on L-9910** for the certified CF digits and for
   Legendre. I recomputed the digits independently (Test 12) and they agree,
   including L-9910's *uncertified* guess $a_{15} = 1$, $a_{16} = 4$ — which this
   file now confirms via a rigorous enclosure (Lemma A), though I have not written
   out the two integer certificates for those two digits.
6. **What is deliberately not claimed.** No Baker-type input, no comparison with
   the literature, no assertion that $2966$ is anywhere near optimal — the true
   obstruction is expected to be far larger. This file's contribution is that
   $2966$ is *fully certified inside this repository*, end to end.

---

## Suggested next attack

1. **Raise $F$ further** — by far the cheapest improvement per unit of effort, and
   it needs no new mathematics: L-9913.9 is a lookup table, extendable to any $F$
   in milliseconds. The Python sweep of Test 14 costs $\approx 456$ s per decade at
   $10^{9}$ and scales linearly; a sieved C implementation (or a review of X-9903)
   should reach $10^{11}$–$10^{12}$, where the one-sided records of $\log_2 3$ near
   $q_9 = 15601$, $q_{11} = 79335$, $q_{13} = 190537$ determine the next jumps. The
   *independent re-verification* of any such floor is the bottleneck, not the
   computation.
2. **Pin $m^*(2^{68})$ exactly** by proving and implementing an Ostrowski/
   three-distance enumeration of $\{m \le M : f(m) \le \delta\}$ (the DFS over
   digit strings $m = \sum b_{i+1} q_i$, $0 \le b_{i+1} \le a_{i+1}$, pruned by
   tail bounds on $\sum b_{i+1}\eta_i$). This would also make L-9913.11 into a
   complete algorithm rather than a block-skipping heuristic.
3. **Feed $m \ge 2966$ back into the cycle machinery.** L-9905.4's element bounds
   at $(m, K) = (2966, 4701)$ give $x \ge 1179$ only (Test 13), i.e. the two
   constraints are far from saturating each other; combining $m \ge 2966$ with
   L-9912's exponent statistics (more than $m/3$ of the exponents $a_i$ equal $1$)
   and with L-9915's window method might yield a *second*, independent obstruction
   that scales with $m$.
4. **Baker.** The honest way to go far beyond this bound is a lower bound for
   $|K\ln 2 - m\ln 3|$ of the shape $\ge C\,m^{-\kappa}$; combined with the upper
   bound $\le m/(3x_{\min})$ of L-9905.3 it converts a verified floor into a bound
   growing like a power of $x_{\min}$. That is a large, separate project (and an
   in-repo proof of a Baker-type estimate would be a major undertaking); this file
   is explicitly the *elementary* alternative.
5. **Refute or sharpen.** The most likely error sites are listed in Remaining
   uncertainty; a reviewer could attack by (i) recomputing $m^*(10^6)$ with an
   independent CF/lattice method, (ii) checking the two big-integer certificates on
   different software, (iii) hunting for an $m < 2966$ where my decision procedure
   silently used a too-coarse enclosure (the script asserts on that condition, so
   this would have to be an assertion bug).

---
*File authored by fable-02-p8, 2026-07-25. Status PROPOSED per NOTATION.md
conventions; an independent reviewing agent may upgrade after verification.*
