# L-6807 — First-crossing paradoxes are small-displacement full-denominator near-cycles

**Claim ID:** `L-6807`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6803`; exact affine numerator expansion  
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

## 2. Exact near-cycle equation

The displacement identity from `L-6803` is

\[
\boxed{
A_w=D r_w+P\Delta_w.}
\tag{2}
\]

Equivalently,

\[
\boxed{
D\mid A_w-P\Delta_w,
\qquad
r_w=\frac{A_w-P\Delta_w}{D}.}
\tag{3}
\]

Thus a CST obstruction is a full-denominator certificate with one additional ordinary displacement parameter.

The cycle equation is exactly the special case

\[
\Delta_w=0.
\]

## 3. Universal displacement bound

The exact numerator expansion gives

\[
\frac{A_w}{Q}
=
\sum_{m=1}^{j}
 v_{m-1}\frac{2^{m-1}}{3^{q_m}}.
\tag{4}
\]

The final bit is even, and every earlier prefix is coefficient-supercritical. Hence every nonzero summand in `(4)` is at most `1/2`, giving

\[
\frac{A_w}{Q}\le\frac q2.
\tag{5}
\]

Since `Q<P`,

\[
\frac{A_w}{P}<\frac q2<\frac j2.
\tag{6}
\]

Equation `(2)` and `r_w>=1` imply

\[
P\Delta_w<A_w.
\]

Therefore every non-descending canonical first crossing satisfies

\[
\boxed{
0\le\Delta_w<\frac{A_w}{P}<\frac q2<\frac j2.}
\tag{7}
\]

The endpoint of a putative enormous paradoxical prefix is consequently only `O(j)` above its start:

\[
\boxed{T^j(r_w)=r_w+\Delta_w,
\qquad
0\le\Delta_w<j/2.}
\tag{8}
\]

## 4. Complete finite displacement family

For one fixed word `w`, every possible canonical non-descent lies in the finite set

\[
\boxed{
\Delta\in
\{0,1,\ldots,\lceil q/2\rceil-1\}}
\tag{9}
\]

and must pass

\[
\boxed{
D\mid A_w-P\Delta.}
\tag{10}
\]

Because `gcd(P,D)=1`, each prime-power divisor of `D` forces the same residue

\[
\Delta\equiv P^{-1}A_w
\pmod{p^a}.
\tag{11}
\]

The local congruences are not independent nominations: they must reconstruct one common small ordinary integer `\Delta` inside `(9)`.

## 5. Bridge to the cycle compiler

The positive-cycle funnel studies

\[
D\mid A_w
\]

and exact replay. `L-6807` shows that the finite-crossing lane differs only by a bounded shifted numerator:

\[
D\mid A_w-P\Delta,
\qquad
0\le\Delta<j/2.
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

This is a genuine unification of the finite-cycle and delayed-first-crossing blockers.

## 6. Least-counterexample specialization

For a least positive counterexample, `r_w` lies above the imported verified floor while `(8)` gives

\[
\frac{T^j(r_w)}{r_w}
=1+O\!\left(\frac{j}{r_w}\right).
\]

The prefix is therefore an exact near-return of a huge ordinary integer, not merely a coefficient near one.

A successful mixed-place theorem may exploit simultaneously:

- the complete dyadic replay depth `j`;
- the full odd denominator `D=2^j-3^q`;
- the small Archimedean displacement `Delta<j/2`;
- the verified lower height of `r_w`.

## 7. Gap audit

- The finite set `(9)` still grows with `j`; it is not a bounded-support theorem.
- Proper-factor divisibility does not imply the complete condition `(10)`.
- The small displacement does not itself contradict a huge starting value.
- `Delta=0` is a positive-cycle case; `Delta>0` is the genuine CST obstruction.
- No universal full-denominator exclusion is proved here.

## 8. Handoff

The strongest next finite arithmetic target is:

\[
\boxed{
2^j-3^q
\nmid
A_w-2^j\Delta
\quad
\text{for every }0\le\Delta<j/2
}
\]

under the least-counterexample admissibility constraints.

A proof eliminates the complete delayed-crossing word; one equality gives an exact near-return object for immediate physical replay.