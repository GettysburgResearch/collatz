# Agent report — centered rational-power equivalence

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-22

## Objective

Complete and document the observation that the ordinary `64 -> 81` section is equivalent to one critical nearest-integer orbit, then use adjacent repository programs to identify the exact remaining obstruction.

## 1. Main theorem

For every coprime binary expanding chart `M<N`, define

\[
\mathcal Z^{\rm ctr}_{M,N}
=
\left\{
\xi>0:
\|\xi(N/M)^n\|\le1/N
\text{ for all }n
\right\}.
\]

`T-9315` proves a bijection between this set and nontrivial ordinary integral orbits of

\[
M A_{n+1}=N A_n-(N-M)\varepsilon_n,
\qquad
\varepsilon_n\in\{0,1\}.
\]

If

\[
\xi(N/M)^n=B_n+u_n
\]

with `B_n` the nearest integer, then

\[
\varepsilon_n=\mathbf1_{u_n>0},
\qquad
A_n=M B_n+\varepsilon_n
=\lceil M\xi(N/M)^n\rceil.
\]

The centered carry

\[
N u_n-Mu_{n+1}
\]

is an integer in `{-1,0,1}` and equals

\[
\varepsilon_n-arepsilon_{n+1}.
\]

For `M=64,N=81`, the ordinary section is nontrivial exactly when

\[
\exists\xi>0:
\|\xi(81/64)^n\|\le1/81
\quad\forall n.
\]

## 2. Proof-critical points

The converse required four checks:

1. **Nearest integers are unique.** The radius `1/N` is below `1/2`.
2. **No centered error is zero.** If one power were an integer, the later critical bounds would force divisibility by every power of `M`.
3. **The carry sign table is exact.** Its magnitude is below `2`, and the endpoint cases are excluded.
4. **The reconstructed orbit is nontrivial.** A state `1` would remain `1` and force a positive centered error to expand beyond the strip.

The closed critical inequality is therefore automatically strict for every positive infinite orbit.

## 3. Fourth-power schedule

Because

\[
81/64=(3/2)^4,
\]

`L-9312` derives a schedule for the full `3/2` orbit. At phases modulo four, the orbit lies near

\[
\begin{array}{c|c|c}
r&\text{centers}&\text{radius}\\
\hline
0&0&1/81\\
1&0,1/2&1/54\\
2&0,1/4,3/4&1/36\\
3&0,3/8,5/8&1/24.
\end{array}
\]

The center is controlled by

\[
B_n\pmod{64}\in\{0,15,49\},
\]

which records whether the binary itinerary keeps or changes sign.

## 4. Exact replay

`X-9304` checks all binary words through depth `8`, using exact fractions and integers:

- `494` nontrivial finite survivor words;
- `3,514` centered trace checks;
- `3,020` carry and scheduled-phase checks;
- exact survivor replay;
- ceiling and nearest-integer reconstruction;
- sign-to-digit recovery;
- residue states `0,15,49`;
- all four intermediate `3/2` phase neighborhoods.

Frozen digest:

```text
e287cbf70c55adbbdfe3ae4296fc8836f424b2ca48ddda03830235b46f952a2f
```

## 5. Relationship to fixed-room coherence

`T-9313` coupled the past, future, and room quotient through

\[
81^jA=64^jA_j+P_j.
\]

`T-9315` diagonalizes the same recurrence:

\[
A_j-x_j=64\xi(81/64)^j.
\]

The ordinary state is the ceiling of this eigenmode and the bounded real companion is its ceiling error. Once a positive centered parameter is given, the ordinary orbit is explicit.

## 6. Cross-program correction: the real system is a full shift

The initial proposed next step was to prove that the scheduled real cylinders become empty. Cross-reading PR #20's active cylinders and PR #19's ghost/carry frontier exposed that this is the wrong boundary.

`L-9313` proves that every binary itinerary has a unique bounded real error path

\[
81u_n-64u_{n+1}
=
\varepsilon_n-arepsilon_{n+1},
\qquad
|u_n|\le1/81.
\]

