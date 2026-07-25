# L-9919 — The odd-preimage descent map, descent depth $\nu_3(y+1)$, and the joint $2$-adic/$3$-adic survivor sieve

```text
Claim ID: L-9919
Title: The odd T-preimage descent map D(y) = (2y-1)/3, its exact iterate
       D^d(y) = 2^d(y+1)/3^d - 1, the descent depth d(y) = nu_3(y+1), the amplified
       orbit floor for the minimal counterexample, and the resulting joint sieve
       modulo 2^k * 3^D — with an exact measurement of how much it improves on L-9909
Status: PROPOSED
Authoring agent: fable-02-p13
Reviewing agents: (none yet)
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: research/foundations/NOTATION.md (D-9901 C, D-9902 T, D-9905 orbits,
              D-9906 parity vector, D-9909 counterexample, D-9910 stopping time);
              L-9902 (PROVED) — parity word of n depends only on n mod 2^k, and
                pi_k : Z/2^k -> {0,1}^k is a bijection;
              L-9903 (PROVED) — affine iteration formula T^k(n) = (3^{a_k} n + rho_k)/2^k
                with rho_k a function of the parity word only;
              L-9909 (PROVED) — L-9909.2(E)/(M) (counterexample closure under
                n -> (2n-1)/3, and mu odd, mu = 3 mod 4, sigma(mu) = infinity), the
                uniform-descent survivor sieve mod 2^k, its bounds B_k, and X-9901
                (every n <= 10^6 reaches 1);
              L-9911 (PROVED) — U2 (two-sided closure of the counterexample set),
                U3 (T-preimage characterization), L-9911.1 (orbit floor), L-9911.3
                (record-word disjunction);
              L-9907 (PROVED) — L-9907.5 (the identity T^j(n) = 3^j(n+1)/2^j - 1 on
                all-ones words) and L-9907.2 (divergence forces liminf a_k/k >= gamma),
                used only in the "no improvement" statements of L-9919.6.
Scope: Everything about the maps D, T, C and about residue classes is UNCONDITIONAL.
       Everything about mu (the minimal counterexample) is CONDITIONAL on the standing
       hypothesis (H) below and is labelled [H]. Computations are exact finite
       computations over explicitly stated finite ranges and are labelled as such;
       they are never proof of an infinite statement. Sub-claim L-9919.8 is an
       exploratory EXTENSION whose soundness is proved but whose computational
       characterisation is finite-range only.
Related counterexample candidates: none
```

Notation is exactly `research/foundations/NOTATION.md`. Throughout,
$\mathbb{Z}^+ = \{1,2,3,\dots\}$, $T$ is the shortcut map (D-9902), $C$ the Collatz map
(D-9901), $v_i(n) = T^i(n) \bmod 2$ and $a_k(n) = \sum_{i<k} v_i(n)$ (D-9906),
$\sigma$ the stopping time (D-9910), $\gamma := \log_3 2 \approx 0.6309298$,
$\nu_2, \nu_3$ the $2$-adic and $3$-adic valuations, and $\rho_k(n)$ the remainder of
L-9903. We write $\nu_3(0) := +\infty$.

---

## Standing hypothesis

> **(H)** — **ASSUME** the counterexample set
> $$X \;:=\; \{\, n \in \mathbb{Z}^+ : 1 \notin O_C(n) \,\}$$
> (D-9909) is **nonempty**, and let $\mu := \min X$ (well defined by well-ordering).
>
> Every statement tagged **[H]** below is conditional on (H). This file does **not**
> assert, and must not be cited as evidence, that $X \neq \varnothing$. All statements
> **not** tagged [H] are unconditional facts about $T$, $C$, residue classes and finite
> computations, true whether or not (H) holds.

---

## Statement

### L-9919.1 (the descent map)

Define the **descent map** $D$ on $\{\,y \in \mathbb{Z}^+ : y \equiv 2 \pmod 3\,\}$ by
$$D(y) \;:=\; \frac{2y-1}{3}.$$

For every $y \in \mathbb{Z}^+$:

1. **(Integrality iff.)** $\dfrac{2y-1}{3} \in \mathbb{Z} \iff y \equiv 2 \pmod 3$.
2. **(Shape.)** If $y \equiv 2 \pmod 3$ then $D(y) \in \mathbb{Z}^+$, $D(y)$ is **odd**,
   $T(D(y)) = y$, and $D(y) < y$. (Both $D(y) \ge 1$ and $D(y) < y$ hold for **every**
   $y \in \mathbb{Z}^+$ with $y \equiv 2 \bmod 3$; no lower bound on $y$ is needed. The
   least such $y$ is $y = 2$, with $D(2) = 1$.)
3. **(Complete preimage set; = L-9911 U3, restated.)**
   $$T^{-1}(y) \cap \mathbb{Z}^+ \;=\; \{2y\} \cup \begin{cases} \{D(y)\} & y \equiv 2 \pmod 3,\\ \varnothing & \text{otherwise.}\end{cases}$$
   $2y$ is even and $D(y)$ (when present) is odd, so the two are always distinct.
   Degenerate cases: $T^{-1}(1) = \{2\}$ (since $1 \not\equiv 2 \bmod 3$);
   $T^{-1}(2) = \{1,4\}$ (since $2 \equiv 2 \bmod 3$ and $D(2) = 1$).
4. **(Closure.)** For every $y \in \mathbb{Z}^+$ with $y \equiv 2 \pmod 3$:
   $y \in X \iff D(y) \in X$. In particular if $y \in X$ then $D(y) \in X$.
5. **[H] (first consequence.)** $\mu \not\equiv 2 \pmod 3$; equivalently
   $3 \nmid \mu + 1$. Combined with L-9909.2(M)(ii) ($\mu \equiv 3 \bmod 4$):
   $$\mu \equiv 3 \ \text{ or } \ 7 \pmod{12}.$$

### L-9919.2 (descent depth is a single $3$-adic congruence)

For $y \in \mathbb{Z}^+$ define the **descent depth**
$$d(y) \;:=\; \sup\{\, d \ge 0 \;:\; D^d(y) \text{ is defined and lies in } \mathbb{Z}^+ \,\},$$
where "$D^d(y)$ is defined" means that $D$ can be applied $d$ times in succession
starting from $y$, each application being legal (its argument $\equiv 2 \bmod 3$) and
producing an element of $\mathbb{Z}^+$.

For every $y \in \mathbb{Z}^+$ and every integer $d \ge 0$:

1. **(Exact affine iterate.)** If $D^d(y)$ is defined then
   $$D^d(y) \;=\; \frac{2^d(y+1) - 3^d}{3^d} \;=\; \frac{2^d\,y - (3^d - 2^d)}{3^d} \;=\; \frac{2^d(y+1)}{3^d} - 1 .$$
   Equivalently, in the shifted coordinate $u := y+1$, $D$ is exactly multiplication
   by $2/3$: $D(y) + 1 = \tfrac{2}{3}(y+1)$.
2. **(Legality is one congruence.)** $D^d(y)$ is defined $\iff 3^d \mid (y+1)$
   $\iff y \equiv -1 \pmod{3^d}$. Hence
   $$\{\, y \in \mathbb{Z}^+ : d(y) \ge d \,\} \;=\; \{\, y : y \equiv -1 \!\!\pmod{3^d} \,\},$$
   **a single residue class mod $3^d$**, and
   $$\boxed{\,d(y) \;=\; \nu_3(y+1)\,}$$
   which is finite for every $y \in \mathbb{Z}^+$.
3. **(Positivity never binds.)** If $3^d \mid (y+1)$, write $m := (y+1)/3^d \ge 1$. Then
   $D^d(y) = 2^d m - 1 \ge 1$, and every intermediate $D^i(y)$ ($0 \le i \le d$) is
   likewise a positive integer. So the only obstruction to descending is the
   congruence in (2), never positivity.
4. **(Monotonicity and inversion.)** $D^{i+1}(y) < D^i(y)$ for $0 \le i < d(y)$, each
   $D^i(y)$ with $i \ge 1$ is odd, and $T^{\,i}\!\left(D^i(y)\right) = y$ for
   $0 \le i \le d(y)$.

*(Correction to the framing this file was assigned: the correct statement is
$d(y) = \nu_3(y+1)$ exactly — no positivity correction term appears, because the
positivity constraint is implied by the divisibility constraint. See the proof.)*

### L-9919.3 (the amplified orbit floor)

**[H]** Let $j \ge 0$, put $y := T^j(\mu)$ and $d := d(y) = \nu_3(y+1)$. Then
$D^{d}(y) \in X$, hence $D^{d}(y) \ge \mu$, i.e.
$$\boxed{\;2^{d}\,(y+1) \;\ge\; 3^{d}\,(\mu+1)\;}
\qquad\Longleftrightarrow\qquad
y \;\ge\; \Big(\tfrac{3}{2}\Big)^{d}(\mu+1) - 1
\;=\; \Big(\tfrac{3}{2}\Big)^{d}\mu \;+\; c_d, \qquad
\boxed{\,c_d = \Big(\tfrac{3}{2}\Big)^{d} - 1\,} .$$
The same inequality holds with $d$ replaced by any $0 \le i \le d(y)$ (it is weakest at
$i = 0$, where it is the known orbit floor $T^j(\mu) \ge \mu$ of L-9911.1).

**Contrapositive (sieve form).** Under (H), for every $j \ge 0$ the orbit point
$y = T^j(\mu)$ satisfies
$$\nu_3(y+1) \;\le\; \log_{3/2}\!\frac{y+1}{\mu+1}.$$
Equivalently: **$\mu$'s $T$-orbit never visits a point that is simultaneously "small
relative to $\mu$" and "$3$-adically deep"**: there is no $j$ and no $d \ge 1$ with
$$T^j(\mu) \equiv -1 \!\!\pmod{3^d} \quad\text{and}\quad T^j(\mu) < \Big(\tfrac{3}{2}\Big)^{d}(\mu+1) - 1 .$$
Taking $j = 0$ forces $d(\mu) = 0$, which is L-9919.1(5).

**Caveat (scope of the gain).** If $v_{j-1}(\mu) = \dots = v_{j-t}(\mu) = 1$ (a run of
$t$ odd steps ending at index $j$), then $D^i(T^j(\mu)) = T^{\,j-i}(\mu)$ for
$0 \le i \le t$: the first $t$ descents merely retrace the orbit backwards and give
nothing beyond L-9911.1. The new information is exactly the part of the descent that
overshoots the start of the orbit segment, i.e. the indices $i$ with $t < i \le d(y)$.

### L-9919.4 (the joint sieve)

Fix $k \ge 1$. By L-9902 the length-$k$ parity word $w = (v_0,\dots,v_{k-1})$ is a
function of the class $r = n \bmod 2^k$ alone, and so are $a_j$ and $\rho_j$
($0 \le j \le k$) by L-9903. Define the **shifted remainder**
$$\delta_j \;:=\; \rho_j + 2^j - 3^{a_j} \qquad (0 \le j \le k).$$

1. **(Shifted iteration formula.)** For every $n \in \mathbb{Z}^+$ in the class and
   every $0 \le j \le k$, writing $u := n+1$,
   $$\boxed{\;2^j\bigl(T^j(n)+1\bigr) \;=\; 3^{a_j}\,u \;+\; \delta_j\;}$$
   and $\delta_j = \sum_{i<j,\ v_i = 0} 3^{\,s_i} 2^{\,i} \ \ge 0$ with
   $s_i = \#\{l : i < l < j,\ v_l = 1\}$; recursively $\delta_0 = 0$,
   $\delta_{i+1} = 3\delta_i$ if $v_i = 1$ and $\delta_{i+1} = \delta_i + 2^i$ if
   $v_i = 0$. Moreover $\delta_j = 0 \iff v_0 = \dots = v_{j-1} = 1$.
2. **(Trichotomy for the depth condition.)** For $d \ge 0$,
   $$\nu_3\bigl(T^j(n)+1\bigr) \ge d \iff 3^d \mid \bigl(3^{a_j}u + \delta_j\bigr),$$
   and exactly one of the following holds:
   * **(U) class-uniform:** $d \le \min\bigl(a_j, \nu_3(\delta_j)\bigr)$ — the condition
     holds for **every** $n$ in the class (no information about $n \bmod 3^\bullet$ is
     used);
   * **(V) void:** $d \le a_j$ but $d > \nu_3(\delta_j)$ — the condition holds for **no**
     $n$ in the class;
   * **(N) $n$-dependent:** $d > a_j$ — the condition is solvable iff
     $3^{a_j} \mid \delta_j$, and then it is exactly the single congruence
     $u \equiv -\delta_j/3^{a_j} \pmod{3^{\,d-a_j}}$.
3. **(The descent-below-$n$ test.)** If $3^d \mid (3^{a_j}u + \delta_j)$ then
   $$D^d\bigl(T^j(n)\bigr) < n
   \iff u\bigl(2^{j}3^{d} - 2^{d}3^{a_j}\bigr) > 2^{d}\delta_j .$$
   This is satisfiable for large $n$ iff
   $$2^{j}3^{d} > 2^{d}3^{a_j} \iff \Bigl(\tfrac{3}{2}\Bigr)^{d} > \frac{3^{a_j}}{2^{j}},$$
   and then it holds exactly for
   $$n \;>\; \theta_{j,d} \;:=\; \frac{2^{d}\delta_j}{2^{j}3^{d} - 2^{d}3^{a_j}} - 1
   \;\;\Bigl(= \frac{\delta_j/3^d}{2^{\,j-d} - 3^{\,a_j-d}} - 1 \text{ when } d \le \min(a_j,j)\Bigr).$$
   Two boundary facts: $d = 0$ reproduces **exactly** the L-9909.3(b) test
   ($\theta_{j,0} = \rho_j/(2^j - 3^{a_j})$); and $d > a_j$ makes
   $2^{j}3^{d} > 2^{d}3^{a_j}$ **automatic**.
