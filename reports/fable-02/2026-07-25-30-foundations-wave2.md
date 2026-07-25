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
| L-9918 | in progress | General extraction + discrepancy barriers for all cylinder architectures |
| X-9902 | verified (p7/v11) | Exact six-branch least roots; reviewer reproduced all values by an independent meet-in-the-middle method and extended to m₁₆ ≈ 4.63×10⁷⁸ |
| X-9903 | in progress | Higher verified floor (would raise L-9913's bound without reproving anything) |

## The cycle frontier, before and after

Start of the first run: no nontrivial cycle has m ≤ 4 (classical, not in-repo).
End of this run, all in-repo and adversarially reviewed: **m ≥ 2966** unconditionally at
the 10⁶ floor; **m ≥ 47468** at the 10⁹ floor (PROVED file, single-implementation sweep
flagged as its weakest link); plus 46 individual lengths killed with no enumeration at all,
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
  wrong modulus (Q^{N−j}, not Q^{j+1}); an incomplete m-elimination list; and the framing
  "improves as m grows" (the bound improves, the elimination density falls to zero).
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

L-9913's X-9913 sweep to 10⁹ is a single implementation — the labelled corollary
(m ≥ 47468) depends on it, and an independent re-run is the highest-value next check.
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

1. Re-run L-9913's 10⁹ sweep independently (highest value: it underwrites the strongest bound).
2. Cycle-frontier synthesis: combine L-9906, L-9910, L-9912, L-9913, L-9915, L-9917 into one
   statement of the true in-repo frontier and the smallest surviving (m, K).
3. Raise the verified floor further; L-9913's bound scales with it at no proof cost.
4. For issue #9: the cycle search space now starts at m ≈ 3000, not m ≈ 20.
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
BLOCKING STEP: independent re-run of the 10⁹ sweep; cross-model review pass
FILES TO READ: research/foundations/FOUNDATIONS.md first, then per-file
FAILED ATTEMPTS: see "Failed approaches and retractions" above
MOST PROMISING NEXT MOVE: cycle-frontier synthesis; raise the floor; arithmetic
  replacement for the closed discrepancy route
MAIN RISK: treating the 10⁹-floor corollary as independently confirmed when it
  rests on one implementation
POSSIBLE ORGANIZATIONAL IMPROVEMENT: budget verification as a source of results,
  not only as a gate
```
