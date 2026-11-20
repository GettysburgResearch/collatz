# Positive rational cycles in a prescribed real and arithmetic neighborhood

**PROPOSED, self-contained obstruction theorem.** This note does not construct
an integer counterexample or prove the Collatz conjecture. It studies the
shortcut map on rationals with odd denominator, with branch choice determined
by their parity in the 2-adic integers. It strengthens one particular local
countermodel interface: the real root can approach a supplied positive real
value while its binary and ternary residue classes are independently fixed.
The exact denominator remains part of the conclusion.

## 1. Statement

Write
\[
 E(x)=x/2,\qquad O(x)=(3x+1)/2.
\]
For a reduced rational with odd denominator, the shortcut map applies E when
its numerator is even and O when its numerator is odd. A positive rational
cycle is a finite periodic orbit of this deterministic map. Words below are
written in chronological order.

**AR1 (simultaneous density).** Fix a real number x_*>0, an error epsilon>0,
an integer K>=0, a residue z modulo 2^K, an integer M>=0, and, when M>0, a
unit residue t modulo 3^M. There are infinitely many positive noninteger
rational cycle roots r such that
\[
 |r-x_*|<\epsilon,\qquad
 r-z\in2^K\mathbb Z_2,\qquad
 r-t\in3^M\mathbb Z_3.                                  \tag{1}
\]
The final condition is vacuous for M=0. Every cycle state has the same
reduced denominator d>1, coprime to six, and is a ternary unit. The cycle
word may be chosen so that, with Q odd letters and N total shortcut
letters,
\[
 8Q-5N>0.                                               \tag{2}
\]
Consequently the inverse score W=sup(8q-5A), defined on odd rational unit
roots using legal accelerated inverse words, is infinite at every odd
phase of these cycles.

In topological language, these noninteger cycle roots are dense in
R_{>0} x Z_2 x Z_3^times under the diagonal embedding. The real coordinate
and the two residue coordinates are independent inputs to this statement.
It does not assert that an infinite sequence of different rational models
is the forward orbit of any one ordinary integer.

## 2. The explicit cyclic word

Let w be the length-K parity word of z, computed using any nonnegative
integer representative of z. Its affine composition is
\[
 F_w(x)=\frac{3^q x+C}{2^K}=Ax+B,
 \qquad A=3^q/2^K>0,\quad B=C/2^K\ge0.                  \tag{3}
\]
Here q is the number of odd letters and C is a nonnegative integer.
The empty word has K=q=C=0. The parity word is independent of the chosen
representative: at each step a difference divisible by 2^h becomes a
difference divisible by 2^{h-1}, since both branch slopes have odd numerator.

Append b odd letters and then a even letters, where a,b>=1. Since
\[
 O^b(y)=(3/2)^b(y+1)-1,
\]
the return map of w 1^b 0^a is
\[
 F(x)=RAx+R(B+1)-2^{-a},\qquad R=3^b/2^{a+b}.
\]
Its fixed point is
\[
 r_{a,b}=\frac{R(B+1)-2^{-a}}{1-RA}
       =\frac{C_{a,b}}{D_{a,b}},                         \tag{4}
\]
where
\[
 C_{a,b}=3^b(C+2^K)-2^{K+b},\qquad
 D_{a,b}=2^{K+a+b}-3^{q+b}.                              \tag{5}
\]
The numerator is positive for b>=1. The denominator is odd and prime to
three. Whenever RA<1, the root is positive.

For clarity, this is a genuine parity cycle, not a freely selected real
orbit. Each cyclic rotation of a word with at least one odd letter has
fixed-point denominator 2^N-3^Q, which is odd. All its phases therefore
belong to Z_2. At an even letter the identity 2y=x forces x to be even;
at an odd letter 2y=3x+1 forces x to be odd. Thus the chosen branches are
the actual parity branches at every phase. Positivity holds at all phases
because E and O preserve positive real numbers. One odd branch produces
a ternary unit, and both branches preserve ternary units thereafter, so
every phase is a unit modulo three.

The first K branches agree with w. A fixed parity prefix specifies exactly
one residue class modulo 2^K: the preceding parity induction gives
existence on every class, and backwards induction on the two branches
gives injectivity. Therefore r_{a,b}=z modulo 2^K.

## 3. Tuning the real coordinate while fixing the ternary coordinate

Put
\[
 R_* = \frac{x_*}{Ax_*+B+1}>0.
\]
Then R_*A<1. If a,b tend to infinity and R tends to R_*, equation (4)
gives r_{a,b}->x_*.

For M>0 and b>=M, reduction of (5) gives the particularly simple formula
\[
 r_{a,b}\equiv-2^{-a}\pmod{3^M}.                        \tag{6}
\]
The order of two modulo 3^M is P=2*3^{M-1}. Indeed, the elementary lifting
identity v_3(4^h-1)=1+v_3(h), proved by successive binomial expansion,
gives this order. Thus two generates the unit group modulo 3^M. Choose
a_0 modulo P with -2^{-a_0}=t modulo 3^M. For M=0 take P=1 and a_0=0.

Let gamma=log_2(3/2), which is irrational by unique prime factorization.
The multiples of gamma are dense modulo P, so there are b_i->infinity and
a_i in a_0+P Z with
\[
 b_i\gamma-a_i\longrightarrow\log_2 R_* .              \tag{7}
\]
One elementary proof of this rotation fact uses the pigeonhole principle
to find a nonzero multiple of gamma/P arbitrarily close to zero modulo
one; its successive multiples form an arbitrarily fine net. Removing a
finite initial set of multiples preserves density. The integers a_i in
(7) satisfy a_i/b_i->gamma>0, hence a_i->infinity.

Equations (4), (6), and (7) give all three agreements in (1), with positive
denominator and positive root for sufficiently large i.