4. **(Definition of the sieve.)** Put $m_j := \min\bigl(a_j, \nu_3(\delta_j)\bigr)$.
   Call the class $r \bmod 2^k$ an **augmented $k$-survivor** if
   $$3^{\,a_j - m_j} \;\ge\; 2^{\,j - m_j} \qquad \text{for every } 0 \le j \le k$$
   (equivalently: no branch-(U) kill exists at any $j \le k$ and any
   $0 \le d \le m_j$; the test is monotone in $d$, so $d = m_j$ is the binding case).
   Taking $m_j \equiv 0$ gives back precisely the L-9909 $k$-survivor condition, so
   every augmented $k$-survivor is an L-9909 $k$-survivor.
   For $D \ge 1$, call a pair $(r \bmod 2^k,\ s \bmod 3^D)$ a **joint $(k,D)$-survivor**
   if $r$ is an augmented $k$-survivor and, in addition, no branch-(N) event at any
   $j \le k$ and $a_j < d \le D$ forbids $s$.
5. **(THE CRUX — $3$-adic collapse.)** *Unconditional.* Let $r \bmod 2^k$ be an
   augmented $k$-survivor and let $0 \le j \le k$ be such that branch (N) is nonempty
   at $j$, i.e. $3^{a_j} \mid \delta_j$. Then in fact $\nu_3(\delta_j) > a_j$, hence
   $-\delta_j/3^{a_j} \equiv 0 \pmod 3$ and every branch-(N) forbidden set at $j$ is
   contained in $\{u \equiv 0 \bmod 3\} = \{n \equiv 2 \bmod 3\}$. Consequently, for
   every $k \ge 1$ and every $D \ge 1$,
   $$\boxed{\ \text{Joint}(k,D) \;=\; \text{Aug}(k) \;\times\; \{\, s \bmod 3^D : s \not\equiv 2 \bmod 3 \,\}\ }$$
   and the joint survivor density is exactly
   $$\frac{|\text{Joint}(k,D)|}{2^k 3^D} \;=\; \frac{2}{3}\cdot\frac{|\text{Aug}(k)|}{2^k}
   \qquad \text{independently of } D .$$
   **In words: the $3$-adic direction contributes exactly one bit of information —
   the single congruence $\mu \not\equiv 2 \pmod 3$ — and nothing more, at any depth
   $D$. All further leverage of the descent is class-uniform, i.e. purely $2$-adic.**
6. **(Sieve theorem.)** *Unconditional given the exceptional bound.* Define
   $$B^{\mathrm{aug}}_k \;:=\; \max\Bigl\{\, \theta_{j,d} \;:\; \text{the first (least-}j\text{) branch-(U) kill of a class } r \bmod 2^{j},\ j \le k \,\Bigr\}
   \in \mathbb{Q}_{\ge 0},$$
   the maximum being over the finitely many classes that fail the augmented sieve at
   some level $\le k$, taking at each such class the kill with the smallest threshold.
   Then for every $n \in \mathbb{Z}^+$ with $n > B^{\mathrm{aug}}_k$: if
   $n \bmod 2^k$ is **not** an augmented $k$-survivor, then there exist $j \le k$ and
   $d \ge 0$ with $D^d(T^j(n))$ defined, a positive integer, and $< n$.
   **[H] Consequently**, for every $k \ge 1$ with $\mu > B^{\mathrm{aug}}_k$:
   $\mu \bmod 2^k$ is an augmented $k$-survivor **and** $\mu \not\equiv 2 \pmod 3$,
   i.e. $(\mu \bmod 2^k, \mu \bmod 3^D)$ is a joint $(k,D)$-survivor for every $D \ge 1$.

### L-9919.5 (exact computation)

All numbers below are exact finite computations (scripts and their real outputs are in
the Adversarial tests section). Densities of L-9909 are quoted from L-9909.4 and were
**re-derived independently here** (they matched exactly).

**(a) Survivor counts mod $2^k$.**

| $k$ | L-9909 survivors | augmented survivors | ratio old/new | $B^{\mathrm{aug}}_k$ |
|---|---|---|---|---|
| 1–5 | 1, 1, 2, 3, 4 | 1, 1, 2, 3, 4 | 1 | $0,1,1,1,23/5$ |
| 6 | 8 | **7** | 1.1429 | $23/5$ |
| 7 | 13 | **12** | 1.0833 | $23/5$ |
| 8 | 19 | **18** | 1.0556 | $319/13$ |
| 12 | 226 | **192** | 1.1771 | $319/13$ |
| 16 | 2114 | **1855** | 1.1396 | $319/13$ |
| 20 | 27328 | **22384** | 1.2209 | $319/13$ |
| 24 | 286581 | **243479** | 1.1770 | $319/13$ |

The augmented sieve first differs from L-9909 at $k = 6$, where it removes the class
$15 \bmod 64$. Explicit augmented survivor classes:

