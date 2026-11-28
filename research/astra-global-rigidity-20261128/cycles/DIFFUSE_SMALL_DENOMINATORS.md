# Nearcritical rational cycles can evade every fixed height band and every prescribed native mismatch growth rate

For every prescribed function \(F(p)\to\infty\), there is a sequence of actual primitive positive rational Collatz cycles, of least odd period \(p\to\infty\), satisfying all of the following. Write \(h\) for the shortcut period, \(m,X\) for the real odd minimum and maximum, and \(q\) for the complete common reduced denominator.

* All native exponents are one or two, \(q>1\), \(\log q=o(p)\), and \(0<h-p\log_2 3<p^{-1+o(1)}\).
* The minimum satisfies \(p^{2-o(1)}\le m\le p^{O(1)}\). There is a scale \(b=p^{1-o(1)}=o(p)\) with \(\log(X/m)=\Theta(b)\). For every \(K\ge1\) depending on the example with \(\log K=o(b)\), the proportion of odd states in \([Y,KY]\) tends uniformly to zero over \(Y>0\).
* The longest native matching run, maximized over all proper lags, is \(o(p)\). Nevertheless there is a native rotation of **order five** whose number of Hamming mismatches tends to infinity more slowly than \(F(p)\), in the sense \(m_5/F(p)\to0\).

In particular the qualitative divergence in [the native rotation theorem](NATIVE_ROTATION_SEPARATION.md) for \(\log q=o(p)\) admits no lower growth rate tending to infinity uniformly over that entire asymptotic class. An ordinary-denominator rate would distinguish \(q=1\) from these genuine cycles. The examples also avoid concentration in **any** fixed multiplicative band. They complement [the narrow rational examples](RATIONAL_MATCHING_BARRIER.md), where width itself already separates them from candidate integer cycles.

## Three independent markers in a shaped cell

We use the exact independent-clock construction of PR212, with a different template. Fix distinct primes \(\ell_2,\ell_3>5\) tending to infinity and put \(N=5\ell_2\ell_3\). At the \(j\)-th choice of primes choose a coprime upper convergent \(n/b\) to \(\gamma=\log_2 3\), with \(0<\delta=n-b\gamma<1/b\), so far out that \(b>N^j\) and \(F(Nb)\ge N^2\). These choices are possible by irrationality and the stated limit of \(F\). Put \(u=\lfloor b/\lceil\log_2(b+1)\rceil\rfloor\), so \(u=o(b)\) and \(u=b^{1-o(1)}\).

Use initial native exponents \(e_t=\lfloor(t+1)n/b\rfloor-\lfloor tn/b\rfloor\) for \(0\le t<u\). They are one or two. Every exponent one here is followed by a two, apart from a possible last site: the fractional increase \(n/b-1>1/2\) prevents consecutive ones. The count of ones is \((2-n/b)u+O(1)\). Choose three well-separated pairs \((1,2)\) wholly inside this prefix, away from its endpoints. After the prefix, arrange all remaining exponents one consecutively and then all remaining exponents two consecutively, using \(2b-n\) ones and \(n-b\) twos in the full cell. The large two terminal groups have respective sizes \((2-\gamma)b+o(b)\) and \((\gamma-1)b+o(b)\).

In the shortcut word, a selected pair followed by its next odd cut spells \(1101\). Mark the middle \(10\) in \(110\); swapping it to \(01\) changes exactly the two corresponding native exponents from \((1,2)\) to \((2,1)\). The three marker pairs are separated, so this holds under any combination of swaps. Read \(N\) cells numbered \(j=0,\ldots,N-1\), swapping the first, second or third marker precisely when \(5\mid j\), \(\ell_2\mid j\), or \(\ell_3\mid j\), respectively. The complete word has \(h=Nn\), \(p=Nb\), and positive determinant since \(2^n>3^b\).

