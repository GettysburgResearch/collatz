# One variable odd rank with unrestricted marker sizes

Fix an integer $M\ge2$. Let a primitive positive rational odd cycle have $p=Md$ odd steps and shortcut period $h$. In each of its $M$ chronological cells of $d$ consecutive odd steps, suppose the first $d-1$ division exponents are the same word $U$ and the final exponent $a_j$ may vary. The positive exponents, the word $U$ and the marker sum $\sum a_j$ may all vary with the cycle. Write $q$ for the entire reduced denominator and $\gamma=\log_2 3$. As $d\to\infty$,
\[
 \log_2 q\ \ge\ \frac{h-(\gamma-1)p}{M}-o(h),
 \qquad
 \liminf\frac{\log_2 q}{h}\ge\frac1{\gamma M}.                          \tag{1}
\]
No bound on $h/p$ from above is required. For nontrivial ordinary cycles the positive lap product gives $h<2p$, so unbounded shortcut periods force $d\to\infty$ at fixed $M$. This rules out arbitrarily long ordinary cycles of this form, including cases with markers a positive fraction of the entire clock. A proposed ordinary odd rotation of fixed order $M$ whose comparisons vary along a single residue class modulo $d=\gcd(\ell,p)$ has exactly this form after choosing the cell seam. The other $d-1$ residue circles must be constant.

Armstrong's shared-background denominator law already gives this cell factorization, identifies its marker Fourier modes, and gives an effective resultant bound involving the marker total. It implies finiteness at fixed $M$ and fixed marker total and gives a growing-copy condition when the marker average is bounded. Here the marker total may be comparable to $h$ or larger than any fixed multiple of $d$. A fixed-dimensional unit-gcd argument controls such moving markers at an ineffective onset. The ordinary exclusions of two and three mismatches and the finiteness for exactly four mismatches are prior results. [Armstrong, shared-background denominator law](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/results/shared-background-denominator-law/README.md) · [Prior rotation counts and open question](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-growth.md)

## The common carry and the marker sum

Let $A$ be the sum of $U$, let $H_j=A+a_j$ be the cell totals and $B_j=\sum_{k<j}H_k$. The cell map is
\[
              2^{H_j}x_{j+1}=3^d x_j+C.
\]
Its carry $C=\sum_{i=0}^{d-1}2^{E_i}3^{d-1-i}$ only uses the prefix sums $E_i$ of the common $U$, including $E_0=0$ and $E_{d-1}=A$. Put
\[
 D=2^h-3^{Md}>0,\qquad S=\sum_{j=0}^{M-1}2^{B_j}3^{d(M-1-j)} .
\]
Thus $D x_0=C S$, $q=D/\gcd(D,CS)$, and $q\ge[D/\gcd(D,S)]/C$. Since $E_i\le A-(d-1-i)$ and $A<h/M$,
\[
                     \log_2 C\le A+(\gamma-1)(d-1)+\log_2 d.          \tag{2}
\]
It suffices to prove that $\log_2[D/\gcd(D,S)]\ge2h/M-o(h)$. The nonconstant vector of positive markers is essential at this step.

## Two surviving marker frequencies

Write $X=2^h3^{-p}$ and $Y_j=2^{B_j}3^{d(M-1-j)}$. Follow any subsequence realizing a candidate lower limit and choose a fixed connected torus translate of minimal dimension carrying infinitely many of these rational unit points. Choose its origin at a retained positive point. Laurent's theorem permits removal of finitely many points in each further proper closed locus. Write $X=cT^n$ and $Y_j=c_j T^{m_j}Z^{v_j}$ in integral characters, with $c,c_j,T,Z$ positive at the retained real points, $n\ge1$, and all coordinates rational units outside two and three. Here $X$ varies because $h\to\infty$. The polynomial $F=cT^n-1$ is squarefree. A root of $F$ survives if at least one coefficient of the Laurent polynomial $G=\sum c_jT^{m_j}Z^{v_j}$ in the $Z$ monomials is nonzero there. If $J$ of its $n$ roots survive then
\[
                   \log_2[D/\gcd(D,S)]=(J/n)h+o(h).                  \tag{3}
\]
The fixed-translate proof applies unchanged: divide out the common root polynomial, use Levin's multivariable gcd theorem for the coprime residuals, and use $\log_2 D=h+o(h)$ from two-logarithm separation. Valuation sums of the two monic factors outside two and three add to $\log D$ and have complementary degree height bounds whose sum is $h\log2+O(1)$. All numerical prime powers are retained. [Fixed-translate proof, including the height normalization](SPARSE_DENOMINATORS.md) · [Laurent](https://doi.org/10.1007/BF01388597) · [Levin](https://doi.org/10.1007/s00222-018-0831-z)

Within a given $Z$ group, compare $Y_j/Y_k$ at three with $X=cT^n$. Since $d\to\infty$ and $p=Md$, this gives the exact fixed-character relation
\[
                   (m_j-m_k)/n=(j-k)/M .                              \tag{4}
\]
In particular all exponents in one group are distinct modulo $n$. If two or more groups occur, the smallest has $t\le M/2$ terms. Its nonzero coefficients at a positive root $\lambda=c^{-1/n}$ multiply distinct bases as the root is varied through $\lambda\zeta^k$, with $\zeta$ primitive of order $n$. A Vandermonde determinant forbids $t$ successive zeros. Counting cyclic windows gives $J/n\ge1/t\ge2/M$.

