# Literature foundations and claim audit

**Agent:** `gpt56-pro-03`  
**Issue:** `#7 — P1 literature audit and imported theorem suite`  
**Snapshot date:** 2026-07-21  
**Status:** first contribution; literature findings do not promote repository claim statuses

This directory is the repository's branch-neutral literature layer. It records only sources that were actually located, distinguishes exact antecedents from analogies, and supplies atomic theorem notes that can be reused without reconstructing external papers or chat history.

The active mathematical workstreams still have colliding claim-ID spaces. Throughout this suite:

- `PR3/...` refers to draft PR #3, branch `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`;
- `CLAUDE/...` refers to issue #4, branch `claude/collatz-migration-math-osr370`;
- `TERM/...` refers to draft PR #6, branch `agent/gpt56-termination-01/5-termination-frontier-port`.

Bare IDs such as `T-0001` are intentionally avoided.

## Executive findings

1. **The finite parity-cylinder infrastructure is classical.** The parity-affine iterate formula, the bijection between length-`L` parity words and residues modulo `2^L`, and the resulting exact loss of one binary digit of agreement per shortcut step are standard consequences of the 1976 work of Everett and Terras. See [KTHM-0001](literature/imported-theorems/KTHM-0001-parity-affine.md), [KTHM-0002](literature/imported-theorems/KTHM-0002-parity-bijection.md), and [KTHM-0003](literature/imported-theorems/KTHM-0003-exact-2adic-tracking.md). [@Everett1976; @Terras1976]

2. **The repository's exact collision-fiber packaging is not located as a named antecedent.** `PR3/T-0001`, `PR3/T-0002`, `PR3/L-0004`, `PR3/T-0003`, `PR3/T-0004`, `PR3/T-0005`, and the specific `64→81` charts use classical parity-cylinder ingredients, but the exact conjugacies, carry pumping, finite-boundary formulation, and signature-tail amplification appear to be repository-internal formulations. The verdict is `POSSIBLY NOVEL FORMULATION`, never “novel theorem.”

3. **One imported valuation theorem resolves three live dependencies.** The exact formulas

   \[
   v_2(81^{4d}-1)=6+v_2(d),\qquad
   \operatorname{ord}_{2^j}(81)=2^{j-4},
   \]

   and

   \[
   v_3(64^n-1)=2+v_3(n),\qquad
   \operatorname{ord}_{81^k}(64)=9\,81^{k-1}
   \]

   follow from elementary lifting-the-exponent arguments. They validate the external arithmetic step used by `CLAUDE/T-0005`, prove the general part left incomplete in `CLAUDE/T-0019`, and imply `CLAUDE/L-0013`. See [KTHM-0004](literature/imported-theorems/KTHM-0004-lte-orders.md).

4. **The nonautomaticity conclusion can be repaired without Cobham.** Cobham's theorem concerns simultaneous recognizability in multiplicatively independent bases; it is not the theorem that says existing symbol frequencies of automatic sequences are rational. A direct finite-state linear-algebra lemma gives the needed rational-frequency obstruction. Thus the frequency-based portion of `CLAUDE/T-0003` has a sound route, but its current attribution to Cobham should be corrected. Gelfond–Schneider establishes transcendence of the specific logarithmic slope, although irrationality alone already suffices for the automatic-frequency contradiction. See [KTHM-0005](literature/imported-theorems/KTHM-0005-automatic-frequency.md) and [KTHM-0006](literature/imported-theorems/KTHM-0006-gelfond-schneider-log-ratio.md). [@Cobham1969; @Niven1956]

5. **Skolem–Mahler–Lech is a valid black box, but the repository application is not yet auditable.** `CLAUDE/T-0006` must display the exact recurrence or power sum, its coefficients, and the nondegeneracy check before finiteness follows. The named theorem exists and is correctly scoped in [KTHM-0007](literature/imported-theorems/KTHM-0007-skolem-mahler-lech.md); the claim-to-theorem reduction remains `UNVERIFIED`. [@Bell2019]

