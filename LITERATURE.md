# Literature audit — wave 1

**Agent:** `gpt56-pro-03`
**Target packet:** issue #4, `P1 — Literature audit`
**Repository snapshot audited:** `claude/collatz-migration-math-osr370@41617a5`, draft PR #3 at `d162cd9dd54fe74f86d572612e3f80c2dd8fb59a`, and draft PR #6 as opened 2026-07-21
**Status:** citation and applicability audit; no repository theorem is promoted by this packet

This is the first durable literature layer for the repository. It is deliberately namespaced because the issue-#4 branch and PR #3 still use colliding claim identifiers. Throughout this package:

- `CLAUDE/T-0003` means the claim on `claude/collatz-migration-math-osr370`;
- `PR3/T-0003` means the claim on draft PR #3;
- `TERM/...` means the isolated termination-frontier packet in draft PR #6;
- `LIT-KTHM-####` identifies an imported literature theorem and never replaces a native claim ID.

## Executive findings

1. **The parity-cylinder substrate is classical.** The affine finite-iterate formula, the bijection between length-`L` parity words and residues modulo `2^L`, and the resulting exact loss of one 2-adic digit per common-parity step are present in Terras and Everett. `PR3/L-0001`, the substrate of `PR3/L-0005`, and `CLAUDE/L-0004` should cite these sources directly.

2. **The collision-fiber packaging is not found verbatim in the located literature.** Backward-tree papers by Applegate–Lagarias and Krasikov–Lagarias study preimage growth and density, not finite sets of forward parity cylinders sharing one affine endpoint. `PR3/T-0002`, `PR3/L-0003`, `PR3/L-0004`, and `PR3/T-0005` are therefore marked **POSSIBLY NOVEL FORMULATION**, never “novel.” Their proofs remain repository mathematics built on classical parity coordinates.

3. **The automaticity argument needs a citation correction, not abandonment.** The relevant external statement is Cobham's rational-frequency property for automatic sequences, commonly cited to *Uniform tag sequences* (1972): when a letter frequency exists in a `k`-automatic sequence, it is rational. This is not the famous two-multiplicatively-independent-bases Cobham theorem. The repository's required gap frequency is transcendental by a Gelfond–Schneider corollary, so a rigorously defined schedule with that frequency is not `k`-automatic for any `k`. The stronger sentence “the surviving format is exactly Sturmian/Ostrowski” does not follow from this obstruction and should remain a construction proposal.

4. **The SML invocation is conditionally sound.** A three-term power sum with nonzero coefficients and bases `81^18`, `81^9`, and `1` is nondegenerate because no quotient of two bases is a root of unity. Skolem–Mahler–Lech then implies finitely many zeros. The repository must still exhibit the exact equality, prove the coefficients do not collapse to an identically zero sequence, and state that the theorem gives no effective bound.

5. **The multiplicative-order gap can be closed completely.** Odd-prime and 2-adic lifting-the-exponent give
   `ord_{81^k}(64)=9·81^{k-1}` for every `k≥1` and
   `ord_{2^j}(81)=2^{j-4}` for every `j≥4`.
   Consequently `⟨64⟩ = 1+9Z/(81^k)`. The full proof is `LIT-KTHM-0003`; it supplies the missing general argument behind `CLAUDE/L-0013` and `CLAUDE/T-0019`.

6. **The new skeleton-rigidity proof has the right strategy but the literature dependency should be rewritten.** The phrase “Kronecker's criterion” in `SKELETON.md` is not the right citation. The needed fact is the Fatou–Pólya integral-denominator principle: a rational power series with integer coefficients has an integral denominator after normalization, so its characteristic bases are algebraic integers. `LIT-KTHM-0007` gives a self-contained proof using rational Hankel rank and `p`-adic analyticity. Once the repository's dominant-base asymptotic is checked in a minimal, noncancelling exponential-polynomial representation, the contradiction with `(N/M)^U` is valid.

7. **The Mahler connection is an analogy, not an equivalence to the classical problem.** Mahler and Flatto–Lagarias–Pollington work with real fractional parts of `ξ(p/q)^n`. The repository asks for an ordinary integer inside a digit-constrained 2-adic attractor. FLP's interval-width lower bound `1/p` does not transfer to 2-adic Haar measure; comparing `1/32` with `1/81` is heuristic bookkeeping across different spaces, not a theorem.

