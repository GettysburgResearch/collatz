# L-9312 — Four-phase `3/2` schedule

**Claim ID:** L-9312  
**Title:** A centered `81/64` orbit forces the full `3/2` orbit into a three-state four-phase trapping schedule  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9315`; elementary residue arithmetic modulo `64`  
**Scope:** the centered-power ordinary-section reformulation  
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
\varepsilon_n
=
\mathbf 1_{u_n>0}.
\tag{3}
\]

The nearest-integer carry relation is

\[
\boxed{
64B_{n+1}-81B_n
=
\varepsilon_n-arepsilon_{n+1}.
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
\in
\{0,15,49\}.
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

Thus the centered orbit carries a three-state residue process, not an arbitrary nearest-integer sequence.

## 2. Fourth-power decomposition

Since

\[
\frac{81}{64}
=
\left(\frac32\right)^4,
\tag{7}
\]

put

\[
Y_m
=
\xi\left(\frac32\right)^m.
\tag{8}
\]

For

\[
m=4n+r,
\qquad
0\le r<4,
\]

we have

\[
Y_{4n+r}
=
\frac{3^r}{2^r}(B_n+u_n).
\tag{9}
\]

The error radius is

\[
\left|\frac{3^r}{2^r}u_n\right|
<
\frac{(3/2)^r}{81}.
\tag{10}
\]

The possible centers are determined by `(5)`.

## 3. Exact four-phase schedule

For every `n>=0`, the fractional part of the full `3/2` orbit lies in the following disjoint scheduled neighborhoods:

\[
\boxed{
\begin{array}{c|c|c}
r&\text{allowed centers modulo }1&\text{radius}\\
\hline
0&0&1/81\\
1&0,\ 1/2&1/54\\
2&0,\ 1/4,\ 3/4&1/36\\
3&0,\ 3/8,\ 5/8&1/24
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

### Phase `r=0`

The center is `0`, and `(2)` gives radius `1/81`.

### Phase `r=1`

Only the parity of `B_n` matters. The residue set `(5)` contains one even state and two odd states, giving centers

\[
0,
\qquad
1/2.
\]

The radius is

\[
\frac32\cdot\frac1{81}
=
\frac1{54}.
\]

### Phase `r=2`

Modulo `4`, the possible residues are

\[
B_n\equiv0,3,1\pmod4.
\]

Since `9≡1 mod4`, the centers are

\[
0,
\qquad
3/4,
\qquad
1/4.
\]

The radius is

\[
\frac94\cdot\frac1{81}
=
\frac1{36}.
\]

### Phase `r=3`

Modulo `8`, the possible residues are

\[
B_n\equiv0,7,1\pmod8.
\]

Since `27≡3 mod8`, the centers are

\[
0,
\qquad
\frac{3\cdot7}{8}\equiv\frac58,
\qquad
\frac38.
\]

The radius is

\[
\frac{27}{8}\cdot\frac1{81}
=
\frac1{24}.
\]

This proves `(11)`.

## 5. Transition information

The schedule is not merely four unrelated unions of arcs. The state

\[
B_n\pmod{64}
\in\{0,15,49\}
\]

is equivalent to the adjacent digit pair `(epsilon_n,epsilon_(n+1))` through `(6)`. Hence the choice of center at one block determines whether the centered error keeps or changes sign at the next block.

The three states have the interpretation

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

A proof using only the total length of the unions in `(11)` discards this transition structure. The natural object is a graph-directed shrinking-target system for multiplication by `3/2`.

## 6. Relationship to Mahler-type problems

The classical Mahler problem constrains every power to a fixed one-sided interval. Here the complete `3/2` orbit is constrained by a periodic four-phase schedule with a three-state transition graph.

Thus `T-9315` does not merely produce a generic `Z`-number analogue. It produces a **scheduled centered `3/2` orbit** whose state is synchronized with the ordinary integral itinerary.

No theorem in the current literature packet is asserted to exclude this schedule. In particular, a range-width theorem for one Euclidean interval cannot be transferred by replacing the scheduled unions with their total length.

## 7. Gap audit

- The schedule is necessary and exact, but no nonexistence theorem for it is proved here.
- Phase `r=0` is already equivalent to the centered `81/64` condition; the value of `(11)` is the extra transition geometry at the intermediate `3/2` powers.
- Ignoring the state transitions may make the trapping set look much larger than the actual admissible language.
- The theorem applies to the induced `64 -> 81` ordinary section, not automatically to every Collatz counterexample.

## 8. Suggested next attack

Construct the graph-directed transfer operator on the three states `0,15,49`, retaining the exact interval images under multiplication by `3/2` across all four phases.

A decisive result would show that the nested real cylinder associated with every infinite admissible state path is empty or collapses to `xi=0`. This would prove

\[
\mathcal Z^{\rm ctr}_{64,81}=\varnothing
\]

and, by `T-9315`, close the ordinary section.