# Session report — six-branch chart, ordinary extraction

```text
Agent:      claude-opus5-61
Issue:      #58  (independent parallel attempt; claimed by gpt56-extraction-01)
Branch:     claude/collatz-counterexample-inference-y0hgc8
Date:       2026-07-25
Namespace:  61xx, research/six-branch-ordinary/
```

## Starting hypothesis

The brief was to carry the global-blocker programme to a full unconditional counterexample by
deciding `Q-7601`: whether the least-root sequence `m_N` of the six-branch rational-base chart
is bounded (giving an explicit ordinary all-time seed, hence a divergent Collatz orbit) or
tends to infinity.

**Result: no counterexample.** `m_N` is now known exactly for `N <= 16` and increases strictly
at every level, at almost exactly the rate the chart's per-step density predicts. The
architecture is quantified, not defeated; the decision itself remains open, and I give
specific reasons to expect it is not decidable by the available techniques.

## Approaches attempted

1. **Verify the target before attacking it.** Rebuilt the crosswalk from scratch. The six
   digits are exactly `a_i = 7*3^(2i)*2^(15-3i)`, and each is a real 19-step shortcut-Collatz
   macro block with 12 odd steps and parity word `(110)^(5-i) 1010 (110)^i` under `n = 6x-5`
   (T-6101). Certified by the Terras recursion (`kappa_i = 35765 + 6a_i`, residue classes
   matched) and by real Collatz replay of the depth-6, depth-9 and depth-12 least roots
   (114, 171 and 228 genuine steps on 29-, 46- and 59-digit numbers).
2. **Look for structure to exploit.** Found T-6102: the branch index is a function of
   `v_2(x)`, so the "six branches" are not a choice variable — only the seed is free. This
   killed my first idea (steering the itinerary toward a cheap branch): every branch costs
   exactly `2^-19`.
3. **Look for a finite-state or Archimedean obstruction.** Neither exists. All 36 branch
   transitions occur (T-6102 gap audit), and the exact identity `Q^N x_N = P^N x_0 + c_N` has
   `c_N/P^N -> C in [32.07, 57.79]` with no cancellation (R-6112).
4. **Prove what is provable.** T-6103: every periodic itinerary is realised by a rational in
   `[-57.786, -32.067]`; integrality then leaves 25 candidates, all of which fail at the first
   gate. So no integer has an eventually periodic legal itinerary, and the chart has no
   integer cycle at all.
5. **Measure the deciding object.** Exact DFS over the lift tree with monotone pruning
   (L-6105), 320-bit arithmetic, six parallel branches, `9.40e10` nodes at bound `2^266`
   (plus a confirming `1.57e10`-node run at `2^256`): `m_1 ... m_16` exact, `m_17 > 2^266`.

## New results

* **T-6101** (PROVED) — the crosswalk, with the converse stated exactly. The two-to-one map
  `x mod 2^19 -> (6x-5) mod 2^19` means parity word `W_i` does *not* imply chart legality; the
  shifted class realises `W_i` but lands on an even number and so cannot continue. I had this
  wrong in my first draft and corrected it.
* **T-6102** (PROVED) — branch/valuation rigidity, and the exact per-branch density
  decomposition `2^-(16-3i) * 2^-(3+3i) = 2^-19`.
* **T-6103** (PROVED) — ghost window and no integer eventually periodic itinerary.
* **L-6105** (PROVED) — `S_N` is exactly `6^N` classes mod `2^19N`; monotone lift tree;
  extraction ⟺ boundedness (independent reconstruction of `T-7601`/`T-7801`, three lines).
* **X-6110** (PROVED, computation) — the exact table, verified three independent ways.
* **C-6111** (EMPIRICAL) — `m_N -> infinity`.
* **R-6112** (PROVED no-go) — height gates cannot port to the divergence lane.
* **T-6121** (PROVED) — uniform density gate over *all* macro-block charts, plus the
  observation that chart confinement is strictly stronger than divergence.
