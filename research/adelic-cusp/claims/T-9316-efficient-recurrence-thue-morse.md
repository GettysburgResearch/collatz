# T-9316 — Efficient recurrence cone and Thue--Morse block nonstabilization

**Claim ID:** T-9316  
**Title:** Efficient repeated factors cannot occur in an ordinary survivor; every Thue--Morse extremal has infinitely many nonzero cylinder blocks  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `L-9311`, `L-9313`, `T-9315`  
**Scope:** symbolic recurrence inside the ordinary `64 -> 81` section; native bridge to Thue--Morse extremals in rational-power literature  
**Related counterexample candidates:** none

## 1. The global recurrence cone

Put

\[
\beta=\frac{81}{64},
\qquad
\delta=\log_{64}\beta
       =\log_{64}81-1.
\tag{1}
\]

Suppose that

\[
A_0\ge2
\]

is a nontrivial ordinary survivor with binary itinerary

\[
e=(e_n)_{n\ge0}.
\]

Assume equal factors of length `ell` begin at positions `r<t`:

\[
e_{r+i}=e_{t+i}
\qquad(0\le i<\ell).
\tag{2}
\]

Then

\[
\boxed{
\ell
<
\delta t+\log_{64}A_0.
}
\tag{3}
\]

### Proof

`L-9311` gives the local orbit-difference bound

\[
\ell
<
\delta(t-r)+\log_{64}A_r.
\tag{4}
\]

The ordinary tail growth estimate from `D-9302` gives

\[
A_r\le\beta^rA_0.
\tag{5}
\]

Hence

\[
\log_{64}A_r
\le
\delta r+\log_{64}A_0.
\tag{6}
\]

Substitution of `(6)` into `(4)` proves `(3)`. QED.

## 2. Efficient-recurrence obstruction

Let an infinite binary itinerary `e` contain equal-factor triples

\[
(r_j,t_j,\ell_j),
\qquad
0\le r_j<t_j,
\qquad
\ell_j\to\infty,
\tag{7}
\]

such that

\[
\boxed{
\ell_j-\delta t_j\longrightarrow+\infty.
}
\tag{8}
\]

Then `e` cannot be the itinerary of a nontrivial ordinary survivor.

Equivalently, its selected nearest-integer completion point from `L-9313` is not an ordinary positive integer, and its appended base-64 cylinder blocks cannot be eventually zero.

Indeed, `(3)` would imply

\[
\ell_j-\delta t_j
<
\log_{64}A_0
\tag{9}
\]

for every `j`, contradicting `(8)`.

A useful sufficient form is

\[
\limsup_{j\to\infty}
\frac{t_j}{\ell_j}
<
\frac1\delta.
\tag{10}
\]

Thus the obstruction is geometric: a repeated block that returns too early relative to its length is incompatible with one fixed ordinary starting room.

## 3. Thue--Morse squares

Let `tau` be the Thue--Morse fixed point of the length-two morphism

```text
mu(0)=01,
mu(1)=10.
```

Thus

```text
tau = 01101001...
```

with zero-based indexing. The two symbols at positions `1` and `2` are both one:

```text
tau[1:3] = 11.
```

Applying `mu^m` to this occurrence gives, for every `m>=0`,

\[
\boxed{
\tau[2^m:2\cdot2^m]
=
\mu^m(1)
=
\tau[2\cdot2^m:3\cdot2^m].
}
\tag{11}
\]

The repeated factors in `(11)` have

\[
\ell_m=2^m,
\qquad
t_m=2\cdot2^m.
\tag{12}
\]

Therefore

\[
\ell_m-\delta t_m
=
(1-2\delta)2^m.
\tag{13}
\]

The coefficient is positive. Indeed,

\[
2\delta<1
\iff
\left(\frac{81}{64}\right)^2<64
\iff
81^2<64^3.
\tag{14}
\]

The last inequality is immediate:

\[
81^2=6561<262144=64^3.
\tag{15}
\]

Hence `(13)` tends to `+infinity`, and the efficient-recurrence obstruction applies.

