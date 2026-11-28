# A full-period character test for all clock types

**Proposed written theorem.** The primitive period of the colored Apéry boundary is exactly the least common multiple of the orders of its active characters, times the reduced clock length. Every active character, including orders divisible by two or three, has a nonzero selected-root resultant once its short clock relation clears an explicit digit threshold. This gives simultaneous lower bounds on the complete reduced denominator, with all shared primes retained. For a fixed prime common divisor of the two counts and a sublinear-conductor regime specified below, every primitive near-critical parity circle has reduced denominator $2^{n-o(n)}$.

## Physical data and structural cancellation

Use the [complete colored-semigroup construction](../phase2/SEMIGROUP_BOUNDARY.md). Write the displayed length and weight as $n=gN,u=gU$ with $0<U<N$ and $(U,N)=1$. Choose $aU+bN=1$, and put $X=z^Ut^b, Y=z^Nt^{-a}$ where $t^g=1$. Let $G(z,t)=\sum_h G_h(t)z^h$ be the actual nonnegative holes polynomial. Each coefficient of each $G_h(t)$ is zero or one in degrees $0,\ldots,g-1$. Set $A_0=2^N,B_0=3^U$. For $\ell\mid g$ let
$$ D_\ell=\left|B_0^{\varphi(\ell)}\Phi_\ell(A_0/B_0)\right|,
\qquad D=|2^n-3^u|=\prod_{\ell\mid g}D_\ell. $$
The selected roots $z_0=2^a3^b$ and $t_0=A_0/B_0$ are evaluated modulo each divisor of $D$ using inverses of two and three. At $\ell>1$, the geometric-sum term in the physical boundary vanishes modulo $D_\ell$ and the remaining value is $G(z_0,t_0)$, up to a physical unit multiplying the affine numerator. At $\ell=1$ the corresponding value is the univariate polynomial
$$ P_1(z)=g-(1-z)G(z,1). $$
In fact the physical boundary at $t=1$ is $[U]_z P_1(z)$, and $(z_0-1)[U]_{z_0}=1\bmod D_1$. The polynomial $P_1$ is positive for all positive real arguments. Above one this follows from its displayed formula, below one from $(1-z)H_S(z,1)>0$, and at one from $P_1(1)=g$.

Call $\ell>1$ **active** if some $G_h(\zeta_\ell)\ne0$ at a primitive $\ell$th root. This condition is independent of the chosen primitive root. For an inactive order, each $G_h(t)$ is divisible in $\mathbb Z[t]$ by the monic $\Phi_\ell(t)$. Therefore all of $D_\ell$ cancels in the affine numerator. Distinct factors need not be coprime.

**Exact period.** Let $q$ be the least common multiple of all active orders, with the empty least common multiple equal to one. The least physical period of the displayed word is exactly $Nq$. Indeed, shifting the colors by $j$ fixes every height layer of $G$ precisely when $\ell\mid j$ for every active order, by the invertible finite Fourier transform on the cyclic color group. This condition fixes the whole semimodule because its filled half-cylinder is color invariant. The color increment $(0,1)=NX-UY$ moves the Apéry class by $N$ clocks modulo the ray direction $Y$. Equal Apéry heights after $jN$ clocks give equal bits there by taking successive differences. Conversely if the word repeats after $jN$ clocks, every length-$jN$ interval contains $jU$ ones and the clock points differ by precisely the color increment $j$. Every least period is a multiple of $N$ because the reduced weight-to-length ratio is $U/N$. These implications prove the assertion in both directions.

## An elementary radical lemma over the abelian extensions

