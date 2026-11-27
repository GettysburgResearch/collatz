# Large denominator fractions for unbounded clusters of clock defects

**PROPOSED written theorem.** Arbitrarily many signed terms are permitted in finitely many exponent rectangles of sublinear diameter. The same largest-gap lower bound and fixed clock-gcd grid apply as in the fixed-term toric window estimate. The number of raw terms may grow linearly in the odd period. A fixed number of macroscopic centers is still required. The input is the moving-target outside-place gcd theorem of Grieve and Wang. This note uses rational coefficient heights throughout.

## Moving sparse estimate

Let p tend to infinity, \(D=2^A-3^p>0\), and \(A=O(p)\). Let
\[
 Z=\sum_{i=1}^N c_i 2^{a_i}3^{b_i}
\]
be a nonzero integer, with fixed N, integer exponents of absolute value \(O(p)\), and nonzero rational coefficients that may vary with p but satisfy \(\max_i h(c_i)=o(p)\). Here \(h(a/b)=\log\max(|a|,|b|)\) in lowest terms. Write \(R_3=\max b_i-\min b_i\). Then
\[
 \limsup\left(\frac{\log\gcd(D,Z)}{\log D}-\frac{R_3}{p}\right)\le0.\tag{M1}
\]
The binary and integer-direction versions replace the ternary projection by the corresponding projection of the exponents and determinant vector \((A,-p)\). Every accumulation point of the gcd fraction is rational. If \(\gcd(A,p)=g\) is fixed, it belongs to \(\{0,1/g,\ldots,1\}\).

The fixed-coefficient proof in the companion toric-window manuscript descends to a minimal *fixed* translate. Varying small coefficients can give relations only up to sublinear height, so such a descent alone would not prove (M1).

