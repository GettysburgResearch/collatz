# Session report — least-counterexample preimage and packing attack

**Agent:** `gpt56-pro-56`  
**Date:** 2026-07-31  
**Issue:** #78  
**Branch:** `agent/gpt56-pro-56/78-preimage-packing`  

## Objective

Cross-read the newest positive-direction repository work and the current literature, then attack only the two exhaustive coefficient-stopping lanes of a least positive Collatz counterexample.

## Sources inspected

Repository:

- PR #76: coefficient stopping, Farey gate, mechanical extremizer, Denjoy--Koksma exclusion;
- PR #77: independent affine review and full divergence of all-prefix-supercritical ordinary paths;
- issues #54--#59 and PRs #56--#57: ordinary extraction and full-denominator boundaries;
- issue #78: current two-lane positive proof target.

Literature:

- Angeltveit, arXiv:2602.10466;
- Rozier--Terracol, arXiv:2502.00948v5 / *Discrete Mathematics* 349 (2026) 115167;
- Chang, arXiv:2603.25753;
- Niu, arXiv:2605.13886, consulted only to confirm withdrawal and duplication boundary.

## New exact results

1. Coefficient supercriticality already implies the `485/306` ballot condition on every proper prefix before the first crossing.
2. A smaller merging preimage of the first-crossing endpoint yields a general linear-in-root gate. The standard mod-9 preimages raise the gate to approximately `10^21`--`10^22` steps on four endpoint classes.
3. In the all-time supercritical lane, distinct-state packing and the exact product formula imply:
   - at most `O(K^(1/6)3^H)` visits to defect band `D<=H`;
   - mean defect at least `(5/6) log_3(K/n)-O(1)`.
4. Along lower convergents, the maximal mechanical paradoxical threshold grows quadratically in the denominator. Therefore a fixed verified floor plus the unconstrained maximal-remainder comparison cannot be a cofinal proof.

## Why the full proof is not claimed

The uncovered first-crossing endpoint classes remain, and the preimage theorem gives lower gates rather than impossibility. The supercritical packing theorem forces high coefficient capital but does not show that its unique compatible parity completion is nonordinary. Chang's paper explicitly leaves the decisive orbit-level one-bit mixing issue open.

## Exact next theorem

A complete positive proof now needs one of:

- cofinal path-merging coverage with a contradiction-producing bound;
- exact separation of every later first-crossing cylinder root from its paradoxical threshold;
- an ordinary nonrealization theorem for all-prefix-supercritical parity paths satisfying the new defect-area pressure.

The packet intentionally does not replace these targets with another finite census or prescribed schedule.