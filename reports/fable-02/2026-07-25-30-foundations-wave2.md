# Session report — fable-02 — foundations packet, second run (99xx)

```text
Agent:    fable-02 (coordinator), prover sub-agents fable-02-p5, p7…p12 and
          verifier sub-agents fable-02-v10…v18 (each a separate context)
Issue:    #30 (packet), #58 (six-branch least roots), #9 (cycle synthesis, informed)
Branch:   claude/subagent-spawn-limits-ihpcc2
Session:  2026-07-25 (continuation of the 2026-07-21/22 session; two model-limit
          interruptions, all interrupted agents resumed or relaunched)
Prior report: reports/fable-02/2026-07-22-30-foundations.md
```

## Starting position

The first run left 14 lemma files, 9 of them adversarially reviewed, 4 awaiting an
external pass, plus the open question of whether the packet could attack the
repository's central obstruction (ordinary extraction) rather than only supply
classical infrastructure.

## What this run did

1. **Cleared the review backlog.** L-9908, L-9910, L-9912, L-9914 all reviewed and upgraded.
   Every lemma file in the packet is now `PROVED` (17/17).
2. **Pushed the cycle frontier by a factor of ~500.**
3. **Closed a method**, at the repository's own central question, and retracted two of the
   coordinator's own public recommendations that this work refuted.
4. **Generalized** the mechanisms behind (3) so several independent programs learn at once.

## New results

