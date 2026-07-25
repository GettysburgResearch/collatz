# L-9917 — The sorted-element product bound: a sharpened $K$-window for Syracuse cycles, and the exact finite reach of empty-window elimination

```text
Claim ID:      L-9917
Title:         Sorted-element sharpening of the cycle product formula: the window
               3^m < 2^K <= prod_{j<m}(3 + 1/(7+2j)), the complete list of m with
               empty window, and the (1/6)log_2 m growth of the window width
Status:        PROVED
Authoring agent:   fable-02-p11
Reviewing agents:  fable-02-v17 (adversarial review 2026-07-25: PASS)
Created:       2026-07-25
Last updated:  2026-07-25
Dependencies:  NOTATION.md (D-9903 odd part, D-9904 Syracuse map S and step
               exponent a(x) = nu_2(3x+1) >= 1, D-9905 trivial cycle (1),
               D-9908 S-cycle notation x_1 -> ... -> x_m -> x_1, least period m,
               a_i, A_i, K = sum a_i, x_min; empty-product convention).
               L-9905 (Status: PROVED, reviewed by fable-02-v4) — cited for
               L-9905.2 (positivity 2^K > 3^m) and L-9905.3 (product formula
               2^K = prod_{i=1}^m (3 + 1/x_i)).  BOTH ARE RE-DERIVED INLINE in
               Step 2 below (four lines), so this file does not rest on any
               other content of L-9905.
               L-9906 (Status: PROVED, reviewed by fable-02-v5) — cited for
               L-9906.2 (every element of a nontrivial S-cycle is >= 7).  ITS
               ARGUMENT IS RE-DERIVED INLINE in Step 1c (three lines, using only
               S(1) = 1, S(3) = 5, S(5) = 1); this file therefore does NOT depend
               on the m <= 6 enumeration content of L-9906.
               L-9912 (Status: PROVED, fable-02-v14) and L-9915 (Status: PROVED,
               fable-02-v10) are COMPARED AGAINST but are NOT load-bearing: no
               statement of this file is inferred from them.  L-9912.3(1)
               (m_1 >= 2m - K) is re-derived inline in Step 6.
Scope:         All nontrivial S-cycles (D-9908) on the POSITIVE odd integers,
               every least period m >= 1.  L-9917.1, .2 require positivity and
               the floor; they are FALSE for the trivial cycle (1) and for the
               negative cycles (-1), (-5,-7), (-17,...) — see Adversarial tests,
               where the failing hypothesis is identified for each.  L-9917.2 is
               stated for a general odd floor B >= 1; only B = 7 is currently
               justified by a PROVED in-repo fact.  L-9917.3's elimination list
               and L-9917.4's threshold m_0 = 196 are EXACT integer computations,
               complete over ALL m >= 1 (not merely over a searched range).
Related counterexample candidates: none
```

---

## Statement

Throughout, $S$ is the Syracuse map (D-9904) on the positive odd integers,
$S(x) = (3x+1)/2^{\nu_2(3x+1)}$, with step exponent $a(x) := \nu_2(3x+1) \ge 1$.
An $S$-cycle is written as in D-9908: $x_1 \to x_2 \to \dots \to x_m \to x_1$ with
$m \ge 1$ the **least** period, all $x_i$ positive odd, $x_{i+m} := x_i$,
$a_i := a(x_i) \ge 1$, $A_0 := 0$, $A_i := a_1 + \dots + a_i$, $K := A_m = \sum_{i=1}^m a_i$,
$x_{\min} := \min_i x_i$. The **trivial** cycle is the fixed point $(1)$ (D-9905);
a cycle is **nontrivial** if it is not $(1)$.

For an odd integer $B \ge 1$ and $m \ge 1$ define the **sorted-floor product**
$$P_B(m) \;:=\; \prod_{j=0}^{m-1}\left(3 + \frac{1}{B + 2j}\right) \;\in\; \mathbb{Q}_{>0},
\qquad P(m) \;:=\; P_7(m),$$
and its cleared-denominator integer form (for $B = 7$)
$$N(m) \;:=\; \prod_{j=0}^{m-1}(22 + 6j), \qquad D(m) \;:=\; \prod_{j=0}^{m-1}(7 + 2j),
\qquad P(m) = \frac{N(m)}{D(m)} .$$
Define the **excess ratio** and the **window width**
$$R(m) \;:=\; \frac{P(m)}{3^m} \;=\; \prod_{j=0}^{m-1}\left(1 + \frac{1}{21 + 6j}\right),
\qquad \mathrm{Wd}(m) \;:=\; \log_2 R(m) \;=\; \log_2 P(m) - m\log_2 3 .$$
Finally define the **sharpened integer $K$-window**
$$\boxed{\;W^*(m) \;:=\; \bigl\{\, K \in \mathbb{Z} \;:\; 3^m < 2^K \le P(m) \,\bigr\}
\;=\; \bigl\{\, K \in \mathbb{Z} \;:\; 3^m < 2^K \ \text{ and } \ 2^K D(m) \le N(m) \,\bigr\}. \;}$$
(The two descriptions agree because $D(m) > 0$; the right-hand one uses only integer
comparisons and is what every computation in this file performs.)

---

**L-9917.1 (sorted floor).** Let $x_1 \to \dots \to x_m \to x_1$ be a **nontrivial**
$S$-cycle of least period $m$. Then:

1. $x_1, \dots, x_m$ are **pairwise distinct** positive odd integers (consequence of
   least-periodicity alone);
2. $x_i \ge 7$ for **every** $i$ (equivalently $x_{\min} \ge 7$);
3. consequently, writing the elements in increasing order as
   $x_{(0)} < x_{(1)} < \dots < x_{(m-1)}$,
   $$x_{(j)} \;\ge\; 7 + 2j \qquad \text{for every } 0 \le j \le m-1 .$$

More generally, if every element of an $S$-cycle satisfies $x_i \ge B$ for some odd
integer $B \ge 1$, and the $x_i$ are pairwise distinct positive odd integers, then
$x_{(j)} \ge B + 2j$ for $0 \le j \le m-1$.

**L-9917.2 (sharpened product bound).** Let $x_1 \to \dots \to x_m \to x_1$ be an
$S$-cycle on the positive odd integers of least period $m \ge 1$, and let $B \ge 1$ be an
odd integer with $x_i \ge B$ for all $i$. Then
$$3^m \;<\; 2^K \;\le\; P_B(m) \;=\; \prod_{j=0}^{m-1}\left(3 + \frac{1}{B+2j}\right).$$
In particular, for every **nontrivial** $S$-cycle (where $B = 7$ is available by
L-9917.1(2)):
$$\boxed{\;3^m \;<\; 2^K \;\le\; P(m) \;=\; \prod_{j=0}^{m-1}\left(3 + \frac{1}{7+2j}\right),
\qquad\text{i.e.}\qquad K \in W^*(m). \;}$$
Moreover $P_B(m) \le \bigl(3 + \tfrac1B\bigr)^m$ with **strict** inequality for $m \ge 2$;
for $B = 7$ this says $P(m) \le (22/7)^m$, strictly for $m \ge 2$. Hence
$W^*(m) \subseteq W(m)$, where $W(m) = \{K : 3^m < 2^K,\ 2^K 7^m \le 22^m\}$ is the
uniform window of L-9912.4(iii)/L-9915.1: **the sharpened window is never worse and is
strictly narrower in real length for every $m \ge 2$.**

**L-9917.3 (exact elimination set; complete over all $m$).** Define
$$\mathcal{E} \;:=\; \{\, m \ge 1 \;:\; W^*(m) = \varnothing \,\}.$$
Then $\mathcal{E}$ is **finite** and equals **exactly** the following $46$-element set:
$$\mathcal{E} = \{\,1,\,2,\,3,\,4,\,6,\,7,\,8,\,9,\,11,\,12,\,14,\,16,\,18,\,19,\,21,\,23,\,24,\,26,\,28,\,31,\,33,\,36,\,38,$$
$$\qquad\quad 43,\,45,\,48,\,50,\,53,\,55,\,60,\,62,\,65,\,67,\,72,\,77,\,84,\,89,\,96,\,101,\,106,\,113,\,118,\,130,\,142,\,159,\,171\,\},$$
with $\max \mathcal{E} = 171$. Consequently:

> **No nontrivial $S$-cycle has least period $m \in \mathcal{E}$**, and this is obtained
> with **no enumeration of exponent words whatsoever** — two exact integer comparisons
> per value of $m$.

The certificate for each $m \in \mathcal{E}$ consists of the two integer inequalities
$$\text{(a)}\;\; 2^{\,\kappa(m)-1} \le 3^m \qquad\text{and}\qquad
  \text{(b)}\;\; 2^{\,\kappa(m)} D(m) \;>\; N(m),$$
where $\kappa(m) := \mathrm{bl}(3^m)$ is the bit length of $3^m$, i.e. the least integer
$K$ with $2^K > 3^m$. Two comparisons suffice because $K \mapsto 2^K D(m)$ is increasing,
so (b) kills $\kappa(m)$ and every larger $K$, while (a) certifies that $\kappa(m)$ is
the smallest admissible $K$. (All $46$ certificate pairs are exhibited in Adversarial
test T5.)

*Sample fully explicit certificates.*
$$m = 8:\quad 2^{12} = 4096 \le 6561 = 3^8; \qquad
  2^{13} D(8) = 7\,508\,956\,815\,360 \;>\; 7\,438\,558\,167\,040 = N(8),$$
with $D(8) = 916\,620\,705$, $N(8) = 7\,438\,558\,167\,040$.
$$m = 11:\quad 2^{17} = 131\,072 \le 177\,147 = 3^{11}; \qquad
  2^{18} D(11) = 3\,730\,449\,745\,870\,848\,000 \;>\; 3\,244\,996\,614\,789\,529\,600 = N(11).$$
$$m = 14:\quad 2^{22} = 4\,194\,304 \le 4\,782\,969 = 3^{14}; \qquad
  2^{23} D(14) = 3\,541\,480\,083\,544\,014\,323\,712\,000 \;>\; 2\,684\,261\,199\,753\,898\,885\,120\,000 = N(14).$$

*Tightest margin in the whole list.* At $m = 62$ the certificate (b) holds by a factor of
only $1.0000290\ldots$ ($\kappa(62) = 99$); at $m = 171$, by $1.0017771\ldots$. Exact
integer arithmetic is therefore **not** pedantry here: double precision cannot be trusted
to classify $m = 62$.

**L-9917.4 (window width: exact asymptotics, and the exact point at which empty windows
stop forever).**

1. **(Exact closed form.)** For every $m \ge 1$,
   $$R(m) \;=\; \prod_{j=0}^{m-1}\frac{22+6j}{21+6j}
     \;=\; \prod_{j=0}^{m-1}\frac{\tfrac{11}{3}+j}{\tfrac72+j}
     \;=\; \frac{(11/3)_m}{(7/2)_m},$$
   where $(a)_m := a(a+1)\cdots(a+m-1)$ is the Pochhammer symbol. $R$ is strictly
   increasing in $m$ and $R(1) = 22/21$.
