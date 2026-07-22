# Agent report — wave-5 recurrence cone and Dubickas bridge

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-22

## Requested objective

Continue the ordinary-section attack after reading:

- `LITERATURE.md`;
- `literature/LIVE_REPO_REVIEW_WAVE5.md`;
- the newest `gpt56-pro-03` guidance associated with PR #16 / issue #15.

The requested emphasis was to use that advice rather than continue an obsolete real-cylinder route.

## 1. Literature advice absorbed

Wave 5 makes four load-bearing points for PR #16:

1. `T-9315` is a serious exact reformulation, but the real error language is a full shift.
2. The arithmetic object is the appended nearest-integer block
   \[
   R_{K+1}=R_K+q_K64^K.
   \]
3. The full Dubickas 2006 and 2008 formulas must be specialized at `(81,64)` and radius `1/81`.
4. The extremal Thue--Morse sign word must be translated into the native `q_K` recurrence, rather than discussed only as a real symbolic word.

The review also warns that abstracts do not expose the exact source constants, endpoint conventions, equality cases, or rational/irrational scope.

## 2. New native theorem: recurrence cone

`T-9316` derives a global repeated-factor bound for every nontrivial ordinary itinerary.

Let

\[
\delta=\log_{64}(81/64).
\]

If equal length-`ell` factors have second start `t`, then

\[
\boxed{
\ell<\delta t+\log_{64}A_0.
}
\]

This follows by combining:

- `L-9311`'s local orbit-difference zero-carry bound;
- the ordinary tail growth estimate `A_r<=(81/64)^rA_0`.

Therefore any itinerary with repeated factors satisfying

\[
\ell_j-\delta t_j\to+\infty
\]

cannot select an ordinary positive cylinder.

## 3. Sharpened Thue--Morse block nonstabilization

The Thue--Morse fixed point begins

```text
01101001...
```

and has `11` at zero-based positions `1,2`. Applying the length-two morphism `m` times gives equal adjacent blocks of length `2^m` with second start `2*2^m`.

Hence

\[
\ell_m-\delta t_m=(1-2\delta)2^m.
\]

The coefficient is positive because

\[
81^2<64^3.
\]

Thus every finite shift of Thue--Morse, and every complemented shift, violates the ordinary recurrence cone.

By `L-9313` and `L-9314`, this is exactly the arithmetic conclusion

\[
\boxed{
q_K\ne0
\text{ for infinitely many }K.
}
\]

This is the first infinite nonperiodic symbolic family for which the centered nearest-integer block tail is proved not to stabilize.

The sharper witness supersedes the initially recorded `00` occurrence at positions `5,6`; that earlier witness was valid but unnecessarily weak.

## 4. Bounded-distortion source recodings

`L-9315` extends the recurrence obstruction through non-erasing morphic encodings.

If a morphism has output lengths in `[a,b]`, then a repeated source factor of length `ell` and second start `t` yields an equal output factor with

\[
L\ge a\ell,
\qquad
T\le bt.
\]

For Thue--Morse, ordinary stabilization is excluded whenever

\[
\boxed{
\frac ba
<
\frac1{2\log_{64}(81/64)}
=8.8274237885\ldots.
}
\]

Thus all codings, complemented codings, finite shifts, and every non-erasing binary morphism with image-length distortion at most `8` remain excluded.

This removes most sign-convention sensitivity from the Dubickas bridge. A finite-state transducer is not silently treated as a morphism and still needs a synchronization argument.

## 5. Source threshold/equality bridge

`T-9317` freezes the exact source logic.

Suppose an external theorem proves

\[
\limsup_n\|\xi(81/64)^n\|\ge\rho.
\]

Then:

```text
rho > 1/81
  -> immediate nonexistence;

rho = 1/81
  -> equality-language audit;
     efficient recurrence and bounded-distortion Thue--Morse recodings
     are excluded by T-9316/L-9315;

rho < 1/81
  -> record the exact deficit and prove arithmetic stabilization
     supplies the missing gain.
```

