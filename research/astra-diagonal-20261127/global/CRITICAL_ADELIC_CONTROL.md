# An integer-valued control at the capacity boundary

**PROPOSED explicit countermodel for a general analytic implication.** Given any \(\theta>0\), choose \(p>1/\theta\), \(\lambda=\log_2 3\) and \(C>p/((\lambda-1)\log 2)\), taking \(p>1\) as well. Define
\[
 A_n=\lfloor\lambda n-p\log_2(1+n/C)\rfloor,\qquad e_n=A_{n+1}-A_n .
\]
The derivative of the expression in the floor lies strictly between one and two, so \(A_0=0\) and every \(e_n\) is one or two. Start at any one positive odd integer \(x_0=a\). Choose \(d_n\) as the residue of \(2^{e_n}-3x_n\) in \([1,2^{e_n+1}-1]\) modulo \(2^{e_n+1}\), and let \(x_{n+1}=(3x_n+d_n)/2^{e_n}\). Induction makes \(d_n\) odd in \(\{1,3,5,7\}\), \(x_{n+1}\) a positive odd integer, and the displayed valuation exact at every step.

The integer series
\[
 G(z)=\sum_{n\ge0}d_n 2^{A_n}z^n
\]
has real radius \(1/3\), binary radius \(3\), and radius one at every other prime. At the latter places, bounded valuations of \(d_n\) suffice. The capacity product of the corresponding centered disks equals one. Even at the Archimedean radius its Taylor coefficients after rescaling belong to \(\ell^\theta\cap\ell^1\), because \(2^{A_n}3^{-n}\asymp (1+n/C)^{-p}\). The identity
\[
 3^{-n}2^{A_n}x_n=a+\tfrac13\sum_{i<n}d_i2^{A_i}3^{-i}
\]
gives \(G(1/3)=-3a\) at two, a strictly positive value over the reals, and \(x_n\asymp(1+n/C)^p\) on this one actual integer process. The series is nonrational. A rational function of finite radius has a pole on its radius circle, whereas this series is uniformly bounded on the closed radius disk by absolute summability.

This example retains the exact disk capacities, arbitrarily small positive boundary summability exponent, a rational binary evaluation at the same point, bounded odd multipliers supported on three primes, bounded positive exact division clocks and a fixed positive ordinary seed. Its additive term \(d_n\) is selected at each step. For the actual Collatz clock all these multipliers must equal one. Any critical rationality argument must use additional information beyond the retained hypotheses. The strict criterion and the ordinary clock calculation are in the [prior adelic note](../../astra-six-hour-20261127/root/ADELIC_CLOCK.md). [Bost and Chambert-Loir, Theorem 7.9 and Example 7.10](https://arxiv.org/abs/math/0702593).
