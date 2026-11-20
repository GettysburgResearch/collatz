# A terminal phase budget for homogeneous five compilers

**PROPOSED application of the existing stopping-grade mechanism.**
This note rules out completeness of a specified compiler architecture.
It does not rule out five-closure, a compiler with other physical exits,
or a Collatz proof.

The general stopping grade, affine-edge invariant, and a finite-seed
obstruction for a different exponential family are already in PR146,
fd991063721e9c157d318e40bb20131762f7d750,
research/upper-bit-mergers/BASIN_PHASE.md, especially “The obstruction
on the smallest nontrivial witness family.” PR157, GCL-002, already
uses the exact grades of 5 and 25 to obstruct a uniform inverse-five
lift. No priority for either invariant or that example is claimed.

The additional scope here is **arbitrary compositions from an unbounded
dictionary of proportional five rewrites, with any finite certified
terminal library**, tested on the one-odd-step antecedent family from
PR157 GCL-001. Ordinary reverse edges may be used in each rewrite.

## TP1. The preserved quantity

For n whose actual ordinary orbit reaches 1, let tau(n) and r(n) be
its first-hit shortcut clock and number of odd inputs. Set

\[
 H(n)=\tau(n)-2r(n).
\]

Appending a whole turn of the 1,2 cycle adds two clocks and one odd
input, so H is independent of such padding. For every finite ordinary
prefix of length L with p odd inputs, including one extending past a
first hit,

\[
 H(n)=L-2p+H(T^L n).                                    \tag{1}
\]

Whenever both x and 5x converge, define

\[
 \Delta(x)=H(5x)-H(x).
\]

A homogeneous forward five block consists of actual finite paths

\[
 T^L(x)=q,\qquad T^L(5x)=5q
\]

with the same odd count p on both arms. Equation (1) gives

\[
 \Delta(x)=\Delta(q).                                   \tag{2}
\]

Every block in PR166's ladder and the new valuation-word transformation
(1,1,1,b) to (1,2,5,b-5) has this property.

### Extension to arbitrary native affine paths

More generally, allow finite paths made from actual ordinary T edges
in either direction. A forward even or odd edge has slope 1/2 or 3/2;
its inverse has slope 2 or 2/3. The composed slope therefore has the
form 3^j/2^k with signed integers j,k. Along such a path from v to w,

\[
 H(v)-H(w)=k-2j.                                       \tag{3}
\]

This follows edge by edge from (1). Positivity, divisibility and parity
guards remain part of the meaning of an actual path.

Suppose two such fixed affine paths, valid on a nonconstant arithmetic
progression, take the pair (x,5x) to (q(x),5q(x)). The endpoint slopes
force their two native path slopes to be equal. Unique factorization
then forces both signed j values and both signed k values to be equal.
Subtract (3) on the two arms to obtain (2).

Thus arbitrary native reverse edges, unequal total path lengths, and
nonmonotone intermediate heights do not defeat the phase invariant.
The two paths may be chosen adaptively for the supplied source from
an infinite dictionary of such whole-family identities. Every stage
still preserves Delta. Singleton numerical coincidences or rewrites
with nonproportional endpoint pairs are outside this statement.

## TP2. No bounded-below terminal phase library is complete

Let Q be any collection of terminal parameters for which both q and 5q
are certified to reach 1. Suppose their phases are bounded below:

\[
 \Delta(q)\ge D\quad(q\in Q)
\]

for some integer D. Every finite certified terminal library has this
property.

**Theorem.** No compiler using only the proportional native affine
rewrites of TP1, followed by a terminal in Q, can succeed for every
positive odd ternary-unit x with a supplied convergence certificate.

The proof uses the known rank-one family

\[
 x_a=\frac{4^a-1}{3},\qquad a\ge2,\quad3\nmid a.
\]

Each x_a is an odd ternary unit with U(x_a)=1 and
H(x_a)=2a-2. PR157's exact positive path, reconstructed below, shows
that y_a=5x_a uses at least 2a-1 odd inputs before it could first reach
1. If y_a does converge, write r_y for its first-hit odd count.
Every odd input before that hit is at least three. The exact product
identity along its path gives

\[
 2^{H(y_a)}
 =y_a(3/4)^{r_y}\prod_{j<r_y}\left(1+\frac1{3n_j}\right)
 \le y_a(5/6)^{r_y}.
\]