2. **(Rigorous two-sided envelope; explicit constants.)** For every $m \ge 1$,
   $$\frac16\ln\frac{6m+21}{21} \;-\; \frac1{196}
     \;<\; \ln R(m) \;<\;
     \frac16\ln\frac{6m+15}{21} \;+\; \frac1{21},$$
   equivalently, in the units that matter ($\mathrm{Wd}(m) = \ln R(m)/\ln 2$),
   $$\frac16\log_2\frac{2m+7}{7} - \frac{1}{196\ln 2}
     \;<\; \mathrm{Wd}(m) \;<\;
     \frac16\log_2\frac{2m+5}{7} + \frac{1}{21\ln 2},$$
   with $\tfrac{1}{196\ln 2} < 0.0073607$ and $\tfrac{1}{21\ln 2} < 0.0686998$. A weaker
   but uniform corollary, valid for **every** $m \ge 1$:
   $$\frac16\log_2 m \;-\; 0.3087 \;<\; \mathrm{Wd}(m) \;<\; \frac16\log_2 m \;+\; 0.0687 .$$
   Hence $\mathrm{Wd}(m) = \tfrac16\log_2 m + O(1)$, i.e. $R(m) = \Theta(m^{1/6})$:
   **the sketch's $m^{1/6}$ rate is correct.** The true constant is
   $$\lim_{m\to\infty}\frac{R(m)}{m^{1/6}} \;=\; \frac{\Gamma(7/2)}{\Gamma(11/3)}
     \;=\; 0.8283111\ldots,\qquad
     \lim_{m\to\infty}\Bigl(\mathrm{Wd}(m) - \tfrac16\log_2 m\Bigr) = -0.2717553\ldots,$$
   consistent with (and strictly inside) the proved envelope
   $[-0.30859,\,-0.23253]$. *(The $\Gamma$-limit is standard Stirling asymptotics for
   $\Gamma(m+a)/\Gamma(m+b)$; it is stated as a REMARK and is **not** used anywhere in
   this file's proofs — every rigorous statement uses only the elementary envelope.)*
3. **(Window cardinality.)** $W^*(m)$ is precisely the set of integers in the half-open
   real interval $\bigl(m\log_2 3,\; m\log_2 3 + \mathrm{Wd}(m)\bigr]$; hence
   $$|W^*(m)| \;\in\; \bigl\{\lfloor \mathrm{Wd}(m)\rfloor,\ \lfloor \mathrm{Wd}(m)\rfloor + 1\bigr\},$$
   so by part 2, $|W^*(m)| \le \tfrac16\log_2 m + 1.069$ for every $m \ge 1$.
   **The number of admissible $K$ per $m$ therefore grows without bound, but only like
   $\tfrac16\log_2 m$.**
4. **(Empty windows TERMINATE; the exact threshold.)** Let
   $$m_0 \;:=\; \min\{\, m \ge 1 : R(m) \ge 2 \,\} \;=\; \min\{\, m \ge 1 : N(m) \ge 2\cdot 3^m D(m)\,\}.$$
   Then $m_0 = 196$, certified by the two exact integer comparisons
   $$N(195) \;<\; 2\cdot 3^{195} D(195), \qquad N(196) \;\ge\; 2\cdot 3^{196} D(196)$$
   (both sides $521$- resp. $524$-digit integers; ratios $0.99993452\ldots$ and
   $1.00077409\ldots$). Since $R$ is strictly increasing, $R(m) \ge 2$, i.e.
   $\mathrm{Wd}(m) \ge 1$, for **every** $m \ge 196$; and a half-open real interval of
   length $\ge 1$ contains an integer. Therefore
   $$W^*(m) \ne \varnothing \quad\text{for every } m \ge 196 .$$
   Combined with the exhaustive exact check of $1 \le m \le 195$ (Adversarial test T1),
   this **proves** that $\mathcal{E}$ is exactly the $46$-element set of L-9917.3 — a
   statement about all $m$, not an artefact of a search range.

   > **Crux, stated honestly.** The empty-window method with floor $7$ has **finite**
   > elimination power: it eliminates exactly $46$ values of $m$, the largest being
   > $171$, and it can never eliminate any $m \ge 196$ (nor, by the computation, any
   > $m \in [172, 195]$). It is **not** true that infinitely many $m$ have
   > $W^*(m) = \varnothing$. This mirrors, and quantitatively refines, L-9915.1's
   > observation that the cruder window is nonempty for all $m \ge 15$: the sharpened
   > bound pushes the "no more free lunches" threshold from $15$ to $196$, but does not
   > remove it.

5. **(How slowly the window really opens.)** The least $m$ with $\mathrm{Wd}(m) \ge 2$
   (i.e. $R(m) \ge 4$, guaranteeing $|W^*(m)| \ge 2$ from there on) is exactly
   $m = 12\,680$ — an exact big-integer computation. So on the range where any
   enumeration is remotely feasible, $|W^*(m)| \le 1$: **for every $m \le 12\,679$ the
   sharpened window contains at most one integer $K$**, and for $m \le 195$ it contains
   at most one and is empty for $46$ of those values.

6. **(General floor: the reach is $\Theta(B)$.)** For an odd floor $B \ge 1$ put
   $m_0(B) := \min\{m : P_B(m) \ge 2\cdot 3^m\}$. Then $m_0(B)/B \to \tfrac{2^6-1}{2} = 31.5$,
   and exactly: $m_0(1) = 13$, $m_0(3) = 71$, $m_0(5) = 133$, $m_0(7) = 196$,
   $m_0(9) = 258$, $m_0(27) = 825$, $m_0(101) = 3156$, $m_0(1001) = 31\,506$
   (finite verification T7; the limit $31.5$ is a REMARK, from
   $\tfrac16\ln(1 + 2m/B) \to \ln 2$). **Structural consequence:** raising the proved
   floor $B$ extends the empty-window method's reach only *linearly* in $B$; the method
   is intrinsically finite for any fixed floor.

**L-9917.5 (combined elimination statement).** Let $\mathcal{E}$ be as in L-9917.3.

1. **(Free re-derivations.)** $\mathcal{E} \cap [1,21] = \{1,2,3,4,6,7,8,9,11,12,14,16,18,19,21\}$
   ($15$ values). Every one of these is eliminated by two integer comparisons and no
   enumeration. This **independently corroborates**, from L-9905/L-9906's elementary core
   only, $15$ of the $21$ cases that L-9906 (hand analysis plus $105 + 1632$ enumerated
   cases) and L-9915 ($1\,192\,712\,185$ enumerated compositions) settled by enumeration.
2. **(What this method does NOT reach below $22$.)** $\{1,\dots,21\}\setminus\mathcal{E}
   = \{5, 10, 13, 15, 17, 20\}$. For these the sharpened window is the singleton
   $W^*(5) = \{8\}$, $W^*(10) = \{16\}$, $W^*(13) = \{21\}$, $W^*(15) = \{24\}$,
   $W^*(17) = \{27\}$, $W^*(20) = \{32\}$, and the elimination genuinely requires
   L-9906/L-9915's composition enumeration. **No claim of this file eliminates them.**
3. **(New eliminations beyond L-9915.)** $\mathcal{E} \cap [22,\infty) $ is the $31$-element set
   $$\{23,\,24,\,26,\,28,\,31,\,33,\,36,\,38,\,43,\,45,\,48,\,50,\,53,\,55,\,60,\,62,\,65,\,67,\,72,\,77,\,84,\,89,\,96,\,101,\,106,\,113,\,118,\,130,\,142,\,159,\,171\}.$$
   For each of these, **no nontrivial $S$-cycle exists**, proved here with no enumeration.
   None of them is covered by L-9906 or L-9915 (whose combined certified range is
   $m \le 21$), and none is covered by the cruder uniform window (which is nonempty for
   every $m \ge 15$, L-9915.1).
4. **(Combined theorem, using PROVED dependencies.)** Combining this file's L-9917.3 with
   L-9915's Main Theorem (PROVED: no nontrivial $S$-cycle with $m \le 21$):
   $$\text{No nontrivial } S\text{-cycle has least period }
     m \in \{1,\dots,21\} \cup \bigl(\mathcal{E}\cap[22,\infty)\bigr),$$
   i.e. the smallest surviving least period is $m = 22$, and the surviving set below
   $200$ is
   $$\{22,25,27,29,30,32,34,35,37,39,40,41,42,44,46,47,49,51,52,54,56,57,58,59,61,63,64,66,$$
   $$\;68,\dots,71,73,\dots,76,78,\dots,83,85,\dots,88,90,\dots,95,97,\dots,100,102,\dots,105,$$
   $$\;107,\dots,112,114,\dots,117,119,\dots,129,131,\dots,141,143,\dots,158,160,\dots,170,172,\dots,199\}.$$
   (Explicitly: $[22,199] \setminus \mathcal{E}$.)

**L-9917.6 (sharpened one-fraction bound for exponent statistics).** Let
$m_1 := \#\{i : a_i = 1\}$. For every nontrivial $S$-cycle of least period $m$:

1. **(Exact integer form.)**
   $$m_1 \;\ge\; 2m - K \;\ge\; 2m - \bigl\lfloor \log_2 P(m) \bigr\rfloor,$$
   where $\lfloor\log_2 P(m)\rfloor = \max\{K \in \mathbb{Z} : 2^K D(m) \le N(m)\}$ is
   computed by integer comparisons alone.
2. **(Real form.)** $m_1 \ge m\bigl(2 - \log_2 P(m)^{1/m}\bigr) = (2 - \log_2 3)m - \mathrm{Wd}(m)$,
   with $2 - \log_2 3 = 0.4150374\ldots$.
3. **(Explicit $m$-dependent form.)** Using L-9917.4(2), for every $m \ge 1$
   $$m_1 \;>\; (2 - \log_2 3)\,m \;-\; \frac16\log_2\frac{2m+5}{7} \;-\; 0.0687
     \;>\; (2 - \log_2 3)\,m \;-\; \frac16\log_2 m \;-\; 0.0687 .$$
4. **(Uniform improvement over L-9912.3(2).)** Since $P(m) \le (22/7)^m$, the bound of
   part 1 is $\ge m\log_2\tfrac{14}{11} = 0.3479233\ldots m$, i.e. it is **never weaker**
   than L-9912's floor-$7$ bound $m_1 > m/3$, and it is strictly stronger for every
   $m \ge 2$ in real terms. Numerically the integer bound of part 1 first strictly beats
   $\lceil m\log_2\tfrac{14}{11}\rceil$ at $m = 8$ ($4$ vs $3$), and by $m = 400$ gives
   $165$ vs $140$.
5. **(Limit.)** $\displaystyle \liminf_{m\to\infty} \frac{m_1}{m} \;\ge\; 2 - \log_2 3 = 0.4150374\ldots$,
   because $\mathrm{Wd}(m)/m \to 0$ by part 2 of L-9917.4. This is a genuine improvement
   on L-9912.3(2)'s $\log_2\tfrac{14}{11} = 0.3479\ldots$; it is also **exactly the
   ceiling of the method**, since $2^K > 3^m$ forces $K > m\log_2 3$ and hence
   $2m - K < (2 - \log_2 3)m$: no bound of this counting type can exceed
   $(2-\log_2 3)m$.

**Correction flags (audit of the originating sketch).**

- **(C1) The $m \le 40$ list is correct as a list of *new* eliminations, but incomplete as
  a list of empty windows.** The sketch reports "$m = 8$ eliminated and, for $m \le 40$,
  also $m \in \{11,14,16,18,19,21,23,24,26,28,31,33,36,38\}$". My exact computation
  confirms **every one of those $15$ values** has $W^*(m) = \varnothing$ — no value is
  wrong and none is missing *from that list's evident intent*. However
  $\mathcal{E} \cap [1,40]$ has $23$ elements: the sketch silently omits
  $\{1,2,3,4,6,7,9,12\}$, which also have $W^*(m) = \varnothing$. Those eight are exactly
  the $m$ for which the **cruder** window of L-9912.4(iii)/L-9915.2 is already empty, so
  the sketch's list is precisely "$\mathcal{E}\cap[1,40]$ minus what the crude window
  already gave". Stated as written ("report all $m$ with $W^*(m) = \varnothing$") it is
  incomplete; stated as "new beyond the uniform window" it is exactly right. Flagged
  rather than corrected, since the intent is recoverable.
- **(C2) The $m^{1/6}$ rate is CORRECT** — and can be sharpened to an exact constant,
  $R(m)/m^{1/6} \to \Gamma(7/2)/\Gamma(11/3) = 0.8283111\ldots$ (L-9917.4(2)).
- **(C3) The sketch's phrase "the number of admissible $K$ per $m$ grows without bound"
  is correct but must not be read as "so empty windows keep occurring".** The truth is the
  opposite and is the main structural finding of this file: empty windows **stop**, and
  stop early. Beyond $m = 195$ there are none, ever; the last one is $m = 171$
  (L-9917.4(4)). The sketch's own suggested test — "compute the exact $m$ beyond which the
  width provably exceeds $1$" — was the right question, and the answer is $m_0 = 196$.
- **(C4) The sketch's suggestion that $W^*(m) = \varnothing$ "improves as $m$ grows" is
  misleading.** The *bound* improves (the ratio $P(m)/(22/7)^m \to 0$ super-polynomially),
  but the *elimination rate* deteriorates: the density of $\mathcal{E}$ in $[1,M]$ falls
  from $23/40$ to $46/200$ to $0$.

---

## Definitions

- $S$, $a(x) = \nu_2(3x+1)$ — D-9904. $S$-cycle notation $x_i$, $a_i$, $A_i$, $K$, least
  period $m$, $x_{\min}$ — D-9908. Trivial cycle $(1)$ — D-9905.
- **Cycle set.** For an $S$-cycle of least period $m$, $\mathcal{C} := \{x_1,\dots,x_m\}$.
  It is closed under $S$ and $S(\mathcal{C}) = \mathcal{C}$.
- **Sorted labelling.** $x_{(0)} \le x_{(1)} \le \dots \le x_{(m-1)}$ is the increasing
  rearrangement of the multiset $\{\!\{x_1,\dots,x_m\}\!\}$; by L-9917.1(1) the
  inequalities are strict and the multiset is a set of size $m$.
- **Bit length.** $\mathrm{bl}(v)$ is the unique $b \ge 1$ with $2^{b-1} \le v < 2^b$, for
  $v \in \mathbb{Z}^+$; equivalently $\mathrm{bl}(v) = \lfloor \log_2 v\rfloor + 1$, and
  $\mathrm{bl}(v)$ is the least $K$ with $2^K > v$.
- **Pochhammer symbol.** $(a)_0 := 1$, $(a)_m := a(a+1)\cdots(a+m-1)$.
- **Window width.** $\mathrm{Wd}(m) := \log_2 P(m) - m\log_2 3$; this is the real length
  of the interval whose integer points form $W^*(m)$.
- **One-count.** $m_1 := \#\{i \in \{1,\dots,m\} : a_i = 1\}$, rotation-invariant.
- Empty products are $1$ (NOTATION.md), so $P_B(0) = R(0) = 1$.
- All arithmetic in the proofs and scripts of this file is exact: `int` and
  `fractions.Fraction`. Floating point appears only in clearly labelled *informational*
  ratio displays and in the numerical envelope re-checks of T6, never in a certificate.

---

## Motivation

L-9906 and L-9915 eliminate small least periods by a two-stage pipeline: (i) derive a
finite integer window of admissible $K$ from global constraints, then (ii) enumerate all
$\binom{K-1}{m-1}$ exponent compositions inside that window. Stage (ii) is what costs —
L-9915 spent $1.19\times10^9$ composition evaluations to reach $m \le 21$, and the count
grows super-exponentially, so brute force dies around $m \approx 25$.

Stage (i) is therefore where leverage lives, and it had been left blunt. Both L-9912 and
L-9915 bound $2^K = \prod_i (3 + 1/x_i)$ by replacing *every* $x_i$ with the global floor
$x_{\min} \ge 7$, giving $2^K \le (22/7)^m$. But the $m$ elements of a cycle are
**distinct** — this is exactly what "least period $m$" means — and all of them are $\ge 7$,
so at most one of them can be $7$, at most one can be $9$, and so on. Only the smallest
element deserves the factor $22/7$; the $j$-th smallest deserves at most
$3 + 1/(7+2j)$. That single observation costs nothing and tightens the window by a factor
$(22/7)^m/P(m)$ which grows super-polynomially in $m$.

The payoff is concrete for the counterexample-construction program of issue #9: it
identifies $31$ new values of $m > 21$ for which **no** exponent word need ever be
searched, and — more importantly for planning — it settles the structural question of how
far this style of argument can go. The answer (L-9917.4(4)) is: exactly $46$ values of
$m$, all $\le 171$, and never again. Any search program that hopes to certify "no cycle"
for large $m$ must therefore obtain its leverage elsewhere (a bigger proved floor $B$,
which buys reach only $\Theta(B)$; or genuinely new arithmetic constraints). Recording
this negative structural fact precisely is as valuable as the $31$ eliminations, because
it prevents another agent from investing in a method whose ceiling is now known.

---

## Proof or construction

### Step 0 — standing setup

Fix an $S$-cycle $x_1 \to \dots \to x_m \to x_1$ of least period $m \ge 1$ on the
positive odd integers, with the cyclic index convention $x_{i+m} = x_i$, $a_{i+m} = a_i$.
The defining step relation is, for every $i \in \mathbb{Z}$,
$$2^{a_i}\,x_{i+1} \;=\; 3x_i + 1. \tag{$\ast_i$}$$
This is immediate from $S(x) = (3x+1)/2^{\nu_2(3x+1)}$ and $a_i = \nu_2(3x_i+1)$.

### Step 1 — L-9917.1 (sorted floor)

**(1a) Least period $\Rightarrow$ the $x_i$ are pairwise distinct.**
Call $p \ge 1$ a *period* of the bi-infinite sequence $(x_i)_{i\in\mathbb{Z}}$ if
$x_{i+p} = x_i$ for all $i \in \mathbb{Z}$. By hypothesis $m$ is a period, and it is the
least one (D-9908).

Suppose $x_i = x_j$ for some $1 \le i < j \le m$, and set $p := j - i$, so $1 \le p \le m-1$.
Applying $S$ repeatedly to the equality $x_{i+p} = x_i$ gives
$x_{i+p+t} = S^t(x_{i+p}) = S^t(x_i) = x_{i+t}$ for every integer $t \ge 0$. Now let
$k \in \mathbb{Z}$ be arbitrary. Choose an integer $t \ge 0$ with $t \equiv k - i \pmod m$;
then, using $m$-periodicity of the index convention, $x_{i+t} = x_k$ and
$x_{i+t+p} = x_{k+p}$. Hence $x_{k+p} = x_{i+t+p} = x_{i+t} = x_k$. As $k$ was arbitrary,
$p$ is a period of $(x_i)$.

The set of periods of a periodic sequence, together with $0$ and negatives, is a subgroup
of $\mathbb{Z}$: if $p, q$ are periods then so are $p+q$ and $-p$. This subgroup is
generated by its least positive element, which is $m$. Hence $m \mid p$, contradicting
$1 \le p \le m - 1$. Therefore no such $i < j$ exists and $x_1, \dots, x_m$ are pairwise
distinct. They are positive odd integers by D-9904/D-9908. $\square$

*(For $m = 1$ the statement is vacuous and true.)*

**(1b) $1 \notin \mathcal{C}$ for a nontrivial cycle.**
$3\cdot 1 + 1 = 4 = 2^2$, so $a(1) = 2$ and $S(1) = 1$. Thus $\{1\}$ is an $S$-cycle of
least period $1$, and it is the trivial cycle. If $1 \in \mathcal{C}$ then, since
$\mathcal{C}$ is the (finite) forward orbit of any of its elements and $S(1) = 1$, we get
$\mathcal{C} = \{S^t(1) : t \ge 0\} = \{1\}$, so $m = 1$ and the cycle is the trivial one.
Contrapositive: a nontrivial cycle does not contain $1$. $\square$

**(1c) $x_i \ge 7$ for all $i$ in a nontrivial cycle (this is L-9906.2; argument restated).**
Compute: $3\cdot 3 + 1 = 10 = 2^1\cdot 5$, so $S(3) = 5$; and $3\cdot 5 + 1 = 16 = 2^4$, so
$S(5) = 1$. Hence $S^2(3) = 1$ and $S(5) = 1$: both $3$ and $5$ **reach $1$**.
If $3 \in \mathcal{C}$ then, $\mathcal{C}$ being closed under $S$, also
$5 = S(3) \in \mathcal{C}$ and $1 = S(5) \in \mathcal{C}$, contradicting (1b). Likewise
$5 \in \mathcal{C}$ forces $1 \in \mathcal{C}$. With (1b) this gives
$\mathcal{C} \cap \{1,3,5\} = \varnothing$. Since every element is a positive odd integer,
every element is $\ge 7$. $\square$

*(This is exactly L-9906.2, and the three lines above are its entire content. Nothing from
the $m \le 6$ case analysis of L-9906 is used anywhere in this file.)*

**(1d) The sorted bound.**
By (1a) the $m$ elements are pairwise distinct; let
$x_{(0)} < x_{(1)} < \dots < x_{(m-1)}$ be their increasing rearrangement. Let $B \ge 1$ be
an odd integer with $x_i \ge B$ for all $i$ (for a nontrivial cycle, $B = 7$ by (1c)).
Induct on $j$. For $j = 0$: $x_{(0)} = x_{\min} \ge B = B + 2\cdot 0$. For $1 \le j \le m-1$:
$x_{(j)} > x_{(j-1)}$ and both are odd integers, so $x_{(j)} \ge x_{(j-1)} + 2$; by the
induction hypothesis $x_{(j-1)} \ge B + 2(j-1)$, whence $x_{(j)} \ge B + 2j$. $\square$

### Step 2 — the product formula and positivity, re-derived inline

These are L-9905.3 and L-9905.2. Four lines:

From $(\ast_i)$, and using $x_i \ne 0$, divide by $x_i$:
$$2^{a_i}\,\frac{x_{i+1}}{x_i} \;=\; 3 + \frac{1}{x_i} \qquad (1 \le i \le m).$$
Multiply over $i = 1, \dots, m$. On the left, $\prod_{i=1}^m 2^{a_i} = 2^{\sum a_i} = 2^K$
and $\prod_{i=1}^m \frac{x_{i+1}}{x_i} = \frac{x_2 x_3 \cdots x_{m+1}}{x_1 x_2 \cdots x_m} = \frac{x_{m+1}}{x_1} = 1$
(telescoping; $x_{m+1} = x_1 \ne 0$). Hence
$$2^K \;=\; \prod_{i=1}^{m}\left(3 + \frac{1}{x_i}\right). \tag{PF}$$
Since every $x_i > 0$, every factor satisfies $3 + 1/x_i > 3 > 0$, so
$$2^K \;>\; 3^m. \tag{POS}$$
$\square$

*(Note that (POS) is where positivity of the $x_i$ enters; it is the hypothesis that fails
for all three negative cycles — see Adversarial test T4.)*

### Step 3 — L-9917.2 (sharpened product bound)

Let the cycle be as in Step 0 with all $x_i \ge B$, $B \ge 1$ odd. Set $f(t) := 3 + 1/t$
on $(0,\infty)$; $f'(t) = -1/t^2 < 0$, so $f$ is strictly decreasing, and $f(t) > 3 > 0$
there.

**The rearrangement step.** The product in (PF) is a product over the index set
$\{1,\dots,m\}$ of positive reals. Let $\sigma : \{0,\dots,m-1\} \to \{1,\dots,m\}$ be the
bijection with $x_{\sigma(j)} = x_{(j)}$ (well defined and bijective because, by
L-9917.1(1), the $x_i$ are pairwise distinct, so the multiset
$\{\!\{x_1,\dots,x_m\}\!\}$ is a set of cardinality $m$ and its increasing enumeration is
a bijective relabelling). Multiplication in $\mathbb{R}_{>0}$ is commutative and
associative, so reindexing by $\sigma$ leaves the product unchanged:
$$\prod_{i=1}^{m}\left(3 + \frac{1}{x_i}\right) \;=\; \prod_{j=0}^{m-1}\left(3 + \frac{1}{x_{(j)}}\right).$$
*(Distinctness is not needed for this identity — a product over a multiset is
permutation-invariant regardless — but it is needed in the next display, and it is what
makes the increasing enumeration strictly increasing.)*

**Termwise domination.** By L-9917.1(1d), $x_{(j)} \ge B + 2j > 0$ for each
$0 \le j \le m-1$, and $f$ is decreasing, so
$$0 \;<\; 3 + \frac{1}{x_{(j)}} \;\le\; 3 + \frac{1}{B + 2j}.$$
A product of finitely many positive reals is monotone in each factor: if
$0 < u_j \le v_j$ for $j = 0,\dots,m-1$ then $\prod u_j \le \prod v_j$ (immediate induction
on $m$: $\prod_{j\le r} u_j \le \bigl(\prod_{j<r} v_j\bigr) u_r \le \prod_{j \le r} v_j$,
using positivity of all factors). Hence
$$2^K \;=\; \prod_{j=0}^{m-1}\left(3 + \frac{1}{x_{(j)}}\right)
  \;\le\; \prod_{j=0}^{m-1}\left(3 + \frac{1}{B+2j}\right) \;=\; P_B(m).$$
Together with (POS) this is the claim: $3^m < 2^K \le P_B(m)$. For a nontrivial cycle,
$B = 7$ is admissible by Step 1c, giving $3^m < 2^K \le P(m)$, i.e. $K \in W^*(m)$.

**Comparison with the uniform bound.** Each factor of $P_B(m)$ satisfies
$3 + 1/(B+2j) \le 3 + 1/B$, with strict inequality whenever $j \ge 1$; all factors are
positive. Hence $P_B(m) \le (3 + 1/B)^m$, strictly for $m \ge 2$. Taking $B = 7$:
$P(m) \le (22/7)^m$, strictly for $m \ge 2$. Consequently
$$W^*(m) = \{K : 3^m < 2^K \le P(m)\} \subseteq \{K : 3^m < 2^K \le (22/7)^m\} = W(m),$$
the last set being exactly L-9915.1's window (its condition $2^K 7^m \le 22^m$ is
$2^K \le (22/7)^m$ cleared of denominators). $\square$

