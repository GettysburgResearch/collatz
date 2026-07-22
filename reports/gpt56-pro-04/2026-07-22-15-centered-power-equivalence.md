# Agent report — centered rational-power equivalence

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-22

## Objective

Complete and document the uncommitted observation that the ordinary `64 -> 81` section is equivalent to one critical nearest-integer orbit, then use the rest of the repository to reframe the next proof attempt.

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

The reconstruction is explicit. If

\[
\xi(N/M)^n=B_n+u_n
\]

with `B_n` nearest integer, then

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
\varepsilon_n-\varepsilon_{n+1}.
\]

For `M=64,N=81`, the ordinary section is nontrivial exactly when

\[
\exists\xi>0:
\|\xi(81/64)^n\|\le1/81
\quad\forall n.
\]

## 2. Proof-critical points

The converse required four checks that were not optional:

1. **Nearest integers are unique.** The radius `1/N` is below `1/2`.
2. **No centered error is zero.** If one power were an integer, the critical bound at all later powers would force divisibility by every power of `M`.
3. **The carry sign table is exact.** Its magnitude is below `2`, and same-sign nonzero carries violate the endpoint bounds.
4. **The reconstructed orbit is nontrivial.** A reconstructed state `1` would remain `1`, forcing the positive centered error to expand beyond its strip.

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

which records whether the binary itinerary keeps or changes sign. The problem is therefore graph-directed rather than a union-of-intervals problem.

## 4. Exact replay

Added `X-9304`.

It checks all binary words through depth `8`, using exact fractions and integers:

- `494` nontrivial finite survivor words;
- `3,514` centered trace checks;
- `3,020` carry and scheduled-phase checks;
- exact survivor replay;
- ceiling reconstruction;
- nearest-integer reconstruction;
- sign-to-digit recovery;
- residue states `0,15,49`;
- all four `3/2` phase neighborhoods.

Frozen digest:

```text
e287cbf70c55adbbdfe3ae4296fc8836f424b2ca48ddda03830235b46f952a2f
```

## 5. Relationship to the prior fixed-room theorem

`T-9313` coupled the past, future, and room quotient through

\[
81^jA=64^jA_j+P_j.
\]

`T-9315` diagonalizes the same recurrence:

\[
A_j-x_j=64\xi(81/64)^j.
\]

The ordinary state is the ceiling of this eigenmode and the real companion is its ceiling error. Thus the finite-versus-adic issue is fully removed once a positive centered parameter is given.

## 6. Literature and repository crosswalk

The literature packet correctly warned against identifying the survivor problem with Mahler's classical one-sided interval problem. The new theorem changes the relationship from analogy to an exact **centered** problem, but the scope warning remains:

- the critical set is two arcs around the circle origin;
- the complete `3/2` orbit has a four-phase schedule;
- the arc choices follow a three-state graph;
- no imported range theorem currently matches this exact target.

PR #20's active-cylinder theorem supplies the best arithmetic parallel: ordinary closure is eventual termination of nested cylinder blocks. PR #19's H-frontier similarly identifies eventual zero carry as the ordinary-versus-adic boundary. The centered error sequence gives a common real normalization for these stabilization problems.

## 7. Reframed highest-value path

The next proof should not return to raw factor complexity or another finite minimum scan. It should construct the exact graph-directed pullback operator for the three residue states.

For each state and each four-phase block:

1. start with the critical interval around an integer;
2. multiply successively by `3/2`;
3. require membership in the scheduled target neighborhoods;
4. enforce the next residue state through the centered carry;
5. pull the surviving interval back to the preceding block.

A proof that every nonzero branch loses all interval length—or that every nested cylinder eventually misses the real line—would show

\[
\mathcal Z^{\rm ctr}_{64,81}=\varnothing
\]

and close the ordinary section by `T-9315`.

## 8. Files added

- `research/adelic-cusp/claims/T-9315-centered-rational-power-equivalence.md`
- `research/adelic-cusp/claims/L-9312-four-phase-three-halves-schedule.md`
- `research/adelic-cusp/CENTERED_POWER.md`
- `experiments/X-9304-centered-power-replay/run.py`
- `experiments/X-9304-centered-power-replay/README.md`
- `experiments/X-9304-centered-power-replay/results/canonical.json`
- this report

## 9. Status boundary

- `T-9315`, `L-9312`: `PROPOSED`.
- `X-9304`: bounded exact-interface audit.
- No positive centered parameter or ordinary survivor is produced.
- No nonexistence theorem is claimed.
- No claim about every possible Collatz counterexample is made without the separate chart translation.
