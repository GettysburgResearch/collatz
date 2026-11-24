# Defects escape every translated short interval

**TB1. Proposed written theorem.** Fix a real number $0<\epsilon<1$. Take the least odd period $p$ of a nontrivial positive integer cycle, with total binary clock $A$, and put $g=\gcd(A,p)$, $b=p/g$, $a=A/g$. Rotate the odd cycle at a minimum of $b d_i-ai$, where $d_i$ is its cumulative binary clock. Write

$$
b d_i-ai=r_i+b k_i,\qquad 0\le r_i<b,\quad k_i\ge0 .
$$

For all sufficiently large $p$, the support $\{r_i:k_i>0\}$ is contained in no cyclic interval of $\lfloor b^{1-\epsilon}\rfloor+1$ consecutive residues. The center of the interval may depend arbitrarily on the cycle. Visits with the same residue may have different heights. The cutoff is effective given an effective finite irrationality measure for $\log_2 3$.

## Principal factor and the choice of precision

Use CF3 and CF6–7 of the accompanying cycle packet for the factorwise resultant lemma and the principal root. Here are the quantitative inputs. With $D_1=2^a-3^b$, there is a unit $x\bmod D_1$ satisfying $x^b=2$, $x^a=3$. At this root

$$
F_1(x)=0,\qquad F_1(X)=\sum_{0\le i<p}2^{k_i}X^{r_i}.
$$

Indeed $D_1\mid 2^A-3^p$ divides the ordinary cycle numerator, including after this rotation. The identity $x^{b d_i-ai}=2^{d_i}3^{-i}$ gives the evaluation. Put $\alpha=\log_2 3$. Distinct odd states of a least-period cycle and the effective two-logarithm bound give, as in CF7,

$$
a/b=\alpha+O((1+\log b)/b),\quad D_1\ge c\,3^b b^{-\kappa},\quad
g=O(b^{2\kappa+1}).
$$

In particular $b\to\infty$ with $p$. Fix $B$ to be the last continued-fraction denominator of $\alpha$ at most $b^{\epsilon/4}$. The finite irrationality measure supplies $B\ge c_1 b^{\epsilon/(4\kappa)}$ for large $b$. Use the convergent of denominator $B$ and its predecessor. Both pairs $(h,k)$ have coordinates $O(B)$ and satisfy $|h-k\alpha|\le 1/B$. The two corresponding integer binomials, obtained from $x^{h b-k a}=2^h3^{-k}$, have

$$
\deg Q_i=O(b/B+B\log b)=O(b/B),\qquad
\log\lVert Q_i\rVert_1=O(B).
$$

Their exponents are nonzero by $\gcd(a,b)=1$ and $0<k<b$. The determinant of consecutive convergents has absolute value one, so the two binomials have no common complex root by independence of 2 and 3. Applying the CF3 resultant argument irreducible factor by irreducible factor shows that any nonzero integer polynomial $G$ annihilated by $x\bmod D_1$ satisfies

$$
\log D_1\le O(b/B)\log\max(1,\lVert G\rVert_1)+O(B)\deg G.\tag{1}
$$

The alignment $B$ with an actual convergent denominator matters here. Bounding its predecessor relative to an arbitrary cutoff would weaken the simultaneous scales in (1).

## Eliminating the translated center

Suppose the support is contained in $u,u+1,\ldots,u+W\pmod b$, where $0\le u<b$ and $W=\lfloor b^{1-\epsilon}\rfloor$. The residue step is subtraction of $s=a-b\pmod b$. For large $b$ one has $W<\min(s,b-s)$, so this interval and its one-step translate are disjoint. Every positive elevation has next height zero. By the exact gap identity

$$
a_i=1+\mathbf1_{r_i<s}+k_{i+1}-k_i\ge1
$$

its height is one. Each residue is visited $g$ times. For $0\le j\le W$, let $n_j$ be the number of elevated visits to $u+j\pmod b$. Multiplying the baseline geometric sum by $X-1$ gives 1 modulo $X^b-2$. In that ring,

$$
2(X-1)F_1(X)=2g+X^uH(X),\qquad
H(X)=(X-1)\sum_{j=0}^{W}2^{1-\lfloor(u+j)/b\rfloor} n_jX^j.
$$

The common factor 2 clears the single possible wrap. Thus $H(1)=0$, $\deg H\le W+1$ when $H\ne0$, and $\|H\|_1\le4p$. If $H=0$, then $D_1\mid2g$ contradicts the displayed growth bounds for large $b$. Otherwise $x^u H(x)=-2g\pmod{D_1}$.

Set $T=\lceil B^{2/3}\rceil$. Place the $(T+1)^2$ points $(m u+j a)/b\pmod1$, $0\le m,j\le T$, on the unit circle. Two consecutive points in increasing cyclic order are within $1/(T+1)^2$, with coincident points allowed. Their differences give integers $m,j,t,e$ with

