# L-6809 — Lossless prime-power compiler for first-crossing near-cycles

**Claim ID:** `L-6809`  
**Status:** **PROPOSED / SOURCE-QUALIFIED EXACT REDUCTION**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Last updated:** 2026-07-31  
**Dependencies:** `L-6803`, `L-6807`, `L-6812`; PR #34 `L-9909/L-9914` full-order window and excess-path CRT method  
**Scope:** complete prime-power factorizations of first-crossing denominators  
**Counterexample status:** none

## 1. Setup

Let `w` be a shortcut parity word of length `j` and weight `q`, with first
bit one and final bit zero. Put

\[
P=2^j,
\qquad
Q=3^q,
\qquad
D=P-Q>1,
\qquad
E=j-q.
\tag{1}
\]

Write the odd positions as

\[
0=d_1<d_2<\cdots<d_q\le j-2
\tag{2}
\]

and define the nondecreasing even-excess path

\[
e_i=d_i-(i-1)
\qquad(1\le i\le q).
\tag{3}
\]

Then

\[
0=e_1\le e_2\le\cdots\le e_q\le E-1.
\tag{4}
\]

The affine numerator is

\[
\boxed{
A_w
=
\sum_{i=1}^{q}
3^{q-i}2^{i-1+e_i}.}
\tag{5}
\]

A canonical non-descending first crossing has one displacement

\[
\boxed{
0\le\Delta<q/3}
\tag{6}
\]

by `L-6812`, and satisfies

\[
\boxed{
D\mid A_w-P\Delta,
\qquad
r_w=\frac{A_w-P\Delta}{D},
\qquad
T^j(r_w)=r_w+\Delta.}
\tag{7}
\]

Equivalently,

\[
D\mid A_w-Q\Delta,
\]

and the endpoint is `(A_w-Q Delta)/D`.

## 2. Complete local order data

Factor the complete denominator into pairwise coprime prime powers:

\[
D=\prod_{s=1}^{t}Q_s,
\qquad
Q_s=p_s^{\nu_s}.
\tag{8}
\]

Put

\[
h_s=\operatorname{ord}_{Q_s}(2),
\qquad
H=\operatorname{lcm}_{s}h_s
=\operatorname{ord}_{D}(2).
\tag{9}
\]

The full-order theorem in PR #34 `L-9909/L-9914`, specialized to
`(A,k)=(j,q)`, gives the source-qualified strict window

\[
\boxed{H>E.}
\tag{10}
\]

The primary logarithmic-form dependency of that order theorem retains its
source status here.

For every factor and every odd index, define the local excess residue

\[
\epsilon_{s,i}\equiv e_i\pmod{h_s}.
\tag{11}
\]

## 3. Exact reconstruction theorem

Suppose local data

\[
\epsilon_{s,i}\in\mathbf Z/h_s\mathbf Z
\qquad
(1\le s\le t,\ 1\le i\le q)
\]

and one ordinary integer `Delta` satisfying `(6)` are given.

There is a **coefficient-first-crossing** word whose excess path realizes the
local data and whose shifted numerator satisfies `(7)` if and only if all of
the following conditions hold.

### A. Generalized-CRT compatibility

For every `i,s,u`,

\[
\boxed{
\epsilon_{s,i}
\equiv
\epsilon_{u,i}
\pmod{\gcd(h_s,h_u)}.}
\tag{12}
\]

Let `hat e_i in [0,H-1]` be the simultaneous CRT representative.

### B. Ordinary path window

\[
\boxed{
0=\widehat e_1
\le
\widehat e_2
\le\cdots\le
\widehat e_q
\le E-1.}
\tag{13}
\]

Because of `(10)`, this is the unique integer path in the physical window.
Define

\[
\widehat d_i=i-1+\widehat e_i.
\tag{14}
\]

The positions `(14)` reconstruct one unique binary word with first bit one,
last bit zero, length `j`, and weight `q`.

### C. Exact first-crossing prefix barrier

For every proper prefix `1<=m<j`, put

\[
\widehat S_m
=
\#\{i:\widehat d_i<m\}.
\tag{15}
\]

Require

\[
\boxed{
3^{\widehat S_m}\ge2^m
\qquad(1\le m<j),}
\tag{16}
\]

