# The whole-period rounding bias and the size of the periodic set

Let \(F_K\) be the least dyadic multiple of an integer in \([K,2K)\) above or equal to three times its input, and let \(\eta_K\) be its rotation clock in base-two turns per step. Put \(\gamma=\log_2 3\), \(C=1/(6(\ln2)^2)\), and let \(P_K\) count all fundamental grid representatives on periodic orbits. In particular \(P_K\) is at least the reduced denominator of \(\eta_K\). For \(0\le\rho\le1\), define
\[
 \mathcal P(t)=\int_0^1\ln\left(1+e^{t2^{-v}}+e^{2t2^{-v}}\right)\,dv,
 \qquad U(\rho)=\frac{1}{3\ln2}\inf_{t>0}
                       \frac{\mathcal P(t)-\rho\ln3}{t}.
\]
For any sequence \(K\to\infty\) with \(\liminf \ln P_K/\ln K\ge\rho\), every accumulation point \(z\) of the scaled rounding bias satisfies
\[
                      2C-U(\rho)\le z\le U(\rho),
              \qquad z=\lim K(\eta_K-\gamma).                         \tag{1}
\]
In particular **the predicted coefficient \(C\) holds on every full-exponent sequence \(P_K=K^{1-o(1)}\)**. The same applies if the single reduced period has full exponent. Unconditionally \(\rho=1/5.116201\) is admissible and \(U(\rho)<2C\). For example, with \(h_*=(\ln3)/5.116201\) and \(J=\ln(1+e^{-2}+e^{-4})\), all accumulation points lie in
\[
             [\,(h_*-J)/(12\ln2),\ 2C-(h_*-J)/(12\ln2)\,].
                                                                         \tag{2}
\]
The variational interval is sharper. The unrestricted upper bound \(C\) on sparse periodic sets remains open.

