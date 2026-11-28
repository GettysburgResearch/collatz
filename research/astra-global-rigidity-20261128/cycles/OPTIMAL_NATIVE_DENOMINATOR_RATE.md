# The optimal order of the complete-denominator exponent is inverse native mismatch count

Write \(p\) for the least odd period of a primitive positive rational cycle, \(q\) for its complete reduced denominator, \(P\) for the number of native exponents equal to one (called rises below), \(m(r)\) for the number of mismatched native division exponents at a proper circular lag \(r\), and \(\gamma=\log_2 3,\ \beta=\gamma-1,\ \kappa=2-\gamma\). For each fixed integer \(s\ge1\), uniformly over cycles with \(\min_r m(r)\le s\),
\[
           \gamma p\le 2\beta P+2s\log_2q+o_s(p)\qquad(p\to\infty).    \tag{1}
\]
In particular \(\liminf (\log_2 q)/p\ge\kappa/(2s)\) on every such family. The coefficient is explicit and the threshold for a strictly smaller coefficient remains ineffective.

To state the converse, let \(E_s\) be the infimum, over all such families with \(p\to\infty\), of \(\liminf(\log_2q)/p\), taking the empty infimum as infinity. For all sufficiently large \(s\) there are actual positive rational primitive families with this cutoff and \(\limsup(\log_2q)/p\ll 1/s\) with an absolute implied constant. Consequently
\[
                              E_s=\Theta(1/s).                         \tag{2}
\]
This concerns a fixed mismatch cutoff followed by increasing period, and then the dependence on the cutoff. It gives no effective period-dependent diverging lower function for the ordinary cycle mismatches. It sharpens the coefficient in [the first explicit corollary](NATIVE_ROTATION_COEFFICIENT.md) and uses the fixed-place construction of [native rotation separation](NATIVE_ROTATION_SEPARATION.md).

## Lower bound by repeated comparisons at a proper phase offset

Suppose (1) fails with a fixed positive linear deficit along some sequence. Then \(\log_2q=O_s(p)\). Cut at the real odd minimum and use integer numerators \(y_i\). The classical two-log estimate used in native rotation separation gives \(\log_2(y_0+q)\le\log_2q+O(\log p)\). In particular every numerator in the lap has logarithm \(O_s(p)\) by forward growth. Choose a proper lag \(r\) attaining the cutoff. On any matching run the common binary-clock power divides the nonzero integer difference of the two sources; it is at most \(2^{O_s(p)}\). At each mismatched departure \(a_i\le\log_2(3y_i+q)=O_s(p)\). The full lap splits at the cut into at most \(s+1\) matching runs and at most \(s\) individual mismatched departures. Its halving total is therefore \(O_s(p)\), including when a comparison wraps around the native lap.

Fix an arbitrary positive integer \(K\), put \(d=Kp+r\), and compare native dates \(t\) and \(t+d\) through \(0\le t<d\), in the actual path continued for \(2d\) departures. Every compared pair is distinct since \(r\) is proper; other repetitions are permitted. There are at most \((K+1)s\) mismatches and at most \(k_0=(K+1)s+1\) matching runs. Their union in the first copy has normalized length tending to one. The total binary clock is \(O_{K,s}(p)\), hence \(O_{K,s}(d)\), by the preceding full-lap bound. All logarithmic heights needed in Sections 1–4 of native rotation separation are \(O_{K,s}(d)\).

