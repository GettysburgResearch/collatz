# Centered rational powers and the ordinary section

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Status:** theorem-level claims `PROPOSED`; finite replay `EMPIRICAL`; no counterexample claimed

## 1. Executive reformulation

The ordinary-section problem for the binary `64 -> 81` subsystem is exactly the critical centered rational-power problem

\[
\boxed{
\mathcal Z^{\rm ctr}_{64,81}
=
\left\{
\xi>0:
\left\|
\xi\left(\frac{81}{64}\right)^n
\right\|
\le\frac1{81}
\quad\forall n\ge0
\right\}.
}
\]

`T-9315` proves

\[
\boxed{
\Phi(\{0,1\}^{\mathbb N})
\cap
\mathbb Z_{\ge2}
\ne\varnothing
\iff
\mathcal Z^{\rm ctr}_{64,81}
\ne\varnothing.
}
\]

This is an exact bijection, not merely a necessary condition and not merely a structural analogy to Mahler's problem.

Given a centered parameter, the complete ordinary orbit is reconstructed by

\[
\boxed{
A_n
=
\left\lceil
64\xi\left(\frac{81}{64}\right)^n
\right\rceil.
}
\]

Its binary chart digit is

\[
\boxed{\varepsilon_n=A_n\bmod64\in\{0,1\},}
\]

and the bounded real companion is

\[
\boxed{
x_n=A_n-64\xi(81/64)^n\in(0,1).}
\]

Conversely, every nontrivial ordinary survivor produces exactly one positive centered parameter

\[
\boxed{\xi=(A_0-x_0)/64.}
\]

Thus symbolic novelty, integral tails, the bounded real coordinate, and the affine carry law are four coordinate descriptions of one nearest-integer orbit.

## 2. The nearest-integer cocycle

Write

\[
\xi(81/64)^n=B_n+u_n,
\qquad
B_n\in\mathbb Z,
\qquad
|u_n|<1/81.
\]

The digit is the sign of the centered error:

\[
\varepsilon_n=\mathbf1_{u_n>0}.
\]

The adjacent errors satisfy the exact integral relation

\[
\boxed{
81u_n-64u_{n+1}
=64B_{n+1}-81B_n
=\varepsilon_n-\varepsilon_{n+1}.
}
\]

The carry belongs to `{-1,0,1}`. Its sign records whether the itinerary changes from `1` to `0`, stays fixed, or changes from `0` to `1`.

This is the direct real counterpart of the integral phase carries in `L-9310` and the orbit-difference carries in `L-9311`.

## 3. Why the equivalence is stronger than fixed-room coherence

`T-9313` expresses an ordinary point as one room quotient preserved across every past/future split:

\[
81^jA=64^jA_j+P_j.
\]

The centered-power theorem diagonalizes this recurrence. The quantity

\[
A_n-x_n
\]

is a pure expanding eigenmode:

\[
A_n-x_n
=64\xi(81/64)^n.
\]

The nearest-integer decomposition of that eigenmode recovers both the ordinary state and the symbolic digit. Hence no separate inverse-limit stabilization argument is required once `xi` exists.

The remaining question is entirely real and arithmetic:

> Can a positive rational-power orbit remain within centered distance `1/81` of the integers forever?

## 4. Fourth-power structure

The multiplier is

\[
\frac{81}{64}
=\left(\frac32\right)^4.
\]

`L-9312` therefore expands the centered condition into a schedule for the complete `3/2` orbit

\[
Y_m=\xi(3/2)^m.
\]

At phases `m=4n+r`, the allowed neighborhoods are

\[
\begin{array}{c|c|c}
r&\text{centers modulo }1&\text{radius}\\
\hline
0&0&1/81\\
1&0,\ 1/2&1/54\\
2&0,\ 1/4,\ 3/4&1/36\\
3&0,\ 3/8,\ 5/8&1/24.
\end{array}
\]

The center choice is not independent. If `B_n` is the nearest integer at phase `4n`, then

\[
B_n\pmod{64}
\in\{0,15,49\},
\]

with the exact transition interpretation

\[
\begin{array}{c|c}
B_n\pmod{64}&(\varepsilon_n,\varepsilon_{n+1})\\
\hline
0&(0,0)\text{ or }(1,1)\\
15&(1,0)\\
49&(0,1).
\end{array}
\]