**Cleared-denominator form.** $3 + \frac{1}{7+2j} = \frac{3(7+2j)+1}{7+2j} = \frac{22+6j}{7+2j}$,
so $P(m) = N(m)/D(m)$ with $N(m) = \prod_{j<m}(22+6j)$, $D(m) = \prod_{j<m}(7+2j) > 0$.
Therefore, for integers $K$,
$$2^K \le P(m) \iff 2^K D(m) \le N(m),$$
an inequality between positive integers. Likewise
$3 + \frac{1}{7+2j} = 3\bigl(1 + \frac{1}{21+6j}\bigr)$ gives
$R(m) = P(m)/3^m = \prod_{j<m}\bigl(1 + \frac{1}{21+6j}\bigr) = \prod_{j<m}\frac{22+6j}{21+6j}$,
as stated. $\square$

### Step 4 — L-9917.3 (the elimination set) and the certificate structure

**Window as an integer interval.** Fix $m$. The map $K \mapsto 2^K$ is strictly increasing
on $\mathbb{Z}$, so $\{K : 3^m < 2^K\} = \{K \ge \kappa(m)\}$ with
$\kappa(m) = \mathrm{bl}(3^m)$ (the least $K$ with $2^K > 3^m$), and
$\{K : 2^K D(m) \le N(m)\} = \{K \le \lambda(m)\}$ with
$\lambda(m) := \max\{K \in \mathbb{Z} : 2^K D(m) \le N(m)\} = \lfloor \log_2 P(m)\rfloor$
(finite since $N(m)/D(m)$ is a fixed positive rational). Hence
$W^*(m) = \{\kappa(m), \kappa(m)+1, \dots, \lambda(m)\}$, an integer interval, and
$$W^*(m) = \varnothing \iff \lambda(m) < \kappa(m) \iff 2^{\kappa(m)} D(m) > N(m).$$
So exactly **two** exact integer comparisons decide emptiness for each $m$: (a)
$2^{\kappa(m)-1} \le 3^m$ (which, with $2^{\kappa(m)} > 3^m$, certifies $\kappa(m)$), and
(b) $2^{\kappa(m)} D(m) > N(m)$.

