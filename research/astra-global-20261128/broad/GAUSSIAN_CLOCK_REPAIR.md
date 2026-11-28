# An exact denominator obstruction to Gaussian repair of quadratic clock forms

The unperturbed construction in `QUADRATIC_CLOCK_PADE.md` cancels a block of consecutive event rows by a polynomial. A bounded error in a cumulative odd clock can break that polynomial cancellation even if the error occurs at only one index. The following finite calculation identifies the entire new denominator. It concerns this particular system of exact cancellation equations.

Put $C(j)=j(j-1)/2$, $\beta=2/3$, and consider $u_j=bj+hC(j)+e_j$, with $h>0$ even. The event term is $a_j z^j\beta^{hC(j)}$ for $a_j=\beta^{e_j}$ and $z=2\beta^b$. Let $X=\beta^{h/2}$. For fixed $m\ge0,n\ge2$, the weighted sum of shifted tails with column coefficients
$$
 w_k R_k=z^{-k}\beta^{-h(m+n-1/2)k}R_k\qquad(0\le k\le n)
$$
has its first $n$ tail-event rows zero exactly when
$$
 \sum_{k=0}^n a_{m+n+k-i}X^{(k-i)^2}R_k=0\quad(0\le i<n). \tag{1}
$$
Indeed the row using event $m+n-i+k$ has common factor $z^{m+n-i}\beta^{hC(m+n)-hi(m+n-1/2)}$. Normalize $R_n=1$. In the flat case $a_j=1$, the polynomial $P(Y)=\sum_{k=0}^n X^{k^2}R_kY^k$ vanishes at the $n$ distinct nodes $Y_i=X^{-2i}$, and has top coefficient $X^{n^2}$. Its subleading coefficient consequently gives
$$
 R_{n-1}^{\rm flat}=-X\sum_{j=0}^{n-1}X^{2j}. \tag{2}
$$

**One bounded defect.** Now set $e_{m+2n}=1$ and all other $e_j=0$. This cumulative perturbation changes just two adjacent gap lengths by opposite units. The coefficient matrix $G_{ik}=X^{(i-k)^2}$ for $0\le i,k<n$ is unchanged. Only the fixed right column in row zero changes, by $(\beta-1)X^{n^2}$. The precise new coefficient is
$$
 R_{n-1}=R_{n-1}^{\rm flat}-(\beta-1)(-1)^{n-1}
 \frac{X^{n^2+n-1}}{\prod_{d=1}^{n-1}(1-X^{2d})}. \tag{3}
$$
To see this, solve $Gv=(1,0,\ldots,0)^\mathsf{T}$. The degree-$n-1$ polynomial $\sum_k X^{k^2}v_kY^k$ equals one at $Y_0=1$ and zero at each other $Y_i$. Its leading coefficient is $\prod_{d=1}^{n-1}(1-X^{-2d})^{-1}$ by Lagrange interpolation. Divide by $X^{(n-1)^2}$ to obtain $(G^{-1})_{n-1,0}=(-1)^{n-1}X^{n-1}/\prod_{d<n}(1-X^{2d})$, using $1\le d<n$ in the denominator.

At $X=(2/3)^{h/2}$ the exact part of the reduced denominator of $R_{n-1}$ outside 2 and 3 is
$$
 P_{n,h}=\prod_{d=1}^{n-1}(3^{hd}-2^{hd}). \tag{4}
$$
Every factor is coprime to six, the numerator of the correction is a signed product of powers of 2 and 3, and (2) is integral outside six. Thus addition of the flat coefficient cannot cancel even one prime factor of $P_{n,h}$. The column factors $w_k$ are themselves units outside six. In every integral normalization of all the column coefficients the scale at the right boundary therefore contains this entire factor outside six. Its binary size is
$$
 \log_2 P_{n,h}=(\log_2 3)h\,n(n-1)/2+O_h(1),
$$
by convergence of $\sum_{d\ge1}|\log(1-(2/3)^{hd})|$. With $n=2s$ this added cost exceeds the old quadratic margin $(21-13\log_2 3)hs^2/2$ in the direct unperturbed height estimate. Equation (4) does not exclude a smaller final form after additional cancellation among the columns or a different auxiliary construction.

The same calculation tests a proposed iterative repair. When $h$ is large, $G$ is close to its diagonal both in the ordinary and dyadic norms, so its inverse has a convergent series in off-diagonal entries. Nevertheless the correction in (3), viewed as a formal series in $X$ with $\beta=2/3$ fixed, has infinitely many nonzero coefficients. The term of every degree $n^2+n-1+2j$ occurs because $1/(1-X^2)$ is among the factors and the other geometric factors have nonnegative integer coefficients. Truncating that series abandons exact row cancellation; both its residual valuation and the resulting integer height would need a fresh estimate. Fixed curvature, a single defect and large diagonal dominance already exhibit the obstruction. [Zudilin's unperturbed construction, equations (7)–(10)](https://arxiv.org/pdf/math/0506086).
