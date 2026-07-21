# Agent report — literature foundations and claim audit

**Agent:** `gpt56-pro-03`  
**Issue:** `#7 — P1 literature audit and imported theorem suite`  
**Branch:** `agent/gpt56-pro-03/7-literature-foundations`  
**Date:** 2026-07-21

## Starting hypothesis

The active branches used a mixture of classical Collatz facts, exact repository constructions, broad literature analogies, and a few external-theorem invocations whose hypotheses had not yet been frozen. A branch-neutral literature layer could make those boundaries auditable without choosing between the colliding claim ledgers.

## Approaches attempted

1. Re-read the live repository governance and all active issue/PR metadata.
2. Froze the current ledgers of PR #3, issue #4, and the termination-frontier PR rather than relying on the earlier handoff snapshot.
3. Located primary or publisher-hosted sources across parity-vector theory, preimage trees, Mahler's problem, automaticity, recurrence zeros, Fourier decay, measure rigidity, generalized Collatz undecidability, automated rewriting, and recent computation.
4. Reconstructed short reusable results independently when the imported fact was elementary enough to prove safely.
5. Compared every live mathematical claim to the sources using conservative verdicts and qualified IDs.
6. Added static validation for bibliography keys, relative links, theorem IDs, and ambiguous bare claim IDs.

## New results

### Proved facts added to the literature suite

- Complete parity-affine, parity-bijection, and exact `2`-adic tracking proofs (`KTHM-0001`–`KTHM-0003`).
- Complete LTE/order proof simultaneously supporting `CLAUDE/T-0005`, `CLAUDE/L-0013`, and `CLAUDE/T-0019` (`KTHM-0004`).
- Complete proof that an existing letter frequency of a fixed-base automatic sequence is rational (`KTHM-0005`).
- Complete Gelfond–Schneider corollary proving `log_64 81` and its nonconstant rational Möbius transforms transcendental (`KTHM-0006`).
- Complete nondegenerate power-sum corollary from Skolem–Mahler–Lech (`KTHM-0007`).
- Complete proof that reciprocal poles of rational integer power series are algebraic integers (`KTHM-0008`).

### Citation-audit findings

- `CLAUDE/T-0003` currently attributes the rational-frequency step to Cobham; that attribution is incorrect. The conclusion has a repair through `KTHM-0005` once the schedule and its frequency are stated precisely.
- `CLAUDE/T-0006` names a valid theorem, but its exact power sum, coefficients, and nondegeneracy check are not written. Its literature reduction remains `UNVERIFIED`.
- `CLAUDE/Q-0002` is a useful `2`-adic analogue of Mahler's Z-number problem, not an externally known equivalence.
- Direct applications of Li–Sahlsten/Solomyak to EQ and Furstenberg/Rudolph/Shmerkin/Wu to one integer point fail at the currently written hypotheses; they remain methodological interfaces.
- No exact external antecedent was located for the collision-fiber conjugacies, universal carry pumping, signature-tail amplification, geometry-preserving tensor law, or finite-boundary regeneration. These are marked only `POSSIBLY NOVEL FORMULATION`.
- The Aaronson–Yolcu item was verified as the three-author Yolcu–Aaronson–Heule paper, with an exact termination/Collatz equivalence.

## Candidate counterexamples

None added. No source inspected and no repository claim establishes a positive-integer divergent orbit or nontrivial cycle.

## Failed approaches

- Treating Cobham as a symbol-frequency theorem was rejected after checking its actual two-base recognizability scope.
- Treating the EQ product as an off-the-shelf self-similar measure was rejected because the family is modular and depth-dependent.
- Treating `S`-unit terminology in the run-length skeleton as an automatic application of an `S`-unit theorem was rejected because the cofactors vary.
- Treating measure/dimension rigidity as a pointwise theorem about `V∞∩Z` was rejected.
- A single canonical claim-number assignment was deliberately avoided because the live branches still collide.

## Potential errors and remaining uncertainty

- Black-box theorem imports preserve the located source statement but do not reproduce long external proofs.
- The SML mapping cannot be completed without the exact repository sequence.
- The automatic-frequency repair still requires an exact proof that the proposed schedule is a fixed-base automatic sequence and that the relevant natural frequency exists.
- “No antecedent found” is not a novelty proof.
- Source inspection levels vary and are recorded in `literature/SOURCE_LEDGER.md`.

## Files changed

- `LITERATURE.md`
- `literature/README.md`
- `literature/SOURCE_LEDGER.md`
- `literature/CLAIM_CROSSWALK.md`
- `literature/UNVERIFIED.md`
- `literature/references.bib`
- `literature/claim-maps/{PR3,CLAUDE,TERMINATION}.md`
- `literature/imported-theorems/README.md` and `KTHM-0001` through `KTHM-0013`
- ten files under `literature/topic-notes/`
- `scripts/check_literature.py`
- this report

## Claims affected

No canonical status changed. The audit supplies mappings or correction requests for all live PR #3 claims, `CLAUDE/L-0001`–`CLAUDE/L-0015`, `CLAUDE/T-0001`–`CLAUDE/T-0021`, the active CLAUDE questions, and `TERM/...`.

## Recommended next actions

1. Apply the automatic-frequency attribution repair to issue #4.
2. Freeze and audit the exact SML power sum.
3. Independently review `KTHM-0004` and use it as the common arithmetic dependency.
4. Build a difference-inequality system for same-weight collision-fiber multiplicity, inspired by Applegate–Lagarias/Krasikov–Lagarias but adapted to the correct object.
5. Continue with rational/negative cycle literature, effective recurrence-zero bounds, and genuine `S`-unit reductions.

## Organizational improvement ideas

Keep this branch-neutral literature directory permanently separate from mathematical claim ledgers. Require every external dependency to name a source-inspection level and an atomic import ID where possible. Preserve branch-qualified IDs until an integrator selects a canonical ledger. This avoids both citation drift and merge conflicts in a rapidly changing multi-agent repository.