**Elimination.** If a nontrivial $S$-cycle of least period $m$ existed, Step 3 would give
$K \in W^*(m)$, so $W^*(m) \ne \varnothing$. Contrapositive: $W^*(m) = \varnothing$
implies no nontrivial $S$-cycle of least period $m$. $\square$

**Determination of $\mathcal{E}$.** For $1 \le m \le 195$, the two comparisons above were
evaluated exactly, by two independent implementations (exact `Fraction` arithmetic and
cleared-integer arithmetic), which agree on every $m$ (T1, run to $m = 400$). This
produces the $46$ listed values. For $m \ge 196$, Step 5(4) below proves
$W^*(m) \ne \varnothing$. Hence $\mathcal{E}$ is exactly as stated, over all $m \ge 1$.
$\square$

### Step 5 — L-9917.4 (width asymptotics and termination)

**(5.1) Exact closed form.** $\frac{22+6j}{21+6j} = \frac{(22+6j)/6}{(21+6j)/6} = \frac{11/3+j}{7/2+j}$,
so $R(m) = \prod_{j=0}^{m-1}\frac{11/3+j}{7/2+j} = \frac{(11/3)_m}{(7/2)_m}$. Every factor
exceeds $1$ (as $11/3 > 7/2$), so $R$ is strictly increasing in $m$, with $R(0) = 1$,
$R(1) = 22/21$. $\square$

**(5.2) Envelope.** Put $g(t) := \frac{1}{21+6t}$ for $t \ge 0$; $g$ is positive, strictly
decreasing, with $\int g = \frac16\ln(21+6t)$ and $\int g^2 = -\frac{1}{6(21+6t)}$. Write
$u_j := g(j) \in (0, 1/21]$, so $\ln R(m) = \sum_{j=0}^{m-1}\ln(1+u_j)$.

*Sum vs. integral, upper.* For $j \ge 1$, monotonicity gives $u_j = g(j) \le \int_{j-1}^{j} g(t)\,dt$.
Hence, for $m \ge 1$,
$$\sum_{j=0}^{m-1} u_j \;\le\; u_0 + \int_0^{m-1} g(t)\,dt
  \;=\; \frac1{21} + \frac16\ln\frac{21+6(m-1)}{21} \;=\; \frac1{21} + \frac16\ln\frac{6m+15}{21}.$$
*Sum vs. integral, lower.* For $j \ge 0$, $u_j = g(j) \ge \int_{j}^{j+1} g(t)\,dt$, so
$$\sum_{j=0}^{m-1} u_j \;\ge\; \int_0^{m} g(t)\,dt \;=\; \frac16\ln\frac{21+6m}{21} .$$
*Logarithm bounds.* For $u > 0$, $u - \tfrac{u^2}{2} < \ln(1+u) < u$ (standard: the
functions $u - \ln(1+u)$ and $\ln(1+u) - u + u^2/2$ vanish at $0$ and have derivatives
$\frac{u}{1+u} > 0$ and $\frac{u^2}{1+u} > 0$ on $u>0$).

*Tail of squares.* $g^2$ is decreasing, so $u_j^2 \le \int_{j-1}^{j} g^2$ for $j \ge 1$,
whence
$$\sum_{j\ge 0} u_j^2 \;\le\; u_0^2 + \int_0^{\infty} g(t)^2\,dt
  \;=\; \frac1{441} + \frac1{126} \;=\; \frac{2}{882} + \frac{7}{882} \;=\; \frac{9}{882} \;=\; \frac1{98},$$
so $\tfrac12\sum_{j\ge0}u_j^2 \le \tfrac1{196}$.

Combining,
$$\ln R(m) \;<\; \sum_{j=0}^{m-1}u_j \;\le\; \frac1{21} + \frac16\ln\frac{6m+15}{21},$$
$$\ln R(m) \;>\; \sum_{j=0}^{m-1}u_j - \frac12\sum_{j=0}^{m-1}u_j^2
  \;\ge\; \frac16\ln\frac{6m+21}{21} - \frac1{196},$$
which is the stated envelope. Dividing by $\ln 2$ and using
$\frac{6m+21}{21} = \frac{2m+7}{7}$, $\frac{6m+15}{21} = \frac{2m+5}{7}$ gives the
$\log_2$ form. For the uniform corollary: $\frac{2m+7}{7} \ge \frac{2m}{7}$ gives the lower
bound $\frac16\log_2 m + \frac16\log_2\frac27 - \frac{1}{196\ln2} > \frac16\log_2 m - 0.3012259 - 0.0073607 > \frac16\log_2 m - 0.3087$;
and $\frac{2m+5}{7} \le m$ for all $m \ge 1$ (equivalent to $2m+5 \le 7m$, i.e. $m \ge 1$)
gives the upper bound $\frac16\log_2 m + \frac{1}{21\ln 2} < \frac16\log_2 m + 0.0687$.
$\square$

Since $\frac16\log_2 m \to \infty$, $\mathrm{Wd}(m) \to \infty$: the width is unbounded,
but at the rate $\tfrac16\log_2 m$ — to gain one more admissible $K$ one must multiply
$m$ by $2^6 = 64$.

*Remark (not used in any proof).* By Stirling's ratio asymptotic
$\Gamma(m+a)/\Gamma(m+b) \sim m^{a-b}$, (5.1) gives
$R(m) = \frac{\Gamma(7/2)}{\Gamma(11/3)}\cdot\frac{\Gamma(m+11/3)}{\Gamma(m+7/2)} \sim \frac{\Gamma(7/2)}{\Gamma(11/3)}\, m^{11/3-7/2} = \frac{\Gamma(7/2)}{\Gamma(11/3)}\,m^{1/6}$,
with $\Gamma(7/2)/\Gamma(11/3) = 0.8283111241\ldots$ Numerically
$R(400)/(0.8283111\cdot 400^{1/6}) = 1.00128$ (T3).

**(5.3) Window cardinality.** $3^m < 2^K \le P(m)$ reads, after $\log_2$,
$m\log_2 3 < K \le \log_2 P(m) = m\log_2 3 + \mathrm{Wd}(m)$. Both transformations are
equivalences since $\log_2$ is strictly increasing. So $W^*(m)$ is the set of integers in
the half-open interval $(\alpha, \alpha + L]$ with $\alpha := m\log_2 3$,
$L := \mathrm{Wd}(m) \ge 0$. The number of integers in $(\alpha,\beta]$ is
$\lfloor\beta\rfloor - \lfloor\alpha\rfloor$, which for $\beta - \alpha = L$ lies in
$\{\lfloor L\rfloor, \lfloor L\rfloor + 1\}$. With (5.2),
$|W^*(m)| \le \mathrm{Wd}(m) + 1 < \frac16\log_2 m + 1.0687$. $\square$

**(5.4) Termination of empty windows.** If $L = \mathrm{Wd}(m) \ge 1$ then
$(\alpha, \alpha+L] \supseteq (\alpha, \alpha+1]$, and $(\alpha,\alpha+1]$ contains the
integer $\lfloor\alpha\rfloor + 1$ (indeed $\alpha < \lfloor\alpha\rfloor+1 \le \alpha+1$).
Hence $W^*(m) \ne \varnothing$. Now $\mathrm{Wd}(m) \ge 1 \iff R(m) \ge 2 \iff N(m) \ge 2\cdot 3^m D(m)$
(clearing denominators; all quantities positive integers). By (5.1) $R$ is strictly
increasing, so $\{m : R(m) \ge 2\} = \{m \ge m_0\}$ where $m_0 = \min\{m : R(m)\ge2\}$. The
exact integer computation T2 gives $m_0 = 196$, with the boundary certificates
$N(195) < 2\cdot3^{195}D(195)$ and $N(196) \ge 2\cdot3^{196}D(196)$. Therefore
$W^*(m) \ne \varnothing$ for all $m \ge 196$. Together with the exhaustive exact
evaluation of $m \le 195$ (T1), $\mathcal{E}$ is exactly the $46$-element set of
L-9917.3, and $\max\mathcal{E} = 171$. $\square$

*(Analysis alone, without the exact computation, already gives termination: the envelope
lower bound $\frac16\log_2\frac{2m+7}{7} - \frac{1}{196\ln2} \ge 1$ holds for $m \ge 228$
(T6). The exact threshold $196$ is better, and is what is claimed.)*

**(5.5) Width $\ge 2$.** By the same argument, $|W^*(m)| \ge 2$ once $R(m) \ge 4$; the
exact least such $m$ is $12\,680$ (T7). Hence $|W^*(m)| \le 1$ for every $m \le 12\,679$.
$\square$

**(5.6) General floor.** For odd $B \ge 1$, $P_B(m)/3^m = \prod_{j<m}\bigl(1 + \frac{1}{3B+6j}\bigr)$
and the same argument gives: empty $B$-windows cease at
$m_0(B) = \min\{m : \prod_{j<m}(3B+6j+1) \ge 2\prod_{j<m}(3B+6j)\}$. Exact values are
tabulated in T7; $m_0(B)/B \to 31.5$ because
$\sum_{j<m}\frac{1}{3B+6j} \approx \frac16\ln\bigl(1+\frac{2m}{B}\bigr)$ and
$\frac16\ln(1+2m/B) = \ln 2 \iff 1 + 2m/B = 64$. *(The limit is a REMARK; the tabulated
values are exact.)* $\square$

### Step 6 — L-9917.6 (sharpened one-fraction bound)

**(6.1) $m_1 \ge 2m - K$ (this is L-9912.3(1); re-derived).** Each $a_i \ge 1$, and
$a_i \ge 2$ for the $m - m_1$ indices with $a_i \ne 1$. Hence
$$K = \sum_{i=1}^m a_i \;\ge\; 1\cdot m_1 + 2(m - m_1) \;=\; 2m - m_1,$$
i.e. $m_1 \ge 2m - K$. $\square$