## 4. Shift and complement closure

Let `s>=0` be fixed. For every sufficiently large `m` with `2^m>s`, the shifted word

\[
\sigma^s\tau
\]

contains the same two factors at starts

\[
r_m=2^m-s,
\qquad
t_m=2\cdot2^m-s.
\tag{16}
\]

Then

\[
\ell_m-\delta t_m
=
(1-2\delta)2^m+\delta s
\longrightarrow+\infty.
\tag{17}
\]

Bitwise complementation preserves equality of factors. Consequently:

\[
\boxed{
\text{No finite shift of the Thue--Morse word or its complement}
\text{ is an ordinary survivor itinerary.}
}
\tag{18}
\]

## 5. Appended-block consequence

For any itinerary `e`, write

\[
R_{K+1}=R_K+q_K64^K,
\qquad
q_K\in\{0,\ldots,63\},
\tag{19}
\]

for the nearest-integer cylinders from `L-9313` and `L-9314`.

If `(q_K)` were eventually zero, the least representatives would stabilize at one ordinary nonnegative integer. A nonconstant Thue--Morse shift cannot stabilize at zero: the recurrence with initial nearest integer zero would force every digit difference to vanish and hence the entire itinerary to be constant. Therefore eventual zero would give a positive ordinary lift, contradicting `(18)`.

Thus

\[
\boxed{
\text{Every finite shift of Thue--Morse, and every complemented shift,}
\text{ has infinitely many }q_K\ne0.
}
\tag{20}
\]

This is the requested native translation of the literature's Thue--Morse extremal pattern into the appended-cylinder language.

## 6. General constant-length morphism corollary

The same argument applies to any fixed point of a constant-length morphism of length `L` containing two equal adjacent letters at positions `a,a+1`.

Applying the `m`-th morphism iterate produces equal adjacent factors of length `L^m` with second start `(a+1)L^m`. Therefore the fixed point is excluded whenever

\[
\boxed{
(a+1)\delta<1.
}
\tag{21}
\]

No automaticity theorem is used. The proof needs only one explicit self-similar family of efficient repeated factors.

## 7. Literature interface

The wave-5 literature audit asks that any Dubickas extremal Thue--Morse sign word be translated into the native appended blocks.

A sign convention converts that word into either `tau` or its complement; a choice of starting phase produces at most a finite shift. Equation `(20)` shows unconditionally that none of these extremal symbolic candidates can have an eventual-zero block tail.

This does **not** assert that the uninspected Dubickas equality classification for `(p,q)=(81,64)` has exactly this form. It proves the native half of the bridge in advance: if the source equality language is a shifted/complemented Thue--Morse language, arithmetic stabilization is impossible.

## 8. Dependency audit

- `L-9311` supplies the local repeated-factor height bound.
- `D-9302` supplies the ordinary tail growth estimate used in `(5)`.
- `L-9313` supplies nearest-integer cylinders and the stabilization criterion.
- `T-9315` identifies a positive stabilized cylinder with a nontrivial centered ordinary orbit.
- The Thue--Morse square construction is elementary morphism algebra.
- No external theorem, computation, or PR-#20 result is a proof dependency.

## 9. Gap audit

- The theorem excludes one important extremal symbolic family, not every itinerary.
- A Dubickas lower-bound theorem still requires full-source acquisition and exact specialization at `(81,64)`.
- The source extremal language must not be assumed to be Thue--Morse without checking its exact equality statement and sign convention.
- Efficient recurrence is sufficient for nonstabilization, not necessary; a high-complexity ordinary candidate could avoid this obstruction.
- The translation from the induced chart to every possible Collatz counterexample remains separate.

## 10. Suggested next attack

Use `T-9316` as the equality-case half of a source bridge:

1. specialize the exact Dubickas lower constant `rho_(81,64)`;
2. if `rho_(81,64)>1/81`, close the ordinary section directly;
3. if equality holds, audit whether every equality sign word is a shifted/complemented Thue--Morse word or, more generally, satisfies `(8)`;
4. only if the constant is smaller should a new native block estimate be required.
