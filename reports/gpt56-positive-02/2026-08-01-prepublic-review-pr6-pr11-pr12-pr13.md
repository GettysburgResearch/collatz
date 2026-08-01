# Pre-public independent review — PRs #6, #11, #12, and #13

**Reviewer:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Review type:** SHA-scoped mathematical and artifact review  
**Status effect:** review verdicts only; no source claim status is silently changed  

No PR was merged. No public README was edited. No Collatz proof, counterexample, cycle, or `K-####` object is claimed.

## Frozen heads

| PR | Frozen head reviewed | Overall verdict |
|---|---|---|
| #6 | `4810a0771da61a1cb609ef8707dfcf7f0f6e666f` | **VERIFIED WITH FIXES** |
| #11 | `7950713cbb6ba0af0a424806cc36ce01ad24cf9e` | **REJECTED** |
| #12 | `7ea63c56c423f09b856818fc8a051c9d064d8eae` | **VERIFIED WITH FIXES** |
| #13 | `de739355f1f6d4d533d0c0e8148e678ee5abecea` | **VERIFIED WITH FIXES** |

The verdicts apply only to these commits. Later commits require a new review.

## Review method

The review traced load-bearing hypotheses, affine algebra, quantifiers, notation, dependency edges, source status, and finite-versus-all-depth conclusions. Code and frozen artifacts were inspected for whether they reconstruct the claimed mathematics or merely compare generated data. Expensive searches were not rerun.

Small targeted checks were used only where they decided a theorem boundary:

- PR #11 fixed-modulus determinism was falsified at modulus `4` by `1 ≡ 5 (mod 4)` but `T(1) ≡ 2`, `T(5) ≡ 0 (mod 4)`.
- PR #12 `L-9114` was independently exhausted for `q=3,4,5,6`: respectively `6`, `48`, `480`, and `5760` syntactically admissible transition tables, with zero countermodels.
- PR #13 support thresholds were checked exactly:
  `P3: 18/19`, `P11: 117/118`; the Barina–Ansari floor arithmetic was also checked exactly.

---

# PR #6 — termination-frontier port

## Verdict: **VERIFIED WITH FIXES**

### Verified claims

- `research/termination-frontier/CLAIM_INVENTORY.md`, `L-9001` — **VERIFIED at the frozen SHA** under the explicitly stated match annotation
  \[
  h=1+\min(i,j).
  \]
  The induction producing height `n` from `a_0^n e_0^n` is correct. The conclusion is only that this ordinary global match-bound criterion cannot have a finite bound; it does not imply nontermination.

- The same file, `R-9001` — **VERIFIED at the frozen SHA**. The two-vertex functional graph `1→2`, `2→2` is a complete countermodel to the inference
  ```text
  same weak component as a cycle
    ->
  at least the cycle minimum.
  ```
  A Collatz-specific lower bound would need additional arithmetic hypotheses.

- `Q-9001` and `Q-9002` remain open questions and make no theorem claim.

### Required fixes / status boundary

1. The packet should record the two review verdicts without changing the status of the unavailable legacy results.
2. `L-9001` does **not** verify that a particular external match-bound tool uses the same `1+min` annotation convention. That equivalence remains a separate source/tool interface.
3. The wider natural/arctic/CRT/cycle inventory is correctly marked provenance-only and must remain forbidden as a proof dependency until its statements, proofs, and artifacts are recovered.

### Integration concern

PR #6 is safe to integrate as a quarantined port after stable-ID aliasing. PR #13 `LIT-KTHM-0013` supplies the black-box AYH rewrite/Collatz equivalence, but it likewise does not prove that the native match annotation is tool-identical. No dependency on PR #11 should be introduced.

---

# PR #11 — ping-pong / Schottky packet

## Verdict: **REJECTED**

The frozen PR cannot be integrated as a theorem packet. It contains multiple load-bearing false statements, not merely missing citations or cosmetic defects.

## Fatal defect 1 — `T-0104` and `T-0105` are false

Files:

- `claims/theorems/T-0104-atomic-tensor-geometry-freeze.md`
- `claims/theorems/T-0105-general-tensor-radius-freeze.md`
- the corresponding closure language in `PACKET.md`

The asserted implication

```text
D1 = D0 + 2^L E,
R(D0) < 2^L
  ->
R(D1)=R(D0)
```

is false. For every `L>=2`, take

```text
D0={0,2^L-1},
E={0,1}.
```

Then `R(D0)=0`, while `D1-D1` contains `±1` by cancellation between the new `2^L` suffix and the old difference `2^L-1`.

PR #13 `LIT-KTHM-0024` gives a separate corrected theorem with the sufficient hypothesis

\[
\operatorname{diam}(D_0)+R(D_0)+1<2^L.
\]

