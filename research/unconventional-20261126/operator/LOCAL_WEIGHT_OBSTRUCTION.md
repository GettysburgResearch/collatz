# Ordinary near-invariants for weights with finitely many local singularities

**PROPOSED theorem with a written proof.** The one-edge obstruction survives a class of arithmetic weights considerably larger than the nonincreasing weights in [O5](WEIGHTED_GAP.md). It addresses a particular attempted positive Lyapunov estimate. Weighting an odd climb by $3^{v_3(n+1)}$ can compensate for its growth since $v_3(Tn+1)=v_3(n+1)+1$ on an odd shortcut step. The construction below arranges that neither end of a complete, certified growing segment receives an unbounded correction from any prescribed finite list of local singularities.

Let $S$ be a finite set of primes. At each $\ell\in S$, let $E_\ell\subset\mathbb Z_\ell$ be finite and let $h_\ell$ be positive and locally bounded above and away from zero on $\mathbb Z_\ell\setminus E_\ell$. Assume a finite positive value for the resulting weight at every positive ordinary integer, including any ordinary exceptional point. Suppose
$$
   w(n)=n^{-\sigma}\prod_{\ell\in S}h_\ell(n),\qquad
   \sigma>0,\qquad \sum_{n\ge1}w(n)<\infty.                         \tag{1}
$$
Arbitrary finite powers of the local absolute values of fixed nonzero polynomials are examples when (1) holds and values at ordinary zeros are assigned separately. Bounded positive multiplicative changes with uniform lower bound leave the conclusion unchanged.

**Theorem O7.** For every sufficiently large $k$ there are infinitely many pairwise disjoint ordinary predecessor cones $D_z$ in the basin of 1. Each indicator satisfies exact doubling invariance and has a single nonzero shortcut edge residual at its odd root $z$. For any $1\le p<\infty$ and every vector in the closed span of these indicators,
$$
       \|f-f\circ T\|_{p,w}
       \le C(2/3)^{k\sigma/p}\|f\|_{p,w}.                         \tag{2}
$$
Here $C$ can depend on the local weights, $\sigma$ and $p$; it is independent of $k$ and of the member of the family. Arbitrary finite anchors can be removed. This invalidates a strict gap obtained solely by this class of local corrections, even on the known component.

### 1. Choose three ordinary exponents

If necessary supplement $S$ with 2 and 3, assigning the constant function 1 there. Choose a fixed positive odd $e$, and fixed positive $d,r$, so that
$$
  b_e=-\frac{2^e+1}{3}\notin E_2\cup E_3,\qquad
  b_{2,r}=(2/3)^r-1\notin E_2,\qquad
  b_{3,d}=-2^{-d}\notin E_3.
$$
Membership is tested in the indicated local fields. Each displayed sequence gives distinct rational numbers as its chosen exponent varies; odd $e$ makes $b_e$ integral also at 3. The finite forbidden sets permit the choices.

For each sufficiently large $k$, impose on $L$ the congruence
$$
    2^L\equiv-1+(2^d-1)3^r2^{-(d+r)}
       \pmod {3^{2k+r}}.                                           \tag{3}
$$
The right side is a ternary unit congruent to $-1\bmod3$. Since $2$ is a primitive root at every power of 3, (3) gives an arithmetic progression of odd positive exponents with period $J_0=2\cdot 3^{2k+r-1}$. One elementary check is $v_3(4^{3^j}-1)=j+1$, by applying the factorization $u^3-1=(u-1)(u^2+u+1)$ at $u\equiv1\bmod3$; each cubing adds exactly one to the valuation.

Use sufficiently large exponents from this progression and set
$$
   z=\frac{2^r(2^L+1)}{3^r}-1,\qquad
   y=\frac{2^dz+1}{3^k},\qquad n=2^ky-1,\qquad
   x=\frac{2^e n-1}{3}.                                           \tag{4}
