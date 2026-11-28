# Composite odd grades can lose almost the whole raw denominator

Let \(s(p)=\min\mathcal S_p\) be the least achievable limit of \(\log_2 q/L\) among primitive positive rational shortcut cycles at fixed odd grade \(p\), in the notation of the [spectrum decision theorem](DECIDABLE_FIXED_GRADE_SPECTRUM.md). We give a pair of bounds for this exact function on **all** and on **infinitely many** grades, respectively. Logarithms in their growth factors are natural.

**Proposed results.** There are absolute positive constants \(c,C\) such that
\[
   p\,s(p)\ge c\,\frac{(\log p)^2}{\log\log p}\quad (p\ge 3),
 \qquad
   p\,s(p)\le C\,\frac{(\log p)^3}{(\log\log p)^2}
                                   \quad\text{for infinitely many }p.    \tag{1}
\]
Thus along explicit composite grades \(s(p)=p^{-1+o(1)}\), even for attaining words in which all consecutive native odd gaps take only the three values \(n-1,n,n+1\). At fixed prime grades \(s(p)=1\) instead. The upper construction also supplies a simultaneous, finite bound for every displayed \(p\) and \(n\ge3\), without waiting for a grade-dependent onset. A direct multiplicative-order comparison in the last section shows why this large cancellation alone cannot bypass the one-odd pumping obstruction.

## The orders needed for a period of size \(g\)

Use the [fixed-target reduction](PRIME_GRADE_DENOMINATORS.md): the limiting exponent along a subsequence is \(\deg V/k\), with \(g=\gcd(k,a,p)\mid p\) and \(1\in S\), \(\operatorname{lcm}S=g\). The set \(S\) comprises the orders of the images of the surviving roots under \(Z=2^{a/g}X^{k/g}/3^{p/g}\). For \(d\in S\) take a surviving root \(\beta\) of \(V\) with \(Z(\beta)\) primitive of order \(d\). Rational conjugation gives every primitive \(d\)th root as an image. Each such image has at least \(k/(2g)\) distinct preimages among roots of \(V\): the [positive-radical degree calculation](DECIDABLE_FIXED_GRADE_SPECTRUM.md) gives at least this degree over \(\mathbb Q^{\rm ab}\) for \(\beta\), since it is \((3^{p/g}2^{-a/g})^{g/k}\) times a root of unity. Its conjugates over this field have the same image in \(\mathbb Q^{\rm ab}\). Different images have disjoint preimages. Thus, allowing every ramified case at two and three,
\[
                      \sigma\ge\frac1{2g}\sum_{d\in S}\varphi(d).      \tag{2}
\]

Assign each exact prime power \(\ell^b\parallel g\) to a \(d\in S\) it divides. In \(\varphi(d)\) the positive factors \(\varphi(\ell^a)\) include at most one equal to one; a product of any list of integers at least two dominates their sum when there are at least two factors. The singleton case gives equality. Thus each \(\varphi(d)\) is at least half the sum of the factors assigned to it, including the possible factor one. As \(\varphi(\ell^b)\ge\ell^b/2\), putting \(A=\sum_{\ell^b\parallel g}\ell^b\) we get \(\sum_{d\in S}\varphi(d)\ge A/4\) for \(g>1\).

The elementary Chebyshev estimate \(\log\operatorname{lcm}(1,\ldots,\lfloor y\rfloor)=O(y)\) yields
\[
             \log g\ll y+A\log y/y \qquad(y\ge3).
\]
Indeed sum the logarithms of the assigned powers at most \(y\) using that lcm, and bound \(\log z/z\) for the larger ones. Choosing \(y=\max(3,\sqrt{A\log(2+A)})\) gives \(A\gg(\log g)^2/\log\log g\) at large \(g\): if \(A>(\log g)^2\) this is immediate, and otherwise \(\log A\le2\log\log g\). For \(g\ge\sqrt p\), (2) gives the lower part of (1). For \(g<\sqrt p\), (2) already gives \(p\sigma\ge\sqrt p/2\). A decrease of the absolute constant includes all remaining finite grades.

## Residue classes select different data primes

