# T-0040 — Arbitrary-width linear-height quotient refund

Claim ID: `T-0040`  
Title: Linear-height phase-34 blocks refund the complete next cylinder at every finite width above an explicit threshold  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-23  
Dependencies: `L-0035`; elementary inequality `3^53>2^84`  
Scope: stabilized phase-`-34` linear height grids  
Related counterexample candidates: none

## 1. Block exponents

Fix a block width `L>=1` and a base height `B` divisible by `16`. Use the linear grid

\[
t_j=B+16j
\qquad(0\le j\le L).
\]

By `L-0035`, one block has odd exponent

\[
\boxed{
A_L(B)=7L(B+1)+56L(L-1),}
\tag{1}
\]

and binary input radix exponent

\[
\boxed{
E_L(B)=11L(B+1)+88L(L+1).}
\tag{2}
\]

The following block begins at `B+16L`, so its complete radix exponent is

\[
\boxed{
E_L(B+16L)
=11L(B+1)+264L^2+88L.}
\tag{3}
\]

## 2. Exact integer margin

Define

\[
\boxed{
\Delta_L(B)
=
84A_L(B)-53\bigl(E_L(B+16L)+1\bigr).}
\tag{4}
\]

Direct simplification gives

\[
\boxed{
\Delta_L(B)
=
L(5B-9288L-9363)-53.}
\tag{5}
\]

### Theorem 1 — quotient refund

If

\[
\boxed{
16\mid B,
\qquad
\Delta_L(B)>0,}
\tag{6}
\]

then

\[
\boxed{
3^{A_L(B)}
>
2\,2^{E_L(B+16L)}.}
\tag{7}
\]

### Proof

The exact integer inequality

\[
3^{53}>2^{84}
\]

implies

\[
3^a>2^{84a/53}
\]

for every positive integer `a`. Condition (4) says

\[
\frac{84A_L(B)}{53}>E_L(B+16L)+1.
\]

Substitution proves (7). ∎

## 3. Strict growth of every positive free lift

Take any current block word and any physically overlapping next block word of the same width. By `L-0035`, their exact quotient transition has the form

\[
Y=y+Qh,
\qquad
Y'=c+Nh,
\tag{8}
\]

where

\[
Q=2^{E_L(B+16L)},
\qquad
N=3^{A_L(B)},
\tag{9}
\]

\[
0\le y<Q,
\qquad
c\ge0,
\qquad
h\ge0.
\tag{10}
\]

### Theorem 2 — universal positive-lift growth

Under condition (6), every lift with `h>=1` satisfies

\[
\boxed{Y'>Y.}
\tag{11}
\]

### Proof

Because `0<=y<Q` and `h>=1`,

\[
Y=y+Qh<Q(h+1)\le2Qh.
\]

By (7),

\[
2Qh<Nh\le c+Nh=Y'.
\]

This proves (11). ∎

Thus every finite ordered word pair possesses infinitely many positive ordinary quotient transitions, and every noncanonical lift grows strictly.

## 4. Exact certified thresholds

Let `B_L` be the least positive multiple of `16` for which (6) holds. Exact evaluation gives

| block width `L` | `B_L` | margin `Delta_L(B_L)` |
|---:|---:|---:|
| 1 | 3744 | 16 |
| 2 | 5600 | 69 |
| 16 | 31600 | 411 |
| 256 | 477424 | 7371 |

The last row recovers the linear 256-transition refund threshold from `LIT-KTHM-0050`. The first row is the important reduction:

\[
\boxed{
L=1,\ B=3744
}
\]

already suffices.

For width one, every transition raises the height by `16`. The next-cylinder depth grows by exactly

\[
\boxed{176}
\]

binary bits per transition, while the odd multiplier is multiplied by

\[
\boxed{3^{112}.}
\]

Consequently the constructive state can be organized as

```text
16 oriented tower states
+ one fixed-width 176-bit moving block
+ one unbounded ordinary quotient
+ one canonical most-significant boundary.
```

The old 256-symbol stage is not required to obtain refund or growth.

## 5. Counterexample criterion

Suppose there are:

1. an initial height `B>=B_L` satisfying (6);
2. one explicit finite physically positive Collatz state whose scaled quotient is `Y_0`;
3. a causal finite or finitely generated rule choosing each next block word from the current ordinary state;
4. a proof that at every transition the current quotient has a representation (8) with `h>=1`;
5. a proof that the canonical most-significant boundary remains finite and all local tower blocks replay the deterministic shortcut map.

Then Theorem 2 gives a strictly increasing quotient sequence. The physical phase-34 embedding from `L-0016` and `L-0031` transports this to an unbounded positive shortcut-Collatz orbit. Hence the initial positive integer is a counterexample.

## Strategic consequence

The missing theorem is no longer raw growth. It is a one-counter invariant that regenerates one fixed-size moving boundary block.

The highest-value positive route is:

\[
\boxed{
\text{efficient exact selector for the next 176 bits}
+
\text{width-one quotient refund}.}
\]

A collision code with complete dyadic projection can provide arbitrary finite low-bit corrections, but the existing explicit construction is exponentially long in the number of selected bits. A successful synthesis should therefore seek an efficient tensorable selector or a direct top-boundary invariant.

## Gap audit

- Pairwise finite overlaps do not produce one infinite ordinary path.
- A compatible `2`-adic quotient is not an ordinary finite initialization.
- The quotient must occupy the required residue cylinder at every height using only current finite data.
- Growth of the quotient does not by itself prove closure of the most-significant finite boundary.
- No positive counterexample is claimed.

## Exact verification

`X-0018` verifies the formulas, all width-one cylinders and overlaps at `B=3744`, every width-two word at `B=5600`, representative width-two word-pair overlaps, and strict growth for multiple positive lifts.