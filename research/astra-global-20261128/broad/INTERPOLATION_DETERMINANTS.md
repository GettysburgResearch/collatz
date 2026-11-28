# An arbitrary-dimension test of interpolation on the greedy sums

**PROPOSED, written proof.** Let $C_e=n+1+\sum_{j<e}2^j(2/3)^{u_j}$ be the greedy sum of the [pin construction](PIN_APPROXIMATION.md). The sought pointwise bound is $v_2(C_e)\le 2.36\ldots\,e+O_n(1)$. This note tests whether multiplying the simultaneous approximations by a sparse interpolation determinant can improve the height inequality. The rows, powers and dimension are unrestricted within the family specified below.

## 1. Which rows have valuations in opposite orders?

The increasing positive real numbers $C_e$ satisfy $v_2(C_e)=e+u_e$, strictly increasing. Let $x_e$ be the state just after the $e$-th even input, for $e\ge1$. The common-prefix identity gives
$$
 3^{u_{e-1}}C_e=2^{e+u_{e-1}}(x_e+1).
$$
If the odd run immediately before this even input had positive length $g$, then $x_e+1=(3^gq+1)/2$ for a positive odd integer $q$. Consequently $v_3(x_e+1)=0$ and $-v_3(C_e)=u_{e-1}$. Select any rows $e_1<\cdots<e_s$ satisfying that positive-run condition. Their denominator exponents $u_{e_i-1}$ increase strictly, since the intervening odd counts include at least the last positive run. All ordinary orbits have infinitely many selectable rows: a tail of only one parity is impossible for a positive integer, by division by two for an all-even tail and by the finite valuation of its shifted state for an all-odd tail. Thus infinitely many positive odd runs end at even inputs.

For the rest of the argument it suffices to have numbers $0<X_1<\cdots<X_s$ in $\mathbb Z[1/3]$ with strictly increasing lists $d_i=v_2(X_i)$ and $b_i=-v_3(X_i)$. One can take $X_i=C_{e_i}$ above.

## 2. The complete valuation and positivity calculation

Choose arbitrary integer powers $0\le m_1<\cdots<m_s$. Put
$$
 V=\det[X_i^{\,j-1}]_{i,j}=\prod_{i<j}(X_j-X_i),\quad
 S=\frac{\det[X_i^{\,m_j}]_{i,j}}{V},\quad
 \lambda_i=m_{s+1-i}-(s-i).
$$
The $\lambda_i$ form a weakly decreasing sequence of nonnegative integers. Write $N_\lambda=S(1,\ldots,1)$, using the polynomial extension of the quotient to equal inputs. Let $Z=\prod_i X_i^{\lambda_i}$.

**Theorem.** For every such choice,
$$
 v_2(S)=\sum_i\lambda_i d_i=v_2(Z),\qquad
 -v_3(S)=\sum_i\lambda_i b_{s+1-i},\qquad
 S\ge N_\lambda Z>0. \tag{1}
$$
The exact denominator cost relative to the same monomial, at the prime 3, satisfies
$$
 G=\sum_i\lambda_i(b_{s+1-i}-b_i)
 \ \ge\ \sum_{i=1}^{s-1}(\lambda_i-\lambda_{i+1})i(s-i). \tag{2}
$$
The valuations in the first display follow directly from the determinant expansion. At 2 the unique permutation of smallest valuation pairs increasing $d_i$ with decreasing $m_j$. At 3 the increasing $b_i$ have a negative sign, so the unique minimum pairs both increasing lists in the same order. A unique minimum survives in the sum. Subtracting the valuations of the determinant with powers $0,\ldots,s-1$ gives (1). Summation by parts decomposes $G$ into the successive differences $\lambda_i-\lambda_{i+1}$ times the sum of the largest $i$ of the $b_j$ minus the sum of the smallest $i$. The latter difference is at least $i(s-i)$ because two entries $s-i$ positions apart differ by at least $s-i$.

The bialternant and tableau formulas identify $S$ with the Schur polynomial of shape $\lambda$ in the $X_i$. Its monomials with multiplicity are indexed by semistandard tableaux with entries $1,\ldots,s$. Each entry in row $j$ is at least $j$, since columns strictly increase. Hence the monomial for each tableau is at least the weight $Z$ obtained by filling row $j$ with $j$. There are $N_\lambda$ tableaux. This gives the real inequality in (1) directly. The underlying standard identities are stated together at the start of [Tamvakis, *The theory of Schur polynomials revisited*](https://www.math.umd.edu/~harryt/papers/schurrev.pdf).

## 3. What the product formula delivers

For positive $X_i$ as above, $3^{b_i}X_i$ is a positive integer. The individual numerator inequalities are $2^{d_i}\le3^{b_i}X_i$. Multiplying them with weights $\lambda_i$ gives
$$
 2^{v_2(S)}\le3^{\sum_i\lambda_i b_i}Z.
$$
By (1)–(2), the right-hand side is at most $3^{-v_3(S)}S/(3^G N_\lambda)$. Thus even a factor $N_\lambda$ of extra divisibility in the Schur numerator, away from 2 and 3, is covered by the archimedean growth of the Schur polynomial before any use of the denominator loss $3^G$.

In fact every fixed prime-to-six divisor that follows solely from membership in $\mathbb Z[1/3]$, positivity, real ordering and the two lists of valuations divides $N_\lambda$. To verify it, for any $p\ge5$ and $k> v_p(N_\lambda)$ choose $Y_i=2^{d_i}a_i/3^{b_i}$ with $a_i$ a positive integer coprime to 6. The Chinese remainder theorem lets one impose $Y_i\equiv1\bmod p^k$. The choices $a_i$ can be made successively large to give $0<Y_1<\cdots<Y_s$. Since the Schur polynomial has integer coefficients, its value there is $N_\lambda\bmod p^k$. This test does not prescribe the actual orbit's residues at $p$. A gain relying on those additional residues is outside the theorem.

The removed Vandermonde factor depends on the schedule $u_j$ alone: for $a<b$, $C_b-C_a=\sum_{a\le j<b}2^j(2/3)^{u_j}$. Positivity, divisibility and archimedean clustering of this difference for a given schedule hold for every choice of its root term $n+1$. In particular, the ordinary integer divisibilities of a Vandermonde matrix cannot by themselves test that the schedule is the maximizing one for a given root.

**Example.** For $m_j=L(j-1)$, the partition is $\lambda_i=(L-1)(s-i)$. Here $N_\lambda=L^{s(s-1)/2}$, by factoring the product of the ratios $(X_j^L-X_i^L)/(X_j-X_i)$ and setting all variables equal to one. The extra denominator exponent $G$ is at least $(L-1)s(s^2-1)/6$. These losses persist as the dimension grows.

The estimate covers the normalized, one-variable alternants on all the selectable greedy rows, including arbitrary sparse powers. In this family the product formula using the two valuations, real positivity and universal fixed divisors is already implied by the separate numerator estimates. In an actual trajectory, the value of $S$ may have additional non-universal prime divisibility. Mixed-coordinate determinants, row-dependent functions, simultaneous residues at other primes and the valuation ties after consecutive even inputs all require separate analysis.