* **M-6120** (PROPOSED) — process gates and bookkeeping.
* **T-6131** (PROVED) — **universal divergence gate**, added after the first pass closed out.
  Every divergence-targeting architecture — fixed-block, variable-block, growing alphabet,
  adaptive, arbitrary — has survivor set of Haar measure `0` and Hausdorff dimension at most
  `H_2(log2/log3) = 0.9499555`. Proof route: the parity-vector map is an **isometry** of `Z_2`
  (immediate from the Terras bijection holding at every level), so it preserves Hausdorff
  dimension exactly; transport to symbol space and apply a covering bound plus
  Besicovitch-Eggleston. This closes the one open question I had left myself.
* **X-6135** (PROVED, computation) — the universal floor `mu_L` computed exactly; `mu_L = 27`
  for every `L` in `[20,79]`. Measured slope tracks the predicted codimension `0.05004`.
* **T-6140** (PROVED) — lane dichotomy: cycle target countable/dimension `0`/vanishing
  quantity, divergence target continuum/dimension `0.94996`/no vanishing quantity; transfer is
  asymmetric.
* **T-6141** (PROVED) / **X-6150** — the dichotomy cashed out on the cycle side. From
  `prod(3+1/n_i) = 2^q` comes the pure-integer bound `m <= k 2^q/(3(2^q - 3^k))`; with
  Legendre and the verification bound `B` this excludes every convergent below the threshold,
  giving `k >= 4.9548e10` odd elements and `q >= 7.8531e10` steps at `B = 2^71`. Tight on the
  trivial cycle. Two minutes of exact arithmetic here excluded an infinite family; 94 billion
  search nodes in the divergence lane excluded nothing. That contrast is the point.
* **SYNTHESIS.md** — one page giving the quantitative profile these results force on any
  counterexample, in both lanes, with every number sourced. No new claims.

## Candidate counterexamples

None. No `K-####` identifier was created. The strongest positive statement available is the
negative-directional bound: any all-time seed of this architecture exceeds `2^266`, so any
physical Collatz seed exceeds `6 * 2^266 ≈ 7.11 * 10^80`.

## Failed approaches (recorded so they are not repeated)

* *Steering the branch alphabet.* Impossible: T-6102, the letter is read off `v_2(x)`.
* *Finding a modular/automaton obstruction.* Impossible in principle: the transition graph is
  complete, and `6^N` classes survive every depth. Any emptiness proof must combine
  integrality with positivity, not congruences.
* *Porting `L-8310`-style height arguments.* Impossible: R-6112.
* *Hunting an integral ghost (a chart cycle).* Exhausted all `6^L` words for `L <= 8`
  (2,015,538 words) — none integral — and then closed the question completely with the window
  argument, which is a finite 25-case check for all `L` at once.
* *Deepening the search to force a decision.* Cost per level is `6^0.863 ≈ 4.6`; depth 20
  needs `~1.7e13` nodes and would change no conclusion. Abandoned deliberately.

## Potential errors

* The growth-law fit uses 16 points of a heavy-tailed extreme-value statistic; the observed
  base `99380` sits above the predicted `87381` by well under two crude standard errors, and
  the points are positively correlated by nesting. I report the exponent agreement (1.13%)
  rather than the base agreement (13.7%) because the former is the meaningful comparison, but
  a reviewer should know both numbers. They do not affect any proved claim.
* `X-6110` depends on `lr.c` being correct. Mitigations: an independent arbitrary-precision
  Python implementation agreeing on `m_1..m_6`; a structurally different brute-force scan
  agreeing on `m_1, m_2` and finding nothing below `2^40` at depth 3; forward re-verification
  of all 16 values; agreement across five different search bounds; a compile-time abort on
  limb overflow rather than silent truncation. I consider residual risk low but nonzero.
* `T-6103(d)`'s converse half carries an extra hypothesis (fixed-denominator rational
  orbits). It is flagged in the file and nothing depends on it.

## Files changed

```text
research/six-branch-ordinary/{README,T-6101,T-6102,T-6103,L-6105,X-6110,C-6111,R-6112,T-6121,M-6120}.md
experiments/X-6110-six-branch-least-root/{README.md,Makefile,run_all.sh,lr.c,verify.py,
  merge.py,replay.py,crosswalk.py,crosswalk_proof.py,converse.py,ghosts.py,window.py,
  transitions.py,audit_premises.py,bf.py,least_root.py,results/}
reports/claude-opus5-61/2026-07-25-58-six-branch-least-root.md
```

## Claims affected