Take coprime integers $k>0,l\le0$ and $R=(2^k3^l)^{\pm1}$. For a positive integer $m$, a root of unity $\omega$ and any complex root $\alpha^m=R\omega$, let $L$ be the union of finite abelian extensions of $\mathbb Q$ in $\mathbb C$. Then
$$ [L(\alpha):L]=e=m/\gcd(m,2),\qquad
\alpha^e\in L,\qquad |v_2(\alpha^e)|=k/\gcd(m,2),                 \tag{1}$$
where $v_2(2)=1$ at any chosen place over two. **Proof.** All roots of unity lie in $L$. Multiplying by one reduces to the positive real root $\beta=R^{1/m}$. The extension $L(\beta)/L$ is the splitting field of $x^m-R$, and its Galois group acts on $\beta$ by multiplication by a subgroup of $\mu_m$ of some order $e'\mid m$. Hence $\beta^{e'}\in L$. For each $d\mid m$ the positive pure radical $R^{1/d}$ has degree $d$ over $\mathbb Q$. Indeed, the absolute constant term of a monic rational factor of $x^d-R$ of degree $j$ is $R^{j/d}$. Rationality of this number forces $d\mid jk,jl$ and hence $d\mid j$. A real pure radical field of degree $d>2$ has nonreal conjugates and cannot be Galois over $\mathbb Q$. Every finite subextension of $L/\mathbb Q$ is Galois, as it is contained in a finite abelian extension. Applying this to $\beta^{e'}$ shows that $m/e'\le2$. If $m$ is even then $\sqrt R\in L$ and $e'\le m/2$. This proves the degree; raising the defining equation to the indicated power gives the valuation statement.

**Digit separation.** Suppose $P(z,t)=\sum_h P_h(t)z^h$ with every $P_h$ a zero-one mask on the $g$ colors, $\ell\mid g$, $\zeta$ primitive of order $\ell$, and $\alpha^m=R\omega$ as above. If
$$                  k>\gcd(m,2)\,\varphi(\ell)\log_2 g,              \tag{2}$$
then $P(\alpha,\zeta)=0$ if and only if $P_h(\zeta)=0$ for every height. To prove this, separate exponents into classes modulo $e$ from (1). The powers $1,\alpha,\ldots,\alpha^{e-1}$ are linearly independent over $L$. Each class therefore gives a vanishing polynomial in $\alpha^e$ with coefficients in $\mathbb Z[\zeta]$. Each nonzero coefficient $c=P_h(\zeta)$ is an algebraic integer with $|\sigma(c)|\le g$ at every embedding. Its nonzero integer norm thus has absolute value at most $g^{\varphi(\ell)}$. Positivity of all finite valuations of integral conjugates gives $0\le v_2(c)\le\varphi(\ell)\log_2 g$. When $v_2(\alpha^e)>0$ the term of least exponent with nonzero coefficient has uniquely lowest valuation by (2). When this valuation is negative the term of greatest exponent does. A sum with a uniquely lowest valuation cannot vanish. This proves the forward implication; the reverse follows by evaluation. The proof applies unchanged when two or three ramifies in the character field.

## Factorwise divisibility at the actual root

For any $1\le K<N$ the circular-gap argument gives primitive $(k,l)$ with $1\le k\le K,-k\le l\le0$ and $0<m=|kU+lN|\le N/(K+1)$. Write $\epsilon=\operatorname{sgn}(kU+lN)$, $r=bk-al$ and $(2^k3^l)^\epsilon=A/B$ in lowest terms. Then
$$ B z_0^m=A t_0^{-\epsilon r},\qquad 1\le A,B\le3^K. $$
For $\ell>1$ use $P=G$, and for the principal character use $P=P_1$. Select $j\equiv-\epsilon r\bmod\ell$ with $0\le j<\ell$. Modulo $D_\ell$, $t_0^\ell=1$ since $\Phi_\ell(t_0)=0$. Form the integer
$$ \mathcal R_\ell=\operatorname{Res}_t\left(\Phi_\ell(t),
       \operatorname{Res}_z(Bz^m-At^j,P(z,t))\right). $$
Every divisor common to $D_\ell$ and the physical affine numerator divides $\mathcal R_\ell$. Evaluate the integer Bezout identities for the two resultants first at $z_0,t_0$, then at $t_0$. This argument applies to any divisor, even a prime power occurring in several homogeneous cyclotomic values. A padded inner resultant, using the displayed degree $d=\deg_zP$, satisfies the same identity and specializes to $B^d\prod P(\alpha,\zeta)$ at each character even if a leading coefficient vanishes.

For the principal character $\mathcal R_1\ne0$: the univariate binomial is irreducible over $\mathbb Q$ by the constant-term proof above and has a positive real root, where $P_1>0$. For an active nonprincipal character (2) gives $\mathcal R_\ell\ne0$. Write $W=\sum_{h,r}|[z^ht^r]P|\ge1$. All binomial roots at every character have absolute value $(A/B)^{1/m}$. Taking absolute values in the product formula gives the finite bound
$$ \log\gcd(D_\ell,C)\le\log|\mathcal R_\ell|
   \le \varphi(\ell)\left(m\log W+d\log\max(A,B)\right)
   \le \varphi(\ell)\left(\frac{N\log W}{K+1}+d K\log3\right).       \tag{3}$$
Here $C$ is the original affine numerator. For any subset of factors with nonzero resultants,
$$ d_{\rm red}=D/\gcd(D,C)\ge\!
    \prod_{\ell\text{ in subset}} D_\ell/\gcd(D_\ell,C).            \tag{4}$$
For a prime of exponent $e_\ell$ in each factor and exponent $v$ in $C$, this is the elementary inequality $(\sum e_\ell-v)_+\ge\sum(e_\ell-v)_+$. In particular the lower bound does not assume the cyclotomic factors are coprime.

**Consequence for near-critical primitive words.** Fix any $g$. Let $N\to\infty,U/N\to\log_3 2$. Put $c=1+\max\{h:G_h\ne0\}$, with $c=0$ when there are no holes. Suppose
$$                         c\log(2+gc)=o(N).                         \tag{5}$$
Then for the active orders $\mathcal A$ of each word,
$$ \log d_{\rm red}\ \ge N\log 2\left(1+\sum_{\ell\in\mathcal A}\varphi(\ell)\right)-o(N).
                                                                        \tag{6}$$
In (3), $d\le c$ and $W\le g+2gc$ suffice for either polynomial. For bounded $c$ take $K=\lfloor\sqrt N\rfloor$. In general choose integer $K\asymp\sqrt{N(1+\log(g+2gc))/\max(1,c)}$, capped at $N-1$. Then $K\to\infty$ and (3) is $o(N)$ uniformly over the fixed divisor set. Any associated $k$ tends to infinity because a bounded $(k,l)$ has $|kU/N+l|$ bounded away from zero at the irrational limiting slope, whereas $m/N\to0$. Thus (2) holds for each active order eventually. Every nonprincipal $D_\ell$ has $\log D_\ell=N\varphi(\ell)\log2+o(N)$ since every primitive root of order $\ell>1$ is separated from the positive real axis, with $\ell$ fixed. The principal $\log D_1=N\log2+o(N)$ uses the externally sourced elementary-effective two-logarithm separation in the [calendar note](../CONTRACTING_CALENDARS.md). Apply (4).

For a primitive word the least common multiple of the active orders is $g$. In particular at prime $g$ its only nonprincipal order is active and (6) yields $\log d_{\rm red}=n\log2+o(n)$. At arbitrary $g$ the same full rate holds whenever all nonprincipal orders are active. The conductor hypothesis is an additional condition on the word and can fail by a quadratic factor in the height scale. No boundedness of the common divisor $g$, or sublinear conductor, has been deduced for an arbitrary ordinary cycle. Equations (1)–(4) themselves are finite statements for all clock types.

## Primes and prime powers without a digit-size threshold

For any **prime** $g$, including a prime allowed to grow with the clock, every primitive physical word has $\mathcal R_g\ne0$ for every short relation above. More generally, its top character has this property for every odd prime power $g=p^a$.

First suppose $g$ is odd. The binomial $Bz^m-A\zeta^j$ is irreducible over $K_0=\mathbb Q(\zeta_g)$. This follows immediately from (1) if $m$ is odd. If $m$ is even, $\zeta^j$ is a square in $K_0$, since its order is odd. The positive $\sqrt{A/B}$ has squarefree part $2,3$ or $6$, by primitivity of $(k,l)$. It lies in the real part of $\mathbb Q(\zeta_{24})$: use $\zeta_8+\zeta_8^{-1}=\sqrt2$ and $\zeta_{12}+\zeta_{12}^{-1}=\sqrt3$. But
$$ \mathbb Q(\zeta_g)\cap\mathbb Q(\zeta_{24})
        =\mathbb Q(\zeta_{\gcd(g,24)}) $$
is either $\mathbb Q$ or the imaginary quadratic field $\mathbb Q(\zeta_3)$. The intersection formula follows from the degrees $\varphi(g),\varphi(24),\varphi(\operatorname{lcm}(g,24))$ of the fields and their compositum, since the extensions are Galois. Thus $\alpha^{m/2}\notin K_0$. Its degree over $K_0$ is two, and the degree of $\alpha$ over $K_0(\alpha^{m/2})\subset L$ is at least $m/2$ by (1). This gives degree $m$ as claimed. For $g=2$ the binomial over $K_0=\mathbb Q$ has common complex-root radius $(A/B)^{1/m}$. The rational-factor constant-term proof applies to either sign of its constant term.

Group a putative relation $G(\alpha,\zeta)=0$ by height modulo $m$, using the just-proved independence of powers over $K_0$. For each height class evaluate $\alpha^m=(A/B)\zeta^j$. At layer index $v$ in that class the torsion factor cyclically rotates its zero-one mask by $jv$ colors. Consequently the relation is
$$ \sum_{r=0}^{g-1} L_r(A/B)\zeta^r=0,$$
where every $L_r(x)$ is an ordinary polynomial with coefficients in $\{0,1\}$. For $g=p^a$ the cyclotomic polynomial is $\sum_{i=0}^{p-1}t^{i g/p}$, so the rational coefficients $L_r(A/B)$ are equal on each coset modulo $g/p$. This follows by division over $\mathbb Q[t]$ because the quotient has degree less than $g/p$. Every difference polynomial has coefficients in $\{-1,0,1\}$. After stripping powers of $x$ a nonzero such polynomial has leading and constant coefficients of absolute value one; its only possible rational roots are $\pm1$. Since $A/B>0$ differs from one, all the corresponding digit polynomials coincide coefficientwise. Undoing the color rotations shows that $\Phi_g(t)\mid G_h(t)$ for every $h$, contrary to activity. Primitivity at a prime-power clock forces this top character to be active by the exact period theorem.

For every prime $g$, all components in (4) are therefore bounded without (2). In particular the fixed-$g$ restriction can be removed from the prime case of (6): for arbitrary varying primes $g$, $N\to\infty$, $U/N\to\log_3 2$, and $c\log(2+gc)=o(N)$ on primitive words, the full reduced denominator has $\log d_{\rm red}=n\log2+o(n)$. Indeed the sum of the weights in (3) is $1+\varphi(g)=g$. When $c\ge1$ the optimization yields $o(gN)$ uniformly. The case $c=0$ gives least period $N$, so does not occur for a primitive word with $g>1$. Apply the two-logarithm separation directly to $D$ at the original clock $n,u$.

The cyclotomic factorization and its shared-prime warning occur in prior work. The conductor bound here uses the actual colored semimodule, its exact period dictionary, primitive rational short relations, abelian radical degree, and the zero-one digit valuation bound. [PR191, 37b3916633cd32a0c173b20bb18ec3a7ec290a63, TCP-3/4](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md)

## Two primitive controls for genuine component loss

At $g=6,N=5,U=3$, put holes in colors $\{0,2,4\}$ at height zero and $\{0,3\}$ at height one. Both heights lie below $\min(U,N-U)=2$, so removing those points leaves a legitimate semimodule. Its active orders are exactly two and three. The word has least period thirty while the entire inactive factor $D_6=32^2-32\cdot27+27^2=889$ cancels. Thus primitivity at a general composite clock does not imply activity of the top component.

There is also **genuine short-binomial resonance on an active component**. Let $g=4$, $N\ge3$ odd and $U$ even with $(U,N)=1$ and $0<U/2<N-U$. Then $b$ is odd. Remove the colored points
$$                  G(z,t)=t^2+t^{b\bmod4}+z^{U/2}.                 \tag{7}$$
As before the holes lie below both positive generators and some point of height zero survives. Every mask at height $U/2$ in (7) has a single occupied color, so the word is primitive and its fourth character active. At the short relation $k=1,l=0$ one has $z^U=2i^{-b}$ upon setting $t=i$. A root with $z^{U/2}=1-i^b$ satisfies the binomial and annihilates (7), since $(1-i^b)^2=2i^{-b}$. Here $m=U$. If $U>N/2$, this particular relation is longer in height than the circular-gap bound when $K=1$. The calculation tests the more general nonresonance claim for primitive short-coefficient relations. At $U\le N/2$ it also meets the circular-gap height bound for $K=1$.

This zero resultant detects precisely half of a cyclotomic factor on the exponential scale. Put
$$ x=3^{U/2},\quad y=2^{(N-1)/2},\quad c=(b-1)/2,\quad
\sigma=\begin{cases}+1&c\equiv0,3\pmod4,\\-1&c\equiv1,2\pmod4.\end{cases} $$
Then the exact physical cancellation on $D_4$ is
$$ \gcd(D_4,C)=x^2-2\sigma xy+2y^2,\qquad
 D_4=(x^2-2xy+2y^2)(x^2+2xy+2y^2).                               \tag{8}$$
Indeed work modulo any divisor of $D_4$. Write $t=t_0=2y^2/x^2$, $\lambda=x/y$. Then $t^2=-1$. Using $aU+bN=1$ gives $z_0^{U/2}=\lambda t^{-c}$ as a positive rational identity. Hence $G(z_0,t_0)=0$ precisely when $\lambda=t^c(1-t^b)=\sigma(1-t)$. This implies $\lambda^2-2\sigma\lambda+2=0$. Conversely that quadratic gives $(\sigma\lambda-1)^2=-1$ and $t=2/\lambda^2=1/(\sigma\lambda-1)=1-\sigma\lambda$, proving the equivalence for every prime power. The two displayed integer factors are coprime: any common prime divides $4xy$, whereas both are odd and coprime to $xy$. This proves (8). Taking odd prime $N\to\infty$ and $U=2\lfloor N\log_3(2)/2\rfloor$ gives positive clocks tending to the critical slope with $\log\gcd(D_4,C)=(1+o(1))N\log2$ and $\log D_4=(2+o(1))N\log2$.

The [exact controls](colored_selected_controls.py) check all 2,320 noncoprime necklaces through length fifteen, including 78 inactive homogeneous factors and 5,466 nonzero prime-component short-binomial remainders. They also check the exact selected factor (8) on all 1,515 eligible parameter pairs through $N=149$, using the reconstructed physical bits and the original affine numerator.
