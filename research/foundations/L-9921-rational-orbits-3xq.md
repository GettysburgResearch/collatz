# L-9921 — Rational $T$-orbits are exactly $3x+q$ orbits: the precise reduction of Q-9904

```text
Claim ID:      L-9921
Title:         Rational T-orbits are exactly shortcut 3x+q orbits: conjugacy on (1/q)Z,
               the trichotomy that the integer pigeonhole DOES support there, the exact
               reduction of Q-9904 to "no divergent 3x+q orbit for any positive odd q",
               and the ported cycle equation
Status:        PROVED
Authoring agent:   fable-02-p15
Reviewing agents:  fable-02-v23 (adversarial review 2026-07-26: PASS)
Created:       2026-07-25
Last updated:  2026-07-26 (adversarial review by fable-02-v23; Status PROPOSED →
               PROVED; no change to any numbered claim or proof — see the
               Verification note at the end of the file)
Dependencies:  NOTATION.md (D-9902 shortcut map T; D-9906 parity vector v_i, a_k;
               D-9907 bounded/unbounded/divergent; D-9908 cycles; D-9909 counterexample;
               conventions on empty sums/products).
               L-9904 (PROVED): fact B7 (Q ∩ Z_2 = Z_(2) and the parity of p/q),
               the 2-adic map T and its well-definedness, L-9904.5(i) (realization),
               L-9904.5(ii) (periodic-point formula), L-9904.5(iii)/(3b) (orbit
               dichotomy), Lemma D, and the statement of Q-9904 itself.
               L-9901 (PROVED): .2(iii) and .4 (orbit trichotomy on Z^+) and .5, used
               only in L-9921.4 for the C-vs-T transfer; its boxed pigeonhole remark is
               discussed and refined in L-9921.2.
               L-9907 (PROVED): .3 and its BOXED CAVEAT, which L-9921.2 generalizes;
               .1 is the model for the ported lower envelope L-9921.5(b).
               L-9903 (PROVED): the word constant rho(w) is used, but its recursion and
               the only property needed (rho_k >= 0) are re-derived inline as Lemma A_q,
               so no proof here depends on L-9903.
               L-9905 (PROVED): the object being ported in L-9921.6; its statement is
               quoted, its proof is re-derived from scratch in the 3x+q setting.
Scope:         All positive odd integers q; all a in Z (both signs and 0); all
               x in Q ∩ Z_2. L-9921.1–.4 and .6 are unconditional proofs. L-9921.5(a)
               is EXPLICITLY EMPIRICAL (a finite census); L-9921.5(b) is proved;
               L-9921.5(c) is an explicitly labelled UNVERIFIED port; L-9921.5(d) is a
               labelled subjective assessment, not a mathematical claim.
               Nothing here resolves Q-9904 or any part of the Collatz conjecture, and
               no direction is suggested for either.
Related counterexample candidates: none
```

---

## Statement

Throughout, $T$ is the shortcut map, taken in the 2-adic form established in L-9904:
$$T : \mathbb{Z}_2 \to \mathbb{Z}_2, \qquad
T(z) = \begin{cases} z/2 & z \text{ even},\\ (3z+1)/2 & z \text{ odd},\end{cases}$$
where "even"/"odd" for $z \in \mathbb{Z}_2$ means $z \in 2\mathbb{Z}_2$ / $z \notin
2\mathbb{Z}_2$. On $\mathbb{Z}^+$ this is D-9902 (L-9904, P0).
$\mathbb{Z}_{(2)} := \mathbb{Q} \cap \mathbb{Z}_2$ is the set of rationals with odd
denominator (L-9904, B7). For a positive odd integer $q$ put
$$\Lambda_q \;:=\; \tfrac{1}{q}\mathbb{Z} \;=\; \{\, a/q \,:\, a \in \mathbb{Z} \,\}
\;\subseteq\; \mathbb{Q}.$$

**D-9921.1 (the shortcut $3x+q$ map).** For a positive odd integer $q$ define
$$T_q : \mathbb{Z} \to \mathbb{Z}, \qquad
T_q(a) \;=\; \begin{cases} a/2 & a \text{ even},\\[2pt] (3a+q)/2 & a \text{ odd}.\end{cases}$$
This is well defined: if $a$ is odd then $3a$ is odd and $q$ is odd, so $3a+q$ is even.
$T_1 = T|_{\mathbb{Z}}$.

**D-9921.2 (divergence in absolute value).** A sequence $(y_k)_{k \ge 0}$ of rationals
**diverges in absolute value** if $|y_k| \to \infty$ as $k \to \infty$, i.e.
$\forall B \in \mathbb{R}\ \exists k_0\ \forall k \ge k_0 : |y_k| > B$. For sequences of
positive reals this is D-9907's "divergent"; the absolute value is required here because
$T_q$ does **not** preserve sign when $q > 1$ (e.g. $T_5(-1) = 1$; see Test M).

**D-9921.3 (eventually periodic orbit).** For a map $f$ of a set $X$ and $x \in X$, the
orbit $(f^k(x))_{k\ge0}$ is **eventually periodic** if
$\exists \ell \ge 0\ \exists K \ge 1 : f^{\ell+K}(x) = f^{\ell}(x)$.

---

**L-9921.1 (exact conjugacy on $\Lambda_q$).** Let $q$ be a positive odd integer.

