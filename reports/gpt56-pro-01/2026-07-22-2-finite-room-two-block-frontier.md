# Session report — finite rooms and the adjacent Hensel frontier

Date: 2026-07-22  
Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Draft PR: `#3`

## Objective

Continue the corrected-stage construction after the fixed-room and fresh-prime
reductions, while reading the requested literature and live cross-program
advice.  The immediate goal was to determine whether the room/seam system could
be closed, or at least compressed to a single exact arithmetic obstruction.

## Material read

The session read and used:

- PR #13 `LITERATURE.md`;
- PR #13 `literature/LIVE_REPO_REVIEW_WAVE5.md`;
- the latest `gpt56-pro-03` guidance on fixed-word S-unit equations;
- PR #34's newest room, collar, cap-cell, Hensel, and coarse-carry results,
  especially `T-9808`, `T-9809`, `T-9811`, `T-9813`, `T-9817`, `L-9887`,
  `L-9888`, `L-9893`, and `L-9898`.

The cross-reading produced two decisive corrections to the search model:

1. the eventual room frontier is finite rather than freely symbolic;
2. the first unresolved physical choice is one lifted three-symbol address, not
   an independent 256-symbol stage word.

## New proposed claims

### `L-0033` — three-symbol Hensel output filter

For a prefix `(a,b,c)`, define

\[
M_m=T_1T_2T_3,
\qquad
N_m=N_0N_1N_2,
\]

\[
\tau_m=N_1N_2b_a+T_1N_2b_b+T_1T_2b_c.
\]

The canonical scaled input is

\[
\rho_m(a,b,c)=[-\tau_mN_m^{-1}]_{M_m}.
\]

Lifting by six bits gives

\[
[-\tau_mN_m^{-1}]_{64M_m}
=ho_m+M_mh_m.
\]

The canonical three-step output satisfies

\[
\sigma_m\equiv-N_mh_m\pmod{64}.
\]

Thus the fourth tower type exists exactly when this residue belongs to
`{5,30,20,56}`, and it is then unique.

The three-symbol addresses are pairwise distinct by the first-unequal-symbol
valuation argument in the positive toll.

### `T-0037` — at most 64 eventual rooms

The three-symbol modulus grows faster than the fixed room scale.  Every fixed
room eventually lies in one of 64 intervals

\[
\left[
{\rho_m(a,b,c)\over H_m},
{\rho_m(a,b,c)+1\over H_m}
\right).
\]

These intervals shrink to zero.  Sixty-five distinct rooms would eventually
need 65 disjoint addresses at one scale, impossible.  Hence

\[
\#\mathscr C\le64.
\]

A fixed room determines at most one eventual ordinary trajectory.

### `T-0038` — every room is transcendental

`O-0011` supplies reduced rationals `P_m/Q_m` with

\[
\left|C_\infty-{P_m\over Q_m}\right|
|P_m|_2|Q_m|_3
< H(P_m,Q_m)^{-2-1/1024}.
\]

The session adopted the exact projective Ridout normalization independently
audited in PR #34 `T-9811`, with targets

```text
real place: C_infinity;
2-adic place: 0;
3-adic place: infinity.
```

Infinitely many distinct approximants violate Ridout for an algebraic target.
Therefore every eventual room is transcendental.

This is classification, not nonexistence.

### `L-0034` — exact real defect digits

At every local boundary put

\[
\varepsilon_n=C_\infty H_n-W_n,
\qquad
Z_n=3^{7(t_n+1)}\varepsilon_n.
\]

Then

\[
Z_n=b_{i_n}
+\left({2048\over2187}\right)^{t_{n+1}+1}Z_{n+1}
\]

and hence

\[
Z_n=
\sum_{k\ge0}
 b_{i_{n+k}}
 \prod_{r=1}^k
 \left({2048\over2187}\right)^{t_{n+r}+1}.
\]

In the stabilized region,

\[
b_{i_n}<Z_n<b_{i_n}+{1\over16}.
\]

The type is now forced simultaneously by a binary valuation, a ternary
valuation, and one leading real defect digit.

### `T-0039` — adjacent twelve-bit room criterion

Define the top six input bits below the three-symbol modulus by

\[
q_m(a,b,c)
=\left\lfloor{64\rho_m(a,b,c)\over M_m}\right\rfloor.
\]

The room scale is not merely below `M_m`; it is eventually below `M_m/64`.
Therefore every room requires at every sufficiently late scale

\[
q_m=0
\]

and simultaneously

\[
[-N_mh_m]_{64}\in\{5,30,20,56\}.
\]

These are adjacent blocks of the same lifted inverse:

```text
upper block: allowed six-bit output Hensel lift;
lower block: zero six-bit input cell.
```

Let `mathfrak Z_m` be the set of prefixes satisfying both.  Cofinal emptiness
of `mathfrak Z_m`, or cofinal emptiness of its exact overlap graph, excludes
every room.

This is the smallest unresolved object identified in the branch.

## Exact audit `X-0017`

The portable standard-library checker reproduces the exact filters at scales
12 and 13:

```text
m=12: 0311,1330,2013,2111,2303
m=13: 0203,2202,2300
```

It also checks the exact defect-digit recurrence, the `1/16` leading interval,
and the completion-height coefficient

\[
{4257\over128}-{1083\over41}
={35913\over5248}.
\]

A separate GMP authoring audit extended the lifted-inverse filter through scale
20.  Allowed-output counts were

```text
m : 12 13 14 15 16 17 18 19 20
n :  5  3  4  6  3  4  5  2  5
```

and

\[
\mathfrak Z_m=\varnothing
\qquad(12\le m\le20).
\]

The scale-20 allowed heads were

```text
0110, 0202, 1110, 1202, 3033.
```

This finite emptiness is explicitly not treated as an induction.

## Principal negative finding

The projected six-bit quotient is not a closed state.  The exact scale-doubling
inverse update retains a Newton quotient block whose width is `Theta(2^m)`.
Across the abstract lift fiber, every one of the 64 next six-bit values occurs.
Therefore a finite-state recurrence on the six-bit quotient cannot prove the
result.

A closing theorem must:

1. retain or recompute the source-specific Newton carry;
2. prove that an allowed output lift forces a nonzero lower block;
3. or prove that the exact overlap graph is empty cofinally.

## Repository changes

Added:

- `L-0033`;
- `L-0034`;
- `T-0037`;
- `T-0038`;
- `T-0039`;
- `X-0017`.

Updated:

- `CLAIMS.md`;
- `CURRENT_STATE.md`;
- `OPEN_PROBLEMS.md`;
- `CANDIDATES.md`;
- `NEGATIVE_RESULTS.md`.

## Exact remaining gap

No counterexample and no universal exclusion theorem was obtained.

The load-bearing problem is now:

> Control the source-specific adjacent twelve moving bits under scale doubling.
> Prove that the allowed upper six-bit type block and the zero lower six-bit
> room block cannot occur cofinally, or construct one coherent transcendental
> room and one finite positive initialization that realizes them forever.

This is a much narrower target than the former 256-symbol stage search, but it
remains an all-scale arithmetic theorem.