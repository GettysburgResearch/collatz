# Canonical integrated claim records

**Snapshot:** `2026-08-01-first-major-integration`  
**Cutoff:** `2026-08-01T21:16:40Z`  

These are claim-level integration records. Proof-bearing source files remain at the exact commits listed below. The repository remains **UNSOLVED**.

## IC-EXTRACT-001 — Canonical-residue stabilization is the ordinary-extraction criterion

**Kind:** `theorem-interface`  
**Mathematical status:** `verified`  
**Integration status:** `canonical`  

### Statement

Let nested dyadic cylinders have compatible canonical least representatives R_n. A nonnegative ordinary integer lies in every cylinder exactly when R_n is bounded, equivalently eventually constant. For nested nonempty positive survivor sets, bounded least roots are likewise equivalent to eventual constancy and yield one positive all-depth ordinary survivor. The signed negative boundary is represented by eventual maximal appended blocks, not by bounded least representatives.

### Scope

Compatible dyadic residue chains and nested positive survivor sets. This is an extraction theorem, not a theorem that any particular Collatz-derived survivor set is nonempty or bounded.

### Does not establish

- Finite compatibility alone is insufficient.
- A 2-adic completion need not be an ordinary integer.
- The theorem does not prove SC* or produce a Collatz counterexample.

### Provenance

- PR #57 at `f12e6ec45a88da98b64ef97bdfd25c3c7d48b435` — `L-7601`, `T-7601`; `research/ordinary-extraction/claims/L-7601-signed-stabilization.md`; `research/ordinary-extraction/claims/T-7601-bounded-minimum-extraction.md`. Role: canonical proof source.
- PR #3 at `caa775e85a3618a6cce0bbad345300aaefeab640` — `T-0043`; `claims/theorems/T-0043-universal-ordinary-extraction-barrier.md`. Role: independent overlapping formulation.
- PR #56 at `53ed4e49be522052405e6aa2c11b2b810a01bf2a` — `T-7801`; `research/global-extraction/claims/T-7801-ordinary-extraction-dichotomy.md`. Role: independent overlapping formulation.
- PR #60 at `1221ef5639bd89b56a0583a58f0b2fc63af52931` — `T-7401`; `research/global-blocker-review/claims/T-7401-archimedean-tightness-extraction.md`. Role: independent overlapping formulation.

### Review and evidence

- Verdict: verified within packages classified VERIFIED WITH FIXES.
- Report: `research/positive-coefficient-gate/reviews/PREPUBLIC-PR56-PR57-PR60.md` at `1c25b5e4be25a7c73b78e80b505c54879f02d8f1`.
- Proof evidence: independently reconstructed.
- Artifact evidence: not applicable; symbolic theorem.

### Repair / supersession boundary

The integration selects PR #57's signed decomposition as canonical and records the other statements as aliases; no source file is silently renamed.

---

## IC-GHOST-001 — Finite positive representatives do not force an ordinary all-depth point

**Kind:** `countermodel-theorem`  
**Mathematical status:** `verified`  
**Integration status:** `canonical`  

### Statement

The periodic parity block 1110 has affine fourth iterate T^4(x)=(27x+19)/16 and unique periodic 2-adic realization -19/11. Every finite prefix cylinder has infinitely many positive ordinary representatives, while the all-depth completion is nonintegral and negative in the real order.

### Scope

An explicit parity-cylinder countermodel to compactness, drift, and finite-prefix extrapolation.

### Does not establish

- It is not a positive Collatz orbit.
- It does not refute Collatz.
- It does not say every compatible family has a nonordinary completion.

### Provenance

- PR #57 at `f12e6ec45a88da98b64ef97bdfd25c3c7d48b435` — `T-7602`; `research/ordinary-extraction/claims/T-7602-supercritical-ghost-schedules.md`. Role: proof source.

### Review and evidence

- Verdict: verified.
- Report: `research/positive-coefficient-gate/reviews/PREPUBLIC-PR56-PR57-PR60.md` at `1c25b5e4be25a7c73b78e80b505c54879f02d8f1`.
- Proof evidence: independently reconstructed.
- Artifact evidence: small exact replay reported; no expensive computation.
- Dependencies: `IC-EXTRACT-001`.

---

## IC-PERIODIC-001 — Periodic parity tails are controlled by the complete denominator

**Kind:** `theorem`  
**Mathematical status:** `verified`  
**Integration status:** `canonical`  

### Statement

For a nonempty binary word w of length L with s one-bits and affine constant C_w, the periodic tail w^infinity has the unique 2-adic realizer x_w=C_w/(2^L-3^s). If 3^s>2^L then x_w<0. If 3^s<2^L and s>=1, then x_w is a positive integer exactly when 2^L-3^s divides C_w, in which case exact parity replay gives a positive cycle. The all-zero word is the separate endpoint x_w=0. Consequently, every positive ordinary eventually periodic parity tail enters a positive cycle.

