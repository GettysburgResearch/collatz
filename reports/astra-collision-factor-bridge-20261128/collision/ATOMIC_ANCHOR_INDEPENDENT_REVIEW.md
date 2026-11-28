# Independent review: atomic-anchor majorant obstruction

Reviewer: collision lower-bound lane. Reviewed UTC: 2026-11-28T10:46:33.454073+00:00.

Source: `research/astra-collision-factor-bridge-20261128/arithmetic/ATOMIC_ANCHOR_MAJORANT_OBSTRUCTION.md`.

SHA-256: `f7b4a61fc92082e5c4fd28098f36272f8e5183b3750480a22541d4eb62bb2a0a`.

**Result: the stated theorem passes independent mathematical reconstruction.** This is a self-contained obstruction to the specified certificate class, not a proof of Collatz or an obstruction to all inverse supersolutions. No Lean formalization of the infinite-dimensional theorem is asserted.

## Checked interfaces

1. Every dyadic anchor lies in the ternary integers. Its exclusion from positive odd integers makes every ordinary-target kernel finite, and the absolute denominator-height moment implies both pointwise absolute convergence and a power-sublinear ordinary bound. The inverse branch sum is absolutely convergent because the exponent is below one.
2. The centered transfer identity includes the necessary residue background. On an admissible branch the new valuation is the old valuation plus one; on an inadmissible branch it is zero. The affine maps preserve the anchor class and their geometric exponent weights preserve the stated height moment.
3. The ordinary-to-Haar step is justified here, rather than assumed from countability. Expanding the kernel into nested residue indicators gives a uniform ordinary-average bound dominated by a constant times one plus anchor height to the stated exponent. At each fixed anchor the residue-count rounding error tends to zero, and the remaining Haar tail decays geometrically. The absolute height moment permits exchange of the anchor series with every fixed-cylinder average, also for signed coefficients and the pushed-forward measure.
4. Nonnegative ordinary cylinder averages imply nonnegativity of the corresponding integrable Haar functions. The inverse operator preserves the Haar integral, so the nonnegative supersolution defect is zero almost everywhere. Its bounded residue part creates no convergence issue.
5. A shrinking-ball average, divided by the kernel scale, extracts exactly the atom at its center. The normalized contributions are uniformly bounded against total variation; every other fixed anchor tends to zero. Nonnegative potential therefore forces every atomic coefficient to be nonnegative. Applying the same extraction to the bounded transfer defect gives the atomic measure equation with mass multiplier greater than one. Total mass and nonnegativity force the measure to vanish.
6. The remaining fixed-residue background vanishes: CRT supplies arbitrarily long exponent-one inverse chains ending in any selected residue. Positivity propagates a fixed positive endpoint value backward by an unbounded factor. Nonunit residues vanish directly from the inverse equation.

## Scope retained

The conclusion depends on absolute summability with the explicit height moment and on an integrable ternary kernel. It does not cover a critical kernel, a non-atomic anchor measure, conditionally convergent renormalization, or a canonical ordinary trace outside this representation. In particular it supplies no bound on the independent Green-tail defect.
