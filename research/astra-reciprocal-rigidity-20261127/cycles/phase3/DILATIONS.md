# Exact denominator exponents along symbol dilations

Fix a nonconstant cyclic binary mask \(w\) of length \(n\), weight \(u\), with \(2^n>3^u\). Replace **each letter individually** by \(l\) copies of itself to obtain \(w^{[l]}\) of length \(ln\). Write \(d_l\) for its reduced positive shortcut-cycle denominator. This differs from repeating the entire mask \(l\) times. The following finite algorithm computes the exact limit of \(\log_2 d_l/(ln)\) for each fixed mask, using the published outside-\(S\) gcd theorem stated in [BOUNDED_RUNS.md](BOUNDED_RUNS.md).

## Signed corner arrays

Put \(g=\gcd(n,u),\ N=n/g,\ U=u/g\). Cut \(w\) at the start of an odd run, with a preceding zero. At each cut site \(i\) let \(s_i\) be the ones from \(i\) up to the end. Thus \(s_{i+n}=s_i-u\) on the lifted word. Put a \(+1\) corner at \((i,s_i)\) when a run of ones starts there, and a \(-1\) corner when a run of ones has just ended. These corners occur at distinct physical sites. Group them by level
\[
 L=Ui+Ns_i .
\]
At any nonempty level choose one corner site \(i_L\). All sites \(i\) on that level satisfy \(i-i_L\in N\mathbb Z\) because \(\gcd(N,U)=1\). Put the corner's sign in slot \(r=(i-i_L)/N\bmod g\) of an array \(a_L\colon\mathbb Z/g\to\mathbb Z\), filling unused slots with zero. A slot contains at most one corner since \(0\le i<n=Ng\). Let
\[
 S=\bigcup_L\{j\bmod g:\ \sum_r a_L(r)e^{2\pi i jr/g}\ne0\}.
\]
Changing the reference slot rotates an array and preserves its Fourier support. All sites from any later cyclic cut describe the same reduced denominators and hence the same final fraction. In fact their supports agree by the monomial rotation congruence modulo the determinant. The algorithm works with any chosen initial odd-run boundary.

**Exact formula.**
\[
 \boxed{\displaystyle\lim_{l\to\infty}\frac{\log_2 d_l}{ln}=\frac{|S|}{g}.}
 \tag{1}
\]
Every surviving root order can be decided by integer polynomial remainders. Put \(A_L(Z)=\sum_{r=0}^{g-1}a_L(r)Z^r\). The entire order-\(d\) class for \(d\mid g\) survives when some \(A_L\) has nonzero remainder mod \(\Phi_d(Z)\). Thus the numerator in (1) is the sum of \(\varphi(d)\) over the surviving orders. The algorithm needs only the fixed template \(w\).

### Proof

Let \(X=2^l,Y=3^l\). The determinant is \(F(X,Y)=X^n-Y^u\). The dilated affine numerator is the integer polynomial
\[
 P(X,Y)=\sum_{(i,s_i)} \operatorname{sign}(i)\,X^iY^{s_i}.
\]
This is the block identity \(\sum X^{p}Y^{s}(Y^a-X^a)\), since a dilated run of \(a\) odds has length \(la\). Put \(Z=X^N/Y^U\). The character \((N,-U)\) is primitive in the Laurent exponent lattice. Extending it to an integral basis makes the Laurent ring \(\mathbb Q[X^{\pm1},Y^{\pm1}]\) equal to \(\mathbb Q[Z^{\pm1},W^{\pm1}]\). Distinct levels \(L\) have distinct powers of \(W\), up to changing the sign convention of \(W\). Terms at one level differ by powers of \(Z\). On \(Z^g=1\) their coefficient agrees with \(A_L(Z)\) up to a nonzero monomial. Consequently the rational irreducible factor \(\Phi_d(Z)\) divides \(P\) in the Laurent ring exactly when it divides every \(A_L\). The homogeneous binomial factor in \(F\) is
\[
 H_d(X,Y)= Y^{U\varphi(d)}\Phi_d(X^N/Y^U).
\]
It is irreducible in the Laurent ring and has no coordinate factor in \(\mathbb Q[X,Y]\). The product of all \(H_d\), \(d\mid g\), is \(F\).

