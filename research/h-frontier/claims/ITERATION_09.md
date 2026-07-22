# Iteration 09: compiler-construction no-go and exact renewal-box audit

All theorem-level claims remain `PROPOSED` pending independent review.
`X-9508` is an exact finite computation and does not prove an infinite theorem.

This iteration refocuses on the most concrete structured construction left by
the cross-direction compiler work: the adaptive suffixes `10` and `30`, their
renormalized irrational-rotation core, and the physically required zero-carry
condition.

Retain normalized exact block maps

\[
f_r(x)=\frac{3^{2r+1}}{2^{3r+2}}x+\frac14,
\]

where `x=p/4` is a positive integer at an exact block state.

---

## L-9524: zero-carry macro descent criterion

**Claim ID:** `L-9524`  
**Title:** A contracting exact macro whose fixed point lies below its canonical input cannot occur forever with zero carry  
**Status:** `PROPOSED`  
**Dependencies:** exact cylinder concatenation  
**Scope:** exact normalized macro words

Let an exact nonempty word `z` have normalized affine data

\[
f_z(x)=\frac{V_zx+B_z}{U_z},
\qquad U_z>V_z>0,
\]

and canonical exact input/output

\[
0\le A_z<U_z,
\qquad
Y_z=f_z(A_z)\in\mathbb Z_{\ge0}.
\]

Its real fixed point is

\[
t_z=\frac{B_z}{U_z-V_z}.
\]

Suppose

\[
\boxed{A_z>t_z.}
\tag{1}
\]

If an exact prefix has canonical normalized endpoint `Y` and appending `z`
has zero ordinary carry, then

\[
Y=A_z+kU_z
\qquad(k\in\mathbb Z_{\ge0})
\]

and

\[
\boxed{f_z(Y)<Y.}
\tag{2}
\]

Consequently no infinite positive exact orbit can be decomposed, after some
time, into zero-carry concatenations of words from a finite family satisfying
(1).

### Proof

Zero carry means that the old initial representative already realizes `z`.
The interface state therefore lies in the exact input progression of `z`:

\[
Y=A_z+kU_z.
\]

Since `U_z>V_z`, the map is strictly contracting and

\[
Y-f_z(Y)
=
\frac{(U_z-V_z)(Y-t_z)}{U_z}.
\]

Condition (1) and `Y>=A_z` make the right side strictly positive. Since the
interface endpoints are positive integers, infinitely many such macro steps
would give an infinite strict descent. QED.

---

## L-9525: the `10/30` compiler cannot produce an ordinary counterexample

**Claim ID:** `L-9525`  
**Title:** Both the raw zero-carry compiler and its renormalized Sturmian core are nonphysical as infinite positive H orbits  
**Status:** `PROPOSED`  
**Dependencies:** `L-9524`; `T-9502` (or `T-9506` plus `L-9504`);
cross-direction exact compiler data `L-9814`, `L-9822`, `L-9827`  
**Scope:** the adaptive compiler suffixes `10` and `30`

### Part A: raw zero-carry suffixes strictly descend

The exact normalized data are

\[
\begin{array}{c|ccccc}
z&U_z&V_z&B_z&A_z&Y_z\\ \hline
10&128&81&56&72&46\\
30&8192&6561&3584&4608&3691.
\end{array}
\]

Thus

\[
f_{10}(Y)=\frac{81Y+56}{128},
\qquad
t_{10}=\frac{56}{47}<72=A_{10},
\]

and

\[
f_{30}(Y)=\frac{6561Y+3584}{8192},
\qquad
t_{30}=\frac{3584}{1631}<4608=A_{30}.
\]

By `L-9524`, every zero-carry use of either suffix strictly lowers the positive
integer endpoint. More explicitly,

\[
Y-f_{10}(Y)=\frac{47Y-56}{128}>0
\quad(Y\ge72),
\]

\[
Y-f_{30}(Y)=\frac{1631Y-3584}{8192}>0
\quad(Y\ge4608).
\]

Therefore

