# Exact ordinary five-ray returns and the limits of a descent guard

**Status: proved elementary statements and an explicitly partial ordinary guard.**
All numbers in FR-004--FR-007 are positive ordinary integers, and all paths use
the shortcut map \(T(n)=n/2\) for even \(n\), \((3n+1)/2\) for odd \(n\).
Write \(s_H(n)\) for the number of odd inputs among its first \(H\) steps and
\(f(n)\) for its unrestricted merger component.

A *synchronous five-ray return* from \(t\) to \(u\) is
\[
 T^H(t)=u,\qquad T^H(5t+1)=5u+1,
 \qquad H\ge1.                                             \tag{1}
\]
It is *balanced* if the two odd counts also agree. These are **physical shortcut
words**, including their even inputs. They are not odd-only inverse blocks.
Every return transports the entire ordinary merger question:
\[
 f(t)=f(5t+1)\quad\Longleftrightarrow\quad f(u)=f(5u+1).     \tag{2}
\]
No upper bound on the eventual meeting clocks is needed for (2).

## FR-004: an all-time ternary obstruction to backward return branches

Every nontrivial synchronous return (1), balanced or not, satisfies
\[
                              u\equiv2\pmod3.              \tag{3}
\]
This is independent of the size of \(H\).

An odd shortcut step ends at a ternary unit, and every later shortcut step stays
at a ternary unit. Thus a positive path ending at a multiple of three must have
consisted entirely of halvings.

If \(3\mid u\), the lower path in (1) has only halvings, so \(t=2^H u\).
Its upper starting value \(5t+1\) is odd. At least one odd step on that arm and
the nonnegative affine offset imply
\[
 T^H(5t+1)\ge\frac{3(5\cdot2^H u+1)}{2^H}>5u+1,
\]
a contradiction. If \(u\equiv1\pmod3\), the upper endpoint \(5u+1\) is divisible
by three. That arm consists only of halvings, whence
\[
 t=2^H u+\frac{2^H-1}{5},\qquad
 T^H(t)\ge t/2^H=u+\frac{1-2^{-H}}5>u,
\]
also a contradiction. This proves (3).

There is a second useful constraint. Suppose two fixed parity words, at
possibly different clocks \(i,j\), give a return identity on **two distinct
parameters**. If their odd counts are \(p,q\), the slopes in
\(T^j(5t+1)=5T^i(t)+1\) must agree:
\[
                          5\cdot3^q/2^j=5\cdot3^p/2^i.
\]
Unique factorization gives \(i=j\) and \(p=q\). Therefore every nontrivial
uniform affine paired-return certificate is balanced and obeys (3).

Consequently, backward branching based on such certificates cannot even begin
at a parameter \(u\equiv0\) or \(1\pmod3\). Allowing an adaptive choice among
uniform certificates of unbounded lengths does not remove this target
obstruction. It **does not** prevent a forward guard from landing in the class
\(u\equiv2\pmod3\), and it does not refute arbitrary adaptive forward coverage.
Showing that every hypothetical permanent failure can be transported into that
target class remains a separate universal implication.

The equal-clock qualification is essential for a pointwise return. The ordinary
pair \((19,96)\) reaches \((1,6)\) at clocks \((14,4)\). Its target violates (3),
and it is not a uniform affine return identity. The checker verifies both paths.

## FR-005: the complete balanced returns through six steps

For every integer \(v\ge0\), the following identities hold:

| Starting parameter \(t\) | Returned parameter \(u\) | Clock | Lower parity word | Upper parity word | Odd counts |
|---|---:|---:|---|---|---:|
| \(64v+11\) | \(27v+5\) | 6 | `110100` | `000111` | 3, 3 |
| \(64v+35\) | \(9v+5\) | 6 | `110000` | `000011` | 2, 2 |

In both rows the upper endpoint is exactly \(5u+1\), and \(0<u<t\).
The six fixed low bits determine both parity words; their endpoint slopes on
\(v\) are respectively \((27,135)\) and \((9,45)\), and the constant endpoints
are \((5,26)\). This proves the identities for every positive lift.

These are the **only** positive parameters with a balanced return at a clock
from 1 through 6: at clock 6 their classes are exactly \(11,35\pmod{64}\), and
there are no earlier balanced-return classes. This last, finite classification
is certified by all \(2+4+\cdots+64=126\) binary cells. For each cell the two odd
counts and endpoint affine maps are computed exactly; if the counts agree,
the difference of the upper endpoint and five times the lower endpoint is
constant on every lift. No claim about larger clocks follows from this
classification.

