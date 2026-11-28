# The complete denominator at fixed prime odd grade

For the shortcut map \(T(x)=x/2\) on even odd-denominator rationals and \(T(x)=(3x+1)/2\) on odd ones, let \(L\) be the **least** native period of a positive rational cycle, \(p>0\) its number of odd departures, and \(q\) its complete reduced denominator at any phase. Write
\[
                       \sigma=\frac{\log_2 q}{L}.
\]

**Proposed theorem.** At each **fixed prime** \(p\), along all these cycles as \(L\to\infty\),
\[
                            \sigma\longrightarrow1.                     \tag{1}
\]
This includes the clocks \(p\mid L\). More generally, if \(p\) is fixed and coprime to six, every sequence has a subsequence on which, for a fixed \(g\mid\gcd(L,p)\) and a fixed set \(S\) of divisors of \(g\),
\[
 \sigma\longrightarrow\frac{1}{g}\sum_{d\in S}\varphi(d),\qquad
             1\in S,\qquad \operatorname{lcm}_{d\in S}d=g.              \tag{2}
\]
In particular at \(p=\ell^a,\ \ell\ge5\) prime,
\[
                    \liminf \sigma=1-\frac1\ell+\frac1p.                \tag{3}
\]
At \(p=4\) the possible limits are exactly \(3/4\) and \(1\). The four-odd-step case supplies a primitive counterexample to (1) for general fixed composite grades.

The [PR212 moving-arc theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MOVING_ARCS.md) already implies fixed-grade rational quantization with limit denominator dividing \(\gcd(L,p)\), and hence (1) for coprime clocks: decompose into at most \(2p\) powers of the single-letter motifs. The present argument determines which orders must survive at a primitive cycle. It uses the fixed-target Laurent gcd method of the [bounded-grade paired-period theorem](BOUNDED_GRADE_PAIRED_PERIODS.md). Belaga's [Theorem 3.2 and (1.4)](https://www.impan.pl/shop/publication/transaction/download/product/82606) give \(L/p\le\log_2(q+3)\) for arbitrary primitive rational cycles by clearing the denominator. No increasing-grade uniformity is asserted in (1)–(3).

## A proper shorter congruence cannot persist

Write \(b_t=q x_t\) at native date \(t\), with cyclic subscripts. Each \(b_t\) is an integer prime to three and \(q\) is prime to six. This follows by rotating the word carry: in its sum the last odd departure contributes a two-power and every preceding term is a multiple of three, while the raw denominator \(D=2^L-3^p\) is prime to six. The denominator is the same at every date by the native affine formulas. For fixed \(p\) all \(x_t\le 2\cdot3^p\) when \(L\) is sufficiently large, since each rotated carry is at most \(2^L3^p\) and \(D\ge 2^{L-1}\). Thus for every fixed \(\delta>0\), outside \(O_{p,\delta}(1)\) native dates one has \(x_t<\delta\). Indeed a fixed number of consecutive even letters suffices to halve that uniform upper bound below \(\delta\), and each of the \(p\) odd letters rules out at most that many dates.

There are consequently no relations, along an infinite family of these least-period cycles, of the form
\[
    q\mid C(2^K-3^H),\qquad 0<K<L,\qquad 0\le H\le p,                  \tag{4}
\]
for any **fixed** positive integer \(C\), even if \(K,H\) vary. Take a date where both \(x_t\) and \(x_{t+K}\) are less than \(1/(3C3^p)\). Such a date exists because the two exceptional sets have bounded cardinality, also for variable \(K\). The word on this interval has some grade \(h\le p\), so \(2^K b_{t+K}\equiv3^h b_t\bmod q\). By (4), \(C(3^H x_{t+K}-3^h x_t)\) is an integer of absolute value less than one. Equality to zero and the ternary-unit numerators force \(H=h\), and then \(x_{t+K}=x_t\), contrary to the least period.

## A fixed polynomial on the binary exponent lattice

