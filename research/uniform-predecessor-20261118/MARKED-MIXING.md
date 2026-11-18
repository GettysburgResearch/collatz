# Fine-scale mixing with a marked valuation sum

Use iid positive geometric exponents e_i with P(e_i=j)=2^(−j),
S_n=sum_{i≤n}e_i, and the inverse-order offset

    F_n = sum_(j=1)^n 3^(j−1) 2^(−S_j).

Write ν_(n,a) for the subprobability law of F_n modulo 3^n on
S_n=a, and lift a coarse projection uniformly back to the full quotient.
For each D>0 and fixed 0<γ<1,

    ||ν_(n,a)−lift(proj_m ν_(n,a))||₁ ≤ C_(D,γ) n^(−D),
       γ n ≤ m ≤ n,  a an arbitrary integer.                          (1)

The norm here is the sum of absolute probability masses, equivalently
the Haar L¹ norm of the normalized densities. The coarse projection is
the actual joint marginal with the same total event; no independence
between the coarse digits and the total is asserted.

This proof imports the estimates in Tao's argument for fine-scale
mixing. The extra total indicator is not an assumption on an individual
ordinary orbit.

## Fourier damping with a total mark

For a primitive character χ of conductor 3^p and any function v with
|v|≤1, Tao's Proposition 7.3 and (7.5)–(7.10) give

    |E[χ(F_p) v(S_p)]| ≤ C_D p^(−D).                                (2)

Indeed condition on all pair sums e_(2i−1)+e_(2i), and on the last
exponent separately if p is odd. The factor v(S_p) is fixed by this
conditioning, and has modulus at most one. The remaining conditional
expectation factors exactly into the pair factors of (7.4), with an
additional unit phase for the odd final term. Taking absolute values
gives the identical upper bound by the expected product of the absolute
pair factors. The white-point estimate and Proposition 7.3 apply
unchanged. If the word has length p+j and the character has conductor
3^p, its value depends only on the first p exponents. Integrating out
the last j independent exponents turns any bounded function of the
full sum into another bounded function of S_p. The same bound follows.

[Tao, §7, including Proposition 7.3](https://arxiv.org/html/1909.03562v7#S7).

## Passage from Fourier damping to total variation

First suppose m≥0.9n. In Tao §6, impose S_n=a in the probability
law throughout equations (6.2)–(6.11). The costs of discarding the
large-deviation exceptional set and enlarging E to E_k only decrease.
The dyadic stopping index k and the fixed prefix sum l=S_(k+1) range
over the same polynomially many possibilities in (6.5)–(6.8). On
the event C_(k,l), the added indicator is exactly the event that the
remaining n−k−1 independent exponents have sum a−l. In the Fourier
factorization after (6.10) it therefore affects only the second factor,
whose conductor is 3^(n−k−j−1) for j<n−m. The exponent is bounded
below by a positive multiple of n as in §6. Equation (2), including
its extension to more steps than the conductor, gives arbitrarily high
polynomial decay for this factor, uniformly in a−l. The first factor
and its squared Fourier sum are exactly the original ones: the residue
separation in Corollary 6.3 gives the same polynomial loss following
(6.11). Choosing the decay power as large as needed, Plancherel and the
triangle inequalities in (6.4)–(6.10) prove (1) for m≥0.9n. This
argument uses the estimates inside §6, not an inference from the
unmarked conclusion of Proposition 1.14 alone.

For a projection to a lower level k, F_n≡F_k modulo 3^k and the
remaining sum is independent. Consequently proj_k ν_(n,a) is the
mixture of ν_(k,s) with coefficients P(S_(n−k)=a−s). Summing these
coefficients over all integer s gives one. The proved one-ratio estimate
therefore applies to a further projection from k to k'≥0.9k, uniformly
in n and a, with cost O_D(k^(−D)). Telescope through a bounded number
(depending on γ) of such ratios down to m≥γ n, treating bounded small
n separately. This proves (1).

[Tao, §6, including stopping decomposition and Corollary 6.3](https://arxiv.org/html/1909.03562v7#S6).