Choose a prime \(h\), an integer \(m\le h\), and \(m\) distinct primes \(\ell_i\) different from \(h\). Fix distinct addresses \(a_i\bmod h\). Set
\[
 p=h\prod_{i=1}^m\ell_i,\qquad
 \delta_j=\sum_{i=1}^m
        \mathbf 1_{j\equiv a_i\ (\bmod h)}
        \mathbf 1_{j\equiv0\ (\bmod\ell_i)},\qquad
 u_j=jn+\delta_j\quad(0\le j<p),\quad L=pn.                            \tag{3}
\]
The address classes are disjoint, so \(\delta_j\in\{0,1\}\). This is the cyclic Chinese-remainder version of the familiar address-function construction in Fourier sparsity; [Sanyal](https://doi.org/10.4086/toc.2019.v015a011) treats the Boolean-cube version. The following Fourier calculation is over the cyclic group of odd-date indices, not a claim about cube dimension.

Let \(f(j)=2^{\delta_j}=1+\delta_j\). Identify the character group with that of \(\mathbb Z/h\times\prod\mathbb Z/\ell_i\). If a character is nontrivial at two data primes, its Fourier coefficient vanishes by summing a free coordinate in each individual summand. For a character nontrivial at exactly \(\ell_i\), only summand \(i\) survives and it is nonzero for every address character, since both fixed-coordinate point masses have nonzero Fourier transform. For no nontrivial data characters and a nontrivial address character \(b\), the coefficient is proportional to
\(\sum_i\zeta_h^{b a_i}/\ell_i\). It is nonzero: multiply by \(\prod_i\ell_i\) and reduce modulo any prime ideal over \(\ell_1\). Only its first term survives and is a unit. The trivial coefficient is positive. Hence the **exact** support cardinality is
\[
                             s=h\left(1+\sum_i(\ell_i-1)\right).         \tag{4}
\]
The support also generates the full character group, since it includes the individual characters of each prime coordinate. Therefore \(f\) and \(\delta\) have least period \(p\). The cyclic gap word \(n+\delta_{j+1}-\delta_j\) has the same least period: shift invariance of these differences would make \(\delta_{j+r}-\delta_j\) constant, and its sum around the circle is zero. For \(n\ge3\) the dates in (3) give a primitive native word with positive rational fixed point and the stated three allowed gaps.

Put \(X=2^n\). Its carry is \(3^{p-1}\sum_{j<p} f(j)(X/3)^j\); its raw denominator is \(X^p-3^p\). Precisely \(s\) of the roots \(3\zeta_p^k\) survive polynomial cancellation, by (4). The monic product of the other factors divides the integral carry polynomial over \(\mathbb Z[X]\) by monic division and rational Galois invariance. Every surviving root has absolute value three. Consequently the complete denominator obeys the uniform estimate
\[
                 q\le (2^n+3)^s,\qquad
                 \lim_{n\to\infty}\frac{\log_2 q}{pn}=\frac{s}{p}.     \tag{5}
\]
The limit at each fixed choice uses the univariate resultant for the residual polynomials as in the spectrum theorem. The inequality holds for simultaneous choices of \(p,n\).

For the upper bound of (1), take \(m\to\infty\), a prime \(h\in[m,2m]\), and \(m\) distinct primes larger than \(2m\) and at most \(C_0m\log m\), available by the prime number theorem. Then \(\log p\asymp m\log m\) and \(s=O(m^3\log m)\), yielding the asserted bound. Equations (3)–(5) also prove that there is no uniform positive constant in front of \(p^{-1+\epsilon}\) as a lower denominator exponent across all odd grades, for any fixed \(\epsilon>0\). The limits in (1) are taken first over native length at a specified grade.

## Translation of a full motif and the order of three

Take a word of length \(n\) with \(p_0\ge1\) odd dates \(v_0<\cdots<v_{p_0-1}\), positive raw determinant \(D_0=2^n-3^{p_0}\), carry \(C_0\), and complete reduced denominator \(q_0=D_0/\gcd(D_0,C_0)\). Suppose a positive calendar has length \(Nn\) and chronological odd dates
\[
         in+v_j+\Delta_i,\qquad
             0\le i<N,\quad0\le j<p_0,
\]
listed in lexicographic order of \((i,j)\) and inside the native period. The shifts are any integers of spread \(B=\max_i\Delta_i-\min_i\Delta_i\); the full calendar need not be primitive for the following exact comparison. Write \(q\) for its complete denominator. Then
\[
 \frac{q_0}{\gcd(q_0,S)}\mid q,\qquad
 S=\sum_{i<N}2^{\Delta_i-\min\Delta},\qquad
          \operatorname{ord}_{q_0}(3)
                \le N2^B\,\operatorname{ord}_q(3),                    \tag{6}
\]
where the order modulo one is set to one. Indeed \(D_0\mid 2^{Nn}-3^{Np_0}\). In \(\mathbb Z[1/2]\) modulo \(D_0\) the full carry reduces to \(3^{(N-1)p_0}2^{\min\Delta} C_0 S\), since \(2^{in}\equiv3^{ip_0}\). All scalar powers here are units modulo \(D_0\). At each prime of \(D_0\) the amount of \(q_0\) surviving the additional \(S\) is a lower bound on the valuation in the full denominator. This proves the divisibility. For any \(d\mid q_0\), the kernel on units modulo \(q_0\) of reduction modulo \(q_0/d\) has at most \(d\) elements, by counting residue classes. Thus \(\operatorname{ord}_{q_0}(3)\le d\,\operatorname{ord}_{q_0/d}(3)\). Taking \(d=\gcd(q_0,S)\le N2^B\) proves (6).

In particular a primitive cycle (3) whose entry order is \(j=\operatorname{ord}_q3\) satisfies \(\operatorname{ord}_{2^n-3}3\le 2p j\). More generally if \(p_0=1\) and successive calendars have \(n/\log(2+N+j)\to\infty,\ B=o(n)\), then \(\log(2+\operatorname{ord}_{2^n-3}3)=o(n)\). Conversely any one-odd family with this last subexponential order is itself a translated-copy family with \(N=1\). Hence the [one-odd multiplicative-order obstruction](PERIODIC_PUMP_FRONTIER.md) remains necessary and sufficient for a superlogarithmic pump within the larger class of ordered small-spread translates of a one-odd template. The construction of small denominator exponents across composite grades supplies no such order estimate.
