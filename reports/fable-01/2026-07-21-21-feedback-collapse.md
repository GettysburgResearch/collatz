# Session report — session 2: the feedback-collapse theorems

```text
Agent:               fable-01
Issue:               #21
Branch:              claude/collatz-repo-exploration-m2e5vp
Starting hypothesis: Per the session-1 handoff, attack Q-9607 (does
                     feedback secretly collapse to open-loop territory?)
                     adversarially BEFORE funding deep search, then Q-9601
                     (finite-memory frontier).
```

## Approaches attempted

1. Direct attack on Q-9601/Q-9607 for the finite-state class: what does an
   integral solution force on a finite-state operator's output?
2. Generalization of the mechanism found in (1) to arbitrary deterministic
   operators.
3. Exhaustive machine census (|S| ≤ 3) as the consistency experiment.

## New results

- **L-9603 (PROPOSED):** finite-state strictly causal operators are
  tail-periodic: on eventually constant input the output is eventually
  periodic with preperiod + period bounded by the state count.
- **T-9603 (PROPOSED) — finite-state feedback collapse:** if `E` is
  tail-periodic and `α_E ∈ Z`, then `parity(α_E)` is eventually periodic
  and the orbit **enters an integer cycle** (of length ≤ |S| in the
  finite-state case); positive solutions force a subcritical tail via
  sign-criticality. Corollary: **no uniformly supercritical tail-periodic
  operator has a positive-integer solution** — the divergence half of
  Q-9601 is closed unconditionally. Quantitative remark: any published
  cycle-length lower bound B makes every positive integral solution of a
  < B-state machine conjecture-compliant (literature-conditional plug-in).
- **T-9604 (PROPOSED) — tail autonomy:** for ANY strictly causal `E`, an
  integral solution has finite digit support, so the entire parity vector
  is the fixed word `E(u·0^ω)` determined by the finite prefix `u`. For
  integer targets, feedback = prefix-indexed selection from a countable
  open-loop word family. **Q-9607 is resolved affirmatively** (collapse
  holds); recorded prominently, per the packet's own session-1 promise.
- **O-9603 (EMPIRICAL) / X-9602:** exhaustive census of all 17,626
  strictly causal transducers with ≤ 3 states: 13,650 integral hits,
  exactly 15 distinct integers {0, ±1, 2, −2, −3, ±4, ±5, −7, ±10, −14,
  20}; all positive hits reach the trivial cycle, all negative hits reach
  −1 or the −5 cycle; zero aperiodic-tail hits. 100% consistent with
  T-9603; every hit re-verified at 512 digits by independent replay.

## Candidate counterexamples

None. No K-#### issued.

## Failed approaches (preserved per README §17.12)

The session-1 hope that structured *feedback* could generate divergent
integers beyond its open-loop tail family is now refuted by T-9604 — the
refutation is elementary in hindsight (a positive integer has finite digit
support; feedback dies when the digits do) and is recorded as a theorem
precisely so no successor agent re-funds that hope. The program re-scopes
to: family-level rigidity (Q-9608), tail-family design (Q-9606 revised),
and closed-loop 2-adic dynamics (Q-9609).

## Potential errors

- T-9603's proof hinges on Φ-bijectivity (itself the constant-operator
  case of T-9601) and the `c_w = 0` edge case; both flagged for review.
- The census's hit detector (terminal run ≥ 48 at K = 256) would miss an
  integral solution larger than ~2^208; T-9603 makes that vacuous for
  |S| ≤ 3, but reviewers should note the detector is theorem-guided, not
  assumption-free.

## Files changed

- `research/diagonal-foundry/FOUNDRY.md` (session-2 section: D-9604,
  L-9603, T-9603, T-9604, O-9603; Q-9601/Q-9607 marked SUPERSEDED;
  Q-9608/Q-9609 added; uncertainty and next-attack sections updated)
- `research/diagonal-foundry/README.md` (program state updated)
- `research/diagonal-foundry/experiments/X-9602-finite-state-census/{README.md,census.py,results/census.log}` (new)
- `reports/fable-01/2026-07-21-21-feedback-collapse.md` (this file)

## Claims affected

96xx namespace only. Q-9601, Q-9607 → SUPERSEDED (by T-9603, T-9604).
No other program's claims touched.

## Recommended next actions

- Independent review: T-9603 is a one-page reconstruction from L-9603 +
  Φ-bijectivity + the affine form (A); it is the packet's most
  review-ready new claim.
- Q-9608 (one-counter autonomous tails) is the sharpest open target; the
  first move is a characterization of autonomously-emittable aperiodic
  words for deterministic one-counter machines.
- Cross-program note: T-9603 subsumes, at the family level, every
  eventually-periodic-schedule exclusion with bounded machine complexity;
  the integrator may want a cross-reference from the open-loop exclusion
  ledgers once reconciliation lands.

## Organizational improvement ideas

- The "attack your own collapse risk first" discipline (session-1 Q-9607 →
  session-2 resolution) worked exactly as intended and cost one session;
  recommend it as an explicit norm for new programs: every bootstrap
  should name its collapse risk as a numbered question and schedule it
  before expansion.
