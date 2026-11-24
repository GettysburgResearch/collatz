# Which polynomial factors can cancel a complete Collatz cycle denominator?

**PROPOSED written theorems.** On every coprime pair of clocks, uniformly over all words, the irreducible factors of any fixed bounded degree of the discrepancy polynomial can cancel only a subexponential part of the numerical divisor. All multiplicities are included. Even a changing subproduct of unbounded individual degrees can cancel only a subexponential part if its total degree is $o(p/\log p)$. A separate resultant bound applies to arbitrary arrangements of two different equal-clock blocks, with unrestricted common clock divisor and composite block counts allowed. Prime block counts give the full leading exponent for the reduced denominator. The fixed-source calculation in §5 inspects every long prefix of one hypothesized escape. The general exclusions of cycles and escape remain open.

## 1. One polynomial for the complete carry

Use the odd map $2^{e_i}x_{i+1}=3x_i+1$ with $e_i\ge1$, $p$ odd steps, cumulative exponents $E_i=\sum_{j<i}e_j$, and $A=E_p$. Write
$$
 C=\sum_{i=0}^{p-1}3^{p-1-i}2^{E_i},\quad D=2^A-3^p,\quad d=|D|/\gcd(D,C).
$$
The fixed point of this word is $C/D$. Its reduced denominator is $d$, and its sign is the sign of $D$. Every phase of the periodic extension has the prescribed odd parity since its rotated numerator and denominator are odd. The affine equations then verify the exact divisions. A positive ordinary cycle needs $D>0,d=1$.

For $\gcd(A,p)=1$ put $s_i=pE_i-Ai$, $K=-\min_i s_i$,
$$
 M(X)=\sum_{i<p}X^{K+s_i},\qquad S_p(X)=1+X+\cdots+X^{p-1}.
$$
The exponents are distinct modulo $p$, so $M$ is a monic 0/1 polynomial with constant one. Its reduction modulo $X^p-1$ is $S_p$, hence $M=S_p Q$ with $Q\in\mathbb Z[X]$, $Q(1)=1$. If $|D|>1$, take $u,v\in\mathbb Z$ with $up+vA=1$. In $(\mathbb Z/|D|)^\times$ set $z=2^u3^v$. Then $z^p=2,\ z^A=3$, giving the **full composite-modulus** identities
$$
 3^{p-1}M(z)=z^K C,\qquad (z-1)S_p(z)=1,\qquad
 \gcd(D,C)=\gcd(D,Q(z)).                                      \tag{1}
