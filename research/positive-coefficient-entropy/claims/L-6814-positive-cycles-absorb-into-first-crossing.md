# L-6814 — Every positive cycle produces a canonical first-crossing failure

**Claim ID:** `L-6814`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6803`, `L-6812`; elementary positive-cycle affine algebra  
**Scope:** positive shortcut-Collatz cycles and the coefficient-first-crossing target

## 1. Statement

Let a nontrivial positive shortcut-Collatz cycle exist. Rotate it to a
minimum state `n`, let its primitive period have length `p`, and let `j` be
the first time along that period at which the multiplicative coefficient
becomes subcritical:

\[
3^{q_k}\ge2^k
\quad(1\le k<j),
\qquad
3^{q_j}<2^j.
\tag{1}
\]

Let `w` be this length-`j` parity prefix and let

\[
(r_w,s_w)
\]

be its canonical start--end pair.

Then

\[
\boxed{s_w\ge r_w.}
\tag{2}
\]

Thus every nontrivial positive cycle produces a canonical coefficient-first-
crossing target failure.

Consequently, proving

\[
\boxed{s_w<r_w}
\]

for every nontrivial canonical first-crossing word automatically excludes all
nontrivial positive cycles.  No third cycle premise is needed in the final
coefficient-stopping implication.

## 2. Existence of a first coefficient crossing on the cycle

Let the full primitive period have length `p`, weight `q`, and affine
numerator `A>0`.  Since it returns `n` to itself,

\[
2^p n=3^q n+A.
\]

Therefore

\[
(2^p-3^q)n=A>0,
\]

so

\[
3^q<2^p.
\]

Hence the first index `j` in `(1)` exists and satisfies `1<=j<=p`.

Because `n` is the minimum state on the cycle,

\[
T^j(n)\ge n.
\tag{3}
\]

## 3. Canonical-ray transfer

Put

\[
P=2^j,
\qquad
Q=3^{q_j},
\qquad
D=P-Q>0.
\]

Every positive realization of `w` is, by `L-6803`, uniquely

\[
n=r_w+tP,
\qquad
t\in\mathbf Z_{\ge0},
\tag{4}
\]

with endpoint

\[
T^j(n)=s_w+tQ.
\tag{5}
\]

Subtracting `(4)` from `(5)`,

\[
T^j(n)-n
=(s_w-r_w)-tD.
\tag{6}
\]

The left side is nonnegative by `(3)`. Therefore

\[
\boxed{s_w-r_w\ge tD\ge0,}
\tag{7}
\]

which proves `(2)`.

In particular, a non-descending higher lift can never hide a descending
canonical member: coefficient contraction makes every higher lift **more**
descending by exactly `D` per lift.

## 4. Cycle and acyclic displacement levels

Put

\[
d=s_w-r_w\ge0.
\]

`L-6812` gives

\[
\boxed{
A_w=Dr_w+Pd
=Ds_w+Qd,
\qquad
0\le d<q_j/3.}
\tag{8}
\]

There are two possibilities.

### Canonical cycle level

If

\[
d=0,
\]

then `(7)` forces `t=0`, and

\[
T^j(r_w)=r_w.
\]

The first-crossing prefix itself is a positive periodic word.

### Canonical near-return level

If

\[
d>0,
\]

then the cycle has produced a canonical acyclic first-crossing obstruction

\[
T^j(r_w)=r_w+d,
\qquad
1\le d<q_j/3.
\]

The later completion of the original orbit closes the full cycle, but the
first coefficient crossing is already a canonical CST failure.

Thus a positive cycle is absorbed by the same shifted-denominator language
as every other Box-2 obstruction.

## 5. Unified full-denominator target

The complete finite-crossing compiler should retain

\[
\boxed{
0\le d<q/3.}
\]

- `d=0` contains the positive-cycle level;
- `d>0` contains acyclic delayed first crossings;
- the sole accepted equality in the desired theorem is the trivial word
  `10`, source `1`, endpoint `1`.

A uniform exclusion of every other complete tuple in `L-6809` therefore
proves both:

```text
no nontrivial positive cycle;
every nontrivial first coefficient crossing descends canonically.
```

## 6. Complete two-lane implication

The final coefficient program needs only:

```text
SC*:
  no all-time-supercritical ordinary canonical source;

FC*:
  no nontrivial complete first-crossing tuple with 0<=d<q/3.
```

`L-6814` shows that `FC*` already contains the positive-cycle obligation.
Thus `SC*+FC*` imply Collatz without an additional cycle hypothesis.

## 7. Gap audit

- The lemma absorbs cycles into the first-crossing target; it does not exclude
  that target.
- The canonical first crossing induced by a cycle may have `d>0`; one must not
  search only the cycle level `d=0`.
- The trivial `1 <-> 2` cycle gives the word `10` and must remain exempt from
  the strict universal statement.
- No proof of FC*, SC*, or Collatz is claimed.
