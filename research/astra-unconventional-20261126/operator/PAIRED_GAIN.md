# A synchronized strict descent on a positive ternary subprogression

**PROPOSED, with physical kernels verified in Lean.** Use \(T(2n)=n,\ T(2n+1)=3n+2\) on positive ordinary integers. For \(k\ge0\), fix any positive ordinary \(X\) satisfying
\[
             32768X\equiv17569\pmod{3^{k+8}}.
\]
Put \(u=(32768X-17569)/3^{k+8}\), a positive integer, and \(Y=2^{k+2}u-1\). Then
\[
 (T^{k+17}Y,\ T^{k+17}(3Y-1))=(X,3X-1)
\]
with exactly \(k+8\) odd departures on each arm. In particular
\[
       0<Y< {2^{k+17}\over3^{k+8}}X .
\]
This is strict descent for \(k\ge8\), and \(Y<X/2^{40}\) for \(k\ge76\). The time exceeds the per-arm odd count by exactly nine at every depth. Increasing \(k\) narrows the required class of \(X\). No fixed positive integer satisfies its congruence at every \(k\), since that would give \(32768X=17569\).

## O9. Physical opening and fixed suffix

Write \(v=3^k u\). The first two clocks on the lower arm and the next \(k\) are odd, taking \(Y\) to \(9v-1\). The upper arm starts at \(3Y-1=4(3\cdot2^k u-1)\). Two halvings and \(k\) odd departures take it to \(3v-1\). These statements use the elementary identity \(T^j(2^j w-1)=3^j w-1\) for positive \(w\). In the rank/carry model the first two bit pairs are \(10,10\), reaching \(r=-1,c=-2\), where \(11\) fixes the relative state.

The entry equation is now \(32768X=6561v+17569\). Equivalently \(v=13567+32768t,\ X=2717+6561t\), \(t\ge0\). At \(t=0\) the 15-clock suffix takes 122102 to 2717 in six odd departures, and 40700 to 8150 in eight. At arbitrary \(t\), the two source shifts are respectively \(2^{15}(9t)\) and \(2^{15}(3t)\). Their corresponding endpoint shifts are \(3^6(9t)=6561t\) and \(3^8(3t)=3\cdot6561t\). The actual parity decisions and both counts persist along the entire ordinary progression. The displayed height bound follows on substituting \(u\). Incrementing \(k\) multiplies its slope by \(2/3\).

All these targets have \(X\equiv8\bmod9\). Since the stride \(3^{k+8}\) is odd, one may additionally impose \(X\equiv2\bmod8\), giving infinitely many targets in the canonical class \(X\equiv26\bmod72\). This covers one subprogression of that class for each \(k\).

## Entrance from the hard Mersenne source

For the existing hard family \(m=11+162j\), \(z=(2^{m+7}-271)/81\), the initial value \(z\) is positive odd. One ordinary odd departure sends \((z,3z)\) to \((X,3X-1)\) with
\[
         X=(3z+1)/2=(2^{m+6}-122)/27 .
\]
The target condition above becomes
\[
       2^{m+21}\equiv32768\cdot122+27\cdot17569
                          \pmod{3^{k+11}}.
\]
Both sides are 130 modulo \(3^5\). Moreover \(v_3(2^{162}-1)=5\), by \(2^{162}=4^{81}\) and the binomial lifting identity. Powers of \(2^{162}\) therefore exhaust the principal-unit classes congruent to one modulo \(3^5\) at every higher precision. Exactly one class of \(j\bmod3^{k+6}\) works for any chosen \(k\). This establishes a true unbounded hard-family subprogression. Every upper hitting certificate for \(3z\) transfers to \(3Y-1\) with \(k+16\) additional clocks and \(k+7\) additional odds, by dropping the original first odd and prepending the new upper path.

One more ternary digit, \(3\mid u\), also gives a positive odd \(Z=(2Y-1)/3\). Then one odd departure on each arm sends \((Z,3Z)\) to \((Y,3Y-1)\), reaching the original two components. The comparison is in ordinary size. For \(k\ge1\) the new \(Z\) is \(-1\bmod16\); this refinement does not return \(Z\) to the original \(17\bmod48\) source class. The hard-family interpretation uses the sibling lane's chart and extends a prior all-odd identity. [Signed source and earlier stable bridge](../descent/SIGNED_MERSENNE.md).

**Formal scope.** [PairedGain.lean](PairedGain.lean) imports the sibling [Portal.lean](../descent/Portal.lean). The checked theorems give the explicit two-arm suffix, all-\(k\) physical transport for the positive linkage, the modulo-nine consequence, and the factor \(2^{40}\) height gain for \(k\ge76\). CRT and the hard-family index calculation above are written arithmetic. [Compiler and axiom output](../../../reports/astra-unconventional-20261126/operator/paired_gain_lean.txt).