The exact grid and the coefficient question, including both extreme rounding biases on actual segments through the information horizon, are in [PR215, DIGITAL_ROTATION at 5845a20](https://github.com/GettysburgResearch/collatz/blob/5845a208956bce43b80cf6b4adbadb849d35c15d/research/astra-nine-hour-20261128/cycles/phase8/DIGITAL_ROTATION.md). The earlier [PR213 pooled-rank and digit proof](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/PERIODIC_GRID_DENSITY.md) uses the same grid with odd cutoff \(2K-1\), and its [component-lifetime paper](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/PLATEAU_COMPONENTS.md) already uses rotation calendars and logarithmic-scale entropy to bound component persistence. Here we obtain a full-period coefficient interval from the pooled count and identify the exact ternary pressure for the forward dyadic ceiling alphabets.

## Spatial calendar and whole-period information

Order all \(P=P_K\) periodic representatives \(x_0<\cdots<x_{P-1}\) in \([K,2K)\), and extend with \(x_{i+P}=2x_i\) for every integer \(i\). The increasing lift permutes the pooled points bijectively and preserves strict order on them. Thus it is an integer translation on these bi-infinite ranks. Its displacement divided by \(P\) is the common clock \(\eta=\eta_K\). At fundamental rank \(i\) write \(v=i/P\). Its next normalized rank has coordinate \(v'=\{v+\eta\}\), its winding is \(b=\lfloor v+\eta\rfloor\), and its actual forward edge is
\[
                  2^b x'=3x+d,\qquad 0\le d<2^b .
\]
The latter ceiling bound follows directly in the target octave. If an upper rounded endpoint wraps to the next octave, the new winding only increases the displayed bound. For large \(K\), \(b\in\{1,2\}\). Indeed each edge has raw relative error \(O(1/K)\) by the dyadic grid spacing, hence \(\eta=\gamma+O(1/K)\) on multiplying the cycle edges (and \(\eta>\gamma\) by irrationality).

The physical angles \(\log_2(x/K)\) of these pooled vertices converge in law to uniform measure: every subsequential limit is invariant under translation by \(\gamma\) on the circle since every actual angle increment is \(\gamma+O(1/K)\), and irrational rotation has the unique uniform invariant law. Uniform convergence of the distribution functions to the continuous uniform distribution then gives
\[
                  \max_{0\le i<P}|\log_2(x_i/K)-i/P|=o(1).
\]
In particular \(P\to\infty\), also immediate from the reduced period. Uniform Taylor expansion and the actual permuted lifts give
\[
              3\ln2\,K(\eta-\gamma)
                   =P^{-1}\sum_i d_i 2^{-i/P}+o(1).                     \tag{3}
\]

Set \(n=\lceil\log_3(2K)\rceil\) and take a uniform starting rank. The cumulative actual winding \(B_n=\lfloor v+n\eta\rfloor\) satisfies \(2^{B_n}\ge3^n/2\ge K\). Two starts with the same \(n\)-step winding and digit strings obey
\[
                    2^{B_n}(x_n-x'_n)=3^n(x_0-x'_0).
\]
Their integer starting representatives differ by less than \(K\), so they coincide. This injects the **whole** pooled set into its observed calendar-and-digit words.

Partition the rank circle into \(m\) equal bins for any fixed positive integer \(m\), and also at the cut determining \(b\). The common refinement of all first \(n\) pullbacks of these cuts by rotation by \(\eta\) has at most \((m+2)n\) cells, with half-open endpoints. In a cell the whole winding and bin calendars are fixed. Put \(w_m(v)=2^{-\lfloor mv\rfloor/m}\) for fundamental \(0\le v<1\). Given a calendar cell, the entropy of its digit word is at most the sum of the one-date conditional entropies. For an alphabet \(0,\ldots,D-1\), entropy of any law with mean \(\bar d\) is at most \(\ln\sum_{j<D}e^{t wj}-tw\bar d\), by the nonnegativity of relative entropy. The injectivity, the cell count and stationarity of the uniform rank law now give, for each real \(t\),
\[
 \frac{\ln P-\ln((m+2)n)}{n}
       \le \frac1P\sum_{i=0}^{P-1}
            \left[\ln\sum_{j<2^{b_i}}e^{t w_m(i/P)j}
                      -t w_m(i/P)d_i\right].                           \tag{4}
\]
This estimate uses the order of the actual periodic pool only. An isolated input segment can exhaust its source digits at the same horizon.

Since \(n\sim(\ln K)/\ln3\), the left side has lower limit at least \(\rho\ln3\). First let \(K\to\infty\) on a subsequence realizing (3), then \(m\to\infty\). The winding cut converges to \(b(v)=\lfloor v+\gamma\rfloor\), and the fundamental ranks form a uniform mesh. The uniform error from replacing \(w_m\) by \(w(v)=2^{-v}\) tends to zero, including in the weighted digit term. Thus
\[
          \rho\ln3+3t\ln2\, z
               \le \int_0^1 \ln\sum_{j<2^{b(v)}}e^{tw(v)j}\,dv .       \tag{5}
\]

## The same pressure as a uniform ternary alphabet

For \(v'=\{v+\gamma\}\) one has \(2^{b(v)}w(v)=3w(v')\). For nonzero real \(t\) use the geometric sum and \(\ln|e^s-1|\) at numerator and denominator. Translation of Haar measure from \(v\) to \(v'\) turns the integral in (5) into
\[
 \int_0^1\ln\left|\frac{e^{3tw(v)}-1}{e^{tw(v)}-1}\right|dv
             =\mathcal P(t).
\]
The value at zero is \(\ln3\). With \(D=\int_0^1 w(v)\,dv=1/(2\ln2)\), the identity \(\mathcal P(t)=2tD+\mathcal P(-t)\) proves the symmetric interval (1) from both signs of (5). At \(\rho=1\), take \(t\to0\) from both signs, using \(\mathcal P'(0)=D\), to get \(z=D/(3\ln2)=C\).

Write \(a/q=\eta_K\) in lowest terms. The published linear-form bound of [Bondareva, Luchin and Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) gives \(a\ln2-q\ln3\gg q^{-4.116201}\) since \(a\asymp q\). Combined with \(\eta_K-\gamma=O(1/K)\) this gives \(P_K\ge q\gg K^{1/5.116201}\). At \(t=4\), \(\mathcal P(4)\le8D+J\) by \(w\ge1/2\). Substitution gives (2), where \(J<h_*\). All biases and all estimates here concern complete integer orbits of the homogeneous grid. PR215's inequality \(A/p\le\eta_{2m}\) for any ordinary cycle with minimum \(m\) consequently gives \(\limsup m p^{-1}\sum_y 1/y\le(3\ln2/2)U(1/5.116201)\) on any unbounded sequence of distinct cycles by the uniform true-edge Taylor expansion. Their existence is not needed for the grid result.

[Exact finite calendar, word-injection and pressure-product controls](check_grid_period_pressure.py)
