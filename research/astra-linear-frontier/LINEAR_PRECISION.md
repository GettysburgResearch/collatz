# ALF-001–003: linear inverse precision and an output-sensitive finite search

**Status: PROPOSED; independent mathematical review pending.** These are claims
about exact ordinary finite paths. They are not a proof of Collatz. The starting
repository is `69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a`.

## 1. Definitions and credited interface

Use the shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n. Put

    H = {n>=1 : n=1 mod3},
    h(n)=v3(2n+1),   u(n)=(2n+1)/3^h(n),
    P(n)=(2n+1)^2/3^h(n).

For positive n, P is an injective positive integer rank, with P(n)>=2n+1.
Indeed P=3^h u^2, where u is a positive 3-unit. Its valuation recovers h and
its remaining square recovers u. P(1)=3. Absorb at1. For n>1 in H, R is the
first positive-time return to H, including arrival at1.

If 4 divides n, R(n)=n/4 with word00. Otherwise let m=n for odd n and m=n/2
for even n, and a=v2(m+1). Then

    R(n)=(3^a (m+1)/2^a-1)/2,

with word 1^a0 or 01^a0. Each such return is finite without assuming eventual
convergence. Every return has at most two even shortcut steps.

For y>1 in H, the complete inverse fan consists of

    s_j=2^(j+1)3^(h-j)u-2,  0<=j<h,
    z=2^h u-1, included exactly when z=1 mod3.

The respective words are 01^j0 and 1^h0. The same formula enumerates signed
first-return ancestors in {y<=-2:y=1 mod3}. Starting backward at2y, take an
even preimage to exit into the section or the odd preimage to continue in
residue2. A terminal residue0 branch has no later section exit. This proves
completeness. Every positive predecessor is at most4y; every negative one has
absolute value at most4|y|.

These interfaces and the finite inverse shield below come from PR91 and PR90:
`research/astra-critical-mass/INVERSE_SHADOW_FRONTIER.md`, L-AS7-001 and
T-AS7-002/003, blob `ac38112f418b35250e610b42941c75c55a033544`, resident unchanged
at the frozen main. The new contribution starts with the improved precision
bound. No charged-transfer or external predecessor theorem is used.

## 2. ALF-001 — a negative-path product bound

Let C_r be the complete inverse section ball of radius r around the actual
negative integer -2, including its root. For v in C_r, let w_v be its
source-to-root word, with k shortcut steps, q odd steps, and e=k-q even steps.
Let H_v=v3(2v+1), and define

    B_r=1+max_{v in C_r}(q+H_v).

No negative convergence assumption is involved: every enumerated vertex
already has its displayed finite path to -2. That path cannot repeat a state:
a repeat would force a cycle through -2, whereas -2 maps to the fixed point -1.
In particular its q odd absolute values are distinct odd integers at least3.
If ordered increasingly as a_i, they satisfy a_i>=2i+1.

For q>=0 the exact magnitude product is

    2=|v|(3/2)^q 2^(-e) product_i (1-1/(3a_i)).                 (1)

The correction product satisfies

    product_i (1-1/(3a_i)) >= (q+1)^(-1/5).                    (2)

To prove this without decimal estimates, for every integer i>=1 expand

    (6i+2)^5(i+1)-(6i+3)^5 i
      =1296i^5+2160i^4+1800i^3+930i^2+269i+32 >0.

Thus ((6i+2)/(6i+3))^5>i/(i+1). Multiply and use a_i>=2i+1.
At q=0 both products are empty and equal1.

Since e<=2r and |v|>=3^H_v/2, (1)–(2) imply

    3^H_v (3/2)^q <=4*4^r(q+1)^(1/5).

Writing m=q+H_v, we have H_v>=1, q+1<=m, and hence

    (3/2)^(5m) <=32m*4^(5r).                                  (3)

The proof retains the affine correction; it does not replace negative
trajectories by purely multiplicative ones.

## 3. ALF-002 — the precision budget has linear order

For every integer r>=0,

    floor(r/3)+2 <= B_r <=4r+2.                                (4)

For the upper bound, (3) contradicts m>=4r+2 when r>=2. At r=2 the requisite
strict comparison is

    (3/2)^50 >320*4^10.

On replacing r by r+1, the ratio of the left side to the right side at
m=4r+2 is multiplied by

    (81/64)^5 (4r+2)/(4r+6) >1,

