# A native-clock marked detector and the backward corrected-height law

**Status.** Source-qualified written theorems. The source is an ordinary
positive odd integer, and the word law assigns probability \(2^{-e}\) to
each exponent \(e\ge1\). The joint fine-scale mixing input is Weaver–Wren
Theorem 6. The negative-grade limit \(H_C>0\) uses the separately pinned
two-sided trace result. No limit here proves that every ordinary source
enters a cycle.

## The finite marked statistic

Let \(E_k(x)=\sum_{i<k}v_2(3U^ix+1)\), \(f_k(x)=\prod_{i<k}w_{U^ix}\),
\(q=3^k\). For any real-valued function \(\psi\) on \(\mathbb Z/3\)
with \(\sum_r\psi(r)=0\), define
\[
 M_k^\psi(h,y)=\sum_{\substack{U^kx=y\\E_k(x)=h}}
                      \psi(x)\frac{f_k(x)}x,\qquad
 {\cal D}_k(\psi)=\sum_{\substack{0<y<6q\\y\ {\rm odd}}}
                                 \sum_{h\ge0}|M_k^\psi(h,y)|.            \tag{1}
\]
The norm uses only one marked coordinate in addition to the positive odd
representative. Write \(P_h(r)=\Pr(E_k=h,F_k=r\bmod 3q)\) for the
original finite affine intercept law, as in the
[physical-source estimate](PHYSICAL_SOURCE.md). For every such target,
\[
 M_k^\psi(h,y)=\frac qy
             \sum_{j=0}^2\psi(2^hj\bmod3)P_h(y-jq\bmod 3q).            \tag{2}
\]
Indeed a legal inverse word gives its unique positive odd source by
successive inversion, with residue \(x=2^h(y-F_k)/q\bmod3\), and
\(f_k(x)/x=(q/y)2^{-h}\). Formula (2) evaluates (1) using the
original finite random law without testing any trajectory for escape.

