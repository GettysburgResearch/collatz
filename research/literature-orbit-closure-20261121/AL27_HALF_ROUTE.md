# A variable-clock smaller-source selector on half of the AL27 branch

**Status:** the parameterized arithmetic, ordinary merger, complete progressions,
and non-descent through the merger are proved in `lean/AL27HalfSelector.lean`.
The natural-density and overlap deductions below are written proofs with an
exact finite arithmetic replay. No universal convergence conclusion is claimed.

Use the ordinary shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n.
For every k,t>=0, put

\[
w_k=(28\,2^{5k+1}+9\,3^k)\bmod36,\quad w=w_k+36t,
\quad z=\left\lfloor\frac{2^kw}{9}\right\rfloor,
\]

\[
n=128z+27,\qquad x=2^{k+3}w-1.
\]

The theorem proves

\[
0<x<n,\qquad16x+3=9n,\qquad
T^{k+5}(x)=T^{k+9}(n),
\]

and simultaneously

\[
T^i(n)\ge n\qquad(0\le i\le k+9).
\]

Thus this is a smaller-source certificate even though the original orbit has
not descended at any clock through the displayed meeting point. The clocks
are unbounded. A source and its partner are ordinary positive integers; the
partner need not lie in the marked band or in this selected source family.
The final Lean induction theorem retains convergence of all smaller positive
sources as its hypothesis.

## Why starting the deletion earlier matters

For every source n=128z+27, three ordinary steps give

\[
m=T^3(n)=144z+31,\qquad m+1=16(9z+2).
\]

Write 9z+2=2^k w with w odd. Then m=2^{k+4}w-1 begins with k+4 odd steps.
The short endpoint diamond applies when

\[
3^{k+3}w\equiv3\pmod4.
\]

It gives the half-source partner x=(m-1)/2 and clocks k+5 and k+6 measured
from x and m respectively. Restoring the original three-step prefix gives
the clocks above. The original prefix expands n only by a leading factor
9/8, so halving its endpoint still leaves a partner with leading factor9/16
relative to n.

The CRT formula supplies both requirements with no hypothesis left over:

\[
w\equiv2^{5k+1}\pmod9,\qquad w\equiv3^k\pmod4.
\]

Since 2^6=1 mod9, the first gives 2^kw=2 mod9. The second gives the short
diamond phase. Both residues are odd, so w is positive and odd.

## No direct descent through the common endpoint

The first three states stay above n, and the following k+4 odd steps rise.
At the end of that odd run the source is

\[
S=3^{k+4}w-1,
\qquad9n=128\,2^kw-13.
\]

Since 729*3^k>=512*2^k,

\[
9(S-4n)=(729\,3^k-512\,2^k)w+43>0.
\]

The selected phase makes S divisible by four. Its next two halvings therefore
stay above n, including the common endpoint S/4. This proves the claimed
non-descent for every k,t, not just for sampled inputs.

## Exact natural density: one-half of the branch

For each k, the Lean progression and base theorems give

\[
n(k,t)=n(k,0)+2^{k+9}t,\qquad0<n(k,0)<2^{k+9}.
\]

The k-progressions are disjoint because k is the exact valuation of9z+2.
Relative to n=27 mod128, the kth progression has density2^{-(k+2)}.
Their sum is1/2. To justify natural density for the countable union, the tail
k>=K is contained in2^K dividing9z+2, whose relative density is2^{-K}.
This tail tends to zero, so finite partial sums determine the density.

The selector also exhausts the short-diamond phase within the branch: every
n=128z+27 satisfying3^{k+4}w=1 mod4, with9z+2=2^kw and w odd, has w in the
specified CRT progression. Its remaining half is not covered by this theorem.

## Exact overlap with the previous446 complete rays

A half-density theorem does not add288 new classes to the previous446.
The overlap is substantial and can be classified exactly.

On one old cell n=n0+73728t, the quantity m+1=T^3(n)+1 changes by
2^10*81*t. If its base valuation R is at most8, both R and the endpoint
phase modulo4 are fixed, so the whole cell is either selected or unselected.
If R>=9, exactly half the cell is selected. For R=9 the odd core alternates
modulo4; for larger R the same valuation partition and vanishing divisibility
tail apply.

Among the old130 unresolved cells,120 have a fixed unselected phase. These10
cells are now half selected:

1819,10011,22299,26395,34587,38683,46875,59163,63259,71451 (mod73728).

Consequently the union of the old446-ray certificate and this new selector
has relative natural density

\[
\frac{446+10/2}{576}=\frac{451}{576}
\]

inside the27mod128 branch. This is a density of smaller-source certificates,
not a density theorem for convergence to one. None of the old130 cells is
now wholly certified:120 remain wholly outside these two constructions and10
remain partly outside them.

`certificates/half_selector_overlap.py` checks the complete finite phase
classification and these exact rational counts. The original certificate is
unchanged; its130 unresolved entries retain their original, narrower scope.

## What the route still needs

The short endpoint phase gives a broad parameterized family with actual
source decrease and unbounded clocks. It does not provide a successful rule
for the complementary phase, and it does not show that the smaller partner
remains inside the selected family. A full proof still needs a complete
well-founded combination of physical rules or another universal argument.