### Scope

Raw parity words, or accelerated/controller symbols only after each repeated symbol is proved to emit one fixed finite parity block.

### Does not establish

- Recurrence of a coarse type alone is insufficient.
- Proper-factor divisibility is insufficient; the complete denominator is required.
- No nontrivial positive cycle is produced.

### Provenance

- PR #61 at `8a85b6c96d677143e08568477c26a232d56263a9` — `T-7401`; `research/periodic-extraction/claims/T-7401-eventual-periodicity-full-denominator.md`. Role: source with all-zero clause requiring correction.
- PR #62 at `20a4d5d7ba9d9a2b5e7a4dfecb83f6220bb7da36` — `T-7701`; `research/ordinary-extraction/claims/T-7701-eventually-periodic-supercritical-firewall.md`. Role: verified supercritical firewall.
- PR #63 at `3011e6a78bd572c0c15a5b6112904f9c492ef29a` — `L-7501`, `T-7501`; `research/ordinary-extraction-review/claims/L-7501-periodic-shortcut-fixed-point.md`; `research/ordinary-extraction-review/claims/T-7501-no-eventually-periodic-divergent-parity.md`. Role: source with explicit least-root escape and all-zero metadata fix.

### Review and evidence

- Verdict: corrected statement independently verified; frozen PR #61/#63 packages remain VERIFIED WITH FIXES.
- Report: `reports/gpt56-crossmodel-audit-01/2026-08-01-prepublic-pr61-pr63-review.md` at `e85a9bb709da369852d2b0044a76005082a82897`.
- Proof evidence: independently reconstructed.
- Artifact evidence: X-7710 small exact audit passed; not an expensive search.

### Repair / supersession boundary

This canonical statement is a new corrected integration statement. It does not retroactively change the frozen PR #61 or PR #63 verdicts; both remain VERIFIED WITH FIXES.

---

## IC-SC-001 — Coefficient-stopping finiteness is equivalent to escape of least all-supercritical sources

**Kind:** `theorem-interface`  
**Mathematical status:** `verified`  
**Integration status:** `canonical`  

### Statement

Let m_N^sup be the least positive source whose first N coefficient prefixes are all supercritical. Then m_N^sup tends to infinity exactly when every fixed positive integer has finite coefficient stopping time. Moreover, an ordinary positive orbit whose every shifted coefficient prefix remains supercritical diverges to +infinity.

### Scope

Fixed ordinary sources and canonical all-supercritical cylinders.

### Does not establish

- The universal finiteness assertion itself, called SC* in the roadmap, remains open.
- This is not the stronger literature conjecture t(n)=tau_c(n); the integration uses 'coefficient-stopping finiteness' to avoid that nomenclature error.
- Moving compatible sources or a 2-adic completion do not satisfy the fixed-source hypothesis.

### Provenance

- PR #77 at `3efcbfb2e38f02b04eb6bba35eb258ec552d655c` — `T-6709`, `T-6710`, `L-6711`; `research/positive-coefficient-gate/T-6709-supercritical-implies-divergence.md`; `research/positive-coefficient-gate/T-6710-SC-star-inverse-stopping-equivalence.md`; `research/positive-coefficient-gate/L-6711-canonical-low-band-source-endpoint-bound.md`. Role: proof source.

### Review and evidence

- Verdict: verified with terminology/provenance fixes.
- Report: `reports/gpt56-complexity-01/2026-08-01-pre-public-review-76-77-79.md` at `046eeda2268b4ac1b90a9618a4ed2460a111a0e5`.
- Proof evidence: independently reconstructed.
- Artifact evidence: symbolic; no large computation.
- Dependencies: `IC-EXTRACT-001`.

### Repair / supersession boundary

The canonical wording incorporates the review's terminology repair and does not extend the verdict to current PR #77's post-review M-6712 note.

---

## IC-AUT-001 — The finite canonical-tail safety SCC is a cofinite artifact

**Kind:** `theorem`  
**Mathematical status:** `verified`  
**Integration status:** `canonical`  

### Statement

For each fixed safety depth d in the PR #14 reverse-tree language, the forbidden set is finite, the safe language is cofinite, and the minimal complete DFA has exactly one cyclic SCC: the terminal two-state canonical tail. Removing that SCC leaves a DAG; the exact power-of-two witness shows nonclosure. No cofinite forward-invariant set can exclude {1,2}.

### Scope

The fixed-depth LSD-first canonical safety language defined in PR #14.

### Does not establish

- Recurring motifs across different depths are not an all-depth sanctuary.
- The result does not classify arbitrary regular guards or infinite-state arithmetic sets.

