# L-9927 — S-closure refines the product bound: the mod-3 surjectivity sieve, 118 new eliminated cycle lengths (80 beyond the old ceiling 207), the exact new threshold 1039, and two ceiling theorems for the entire allowed-set family

```text
Claim ID:      L-9927
Title:         What S-closure adds to the sorted/profile product bounds: every cycle
               element is an S-image, hence not divisible by 3; the closure-sieved
               sorted bound 2^K <= prod (3 + 1/u_k) with u_k = 3k+7+(k mod 2); the
               exact 166-value elimination set E_U (max 1024, complete over all m),
               of which 118 values are new and 80 exceed 207; width envelope
               (1/9)log2 m + O(1); exact termination threshold m_U = 1039; per-class
               closure floors; NULL verdict in the verified-floor regime; and a
               universal ceiling: no allowed-set sieve, of any thinness, can
               eliminate all large m
Status:        PROPOSED
Authoring agent:   fable-02-p21
Reviewing agents:  (none yet)
Created:       2026-07-27
Last updated:  2026-07-27
Dependencies:  NOTATION.md (D-9903 odd part, D-9904 Syracuse map S and step exponent
               a(x) = nu_2(3x+1) >= 1, D-9905 trivial cycle (1), D-9908 S-cycle
               notation x_1 -> ... -> x_m -> x_1, least period m, a_i, K = sum a_i,
               x_min; D-9909 counterexample; empty-product convention).
               foundations/L-9905 (PROVED, fable-02-v4) — L-9905.2 (2^K > 3^m) and
               L-9905.3 (product formula).  BOTH RE-DERIVED INLINE (Step 1).
               foundations/L-9906 (PROVED, fable-02-v5) — L-9906.2 (every element of
               a nontrivial S-cycle is >= 7).  RE-DERIVED INLINE (Step 2b).
               foundations/L-9909 (PROVED, fable-02-v7) — L-9909.1 (Syracuse
               preimages; n == 0 mod 3 is a leaf; preimage-residue rotation mod 3).
               The three facts used are RE-PROVED INLINE (Step 3); L-9909 is cited
               as in-repo provenance of the leaf fact.
               foundations/L-9912 (PROVED, fable-02-v14) — L-9912.5 (exponent-residue
               dictionary).  The t = 1 case and the general class structure are
               RE-DERIVED INLINE where used (Steps 4, 8).
               foundations/L-9917 (PROVED, fable-02-v17) — LOAD-BEARING in one place:
               L-9917.1(1) (elements of a least-period-m cycle are pairwise
               distinct), restated with a two-line proof sketch in Step 2a.  Its
               numbers P(m), the window W*(m), the 46-value set E and the threshold
               m_0 = 196 are RECOMPUTED from scratch here (test A/T4) and used for
               comparison; the containment E subset E_U is also a one-line theorem
               (Step 5d).
               foundations/L-9920 (PROVED, fable-02-v22) — comparison target only:
               its E' = E + {13, 79}, threshold 208, and beta_t floors are quoted;
               13, 79 in E_U is verified by this file's own certificates; nothing
               here is inferred from L-9920.  This file answers its Q-9920-A.
               foundations/L-9913 (PROVED, fable-02-v18) — used ONLY in L-9927.7 as
               the comparison target (its (V_F) hypothesis and the values
               m*(10^6) = 2966, m*(10^9) = 47468); (V_F) is not assumed anywhere
               else in this file.
               research/foundations/NEGATIVE_RESULTS.md §3.4 — context only: the
               p = 3 WORD-level sieve is vacuous; this file's p = 3 ELEMENT-level
               sieve is not, and the two findings are consistent (see Motivation).
Scope:         L-9927.1 (the surjectivity / mod-3 facts) holds for EVERY S-cycle of
               the formula x -> (3x+1)/2^{nu_2(3x+1)} on the nonzero odd integers of
               either sign, trivial cycle included; it needs no positivity.
               L-9927.2–.6 are about nontrivial S-cycles on the POSITIVE odd
               integers (D-9908): they use positivity (via 2^K > 3^m) and the floor
               x_i >= 7, and are FALSE or vacuous for the trivial cycle (1) and for
               the negative cycles (-1), (-5,-7), (-17,...) — test A/T3 identifies
               the failing hypothesis in each case.  The elimination set E_U of
               L-9927.4 and the threshold m_U = 1039 are EXACT integer
               computations, complete over ALL m >= 1 (not artefacts of a search
               range).  L-9927.7 is conditional on L-9913's (V_F) and is a NULL
               (no-change) statement.  L-9927.8 quantifies over ALL valid allowed
               sets, including any future refinement of this family.
Related counterexample candidates: none
```

---

## Statement

Throughout, $S$ is the Syracuse map (D-9904), $S(x) = (3x+1)/2^{\nu_2(3x+1)}$, with step
exponent $a(x) := \nu_2(3x+1) \ge 1$; the same formula defines $S$ on every nonzero odd
integer of either sign (as in foundations/L-9905, Remark 1.2). An $S$-cycle is written
as in D-9908: $x_1 \to x_2 \to \dots \to x_m \to x_1$, least period $m \ge 1$, cyclic
indices $x_{i+m} = x_i$, exponents $a_i := a(x_i)$, $K := \sum_{i=1}^m a_i$,
$x_{\min} := \min_i x_i$, $x_{\max} := \max_i x_i$, cycle set
$\mathcal{C} := \{x_1, \dots, x_m\}$. The **trivial** cycle is the fixed point $(1)$
(D-9905). $\alpha := \log_2 3$, and $\kappa(m) := \mathrm{bl}(3^m)$ is the bit length of
$3^m$, i.e. the least integer $K$ with $2^K > 3^m$.

**The closure-sieved allowed set.** Define
$$U \;:=\; \{\, x \in \mathbb{Z} \;:\; x \text{ odd},\ x \ge 7,\ 3 \nmid x \,\}
\qquad\text{with increasing enumeration}\qquad
u_k \;=\; 3k + 7 + (k \bmod 2) \quad (k \ge 0),$$
so $(u_0, u_1, u_2, \dots) = (7, 11, 13, 17, 19, 23, 25, 29, 31, 35, \dots)$. Put
$$P_U(m) := \prod_{k=0}^{m-1}\Bigl(3 + \frac{1}{u_k}\Bigr) = \frac{N_U(m)}{D_U(m)},
\qquad N_U(m) := \prod_{k<m}(3u_k + 1),\quad D_U(m) := \prod_{k<m} u_k,$$
$$R_U(m) := \frac{P_U(m)}{3^m} = \prod_{k<m}\Bigl(1 + \frac{1}{3u_k}\Bigr),
\qquad \mathrm{Wd}_U(m) := \log_2 R_U(m),$$
$$\boxed{\;W_U(m) \;:=\; \{\, K \in \mathbb{Z} : 3^m < 2^K \le P_U(m) \,\}
      \;=\; \{\, K \in \mathbb{Z} : 3^m < 2^K \ \text{and}\ 2^K D_U(m) \le N_U(m) \,\},\;}$$
to be compared with foundations/L-9917's $W^*(m)$ (allowed set = all distinct odds
$\ge 7$; sorted floors $7 + 2k$) and foundations/L-9920's $W'(m)$ (adds the
exponent–residue dictionary).

---

**L-9927.1 (S-closure at the set level: the surjectivity sieve; sign-agnostic).**

1. **(Every element is an image.)** In every $S$-cycle (either sign, trivial included),
   every element is the $S$-image of another element: $x_i = S(x_{i-1})$ for all $i$
   (cyclically; in particular $x_1 = S(x_m)$). Hence $S|_{\mathcal C}$ is a bijection
   of $\mathcal C$ onto itself.
2. **(Images avoid multiples of 3.)** For every nonzero odd integer $y$ (either sign),
   $3 \nmid S(y)$. Consequently **no element of any $S$-cycle is divisible by $3$.**
   (For the trivial cycle: $3 \nmid 1$. Verified on all four known cycles of the
   formula, including the three negative ones — test A/T3.)
