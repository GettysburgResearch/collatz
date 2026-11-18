# Excluding quadratic interruption times by a 2-adic Tschakaloff estimate

**PROPOSED.** No rational 2-adic integer has an eventually prescribed sequence of even shortcut-input positions equal to an integer-valued quadratic polynomial of their successive indices with positive leading coefficient. More generally, let W be a nonempty shortcut parity word and V a fixed possibly empty word. If a positive rational 2-adic source has a parity tail

    W^B V W^(A+B) V W^(2A+B) V … ,       A≥1, B≥0,                    (1)

then its orbit is eventually periodic. For an expansive W the rational exclusion below applies without assuming a positive source. No descent or symbolic hypothesis for arbitrary ordinary sources is inferred.

The quadratic case includes polynomial-growth morphic words such as an increasing arithmetic progression of odd-run lengths separated by a single even input. The previously published morphic results address exponentially growing substitutions; paper 69 explicitly excludes polynomial-growth presentations from its dynamical conclusion. The rational irrationality estimate used here is modeled on Zudilin's proof for the **real** values. Its real rational-q theorem as printed does not give the 2-adic statement needed for this deduction. No claim about priority of that p-adic irrationality criterion is made. [Zudilin, *An elementary proof of the irrationality of Tschakaloff series*](https://arxiv.org/abs/math/0506086) · [Morphic Collatz parity, paper 69](https://rstation.ai/problems/collatz/papers/69/v1)

## Place-specific irrationality lemma

Let q=P/D>1 in lowest terms, with D a positive power of 2 and P odd. If P^13<D^21, then for every nonzero rational z the 2-adic value

    T_q(z)=Σ_(k≥0) z^k q^(−k(k−1)/2)                                   (2)

is irrational. The terms converge since |q|₂=D>1. We reproduce the rational approximation estimates, in particular their orientations, as the archimedean value need not equal the hypothetical rational 2-adic value.

Put m=⌊n/2⌋ and R(T)=∏_(i=1)^n(1−q^i T)=Σ C_k T^k. Its coefficients are integer polynomials in q of degree at most n(n+1)/2, more precisely degree at most kn−k(k−1)/2 for C_k. At either convergent place form

    I_n=Σ_(t≥1) R(q^(−t)) z^(t+m) q^(−(t+m)(t+m−1)/2).

Expanding C_k and substituting l=k+t+m writes I_n=B'_n T_q(z)−A'_n with

    B'_n=Σ_(k=0)^n z^(−k) C_k q^(k(k−1)/2+km),
    A'_n=Σ_(k=0)^n Σ_(l=0)^(k+m) z^(l−k) C_k q^(k(k−1)/2+km−l(l−1)/2).

Write z=z₁/z₂ in lowest terms. The common factor

    H_n=z₁^n z₂^m P^(m(m−1)/2) D^(n(n+m))

clears both denominators, since the minimum q exponent in A'_n is −m(m−1)/2, the maximum total degree is ≤n(n+m), and −n≤l−k≤m. Suppose the 2-adic value equals a rational α of denominator h>0. Then M_n=h H_n(B'_n α−A'_n) is an ordinary integer. For t≤n the terms of I_n vanish. At 2 every R(q^(−t)) for t>n has norm one; the t=n+1 term has strictly larger norm than all its successors once n is large. Consequently M_n≠0 and

    log |M_n|₂ ≤ −[n(n+m)+(n+m)(n+m+1)/2] log D + O_z,h(n).

At infinity |B'_n|≤exp(O_z(n)) q^(n(n+m)): use the coefficient degree bound and the at most 2^n unsigned monomials. Also |A'_n| satisfies the same estimate, since Σ_(l≥0)|z|^l q^(−l(l−1)/2) is finite. It follows for the same rational α, without any identification of the real and 2-adic series, that

    log |M_n|∞ ≤ [m(m−1)/2+n(n+m)] log P + O_(q,z,α)(n).

The logarithm of |M_n|∞ |M_n|₂ is therefore at most n²(13 log P−21 log D)/8+O(n). This is negative for large n, contradicting |M_n|∞ |M_n|₂≥1 for a nonzero ordinary integer. The estimates directly adapt [Zudilin, equations (3)–(10)](https://arxiv.org/abs/math/0506086).

## Application to a growing repeated block

Let ξ be the unique rational affine fixed point of W, let λ=3^p/2^v be its slope (v the width, p its odd count), and let μ>0 be the rational slope of V. The point ξ is 2-adically integral. Write d=V(ξ)−ξ for the uncentered affine value of V at ξ minus ξ. With x_j the starting state of the jth W-block and z_j=x_j−ξ, the exact equations are

    z_(j+1)=μ λ^(Aj+B) z_j + d.

When d=0, V is legally followed at ξ (its image is 2-adically integral) and returns to ξ. Each W also returns to ξ. The infinite parity tail (1) is therefore that of ξ; uniqueness of a 2-adic source for an infinite parity sequence gives x₀=ξ. Uniqueness follows directly from the parity-word bijection modulo every 2^L.

Suppose d≠0 and λ>1. Dividing through by the successive products in the recurrence gives, in the 2-adics,

    z₀=−d μ^(−1) λ^(−B) T_(λ^A)(μ^(−1) λ^(−A−B)).

Indeed the remainder tends to zero because all z_j are 2-adically integral and |λ|₂>1. The lemma applies: P=3^(pA), D=2^(vA), with P>D and P^13<D^21 since p≤v and 3^13=1594323<2097152=2^21. Thus z₀ cannot be rational.

It remains to consider λ<1 for positive rational input of odd denominator. The odd-input frequency along (1) is p/v, also along partial stages since each stage has length O(j) versus total length of order j². The denominator of every positive shortcut state divides the fixed initial odd denominator D₀. On a nonperiodic orbit the first N states are distinct, giving a reciprocal sum at most D₀ Σ_(i≤N)1/i=O_(D₀)(log N) by discreteness. The exact logarithmic product for T yields

    log T^N(x₀)/N → (p/v) log 3−log 2<0,

contradicting T^N(x₀)≥1/D₀. The possibility λ=1 never occurs for a nonempty word. Finite prepending or deletion preserves the rational-source exclusion by the rational affine word map.

Finally, eventually quadratic even positions have eventually positive, affine gaps between successive even letters; hence their suffix is (1) with W the odd letter and V the even letter. Equivalently the 2-adic identity −(x+1)=Σ_(j≥0)3^j(2/3)^(d_j) over even positions d_j is obtained by iterating the two affine maps on x+1. A quadratic d_j reduces that sum directly to (2).
