# L-6807 — First-crossing paradoxes are small-displacement full-denominator near-cycles

**Claim ID:** `L-6807`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Last updated:** 2026-07-31  
**Dependencies:** `L-6803`, `L-6812`; exact affine numerator expansion  
**Scope:** coefficient-first-crossing words whose canonical member does not descend

## 1. Setup

Let `w` be coefficient-first-crossing of length `j` and weight `q`:

\[
3^{q_m}\ge2^m
\quad(m<j),
\qquad
3^q<2^j.
\]

Put

\[
P=2^j,
\qquad
Q=3^q,
\qquad
D=P-Q>0,
\]

and write

\[
T_w(x)=\frac{Qx+A_w}{P}.
\]

Let `(r_w,s_w)` be the canonical pair from `L-6803` and put

\[
\Delta_w=s_w-r_w.
\]

Assume the canonical member is non-descending:

\[
\Delta_w\ge0.
\tag{1}
\]

## 2. Exact bilateral near-cycle equation

The displacement identity is

\[
\boxed{
A_w=D r_w+P\Delta_w.}
\tag{2}
\]

Since `s_w=r_w+Delta_w`, the equivalent endpoint form is

\[
\boxed{
A_w=D s_w+Q\Delta_w.}
\tag{3}
\]

Consequently

\[
\boxed{
D\mid A_w-P\Delta_w,
\qquad
r_w=\frac{A_w-P\Delta_w}{D},}
\tag{4}
\]

and

\[
\boxed{
D\mid A_w-Q\Delta_w,
\qquad
s_w=\frac{A_w-Q\Delta_w}{D}.}
\tag{5}
\]

The two congruences are equivalent because `P congruent Q (mod D)`, but the
integer quotients are different coordinates.  The source uses `(4)`; the
endpoint uses `(5)`.

The cycle equation is exactly the special case

\[
\Delta_w=0.
\]

## 3. Universal one-third displacement bound

Put

\[
\alpha={\log2\over\log3},
\qquad
D_m=q_m-\alpha m.
\]

The normalized affine remainder is

\[
\frac{A_w}{P}
=
\frac12
\sum_{m=1}^{j}
 v_{m-1}3^{D_j-D_m}.
\tag{6}
\]

The final bit is even.  Every nonzero summand therefore comes from an odd
step ending at a proper time `m<j`.  At such a time,

\[
D_m=D_{m-1}+1-\alpha\ge1-\alpha,
\]

whereas first crossing gives `D_j<0`.  Hence every nonzero summand in `(6)`
is strictly smaller than

\[
\frac12 3^{-(1-\alpha)}
=\frac13.
\]

There are exactly `q` odd steps, so

\[
\boxed{
0<\frac{A_w}{P}<\frac q3.}
\tag{7}
\]

Equation `(2)` and `r_w>=1` imply

\[
P\Delta_w<A_w.
\]

Therefore every non-descending canonical first crossing satisfies

\[
\boxed{
0\le\Delta_w
<\frac{A_w}{P}
<\frac q3
<\frac j3.}
\tag{8}
\]

The endpoint of a putative enormous paradoxical prefix is consequently only
`O(j)` above its start, with the sharper constant

\[
\boxed{
T^j(r_w)=r_w+\Delta_w,
\qquad
0\le\Delta_w<q/3.}
\tag{9}
\]

## 4. Complete finite displacement family

For one fixed word `w`, every possible canonical non-descent lies in the
finite set

\[
\boxed{
\Delta\in\mathbf Z,
\qquad
0\le\Delta<q/3,}
\tag{10}
\]

and must pass

\[
\boxed{
D\mid A_w-P\Delta.}
\tag{11}
\]

Equivalently,

\[
\boxed{
D\mid A_w-Q\Delta.}
\tag{12}
\]

Because `gcd(P,D)=gcd(Q,D)=1`, each complete prime-power divisor of `D`
forces the same residue for the one ordinary `Delta`.  The local congruences
are not independent nominations: they must reconstruct one common integer
inside `(10)`.

## 5. Bridge to the cycle compiler

The positive-cycle funnel studies

\[
D\mid A_w.
\]

The finite-crossing lane differs only by the one bounded shifted numerator

\[
D\mid A_w-P\Delta,
\qquad
0\le\Delta<q/3.
\]

Modulo a factor of `D`, this may be written

\[
A_w\equiv Q\Delta=3^q\Delta.
\]

Therefore every full-denominator method has a direct near-cycle analogue:

```text
prime-power excess paths:
    reconstruct one common Delta;

mixed-place height gate:
    prove A_w-P Delta is too small to be a nonzero multiple of D;

Christoffel / S-unit repairs:
    synthesize or exclude all small shifted residuals;

exact replay:
    verify r_w -> r_w+Delta over the complete parity word.
```

## 6. Least-counterexample specialization

For a least positive counterexample, `r_w` lies above the imported verified
floor while `(9)` gives

\[
\frac{T^j(r_w)}{r_w}
=1+O\!\left(\frac{j}{r_w}\right).
\]

The prefix is an exact near-return of a huge ordinary integer, not merely a
coefficient near one.

A successful mixed-place theorem may exploit simultaneously:

- the complete dyadic replay depth `j`;
- the full odd denominator `D=2^j-3^q`;
- the small Archimedean displacement `Delta<q/3`;
- the verified lower height of `r_w`.

## 7. Coordinate firewall

The identity

\[
A_w=nD+Q\Delta
\]

uses `n=s_w`, the endpoint.  If `n` denotes the source, the correct identity
is

\[
A_w=nD+P\Delta.
\]

The modular congruence is unchanged, but candidate reconstruction and
physical replay are not.  `L-6812` records this firewall in full.

## 8. Gap audit

- The finite set `(10)` still grows with `j`.
- Proper-factor divisibility does not imply the complete conditions
  `(11)--(12)`.
- The small displacement does not itself contradict a huge starting value.
- `Delta=0` is a positive-cycle case; `Delta>0` is the genuine CST
  obstruction.
- No universal full-denominator exclusion is proved here.

## 9. Handoff

The strongest finite arithmetic target is

\[
\boxed{
2^j-3^q
\nmid
A_w-2^j\Delta
\quad
\text{for every integer }0\le\Delta<q/3
}
\]

under the least-counterexample admissibility constraints.

A proof eliminates the complete delayed-crossing word; one equality gives an
exact near-return object for immediate physical replay.
