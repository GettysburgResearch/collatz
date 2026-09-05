# Negative comparison trees and a lossless inverse precision frontier

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05.
Frozen base: `b9a7b7ed0dd0cdf36d9dee578b1c75144ec9266d` in draft PR #90.

**All new mathematical claims are PROPOSED pending independent review.**
A complete proof was attempted, not obtained. The new result is an exact
rank-minimum-preserving pruning theorem for EVERY finite inverse radius, with
at most D^2+1 retained exits at a node with D returns remaining. The cutoff
is derived from an actual finite negative-integer comparison tree, not a
hypothetical ordinary realization of a 3-adic limit. The same comparison
identifies explicit families of positive rank-lowering mergers at its precision
frontier. Neither result proves that every positive source encounters a
sufficiently strong frontier event.

The sixth boundary-fan contribution did land, byte-for-byte, at this base.
Its six Git blob hashes match the supplied ZIP, and both original checkers
were replayed. The parent also contains the separate `CLOCK_DEFECT.md` packet.
Both older files use some `T-ASTRA-030` through `034` identifiers for DIFFERENT
claims. They are cited by filename and SHA here; new IDs use **AS7** and do
not silently resolve or promote either older namespace.

## Claim map

| ID | Result | Boundary |
|---|---|---|
| L-AS7-001 | Signed inverse fan and finite negative comparison precision | No negative-to-positive convergence implication |
| T-AS7-002 | Exact positive-cone matching and a strict rank shield | Applies before the specified precision threshold |
| T-AS7-003 | Lossless depth-dependent pruning for every finite radius | Bounded search is not a total Collatz selector |
| T-AS7-004 | Precision-record paths generate ordinary rank-lowering families | These families are not a complete cover |
| C-AS7-005 | Unbounded delayed interior-return family | A particular path, not a shortest-path theorem |
| R-AS7-006 | 121 has no lower-rank ancestor at ANY depth; exact minimum merging clock is 54 | One source; proves necessity of forward access for this rank |

## 0. Definitions and exact credited input

Use the shortcut map on ordinary integers,

    T(n)=n/2 if n is even; T(n)=(3n+1)/2 if n is odd.

The positive section is H={n>=1:n=1 mod3}, with absorption at 1. On positive
integers define

    h(n)=v3(2n+1),    P(n)=(2n+1)^2 / 3^h(n).

The rank is an integer and P(n)>=2n+1. It is injective: the 3-adic valuation
of P recovers h, and its remaining positive square recovers n. The first
positive-time section return R is defined for every n>1 in H by the finite
odd-run formulas in the earlier packets. No termination of the complete
orbit is assumed.

For signed nonzero arguments of v3 use their absolute values. The negative
section used below is H_-={n<=-2:n=1 mod3}. We only enumerate ancestors that
reach -2 through finitely many first section returns. The ordinary calculation
T(-2)=-1 and T(-1)=-1 shows that -2 is not periodic. There is no assertion that
all negative Collatz orbits converge, nor any need for such an assertion.

The positive section/fan/rank were introduced by PR #91 at
`b8c88843726ee7ac11cf91323c69bf911ca50706`. The boundary-fan proof and its failed
depth-three strengthening are in [BOUNDARY_FAN.md](BOUNDARY_FAN.md), now resident
at the frozen base. Its elementary fan interface is rederived below. No charged
operator theorem, predecessor exponent, or large external computation is used.

## 1. L-AS7-001: the finite negative comparison tree

For y in H\{1} or H_-, write h=v3(2y+1), u=(2y+1)/3^h. Its entire section
predecessor fan is

    s_j = 2^(j+1) 3^(h-j) u - 2,       0<=j<h,
    z   = 2^h u - 1,                  included only if z=1 mod3.       (1.1)

The word from s_j to y is `0 1^j 0`; the word from z is `1^h 0`.
These are first section returns. Starting backwards at 2y, an even predecessor
exits into the section and an odd predecessor continues the residue-2 chain.
The chain ends on entering the section or residue zero. A residue-zero node
has only even predecessors, all still divisible by three. Thus no section
exit is lost. The odd inverse (2m-1)/3 shortens absolute value for |m|>1,
so the intermediate residue-2 chain is finite for either sign here.

All negative fan sources remain at most -2. Furthermore

    |s_j| <= 4|y|,    |z| <= 4|y|.                                  (1.2)

