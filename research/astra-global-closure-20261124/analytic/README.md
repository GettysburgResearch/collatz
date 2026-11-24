# Physical gap series and reducible binary substitutions

**PROPOSED written results.** This packet gives an arithmetic test for each positive odd orbit and extends the substitution exclusion of PR #190 to the reducible, nonuniform cases for genuine growing binary fixed words. It leaves the unrestricted ordinary-orbit problem open. No assertion of priority across the literature is intended.

## A Pólya-series test for every ordinary odd source

Take one positive odd integer $q_0$. Use $q_{j+1}=(3q_j+1)/2^{g_j}$ with $g_j=v_2(3q_j+1)$, and write $A_n=\sum_{j<n}g_j$. Define the formal series over the rationals
$$
 F_q(z)=\sum_{n\ge0}2^{A_n}z^n .
$$

**GS1.** The following conditions are equivalent for this source.

1. Its odd orbit is eventually periodic.
2. Its gap word is eventually periodic.
3. $F_q$ is rational over $\mathbb Q(z)$.
4. $F_q$ satisfies a nonzero linear differential equation over $\mathbb Q(z)$, also called D-finiteness.

In particular an algebraic series, or a univariate diagonal of a multivariate rational power series over the rationals, suffices for eventual periodicity.

**Proof.** The physical inverse equations telescope to
$$
 q_j=\frac{2^{A_{j+n}-A_j}}{3^n}q_{j+n}
      -\sum_{t=0}^{n-1}\frac{2^{A_{j+t}-A_j}}{3^{t+1}}.
$$
In the 2-adic norm the first term tends to zero, since the endpoints are integers and $A_{j+n}-A_j\ge n$. The infinite tail of gaps determines $q_j$ uniquely, so (1) and (2) are equivalent. A periodic gap tail gives $A_{n+p}=A_n+d$ for some $p,d>0$ at every late $n$, so the series is a polynomial plus a rational tail of denominator $1-2^dz^p$. Rational series are D-finite.

For (4) to (2), apply the following slightly more general observation. If $u\in\mathbb Q_{>0}\setminus\{1\}$ and $C_i$ are nondecreasing nonnegative integers, then
$$
 \sum_{i\ge0} u^{C_i}z^i\text{ is D-finite}
 \quad\Longleftrightarrow\quad C_{i+1}-C_i\text{ is eventually periodic}.
$$
The coefficients are nonzero in the finitely generated subgroup $G=\langle u\rangle$ of $\mathbb Q^\times$. Bell–Smertnig, Theorem 1.3(a,d), gives a finite disjoint decomposition of their support into singletons and arithmetic progressions, geometric on each progression with ratio in $G$. Pass to a common period $p$ and discard a finite prefix. Injectivity of $e\mapsto u^e$ gives $C_{N+kp+r}=c_r+k s_r$ for $0\le r<p$. The slopes are nonnegative by monotonicity. For every $k$,
$$
 c_0+k s_0\le c_r+k s_r\le c_0+(k+1)s_0 .
$$
Therefore $s_r=s_0$ for every residue. Now $C_{i+p}=C_i+s_0$ for late $i$; consecutive differences are $p$-periodic. The reverse direction follows by the same geometric sum as above. Apply this to $u=2,C_i=A_i$. The diagonal implication uses the D-finiteness of diagonals in characteristic zero. [Bell and Smertnig, *Canadian Journal of Mathematics* 75 (2023), Theorem 1.3 and Lemma 7.1](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/dfinite-multivariate-series-with-arithmetic-restrictions-on-their-coefficients/5FD05E0857CEEA88298C5C8057C2A095)

