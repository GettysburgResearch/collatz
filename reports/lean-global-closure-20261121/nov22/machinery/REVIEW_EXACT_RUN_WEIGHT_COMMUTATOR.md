# Independent scoped review of the exact canonical commutator

Date: 2026-11-22. Reviewer lane: entropy / ordinary fibres.

Reviewed file:
`machinery22/potential/EXACT_RUN_WEIGHT_COMMUTATOR.md`

Frozen SHA-256:
`521ed021ebfa0f010c9881e2ec40fb2603438547c383a0ff8bd6762fbc8be6b7`

**Verdict: the new written deductions pass this independent reconstruction,
conditional on the frozen inputs explicitly listed in Section 1.** No Lean
formalization, independent replay of ESS, or re-audit of the canonical
construction is asserted by this review. The source-qualified and
non-closure status in the note is accurate.

## Checks performed

1. **Integrability before signed rearrangement.** For each finite Green
   depth, \(a_M=\nu R_M^2\le\nu R_M\) and
   \(\|a_M\|_1\le M\|d\|_1\). Killed forward transport does not increase
   the mass of a finite nonnegative measure. Thus both \(a_M\) and
   \(La_M\) are finite, \(\lambda_M=La_M-a_M\) is absolutely summable,
   and all pairings with the bounded future envelopes are valid. No
   Hilbert-space membership of those envelopes is required.

2. **The source-preserving negative-part bound.** Since \(K\) is Markov,
   Jensen gives \(Kf^2\ge(Kf)^2\). For \(f=R_M\),
   \(f-Kf=g-K^Mg\le g\) and \(0\le f,Kf\le1\). Therefore
   \((\nu f^2-\nu Kf^2)_+\le2\nu g=2d\), exactly the claimed
   \(\lambda_M^-\le2d\). The constant is independent of \(M\).

3. **The telescoping identity and both killed-envelope signs.** Adjointness
   gives \(T_{N,M}=\langle H_N,\lambda_M\rangle\), with
   \(H_N=N^{-1}\sum_{j<N}C^jw\). For the future supremum and infimum,
   \(CH_N^+\le H_N^+\) and \(CH_N^-\ge H_N^-\). These remain correct at
   killed vertices because every later value is zero. Pairing those
   inequalities with \(a_M\ge0\), then using the negative-part bound,
   gives both sides of (14) and the uniform absolute bound (15).

4. **The limit is uniform in finite Green depth.** On an escaping source,
   the imported upper Banach run statement forces *every* length-\(N\)
   future window average to approach the fixed cutoff \(W\). On a source
   killed after finitely many retained steps, all future averages are
   bounded by \(W\tau(x)/N\), and the future infimum is zero. Thus the
   envelope oscillation tends to zero at every original source. The
   dominating measure is the same finite \(d\); the bound contains no
   \(M\). This proves (7) in precisely the claimed absolute uniform form.

5. **Component limits and source preservation.** The inverse-tree formula
   (18) counts each source once because a retained root is nonperiodic.
   Along an escaping ray the predecessor trees increase and exhaust its
   component, so \(R(U^kx)\to D_E/c_E=F_E\). Each original summand of the
   transport term converges to \(2d(x)F_E(W-w(x))\). Its absolute value
   after time averaging is bounded by \(2W d(x)\), which justifies both
   the source sum and the component regrouping. Since \(0<F_E\le1\),
   all component series used are bounded by the original finite charge
   or its original weighted forcing. No mass is reattached at the
   terminal point.

6. **The supremum over all finite Green depths.** Although
   \(A_{N,M}\) need not increase with \(M\), its excess over
   \(A_{N,\infty}\) is bounded by the negative-coefficient error
   \(\eta_{N,L_0}\) in (24). On escape this tends to zero because
   \((w(x)-w(U^jx))_+\le W-w(U^jx)\); on a killed source only finitely
   many terms survive. Dominated convergence against \(d\) is legitimate.
   For the reverse inequality, convergence
   \(A_{N,M}\to A_{N,\infty}\) at fixed \(N\) implies
   \(A_{N,\infty}\le\sup_M A_{N,M}\). Combining this with the uniform
   absolute boundary bound gives exactly the two-sided sandwich (25).
   It does not require a limit of the signed boundary term as
   \(M\to\infty\).

## Scope of the conclusion

Equations (7)--(8) identify the previously unresolved commutator for every
fixed run cutoff, including the supremum over all finite Green depths.
The leading surviving term is \(2Wb_\infty\); the subtraction is bounded
independently of the cutoff by the imported finite static forcing.
Consequently the note proves no bound uniform in that cutoff under a
positive escape charge. It correctly records this as an exact evaluation
of the actual canonical obstruction, not a proof that escape charge
vanishes.