\[
\boxed{
\text{no infinite positive exact orbit is eventually a zero-carry concatenation
of }10\text{ and }30.
}
\tag{3}
\]

### Part B: undoing the terminal zeros gives bounded capital

Removing the common terminal zero leaves the adaptive letters `3` and `1`.
Their multiplier phase is conjugate to the irrational rotation on

\[
\mathcal K=(1,81/64]
\]

from `L-9822`. If `R_n` is that phase and `M_n` is the cumulative exact block
multiplier, then

\[
M_n/M_0=R_n/R_0.
\]

Hence `M_n` remains bounded above and bounded away from zero. The branch word
is aperiodic.

If this renormalized word were the itinerary of a positive exact orbit, the
exact toll formula would give

\[
p_n=M_n\left(p_0+\sum_{j=1}^n\frac1{M_j}\right)=\Theta(n).
\]

The states are distinct because the itinerary is aperiodic. Therefore

\[
\sum_n\frac1{p_n}=\infty.
\]

But `T-9506` gives finite harmonic mass for the whole infinite-survivor set.
Equivalently, `T-9502` says every nonperiodic survivor has `M_n->infinity`.
Either formulation is a contradiction. Thus

\[
\boxed{
\text{the renormalized Sturmian }3/1\text{ compiler core is not an ordinary
positive exact orbit.}
}
\tag{4}
\]

---

## R-9507: abstract tail freedom is not physical ordinary freedom

**Claim ID:** `R-9507`  
**Title:** Full `2`-adic tail surjectivity of the compiler does not construct a positive ordinary orbit  
**Status:** `PROPOSED`  
**Dependencies:** `L-9525`, cross-direction `L-9827`

The exact tail maps attached to `10` and `30` are surjective left shifts on the
full abstract `2`-adic tail after an affine translation. This gives
`2^7` and `2^13` abstract inverse choices.

A positive ordinary orbit, however, requires eventual zero **ordinary carry**.
On that physical slice, `L-9525` Part A converts the same suffixes into strict
integer descent. Undoing the terminal zeros converts the construction into the
bounded-capital irrational rotation excluded in Part B.

Therefore neither the full-shift tail geometry nor the Sturmian phase core is
a counterexample construction. Any successful structured counterexample must
use a different macro family whose physical zero-carry return is genuinely
expanding and whose cumulative multiplier escapes.

---

## X-9508: exact structured-renewal box audit

The finite audit enumerates centered stars

\[
3^aX+1=8^RU,
\qquad
X\equiv5\pmod6,
\qquad
U\equiv1\pmod4,
\]

using the canonical residue and the first `t_max+1` ordinary lifts for

\[
1\le a\le30,
\qquad
1\le R\le20,
\qquad
0\le t\le2000.
\]

It then iterates the exact renewal map

\[
4^bY+1=9^RU
\]

until the first illegal bridge or 100 renewals.

The frozen run checked

\[
1,200,600
\]

canonical stars, of which

\[
800,375
\]

had the prescribed first renewal. It found no cycle. The maximum exact renewal
life was five, attained from

\[
(a,R,t,X)=(6,8,1486,299172995735).
\]

The exact trajectory is recorded in the experiment result. Digest:

```text
0dd31788d926b9d5a815860a97e8d16300cb627c4b3dabba5dbed15c449a7eda
```

This is finite negative evidence only.

---

## Q-9511: remaining construction interface

**Claim ID:** `Q-9511`  
**Title:** Find a physical expanding macro family, not merely an abstract tail shift  
**Status:** `IDEA`

The adaptive `10/30` compiler is now closed as a counterexample architecture.
A viable construction must supply exact macros `z_i` and one positive ordinary
initial state such that:

1. every late macro has zero ordinary carry;
2. the exact integer endpoint does not descend;
3. the cumulative macro multiplier tends to infinity;
4. the physical tail remains in the exact input cylinder at every stage;
5. one finite initialization and induction prove all four properties.

Abstract `2`-adic surjectivity, a renormalized phase rotation, or arbitrarily
long finite cylinders do not meet this interface.
