# Failed strengthening: universal synchronous erasure

Date: 2026-11-21 UTC. Status: exact written counterexample and affine algebra;
no new Lean proof or compiler run is claimed.

Use the shortcut map `T(n)=n/2` for even `n` and `(3n+1)/2` for odd `n`.
The positive erasure theorem uses

\[
n=2^ku-1,\quad x=2^{k-r}u-1,\quad v=3^{k-r}u,
\]

and a synchronous endpoint diamond
`T^h(v-1)=T^h(3^r v-1)`. Such a diamond gives a genuine smaller source,
and markedness is preserved. The strengthening claiming that every marked
source has some such diamond is false, even if `r` and `h` are allowed to
vary.

## 1. The marked source 7 has no admissible synchronous erasure

Take `n=7=2^3*1-1`. It is marked: its binary exponent is 2 and
`(2+1)(7-4)=9 <= 70*4`.

The only positive erasures with `0<r<k=3` are:

| r | Smaller source x | Endpoint pair requiring equal-clock merger |
|---|---:|---|
| 1 | 3 | `(8,26)` |
| 2 | 1 | `(2,26)` |

Indeed `T^3(7)=26`, `T^2(3)=8`, and `T(1)=2`. At `r=3` the proposed
source would be zero, so it is inadmissible. Writing 7 with a shorter
initial run introduces no new partner: the admissible deletion still has
`r=1` or `r=2`, and any shorter-prefix synchronous identity can be advanced
by the remaining odd steps to the corresponding endpoint pair above.

The first nine states of the two relevant trajectories are

\[
8,4,2,1,2,1,2,1,2
\]

and

\[
26,13,20,10,5,8,4,2,1.
\]

They differ at clocks 0 through 7. At every even clock `h>=8`, the first
is 2 and the second is 1; at every odd clock `h>=8`, these values reverse.
Thus `T^h(8) != T^h(26)` for every `h`.

The trajectory starting at 2 is 2 at even clocks and 1 at odd clocks.
Comparing its clocks 0 through 7 with the second row, and then using the
same opposite phases, proves `T^h(2) != T^h(26)` for every `h`.

This refutes the universal **synchronous** diamond cover. It does not
refute common-future merging or Collatz: the unequal-clock identities

\[
T^0(8)=T^5(26),\qquad T^0(2)=T^7(26)
\]

give the actual source mergers

\[
T^2(3)=T^8(7),\qquad T(1)=T^{10}(7).
\]

The same endpoint pair `(8,26)` occurs for the marked source `11=2^2*3-1`
and its half-source partner 5.

## 2. Unequal clocks cannot give an affine-cylinder identity for these arms

Fix `r,a,b`, and fix the parity words of lengths `a,b` followed by the
two arms `v-1` and `3^r v-1`. Write their odd counts as `p,q` and their
integer affine constants as `C,D`. On their common parity cylinder,

\[
T^a(v-1)=\frac{3^p v+C-3^p}{2^a},\qquad
T^b(3^r v-1)=\frac{3^{q+r}v+D-3^q}{2^b}.
\]

If these affine expressions agree for two distinct values of `v`, their
slopes agree:

\[
2^b3^p=2^a3^{q+r}.
\]

Taking the exact exponent of 2 on both sides forces `a=b`; equality of
the remaining powers of 3 then forces `p=q+r`.

Therefore a fixed unequal-clock identity `a!=b` holds for **at most one
rational parameter in each fixed parity cylinder**. In particular it
cannot hold on an infinite arithmetic progression of ordinary parameters.
For fixed `r,a,b` there are only finitely many parity cylinders, so such
an unequal-clock rule covers only finitely many parameters.

Allowing clocks to depend without bound on the individual parameter is
not excluded. Nor is a different partner formula, whose slope may include
an additional power of 2. Neither possibility has been turned here into a
universal ordinary-source construction. The new marked-preservation
theorem removes the markedness obligation after a successful dyadic
erasure; it does not supply its missing physical merger.
