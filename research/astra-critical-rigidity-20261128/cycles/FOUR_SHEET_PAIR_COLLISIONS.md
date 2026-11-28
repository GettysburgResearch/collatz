# One primitive rational cycle can have exact pair collisions at the four-width boundary

**Proposed written construction.** There are primitive positive rational Syracuse cycles of odd period \(p=4P\to\infty\), full native division sum \(A=4B\), and real odd width \(X/m\to4\), where \(B/P\) ranges over sufficiently large upper convergents to \(\gamma=\log_2 3\). On each cycle compare four actual phases, separated chronologically by complete \(P\)-step blocks. With the explicit integer tags below, their signed folded pair difference is an integer on all \(4P\) dates. At exactly eight dates it is zero. At the other dates it has both signs, and equals \(2\) or \(-2\) outside four additional dates. On each of the four sheets all but two reduced ranks have nonzero comparison. On every fixed open interval of reduced rank fractions both signs occur as \(P\to\infty\).

This tests whether a zero comparison near width four forces a macroscopic zero arc by the synchronized scalar recurrence, bounded signed height, true cyclic returns, and an actual common reduced denominator. All those properties hold here. The four phases occupy different sheets of the same reduced angle. Positive ordinary cycles at this width have only one sheet by the [residue-fiber order theorem](RESIDUE_FIBER_INVERSIONS.md). A comparison of four distinct short spatial offsets of that ordinary sheet has additional structure. The [two-grade pair theorem](TWO_GRADE_SIDON.md) applies at fixed widths strictly below four, and the [prior complete rational tetrad](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/TETRAD_RANK.md) gives a different, single-clock, wider-band reversal.

## Four real phases on one word

Put \(\rho=B/P\), \(f_t=\{t\rho\}\) and \(b_t=\lfloor(t+1)\rho\rfloor-\lfloor t\rho\rfloor\). For all large convergents, \(b_t\in\{1,2\}\), and a winding one is followed by a winding two. For a tuple \(C=(c_1,c_2,c_3,c_4)\) write \(d(C)=c_1+c_2-c_3-c_4\) and \(\pi C=(c_3,c_4,c_2,c_1)\). This four-cycle changes the sign of \(d\). Use the following regular tag tuple \(D_t\):
\[
   (2,2,4,2)\quad (b_t=1),\qquad
   (4,4,4,2)\quad (b_t=2,\ b_{t-1}=1),\qquad
   (4,2,2,2)\quad (b_t=b_{t-1}=2).
\]
It has \(3\cdot2+d(D_t)=2^{b_t}\cdot2\). Across each winding one, tags can only increase, as required for positive native valuations. Windings two between regular tuples allow both tag directions.

At each \(t=jP\) replace a seven-date neighborhood by \(\pi^j\) applied to the tuples in the table. Between this neighborhood and the next one use \(\pi^{j+1}D_t\). The displayed height \(H_t\) on the \(j\)-th neighborhood is multiplied by \((-1)^j\); between that neighborhood and the next it is \(2(-1)^{j+1}\).

| \(t-jP\) | \(b_t\) | Tag tuple before \(\pi^j\) | \(H_t\) before \((-1)^j\) |
|---:|---:|---|---:|
| \(-3\) | 1 | \(2,2,4,2\) | 2 |
| \(-2\) | 2 | \(4,4,4,2\) | 2 |
| \(-1\) | 2 | \(2,2,2,4\) | 2 |
| \(0\) | 1 | \(1,1,1,4\) | 1 |
| \(1\) | 2 | \(2,4,2,4\) | 0 |
| \(2\) | 1 | \(2,2,4,4\) | 0 |
| \(3\) | 2 | \(4,2,4,4\) | \(-2\) |

The letters follow directly from the floors at \(t=-3,\ldots,3\), also at \(t=0\) where the rank is exactly zero. The first tuple is \(D_{-3}\), and the last is \(\pi D_3\). Every column obeys \(b_t+\log_2 c_{t+1}-\log_2 c_t\ge1\), including the descent to tag one after a winding two. Direct substitution gives the exact scalar equation for the complete periodic tuples \(C_t\):
\[
                    2^{b_t}H_{t+1}=3H_t+d(C_t).                     \tag{1}
\]
The construction gives \(C_{t+P}=\pi C_t\) and period \(4P\).

Use just the first component \(\ell_t=(C_t)_1\). Its native exponent is \(a_t=b_t+\log_2\ell_{t+1}-\log_2\ell_t\). This cyclic word has total exponent \(4B\). Its unique affine fixed point gives a positive rational odd cycle \(x_t\), because \(2^{4B}>3^{4P}\). The native words are exact: their cyclic carry formula has odd raw denominator prime to three, and each rotated carry is odd, so all prescribed exponents are the true dyadic valuations. Reduction gives one common full denominator for all phases. A repetition factor of the word divides \(\gcd(4P,4B)=4\). Any nontrivial repetition would give period \(2P\). In that case \(\log_2\ell_{t+2P}-\log_2\ell_t\) would be constant by the native exponent formula and \(b_{t+2P}=b_t\), hence zero by cyclic iteration. At the four gates \(t=jP\), the first component takes the value four once and one three times. This rules out \(2P\)-periodicity and proves primitivity.

Define \(Z_t=\ell_t x_t\), so \(2^{b_t}Z_{t+1}=3Z_t+\ell_t\). In the four-column order used above, the actual tuple is \((Z_t,Z_{t+2P},Z_{t+P},Z_{t+3P})\); the first entries of \(C_t,\pi C_t,\pi^2 C_t,\pi^3 C_t\) are \(c_1,c_3,c_2,c_4\). Its signed difference satisfies (1). The difference between this physical register and the table has full-lap multiplier \(3^{4P}/2^{4B}<1\), so its periodic value is zero. This proves all asserted equality, sign, and integrality statements. The exact zeros lie at \(t=jP+1,jP+2\). On each other reduced rank outside the gates, two sheets have height \(2\) and two have height \(-2\).

Finally let \(V_t=2^{-f_t}Z_t\). Then \(2^\rho V_{t+1}=3V_t+2^{-f_t}\ell_t\), with added term between \(1/2\) and four. Iterating or applying the extremal bounds on the periodic circuit gives
\[
     \frac{1/2}{2^\rho-3}\le V_t\le\frac4{2^\rho-3},\qquad
     |V_{t+1}-V_t|\le 8 .
\]
Thus \(\max V_t/\min V_t=1+O(P(\rho-\gamma))=1+o(1)\). The scale \(x_t/V_t=2^{f_t}/\ell_t\) always belongs to \([1/4,1]\): tag one occurs only at \(f_t=0\), and the other tags are two or four. Both endpoints occur at gates, giving \(X/m\to4\). The order modulo the full denominator is exactly four for the multiplier \(3^P2^{-B}\), by the width-nine residue theorem. Nothing in this argument claims an ordinary positive integer cycle.

[Exact single-cycle checker](check_four_sheet_pair_collisions.py) · [Exact controls](four_sheet_pair_collision_controls.json)