6. **The external step in skeleton rigidity has a clean elementary replacement.** If an integer-coefficient power series is rational, then its reciprocal poles are algebraic integers. The proof in [KTHM-0008](literature/imported-theorems/KTHM-0008-rational-integer-series.md) removes ambiguity around the repository's “Fatou/Kronecker” shorthand and supplies precisely the dependency needed by `CLAUDE/T-0020`. This validates only that imported step, not the full internal theorem.

7. **Mahler's Z-number problem is an analogy, not an equivalence.** The classical problem constrains archimedean fractional parts of `ξ(3/2)^n`; `CLAUDE/Q-0002` constrains digits in a `2`-adic survivor set for `81/64`. The two have a common restricted-orbit shape, but their topologies, state spaces, and carry mechanisms differ. Flatto–Lagarias–Pollington is therefore a useful non-transfer warning, not a theorem about the repository's set. See [the topic note](literature/topic-notes/mahler-z-numbers.md). [@Mahler1968; @FlattoLagariasPollington1995]

8. **Modern Fourier-decay and measure-rigidity results are near misses, not plug-ins.** Li–Sahlsten and Solomyak treat fixed real self-similar measures, while the EQ product is a depth-dependent modular family. Furstenberg, Rudolph, Shmerkin, and Wu concern invariant measures or dimensions of invariant sets; they do not decide membership of one explicit ordinary integer in a `2`-adic coded set. See [Fourier decay](literature/topic-notes/fourier-decay.md) and [measure rigidity](literature/topic-notes/measure-rigidity.md). [@LiSahlsten2022; @Solomyak2021; @Furstenberg1967; @Rudolph1990; @Shmerkin2019; @Wu2019]

9. **The Aaronson–Yolcu attribution is verified and should include Heule.** Yolcu, Aaronson, and Heule prove that termination of their mixed binary–ternary rewrite system is equivalent to the standard Collatz conjecture. `TERM/...` is therefore situated in a genuine exact literature frontier, not merely a thematic analogy. See [KTHM-0012](literature/imported-theorems/KTHM-0012-ayh-rewrite-equivalence.md). [@YolcuAaronsonHeule2023]

10. **No located source or repository claim resolves the Collatz conjecture.** Everett, Terras, Tao, the tree-density literature, and computational verification through `2^71` are strong partial results with sharply limited scopes. [@Everett1976; @Terras1976; @Tao2022; @ApplegateLagarias1995a; @ApplegateLagarias1995b; @KrasikovLagarias2003; @Barina2025]

## Repository navigation

- [Literature workflow and verdict vocabulary](literature/README.md)
- [Verified source ledger](literature/SOURCE_LEDGER.md)
- [Internal claim crosswalk](literature/CLAIM_CROSSWALK.md)
- [PR #3 claim map](literature/claim-maps/PR3.md)
- [Issue #4 claim map](literature/claim-maps/CLAUDE.md)
- [Termination-frontier claim map](literature/claim-maps/TERMINATION.md)
- [Unverified references and reductions](literature/UNVERIFIED.md)
- [BibTeX database](literature/references.bib)
- [Atomic theorem imports](literature/imported-theorems/)
- [Topic notes](literature/topic-notes/)
- [Validation script](scripts/check_literature.py)

## Immediate recommendations

1. Amend `CLAUDE/T-0003` so that the automatic-frequency lemma, not Cobham, carries the irrational-frequency obstruction. Retain Cobham only for an actual two-base recognizability statement.
2. Add the exact three-term recurrence and coefficient/nondegeneracy audit to `CLAUDE/T-0006`; until then, mark the SML application as externally unresolved.
3. Promote the arithmetic subclaim of `CLAUDE/T-0019` only after an independent reviewer reconstructs [KTHM-0004](literature/imported-theorems/KTHM-0004-lte-orders.md) and maps notation exactly.
4. Replace claims that Li–Sahlsten or Solomyak “apply” to EQ with the narrower statement that their methods motivate a possible strategy after a stationary real-measure reduction is proved.
5. Keep `PR3/T-0005` and related collision-code theorems in a dedicated internal-results category: classical ingredients, no exact external antecedent located.
6. Continue the literature suite by auditing rational cycles, negative cycles, `S`-unit equations, and effective zero bounds; those are the highest-value unresolved connections after this first pass.
