# Root reconstruction of the global-forcing packet

## Verdict and exact scope

**VERIFIED WITH NAMED EXTERNAL INPUTS** for SRC-001--SRC-005;
**VERIFIED** for the elementary CF1--CF5, CR1--CR3 and TP1--TP2
statements at the file identities below. These are scoped internal
mathematical reviews, not external referee acceptance, a formal
proof-assistant build, or a proof of Collatz. The universal closing
obligations remain **OPEN**.

The root reviewer did not author these four proof notes. The review
reconstructs their ordinary domains, algebra, quantifiers, constants and
conditional dependencies. It is not inferred from passing the accompanying
finite programs. Execution receipts are recorded separately.

| Reviewed note under research/global-forcing-20261121/ | SHA-256 |
|---|---|
| arithmetic/SHIFTED_RANK_COMPACTNESS.md | 25af03cd100c76d2fdaff86155fecba366c1d9ae085ce38790a99ed9a0f02095 |
| certificates/CARRY_COMPILER.md | 394571cd06d55caa4465cdb7a1d76cefc1d36b29bfc41522ac5a2c136f6cf7ea |
| energy/COUPLED_RENEWAL.md | 1ac74226cc170ca3000ccd24359093dc9c2d652db1a23d323211f4b4f90ada11 |
| energy/TERMINAL_PHASE.md | a6244f942da0f2b597fa3d204300dc300fec1200f13004e43b68438c5ebd0280 |

The final source refresh found concurrent PR167--169 and a later PR146.
The front-door source comparison and the three LATEST_COMPARISON notes
qualify originality and coverage. In particular, CF1 independently
reconstructs a short identity already present in concurrent PR168.
CF5 is a concrete language within PR168's more general balanced-return
recognizer. Neither distinction changes the verified algebra. Frozen
proof notes preserve their initial source lists; they are not exhaustive
priority claims.

## 1. Shifted multiplicative rank

For an odd defect edge, the shifted equation is

    2^b + (3/2)m - 2^b m' = 1,    m=n+1, b=a(n)-1>=1.

