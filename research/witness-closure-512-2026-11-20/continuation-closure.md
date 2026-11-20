# Continuation: global multiplication closure and its exact boundary

**The original 512-residue implication remains OPEN.** This note proves an
equivalence involving a stronger global closure property and records which
weaker multiplication statements follow conditionally from the original
bridges. It does not establish the missing implication between them.

All arguments are direct finite integer algebra using the supplied
definition of `E` and the witness/trajectory equivalence in
[the proof packet](README.md). No external convergence theorem is assumed.

For positive odd `n`, put

\[
T(n)=\frac{3n+1}{2^{\nu_2(3n+1)}},\qquad
J(n)=4n+1,\qquad H(n)=2n+1.
\]

We use the proved identities

\[
J(n)\in E\Longleftrightarrow n\in E,
\tag{CL.1}
\]

\[
4^d n+1\in E\Longleftrightarrow3^{d-1}n\in E
\quad(d\geq1),
\tag{CL.2}
\]

and

\[
T^d(2\cdot4^d n+1)=2\cdot3^d n+1
\quad(d\geq0).
\tag{CL.3}
\]

Every parameter to which membership in `E` is applied below is a positive
odd integer.

## CL-001: three equivalent global statements

The following statements are equivalent:

1. Every positive odd integer belongs to `E`.
2. For every positive odd \(n\in E\), one has \(3n\in E\).
3. For every positive odd \(n\in E\), one has \(H(n)=2n+1\in E\).

Statement 1 trivially implies statements 2 and 3. The other directions
require the following argument.

### Global multiplication by 3 implies a preliminary `H(3n)` closure

Assume statement 2. Given \(n\in E\), (CL.1) gives \(J(n)\in E\).
Applying statement 2 twice gives \(9J(n)\in E\). But

\[
9J(n)=36n+9=J(9n+2),
\]

so \(9n+2\in E\). Also

\[
T(6n+1)=9n+2,
\]

because \(3(6n+1)+1=2(9n+2)\) and \(9n+2\) is odd. Consequently

\[
\boxed{n\in E\Longrightarrow H(3n)=6n+1\in E.}
\tag{CL.4}
\]

This lemma has been obtained directly from statement 2. It does not assume
statement 3 or any bound on the length of a multiplication witness.

### Global multiplication by 3 implies global `H` closure

We prove statement 3 by induction on the length `r` of a supplied witness
for `n`. The base `r=0` means `n=1`, and `H(1)=3` has the finite trajectory
\(3\to5\to1\).

For `r>0`, write

\[
a=\nu_2(3n+1),\qquad t=T(n).
\]

Dropping the first step of the supplied witness gives a witness of length
`r-1` for `t`. Since `n` is odd,

\[
T(H(n))=3n+2=2^a t+1.
\tag{CL.5}
\]

There are three cases.

* If \(a=2d\), with \(d\geq1\), then (CL.2) and (CL.5) give
  \[
  H(n)\in E\Longleftrightarrow3^{d-1}t\in E.
  \]
  Repeated application of statement 2 supplies this membership from
  \(t\in E\).
* If \(a=2d+1\), with \(d\geq1\), then (CL.3) and (CL.5) give
  \[
  H(n)\in E\Longleftrightarrow H(3^d t)\in E.
  \]
  Statement 2 supplies \(w=3^{d-1}t\in E\), and the already proved
  lemma (CL.4) supplies \(H(3w)=H(3^d t)\in E\).
* If `a=1`, then (CL.5) gives
  \[
  H(n)\in E\Longleftrightarrow H(t)\in E.
  \]
  The induction hypothesis applies to the shorter supplied witness for
  `t`.

Only the last case invokes the witness-length induction. In the other
cases, new multiplication witnesses may have arbitrary finite lengths;
the proof never asserts that these witnesses are shorter. This distinction
prevents a circular induction.

### Global `H` closure implies all positive odd integers belong to `E`

Assume statement 3 and use strong induction on a positive odd integer `N`.
The case `N=1` is the empty witness.

If \(N>1\) and \(N\equiv1\pmod4\), then

\[
T(N)\leq\frac{3N+1}{4}<N.
\]

The induction hypothesis gives \(T(N)\in E\), and prepending one step
gives \(N\in E\).

If \(N\equiv3\pmod4\), then \(n=(N-1)/2\) is a smaller positive odd
integer. The induction hypothesis gives \(n\in E\), and statement 3 gives
\(N=H(n)\in E\).

This proves statement 1 and completes the equivalence.

## CL-002: what the original bridges imply conditionally

For the remainder of this section only, assume the full unproved bridge
assertion: for every positive odd `m`, both

\[
P(m):\quad27m\in E\Longrightarrow54m+1\in E
\]

and

\[
Q(m):\quad54m+1\in E\Longrightarrow9m\in E
\]

hold. These assumptions are equivalent to the original 512-residue claim,
as proved in W512-020 of the proof packet.

### Removing a factor of 3 above the level of 9

Applying `P(m)` and then `Q(m)` gives

\[
27m\in E\Longrightarrow9m\in E.
\]

In particular, for every positive odd `z` and every \(j\geq3\),

\[
\boxed{3^jz\in E\Longrightarrow3^{j-1}z\in E.}
\tag{CL.6}
\]

This does not give either `9z in E => 3z in E` or `3z in E => z in E`
for arbitrary positive odd `z`.

### Multiplication by every higher power of 3 for a known 3-unit

Let \(z\in E\) and assume \(3\nmid z\). Then, conditionally on all
`P` and `Q`,

\[
\boxed{3^jz\in E\qquad\text{for every }j\geq2.}
\tag{CL.7}
\]

