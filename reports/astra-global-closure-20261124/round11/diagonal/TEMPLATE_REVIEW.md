# Independent review of bounded repeated-template visits

**VERIFIED as a written consequence of Evertse–Schlickewei–Schmidt.** For one fixed positive odd base, one fixed finite bank of nonempty chronological parity words, and one fixed upper bound on the number of powered blocks, only finitely many tower exponents admit an actual nonempty forward visit of that form to the stated lower cone. Repetition counts can vary without bound. The external theorem and this finiteness assertion are outside the four finite Lean kernels.

| Reviewed source | SHA-256 |
|---|---|
| BOUNDED_TEMPLATE.md | 8a0375a90421ee0b264573a3211cad96d8995840c2d66709d6d91e1343ca2077 |
| TemplateChain.lean | d66528f21e07a62ed43b9b334a04a266d31783b00cbc89b41076b16bd9f90f3b |

## Ordinary starting point and endpoint

For a word of positive length \(E\) and odd count \(P\), the slope \(3^P/2^E\) differs from one by unique prime factorization. The affine map consequently has a rational center, including the zero center of an all-even word. Fix the ordered block list. Each template's center is then fixed independently of the repetition counts. Equating consecutive centered maps after division by their cumulative slopes \(F_j\) gives the signs shown in equation (1). Identical adjacent centers remove interior terms. The original source and the negative endpoint term retain separate indices even if some numerical values subsequently cancel.

The initial integer \(w3^r\) is odd. Its first shortcut image is \(2\bmod3\), and every later shortcut preserves nondivisibility by three. Consequently any endpoint in the full cone is \(2^i b\) with \(1\le b\le w,\ 3\nmid b\). This argument includes odd \(w\) divisible by three. On the equal-base arm the actual \(s=0\) must also satisfy \(s<r\). Dropping that last restriction only enlarges the comparison set. The nonempty hypothesis is necessary in the stated generality: for \(3\mid w\), an empty trace already has the representation \(3^{r+1}(w/3)\) on a smaller base at every \(r\).

## Vanishing subsets and reference positions

Fix \(b\) as well. Write each term of (1) as \(A_j m_j\) with fixed rational coefficient \(A_j\ne0\) and a nonzero monomial \(m_j\) in the \(k+2\) parameters \(r,i,\ell_1,\ldots,\ell_k\). Here the term indices identify positions, including the separate endpoints. The term vector as a function of these integer parameters, **after removing the coefficients**, lies in the image of \(\mathbb Z^{k+2}\) under a multiplicative homomorphism. Positivity constraints on the parameters may be dropped for this group containment.

For each actual solution choose an inclusion-minimal zero-sum set of term indices containing the source. No proper nonempty subset can vanish. A vanishing subset containing the source contradicts minimality directly; one omitting the source can be removed and its nonempty complement still contains the source and vanishes. There are at least two terms since the source is nonzero. Choose a nonsource index \(d\) in this set and divide all the other terms by \(-A_d m_d\). For this fixed choice of indices and reference, the normalized variable vector \(m_j/m_d\) still belongs to a multiplicative group of rank at most \(k+2\), and the coefficients \(-A_j/A_d\) remain fixed. The resulting equation has right side one and no zero subsum. For two original terms there is a single projective ratio by elementary algebra. For more terms apply the published finite-rank theorem. Arbitrary vanishing subsets of the **full** expansion cause no loss of solutions. [Evertse, Schlickewei and Schmidt, Theorem 1.1](https://annals.math.princeton.edu/2002/155-3/p04) · [Author preprint, §§1 and 4](https://pub.math.leidenuniv.nl/~evertsejh/00-equation.pdf)

The finiteness of normalized ratios alone need not determine the original scale. It does bound the original exponent here. Every eligible nonsource monomial is either \(1/F_j\) or \(2^i/F_k\), with \(F_0=1\) allowed for the constant term. Its 3-adic valuation is nonpositive because every \(P_t\ell_t\ge0\), including all-even blocks. Therefore any fixed nonzero value \(\rho=(w3^r)/(A_d m_d)\) satisfies
\[
 r\le v_3(\rho)+v_3(A_d)-v_3(w).
\]
This bound holds for every parameter tuple realizing that ratio, with no lower bound on \(v_3(m_d)\). Changing the reference between different solutions costs only finitely many indexed choices. The union over those choices, source-containing subsets, \(b\), ordered templates and block counts remains finite. The ESS cardinality bound alone does not locate the last exponent.

## Checks and scope

I recompiled TemplateChain.lean with Lean 4.34.1 and the project Mathlib pin, using the previously built TowerClock dependency. The compiler exited zero with warnings as errors. The four printed declarations used only propext, Classical.choice and Quot.sound. The chain lemma assumes the displayed successive edge equations. Its instantiation by the physically realized repeated words is justified in the written proof.

An independent exact-rational check used all odd \(w\le31\), \(0\le r\le8\), and two blocks of lengths \(1\) through \(4\), each repeated one, two or three times. Reading each candidate from the actual orbit and discarding failed repetitions yielded 4,004 realized presentations. All satisfied (1) and had 3-free endpoints. They included 1,129 presentations with a zero center, 1,525 with a nonintegral center and 654 with equal centers. In 584 presentations the endpoint belonged to the lower cone. These are counts of presentations and serve as finite checks only.

The result covers a visit ending at the last specified block. It gives no universal ban on visits involving unboundedly many blocks, no bound on a source-dependent bank, and no exclusion of a two-arm meeting via unrelated preperiods.
