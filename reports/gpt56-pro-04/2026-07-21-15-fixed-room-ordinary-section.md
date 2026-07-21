# Agent report — fixed-room ordinary-section theorem attempt

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Requested objective

Attempt the decisive theorem that no infinite itinerary can simultaneously:

1. supply the symbolic novelty required by ordinary-code repetition rigidity;
2. preserve ordinary integrality at every shift;
3. remain in the bounded real companion section;
4. avoid both repetition-height and reciprocal carry-height contradictions.

The session pushed the argument as far as the current exact interfaces support.

## 1. First attempted synthesis: compare the two criticality constants

PR #20 proves a repetition/factor-complexity obstruction with

\[
\kappa
=
\frac1{\log_{64}81-1}.
\]

PR #16 proves a reciprocal phase-carry obstruction with

\[
\kappa
=
\frac{\log64}{\log(81/64)}.
\]

These are the same number. The initial hypothesis was that the ordinary itinerary might be forced to spend more than one binary bit budget by satisfying both constraints.

That hypothesis does not survive exact reconstruction.

## 2. New exact result: repetition is an orbit-difference zero-carry chain

Let `A_k` be the ordinary integral tail orbit of a hypothetical survivor. If two length-`ell` factors begin at `r<t`, define

\[
D_i=A_{r+i}-A_{t+i}.
\]

During the common factor, subtracting the two tail recurrences gives

\[
64D_{i+1}=81D_i.
\]

Hence

\[
D_i=64^{\ell-i}81^iu
\]

for one nonzero integer `u`. The repeated factor is exactly a zero-carry chain in an integral difference cocycle.

The local height bound follows immediately:

\[
64^\ell
\le A_t-A_r
<
(81/64)^{t-r}A_r,
\]

so

\[
\ell
<
(\log_{64}81-1)(t-r)+\log_{64}A_r.
\]

This independently reconstructs PR #20's local repetition theorem and explains the identical criticality constant.

### Methodological conclusion

The repetition and reciprocal-carry inequalities are not opposing constraints. They are two uses of the same completion-height mechanism on different cocycles. High symbolic novelty and many nonzero carries can coexist.

`R-9302` therefore closes the naive numerical comparison route. A final theorem needs a new invariant that couples the two cocycles through the same ordinary point.

## 3. New exact coupling: the fixed-room invariant

For a hypothetical ordinary room

\[
A=\Phi(\varepsilon),
\]

let `A_j` be the ordinary tail after `j` digits and define

\[
P_j
=
17\sum_{t=0}^{j-1}
\varepsilon_t81^{j-1-t}64^t.
\]

Iteration of the tail recurrence gives

\[
\boxed{
81^jA=64^jA_j+P_j.
}
\]

This quotient is the same fixed integer `A` at every depth.

Reverse the past word. Its triadic coordinate lies in the depth-`j` class set `C_j`, and

\[
A_j\pmod{81^j}
\]

is exactly that coordinate. The future word simultaneously puts `A_j` in the infinite survivor attractor.

The real companion gives the moving window

\[
(81/64)^j(A-1)+1
\le A_j
\le(81/64)^jA.
\]

Conversely, any coherent sequence of ordinary integers satisfying the fixed-room equation reconstructs the original `2`-adic survivor series. Thus `T-9313` is an exact equivalence, not only a necessary condition.

## 4. Finite certificate theorem

Let

\[
m_j=\min(C_j\setminus\{0,1\})
\]

in standard representatives and define

\[
B_j
=
\min\left\{
64^j,
\left\lceil m_j(64/81)^j\right\rceil
\right\}.
\]

Every nontrivial ordinary survivor satisfies

\[
A\ge B_j
\]

for every depth.

This gives a finite, exact, replayable ordinary-section certificate.

## 5. Exact meet-in-the-middle computation

`X-9303` computes `m_j` as a modular subset-sum minimum. It uses a meet-in-the-middle split, Gray-code subset-sum generation, sorting, and exact nearest-complement search.

The frozen checkpoints reach depth `44`. At that depth,

\[
m_{44}
=
7220252188262239184305599554690421895921563960360483237559093394744562,
\]

and

\[
\boxed{
B_{44}
=
227578060273510610973552811001603322347312502177488333909527505984
>2^{217}.
}
\]

Therefore `T-9314` excludes every nontrivial ordinary survivor room through `2^217`, subject to independent replay.

Frozen digest:

```text
0ae0ccf0df779ffe4dc8b4d2a4f91471033cdf84b47738d9f79d6b7c85f43add
```

## 6. Why the universal contradiction did not close

The remaining asymptotic statement is

\[
B_j\to\infty.
\]

The computation strongly suggests far faster growth, but finite values do not prove it.

The unconditional minimum `m_j` ranges over all past words. A genuine ordinary path is much more constrained: it must be coherent at every earlier depth and admit an infinite future survivor. This suggests that the **coherent** minimum, rather than the full minimum of `C_j`, is the right next object.

No currently proved interface forces its divergence.

## 7. New files

- `research/adelic-cusp/claims/L-9311-orbit-difference-carry-duality.md`
- `research/adelic-cusp/claims/T-9313-fixed-room-past-future-equivalence.md`
- `research/adelic-cusp/claims/T-9314-bounded-ordinary-room-exclusion.md`
- `research/adelic-cusp/claims/R-9302-naive-complexity-carry-incompatibility.md`
- `research/adelic-cusp/ORDINARY_SECTION.md`
- `experiments/X-9303-fixed-room-cantor-minimum/README.md`
- `experiments/X-9303-fixed-room-cantor-minimum/run.py`
- `experiments/X-9303-fixed-room-cantor-minimum/results/canonical.json`
- this report

Updated:

- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/claims/Q-9302-two-place-room-cusp.md`
- PR #16 metadata and cross-program comments

## 8. Claim effects

Added:

- `L-9311` — `PROPOSED`;
- `T-9313`, `T-9314` — `PROPOSED`;
- `R-9302` — `PROPOSED`;
- `O-9303`, `X-9303` — exact finite computation.

No issue-#4 or PR #20 claim is promoted or altered.

## 9. Review priorities

1. Reconstruct the fixed-room identity and converse in `T-9313`.
2. Check the reversed-word indexing in the `C_j` congruence.
3. Check the two-case derivation of `A>=B_j`.
4. Replay `X-9303`, especially the modular wrap and exclusion of classes `0,1`.
5. Reconstruct `L-9311` and confirm that it exactly recovers the local repetition inequality.
6. Confirm that `R-9302` is scoped only to the naive proof route.

## 10. Highest-value next theorem

Define the coherent subset of `C_j` consisting of past classes that:

- survive all predecessor equations;
- admit an integral future tail;
- preserve one fixed room;
- and stay in the critical archimedean window.

Prove that the least nontrivial coherent representative divided by `(81/64)^j` tends to infinity.

That theorem would exclude every fixed ordinary room and close `Q-9301`.

## Status boundary

This session did not prove the universal nonintersection theorem requested. It did prove the strongest exact reduction found, close one misleading incompatibility route, and obtain a new explicit ordinary-section exclusion through `2^217`.

No ordinary survivor, divergent Collatz seed, nontrivial cycle, or resolution is claimed.
