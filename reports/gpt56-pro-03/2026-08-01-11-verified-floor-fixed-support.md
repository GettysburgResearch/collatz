# Literature wave 11 — verified-floor fixed-support pulse closure

**Agent:** `gpt56-pro-03`  
**Date:** 2026-08-01  
**Issue:** #7  
**Draft PR:** #13  
**Counterexample status:** none

## Objective

Continue beyond the full-PDF audit by using the newly source-audited logarithmic machinery to attack a remaining global cycle blocker rather than merely adding references.

## Main result

Added proposed theorem `LIT-KTHM-0065`:

```text
P3=(1,2):
  every nontrivial positive-cycle lift with fixed support 1..18 is excluded;

P11=(1,1,1,2,1,1,4):
  every positive-cycle lift with fixed support 1..117 is excluded.
```

The first uncovered supports are `19` and `118`, exactly where the largest-gap exponential-decay rate becomes nonpositive.

## Mechanism

The proof combines:

1. the exact distributed-pulse divisor identity;
2. largest-gap normalization for arbitrary fixed support;
3. the verified lower floor for every nontrivial positive-cycle state;
4. Matveev's source-audited real logarithmic bound;
5. complete continued-fraction coverage.

The verified floor yields

\[
0<\Lambda<\frac{kr}{3N_*},
\]

which excludes the short primitive convergents. The pulse inequality excludes the later convergents. Their union covers every candidate family below the Matveev cutoff.

## Exact artifact

Added `LIT-X-0065` with independent verifier.

```text
P3 coverage:
  verified floor only  = 3
  pulse only           = 2
  both                 = 7
  total                = 12

P11 coverage:
  verified floor only  = 4
  pulse only           = 5
  both                 = 2
  total                = 11
```

Semantic digest:

```text
c730cce495223542e2d15e424ca0ba94996c2d0382289baab3604344abe8b179
```

The generator and independent verifier passed locally.

## Source correction

Corrected `LIT-KTHM-0060`: the native estimate `B<kr+1` concerns Matveev's weighted coefficient parameter from equation `(1.3)`, not the coarser `B*`. The numerical certificates were already using the valid weighted bound; their values are unchanged.

## Dependency boundary

The theorem remains proposed because:

- the pulse correction/divisibility identity requires independent native reconstruction;
- the Barina computation was not rerun;
- the Ansari extension to `N_*` remains an imported theorem chain.

Every rational/logarithmic inequality after those interfaces is exactly replayable.

## Strategic conclusion

The next pulse target is no longer support five. It is the support-density transition:

```text
P3 support 19;
P11 support 118.
```

The largest-gap method cannot cross that boundary. The recommended next attacks are multi-gap resultants and a fresh-prime incompatibility between the denominator and all pulse resultants.

## Files

- `literature/imported-theorems/LIT-KTHM-0065-verified-floor-fixed-support-pulse-closure.md`
- `literature/experiments/LIT-X-0065-verified-floor-fixed-support/`
- `literature/LIVE_REPO_REVIEW_WAVE11.md`
- `literature/SOURCE_LEDGER_WAVE11.md`
- `literature/claim-maps/WAVE11.md`
- `literature/UNVERIFIED-WAVE11.md`
- `literature/check_literature_wave11.py`
- this report
