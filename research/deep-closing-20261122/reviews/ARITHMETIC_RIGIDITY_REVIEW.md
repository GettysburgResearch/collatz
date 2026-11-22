# Independent review: the long-two-run permutation claim

Date: 2026-11-22. Author: `deep_arithmetic`; reviewer: `deep_cycles`.
Reviewed `collatz_work/deep_arithmetic/ARITHMETIC_ATTACK.md`, SHA256
`aebf19e35c498d4d318af7c45bce49d457bac33ba149be9f81344707a68cc520`.

**Verdict: VERIFIED for Theorem A, its negative-shadow application, and
the displayed finite replacement certificate.** The new termination
literature and the upstream joint-counterquery reductions were not
independently audited in this review.

Write y=z-1. The inverse maps for gaps 1,2,3 act by

\[
y\mapsto(2/3)y-2/3,\quad
y\mapsto(4/3)y,\quad
y\mapsto(8/3)y+4/3.
\]

Set R=4/3. A word with one 1, one 3 and all remaining entries 2 has
total shifted slope R^N. Compose in the inverse-word order, so a
correction at position j is multiplied by the slopes at positions
strictly before j. If the 3 precedes the 1, the two corrections are
R^(i+1) and -R^(j+1). If the 1 precedes the 3, they are
-R^(j+1)/2 and R^(i+1)/2. This reconstructs both formulas in the
source without assuming any intermediate integer legality.

For b=1+max(i,j), the coefficient of the highest R power has a
numerator prime to3 after the denominator3^b is cleared. Every other
term is divisible by3. In the half-difference case the numerator is
still an integer because all powers of4 involved are even, and
division by2 cannot introduce or remove a factor3. Thus the exact
reduced denominator is3^b in both cases.

The original correction is R-R^4=-148/81, whose reduced denominator
is3^4. Corrections differing by an integer must have the same reduced
denominator. Therefore the later exceptional position is exactly3.
There are six placements remaining, independently of the number of
trailing twos. An independent exact Fraction calculation gave

\[
0,\quad4/9,\quad28/27,\quad74/27,\quad68/27,\quad20/9.
\]

Only the first difference is integral. It is the original placement.
This proves the all-length theorem and the stated application to a
prefix [3,2,2,1,2] followed by any number of additional twos.

I also replayed the separate proposed replacement source219565229
using every displayed gap. At each step3x+1 is divisible by the
specified2^a and its quotient is odd, so the valuation is exact.
The41-step word ends at1 and has counts
{1:6,2:20,3:13,4:2}. Its powered source439130458 exceeds235398836.
The high grade comparison uses the displayed two versus five copies
of gap4, with no larger gap. This finite certificate does not assert
an all-parameter source replacement or a source-maximality theorem.

No prior Lean compilation was repeated or relabeled. The all-length
permutation argument is written mathematics; the finite rational and
ordinary calculations are controls for the stated formulas.
