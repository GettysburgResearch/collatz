# L-9312 — Exact square-root lift to a paired `8 -> 9` chart

**Claim ID:** L-9312  
**Title:** The `64 -> 81` ordinary section is exactly the even-time subsystem of a duplicated-digit `8 -> 9` chart  
**Status:** PROPOSED / CORRECTED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9315`; elementary affine algebra  
**Scope:** the centered-power ordinary-section reformulation  
**Related counterexample candidates:** none

## 0. Correction notice

An earlier version of this claim used the false identity

\[
81/64=(3/2)^4.
\]

In fact

\[
\boxed{
\frac{81}{64}=\left(\frac98\right)^2,
}
\tag{0}
\]

because `64=8^2`, not `2^4`.

The former four-phase `3/2` schedule is retracted. It is not a dependency of
`T-9315`, `L-9313`, `L-9314`, `T-9316`, `L-9315`, `L-9316`, `T-9317`, or
`T-9318`. The exact replacement is the paired `8 -> 9` lift below.

## 1. The `64 -> 81` chart

Let

\[
A_n\in\mathbb Z_{\ge2},
\qquad
 e_n\in\{0,1\},
\tag{1}
\]

satisfy

\[
\boxed{
64A_{n+1}=81A_n-17e_n.
}
\tag{2}
\]

Reduction modulo `64` gives

\[
\boxed{A_n\equiv e_n\pmod{64}.}
\tag{3}
\]

## 2. Exact integer square-root factorization

Define an integer sequence `(X_m)` and a binary sequence `(f_m)` by

\[
\boxed{
X_{2n}=A_n,
\qquad
X_{2n+1}=\frac{9A_n-e_n}{8},
}
\tag{4}
\]

and

\[
\boxed{
f_{2n}=f_{2n+1}=e_n.
}
\tag{5}
\]

Then every `X_m` is an ordinary integer and

\[
\boxed{
8X_{m+1}=9X_m-f_m,
\qquad
X_m\equiv f_m\pmod8.
}
\tag{6}
\]

### Proof

Write

\[
A_n=64k+e_n.
\]

Then

\[
X_{2n+1}
=\frac{9(64k+e_n)-e_n}{8}
=72k+e_n,
\]

so `X_(2n+1)` is integral and congruent to `e_n mod 8`. The first half-step
in `(6)` follows from its definition. For the second half-step,

\[
\frac{9X_{2n+1}-e_n}{8}
=
\frac{81A_n-17e_n}{64}
=A_{n+1}
=X_{2n+2},
\]

using `(2)`. Equation `(3)` supplies the even-time residue condition. QED.

Thus the original chart is not a four-phase `3/2` system. It is the exact
even-time compression of the `8 -> 9` binary chart, with every chart digit
repeated twice.

## 3. Converse compression

Conversely, suppose ordinary integers `X_m>=2` and binary digits `f_m` satisfy

\[
8X_{m+1}=9X_m-f_m,
\qquad
X_m\equiv f_m\pmod8,
\tag{7}
\]

and suppose

\[
f_{2n}=f_{2n+1}
\quad(n\ge0).
\tag{8}
\]

Put

\[
A_n=X_{2n},
\qquad
e_n=f_{2n}.
\]

Composing the two successive equations in `(7)` gives

\[
64A_{n+1}
=81A_n-(9+8)e_n
=81A_n-17e_n.
\]

The even-time residue condition in `(3)` follows by composing the two exact
`8`-adic cylinder conditions. Hence `(4)`--`(5)` give a bijection between:

1. nontrivial ordinary `64 -> 81` orbits; and
2. nontrivial ordinary `8 -> 9` orbits whose digit word is pairwise duplicated.

## 4. Real companion and centered parameter

Let `(x_n)` be the bounded real companion of `(A_n,e_n)`:

\[
64x_{n+1}=81x_n-17e_n,
\qquad
0<x_n<1.
\tag{9}
\]

Define

\[
\boxed{
y_{2n}=x_n,
\qquad
y_{2n+1}=\frac{9x_n-e_n}{8}.}
\tag{10}
\]

Then

\[
8y_{m+1}=9y_m-f_m,
\qquad
0<y_m<1.
\tag{11}
\]

The inequalities follow directly from the two branch ranges in `(9)`. By
uniqueness of the bounded real companion, `(y_m)` is exactly the real companion
of the paired `8 -> 9` orbit.

The original centered parameter is

\[
\xi=\frac{A_0-x_0}{64}.
\tag{12}
\]

For the `8 -> 9` chart the centered parameter is

\[
\boxed{
\zeta=\frac{X_0-y_0}{8}=8\xi.}
\tag{13}
\]

Therefore `T-9315`, applied with `(M,N)=(8,9)`, gives

\[
\boxed{
\left\|\zeta\left(\frac98\right)^m\right\|<\frac19
\quad(m\ge0),
}
\tag{14}
\]

and its sign itinerary is the duplicated word `(f_m)`.

## 5. Exact two-phase centered identities

Write the original centered orbit as

\[
\xi(81/64)^n=B_n+u_n,
\qquad
B_n\in\mathbb Z,
\qquad
|u_n|<1/81.
\tag{15}
\]

Equations `(0)` and `(13)` give

\[
\boxed{
\zeta(9/8)^{2n}=8B_n+8u_n,
}
\tag{16}
\]

and

\[
\boxed{
\zeta(9/8)^{2n+1}=9B_n+9u_n.
}
\tag{17}
\]

Hence the nearest integers at the two phases are exactly `8B_n` and `9B_n`,
with errors

\[
8u_n
\quad\text{and}\quad
9u_n.
\]

In particular,

\[
\left\|\zeta(9/8)^{2n}\right\|<\frac8{81},
\qquad
\left\|\zeta(9/8)^{2n+1}\right\|<\frac19.
\tag{18}
\]

The two errors have the same sign. This is the exact phase geometry replacing
the invalid four-phase schedule.

## 6. Approximate-multiplication normal form

Put

\[
H_m=X_m-1,
\qquad
S_m=1-f_m.
\tag{19}
\]

Then `(6)` is equivalent to

\[
\boxed{
8H_{m+1}=9H_m+S_m,
\qquad
H_m\pmod8\in\{0,7\}.
}
\tag{20}
\]

The pair constraint becomes

\[
S_{2n}=S_{2n+1}.
\tag{21}
\]

Thus the ordinary-section problem is exactly the termination/nonstabilization
problem for the paired sublanguage of the approximate-multiplication system

\[
(p,q,S)=(9,8,\{0,7\}).
\]

At even times, setting `h_n=H_(2n)` and `s_n=S_(2n)` recovers

\[
\boxed{
64h_{n+1}=81h_n+17s_n,
\qquad
h_n\pmod{64}\in\{0,63\}.
}
\tag{22}
\]

## 7. Consequence for the proof program

The corrected factorization supplies two exact routes:

1. work directly with the original `64 -> 81` appended blocks `q_K`;
2. work with the simpler `8 -> 9` chart while retaining the load-bearing
   duplicated-digit constraint.

Dropping the pair constraint enlarges the problem to the full two-residue
`(9,8,{0,7})` approximate-multiplication problem and is not a valid proof
shortcut.

## 8. Dependency audit

- The integer factorization uses only `81=9^2`, `64=8^2`, and `17=9+8`.
- `T-9315` supplies the centered equivalence for the `8 -> 9` chart.
- No external rational-power theorem is a dependency.
- `L-9313`, `L-9314`, `T-9316`, `L-9315`, `L-9316`, `T-9317`, and `T-9318`
  do not depend on the retracted four-phase claim.

## 9. Gap audit

- The paired `8 -> 9` reformulation is exact but does not prove termination.
- A theorem for an unrestricted `8 -> 9` digit language cannot be imported
  without checking the pair constraint and direction of implication.
- The centered interval in `(14)` is a torus interval of total length `2/9`,
  not an ordinary interval of length `1/9`; the critical one-interval theorem
  cannot be applied by halving its length.
- Translation from this induced subsystem to every possible Collatz
  counterexample remains separate.