The natural object is therefore a three-state graph-directed shrinking-target system for multiplication by `3/2`.

## 5. Relationship to the finite minimum program

`T-9313` and `T-9314` study

\[
M_j=\min(R_j\setminus\{0,1\}).
\]

The centered-power formulation gives a parallel finite object. A depth-`j` survivor prefix corresponds to a finite centered trace

\[
\left\|\xi(81/64)^n\right\|<1/81,
\qquad
0\le n<j,
\]

with starting room

\[
A_0=\lceil64\xi\rceil.
\]

Thus the exact depth-46 minimum certificate can be read as a lower bound on the first ceiling value of every length-46 centered trace compatible with a survivor word.

The infinite ordinary-section problem remains equivalent to

\[
M_j\longrightarrow\infty,
\]

or, in centered language, to emptiness of the infinite nested scheduled cylinders for every `xi>0`.

## 6. Literature boundary

The repository's Mahler/FLP audit remains important but changes role.

Before `T-9315`, Mahler's problem was only an analogy for the tension between rational expansion and a compact digit restriction. After `T-9315`, the repository has an exact centered rational-power problem. It is still not the classical one-sided problem:

- the trapping set at phase zero is two arcs meeting at the circle origin;
- the full `3/2` orbit follows a four-phase schedule;
- the permitted centers form a three-state transition graph;
- the critical radius is exactly `1/81`.

No theorem presently imported as `LIT-KTHM-####` is claimed to exclude this scheduled centered system. A theorem about the width of one interval, generic parameters, or Haar-almost-every points cannot be substituted for the required individual-orbit statement.

## 7. Exact finite replay

`X-9304` checks the theorem interfaces with exact fractions and integers.

Frozen scope:

- all binary words through depth `8`;
- `494` nontrivial finite survivor words;
- `3,514` centered trace reconstructions;
- `3,020` carry and scheduled-phase checks;
- no floating-point arithmetic;
- no random sampling.

Replay:

```bash
python3 -B -m py_compile experiments/X-9304-centered-power-replay/run.py
python3 -B experiments/X-9304-centered-power-replay/run.py \
  --check-results \
  experiments/X-9304-centered-power-replay/results/canonical.json
```

Frozen SHA-256:

```text
e287cbf70c55adbbdfe3ae4296fc8836f424b2ca48ddda03830235b46f952a2f
```

The replay is an interface audit, not a proof dependency.

## 8. Reframed proof program

### Route A — graph-directed interval pullback

For each state `s in {0,15,49}`, write the exact four-phase interval transition under multiplication by `3/2`. Pull the target arcs backwards and intersect with the source arc.

A universal nonexistence theorem would follow if every infinite state path has empty nested intersection, or if the only surviving intersection is `xi=0`.

### Route B — scheduled range theorem

Prove a Flatto--Lagarias--Pollington-type range obstruction adapted to:

- a periodic family of target unions;
- state-dependent transitions;
- the fixed rational multiplier `3/2`;
- one individual orbit rather than an average statement.

The total length of the unions is not the correct invariant. The transition graph and cyclic order of the arcs are load-bearing.

### Route C — integer nearest-point dynamics

Use

\[
64B_{n+1}-81B_n
\in\{-1,0,1\}
\]

with the residue restriction

\[
B_n\pmod{64}\in\{0,15,49\}.
\]

This is an expanding nearest-integer recurrence with only three admissible residue states. A proof that every positive orbit eventually leaves the critical error strip would close the ordinary section directly.

### Route D — cross-program cylinder stabilization

PR #20 reduces active stack closure to eventual zero of appended cylinder blocks. The centered errors `u_n` provide a canonical real normalization of an ordinary nested cylinder.

The next cross-program lemma should identify a vanishing block tail with eventual periodicity or a zero centered error, both impossible for a positive centered orbit.

## 9. Status boundary

- `T-9315` and `L-9312` are `PROPOSED`.
- `X-9304` is a bounded exact-interface audit.
- No centered parameter is constructed.
- No nonexistence theorem for the centered set is proved.
- No universal lower bound for every Collatz counterexample is claimed.
- The exact issue-#4 chart translation remains separate.