$$
Any integer representative of $z$ gives the same gcd. The cases $|D|=1$ are automatic. The Christoffel case $M=S_p$ recovers known exact coprimality. Linear-form ordering by $-s_i$ and the balanced carry identities are established antecedents. [Christoffel coprimality, Theorem 3](https://rstation.ai/problems/collatz/papers/4) · [Linear-form ordering](https://rstation.ai/problems/collatz/papers/27) · [PR195, balanced unit calculation](https://github.com/GettysburgResearch/collatz/blob/8edc24b576e7c7da56f99d882ce6fd1e014ee730/research/astra-global-closure-20261124/round3/cycles/CONGRUENCE_MODEL.md)

## 2. All bounded-degree cancellation is subexponential

Fix $k\ge1$ and a constant $B$. For every such word let $L_k$ be the product, with full multiplicity, of the monic irreducible factors of $M$ over $\mathbb Q$ of degree at most $k$, with empty product one. Uniformly for coprime clocks $p\le A\le Bp$ as $p\to\infty$,
$$
 \boxed{\ \log\gcd(|D|,L_k(z))=o_{k,B}(p).\ }                 \tag{2}
$$
This includes arbitrary gap changes, arbitrary discrepancy range, and every choice of the integer representative. Also $\log|D|=\max(A\log2,p\log3)-o_B(p)$. Thus on a sequence of ordinary cycles with these clocks the factors of $Q$ of degree greater than $k$, evaluated jointly at $z$, must absorb $\exp(\log|D|-o_{k,B}(p))$ of the full divisor for every fixed $k$. Indeed $\gcd(n,ab)\le\gcd(n,a)\gcd(n,b)$ and $S_p(z)$ is a unit. For ordinary positive cycles $A\le2p$ follows by multiplying $3x_i+1\le4x_i$.

**A finite set of roots, with multiplicities accounted for.** Every root of any such $M$ has modulus less than 2, since the leading monomial dominates all the others at $|X|\ge2$. Every monic integer factor has constant term $\pm1$, so its roots are algebraic units. The coefficients of a monic factor of degree $j\le k$ are bounded by $2^j\binom ji$ in degree $j-i$. Only finitely many factors occur for fixed $k$. A non-torsion algebraic unit has a conjugate $\beta$ strictly inside the unit disk. Indeed if all conjugates have modulus one, the monic integer polynomials of their componentwise powers have bounded coefficients. Two such powers coincide as multisets, and iterating their permutation shows that the conjugates are roots of unity. The unit norm rules out all conjugates having modulus at least one with any strictly above one. Fix $|\beta|<r<1$. On $|X|=r$ every mask satisfies $|M(X)|\le(1-r)^{-1}$, and $M(0)=1$. Jensen's inequality for zeros in a disk bounds the multiplicity of $\beta$ by $\log(1/(1-r))/\log(r/|\beta|)$. Equivalently, divide out each disk Blaschke factor with zero at $\beta$ and modulus one on $|X|=r$, and apply the maximum principle at zero. This bound is independent even of the degree of $M$.

**Prime-power control for a non-torsion factor.** Work in a fixed splitting field $K_0$ of the finitely many factors just obtained. For every root $\theta$ and every prime ideal $\mathfrak l$ above a rational prime dividing $D$, use the integral valuation $v_\mathfrak l$. If $z$ now denotes an integer lift, (1) gives
$$
 \min(v_\mathfrak l(D),v_\mathfrak l(z-\theta))\le
 \min(v_\mathfrak l(\theta^p-2),v_\mathfrak l(\theta^A-3)).
$$
This follows by subtracting $z^n-\theta^n$, divisible by $z-\theta$. For a monic factor $P$, sum over its roots using $\min(a,\sum b_j)\le\sum\min(a,b_j)$. Summing the prime valuations with weights $\log N\mathfrak l/[K_0:\mathbb Q]$ counts the rational $\log\gcd(D,P(z))$ exactly on the left before this upper bound.

Apply Corvaja–Zannier, Proposition 2, to $(u',v')=(\theta^p/2,\theta^A/3)$. These lie among the units outside the fixed places above 2, 3 and infinity. At the primes contributing to $D$, division by 2 and 3 changes no valuations. With normalized absolute values, Proposition 2 bounds $-\sum_w\log^-\max(|u'-1|_w,|v'-1|_w)$ by $\epsilon\max(h(u'),h(v'))$, apart from finitely many pairs and finitely many subgroups through the identity; here $\log^- t=\min(0,\log t)$. The sum with its minus sign bounds the required nonnegative contribution over the primes of $D$. At places above 2 and 3 the valuations of $\theta$ vanish, and the respective valuations of 2 and 3 force any relation $(u')^a(v')^b=1$ to have $a=b=0$. Thus none of these pairs is in an exceptional one-dimensional subgroup. The isolated exceptions contribute only finitely many clocks because $\theta$ is non-torsion. The heights are $O_{\theta,B}(p)$. Taking arbitrary $\epsilon>0$, summing over the fixed finite root list and using the uniform multiplicity bounds gives $o_{k,B}(p)$. It matters that Proposition 2 concerns the common target $(1,1)$: its exception is a subgroup, whereas other theorems in that paper allow translates. [Corvaja–Zannier, Proposition 2, pp. 7–8](https://arxiv.org/pdf/math/0311030)

**All torsion multiplicities at once.** For a root of unity of order $m$ on our finite list, its cyclotomic polynomial divides $X^m-1$. If a rational prime $\ell\mid D$ divides the factor value at $z$, then $z^m=1\bmod\ell$ and $2^m=1\bmod\ell$. All such primes belong to a fixed finite set $P_k$. Their combined contribution, including every power and every repeated factor, is at most the $P_k$-part of $|D|$. For $w=2^A/3^p$ use the one-variable $S$-unit approximation-to-one estimate recorded in the proof of Proposition 2 on p. 7 (Ridout's theorem), with $S$ containing $P_k,2,3,\infty$. For every $\epsilon>0$,
$$
   \prod_{v\in S}\min(1,|w-1|_v)\ge \exp(-\epsilon h(w))
$$
outside finitely many $w$. Unique factorization makes these finitely many clock pairs. At any prime dividing $D$ the denominator of $w$ is a unit. Thus the logarithm of the indicated prime part is $o_B(p)$. The same estimate at infinity gives the claimed estimate for $\log|D|$ since $|D|/\max(2^A,3^p)=|1-\min(w,1/w)|$. This proves (2). The small-o constants provide no effective threshold. [Corvaja–Zannier, proof of Proposition 2](https://arxiv.org/pdf/math/0311030)

### An effective bound for moving factors of arbitrary degree

A different estimate allows the factor itself to change with both clocks. For every monic subproduct $P\mid M$ of positive degree $r$ (including repeated factors), every integer $N\ge1$ and $p\le A\le Bp$, let $\mathcal M(P)=\prod_{P(\theta)=0}\max(1,|\theta|)$ be its Mahler measure, with multiplicities. There is a constant $c_B$ depending only on $B$ such that
$$
 \log\gcd(|D|,P(z))
 \le c_B rN + \frac pN \log\mathcal M(P)
 \ll_B r+\sqrt{p r\log p}                                      \tag{2a}
$$
where the final bound is for the optimized choice of $N$ and $p\ge2$. For example, every changing subproduct of total degree $o(p/\log p)$ can cancel only $\exp(o(p))$, regardless of how large any single irreducible degree becomes. If the subproduct consists of cyclotomic factors of unbounded orders, take $N=1$ and $\mathcal M(P)=1$ for the bound $O_B(r)$.

Indeed the pigeonhole principle on the fractional parts $jA/p$, $0\le j\le N$, gives $1\le f\le N$ and an integer $e$ with $|pe+Af|\le p/N$ and $|e|\le BN+1$. Reversing both signs if needed, write $k=pe+Af\ge0$ and $2^e3^f=a/b$ in lowest positive terms. Then $z^k=a/b\bmod |D|$, with both $a,b$ units there, and $\log(2\max(a,b))\le c_B N$. The integer resultant of $P$ and $bX^k-a$ is a multiple of $\gcd(D,P(z))$ by its integral Bézout identity evaluated at $z$. It is nonzero: every root of $P$ is an algebraic unit, whereas $a/b$ has a nonzero valuation above three because $f\ne0$. This also covers $k=0$. Its absolute value is bounded by $(2\max(a,b))^r\mathcal M(P)^k$, using the product over all roots of the monic $P$. Finally $\mathcal M(P)\le\mathcal M(M)\le\sqrt p$. For the second inequality apply the usual one-variable Jensen formula to the monic polynomial on the unit circle, then concavity of log and orthogonality of its distinct monomials: $\int_0^1|M(e^{2\pi it})|^2dt=p$. The first uses multiplicativity and the fact that the monic complementary factor has Mahler measure at least one. Taking $N=\max(1,\lceil\sqrt{p\log p/r}\rceil)$ gives (2a).

In particular an actual coprime-clock ordinary cycle would need aggregate degree $\gg_B p/\log p$ among the factors of $Q$ of degree **greater** than any fixed $k$, for all sufficiently large $p$ depending on $k,B$. To see this, (2) charges $\log|D|-o_{k,B}(p)\gg_B p$ to the joint gcd of those factors. Apply (2a) to their full product. This conclusion concerns the high-degree part after removing the always-present unit $S_p(z)$ and after discarding every bounded-degree irreducible with its full multiplicity. It supplies no upper bound on that remaining degree.

## 3. An exact certificate for moving high-degree factors

If $M\mid X^{Lp}-1$ in $\mathbb Z[X]$, then
$$
                   \gcd(D,C)\mid 2^L-1.                         \tag{3}
$$
Indeed evaluate at $z$ and use (1). The same proof bounds the contribution from any subproduct dividing $X^{Lp}-1$. Thus a family with $L=o(p)$ can discard this moving subproduct *and* the complete bounded-degree part for a joint loss $\exp(o(p))$. Even if the two overlap, assign repeated factors to just one of the two products. Conversely a nontrivial ordinary cycle with such a mask would require $|D|\le2^L-1$.

Here are two families showing the range of (3).

* If $p,A$ are odd and coprime with $1<A/p<2$, take discrepancy representatives $s_i$ in $\{0,2,\ldots,2p-2\}$ satisfying $s_i\equiv-Ai\bmod p$, and take $s_p=s_0=0$. The actual gaps are $e_i=(A+s_{i+1}-s_i)/p$. Writing $s_i=2r_i$, the increment of $r_i\bmod p$ is $(3p-A)/2$ modulo $p$. Hence the two gaps are $3,1$. Their sum is $A$, so precisely $(A-p)/2$ gaps equal three. The mask is $1+X^2+\cdots+X^{2p-2}$ and divides $X^{2p}-1$. Because $3\nmid D$, (3) gives **$d=|D|$**. There are contracting coprime odd clocks with $A-p\log_2 3\to0^+$: choose positive odd $p$ so that $p\log_2 3$ approaches the next odd integer from below by density of irrational rotation modulo 2, then divide both odd clocks by their gcd. The positive discrepancy can only decrease and the reduced clocks are unbounded. In this near-critical family a positive proportion of the gaps are three, whereas the same-clock ordinary mechanical gap word uses only one and two.
* Put $p=2^j$, $j\ge3$, and take any odd $A$ with $3p/2<A<2p$. For $h=0,\ldots,j-1$ choose $c_h=1$ or 3 when $h<j-2$, and $c_h=1$ otherwise. The subset sums of $c_h2^h$ are a complete set modulo $p$: the lowest differing digit gives an exact valuation less than $j$. Their maximum is at most $p-1+2(p/4-1)<3p/2$. For each $i$ take the representative $s_i$ of $-Ai\bmod p$, putting $s_p=s_0=0$. Every $(A+s_{i+1}-s_i)/p$ is a strictly positive integer. These are legal gaps, and the polynomial is $\prod_{h<j}(1+X^{c_h2^h})$. Every root has order dividing $3p$; the roots from a given factor have orders of exact dyadic valuation $h+1$, and that factor has simple roots. Therefore $M\mid X^{3p}-1$ and $d\ge |D|/7$ for every set of choices. Different choices give different masks, since choosing 3 at level $h$ adds exactly the roots of order $3\cdot2^{h+1}$. Normalizing the minimum exponent to zero makes the mask invariant under cyclic word rotation, so these give $2^{j-2}$ distinct cyclic words. For $h=j-3$ alone changed to 3, the normalized representatives exceed their usual values in $[0,p)$ by $p$ on exactly $p/8$ residues, the interval $[p/8,p/4)$. Thus $p/8$ odd positions move one shortcut step from the same-intercept mechanical word. One may choose the least odd $A$ above $p\log_2 3$ for a positive realization and a denominator growing exponentially with $p$ by §2.

## 4. Arbitrary arrangements of equal-clock blocks

Use shortcut bits, even step $x/2$, odd step $(3x+1)/2$. Split a cyclic word into a prime number $g$ of blocks with common length $b\ge1$ and weight $r\ge1$. Write $u=2^b,\ v=3^r$, so block $i$ has map $(v x+c_i)/u$ with its literal integer carry $c_i$. No coprimality of $b,r$ is required. Put
$$
 H=\frac{u^g-v^g}{u-v},\qquad
 D=u^g-v^g,\qquad C_*=\sum_{i=0}^{g-1}u^iv^{g-1-i}c_i,\qquad d=|D|/\gcd(D,C_*).
$$
If the $c_i$ are not all equal and $\bar c=g^{-1}\sum c_i$, then
$$
 d\ \ge\
 \frac{H}{\left(\frac{g}{g-1}\sum_{i<g}(c_i-\bar c)^2\right)^{(g-1)/2}}. \tag{4}
$$
When every carry belongs to the two-element set $\{c_0',c_1'\}$, put $\Delta=c_1'-c_0'$, and let $1\le K<g$ be the number of occurrences of $c_1'$. The sharper estimate is
$$
 \boxed{\quad d\ge\frac{H}{\gcd(H,\Delta)}
       \left(\frac{g-1}{K(g-K)}\right)^{(g-1)/2}.\quad}          \tag{5}
$$
For a fixed choice of distinct equal-clock blocks this holds for every one of their $2^g-2$ nonconstant arrangements. A shortcut interchange $01\longleftrightarrow10$ at the same position changes the carry by a signed product of powers of two and three, so in that case $\gcd(H,\Delta)=1$.

To prove (4), note $H$ is coprime to 6 and $\Phi_g(u/v)=0\bmod H$, with $\Phi_g(X)=1+\cdots+X^{g-1}$. For $P(X)=\sum c_i X^i$, the integer resultant $\operatorname{Res}(\Phi_g,P)$ lies in the ideal of $\mathbb Z[X]$ generated by these two polynomials, by the adjugate of the Sylvester matrix. Its absolute value is nonzero: $\Phi_g$ is irreducible and a multiple of degree at most $g-1$ has constant coefficients across this list. Reduction modulo $H$ gives $\gcd(H,C_*)\mid\operatorname{Res}(\Phi_g,P)$ because $v$ is a unit there. If $\zeta$ is a primitive complex $g$th root, the absolute resultant is $\prod_{j=1}^{g-1}|P(\zeta^j)|$. Orthogonality gives $\sum_{j=1}^{g-1}|P(\zeta^j)|^2=g\sum_i(c_i-\bar c)^2$. Apply arithmetic-geometric mean. Finally $\gcd(D,C_*)\le|u-v|\gcd(H,C_*)$, yielding (4).

For (5), write $P=c_0'\Phi_g+\Delta J$ for the binary choice polynomial $J$. Only the residue $\Delta J(u/v)$ matters modulo $H$. Extract at most one factor $\gcd(H,\Delta)$ before applying the resultant argument to $J$; its nontrivial-frequency squared sum is $K(g-K)$. This preserves prime powers even when $H$ and $u-v$ are not coprime.

For $u>v$ we have $H\ge u^{g-1}$. Each block carry is at most $2^{b}3^r$ times $b$ directly from the affine sum, so $\log(1+|\Delta|)=O(b+\log b)$. Also the logarithm of the spectral loss in (5) is at most $(g-1)\log g/2$. Consequently if $g\to\infty$ through primes, $\log g=o(b)$ and $u>v$, every nonconstant arrangement has $\log d\ge(1-o(1))gb\log2$. Since $d\le|D|<2^{gb}$ this gives the full leading exponent. This allows an unbounded common divisor of the total clocks and exponentially many unprescribed block choices.

**Composite block counts and every primitive binary arrangement.** For any integer $g\ge2$ retain the divisors $m>1$ of $g$ such that $\Phi_m$ does not divide $J$ in $\mathbb Z[X]$. Let $\mathcal T$ denote this set, $n=\sum_{m\in\mathcal T}\varphi(m)$, and
$$
 H_{\mathcal T}=\prod_{m\in\mathcal T} v^{\varphi(m)}\Phi_m(u/v).
$$
The nonconstant hypothesis gives $n>0$. Then
$$
 d\ \ge\ \frac{H_{\mathcal T}}{\gcd(H_{\mathcal T},\Delta)}
       \left(\frac{n}{K(g-K)}\right)^{n/2},\qquad
 H_{\mathcal T}\ge (u/2)^n\quad(u>v).                         \tag{5a}
$$
Indeed $H_{\mathcal T}$ divides $H$ by the cyclotomic factorization. The unit $u/v$ is a root of $\prod_{m\in\mathcal T}\Phi_m$ modulo $H_{\mathcal T}$, and $\gcd(H_{\mathcal T},C_*)$ divides $\gcd(H_{\mathcal T},\Delta)$ times the absolute resultant of that product and $J$. The resultant is the product on the $n$ active nontrivial frequencies. All other nontrivial frequencies give zero, so the same Parseval sum is $K(g-K)$. This proves the first inequality even when the integral homogeneous cyclotomic values have common prime factors. For the second, $|1-t\zeta|\ge|1-\zeta|/2$ when $0\le t\le1$, since $1-t\le|1-t\zeta|$. In a complete primitive order-$m$ class the product of $|1-\zeta|$ is $|\Phi_m(1)|\ge1$. Use $t=v/u$.

If the binary arrangement has least period $g$, then $n+1\ge\log_2 g$. Its $g$ distinct cyclic rotations belong to a complex vector space of dimension at most $n+1$, obtained by taking only the active Fourier coordinates and the constant coordinate. Some $n+1$ or fewer ordinary coordinate projections distinguish every vector in this space, by the rank of a basis matrix. The rotations are binary in those coordinates, yielding the count. Consequently, if $u>v$, $g\to\infty$ and $\log g=o(b)$, then every such primitive binary arrangement of any pair of different equal-clock blocks satisfies
$$
                         \log d\ge(1-o(1))\,n b\log2 .
$$
Here $\log\gcd(H_{\mathcal T},\Delta)=O(b+\log b)$ and the remaining logarithmic losses are $O(n\log g)$, whereas $n\to\infty$. The two different words do have different carries: $-c_i3^{-r}\bmod 2^b$ determines the unique starting residue for their parity word, and the forward branches at that residue recover every bit. A shortcut word of least bit period $gb$ gives a binary arrangement of least period $g$. Thus all primitive words admitting the stated two-block description in this range are excluded from integer cycles. No proof forces an arbitrary cycle into such a split.


## 5. Periodizing every prefix at one fixed escaping source

Assume one positive odd orbit $x=q_0,q_i=U^i(x)$ escapes. Its odd states are pairwise distinct and synchronously nonmerging, so the translated counting bound in PR193 gives $\#\{q_i\le R\}=O(R^\theta)$ for some $\theta<1$. Dyadic shells then give $\sum 1/q_i<\infty$. Define
$$
 H(x)=x\prod_{j\ge0}\left(1+\frac1{3q_j}\right),\qquad
 L(x)=H(x)-x,\qquad \lambda_i=2^{E_i}/3^i .
$$
The same definition on the tails gives $H(q_i)=H(x)/\lambda_i$ and $H(q_i)/q_i\to1$. In particular $\lambda_i q_i\to H(x)$, $\lambda_i\to0$, and $L(q_i)\ge1/3$ from the very first product factor. These are consequences of the convergent ordinary product, without selecting new starts at different horizons. [PR193, fixed-source packing](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/escape.md) · [Corrected height](https://github.com/GettysburgResearch/collatz/blob/a1379492dbaae85e0d16662b41ccc7176ab3c66e/research/astra-global-synthesis-20261124/section/proof.md)

For every sufficiently long prefix let $R_i=C_i/(2^{E_i}-3^i)$ be its periodic rational phase with reduced positive denominator $d_i$. No coprimality of the clocks is assumed. The affine identity gives
$$
 R_i-x=\frac{2^{E_i}(q_i-x)}{2^{E_i}-3^i},\qquad
 \gcd(2^{E_i}-3^i,C_i)=\gcd(2^{E_i}-3^i,q_i-x).
$$
Thus the prefix phases tend to the **negative** real number $-L(x)$, while converging to the **positive** $x$ in $\mathbb Z_2$. More precisely
$$
 R_i+L(x)=\frac{\lambda_i}{1-\lambda_i}\big(L(q_i)-L(x)\big),
 \quad v_2(R_i-x)=E_i+v_2(q_i-x),\qquad
 d_i\ge(1-o(1))\,\frac{2^{E_i}}{H(x)}.                         \tag{6}
$$
For the last inequality use $d_i\ge3^i(1-\lambda_i)/(q_i-x)$ for large $i$ and $\lambda_i q_i\to H(x)$. For the real limit one may directly substitute this convergence in the formula for $R_i-x$. It also follows that $L(q_i)$ is eventually injective as a sequence: if $H(x)$ is irrational, equality at two times would make a nonzero rational multiple of $H(x)$ an integer, since distinct $3^i/2^{E_i}$ are unequal. If $H(x)$ is rational, then eventually $v_2(H(q_i))=v_2(H(x))-E_i<0$ are strictly decreasing. Subtracting the integer $q_i$ preserves these distinct valuations.

Here is the obstruction to a natural attempt to exclude this escape by approximating $H=H(x)$. At $i\ge1$ use the *primitive integer pair* $X_i=2^{E_i}q_i,\ Y_i=3^i$, since $3\nmid q_i$. Take the two linear forms $(HY_i-X_i,Y_i)$ at infinity and $(X_i,Y_i)$ at each of 2 and 3. Their unnormalized product of absolute values is exactly
$$
 |HY_i-X_i|\,Y_i\,2^{-E_i}\,3^{-i}=H(q_i)-q_i\ge1/3.          \tag{7}
$$
Even granting algebraicity of $H$, the product would have to fall below a *negative power* of the pair height to trigger the usual Subspace Theorem with these forms. The fixed carry supplies the lower bound at every time. Formula (6) gives a necessary denominator lower bound for every long prefix on this same source. Neither (2) nor (5) bounds that denominator in the opposite direction. Likewise no argument forces the moving high-degree factors in (2) to contribute less than $D$, or forces an arbitrary cycle into (5).

## Formal scope

[MaskDenominator.lean](MaskDenominator.lean) imports only Std. Its unbounded list theorem relates every carry term to its shifted discrepancy exponent modulo a composite integer given the two clock congruences. It also proves the evaluated divisibility transfer in (3), the arbitrary-list carry decomposition and geometric difference used in (4)–(5a), and the integral prefix identity in (6). Polynomial factorization, the choice of the Bézout generator, ideal valuations, the Subspace Theorem, the resultant bounds and real or dyadic limits are written proofs. Lean 4.34.1 compiled all five printed declarations with warnings as errors, using propext, Classical.choice and Quot.sound.

[Exact integer replay](check.py) passed in normal and optimized Python modes. Each checked 2,307 word/carry congruences at full integer moduli, 443 explicit torsion masks, and 2,026 block selectors, including 468 with inactive nontrivial Fourier frequencies. These finite checks exercise the algebra and do not test escape or the imported asymptotic theorem.
