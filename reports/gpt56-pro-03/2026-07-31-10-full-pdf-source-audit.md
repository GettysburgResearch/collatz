# Wave 10 report — full-PDF source audit and blocker attack

**Agent:** `gpt56-pro-03`  
**Date:** 2026-07-31  
**Issue:** #7, with direct interfaces to #40, #52, #58  
**Status:** source audit plus exact native corollaries; no Collatz resolution

## Work performed

All six newly supplied PDFs were read in full:

- Dubickas 2006;
- Dubickas 2008;
- Dubickas 2009;
- Matveev 2000;
- Bugeaud 2002;
- Chim 2025.

The paper files themselves are not redistributed. Repository-ready theorem capsules preserve the load-bearing formulas, exact theorem/page locations, applicability checks, and native substitutions.

## Main mathematical gains

1. Confirmed the exact Dubickas constant and proved a stronger four-phase `3/2` lift for the centered `81/64` errors.
2. Proved that the full Dubickas trilogy does not directly exclude the centered two-sided union.
3. Reconstructed Matveev Corollary 2.3 at `log2/log3` and replaced the coarse `2^32` constant by the safe bound `748,000,000`.
4. Reduced the PR #53/PR #70 cutoffs by factors of roughly six to nine.
5. Generalized the largest-gap/Matveev mechanism from three pulses to every fixed support below an exact critical density: `18` for `P3`, `117` for `P11`.
6. Imported strict Bugeaud/Chim applicability gates and an effective finite-prime escape corollary.

## Exact artifacts

```text
LIT-X-0058-centered-dubickas
semantic digest:
8db492a8bd64439e374f09956b5304f7c95ad4bbc8853107e830b42db83b26fc

LIT-X-0060-matveev-specialization
four cutoff margin hashes and exact support-threshold certificates
stored in canonical.json
```

Both scripts replay their canonical JSON byte-for-byte using Python's standard library and exact `Fraction` arithmetic.

## Honest remaining blockers

- no ordinary centered seed is constructed or excluded;
- support four has not yet been exhaustively replayed;
- the fixed-support theorem stops at support density `19/118` for the two baselines;
- no fresh-prime/resultant incompatibility theorem is proved;
- no six-branch zero-digit hitting theorem is proved;
- source audit does not promote unreconstructed native claims automatically.

## Recommended review order

1. `LIT-KTHM-0060-matveev-log2-log3-specialization.md`
2. `LIT-X-0060-matveev-specialization/run.py`
3. `LIT-KTHM-0061-fixed-support-pulse-finite-reduction.md`
4. `LIT-KTHM-0058-dubickas-centered-limit-points.md`
5. `LIT-X-0058-centered-dubickas/run.py`
6. `LIT-KTHM-0059-dubickas-small-interval-boundary.md`
7. `LIT-KTHM-0062-bugeaud-simultaneous-madic.md`
8. `LIT-KTHM-0063-chim-padic-two-logarithms.md`
9. `LIVE_REPO_REVIEW_WAVE10.md`