$$
Congruence (3) implies $3^r\mid 2^L+1$ and $3^{2k}\mid 2^dz+1$. Thus $z,y,n$ are odd positive integers for large $L$, and $3^k\mid y$. As $n\equiv-1\bmod3$ and $e$ is odd, $x$ is also an odd positive integer. Its next accelerated odd state is $n$. From $n$, exactly $k$ consecutive odd shortcut inputs produce $3^k y-1=2^d z$. Then $d$ halvings give $z$. From $z$, exactly $r$ consecutive odd shortcut inputs produce $2^L$, which reaches 1. The word can be verified directly from $T^j(2^a u-1)=3^j2^{a-j}u-1$ for $j\le a$ and $u>0$.

Since $z=(3^k y-1)/2^d$ and $x=(2^e(2^ky-1)-1)/3$, we have
$$
                  z/x\ge c_{d,e}(3/2)^k.
$$
For example $3^k y-1\ge 3^k y/2$ and $x\le 2^{e+k}y/3$ suffice. The $z$ from distinct exponents $L$ have disjoint cones: before the first power of two their remaining route has exactly $r$ odd inputs, and the first power is $2^L$. If the orbit of one such odd target $>1$ met another, its first power of two would be the same. After that first power it can visit only powers of two.

### 2. Keep both endpoints out of the exceptional neighborhoods

At 2 and 3 equations (4) give
$$
 x-b_e=\frac{2^{e+k}y}{3},\qquad
 z-b_{2,r}=\frac{2^{L+r}}{3^r},\qquad
 z-b_{3,d}=\frac{3^k y}{2^d}.
$$
The first difference tends to zero in both local fields, uniformly as $k\to\infty$, by $3^k\mid y$. The second tends to zero at 2 as $L\to\infty$, and the third tends to zero at 3 as $k\to\infty$. Local upper and lower bounds at the three chosen limits thus give constants working for all large $k,L$.

For $\ell\in S\setminus\{2,3\}$ both $z$ and $x$ are affine functions of $2^L$ with $\ell$-adic unit slopes. For $x$ this follows by substitution in (4): its slope as a function of $z$ is $2^{e+k+d}/3^{k+1}$, while the slope of $z$ is $2^r/3^r$. Let $B=\prod_{\ell\in S,\ \ell>3}(\ell-1)$, taking $B=1$ when the product is empty, and restrict further to $L=L_0+Jt$ with $J=J_0 B$ and $L_0$ one solution of (3). Put
$$
       c_\ell=v_\ell(2^{2B}-1)\ge1.
$$
Then $v_\ell(2^J-1)=c_\ell$ uniformly in $k$, since $J/(2B)$ is a power of 3. For $h>c_\ell$, the order of $2^J\bmod\ell^h$ is $\ell^{h-c_\ell}$. Both assertions follow from the elementary odd-prime identity
$v_\ell(u^a-1)=v_\ell(u-1)+v_\ell(a)$ for $u\equiv1\bmod\ell$, obtained by binomial expansion for $a=\ell$ and for $a$ prime to $\ell$.

Choose once and for all $H_\ell>c_\ell$ such that $\ell^{H_\ell-c_\ell}>2|E_\ell|$. Excluding the residue modulo $\ell^{H_\ell}$ of every exceptional point, at each of $x$ and $z$, forbids at most $2|E_\ell|$ values of $2^L$ because both affine slopes are units. As $t$ varies modulo $\ell^{H_\ell-c_\ell}$ the available values are all distinct. Select one allowed $t$ for each prime and combine by the Chinese remainder theorem on these prime-power moduli. This leaves arbitrarily large exponents $L$ satisfying all the requirements simultaneously. The complements of the excluded local residue balls are compact and avoid $E_\ell$, so each $h_\ell$ is bounded above and below there by finite positive constants.

Consequently $w(x)\ge c x^{-\sigma}$ and $w(z)\le C z^{-\sigma}$ uniformly on the constructed endpoints. The cone contains $x$, so $w(z)/w(D_z)\le C'(2/3)^{k\sigma}$. The one-edge residual and closed-span summation in O5 now prove (2). This does not assert boundedness of composition on the full weighted space for arbitrary local functions. The displayed closed spans do lie in its domain. The mechanism does not exclude weights using unbounded orbit history or singular sets that cannot be avoided by these finite choices.
