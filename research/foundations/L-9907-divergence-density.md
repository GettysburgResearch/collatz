# L-9907 — Parity-density threshold for divergent trajectories

```text
Claim ID: L-9907
Title: Parity-density threshold for divergent trajectories (the gamma = log_3 2 criterion)
Status: PROPOSED
Authoring agent: fable-02-p6
Reviewing agents: (none yet)
Created: 2026-07-21
Last updated: 2026-07-21
Dependencies: NOTATION.md (D-9902 shortcut map T; D-9906 parity vector v_i, a_k;
              D-9907 bounded/unbounded/divergent). Related: L-9901 (orbit trichotomy,
              parallel file), L-9903 — all overlaps with those files are re-proved
              inline here; this file depends on NOTATION.md only.
Scope: T-orbits (D-9902) of positive integers; L-9907.5 also identifies explicit
       residue classes. All statements are about T, never C or S, unless stated.
Related counterexample candidates: none
```

---

## Statement

Throughout, $n \in \mathbb{Z}^+$, $T$ is the shortcut map (D-9902), $v_i = v_i(n) \in \{0,1\}$
and $a_k = a_k(n) = \sum_{i=0}^{k-1} v_i$ are as in D-9906, and
$$\gamma := \log_3 2 = \frac{\ln 2}{\ln 3} = \frac{1}{\log_2 3} \approx 0.6309298.$$
Note the identity $\gamma \cdot \log_2 3 = 1$, used repeatedly. Since $0 \le a_k \le k$,
the sequence $(a_k/k)_{k \ge 1}$ lies in $[0,1]$, so its $\liminf$ and $\limsup$ exist in $[0,1]$.

**L-9907.1 (lower envelope; supercritical criterion).**
For every $n \in \mathbb{Z}^+$ and every $k \ge 0$,
$$T^k(n) \;\ge\; \frac{3^{a_k(n)}}{2^k}\, n \;=\; n \cdot 2^{\,a_k(n)\log_2 3 - k}.$$
Consequently:
(i) if $\limsup_{k\to\infty} a_k(n)/k > \gamma$, then the $T$-orbit of $n$ is unbounded
(D-9907), i.e. $\sup_k T^k(n) = \infty$;
(ii) if $\liminf_{k\to\infty} a_k(n)/k > \gamma$, then $T^k(n) \to \infty$ (the orbit is
divergent, D-9907).

**L-9907.2 (divergence forces density; the deep direction).**
If $T^k(n) \to \infty$ as $k \to \infty$, then
$$\liminf_{k\to\infty} \frac{a_k(n)}{k} \;\ge\; \gamma.$$
Quantitatively: for every $\delta \in (0,1)$ there is an explicit constant
$C(\delta, n) \ge 0$ (defined in the proof) such that
$a_k(n)\log_2 3 \ge k(1-\delta) - C(\delta,n)$ for all $k \ge t_0(\delta,n)$.

**L-9907.3 (unbounded suffices, for integers).**
For every $n \in \mathbb{Z}^+$, exactly one of the following holds:
(a) the $T$-orbit of $n$ is eventually periodic, and then it is bounded;
(b) $T^k(n) \to \infty$.
In particular, for integer $T$-orbits, *unbounded* $\iff$ *divergent*, and hence
(combining with L-9907.2) an unbounded integer $T$-orbit satisfies
$\liminf_k a_k(n)/k \ge \gamma$. A boxed caveat in the proof section delimits exactly
where this pigeonhole argument does and does not apply.

**L-9907.4 (two-sided summary, refinement, and open boundary).**
For every $n \in \mathbb{Z}^+$:
$$\liminf_k \frac{a_k(n)}{k} > \gamma
\;\Longrightarrow\; T^k(n) \to \infty
\;\Longrightarrow\; \liminf_k \frac{a_k(n)}{k} \ge \gamma,$$
and also $\limsup_k a_k(n)/k > \gamma \Rightarrow$ unbounded $\Rightarrow$ divergent
$\Rightarrow \liminf_k a_k(n)/k \ge \gamma$ (the middle step is $\mathbb{Z}^+$-specific,
via L-9907.3). Refinement L-9907.4-R (proved below): for a divergent integer orbit,
$$\liminf_k \frac{a_k(n)}{k} = \gamma\Big(1 + \liminf_k \frac{\log_2 T^k(n)}{k}\Big),
\qquad
\limsup_k \frac{a_k(n)}{k} = \gamma\Big(1 + \limsup_k \frac{\log_2 T^k(n)}{k}\Big).$$
The boundary case $\liminf_k a_k/k = \gamma$ is **not decided** by these methods; it is
recorded as open question Q-9902 below.

**L-9907.5 (glider lemma — long rises exist).**
For every $j \ge 1$ and every $n \in \mathbb{Z}^+$:
$$n \equiv -1 \pmod{2^j}
\;\Longleftrightarrow\;
v_0(n) = v_1(n) = \dots = v_{j-1}(n) = 1,$$
and when these hold,
$$T^j(n) \;=\; \frac{3^j (n+1)}{2^j} - 1 \;>\; \Big(\frac{3}{2}\Big)^{\!j} n .$$
Corollaries: $T^j(2^j - 1) = 3^j - 1$; the initial parity run of $j$ ones occurs for
*exactly* the residue class $n \equiv 2^j - 1 \pmod{2^j}$ (equivalently
$n \equiv -1 \pmod{2^j}$), a class of natural density $2^{-j}$, nonempty for every $j$;
hence arbitrarily long all-ones parity runs, and rises by a factor exceeding $(3/2)^j$,
occur among positive integers.

---

## Definitions

All notation is from `NOTATION.md`; the following items are restated or introduced here.

- $T(n) = n/2$ ($n$ even), $T(n) = (3n+1)/2$ ($n$ odd) — the shortcut map (D-9902).
  $T$ maps $\mathbb{Z}^+$ into $\mathbb{Z}^+$, so $T^k(n) \ge 1$ for all $k \ge 0$.
- $v_i(n) = T^i(n) \bmod 2$, $a_k(n) = \sum_{i=0}^{k-1} v_i(n)$ (D-9906). Empty sum: $a_0 = 0$.
- Bounded / unbounded / divergent orbits per D-9907: $(x_k)$ is bounded if
  $\sup_k x_k < \infty$, unbounded otherwise, divergent if $x_k \to \infty$
  (for every $B$ there is $K$ with $x_k \ge B$ for all $k \ge K$).
- **Eventually periodic:** $(x_k)_{k\ge0}$ is eventually periodic if there are
  $k_1 \ge 0$ and $p \ge 1$ with $x_{k+p} = x_k$ for all $k \ge k_1$.
- $\gamma = \log_3 2 = 1/\log_2 3$; $\log_2 3 \approx 1.5849625$; $\gamma\log_2 3 = 1$.
- **Odd-step defect:** for odd $x \in \mathbb{Z}^+$,
  $$\varepsilon(x) := \log_2\!\Big(1 + \frac{1}{3x}\Big).$$
  Since $x \ge 1$, $0 < \tfrac{1}{3x} \le \tfrac13$, so
  $\varepsilon(x) \in (0, \log_2(4/3)]$ with $\log_2(4/3) \approx 0.4150375$;
  and $\varepsilon$ is strictly decreasing in $x$.
- **Accumulated defect:** $E_k = E_k(n) := \sum_{i < k,\ v_i(n) = 1} \varepsilon(T^i(n)) \ge 0$
  (empty sum $= 0$). Note $E_k \le a_k \log_2(4/3)$.
