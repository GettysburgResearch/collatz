# Unverified references, reductions, and novelty gaps

An item remains here until a source or complete reduction is actually inspected. “Not found” is not evidence of novelty.

## U-0001 — Exact antecedent for arbitrary collision-fiber conjugacy

- **Targets:** `PR3/T-0001`, `PR3/T-0002`.
- **Searches:** Terras/Everett parity cylinders; Lagarias surveys and bibliography; Bernstein–Lagarias conjugacy; Applegate–Lagarias and Krasikov–Lagarias preimage trees; generalized Collatz literature.
- **Found:** classical affine cylinders, residue/parity bijections, `2`-adic conjugacy, and backward-tree counts.
- **Missing:** a located theorem packaging a finite same-depth affine collision fiber into the exact digit-preserving map `H_D(MB+d)=NB+d` with the repository's invariant positive lift.
- **Verdict:** `POSSIBLY NOVEL FORMULATION`.

## U-0002 — Exact antecedent for universal carry-cycle pumping

- **Targets:** `PR3/L-0004`, `CLAUDE/L-0010`, `CLAUDE/L-0014`.
- **Searches:** mixed-radix conversion, transducers, automatic sequences, string-rewrite Collatz literature.
- **Found:** broad radix-transducer and rewriting frameworks; AYH's distinct mixed-base system.
- **Missing:** the repository's exact horizontal pumping theorem for every closed carry path and its zero-output amplifier corollary.
- **Verdict:** `POSSIBLY NOVEL FORMULATION`.

## U-0003 — SML reduction for unsteered coincidences

- **Target:** `CLAUDE/T-0006`.
- **Located theorem:** Skolem–Mahler–Lech is verified. [@Bell2019]
- **Missing repository data:** a displayed sequence `u_n`, exact coefficients, characteristic roots, index set, and proof that all root ratios associated with nonzero coefficients are not roots of unity.
- **Why this matters:** SML gives finite union of arithmetic progressions in general. Finiteness requires a nondegeneracy argument or a separate exclusion of progressions.
- **Verdict:** `UNVERIFIED` reduction, not a rejection of the theorem.

## U-0004 — Direct applicability of Li–Sahlsten or Solomyak to EQ

- **Target:** `CLAUDE/C-0002`, `CLAUDE/Q-0003`, `MINIMAL.md` language that these results apply to “exactly this shape.”
- **Found:** the cited papers concern fixed probability measures on real self-similar IFSs. [@LiSahlsten2022; @Solomyak2021]
- **Mismatch:** EQ uses a finite, depth-dependent modular product with frequencies restricted relative to the changing modulus; no fixed real stationary measure and no matching parameter theorem has been exhibited.
- **Verdict:** `MISAPPLIED / HYPOTHESES FAIL` if stated as direct application; `PARTIAL OVERLAP` as methodological inspiration.

## U-0005 — Measure-rigidity implication for `V∞∩Z`

- **Target:** `CLAUDE/Q-0005`.
- **Found:** Furstenberg/Rudolph/Shmerkin/Wu results about invariant measures, entropy, closed invariant sets, and Hausdorff dimension. [@Furstenberg1967; @Rudolph1990; @Shmerkin2019; @Wu2019]
- **Missing:** a construction placing the repository's `2`-adic survivor set and its ordinary-integer intersection inside the exact hypotheses, plus a theorem converting a dimension/measure conclusion to exclusion of one integer point.
- **Verdict:** `UNVERIFIED` research direction; no current theorem application.

## U-0006 — “2-adic Mahler equivalence” as a literature claim

- **Target:** `CLAUDE/Q-0002`.
- **Found:** Mahler's archimedean Z-number problem and FLP's range theorem. [@Mahler1968; @FlattoLagariasPollington1995]
- **Mismatch:** the repository problem is `2`-adic and includes a digit-preserving carry map; Mahler's is a real fractional-part orbit.
- **Verdict:** verified **analogy**, unverified as any stronger equivalence to a known named problem.

## U-0007 — Exact literature predecessor of exponential signature-tail fibers

- **Targets:** `PR3/L-0005`, `PR3/L-0006`, `PR3/T-0005`, `PR3/T-0006`.
- **Searches:** parity-vector inversion; tree counting; coding and CRT constructions; preimage-density bounds.
- **Found:** all component tools are classical or elementary.
- **Missing:** the exact theorem separating a large equal-signature class from a common all-odd tail to obtain exponentially many mildly supercritical same-output residues, and the geometry-preserving tensor amplification.
- **Verdict:** `POSSIBLY NOVEL FORMULATION`.

## U-0008 — Original attribution of the rational integer-series lemma

- **Target:** external step in `CLAUDE/T-0020`, called “Fatou/Kronecker.”
- **Found:** Fatou/Pólya–Carlson literature and a modern Fatou-theorem proof. [@BorweinCoons2009]
- **Ambiguity:** the exact short lemma needed by the repository—rational integer Taylor series imply algebraic-integer reciprocal poles—was not located under one unambiguous theorem number in the inspected sources.
- **Resolution in this suite:** [KTHM-0008](imported-theorems/KTHM-0008-rational-integer-series.md) supplies a complete proof, so the mathematics need not depend on the attribution.
- **Verdict:** bibliographic attribution `UNVERIFIED`; theorem proved locally.

## U-0009 — Effective zero bound from SML

- **Targets:** any future computational claim that needs a last possible coincidence index.
- **Found:** qualitative characteristic-zero SML. [@Bell2019]
- **Missing:** an effective bound applicable to the repository's exact sequence.
- **Verdict:** `UNVERIFIED`; ordinary SML is generally not an effective numerical bound in the form cited.

## U-0010 — Current survey covering every 2025–2026 development

- **Searches:** recent Collatz surveys, verified computational work, 2026 preprints.
- **Found:** Barina's 2025 verification paper and Angeltveit's 2026 algorithm preprint. [@Barina2025; @Angeltveit2026]
- **Missing:** one authoritative survey incorporating all current theoretical and computational developments through July 2026.
- **Verdict:** `UNVERIFIED`; use primary sources and date-stamped topic notes instead.
