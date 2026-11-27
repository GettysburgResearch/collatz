# Exact central clocks at fixed and moving ordinary roots

**Status.** Source-qualified written theorems. The fixed-root statement
applies to every specified positive odd target, including periodic
ones. The moving-root statement concerns the actual future of a single
hypothetical escaping positive source. The remaining issue is uniformity
in the root at intermediate depths.

Let \(F_n\) be the length-\(n\) original Syracuse affine offset,
\(E_n\) its total division exponent, and \(g_n(h)=\Pr(E_n=h)\).
For a positive odd \(y\), let
\[
 A_n(y,h)=\#\{x>0\ {\rm odd}:U^nx=y,\ E_n(x)=h\},\qquad
 p_{n,h}=y\,2^h3^{-n},\qquad
 m_n(h)=A_n(y,h)/p_{n,h}.
\]
Thus \(m_n(h)=(3^n/y)\Pr(F_n=y\bmod3^n,\ E_n=h)\). Write
\(h_{\rm tr}(y)=\lim_n\rho_n(y)\) for the ordinary integer trace.

## Every fixed ordinary root

For every fixed positive odd \(y\),
\[
 \sup_{n,h:\ p_{n,h}\ge R}\sqrt{\log p_{n,h}}\,
 \left|m_n(h)-\frac{h_{\rm tr}(y)}y\,g_n(h)\right|
                 \ \longrightarrow0\qquad(R\to\infty).               \tag{1}
\]
In particular for every fixed \(K<\infty\)
\[
 \sup_{|h-2n|\le K\sqrt n}
 \left|3^n\Pr(F_n=y\bmod3^n\mid E_n=h)-h_{\rm tr}(y)\right|
                   \longrightarrow0.                                 \tag{2}
\]
At the exact central total,
\[
             A_n(y,2n)\sim
          \frac{h_{\rm tr}(y)(4/3)^n}{\sqrt{4\pi n}}
                    \quad(3\nmid y).                                  \tag{3}
\]
At \(3\mid y\) all the layers beyond time zero vanish. Thus (3) gives
large genuine simultaneous-clock inverse fibres even at fixed roots such
as \(5\) whose future enters the elementary cycle.

To prove it, for \(r=0,1,2\) let
\(\psi_r={\bf1}_{x=r\bmod3}-1/3\). Split \(m_n(h)\) by the residue
of the corresponding ordinary starts, say as \(m_{n,r}(h)\). The
difference \(\epsilon_n^r(h)=m_{n,r}(h)-m_n(h)/3\) is the signed
weight \(\sum\psi_r(x)f_n(x)/x\) on that exact layer. One has
\[
 \sum_{n,h}|\epsilon_n^r(h)|<\infty,\qquad
 \sum_{n,h:\ p_{n,h}\ge R}|\epsilon_n^r(h)|
                  \ll_{y,A}(1+\log R)^{-A}.                           \tag{4}
\]
Here is the uniformity over all times in (4). Any marked site \((h,z)\)
has total subsequent surviving weight at \(y\), summed over *all*
elapsed times including zero, at most
\[
 J_y=1\quad(y\ \hbox{nonperiodic}),\qquad
 J_y=(1-\lambda_y)^{-1}\quad(y\ \hbox{periodic}),
\]
where \(\lambda_y<1\) is the product of \(w\)'s around the odd cycle.
On that cycle \(\lambda_y\le w_y=3y/(3y+1)\), hence \(J_y\le3y+1\).
An ordinary trajectory visits the former at most once. After its first
visit to a cycle target, later weights decrease geometrically at each
full lap. The current clock mark does not change this bound.

