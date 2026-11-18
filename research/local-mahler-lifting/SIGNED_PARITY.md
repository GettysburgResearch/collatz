# Exponential morphic parity on rational sources of either sign

**Proposed.** Let $x\in\mathbb Q\cap\mathbb Z_2$ have a shortcut-Collatz parity word admitting a morphic presentation of exponential emitted length. Then the orbit of $x$ is eventually periodic. This includes arbitrary automatic parity words and primitive substitution codings, and allows finite prepending or deleting a finite prefix. The same polynomial-growth restrictions for any hypothetical divergent morphic itinerary consequently hold for negative as well as positive rational sources. The proof uses the [exponential transfer](EXPONENTIAL_MORPHIC.md) and [erasing normalization](MORPHIC_NORMALIZATION.md).

In a nonperiodic rational orbit fix an odd positive denominator $d$ throughout. All states are distinct and $|x_n|\to\infty$ since the numerators are integers. There is therefore a tail of fixed sign with $|x_n|>1$; the shortcut map preserves the sign whenever $|x_n|>1$. Start on this tail, or equivalently transfer finite prefixes using the inverse affine identity. The odd absolute numerator states $a=d|x_n|$ have accelerated updates
$$
 a\longmapsto (3a+\varepsilon d)/2^{v_2(3a+\varepsilon d)},
$$
where $\varepsilon$ is this sign. They are positive, distinct, and have distinct endpoints at every fixed number of odd steps. The cylinder and endpoint count in the exponential proof works for either sign. Multiplication by the odd unit $\varepsilon d$ identifies parity-residue cylinders with the ordinary $3n+1$ cylinders; their positive odd source count up to $X$ has the same bound in each residue. The magnitude of the affine correction after $j$ steps is at most $d((3/2)^j-1)$ in both cases. Hence the number of odd absolute numerators up to $X$ is $O_d(X^{39/40})$ and their reciprocal sum is finite.

Real telescoping now gives a **nonzero signed** limit
$$
 \lim_{n\to\infty} M_n x_n
   = x_0\prod_{j:e_j=1}(1+1/(3x_j))\ne0,
 \qquad M_n=2^n3^{-s_n}.
$$
Each factor is positive on the chosen tail; the sum of its deviation from one converges absolutely, so the product converges to a positive real number. The other exact telescope yields $\sum_{e_j=1} M_j<\infty$, and summing through the even runs again gives $\sum_j M_j<\infty$. Therefore the real absolute convergence needed by the exponential transfer holds. At 2, $M_n x_n\to0$, so $x_0+\frac13\sum_{e_j=1}M_j=0$ there. The finite-place argument would give the same identity over the reals, contradicting the nonzero limit above. For the original unshifted coding, convergence and the nonzero limit are preserved under the finite rational affine initial segment.