For an even exit this follows from (2/3)^j<=1 and
|s_j|=2^(j+1)3^(h-j)|u|+2; the odd exit is smaller still.

Let C_r be the COMPLETE negative inverse ball of section radius r around -2,
including the root. For v in C_r let t(v) be its section depth and let w_v
be its actual source-to-root shortcut word. Set

    k(v)=|w_v|,    q(v)=number of odd bits in w_v,
    e(v)=q(v)+v3(2v+1),
    B_r=1+max_{v in C_r} e(v).                                      (1.3)

The words are unique. A repeated negative state on a path to -2 would force
a cycle through -2, contradicting its displayed orbit. In particular C_r
is a finite tree of actual ordinary integers.

For a node of section depth t,

    |v| <= 2*4^t,
    h(v) <= 2t+1,
    q(v) <= t^2.                                                    (1.4)

The first inequality follows from (1.2). Then |2v+1|<4^(t+1)<3^(2t+2),
proving the second. Each inverse section edge at level i uses at most h of
its parent, hence at most 2i+1 odd steps. Summing these bounds proves the third.
Consequently

    2 <= B_r <= (r+1)^2+1.                                         (1.5)

There is also a sharper bound needed below:

    |v| <= 2^(k(v)-q(v)+1).                                        (1.6)

Each literal inverse even step doubles absolute value. Each inverse odd step
on a negative integer satisfies |(2m-1)/3|=(2|m|+1)/3<=|m|. Starting at -2
and counting the k-q even steps proves (1.6).

A finite calculation gives the following exact initial precision budgets.
The all-radius bound (1.5) comes from the proof, not extrapolation of this table.

| r | Negative vertices | B_r |
|---:|---:|---:|
| 0 | 1 | 2 |
| 1 | 2 | 2 |
| 2 | 4 | 3 |
| 3 | 8 | 4 |
| 4 | 15 | 6 |
| 5 | 32 | 7 |
| 6 | 60 | 13 |
| 7 | 128 | 14 |
| 8 | 251 | 15 |
| 9 | 494 | 16 |
| 10 | 984 | 19 |

## 2. T-AS7-002: an interior branch follows the negative tree before its precision frontier

Let y>1 in H, h=h(y), u=u(y)>0, and select an even fan exit s_j in (1.1).
Put

    d=h-j,       s_j=2^(j+1)3^d u-2.

If d>=B_r, its entire positive inverse ball of section radius r is in exact
word-preserving bijection with C_r. The positive vertex corresponding to v is

    x_v = 2^(k(v)+j+1) 3^(d-q(v)) u + v.                            (2.1)

Every such vertex has the same ternary depth as v and satisfies

    P(x_v) > (64/3) P(y) > P(y).                                   (2.2)

This excludes every vertex in this WHOLE finite subtree as a rank improvement
on y. It does not say the subtree can never improve rank at a greater radius.

### Exact correspondence and completeness

The initial difference from the negative comparison root is
s_j-(-2)=2^(j+1)3^d u. Along the inverse word w_v, the affine difference is
multiplied by 2^k/3^q, giving (2.1). Since

    d-q(v) >= h(v)+1,                                              (2.3)

the difference in shifted values is divisible by a strictly higher power of
three than 2v+1. Thus h(x_v)=h(v), and their ternary units agree modulo three.
These two facts determine the whole next fan: the h even exits and whether
the terminal odd exit exists. Induction on section depth therefore matches
EVERY child, in both directions. No positive branch is silently omitted.
Positive fan sources stay positive, and their finite parity words are physical.

The comparison does not replace a positive integer by a nonordinary point.
Both x_v and v are explicitly given integers; only their finite congruences
and affine differences are compared.

### Uniform rank shield

Write H_v=h(v), k=k(v), q=q(v), and

    Z=2^(k+j+2)3^(d-q)u.

Then 2x_v+1=Z+(2v+1). By (1.6),

    |2v+1| < 2^(k-q+2),
    |2v+1|/Z < 2^(-q-j) 3^(q-d)/u <= 1/3.

Here (2.3) even gives d-q>=2; the weaker one-third bound is sufficient.
Hence 2x_v+1>(2/3)Z. Since P(y)=3^(j+d)u^2, we obtain

    P(x_v)/P(y)
      > (64/9) 4^k (4/3)^j 3^(d-2q-H_v)
      >= (64/3) (4^k/3^q) (4/3)^j
      >= 64/3.                                                     (2.4)

