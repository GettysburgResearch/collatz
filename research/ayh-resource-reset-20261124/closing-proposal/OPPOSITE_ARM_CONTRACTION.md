# Ordinary contraction on the last Mersenne offset

**Written theorem with an exact finite replay.** For the rank-three family
\(z=(2^{a+9}-527)/81\), \(a=98+162t\), the first nonbasin Mersenne
index of a least reverse defect could only be \(j=a-1=97+162t\) after
the forty affine returns and the even-index merger. Of the 59,049 residue
classes of \(t\) modulo \(3^{10}\), the certificates here exclude 1,000
from that possibility. Among these, 616 use an actual power of two on the
opposite arm and 384 instead use an ordinary contraction toward the positive
cycle. The other **58,049** classes have no certificate in this list.
The conclusion assumes the written bounded return of a reverse defect at
height at most \(2^{40}n\) from each positive nonbasin \(n\). This is one
upper-rank-three family. The all-rank Collatz implication remains open.

## Why a positive shadow can certify a genuine query

Put \(M_j=2^j-1\), so \(81z=1024\cdot2^j-527\). Each row specifies
integers \(d,t_0,E,m\) with \(t=t_0\pmod{3^{d-4}}\). Define
\[
 p=E+d,\qquad w=(2^{j+p}-m)/3^d,\qquad x=-m/3^d.
\]
The replay checks the congruence \(2^{j+p}-m=17\cdot3^d\pmod{48\cdot3^d}\)
at the initial exponent, and the exact order-divisibility needed for every
successive exponent in the class. It also checks positivity and \(w<z\).
In fact \(81\cdot2^p<1024\cdot3^d\) with integer slack, and
\(2^{97}>527\cdot3^d\).

At an odd-denominator rational use the parity of its numerator in reduced
form. Through any prefix of length \(h\le j+p\), the shadow and the ordinary
source have the same parity word. At each clock their signed difference
is multiplied by \(1/2\) or \(3/2\) on that common branch, so an unspent
factor of two guarantees the next parity agrees. The shadows are invoked
only to compute this finite word for each actual positive input.

If \(T^h x=-1\) with \(o\ge d\) odd inputs and \(h-o=E\), then exactly
\[
 T^h w=3^{o-d}2^{j-(o-d)}-1=T^{o-d}(M_j).
\]
The final equality follows by taking successive odd steps on \(2^j-1\).
This puts \(w\) outside the basin under the first-bad hypothesis.

On the opposite arm, let \(T^H(3x)=c\in\{0,1\}\) with \(O\) odd inputs.
Then the actual positive value is
\[
 T^H(3w)=3^{O+1-d}2^{j+p-H}+c.
\]
For the recorded \(c=0\) rows one has \(O+1=d\), so the triple reaches 1.
For \(c=1\), let \(b=3^{O+1-d}\). After \(k\) further pairs of clocks the
actual triple is at \(n=b3^k2^{j+p-H-2k}+1\), provided the displayed binary
exponent is nonnegative. This uses \(T^2(4v+1)=3v+1\) on positive indices.
Choose \(k\) so \(2^{40}\cdot81b2^{p-H}(3/4)^k<512\), then verify that
there are enough binary digits at the smallest exponent of the class. Since
\(512\cdot2^j>81\cdot2^{40}+527\), the actual endpoint obeys \(2^{40}n<z\).
If \(n\) were outside the basin, the quantitative return would give a
reverse defect strictly below \(z\). Thus \(3w\) belongs to the basin in
both cases, making \(w<z\) itself a reverse defect. This contradicts leastness.

## One complete positive-cycle family

Take \(t=181\pmod{2187}\), so \(j=29419\pmod{354294}\). Put
\(w=(2^{j+21}-3170149)/177147\). The shadow of \(w\) reaches \(-1\) in
21 clocks with 11 odd inputs. The shadow of \(3w\) reaches \(+1\) in
24 clocks with 10 odd inputs. The actual endpoints are therefore
\(M_j\) and \(2^{j-3}+1\), respectively. One hundred odd-even pairs send
the latter to \(3^{100}2^{j-203}+1\). The numerical comparison
\(81\cdot2^{40}3^{100}<512\cdot8\cdot4^{100}\) gives the required strict
contraction. The exponent is at least 29,419 throughout this class.

## Scope of the finite record

`OppositeArmQueries.json` contains 214 disjoint certificates. The counts
of new whole residue classes at depths 10 through 14, measured at their own
moduli, are 2, 13, 15, 84 and 100. Their lifts to the common modulus give
\(2\cdot81+13\cdot27+15\cdot9+84\cdot3+100=1000\). The checker verifies
the literal congruence, shadow trajectories, binary budget, height, and
disjointness. It makes no completeness or impossibility claim about any
other query. Run `python -B check_opposite_arm_queries.py` in this directory.

`MersenneParity.lean` separately proves the exact ordinary meeting between
an even-index Mersenne start and its immediate predecessor, the basin
equivalence, and the bridge to the pinned `Hits` predicate. `OppositeArm.lean` separately proves the congruence lifting, exact two-arm
clocks and strict height for the entire family \(t=181\pmod{2187}\). In particular
`CollatzOppositeArm.family_query` supplies ordinary query witnesses for every
nonnegative progression index. The full 214-family census and the leastness
consumer have written proofs with exact integer/fraction replay. The existing PR146 file `MERSENNE_EXPONENT_DESCENT.md` constructs
arbitrarily long post-ascent deadlines at which no earlier shifted ternary
power meets a supplied one. Its construction also fits this residual
exponent row because \(v_2(3^{162}-1)=3\). Its deadline does not preclude
later ordinary meetings or the directed shorter-source queries used here.
