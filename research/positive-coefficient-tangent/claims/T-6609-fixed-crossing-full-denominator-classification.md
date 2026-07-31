# T-6609 — complete fixed-crossing classification by a short full-denominator window

**Claim ID:** `T-6609`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `L-6601`, `T-6607`, `L-6602`; elementary converse algebra  
**Scope:** all first-coefficient-crossing words at one fixed length  

## 1. First-crossing language

Put

\[
\alpha={\log2\over\log3}.
\]

Fix `j>=2` for which there is an integer `q` satisfying

\[
3^q\ge2^{j-1},
\qquad
3^q<2^j.
\tag{1}
\]

Because the interval in `(1)` has logarithmic length `alpha<1`, `q` is unique.

Let `W_(j,q)` be the finite set of binary words

\[
v=(v_0,\ldots,v_{j-1})
\]

such that

\[
S_m(v)=\sum_{r=0}^{m-1}v_r
\ge\lceil\alpha m\rceil
\qquad(1\le m<j),
\tag{2}
\]

and

\[
S_j(v)=q.
\tag{3}
\]

Every member ends in zero and has its first coefficient crossing at time `j`.

Let `w=w_(j,q)` be the upper mechanical word with equality in `(2)` at every proper prefix.

For any `v in W_(j,q)`, write

\[
A_v=\sum_{i=1}^{q}3^{q-i}2^{d_i(v)},
\tag{4}
\]

where `d_i(v)` are its odd positions, and let

\[
r_v\in[1,2^j)
\]

be its least positive parity-cylinder representative. Put

\[
y_v=T_v^j(r_v),
\qquad
\delta_v=r_v-y_v.
\tag{5}
\]

Finally define

\[
D=2^j-3^q>0,
\tag{6}
\]

and for the mechanical word

\[
r_w,\ y_w,\ \delta_w=r_w-y_w,
\qquad
E_w={A_w\over2^j}.
\tag{7}
\]

## 2. Mechanical dominance

For every `v in W_(j,q)`, prefix dominance gives

\[
d_i(v)\le d_i(w)
\qquad(1\le i\le q),
\]

and hence

\[
\Delta_v=A_w-A_v\ge0.
\tag{8}
\]

Equality holds exactly when `v=w`.

## 3. Complete displacement classification

For a nonmechanical word `v`, the following data are equivalent.

### A. Canonical word data

The word `v`, its canonical root `r_v`, and its descent defect `delta_v`.

### B. Full-denominator data

A unique pair of positive integers `(u,h)` satisfying

\[
\boxed{
A_w-A_v=Du-h2^j,}
\tag{9}
\]

with

\[
\boxed{u=r_w-r_v,}
\tag{10}
\]

and

\[
\boxed{h=\delta_w-\delta_v.}
\tag{11}
\]

Equivalently,

\[
\boxed{
A_v\equiv A_w+h2^j\pmod D,}
\tag{12}
\]

and

\[
\boxed{
u={A_w-A_v+h2^j\over D}.}
\tag{13}
\]

### Proof

Subtracting the defect identities

\[
2^j\delta_z=Dr_z-A_z
\]

for `z=w,v` gives `(9)--(11)`.

Conversely, suppose an admissible word `v` and positive integers `(u,h)` satisfy `(9)` with

\[
1\le u<r_w.
\tag{14}
\]

Then

\[
\begin{aligned}
3^q(r_w-u)+A_v
&=3^q r_w+A_w-3^q u-(A_w-A_v)\\
&=3^q r_w+A_w-3^q u-Du+h2^j\\
&=3^q r_w+A_w+(h-u)2^j,
\end{aligned}
\]

so `r_w-u` lies in the parity cylinder of `v`. By `(14)` it belongs to `[1,2^j)`, hence uniqueness of the finite parity residue gives

\[
r_v=r_w-u.
\]

The defect identity then gives

\[
\delta_v=\delta_w-h.
\]

Thus the correspondence is exact. ∎

## 4. Short dangerous window

Assume the mechanical representative descends:

\[
\delta_w>0.
\tag{15}
\]

A word `v` fails the strict descent target exactly when

\[
\delta_v\le0,
\]

or, by `(11)`,

\[
h\ge\delta_w.
\tag{16}
\]

Since `Delta_v>0`, equation `(9)` and `u<r_w` imply

\[
h
<{Du\over2^j}
<{Dr_w\over2^j}
=\delta_w+E_w.
\tag{17}
\]

Therefore every nonmechanical target failure belongs to the finite integer window

\[
\boxed{
\delta_w
\le h
<\delta_w+E_w.}
\tag{18}
\]

The equality level

\[
h=\delta_w
\]

is exactly `delta_v=0`, a positive cycle. Every acyclic failure belongs to

\[
\boxed{
\delta_w+1
\le h
<\delta_w+E_w.}
\tag{19}
\]

## 5. Complete fixed-`j` Box-2 criterion

Every word in `W_(j,q)` satisfies the strict canonical descent target

\[
r_v>{A_v\over D}
\tag{20}
\]

if and only if both of the following hold.

### Mechanical gate

\[
\boxed{\delta_w>0.}
\tag{21}
\]

### Short full-denominator gate

For every integer

\[
\delta_w\le h<\delta_w+E_w
\tag{22}
\]

there is no nonmechanical `v in W_(j,q)` such that

\[
\boxed{
D\mid A_w-A_v+h2^j}
\tag{23}
\]

and

\[
\boxed{
1\le{A_w-A_v+h2^j\over D}<r_w.}
\tag{24}
\]

Indeed, `(23)--(24)` are exactly `(9)` and `(14)`, and the resulting defect is `delta_w-h<=0`.

This is a necessary-and-sufficient finite decision, not merely an obstruction.

## 6. Size of the finite window

The number of acyclic levels `(19)` is at most

\[
\max\{0,\lceil E_w\rceil-1\}.
\]

For a first-crossing mechanical word, every odd remainder contribution is below `1/2`, so

\[
E_w<{q\over2}<{j\over2}.
\]

Thus all nonmechanical canonical failures at length `j` reduce to fewer than `j/2` full-denominator target residues.

## 7. Displacement-language form

Let

\[
e_i=d_i(w).
\]

The nonmechanical numerators in `(23)` have the explicit form

\[
\boxed{
A_w-A_v
=
\sum_{i=1}^{q}
3^{q-i}\left(2^{e_i}-2^{d_i}\right),}
\tag{25}
\]

where

\[
0\le d_1<\cdots<d_q<j,
\qquad
d_i\le e_i,
\]

and the corresponding binary word satisfies the equivalent prefix constraints `(2)`.

The uniform Box-2 problem is therefore a sparse full-denominator avoidance theorem for the displacement language `(25)` against the short residue list

\[
A_w+h2^j\pmod D.
\]

## 8. Relationship to the cycle lane

The level `h=delta_w` is not discarded: it is exactly the full-denominator equality producing a positive cycle.

Thus one uniform avoidance theorem for `(23)--(25)` would simultaneously:

- exclude every acyclic first-crossing canonical failure; and
- exclude every positive cycle whose minimal parity block has its first coefficient crossing at the end.

## 9. Gap audit

- The theorem is complete at fixed `j` but does not establish the uniform avoidance.
- The displacement language has exponentially many words even though the target residue list has fewer than `j/2` levels.
- Proper-factor congruences are insufficient unless they combine to exclude `(23)` for the full denominator `D`.
- No proof of CST or Collatz is claimed.