**(6.2) Substituting the sharpened window.** For a nontrivial cycle, Step 3 gives
$2^K \le P(m)$, hence $K \le \lfloor\log_2 P(m)\rfloor = \lambda(m)$ (as $K \in \mathbb{Z}$),
so $m_1 \ge 2m - \lambda(m)$. In real form,
$K \le \log_2 P(m) = m\log_2 3 + \mathrm{Wd}(m)$ gives
$$m_1 \;\ge\; 2m - \log_2 P(m) \;=\; m\bigl(2 - \log_2 P(m)^{1/m}\bigr) \;=\; (2-\log_2 3)m - \mathrm{Wd}(m).$$
$\square$

**(6.3) Explicit $m$-dependent form.** Insert the envelope upper bound of (5.2):
$\mathrm{Wd}(m) < \frac16\log_2\frac{2m+5}{7} + \frac{1}{21\ln 2} < \frac16\log_2 m + 0.0687$,
giving
$$m_1 \;>\; (2-\log_2 3)m - \frac16\log_2 m - 0.0687 \qquad (m \ge 1). \square$$

**(6.4) Uniform improvement.** $P(m) \le (22/7)^m$ (Step 3), so
$\log_2 P(m) \le m\log_2\frac{22}{7}$ and
$$m_1 \;\ge\; 2m - \log_2 P(m) \;\ge\; 2m - m\log_2\tfrac{22}{7} \;=\; m\log_2\tfrac{14}{11},$$
which is exactly L-9912.3(2)'s floor-$7$ bound. So the new bound dominates it for every
$m$, strictly for $m \ge 2$ in real terms. $\square$

**(6.5) Limit and ceiling.** $\mathrm{Wd}(m)/m \to 0$ by (5.2), so
$m_1/m \ge (2-\log_2 3) - \mathrm{Wd}(m)/m \to 2 - \log_2 3$, giving
$\liminf m_1/m \ge 2-\log_2 3 = 0.4150374\ldots$. Conversely (POS) forces
$K > m\log_2 3$, so the counting bound itself satisfies $2m - K < (2-\log_2 3)m$: no
improvement of the *floor* $B$ can push this style of bound past $(2-\log_2 3)m$.
$\square$

---

## Dependency audit

| Used where | Statement used | Source | Status | Re-derived inline? |
|---|---|---|---|---|
| Step 0, $(\ast_i)$ | $S(x) = (3x+1)/2^{\nu_2(3x+1)}$, $a(x)=\nu_2(3x+1)\ge1$ | NOTATION.md D-9904 | definition | n/a |
| Step 0, Step 1a | $S$-cycle notation, least period $m$, $K=\sum a_i$, cyclic indices | NOTATION.md D-9908 | definition | n/a |
| Step 1b | trivial $S$-cycle is the fixed point $(1)$ | NOTATION.md D-9905 | definition | n/a |
| Step 2 (PF) | $2^K = \prod_i(3+1/x_i)$ | L-9905.3 | PROVED (fable-02-v4) | **Yes**, 3 lines |
| Step 2 (POS) | $2^K > 3^m$ | L-9905.2 | PROVED (fable-02-v4) | **Yes**, 1 line (from PF + $x_i>0$) |
| Step 1c | every element of a nontrivial cycle is $\ge 7$ | L-9906.2 | PROVED (fable-02-v5) | **Yes**, 3 lines |
| Step 6.1 | $m_1 \ge 2m - K$ | L-9912.3(1) | PROVED (fable-02-v14) | **Yes**, 1 line |
| L-9917.2 comparison remark | $W(m) = \{K : 3^m<2^K,\ 2^K7^m\le22^m\}$ | L-9915.1 | PROVED (fable-02-v10) | quoted only, for **comparison**; not used to derive anything |
| L-9917.5(1),(2),(4) | no nontrivial $S$-cycle with $m \le 21$ | L-9915 Main Thm (+ L-9906) | PROVED | quoted; used **only** in the combined statement L-9917.5(4), never inside a proof |
| L-9917.5(3) | crude window nonempty for all $m \ge 15$ | L-9915.1 | PROVED | quoted for context only |
| L-9917.6(4) | $m_1 > m/3$ from floor $7$ | L-9912.3(2) | PROVED | re-derived as a corollary in Step 6.4 |

**Net dependency.** Every *original* assertion of this file (L-9917.1–.4, .6) follows from
NOTATION.md's definitions plus the inline derivations of Steps 1–6 and the exact integer
computations. L-9905, L-9906, L-9912 are cited for provenance and their used statements
are re-derived in at most three lines each. **L-9915 is not load-bearing anywhere**: it is
used only inside the *combined* statement L-9917.5(4), which is explicitly labelled as a
combination and would simply shrink (to $m \in \mathcal{E}$) if L-9915 were withdrawn.
There is no circularity: L-9905/L-9906 do not cite this file.

**Overlap note.** L-9917.3's set $\mathcal{E}$ contains $\{1,2,3,4,6,7,9,12\}$, which
L-9912.4(iii)/L-9915.2 already obtain from the cruder window. Those overlaps are noted, not
claimed as new; the $38$ values $\mathcal{E}\setminus\{1,2,3,4,6,7,9,12\}$ are new to the
window method, of which $31$ (those $> 21$) are new to the repository outright.

---

## Gap audit

- **Hidden finiteness assumptions.** The only finite computations are (i) the two integer
  comparisons per $m$ for $1 \le m \le 195$, (ii) the two boundary comparisons at
  $m = 195, 196$, (iii) the $m = 12\,680$ threshold, (iv) the $m_0(B)$ table. None is
  extrapolated: the statement "$W^*(m) \ne \varnothing$ for all $m \ge 196$" is
  **proved** by monotonicity of $R$ plus one integer comparison, not observed. This is the
  point at which most window-method write-ups quietly extrapolate; here the infinite tail
  is handled by Step 5.4, and the finite head by exhaustive exact computation, with the
  two ranges meeting exactly at $195/196$ with no gap.
- **Unjustified induction.** Two inductions appear: L-9917.1(1d) (sorted floor, induction
  on $j$, base $j = 0$ explicit) and the product-monotonicity lemma in Step 3 (induction
  on the number of factors, using positivity at each step). Both are elementary and
  fully written out.
- **Boundary cases.** $m = 1$: L-9917.1(1a) is vacuous; the floor still gives
  $2^K \le 22/7 < 4$ together with $2^K > 3$, so $W^*(1) = \varnothing$ — the argument
  covers $m=1$ without appealing to L-9905.6. $m = 2$: distinctness is the statement
  $x_1 \ne x_2$, which follows from least period $2$. Empty products: $P_B(0) = 1$, never
  used since $m \ge 1$. The window endpoint: the definition uses $2^K \le P(m)$ (closed at
  the top), which is the conservative choice; T8 verifies that $2^K D(m) = N(m)$ never
  occurs for $m \le 400$, so nothing hinges on it — and in fact equality in Step 3 would
  force the cycle to be exactly $\{7,9,\dots,7+2(m-1)\}$, impossible since
  $S: 7 \to 11 \to 17 \to 13 \to 5 \to 1$ shows $7$ reaches $1$.
- **Empirical vs. universal.** The elimination list is universal (quantified over all
  $m \ge 1$), because of Step 5.4. The $m^{1/6}$ *constant* $\Gamma(7/2)/\Gamma(11/3)$ and
  the limit $m_0(B)/B \to 31.5$ are explicitly labelled REMARKs relying on standard
  Stirling asymptotics; no rigorous claim uses them. All rigorous width statements use
  only the elementary envelope of Step 5.2.
- **Invalid interchange of limits.** None: the only limit statements are (a) the Stirling
  remark (labelled, unused) and (b) $\liminf m_1/m \ge 2-\log_2 3$, which follows from a
  pointwise inequality plus $\mathrm{Wd}(m)/m \to 0$, itself immediate from the envelope.
- **Circular dependence.** None; see Dependency audit. In particular this file does **not**
  use L-9915's enumeration to prove any of its eliminations, so L-9917.5(3)'s $31$ new
  values are independent of that $1.19\times10^9$-case computation.
- **Nonuniform estimates.** The envelope constants $1/196$, $1/21$, $0.3087$, $0.0687$ are
  absolute and valid for every $m \ge 1$ (numerically re-checked for $1 \le m \le 2000$ in
  T6, with zero violations); nothing is "for large $m$".
- **Assumptions equivalent to Collatz.** None. The floor $x \ge 7$ uses only the three
  finite computations $S(1)=1$, $S(3)=5$, $S(5)=1$. No claim that any other integer
  reaches $1$ is used. (Raising $B$ *would* require such claims — see Remaining
  uncertainty.)
- **Incorrectly assumed independence.** The bound $x_{(j)} \ge 7+2j$ treats the elements as
  if they could be any distinct odd numbers $\ge 7$; they cannot (e.g. $7, 9, 11, 13, 17$
  all reach $1$). This makes the bound *valid but not tight* — a loss, never a gap. No
  step assumes elements are independent or "generic".
- **Finite computation extrapolated to infinite behaviour.** Explicitly avoided; see the
  first bullet. The one place where a reader might expect extrapolation — "and presumably
  no larger $m$ has an empty window" — is instead a proof.
- **Symbolic object $\to$ actual integer.** Not applicable: this file eliminates, it does
  not construct.
- **Known lossiness, stated.** (i) The floor $7$ is far from the truth; (ii) the sorted
  bound ignores that consecutive cycle elements are linked by $(\ast_i)$; (iii) the window
  ignores all divisibility structure ($d \mid c$). Each of these is a place where the
  method is weaker than reality, hence a place where the *eliminations are still valid*
  but more $m$ could in principle be eliminated by a stronger argument.

---

## Adversarial tests

All scripts live in
`/tmp/claude-0/-home-user-collatz/114bdecf-6016-53ed-8de1-7dbb35adc114/scratchpad/`.
Every code block below is the **actual** script and every output block is its **actual
captured output**. All arithmetic is exact (`int` / `fractions.Fraction`); the only
floating-point numbers printed are clearly-labelled informational ratios and the
numerical envelope re-checks (T3, T6), which certify nothing.

**These are finite verifications, not proofs**, except where a finite computation *is*
the whole content of a claim (the $46$ certificate pairs of L-9917.3 and the boundary
comparisons at $m = 195,196$ of L-9917.4(4)); those are exact integer comparisons and are
complete arguments for their statements.

### T1 — the elimination list, by two independent implementations

```python
# L-9917 finite verification #1: exact sharpened K-windows W*(m), two independent
# implementations (Fraction-based and cleared-integer), agreement asserted.
from fractions import Fraction

MMAX = 400

# ---------- Implementation A: exact Fractions ----------
def windows_fraction(mmax):
    out = {}
    P = Fraction(1)          # P(m) = prod_{j<m} (3 + 1/(7+2j))
    for m in range(1, mmax + 1):
        j = m - 1
        P *= Fraction(3) + Fraction(1, 7 + 2 * j)
        lo = Fraction(3) ** m                      # need 2^K > 3^m
        Ks = []
        # K ranges over integers with 3^m < 2^K <= P(m)
        K = 1
        while Fraction(2) ** K <= lo:
            K += 1
        while Fraction(2) ** K <= P:
            Ks.append(K)
            K += 1
        out[m] = (Ks, P)
    return out

# ---------- Implementation B: cleared integers only ----------
# P(m) = N(m)/D(m) with N(m) = prod_{j<m} (22 + 6j), D(m) = prod_{j<m} (7 + 2j).
# Conditions: 3^m < 2^K   and   2^K * D(m) <= N(m).
def windows_integer(mmax):
    out = {}
    N = 1
    D = 1
    for m in range(1, mmax + 1):
        j = m - 1
        N *= (22 + 6 * j)
        D *= (7 + 2 * j)
        three = 3 ** m
        Kmin = three.bit_length()          # least K with 2^K > 3^m
        assert 2 ** Kmin > three and 2 ** (Kmin - 1) <= three
        Ks = []
        K = Kmin
        while (1 << K) * D <= N:
            Ks.append(K)
            K += 1
        out[m] = (Ks, N, D)
    return out

A = windows_fraction(MMAX)
B = windows_integer(MMAX)

# cross-check the two implementations
for m in range(1, MMAX + 1):
    KsA, P = A[m]
    KsB, N, D = B[m]
    assert Fraction(N, D) == P, (m, "P mismatch")
    assert KsA == KsB, (m, KsA, KsB)
print("implementations agree on all m <= %d" % MMAX)

empty = [m for m in range(1, MMAX + 1) if not B[m][0]]
print("m <= %d with W*(m) empty:" % MMAX)
print(empty)
print("count =", len(empty), " max =", max(empty))

# restricted to m <= 40, and to m <= 200
print("empty, m <= 40 :", [m for m in empty if m <= 40])
print("empty, m <= 200:", [m for m in empty if m <= 200])

# reviewer's sketch list for m <= 40
sketch = [8, 11, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38]
mine40 = [m for m in empty if m <= 40]
print("sketch (m<=40)  :", sketch)
print("mine   (m<=40)  :", mine40)
print("in sketch not mine:", sorted(set(sketch) - set(mine40)))
print("in mine not sketch:", sorted(set(mine40) - set(sketch)))
```

