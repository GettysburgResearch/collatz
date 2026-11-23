# Independent review of the rational shadow obstruction

Reviewed [UNIVERSAL_SOURCE.md](UNIVERSAL_SOURCE.md) and the exact certificate in
[RationalShadowTest.lean](lean/RationalShadowTest.lean), with an independent
Python Fraction replay of every displayed source gap and target entry
state. The review concerns the arithmetic and the scope of the proposed
rational-shadow implication; the packet's fresh Lean build separately
records kernel acceptance.

**Result: the rational counterexample and its infinite prefix-coefficient
claims are arithmetically correct.** It is not a positive-integer
counterexample, and supplies no complete positive integer source lift.

## Source: actual gaps, including the crossing through zero

The common denominator is \(D=2187=3^7\), and
\[
x=-6005/2187,\qquad y=8x+19=-6487/2187.
\]
The source numerator sequence is
\[
-6005,\ -3957,\ -2421,\ -1269,\ -405,\ 243,\ 729,\ 2187,
\]
with accelerated gaps
\[
(2,2,2,2,2,2,1).
\]
For each consecutive pair \(H,H'\), the exact identity is
\(3H+D=2^aH'\). Both numerators and \(D\) are odd, so
\[
v_2(3(H/D)+1)=a.
\]
Thus these are the actual rational two-adic valuations, not just lower
bounds on divisibility.

In reduced terms the orbit is
\[
-\frac{6005}{2187},\
-\frac{1319}{729},\
-\frac{269}{243},\
-\frac{47}{81},\
-\frac5{27},\
\frac19,\
\frac13,\
1.
\]
It crosses from \(-5/27\) to \(1/9\) at the fifth accelerated step,
reaches \(1\) at the seventh, and thereafter has gap two forever.
The initial word has ordinary clock thirteen and seven odd steps.

For the first six nonempty accelerated prefixes, the leading coefficient
is \((3/4)^j<1\). At the seventh and every subsequent accelerated prefix,
it is
\[
\frac{3^{7+k}}{2^{13+2k}}
=\frac{2187}{8192}\left(\frac34\right)^k<1
\qquad(k\ge0).
\]
The bounded-four condition is a bound on each individual gap; the listed
gaps satisfy it. There is no assumed upper bound on the cumulative
inverse coefficient \(Q_j=2^{A_j}/3^j\).

## Target: actual states and every positive ordinary clock

At ordinary shortcut clocks zero through twelve the target numerators
are
\[
\begin{split}
&-6487,-8637,-11862,-5931,-7803,-10611,-14823,\\
&-21141,-30618,-15309,-21870,-10935,-15309.
\end{split}
\]
Reduction by an odd common denominator does not change parity. Direct
application of the even and odd shortcut rules therefore verifies this
entire sequence.

The target reaches \(-14\) at clock eight, \(-7\) at clock nine, and then
follows the ordinary negative cycle
\[
-7\longmapsto-10\longmapsto-5\longmapsto-7.
\]
Its odd counts at clocks one through twelve are
\[
1,2,2,3,4,5,6,7,7,8,8,9.
\]
The coefficients at clocks one through eight are
\[
\frac32,\ \frac94,\ \frac98,\ \frac{27}{16},\
\frac{81}{32},\ \frac{243}{64},\
\frac{729}{128},\ \frac{2187}{256}.
\]
Their minimum is \(9/8\). At clock \(9+3k+r\), with \(0\le r<3\), the
coefficient is
\[
\frac{2187}{512}\left(\frac98\right)^k
\begin{cases}
1,&r=0,\\
3/2,&r=1,\\
3/4,&r=2.
\end{cases}
\]
This is at least \(6561/2048>9/8\). Hence the global minimum at every
positive ordinary clock is exactly \(9/8\), attained at clock three.
Every nonempty ordinary target prefix has coefficient strictly greater
than one.

## What is and is not refuted

The certificate refutes a proposed universal implication from a complete
rational source word with bounded gaps and strict contraction of all
source prefixes to the existence of a contractive prefix for its affine
target \(8x+19\). The source and target must be interpreted in the
rationals with odd denominator, using their actual rational parity.

Both starting values here are negative and nonintegral. Their completion
and their infinite coefficient inequalities cannot be substituted for a
complete source certificate on positive ordinary integers. A finite
binary pin, or its positive integer realization, also does not preserve
the whole infinite rational trace automatically.

This does not refute PR185's existing repeated-block dispatcher. That
compiler retains an actual positive integer source trace, the full binary
pin, and a paid contractive target prefix. Its contracting repeated
source block has positive rational fixed point
\(C/(2^L-3^s)\). The present negative source is a preperiod entering one,
not that fixed point, and its target has no supplied contractive prefix.

The Lean module's finite numerator certificates, source coefficient
family, target count induction, and target coefficient inequality match
the calculations above. They introduce no positive-integer Collatz
counterexample or universal convergence premise.

## Other written calculations in the source note

The copied-word formula
\[
z_j=64^jz+
\frac{(64^j-1)(3C+2^A)}{3^{r+1}}
\]
and its exact integrality condition \(3^{r-1}\mid j\) are correct for
\(r\ge1,j>0\). The factor \(3C+2^A\) is a ternary unit, and
\(v_3(64^j-1)=2+v_3(j)\). Endpoint congruence modulo \(3^r\) propagates
integrality through the whole inverse word. Monotonicity of the inverse
branches preserves positivity; oddness of each target makes every
displayed halving gap exact. The possible loss of ternary-unit status at
the oldest source is correctly distinguished, with \(3^r\mid j\) a
sufficient stronger condition.

The finite obstacle estimate \(V_r\le2^r\) follows by induction from the
unit obstacle and the row-sum bound two. Its consequence
\(n/3^r\le\eta^{-1}(2/3)^r\) on \(V_r(n)\ge\eta n\) has the correct
direction. The note does not infer an unproved weighted sibling transfer
from local carry repairability.

No correction remains outstanding in the reviewed written argument.
The source-prefix clock qualification in the opening statement was
clarified during review: those prefixes are accelerated odd prefixes,
whereas the target claim concerns every ordinary shortcut prefix.