Let \(B\) be the product of all nonsurviving \(H_d\). Thus \(F=B F_1,\ P=B P_1\) in \(\mathbb Z[X,Y]\), by Gauss's lemma. The cofactors \(F_1,P_1\) are coprime. At \((2^l,3^l)\), every proper torus translate containing such a point imposes a nontrivial relation \((2^a3^b)^l=c\) for fixed integers \(a,b\) and a fixed \(c\). Unique prime factorization shows it can contain at most one \(l\). The outside-\(\{\infty,2,3\}\) gcd theorem therefore gives \(\log\gcd(|F_1(2^l,3^l)|,|P_1(2^l,3^l)|)=o(l)\). The factor \(F_1(2^l,3^l)\mid2^{nl}-3^{ul}\) is prime to 6. Finally, \(2^N>3^U\) is fixed. Each surviving \(H_d(2^l,3^l)=2^{lN\varphi(d)}(1+o(1))\), as \(\Phi_d\) is monic and \(3^{lU}/2^{lN}\to0\). Taking the ratio to \(nl\) proves (1). This fixed-template theorem requires no two-logarithm lower bound. [Levin and Wang, Theorem 1.13(a)](https://doi.org/10.1515/crelle-2019-0033)

## Primitivity forces the surviving characters to be faithful

The top occupied level has only positive corners. Each negative corner at the end of a nonempty run has level strictly below the positive corner at its start, by \((N-U)a\) for that run length \(a\). Hence \(0\in S\).

Suppose the template is primitive. Then \(S\) generates the whole dual group \(\mathbb Z/g\). Indeed any \(a\) annihilating \(S\) is a period of each \(a_L\) by Fourier inversion. Therefore translating every corner of the lifted word by \((aN,-aU)\) preserves its sign and corner status, including across the seam \((n,-u)\). This makes the signed jump sequence \(w_i-w_{i-1}\) periodic under translation by \(aN\). Then \(w_{i+aN}-w_i\) is constant, and summing around the cycle makes it zero. A nonzero \(a\bmod g\) would give a proper period. Conversely a template period \(aN\) produces this invariance, since the weight in its cyclic length-\(aN\) windows is then \(aU\). The exact stabilizer of the arrays is the corresponding period subgroup.

Because each survivor order contributes its entire Galois orbit, the least common multiple of the surviving orders is \(g\). This gives the following exact consequences for primitive templates, regardless of how large the number of runs is.

- When \(g=1\) or \(g\) is prime, the exponent in (1) equals 1.
- For \(g=p^a>1\), its exponent is at least \((1+\varphi(g))/g\). The extra 1 is the order-one character.
- More generally, for \(g>1\) let \(q\) run through the exact prime powers \(p^{v_p(g)}\). The exponent is at least
  \[
  \frac{1+\sum_{q\parallel g}\varphi(q)-1_{\{g>2,\ 2\parallel g\}}}{g}.
  \]
  Here the sum uses one exact prime power for each prime dividing \(g\). To see the bound, assign each exact prime power to a surviving order divisible by it, which exists by the lcm assertion. All its assigned totients multiply to at most the totient of that order by multiplicativity and monotonicity along divisibility. A product of two or more integers all at least 2 dominates their sum. The sole possible totient 1 comes from \(2\parallel g\), and may be absorbed into one other order at zero cost if \(g>2\). Add the order-one character separately.

For \(10110100\), \(g=4\) and the survivors have orders 1 and 4. The exponent is \(3/4\), attaining the prime-power lower bound. The explicit polynomial factors appear in [BOUNDED_RUNS.md](BOUNDED_RUNS.md). The theorem classifies the ray of dilations of each fixed mask. Its limiting estimate has no claimed uniform onset as the template itself varies.
