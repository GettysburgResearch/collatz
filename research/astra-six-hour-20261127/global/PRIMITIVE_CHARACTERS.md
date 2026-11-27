# The original escape trace in primitive Dirichlet characters

**PROPOSED written identities.** Put $q=3^k$. Start with $Y_0=0$ and use the original independent geometric letters, $\Pr(E=e)=2^{-e}$ for $e\ge1$. The recursion is $Y_{k+1}=2^{-E}(1+3Y_k)\pmod{3q}$. For $k\ge1$, $Y_k$ is a unit. Its residue law is compatible under reduction since the outer affine maps contract by one ternary digit. Write $A_k(\chi)=\mathbb E\chi(Y_k)$, with characters evaluated on units. The three conductor-eight twists in [the root trace](../root/DIRICHLET_TRACE.md) can use ordinary Dirichlet $L$-functions, acting on *these exact coefficients*.

For any of the nonprincipal real dyadic characters $\eta$ in that trace and $k\ge1$ one has
\[
 \sum_{n\ge1}\frac{\rho_k(n)\eta(n)}{n}=
 \frac32\left[(1-\eta(3)/3)L(1,\eta)+
 \sum_{j=1}^k\sum_{\chi\ {m primitive}\bmod 3^j}
                A_j(\bar\chi)L(1,\chi\eta)\right].                         \tag{1}
\]
For $j=1$ the inner sum has one character. To prove (1), invert the multiplicative Fourier transform of $p_k$ on the $\varphi(q)=2q/3$ units. Every character except the principal one is induced from a unique primitive $\chi$ modulo $3^j$, $1\le j\le k$. Its value under $p_k$ is the same as at depth $j$. The induced character has the same Dirichlet series after multiplication by $\eta$. The principal term removes the Euler factor at three. All these series converge in ordinary order by periodicity and vanishing mean over the coprime moduli. In particular each first difference of the completed escape trace is one *new* conductor shell with exact input law.

## A flat transition with the complete Gauss phases

Fix $k\ge2$. Let $U_q=(\mathbb Z/q\mathbb Z)^\times$ and $\tau_q(\psi)=\sum_{x\in U_q}\psi(x)e(x/q)$, $e(t)=\exp(2\pi i t)$. For primitive $\chi\bmod3q$ and $\psi\bmod q$ put
\[
 J(\chi,\psi)=\frac1{\varphi(q)}\sum_{x\in U_q}\chi(1+3x)\bar\psi(x).
\]
The exact recurrence is
\[
 A_{k+1}(\chi)=\frac1{2\chi(2)-1}
       \sum_{\psi\ {m primitive}\bmod q} J(\chi,\psi)A_k(\psi),
 \qquad
 J(\chi,\psi)=
 \frac{\tau_q(\bar\psi)\tau_{3q}(\bar\chi\psi^*)}
      {\varphi(q)\tau_{3q}(\bar\chi)},                                     \tag{2}
\]
where $\psi^*$ denotes inflation. Expand $\chi(1+3x)$ by its primitive Gauss sum. For a unit $a\bmod 3q$, summation over $x$ of $\bar\psi(x)e(ax/q)$ gives $\psi(a)\tau_q(\bar\psi)$ when $\psi$ is primitive. It vanishes for every imprimitive $\psi$ since $k\ge2$ and summing over the three lifts modulo $q/3$ cancels the additive character. Since $\chi$ is primitive and $\psi^*$ is trivial on the last lift group, $\bar\chi\psi^*$ is primitive too. The external factor is exactly $\mathbb E\chi(2)^{-E}$. The independence here is the original geometric law.

Every entry of $J$ between primitive shells has absolute value $\sqrt q/\varphi(q)=3/(2\sqrt q)$. There are $4q/9$ input characters and three times as many output characters. Each row has norm one, and $J^*J=3I$. For the latter identity, sum first over every output character and use orthogonality and injectivity of $x\mapsto1+3x$. The imprimitive output rows vanish on primitive input columns since their composed functions factor through $q/3$. The Fourier transform in (2) retains phases in both directions. Replacing its entries by their absolute values changes the operator.

