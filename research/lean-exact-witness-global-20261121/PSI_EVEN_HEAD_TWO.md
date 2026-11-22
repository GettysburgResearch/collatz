# Complete first-gap-two return at initial exponent two

**Status: proved in Lean core for every supplied complete source tail.**
Formal source:
[Collatz/PsiEvenHeadTwo.lean](lean/Collatz/PsiEvenHeadTwo.lean).

This closes the entire initial-exponent-two, first-odd-gap-two psi branch
under the original complete-source interval induction hypothesis. It adds no
new global closure premise and imposes no bound or pattern on the inherited
source tail.

## Exact target transport

Write the supplied source certificate as

\[
 S=4q,\qquad
 \operatorname{Certificate}(q;(2)\Vert\tau),\qquad
 3q+1=4u,\qquad
 \operatorname{Certificate}(u;\tau).
\]

Both \(q\) and \(u\) are positive and odd. The wanted target is
\(2S-1=8q-1\). Its exact target prefix is

\[
 \operatorname{Prefix}(2S-1;[1,1,2,1];27u-7).
\]

The polynomial check is

\[
 81(2S-1)+73=32(27u-7),
\]

which follows directly from the supplied first source edge. All four target
gaps are positive. The endpoint is permitted to be even.

## Case one: the literal tail endpoint is one modulo four

If \(u\equiv1\pmod4\), write

\[
 27u-7=4v.
\]

Then \(v>0\) and

\[
 v=\frac{27u-7}{4}\le8u+1.
\]

Use the known child source \(4u\), retaining initial exponent two and the
literal tail \(\tau\). Its complete grade strictly decreases by deletion
of the first source gap:

\[
 \Gamma(2;\tau)\prec\Gamma(2;(2)\Vert\tau).
\]

The original interval hypothesis supplies convergence of \(v\).
The factor four and the exact target prefix transport it back to
\(2S-1\). This case includes \(u=1\), so no empty-tail exception is
left open.

## Case two: the literal tail endpoint is three modulo four

If \(u\equiv3\pmod4\), its actual next source shortcut is odd:

\[
 w=\frac{3u+1}{2}.
\]

Thus its literal next source gap is one. The source identities give

\[
 6w-6q=u+5>0,
\]

so \(w>q\). Consuming the supplied source prefix \((2,1)\) therefore
replaces the old known source \(4q\) by the larger known source \(4w\).
The wanted target stays unchanged and remains in the child interval.

The Lean proof uses `ordinary_step` on the supplied certificate at
\(u\), proves that its returned initial even exponent is zero from the
oddness of \(w\), and retains initial exponent two around that actual
source tail. The resulting strict rank decrease is composed with deletion
of the old first gap two. It never extracts a new source certificate from
an induction conclusion.

## Formal interfaces and remaining scope

`CollatzPsiEvenHeadTwo.target_prefix` proves the exact arithmetic target
transport.

`CollatzPsiEvenHeadTwo.psi_rule` proves

\[
 \begin{gathered}
 \operatorname{PoweredCertificate}(S;2;(2)\Vert\tau),\\
 \operatorname{Hyp}(\operatorname{Interval};
                   \Gamma(2;(2)\Vert\tau))\\
 \Longrightarrow\quad B(2S-1).
 \end{gathered}
\]

Together with the already covered first gap one and the high-gap reductions,
this removes first gap two from the remaining initial-exponent-two psi
cases. The other source heads are handled separately in the aggregate
coverage work; this module introduces no assumption about them.

Validation uses Lean 4.34.1 core with `-DwarningAsError=true`.
No `sorry`, `native_decide`, or custom axiom is used.