In the estimate on an octave \(X\le x<2X\) in the physical-source note,
its equation (2) was already summed in absolute value *before* summing
the clock \(h\). Each word reassignment or truncation error there was
bounded by its unsigned source mass. The argument therefore proves,
for \(1\le t\le(\log_2X)/32\), any interval \(I\subset[X,2X]\) and
fixed \(A>0\),
\[
 \sum_{h,y}\left|\sum_{\substack{x\in I,\ U^tx=y\\E_t(x)=h}}
                \psi(x)f_t(x)/x\right|
                       \ll_A\|\psi\|_\infty t^{-A}.                     \tag{3}
\]
Here \(y\) ranges over all positive odd targets. The future marked
transfer sends \(\delta_{(h,y)}\) to
\(w_y\delta_{(h+e(y),Uy)}\) and contracts the joint sum norm.
Consequently the same octave summation, including the unconditioned
large-clock tail when \(\log_2 X>16k\), gives
\[
 \limsup_{k\to\infty}\sum_{\substack{y<6q,\ y\ {\rm odd}\\h\ge0}}
 \left|\sum_{\substack{x\ge R,\ U^kx=y\\E_k(x)=h}}
           \psi(x)f_k(x)/x\right|
       \ll_A\|\psi\|_\infty(1+\log R)^{-A}.                            \tag{4}
\]
The constants are uniform in \(R\) and \(\psi\). They may depend on
the exponent \(A\). [Weaver–Wren, Paper 48/v1, §8, Theorem 6](https://rstation.ai/problems/collatz/papers/48/v1)

## Exact corrected-height classes

On an escaping component \(C\) put \(p=P(x)=x/f_\infty(x)\), with
\(P(Ux)=3\,2^{-e(x)}P(x)\). All sites with the same value of \(p\)
in \(C\) have the same signed odd grade. Indeed, if \(U^ix=U^jz\)
and \(P(x)=P(z)\), then \(3^{i-j}=2^{E_i(x)-E_j(z)}\). Unique
factorization gives \(i=j\) and equal native clocks. Conversely at
any fixed time \(k\), two inputs of the same \((E_k,U^k)\) have the
same component and corrected height if they escape. At fixed \((C,p)\)
there are only finitely many starts, since \(x\le p\).

There is also an absolute \(K\) with \(P(x)\le Kx\) for *all* escaping
starts. The interval compression in the
[source occupation note](SOURCE_OCCUPATION.md) bounds the number of
distinct states of an actual escaping orbit in \([2^j,2^{j+1}]\) by
\(O(2^{js})\), for a fixed \(s<1\), uniformly over all time horizons
and starts. Summing by dyadic intervals gives a uniform bound for
\(\sum_{i\ge0}1/U^ix\), and
\(\log(P(x)/x)=\sum_{i\ge0}\log(1+1/(3U^ix))\). This only gives a
constant-factor comparison at large ancestors. The stronger ratio
\(P(U^nx)/U^nx\to1\) applies along the future of a fixed escaping start.

Define
\[
 B^\psi(C,p)=\frac1p\sum_{\substack{x\in C\\P(x)=p}}\psi(x),\qquad
 B_R^\psi(C,p)=\frac1p\sum_{\substack{x<R,\ x\in C\\P(x)=p}}\psi(x).
\]
Then, in the sum norm over all components and their countable attained
heights,
\[
 \|B^\psi-B_R^\psi\|_1\ll_A\|\psi\|_\infty(1+\log R)^{-A},\qquad
 \boxed{\displaystyle\lim_{k\to\infty}{\cal D}_k(\psi)
            =\sum_{C,p}|B^\psi(C,p)|<\infty.}                          \tag{5}
\]
For proof, truncate the input at \(R\). Eventually periodic inputs lose
all their mass. Escaping inputs in a common exact class eventually
coalesce at precisely the same marked site. Distinct classes cannot do
so. All retained positive inputs lie in \(y<6q\) at sufficiently large
depth by the elementary \(U^kx+1\le(3/2)^k(x+1)\). Hence the norm of
the truncated signed output tends to \(\|B_R^\psi\|_1\).
For two cutoffs \(R<R'\), apply (4) to the input on \([R,R')\), using
partial initial and final octaves in its proof. Taking \(k\to\infty\)
makes \(B_R^\psi\) Cauchy in \(\ell^1(C,p)\). Since each class is
finite, the coordinatewise limit is the stated \(B^\psi\). Equation (4)
now compares the full norm to the truncated one and proves (5).
In particular
\[
              \sum_{C,p\ge L}|B^\psi(C,p)|
                       \ll_A\|\psi\|_\infty(1+\log L)^{-A},             \tag{6}
\]
where the notation sums every \(C\) and the attained \(p\ge L\).
Use \(P(x)\le Kx\) in (5), choosing \(R=L/K\) when \(L\ge2K\).

