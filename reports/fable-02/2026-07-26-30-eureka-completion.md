# Session report — fable-02 — Eureka reconstruction + backlog closure (third run)

```text
Agent:    fable-02 (coordinator), provers fable-02-p17…p19, verifiers fable-02-v21…v26
Issue:    #30 (packet); PR #47 (source program, cross-posted); issue #58 (context)
Branch:   claude/subagent-spawn-limits-ihpcc2
Session:  2026-07-26 (~3h window)
Prior reports: 2026-07-22, 2026-07-25 in this directory
```

## What this run did

1. **Cleared the entire review backlog**: L-9919, L-9920, L-9921, L-9922 all PASS →
   the pre-existing packet is 22/22 PROVED.
2. **Reconstructed, strengthened, and verified the owner-supplied "Eureka" packet**
   (drafted externally as L-9608/L-9609/T-9608 for PR #47, never pushed):
   - **L-9923** (PROVED, p17/v25): affine cycle-collapse toolkit. STRENGTHENS the source:
     the sharp collapse threshold is W < P+Q, not W < Q (the source's W = Q sharpness
     example is provably impossible; true extremal is a 2-cycle at W = P+Q). Verified by a
     conclusive closed sweep over all alphabets for all 435 pairs P < Q ≤ 30. The
     minimum-edge sieve E = Dm + Qk needs no sign hypothesis; height gate E_max < gD.
   - **T-9924** (PROVED, p18/v26): the all-repetition pulse-grammar theorem. For every
     b ≥ 1 and 0 ≤ a ≤ 5, no finite word over the complete fixed-weight (a,b) macro
     alphabet has a nontrivial integral cycle (contracting packets: any sign; (5,1):
     positive cycles impossible by supercriticality). Source verified with ZERO numerical
     corrections; three strengthenings: (4,2) closes by sharp collapse directly;
     contracting closures cover integral cycles of any sign; and the EXACT bijection
     E = 3(α + 7153) between (5,1)'s branch constants and the six-branch digit ladder —
     the pulse program and issue #58's least-root program are the same object, and the
     a-cutoff and (5,1)-supercriticality are both the single inequality 3¹² > 2¹⁹.
3. **Two cross-file defects found and formally corrected** by the review layer:
   L-9917.4(5)'s singleton-window side-claim withdrawn (counterexample |W*(241)| = 2);
   L-9905.4 annotated as a = 3-specific (general form needs 1/(a−2); false at a = 5).
4. **T-9925 (contracting-phase extension to a ≥ 6) commissioned and in flight** at the
   window's close: target-set stabilization toward the m+k = 3 trio, mod-9 parity kill
   for odd a, per-row congruence hunt for even a; possible complete classification.
   Its file will land in the working tree when the prover finishes; commit separately.

## Corrections to the source spec (provenance duty)

The external report's mathematics survived verification essentially intact — a rare and
creditable outcome — with these amendments: the sharpness claim W = Q was wrong (now
W < P+Q, a stronger theorem); (4,2) closes more simply than its sieve route; the "two
targets" at (5,2) are {3D, 2D+Q}; all six packet closures reproduce exactly.

## Candidate counterexamples

None proposed, none found. T-9924 eliminates grammars; it does not bear on the truth of
the conjecture and creates no K-#### object. The six-branch m_N dichotomy is untouched —
but now positioned exactly: the first supercritical one-pulse packet immediately beyond a
completely cycle-free contracting regime.

## Recommended next actions

1. Land T-9925 when the prover finishes; review it (v27).
2. Lift L-9923/T-9924 into PR #47's program if its owner wants them (one comment posted).
3. The m_N dichotomy remains THE open frontier; see NEGATIVE_RESULTS.md for what cannot
   decide it and the two doors that remain (phase-preserving methods; architecture-specific
   arithmetic — of which T-9924's exact bijection is a new piece).

```text
HANDOFF FROM: fable-02
HANDOFF TO: any
CURRENT CLAIM OR CANDIDATE: 24/24 landed files PROVED; T-9925 in flight
BLOCKING STEP: T-9925 completion + review; cross-model pass still welcome packet-wide
FILES TO READ: FOUNDATIONS.md, then L-9923/T-9924
MOST PROMISING NEXT MOVE: T-9925 rows; then the m_N dichotomy via the exact bijection
MAIN RISK: treating T-9924's grammar eliminations as bearing on Collatz itself
```
