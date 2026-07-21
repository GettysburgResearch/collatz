# Agent report — literature audit wave 1

Agent: `gpt56-pro-03`
Issue: `#4`, packet P1
Branch: `agent/gpt56-pro-03/4-literature-audit`
Starting hypothesis: the highest-value first literature contribution would be an applicability audit of the live branches' external dependencies, plus atomic proofs of reusable classical inputs, rather than a flat bibliography.

## Approaches attempted

- Re-read the current issue-#4 packet queue and claim ledger at head `41617a5`.
- Re-read draft PR #3 at head `d162cd9dd54fe74f86d572612e3f80c2dd8fb59a`, including the new inverse-signature and exponential-fiber theorem.
- Inspected draft PR #6 to verify the Aaronson–Yolcu–Heule provenance.
- Located and inspected primary or official sources across parity vectors, almost-all Collatz results, backward trees, Mahler Z-numbers, automatic sequences, transcendence, Skolem–Mahler–Lech, integer power series, Fourier decay, measure rigidity, generalized undecidability, and automated rewriting.
- Audited source hypotheses separately from native reductions.
- Reconstructed short proofs that will be reused across multiple native claims.

## New results

### Literature and applicability findings

- Terras/Everett exactly cover finite parity cylinders and the parity-residue bijection.
- The automaticity obstruction should cite Cobham's rational-frequency property, not the famous two-base theorem.
- The SML step is valid only after an explicit coefficient/nondegeneracy audit.
- Mahler/FLP provide a real analogue, not an equivalence or a 2-adic measure threshold.
- Li–Sahlsten/Solomyak and Rudolph/Shmerkin/Wu are methodologically adjacent but do not directly apply to the current objects.
- Applegate–Lagarias/Krasikov–Lagarias count backward trees, not forward common-output collision fibers.
- Yolcu–Aaronson–Heule is verified and directly relevant; generalized undecidability remains scoped to generalized maps.

### Complete atomic proofs added

- parity-affine cylinders and residue bijection;
- exact 2-adic tracking-depth loss;
- all-level orders `ord_(81^k)(64)` and `ord_(2^j)(81)`;
- transcendence of the `64/81` slope and gap frequency;
- rational-frequency obstruction for automatic sequences;
- algebraicity of primitive-substitution frequencies;
- Fatou–Pólya integral denominators for integer recurrences;
- nondegenerate Skolem–Mahler–Lech corollary;
- binomial entropy tail bound.

The order theorem closes the missing proof in `CLAUDE/T-0019`. The Fatou–Pólya theorem supplies a cleaner dependency for the load-bearing final step of `CLAUDE/T-0020`.

## Candidate counterexamples

None. No positive-integer Collatz counterexample is claimed or supported by this report.

## Failed approaches and negative findings

- No exact literature antecedent was located for PR #3's arbitrary collision-fiber conjugacy, carry pumping, run-length skeleton, inverse signatures, or exponential odd-tail amplification. This is recorded as `POSSIBLY NOVEL FORMULATION`, not novelty.
- No direct theorem was found transferring FLP's real interval obstruction to `Z_2`.
- No direct Li–Sahlsten/Solomyak theorem covers the depth-dependent modular Fourier product.
- No measure-rigidity theorem found addresses membership of one ordinary integer in `V∞`.
- The historical “Kronecker criterion” label in `SKELETON.md` did not match the needed theorem and was replaced by a proved integral-denominator result.
- No authoritative comprehensive overview later than Lagarias 2021 was located and inspected; Strauch 2022 was added as recent problem-specific Mahler literature, not a Collatz overview.

## Potential errors / review requests

- Review the `p`-adic denominator proof in `LIT-KTHM-0007`, especially the transition from absence of denominator roots in every open unit disk to algebraic integrality of reciprocal poles.
- Check that `CLAUDE/T-0020`'s exponential-polynomial representation is minimal and noncancelling before identifying its ratio limit with a characteristic base.
- Expose and verify the exact coefficients used by `CLAUDE/T-0006` before upgrading its external reduction.
- Reconcile `PR3/T-0005` with the issue-#4 fixed-depth width conjecture only after aligning their fiber definitions and depth accounting.

## Files changed

- `LITERATURE.md`
- `literature/README.md`
- `literature/SOURCE_LEDGER.md`
- `literature/CLAIM_CROSSWALK.md`
- `literature/APPLICABILITY_AUDITS.md`
- `literature/UNVERIFIED.md`
- `literature/references.bib`
- `literature/check_literature.py`
- branch-specific claim maps
- eight topic notes
- fourteen imported-theorem notes
- this report

## Claims affected

Primary: `CLAUDE/L-0004`, `L-0013`, `T-0003`, `T-0005`, `T-0006`, `T-0011`–`T-0012`, `T-0014`, `T-0019`, `T-0020`, `T-0021`, `Q-0002`, `Q-0005`; `PR3/L-0001`, `L-0005`–`L-0006`, `T-0002`–`T-0005`; termination-frontier provenance in PR #6.

No native status is changed by this report.

## Recommended next actions

1. Integrate the wording corrections into native claim files through separate reviewable commits.
2. Independently reconstruct `CLAUDE/T-0019` from `LIT-KTHM-0003` and consider promotion after review.
3. Audit the exact coefficients and equality in `CLAUDE/T-0006`.
4. Review the Fatou step in `CLAUDE/T-0020` against `LIT-KTHM-0007`.
5. Begin wave 2 with exact provenance for rational cycles, accelerated/generalized maps, beta-expansion and p-adic digit-restriction literature, and stronger structured-fiber counting analogues.

## Organizational improvement ideas

- Keep a permanent namespaced literature ledger separate from the mathematical truth-status ledger.
- Require every external-theorem use to link both an imported theorem note and a native reduction audit.
- Add the literature checker to CI after the first literature PR merges.
- Distinguish `SOURCE VERIFIED`, `THEOREM VERIFIED`, and `APPLICATION VERIFIED`; these are different evidence levels.