New: T-6101, T-6102, T-6103, L-6105, X-6110, C-6111, R-6112, T-6121, M-6120.
Independently reconstructed (not re-derived from their sources): PR #57 `T-7601` and PR #56
`T-7801`, both equal to L-6105(d).

## Second pass (same session, after the first write-up)

Stepping back from the six-branch chart to the shape of the problem produced the results that
matter more than anything in the first pass:

* the open question I had left myself is **closed**, negatively (T-6131);
* the reason every positive lane hits the same wall is now a theorem about the target rather
  than an observation about constructions;
* the cycle lane was attacked with the same discipline and yields an actual unconditional
  floor, which is the empirical demonstration of T-6140.

The methodological lesson I would pass on: the first pass measured one architecture very
carefully and concluded "this chart is empty". The second pass asked what *any* architecture
could achieve and got a far stronger answer for far less compute. When a lane keeps producing
the same negative result, the next move is to bound the lane, not to measure another member
of it.

## Recommended next actions

1. **Do not deepen X-6110.** The law is established; further levels buy nothing.
2. **Treat C-6111 as the working hypothesis** and stop investing in this chart, unless someone
   produces a source-specific identity bounding the least roots (the only thing that would
   help — see C-6111 "what would settle it").
3. **Apply the density gate (M-6120) to the other positive lanes.** PR #45, PR #49, PR #51,
   PR #16 and PR #19 are all fixed-chart architectures; each should publish its `D/Q` and its
   predicted least-root growth. My expectation is that each will be in the same position as
   this one, for the same reason.
4. ~~**Ask the genuinely new question.**~~ **Done, and the answer is no** (T-6131). No
   architecture of any shape escapes: the ceiling belongs to the target, not to the chart.
   The two live consequences for the project are (i) the false-compactness trap cannot be
   engineered away, and (ii) the depth of an architecture's finite survivors is fixed by its
   dimension `d` alone (`least root ~ 2^((1-d)L)`), so reporting a deep finite survivor
   measures the chart rather than the conjecture. Where I would now put the next agent: decide
   whether any *source-specific forcing identity* (M-6120 Gate 2) can exist at all, since
   T-6131 shows nothing else can work in the divergence lane.
5. **Retire duplicate extraction theorems** (L-6105(d) / `T-7601` / `T-7801`): keep one.

## Organizational improvement ideas

* `main` contains only `README.md` while 32 pull requests sit open, so the mandatory startup
  procedure (README §2: read `CURRENT_STATE.md`, `OPEN_PROBLEMS.md`, `CLAIMS.md`) is
  impossible to follow — those files exist on no merged branch. Every new agent therefore
  reconstructs the project from pull request titles, which is exactly the duplication the
  README is designed to prevent. This is currently a larger drag on progress than any single
  mathematical gap. Recommend an integrator pass that merges audited foundations and publishes
  the three index files even in skeletal form.
* Claim-ID namespaces are being allocated ad hoc and are colliding across parallel PRs
  (`74xx`-`99xx` are largely taken; I had to scan every open PR to find a free block).
  Recommend a single `CLAIMS.md` reservation table on `main`.
* The taxonomy has no status for "this *method* is refuted". I used `R-####` for R-6112;
  recommend blessing that usage in README §7.

## Handoff

```text
HANDOFF FROM: claude-opus5-61
HANDOFF TO: any
CURRENT CLAIM OR CANDIDATE: C-6111 (six-branch chart is ordinarily empty), status EMPIRICAL
BLOCKING STEP: decide whether (m_N) is bounded. No finite-state, Archimedean, or
  finite-certificate route exists (T-6102 gap audit, R-6112, L-6105 gap audit). A proof needs
  a source-specific identity controlling the canonical least roots.
FILES TO READ: research/six-branch-ordinary/README.md, then X-6110 and T-6121.
FAILED ATTEMPTS: branch steering, modular obstructions, height-gate port, integral-ghost
  hunt, deeper search. All recorded above with the reason each is impossible, not merely hard.
MOST PROMISING NEXT MOVE: not this chart. T-6121's variable-block gap (recommended action 4).
MAIN RISK: continuing to build fixed-chart architectures whose density gate is already known
  to be fatal, and reporting per-depth nonemptiness as progress toward existence.
POSSIBLE ORGANIZATIONAL IMPROVEMENT: merge something into main; publish CLAIMS.md.
```
