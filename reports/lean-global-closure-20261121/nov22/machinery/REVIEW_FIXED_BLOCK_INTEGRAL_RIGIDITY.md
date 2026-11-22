# Scoped review: fixed-block integral rigidity

Date: 2026-11-22. **Verdict: VERIFIED in the displayed written mathematical scope, importing the published Corvaja–Zannier result.** No full Collatz conclusion is established, and no Lean verification is asserted.

Reviewed artifact: `machinery22/arithmetic/FIXED_BLOCK_INTEGRAL_RIGIDITY.md`.

SHA256: `0fd4f41c6df82dc467c2295ecdadb0fa7fe9095ac945a9ff49142e954b76c9a4`.

## Primary theorem boundary

I independently retrieved the indexed text of Corvaja–Zannier's author-hosted paper:

- P. Corvaja and U. Zannier, *Finiteness of integral values for the ratio of two linear recurrences*, Invent. Math. 149 (2002), 431–451.
- DOI: https://doi.org/10.1007/s002220200221
- Primary PDF: https://oerior.uniud.it/wp-content/uploads/2018/12/CorvajaZannier2002.pdf
- Statement checked: Corollary 1 and its explanation immediately following Theorem 2.

The corollary applies when the root group is torsion-free and the denominator's coefficient polynomials have constant gcd, in particular to a simple denominator. Infinitely many values in the specified finitely generated ring then imply a recurrence quotient. The text also explains why passing to progressions is unnecessary when the group is already torsion-free. The two denominator roots in the draft are distinct positive powers of two and three, so these hypotheses hold with the ring Z. The imported theorem's complete proof was not re-audited.

## Independent reconstruction

1. **Full affine composition.** Iterating one fixed block gives its displayed numerator `u^e x + κ(v^e−u^e)` over `v^e`. Composing from left to right multiplies a block's correction by all earlier denominator factors and all later numerator factors. This yields exactly `F=Σ κ_i(P_i−P_(i−1))` and `E=P_r−P_0`. The denominator has both complete terms; no proper-factor substitution occurs.

2. **Degenerate cases.** After shifting the parameter, all exponents are nonnegative. `A=0` forces every variable schedule coefficient to be zero, because each retained block has positive length. That case is constant. Empty whole words are properly removed. For `A>0`, `2^A` and `3^S` cannot coincide, including `S=0`.

3. **Root-group confinement.** Multiplication by the two-root denominator preserves cosets of `G=<2,3>` in the multiplicative complex numbers. On a nonzero finite exponential-polynomial sum, take a root of maximal modulus and multiply it by the larger positive denominator root. This produces a surviving maximal-modulus term; the smaller denominator root cannot cancel it. Thus multiplication is injective on each coset, and every nonidentity coset of the quotient must vanish. The same injectivity applied to the highest polynomial coefficient removes all positive powers of the index from the quotient coefficients.

4. **Laurent-polynomial identity.** Every remaining quotient root is uniquely `2^a 3^b` with integral exponents. Distinct Laurent monomials give distinct positive exponential bases, so an eventual sequence identity implies `F=EH` as a Laurent-polynomial identity. Minimum exponents add over the coefficient domain, and both minima of E are zero. Since F has no negative exponents, neither does H. Its X- and Y-degrees must both be zero because F is inside E's same bidegree rectangle. This argument includes `S=0`; `F=0` is handled separately. A single integral index then makes the constant quotient an integer.

5. **Common block fixed point.** If every `a_i>0`, the X-exponents of `P_0,...,P_r` strictly increase. Comparing their coefficients forces every adjacent `κ_i` to agree with the same constant z. The converse telescopes. Fixed connecting blocks do not satisfy this distinct-monomial argument; the stated `(10)^k 1 (01)^k 0` example correctly explains the exception.

6. **Physical legality.** At an integer fixed point, reducing the complete fixed-point equation modulo two forces the first prescribed parity. Applying that legal branch gives an integer fixed point of the cyclically rotated word. Iteration verifies all parities; a positive starting point remains positive. Thus the positive constant case really consists of loops of the deterministic Collatz map through the same state, and does not eliminate a hypothetical nontrivial cycle.

## Scope conclusion

The result concerns each fixed finite block list with affine repetition schedules. It does not supply a uniform cutoff across changing word descriptions, force an arbitrary exceptional word into one such schema, or turn a carried target into a recurrence merely because its source has entered a repeating tail. The draft correctly leaves those global inferences open.

No substantive correction was required. This review was independent reconstruction of the argument and a primary-statement check, not an independent proof of Corvaja–Zannier, a search for every prior appearance of the specialization, or a compiler run.