Take \(X\ge \max(4,y^2)\) and an ordinary source interval
\(I\subset[X,2X]\). At \(t=\lfloor(\log_2 X)/32\rfloor\), the
joint marked cancellation (3) of the
[marked-fibre theorem](MARKED_FIBRES.md) bounds the norm of the signed
layer over all \((h,z)\) by \(O_A((1+\log X)^{-A})\), enlarging
constants for small \(t\). Sum its future contributions to \(y\) for
all \(n\ge t\), paying at most \(J_y\) times this bound. For earlier
visits \(n<t\), the positivity of the affine offset forces
\(2^{E_n(x)}\ge x/y\ge \sqrt X\), hence \(E_t(x)\ge(\log_2 X)/2\).
For \(L=\lfloor(\log_2 X)/2\rfloor-1\), the event \(E_t>L\) is read
modulo \(2^{L+1}\) on odd integers. Its Haar probability is at most
\(3^t(2/3)^L\ll X^{-c}\) for an absolute \(c>0\); the incomplete
period in the octave contributes \(O(2^{L+1}/X)\) to the reciprocal
mass. Each exceptional start can contribute at most \(J_y/x\) over all
its visits. This bounds also the sum over \(n<t,h\). Summing octaves
proves a rapid \((\log R)^{-A}\) bound for the signed contribution from
all starts \(x\ge R\) to these fixed-target layers. A finite range
\(x<R\) contributes at most \(J_y\sum_{x<R}1/x\).

To obtain the asserted \(p_{n,h}\)-tail in (4), first use the
source-tail bound on \(x\ge\sqrt R\). Each remaining site
\(x<\sqrt R\) contributes at most \(J_y/R\) to cells with
\(p_{n,h}\ge R\): at its first eligible visit the weight is
\(1/p_{n,h}\le1/R\), and later visits, if any, form a geometrically
decaying sequence. There are at most \(\sqrt R\) such starts.
This proves (4), including periodic targets.

