# A strict direct-R descent from a source-zero reference

**PROVED-IN-NOTE on the stated progression. Universal R remains OPEN.**
This rule transports arbitrary complete witnesses to a smaller ordinary
parameter. Its source witness becomes longer, so the decreasing quantity
is the parameter, not the source witness length.

Use the witness convention and accelerated odd map of
[DIRECT_R_WORDS.md](DIRECT_R_WORDS.md), and write

\[
R(m):\quad27m\in E\Longrightarrow9m\in E.
\]

Only the defining witness identity and direct integer algebra are needed
below. No conjectural closure, density statement, or global reduction is
assumed.

## SZD-001. The ordinary cell and the witness substitutions

For \(u\ge0\), put

\[
m=69984u+50063,\qquad p=65536u+46881.
\tag{1}
\]

Equivalently,

\[
m>0,\quad m\equiv15\pmod{32},\quad m\equiv1949\pmod{2187},
\qquad
\boxed{p=\frac{2048m-277}{2187}.}
\tag{2}
\]

Then \(p\) is positive odd, \(p\equiv33\pmod{64}\), and

\[
m-p=4448u+3182>0.
\tag{3}
\]

The following literal substitutions transport complete supplied witnesses.
The symbol \(\Vert\) denotes concatenation; the copied tail may be empty.

**Source, parent to child:**

\[
\boxed{(a)\Vert w
\longmapsto(1,2,1,2,3,1,3,a-2)\Vert w,\qquad a\ge5.}
\tag{4}
\]

**Target, child to parent:**

\[
\boxed{(2,1,1,1,1,2,2,1,1,1,c)\Vert v
\longmapsto(1,1,2,c-2)\Vert v,\qquad c\ge3.}
\tag{5}
\]

The first increases the odd length by seven and the total exponent by
eleven. The second decreases them by seven and eleven. Both have exact
inverse substitutions. Every supplied terminal exponent-2 loop is
preserved in the copied tail. Consequently

\[
\boxed{27m\in E\iff27p\in E,
\qquad9m\in E\iff9p\in E,
\qquad R(m)\iff R(p).}
\tag{6}
\]

The last equivalence is conditional: the construction provides a smaller
R instance, not a proof that every such child instance is true.

## SZD-002. Complete proof by ordinary affine prefixes

Define the fixed words

\[
\begin{aligned}
W&=(1,2,1,2,3,1,3,3),\\
V&=(2,1,1,1,1,2,2,1,1,1,3),\\
A&=(1,1,2,1),
\end{aligned}
\]

and the positive integers

\[
\begin{aligned}
t&=177147u+126722=\frac{81m+1}{32},\\
q&=1594323u+1140500=9t+2,\\
h&=v_2(t),\qquad g=v_2(q),\\
t_o&=t/2^h,\qquad q_o=q/2^g.
\end{aligned}
\tag{7}
\]

The four exact accelerated prefixes are

| Start | Exact exponent word | Positive odd endpoint |
|---|---|---|
| \(27m\) | \((5+h)\) | \(t_o\) |
| \(27p\) | \((1,2,1,2,3,1,3,3+h)\) | \(t_o\) |
| \(9m\) | \((1,1,2,1+g)\) | \(q_o\) |
| \(9p\) | \((2,1,1,1,1,2,2,1,1,1,3+g)\) | \(q_o\) |

The valuation corrections \(h,g\) are essential. The fixed words
\((5),W,A,V\) end at \(t,t,q,q\), which need not be odd; only the
adjusted words in this table are asserted to be accelerated prefixes.

### Exact identities

For a word \(w=(a_1,\ldots,a_r)\), let

\[
B(w)=\sum_i a_i,\qquad
C(w)=\sum_{i=0}^{r-1}3^{r-1-i}2^{a_1+\cdots+a_i}.
\]

Its rational forward affine function is

\[
F_w(x)=\frac{3^r x+C(w)}{2^{B(w)}}.
\tag{8}
\]

Direct addition gives

| Word | Length | \(B(w)\) | \(C(w)\) |
|---|---:|---:|---:|
| \((5)\) | 1 | 5 | 1 |
| \(W\) | 8 | 16 | 24485 |
| \(A\) | 4 | 5 | 73 |
| \(V\) | 11 | 16 | 351437 |

