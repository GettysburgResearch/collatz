# Route 2 — every lower-rank merging proof must sometimes climb much higher

**Status: PROPOSED pending independent review.** The full lower-rank merging
cover is OPEN. This pass supplies a necessary resource bound for ALL merging
diagrams, together with explicit ordinary infinite families that repay that
resource cost. It does not presume that enlarging a search eventually succeeds.

Use T and the SAME integer rank R from [RANK_MOMENTS.md](RANK_MOMENTS.md). Two
ordinary sources n,x merge if T^r(n)=T^s(x) for finite r,s>=0. The rank cost of
a diagram is the maximum R over both finite paths, including both starts and
the common endpoint. Let C_R(n) be the least such cost among diagrams with
R(x)<R(n), or infinity if none exists.

## 1. T-A3-1051 — a forced first-edge rank barrier for every diagram

Let n be odd and H=v3(n)>=1. Then

    R(n)=n^2/3^H,
    R(T(n))=((3n-1)/2)^2,
    C_R(n) >= ((3n-1)/2)^2.                              (1)

This covers arbitrary lengths, arbitrary unequal clocks, and every ordinary
lower-rank witness x. It is not limited to a selected inverse word or compiler.

### Proof

For any multiple z of 3, h(z)=v3(2z+1)=0. The only possible rank entries are
z^2/3^v3(z), (z-1)^2 and (z+5)^2. For z>=3, the first is at most z^2/3 and
strictly below (z-1)^2, so it is the minimum. This proves the first formula.
The endpoint y=(3n+1)/2 is 2 modulo3, so all three entries have ternary order
zero and R(y)=(y-1)^2. This proves the second.

An integer multiple of 3 has no odd shortcut predecessor: (2z-1)/3 is not
integral. Reversing any number of T steps from n therefore gives ONLY
2^j n, j>=0. Their ranks are exactly 4^j R(n), never smaller. Thus a
lower-rank merging diagram cannot have r=0. It must include the first forward
edge n->T(n), proving (1). The equivalent undirected-graph argument says that
all reverse paths initially stay on this unbranched even ray; the only exit
is the indicated forward edge.

Consequently the mandatory excursion ratio is

    C_R(n)/R(n) >= (3^H/4)(3-1/n)^2.                    (2)

No fixed multiple of the starting rank suffices as a universal intermediate
rank cap. On n=3^H, the bound is quadratic in the starting rank R(n)=n. A
claim of an upper bound or of convergence for every power 3^H is NOT made.
In particular, the parent's endpoint cap x<=R(n) for a lower witness never
licensed applying that cap to intermediate vertices. This theorem demonstrates
exactly how badly that intermediate-cap substitution can fail.

## 2. T-A3-1052 — an infinite family attaining the barrier scale

For each H>=2 impose the ordinary congruences

    n=3^H mod 3^(H+1),
    n=1+4^H mod 2^(2H+1).                                (3)

CRT gives infinitely many positive sources for every H. They have v3(n)=H,
v2(n-1)=2H and active mode a=1. The total acceleration consumes exactly H
copies of 10, with endpoint

    y=1+(3/4)^H(n-1).

The component at index1 gives

    R(y) <= (3/16)^H(n-1)^2
          <(9/16)^H R(n)<R(n).                          (4)

The first inequality uses v3(n-1)=0, so v3(y-1)=H; it does not require guessing
the endpoint's minimizing component. These are genuine finite merging diagrams
with witness x=y (its backward clock is zero).

During the word (10)^H, successive odd starts decrease toward1. The largest
ordinary value is T(n)=(3n+1)/2. Since R(z)<=z^2, combining this explicit
path with (1) yields the all-diagram optimal-cost bracket

    ((3n-1)/2)^2 <= C_R(n) <= ((3n+1)/2)^2.              (5)

Its width is exactly 3n. The family has unbounded ternary height, unbounded
necessary relative rank excursion, and a proved finite repayment. A bounded
relative-cap search would miss these reductions even though the displayed
path is elementary. This is a common-rank resource theorem; no external
novelty is claimed for the elementary alternating numerical descent word.

For example H=2 gives the progression beginning at n=657. Its rank is47,961;
the four-step endpoint is370, whose rank is15,129. Every lower-rank diagram
must encounter rank at least970,225, while this diagram stays below972,196.
The named endpoint is verified by literal stepping in the new checker.

## 3. Complete finite rank balls are useful but do not remove the barrier

T-A3-1001 gives a complete short enumeration of all rank<=B vertices, in fewer
than9sqrt(B) candidates after actual rank filtering. Hence a graph induced by
one rank ball is finite, and every simple path in it has length less than the
vertex count. Physical edges and same-rank components can be checked exactly.

That is a valid decision for a GIVEN resource cap. It is not a complete merging
procedure with B fixed as a small multiple of R(n). Equations (2)-(5) show that
some legitimate reductions require much more intermediate rank. Nor does the
counting theorem prove any global upper bound on C_R(n). Increasing the cap
until an unproved reduction appears is not a total selector.

The full end-to-end argument remains: an exceptional component has a minimum
positive integer rank; a finite lower-rank merging diagram for every possible
minimum contradicts that choice. This covers both cycles and nonperiodic
orbits. The parent supplied local inverse fans and partial reductions; this
pass proves how much resource a universal extension must allow and resolves
one unbounded family at that resource scale. A complete recursively closed
cover of the remaining sources is NOT supplied.

## 4. Relation to adjacent work and finite checks

PR #90 at a4b9b3a267e526f2b33ffd43c3b60d58be2aed5d develops a ternary-precision
lower bound on diagram CLOCK length for its different rank
(2n+1)^2/3^v3(2n+1). The new theorem concerns the MAXIMUM RANK on EVERY diagram
for this packet's moving-envelope rank, and uses a different inverse-ray
obstruction. Neither result is silently imported or used to certify the other.

The independent verifier checks45 CRT sources (H=2,...,16 and three upward
lifts),855 path positions and405 inverse-ray entries. These finite checks
validate arithmetic interfaces; Sections 1-2 are the all-parameter proofs.
No universal convergence or proof of the full merging cover follows from the
finite range. The earlier SC and cycle targets remain open and unchanged.
