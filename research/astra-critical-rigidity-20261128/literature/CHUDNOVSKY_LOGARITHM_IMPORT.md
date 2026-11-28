# The exponent-three theorem for the actual Collatz clock

Gregory V. Chudnovsky's October 20, 2026 preprint, Theorem 11.1, gives
\[
  2\le\mu(\gamma)\le3,\qquad \gamma=\frac{\log3}{\log2}.
\]
Here \(\mu\) is the ordinary irrationality exponent. Apply the theorem to the positive rational bases \(a=3,b=2\). For \(q>0\), \(3^q=2^p\) is impossible for an integer \(p\). For \(p\le0\) compare sizes, and for \(p>0\) compare parity. The denominator logarithm is positive. The theorem gives finitely many reduced rational approximants of exponent \(\nu\) for each fixed \(\nu>3\). [Original v1, Theorem 11.1 and proof](https://arxiv.org/html/2610.28079v1#S11) · [Original v1 source and Lean supplement](https://arxiv.org/src/2610.28079v1)

The [matched Sidon code argument](../cycles/MATCHED_SIDON_CODES.md) gives the opposite approximation requirement at every fixed width \(R<4\). In its notation a growing family of primitive positive ordinary cycles in that band has
\[
   0<A/p-\gamma\le p^{-3.12788862+o(1)}.
\]
Choose \(3<\nu<3.12788862\). Reduction of \(A/p\) can only improve the comparison with the negative \(\nu\)-th power of its denominator. These rational values approach the irrational \(\gamma\), so they include infinitely many distinct values. This contradicts Theorem 11.1. Thus each fixed \(R<4\) contains finitely many such cycles. Along every sequence of distinct positive ordinary cycles, \(\liminf X/m\ge4\), where \(m,X\) are the least and greatest odd states. This argument permits widths tending to four from either side. [Matched code theorem](../cycles/MATCHED_SIDON_CODES.md)

## What the October formal source exports

The archive's `anc/lean/QuadraticPi/RationalLogRatioTheorem.lean` exports general exponent bounds, finiteness of good rational approximations and a specialization for numerator logarithm two and denominator logarithm three. The general root takes positive rational bases, a nonzero denominator logarithm and the condition that \(a^q\ne b^p\) for every positive natural \(q\) and integer \(p\). A second version takes irrationality of the ratio. The fixed-pair linear-form version covers arbitrary nonzero integer coefficient pairs, including unreduced approximants. The principal declarations are

* `QuadraticPi.rationalLogRatio_finite_good`
* `QuadraticPi.rationalLogRatio_irrationalityExponent_bounds`
* `QuadraticPi.rationalLogRatio_irrationalityExponent_bounds_of_irrational`
* `QuadraticPi.log_two_div_log_three_irrationalityExponent_bounds`
* `QuadraticPi.rationalTwoLog_linearForm_lowerBound`

The source definition in `ExponentConclusion.lean` uses a set of rationals with their canonical positive reduced denominators. It requires denominator at least two and strictly positive error below that denominator to the negative exponent. It takes the real supremum of those positive exponents for which this set is infinite. `FiniteSpectrumConclusion.lean` proves boundedness and nonemptiness before using the real supremum. The separate finiteness theorem gives the cycle application directly.

In `TwoLogarithmConclusion.lean` an intermediate statement accepts center-uniform interpolation. The public wrapper supplies `TwoLogUniformInterpolation.twoLogUniformInterpolation`, proved by constructing successive thresholds and the actual jet-map surjections. The determinant proof uses the same selected minor for its arithmetic lower and analytic upper bounds. It fixes dimension first, then selects widely separated approximants, then lets the divisible polynomial degree increase. Appendix A, Review 19 identifies the ratio theorem as a directly checked result. Nine other applications in the paper have named classical inputs. [Original Appendix A](https://arxiv.org/html/2610.28079v1#A1)

## November's extension and the exponent convention

Chudnovsky's November 23, 2026 preprint, Theorem 1.1, treats positive multiplicatively independent rationals \(a_1,\ldots,a_n\). For every \(\varepsilon>0\) it obtains a positive, ineffective \(C\) such that
\[
 |h_0+\textstyle\sum_i h_i\log a_i|\ge C H^{-n-\varepsilon},
 \qquad H=\max(1,|h_0|,\ldots,|h_n|),
\]
for every nonzero integer coefficient vector. The literal declaration `QuadraticPi.CLogMainTheorem.linear_forms_in_logarithms_with_constant` takes the dimension condition, positivity, absence of integral multiplicative relations and \(\varepsilon>0\). Corollary 1.2, `QuadraticPi.CLogCorollaries.linear_forms_in_logarithms`, sets \(h_0=0\). With \(n=2\), dividing a small linear form by the denominator and the fixed nonzero logarithm gives rational-approximation exponent at most **three**. The affine exponent's optimality allows a moving integer constant term. The proof builds on the October two-torus argument. [Original Theorem 1.1 and Corollary 1.2](https://arxiv.org/html/2611.30820v1#S1.SS1) · [Original v1 source and Lean supplement](https://arxiv.org/src/2611.30820v1)

## Source provenance and verification boundary

The independently downloaded October archive has SHA-256 `2b37bfa6f04a1316eead45f1b6ba2ad660eef6a02f00b31476d603a7e55de69e`. The November archive has SHA-256 `dd44d584be74e1fe48b365f9a3b8e22f01b59eccc3cce67be3e495769712e31e`. Both pin the official Lean 4.34.1 release, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The October source manifest verifies 1,604 files and separately the manuscript. November reproduces the same manifest and the same 1,604 files, with 300 additional verified files. Each archive's literal endpoint types and hypotheses were inspected against its original TeX.

The October author's recorded audit at `anc/lean/validation/final-review-2026-10-19/original-2145-declaration-audit.log` reports exactly `propext`, `Classical.choice` and `Quot.sound` for the two general exponent roots and the homogeneous linear-form root. The last October build reused source-guarded project objects. November's `anc/docs/build-reports/fresh_clone_build_2026-11-22.txt` records the same axioms for the affine and homogeneous roots. The source audit reproduces these checks directly against both arXiv archives. [Audit script](audit_logarithm_sources.py) · [Source and historical audit receipt](LOGARITHM_SOURCE_AUDIT.json)

A separate portable replay builds the original October endpoint, applies it to the order \((3,2)\) and prints the axioms of four original and three local declarations. It requires an official Lean installation, the pinned external dependencies, adequate local storage, and time for the original thousand-module import closure. The source-audit receipt records archive verification and the author's historical output. A fresh local kernel receipt must be identified separately. The mixed-code estimates and the Collatz implication are written mathematics. [Rebuild script](replay_logarithm_endpoint.py) · [Lean specialization](ChudnovskyLog32.lean)
