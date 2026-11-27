# The actual child-component descent still required

**Universal closure OPEN.** This continuation attacks the single ordinary
implication left by the pinned finite reduction:
\[
36k+8\in C\quad\Longrightarrow\quad72k+17\in C,
\]
equivalently \(u\in C\Rightarrow9u+2\in C\) for \(u=9k+2\).
Here \(C\) is the basin of 1 for the positive shortcut map.
The [preceding packet](../astra-global-budget-20261124/README.md)
contains the earlier cost, certificate and paired-renewal attempts.

The direct round gives an explicit weaker obligation at the original
least counterexample. Write
\[
(4u+1)/9=3^h w,\qquad 3\nmid w,\qquad B(u)=8\,2^h w-1.
\]
This integer lies in the actual child's ordinary component. If \(N\)
is the least counterexample, the complete finite reduction supplies a
failed transfer with
\[
N\le B(u)\le JN,\qquad J=\frac{20970919}{122875}<171.
\]
Thus an actual child-component value \(z<B(u)/J\), or a physical hit
of 1, discharges this candidate. Either direction of an ordinary edge
preserves its basin label; a numerical size comparison alone does not
give that connection.

The full proof and dependencies are in [the descent note](descent/README.md).
The elementary normalization and all-odd paths are
[kernel checked](descent/CanonicalSource.lean).
The finite table and its exact multiplier are imported from PR193 at
67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e; their affine replay is
independently checked in the reviews.

## The earlier terminal family now has an actual descent

For \(u=2^{6j+1}\), the child at the parent stopping clock is
\(9\cdot27^j+1\). That value is smaller than \(B(u)/171\) for every
\(j\ge10\). The ten earlier children reach 1 by explicit finite traces.
This discharges the whole family as a witness in the least-counterexample
argument. It does not infer that a large endpoint converges merely
because the parent does.

A further written application of Evertse's theorem treats deep
translates \(u=2^a v+d\) around any fixed certified reference
\(9d+2\in C\). The exact child's endpoint discharges sufficiently deep
translates with \(\log v=o(a)\). Its constants depend on the fixed
reference. This supplies no uniform statement for arbitrary changing
low-bit references.

## The unresolved arbitrary-parent step

For \(u=(2^\ell-1)/3\), \(\ell=18j+16\), the parent has only one odd
input before reaching 1. The child has \(\ell\) consecutive odd inputs,
ending at \(3^{\ell+1}-1\). It does not drop below the required threshold
during the parent's certificate.

An actual failure here can be reselected to an odd exponent \(d\) such
that \(2^{d-1}-1\) converges but \(2^d-1\) does not. Its known-good
parent is \((3^{d-1}-1)/4\). The new reduction is an ordinary component
calculation. It has no proved decreasing measure, and its canonical
size need not retain the original \(JN\) bound. Applying it repeatedly
is therefore not a terminating proof.

The next universal lemma must construct the strict component decrease
or a successful physical certificate for every candidate supplied by
the finite reduction. The direct round did not prove it. The renewal
stream also did not obtain a fixed ordinary companion-state floor;
the preceding moving-state counts do not supply that lemma.

The [coordinator review](../../reports/astra-closing-step-20261124/ROOT_REVIEW.md)
and [execution record](../../reports/astra-closing-step-20261124/VERIFICATION.md)
separate the written argument, the pinned upstream table and the four
new named Lean declarations.