For clarity, set \(A=2^n\), \(B=3^b\). The normalized cell recurrence is \(x_{j+1}=(Bx_j+c_j)/A\), with \(c_j=c_*+\sum_{i=1}^3d_i\boldsymbol1_{\ell_i\mid j}\), \(\ell_1=5\). Each \(d_i\) has only prime factors two and three, since disjoint \(10\) swaps move the corresponding odd letter one bit and preserve all later counts. PR212's exact theorem for arbitrary templates therefore produces the true positive rational cycle, with
\[
 q=\frac{A-B}{\gcd(A-B,\sum_jc_j)}
       \prod_{i=1}^3\frac{A^{\ell_i}-B^{\ell_i}}{A-B}>1,
 \qquad \log_2 q\le n\left(1+\sum_i(\ell_i-1)\right)+\log_2 N=o(p).
\]
The last smallness uses \((\ell_2+\ell_3+O(1))/N\to0\). No factor of the displayed cyclotomic product cancels. Any repetition multiplicity divides \(\gcd(h,p)=N\), hence any smaller period is a cell shift, which would have to preserve all three independent prime markers. Thus the shortcut word is primitive, and so is the native word. Also \(N=b^{o(1)}\) and \(0<h-p\gamma=N\delta<N/b=p^{-1+o(1)}\). [PR212, exact cell formulas (2)–(5), including physical realization and primitivity](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md)

## Height distribution and rotation statistics

Let \(S_j(t)\) be the native clock through \(t\) departures of cell \(j\), and write \(G_j(t)=\gamma t-S_j(t)\). On the low prefix \(0\le t\le u\), one has \(|G_j(t)|\le 3\) for large examples, by the mechanical formula and the possible one-clock shift between the two ends of a swapped pair. Following it \(G_j\) increases by \(\beta=\gamma-1>0\) at each remaining one, then decreases by \(\kappa=2-\gamma>0\) at each remaining two, ending at \(-\delta\). Its minimum is bounded below absolutely and its maximum is \(\beta(2-\gamma)b+o(b)\).

Let \(x_{j,t}\) be the actual positive rational odd state at this date, and \(x_{0,0}\) the first cell boundary. The exact positive product on the initial segment gives
\[
 \log_2(x_{j,t}/x_{0,0})=-j\delta+G_j(t)+E_{j,t},
 \qquad 0\le E_{j,t}\le N\delta.
\]
Indeed \(E_{j,t}\) is a partial sum of \(\log_2(1+1/(3x))\); its full lap sum is exactly \(N\delta\). Thus the logarithmic error relative to \(G_j(t)\) tends uniformly to zero. The minimum is comparable to \(x_{0,0}\), all \(Nu\) low prefix departures are within a fixed factor of the minimum, and \(\log_2(X/m)=\beta(2-\gamma)b+o(b)\). Since \(N\delta\to0\), even the minimum tends to infinity. Its \(Nu\) comparable states each contribute \(\gg1/m\) to the gap, proving \(m\gg u/\delta\gg ub=p^{2-o(1)}\). The usual classical two-log lower bound on \(h-p\gamma\) together with the positive lap sum gives \(m\ll p^{O(1)}\). [Bondareva–Luchin–Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

Uniformly for any real log-height interval of width \(w\), a cell contributes at most \(u+O(1+w)\) dates therein: the two straight ramps of \(G_j\) have nonzero fixed slopes and the true log heights are within \(o(1)\) after a common shift. Dividing by \(b\) proves the claimed band estimate. Every true odd numerator \(y=qx\) now has \(\log y\le\log q+O(b+\log p)=o(p)\), since \(b=p/N\) and \(N\to\infty\). At any proper lag a matching run of length \(L\) imposes \(2^L\le |y_i-y_{i+r}|\) on its distinct sources. This bounds every such run by \(o(p)\) uniformly.

Finally rotate by \(r=bN/5\) native dates. This has order five. It advances cells by \(N/5=\ell_2\ell_3\), preserving the two larger-prime markers and moving the residue modulo five by a nonzero value. Exactly \(2N/5\) of the cells differ at the first marker, each at exactly two native exponents. Thus \(m_5=4N/5\to\infty\) while \(m_5/F(p)\le4/(5N)\to0\). This conclusion concerns native Hamming mismatches, independently of the shortcut-word factor complexity.
