# Independent review of the Hardy inverse-tree construction

Date: 2026-11-23. Reviewer: `/root/risk23_compact_escape`.

Reviewed file: `risk23/cycle/HARDY_INVERSE_TREE.md`.
Reviewed SHA256: `bb1d37dfcd61c53d28611bfc950d437d4f7b5d54bd5a35098558f8493cebca4a`.

**Outcome: no mathematical flaw found in the written infinite-dimensional argument.** This is an independent written review, not Lean verification of Hardy-space or Hilbert-space results.

## Specific checks

1. The shortcut pushforward is bounded on coefficient square-summable sequences, with operator norm at most square root of two, because each target has at most two ordinary preimages.
2. The exponent table in the interval 3 through 8 selects exactly two genuine odd unit parents, both strictly larger than the target. The chosen tree is injective at unequal depths even when its root is periodic in the ambient graph: equality would identify the root with a strict selected descendant.
3. The even-block coefficient is the sum of the active channel coefficients. At the vertex 2^j v, the incoming even coefficient and the possible odd child with exponent j+1 add to lambda times the prescribed coefficient. No independent mass is assigned twice on a shared even tail.
4. The generation-square sum is bounded by [max(1,abs(lambda)^16)/2]^k, so the stated Hardy norm bound and its open disk of validity are correct.
5. The root-excluded flow has precisely the defect lambda times the root monomial. There are no unaccounted external defects because every supported vertex maps to another supported block or to that root.
6. For a single channel of exponent e, the finite coast has defect lambda z^n minus lambda^e z^(2^(e-1)n). The child monomial plus its root-excluded flow cancels the second term exactly. Subtracting the two channels therefore yields an eigenvector.
7. The eigenvector is nonzero at the first odd child. The second channel cannot contain that odd vertex by selected-tree injectivity; its coast is even.
8. The antichain of selected strings 1, 01, 001, ... has disjoint odd subtrees. Even blocks with different odd parts cannot intersect. Hence the constructed eigenvectors are pairwise orthogonal, not merely formally independent.
9. The zero-eigenvalue vectors have disjoint odd/even source pairs with equal actual shortcut images. The zero-constant-term and quotient-by-the-trivial-cycle claims are valid.
10. At lambda=1 the coefficient sequences belong to every ell^s with s>1 and fail ell^1, for the stated generation-mass reason. Thus no finite positive invariant support or new integer cycle follows from the construction.

## Primary-source check

Opened Mikhail Neklyudov, *Functional analysis approach to the Collatz conjecture*, arXiv:2106.11859v9, https://arxiv.org/pdf/2106.11859. Its displayed operator is exactly the coefficient pushforward used in the draft. Theorem 4.4 explicitly places its cycle-count index bound on unweighted H^2(D). Theorem 2.3 constructs the displayed dyadic-ray eigenvectors in the Bergman quotient, so the draft correctly distinguishes that result from the branching-tree H^2 construction.

No exhaustive novelty or priority search was performed. The review supports the explicit theorem and the limitation of the stated unweighted Hardy-index route, without a Collatz convergence or cycle-exclusion claim.
