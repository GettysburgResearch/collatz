# The unscaled depth difference of the original Syracuse law

**Status.** Proposed written detector and quantitative truncation, conditional
on the cited published mixing and ordinary trace inputs. The root remains
one ordinary positive integer throughout each propagated term. The signed
charge below need not vanish by global mean zero.

Use \(S=U\) on positive odd sites, \(w_x=3x/(3x+1)\), and define
\(T\delta_x=w_x\delta_{Ux}\). On signed \(\ell^1\) this is a positive
contraction in total variation. For the original geometric law write
\(u_k(y)=\rho_k(y)/y\), \(\rho_0=1\), and
\[
 \sigma(x)={\bf1}_{x=2\bmod3}-{\bf1}_{x=0\bmod3},\quad
 s(x)=\sigma(x)/x,\qquad d_k=u_{k+1}-u_k=T^ks .                       \tag{1}
\]
Here \(s\) itself is not summable. At every fixed positive \(y,k\),
the sums defining \(T^ks(y)\) are absolutely convergent by domination
by \(T^ku_0(y)=u_k(y)\). Equation (1) follows from the ordinary
one-copy transfer and the exact masses \(\rho_1(0,1,2)=(0,1,2)\).

Let \(q_k=3^{k+1}\), and restrict \(d_k\) to its one complete period
of *positive odd representatives*, writing
\(p_k={\bf1}_{y<2q_k}d_k\). The quantity
\[
 D_k=\|p_k\|_1=
 \sum_{\substack{0<y<2\cdot3^{k+1}\\y\ {\rm odd}}}
        \frac{|\rho_{k+1}(y)-\rho_k(y)|}{y}
\]
uses no period test on an orbit, clipping or two-copy statistic.

## A summable error in propagating the exact finite period

Put \(t_k=3^{-(k+1)}\sum_{r\bmod3^{k+1}}
|\rho_{k+1}(r)-\rho_k(r)|\). At every depth \(k\ge0\),
\[
 p_{k+1}=T p_k+e_k,\qquad \|e_k\|_1\le t_k.                           \tag{2}
\]
All retained sites map inside the next window since \(Ux\le(3x+1)/2\).
Thus \(e_k\) comes exactly from discarded positive parents \(x\ge2q_k\)
mapping into \(Ux<6q_k\). Write \(Q=q_k\), \(x=r+2Qj\), \(r\) the odd
representative, \(j\ge1\). If \(2^h\le j<2^{h+1}\) and \(Ux<6Q\),
then \(2^{v_2(3x+1)}>(3x+1)/(6Q)>j\), so \(2^{h+1}\mid3r+1+6Qj\).
Since \(3Q\) is odd, this selects a single class of \(j\) modulo \(2^h\);
each indicated shell has at most one admissible \(j\). Its reciprocal
weight is at most \(1/(2Q\,2^h)\). The total is at most \(1/Q\) for
each \(r\). Multiply by \(|\rho_{k+1}(r)-\rho_k(r)|\), use \(w_x\le1\),
and sum over \(r\). This gives (2), including its constant.