The middle step uses d>=q+H_v+1 and the last uses k>=q and j>=0.
This proves (2.2), uniformly in y,u,j and the stated inverse radius.

## 3. T-AS7-003: a lossless recursive frontier at every finite inverse radius

Let m_D(y) be the least P in the complete inverse section ball of radius D,
including y. Absorb at 1 and define m_D(1)=3. At a node y>1 with D>=1 returns
remaining, retain:

* the even exits with h(y)-j < B_(D-1);
* the terminal odd exit, when it exists;
* the current node as a possible minimum.

Recurse on the retained exits with D-1 returns remaining. This returns EXACTLY
m_D(y), not merely an upper or lower estimate.

Indeed every deleted exit has a whole remaining subtree with rank>P(y), by
T-AS7-002. Since y itself is in the ball, none can improve the answer. Induction
on D proves equality of the original and reduced minima. This remains valid
when the current node has rank above the original root: the comparison uses
a node already present in the search, not an unjustified global lower bound.

The retained fan has at most

    (B_(D-1)-1)+1 = B_(D-1) <= D^2+1                              (3.1)

members, INDEPENDENT of source size and h(y). Thus a search tree has at most

    1 + sum_{t=1}^D product_{i=0}^{t-1} ((D-i)^2+1)                 (3.2)

nodes before duplicate elimination. This is exp(O(D log D)), not a polynomial
bound in D. The bit lengths of actual source integers are not bounded by (3.2).
Nor are shortcut clocks bounded by D: a retained section edge can contain an
arbitrarily long odd run. Thus this does not contradict CLOCK_DEFECT.md's
short-clock obstruction at high ternary precision.
The source-independent budgets B_r may be precomputed on C_r; alternatively
use the larger proved budget D^2+1, without any negative-tree computation.

For D=1 and D=2, B_0=B_1=2 retains exactly the boundary exits, agreeing with
the earlier radius-two result. For D=3, B_2=3 also retains the next interior
exit. It therefore restores the earlier missed path

    4445077 -> 3333808 -> 833452 -> 208363,

whose shortcut word is 100000. The old boundary-only ball has seven nodes;
the complete ball has twelve; the new reduced ball has eleven and retains
the correct least-rank source 4445077. The full-radius theorem, not this one
control, justifies the recursive rule.

### Two-sided search interface, without a termination claim

For a total SECTION-return budget D, set

    M_D(n)=min_{0<=r<=D} m_(D-r)(R^r(n)),                          (3.3)

stopping the forward orbit upon reaching 1. Equation (3.3) is the exact
minimum rank over diagrams R^r(n)=R^s(x) with r+s<=D. Each inverse minimum
may be computed by the lossless pruning above. No forward-only or inverse-only
restriction is substituted for this two-sided population.

A strict improvement gives a finite physical merging certificate. If none
is found, the correct output is UNRESOLVED AT BUDGET D. Every individual
budget terminates. A proof that every n>1 eventually gives an improvement
would prove Collatz, but is NOT supplied by (3.3) or by the finite branching
bound. The search radius cannot be sent to infinity without that theorem.

## 4. T-AS7-004: the frontier itself generates ordinary rank-lowering families

There is a constructive complement to the shield. Consider an actual negative
inverse path from v to -2 with word w, length k, odd count q, H=v3(2v+1), and

    d=q+H >=2.

Require d to be a STRICT NEW RECORD along this path: every proper section
vertex between -2 and v has smaller q(prefix)+h. Put c=(2v+1)/3^H, a negative
3-unit. For any j>=0 and K>=1 choose a positive odd 3-unit u satisfying

    v3(2^(k+j+2)u+c)=K.                                            (4.1)

Define

    y=(3^(j+d)u-1)/2,
    x=2^(k+j+1)3^H u+v.                                           (4.2)

Take u sufficiently large so x>0. The words w and `0 1^j 0` give an actual
path from x to y, and

    h(y)=j+d,        h(x)=H+K,
    P(x)/P(y) < 4^(k+j+2) / 3^(j+q+K).                            (4.3)

Thus every K with 4*4^(k+j+2)<3^(j+q+K) gives P(x)<P(y)/4.
The parameters j and K have no uniform upper bound in this statement.

### Proof