* mod 2: $\{1\}$; mod 4: $\{3\}$; mod 8: $\{3,7\}$; mod 16: $\{7,11,15\}$; mod 32: $\{7,15,27,31\}$
* mod 64: $\{7, 27, 31, 39, 47, 59, 63\}$  (L-9909's list minus $15$)
* mod 128: $\{27, 31, 39, 47, 63, 71, 91, 95, 103, 111, 123, 127\}$  (minus $79$)
* mod 256: $\{27, 31, 47, 63, 71, 91, 103, 111, 127, 155, 159, 167, 191, 223, 231, 239, 251, 255\}$  (minus $207$)

**(b) Joint densities mod $2^k 3^D$.** Verified equal to
$\tfrac23 \cdot |\text{Aug}(k)| / 2^k$ for all $1 \le k \le 14$, $D \in \{1,2,3\}$ —
i.e. the product form of L-9919.4(5) holds exactly, with **no** dependence on $D$.
Sample (joint density; ratio to the L-9909 density):

| $k$ | L-9909 density | joint density | ratio |
|---|---|---|---|
| 5 | $1/8$ | $1/12$ | $0.6667$ |
| 6 | $1/8$ | $7/96$ | $0.5833$ |
| 8 | $19/256$ | $3/64$ | $0.6316$ |
| 11 | $1/16$ | $17/512$ | $0.5313$ |
| 14 | $367/8192$ | $593/24576$ | $0.5386$ |
| 24 | $286581/2^{24}$ | $\tfrac23 \cdot 243479/2^{24}$ | $0.5664$ |

**(c) HONEST QUANTITATIVE VERDICT.** The joint sieve **is strictly stronger** than
L-9909's for every $k \ge 6$, but only by a **bounded factor** on the computed range,
not by a visibly improved exponential rate. Over $6 \le k \le 30$ (exact counts, script
`l9919_rate.py`) the ratio $|\text{L-9909}(k)| / |\text{Aug}(k)|$ stays inside
$[1.05556,\ 1.29758]$ and $\log_2$ of it inside $[0.07800,\ 0.37582]$, while the
*rate difference* $\frac1k\log_2\bigl(|\text{L-9909}(k)|/|\text{Aug}(k)|\bigr)$
**decreases**: $0.0321\ (k{=}6)$, $0.0196\ (k{=}12)$, $0.0136\ (k{=}18)$,
$0.0098\ (k{=}24)$, $0.0125\ (k{=}30)$. The data are consistent with a constant-factor
gain and give no evidence of an improved exponential decay rate (the sequence
oscillates with the continued-fraction structure of $\log_2 3$). Including the mod-3
factor $2/3$, the joint sieve's survivor density is $0.5833, 0.5664, 0.5630, 0.5664,
0.5138$ times L-9909's at $k = 6, 12, 18, 24, 30$ — i.e. about $0.51$–$0.59$ for
$k \ge 6$, roughly uniform in $k$.

### L-9919.6 (consequences actually derived)

**[H] and unconditional given X-9901** (every $n \le 10^6$ reaches $1$, hence
$\mu > 10^6$; a fortiori given the larger verified floor of experiment X-9903). Since
$B^{\mathrm{aug}}_k = 319/13 < 25$ for all $8 \le k \le 24$ (and smaller below), the
hypothesis $\mu > B^{\mathrm{aug}}_k$ of L-9919.4(6) is discharged for every $k \le 24$.

1. **New congruence.** $\mu \not\equiv 2 \pmod 3$. With L-9909.2(M),
   $$\mu \text{ odd}, \quad \mu \equiv 3 \pmod 4, \quad \mu \not\equiv 2 \pmod 3
   \;\Longrightarrow\; \mu \equiv 3 \text{ or } 7 \pmod{12},$$
   a class of density $1/6$ (against $1/4$ from $\mu \equiv 3 \bmod 4$ alone).
   Both residues survive; nothing here decides between $3 \mid \mu$ and $\mu \equiv 1 \bmod 3$.
2. **Improved mod-$2^k$ lists.** $\mu \bmod 64 \in \{7,27,31,39,47,59,63\}$ (L-9909
   also allowed $15$); $\mu \bmod 128$ in the 12-element list above (L-9909 also allowed
   $79$); $\mu \bmod 256$ in the 18-element list above (L-9909 also allowed $207$).
   Combining with (1): $\mu$ lies in exactly $36$ classes mod $768 = 2^8\cdot 3$,
   density $3/64 \approx 0.0469$ versus L-9909's $19/256 \approx 0.0742$.
3. **Strengthened parity-word constraint.** For every $j \le k \le 24$,
   $$a_j(\mu) \;\ge\; m_j + \bigl\lceil (j-m_j)\gamma \bigr\rceil, \qquad
     m_j = \min\bigl(a_j(\mu),\ \nu_3(\delta_j(\mu))\bigr),$$
   which is $\ge \lceil j\gamma\rceil$ and is **strictly** stronger than L-9911.3
   exactly at those $j$ where $m_j \ge 1$ and $\lceil j\gamma\rceil = \lceil (j-m_j)\gamma\rceil + m_j$
   fails. (Same statement for all $j$, given $\mu > B^{\mathrm{aug}}_j$.)
4. **No improvement to the exceptional bounds.** $B^{\mathrm{aug}}_k \le 319/13 < 25$
   for $k \le 24$ — the augmentation does **not** degrade L-9909's bound, and with the
   least-threshold refinement it is in fact smaller than L-9909's published
   $B_8 = 1688/13$. But this is a bookkeeping improvement only: both are $\lll 10^6$,
   so neither changes any conclusion.
5. **NO improvement to L-9907's density threshold.** In divergent mode L-9907.2 gives
   $\liminf_k a_k(\mu)/k \ge \gamma$. Item (3) gives
   $a_j/j \ge \gamma + m_j(1-\gamma)/j$, and $m_j$ is not bounded below by any positive
   multiple of $j$ by anything proved here (indeed $m_j = 0$ whenever
   $3 \nmid \delta_j$). **Therefore this file yields no improvement whatsoever to the
   $\gamma$ threshold**, and no interaction with Q-9902. This is stated explicitly so
   that it is not mistaken for one.
6. **Nothing about cycles.** No statement here bears on cycle length, $x_{\min}$, or
   the results of L-9905/L-9906/L-9910/L-9912/L-9913/L-9915/L-9917.

### L-9919.7 (honest assessment — MANDATORY)

**What survives.** The core observation is **correct**, with three corrections to the
framing this file was assigned:

* the descent depth is exactly $d(y) = \nu_3(y+1)$; **positivity never binds**
  (the assignment anticipated an extra positivity constraint — there is none);
* the exact amplified floor is $y+1 \ge (3/2)^{d}(\mu+1)$, i.e.
  $y \ge (3/2)^d \mu + c_d$ with $c_d = (3/2)^d - 1$ (the shift is by $\mu+1$, not $\mu$);
* the assignment's guess that the $a_j \ge d$ branch "may make the constraint either
  very strong or vacuous" resolves in a third way: that branch is where **all** the new
  strength lives (it is a genuine strengthening of the mod-$2^k$ sieve), while the
  complementary $a_j < d$ branch — the one that actually uses $3$-adic information about
  $n$ — **collapses to the single congruence $\mu \not\equiv 2 \bmod 3$** (L-9919.4(5),
  proved, not merely observed).

**What is genuinely new in this repository.** (i) The closed forms
$D^d(y) = 2^d(y+1)/3^d - 1$ and $d(y) = \nu_3(y+1)$ — I searched the packet for
$\nu_3$ and for any $(2n-1)/3$-iteration statement: `L-9904`, `L-9909`, `L-9911`
mention the single-step map $n \mapsto (2n-1)/3$, none iterates it, and $\nu_3$ occurs
nowhere in the repository. (ii) The congruence $\mu \not\equiv 2 \pmod 3$: absent from
L-9909.2(M) and L-9911.2, which stop at $\mu$ odd, $\mu \equiv 3 \bmod 4$. (iii) The
augmented mod-$2^k$ sieve and its exact tables. (iv) The $3$-adic collapse theorem.

**What is *not* new.** The underlying closure fact — every $T$-preimage of every orbit
point of $\mu$ lies in $X$ and hence is $\ge \mu$ — is already L-9911.5 (conditional
part) and L-9909.2(E). L-9919 does not add a new closure property; it *quantifies* a
known one into an effective congruence sieve. The shifted coordinate $u = n+1$ already
appears in L-9907.5, though only for all-ones words and only forwards.

**Is the mod-$6$ structure genuine leverage or repackaging?** Honest answer: **mostly
repackaging, with one small genuine gain.** By L-9919.4(5) the joint sieve *factorises*:
it is (an improved mod-$2^k$ sieve) $\times$ (one mod-$3$ condition). There is no
genuinely two-dimensional mod-$6^k$ interaction: the $3$-adic depth $D$ buys nothing
beyond $D = 1$, proved, not merely measured. So "a sieve modulo $6^k$" is the wrong
mental picture; the right one is "L-9909's sieve, slightly sharpened, times $2/3$".

**Is it subsumed?** Not literally — the augmented survivor lists are strictly smaller
than L-9909's from $k = 6$ on, and $\mu \not\equiv 2 \bmod 3$ is not in the packet.
But qualitatively it is the natural quantitative shadow of L-9911.5, and it is
**subsumed in spirit** by the trivial observation that $\mu$ cannot lie in the forward
orbit of any smaller integer.

**Is it a real advance? No.** The measured gain is a bounded factor $\approx 1.15$–$1.30$
on the mod-$2^k$ side and exactly $2/3$ on the mod-$3$ side, with the rate difference
$\frac1k \log_2(\text{old}/\text{new})$ decaying over the computed range. A search
program gains a constant factor $\approx 1.8$; nothing asymptotic changes; no bound on
$\mu$, on cycle length, or on parity density improves. **This is elegant but adds no
quantitative advance.** The heuristic reason is worth recording: the augmentation
imposes "one extra odd step" at a positive density of indices $j$, but the surviving
parity walks are conditioned to stay above the line $a_j \ge j\gamma$ and therefore sit
at height $\asymp \sqrt{j}$ above it, so a $+1$ requirement is satisfied automatically
except near the ends of the window — a constant-factor, not exponential, cost.

**What would have to be true for a real advance.** The augmentation would have to bite
at a positive density of indices *for the surviving walks*, i.e. the extra requirement
would have to grow with $j$ rather than being $+m_j$ with $m_j = O(1)$. That needs
$\nu_3(\delta_j)$ to be large along survivors. Nothing here suggests it is; on the
contrary $\delta_j$ behaves like a "random" integer mod $3$ after each even step. The
one direction with visible remaining headroom is L-9919.8.

**Also honestly: the family used here is not maximal.** See L-9919.8 — allowing the
backward moves $z \mapsto 2z$ interleaved with $D$ gives a strictly stronger, still
class-uniform, still congruence-local sieve. And the *full* constraint "no $x < \mu$
has an orbit meeting $\mu$'s orbit" is stronger than any of these but is not a
congruence condition at all, so it cannot be made into a sieve of this type.

### L-9919.8 (EXTENSION, exploratory: the backward-word sieve)

*Soundness proved; strength measured only on a finite range. Status of this sub-claim:
PARTIAL.*

Work in $u = z+1$ coordinates. The two backward moves of $T$ are
$$\mathsf{D}: u \mapsto \tfrac{2}{3}u \ \ (\text{legal iff } 3 \mid u), \qquad
\mathsf{M}: u \mapsto 2u - 1 \ \ (\text{i.e. } z \mapsto 2z, \text{ always legal}).$$
Starting from $u_0 = T^j(n)+1$, whose form is $(3^{a_j}u + \delta_j)/2^j$ by
L-9919.4(1), every backward word $w \in \{\mathsf{D},\mathsf{M}\}^*$ keeps the state in
the shape $u_{\mathrm{cur}} = (Pu + Q)/2^j$ with $P \in \mathbb{Z}^+$, $Q \in \mathbb{Z}$:
$$\mathsf{D}: (P,Q) \mapsto (\tfrac{2P}{3}, \tfrac{2Q}{3}) \quad\text{(class-uniformly legal iff } 3 \mid P \text{ and } 3 \mid Q),
\qquad \mathsf{M}: (P,Q) \mapsto (2P,\ 2Q - 2^j).$$
1. **(Soundness.)** If $3 \mid P$ and $3 \mid Q$ then $3 \mid u_{\mathrm{cur}}$ for
   **every** $n$ in the class (because $2^j$ is invertible mod $3$ and $u$ ranges over
   all residues mod $3$ within a class mod $2^k$). Hence for a word $w$ all of whose
   $\mathsf{D}$-moves satisfy this, the terminal value $z_w = u_{\mathrm{cur}}-1$ is a
   positive integer $T$-preimage-chain ancestor of $T^j(n)$ for every
   $n > \theta_w$, where $\theta_w$ is the maximum of the positivity thresholds
   $(2^{j+1}-Q)/P - 1$ along the word and of the descent threshold
   $Q/(2^j - P) - 1$ (relevant only when $2^j > P$). **[H]** If $z_w < n = \mu$ this
   contradicts minimality, so the class is excluded.
2. **(Strictly stronger.)** Restricting $w$ to $\mathsf{D}$-only words reproduces
   L-9919.4 exactly. Allowing $\mathsf{M}$ is strictly stronger: the class
   $63 \bmod 256$ is an augmented $8$-survivor, yet the word
   $\mathsf{D}\mathsf{M}\mathsf{D}\mathsf{D}\mathsf{D}\mathsf{D}$ applied to $T^8(n)$
   lands on $3(n+1)/4 - 1 < n$ for every $n \equiv 63 \pmod{256}$, $n > 5/3$.
   (Verified: $n=63$: $T^8(63)=182$, chain $182 \to 121 \to 242 \to 161 \to 107 \to 71
   \to 47$, and $T^6(47) = 182$, $47 < 63$.)
3. **(Measured strength, words of length $\le 12$.)**

| $k$ | L-9909 | L-9919.4 (descent only) | L-9919.8 (backward words) |
|---|---|---|---|
| 8 | 19 | 18 | **16** |
| 10 | 64 | 57 | **46** |
| 12 | 226 | 192 | **144** |
| 14 | 734 | 593 | **436** |
| 16 | 2114 | 1855 | **1366** |

   Maximum kill threshold over all of these: $159/13 < 13$, so the same discharge
   argument applies. At $k=16$ the backward-word sieve retains $0.646$ of L-9909's
   classes ($0.431$ after the mod-$3$ factor). This is still a bounded factor on the
   computed range; whether it improves the exponential rate is **not determined here**
   and is the obvious next question.

---

## Definitions

All D-numbers are from `NOTATION.md`. Local definitions:

* **Descent map** $D(y) := (2y-1)/3$, defined for $y \in \mathbb{Z}^+$ with
  $y \equiv 2 \pmod 3$. It is the unique **odd** $T$-preimage of $y$.
* **Descent depth** $d(y) := \sup\{d \ge 0 : D^d(y) \text{ defined in } \mathbb{Z}^+\}$
  (D applied $d$ times in succession, each application legal). $d(y) = 0$ means
  $y \not\equiv 2 \bmod 3$.
* **Shifted coordinate** $u := n+1$ (or $y+1$). In this coordinate the odd branch of
  $T$ is $u \mapsto \tfrac32 u$, the even branch is $u \mapsto \tfrac{u+1}{2}$, and
  $D$ is $u \mapsto \tfrac23 u$.
* **Shifted remainder** $\delta_j := \rho_j + 2^j - 3^{a_j}$, a function of the parity
  word only (L-9903.2). $\nu_3(0) := +\infty$; $m_j := \min(a_j, \nu_3(\delta_j))$.
* **Augmented $k$-survivor**, **joint $(k,D)$-survivor**, **branch (U)/(V)/(N)**,
  $\theta_{j,d}$, $B^{\mathrm{aug}}_k$: as defined in L-9919.4.
* **$\text{Aug}(k)$**: the set of augmented $k$-survivor classes mod $2^k$;
  **$\text{Joint}(k,D)$**: the set of joint $(k,D)$-survivor pairs.
* **Counterexample set** $X$, **minimal counterexample** $\mu$: as in the Standing
  hypothesis (identical to L-9911's $X$, $\mu$ and L-9909's $K$, $\mu$).

---

## Motivation

A counterexample search, or a construction of a counterexample, benefits from every
congruence restriction on $\mu$ that can be discharged unconditionally against a
verified floor. L-9909 supplies such restrictions from the *forward* dynamics
($T^j(n) \ge n$). The counterexample set is also closed *backwards* (L-9911.5), and
backward closure is a genuinely different source of constraints because the backward
tree is not contained in the forward orbit. This file asks how much of that backward
closure can be turned into congruence conditions, and answers it exactly: the pure
descent family gives a sharper mod-$2^k$ sieve plus one mod-$3$ condition, and the
factorisation is exact. The negative half of the answer is as useful as the positive
half: it tells later agents not to look for a genuinely two-dimensional mod-$6^k$
sieve from this family, and points instead at L-9919.8 (mixed backward words) as the
only direction here with visible headroom. If a counterexample is ever exhibited, the
congruence $\mu \equiv 3$ or $7 \pmod{12}$ is a cheap consistency check on it.

---

## Proof or construction

### Proof of L-9919.1

**(1)** $3 \mid 2y - 1 \iff 2y \equiv 1 \pmod 3$. Since $2 \cdot 2 = 4 \equiv 1$, the
inverse of $2$ mod $3$ is $2$, so $2y \equiv 1 \iff y \equiv 2 \pmod 3$. Conversely if
$y \equiv 2$ then $2y - 1 \equiv 4 - 1 = 3 \equiv 0$. Both directions are elementary and
hold for all $y \in \mathbb{Z}$.

**(2)** Let $y \equiv 2 \pmod 3$, $y \in \mathbb{Z}^+$; then $y \ge 2$ (the positive
integers $\equiv 2 \bmod 3$ are $2,5,8,\dots$). Put $x := (2y-1)/3 \in \mathbb{Z}$ by (1).
*Positivity:* $2y - 1 \ge 3$, so $x \ge 1$. *Oddness:* $3x = 2y-1$ is odd; if $x$ were
even then $3x$ would be even. So $x$ is odd. *$T(x) = y$:* $x$ odd gives
$T(x) = (3x+1)/2 = ((2y-1)+1)/2 = y$. *$x < y$:* $x < y \iff 2y - 1 < 3y \iff -1 < y$,
true for every $y \ge 1$. All four statements hold for every admissible $y$, including
the least one $y = 2$ ($x = 1$, odd, $T(1) = 2$, $1 < 2$). No case distinction on the
size of $y$ is needed.

**(3)** Let $x \in \mathbb{Z}^+$ with $T(x) = y$. If $x$ is even then $x/2 = y$, so
$x = 2y$; conversely $T(2y) = y$ always. If $x$ is odd then $(3x+1)/2 = y$, so
$3x = 2y-1$, so $3 \mid 2y-1$, so $y \equiv 2 \bmod 3$ by (1), and then $x = D(y)$;
conversely by (2) $D(y)$ is an odd positive integer with $T(D(y)) = y$ whenever
$y \equiv 2 \bmod 3$. $2y$ is even, $D(y)$ odd, so they are distinct. This is exactly
L-9911 U3, re-derived here so this file is self-contained. For $y = 1$: $1 \equiv 1
\bmod 3$, so $T^{-1}(1) = \{2\}$ (and indeed $T(2) = 1$). For $y = 2$: $2 \equiv 2
\bmod 3$, $D(2) = 1$, so $T^{-1}(2) = \{1,4\}$.

**(4)** By L-9911 U2 (two-sided closure), $n \in X \iff T(n) \in X$ for every
$n \in \mathbb{Z}^+$. Apply it with $n = D(y)$, using $T(D(y)) = y$ from (2):
$D(y) \in X \iff y \in X$. (Self-contained re-derivation: $x$ odd gives $C(x) = 3x+1$
even and $C^2(x) = (3x+1)/2 = T(x)$; so $y \in O_C(D(y))$ and $O_C(y) \subseteq O_C(D(y))$,
whence $1 \in O_C(D(y)) \iff 1 \in O_C(y)$ — the forward inclusion is L-9909.2(F), the
backward one L-9909.2(B).)

**(5)** Assume (H) and suppose $\mu \equiv 2 \pmod 3$. By (2), $x := D(\mu)$ is a
positive integer with $x < \mu$, and by (4) $x \in X$. This contradicts the minimality
of $\mu$. Hence $\mu \not\equiv 2 \pmod 3$. Since $\mu \equiv 3 \pmod 4$
(L-9909.2(M)(ii)), the Chinese Remainder Theorem gives
$\mu \bmod 12 \in \{3,7,11\}$, and $11 \equiv 2 \bmod 3$ is excluded, leaving
$\mu \equiv 3$ or $7 \pmod{12}$. $\square$

### Proof of L-9919.2

**(1) and (2) together, by induction on $d$.** Claim: for every $d \ge 0$ and every
$y \in \mathbb{Z}^+$, $D^d(y)$ is defined iff $3^d \mid (y+1)$, and then
$D^d(y) + 1 = 2^d(y+1)/3^d$.

*Base $d = 0$:* $D^0(y) = y$ is defined, $3^0 \mid y+1$ trivially, and
$y + 1 = 2^0(y+1)/3^0$.

*Step.* Assume the claim for $d$. Note first the one-step identity: if $y \equiv 2
\bmod 3$ then
$$D(y) + 1 = \frac{2y-1}{3} + 1 = \frac{2y+2}{3} = \frac{2(y+1)}{3},$$
i.e. $D$ is multiplication by $2/3$ in the coordinate $u = y+1$; and legality
$y \equiv 2 \bmod 3$ is exactly $3 \mid y+1$.

($\Rightarrow$) Suppose $D^{d+1}(y)$ is defined. Then $D^d(y)$ is defined, so by the
inductive hypothesis $3^d \mid (y+1)$ and $D^d(y)+1 = 2^d(y+1)/3^d$. Legality of the
$(d{+}1)$-st step means $3 \mid D^d(y)+1 = 2^d(y+1)/3^d$; since $\gcd(2,3) = 1$ this
forces $3^{d+1} \mid (y+1)$. And then
$D^{d+1}(y)+1 = \tfrac23\bigl(2^d(y+1)/3^d\bigr) = 2^{d+1}(y+1)/3^{d+1}$.

($\Leftarrow$) Suppose $3^{d+1} \mid (y+1)$. Then $3^d \mid (y+1)$, so by induction
$D^d(y)$ is defined with $D^d(y)+1 = 2^d(y+1)/3^d$, which is divisible by $3$ (again
because $3^{d+1} \mid y+1$ and $\gcd(2,3)=1$); so the $(d{+}1)$-st step is legal, and
the value is as stated. It remains to check the *positivity* half of "defined in
$\mathbb{Z}^+$"; that is (3) below, proved independently of this induction.

Rearranging $D^d(y)+1 = 2^d(y+1)/3^d$ gives the three displayed forms in (1)
(using $3^d \cdot 1 = 3^d$ for the second and $2^d y + 2^d - 3^d$ for the third).

Finally, $\{y : d(y) \ge d\} = \{y : 3^d \mid y+1\} = \{y \equiv -1 \bmod 3^d\}$ is a
single residue class mod $3^d$, and $d(y) = \max\{d : 3^d \mid y+1\} = \nu_3(y+1)$,
finite because $y + 1 \ge 2$.

**(3) Positivity never binds.** Let $3^d \mid (y+1)$ and $m := (y+1)/3^d$, so
$m \ge 1$ because $y+1 \ge 1$ and $m$ is a positive integer. By (1),
$D^d(y) = 2^d m - 1 \ge 2^0 \cdot 1 - 1 = 0$; and for $d \ge 1$,
$D^d(y) = 2^d m - 1 \ge 2 - 1 = 1$. For $d = 0$, $D^0(y) = y \ge 1$. So in all cases
$D^d(y) \ge 1$. The same argument applied to each $i \le d$ (note $3^i \mid y+1$) shows
every intermediate is $\ge 1$. Hence the divisibility condition of (2) already
guarantees membership in $\mathbb{Z}^+$, and the "staying positive" requirement in the
definition of $d(y)$ is automatically satisfied. (Also $D^d(y) = 2^d m - 1$ is odd for
$d \ge 1$, giving the oddness in (4).)

**(4)** Monotonicity: $D^{i+1}(y)+1 = \tfrac23(D^i(y)+1) < D^i(y)+1$ since
$D^i(y)+1 > 0$. Inversion: $T(D(z)) = z$ by L-9919.1(2), so
$T^i(D^i(y)) = y$ by induction on $i$. $\square$

### Proof of L-9919.3

Assume (H). Fix $j \ge 0$ and set $y := T^j(\mu)$, $d := \nu_3(y+1) = d(y)$.

By L-9911.1 (or L-9909.2(F)), $y \in X$. By L-9919.2(2)-(3), $D^i(y)$ is a positive
integer for every $0 \le i \le d$, and by L-9919.1(4) applied $i$ times,
$D^i(y) \in X$. By minimality of $\mu$, $D^i(y) \ge \mu$ for every $0 \le i \le d$.

Take $i = d$ (the smallest of these, by L-9919.2(4)). Using
$D^d(y) + 1 = 2^d(y+1)/3^d$ from L-9919.2(1), the inequality $D^d(y) \ge \mu$ is
equivalent to $2^d(y+1)/3^d \ge \mu+1$, i.e. $2^d(y+1) \ge 3^d(\mu+1)$, i.e.
$$y \ge \Bigl(\tfrac32\Bigr)^{d}(\mu+1) - 1 = \Bigl(\tfrac32\Bigr)^{d}\mu + \Bigl(\tfrac32\Bigr)^{d} - 1 ,$$
so $c_d = (3/2)^d - 1$ exactly. All steps are equivalences (multiplication by the
positive quantities $3^d, 2^{-d}$), so no sharpness is lost.

The contrapositive form is the same statement with the roles of hypothesis and
conclusion exchanged; taking logarithms base $3/2$ of $2^d(y+1) \ge 3^d(\mu+1)$ gives
$d \le \log_{3/2}\frac{y+1}{\mu+1}$.

$j = 0$: here $y = \mu$ and the inequality reads $2^{d}(\mu+1) \ge 3^{d}(\mu+1)$, i.e.
$2^d \ge 3^d$, which forces $d = 0$, i.e. $\nu_3(\mu+1) = 0$, i.e.
$\mu \not\equiv 2 \bmod 3$ — recovering L-9919.1(5).

**Caveat proof.** If $v_{j-1}(\mu) = \dots = v_{j-t}(\mu) = 1$ then for $1 \le i \le t$,
$T^{j-i}(\mu)$ is odd and $T(T^{j-i}(\mu)) = T^{j-i+1}(\mu)$; by uniqueness of the odd
preimage (L-9919.1(3)), $D(T^{j-i+1}(\mu)) = T^{j-i}(\mu)$. Induction gives
$D^i(T^j(\mu)) = T^{j-i}(\mu)$ for $0 \le i \le t$, and these are orbit points, already
$\ge \mu$ by L-9911.1. $\square$

### Proof of L-9919.4

**(1)** By L-9903.1, $2^j T^j(n) = 3^{a_j} n + \rho_j$. Add $2^j$ to both sides and
substitute $n = u - 1$:
$$2^j\bigl(T^j(n)+1\bigr) = 3^{a_j}n + \rho_j + 2^j = 3^{a_j}u + \bigl(\rho_j + 2^j - 3^{a_j}\bigr) = 3^{a_j}u + \delta_j .$$
The recursion for $\delta$ follows from $\rho_{i+1} = 3^{v_i}\rho_i + v_i 2^i$: if
$v_i = 1$ then $a_{i+1} = a_i + 1$ and
$\delta_{i+1} = 3\rho_i + 2^i + 2^{i+1} - 3^{a_i+1} = 3(\rho_i + 2^i - 3^{a_i}) = 3\delta_i$;
if $v_i = 0$ then $a_{i+1} = a_i$ and
$\delta_{i+1} = \rho_i + 2^{i+1} - 3^{a_i} = \delta_i + 2^i$. The closed form
$\delta_j = \sum_{i<j,\,v_i=0} 3^{s_i}2^i$ follows by the same telescoping as in
L-9903.2 (each even step contributes $2^i$, subsequently multiplied by $3$ once per
later odd step). Nonnegativity and "$\delta_j = 0 \iff$ all-ones" are immediate from
the closed form (the terms are positive and indexed by the even steps). *Cross-check:*
for the all-ones word, (1) becomes $2^j(T^j(n)+1) = 3^j(n+1)$, which is precisely
L-9907.5.

**(2)** $\nu_3(T^j(n)+1) \ge d \iff 3^d \mid (T^j(n)+1) \iff 3^d \mid 2^j(T^j(n)+1)$
(as $\gcd(2,3)=1$) $\iff 3^d \mid 3^{a_j}u + \delta_j$ by (1). Now:
*if $d \le a_j$*, then $3^d \mid 3^{a_j}u$ for every $u$, so the condition reduces to
$3^d \mid \delta_j$, i.e. $d \le \nu_3(\delta_j)$ — which is independent of $n$, giving
branch (U) when it holds and branch (V) when it fails.
*If $d > a_j$*, the congruence $3^{a_j}u \equiv -\delta_j \pmod{3^d}$ has a solution iff
$\gcd(3^{a_j},3^d) = 3^{a_j}$ divides $\delta_j$, and then dividing through by $3^{a_j}$
gives the equivalent congruence $u \equiv -\delta_j/3^{a_j} \pmod{3^{d-a_j}}$, a single
class. The three branches are mutually exclusive and exhaustive by the sign of
$d - a_j$ and (in the first case) of $d - \nu_3(\delta_j)$.

**(3)** Given the divisibility, L-9919.2(1) gives
$D^d(T^j(n)) + 1 = 2^d(T^j(n)+1)/3^d$, so
$$D^d(T^j(n)) < n \iff \frac{2^d\bigl(T^j(n)+1\bigr)}{3^d} < u
\iff 2^d \cdot \frac{3^{a_j}u + \delta_j}{2^j} < 3^d u
\iff u\bigl(2^{j}3^{d} - 2^{d}3^{a_j}\bigr) > 2^{d}\delta_j,$$
multiplying by the positive quantity $2^j 3^{-d}\cdot 3^d = 2^j$ and rearranging; every
step is an equivalence. If $2^j3^d \le 2^d3^{a_j}$ the left side is $\le 0 \le 2^d\delta_j$
so the inequality fails for every $u$ (note $\delta_j \ge 0$; when $\delta_j = 0$ the
inequality is strict-vs-zero and still fails). If $2^j3^d > 2^d3^{a_j}$ the inequality
is equivalent to $u > 2^d\delta_j/(2^j3^d - 2^d3^{a_j})$, i.e. $n > \theta_{j,d}$.

*$d = 0$:* $\theta_{j,0} = \delta_j/(2^j - 3^{a_j}) - 1 = (\rho_j + 2^j - 3^{a_j} - 2^j + 3^{a_j})/(2^j-3^{a_j}) = \rho_j/(2^j - 3^{a_j})$,
which is exactly L-9909.3(b)'s threshold; and $2^j > 3^{a_j}$ is exactly L-9909's
failing-index condition. So the augmented sieve contains L-9909's.

*$d > a_j \Rightarrow 2^j3^d > 2^d3^{a_j}$:* the inequality is
$3^{\,d-a_j} > 2^{\,d-j}$. If $d \le j$ then the right side is $\le 1 < 3 \le 3^{d-a_j}$
(as $d - a_j \ge 1$). If $d > j$ then $d - a_j \ge d - j \ge 1$ (since $a_j \le j$) and
$3^{d-a_j} \ge 3^{d-j} > 2^{d-j}$. Either way the inequality holds.

*Monotonicity in $d$ (used in (4)):* $2^j3^d > 2^d3^{a_j} \iff (3/2)^d > 3^{a_j}/2^j$,
and $(3/2)^d$ is strictly increasing in $d$; so if a branch-(U) kill exists for some
$d \le m_j$ it exists for $d = m_j$.

**(4)** is a definition; the equivalence stated inside it is the monotonicity just
proved, plus the observation that branch (U) is available exactly for
$0 \le d \le m_j$. Taking only $d = 0$ gives $3^{a_j} \ge 2^j$ for all $j \le k$, which
is L-9909's $k$-survivor condition; since $m_j \ge 0$ the augmented condition at
$d = m_j$ implies the one at $d = 0$ by monotonicity, so
$\text{Aug}(k) \subseteq \text{L-9909-survivors}(k)$.

**(5) The $3$-adic collapse.** Let $r \bmod 2^k$ be an augmented $k$-survivor, $j \le k$,
and suppose branch (N) is nonempty at $j$, i.e. $3^{a_j} \mid \delta_j$, i.e.
$\nu_3(\delta_j) \ge a_j$. Suppose, for contradiction, $\nu_3(\delta_j) = a_j$ exactly.
Then $m_j = \min(a_j, \nu_3(\delta_j)) = a_j$, and the augmented survivor condition at
$j$ reads $3^{a_j - a_j} \ge 2^{\,j - a_j}$, i.e. $1 \ge 2^{\,j-a_j}$, i.e. $j \le a_j$.
Since always $a_j \le j$, this forces $a_j = j$, i.e. the length-$j$ prefix of the word
is all ones, whence $\delta_j = 0$ by (1) and $\nu_3(\delta_j) = +\infty \ne a_j$ — a
contradiction. Therefore $\nu_3(\delta_j) > a_j$ (including the case
$\delta_j = 0$, $\nu_3 = \infty$).

Consequently $3 \mid \delta_j/3^{a_j}$, so $-\delta_j/3^{a_j} \equiv 0 \pmod 3$ and the
branch-(N) forbidden class $u \equiv -\delta_j/3^{a_j} \pmod{3^{d-a_j}}$ is contained in
$\{u \equiv 0 \bmod 3\}$ for every $d > a_j$.

Conversely the single event $(j,d) = (0,1)$ realises $\{u \equiv 0 \bmod 3\}$ exactly:
$a_0 = 0$, $\delta_0 = 0$, branch (N) applies ($d = 1 > 0 = a_0$, and
$3^{0} \mid 0$), the forbidden class is $u \equiv 0 \bmod 3$, the numeric condition
$2^0 3^1 > 2^1 3^0$ holds, and $\theta_{0,1} = 0 - 1 = -1$, so **every** $n \ge 1$ with
$u \equiv 0 \bmod 3$ is killed. (Indeed this kill *is* $D(n) < n$, L-9919.1(2).)

Hence the union of all branch-(N) forbidden sets over $j \le k$, $a_j < d \le D$, on an
augmented $k$-survivor class, is exactly $\{u \equiv 0 \bmod 3\}
= \{n \equiv 2 \bmod 3\}$, independent of $D \ge 1$. This is precisely the asserted
product decomposition and density formula. $\square$

**(6) Sieve theorem.** Enumerate the classes mod $2^{k'}$ for $k' = 1,2,\dots,k$ as a
binary tree (L-9902.2: classes mod $2^{k'}$ $\leftrightarrow$ words of length $k'$;
L-9902.3(iii): each class has exactly two lifts, realising the two word extensions).
If $r \bmod 2^k$ is not an augmented $k$-survivor, let $k' \le k$ be least such that
$r \bmod 2^{k'}$ has a branch-(U) kill at $j = k'$ (such $k'$ exists: some $j \le k$
carries a kill, and the kill at $j$ is a property of the class mod $2^{j}$). Among the
kills at that $(k',j=k')$ pick the one with smallest $\theta$; by definition
$\theta \le B^{\mathrm{aug}}_k$. If $n > B^{\mathrm{aug}}_k \ge \theta$ then by (3) the
corresponding $D^{d}(T^{k'}(n))$ is defined (branch (U): the divisibility holds for every
$n$ in the class), is a positive integer by L-9919.2(3), and is $< n$.

**[H]** Suppose $\mu > B^{\mathrm{aug}}_k$ and $\mu \bmod 2^k$ were not an augmented
$k$-survivor. The previous paragraph produces $j \le k$, $d \ge 0$ and a positive
integer $x = D^d(T^j(\mu)) < \mu$. By L-9911.1, $T^j(\mu) \in X$; by L-9919.1(4)
applied $d$ times, $x \in X$; so $x$ contradicts minimality. Hence $\mu \bmod 2^k \in
\text{Aug}(k)$. Together with L-9919.1(5) ($\mu \not\equiv 2 \bmod 3$) and (5), the pair
$(\mu \bmod 2^k, \mu \bmod 3^D)$ is a joint $(k,D)$-survivor for every $D \ge 1$.
$\square$

### Proof of L-9919.5

The tables are exact finite computations; the scripts and their real captured outputs
appear in the Adversarial tests section. Their **logical role** is: (i) PART A of
`l9919_sieve.py` independently reproduces L-9909.4's published survivor lists for
$k \le 8$ (a cross-check of the implementation, not a new claim); (ii) PARTS B, C, E
evaluate the *definitions* of L-9919.4(4) — finitely many classes, exact integer
arithmetic — so their outputs are theorems about those finite sets; (iii) PART F and
`l9919_orbits.py` compare the sieve's prediction against **directly computed orbits and
descents**, which is an adversarial test of the derivation in L-9919.4(2)-(3), not an
ingredient of any proof. Nothing in L-9919.5 is extrapolated beyond the stated ranges.
The verdict statements in L-9919.5(c) are explicitly labelled as descriptions of the
computed range, not as asymptotic theorems.

### Proof of L-9919.6

Items (1) and (2) are L-9919.1(5) and L-9919.4(6) instantiated with the computed
$\text{Aug}(k)$ tables and $B^{\mathrm{aug}}_k = 319/13 < 25 < 10^6 < \mu$ (the last
inequality from X-9901 inside L-9909, which is the finite verification that every
$n \le 10^6$ reaches $1$; experiment X-9903 verifies a larger floor and would serve
equally). The count "36 classes mod 768" is $18 \times 2$ by L-9919.4(5) and CRT.

Item (3): the augmented survivor condition at $j$ is $3^{a_j - m_j} \ge 2^{\,j-m_j}$.
For integers $A \ge 0$ and $B \ge 1$, $3^A \ge 2^B \iff A \ge B\gamma \iff A \ge
\lceil B\gamma\rceil$, the last step because $B\gamma \notin \mathbb{Z}$ for $B \ge 1$
(irrationality of $\log_2 3$; L-9909 Lemma D, L-9911.3). With $A = a_j - m_j$ and
$B = j - m_j$ this is $a_j \ge m_j + \lceil (j-m_j)\gamma\rceil$; for $j = m_j$ the
condition is vacuous and the inequality holds trivially.

Item (4) is read off the computed $B^{\mathrm{aug}}_k$ column; that the least-threshold
refinement is legitimate is part of the proof of L-9919.4(6) (only the kill actually
used enters).

Item (5): from (3), $a_j/j \ge \gamma + m_j(1-\gamma)/j$. To improve
$\liminf_j a_j/j \ge \gamma$ one would need $\liminf_j m_j/j > 0$. Nothing proved here
gives any positive lower bound on $m_j$: indeed $m_j = 0$ whenever $3 \nmid \delta_j$,
and $\delta_{i+1} = \delta_i + 2^i$ at each even step, so a single even step following a
$\delta$ divisible by $3$ makes $\nu_3(\delta) = 0$ (since $3 \nmid 2^i$). Hence no
improvement to L-9907.2's threshold follows, and none is claimed.

Item (6) is a scope statement: no argument above mentions cycles. $\square$

### Proof of L-9919.8(1)-(2)

**(1)** Write the state after a prefix of the backward word as
$u_{\mathrm{cur}} = (Pu+Q)/2^j$ with $P \in \mathbb{Z}^+$, $Q \in \mathbb{Z}$; the
initial state is $P = 3^{a_j}$, $Q = \delta_j$ by L-9919.4(1). The move $\mathsf{M}$
($z \mapsto 2z$, always a legal $T$-preimage by L-9919.1(3)) sends
$u_{\mathrm{cur}} \mapsto 2u_{\mathrm{cur}} - 1 = (2Pu + 2Q - 2^j)/2^j$. The move
$\mathsf{D}$ is legal iff $3 \mid u_{\mathrm{cur}}$, i.e. iff $3 \mid (Pu+Q)$ (as
$\gcd(2,3)=1$); this holds for **every** $n$ in the class mod $2^k$ iff $3 \mid P$ and
$3 \mid Q$ — necessity because a class mod $2^k$ contains integers $u$ in all three
residue classes mod $3$ (CRT), so $Pu + Q \equiv 0$ for all three values of $u \bmod 3$
forces $P \equiv Q \equiv 0$. When legal, $u_{\mathrm{cur}} \mapsto \tfrac23
u_{\mathrm{cur}} = ((2P/3)u + (2Q/3))/2^j$. Each node's $z = u_{\mathrm{cur}} - 1$ must
be a positive integer: integrality is inherited (initial state integral, both moves
preserve it under the stated legality), and $z \ge 1 \iff Pu + Q \ge 2^{j+1} \iff
n \ge (2^{j+1}-Q)/P - 1$, which is the recorded positivity threshold. The terminal $z_w$
satisfies $T^{|w|}(z_w) = T^j(n)$ by construction, so $z_w \in X$ whenever $n \in X$
(L-9911 U2 applied $|w|$ times). If moreover $z_w < n$, then $n = \mu$ contradicts
minimality. The descent threshold: $z_w < n \iff (Pu+Q)/2^j < u \iff u(2^j - P) > Q$,
which for $2^j > P$ is $n > Q/(2^j-P) - 1$.

**(2)** Restricting to $\mathsf{D}$-only words: starting from $(P,Q) = (3^{a_j},\delta_j)$,
$d$ successive $\mathsf{D}$'s give $(P,Q) = (2^d3^{a_j-d},\ 2^d\delta_j/3^d)$, legal
class-uniformly iff $3^d \mid 3^{a_j}$ and $3^d \mid \delta_j$, i.e. $d \le m_j$ — exactly
branch (U); and the descent condition $u(2^j - P) > Q$ becomes
$u(2^j - 2^d3^{a_j-d}) > 2^d\delta_j/3^d$, i.e. (multiplying by $3^d$)
$u(2^j3^d - 2^d3^{a_j}) > 2^d\delta_j$, which is L-9919.4(3). So L-9919.8 restricted to
$\mathsf{D}$-only words *is* L-9919.4. Strictness of the extension is witnessed by the
class $63 \bmod 256$ (word $\mathsf{DMDDDD}$ at $j=8$), verified numerically in the
Adversarial tests; the affine form there is $P = 192$, $Q = 0$, $2^j = 256$, giving
$z_w = 3(n+1)/4 - 1 < n$ for $n > 5/3$. $\square$

---

## Dependency audit

| Used | Where | Exact role |
|---|---|---|
| D-9901, D-9902, D-9905, D-9906, D-9909, D-9910 | throughout | definitions of $C$, $T$, orbits, parity data, $X$, $\sigma$ |
| L-9902.1(c), L-9902.2, L-9902.3(iii) (PROVED) | L-9919.4 setup; proof of L-9919.4(6) | the length-$k$ parity word (hence $a_j$, $\rho_j$, $\delta_j$) is a function of $n \bmod 2^k$; classes $\leftrightarrow$ words bijectively; the two-lift tree structure used to enumerate classes by DFS over words |
| L-9903.1 (PROVED) | proof of L-9919.4(1) | $2^jT^j(n) = 3^{a_j}n+\rho_j$ — the only input to the shifted iteration formula |
| L-9903.2 (PROVED) | proof of L-9919.4(1) | $\rho_j$ depends only on the word; telescoping used for the closed form of $\delta_j$ |
| L-9909.2(B),(F) (PROVED) | proof of L-9919.1(4) | forward/backward closure of $X$ under $C$ |
| L-9909.2(M)(ii) (PROVED) | L-9919.1(5), L-9919.6(1) | $\mu \equiv 3 \pmod 4$ |
| L-9909.3(b), L-9909.4 (PROVED) | L-9919.4(3) boundary case $d=0$; L-9919.5 PART A | the $d = 0$ threshold and the published survivor lists used as an implementation cross-check |
| X-9901 (finite verification inside L-9909) | L-9919.6 | $\mu > 10^6$, discharging $\mu > B^{\mathrm{aug}}_k$ |
| L-9911 U2 (PROVED) | proofs of L-9919.1(4), L-9919.8(1) | $n \in X \iff T(n) \in X$ |
| L-9911 U3 (PROVED) | L-9919.1(3) (restated and re-proved inline) | complete $T$-preimage set |
| L-9911.1 (PROVED) | proofs of L-9919.3, L-9919.4(6) | $O_T(\mu) \subseteq X \cap [\mu,\infty)$ |
| L-9911.3 / L-9909 Lemma D (PROVED) | L-9919.6(3) | $3^A \ge 2^B \iff A \ge \lceil B\gamma\rceil$ for $B \ge 1$ |
| L-9907.5 (PROVED) | cross-check in proof of L-9919.4(1) | the all-ones specialisation $2^j(T^j(n)+1) = 3^j(n+1)$ |
| L-9907.2 (PROVED) | L-9919.6(5) | the $\gamma$ threshold that is *not* improved |
| X-9903 (EMPIRICAL) | L-9919.6 (optional) | a larger verified floor; not needed, since $B^{\mathrm{aug}}_k < 25$ |

**No circularity.** L-9919 uses L-9902/L-9903/L-9907/L-9909/L-9911 and is used by none
of them. The only conditional inputs are L-9911.1 and L-9909.2(M), both themselves
conditional on (H), which is this file's standing hypothesis; no unconditional
statement of this file depends on any conditional statement.

---

## Gap audit

* **Hidden finiteness assumptions.** L-9919.1–.4 and .8(1)-(2) are proved for all
  $y, n, j, d, k, D$ in the stated ranges with no appeal to computation. The tables of
  L-9919.5 and the strength figures of L-9919.8(3) are finite computations and are
  labelled as such; the verdict in L-9919.5(c) is explicitly phrased as "over the
  computed range" and does **not** claim an asymptotic theorem. The heuristic
  explanation offered in L-9919.7 is labelled heuristic.
* **Unjustified induction.** The two inductions (L-9919.2(1)-(2) on $d$; the closed form
  of $\delta_j$) are written out with base case and both directions of the step. The
  induction in L-9919.2(2) deliberately proves only "defined as a rational/integer"; the
  positivity half is proved separately in (3) so that the induction is not circular.
* **Boundary cases.** $y = 1$ and $y = 2$ (L-9919.1(3)); $d = 0$ and $j = 0$ (all of
  L-9919.2–.4); $\delta_j = 0$ (all-ones words) is handled explicitly wherever
  $\nu_3(\delta_j)$ appears, via the convention $\nu_3(0) = +\infty$; $a_j = j$ and
  $a_j = 0$; the degenerate equality case $2^j3^d = 2^d3^{a_j}$, which by unique
  factorisation forces $d = j$ and $a_j = d$, hence the all-ones word, hence
  $\delta_j = 0$ and no kill.
* **Empirical vs universal.** The only universal statements are those proved in the
  Proof section. The tables prove universal statements *about finite sets of residue
  classes* (e.g. "$\text{Aug}(8)$ has exactly 18 elements"), which is legitimate; they
  do not prove anything about $\text{Aug}(k)$ for $k > 24$.
* **Interchange of limits.** None taken.
* **Circular dependence.** Audited above.
* **Nonuniform estimates.** The thresholds $\theta_{j,d}$ are explicit rationals and the
  bound $B^{\mathrm{aug}}_k$ is an explicit maximum over a finite set; the quantifier
  order in L-9919.4(6) is "for every $n$ greater than a bound depending only on $k$",
  which is the uniformity actually needed.
* **Assumptions equivalent to the conjecture.** None. (H) is the *negation* of the
  conjecture, used only to define $\mu$; every [H]-tagged statement says so.
* **Incorrectly assumed independence.** The product decomposition
  $\text{Joint}(k,D) = \text{Aug}(k) \times \{u \not\equiv 0 \bmod 3\}$ is *proved*
  (L-9919.4(5)), not assumed from CRT heuristics; it is also verified computationally
  for all $k \le 14$, $D \le 3$ by a direct enumeration that does not assume the product
  form (PART E asserts the product identity only as a post-hoc `assert`).
* **Unproved properties of an infinite rewrite sequence.** The backward words of
  L-9919.8 are finite and their legality conditions are proved class-uniformly.
* **Finite computation extrapolated to infinite behaviour.** Explicitly avoided;
  see L-9919.5(c) and L-9919.8(3), both of which state the range and refuse the
  extrapolation.
* **Circularly defined counterexample.** No counterexample is proposed.
* **Symbolic object vs actual positive integer.** L-9919.2(3) is exactly this check for
  the descent iterates, and L-9919.8(1) carries the positivity thresholds explicitly.
* **Known soft spot (declared).** $B^{\mathrm{aug}}_k$ is defined via the *first* kill
  along the class tree with the *smallest* threshold, which is sharper than L-9909's
  max-over-all-classes $B_k$. The proof of L-9919.4(6) uses exactly that definition
  (least $k'$, then least $\theta$), and no other. A reviewer should re-derive this
  step independently; it is the one place where the bookkeeping could hide an error,
  and the numerical value ($319/13 < 25$) is so far below $10^6$ that any plausible
  error is harmless in practice but would still be an error.

---

## Adversarial tests

Finite verification, **not** proof. All arithmetic is exact (Python `int` / `Fraction`);
no floating point enters any claim (floats appear only in ratio columns printed for
readability). Scripts were run with CPython 3; each block below is followed by its
**real captured output**.

### Script 1 — `l9919_descent.py` (L-9919.1, L-9919.2, L-9919.3)

```python
#!/usr/bin/env python3
# l9919_descent.py -- adversarial finite verification for L-9919.1, L-9919.2, L-9919.3.
# Agent: fable-02-p13.  Python 3 stdlib only; every arithmetic claim exact (int).
# FINITE VERIFICATION, NOT PROOF.
def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def nu3(x):
    assert x != 0
    v = 0
    while x % 3 == 0:
        x //= 3; v += 1
    return v

# ---------------------------------------------------------------------------
# Test 1 (L-9919.1).  T-preimage characterization, exhaustive for n <= N1.
#   Claim: T^{-1}(n) cap Z^+ = {2n} u ({D(n)} iff n = 2 mod 3), D(n) := (2n-1)/3;
#   and when present D(n) is ODD, positive, T(D(n)) = n, and D(n) < n.
#   Completeness: T(x) >= x/2 for every x, so any preimage of n is <= 2n;
#   scanning every x <= 2*N1 therefore finds every preimage of every n <= N1.
# ---------------------------------------------------------------------------
N1 = 10**6
found = [[] for _ in range(N1 + 1)]
for x in range(1, 2 * N1 + 1):
    y = T(x)
    if y <= N1:
        found[y].append(x)
bad_sound = bad_complete = bad_odd = bad_lt = bad_int = 0
for n in range(1, N1 + 1):
    pred = {2 * n}
    if n % 3 == 2:
        num = 2 * n - 1
        if num % 3 != 0:
            bad_int += 1
        x = num // 3
        if x <= 0 or 3 * x != num:
            bad_int += 1
        if x % 2 != 1:
            bad_odd += 1
        if T(x) != n:
            bad_sound += 1
        if not (x < n):
            bad_lt += 1
        pred.add(x)
    else:
        if (2 * n - 1) % 3 == 0:
            bad_int += 1          # integrality must FAIL off the class
    if set(found[n]) != pred:
        bad_complete += 1
print("T1  n <= %d : integrality-iff failures %d, oddness %d, T(x)=n %d, x<n %d, set-equality %d"
      % (N1, bad_int, bad_odd, bad_sound, bad_lt, bad_complete))
print("T1  degenerate cases: n=1 preimages", sorted(found[1]), " n=2 preimages", sorted(found[2]),
      " D(2) =", (2*2-1)//3, " T(1) =", T(1))

# ---------------------------------------------------------------------------
# Test 2 (L-9919.2).  Descent depth by DIRECT SIMULATION vs the closed form
#   d(y) = nu_3(y+1), for every y <= N2, together with
#   D^i(y) = 2^i (y+1)/3^i - 1 for every 0 <= i <= d(y), and T^i(D^i(y)) = y.
#   Also records that positivity never binds (every intermediate is >= 1).
# ---------------------------------------------------------------------------
N2 = 10**6
bad_depth = bad_iter = bad_back = bad_pos = 0
maxdepth = 0
for y in range(1, N2 + 1):
    z = y; sim = 0
    while z % 3 == 2:
        z = (2 * z - 1) // 3
        assert z >= 1
        sim += 1
        if sim > 60: break
    if sim != nu3(y + 1):
        bad_depth += 1
    maxdepth = max(maxdepth, sim)
    d = sim
    z = y
    for i in range(1, d + 1):
        z = (2 * z - 1) // 3
        if 3**i * (z + 1) != 2**i * (y + 1):
            bad_iter += 1
        if z < 1:
            bad_pos += 1
        w = z
        for _ in range(i):
            w = T(w)
        if w != y:
            bad_back += 1
print("T2  y <= %d : depth-vs-nu3 mismatches %d, affine-iterate %d, T^i inverse %d, positivity %d, max depth %d"
      % (N2, bad_depth, bad_iter, bad_back, bad_pos, maxdepth))

# ---------------------------------------------------------------------------
# Test 3 (L-9919.2).  The 3-adic characterization
#     {y in Z^+ : d(y) >= d}  =  {y : y = -1 (mod 3^d)},
#   exhaustively over ALL residues mod 3^d for every d <= 8, each residue tested at
#   three positive lifts (which also probes "depends only on y mod 3^d").
# ---------------------------------------------------------------------------
def descends(y, d):
    """can the descent be applied d times to y, staying in Z^+ ?"""
    z = y
    for _ in range(d):
        if z % 3 != 2: return False
        z = (2*z - 1)//3
        if z < 1: return False
    return True

bad_class = 0; bad_local = 0; counts = []
for d in range(0, 9):
    M = 3**d; cnt = 0
    for r in range(M):
        lifts = [r + t*M for t in range(3) if r + t*M >= 1]
        vals = [descends(y, d) for y in lifts]
        if len(set(vals)) != 1: bad_local += 1
        v = vals[0]
        if v != (r % M == (M - 1) % M): bad_class += 1
        if v: cnt += 1
    counts.append((d, cnt))
print("T3  d <= 8 : locality failures %d, class-characterization failures %d;"
      % (bad_local, bad_class))
print("T3  #residues r mod 3^d with d(y) >= d :", counts, "(1 each: the class y = -1)")

# ---------------------------------------------------------------------------
# Test 4 (L-9919.3).  The amplified-floor ALGEBRA as an exact equivalence on integers:
#     D^d(T^j(n)) >= n     <=>     2^d (T^j(n)+1) >= 3^d (n+1),
#   for every n <= 20000, every j <= 30 and every d <= d(T^j(n)).
#   (Applied to n = mu this is exactly L-9919.3; here only the algebra is tested.)
# ---------------------------------------------------------------------------
bad_equiv = 0; checked = 0
for n in range(1, 20001):
    y = n
    for j in range(0, 31):
        d_max = nu3(y + 1)
        for d in range(0, d_max + 1):
            num = 2**d * (y + 1)
            assert num % 3**d == 0
            x = num // 3**d - 1                       # = D^d(T^j(n))
            lhs = (x >= n)
            rhs = (2**d * (y + 1) >= 3**d * (n + 1))
            if lhs != rhs: bad_equiv += 1
            checked += 1
        y = T(y)
print("T4  equivalence  [D^d(T^j(n)) >= n] <=> [2^d(T^j(n)+1) >= 3^d(n+1)] :",
      "%d failures out of %d checks" % (bad_equiv, checked))

# ---------------------------------------------------------------------------
# Test 5.  Small explicit table: the first orbit points of some n and their depths.
# ---------------------------------------------------------------------------
print("T5  sample: n=15, j -> (T^j(15), d = nu3(T^j+1), D^d(T^j(15)))")
y = 15
for j in range(0, 8):
    d = nu3(y + 1)
    x = (2**d * (y + 1)) // 3**d - 1
    print("      j=%d  T^j=%5d  d=%d  D^d=%5d %s" % (j, y, d, x, "  <-- below 15" if x < 15 else ""))
    y = T(y)
```

Output:

```text
T1  n <= 1000000 : integrality-iff failures 0, oddness 0, T(x)=n 0, x<n 0, set-equality 0
T1  degenerate cases: n=1 preimages [2]  n=2 preimages [1, 4]  D(2) = 1  T(1) = 2
T2  y <= 1000000 : depth-vs-nu3 mismatches 0, affine-iterate 0, T^i inverse 0, positivity 0, max depth 12
T3  d <= 8 : locality failures 0, class-characterization failures 0;
T3  #residues r mod 3^d with d(y) >= d : [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)] (1 each: the class y = -1)
T4  equivalence  [D^d(T^j(n)) >= n] <=> [2^d(T^j(n)+1) >= 3^d(n+1)] : 0 failures out of 1411332 checks
T5  sample: n=15, j -> (T^j(15), d = nu3(T^j+1), D^d(T^j(15)))
      j=0  T^j=   15  d=0  D^d=   15 
      j=1  T^j=   23  d=1  D^d=   15 
      j=2  T^j=   35  d=2  D^d=   15 
      j=3  T^j=   53  d=3  D^d=   15 
      j=4  T^j=   80  d=4  D^d=   15 
      j=5  T^j=   40  d=0  D^d=   40 
      j=6  T^j=   20  d=1  D^d=   13   <-- below 15
      j=7  T^j=   10  d=0  D^d=   10   <-- below 15
```

T5 is the smallest instance of the whole mechanism: $j \le 4$ merely retraces the
initial all-ones run (the caveat in L-9919.3), $j = 5$ has depth $0$, and $j = 6$
overshoots: $D(T^6(15)) = 13 < 15$. This is exactly why the class $15 \bmod 64$ is
removed from L-9909's survivor list by L-9919.

### Script 2 — `l9919_sieve.py` (L-9919.4, L-9919.5)

```python
#!/usr/bin/env python3
# l9919_sieve.py -- L-9919.4 / L-9919.5: the descent-augmented (joint) sieve.
# Agent: fable-02-p13.  Python 3 stdlib only; exact arithmetic (int / Fraction).
# FINITE COMPUTATION, NOT PROOF.
from fractions import Fraction
import sys
sys.setrecursionlimit(200000)

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def nu3(x):
    if x == 0: return None            # None encodes +infinity
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v

def word_of(r, k):
    n = r if r > 0 else r + (1 << k)
    w = []
    for _ in range(k):
        w.append(n % 2); n = T(n)
    return tuple(w)

def word_data(w):
    """a[0..k], rho[0..k], delta[0..k] with delta_j = rho_j + 2^j - 3^{a_j}."""
    k = len(w); a = [0]*(k+1); rho = [0]*(k+1)
    for i in range(k):
        a[i+1] = a[i] + w[i]; rho[i+1] = (3**w[i])*rho[i] + w[i]*(2**i)
    delta = [rho[j] + 2**j - 3**a[j] for j in range(k+1)]
    return a, rho, delta

def dmax(a, delta):
    """largest d with 3^d | (3^a n + delta_j) for EVERY n, i.e. min(a, nu_3(delta))."""
    v = nu3(delta)
    return a if v is None else min(a, v)

def kill_events(j, a, delta):
    """all class-uniform kill levels d (0 <= d <= dmax) with threshold theta;
       kill means: for every n > theta in the class, D^d(T^j(n)) < n."""
    out = []
    for d in range(0, dmax(a, delta) + 1):
        if 3**(a-d) < 2**(j-d):
            th = Fraction(delta // 3**d, 2**(j-d) - 3**(a-d)) - 1
            out.append((d, th))
    return out

# ===========================================================================
# PART A -- reproduce the L-9909 (d = 0 only) survivor sieve as a cross-check
# ===========================================================================
print("PART A  L-9909 uniform-descent sieve (d = 0 only), reproduced")
L9909_PUBLISHED = {1:[1],2:[3],3:[3,7],4:[7,11,15],5:[7,15,27,31],
                   6:[7,15,27,31,39,47,59,63],
                   7:[27,31,39,47,63,71,79,91,95,103,111,123,127],
                   8:[27,31,47,63,71,91,103,111,127,155,159,167,191,207,223,231,239,251,255]}
old_classes = {}
for k in range(1, 9):
    surv = []
    for r in range(1 << k):
        a, rho, delta = word_data(word_of(r, k))
        if all(3**a[j] >= 2**j for j in range(1, k+1)): surv.append(r)
    old_classes[k] = surv
    print("   k=%d  count=%2d  density=%-8s  matches L-9909 table: %s"
          % (k, len(surv), Fraction(len(surv), 1 << k), surv == L9909_PUBLISHED[k]))

# ===========================================================================
# PART B -- descent-augmented sieve: explicit classes (k <= 8) and counts
# ===========================================================================
print()
print("PART B  descent-augmented sieve (all d >= 0), explicit classes")
new_classes = {}
for k in range(1, 9):
    surv = []
    for r in range(1 << k):
        a, rho, delta = word_data(word_of(r, k))
        if all(not kill_events(j, a[j], delta[j]) for j in range(0, k+1)): surv.append(r)
    new_classes[k] = surv
    removed = [r for r in old_classes[k] if r not in surv]
    extra   = [r for r in surv if r not in old_classes[k]]
    print("   k=%d  count=%2d  density=%-9s  removed vs L-9909: %-9s  spurious extras: %s"
          % (k, len(surv), Fraction(len(surv), 1 << k), removed, extra))
print("   augmented survivor classes mod 2^k:")
for k in range(1, 9):
    print("     mod %3d : %s" % (1 << k, new_classes[k]))

# ===========================================================================
# PART C -- counts, densities and the exceptional bound B_k, to k = 24
# ===========================================================================
print()
print("PART C  counts / densities / exceptional bound, k <= 24")
KMAX = 24
cnt = [0]*(KMAX+1); Bk = [Fraction(0)]*(KMAX+1); mind = {}
def dfs(k, a, delta):
    cnt[k] += 1
    if k == KMAX: return
    p = 1 << k
    for b in (0, 1):
        a2 = a + b; d2 = 3*delta if b == 1 else delta + p
        ev = kill_events(k+1, a2, d2)
        if not ev:
            dfs(k+1, a2, d2)
        else:
            d, th = min(ev, key=lambda e: e[1])       # strongest (smallest-threshold) kill
            newonly = all(e[0] >= 1 for e in ev)      # no d = 0 (L-9909) kill available
            mind[("d>=1 only" if newonly else "d=0 available")] = \
                mind.get(("d>=1 only" if newonly else "d=0 available"), 0) + 1
            for kk in range(k+1, KMAX+1): Bk[kk] = max(Bk[kk], th)
dfs(0, 0, 0)
# L-9909 counts by DP for comparison
old = [0]*(KMAX+1); dp = {0: 1}; old[0] = 1
for j in range(1, KMAX+1):
    nd = {}
    for a, c in dp.items():
        for b in (0, 1):
            a2 = a + b
            if 3**a2 >= 2**j: nd[a2] = nd.get(a2, 0) + c
    dp = nd; old[j] = sum(dp.values())
print("    k    L-9909     augmented    old/new      B_k(augmented, exact)")
for k in range(1, KMAX+1):
    print("   %2d %9d %11d   %8.5f     %s" % (k, old[k], cnt[k], old[k]/cnt[k], Bk[k]))
print("   kill events by type (over all levels k <= %d):" % KMAX, dict(sorted(mind.items())))

# ===========================================================================
# PART D -- the 3-adic ("type-N", n-dependent) part of the sieve
#   For a class alive under PART B through level k and any j <= k with
#   3^{a_j} | delta_j, the extra condition is a congruence on u = n+1.
#   AUDIT: is the forbidden class always u = 0 mod 3 (i.e. n = 2 mod 3)?
# ===========================================================================
print()
print("PART D  3-adic collapse audit (u = n+1 coordinates)")
KA = 22
viol = []; tested = 0
def dfs2(k, a, delta):
    global tested
    v = nu3(delta)
    if v is None or v >= a:                     # 3^{a} | delta_j : type-(N) applies
        tested += 1
        t = 0 if v is None else (delta // 3**a) % 3
        if (-t) % 3 != 0:                       # forbidden class of u is not 0 mod 3
            viol.append((k, a, delta, (-t) % 3))
    if k == KA: return
    p = 1 << k
    for b in (0, 1):
        a2 = a+b; d2 = 3*delta if b == 1 else delta + p
        if not kill_events(k+1, a2, d2): dfs2(k+1, a2, d2)
dfs2(0, 0, 0)
print("   (class, j) pairs alive through k<=%d with 3^{a_j} | delta_j : %d" % (KA, tested))
print("   of those, forbidden residue of u = n+1 differs from 0 mod 3 :", len(viol), viol[:5])

# ===========================================================================
# PART E -- joint survivor counts modulo 2^k * 3^D, directly (no product ansatz)
# ===========================================================================
print()
print("PART E  joint survivors modulo 2^k * 3^D  (D = 1,2,3)")
def joint_count(k, D):
    M = 3**D; tot = 0; alive2 = 0
    for r in range(1 << k):
        a, rho, delta = word_data(word_of(r, k))
        if any(kill_events(j, a[j], delta[j]) for j in range(0, k+1)): continue
        alive2 += 1
        forb = [False]*M
        for j in range(0, k+1):
            v = nu3(delta[j])
            if not (v is None or v >= a[j]): continue
            tau = 0 if v is None else delta[j] // 3**a[j]
            for d in range(a[j]+1, D+1):
                mod = 3**(d - a[j]); c = (-tau) % mod
                for s in range(c, M, mod): forb[s] = True
        tot += M - sum(forb)
    return alive2, tot
print("    k   D    aug(2^k)   joint(2^k*3^D)   joint density      / L-9909 density")
for k in range(1, 15):
    for D in (1, 2, 3):
        a2, tot = joint_count(k, D)
        dj = Fraction(tot, (1 << k) * 3**D); d9 = Fraction(old[k], 1 << k)
        assert tot == a2 * 2 * 3**(D-1), (k, D, tot, a2)
        if D == 1:
            print("   %2d   %d   %8d   %12d   %-16s   %.5f"
                  % (k, D, a2, tot, str(dj), float(dj/d9)))
        else:
            print("   %2d   %d   %8d   %12d   %-16s   %.5f   (= product form: yes)"
                  % (k, D, a2, tot, str(dj), float(dj/d9)))

# ===========================================================================
# PART F -- BRUTE FORCE: predicted kills vs directly computed descents
#   For k <= 10 and every n in [1, 2^k * 9 * 8], compute the orbit and every
#   descent D^d(T^j(n)) directly and compare with the sieve prediction.
# ===========================================================================
print()
print("PART F  brute-force validation of the congruence solving")
for k in (4, 6, 8, 10):
    NMAX = (1 << k) * 9 * 8
    pred_tab = {}
    for r in range(1 << k):
        a, rho, delta = word_data(word_of(r, k))
        pred_tab[r] = (a, delta)
    mism = 0; killed_direct = 0; killed_pred = 0
    for n in range(1, NMAX+1):
        a, delta = pred_tab[n % (1 << k)]
        # direct: does some D^d(T^j(n)) with j<=k drop below n ?
        direct = False; y = n
        for j in range(0, k+1):
            z = y
            if z < n: direct = True            # d = 0 (this is the L-9909 descent)
            while z % 3 == 2:
                z = (2*z - 1)//3               # d -> d+1
                if z < n: direct = True
            if direct: break
            y = T(y)
        # predicted: some (j,d) with 3^d | (3^{a_j}(n+1)+delta_j) and
        #            (n+1)(2^{j-d}-3^{a_j-d}) > delta_j/3^d
        pred = False
        for j in range(0, k+1):
            aj = a[j]; dj = delta[j]
            for d in range(0, 45):
                if (3**aj * (n+1) + dj) % 3**d: continue     # 3^d | (T^j(n)+1)
                lhs = Fraction(n+1) * (Fraction(2)**(j-d) - Fraction(3)**(aj-d))
                rhs = Fraction(dj, 3**d)
                if lhs > rhs: pred = True; break
            if pred: break
        if direct: killed_direct += 1
        if pred: killed_pred += 1
        if direct != pred: mism += 1
    print("   k=%2d  n <= %6d : direct-kill %6d   predicted-kill %6d   mismatches %d"
          % (k, NMAX, killed_direct, killed_pred, mism))
```

Output:

```text
PART A  L-9909 uniform-descent sieve (d = 0 only), reproduced
   k=1  count= 1  density=1/2       matches L-9909 table: True
   k=2  count= 1  density=1/4       matches L-9909 table: True
   k=3  count= 2  density=1/4       matches L-9909 table: True
   k=4  count= 3  density=3/16      matches L-9909 table: True
   k=5  count= 4  density=1/8       matches L-9909 table: True
   k=6  count= 8  density=1/8       matches L-9909 table: True
   k=7  count=13  density=13/128    matches L-9909 table: True
   k=8  count=19  density=19/256    matches L-9909 table: True

PART B  descent-augmented sieve (all d >= 0), explicit classes
   k=1  count= 1  density=1/2        removed vs L-9909: []         spurious extras: []
   k=2  count= 1  density=1/4        removed vs L-9909: []         spurious extras: []
   k=3  count= 2  density=1/4        removed vs L-9909: []         spurious extras: []
   k=4  count= 3  density=3/16       removed vs L-9909: []         spurious extras: []
   k=5  count= 4  density=1/8        removed vs L-9909: []         spurious extras: []
   k=6  count= 7  density=7/64       removed vs L-9909: [15]       spurious extras: []
   k=7  count=12  density=3/32       removed vs L-9909: [79]       spurious extras: []
   k=8  count=18  density=9/128      removed vs L-9909: [207]      spurious extras: []
   augmented survivor classes mod 2^k:
     mod   2 : [1]
     mod   4 : [3]
     mod   8 : [3, 7]
     mod  16 : [7, 11, 15]
     mod  32 : [7, 15, 27, 31]
     mod  64 : [7, 27, 31, 39, 47, 59, 63]
     mod 128 : [27, 31, 39, 47, 63, 71, 91, 95, 103, 111, 123, 127]
     mod 256 : [27, 31, 47, 63, 71, 91, 103, 111, 127, 155, 159, 167, 191, 223, 231, 239, 251, 255]

PART C  counts / densities / exceptional bound, k <= 24
    k    L-9909     augmented    old/new      B_k(augmented, exact)
    1         1           1    1.00000     0
    2         1           1    1.00000     1
    3         2           2    1.00000     1
    4         3           3    1.00000     1
    5         4           4    1.00000     23/5
    6         8           7    1.14286     23/5
    7        13          12    1.08333     23/5
    8        19          18    1.05556     319/13
    9        38          32    1.18750     319/13
   10        64          57    1.12281     319/13
   11       128         102    1.25490     319/13
   12       226         192    1.17708     319/13
   13       367         324    1.13272     319/13
   14       734         593    1.23777     319/13
   15      1295        1100    1.17727     319/13
   16      2114        1855    1.13962     319/13
   17      4228        3407    1.24097     319/13
   18      7495        6329    1.18423     319/13
   19     14990       11698    1.28142     319/13
   20     27328       22384    1.22087     319/13
   21     46611       39549    1.17856     319/13
   22     93222       73718    1.26458     319/13
   23    168807      139084    1.21371     319/13
   24    286581      243479    1.17703     319/13
   kill events by type (over all levels k <= 24): {'d=0 available': 49797, 'd>=1 only': 7198}

PART D  3-adic collapse audit (u = n+1 coordinates)
   (class, j) pairs alive through k<=22 with 3^{a_j} | delta_j : 23
   of those, forbidden residue of u = n+1 differs from 0 mod 3 : 0 []

PART E  joint survivors modulo 2^k * 3^D  (D = 1,2,3)
    k   D    aug(2^k)   joint(2^k*3^D)   joint density      / L-9909 density
    1   1          1              2   1/3                0.66667
    1   2          1              6   1/3                0.66667   (= product form: yes)
    1   3          1             18   1/3                0.66667   (= product form: yes)
    2   1          1              2   1/6                0.66667
    2   2          1              6   1/6                0.66667   (= product form: yes)
    2   3          1             18   1/6                0.66667   (= product form: yes)
    3   1          2              4   1/6                0.66667
    3   2          2             12   1/6                0.66667   (= product form: yes)
    3   3          2             36   1/6                0.66667   (= product form: yes)
    4   1          3              6   1/8                0.66667
    4   2          3             18   1/8                0.66667   (= product form: yes)
    4   3          3             54   1/8                0.66667   (= product form: yes)
    5   1          4              8   1/12               0.66667
    5   2          4             24   1/12               0.66667   (= product form: yes)
    5   3          4             72   1/12               0.66667   (= product form: yes)
    6   1          7             14   7/96               0.58333
    6   2          7             42   7/96               0.58333   (= product form: yes)
    6   3          7            126   7/96               0.58333   (= product form: yes)
    7   1         12             24   1/16               0.61538
    7   2         12             72   1/16               0.61538   (= product form: yes)
    7   3         12            216   1/16               0.61538   (= product form: yes)
    8   1         18             36   3/64               0.63158
    8   2         18            108   3/64               0.63158   (= product form: yes)
    8   3         18            324   3/64               0.63158   (= product form: yes)
    9   1         32             64   1/24               0.56140
    9   2         32            192   1/24               0.56140   (= product form: yes)
    9   3         32            576   1/24               0.56140   (= product form: yes)
   10   1         57            114   19/512             0.59375
   10   2         57            342   19/512             0.59375   (= product form: yes)
   10   3         57           1026   19/512             0.59375   (= product form: yes)
   11   1        102            204   17/512             0.53125
   11   2        102            612   17/512             0.53125   (= product form: yes)
   11   3        102           1836   17/512             0.53125   (= product form: yes)
   12   1        192            384   1/32               0.56637
   12   2        192           1152   1/32               0.56637   (= product form: yes)
   12   3        192           3456   1/32               0.56637   (= product form: yes)
   13   1        324            648   27/1024            0.58856
   13   2        324           1944   27/1024            0.58856   (= product form: yes)
   13   3        324           5832   27/1024            0.58856   (= product form: yes)
   14   1        593           1186   593/24576          0.53860
   14   2        593           3558   593/24576          0.53860   (= product form: yes)
   14   3        593          10674   593/24576          0.53860   (= product form: yes)

PART F  brute-force validation of the congruence solving
   k= 4  n <=   1152 : direct-kill   1007   predicted-kill   1007   mismatches 0
   k= 6  n <=   4608 : direct-kill   4271   predicted-kill   4271   mismatches 0
   k= 8  n <=  18432 : direct-kill  17567   predicted-kill  17567   mismatches 0
   k=10  n <=  73728 : direct-kill  70991   predicted-kill  70991   mismatches 0
```

Notes on what PART F tests: the "direct" side computes orbits and descents with no
reference to $a_j$, $\delta_j$ or any congruence; the "predicted" side uses only
$n \bmod 2^k$ and the congruence solving of L-9919.4(2)-(3). Zero mismatches over
$1 \le n \le 2^k \cdot 72$ for $k \in \{4,6,8,10\}$. An earlier version of this test
reported mismatches; the cause was a bug in the *direct* side (it omitted the $d = 0$
case), not in the sieve — recorded here because a reviewer should re-run it rather than
trust it.

### Script 3 — `l9919_orbits.py` (cross-check against real orbits, $n \le 10^6$)

```python
#!/usr/bin/env python3
# l9919_orbits.py -- adversarial cross-check of the L-9919 joint sieve against
# DIRECTLY COMPUTED orbits and descents, for every n <= 10^6.
# Agent: fable-02-p13.  Python 3 stdlib only, exact integer arithmetic.
# FINITE VERIFICATION, NOT PROOF.
from fractions import Fraction

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2
def nu3(x):
    if x == 0: return None
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v

J = 20                      # sieve depth (= k)
NMAX = 10**6
BJ = Fraction(319, 13)      # B_k(augmented) for k <= 24, from l9919_sieve.py PART C

# ---- sieve side: augmented survivor classes mod 2^J, via the parity word ----
def word_data_from(n, k):
    a = [0]*(k+1); rho = [0]*(k+1); x = n
    for i in range(k):
        b = x % 2
        a[i+1] = a[i] + b; rho[i+1] = (3**b)*rho[i] + b*(2**i)
        x = T(x)
    return a, [rho[j] + 2**j - 3**a[j] for j in range(k+1)]

def uniform_killed(a, delta, k):
    for j in range(0, k+1):
        v = nu3(delta[j]); m = a[j] if v is None else min(a[j], v)
        if 3**(a[j]-m) < 2**(j-m): return True
    return False

# cache the verdict per residue class mod 2^J using the least positive representative
print("building augmented-survivor verdicts for all %d classes mod 2^%d ..." % (1 << J, J))
verdict = bytearray(1 << J)
for r in range(1 << J):
    n0 = r if r > 0 else (1 << J)
    a, delta = word_data_from(n0, J)
    verdict[r] = 0 if uniform_killed(a, delta, J) else 1
print("  augmented survivor classes mod 2^%d : %d" % (J, sum(verdict)))

# ---- direct side: for each n, is there (j <= J, d >= 0) with D^d(T^j(n)) < n ? ----
mismatch = []; alive_direct = 0; alive_sieve = 0; below_B = 0
for n in range(1, NMAX + 1):
    y = n; direct_alive = True
    for j in range(0, J + 1):
        z = y
        if z < n: direct_alive = False; break        # d = 0
        while z % 3 == 2:
            z = (2*z - 1)//3
            if z < n: direct_alive = False; break
        if not direct_alive: break
        y = T(y)
    sieve_alive = bool(verdict[n % (1 << J)]) and (n % 3 != 2)
    if direct_alive: alive_direct += 1
    if sieve_alive: alive_sieve += 1
    if n > BJ and direct_alive != sieve_alive:
        mismatch.append(n)
    if n <= BJ: below_B += 1
print("n <= %d, J = %d :" % (NMAX, J))
print("  survive ALL directly computed descent tests : %d" % alive_direct)
print("  predicted alive by the joint sieve          : %d" % alive_sieve)
print("  mismatches among n > B_J = %s              : %d %s"
      % (BJ, len(mismatch), mismatch[:10]))
print("  (n <= B_J excluded from the comparison: %d values)" % below_B)

# ---- soundness spot-audit: every predicted kill is realised by a genuine
#      T-preimage chain landing strictly below n ------------------------------
bad = 0; checked = 0
for n in range(3, 200001, 2):
    if verdict[n % (1 << J)] and n % 3 != 2:   # sieve says alive -> nothing to audit
        continue
    y = n; wit = None
    for j in range(0, J + 1):
        z = y; d = 0
        while True:
            if z < n and (j > 0 or d > 0): wit = (j, d, z); break
            if z % 3 != 2: break
            z = (2*z - 1)//3; d += 1
        if wit: break
        y = T(y)
    if wit is None:
        if n > BJ: bad += 1
        continue
    j, d, z = wit
    w = z
    for _ in range(d): w = T(w)          # d descent steps undone
    for _ in range(j): pass
    # w must equal T^j(n)
    t = n
    for _ in range(j): t = T(t)
    if w != t or z >= n or z < 1: bad += 1
    checked += 1
print("  soundness audit on odd n < 200000 predicted dead: %d witnesses verified, %d failures"
      % (checked, bad))

# ---- the mod 3 statement, directly -----------------------------------------
bad3 = 0
for n in range(2, NMAX + 1, 3):        # n = 2 mod 3
    x = (2*n - 1)//3
    if not (x >= 1 and x % 2 == 1 and T(x) == n and x < n): bad3 += 1
print("  n = 2 (mod 3), n <= %d : descent-witness failures %d" % (NMAX, bad3))
```

Output:

```text
building augmented-survivor verdicts for all 1048576 classes mod 2^20 ...
  augmented survivor classes mod 2^20 : 22384
n <= 1000000, J = 20 :
  survive ALL directly computed descent tests : 14235
  predicted alive by the joint sieve          : 14234
  mismatches among n > B_J = 319/13              : 0 []
  (n <= B_J excluded from the comparison: 24 values)
  soundness audit on odd n < 200000 predicted dead: 97183 witnesses verified, 0 failures
  n = 2 (mod 3), n <= 1000000 : descent-witness failures 0
```

The single-unit difference $14235$ vs $14234$ is entirely accounted for by the $24$
values $n \le B_J = 319/13$ excluded from the comparison, where the sieve is not
claimed to apply; there are **zero** mismatches above the bound. The survivor class
count $22384$ agrees with PART C at $k = 20$. Since every $n \le 10^6$ reaches $1$
(X-9901), none of these $n$ is a counterexample, so no *conditional* claim of this file
is even applicable to them; what is tested here is the **soundness of the sieve's
congruence bookkeeping** against genuinely computed orbits.

### Script 4 — `l9919_backword.py` (L-9919.8, the extension)

```python
#!/usr/bin/env python3
# l9919_backword.py -- L-9919.8: the FULL class-uniform backward-word sieve.
# A backward word is a sequence of moves applied to y = T^j(n), written in the
# coordinate u = z+1 :   D : u -> (2/3)u  (legal iff 3 | u) ,  M : u -> 2u-1  (z -> 2z).
# State is kept exactly as u_cur = (P*u + Q)/2^s with u = n+1.
# Agent: fable-02-p13.  Python 3 stdlib only, exact arithmetic.  FINITE COMPUTATION.
from fractions import Fraction

def T(n): return n//2 if n%2==0 else (3*n+1)//2
def nu3(x):
    if x==0: return None
    v=0
    while x%3==0: x//=3; v+=1
    return v
def word_data_from(n,k):
    a=[0]*(k+1); rho=[0]*(k+1); x=n
    for i in range(k):
        b=x%2; a[i+1]=a[i]+b; rho[i+1]=(3**b)*rho[i]+b*(2**i); x=T(x)
    return a,[rho[j]+2**j-3**a[j] for j in range(k+1)]
def pure_killed(a,delta,k):
    for j in range(0,k+1):
        v=nu3(delta[j]); m=a[j] if v is None else min(a[j],v)
        if 3**(a[j]-m)<2**(j-m): return True
    return False

def backword_kill(j, a, delta, L):
    """Least n-threshold theta such that EVERY n > theta in the class admits a
       class-uniform backward word (length <= L) from T^j(n) landing strictly below n.
       Thresholds include the positivity requirement z >= 1 at every node."""
    S = 2**j; best = None
    # stack entries: (P, Q, depth, pos_threshold_so_far, word)
    stack = [(3**a, delta, 0, Fraction(-1), "")]
    while stack:
        p,q,dep,pos,wd = stack.pop()
        if S > p:
            th = max(Fraction(q, S-p) - 1, pos)
            if best is None or th < best[0]: best = (th, wd)
        rem = L - dep
        if rem > 0 and Fraction(p*2**rem, 3**rem) < S:
            if p % 3 == 0 and q % 3 == 0:
                p2,q2 = 2*p//3, 2*q//3
                # positivity of the new node: (p2 u + q2)/2^s >= 2  <=>  n >= (2^{s+1}-q2)/p2 - 1
                pos2 = max(pos, Fraction(2*S - q2, p2) - 1)
                stack.append((p2,q2,dep+1,pos2,wd+"D"))
            p2,q2 = 2*p, 2*q - S
            pos2 = max(pos, Fraction(2*S - q2, p2) - 1)
            stack.append((p2,q2,dep+1,pos2,wd+"M"))
    return best

L = 12
print("k    L-9909    pure-descent (L-9919.4)   full backward-word (L-9919.8)   max threshold")
for K in (6,8,10,12,14,16):
    old=0; pure=0; full=0; mx=None
    for r in range(1<<K):
        n0 = r if r>0 else (1<<K)
        a,delta = word_data_from(n0,K)
        if all(3**a[j] >= 2**j for j in range(1,K+1)): old += 1
        if pure_killed(a,delta,K): continue
        pure += 1
        hit=None
        for j in range(0,K+1):
            e = backword_kill(j, a[j], delta[j], L)
            if e is not None and (hit is None or e[0] < hit[0]): hit = e
        if hit is None: full += 1
        elif mx is None or hit[0] > mx: mx = hit[0]
    print("%2d  %7d   %19d   %25d   %s" % (K, old, pure, full, mx))

# explicit verified witness for the smallest class that only the extension kills
print()
print("witness: class 63 mod 256 (a pure-descent survivor, killed by the word DMDDDD at j=8)")
for n in (63, 319, 575, 63+256*97):
    y=n
    for _ in range(8): y=T(y)
    z=y; seq=[y]
    for mv in "DMDDDD":
        z = (2*z-1)//3 if mv=="D" else 2*z
        seq.append(z)
    fwd=z
    for _ in range(6): fwd=T(fwd)
    print("  n=%7d  T^8(n)=%9d  backward word DMDDDD -> %8d   (< n: %s ; T^6 back to T^8(n): %s)"
          % (n, y, z, z<n, fwd==y))
    print("       chain:", seq)
```

Output:

```text
k    L-9909    pure-descent (L-9919.4)   full backward-word (L-9919.8)   max threshold
 6        8                     7                           7   None
 8       19                    18                          16   5/3
10       64                    57                          46   5/3
12      226                   192                         144   159/13
14      734                   593                         436   159/13
16     2114                  1855                        1366   159/13

witness: class 63 mod 256 (a pure-descent survivor, killed by the word DMDDDD at j=8)
  n=     63  T^8(n)=      182  backward word DMDDDD ->       47   (< n: True ; T^6 back to T^8(n): True)
       chain: [182, 121, 242, 161, 107, 71, 47]
  n=    319  T^8(n)=      911  backward word DMDDDD ->      239   (< n: True ; T^6 back to T^8(n): True)
       chain: [911, 607, 1214, 809, 539, 359, 239]
  n=    575  T^8(n)=     1640  backward word DMDDDD ->      431   (< n: True ; T^6 back to T^8(n): True)
       chain: [1640, 1093, 2186, 1457, 971, 647, 431]
  n=  24895  T^8(n)=    70895  backward word DMDDDD ->    18671   (< n: True ; T^6 back to T^8(n): True)
       chain: [70895, 47263, 94526, 63017, 42011, 28007, 18671]
```

### Reproducibility self-check

All four blocks above were re-extracted from this Markdown file, written to fresh
files, executed, and their stdout compared byte-for-byte with the recorded outputs;
all four matched. Total runtime on the authoring machine: about 25 s. No block is a
placeholder; every number displayed above was produced by the code shown immediately
above it.

### Negative / sharpness probes attempted

1. **Is the mod-$3^D$ direction really exhausted at $D = 1$?** PART E computes joint
   survivors for $D = 1,2,3$ *without* assuming the product form (it enumerates the
   forbidden residues mod $3^D$ class by class) and finds the density unchanged. The
   proof of L-9919.4(5) explains why. Attempted counterexample: a class with
   $\nu_3(\delta_j) = a_j$ and $\delta_j \ne 0$ would give a *different* forbidden class
   mod $3$; PART D searched all classes alive through $k \le 22$ and found $23$
   branch-(N) instances, **all** of them the degenerate $\delta_j = 0$ (all-ones prefix)
   case, and **zero** with a forbidden residue other than $u \equiv 0$.
2. **Does the augmentation ever wrongly remove a class?** PART B reports "spurious
   extras: []" at every $k \le 8$, i.e. $\text{Aug}(k) \subseteq$ L-9909's list, as the
   theory demands; and Script 3 checks $10^6$ integers against directly computed orbits
   with zero mismatches above the bound.
3. **Is the gain exponential?** Deliberately probed and **refuted for the computed
   range**: the rate difference $\frac1k\log_2(\text{old}/\text{new})$ decreases with
   $k$ (see L-9919.5(c)); an exponential gain would require it to be bounded below.
4. **Is the descent family maximal?** Deliberately probed and **refuted**: L-9919.8
   exhibits the class $63 \bmod 256$, an augmented $8$-survivor killed by the mixed
   backward word $\mathsf{DMDDDD}$, verified on four explicit representatives.
5. **Does the full backward tree give still more?** Yes, but not congruence-locally:
   e.g. $27 < 31$ and $T^3(27) = 31$, so $31$ can never be minimal — a constraint of a
   completely different (non-congruence) type. Recorded so that L-9919's sieve is not
   mistaken for the strongest available minimality constraint.

---

## Remaining uncertainty

* **Highest-risk step:** the definition and use of $B^{\mathrm{aug}}_k$ in
  L-9919.4(6) (least level, then least threshold). It is correct as written, but it is
  bookkeeping-heavy and is the place I would attack first as a reviewer. The numerical
  values are so small ($\le 319/13 < 25$) that any error there cannot affect the
  conclusions, given $\mu > 10^6$; but it could affect the *stated* bound.
* **Second:** the claim that branch (U)/(V)/(N) is an exhaustive trichotomy relies on
  the convention $\nu_3(0) = +\infty$ being applied consistently. I have checked every
  occurrence; a reviewer should re-check the $\delta_j = 0$ (all-ones prefix) case
  independently, since that is where a silent off-by-one would hide.
* **Third:** L-9919.5(c) and L-9919.8(3) are finite-range statements. I am confident
  the gain is a bounded factor over $k \le 30$; I am **not** claiming, and have not
  proved, that it is bounded as $k \to \infty$. The observed decay of the rate
  difference is suggestive, not conclusive — the sequence oscillates with the
  continued-fraction structure of $\log_2 3$ and $k \le 30$ is a short window.
* **Fourth:** L-9919.8 is exploratory. Its soundness proof I believe complete; its
  computational characterisation uses a search bounded by word length $\le 12$ and a
  pruning rule (`p*(2/3)^rem < 2^s`), so the reported counts are *upper* bounds for the
  true backward-word survivor counts at those $k$ (a longer search can only kill more).
* **Not uncertain:** L-9919.1, L-9919.2 and L-9919.3 are short and elementary and I am
  confident in them; L-9919.7's negative verdict is the honest reading of the data and
  I would defend it against a more optimistic framing.

---

## Suggested next attack

1. **Settle L-9919.8 properly.** Give the backward-word sieve a clean recursive
   definition (state $(P,Q)$ modulo a suitable modulus), prove the analogue of the
   $3$-adic collapse for it (does it too factorise?), and push the computation to
   $k \approx 26$ with pruning to decide whether the gain over L-9909 is a constant
   factor or a genuine rate improvement. This is the only direction in this file with
   visible headroom, and it is a self-contained, finite, purely computational question
   modulo the (already proved) soundness lemma.
2. **Rate question.** Prove or refute: $\lim_k \frac1k \log_2 \bigl(|\text{L-9909}(k)|/|\text{Aug}(k)|\bigr) = 0$.
   A ballot-problem / conditioned-random-walk argument (the surviving walks sit at
   height $\asymp\sqrt{k}$ above the line $a_j = j\gamma$) should decide it; if the
   limit is $0$, this file's negative verdict becomes a theorem rather than a
   measurement, which is worth recording.
3. **Cheap win for search programs.** Ship $\mu \equiv 3, 7 \pmod{12}$ together with the
   18-element mod-$256$ list; it is a factor $\approx 1.8$ over L-9909.5's packaging at
   zero cost, and the discharge condition ($\mu > 25$) is trivially met.
4. **Do not** look for a genuinely two-dimensional mod-$6^k$ sieve from this family:
   L-9919.4(5) proves there is none. If a mod-$3^D$ condition with $D \ge 2$ is wanted,
   it must come from a family whose $3$-adic branch is not dominated by the $j = 0$
   event — e.g. constraints on $\nu_3$ of *cycle* quantities, which this file says
   nothing about.

---

*Authored by fable-02-p13, 2026-07-25. Status PROPOSED: no independent verification yet.
Conditional statements are tagged [H] throughout; nothing here asserts that a
counterexample exists.*
