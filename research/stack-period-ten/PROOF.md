# A minimal-period-ten stack family with irrational 2-adic context

**PROPOSED.** Let $t_j=1$ if $j\equiv1,2\pmod {10}$ and $t_j=0$ otherwise, for all integer j. For every integer $d\ge2$, define the positive increment directive
$$
 d_j=d+t_j-2t_{j-1}+t_{j-2}\quad (j\ge1).
$$
This directive has minimal period ten. For every initial stack height $m\ge0$, its native stack value $\Theta$ in $\mathbb Q_2$ is irrational. An arbitrary finite steering prefix of positive increments leaves this conclusion intact. Thus this prescribed periodic architecture cannot start from an ordinary context. This theorem does not classify arbitrary period-ten words.

PR #20, head `82ca2f932438a9fe0897704ba62959ca23ec830f`, supplies the stack interpretation in `research/padic-repetition/claims/L-9407-stack-partial-theta-normal-form.md` and finite steering transfer in L-9408. The same source's L-9418 and T-9422 use delayed Padé approximation and give native irrationality through period nine. Its R-9410 ceiling concerns the complete equal-phase family at period ten. Here the alternating sum of the *unblocked* periodic weights vanishes, yielding a different cancellation polynomial of degree nine for ten time positions. The argument below uses one completion throughout.

## 1. The weighted quadratic series

Over one period the increments are $d+1,d-1,d-1,d+1,d,d,d,d,d,d$. Positivity follows from $d\ge2$. The positions of $d+1$ modulo ten are $1,4$ and are invariant under none of the proper divisor shifts $1,2,5$. Set $T=64/81$, $m_j=m+\sum_{i=1}^j d_i$, and $H_j=\sum_{i=1}^j(9m_i+1)$ with $H_0=0$. Telescoping, using $t_{-1}=t_0=0$, gives
$$
 H_j=A{j\choose2}+Bj+9t_j,
 \qquad A=9d,\qquad B=9m+1+9d.
$$
Put $q=T^A$, $z=T^B$ and $w_j=T^{9t_j}$. The value required by the stack context is
$$
 \Theta=F(1),\qquad F(Y)=\sum_{j\ge0}w_j z^j q^{\binom j2}Y^j.
$$
Use the backward shift $(Sw)_j=w_{j-1}$ on rational ten-periodic vectors. The polynomial
$$
 L(X)=\sum_{i=0}^9(-X)^i
$$
satisfies $L(S)w=0$, since each parity class has one exceptional entry $T^9$ and four entries 1. Also $L(X)=-X^9L(X^{-1})$. These two identities give cancellation and control the first nonzero error respectively.

## 2. A delayed denominator and its exact error

Take even $n\ge2$, $M=37n/2$ and $D=9n$. Define
$$
 \prod_{s=0}^{n-1} L(q^{M+s}X)=\sum_{k=0}^D p_kX^k,
 \qquad b_k=p_k z^k q^{-\binom{k+1}{2}},
 \qquad V(Y)=\sum_{k=0}^D b_kY^k.
$$
Each monomial of $p_k$ is signed $q^{Mk+u}$ with $0\le u\le9\binom n2$, from selecting at most nine copies of s at each index s. Since $D<M$, all exponents in $p_kq^{-\binom{k+1}2}$ are nonnegative. Thus $V(1)$ is a 2-adic unit by $b_0=1$ and the positive power $z^k$ when $k>0$.

Write $\Gamma_j=[Y^j]V(Y)F(Y)$, and let $U(Y)=\sum_{j=0}^{M-1}\Gamma_jY^j$. For $j\ge D$, direct convolution gives
$$
 \Gamma_j=z^j q^{\binom j2}
 \left[\prod_{s=0}^{n-1}L(q^{M+s-j}S)w\right]_j.                  \tag{1}
$$
Indeed $\binom{j-k}{2}-\binom{k+1}{2}=\binom j2-jk$. At $M\le j<M+n$ one commuting factor equals $L(S)$, so $\Gamma_j=0$.

At $j\ge j_0=M+n$ reverse each factor in (1) using reciprocity of L. This gives
$$
 \Gamma_j=(-1)^n z^j q^{\binom j2-D(j-M)+9\binom n2}
 \left[\prod_{s=0}^{n-1}L(q^{j-M-s}S^{-1})w\right]_{j-D}.         \tag{2}
$$
All exponents $j-M-s$ here are positive. The bracket equals $w_{j-D}$ modulo $2^{6A}$ in $\mathbb Z_2$. Since $w_{j-D}$ has valuation 0 or 54 and $6A\ge108$, the bracket has valuation exactly $54t_{j-D}$. Formula (2) yields the exact first error
$$
 v_2(\Theta-U(1)/V(1))
 =6\left[A\left({j_0\choose2}-9\frac{n(n+1)}2\right)+Bj_0+9t_{j_0-D}\right].       \tag{3}
$$
In detail, the valuation in (2) increases from j to j+1 by at least $6[A(j-D)+B-9]>0$. The first tail coefficient therefore survives in the 2-adically convergent sum at $Y=1$. Division by the unit $V(1)$ preserves its valuation.

## 3. Archimedean height and irrationality

Both $U(1)$ and $V(1)$ are integer sums of nonnegative powers of $T$ with exponents at most
$$
 K=A\left[{M\choose2}+9{n\choose2}\right]+BM+9.                   \tag{4}
$$
For a monomial contributing to $\Gamma_j$ with $j<M$, the q exponent is $\binom j2+(M-j)k+u$, $k\le j$ and $u\le9\binom n2$. The first two terms are at most $Mj-j(j+1)/2\le\binom M2$. The factors $z^j w_{j-k}$ supply at most $BM+9$ more T powers. For $b_k$ the q exponent is $Mk-k(k+1)/2+u$ with the same bound. This also verifies nonnegativity for every monomial in (4).

The product of n polynomials L has at most $10^n$ expanded terms, counting multiplicity. For each $j<M$ every one contributes at most one convolution monomial. Because $0<T<1$ in the real embedding, clearing by $81^K$ gives integers of absolute value at most $(M+1)10^n81^K$ for numerator and denominator. This bounds the height of $U(1)/V(1)$ in lowest terms; reduction can only decrease it.

Divide (3) by the logarithm base two of this height bound and take even $n\to\infty$. The lower-order terms vanish since m,d are fixed. The limiting ratio is
$$
 \log_{81}(64)\,\frac{(39/2)^2-9}{(37/2)^2+9}
 =\log_{81}(64)\frac{297}{281}>1.
$$
The strict inequality follows from $64^{93}>81^{88}$ and $88\cdot297-93\cdot281=3$. If $\Theta=a/b$ were rational in lowest terms, b would be odd. The reduced approximant $u/v$ also has odd denominator, and (3) makes $av-bu$ nonzero with valuation equal to (3). But $2^{v_2(av-bu)}\le |av-bu|\le (|a|+|b|)\operatorname{height}(u/v)$. The limiting strict excess contradicts that inequality.

Finally any finite positive-increment steering prefix gives a rational affine transformation of the tail value with nonzero multiplier, by directly splitting the defining series at the end of the prefix and updating m. The context itself is a rational affine function with nonzero multiplier as specified in L-9407. Irrationality survives both operations.