That new theorem does not retroactively verify either original PR #11 theorem.

## Fatal defect 2 — `L-0108` fixed-modulus determinism is false

File:

- `claims/lemmas/L-0108-forward-crt-deterministic.md`

The shortcut Collatz image modulo `2^A` is not determined by the source modulo `2^A`, because division by two exposes one additional bit. At `A=2`,

```text
1 ≡ 5 (mod 4),
T(1)=2 ≢ 0=T(5) (mod 4).
```

Similarly `3 ≡ 7 (mod 4)` but `T(3) ≢ T(7) (mod 4)`.

This invalidates or removes the stated proof of:

- `T-0101`, clause E (“finite prepaid state bound”);
- `T-0102`, sections 4–5 insofar as they invoke fixed-modulus forward determinism;
- `T-0103`, the `Det` branch of the proposed meta-obstruction.

A valid finite residue dynamics must either retain the extra carry bit, use a relation rather than a function, or refine the modulus at each division.

## Additional gap — `L-0104`

The congruence/precision calculation in `L-0104-precision-drain-two-port.md` is useful, but increasing moduli alone do not prove that the compatible inverse-limit point is nonordinary. The specific expanding periodic pair can instead be excluded through the periodic fixed-point theorem `L-0107`. The original general inference must not be retained.

## Individually verified or salvageable material

The rejection is not a verdict that every file is false. The following claims pass in their stated narrow scopes, subject to the noted wording repairs:

- `L-0101`: the no-common-positive-interval conclusion is correct; replace the endpoint-only proof by an infimum/continuity argument for arbitrary intervals.
- `L-0102`: compact infinity-chart obstruction.
- `L-0103`: eventually periodic block schedules produce eventually periodic bit schedules.
- `L-0105`: odd-multiplier thinning.
- `L-0106`: scoped bit-tax algebra; “free 2-rank” remains informal terminology.
- `L-0107`: a purely periodic supercritical word has a negative rational `2`-adic fixed point. The eventual-preperiod wording should be stated separately.
- `L-0109`: common compact inverse-IFS obstruction.
- `L-0110`: morphic-schedule accounting, without an ordinary-nonrealization conclusion.
- `L-0111`: multichart tax.
- `L-0112`: weight-one suffix gap.
- `L-0114`: exact deep-burn `2`-adic valuation lemma.
- `L-0115`: the `3`-adic ultrametric valuation ledger; its Archimedean “bounded boost” discussion is not proved by the valuation statement.
- `T-0101` clauses B–D, and clause A under its generic odd-transport hypothesis, are salvageable after removing clause E and repairing dependencies.
- `T-0102` sections 1–3 are salvageable after removing the fixed-modulus conclusion.

`L-0113` is correctly only empirical/partial.

## Artifact review

- `X-0134` is a bounded validation script for `L-0114`, not an independent theorem verifier.
- `X-0139` checks the `3`-adic ledger, but part of the equal-valuation branch recomputes the same right-hand side it reports; it is a regression check, not independent evidence.
- No artifact can repair the false universal theorems above.

## Required integration action

Do not merge the frozen PR. Split it into:

1. a refutation/status packet marking `T-0104`, `T-0105`, and `L-0108` rejected and removing their downstream dependencies;
2. a clean salvage PR containing only the independently passing lemmas and repaired statements.

PR #13 `LIT-KTHM-0024` should land before, or be copied exactly into, any tensor-freeze repair.

---

# PR #12 — regular-sanctuary program

## Verdict: **VERIFIED WITH FIXES**

The exact finite-language core passes. The PR correctly does **not** claim existence of a sanctuary, a counterexample, or an all-size synthesis theorem.

## Verified unconditional core

The following files/claims pass at the frozen SHA:

- `D-9101-canonical-semantics.md`: canonical finite LSD-first positive words.
- `L-9101-shortcut-transducer.md`: the five-state subsequential shortcut transducer and terminal flush semantics.
- `L-9102-closure-decision.md`: decidability of exact forward closure for one fixed DFA.
- `L-9103-maximal-safe-kernel.md`: greatest safe accepting-state set by backward reachability.
- `L-9104-short-witness-bound.md`: every nonempty semantic `q`-state DFA has a canonical witness of length at most `q`.
- `L-9105-fixed-block-normalization.md`: fixed block invariance reduces to one-step regular invariance.
- `L-9106-odd-core-equivalence.md`: exact odd-core normalization.
- `L-9107-dyadic-cylinder-density.md`: the stated fixed-modulus basin-density theorem.
- the finite-lasso core of `L-9108-finite-lasso-obstruction.md`.
- `L-9109-exact-floor-normal-form.md`.
- `L-9110-quotient-monotonicity.md`.
- `L-9111-odd-suffix-floor.md`.
- `L-9112-depth-colored-residual-refinement.md`.
- `L-9113-reset-spine-bank-blind-spot.md`, including the distinction between concrete DFA banks and symbolic clause learning.
- `L-9114-gate-two-carry-elimination.md`.

