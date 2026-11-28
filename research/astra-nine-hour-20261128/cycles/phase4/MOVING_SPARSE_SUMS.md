# Sharp complete-denominator rates for sparse sums with moving coefficients

**Proposed written theorem, conditional only on cited established Diophantine theorems.** PR212 proves a sharp sparse rate and rational limit quantization for fixed odd integral coefficients in one dyadic period window. Here the coefficients may vary through rationals of sublinear logarithmic height, with no fixed restriction on their prime factors. Positivity permits arbitrary exponent positions. A signed version retains either a dyadic separation condition or a stable real evaluation. The application to [moving powered words](MOVING_POWERED_WORDS.md) allows a fixed number of different moving templates and moving connectors on a primitive rational cycle. The number of terms is fixed in the following Subspace Theorem argument. [PR212, 505d3fe782922904e86477990cc5d41e9110edda, SPARSE_DENOMINATORS.md, (2)–(8)](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/SPARSE_DENOMINATORS.md) · [Weaver–Mahler–Wren, paper 22/v2, Lemma 3, qualitative signed sparse-multiple gap](https://rstation.ai/problems/collatz/papers/22/v2)

Take $n\to\infty$, $0<u<n$, $X=2^n3^{-u}>1$ and $D=2^n-3^u$. Put
$$ V=\sum_{j=1}^r c_jY_j,\qquad Y_j=2^{a_j}3^{b_j},\qquad
     |a_j|+|b_j|=O(n),\qquad c_j\in\mathbb Q^\times,\quad h(c_j)=o(n). $$
Here $r$ is fixed and $h$ is absolute logarithmic Weil height. Clear the coefficients' rational denominators by a common positive integer with logarithm $o(n)$ and clear powers of two and three from the resulting sum. Let $d_V=D/\gcd(D,V_{\rm clear})$. Different common clearings whose residual factors outside two and three have height $o(n)$ change $\log d_V$ by $o(n)$. Equivalently compute the native outside-$\{2,3\}$ denominator contribution of $V/(X-1)$ up to $o(n)$ in its logarithm. The assumption is one of the following.

1. All $c_j$ are positive.
2. The adjusted dyadic indices $a_j+v_2(c_j)$ are pairwise distinct modulo $n$.
3. $X\to1$ and $\left|\sum_j c_jY_j\right|\ge\epsilon\sum_j|c_jY_j|$ for some fixed $\epsilon>0$.

Then
$$              \liminf\frac{\log d_V}{n\log2}\ \ge\ \frac1r.        \tag{1}$$
Every subsequential limit of this normalized log is rational. Its reduced denominator divides $\gcd(n,u)$ on a further subsequence attaining the limit. In particular the normalized log tends to one if $n,u$ are coprime throughout, or if every fixed prime eventually misses their gcd. The sharpness example at $g=r$ is $V=\sum_{j=0}^{r-1}(2^N)^j(3^U)^{r-1-j}$ at $n=rN,u=rU$, giving exactly $d_V=2^N-3^U$.

## A lattice of limiting exponent vectors

Restrict to any subsequence on which the normalized denominator log tends to a limit. Make the common rational coefficient clearing first; its height is $o(n)$ since $r$ is fixed. This preserves each of the three conditions. Absorb only two-three units later. Extract limits of the exponent pairs divided by $n$ for $X,Y_1,\ldots,Y_r$. The subgroup of $\mathbb R^2$ generated over $\mathbb Z$ by these finitely many vectors is free abelian. Its rank $t$ can exceed two because the scalars here are integers, not reals. Choose a basis with the nonzero vector of $X$ equal to $e$ times its first member, $e\ge1$. Lift each basis element to a fixed integral combination of the original exponent vectors. This gives positive rational two-three monomials $Z_1,\ldots,Z_t$ depending on the input, with
$$ X=\xi_0 Z_1^e,\qquad
   Y_j=\xi_j Z_1^{m_j}\prod_{l=2}^t Z_l^{m_{jl}}.                    \tag{2}$$
All exponents on the right are fixed integers on this subsequence. Each $\xi_j$ is a rational two-three unit with height $o(n)$: the two valuations of the quotient have zero normalized limit. The $Z_l$ have height $O(n)$, and every fixed nontrivial character in them has height bounded below by a positive multiple of $n$ eventually, because its limiting exponent vector is nonzero. In particular the height of $Z_1$ equals $n\log2/e+o(n)$ since $h(X)=n\log2$.

Work over the fixed number field $K=\mathbb Q(\mu_e,2^{1/e},3^{1/e})$. The positive number $\theta=\xi_0^{-1/e}$ belongs to $K$ and has height $o(n)$. The roots of the first polynomial in (2) at $X=1$ are $\omega\theta$, $\omega\in\mu_e$. Their heights remain uniform over all conjugates via the absolute Weil height. Express $V$ as a moving Laurent polynomial $G$ in the $Z_l$ by (2), with rational coefficients of height $o(n)$. Multiplication by a single fixed Laurent monomial clears all negative exponents and is a unit outside two and three upon evaluation. On a further subsequence its support and degree are fixed. Its coefficients are integral outside the places over two and three after the initial clearing. An order-$e$ character component is called active here if $G(\omega\theta,Z_2,\ldots,Z_t)$ is not the zero Laurent polynomial. Extract a common active subset with cardinality $J$.

## How many components survive

Evaluate the coordinates other than $Z_1$ at their actual positive values. At the root $\omega\theta$, the original $j$th term becomes
$$                 c_jY_j X^{-m_j/e}\omega^{m_j}.                   \tag{3}$$
Group the complex coefficients of (3) by $m_j\bmod e$ before inserting $\omega$. The resulting Fourier vector has at most $r$ occupied entries. In case 1 its entries are nonnegative and some entry is positive. In case 3 its sum at $\omega=1$ is nonzero eventually: multiplying the individual terms by $X^{-m_j/e}=1+o(1)$ perturbs the sum by $o(\sum|c_jY_j|)$ because the $m_j$ are fixed. In case 2 choose a place over two with valuation normalized by $v_2(2)=1$. Inside any one occupied class the unweighted terms have valuations
$$                       a_j+v_2(c_j)-m_j n/e . $$
These are distinct by condition 2, as the $m_j$ in the class differ by multiples of $e$. The term of least valuation is unique and the class sum is nonzero. Thus in every case the Fourier vector is nonzero.

For any nonzero vector on $\mathbb Z/e$ with at most $r$ nonzero entries, at least $e/r$ of its Fourier coefficients are nonzero. Indeed every squared coefficient is at most $r$ times the squared Euclidean norm of the vector by Cauchy–Schwarz, whereas their sum is exactly $e$ times that norm by elementary character orthogonality. A nonzero value at the actual remaining coordinates implies active polynomial restriction. Hence $J/e\ge1/r$.

## Complete prime powers on each component

Let $S$ comprise the archimedean places of $K$ and all places above two and three. Use normalized local logarithms, so the sum over places over one rational prime agrees with the rational calculation on rational inputs. At every $v\notin S$, the factors $Z_1-\omega\theta$ are integral and multiply, up to the unit $\xi_0$, to $X-1$. Denote the outside-$S$ logarithmic zero mass of the factor by $H_\omega$. This is the sum of $-\log|Z_1-\omega\theta|_v$ at those places. None of the factors vanishes at the arguments since $X>1$. The total equals $\log D=n\log2+o(n)$ by the [two-logarithm separation](../CONTRACTING_CALENDARS.md). The product formula gives
$$ H_\omega\le h(Z_1-\omega\theta)
       \le h(Z_1)+h(\theta)+\log2=n\log2/e+o(n). $$
There are $e$ fixed components. The sum and these individual upper bounds imply $H_\omega=n\log2/e+o(n)$ for **every** component. The argument incorporates all archimedean embeddings and does not require lower bounds at a separately selected embedding.

For an active $\omega$, the polynomials $Z_1-\omega\theta$ and $G$ are coprime over $K$. The root is a unit in the Laurent ring and the active specialization is nonzero, so multiplication by the chosen monomial does not introduce this factor. They have coefficients of height $o(n)$ and at least the first has nonzero constant term. If $G$ has positive degree, apply Grieve–Wang Theorem 1.2 (or the outside-$S$ Theorem 3.1) to the moving polynomials and the $S$-unit arguments $Z_l$. Their maximum height is comparable to $n$. The alternative of a fixed nontrivial character with height $o(n)$ on a subsequence is impossible by the basis construction. Thus the outside-$S$ logarithmic gcd is $o(n)$: if a fixed positive fraction remained on some subsequence, apply the external theorem there with a smaller fixed tolerance. For a nonzero constant $G$ the coefficient height alone gives the same result. The moving theorem's small-character conclusion is explicit in the proof of its Theorem 3.1, equation (3.21). [Grieve–Wang, Theorems 1.2 and 3.1](https://arxiv.org/pdf/1902.09109)

At each outside place let $w_\omega\ge0$ be its valuation on the factors, and $b\ge0$ its valuation on the evaluated $G$. Then
$$  \sum_{\omega\ {\rm active}}\big(w_\omega-\min(w_\omega,b)\big)
             \le \left(\sum_\omega w_\omega-b\right)_+. $$
This proves the lower bound $\log d_V\ge Jn\log2/e-o(n)$ without assuming disjoint prime support. For the matching upper bound, the product of all inactive linear factors divides $G$ in the Laurent polynomial ring over $K$. After the fixed monomial clearing, successive monic divisions preserve integrality outside $S$ because the roots are units there. Hence the product's entire outside zero mass, including shared prime powers, is canceled in $G$. This gives
$$                  \frac{\log d_V}{n\log2}\ \longrightarrow\ J/e  \tag{4}$$
on the retained subsequence and proves (1).

The active roots are conjugation stable over $\mathbb Q$ on each input because both the binomial and $G$ have rational coefficients. Their monic polynomial therefore has a nonzero rational constant, whose ordinary absolute value is $\theta^J$. Rationality forces $e\mid Jv_2(\xi_0)$ and $e\mid Jv_3(\xi_0)$. By (2) these valuations are congruent respectively to $n$ and $-u$ modulo $e$. Thus $e/\gcd(e,J)$ divides both clock counts on the retained subsequence. This proves the quantization and coprime-type assertions.

The preceding arithmetic includes the established fixed-coefficient result as an overlapping case. The new input in this formulation is the quotient by **limiting** exponent relations, keeping their finite-input discrepancies as small-height units in fixed moving polynomials. It gives no effective onset or estimate uniform in a growing term count. The positivity and dyadic hypotheses prevent total vanishing on the components; the signed sparse polynomial $X-1$ itself illustrates the necessity of some such hypothesis.

## Positive coefficients and the least prime in the clock gcd

In case 1 there is a further conclusion. If every prime dividing $g=\gcd(n,u)$ is **greater than the fixed term count $r$**, then $\log_2 d_V/n\to1$. This permits the same large prime to divide the two clock counts throughout. Case 2 alone cannot give this improvement: for a fixed odd prime $g>2$, the two-term signed sum $V=2^N3^{-U}-1$ at $n=gN,u=gU$ has separated dates $0,N$ but cancels the entire principal determinant, giving limiting denominator rate $(g-1)/g$ when $N\to\infty$ and $D>0$.

For case 1 every component is active. Indeed at an actual positive specialization the putative vanishing in (3) is
$$               \sum_j q_j\beta^{m_j}=0,\quad q_j=c_jY_j>0
                   \text{ rational},\quad \beta=\omega X^{-1/e}. $$
Let $h_0=\gcd(e,n,u)$, $d=e/h_0$, $R=2^{n/h_0}3^{-u/h_0}$, and $\zeta=\omega^d$ of order $b\mid h_0$. Thus $\beta^d=\zeta/R$. The case $r=1$ is immediate. For $r=2$ a vanishing sum requires $\beta^{m_1-m_2}$ to be a negative rational. Its absolute value is $X^{-(m_1-m_2)/e}$, so $e$ divides both $n(m_1-m_2)$ and $u(m_1-m_2)$, hence $d\mid m_1-m_2$. Its phase is then a power of $\zeta$, whose odd order forbids $-1$.

For $r\ge3$, the order $b$ is coprime to six. In the cyclotomic field $K_0=\mathbb Q(\zeta)$ the rational primes two and three are unramified. The binomial $T^d-\zeta/R$ is irreducible over $K_0$: every monic factor of positive degree $k$ has constant term valuations $-k v_p(R)/d$ above $p=2,3$, using integer-valued valuations with $v_p(p)=1$. Since $\gcd(d,n/h_0,u/h_0)=1$, integrality of these valuations forces $d\mid k$. This also works for $b=1$ and forces $k=d$. Grouping a putative vanishing sum by $m_j\bmod d$ now forces each occupied class to vanish separately, by the power basis of $\beta$ over $K_0$. Each such coefficient is a nonempty sum of at most $r$ positive rational multiples of $b$th roots of unity.

For completeness such a sum cannot vanish if the least prime of $b$ exceeds $r$. Induct on $b$, the case $b=1$ being positivity. If $p^2\mid b$, group by the exponent modulo $p$ of a primitive $b$th root; its powers of degrees $0,\ldots,p-1$ are independent over $\mathbb Q(\mu_{b/p})$ by the cyclotomic degree formula. Each nonempty class would give a forbidden shorter-order relation. If $p\parallel b$, decompose each root into a $p$th root and a $(b/p)$th root. The only linear dependence of the $p$th roots over $\mathbb Q(\mu_{b/p})$ is their complete sum, again by the degree formula. Since fewer than $p$ terms occur, some class is empty, so all coefficients must vanish. An occupied class again contradicts the induction hypothesis. Thus every specialized sum survives. In (4) one has $J=e$, proving full denominator rate.
