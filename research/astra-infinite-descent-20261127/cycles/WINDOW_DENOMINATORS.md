# Exponential rational denominators for sparse native window-sum errors

Let a positive primitive rational odd cycle have common reduced denominator $q$, $p$ odd steps, $h$ total divisions, $D=2^h-3^p>0$, and native division counts $e_i\ge1$. Put $E_0=0$, $E_{i+1}=E_i+e_i$ and extend $E_{i+p}=E_i+h$. Consider **any** $0<\ell<p$ and any integer comparison $K$, both permitted to vary with the cycle. Suppose the length-$\ell$ clock $t_i=E_{i+\ell}-E_i$ differs from $K$ at no more than $s$ cyclic dates for some fixed $s\ge1$. Along growing periods with $p\asymp h$,
\[
                       \liminf \frac{\log_2q}{h}\ge\frac1s.              \tag{1}
\]
If $h,p$ are coprime throughout, the limit is one. The same holds when the common clock factors have no fixed prime divisor on any infinite subsequence. This is a pointwise rational denominator conclusion for sparse *dates*. Each date can contribute two distinct signed powers of two with arbitrarily large separation. The physical spread and the individual division exponents are unrestricted.

Weaver, Mahler and Wren's Paper 22/v4 already proves the sparse-multiple gap lemma giving integer finiteness, allowing signed cancellations and arbitrary clock gcd. Their explicit results give stronger, effective growth estimates on Farey and upper windows; complementary lags cover the corresponding lower windows. We use their fixed-torus argument and retain a positive proportion of all binomial roots to obtain (1) for the full rational orbit. The qualitative absence of bounded-error integer families follows directly from their gap lemma and the native comparison. [Paper 22/v4, Theorem 1, Lemma 3 and Theorems 4–5](https://rstation.ai/problems/collatz/papers/22/v4)

## Native signed comparison and its exact denominator

The recurrence $2^{e_i}x_{i+1}=3x_i+1$ gives
\[
 \Psi_i=2^{t_i}x_{i+\ell}-2^Kx_i,
 \qquad 2^{e_i}\Psi_{i+1}=3\Psi_i+2^{t_i}-2^K.                         \tag{2}
\]
For large increasing $p$ there is at least one matching date, so $1\le K<h$. Any equality $\Psi_i=0$ would identify the odd parts of the two distinct reduced numerators; primitivity forbids this at **every** cut. In particular at least one date mismatches, since a homogeneous cycle of multiplier $3^p/2^h$ would have $\Psi_i=0$. Also $2^{t_i}x_{i+\ell}=3^\ell x_i+A_{i,\ell}$ for an integer native carry. Hence the positive denominator of $\Psi_i$ in lowest terms is exactly
\[
                     Q=\frac{q}{\gcd(q,|2^K-3^\ell|)}.                  \tag{3}
\]
It is common to every cut. The unrolled identity is
\[
        D\Psi_0=\sum_{i:\,t_i\ne K}3^{p-1-i}2^{E_i}
                       (2^{t_i}-2^K)\ne0 .                              \tag{4}
\]
The right side has at most $2s$ signed integer atoms, with dyadic exponents in $[0,2h]$. Rotate the cut to put all support dates inside a nonwrapping arc of width at most $(1-1/s)p$: the largest cyclic gap has length at least $p/s$. The ternary exponents then occupy an interval of that same width, and occur at no more than $s$ distinct levels.

## Recovering the proportion of uncancelled binomial roots