The `L-9114` carry argument was independently checked on all syntactically admissible tables through six states, with zero countermodels.

## Source-conditioned conclusions

These conclusions are mathematically valid only after their external inputs are integrated:

1. The `q<=71`, `q=72`, and `d<=69` numerical floors use Barina’s verified range below `2^71`.
2. The slender-language corollary of `L-9108` uses the finite-union lasso decomposition for slender regular languages.

Barina’s 2025 source does state verification of all starts below `2^71`. PR #13 provides the source capsule. The unconditional automata statements should merge independently from these numerical/source corollaries.

## Artifact review

- `experiments/X-9101-regular-sanctuary/check_certificate.py` is fail-closed on its declared schema, map normalization, and the absent `3n-1` branch.
- `verify.py` reconstructs the exact terminal relation and closure checks.
- `independent_check.py` uses a separate traversal and is a useful differential checker, but it imports the shared `preimage_dfa` helper. It should be described as **differential/separately traversed**, not fully implementation-independent.
- the frozen `q=71`, gates `2..70` result is bounded evidence. Its solver `UNSAT` rows are not proofs of arbitrary-size nonexistence and are correctly not promoted.
- `literature/check_*`-style integrity checks and schema digests would not by themselves verify the mathematical relation; here the relation is separately reconstructed, which is the important distinction.

## Required fixes

1. Add a claim-level status matrix distinguishing unconditional finite-language theorems, source-conditioned corollaries, and bounded solver evidence.
2. Rename or qualify the “independent” checker description.
3. Link the Barina source capsule before promoting numerical floors.
4. Keep the slender decomposition explicitly source-qualified until the exact source theorem is admitted.

## Integration concern

PR #12 does not depend on the rejected PR #11. Its unconditional core can merge before the source corollaries. For a clean public dependency graph, merge the relevant PR #13 source capsules first, then promote only the conditional corollaries whose sources have been admitted.

---

# PR #13 — citation-critical literature and source suite

## Verdict: **VERIFIED WITH FIXES**

The literature-governance architecture is sound and unusually careful: source inspection tiers, native applicability checklists, branch-qualified mappings, and explicit `UNVERIFIED` registers are correctly separated. The verdict does **not** promote every file in `literature/imported-theorems/` to a verified theorem; that directory also contains native proposed syntheses.

## Source/import layer that passes review

Representative load-bearing items independently checked in this pass include:

- `LIT-KTHM-0013`: AYH construct a mixed binary–ternary rewrite system whose termination is equivalent to Collatz; the capsule correctly says this does not prove termination and does not identify every native rewrite convention.
- `LIT-KTHM-0019`, `0020`, `0021`: regular transducer image, closure decision, and greatest safety kernel; all include correct self-contained finite proofs.
- `LIT-KTHM-0024`: correct refutation of PR #11’s tensor-radius theorem and correct sufficient separation condition.
- `LIT-KTHM-0058`, `0059`: the Dubickas scalar/four-phase and one-interval applicability boundaries are conservatively stated; neither is promoted to centered-orbit nonexistence.
- `LIT-KTHM-0060`: the Matveev specialization uses the weighted coefficient parameter and the stated rational-field constant in the correct normalization.
- Barina 2025: all starts below `2^71` are verified.
- Ansari 2025: the extension through
  \[
  4\cdot3^{44}+2
  \]
  is valid. The clean citation route is Corollary 2.2 plus the explicit gap in the recursively sufficient set. Proposition 3.2 is printed with a “largest known” hypothesis, but its proof does not use maximality, and Remark 3.1 applies the same gap to the `2^71` floor.
- Hercher’s published result supplies the external `m>=92` local-minimum input used by `LIT-KTHM-0052`.

Exact arithmetic checks confirm

```text
2*3^44+1 < 2^71 < 4*3^44+2,
4*3^44+2 = 2*(2*3^44+1),
```

and the fixed-support rate thresholds

```text
P3:  s<=18, first uncovered s=19;
P11: s<=117, first uncovered s=118.
```

## Native proposed results that remain dependency-limited

The following are substantial and internally coherent, but must retain their proposed/branch-qualified status:

- `LIT-KTHM-0052`: the length-184 decoder and stability argument are coherent, and the code is exact. It still imports Hercher and has only the author-side `run.py --check-results` interface rather than a separately implemented verifier.
- `LIT-KTHM-0061`: fixed-support finite reduction is conditional on PR #53 `L-8201` and the distributed-pulse identity.
- `LIT-KTHM-0064`: the independent verifier reconstructs product, transition, Legendre, Matveev, continued-fraction, and exceptional-family certificates; it does not independently prove the native four-pulse numerator identity.
- `LIT-KTHM-0065`: the independent verifier genuinely reconstructs logarithm intervals, continued fractions, support thresholds, verified-floor and pulse-comparison coverage. It does not verify Barina’s distributed computation or the native pulse/divisor identities, exactly as disclosed.

These files are not rejected. They are **GAP/BLOCKED at their stated native dependencies**, while the surrounding source audit is verified.

## Code and artifact boundary

- `check_literature.py` and wave checkers are integrity linters: file presence, IDs, links, digests, and expected markers. They are not mathematical theorem verifiers.
- `LIT-X-0064/0065` verifiers are substantially stronger and independently reconstruct the recorded inequalities and continued-fraction coverage without importing generator code.
- No expensive scan was rerun in this review.

## Required fixes

1. `LITERATURE.md` at the frozen head summarizes only waves 1–6, while the PR contains waves 1–11. Add an explicit current-wave index or point to `literature/README.md` and the wave 7–11 ledgers.
2. Correct the typographical `\nu_n`/`u_n` mismatch in `LIT-KTHM-0059`.
3. Separate, by directory or unmistakable front-matter, **external imported theorem capsules** from **native proposed corollaries/theorems** such as `0052`, `0050`, `0061`, `0064`, and `0065`. The current directory name can otherwise imply a stronger trust status than the file header.
4. Phrase the Barina–Ansari extension through Corollary 2.2 and the explicit recursively-sufficient-set gap, rather than citing the proposition headline alone.
5. Add a separately implemented verifier for `LIT-X-0052` before promoting the length-184 theorem.

## Integration / merge order

1. Merge the source/governance layer and self-contained correction capsules first.
2. PR #13 `LIT-KTHM-0024` must precede any salvage of PR #11.
3. Admit the Barina/Ansari and regular-language sources before promoting PR #12’s conditional floors and slender corollary.
4. Keep `LIT-KTHM-0052/0061/0064/0065` proposed until their native pulse/cycle dependencies receive separate mathematical review; merging their documentation does not verify those dependencies.

---

# Cross-PR connections found during review

These are observations about the reviewed results, not new verified theorems.

1. **Weak SCC reasoning versus exact safety kernels.** PR #6 `R-9001` explains why weak-component membership cannot justify a cycle-minimum bound. PR #12 supplies the correct finite-state replacement: compute the exact predecessor closure of forbidden states and take its complement. This should be the default pattern whenever a finite relation is available.

2. **Why PR #11’s tensor freeze failed, and what PR #12 contributes.** PR #13’s corrected separation theorem shows that scale separation alone is insufficient because old and new differences can nearly cancel. PR #12’s carry/refinement lemmas are precisely the kind of extra state restriction that could establish the required diameter inequality on a particular slice. This possible salvage is PROPOSED, not proved.

3. **Full-denominator frontier.** PR #13’s fixed-support pulse work and its source-audited Archimedean/non-Archimedean tools are naturally compatible with the repository’s complete-denominator first-crossing compiler. The missing bridge is uniform incompatibility at growing support, not another bounded pulse scan.

The separate proposed-connections note on this branch records these points without changing any reviewed verdict.

---

# SERIOUS RESOLUTION PATH

**Present repository-wide, but not completed by any reviewed PR.**

The clearest serious program is still the two-obligation route:

```text
SC*: exclude every fixed ordinary all-prefix-supercritical source;
FC*: exclude every complete first-crossing/cycle denominator tuple.
```

The reviewed PRs contribute as follows:

- PR #6 gives valid method obstructions but no termination proof.
- PR #11, at the frozen SHA, cannot be used.
- PR #12 gives exact decision and strong obstructions for regular sanctuaries, but regularity is not exhaustive for Collatz counterexamples.
- PR #13 gives source-audited logarithmic and finite-place tools plus fixed-support cycle closures, but arbitrary words and growing support remain.

Exact missing steps for a serious full resolution are:

1. **SC***: prove a fixed-source valuation or canonical-boundary inequality bounding the length of every all-supercritical prefix from one positive integer.
2. **FC***: prove a uniform fresh-prime/resultant or full-denominator incompatibility for the growing-support, high-bank first-crossing language, including displacement zero.
3. Prove that the chosen FC argument applies to every complete candidate word, not only pulse lifts of the two known negative cycles.
4. Independently reconstruct every external source and native compiler used in the final chain.

Until both SC* and FC* are closed, the repository status remains **UNSOLVED**.
