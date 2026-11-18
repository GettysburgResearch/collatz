# An infinite family of native periodic directives with at most one algebraic value

**PROPOSED.** Fix $T=64/81$. In the entire countable family below, the difference of the 2-adic stack values of any two distinct directives is transcendental over $\mathbb Q$. Consequently at most one member can have an algebraic 2-adic value, and at most one can admit an ordinary initial context. For each odd prime $k$ the family includes exactly $2^{(k+1)/2}-2$ members of minimal period $9k$ constructed at that modulus. The theorem permits a single exception across all periods combined.

## Native directives

Choose any periodic subset $A$ of the integers that is contained in $3+9\mathbb Z$ and invariant under $j\mapsto-3-j$. Put
$$
E_j(A)=36j(j+3)+(j\bmod9)+9\mathbf1_A(j),
$$
using residues $0,\ldots,8$. Then $E_0=0$ and
$$
E_j-E_{j-1}=9m_j+1,\qquad
m_j=8(j+1)-\mathbf1_{9\mid j}+\mathbf1_A(j)-\mathbf1_A(j-1).
$$
In particular $m_0=7$ and $d_j=m_j-m_{j-1}\ge8-1-2=5$. Thus $\Theta_A=\sum_{j\ge0}T^{E_j(A)}$ is exactly the native value in the positive-increment stack normal form. Each finite steering prefix taking a tail into the specified phase and height gives a rational affine change of the same native value with nonzero slope. [Stack interface at PR 20, L-9407](https://github.com/gfreund123/collatz/blob/82ca2f932438a9fe0897704ba62959ca23ec830f/research/padic-repetition/claims/L-9407-stack-partial-theta-normal-form.md)

Write $w_j=(j\bmod9)+9\mathbf1_A(j)$. The least period of $d$ equals that of $w$. Indeed the second difference of $w$ differs from $9d$ by a constant. If a shift fixes this second difference, its difference on $w$ is affine in j, bounded by periodicity, and has mean zero. Hence it vanishes. A period of $w$ is a multiple of nine by reduction modulo nine. On $j=9z+3$ the reflection is $z\mapsto-1-z$. Modulo an odd prime $k$ it has $(k+1)/2$ orbits. Every nonconstant union of those orbits in $\mathbb Z/k\mathbb Z$ has least period $k$, proving the stated count after lifting.

## A consequence of the p-adic modular transcendence theorem

For a nonzero even periodic sequence $c(n)$ of algebraic numbers, let
$$
f(q)=\sum_{n\in\mathbb Z}c(n)q^{n^2}.
$$
For any algebraic $q_0$ with $0<|q_0|_2<1$, its value $f(q_0)$ in $\mathbb C_2$ is transcendental. Here the coefficients are interpreted through a fixed embedding into $\mathbb C_2$.

To see this, $f$ is a nonzero holomorphic modular form of weight $1/2$ on a finite-index subgroup with finite-order multiplier. Its decomposition by residue class is precisely a linear combination of the unary theta functions: for period $L$, take the components $\theta_{L,\mu}(4L\tau,0)$, $\mu$ modulo $2L$, with $q=e^{2\pi i\tau}$. Their transformation formulas give algebraic Fourier coefficients at every cusp, allowing fractional exponents there. Nonvanishing follows also from the coefficients $2c(n)$ at positive squares. [Eichler and Zagier, The Theory of Jacobi Forms, Section 5](https://people.mpim-bonn.mpg.de/zagier/files-restricted/scanned/TheoryOfJacobiForms/fulltext.pdf)

Choose a positive power $g=f^e$ of positive even integral weight $w=e/2$ with trivial multiplier on a finite-index subgroup. The polynomial
$$
\prod_\gamma (X-g|_w\gamma)
=X^d+\sum_{i=1}^d A_i X^{d-i}
$$
over right translates indexed by left cosets has $A_i$ in the full-level holomorphic modular forms of weight $wi$ with algebraic Fourier coefficients. The constant term is nonzero as a form. By the full-level modular form ring theorem, $A_i$ is a weighted-homogeneous polynomial in $E_4,E_6$ over the algebraic numbers. These identities of Fourier expansions can be evaluated at $q_0$: on the polynomial side the Eisenstein series converge there, and $g$ also converges by construction. If $g(q_0)=\alpha$ were algebraic, substituting $X=\alpha$ would give a nonzero polynomial relation on $E_4(q_0),E_6(q_0)$. Indeed its highest weighted component is the nonzero constant term $A_d$, of weight $wd$. Nesterenko's theorem at the 2-adic place gives algebraic independence of $E_2(q_0),E_4(q_0),E_6(q_0)$ for nonzero algebraic $q_0$ of absolute value less than one. The original paper states the p-adic analogue at the end of Section 1, and Philibert states it explicitly in the introduction and Section 3. [Nesterenko, Modular functions and transcendence questions](https://www.mathnet.ru/links/14cb2e3131de83d7fbb9a1cd521d43f3/sm158_eng.pdf) · [Philibert, Transcendance et fonctions modulaires](https://www.numdam.org/item/JTNB_1999__11_1_73_0.pdf)

## Exact bilateral difference

Let $A,B$ be distinct permitted subsets. Define $c(2j+3)=\mathbf1_A(j)-\mathbf1_B(j)$ for all integer $j$, with $c(n)=0$ for even $n$. This sequence is periodic (use a common multiple of the two periods), nonzero, even under $n\mapsto-n$, and supported on $n\equiv9\pmod {18}$. On its support $j\equiv3\pmod9$, so
$$
36j(j+3)+3=9(2j+3)^2-78.
$$
The nonnegative $j$ in the support correspond to all positive supported $n$, including the first possible $n=9$. Therefore the identity
$$
\Theta_A-\Theta_B=\frac{(T^9-1)T^{-78}}2
\sum_{n\in\mathbb Z}c(n)(T^9)^{n^2}
$$
holds in $\mathbb Q_2$. The prefactor is nonzero rational and $T^9$ has positive 2-adic valuation, so the modular result proves the assertion.

More precisely, for any finite partition of permitted residues into reflection orbits at a common modulus, the singleton-orbit differences $\Theta_A-\Theta_\varnothing$, together with 1, are linearly independent over the algebraic numbers. Every nonempty algebraic combination of the corresponding even weights remains nonzero by their disjoint supports. This gives a dimension bound in addition to the single-exception conclusion. The exceptional member, if one exists, is unidentified. General unrestricted periodic stack words remain open.