The exact inverse-parent identity is
\[
 m_{n+1}(h)=\sum_{e\ge1}3\,2^{-e}m_{n,r_e}(h-e)
                       =(G*m_n)(h)+c_{n+1}(h),\qquad r_e=2^{-e}\bmod3 .
\]
Equation (4) and the geometric shift in
\(p_{n+1,h}=(2^e/3)p_{n,h-e}\) imply the same summability and
rapid tail for \(c\). Include \(m_0=\delta_0/y\) as forcing at time
zero. The exact solution is the sum of these fixed forcings convolved
with \(g_{n-j}\) from each forcing time \(j\le n\).
Its total forcing mass is \(\lim_n\sum_h m_n(h)=h_{\rm tr}(y)/y\),
by summing the recurrence. Conversely this argument also yields
existence of the ordinary-depth limit, previously obtained by Weaver.
For (1) apply the point-kernel bounds and the finite-forcing
approximation in [the local height law](LOCAL_HEIGHT_LAW.md), now with
lag \(n-j\) and origin height \(p_{j,h_0}\). The contributing
displacement is exactly \(\log_2(p_{n,h}/p_{j,h_0})=h-h_0-(n-j)\log_2 3\).
In the window of (2), \(\log p_{n,h}\asymp_y n\) and
\(g_n(h)\gg_K n^{-1/2}\) by Stirling, hence division of (1) by \(g_n(h)\)
is legitimate. The atom floor makes \(h_{\rm tr}(y)>0\) for units.
[Weaver–Wren, Paper 48, v2, Theorem 6](https://rstation.ai/problems/collatz/papers/48) · [Weaver, Paper 176, ordinary integer trace](https://rstation.ai/problems/collatz/papers/176) · [Weaver, Paper 9, Theorem 18, compact-real central-clock stability in Haar norms](https://rstation.ai/problems/collatz/papers/9)

The same convolution with its summable forcing gives
\(\|m_n-(h_{\rm tr}(y)/y)g_n\|_1\to0\), by translation continuity of
\(g_n\) as in the marked-fibre theorem. Thus for positive odd units the
total variation distance between the actual clock conditioned on this
fixed terminal residue and the original \(g_n\) tends to zero.

## The diffusive onset forced by any escaping ordinary source

Fix a positive odd unit \(a_0\) whose future escapes, write
\(a_j=U^ja_0\), \(A_j=E_j(a_0)\), and choose this site as the origin
of its component grade. If \(n=j+d\) and \(j,d\to\infty\), then
\[
 d_{\rm TV}\bigl({\cal L}(E_n\mid F_n=a_j\bmod3^n),\
                      {\cal L}(A_j+E_d)\bigr)\ \longrightarrow0.       \tag{5}
\]
The \(E_d\) on the right has the original iid law. The depth \(n\),
root \(a_j\), and conditional total all use the same ordinary forward
trajectory. With this moving condition, (5) gives
\[
 \begin{array}{ll}
 d_{\rm TV}\bigl({\cal L}(E_n\mid F_n=a_j\bmod3^n),g_n\bigr)\to1
                              &\text{if }n=o(j^2),\\
 \liminf d_{\rm TV}\bigl({\cal L}(E_n\mid F_n=a_j\bmod3^n),g_n\bigr)>0
                              &\text{if }n=O(j^2),\\
 d_{\rm TV}\bigl({\cal L}(E_n\mid F_n=a_j\bmod3^n),g_n\bigr)\to0
                              &\text{if }j^2=o(n).
 \end{array}                                                           \tag{6}
\]

Indeed, a source with \(U^nx=a_j,E_n(x)=h\) has corrected height
\(P_0 3^{-d}2^{h-A_j}\). Its weight \(1/P(x)\) is constant on this
exact cell and every such source belongs to the grade-\((-d)\) count.
At each \(h\), its corrected mass is bounded above by the full
\(m_{-d}(h-A_j)\). The *sum of these nonnegative differences* over
\(h\) is exactly
\[
                  Z_{C,-d}-\rho_n(a_j)/P(a_j)=o_{j\to\infty}(1)
                             \quad\hbox{uniformly in }d\ge0,
\]
by the uniform lag theorem. The backward grade law (9) in the
marked-fibre theorem replaces \(m_{-d}\) in sum norm by \(H_Cg_d\),
with \(H_C>0\). Normalization cancels the common \(P(a_j)\) factor,
giving (5).
[PR 193, uniform lag identity at all depths](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/TRACE_PROFILE.md)

The two clocks in (6) have means \(A_j+2d\) and \(2n\); the gap
\(\Delta_j=2j-A_j\) satisfies
\[
 (2-\log_2 3)j-O_{a_0}(1)\le\Delta_j\le j.
\]
The lower bound uses \(P(a_j)=3^j2^{-A_j}P_0\ge1\), the upper bound
uses \(A_j\ge j\). Both variances are at most \(2n\), so the event below
the midpoint of the two means gives a total variation lower bound
\(1-O(n/\Delta_j^2)\) when \(j/\sqrt n\to\infty\). If \(n=O(j^2)\)
and this ratio stays bounded along a subsequence, then \(d/n\to1\)
and the two means differ by a positive bounded-below number of standard
deviations. The ordinary iid central limit theorem at the midpoint
gives a strictly positive difference of probabilities, uniformly when
the ratio is bounded and bounded away from zero. Finally
\(g_n=g_j*g_d\) and translating the unimodal \(g_d\) by \(b\) costs at
most \(2|b|\|g_d\|_\infty\) in sum norm. Thus its distance after a
shift \(A_j\) from \(g_n\) is \(O(j/\sqrt d)\), proving the third line.

In particular the unconditioned central-clock limit at each fixed
integer root cannot be used at moving positive roots without a
quantified onset. Equation (6) places that onset directly on the
*square of the elapsed odd time of the ordinary source*. A uniform
estimate forcing central-clock agreement on this actual diagonal for
some \(n\ll j^2\) would exclude escape. No such estimate is established
by the fixed-root theorem or by Haar-averaged joint mixing.
