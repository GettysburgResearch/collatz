# T-0037 — Finite classification of eventual corrected-stage rooms

Claim ID: `T-0037`  
Title: At most sixty-four fixed rooms and eventual tower tails can occur in the corrected phase-34 architecture  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0031`, `L-0033`, `T-0033`, `T-0036`  
Cross-program antecedent: independently derived in PR #34 `T-9808`/`T-9809`  
Scope: eventual positive ordinary trajectories through the fixed corrected 256-transition stage architecture  
Related counterexample candidates: none

## Eventual room set

Let `mathscr C` be the set of real numbers `C > 0` for which there is some
starting scale `m_0(C) >= 12` and an infinite ordinary scaled-tail trajectory
satisfying

\[
W_m=\lfloor C H_m\rfloor
\qquad(m\ge m_0(C)),
\tag{1}
\]

with the exact corrected-stage recurrence of `L-0031`.

The starting scale is allowed to depend on the room.

## Statement

One has

\[
\boxed{\#\mathscr C\le64.}
\tag{2}
\]

A fixed room determines at most one eventual sequence of ordinary boundaries,
local tower types, stage words, residual corrections, and cap stitches.
Consequently there are at most 64 eventual corrected-stage tails, modulo
deletion of a finite initial segment.

## Proof

Assume for contradiction that there are 65 distinct rooms

\[
C_1,\ldots,C_{65}\in\mathscr C.
\]

Put

\[
K=1+\max_jC_j,
\qquad
d_0=\min_{r\ne s}|C_r-C_s|>0.
\tag{3}
\]

Choose one scale beyond all 65 starting scales and so large that

\[
K H_m<M_m=2^{U_m},
\qquad
H_m^{-1}<d_0.
\tag{4}
\]

The first inequality follows from `L-0033/(15)`, uniformly for the fixed
constant `K`.  For each room, (1) and (4) give

\[
0\le W_m< M_m.
\]

The three-symbol divisibility relation therefore identifies `W_m` with one of
the 64 distinct least addresses

\[
\rho_m(a,b,c),
\qquad(a,b,c)\in\{0,1,2,3\}^3.
\tag{5}
\]

Hence every selected room belongs to one of the 64 half-open intervals

\[
I_m(a,b,c)
=
\left[
{\rho_m(a,b,c)\over H_m},
{\rho_m(a,b,c)+1\over H_m}
\right).
\tag{6}
\]

Each interval has diameter `H_m^(-1)<d_0`, so it contains at most one of the 65
rooms.  There are only 64 intervals, a contradiction.  This proves (2).

For uniqueness of the tail, a fixed room determines every sufficiently late
integer `W_m` by (1).  Its residue modulo 64 determines the current tower type
by `T-0036`.  More strongly, reduction of the positive stage toll modulo the
successive prefix powers of two is lossless: the first unequal symbol produces
the unique lowest valuation, exactly as in `L-0033`.  Thus `W_m` determines the
entire 256-symbol source word.  The exact recurrence then determines
`W_(m+1)`, and induction determines the full tail. ∎

## Stronger variable filter

At each scale define the three-symbol survivor set

\[
\mathfrak P_m
=
\{(a,b,c):
[-N_mh_m(a,b,c)]_{64}\in\{5,30,20,56\}\},
\tag{7}
\]

using the six-bit lift from `L-0033`, and put

\[
n_m=\#\mathfrak P_m.
\tag{8}
\]

Then

\[
\boxed{
0\le n_m\le64,
\qquad
\#\mathscr C\le\liminf_{m\to\infty}n_m.}
\tag{9}
\]

Indeed, at all sufficiently late scales distinct rooms give distinct ordinary
integers `floor(C H_m)`, hence distinct three-symbol addresses, and every such
address must pass (7).

Therefore any cofinal sequence of scales with `n_m=0` excludes every room.  A
cofinal bound `n_m<=R` improves the global room bound to `R`.

## Exact bounded audit

`X-0017` evaluates (7) by one six-bit Hensel lift.  At scales 12 through 19 the
exact survivor counts are

```text
m : 12 13 14 15 16 17 18 19
n :  5  3  4  6  3  4  5  2
```

This is finite evidence only.  In particular, the value `2` at scale 19 does
not prove the global bound is two, because a room may begin later and (9)
requires a lower-limit statement.

## Interpretation

The architecture no longer has an uncountable or freely symbolic room
frontier.  It has at most 64 exceptional real constants, each encoding one
complete eventual ordinary trajectory.

The remaining problem is not cardinality.  It is to prove that the moving
Hensel filter (7) is empty cofinally, or to construct one of its finitely many
coherent room paths from a finite ordinary initialization.

## Gap audit

- A finite set of rooms may consist of transcendental numbers.
- One small finite value of `n_m` is not an asymptotic theorem.
- The theorem does not decide whether `mathscr C` is empty.
- No positive integer or counterexample is claimed.