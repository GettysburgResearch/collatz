# Claim map — literature wave 10

| Imported/native item | Source | Repository interface | Verdict |
|---|---|---|---|
| `LIT-KTHM-0058` direct `81/64` limit point | Dubickas 2006 Thm. 3 | PR #16 `T-9317` | `KNOWN — EXACT`; subcritical |
| `LIT-KTHM-0058` four-phase lift | Dubickas 2006 + exact `81/64=(3/2)^4` calculation | PR #16/PR #67 | `KNOWN — COROLLARY`; stronger but subcritical |
| `LIT-KTHM-0059` one-sided interval exclusion | Dubickas 2009 Thm. 1 | centered sign word | `KNOWN — COROLLARY`; both signs recur |
| centered two-sided union exclusion | Dubickas 2008/2009 | PR #16/PR #67 | `HYPOTHESES FAIL / NOT PROVIDED` |
| `LIT-KTHM-0060` Matveev step | Matveev 2000 Cor. 2.3 | PR #53 `T-8255`, PR #70 `T-8260` | `KNOWN — EXACT SOURCE SPECIALIZATION` |
| old constant `2^32` | same source second branch | PR #53/PR #70 | safe but nonoptimal |
| `LIT-KTHM-0061` fixed-support finite reduction | native pulse identity + `L-8201` + Matveev | support `s<=18/117` | `PROPOSED / BRANCH-QUALIFIED COROLLARY` |
| `LIT-KTHM-0062` simultaneous finite places | Bugeaud 2002 | pulse resultants after two-term elimination | `KNOWN — EXACT`, conditional application |
| `LIT-KTHM-0063` one-prime logarithmic bound | Chim 2025 | denominator fresh-prime program | `KNOWN — EXACT`, conditional application |
| ordinary centered extraction | none of the six papers | PR #16/PR #67 | still open |
| six-branch zero-digit hitting | none of the six papers | PR #64 `Q-7401` | still open |
| full-denominator pulse contradiction | none of the six papers alone | PR #50/PR #53/PR #70 | still open |

## Main status changes

1. The Dubickas formula in PR #16 is no longer conditional or guessed.
2. The scalar centered route is now known to be subcritical even after a stronger four-phase lift.
3. The Matveev source boundary in PR #53/PR #70 is reconstructed and quantitatively improved.
4. Fixed support is finite-decision far beyond three pulses: `18` for `P3`, `117` for `P11`.
5. Bugeaud and Chim are tools only after an exact two-term finite-place reduction; they do not justify generic multi-term claims.