On an arbitrary subsequence, fix the odd departure positions \(0\le u_0<\cdots<u_{p-1}<L\) as coordinates (their values vary). Thus
\[
       A=\sum_{i=0}^{p-1}3^{p-1-i}2^{u_i},\qquad q=D/\gcd(D,A).
\]
Pass to a rational affine space of least dimension containing infinitely many of the integer vectors \((L,u_0,\ldots,u_{p-1})\) and retain those points. In an integral basis of its direction lattice, a unimodular change of variables for the nonconstant coordinate \(L\) gives
\[
             L=a+kn,\qquad u_i=b_i+c_i n+v_i\cdot m,\qquad k>0,
\]
where \(a,b_i,c_i\) and the integer vectors \(v_i\) are fixed. The varying integer coordinates \(n,m\) are \(O(L)\) by a fixed left inverse, and \(n\to\infty\). No proper fixed affine hyperplane in these coordinates contains infinitely many of the retained points. Let \(X=2^n,\ Y_j=2^{m_j}\). The Laurent polynomials with values \(D,A\) are
\[
 F=2^a X^k-3^p,\qquad B=\sum_i 3^{p-1-i}2^{b_i} X^{c_i}Y^{v_i}.
\]
In \(\mathbb Q[X]\) choose the monic product \(U\) of the irreducible factors of \(F\) dividing \(B\) in the rational Laurent ring, and put \(V=F/U\). The polynomial \(F\) is squarefree. The positive real root of \(F\) cannot be a root whose irreducible factor divides \(B\): specialize all \(Y_j=1\) and every term of \(B\) is strictly positive there. In particular \(\deg V>0\).

Here is the exact denominator estimate on this subsequence:
\[
                  \log_2 q=\frac{\deg V}{k}\,L+o(L).                   \tag{5}
\]
The monic factors of \(2^{-a}F\) have coefficients integral outside \(2,3\), as do their quotients; all roots are units at such primes. Monic division after clearing Laurent powers puts \(B/U\) in the same ring integral outside \(2,3\). At all primes outside \(2,3\) simultaneous cancellation of \(U(X)\) gives the denominator from \(V(X)\) and its gcd with \((B/U)(X,Y)\). These residual polynomials are coprime. Multiply the second by a Laurent monomial to clear negative exponents, using the componentwise smallest exponents so as not to introduce a common variable factor. By [Levin–Wang, Theorem 1.13(a)](https://doi.org/10.1515/crelle-2019-0033) their logarithmic gcd outside \(2,3\) is \(o(L)\). Indeed the coordinate heights are \(O(L)\), and points on a translated proper subgroup would have some fixed nontrivial character constant. Its valuation at two would contradict the minimal affine-space choice. For each chosen error the theorem excludes just a fixed finite union of such translates. A nonzero constant residual gives the same assertion directly. The absolute real value of \(V(X)\) is \(2^{n\deg V+O(1)}\). Its valuation at two is eventually that of its nonzero constant term since \(n\to\infty\). At three, the factors \(U(X),2^{-a}V(X)\) are integral (roots have nonnegative valuation there), and their product \(2^{-a}D\) is a unit. Thus the logarithm of the part outside \(2,3\) is \(n\deg V+O(1)\) in base two, proving (5).

## The orders retained by a primitive orbit

Put \(g=\gcd(k,a,p)\), \(k'=k/g\), \(a'=a/g\), \(p'=p/g\), and \(Z=2^{a'}X^{k'}/3^{p'}\). Then \(g\mid \gcd(L,p)\), and \(F=3^p(Z^g-1)\). Let \(S\) be the set of divisors \(d\mid g\) for which \(V\) has a root with \(Z\) of exact order \(d\). The positive-root argument gives \(1\in S\). If \(e=\operatorname{lcm}S<g\), squarefreeness gives divisibility of \(Z^e-1\) by \(V\) in \(\mathbb Q[X]\). After clearing **fixed** coefficient denominators, (5)'s exact outside-\(\{2,3\}\) divisibility \(v(q)\le v(V(X))\) shows
\[
                     q\mid C(2^{eL/g}-3^{ep/g})
\]
for a fixed positive integer \(C\). All evaluations use \(X=2^n\), now an integer, and \(q\) is prime to six. This is forbidden by (4). Thus \(\operatorname{lcm}S=g\), for arbitrary fixed \(p\).

