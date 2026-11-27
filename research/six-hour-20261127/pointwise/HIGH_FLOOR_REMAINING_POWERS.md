# The remaining powers of the high-floor principal-source law

Use the same \(F_{H,n}\), \(Z_n(z)\) and \(R_H(z)\) as in the positive-order high-floor theorem (frozen SHA-256 5aa2ded620dc9dc513caad4a804c42efa625baef102154de76196276fdf49eb1). The exact formula on the whole real power axis is
\[
 \lim_{n\to\infty}\frac1n\log\mathbb E[\mathbf1_{F_{H,n}} Z_n(z)^p]
       =\max(0,p-1)\log R_H(z)\qquad (p\in\mathbb R).
\]
The new cases \(p\le1\) need only the elementary principal-source first-moment inequality.

Indeed any true principal path satisfies \(x_i\ge3^i m/2^{A_i}\). If some \(x_i\le H\) through date \(n\), with \(H>0\), then
\[
 Z_n(0)=2^{A_n}/m\ge H^{-1}3^i2^{A_n-A_i}\ge H^{-1}2^n,
\]
since every remaining exponent is at least one. Thus
\[
 \Pr(F_{H,n}^c)\le H(n+1)2^{-n},
\]
by \(\mathbb E Z_n(0)\le n+1\). For \(H=0\) the event is empty. The principal terminal \(y\) is the least positive odd integer of its class modulo \(3^n\), hence \(1\le y<2\cdot3^n\). The affine identity gives \(Z_n(z)=(3^n/y)(m+G)/(m+zG)\ge [2\max(1,z)]^{-1}\) for all \(z\ge0\). This includes \(z=0\). For \(0\le p\le1\), the floor and \(\Pr(F_{H,n})\to1\) bound the moment from below, and concavity gives the upper bound \((n+1)^p\). For \(p<0\), the pointwise floor bounds the moment from above. Conditional Jensen gives a lower bound \(\Pr(F_{H,n})^{1-p}(n+1)^p\), using \(\mathbb E[\mathbf1_{F_{H,n}}Z_n(z)]\le n+1\). All three bounds have zero exponential rate.

The high-floor event therefore retains nearly all original geometric-word probability, even though its behavior after multiplication by the high powers of the principal payoff can detect positive cycles. This location estimate refers to finite principal paths sampled from the original word law.

Prepared by the binary-energy reviewer, 27 November 2026 UTC.