Up to every proper vertex, initial precision d exceeds the needed q+h.
The same induction as in Section 2 transports the exact section word, until
the final vertex. At that vertex,

    2x+1=3^H (2^(k+j+2)u+c).

Equation (4.1) gives h(x)=H+K exactly. Positivity and integrality of x follow
from (4.2) and a sufficiently large u. All branches replay physically. Since
c<0 and 2x+1>0,

    (2x+1)^2 < 3^(2H) 4^(k+j+2) u^2.

Divide by 3^(H+K) and by P(y)=3^(j+q+H)u^2 to obtain (4.3).

For nonvacuity, choose epsilon=1 or 2 and solve

    2^(k+j+2)u+c = epsilon*3^K mod 3^(K+1).

The coefficient is a unit, and c is a unit, so the solution u is a 3-unit.
CRT with u odd, and then sufficiently large positive lifts, supplies infinitely
many ordinary sources. Any additional finite dyadic source condition may be
imposed when consistent; it is not inferred without checking it.

The same affine progression preserves both exact depths and gives a uniform
rank bound for every positive lift. The implemented cases use 102 record nodes
through negative section depth eight, two values of j, two certified K choices,
two terminal ternary units and two positive lifts: 1,632 actual certificates.
The proof covers all paths/parameters satisfying the statement, not only those
cases. It does NOT say every positive source lies in one of these progressions.

### Precision failure alone is not a descent theorem

Even if the strict shield no longer applies, the actual extra valuation K
may be insufficient. For example the shadow word from -11 to -2 is 1000,
with q=1,H=1,d=2. With j=0,u=31 the positive root is y=139 and the corresponding
source is x=2965. The actual word 100000 sends x to y, but

    P(2965)=3,908,529 > 8,649=P(139).

Here the final precision is at the record frontier, but the valuation gain
is too small. This is a concrete failure of the attempted closing shortcut
"reaching a precision frontier forces a rank decrease." The strict inequality
in (4.3) must be checked or proved; it cannot be assumed.

## 5. C-AS7-005: interior branches can wait an unbounded number of returns

For every d>=2 put

    N=3^(d-1),       C=(4^N-1)/3^d.

One has v3(4^N-1)=d, so C is a positive 3-unit. This elementary valuation
identity follows from v3(4^m-1)=1+v3(m): first for 3 not dividing m, expand
(1+3)^m modulo 9; each replacement m -> 3m raises the valuation by one
using A^3-1=(A-1)(A^2+A+1).

Choose K>=1 with 4*16^N<3^(K+1) and positive odd 3-unit u with

    v3(4^N u-C)=K.

Then

    y=(3^d u-1)/2,     x=(4^N y-1)/3

are positive ordinary section states, after taking positive lifts if needed,
and the actual word `1 0^(2N-1)` proves

    R^N(x)=y,         h(x)=d+K-1,
    P(x)/P(y)<16^N/3^(K+1)<1/4.                                 (5.1)

Every earlier vertex of the pure-even inverse chain satisfies

    h(4^i y)=1+v3(i)<d,
    P(4^i y)>P(y),                 1<=i<N.                       (5.2)

At i=N the even ancestor 4^N y has rank below (3/4)P(y); its odd sibling x
has one third of that rank. Thus this PARTICULAR interior branch can delay
its first pure-even-chain rank decrease for N-1 returns. We do not claim
there is no other, earlier certificate in the full inverse ball.

To verify (5.2), use

    2*4^i y+1=4^i3^d u-(4^i-1)

and 1+v3(i)<d for i<N. At i=N the two terms can cancel; explicitly

    2x+1=3^(d-1)(4^N u-C).

This gives the exact depth and strict rank ratio in (5.1). The inverse
chain follows ordinary even steps and the odd sibling follows the displayed
word; all of its intermediate states exceed the positive endpoint. CRT
supplies infinitely many u for every d,K. No unbounded backtrace is asserted
to have a single positive starting source.

This family illustrates why permanent deletion of an interior branch is
unsound. The new pruning only deletes it within its proved finite budget,
and reconsiders it when the budget increases.

## 6. R-AS7-006: an inverse-only completion is false, even without a depth cap

For the global rank P, the full set of positive integers below P(121)=243 is

    {1,2,3,4,5,6,7,10,13,22,40}.                                  (6.1)

