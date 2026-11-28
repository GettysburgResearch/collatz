# Explicit complete denominator spectra at every prime-power odd grade

Let \(p\) count odd departures at the **least** native period \(L\) of a positive rational shortcut cycle. Let \(q\) be its full reduced denominator. Write \(\mathcal S_p\) for the possible limits of \(\log_2(q)/L\) along such cycles as \(L\to\infty\) with \(p\) fixed.

For every **odd** prime \(\ell\) and \(p=\ell^a\), \(a\ge1\), the complete list is
\[
 \mathcal S_{\ell^a}=
 \left\{\frac{1+\sum_{b\in B}\varphi(\ell^b)}{\ell^a}\ :\
                  a\in B\subseteq\{1,\ldots,a\}\right\}.                \tag{1}
\]
For binary prime powers it is
\[
 \mathcal S_2=\{1\},\qquad \mathcal S_4=\{3/4,1\},\qquad
 \mathcal S_{2^a}=\left\{\frac{j}{2^a}:2^{a-1}\le j\le2^a,\ j\in\mathbb Z\right\}
                           \quad(a\ge3).                                \tag{2}
\]
For example \(\mathcal S_9=\{7/9,1\}\), \(\mathcal S_{27}=\{19/27,21/27,25/27,1\}\), and \(\mathcal S_8=\{1/2,5/8,3/4,7/8,1\}\). Every value in (1)–(2) has an explicit family with \(\log_2 q=\sigma L+O_p(1)\). All limits here fix the grade before letting the physical period grow.

The [prime-grade denominator theorem](../ordinary/PRIME_GRADE_DENOMINATORS.md) gives (1) at primes, the minimum at odd prime powers \(\ell\ge5\), all of grade four, the retained-order condition and its fixed-target gcd argument. The [decidable spectrum theorem](../ordinary/DECIDABLE_FIXED_GRADE_SPECTRUM.md) supplies the reduction to affine families and the positive-radical degree over the maximal abelian extension. The [PR212 moving-arc theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MOVING_ARCS.md) already gives general fixed-grade quantization. We give the explicit realization of every retained-order subset, the ramified-component analysis at grades divisible by two or three, and primitive families attaining the additional binary rate \(1/2\).

## The field degree at each possible order

Use an affine calendar from the cited reduction, with \(L=kn+A\), \(X=2^n\), and odd positions affine in \(n\). Its denominator polynomial is \(F=2^A X^k-3^p\). The reduced exponent is \(\deg V/k\), where \(V\) is the residual polynomial after canceling the polynomial gcd with the carry. Put
\[
 g=\gcd(k,A,p),\qquad k'=k/g,\quad A'=A/g,\quad p'=p/g.
\]
The orders \(d\mid g\) retained by \(V\) include one and have least common multiple \(g\), by the physical no-shorter-congruence argument in the prime-grade theorem. For a primitive \(d\)-th root \(\zeta\), set \(K=\mathbb Q(\zeta)\) and take a root \(x\) with
\[
                   x^{k'}=3^{p'}2^{-A'}\zeta=\eta .
\]
Then \(K\subseteq\mathbb Q(x)\). Over \(\mathbb Q^{\rm ab}\) the degree of \(x\) is \(k'/\gcd(2,k')\) by [the positive-radical argument](../ordinary/DECIDABLE_FIXED_GRADE_SPECTRUM.md): multiplication by a root of unity identifies \(x\) with the positive radical there. This degree divides \([K(x):K]\). Indeed \(\mathbb Q^{\rm ab}/K\) is normal and separable: restricting the finite Galois Kummer group over \(\mathbb Q^{\rm ab}\) gives an orbit of size \(k'/\gcd(2,k')\) on every root in a given \(K\)-conjugacy class, so its size divides the size of that class. Equivalently, each irreducible factor over \(K\) splits over \(\mathbb Q^{\rm ab}\) into factors all of that common degree. Since \(x\) satisfies a degree-\(k'\) binomial, only a factor of two can be missing. For odd \(k'\) the whole component of degree \(k'\varphi(d)\) is irreducible over \(\mathbb Q\).

Here and below use normalized discrete valuations of number fields. When all conjugates of the root of a binomial have valuation \(s/t\) in lowest terms relative to a given base field, the valuation of the minimal polynomial's nonzero constant term forces \(t\) to divide the degree. In particular an odd valuation of \(\eta\) forces the full two-part of \(k'\) into \([K(x):K]\).