**Arithmetic input.** Grieve–Wang, Theorem 3.1, applies over a number field to coprime moving polynomials of fixed positive degrees at S-unit coordinates, with polynomial heights little-o of the maximum coordinate height. For any positive tolerance it gives either the outside-S gcd bound on an infinite subsequence or a moving exceptional relation. In its proof, equation (3.36) and Proposition 3.5 express the latter by a fixed nontrivial character whose height is little-o of the maximal coordinate height along an infinite subsequence. This is the outside-S result that does not require a condition at the origin. We normalize one coefficient of each polynomial to one before applying it. In this application all individual coefficient heights, including the two removed scalars, are little-o of the scale. [Grieve and Wang, Transactions of the AMS, Theorem 3.1 and equations (3.35)–(3.36)](https://arxiv.org/pdf/1902.09109) · [Published article](https://doi.org/10.1090/tran/8220)

**Proof.** Start on a subsequence on which the gcd fraction, normalized spans, and all normalized dyadic and ternary valuations of \(U=2^A3^{-p}, L_i=2^{a_i}3^{b_i}\) converge. Let \(P=(U,L_1,\ldots,L_N)\). On the free character group \(M=\mathbb Z^{N+1}\), form the homomorphism
\[
 \ell(e)=\lim (v_2(P^e),v_3(P^e))/p\in\mathbb R^2 .
\]
Its kernel is saturated, since its quotient embeds in a torsion-free group. Extend a basis of this kernel to an integral basis of M. The kernel basis evaluates at S-units of height o(p) for \(S=\{\infty,2,3\}\). Denote the complementary S-unit coordinates by t. For every fixed nonzero character of t, at least one of its two normalized valuations has a nonzero limit. Its height therefore has a positive linear lower bound, also on every further subsequence. The maximum coordinate height of t is comparable with p, because the ternary valuation of U is −p. This establishes the nondegeneracy required by the moving theorem, including all further subsequences.

In the complementary lattice the class of U is q times a primitive vector for a fixed positive integer q. Make that primitive vector the coordinate V by a further integral change of basis. Evaluation and the inverse basis change give
\[
 U=c V^q,\qquad L_i=d_i t^{w_i},
\]
where c and all \(d_i\) are moving rational S-units of height o(p), and the vectors \(w_i\) are fixed. In the Laurent polynomial ring in t put \(f=cV^q-1,\ z=\sum_i c_i d_i t^{w_i}\). Its specialization at the actual coordinates equals the specified nonzero integer Z. For each p, let G be the monic greatest common divisor of f and z, up to Laurent units. It is a polynomial in V with nonzero constant coefficient and degree j at most q. The reason is that all prime factors of f in the rational Laurent ring are its univariate factors. Pass to fixed j.

All coefficients of G, of \(f'=f/G\), and of \(z'=z/G\) have height o(p). To see the factor claim, clear the denominator of c in f, giving a primitive integer binomial with both coefficient heights o(p). Choose primitive integer factors. The absolute value of each leading coefficient is bounded by the original leading coefficient and every root has modulus \(|c|^{-1/q}=\exp(o(p))\). Their fixed degrees bound all coefficients by elementary symmetric polynomials in these roots times the leading coefficient; rational monic normalization costs o(p). To see the quotient claim, multiply z by a fixed Laurent monomial making its powers nonnegative and divide by monic G in V. There are a bounded number of coefficient operations in fixed degrees. The remainder is zero because G has nonzero constant term and divides in the Laurent ring. This proves the assertion on coefficients and bounds all resulting supports independently of p.

Take the complementary factors as a coprime pair, clearing the monomial in the second factor. No coordinate variable divides the first factor, so polynomial coprimeness holds. Pass to constant degrees on a subsequence. If either polynomial is constant, its outside-S gcd contribution is o(p) by its scalar height. Otherwise apply the cited theorem to the normalized pair. The exceptional alternative is impossible by the positive linear height of every nonzero fast character. To obtain the bound along the retained sequence, apply the theorem on any putative infinite subsequence where the gcd is at least a fixed positive multiple of p. Its positive tolerance can be chosen smaller than that multiple divided by the fixed coordinate-height upper constant. This contradiction gives
\[
 N_{\gcd,S}(f'(t),z'(t))=o(p).
\]
Multiplication by an S-unit monomial leaves this quantity unchanged. The cost of normalizing two moving rational scalar coefficients is at most their combined height, hence o(p).

At every prime outside S, write the two evaluated factors as G times their quotients and take the positive part of the minimum valuation. Summation bounds \(\log\gcd(D,Z)\) by \(h(G(V))+o(p)\le jh(V)+o(p)\). Since \(U=cV^q\) and \(h(U)=A\log2\), this is \((j/q)A\log2+o(p)\). Conversely the deficiency of the outside-S gcd relative to \(f(t)=D/3^p\) is the sum of positive parts of \(v(f')-v(z')\). It is at most the numerator height of \(f'(V)\) plus the total possible outside-S denominator cost of \(z'\). The latter is o(p), by the individual coefficient heights and the S-unit coordinates. The former is at most \((q-j)h(V)+o(p)\). Two fixed logarithms give \(\log D=A\log2-O(\log p)\). Hence the gcd fraction tends to j/q on this subsequence. [Matveev](https://doi.org/10.1070/IM2000v064n06ABEH000314)

For each particular p, freeze these moving rational polynomial coefficients and replace each fast variable \(t_k\) by \(t_k y^{v_3(t_k)}\). This is a Laurent polynomial identity; no assertion about valuations of sums is needed. The exponent of term i of z becomes \(b_i-v_3(d_i)=b_i+o(p)\), uniformly in the fixed number of terms. The image of G has width \(j|v_3(V)|=j(p+o(p))/q\) and divides the image of z, which is nonzero at y=1. Additivity of Laurent widths gives \(j/q\le\lim R_3/p\). The same argument works with any fixed integer linear combination of the two valuations. Finally, a root of an irreducible factor of \(c V^q-1\) of degree s has norm giving \(q\mid s v_2(c),\ q\mid s v_3(c)\). But \(v_2(c)\equiv A\pmod q\) and \(v_3(c)\equiv-p\pmod q\). Thus \(j/q\) belongs to \(\frac1{\gcd(q,A,p)}\mathbb Z\), even though c varies. Any initially chosen limit persists on the retained subsequence. This proves (M1), rationality and the fixed-g grid.

## Compressing an unbounded number of terms

Suppose instead Z has K signed unit monomials, with \(\log(1+K)=o(p)\). Partition their exponent pairs into at most a fixed N sets, each contained in an axis-parallel rectangle of binary width o(p) and ternary width o(p). For each nonempty cluster, subtract its two coordinate minima. The coefficient that remains after factoring the representative monomial is an integer satisfying
\[
 |c_i|\le K\,2^{o(p)}3^{o(p)} .
\]
Discard zero coefficients, pass to fixed actual count, and apply (M1). At least one cluster survives since Z is nonzero. The ternary span of the retained representatives is at most the original span. This proves (M1) for the clustered sum and proves the residual grid and spectrum. No uniformity in the number of rectangles is asserted.

For a positive rational accelerated Collatz word let the cyclic window residual, after a largest-gap cut, have pairs
\[
 (E_i+u-b_*,p-h-i),\qquad (E_{i+v}-b_*,p-h-i)\quad (i\in J).
\]
Here p is the odd period, A the native clock, u the common native total of a length-v window, h its longest cyclic defect spacing, \(b_*=\min(u,E_v)\), and \(d=D/\gcd(D,C)\) the full common denominator of all phases. The residual is nonzero and divisible by \(\gcd(D,C)\) by the prior cyclic difference and oddness argument. If its **two-dimensional exponent pairs** satisfy the rectangle hypothesis, the full-cycle bounds (T1) and (T2) follow with precisely the same proof, including coprime full leading denominator. The raw count is at most 2p, so its logarithm is negligible. In this setting, finitely many shrinking two-dimensional rectangles also imply that there are only o(p) exceptional indices. Thus this is a genuine unbounded-cardinality regime, with sparse macroscopic geometry. [Weaver, Mahler and Wren, Paper 22 v4](https://rstation.ai/problems/collatz/papers/22/v4)

## A family with no bounded-exception window

Take growing upper convergents A/p to \(\log_2 3\) and put \(k=\lfloor\sqrt p\rfloor\). Choose an arbitrary word on \(\{2,3\}\) on k consecutive gap positions starting at \(\lfloor p/2\rfloor\). Its excess above k is s, with \(k\le s\le2k\). Set \(e_0=1+A-p-s\) and set all remaining gaps to one. The unique giant gap forces primitive period p. For \(v=u=1\) there are exactly k+1 exceptional starts. Their ternary coordinates concentrate near two locations, and the native coordinates for the k-letter patch vary by at most 3k. The isolated giant row adds just two points. Thus (M1) applies. Since the clock gcd is one, the full reduced denominator satisfies \(\log d/\log D\to1\) for every choice of the entire k-letter patch. The full drift tends to zero, so every positive rational phase tends uniformly to infinity by the positive product identity.

For every proper v and integer u, the number of exceptions tends to infinity uniformly. Replacing v by p−v and u by A−u preserves this count after rotation, so take \(v\le p/2\). The v windows containing the giant gap have total strictly larger than every window not containing it because its excess is greater than all other excess combined. Thus if \(v\ge k/2\) there are at least \(k/2\) exceptions. Otherwise at least \(k-v+1>k/2\) windows lie fully in the patch, each having total at least 2v. At least \(p-k-2v\) avoid both the patch and the giant, each with total v. Either value of u therefore leaves more than k/2 exceptions for large p. The original fixed-count window theorem does not apply at any proper lag in this family.

The growing-rank switch example in the companion toric manuscript bars a period-independent positive exponential denominator rate when raw exceptions are allowed to grow arbitrarily slowly without the rectangle assumption. For arbitrary integer cycles there is no established theorem that produces a lag with finitely many such rectangles. The first unsupported global inference would be precisely that existence assertion.
