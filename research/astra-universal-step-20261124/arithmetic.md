# Testing every shorter inverse clock at a fixed source

**No unrestricted descent proof resulted.** I tested whether the complete inverse minimum forces the repeated block needed by the ordinary Green estimate. The finite arithmetic below identifies which data the minimum actually reads. It supplies neither a forced repeated block nor a bound for the contribution of the remaining words. The argument concerns an escaping component. It does not exclude a positive cycle.

Assume an escaping component and use its real corrected height from the pinned PR193 section proof. For each ordinary odd source whose forward orbit enters the component, the same correction is defined by a convergent product. It satisfies \(H(x)>x\) and \(H(Ux)=3H(x)/2^{e(x)}\), with \(U(x)=(3x+1)/2^{e(x)}\). Choose the smallest ordinary integer \(m\) among all the component's minimizers of \(H\), including odd multiples of three. Such a minimum is attained because every sublevel is finite. Put \(y_j=U^j(m)\), write \(E_j\) for its cumulative odd clock, and set \(\alpha=\log_2 3\). [PR193, section proof](https://github.com/GettysburgResearch/collatz/blob/a1379492dbaae85e0d16662b41ccc7176ab3c66e/research/astra-global-synthesis-20261124/section/proof.md).

For any positive odd endpoint \(y\) and a competing gap word of length \(h\) and cost \(F\), reverse the steps as \(x\mapsto(2^e x-1)/3\). Admissibility depends only on \(y\bmod 3^h\). Indeed the forward word has affine form \(2^F y=3^h x+C\), and the congruence modulo \(3^h\) forces integrality at each reverse step, by successively reducing modulo three. Each integral predecessor of a positive odd state is again positive and odd. The converse follows from the affine identity. There is no terminal unit guard on the *origin* of the competitor. Write \(V_h(y)\) for the least admissible cost, assigning infinity when no word exists and \(V_0=0\).

Every finite-cost competitor at \(y_j\) has height relative to \(m\) given by \(2^{F-E_j}3^{j-h}\). Hence for every \(h\ge0\),
\[
 V_h(y_j)\ \ge\ \lceil E_j+\alpha(h-j)\rceil .
\]
In particular \(V_j(y_j)=E_j\). Among words attaining this cost the actual word maximizes \(C\), since at that cost all ordinary origins have height \(H(m)\) and \(x=(2^{E_j}y_j-C)/3^j\). Equality of both cost and carry gives the same origin and hence the same actual word by determinism.

The same-depth optimization can therefore be performed without sampling an endpoint. Starting from residue zero modulo one, a chronological extension by gap \(e\) sends \(r\bmod3^h\) to \((3r+1)2^{-e}\bmod3^{h+1}\). At each residue keep the least cost and, among ties, the largest carry. This pruning is exact: an extension raises all parent costs by the same \(e\), and updates its carry from \(C\) to \(3C+2^F\). At a specified finite cost bound there are only finitely many extensions to test. This yields a unique canonical word for an attained optimal residue. It gives a different optimization problem at each depth. No theorem here bounds the factor complexity or the return of a prefix along an infinite canonical ray.

For an actual prefix of length \(j\), even the comparisons with all horizons \(h\le j\) see only this word: the endpoint residue for each such horizon follows by reducing \(C2^{-E_j}\) modulo \(3^h\). For \(h=j+d>j\), the required residue is instead \((C+3^j m)2^{-E_j}\bmod3^{j+d}\), and therefore also reads the fixed source modulo \(3^d\). A computation that independently changes those higher digits as \(j\) grows cannot establish the longer-horizon tests for an ordinary source.

I found no argument that forces one of these inequalities to fail for some prefix of the same ordinary \(m\). In particular, unique canonical decoding at a given ternary residue does not imply that the words at successive moving residues have a repeated block. The power-word Green estimate supplies an upper bound after a qualifying repetition has been located. The missing step is an ordinary-source estimate on the histories left outside that bound, or an actual cheaper admissible inverse word at one of the moving endpoints. This calculation is a written audit. No Lean result is claimed here.

## A fixed ordinary source cannot supply arbitrarily long matching pairs

Use the binary shortcut \(T(n)=n/2\) on evens and \((3n+1)/2\) on odds. Consider consecutive actual blocks of the same positive length \(h\) and same odd count \(v\), with positive start \(x\), midpoint \(z\), and endpoint \(y\ne z\). Put \(P=3^v, Q=2^h\), and denote the chronological carries by \(C_1,C_2\). If \(C_1\equiv C_2\pmod P\), then
\[
                      (4/3)^v < x+1,\qquad h<7\log_2(x+1).
\]

Indeed the two affine equations give \(Q(y-z)=P(z-x)+C_2-C_1\). Coprimality forces \(P\mid y-z\), hence \(P\le |y-z|<\max(y+1,z+1)\). An odd step multiplies the coordinate \(n+1\) by \(3/2\); an even step can only decrease it. Both \(y+1\) and \(z+1\) are therefore at most \((3/2)^{2v}(x+1)\). This proves the first strict inequality. On the first block an odd step multiplies the unshifted positive integer by at most two, and an even step divides by two, so \(1\le z\le 2^{2v-h}x\). Thus \(h\le 2v+\log_2 x\). Since \((4/3)^3>2\), the first bound gives \(v<3\log_2(x+1)\), proving the second. If \(v=0\) the congruence modulo one is automatic; the two actual all-even blocks require \(2^{2h}\mid x\), already bounding their lengths.

For a fixed positive origin \(b\) with a prefix flank of length \(a\) before the pair, \(x+1\le(3/2)^a(b+1)\). In particular if \(a\le h/25\), then
\[
                          h < (175/18)\log_2(b+1).
\]
This follows by substituting \(\log_2(x+1)\le a+\log_2(b+1)\) in the preceding bound. If the two checkpoints coincide, the midpoint is periodic, and all later states are on that cycle. Thus on any injective ordinary trajectory the covered pairs, even with the allowed short initial flank, have **bounded block length for this fixed origin**. The positive Green bound on those histories cannot capture arbitrarily long prefixes of the hypothetical escaping atom by forcing such a pair. It leaves other histories open.

The companion `arithmetic.lean` imports the literal shortcut histories from `descent.lean`. Lean 4.34.1 checked `odd_growth` and `matching_separation` with warnings as errors. The displayed logarithmic bounds follow by the written inequalities above.
