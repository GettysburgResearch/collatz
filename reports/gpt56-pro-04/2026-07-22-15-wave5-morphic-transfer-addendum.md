# Agent report addendum — bounded-distortion morphic source transfer

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-22  
**Parent report:** `2026-07-22-15-wave5-recurrence-source-bridge.md`

## Purpose

The full Dubickas source may encode its Thue--Morse-related extremal sign language through a convention more complicated than literal bit complementation or a finite shift.

This addendum records the native transfer theorem that removes most of that convention sensitivity.

## New `L-9315`

Let an infinite source word `v` contain equal factors of length `ell_j` whose second starts are `t_j`. Let `h` be a non-erasing morphism whose letter images have lengths in

\[
[a,b].
\]

Then the morphic image `h(v)` has equal factors with

\[
L_j\ge a\ell_j,
\qquad
T_j\le bt_j.
\]

Therefore `T-9316` excludes `h(v)` whenever

\[
a\ell_j-\delta b t_j\to+\infty,
\qquad
\delta=\log_{64}(81/64).
\]

For Thue--Morse,

\[
\ell_j=2^j,
\qquad
t_j=6\cdot2^j,
\]

so the sufficient condition is

\[
\boxed{
\frac ba
<
\frac1{6\log_{64}(81/64)}
=2.9424745961\ldots.
}
\]

Thus the following are all excluded from ordinary nearest-integer cylinder stabilization:

- every letter-to-letter coding of Thue--Morse;
- every complemented coding and finite shift;
- every non-erasing binary morphism whose image lengths lie in `{1,2}`;
- any exact source sign encoding with output-length distortion below `2.9424...`.

## Source-audit consequence

The equality-language checklist in `T-9317` no longer needs the source word to be literally the standard binary Thue--Morse fixed point.

Once the full source supplies its exact coding, the native audit is:

```text
1. expose the coding or morphism;
2. compute minimum and maximum image lengths a,b;
3. if b/a < 2.9424745961..., apply L-9315;
4. conclude infinitely many appended q_K blocks are nonzero.
```

If the source uses a finite-state transducer rather than a morphism, an additional synchronization lemma is required; `L-9315` does not silently identify those two models.

## Files

- `research/adelic-cusp/claims/L-9315-bounded-distortion-morphic-recurrence.md`
- updated `research/adelic-cusp/CLAIMS.md`
- this addendum

## Status boundary

- `L-9315` is `PROPOSED` pending independent reconstruction.
- No exact Dubickas coding is asserted before full-source acquisition.
- Exclusion of a broad extremal family is not an all-itinerary nonintersection theorem.
- No ordinary survivor, Collatz counterexample, cycle, or resolution is claimed.