```text
implementations agree on all m <= 400
m <= 400 with W*(m) empty:
[1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48, 50, 53, 55, 60, 62, 65, 67, 72, 77, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]
count = 46  max = 171
empty, m <= 40 : [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38]
empty, m <= 200: [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48, 50, 53, 55, 60, 62, 65, 67, 72, 77, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]
sketch (m<=40)  : [8, 11, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38]
mine   (m<=40)  : [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38]
in sketch not mine: []
in mine not sketch: [1, 2, 3, 4, 6, 7, 9, 12]
```

**Verdict.** Every value in the originating sketch's $m \le 40$ list is confirmed; the
sketch omits the eight values $\{1,2,3,4,6,7,9,12\}$, which are precisely those already
empty under the cruder uniform window. See correction flag (C1).

### T2 — the exact termination threshold $m_0 = 196$

```python
# L-9917 finite verification #2: exact width-exceeds-1 threshold m0.
# Width(m) := log2(P(m)) - m*log2(3) = log2(P(m)/3^m).  Width(m) >= 1  <=>  P(m) >= 2*3^m
# <=> N(m) >= 2 * 3^m * D(m)  with N(m)=prod(22+6j), D(m)=prod(7+2j).  Pure integers.
MMAX = 600
N = D = 1
ratios = []          # (m, N - 2*3^m*D  sign)
m0 = None
for m in range(1, MMAX + 1):
    j = m - 1
    N *= (22 + 6*j)
    D *= (7 + 2*j)
    lhs = N
    rhs = 2 * (3 ** m) * D
    if lhs >= rhs and m0 is None:
        m0 = m
    ratios.append((m, lhs >= rhs))
print("m0 = least m with P(m) >= 2*3^m :", m0)
# monotonicity: P(m)/3^m strictly increases (each factor (3+1/(7+2j))/3 = 1+1/(3(7+2j)) > 1)
first_true = [m for m, t in ratios if t]
print("holds for every m in [m0, %d]?  %s" % (MMAX, first_true == list(range(m0, MMAX + 1))))

# exact certificate at m0-1 and m0
def ND(m):
    N = D = 1
    for j in range(m):
        N *= (22 + 6*j); D *= (7 + 2*j)
    return N, D
for mm in (m0 - 1, m0):
    N_, D_ = ND(mm)
    L = N_; R = 2 * (3 ** mm) * D_
    print("m=%d: N(m) %s 2*3^m*D(m)   (digits: %d vs %d)" % (mm, ">=" if L >= R else "<", len(str(L)), len(str(R))))
    print("      ratio N/(2*3^m*D) = %.12f" % (L / R))
```

```text
m0 = least m with P(m) >= 2*3^m : 196
holds for every m in [m0, 600]?  True
m=195: N(m) < 2*3^m*D(m)   (digits: 521 vs 521)
      ratio N/(2*3^m*D) = 0.999934521779
m=196: N(m) >= 2*3^m*D(m)   (digits: 524 vs 524)
      ratio N/(2*3^m*D) = 1.000774097364
```

### T3 — asymptotic envelope and the $m^{1/6}$ rate, checked against exact windows

```python
# L-9917 finite verification #3: asymptotic width vs exact windows.
# R(m) := P(m)/3^m = prod_{j<m} (22+6j)/(21+6j);  Width(m) := log2 R(m).
# Rigorous envelope proved in the file:
#   (1/6)ln(m+7/2) - (1/6)ln(7/2) - 1/196  <=  ln R(m) <= 1/21 + (1/6)ln(m+5/2) - (1/6)ln(7/2)
from fractions import Fraction
import math

def data(mmax):
    N = D = 1
    rows = []
    for m in range(1, mmax + 1):
        j = m - 1
        N *= (22 + 6*j); D *= (21 + 6*j)
        rows.append((m, N, D))
    return rows

rows = data(400)
print(" m   |W*(m)|  Width(m)     lowerbnd     upperbnd    (1/6)log2 m")
bad = 0
for m, N, D in rows:
    lnR = sum(math.log1p(1.0 / (21 + 6*j)) for j in range(m))
    lo = (1/6)*math.log(m + 3.5) - (1/6)*math.log(3.5) - 1/196
    hi = 1/21 + (1/6)*math.log(m + 2.5) - (1/6)*math.log(3.5)
    if not (lo <= lnR <= hi):
        bad += 1
        print("ENVELOPE VIOLATION at m =", m, lo, lnR, hi)
print("envelope violations for 1<=m<=400:", bad)

def windows(mmax):
    N = D = 1
    out = []
    for m in range(1, mmax + 1):
        j = m - 1
        N *= (22 + 6*j); D *= (7 + 2*j)
        Kmin = (3 ** m).bit_length()
        n = 0
        K = Kmin
        while (1 << K) * D <= N:
            n += 1; K += 1
        out.append((m, n, Kmin, Kmin + n - 1 if n else None))
    return out

W = windows(400)
print()
print("  m  |W*(m)|  Kmin..Kmax    Width(m)   floor-check |W*| in {floor,ceil} of Width?")
for m, n, kmin, kmax in W:
    if m in (1,2,5,8,11,14,21,22,50,100,171,172,195,196,197,200,300,400):
        lnR = sum(math.log1p(1.0/(21+6*j)) for j in range(m))
        wd = lnR/math.log(2)
        print("%4d   %3d   %6s..%-6s  %8.5f   %s" % (m, n, kmin, kmax, wd,
              "ok" if n in (math.floor(wd), math.ceil(wd)) else "CHECK"))

viol = []
for m, n, kmin, kmax in W:
    lnR = sum(math.log1p(1.0/(21+6*j)) for j in range(m))
    wd = lnR/math.log(2)
    if n not in (math.floor(wd), math.ceil(wd)):
        viol.append((m, n, wd))
print("count of m<=400 where |W*(m)| not in {floor(Width),ceil(Width)}:", len(viol), viol[:5])

c = math.gamma(3.5)/math.gamma(11/3)
print()
print("predicted R(m) ~ c*m^(1/6), c = Gamma(7/2)/Gamma(11/3) = %.10f" % c)
for m in (10, 50, 100, 196, 400):
    lnR = sum(math.log1p(1.0/(21+6*j)) for j in range(m))
    print("  m=%4d  R(m)=%.8f   c*m^(1/6)=%.8f   ratio=%.8f" % (m, math.exp(lnR), c*m**(1/6), math.exp(lnR)/(c*m**(1/6))))
```

```text
 m   |W*(m)|  Width(m)     lowerbnd     upperbnd    (1/6)log2 m
envelope violations for 1<=m<=400: 0

  m  |W*(m)|  Kmin..Kmax    Width(m)   floor-check |W*| in {floor,ceil} of Width?
   1     0        2..None     0.06711   ok
   2     0        4..None     0.11958   ok
   5     1        8..8        0.23089   ok
   8     0       13..None     0.30671   ok
  11     0       18..None     0.36428   ok
  14     0       23..None     0.41070   ok
  21     0       34..None     0.49326   ok
  22     1       35..35       0.50304   ok
  50     0       80..None     0.68328   ok
 100     1      159..159      0.84286   ok
 171     0      272..None     0.96885   ok
 172     1      273..273      0.97023   ok
 195     1      310..310      0.99991   ok
 196     1      311..311      1.00112   ok
 197     1      313..313      1.00232   ok
 200     1      317..317      1.00590   ok
 300     1      476..476      1.10217   ok
 400     2      634..635      1.17073   ok
count of m<=400 where |W*(m)| not in {floor(Width),ceil(Width)}: 0 []

predicted R(m) ~ c*m^(1/6), c = Gamma(7/2)/Gamma(11/3) = 0.8283111241
  m=  10  R(m)=1.27154092   c*m^(1/6)=1.21579446   ratio=1.04585188
  m=  50  R(m)=1.60578562   c*m^(1/6)=1.58984638   ratio=1.01002565
  m= 100  R(m)=1.79359828   c*m^(1/6)=1.78454222   ratio=1.00507472
  m= 196  R(m)=2.00154819   c*m^(1/6)=1.99634765   ratio=1.00260503
  m= 400  R(m)=2.25126171   c*m^(1/6)=2.24838231   ratio=1.00128066
```

Note that $m = 171$ has $|W^*| = 0$ while $m = 172$ has $|W^*| = 1$: the last empty window
sits at width $\approx 0.969$, just below $1$. Widths below $1$ do not *force* emptiness
(most $m$ with $\mathrm{Wd}(m) < 1$ have $|W^*(m)| = 1$); width $\ge 1$ does force
nonemptiness, which is why $m_0 = 196 > 171$.

### T4 — edge cases: the trivial cycle and the three negative cycles

```python
# L-9917 finite verification #4: edge cases (trivial cycle, negative cycles),
# P(m) <= (22/7)^m domination, and the sharpened one-fraction bound m1 >= 2m - log2 P(m).
from fractions import Fraction
import math

def nu2(n):
    n = abs(n); k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k
def S(x): return (3*x + 1) // 2**nu2(3*x + 1)

print("--- edge case A: trivial S-cycle (1) ---")
cyc = [1]
K = sum(nu2(3*x+1) for x in cyc); m = len(cyc)
prod = Fraction(1)
for x in cyc: prod *= Fraction(3) + Fraction(1, x)
P1 = Fraction(3) + Fraction(1, 7)
print("  cycle", cyc, " m =", m, " K =", K, " 2^K =", 2**K)
print("  product formula prod(3+1/x_i) =", prod, "  equals 2^K:", prod == 2**K)
print("  2^K > 3^m ?", 2**K > 3**m, "   2^K <= P(1)=22/7 ?", Fraction(2**K) <= P1,
      "  <- sorted bound FAILS; hypothesis violated: x=1 < 7 (cycle is trivial)")

print()
print("--- edge case B: negative cycles ---")
for start in (-1, -5, -17):
    c = [start]; x = S(start)
    while x != start: c.append(x); x = S(x)
    m = len(c); K = sum(nu2(3*t+1) for t in c)
    prod = Fraction(1)
    for t in c: prod *= Fraction(3) + Fraction(1, t)
    Pm = Fraction(1)
    for j in range(m): Pm *= Fraction(3) + Fraction(1, 7+2*j)
    print("  cycle %-58s m=%d K=%d" % (str(c), m, K))
    print("     prod(3+1/x_i) = %s ; 2^K = %d ; identity holds: %s" % (prod, 2**K, prod == 2**K))
    print("     positivity 2^K > 3^m : %s   (2^K=%d, 3^m=%d)" % (2**K > 3**m, 2**K, 3**m))
    print("     all elements >= 7    : %s   (min = %d)" % (min(c) >= 7, min(c)))
    print("     sorted bound 2^K <= P(m)=%s : %s" % (Pm, Fraction(2**K) <= Pm))

print()
print("--- P(m) <= (22/7)^m  (so the sharpened bound dominates L-9912/L-9915 uniformly) ---")
ok = True
for m in range(1, 401):
    P = Fraction(1)
    for j in range(m): P *= Fraction(3) + Fraction(1, 7+2*j)
    if not (P <= Fraction(22,7)**m): ok = False; print("FAIL at m =", m)
print("  P(m) <= (22/7)^m for all 1<=m<=400:", ok)
```