Here is the complete lifting argument. The residue of 2 has order 54
modulo 81: direct calculation gives

\[
2^{18}\equiv28\pmod{81},\qquad
2^{27}\equiv-1\pmod{81},\qquad
2^{54}\equiv1\pmod{81}.
\]

These exclude both proper maximal divisors 18 and 27 of 54. There are 54
units modulo 81, so powers of 2 comprise all of them. Consequently there
are arbitrarily large integers `a` with

\[
2^a z\equiv1\pmod{81}.
\]

For each such `a`, put

\[
A=\frac{2^a z-1}{3}=27m,
\qquad m=\frac{2^a z-1}{81}.
\]

Taking `a` large makes `m` positive; it is odd. Since \(T(A)=z\), we
have \(A\in E\). The assumed `P(m)` gives \(H(A)\in E\), and

\[
T(H(A))=2^a z+1.
\]

If \(a=2d\), (CL.2) gives \(3^{d-1}z\in E\). If
\(a=2d+1\), (CL.3) gives \(H(3^d z)\in E\). For `d>=3`, the
assumed `Q` at \(m'=3^{d-3}z\) then gives \(3^{d-1}z\in E\).

Replacing `a` by `a+54` produces arbitrarily large exponents `d-1` in
both cases. Repeated use of (CL.6) reduces any sufficiently large one to
any prescribed \(j\geq2\), proving (CL.7).

The condition \(3\nmid z\) enters at the congruence
\(2^a z\equiv1\pmod{81}\). If \(3\mid z\), this congruence is
impossible; indeed \((2^a z-1)/3\) is never an integer. The proof therefore
does not extend to such `z` by repeating the same construction.

As a conditional corollary, all powers of 3 belong to `E`: use `z=1` in
(CL.7), and note the explicit witnesses for 1 and 3. This is a consequence
of the unproved bridges, not an unconditional conclusion of this note.

### A limited `H(3n)` closure and a reverse direction for `Q`

If \(n\in E\) and \(n\not\equiv2\pmod3\), then
\(J(n)\not\equiv0\pmod3\). Conditional formula (CL.7), applied to
`J(n)`, gives \(9J(n)\in E\). The same algebra used in (CL.4) yields

\[
\boxed{
n\in E,\quad n\not\equiv2\pmod3
\Longrightarrow H(3n)\in E.
}
\tag{CL.8}
\]

In particular, take \(n=9m\). Combining (CL.8) with the assumed `Q(m)`
shows that, under the full bridge assumption,

\[
\boxed{54m+1\in E\Longleftrightarrow9m\in E.}
\tag{CL.9}
\]

This does not reverse `P(m)` and does not establish \(3n\in E\) from
\(n\in E\).

## CL-003: an unconditional multiplication-by-3 merger on one class

There is also an exact positive result that does not assume the original
bridges. For every \(n\equiv187\pmod{256}\), \(n>0\),

\[
\boxed{3n\in E\Longleftrightarrow n\in E.}
\tag{CL.10}
\]

Write \(n=256t+187\), where `t>=0`. From `3n`, the exact exponent word
\([2,4,1]\) gives the following odd states:

\[
768t+561\ \longrightarrow\ 576t+421
\ \longrightarrow\ 108t+79
\ \longrightarrow\ 162t+119.
\]

From `n`, the exact word \([1,2,1,3]\) gives

\[
256t+187\ \longrightarrow\ 384t+281
\ \longrightarrow\ 288t+211
\ \longrightarrow\ 432t+317
\ \longrightarrow\ 162t+119.
\]

At every displayed step, applying \((3x+1)/2^a\) with the indicated
exponent gives the next positive odd integer. Thus the exponents are
maximal and the two ordinary trajectories merge. Their common endpoint is

\[
\frac{81n+85}{128}.
\]

Either supplied witness can therefore be converted to a witness for the
other input by replacing its displayed prefix and retaining the suffix.

For a particular infinite family of powers, direct modular calculation
gives

\[
3^{27}\equiv187\pmod{256},\qquad
3^{32}\equiv129\pmod{256},\qquad
3^{64}\equiv1\pmod{256}.
\]

The order of 3 modulo 256 is therefore 64: it divides 64, and every proper
divisor of 64 divides 32. Applying (CL.10) to
\(n=3^{64q+27}\) gives the unconditional equivalence

\[
\boxed{
3^{64q+27}\in E\Longleftrightarrow3^{64q+28}\in E
\qquad(q\geq0).
}
\tag{CL.11}
\]

This is an equivalence of memberships, not an assertion that either
membership has been established for every `q`.

## 4. The first unsupported strengthening

CL-001 proves that **global** multiplication-by-3 closure would already
prove membership in `E` for every positive odd integer. CL-002 proves only
the following conditional pieces from the original bridges:

* upward multiplication by \(3^j\), `j>=2`, when the known starting
  integer is not divisible by 3;
* downward removal of a factor of 3 when the known integer is divisible
  by 27;
* the restricted `H(3n)` implication (CL.8).

Two extensions remain unproved here: the missing first upward factor for
known 3-units, and upward multiplication for known integers already
divisible by 3. Even proving only the former would not, by itself, meet
the hypotheses of the global theorem CL-001.

The distinction is visible in the proof: the unrestricted preliminary
lemma (CL.4) needs \(9J(n)\in E\) even when \(J(n)\) is divisible by
3. Formula (CL.7) cannot supply this when \(n\equiv2\pmod3\).
Replacing the restricted statement by the unrestricted one without a new
argument would be the first unsupported step.

Thus this note neither proves the original bridges nor proves that those
bridges are equivalent to convergence of every positive odd integer. It
identifies a precise stronger closure whose proof would have that force.
