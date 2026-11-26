# A restriction on the third odd step of a least reverse defect

**Proposed written theorem.** Assume the same quantitative ordinary reverse return as in RANK_TWO_DESCENT.md. If a least reverse defect has a certificate for its triple with exactly three odd inputs, the number \(e\) of consecutive even inputs between the second and third odd inputs satisfies \(6\le e\le48\). The proof uses the actual lower ordinary trajectory and an exhaustive finite parity calculation. The rank-three restriction has not been formalized in Lean.

Let \(z=17\bmod48\) be the positive least reverse defect. After the two forced odd inputs its triple reaches \(A=(27z+5)/4\). Write \(A=2^e w\) with \(w\) positive and odd, and let \(b\) be the even tail after the third odd step. Then
\[
 (3w+1)/2=2^b, \qquad 81z+15+2^{e+2}=2^{e+b+3}.
\]
Here \(A=116+324t\), so \(e\ge2\). If \(e\ge201\), let \(c=A/2^{201}\). The rank-two packet's large-drop calculation applies to *every* positive \(c\) satisfying \(27z+5=32\cdot4^{99}c\). Thus its 203 ordinary steps give a nonbasin integer \(n\) with \(2^{40}n<z\), contradicting minimality by the quantitative return. This also proves \(v_2(A)\le200\) for a least reverse defect at any upper odd rank.

For each \(e\in\{2,3,4,5\}\cup[49,200]\), take the fixed rational
\[
 x_e=-(15+2^{e+2})/81.
\]
At a reduced rational of odd denominator, use the numerator's parity for the shortcut choice. Each next denominator remains odd. The integer \(z\) and this rational differ by \(2^{e+b+3}/81\). They have identical parity words through any length \(H\le e+b+3\): at the current common branch, the difference is multiplied by either \(1/2\) or \(3/2\), which consumes just one power of two. This is a finite congruence computation for the supplied ordinary source.

For each of the 156 exponents the deterministic checker finds a prefix of length \(H\le343\), with \(p\) odd inputs, for which \(2^{40}3^p<2^H\). If \(b\ge700\) the prefix is shared. Also \(81z\ge2^{703}-15-2^{202}>81\cdot2^{40}3^{343}\). The shared word has the standard integer identity \(2^H T^H(z)=3^p z+B_H\), where \(0\le B_H<3^H\). The bound follows inductively from the updates \(B_{j+1}=3^{\epsilon_j}B_j+\epsilon_j 2^j\), which give \(B_j\le3^j-2^j\). Since \(2^H-2^{40}3^p\) is a positive integer, \((2^H-2^{40}3^p)z\ge z>2^{40}B_H\). The genuine positive endpoint therefore satisfies \(2^{40}T^H(z)<z\). It is outside the basin, yielding the same contradiction.

For \(0\le b<700\) the checker enumerates all 156 exponent families and keeps every positive solution of the displayed identity with \(z=17\bmod48\). There are 675 such starts; direct integer iteration of each lower source reaches 1, with maximum first-hit time 5,619. Together these cases prove the claim. The supplied checker uses exact rationals for the finite parity data and integers throughout the ordinary orbit computation.

The first remaining value \(e=6\) illustrates what the argument leaves. For \(b=162m+9\), \(z=(2^{162m+18}-271)/81\) has residue 17 modulo 48: the base numerator is \(81\cdot3233\), and \(2^{162}=1\bmod243\) by Euler's theorem, while both large powers vanish modulo 16. The upper even tail begins at \(2^b\); the first seven lower parities match \(-271/81\), whose seventh iterate is \(-1\) with four odd inputs. The corresponding positive lower iterate is exactly \(2^{162m+11}-1\). The proof above does not give an opposing descent for this infinite Mersenne family.

More precisely, this family defeats every fixed deadline for even a factor-of-two native descent. Through clocks zero to seven, the slope numerators divided by the clock powers of two along the rational shadow are \(1,3/2,3/4,9/8,9/16,27/32,81/64,81/128\). Every subsequent shadow input is \(-1\), and every subsequent slope is multiplied by \(3/2\). For each fixed \(H\), the positive sources in the family share the shadow word through \(H\) for all sufficiently large \(m\). Their ordinary affine intercepts are nonnegative. They therefore satisfy \(T^j(z)\ge9z/16\) simultaneously at every \(0\le j\le H\). This does not exclude a later strict descent whose clock grows with the source.
