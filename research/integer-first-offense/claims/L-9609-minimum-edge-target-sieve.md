# L-9609 — A cycle minimum reduces an arbitrary equal-summary grammar to a finite target set

**Claim ID:** `L-9609`
**Status:** `PROPOSED`
**Agent:** `gpt56-pro-04`
**Issue:** #46
**Date:** 2026-07-26
**Dependencies:** elementary affine-block arithmetic
**Scope:** finite alphabets of positive contracting affine blocks with one common multiplier and divisor

## 1. Statement

Fix integers

\[
0<P<Q,
\qquad D=Q-P>0,
\]

and a finite alphabet of nonnegative integer constants

\[
\mathcal E=\{E_1,\ldots,E_s\}.
\]

The block labeled `i` is

\[
Qy'=Py+E_i.
\tag{1}
\]

Suppose a finite word in this alphabet has a positive integral cycle

\[
y_0,y_1,\ldots,y_R=y_0,
\qquad y_t\in\mathbf Z_{>0}.
\tag{2}
\]

Let

\[
m=\min_{0\le t<R}y_t
\]

and rotate the word so that `y_0=m`. Then the first selected constant belongs to the exact finite target set

\[
\boxed{
\mathcal T(E_{\max})=
\left\{
Dm+Qk:
 m\ge1,\ k\ge0,\ Dm+Qk\le E_{\max}
\right\},}
\tag{3}
\]

where

\[
E_{\max}=\max_iE_i.
\]

Equivalently, for some integers `m>=1` and `k>=0`,

\[
\boxed{E_{i_0}=Dm+Qk,}
\qquad
\boxed{y_1=m+k.}
\tag{4}
\]

Consequently, if

\[
\mathcal E\cap\mathcal T(E_{\max})=\varnothing,
\tag{5}
\]

then no positive integral cycle exists, at any repetition length or ordering of the alphabet.

## 2. Divisibility sharpening

Assume in addition that an integer `g>=2` satisfies

\[
g\mid P,
\qquad
\gcd(g,Q)=1,
\qquad
E_i\equiv0\pmod g
\quad(1\le i\le s).
\tag{6}
\]

Then every target in `(4)` obeys

\[
\boxed{m+k\equiv0\pmod g.}
\tag{7}
\]

In particular,

\[
\boxed{E_{i_0}\ge gD.}
\tag{8}
\]

Hence the one-line height gate

\[
\boxed{E_{\max}<gD}
\tag{9}
\]

excludes every positive integral cycle.

More generally, only the finite set

\[
\boxed{
\mathcal T_g(E_{\max})=
\left\{
Dm+Qk:
 m\ge1,\ k\ge0,\
 m+k\equiv0\pmod g,\
 Dm+Qk\le E_{\max}
\right\}}
\tag{10}
\]

needs to be compared with the block alphabet.

## 3. Proof

Rotate a proposed cycle so that `y_0=m` is a minimum. The first edge gives

\[
Qy_1=Pm+E_{i_0}.
\]

Since `y_1>=m`, write

\[
y_1=m+k,
\qquad k\in\mathbf Z_{\ge0}.
\]

Then

\[
E_{i_0}
=Q(m+k)-Pm
=(Q-P)m+Qk
=Dm+Qk.
\]

This proves `(3)` and `(4)`. Finiteness follows from `D,Q>0` and the upper bound `E_(i_0)<=E_max`. If the alphabet misses the target set, the required first edge cannot exist, proving `(5)`.

Under `(6)`, reduce `(4)` modulo `g`. Because `D=Q-P` and `g|P`,

\[
0\equiv E_{i_0}
\equiv Q(m+k)\pmod g.
\]

The invertibility of `Q modulo g` gives `(7)`. Since `m>=1`, `k>=0`, and their sum is a positive multiple of `g`, one has `m+k>=g`. Finally,

\[
Dm+Qk
=D(m+k)+Pk
\ge D(m+k)
\ge gD,
\]

which proves `(8)` and `(9)`. Formula `(10)` is the exact remaining target set. ∎

## 4. Strength

The theorem removes the whole repetition axis before any word enumeration:

```text
arbitrary word length
+ arbitrary ordering
+ arbitrary repeated or nonperiodic use of the finite block alphabet
    -> one finite set of first-edge integer targets.
```

The reduction is full-denominator and Archimedean simultaneously. It does not test selected factors of `Q^R-P^R`; it uses the exact integer state at a cycle minimum.

## 5. Relationship to `L-9608`

`L-9608` proves zero carry when the complete constant alphabet has width below `Q`. `L-9609` is independent and complementary:

- no narrowness hypothesis is needed;
- the alphabet may span many `Q`-cells;
- a congruence shared by all constants can make the target set empty;
- the result is a necessary finite target test rather than automatic statewise collapse.

## 6. Gap audit

- A target hit is necessary, not sufficient; later edges and physical replay still matter.
- The theorem excludes cycles, not aperiodic divergent paths.
- Positivity of the cycle states is used in `m>=1`.
- Common `P,Q` are load-bearing; scale-varying summaries require a different minimum-edge calculation.
- The congruence sharpening requires `g|P`, `gcd(g,Q)=1`, and divisibility of every alphabet constant.

## 7. Suggested use

For a fixed-weight Collatz block alphabet:

1. center at a known fixed point if this makes all constants share a useful factor;
2. compute `D=Q-P` and the exact `E_max`;
3. apply `(9)` if possible;
4. otherwise enumerate the finite target set `(10)` symbolically and separate it from the block constants by one exact congruence.