because the last fraction is at least5/7 and 5*81^5>7*64^5. For fixed r,
(3/2)^(5m)/m increases for m>=1. Therefore m<=4r+1, proving B_r<=4r+2.
The cases r=0,1 follow directly from C_0={-2}, C_1={-2,-8}, both with B=2.

For the lower bound, construct an infinite backward sequence of actual
negative integers, beginning at -2. At a section state y=1 mod9, use
x=(4y-1)/3 with word10. Otherwise use x=4y with word00. The first choice is
an odd section source; the second is always a section source. Multiplication
by4 cycles the section residues modulo9 as 1,4,7,1. Therefore there is at
least one odd inverse edge in every three returns. At radius r the constructed
vertex has q>=floor(r/3), while H_v>=1. This proves the lower bound.

Consequently B_r=Theta(r). No optimal leading constant is claimed. Combining
(3) with m<=4r+1 also gives the optional refinement

    B_r <= [log4/log(3/2)] r + O(log(r+1)).

This supersedes only the quadratic *upper estimate* in L-AS7-001. It neither
rejects that older estimate nor changes its exact negative-tree definition.

## 4. ALF-003 — lossless linear-frontier search

At a node y with D>=1 inverse returns remaining, retain the even exits whose
remaining ternary gap d=h(y)-j satisfies

    1<=d<4D-2,

and the terminal odd exit, when it exists. Include y itself in the candidate
minimum; recurse with D-1 returns. The algorithm returns exactly the minimum
P in the complete inverse ball, not merely a minimum among selected examples.

Here is the finite shield that justifies deletion. For the even exit
s_j=2^(j+1)3^d u-2, if d>=B_r, its entire inverse ball of radius r is in
word-preserving bijection with C_r via

    x_v=2^(k+j+1)3^(d-q)u+v.                                  (5)

The condition d>=q+H_v+1 preserves both the exact ternary depth and its unit
modulo3 at each node. Those two data determine every child of the full fan.
Thus the correspondence is complete, not just an inclusion. The estimate
|v|<=2^(k-q+1), obtained from literal inverse negative steps, gives

    P(x_v)/P(y)
      >(64/9)4^k(4/3)^j 3^(d-2q-H_v)
      >=(64/3)(4^k/3^q)(4/3)^j >=64/3.                       (6)

In deriving (6), the shifted main term dominates |2v+1| by more than three.
All matched positive vertices are physical positive integers.

For r=D-1, (4) gives B_r<=4D-2. Every deleted subtree therefore has rank
strictly larger than its parent. Since that parent is already a candidate,
no deletion changes the minimum. Induction proves the claimed exactness.
This is the original finite shield with a new proved upper budget, not an
unjustified permanent deletion of interior branches.

There are at most4D-2 retained successors at a node with D remaining. Generate
only these gaps directly; do not first form all h(y) exits. The resulting tree
has at most

    1+sum_{t=1}^D product_{i=0}^{t-1}(4(D-i)-2)
      <=2*4^D*D!                                               (7)

nodes. This improves the previous generic factorial-squared bound, not a
polynomial-in-D bound. One can use the minimum of this budget, the old
quadratic budget, and any exactly computed B_r. The linear upper budget is
not claimed smaller at every small D.

### Sizes and shortcut clocks

If R^d(x)=y, d<=D, with q odd and e even shortcut steps, positivity of the
affine correction gives

    y>=x(3/2)^q 2^(-e),    e<=2d.

Hence

    q<= [log y+2D log2]/log(3/2),
    k=q+e <= log y/log(3/2)+[2+2log2/log(3/2)]D.                 (8)

Also x<=4^D y. Intermediate shortcut states are at most2*4^D y: the peak of
an odd run is twice its following section endpoint. Thus the integer bit
lengths are O(log y+D). This gives a fixed-parameter finite inverse procedure
with parameter D; it is not a source-independent shortcut-clock bound.

For a two-sided box 0<=r,s<=D, enumerate R^r(n), r=0,...,D, stopping at1, and
compute each inverse minimum at radius D. This covers precisely all section
witnesses R^r(n)=R^s(x) in that box. Each fixed box terminates. A proof that
some box succeeds for every n is a different statement and is NOT obtained.
The next file gives an obstruction to every fixed box, together with a
positive repayment construction and a different rank that descends immediately.
