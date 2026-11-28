# A rational arithmetic gap for finite inverse windows

For a positive-gap word write
\(A_e(x)=(1+3x)/2^e\) and
\(A_w=A_{e_1}\circ\cdots\circ A_{e_k}\).
The [Lean kernel](NegativeAffineGap.lean) uses exactly the rational slope
and offset of the earlier [finite transporter](../phase7/FINITE_AFFINE_TRANSPORTER.md).
Its value is \(A_w(-1)\), including the empty word.

Induction gives the exhaustive coarse alternative
\[
 A_w(-1)=-1,\qquad A_w(-1)=-1/2,\qquad\text{or}\quad A_w(-1)\ge-1/4.
\]
If the last alternative holds, one further outer positive-gap map has
strictly positive value. Thus no word image lies in the open interval
\((-1/2,-1/4)\). If only the **first** gap is at most \(R\), every negative
word value is at most \(-2^{-(R+1)}\); in particular it cannot equal
\(-2^{-k}\) for \(k\ge R+2\). The remaining gaps need no upper bound.

A second formal statement supplies the positive witness used by the
[finite-window strict improvement theorem](../machinery/phase9/STRICT_WINDOW_IMPROVEMENT.md).
For \(0<z<2^{-(R+2)}\) and \(e\le R\),
\[
 -1/3<(2^ez-1)/3<-1/4.
\]
Consequently the first capped inverse step lands where no finite
positive-gap forward word can come from \(-1\). Any later legal inverse
sequence therefore avoids \(-1\). This exact rational exclusion is
independent of a finite census or a conjecture about negative Collatz
orbits. Ternary legality, the construction of such a witness in every
source class, and the finite MDP block argument are separately written
and checked in the linked theorem.