In particular \(351437=9\cdot24485+2^{17}\). Substitution of (2)
therefore gives the identities

\[
F_{(5)}(27m)=F_W(27p)=t,
\qquad F_A(9m)=F_V(9p)=9t+2=q.
\tag{9}
\]

Changing a word's final letter does not change its correction \(C(w)\).
Increasing the respective final letters by \(h,h,g,g\) in (9) thus
gives the displayed positive odd endpoints \(t_o,t_o,q_o,q_o\).

**Ordinary-prefix observation.** If \(x,y\) are positive odd integers,
all letters of \(w\) are positive, and \(F_w(x)=y\), the entire word
is an exact ordinary odd prefix. To prove it, write
\(2^{B(w)}y-C(w)=3^r x\). Modulo 3 this forces the last inverse
step \((2^{a_r}y-1)/3\) to be integral. Cancel that step and repeat
modulo 3. Each recovered integral inverse of a positive odd endpoint is
positive odd. Reversing the recurrences gives exactly the prescribed
valuations. This proves the observation and the entire four-path table
for every \(u\ge0\).

The checker separately verifies each affine coefficient division before
the last normalization. Every earlier state has positive even slope and
positive odd intercept. The final unnormalized endpoints have positive
integer coefficients as in (7).

### Why empty tails are valid

The normalized endpoints can equal 1, so a nonempty tail is not required.
No earlier state can equal 1. The respective states just before the final
step are \(27m\), \((8t-1)/3\), \(6t+1\), and \((8q-1)/3\), all
strictly above 1. Any earlier visit to 1 would force that later odd state
to remain 1. Thus every complete witness contains its full adjusted
prefix, and it may finish exactly at that prefix's endpoint.

At the common endpoint, replace only the prefix and copy the entire
remaining tail. This proves (4)--(5) and their inverses. The length
differences are \(8-1=11-4=7\); the total exponent differences are
\((16+h)-(5+h)=(16+g)-(5+g)=11\). Terminal padding is copied
unchanged. Membership is equivalent along finite ordinary prefixes, so
(6) follows. Formula (1) proves all positivity, residue, and descent
assertions in (2)--(3).

### The original first-letter-five half

When \(u=2j+1\), both \(t\) and \(q\) are odd and \(h=g=0\).
The cell specializes to

\[
m=139968j+120047,\qquad p=131072j+112417,
\]

with the fixed words \((5),W,A,V\). The even values of \(u\) supply
the additional half of the domain. For example \(u=0\) gives
\(h=1,g=2\), so its parent source first letter is 6.

## SZD-003. Two exact unbounded rank-two exponent subfamilies

The source word \((a,b)\) has value

\[
N=\frac{2^{a+b}-2^a-3}{9}.
\tag{10}
\]

For the following two families, \(N=27m\) is positive odd and the
displayed word is a complete first-hit witness:

| First letter | Parent family | Residual target after ordinary normalization |
|---|---|---|
| \(a=5\) | \(b=88+162j,\ m=(2^{b+5}-35)/243\) | \(2^{b+1}-1\) |
| \(a=6\) | \(b=38+162j,\ m=(2^{b+6}-67)/243\) | \(2^b-1\) |

Here \(j\ge0\). The residual membership equivalences follow directly
from the first-letter normal forms in DIRECT_R_WORDS.md. Within these
families, the new descent applies exactly on

\[
\boxed{\begin{aligned}
a=5:&\quad j\equiv1518\pmod{2187},
&&b\equiv246004\pmod{354294};\\
a=6:&\quad j\equiv1824\pmod{2187},
&&b\equiv295526\pmod{354294}.
\end{aligned}}
\tag{11}
\]

These are infinite subfamilies, not all exponent parameters.

### Elementary order and congruence proof

For \(d\ge1\),

\[
\operatorname{ord}_{3^d}(2)=2\cdot3^{d-1}.
\tag{12}
\]