- $\nu_2(m)$: 2-adic valuation of $m \ne 0$.
- $\limsup_k x_k := \inf_{K} \sup_{k \ge K} x_k$, $\liminf_k x_k := \sup_K \inf_{k\ge K} x_k$.
  Two standard facts are used, with one-line proofs where invoked:
  (F1) if $\limsup_k x_k = L$ and $\eta > 0$, then $x_k > L - \eta$ for infinitely many $k$;
  (F2) if $\liminf_k x_k = \ell$ and $\eta > 0$, then $x_k > \ell - \eta$ for all
  sufficiently large $k$.

---

## Motivation

The project objective (D-9909) is to construct a Collatz counterexample; one of the two
possible failure modes is a divergent trajectory. This file pins down the exact
parity-density threshold that governs divergence, in both directions:

1. **Sufficient direction (a target).** Issue #21's supercritical criterion T-9602 is
   exactly the mechanism L-9907.1(i) + L-9907.3: exhibit an integer orbit whose odd-step
   density exceeds $\gamma$ along a subsequence, and unboundedness — hence, for integers,
   divergence — follows. This file gives that mechanism a rigorous, self-contained,
   independently-authored base in the foundations packet.
2. **Necessary direction (a filter).** L-9907.2 constrains every divergence program
   (issues #4/M1, #8, #10): *any* divergent candidate must sustain odd-step density
   $\ge \gamma \approx 0.6309298$ in the $\liminf$. Any proposed divergent orbit whose
   parity statistics provably fall below $\gamma$ on a tail is thereby refuted — a cheap,
   rigorous rejection test for candidates.
3. **Raw material.** L-9907.5 exhibits, with an exact closed form, the standard source of
   long rises (all-ones parity blocks on explicit residue classes), and the remark after
   its proof states precisely the gap between "long rises are abundant" and "density
   $\ge \gamma$ forever", which is what a divergence construction must close.
4. L-9907.4-R converts the boundary question into a growth-rate dichotomy
   (subexponential vs. exponential divergence), sharpening what any construction must
   decide about its own candidate.

---

## Proof or construction

### L-9907.1 — lower envelope and the supercritical criterion

**Envelope inequality.** We prove by induction on $k$: for all $n \in \mathbb{Z}^+$, $k \ge 0$,
$$T^k(n) \ \ge\ \frac{3^{a_k(n)}}{2^k}\, n. \tag{1.1}$$

*Base case $k = 0$:* $T^0(n) = n$ and $a_0 = 0$, so the right side is $3^0 n / 2^0 = n$.
Equality holds.

*Inductive step:* assume (1.1) for $k$; write $x := T^k(n) \ge 1$.
- If $v_k(n) = 0$ ($x$ even): $T^{k+1}(n) = x/2 \ge \tfrac{1}{2}\cdot\tfrac{3^{a_k}}{2^k} n
  = \tfrac{3^{a_{k+1}}}{2^{k+1}} n$, since $a_{k+1} = a_k$.
- If $v_k(n) = 1$ ($x$ odd): $T^{k+1}(n) = \tfrac{3x+1}{2} > \tfrac{3x}{2}
  \ge \tfrac{3}{2}\cdot\tfrac{3^{a_k}}{2^k} n = \tfrac{3^{a_{k+1}}}{2^{k+1}} n$,
  since $a_{k+1} = a_k + 1$.

This proves (1.1) for $k+1$; induction complete. Writing $3^{a_k} = 2^{a_k \log_2 3}$
gives the second form $T^k(n) \ge n\, 2^{a_k \log_2 3 - k}$. (The inequality is strict as
soon as at least one odd step has occurred.)

**Key computation.** If $a_k/k \ge \gamma + \eta$ for some $\eta > 0$, then, using
$\gamma \log_2 3 = 1$,
$$a_k \log_2 3 - k \;\ge\; k\big((\gamma + \eta)\log_2 3 - 1\big) \;=\; k\,\eta \log_2 3,$$
so by (1.1),
$$T^k(n) \;\ge\; n\, 2^{k \eta \log_2 3} \;=\; n\, 3^{k\eta}. \tag{1.2}$$

**(i).** Suppose $L^* := \limsup_k a_k/k > \gamma$; set $\eta := (L^* - \gamma)/2 > 0$.
By fact (F1) (proof: if $x_k \le L^* - \eta$ for all $k \ge K$, then
$\sup_{k \ge K'} x_k \le L^* - \eta$ for all $K' \ge K$, so
$\limsup x_k \le L^* - \eta < L^*$, contradiction), there are infinitely many $k$ with
$a_k/k > L^* - \eta = \gamma + \eta$. For each such $k$, (1.2) gives
$T^k(n) \ge n\,3^{k\eta}$. Since $3^{k\eta} \to \infty$ along this infinite set of $k$,
$\sup_k T^k(n) = \infty$: the orbit is unbounded (D-9907). $\square$

*Note.* (i) concludes unboundedness only. Divergence does **not** follow from (i) alone;
for integer orbits it follows by adding L-9907.3.

**(ii).** Suppose $\ell := \liminf_k a_k/k > \gamma$; set $\eta := (\ell - \gamma)/2 > 0$.
By fact (F2) (proof: $\inf_{k \ge K} x_k \uparrow \ell$ as $K \to \infty$, so some $K_0$
has $\inf_{k \ge K_0} x_k > \ell - \eta$), there is $k_0$ with
$a_k/k > \ell - \eta = \gamma + \eta$ for **all** $k \ge k_0$. By (1.2),
$T^k(n) \ge n\,3^{k\eta}$ for all $k \ge k_0$, and the right side tends to $\infty$
monotonically in $k$; hence $T^k(n) \to \infty$. $\square$

### L-9907.2 — divergence forces density $\ge \gamma$

**Step 1 (one-step logarithm).** Let $x \in \mathbb{Z}^+$.
- If $x$ is odd: $T(x) = \tfrac{3x+1}{2} = \tfrac{3x}{2}\big(1 + \tfrac{1}{3x}\big)$, so
  $$\log_2 T(x) = \log_2 x + \log_2 3 - 1 + \varepsilon(x),
  \qquad \varepsilon(x) = \log_2\!\Big(1+\frac{1}{3x}\Big) \in \big(0, \log_2\tfrac43\big].$$
  (Bounds: $x \ge 1$ odd gives $0 < \tfrac1{3x} \le \tfrac13$; $\log_2$ is strictly
  increasing; $\varepsilon(1) = \log_2(4/3)$.)
- If $x$ is even: $T(x) = x/2$, so $\log_2 T(x) = \log_2 x - 1$.

**Step 2 (telescoping identity).** For all $n \in \mathbb{Z}^+$ and $k \ge 0$,
$$\log_2 T^k(n) - \log_2 n \;=\; a_k(n)\,\log_2 3 \;-\; k \;+\; E_k(n),
\qquad E_k(n) = \sum_{\substack{0 \le i < k \\ v_i(n) = 1}} \varepsilon\big(T^i(n)\big) \ \ge 0.
\tag{2.1}$$
*Proof:* write $\log_2 T^k(n) - \log_2 n = \sum_{i=0}^{k-1}
\big(\log_2 T^{i+1}(n) - \log_2 T^i(n)\big)$; by Step 1, the $i$-th summand equals
$\log_2 3 - 1 + \varepsilon(T^i(n))$ when $v_i = 1$ and $-1$ when $v_i = 0$. Summing:
the $-1$'s contribute $-k$, the $\log_2 3$'s contribute $a_k \log_2 3$, and the
$\varepsilon$-terms contribute $E_k$. (Exponentiated exact form, verified with rational
arithmetic in the Adversarial tests:
$T^k(n)\,2^k = n\,3^{a_k}\prod_{i<k,\,v_i=1}\big(1+\tfrac{1}{3T^i(n)}\big)$.)
Each $\varepsilon$-term lies in $(0, \log_2(4/3)]$, so also
$0 \le E_k \le a_k \log_2(4/3) \le k \log_2(4/3)$. $\square$

**Step 3 (choice of constants).** Fix $\delta \in (0,1)$ and define
$$M(\delta) := \Big\lceil \frac{1}{3\,(2^{\delta} - 1)} \Big\rceil \in \mathbb{Z}^+ .$$
Then for every odd $x \ge M(\delta)$:
$$\varepsilon(x) \le \varepsilon\big(M(\delta)\big)
= \log_2\!\Big(1 + \frac{1}{3M(\delta)}\Big) \le \delta,$$
because $\varepsilon$ is decreasing, and $M(\delta) \ge \tfrac{1}{3(2^\delta-1)}$ gives
$\tfrac{1}{3M(\delta)} \le 2^\delta - 1$, i.e. $1 + \tfrac1{3M(\delta)} \le 2^\delta$.
($M(\delta) \ge 1$ since it is the ceiling of a positive real.)

**Step 4 (divergence supplies a tail).** Assume $T^k(n) \to \infty$. By the definition of
divergence applied with the bound $M(\delta)$, the set
$\{t \ge 0 : T^s(n) \ge M(\delta) \text{ for all } s \ge t\}$ is nonempty; let
$t_0 = t_0(\delta, n)$ be its least element. Define
$$C(\delta, n) := \log_2 n + E_{t_0}(n) \;\ge\; 0 .$$
$E_{t_0}(n)$ is a **finite** constant, explicitly bounded: it is a sum of at most $t_0$
terms (one per odd step among $i < t_0$), each in $(0,\log_2(4/3)]$ by Step 1, so
$$0 \le E_{t_0}(n) \le t_0(\delta,n)\,\log_2(4/3) < \infty,
\qquad\text{hence}\qquad
0 \le C(\delta,n) \le \log_2 n + t_0(\delta,n)\log_2\tfrac43 .$$
$C(\delta, n)$ depends on $\delta$ and $n$ but **not** on $k$.

**Step 5 (splitting $E_k$).** For every $k \ge t_0$:
$$E_k \;=\; E_{t_0} + \sum_{\substack{t_0 \le i < k \\ v_i = 1}} \varepsilon\big(T^i(n)\big)
\;\le\; E_{t_0} + (k - t_0)\,\delta \;\le\; E_{t_0} + k\,\delta, \tag{2.2}$$
because each index $i$ in the second sum has $T^i(n)$ odd (that is what $v_i = 1$ means)
and $T^i(n) \ge M(\delta)$ (since $i \ge t_0$), so $\varepsilon(T^i(n)) \le \delta$ by
Step 3, and there are at most $k - t_0$ such indices. (For $k = t_0$ the sum is empty and
(2.2) is trivial.)

**Step 6 (lower bound on $\log_2 T^k(n)$).** For $k \ge t_0$ we have
$T^k(n) \ge M(\delta) \ge 1$, hence $\log_2 T^k(n) \ge \log_2 M(\delta) \ge 0$.
(For integer orbits, $\log_2 T^k(n) \ge 0$ actually holds for *all* $k$, since
$T^k(n) \in \mathbb{Z}^+$ means $T^k(n) \ge 1$. We use only the eventual bound $\ge 0$,
which is the form that survives generalization to ambient sets containing points in
$(0,1)$, e.g. odd-denominator rationals.)

**Step 7 (conclusion for fixed $\delta$).** Rearranging (2.1):
$a_k \log_2 3 = k + \big(\log_2 T^k(n) - \log_2 n\big) - E_k$. For all $k \ge t_0$,
using Step 6 ($\log_2 T^k(n) \ge 0$) and (2.2):
$$a_k \log_2 3 \;\ge\; k - \log_2 n - E_{t_0} - k\delta
\;=\; k(1 - \delta) - C(\delta, n). \tag{2.3}$$
Dividing by $k \log_2 3 > 0$ and using $1/\log_2 3 = \gamma$:
$$\frac{a_k}{k} \;\ge\; (1-\delta)\,\gamma \;-\; \frac{C(\delta,n)}{k \log_2 3}
\qquad\text{for all } k \ge t_0. \tag{2.4}$$
Now take $\liminf_k$: for any $\eta > 0$ choose $k_1 \ge t_0$ with
$C(\delta,n)/(k\log_2 3) < \eta$ for all $k \ge k_1$ (possible since $C$ is a constant);
then $a_k/k > (1-\delta)\gamma - \eta$ for all $k \ge k_1$, so
$\liminf_k a_k/k \ge (1-\delta)\gamma - \eta$; as $\eta > 0$ was arbitrary,
$$\liminf_{k\to\infty} \frac{a_k}{k} \;\ge\; (1 - \delta)\,\gamma. \tag{2.5}$$

**Step 8 ($\delta \to 0$).** The left side of (2.5) is a single real number
$L \in [0,1]$, independent of $\delta$. (2.5) holds for **every** $\delta \in (0,1)$
(each with its own $M(\delta), t_0, C$ — those were used only inside the proof of (2.5)
for that $\delta$). Hence $L \ge \sup_{\delta \in (0,1)} (1-\delta)\gamma = \gamma$.
There is no interchange of limits here: for each fixed $\delta$ the limit in $k$ was
taken first and completely; then a supremum over $\delta$ of the resulting constants.
$\square$

*Where divergence was genuinely used:* only in Step 4, to produce a tail on which every
odd iterate is $\ge M(\delta)$ — i.e. to make the per-step defect $\varepsilon$ uniformly
$\le \delta$ eventually — and in Step 6's eventual lower bound. Unboundedness alone
(values $\ge M$ infinitely often) would not give Step 5, because the sum in (2.2) needs
*every* odd index $i \ge t_0$ to be large, not just infinitely many. For integers this
distinction is then erased by L-9907.3.

### L-9907.3 — for integer orbits, unbounded implies divergent

**Claim.** For $n \in \mathbb{Z}^+$, exactly one of:
(a) $O_T(n)$ is eventually periodic (hence bounded); (b) $T^k(n) \to \infty$.

**Proof.**
*(a) and (b) are mutually exclusive.* If the orbit is eventually periodic — say
$T^{k+p}(n) = T^k(n)$ for all $k \ge k_1$, with $p \ge 1$ — then (division with
remainder, as spelled out below) every orbit value lies in the finite set
$\{n, T(n), \dots, T^{k_1+p-1}(n)\}$, so the orbit is bounded: with
$B_0 := \max\{n, T(n), \dots, T^{k_1+p-1}(n)\}$, no $K$ satisfies
"$T^k(n) \ge B_0 + 1$ for all $k \ge K$", so $T^k(n) \not\to \infty$. Hence (a)
excludes (b), and conversely.

*At least one of (a), (b) holds — the pigeonhole step.* Suppose (b) fails:
$T^k(n) \not\to \infty$. Negating the definition of divergence: there exists
$B \in \mathbb{Z}^+$ such that
$$I := \{k \ge 0 : T^k(n) \le B\} \text{ is infinite.}$$
For $k \in I$, the value $T^k(n)$ lies in the **finite** set $\{1, 2, \dots, B\}$
(here integrality and positivity of the orbit are used: $T^k(n) \in \mathbb{Z}^+$).
Infinitely many indices, finitely many values: by pigeonhole some value
$m \in \{1,\dots,B\}$ satisfies $T^k(n) = m$ for infinitely many $k$. In particular there
exist $k_1 < k_2$ with
$$T^{k_1}(n) = T^{k_2}(n) = m.$$
$T$ is a deterministic function, so by induction on $t \ge 0$,
$T^{k_1 + t}(n) = T^{k_2 + t}(n)$ (base $t=0$ is the displayed equality; step: apply $T$
to both sides). Setting $p := k_2 - k_1 \ge 1$ and $t := k - k_1$ for any $k \ge k_1$:
$$T^{k + p}(n) = T^{k}(n) \qquad \text{for all } k \ge k_1,$$
i.e. the orbit is eventually periodic with period dividing $p$. Consequently, for every
$k \ge k_1$, writing $k - k_1 = qp + r$ with $0 \le r < p$ and applying the displayed
identity $q$ times, $T^k(n) = T^{k_1 + r}(n)$; hence
$$\{T^k(n) : k \ge 0\} \subseteq \{n, T(n), \dots, T^{k_1 + p - 1}(n)\},$$
a finite set. The orbit is bounded and eventually periodic: (a) holds. $\square$

**Corollary.** Unbounded $\Rightarrow$ not (a) $\Rightarrow$ (b): every unbounded integer
$T$-orbit is divergent, and therefore, by L-9907.2, satisfies
$\liminf_k a_k(n)/k \ge \gamma$. (Conversely divergent $\Rightarrow$ unbounded, so for
integer $T$-orbits *unbounded* $\iff$ *divergent*.) $\square$

*Relation to L-9901:* a parallel foundations file, L-9901, proves the orbit trichotomy
(reaches the trivial cycle / eventually enters a nontrivial cycle / diverges), of which
the dichotomy above is the coarse form — case (a) splits according to whether the
periodic part is the trivial cycle $(1,2)$ (D-9905) or a nontrivial cycle (D-9908). The
proof above is self-contained and does not cite L-9901.

> **BOXED CAVEAT (scope of L-9907.3) — with a correction to the folklore phrasing.**
>
> The pigeonhole argument above uses exactly two ingredients:
> (P1) the orbit is a *single deterministic orbit* of one fixed starting point, and
> (P2) the orbit lies in a fixed ambient set $S$ such that $S \cap [0, B]$ is **finite**
> for every real $B$ (here $S = \mathbb{Z}^+$).
> Where either ingredient fails, "unbounded $\Rightarrow$ divergent" is **not available**
> and must not be invoked.
>
> **Correction (flagged).** The tasked/folklore form of this caveat asserts that "in
> $\mathbb{Q}$ an unbounded orbit need not tend to $\infty$." As stated, that is
> *incorrect for genuine single $T$-orbits*: extend $T$ to positive rationals with odd
> denominator by reading parity 2-adically (for $x = p/q$ in lowest terms with $q$ odd,
> $x \equiv p \pmod 2$ in $\mathbb{Z}_2$ since $q^{-1}$ is odd). Then along any orbit the
> denominators divide the initial denominator $q$: if $p$ is even,
> $T(x) = (p/2)/q$; if $p$ is odd, $T(x) = \frac{(3p+q)/2}{q}$ with $3p + q$ even — in
> both cases the new denominator divides $q$. So the orbit stays in
> $\tfrac1q\mathbb{Z} \cap (0,\infty)$, which satisfies (P2), and the pigeonhole proof
> goes through verbatim: *for a single $T$-orbit of a positive odd-denominator rational,
> unbounded still implies divergent.* (Finite check: Test 6 below.)
>
> The caveat's **genuine** failure modes, which are the ones that matter for this
> project, are:
> 1. **$\mathbb{Z}_2$-points not proven rational.** $T$ extends continuously to
>    $\mathbb{Z}_2$, but an element of $\mathbb{Z}_2 \setminus \mathbb{Q}$ has no
>    archimedean absolute value at all; "bounded", "unbounded", and "$\to \infty$" are
>    statements about real magnitudes that do not exist for such points. L-9907.3 is not
>    even well-posed there.
> 2. **Symbolic or diagonal constructions that are not one orbit.** A sequence
>    $(x_k)$ assembled from *different* integer orbits (e.g. $x_k$ an iterate of some
>    $n_k$ depending on $k$, or a limit of finite parity-prefix solutions) violates (P1):
>    determinism no longer propagates a coincidence $x_{k_1} = x_{k_2}$ forward, so
>    "some value twice $\Rightarrow$ eventually periodic" fails, and unboundedness of
>    $(x_k)$ implies nothing about divergence of any actual orbit.
> 3. **Unproven integrality.** Any construction whose "orbit values" are not proven to
>    lie in $\mathbb{Z}^+$ (or at least in a fixed $\tfrac1q\mathbb{Z}$) violates (P2).
>
> **Operational rule:** a symbolic / 2-adic / limiting construction may use L-9907.3
> only after proving that its object is the honest $T$-orbit of a single positive
> integer (or of a single positive rational with fixed odd denominator). Without such an
> integrality proof, only L-9907.1 and L-9907.2 (suitably re-derived in the relevant
> setting) are available, and "unbounded" may not be upgraded to "divergent".

### L-9907.4 — two-sided summary, refinement, and the open boundary

**Summary chain.** Let $n \in \mathbb{Z}^+$.
- If $\liminf_k a_k/k > \gamma$, then $T^k(n) \to \infty$ by L-9907.1(ii).
- If $T^k(n) \to \infty$, then $\liminf_k a_k/k \ge \gamma$ by L-9907.2.
- If $\limsup_k a_k/k > \gamma$, then the orbit is unbounded by L-9907.1(i), hence
  divergent by L-9907.3 (this step is $\mathbb{Z}^+$-specific), hence
  $\liminf_k a_k/k \ge \gamma$ by L-9907.2.

**Corollary (self-improvement, $\mathbb{Z}^+$ only).** For $n \in \mathbb{Z}^+$:
$\limsup_k a_k/k > \gamma \Rightarrow \liminf_k a_k/k \ge \gamma$. (Immediate from the
third chain.) $\square$

**L-9907.4-R (growth-rate refinement; proved).** Dividing the exact identity (2.1) by
$k \log_2 3$ and using $1/\log_2 3 = \gamma$ gives, for every $k \ge 1$, the exact identity
$$\frac{a_k}{k} \;=\; \gamma \;+\; \gamma\,\frac{\log_2 T^k(n)}{k}
\;-\; \gamma\,\frac{\log_2 n + E_k}{k}. \tag{4.1}$$
Now assume $T^k(n) \to \infty$. Then $E_k / k \to 0$: indeed for each $\delta \in (0,1)$,
(2.2) gives $0 \le E_k/k \le E_{t_0}/k + \delta$ for $k \ge t_0(\delta,n)$, so
$\limsup_k E_k/k \le \delta$; letting $\delta \downarrow 0$, $\lim_k E_k/k = 0$. Hence
the third term of (4.1), $y_k := \gamma(\log_2 n + E_k)/k$, tends to $0$. Both remaining
sequences in (4.1) are bounded for large $k$ ($a_k/k \in [0,1]$; hence
$\gamma + \gamma \log_2 T^k(n)/k = a_k/k + y_k$ is bounded), so the standard sandwich
applies: for $\eta > 0$ and all large $k$, $|y_k| \le \eta$, so
$$\gamma + \gamma\frac{\log_2 T^k(n)}{k} - \eta \;\le\; \frac{a_k}{k}
\;\le\; \gamma + \gamma\frac{\log_2 T^k(n)}{k} + \eta,$$
whence $\big|\liminf_k a_k/k - \gamma - \gamma \liminf_k (\log_2 T^k(n))/k\big| \le \eta$
and likewise for $\limsup$; letting $\eta \downarrow 0$:
$$\liminf_k \frac{a_k}{k} = \gamma\Big(1 + \liminf_k \frac{\log_2 T^k(n)}{k}\Big),
\qquad
\limsup_k \frac{a_k}{k} = \gamma\Big(1 + \limsup_k \frac{\log_2 T^k(n)}{k}\Big).
\tag{4.2}$$
Since divergence and integrality give $\log_2 T^k(n) \ge 0$ eventually, (4.2) re-proves
L-9907.2; and it shows: *for a divergent integer orbit,*
$$\liminf_k \frac{a_k}{k} = \gamma
\iff \liminf_k \frac{\log_2 T^k(n)}{k} = 0
\quad (\text{subexponential growth along a subsequence}),$$
$$\liminf_k \frac{a_k}{k} > \gamma
\iff \liminf_k \frac{\log_2 T^k(n)}{k} > 0
\quad (\text{uniform exponential growth}). \qquad \square$$

**Q-9902 (open question; recorded, not answered).**
*Does there exist a divergent integer $T$-orbit, and if so, must it have
$\liminf_k a_k(n)/k = \gamma$, or can the liminf exceed $\gamma$?*
By L-9907.4-R this is equivalent to: can a divergent integer orbit grow at a uniform
exponential rate, or is every divergent orbit (if any exists) subexponential along some
subsequence? The methods of this file bound the boundary from both sides
($> \gamma$ suffices, $\ge \gamma$ is necessary) but are structurally incapable of
resolving the case $\liminf = \gamma$: L-9907.1 needs strict excess to force growth, and
L-9907.2 produces no strict inequality. **Status: OPEN. No answer is asserted or
conjectured here.**

### L-9907.5 — glider lemma: long rises on explicit residue classes

**Forward direction and formula.** Claim: for all $j \ge 1$, if
$n \equiv -1 \pmod{2^j}$ (equivalently $2^j \mid n+1$; equivalently
$n \equiv 2^j - 1 \pmod{2^j}$), then
$$v_0(n) = \dots = v_{j-1}(n) = 1 \qquad\text{and}\qquad
T^j(n) = \frac{3^j(n+1)}{2^j} - 1. \tag{5.1}$$
(Note $\tfrac{n+1}{2^j} \in \mathbb{Z}^+$ by hypothesis, so the formula is an integer
identity.) Induction on $j$:

*Base $j = 1$:* $n \equiv -1 \equiv 1 \pmod 2$ is odd, so $v_0 = 1$, and writing
$n = 2m - 1$ ($m = \tfrac{n+1}{2} \in \mathbb{Z}^+$):
$T(n) = \tfrac{3n+1}{2} = \tfrac{6m - 2}{2} = 3m - 1 = \tfrac{3(n+1)}{2} - 1$. Matches (5.1).

*Step $j \to j+1$:* let $n \equiv -1 \pmod{2^{j+1}}$ and write $n + 1 = 2^{j+1} m$,
$m \in \mathbb{Z}^+$. Then also $n \equiv -1 \pmod{2^j}$, so by the induction hypothesis
$v_0 = \dots = v_{j-1} = 1$ and
$$T^j(n) = \frac{3^j (n+1)}{2^j} - 1 = 3^j \cdot 2m - 1,$$
which is odd; hence $v_j(n) = 1$ and
$$T^{j+1}(n) = \frac{3\,(3^j 2m - 1) + 1}{2} = \frac{3^{j+1}\cdot 2m - 2}{2}
= 3^{j+1} m - 1 = \frac{3^{j+1}(n+1)}{2^{j+1}} - 1.$$
This is (5.1) for $j + 1$. $\square$

**Converse (the run of $j$ ones occurs for exactly this class).** Claim: if
$v_0(n) = \dots = v_{j-1}(n) = 1$ then $n \equiv -1 \pmod{2^j}$. Induction on $j$:

*Base $j = 1$:* $v_0 = 1$ means $n$ odd, i.e. $n \equiv 1 \equiv -1 \pmod 2$.

*Step:* suppose the claim holds for $j$ and let $v_0 = \dots = v_j = 1$. By the induction
hypothesis $n \equiv -1 \pmod{2^j}$, so by (5.1) $T^j(n) = 3^j\,\tfrac{n+1}{2^j} - 1$.
Since $v_j = 1$, $T^j(n)$ is odd, so $3^j \tfrac{n+1}{2^j}$ is even; as $3^j$ is odd,
$\tfrac{n+1}{2^j}$ is even, i.e. $2^{j+1} \mid n + 1$: $n \equiv -1 \pmod{2^{j+1}}$.
$\square$

Together: for every $j \ge 1$,
$v_0 = \dots = v_{j-1} = 1 \iff n \equiv -1 \pmod{2^j} \iff \nu_2(n+1) \ge j$;
and the *maximal* initial all-ones run has length exactly $\nu_2(n+1)$.

**Corollaries.**
1. $n = 2^j - 1$ (the class member with $\tfrac{n+1}{2^j} = 1$):
   $T^j(2^j - 1) = 3^j - 1$.
2. Rise factor: for $n \equiv -1 \pmod{2^j}$,
   $T^j(n) = \big(\tfrac32\big)^j (n+1) - 1
   = \big(\tfrac32\big)^j n + \big(\tfrac32\big)^j - 1 > \big(\tfrac32\big)^j n$,
   since $(3/2)^j > 1$. (Consistent with the L-9907.1 envelope at $a_j = j$, which gives
   exactly $T^j(n) \ge (3/2)^j n$; the glider classes achieve it within an additive
   constant.)
3. For every $j$, the class $\{n \in \mathbb{Z}^+ : n \equiv 2^j - 1 \pmod{2^j}\}$ is
   infinite (natural density $2^{-j}$), so arbitrarily long all-ones parity runs and
   rises by a factor $> (3/2)^j$ occur among positive integers, on those explicit
   classes and only on them.

**Remark (the tension with L-9907.2 — the precise gap).** L-9907.5 shows *long rises are
abundant*: for any $j$, a positive-density set of integers rises by more than $(3/2)^j$
in its first $j$ steps, with parity density $a_j/j = 1 > \gamma$ on that window. But
L-9907.1/2 show that divergence is governed by the *asymptotic* density: a divergent
orbit must keep $a_k/k \ge \gamma - o(1)$ for **all** large $k$, not merely on bursts.
After a glider window the orbit sits at $3^j m - 1$ with $m = \tfrac{n+1}{2^j}$, and
nothing in L-9907.5 controls the parities after step $j$; empirically (Test 5,
observational only) the density decays toward $1/2 < \gamma$ for every tested start. The
precise gap every divergence-hunting construction (issues #4/M1, #8, #10, #21) must
close is exactly this: *not* producing long rises (easy, explicit, classified above),
but proving that a single integer orbit sustains odd-step density $\ge \gamma$ in the
liminf forever — equivalently (L-9907.4-R), sustains a nonnegative exponential growth
rate. Concatenating glider windows requires re-entering classes
$\equiv -1 \pmod{2^{j'}}$ infinitely often with sufficient $j'$, and no mechanism for
forcing that along one orbit is provided by this file.

---

## Dependency audit

Used from `NOTATION.md` (the only file dependency):
- **D-9902** (shortcut map $T$): every sub-claim; specifically the two branches of $T$ in
  L-9907.1 (inductive step), L-9907.2 (Step 1), L-9907.3 (determinism of $T$ and
  $T(\mathbb{Z}^+) \subseteq \mathbb{Z}^+$), L-9907.5 (both inductions).
- **D-9906** ($v_i$, $a_k$): statements and proofs throughout; $a_0 = 0$ (empty sum
  convention, NOTATION Conventions) in the base case of L-9907.1.
- **D-9907** (bounded/unbounded/divergent): conclusions of L-9907.1(i)/(ii), hypothesis
  of L-9907.2 (Step 4 uses the definition of $\to\infty$ verbatim), the dichotomy of
  L-9907.3.
- **D-9905 / D-9908** (trivial/nontrivial cycles): only in the *remark* relating
  L-9907.3 to L-9901; not load-bearing.

External mathematical facts used (all elementary, proved or referenced inline):
- (F1)/(F2), the subsequence characterizations of $\limsup$/$\liminf$: one-line proofs
  given inside L-9907.1(i)/(ii).
- The sandwich argument for $\liminf/\limsup$ under an $o(1)$ perturbation:
  proved inline in L-9907.4-R.
- Strict monotonicity of $\log_2$; pigeonhole on finite sets; division with remainder
  (L-9907.3); induction.

Overlaps with parallel foundations files (per NOTATION.md Conventions, re-derived here
because those files may land later): L-9901 (trichotomy) overlaps L-9907.3 — proof given
inline, no citation load; L-9903 overlaps the envelope/telescoping material of
L-9907.1–.2 — likewise inline. No circular dependence: this file cites no result of
L-9901 or L-9903.

Namespace note: T-9602 (issue #21) is cited in Motivation only, as context; no statement
of T-9602 is assumed anywhere in the proofs.

---

## Gap audit

Checklist per README §8, item by item:

- **Hidden finiteness assumptions.** The only finiteness-sensitive step is the
  pigeonhole in L-9907.3; it is isolated, and its exact requirements (P1), (P2) are
  stated in the boxed caveat, including the corrected analysis for odd-denominator
  rationals and the genuine failure modes ($\mathbb{Z}_2\setminus\mathbb{Q}$, diagonal
  constructions, unproven integrality). $E_{t_0} < \infty$ in L-9907.2 Step 4 is proved
  with an explicit bound ($\le t_0 \log_2(4/3)$), not assumed.
- **Unjustified induction / base cases.** Three inductions (L-9907.1 envelope; L-9907.5
  forward; L-9907.5 converse) each display their base case and step. The auxiliary
  induction in L-9907.3 (determinism propagation) states base and step.
- **Boundary cases.** $k = 0$ and $a_0 = 0$ (envelope, equality); $k = t_0$ (empty sum
  in (2.2)); $n = 1$ and the trivial cycle (hypotheses of L-9907.2 simply fail; no claim
  made); $j = 1$ base of L-9907.5; $x = 1$ attains $\varepsilon = \log_2(4/3)$
  (endpoint of the $\varepsilon$-range is closed on the right, open on the left —
  checked). The boundary $\liminf = \gamma$ is explicitly excluded from all claims and
  quarantined in Q-9902.
- **Empirical vs. universal.** All computational content is confined to the Adversarial
  tests section and labeled finite verification; Test 5 is additionally labeled
  observational. No proof step cites a computation.
- **Invalid interchange of limits.** The $\delta$/$k$ order in L-9907.2 is discussed
  explicitly (Step 8): the $k$-liminf is completed for each fixed $\delta$ before the
  supremum over $\delta$; no interchange occurs. In L-9907.4-R the sandwich is applied
  to bounded sequences with a genuine $o(1)$ term, with the $\eta$-argument written out.
- **Circular dependence.** None: only NOTATION.md definitions are consumed; L-9901/L-9903
  overlaps are re-proved, not cited.
- **Nonuniform estimates.** All constants carry their dependencies in their names:
  $M(\delta)$, $t_0(\delta, n)$, $C(\delta, n)$; (2.3)–(2.4) hold for all $k \ge
  t_0(\delta,n)$ with $C$ independent of $k$. Nothing is claimed uniform in $n$.
- **Assumptions equivalent to the conjecture.** None; no claim here decides whether
  divergent orbits exist (Q-9902 records precisely this neutrality, per D-9909's
  neutrality requirement).
- **Incorrectly assumed independence.** No probabilistic reasoning is used anywhere;
  the heuristic "random parity" picture is deliberately absent from the proofs.
- **Unproved properties of infinite objects / finite-to-infinite extrapolation.**
  The only infinite-behavior claims (L-9907.1(ii), L-9907.2, L-9907.3) are proved by
  explicit $\forall k \ge k_0$ estimates, not by extrapolation. L-9907.5 is a
  finite-window statement and is labeled as such in the tension remark.
- **Symbolic object vs. integer trajectory.** This is the entire content of the boxed
  caveat; the operational rule there is the safeguard.
- **Known slip risks specific to this file** (searched for deliberately):
  (1) $\limsup$ vs. $\liminf$ in L-9907.1 — (i) yields only unboundedness, (ii) yields
  divergence; the note after (i) flags that (i) alone does not give divergence.
  (2) The direction of (2.2) requires *every* odd index in the tail to be large —
  unboundedness would not suffice; flagged at the end of L-9907.2.
  (3) In L-9907.4's third chain, the use of L-9907.3 makes it $\mathbb{Z}^+$-specific;
  flagged in the statement and the chain.

---

## Adversarial tests

Finite verification only — none of the following is a proof. Exact claims are tested in
exact rational/integer arithmetic (`fractions.Fraction`, Python arbitrary-precision
`int`); floating point appears only in cross-checks of logarithmic forms with explicit
tolerances, and in the observational density table. Random seed fixed: `99071`.
Environment: CPython 3.x, standard library only. Script also stored at the session
scratchpad as `l9907_tests.py`.

```python
#!/usr/bin/env python3
# Adversarial tests for L-9907 (finite verification, NOT proof).
# Agent: fable-02-p6. Exact arithmetic via fractions.Fraction where the claim is exact;
# floats used only for cross-checks of logarithmic forms, with explicit tolerances.

from fractions import Fraction
import math
import random

random.seed(99071)

LOG2_3 = math.log2(3)
GAMMA = 1 / LOG2_3  # log_3 2


def T_int(n: int) -> int:
    """Shortcut (Terras) map on Z+ (D-9902)."""
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def orbit_and_parities(n: int, k: int):
    """Return xs = [T^0(n), ..., T^k(n)] and vs = [v_0, ..., v_{k-1}]."""
    xs = [n]
    vs = []
    for _ in range(k):
        vs.append(xs[-1] % 2)
        xs.append(T_int(xs[-1]))
    return xs, vs


# ---------------------------------------------------------------------------
# Test 1 — exact multiplicative telescoping identity + lower envelope.
# Claim (exponentiated form of the L-9907.2 telescoping identity, exact in Q):
#   T^k(n) * 2^k == n * 3^{a_k} * prod_{i<k, v_i=1} (1 + 1/(3 T^i(n)))
# and the L-9907.1 lower envelope, exact in Q:
#   T^k(n) >= 3^{a_k} * n / 2^k.
# Float cross-check of the log form:
#   log2 T^k(n) - log2 n == a_k*log2(3) - k + E_k   (tolerance 1e-6).
# ---------------------------------------------------------------------------
def test_telescoping(trials: int = 300) -> None:
    for _ in range(trials):
        n = random.randint(1, 10**12)
        k = random.randint(1, 200)
        xs, vs = orbit_and_parities(n, k)
        ak = sum(vs)
        prod = Fraction(1)
        for i in range(k):
            if vs[i] == 1:
                prod *= 1 + Fraction(1, 3 * xs[i])
        assert Fraction(xs[k]) * 2**k == Fraction(n) * 3**ak * prod, (n, k)
        assert Fraction(xs[k]) >= Fraction(3**ak * n, 2**k), (n, k)
        E_k = sum(math.log2(1 + 1 / (3 * xs[i])) for i in range(k) if vs[i] == 1)
        lhs = math.log2(xs[k]) - math.log2(n)
        rhs = ak * LOG2_3 - k + E_k
        assert abs(lhs - rhs) < 1e-6, (n, k, lhs - rhs)
        assert 0 <= E_k <= ak * math.log2(4 / 3) + 1e-12, (n, k)
    print(f"Test 1 PASS: exact telescoping identity, exact lower envelope, and float "
          f"log-form (tol 1e-6) for {trials} random (n,k), n <= 10^12, k <= 200.")


# ---------------------------------------------------------------------------
# Test 2 — glider lemma L-9907.5, j <= 20, across residues, plus exact converse:
#   n == -1 (mod 2^j)  ==>  v_0 = ... = v_{j-1} = 1 and T^j(n) = 3^j (n+1)/2^j - 1;
#   maximal initial all-ones run == nu_2(n+1).
# ---------------------------------------------------------------------------
def test_glider(jmax: int = 20) -> None:
    for j in range(1, jmax + 1):
        ms = [1, 2, 3, 5, 1000] + random.sample(range(1, 10**6), 25)
        for m in ms:
            n = m * 2**j - 1
            xs, vs = orbit_and_parities(n, j)
            assert all(v == 1 for v in vs), (j, m)
            assert xs[j] == 3**j * (n + 1) // 2**j - 1, (j, m)
    # Converse / exactness: initial all-ones run length equals nu_2(n+1).
    for _ in range(3000):
        n = random.randint(1, 10**9)
        xs, vs = orbit_and_parities(n, 40)
        r = 0
        while r < 40 and vs[r] == 1:
            r += 1
        nu = 0
        t = n + 1
        while t % 2 == 0:
            nu += 1
            t //= 2
        assert r == min(nu, 40), (n, r, nu)
    print(f"Test 2 PASS: glider identity for j <= {jmax} over 30 residue-class members "
          f"each; initial 1-run == nu_2(n+1) for 3000 random n <= 10^9.")


# ---------------------------------------------------------------------------
# Test 3 — T^j(2^j - 1) = 3^j - 1 for j <= 25 (exact integers).
# ---------------------------------------------------------------------------
def test_mersenne(jmax: int = 25) -> None:
    for j in range(1, jmax + 1):
        n = 2**j - 1
        xs, _ = orbit_and_parities(n, j)
        assert xs[j] == 3**j - 1, j
    print(f"Test 3 PASS: T^j(2^j - 1) == 3^j - 1 exactly for 1 <= j <= {jmax}.")


# ---------------------------------------------------------------------------
# Test 4 — explicit M(delta) from L-9907.2: M = ceil(1/(3(2^delta - 1)))
# satisfies log2(1 + 1/(3M)) <= delta.
# ---------------------------------------------------------------------------
def test_M_delta() -> None:
    for delta in [0.5, 0.1, 0.01, 0.001, 0.0001]:
        M = math.ceil(1 / (3 * (2**delta - 1)))
        eps_M = math.log2(1 + 1 / (3 * M))
        assert M >= 1 and eps_M <= delta, (delta, M, eps_M)
        print(f"  delta = {delta:<7} -> M(delta) = {M:>6}, "
              f"log2(1 + 1/(3M)) = {eps_M:.6f} <= delta: OK")
    print("Test 4 PASS: explicit M(delta) works for sampled delta.")


# ---------------------------------------------------------------------------
# Test 5 (OBSERVATIONAL, not part of any proof) — a_k/k along some orbits.
# Convergent orbits fall into the (1,2) T-cycle, whose parity word alternates
# 1,0,1,0,..., so a_k/k -> 1/2 < gamma. This is illustration only.
# ---------------------------------------------------------------------------
def test_density_tables() -> None:
    print(f"Test 5 (OBSERVATIONAL): a_k/k tables; gamma = {GAMMA:.7f}")
    starts = [27, 703, 2**30 - 1, 2**60 + 1, 10**18 + 7]
    ks = [10, 100, 1000, 10000, 100000]
    for n in starts:
        x = n
        a = 0
        row = []
        kmax = ks[-1]
        checkpoints = set(ks)
        for k in range(1, kmax + 1):
            a += x % 2
            x = T_int(x)
            if k in checkpoints:
                row.append((k, a / k))
        cells = ", ".join(f"a_{k}/{k} = {r:.4f}" for k, r in row)
        print(f"  n = {n}: {cells}")
    n = 2**30 - 1
    xs, vs = orbit_and_parities(n, 60)
    a = 0
    peaks = []
    for k in range(1, 61):
        a += vs[k - 1]
        if k in (10, 20, 30, 31, 40, 60):
            peaks.append((k, a / k))
    print(f"  glider n = 2^30 - 1, early window: "
          + ", ".join(f"a_{k}/{k} = {r:.4f}" for k, r in peaks))
    print("  (all-ones prefix of length exactly 30, then density decays: observational)")


# ---------------------------------------------------------------------------
# Test 6 — fixed-denominator remark in the L-9907.3 caveat box: T extends to
# positive rationals with odd denominator (parity := numerator parity in lowest
# terms); denominators along an orbit divide the initial denominator. Example
# rational cycle 1/5 -> 4/5 -> 2/5 -> 1/5 (exact Fractions).
# ---------------------------------------------------------------------------
def T_rat(x: Fraction) -> Fraction:
    assert x.denominator % 2 == 1
    if x.numerator % 2 == 0:
        return x / 2
    return (3 * x + 1) / 2


def test_rational_remark() -> None:
    x = Fraction(1, 5)
    seq = [x]
    for _ in range(6):
        seq.append(T_rat(seq[-1]))
    assert seq[3] == Fraction(1, 5) and seq[1] == Fraction(4, 5) \
        and seq[2] == Fraction(2, 5)
    for _ in range(500):
        q = random.choice([3, 5, 7, 9, 15, 21, 33, 45])
        p = random.randint(1, 10**6)
        x = Fraction(p, q)
        for _ in range(200):
            assert q % x.denominator == 0, (p, q, x)
            x = T_rat(x)
    print("Test 6 PASS: rational cycle (1/5, 4/5, 2/5) exact; along 500 random "
          "odd-denominator orbits (200 steps), denominators always divide q.")


if __name__ == "__main__":
    test_telescoping()
    test_glider()
    test_mersenne()
    test_M_delta()
    test_density_tables()
    test_rational_remark()
    print("ALL TESTS PASS (finite verification only; no test is a proof).")
```

Output (command: `python3 l9907_tests.py`), verbatim:

```text
Test 1 PASS: exact telescoping identity, exact lower envelope, and float log-form (tol 1e-6) for 300 random (n,k), n <= 10^12, k <= 200.
Test 2 PASS: glider identity for j <= 20 over 30 residue-class members each; initial 1-run == nu_2(n+1) for 3000 random n <= 10^9.
Test 3 PASS: T^j(2^j - 1) == 3^j - 1 exactly for 1 <= j <= 25.
  delta = 0.5     -> M(delta) =      1, log2(1 + 1/(3M)) = 0.415037 <= delta: OK
  delta = 0.1     -> M(delta) =      5, log2(1 + 1/(3M)) = 0.093109 <= delta: OK
  delta = 0.01    -> M(delta) =     48, log2(1 + 1/(3M)) = 0.009984 <= delta: OK
  delta = 0.001   -> M(delta) =    481, log2(1 + 1/(3M)) = 0.000999 <= delta: OK
  delta = 0.0001  -> M(delta) =   4809, log2(1 + 1/(3M)) = 0.000100 <= delta: OK
Test 4 PASS: explicit M(delta) works for sampled delta.
Test 5 (OBSERVATIONAL): a_k/k tables; gamma = 0.6309298
  n = 27: a_10/10 = 0.8000, a_100/100 = 0.5600, a_1000/1000 = 0.5060, a_10000/10000 = 0.5006, a_100000/100000 = 0.5001
  n = 703: a_10/10 = 0.8000, a_100/100 = 0.6000, a_1000/1000 = 0.5080, a_10000/10000 = 0.5008, a_100000/100000 = 0.5001
  n = 1073741823: a_10/10 = 1.0000, a_100/100 = 0.6500, a_1000/1000 = 0.5190, a_10000/10000 = 0.5019, a_100000/100000 = 0.5002
  n = 1152921504606846977: a_10/10 = 0.5000, a_100/100 = 0.5200, a_1000/1000 = 0.5040, a_10000/10000 = 0.5004, a_100000/100000 = 0.5000
  n = 1000000000000000007: a_10/10 = 0.5000, a_100/100 = 0.5300, a_1000/1000 = 0.4950, a_10000/10000 = 0.4995, a_100000/100000 = 0.5000
  glider n = 2^30 - 1, early window: a_10/10 = 1.0000, a_20/20 = 1.0000, a_30/30 = 1.0000, a_31/31 = 0.9677, a_40/40 = 0.8250, a_60/60 = 0.7333
  (all-ones prefix of length exactly 30, then density decays: observational)
Test 6 PASS: rational cycle (1/5, 4/5, 2/5) exact; along 500 random odd-denominator orbits (200 steps), denominators always divide q.
ALL TESTS PASS (finite verification only; no test is a proof).
```

Interpretation and limitations: Tests 1–3 and 6 verify *exact* finite instances of
proved identities/inequalities (they could only expose an error, never establish the
universal claims); Test 4 checks the explicit constant of L-9907.2 Step 3 at sample
points; Test 5 is purely observational — the approach of $a_k/k$ to $1/2$ reflects the
tested orbits entering the trivial cycle $(1,2)$ (alternating parity), and says nothing
about hypothetical divergent orbits.

---

## Remaining uncertainty

1. **The correction inside the boxed caveat** (odd-denominator rationals: denominators
   divide $q$ along the orbit, so the pigeonhole survives) departs from the folklore
   phrasing I was handed. I re-derived it from scratch (the two-case denominator
   computation, plus the parity convention $x \equiv p \pmod 2$ for $q$ odd) and checked
   it finitely (Test 6), but a reviewer should re-verify the lowest-terms bookkeeping —
   in the odd case the new denominator can be $q/3$ rather than $q$ (when $3 \mid q$ and
   cancellation occurs), which still divides $q$, as used. If the reviewer disagrees,
   the safe fallback is to weaken the box back to "unavailable outside $\mathbb{Z}^+$",
   which only *strengthens* the warning and touches nothing else in the file.
2. In L-9907.2 I state the quantitative bound (2.3) "for all $k \ge t_0(\delta,n)$" with
   $C(\delta,n) = \log_2 n + E_{t_0}$; a reviewer should confirm the $k = t_0$ edge
   (empty second sum in (2.2)) and that no step silently required $k > t_0$.
3. The standard limsup/liminf facts (F1), (F2) and the sandwich in L-9907.4-R are proved
   inline in one or two lines each; these are the likeliest places for a quantifier slip
   and deserve a targeted re-read.
4. L-9901 and L-9903 had not landed in `research/foundations/` at the time of writing;
   the "Related" pointers may need path/ID reconciliation by the integrator once those
   files exist. Nothing in the proofs depends on them.
5. Motivation-section claims about issues #21 (T-9602), #4/M1, #8, #10 are contextual
   pointers supplied with the task assignment, not verified against those threads by me;
   they carry no logical weight in this file.

I am confident in the mathematics of L-9907.1–.5 as stated; they are classical in
substance, and every step is elementary and written out.

---

## Suggested next attack

1. **Verification path to PROVED.** An independent agent should reconstruct L-9907.2
   from (2.1) alone without reading Steps 3–8, then diff against this file; the
   $\varepsilon$-management (Steps 3–6) is where a hidden nonuniformity would live.
   Computationally: instrument random large orbits and check (2.3) with the explicit
   $t_0, C$ for several $\delta$ (a direct falsification harness for the constants).
2. **Exploit L-9907.4-R.** Divergence programs should declare which regime they target:
   $\liminf a_k/k > \gamma$ forces *uniform exponential growth* of the candidate orbit —
   a much stronger structural demand than divergence itself — while the boundary regime
   $\liminf = \gamma$ (subexponential divergence along a subsequence) is untouched by
   the supercritical criterion. A useful next lemma: quantitative excursion control —
   from (2.1), bound how far and how long $a_k/k$ can dip below $\gamma$ during a finite
   window of a divergent orbit in terms of the loss in $\log_2 T^k(n)$.
3. **Attack Q-9902's second half.** Try to prove: if a divergent orbit exists, then
   some divergent orbit has $\liminf a_k/k = \gamma$ (e.g. by a compactness/diagonal
   argument in parity space) — or refute that approach by locating exactly where the
   caveat box (failure mode 2) blocks it. Either outcome sharpens the target.
4. **Strengthen L-9907.5 toward concatenation.** Characterize, for $n \equiv -1
   \pmod{2^j}$, the residue data of $T^j(n) = 3^j m - 1$ that controls the *next*
   all-ones run, i.e. $\nu_2(3^j m)$-type conditions on $m$; a self-sustaining recursion
   here is precisely what failure mode 2 of the caveat requires to be realized by a
   single integer, and is the natural bridge from this file to the divergence programs.
5. **Refute-fast filter.** Wire L-9907.2 into candidate triage: any proposed divergent
   candidate whose claimed parity statistics have $\liminf a_k/k < \gamma$ is refuted on
   the spot; automate this check against the `K-` candidate files.

---

Signed: fable-02-p6, 2026-07-21.
