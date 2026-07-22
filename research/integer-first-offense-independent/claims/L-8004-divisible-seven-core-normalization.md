# L-8004 — Divisible-three image normalization and the invariant divisible-seven core

**Claim ID:** `L-8004`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** local `O-8001`, `L-8002`  
**Scope:** exact ordinary paths in the negative-three-cycle pulse chart

## 1. The normalized image chart

Local `O-8001` gives the exact chart in the coordinate

\[
 h=\frac{n+5}{2}:
\]

\[
 h=8q\longmapsto9q,
 \qquad
 h=3+16q\longmapsto3+9q.
\tag{1}
\]

Both outputs in (1) are divisible by `3`. Therefore every legal chart path,
after at most one edge, enters the invariant image

\[
 h=3z.
\tag{2}
\]

In this coordinate the exact ordinary chart is

\[
 \boxed{
 A:z=8q\longmapsto9q,
 \qquad
 B:z=1+16q\longmapsto1+9q,}
\tag{3}
\]

and the physical shortcut-Collatz state is

\[
 \boxed{n=6z-5.}
\tag{4}
\]

Thus the normalized chart used in `L-8002` loses no infinite path: every
infinite path in (1) reaches it after its first block.

## 2. The exact invariant `7 | z`

The subset

\[
 \boxed{7\mathbf Z_{>0}}
\tag{5}
\]

is forward invariant under every legal edge of (3).

For `A`, this is immediate from `z'=9z/8`, since `8` is invertible modulo
`7`. For `B`, if `7|z`, then `7|(9z+7)` and `16` is coprime to `7`.

This is an ordinary divisibility invariant, not a completion statement.

## 3. The `+1` run-core equation

In the maximal-run coordinates of `L-8002`, impose (5) and write

\[
 \boxed{z=7\,2^{3r}v,}
 \qquad v\text{ odd}.
\tag{6}
\]

If the next run has length `s`, write

\[
 z^+=7\,2^{3s}v^+.
\tag{7}
\]

The core equation of `L-8002` divides exactly by seven and becomes

\[
 \boxed{
 2^{4+3s}v^+=9^{r+1}v+1.}
\tag{8}
\]

Every completed next core satisfies

\[
 \boxed{
 v^+\equiv
 \begin{cases}
 103\pmod {144},&s\text{ even},\\
 95\pmod {144},&s\text{ odd}.
 \end{cases}}
\tag{9}
\]

### Proof of (9)

Modulo `9`, equation (8) gives

\[
 2^{4+3s}v^+\equiv1\pmod9.
\]

Since `2^(4+3s) congruent 7(-1)^s mod9`, one gets

\[
 v^+\equiv4\pmod9\quad(s\text{ even}),
 \qquad
 v^+\equiv5\pmod9\quad(s\text{ odd}).
\]

The next `B` condition is

\[
 7\,9^s v^+\equiv1\pmod {16}.
\]

Because `7^(-1) congruent7 mod16` and `9^2 congruent1 mod16`, this gives

\[
 v^+\equiv7\pmod {16}\quad(s\text{ even}),
 \qquad
 v^+\equiv15\pmod {16}\quad(s\text{ odd}).
\]

CRT gives (9). ∎

## 4. One quotient in the divisible-seven subchart

Put

\[
 M_s=2^{4+3s},
 \qquad
 L_s=16M_s=2^{8+3s},
\tag{10}
\]

and

\[
 e_s=
 \begin{cases}
 7,&s\text{ even},\\
 15,&s\text{ odd}.
 \end{cases}
\tag{11}
\]

Define

\[
 \boxed{
 \widetilde a_{r,s}
 =[(M_se_s-1)9^{-(r+1)}]_{L_s}.}
\tag{12}
\]

Then the current core `v` has exact next run `s` and a legal following `B`
edge if and only if

\[
 \boxed{v\equiv\widetilde a_{r,s}\pmod {L_s}.}
\tag{13}
\]

Writing

\[
 v=\widetilde a_{r,s}+L_sk
\tag{14}
\]

leaves one ordinary quotient, and

\[
 \boxed{
 v^+=\widetilde c_{r,s}+16\,9^{r+1}k,}
\tag{15}
\]

where

\[
 \widetilde c_{r,s}
 =\frac{9^{r+1}\widetilde a_{r,s}+1}{M_s}
 \equiv e_s\pmod {16}.
\tag{16}
\]

Thus the invariant changes the affine constant from `7` to `1` while
preserving the same multiplicative changing-modulus quotient-refund
architecture.

## 5. Canonical ordinary representative in every finite cylinder

Let a finite run prefix determine one residue class

\[
 z\equiv R\pmod {2^S}.
\tag{17}
\]

Because `2^S` is invertible modulo `7`, there is a unique

\[
 t\in\{0,1,\ldots,6\}
\]

such that

\[
 \boxed{R+2^St\equiv0\pmod7.}
\tag{18}
\]

If the value in (18) is zero, the least positive representative is
`7*2^S`. Otherwise it is the least positive divisible-seven member of the
finite cylinder.

This selection is an exact ordinary finite-prefix operation. It does **not**
prove that the selected representatives stabilize through infinitely many
prefixes.

If the canonical representative of a prefix actually realizes one more run,
it is also the canonical representative of the corresponding child cylinder:
any smaller divisible-seven child representative would already be a smaller
representative of the parent.

## 6. Constructive significance

The divisible-seven chart is the smallest exact arithmetic subchart found so
far in which:

```text
physical ordinary state is explicit;
all edges are exact Collatz blocks;
one changing-modulus quotient carries the top boundary;
the core recurrence has constant +1;
run >=5 gives strict physical growth.
```

A finite state whose deterministic quotient map is defined forever and emits
runs at least five remains a complete counterexample by `T-8002`.

## 7. Gap audit

- Divisibility by seven does not guarantee one further chart edge.
- The canonical representative in (18) usually leaves the high-run language;
  it is a finite selector, not an invariant theorem.
- A sequence of compatible divisible-seven residues can still converge only
  to a nonordinary completion unless the least representatives stabilize.
- The additive one-counter obstruction `PR34/L-9915` does not apply to (15),
  but no positive theorem follows merely from escaping that scope.

## 8. Suggested next attack

Use (8) rather than the unnormalized `+7` equation. Freeze a small run alphabet
above the pointwise threshold and search for an inductive class on the exact
quotient `k` that:

1. keeps `v` in the two residue classes (9);
2. makes the next changing-modulus division exact;
3. refunds the top quotient under the multiplier `9^(r+1)`; and
4. never emits a run below five.