For \(\psi=3{\bf1}_{r=2}-1\), the limit in (5) is zero exactly when
there is no positive ordinary escape. In fact every nonempty escaping
component has a minimum corrected height \(p_*\). Some site realizes
it, since \(x\le P(x)\) makes all bounded height sublevel sets finite.
If a minimizer \(x\) were \(2\bmod3\), its ordinary odd parent
\((2x-1)/3\) would have corrected height \(2p_*/3<p_*\). Therefore
\(B^\psi(C,p_*)=-\#\{x\in C:P(x)=p_*\}/p_*<0\).
This criterion permits positive cycles of any period. The minimum-cell
argument itself uses neither the stationary integer trace nor a lower
bound on \(H_C\). The estimate (4) controls the marked contribution
from large physical inputs. The contribution of a fixed finite input
that reaches arbitrarily large heights remains an open obstruction.

## A geometric convolution on the actual backward grades

Fix an escaping component \(C\) and base site \(a_0\), of grade zero,
with \(P_0=P(a_0)\). At grade \(v\in\mathbb Z\) each corrected height
is \(p_{v,l}=P_0 3^v2^l\) for one \(l\in\mathbb Z\); different
\((v,l)\) are distinct even for negative indices. Put
\[
 m_v(l)=\frac{\#\{x\in C:P(x)=p_{v,l}\}}{p_{v,l}},\qquad
 m_{v,r}(l)=\frac{\#\{x\in C:P(x)=p_{v,l},\ x=r\bmod3\}}{p_{v,l}}.
\]
Then \(\|m_v\|_1=Z_{C,v}<\infty\) by the fixed-grade atom-floor
argument. Apply (5) to \(\psi_r={\bf1}_{r}-1/3\) to obtain
\[
             \sum_{C,v,l}\left|m_{v,r}(l)-m_v(l)/3\right|<\infty       \tag{7}
\]
with the tail (6). At any target of grade \(v\) and height
\(p_{v,l-e}\), a parent with gap \(e\ge1\) exists exactly when its
residue is \(r_e=2^{-e}\bmod3\); it is then unique, ordinary positive
and odd, with height \(p_{v-1,l}\). Consequently
\[
  m_{v-1}(l)=\sum_{e\ge1}3\,2^{-e}\,m_{v,r_e}(l-e)
            =(G*m_v)(l)+b_v(l),\qquad G(e)=2^{-e}{\bf1}_{e\ge1}.       \tag{8}
\]
By the triangle inequality and (7),
\(\sum_{C,v}\|b_v\|_1\le 3\sum_{C,v,l,r}|m_{v,r}(l)-m_v(l)/3|<\infty\).

Write \(g_n=G^{*n}\), the law of the sum of \(n\) independent original
positive geometric gaps. For each component the backward profile obeys
\[
                    \boxed{\displaystyle
       \|m_{-n}-H_C g_n\|_{\ell^1(\mathbb Z)}\longrightarrow0.}          \tag{9}
\]
To see this, iterate (8) exactly:
\[
 m_{-n}=g_n*m_0+\sum_{j=0}^{n-1}g_{n-1-j}*b_{-j}.
\]
For fixed \(d\ge0,\ l\in\mathbb Z\), the sum-norm distance from
\(g_{n-d}(\cdot-l)\) to \(g_n\) tends to zero. In fact
\(g_n(t)=\binom{t-1}{n-1}2^{-t}\) for \(t\ge n\) is unimodal with
\(\max_tg_n(t)=O(n^{-1/2})\) by its consecutive ratio and the central
binomial bound. Thus a shift by \(l\) has cost at most
\(2|l|\max g_n\). Integrating the fixed shifts in
\(g_n=g_d*g_{n-d}\) proves the claim since the distance is bounded by
two. By finite-support approximation of an \(\ell^1\) input,
\(g_{n-d}*c\) differs from \((\sum_l c(l))g_n\) by \(o(1)\) for fixed
\(c,d\). Apply this to \(m_0\) and finitely many \(b_{-j}\), and bound
the remaining errors in sum norm by their summable tail. The scalar
multiplying \(g_n\) is \(\sum_l m_0(l)+\sum_{j\ge0,l}b_{-j}(l)\),
which equals \(\lim_n Z_{C,-n}=H_C\) by summing (8) and using the
two-sided profile. [PR 193, two-sided profile and atom-floor inputs](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/COLLISION_ENERGY.md)

In particular, with each grade-\((-n)\) source weighted by \(1/P(x)\),
the measured exponent \(l=\log_2(P(x)/P_0)+n\log_2 3\) has total
variation distance \(o(1)\) from this negative-binomial law after
normalization by \(Z_{C,-n}\), and its ternary residue is asymptotically
uniform jointly with \(l\), by (7). The bulk has
\(\log_2(P/P_0)=(2-\log_2 3)n+O_{\rm prob}(\sqrt n)\).
Equation (9) allows an exceptional set of mass \(o(1)\) and does not
give relative estimates in its exponentially small tails. In particular
it gives no pointwise law for the future of a specified positive source.
