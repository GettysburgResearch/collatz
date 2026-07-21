# Literature audit — waves 1 and 2

**Agent:** `gpt56-pro-03`  
**Issue:** `#7 — P1 literature audit and imported theorem suite`  
**Status:** citation and applicability audit; no native theorem is promoted by this package

This is the repository's durable external-results layer. It remains namespaced because active branches still use colliding native claim identifiers.

- `CLAUDE/...` refers to the issue-#4 symbolic-rewrite branch.
- `PR3/...` refers to draft PR #3.
- `TERM/...` refers to draft PR #6.
- `PING/...` refers to draft PR #11.
- `REG/...` refers to draft PR #12.
- `LIT-KTHM-####` identifies an imported theorem and never replaces a native claim ID.

## Wave 1 — foundational audit

1. Terras and Everett supply the classical parity-cylinder affine formula, parity-word/residue bijection, and exact loss of one dyadic digit per common-parity step.
2. No exact printed antecedent was located for the repository's sparse forward collision-fiber packaging, carry pumping, or signature-tail amplification. These remain `POSSIBLY NOVEL FORMULATION`, never proved novel.
3. The automaticity obstruction should use rational letter frequencies of automatic sequences, not the famous two-base Cobham theorem. Gelfond–Schneider supplies the transcendental slope, but does not imply “exactly Sturmian/Ostrowski.”
4. Skolem–Mahler–Lech applies to the stated three-base power sum only after the native coefficients, nondegeneracy, and exact-equality reduction are exposed.
5. LTE proves all-level multiplicative orders for `64 mod 81^k` and `81 mod 2^j`.
6. Skeleton rigidity should use the integral-recurrence/Fatou–Pólya algebraic-integrality principle with a minimal noncancelling representation.
7. Mahler is a useful `2`-adic analogy, not a classical equivalence; FLP's real interval-width theorem does not transfer by Haar-measure comparison.
8. Li–Sahlsten, Solomyak, Rudolph, Shmerkin, and Wu provide nearby methods/object classes, not direct theorems for EQ or one integer in `V∞`.
9. Yolcu–Aaronson–Heule is verified; Conway/Kurtz–Simon undecidability concerns generalized maps.
10. Everett/Tao almost-all results are context, not explicit counterexample constructions.

## Wave 2 — live portfolio audit

The repository now has six interacting programs: PR #3 negative-return graphs; issue #4 EQ/rigidity; PR #6 rewrite termination; PR #11 ping-pong/cycle/fuel; PR #12 regular sanctuaries; and issues #8/#9 conditioned resonance/compressed cycles.

The common frontier is an **infinite ordinary-integer realization theorem**. Large finite objects, compact completion points, compatible residue prefixes, and decidable fixed-certificate checks are not enough.

Wave 2 adds `LIT-KTHM-0015` through `LIT-KTHM-0027`:

- accelerated affine monoid;
- rational-base address and bounded-tail law;
- positive cycle-mean phase potentials;
- finite clopen-cover obstruction in `Z_p`;
- regularity of subsequential images;
- exact fixed-DFA closure decision;
- greatest finite safety kernel;
- short canonical witness bound;
- exact accelerated cycle equation;
- Minkowski cancellation refutation and corrected separation theorem;
- match-bound scope theorem;
- finite-state tilted transfer bound;
- graph-directed compact-attractor theorem with the ordinary-integer non-application.

### Blocking correctness finding

`PING/T-0104` and `PING/T-0105` are false as stated. For

```text
D0 = {0, 2^L - 1},
E  = {0, 1},
D1 = D0 + 2^L E,
```

one has `R(D0)=0`, while `D1-D1` contains `±1`. The proof omitted cancellation between a large scaled suffix difference and a seed difference. `LIT-KTHM-0024` supplies the corrected sufficient condition

```text
diam(D0) + R(D0) + 1 < 2^L,
```

which must hold at every iterated stage.

## Verdict vocabulary

- **KNOWN — EXACT:** the located source proves essentially the same statement after notation changes.
- **KNOWN — COROLLARY:** the native statement follows by a short supplied derivation.
- **PARTIAL OVERLAP:** a load-bearing component is known, but the full native statement is not imported.
- **FOLKLORE / STANDARD:** elementary or standard; a proof is supplied where useful.
- **POSSIBLY NOVEL FORMULATION:** no exact antecedent was located after a documented search; not a novelty proof.
- **UNVERIFIED:** source attribution or exact theorem match was not confirmed.
- **MISAPPLIED / HYPOTHESES FAIL:** the cited theorem does not justify the native inference as written.
- **INTERNAL EXACT COMPUTATION:** a repository computation, not a literature theorem.

## Package map

- [`literature/LIVE_REPO_REVIEW_WAVE2.md`](literature/LIVE_REPO_REVIEW_WAVE2.md) — live cross-program review and strategy.
- [`literature/SOURCE_LEDGER.md`](literature/SOURCE_LEDGER.md) and [`SOURCE_LEDGER_WAVE2.md`](literature/SOURCE_LEDGER_WAVE2.md) — only located sources, with inspection level.
- [`literature/CLAIM_CROSSWALK.md`](literature/CLAIM_CROSSWALK.md) — internal branch overlap.
- [`literature/APPLICABILITY_AUDITS.md`](literature/APPLICABILITY_AUDITS.md) — automaticity, SML, Fatou, Mahler, Fourier, and rigidity checks.
- [`literature/UNVERIFIED.md`](literature/UNVERIFIED.md) — honest gaps.
- [`literature/claim-maps/`](literature/claim-maps/) — branch-qualified verdicts for every active program.
- [`literature/imported-theorems/`](literature/imported-theorems/) — 27 atomic statements/proofs/black-box boundaries.
- [`literature/topic-notes/`](literature/topic-notes/) — reusable research maps.
- [`literature/references.bib`](literature/references.bib) and [`references-wave2.bib`](literature/references-wave2.bib) — bibliographic records.
- [`literature/check_literature.py`](literature/check_literature.py) — mechanical integrity checks.

## Process recommendation pending owner approval

Add a short README section establishing imported-theorem IDs, inspection levels, separation of source theorem/native reduction/analogy, and mandatory narrowing or `REFUTED` status after a concrete review counterexample. Keep the fast-changing program dashboard in a separate `RESEARCH_INDEX.md`, not the stable README.

No statement in this suite resolves or refutes the Collatz conjecture.