Take an arbitrary subsequence on which $\log_2Q/h$ converges. Pass further to keep the number, signs and pairing of the atoms fixed. Denote them by $Y_j=2^{u_j}3^{v_j}$ and put $X=2^h3^{-p}$. All coordinates have height $O(h)$ and are units outside $S=\{\infty,2,3\}$. Use a connected algebraic-torus translate of minimal dimension containing infinitely many of these points; a fixed positive rational candidate serves as origin. On the retained sequence a proper algebraic subset contains at most finitely many points, since Laurent's theorem decomposes its intersection with the finitely generated unit group into finitely many subgroup translates. In integral character coordinates on this fixed translate, write
\[
 X=cT^d,\qquad Y_j=c_j T^{m_j} Z^{a_j},
\]
where $T$ is primitive, $d\ge1$, and $c,c_j$ are fixed rational $S$-units. A constant $X$ is impossible on growing $h$ by its dyadic valuation. The points and their coordinate heights are $O(h)$; specifically $\operatorname{ht}(T)=(h\log2)/d+O(1)$. The last equality uses $D>0$. [Laurent, multiplicative exponential Diophantine equations](https://doi.org/10.1007/BF01388597) · [Fixed-translate denominator proof and sources](SPARSE_DENOMINATORS.md)

Let $F=cT^d-1$ and $G=\sum_j\epsilon_j c_jT^{m_j}Z^{a_j}$, and group the latter by $a_j$. If $a_j=a_k$ and $m_j-m_k=Nd$, evaluating gives
\[
                      v_j-v_k=O(1)-Np .
\]
The missing ternary arc implies $N=0$ on the retained sequence. Combine terms with identical $(a_j,m_j)$, deleting exact zero sums. At least one group remains by (4). In any occupied $Z$-group distinct surviving $m_j$ have distinct residues modulo $d$. Moreover there are **at most $s$ such exponents**: if two original terms share a ternary level, then with common $a_j$ their difference in ternary valuation is
\[
             0=v_3(c_j/c_k)+(m_j-m_k)(-p-v_3(c))/d .
\]
This forces $m_j=m_k$ on growing $p$. The number-of-dates saving survives even when the dyadic exponents at a single date are macroscopically separated.

Let $R$ be the monic common factor of $F$ and all $Z$-coefficients of $G$ over $\mathbb Q$. It is squarefree. For a root $\lambda$ of $F$ and a primitive $d$th root $\zeta$, each occupied group at $\lambda\zeta^b$ is an exponential sum with at most $s$ distinct bases and nonzero coefficients. A Vandermonde determinant precludes a run of zeros as long as the number of bases. Counting cyclic windows shows that at least $d/s$ of the roots survive. Therefore $J=d-\deg R\ge d/s$.

The residual polynomials $F/R,G/R$ are coprime after clearing monomials in the $S$-unit coordinates. The univariate residual of $F$ has nonzero constant. Levin's fixed-polynomial gcd theorem makes the remaining logarithmic gcd outside $S$ equal to $o(h)$ on the retained sequence; proper exceptional algebraic loci have already been removed. Constants and monomials contribute only $O(1)$. The coprime multiplicative normalization of positive and negative $S$-valuations is the one in the [fixed-translate proof](SPARSE_DENOMINATORS.md). At each outside prime $R$ and $F/R$ have integral evaluations up to fixed denominators, since roots of $F$ are units there, while the two valuation sums together equal $\log D=h\log 2+o(h)$ by two-logarithm separation. Their upper height bounds are $(d-J)h\log2/d+O(1)$ and $Jh\log2/d+O(1)$, so both are attained to $o(h)$. The resulting limit of $\log_2Q/h$ is $J/d\ge1/s$.

The rational monic complementary factor of degree $J$ has nonzero constant and each root has valuation $-v_l(c)/d$ for $l=2,3$. Thus $d\mid Jv_l(c)$ at both primes. Since $X=cT^d$, one has $d\mid Jh$ and $d\mid Jp$. In particular every subsequential limit for $Q$ is rational with reduced denominator dividing the clock gcd on a further subsequence. Equations (3) and $q\le D<2^h$ now prove all statements following (1). The exact cutoff in period is ineffective. For nonproportional clocks $Kp\ne\ell h$, Corvaja–Zannier applied to the multiplicatively independent units $2^h3^{-p}$ and $2^K3^{-\ell}$ gives $\log\gcd(D,|2^K-3^\ell|)=o(h)$; in this case $q$ itself has the same accumulation rates as $Q$. At proportional clocks the exact gcd with $D$ is $2^{(h/g)j}-3^{(p/g)j}$, where $g=\gcd(h,p)$, $u=\ell/(p/g)=K/(h/g)$ and $j=\gcd(g,u)$. That possible large factor is retained in (3). [Corvaja–Zannier, Proposition 2](https://arxiv.org/abs/math/0311030) · [Exact proportional-case gcd](DISPERSED_EDITS.md)

[Exact rotation controls](check_cycle_rotations.py) · [Archived counts and rational comparisons](../../../reports/astra-infinite-descent-20261127/cycles/ROTATION_CONTROLS.json)
