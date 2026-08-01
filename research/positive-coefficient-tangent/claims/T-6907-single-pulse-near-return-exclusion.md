# T-6907 — all-repetition exclusion of single-pulse positive near-returns

**Claim ID:** `T-6907`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issues:** #75; bridge to #52  
**Dependencies:** exact single-pulse affine reduction; the two-logarithm Matveev normalization used in PR #53 `T-8202`; elementary continued fractions; exact small-case checker `X-6901`  
**Scope:** one upward valuation pulse in an arbitrary repetition and rotation of either known ordinary negative accelerated Collatz cycle, with arbitrary nonnegative endpoint displacement

## Statement

Consider either primitive accelerated negative cycle

```text
P3  = (1,2),                 (A,k)=(3,2),
P11 = (1,1,1,2,1,1,4),      (A,k)=(11,7).
```

Repeat it an arbitrary number `r>=1` of times, rotate it arbitrarily, and increase the first valuation of the rotated word by an arbitrary integer `delta>=1`.

There do not exist positive integers `n` and `d>=0` such that the resulting accelerated word maps

\[
\boxed{n\longmapsto n+d,}
\tag{1}
\]

except for the trivial accelerated cycle

```text
(1,2) -> (2,2),
n=1,
d=0.
```

Thus, subject to primary-source reconstruction of the Matveev input, no nontrivial positive cycle **and no positive near-return of any displacement** is a one-pulse lift of any repetition or rotation of either known negative cycle.

This strictly strengthens `T-8202`, whose stated scope was `d=0`.

## Exact shifted numerator

Fix one rotated primitive cycle and let `z<0` be its negative odd fixed point. Put

\[
U=2^A,
\qquad
Q=3^k,
\qquad
K=kr.
\]

After `r` repetitions and one pulse of height `delta`, the denominator is

\[
\boxed{D=U^r2^\delta-Q^r.}
\tag{2}
\]

A positive accelerated near-return requires `D>0`.

Put

\[
g=-(3z+1)>0.
\]

The exact pulsed numerator is

\[
\boxed{
C=zD+g(2^\delta-1)3^{K-1}.}
\tag{3}
\]

Indeed, this is the single-pulse identity of `T-8202` with the sign of the negative state made explicit.

If `(1)` holds, then

\[
2^{Ar+\delta}(n+d)=3^K n+C,
\]

so

\[
Dn=C-d2^{Ar+\delta}.
\tag{4}
\]

Reducing `(4)` modulo `D`, using

\[
2^{Ar+\delta}\equiv3^K\pmod D,
\]

and removing the unit `3^(K-1)` gives the exact shifted full-denominator condition

\[
\boxed{
D\mid g(2^\delta-1)-3d.}
\tag{5}
\]

Write

\[
R=g(2^\delta-1)-3d.
\]

Equation `(3)--(4)` gives

\[
\boxed{
 n=z+3^{K-1}\frac RD.}
\tag{6}
\]

Since `n>0` and `z<0`, one must have `R>0`. Therefore every hit satisfies the displacement-independent size inequality

\[
\boxed{
0<D\le R<g(2^\delta-1).}
\tag{7}
\]

This is the key point: a positive displacement makes the reduced numerator **smaller**, so every near-return obeys the same logarithmic proximity mechanism as a cycle.

## Uniform logarithmic proximity

Define

\[
\eta=\log_2(Q/U)>0
\]

and

\[
\Lambda=(Ar+\delta)\log2-kr\log3
       =(\delta-r\eta)\log2>0.
\]

Since

\[
D=U^r2^\delta(1-e^{-\Lambda}),
\]

inequality `(7)` gives

\[
0<1-e^{-\Lambda}<\frac g{U^r}.
\tag{8}
\]

For the two primitive families one may use

```text
P3:  g <= 20,
P11: g <= 272.
```

For `P3, r>=3` and `P11, r>=1`, the right side of `(8)` is less than `1/2`. Hence

\[
\boxed{
0<\Lambda<\frac{2g_*}{U^r},}
\tag{9}
\]

with `g_*=20` and `272`, respectively.

The exact two-logarithm Matveev theorem used in `T-8202` then supplies the same valid cutoffs

```text
P3:  r < 50,000,000,000,
P11: r < 12,000,000,000.
```

The old margins are reduced only by `log(20/7)` or `log(272/91)` and remain overwhelmingly positive; `X-6901` reconstructs the inequalities with the new constants.

## Continued-fraction elimination

Dividing `(9)` by `r log 2` gives

\[
0<\frac\delta r-\eta
<\frac{2g_*}{r\log2\,U^r}.
\]

The exact Legendre thresholds are still

```text
P3:  r>=3,
P11: r>=1.
```

Thus, after reducing `delta/r=p/q`, the fraction `p/q` is an upper continued-fraction convergent of `eta`.

Let `q_+` be the next convergent denominator. For every positive multiple `(r,delta)=m(q,p)`,

\[
\Lambda
=m(p-q\eta)\log2
>\frac{\log2}{q+q_+}.
\]

On the other hand, `(9)` decreases with `m`. The exact checker verifies for every relevant upper convergent below the Matveev cutoff that

\[
\boxed{
U^q>4g_*(q+q_+).}
\tag{10}
\]

Using `log2>1/2`, `(10)` contradicts both bounds on `Lambda`. Hence no hit occurs in the analytic range.

Unlike the two-pulse theorem, no exceptional `1/5` family remains: with the new single-pulse constants, inequality `(10)` already holds at that first upper convergent.

## Complete small cases

Only the following repetitions lie below the Legendre range:

```text
P3:  r=1,2;
P11: none.
```

`X-6901` also replays `P11,r=1` as a redundant control.

For a fixed small packet, if

\[
R=mD,
\qquad m\ge1,
\]

then `(6)` gives

\[
n=z+m3^{K-1}.
\]

Positivity imposes

\[
m\ge m_{\min}
=\left\lfloor\frac{-z}{3^{K-1}}\right\rfloor+1.
\]

Combining `m_min D<=g(2^delta-1)` gives the finite pulse cap

\[
\boxed{
(m_{\min}U^r-g)2^\delta
\le m_{\min}Q^r-g.}
\tag{11}
\]

The coefficient on the left is positive in every small packet. Exact enumeration inside `(11)` leaves the unique hit

```text
P3, r=1, z=-5, delta=1,
m=2, d=0, n=1,
word (2,2).
```

Every candidate is physically replayed.

This completes the exclusion. ∎

## Relationship to the coefficient blocker

`L-6909` proves that every sufficiently late finite first-crossing failure is a positive near-return

\[
n\mapsto n+d,
\qquad 0<d<j/2,
\]

satisfying a shifted full-denominator equation.

`T-6907` therefore eliminates the entire subclass in which the first-crossing word is a one-pulse lift of any repetition or rotation of either known negative cycle.

This is a genuine exhaustive negative theorem for a strict infinite family, not a bounded search.

## Gap audit

- Exactly one pulse position only.
- Only the two known ordinary negative-cycle baselines.
- The exact primary Matveev formulation remains source-dependent.
- Multi-pulse, mixed-block, high-entropy, and arbitrary first-crossing words remain open.
- No full Collatz resolution is claimed.