3. **(Exact image set; the sieve is complete at every depth.)** On the positive odd
   integers, $\mathrm{image}(S) = \{\text{odd } z \ge 1 : 3 \nmid z\}$ exactly: if
   $z \equiv 2 \pmod 3$ then $y = (2z-1)/3$ is a positive odd integer with
   $S(y) = z$ (and $a(y) = 1$); if $z \equiv 1 \pmod 3$ then $y = (4z-1)/3$ works
   (with $a(y) = 2$). Moreover every $z$ with $3 \nmid z$ has infinitely many
   preimages $y$ with $3 \nmid y$ (consecutive preimages satisfy
   $y' = 4y + 1$, which walks through all residues mod $3$), so
   $$\mathrm{image}(S^k) \;=\; \{\text{odd } z \ge 1 : 3 \nmid z\} \qquad\text{for every } k \ge 1 :$$
   **iterated surjectivity yields no plain congruence constraint beyond
   $3 \nmid z$, at any depth.** (What survives at depth $2$ is only a constraint
   *coupled to the predecessor's exponent* — recorded as Q-9927-B.)

**L-9927.2 (S-closure at the element level: extremal and local facts).** Let
$x_1 \to \dots \to x_m \to x_1$ be a **nontrivial** $S$-cycle on the positive odd
integers. Then:

1. **(Minimum.)** $a(x_{\min}) = 1$ exactly, and $S(x_{\min}) = (3x_{\min}+1)/2 \in
   \mathcal{C}$ is a strictly larger element. Consequently $x_{\min} \equiv 3 \pmod 4$,
   and with L-9927.1(2), $x_{\min} \equiv 7$ or $11 \pmod{12}$.
   (For the trivial cycle $a(1) = 2$: the proof uses the floor $x_{\min} \ge 7$. On the
   negative cycles the statement FAILS — the minima of the $(-5,-7)$ and $(-17,\dots)$
   cycles have exponents $2$ and $4$ — positivity is necessary; test A/T3.)
2. **(Maximum.)** $a(x_{\max}) \ge 2$; hence $x_{\max} \equiv 1 \pmod 4$ and, with
   L-9927.1(2), $x_{\max} \equiv 1$ or $5 \pmod{12}$.
3. **(Forced-exponent-1 slab.)** Every element $y \in \mathcal{C}$ with
   $y < (4x_{\min} - 1)/3$ has $a(y) = 1$ (so the slab
   $[x_{\min},\, (4x_{\min}-1)/3)$, which contains $x_{\min}$, consists entirely of
   elements $\equiv 3 \bmod 4$, indeed $\equiv 7, 11 \bmod{12}$).
4. **(Per-class image floors.)** Every $y \in \mathcal{C}$ with $a(y) = t$ satisfies
   $$y \;\ge\; \frac{2^t\,x_{\min} - 1}{3} \;\ge\; \frac{7 \cdot 2^t - 1}{3},$$
   because $S(y) = (3y+1)/2^t \in \mathcal{C}$ forces $S(y) \ge x_{\min} \ge 7$.
   (Vacuous for $t = 1$; a genuinely new constraint for every $t \ge 2$.)

**L-9927.3 (the closure-sieved sorted product bound).** Let
$x_1 \to \dots \to x_m \to x_1$ be a nontrivial $S$-cycle. Then:

1. the elements are $m$ pairwise-distinct members of $U$ (distinct by least
   periodicity; $\ge 7$ by the elementary floor; $3 \nmid x_i$ by L-9927.1(2)), so the
   increasing rearrangement satisfies
   $$x_{(k)} \;\ge\; u_k \;=\; 3k + 7 + (k \bmod 2) \qquad (0 \le k \le m-1);$$
2. consequently
   $$\boxed{\;3^m \;<\; 2^K \;=\; \prod_{i=1}^m\Bigl(3+\frac{1}{x_i}\Bigr) \;\le\; P_U(m),
   \qquad\text{i.e.}\qquad K \in W_U(m);\;}$$
3. $u_k \ge 7 + 2k$ for every $k$, with strict inequality for every $k \ge 1$; hence
   $P_U(m) \le P(m)$ (foundations/L-9917's sorted bound), strictly for $m \ge 2$, and
   $W_U(m) \subseteq W^*(m)$. **The closure-sieved window is never worse than
   L-9917's and is strictly narrower in real length for every $m \ge 2$.**

**L-9927.4 (the exact elimination set; complete over all $m$).** Define
$\mathcal{E}_U := \{\, m \ge 1 : W_U(m) = \varnothing \,\}$. Then $\mathcal{E}_U$ is
**finite** and equals **exactly** the following $166$-element set, with
$\max \mathcal{E}_U = 1024$:

```text
E_U = { 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 18, 19, 21, 23, 24, 26, 28,
        30, 31, 33, 35, 36, 38, 40, 43, 45, 48, 50, 52, 53, 55, 57, 60, 62, 64,
        65, 67, 69, 72, 74, 77, 79, 81, 84, 86, 89, 91, 96, 98, 101, 103, 106,
        108, 110, 113, 115, 118, 120, 125, 127, 130, 132, 137, 139, 142, 144,
        149, 154, 156, 159, 161, 166, 168, 171, 173, 178, 183, 185, 190, 195,
        197, 202, 207, 212, 214, 219, 224, 226, 231, 236, 238, 243, 248, 255,
        260, 265, 267, 272, 277, 279, 284, 289, 296, 301, 308, 313, 318, 320,
        325, 330, 337, 342, 349, 354, 359, 366, 371, 378, 383, 390, 395, 407,
        412, 419, 424, 431, 436, 448, 460, 465, 472, 477, 484, 489, 501, 513,
        518, 525, 530, 542, 554, 566, 571, 583, 595, 607, 624, 636, 648, 665,
        677, 689, 701, 718, 730, 742, 771, 783, 824, 836, 877, 930, 1024 }
```

> **No nontrivial $S$-cycle has least period $m \in \mathcal{E}_U$** — obtained with
> no enumeration of exponent words and no orbit verification beyond the three
> one-step computations $S(1) = 1$, $S(3) = 5$, $S(5) = 1$ already used by
> foundations/L-9906.2: two exact integer comparisons per value of $m$.

Furthermore:

1. **(Containment and the new values.)** $\mathcal{E} \subseteq \mathcal{E}_U$ is a
   theorem (by L-9927.3(3)), and $\{13, 79\} \subset \mathcal{E}_U$ holds by this
   file's own certificates, so $\mathcal{E}' = \mathcal{E} \cup \{13,79\} \subseteq
   \mathcal{E}_U$ (foundations/L-9920's full $48$-value set). The difference
   $$\mathcal{E}_U \setminus \mathcal{E}' \quad\text{has exactly } 118 \text{ elements
   (smallest } 30\text{, largest } 1024\text{)},$$
   of which **$80$ exceed $207$** — the value beyond which foundations/L-9920 proved
   its own (closure-free) family can never eliminate anything. The former ceiling
   $\max \mathcal{E}' = 171$ moves to $\max \mathcal{E}_U = 1024$.
2. **(Certificates.)** For each $m \in \mathcal{E}_U$ the certificate is the pair of
   integer inequalities (a) $2^{\kappa(m)-1} \le 3^m$ and (b)
   $2^{\kappa(m)} D_U(m) > N_U(m)$. Sample: $m = 30$ ($\kappa = 48$, ratio
   $1.00628\ldots$; full integers in test A/T4), $m = 212$ ($\kappa = 337$, ratio
   $1.18220\ldots$), $m = 1024$ ($\kappa = 1624$, ratio $1.00049\ldots$). The
   **tightest margin** in the whole list is $m = 320$ ($\kappa = 508$), where (b)
   holds by a factor of only $1.0000334751\ldots$ — exact arithmetic is mandatory.
3. **(Completeness.)** $R_U$ is strictly increasing, and
   $$m_U := \min\{m : R_U(m) \ge 2\} = 1039,$$
   certified by $N_U(1038) < 2 \cdot 3^{1038} D_U(1038)$ (ratio $0.9999109\ldots$) and
   $N_U(1039) \ge 2 \cdot 3^{1039} D_U(1039)$ (ratio $1.0000177\ldots$). Hence
   $\mathrm{Wd}_U(m) \ge 1$ and $W_U(m) \ne \varnothing$ for **every** $m \ge 1039$;
   together with the exhaustive exact evaluation of $1 \le m \le 1038$ this proves
   $\mathcal{E}_U$ is exactly the set above — a statement about **all** $m$. The
   thresholds of the family move $196$ (L-9917) $/\ 208$ (L-9920) $\to 1039$.

**L-9927.5 (width envelope and window cardinality).**

1. **(Envelope; exact rational constants, nats.)** For every $m \ge 1$,
   $$\frac19 \ln\frac{3m+8}{8} \;-\; \frac{5}{1323} \;<\; \ln R_U(m) \;<\;
     \frac{1}{21} \;+\; \frac19 \ln\frac{3m+4}{7}.$$
2. **(Bits; uniform corollary.)** With the certified enclosures
   $1.4426 < \log_2 e < 1.4427$ (test B/T5): for every $m \ge 1$,
   $$\frac19\log_2\frac{3m+8}{8} - 0.00546 \;<\; \mathrm{Wd}_U(m) \;<\;
     \frac19\log_2\frac{3m+4}{7} + 0.0687,$$
   and uniformly $\;\frac19\log_2 m - 0.1627 < \mathrm{Wd}_U(m) < \frac19\log_2 m + 0.0687$.
   Hence $\mathrm{Wd}_U(m) = \frac19\log_2 m + O(1)$, i.e. $R_U(m) = \Theta(m^{1/9})$:
   **the closure sieve changes the growth *rate* of the window width, from L-9917's
   $\frac16\log_2 m$ to $\frac19\log_2 m$** — one extra admissible $K$ now costs a
   factor $2^9 = 512$ in $m$ instead of $2^6 = 64$. (L-9920, by contrast, changed
   only the additive constant, by $\approx 0.015$.)
3. **(Cardinality.)** $W_U(m)$ is the set of integers in
   $(m\alpha,\, m\alpha + \mathrm{Wd}_U(m)]$, so
   $|W_U(m)| \in \{\lfloor \mathrm{Wd}_U(m)\rfloor, \lfloor \mathrm{Wd}_U(m)\rfloor + 1\}
   \le \frac19\log_2 m + 1.0687$. Computed exactly: for $m \le 1500$ every window has
   $\le 2$ elements, and the first two-element window occurs at $m = 1171$. (No
   claim that windows are singletons on any range beyond what is computed — cf. the
   fable-02-v22 correction to L-9917.4(5).)
4. *(Remark, non-load-bearing.)* By Stirling for Pochhammer ratios,
   $R_U(m)/m^{1/9} \to 2^{-1/9}\,\Gamma(\tfrac76)\Gamma(\tfrac{11}6)\big/
   \bigl(\Gamma(\tfrac{11}9)\Gamma(\tfrac{17}9)\bigr) = 0.9242\ldots$
   (measured $0.924228$ at $m = 5999$); no rigorous claim uses this.

**L-9927.6 (per-class closure floors; the profile-level refinement).** For $t \ge 1$
let $r_t$ be the exponent-residue base point (foundations/L-9912.5; re-derived in
Step 8): $a(x) = t \iff x \equiv r_t \pmod{2^{t+1}}$. Define the **closure-sieved
class**
$$A^*_t \;:=\; \{\, x \equiv r_t \ (\mathrm{mod}\ 2^{t+1}) \;:\; x \ge 7,\ 3 \nmid x,\
   3x + 1 \ge 7 \cdot 2^t \,\}$$
(the last condition is L-9927.2(4)) with increasing enumeration $\gamma_t(0) <
\gamma_t(1) < \dots$ ($A^*_t$ is infinite). Then, for a nontrivial cycle with profile
$\pi = (m_t)$ ($m_t := \#\{i : a_i = t\}$), the $j$-th smallest class-$t$ element is
$\ge \gamma_t(j)$, hence
$$2^K \;\le\; P^*_U(\pi) \;:=\; \prod_{t\ge1}\ \prod_{j<m_t}\Bigl(3+\frac1{\gamma_t(j)}\Bigr)
\;\le\; Q^*_U(m,K) \;:=\; \max_{\pi}\, P^*_U(\pi) \;\le\; P_U(m).$$
The class floors $\beta^*_t := \gamma_t(0)$ for $t = 1..14$ are (exact; test B/T7,
brute force agreeing with the progression-based computation; L-9920's floors
$\beta_t$ for comparison):

| $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\beta_t$ (L-9920) | 7 | 9 | 13 | 37 | 53 | 21 | 213 | 85 | 853 | 341 | 3413 | 1365 | 13653 | 5461 |
| $\beta^*_t$ (this file) | 7 | **17** | **29** | 37 | **181** | **149** | **469** | **1109** | **1877** | **2389** | **11605** | **9557** | **30037** | **70997** |

(Mod $3$ bans the old floor itself at $t \in \{2, 6, 12, 13\}$ — e.g. $9$, $21$,
$1365$, $13653$ are multiples of $3$, so **no cycle contains them**; the image floor
$3x + 1 \ge 7\cdot2^t$ binds at $t \in \{3,5,8,9,10,11,14\}$.) Evaluated exactly on
every surviving window with $m \le 40$ (test B/T8): the per-class refinement
eliminates **nothing beyond $\mathcal{E}_U$ there** — its deficit
$\log_2(P_U/Q^*_U)$ is only $0.02$–$0.04$ bits, the nearest miss being $m = 25$
($2^{40}/Q^*_U = 0.996893$). The full sweep $m \le 1038$ is left open as
**Q-9927-A** with an honest cost estimate (Suggested next attack).

**L-9927.7 (the verified-floor regime is untouched: NULL).** Assume L-9913's
$(\mathrm{V}_F)$ and let $m^*(F)$ be its minimal admissible least period. Replacing
the floor $7$ by $F+1$ throughout L-9927.3 (allowed set $\{x > F$ odd, $3\nmid x\}$)
gives a valid, strictly stronger window; nevertheless, exactly (test B/T9):

- $F = 10^6$, $m = 2966$, $K = 4701$: thinned width $0.001420037$ bits $\ge$ required
  $0.001222861$ bits — $K$ remains admissible, so $m^*(10^6) = 2966$ **unchanged**;
- $F = 10^9$, $m = 47468$, $K = 75235$: thinned width $0.000022826 \ge 0.000015768$ —
  $m^*(10^9) = 47468$ **unchanged**.

With foundations/L-9920.5's numbers this completes a strictly ordered five-tier chain
at $(F, m) = (10^6, 2966)$: crude $0.001426343 >$ distinctness $0.001422130 >$
per-class $0.001421757 >$ **mod-3-thinned $0.001420037$** $>$ required $0.001222861$.
The closure sieve is the strongest of the four bounds and still $16\%$ above the
requirement: in the large-floor regime the sieve is a relative $O(m/F)$ effect and
buys nothing, exactly as L-9920.5 found for the dictionary. **The regimes are now
mapped: elementary floor — large gain; verified floor — none.**

**L-9927.8 (universal ceiling for the entire allowed-set family).** Call
$V \subseteq \mathbb{Z}^+$ a **valid allowed set** if $V$ is infinite and every
element of every nontrivial $S$-cycle belongs to $V$; write $v_0 < v_1 < \dots$ for
its enumeration, $P_V(m) := \prod_{k<m}(3 + 1/v_k)$,
$W_V(m) := \{K : 3^m < 2^K \le P_V(m)\}$, $\mathrm{Wd}_V(m) := \log_2(P_V(m)/3^m)$.
Then every nontrivial cycle of least period $m$ has $K \in W_V(m)$
("the $V$-window method"; L-9917, L-9920 restricted to sets, and this file are the
instances $V = $ odds $\ge 7$, its dictionary refinement, and $U$). Two ceilings:

1. **(Arithmetic-progression tails give finite reach.)** If $V \supseteq
   \{x^\circ + qj : j \ge 0\}$ for some $x^\circ, q \ge 1$, then $\mathrm{Wd}_V(m)
   \to \infty$; hence there is $M_V$ with $W_V(m) \ne \varnothing$ for all
   $m \ge M_V$, so $\{m : W_V(m) = \varnothing\}$ is **finite**. Every allowed set
   defined by finitely many congruence conditions that leave at least one residue
   class admissible is of this type. **No congruence sieve, of any modulus or
   surjectivity depth, escapes finiteness of its elimination list.**
2. **(No allowed set whatsoever reaches all large $m$.)** For EVERY valid allowed
   set $V$: the set $\{m : W_V(m) \ne \varnothing\}$ is **infinite**. Precisely,
   $\delta_V := \log_2(1 + 1/(3v_0)) > 0$ satisfies $\mathrm{Wd}_V(m) \ge \delta_V$
   for all $m \ge 1$, and (density lemma, proved in Step 10 from the irrationality
   of $\alpha$ by pigeonhole alone) there are infinitely many $m$ with
   $\kappa(m) - m\alpha = 1 - \{m\alpha\} < \delta_V$; for each of them
   $\kappa(m) \in W_V(m)$. **Consequently the product-window method — with any
   valid allowed set, however thin — can never prove "no nontrivial cycles for all
   $m \ge M$"**; it can only produce finite elimination lists (this family) or
   lower-bound thresholds (L-9913). Concretely (test B/T10): $m = 306$ has
   $\kappa(306) - 306\alpha < 0.00148$, certified by the exact positive integer
   $d = 2^{485} - 3^{306}$, while every $V$ with $\min V \le 225$ has
   $\mathrm{Wd}_V(306) \ge \delta_V > 0.00213$ — so $m = 306$ (and, by the density
   lemma, infinitely many $m$) survives every such sieve. Deciding all large $m$
   requires input that bounds $K - m\alpha$ away from $0$ *as a function of $m$* —
   Diophantine input in the style of foundations/L-9910 — not membership sieves.

**Open questions.**

- **Q-9927-A.** Run the per-class evaluation $Q^*_U(m,K)$ (L-9927.6) over all
  $m \le 1038$, $K \in W_U(m)$, with certified log-domain arithmetic in the style of
  L-9920's implementation A. Expected gain per window is $0.02$–$0.05$ bits against
  typical needed margins of $0.1$–$1$ bit, so at most a handful of new $m$; the DP
  at $m \approx 1000$ has $\sim 3\cdot 10^5$ states over $\sim 4000$ items.
- **Q-9927-B (profile-coupled depth-2 sieve).** Depth-2 surjectivity constrains each
  element mod $9$ *given the predecessor's exponent*: for each $t$, exactly $m_t$
  elements lie in $\{4 \cdot 2^{-t}, 7 \cdot 2^{-t}\} \bmod 9$. As a set bound this
  is a bipartite matching/transportation constraint between the multiset of element
  residues mod 9 and the profile — strictly finer than L-9927.6, not expressible as
  a plain sieve (L-9927.1(3)), and unexplored.
- **Q-9927-C (transport/chains).** The coordinator sketch's ladder intuition, made
  honest: closure transports population upward ($n$ elements of class 1 in a height
  layer force $\ge n$ elements $3/2$ higher). Formulate layer-population
  inequalities and determine whether they beat the $\Theta(\log m)$ width. This is
  the one identified route to a super-sieve gain at the set level, and it must
  confront the cyclic-vs-sorted permutation explicitly.

---

## Definitions

- $S$, $a(x)$ — D-9904; cycle data $x_i, a_i, K$, least period $m$ — D-9908; trivial
  cycle — D-9905; counterexample — D-9909. $\mathrm{odd}(\cdot)$ — D-9903.
- **$U$, $u_k$, $N_U, D_U, P_U, R_U, \mathrm{Wd}_U, W_U$** — as in the Statement.
  $\kappa(m) = \mathrm{bl}(3^m)$; $\lambda_U(m) := \max\{K : 2^K D_U(m) \le N_U(m)\}$,
  so $W_U(m) = \{\kappa(m), \dots, \lambda_U(m)\}$ (an integer interval, possibly
  empty). $\mathcal{E}_U := \{m : W_U(m) = \varnothing\}$;
  $m_U := \min\{m : R_U(m) \ge 2\}$.
- **Profile.** $\pi = (m_t)_{t \ge 1}$, $m_t = \#\{i : a_i = t\}$;
  $\sum_t m_t = m$, $\sum_t t\,m_t = K$.
- **Dictionary base points** $r_t := (2^t-1)/3$ ($t$ even), $(5 \cdot 2^t - 1)/3$
  ($t$ odd) — foundations/L-9912.5, re-derived in Step 8.
- **$A^*_t$, $\gamma_t(j)$, $\beta^*_t$, $P^*_U, Q^*_U$** — as in L-9927.6.
- **Valid allowed set $V$**, $P_V, W_V, \mathrm{Wd}_V$ — as in L-9927.8.
- $\{x\}$ denotes the fractional part; for $m \ge 1$, $m\alpha \notin \mathbb{Z}$
  (Step 10, Lemma A), so $\kappa(m) = \lfloor m\alpha \rfloor + 1$ and
  $\kappa(m) - m\alpha = 1 - \{m\alpha\} \in (0,1)$ — this is L-9913's $f(m)$.
- Empty products are $1$ (NOTATION.md). All arithmetic in proofs and scripts is
  exact (`int`, `fractions.Fraction`); floats appear only in labelled informational
  displays and the envelope re-check (test B/T6), never in a decision.

---

## Motivation

foundations/L-9920 closed the closure-free set-level program: its $Q(m,K)$ is the
best bound extractable from {product formula, positivity, floor $7$, dictionary,
distinctness}, it eliminates exactly $48$ cycle lengths, none beyond $m = 207$, and
its file records **Q-9920-A**: the next gain must come from the one fact all of
L-9905/L-9912/L-9913/L-9917/L-9920 discard — that the element set is **closed under
$S$**. This file is the direct answer.

The observation that unlocks it is embarrassingly simple. Closure means every
element has its predecessor in the cycle, i.e. every element is an $S$-image; and an
$S$-image is never divisible by $3$, because $2^{a}S(y) = 3y + 1 \equiv 1 \pmod 3$.
So a cycle's elements avoid an entire residue class mod $3$ — one third of all
candidates, concentrated exactly where the product bound is sensitive (the small
elements). The $j$-th smallest element is now forced up at rate $3j$ instead of
L-9917's $2j$, the window-width growth constant drops from $\frac16\log_2 m$ to
$\frac19\log_2 m$, and the whole elimination machinery of L-9917 replays with much
longer reach: $166$ eliminated lengths instead of $46/48$, ceiling $1024$ instead of
$171$, threshold $1039$ instead of $196/208$ — still by two integer comparisons per
$m$, with no orbit verification and no enumeration.

Two prior in-repo items make this genuinely new rather than folklore-shuffling.
First, foundations/L-9909.1 proved the leaf fact ($n \equiv 0 \bmod 3$ has no
$S$-preimage) but it was never injected into the cycle bounds: L-9917/L-9920's
allowed sets and classes contain multiples of $3$ (e.g. $15 \in A_1$, $9 = \beta_2$,
$21 = \beta_6$). Second, NEGATIVE_RESULTS.md §3.4 proved the $p = 3$ **word-level**
sieve is vacuous (the suffix map is surjective onto all units mod $3^j$) — which is
consistent with, and even explains, this file's completeness result L-9927.1(3): at
the element level, $p = 3$ contributes exactly the single congruence
"$z$ is a unit mod $3$", no more at any depth; the whole point is that this single
congruence, fed into the *product bound*, is worth a factor $\frac{2}{3}$ in the
width's growth rate. The scout's "0.000% filtering on words" and this file's "118
new eliminations on lengths" are about different objects.

The second half of the file is the honest ceiling. The closure sieve is still a
membership sieve, and the family needed its Q-9920-A-style door closed properly:
L-9927.8 proves that *no* allowed-set sieve — congruence-defined or not, of any
thinness — can eliminate all large $m$, because the width is bounded below by a
positive constant while $\kappa(m) - m\alpha$ dips below every positive constant
infinitely often (pigeonhole density of $\{m\alpha\}$). So this family can only ever
produce finite lists or floor-driven thresholds; the routes that remain are the
profile-coupled/transport constraints (Q-9927-B/C) and Diophantine input (L-9910).
For the counterexample program of issue #9 the practical output is: $118$ more
cycle lengths need never be searched, and the live search targets remain
$m \in \{22, 25, 27, 29, 32, 34, 37, 39, \dots\} \setminus \mathcal{E}_U$
(unconditionally) resp. $m \ge 2966$ (given $(\mathrm{V}_{10^6})$).

---

## Proof or construction

### Step 0 — standing setup

Fix an $S$-cycle $x_1 \to \dots \to x_m \to x_1$ of least period $m \ge 1$, cyclic
indices $x_{i+m} = x_i$, $a_{i+m} = a_i$. The defining relation is
$$2^{a_i}\,x_{i+1} \;=\; 3x_i + 1 \qquad (i \in \mathbb{Z}). \tag{$\ast_i$}$$
Steps 1–2 and 4–9 concern cycles on the positive odd integers; Step 3 is
sign-agnostic and uses only $(\ast_i)$.

### Step 1 — product formula and positivity, re-derived inline

Divide $(\ast_i)$ by $x_i \ne 0$ and multiply over $i = 1, \dots, m$; the left side
telescopes ($\prod x_{i+1}/x_i = x_{m+1}/x_1 = 1$):
$$2^K \;=\; \prod_{i=1}^m\Bigl(3 + \frac{1}{x_i}\Bigr). \tag{PF}$$
If every $x_i > 0$ then every factor exceeds $3$, so
$$2^K \;>\; 3^m. \tag{POS}$$
(These are foundations/L-9905.3 and L-9905.2; (POS) is the only place positivity
enters the window machinery, and it is exactly what fails on the negative cycles —
test A/T3.) $\square$

### Step 2 — distinctness and the elementary floor, re-derived

**(2a) Distinctness.** The elements $x_1, \dots, x_m$ of a least-period-$m$ cycle
are pairwise distinct. *(This is foundations/L-9917.1(1), PROVED; two-line sketch:
$x_i = x_j$ with $p := j - i \in [1, m-1]$ makes $p$ a period of the bi-infinite
sequence $(x_i)$; the periods form a subgroup of $\mathbb{Z}$ generated by the least
period $m$, so $m \mid p$ — contradiction.)*

**(2b) Floor.** Every element of a nontrivial cycle is $\ge 7$. *(This is
foundations/L-9906.2; argument restated: $S(1) = 1$, $S(3) = 5$, $S(5) = 1$ — three
one-step computations — so $1$ lies only on the trivial cycle and $3, 5$ reach $1$
and lie on no cycle; a cycle set is $S$-invariant, so
$\mathcal{C} \cap \{1,3,5\} = \varnothing$, and every positive odd integer outside
$\{1,3,5\}$ is $\ge 7$.)* $\square$

### Step 3 — proof of L-9927.1 (the surjectivity sieve; sign-agnostic)

**(3a) Every element is an image.** By D-9908 the cycle relation gives
$x_{i} = S(x_{i-1})$ for every $i$ under the cyclic convention — in particular
$x_1 = S(x_m)$. So $S(\mathcal{C}) = \mathcal{C}$, and $S|_{\mathcal C}$, being a
surjective self-map of a finite set, is a bijection. $\square$

**(3b) Images avoid multiples of 3.** Let $y$ be any nonzero odd integer and
$a = a(y)$. From $2^{a} S(y) = 3y + 1 \equiv 1 \pmod 3$: if $3 \mid S(y)$ then
$3 \mid 2^a S(y)$, contradicting $2^aS(y) \equiv 1 \pmod 3$. So $3 \nmid S(y)$.
With (3a): no element of any $S$-cycle (either sign; trivial included) is divisible
by $3$. $\square$

**(3c) Exact image set.** Let $z \ge 1$ be odd with $3 \nmid z$.

- If $z \equiv 2 \pmod 3$: $2z - 1 \equiv 4 - 1 = 3 \equiv 0 \pmod 3$, so
  $y := (2z-1)/3 \in \mathbb{Z}$, and $y \ge 1$ ($z \ge 2$... precisely $z \ge 5$
  gives $y \ge 3$; $z = 2$ is even, excluded; the smallest case is $z = 5, y = 3$;
  for $z \equiv 2 \bmod 3$ odd, $z \ge 5$). $3y = 2z - 1$ is odd, so $y$ is odd.
  And $3y + 1 = 2z$ with $z$ odd, so $a(y) = \nu_2(2z) = 1$ and $S(y) = z$.
- If $z \equiv 1 \pmod 3$: $4z - 1 \equiv 4 - 1 \equiv 0 \pmod 3$, so
  $y := (4z-1)/3 \in \mathbb{Z}$, $y \ge 1$ (already $z = 1$ gives $y = 1$), odd
  (as $3y = 4z-1$ is odd), and $3y + 1 = 4z$ with $z$ odd gives $a(y) = 2$,
  $S(y) = z$.

With (3b) this proves $\mathrm{image}(S) = \{\text{odd } z \ge 1 : 3\nmid z\}$.

**(3d) Depth stability.** Fix odd $z \ge 1$ with $3 \nmid z$ and let $t_0 \in
\{1,2\}$ be as in (3c). For $i \ge 0$ put $y_i := (2^{t_0 + 2i} z - 1)/3$. Each
$y_i$ is an integer (induction: $y_{i+1} = (4 \cdot 2^{t_0+2i}z - 4 + 3)/3 =
4y_i + 1$), odd, positive, with $a(y_i) = t_0 + 2i$ and $S(y_i) = z$ (same
computation as (3c): $3y_i + 1 = 2^{t_0+2i}z$, $z$ odd). The recursion
$y_{i+1} = 4y_i + 1$ reduces mod $3$ to $y_{i+1} \equiv y_i + 1$: the preimage
residues cycle through all classes mod $3$ with period $3$ in $i$ (this is
foundations/L-9909.1(3), re-derived). In particular every such $z$ has infinitely
many preimages $y$ with $3 \nmid y$. By induction on $k$: every $z$ with
$3 \nmid z$ lies in $\mathrm{image}(S^k)$ for every $k \ge 1$ (choose a preimage
avoiding multiples of $3$ and recurse), while by (3b) no multiple of $3$ does.
Hence $\mathrm{image}(S^k) = \{\text{odd } z \ge 1 : 3 \nmid z\}$ for all $k \ge 1$:
the plain-congruence content of surjectivity is exhausted at depth $1$.
(Exhaustively machine-checked in test A/T2.) $\blacksquare$

### Step 4 — proof of L-9927.2 (extremal and local facts)

Throughout this step the cycle is nontrivial on the positive odds, so (2b) gives
$x_{\min} \ge 7$, and by (3a) $S(y) \in \mathcal{C}$ for every $y \in \mathcal{C}$,
hence $S(y) \ge x_{\min}$.

**(4a) Minimum.** Apply $S(x_{\min}) \ge x_{\min}$ with $a := a(x_{\min})$:
$(3x_{\min}+1)/2^a \ge x_{\min}$, and multiplying by $2^a > 0$,
$3x_{\min} + 1 \ge 2^a x_{\min}$, i.e. (dividing by $x_{\min} > 0$)
$$2^a \;\le\; 3 + \frac{1}{x_{\min}} \;\le\; 3 + \frac17 \;=\; \frac{22}{7} \;<\; 4 ,$$
so $a \le 1$, i.e. $a = 1$ and $S(x_{\min}) = (3x_{\min}+1)/2 > x_{\min}$ (strict
since $(3x+1)/2 > x \iff x > -1$). The dictionary case $t = 1$ (re-derivation:
$a(x) = 1 \iff \nu_2(3x+1) = 1 \iff 3x + 1 \equiv 2 \pmod 4 \iff x \equiv 3
\pmod 4$, using $3^{-1} \equiv 3 \pmod 4$) gives $x_{\min} \equiv 3 \pmod 4$; with
$3 \nmid x_{\min}$ (Step 3) and CRT mod 12: $x_{\min} \in \{7, 11\} \bmod 12$.
*(Positivity and the floor are both used: the trivial cycle has $x_{\min} = 1$,
where $2^a \le 4$ permits $a = 2$ — and indeed $a(1) = 2$; the negative cycles
violate the conclusion outright, test A/T3.)* $\square$

**(4b) Maximum.** $S(x_{\max}) \le x_{\max}$ gives $3x_{\max} + 1 \le
2^{a}x_{\max}$, so $2^{a} \ge 3 + 1/x_{\max} > 3$, forcing $a \ge 2$. The
complementary dictionary case ($a(x) \ge 2 \iff 4 \mid 3x+1 \iff x \equiv 1
\pmod 4$) and $3 \nmid x_{\max}$ give $x_{\max} \in \{1, 5\} \bmod 12$. $\square$

**(4c) Slab.** Let $y \in \mathcal{C}$ with $y < (4x_{\min}-1)/3$, i.e.
$3y + 1 < 4x_{\min}$. If $a(y) \ge 2$ then
$S(y) = (3y+1)/2^{a(y)} \le (3y+1)/4 < x_{\min}$, contradicting
$S(y) \ge x_{\min}$. So $a(y) = 1$. $\square$

**(4d) Per-class image floors.** Let $y \in \mathcal{C}$, $t := a(y)$. Then
$S(y) = (3y+1)/2^t \in \mathcal{C}$, so $S(y) \ge x_{\min} \ge 7$, i.e.
$3y + 1 \ge 2^t x_{\min} \ge 7 \cdot 2^t$ and
$y \ge (2^t x_{\min} - 1)/3 \ge (7 \cdot 2^t - 1)/3$. For $t = 1$ this is
$(2x_{\min}-1)/3 < x_{\min}$ — vacuous; for $t \ge 2$ it exceeds $x_{\min}$
whenever $2^t > 3 + 1/x_{\min}$, i.e. always. $\blacksquare$

### Step 5 — proof of L-9927.3 (the closure-sieved sorted bound)

**(5a) The enumeration of $U$.** An integer is odd and not divisible by $3$ iff it
is $\equiv 1$ or $5 \pmod 6$. The members of $U$ in the class $1 \bmod 6$ are
$6j + 7$ ($j \ge 0$) and in the class $5 \bmod 6$ are $6j + 11$ ($j \ge 0$); since
$6j + 7 < 6j + 11 < 6(j+1) + 7$, the increasing enumeration of $U$ alternates
between the two progressions:
$$u_{2j} = 6j + 7, \qquad u_{2j+1} = 6j + 11 \qquad (j \ge 0),$$
which is the closed form $u_k = 3k + 7 + (k \bmod 2)$ (substitute $k = 2j$ and
$k = 2j+1$). Exhaustively checked to $10^5$ in test A/T1. $\square$

**(5b) Sorted floors.** By (2a), (2b) and Step 3, the $m$ elements of a nontrivial
cycle form an $m$-element subset $X \subseteq U$. For the increasing enumeration
$x_{(0)} < \dots < x_{(m-1)}$ of $X$ and any $k$: the $k+1$ elements
$x_{(0)}, \dots, x_{(k)}$ all lie in $U \cap [1, x_{(k)}]$, so $U$ has at least
$k+1$ elements $\le x_{(k)}$, whence $u_k \le x_{(k)}$ (as $u_k$ is the
$(k{+}1)$-st smallest element of $U$). $\square$

**(5c) The bound.** The function $f(v) = 3 + 1/v$ is strictly decreasing and
positive on $(0, \infty)$. Reindexing the product (PF) by the increasing
enumeration (a bijective relabelling; multiplication is commutative) and using
(5b) termwise, with the elementary monotonicity of finite products of positive
reals in each factor:
$$2^K \;=\; \prod_{k=0}^{m-1}\Bigl(3 + \frac{1}{x_{(k)}}\Bigr)
\;\le\; \prod_{k=0}^{m-1}\Bigl(3 + \frac{1}{u_k}\Bigr) \;=\; P_U(m).$$
With (POS): $K \in W_U(m)$. Clearing denominators
($3 + 1/u_k = (3u_k+1)/u_k$) gives the integer form
$2^K \le P_U(m) \iff 2^K D_U(m) \le N_U(m)$. $\square$

**(5d) Domination over L-9917.** For every $k \ge 0$: $u_k = 3k + 7 + (k \bmod 2)
\ge 2k + 7$, with equality iff $k = 0$. Hence termwise
$3 + 1/u_k \le 3 + 1/(7+2k)$, strictly for $k \ge 1$, so
$P_U(m) \le P(m)$ with strict inequality for $m \ge 2$, and
$W_U(m) \subseteq W^*(m)$. In particular $W^*(m) = \varnothing \Rightarrow W_U(m) =
\varnothing$: **L-9917's 46-element $\mathcal{E}$ is contained in $\mathcal{E}_U$ by
proof**, independently of any computation. $\blacksquare$

### Step 6 — proof of L-9927.4 (the elimination set and its completeness)

**(6a) Window structure and certificates.** $K \mapsto 2^K$ and
$K \mapsto 2^K D_U(m)$ are strictly increasing, so
$W_U(m) = \{\kappa(m), \dots, \lambda_U(m)\}$ and
$$W_U(m) = \varnothing \iff 2^{\kappa(m)} D_U(m) > N_U(m).$$
Thus two exact integer comparisons decide each $m$: (a) $2^{\kappa(m)-1} \le 3^m$
(with $3^m < 2^{\kappa(m)}$ from the bit length, this certifies $\kappa$), and (b)
$2^{\kappa(m)} D_U(m) > N_U(m)$. If a nontrivial cycle of least period $m$ existed,
Step 5 would put its $K$ in $W_U(m)$; contrapositive: $W_U(m) = \varnothing$
eliminates $m$. $\square$

**(6b) The sweep.** For every $1 \le m \le 1500$ the comparisons were evaluated
exactly by two independent implementations (cleared integers; `Fraction`s), which
agree everywhere (test A/T4). This produces the $166$-element list of the
Statement for $m \le 1038$, reproduces foundations/L-9917's $\mathcal{E}$ ($46$
values) and threshold $196$ exactly as a machinery cross-check, verifies
$W_U(m) \subseteq W^*(m)$ at every $m$, and verifies $13, 79 \in \mathcal{E}_U$
directly (so $\mathcal{E}' \subseteq \mathcal{E}_U$, the $46$ by (5d) and the two
by certificate). $\square$

**(6c) Completeness over all $m$.** Each factor of $R_U$ satisfies
$1 + 1/(3u_k) > 1$, so $R_U$ is strictly increasing. The two boundary certificates
(test A/T4)
$$N_U(1038) < 2 \cdot 3^{1038}\,D_U(1038), \qquad N_U(1039) \ge 2 \cdot 3^{1039}\,D_U(1039)$$
give $m_U = 1039$ exactly, and $R_U(m) \ge R_U(1039) \ge 2$ for every $m \ge 1039$.
For such $m$, $\mathrm{Wd}_U(m) \ge 1$, and a half-open real interval
$(m\alpha, m\alpha + L]$ with $L \ge 1$ contains the integer
$\lfloor m\alpha\rfloor + 1$; hence $W_U(m) \ne \varnothing$ and
$m \notin \mathcal{E}_U$. With (6b)'s exhaustive evaluation of $m \le 1038$,
$\mathcal{E}_U$ is exactly the stated set, over **all** $m \ge 1$. $\square$

**(6d) Bookkeeping of novelty.** $|\mathcal{E}_U| = 166$;
$\mathcal{E}_U \cap [1, 21]$ ($16$ values) re-derives cases settled by
foundations/L-9906/L-9915 enumeration; $\mathcal{E}_U \setminus \mathcal{E}'$ has
$118$ elements, all $\ge 22$, none previously eliminated by any in-repo
unconditional result; $80$ of them exceed $207$. Under $(\mathrm{V}_{10^6})$,
foundations/L-9913 eliminates every $m \le 2965$ conditionally, which covers all of
$\mathcal{E}_U$; the value of $\mathcal{E}_U$ is that it is unconditional (no orbit
verification) — the same relationship L-9917/L-9920 already have to L-9913, stated
there in the same terms. The smallest least period not excluded unconditionally
remains $m = 22$. $\blacksquare$

### Step 7 — proof of L-9927.5 (envelope and cardinality)

**(7a) Term bounds.** $\ln R_U(m) = \sum_{k<m}\ln(1 + s_k)$ with
$s_k := 1/(3u_k)$. From (5a), $3k + 7 \le u_k \le 3k + 8$, so
$$\frac{1}{9k+24} \;\le\; s_k \;\le\; \frac{1}{9k+21} \;\le\; \frac{1}{21}.$$
The elementary inequalities $u - u^2/2 < \ln(1+u) < u$ for $u > 0$ hold because
$u - \ln(1+u)$ and $\ln(1+u) - u + u^2/2$ vanish at $0$ and have derivatives
$u/(1+u) > 0$ and $u^2/(1+u) > 0$.

**(7b) Upper bound.** Since $t \mapsto 1/(9t+21)$ is decreasing,
$1/(9k+21) \le \int_{k-1}^{k} \frac{dt}{9t+21}$ for $k \ge 1$, so
$$\ln R_U(m) < \sum_{k<m} \frac{1}{9k+21}
\le \frac{1}{21} + \int_0^{m-1}\frac{dt}{9t+21}
= \frac{1}{21} + \frac19\ln\frac{9m+12}{21}
= \frac{1}{21} + \frac19\ln\frac{3m+4}{7}.$$

**(7c) Lower bound.** $1/(9k+24) \ge \int_k^{k+1}\frac{dt}{9t+24}$, so
$\sum_{k<m} s_k \ge \frac19\ln\frac{9m+24}{24} = \frac19\ln\frac{3m+8}{8}$; and
$$\frac12\sum_{k<m}s_k^2 \le \frac12\sum_{k\ge0}\frac{1}{(9k+21)^2}
\le \frac12\Bigl(\frac{1}{441} + \int_0^\infty\frac{dt}{(9t+21)^2}\Bigr)
= \frac12\Bigl(\frac{1}{441} + \frac{1}{189}\Bigr) = \frac{5}{1323}.$$
Hence $\ln R_U(m) > \frac19\ln\frac{3m+8}{8} - \frac{5}{1323}$. Together with (7b)
this is L-9927.5(1); numerically re-checked for $m \le 2000$ with positive slack
everywhere (test B/T6).

**(7d) Bits and uniform corollary.** Dividing by $\ln 2$ and using the certified
$\log_2 e < 1.4427$ (test B/T5): $\frac{1}{21\ln 2} < \frac{1.4427}{21} = 0.0687$
and $\frac{5}{1323\ln 2} < \frac{5 \cdot 1.4427}{1323} < 0.00546$, giving
L-9927.5(2)'s first display. For the uniform form: $(3m+4)/7 \le m \iff 4 \le 4m$,
true for $m \ge 1$; and $(3m+8)/8 \ge 3m/8$ with
$\frac19\log_2\frac38 = -\frac19(3 - \log_2 3) > -\frac{1.4151}{9} > -0.15724$
(certified $\log_2 3 > 1.5849$), so the lower constant is
$-0.15724 - 0.00546 > -0.1627$. $\square$

**(7e) Cardinality.** $3^m < 2^K \le P_U(m)$ is equivalent (strictly increasing
$\log_2$) to $K \in (m\alpha, m\alpha + \mathrm{Wd}_U(m)]$; the number of integers
in $(\beta - L, \beta]$ is $\lfloor\beta\rfloor - \lfloor\beta - L\rfloor \in
\{\lfloor L\rfloor, \lfloor L\rfloor + 1\}$. The two-element onset $m = 1171$ and
the absence of $\ge 3$-element windows for $m \le 1500$ are exact computations
(test B/T11); nothing beyond the computed range is claimed. $\blacksquare$

### Step 8 — proof of L-9927.6 (per-class refinement)

**(8a) Dictionary, re-derived.** For $t \ge 1$ and odd $x$:
$a(x) = t \iff 3x + 1 \equiv 2^t \pmod{2^{t+1}} \iff 3x \equiv 2^t - 1
\pmod{2^{t+1}}$, which has the unique solution $x \equiv r_t \pmod{2^{t+1}}$ since
$\gcd(3, 2^{t+1}) = 1$; and $r_t$ as defined solves it: for even $t$,
$3r_t = 2^t - 1$; for odd $t$, $3r_t + 1 = 5 \cdot 2^t \equiv 2^t \pmod{2^{t+1}}$
(this is foundations/L-9912.5 / L-9920 Step 2, re-derived).

**(8b) Class membership and spacing.** Let the cycle be nontrivial with profile
$\pi$. Fix $t$ with $m_t \ge 1$. The class-$t$ elements are pairwise distinct
(2a), lie in the single class $r_t \bmod 2^{t+1}$ (8a), are $\ge 7$ (2b), satisfy
$3 \nmid x$ (Step 3), and satisfy $3x + 1 \ge 7 \cdot 2^t$ (4d). Hence they are
$m_t$ distinct members of $A^*_t$, and by the counting argument of (5b) applied to
$A^*_t$, the $j$-th smallest is $\ge \gamma_t(j)$. ($A^*_t$ is infinite: the class
$r_t \bmod 2^{t+1}$ meets every residue mod $3$ — as $2^{t+1}$ is invertible mod
$3$ — so two of every three consecutive class members avoid multiples of $3$, and
all but finitely many clear the other two floors.)

**(8c) The bound and its evaluation.** Splitting (PF) over the classes and
bounding each block termwise exactly as in (5c) gives $2^K \le P^*_U(\pi) \le
Q^*_U(m,K)$; finiteness of the profile set at fixed $(m, K)$ is L-9920.3(3)'s
argument (excess $E = K - m$ caps support and multiplicities), so the maximum
exists. Domination $Q^*_U(m,K) \le P_U(m)$: the union of the per-class prefixes is
an $m$-element subset of $U$ (classes are disjoint, all members lie in $U$), so its
sorted product is $\le P_U(m)$ by (5b)+(5c)'s argument. The floors table is exact
(test B/T7, two independent methods); the exact evaluation of $Q^*_U$ on every
surviving window with $m \le 40$ (test B/T8, exact `Fraction` knapsack over
class-prefix products — within a class only the prefix can be optimal, since the
class sequence increases and $f$ decreases) eliminates nothing beyond
$\mathcal{E}_U$ and measures the deficit $\log_2(P_U/Q^*_U)$ at $0.02$–$0.041$
bits on that range. No claim is made about $m > 40$ (Q-9927-A). $\blacksquare$

### Step 9 — proof of L-9927.7 (large-floor NULL)

Assume $(\mathrm{V}_F)$; by L-9913.1 every element of a nontrivial cycle exceeds
$F$. Replacing $U$ by $U_F := \{x > F$ odd, $3 \nmid x\}$, Steps 5b–5c apply
verbatim (distinctness, floor, mod-3 are all still true) and give
$2^K \le P_{U_F}(m) := \prod_{k<m}(3 + 1/v_k)$ with $v_k$ the enumeration of
$U_F$. Since $U_F \subseteq \{x > F$ odd$\}$, this is stronger than L-9913's crude
constraint, so every $m$ excluded by L-9913 stays excluded, and
$m^*_{\text{thinned}}(F) \ge m^*(F)$. To show equality it suffices to check that
$K = \kappa(m^*(F))$ still satisfies the thinned constraint at $m = m^*(F)$. This
is done exactly in test B/T9:
$$2^{4701} D \le N \ \text{at}\ (F, m) = (10^6, 2966), \qquad
  2^{75235} D \le N \ \text{at}\ (F, m) = (10^9, 47468),$$
where $N, D$ are the cleared products over $U_F$'s first $m$ elements. Hence
$m^*(10^6) = 2966$ and $m^*(10^9) = 47468$ are unchanged. The structural reason
(as in L-9920.5, and quantified by the measured widths in the Statement): for
$m \ll F$ all elements are $F(1 + O(m/F))$, so passing from spacing $2$ to
average spacing $3$ perturbs $\sum 1/x$ — and hence the width — by a relative
$O(m/F)$, which is $\sim 10^{-3}$ at $F = 10^6$ against a required change of
$\sim 10^{-1}$. $\blacksquare$

### Step 10 — proof of L-9927.8 (the universal ceilings)

**(10a) The generic sieve bound.** Let $V$ be a valid allowed set. A nontrivial
cycle's elements are $m$ distinct members of $V$ (distinctness by (2a); membership
by validity), so the argument of (5b)–(5c), with $U$ replaced by $V$, gives
$2^K \le P_V(m)$; with (POS), $K \in W_V(m)$. $\square$

**Lemma A (irrationality).** $\alpha = \log_2 3 \notin \mathbb{Q}$: if
$\alpha = p/q$ with $p, q \ge 1$ then $2^p = 3^q$, impossible (left side even,
right side odd, both $> 1$). In particular $m\alpha \notin \mathbb{Z}$ for
$m \ge 1$ (else $\alpha = n/m$), so $\kappa(m) = \lfloor m\alpha\rfloor + 1$ and
$\kappa(m) - m\alpha = 1 - \{m\alpha\} \in (0,1)$. $\square$

**Lemma B (one hit).** For every $\varepsilon \in (0, 1)$ there exists $m \ge 1$
with $\{m\alpha\} > 1 - \varepsilon$.
*Proof.* Let $n := \lceil 1/\varepsilon\rceil$ and partition $[0,1)$ into the $n$
intervals $[i/n, (i+1)/n)$. The $n+1$ numbers $\{j\alpha\}$, $j = 1, \dots, n+1$,
are pairwise distinct (Lemma A: $\{j\alpha\} = \{j'\alpha\}$ forces
$(j - j')\alpha \in \mathbb{Z}$), so two of them, say with $j_1 < j_2$, lie in one
interval. Put $h := j_2 - j_1 \in [1, n]$ and
$\theta := \{j_2\alpha\} - \{j_1\alpha\} \in (-1/n, 1/n) \setminus \{0\}$; note
$\{h\alpha\} = \theta$ if $\theta > 0$ and $\{h\alpha\} = 1 + \theta$ if
$\theta < 0$ (as $h\alpha \equiv j_2\alpha - j_1\alpha \pmod 1$).
*Case $\theta < 0$:* $\{h\alpha\} = 1 + \theta > 1 - 1/n \ge 1 - \varepsilon$, so
$m = h$ works. *Case $\theta > 0$:* for every $j \ge 1$,
$jh\alpha = j\lfloor h\alpha\rfloor + j\theta$ gives $\{jh\alpha\} = \{j\theta\}$.
Take $j^* := \lfloor 1/\theta\rfloor \ge 1$; then $j^*\theta \le 1$ with equality
impossible ($\theta = \{h\alpha\}$ is irrational by Lemma A), and
$j^*\theta > 1 - \theta > 1 - \varepsilon$; since $j^*\theta < 1$,
$\{j^*h\alpha\} = j^*\theta \in (1 - \varepsilon, 1)$, so $m = j^*h$ works.
$\square$

**Lemma C (infinitely many hits).** For every $\varepsilon \in (0,1)$ the set
$D_\varepsilon := \{m \ge 1 : \{m\alpha\} > 1 - \varepsilon\}$ is infinite.
*Proof.* $D_\varepsilon \ne \varnothing$ by Lemma B. If $D_\varepsilon$ were
finite, let $s := \max_{m \in D_\varepsilon}\{m\alpha\} < 1$ (a maximum of finitely
many values, each $< 1$), and note $s > 1 - \varepsilon$. Applying Lemma B with
$\varepsilon' := 1 - s \in (0, \varepsilon)$ produces $m'$ with
$\{m'\alpha\} > 1 - \varepsilon' = s > 1 - \varepsilon$; then
$m' \in D_\varepsilon$ with $\{m'\alpha\} > s$, contradicting maximality.
$\square$

**(10b) Proof of L-9927.8(1).** Suppose $\{x^\circ + qj : j \ge 0\} \subseteq V$.
For every $k$, the $k+1$ elements $x^\circ, x^\circ + q, \dots, x^\circ + qk$ of
$V$ are all $\le x^\circ + qk$, so $v_k \le x^\circ + qk$. Using
$\ln(1+u) \ge u/(1+u)$ (equivalent to $e^{u/(1+u)} \le 1 + u$, which follows from
$e^w \le 1/(1-w)$ for $w < 1$ at $w = u/(1+u)$ — or directly: $g(u) :=
\ln(1+u) - u/(1+u)$ has $g(0) = 0$, $g'(u) = u/(1+u)^2 > 0$):
$$\ln\frac{P_V(m)}{3^m} \;=\; \sum_{k<m}\ln\Bigl(1 + \frac{1}{3v_k}\Bigr)
\;\ge\; \sum_{k<m}\frac{1}{3v_k + 1}
\;\ge\; \sum_{k<m}\frac{1}{3x^\circ + 3qk + 1} \;\longrightarrow\; \infty$$
as $m \to \infty$ (integral comparison:
$\sum_{k<m} \frac{1}{a + bk} \ge \frac1b\ln\frac{a+bm}{a}$ with
$a = 3x^\circ + 1$, $b = 3q$). So $\mathrm{Wd}_V(m) \to \infty$; since
$\mathrm{Wd}_V$ is nondecreasing (each factor $> 1$), there is $M_V$ with
$\mathrm{Wd}_V(m) \ge 1$ for all $m \ge M_V$, and then (as in (6c))
$W_V(m) \ni \lfloor m\alpha\rfloor + 1$. A congruence-defined allowed set — all
$x$ in a nonempty set of residue classes mod some $M$, above some floor — contains
the full progression tail of any of its admissible classes, so it is of this type.
$\square$

**(10c) Proof of L-9927.8(2).** $\mathrm{Wd}_V(m) \ge \mathrm{Wd}_V(1) =
\log_2(1 + 1/(3v_0)) =: \delta_V > 0$ for every $m \ge 1$ (the width is a sum of
$m \ge 1$ positive terms of which the first is $\delta_V$... precisely: the terms
are positive and the $k = 0$ term equals $\delta_V$). By Lemma C with
$\varepsilon = \delta_V$ (or $\min(\delta_V, \tfrac12)$ if $\delta_V \ge 1$),
infinitely many $m$ satisfy $\kappa(m) - m\alpha = 1 - \{m\alpha\} < \delta_V \le
\mathrm{Wd}_V(m)$; for each, $2^{\kappa(m)} \le 3^m \cdot 2^{\,\kappa(m) - m\alpha}
\le 3^m R_V(m) = P_V(m)$ — the middle step because $2^{\kappa - m\alpha} \le
R_V(m) \iff \kappa - m\alpha \le \mathrm{Wd}_V(m)$ — and $3^m < 2^{\kappa(m)}$ by
definition, so $\kappa(m) \in W_V(m) \ne \varnothing$. The concrete instance
$m = 306$ is certified in test B/T10: $d := 2^{485} - 3^{306} > 0$ and
$\kappa(306) - 306\alpha = \log_2(1 + d/3^{306}) \le (\log_2 e)\,d/3^{306} <
0.00148$ (using $\ln(1+u) \le u$ and the certified $\log_2 e < 1.4427$), while any
$V$ with $v_0 \le 225$ has $\delta_V \ge \log_2(1 + 1/675) \ge
(\log_2 e)\cdot\frac{1/675}{1 + 1/675} > 0.00213$. $\blacksquare$

*Scope remark.* L-9927.8 constrains the **window method**: elimination of $m$ solely
by "no integer $K$ with $3^m < 2^K \le P_V(m)$". It does not constrain hybrid
methods that use additional structure per $(m, K)$ — e.g. the divisibility
$(2^K - 3^m) \mid c$ with enumeration (foundations/L-9906/L-9915), profile-coupled
constraints (Q-9927-B), transport (Q-9927-C), or Diophantine lower bounds on
$K\ln 2 - m\ln 3$. That is exactly where it redirects effort.

---

## Coordinator sketch corrections

Per packet protocol, discrepancies between the assigning sketch and the proved
mathematics are flagged prominently:

- **(C1) The sketch's central mechanism is not the one that works, and its central
  claim is unproven.** The sketch proposed
  "$x_{(j)} \ge c\,(3/2)^{f(j)}\,x_{\min}$ for some explicit staircase $f$" from
  interleaved up/down moves. As the sketch itself warned, this conflates cyclic
  order with sorted order; the obstruction is real, no such staircase is proved
  here, and none is needed. What S-closure provably yields at the set level — and
  the sketch does not mention — is the **surjectivity sieve** ($3 \nmid x_i$),
  which is the quantitatively dominant consequence: it changes the width's growth
  constant ($\tfrac16 \to \tfrac19$) and delivers all 118 new eliminations. The
  ladder intuition survives only in the weaker proved forms L-9927.2(3)–(4)
  (slab + per-class image floors), whose set-level worth is measured at
  $0.02$–$0.04$ bits (test B/T8).
- **(C2) "The exponent-1 run length starting at $x_{\min}$ is constrained by
  L-9912's statistics" is misleading.** The global one-fraction
  ($m_1 > m/3$, foundations/L-9912.3) does not bound the run at $x_{\min}$ from
  below; a run of length $1$ at $x_{\min}$ is consistent with every in-repo
  constraint (the second element $(3x_{\min}+1)/2$ may have exponent $\ge 2$, its
  image $(9x_{\min}+5)/8 \ge x_{\min}$ always). The correct positional statement is
  the slab lemma L-9927.2(3), which bounds by **value** ($y < (4x_{\min}-1)/3
  \Rightarrow a(y) = 1$), not by orbit position.
- **(C3) The proposed calibration ("synthetic near-cycles of random large odd
  $n$") measures nothing relevant here.** All elements of such a segment are
  $\approx n$, so its product is $3^m(1 + O(m/n))$ — the free-vs-true comparison
  degenerates. The informative calibration is model-vs-model width (done exactly:
  the $\mathcal{E}_U$ sweep, T8's deficits, T9's five-tier chain).
- **(C4) The sketch's dichotomy "bounded gain $\Rightarrow$ outcome (c); growing
  gain $\Rightarrow$ (a)/(b)" was too coarse.** Both hold at once: the sieve's gain
  grows with $m$ (outcomes (a) and (b): 118 new $m$, rate change), yet the family
  has a proved ceiling (outcome (c): L-9927.4(3) and both parts of L-9927.8).
- **(C5) Confirmed items.** $a(x_{\min}) = 1$ exactly, with the sketch's argument
  ($2^a \le 3 + 1/x_{\min} < 4$) — completed with the precise hypothesis
  bookkeeping (positivity + nontriviality/floor; the trivial cycle has $a = 2$;
  negative-cycle minima have $a \in \{1, 2, 4\}$ — test A/T3). Likewise "elements
  with $a \ge 2$ map down by at least a factor $\approx 3/4$" (used in (4b), (4c)).

---

## What this adds beyond L-9917 / L-9920 (exact delta)

1. **First use of S-closure in the bound family** — the answer to Q-9920-A. Both
   prior files maximize over element *sets*; every constraint they use is closed
   under adding multiples of 3, which closure forbids.
2. **Eliminations.** $\mathcal{E}$ ($46$, max $171$) $\subset \mathcal{E}'$ ($48$,
   max $171$) $\subset \mathcal{E}_U$ ($166$, max $1024$): $+118$ values, $80$ of
   them beyond $207$ — the exact point where L-9920 proved its own family stops
   forever. Zero enumeration, zero orbit verification, two integer comparisons per
   $m$.
3. **Rate, not constant.** L-9920 lowered L-9917's width by $\approx 0.015$ bits
   (additive). The closure sieve lowers the *growth rate*: $\tfrac16\log_2 m \to
   \tfrac19\log_2 m$ (proved envelope) — the first structural change of the
   family's asymptotics.
4. **Thresholds.** "Empty windows terminate" moves $196$ (L-9917) / $208$ (L-9920)
   $\to 1039$, with exact boundary certificates.
5. **A lemma kit for the next route** (L-9927.1–.2): surjectivity/bijectivity of
   $S$ on $\mathcal{C}$, exact image characterization with depth stability,
   $a(x_{\min}) = 1$, $x_{\min} \bmod 12$, $a(x_{\max}) \ge 2$, the forced-slab and
   per-class image floors — the proved seeds for Q-9927-B/C.
6. **Two ceiling theorems** (L-9927.8) that close the *extended* family: every
   congruence sieve has finite reach, and *no* allowed-set sieve — of any thinness,
   including any future closure-derived congruence refinement — can eliminate all
   large $m$. Q-9920-A's set-level door is now closed with a proof, in both
   directions: this file extracts the remaining finite juice, and proves the juice
   is finite.
7. **Regime map completed** (L-9927.7): in the verified-floor regime the sieve is
   NULL — L-9913's $2966$ / $47468$ stand exactly; strengthenings of this family
   matter only in the elementary-floor regime.

---

## Dependency audit

| Used where | Statement used | Source | Status | Re-derived inline? |
|---|---|---|---|---|
| Step 0 | $S$, $a(x) \ge 1$, $(\ast_i)$ | NOTATION D-9904 | definition | n/a |
| Step 0, 2a | cycle notation, least period, $K$ | NOTATION D-9908 | definition | n/a |
| Step 2b, 4a | trivial cycle $(1)$ | NOTATION D-9905 | definition | n/a |
| Step 1 (PF) | $2^K = \prod(3+1/x_i)$ | foundations/L-9905.3 | PROVED (v4) | **Yes**, 3 lines |
| Step 1 (POS) | $2^K > 3^m$ | foundations/L-9905.2 | PROVED (v4) | **Yes**, 1 line |
| Step 2a | pairwise distinctness | foundations/L-9917.1(1) | PROVED (v17) | sketch (2 lines) — **the one imported proof** |
| Step 2b | every element $\ge 7$ | foundations/L-9906.2 | PROVED (v5) | **Yes**, 3 lines |
| Step 3 | leaf fact and preimage rotation mod 3 | foundations/L-9909.1(2),(3) | PROVED (v7) | **Yes**, proved from scratch (3b–3d) |
| Steps 4, 8 | dictionary $a(x)=t \iff x \equiv r_t\ (2^{t+1})$; $t=1,2$ cases | foundations/L-9912.5 | PROVED (v14) | **Yes** (4a: $t\le2$; 8a: general) |
| Step 5d, 6b | $P(m)$, $W^*(m)$, $\mathcal{E}$ (46 values), $m_0 = 196$ | foundations/L-9917.2–.4 | PROVED (v17) | **recomputed** (test A/T4); containment also proved (5d) |
| Statement, 6b | $\mathcal{E}' = \mathcal{E}\cup\{13,79\}$, threshold 208, $\beta_t$ | foundations/L-9920 | PROVED (v22) | comparison only; $13, 79 \in \mathcal{E}_U$ by own certificates |
| Step 9 | $(\mathrm{V}_F)$; elements $> F$; $m^*(10^6) = 2966$, $m^*(10^9) = 47468$ | foundations/L-9913.1/.5/.10 (+X-9901, X-9903) | PROVED (v18) | cited; used ONLY in L-9927.7 |
| Motivation | word-level $p=3$ sieve vacuous | NEGATIVE_RESULTS.md §3.4 | recorded scout result | context only, not load-bearing |
| Step 8c | profile finiteness at fixed $(m,K)$ | foundations/L-9920.3(3) | PROVED (v22) | argument restated in 1 line |

**Net dependency.** Every original assertion (L-9927.1–.8) follows from NOTATION's
definitions, the inline derivations of Steps 1–10, and the exact integer
computations of tests A/B. The only imported proof is distinctness
(foundations/L-9917.1(1)), itself a two-line subgroup argument independent of
everything here. No circularity: none of L-9905/06/09/12/13/17/20 cites L-9927.
Nothing assumes the Collatz conjecture or its negation; no literature import; no
Baker-type input; no floating point in any decision.

---

## Gap audit

- **Quantifier hygiene.** L-9927.1 is quantified over all $S$-cycles of the formula
  on nonzero odd integers of either sign (and .1(3) over all positive odd $z$ and
  all depths $k$); L-9927.2–.6 over all nontrivial $S$-cycles on positive odds;
  L-9927.7 is conditional on $(\mathrm{V}_F)$ and says only "unchanged"; L-9927.8
  over all valid allowed sets. The trivial cycle: excluded from .2–.6 by the floor
  hypothesis (as in L-9917/L-9920 — $m = 1 \in \mathcal{E}_U$ is the statement
  "no *nontrivial* cycle", and nontrivial $m = 1$ is also L-9905.6); included in
  .1 (and satisfies it: $3 \nmid 1$).
- **Where positivity enters.** Only via (POS) and via "$S(y) \ge x_{\min} \ge 7$"
  (Steps 4, 8). The sign-agnostic layer (Step 3) is verified to hold on the three
  negative cycles, and the positive-only layer is verified to fail there exactly
  at those two points (test A/T3) — hypothesis necessity is witnessed, not
  asserted.
- **Hidden finiteness.** Two infinite tails are handled by proof, not
  extrapolation: (i) all $m \ge 1039$ (monotonicity of $R_U$ + one integer
  comparison, Step 6c); (ii) all depths $k$ in L-9927.1(3) (induction via the
  preimage ladder). The sweep and the threshold meet at $1038/1039$ with no gap.
  The profile maximum in Step 8 is over a finite set (excess caps).
- **Finite verification vs. proof.** The certificates (two integer comparisons per
  $m$; the boundary pair at $1038/1039$; the floors table; T9's two window
  memberships; T10's inequalities) are exact finite computations that ARE the
  content of the corresponding claims. Everything else in the scripts is labelled
  finite verification supporting separately-proved universal statements. The
  envelope re-check (T6) and all displayed ratios are floats and certify nothing.
- **Empirical vs. universal.** The only empirical statements are labelled: the
  $\Gamma$-constant remark (L-9927.5(4)), the T8 deficit measurements, and the
  informational float displays. $\mathcal{E}_U$ and $m_U$ are exact and complete.
- **Boundary cases.** $m = 1$: $W_U(1) = \varnothing$ handled as above. $k = 0$ in
  (5b) (empty prefix), $j = 0$ in (8b), $E = 0$ profiles ($m_1 = m$, empty
  knapsack), and the window endpoint convention (left strict, right closed;
  elimination is the strict inequality (b)) are all explicit. Equality
  $2^K D_U = N_U$ never occurred in the sweep (it would put $K$ in the window —
  conservative direction).
- **Cardinality trap (v22 precedent).** No claim that windows are singletons on
  any uncomputed range; the two-element onset $1171$ is reported as a computation
  (test B/T11), and the completeness argument never uses window cardinality.
- **Independence not assumed.** The sorted bound treats elements as an arbitrary
  $m$-subset of $U$ — valid but lossy (elements are in fact dynamically linked);
  the loss is the content of Q-9927-B/C, and lossiness can only make the
  eliminations *valid*, never wrong.
- **What is honestly NOT proved.** (i) Any elimination beyond $\mathcal{E}_U$
  (in particular the per-class sweep for $40 < m \le 1038$, Q-9927-A); (ii) the
  asymptotic constant of $\mathrm{Wd}_U$; (iii) any statement about the surviving
  $m$ — "not eliminated" is not evidence for a cycle; (iv) any improvement in the
  verified-floor regime (proved NULL at the two operative points); (v) any claim
  that the mod-9 profile-coupled constraint or transport route works (open).
- **Assumptions equivalent to Collatz.** None. The unconditional layer uses three
  one-step computations ($S(1), S(3), S(5)$) and congruence arithmetic; L-9927.7
  alone uses $(\mathrm{V}_F)$, explicitly flagged, in a NULL statement.

---

## Adversarial tests

Scripts live in
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/`
(session-local); the complete code and its verbatim captured output follow. All
decisions are exact (`int`/`Fraction`); floats appear only in labelled
informational displays. **Finite verification, not proof**, except where the
finite computation is itself the claimed content (certificates, floors, T9/T10
memberships), as marked in the Gap audit.

### Script A — the sieve, the main sweep, the elimination set

```python
#!/usr/bin/env python3
# L-9927 verification script A: the closure sieve, the main sweep, and the elimination set.
# Agent fable-02-p21, 2026-07-27.  EXACT integer/Fraction arithmetic in every decision;
# floats appear only in clearly labelled informational ratio displays.
from fractions import Fraction
import math

fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

def nu2(y):
    a = 0
    while y % 2 == 0:
        y //= 2; a += 1
    return a

def S(x):
    y = 3*x + 1; a = nu2(y)
    return y // 2**a, a

def u(k):                      # the closure-sieved sorted floor sequence
    return 3*k + 7 + (k & 1)

# ---------- T1: allowed set U = {odd x >= 7, 3 nmid x} and the closed form ----------
direct = [x for x in range(7, 100001, 2) if x % 3 != 0]
check("T1 closed form u_k", direct == [u(k) for k in range(len(direct))])
check("T1 u_k >= 7+2k (domination over L-9917 floors)", all(u(k) >= 7+2*k for k in range(100000)))
print("T1 PASS: sorted U is exactly u_k = 3k+7+(k mod 2), k >= 0 (exhaustive to 10^5); u_k >= 7+2k.")

# ---------- T2: image(S on odds) = {odd z : 3 nmid z}, both directions ----------
check("T2 images never divisible by 3 (both signs)",
      all(S(y)[0] % 3 != 0 for y in range(-99999, 100000, 2)))
for z in range(1, 100001, 2):
    if z % 3 == 1:
        yy = (4*z-1)//3
        check(f"T2 preimage z={z}", (4*z-1) % 3 == 0 and yy % 2 == 1 and yy >= 1 and S(yy) == (z, 2))
    elif z % 3 == 2:
        yy = (2*z-1)//3
        check(f"T2 preimage z={z}", (2*z-1) % 3 == 0 and yy % 2 == 1 and yy >= 1 and S(yy) == (z, 1))
pre3 = [S(y)[0] for y in range(1, 3*10**5, 2) if S(y)[0] % 3 == 0]
check("T2 no multiple of 3 is an image", pre3 == [])
# depth stability: y_{t+2} = 4 y_t + 1 walks preimage residues through all classes mod 3
for z in range(1, 2001, 2):
    if z % 3 != 0:
        t0 = 1 if z % 3 == 2 else 2
        ys = [(2**(t0+2*i)*z - 1)//3 for i in range(3)]
        check(f"T2 preimage ladder z={z}", ys[1] == 4*ys[0]+1 and ys[2] == 4*ys[1]+1
              and sorted(y % 3 for y in ys) == [0, 1, 2])
print("T2 PASS: image(S) on odds = {odd z : 3 nmid z} (never-0-mod-3 for |y| < 10^5; explicit")
print("         preimages for all odd z <= 10^5; ladder y -> 4y+1 covers all residues mod 3, so")
print("         the image set is unchanged at every surjectivity depth k >= 1).")

# ---------- T3: the four known cycles of the formula; extremal-exponent audit ----------
def find_cycle(x0):
    seen = {}; x = x0; path = []
    while x not in seen:
        seen[x] = len(path); path.append(x); x = S(x)[0]
    return path[seen[x]:]
for x0 in (1, -1, -5, -17):
    cyc = find_cycle(x0)
    check(f"T3 no multiple of 3 in cycle({x0})", all(x % 3 != 0 for x in cyc))
    xm = min(cyc); am = S(xm)[1]
    print(f"T3: cycle through {x0}: elements {tuple(cyc)}, exponent of min({xm}) = {am}"
          + ("   [a(x_min)=1 FAILS: positivity is necessary]" if xm < 0 and am != 1 else
             ("   [trivial: a=2, floor-7 hypothesis fails]" if x0 == 1 else "")))
check("T3 -5 cycle min exponent", S(min(find_cycle(-5)))[1] == 2)
check("T3 -17 cycle min exponent", S(min(find_cycle(-17)))[1] == 4)
check("T3 trivial min exponent", S(1)[1] == 2)
print("T3 PASS: all four known cycles avoid multiples of 3 (the sign-agnostic half); the")
print("         positive-cycle extremal facts fail on negative cycles exactly at positivity.")

# ---------- T4: MAIN SWEEP m = 1..1500, two independent implementations ----------
MMAX = 1500
NU = DU = 1          # N_U(m) = prod (3 u_k + 1), D_U(m) = prod u_k
N17 = D17 = 1        # L-9917 comparison: prod (22+6j), prod (7+2j)
P3 = 1               # 3^m
EU = []; E17 = []; winU = {}; maxwin = 0
mU = m17 = None
for m in range(1, MMAX+1):
    k = m-1
    NU *= 3*u(k)+1; DU *= u(k)
    N17 *= 22+6*k;  D17 *= 7+2*k
    P3 *= 3
    kap = P3.bit_length()
    check(f"T4 kappa cert m={m}", 2**(kap-1) <= P3 < 2**kap)
    Ks = []
    K = kap
    while 2**K * DU <= NU:
        Ks.append(K); K += 1
    winU[m] = Ks; maxwin = max(maxwin, len(Ks))
    if not Ks: EU.append(m)
    Ks7 = []
    K = kap
    while 2**K * D17 <= N17:
        Ks7.append(K); K += 1
    if not Ks7: E17.append(m)
    check(f"T4 W_U(m) subset W*(m) m={m}", set(Ks) <= set(Ks7))
    if mU is None and NU >= 2*P3*DU: mU = m
    if m17 is None and N17 >= 2*P3*D17: m17 = m
# independent implementation B (Fractions)
PUf = Fraction(1); p3 = 1; EU_B = []
for m in range(1, MMAX+1):
    PUf *= Fraction(3) + Fraction(1, u(m-1)); p3 *= 3
    K = p3.bit_length(); Ks = []
    while Fraction(2)**K <= PUf:
        Ks.append(K); K += 1
    if Ks != winU[m]:
        check(f"T4B mismatch m={m}", False)
    if not Ks: EU_B.append(m)
check("T4 implementations agree", EU == EU_B)
E17_known = [1,2,3,4,6,7,8,9,11,12,14,16,18,19,21,23,24,26,28,31,33,36,38,43,45,48,50,
             53,55,60,62,65,67,72,77,84,89,96,101,106,113,118,130,142,159,171]
check("T4 reproduces L-9917.3's E exactly", E17 == E17_known)
check("T4 reproduces L-9917.4's threshold 196", m17 == 196)
check("T4 E(L-9917) subset E_U", set(E17_known) <= set(EU))
check("T4 13, 79 (L-9920's additions) in E_U", 13 in EU and 79 in EU)
check("T4 max E_U < m_U", max(EU) < mU)
check("T4 windows nonempty for all m in [m_U, 1500]", all(winU[m] for m in range(mU, MMAX+1)))
print(f"T4 MAIN RESULT: |E_U| = {len(EU)}, max E_U = {max(EU)}, threshold m_U = {mU}, max |W_U(m)| (m<=1500) = {maxwin}")
print("E_U =", EU)
Eprime = set(E17_known) | {13, 79}
newv = sorted(set(EU) - Eprime)
print(f"new vs L-9920's E' (48 values): {len(newv)} new eliminations; of these > 207: {len([m for m in newv if m > 207])}")
print("new values =", newv)
surv = sorted(set(range(22, 61)) - set(EU))
print("surviving m in [22, 60]:", surv, " (smallest possibly-cyclic least period remains m = 22)")
# threshold boundary certificates
NA = DA = 1
for k in range(mU-1): NA *= 3*u(k)+1; DA *= u(k)
NB, DB = NA*(3*u(mU-1)+1), DA*u(mU-1)
check("T4 threshold certs", NA < 2*3**(mU-1)*DA and NB >= 2*3**mU*DB)
print(f"threshold certificates: N_U({mU-1}) < 2*3^{mU-1}*D_U({mU-1})  [ratio {float(Fraction(NA,2*3**(mU-1)*DA)):.10f}]")
print(f"                        N_U({mU}) >= 2*3^{mU}*D_U({mU})    [ratio {float(Fraction(NB,2*3**mU*DB)):.10f}]")
# tightest margins and sample certificates
worst = None
NA = DA = 1; p3 = 1
for m in range(1, mU):
    NA *= 3*u(m-1)+1; DA *= u(m-1); p3 *= 3
    kap = p3.bit_length()
    if 2**kap*DA > NA:
        marg = Fraction(2**kap*DA, NA)
        if worst is None or marg < worst[0]: worst = (marg, m, kap)
print(f"tightest elimination margin: m = {worst[1]} (kappa = {worst[2]}), 2^kappa*D_U/N_U = {float(worst[0]):.10f}")
for mm in (30, 212, 1024):
    NA = DA = 1
    for k in range(mm): NA *= 3*u(k)+1; DA *= u(k)
    p3 = 3**mm; kap = p3.bit_length()
    check(f"T4 cert m={mm}", 2**(kap-1) <= p3 < 2**kap and 2**kap*DA > NA)
    print(f"certificate m = {mm}: kappa = {kap}; 2^kappa*D_U > N_U with ratio {float(Fraction(2**kap*DA,NA)):.9f} "
          f"(N_U has {NA.bit_length()} bits)")
# m = 30 in full explicit integers (hand-checkable scale)
NA = DA = 1
for k in range(30): NA *= 3*u(k)+1; DA *= u(k)
print("m = 30 fully explicit: 3^30 =", 3**30, " kappa = 48")
print("  D_U(30) =", DA)
print("  N_U(30) =", NA)
print("  2^48*D_U(30) =", 2**48*DA, " > N_U(30): ", 2**48*DA > NA)
print("SCRIPT A RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-27, CPython 3, Linux):**

```text
T1 PASS: sorted U is exactly u_k = 3k+7+(k mod 2), k >= 0 (exhaustive to 10^5); u_k >= 7+2k.
T2 PASS: image(S) on odds = {odd z : 3 nmid z} (never-0-mod-3 for |y| < 10^5; explicit
         preimages for all odd z <= 10^5; ladder y -> 4y+1 covers all residues mod 3, so
         the image set is unchanged at every surjectivity depth k >= 1).
T3: cycle through 1: elements (1,), exponent of min(1) = 2   [trivial: a=2, floor-7 hypothesis fails]
T3: cycle through -1: elements (-1,), exponent of min(-1) = 1
T3: cycle through -5: elements (-5, -7), exponent of min(-7) = 2   [a(x_min)=1 FAILS: positivity is necessary]
T3: cycle through -17: elements (-17, -25, -37, -55, -41, -61, -91), exponent of min(-91) = 4   [a(x_min)=1 FAILS: positivity is necessary]
T3 PASS: all four known cycles avoid multiples of 3 (the sign-agnostic half); the
         positive-cycle extremal facts fail on negative cycles exactly at positivity.
T4 MAIN RESULT: |E_U| = 166, max E_U = 1024, threshold m_U = 1039, max |W_U(m)| (m<=1500) = 2
E_U = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 35, 36, 38, 40, 43, 45, 48, 50, 52, 53, 55, 57, 60, 62, 64, 65, 67, 69, 72, 74, 77, 79, 81, 84, 86, 89, 91, 96, 98, 101, 103, 106, 108, 110, 113, 115, 118, 120, 125, 127, 130, 132, 137, 139, 142, 144, 149, 154, 156, 159, 161, 166, 168, 171, 173, 178, 183, 185, 190, 195, 197, 202, 207, 212, 214, 219, 224, 226, 231, 236, 238, 243, 248, 255, 260, 265, 267, 272, 277, 279, 284, 289, 296, 301, 308, 313, 318, 320, 325, 330, 337, 342, 349, 354, 359, 366, 371, 378, 383, 390, 395, 407, 412, 419, 424, 431, 436, 448, 460, 465, 472, 477, 484, 489, 501, 513, 518, 525, 530, 542, 554, 566, 571, 583, 595, 607, 624, 636, 648, 665, 677, 689, 701, 718, 730, 742, 771, 783, 824, 836, 877, 930, 1024]
new vs L-9920's E' (48 values): 118 new eliminations; of these > 207: 80
new values = [30, 35, 40, 52, 57, 64, 69, 74, 81, 86, 91, 98, 103, 108, 110, 115, 120, 125, 127, 132, 137, 139, 144, 149, 154, 156, 161, 166, 168, 173, 178, 183, 185, 190, 195, 197, 202, 207, 212, 214, 219, 224, 226, 231, 236, 238, 243, 248, 255, 260, 265, 267, 272, 277, 279, 284, 289, 296, 301, 308, 313, 318, 320, 325, 330, 337, 342, 349, 354, 359, 366, 371, 378, 383, 390, 395, 407, 412, 419, 424, 431, 436, 448, 460, 465, 472, 477, 484, 489, 501, 513, 518, 525, 530, 542, 554, 566, 571, 583, 595, 607, 624, 636, 648, 665, 677, 689, 701, 718, 730, 742, 771, 783, 824, 836, 877, 930, 1024]
surviving m in [22, 60]: [22, 25, 27, 29, 32, 34, 37, 39, 41, 42, 44, 46, 47, 49, 51, 54, 56, 58, 59]  (smallest possibly-cyclic least period remains m = 22)
threshold certificates: N_U(1038) < 2*3^1038*D_U(1038)  [ratio 0.9999109034]
                        N_U(1039) >= 2*3^1039*D_U(1039)    [ratio 1.0000176972]
tightest elimination margin: m = 320 (kappa = 508), 2^kappa*D_U/N_U = 1.0000334751
certificate m = 30: kappa = 48; 2^kappa*D_U > N_U with ratio 1.006281279 (N_U has 211 bits)
certificate m = 212: kappa = 337; 2^kappa*D_U > N_U with ratio 1.182203960 (N_U has 2022 bits)
certificate m = 1024: kappa = 1624; 2^kappa*D_U > N_U with ratio 1.000485475 (N_U has 12031 bits)
m = 30 fully explicit: 3^30 = 205891132094649  kappa = 48
  D_U(30) = 6871313566565837585951786314426900768460902578125
  N_U(30) = 1922030019675836215374968185347559223643289860936250163200000000
  2^48*D_U(30) = 1934102826120733750887088865492593002622277702627423682560000000  > N_U(30):  True
SCRIPT A RESULT: ALL CHECKS PASSED
```

### Script B — enclosures, envelope, per-class refinement, NULL, ceilings

```python
#!/usr/bin/env python3
# L-9927 verification script B: enclosures, envelope, per-class refinement, large-floor
# NULL, and the universal-ceiling demonstrations.  Agent fable-02-p21, 2026-07-27.
# EXACT integer/Fraction arithmetic in every decision; floats only in labelled displays.
from fractions import Fraction
from math import factorial
import math

fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

def nu2(y):
    a = 0
    while y % 2 == 0:
        y //= 2; a += 1
    return a

def u(k): return 3*k + 7 + (k & 1)

def r_t(t):
    return (2**t - 1)//3 if t % 2 == 0 else (5*2**t - 1)//3

def log2_big_ratio(NN, DD):
    """informational float log2(NN/DD) for huge integers."""
    sh = NN.bit_length() - DD.bit_length()
    return sh + math.log2(float(Fraction(NN, DD) / Fraction(2)**sh))

# ---------- T5: certified enclosures used by the envelope corollaries ----------
N = 10000
check("T5 log2 3 enclosure", 2**15849 < 3**N < 2**15850)
lo_e = sum(Fraction(1, factorial(k)) for k in range(18)); hi_e = lo_e + Fraction(2, factorial(18))
check("T5 log2 e enclosure", lo_e**N > Fraction(2)**14426 and hi_e**N < Fraction(2)**14427)
print("T5 PASS: certified 1.5849 < log2 3 < 1.5850 and 1.4426 < log2 e < 1.4427")
print("   (e is enclosed by sum_{k<=17} 1/k! < e < same + 2/18!, then both sides raised to 10^4)")

# ---------- T6: envelope numeric re-check (floats; certifies nothing) ----------
worstlo = worsthi = None
lnR = 0.0
for m in range(1, 2001):
    lnR += math.log1p(1/(3*u(m-1)))
    lob = math.log((3*m+8)/8)/9 - 5/1323
    hib = 1/21 + math.log((3*m+4)/7)/9
    if not (lob < lnR < hib):
        check(f"T6 envelope violated at m={m}", False)
    if worstlo is None or lnR - lob < worstlo[0]: worstlo = (lnR-lob, m)
    if worsthi is None or hib - lnR < worsthi[0]: worsthi = (hib-lnR, m)
print(f"T6 PASS (numerical re-check, m <= 2000): (1/9)ln((3m+8)/8) - 5/1323 < ln R_U(m) < 1/21 + (1/9)ln((3m+4)/7);")
print(f"   minimum slack: lower {worstlo[0]:.6f} (at m={worstlo[1]}), upper {worsthi[0]:.6f} (at m={worsthi[1]})")

# ---------- T7: per-class floors under the closure sieve ----------
rows = []
for t in range(1, 15):
    b_cls = b_img = None
    x = 7
    while b_img is None:
        if x % 3 != 0 and nu2(3*x+1) == t:
            if b_cls is None: b_cls = x
            if 3*x+1 >= 7*2**t: b_img = x
        x += 2
    M = 2**(t+1); r = r_t(t)
    seq = [c for c in (r + M*j for j in range(60)) if c >= 7 and c % 3 != 0]
    seqi = [c for c in seq if 3*c+1 >= 7*2**t]
    check(f"T7 t={t} floors agree", seq[0] == b_cls and seqi[0] == b_img)
    rows.append((t, r, b_cls, b_img))
print("T7 PASS: per-class floors, brute force == progression-based, t = 1..14:")
print("   t : r_t    | beta'_t (+3nmid) | beta''_t (+image>=7) | L-9920 beta_t")
b920 = {1:7,2:9,3:13,4:37,5:53,6:21,7:213,8:85,9:853,10:341,11:3413,12:1365,13:13653,14:5461}
for t, r, bc, bi in rows:
    print(f"   {t:2d}: {r:6d} | {bc:8d} | {bi:8d} | {b920[t]:6d}")

# ---------- T8: per-class knapsack demo on every surviving window, m <= 40 ----------
def class_seq(t, count):
    M = 2**(t+1); r = r_t(t); out = []; j = 0
    while len(out) < count:
        c = r + M*j
        if c >= 7 and c % 3 != 0 and 3*c+1 >= 7*2**t:
            out.append(c)
        j += 1
    return out
def Qstar(m, K):
    E = K - m
    best = {(0, 0): Fraction(1)}
    for t in range(2, E+2):
        w = t-1; maxc = E//w
        if maxc == 0: continue
        seq = class_seq(t, maxc)
        pref = [Fraction(1)]
        for x in seq: pref.append(pref[-1]*(3+Fraction(1, x)))
        nb = {}
        for (n, e), v in best.items():
            for c in range(maxc+1):
                if e + c*w > E or n + c > m: break
                key = (n+c, e+c*w); val = v*pref[c]
                if key not in nb or val > nb[key]: nb[key] = val
        best = nb
    a1 = class_seq(1, m)
    p1 = [Fraction(1)]
    for x in a1: p1.append(p1[-1]*(3+Fraction(1, x)))
    out = None
    for (n, e), v in best.items():
        if e == E:
            val = v*p1[m-n]
            if out is None or val > out: out = val
    return out
NU = DU = 1; P3 = 1; surv = []
for m in range(1, 41):
    NU *= 3*u(m-1)+1; DU *= u(m-1); P3 *= 3
    K = P3.bit_length(); Ks = []
    while 2**K*DU <= NU:
        Ks.append(K); K += 1
    if Ks: surv.append((m, Ks, Fraction(NU, DU)))
print("T8: exact per-class maximum Q*_U(m,K) on every surviving window with m <= 40:")
closed = []
for m, Ks, PU in surv:
    for K in Ks:
        q = Qstar(m, K)
        if Fraction(2)**K > q: closed.append((m, K))
        print(f"   m={m:2d} K={K:3d}: 2^K/Q*_U = {float(Fraction(2)**K/q):.6f}; "
              f"deficit log2(P_U/Q*_U) = {math.log2(float(PU/q)):.4f} bits; "
              f"{'ELIMINATED' if Fraction(2)**K > q else 'survives'}")
print("   per-class refinement eliminates beyond E_U in m <= 40:", closed if closed else "NONE")

# ---------- T9: the large-floor (L-9913) regime is untouched: NULL at F = 10^6, 10^9 ----------
for F, m0, Kexp in ((10**6, 2966, 4701), (10**9, 47468, 75235)):
    p3 = 3**m0; kap = p3.bit_length()
    check(f"T9 kappa({m0}) = {Kexp}", kap == Kexp)
    NN = DD = 1; cnt = 0; x = F+1
    while cnt < m0:
        if x % 3 != 0:
            NN *= 3*x+1; DD *= x; cnt += 1
        x += 2
    check(f"T9 thinned window at F={F} still admits K={Kexp} (NULL)", 2**kap*DD <= NN)
    wd = log2_big_ratio(NN, DD) - m0*math.log2(3)
    need = kap - m0*math.log2(3)
    print(f"T9 PASS: F={F}, m={m0}, K={kap}: mod-3-thinned width {wd:.9f} bits >= required {need:.9f} bits")
print("   -> the closure sieve does NOT raise L-9913's lower bounds m*(10^6) = 2966, m*(10^9) = 47468 (NULL).")

# ---------- T10: universal-ceiling demonstration at m = 306 ----------
d = 2**485 - 3**306
check("T10 2^485 > 3^306", d > 0)
ratio = Fraction(d, 3**306)
check("T10 need(306) < 0.00148", Fraction(14427, 10000)*ratio < Fraction(148, 100000))
xx = Fraction(1, 675)
check("T10 any-sieve width floor", Fraction(14426, 10000)*xx/(1+xx) > Fraction(213, 100000))
print(f"T10 PASS: 485 - 306*log2(3) = log2(1 + d/3^306) < 1.4427*(d/3^306) < 0.00148  [d = 2^485 - 3^306,")
print(f"   a {d.bit_length()}-bit positive integer, d/3^306 = {float(ratio):.9f}], while ANY allowed set V with")
print(f"   min V <= 225 has width_V(m) >= width_V(1) = log2(1+1/(3 min V)) >= 1.4426/676 > 0.00213.")
print(f"   Hence K = 485 lies in every such V-window at m = 306: m = 306 survives every such sieve.")

# ---------- T11: window cardinality onset ----------
NU = DU = 1; P3 = 1; first2 = None
for m in range(1, 1501):
    NU *= 3*u(m-1)+1; DU *= u(m-1); P3 *= 3
    K = P3.bit_length(); c = 0
    while 2**K*DU <= NU:
        c += 1; K += 1
    if c >= 2 and first2 is None: first2 = (m, c)
print(f"T11: first m <= 1500 with |W_U(m)| = 2 is m = {first2[0]}; no window has 3 or more elements in this range.")
print("SCRIPT B RESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-27, CPython 3, Linux):**

```text
T5 PASS: certified 1.5849 < log2 3 < 1.5850 and 1.4426 < log2 e < 1.4427
   (e is enclosed by sum_{k<=17} 1/k! < e < same + 2/18!, then both sides raised to 10^4)
T6 PASS (numerical re-check, m <= 2000): (1/9)ln((3m+8)/8) - 5/1323 < ln R_U(m) < 1/21 + (1/9)ln((3m+4)/7);
   minimum slack: lower 0.014916 (at m=1), upper 0.001099 (at m=1)
T7 PASS: per-class floors, brute force == progression-based, t = 1..14:
   t : r_t    | beta'_t (+3nmid) | beta''_t (+image>=7) | L-9920 beta_t
    1:      3 |        7 |        7 |      7
    2:      1 |       17 |       17 |      9
    3:     13 |       13 |       29 |     13
    4:      5 |       37 |       37 |     37
    5:     53 |       53 |      181 |     53
    6:     21 |      149 |      149 |     21
    7:    213 |      469 |      469 |    213
    8:     85 |       85 |     1109 |     85
    9:    853 |      853 |     1877 |    853
   10:    341 |      341 |     2389 |    341
   11:   3413 |     3413 |    11605 |   3413
   12:   1365 |     9557 |     9557 |   1365
   13:  13653 |    30037 |    30037 |  13653
   14:   5461 |     5461 |    70997 |   5461
T8: exact per-class maximum Q*_U(m,K) on every surviving window with m <= 40:
   m= 5 K=  8: 2^K/Q*_U = 0.930070; deficit log2(P_U/Q*_U) = 0.0200 bits; survives
   m=10 K= 16: 2^K/Q*_U = 0.928835; deficit log2(P_U/Q*_U) = 0.0284 bits; survives
   m=15 K= 24: 2^K/Q*_U = 0.941060; deficit log2(P_U/Q*_U) = 0.0278 bits; survives
   m=17 K= 27: 2^K/Q*_U = 0.827554; deficit log2(P_U/Q*_U) = 0.0301 bits; survives
   m=20 K= 32: 2^K/Q*_U = 0.966110; deficit log2(P_U/Q*_U) = 0.0317 bits; survives
   m=22 K= 35: 2^K/Q*_U = 0.851269; deficit log2(P_U/Q*_U) = 0.0329 bits; survives
   m=25 K= 40: 2^K/Q*_U = 0.996893; deficit log2(P_U/Q*_U) = 0.0345 bits; survives
   m=27 K= 43: 2^K/Q*_U = 0.879734; deficit log2(P_U/Q*_U) = 0.0355 bits; survives
   m=29 K= 46: 2^K/Q*_U = 0.776794; deficit log2(P_U/Q*_U) = 0.0366 bits; survives
   m=32 K= 51: 2^K/Q*_U = 0.912342; deficit log2(P_U/Q*_U) = 0.0382 bits; survives
   m=34 K= 54: 2^K/Q*_U = 0.806327; deficit log2(P_U/Q*_U) = 0.0391 bits; survives
   m=37 K= 59: 2^K/Q*_U = 0.947885; deficit log2(P_U/Q*_U) = 0.0402 bits; survives
   m=39 K= 62: 2^K/Q*_U = 0.838341; deficit log2(P_U/Q*_U) = 0.0409 bits; survives
   per-class refinement eliminates beyond E_U in m <= 40: NONE
T9 PASS: F=1000000, m=2966, K=4701: mod-3-thinned width 0.001420037 bits >= required 0.001222861 bits
T9 PASS: F=1000000000, m=47468, K=75235: mod-3-thinned width 0.000022826 bits >= required 0.000015768 bits
   -> the closure sieve does NOT raise L-9913's lower bounds m*(10^6) = 2966, m*(10^9) = 47468 (NULL).
T10 PASS: 485 - 306*log2(3) = log2(1 + d/3^306) < 1.4427*(d/3^306) < 0.00148  [d = 2^485 - 3^306,
   a 476-bit positive integer, d/3^306 = 0.001022762], while ANY allowed set V with
   min V <= 225 has width_V(m) >= width_V(1) = log2(1+1/(3 min V)) >= 1.4426/676 > 0.00213.
   Hence K = 485 lies in every such V-window at m = 306: m = 306 survives every such sieve.
T11: first m <= 1500 with |W_U(m)| = 2 is m = 1171; no window has 3 or more elements in this range.
SCRIPT B RESULT: ALL CHECKS PASSED
```

*Flavor note (informational).* The empty windows cluster at $m$ where
$\{m\alpha\}$ is small — e.g. the continued-fraction denominator $m = 665$
($3^{665}$ just above $2^{1054}$, needed excess $\approx 0.99994$) lies in
$\mathcal{E}_U$ — while the guaranteed survivors of L-9927.8(2) sit at the
opposite phase (e.g. $m = 306$, needed excess $< 0.00148$). The elimination
pattern is the fractional-part orbit of $\log_2 3$ made visible.

---

## Remaining uncertainty

1. **Both sweep implementations share an author.** The elimination list rests on
   two implementations written by the same agent (mirroring L-9917's T1 situation
   before review); an adversarial reviewer should re-derive $\mathcal{E}_U$ from
   the Statement alone. The internal cross-check (exact reproduction of L-9917's
   independently reviewed $\mathcal{E}$ and threshold $196$ from the same code
   path) is reassuring but not independence.
2. **The envelope (Step 7)** is the file's main analytic proof; the two
   integral-comparison directions and the constants $5/1323$, $1/21$ deserve a
   line-by-line check (T6 is only a float re-check).
3. **The density lemma (Step 10, Lemmas B–C)** is the one place with
   equidistribution-flavored reasoning; the two pigeonhole cases and the
   finiteness-contradiction in Lemma C should be checked for quantifier slips.
   Note only *density* of $\{m\alpha\}$ near $1$ is used — never equidistribution.
4. **The per-class demo (T8)** relies on prefix-optimality within classes (argued
   as in foundations/L-9920's Step 5d) and an exact-`Fraction` DP; it is
   informational (nothing is eliminated by it), so an error there cannot
   invalidate $\mathcal{E}_U$, but the recorded deficits guide Q-9927-A.
5. **Scope of L-9927.8(2).** The theorem is about the window method as defined; I
   have tried to state its scope so it cannot be over-read as a barrier against
   hybrid (enumeration/divisibility/Diophantine) methods, which it is not.

## Where a reviewer should look hardest

1. **Step 3 (four lines carry the file):** $x_1 = S(x_m)$ (closure), and
   $2^aS(y) = 3y + 1 \equiv 1 \bmod 3 \Rightarrow 3 \nmid S(y)$. If these are
   right, everything down-stream is bookkeeping.
2. **Step 5b's counting argument** ($k$-th smallest of an $m$-subset of $U$ is
   $\ge u_k$) and the closed form $u_k = 3k + 7 + (k \bmod 2)$ (5a) — an off-by-one
   here would silently shift every window.
3. **Step 6c's completeness:** strict monotonicity of $R_U$, the two boundary
   certificates at $1038/1039$, and the "interval of length $\ge 1$ contains an
   integer" step; also that the sweep truly covers every $m \le 1038$.
4. **Step 4's inequality directions** (multiplying $S(x_{\min}) \ge x_{\min}$ by
   $2^a$; $a \ge 2 \Rightarrow S(y) \le (3y+1)/4$; the slab endpoint algebra), and
   the necessity audit against the trivial/negative cycles (T3).
5. **Step 10:** Lemma B's two cases (especially $\{jh\alpha\} = \{j\theta\}$ and
   the choice $j^* = \lfloor 1/\theta \rfloor$), Lemma C's max-contradiction, and
   the assembly in (10c) including the T10 certificate's use of
   $\ln(1+u) \le u$ and the $\log_2 e$ enclosure.
6. **The tightest certificates** ($m = 320$ at $1.0000335$; threshold pair
   $0.99991/1.00002$): re-verify these few integer comparisons independently
   (bignum in any other language) — they are where a silent arithmetic bug would
   live, and the repo has already recorded float traps exactly here
   (NEGATIVE_RESULTS.md §5).

## Suggested next attack

- **Q-9927-A (finish the per-class layer).** Port L-9920's certified log-domain DP
  to the $A^*_t$ sequences and sweep $m \le 1038$. Expected yield: a few
  eliminations at near-miss windows (the analogue of L-9920's $\{13, 79\}$); the
  T8 deficits ($0.02$–$0.04$ bits and slowly growing) calibrate expectations.
- **Q-9927-B (profile-coupled mod-9 transport).** Each element's residue mod $9$
  is confined to two classes determined by its predecessor's exponent, and the
  predecessor-exponent multiset is the profile. Formulate the resulting bipartite
  feasibility (elements-mod-9 vs. profile capacities) and add it to the knapsack —
  this is the cheapest constraint that is provably invisible to plain sieves
  (L-9927.1(3)) yet strictly finer.
- **Q-9927-C (chains/transport — the identified escape from L-9927.8).** The
  ceiling theorems say membership information cannot finish the job; the closure
  facts L-9927.2 are the proved seeds of *relational* information (each class-1
  element forces an element $3/2$ higher). Layer-population inequalities over
  dyadic height layers would be the first genuinely non-sieve set-level bound;
  the obstruction to quantify is that the class composition of a layer is free.
- **Combine with foundations/L-9910.** The survivors of $\mathcal{E}_U$
  concentrate at $m$ with $\{m\alpha\}$ large (widest windows, CF structure);
  L-9910's convergent constraints speak exactly to those $m$ — a joint statement
  ("every surviving $m \le 1038$ has $K/m$ among specific convergents /
  semiconvergents") may be cheap and would sharpen issue #9's target list.
- **Verification priorities for the packet:** upgrade path is (i) independent
  re-derivation of $\mathcal{E}_U$ (fresh implementation from the Statement),
  (ii) hand-check of Steps 3–6, (iii) spot re-verification of the five decisive
  certificates named above.

---
*File authored by fable-02-p21, 2026-07-27. Status PROPOSED per NOTATION.md
conventions; an independent reviewing agent may upgrade after verification.*