1. *(Location.)* $\Lambda_q \subseteq \mathbb{Z}_{(2)} = \mathbb{Q} \cap \mathbb{Z}_2$,
   and $\Lambda_q$ is exactly the set of rationals whose lowest-terms denominator divides
   $q$. Moreover $\mathbb{Z}_{(2)} = \bigcup_{q \ \mathrm{odd},\, q \ge 1} \Lambda_q$,
   and $\Lambda_q \subseteq \Lambda_{q'}$ whenever $q \mid q'$.
2. *(Parity dictionary.)* For every $a \in \mathbb{Z}$ (no coprimality assumed),
   $a/q$ is odd in $\mathbb{Z}_2$ **iff** $a$ is an odd integer. The parity so computed
   does not depend on the representation: if $a/q = a'/q'$ with $q, q'$ positive odd,
   then $a \equiv a' \pmod 2$.
3. *(Invariance.)* $T(\Lambda_q) \subseteq \Lambda_q$; so $T$ restricts to a self-map
   $T|_{\Lambda_q} : \Lambda_q \to \Lambda_q$.
4. *(Conjugacy.)* The map $\mu_q : \Lambda_q \to \mathbb{Z}$, $\mu_q(x) := qx$, is a
   bijection with inverse $a \mapsto a/q$, and
   $$\mu_q \circ \big(T|_{\Lambda_q}\big) \;=\; T_q \circ \mu_q ,
   \qquad\text{equivalently}\qquad
   T\!\left(\frac{a}{q}\right) = \frac{T_q(a)}{q} \ \ \text{ for all } a \in \mathbb{Z}.$$
   Consequently, for all $a \in \mathbb{Z}$ and all $k \ge 0$,
   $$T^k\!\left(\frac{a}{q}\right) \;=\; \frac{T_q^k(a)}{q},$$
   so the whole forward $T$-orbit of $a/q$ lies in $\Lambda_q$, and the parity vectors
   agree: $v_i(a/q) = T_q^i(a) \bmod 2$ for all $i \ge 0$ (D-9906).
5. *(Both directions, dictionary form.)* For every $q$ positive odd and every
   $a \in \mathbb{Z}$, and for $x := a/q$: the $T$-orbit of $x$ is eventually periodic
   $\iff$ the $T_q$-orbit of $a$ is eventually periodic; and $|T^k(x)| \to \infty$
   $\iff$ $|T_q^k(a)| \to \infty$ (indeed $|T^k(x)| = |T_q^k(a)|/q$ for every $k$).
   Conversely every $x \in \mathbb{Z}_{(2)}$ arises this way: writing $x = p/q_0$ in
   lowest terms with $q_0 \ge 1$ odd, $x \in \Lambda_{q_0}$ and $\mu_{q_0}(x) = p$.

**L-9921.1b (denominator/gcd bookkeeping).** Let $q$ be positive odd, $a \in \mathbb{Z}$.
1. $\gcd(a,q) \mid \gcd(T_q(a), q)$; hence $k \mapsto \gcd(T_q^k(a), q)$ is
   non-decreasing for the divisibility order, and it is **constant** along any
   $T_q$-cycle.
2. Equivalently, the lowest-terms denominator of $T^{k+1}(a/q)$ divides that of
   $T^k(a/q)$, which divides $q$. The divisibility can be strict: $1/3 \mapsto 1$.
   So "$a/q$ in lowest terms" is **not** preserved by $T$ — but membership in
   $\Lambda_q$ is, which is all that L-9921.1 asserts and all that is used below.
3. *(Scaling.)* If $d$ is a positive odd divisor of $q$ then, for every $b \in
   \mathbb{Z}$, $T_q(d\,b) = d\, T_{q/d}(b)$, hence $T_q^k(d\,b) = d\,T_{q/d}^k(b)$ for
   all $k \ge 0$.
4. *(The factor 3.)* If $3 \mid q$ then: (i) $3\mathbb{Z}$ is $T_q$-invariant; (ii) for
   every odd $a$, $T_q(a) \in 3\mathbb{Z}$; (iii) every $T_q$-orbit meets $3\mathbb{Z}$;
   (iv) every $T_q$-cycle is contained in $3\mathbb{Z}$ and equals $3\cdot\Gamma$ for a
   unique $T_{q/3}$-cycle $\Gamma$.

**L-9921.2 (trichotomy on $\Lambda_q$; the pigeonhole is available here).**
Let $q$ be a positive odd integer and $x \in \Lambda_q$ (equivalently: $x$ is a rational
whose lowest-terms denominator divides $q$; equivalently, by .1, $x = a/q$ for a unique
$a \in \mathbb{Z}$, of either sign). Then **exactly one** of the following holds:

*(a)* the $T$-orbit of $x$ is eventually periodic — and then it takes finitely many
values, so $\sup_k |T^k(x)| < \infty$, and it eventually enters a unique $T$-cycle
contained in $\Lambda_q$;

*(b)* $|T^k(x)| \to \infty$ (divergence in absolute value, D-9921.2).

The same dichotomy holds verbatim for the $T_q$-orbit of any $a \in \mathbb{Z}$.
The proof is the pigeonhole of L-9901's Lemma D / L-9907.3, and it applies because of
the single hypothesis
$$\textbf{(P2)}\qquad
\#\big(\Lambda_q \cap [-B, B]\big) \;=\; 2\lfloor qB \rfloor + 1 \;<\; \infty
\qquad \text{for every real } B \ge 0 .$$

> **Relation to the caveats already in the packet (refinement, not correction of any
> proved statement).** L-9901's boxed remark and L-9907's BOXED CAVEAT both delimit the
> pigeonhole. L-9907 already recorded the correct fact for *positive* odd-denominator
> rationals on a *single* orbit. L-9921.2 is the general statement: it drops positivity
> (allowing $a < 0$, hence divergence in absolute value), it is stated for the whole
> ambient set $\Lambda_q$ rather than one orbit, and it makes explicit that the correct
> ambient set is $\Lambda_q$ and **not** $\mathbb{Z}_{(2)}$. L-9901's remark
> "*denominators may grow forever inside a bounded interval*" is a true statement about
> the **set** $\mathbb{Z}_{(2)}$ (which indeed fails (P2)) and it correctly says that the
> pigeonhole with ambient set $\mathbb{Z}_{(2)}$ yields nothing; it must **not** be read
> as saying that "unbounded $\Rightarrow$ divergent" fails for a single rational
> $T$-orbit. Along one orbit the denominators never grow (L-9921.1b(2)), so the orbit is
> confined to some $\Lambda_q$ and the implication does hold. Both files' proved
> statements stand unchanged; only the reading of the informal remark is sharpened.

**L-9921.3 (EXACT REDUCTION OF Q-9904).** The following four statements are equivalent.

- **(A)** *(Q-9904 answered affirmatively.)* For every $z \in \mathbb{Q} \cap
  \mathbb{Z}_2$ there exist $\ell \ge 0$ and $K \ge 1$ with $T^{\ell+K}(z) = T^{\ell}(z)$.
- **(B)** For every positive odd integer $q$ and every $a \in \mathbb{Z}$ there exist
  $\ell \ge 0$ and $K \ge 1$ with $T_q^{\ell+K}(a) = T_q^{\ell}(a)$.
- **(C)** For every positive odd integer $q$ there is **no** $a \in \mathbb{Z}$ with
  $|T_q^k(a)| \to \infty$; i.e. the shortcut $3x+q$ map has no divergent orbit on
  $\mathbb{Z}$.
- **(C$'$)** For every positive odd integer $q$ with $\gcd(q,3) = 1$ and every
  $a \in \mathbb{Z}$ with $\gcd(a,q) = 1$, the $T_q$-orbit of $a$ is not divergent in
  absolute value.

Fully quantified, (C) reads: $\forall q \in \mathbb{Z}^+$ with $q$ odd,
$\forall a \in \mathbb{Z}$, $\exists B \in \mathbb{R}$, $\forall k_0 \ge 0$,
$\exists k \ge k_0 : |T_q^k(a)| \le B$.
By L-9904.5(iii)(3b) each of (A)–(C$'$) is further equivalent to: *every rational
element of $\mathbb{Z}_2$ has an eventually periodic parity word.*

**L-9921.4 (Q-9904 contains the divergence half of Collatz; no converse claimed).**

1. $T_1 = T|_{\mathbb{Z}}$, so the instance $q = 1$ of (C) reads: no $a \in \mathbb{Z}$
   has $|T^k(a)| \to \infty$.
2. Restricting further to $a = n \in \mathbb{Z}^+$: for $n \in \mathbb{Z}^+$,
   $T^k(n) \to \infty \iff C^k(n) \to \infty$ (proved below from L-9901.2(iii) and
   L-9901.4). Hence (A) $\Rightarrow$ *no positive integer has a divergent Collatz
   orbit* — the **divergence half** of the Collatz conjecture (in the D-9909/L-9901.5
   dichotomy, this is exactly the elimination of alternative (c)).
3. *(The negative integers are consistent, and are extra content.)* $T$ maps
   $\mathbb{Z}^-$ into $\mathbb{Z}^-$, and $n \mapsto -n$ conjugates $T|_{\mathbb{Z}^-}$
   to the shortcut $3x-1$ map $T^-(n) = n/2$ ($n$ even), $(3n-1)/2$ ($n$ odd) on
   $\mathbb{Z}^+$. The three known negative $T$-cycles are, verified exactly below and
   in Test F,
   $$(-1),\qquad (-5,-7,-10),\qquad
   (-17,-25,-37,-55,-82,-41,-61,-91,-136,-68,-34),$$
   of least periods $1$, $3$, $11$. Being cycles, they are bounded, hence **not**
   divergent: they are consistent with (C) at $q=1$, and they are not counterexamples to
   anything asserted here. However, (C) at $q = 1$ also asserts that **no** negative
   integer has a divergent orbit, which is the divergence half of the $3x-1$ problem and
   is not part of the Collatz conjecture.
4. **Conclusion.** Q-9904 $\Rightarrow$ the divergence half of the Collatz conjecture.
   Therefore Q-9904 is **at least as hard** as that half. **No converse is claimed**:
   nothing here shows that the divergence half of Collatz implies Q-9904, nor even that
   it implies the $q=1$ instance of (C) (which additionally covers $\mathbb{Z}^-$).
   Nothing here asserts that Q-9904 is true, or that it is false.

**L-9921.5 (what is known, what this buys, and the honest verdict).**

*(a) EMPIRICAL — finite census, not proof.* For every odd $q \le 21$, a complete walk of
the $T_q$-orbit of every $a$ with $|a| \le 20000$ (escape window $|{\cdot}| \le 10^{15}$,
step cap $10^5$) resolved **every** start into a cycle: $0$ starts escaped the window and
$0$ starts hit the step cap. The cycles found are tabulated in the Proof section
(and printed in full in Adversarial tests). No claim whatsoever about divergence follows
from this: a finite search over a finite window cannot certify the absence of divergent
orbits, and the census says nothing about $|a| > 20000$.

*(b) PROVED — the lower-envelope criterion of L-9907.1 ports verbatim.* For every
positive odd $q$, every $a \in \mathbb{Z}^+$ and every $k \ge 0$,
$$T_q^k(a) \;\ge\; \frac{3^{\,a_k}}{2^{\,k}}\, a, \qquad a_k := \#\{ i < k :
T_q^i(a) \text{ odd}\},$$
so if $\limsup_k a_k/k > \gamma := \log_3 2$ the positive $T_q$-orbit of $a$ is
unbounded, and if $\liminf_k a_k/k > \gamma$ it is divergent.

*(c) UNVERIFIED PORT (labelled; not proved here, not used anywhere).* The proof of
L-9907.2 ("divergence forces $\liminf a_k/k \ge \gamma$") uses only the telescoping
identity and the bound $\varepsilon(x) = \log_2(1 + \tfrac{1}{3x}) \to 0$; in the
$3x+q$ setting the corresponding term is $\log_2(1 + \tfrac{q}{3x})$, which also tends to
$0$ as $x \to \infty$ for fixed $q$. The author expects the port to go through for each
fixed $q$ with $q$-dependent constants, but has **not** re-derived it and does not use it.

*(d) HONEST VERDICT (subjective assessment, explicitly not a theorem).* This reduction
does **not** make Q-9904 easier; it **reformulates** it. Three concrete reasons are
recorded, the first two of them proved:
  - (proved, L-9921.4) the single instance $q = 1$ already contains the divergence half
    of Collatz *and* the divergence half of the $3x-1$ problem, both open;
  - (proved, L-9921.6 Corollary 3) *every* finite binary word is the parity word of an
    integer periodic point of $T_q$ for a suitable positive odd $q$. Hence the packet's
    cycle-elimination results (L-9906, L-9912, L-9913, L-9915, L-9917) cannot possibly
    hold uniformly in $q$: they can only be re-run for one $q$ at a time, with bounds
    that degrade in $q$ (see L-9921.6 Corollary 4);
  - (assessment) the one genuine gain is a change of category, not of difficulty:
    on $\mathbb{Z}_2$ the words "bounded", "unbounded", "$\to\infty$" are meaningless,
    whereas on $\Lambda_q \cong \mathbb{Z}$ they are meaningful and the archimedean
    machinery of the packet becomes applicable (5(b) is the smallest instance). Q-9904
    thereby becomes a *family of concrete integer problems* rather than one statement
    about a null subset of $\mathbb{Z}_2$; it does not become a smaller problem.

**L-9921.6 (the cycle equation in the $3x+q$ setting).** Let $q$ be a positive odd
integer. Define the Syracuse-type map $S_q(x) := (3x+q)/2^{\nu_2(3x+q)}$ on
$\{x \in \mathbb{Z} : x \text{ odd},\ 3x + q \ne 0\}$.

**Lemma A$_q$ (iteration formula).** For all $a \in \mathbb{Z}$, $q$ positive odd and
$k \ge 0$, with $v_i := T_q^i(a) \bmod 2$, $a_k := \sum_{i<k} v_i$, and
$\rho_0 := 0$, $\rho_{i+1} := 3^{v_i}\rho_i + v_i 2^i$ (the word constant of L-9903
evaluated on $(v_0,\dots,v_{k-1})$):
$$2^k\, T_q^k(a) \;=\; 3^{\,a_k}\, a \;+\; q\,\rho_k , \qquad \rho_k \ge 0 .$$

**L-9921.6.1 (cycle equation, $S_q$-form).** Let $x_1 \to x_2 \to \dots \to x_m \to x_1$
be an $S_q$-cycle ($m \ge 1$ its least period, all $x_i$ odd integers, pairwise
distinct), with exponents $a_i := \nu_2(3x_i+q) \ge 1$, $A_0 := 0$,
$A_i := a_1 + \dots + a_i$, $K := A_m$, and
$$c \;:=\; \sum_{i=1}^{m} 3^{\,m-i}\, 2^{\,A_{i-1}} \;\in\; \mathbb{Z}^+ .$$
Then
$$\boxed{\;x_1\big(2^K - 3^m\big) \;=\; q\,c\;}$$
with **exactly the same** word-sum $c$ as in L-9905 (which is the case $q = 1$).
The constant $c$ depends on the anchoring $x_1$; the identity holds for every anchoring,
each with its own $c$, while $m$ and $K$ are anchor-independent.
Moreover $c = \rho(w)$, where $w \in \{0,1\}^K$ is the parity word of the corresponding
$T_q$-cycle read from the odd element $x_1$, so the $T_q$-form of the same statement is
$x_1(2^K - 3^{a_K}) = q\,\rho(w)$ with $a_K = m$.

**Corollary 1 (positivity and product formula).** For every $S_q$-cycle:
$c \ge 3^m - 2^m \ge m \ge 1$ (composition-level, using only $a_i \ge 1$, $A_0 = 0$,
$\sum a_i = K$), and $2^K = \prod_{i=1}^m\big(3 + q/x_i\big)$. Hence if all $x_i > 0$
then $2^K > 3^m$, and
$$x_1 \;=\; \frac{q\,c}{2^K - 3^m}\ \ge\ \frac{q\,(3^m - 2^m)}{2^K - 3^m},
\qquad
0 \;<\; \frac{K}{m} - \log_2 3 \;\le\; \frac{q}{3\, x_{\min}\, \ln 2}.$$

**Corollary 2 (the scaled-cycle correspondence — stated exactly).** Fix positive odd $q$.
1. If $\Gamma$ is a $T$-cycle in $\mathbb{Z}$ (a $3x{+}1$ shortcut cycle) then
   $q\Gamma := \{q\gamma : \gamma \in \Gamma\}$ is a $T_q$-cycle of the same length and
   the same parity word.
2. A $T_q$-cycle $\Delta$ has the form $q\Gamma$ with $\Gamma$ a $T$-cycle in
   $\mathbb{Z}$ **iff** $q \mid x$ for some — equivalently, by L-9921.1b(1), for every —
   $x \in \Delta$.
3. **The converse of 1 is FALSE in general.** For $q = 5$, $\Delta = \{1, 4, 2\}$ is a
   $T_5$-cycle and $1/5 \notin \mathbb{Z}$, so $\Delta$ is not $5$ times an integer
   $T$-cycle. What is always true is the *rational* statement: $x \mapsto x/q$ is a
   bijection from the set of $T_q$-cycles on $\mathbb{Z}$ onto the set of $T$-cycles
   contained in $\Lambda_q$. (Here $\Delta/5 = \{1/5, 4/5, 2/5\}$, which is exactly the
   rational $T$-cycle of L-9904.6 item 5.)
4. In general, let $d := \gcd(x, q)$ for any $x \in \Delta$ (constant on $\Delta$ by
   L-9921.1b(1)). Then $\Delta = d\cdot\Delta'$ where $\Delta' := \{x/d : x \in \Delta\}$
   is a $T_{q/d}$-cycle with $\gcd(x', q/d) = 1$ for every $x' \in \Delta'$. So every
   $T_q$-cycle is $d$ times a **primitive** $T_{q/d}$-cycle for a unique divisor
   $d \mid q$; item 2 is the case $d = q$.

**Corollary 3 (every word is a cycle word for some $q$).** Let $w \in \{0,1\}^K$ with
$K \ge 1$, $a := |w|_1$, $D := 2^K - 3^{a}$ (an odd nonzero integer), $\rho_w := \rho(w)$,
$g := \gcd(|D|, \rho_w)$ (with $\gcd(|D|,0) = |D|$) and $q_w := |D|/g$, an odd positive
integer. Then for every positive odd $q$:
$$\exists\, x \in \mathbb{Z}:\ T_q^K(x) = x \ \text{ and the } T_q\text{-parity word of }
x \text{ is } w^\infty \iff q_w \mid q,$$
and in that case $x = q\rho_w/D$ is the unique such integer. In particular $q = q_w$
always works: **every** finite binary word is realized by an integer periodic point of
$T_q$ for some positive odd $q$.

**Corollary 4 (what degrades in $q$).** In Corollary 1 the bound
$K/m - \log_2 3 \le q/(3 x_{\min}\ln 2)$ carries the factor $q$, and the element bound
carries the factor $q$; so every quantitative cycle-exclusion argument of the packet
weakens linearly in $q$ when ported. Combined with Corollary 3, this is the precise
reason no cycle-side argument can be uniform in $q$.

---

## Definitions

All Collatz notation is from `NOTATION.md`. Additional notation, fixed for this file:

- $q$ always denotes a **positive odd integer**; $a, b, x, y$ denote integers;
  $z$ denotes an element of $\mathbb{Z}_2$; $\mathbb{Z}^- := \{-1,-2,-3,\dots\}$.
- $\Lambda_q := \tfrac1q\mathbb{Z}$, $\ \mathbb{Z}_{(2)} := \mathbb{Q}\cap\mathbb{Z}_2$.
- $T_q$ is D-9921.1; $T = T_1$ on $\mathbb{Z}$ and $T$ also denotes the 2-adic map of
  L-9904 (they agree on $\mathbb{Z}$, by L-9904's P0).
- "**Divergent**" for an integer or rational orbit means D-9921.2 (divergence in
  absolute value). For orbits in $\mathbb{Z}^+$ this coincides with D-9907.
- **Word constant** (L-9903.2, a purely combinatorial object): for
  $w = (w_0,\dots,w_{K-1}) \in \{0,1\}^K$, $r_0 := 0$,
  $r_{i+1} := 3^{w_i} r_i + w_i 2^i$, $\rho(w) := r_K$; closed form
  $\rho(w) = \sum_{i : w_i = 1} 3^{s_i(w)} 2^i$ with $s_i(w) := \#\{j > i : w_j = 1\}$.
  Only the recursion and $\rho(w) \ge 0$ are used, both re-derived in Lemma A$_q$.
- A **$T_q$-cycle** is a purely periodic $T_q$-orbit, identified with its (finite) point
  set; its **length** is its least period (D-9908, transported to this map). A
  $T_q$-cycle $\Delta$ is **primitive** if $\gcd(x, q) = 1$ for one — equivalently every,
  by L-9921.1b(1) — $x \in \Delta$.
- **Anchoring** an $S_q$-cycle at $x_r$ means the cyclic relabelling of L-9905's
  Definitions; $m$ and $K$ are anchor-independent, $c$ and the $A_i$ are not.
- Empty sums are $0$, empty products are $1$.

**Imported facts, with the exact place of use.**
- **(B7 of L-9904)** $\mathbb{Q} \cap \mathbb{Z}_2 = \mathbb{Z}_{(2)}$, and for
  $p/q$ with $q$ odd, $p/q \equiv p \pmod{2\mathbb{Z}_2}$. Used in L-9921.1(1),(2).
- **(L-9904, P0 and L-9904.1)** $T$ is a well-defined self-map of $\mathbb{Z}_2$ agreeing
  with D-9902 on $\mathbb{Z}^+$ and mapping $\mathbb{Z}_{(2)}$ into itself. Used
  throughout.
- **(L-9904.5(i))** every infinite binary word is the parity word of exactly one
  $z \in \mathbb{Z}_2$. Used in L-9921.6 Corollary 3 (uniqueness).
- **(L-9904.5(ii))** the unique $z$ with parity word $w^\infty$ satisfies $T^K(z) = z$
  and $z = \rho(w)/(2^K - 3^{|w|_1})$. Used in L-9921.6 Corollary 3.
- **(L-9904.5(iii)(3b))** orbit eventually periodic $\iff$ parity word eventually
  periodic. Used in the closing remark of L-9921.3.
- **(L-9901.2(iii), L-9901.4)** simultaneous boundedness of the $C$- and $T$-orbits of
  $n \in \mathbb{Z}^+$, and the $\mathbb{Z}^+$ trichotomy. Used **only** in L-9921.4(2).
- **(L-9901.5)** the counterexample dichotomy (nontrivial cycle *or* divergence). Used
  only to phrase "the divergence half" in L-9921.4.

---

## Motivation

L-9904 proved that $T$ on $\mathbb{Z}_2$ is the full binary shift, that every parity word
is realized, and that the realizer of an eventually periodic word is automatically a
rational with odd denominator. It then recorded **Q-9904**: *is every rational element of
$\mathbb{Z}_2$ eventually $T$-periodic?* — noting that an affirmative answer would rule
out divergent positive-integer trajectories. L-9904's own "Suggested next attack" item 4
proposed exactly the present investigation ("for fixed odd denominator $q$, $T$ maps
$\{p/q\}$ to itself; the induced map on numerators is a finite-data object").

This file executes that program and finds that the induced object is not merely
"finite-data" but a completely classical one: the shortcut $3x+q$ map on $\mathbb{Z}$.
The value of pinning this down exactly is fourfold.

- **It converts an open question of the packet into a statement about integers.**
  Q-9904 quantifies over a $\mu$-null subset of $\mathbb{Z}_2$ (L-9904, B8), where no
  archimedean notion of size exists, so none of the packet's growth machinery (L-9905,
  L-9907, L-9908, L-9910, L-9913, L-9917) can even be stated. After L-9921.1 the same
  question is a statement about integer orbits, where all of it can be stated. L-9921.5(b)
  is the smallest example actually carried across.
- **It repairs a reading of the pigeonhole caveats.** L-9901 and L-9907 both fence off the
  "unbounded $\Rightarrow$ divergent" step as integer-only. L-9907 already corrected the
  folklore for single positive rational orbits; L-9921.2 gives the general statement with
  the correct ambient set $\Lambda_q$, both signs, and the exact finiteness hypothesis
  (P2). A construction that produces a bounded, non-periodic *rational* orbit is thereby
  ruled out — which closes off one tempting family of counterexample designs.
- **It calibrates the difficulty of Q-9904 honestly.** L-9921.4 shows Q-9904 strictly
  contains the divergence half of Collatz plus the divergence half of $3x-1$. Any agent
  planning to "settle Q-9904 and thereby learn something about Collatz" should read
  L-9921.5(d) first: the reduction is a reformulation, not a simplification.
- **It supplies a rich test-bed for the cycle machinery.** L-9921.6 ports L-9905 exactly,
  with the single change $c \mapsto qc$; the census of L-9921.5(a) exhibits many cycles
  in the family (e.g. seven distinct $8$-element $S_{13}$-cycles), so a candidate
  cycle-exclusion technique can be *falsified* cheaply by running it at $q > 1$, where
  cycles demonstrably exist. Corollary 3 makes precise that any technique which would
  exclude cycles for all $q$ is wrong.

---

## Proof

### P0. Preliminaries on $\Lambda_q$

Fix a positive odd integer $q$.

**(P0.1) $\Lambda_q$ is the set of rationals with lowest-terms denominator dividing $q$.**
If $x = a/q$ with $a \in \mathbb{Z}$, write $d := \gcd(a,q) \ge 1$; then
$x = (a/d)/(q/d)$ is in lowest terms with denominator $q/d \mid q$. Conversely, if
$x = p/q'$ in lowest terms with $q' \mid q$, then $x = \big(p\cdot(q/q')\big)/q \in
\Lambda_q$ because $q/q' \in \mathbb{Z}$. $\square$

**(P0.2) $\Lambda_q \subseteq \mathbb{Z}_{(2)}$, and $\mathbb{Z}_{(2)} = \bigcup_q
\Lambda_q$.** By (P0.1) the lowest-terms denominator of any $x \in \Lambda_q$ divides the
odd number $q$, hence is odd, so $x \in \mathbb{Z}_{(2)}$ by B7. Conversely, if
$x \in \mathbb{Z}_{(2)}$, write $x = p/q_0$ in lowest terms with $q_0 \ge 1$; $q_0$ is
odd by B7, and $x \in \Lambda_{q_0}$. Finally, if $q \mid q'$ then
$a/q = (a\,(q'/q))/q'$, so $\Lambda_q \subseteq \Lambda_{q'}$. $\square$

**(P0.3) Uniqueness of the numerator.** For fixed $q$, the map $a \mapsto a/q$ is
injective on $\mathbb{Z}$ (multiply by $q \neq 0$), so every $x \in \Lambda_q$ has a
*unique* representation $x = a/q$ with $a = qx \in \mathbb{Z}$. Hence "the numerator of
$x$ over $q$" is well defined without any coprimality convention. $\square$

### L-9921.1(2) — the parity dictionary

Let $a \in \mathbb{Z}$ and let $q$ be positive odd. By B3 of L-9904, $q$ is a unit of
$\mathbb{Z}_2$ and $q^{-1}$ is odd, so $q^{-1} = 1 + 2t$ for some $t \in \mathbb{Z}_2$
and
$$\frac{a}{q} \;=\; a\,q^{-1} \;=\; a + 2at \;\equiv\; a \pmod{2\mathbb{Z}_2}.$$
By L-9904's P0, an integer $a$ is even in $\mathbb{Z}_2$ iff it is even in $\mathbb{Z}$.
Therefore $a/q$ is odd in $\mathbb{Z}_2$ iff $a$ is an odd integer.

*Representation-independence.* Suppose $a/q = a'/q'$ with $q, q'$ positive odd. Then
$aq' = a'q$; reducing mod $2$ and using that $q, q'$ are odd gives $a \equiv a' \pmod 2$.
(Equivalently: both compute the $0$-th 2-adic digit of the same element.) $\blacksquare$

*(Independent numerical check of exactly this statement, computing the 2-adic side from
$q^{-1} \bmod 2^{64}$ rather than from the numerator: Test A.)*

### L-9921.1(3),(4) — invariance and conjugacy

Let $a \in \mathbb{Z}$ and put $x := a/q$.

*Case $a$ even.* By L-9921.1(2), $x$ is even in $\mathbb{Z}_2$, so
$$T(x) \;=\; \frac{x}{2} \;=\; \frac{a}{2q} \;=\; \frac{a/2}{q} \;=\; \frac{T_q(a)}{q},$$
and $a/2 \in \mathbb{Z}$, so $T(x) \in \Lambda_q$. (The middle equalities are identities
in $\mathbb{Q}$; they agree with the 2-adic division by $2$ because $\mathbb{Q} \cap
\mathbb{Z}_2 \subseteq \mathbb{Z}_2$ is a subring and $2\cdot\frac{a}{2q} = x$, division
by $2$ being unique in the integral domain $\mathbb{Z}_2$ — B2.)

*Case $a$ odd.* By L-9921.1(2), $x$ is odd in $\mathbb{Z}_2$, so
$$T(x) \;=\; \frac{3x+1}{2} \;=\; \frac{\frac{3a}{q} + 1}{2} \;=\; \frac{3a+q}{2q}
\;=\; \frac{(3a+q)/2}{q} \;=\; \frac{T_q(a)}{q},$$
and $(3a+q)/2 \in \mathbb{Z}$ because $3a$ and $q$ are both odd, so $3a + q$ is even.
Hence $T(x) \in \Lambda_q$.

The two cases are exhaustive and mutually exclusive, which proves both
$T(\Lambda_q) \subseteq \Lambda_q$ (item 3) and the one-step identity
$T(a/q) = T_q(a)/q$ (item 4). Since $\mu_q(x) = qx$ is a bijection $\Lambda_q \to
\mathbb{Z}$ (P0.3, with inverse $a \mapsto a/q$), the identity is exactly
$\mu_q \circ T|_{\Lambda_q} = T_q \circ \mu_q$, i.e. a conjugacy of self-maps.

*Iteration.* By induction on $k$: for $k = 0$ both sides are $a/q$; if
$T^k(a/q) = T_q^k(a)/q$ then applying $T$ and the one-step identity at the integer
$T_q^k(a)$ gives $T^{k+1}(a/q) = T_q\big(T_q^k(a)\big)/q = T_q^{k+1}(a)/q$. In
particular every forward iterate lies in $\Lambda_q$.

*Parity vectors.* $v_i(a/q) = T^i(a/q) \bmod 2\mathbb{Z}_2 = \big(T_q^i(a)/q\big) \bmod
2\mathbb{Z}_2 = T_q^i(a) \bmod 2$ by L-9921.1(2) applied to the integer $T_q^i(a)$.
$\blacksquare$

*(Numerical check, stepwise, in exact rational arithmetic with both signs of $a$ and
$k \le 200$: Test B.)*

### L-9921.1(5) — the dictionary in both directions

Let $q$ be positive odd, $a \in \mathbb{Z}$, $x := a/q$.

*Eventual periodicity.* If $T^{\ell+K}(x) = T^{\ell}(x)$ with $\ell \ge 0$, $K \ge 1$,
then by item 4, $T_q^{\ell+K}(a)/q = T_q^{\ell}(a)/q$; multiplying by $q \ne 0$ gives
$T_q^{\ell+K}(a) = T_q^{\ell}(a)$. Conversely, if $T_q^{\ell+K}(a) = T_q^{\ell}(a)$ then
dividing by $q$ and using item 4 gives $T^{\ell+K}(x) = T^{\ell}(x)$.

*Magnitudes.* $|T^k(x)| = |T_q^k(a)|/q$ for every $k$, by item 4 and $q > 0$. Since $q$
is a fixed positive constant, $|T^k(x)| \to \infty \iff |T_q^k(a)| \to \infty$
(for $B > 0$: $|T^k(x)| > B \iff |T_q^k(a)| > qB$).

*Surjectivity of the dictionary.* Given $z \in \mathbb{Z}_{(2)}$, (P0.2) supplies
$q_0 \ge 1$ odd with $z \in \Lambda_{q_0}$ (take $q_0$ = the lowest-terms denominator),
and $\mu_{q_0}(z) = q_0 z = p \in \mathbb{Z}$. Note that *any* odd multiple of $q_0$ also
works, by $\Lambda_{q_0} \subseteq \Lambda_{q}$ for $q_0 \mid q$; the correspondence is
not canonical in $q$, only in the pair $(q, a)$. $\blacksquare$

### L-9921.1b — bookkeeping

**(1) $\gcd$ monotonicity.** Let $d := \gcd(a, q)$. Then $d \mid q$, and $q$ is odd, so
$d$ is odd. If $a$ is even, then $a = 2^{\nu}u$ with $\nu \ge 1$ and $d \mid a$ with $d$
odd forces $d \mid u$, hence $d \mid a/2 = T_q(a)$. If $a$ is odd, then $d \mid 3a$ and
$d \mid q$, so $d \mid 3a+q$; as $d$ is odd and $3a+q = 2\cdot T_q(a)$, we get
$d \mid T_q(a)$. In both cases $d \mid T_q(a)$ and $d \mid q$, so
$d \mid \gcd(T_q(a), q)$. Iterating gives the divisibility-monotonicity in $k$.

*Constancy on a cycle.* If $T_q^{K}(x) = x$ with $K \ge 1$, then
$\gcd(x,q) \mid \gcd(T_q(x),q) \mid \dots \mid \gcd(T_q^{K}(x),q) = \gcd(x,q)$, so all
these divisibilities are equalities and $\gcd(\cdot,q)$ is constant on the cycle.
$\square$

**(2) Denominators.** By (P0.1) the lowest-terms denominator of $T_q^k(a)/q$ is
$q/\gcd(T_q^k(a), q)$; by (1) the gcd is non-decreasing for divisibility, so the
denominator is non-increasing for divisibility, and it divides $q$ throughout. Strictness
occurs: $\gcd(1,3) = 1$ while $T_3(1) = (3 + 3)/2 = 3$ has $\gcd(3,3) = 3$, i.e.
$T(1/3) = 1$ and the denominator drops from $3$ to $1$. $\square$

**(3) Scaling.** Let $d \mid q$ with $d$ odd positive, $\tilde q := q/d$ (odd), and
$b \in \mathbb{Z}$. Since $d$ is odd, $db \equiv b \pmod 2$. If $b$ is even,
$T_q(db) = db/2 = d(b/2) = d\,T_{\tilde q}(b)$. If $b$ is odd,
$T_q(db) = (3db + d\tilde q)/2 = d\,(3b + \tilde q)/2 = d\,T_{\tilde q}(b)$, the middle
expression being an integer because $3b + \tilde q$ is even. Induction on $k$ gives
$T_q^k(db) = d\,T_{\tilde q}^k(b)$. $\square$

**(4) The factor 3.** Assume $3 \mid q$ and write $\tilde q := q/3$ (odd).
*(ii)* If $a$ is odd then $T_q(a) = (3a+q)/2 = 3\,(a + \tilde q)/2$, and
$(a+\tilde q)/2 \in \mathbb{Z}$ because $a$ and $\tilde q$ are both odd; so
$T_q(a) \in 3\mathbb{Z}$.
*(i)* If $3 \mid b$: for $b$ even, $3 \mid b$ and $b/2 \in \mathbb{Z}$ with $3$ odd give
$3 \mid b/2 = T_q(b)$; for $b$ odd, $3 \mid 3b$ and $3 \mid q$ give $3 \mid 3b+q$, and
$3$ odd gives $3 \mid (3b+q)/2 = T_q(b)$. So $3\mathbb{Z}$ is $T_q$-invariant.
*(iii)* If some iterate $T_q^{j}(a)$ is odd, then $T_q^{j+1}(a) \in 3\mathbb{Z}$ by (ii)
and the orbit stays there by (i). Otherwise every iterate is even, so $T_q^k(a) = a/2^k
\in \mathbb{Z}$ for all $k$, forcing $2^k \mid a$ for all $k$, i.e. $a = 0 \in
3\mathbb{Z}$.
*(iv)* A cycle equals its own tail, and by (iii) some tail element lies in $3\mathbb{Z}$;
by (i) all subsequent elements do, and going once around the cycle covers all of it. So
$\Delta \subseteq 3\mathbb{Z}$, and by (3) with $d = 3$, $\Delta/3$ is a $T_{\tilde
q}$-cycle (a set of the same size, cyclically permuted the same way), uniquely determined
by $\Delta$. $\square$

*(Numerical checks: Tests C, D, E. The census of L-9921.5(a) independently confirms (iv):
for $q \in \{3, 9, 15, 21\}$ the search found $0$ primitive cycles.)*

### L-9921.2 — the trichotomy on $\Lambda_q$

Fix a positive odd $q$ and $x \in \Lambda_q$; write $a := qx \in \mathbb{Z}$ (P0.3). By
L-9921.1(5) it suffices to prove the dichotomy for the $T_q$-orbit of $a$ in
$\mathbb{Z}$, or equivalently for the $T$-orbit of $x$ in $\Lambda_q$; we argue in
$\Lambda_q$, since (P2) is the property being highlighted.

**Step 1: (P2).** For real $B \ge 0$,
$$\Lambda_q \cap [-B, B] \;=\; \Big\{\tfrac{a}{q} : a \in \mathbb{Z},\ |a| \le qB\Big\}
\;=\; \Big\{\tfrac{a}{q} : a \in \mathbb{Z},\ |a| \le \lfloor qB\rfloor \Big\},$$
a set of exactly $2\lfloor qB\rfloor + 1$ elements — in particular finite. (The second
equality holds because $a$ is an integer.) $\square$

**Step 2: (a) and (b) are mutually exclusive.** Suppose the orbit is eventually
periodic, say $T^{\ell+K}(x) = T^{\ell}(x)$ with $\ell \ge 0$, $K \ge 1$. Then for every
$k \ge \ell$, division with remainder $k - \ell = sK + r$ ($s \ge 0$, $0 \le r < K$) and
$s$-fold application of the periodicity gives $T^k(x) = T^{\ell + r}(x)$; hence
$$\{T^k(x) : k \ge 0\} \;=\; \{T^0(x), \dots, T^{\ell+K-1}(x)\}$$
is finite, so $B_0 := \max_{0 \le j < \ell+K} |T^j(x)| < \infty$ bounds every iterate and
$|T^k(x)| \to \infty$ fails. Conversely, if $|T^k(x)| \to \infty$ then no bound exists,
so the orbit is not eventually periodic. $\square$

**Step 3: at least one of (a),(b) holds — the pigeonhole.** Suppose (b) fails. Negating
D-9921.2: there is $B \in \mathbb{R}$ such that $I := \{k \ge 0 : |T^k(x)| \le B\}$ is
infinite. For $k \in I$ the value $T^k(x)$ lies in $\Lambda_q \cap [-B,B]$ (using
L-9921.1(3): the whole orbit stays in $\Lambda_q$), a finite set by Step 1. Infinitely
many indices and finitely many values force, by the pigeonhole principle, some value
$y$ with $T^{k_1}(x) = T^{k_2}(x) = y$ for two indices $k_1 < k_2$. Since $T$ is a
function, induction on $t \ge 0$ gives $T^{k_1+t}(x) = T^{k_2+t}(x)$; with
$K := k_2 - k_1 \ge 1$ and $\ell := k_1$ this is $T^{\ell+K}(x) = T^{\ell}(x)$, i.e. (a).
$\square$

**Step 4: the tail is a cycle, and it lies in $\Lambda_q$.** In case (a), let $\ell, K$ be
as above with $K$ minimal. Then $\Delta := \{T^{\ell}(x), \dots, T^{\ell+K-1}(x)\}$ is a
purely periodic orbit, i.e. a $T$-cycle, contained in $\Lambda_q$ by L-9921.1(3). It is
unique: any cycle containing a tail point of the orbit contains the whole forward orbit of
that point, hence equals $\Delta$. $\square$

Steps 2–4 give "exactly one of (a),(b)", and the parenthetical claims of (a).
Transporting through $\mu_q$ (L-9921.1(5)) yields the identical statement for
$T_q$-orbits on $\mathbb{Z}$; alternatively, for $T_q$ the ambient set is $\mathbb{Z}$
itself and $\mathbb{Z} \cap [-B,B]$ is finite, which is the same argument with
$q = 1$. $\blacksquare$

*(Numerical checks: Test K for (P2); Test L for 400 random rational orbits, all of which
resolved into cycles with every iterate in $\Lambda_q$.)*

**Remark (what Step 3 does and does not need).** Exactly the two ingredients isolated in
L-9907's boxed caveat are used: (P1) the sequence is a single deterministic orbit of one
starting point — used in "$T$ is a function, so a repeat propagates"; and (P2) the ambient
set meets every bounded interval in a finite set. Nothing else. The point of this file is
that a rational orbit satisfies both, with ambient set $\Lambda_q$ rather than
$\mathbb{Z}_{(2)}$. For a $z \in \mathbb{Z}_2 \setminus \mathbb{Q}$ the statement is not
merely unproved but ill-posed: no archimedean absolute value exists on $\mathbb{Z}_2$
(L-9907's caveat, failure mode 1).

### L-9921.3 — the equivalence

**(A) $\Rightarrow$ (B).** Let $q$ be positive odd and $a \in \mathbb{Z}$. By (P0.2),
$x := a/q \in \Lambda_q \subseteq \mathbb{Q}\cap\mathbb{Z}_2$. By (A) there are
$\ell \ge 0$, $K \ge 1$ with $T^{\ell+K}(x) = T^{\ell}(x)$. By L-9921.1(5),
$T_q^{\ell+K}(a) = T_q^{\ell}(a)$. $\square$

**(B) $\Rightarrow$ (A).** Let $z \in \mathbb{Q} \cap \mathbb{Z}_2$. By B7, $z = p/q_0$
in lowest terms with $q_0 \ge 1$ odd and $p \in \mathbb{Z}$, so $z \in \Lambda_{q_0}$ and
$\mu_{q_0}(z) = p$. By (B) applied to $(q_0, p)$ there are $\ell \ge 0$, $K \ge 1$ with
$T_{q_0}^{\ell+K}(p) = T_{q_0}^{\ell}(p)$. By L-9921.1(5),
$T^{\ell+K}(z) = T^{\ell}(z)$. $\square$

**(B) $\Rightarrow$ (C).** Let $q$ be positive odd, $a \in \mathbb{Z}$. By (B) the
$T_q$-orbit of $a$ is eventually periodic, hence (Step 2 of L-9921.2, transported) it is
bounded in absolute value, so $|T_q^k(a)| \to \infty$ fails. $\square$

**(C) $\Rightarrow$ (B).** Let $q$ be positive odd, $a \in \mathbb{Z}$. By L-9921.2
(applied to $x = a/q$, or directly on $\mathbb{Z}$) exactly one of "eventually periodic"
and "divergent in absolute value" holds; (C) excludes the second, so the first holds.
$\square$

**(C) $\Rightarrow$ (C$'$).** (C$'$) is a special case of (C). $\square$

**(C$'$) $\Rightarrow$ (C).** We prove the contrapositive via:

> **Reduction Lemma R.** *If there exist a positive odd $q$ and $a \in \mathbb{Z}$ whose
> $T_q$-orbit is divergent in absolute value, then there exist a positive odd $q^*$ with
> $\gcd(q^*,3) = 1$ and $a^* \in \mathbb{Z}$ with $\gcd(a^*, q^*) = 1$ whose
> $T_{q^*}$-orbit is divergent in absolute value.*

*Proof of R, by strong induction on $q \ge 1$.* Suppose the $T_q$-orbit of $a$ is
divergent.

*Case 1: $d := \gcd(a,q) > 1$.* By L-9921.1b(3), $T_q^k(a) = d\,T_{q/d}^k(a/d)$ for all
$k$, so $|T_{q/d}^k(a/d)| = |T_q^k(a)|/d \to \infty$: the $T_{q/d}$-orbit of $a/d$ is
divergent, and $1 \le q/d < q$. Apply the induction hypothesis to $(q/d, a/d)$.

*Case 2: $\gcd(a,q) = 1$ and $3 \mid q$.* The orbit is divergent, hence not the constant
orbit at $0$, so $a \neq 0$; by L-9921.1b(4)(iii) there is $j \ge 0$ with
$b := T_q^j(a) \in 3\mathbb{Z}$. The $T_q$-orbit of $b$ is the $j$-shifted tail of the
orbit of $a$, hence also divergent (a tail of a sequence tending to $\infty$ in absolute
value tends to $\infty$). Now $3 \mid \gcd(b, q)$, so $\gcd(b,q) > 1$ and Case 1 applied
to $(q, b)$ produces a divergent $T_{q'}$-orbit with $q' = q/\gcd(b,q) \le q/3 < q$;
apply the induction hypothesis to it.

*Case 3: $\gcd(a,q) = 1$ and $3 \nmid q$.* Take $(q^*, a^*) := (q, a)$.

The induction is well founded: Cases 1 and 2 both invoke the hypothesis at a strictly
smaller positive odd modulus, and at $q = 1$ we are necessarily in Case 3 (since
$\gcd(a,1) = 1$ and $3 \nmid 1$). $\square$

Given Lemma R, suppose (C) fails: some $T_q$-orbit is divergent. Then R produces a
divergent $T_{q^*}$-orbit of some $a^*$ with $\gcd(q^*,3)=1$ and $\gcd(a^*,q^*)=1$,
contradicting (C$'$). Hence (C$'$) $\Rightarrow$ (C). $\blacksquare$

**Closing remark of L-9921.3.** By L-9904.5(iii)(3b), for $z \in \mathbb{Z}_2$ the orbit
is eventually periodic iff $V(z)$ is eventually periodic; so (A) is also equivalent to
"every rational element of $\mathbb{Z}_2$ has eventually periodic parity word", which is
the second phrasing of Q-9904 in L-9904. $\square$

### L-9921.4 — Q-9904 strictly contains a Collatz statement

**(1)** $T_1(a) = a/2$ for even $a$ and $(3a+1)/2$ for odd $a$, which is the restriction
of the 2-adic $T$ to $\mathbb{Z}$ (L-9904, P0). So (C) at $q=1$ says precisely: no
$a \in \mathbb{Z}$ has $|T^k(a)| \to \infty$. $\square$

**(2) The $C$/$T$ transfer on $\mathbb{Z}^+$.** Let $n \in \mathbb{Z}^+$. Both $C$ and
$T$ are self-maps of $\mathbb{Z}^+$ (D-9901, D-9902), so both orbits lie in
$\mathbb{Z}^+$ and $|{\cdot}|$ is the ordinary value. By L-9901.2(iii),
$\sup_k C^k(n) < \infty \iff \sup_k T^k(n) < \infty$. By L-9901.4 (equivalently L-9904's
Lemma D) applied to each map, for orbits in $\mathbb{Z}^+$: unbounded $\iff$ divergent.
Chaining,
$$T^k(n) \to \infty \iff \sup_k T^k(n) = \infty \iff \sup_k C^k(n) = \infty
\iff C^k(n) \to \infty .$$
Hence (A) $\Rightarrow$ (C) $\Rightarrow$ [$q=1$, $a = n > 0$] no $n \in \mathbb{Z}^+$ has
$T^k(n) \to \infty$ $\Rightarrow$ no $n \in \mathbb{Z}^+$ has $C^k(n) \to \infty$. In the
language of L-9901.5, alternative (c) of the trichotomy is eliminated for every
$n \in \mathbb{Z}^+$: this is the divergence half of the Collatz conjecture. (The
remaining half — that no nontrivial cycle exists — is untouched by Q-9904, since a
nontrivial $T$-cycle in $\mathbb{Z}^+$ *is* an eventually periodic rational orbit and is
therefore fully consistent with (A).) $\square$

**(3) The negative integers.**

*Sign preservation at $q=1$.* If $a < 0$ is even then $T(a) = a/2 < 0$; if $a < 0$ is odd
then $a \le -1$, so $3a + 1 \le -2$ and $T(a) = (3a+1)/2 \le -1 < 0$. So
$T(\mathbb{Z}^-) \subseteq \mathbb{Z}^-$.

*Conjugacy with $3x-1$.* Define $T^-(n) := n/2$ for even $n \in \mathbb{Z}^+$ and
$(3n-1)/2$ for odd $n \in \mathbb{Z}^+$ (this is a self-map of $\mathbb{Z}^+$: for odd
$n \ge 1$, $3n - 1 \ge 2$ is even). For $n \in \mathbb{Z}^+$: if $n$ is even then
$T(-n) = -n/2 = -T^-(n)$; if $n$ is odd then $-n$ is odd and
$T(-n) = (-3n+1)/2 = -(3n-1)/2 = -T^-(n)$. So $n \mapsto -n$ conjugates $T^-$ on
$\mathbb{Z}^+$ with $T$ on $\mathbb{Z}^-$.

*The three cycles, verified by exact computation.*
$$T(-1) = \tfrac{3(-1)+1}{2} = -1 ,$$
$$-5 \xrightarrow{\ (3(-5)+1)/2\ } -7 \xrightarrow{\ (3(-7)+1)/2\ } -10
\xrightarrow{\ -10/2\ } -5 ,$$
$$-17 \to -25 \to -37 \to -55 \to -82 \to -41 \to -61 \to -91 \to -136 \to -68 \to -34
\to -17 ,$$
where each odd step is $(3x+1)/2$ and each even step is $x/2$; the eleven listed values
are pairwise distinct, so the least period is $11$ (and $1$, $3$ respectively for the
first two). Each of these orbits is purely periodic, hence finite, hence bounded, hence
**not** divergent in absolute value (Step 2 of L-9921.2). They are therefore consistent
with (C) at $q = 1$; no contradiction arises from allowing negative $a$.

*Extra content.* (C) at $q=1$ additionally asserts that no $a \in \mathbb{Z}^-$ has a
divergent orbit, equivalently (by the conjugacy above) that no $n \in \mathbb{Z}^+$ has a
divergent $T^-$-orbit. That is the divergence half of the $3x-1$ problem, which is open
and is not part of the Collatz conjecture. $\square$

**(4) Conclusion, precisely stated.** Q-9904 (statement (A)) implies the divergence half
of the Collatz conjecture; hence proving Q-9904 is at least as hard as proving that half.
**No converse is claimed** and none is proved here: this file does not show that the
divergence half of Collatz implies (A), nor that it implies (C) at $q = 1$, nor that (A)
holds or fails. $\blacksquare$

*(Numerical check of the three cycles, their closure and their least periods: Test F.)*

### L-9921.5 — census, ported envelope, verdict

**(a) The census (EMPIRICAL).** Method: for each odd $q \le 21$, walk the $T_q$-orbit of
every start $a$ with $|a| \le 20000$, memoising resolved values; a start is *resolved*
when its orbit meets a previously resolved value or repeats a value on its own path;
it is *unresolved* if $|{\rm value}| > 10^{15}$ (escaped the window) or $10^5$ steps
elapse. Result: **every** start resolved — $0$ escaped, $0$ hit the step cap — and the
following cycles were met (full listing in Adversarial tests; $K$ = cycle length,
$m$ = number of odd elements, "$d$" = the constant $\gcd(x,q)$ of L-9921.1b(1)).

| $q$ | cycles found | primitive ($d=1$) | primitive cycles (anchored at the element of least $\lvert\cdot\rvert$), as $(K, m)$ |
|---|---|---|---|
| 1 | 5 | 5 | $\{0\}$ $(1,0)$; $\{-1\}$ $(1,1)$; $\{1,2\}$ $(2,1)$; $\{-5,-7,-10\}$ $(3,2)$; $\{-17,\dots\}$ $(11,7)$ |
| 3 | 5 | 0 | — (all are $3\times$ a $T_1$-cycle) |
| 5 | 10 | 5 | $\{1,4,2\}$ $(3,1)$; $\{19,\dots\}$ $(5,3)$; $\{23,\dots\}$ $(5,3)$; $\{187,\dots\}$ $(27,17)$; $\{347,\dots\}$ $(27,17)$ |
| 7 | 6 | 1 | $\{5,11,20,10\}$ $(4,2)$ |
| 9 | 5 | 0 | — (all are $9\times$ a $T_1$-cycle) |
| 11 | 8 | 3 | $\{-19,-23,-29,-38\}$ $(4,3)$; $\{1,7,16,8,4,2\}$ $(6,2)$; $\{13,\dots\}$ $(14,8)$ |
| 13 | 14 | 9 | $\{1,8,4,2\}$ $(4,1)$; **seven** distinct $(8,5)$ cycles through $211,227,251,259,283,287,319$; $\{131,\dots\}$ $(24,15)$ |
| 15 | 10 | 0 | — (all are $3\times$ a $T_5$-cycle or $15\times$ a $T_1$-cycle) |
| 17 | 9 | 4 | $\{-65,\dots\}$ $(6,4)$; $\{-73,\dots\}$ $(6,4)$; $\{1,10,5,16,8,4,2\}$ $(7,2)$; $\{23,\dots\}$ $(31,18)$ |
| 19 | 7 | 2 | $\{5,17,35,62,31,56,28,14,7,20,10\}$ $(11,5)$; $\{-115,\dots\}$ $(17,11)$ |
| 21 | 6 | 0 | — (all are $3\times$ a $T_7$-cycle or $21\times$ a $T_1$-cycle) |

Two features of this table are **proved**, not empirical, and serve as consistency checks
on the census: (i) for $q \in \{3,9,15,21\}$ (i.e. $3 \mid q$) there are no primitive
cycles at all — L-9921.1b(4)(iv); (ii) every $q$ carries the five images
$q\cdot\{0\}$, $q\cdot\{-1\}$, $q\cdot\{1,2\}$, $q\cdot\{-5,-7,-10\}$, $q\cdot\{-17,\dots\}$
of the five $T_1$-cycles whose closure is verified exactly in Test F — L-9921.6
Corollary 2(1). (Claim (ii) does **not** presuppose that those five are *all* the
$T_1$-cycles; that is precisely what is open.) Everything else in the table is a finite
observation about a finite window.

**What the census does not show.** It does not show that $T_q$ has no divergent orbit for
any $q$, not even for $q=1$; "0 escaped starts" means only that no orbit *in the searched
window* left the window before closing. It also does not show that the listed cycles are
all the cycles of $T_q$: a cycle all of whose elements exceed $20000$ in absolute value
would not be seen.

**(b) The ported lower envelope (PROVED).** Let $q$ be positive odd, $a \in \mathbb{Z}^+$,
$k \ge 0$. Lemma A$_q$ (proved below) gives $2^k T_q^k(a) = 3^{a_k} a + q\rho_k$ with
$\rho_k \ge 0$ and $q > 0$, hence
$$T_q^k(a) \;\ge\; \frac{3^{\,a_k}}{2^{\,k}}\,a \;=\; a\cdot 2^{\,a_k \log_2 3 - k}.$$
If $\limsup_k a_k/k > \gamma = \log_3 2$, pick $\varepsilon > 0$ and infinitely many $k$
with $a_k/k \ge \gamma + \varepsilon$; then $a_k \log_2 3 - k \ge
k\big((\gamma+\varepsilon)\log_2 3 - 1\big) = k\,\varepsilon \log_2 3 \to \infty$ along
those $k$ (using $\gamma \log_2 3 = 1$), so $\sup_k T_q^k(a) = \infty$. If
$\liminf_k a_k/k > \gamma$, the same estimate holds for **all** large $k$, so
$T_q^k(a) \to \infty$. (This is L-9907.1 with $q$ inserted; the proof is identical because
$\rho_k \ge 0$ is all that was ever used.) $\blacksquare$

**(c)** Labelled UNVERIFIED, as stated in the Statement section. Not used anywhere in
this file.

**(d)** The verdict is a labelled assessment; its two proved supports are L-9921.4 and
L-9921.6 Corollary 3 / Corollary 4, proved in their places.

### L-9921.6 — the cycle equation

**Lemma A$_q$.** *For all positive odd $q$, $a \in \mathbb{Z}$, $k \ge 0$:*
$2^k T_q^k(a) = 3^{a_k} a + q\rho_k$, *with $\rho_k = \rho(v_0,\dots,v_{k-1}) \ge 0$.*

*Proof.* First, the one-step identity: for every $b \in \mathbb{Z}$ with parity
$v := b \bmod 2$, $2\,T_q(b) = 3^{v} b + v\,q$ (if $v = 0$: $2\cdot(b/2) = b$; if $v=1$:
$2\cdot(3b+q)/2 = 3b+q$). Now induct on $k$. Base $k=0$: $a_0 = 0$, $\rho_0 = 0$, both
sides are $a$. Step: with $v_k = T_q^k(a) \bmod 2$,
$$2^{k+1}T_q^{k+1}(a) = 2^k\cdot 2 T_q\big(T_q^k(a)\big)
= 2^k\big(3^{v_k}T_q^k(a) + v_k q\big)
= 3^{v_k}\big(3^{a_k}a + q\rho_k\big) + v_k q 2^k
= 3^{a_{k+1}}a + q\big(3^{v_k}\rho_k + v_k 2^k\big),$$
and $3^{v_k}\rho_k + v_k 2^k = \rho_{k+1}$ by the defining recursion, while
$a_{k+1} = a_k + v_k$ (D-9906). Non-negativity: $\rho_0 = 0 \ge 0$ and
$\rho_{k+1} = 3^{v_k}\rho_k + v_k2^k \ge 0$ whenever $\rho_k \ge 0$. $\blacksquare$

*(Numerical check on 3000 random $(a,q,k)$ with $k \le 60$, both signs of $a$: Test G.)*

**Proof of L-9921.6.1.** Let $x_1 \to \dots \to x_m \to x_1$ be an $S_q$-cycle, indices
extended $m$-periodically ($x_{i+m} := x_i$, $a_{i+m} := a_i$), so that the step relation
$$2^{a_i}\,x_{i+1} \;=\; 3x_i + q \tag{$*_i$}$$
holds for every integer $i$, with $a_i = \nu_2(3x_i+q) \ge 1$ (well defined because
$3x_i + q \neq 0$ by the domain of $S_q$; and $a_i \ge 1$ because $3x_i$ and $q$ are both
odd, so $3x_i+q$ is even).

Multiply $(*_i)$ by $3^{\,m-i}2^{\,A_{i-1}}$:
$$3^{\,m-i}2^{\,A_{i}}\,x_{i+1} \;=\; 3^{\,m-i+1}2^{\,A_{i-1}}\,x_i
\;+\; q\,3^{\,m-i}2^{\,A_{i-1}}, \qquad 1 \le i \le m,$$
using $A_{i-1} + a_i = A_i$. Put $u_i := 3^{\,m-i+1}2^{\,A_{i-1}}x_i$ for
$1 \le i \le m+1$ (with $x_{m+1} = x_1$ and $A_m = K$). The left side of the $i$-th
equation is $3^{\,m-(i+1)+1}2^{\,A_{(i+1)-1}}x_{i+1} = u_{i+1}$ and the first right-hand
term is $u_i$. Summing over $i = 1, \dots, m$ telescopes:
$$\sum_{i=1}^m u_{i+1} \;=\; \sum_{i=1}^m u_i \;+\; q\sum_{i=1}^m 3^{\,m-i}2^{\,A_{i-1}}
\qquad\Longrightarrow\qquad u_{m+1} - u_1 \;=\; q\,c .$$
Finally $u_{m+1} = 3^{0}2^{A_m}x_{m+1} = 2^K x_1$ and $u_1 = 3^{m}2^{A_0}x_1 = 3^m x_1$
(using $A_0 = 0$). Hence $x_1(2^K - 3^m) = q\,c$. Since each summand of $c$ is a positive
integer, $c \ge m \ge 1$. Anchoring at $x_r$ instead re-indexes the same computation and
yields the same identity with $x_r$ and the corresponding $c_r$; $m$ and $K$ are unchanged
because both sum one full period of an $m$-periodic sequence. $\square$

**$c = \rho(w)$.** Let $w \in \{0,1\}^K$ be the parity word of the $T_q$-orbit of the odd
integer $x_1$, i.e. $w_j = T_q^j(x_1) \bmod 2$ for $0 \le j < K$. One $S_q$-step from
$x_i$ consists of one odd $T_q$-step followed by $a_i - 1$ even $T_q$-steps (because
$2^{a_i}x_{i+1} = 3x_i+q$ with $x_{i+1}$ odd means exactly $a_i$ halvings occur before the
next odd value). Hence the positions $j$ with $w_j = 1$ are precisely
$j \in \{A_0, A_1, \dots, A_{m-1}\}$, and $|w|_1 = m$, $|w| = A_m = K$. For
$j = A_{i-1}$ the number of ones strictly after position $j$ is
$s_j(w) = m - i$. The closed form of L-9903.2 therefore gives
$$\rho(w) \;=\; \sum_{j : w_j = 1} 3^{\,s_j(w)}2^{\,j}
\;=\; \sum_{i=1}^{m} 3^{\,m-i}\,2^{\,A_{i-1}} \;=\; c .$$
Combined with Lemma A$_q$ at $k = K$ (where $T_q^K(x_1) = x_1$ and $a_K = m$), this
re-derives $x_1(2^K - 3^m) = q\rho(w) = qc$ independently. $\square$

*(Numerical check: Test H verifies $x_1(2^K-3^m) = qc$ **and** $\rho(w) = c$ for all 85
cycles met by the census, at all 315 anchorings at odd elements, for every odd
$q \le 21$.)*

**Proof of Corollary 1.** *Lower bound on $c$:* $a_i \ge 1$ and $A_0 = 0$ give
$A_{i-1} \ge i-1$ for $1 \le i \le m$ (induction), hence
$c \ge \sum_{i=1}^m 3^{m-i}2^{i-1} = 3^m - 2^m$ (the geometric identity
$\sum_{i=1}^m 3^{m-i}2^{i-1} = (3^m - 2^m)/(3-2)$), and $3^m - 2^m \ge m$ for $m \ge 1$
(induction: true at $m=1$; $3^{m+1}-2^{m+1} = 3(3^m-2^m) + 2^m \ge 3m + 1 \ge m+1$).
*Product formula:* multiply $(*_i)$ over $i = 1,\dots,m$; all $x_i \ne 0$ (they are odd),
so
$$2^{K}\prod_{i=1}^m x_{i+1} \;=\; \prod_{i=1}^m (3x_i + q)
\;=\; \prod_{i=1}^m x_i\Big(3 + \frac{q}{x_i}\Big),$$
and $\prod_i x_{i+1} = \prod_i x_i \ne 0$ (same multiset), so
$2^K = \prod_i (3 + q/x_i)$. *Positive case:* if all $x_i > 0$ then $c \ge 1 > 0$ and
$x_1 > 0$ force $2^K - 3^m = qc/x_1 > 0$; and each factor satisfies
$3 < 3 + q/x_i \le 3 + q/x_{\min}$, so
$3^m < 2^K \le (3 + q/x_{\min})^m$. Taking $\ln$ and using
$\ln(1+t) \le t$ for $t \ge 0$:
$$0 < K\ln 2 - m\ln 3 \le m\ln\Big(1 + \frac{q}{3x_{\min}}\Big) \le \frac{mq}{3x_{\min}},$$
which upon division by $m\ln 2$ is the displayed bound. The element bound is
$x_1 = qc/(2^K-3^m) \ge q(3^m-2^m)/(2^K-3^m)$. $\square$

**Proof of Corollary 2.**
*(1)* Let $\Gamma$ be a $T$-cycle in $\mathbb{Z}$ of length $L$, i.e. $T^L(\gamma) =
\gamma$ with $L$ least. By L-9921.1b(3) with $d = q$ (and $\tilde q = 1$),
$T_q^k(q\gamma) = q\,T^k(\gamma)$ for all $k$; hence $T_q^L(q\gamma) = q\gamma$, and no
smaller period is possible (a period $L' < L$ for $q\gamma$ would give
$q T^{L'}(\gamma) = q\gamma$, so $T^{L'}(\gamma) = \gamma$). Parity words agree because
$q\,T^k(\gamma) \equiv T^k(\gamma) \pmod 2$ ($q$ odd).
*(2)* ($\Leftarrow$) If $q \mid x$ for some $x \in \Delta$ then, $\gcd(\cdot,q)$ being
constant on $\Delta$ (L-9921.1b(1)) and equal to $q$, every element is divisible by $q$;
put $\Gamma := \Delta/q$. By L-9921.1b(3) with $d=q$, $T(y) = T_q(qy)/q$ for
$y \in \Gamma$, so $\Gamma$ is a $T$-cycle in $\mathbb{Z}$ and $\Delta = q\Gamma$.
($\Rightarrow$) immediate.
*(3)* $T_5(1) = (3+5)/2 = 4$, $T_5(4) = 2$, $T_5(2) = 1$, and $1,4,2$ are distinct: so
$\{1,4,2\}$ is a $T_5$-cycle of length $3$. Its elements are not all divisible by $5$
(indeed none is), so by (2) it is **not** $5$ times an integer $T$-cycle. The bijection
statement is L-9921.1(4): $\mu_q^{-1} = (x \mapsto x/q)$ conjugates $T_q$ to
$T|_{\Lambda_q}$, and a conjugacy by a bijection carries cycles to cycles of the same
length, bijectively, in both directions. Applying it, $\{1,4,2\}/5 = \{1/5,4/5,2/5\}$ is
a $T$-cycle in $\Lambda_5$ — exactly L-9904.6 item 5, where $1/5 \to 4/5 \to 2/5 \to 1/5$
is computed independently in $\mathbb{Z}_2$.
*(4)* Let $d := \gcd(x,q)$, constant on $\Delta$ by L-9921.1b(1); $d \mid q$ and $d$ is
odd. Every $x \in \Delta$ is divisible by $d$, and by L-9921.1b(3),
$T_{q/d}(x/d) = T_q(x)/d$, so $\Delta' := \Delta/d$ is a $T_{q/d}$-cycle of the same
length. For $x \in \Delta$, $\gcd(x/d, q/d) = \gcd(x,q)/d = d/d = 1$ (the identity
$\gcd(u/d, v/d) = \gcd(u,v)/d$ holds whenever $d \mid \gcd(u,v)$). So $\Delta'$ is
primitive. Item 2 is the case $d = q$. $\square$

**Proof of Corollary 3.** Let $w \in \{0,1\}^K$, $K \ge 1$, $a := |w|_1$,
$D := 2^K - 3^a$, $\rho_w := \rho(w)$. $D$ is odd (as $2^K$ is even and $3^a$ is odd),
hence $D \ne 0$; so $g := \gcd(|D|,\rho_w) \ge 1$ and $q_w := |D|/g$ is a positive odd
integer (a divisor of the odd number $|D|$).

By L-9904.5(i) there is exactly one $z \in \mathbb{Z}_2$ with parity word $w^\infty$, and
by L-9904.5(ii) it satisfies $T^K(z) = z$ and $z = \rho_w/D \in \mathbb{Q}$.

*The divisibility criterion.* Write $D' := |D|/g = q_w$ and $\rho' := \rho_w/g$, so that
$|D| = gD'$, $\rho_w = g\rho'$ and $\gcd(D',\rho') = 1$. For every positive odd $q$,
since divisibility is insensitive to the sign of $D$ and $g \ge 1$,
$$D \mid q\rho_w \iff |D| \mid q\rho_w \iff gD' \mid q\,g\,\rho' \iff D' \mid q\rho'
\iff D' \mid q \iff q_w \mid q ,$$
the fourth equivalence by Gauss's lemma applied to $\gcd(D', \rho') = 1$. (Degenerate
case $\rho_w = 0$: then $g = |D|$, $D' = q_w = 1$, $\rho' = 0$, and both sides of every
equivalence hold for every $q$.)

($\Leftarrow$) Suppose $q_w \mid q$ with $q$ positive odd. By the criterion,
$x := q\rho_w/D \in \mathbb{Z}$.
Now $x = qz$, so $x/q = z \in \Lambda_q$ and by L-9921.1(4),
$T_q^K(x) = q\,T^K(z) = qz = x$, and the $T_q$-parity word of $x$ equals the $T$-parity
word of $z$, namely $w^\infty$ (L-9921.1(4), last clause).

($\Rightarrow$) Suppose $x \in \mathbb{Z}$ has $T_q^K(x) = x$ and $T_q$-parity word
$w^\infty$. Then $y := x/q \in \Lambda_q \subseteq \mathbb{Z}_2$ has $T^K(y) = y$ and
$T$-parity word $w^\infty$ (L-9921.1(4)); by the uniqueness in L-9904.5(i), $y = z =
\rho_w/D$, so $x = q\rho_w/D \in \mathbb{Z}$, i.e. $D \mid q\rho_w$, i.e. $q_w \mid q$ by
the displayed chain of equivalences. This also proves uniqueness of $x$. Taking $q :=
q_w$ shows every $w$ is realized for some positive odd $q$. $\square$

*(Numerical check: Test I verifies all 2046 words with $1 \le K \le 10$ — integrality of
$x$, $T_{q_w}^K(x) = x$, parity word $w^\infty$ over $2K$ steps — and, for $K \le 7$,
the divisibility criterion "$q\rho_w/D \in \mathbb{Z} \iff q_w \mid q$" for every odd
$q \le 2001$.)*

**Proof of Corollary 4.** Immediate from Corollary 1: the two displayed bounds carry the
factor $q$ explicitly. Combined with Corollary 3 (for every word $w$ there is a $q$ with
an integer $T_q$-cycle of that word), no statement of the form "for all positive odd $q$,
$T_q$ has no cycle with property $P$" can hold when $P$ is satisfied by some word. $\square$

---

## Dependency audit

| Dependency | Status | Precise point of use |
|---|---|---|
| NOTATION.md D-9902 (shortcut $T$) | canonical | D-9921.1 ($T_1 = T$); L-9921.4(1),(2). |
| NOTATION.md D-9906 ($v_i$, $a_k$) | canonical | L-9921.1(4) (parity vectors agree); Lemma A$_q$ ($a_{k+1} = a_k + v_k$); L-9921.5(b). |
| NOTATION.md D-9907 (bounded/divergent) | canonical | D-9921.2 (extended to absolute value); L-9921.2; L-9921.5(b). |
| NOTATION.md D-9908 (cycles, $m$, $a_i$, $A_i$, $K$) | canonical | L-9921.6.1 and its corollaries. |
| NOTATION.md D-9909, conventions | canonical | L-9921.4 ("Collatz counterexample"); empty sums in $c$, $\rho$. |
| L-9904 B7 ($\mathbb{Q}\cap\mathbb{Z}_2 = \mathbb{Z}_{(2)}$; parity of $p/q$) | PROVED | P0.2; L-9921.1(1),(2); L-9921.3 (B)$\Rightarrow$(A). |
| L-9904 B2, B3 (division by 2 unique; odd = unit, $q^{-1}$ odd) | PROVED | L-9921.1(2) proof; L-9921.1(3) proof. |
| L-9904 P0, L-9904.1 ($T$ well defined on $\mathbb{Z}_2$, restricts to D-9902) | PROVED | throughout; L-9921.4(1). |
| L-9904.5(i) (unique realizer of a word) | PROVED | Corollary 3 (uniqueness, both directions). |
| L-9904.5(ii) ($z = \rho_w/(2^K-3^a)$, $T^K z = z$) | PROVED | Corollary 3. |
| L-9904.5(iii)(3b) (orbit ev. periodic $\iff$ word ev. periodic) | PROVED | closing remark of L-9921.3 only. |
| L-9904.6 item 5 ($1/5 \to 4/5 \to 2/5$) | PROVED | cross-check in Corollary 2(3); not load-bearing. |
| L-9904 Q-9904 (statement) | OPEN QUESTION | the object of L-9921.3(A); never assumed. |
| L-9901.2(iii), L-9901.4 | PROVED | **only** in L-9921.4(2) (the $C$/$T$ transfer). |
| L-9901.5 | PROVED | only to phrase "the divergence half" in L-9921.4(2). |
| L-9901 boxed pigeonhole remark | PROVED file, informal remark | discussed and sharpened in the box after L-9921.2; not used in any proof. |
| L-9907.3 + BOXED CAVEAT | PROVED | the (P1)/(P2) formulation reused in L-9921.2 Step 3 and the following Remark; L-9907 already recorded the single-orbit positive-rational case, which L-9921.2 generalizes. |
| L-9907.1 | PROVED | model for L-9921.5(b), which is re-proved from Lemma A$_q$ rather than imported. |
| L-9903.2 (word constant $\rho$, closed form) | PROVED | the closed form is used once, in "$c = \rho(w)$"; the recursion and $\rho \ge 0$ are re-derived inline (Lemma A$_q$). |
| L-9905.1 (cycle equation, $q=1$) | PROVED | the statement being ported; its **proof is re-derived from scratch** in L-9921.6.1, so no logical dependence. |
| L-9905.4 ($c$-bounds), L-9905.3 (product formula), L-9905.5 | PROVED | Corollary 1 re-derives the $q$-analogues from scratch; L-9905 is cited for the $q=1$ comparison only. |

**No circularity.** None of L-9901, L-9903, L-9904, L-9905, L-9907 cites L-9921 (this
file is new). No proof here uses Q-9904 or any statement equivalent to the Collatz
conjecture as a hypothesis: L-9921.3 states an equivalence between two open statements
and asserts neither.

---

## Gap audit

- **Hidden finiteness assumptions.** The only finiteness used is (P2):
  $\Lambda_q \cap [-B,B]$ is finite. It is proved (L-9921.2 Step 1) with an exact count,
  not assumed, and the box after L-9921.2 states explicitly that it *fails* for the
  ambient set $\mathbb{Z}_{(2)}$ — which is exactly why the correct ambient set had to be
  identified. The census of L-9921.5(a) is finite and is labelled EMPIRICAL in the
  Statement, in the Scope line, in the section itself, and in the script header; no proof
  cites it.
- **Extrapolating a finite computation to infinite behaviour.** Deliberately guarded:
  L-9921.5(a) states in its own words that "$0$ escaped starts" carries no information
  about divergence, and that unseen cycles with all elements $> 20000$ in absolute value
  would be missed. Two entries of the census table are cross-checked against *proved*
  statements (no primitive cycles when $3 \mid q$; the five $q$-scaled $T_1$-cycles always
  present) precisely so that a census bug would show up as a contradiction.
- **Unjustified induction.** Every induction has an explicit base and step: iteration of
  the conjugacy (base $k=0$); Lemma A$_q$ (base $k=0$); $A_{i-1} \ge i-1$;
  $3^m - 2^m \ge m$; the strong induction in Lemma R, whose well-foundedness is argued
  explicitly (each recursive call strictly decreases the positive integer $q$, and $q=1$
  is terminal).
- **Boundary cases.** $a = 0$: $T_q(0) = 0$, the orbit is a cycle, not divergent — used
  explicitly in Lemma R Case 2 and in L-9921.1b(4)(iii). $q = 1$: $\Lambda_1 = \mathbb{Z}$,
  $T_1 = T$, $\gcd(a,1)=1$ — the terminal case of Lemma R and the subject of L-9921.4.
  $m = 0$ in a $T_q$-cycle (the cycle $\{0\}$, which has no odd element): the $S_q$-form
  of L-9921.6.1 does not apply, and it is excluded there by hypothesis (an $S_q$-cycle
  consists of odd integers); the $T_q$-form via Lemma A$_q$ still holds and reads
  $0\cdot(2^K-1) = q\cdot 0$. This case is handled separately in Test H.
  $3x_i + q = 0$: excluded from the domain of $S_q$; such a point maps to $0$ under $T_q$
  and hence is not on any cycle (its forward orbit is constantly $0$, while a cycle
  element is odd). $\rho_w = 0$ (i.e. $w = 0^K$) in Corollary 3: then
  $g = \gcd(|D|,0) = |D|$ and $q_w = 1$, giving $x = 0$ for every $q$ — consistent,
  and covered by Test I. $B$ non-integral in (P2): handled by the floor in the count.
- **Confusion between empirical and universal statements.** L-9921.5(a) and (c) are
  labelled; (b) and (d) are separated, (b) proved and (d) explicitly marked a subjective
  assessment. No numbered claim rests on a computation.
- **Invalid interchange of limits.** No limits are interchanged. The only limit
  statements are $|y_k| \to \infty$ (used through its negation, an $\varepsilon$-free
  quantifier statement) and the $\limsup/\liminf$ comparisons of L-9921.5(b), which are
  applied along a subsequence (for $\limsup$) or eventually (for $\liminf$) — stated
  separately for exactly that reason.
- **Nonuniform estimates.** Corollary 1's bounds carry $q$ explicitly, and Corollary 4
  states the non-uniformity as a conclusion rather than hiding it. L-9921.5(b) is uniform
  in $a$ but not in $q$ in the sense that no $q$-free statement is made. L-9921.5(c) is
  flagged as an unverified port precisely because its constants' dependence on $q$ has
  not been checked.
- **Circular dependence.** None; see the audit table. Q-9904 is quantified as a statement
  in an equivalence, never assumed.
- **Assumptions equivalent to the Collatz conjecture.** None assumed. L-9921.4 *proves* a
  containment in the other direction (Q-9904 $\Rightarrow$ Collatz-divergence-half) and
  states in the same breath that no converse is claimed.
- **Incorrectly assumed independence.** The seven $(8,5)$-cycles for $q = 13$ and other
  census data are not treated as independent samples of anything; no probabilistic claim
  is made anywhere in this file.
- **Failure to prove a symbolic object is an actual integer.** This is the exact content
  of Corollary 3, which *proves* integrality of $x = q\rho_w/D$ under the stated
  divisibility criterion rather than assuming it — and note that it does so for a
  *chosen* $q$, which is precisely why it does **not** dent L-9904.7: for $q = 1$ the
  criterion $q_w \mid 1$ is a hard Diophantine condition on $w$, and this file supplies
  no way to satisfy it.
- **A corrected statement in the task sketch, recorded.** The task sketch described the
  domain as "rationals $x = a/q$ **in lowest terms**". That description is too narrow: the
  correct object is $\Lambda_q = \tfrac1q\mathbb{Z}$, i.e. rationals with lowest-terms
  denominator *dividing* $q$, and the coprimality of $a$ and $q$ is neither assumed nor
  preserved (L-9921.1b(1),(2): the gcd can strictly increase, e.g. $1/3 \mapsto 1$). The
  sketch itself flagged this ("gcd may change — handle it"), and L-9921.1(2) proves that
  the parity dictionary needs no coprimality at all. The sketch's remaining assertions
  were verified as stated.
- **A second correction, recorded.** The task sketch says the orbits "diverge in absolute
  value"; this wording is necessary and not cosmetic, because $T_q$ does **not** preserve
  sign for $q > 1$ ($T_5(-1) = 1$, $T_{11}(-3) = 1$: Test M). Only $T_1$ preserves sign.
  Every statement above is phrased with $|\cdot|$ accordingly.

---

## Adversarial tests

**Finite verification only — not proof.** All arithmetic is exact (Python integers and
`fractions.Fraction` restricted to odd denominators, i.e. elements of
$\mathbb{Z}_{(2)} \subset \mathbb{Z}_2$). Two scripts, in
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/`:
`cycles_L9921.py` (the census; also imported as a module by the second script) and
`verify_L9921.py` (tests A–N). Python 3.11, stdlib only, fixed seed `99212026`; total
runtime under 1 s each. Both are reproduced in full below with their verbatim output.

### Script 1 — `cycles_L9921.py` (census)

```python
#!/usr/bin/env python3
# Empirical cycle census for the shortcut 3x+q map T_q on Z (L-9921.5).
# Agent: fable-02-p15. Date: 2026-07-25.  Exact integer arithmetic only (Python ints).
#
#   T_q(a) = a/2            if a is even
#            (3a+q)/2       if a is odd          (3a+q is even since 3a, q are odd)
#
# For every positive odd q <= QMAX we walk the T_q-orbit of every start a with
# |a| <= NSTART, memoising resolved values, and record:
#   * every cycle met (as a canonical sorted tuple),
#   * the number of starts that escaped the search window (|value| > BIG) or
#     exceeded STEPS iterations without resolving -- these are INCONCLUSIVE,
#     not evidence of divergence.
# EMPIRICAL ONLY: a finite search can never certify absence of divergent orbits.

from math import gcd

QMAX = 21
NSTART = 20000
BIG = 10 ** 15
STEPS = 100000


def Tq(a, q):
    return a // 2 if a % 2 == 0 else (3 * a + q) // 2


def census(q, nstart=NSTART, big=BIG, steps=STEPS):
    """Return (cycles, n_escaped, n_stepcap). cycles: list of canonical tuples."""
    cycles = []            # list of frozensets
    label = {}             # value -> index into cycles, or -1 for 'unresolved'
    n_escaped = 0
    n_stepcap = 0
    for a0 in range(-nstart, nstart + 1):
        if a0 in label:
            continue
        path = []
        pos = {}
        a = a0
        outcome = None
        for t in range(steps):
            if a in label:
                outcome = label[a]
                break
            if a in pos:
                cyc = frozenset(path[pos[a]:])
                cycles.append(cyc)
                outcome = len(cycles) - 1
                break
            if abs(a) > big:
                outcome = -1
                break
            pos[a] = len(path)
            path.append(a)
            a = Tq(a, q)
        if outcome is None:
            outcome = -1
            n_stepcap += 1
        elif outcome == -1:
            n_escaped += 1
        for v in path:
            label[v] = outcome
    canon = []
    for c in cycles:
        s = sorted(c)
        canon.append(tuple(s))
    canon.sort(key=lambda t: (len(t), t))
    return canon, n_escaped, n_stepcap


def cycle_report(c, q):
    """Descriptive data for a T_q-cycle given as a sorted tuple:
       K = length, m = number of odd elements, d = gcd(x, q) (constant on the cycle)."""
    K = len(c)
    m = sum(1 for x in c if x % 2 == 1)
    d = 0
    for x in c:
        d = gcd(d, x)
    d = gcd(d, q)
    return K, m, d


def main():
    print(f"Shortcut 3x+q map T_q on Z: cycle census, odd q <= {QMAX},")
    print(f"starts |a| <= {NSTART}, escape window |value| <= 10^{len(str(BIG))-1}, step cap {STEPS}.")
    print("EMPIRICAL / FINITE SEARCH ONLY.")
    print()
    tot_esc = tot_step = 0
    for q in range(1, QMAX + 1, 2):
        cyc, nesc, nstep = census(q)
        tot_esc += nesc
        tot_step += nstep
        nprim = sum(1 for c in cyc if cycle_report(c, q)[2] == 1)
        print(f"q = {q}:  {len(cyc)} cycle(s) found ({nprim} primitive); "
              f"escaped-window starts: {nesc}; step-cap starts: {nstep}")
        for c in cyc:
            K, m, d = cycle_report(c, q)
            tag = "primitive" if d == 1 else f"= {d} x (a T_{q // d}-cycle)"
            start = min(c, key=lambda x: (abs(x), x))   # anchor at the element of least |.|
            orb = [start]
            while True:
                nxt = Tq(orb[-1], q)
                if nxt == start:
                    break
                orb.append(nxt)
            head = f"    K={K:2d} m={m:2d} {tag:22s} "
            for r in range(0, len(orb), 12):
                print(head + " ".join(f"{x}" for x in orb[r:r + 12]))
                head = " " * len(head)
        print()
    print(f"TOTALS over all odd q <= {QMAX}: escaped-window starts {tot_esc}, step-cap starts {tot_step}.")
    print("No searched orbit left the window; this is NOT evidence about divergence in general.")


if __name__ == "__main__":
    main()
```

**Output of `python3 cycles_L9921.py` (verbatim, single run, 2026-07-25, CPython 3.11,
Linux; runtime 0.27 s):**

```text
Shortcut 3x+q map T_q on Z: cycle census, odd q <= 21,
starts |a| <= 20000, escape window |value| <= 10^15, step cap 100000.
EMPIRICAL / FINITE SEARCH ONLY.

q = 1:  5 cycle(s) found (5 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 primitive              -1
    K= 1 m= 0 primitive              0
    K= 2 m= 1 primitive              1 2
    K= 3 m= 2 primitive              -5 -7 -10
    K=11 m= 7 primitive              -17 -25 -37 -55 -82 -41 -61 -91 -136 -68 -34

q = 3:  5 cycle(s) found (0 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 3 x (a T_1-cycle)    -3
    K= 1 m= 0 = 3 x (a T_1-cycle)    0
    K= 2 m= 1 = 3 x (a T_1-cycle)    3 6
    K= 3 m= 2 = 3 x (a T_1-cycle)    -15 -21 -30
    K=11 m= 7 = 3 x (a T_1-cycle)    -51 -75 -111 -165 -246 -123 -183 -273 -408 -204 -102

q = 5:  10 cycle(s) found (5 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 5 x (a T_1-cycle)    -5
    K= 1 m= 0 = 5 x (a T_1-cycle)    0
    K= 2 m= 1 = 5 x (a T_1-cycle)    5 10
    K= 3 m= 2 = 5 x (a T_1-cycle)    -25 -35 -50
    K= 3 m= 1 primitive              1 4 2
    K= 5 m= 3 primitive              19 31 49 76 38
    K= 5 m= 3 primitive              23 37 58 29 46
    K=11 m= 7 = 5 x (a T_1-cycle)    -85 -125 -185 -275 -410 -205 -305 -455 -680 -340 -170
    K=27 m=17 primitive              187 283 427 643 967 1453 2182 1091 1639 2461 3694 1847
                                     2773 4162 2081 3124 1562 781 1174 587 883 1327 1993 2992
                                     1496 748 374
    K=27 m=17 primitive              347 523 787 1183 1777 2668 1334 667 1003 1507 2263 3397
                                     5098 2549 3826 1913 2872 1436 718 359 541 814 407 613
                                     922 461 694

q = 7:  6 cycle(s) found (1 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 7 x (a T_1-cycle)    -7
    K= 1 m= 0 = 7 x (a T_1-cycle)    0
    K= 2 m= 1 = 7 x (a T_1-cycle)    7 14
    K= 3 m= 2 = 7 x (a T_1-cycle)    -35 -49 -70
    K= 4 m= 2 primitive              5 11 20 10
    K=11 m= 7 = 7 x (a T_1-cycle)    -119 -175 -259 -385 -574 -287 -427 -637 -952 -476 -238

q = 9:  5 cycle(s) found (0 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 9 x (a T_1-cycle)    -9
    K= 1 m= 0 = 9 x (a T_1-cycle)    0
    K= 2 m= 1 = 9 x (a T_1-cycle)    9 18
    K= 3 m= 2 = 9 x (a T_1-cycle)    -45 -63 -90
    K=11 m= 7 = 9 x (a T_1-cycle)    -153 -225 -333 -495 -738 -369 -549 -819 -1224 -612 -306

q = 11:  8 cycle(s) found (3 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 11 x (a T_1-cycle)   -11
    K= 1 m= 0 = 11 x (a T_1-cycle)   0
    K= 2 m= 1 = 11 x (a T_1-cycle)   11 22
    K= 3 m= 2 = 11 x (a T_1-cycle)   -55 -77 -110
    K= 4 m= 3 primitive              -19 -23 -29 -38
    K= 6 m= 2 primitive              1 7 16 8 4 2
    K=11 m= 7 = 11 x (a T_1-cycle)   -187 -275 -407 -605 -902 -451 -671 -1001 -1496 -748 -374
    K=14 m= 8 primitive              13 25 43 70 35 58 29 49 79 124 62 31
                                     52 26

q = 13:  14 cycle(s) found (9 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 13 x (a T_1-cycle)   -13
    K= 1 m= 0 = 13 x (a T_1-cycle)   0
    K= 2 m= 1 = 13 x (a T_1-cycle)   13 26
    K= 3 m= 2 = 13 x (a T_1-cycle)   -65 -91 -130
    K= 4 m= 1 primitive              1 8 4 2
    K= 8 m= 5 primitive              211 323 491 743 1121 1688 844 422
    K= 8 m= 5 primitive              227 347 527 797 1202 601 908 454
    K= 8 m= 5 primitive              251 383 581 878 439 665 1004 502
    K= 8 m= 5 primitive              259 395 599 905 1364 682 341 518
    K= 8 m= 5 primitive              283 431 653 986 493 746 373 566
    K= 8 m= 5 primitive              287 437 662 331 503 761 1148 574
    K= 8 m= 5 primitive              319 485 734 367 557 842 421 638
    K=11 m= 7 = 13 x (a T_1-cycle)   -221 -325 -481 -715 -1066 -533 -793 -1183 -1768 -884 -442
    K=24 m=15 primitive              131 203 311 473 716 358 179 275 419 635 959 1445
                                     2174 1087 1637 2462 1231 1853 2786 1393 2096 1048 524 262

q = 15:  10 cycle(s) found (0 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 15 x (a T_1-cycle)   -15
    K= 1 m= 0 = 15 x (a T_1-cycle)   0
    K= 2 m= 1 = 15 x (a T_1-cycle)   15 30
    K= 3 m= 2 = 15 x (a T_1-cycle)   -75 -105 -150
    K= 3 m= 1 = 3 x (a T_5-cycle)    3 12 6
    K= 5 m= 3 = 3 x (a T_5-cycle)    57 93 147 228 114
    K= 5 m= 3 = 3 x (a T_5-cycle)    69 111 174 87 138
    K=11 m= 7 = 15 x (a T_1-cycle)   -255 -375 -555 -825 -1230 -615 -915 -1365 -2040 -1020 -510
    K=27 m=17 = 3 x (a T_5-cycle)    561 849 1281 1929 2901 4359 6546 3273 4917 7383 11082 5541
                                     8319 12486 6243 9372 4686 2343 3522 1761 2649 3981 5979 8976
                                     4488 2244 1122
    K=27 m=17 = 3 x (a T_5-cycle)    1041 1569 2361 3549 5331 8004 4002 2001 3009 4521 6789 10191
                                     15294 7647 11478 5739 8616 4308 2154 1077 1623 2442 1221 1839
                                     2766 1383 2082

q = 17:  9 cycle(s) found (4 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 17 x (a T_1-cycle)   -17
    K= 1 m= 0 = 17 x (a T_1-cycle)   0
    K= 2 m= 1 = 17 x (a T_1-cycle)   17 34
    K= 3 m= 2 = 17 x (a T_1-cycle)   -85 -119 -170
    K= 6 m= 4 primitive              -65 -89 -125 -179 -260 -130
    K= 6 m= 4 primitive              -73 -101 -143 -206 -103 -146
    K= 7 m= 2 primitive              1 10 5 16 8 4 2
    K=11 m= 7 = 17 x (a T_1-cycle)   -289 -425 -629 -935 -1394 -697 -1037 -1547 -2312 -1156 -578
    K=31 m=18 primitive              23 43 73 118 59 97 154 77 124 62 31 55
                                     91 145 226 113 178 89 142 71 115 181 280 140
                                     70 35 61 100 50 25 46

q = 19:  7 cycle(s) found (2 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 19 x (a T_1-cycle)   -19
    K= 1 m= 0 = 19 x (a T_1-cycle)   0
    K= 2 m= 1 = 19 x (a T_1-cycle)   19 38
    K= 3 m= 2 = 19 x (a T_1-cycle)   -95 -133 -190
    K=11 m= 7 = 19 x (a T_1-cycle)   -323 -475 -703 -1045 -1558 -779 -1159 -1729 -2584 -1292 -646
    K=11 m= 5 primitive              5 17 35 62 31 56 28 14 7 20 10
    K=17 m=11 primitive              -115 -163 -235 -343 -505 -748 -374 -187 -271 -397 -586 -293
                                     -430 -215 -313 -460 -230

q = 21:  6 cycle(s) found (0 primitive); escaped-window starts: 0; step-cap starts: 0
    K= 1 m= 1 = 21 x (a T_1-cycle)   -21
    K= 1 m= 0 = 21 x (a T_1-cycle)   0
    K= 2 m= 1 = 21 x (a T_1-cycle)   21 42
    K= 3 m= 2 = 21 x (a T_1-cycle)   -105 -147 -210
    K= 4 m= 2 = 3 x (a T_7-cycle)    15 33 60 30
    K=11 m= 7 = 21 x (a T_1-cycle)   -357 -525 -777 -1155 -1722 -861 -1281 -1911 -2856 -1428 -714

TOTALS over all odd q <= 21: escaped-window starts 0, step-cap starts 0.
No searched orbit left the window; this is NOT evidence about divergence in general.
```

### Script 2 — `verify_L9921.py` (tests A–N)

```python
#!/usr/bin/env python3
# Adversarial finite verification for L-9921 (rational T-orbits <-> the shortcut 3x+q map).
# Agent: fable-02-p15. Date: 2026-07-25.
# EXACT arithmetic only: Python ints and fractions.Fraction restricted to odd denominators
# (= Z_(2) = Q cap Z_2). 2-adic parity of x = a/q (q odd) is read as a mod 2 (L-9904 B7),
# which Test A verifies independently against the 2-adic definition x mod 2Z_2.
#
# Tests:
#  A. parity dictionary: for q odd, a/q is 2-adically odd  <=>  a is odd.  The 2-adic
#     side is computed independently as the 0-th 2-adic digit of a * q^{-1}, using the
#     inverse of q modulo 2^64 (which agrees with the 2-adic inverse to 64 digits).
#  B. conjugacy L-9921.1: T(a/q) = T_q(a)/q, and T^k(a/q) = T_q^k(a)/q for k up to 200,
#     over both signs of a and many odd q; orbit stays in (1/q)Z (denominator divides q)
#  C. gcd monotonicity: gcd(a,q) | gcd(T_q(a),q); lowest-terms denominator of T^k(a/q)
#     divides q and is non-increasing (divides its predecessor); it can strictly drop
#  D. scaling lemma: for d | q (d odd), T_q(d*b) = d*T_{q/d}(b)
#  E. 3|q reduction: for a odd, T_q(a) in 3Z when 3|q; every orbit reaches 3Z
#  F. the T_1 = T cycles through 0, 1, -1, -5, -17 (exact, closed, least periods)
#  G. Lemma A_q: 2^k T_q^k(a) = 3^{a_k} a + q rho_k, exactly, random (a, q, k)
#  H. cycle equation L-9921.6: x_1(2^K - 3^m) = q c for EVERY cycle found by the census
#     for every odd q <= 21, anchored at EVERY odd cycle element; and rho_w = c
#  I. realization: for every word w with 1 <= K <= 10, with D = 2^K - 3^a, g = gcd(|D|,rho_w),
#     q0 = |D|/g: q0 is odd, x_1 = q0 rho_w / D is an integer, T_{q0}^K(x_1) = x_1 with
#     parity word w^infty; and for odd q <= 2001, q rho_w/D is an integer iff q0 | q
#  J. the correspondence trap: {1,4,2} is a T_5-cycle but 1/5 is NOT an integer, so a
#     3x+q cycle need NOT be q times an integer 3x+1 cycle; {1/5,4/5,2/5} IS a rational
#     T-cycle (matches L-9904.6 item 5)
#  K. finiteness of (1/q)Z cap [-B,B] (the pigeonhole hypothesis of L-9921.2)
#  L. trichotomy shadow: random rationals a/q resolve to cycles, values stay in (1/q)Z
#  M. sign is NOT preserved by T_q for q > 1 (so "diverges" must mean |.| -> infinity)
#  N. lower envelope L-9921.5(b): T_q^k(a) >= 3^{a_k} a / 2^k for a > 0

from fractions import Fraction
from itertools import product
from math import gcd
import random

from cycles_L9921 import census, Tq, QMAX

random.seed(99212026)


def T(x):
    """The 2-adic shortcut map on Z_(2) = Q cap Z_2, parity read 2-adically."""
    if isinstance(x, int):
        return x // 2 if x % 2 == 0 else (3 * x + 1) // 2
    assert x.denominator % 2 == 1, x
    p = x.numerator % 2                      # B7: parity of p/q (q odd) is parity of p
    y = x / 2 if p == 0 else (3 * x + 1) / 2
    assert y.denominator % 2 == 1, x
    return y


def rho_rec(w):
    r = 0
    for i, wi in enumerate(w):
        r = (3 ** wi) * r + wi * (2 ** i)
    return r


def word_q(a, q, k):
    w = []
    for _ in range(k):
        w.append(a % 2)
        a = Tq(a, q)
    return tuple(w)


def rand_odd_q(hi=999):
    return 2 * random.randint(0, (hi - 1) // 2) + 1


# ---------------- A. parity dictionary ----------------
MOD = 2 ** 64
nA = 0
for _ in range(5000):
    q = rand_odd_q()
    a = random.randint(-10 ** 12, 10 ** 12)
    x = Fraction(a, q)
    # intrinsic 2-adic parity: the 0-th 2-adic digit of a*q^{-1}, computed mod 2^64
    intrinsic = (a * pow(q, -1, MOD)) % 2
    assert intrinsic == a % 2 == x.numerator % 2, (a, q)
    nA += 1
print(f"A: 2-adic parity of a/q equals a mod 2 for {nA} random (a,q), q odd, a of both signs")
print("   (checked against the intrinsic digit of a*q^{-1} mod 2^64, and against lowest terms).")

# ---------------- B. conjugacy ----------------
nB = 0
maxk = 0
for _ in range(600):
    q = rand_odd_q()
    a = random.randint(-10 ** 9, 10 ** 9)
    k = random.randint(0, 200)
    x = Fraction(a, q)
    aa = a
    for i in range(k):
        # one-step identity
        assert T(x) == Fraction(Tq(aa, q), q), (a, q, i)
        x, aa = T(x), Tq(aa, q)
        # orbit stays in (1/q)Z  <=>  lowest-terms denominator divides q
        assert q % x.denominator == 0, (a, q, i)
        assert Fraction(aa, q) == x, (a, q, i)
    assert x == Fraction(aa, q)
    maxk = max(maxk, k)
    nB += 1
print(f"B: T^k(a/q) = T_q^k(a)/q verified stepwise on {nB} random (a,q) with k up to {maxk};")
print("   every iterate lies in (1/q)Z (lowest-terms denominator divides q).")

# ---------------- C. gcd monotonicity / denominator drop ----------------
drops = 0
for _ in range(3000):
    q = rand_odd_q()
    a = random.randint(-10 ** 8, 10 ** 8)
    d0 = gcd(a, q)
    b = Tq(a, q)
    d1 = gcd(b, q)
    assert d1 % d0 == 0, (a, q, d0, d1)          # gcd(a,q) divides gcd(T_q(a),q)
    den0 = Fraction(a, q).denominator
    den1 = Fraction(b, q).denominator
    assert den0 % den1 == 0, (a, q)              # denominator divides its predecessor
    if den1 < den0:
        drops += 1
assert gcd(Tq(1, 3), 3) == 3 and gcd(1, 3) == 1  # explicit strict increase of the gcd
assert Fraction(1, 3).denominator == 3 and T(Fraction(1, 3)) == 1
print(f"C: gcd(a,q) | gcd(T_q(a),q) on 3000 random pairs; the lowest-terms denominator divides")
print(f"   its predecessor and strictly dropped in {drops} of them; explicit drop 1/3 -> 1.")

# ---------------- D. scaling lemma ----------------
nD = 0
for _ in range(3000):
    qt = rand_odd_q(199)
    d = rand_odd_q(199)
    q = d * qt
    b = random.randint(-10 ** 7, 10 ** 7)
    assert Tq(d * b, q) == d * Tq(b, qt), (d, qt, b)
    nD += 1
print(f"D: scaling lemma T_q(d*b) = d*T_(q/d)(b) for d | q verified on {nD} random (d, q/d, b).")

# ---------------- E. 3 | q reduction ----------------
nE = 0
for _ in range(2000):
    qt = rand_odd_q(333)
    q = 3 * qt
    a = random.randint(-10 ** 7, 10 ** 7)
    if a % 2 == 1:
        assert Tq(a, q) % 3 == 0, (a, q)
    # every orbit reaches 3Z (or is the constant orbit at 0)
    x = a
    for t in range(200):
        if x % 3 == 0:
            break
        x = Tq(x, q)
    else:
        raise AssertionError((a, q))
    nE += 1
print(f"E: for 3|q and a odd, T_q(a) in 3Z; every one of {nE} random orbits reached 3Z within 200 steps.")

# ---------------- F. the T_1 cycles ----------------
known = {
    0: [0],
    1: [1, 2],
    -1: [-1],
    -5: [-5, -7, -10],
    -17: [-17, -25, -37, -55, -82, -41, -61, -91, -136, -68, -34],
}
for s, expected in known.items():
    orb = [s]
    while True:
        nxt = Tq(orb[-1], 1)
        if nxt == s:
            break
        orb.append(nxt)
        assert len(orb) < 1000, s
    assert orb == expected, (s, orb, expected)
    assert len(set(orb)) == len(orb), s            # least period = length
    assert Tq(orb[-1], 1) == orb[0], s
print("F: T_1 = T cycles verified exactly and closed, with least periods:")
for s, e in known.items():
    print(f"   {s:>4}: length {len(e):2d}  {e}")

# ---------------- G. Lemma A_q ----------------
nG = 0
for _ in range(3000):
    q = rand_odd_q()
    a = random.randint(-10 ** 9, 10 ** 9)
    k = random.randint(0, 60)
    w = word_q(a, q, k)
    x = a
    for _ in range(k):
        x = Tq(x, q)
    assert 2 ** k * x == 3 ** sum(w) * a + q * rho_rec(w), (a, q, k)
    nG += 1
print(f"G: Lemma A_q  2^k T_q^k(a) = 3^(a_k) a + q rho_k  exact on {nG} random (a,q,k), k <= 60.")

# ---------------- H. cycle equation on every census cycle ----------------
nH = ncyc = 0
for q in range(1, QMAX + 1, 2):
    cyc, _, _ = census(q, nstart=2000)
    for c in cyc:
        ncyc += 1
        K = len(c)
        ds = {gcd(x, q) for x in c}
        assert len(ds) == 1, (q, c)              # gcd(x,q) is constant along a cycle
        odds = [x for x in c if x % 2 == 1]
        if not odds:                                # the {0} cycle: no odd element
            assert c == (0,) and 0 * (2 ** K - 3 ** 0) == q * 0
            continue
        for anchor in odds:                         # every anchoring
            xs, expo = [], []
            x = anchor
            while True:
                xs.append(x)
                e = 0
                y = 3 * x + q
                assert y != 0
                while y % 2 == 0:
                    y //= 2
                    e += 1
                expo.append(e)
                x = y
                if x == anchor:
                    break
            m = len(xs)
            A = [0]
            for e in expo:
                A.append(A[-1] + e)
            assert A[m] == K, (q, c)
            cc = sum(3 ** (m - i) * 2 ** A[i - 1] for i in range(1, m + 1))
            assert xs[0] * (2 ** K - 3 ** m) == q * cc, (q, c, anchor)
            w = word_q(anchor, q, K)
            assert sum(w) == m and rho_rec(w) == cc, (q, c, anchor)   # rho_w = c
            nH += 1
print(f"H: cycle equation x_1(2^K - 3^m) = q*c verified for all {ncyc} cycles met by the census")
print(f"   with starts |a| <= 2000, for every odd q <= {QMAX},")
print(f"   at all {nH} anchorings at odd elements; in each case the word constant rho_w equals c.")

# ---------------- I. realization of every word by some q ----------------
nI = 0
for K in range(1, 11):
    for w in product((0, 1), repeat=K):
        a = sum(w)
        D = 2 ** K - 3 ** a
        assert D % 2 == 1 and D != 0
        rho = rho_rec(w)
        g = gcd(abs(D), rho)
        q0 = abs(D) // g
        assert q0 % 2 == 1, (w,)
        num = q0 * rho
        assert num % D == 0, (w,)
        x1 = num // D
        y = x1
        for _ in range(K):
            y = Tq(y, q0)
        assert y == x1, (w,)                                   # T_{q0}^K(x1) = x1
        reps = (2 * K // K) + 1
        assert word_q(x1, q0, 2 * K) == (w * reps)[:2 * K]      # parity word is w^infty
        if K <= 7:                                             # divisibility criterion
            for q in range(1, 2002, 2):
                assert ((q * rho) % D == 0) == (q % q0 == 0), (w, q)
        nI += 1
print(f"I: every one of the {nI} words with 1 <= K <= 10 is realized as an integer T_q0-periodic")
print("   point with q0 = |2^K-3^a|/gcd(|2^K-3^a|,rho_w) odd; for K <= 7 the criterion")
print("   'q*rho_w/(2^K-3^a) in Z  <=>  q0 | q' checked for every odd q <= 2001.")

# ---------------- J. the correspondence trap ----------------
orb5 = [1]
while Tq(orb5[-1], 5) != 1:
    orb5.append(Tq(orb5[-1], 5))
assert orb5 == [1, 4, 2]
assert Fraction(1, 5).denominator == 5                       # 1/5 is not an integer
rat = [Fraction(1, 5)]
while T(rat[-1]) != Fraction(1, 5):
    rat.append(T(rat[-1]))
assert rat == [Fraction(1, 5), Fraction(4, 5), Fraction(2, 5)]
# and the true statement in the other direction: q * (a T_1-cycle) IS a T_q-cycle
for q in range(1, 22, 2):
    for base in ([1, 2], [-1], [-5, -7, -10]):
        scaled = [q * b for b in base]
        for i, s in enumerate(scaled):
            assert Tq(s, q) == scaled[(i + 1) % len(scaled)], (q, base)
print("J: {1,4,2} is a T_5-cycle, yet 1/5 is not an integer -- so a 3x+q cycle need NOT be")
print("   q times an integer 3x+1 cycle; it is q times a RATIONAL T-cycle: {1/5,4/5,2/5}")
print("   (= L-9904.6 item 5). Conversely q*(T_1-cycle) is always a T_q-cycle: checked for")
print("   q <= 21 on the cycles (1,2), (-1), (-5,-7,-10).")

# ---------------- K. finiteness of (1/q)Z cap [-B,B] ----------------
for q in range(1, 16, 2):
    for B in range(0, 6):
        S = {Fraction(a, q) for a in range(-q * B, q * B + 1)}
        assert len(S) == 2 * q * B + 1
        assert all(abs(v) <= B for v in S)
        assert Fraction(q * B + 1, q) > B
print("K: |(1/q)Z cap [-B,B]| = 2qB+1 (finite) for all odd q <= 15 and integer B <= 5 --")
print("   the exact hypothesis (P2) that the L-9921.2 pigeonhole needs.")

# ---------------- L. trichotomy shadow ----------------
nL = 0
for _ in range(400):
    q = rand_odd_q(99)
    a = random.randint(-10 ** 5, 10 ** 5)
    x = Fraction(a, q)
    seen = {}
    for t in range(20000):
        assert q % x.denominator == 0
        if x in seen:
            break
        seen[x] = t
        x = T(x)
    else:
        raise AssertionError((a, q))
    nL += 1
print(f"L: {nL} random rational T-orbits a/q (q odd <= 99, |a| <= 10^5) all became eventually")
print("   periodic within 20000 steps, every iterate staying in (1/q)Z.")

# ---------------- M. sign is not preserved for q > 1 ----------------
assert Tq(-1, 5) == 1 and Tq(-1, 1) == -1
assert Tq(-3, 11) == 1 and Tq(-3, 1) == -4
print("M: T_5(-1) = 1 and T_11(-3) = 1: for q > 1, T_q does NOT preserve sign, so divergence")
print("   for T_q must be phrased as |T_q^k(a)| -> infinity (T_1 does preserve sign: T(-1) = -1).")

# ---------------- N. lower envelope ----------------
nN = 0
for _ in range(2000):
    q = rand_odd_q()
    a = random.randint(1, 10 ** 6)
    k = random.randint(0, 40)
    w = word_q(a, q, k)
    x = a
    for _ in range(k):
        x = Tq(x, q)
    assert 2 ** k * x >= 3 ** sum(w) * a, (a, q, k)
    nN += 1
print(f"N: lower envelope T_q^k(a) >= 3^(a_k) a / 2^k for a > 0 on {nN} random (a,q,k).")

print()
print("ALL CHECKS PASSED")
```

**Output of `python3 verify_L9921.py` (verbatim, single run, 2026-07-25, CPython 3.11,
Linux; runtime 0.62 s):**

```text
A: 2-adic parity of a/q equals a mod 2 for 5000 random (a,q), q odd, a of both signs
   (checked against the intrinsic digit of a*q^{-1} mod 2^64, and against lowest terms).
B: T^k(a/q) = T_q^k(a)/q verified stepwise on 600 random (a,q) with k up to 200;
   every iterate lies in (1/q)Z (lowest-terms denominator divides q).
C: gcd(a,q) | gcd(T_q(a),q) on 3000 random pairs; the lowest-terms denominator divides
   its predecessor and strictly dropped in 356 of them; explicit drop 1/3 -> 1.
D: scaling lemma T_q(d*b) = d*T_(q/d)(b) for d | q verified on 3000 random (d, q/d, b).
E: for 3|q and a odd, T_q(a) in 3Z; every one of 2000 random orbits reached 3Z within 200 steps.
F: T_1 = T cycles verified exactly and closed, with least periods:
      0: length  1  [0]
      1: length  2  [1, 2]
     -1: length  1  [-1]
     -5: length  3  [-5, -7, -10]
    -17: length 11  [-17, -25, -37, -55, -82, -41, -61, -91, -136, -68, -34]
G: Lemma A_q  2^k T_q^k(a) = 3^(a_k) a + q rho_k  exact on 3000 random (a,q,k), k <= 60.
H: cycle equation x_1(2^K - 3^m) = q*c verified for all 85 cycles met by the census
   with starts |a| <= 2000, for every odd q <= 21,
   at all 315 anchorings at odd elements; in each case the word constant rho_w equals c.
I: every one of the 2046 words with 1 <= K <= 10 is realized as an integer T_q0-periodic
   point with q0 = |2^K-3^a|/gcd(|2^K-3^a|,rho_w) odd; for K <= 7 the criterion
   'q*rho_w/(2^K-3^a) in Z  <=>  q0 | q' checked for every odd q <= 2001.
J: {1,4,2} is a T_5-cycle, yet 1/5 is not an integer -- so a 3x+q cycle need NOT be
   q times an integer 3x+1 cycle; it is q times a RATIONAL T-cycle: {1/5,4/5,2/5}
   (= L-9904.6 item 5). Conversely q*(T_1-cycle) is always a T_q-cycle: checked for
   q <= 21 on the cycles (1,2), (-1), (-5,-7,-10).
K: |(1/q)Z cap [-B,B]| = 2qB+1 (finite) for all odd q <= 15 and integer B <= 5 --
   the exact hypothesis (P2) that the L-9921.2 pigeonhole needs.
L: 400 random rational T-orbits a/q (q odd <= 99, |a| <= 10^5) all became eventually
   periodic within 20000 steps, every iterate staying in (1/q)Z.
M: T_5(-1) = 1 and T_11(-3) = 1: for q > 1, T_q does NOT preserve sign, so divergence
   for T_q must be phrased as |T_q^k(a)| -> infinity (T_1 does preserve sign: T(-1) = -1).
N: lower envelope T_q^k(a) >= 3^(a_k) a / 2^k for a > 0 on 2000 random (a,q,k).

ALL CHECKS PASSED
```

### What the tests attack, and their limits

- **A** is the one place where the file's whole dictionary could silently be wrong: it
  recomputes the 2-adic parity of $a/q$ from $q^{-1} \bmod 2^{64}$ — an independent route
  — instead of trusting "numerator mod 2". A sign error or a wrong inverse would fail on
  the first sample.
- **B** iterates *both* sides stepwise (not just endpoints), on negative $a$ as well as
  positive, for up to 200 steps, in exact rational arithmetic, and asserts the
  denominator condition at every single step. An error in the odd branch
  ($(3a+q)/2$ vs $(3a+1)/2$) fails immediately.
- **C/D/E** attack the bookkeeping claims that are easiest to state backwards: the gcd
  moves *up*, not down (356 observed strict denominator drops), the scaling lemma needs
  $d \mid q$ *and* $d \mid a$, and the $3\mid q$ collapse.
- **F** is the required anchor and pins the least periods (a spurious extra element or a
  wrong sign would break the closure assertion).
- **G/H** attack L-9921.6 from two independent directions: the $T_q$-form (Lemma A$_q$,
  random inputs including negatives) and the $S_q$-form (every anchoring of every cycle
  found), and cross-check that $\rho(w) = c$, which is the identification most easily got
  wrong.
- **I** attacks Corollary 3 exhaustively over all $2046$ words of length $\le 10$,
  including $w = 0^K$ and $w = 1^K$, and checks the divisibility criterion in **both**
  directions over 1001 values of $q$ per word for $K \le 7$ — a one-sided criterion would
  fail.
- **J** is the deliberate trap: it exhibits the standard misstatement of the classical
  correspondence and refutes it with an explicit object, while confirming the direction
  that *is* true.
- **Limits.** Everything here is finite. The census inspects $|a| \le 20000$, $q \le 21$
  only; Test I inspects $K \le 10$; no test bears on Q-9904, on divergence, or on any
  $q > 21$. None of the numbered claims cites any test.

---

## Remaining uncertainty

- L-9921.1, .1b, .2, .3, .4 and .6 (with Lemma A$_q$, Lemma R and Corollaries 1–4) are,
  in the author's assessment, complete proofs from the listed dependencies; no PARTIAL
  label is needed for them. Status is PROPOSED; only an independent reviewing agent may
  upgrade it.
- **Explicitly labelled non-proofs in this file:** L-9921.5(a) is EMPIRICAL;
  L-9921.5(c) is an UNVERIFIED port and is used nowhere; L-9921.5(d) is a subjective
  assessment.
- **The imports to probe.** Everything rests on L-9904's B7 (the parity of an
  odd-denominator rational is the parity of its numerator) and on L-9904.5(i)/(ii) for
  Corollary 3. If B7 were wrong the entire file collapses; it is proved in L-9904 and
  re-derived here in the L-9921.1(2) proof from B3 alone, and independently checked in
  Test A.
- **Proof spots a verifier should press hardest.**
  1. **The well-foundedness of Lemma R** (L-9921.3, (C$'$)$\Rightarrow$(C)). Case 2
     invokes Case 1 *at the same $q$* before recursing; the reader should check that the
     eventual recursive call really is at a modulus $\le q/3 < q$, and that "the tail of a
     divergent orbit is divergent" is used only in the direction stated.
  2. **The claim $c = \rho(w)$** in L-9921.6 — specifically that the positions of the ones
     in the $T_q$-parity word anchored at an odd element are exactly $A_0, \dots, A_{m-1}$
     and that $s_{A_{i-1}}(w) = m-i$. An off-by-one here would silently change $c$.
     Independently checked by Test H at 315 anchorings.
  3. **Corollary 2(2)**, where the constancy of $\gcd(\cdot,q)$ on a cycle
     (L-9921.1b(1)) is what upgrades "some element divisible by $q$" to "all elements
     divisible by $q$". Without that step the corollary is false as stated.
  4. **The direction of the divisibility in Corollary 3**: $|D| \mid q\rho_w \iff
     q_w \mid q$ uses Gauss's lemma after dividing out $g$; the degenerate case
     $\rho_w = 0$ must be checked separately (it is, in the Gap audit and Test I).
  5. **The box after L-9921.2**: a verifier should confirm that no *proved* statement of
     L-9901 or L-9907 is being contradicted — only the informal reading of L-9901's
     remark is sharpened, and L-9907's caveat already contained the positive-rational
     case.
- **Two deviations from the task sketch are recorded in the Gap audit** ("in lowest
  terms" narrowed the domain incorrectly; "divergent" must mean divergence in absolute
  value because $T_q$ does not preserve sign for $q>1$). Everything else in the sketch
  verified as given.

---

## Suggested next attack

1. **Review to PROVED.** Reconstruct L-9921.3 independently — in particular Lemma R,
   which is the only non-routine argument in the equivalence — and re-derive
   L-9921.6.1's telescoping from scratch. A second, independent census implementation
   (e.g. Brent cycle detection with no memo table) would also re-derive the L-9921.5(a)
   table.
2. **Consume downstream.** (i) L-9904's "Suggested next attack" item 4 can now be closed
   and replaced by a pointer here. (ii) Any file that invokes "unbounded $\Rightarrow$
   divergent" for a rational object should cite L-9921.2 rather than re-deriving it, and
   any file proposing a bounded non-periodic *rational* orbit is refuted by it.
   (iii) Issue #21/#4/#10 constructions that land in $\mathbb{Q}$ rather than
   $\mathbb{Z}$ now have a sharp verdict: they are $3x+q$ statements, not Collatz
   statements, unless $q = 1$.
3. **Port the deep half of L-9907 (the honest next lemma).** L-9921.5(c) is the obvious
   gap: prove that a divergent $T_q$-orbit in $\mathbb{Z}^+$ has
   $\liminf a_k/k \ge \gamma$, with the constant's dependence on $q$ made explicit. This
   is a bounded, well-posed task and would give the first genuinely *uniform-in-$q$*
   statement in the family.
4. **Probe cycle techniques against $q > 1$ as a falsification harness.** Any proposed
   proof that "no nontrivial cycle exists" should be re-run verbatim with $q$ as a
   parameter. By Corollary 3 it *must* break somewhere for large $q$; locating the exact
   step that fails is a cheap and sharp diagnostic of whether the argument uses anything
   beyond the shape of the cycle equation. The census table is a ready-made set of
   counterexample cycles for exactly this purpose (e.g. the seven $(K,m) = (8,5)$ cycles
   at $q = 13$).
5. **A well-posed finite sub-question that is NOT Collatz.** For fixed $q$ coprime to $3$
   with $q > 1$, is every $T_q$-orbit eventually periodic? By Lemma R this family (with
   $\gcd(a,q) = 1$) is exactly the content of Q-9904 beyond $q=1$. Nothing here suggests
   it is easier than $q=1$, but the $q > 1$ cases are at least *not* known to contain the
   Collatz problem, so a negative answer at some $q > 1$ would settle Q-9904 without
   settling Collatz — the third alternative already noted in L-9904's Q-9904 remark, now
   with an explicit search space.

---

*Signed: fable-02-p15, 2026-07-25. Finite verification scripts `cycles_L9921.py` and
`verify_L9921.py` (scratchpad; full text and verbatim output above).*

---

## Verification note (fable-02-v23, 2026-07-26)

**Verdict: PASS.** Independent adversarial review per README §13, performed without
relying on the author's confidence. Every proof was reconstructed from the listed
dependencies before re-reading the author's argument, and all computations were redone
with independently written code (different algorithms, different random seed) before
the embedded scripts were re-run. Status upgraded PROPOSED → PROVED. Not
INDEPENDENTLY_VERIFIED — per this packet's convention that upgrade is reserved for a
further cross-session review. **No gap was found in any numbered claim: L-9921.1,
.1b, .2, .3 (with Lemma R), .4, .5(b), and .6 (Lemma A$_q$, L-9921.6.1, Corollaries
1–4) are correct as stated.** The labelling of the non-proof material — .5(a)
EMPIRICAL, .5(c) UNVERIFIED port (used nowhere), .5(d) subjective assessment — is
accurate and consistently maintained in the Statement, Scope, Proof, and Gap audit.

### 1. The author's five flagged probe spots (Remaining uncertainty), each pressed

1. **Well-foundedness of Lemma R — sound.** The recursion structure was traced
   explicitly. Case 1 invokes the induction hypothesis at modulus $q/d$ with
   $d = \gcd(a,q) > 1$ odd, hence $d \ge 3$ and $q/d \le q/3 < q$. Case 2 performs
   *no* recursive call at modulus $q$: the passage to the tail element
   $b = T_q^j(a) \in 3\mathbb{Z}$ is an inline computation (1b(4)(iii)), and the
   subsequent "Case 1 applied to $(q,b)$" is the *scaling step* of Case 1 (1b(3)),
   which produces a divergent $T_{q'}$-orbit at $q' = q/\gcd(b,q) \le q/3 < q$
   (since $3 \mid \gcd(b,q)$) before the induction hypothesis is invoked — at $q'$,
   not at $q$. Every IH invocation is therefore at a strictly smaller positive odd
   modulus, and $q = 1$ is necessarily terminal Case 3 ($\gcd(a,1)=1$, $3 \nmid 1$).
   "Tail of a divergent sequence is divergent" is used only in the stated direction
   (whole orbit divergent $\Rightarrow$ tail divergent). The degenerate starts are
   covered: $a = 0$ cannot occur in Case 2 (its orbit is constantly $0$, not
   divergent), and $q \mid b$ in Case 2 harmlessly lands the recursion at $q' = 1$.
2. **The identity $c = \rho(w)$ — sound; the off-by-one was checked both
   symbolically and mechanically.** Re-derivation: by induction along the cycle,
   $T_q^{A_{i-1}}(x_1) = x_i$ for $1 \le i \le m$; from odd $x_i$, one odd $T_q$-step
   gives $2^{a_i-1}x_{i+1}$ followed by exactly $a_i - 1$ even steps, so within
   $[0,K)$ the ones of $w$ sit exactly at $\{A_0, \dots, A_{m-1}\}$ (note $A_{i-1}$,
   not $A_i$), the $A_j$ being strictly increasing since $a_i \ge 1$. Hence for
   $j = A_{i-1}$ the strict-after count is $s_j(w) = \#\{A_i, \dots, A_{m-1}\} = m-i$
   — matching L-9903.2's convention $s_i(w) = \#\{j : i < j < K,\ w_j = 1\}$
   exactly — and the closed form gives $\rho(w) = \sum_i 3^{m-i}2^{A_{i-1}} = c$.
   Independently verified at **all 315 anchorings of all 85 census cycles**, with
   the ones-positions and every $s_{A_{i-1}}$ value asserted individually, and with
   $\rho$ computed **two** ways (recursion and closed form) — see §3.
3. **Corollary 2(2) — sound.** The upgrade "some element divisible by $q$
   $\Rightarrow$ all elements" is exactly the constancy of $\gcd(\cdot,q)$ on a
   cycle (1b(1)), whose proof (divisibility chain closing on itself) was
   re-derived; gcd-constancy was also machine-checked on every census cycle.
   Without it the corollary would indeed be false as stated; with it the proof is
   complete, and the $d = q$ instance of 1b(3) correctly converts $\Delta/q$ into a
   $T$-cycle.
4. **The Gauss step in Corollary 3 — sound, including the degenerate case.** The
   chain $D \mid q\rho_w \iff |D| \mid q\rho_w \iff gD' \mid gq\rho' \iff
   D' \mid q\rho' \iff D' \mid q$ was checked link by link ($g \ge 1$ cancels;
   Gauss/Euclid applies since $\gcd(D',\rho') = 1$; sign of $D$ irrelevant).
   $\rho_w = 0$ gives $g = |D|$, $q_w = 1$, both sides universally true, and
   $x = 0$: consistent. Exhaustively re-verified for all $2046$ words with
   $K \le 10$ (realization at $q_w$, $K$-periodicity, word $= w^\infty$ over $3K$
   steps) and, two-sidedly, for the criterion at every odd $q \le 2001$ for
   $K \le 7$, plus 300 random words with $11 \le K \le 16$.
5. **The box after L-9921.2 — no PROVED statement of L-9901 or L-9907 is
   contradicted.** Checked against the sources. L-9901's Lemma D and L-9901.4 are
   scoped to $X \subseteq \mathbb{Z}^+$ and are untouched. L-9901's boxed remark's
   $\mathbb{Q}$ bullet asserts only that the pigeonhole *with ambient set*
   $\mathbb{Z}_{(2)}$ yields nothing — true, since $\mathbb{Z}_{(2)} \cap [0,B]$ is
   infinite (P2 fails there); L-9921.2 instead uses ambient $\Lambda_q$, so there is
   no conflict, and 1b(2) (denominators never grow along one orbit) is the correct
   sharpening of the remark's set-level phrasing. L-9907's BOXED CAVEAT already
   *proves* the positive single-orbit rational case ("for a single $T$-orbit of a
   positive odd-denominator rational, unbounded still implies divergent"), of which
   L-9921.2 is the two-signed, whole-ambient-set generalization — the two agree
   where they overlap. The box's own characterization of itself ("refinement, not
   correction of any proved statement") is accurate.

### 2. Independent reconstruction of the proofs

- **L-9921.1(1)–(5), P0.1–P0.3:** re-derived from B7/B3/B2 of L-9904 (statuses
  confirmed: L-9901, L-9903, L-9904, L-9905, L-9907 are all PROVED with recorded
  reviewers). The parity dictionary needs no coprimality; representation
  independence follows from $aq' = a'q$ mod $2$. The conjugacy computation in both
  branches, the induction on $k$, and the transfer of eventual periodicity
  (multiply/divide by $q \ne 0$) and of magnitudes ($|T^k(x)| = |T_q^k(a)|/q$) are
  all correct.
- **L-9921.1b:** all four items re-proved; the strict-drop example $1/3 \mapsto 1$
  checked ($\gcd$ jumps $1 \to 3$).
- **L-9921.2:** (P2) recounted (floor handles non-integer $B$; $B = 0$ gives $1$);
  Steps 2–4 are the standard pigeonhole and were re-derived; the proof uses exactly
  (P1)+(P2) as claimed.
- **L-9921.3:** all six implications re-derived; the fully-quantified form of (C)
  is the correct negation of D-9921.2. The closing remark correctly routes through
  L-9904.5(iii)(3b).
- **L-9921.4:** the $C$/$T$ chain uses L-9901.2(iii) and (via L-9901.4, whose
  Lemma D covers arbitrary self-maps of subsets of $\mathbb{Z}^+$, hence $C$)
  unbounded $\iff$ divergent, correctly. Sign preservation of $T$ on
  $\mathbb{Z}^-$, the $3x{-}1$ conjugation, and the three negative cycles were
  re-verified by hand and by machine (least periods $1, 3, 11$; all steps exact).
  The "no converse is claimed" discipline is maintained throughout.
- **L-9921.5(b):** follows from Lemma A$_q$ with $q\rho_k \ge 0$; the
  $\limsup$/$\liminf$ split is handled correctly ($\gamma \log_2 3 = 1$). A useful
  side fact implicit in the proof was confirmed: for $a > 0$ the identity forces
  $T_q^k(a) > 0$ for all $k$, so "the positive $T_q$-orbit" is well-posed.
- **L-9921.6:** Lemma A$_q$'s one-step identity and induction re-derived; the
  telescoping in L-9921.6.1 recomputed from scratch ($u_{m+1} - u_1 = qc$ with
  $u_{m+1} = 2^K x_1$, $u_1 = 3^m x_1$); anchor-independence of $m, K$ is correct.
  Corollary 1's geometric identity $\sum_{i=1}^m 3^{m-i}2^{i-1} = 3^m - 2^m$, the
  product formula (cancellation legitimate: all $x_i$ odd, hence $\ne 0$), and the
  $\ln$-estimates were re-derived. Corollary 2(1),(3),(4) re-proved;
  $\{1,4,2\}$ at $q=5$ and its rational image $\{1/5,4/5,2/5\}$ (= L-9904.6 item 5)
  confirmed. Corollary 4 is immediate as stated.
- **Dependency audit cross-checked:** every imported statement was located in its
  source file and says what this file uses (L-9904 B7/B2/B3/P0/.1/.5(i)(ii)(iii)(3b)/
  Lemma D/L-9904.6 item 5/L-9904.7; L-9901.2(iii)/.4/.5 + boxed remark; L-9907.1/.3
  + caveat; L-9903.2; L-9905.1/.3/.4/.5). No dependency cites L-9921 (grep over
  L-9901/03/04/05/07): no circularity. Q-9904 is never assumed.

### 3. Independent computation (scripts `extract_embedded.py`, `indep_L9921.py`,
scratchpad of session v23; exact arithmetic; seed 20260726, distinct from the
author's; runtime ≈ 5 s)

- **Census re-derived with a different algorithm.** Brent cycle detection, one
  start at a time, **no memo table** (the author's suggested falsification route),
  over all $|a| \le 20000$ for $q \in \{1, 5, 13, 17\}$: cycle inventories agree
  **exactly** (as sets of sets) with both my own memoized re-implementation and the
  author's `census()`. The memoized re-implementation was run for all odd
  $q \le 21$: all 11 inventories match the author's; totals
  $(5,5,10,6,5,8,14,10,9,7,6)$, $85$ cycles, $0$ escapes/step-caps. Table
  cross-checks all pass: primitive counts per $q$; the $(K,m)$ profiles of every
  primitive cycle; the **seven** $(8,5)$ cycles at $q=13$ anchored at
  $211, 227, 251, 259, 283, 287, 319$; the $(31,18)$ cycle at $q=17$ anchored at
  $23$; the two $(27,17)$ cycles at $q=5$ (anchors $187, 347$); gcd-constancy on
  every cycle; the five $q$-scaled $T_1$-cycles present for every $q$ (re-checked up
  to $q = 41$, beyond the census range); zero primitive cycles for
  $q \in \{3,9,15,21\}$; and every non-primitive cycle verified to be $d \times$ a
  primitive $T_{q/d}$-cycle (Corollary 2(4)) by direct computation.
- **Cycle equation and $c = \rho(w)$:** verified at all $315$ anchorings of all
  $85$ cycles (count independently reproduced), including the all-negative cycles
  (e.g. $q=17$, anchor $-65$: $c = 65$, $2^6 - 3^4 = -17$), with ones-positions,
  $s$-values, both $\rho$ evaluations, Lemma A$_q$ closure at $k = K$, and — for
  all-positive cycles — $2^K > 3^m$ and the exact product formula
  $2^K = \prod (3 + q/x_i)$ in `Fraction` arithmetic.
- **Conjugacy:** $T^k(a/q) = T_q^k(a)/q$ checked stepwise in exact rationals for
  500 random $(a,q)$, $|a| \le 10^{10}$, odd $q \le 1201$, both signs,
  $k \le 300$, asserting at every step membership in $\Lambda_q$, the parity
  dictionary, and that the lowest-terms denominator divides its predecessor.
  Parity dictionary independently re-checked against the intrinsic digit
  $a \cdot q^{-1} \bmod 2^{80}$ (different modulus from the author's Test A) on
  4000 samples.
- **Other:** iterated scaling $T_q^k(db) = d\,T_{q/d}^k(b)$ (3000 samples,
  $k \le 50$); $3 \mid q$ facts; (P2) counts including non-integer $B$;
  $T_5(-1) = 1$, $T_{11}(-3) = 1$ and $T_1$'s sign preservation on 2000 negative
  samples; the $3x{-}1$ conjugation on 2000 samples; 300 random rational orbits all
  eventually periodic within $\Lambda_q$; the envelope of .5(b) on 3000 samples.
- **Placeholder audit: PASS.** Both embedded scripts were extracted verbatim from
  the file and re-run under CPython 3.11 (the stated environment): the outputs are
  **byte-identical** to the recorded output blocks (raw `diff`, no normalization),
  including every incidental constant (e.g. the "356" strict denominator drops in
  Test C, which is seed-determined).

### 4. Minor remarks (no action required; recorded for completeness)

- **Naming:** L-9921.2 is titled "trichotomy" (echoing L-9901.4, where case (a)
  splits by which cycle is entered) but is formally stated as a dichotomy
  (a)/(b). The formal statement is exact and self-contained, and every internal
  citation uses the statement, not the name; left as is.
- The Adversarial-tests section stores its scripts under a session-specific
  scratchpad path; since both scripts are reproduced in full in the file and
  re-verified here, nothing is lost, but a future re-organization pass could move
  them under `experiments/` per README §10.
- The empirical census necessarily says nothing about cycles all of whose elements
  exceed $20000$ in absolute value, about $q > 21$, or about divergence — exactly
  as the file itself states, prominently and repeatedly. No claim in the file
  overreaches its evidence.

*Signed: fable-02-v23, 2026-07-26.*
