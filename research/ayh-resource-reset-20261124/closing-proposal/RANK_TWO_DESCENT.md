# The least reverse defect has at least three odd moves on its convergent arm

Use the ordinary positive shortcut map. A reverse defect is a positive integer
\(z\equiv17\pmod {48}\) outside the basin of 1 whose triple lies in the basin.
The directed equivalence at commit
`7ad81ec56947146fac854d2586651ca0c934a536` gives a reverse defect if Collatz
fails. The least such integer therefore exists under failure.

**Proposition.** The least reverse defect cannot have a convergence certificate
for its triple with exactly two odd moves. In this residue the first two moves
on the triple are odd, so every convergence certificate for that triple must
use at least three odd moves.

## A bounded return for the smaller ordinary endpoint

For every positive nonbasin integer \(n\), the pinned directed descent produces
an actual reverse defect \(w\le 2^{40}n\). To obtain this constant, use the
26-leaf odd-source certificate in the pinned copy of PR146's `ReverseBasin.lean`.
An even source halves. In a certified positive odd batch the moves \(S_h\),
\(I_h\) and \(M\) increase height by factors at most \(4/2^h\), \(2^h/3\) and
\(3\), respectively. These follow directly from their affine formulas. The
maximal product over every prefix of all 26 literal words is \(16384/9\).
Each completed batch has a strictly smaller positive endpoint, so the same
bound applies along all batches with respect to the original \(n\). The
resulting finite path ends at 1. Before the first change from nonbasin to
basin, one encounters a directed tripling \(v\longrightarrow3v\) at an odd
multiple \(v=3u\). The two-successor exchange supplies a defect in the same
orientation at \(16u+1\) or \(32u+1\), both at most \(11v\). The directed
1-mod-16 to 11-mod-32 replacement costs the factor
\(574854143371/219537\). Passing from \(32t+11\) to \(48t+17\) costs less
than two. The product of these bounds is below \(2^{40}\).

## The ordinary descent at rank two

The first two steps send \(3z\) to \((27z+5)/4\). If these are the only odd
moves on a certificate to 1, then \(27z+5=4\cdot2^e\) for an integer
\(e\ge0\). For \(e<201\), the necessary congruence
\(4\cdot2^e\equiv464\pmod {1296}\) admits exactly \(e=39,93,147\).
The three resulting ordinary sources reach 1 in 168, 398 and 677 steps.

If \(e\ge201\), put \(c=2^{e-201}\). The source obeys
\(27z+5=32\cdot4^{99}c\) and \(z\equiv1\pmod {32}\).
Five steps give \(4^{99}c+1\). Each pair of steps sends \(4d+1\) to
\(3d+1\). After 198 further steps the source is at \(n=3^{99}c+1\).
The integer inequality
\[
  27\cdot2^{40}(3^{99}+1)+5<32\cdot4^{99}
\]
implies \(2^{40}n<z\) for every \(c\ge1\). If \(z\) were outside the basin,
then \(n\) would also be outside. The bounded return gives a reverse defect
\(w\le2^{40}n<z\), contradicting minimality.

The ordinary finite descent is `CollatzTwoOdd.two_odd_progress`. Its least
defect corollary takes the quantitative return above as an explicit argument.
The return's quantitative constant is justified by the pinned written directed
height certificate and an exact arithmetic replay. The original kernel
equivalence has no quantitative output.

## Scope of the rank argument

The family \(z_m=(2^{54m+41}-5)/27\) has an upper certificate containing
exactly two odd moves. Its lower orbit first reaches \(4^{27m+18}+1\) after
five steps, then reaches \(3^{27m+18}+1\) after \(27m+18\) odd-even pairs.
Before that endpoint it cannot have hit 1, since the later endpoint exceeds 2.
Thus any lower convergence certificate contains at least \(27m+21\) odd
moves, while the large-source cases above admit strict ordinary descent by the
factor needed for a new smaller reverse defect.

PR146 at `f431078244e868dc699fad011044f0d5e7f76437` already proves
rank-transfer obstructions for the opposite, binary one-sided implication and
contains Mersenne and shifted-power constructions. The present result uses the
actual reverse 17-mod-48 residue, a quantitative return to a genuine defect,
and explicit closure of its entire two-odd layer at the least witness.
No classification of certificates with three or more odd moves is established.