### Provenance

- PR #14 at `9e3d90f50a6bf908401d2a2556513077daca3eb4` — `D-9201`, `L-9201`; `research/safety-quotient/claims/D-9201-finite-safety-language.md`; `research/safety-quotient/claims/L-9201-cofinite-tail-obstruction.md`. Role: proof source.

### Review and evidence

- Verdict: verified.
- Report: `reports/gpt56-pro-03/2026-08-01-prepublic-review-pr3-pr14-pr16-pr19.md` at `3d2b0a3c7e873388c42f00c5cbb4f09cf9897391`.
- Proof evidence: independently reconstructed.
- Artifact evidence: bounded automaton artifact inspected; theorem does not extrapolate it.

---

## IC-RIG-001 — Finite tame sections cannot self-replicate the reviewed six-branch chart

**Kind:** `theorem-packet`  
**Mathematical status:** `verified`  
**Integration status:** `canonical`  

### Statement

For the fixed rational chart P=3^12, Q=2^19 and its six reviewed digits: the only full-tail finite integer-affine section nucleus is the original expanding forward map; the same holds for finite rational-function nuclei after eventual integrality; and the all-depth survivor contains no infinite arithmetic progression or semilinear forward-invariant sanctuary.

### Scope

The exact six-branch chart of PR #64. The rational-function conclusion uses the reviewed eventual-integrality and finite-control hypotheses.

### Does not establish

- No theorem decides whether the least roots are bounded or escape.
- The physical seed crosswalk remains branch-qualified to PR #45 L-8405 and is not part of this canonical claim.
- The PR #65 algebraic/semialgebraic extension is not included until its proof repairs are reviewed at a new SHA.

### Provenance

- PR #64 at `88884c3e590b08aeb2018872987e71e14de1fe7b` — `D-7401`, `L-7401`, `T-7401`, `T-7402`, `T-7403`, `T-7404`; `research/six-branch-extraction/claims/D-7401-six-branch-minimal-word-system.md`; `research/six-branch-extraction/claims/L-7401-high-quotient-section.md`; `research/six-branch-extraction/claims/T-7401-affine-section-rigidity.md`; `research/six-branch-extraction/claims/T-7402-finite-affine-nucleus-rigidity.md`; `research/six-branch-extraction/claims/T-7403-finite-rational-nucleus-rigidity.md`; `research/six-branch-extraction/claims/T-7404-no-semilinear-sanctuary.md`. Role: proof source.

### Review and evidence

- Verdict: verified with namespace and dependency fixes.
- Report: `reports/gpt56-cartographer-01/2026-08-01-pre-public-review-pr64-pr65-pr66.md` at `591a06ad914b63dddfd65ee658dbec36291ffbc0`.
- Proof evidence: independently reconstructed.
- Artifact evidence: small exact table checks; no expensive computation.

### Repair / supersession boundary

The `IC-RIG-001` namespace resolves collisions with unrelated PR #60/#61 `T-7401` claims without renaming or erasing the source IDs.

---

## IC-REF-001 — Universal itinerary factor-complexity barrier is false

**Kind:** `refutation`  
**Mathematical status:** `refuted`  
**Integration status:** `canonical`  

### Statement

The original PR #37 `T-9318` claim, asserted for every itinerary, is false: the constant words 0^infinity and 1^infinity select the ordinary completion 0 while having factor complexity one.

### Scope

The exact universal statement at PR #37 frozen head.

### Does not establish

- This refutation does not invalidate the nonconstant repair in IC-REP-001.
- It does not refute the centered-power equivalence or recurrence cone.

### Provenance

- PR #37 at `a518db7feece37513ddcda729553e8b8c4c4d657` — `T-9318`, `R-9304`; `research/adelic-cusp/claims/T-9318-factor-complexity-cylinder-barrier.md`; `research/adelic-cusp/claims/R-9304-t9318-constant-word-counterexamples.md`. Role: refuted source and exact counterexample.

### Review and evidence

- Verdict: T-9318 rejected/refuted; R-9304 verified.
- Report: `reports/gpt56-positive-entropy-01/2026-08-01-prepublic-pr35-pr37-pr38-pr42-review.md` at `09d6f9086d4ead63a5102f05458441939c29f4f5`.
- Proof evidence: explicit exact counterexamples independently checked.
- Artifact evidence: not required.

### Repair / supersession boundary

The refutation remains permanently visible. It is not overwritten by the repaired theorem.

---

## IC-REP-001 — Nonconstant itinerary factor-complexity barrier

**Kind:** `repaired-theorem`  
**Mathematical status:** `verified`  
**Integration status:** `canonical`  

### Statement

