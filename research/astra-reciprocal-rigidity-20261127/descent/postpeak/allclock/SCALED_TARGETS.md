# Protection against all visitor clocks on a growing range of scaled targets

**Written theorem.** Let \(s=284051/829440>1/3\) and \(s_0=1041139/4147200>1/4\). In every shell \(X\le n<2X\), as \(X\to\infty\), at least \((s-o(1))X\) positive integers have the following property. For **every** pair \(j,\delta\ge0\) with
\[
                    2^\delta(3/2)^j\le X^{1/50},
\]
if \(Y=2^\delta(3/2)^j(n+1)-1\) is an integer, then no positive \(m<n\) reaches \(Y\) at any ordinary shortcut clock. At least \((s_0-o(1))X\) such integers are multiples of three. The conclusion includes every pair \(j,\delta\le (\log_2 X)/80\) simultaneously, since \(\log_2 3<8/5\).

The all-clock claim differs from the pointwise finite-precision selector, which excludes visitors only up to a stated odd budget. Here a vanishing number of exceptional shell sources is removed and the conclusion concerns a growing set of actual integer targets. Some of these targets are genuine initial ramp states and others are scaled affine sites. No conclusion about arbitrary later states or Collatz convergence follows.

The inputs are this sprint's common finite selector bound and Weaver's long-arrival estimate, with a uniform finite-size version derived below from his existing proof. Weaver 178/v1 §7 already proves stronger all-clock conditional proportions on the pure odd ascent. The new application handles a common set of ordinary integers for a growing two-parameter range of additional scales. [Common ternary protection theorem](../../../root/phase5/COMMON_PROTECTION.md) · [Weaver 177/v1 §§7–8, especially (3)](https://rstation.ai/problems/collatz/papers/177/v1) · [Weaver 178/v1 §§2,7](https://rstation.ai/problems/collatz/papers/178/v1)

## A finite uniform bound on long minimum-source arrivals

Write \(T\) for the positive shortcut map and \(I_Y=[1,\lfloor Y\rfloor]\). Let \(E_J(Y)\) be the \(z\in I_Y\) for which some \(b\in I_Y\) first or later reaches \(z\) at clock \(d>J\) along a path all of whose states are at least \(b\). We use
\[
          |E_J(Y)|\ll Y\,2^{-J/25}+Y^{49/50}
          \quad(1\le J\le k=\lfloor\log_2Y\rfloor).
\]
Changing the fixed factor \(2\) in Weaver's definition only changes absolute constants. This form follows from the orbit-union and entropy arguments already in his §§7–8; we give the details to keep both growing parameters explicit.

First, for the union \(\mathcal U\) of \(N_0\) positive forward orbits,
\[
       |\mathcal U\cap I_Y|\le |T^k(I_Y)|+2kN_0 .
\]
Indeed, add the orbits in order up to their first intersections with previous ones. Each new portion is a disjoint simple path, or consists of a simple path followed by its previously unseen cycle. Remove at most \(k\) final states of a finite path and at most \(k\) final preperiod states leading to a new cycle. On each remaining path or cycle \(T^k\) is injective and has images in its own portion. This proves the bound even if an orbit is unbounded or periodic.

We have \(|T^k(I_Y)|\ll Y^{49/50}\). Words with at least \(3k/5\) odd departures give \(O(2^{H_2(3/5)k})\) choices by the binomial entropy bound. Each is one dyadic residue class modulo \(2^k\), with at most two representatives in \(I_Y\). For the other words the endpoint is at most
\[
       3^{3k/5}\,Y/2^k+(3/2)^k .
\]
The affine offset is bounded by \((3/2)^k-1\) by replacing each even branch by the odd branch when bounding the all-odd maximum from zero. Now \(H_2(3/5)<49/50\), \(\log_2 3<8/5\), and \(2^k>Y/2\), proving the image bound.

Sources \(b\le\sqrt{Y}\) therefore contribute \(O(Y^{49/50}+k\sqrt Y)=O(Y^{49/50})\) target integers by the orbit-union estimate. For \(b>\sqrt Y\), a length-\(i\) prefix staying above \(b\), with \(i\le k\) and \(u_i\) odd departures, satisfies
\[
       1\le T^i(b)/b
          \le 3^{u_i}2^{-i}\exp(i/(3\sqrt Y)).
\]
Thus \(u_i\ge i\log_3 2-1\) for all large \(Y\). Since \(\log_3 2>5/8\) by \(3^5<2^8\), for all sufficiently large \(i\) this implies \(u_i\ge5i/8\). There are \(O(2^{24i/25})\) candidate words by \(H_2(5/8)<24/25\), with small \(i\) absorbed in the constant. Each word selects at most \(1+Y/2^i\le 2Y/2^i\) sources up to \(Y\). For \(J<d<k\) sum over first-arrival clocks (or over all allowed clocks), obtaining \(O(Y2^{-J/25})\) pairs. For \(d\ge k\) there are only \(O(Y^{24/25})\) potentially eligible sources by their first \(k\) letters. Their complete forward orbits contribute \(O(Y^{49/50}+kY^{24/25})=O(Y^{49/50})\) possible targets. This proves the uniform bound without assuming any positive orbit terminates.

Both numerical entropy inequalities can be checked without logarithmic rounding:
\[
     5^{250}<2^{245}3^{150}2^{100},\qquad
     8^{200}<2^{192}5^{125}3^{75}.
\]

## Removing the odd budget on the full shell

Take \(K=\lfloor(3/5)\log_2 X\rfloor\). Since \(3^K\le X^{24/25}\), the selector cutoff \(2n\ge K(1+3^K)\) holds everywhere on the shell for large \(X\). CRT or simple periodic counting gives at least \(sX-O(3^K)\) shell representatives in the common set \(F_K\), including \(s_0X-O(3^K)\) representatives with residue zero modulo three. Every visitor from below one of these starts to a listed \(Y\) must spend more than \(j+K\) odd departures.

For a listed \(Y\) admitting a smaller visitor, choose its least positive ancestor \(b\). Its first arrival uses more than \(K\) clock steps. Every state along that arrival is at least \(b\), since each intermediate state itself reaches \(Y\). Both \(b\) and \(Y\) lie in \(I_Z\) for \(Z=3X^{51/50}\). Therefore \(Y\in E_K(Z)\). For fixed \(j,\delta\), the map taking \(n\) to an integral \(Y\) is injective. There are \(O((\log X)^2)\) possible pairs in the growth range, so the number of discarded shell sources is at most
\[
 O\!\left((\log X)^2
     \left[X^{51/50-3/125}+X^{(51/50)(49/50)}\right]\right)=o(X).
\]
The exponents are \(249/250\) and \(2499/2500\). This proves both common lower proportions. Deducting \(o(X)\) from the single class here is legitimate because both displayed densities are normalized by the full shell length \(X\).

A finite fixed collection of scales also admits the same two bounds relative to any prescribed dyadic progression. In that case periodic counting on the progression has the same asymptotic ternary proportions, and its fixed reciprocal density absorbs the global \(o(X)\) error. The theorem gives no simultaneous all-scale pointwise assertion at a single fixed \(n\).
