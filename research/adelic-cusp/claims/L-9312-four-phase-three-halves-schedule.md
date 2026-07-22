# L-9312 — Four-phase `3/2` schedule

**Claim ID:** L-9312  
**Title:** A centered `81/64` orbit forces the full `3/2` orbit into a three-state four-phase schedule  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9315`; elementary residue arithmetic modulo `64`; `L-9313` for the full-shift boundary  
**Scope:** centered-power geometry and its nearest-integer state  
**Related counterexample candidates:** none

## 1. Setup

Assume

\[
\xi>0,
\qquad
\left\|
\xi\left(\frac{81}{64}\right)^n
\right\|
\le\frac1{81}
\quad(n\ge0).
\tag{1}
\]

By `T-9315`, write uniquely

\[
\xi\left(\frac{81}{64}\right)^n
=B_n+u_n,
\qquad
B_n\in\mathbb Z,
\qquad
|u_n|<\frac1{81},
\tag{2}
\]

and define

\[
\varepsilon_n=\mathbf1_{u_n>0}.
\tag{3}
\]

The nearest-integer carry relation is

\[
\boxed{
64B_{n+1}-81B_n
=
\varepsilon_n-\varepsilon_{n+1}.
}
\tag{4}
\]

Because

\[
17^{-1}\equiv49\pmod{64},
\]

reduction of `(4)` modulo `64` gives

\[
\boxed{
B_n\pmod{64}
\in\{0,15,49\}.
}
\tag{5}
\]

More precisely,

\[
\begin{array}{c|c|c}
(\varepsilon_n,\varepsilon_{n+1})
&\varepsilon_n-\varepsilon_{n+1}
&B_n\pmod{64}\\
\hline
(0,0),(1,1)&0&0\\
(1,0)&1&15\\
(0,1)&-1&49
\end{array}
\tag{6}
\]

Thus the centered orbit carries a three-state nearest-integer residue process.

## 2. Fourth-power decomposition

Since

\[
\frac{81}{64}=\left(\frac32\right)^4,
\tag{7}
\]

put

\[
Y_m=\xi\left(\frac32\right)^m.
\tag{8}
\]

For

\[
m=4n+r,
\qquad0\le r<4,
\]

we have

\[
Y_{4n+r}
=\frac{3^r}{2^r}(B_n+u_n).
\tag{9}
\]

The error radius is

\[
\left|\frac{3^r}{2^r}u_n\right|
<\frac{(3/2)^r}{81}.
\tag{10}
\]

## 3. Exact four-phase schedule

For every `n>=0`, the fractional part of the full `3/2` orbit lies in the scheduled neighborhoods

\[
\boxed{
\begin{array}{c|c|c}
r&\text{allowed centers modulo }1&\text{radius}\\
\hline
0&0&1/81\\
1&0,\ 1/2&1/54\\
2&0,\ 1/4,\ 3/4&1/36\\
3&0,\ 3/8,\ 5/8&1/24.
\end{array}
}
\tag{11}
\]

Equivalently,

\[
\operatorname{dist}
\left(
Y_{4n+r},
\mathcal C_r+\mathbb Z
\right)
<\delta_r,
\tag{12}
\]

where

\[
\begin{aligned}
\mathcal C_0&=\{0\},&\delta_0&=1/81,\\
\mathcal C_1&=\{0,1/2\},&\delta_1&=1/54,\\
\mathcal C_2&=\{0,1/4,3/4\},&\delta_2&=1/36,\\
\mathcal C_3&=\{0,3/8,5/8\},&\delta_3&=1/24.
\end{aligned}
\tag{13}
\]

## 4. Proof of the centers

At phase `r`, the center is

\[
\frac{3^rB_n}{2^r}\pmod1.
\tag{14}
\]

- At `r=0`, the center is `0` and the radius is `1/81`.
- At `r=1`, only the parity of `B_n` matters, giving `0` or `1/2`; the radius is `1/54`.
- At `r=2`, equation `(5)` gives `B_n=0,3,1 mod4`. Since `9=1 mod4`, the centers are `0,3/4,1/4`; the radius is `1/36`.
- At `r=3`, equation `(5)` gives `B_n=0,7,1 mod8`. Since `27=3 mod8`, the centers are `0,5/8,3/8`; the radius is `1/24`.

This proves `(11)`.

## 5. Transition information

The state in `(5)` is equivalent to the adjacent digit pair through `(6)`:

\[
\begin{array}{c|c}
B_n\pmod{64}&\text{digit transition}\\
\hline
0&\varepsilon_{n+1}=\varepsilon_n\\
15&1\to0\\
49&0\to1.
\end{array}
\tag{15}
\]

The schedule is therefore not four unrelated unions of arcs. The intermediate centers are synchronized with a nearest-integer residue state.

## 6. Full-shift boundary

`L-9313` proves that every binary itinerary has one bounded real centered-error path. Therefore the real scheduled cylinders in `(11)` do **not** become empty merely because the symbolic path is long or complicated.

This corrects the tempting but false proof target:

> pull the real intervals back and prove every nonzero path disappears.

The real error coordinate has full symbolic support. The genuine obstruction is whether the same path's nested nearest-integer congruences select one ordinary integer.

`R-9303` records this method closure explicitly.

## 7. Relationship to Mahler-type problems

The classical Mahler problem constrains every power to one fixed one-sided interval. Here the complete `3/2` orbit follows a periodic schedule and carries an arithmetic state.

No theorem in the current literature packet is asserted to exclude the exact combined object. In particular:

- a range-width theorem for one interval cannot be applied to the union of scheduled arcs;
- a real graph-directed nonemptiness calculation ignores nearest-integer stabilization;
- a finite-state graph on `0,15,49` loses the unbounded base-64 precision selected by the itinerary.

## 8. Correct next attack

Retain both coordinates:

1. the bounded real error path `u_n`;
2. the nested nearest-integer cylinder `B_0 mod64^K`.

The exact next target is `Q-9303`: derive a recurrence or invariant for the newly appended cylinder blocks and prove that they are nonzero infinitely often on every nontrivial path.

The four-phase schedule remains useful as a real normalization of those arithmetic blocks, not as a standalone emptiness theorem.

## 9. Gap audit

- The schedule is necessary and exact but does not prove nonexistence.
- Every symbolic path has a real error lift; only some could have an ordinary nearest-integer lift.
- Ignoring the nested integer cylinder is a fatal loss of information.
- The theorem applies to the induced `64 -> 81` ordinary section, not automatically to every Collatz counterexample.
