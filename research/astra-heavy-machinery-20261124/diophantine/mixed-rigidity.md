# All finite source-time translates of the weighted clock are independent

**PROPOSED written theorem.** For each ordinary positive odd source $2n+1$, let $a_j$ be its successive valuations $v_2(3x+1)$, $A_j$ their sum before step $j$, and $u(n,j)=2^{A_j-j}$. Let $K=\overline{\mathbb Q}$. The positive-source series

$$\Phi(t,z)=\sum_{n,j\ge0}u(n,j)t^nz^j$$

satisfies no nonzero homogeneous *linear* partial differential equation with polynomial coefficients in $t,z$, including equations using mixed derivatives. This strengthens the specific holonomicity obstruction in [the two-place packet, §6](proof.md). The result concerns a uniform expression retaining the initial source as a coordinate. The fixed-source eventual-periodicity question is open.

## Translate independence

For every finite set of distinct shift pairs $(h,l)\in\mathbb N^2$, the functions $u(n+h,j+l)$ are linearly independent over $K(n,j)$ modulo identities holding for all sufficiently large $n,j$. Clear all denominators in a proposed relation with polynomial coefficients $p_{h,l}(n,j)$. Choose the largest $l$ that occurs, and among its terms the smallest $h$. Fix an arbitrarily large $j$ and put $J=j+l\ge1$.

Use the odd 2-adic rational center $x_*=(2/3)^J-1$. For $0\le i<J$ the intermediate test points $x_i=(2/3)^{J-i}-1$ are odd in $\mathbb Z_2$, and $3x_i+1=2x_{i+1}$ for $i<J-1$. Thus the first $J-1$ gaps are one, and $x_{J-1}=-1/3$, where the next valuation is infinite. We use this center only to prescribe finite cylinders of positive ordinary integers. It does not constitute a positive orbit.

Write $n_*=(x_*-1)/2-h\in\mathbb Z_2$. For a shifted term $(h',l')$ the centered source is $x_*+2(h'-h)$. Its reduced rational denominator is exactly $3^J$, since its numerator is $2^J$ modulo 3. For an odd 2-adic rational whose reduced denominator is $3^b$ with $b\ge2$, a legal odd step reduces the ternary denominator exponent by exactly one. Indeed the numerator after multiplication by 3 and addition of 1, over the old denominator, is $3(v+3^{b-1})$ with $3\nmid v$. Powers of two from the odd normalization cancel from that numerator and do not change its ternary valuation. Such a point cannot already equal $-1/3$. In particular every translated source has a legal prefix of length $J-1$, even when it is negative in the usual real ordering. If $l'<l$, this covers its entire required prefix. If $l'=l$ and $h'>h$, the source $x_*+2(h'-h)>0$ is real positive and its next odd step is also legal. These are all competing terms.

Each competing finite valuation prefix is locally constant on some 2-adic neighborhood of $n_*$. This follows by induction, since $v_2$ is locally constant off zero and the branch with fixed valuation is rational affine and continuous. Intersecting the finitely many neighborhoods gives a common one. For the selected term, all positive ordinary $n$ sufficiently close to $n_*$ have $J-1$ initial ones. On this cylinder the next undivided numerator is

$$3U^{J-1}(2(n+h)+1)+1=3^J\,2(n-n_*)/2^{J-1}.$$

For every sufficiently large integer $e$, the condition $v_2(n-n_*)=e+J-2$ therefore makes the last gap exactly $e$ and $u(n+h,j+l)=2^{e-1}$. It describes one residue class modulo $2^{e+J-1}$ with infinitely many positive ordinary members. All competing values have fixed integer values $c_{h',l'}$ independently of $e$ on these classes.

For each such $e$, substitution in the proposed relation gives an identity of polynomials in $X$,

$$2^{e-1}p_{h,l}(X,j)+\sum_{(h',l')\ne(h,l)}c_{h',l'}p_{h',l'}(X,j)=0,$$

since the polynomial vanishes on infinitely many integers of the indicated class. Subtracting the identity for $e+1$ gives $p_{h,l}(X,j)=0$. This holds for arbitrarily large $j$, forcing $p_{h,l}=0$ as a bivariate polynomial, a contradiction. The source classes may vary with $j,e$. All values used to refute a *uniform* relation are values at actual ordinary positive integers.

## Differential consequence

Write any polynomial-coefficient partial differential operator as a finite sum of $t^b z^d\partial_t^a\partial_z^c$ with constant multipliers and like terms already combined. Extracting $[t^n z^j]$ at sufficiently large indices gives shifts $(h,l)=(a-b,c-d)$ and multipliers

$$(n+h)_{\underline a}(j+l)_{\underline c},$$

where the subscripts are falling factorials. For any fixed shift pair, the products for different $(a,c)$ are linearly independent as polynomials in $n,j$, by the univariate falling-factorial basis in each variable. At least one shift coefficient for a nonzero differential operator therefore remains nonzero. Translating both indices by fixed integers makes all shifts nonnegative without changing eventual validity. The proven independence excludes the resulting relation. The same conclusion holds for rational-function operator coefficients after clearing denominators. In particular there is no source-uniform polynomial-coefficient time recurrence involving any finite family of nearby integral sources and bounded time shifts.

This test allows mixed derivatives and arbitrary algebraic degree in both coefficients. It does not rule out a different equation for each fixed positive source, a nonlinear differential equation, or a transformed observable using different coordinates. Every eventually periodic individual orbit still has a rational time series, as proved in the two-place packet.
