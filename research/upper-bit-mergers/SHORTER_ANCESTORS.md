# Constructing an ancestor in any prescribed binary residue class

**PROPOSED, unconditional.** All paths below are ordinary positive Collatz paths. Write $s=s_k(b)$ for the number of odd inputs in the first $k$ shortcut steps from an odd residue representative $0<b<2^k$. There is an effective integer $D(s)$ with

$$
\log D(s)=O\!\left(\frac{s}{\log(s+2)}\right)
$$

such that for every positive odd $t$ prime to three one can find

$$
n=b+2^k w,\qquad 0\le w<4t\,2^{D(s)},\qquad T^i(n)=t
$$

for some $i\le k+\lceil\log_2(2\cdot3^s)\rceil+D(s)$. Thus at most $D(s)+\lceil\log_2(4t)\rceil$ extra binary digits suffice, uniformly in the original residue. In fact one can prescribe **any** time $i=k+J$ with $J\ge\lceil\log_2(T^k(b)+1)\rceil+D(s)$ and obtain an ancestor visiting $t$ at exactly that time. The number of odd steps after time $k$ depends only on $s$. The bound on $w$ above is for the earliest allowed choice of $J$. The elementary one-exponent construction in [criterion (4)](README.md#an-unconditional-finite-criterion) costs $2\cdot3^{s-1}+O(\log t)$ extra digits for existence. This proof uses independent exponent choices and finite Fourier inversion. It constructs some ancestor in each class. The original prescribed integer in the class can have any orbit.

## Cancellation over an interval of exponents

Write $e(u)=\exp(2\pi i u)$. Let $L\ge2$ be an integer and $H=2\cdot3^{5L}$. For $m\ge2$ denote by $B_m$ the supremum of

$$
\left|\frac1H\sum_{v\in I}e(a2^v/3^m)\right|
$$

over all consecutive intervals $I$ of $H$ nonnegative exponents and all $3\nmid a$. With $D_m=\lceil m/L\rceil$,

$$
B_m\le 4\cdot3^{-L/2^{D_m}}. \tag{A}
$$

For $2\le m\le3L$, a full multiplicative period runs through the units modulo $3^m$. The additive character sums to zero on the units, by subtracting the sum over multiples of three from the sum over all residues. A remainder of a period contributes at most $3^{3L}/H$. The period length is $2\cdot3^{m-1}$, since $v_3(4^{3^i}-1)=i+1$.

For $m>3L$ take $J=3^L$ and $d=2\cdot3^{L-1}$. Average the $J$ translates by $0,d,\ldots,(J-1)d$ of the same normalized sum. End effects change its value by at most $2Jd/H$. Apply Cauchy–Schwarz in $v$ to the translated average and expand the square. The equal shifts contribute $1/J$. For two unequal shifts at distance $jd$, $1\le j<J$, the phase difference has denominator $3^{m'}$ in lowest terms, with

$$
m'=m-L-v_3(j),\qquad m-2L<m'\le m-L.
$$

In fact $v_3(2^{jd}-1)=L+v_3(j)$, by factoring powers of $4$, and the extra factor from the smaller shift is a unit. Hence

$$
B_m\le 2Jd/H+\sqrt{J^{-1}+\max_{m-2L<m'\le m-L}B_{m'}}.
$$

Here $m'>L$, so conductor one never enters the recursion. Put $\eta=3^{-L}$. The error $2Jd/H\le2\eta^3$. For $D_m=D$, the induction hypothesis in the square root is at most $4\eta^{1/2^{D-1}}$. The square root is at most $\sqrt5\,\eta^{1/2^D}$, proving (A) with the stated constant. This is an elementary differencing estimate.

## Ordered exponents with a prescribed residue

For sufficiently large $s$ set

$$
\ell=\lceil\sqrt s\rceil,\quad
L=\lceil 8s/\log_2 s\rceil,\quad H=2\cdot3^{5L},\quad Q=3^{s+\ell}.
$$

Choose a nonnegative integer $K$. Independently sample $v_i$ uniformly from $[K+iH,K+(i+1)H)$ for $0\le i<\ell$. Fix $v_\ell=J$ at **any prescribed** $J\ge V=K+\ell H$. The exponents are strictly increasing. For every integer $y$ and every odd unit $t$ we have, uniformly also in $K,J$,

$$
Q\,\Pr\left\{2^{v_\ell}t-\sum_{i=0}^{\ell-1}3^{\ell-1-i}2^{v_i}
               \equiv3^\ell y\pmod Q\right\}=\frac32+o(1). \tag{B}
$$

To see this, invert the indicator by additive characters modulo $Q$. Independence gives $\ell$ interval averages times one fixed phase for each frequency. The zero frequency contributes 1. Together the two characters of conductor three contribute $1/2$. The target is a multiple of three and only the variable with coefficient $-1$ survives modulo three. Its average is $-1/2$ over the even length $H$. The two fixed phases at $2^J t$ sum to $-1$, since $3\nmid t$.

For a character of conductor $3^m$ with $2\le m\le\ell+1$, the term vanishes. The variable with coefficient $-1$ averages over an exact number of periods because $\ell\le5L$. For $m>\ell+1$ every random factor has conductor $3^{m_i}$ with $2\le m_i\le s+\ell$ even after removing the power of three in its coefficient. By (A) each is bounded by $4\cdot3^{-L/2^{\lceil(s+\ell)/L\rceil}}$. The absolute error in (B) is at most

$$
Q\left(4\cdot3^{-L/2^{\lceil(s+\ell)/L\rceil}}\right)^{\ell}. \tag{C}
$$

For large $s$, $s+\ell\le2s$ and $2^{\lceil(s+\ell)/L\rceil}\le2s^{1/4}$. The negative term in the logarithm of (C) has magnitude at least a constant times $s^{5/4}/\log s$, while $\log Q+\ell\log4=O(s)$. Thus (C) tends to zero. In particular the count of successful tuples is asymptotic to $3H^\ell/(2Q)$ for every $y$, even with the last clock fixed. The estimates concern this explicit distribution on exponent tuples.

## From the congruence to a legal Collatz path

For a successful tuple set $x_\ell=t$ and, in reverse order, set

$$
x_i=(2^{v_{i+1}-v_i}x_{i+1}-1)/3,\qquad z=2^{v_0}x_0.
$$

Each division is exact. Reducing the numerator on the left of the congruence in (B) modulo three first forces $3\mid 2^{v_\ell-v_{\ell-1}}t-1$. Substitute $x_{\ell-1}$, divide the numerator by three and repeat. Each new $x_i$ is a positive odd integer, since its numerator is positive and odd and divisible by three. The identity $3x_i+1=2^{v_{i+1}-v_i}x_{i+1}$ certifies the exact number of halvings at every stage. Thus the shortcut path from $z$ reaches $t$ at time $v_\ell$, with exactly $\ell$ odd steps, and (B) gives $z\equiv y\bmod3^s$. Distinct successful tuples give distinct $z$ for fixed $\ell,t$ because the initial valuation of $z$ gives $v_0$ and its next $\ell$ odd-source valuations recover the successive differences.

Now put $g=3^s$, $y=T^k(b)$ and $K=\lceil\log_2(y+1)\rceil$. The prefix bound gives $0<y<2g$. We have $z\ge2^K>y$ and $z\le2^Jt$. Hence $w=(z-y)/g$ is a nonnegative integer, smaller than $4t\,2^{\ell H}$ when $J=K+\ell H$, using $2^K<4g$. The exact lift $T^k(b+2^k w)=y+gw=z$ proves the announced result with $D(s)=\ell H$ at large $s$. The displayed choices give $\log D(s)=O(s/\log(s+2))$.

For any larger $J$, the constructed endpoints $z$ lie in an interval of **fixed absolute width** as $J$ varies. Specifically,

$$
0<\frac{2^Jt}{3^\ell}-z
 =\sum_{i=0}^{\ell-1}\frac{2^{v_i}}{3^{i+1}}
 <\frac{2^V}{3^\ell}.
$$

Indeed $2^{v_i}\le2^{K+(i+1)H-1}$ and the resulting geometric sum has ratio $2^H/3>2$. This also locates the original sources by the linear formula for $w$. Visits to periodic targets need not be first visits.

All constants are effective. For $s<4$ or when (C) is at least 1, use one odd step and put $D(s)=2\cdot3^s$. For each $J\ge K+D(s)$ choose $v_0\in[K,K+D(s))$ with $2^{v_0}\equiv 2^Jt-3y\bmod 3^{s+1}$. The right side is a unit, and the interval contains a whole multiplicative period. The same inverse construction gives the claimed path. One can use this finite alternative whenever its cost is smaller. For the existential block criterion alone the earlier $2\cdot3^{s-1}$ bound is also available.

For example, take $b=5,k=3,t=7$. The prefix ends at $y=2$ and $s=1$. For $J=8$, $v_0=2$ gives $z=(2^8\cdot7-2^2)/3=596$, so $w=198$ and $n=1589$ reaches 7 at time 11. For $J=9$, $v_0=5$ gives $z=1184$, $w=394$ and $n=3157$ reaches 7 at time 12. Both sources have residue 5 modulo 8.

## Consequence for the full problem

In the finite criterion (4) replace $d=2\cdot3^{s_k(b)-1}$ by $D(s_k(b))$, both in the exponent of the weight and the endpoint of the sum. This is again equivalent to the full conjecture. If a second component contains an odd unit $t$, choose $t$ or 1 as the target of the construction so its membership in the basin of 1 differs from that of $b$. There is then a failed binary edge within $D(s)+\lceil\log_2(4t)\rceil$ extra bits in every cell. For $k\ge\lceil\log_2(4t)\rceil$, after multiplication by $2^{D(s)}$ that edge alone contributes at least $2^{1-\lceil\log_2(4t)\rceil}$ to the finite-budget sum. Conversely a finite block of pairs that actually merge always has a common finite budget. What remains unproved is that arbitrarily accurate blocks exist. No local-density or conjectural synchronization input is used in this deduction.

The source-qualified first-landing estimate gives stronger density and scale information when invoked. The elementary argument here supplies a direct bound on individual ordinary paths and an explicit distribution of short lists of exponent choices. [First-landing estimate and dependencies](https://github.com/GettysburgResearch/collatz/blob/4e94f656236485ebf854711528b06c18b91d4ad3/research/critical-orbit-mellin/LOCAL_FIRST_LANDING.md)