Tao's fine-scale mixing gives \(t_k\ll_A(k+1)^{-A}\) for every fixed
\(A>0\), by comparing the fresh ternary digit with its Haar lift. The
normalization here is the sum norm of the probability discrepancy.
In particular \(\sum_kt_k<\infty\).
[Tao, Proposition 1.14](https://arxiv.org/abs/1909.03562) · [Weaver, Paper 176, equation (7)](https://rstation.ai/problems/collatz/papers/176/v1)

For all \(j\le k\) we have
\[
 \|p_k-T^{k-j}p_j\|_1\le\sum_{i=j}^{k-1}t_i,\qquad
 D_k\le D_j+\sum_{i=j}^{k-1}t_i.                                       \tag{3}
\]
This is a bound in the physical positive-integer norm. An arbitrary
small perturbation at the final ternary quotient does not suffice for
this assertion. It is the exact propagation and the sparse set of
returning *discarded lifts* that make the error summable.

## The limiting signed masses ride on individual rays

For each escaping component \(C\), choose a ray \(a_{C,0},a_{C,1},\ldots\)
of odd units; \(g_C(Ux)=g_C(x)+1\) is the signed grade determined by
\(g_C(a_{C,n})=n\). Write \(f_\infty(x)=\prod_{j\ge0}w_{U^j x}\),
\(P(x)=x/f_\infty(x)\) on escapes, and
\(Z_{C,v}=\sum_{x\in C,\ g_C(x)=v}1/P(x)\).
Write \(\Delta_{C,v}=Z_{C,v-1}-Z_{C,v}\). Then
\[
 \sum_{C,v}|\Delta_{C,v}|<\infty,\qquad
 \left\|p_k-
  \sum_{\substack{C,v\\k+v\ge0}}\Delta_{C,v}\,
       \delta_{a_{C,k+v}}\right\|_1\longrightarrow0.                   \tag{4}
\]
The comparison is on all odd sites, regarding \(p_k\) as zero outside
its finite window. In particular
\[
 \lim_k D_k=\sum_{C,v}|\Delta_{C,v}|,\qquad
 \lim_k\|p_k\|_\infty=\sup_{C,v}|\Delta_{C,v}|.                         \tag{5}
\]
The empty supremum is zero. Either limit vanishes exactly in the absence
of positive ordinary escape. This conclusion allows any positive cycles.

Here is a proof that keeps the quantifiers of the limiting array.
For a finite signed input \(b\) at depth \(j\), assign its potential
surviving mass to indices \((C,v)\) by summing
\(f_\infty(x)b(x)\) over its escaping support with \(v=g_C(x)-j\).
Call the resulting finite array \(A_j(b)\). Its norm is at most
\(\|b\|_1\) and \(A_{j+1}(Tb)=A_j(b)\). The latter identity uses
\(f_\infty(x)=w_xf_\infty(Ux)\). For \(b=p_j\), (2) implies that
the arrays are Cauchy in \(\ell^1(C,v)\); denote their limit by \(A\).
At fixed \(j\), each site in the finite support of \(p_j\) either
enters a cycle and loses all its mass in the limit, or eventually
lands exactly at \(a_{C,k+v}\) with multiplier tending to \(f_\infty(x)\).
Thus the norm difference between \(T^{k-j}p_j\) and the moving placement
of \(A_j(p_j)\) tends to zero. The placement operator, omitting
\(k+v<0\), has norm at most one. Equation (3) and then \(j\to\infty\)
give (4) with \(A\) in place of \(\Delta\).

For each fixed \(C,v\), the site \(a_{C,k+v}\) lies in the period
for all sufficiently large \(k\): \(a_{C,n}+1\le(3/2)^n(a_{C,0}+1)\).
The ordinary uniform lag identity gives
\(u_{k+1}(a_{C,k+v})\to Z_{C,v-1}\) and
\(u_k(a_{C,k+v})\to Z_{C,v}\), since \(P(a_{C,n})/a_{C,n}\to1\).
Distinct placed entries sit at distinct sites. This identifies
\(A_{C,v}=\Delta_{C,v}\). The array is summable and every fixed
entry is eventually included, proving (5). On every escaping component
the grade profile has \(Z_{C,v}\to0\) at \(+\infty\) while \(Z_{C,0}>0\)
from the chosen positive source itself. It cannot be constant. Under
the stronger two-sided trace input, summing over the grades gives
\(\sum_v\Delta_{C,v}=H_C>0\); hence \(\lim D_k\ge\sum_C H_C\).
[PR 193, fixed-source lag identity and future tail](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/TRACE_PROFILE.md) · [Original two-sided profile](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/COLLISION_ENERGY.md)

Summing the physical signed output in (4) gives the scalar identity
\[
 S_k=\sum_{\substack{0<y<2\cdot3^{k+1}\\y\ {\rm odd}}}
           \frac{\rho_{k+1}(y)-\rho_k(y)}y
              \ \longrightarrow\ \sum_C H_C.                          \tag{6}
\]
The sum is absolutely convergent by (4) and
\(\sum_C H_C\le\sum_{C,v}|\Delta_{C,v}|\). Thus even the scalar
inequality \(\liminf_k S_k\le0\) would exclude escape.

The same proof gives the finite-depth upper bound
\(\lim D_k\le D_j+\sum_{i\ge j}t_i\) at every \(j\). Proving
\(\liminf D_j=0\), or merely \(\liminf\|p_j\|_\infty=0\), would close
the escape question. Summability of the errors in (2) propagates the
finite signed charge, but it does not kill that charge on an infinite
ordinary component.
