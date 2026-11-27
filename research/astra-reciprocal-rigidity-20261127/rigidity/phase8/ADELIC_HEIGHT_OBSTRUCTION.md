# Finite-place local potentials cannot supply a radial escape certificate

Write $w(n)=1/4$ at even positive integers and $w(n)=9/4$ at odd ones. A strictly positive function satisfying
\[
        u(Tn)\ge w(n)u(n),\qquad u(n)=o(n^2)                            \tag{1}
\]
would exclude every escaping positive orbit. For a finite simple segment $x_0,\ldots,x_t$, T-A3-651, equations (1)–(2), gives $\sum_{i<t,\, x_i\text{ odd}}1/x_i\le200$. Indeed its uniform counting estimate $\#\{x_i\le X:x_i\text{ odd}\}\le 5X^{39/40}$ integrates to $200$ against $X^{-2}\,dX$ on $[1,\infty)$. Writing $A_t$ for the product of the branch slopes, $x_t=x_0 A_t\prod_{i<t,\,x_i\text{ odd}}(1+1/(3x_i))$. Hence (1) yields $u(x_t)/x_t^2\ge e^{-400/3} u(x_0)/x_0^2$ on every such segment, including the initial segments of an escaping path. [Finite-path distortion, T-A3-651](../../../astra-three-routes/pass3/FINITE_RECORDS.md) In particular an inverse supersolution can be tested against its individual edges. The previous [height obstruction](../phase2/DUAL_HEIGHT.md) treats candidates with envelope $O(n^s)$, $s<2$. Here the radial improvement over $n^2$ can grow arbitrarily slowly. We specify the admissible local corrections, which can be unbounded at individual finite places. The result excludes a class of proposed certificates.

Let $S$ be a fixed finite set of primes containing 2, write $D=\prod_{\ell\in S}\ell$, and embed ordinary positive integers diagonally in $Z_S=\prod_{\ell\in S}\mathbb Z_\ell$. In each coordinate $B_{\ell,i}(z)$ denotes its residue class modulo $\ell^i$. Allow finite sums $P(n)$ of the following real-valued terms.

* A bounded function on $Z_S$ whose variation on each product of depth-$r$ residue classes is at most $C(1+r)^{-\sigma}$ for some $\sigma>0$. Every locally constant or Hölder-continuous finite-place observable qualifies.
* For any finite signed measure $\xi$ on $\mathbb Z_\ell$, the finite-precision logarithmic potential $\sum_{i=1}^{N_\ell(n)}\xi(B_{\ell,i}(n))$, with $c\log(2+n)\le N_\ell(n)\le C\log(2+n)$ for all sufficiently large $n$. Constants may vary by term. No condition is imposed on the centers of this measure.
* The full potential $\int v_\ell(n-r)\,d\xi(r)$ for a finite signed measure on algebraic $r\in\mathbb Z_\ell$ outside the positive rational integers. Choose a nonzero integral annihilating polynomial $A_r$ without positive integer roots, for instance the primitive minimal polynomial. Require
\[
       \int\bigl(\deg A_r+\log(2+\textstyle\sum_i|[X^i]A_r|)\bigr)\,d|\xi|(r)<\infty.                \tag{2}
\]
In particular a mixture of negative rational centers suffices if the logarithms of their numerator and denominator heights have finite first moment.

**Obstruction.** Suppose $g:[0,\infty)\to[0,\infty)$ is nondecreasing. If the function
\[
           u(n)=n^2\exp\{-g(\log_2 n)-P(n)-E(n)\},\qquad
           E(n)=O((1+\log n)^{-\sigma_0}),\quad \sigma_0>0,            \tag{3}
\]
satisfies the one-edge inequality of (1) on all sufficiently large ordinary positive integers, then $g$ is bounded. This includes $g$ slower than any prescribed iterated logarithm. The terms of $P$ can have either sign. Formula (3) is a representation hypothesis; the theorem does not infer it for arbitrary positive supersolutions. In particular, unrestricted arithmetic functions of the full input retain information outside these local classes.

