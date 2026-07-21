# Session report: Fiber Ladder session 1 (packets P5–P8)

```
Agent:    claude-01
Issue:    #4
Branch:   claude/collatz-migration-math-osr370
Date:     2026-07-21 (second session of the day; follows the
          migration/bootstrap report)
```

## Starting hypothesis

The PR #3 branch's collision-fiber discoveries (independently
re-verified by me before use: all three new chart identities exact to
q = 10¹⁸+7) are sparse-alphabet instances of this program's
digit-transfer framework. Working hypotheses for the session:
(a) the run-length skeleton admits a rigidity theorem in the style of
T-0013; (b) the survivor law holds at every chart rung (tripwire for
the opposite); (c) chart transitions don't change relay economics;
(d) fiber widths grow and the growth is quantifiable.

## Approaches attempted and new results

**P5 — Skeleton rigidity (T-0020, PROPOSED; `SKELETON.md`).** Proved:
no infinite skeleton chain of a nontrivial induced orbit is generated
by a finite cyclic exp-poly schema family (affine exponent schedules,
arbitrary real cofactor ratios), except bounded-state chains =
eventually periodic itineraries, which are excluded. The proof is
four steps: telescoping `V_{k+1} = (N/M)^{u_{k+1}}(V_k + δ_k)`;
`V → ∞` for nontrivial orbits; affine exponent growth contradicts the
finite dominant ratio of an exp-poly; and — the load-bearing step —
integrality of the cofactors plus **Fatou's lemma** (integer-series
poles have algebraic-integer reciprocals) forbids the forced growth
ratio `(N/M)^U`, a rational non-integer. Consequence: the skeleton
search space is provably S-adic or nothing — Pisot-substitution
schemas die too. **Dead end recorded**: my first draft closed the
bounded-`u` case by composing leading-coefficient identities around
the schema cycle; that argument was wrong (the composed identity is
consistent) and was replaced by the Fatou argument, which is stronger
(no smoothness hypothesis needed). External imports flagged for P1:
Fatou, Kronecker's criterion.
Computational companion (X-0025): skeleton normal form verified on
1021 chain links across all four charts; periodic-chain search over
636,350 patterns (p ≤ 3, u ≤ 5): **zero integral chains of any
sign** (L-0015).