Indeed, an exponent giving 1 modulo 3 is even, and
\(v_3(4^r-1)=1+v_3(r)\). The latter follows by binomial induction
at powers of three and then at a factor coprime to three. It proves
(12) without a distribution assumption.

Exact modular arithmetic gives
\(2^{93}\equiv35\pmod{243}\) and
\(2^{44}\equiv67\pmod{243}\). Thus (12) proves the parent
progressions in the table. Both numerators in (10) are positive, and the
inverse recurrences verify their complete two-letter words. The binary
condition \(m\equiv15\pmod{32}\) is automatic, since the power of
two vanishes modulo 32 and
\(-35\cdot243^{-1}\equiv-67\cdot243^{-1}\equiv15\pmod{32}\).

Put \(M=3^{12}=531441\). The additional condition
\(m\equiv1949\pmod{2187}\) is respectively

\[
2^{b+5}\equiv473642\pmod M,
\qquad
2^{b+6}\equiv473674\pmod M.
\tag{13}
\]

Repeated squaring verifies

\[
2^{246009}\equiv473642\pmod M,
\qquad
2^{295532}\equiv473674\pmod M.
\tag{14}
\]

By (12), the order is exactly \(354294\). Each congruence in (13)
therefore has exactly the exponent class displayed in (11). Since
\(162\cdot2187=354294\), converting back to \(j\) gives precisely
1518 and 1824 modulo 2187. This proves completeness of the stated
congruence classes, not just two successful numerical examples.

The corresponding child source witnesses are explicit: they are (4)
applied to \((5,b)\) or \((6,b)\). Each has nine odd steps, with
total exponent \(b+16\) or \(b+17\). The checker validates these
inherited source certificates at \(b=246004\) and \(b=295526\)
without searching either huge target orbit.

## SZD-004. How the source-zero reference selected the rule

The preceding positive ordinary proof is sufficient by itself. The
following finite calculation explains the construction.

For a source inverse word of length \(r\), total exponent \(B\),
and correction \(C\), prepend it to \(t=(2^b-1)/3\). Then

\[
N'=\frac{2^B t-C}{3^r},\qquad
N'/3=\frac{2^{b+B}-(2^B+3C)}{3^{r+2}}.
\tag{15}
\]

Suppose a finite exact rational reference word for
\(-(2^B+3C)/3^{r+2}\) reaches \(-1\), with length \(s\),
total exponent \(D\), and correction \(C'\). Comparing its affine
endpoint with \(k\) exponent-1 steps after the parent's Mersenne
endpoint forces

\[
s=r+2+k,\qquad D=B+k-1,\qquad
C'=3^k(2^B+3C)-2^{B+k-1}.
\tag{16}
\]

The child parameter's slope is
\(2^{B-5}/3^{r-1}\). The present pair has
\(r=8,B=16,C=24485,k=1\), slope \(2048/2187<1\), and

\[
-\frac{138991}{59049}\xrightarrow{V}-1,
\qquad
-\frac{138991}{19683}\xrightarrow{W}-\frac13.
\tag{17}
\]

Every displayed reference valuation is exact. The next numerator after
\(-1/3\) is zero. We do **not** assign an accelerated valuation to
that zero or treat it as an odd reference step. In the positive ordinary
construction, the supplied complete tail witness is retained instead.
That is the source-zero operation used by this rule.

The matching equations do not show that a contracting pair exists for
every input. Only the ordinary progression (1) and its exact subfamilies
(11) are claimed here. They do not provide a complete first-letter-five
or first-letter-six selector.

## Replay and evidence limits

From the repository root run

```sh
python3 research/witness-global-closure-20261121/check_source_zero_descent.py
python3 -O research/witness-global-closure-20261121/check_source_zero_descent.py
```

The checker verifies all affine coefficient divisions, the final
valuation normalizations, the finite rational references, the modular
order data, and complete-witness substitutions with copied tails. Small
ordinary fixtures test both directions with and without terminal padding.
Two constructed endpoint-one fixtures test empty tails. The two enormous
rank-two fixtures test source transport only; their target status is
explicitly unresolved.

The universal progression follows from the integer proof. Finite replay
is implementation evidence, not formal verification, universal R
coverage, or a target certificate for all members of either rank-two
family.