The two inverse branches have target domains \(u\equiv5\pmod{27}\) and
\(u\equiv5\pmod9\), respectively:
\[
             t=(64u-23)/27,\qquad t=(64u-5)/9.              \tag{4}
\]
They do not give a branch at every target congruent to 2 modulo three.

## FR-006: an expanding first return with no earlier merger

For every integer \(v\ge0\), set
\[
                 t=512v+287,\qquad u=729v+410.
\]
The first synchronous five-ray return is at clock 9, with six odd inputs on
each arm:
\[
                T^9(t)=u>t,\qquad T^9(5t+1)=5u+1.          \tag{5}
\]
The words are `111110100` and `001110111`. Moreover, the two original arms
have **no meeting at any independent clocks** \(0\le i,j\le9\).
Thus a rule that waits for an early merger or the first synchronous return and
then presumes descent fails on this entire ordinary progression.

Here is a complete affine certificate. Each entry is a coefficient and an
intercept on the parameter \(v\); hence \((A,B)\) denotes \(Av+B\).

| Clock | Lower arm | Upper arm |
|---:|---:|---:|
| 0 | (512, 287) | (2560, 1436) |
| 1 | (768, 431) | (1280, 718) |
| 2 | (1152, 647) | (640, 359) |
| 3 | (1728, 971) | (960, 539) |
| 4 | (2592, 1457) | (1440, 809) |
| 5 | (3888, 2186) | (2160, 1214) |
| 6 | (1944, 1093) | (1080, 607) |
| 7 | (2916, 1640) | (1620, 911) |
| 8 | (1458, 820) | (2430, 1367) |
| 9 | (729, 410) | (3645, 2051) |

Before the last step every coefficient is even, so the intercepts determine the
displayed parity words uniformly on all integer \(v\). At clocks 1 through 8,
the upper affine function minus five times the lower minus 1 has **both**
coefficient and intercept strictly negative. At clock 9 it is identically zero.
This proves the first-return assertion, without needing an odd-count restriction
on earlier possible returns.

For the independent-clock assertion, all 20 coefficients in the table are
distinct. Sorting these 20 coefficients into increasing order sorts their
intercepts into strictly increasing order as well. Therefore the difference
between any lower and upper affine function has coefficient and intercept of
the same strict sign. It cannot vanish for \(v\ge0\). Equivalently, the checker
verifies these signs for all \(10\cdot10=100\) cross-arm equations. This is an
exact finite certificate for **all** ordinary lifts, not a sample of them.

The expansion also has a useful reverse direction. If \(u\equiv410\pmod{729}\),
then
\[
              t=(512u-697)/729\quad\text{is positive and below }u,
\]
and (2) reduces the question at \(u\) to the smaller question at \(t\).

## FR-007: a total partial guard, with a strict decrease on every accepted step

The executable guard in [`check_paired_returns.py`](check_paired_returns.py)
uses the following three rules:

| Input condition | Smaller parameter | Certificate direction |
|---|---:|---|
| \(n=64v+11\) | \(27v+5\) | Forward, 6 steps |
| \(n=64v+35\) | \(9v+5\) | Forward, 6 steps |
| \(n=729v+410\) | \(512v+287\) | Backward through (5), 9 steps |

Here \(v\ge0\) is automatic for positive inputs in the indicated residue class.
The decreases are \(37v+6\), \(55v+30\), and \(217v+123\), respectively.
Every accepted step preserves the answer to the all-time merger question by
actual finite ordinary paths. The union of the three starting domains has exact
natural density
\[
 \frac1{32}+\frac1{729}-\frac1{32\cdot729}
                        =\frac{95}{2916}.                 \tag{6}
\]
This follows from the Chinese remainder theorem, or from the exact 46,656-cell
period checked by the script. It concerns inputs permitting **one** certified
reduction, not the density of successful global mergers.

The guard first checks independent-clock meetings within a supplied finite
budget, then applies an available strict reduction, and repeats. Every reduction
lowers a positive integer, so this is a terminating ordinary algorithm. Its
possible outcomes are `MERGER_CERTIFIED`, `REDUCED_UNRESOLVED`, and `UNRESOLVED`.
The latter two are not failures of the Collatz conjecture. For example,

```
python -B research/focused-forward-20261120/five-ray/check_paired_returns.py --start 410 --clock 9
```

reduces 410 to 287 and then reports the question unresolved at that budget.
By FR-006, this unresolved outcome is expected. The same guard can report
`UNRESOLVED` at parameter 2 with budget 8 and certify it with budget 9.

