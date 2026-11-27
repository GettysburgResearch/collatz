# A fourth rank difference can reverse sign within every finite physical window

**Proposed obstruction to a local proof.** PR201's second-difference elimination uses several adjacent rank labels, their shared mechanical calendar, exact odd exponents, and the common finite past. The next two difference orders permit a distinct outcome even when all lower differences are strictly positive. This matters because positivity of sufficiently high rank differences would combine with [the complete-denominator bound](POLYNOMIAL_RANK.md) to exclude large bounded-branch integer cycles. The following construction uses ordinary integers throughout each padded path. Membership of all the paths in one closed orbit remains an additional condition.

## Two finite words of lowbit tags

At a date take \(m+1\) fundamental scaled labels \(Z_i=c_i x_i\), with each \(x_i\) odd and \(c_i\in\{1,2,4\}\). A mechanical letter \(b\) acts by
\[
                  2^b Z'_i=3Z_i+c_i,\qquad
                  2^{a_i}=2^b c'_i/c_i\in\{2,4\}.
\]
Every \(x_i\to x'_i\) is then an actual binary odd edge \(2^{a_i}x'_i=3x_i+1\). Write \(w_i=(-1)^{m-i}\binom{m}{i}\), \(H=\sum_i w_i Z_i\). The transport of the signed difference is \(2^b H'=3H+\sum_i w_i c_i\).

Use the slope \(\gamma=\log_2 3\), phase \(\phi=1/6\), and letter \(b_j=\lfloor\phi+(j+1)\gamma\rfloor-\lfloor\phi+j\gamma\rfloor\). Each displayed row gives its date's tag tuple and \(H_j\). The calendar column acts from this row to the next. Juxtaposed digits in a tag tuple are separate coordinates.

| Date | \(b_j\) | Third-order tags | \(\Delta^3 Z\) | Fourth-order tags | \(\Delta^4 Z\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 2222 | 0 | 22222 | 0 |
| 1 | 2 | 2244 | 0 | 24442 | 0 |
| 2 | 1 | 1224 | -1 | 22221 | -1 |
| 3 | 2 | 2424 | 0 | 42422 | -2 |
| 4 | 2 | 2224 | 2 | 42222 | 2 |
| 5 | 1 | 1122 | 2 | 22122 | 2 |
| 6 | 2 | 2242 | 2 | 22222 | 0 |
| 7 | — | 2222 | 0 | 22222 | 0 |

In the fourth-order column there are six essential transitions. The seventh is a constant extension. The rank grade cap is respected: a tag one occurs solely at a date with \(b_j=1\). Direct substitution checks the signed equation and every exponent in both arrays. The fourth difference goes directly from \(-2\) to \(+2\). Reversing the spatial order in the third-order gadget reverses all its third differences, with the same native tag rules.

## Arbitrary calendar depth, true ordinates and strict lower differences

**Theorem 2.** For either displayed order \(m\), prepend and append arbitrarily many mechanical letters, using the constant tag two at every new site. There are \(m+1\) parallel trajectories of distinct positive ordinary odd phases which realize the entire padded array. At each date the \(m+1\) scaled labels have all their consecutive differences of orders \(1,\ldots,m-1\) strictly positive. They realize the displayed \(m\)-th carry, and its value is zero throughout each padded tail. The minimum of all physical phases may be made arbitrarily large, with all phases in one band of ratio strictly below \(16/3\).

The same padded calendar and physical tag mask occur at \(m+1\) neighboring ranks for all sufficiently accurate rational approximations \(h/p\to\gamma\) from above with \(p\to\infty\), taking the initial rank \(\lfloor p/6\rfloor\). Indeed, none of the finitely many fractional phases \(\{\phi+j\gamma\}\) is zero: irrationality handles \(j\ne0\), and the initial value is \(1/6\). Also the grade cutoff \(\{\phi+j\gamma\}=2-\gamma\) would force the next fractional phase to be zero. Thus all the finitely many strict calendar and grade choices are stable, including the \(m\) neighboring mesh offsets. Coprime approximations exist, for instance by taking \(p\) prime and \(h=\lceil p\gamma\rceil\). This finite calendar observation does not impose the global height/clock relation required of an entire cycle.

**Proof of ordinary realization.** Write \(n\) for the total number of padded edges and \(B\) for the mechanical clock of those edges. Both boundary tag tuples are constant two, so each of the \(m+1\) native words also has total clock \(B\). For column \(i\) its actual affine law has a positive integer carry \(K_i\):
\[
                    2^B x_{n,i}=3^n x_{0,i}+K_i.
\]
Unrolling the *scaled* signed equation with \(H_0=H_n=0\) gives \(\sum_i w_iK_i=0\). Indeed the scaled carry of column \(i\) equals \(2K_i\) because both of its boundary tags equal two.

Let \(M=3\cdot2^{B+1}\). For each \(i\), first choose a source residue \(r_i\bmod M\) with \(r_i\equiv1\bmod3\) and \(3^n r_i+K_i\equiv 2^B\bmod 2^{B+1}\). This last congruence gives the exact finite native word: the terminal quotient is odd, and reducing the successive affine equations shows every intervening division has its prescribed odd quotient. Equivalently one may read the word backwards from that odd terminal symbol in the parity cylinder. Summing the congruences with coefficients \(w_i\), using \(\sum w_i=0\), gives \(M\mid\sum_i w_i r_i\). Because \(w_m=1\), subtract that sum from the last chosen representative. The resulting lifts have \(\sum_iw_i r_i=0\) exactly.

Now replace these signed representatives by
\[
               x_{0,i}=r_i+M\bigl(A+C(1+i)^{m-1}\bigr).
\]
Their \(m\)-th difference is still zero. The native residues and every prescribed lowbit persist. At date \(j\), in scaled labels the addition has become the common positive multiplier \(2M\,3^j/2^{B_j}\) times the same polynomial, where \(B_j\) is the elapsed mechanical clock from the earliest date. All consecutive forward differences of \((1+i)^{m-1}\) of orders one through \(m-1\) are positive on these indices, by the binomial theorem or positive finite differences of monomials at positive integers. With finitely many dates and slots, choosing \(C\) sufficiently large gives the asserted strict lower differences everywhere. Choosing \(A\) sufficiently large then gives positive odd ordinates on every edge and any chosen floor. Signed transport gives exactly the tabulated \(H\).

At each fixed date as \(A\) grows the odd phases divided by one common global scale converge to \(2^{\{\phi+j\gamma\}}/c_{j,i}\), since \(3^j/2^{B_j}\) is the ratio of the corresponding ideal phase powers of two. The normalized target exceeds \(1/4\). It is below \(4/3\): if \(c=1\), its allowed letter one gives \(\{\phi+j\gamma\}<2-\gamma\); if \(c\ge2\), it is below one. A common strict ratio below \(16/3\) follows by finiteness. Different dates have distinct limiting normalized odd ordinates up to dyadic tags, because their fractional phases differ by a noninteger. At a common date different tags also separate, and for equal tags strict first differences ensure actual distinctness. Thus all physical odd states are distinct.

**What this rules out.** Every specified finite number of reverse and forward tests about these five columns can coexist with the direct fourth-order sign reversal, including exact odd integrality, an arbitrarily high ordinary floor, the physical band, and positive first through third spatial differences. The columns are separate trajectories with separately chosen initial residues coupled by one exact signed relation. No common closed cycle has been supplied. A global argument using chronological connections among the neighboring ranks, additional ranks, or a quantitative restriction on the true minimum as a function of the calendar can still distinguish them. This obstruction does not establish sign reversal on any positive integer cycle.

[PR201, strict second difference](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md)

[The exact replay](check_higher_differences.py) constructs signed source congruences and checks every native transition of ten ordinary fixtures, including 511 past and 257 future padding dates on each order. Its largest fourth-order fixture contains 3,875 distinct odd states with a 2,461-bit minimum. [Recorded output](higher_difference_controls.json). These are finite integer controls for the symbolic arbitrary-padding proof.

## Matching the real rank profile at the same local signs

There is a stronger choice of the integer lifts. Fix the padding, let \(h/p\to\gamma\), \(p\to\infty\), and let the desired positive real minimum parameter \(s\to\infty\). Write \(\delta=|h/p-\gamma|\). For all sufficiently large \(p\), throughout these same ordinary columns one can impose
\[
 \left|Z_{t,i}-4s\,2^{(r_t+i)/p}\right|
       \le C_{\rm pad}\left(1+\frac{s}{p^m}+s\delta\right)
\]
at every specified local rank \(r_t+i\). If \(s\delta=O(1)\) and \(s\le p^{3+o(1)}\), the right side on the fourth-order counterexample is \(O_{\rm pad}(1)\). The two parameter bounds here are conditional estimates on supplied clock and scale pairs; this assertion does not produce a growing sequence of clocks satisfying every necessary cycle condition.

To prove the bound, let \(r_0\) be the rotation rank at the earliest padded date. After taking \(p\) large there is no wrap within a spatial tuple. Use the CRT representatives \(u_i\) in the preceding proof with \(\Delta^m u_0=0\). Therefore on these \(m+1\) slots they are given by an integer-valued polynomial with Newton coefficients \(u^{(\ell)}=\Delta^\ell u_0\), \(0\le\ell<m\). Each coefficient can be changed independently by a multiple of \(M\), preserving all the native source congruences and \(\Delta^m u_0=0\). Put \(Y=2s\,2^{r_0/p}\), \(\tau=2^{1/p}\). The Newton coefficients of \(Y\tau^i\) are \(Y(\tau-1)^\ell\). For \(\ell\ge1\) take the smallest permitted coefficient at least \(Y(\tau-1)^\ell+K\), with a fixed \(K>0\) to be chosen. For the constant coefficient take the nearest permitted value to \(Y\). All coefficient errors are \(O_{\rm pad}(1+K)\). The omitted degree-\(m\) coefficient, needed only at the final spatial slot, has size \(O_m(s/p^m)\). The approximation at the earliest date follows.

All lower differences of the resulting Newton polynomial are at least \(K\) on their available slots, since forward differencing lowers the index of \(\binom{i}{\ell}\) and all its positive-degree coefficients are positive. At every later date these differences are multiplied by the same positive chronological slope, with additive errors bounded in terms of the fixed padding. A sufficiently large fixed \(K\) therefore keeps all lower differences strictly positive throughout, while preserving the displayed \(m\)-th difference.

In \(j\) edges of elapsed clock \(B_j\), the transported geometric profile has homogeneous multiplier \(2^{jh/p}/2^{B_j}\) by the actual rational rank rotation. The actual scaled coordinates have multiplier \(3^j/2^{B_j}\) and a carry bounded in terms of the padding. Replacing one multiplier by the other costs \(O_{\rm pad}(s\delta)\) on the profile, which proves the estimate. Its relative error tends to zero, so the floor, strict ratio and distinctness conclusions of Theorem 2 also hold for this choice. Equal-tag positions at a common date remain distinct by strict increase. No finite local comparison against this real rank profile can on its own eliminate the fourth-order transition.

[HigherDifference.lean](HigherDifference.lean) checks both signed transition tables, the native-edge identity, the last-slot congruence repair, and the vanishing differences of the two polynomial lifts. The calendar, arbitrary-padding construction and approximation estimates are proved in the text.
