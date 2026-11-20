# Independent review of the local single-slice energy bridge

**Verdict: VERIFIED local identities and conditional continuation at the
frozen bytes; universal propagation remains OPEN.**

Reviewed source:
`research/closure-attacks-20261120/critical/SINGLE_SLICE_ENERGY.md`, SHA256
`f102fbf260c0ccdf6bc489392de3602a9e9b52f047a38f9e8ae5ed8afb796e79`.

This review independently reconstructs SE-001, the additional adjacent
transport, their weights, and the scalar conditional continuation. It does
not promote the separate M5 hypothesis or PD/UP dependencies.

## Exact domains and local edges

For shortcut-invariant metric labels, \(e_5(2x)=e_5(x)\). Unique removal
of powers of two and Tonelli summation therefore give the factor
\((1-2^{-s})^{-1}\) for every \(s>0\), including extended sums.
The old five-ray slice is related to this defect by the displayed actual
ordinary identities, with exactly the weight \(4^{-s}\).

If \(n\equiv1\pmod4\), then both \(n\) and \(5n\) are followed by
an even intermediate state. Their actual two-step outputs are
\(b=(3n+1)/4\) and \(a=(15n+1)/4=5b-1\). The triangle inequality
gives \(A_f(a)\le e_5(n)+e_5(b)\). The restriction \(3\nmid n\)
is retained, while \(b\equiv1\pmod3\) automatically. Parameterizing
\(n=4m+1\) shows that the valid adjacent edges are exactly the classes
\(a\equiv4,19\pmod{45}\), with the class 34 correctly excluded.

The inequalities \(a\ge15n/4\) and \(a=5b-1\ge4b\), together with
injectivity before removing powers of two, give the constant
\((4/15)^s+4^{-s}/(1-2^{-s})\). At exponent one this is exactly
\(23/30\). In particular, the geometric factor accounts for all
possible collisions when the even parameter \(b\) is reduced to its
odd part; no false finite multiplicity is assumed at that step.

## Additional two-step adjacent transport

For \(z=4k+1\), the adjacent ordinary sources \(z,z+1\) have respective
two-step images \(3k+1,3k+2\). Hence
\(A_f(a)=A_f((4a-1)/3)\) for \(a\equiv1\pmod3\), as stated.

At the sparse target \(a=54j+1\), the direct bridge has the correct
domain for \(j\equiv2\pmod5\). The transport changes its endpoint to
\(72j+1\), which lies in the required class 19 modulo 45 when
\(j\equiv4\pmod5\). The displayed parameters in both cases are
positive ternary units, and their first query is 1 modulo 4. The ratio
\((72j+1)/(54j+1)<4/3\) supplies the extra weight factor. Both affine
maps are injective. Summing the two bounds separately permits overlapping
image sets and gives precisely the claimed constant
\([1+(4/3)^s]C_s\), or \(161/90\) at exponent one.

## Conditional continuation and remaining gap

The corrected continuation first applies a bounded real 1-Lipschitz test
to an arbitrary metric label. This avoids assuming a metric-valued
\(L^1\) limit, completeness, or boundedness of the original target.
If the proposed full adjacent harmonic-energy bound were known, exact
doubling would make the scalar logarithmic profiles \(L^1\)-Cauchy.
The named ordinary synchronization and variation inputs give an
irrational-rotation invariant limit, and PD with a separating scalar test
then forces constancy. This is a valid sufficient conditional route.

No estimate propagating the two covered quinary classes to all required
queries has been proved. The note correctly does not replace missing
weighted global multiplicity by a finite number of local oracle calls or
by logarithmic descent depth. This review accepts no finite-energy
single-slice rigidity theorem beyond the explicitly conditional argument.

The checks here are symbolic reconstruction of the written formulas.
The author's finite checker was not rerun for this review, and this note
does not represent a new ordinary trajectory census or a proof of global
summability.
