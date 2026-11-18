# A transcendental combination for every periodic word and its reverse subsequences

**PROPOSED.** For every positive periodic stack word, every initial height, and every period $r$, there are eight explicit further native periodic stack values such that a rational linear combination of the original value and these eight values is transcendental over $\mathbb Q$. The eight companion periods divide $r/\gcd(r,8)$. All coefficients in the combination are positive. At least one of the nine values is transcendental. This alternative does not require reflection symmetry or identify the transcendental member.

Extend $d_j,m_j,E_j$ to all integer indices by their defining recurrences. Thus $E_j-E_{j-1}=9m_j+1$, $m_j-m_{j-1}=d_j>0$, and $E_0=0$. There exist rational $a>0,b$ and a rational periodic sequence $u_j$ of period $r$ with $E_j=aj^2/2+bj+u_j$. In particular both tails tend quadratically to positive infinity.

The bilateral sum $H=\sum_{j\in\mathbb Z}T^{E_j}$, where $T=64/81$, is transcendental in $\mathbb Q_2$. To see this write $b/a=v/L$ with integers $v$ and $L>0$, giving
$$
E_j=\frac{a}{2L^2}(Lj+v)^2+u_j-\frac{b^2}{2a}.
$$
Set $q_0=T^{a/(2L^2)}$ and assign weight $T^{u_j-b^2/(2a)}$ to $n=Lj+v$, with weight zero outside this progression. Define all rational powers from the same positive real algebraic root of $T$ of sufficiently divisible order, then fix one embedding into $\mathbb C_2$. The weights are algebraic and periodic in $n$ of period $Lr$. Symmetrizing them by $c(n)=(w(n)+w(-n))/2$ leaves the sum unchanged and gives a nonzero sequence: the weights on the progression are positive in the chosen real embedding. Since $0<|q_0|_2<1$, the [unary theta consequence of Nesterenko's theorem](PROOF.md) applies directly to $H=\sum_n c(n)q_0^{n^2}$.

To express $H$ by native values, retain the original $j\ge0$ half. In the negative half take the eight sequences $-1-i-8l$ with $0\le i<8$, $l\ge0$. For each choose an integer $K_i\ge0$ large enough that for $J=-1-i-8K_i$ one has $E_J-E_{J+8}\ge1$. Define
$$
E'_l=E_{J-8l}-E_J,\qquad
m'_l=(E_{J-8l}-E_{J-8l+8}-1)/9\quad(l\ge0).
$$
Since $E_j\equiv j\pmod9$, every $m'_l$ is an integer, and $m'_0\ge0$. The backward eight-step differences increase strictly with $l$ by strict convexity of $E$. Therefore $d'_l=m'_l-m'_{l-1}$ is a positive integer. One has
$$
E'_0=0,\qquad E'_l-E'_{l-1}=9m'_l+1\quad(l\ge1).
$$
Further, $9d'_l$ is the second difference of $E$ with stride eight. Its value depends only on $J-8l\bmod r$, by the quadratic-plus-periodic formula. The increments therefore have period dividing $r/\gcd(r,8)$.

The omitted negative terms form a rational constant $C$. The exact identity
$$
H=C+\Theta+\sum_{i=0}^7 T^{E_{-1-i-8K_i}}\Theta'_i
$$
proves transcendence of the indicated rational linear combination. Each $K_i$ can be found by testing successive integers, since the required difference tends to infinity. No assumption that the negative indices of the original stack have physical meaning enters the construction; all eight resulting directives start at nonnegative heights.