Related work asks for a polynomial-coefficient recurrence on the *orbit states*, including at fixed odd strides. GS1 instead places that hypothesis on the cumulative dyadic factors $2^{A_n}$, a sequence lying in a single cyclic multiplicative group. Neither condition is furnished for arbitrary positive sources. [*Holonomic rigidity and finite recurrence bounds for Collatz trajectories*, rStation Paper 106](https://rstation.ai/problems/collatz/papers/106)

**What can be proved without a structural model.** At the single point $z=1/3$, the infinite telescope gives $F_q(1/3)=-3q_0$ in $\mathbb Q_2$ for *every* ordinary source. Its shifted identities supply that same telescope at its successive tails. Neither these evaluations nor known estimates for Dirichlet characters give a differential equation for the whole series. A proof of D-finiteness for every physical source would settle eventual periodicity by GS1, and would still require exclusion of nontrivial positive cycles for full Collatz. GS1 alone is an exact reformulation in that lane. GS2 below uses the coefficient result in a restricted architecture where there actually is a functional equation.

There is a second check on the same fixed source. If its orbit is injective, the project's orbitwise reciprocal bound gives $\sum_j1/q_j<\infty$. In the real norm, multiplication of the physical step equations gives $2^{A_n}q_n/3^n=q_0\prod_{j<n}(1+1/(3q_j))$. Substituting in the finite telescope and passing to the limit gives
$$
 F_q(1/3)_{\mathbb R}=3q_0\left[\prod_{j\ge0}\left(1+\frac{1}{3q_j}\right)-1\right]>0.
$$
Thus under that hypothesis the same rational partial sums converge to a positive real and the negative integer $-3q_0$ in the 2-adic norm. Identifying the two limits would invalidate the argument. [Repository proof of reciprocal summability on injective orbits](../../integrated/orbitwise-boundaries/README.md)

**Counterexample to an unrestricted specialization argument.** Take $J(z)=\sum_{n\ge0}2^{n^2}z^n$. The observation above makes $J$ non-D-finite because its exponent differences $2n+1$ are unbounded. Yet $1+(1-3z)J(z)$ converges at $1/3$ in $\mathbb Q_2$ with value $1$ and is also non-D-finite, since D-finite series are closed under addition and multiplication by rational functions regular at zero. This example tests only the general inference from one specialization; the coefficients of the modified series need not be ordinary Collatz clock powers.

## Reducible substitution exclusion

**GS2.** Let $s=\lim_{n\to\infty}\sigma^n(e)$ be a non-eventually-periodic word over two letters, for a **nonerasing** substitution prolongable on $e$ with unbounded iterated length. Attach rational affine inverse maps $f_i(t)=u_i+x_i t$, where $x_i>0$, $v_2(x_i)>0$, and their rational fixed points are distinct. For a reducible incidence matrix, the unique 2-adic completion of $s$ is transcendental over $\mathbb Q$.

Thus GS2 and the proposed primitive case MPS-5 of PR #190 together cover every nonperiodic **pure binary morphic word generated from a growing prolongable letter** in this two-block physical setting. An irreducible, imprimitive nonnegative $2\times2$ matrix has zero diagonal. Each letter then maps to a word in the opposite letter, preventing prolongability. A coding from a larger alphabet and an unrestricted ordinary Collatz gap schedule lie outside this theorem. An identity substitution fixes arbitrary words but does not generate one from a growing letter.

**Direct shortcut-map corollary.** Take $f_0(t)=2t$ for an even source and $f_1(t)=(2t-1)/3$ for an odd source. Their slopes have valuation one and their fixed points are $0$ and $-1$. Thus the combined result applies to the ordinary shortcut parity sequence itself, with no recoding into return blocks. Every positive source whose parity sequence is generated by a growing nonerasing binary substitution must be eventually periodic. This implication still allows an unknown nontrivial positive cycle.

[Pinned PR #190, MPS-5 and MPS-6, ba58227c5a047ff3859a148a5fdaac4fd1451e4c](https://github.com/GettysburgResearch/collatz/blob/ba58227c5a047ff3859a148a5fdaac4fd1451e4c/research/mahler-physical-scripts-20261124/PRIMITIVE_MORPHISMS.md)

### The fixed-word identity

Relabel the generating letter as zero. If its images never produce a one, the word is constant. Reducibility now forces
$$
 \sigma(0)=w,\qquad \sigma(1)=1^d,\qquad
 |w|_0=a,\quad |w|_1=b,\quad b,d\ge1.
$$
The word $w$ starts in zero. If $a=1$, the generated word is $01^\infty$, so $a\ge2$. Both letters occur infinitely often. Indeed the number of zeros in the prefixes $\sigma^n(0)$ is $a^n$, and every zero produces at least one one at the next level.

Let $B_i$ be the number of ones preceding the zero of zero-based index $i$ in $s$. Write
$$
 H(X,Y)=\sum_{i\ge0}X^iY^{B_i}.
$$
The formal coefficients in $X$ are polynomials in $Y$. If the differences $B_{i+1}-B_i$ were eventually periodic, then concatenating the corresponding blocks of one zero followed by that many ones would give an eventually periodic $s$. The observation in GS1 proves $H(X,t)$ transcendental over $\mathbb Q(X)$ for every fixed rational $t>0, t\ne1$. It also implies $H(X,Y)$ is transcendental over $\mathbb Q(X,Y)$: in a hypothetical polynomial relation divide by the highest power of $Y-2$ common to all coefficients in $X,Z$, then specialize $Y=2$ coefficientwise in $X$. This would give a nonzero polynomial relation for $H(X,2)$.

Let $P(X,Y)$ sum the prefix monomials at zero positions in $w$. Grouping $s=\sigma(s)$ into images, and using that the other image contains no zeros, gives
$$
 H(X,Y)=P(X,Y)H(X^aY^b,Y^d).
$$
The coefficient $P(x,y)$ is positive on positive rational inputs. Let $G_1$ denote the analogous sum of prefix monomials at one positions. Telescoping the prefix products yields $(1-x)H(x,y)+(1-y)G_1(x,y)=1$ at physically allowed rational multipliers $x=x_0,y=x_1$. The physical completion is $u_0 H(x,y)+u_1G_1(x,y)$; the coefficient of $H$ after eliminating $G_1$ is nonzero by the distinct-fixed-point assumption. All these evaluations converge in $\mathbb Q_2$. It therefore suffices to prove $H(x,y)$ transcendental.

### Heights at the moving rational points

Set $x_0=x,y_0=y$, $x_{n+1}=x_n^a y_n^b,y_{n+1}=y_n^d$. Both coordinates have positive 2-adic valuation. If $U_0=H(x,y)$ were algebraic, $U_n=H(x_n,y_n)$ would lie in the fixed number field $K=\mathbb Q(U_0)\subset\mathbb Q_2$, because $U_{n+1}=U_n/P(x_n,y_n)$ with positive rational divisor. Write $V_n=v_2(x_n)$, $W_n=v_2(y_n)=d^n v_2(y)$. All implied height constants below may depend on the source and substitution. For every $n$,
$$
 V_n=a^n v_2(x)+b v_2(y)\sum_{j<n}a^{n-1-j}d^j,\qquad
 h(x_n)=O(V_n),\quad h(y_n)=O(W_n).
$$
The height bounds follow by applying subadditivity to the same nonnegative powers of $x,y$. Since $a\ge2,b>0$, we have $V_{n+1}\ge 2V_n$, and $W_n=O(V_n)$ follows from $V_n\ge bW_{n-1}$ for $n\ge1$. Thus $h(U_n)=O(V_n)$ by summing $h(P(x_j,y_j))=O(V_j)$. For any nonzero $t\in K$, the height inequality used below is $v_2(t)\log 2\le [K:\mathbb Q]h(t)$.

### Unequal asymptotic scales, including the Jordan case

Suppose $a\ge d\ge2$. Then $W_n=o(V_n)$: for $a>d$ the numerator grows like $d^n$ against $a^n$, and for $a=d$ the sum above is $n a^{n-1}$. A two-variable total-degree approximation would charge the slow scale on every vanishing coefficient. Instead work over the field $\mathbb Q(Y)$. For any integer $m\ge1$, choose nonzero $R(X,Y,Z)$ of degree at most $m$ in each of $X,Z$ such that
$$
 S(X,Y)=R(X,Y,H(X,Y))\quad\text{has }X\text{-order at least }D=(m+1)^2-1.
$$
There are $(m+1)^2$ unknowns over $\mathbb Q(Y)$ and $D$ homogeneous coefficient equations. Clearing all denominators yields $R\in\mathbb Z[X,Y,Z]$. Its degree in $Y$ may depend arbitrarily on $m$. Transcendence of $H$ ensures $S\ne0$.

Write its actual leading term as $X^t C_t(Y)$, $t\ge D$, where $0\ne C_t\in\mathbb Z[Y]$. Every subsequent coefficient in $X$ also belongs to $\mathbb Z[Y]$. Since $W_n\to\infty$, the least-degree nonzero monomial of $C_t$ is eventually dominant at $y_n$, so $v_2(C_t(y_n))=O_R(1+W_n)=o(V_n)$. The tail has valuation at least $(t+1)V_n$. Hence the evaluated auxiliary number is nonzero for large $n$ and has valuation at least $D V_n$. On the other hand,
$$
 h(R(x_n,y_n,U_n))
 \le C m V_n+\deg_Y(R) O(W_n)+O_R(1).
$$
Here $C$ is independent of $m,R$. First fix $m$ and let $n\to\infty$, so even an enormous slow-variable degree disappears after division by $V_n$. The product formula gives $D\log2\le [K:\mathbb Q] Cm$. Letting $m\to\infty$ contradicts this bound.

If $d=1$, use $y_n=y$, the transcendental one-variable formal function $H(X,y)$, and an auxiliary polynomial in $X,Z$ of degree at most $m$ in each. Its nonzero composition has order at least $D$. Coefficients of $H(X,y)$ are 2-adically integral, so the leading term eventually dominates at $x_n\to0$. The preceding height contradiction applies without a slow-variable term. Bell–Smertnig is used here even when the numbers of ones between consecutive zeros are unbounded.

### Comparable scales for $d>a$

Take coprime positive $p,q$ with $p/q=b/(d-a)$. The recurrences give
$$
 V_n=d^n\frac{p}{q}v_2(y)+O(a^n),\qquad W_n=d^n v_2(y),\qquad
 r_n=y_n^p/x_n^q=(y^p/x^q)^{a^n}.
$$
Write $C=v_2(y)/q>0$. If $r_0\ne1$, the $r_n$ are distinct positive rationals of height $O(a^n)$. Choose an integer auxiliary polynomial $R(X,Y,Z)$ of degree at most $m$ in each variable killing all coefficients of total degree $<D=\lfloor m^{3/2}\rfloor$ of $R(X,Y,H)$. There are $D(D+1)/2<(m+1)^3$ conditions. This nonzero auxiliary series has integral coefficients. In its first occupied weighted degree $s=pi+qj$, the homogeneous component factors, at the moving point, as $x_n^{i_0}y_n^{j_0}Q(r_n)$ with $0\ne Q\in\mathbb Z[T]$, choosing the occupied exponent pair with smallest $j$ in the progression $(i,j)=(i_0,j_0)+k(-q,p)$ with $k\ge0$. A polynomial has finitely many roots; the height bound gives $v_2(Q(r_n))\le O_R(a^n+1)$ for sufficiently large $n$. The first component consequently has valuation at most $C s d^n+O_R(a^n)$. For every $\epsilon>0$, all higher weighted degrees have valuation at least $(C-\epsilon)(s+1)d^n$ eventually, uniformly in their monomials by the two coordinate asymptotics. Choose $\epsilon<C/(s+1)$. The first component is strictly dominant. The value is nonzero and has valuation at least $D\min(V_n,W_n)\gg Dd^n$, whereas height is $O(m d^n)+O_R(1)$. This contradicts the product formula after taking $n\to\infty$ and then $m\to\infty$.

If $r_0=1$, there is a positive rational $t$ with $x=t^p,y=t^q$, by Bézout and $y^p=x^q$. Under iteration $t_n=t^{d^n}$. The one-variable series $J(T)=H(T^p,T^q)$ has coefficient 1 exactly at the strictly increasing positions $pi+qB_i$. If $J$ were algebraic it would be D-finite. Theorem 1.3 with $G=\{1\}$ makes this support eventually periodic. The distances between successive positions would then be eventually periodic, forcing the same conclusion for $B_{i+1}-B_i$ and contradicting the hypothesis on $s$. Thus $J$ is transcendental. The one-variable auxiliary argument from the $d=1$ case now applies at $t_n$: valuations grow as $d^n$ and both relevant heights are $O(d^n)$. This finishes the reducible theorem.

### An explicit nonuniform, nonprimitive expanding script

Take $0\mapsto0011,\ 1\mapsto11$. Its prefix $\sigma^n(0)$ has $2^n$ zeros and $n2^n$ ones. It follows that there are infinitely many zeros, while their proportion tends to zero along these prefixes. An eventually periodic word with infinitely many zeros has a positive limiting proportion of zeros, so the generated word is aperiodic. Assign the rare zero the physical odd-gap block $P=(1,4)$ and the frequent one $L=(2,1)$. Their inverse maps are $f_P(t)=(32t-5)/9$ and $f_L(t)=(8t-7)/9$, with distinct fixed points $5/23$ and $-7$. The complete forward slope on these prefixes is
$$
 (9/32)^{2^n}(9/8)^{n2^n};
$$
it diverges along this sequence of levels. The reducible theorem excludes an algebraic 2-adic completion even here. This fixed script lies outside #190's stated nonuniform primitive hypothesis.

**Sharp input check.** Let $f_0(t)=2t-1$ and $f_1(t)=4t-3$. Their multipliers have positive 2-adic valuation, but both fix $1$. Every finite composition takes $1$ to $1$, so even the aperiodic Jordan script has 2-adic completion $1$ for this pair. This verifies the need for distinct block fixed points in GS2.

### Relation to earlier parity results

Lyapunov Weaver's rStation Paper 16, Theorems 1e–1f, states positive-rational eventual periodicity for the ordinary shortcut parity in two settings. Theorem 1e assumes a nonerasing prolongable substitution with reachable spectral radius above one, semisimple eigenvalues on the spectral circle, and an ordinary frequency for the binary coding. Theorem 1f assumes coupled primitive components with exact incidence matrix $[[A,A],[0,A]]$, positive integral $A$ of irreducible characteristic polynomial and Perron root above one. It allows larger alphabets and binary codings, as well as finite deletion and prepending. The displayed $0011/11$ script is the scalar $A=2$ case; its positive-rational parity exclusion is already covered there. Weaver also credits a prior periodic-approximation criterion for that scalar Jordan example.

GS2 allows any triangular coupling $b>0$ in the two-letter system, imposes no coded-frequency condition, treats arbitrary rational affine inverse blocks obeying its two multiplier and distinct-fixed-point conditions, and concludes transcendence of the physical completion over the rationals. These are the specific claims compared here. Weaver's larger-alphabet conclusions and GS2's algebraic-source exclusion have different scopes. No historical first-result claim is made for either the positive-rational example or the Padé method. [Weaver, *Automatic, primitive, and nonprimitive parity in rational Collatz dynamics*, Theorems 1e–1f and §§19–20](https://rstation.ai/problems/collatz/papers/16)

### Scope and proof audit

PR #190's primitive proof separates an irrational Perron-weight ratio, a nontrivial rational transverse character, and specialization on a fixed subtorus. The proof at the pinned head guards the finite-image proper-prefix issue with periodic repetitions and uses a separate transcendence argument for the weighted clock specialization. The three moving-point leading-term comparisons use positivity of both coordinates, a strictly dominant Perron eigenvalue, and integral or bounded-denominator coefficients as specified there. Reusing that primitive proof for the Jordan case would fail at the assertion that the smaller valuation controls the total height. GS2 instead gives the unequal-scale argument in full. GS2 does not rely on the primitive theorem for its own proof. No theorem of Dirichlet-prime distribution supplies the functional equation $H=P\,H\circ M$ for a general actual itinerary. The unrestricted all-source D-finiteness or another global recurrence remains OPEN.

PR #189 gives an additional reason to keep its entropy criterion separate from substitution structure. On a hypothetical injective orbit with rational scalar, the shifted canonical word $b$ is periodic, with rational mean $B$. The physical mean bound in F1 gives $B\le\log_2 3$, hence $B<\log_2 3$. On a whole number of periods, the canonical coefficient of the prefix is $(3/2^B)^N$, giving an exponential lower bound for the maximum drawup $D_N$ (and the same exponential bound up to a constant for all intermediate lengths). F6's polynomial upper bound on drawup cannot be obtained in this lane from rationality alone. Its separate F4 lower bound on running heights does apply. No property of this canonical word yields a substitution equation for the literal physical gap sequence. [PR #189, F1–F6, a0be70b1ffa075cbc50755ac76036108c028d120](https://github.com/GettysburgResearch/collatz/blob/a0be70b1ffa075cbc50755ac76036108c028d120/research/stationary-carry-rigidity-20261124/FINITE_PHASE_ENTROPY.md)

Lean and execution scope are recorded in [CHECKS.md](CHECKS.md).