```text
--- edge case A: trivial S-cycle (1) ---
  cycle [1]  m = 1  K = 2  2^K = 4
  product formula prod(3+1/x_i) = 4   equals 2^K: True
  2^K > 3^m ? True    2^K <= P(1)=22/7 ? False   <- sorted bound FAILS; hypothesis violated: x=1 < 7 (cycle is trivial)

--- edge case B: negative cycles ---
  cycle [-1]                                                       m=1 K=1
     prod(3+1/x_i) = 2 ; 2^K = 2 ; identity holds: True
     positivity 2^K > 3^m : False   (2^K=2, 3^m=3)
     all elements >= 7    : False   (min = -1)
     sorted bound 2^K <= P(m)=22/7 : True
  cycle [-5, -7]                                                   m=2 K=3
     prod(3+1/x_i) = 8 ; 2^K = 8 ; identity holds: True
     positivity 2^K > 3^m : False   (2^K=8, 3^m=9)
     all elements >= 7    : False   (min = -7)
     sorted bound 2^K <= P(m)=88/9 : True
  cycle [-17, -25, -37, -55, -41, -61, -91]                        m=7 K=11
     prod(3+1/x_i) = 2048 ; 2^K = 2048 ; identity holds: True
     positivity 2^K > 3^m : False   (2^K=2048, 3^m=2187)
     all elements >= 7    : False   (min = -91)
     sorted bound 2^K <= P(m)=1366016/513 : True

--- P(m) <= (22/7)^m  (so the sharpened bound dominates L-9912/L-9915 uniformly) ---
  P(m) <= (22/7)^m for all 1<=m<=400: True
```

**Which hypothesis fails, case by case.**

| object | product formula (PF) | positivity $2^K>3^m$ | floor $\ge 7$ | sorted bound $2^K \le P(m)$ |
|---|---|---|---|---|
| trivial cycle $(1)$, $m=1$, $K=2$ | holds ($4 = 3+1/1$) | holds ($4 > 3$) | **FAILS** ($x=1$) | **FAILS** ($4 > 22/7$) |
| $(-1)$, $m=1$, $K=1$ | holds ($2 = 3-1$) | **FAILS** ($2 < 3$) | **FAILS** (negative) | holds vacuously |
| $(-5,-7)$, $m=2$, $K=3$ | holds ($8 = \tfrac{14}{5}\cdot\tfrac{20}{7}$) | **FAILS** ($8 < 9$) | **FAILS** (negative) | holds vacuously |
| $(-17,-25,-37,-55,-41,-61,-91)$, $m=7$, $K=11$ | holds ($2048$) | **FAILS** ($2048 < 2187$) | **FAILS** (negative) | holds vacuously |

The trivial cycle is the sharpest test: it satisfies *both* L-9905 constraints and is
excluded **only** by the floor — which is exactly why L-9917.1(1b)–(1c) must be proved
before L-9917.2 may be applied. The negative cycles fail positivity, which is the step
where $x_i > 0$ enters (Step 2, (POS)); note the sorted bound happens to hold for them
"by accident" (their factors $3 + 1/x_i < 3$ make the product small), so it is **not** the
sorted bound that excludes negative cycles — a reader must not mistake this file for a
constraint on negative cycles. Scope line, respected.

### T5 — the $46$ certificate pairs, and explicit small-$m$ certificates

```python
# L-9917 finite verification #5: certificates for every empty window, and comparison tables.
N = D = 1
Ns = {}; Ds = {}
EMPTY = []; ROWS = []
for m in range(1, 401):
    j = m - 1
    N *= (22 + 6*j); D *= (7 + 2*j)
    Ns[m] = N; Ds[m] = D
    Kmin = (3**m).bit_length()
    Ks = []
    K = Kmin
    while (1 << K)*D <= N: Ks.append(K); K += 1
    ROWS.append((m, Kmin, Ks))
    if not Ks: EMPTY.append(m)

# crude window of L-9915: 3^m < 2^K and 2^K * 7^m <= 22^m
CRUDE_EMPTY = []
for m in range(1, 401):
    Kmin = (3**m).bit_length()
    if (1 << Kmin) * 7**m > 22**m: CRUDE_EMPTY.append(m)

print("EMPTY  W*(m)=∅ :", EMPTY)
print("count:", len(EMPTY), "  max:", max(EMPTY))
print("CRUDE  W(m)=∅  :", CRUDE_EMPTY)
print("NEW (sharpened only):", sorted(set(EMPTY) - set(CRUDE_EMPTY)))
print("count new:", len(sorted(set(EMPTY) - set(CRUDE_EMPTY))))
print("subset check CRUDE ⊆ EMPTY:", set(CRUDE_EMPTY) <= set(EMPTY))
print()
print("W*(m) for m <= 24 (Kmin..Kmax or empty):")
for m, Kmin, Ks in ROWS[:24]:
    print("   m=%2d  Kmin=%3d  W*(m)=%s" % (m, Kmin, ("{%s}" % ",".join(map(str,Ks))) if Ks else "EMPTY"))
print()
print("Certificates (two integer comparisons per empty m): 2^(Kmin-1) <= 3^m  and  2^Kmin * D(m) > N(m)")
print("   m   Kmin   2^Kmin*D(m) / N(m)  (float, must be > 1)   [both comparisons exact]")
for m in EMPTY:
    Kmin = (3**m).bit_length()
    a = (1 << (Kmin-1)) <= 3**m
    b = (1 << Kmin)*Ds[m] > Ns[m]
    assert a and b, m
    print("  %4d  %4d   %.9f" % (m, Kmin, ((1 << Kmin)*Ds[m]) / Ns[m]))
print()
print("small-m fully explicit certificates:")
for m in (8, 11, 14):
    Kmin = (3**m).bit_length()
    print("  m=%d: 2^%d = %d <= %d = 3^%d ;  2^%d*D = %d > %d = N" % (
        m, Kmin-1, 2**(Kmin-1), 3**m, m, Kmin, (1<<Kmin)*Ds[m], Ns[m]))
    print("       D(%d)=%d  N(%d)=%d   P(%d)=N/D=%.10f  2^%d=%d" % (m, Ds[m], m, Ns[m], m, Ns[m]/Ds[m], Kmin, 2**Kmin))
```

```text
EMPTY  W*(m)=∅ : [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48, 50, 53, 55, 60, 62, 65, 67, 72, 77, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]
count: 46   max: 171
CRUDE  W(m)=∅  : [1, 2, 3, 4, 6, 7, 9, 12]
NEW (sharpened only): [8, 11, 14, 16, 18, 19, 21, 23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48, 50, 53, 55, 60, 62, 65, 67, 72, 77, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]
count new: 38
subset check CRUDE ⊆ EMPTY: True

W*(m) for m <= 24 (Kmin..Kmax or empty):
   m= 1  Kmin=  2  W*(m)=EMPTY
   m= 2  Kmin=  4  W*(m)=EMPTY
   m= 3  Kmin=  5  W*(m)=EMPTY
   m= 4  Kmin=  7  W*(m)=EMPTY
   m= 5  Kmin=  8  W*(m)={8}
   m= 6  Kmin= 10  W*(m)=EMPTY
   m= 7  Kmin= 12  W*(m)=EMPTY
   m= 8  Kmin= 13  W*(m)=EMPTY
   m= 9  Kmin= 15  W*(m)=EMPTY
   m=10  Kmin= 16  W*(m)={16}
   m=11  Kmin= 18  W*(m)=EMPTY
   m=12  Kmin= 20  W*(m)=EMPTY
   m=13  Kmin= 21  W*(m)={21}
   m=14  Kmin= 23  W*(m)=EMPTY
   m=15  Kmin= 24  W*(m)={24}
   m=16  Kmin= 26  W*(m)=EMPTY
   m=17  Kmin= 27  W*(m)={27}
   m=18  Kmin= 29  W*(m)=EMPTY
   m=19  Kmin= 31  W*(m)=EMPTY
   m=20  Kmin= 32  W*(m)={32}
   m=21  Kmin= 34  W*(m)=EMPTY
   m=22  Kmin= 35  W*(m)={35}
   m=23  Kmin= 37  W*(m)=EMPTY
   m=24  Kmin= 39  W*(m)=EMPTY

Certificates (two integer comparisons per empty m): 2^(Kmin-1) <= 3^m  and  2^Kmin * D(m) > N(m)
   m   Kmin   2^Kmin*D(m) / N(m)  (float, must be > 1)   [both comparisons exact]
     1     2   1.272727273
     2     4   1.636363636
     3     5   1.058823529
     4     7   1.376470588
     6    10   1.173913043
     7    12   1.538230885
     8    13   1.009464018
     9    15   1.326724138
    11    18   1.149600505
    12    20   1.515382483
    14    23   1.319350026
    16    26   1.151319598
    18    29   1.006539113
    19    31   1.331728672
    21    34   1.166779678
    23    37   1.023440651
    24    39   1.356058863
    26    42   1.191158457
    28    45   1.047137100
    31    50   1.222140658
    33    53   1.076072445
    36    58   1.258482650
    38    61   1.109385656
    43    69   1.146577880
    45    72   1.011989568
    48    77   1.187357821
    50    80   1.048695373
    53    85   1.231562346
    55    88   1.088347683
    60    96   1.130900244
    62    99   1.000029076
    65   104   1.176351374
    67   107   1.040612218
    72   115   1.083763591
    77   123   1.129540685
    84   134   1.043080039
    89   142   1.088705380
    96   153   1.007136470
   101   161   1.052346139
   106   169   1.100008717
   113   180   1.019472260
   118   188   1.066489800
   130   207   1.035694614
   142   226   1.007158052
   159   253   1.027604673
   171   272   1.001777194

small-m fully explicit certificates:
  m=8: 2^12 = 4096 <= 6561 = 3^8 ;  2^13*D = 7508956815360 > 7438558167040 = N
       D(8)=916620705  N(8)=7438558167040   P(8)=N/D=8115.1976236889  2^13=8192
  m=11: 2^17 = 131072 <= 177147 = 3^11 ;  2^18*D = 3730449745870848000 > 3244996614789529600 = N
       D(11)=14230536445125  N(11)=3244996614789529600   P(11)=N/D=228030.5192501143  2^18=262144
  m=14: 2^22 = 4194304 <= 4782969 = 3^14 ;  2^23*D = 3541480083544014323712000 > 2684261199753898885120000 = N
       D(14)=422177324717523375  N(14)=2684261199753898885120000   P(14)=N/D=6358136.8363398574  2^23=8388608
```

The printed ratios and `P(m)` values are informational floats; the certificates are the
integer comparisons asserted in the loop (`assert a and b`), which passed for all $46$
values.

### T6 — envelope re-check to $m = 2000$, and the analysis-only threshold

```python
import math
L2 = math.log(2)
def Width(m): return sum(math.log1p(1.0/(21+6*j)) for j in range(m))/L2
bad1 = bad2 = 0
for m in range(1, 2001):
    w = Width(m)
    # sharp two-sided form
    lo = (1/6)*math.log2((2*m+7)/7) - 1/(196*L2)
    hi = (1/6)*math.log2((2*m+5)/7) + 1/(21*L2)
    if not (lo < w < hi): bad1 += 1; print("SHARP FAIL", m, lo, w, hi)
    # uniform simplified form
    lo2 = (1/6)*math.log2(m) - 0.3087
    hi2 = (1/6)*math.log2(m) + 0.0687
    if not (lo2 < w < hi2): bad2 += 1; print("UNIFORM FAIL", m, lo2, w, hi2)
print("sharp-envelope failures 1<=m<=2000:", bad1)
print("uniform-envelope failures 1<=m<=2000:", bad2)
m = 1
while (1/6)*math.log2((2*m+7)/7) - 1/(196*L2) < 1: m += 1
print("analysis-only sufficient threshold (sharp form) for Width>=1:", m)
m = 1
while (1/6)*math.log2(m) - 0.3087 < 1: m += 1
print("analysis-only sufficient threshold (uniform form) for Width>=1:", m)
print("2 - log2 3 =", 2 - math.log2(3))
print("log2(14/11) =", math.log2(14/11))
```

```text
sharp-envelope failures 1<=m<=2000: 0
uniform-envelope failures 1<=m<=2000: 0
analysis-only sufficient threshold (sharp form) for Width>=1: 228
analysis-only sufficient threshold (uniform form) for Width>=1: 232
2 - log2 3 = 0.4150374992788439
log2(14/11) = 0.3479233034203068
```

### T7 — width $\ge 2$ threshold, and general-floor reach $m_0(B)$