The backward maps are contractions. Therefore the real error system has full symbolic support: no itinerary is eliminated by real interval geometry alone.

`R-9303` records this method closure.

## 7. Exact nearest-integer cylinder

The nearest integers must satisfy

\[
64B_{n+1}
=81B_n+\varepsilon_n-arepsilon_{n+1}.
\]

A prefix through depth `K` selects exactly one class

\[
B_0\pmod{64^K}.
\]

An infinite itinerary selects the `2`-adic point

\[
\boxed{
B_0^*(\varepsilon)
=-\sum_{n\ge0}
(\varepsilon_n-arepsilon_{n+1})
\frac{64^n}{81^{n+1}}.
}
\]

For the `64 -> 81` coding this is also

\[
\boxed{
B_0^*(\varepsilon)
=\frac{\Phi(\varepsilon)-\varepsilon_0}{64}.
}
\]

If `R_K` is the least representative of the depth-`K` cylinder, then the centered itinerary has an ordinary nearest-integer start exactly when `R_K` eventually stabilizes.

Thus `T-9315` does not remove the finite-versus-adic boundary. It gives that boundary a canonical real centered coordinate.

## 8. Literature and repository crosswalk

The literature packet correctly warned against identifying the survivor problem with Mahler's classical one-sided interval problem. The new theorem creates an exact **centered** rational-power problem, but its decisive arithmetic component is an inverse-limit nearest-integer cylinder.

PR #20 supplies the strongest parallel:

- prescribed directives select one `2`-adic point;
- ordinary closure is eventual zero of appended cylinder blocks;
- direct rational truncations can have an exactly subcritical approximation exponent;
- successful Diophantine attacks may require shifted-value determinants or Padé-type cancellation.

PR #19 supplies the phase lesson:

- normalize the finite cylinder by a real phase;
- same-sign behavior may be automatic;
- the new information lies in sign crossings and carry updates;
- ordinary closure is still eventual carry termination.

The centered errors provide a common real normalization of these stabilization problems.

## 9. Reframed highest-value path

The current exact target is `Q-9303`.

For nested least representatives

\[
R_{K+1}=R_K+q_K64^K,
\qquad
q_K\in\{0,\ldots,63\},
\]

prove that every nontrivial itinerary has infinitely many

\[
q_K\ne0.
\]

Promising routes are:

1. derive an exact block-digit recurrence coupling `q_K` to the centered errors;
2. construct a shifted-tail determinant whose real size is controlled by `u_n` and whose `2`-adic order grows under a long zero block tail;
3. prove eventual cylinder stabilization forces periodicity, repeated return words, or another structure contradicted by `L-9311`;
4. use the centered cylinder state to prove divergence of the least extendible finite survivor.

A proof using only real interval pullbacks is explicitly ruled out by `R-9303`.

## 10. Files added or revised

Added:

- `research/adelic-cusp/claims/T-9315-centered-rational-power-equivalence.md`
- `research/adelic-cusp/claims/L-9312-four-phase-three-halves-schedule.md`
- `research/adelic-cusp/claims/L-9313-centered-error-full-shift-cylinder.md`
- `research/adelic-cusp/claims/R-9303-real-cylinder-emptiness.md`
- `research/adelic-cusp/claims/Q-9303-centered-cylinder-nonstabilization.md`
- `research/adelic-cusp/CENTERED_POWER.md`
- `experiments/X-9304-centered-power-replay/run.py`
- `experiments/X-9304-centered-power-replay/README.md`
- `experiments/X-9304-centered-power-replay/results/canonical.json`
- this report

Updated:

- `research/adelic-cusp/CLAIMS.md`
- `L-9312` and `CENTERED_POWER.md` after the full-shift audit.

## 11. Status boundary

- `T-9315`, `L-9312`, and `L-9313`: `PROPOSED`.
- `R-9303`: method refutation, `PROPOSED`.
- `Q-9303`: open decisive interface.
- `X-9304`: bounded exact-interface audit.
- No positive centered parameter or ordinary survivor is produced.
- No nonexistence theorem is claimed.
- No claim about every possible Collatz counterexample is made without the separate chart translation.
