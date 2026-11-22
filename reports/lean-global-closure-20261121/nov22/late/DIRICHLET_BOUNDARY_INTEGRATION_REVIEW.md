# Scoped review of the sharp Green-potential energy identities

Date: 2026-11-22. Reviewer: `global_merger22`.

**Result: VERIFIED within the scope below, under the displayed frozen
ordinary harmonic and canonical Green inputs.** This is a written semantic
review, not a Lean audit or a fresh certification of upstream analytic inputs.

## Frozen target and review scope

Target: `agent22_analytic/LITERATURE_DIRICHLET_BOUNDARY.md`.

SHA256:
`41b4fe328417b3feef665b4de53fff1e94fdccc37bea1e75ce99ee4c3523c504`.

The prior reviewed version had hash
`2e4ff88d3da717d522484efe96b746a6328cf335159687ab962f51649bdcb941`.
The final version adds introductory clarification distinguishing the shortcut,
accelerated, and killed-domain companion counterexamples; the reviewed sharp
identities are unchanged. The final Section 6 was read again before repinning.

The actual bytes were read and hashed before writing this receipt. The review
covers Section 6, especially equations (19)–(24), and reconstructs the required
Green-truncation and Hilbert-space facts from Sections 2–3. It checks both sharp
averaging identities, the non-square-integrable boundary term, killing, and the
scope of the zero-coefficient conclusion. It does not certify the full Section 7
countermodel, the external literature quotations, the predecessor-population
construction, or the separate five-edge transport theorem.

The reviewer supplied the weak-gradient boundary argument during collaboration.
Accordingly this is a reconstruction of its integration and of the surrounding
sharp identities, not an assertion of independent authorship or a blind
independent review of that idea. The certificate lane supplies an additional
independent review of the combined note.

## 1. The relevant expressions really belong to the Hilbert space

The state space has strictly positive finite weights, so finite-support vectors
are dense in \(H=\ell^2(\mathcal N,\nu)\). Harmonicity gives the killed
composition isometry \(C\), its adjoint \(K\), and \(KC=I\).

The nonnegative charge satisfies \(D=\sum d<\infty\), and
\(g=d/\nu\le R\le1\). Thus \(g\in L^1(\nu)\cap H\). Each finite Green
sum \(R_M=\sum_{j<M}K^jg\) belongs to \(H\), has values in \([0,1]\),
and obeys \((I-K)R_M=g-K^Mg\). The isometry energy identity gives

\[
\|(I-C)R_M\|_H^2\le2\sum dR_M\le2D.
\]

The pointwise limit of these gradients is \(a=(I-C)R\). Fatou puts \(a\)
in \(H\). Uniform boundedness, convergence of pairings with finite-support
vectors, and their density prove \((I-C)R_M\rightharpoonup a\). Strong
convergence of these gradients is neither asserted nor needed.

The equality \(Ka=-g\) is legitimate even though \(R\) itself need not be
in \(H\): the bounded point-function extension has \(KR=R-g\) by the
nonnegative Green series, while \(KCR=R\) by the harmonic row sums.
On the actual Hilbert vector \(a\), this extension agrees with the adjoint.

## 2. The boundary pairing is exact

Using only finite Green sums inside Hilbert pairings,

\[
\begin{aligned}
\langle a,(I-C)R_M\rangle_H
 &=\langle a+g,R_M\rangle_H\\
 &=\sum_{j<M}\langle C^ja,g\rangle_H+\sum dR_M\\
 &=b_0-b_M+\sum dR_M,
\qquad b_j=\sum d\,C^jR.
\end{aligned}
\]

The finite telescope uses \(C^ja=C^jR-C^{j+1}R\). Its sums against \(d\)
are absolutely integrable because \(0\le C^jR\le1\) and \(D<\infty\).
The killed extension is retained throughout. Weak convergence of gradients
handles the left side; monotone convergence handles \(\sum dR_M\); the
source-qualified pointwise forward limit and dominated convergence handle
\(b_M\to b_\infty=\sum dF\). Therefore

\[
\mathcal D(R)=2b_0-b_\infty.
\]

There is no subtraction of two infinite \(\|R\|_H^2\) expressions and no
unjustified interchange of an infinite edge sum with a signed limit.

## 3. Both normalized averaging constants check

For \(j\ge1\), adjointness gives the exact correlation

\[
\langle a,C^ja\rangle_H
=\langle Ka,C^{j-1}a\rangle_H=b_j-b_{j-1}.
\]

Expanding the finite Cesàro square gives

\[
N\mathcal D(\mathsf A_NR)
=\|a\|_H^2+\frac2N\sum_{j=1}^{N-1}(N-j)(b_j-b_{j-1})
=\frac2N\sum_{j<N}b_j-b_\infty.
\]

This proves the exact identity and limit in (21), including \(N=1\).
It uses ordinary Cesàro convergence of the already convergent bounded
sequence \(b_j\), not a forward monotonicity assumption.

For the Abel square, the correlation expansion is absolutely convergent
because \(|\langle a,C^ja\rangle_H|\le\|a\|_H^2\) and \(\alpha<1\).
The diagonal weight is \((1-\alpha)/(1+\alpha)\), and

\[
\sum_{j\ge1}\alpha^j(b_j-b_{j-1})
=(1-\alpha)\sum_{j\ge0}\alpha^jb_j-b_0.
\]

Substituting the boundary identity yields

\[
\frac{1+\alpha}{1-\alpha}\mathcal D(\mathsf B_\alpha R)
=2(1-\alpha)\sum_{j\ge0}\alpha^jb_j-b_\infty.
\]

This verifies (22), its \(\alpha=0\) endpoint, and its limit as
\(\alpha\uparrow1\). The normalization is the stated
\((1+\alpha)/(1-\alpha)\), without an omitted factor of two.

## 4. Component interpretation and exact scope

The imported canonical limit \(F_C=D_C/C_C\), the nonnegativity of the
charge, and countability of the state space justify

\[
b_\infty=\sum_{C\text{ escaping}}D_C^2/C_C\le D.
\]

Every escaping component contains a state with strictly positive charge,
so this coefficient vanishes exactly when no escaping component exists.
The little-oh conditions stated after (24) follow from the proved limits.
An \(O(1/N)\) or \(O(1-\alpha)\) estimate alone does not imply the
little-oh condition. The note correctly leaves nontrivial periodic cycles
outside the conclusion, because the domain kills all periodic points.

No correction is required to the reviewed sharp identities or their stated
scope. Their dependencies remain written analytic inputs rather than
kernel-checked Lean hypotheses.
