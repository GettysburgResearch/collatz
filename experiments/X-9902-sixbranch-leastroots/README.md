# X-9902 — six-branch chart least roots: exact m_N (N ≤ 10) and certified small elements u_N (N ≤ 60)

```text
Experiment ID: X-9902
Status: EMPIRICAL (computational record; contains two small PROVED exactness lemmas
        used by the code, stated with proofs below)
Agent: fable-02-p7
Created: 2026-07-25 (run date; see run_log.txt)
Associated issue: #58 (six-branch chart least-root trichotomy)
Associated claims: L-9916 (forward reference — planned claim file for the trichotomy;
        does not exist yet), validation values posted by fable-02 on #58.
Related context (not used): L-9914 certificate (C1) is the inequality 3^12 > 2^19 for
        the same exponent pair; P/Q = 3^12/2^19 = 531441/524288 ≈ 1.013643 is the
        classical near-commensurate pair (12 odd steps vs 19 halvings).
```

## Research question

For the deterministic chart with $P = 3^{12} = 531441$, $Q = 2^{19} = 524288$,
$$x_{n+1} = \lceil P x_n / Q \rceil, \qquad a_n = Q x_{n+1} - P x_n \in [0, Q),$$
and digit alphabet
$$A = \{\, 7 \cdot 3^{2i} \cdot 2^{15-3i} \ :\ i = 0..5 \,\}
    = \{229376,\ 258048,\ 290304,\ 326592,\ 367416,\ 413343\} = \{7\cdot 2^{15} (9/8)^i\},$$
let $S_N = \{x_0 > 0 : a_0, \dots, a_{N-1} \in A\}$ and $m_N = \min S_N$. **How does
$m_N$ grow with $N$?** Consistency with the null "escape law" $m_N \approx (Q/6)^N$
(slope $\log_{10}(Q/6) \approx 4.9414$ per level) supports the escape branch of issue
#58's trichotomy for this chart; a *stall* (small elements persisting at large $N$)
would be a candidate seed for a bounded/recurrent structure. This experiment measures:
(1) $m_N$ **exactly** for $N \le 10$; (2) certified (non-minimal) small elements
$u_N \in S_N$ for $N$ up to 60 by beam search, as upper bounds and stall probes.

## Structure of S_N (5-line derivation of the unique digit-lift)

Requiring $a_n = \alpha_n$ with $\alpha_n \in A \subset [0, Q)$ is, since
$x_{n+1} = (P x_n + a_n)/Q$, the condition $Q \mid P x_n + \alpha_n$ (and then the
digit is automatically $\alpha_n$, the unique representative in $[0, Q)$). Unrolling,
the conjunction over $n = 0..N-1$ is
$Q^{j+1} \mid E_{j+1} := P^{j+1} x_0 + \sum_{i \le j} P^{j-i} Q^i \alpha_i$ for each
$j < N$; since $E_N = P^{N-1-j} E_{j+1} + (\text{terms divisible by } Q^{j+1})$ and
$P$ is odd — a **unit mod $Q^N$** — the single last condition $Q^N \mid E_N$ implies
all the others. Hence, for each word $w = (\alpha_0..\alpha_{N-1}) \in A^N$, the
condition "$x_0 \in S_N$ with digit word $w$" is exactly one residue class
$x_0 \equiv r_w := -P^{-N} \sum_{i<N} P^{N-1-i} Q^i \alpha_i \pmod{Q^N}$, and
distinct words give distinct classes (the digits are recovered from $x_0$ by
replaying the chart). So $S_N$ is a disjoint union of $6^N$ classes mod $Q^N$, and
$m_N$ is the least positive representative over the $6^N$ classes. ($r_w \ne 0$:
$\nu_2(\sum \dots) = \nu_2(\alpha_0) \le 15 < 19N$.)

**Incremental lift (the recurrence run.py uses).** If a word $w$ of length $n$ has
least representative $r < Q^n$ and exact iterate $s = x_n(r)$, then appending digit
$\alpha$ forces $x_0 \equiv r + Q^n t \pmod{Q^{n+1}}$ with the **unique**
$t = (-(P s + \alpha) P^{-(n+1)}) \bmod Q$, giving the new least representative
$r' = r + Q^n t$ and new iterate $s' = (P(s + P^n t) + \alpha)/Q$ (an exact
division, asserted by the code).

## Two exactness lemmas (proved; load-bearing for tasks 1 and 1b)

* **Monotonicity ("roots only grow along lifts").** $r' = r + Q^n t$ with
  $t \in [0, Q)$, so $r' \ge r$: the least representative is non-decreasing along
  every branch of the digit tree. *Proof:* the displayed formula; $t \ge 0$.
  Consequently any node with $r \ge$ (current upper bound) can be pruned from an
  exact minimum search, and $m_{N+1} \ge m_N$.