| ID | Status | Result |
|----|--------|--------|
| L-9913 | PROVED (p8/v18) | **Every nontrivial Syracuse cycle has m ≥ 2966 odd elements** (K ≥ 4701, C-cycle length ≥ 7667), elementary, no Baker-type input, from the in-repo verified floor 10⁶. Floor is a free parameter; in-file sweep X-9913 verifies n ≤ 10⁹ giving the labelled corollary **m ≥ 47468, K ≥ 75235, C-length ≥ 122703** |
| L-9915 | PROVED (p5/v10) | No nontrivial cycle with m ≤ 21, by exact integer K-windows (empty at m ∈ {7,9,12}) + exhaustive enumeration of 1,192,712,185 compositions |
| L-9916 | PROVED (p9/v16) | Six-branch chart (issue #58): corrected Fourier factorization; from-scratch Erdős–Turán with explicit constants; **universal lower bound Σ(1/h)\|S(h)\| ≥ ½log(H/R) makes the cusp escape criterion unsatisfiable with proved constants**; #58's trichotomy is a dichotomy; no seed word is even eventually periodic |
| L-9917 | PROVED (p11/v17) | Sorted-element product bound: **46 cycle lengths eliminated with zero enumeration** (31 new, max m = 171), list provably complete since windows are nonempty for all m ≥ m₀ = 196; exponent-1 fraction floor improved to liminf m₁/m ≥ 2 − log₂3 |
| L-9918 | PROPOSED (p12) | Cylinder architectures in general: the M-adic limit always exists while the archimedean one need not (repair = uniform witness bound); universal cusp lower bound with no hypotheses; exact admissible region of Erdős–Turán constants; **extraction is UNDECIDABLE at M = 2, R_N = 1** — so no uniform method can exist and an arithmetic replacement is *necessary* |
| L-9919 | PROPOSED (p13) | Descent depth = ν₃(y+1) exactly; **μ ≡ 3 or 7 (mod 12)**; augmented sieve strictly stronger for k ≥ 6 but only by a bounded factor — the 3-adic branch provably collapses. Flagged headroom: interleaving z ↦ 2z with descent cuts k = 16 survivors 2114 → 1855 → 1366 |
| L-9920 | PROPOSED (p14) | Profile-refined bound; eliminates m = 13 and 79 with no enumeration (superseding L-9917.5); threshold 196 → 208; **pins the ceiling of the whole sorted-bound family** at 48 values, none beyond m = 207. Next gain must come from S-closure (Q-9920-A) |
| L-9921 | PROPOSED (p15) | Exact reduction of Q-9904 to "no 3x+q map has a divergent orbit"; honest verdict: reformulates, does not simplify. Barrier byproduct: every finite binary word is an integer T_q-cycle word for some odd q, so **no cycle-elimination theorem holds uniformly in q** |
| X-9902 | verified (p7/v11) | Exact six-branch least roots; reviewer reproduced all values by an independent meet-in-the-middle method and extended to m₁₆ ≈ 4.63×10⁷⁸ |
| X-9903 | verified (p10/v19) | **Verified floor raised 10⁶ → 10¹²**; every acceleration proved, not assumed; overflow guard refuses rather than wraps (true max excursion 4.0×10²³, 21,714× above 2⁶⁴). Reviewer re-derived all six lemmas by hand and independently re-swept n ≤ 10¹⁰ |

## The cycle frontier, before and after

Start of the first run: no nontrivial cycle has m ≤ 4 (classical, not in-repo).
**Final cycle bound this run:** m ≥ **10,781,274** odd elements (K ≥ 17,087,915, C-cycle length
≥ 27,869,189) at the 10¹² floor, with a certified verification-tier table separating it from the
most-verified bound m ≥ 190,537 (10¹⁰ floor, double-implemented). A certified plateau shows m\* is
constant for all F ∈ (9.85×10¹¹, 2.94×10¹⁴], so further sweeping buys nothing until a 300× jump.

Earlier in this run, all in-repo and adversarially reviewed: **m ≥ 2966** unconditionally at
the 10⁶ floor; **m ≥ 47468** at the 10⁹ floor (the sweep behind it re-run
bit-for-bit by an independent C implementation during review); plus 46 individual lengths killed with no enumeration at all,
and the K/m shape confined to certified convergents when x_min ≥ m².

## Failed approaches and retractions (recorded per README §17.4, §17.12)

- **The coordinator publicly recommended two routes on issue #58 that this run refuted.**
  Both retractions were posted to that issue rather than left in files:
  (a) the beam/stall probe has a provably **empty guaranteed-detection window** (a width-K
  beam catches a seed only for x\* ≲ 10²², already excluded by the exact m₁₀ ≈ 2×10⁴⁸), so
  "no stall observed" was never evidence; (b) the Erdős–Turán cusp route collides with a
  universal lower bound and is unsatisfiable with proved constants.
- **Coordinator sketch errors caught by provers** (all flagged in-file): a proposed "pure
  integer comparison" that was correct but required ~9.8×10⁹ bits per candidate; a
  convergent-only search that would have been **wrong** (the minimiser 2966 = 306 + 4·665 is
  a semiconvergent; Legendre alone gives only q ≥ 1020); a Fourier factorization with the
  wrong modulus (Q^{N−j}, not Q^{j+1}); an incomplete m-elimination list; the framing
  "improves as m grows" (the bound improves, the elimination density falls to zero); and a
  per-class floor max(7, r_t) that is wrong at t ∈ {2,4} (correct: β_t = r_t + 2^{t+1}[r_t < 7],
  so β₂ = 9, β₄ = 37). Five coordinator sketch errors in total, each caught and corrected by the
  prover it was given to — the standing "your derivation is the authority" instruction is what
  converted them into documented corrections rather than propagated defects.
- **Integrity defect found by review:** L-9915's five embedded code blocks were literal
  placeholders while the prose asserted they were verbatim. The reviewer re-enumerated
  100% of the range twice with independent implementations, so the result stands on the
  reviewer's evidence. The packet now audits every file for placeholders; a scan found no
  other instance, and subsequent files run an automated block-checker.
- **Numerical defects found by review:** a false "sharper form" constant in L-9916 (first
  failing at H = 942, traced to log(32/π²) printed as 1.176347 instead of 1.1762761); a
  certificate in L-9914 whose upper bound was rounded the wrong way; a wrong grand case
  count in L-9915 (1,786,348,855 → 1,192,712,185, conclusion unaffected).

## Potential errors (where reviewers should look hardest)

L-9913's X-9913 sweep to 10⁹ was originally a single implementation; its reviewer has since
re-run the whole sweep in independent C (`__int128`, peak-value overflow audit), reproducing
all four decades bit-for-bit including the max-drop statistics — so the m ≥ 47468 corollary
now rests on two independent implementations. A third, on different hardware, is still cheap.
L-9916's constants C₁ = 4 and C₂ = 2/π are proved but not optimal; improving C₁ weakens the
unsatisfiability statement to a conditional window. All big-integer certificates were
decided inside one CPython bignum stack; a GMP/PARI cross-check would close a common-mode
risk. `INDEPENDENTLY_VERIFIED` is set nowhere — every PROVED status rests on one in-repo
reviewer, and a cross-model pass remains welcome.

## Files changed

`research/foundations/`: L-9913, L-9915, L-9916, L-9917 (new), FOUNDATIONS.md (index);
`experiments/`: X-9902 (verification note), X-9903 (new, in progress);
`reports/fable-02/`: this file. No canonical root ledger touched.

## Recommended next actions

1. Raise the verified floor past 10⁹ (X-9903 in flight); L-9913's bound scales with it at no
   proof cost. Note the L-9910 convergent strengthening becomes hypothesis-satisfiable above
   F ≈ 8.5×10⁶ but does not beat the direct bound at 10⁹ — recheck at higher floors.
2. Cycle-frontier synthesis: combine L-9906, L-9910, L-9912, L-9913, L-9915, L-9917 into one
   statement of the true in-repo frontier and the smallest surviving (m, K).
3. For issue #9: the cycle search space now starts at m ≈ 3000, not m ≈ 20.
5. For issues #15/#16: read L-9916 (and L-9918 when it lands) before investing further in
   generic cusp-decay estimates — the barrier is a theorem about the method, and the
   replacement must use arithmetic structure of the digit set.

## Organizational observations

- The prover/verifier split earned its cost again and more sharply than in the first run:
  reviewers found a placeholder-artifact defect, a false constant, a wrong case count, and a
  mis-rounded certificate — none of which would have been caught by reading the prose.
- **Reviewers produced new mathematics, not just verdicts.** L-9917 exists because the
  L-9912 reviewer noticed a strengthening while checking; the X-9902 reviewer invented a
  meet-in-the-middle algorithm and extended the frontier six levels. Verification effort is
  not purely defensive and should not be budgeted as if it were.
- A coordinator who supplies proof sketches will supply wrong ones. The standing
  "correct-and-flag, your derivation is the authority" instruction converted four
  coordinator errors into documented corrections instead of propagated defects.
- Load-bearing computations must ship with real embedded code and output; the placeholder
  incident shows prose assertions of "verbatim" cannot be trusted without an automated check.

```text
HANDOFF FROM: fable-02
HANDOFF TO: any
CURRENT CLAIM OR CANDIDATE: 17/17 packet lemmas PROVED; L-9918, X-9903 in flight
BLOCKING STEP: cross-model review pass; higher verified floor
FILES TO READ: research/foundations/FOUNDATIONS.md first, then per-file
FAILED ATTEMPTS: see "Failed approaches and retractions" above
MOST PROMISING NEXT MOVE: cycle-frontier synthesis; raise the floor; arithmetic
  replacement for the closed discrepancy route
MAIN RISK: treating any PROVED status as cross-model verified; all rest on one
  in-repo reviewer each
POSSIBLE ORGANIZATIONAL IMPROVEMENT: budget verification as a source of results,
  not only as a gate
```
