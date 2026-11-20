# Two exact descents for families with long trailing ones

**Main claim W512-001 remains OPEN.** This note proves two descending
families. It does not claim that these families, or the currently known families,
cover every parameter.

Let

\[
\mathcal C(M):\quad128M+1\in E\Longrightarrow64M+1\in E.
\]

Here \(E\) has exactly the witness definition in [README.md](README.md).
All actual witnesses and trajectories in the theorem below are positive
integer trajectories. Rational negative values are used only as finite
algebraic reference points for proving the prescribed exponent words.

| Claim ID | Status | Scope |
|---|---|---|
| W512-070 | PROVED-IN-NOTE | The exact equivalence and strict parameter descent in (2), under the congruences in (1). |
| W512-071 | PROVED-IN-NOTE | The source and target witness transfers in Section 3, with the stated length and exponent changes. |
| W512-072 | PROVED-IN-NOTE | The second contraction in Section 4, with its exact witness transfers. |

## 1. The descending parameter

Suppose

\[
\boxed{
M>0,\qquad M\equiv-1\pmod{2048},\qquad M+1\equiv49\pmod{243}.
}
\tag{1}
\]

Define

\[
\boxed{M'=\frac{128M-69}{243}.}
\tag{2}
\]

Then \(M'\) is a positive odd integer, \(M'<M\), and

\[
\boxed{\mathcal C(M)\quad\Longleftrightarrow\quad\mathcal C(M').}
\tag{3}
\]

In particular, a proof of the strictly smaller instance \(\mathcal C(M')\)
proves \(\mathcal C(M)\). No unproved \(P\)- or \(Q\)-instance is needed
to establish the equivalence itself.

To check integrality, (1) gives
\(128(M+1)\equiv128\cdot49\equiv197\pmod{243}\), which is equivalent
to the numerator in (2) being divisible by 243. The numerator is odd, so
\(M'\) is odd. Positivity follows from \(M\geq2047\), and

\[
M-M'=\frac{115M+69}{243}>0.
\]

Write \(M=2048t-1\), with \(t\) any positive integer. The second
congruence in (1) is exactly

\[
t\equiv143\pmod{243}.
\]

No oddness assumption on \(t\) is required. Equivalently, the entire theorem
has the following ordinary positive-integer parametrization:

\[
\boxed{
M=497664j+292863,\qquad
M'=262144j+154265,\qquad j\geq0.
}
\tag{3a}
\]

Here \(t=243j+143\), and
\(M-M'=235520j+138598>0\). Formula (3a), together with the four positive
prefixes below, is sufficient for the proof; no negative trajectory is needed.

## 2. Exact common endpoints

Put

\[
X=128M+1,\quad Y=64M+1,\quad
X'=128M'+1,\quad Y'=64M'+1.
\]

The following are exact successive exponent words for every parameter in
(1):

| Starting value | Exact exponent word | Length | Sum | Endpoint |
|---|---|---:|---:|---|
| \(X\) | \([2,2,2,1,2,4]\) | 6 | 13 | \(S=5668704j+3335893\) |
| \(X'\) | \([2,2,2,1,1,2,2,1,2,4,5]\) | 11 | 24 | \(V=354294j+208493\) |
| \(Y\) | \([2,2,3,1,3,2]\) | 6 | 13 | \(2834352j+1667947\) |
| \(Y'\) | \([2,2,4,2,1,1,2,1,2,1,2]\) | 11 | 20 | \(2834352j+1667947\) |

Here \(S=16V+5=J^2(V)\), where \(J(z)=4z+1\), and \(V\) is a
positive odd integer. By W512-012, \(S\in E\Longleftrightarrow V\in E\).
Thus \(X\in E\Longleftrightarrow X'\in E\) and
\(Y\in E\Longleftrightarrow Y'\in E\). These two equivalences prove (3).

### Proof using only ordinary positive integers

Substitute (3a) into the four starting values. Their constant terms at
\(j=0\) are respectively

\[
37486465,\quad19745921,\quad18743233,\quad9872961.
\]

Directly applying the displayed finite exponent words to these constants
gives odd positive integers at every step and the constant endpoints in the
table. The coefficients of \(j\) in the four starting values are,
respectively,

\[
3^5\,2^{18},\quad2^{25},\quad3^5\,2^{17},\quad2^{24}.
\]

After a prefix of length \(i\) and cumulative exponent \(A_i\), a starting
coefficient \(c\) becomes \(3^ic/2^{A_i}\). Since the total exponents of
the four words are 13, 24, 13, and 20, all of these intermediate
coefficients are even positive integers, including at the final step.

Every lifted intermediate value is therefore its odd positive base value
plus an even nonnegative multiple of \(j\). In particular, each prescribed
exponent remains exact for every \(j\geq0\). The affine endpoint calculations
then give the table and prove (3). The companion replay checks these exact
positive affine identities and every prefix; they can also be checked simply
by the displayed divisions.

### How the rational reference calculation produces the same words

The following is an additional algebraic explanation of the template. The
positive proof above does not depend on interpreting rational values as
ordinary Collatz states.

The old reference values are \(-127\) and \(-63\). Their displayed words
of lengths 6 and 6 end at \(-11\) and \(-5\), respectively. Lifting by the
actual shifts \(2^{18}t\) and \(2^{17}t\) therefore gives

\[
T^6(X)=-11+3^6\,2^5t=23328t-11,
\]

\[
T^6(Y)=-5+3^6\,2^4t=11664t-5.
\tag{4}
\]

For the new parameter, write

\[
M'=-\frac{197}{243}+\frac{2^{18}}{243}t.
\]

The rational reference values of \(X'\) and \(Y'\) are
\(-24973/243\) and \(-12365/243\). The following two finite calculations
use the algebraic update \(z\mapsto(3z+1)/2^a\):

\[
-\frac{24973}{243}
\xrightarrow{[2,2,2,1,1,2,2,1,2,4,5]}-1,
\qquad (r,A)=(11,24),
\]

\[
-\frac{12365}{243}
\xrightarrow{[2,2,4,2,1]}-5,
\qquad (r,A)=(5,11).
\tag{5}
\]

Each intermediate reference value has odd numerator and odd denominator
after cancellation. The lifted values in (5) are

\[
T^{11}(X')=-1+3^6\,2t=1458t-1,
\]

\[
T^5(Y')=-5+2^{13}t.
\tag{6}
\]

The first value in (4) is exactly \(J^2\) of the first value in (6):

\[
16(1458t-1)+5=23328t-11.
\]

For the second value, the reference two-step pattern at \(-5\) is
\([-5\xrightarrow{1}-7\xrightarrow{2}-5]\). Whenever \(e\geq4\),

\[
-5+2^e c\xrightarrow{[1,2]}-5+9\,2^{e-3}c
\]

with the exponents exact for any positive integer \(c\). Apply this three
times, starting with \(e=13,c=t\), to obtain
\(-5+3^6\,2^4t\). This gives the last six exponents of the word for
\(Y'\).

### Why these are ordinary positive integer steps

The rational reference calculations are finite identities, not claims about
convergence of negative numbers. At each indicated prefix, the reference
endpoint has odd numerator and odd denominator, while the perturbation
coefficient multiplying \(t\) has even numerator and odd denominator.
Their sum therefore has 2-adic valuation zero.

The actual starting values \(X,Y,X',Y'\) are positive odd integers. By
induction, if the preceding actual value is integral, the prescribed division
of \(3n+1\) has valuation zero after division. It is consequently an odd
integer, and the prescribed exponent is exactly \(\nu_2(3n+1)\). Positivity
is preserved by \((3n+1)/2^a\). This proves the legality of every step for
every positive integer \(t\) satisfying the integrality congruence.

The companion exact-rational replay also checks the affine endpoint identities
and the odd-reference/even-perturbation property at every prefix.

## 3. W512-071: arbitrary-witness transfer

Suppose a witness supplied for \(X\) has length \(r\), final exponent
\(A\), and its exact exponent word. Strip its forced first six exponents,
obtaining a witness for \(S=J^2(V)\). Reverse \(J\) twice: this subtracts
4 from the first remaining exponent and preserves the length of the tail.
That first exponent is \(\nu_2(3V+1)+4\geq5\), so the new exponent is
positive. Prepend the eleven-exponent word for \(X'\). The result is a
witness for \(X'\), with

\[
\boxed{r'=r+5,\qquad A'=A+7.}
\tag{7}
\]

After the smaller assertion \(\mathcal C(M')\) supplies any witness for
\(Y'\), replace its forced eleven-exponent prefix by the six-exponent word
for \(Y\). If the child target witness has length \(s\) and final exponent
\(B\), this produces a witness for \(Y\) with

\[
\boxed{s'=s-5,\qquad B'=B-7.}
\tag{8}
\]

The source states \(S,V\) and the common target endpoint exceed 1. Every
supplied witness therefore contains the required prefixes before it can terminate;
no padding exception is needed. Strict positivity of every remaining
exponent follows because the tail is copied unchanged. The witness identity
follows from the concatenation formula W512-011.

The source witness becomes longer in (7). This does not invalidate the
descent: its well-founded parameter is \(M'<M\), not the witness length.

### The original fixed-word specialization

If additionally \(M\equiv-1\pmod{4096}\), then the parameter \(j\) in
(3a) is odd. Writing \(j=2i+1\) gives

\[
M=995328i+790527,\qquad M'=524288i+416409.
\]

Here the source's next exponents specialize to 5 and 1, so the old source
word extends to \([2,2,2,1,2,4,5]\), and the new source word extends to
\([2,2,2,1,1,2,2,1,2,4,5,1]\). These longer words reach the same endpoint
\(1062882i+844181\). The target words already in the table reach
\(5668704i+4502299\). This recovers the fixed-prefix proof on the smaller
cylinder while the \(J^2\) proof covers both parities of \(j\).

## 4. W512-072: a second contraction

The same method also gives the independent family

\[
\boxed{
M=1492992j+774143,\qquad
M'=1048576j+543705=\frac{512M-271}{729},\qquad j\geq0.
}
\tag{9}
\]

Equivalently, \(M>0\), \(M\equiv-1\pmod{2048}\), and
\(M+1\equiv675\pmod{729}\). Both parameters are positive odd integers and
\(M-M'=444416j+230438>0\).

With the same definitions of \(X,Y,X',Y'\), the exact prefix table is:

| Starting value | Exact exponent word | Length | Sum | Endpoint |
|---|---|---:|---:|---|
| \(X\) | \([2,2,2,1,2,4]\) | 6 | 13 | \(S=17006112j+8817973\) |
| \(X'\) | \([2,2,2,1,1,2,2,2,1,2,4,5]\) | 12 | 26 | \(V=1062882j+551123\) |
| \(Y\) | \([2,2,3,1,3,2]\) | 6 | 13 | \(8503056j+4408987\) |
| \(Y'\) | \([2,2,4,2,1,2,1,2,1,2,1,2]\) | 12 | 22 | \(8503056j+4408987\) |

Again \(S=16V+5=J^2(V)\) with \(V\) positive odd. Direct substitution at
every prefix gives an even integer coefficient of \(j\) and a positive odd
constant term, proving the exponent words for all \(j\geq0\). Thus
\(\mathcal C(M)\Longleftrightarrow\mathcal C(M')\).

The source witness conversion strips six exponents, reverses \(J\) twice,
and prepends the twelve-exponent new source word. It changes length and
final exponent by \(+6,+9\). The target conversion strips twelve exponents
and prepends the old six-exponent word, changing them by \(-6,-9\).

The finite reference calculation behind this template uses
\(M_0'=-29/27\). Its source reference \(-3685/27\) follows the displayed
twelve-step source word to \(-1\); its target reference \(-1829/27\)
follows \([2,2,4,2]\) to \(-5\). Four copies of the two-step word
\([1,2]\) produce the displayed twelve-step target word. As before, the
ordinary positive table is the primary proof.

## 5. Replay and remaining coverage

From the repository root, run:

```sh
python3 research/witness-closure-512-2026-11-20/verify_negative.py
python3 -O research/witness-closure-512-2026-11-20/verify_negative.py
```

The replay verifies the two ordinary positive affine tables, the first
rule's fixed-word specialization, and its rational-reference versions using
exact `Fraction` arithmetic, and checks their parity certificates. It also tests witness
reconstruction on a declared finite collection of instances, including even
and odd \(t\), and rejects unsupported inputs rather than treating them as
proved. Its emitted counts describe finite checks, not an exhaustive search.

The new progressions address some values with arbitrarily long strings of
trailing binary ones. Their additional congruences modulo 243 and 729 are
essential to these constructions. No proof that all other 3-adic classes admit a
descending template is supplied. The missing global coverage obligation,
and therefore W512-001, remain OPEN.