We record exactly what changes in that proof. The paired-source inequalities suffice for its nonzero protected differences. The enlarged-run circle cover and movable terminal dates yield \(k'\le k_0\) representatives with summed true ternary gains divided by \(d\) arbitrarily close to one from below. Their protected differences and endpoints are independent over the alignment field as before, so the same fixed translated boxes and Subspace Theorem apply. At a nonrise, \(y_{i+1}\le\max(y_i,q)\) because \(2^{a_i}\ge4\). At a rise, \(y_{i+1}+q=(3/2)(y_i+q)\). Thus \(\max(y_t+q,2q)\) increases by a factor of at most \(3/2\) at rises and never increases at the other steps. Let \(P_{2d}\) count all rises through the window. As in [the selected run estimate](NATIVE_MATCHING_MASS.md), for chronological dates \(a\le i<b\),
\[
              B_i/B_b\le(3/2)^{P[a,b)},\qquad B_i=2^{S_i}3^{-i}.
\]
The exact positive sum \(H_b-H_a=(q/3)\sum_{a\le i<b}B_i\) now gives the following upper bound for the base-two logarithm of an entire chronological box row before the ternary replacements:
\[
       \beta P_{2d}+\log_2(2(y_0+q))+(2k'-1)\log_2 q+O_{K,s}(\log p).
\]
It remains valid for \(q\) exponential in \(p\). Section 4's contradiction applies whenever this charge is less than \(\gamma d\) by a fixed positive multiple of \(d\): choose both fixed coverage losses smaller than that margin before the Subspace Theorem. It follows that
\[
      \gamma d\le\beta P_{2d}+2k_0\log_2 q+o_{K,s}(p),
\]
where the minimum bound absorbed the initial numerator charge. Since \(d\ge Kp\) and \(P_{2d}\le(2K+2)P\),
\[
   \gamma p\le (2+2/K)\beta P+
            \bigl(2s+(2s+2)/K\bigr)\log_2 q+o_{K,s}(p).
\]
First take a limit superior of the normalized alleged deficit at fixed \(K\). The two terms with \(1/K\) have bounded normalized coefficients on the violating family. Then send \(K\to\infty\). This proves (1) with no fixed-order restriction on the physical lag. As \(P\le p\), it proves the lower side of (2).

## Upper side from two independent prime markers

For a fixed large \(s\), choose a prime \(\ell\) with \(\lfloor s/8\rfloor<\ell\le 2\lfloor s/8\rfloor\le s/4\), by Bertrand's postulate. Choose any prime \(L>\ell^2\) and fix \(N=\ell L\). In particular \(\ell,L\ge5\) for large \(s\). Now take coprime upper convergents \(n/b\) to \(\gamma\) with \(b\to\infty\), keeping these primes fixed. A mechanical native cell of \(b\) exponents one or two and clock \(n\) has arbitrarily many well-separated \((1,2)\) pairs. Select two wholly in the interior. In the shortcut representation they give disjoint marks \(110\to101\); the initial letter and the odd cut after each pattern stay fixed, so such a swap changes just those two native exponents, from \((1,2)\) to \((2,1)\). In cell \(j\) make the two swaps according as \(\ell\mid j\) and \(L\mid j\). Use \(N\) cells. This is the arbitrary-template construction of PR212, applied with two markers.

The complete denominator satisfies, with \(A=2^n\), \(B=3^b\), cell carries \(c_j\),
\[
 q=\frac{A-B}{\gcd(A-B,\sum_j c_j)}
        \frac{A^{\ell}-B^{\ell}}{A-B}\frac{A^L-B^L}{A-B}
      \le N\,2^{n(\ell+L-1)}.
\]
In particular it exceeds one. The exact formula and the fact that the positive affine fixed point realizes every prescribed shortcut phase are proved in the primary source. Any repetition multiplicity divides \(\gcd(Nn,Nb)=N\); hence a smaller period would be a whole-cell shift, necessarily preserving both prime indicators. Only the full shift does so. Thus the cycle is primitive with least odd period \(p=Nb\).

The lag \(r=b\ell\) advances \(\ell\) cells, preserving the first marker and changing the second on exactly \(2N/L=2\ell\) cells. Each changed pattern contributes two native mismatches, hence \(m(r)=4\ell\le s\). Along this fixed-prime family
\[
       \limsup_{b\to\infty}\frac{\log_2 q}{p}
             \le \gamma\frac{\ell+L-1}{\ell L}
             \le \gamma(1/\ell+1/L)\ll 1/s.
\]
The implied constant is independent of the original cutoff. This proves (2). The construction of the positive rational orbits and their full cyclotomic denominators is due to the following source; the two-prime parameter choice and its comparison with (1) give the matching inverse-cutoff order here. [PR212, independent clocks, exact full denominator and primitivity](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md)