When \(p\) is coprime to six, for every \(d\mid g\) the polynomial \(\Phi_d(Z)\) is irreducible in \(\mathbb Q[X]\) up to its nonzero leading constant. To see this, take a primitive \(d\)th root \(\zeta\), \(K=\mathbb Q(\zeta)\), and any root \(x\) with \(x^{k'}=3^{p'}2^{-a'}\zeta\). Then \(K\subseteq\mathbb Q(x)\). At primes of \(K\) over three and two, which are unramified since \(d\) is prime to six, all conjugates of \(x\) over \(K\) have valuations \(p'/k'\) and \(-a'/k'\), respectively. The constant term of the monic minimal polynomial lies in \(K^\times\), so its degree \(r\) satisfies \(k'\mid rp'\) and \(k'\mid ra'\). Since \(\gcd(k',p',a')=1\), \(k'\mid r\), and \(r=k'\). The rational degree is therefore \(k'\varphi(d)\). This is exactly the degree of \(\Phi_d(Z)\). Thus \(V\) retains the whole component at each \(d\in S\), and (5) proves (2). If \(p=\ell^a,\ \ell\ge5\), then either \(g=1\) or \(g=\ell^b\) and \(g\in S\); the exponent is at least \((1+\varphi(g))/g\ge 1-1/\ell+1/p\). In particular it is one at prime \(p\ge5\).

The small primes can also be treated directly. For \(p=2,3\), if \(g=1\), any rational monic factor of \(2^{-a}F\) of degree \(r\) has constant-term valuations \(rp/k,-ra/k\), forcing \(k\mid r\). Thus \(F\) is irreducible and \(\sigma\to1\). Otherwise \(g=p\), \(p'=1\), and \(1,p\in S\). The \(d=1\) component is irreducible by its valuation \(1/k'\) at three. This also treats \(d=2\) at \(p=2\) because \(\mathbb Q(-1)=\mathbb Q\). For \(p=d=3\), take \(K=\mathbb Q(\zeta)\) with \(\zeta\) a primitive cube root; normalized valuation at its prime over three gives \(v(3)=2\). When \(k'\) is odd this already forces relative degree \(k'\). When \(k'\) is even put \(w=x^{k'/2}\); its square is \(3\,2^{-a'}\zeta\). Since \((1-\zeta)^2=-3\zeta\), adjoining \(w\) is adjoining \(\sqrt{-2^{-a'}}\). This is a genuine quadratic extension of \(K\): according to the parity of \(a'\), its rational square class is \(-1\) or \(-2\), and their quadratic fields differ from \(K=\mathbb Q(\sqrt{-3})\). The extension is unramified at the prime over three, because this is a square root of a local unit in odd residue characteristic (it either splits locally or gives the unramified quadratic extension). There \(w\) has normalized valuation one. Consequently \(x^{k'/2}=w\) forces degree \(k'/2\) over \(K(w)\) by the same constant-term valuation. The full degree over \(K\) is \(k'\). This proves (1) in all cases.

For \(p=4\) and \(g=1\) the constant-term argument again gives the full exponent. For \(g=2\), both \(d=1,2\) must survive; in each case \(K=\mathbb Q\) and the two rational valuations have numerators \(p'=2,-a'\), sufficient by \(\gcd(k',2,a')=1\). For \(g=4\), all three possible \(\Phi_d(Z)\) are irreducible because the prime over three is unramified in \(\mathbb Q(i)\) and \(p'=1\). Orders \(1,4\) must survive and order \(2\) is optional, leaving \(3/4\) and \(1\).

## Sharp primitive words

For \(p=\ell^a,\ \ell\ge5\), or \(p=4\) and \(\ell=2\), put \(b=p/\ell,\ L=pn,\ X=2^n\), and take the \(p\) odd dates
\[
          u_i=in+\mathbf 1_{0\le i<b},\qquad 0\le i<p,\quad n\ge3.
\]
The cyclic gaps have a unique occurrence of \(n+1\) and a unique occurrence of \(n-1\), so the word is primitive. Its unique rational periodic realization is positive for all sufficiently large \(n\). Indeed the usual word fixed point has odd denominator and realizes its word modulo \(2^L\), and \(2^L>3^p\). The carry polynomial is
\[
              3^{p-1}\left(\sum_{i<p}(X/3)^i+\sum_{i<b}(X/3)^i\right).
\]
At any nontrivial \(p\)th root of unity \(X/3\), it vanishes exactly at the nontrivial \(b\)th roots. At \(X=3\) it is positive. In fact the complete denominator is exactly
\[
 q=\frac{(X-3)(X^p-3^p)}
           {(X^b-3^b)\gcd(X-3,\ell+1)}.                               \tag{6}
\]
Indeed after cancellation of the integer \((X^b-3^b)/(X-3)\), writing \(Q=(X^p-3^p)/(X^b-3^b)\), the residual denominator and carry are \((X-3)Q\) and \(Q+3^{p-b}\). Here \(Q\) is a ternary unit, so these last two expressions have gcd \(\gcd(X-3,Q+3^{p-b})=\gcd(X-3,\ell+1)\), by reducing \(X\) to three. Thus
\(\log_2 q/L\to(p-b+1)/p\). This attains (3) and \(3/4\) at grade four. The value one is attained at grade four by choosing \(L=4n+1\) with four consecutive odd dates; the carry is fixed and the unique cyclic gap exceeding one makes the word primitive.

These bounds concern complete rational periodic denominators. They do not give the exponential multiplicative order bound in the [periodic pumping question](PERIODIC_PUMP_FRONTIER.md), nor a time bound for any fixed ordinary positive orbit.