For \(p\) a power of three, every order component is irreducible. We only need to consider even \(k'\), and \(p'\) is odd. At \(d=1\) use the odd valuation \(p'\) at three. At \(d>1\), the prime two is unramified, so odd \(A'\) gives the full two-part as well. In the remaining case \(d=3^c\), \(c\ge1\), and \(A'\) is even. The element \(\eta\) differs from 3 by a square in \(K\), since \(\zeta\) has odd order. The only quadratic subfield of \(\mathbb Q(\zeta_{3^c})\) is \(\mathbb Q(\sqrt{-3})\): its cyclotomic group is cyclic, and the displayed subfield is present. Thus \(y=x^{k'/2}\) generates a quadratic extension of \(K\). At the prime over three one has \(v_K(\eta)=2\cdot3^{c-1}p'\). Adjoining its square root is unramified at this odd residue characteristic: remove an even power of a uniformizer and adjoin the square root of a unit, which either splits or is unramified. At each resulting prime \(v_{K(y)}(y)=3^{c-1}p'\) is odd. Now \(x^{k'/2}=y\) forces the entire two-part of \(k'/2\) into \([K(x):K(y)]\). The initial quadratic degree supplies the other two. Hence \([K(x):K]=k'\). For odd primes \(\ell\ge5\), irreducibility is already proved by the two unramified valuations in the prime-grade theorem.

For \(p\) a power of two, the order-one component is always irreducible. At even \(k'\) either \(p'\) is odd and the unramified valuation at three is odd, or \(p'\) is even and \(A'\) must be odd by \(\gcd(k',A',p')=1\). At \(d=1,2\) in the latter case use the odd two-adic valuation in \(K=\mathbb Q\). At \(d\ge8\) in the latter case, \(K\) contains \(\sqrt2\) and \(i\), hence the square class of \(\eta\) is that of the primitive \(d\)-th root \(\zeta\). It has no square root in \(K\), since such a root has exact order \(2d\) and \([\mathbb Q(\zeta_{2d}):K]=2\). In any field containing \(i\), successive square roots of a nonsquare give a full quadratic tower. Indeed the norm of a square root of \(a\) in its quadratic extension is \(-a\), a nonsquare in the base field when \(a\) is a nonsquare and \(-1\) is a square. The root therefore remains a nonsquare in the new field, and induction applies. Taking the two-part of \(k'\) in \(x^{k'}=\eta\) proves full relative degree here too. At \(d=4\) at least half the component survives whenever it is retained, by the abelian degree bound. A genuine split is possible because \((1+i)^2=2i\).

For an odd prime power, \(g=\ell^c\) and irreducibility imply that the rates at \(g>1\) have the form \((1+\sum_{b\in B'}\varphi(\ell^b))/\ell^c\) with \(c\in B'\); at \(g=1\) the rate is one. Multiplying by \(\ell^{a-c}\) in numerator and denominator inserts all orders through \(a-c\) and moves each original order \(b\) to \(a-c+b\). Thus these values all appear in the candidate list (1). At binary grade and \(g\ge8\), both \(1\) and \(g\) must survive in full, so the rate is at least \(1/g+1/2\). At \(g=4\) retention of \(1,4\) gives at least \(1/4+1/4=1/2\), and at \(g=1,2\) the rate is one. Every degree contributes an integral multiple of \(k'\) to \(\deg V\), even the possible half of the \(\varphi(4)k'\) component. Thus the denominator of each rate divides \(g\) and hence \(p\). These observations prove necessity in (2) for \(p\ge8\); the smaller cases are given by the prime-grade theorem.

## An affine family for every whole-order subset

For any prime \(\ell\), choose \(a\in B\subseteq\{1,\ldots,a\}\) and let \(p=\ell^a\). For \(0\le i<p\) write \(i=\sum_{t=0}^{a-1}x_t\ell^t\), \(0\le x_t<\ell\). Put
\[
 L=pn,\qquad u_i=in+r_i,\qquad
               r_i=\sum_{t+1\in B}\mathbf1_{x_t=0}.
\]
These are valid increasing odd dates for large \(n\). With \(Y=2^n/3\), the carry divided by \(3^{p-1}\) factors as
\[
        \sum_i 2^{r_i}Y^i
       =\prod_{t=0}^{a-1}\sum_{x=0}^{\ell-1}
                   2^{\mathbf1_{t+1\in B,\ x=0}}Y^{x\ell^t}.          \tag{3}
\]
At a root of unity of order \(\ell^b\), \(b\ge1\), factors with \(t\ge b\) are positive. When \(t<b-1\), the minimal polynomial of \(Y^{\ell^t}\) has degree at least \(\varphi(\ell^2)>\ell-1\), so the displayed polynomial of degree \(\ell-1\) cannot vanish there. At \(t=b-1\) the factor vanishes exactly when \(b\notin B\), since activating that digit adds one to the ordinary geometric sum. The value at one is positive. As both the numerator polynomial and denominator \(Y^p-1\) are fixed at a fixed grade, the residual gcd on integer \(X=2^n\) is bounded outside \(2,3\) by their fixed resultant after removing their polynomial gcd and clearing constants. The residual valuations at two and three are bounded as in the prime-grade theorem. The resulting rate is precisely (1).

Primitivity follows from the nonzero Fourier coefficient at a primitive \(p\)-th root, because \(a\in B\). A proper rotational symmetry of the native parity word would permute odd dates by a nontrivial shift in rank. It would preserve the gaps \(n+r_{i+1}-r_i\) with indices cyclic, making \(r_{i+s}-r_i\) constant and then zero by summation. A periodic coefficient vector \((2^{r_i})\) with such a shift has zero Fourier coefficient at every primitive root, a contradiction. For binary \(p\), the Euler values \(\varphi(2^b)=2^{b-1}\) show that (3) attains every integer numerator from \(p/2+1\) through \(p\).

## The extra binary rate one half

At grade eight let \(L=8n+4\) and choose the odd dates \(c_i n+b_i\) with successive pairs
\[
             (0,0),(0,1),(1,2),(2,3),(3,1),(4,3),(6,3),(7,3).
\]
For large \(n\) these are increasing and have a unique cyclic gap of length one, so they are primitive. Writing \(X=2^n\), their carry is exactly
\[
       (2X^2+9)(2X^2+6X+9)(2X^3-18X+45).
\]
The first two factors divide \(16X^8-3^8\). The resultant of the last factor with its residual denominator \((2X^2-9)(2X^2-6X+9)\) is \(21520080\). The denominator rate is \(4/8\).

For every \(p=8r\), \(r\ge2\), the following construction attains the same rate, in particular at every larger binary prime power. Start with the three grade-two words whose odd dates are \((0,1),(2,3),(0,5)\) on a common length-six interval. Their carries are \(5,20,35\). Appending identical odd dates \(6,7,\ldots,r+3\) if \(r>2\) leaves an arithmetic progression of grade-\(r\) carries \(C-t,C,C+t\), with \(t>0\). Let \(L=8n+4\). At position \(in+\lfloor i/2\rfloor\), \(0\le i<8\), place the word of carry \(C+t d_i\), where
\[
                          (d_i)=(1,1,0,-1,-1,-1,0,1).
\]
All other dates are even. The groups are disjoint for large \(n\). At a denominator root \(X=3^r\zeta_8^j/\sqrt2\), the carry divided by \(3^{7r}\) is
\[
       \sum_{i=0}^7 \zeta_8^{ij}\,
              2^{\lfloor i/2\rfloor-i/2}(C+t d_i).
\]
The constant term in parentheses gives a two-periodic coefficient vector with nonzero Fourier values exactly at \(j=0,4\). The vector multiplying \(t\) is precisely \(\cos(\pi i/4)\), with nonzero Fourier values exactly at \(j=1,7\). The surviving denominator roots are therefore exactly four of the eight. The fixed resultant after polynomial cancellation again gives rate \(1/2\).

For large \(n\) there are exactly eight cyclic gaps of length growing with \(n\), separating these eight groups. Any literal repetition factor of the whole native word must divide both eight and \(8n+4\), so a nontrivial repetition would in particular give a period \(L/2\). That shift carries nominal group \(i\) to nominal group \(i+4\), since their starting positions differ by precisely \(4n+2\), and it carries the local word unchanged. Groups zero and four have different carries and hence different words, precluding that period. These primitive words realize positive rational cycles by the unique physical fixed point of each parity word once \(2^L>3^p\). This completes (1) and (2).
