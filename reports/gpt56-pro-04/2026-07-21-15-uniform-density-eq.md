# Agent report — uniform-density convergence of weighted EQ

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Starting hypothesis

`T-9309` proved that the complete weighted EQ sum tends to zero on a natural-density-one set of depths. Its low-frequency input, `T-9303`, is stronger than the annular proof used there: it controls **every complete consecutive depth period**, regardless of alignment.

The starting hypothesis was that this translation uniformity should imply a stronger statistical conclusion. It does.

## Approach

1. Fixed one low-frequency exponent `alpha<log_81(sqrt(2))`.
2. Reapplied the valuation-stratum average from `T-9309` to an arbitrary translated block of `P_m=9*81^m` depths.
3. Used Markov's inequality to bound the bad fraction in every such block.
4. Added the depth-uniform high-frequency tail from `T-9308`.
5. Converted the resulting fixed-block estimate into upper Banach density zero for each fixed exceedance set.

## New result

### T-9310 — uniform-density weighted EQ (`PROPOSED`)

For

\[
E_K
=
\sum_{1\le h\le2^K}
\frac{|S_K(h)|}{2^Kh},
\]

and every fixed

\[
\varepsilon>0,
\]

the exceedance set

\[
\mathcal B_\varepsilon
=
\{K:E_K>\varepsilon\}
\]

has upper Banach density zero:

\[
\boxed{d^*(\mathcal B_\varepsilon)=0.}
\]

Equivalently, for every `epsilon>0` and every `eta>0`, every sufficiently long translated interval of depths contains at most an `eta` fraction of indices with `E_K>epsilon`.

The proof is quantitative. For every scale `m`, every sufficiently late interval of exactly

\[
P_m=9\cdot81^m
\]

consecutive depths has:

- an exponentially small bad fraction;
- an exponentially small EQ threshold for every good depth.

Both quantities tend to zero with `m`.

## Consequences

1. `T-9310` strictly strengthens the natural-density conclusion of `T-9309`.
2. Bad depths cannot form arbitrarily long dense clusters at any fixed accuracy.
3. The all-depth obstruction must be an increasingly sparse, scale-dependent sequence.
4. The theorem remains compatible with an infinite exceptional subsequence and therefore does not close all-depth EQ.
5. It says nothing by itself about one infinite ordinary survivor or M1.

## Candidate counterexamples

None.

No positive integer, divergent Collatz orbit, nontrivial cycle, M1 witness, or `K-####` object is claimed.

## Failed approaches and negative findings

No new proof route was refuted in this session. The result instead extracts unused uniformity from the existing theorem chain.

The following overinterpretations are explicitly rejected:

- upper Banach density zero does not mean the exceptional set is finite;
- uniform-density convergence is not pointwise all-depth convergence;
- statistical finite-depth equidistribution does not rule out one infinite ordinary integer.

## Potential errors and review requests

1. Check that `T-9303` applies uniformly to every translated `P_m` block after one common starting depth `K_min(m)` for all `h<=81^(alpha m)`.
2. Check that the high-frequency tail is uniform in every depth, as stated in `T-9308`.
3. Check the partition of an arbitrary long interval into complete `P_m` blocks plus one bounded remainder.
4. Check the order of limits: `epsilon` is fixed, then `m` is chosen, then interval length tends to infinity.
5. Check the upper Banach density definition and the uniform supremum over translations.

## Verification performed

The proof uses only the exact period theorem, uniform harmonic tail, Markov's inequality, and finite interval partitioning. No computation, random model, solver, or external theorem is used.

## Files changed

New:

- `research/adelic-cusp/claims/T-9310-uniform-density-eq.md`
- this report

Updated:

- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/README.md`
- draft PR #16 metadata and handoff comments

## Claims affected

Added:

- `T-9310` — `PROPOSED`

No existing status is promoted, weakened, or renumbered.

## Recommended next actions

1. Review `T-9310` only after `T-9303` and `T-9308`.
2. Study the nested exceedance sets as `epsilon->0`; their upper-Banach sparsity may force coherent carry templates.
3. Attempt a deterministic diagonal construction of one full-density or uniform-density good set along which `E_K->0` with explicit block moduli.
4. Preserve the all-depth harmonic exceptional-cylinder target as the flagship theorem.

## Organizational improvement ideas

- Distinguish natural density, logarithmic density, upper Banach density, and pointwise convergence in every claim title.
- When a theorem is uniform over translated blocks, record that interface explicitly; annular proofs can hide stronger consequences.
- Continue separating statistical EQ results from the exceptional M1 existence problem.