A strict source inequality is therefore not the only successful outcome. A critical equality theorem plus a classified extremal language is also decisive.

## 6. Conditional source pre-audit

The full Dubickas 2006 formula remains unavailable in the repository.

A later primary-source discussion gives the integer-base Thue--Morse function

\[
E(x)=\frac{1-(1-x)\prod_{j\ge0}(1-x^{2^j})}{2x},
\]

and the published `3/2` endpoint numerically matches

\[
E(2/3)/3=0.2381175584\ldots.
\]

This strongly suggests, but does not verify, the rational candidate

\[
\rho_{p,q}^{\rm cand}=E(q/p)/p.
\]

`DUBICKAS_SPECIALIZATION_PREAUDIT.md` evaluates that candidate rigorously at `(81,64)`:

\[
0.00774716383883335309
<
\rho_{81,64}^{\rm cand}
<
0.00774716383883335835.
\]

This is below

\[
1/81=0.0123456790\ldots,
\]

with conditional deficit approximately

\[
0.00459851517351232.
\]

If the full source confirms this normalization, the scalar large-limit constant alone will not close the ordinary section. The useful source content would then be its extremal/near-extremal word structure or the 2008 two-interval geometry.

The candidate formula remains explicitly labeled unverified until the full theorem is obtained.

## 7. Exact finite audit

`X-9305` checks through appended block index `1024`:

- the exact nearest-integer cylinder recurrence;
- the exact appended block formula;
- direct residue reconstruction at frozen checkpoints;
- the sharpened morphic square witnesses at starts `1*2^m` and `2*2^m`.

Frozen result:

```text
blocks checked   = 1024
nonzero blocks   = 1005
zero blocks      = 19
longest zero run = 1
```

Digest:

```text
c5a7bfb2cc674c5aba9ada80f291d69c79a2a4151d2eba22c784ea3ae64b59dc
```

The finite audit is not a proof dependency.

## 8. Files added

- `research/adelic-cusp/claims/T-9316-efficient-recurrence-thue-morse.md`
- `research/adelic-cusp/claims/L-9315-bounded-distortion-morphic-recurrence.md`
- `research/adelic-cusp/claims/T-9317-threshold-equality-source-bridge.md`
- `research/adelic-cusp/DUBICKAS_SPECIALIZATION_PREAUDIT.md`
- `experiments/X-9305-thue-morse-blocks/run.py`
- `experiments/X-9305-thue-morse-blocks/README.md`
- `experiments/X-9305-thue-morse-blocks/results/canonical.json`
- this report

Updated:

- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/claims/Q-9303-centered-cylinder-nonstabilization.md`
- PR #16 metadata and discussion handoffs

## 9. Reframed highest-value path

The probable scalar source constant appears subcritical. The highest-value native target is therefore a **near-extremal recurrence theorem**:

> Show that every actual nearest-integer orbit remaining inside the radius `1/81` strip must contain efficient repeated factors, or must shadow a classified source extremal at enough scales to force such factors.

That would combine:

1. Dubickas word optimization;
2. `T-9316`'s recurrence cone;
3. `L-9315`'s robustness under symbolic recoding;
4. `L-9314`'s appended arithmetic blocks;
5. the fixed ordinary starting room.

The parallel determinant route remains viable: couple several shifted tails so that a long zero block tail creates large `2`-adic order while centered errors control the real size.

## 10. Status boundary

- `T-9316`, `L-9315` are `PROPOSED`.
- `T-9317` is `PROPOSED / CONDITIONAL`.
- `X-9305` is bounded empirical replay.
- The candidate Dubickas formula is not source-verified.
- A broad nonperiodic extremal family is excluded; the full ordinary section remains open.
- No positive survivor, divergent Collatz seed, nontrivial cycle, or resolution is claimed.