$$
e=m u+j a-t b,\quad |m|,|j|\le T,\quad |e|\le b/(T+1)^2,\quad (m,j)\ne(0,0).
$$

In fact $m\ne0$. If $m=0$, then $0<|j|\le T<B$. The best-approximation property of the convergent just *before* denominator $B$ gives $\lVert j\alpha\rVert\ge1/(2B)$. Indeed the predecessor error is strictly greater than $1/(B+B_{\rm prev})$. The bound on $a/b-\alpha$ gives $|j|\,|a/b-\alpha|=O(T\log b/b)=o(1/B)$. It follows that $\lVert ja/b\rVert\ge 1/(3B)$ for large $b$, contradicting $1/(T+1)^2=o(1/B)$. Negating all four integers if needed ensures $1\le m\le T$. Also $|t|=O(T)$ because $0\le u<b$ and $1<a/b<2$.

Use $x^{mu}=2^t3^{-j}x^e$. Raising the translated relation to the power $m$ and clearing numerical denominators and negative powers of $X$ yields the following polynomial. Write $v_+=\max(v,0)$.

$$
G(X)=2^{t_+}3^{(-j)_+}X^{e_+}H(X)^m
-(-2g)^m 2^{(-t)_+}3^{j_+}X^{(-e)_+}.
$$

It vanishes at $x\bmod D_1$, where 2, 3 and $x$ are units. Its value at 1 is nonzero since $m\ge1$ and $H(1)=0$. In particular, there is no zero-resultant assumption on the translated relation. We have

$$
\deg G\le T(W+1)+b/(T+1)^2=o(b/B),\qquad
\log\lVert G\rVert_1=O(T\log b)=o(B).
$$

For the degree, $BTW/b=O(b^{-\epsilon}B^{5/3})=o(1)$ and $B/(T+1)^2=o(1)$. For the coefficient norm use $p=gb=b^{O(1)}$ and the positive-power lower bound on $B$. Substitution in (1) gives $\log D_1=o(b)$, contradicting $D_1\ge c\,3^b b^{-\kappa}$.

## Polynomially many intervals centered on multiples of one residue

**TB2. Proposed written theorem.** Fix an effective exponent $\kappa\ge1$ as above and put $\delta=\epsilon/(100\kappa)$. For every sufficiently large least period and every $0\le u<b$, the support cannot be contained in

$$
\bigcup_{l=0}^{h}\{lu,lu+1,\ldots,lu+W\}\pmod b,
\qquad 0\le h\le b^\delta,\qquad W=\lfloor b^{1-\epsilon}\rfloor .
$$

The intervals may overlap or wrap, and their internal support is arbitrary. In particular, $u$ need not be small or invertible modulo $b$.

To bound the heights, let $\|z\|$ denote distance to the nearest integer. The irrationality measure implies $\|v\alpha\|\ge c_2v^{-\kappa}$ for integers $v\ge1$, after adjusting the constant for the finitely many small $v$. Hence uniformly for $1\le v\le h+1$,

$$
\|v s/b\|=\|v a/b\|\ge c_2(h+1)^{-\kappa}-O((h+1)\log b/b)>W/b .
$$

Here $(h+1)^{-\kappa}\gg b^{-\epsilon/100}$ and $(h+1)^{\kappa+1}\log b=o(b)$. Consequently no two of $h+2$ consecutive visits can lie in the same interval. With only $h+1$ intervals, at least one of these visits has zero height. The gap identity makes a height drop by at most one per step, so $k_i\le h+1$ at every visit.

Assign each elevated visit to one interval containing it. If assigned to $l$, write its residue as $lu+j\pmod b$ for $0\le j\le W$. Put $C=2^{h+1}$ and $Y=x^u$. The evaluation of $C(X-1)F_1$ can be written as $P(x,Y)=0\bmod D_1$, where

$$
P(X,Y)=Cg+(X-1)\sum_{l=0}^{h} E_l(X)Y^l.
$$

Each visit contributes $2^{h+1-\lfloor(lu+j)/b\rfloor}(2^{k_i}-1)X^j$ to $E_l$. The power of two is integral since $lu+j<(h+1)b$. We have $\deg_X P\le W+1$, $\deg_Y P\le h$, $P(1,Y)=Cg$, and $\log\|P\|_1=O(h+\log b)$ for the sum of absolute values of its bivariate coefficients. Indeed there are at most $p$ visits, each giving a coefficient of size at most $2^{2h+2}$ before taking the difference $X-1$.

Use the integers $m,j,t,e$ from TB1, which depend on $u,a,b$ and not on the support. The polynomial

$$
Q(X,Y)=2^{(-t)_+}3^{j_+}X^{(-e)_+}Y^m-
2^{t_+}3^{(-j)_+}X^{e_+}
$$

