# L-9913 — An unconditional lower bound on the length of a nontrivial Collatz cycle

```text
Claim ID:      L-9913
Title:         Unconditional lower bounds for nontrivial Syracuse cycles: every
               nontrivial cycle has at least 2966 odd elements (elementary, no
               Baker-type input), with the verified floor F as a free parameter
Status:        PROVED
Authoring agent:   fable-02-p8
Reviewing agents:  fable-02-v18 (adversarial review 2026-07-25: PASS)
Created:       2026-07-25
Last updated:  2026-07-25 (fable-02-v18 independent adversarial review; status
               PROPOSED -> PROVED; two documentation fixes; verification note
               appended; no mathematical statement changed)
               2026-07-25 (fable-02-p8 addendum: raised-floor corollaries
               L-9913.12 and L-9913.13 for F = 10^11 and F = 10^12 using the
               new floor X-9903, both marked PROPOSED inside this PROVED file;
               rows added to the L-9913.9 table; Tests 15-22 appended. No
               earlier statement, proof or the verification note was altered.)
               2026-07-25 (fable-02-p8, second addendum after X-9903's review by
               fable-02-v19: m*(10^10) = 190537 computed and certified, a
               three-tier "verification tiers" table added distinguishing the
               most-verified bound m >= 190537 from the strongest bound
               m >= 10781274, the F = 10^10 row added, and the X-9903 status
               wording updated everywhere from "unreviewed" to "reviewed,
               double-implemented only up to 10^10". Still PROPOSED; nothing
               earlier altered.)
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
               X-9903 (experiment packet experiments/X-9903-verified-floor/,
                 agent fable-02-p10; independently reviewed by fable-02-v19,
                 2026-07-25: PASS. Tier caveat recorded by that review and
                 carried here: n <= 10^10 was re-swept contiguously by an
                 independent implementation sharing no code, while
                 (10^10, 10^12] rests on the single original run plus 22M
                 random spot-checks) — used ONLY as the floor hypothesis (V_F)
                 of the addendum L-9913.12/.13, which stay PROPOSED pending
                 review of the addendum itself. Nothing in L-9913.1-.11
                 depends on it.
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
| $10^{10}$ | verified by X-9903, **double-implemented**, reviewed (fable-02-v19) — tier (a) | $190537$ | $301994$ | $492531$ |
| $10^{11}$ | verified by X-9903 (checkpoint), reviewed; single-implementation above $10^{10}$ | $190537$ | $301994$ | $492531$ |
| $10^{12}$ | verified by X-9903, reviewed; single-implementation above $10^{10}$ — tier (b) | $10\,781\,274$ | $17\,087\,915$ | $27\,869\,189$ |
| $2^{68}$ | **not verified anywhere in this repository** — HYPOTHETICAL, literature-scale | $8\,961\,554\,427 \le m^* \le 72\,057\,431\,991$ | — | — |

*(The $10^{11}$ and $10^{12}$ rows were added in the 2026-07-25 addendum; they are
computed, not extrapolated — see L-9913.12 and Tests 16–17. Note the jump from
$47468$ to $190537$ to $10\,781\,274$: $m^*(F)$ is a step function of $F$ with
large, irregular plateaux, so interpolation between rows is meaningless.)*

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

### Addendum of 2026-07-25 — the raised floor $F = 10^{12}$, and verification tiers

> **Status of this addendum.** L-9913.1–.11 and the Main Theorem $m \ge 2966$ are
> **PROVED** (reviewed by fable-02-v18) and are **unchanged**. The two sub-claims
> below are **PROPOSED**: their arithmetic is certified to exactly the same
> standard as the rest of the file (Tests 15–22, exhaustive and exact), but they
> consume a *floor* — X-9903 — that arrived after this file was reviewed, and the
> addendum itself has not yet been reviewed. X-9903 has since passed independent
> adversarial review (fable-02-v19, 2026-07-25), with one distinction that this
> file now carries explicitly: the range $n \le 10^{10}$ was re-swept by a second,
> independent implementation, whereas $(10^{10}, 10^{12}]$ was not. See the
> **verification tiers** table below, which separates the *most-verified* bound
> from the *strongest* bound. Nothing below modifies any earlier statement; a
> reader who rejects X-9903 keeps everything above intact.

**L-9913.12 (raised-floor corollary; PROPOSED).** Suppose $\mathrm{(V}_{10^{12}})$
holds — every $n \le 10^{12}$ reaches $1$ under $C$ — as certified by the
experiment X-9903 (`experiments/X-9903-verified-floor/`, agent fable-02-p10), with
a separately certified checkpoint at $\mathrm{(V}_{10^{11}})$. Then:

1. $m^*(10^{11}) = 190537$ with $K^*= \lceil 190537\,\alpha\rceil = 301994$ and
   $\gcd(301994, 190537) = 1$;
2. $m^*(10^{12}) = 10\,781\,274$ with
   $K^* = \lceil 10781274\,\alpha\rceil = 17\,087\,915$ and $\gcd = 1$;
3. consequently **every nontrivial $S$-cycle satisfies**
   $$m \;\ge\; 10\,781\,274, \qquad q = \frac{m}{\gcd(K,m)} \;\ge\; 10\,781\,274,
     \qquad K \;\ge\; 17\,087\,915,$$
   its $T$-cycle has least period $K \ge 17\,087\,915$, its $C$-cycle has least
   period $K+m \ge 27\,869\,189$, and all of its $\ge 10\,781\,274$ elements
   exceed $10^{12}$. Under the weaker checkpoint $\mathrm{(V}_{10^{11}})$ alone:
   $m \ge 190\,537$, $K \ge 301\,994$, $C$-length $\ge 492\,531$.
4. Both minimisers are **exactly** odd-index convergent denominators of $\alpha$:
   $190537 = q_{13}$ (with $301994 = p_{13}$) and $10781274 = q_{15}$ (with
   $17087915 = p_{15}$) — in contrast with $F = 10^6$, where the minimiser $2966$
   is a semiconvergent.
5. *(Added after X-9903's review.)* $m^*(10^{10}) = 190537$ likewise, with
   $K^* = 301994$ — the same value as $m^*(10^{11})$, because both floors lie in
   the single plateau $(7.2176\cdot 10^{9},\ 9.8478\cdot 10^{11}]$ of the remark
   below. This is the bound of **tier (a)**: the strongest one whose floor has
   been computed twice by independent implementations.

*Remark (plateau — how much further verification is worth).* Admissibility of a
fixed $m$ is monotone in $F$: $\mathrm{Adm}_F(m) \iff F \le F_{\max}(m) :=
\frac{1000\,m}{2079\,f(m)}$. Hence $m^*(F)$ is a nondecreasing step function whose
jumps are the numbers $F_{\max}(m)$, and the exhaustive scans give the exact
plateaux. This is **exhaustively certified** (Test 21): every $m \le 10\,781\,274$
is examined, and the successive record-holders of $m/f(m)$ — equivalently of
$F_{\max}(m)$ — are the jump points. The comparison needs no $\alpha$ at all: with
$f(m) = K_m - m\alpha$,
$$m\,f(m') - m'\,f(m) \;=\; m\,K_{m'} - m'\,K_m,$$
a pure integer test. There are $38$ jump points below $10\,781\,274$; the last
five give the plateaux:

| plateau of $F$ | $m^*(F)$ |
|---|---|
| $(2.8587828883\cdot 10^{8},\ 1.4479896944\cdot 10^{9}]$ | $47468$ |
| $(1.4479896944\cdot 10^{9},\ 7.2176350614\cdot 10^{9}]$ | $79335$ |
| $(7.2176350614\cdot 10^{9},\ 9.8478191629\cdot 10^{11}]$ | $190537$ |
| $(9.8478191629\cdot 10^{11},\ 2.9446434989\cdot 10^{14}]$ | $10\,781\,274$ |

Two consequences worth stating plainly. **(i)** The new floor $10^{12}$ clears the
last transition by only $1.55\%$ — at any floor below $9.848\cdot 10^{11}$ the bound
would still be $190537$. **(ii)** Raising the verified floor any further buys
**nothing at all** for this bound until $F$ exceeds $2.9446\cdot 10^{14}$: the
whole range $10^{12} < F \le 2.94\cdot 10^{14}$ gives the same
$m^* = 10\,781\,274$. (The upper plateau endpoint is $F_{\max}(10781274)$; the
lower is $F_{\max}(190537)$, which is the largest $F_{\max}$ over all
$m < 10\,781\,274$ — established exhaustively by Test 21, and independently
implied by Test 16, whose closest failure at $F = 10^{12}$ is precisely
$m = 190537$.)

*Certificates.* With the certified decimal enclosure (Lemma A, $n = 80$; Test 15)
$$\frac{158496250072115618145}{10^{20}} \;<\; \alpha \;<\; \frac{158496250072115618146}{10^{20}},$$
writing $N := 158496250072115618145$ and $r := K/m - \varepsilon_0(F)$
(so $\mathrm{Adm}_F(m) \iff \alpha \ge r$, L-9913.4(2)):

| | $r$ | integer certificate |
|---|---|---|
| $F = 10^{12}$, **winner** $m = 10781274$, $K = 17087915$ | $\frac{845851792499743303}{533673063000000000}$ | $N \cdot 533673063000000000 = 84585179249999912825580528135000000000 \;\ge\; 84585179249974330300000000000000000000 = 845851792499743303\cdot 10^{20}$ |
| $F = 10^{12}$, **closest failure** $m = 190537$, $K = 301994$ | $\frac{627845525999809463}{396126423000000000}$ | $(N{+}1)\cdot 396126423000000000 = 62784552599980651858608871758000000000 \;\le\; 62784552599980946300000000000000000000 = 627845525999809463 \cdot 10^{20}$ |
| $F = 10^{11}$, **winner** $m = 190537$, $K = 301994$ | $\frac{62784552599809463}{39612642300000000}$ | $N \cdot 39612642300000000 = 6278455259998065185821274533500000000 \;\ge\; 6278455259980946300000000000000000000 = 62784552599809463\cdot 10^{20}$ |
| $F = 10^{11}$, **closest failure** $m = 79335$, $K = 125743$ | $\frac{580932659998237}{366527700000000}$ | $(N{+}1)\cdot 366527700000000 = 58093265997557371653131644200000000 \;\le\; 58093265999823700000000000000000000 = 580932659998237\cdot 10^{20}$ |

The two big-integer certificates of Lemma B(iii) are **not** usable at these
floors: their enclosure width is $4.72\cdot 10^{-11}$ while the closest failure at
$F = 10^{12}$ ($m = 190537$) has margin only $7.433\cdot 10^{-15}$ in $\alpha$-units
(the winner's margin is $4.794\cdot 10^{-13}$). The decimal enclosure above, whose
justification is the already-proved Lemma A, is used instead; it is consistent with
$L_0, U_0$ (Test 15).

*Provenance of the floor (recorded, not verified here).* X-9903 reports: $877$ s
wall clock on $4$ cores; four accelerations each proved in its README (descent
induction with an order-independence corollary licensing multithreading; the
Terras $K$-step identity; a mod-$2^{22}$ descent sieve removing $97.78\%$ of the
range; a peak-decomposition lemma); a `uint64` kernel that **refuses rather than
wraps**, promoting to `unsigned __int128` (promotion fired $17\,121$ times, zero
guard aborts, exit $0$) — the maximum excursion over the range is
$4.0\cdot 10^{23}$ at $n = 871\,673\,828\,443$, i.e. $21\,714\times$ above $2^{64}$,
so a naive $64$-bit sweep would have been **silently wrong**; cross-checks: a
Python arbitrary-precision reference agreeing by checksum on all $n \le 10^6$
($\sum \sigma_C = 131\,434\,424$, max $524$ at $n = 837799$ — the X-9901 gate, which
is also the gate this file's own X-9913 passes), digest-identical runs under three
optimisation levels and five sieve moduli, and an independent byte-for-byte
reproduction of L-9909's survivor tables mod $2 \dots 256$. **This file does not
re-verify any of that**; it records it as the provenance of a hypothesis, and
labels the corollary PROPOSED accordingly.

*Review outcome and verification tiers (added 2026-07-25).* X-9903 has since been
independently reviewed — **fable-02-v19, PASS**: all six of its lemmas re-derived
by hand, the overflow guard audited as unbypassable with the refusal predicate
confirmed exactly right, sieve soundness checked exhaustively to $10^8$,
order-independence confirmed sound, and L-9909's survivor lists re-derived *from
the lemmas* rather than compared against hard-coded values. That review also
recorded a distinction which this file now carries, because it changes which
bound rests on what:

* $n \le 10^{10}$ is **double-implemented**: re-swept contiguously by a second
  implementation sharing no code with the first (raw $C$ map, unconditional
  `unsigned __int128`, no sieve, no memoisation), agreeing on every extreme,
  argmax and checksum;
* $(10^{10},\, 10^{12}]$ was **not re-swept**: it rests on the single original
  $877$ s run plus $22$M random spot-checks, with the *mathematics* of the
  accelerations independently re-derived.

Accordingly, $m^*(10^{10}) = 190537$ was computed by the same certified method
(Test 22; winner $m = 190537$, $K = 301994$, closest failure $m = 79335$,
$K = 125743$; certificates below), and the file's bounds split into three tiers:

| tier | bound | floor | standing of the floor |
|---|---|---|---|
| **(a) most-verified** | $m \ge 190\,537$, $K \ge 301\,994$, $C$-length $\ge 492\,531$ | $F = 10^{10}$ | X-9903 **double-implemented** (two independent sweeps, no shared code) **and** independently reviewed (fable-02-v19) |
| **(b) strongest** | $m \ge 10\,781\,274$, $K \ge 17\,087\,915$, $C$-length $\ge 27\,869\,189$ | $F = 10^{12}$ | X-9903 single-implementation above $10^{10}$ (+22M spot-checks), with its mathematics independently re-derived and reviewed |
| **(c) hypothetical** | $8\,961\,554\,427 \le m^*(2^{68}) \le 72\,057\,431\,991$ | $F = 2^{68}$ | **not verified anywhere in this repository** — PARTIAL, unchanged |

(For completeness the reviewed-floor tier of the *Main Theorem* sits below all
three: $m \ge 2966$ at $F = 10^6$, whose floor X-9901 is reviewed and was
re-derived in this file's X-9913.)

**Planning consequence (the most useful single fact here).** By the certified
plateau below, $m^*(F)$ is *constant* at $10\,781\,274$ for every $F$ in
$(9.8478\cdot 10^{11},\ 2.9446\cdot 10^{14}]$. Therefore a second independent
sweep of $(10^{10}, 10^{12}]$ would **confirm** tier (b) — promoting it to
double-implemented — but could never **improve** it; and *improving the bound at
all* requires pushing the verified floor past $2.9446\cdot 10^{14}$, a
$\approx 300\times$ jump beyond the current $10^{12}$. Verification effort should
therefore be spent either on hardening $(10^{10}, 10^{12}]$ (which buys standing,
not numbers) or on a $\ge 3\cdot 10^{14}$ sweep (which buys numbers); anything in
between buys neither.

*Certificates for tier (a)* ($F = 10^{10}$, $\varepsilon_0 = 1/20\,790\,000\,000$;
notation as above, $N = 158496250072115618145$):

| | $r$ | integer certificate |
|---|---|---|
| **winner** $m = 190537$, $K = 301994$ | $\frac{6278455259809463}{3961264230000000}$ | $N \cdot 3961264230000000 = 627845525999806518582127453350000000 \;\ge\; 627845525980946300000000000000000000 = 6278455259809463 \cdot 10^{20}$ |
| **closest failure** $m = 79335$, $K = 125743$ | $\frac{58093265998237}{36652770000000}$ | $(N{+}1)\cdot 36652770000000 = 5809326599755737165313164420000000 \;\le\; 5809326599823700000000000000000000 = 58093265998237\cdot 10^{20}$ |

**L-9913.13 (does the convergent strengthening now buy anything? — No; PROPOSED).**
For a floor $F$ define the **Legendre window**
$$W(F) \;:=\; \Bigl\{\, q \in \mathbb{Z}^{+} \;:\; 2q^2 \,\varepsilon_0(F) \le 1 \,\Bigr\}
\;=\; \Bigl\{\, q \ge 1 \;:\; q^2 \le \tfrac{2079}{2000} F \,\Bigr\}.$$
Then, assuming $\mathrm{(V}_F)$:

1. **(Applicability.)** If the reduced denominator $q$ of a nontrivial cycle lies
   in $W(F)$, then $|\alpha - p/q| < 1/(2q^2)$, so by Legendre (L-9910.1) $p/q$ is a
   convergent of $\alpha$, necessarily odd-index (L-9910.3), i.e.
   $q \in \{1, 5, 41, 306, 15601, 79335, 190537, 10781274, \dots\}$. (This is the
   reviewer's condition $x_{\min} > \frac{2}{3\ln 2}q^2$ in exact rational form:
   $\frac{2000}{2079} > \frac{2}{3\ln 2}$ because $\ln 2 > \frac{693}{1000}$.)
2. **(The numbers.)** $\max W(10^9) = 32241$, $\max W(10^{11}) = 322412$,
   $\max W(10^{12}) = 1\,019\,558$, with integer certificates
   $1019558^2 = 1\,039\,498\,515\,364 \le 1\,039\,500\,000\,000 = \frac{2079}{2000}10^{12}$
   (and likewise for the others).
3. **(Verdict at $F = 10^{12}$: no gain.)** The direct bound of L-9913.12 already
   gives $q \ge 10\,781\,274 > 1\,019\,558 = \max W(10^{12})$, so **the Legendre
   window lies entirely below the direct bound and the convergent branch is
   vacuous**: it excludes nothing that L-9913.12 has not already excluded. The
   larger floor therefore buys a larger number, not a structurally different
   argument.
4. **(Why, and why $10^{11}$ is different.)** At $F = 10^{9}$ the window
   ($q \le 32241$) also sat below the direct bound $47468$ — the reviewer's
   observation. At $F = 10^{11}$ the window ($q \le 322412$) *does* overlap the
   direct bound $190537$, and there the dichotomy refines usefully: the only
   convergent denominator in $[190537, 322412]$ is $190537$ itself, so
   $q = 190537$ **or** $q > 322412$. At $F = 10^{12}$ the direct bound overshoots
   the window again, and by a factor $10.6$.
5. **(No bootstrap.)** Re-applying (1) with the improved $q \ge 10781274$ would
   need $x_{\min} \ge \frac{2}{3\ln2}q^2 > 1.11\cdot 10^{14}$, far beyond
   $F = 10^{12}$; and the only cycle-side lower bound on $x_{\min}$ available from
   L-9905.4, namely $x_{\min} \ge (3^m-2^m)/(2^K-3^m) \ge 1/(2f(m))$ with
   $f(m) \le \varepsilon_0 m \le 5.19\cdot 10^{-6}$, yields merely
   $x_{\min} \ge 9.6\cdot 10^{4}$. The loop does not close.

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
> (by (3)). They give the same *numerical* bound for the trivial reason that
> $\mathrm{Adm}_F$ is one predicate on one index set, so
> $\min\{m : \mathrm{Adm}_F(m)\}$ and $\min\{q : \mathrm{Adm}_F(q)\}$ are the same
> number $m^*(F)$ by definition — not because of upward closure. (Upward closure,
> part (1), is a separate true fact, used only to describe the *shape* of the
> admissible set; it is not needed for either bound.) The stronger of the two
> conclusions,
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
step (each of $u, v$ is nondecreasing). *Both branches are taken infinitely
often*, so the record sequence $u_1 < u_2 < \dots$ is infinite: if from some
stage on only the $A<B$ branch were taken, $B$ would decrease by the fixed
$A > 0$ at each step and become $\le 0$ after $\lceil B/A\rceil$ steps,
contradicting $B \in (0,1)$; symmetrically for the other branch. (Needed only so
that the block-skipping consequence below covers every $m$; the Main Theorem does
not use this lemma at all.) Also, by construction $A = P - u\alpha$ with $P$ an integer and
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

### Proof of L-9913.12 (raised floor)

Every step is one of the already-proved steps of this file, with the parameter $F$
changed; **no new mathematics is used**, which is precisely why the file was
written with $F$ free.

1. **Floor.** $\mathrm{(V}_{10^{12}})$ is supplied by X-9903 (hypothesis, recorded
   provenance; not verified here). L-9913.1 then gives $x_{\min} > 10^{12}$ for
   every nontrivial $S$-cycle.
2. **Squeeze and admissibility.** L-9913.2 and L-9913.3 apply verbatim with
   $\varepsilon_0(10^{12}) = \frac{1000}{2079\cdot 10^{12}} =
   \frac{1}{2\,079\,000\,000\,000}$: every nontrivial cycle satisfies
   $\mathrm{Adm}_{10^{12}}(m)$ and $\mathrm{Adm}_{10^{12}}(q)$, hence
   $m \ge q \ge m^*(10^{12})$.
3. **The computation.** $m^*(10^{12}) = 10\,781\,274$ and
   $m^*(10^{11}) = 190\,537$ are *exhaustive finite verifications*, identical in
   form to L-9913.5: for **every** $m$ from $1$ to the stated value, $\lceil
   m\alpha\rceil$ is determined by L-9913.4(3) and $\mathrm{Adm}_F(m)$ is decided
   by L-9913.4(2) against a certified enclosure of $\alpha$; all $m$ below the
   stated value fail, the stated value succeeds (Tests 16, 17; $10\,781\,274$
   decisions for $F = 10^{12}$, each exact, with the two extreme certificates
   displayed in the Statement). Because the closest failure at $F = 10^{12}$ has
   $\alpha$-margin $7.433\cdot 10^{-15}$, the enclosure used is the Lemma-A decimal
   enclosure of width $10^{-20}$ (a factor $7.4\cdot 10^{5}$ of slack), not the
   coarser $L_0, U_0$ of Lemma B(iii).
4. **The conclusions.** $K > m\alpha \ge 10781274\,\alpha \notin \mathbb{Z}$ and
   $K \in \mathbb{Z}$ give $K \ge \lceil 10781274\,\alpha\rceil = 17\,087\,915$
   (the ceiling is determined by the decimal enclosure: multiplying $N/10^{20}$ and
   $(N{+}1)/10^{20}$ by $10781274$ gives the same ceiling). The $C$- and $T$-cycle
   lengths $K+m \ge 27\,869\,189$ and $K \ge 17\,087\,915$ are L-9913.7, and the
   element bound $> 10^{12}$ is step 1. Identically for $F = 10^{11}$.
5. **Item 4 of the Statement** ($m^*$ equals $q_{13}$, resp. $q_{15}$) is an
   observation, verified in Test 17 by recomputing the convergents of $\alpha$ from
   the same certified enclosure; it is used only in L-9913.13(4) and in the
   Suggested next attack.
6. **Item 5** ($m^*(10^{10}) = 190537$) is the same exhaustive computation once
   more, at $\varepsilon_0(10^{10}) = 1/20\,790\,000\,000$: every $m \le 190537$ is
   decided, all below fail, $190537$ succeeds (Test 22, with both extreme
   certificates displayed in the Statement). It is *not* an inference from the
   plateau table — the plateau merely explains why it coincides with
   $m^*(10^{11})$. $\blacksquare$

### Proof of L-9913.13 (the Legendre window is vacuous at $F = 10^{12}$)

**(1) Applicability.** Let a nontrivial $S$-cycle be given, $K/m = p/q$ in lowest
terms. The proof of L-9913.3(3) established $0 < p/q - \alpha < \varepsilon_0(F)$.
If $q \in W(F)$, i.e. $2q^2\varepsilon_0(F) \le 1$, then
$$|\alpha - p/q| \;=\; p/q - \alpha \;<\; \varepsilon_0(F) \;\le\; \frac{1}{2q^2},$$
so Legendre's criterion (L-9910.1, PROVED) applies to the reduced fraction $p/q$:
it is a convergent of $\alpha$. Since $p/q > \alpha$ (L-9905.2) and the convergents
above $\alpha$ are exactly the odd-index ones (L-9910.3, PROVED), it is an
odd-index convergent. The displayed form of $W(F)$ is the same statement cleared of
fractions:
$$2q^2\,\frac{1000}{2079F} \le 1 \iff 2000\,q^2 \le 2079\,F \iff q^2 \le \tfrac{2079}{2000}F .$$
*(Equivalence with the reviewer's form.* $x_{\min} > \frac{2}{3\ln 2}q^2$ suffices
because $\frac{1}{3x_{\min}\ln 2} < \frac{1}{2q^2}$; and $x_{\min} > F \ge
\frac{2000}{2079}q^2$ implies it, since $\frac{2000}{2079} > \frac{2}{3\ln 2}
\iff 6000\ln 2 > 4158 \iff \ln 2 > 0.693$, which is Corollary A1. So the rational
window $W(F)$ is the exact, certificate-friendly version of that condition.)*

**(2) The numbers.** $\max W(F) = \lfloor\sqrt{2079F/2000}\rfloor$, computed by
exact integer square root (Test 18): $32241$ at $F = 10^9$, $322412$ at
$F = 10^{11}$, $1\,019\,558$ at $F = 10^{12}$, each with a two-sided integer
certificate, e.g. $1019558^2 = 1\,039\,498\,515\,364 \le 1\,039\,500\,000\,000 <
1\,041\,537\,632\,481 = 1019559^2$.

**(3) Verdict.** At $F = 10^{12}$, L-9913.12 gives $q \ge 10\,781\,274$, while
every $q \in W(10^{12})$ satisfies $q \le 1\,019\,558 < 10\,781\,274$. Hence no
cycle can have $q \in W(10^{12})$ *at all* — the hypothesis of (1) is never
satisfied, so its conclusion is vacuous and adds nothing. Formally: the disjunction
"either $q \notin W(F)$, or $p/q$ is an odd-index convergent" is implied by
$q > \max W(F)$, which L-9913.12 already gives.

**(4) Contrast.** At $F = 10^{9}$: $\max W = 32241 < 47468 = m^*(10^9)$ — vacuous
for the same reason (this is the reviewer's recorded observation, now explained by
a single inequality). At $F = 10^{11}$: $\max W = 322412 \ge 190537 = m^*(10^{11})$,
so the window is *not* vacuous, and since the convergent denominators of $\alpha$
in $[190537, 322412]$ are exactly $\{190537\}$ (consecutive convergent denominators
are $q_{13} = 190537$ and $q_{14} = 10\,590\,737$, L-9910.3), the dichotomy refines
to: $q = 190537$ or $q > 322412$. The *minimum* is unchanged, so the headline bound
at $F = 10^{11}$ stays $190537$; but a future argument excluding the single value
$q = 190537$ would jump that floor's bound to $322413$.

**(5) No bootstrap.** Applying (1) again with the improved bound $q \ge 10781274$
would require $F \ge \frac{2000}{2079}q^2 > 1.11\cdot 10^{14}$, i.e. a verified
floor two orders of magnitude beyond X-9903. The only lower bound on $x_{\min}$
available from the cycle side is L-9905.4's
$x_{\min} \ge (3^m - 2^m)/(2^K - 3^m)$, which for $K - m\alpha = f(m) \le 1$
gives $2^K - 3^m = 3^m(2^{f(m)} - 1) \le 3^m f(m)$ and
$3^m - 2^m \ge 3^m/2$ (valid for $m \ge 2$, since $(2/3)^m \le 4/9 < 1/2$), hence
$x_{\min} \ge 1/(2f(m))$; with $f(m) \le \varepsilon_0(10^{12})\,m$ at
$m = 10781274$ this is only $x_{\min} \ge 9.6\cdot 10^{4}$ — nine orders of
magnitude short of what (1) would need. The loop does not close. $\blacksquare$

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
| **X-9903** (every $n \le 10^{12}$ reaches 1; experiment packet, agent fable-02-p10) | reviewed: fable-02-v19 PASS — but **double-computed only up to $10^{10}$** | L-9913.12, L-9913.13 **only** ($10^{12}$ for tier (b), $10^{10}$ for tier (a)) | separated from the Main Theorem; both sub-claims stay PROPOSED, and the tier table records which floor carries which bound |
| L-9910.1 + L-9910.3 (Legendre; consecutive convergents $q_{13}, q_{14}$) | PROVED | L-9913.13(1),(4) | **no** (L-9913.13's verdict is "no gain") |

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

* **Addendum (2026-07-25), L-9913.12/.13.** The same audit was re-run for the two
  new sub-claims. (i) *Status hygiene:* the new floor $\mathrm{(V}_{10^{12}})$ comes
  from an **unreviewed** experiment, so both sub-claims are labelled PROPOSED and
  are quarantined from the Main Theorem — no earlier statement cites them.
  (ii) *Exhaustiveness:* Test 16 decides every $m \le 10\,781\,274$ individually;
  the record lemma is not used to shorten the search, so no structural assumption
  enters. (iii) *Precision:* the closest failure has $\alpha$-margin
  $7.433\cdot10^{-15}$, which is why the coarser $L_0/U_0$ enclosure is explicitly
  *not* used; the enclosure actually used has width $10^{-20}$, a factor
  $7.4\cdot 10^{5}$ of slack, and the decision procedure asserts rather than
  guesses if that ever fails. (iv) *Safe direction:* $\varepsilon_0 > \varepsilon$
  still holds by Corollary A1, and the substitution is again conservative;
  moreover $\varepsilon_0 - \varepsilon = \frac{1}{3F}\left(\frac{1000}{693} -
  \frac{1}{\ln 2}\right) < 1.03\cdot 10^{-16}$ at $F = 10^{12}$, far below both
  displayed margins ($7.433\cdot10^{-15}$ and $4.794\cdot10^{-13}$), so
  $m^*(10^{12}) = 10\,781\,274$ is unchanged if the exact $\varepsilon$ is used
  instead of $\varepsilon_0$. (v) *Vacuity, stated as such:* L-9913.13's conclusion
  is that a branch is **empty**; it is recorded as "no gain", not dressed up as an
  improvement.

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

### Tests 15–22 — the raised floor (addendum of 2026-07-25)

**Finite verification, not proof.** Same discipline as above: exact `int` /
`Fraction` arithmetic, no floating point in any decision. Script kept at
`scratchpad/l9913_verify_F12.py` (session-local); full code and verbatim output
below. Run: `python3 l9913_verify_F12.py` (Python $\ge 3.8$, stdlib only;
$\approx 14$ s).

Design notes.
1. **Test 16 is exhaustive**, not structural: it decides $\mathrm{Adm}_F(m)$ for
   every single $m$ from $1$ to $m^*(F)$ — $10\,781\,274$ separate exact decisions
   at $F = 10^{12}$ — exactly as Test 4 did at $F = 10^6$. The record lemma
   L-9913.11 is *not* used to shorten it (it would only rule out $m < 193\,514$
   there, since the one-sided records of $\alpha$ jump straight from $190537$ to
   $10\,781\,274$).
2. **Test 17 re-runs the same search along a different code path**: an *additive*
   recurrence for $m\alpha$ (instead of a multiplication per $m$), at a different
   scale ($2^{100}$ instead of $2^{160}$) and from a different series depth
   ($n = 55$ instead of $n = 80$). Both agree.
3. A third, structurally different check was run for $F = 10^{11}$ only: a digit-DFS
   enumeration of $\{m \le 3\cdot 10^{5} : f(m) \le \varepsilon_0 \cdot 3\cdot 10^{5}\}$
   returned the single element $\{190537\}$, confirming both the minimiser and that
   nothing smaller can qualify. The same enumeration did **not** finish within the
   session's time budget at $M = 10\,781\,274$, so for $F = 10^{12}$ the evidence is
   the two exhaustive scans (Tests 16 and 17), not three methods.
4. **Test 18** answers the coordinator's item 4 (does the L-9910 strengthening now
   beat the direct bound?) with exact integer certificates at all three floors.
5. **Tests 20 and 21** compute the plateau endpoints
   $F_{\max}(m) = 1000m/(2079 f(m))$, which is where the practical advice lives:
   the present floor clears the last jump by $1.55\%$, and the *next* jump is not
   until $F > 2.9446\cdot 10^{14}$. Test 21 is exhaustive over all
   $m \le 10\,781\,274$ and uses a pleasant simplification: comparing
   $m/f(m)$ with $m'/f(m')$ is a **pure integer** test, because
   $m f(m') - m' f(m) = m K_{m'} - m' K_m$ — the $\alpha$-terms cancel exactly.
   It finds $38$ jump points in total.

```python
#!/usr/bin/env python3
"""
Adversarial tests for the raised-floor addendum of L-9913 (Tests 15-22):
m*(10^11), m*(10^12), and the Legendre-window question.
Agent: fable-02-p8.  Date: 2026-07-25.
FINITE VERIFICATION ONLY -- not a proof.
Exact arithmetic throughout (int / fractions.Fraction); floats appear only in
display strings, never in a decision.
Run: python3 l9913_verify_F12.py   (Python >= 3.8, stdlib only; ~25 s)
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
import time

fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

# ---------- certified enclosure of alpha = log2(3) (Lemma A of L-9913) --------
def artanh_iv(x, n):
    s = sum(x**(2*k+1) / (2*k+1) for k in range(n))
    return s, s + x**(2*n+1) / ((2*n+1) * (1 - x*x))
def alpha_iv(n):
    a, b = artanh_iv(Fr(1, 3), n); l2lo, l2hi = 2*a, 2*b      # ln 2
    c, d = artanh_iv(Fr(1, 5), n)                              # ln(3/2)
    l3lo, l3hi = l2lo + 2*c, l2hi + 2*d                        # ln 3
    return l3lo / l2hi, l3hi / l2lo
ALO, AHI = alpha_iv(80)

def eps0(F):
    return Fr(1000, 3*693*F)

# ============================================================ Test 15
# A decimal enclosure of alpha at the precision the new floors need, plus the
# margin arithmetic showing why the two big-integer certificates L0/U0 of
# Lemma B(iii) (width 4.72e-11) are NOT sufficient here.
D = 10**20
N = (ALO.numerator*D)//ALO.denominator
check("T15: decimal enclosure brackets alpha", Fr(N, D) < ALO and AHI < Fr(N+1, D))
L0, U0 = Fr(176251, 111202), Fr(301994, 190537)
print(f"Test 15: certified decimal enclosure (Lemma A, n = 80 terms):")
print(f"         {N}/10^20 < alpha < {N+1}/10^20   (width 10^-20)")
print(f"         Lemma B(iii) enclosure width U0-L0 = {float(U0-L0):.3e} is too coarse "
      f"for these floors (smallest margin below is 7.4e-15), so the decimal "
      f"enclosure is used; both are certified, and L0 < {N}/10^20 < "
      f"{N+1}/10^20 < U0 holds: {L0 < Fr(N,D) and Fr(N+1,D) < U0}")

# ============================================================ Test 16
# Exhaustive scan for m*(10^11) and m*(10^12) -- every m from 1 up to the answer
# is decided individually, in exact integer arithmetic at scale 2^160.
SC = 1 << 160
A_LO = (ALO.numerator*SC)//ALO.denominator          # A_LO/SC < alpha
A_HI = -((-AHI.numerator*SC)//AHI.denominator)      # alpha < A_HI/SC
check("T16: scaled alpha gap is 1 ulp", A_HI - A_LO == 1)

def scan(F, cap):
    """Exhaustive: returns (m*, K*, (closest failing m, its K, margin))."""
    e0 = eps0(F); P, Q = e0.numerator, e0.denominator
    best = None
    for m in range(1, cap+1):
        lo, hi = m*A_LO, m*A_HI
        K = hi//SC + 1
        assert lo//SC + 1 == K, ("ceiling undetermined", m)
        rhs = P*m*SC
        if Q*(K*SC - lo) <= rhs:                     # certified admissible
            return m, K, best
        assert Q*(K*SC - hi) > rhs, ("enclosure too coarse", m)
        if Q*(K*SC - hi) <= 20*rhs:                  # cheap filter, then exact
            marg = Fr(K, m) - AHI - e0               # <= f(m)/m - eps0
            if best is None or marg < best[2]:
                best = (m, K, marg)
    raise AssertionError(("no admissible m below cap", F, cap))

for F, cap, lab in ((10**11, 300000, "10^11"), (10**12, 11000000, "10^12")):
    t0 = time.time()
    m, K, (mf, Kf, marg) = scan(F, cap)
    print(f"Test 16: F = {lab}: exhaustive over m = 1..{m}: m* = {m}, "
          f"K* = {K}, K*+m* = {K+m}; closest failure m = {mf} (K = {Kf}), "
          f"margin f(m)/m - eps0 >= {float(marg):.4e}   [{time.time()-t0:.1f}s]")
    if F == 10**11:
        check("T16: m*(10^11) = 190537", (m, K, mf) == (190537, 301994, 79335))
    else:
        check("T16: m*(10^12) = 10781274",
              (m, K, mf) == (10781274, 17087915, 190537))
    check(f"T16: gcd = 1 at {lab}", gcd(K, m) == 1)

# ============================================================ Test 17
# Independent recomputation: (a) additive recurrence instead of multiplication,
# at a different scale (2^100) and a different series depth (n = 55);
# (b) for 10^11, an independent digit-DFS enumeration of {m : f(m) <= delta}.
BLO, BHI = alpha_iv(55)
SC2 = 1 << 100
B_LO = (BLO.numerator*SC2)//BLO.denominator
B_HI = -((-BHI.numerator*SC2)//BHI.denominator)
def scan_additive(F, cap):
    e0 = eps0(F); P, Q = e0.numerator, e0.denominator
    lo = hi = 0
    for m in range(1, cap+1):
        lo += B_LO; hi += B_HI                       # lo/SC2 < m*alpha < hi/SC2
        K = hi//SC2 + 1
        assert lo//SC2 + 1 == K, ("ceiling undetermined", m)
        rhs = P*m*SC2
        if Q*(K*SC2 - lo) <= rhs:
            return m, K
        assert Q*(K*SC2 - hi) > rhs, ("enclosure too coarse", m)
    return None
t0 = time.time()
r11 = scan_additive(10**11, 300000)
r12 = scan_additive(10**12, 11000000)
check("T17a: additive scan reproduces both", r11 == (190537, 301994)
      and r12 == (10781274, 17087915))
print(f"Test 17: additive scan (scale 2^100, 55-term series) reproduces "
      f"m*(10^11) = {r11[0]} and m*(10^12) = {r12[0]}   [{time.time()-t0:.1f}s]")

def cf_digits_convergents(lo, hi, n=20):
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
digits, conv = cf_digits_convergents(ALO, AHI)
above = [(i, p, q) for i, (p, q) in enumerate(conv) if i % 2 == 1]
check("T17b: m*(10^11) is the odd-index convergent q_13", (301994, 190537) == conv[13])
check("T17b: m*(10^12) is the odd-index convergent q_15", (17087915, 10781274) == conv[15])
print(f"Test 17: both minimisers are odd-index (above-alpha) convergents of "
      f"alpha: p13/q13 = 301994/190537 and p15/q15 = 17087915/10781274; "
      f"the next odd-index denominator is q17 = {conv[17][1]}.")

# ============================================================ Test 18
# Item 4: does the L-9910 convergent strengthening beat the direct bound?
# Legendre applies to p/q as soon as x_min > (2/(3 ln2)) q^2; since x_min > F it
# suffices that q^2 <= (3 ln2/2) F, and (safely, via ln 2 > 693/1000) that
# q^2 <= (2079/2000) F.
print("Test 18: Legendre-applicable window vs the direct bound:")
direct = {10**9: 47468, 10**11: 190537, 10**12: 10781274}
for F, lab in ((10**9, "10^9"), (10**11, "10^11"), (10**12, "10^12")):
    lim = Fr(2079, 2000)*F
    q = isqrt(int(lim))
    while (q+1)**2 <= lim: q += 1
    while q**2 > lim:      q -= 1
    verdict = ("VACUOUS (window entirely below the direct bound): no gain"
               if q < direct[F] else "window overlaps the direct bound: refinement possible")
    print(f"   F = {lab:6s}: q <= {q:8d}  (certificate {q}^2 = {q**2} <= "
          f"{int(lim)} = (2079/2000)F);  direct bound q >= {direct[F]:8d}  ->  {verdict}")
    check(f"T18 window {lab}", q**2 <= lim < (q+1)**2)
check("T18: vacuous at 10^12", 1019558 < 10781274)
# the 10^11 overlap case: which convergent denominators lie in [190537, 322412]?
inwin = [q for _, q in conv if 190537 <= q <= 322412]
check("T18: only 190537 in the 10^11 window", inwin == [190537])
print(f"   at F = 10^11 the overlap [190537, 322412] contains exactly one "
      f"convergent denominator, {inwin}, so there the dichotomy refines to "
      f"'q = 190537 or q > 322412' -- but the minimum, hence the bound, is "
      f"unchanged.")
# bootstrap check at 10^12
q12 = 10781274
need = Fr(2, 3)*q12**2/Fr(693, 1000)      # >= (2/(3 ln2)) q^2  (ln2 > .693)
print(f"   bootstrap at F = 10^12: re-applying Legendre with q >= {q12} would "
       f"need x_min >= {float(need):.3e}, far above 10^12; and the only "
       f"cycle-side lower bound available, x_min >= 1/(2 f(m)) with "
       f"f(m) <= eps0*m = {float(eps0(10**12)*q12):.3e}, gives only "
       f"x_min >= {float(1/(2*eps0(10**12)*q12)):.3e}.  No bootstrap.")

# ============================================================ Test 19
# Displayed certificates (winner and closest failure at both new floors), each a
# single comparison of two exact integers, given the Test 15 decimal enclosure.
print("Test 19: displayed certificates (r := K/m - eps0; admissible iff alpha >= r):")
for F, m, K, kind in ((10**11, 190537, 301994, "winner"),
                      (10**11, 79335, 125743, "closest failure"),
                      (10**12, 10781274, 17087915, "winner"),
                      (10**12, 190537, 301994, "closest failure")):
    e0 = eps0(F); P, Q = e0.numerator, e0.denominator
    num, den = K*Q - P*m, m*Q
    g = gcd(num, den); num //= g; den //= g
    lab = f"F=10^{len(str(F))-1} {kind} m={m}, K={K}"
    if kind == "winner":
        ok = N*den >= num*D
        print(f"   {lab}: r = {num}/{den};  N*den = {N*den} >= {num*D} = r_num*10^20 : {ok}")
    else:
        ok = (N+1)*den <= num*D
        print(f"   {lab}: r = {num}/{den};  (N+1)*den = {(N+1)*den} <= {num*D} = r_num*10^20 : {ok}")
    check(f"T19 {lab}", ok)

# ============================================================ Test 20
# Plateau structure.  Adm_F(m) <=> F <= F_max(m) := 1000 m / (2079 f(m)), so
# m*(.) is a step function whose jumps are the numbers F_max(m).  Test 16 showed
# f(m)/m > eps0(10^12) for every m < 10781274, i.e. F_max(m) < 10^12 there, the
# maximum being attained at the closest failure m = 190537.
def Fmax(m):
    K = -((-(m*AHI).numerator)//(m*AHI).denominator)
    assert K == -((-(m*ALO).numerator)//(m*ALO).denominator)
    return Fr(1000*m, 2079)/(K - m*ALO), Fr(1000*m, 2079)/(K - m*AHI)
print("Test 20: plateau endpoints F_max(m) = 1000 m / (2079 f(m)):")
for m in (15601, 47468, 79335, 190537, 10781274):
    lo, hi = Fmax(m)
    check(f"T20 F_max({m}) determined to 10 digits",
          int(lo*10**10 // 10**len(str(int(lo)))) == int(hi*10**10 // 10**len(str(int(hi)))))
    print(f"   m = {m:>9}: F_max in [{float(lo):.10e}, {float(hi):.10e}]")
lo_lo, lo_hi = Fmax(190537)
hi_lo, hi_hi = Fmax(10781274)
check("T20: 10^12 lies in the 10781274-plateau", lo_hi < 10**12 < hi_lo)
print(f"   => m*(F) = 10781274 for every F in (F_max(190537), F_max(10781274)] "
      f"~ (9.8478e11, 2.9446e14]; the floor 10^12 clears the lower end by "
      f"{float(10**12/lo_hi - 1)*100:.2f}% and further verification changes "
      f"nothing until F > 2.9446e14.")

# ============================================================ Test 21
# Exhaustive certification of the plateau table: the successive record-holders of
# m/f(m) -- equivalently of F_max(m) -- below m*(10^12) ARE the jump points of the
# step function F |-> m*(F).  Every m <= 10781274 is examined; each record /
# non-record verdict is certified by the enclosure (the loop asserts otherwise).
# The comparison m/f(m) > m'/f(m') is a PURE INTEGER test: with f(m) = K_m - m*alpha,
# m*f(m') - m'*f(m) = m*K_{m'} - m'*K_m  (the alpha terms cancel exactly).
t0 = time.time(); recs = []; bm = bK = None
for m in range(1, 10781275):
    lo, hi = m*A_LO, m*A_HI
    K = hi//SC + 1
    assert lo//SC + 1 == K, ("ceiling undetermined", m)
    if bm is None or m*bK > bm*K:              # exact: m/f(m) > bm/f(bm)
        recs.append((m, K)); bm, bK = m, K
check("T21: jump points below 10^12 are the expected five",
      [m for m, _ in recs[-5:]] == [15601, 47468, 79335, 190537, 10781274])
print(f"Test 21: exhaustive over m = 1..10781274: {len(recs)} jump points of "
      f"m*(.); the last five (with F_max = 1000 m / (2079 f(m))) are  "
      f"[{time.time()-t0:.1f}s]")
for m, K in recs[-5:]:
    a = Fr(1000*m, 2079)/(Fr(K) - m*AHI); b = Fr(1000*m, 2079)/(Fr(K) - m*ALO)
    print(f"   m = {m:>9}, K = {K:>9}: F_max in [{float(a):.10e}, {float(b):.10e}]")
print("   => m*(F) = 47468 on (2.8588e8, 1.4480e9], 79335 on (1.4480e9, 7.2176e9],"
      " 190537 on (7.2176e9, 9.8478e11], 10781274 on (9.8478e11, 2.9446e14].")

# ============================================================ Test 22
# Verification tier (a): the doubly-computed floor F = 10^10 (the part of X-9903
# that fable-02-v19 re-swept contiguously with an independent implementation).
m10, K10, (mf10, Kf10, marg10) = scan(10**10, 200000)
check("T22: m*(10^10) = 190537", (m10, K10, mf10) == (190537, 301994, 79335))
check("T22: gcd = 1", gcd(K10, m10) == 1)
print(f"Test 22: F = 10^10: exhaustive over m = 1..{m10}: m* = {m10}, K* = {K10}, "
      f"K*+m* = {K10+m10}; closest failure m = {mf10} (K = {Kf10}), margin "
      f"f(m)/m - eps0 >= {float(marg10):.4e}")
for m, K, kind in ((m10, K10, "winner"), (mf10, Kf10, "closest failure")):
    e0 = eps0(10**10); P, Q = e0.numerator, e0.denominator
    num, den = K*Q - P*m, m*Q
    g = gcd(num, den); num //= g; den //= g
    if kind == "winner":
        ok = N*den >= num*D
        print(f"   winner m={m}, K={K}: r = {num}/{den};  N*den = {N*den} >= "
              f"{num*D} = r_num*10^20 : {ok}")
    else:
        ok = (N+1)*den <= num*D
        print(f"   closest failure m={m}, K={K}: r = {num}/{den};  (N+1)*den = "
              f"{(N+1)*den} <= {num*D} = r_num*10^20 : {ok}")
    check(f"T22 cert {kind}", ok)
print(f"   tier (a) [floor double-implemented, reviewed]: m >= {m10}, K >= {K10}, "
      f"C-length >= {K10+m10};  tier (b) [floor single-implementation, "
      f"mathematics reviewed]: m >= 10781274.  Both floors lie inside the same "
      f"certified plateau boundary structure of Test 21.")

print("RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-25, CPython 3.11, Linux; 10 s):**

```text
Test 15: certified decimal enclosure (Lemma A, n = 80 terms):
         158496250072115618145/10^20 < alpha < 158496250072115618146/10^20   (width 10^-20)
         Lemma B(iii) enclosure width U0-L0 = 4.720e-11 is too coarse for these floors (smallest margin below is 7.4e-15), so the decimal enclosure is used; both are certified, and L0 < 158496250072115618145/10^20 < 158496250072115618146/10^20 < U0 holds: True
Test 16: F = 10^11: exhaustive over m = 1..190537: m* = 190537, K* = 301994, K*+m* = 492531; closest failure m = 79335 (K = 125743), margin f(m)/m - eps0 >= 6.1832e-11   [0.2s]
Test 16: F = 10^12: exhaustive over m = 1..10781274: m* = 10781274, K* = 17087915, K*+m* = 27869189; closest failure m = 190537 (K = 301994), margin f(m)/m - eps0 >= 7.4330e-15   [7.7s]
Test 17: additive scan (scale 2^100, 55-term series) reproduces m*(10^11) = 190537 and m*(10^12) = 10781274   [5.1s]
Test 17: both minimisers are odd-index (above-alpha) convergents of alpha: p13/q13 = 301994/190537 and p15/q15 = 17087915/10781274; the next odd-index denominator is q17 = 171928773.
Test 18: Legendre-applicable window vs the direct bound:
   F = 10^9  : q <=    32241  (certificate 32241^2 = 1039482081 <= 1039500000 = (2079/2000)F);  direct bound q >=    47468  ->  VACUOUS (window entirely below the direct bound): no gain
   F = 10^11 : q <=   322412  (certificate 322412^2 = 103949497744 <= 103950000000 = (2079/2000)F);  direct bound q >=   190537  ->  window overlaps the direct bound: refinement possible
   F = 10^12 : q <=  1019558  (certificate 1019558^2 = 1039498515364 <= 1039500000000 = (2079/2000)F);  direct bound q >= 10781274  ->  VACUOUS (window entirely below the direct bound): no gain
   at F = 10^11 the overlap [190537, 322412] contains exactly one convergent denominator, [190537], so there the dichotomy refines to 'q = 190537 or q > 322412' -- but the minimum, hence the bound, is unchanged.
   bootstrap at F = 10^12: re-applying Legendre with q >= 10781274 would need x_min >= 1.118e+14, far above 10^12; and the only cycle-side lower bound available, x_min >= 1/(2 f(m)) with f(m) <= eps0*m = 5.186e-06, gives only x_min >= 9.642e+04.  No bootstrap.
Test 19: displayed certificates (r := K/m - eps0; admissible iff alpha >= r):
   F=10^11 winner m=190537, K=301994: r = 62784552599809463/39612642300000000;  N*den = 6278455259998065185821274533500000000 >= 6278455259980946300000000000000000000 = r_num*10^20 : True
   F=10^11 closest failure m=79335, K=125743: r = 580932659998237/366527700000000;  (N+1)*den = 58093265997557371653131644200000000 <= 58093265999823700000000000000000000 = r_num*10^20 : True
   F=10^12 winner m=10781274, K=17087915: r = 845851792499743303/533673063000000000;  N*den = 84585179249999912825580528135000000000 >= 84585179249974330300000000000000000000 = r_num*10^20 : True
   F=10^12 closest failure m=190537, K=301994: r = 627845525999809463/396126423000000000;  (N+1)*den = 62784552599980651858608871758000000000 <= 62784552599980946300000000000000000000 = r_num*10^20 : True
Test 20: plateau endpoints F_max(m) = 1000 m / (2079 f(m)):
   m =     15601: F_max in [2.8587828883e+08, 2.8587828883e+08]
   m =     47468: F_max in [1.4479896944e+09, 1.4479896944e+09]
   m =     79335: F_max in [7.2176350614e+09, 7.2176350614e+09]
   m =    190537: F_max in [9.8478191629e+11, 9.8478191629e+11]
   m =  10781274: F_max in [2.9446434989e+14, 2.9446434989e+14]
   => m*(F) = 10781274 for every F in (F_max(190537), F_max(10781274)] ~ (9.8478e11, 2.9446e14]; the floor 10^12 clears the lower end by 1.55% and further verification changes nothing until F > 2.9446e14.
Test 21: exhaustive over m = 1..10781274: 38 jump points of m*(.); the last five (with F_max = 1000 m / (2079 f(m))) are  [5.1s]
   m =     15601, K =     24727: F_max in [2.8587828883e+08, 2.8587828883e+08]
   m =     47468, K =     75235: F_max in [1.4479896944e+09, 1.4479896944e+09]
   m =     79335, K =    125743: F_max in [7.2176350614e+09, 7.2176350614e+09]
   m =    190537, K =    301994: F_max in [9.8478191629e+11, 9.8478191629e+11]
   m =  10781274, K =  17087915: F_max in [2.9446434989e+14, 2.9446434989e+14]
   => m*(F) = 47468 on (2.8588e8, 1.4480e9], 79335 on (1.4480e9, 7.2176e9], 190537 on (7.2176e9, 9.8478e11], 10781274 on (9.8478e11, 2.9446e14].
Test 22: F = 10^10: exhaustive over m = 1..190537: m* = 190537, K* = 301994, K*+m* = 492531; closest failure m = 79335 (K = 125743), margin f(m)/m - eps0 >= 1.8542e-11
   winner m=190537, K=301994: r = 6278455259809463/3961264230000000;  N*den = 627845525999806518582127453350000000 >= 627845525980946300000000000000000000 = r_num*10^20 : True
   closest failure m=79335, K=125743: r = 58093265998237/36652770000000;  (N+1)*den = 5809326599755737165313164420000000 <= 5809326599823700000000000000000000 = r_num*10^20 : True
   tier (a) [floor double-implemented, reviewed]: m >= 190537, K >= 301994, C-length >= 492531;  tier (b) [floor single-implementation, mathematics reviewed]: m >= 10781274.  Both floors lie inside the same certified plateau boundary structure of Test 21.
RESULT: ALL CHECKS PASSED
```


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
   **Update (fable-02-v18, 2026-07-25):** the "single-implementation" caveat is now
   partly discharged — the reviewer re-ran the full $n \le 10^{9}$ descent sweep in
   an independent C implementation (128-bit intermediates, explicit peak-value
   overflow audit) and reproduced all four decades bit-for-bit, including the
   max-drop statistics. See the Verification note, §4.
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
7. **(Addendum.) The $m \ge 10\,781\,274$ headline rests on a reviewed but
   singly-computed floor.** L-9913.12/.13 consume X-9903's
   $\mathrm{(V}_{10^{12}})$, which has passed independent review (fable-02-v19)
   — its overflow-*refusing* kernel matters here: the maximum excursion is
   $4.0\cdot10^{23}$ at $n = 871\,673\,828\,443$, i.e. $21\,714\times$ above
   $2^{64}$, so a wrapping $64$-bit kernel would have been silently wrong. **But
   only $n \le 10^{10}$ was swept twice**; $(10^{10}, 10^{12}]$ has one
   implementation plus $22$M spot-checks. Hence the tier split: $m \ge 190\,537$
   is the strongest bound resting on a double-implemented floor, $m \ge
   10\,781\,274$ the strongest resting on a reviewed one. This file re-verified
   none of X-9903 itself; the arithmetic on *this* side is exhaustive and
   certified (Tests 15–22). Full ladder of standing: $m \ge 2966$ (floor X-9901,
   reviewed; this file PROVED) $\;\to\; m \ge 47468$ (floor = this file's X-9913,
   unreviewed) $\;\to\; m \ge 190\,537$ (floor double-implemented + reviewed)
   $\;\to\; m \ge 10\,781\,274$ (floor reviewed, single-implementation).
8. **(Addendum.) $m^*(10^{12})$ sits on a knife edge that $m^*(10^6)$ did not.**
   The closest failure, $m = 190537$, misses admissibility by only
   $7.433\cdot 10^{-15}$ in $\alpha$-units, i.e. by a relative $1.55\%$ of
   $\varepsilon_0$. Had the floor been $\approx 1.6\%$ lower — anywhere below
   $F \approx 9.85\cdot 10^{11}$ — $m^*$ would collapse from $10\,781\,274$ back to
   $190537$, a factor $57$. The value is exact and certified, but it is *not*
   robust to small changes in $F$, and no reader should treat the step from
   $47468$ to $10\,781\,274$ as a smooth trend (item (iv) of the Gap-audit
   addendum shows the $\varepsilon_0$-vs-$\varepsilon$ slack is safely inside the
   margin, so that particular worry is discharged).

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
6. **(Addendum.) Where the next jump lives.** At $F = 10^{12}$ the bound is attained
   *at* an odd-index convergent ($m^* = q_{15} = 10\,781\,274$), so — unlike at
   $F = 10^6$, where the minimiser was a semiconvergent — the convergent structure
   can no longer sharpen it (L-9913.13). The next odd-index convergent denominator
   is $q_{17} = 171\,928\,773$, a factor $15.9$ higher. Two routes to it:
   **(a)** a larger verified floor — mechanical, but the value must be *computed*,
   not extrapolated (the plateaux are long and irregular — see the plateau table
   in L-9913.12; in particular **nothing changes until $F > 2.9446\cdot10^{14}$**,
   so the immediate next verification milestone worth funding is $F \approx
   3\cdot 10^{14}$, not $10^{13}$); **(b)** an independent obstruction killing the
   single pair $(m,K) = (10\,781\,274,\ 17\,087\,915)$ and the semiconvergent
   admissible values just above it — a divisibility/composition argument at
   $m \approx 10^{7}$, far beyond L-9915's enumeration range, so probably only
   reachable by a structural (2-adic or exponent-statistics) route.
7. **(Addendum, updated.) Harden $(10^{10}, 10^{12}]$ — for standing, not for
   numbers.** X-9903 is now reviewed (fable-02-v19) and doubly computed up to
   $10^{10}$. A second independent sweep of the remaining decade-and-a-half would
   promote tier (b) to double-implemented; by the plateau it cannot change
   $10\,781\,274$. Whoever runs it should use a third kernel design (different
   sieve modulus, different overflow strategy) and compare digests, not code.

---
*File authored by fable-02-p8, 2026-07-25. Status PROPOSED per NOTATION.md
conventions; an independent reviewing agent may upgrade after verification.*

---

## Verification note (fable-02-v18, 2026-07-25)

Independent adversarial review per README §13, carried out without relying on the
author's confidence and without reusing a single line of the author's test code.
**Verdict: PASS.** The Main Theorem $m \ge 2966$ is correct, its exhaustiveness
step is genuinely complete (not heuristic), the reduced-denominator trap is
handled correctly, and $m^*(10^6) = 2966$ reproduces exactly under an independent
implementation using a different certification of $\alpha$, a different method for
$\lceil m\alpha\rceil$, and a search range 33x wider than the author's. Status
upgraded PROPOSED $\to$ PROVED. Two documentation-only fixes applied (§6). Per
protocol this review does **not** set `INDEPENDENTLY_VERIFIED`.

### 1. Logical skeleton, reconstructed from the dependencies alone

Before reading the author's proofs I rebuilt the argument from L-9905's Statement
section and NOTATION.md, and then checked the file against it. The skeleton is:

1. **Floor.** Every element of a nontrivial $S$-cycle is a $C$-counterexample, so
   under $\mathrm{(V}_F)$ every element, in particular $x_{\min}$, exceeds $F$.
   Re-derived independently: $S^j(x) = C^{t_j}(x)$ with $t_j \ge 2j$ (one $C$-step
   $x \mapsto 3x+1$ plus $a$ halvings per $S$-step); $S(1) = 1$ and distinctness of
   cycle elements force $x_i \ne 1$; $C^{s}$ is trapped in $\{1,2,4\}$ once it hits
   $1$, and cycle elements are odd, so a cycle element reaching $1$ would force
   some $S^j(x_i) = 1$. Contradiction. **Sound**; matches L-9913.1 exactly.
2. **Squeeze.** L-9905.3 (PROVED, verified verbatim in the source file at line 48)
   gives $0 < K\ln 2 - m\ln 3 \le m/(3x_{\min})$. Divide by $\ln 2$, use
   $x_{\min} > F$: $0 < K - m\alpha < m/(3F\ln 2) = \varepsilon(F) m$. **Sound.**
3. **Ceiling.** $m\alpha \notin \mathbb{Z}$ (else $3^m = 2^{k}$, odd $=$ even), so
   $K > m\alpha$ integer forces $K \ge \lceil m\alpha\rceil$ and
   $f(m) := \lceil m\alpha\rceil - m\alpha \le K - m\alpha$. **Sound.**
4. **Condition.** $f(m) = 1 - \{m\alpha\} \le \varepsilon_0(F)\, m$, i.e.
   $\mathrm{Adm}_F(m)$.
5. **Minimum.** $m^*(F) := \min\{m \ge 1 : \mathrm{Adm}_F(m)\}$; every nontrivial
   cycle has $m \ge m^*(F)$, and also $q := m/\gcd(K,m) \ge m^*(F)$.

Every step of the file's L-9913.1–.6 matched this reconstruction. **First
unsupported inference: none found.**

Boundary/quantifier checks I ran explicitly:

* $\mathrm{Adm}$ is stated with $\le$ while the cycle satisfies the *strict*
  inequality. This is the safe direction (a larger admissible set can only lower
  $m^*$). I also recomputed $m^*$ with the strict predicate: still $2966$
  (Part 11 of my script), so nothing is lost either.
* $\varepsilon_0 > \varepsilon$ is the safe direction and is **proved**, not
  assumed: Corollary A1's arithmetic was re-derived by hand —
  $76545 = 5\cdot7\cdot3^7$, $\tfrac{25515+945+63+5}{76545} = \tfrac{26528}{76545}$,
  $2\cdot 26528 = 53056$, and $53056\cdot 1000 = 53\,056\,000 > 53\,045\,685 =
  693\cdot 76545$ — and Lemma A's remainder bound is a *finite* geometric identity
  plus $0 < R_n \le x^{2n+1}/((2n+1)(1-x^2))$, so no convergence question arises.
  No calculator appeal anywhere. I independently confirmed $53056/76545 < \ln 2$
  against a 160-digit certified series enclosure.
* $x_{\min} \ge F+1$ is available but the file conservatively uses $\varepsilon(F)$
  rather than $\varepsilon(F+1)$. I checked that the sharper constant changes
  nothing: $m^* = 2966$ for $\varepsilon(10^6+1)$ as well.
* The $m = 1$ boundary: $\mathrm{Adm}_F(1)$ is false for every $F \ge 2$ (I checked
  $F \in \{2,3,10,10^6\}$), so the trivial cycle is excluded by the *hypothesis*
  $x_{\min} > F$, never by the squeeze. Correctly stated.
* $K \ge 4701$: $K > m\alpha \ge 2966\alpha \notin \mathbb{Z}$ gives
  $K \ge \lceil 2966\alpha\rceil = 4701$; $C$-length $K + m \ge 7667$ is the sum of
  two independently valid minima. Sound.

### 2. The reduced-denominator question (checked first and hardest)

The coordinator's concern was that the constraint $p - q\alpha < \varepsilon_0 q$
depends only on the **reduced** denominator $q = m/\gcd(K,m)$, so a search over
$m$ treated as an approximation denominator would be illegitimate. **The file does
not make that error, and in fact does not need to.** Both halves check out:

* **Direct route (L-9913.3(2)).** $f(m) \le K - m\alpha < \varepsilon_0 m$ holds
  for the cycle's own $m$ **regardless of $\gcd(K,m)$** — no approximation theory
  is invoked, so $m \ge m^*(F)$ follows immediately. This route alone carries the
  Main Theorem.
* **Reduced route (L-9913.3(3)).** Dividing the squeeze by $m$ cancels
  $d = \gcd(K,m)$, giving $0 < p/q - \alpha < \varepsilon_0$ and hence
  $\mathrm{Adm}_F(q)$, so $q \ge m^*(F)$ — strictly more information, since it also
  says $m$ is a *multiple* of an admissible $q \ge 2966$.
* **Upward closure** $\mathrm{Adm}_F(q) \Rightarrow \mathrm{Adm}_F(tq)$: the proof
  ($\lceil tq\alpha\rceil \le t\lceil q\alpha\rceil$, so $f(tq) \le t f(q)$) is
  correct. I verified it computationally for **all** pairs with $tq \le 10^5$: zero
  violations.
* **Is the number still the sharpest available?** Yes. $m^*(F)$ is by definition
  the minimum of one predicate over one index set, so "least admissible $m$" and
  "least admissible reduced denominator" are the *same number* — there is no
  sharper bound hiding in the reduced-denominator formulation. I confirmed the
  minimiser is itself reduced ($\gcd(4701,2966)=1$) and that the admissible set
  below $3000$ is exactly $\{2966\}$; the full admissible set below $10^5$ begins
  $2966, 3631, 4296, 4961, 5267, 5626, \dots$ (2404 values). The file's boxed note
  attributed the equality of the two minima to upward closure, which is a
  non-sequitur; I rewrote that clause (§6, fix 1). The mathematics was already
  correct.

### 3. Exhaustiveness: provably complete, and the semiconvergent trap

**The Main Theorem's completeness rests on brute force, not on the record lemma.**
L-9913.5 decides $\mathrm{Adm}_{10^6}(m)$ for **every** $m \in \{1,\dots,2965\}$
individually and exactly. That is a complete argument by construction, and I
re-ran it over $m \le 10^{5}$ (33x the author's range) with an independently built
decision procedure. No admissible $m$ below $2966$ exists.

This matters because a *structural* shortcut would have been wrong here, and I
verified the trap concretely:

* $2966 = q_7 + 4q_8 = 306 + 4\cdot 665$ with numerator $4701 = p_7 + 4p_8 =
  485 + 4\cdot 1054$ — a **semiconvergent** (intermediate fraction), **not** a
  convergent of $\alpha$. A convergent-only search would have returned
  $q \ge 15601$: a bound that is *not proved*, because $\mathrm{Adm}(2966)$ is
  genuinely true and no contradiction is derivable at $m = 2966$ from this method.
  The file gets this right and quarantines the convergent statement into the
  conditional dichotomy L-9913.8.
* I reconstructed the one-sided best-approximation lemma (L-9913.11) from scratch,
  checked its unimodularity bookkeeping and its five-row sign-pattern table (all
  nine sign combinations of $(s,t)$ are covered: $(\ge1,\ge1)$ by $m \ge u+v$,
  $(\le-1,\cdot)$ and $(0,\le 0)$ by $m \le 0$, the rest by rows 1–3), and found it
  **correct**. I then computed the record sequence two ways — by brute-force
  running minima of $f$ over $m \le 10^5$, and by the Stern–Brocot recursion — and
  the two lists agree exactly. I additionally confirmed that the records are
  precisely the from-above intermediate-fraction denominators
  $q_{2i-1} + j\,q_{2i}$ ($0 \le j \le a_{2i+1}$):
  $1,3,5\,|\,17,29,41\,|\,94,147,200,253,306\,|\,971,1636,2301,2966,\dots,15601$.
  So the block-skipping reduction is sound *and* structurally complete, and it
  independently reproduces $m^* = 2966$.
* Legendre's route (L-9913.8(b)) gives only $q \ge 1020$: $1/(2q^2) < 1/2079000
  \Rightarrow q^2 > 1\,039\,500$, and $1019^2 = 1\,038\,361 < 1\,039\,500 \le
  1\,040\,400 = 1020^2$. Correctly reported as **weaker**. The odd-index
  convergent denominators $\le 10^5$ recomputed independently:
  $1, 5, 41, 306, 15601, 79335$ — so branch (a)'s jump to $q \ge 15601$ and
  $K \ge \lceil 15601\alpha\rceil = 24727$ is correct.
* **On the L-9910 strengthening.** The reviewer-flagged hypothesis
  $x_{\min} > \tfrac{2}{3\ln 2}q^2$ (equivalently L-9910.2's $x_{\min} \ge m^2$)
  would force $K/m$ to be a convergent. It is **not** available at $F = 10^6$: it
  requires $q < \sqrt{3F\ln 2/2} \approx 1019.6$, i.e. exactly the regime Legendre
  already covers, and every $q$ in that regime is non-admissible anyway. So the
  strengthening cannot improve $2966$ at the current floor, and the file is right
  not to invoke it. It becomes useful only once $F$ exceeds $\approx \tfrac{2}{3\ln 2}
  (m^*)^2$, i.e. around $F \approx 8.5\cdot 10^{6}$ for $q = 2966$ — worth
  revisiting if a floor beyond $10^{7}$ is ever independently certified.

### 4. Independent computation

Written from the Statement sections alone. Three deliberate independences from the
author's code: (i) $\alpha$ is certified by a **different** decomposition —
$\ln 2 = 2\,\mathrm{artanh}(1/3)$ and $\ln 3 = 2\,\mathrm{artanh}(1/2)$, versus the
file's $\ln 3 = \ln 2 + 2\,\mathrm{artanh}(1/5)$; (ii) $\lceil m\alpha\rceil$ is
computed by **bit length of $3^m$** (exact, no enclosure: $2^{b-1} < 3^m < 2^b$
since $3^m$ is odd and $\ge 3$), then cross-checked against the enclosure; (iii)
the sweep runs to $m \le 10^{5}$ rather than $3000$.

```python
#!/usr/bin/env python3
"""INDEPENDENT adversarial verification of L-9913 (fable-02-v18, 2026-07-25).
FINITE VERIFICATION ONLY -- not a proof.  Exact: int / fractions.Fraction only;
no float appears in any decision.  Run: python3 v18_verify.py  (~3.5 s)"""
from fractions import Fraction as Fr
from math import gcd
import random, time

fails = []
def chk(label, ok):
    if not ok: fails.append(label); print("FAIL:", label)
t0 = time.time()

# --- PART 1: certified enclosure of alpha, by a decomposition different from
# the file's:  ln2 = 2 artanh(1/3),  ln3 = 2 artanh(1/2).
# Remainder (Lemma A, re-derived): T_n(x) < artanh(x) <= T_n(x)+x^(2n+1)/((2n+1)(1-x^2))
def artanh_bounds(x, n):
    s = sum(x**(2*k+1) / Fr(2*k+1) for k in range(n))
    return s, s + x**(2*n+1) / ((2*n+1) * (1 - x*x))
N_TERMS = 260
ln2_lo, ln2_hi = [2*t for t in artanh_bounds(Fr(1, 3), N_TERMS)]
ln3_lo, ln3_hi = [2*t for t in artanh_bounds(Fr(1, 2), N_TERMS)]
ALO, AHI = ln3_lo / ln2_hi, ln3_hi / ln2_lo
chk("enclosure ordered", ALO < AHI)
for D in (1000, 10000, 100000):          # bit-length bracket cross-check
    b = (3**D).bit_length()
    chk(f"bitlen bracket D={D}", Fr(b-1, D) < ALO and AHI < Fr(b, D))
L0, U0 = Fr(176251, 111202), Fr(301994, 190537)
chk("file cert C1: 3^111202 > 2^176251", 3**111202 > 2**176251)
chk("file cert C2: 3^190537 < 2^301994", 3**190537 < 2**301994)
chk("file certs bracket alpha", L0 < ALO and AHI < U0)
chk("file cert width", U0 - L0 == Fr(1, 21188095474))

# --- PART 2: ln 2 > 693/1000 (Corollary A1) re-derived
S4 = 2*sum(Fr(1, (2*k+1)*3**(2*k+1)) for k in range(4))
chk("A1 partial sum", S4 == Fr(53056, 76545))
chk("A1 > 693/1000", S4 > Fr(693, 1000))
chk("A1 consistent with series", S4 < ln2_lo)
chk("eps0 > eps", Fr(1000, 2079) > Fr(1, 3)/ln2_lo)

# --- PART 3: exact ceil(m alpha) = bit_length(3^m); Adm decision
def eps0(F): return Fr(1000, 3*693*F)
def decide(K, m, e0):
    r = Fr(K, m) - e0                    # Adm(m)  <=>  alpha >= r
    if ALO > r: return True
    if AHI < r: return False
    raise AssertionError(f"enclosure too coarse at m={m}")
MMAX = 100000
p = 1; Kbit = [0]*(MMAX+1)
for m in range(1, MMAX+1):
    p *= 3; Kbit[m] = p.bit_length()
badc = 0
for m in range(1, MMAX+1):
    lo, hi = m*ALO, m*AHI
    cl = -((-lo.numerator)//lo.denominator); ch = -((-hi.numerator)//hi.denominator)
    if not (cl == ch == Kbit[m]): badc += 1
chk("ceil agreement bitlen vs enclosure", badc == 0)

# --- PART 4: m*(F) by EXHAUSTIVE brute force over ALL m (no CF theory used)
def mstar(F, cap):
    e0 = eps0(F)
    for m in range(1, cap+1):
        if decide(Kbit[m], m, e0): return m, Kbit[m]
res = {}
for F, lab in ((10**6, "10^6"), (10**7, "10^7"), (10**8, "10^8"), (10**9, "10^9")):
    m, K = mstar(F, MMAX); res[lab] = (m, K)
    print(f"[4] F = {lab:5s}: m* = {m:6d}, K* = {K:6d}, K*+m* = {K+m:6d}, gcd = {gcd(K,m)}")
chk("m*(10^6)", res["10^6"] == (2966, 4701)); chk("m*(10^7)", res["10^7"] == (10946, 17349))
chk("m*(10^8)", res["10^8"] == (15601, 24727)); chk("m*(10^9)", res["10^9"] == (47468, 75235))
chk("gcd(4701,2966)=1", gcd(4701, 2966) == 1)
e6 = eps0(10**6)
adm6 = [m for m in range(1, MMAX+1) if decide(Kbit[m], m, e6)]
viol = [(q, t) for q in adm6 if q <= MMAX//2
        for t in range(2, MMAX//q + 1) if (t*q) not in set(adm6)]
chk("upward closure Adm(q)=>Adm(tq)", not viol)
print(f"[4] admissible m <= {MMAX} at F=10^6 (first 6): {adm6[:6]}; total {len(adm6)}")

# --- PART 5: the file's displayed certificates, recomputed
r1 = Fr(4701, 2966) - e6
chk("winner r1", r1 == Fr(4886688017, 3083157000))
chk("winner numbers", (176251*r1.denominator, r1.numerator*111202)
    == (543409504407000, 543409480866434))
chk("winner cert", 176251*r1.denominator >= r1.numerator*111202)
r2 = Fr(3647, 2301) - e6
chk("runner-up K", Kbit[2301] == 3647)
chk("runner-up r2", r2 == Fr(2527370233, 1594593000))
chk("runner-up numbers", (301994*r2.denominator, r2.numerator*190537)
    == (481557518442000, 481557542085121))
chk("runner-up cert", 301994*r2.denominator <= r2.numerator*190537)

# --- PART 6: sensitivity; does the TRUE eps (and eps at x_min >= F+1) still give 2966?
need = Fr(4701, 2966) - AHI
allow = min(Fr(Kbit[m], m) - ALO for m in range(1, 2966))
chk("eps0 inside stability interval", need <= e6 < allow)
chk("true eps inside", need <= Fr(1,3*10**6)/ln2_hi and Fr(1,3*10**6)/ln2_lo < allow)
chk("eps(F+1) inside", need <= Fr(1, 3*(10**6+1))/ln2_lo < allow)
print(f"[6] m*=2966 for eps in [{float(need):.7e}, {float(allow):.7e}); "
      f"eps0={float(e6):.7e}, true eps~{float(Fr(1,3*10**6)/ln2_hi):.7e}")

# --- PART 7: pure-integer form 2^(QK-Pm) <= 3^(Qm) vs enclosure form
random.seed(918273); bad = 0
for _ in range(600):
    Q = random.choice([1,2,3,4,7,11,100,997,5000]); P = random.randint(1,4*Q)
    m = random.randint(1,14); K = random.randint(1,28); ex = Q*K - P*m
    intform = (2**ex <= 3**(Q*m)) if ex >= 0 else (Fr(1,2**(-ex)) <= 3**(Q*m))
    try: ratform = decide(K, m, Fr(P, Q))
    except AssertionError: continue
    if intform != ratform: bad += 1
chk("integer form == enclosure form", bad == 0)
mism = sum(1 for m in range(1, 41)
           if (2**(2079*Kbit[m] - m) <= 3**(2079*m)) != decide(Kbit[m], m, Fr(1,2079)))
chk("full big-int instance Q=2079", mism == 0)

# --- PART 8: second, structural route -- one-sided records (Stern-Brocot)
recs_bf = []; best = None
for m in range(1, MMAX+1):
    lo = Kbit[m] - m*AHI
    if best is None or lo < best: recs_bf.append(m); best = Kbit[m] - m*AHI
def sb_records(limit):
    u, P, v, Q_ = 1, 2, 1, 1; out = []
    while u + v <= limit:
        Alo, Ahi = P - u*AHI, P - u*ALO
        Blo, Bhi = v*ALO - Q_, v*AHI - Q_
        assert Alo > 0 and Blo > 0
        if Alo > Bhi: out.append((u, Alo, Ahi, u+v)); u, P = u+v, P+Q_
        elif Ahi < Blo: v, Q_ = u+v, Q_+P
        else: raise AssertionError("SB undecided")
    return out
sb = sb_records(10**14)
chk("SB records == brute-force records", [u for u,_,_,_ in sb if u <= MMAX] == recs_bf)
def block_skip(F):
    e0 = eps0(F)
    for (u, Alo, Ahi, nu) in sb:
        t = Alo / e0
        if t < nu: return u, nu, t
u_, nu_, t_ = block_skip(10**6); lb = -(-t_.numerator//t_.denominator)
chk("block skip consistent", lb <= 2966 <= nu_)
chk("no survivor below 2966 in window", [m for m in range(lb, nu_) if decide(Kbit[m], m, e6)] == [])
print(f"[8] records <= 3000: {[m for m in recs_bf if m <= 3000]}")
print(f"[8] block-skip F=10^6: all m < {u_} out; in [{u_},{nu_}) need m >= {float(t_):.6g}")

# --- PART 9: F = 2^68 certified bracket
def ceil_ma(m):
    lo, hi = m*ALO, m*AHI
    cl = -((-lo.numerator)//lo.denominator); ch = -((-hi.numerator)//hi.denominator)
    assert cl == ch; return cl
F68 = 2**68; e68 = eps0(F68); LB68, UB68 = 8961554427, 72057431991
chk("2^68 upper endpoint admissible", decide(ceil_ma(UB68), UB68, e68))
u2, nu2, t2 = block_skip(F68)
chk("2^68 lower endpoint", -(-t2.numerator//t2.denominator) == LB68)

# --- PART 10: boundaries, CF data, semiconvergent structure
chk("Adm_F(1) false for all F>=2", all(not decide(Kbit[1], 1, eps0(F)) for F in (2,3,10,10**6)))
chk("ceil(1*alpha)=2", Kbit[1] == 2)
chk("ceil(15601 a) = 24727", Kbit[15601] == 24727)
def cf_digits(lo, hi, n=25):
    a = []; x, y = lo, hi
    for _ in range(n):
        i1, i2 = x.numerator//x.denominator, y.numerator//y.denominator
        if i1 != i2: break
        a.append(i1); x, y = x - i1, y - i2
        if x <= 0: break
        x, y = 1/y, 1/x
    return a
dg = cf_digits(ALO, AHI)
qn, pn = [1, 0], [0, 1]
for a in dg: qn.append(a*qn[-1]+qn[-2]); pn.append(a*pn[-1]+pn[-2])
qs, ps = qn[2:], pn[2:]
chk("CF digits", dg[:15] == [1,1,1,2,2,3,1,5,2,23,2,2,1,1,55])
chk("odd-index conv denominators <=1e5",
    [q for i, q in enumerate(qs) if i % 2 == 1 and q <= 10**5] == [1,5,41,306,15601,79335])
chk("2966 = q7 + 4 q8", qs[7] + 4*qs[8] == 2966)
chk("4701 = p7 + 4 p8", ps[7] + 4*ps[8] == 4701)

# --- PART 11: negation attempts
for F, target in ((10**6,2966), (10**7,10946), (10**8,15601), (10**9,47468)):
    chk(f"no admissible m < {target}",
        [m for m in range(1, target) if decide(Kbit[m], m, eps0(F))] == [])
def decide_strict(K, m, e0):
    r = Fr(K, m) - e0
    if ALO > r: return True
    if AHI < r: return False
    raise AssertionError
chk("strict version same m*",
    next(m for m in range(1, MMAX+1) if decide_strict(Kbit[m], m, e6)) == 2966)

print(f"RESULT: {'ALL CHECKS PASSED' if not fails else str(len(fails))+' FAILURES'}"
      f"  ({time.time()-t0:.1f}s)")
for f in fails: print("  -", f)
```

**Output (verbatim, run 2026-07-25, CPython 3.11.15, Linux):**

```text
[4] F = 10^6 : m* =   2966, K* =   4701, K*+m* =   7667, gcd = 1
[4] F = 10^7 : m* =  10946, K* =  17349, K*+m* =  28295, gcd = 1
[4] F = 10^8 : m* =  15601, K* =  24727, K*+m* =  40328, gcd = 1
[4] F = 10^9 : m* =  47468, K* =  75235, K*+m* = 122703, gcd = 1
[4] admissible m <= 100000 at F=10^6 (first 6): [2966, 3631, 4296, 4961, 5267, 5626]; total 2404
[6] m*=2966 for eps in [4.1229300e-07, 5.5881817e-07); eps0=4.8100048e-07, true eps~4.8089835e-07
[8] records <= 3000: [1, 3, 5, 17, 29, 41, 94, 147, 200, 253, 306, 971, 1636, 2301, 2966]
[8] block-skip F=10^6: all m < 2301 out; in [2301,2966) need m >= 2673.26
RESULT: ALL CHECKS PASSED  (3.5s)
```

**Supplementary run** (script `v18_supp.py`, same session) confirmed three further
claims of the file: the $L_0/U_0$ enclosure **alone** decides both the ceiling and
the $\mathrm{Adm}$ test for every $m \le 3000$ (0 undecided of each), so the Main
Theorem really does rest on just the two big-integer inequalities; the "Cost note"
margin is exact ($\min_{m\le 3000}|\alpha - r| = 6.8707\cdot 10^{-8}$ at $m = 2966$,
a factor $1456$ above $U_0 - L_0$); and the one-sided records coincide exactly with
the from-above intermediate-fraction denominators. It also records a scope caveat
worth stating: at $m \approx 7\cdot10^{10}$ (the $F = 2^{68}$ row) one has
$m(U_0-L_0) \approx 3.4$, so **that row cannot use $L_0/U_0$** and rests instead on
the Lemma-A series enclosure — which is fine (Lemma A is fully proved here), but
the "entire theorem rests on two big-integer inequalities" remark should be read as
scoped to the Main Theorem, which is how it is written.

**X-9913 re-run in an independent implementation.** I re-ran the raised-floor sweep
in C rather than Python, with `unsigned __int128` intermediates and an explicit
audit of the peak value reached (to rule out silent overflow, which is the one
failure mode Python's bignums make impossible and C makes easy):

```c
/* sweep.c -- fable-02-v18.  For every odd n in [3,N]: iterate T until the value
 * drops strictly below n.  128-bit intermediates; peak value reported. */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
int main(int argc, char **argv) {
    unsigned long long N = (argc > 1) ? strtoull(argv[1], NULL, 10) : 1000000ULL;
    unsigned long long maxsteps = 0, argmax = 1, checked = 0;
    u128 peak = 0;
    for (unsigned long long n = 3; n <= N; n += 2) {
        u128 x = ((u128)3 * n + 1) >> 1;          /* first T step from odd n */
        unsigned long long steps = 1;
        while (x >= (u128)n) {
            if (x & 1) x = (3 * x + 1) >> 1; else x >>= 1;
            steps++;
            if (x > peak) peak = x;
        }
        checked++;
        if (steps > maxsteps) { maxsteps = steps; argmax = n; }
    }
    printf("N = %llu: %llu odd n checked; ALL drop strictly below themselves.\n", N, checked);
    printf("max T-steps to first drop: %llu at n = %llu\n", maxsteps, argmax);
    printf("peak intermediate hi:lo = %llu:%llu\n",
           (unsigned long long)(peak >> 64), (unsigned long long)peak);
    return 0;
}
```

```text
N = 1000000:    499999 odd n checked; max T-steps to first drop: 176 at n = 626331
N = 10000000:   4999999 odd n checked; max T-steps to first drop: 246 at n = 8088063
N = 100000000:  49999999 odd n checked; max T-steps to first drop: 376 at n = 63728127
N = 1000000000: 499999999 odd n checked; max T-steps to first drop: 395 at n = 217740015
peak intermediate value at N = 10^9: hi:lo = 0:707118223359971240  (fits in 64 bits)
real 11.1s  (gcc -O2)
```

All four decades reproduce the file's Test 14 output **exactly**, including every
max-drop statistic. The peak intermediate never left 64 bits, so the sweep is
overflow-safe in C and *a fortiori* in the author's exact-integer Python. The
**drop lemma** was re-derived independently and is sound: strong induction on $n$,
with $n=1$ immediate, $n=2$ via $T(2)=1$, even $n \ge 2$ via $T(n)=n/2 < n$, and
odd $n \ge 3$ via the verified $y = T^k(n) < n$ (and $y \ge 1$ since $T$ maps
$\mathbb{Z}^+ \to \mathbb{Z}^+$); note the descending trajectory is allowed to
exceed $N$ en route, which the induction does not care about. Only odd $n$ need
testing, exactly as claimed.

**X-9901 gate.** An independent memoised recomputation of the max *total*
$C$-stopping time over $n \le 10^6$ returns `524 at n = 837799`, matching L-9909's
recorded statistic. Together with the C descent sweep to $10^6$ above, this is a
genuine second implementation of X-9901, not merely a restatement.

### 5. Hypothesis discipline and over-claim check

* The Main Theorem is **unconditional given one in-repo, independently reviewed
  finite verification** (X-9901 in L-9909, PROVED, reviewed by fable-02-v7) — and
  the file says exactly that, in the header, in $\mathrm{(V}_F)$, in the Motivation
  and in Remaining uncertainty. No literature-scale floor is claimed as its own.
* The $F = 2^{68}$ row is labelled **HYPOTHETICAL** and **not verified anywhere in
  this repository** in the table itself, again in the paragraph below it, and again
  in Remaining uncertainty item 3, where it is called PARTIAL. It is a certified
  bracket $8\,961\,554\,427 \le m^*(2^{68}) \le 72\,057\,431\,991$ (both endpoints
  reproduced by me), never a result. Correct.
* The $10^7$–$10^9$ rows are labelled "verified in this file (X-9913, PROPOSED)",
  i.e. in-repo but at the time unreviewed. Accurate; §4 above now supplies an
  independent second implementation.
* The honesty statement about Baker-type bounds is prominent and makes **no** claim
  about literature numbers, methods or priority, and explicitly says $2966$ "is
  certainly not a record". I attempted to find any sentence that could be read as
  claiming a literature-scale result and found none.

### 6. Fixes applied (documentation only; no statement changed)

1. **Boxed note after L-9913.3** — the clause asserting that the two minima agree
   "because $\mathrm{Adm}_F$ is closed upward under multiples" was a non-sequitur:
   $\min\{m : \mathrm{Adm}_F(m)\}$ and $\min\{q : \mathrm{Adm}_F(q)\}$ are the same
   number *by definition* (one predicate, one index set); upward closure is a
   separate fact about the shape of the admissible set and is not needed for either
   bound. Reworded. The bounds themselves were and remain correct.
2. **L-9913.11 Preservation paragraph** — added the missing one-line argument that
   both branches of the recursion are taken infinitely often (otherwise $B$, or
   $A$, would decrease by a fixed positive amount and leave $(0,1)$), so the record
   sequence $u_1 < u_2 < \dots$ is infinite and the block-skipping consequence
   covers every $m$. Used only for the large-$F$ rows; the Main Theorem does not
   use L-9913.11 at all.
3. **Remaining uncertainty item 2** — cross-referenced the independent C re-run of
   the $n \le 10^9$ sweep.

### 7. Attempts to negate or strengthen

* Searched for an admissible $m < 2966$ over $m \le 10^{5}$ with two independent
  certifications of $\alpha$ and two independent methods for $\lceil m\alpha\rceil$:
  none exists.
* Tried to break the bound by tightening $\varepsilon$: replacing $\varepsilon_0$
  by the true $\varepsilon(10^6)$, or by $\varepsilon(10^6+1)$ (using
  $x_{\min} \ge F+1$), or by the strict form of $\mathrm{Adm}$ — all still give
  $m^* = 2966$. The stability interval is $[4.12293\cdot10^{-7},
  5.588182\cdot10^{-7})$, so $\varepsilon_0$ has $\approx 17\%$ slack on both
  sides; the bound would only drop (to $2301$) if $\varepsilon$ were $\approx1.16$x
  larger, which no correct derivation permits.
* Tried to strengthen via the reduced denominator: impossible, for the reason in
  §2 — the two minima coincide by definition.
* Tried to strengthen via L-9910's $x_{\min} \ge m^2$ / $x_{\min} > \frac{2}{3\ln2}q^2$
  route: not available at $F = 10^6$ (§3, last bullet). Still available at higher
  floors — recorded as a live opportunity rather than a defect.
* Circularity: L-9905, L-9909, L-9910 do not cite L-9913; the one fact needed from
  L-9911 is re-proved inline. No cycle. Nothing assumes the Collatz conjecture or
  its negation; the results are implications about hypothetical cycles.

### 8. Residual caveats (not defects)

1. The Main Theorem is exactly as strong as X-9901. That is stated everywhere it
   matters, and X-9901 now has two independent implementations behind it.
2. L-9913.10's $m \ge 47468$ rests on X-9913. It is now corroborated by my
   independent C re-run, but I have left its PROPOSED label for the integrator to
   adjudicate — a reviewer re-running a computation is corroboration, and the
   status of an experiment record is not mine to promote unilaterally.
3. The $F = 2^{68}$ bracket is not tightened here; pinning $m^*(2^{68})$ exactly
   still needs the Ostrowski enumeration the author describes.
4. Scope of my verdict: I verified L-9913.1–.11, Lemmas A and B, the dependency
   audit and the gap audit. I did **not** re-verify L-9906, L-9915 or L-9910's
   internals (they are separately PROVED, and none of them is load-bearing here).

**First unsupported inference: none.** No mathematical defect was found; the two
items in §6 are documentation.

---
*Reviewed by fable-02-v18, 2026-07-25. Status PROPOSED $\to$ PROVED.
`INDEPENDENTLY_VERIFIED` deliberately NOT set, per README §7 and the review
protocol.*