## A stationary finite-place law with positive real slope drift

Fix $1/\alpha<p<1$, where $\alpha=\log_2 3$. On the binary coordinate take the law whose *forward shortcut parities* are iid Bernoulli($p$). Each length-$r$ parity word specifies exactly one residue modulo $2^r$. Indeed replacing a representative by that representative plus $2^r$ preserves the first $r$ bits and changes the endpoint by the odd integer $3^{\#\mathrm{odd}}$. Induction gives the compatible bijections and the infinite binary law. Its pushforward under $T$ deletes the first parity; the remaining sequence is independent of the deleted bit. Each binary ball of depth $r$ has mass at most $\max(p,1-p)^r$. [Bernstein and Lagarias, *The 3x+1 Conjugacy Map*](https://doi.org/10.4153/CJM-1996-060-x)

If $3\in S$, give its coordinate, independently, the law of
\[
   Z_3=\sum_{i\ge1}3^{i-1}2^{-(e_1+\cdots+e_i)},\qquad
   \Pr(e_i=a)=p(1-p)^{a-1}\quad(a\ge1),
\]
with independent gaps. Convergence is ternary. Equivalently $Z_3=2^{-e}(1+3Z_3')$ in distribution for an independent copy and gap. Applying the odd shortcut to an independent draw with probability $p$ selects a new initial gap one. Applying the even shortcut with probability $1-p$ adds one to the initial gap. The combined law is the same geometric mixture. To land in a prescribed depth-$r$ ball, the first gap must have prescribed parity modulo 2 if the target is a ternary unit; a nonunit has zero probability for $r\ge1$. The maximum mass of a parity of the geometric gap is $1/(2-p)$. Once that gap is fixed the next draw must occupy one depth-$(r-1)$ ball. Consequently every depth-$r$ ternary ball has mass at most $(2-p)^{-r}$. This argument supplies the requisite small-ball bound also when the stationary ternary law is singular. The series is the geometric Syracuse law appearing in Tao and its biased extensions. [Tao, Forum of Mathematics, Pi (2022)](https://doi.org/10.1017/fmp.2022.8) · [Weaver, Paper 135, equation (1), with prior tilted-law sources](https://rstation.ai/problems/collatz/papers/135)

Give the remaining coordinates independent normalized Haar laws. Both branch maps $x/2$, $(3x+1)/2$ are affine automorphisms there and preserve these laws separately. Define one transformation on $Z_S$ by selecting the branch from the binary coordinate and applying it in every coordinate. The product law $\nu$ just constructed is stationary. The future binary sequence is independent of the consumed bit and all initial odd coordinates. Conditional on that bit and the ternary coordinate, the other odd coordinates remain product Haar after the branch; mixing the ternary coordinate gives the geometric law again. Thus the joint distribution, including independence, is preserved. There exists $b<1$ such that every depth-$r$ ball in any **single** coordinate has marginal mass at most $b^r$. The constants depend on $p,S$.

## Comparison on finite words of ordinary positive integers

Draw $Z\sim\nu$. Let $n=D^k+[Z]_{D^k}$ be the unique representative in $[D^k,2D^k)$ matching all coordinates modulo their $k$th prime powers. Take $j=\lfloor k/2\rfloor$, $y=T^j n$. All $j$ steps are actual ordinary shortcut steps. At 2 they have the first $j$ parities of $Z$, and the endpoint agrees with $T^jZ$ through depth $k-j$. At the other primes equality of the chosen branch preserves the full precision $k$. Also
\[
      n/2^j\le y\le 2^j n,\qquad
      \log(y/n)=\log A_j + d_j,\qquad
      A_j=3^{p_j}2^{-j},\quad
      0\le d_j\le\frac{2^j}{3n},                                     \tag{4}
\]
where $p_j$ is the odd count and the last bound sums $1/(3T^i n)\le2^i/(3n)$.

We claim there exist constants $C,\sigma>0$ for which
\[
                 |\mathbb E P(n)-\mathbb E P(y)|\le C k^{-\sigma}.    \tag{5}
\]
For a bounded local term, evaluate its joint stationary version at $Z,T^j Z$. The expectations there agree. The retained common depth gives the stated approximation at each endpoint.

For a truncated measure term, take an integer $r\asymp k$ with $r\le k-j$ and $r\le N_\ell(n),N_\ell(y)$ uniformly; (4) and the lower precision budget allow this. At depths $i\le r$ the integrals exactly match the corresponding depth terms at the stationary inputs. Their sums have equal expectations. The absolute contribution above $r$ is bounded pointwise by $Ck |\xi|(B_{\ell,r}(n))$ and likewise for $y$, by nestedness and the upper precision budget. The expected mass of either ball is at most $b^r\|\xi\|$ by stationarity and Fubini.

For a full algebraic potential, polynomial division by the monic $X-r_0$ in $\mathbb Z_\ell[X]$ shows $v_\ell(x-r_0)\le v_\ell(A_{r_0}(x))$ for every positive integer $x$. The right side is bounded by
\[
 (\log \ell)^{-1}\bigl(\deg A_{r_0}\log(1+x)+\log\textstyle\sum_i|[X^i]A_{r_0}|\bigr),
\]
because the integer $A_{r_0}(x)$ is nonzero. In particular the potential is finite. Truncate its ball expansion after $r=k-j$ and use the preceding exact equality of expectations at the lower depths. At $x=n,y$ the remainder has absolute value at most the integral of the displayed height bound over the centers sharing its depth-$r$ ball. Each fixed center has probability at most $b^r$ of sharing it. Formula (2) and (4) give $O(k b^r)$. This completes the proof of (5). The tail proof explains the role of the height moment in evaluating potentials at actual integers.

## Radial growth contradicts the averaged edge inequality

The odd count $p_j$ has the binomial law under our finite CRT sample. Since $p\alpha>1$, there exist $c_0,c_1>0$ such that except with probability $O(e^{-c_1k})$ we have $\log_2 A_j\ge c_0 k$. Let $a=\log_2 D$. The positive affine error in (4) then gives $\log_2y\ge(a+c_0)k$, while $\log_2 n<ak+1$ always. Multiplying the $j$ edge inequalities is legitimate even when they are assumed only above a fixed floor, since every departing value is at least $D^k/2^j$. With the sign convention in (3) this yields
\[
 g(\log_2y)-g(\log_2n)
        \le P(n)-P(y)+E(n)-E(y)+2d_j.
\]
Use nonnegativity on the exceptional event, monotonicity, (4), and (5). Enlarging constants gives
\[
     (1-Ce^{-c_1k})g((a+c_0)k)\le g(ak+1)+C k^{-\sigma}              \tag{6}
\]
for all large integers $k$. Choose $k_0$ large and $k_{i+1}=\lfloor(1+c_0/(2a))k_i\rfloor$. Then $a k_{i+1}+1\le(a+c_0)k_i$ and the $k_i$ increase geometrically. Inserting this sequence in (6), the multiplicative errors have finite product and the additive errors are summable. Thus $g(ak_i+1)$ stays bounded, and monotonicity bounds $g$ everywhere. This proves the obstruction.

The binary and ternary laws here select actual finite lifting populations at every scale. They are not assumed to describe the infinite parity sequence of any one positive integer. Every claimed edge inequality is imposed only on ordinary positive inputs. The contradiction is with its proposed finite-place and radial representation.

## Violation sets must have full upper counting exponent

Let $B=\{n:u(Tn)<w(n)u(n)\}$ for a function of the form (3) with unbounded $g$. Then
\[
                  \limsup_{Y\to\infty}\frac{\log(1+\#(B\cap[1,Y]))}{\log Y}=1.      \tag{7}
\]
Thus an exception set of size $O(Y^{1-\varepsilon})$ cannot suffice, for any fixed $\varepsilon>0$. The conclusion leaves its natural density undetermined.

Suppose that counting bound holds and choose $0<\theta<\varepsilon/4$ (decrease $\varepsilon$ below 1 if necessary). Set $j=\lfloor\theta k\rfloor$, $r=\lfloor\sqrt k\rfloor$, and $D_o=\prod_{\ell\in S,\ell>2}\ell$. Sample $Z$ from the stationary law above. For the ordinary binary residue of length $k$, take its first $j+r$ **parity** bits from $Z$ and its remaining $k-j-r$ parity bits from independent fair coins. The compatible word bijection gives the binary residue uniquely. Use the odd coordinates of $Z$ to precision $r$. With $D_k=2^kD_o^r$, take the unique positive representative $D_k\le n<2D_k$ of all these residues. This represents one genuine integer and does not require any independence of future ordinary iterates past the supplied bits.

At $i\le j$, the endpoint $T^i n$ matches $T^iZ$ at all primes to depth $r$. At the binary place its first $k-i$ subsequent parity bits include **all** $k-j-r$ fair coins. For a fixed positive integer $v$, the event $T^i n=v$ therefore prescribes the full fair tail, whatever the biased prefix or odd residues. In particular
\[
 \Pr(T^i n=v)\le 2^{-k+j+r},\qquad
 T^i n\le 2^{(1+\theta)k+O(\sqrt k)} .
\]
A union bound over $i<j$ and possible members of $B$ up to this height gives an exponentially small chance of hitting a violating vertex:
\[
 O\!\left(k\,2^{[-1+\theta+(1-\varepsilon)(1+\theta)]k+O(\sqrt k)}\right)=O(e^{-c k}).
\]
The tested path thus obeys all its edge inequalities with this loss. Its genuine real growth still satisfies $\log_2 y\ge(1+c_0)k$ except with exponentially small probability, since its first $j$ bits retain the positive-drift iid bias. Initially $\log_2 n\le k+O(\sqrt k)$.

Estimate (5) remains true with a possibly smaller positive power. Use the shared depth $r$ at both endpoints, local variation $O(r^{-\sigma})$, and the potential tail bound $O(k b^r)$. The lower logarithmic precision budgets exceed $r$ since every endpoint lies between $2^{(1-\theta)k}$ and $2^{(1+\theta)k+O(\sqrt k)}$. The three classes also give the pointwise bound $|P(n)|+|P(y)|=O(k)$: for the full potential use (2) and polynomial evaluation, and for a truncated term use the stated upper precision. Removing the exponentially rare failed paths thus changes the *unrestricted* expected local difference by at most $O(ke^{-c k})$. This avoids assuming conditional stationarity after discarding paths.

Take expectations only over the paths satisfying all edge inequalities and use nonnegativity of $g$ on those without the typical increase. For constants $C,c,\sigma'>0$ we obtain
\[
 (1-Ce^{-ck})g((1+c_0)k)\le g(k+C\sqrt k)+C k^{-\sigma'} .
\]
As before take $k_{i+1}=\lfloor(1+c_0/2)k_i\rfloor$, so that $k_{i+1}+C\sqrt{k_{i+1}}\le(1+c_0)k_i$ eventually. The summable errors force $g$ bounded, proving (7).

For completeness, if the representation (3) has bounded $g$, it cannot meet the separate requirement $u(n)=o(n^2)$ either. In the original CRT samples, $\mathbb E|P(n)|=O(1)$: use the single-coordinate small-ball bounds to sum the expected absolute low-depth terms by a geometric series, then use the tail estimates from (5). There is at least one representative in every such sample with bounded $|P(n)|$. These ordinary representatives tend to infinity and keep $u(n)/n^2$ bounded below. The argument applies also to signed corrections.

The high-density fair tail in (7) serves only to avoid a prescribed power-sparse set. The positive drift is imposed on the shorter initial block. Biasing every digit would unnecessarily reduce the dimension of the possible integer sources.