A sufficient missing universal statement would be: every unmerged ordinary
question has an actual certified smaller question, allowing additional rules
if needed. Strong induction, with the merger at parameter 1, would then prove
the universal five-ray condition and hence Collatz. The present three-rule
guard does not establish that statement. Neither adaptive stopping of the
forward pair nor universal backward coverage is proved here.

## FR-008: what the prime-to-three restricted hypothesis actually supplies

This section is **conditional**. Assume
\[
 3\nmid t\quad\Longrightarrow\quad f(5t+1)=f(t)
 \qquad(t\in\mathbb N_{>0}).                               \tag{U}
\]
For every odd ternary unit \(x\), every \(i\ge0\), and every \(j\ge1\), it implies
\[
                       f(3^i5^j x)=f(x).                  \tag{7}
\]
Indeed put \(t=4^a x\), \(a\ge1\), in (U). Repeated use of
\(T^2(4z+1)=3z+1\) sends the upper arm to \(5\cdot3^a x+1\).
This value belongs to the component of the odd integer \(5\cdot3^{a-1}x\).
Since \(f(4^a x)=f(x)\), this proves the case \(j=1\), \(i=a-1\).
Replacing \(x\) by \(5^{j-1}x\) and iterating the \(i=0\) case proves (7).

Define \(F(n)=f(5n)\). Writing \(n=2^v3^i x\), with \(x\) an odd ternary unit,
equation (7) gives \(F(n)=f(x)\). Consequently
\[
 F(2n)=F(3n)=F(5n)=F(n),                                   \tag{8}
\]
and \(F(n)=f(n)\) whenever \(3\nmid n\), or whenever \(5\mid n\).
The last assertion uses \(f(5n)=F(n)=F(5n)\); it must not be extended to all
nonunits without proof.

For \(H(y)=F(y+1)\), the following identities are established:
\[
 H(4h)=H(3h)\quad(h\not\equiv2\pmod3),\qquad
 H(16h)=H(15h)\quad(h\ge1).                                \tag{9}
\]
For the first, \(4h+1\) and \(3h+1\) are both ternary units under the stated
restriction, so \(T^2(4h+1)=3h+1\) transfers to \(F\).
For the second, start at the odd multiple of five \(5(16h+1)\), where \(f=F\).
The identity
\(3\cdot5(16h+1)+1=16(15h+1)\), whose right side is a ternary unit,
and (8) give the result. The tempting middle relation
\(H(10h)=H(9h)\) would use \(f(3(10h+1))\), in a domain not covered by the
known equality \(f=F\).

There is an elementary obstruction to deriving that missing relation solely
from the two multiplicative identities in (9). The ordinary integer function
\[
                  W(y)=v_2(y)+2v_3(y)+2v_5(y)
\]
satisfies \(W(4h)=W(3h)\) and \(W(16h)=W(15h)\) for **all** positive \(h\),
but
\[
                  W(10h)=W(9h)-1,\qquad W(2h)=W(h)+1.
\]
This is a countermodel to a **scaling-only inference**. It is not asserted to
arise from any Collatz component function, and it does not satisfy or replace
all the additional shifted constraints imposed by (8). Thus it neither
disproves (U) nor disproves the possibility that (U) is sufficient for Collatz.

## Evidence boundary

The proof of FR-004 is all-time elementary arithmetic. FR-005 and FR-006 use the
explicit finite words and an exhaustive small affine certificate. FR-007 uses
only these identities and strict ordinary descent on accepted steps. FR-008
has the unproved hypothesis (U), which is displayed throughout its use.

The main checker verifies every six-bit return cell, the complete affine table
and all 100 independent-clock comparisons, the target obstruction on a finite
replay range as a regression, all three guarded rules, and exact residue-domain
counts. It rejects optimized Python execution, which would disable assertions.
Finite replay is not substituted for the all-time proof of the target gate.

`search_paired_returns.cpp` and `paired_return_cones_24.tsv` are separate,
bounded exploratory artifacts. They enumerate uniform balanced returns through
24 bits; the table saves selected finite witnesses with ancestor-redundant
ternary cones removed. The saved cones do not cover all targets
\(u\equiv2\pmod3\); their total ternary measure is \(11842/59049\). This is the
union measure of the saved witnesses, not an assertion that the table lists all
possible return branches. It does not prove that any ordinary question lacks a
longer return. The growing-return count and the
universal target obstruction are the reasons a blanket descent inference was
not adopted. No broader enumeration or universal coverage claim is needed for
the proofs above.