This is a finite exhaustive statement: P(x)>=2x+1 limits every candidate to
x<=120, and direct factorization gives the list. The union of their ENTIRE
forward orbits is the finite forward-invariant set

    U={1,2,3,4,5,6,7,8,10,11,13,17,20,22,26,40}.                   (6.2)

One checks the next T-value of each member of U, and the list (6.1) is contained
in U. Since 121 is not in U, NO lower-rank positive integer ever reaches 121.
Therefore its inverse ball has minimum rank 243 at EVERY radius.

More strongly, direct physical replay gives

    T^54(121)=40,
    T^r(121) not in U for every 0<=r<54.                            (6.3)

Any lower-rank merging witness has its whole orbit in U, so every diagram
T^r(121)=T^s(x) with P(x)<243 must have r>=54, regardless of s. The choice
x=40,s=0 attains r=54. Hence the minimum possible max(r,s), and also minimum
r+s, is exactly 54 for this source and rank.

These are finite certificates with all-witness/all-depth implications, not
bounded-search failures extrapolated to infinity. The finite lists and all
54 prefix values are reconstructed by both programs. They show why even a
complete inverse solver is insufficient alone: forward access to a different
endpoint is mathematically necessary for some residual sources.

## 7. Attempted full closure and first unsupported inference

The preceding packet's failed strategy was to discard all interior exits
recursively. The present theorem repairs that failure: retain a depth-dependent
frontier, prove exactly what each deleted subtree can do, and allow the frontier
to expand. The proof is uniform over every finite search depth.

The negative comparison is more than a bound: its precision records generate
ordinary positive mergers with arbitrarily large valuation gains. This turns
some previously uncontrolled interior histories into explicit reduction rules.
But it does not prove that every given positive u satisfies a rank-crossing
congruence from one of these records. The example y=139 shows why the mere
loss of precision cannot substitute for the needed gain. The all-depth
inverse minimum at 121 shows why an inverse-only completion is impossible.

**Q-AS7-001 (OPEN).** Prove that for every positive residual n, some finite
forward endpoint R^r(n) has a retained or precision-frontier ancestor x with
P(x)<P(n), with all physical guards retained. A recursively described selector
must have its termination proved, not merely terminate at each individual
finite radius. This would contradict a minimum-rank exceptional component and
prove Collatz. No such total selection/coverage theorem has been obtained.

There is no claimed uniform clock bound, no positive counterexample, no
nontrivial positive-cycle exclusion beyond prior finite controls, and no
promotion of SC*, FC*, the Green criterion, or the signed budget.

## 8. Evidence, literature, and provenance

The [experiment](../../experiments/X-AS7-001-shadow-frontier/README.md) compares
the complete and reduced inverse balls in 478 cases, including ternary depths
up to 256. It reconstructs the full negative cone through depth ten, exact
positive/negative cone bijections, 1,632 precision-record bridges, the delayed
family, the old lost-interior example, and the exhaustive witness set for 121.
These are implementation checks, not a substitute for the all-parameter proofs.

The verifier imports neither generator code nor a repository module. It uses
literal signed inverse stepping, rational backward word evaluation, a separate
CRT algorithm, and full inverse enumeration. Both programs share an author;
this is implementation independence, not independent mathematical review.

External positioning only: Monks, Monks, Monks and Monks, *Strongly sufficient
sets and the distribution of arithmetic sequences in the 3x+1 graph*,
arXiv:1204.3904v2 (2012), abstract consulted 2026-09-05. Sufficient sets,
backtracing and congruence restrictions have substantial prior literature.
No general priority claim is made for them. No theorem from that paper is a
proof dependency here; a comprehensive novelty comparison has not been done.
Source: https://arxiv.org/abs/1204.3904 .

Frozen repository references:
- boundary-fan publication: b9a7b7ed0dd0cdf36d9dee578b1c75144ec9266d;
- parallel clock-defect packet: a4b9b3a267e526f2b33ffd43c3b60d58be2aed5d;
- original source rank/fan: PR #91 at b8c88843726ee7ac11cf91323c69bf911ca50706;
- older global normalization: REMAINDER_CANCELLATION.md at
  908fdca1fe21456f8c6d476b31b74c8552670395.

The new packet rederives all elementary facts it uses. The original sixth-pass
proof text, manifest and checkers are preserved unchanged; historical statements
that its authoring session did not publish it remain accurate for that session.
