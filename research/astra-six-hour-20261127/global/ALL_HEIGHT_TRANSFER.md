# One all-height date and positive pullbacks at an ordinary minimum

For a positive odd state \(x\) write
\[
 Q(x)=\sup_{p,q\ge1,\ 3\nmid q}
       \frac{v_3(qx+p)}{\log(2\max(p,q))},
 \qquad
 \Lambda(x)=\log(x+1),\qquad g(x)=\log(3+\Lambda(x)).
\]
The rational pairs can be required coprime. Dividing out their gcd removes no factor of three if \(3\nmid q\), and can only decrease the denominator of the quotient.

## A common date for the whole positive rational family

There are absolute constants \(C,C_1\) such that every ordinary positive odd \(n\) has a date \(j\le C_1\Lambda(n)\) satisfying
\[
            Q(U^j n)\le C\sqrt{\Lambda(U^j n)\,g(U^j n)}.                 \tag{1}
\]
The cited fixed-height theorem gives, for each positive integer \(H\), an actual date \(j\le \lceil\log_2(3(n+1))\rceil\) at which every height at most \(H\) has valuation at most \(C_0\log(2H)g(n)\). Choose one \(H\) with \(\log(2H)\) comparable to \(\max(1,\sqrt{\Lambda(n)/g(n)})\). At the resulting \(x=U^j n\), heights \(h\le H\) have normalized score at most \(C_0\log(2H)g(n)/\log2\). For \(h>H\), positivity implies \(3^{v_3(qx+p)}\le h(x+1)\). Also \(x+1\le(n+1)(3/2)^j\), hence \(\Lambda(x)\ll\Lambda(n)\). Together these give the bound \(Q(x)\ll\sqrt{\Lambda(n)g(n)}\) on all heights at the same date. To replace the right side by its value in (1), accept this date if \(\Lambda(x)\ge\Lambda(n)/2\). Otherwise restart at \(x\). Each unsuccessful restart at least halves the initial logarithmic height. It is always at least \(\log2\), so the procedure terminates. The delays add to \(O(\Lambda(n))\). [Fixed-height pointwise clock and local two-logarithm input](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/pointwise/HEIGHT_FREE_ANCHOR_CLOCK.md)

## Positive pullbacks on real-minimum windows

Suppose \(x_t=U^t x_0,\ 0\le t\le d\), are on a positive simple orbit with the known uniform reciprocal-product bound \(C_2\), and \(x_0\le x_t\) throughout. Put \(E_t=\sum_{j<t}v_2(3x_j+1)\). Then \(2^{E_t}/3^t\le C_2\), since it equals \((x_0/x_t)\prod_{j<t}(1+1/(3x_j))\). If \(p/q>0\) in lowest terms, \(3\nmid q\), and \(v=v_3(qx_d+p)\ge d\), define
\[
 t_0=\frac{2^{E_d}}{3^d}\frac{p}{q}
                       +\sum_{j<d}\frac{2^{E_j}}{3^{j+1}}.
\]
The actual word identity gives \(x_0+t_0=2^{E_d}3^{-d}(x_d+p/q)\). Hence \(q t_0\) is an integer. Indeed its denominator before cancellation divides \(3^d\), while the identity and \(v\ge d\) give nonnegative ternary valuation. It is positive and at most \(C_2(p+dq)\). Thus the reduced positive anchor at the initial minimum has height at most \(C_3(d+1)\max(p,q)\), denominator dividing \(q\), and its displacement at \(x_0\) has valuation \(v-d\). This yields, for example,
\[
 v_3(qx_d+p)\le d+Q(x_0)
             \log\!\bigl(2C_3(d+1)\max(p,q)\bigr).                       \tag{2}
\]
The inequality also holds when \(v<d\). For bounded \(d\), a clean all-height test propagates forward through such a minimum window with a constant depending on \(d\). The terminal relative loss in (2) depends on the elapsed clock. [Simple-orbit reciprocal bound as used in the component correction](../escape/GRADED_CORRECTION_SETS.md)

Equation (1) is pointwise and concerns a single date. The [all-height ordinary census](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/pointwise/ALL_HEIGHT_ORDINARY_CENSUS.md) has the sharper typical scale \(g(x)\). The [physical-height block result](HEIGHT_SHADOWS.md) gives a different pointwise bound on consecutive dates. These estimates give no identity forcing the positive trace loss to exhaust its scale budget.