and retain the final crossing already encoded by `D>0`:

\[
\boxed{3^q<2^j.}
\tag{17}
\]

Condition `(16)` is essential. Monotonicity of the excess path alone
recognizes an ordinary parity word, not a first-crossing word.

### D. Complete prime-power shifted-numerator equations

For every `s`,

\[
\boxed{
\sum_{i=1}^{q}
3^{q-i}2^{i-1+\epsilon_{s,i}}
\equiv
3^q\Delta
\pmod{Q_s}.}
\tag{18}
\]

Here powers of two are reduced modulo their exact local order `h_s`.  The
right side is the endpoint-coordinate shift from `L-6812`; modulo `D` it is
equivalent to the source-coordinate shift `P Delta`.

### E. Canonical positive range

Let

\[
\widehat A
=
\sum_{i=1}^{q}
3^{q-i}2^{i-1+\widehat e_i}
\tag{19}
\]

and define the canonical source

\[
\widehat r
=
\frac{\widehat A-P\Delta}{D}.
\tag{20}
\]

Require

\[
\boxed{1\le\widehat r\le P.}
\tag{21}
\]

Then `(hat r,hat r+Delta)` is the canonical source--endpoint pair.

## 4. Proof

An actual canonical near-cycle gives `(11)--(17)` immediately. Equation
`(18)` is `(7)` reduced modulo each complete prime-power factor, using
`P congruent Q (mod D)` and formula `(5)`.

Conversely, `(12)` is the exact compatibility criterion for simultaneous
congruences with noncoprime moduli. The representatives in `(13)` produce one
legal excess path and hence one binary word. Strict window `(10)` makes the
lift unique. Conditions `(16)--(17)` certify that this reconstructed word is
coefficient-first-crossing rather than merely parity-compatible.

Equation `(18)` at every complete prime-power factor gives

\[
D\mid\widehat A-Q\Delta.
\]

Since `P congruent Q (mod D)`,

\[
D\mid\widehat A-P\Delta.
\tag{22}
\]

Thus `(20)` is integral. Equations `(19)--(22)` give

\[
Q\widehat r+\widehat A
=P(\widehat r+\Delta).
\tag{23}
\]

Condition `(21)` places `hat r` in the canonical source rectangle.  By the
finite parity-cylinder bijection, `(23)` gives complete ordinary physical
replay of the reconstructed first-crossing word, with canonical endpoint
`hat r+Delta`.

This proves necessity and sufficiency.

## 5. Order-cover subsets

Let `S` be a subset of the prime-power factors and put

\[
H_S=\operatorname{lcm}_{s\in S}h_s.
\]

If

\[
H_S>E,
\]

the factors in `S` already reconstruct at most one excess path and one word.
The reconstructed path must still pass the explicit first-crossing gate
`(16)--(17)`. The selected factors prove only

\[
\prod_{s\in S}Q_s
\mid
A_w-P\Delta.
\]

Every omitted prime power must still be checked. Word decoding,
first-crossing admissibility, and complete near-cycle certification are
separate gates.

## 6. Consequence for the remaining Box-2 language

`T-6806`, `T-6807`, `T-6810`, and the wrap theorems force every unbounded
acyclic obstruction family to be nonmechanical, wrapped, early-departing,
and supported on at least square-root many displaced odd positions.

`L-6809` gives the exact lossless factorwise target:

```text
complete denominator factorization
+ compatible local excess paths
+ exact first-crossing prefix barrier
+ one common 0 <= Delta < q/3
+ canonical positive range
    <=>
one exact ordinary first-crossing near-return.
```

A full negative proof may show that no complete tuple reconstructs a
first-crossing word and a common displacement in the one-third window. A
positive tuple is an exact physical near-return object, not a proper-factor
nomination.

## 7. Gap audit

- Factoring `D` and solving all local path equations remains difficult.
- A proper-factor or order-cover hit is not a near-cycle certificate.
- The first-crossing barrier must be checked after CRT reconstruction.
- The order window `(10)` is source-qualified through PR #34.
- The theorem is a lossless reduction, not a nonexistence theorem.
- The cycle level `Delta=0` is retained.
- No CST or Collatz proof is claimed.