Consequently

\[
 \boxed{2^{\Delta(x_a)}
 <\frac{20}{3}(5/6)^{2a-1}.}                            \tag{4}
\]

The right side tends to zero. This is asserted only if y_a converges.
There is no assumption that all members of that target family are
already known to converge.

For an explicit simple bound, 20/3<8 and (6/5)^4>2 imply

\[
 \Delta(x_a)<\frac{13-2a}{4}.                            \tag{5}
\]

Choose any a>=max(2,7-2D) with 3 not dividing a. If the proposed compiler
succeeded on its supplied rank-one certificate, its terminal
certificates and actual ordinary paths would prove that y_a converges.
All the grades used in (2)--(5) would then be defined. Preservation gives
Delta(x_a)=Delta(q)>=D, whereas (5) gives Delta(x_a)<D. This is the
required contradiction.

The argument covers every adaptive search using these proportional
native affine rewrites with a bounded-below terminal phase set. It is
not a finite-search obstruction. An enlarged finite terminal list
cannot repair the architecture. The result is compatible with full
Collatz convergence: under that conjecture the phases in (4) simply
become unbounded below.

## The exact prefix furnishing the rank lower bound

PR157, 64361ecca770092d6c8242dc6211e38818af2e50,
research/global-closure-20261120/closing-attempts.md, GCL-001, proves

\[
 U^{2a-1}(5x_a)=\frac{5\,9^{a-1}-1}{4},                  \tag{6}
\]

with exponent word 2, followed by 2a-3 ones, followed by 3.
To reconstruct it, the first numerator is
4(5*4^(a-1)-1), with odd parenthesis. Put m=a-1.
After that first odd step, successive valuation-one states are

\[
 5\,3^j2^{2m-j}-1\quad(0\le j\le2m-1).
\]

The next numerator is 2(5*9^m-1), whose valuation is exactly three
because 9^m=1 mod8. All these states, including endpoint (6), are above
1 for a>=2. This proves the needed lower bound on r_y independently
of eventual convergence of y_a. The one-step source certificate is
always known.

## A fully certified infinite example for a one-seed compiler

The previous theorem needs no unproved target convergence. There is also
an explicit family for which both targets are known to converge.
Let L=17+18k, k>=0, and

\[
 x=\frac{5\,2^L-7}{9}.
\]

These are odd ternary units, beginning at 72817, in the original
ladder cylinder 49 modulo 64. The source word (2,L-2) reaches 5 and
the target word (5,L-5) reaches 25, both at clock L with two odd
inputs. The actual first-hit data are

| n | tau(n) | r(n) | H(n) |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 5 | 4 | 1 | 2 |
| 25 | 16 | 7 | 2 |

Thus H(x)=H(5x)=L-2 and Delta(x)=0, whereas Delta(1)=2.
No composition of the specified rewrites sends any member of this
family to terminal parameter one. This separates a known successful
ordinary pair from a successful block-to-one compiler. It is a direct
family extension of the already-published x=5 grade example.

## Scope for the energy route

The invariant is not defined here for a nonconvergent target 5x. The
no-go proof uses it only after a purported successful terminal
certificate establishes convergence. In the explicit family above the
metric defect is already zero. These examples therefore do **not**
refute a contraction estimate restricted to hypothetical nonzero
defect support. They refute the specified universal compiler claim.

A complete proof may use singleton numerical certificates, other
intermediate comparisons, or a terminal class with unbounded phase,
provided its own termination and coverage are proved. No such complete
replacement is proved here.

## Source identity and comparison

- PR146 at fd991063721e9c157d318e40bb20131762f7d750,
  BASIN_PHASE.md: the general grade/affine invariant and its existing
  finite-seed application to exponential families.
- PR157 at 64361ecca770092d6c8242dc6211e38818af2e50,
  closing-attempts.md, GCL-001: the exact rank-one source and long target
  prefix; GCL-002: the exact 5/25 obstruction to the uniform inverse
  lift, with its prior PR150 LC-1 and earlier grade sources.
- PR166 at 5996b9f525ca50978bc34f423192c36a87765bf3,
  FIVE_CERTIFICATE_LADDER.md, FL1--FL3: the homogeneous compiler whose
  existing stated language remains valid. TP2 rejects a particular
  proposed extension to all certificates, not that published theorem.