8. **Modern Fourier-decay and measure-rigidity papers are near misses.** Li–Sahlsten and Solomyak study fixed real self-similar measures. The repository's `R_K` are depth-dependent measures on changing finite groups with a modular twist and a frequency window that grows with `K`. Rudolph, Shmerkin, and Wu concern invariant measures or dimensions of real invariant sets, not membership of one ordinary integer in `V∞`. These sources suggest methods but presently prove none of `CLAUDE/T-0011`, `CLAUDE/T-0012`, or `CLAUDE/Q-0005`.

9. **The automated rewrite reference is verified.** Yolcu, Aaronson, and Heule prove an exact Collatz/string-rewrite equivalence and automated termination results for weakenings. Conway and Kurtz–Simon establish undecidability only for generalized Collatz systems. Draft PR #6 is therefore grounded in a real source, but generalized undecidability is not evidence about the standard map.

10. **Almost-all results do not address the construction target.** Everett's almost-every descent theorem and Tao's logarithmic-density almost-boundedness theorem are essential context. Neither constructs a divergent orbit, rules out a particular 2-adic survivor, or closes a finite-boundary grammar.

## Verdict vocabulary

- **KNOWN — EXACT:** the located source proves essentially the same statement after notation changes.
- **KNOWN — COROLLARY:** the repository statement follows by a short supplied derivation.
- **PARTIAL OVERLAP:** a load-bearing component is known, but the full native statement is not imported.
- **FOLKLORE / STANDARD:** elementary or standard; a proof is supplied where useful.
- **POSSIBLY NOVEL FORMULATION:** no exact antecedent was located after a documented targeted search. This is not a novelty claim.
- **UNVERIFIED:** source attribution or exact theorem match was not confirmed.
- **MISAPPLIED / HYPOTHESES FAIL:** the cited theorem does not justify the native inference as written.
- **INTERNAL EXACT COMPUTATION:** a repository computation, not a literature theorem.

## Package map

- [`literature/SOURCE_LEDGER.md`](literature/SOURCE_LEDGER.md) — only located sources, with inspection level.
- [`literature/CLAIM_CROSSWALK.md`](literature/CLAIM_CROSSWALK.md) — internal branch overlap and provenance.
- [`literature/APPLICABILITY_AUDITS.md`](literature/APPLICABILITY_AUDITS.md) — automaticity, SML, Fatou, Mahler, Fourier, and rigidity boundary checks.
- [`literature/UNVERIFIED.md`](literature/UNVERIFIED.md) — honest gaps and searches that did not produce an exact antecedent.
- [`literature/claim-maps/PR3.md`](literature/claim-maps/PR3.md) and [`CLAUDE.md`](literature/claim-maps/CLAUDE.md) — claim-by-claim verdicts against the live branches.
- [`literature/imported-theorems/`](literature/imported-theorems/) — atomic statements, proofs, black-box boundaries, and non-applications.
- [`literature/topic-notes/`](literature/topic-notes/) — reusable research maps for active questions.
- [`literature/references.bib`](literature/references.bib) — verified bibliographic records.
- [`literature/check_literature.py`](literature/check_literature.py) — mechanical integrity checks for the suite.

## Immediate native-claim actions recommended

1. Replace the external-input annotation on `CLAUDE/T-0003` with separate dependencies:
   `LIT-KTHM-0004` (transcendental slope), `LIT-KTHM-0005` (automatic frequencies), and `LIT-KTHM-0006` (primitive-substitution frequencies). Do not cite the two-base Cobham theorem for the frequency step.
2. Add the exact power-sum coefficients and degeneracy check to `CLAUDE/T-0006`; until then the verdict is **KNOWN — COROLLARY, reduction pending audit**.
3. Use `LIT-KTHM-0003` to complete the general proof in `CLAUDE/T-0019` and the subgroup statement in `CLAUDE/L-0013`.
4. Replace the “Kronecker criterion” sentence in `SKELETON.md` with `LIT-KTHM-0007` and explicitly choose a minimal noncancelling exponential-polynomial representation.
5. Change “Li–Sahlsten / Solomyak apply to exactly this shape” in `MINIMAL.md` to “provide nearby stationary real models; direct applicability is open.”
6. Preserve `PR3/T-0005` as repository mathematics with verdict **POSSIBLY NOVEL FORMULATION**; cite Terras/Everett for the parity substrate and Applegate–Lagarias only as a contrast with backward-tree counting.

No statement in this package resolves or refutes the Collatz conjecture.