```python
# Exact integer threshold for Width(m) >= 2, i.e. N(m) >= 4 * 3^m * D(m).
# R is strictly increasing, so the first m >= 1 satisfying it is the threshold; the scan
# starts comparing at m = 12000 only for speed, and the printed 'R(12000) >= 4' flag
# confirms nothing was skipped below that point.
N = D = 1
p3 = 1
ans = None
flag = None
for m in range(1, 14000):
    j = m - 1
    N *= (22 + 6*j); D *= (7 + 2*j); p3 *= 3
    if m == 12000:
        flag = (N >= 4 * p3 * D)
    if m >= 12000 and N >= 4 * p3 * D:
        ans = m; break
print("R(12000) >= 4 already?  (must be False, else the scan skipped the threshold):", flag)
print("exact least m with R(m) >= 4  (Width(m) >= 2):", ans)
```

```text
R(12000) >= 4 already?  (must be False, else the scan skipped the threshold): False
exact least m with R(m) >= 4  (Width(m) >= 2): 12680
```

```python
# General odd floor B: P_B(m) = prod (3 + 1/(B+2j));  R_B(m) = P_B(m)/3^m = prod (3B+6j+1)/(3B+6j)
# m0(B) = least m with R_B(m) >= 2  (integer test: prod(3B+6j+1) >= 2*prod(3B+6j))
def m0(B, cap=200000):
    Nn = Dd = 1
    for m in range(1, cap+1):
        j = m-1
        Nn *= (3*B + 6*j + 1); Dd *= (3*B + 6*j)
        if Nn >= 2*Dd: return m
    return None
for B in (1, 3, 5, 7, 9, 15, 27, 51, 101, 1001):
    v = m0(B)
    print("B = %5d   m0(B) = %7d   m0/B = %.3f" % (B, v, v/B))
```

```text
B =     1   m0(B) =      13   m0/B = 13.000
B =     3   m0(B) =      71   m0/B = 23.667
B =     5   m0(B) =     133   m0/B = 26.600
B =     7   m0(B) =     196   m0/B = 28.000
B =     9   m0(B) =     258   m0/B = 28.667
B =    15   m0(B) =     447   m0/B = 29.800
B =    27   m0(B) =     825   m0/B = 30.556
B =    51   m0(B) =    1581   m0/B = 31.000
B =   101   m0(B) =    3156   m0/B = 31.248
B =  1001   m0(B) =   31506   m0/B = 31.475
```

### T8 — window-endpoint attainment, and the small $S$-orbits used in Step 1

```python
# Boundary check: is the endpoint 2^K = P(m) ever attained (m <= 400)?  And the m<=21 comparison.
N = D = 1
eq = []
for m in range(1, 401):
    j = m-1
    N *= (22+6*j); D *= (7+2*j)
    K = (3**m).bit_length()
    while (1 << K)*D <= N:
        if (1 << K)*D == N: eq.append((m, K))
        K += 1
print("m<=400 with 2^K * D(m) == N(m) exactly (endpoint attained):", eq)

def nu2(n):
    k=0
    while n%2==0: n//=2; k+=1
    return k
def S(x): return (3*x+1)//2**nu2(3*x+1)
for x in (1,3,5,7,9,11):
    o=[x]; y=x
    for _ in range(60):
        y=S(y); o.append(y)
        if y==1: break
    print("  S-orbit of %d: %s" % (x, o))

emp = [1,2,3,4,6,7,8,9,11,12,14,16,18,19,21,23,24,26,28,31,33,36,38,43,45,48,50,53,55,60,62,65,67,72,77,84,89,96,101,106,113,118,130,142,159,171]
print()
print("m in 1..21 with W*(m)=empty :", [m for m in emp if m<=21])
print("m in 1..21 NOT eliminated   :", [m for m in range(1,22) if m not in emp])
print("m in 7..21 with W*(m)=empty (L-9915 range) :", [m for m in emp if 7<=m<=21])
print("m in 7..21 still needing enumeration       :", [m for m in range(7,22) if m not in emp])
print("new eliminations m > 21     :", [m for m in emp if m>21], " count:", len([m for m in emp if m>21]))
```

```text
m<=400 with 2^K * D(m) == N(m) exactly (endpoint attained): []
  S-orbit of 1: [1, 1]
  S-orbit of 3: [3, 5, 1]
  S-orbit of 5: [5, 1]
  S-orbit of 7: [7, 11, 17, 13, 5, 1]
  S-orbit of 9: [9, 7, 11, 17, 13, 5, 1]
  S-orbit of 11: [11, 17, 13, 5, 1]

m in 1..21 with W*(m)=empty : [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 19, 21]
m in 1..21 NOT eliminated   : [5, 10, 13, 15, 17, 20]
m in 7..21 with W*(m)=empty (L-9915 range) : [7, 8, 9, 11, 12, 14, 16, 18, 19, 21]
m in 7..21 still needing enumeration       : [10, 13, 15, 17, 20]
new eliminations m > 21     : [23, 24, 26, 28, 31, 33, 36, 38, 43, 45, 48, 50, 53, 55, 60, 62, 65, 67, 72, 77, 84, 89, 96, 101, 106, 113, 118, 130, 142, 159, 171]  count: 31
```

The $S$-orbits of $1, 3, 5$ printed above are exactly the three computations used in
Step 1c; the orbits of $7, 9, 11$ are printed only to substantiate the Gap-audit remark
that the sorted floor is valid but far from tight.

### T9 — sharpened one-fraction bound, exact integer form

```python
# Sharpened one-fraction bound: m1 >= 2m - floor(log2 P(m)),  exact integer arithmetic.
import math
def floor_log2_frac(N, D):
    # largest K with 2^K <= N/D  <=>  2^K * D <= N
    K = (N // D).bit_length() - 1
    while (1 << (K+1)) * D <= N: K += 1
    while (1 << K) * D > N: K -= 1
    return K
N = D = 1
print("   m   floor(log2 P(m))   NEW: 2m-that   L-9912: ceil(m log2(14/11))   gain   (2-log2 3)m")
rows = [5,8,10,13,15,17,20,22,25,30,50,100,171,196,200,300,400]
for m in range(1, 401):
    j = m-1
    N *= (22+6*j); D *= (7+2*j)
    if m in rows:
        Kf = floor_log2_frac(N, D)
        new = 2*m - Kf
        old = math.ceil(m*math.log2(14/11))
        print("%5d   %10d        %8d      %14d            %5d   %9.2f" % (m, Kf, new, old, new-old, (2-math.log2(3))*m))
```

```text
   m   floor(log2 P(m))   NEW: 2m-that   L-9912: ceil(m log2(14/11))   gain   (2-log2 3)m
    5            8               2                   2                0        2.08
    8           12               4                   3                1        3.32
   10           16               4                   4                0        4.15
   13           21               5                   5                0        5.40
   15           24               6                   6                0        6.23
   17           27               7                   6                1        7.06
   20           32               8                   7                1        8.30
   22           35               9                   8                1        9.13
   25           40              10                   9                1       10.38
   30           48              12                  11                1       12.45
   50           79              21                  18                3       20.75
  100          159              41                  35                6       41.50
  171          271              71                  60               11       70.97
  196          311              81                  69               12       81.35
  200          317              83                  70               13       83.01
  300          476             124                 105               19      124.51
  400          635             165                 140               25      166.01
```

Rows with $m \in \mathcal{E}$ (here $m = 8, 50, 171$) are vacuous as cycle statements — no
such cycle exists — but the arithmetic is displayed for completeness. The `gain` column is
the number of additional forced exponent-$1$ steps over L-9912.3(2).

---

## Remaining uncertainty

1. **Status.** `PROPOSED`. Every mathematical step is written out and every computation is
   exact and reproducible, but no independent agent has checked it. The author's own
   residual doubts are listed below.
2. **Where a reviewer should press hardest.**
   - *Step 1a (distinctness from least periodicity).* The subgroup-of-periods argument is
     standard but the extension "$x_{i+p} = x_i$ for $t \ge 0$" $\Rightarrow$ "$p$ is a
     period of the bi-infinite sequence" is the one place where a sloppy version would be
     wrong. It is written out with the modular choice of $t$; a reviewer should re-check
     that the choice $t \equiv k - i \pmod m$, $t \ge 0$, is legitimate (it is, since
     $m \ge 1$).
   - *The sum-vs-integral inequalities in Step 5.2.* The upper bound peels off $u_0$ and
     integrates on $[0, m-1]$; at $m = 1$ the integral is over a degenerate interval and
     the bound is an equality. Reviewers should confirm the $m = 1$ and $m = 2$ instances
     by hand ($\ln R(1) = \ln(22/21) = 0.046520\ldots < 1/21 = 0.047619\ldots$).
   - *The exhaustive range $1 \le m \le 195$ meeting the proved tail $m \ge 196$.* There
     is no gap, but this is the seam of the argument and deserves an explicit re-run.
   - *The two razor-thin certificates* at $m = 62$ (margin $1.000029$) and $m = 171$
     (margin $1.001777$), and the boundary at $m = 195$ (ratio $0.9999345$). A reviewer
     re-running with exact integers should reproduce these three numbers exactly; anyone
     re-running in floating point may not, and that is the point.
3. **Reproducibility of the embedded blocks.** Every `python` block in Adversarial tests
   was extracted from this file verbatim, executed, and its stdout compared byte-for-byte
   against the `text` block recorded beneath it; all ten pairs match exactly (checker:
   `scratchpad/audit_blocks.py`). A reviewer can and should repeat that check rather than
   trusting the transcription.
4. **Not claimed.** Nothing here eliminates $m \in \{5,10,13,15,17,20,22,25,\dots\}$ or any
   $m \ge 172$. Nothing here constrains negative cycles, $T$-cycles, or $C$-cycles.
   Nothing here bears on divergent trajectories. The $\Gamma$-constant and the
   $m_0(B)/B \to 31.5$ limit are remarks, not claims.
5. **Honest assessment of significance.** The $31$ new eliminations are real but modest,
   and the method is now known to be exhausted. The more durable contribution is
   L-9917.4(4)-(6): a **proof that this whole family of arguments has finite reach**, with
   the exact reach computed ($46$ values, $\max = 171$) and the scaling in the floor
   ($\Theta(B)$) identified. That is a negative result about the method, and it should be
   read as a redirection notice for the cycle-elimination program.

---

## Suggested next attack

1. **Raise the floor $B$ — the only lever with real leverage in this framework.** By
   L-9917.4(6), a proved floor $B$ extends empty-window reach to $m_0(B) \approx 31.5B$.
   A finite verification that every odd $x$ with $7 \le x \le B$ reaches $1$ under $S$
   (exact integer iteration, no extrapolation) is a complete rigorous proof of the floor
   $x_{\min} > B$, and is cheap for $B$ up to $10^7$ or beyond. That would push the
   empty-window frontier from $m \approx 196$ to $m \approx 3\times10^8$, at the cost of
   one large-but-honest computation and an enumeration of the surviving $m$ in that range.
   **Caveat a successor must respect:** the surviving set would then be enormous to
   enumerate, so the deliverable should be the *threshold* $m_0(B)$ plus a characterization
   of survivors, not a literal list.
2. **Use the second-order structure the sorted bound throws away.** Cycle elements are not
   an arbitrary set of distinct odd numbers: consecutive ones satisfy $2^{a_i}x_{i+1} = 3x_i+1$,
   so a small element forces a large successor and vice versa. A bound of the form
   $\prod(3+1/x_i) \le$ (something using the *pairing*) should beat $P(m)$ substantially.
   Concretely: at most $m_1$ elements can be $\equiv 3 \pmod 4$ (L-9912.5), so the sorted
   floor could be refined to a floor *by residue class*.
3. **Combine $W^*(m)$ with the divisibility filter before enumerating.** For the surviving
   $m \le 21$ ($\{5,10,13,15,17,20\}$) and for $22 \le m \le 30$, $|W^*(m)| \le 1$, so
   there is exactly one candidate $K$ per $m$. Any further arithmetic constraint on the
   pair $(m, K)$ — e.g. $2^K - 3^m$ having a prime factor incompatible with $c$ — kills the
   case with no enumeration at all. This is the cheapest available next step and it is
   purely arithmetic.
4. **Verify or refute this file.** A reviewer wishing to break it should target Step 1a and
   the $195/196$ seam (see Remaining uncertainty), and should independently re-implement
   the window in a third way (e.g. `sympy.Rational`, or fixed-point integers with certified
   rounding) and compare the $46$-element set.

---

*Authored by fable-02-p11, 2026-07-25. Status `PROPOSED`; awaiting adversarial review.*