**P6 — EQ ladder (O-0009, EMPIRICAL; `eq_ladder.py`).** The coded
sets `R_K` instantiate at every rung (coding verified functionally;
`|R_K| = |D|^K` exact everywhere). Survivor law min ≍ M^K/|D|^K holds
at all four rungs; ratio bands: [0.19, 1.9] (64→81, K ≤ 16 — matches
the migrated program's K ≤ 20 band), [0.048, 2.65] (512→729, K ≤ 13),
[0.36, 3.78] (2¹⁷, K ≤ 7), [0.46, 2.46] (2²², K ≤ 5). The single
0.048 cell (K = 11) is a ~5% lower-tail event under the exponential
min-statistic; K = 12 (0.117) and K = 13 (0.428) return to band —
fluctuation, not drift. **The tripwire did not fire**: no bending of
equidistribution as density → log₃2 anywhere on the ladder.

**P7 — Bridge economics (T-0021, PROPOSED; `chart_bridges.py`).**
Upgraded from measurement to theorem mid-session: free parity words
leaving any chart exit lattice are *exactly* uniform (the lattice map
is odd-multiplier, so the Terras bijection applies verbatim) — the
measured supercritical fraction equals the binomial null to the last
digit (0.10506, all four charts, j = 16), and that equality is
forced. With the convexity bound on relay cycles: **the chart
groupoid adds reachability, never economy.** All four single-fiber
rungs cost ≥ 0.81 bits/step vs the pooled-atlas floor 0.05004.

**P8 — Fiber widths (O-0010, R-0003, C-0003; `fiber_widths.py`).**
Independent implementation of the coalescence recursion:
reproduces PR #3's width table (2, 3, 4, 5, 8, 12, 18 at L = 6…22)
exactly; **new records: width 26 at L = 25**; `|D_L|` agrees with the
committed atlas-spectrum values at every overlapping L (16–26) —
three independent algorithms now concur on the atlas. The uniform-hash
model predicts logarithmic max width; observed growth is exponential,
slope log₂(width)/L ≈ 0.19 and slowly rising → R-0003 (model
refuted), C-0003 (growth conjecture, EMPIRICAL). **Dead end
recorded**: the natural super-multiplicativity proof of unbounded
widths fails at the carry offset (composed residues share odd-count
but split value); documented precisely in `LADDER.md` §3.

**Synthesis (`LADDER.md` §4).** Single-fiber cost = 1 − width-slope ≈
0.81 bits/step; transitions are free but never profitable (T-0021);
pooling all fibers per level is exactly the atlas hierarchy, floored
at 0.05004 by T-0014. The offense frontier is sharply localized:
either the width law breaks somewhere (C-0003 failing upward — then
find the level), or S-adic schedules through pooled atlases are the
only surviving certificate format, consistent with T-0013, T-0020,
T-0003/T3, T4.

## Candidate counterexamples

None. No K-#### entries created.

## Failed approaches (recorded)

1. Leading-coefficient cycle composition for Step 6 of T-0020 (wrong;
   replaced by Fatou — see `SKELETON.md` Remark 2).
2. Width super-multiplicativity by fiber composition (carry-offset
   obstruction — see `LADDER.md` §3).

## Potential errors / open scrutiny points

* T-0020 Step 4 leans on Fatou's lemma and Kronecker's criterion —
  standard but imported; P1 must verify the citations, and an
  independent reviewer should check the "λ must be a ratio of E_i"
  dominance step and the o(1) absorption in Step 3.
* The ~5%-tail explanation of the 0.048 cell assumes the exponential
  min-statistic model; a reviewer may want the exact order-statistic
  computation.
* C-0003's constant 0.19 is empirical only; no model derives it yet.

## Files changed

Added: `SKELETON.md`, `LADDER.md`, `experiments/skeleton_rigidity.py`,
`experiments/eq_ladder.py`, `experiments/chart_bridges.py`,
`experiments/fiber_widths.py`, four logs under `experiments/results/`,
this report. Updated: `PACKETS.md` (P5–P8 added, claimed),
`CLAIMS.md` (T-0020/0021, L-0015, C-0003, O-0009/0010, R-0003,
X-0025–0028), `NOTATION.md` (N9 appended per freeze protocol).
No migrated document touched.

## Claims affected

New: T-0020 (PROPOSED), T-0021 (PROPOSED), L-0015 (PROPOSED),
C-0003 (EMPIRICAL), O-0009, O-0010 (EMPIRICAL), R-0003 (REFUTED),
X-0025–X-0028. PR #3's Q-0002 is answered empirically (widths grow
exponentially) but not proved; their T-0004 normal form is now
cross-verified on 1021 exact links.

## Recommended next actions

1. Derive or refute the 0.19 width exponent from the coalescence
   recursion (branching analysis) — the sharpest open question this
   session produced (C-0003).
2. P2 (EQ interchange) — untouched today; the flagship theorem target,
   now with four rungs of dial data.
3. Independent review of T-0020 (the Fatou step above all), T-0021,
   L-0015 — reviewer slots open (M-0003).
4. Extend widths past L = 26 (streaming or class-sampling; ~2.5 GB at
   L = 28 naively).
5. P1 literature audit — now also owed Fatou/Kronecker citations.

## Organizational improvement ideas

* The mid-session correction of T-0020's Step 6 argues for a norm:
  proofs drafted in-session get one adversarial re-read pass before
  commit (self-review caught this one; an independent reviewer is
  still required by M-0003).
* Cross-branch claim reuse (their T-0004 → my T-0020 input) worked
  well with explicit provenance lines; keep citing the other branch's
  claim IDs verbatim until the merger reconciles namespaces.