The total odd and shortcut counts are Q=q+b and N=K+a+b. Therefore
\[
 \frac{8Q-5N}{b}\longrightarrow8-5\log_2 3>0,            \tag{8}
\]
where positivity follows from 3^5<2^8. Eventually the lap score is a
positive integer. Compressing the shortcut cycle at its odd phases gives
exact accelerated gaps whose sum is N. Repeating its inverse lap gains
8Q-5N each time, which proves W=+infinity at every odd phase. A word need
not be primitive for this argument.

## 4. Nonintegrality and explicit denominator growth

This step does not assume the absence of integer Collatz cycles.

Suppose r=u/d is one of the positive rational roots in a fixed bounded
interval (0,U), in reduced form. Its denominator d is coprime to six.
Every branch preserves this reduced denominator: if a numerator is even,
division by two preserves coprimality with d; if it is odd,
gcd(3u+d,d)=1 because gcd(3,d)=1, and division by two again preserves it.

At the phase after w, write y=F_w(r)=v/d in reduced form. The b successive
odd inputs imply
\[
 2^b\mid v+d.
\]
This follows directly by iterating O^h(y)+1=3^h(y+1)/2^h and using the
integrality of each numerator through h=b. Since v+d is a positive integer,
\[
 d\ge\frac{2^b}{y+1}
   >\frac{2^b}{AU+B+1}.                                \tag{9}
\]
As b tends to infinity, d tends to infinity. In particular d>1 for all
sufficiently large members of the sequence, and there are infinitely many
distinct roots. This proves all of AR1, without factoring D_{a,b} and
without any assertion about ordinary cycle exclusion.

There is also a useful denominator bound at a supplied ordinary integer.

**AR2 (cost of simultaneous approximation to one integer).** If n is an
integer, r=u/d is reduced with gcd(d,6)=1, r!=n, and
\[
 r-n\in2^K\mathbb Z_2\cap3^M\mathbb Z_3,
\]
then
\[
 d|r-n|\ge2^K3^M.                                     \tag{10}
\]
Indeed the nonzero integer u-nd is divisible by 2^K3^M. Thus any such
root with |r-n|<epsilon has
\[
 d>2^K3^M/\epsilon.                                   \tag{11}
\]
For every positive odd ordinary ternary unit n, AR1 supplies these
simultaneous approximants with W=+infinity and unbounded d. The bound
(11) is a global arithmetic cost, not an integer counterexample.

## 5. What this blocks, and what it leaves open

Precise real location plus any fixed binary and ternary observations does
not exclude positive noninteger rational cycles, even if one also asks
for exact branch legality and infinite inverse score. The failure persists
when the observations are chosen near a particular ordinary integer.

This does not block a proof that uses the exact denominator-one condition,
quantitative bounds relating growing precision to the full reduced
denominator, or consistency along one fixed ordinary orbit. In particular,
the same sequence cannot keep a bounded denominator while its errors
shrink and its precisions grow. The companion
[fixed-source calculation](FIXED_SOURCE_CLOSURE.md) attempts that stronger
bridge and states exactly which gain is still missing.

## 6. Source comparison and evidence boundary

The real density of rational periodic points is classical. Misiurewicz
and Rodrigues, *Real 3x+1*, Proceedings of the AMS 133 (2005), 1109–1118,
[Theorem 4.2](https://doi.org/10.1090/S0002-9939-04-07696-8), even bounds
the entire constructed cycle inside a real interval depending on the
target. Their paper's full text was inspected in the
[available author-content copy](https://www.researchgate.net/publication/346000553_Real_31),
including its parity interpretation and Theorem 4.2. The proof here is
self-contained and claims no novelty for the one-coordinate density fact.

The following repository sources were inspected at the exact heads shown.

| Source | Exact head | Relevant claim and comparison |
| --- | --- | --- |
| PR149, `research/forward-inverse-defect/RATIONAL_CYCLES.md`, Theorem 2 | `92c0129e794dde3ec55ceec470a12d51ba3f7e2f` | Simultaneous binary/ternary agreement, an arbitrary real lower floor for every cycle state, nonintegrality, bounded maximum gap after fixing the arithmetic observations, and infinite W. AR1 instead prescribes a small real neighborhood of the root; its maximum gap is unbounded. Neither package is asserted to dominate every feature of the other. |
| PR145, `research/unrestricted-cycle-denominator/PHYSICAL_PIECES.md` | `dd245a712f985909f541590e3f6c179b7ba011e4` | Long ordinary pieces approximate rational cycles with controlled congruences and a small proportion of incorrect joins. Those joins remain incorrect. AR1 uses exact rational cycles throughout. |
| PR145, `research/critical-orbit-mellin/RATIONAL_PHASE_TRACE.md` | `dd245a712f985909f541590e3f6c179b7ba011e4` | Fixed rational-phase trace classification and restrictions on empirical atoms. It does not identify the moving rational roots in AR1 with one ordinary orbit. |

The claimed addition is the explicit joint real/binary/ternary tuning with
positive critical score and the denominator bounds (9)–(11). No broad
priority claim is made. `check_adic_real_density.py` checks finite witnesses
using integer arithmetic and exact fractions. Density and arbitrary
precision are justified by the proof, not by the finite replay.

The replay passed eight independent-neighborhood cases, including five
simultaneous approximations to a supplied ordinary integer. It checked
4,628 shortcut edges and 2,910 accelerated edges, binary precision up to
nine, ternary precision up to three, positive lap scores, and the exact
denominator inequalities. It separately checked all 2,047 binary residue
classes through precision ten and all 2,186 ternary unit classes through
precision seven. Normal and `-OO` execution produced byte-identical
`adic-real-density-report.json` output. These bounds describe the finite
check, not the universal theorem's range.