* **$\theta$-certificate (exactness of the thresholded m_10 computation).** Fix
  $\theta > 0$. Let $V_\theta$ be the set of level-9 nodes with $r \le \theta$, and
  $\widehat{M} := \min\{r' : r' \text{ a level-10 extension of some } v \in
  V_\theta\}$. **If $\widehat{M} \le \theta$ then $m_{10} = \widehat{M}$.**
  *Proof:* let $w$ be a level-10 word with $r_w = m_{10} \le \widehat{M} \le \theta$
  (the min over a superset is $\le \widehat{M}$). Its length-9 prefix $w'$ has
  $r_{w'} \le r_w \le \theta$ by monotonicity, so $w' \in V_\theta$ and $r_w$ is
  among the extensions considered; hence $\widehat{M} \le r_w = m_{10} \le
  \widehat{M}$. $\square$ (If the certificate fails, run.py retries with
  $\theta \mathrel{*}= 8$; it held on the first attempt.)

## Null model (for interpretation only — heuristic, not a theorem)

Modeling the $6^N$ least representatives as i.i.d. uniform on $(0, Q^N)$, the
minimum is $\approx Q^N/6^N \cdot \mathrm{Exp}(1)$, i.e.
$\log_{10} m_N \approx N \log_{10}(Q/6) + O(1) = 4.9414\,N + O(1)$, with $O(1)$
fluctuations of typical size $\pm 0.4$ and per-step increments scattering widely.
A constant-width-$K$ beam, by contrast, can only harvest a constant factor
($\sim 6K$) below $Q^N$, so beam bounds $u_N$ should follow slope
$\log_{10} Q = 5.7196$ — beams are stall PROBES, not minimum trackers. (Corrected
after verification: at the widths actually run, $K \le 1024$, the probe's
*guaranteed* stall-detection window is empty as well — see Interpretation 2.)

## Stall criterion (stated up front)

A *seed signal* = $u_N$ non-increasing over 3 consecutive sampled $N$ (per beam
width). If triggered, run.py dumps the word prefix and residue for follow-up, and no
claim beyond the data is made. **Outcome: not triggered** (see results).

(Sharpened after verification: by the monotonicity lemma every beam minimum
satisfies $u_{n+1} \ge u_n$, so "non-increasing over 3 sampled $N$" is exactly
"*constant* over 3 sampled $N$" — the right signature for a stall. But see
Interpretation 2 for why the criterion has no power at the widths run.)

## Method

* **Task 1 (m_9 exact):** build all $6^8 = 1{,}679{,}616$ level-8 nodes $(r, s)$ by
  the incremental lift, then stream all $6^9 = 10{,}077{,}696$ level-9 extensions
  keeping the running minimum (no level-9 storage). Full enumeration — exact by the
  bijection above.
* **Task 1b (m_10 exact):** during the same stream, collect the $V_\theta$ survivors
  with $r \le \theta := Q^9/20$ (503,982 of 10.08M ≈ the expected 5%), extend only
  those to level 10, apply the $\theta$-certificate ($\widehat{M} \le \theta$ held),
  yielding **exact** $m_{10}$. Feasibility was estimated beforehand from the null
  model ($\sim$0.5M survivors, $\sim$3M extra extensions) — well under budget;
  total actual runtime 6.4 s.
* **Task 2 (u_N probes):** deterministic beam search over the digit tree keeping the
  $K$ smallest $(r, s)$ per level, $K \in \{1, 64, 1024\}$, sampling
  $N \in \{10, 15, 20, 30, 40, 60\}$. **Every reported $u_N$ is certified by exact
  digit replay from $x_0 = u_N$** (all $N$ digits verified to lie in $A$) —
  mandatory, done in run.py. **LLL: skipped, and here is the statement saying so** —
  no external packages are available and a *sound* sliding-block sublattice
  formulation (one whose short vectors provably correspond to elements of $S_N$
  rather than of a relaxation) was not straightforward enough to certify within this
  experiment; the beam bounds are the deliverable, per the task spec. A follow-up
  may formulate the block lattice carefully and compare.
* **Validation gates (all must pass before results are recorded):** (i) brute scan
  $x = 1, 2, \dots$ reproduces $m_1 = 6472$; (ii) the incremental lift reproduces the
  **full residue multiset** of the independent per-word direct formula for
  $N \le 3$ and the minimum at $N = 4$; (iii) the posted values of $m_1, m_2, m_3,
  m_4, m_8$ (fable-02, issue #58) are reproduced exactly; (iv) every $m_N$
  ($N \le 10$) and every $u_N$ is certified by exact digit replay; (v) 200 random
  level-8 nodes replay-certified (digits and iterate). All PASS.

## Exact code, command, environment

* Code: `run.py` in this directory (Python 3 stdlib only; all decisions exact
  integer arithmetic; `random` used only to choose validation samples, fixed seed
  12345 — no reported number depends on randomness; beams deterministic).
  [v11 correction: the text previously said "seeds 0/12345"; `run.py` uses the
  single seed 12345, in `validate_sample`. Reproducibility confirmed: a rerun
  produced byte-identical `table.txt`, `mN_values.txt`, `uN_values.txt`.]
* Command: `python3 run.py` (writes `results/` and prints the log).
* Environment: CPython 3.11.15, Linux x86-64. Runtime: **6.4 s** total (level build
  1.3 s; 8→9 stream + m_10 phase 4.8 s cumulative; beams 0.3 s), per
  `results/run_log.txt`. [v11 correction: "level build 3.0 s" above was a
  transcription slip — the recorded log says 1.3 s, which is also what the 6.4 s
  total is the sum of. An independent rerun took 7.2 s wall on the verifier's
  machine.]
* Parameters: exact levels $N \le 10$; $\theta = Q^9/20$ (retry $\times 8$ if
  certificate fails — not needed); beams $K \in \{1, 64, 1024\}$ to $N = 60$,
  samples $\{10, 15, 20, 30, 40, 60\}$.
* Outputs: `results/table.txt` (main table), `results/mN_values.txt` (full exact
  $m_N$), `results/uN_values.txt` (full certified $u_N$), `results/run_log.txt`
  (complete run log).

## Results

New exact values (this experiment; validation gates $m_{1..4}, m_8$ reproduced):

```text
m_9  = 274731072270742333628800865325991165013963264            (log10 = 44.4389)
m_10 = 1986427850123090115679978949016973174519765670216        (log10 = 48.2981)
```

Main table (verbatim from `results/table.txt`):

```text
exact least roots m_N  (N = 1..10; N<=4 and N=8 are the posted validation gates)
  N |  log10 m_N | m_N
  1 |     3.8110 | 6472
  2 |     9.2808 | 1908874353
  3 |    13.6523 | 44906374791168
  4 |    20.4397 | 275202518480529950784
  5 |    23.8664 | 735266885070322294097984
  6 |    28.6983 | 49927377479016341945330731072
  7 |    34.4950 | 31262847560142629190894965371116657
  8 |    38.2592 | 181625992579115023082252809688279976000
  9 |    44.4389 | 274731072270742333628800865325991165013963264
 10 |    48.2981 | 1986427850123090115679978949016973174519765670216

fit slope of log10 m_N vs N (N=1..10):  4.9486
null-model slope log10(Q/6):            4.9414

beam upper bounds u_N (certified elements of S_N; NOT minima)
  N | log10 u_N (K=1) | log10 u_N (K=64) | log10 u_N (K=1024)
 10 |          56.4283 |          54.8305 |          53.2087
 15 |          84.5269 |          83.1135 |          81.5223
 20 |         113.7827 |         111.7784 |         110.4857
 30 |         170.7697 |         169.4638 |         167.7249
 40 |         227.8473 |         225.5012 |         225.1169
 60 |         341.3577 |         339.8797 |         339.6903
fit slope log10 u_N vs N, K=   1:  5.7030   (log10 Q = 5.7196)
fit slope log10 u_N vs N, K=  64:  5.7012   (log10 Q = 5.7196)
fit slope log10 u_N vs N, K=1024:  5.7326   (log10 Q = 5.7196)

calibration at N=10: u_10/m_10 = 1.35e+08 (K=1), 3.41e+06 (K=64), 8.14e+04 (K=1024)
stall signal: none
```

## Interpretation (EMPIRICAL — finite data, no unbounded inference)

1. **Escape-law consistency.** Over the ten exact values, $\log_{10} m_N$ grows with
   fitted slope $4.9486$, against the null-model slope $\log_{10}(Q/6) = 4.9414$,
   with per-step increments scattering in $[3.43, 6.79]$ exactly as a
   min-of-exponentials null predicts. **The $0.15\%$ numerical agreement is not a
   precision match and should not be quoted as one** [v11 correction: the original
   text led with "agreement to $\approx 0.15\%$"]: the residual scatter is large
   (sd $0.68$ in $\log_{10}$), so the ten points determine the slope only to about
   $\pm 0.075$, i.e. $\pm 1.5\%$. The honest statement is that the data are
   *consistent* with the null slope (they sit $0.10\sigma$ from it), not that they
   confirm it to three digits; the extended fit over $N \le 16$ in the verification
   note gives $4.9973 \pm 0.032$, still consistent but $1.8\sigma$ high. Within
   $N \le 16$ the data are fully consistent with the escape law
   $m_N \approx (Q/6)^N$ and show **no** anomalous small-root family. This supports
   (does not prove) the escape branch of issue #58's dichotomy for this chart.
2. **No stall — and this carries essentially no evidential weight.** The stall
   criterion was not triggered at any beam width; every sampled $u_N$ grows by
   $\ge 10^{27}$ between consecutive samples. [v11 correction: the original text
   stopped here, which over-presents a null result.] By monotonicity, an all-time
   root $x_*$ has *every* prefix root $\le x_*$, so its branch is retained by a
   width-$K$ beam as soon as fewer than $K$ level-$n$ nodes lie below it at every
   $n$; under the null that needs
   $K \gtrsim \max_n 6^n\min(1, x_*/Q^n) \approx x_*^{\log 6/\log Q} = x_*^{0.136}$.
   So $K = 1024$ is *guaranteed* to catch a stall only for $x_* \lesssim 10^{22}$ —
   a range already excluded outright by the exact value $m_{10} \approx 2\cdot
   10^{48}$ (and by $m_{16} \approx 4.6\cdot10^{78}$ in the verification note). The
   probe's guaranteed detection window is empty given the exact data, so the
   non-trigger is **no information**, not evidence against a stall.
3. **Beams cannot see the minimum.** Beam slopes ($5.70$–$5.73$) track
   $\log_{10} Q = 5.7196$, not $\log_{10}(Q/6)$, and the calibration row shows the
   $N = 10$ beam bound is already $10^{5}$–$10^{8}$ above the true $m_{10}$,
   worsening like $6^N/(6K)$ up to an $O(10)$ constant (verified: the observed
   $N = 10$ ratios exceed $6^N/(6K)$ by factors $8$–$22$). Directly confirmed in the
   verification note: the branch realising $m_{10}$ has prefix rank $6934$ out of
   $6^5$ at level 5, so a $K = 1024$ beam has already discarded it by level 5.
   Consequence for L-9916: **at the widths run here ($K \le 1024$) beam search is
   useless both as a minimum tracker and (per bullet 2) as a stall probe for this
   chart.** [v11 correction: the original text said "heuristic search cannot decide
   the trichotomy at depth; only exact/structural methods ... can" — an unbounded
   claim about an entire class of methods drawn from three beam widths, which
   README §10 does not license.] What the data license is the narrower statement
   above; a beam of width $\sim 6^N$ would track the minimum by construction, and
   nothing measured here bounds what other heuristics (certified lattice reduction,
   say) could achieve.
4. **Cheap exact frontier.** The $\theta$-certificate scheme cost only $\sim$30%
   over the plain $m_9$ enumeration; the same scheme with $\theta$ tuned by the null
   model should reach $m_{12}$–$m_{13}$ within minutes (see Limitations for the
   memory wall), if issue #58 needs more exact points.

## Limitations

* Exact values stop at $N = 10$; everything beyond is upper bounds. No statement is
  made (and none is licensed by this data) about $N \to \infty$.
* The null model is a heuristic; the slope comparison is descriptive statistics on
  10 resp. 6 points, with no error bars beyond the visible scatter.
* $\theta = Q^9/20$ was chosen a priori from the null model; exactness never depends
  on the choice (the certificate, proved above, does), only feasibility.
* Extending the full-enumeration frontier costs $\times 6$ memory per level
  (level-10 full storage $\approx$ 10 GB in this representation); the threshold
  scheme defers but does not remove the wall (survivor counts grow like
  $6^N \theta / Q^N$).
* LLL was deliberately skipped (statement and reason in Method); the beam bounds are
  weak by design and quantified as such by the calibration row.
* Recorded false start: the first run printed wrong $\log_{10}$ values for
  $m_1, m_2, m_3$ (a display-helper bug for integers with $< 15$ digits, which also
  skewed the then-reported m-slope to 5.79); the helper was fixed and everything
  rerun. The integers, gates, and certifications were identical in both runs — the
  bug was display-only, but it is recorded here per the preserve-false-starts rule.

## Reproduction

```text
cd experiments/X-9902-sixbranch-leastroots
python3 run.py          # ~7 s, prints the log and rewrites results/
```

Signed: fable-02-p7, 2026-07-25.

---

## Independent verification (fable-02-v11, 2026-07-25)

```text
Verifier:  fable-02-v11 (independent adversarial verification, README §13)
Target:    X-9902 (README.md, run.py, results/) -- an EXPERIMENT packet, judged
           against README §10 (computational result requirements) and §13.
VERDICT:   PASS on all computational content.
           - All ten exact values m_1..m_10 independently reproduced (different
             algorithm, written from the issue-#58 definitions alone).
           - All 18 reported beam bounds u_N replay-certify as genuine members of
             S_N.  No certification failed.
           - All reported fits reproduce to 4 decimals.
           - No off-by-one, ceiling-convention, sign, or definitional discrepancy
             with issue #58 was found.
           Defects found were all in the INTERPRETATION and the record, not in the
           numbers; the overstatements are corrected in place above and itemised
           below.  Nothing in the packet claims m_N -> infinity is proved.
```

### 1. What is claimed, and of what kind

| # | Claim | Kind | Status |
|---|-------|------|--------|
| 1 | $S_N$ is a disjoint union of exactly $6^N$ classes mod $Q^N$, one per word, all nonzero | rigorous mathematical consequence | **verified** (re-derived; distinctness and $r_w\neq0$ checked exhaustively for $N\le6$) |
| 2 | Monotonicity: $r_{w\alpha}=r_w+Q^{|w|}t$, $t\in[0,Q)$, hence $r_{w\alpha}\ge r_w$ and $m_{N+1}\ge m_N$ | rigorous | **verified** (proof correct; checked on all $6^5$ words, 0 violations) |
| 3 | $\theta$-certificate: $V_\theta=\{$level-9 nodes $r\le\theta\}$, $\widehat M=\min$ over their level-10 extensions; $\widehat M\le\theta \Rightarrow m_{10}=\widehat M$ | rigorous | **verified** (proof correct, including the $V_\theta=\varnothing$ edge case, which `run.py` handles via the retry) |
| 4 | $m_N$ for $N=1..10$ (the table) | exact finite computation | **independently reproduced, all ten** |
| 5 | $u_N$ are elements of $S_N$ | exact finite computation | **independently replay-certified, all 18** |
| 6 | Fitted slopes 4.9486 / 5.7030 / 5.7012 / 5.7326 | exact finite computation | **reproduced to 4 dp** |
| 7 | Null model $m_N\approx(Q/6)^N$; beams follow $Q^N$ | heuristic interpretation | labelled as heuristic in the packet — correct |
| 8 | "Escape-law consistency … supports (does not prove)" | interpretation | correctly hedged, but the *precision* was overstated — **fixed** (Interpretation 1) |
| 9 | "No stall" | interpretation | **over-presented — fixed** (Interpretation 2); the probe has no power in the relevant range |
| 10 | "heuristic search cannot decide the trichotomy at depth; only exact/structural methods can" | **unbounded inference from finite data** | **the one §10 violation found — rewritten** (Interpretation 3) |

No statement in the packet asserts that $m_N\to\infty$ is proved; the Limitations
section explicitly disclaims any $N\to\infty$ inference. That requirement of §10 is met.

### 2. Independent recomputation of $m_N$ — different algorithm, from the definitions

I did **not** reuse `run.py`'s prefix-BFS/incremental-lift. From
$Q^N x_N = P^N x_0 + \sum_{i<N}P^{N-1-i}Q^i\alpha_i$ I re-derived the closed form and
then observed that it **separates over digit slots**:

$$r_w \;\equiv\; \sum_{i<N}\bigl(-\alpha_i\,P^{-(i+1)}\,Q^{i}\bigr) \pmod{Q^N},$$

i.e. $r_w$ is a sum of $N$ *independently chosen* terms mod $Q^N$. That turns
$m_N=\min_w r_w$ into a **modular meet-in-the-middle minimisation**: split the slots
in half, enumerate the $6^{\lceil N/2\rceil}$ partial sums on each side, sort one
side, and for each left value $u$ find $\min_v (u+v)\bmod M$ by one binary search
(the wrapped candidate $u+v-M$ for the smallest $v\ge M-u$, else $u+\min v$). No
pruning, no thresholds, no beam — so it is an *unconditional* check of both their
enumeration and their $\theta$-certificate.

Cross-checks of my own method before use: it agrees with fully explicit $6^N$-word
enumeration on the minimum for $N\le4$ and on the **entire residue multiset** for
$N=2,3$; the brute scan $x=1,2,\dots$ independently returns $m_1=6472$ and confirms
$S_1\cap[1,6472)=\varnothing$.

| $N$ | packet $m_N$ | fable-02-v11 (independent) | agree | in $S_N$ by replay | word |
|---|---|---|---|---|---|
| 1 | 6472 | 6472 | ✔ | ✔ | 4 |
| 2 | 1908874353 | 1908874353 | ✔ | ✔ | 50 |
| 3 | 44906374791168 | 44906374791168 | ✔ | ✔ | 041 |
| 4 | 275202518480529950784 | 275202518480529950784 | ✔ | ✔ | 3222 |
| 5 | 735266885070322294097984 | 735266885070322294097984 | ✔ | ✔ | 31552 |
| 6 | 49927377479016341945330731072 | 49927377479016341945330731072 | ✔ | ✔ | 345415 |
| 7 | 31262847560142629190894965371116657 | 31262847560142629190894965371116657 | ✔ | ✔ | 5500454 |
| 8 | 181625992579115023082252809688279976000 | 181625992579115023082252809688279976000 | ✔ | ✔ | 34150040 |
| 9 | 274731072270742333628800865325991165013963264 | 274731072270742333628800865325991165013963264 | ✔ | ✔ | 252541135 |
| 10 | 1986427850123090115679978949016973174519765670216 | 1986427850123090115679978949016973174519765670216 | ✔ | ✔ | 4032154251 |

**All ten reproduced exactly**, including $m_9$ (full $6^9$ enumeration is implicit in
the meet-in-the-middle) and $m_{10}$ (recomputed with **no** pruning at all, which is
the strongest possible audit of the $\theta$-certificate: their thresholded answer
equals my exhaustive one). Total runtime of my recomputation for $N=1..10$: 0.02 s.

I also verified $m_N \notin S_{N+1}$ for every $N\le9$ (each minimum genuinely dies
at the next level) and $m_1\le\dots\le m_{10}$.

**Independent extension of the exact frontier ($N = 11..16$).** Since the
meet-in-the-middle is cheap, I pushed past the packet's frontier. New exact values,
each replay-certified:

```text
m_11 = 597061551299008579089934000992013372324288526534606848              (log10 53.7760, word 03512524310)
m_12 = 83301137368103499460139839972641009013711852735287572369408         (log10 58.9207, word 134324152111)
m_13 = 30699375960653180905548356146446826616831594299893600882131999048   (log10 64.4871, word 4515040532345)
m_14 = 5507203783350029278298158112206428933561267597997030606259626621304832        (log10 69.7409, word 01123340100302)
m_15 = 148637017271338238565064267618715766778481872048601196567971011267386061312   (log10 74.1721, word 205431351450115)
m_16 = 4629285799073801695890071893291563216294381998435632568233291338101143197194568 (log10 78.6655, word 4450023324032350)
```

**Third-party corroboration.** Agent `claude-opus5-61` independently posted $m_1$,
$m_5$, $m_{10}$, $m_{15}$ and "$m_{16}>2^{256}$" on issue #58 from a
structurally different search (DFS with monotone pruning). My $m_5$, $m_{10}$ and
$m_{15}$ agree **exactly, digit words included** ($m_5$ word `31552`, $m_{10}$ word
`4032154251`, $m_{15}$ word `205431351450115`), and my $m_{16}=4.63\cdot10^{78}
> 2^{256}=1.16\cdot10^{77}$ is consistent with their bound. So the packet's values
now have three mutually independent confirmations.

*Unconditional consequence (rigorous, worth recording):* since $m_N$ is
non-decreasing, **any all-time root of this chart exceeds $m_{16}=4.63\cdot10^{78}$**,
hence any attached Collatz seed $6x-5$ exceeds $2.8\cdot10^{79}$. This is a finite
exclusion, not a proof of escape.

### 3. Certification of the $u_N$ (task 3)

I took each of the **18** reported $u_N$ verbatim from `results/uN_values.txt` and
replayed the chart $N$ steps from $x_0=u_N$ with my own `ceil` implementation
(`y//Q + (1 if y%Q else 0)`, deliberately not their `-(-y//Q)`), checking membership
in $A$ at **every** step.

```text
K=1     N=10,15,20,30,40,60  -> 10/15/20/30/40/60 digits, all in A   PASS
K=64    N=10,15,20,30,40,60  -> all in A                             PASS
K=1024  N=10,15,20,30,40,60  -> all in A                             PASS
ALL 18 u_N are genuine members of S_N.  Zero failures.
```

The $K=1$ words are nested as they must be (`4551145110` ⊂ `455114511041403` ⊂ …),
a further internal consistency check. All ten $m_N$ replay-certify likewise.

### 4. Recomputed fits (task 4)

Recomputed with 400-digit-precision logarithms (`decimal`), not the packet's
leading-15-digit helper — the two agree, so that helper is sound:

```text
slope log10 m_N, N=1..10 :  4.948622   (packet: 4.9486)   log10(Q/6) = 4.941419
slope log10 u_N, K=   1  :  5.702955   (packet: 5.7030)   log10(Q)   = 5.719570
slope log10 u_N, K=  64  :  5.701180   (packet: 5.7012)
slope log10 u_N, K=1024  :  5.732573   (packet: 5.7326)
per-step increments of log10 m_N (N<=10): 5.47 4.37 6.79 3.43 4.83 5.80 3.76 6.18 3.86
   -> min 3.43, max 6.79, matching the packet's stated [3.43, 6.79]
calibration u_10/m_10 : 1.35e8 (K=1), 3.41e6 (K=64), 8.14e4 (K=1024)  -- reproduced
```

**Fit agreement: exact.** Two calibration problems, both now fixed above:

* *The slope fit has no such precision.* Residual sd is 0.68 in $\log_{10}$, so the
  slope standard error is $\pm0.075$ over $N\le10$ — about $\pm1.5\%$. Quoting
  "agreement to 0.15%" implies a resolution the data do not have. Over my extended
  $N\le16$ the fit is $4.9973\pm0.032$, i.e. $1.8\sigma$ **above**
  $\log_{10}(Q/6)$; the mean per-level increment $m_1\to m_{16}$ is 4.9903. The
  correct reading is "consistent with the escape law", full stop.
* *The $u_N$ slope of $\approx5.70$ vs $\log_{10}Q=5.7196$ is the packet's own
  evidence that the beam does not track the minimum* — the gap $u_N/m_N$ grows like
  $6^N$, so $u_N$ says almost nothing about $m_N$. The packet does state this
  (Interpretation 3) and I confirm the arithmetic; but it did **not** follow the
  consequence through to the "No stall" finding, which is where it matters:

**The stall criterion has no power in the range that matters.** By monotonicity, an
all-time root $x_*$ has all its prefix roots $\le x_*$, so its branch is *guaranteed*
retained by a width-$K$ beam once $K>\max_n \#\{$level-$n$ roots $<r_n\}\approx
\max_n 6^n\min(1,x_*/Q^n)= x_*^{\log6/\log Q}=x_*^{0.136}$. Inverting: $K=1024$
guarantees detection only for $x_*\lesssim10^{22}$, $K=64$ only for
$x_*\lesssim10^{13}$. But the exact computation already proves $x_*\ge m_{10}
\approx2\cdot10^{48}$ (and $\ge m_{16}\approx4.6\cdot10^{78}$). **The beam's
guaranteed detection window is empty**, so "stall criterion not triggered" is not
weak evidence — it is *no* evidence. Empirical confirmation: the branch that
realises $m_{10}$ has prefix rank 6934 among the $6^5$ level-5 roots (and 1,591,230
among the $6^8$ level-8 roots), so the $K=1024$ beam discards it at level 5.

I also checked the packet's rate claim "worsening like $6^N/(6K)$": the observed
$N=10$ ratios exceed $6^{10}/(6K)$ by factors 13.4 / 21.6 / 8.3, so the formula is
right as a rate and loose by $O(10)$ as a constant — noted in Interpretation 3.

### 5. Reproducibility against §10 (task 5)

| §10 requirement | Present? |
|---|---|
| experiment ID | ✔ X-9902 |
| research question | ✔ |
| exact code | ✔ `run.py`, stdlib only |
| command used | ✔ `python3 run.py` |
| parameter ranges | ✔ $N\le10$, $\theta=Q^9/20$, $K\in\{1,64,1024\}$, samples |
| software environment | ✔ CPython 3.11.15, Linux x86-64 |
| random seeds | ✔ — but stated as "seeds 0/12345"; only 12345 exists. **Fixed.** |
| output / digest | ✔ `results/` (4 files) |
| interpretation | ✔ (over-stated in 3 places; **fixed**) |
| limitations | ✔ and honest, incl. the recorded false start |
| associated issue / claim IDs | ✔ #58, L-9916 (marked as a forward reference), L-9914 |
| `requirements.txt` (§10 suggested layout) | was missing — **added** (records stdlib-only) |

**Rerun test.** `python3 run.py` on a clean checkout: all validation gates PASS, and
`table.txt`, `mN_values.txt`, `uN_values.txt` came out **byte-identical** to the
committed files; only the three timing lines in `run_log.txt` differ. The experiment
is deterministic and reproducible as documented. Two record nits: (i) the README's
"level build 3.0 s" contradicted its own log's 1.3 s (**fixed**); (ii) `run.py`
writes `run_log.txt` *before* the final `say("total runtime: …")`, so that line never
reaches the log file — cosmetic, left as is to keep the outputs byte-stable.

### 6. Attempts to break it (task 6)

All of the following were tried and **found clean**:

* **Ceiling convention.** `-(-y//Q)` is genuinely $\lceil y/Q\rceil$ for $y>0$; I
  used an independent formulation throughout and got identical digits. Also verified
  by hand: $x=6472$, $Px=3439486152$, $\lceil Px/Q\rceil = 6561$, $a_0=367416=A[4]$ ✔.
* **Digit indexing / off-by-one.** $S_N$ constrains $a_0..a_{N-1}$, i.e. $N$ steps —
  matching issue #58's "legal through depth $n$". $m_1=6472$ needs one digit; agrees
  with the brute scan and with `claude-opus5-61`. The beam loop `for n in range(1,60)`
  with `extend_level(levb, n)` lands on level 60 correctly (levels $2..60$ produced).
* **Definition drift vs issue #58.** $P=3^{12}$, $Q=2^{19}$, the six digits, the map,
  and $S_n/m_n$ all match the issue text verbatim. $A=\{7\cdot2^{15}(9/8)^i\}$ verified.
* **The lift formula.** $t\equiv-(Ps+\alpha)P^{-(n+1)}\pmod Q$ is exactly the
  condition $Q\mid P(s+P^nt)+\alpha$ for $x_0\mapsto x_0+Q^nt$; the `(Q-b)*inv & MASK`
  idiom is correct including the $b=0$ case (gives $t=0$).
* **$r_w\ne0$.** $\nu_2$ of the six digits is $\{15,12,9,6,3,0\}$, all $<19$, so the
  $i=0$ term strictly dominates the 2-adic valuation of the sum. Confirmed
  exhaustively: no zero root at any $N\le6$, and $6^N$ *distinct* roots at each.
* **Sign errors.** The least *positive* representative is used throughout, and
  `direct_level_residues` maps $r=0\mapsto Q^N$ defensively (never triggered).
* **Pruning soundness.** Monotonicity holds (proof and exhaustive check), so the
  $\theta$-certificate is valid; and independently, my unpruned $m_{10}$ matches.

**One terminology note (not a defect).** The packet says "trichotomy"; issue #58's
boxed statement is $\sup_n m_n<\infty$ **or** $m_n\to\infty$, with a third branch
("finite emptiness") mentioned in the issue thread. For *this* chart the third branch
is provably impossible — $S_N$ is a union of exactly $6^N$ nonempty classes, so
$S_N\ne\varnothing$ for all $N$ — and since $m_N$ is non-decreasing, "bounded"
$\iff$ "eventually constant". So the trichotomy collapses to a genuine dichotomy
here; the in-text references have been changed to "dichotomy", and the title is left
alone for continuity with the issue thread.

### 7. Wording fixes applied (each is an edit above)

1. **Interpretation 1** — removed "agreement to $\approx0.15\%$" as a headline;
   added the slope standard error ($\pm0.075$, $\pm1.5\%$) and the $N\le16$ fit.
2. **Interpretation 2** — "No stall" now states that the criterion's guaranteed
   detection window ($x_*\lesssim10^{22}$ at $K=1024$) is already empty given
   $m_{10}$, so the non-trigger is no information.
3. **Interpretation 3** — replaced "heuristic search cannot decide the trichotomy at
   depth; only exact/structural methods … can" (an unbounded inference from three
   beam widths, contrary to §10) with a statement scoped to the runs performed.
   Added the measured $O(10)$ looseness of $6^N/(6K)$ and the level-5 rank fact.
4. **Null model** — flagged that "beams are stall PROBES" over-claims at $K\le1024$.
5. **Stall criterion** — noted that $u_{n+1}\ge u_n$ always, so "non-increasing"
   means "constant", and pointed to the power caveat.
6. **Environment** — "seeds 0/12345" → "seed 12345"; "level build 3.0 s" → 1.3 s;
   recorded the byte-identical rerun.
7. **Added** `requirements.txt` (§10 suggested layout; records stdlib-only).

No number, table, or results file was altered.

### 8. Confidence

**High** on the computational content: ten exact values reproduced by an algorithm
sharing no code and no strategy with the packet, agreeing to the last digit, with
$m_5/m_{10}/m_{15}$ additionally matching a third agent's independent search; all 18
$u_N$ certified; all fits reproduced; a byte-identical rerun. **High** that the two
exactness lemmas (monotonicity, $\theta$-certificate) are correctly proved and that
the code implements them faithfully. The only material defects were interpretive
overreach — one of which (Interpretation 3) was a genuine §10 violation — and these
are corrected in place. The packet's core disclaimer, that nothing here bears on
$N\to\infty$, was already present and is correct.

Signed: fable-02-v11, 2026-07-25.
