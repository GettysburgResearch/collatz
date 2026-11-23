# An exact ancestor optimum need not have a balanced word

Date: 2026-11-23. **Scoped diagnostic, not escape or cycle exclusion.**

This note checks a proposed continuation of PR182's common pressure
maximum and tests whether Christoffel extremality supplies its missing
closing step. The continuation is valid. The proposed automatic passage
from an optimal ordinary ancestor to a balanced word is not valid.

## 1. The continuation of the common-root argument is correct

Let E be an escaping component of positive odd integers coprime to three.
Assume the already supplied positive function r satisfies

\[
0<r(n)\le 1/n,\qquad 2^{a(n)}r(n)=3r(U(n)).
\]

Let m be the least ordinary integer attaining the global maximum of r.
For a target q on the actual forward orbit from m, write h,A for the
number of odd steps and their total gap. The edge equation telescopes:

\[
r(m)=\frac{3^h}{2^A}r(q).
\]

Every positive odd unit ancestor n of the same q, at any depth k and
total gap B, satisfies

\[
\frac{3^k}{2^B}=\frac{r(n)}{r(q)}
\le \frac{r(m)}{r(q)}=\frac{3^h}{2^A}.
\]

There is no depth cap in this comparison. Equality holds exactly when
r(n)=r(m). If k=h and B=A, equality is automatic; leastness of m among
maximizers gives n>=m. Writing the exact affine relation as

\[
2^Aq=3^h n+C_w,
\]

shows that m also maximizes C_w within this **ordinary, positive, unit,
fixed-target admissible fibre**. The order of that fibre cannot be
replaced by the order on all binary words of the same length and weight.
These conclusions extend PR182's displayed common-root identities; they
are not an additional global closure theorem.

## 2. An all-depth optimum with an unbalanced word

Consider the actual odd trajectory

\[
31\to47\to71\to107\to161\to121\to91.
\tag{1}
\]

Its gaps are

\[
(1,1,1,1,2,2),\qquad h=6,\quad A=8,
\qquad \gamma_* =3^6/2^8=729/256.
\]

**Claim.** For each of the seven targets in (1), including 31 itself,
the displayed path from the same source 31 uniquely maximizes the
coefficient 3^k/2^B among every positive odd unit ancestor, at every
depth. Thus this is not merely a fixed-depth optimizer.

For any actual ancestor n of a positive target q, the affine correction
is nonnegative, so

\[
\gamma(n,q)\le q/n.
\tag{2}
\]

This includes the zero-step path; the inequality is strict on every
positive-length path. At the j-th target q_j, let A_j be the original
total gap and gamma_j=3^j/2^{A_j}. Direct integer comparisons give

| j | q_j | A_j | q_j 2^{A_j} | 32*3^j |
|---:|---:|---:|---:|---:|
| 0 | 31 | 0 | 31 | 32 |
| 1 | 47 | 1 | 94 | 96 |
| 2 | 71 | 2 | 284 | 288 |
| 3 | 107 | 3 | 856 | 864 |
| 4 | 161 | 4 | 2576 | 2592 |
| 5 | 121 | 6 | 7744 | 7776 |
| 6 | 91 | 8 | 23296 | 23328 |

Consequently q_j/32<gamma_j. Equation (2) excludes every n>=32
uniformly over all depths. At the final target the comparison reduces
particularly simply to

\[
91/32=728/256<729/256.
\]

The positive odd units below 31 are exactly

\[
1,5,7,11,13,17,19,23,25,29.
\]

Their literal odd trajectories reach one without meeting any target in
(1). The exact control records all ten paths. Source 31 also reaches
one, as the control records, so it cannot return to any nontrivial
earlier state. Hence its displayed first visits are its only visits to
these targets. This completes the unrestricted proof of the claim:
the finite certificate covers only n<32; inequality (2) covers every
larger integer and every clock.

The shortcut parity word of (1) is **11111010**. Its cyclic length-four
windows include 1111 and 1010, containing respectively four and two
ones. Therefore it is not balanced. Equivalently the gap word contains
both consecutive 1,1 and consecutive 2,2, whose two-gap totals differ
by two. It is not a rotation or repetition of the Christoffel word of
the same parameters.

This also gives every incoming coefficient inequality at the same root
31: any nonempty unit inverse path ending there starts at n>=31 and
has positive affine correction, so 3^k/2^B<1. The six displayed
nonempty forward prefixes have coefficient greater than one.

The example is entirely in the known basin of one. It does **not**
construct the infinite escaping ray or a positive r on its entire
component. It disproves the proposed local-to-global principle that
all-depth fixed-target optimality, even at one common root across
successive targets and with all incoming inequalities, already forces
every displayed word to be balanced. An additional genuinely infinite
argument would be needed to use the hypothetical common root.

## 3. The ordinary fibre is not closed under balancing

A second exact example isolates integrality, in the positive-cycle
denominator regime. The ordinary path

\[
11\xrightarrow{1}17\xrightarrow{2}13\xrightarrow{3}5
\]

has h=3, A=6, and carry C=9+6+8=23. Among all positive three-gap
compositions of total six, it is the only one giving a positive odd
unit integer ancestor of target five. The ten possibilities are checked
exactly, not sampled.

Balancing to gaps (2,2,2) raises the carry to 9+12+16=37. Its
fixed-target input becomes

\[
\frac{2^6\cdot5-37}{3^3}=\frac{283}{27},
\]

which is positive but not an ordinary integer. Thus the balancing move
does not furnish a competing ancestor and does not contradict the
ordinary optimizer.

## 4. Exact literature interface

Knight's *Collatz high cycles do not exist*, Discrete Mathematics
349(3), 114812 (2026), concerns the rational cycle maximizing the
minimum cyclic state at fixed length and odd count. The publisher's
abstract and introduction were read; the HAL full text was blocked,
so no claim of reconstructing Knight's complete proof is made here:
<https://www.sciencedirect.com/science/article/pii/S0012365X25004200>.

Fernandez and Ibanez's primary preprint arXiv:2607.24844v1, Sections 3
and 7, states its optimization explicitly as
max_w min_rotation C(rotation(w)) over **all** binary words of given
length and weight. The definitions and Theorem 7.3 were read:
<https://arxiv.org/html/2607.24844v1>.

That objective differs from the fixed-target coefficient and carry
objectives in section 1. In addition, positive rational cycles require
2^A>3^h. The hypothetical escape optimizer's nonempty forward prefixes
instead satisfy 2^A<3^h, as PR182 proves. Applying positive-cycle
nonintegrality directly to those forward prefixes therefore also
changes the denominator regime. Neither literature statement supplies
the omitted admissibility-preserving, infinite continuation argument.

No new Lean wrapper is claimed for the telescoping observation. The
companion exact program checks only the displayed certificates and
the elementary comparisons; the all-depth coverage is the proof (2).
