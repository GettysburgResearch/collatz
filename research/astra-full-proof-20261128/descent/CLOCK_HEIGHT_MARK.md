# A clock and height mark at the last formal denominator

The source law matters in this comparison. Fix \(v>0\), write
\(N=2^k,\ g=k^{3/5},\ \lambda=\log_2 3,\ r_*=k/(2-\lambda)\), and put
\(R=\lfloor r_*+vg\rfloor\). The ordinary law chooses an integer
\(1\le n\le N\) uniformly. The rational law chooses the numerator of
\(x=u/3^R\) uniformly through \(N3^R\). The shortcut takes its branches
on \(\mathbb Z[1/3]\) by reduction modulo two. In either law let
\(\sigma_j\) be the date just after the \(j\)-th odd departure and let
\(y_j=T^{\sigma_j}x\). Every positive source has every finite such date.
The rational law has a positive integer endpoint at date \(\sigma_R\).

Define the real correction in bits by
\[
 C_R(x)=\sum_{j=1}^R\log_2\frac{2y_j}{2y_j-1}
       =\sigma_R-\lambda R+\log_2(y_R/x).                         \tag{1}
\]
Indeed the term at an odd departure from \(z_j\) is
\(\log_2(1+1/(3z_j))\). Multiplying the actual trajectory gives (1).
The clock-weighted entrance operator with \(\zeta=2^{i\tau}\) obeys
\[
 K_\zeta[x^{-i\tau}h](y)=3^{i\tau}y^{-i\tau}
 \left(\frac{2y}{2y-1}\right)^{i\tau}Kh(y),\qquad y>1/2,          \tag{2}
\]
where \(K_\zeta h=\tfrac13\sum_{e\ge0}\zeta^{e+1}h(2^e(2y-1)/3)\)
and \(K=K_1\). Each summand proves (2) separately. Identity (2) keeps
the height phase that a bound on the bare clock transform would lose.

**Joint rational benchmark, written.** Put \(L_1=2-\lambda=\log_2(4/3)\).
Under the rational law,
\[
 C_R/g\ \longrightarrow\ vL_1\qquad\hbox{in probability}.        \tag{3}
\]
This uses the written rational entrance clock and pointwise entrance
tail in the other sprint lanes. The clock gives
\(\sigma_R=2R+O_{\Pr}(\sqrt{k}\log^2 k)\). The tail gives
\(\log_2 y_R=o_{\Pr}(g)\). Indeed in the pointwise two-term bound with
\(\beta>1,\ u\asymp g/k\), summing over \(y\ge2^{\epsilon g}\) costs
\(O(k^L2^{-(\beta-1)\epsilon g}+u^{-1}e^{-c g^2/k})=o(1)\).
The ordinary uniform numerator also gives \(\log_2 x=k+o_{\Pr}(g)\).
Substitution in (1) proves (3). For each bounded continuous \(f\),
\[
 \sup_{|H|\le1}\left|\mathbb E_{\rm rat}H(y_R)
 [f(C_R/g)-f(vL_1)]\right|\longrightarrow0.                       \tag{4}
\]
This is bounded convergence in probability and permits *arbitrary*
endpoint marks. In particular \(\mathbb E_{\rm rat}2^{-C_R}\to0\).
[Rational entrance clock](../parity/RATIONAL_ENTRANCE_CLOCK.md) ·
[Integer entrance law and two-term tail](../mass/RATIONAL_ENTRANCE_KERNEL.md)

**Ordinary comparison, written.** Let \(\tau_1\) be the first physical
date at one (possibly infinite). Put \(L_3=\log_2(10/9)<L_1\).
Uniformly outside an ordinary source fraction \(o(1)\),
\[
 C_R/g\le vL_1+o(1),\qquad
 \tau_1>\sigma_R\ \Longrightarrow\ C_R/g\le vL_3+o(1).             \tag{5}
\]
To prove this, retain \(n\ge 2^k k^{-A}\), and use the native crossing
from [the first-moment note](FIRST_MOMENT.md) at the strict threshold
\(2^{-d} n\), with \(d=k-B-1\) and \(B=K_A\log_2 k+O(1)\) large enough
that the threshold is at least \(k^2\). The first such date \(t\) is
\(2r_*+O_A(\sqrt{k\log k})\) and \(p=Q_t=r_*+O_A(\sqrt{k\log k})\).
Every preceding odd input is at least \(k^2\), so its total cost
through the crossing is \(O_A(1/k)\). The remaining \(R-p\) odd
departures number \(vg+O_A(\sqrt{k\log k})\). Each costs at most
\(L_1\). If the path has yet to reach one every such odd input is at
least three, hence costs at most \(L_3\). This proves (5).
[Weaver, Theorem 1 and Section 4, version 2](https://rstation.ai/problems/collatz/papers/191/v2)

For fixed \(h>0\) the one-sided separation is consequently
\[
 \mathbb E_{\rm ord}2^{-h C_R/g}\ge 2^{-hvL_1}+
 (2^{-hvL_3}-2^{-hvL_1})\Pr_{\rm ord}(\tau_1>\sigma_R)-o(1).       \tag{6}
\]
The rational expectation tends to the first constant in (6). A
nonpositive liminf of the ordinary-minus-rational difference would
therefore exclude both escaping trajectories and additional cycles by
fixed-target positive predecessor density. No such transfer is known.
[Scope of the predecessor result](../../external/mazur-2026/README.md)

At fixed exponent one, \(S_R=2^{-C_R}\) retains escaping trajectories
uniformly and tends to zero on every bounded positive trajectory.
Indeed a bounded trajectory visits a periodic odd state infinitely
many times. An escaping trajectory has no repeated state, and the
published simple-orbit reciprocal estimate bounds its entire additive
correction uniformly. Thus the fixed exponent offers an escape-only
comparison against the vanishing rational expectation in (3). Its
*actual signed denominator ladder* has a uniform small-interval bound.
[Simple-path estimate and primary references](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase4/HARMONIC_SOURCE_PHASE.md) · [Small-interval proof](SURVIVAL_WINDOWS.md)