For the reviewed 64→81 section, put delta=log_64(81/64). A nontrivial ordinary survivor with initial room A_0>=2 and itinerary e satisfies p_e(n)>(n-log_64 A_0)/delta for every n>=1, hence liminf p_e(n)/n>=1/delta=17.6548475770... . More generally, a nonconstant binary word with liminf p_v(n)/n<1/delta cannot have eventually zero nearest-integer cylinder blocks.

### Scope

Nontrivial ordinary 64→81 survivors and nonconstant binary words in the reviewed centered-cylinder model.

### Does not establish

- The constant words are excluded.
- Equality at slope 1/delta is not excluded.
- The theorem concerns this induced section, not every Collatz trajectory.

### Provenance

- PR #37 at `a518db7feece37513ddcda729553e8b8c4c4d657` — `T-9319`; `research/adelic-cusp/claims/T-9319-nonconstant-factor-complexity-cylinder-barrier.md`. Role: proof source.

### Review and evidence

- Verdict: verified as a separate repaired theorem.
- Report: `reports/gpt56-positive-entropy-01/2026-08-01-prepublic-pr35-pr37-pr38-pr42-review.md` at `09d6f9086d4ead63a5102f05458441939c29f4f5`.
- Proof evidence: independently reconstructed.
- Artifact evidence: not required.
- Dependencies: `IC-REF-001`.

### Repair / supersession boundary

This is a distinct theorem with an added nonconstancy hypothesis. It does not retroactively verify PR37:T-9318.

---

## RD-SC-001 — SC*: universal fixed-source coefficient stopping

**Kind:** `open-obligation`  
**Mathematical status:** `open`  
**Integration status:** `roadmap`  

### Statement

Prove that every positive integer has finite coefficient stopping time, equivalently that the least source m_N^sup of an all-supercritical depth-N cylinder tends to infinity.

### Scope

One fixed ordinary source; not moving finite witnesses or a 2-adic completion.

### Does not establish

- No reviewed PR proves this obligation.

### Provenance

- PR #77 at `3efcbfb2e38f02b04eb6bba35eb258ec552d655c` — `T-6710`; `research/positive-coefficient-gate/T-6710-SC-star-inverse-stopping-equivalence.md`. Role: verified equivalence defining the obligation.

### Review and evidence

- Verdict: open; equivalence verified.
- Report: `reports/gpt56-complexity-01/2026-08-01-pre-public-review-76-77-79.md` at `046eeda2268b4ac1b90a9618a4ed2460a111a0e5`.
- Proof evidence: obligation not proved.
- Artifact evidence: not applicable.
- Dependencies: `IC-EXTRACT-001`, `IC-SC-001`.

---

## RD-FC-001 — FC*: complete first-crossing and full-denominator exclusion

**Kind:** `open-obligation`  
**Mathematical status:** `open`  
**Integration status:** `roadmap`  

### Statement

Exclude every complete first-crossing canonical realization, including d=0 nontrivial positive cycles and d>0 acyclic near-returns, by closing the entire denominator 2^j-3^q with compatible source, endpoint, displacement, and exact physical replay.

### Scope

All first-crossing words and every prime-power factor of the complete denominator.

### Does not establish

- Proper-factor hits, bounded support, finite-length censuses, or independently chosen local residues do not prove FC*.
- No reviewed PR proves this obligation.

### Provenance

- PR #81 at `816c364ab2019a6dda235f710f8d30de2da33ab9` — `L-6812`, `L-6814`, `L-6817`, `T-6812`; `research/positive-coefficient-entropy/claims/L-6812-bilateral-shifted-near-return.md`; `research/positive-coefficient-entropy/claims/L-6814-positive-cycles-absorb-into-first-crossing.md`; `research/positive-coefficient-entropy/claims/L-6817-primitive-cycle-injective-reduction.md`; `research/positive-coefficient-entropy/claims/T-6812-support-corrected-cofinal-envelope.md`. Role: reviewed architecture.
- PR #83 at `e6ad4d627e579a46054a07965af0618885206d49` — `L-6912`, `L-6913`, `T-6914`; `research/positive-coefficient-tangent/claims/L-6912-complete-factor-synchronization.md`; `research/positive-coefficient-tangent/claims/L-6913-resultant-root-normal-form.md`; `research/positive-coefficient-tangent/claims/T-6914-rough-support-displacement-window.md`. Role: reviewed factor synchronization.

### Review and evidence

- Verdict: open; reviewed reductions and subclasses only.
- Report: `reports/gpt56-global-01/2026-08-01-pre-public-review-pr80-pr81-pr83.md` at `b8eb3f3f917452eb6151b71038d5722381ad87cc`.
- Proof evidence: obligation not proved.
- Artifact evidence: bounded computations inspected but not used as all-length evidence.
- Dependencies: `IC-PERIODIC-001`.

---
