# Independent review of the complete-ladder energy renewal

## Frozen source and verdict

Reviewed file:
`research/grh-certificate-closure-20261120/LADDER_RENEWAL.md`.

SHA-256:
`dbaff460c0a3f76f6cfa4947ba52d2511fb46ffedfac051baf3904c38402fa32`.

**VERIFIED for R1, R2, R5 and R6 as stated at this hash**, conditional only on the
explicit T-invariance of the label and the elementary FL1–FL3 identities
independently reviewed in `REVIEW_FIVE_LADDER.md`. No GRH assumption is
used. This is an independent mathematical reconstruction. The separate
rational checker written by the author is outside this review's execution
scope. I independently checked the three exact integer comparisons and
the rational coefficient in the subcritical proof; no source census or
additional trajectory test is needed for the argument below.

The source correctly credits PR163, head
`051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
`research/deep-reverse-closure-20261120/CLOSING_ATTEMPTS.md`, section D,
for the earlier r=1 renewal and its coefficient 64/441. The present result
extends the source domain to all ladder cylinders, both for the harmonic
weight 1/x and the subcritical weight x^(-21/25). It does not independently
re-audit PR163's subsequent analytic rigidity dependencies. The subcritical
claim appeared in the final reviewed revision; an earlier harmonic-only
draft is superseded by the present frozen source.

## 1. Exact transfer of the defect

Let f be a metric-valued invariant of the ordinary shortcut map T. For
positive odd ternary units put

\[
D(x)=d(f(5x),f(x))\ge0.
\]

Each x in the ladder union has a unique initial word consisting of r
valuation-two letters followed by one letter b at least four. Its actual
endpoint q is an odd ternary unit. FL1 supplies literal paths from x to q
and from 5x to 5q, and FL3 gives q at most x/7. T-invariance therefore
gives **D(x)=D(q)**. The equality does not rely on any assumption that x
or q converges, nor on an approximation to the trajectories.

The initial valuation run uniquely determines r, b and q for each x.
Thus the following inverse enumeration has no unexplained multiplicity.

## 2. The inverse progression and its mass

For fixed r at least one and odd ternary unit q, inverse sources are

\[
x_b=\frac{2^{2r+b}q-B_r}{3^{r+1}},\qquad
B_r=4^{r+1}-3^{r+1}>0.
\]

Reduction modulo 3^(r+1) gives the exact integrality condition
`2^(b-2)q=1 mod 3^(r+1)`. The order of two is
`P_r=2*3^r`, equal to the size of the unit group. There is consequently
one admissible progression b=b_0+kP_r, with k nonnegative and b_0 the
least admissible value at least four. The full integrality condition
implies each individual inverse division is legal, as checked in the
ladder review. Every resulting source is positive and odd. Deleting
sources divisible by three only reduces the positive sum.

The height estimate used in the note can be checked without an unstated
constant. Indeed,

\[
x_{b_0}-4(4/3)^r q
 =1+(4/3)^r\frac{(2^{b_0}-12)q-4}{3}\ge1,
\]

since b_0 at least four and q at least one. Also,

\[
x_{b_0+kP_r}
 =2^{kP_r}x_{b_0}
  +(2^{kP_r}-1)\frac{B_r}{3^{r+1}}
 \ge2^{kP_r}x_{b_0}.
\]

Therefore the whole inverse-source harmonic mass for fixed r,q is at
most

\[
\frac1q\frac{(3/4)^r}{4(1-2^{-P_r})}.
\]

Summing over r is legitimate for nonnegative terms. Since P_r at least
six,

\[
\sum_{r\ge1}\frac{(3/4)^r}{4(1-2^{-P_r})}
 \le\frac{1}{4(1-2^{-6})}\sum_{r\ge1}(3/4)^r
 =\frac{16}{21}<1.
\]

The constant is a valid conservative bound; optimality is not asserted.

## 3. Truncation and the finiteness equivalence

Write E(X) for the whole harmonic defect sum through X, H(X) for the
ladder portion, and R(X) for the complementary portion, all restricted
to odd ternary units. Each source x at most X has q at most X/7. Applying
the preceding inverse-source bound at each such q and using D(x)=D(q)
gives

\[
H(X)\le\frac{16}{21}E(X/7).
\]

Adding R(X) proves R1. Every finite-cutoff sum is finite, and E is
nondecreasing, so

\[
E(X)\le R(X)+\frac{16}{21}E(X)
\quad\Longrightarrow\quad
E(X)\le\frac{21}{5}R(X).
\]

If R(infinity) is finite, monotone passage to the limit gives the
quantitative bound in R2. The converse follows from R(X) at most E(X).
No infinite quantity has been subtracted, and no exchange of signed
series is involved.

## 4. Subcritical weight: the exceptional zero term matters

For s>0, use weights x^(-s) in the same sums. A direct reuse of the
earlier coarse height bound would not by itself establish the stated
subcritical constant. The new argument correctly removes q=1 first:

\[
D(1)=d(f(5),f(1))=0
\]

because the literal shortcut path is `5 -> 8 -> 4 -> 2 -> 1` and f is
invariant. All remaining odd ternary-unit endpoints satisfy q at least
five. Thus

\[
x_{b_0}
 =1+(4/3)^r\frac{2^{b_0}q-4}{3}
 \ge(4/3)^r q\frac{16q-4}{3q}
 \ge\frac{76}{15}(4/3)^r q.
\]

Every quantity is positive. Raising to power -s reverses this height
bound in the needed direction. The exact same geometric comparison and
source enumeration now give, for each contributing q,

\[
\sum_{r,b}x_b^{-s}
 \le q^{-s}\left(\frac{15}{76}\right)^s
       \sum_{r\ge1}\frac{(3/4)^{rs}}{1-2^{-sP_r}}
 \le q^{-s}C_s,
\]

where

\[
C_s=\left(\frac{15}{76}\right)^s
 \frac{(3/4)^s}{1-(3/4)^s}\frac1{1-64^{-s}}.
\]

Both geometric series converge for every s>0, which proves R5. This does
not assert C_s<1 for every s. At s=21/25, the two integer inequalities

\[
15^{21}50^{25}<76^{21}13^{25},\qquad
3^{21}500^{25}<4^{21}393^{25}
\]

are true, as independently evaluated using exact integer arithmetic. They
imply respectively `(15/76)^s<13/50` and `(3/4)^s<393/500`.
The third bound `64^(-s)<1/32` is exactly `2^126>2^125` after raising
to power 25. Since `t/(1-t)` is increasing for 0<t<1, all comparisons
have the correct direction. Therefore

\[
C_{21/25}
 <\frac{13}{50}\frac{393}{107}\frac{32}{31}
 =\frac{81744}{82925}<1.
\]

This proves the conservative rational coefficient in R6. Finite-cutoff
subtraction is again legal and yields

\[
E_{21/25}(X)\le\frac{82925}{1181}R_{21/25}(X).
\]

Monotone passage to the limit proves both the stated finiteness
equivalence and its quantitative bound. No claim about convergence of
arbitrary q, no decimal rounding, and no subtraction of infinite series
is used.

## 5. The remaining obligation

The covered union has relative density 1/24 among odd ternary units;
its complement is infinite (indeed of relative density 23/24). The
**complementary energy remains unbounded by the present argument**.
This does not mean that it has been proved infinite: its finiteness for
the relevant unknown invariant is precisely what remains to establish.

Positive source density alone gives no estimate for the label-dependent
harmonic or subcritical remainder. The renewal theorem proves that the covered portion
adds no independent finiteness obstruction once the complementary
moment is known. It does not establish that moment, universal forward-five
closure, or Collatz. The frozen source preserves these distinctions.
