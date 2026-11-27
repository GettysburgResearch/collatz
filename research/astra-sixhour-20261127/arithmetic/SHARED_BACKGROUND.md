# Unbounded markers between a fixed number of copies of one odd-step background

**Status.** Independently reviewed written denominator theorem. It uses a published multivariable greatest-common-divisor estimate for $S$-units. The resulting threshold is ineffective. The number of copies is fixed. All dyadic exponents in the background and all markers can grow independently.

Let $U$ be any word of $n$ positive integer valuations with total $s$. Fix $r\ge2$ and form the cyclic odd-step word
\[
 (U,a_0,U,a_1,\ldots,U,a_{r-1}),\qquad a_i\ge1.
\]
Put $k=n+1$, $T=\sum_i a_i$, $A=rs+T$, and suppose that $D=2^A-3^{rk}>0$. Assume the markers are not all equal. Let $q$ be the **complete reduced denominator** of the positive ordinary rational orbit. No lower bound on the real minimum, cancellation, primitiveness or individual marker size is imposed.

**Theorem.** Uniformly over the above words as $k\to\infty$ with $r$ fixed,
\[
 \log_2q\ \ge\ s+2T/r-(\log_2 3-1)k-o_r(k+s+T).                              \tag{1}
\]
In particular, for every $\epsilon>0$ there is $k_0(r,\epsilon)$ such that
\[
                 q\ge2^{(2-\log_2 3-\epsilon)k}\qquad(k\ge k_0).             \tag{2}
\]
If $(s+T)/k$ stays bounded, the error in (1) is $o_r(k)$ along that sequence and $s\ge k-1$. If $(s+T)/k\to\infty$, the positive terms $s+2T/r$ dominate the error and the ratio $\log_2q/k$ tends to infinity. Taking subsequences covers all choices and proves (2). There is no bound on the number of copies in terms of the period supplied by the $S$-unit estimate itself.

