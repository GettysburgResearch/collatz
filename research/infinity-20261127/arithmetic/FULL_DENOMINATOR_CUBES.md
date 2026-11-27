# A cubeclass obstruction at the complete denominator

**PROPOSED, with two published Thue bounds.** Let \(r\) be the affine dimension of the adjacent-product classes modulo rational cubes on one primitive positive rational odd cycle of period \(P\) and complete reduced denominator \(d\). Write \(\omega_1(d)\) for the number of distinct primes dividing \(d\) that are \(1\bmod3\). Then
\[
                 P\le40\cdot5^r3^{\omega_1(d)}.                            \tag{1}
\]
The factor 40 can be replaced by 20 if \(P\) is odd. For an ordinary cycle the sharper bounds are \(4\cdot5^r\) and \(2\cdot5^r\) respectively. In particular every nontrivial positive ordinary cycle has affine cubeclass rank at least 16 among its adjacent products. This concerns the quotient by arbitrary cubes and complements the [squareclass bound](RANK_CERTIFICATE.md).

A family with \(r=o(\log P)\) must have \(\omega_1(d)\ge(1-o(1))\log_3 P\). Arbitrarily high powers of fixed denominator primes, and arbitrarily many distinct primes \(2\bmod3\), cannot by themselves meet this requirement. This statement uses the reduced denominator of the complete physical return. It imposes no prescribed rational denominator on unrestricted words and gives no upper bound on the rank of an ordinary counterexample.

## From one ordinary numerator edge to a binary cubic

Use the [denominator normalization](FULL_DENOMINATOR_PELL.md). For one edge \(2^a n'=3n+d\), both odd numerators are coprime to \(3d\) and to each other. Write \(n=S u^3,\ n'=T v^3\), with \(S,T\) the unique positive cubefree representatives. Split \(a=3q+t,\ 0\le t<3\); put \(A=3S,\ B=2^tT,\ U=u,\ V=2^qv\). Then
\[
             B V^3-AU^3=d,\qquad \gcd(ABUV,d)=1.                         \tag{2}
\]
The pair \(S,T\) permits at most two values of \(t\) on physical edges. Indeed \(2^a n'/d=1+3n/d\) in the unit group modulo nine, and \(n/d\) is a unit there. The right side is either 4 or 7. In the quotient by \(\{1,-1\}\), every unit cube is trivial, and the class of two has order three. Thus \(t\) must put the fixed class of \(T/d\) in one of two prescribed classes.

For \(d=1\), Bennett's Theorem 1.1 states that for fixed nonzero integer coefficients \(A,B\) and \(k\ge3\), \(|B V^k-AU^k|=1\) has at most one positive integral solution. Apply it at \(k=3\). Each \(S,T,t\) therefore accounts for at most one source \(n=S U^3\). Its physical successor is determined. This also proves, for arbitrary \(k\ge3\), the injectivity of the ordinary edge code consisting of the two endpoint classes modulo \(k\)-th powers and \(a\bmod k\). [Bennett, J. Reine Angew. Math. 535 (2001), Theorem 1.1](https://personal.math.ubc.ca/~bennett/B-Crelle2.pdf)

For general \(d\), fix \(S,T,t\) and take \(R=V/U\bmod d\) in (2). It satisfies \(BR^3=A\bmod d\), with at most \(3^{\omega_1(d)}\) possible residues. At \(p\mid d\) the coefficients and the candidate root are units and \(p\ne2,3\). The number of cube roots at \(p\) is at most \(\gcd(3,p-1)\) in the cyclic multiplicative group. Each root lifts uniquely to the required prime power since the derivative \(3BR^2\) is nonzero modulo \(p\). The Chinese remainder theorem gives the stated full-modulus count.

For a fixed representative \(R\), write \(V=RU+dZ\) with \(Z\in\mathbb Z\). Equation (2) becomes \(G(Z,U)=1\) for the integral binary cubic
\[
 G(Z,U)=Bd^2 Z^3+3BRd Z^2U+3BR^2 ZU^2+\frac{BR^3-A}{d}U^3 .
\]
The univariate \(G(Z,1)\) has three distinct complex roots: it is an invertible affine change of \(BV^3-A\) followed by division by \(d\), with \(A,B,d\ne0\). Bennett's Theorem 1.4 therefore gives at most ten integer pairs \((Z,U)\), hence at most ten source values at this root. His general Corollary 1.5 alone would count all denominator primes; the unit condition for this diagonal form removes the primes \(2\bmod3\) from (1). [Bennett, Trans. Amer. Math. Soc. 353 (2001), Theorem 1.4 and Corollary 1.5](https://personal.math.ubc.ca/~bennett/B-Cubic.pdf)

## Counting endpoint classes without bounding their primes

Prime exponents modulo three identify positive rational cubeclasses with a direct sum of copies of \(\mathbb F_3\). Let \(v_i=[n_i]\); the adjacent numerator products \(v_i+v_{i+1}\) lie in some affine space \(w+L\) with \(\dim L=r\), because replacing physical products by numerator products translates every class by \([d^2]\). Starting at phase zero, the recursion puts each even-index \(v_i\) in \(v_0+L\) and each odd-index \(v_i\) in \(w-v_0+L\). If \(P\) is odd, the two cosets coincide at the seam.

Choose \(r\) prime coordinates on which projection of \(L\) is injective. Its projection is also injective on either of the two fixed translates. At one pivot prime the ordered source and successor coordinates have at most five choices:
\((0,0),(0,1),(0,2),(1,0),(2,0)\).
Indeed a positive prime cannot divide both \(n_i\) and \(n_{i+1}\); a nonzero mod-three coordinate means that it does divide the numerator. Thus after fixing the index parity there are at most \(5^r\) ordered class pairs \(S,T\). Accounting for both parities, the at most two values of \(t\), and the Thue count at (2) proves (1). Primitive phases correspond to distinct sources. The same count for \(d=1\) uses the binomial uniqueness theorem. Since \(4\cdot5^{15}=122{,}070{,}312{,}500<137{,}500{,}000{,}000\), the [published period comparison](RANK_CERTIFICATE.md) excludes \(r\le15\).

For an injective ordinary finite prefix the same argument applies after discarding at most its first odd edge, the only one that might start at a multiple of three. Its number of distinct remaining odd departures is at most \(4\cdot5^r\) for its complete product list. For arbitrary sparse edge sets, one may instead suppose their source and target classes lie in two specified translates of the same \(r\)-space. Their count is at most \(20\cdot5^r 3^{\omega_1(d)}\) at fixed \(d\), or \(2\cdot5^r\) at \(d=1\), assuming the odd sources and targets are units at three. A bound on just the products of sparse edges does not imply the alternating-coset property without the intervening transitions.