If there is just one group, (4) gives $M\mid n$. At the positive root the ratio of the $j$th coefficient to the zeroth is
\[
 \frac{c_j\lambda^{m_j}}{c_0\lambda^{m_0}}
   =\frac{Y_j}{Y_0} X^{-j/M}=2^{B_j-jh/M}.
\]
At the $k$th root the common phase factor leaves the Fourier transform of this vector on $\mathbb Z/M$. Its mean is positive. Some nonzero frequency must also survive, since a vector with only its mean is constant by Fourier inversion. A constant vector would give $B_j=jh/M$ for every $0\le j<M$ and hence equal totals $H_j$, including the final one since $B_M=h$. That would repeat the entire cell and contradict primitivity. Consequently $J/n\ge2/M$ in both cases. Equations (2)–(3) imply (1), since $h>\gamma p$.

## Retaining the full marker Fourier support

Let $e$ be the number of nonzero Fourier coefficients on $\mathbb Z/M$ of the actual positive vector $a_j^*=2^{B_j-jh/M}$ (the symbol $e$ in this paragraph is a count, not a division exponent). It can vary with the cycle. Then, uniformly in the unrestricted markers at fixed $M$,
\[
 \log_2[D/\gcd(D,S)]\ge(e/M)h-o(h),\qquad
 \log_2 q\ge(e/M)h-\log_2 C-o(h).
\]
In any one fixed $Z$-group choose a supported index $k$ and divide by its coefficient at the corresponding root. The same ratio calculation as above shows that its vanishing at root number $t$ is equivalent to that of $\sum_{j\in I}a_j^*\exp(2\pi itj/M)$: the two sums differ only by a nonzero scalar. This statement uses ratios only *within* each group. The indicator that at least one group survives is $M$-periodic in $t$ and also $n$-periodic by (4). Its mean over either period is therefore the same. A nonzero Fourier sample of the full vector guarantees that at least one restricted group survives, even though different groups need not share any coefficient normalization on the torus. Hence $J/n\ge e/M$ throughout the retained subsequence. Apply (3) on every subsequence that could violate the inequality.

In particular if $\gcd(h,M)=1$, the dyadic valuations $B_j-jh/M$ are pairwise distinct modulo one. Every twist retains a unique least valuation, giving $e=M$ even for composite $M$. The numerical value $e$ is computable over $\mathbb Q$ as $M$ minus the degree of $\gcd(2^hT^M-1,\sum 2^{B_j}T^j)$. The shared-background work already gives the marker Fourier interpretation. Here the term discarded after retaining this fraction of the binomial roots has logarithmic size $o(h)$ for arbitrary growing marker totals at fixed $M$.

## Prime order

For $M$ prime, all roots survive. For a singleton $Z$-group this is immediate. In any other group, (4) for two distinct indices gives $M\mid n$. After removing its common scalar and monomial at the positive root, the group's coefficient vector on $\mathbb Z/M$ has entries proportional to $2^{B_j-jh/M}$ at its supported indices $j$, and zero elsewhere. This follows by taking ratios to any supported index in the same calculation above, even if the zeroth index is in a different group.

If $M\nmid h$, the dyadic valuations $B_j-jh/M$ are pairwise distinct modulo one. A root-of-unity twist does not change them. Every group's sum therefore has a unique least valuation at any extension of the dyadic place and cannot vanish. If $M\mid h$, the entries are rational up to their common scalar. A polynomial of degree at most $M-1$ with rational coefficients that vanishes at a nontrivial $M$th root is a multiple of $1+T+\cdots+T^{M-1}$ by irreducibility. A proper group has a zero coordinate and a nonzero coordinate. The one possible full group has nonconstant entries by primitivity. Neither is a constant vector. The trivial frequency is nonzero by positivity. Thus (3) yields the stronger prime-order estimate
\[
               \log_2q\ge h-\frac{h+(\gamma-1)p}{M}-o(h).
\]
For $M=2$ it agrees with (1). For fixed prime $M\ge3$ it improves the leading exponent.

With at most one varying residue class the argument allows an arbitrary number of individual mismatches along its $M$-circle. With two or more varying classes, their different common carries enter additively in the full numerator. Extracting them as one scalar factor, as above, would require a further divisibility argument. The [six-mismatch theorem](ROTATION_DENOMINATORS.md) treats every order and any number of varying ranks through six mismatches. Whether every bounded-order rotation must have a diverging mismatch count remains open.


[Finite arithmetic controls](check_one_variable_rank.py) check 999 primitive marker words at ten cell counts, 2,997 partitions, every actual odd cell identity, and the special full-support cases. Twenty examples retain a proper Fourier support. [Archived counts](../../../reports/astra-infinite-descent-20261127/cycles/ONE_VARIABLE_RANK.json)