## Exact singular spectrum of the weighted map

In discrete logarithms to base 2, the group $U_{3q}$ is cyclic of order $n=2q$. The parent image $1+3U_q$ consists exactly of exponents $j\equiv2,4\pmod6$, because the two permitted residues modulo nine are 4 and 7. The weighted map in (2), in physical space, first puts the input on these sites and then convolves by the probabilities $2^{-e}$ on the cyclic group. With unit-normalized counting measures and the density multiplier three, its squared norm quotient is three times the convolution squared norm quotient on the embedded vector. The autocorrelation of $2^{-e}{\bf1}_{e\ge1}$ on the infinite line is $2^{-|j|}/3$. Thus the normal operator is, up to the input permutation and a unitary change of normalization, the restriction of the cyclic kernel
\[
                 \sum_{l\in\mathbb Z}2^{-|j-j'+nl|}
                 \quad(j,j'\equiv2,4\bmod 6).                                \tag{3}
\]
Primitivity is exactly zero sum over the three lifts of every residue modulo $q/3$ in the parent. The injection identifies these with the three lifts of each output site modulo $q$, namely the exponent translates by $n/3$ in $U_{3q}$. On the $m=n/6$ cells $(6s+2,6s+4)$ the surviving frequencies are therefore $\theta=2\pi t/m$, $3\nmid t$. At each such frequency the two eigenvalues of (3) are
\[
 \lambda_\pm(\theta)=A(\theta)\pm |C(\theta)|,\qquad
 A(\theta)=\frac{1-r^{12}}{|1-r^6 e^{i\theta}|^2},\qquad
 C(\theta)=\frac{r^2}{1-r^6e^{i\theta}}+
             \frac{r^4e^{-i\theta}}{1-r^6e^{-i\theta}},\quad r=1/2.        \tag{4}
\]
The diagonal series in (3) has displacements $6l$; the cross series has displacements $6l+2$. Thus its two-by-two Hermitian block has diagonal $A$ and cross-entry $C$ or its conjugate. In ordinary coordinates the two sites in a cell are the siblings $x$ and $4x+1\pmod q$. In particular *half* the singular directions have squared gain greater than $1.14$, and half have squared gain smaller than $0.85$. Indeed $63/65\le A\le65/63$ and $|C|\ge16/65-4/63$. At frequencies tending to zero the squared gains tend to $85/63$ and $5/7$.

The mean squared gain is instead $3$ times the mean of $|2\chi(2)-1|^{-2}$ over the primitive output shell, since all $J$ rows have unit norm. Over all $n$ characters this latter multiplier averages $F(n)=(1+2^{-n})/[3(1-2^{-n})]$ by the Poisson kernel. Its primitive mean is $(3F(n)-F(n/3))/2$, tending to $1/3$. Thus trace-averaging the squared gain misses the uniformly expanding directions in (4).

The discrete-logarithm reindexing by $y_s=(4^s-1)/3$, the cyclic geometric convolution, and an additive-to-multiplicative Parseval identity appear in [rStation Paper 11, Theorems 2.1–2.3](https://rstation.ai/problems/collatz/papers/11). Its scalar multiplier on the full parent ring and exact actual-law energy ratios are prior results. Here (2) gives the phase-resolved transition between ordinary *primitive Dirichlet characters*. Restricting (3) to the two allowed unit sites per three parent positions gives the two singular directions in (4). Standard primitive Gauss-sum formulas also appear in [Pigno and Pinner, prime-power character sums](https://www.math.ksu.edu/~pinner/Pubs/bicharsum3a.pdf).

The exact closing target is a Cesàro upper bound on the special phase-correlations in (1), with the signed linear combination of the three $\eta$ from the root note. The spectrum (4) rules out a uniform norm contraction on this domain. It does not estimate the sign of those correlations and does not decide positive ordinary escape or cycle uniqueness.
