# A universal obstruction to strict finite-window ranks

`CollatzGlobalClosure/LocalProfileObstruction.lean` proves an infinite-family theorem, not a
bounded search result. It is a constraint on one proposed proof architecture,
not a proof or disproof of the Collatz conjecture.

## Exact theorem

For every memory width `r` and every size bound `B`, there are odd natural
numbers `n > m > 1` such that

\[
n>B,\qquad 3n+1=4m,\qquad H_r(n)=H_r(m).
\]

Here `H_r` is the complete multiset of binary windows of length `r+1`,
after padding the ordinary binary expansion by `r` zero bits on both ends.
The formal definition scans `Nat.digits 2 n` from least significant to
most significant, encoding the previous `r` bits in `ZMod (2^r)`.

`Odd m` makes the factor `4` exact: the accelerated odd Collatz map takes
`n` to `m`. The file also proves the corresponding two-step identity for
the shortcut map `n/2` or `(3n+1)/2`.

Consequently, for any preordered codomain and any function `F` of this
histogram, `F(H_r(n))` cannot strictly decrease at every odd Collatz step,
even if all starting values below an arbitrary threshold are exempted.
This includes arbitrary nonlinear functions of the full fixed-width
histogram, and hence arbitrary weighted sums of those local patterns.

## Construction and proof

Fix `r` and `B`. Put

\[
g=r+2,\quad D=6\cdot2^r-1,
\quad L=\varphi(D)(r+B+5),\quad s=L-g.
\]

The modulus `D` is positive and odd. Euler's theorem gives
`2^L ≡ 1 (mod D)`, so the explicitly defined natural number

\[
A=\left\lfloor\frac{2^L}{D}\right\rfloor
\]

satisfies

\[
DA+1=2^{g+s}.
\]

The proof establishes `s ≥ B+3`, `A` odd, `A>1`, and
`2^(s−1) ≤ A < 2^s`; therefore `A` has exactly `s` binary digits. Set

\[
n=A2^{g+1}+1,\qquad m=2^{g+s}+A.
\]

Then

\[
n=8\cdot2^rA+1,\qquad m=6\cdot2^rA+1,
\qquad 3n+1=4m.
\]

Their least-significant-first binary words are

\[
1\,0^g\,\operatorname{digits}(A)
\quad\hbox{and}\quad
\operatorname{digits}(A)\,0^g\,1.
\]

A zero word of length at least `r` resets the finite binary context to
zero. The two padded scans therefore traverse the same two closed
context walks in opposite order. Their edge multisets are equal by
commutativity; cancelling the identical excess terminal zero padding
gives the stated `r`-padded profile equality.

## Scope

The theorem excludes a strict rank depending only on any one fixed
finite-window histogram. It does not exclude phase-dependent ranks,
variable-length multi-step ranks, variable context width, position-sensitive
ranks, matrix products, or ordinal ranks. In particular, it does not
establish that a broader ranking method cannot prove Collatz.

## Reproduction

The file compiles with Lean `4.34.1` and mathlib `v4.34.1`, pinned at
`d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
lake env lean -DwarningAsError=true CollatzGlobalClosure/LocalProfileObstruction.lean
```

The two principal theorem axiom reports contain only `propext`,
`Classical.choice`, and `Quot.sound`. There are no `sorry` terms or custom
axioms, and the theorem does not depend on the numerical linear-programming
experiments that motivated this construction.