Armstrong's shared-background law introduced the exact factor extraction and Fourier support used here. Its resultant bound contains a factor exponential in $T$, and its bounded-denominator finiteness statement fixes both $r$ and $T$. Here the common divisors at the surviving Fourier frequencies are bounded by a different arithmetic argument. The new conclusion keeps only $r$ fixed and gives (2) even when the markers grow much faster than $k$. Armstrong's separate ordinary rotation exclusions already cover two and three mismatches and give an ineffective finiteness theorem at four. [Armstrong's shared-background law, frozen source](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/results/shared-background-denominator-law/README.md) · [Odd-clock rotation frontier](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-growth.md)

## Exact factorization

Write $S_j$ for the sum of the first $j$ letters of $U$, $P=3^k$, and
\[
 C_U=\sum_{j=0}^{n-1}3^{n-1-j}2^{S_j},\qquad E=3C_U+2^s.
\]
The $i$th block $(U,a_i)$ sends $z$ to $(Pz+E)/2^{s+a_i}$. With $t_j=\sum_{i<j}a_i$ and $t_0=0$, its full fixed point is $E H(P)/D$, where
\[
 H(Z)=\sum_{j=0}^{r-1} Z^{r-1-j}2^{js+t_j}.
\]
Hence $D\mid q EH(P)$. Since $D$ is odd and prime to 3, the ordinary rational steps preserve $q$ on the actual periodic word. For the upper height of the common intercept, $S_j\le s-(n-j)$ gives
\[
  C_U\le 2^s\sum_{u=1}^n3^{u-1}/2^u=2^s((3/2)^n-1),\qquad E\le2^{s+1}(3/2)^k.       \tag{3}
\]

Use the fixed number field $K=\mathbb Q(2^{1/r},\zeta_r)$, the positive real root $b=2^{1/r}$, and $R=2^s b^T$. We have $D=R^r-P^r$. Put $x=P/R$, $Y_j=b^{r t_j-jT}$, $Y_0=1$, and define
\[
 L_d(Y)=\sum_{j=0}^{r-1}\zeta_r^{d(r-1-j)}Y_j,\qquad
 J=\{0\le d<r:L_d(Y)\ne0\}.
\]
These are the Fourier coefficients of the positive vector $Y$, up to index convention and a nonzero factor. Its constant coefficient is positive. If it were its sole nonzero coefficient, Fourier inversion would make $Y_j$ constant. The successive ratios $Y_{j+1}/Y_j=2^{a_j-T/r}$, also over the wrap, would make all markers equal. Thus $|J|\ge2$. The exact evaluations are
\[
       H(P)/R^{r-1}=\sum_{j=0}^{r-1}x^{r-1-j}Y_j,
       \qquad H(\zeta_r^d R)/R^{r-1}=L_d(Y).                                     \tag{4}
\]

## Controlling every exceptional translated subtorus

Let $S$ be the archimedean places of $K$ and the places above 2 and 3. Use normalized absolute values for the absolute Weil height. For $S$-integers $u,v$ put
\[
 N_{\rm gcd,S}(u,v)=-\sum_{w\notin S}\min(0,\log\max(|u|_w,|v|_w)).
\]
The arithmetic theorem of Corvaja–Zannier and Levin says that for fixed coprime polynomials $F,G$ in any finite number of variables over $K$, and every $\eta>0$, this quantity at $F(\mathbf z),G(\mathbf z)$ is at most $\eta\max_i h(z_i)$ outside a finite union of translates of proper algebraic subgroups, for all $S$-unit tuples $\mathbf z$. Use the outside-$S$ part. It needs no condition on the common value of the polynomials at the origin. [Levin–Wang, published Theorem 1.13(a)](https://www.degruyterbrill.com/document/doi/10.1515/crelle-2019-0033/pdf) · [Authors' preprint, Theorem 1.12(a), equations (5)–(6)](https://arxiv.org/pdf/1903.03876) · [Corvaja–Zannier in dimension two](https://arxiv.org/pdf/math/0311030)

For each fixed $d$, uniformly along words with $d\in J$ and $k\to\infty$,
\[
       N_{\rm gcd,S}(x-\zeta_r^d,L_d(Y))=o_r(k+s+T).                               \tag{5}
\]
Here are details of the exceptional cases. Suppose an infinite sequence violates (5) by a fixed positive proportion of $W=k+s+T$. The coordinates $x,Y_1,\ldots,Y_{r-1}$ have absolute logarithmic heights $O_r(W)$. The marker exponents $v_j=r t_j-jT$ have absolute values at most $2rT$. More generally, restrict these exponents to any fixed affine integer lattice $v=v_0+Bz$ containing the retained subsequence, choosing free integer coordinates $z$ from a fixed basis of its difference lattice. Their absolute values are $O_B(W+1)$ by a fixed linear left inverse. Then $Y$ consists of fixed Laurent monomials in the variables $b^{z_i}$ with fixed nonzero coefficients.

The restriction of $L_d$ to these marker variables is a nonzero Laurent polynomial because it is nonzero at every retained word. If it is constant, (5) follows at once from the finite outside-$S$ divisor of that fixed nonzero constant. Otherwise clear its negative powers by an $S$-unit monomial, which leaves $N_{\rm gcd,S}$ unchanged. The resulting polynomial and $X-\zeta_r^d$ are coprime, since the former is independent of $X$. Choose $\eta$ smaller than the assumed violation divided by the fixed height constant at this lattice. The cited theorem puts an infinite retained subsequence in one proper translated algebraic subgroup. After passing to a connected component, some nontrivial integer character is constant there. At every fixed place above 3, all $b^{z_i}$ have valuation zero and $x=3^k/R$ has positive valuation tending to infinity. Thus the exponent of $X$ in that character is zero. A nonzero marker character is constant on the subsequence. Since $b>1$ is real, this means one nonzero integer linear combination of the $z_i$ is a fixed integer. Its solutions, when nonempty, form a translate of an integer lattice of strictly smaller rank. Repeating this argument strictly lowers the rank each time. At rank zero $L_d$ is constant. This contradicts the assumed violation and proves (5). The argument allows the constants and the exceptional sets to change after each restriction.

## Returning to the rational denominator

Factor $D$ over $K$, with factors $d_j=P-\zeta_r^jR$ up to an overall sign. These factors are algebraic integers, all units at primes above 2 and 3. At a place $w\notin S$ the number $R$ is a unit. Reducing the polynomial in (4) modulo $x-\zeta_r^j$ gives the exact equality of local common-divisor orders for $(d_j,H(P))$ and $(x-\zeta_r^j,L_j(Y))$. For $j\in J$, (5) therefore bounds their normalized sum by $o_r(W)$.

At every $w\notin S$, write $v_w$ for its additive order. Since $D\mid q E H(P)$,
\[
 v_w(qE)\ \ge\ \sum_{j\in J}v_w(d_j)-
           \sum_{j\in J}\min(v_w(d_j),v_w(H(P))).
\]
Indeed the left side is at least $\max(0,\sum_{j\in J}v_w(d_j)-v_w(H(P)))$. This proof works even when several distinct $d_j$ share a prime. Summing with the normalized logarithmic weights, the product formula gives
\[
 \log(qE)\ge |J|\log(R-P)-o_r(W).
\]
Every archimedean conjugate of $d_j$ has modulus at least $R-P$ because all conjugates of $\zeta_r^jR$ have modulus $R$. All $d_j$ are units at the excluded finite places. There are only $r$ possible frequencies, so (5) is uniform over the varying subset $J$.

Finally $R-P\ge (R/r)(1-P^r/R^r)$. If $A\ge2rk$, the last parenthesis is at least $1-(3/4)^{rk}$. Otherwise $A<2rk$ and Lagarias's Lemma 2.2(1) gives $A\log2-rk\log3\ge(\log3)/(1200A^{13.3})$. Hence $R-P\ge R/(C_r k^{13.3})$ in both cases, enlarging the absolute-in-$k$ constant for bounded $k$. Therefore $\log_2(qE)\ge2(s+T/r)-O_r(\log(k+1))-o_r(W)$ for all sufficiently large $k$. Combining with (3) proves (1). This argument explicitly retains the full height scale $W$ in the gcd loss. [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

The unrestricted word need not consist of any fixed number of copies of one ordered background separated by single varying markers. Multiple unrelated background intercepts would enter the numerator as a sum and the divisibility by one common $E$ used here would no longer follow.

## A sharper half-turn rate

When $r=2$ the stronger uniform conclusion is $\log_2 q\ge k-o(k)$ as $k\to\infty$. This also quantifies every odd half-turn with exactly two differing valuation entries, since the two differing entries are one pair of aligned markers. Rotate the two blocks so the shorter marker occurs first. For this paragraph only, let $N=2^{s+\min(a_0,a_1)}$, $K_0=|a_1-a_0|>0$, $u=2^{K_0}-1$, $G=\gcd(P+N,u)$. At the two macro starts write their **integer** numerators as $x,y$ over $q$. They obey
\[
              Ny=Px+qE,\qquad (u+1)Nx=Py+qE,
\]
so $(P+N)(y-x)=Nux$. Coprimality of $N$ and $P+N$ gives $(P+N)\mid Gx$ and $y>x$. After the same first $j<k$ letters of either block, its integer numerator is at least $3^j x/2^{S_j}$. The remaining $k-j$ short-block exponents are all positive, hence $N/2^{S_j}\ge2^{k-j}$. Every odd numerator is therefore at least $2^k/G$. In particular $q\mu\ge2^k/G$ for the odd real minimum $\mu$.

If $K_0\le3k$, reduce the exponent $\log_2N$ modulo $K_0$ to $0\le h<K_0$. Apply Corvaja–Zannier Proposition 2 to the multiplicatively independent $\{2,3\}$-units $2^{K_0}$ and $-3^k/2^h$. Their heights are $O(k)$, and independence follows from their 3-valuations. At every prime dividing $G$, the two quantities minus one have common order equal to its order in $G$. Thus $\log G=o(k)$ uniformly. The odd real minimum has $\log(\mu+1)=O(\log(k+1))$ uniformly even for arbitrarily large clocks: if $A<4k$ use Lagarias as above and the telescoping inequality $A\log2-2k\log3<2k/(3\mu)$; if $A\ge4k$ the same inequality gives an absolute bound. This proves the desired estimate when $K_0\le3k$. If $K_0>3k$, the long gap and the positive integer next numerator give $2^{K_0}\le3q(\mu+1)(3/2)^{2k}$ since an odd step multiplies $z+1$ by at most $3/2$. This gives an even larger exponent. [Corvaja–Zannier, Proposition 2](https://arxiv.org/pdf/math/0311030)

[The strict Lean module](SharedBackground.lean) proves the exact full-intercept factorization in a run with variable block divisors, the resulting complete determinant divisibility, and the half-turn integer divisibility above. The archimedean, Fourier and imported $S$-unit estimates are written proofs. [The exact replay](check_shared_background.py) compares the full carry with the factorization, the Fourier support via a rational polynomial gcd, and every odd valuation and denominator on each recorded cycle. Its controls include nonprimitive marker patterns with actual polynomial cancellation and marker sums exceeding 1,400. [Recorded output](../../../reports/astra-sixhour-20261127/arithmetic/shared_background.json)