When m=c_i u and m'=c_j v, the tuple (2^b,u,2^b v) lies in the
group of triples (2^z,g,2^z h). Its rank is at most 2r+1,
regardless of the primes or heights in the coefficients c_i,c_j.
In this ordered tuple, the three proper two-term subsums are respectively
positive, 2^b(1-m')<0, and 1-2^b<0. Single terms do not vanish.
The tuple also recovers b and n, so counting solutions bounds distinct
ordinary edges. This does not bound repeated visits to one edge.

The general-rank theorem is the needed one, rather than a finite-prime-pool
estimate. The root opened Evertse--Schlickewei--Schmidt, Theorem 1.1
(arXiv:math/0409604, printed page808), and checked its uniform bound
exp((6t)^(3t)(rank+1)). For t=3 and rank at most 2r+1 this gives
exp(18^9(2r+2)). Since log 2>1/2, the chosen integer
2^(4*18^9*(r+1)) is a larger bound. Summing over k^2 ordered coset
pairs is legitimate; a new group chosen separately for each edge is not.

A maximal initial one-run has length v_2(n+1)-1. Its exact shifted
growth is multiplication by 3/2 at each step. Starting from a fixed
ordinary integer and splitting a simple prefix at defects yields the
stated binary-clock recursion and the finite prefix bound. Thus a
nonperiodic orbit cannot stay eventually in finitely many cosets of one
finite-rank group. This assertion concerns the same fixed orbit; the
inverse tower in SRC-005 instead changes the source with its depth.

For cycles, the minimum is preceded by a defect because a valuation-one
edge strictly increases every odd state. If h=log_2(min(n_i)+1),
a block with one final defect has length at most its initial shifted
logarithm, and its shifted peak is less than the square of its initial
shift. Iterating over d blocks gives N<2^d h and maximum shifted
logarithm at most 2^d h.

The root also opened Lagarias, arXiv:math/0512006 v4, Lemma2.2(1),
equation(2.4), printed page10, to check the exact inequality

    |log_3(2)-p/q| >= 1/(1200*q^14.3).

For the positive cycle linear form A log2-N log3, take p=N,q=A.
The cycle product gives 0<Lambda<N/(3*minimum), while A<=2N.
Weakening the resulting exponent yields
minimum<400*2^14*N^15, and hence
h<23+15d+15 log_2 h. The increasing function
h-15 log_2 h for h>=256d, together with
241d-105>23+15d for d>=1, excludes h>=256d.
This reconstructs N,log_2(max(n_i+1))<256*d*2^d.

Fixed-block cycle finiteness is classical. The root inspected
Simons--de Weger, version1.44, section6.1/Lemma14, and its block
normalization in section1.1. The packet correctly presents its new
interface as the rank/coset-controlled ceiling, not a discovery of that
classical finiteness mechanism. The resulting exhaustive finite decision
procedure is mathematically specified but was not executed.

For absolute shifted rank one, all positive integral shifts are powers
of one integer base. Two such shifts cannot have ratio3/2, excluding
valuation-one edges. Every remaining odd state above one strictly
decreases. This excludes a nontrivial cycle in that restricted class,
not in a union of arbitrary rank-one cosets. The source-varying inverse
tower is an essential negative control against a universal bounded-rank
assumption.

Primary sources:

- https://arxiv.org/pdf/math/0409604
- https://arxiv.org/pdf/math/0512006
- https://math.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf

## 2. Carry-four ordinary realization

The source/target seven-letter entry words each have clock15 and
odd count7, with corrections3709 and149617. Their difference after
multiplication by five is exactly4*2^15. The base source is25065;
the full exact source cylinder is25065 modulo65536, not modulo32768.
The extra binary bit forces the terminal quotient to be odd. Adding a
multiple of65536 leaves every intervening odd quotient's parity unchanged
on both arms, proving exact ordinary legality on every positive lift.

For a valuation-one source z, the identity

    3(5z+4)+1 = 5(3z+1)+8

gives the same exact valuation and transports the carry unchanged.
For the exit, if U(z)=v and the source next exponent is b>=2,
then v=1 modulo4. The first target numerator is8(5v+1), of exact
valuation4, and the next numerator is5(3v+1)/2. This proves the
two-letter exit to5q with exponents4,b-1.

Independent concatenation gives the source correction
B_r=1351*3^(r+5)+2^(r+16) and target correction5B_r. These identities
hold for every supplied legal run length r, not just the lengths checked
by a program. They do not assert ordinary height descent.

For the explicit rank family, the root checked the base congruence
4^81=1+178*3^5 modulo3^10 and the cubing induction at the boundary
r=0 as well as for general r. The definition
t_r=88*2^(-r) modulo243 makes the full inverse numerator congruent
to3^(r+9) modulo3^(r+10), proving the claimed source unit condition.
Full inverse integrality reduces recursively modulo three; positivity
and oddness follow at each inverse step. The last exponent exceeds two,
and an integral inverse of an odd integer greater than one cannot equal
one. This establishes first hit, rather than mere arrival.

The short four-letter block has corrections65 and325, source class
271 modulo512, and q<x/6. Concurrent PR168 contains this identity
already. The production parser consumes a supplied finite first-hit word,
uses distinct block beginnings, and validates the transformed word.
Returning UNRESOLVED on another valid word is preserved as a real
coverage limitation.

Two other route agents independently reconstructed the carry construction.
Their review files distinguish mathematical reconstruction from each
reviewer's own finite replay.

## 3. Positive renewal and endpoint coupling

Each legal physical block gives the exact equality e(x)=e(q) for an
ordinary-invariant metric label. All nonzero contributions have q>=5,
since the known pair1,5 is in one component. The three domains are
disjoint by their initial valuations, and the carry run length is unique.
For the safe carry sublanguage, b>=r+2 is an explicit hypothesis.

At fixed endpoint q, the first family has a single allowed exponent
class with period2*3^r; the short family has period54; the carry
family has period2*3^(r+8). Each inverse has a positive subtracted
constant, so raising its exponent by one period grows the source by
strictly more than the corresponding power of two. The source-unit
guard only deletes summands.

The carry inverse ratio satisfies

    x/q >= (4849051/98415)*(4/3)^r*2^delta,
    delta=b-r-2>=0.

Its correction gives 2^b q=7 modulo27 for all r, including zero.
Writing b_0 for the resulting residue modulo18 gives the lower bound
delta>=(b_0-r-2) modulo18. Grouping the whole nonnegative r sum by
its18 residue classes produces the stated finite rational polynomial
divided by1-(393/500)^18. No run cutoff or random residue reset is
used.

The root independently reconstructed the exact Fraction comparisons,
including the seven rational power enclosures, the common endpoint
cases, and the harmonic interpolation inequality. The main subcritical
case is

    330293/331700 + 1/300 = 248549/248775 < 1.

The case q=16 or25 modulo27 is smaller, as is the complementary
case q not congruent to7 modulo9. These cases exhaust ordinary
ternary units. All contributing endpoints satisfy q<x/6, giving the
finite cutoff in CR3. The inequality
5^25<6^4*4^25 supplies the harmonic coefficient4/5.

At each finite X the energy sum is finite. Subtraction there, followed
by monotone passage to infinity, gives precisely the conditional
finiteness equivalence and constants248775/226 and5. It does not
justify subtracting two infinite energies and does not show that
the uncovered Q is finite. The expanding r=20,b=2 carry example
correctly remains outside the contracting sublanguage.

## 4. Terminal phase architecture

For actually convergent n, H(n)=tau(n)-2*odd_count(n) is unchanged
by padding complete1,2 cycles. A signed native affine path has slope
3^j/2^k and grade change k-2j. Whole-family paths from (x,5x) to
(q(x),5q(x)) have equal slopes on their two arms, forcing equal j,k.
Thus their phase difference is preserved even when intermediate pairs
have nonzero offsets or the paths use legal reverse edges.

For the always-certified rank-one antecedents, the exact target prefix
from PR157 and the first-hit product bound give the stated exponentially
small upper bound for2^Delta, conditional on target convergence.
The proof's order is sound: a hypothetical successful compiler first
certifies that convergence; only then is Delta used. No global
convergence assumption is hidden in the obstruction.

A terminal library whose phases are bounded below cannot serve this
entire family through proportional native rewrites, even with an
infinite dictionary and adaptive choices. The theorem does not exclude
inhomogeneous final comparisons, singleton constructions, or an
independently justified unbounded phase budget. PR146's invariant and
its now-expanded bounded-link-budget obstruction must retain credit.
The fully certified zero-phase controls are good pairs, so this
architecture obstruction is not a disproof of energy control on
hypothetical failed pairs.

## 5. Conditional bridge found in the source refresh

The root reconstructed the energy refresh's conditional passage from
positive lower density of invariant sets to uniformly positive
stationary-weighted mass. Its PD and stationary-density hypotheses
remain named, source-qualified assumptions. Removing a fixed high-binary-
valuation tail and mapping each remaining nonunit to its next odd-step
image is finite-to-one and increases height by at most a factor2.
The author-stage factor3/2 omitted the additive half when the source
is odd; this was repaired to2 before publication. The lower density
eta is explicitly measured among all positive integers, matching Haar
measure on the whole ternary space.

Under the stated L1 stationary-density result, its positivity almost
everywhere on ternary units follows from the stationary support
inequality and ergodicity of multiplication by two there. A small
positive level set, L1 convergence, and exact ordinary densities of
periodic sets then give the uniform lower bound a*eta/4. This requires
no equidistribution of the invariant set. The conditional argument is
VERIFIED WITH THESE FIXES. It removes a weighted-mass premise only;
it does not construct the needed ordinary periodic approximations.

## First unsupported global step

None of these verified restricted statements proves finite uncovered
Q, a successful certificate transformation for every supplied input,
or an arithmetic upper restriction that excludes unrestricted positive
cycles and unrestricted rank growth. The concurrent-source comparison
does not import an unproved regularity or moment hypothesis as the
missing theorem. These are the exact remaining global obligations.
