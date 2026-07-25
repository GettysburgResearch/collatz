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
$\log_{10} Q = 5.7196$ — beams are stall PROBES, not minimum trackers.

## Stall criterion (stated up front)

A *seed signal* = $u_N$ non-increasing over 3 consecutive sampled $N$ (per beam
width). If triggered, run.py dumps the word prefix and residue for follow-up, and no
claim beyond the data is made. **Outcome: not triggered** (see results).

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
  integer arithmetic; `random` used only to choose validation samples, fixed seeds
  0/12345 — no reported number depends on randomness; beams deterministic).
* Command: `python3 run.py` (writes `results/` and prints the log).
* Environment: CPython 3.11.15, Linux x86-64. Runtime: **6.4 s** total (level build
  3.0 s; 8→9 stream + m_10 phase 4.8 s cumulative; beams 0.3 s).
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
   fitted slope $4.9486$, against the null-model slope $\log_{10}(Q/6) = 4.9414$ —
   agreement to $\approx 0.15\%$, with per-step increments scattering in
   $[3.43, 6.79]$ exactly as a min-of-exponentials null predicts. Within $N \le 10$,
   the data are fully consistent with the escape law $m_N \approx (Q/6)^N$ and show
   **no** anomalous small-root family. This supports (does not prove) the escape
   branch of issue #58's trichotomy for this chart.
2. **No stall.** The stall criterion was not triggered at any beam width; every
   sampled $u_N$ grows by $\ge 10^{27}$ between consecutive samples.
3. **Beams cannot see the minimum.** Beam slopes ($5.70$–$5.73$) track
   $\log_{10} Q = 5.7196$, not $\log_{10}(Q/6)$, and the calibration row shows the
   $N = 10$ beam bound is already $10^{5}$–$10^{8}$ above the true $m_{10}$,
   worsening like $6^N/(6K)$. Consequence for L-9916: heuristic search cannot decide
   the trichotomy at depth; only exact/structural methods (like the threshold scheme
   used here, or genuine lattice reduction with a soundness proof) can.
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