vanishes at $(x,x^u)\bmod D_1$. It has $\deg_X Q=|e|$, $\deg_Y Q=m$, and $\log\|Q\|_1=O(T)$. Let $S(X)=\operatorname{Res}_Y(P,Q)\in\mathbb Z[X]$, with $d=\deg_Y P\le h$. The integer-polynomial Sylvester identity gives $S(x)=0\bmod D_1$. At $X=1$ the leading $Y$ coefficient of $Q$ is nonzero and $P(1,Y)=Cg$. The root-product formula using the roots of $Q(1,Y)$ therefore gives $|S(1)|=|\operatorname{lc}_Y Q(1,Y)|^d(Cg)^m>0$. This formula retains the original $d$, including when specialization lowers the degree of $P$.

Each term in the Sylvester determinant uses $m$ coefficients of $P$ and $d$ of $Q$. Thus

$$
\begin{aligned}
\deg S&\le m(W+1)+h|e|,\\
\log\|S\|_1&\le \log((m+d)!)+m\log\|P\|_1+h\log\|Q\|_1 .
\end{aligned}
$$

For large $b$, $h\le B^{1/12}$ by the lower bound on $B$. Hence $hB/(T+1)^2=o(1)$ and $hT=o(B)$. The other terms obey $BT(W+1)/b=o(1)$, $T\log b=o(B)$, and $(T+h)\log(T+h)=o(B)$. We conclude $\deg S=o(b/B)$ and $\log\|S\|_1=o(B)$ uniformly for the allowed $u,h$. Equation (1) again contradicts the exponential lower bound on $D_1$.

## Near-linear widths

**TB3. Proposed corollary.** Fix $C>\kappa$ and $K>0$. The principal root of a sufficiently large least period cannot annihilate a nonzero integer polynomial of degree at most $b/(\log b)^C$ and coefficient norm at most $b^K$. For the same $C$ there is an effective $\delta>0$ such that TB2 holds with $W=\lfloor b/(\log b)^C\rfloor$ and every integer $0\le h\le(\log b)^\delta$, uniformly over all strides $u$. This includes a single arbitrarily translated interval and every fixed number of intervals on the specified grid.

For the polynomial assertion, choose $\kappa<L<C$ and take $B$ to be the last convergent denominator at most $(\log b)^L$. Then $c_1(\log b)^{L/\kappa}\le B\le(\log b)^L$. The same two binomials give (1), since $B^2\log b=o(b)$. For the stated norm and degree, its upper bound divided by $b$ is $O_K((\log b)/B+B/(\log b)^C)=o(1)$.

For the translated intervals, put $Z=\log b$. Fix $0<\mu<\min(L/\kappa-1,C-L,1)$, let $\nu=\mu/2$, and choose $0<\delta<\min(\nu,C/\kappa,1)$. In the circle argument use the rectangle
$$
0\le m\le M=\lfloor Z^\mu\rfloor,\qquad 0\le j\le J=\lfloor B/Z^\nu\rfloor .
$$
Two of its $(M+1)(J+1)$ points give a difference with $|e|\le b/((M+1)(J+1))$. Because $MJ/B\to\infty$, this is $o(b/B)$. Its $m$ is nonzero: a nonzero $|j|\le J<B$ gives $\|j\alpha\|\ge1/(2B)$, and $BJ\log b/b=o(1)$ controls the perturbation by $a/b-\alpha$. Choose the sign so $1\le m\le M$. Then $|t|=O(M+J)=O(J)$, so $\log\|Q\|_1=O(J)$.

For $h\le Z^\delta$ the separation of the first $h+2$ visits used in TB2 still holds. Indeed $(h+1)^{-\kappa}\gg Z^{-\delta\kappa}\gg W/b$ since $\delta\kappa<C$, and $(h+1)^{\kappa+1}\log b=o(b)$. Consequently $k_i\le h+1$ and $\log\|P\|_1=O(h+\log b)=O(Z)$. The same nonzero resultant obeys
$$
\frac{B\deg S}{b}\le \frac{BM(W+1)}b+O\left(\frac{hB}{MJ}\right)=o(1).
$$
The two terms are $O(Z^{L+\mu-C})+o(1)$ and $O(Z^{\delta-\mu+\nu})$, respectively. For its norm, the factorial term is $O((M+h)\log(M+h+2))=o(B)$, the $P$ term is $O(MZ)=o(B)$ because $1+\mu<L/\kappa$, and the $Q$ term is $O(hJ)=O(BZ^{\delta-\nu})=o(B)$. Substitution in (1) again contradicts the exponential lower bound on $D_1$.

## Scope

CF7 tests a support contained near residue zero. TB1 permits one arbitrarily translated interval. TB2 permits a growing number of widely separated intervals when their centers are specified multiples of a common residue. Neither argument provides such a cover for every normalized defect profile. The analytic input comes from CF6–7 and the classical best-approximation property of continued fractions. Both results are written mathematics. The unrestricted positive cycle and escape questions remain open.

