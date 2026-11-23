# The actual boundary law, time information, and the integer-diagonal cost

Date: 2026-11-23.

**Status: SOURCE-QUALIFIED written deductions; the direct entropy-closing
attempt remains OPEN.** This note tests the new coherent real boundary
against the actual-orbit entropy ceiling. It retains the same hypothetical
escaping ordinary component, the same forward ray, and the same inverse
probability laws throughout. No escape or cycle exclusion is claimed.

Two deductions sharpen the interface. The whole actual-path boundary
becomes independent of every observable of the supplied forward clock,
with a relative-entropy error tending to zero. In contrast, obtaining the
same moving ordinary fibre from the bulk real/ternary affine law costs a
linear amount of relative entropy in that clock. Even after paying for
the large real height first, a positive linear conditioning cost remains.
Thus the newly proved full Hausdorff dimension of the boundary **support**
cannot simply be inserted as an entropy lower bound for the time law.

## 1. Objects and exact sources

Use the notation and construction of [ANALYTIC_GLUING.md](ANALYTIC_GLUING.md).
In particular, on one hypothetical escaping component \(E\),

\[
q_j=U^j(q_0),\qquad v_j=\nu(q_j)\uparrow c_E>0,
\qquad K(q,n)=\mathbf1_{Un=q}\nu(n)/\nu(q).
\tag{1}
\]

The two-sided actual-path law is \(\Pi_E\). Its common real boundary is
\(Z\in[a_E,b_E]\), with \(0<a_E<b_E<\infty\). Write

\[
y(n)=n/\chi(n),\quad y(q_j)\uparrow b_E,\quad
s_E=\mathbb E_{\Pi_E}Z,\quad
d\Pi_E^G=(Z/s_E)d\Pi_E.
\tag{2}
\]

The component-normalized boundary variable will be
\(T=1-Z/b_E\). This is different from the physical normalized intercept
at root \(q_j\), which is \(T_j=1-Z/y(q_j)\).

The source qualifications in the following inputs are retained.

| Pin | Exact use |
|---|---|
| PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2`, `research/retained-source-attacks-20261122/CANONICAL_CHARGE.md` | The ordinary harmonic flow and the actual two-sided path law. |
| This checkpoint, `ANALYTIC_GLUING.md`, Sections 2--4 and 6 | The coherent coordinate, exact boundary variable, conditional inverse laws, positive size bias, and dimension-one support construction. |
| PR185, `39ba48e6a8af781193e28c679ea8ab64663c3aa6`, `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`, Sections 1--4 | Exact retracing at every inverse depth and the actual ternary entropy ceiling. |
| PR185, `39ba48e6a8af781193e28c679ea8ab64663c3aa6`, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, Section 7 | Source-qualified fixed-basin sublinearity: \(\nu(n)\to0\) as \(n\to\infty\) within the predecessor basin of a fixed nonperiodic target. |
| PR178, `7e4569476e152f6b8537bdc1711df595ec1ffd89`, `research/whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md`, Sections 2--6 | The comparable trace kernel, its moving real fibres, and their common weak limit. |
| PR175, `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`, `research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`, Theorems 1--2 | Uniform moving-clock scalar and joint-fibre traces, at precision \(j+r+1\). The note itself freezes its earlier external trace inputs. |

No assertion about the actual boundary's metric dimension, absolute
continuity, or Fourier decay is added to these premises. In particular,
the auxiliary Frostman measures constructed in the companion note are
not identified with the canonical probability law.

## 2. A general conditioning identity on these actual paths

Normalize the component clock by \(\ell(q_0)=0\), and put

\[
E_j=\{Q_j=q_j\}.
\]

These are increasing events: the deterministic forward step sends
\(q_j\) to \(q_{j+1}\). Equation (1) gives

\[
\Pi_E(E_j)=v_j/c_E\longrightarrow1.
\tag{3}
\]

The complete inverse law from \(q_j\), with its deterministic future
adjoined, is exactly \(\Pi_E(\,\cdot\mid E_j)\). Thus this conditioning
does not replace an ordinary source by an independent valuation law.

More generally let \(\mathsf P\) be either \(\Pi_E\) or \(\Pi_E^G\),
and set \(p_j=\mathsf P(E_j)\). In both cases \(p_j>0\),
\(p_j\uparrow1\), and the conditional inverse law is the corresponding
ordinary or critical inverse law. For the critical law the companion
note gives the exact expression

\[
p_j^G
=\frac{v_j\,\mathbb E[Z\mid E_j]}{c_Es_E}
=\frac{y(q_j)h(q_j)}{c_Es_E},\qquad h=G/n.
\tag{4}
\]

Choose \(J\) uniformly from \(\{0,\ldots,M\}\). Let
\(\mathsf Q_M\) be the law that then samples the whole actual path
from \(\mathsf P(\,\cdot\mid E_J)\). Let \(\mathsf R_M\) instead
sample that same label independently of a path of law \(\mathsf P\).
The Radon--Nikodym derivative, on the product of the finite label set
and the path space, is

\[
\frac{d\mathsf Q_M}{d\mathsf R_M}(j,\omega)
=\frac{\mathbf1_{E_j}(\omega)}{p_j}.
\]

It follows directly, with natural logarithms, that

\[
\boxed{
D_{\rm KL}(\mathsf Q_M\Vert\mathsf R_M)
=\frac1{M+1}\sum_{j=0}^M\log\frac1{p_j}
=:\beta_M\longrightarrow0.}
\tag{5}
\]

The last step is ordinary Cesaro convergence; the summands tend to zero
and are bounded by \(\log(1/p_0)\). The corresponding total variation
identity is

\[
\|\mathsf Q_M-\mathsf R_M\|_{\rm TV}
=\frac1{M+1}\sum_{j=0}^M(1-p_j).
\tag{6}
\]

Indeed on each label the conditional law has density \(1/p_j\) on
\(E_j\) and zero outside it, and its TV distance from \(\mathsf P\)
is exactly \(1-p_j\). The convention here is
\(\|P-Q\|_{\rm TV}=\sup_A|P(A)-Q(A)|\).

Equation (5) concerns the full inverse history, not merely one endpoint
or a bounded inverse window. Its information loss under any measurable
projection can only decrease.

## 3. Uniform decoupling from every actual time observable

Let \(X_M=f_M(J)\) be any measurable function of the supplied time
label, and let \(Y_M=g_M(Z)\) be any measurable observation of the
common boundary. Their alphabets or resolutions may depend arbitrarily
on \(M\). Under \(\mathsf R_M\) the two variables are independent.
Data processing in (5) gives

\[
D_{\rm KL}\!\left(
 \mathsf Q_M^{(X_M,Y_M)}
 \middle\Vert
 \mathsf Q_M^{X_M}\otimes\mathsf P^{Y_M}
\right)\le\beta_M.
\tag{7}
\]

For completeness, the data-processing inequality here follows by
conditioning the displayed density in Section 2 on the projected
variables and applying Jensen to the convex function \(t\log t\).
The label marginal is unchanged, which explains the first marginal on
the right of (7).

The relative-entropy chain rule splits the left side of (7) into the
mutual information and the relative entropy of the boundary marginal:

\[
\boxed{
I_{\mathsf Q_M}(X_M;Y_M)
 +D_{\rm KL}(\mathsf Q_M^{Y_M}\Vert\mathsf P^{Y_M})
\le\beta_M\longrightarrow0.}
\tag{8}
\]

One may also take \(Y_M=Z\) itself. The finite bound in (7) licenses
the chain rule on these standard Borel spaces; equivalently one first
uses finite partitions and then increases them. In particular (8) is
uniform in all ternary precisions when

\[
X_M=q_J\bmod3^{m_M},
\]

and also holds for the leading binary phase, any chosen valuation
window on the actual forward ray, or their joint observation. These
remain deterministic functions of the **same** \(J\); no orbit is
resampled. For finite observations the equivalent entropy assertion is

\[
H(X_M,Y_M)
\ge H(X_M)+H(Y_M)-\beta_M.
\tag{9}
\]

Thus entropy carried by the component boundary can persist as a
separate latent factor while the actual ternary time marginal retains
its previously proved ceiling

\[
\limsup_M\frac{H_{m_M}(\pi_M)}{m_M\log3}
\le\theta=0.949955527188\ldots,
\qquad m_M=o(M),
\tag{10}
\]

with the boundary correction and exact quantifiers from the pinned
PR185 theorem. The new dimension-one support result does not reverse
(10) through this conditioning mechanism.

### The moving physical normalization must be retained

Equations (7)--(9) hold for the common variable \(Z\), or for
\(T=1-Z/b_E\). The physical fibre at root \(q_J\) instead uses

\[
T_J=1-Z/y(q_J)
=1-\frac{b_E}{y(q_J)}(1-T).
\tag{11}
\]

This is a transformation depending on \(J\). Although \(y(q_j)\to b_E\)
gives the established bounded-Lipschitz convergence of the physical
fibres, it does not allow \(T_J\) to replace \(T\) in (8) at arbitrary
moving resolutions. A small deterministic translation or dilation can
encode its label at a sufficiently fine scale. No continuity estimate
for relative entropy under (11) has been proved for the canonical
boundary law. Dropping this distinction would create a false
all-resolution independence assertion.

The trace law \(h_{\rm tr}\) in PR178 has the further bounded positive
whole-path tilt \(ZW/\mathbb E(ZW)\) of the companion note, with
\(\eta\le W\le2\). Applying Section 2 to that fixed tilted law gives
the same conclusions in the common frame. Neither its exact event
probabilities nor its boundary law are silently identified with (4).

### Fixed-root complete-path entropy diverges, without a rate

Fix \(q\in E\), and write \(\mathcal P_r(q)=\{n:U^r(n)=q\}\)
for its unit inverse-depth level. The pinned fixed-basin sublinearity
from PR185, Section 7, says

\[
\sup_{\substack{n\in\operatorname{Pred}(q)\\n\ge M}}\nu(n)
\longrightarrow0\qquad(M\to\infty).
\]

For each fixed \(M\), only finitely many integers lie below \(M\),
and each can hit the nonperiodic \(q\) at at most one depth. Hence
\(\mathcal P_r(q)\cap[1,M]=\varnothing\) for all sufficiently
large \(r\). This is a fixed-root assertion; its depth threshold
may depend on \(q\) and \(M\).

Under the inverse law \(\mathbb P_\nu^q\) with kernel (1), let
\(W_r=(N_1,\ldots,N_r)\), where \(N_0=q\). Each endpoint
\(n\in\mathcal P_r(q)\) determines exactly one complete legal word,
since its forward path is deterministic. Telescoping the kernel gives
the cylinder probability \(\nu(n)/\nu(q)\). The preceding two facts
therefore prove

\[
a_r(q):=\sup_w\mathbb P_\nu^q(W_r=w)
=\sup_{n\in\mathcal P_r(q)}\frac{\nu(n)}{\nu(q)}
\longrightarrow0,
\qquad
H(W_r)\ge-\log a_r(q)\longrightarrow+\infty.
\]

The entropy inequality is valid also when the countable-word entropy
is infinite. Every infinite path belongs to prefix cylinders of mass
at most \(a_r(q)\); consequently this complete-path law is nonatomic.
The fixed-root critical and trace laws inherit both conclusions from
their bounded positive path-law densities displayed above: their
maximum word masses are at most a fixed multiple of \(a_r(q)\).
The two-sided law \(\Pi_E\) is likewise nonatomic, by conditioning
on its countable state \(Q_0\); the forward future is deterministic
and each conditional inverse law has just been shown nonatomic.

This proves no rate in \(r\). It gives no nonatomicity or metric
entropy conclusion for the real pushforward \(Z\), because no
injectivity or overlap bound for that projection has been established.
It also gives no uniform or diagonal conclusion for moving roots
\(q_j\): the depth threshold above depends on the fixed target, and
the persistent retracing cylinders of the moving-root laws remain.

## 4. A direct test against the bulk joint affine law

Let \(\mathbf m\) be the stationary joint law of the independently
sampled affine series, with real coordinate \(R\) and ternary coordinate
\(Z_3\). It is a different measure from \(\Pi_E\). Write

\[
D_m(q)=3^m\mathbf m\{Z_3\equiv q\pmod{3^m}\}.
\tag{12}
\]

The pinned PR175/178 trace results imply the following useful precise
selection. There exist constants \(0<a<b<\infty\), \(c_1,c_2>0\),
and a finite \(R_0\), depending on the supplied escaping source, such
that for every sufficiently large \(k\) one can choose
\(0\le r_k<R_0\), put \(m_k=k+r_k+1\), and obtain

\[
\begin{aligned}
c_1 q_k3^{-m_k}
&\le\mathbf m(C_k\cap H_k)\le\mathbf m(C_k)
\le c_2q_k3^{-m_k},\\
C_k&=\{Z_3\equiv q_k\pmod{3^{m_k}}\},\qquad
H_k=\{a q_k<R<bq_k\}.
\end{aligned}
\tag{13}
\]

Here is why the choice is legitimate. The common trace fibre has
positive mass in some compact real interval away from zero, by its
exact positive boundary representation and nonconstancy. Choose a
nonnegative bounded Lipschitz test supported in that interval, with
positive limiting integral. The uniform mean BL trace theorem, together
with the uniform scalar mean-absolute trace theorem, makes the average
of the two errors as small as desired over \(0\le r<R_0\), uniformly
in \(k\). At least one \(r\) therefore has both errors small.
Finally \(h_{\rm tr}(q_k)/q_k\) tends to a positive finite constant
in the pinned PR178 theorem. This proves (13) with fixed constants.
One does not need pointwise convergence at every excess depth.

Conditioning a probability on an event of positive mass costs exactly
the negative logarithm of that mass. Consequently (13) gives

\[
\begin{aligned}
D_{\rm KL}(\mathbf m(\,\cdot\mid C_k)\Vert\mathbf m)
&=m_k\log3-\log q_k+O_{q_0}(1)\\
&\ge k\log2-O_{q_0}(1).
\end{aligned}
\tag{14}
\]

The last inequality uses only the actual growth bound
\(q_k+1\le(3/2)^k(q_0+1)\). In particular the conditioning cost
divided by \(m_k\log3\) has lower limit at least
\(\log2/\log3\). This is not the vanishing cost in (5): the two
comparisons start from different measures, explicitly identified above.

### Paying for the real height first still leaves a linear cost

The already imported Kesten--Goldie real-tail result says
\(\mathbf m(R>t)\sim C_*/t\), with \(C_*>0\). Therefore, for the
fixed shell in (13),

\[
\mathbf m(H_k)\asymp_{a,b}q_k^{-1}.
\]

Let \(\mathbf m_k=\mathbf m(\,\cdot\mid H_k)\). Equation (13) gives
\(\mathbf m_k(C_k)\asymp q_k^2 3^{-m_k}\), and hence

\[
\boxed{
\begin{aligned}
D_{\rm KL}(\mathbf m_k(\,\cdot\mid C_k)\Vert\mathbf m_k)
 &=m_k\log3-2\log q_k+O_{q_0}(1)\\
 &\ge k\log(4/3)-O_{q_0}(1).
\end{aligned}}
\tag{15}
\]

This residual cost is at least
\(\log(4/3)/\log3=0.2618595\ldots\) per ternary digit asymptotically,
whereas the dimension deficit in (10) is about \(0.0500445\).
This numerical comparison does not by itself prove an impossibility
theorem for all entropy methods. It does show that this particular
rare-event conditioning is not a negligible change of measure at the
scale where the hoped-for entropy contradiction would operate.

## 5. The geometric and real-localization attacks

The primary manuscript Paper 19 v2, Section 10, gives the uniform
product-ball estimate

\[
\mathbf m(B_\varepsilon(w))
\le C\varepsilon^2\log(e/\varepsilon)
\tag{16}
\]

and full product-metric dimension two. Its proof in Section 10.1 uses
coupling to the finite seed-image density and the same-count bound.
It concerns \(\mathbf m\), not a specified ordinary fibre.

The high-variance closing attempt was to combine (16), the actual
dimension-one support from the companion note, and (10). Equations
(13)--(15) identify the unsupplied step: these moving fibres arise after
normalizing exponentially small cylinder masses. They are not a
positive-mass restriction of \(\mathbf m\). The BL approximation is
also not an entropy approximation at radius \(3^{-m_k}\). Full
dimension of the original measure therefore does not give the needed
dimension or entropy for these moving integer-diagonal restrictions.

A more targeted input was checked in Paper 9 v2, Theorem 16. If
\(s_B\,dm_3=\mathbf m\{B<R\le2B,Z_3\in dz\}\), it supplies, for
every fixed \(1<p<\infty\),

\[
\|s_B\|_p\le C_p B^{1-2/p}[\log(eB)]^{1-1/p}.
\tag{17}
\]

Cover the fixed-ratio shell in (13) by finitely many dyadic shells.
Hölder on the depth-\(m_k\) cylinder and (13) then yield only

\[
q_k^2\le C_{p,q_0}\,3^{m_k}
          [\log(e q_k)]^{p-1}.
\tag{18}
\]

This deduction keeps the moving real height and the exact ternary
precision. It is compatible with the elementary actual bound, since
\(q_k^2 3^{-m_k}=O_{q_0}((3/4)^k)\). Indeed the global real-tail
estimate already gives (18) without the logarithm. The stronger local
moment machinery does not improve the relevant exponential balance in
this application. No ordinary-point bound on the unaveraged limiting
ternary density is inferred from its \(L^p\) class.

For contrast, an early-height trace comparison such as
\(G(n)\le C D_{\lfloor\log_3n\rfloor}(n)\) on all sufficiently large
linear spikes would close escape: the right side divided by \(n\)
tends uniformly to zero because the ternary stationary law is nonatomic.
To justify the last statement, on a compact metric space a nonatomic
finite measure has maximum mass of radius-\(\varepsilon\) balls tending
to zero; otherwise a subsequence of centers converges and produces an
atom. Since \(3^{\lfloor\log_3n\rfloor}\le n\), apply this to (12).
The displayed early-height comparison is **not proved here**. The
actual trace available in (13) remains at \(m_k=k+O(1)\), and (5)
does not move that clock to \(\lfloor\log_3q_k\rfloor\).

## 6. What this pass establishes

The new proved deductions are (5)--(9), on the full actual path and its
common boundary, the fixed-root complete-path entropy statement in
Section 3, and the exact conditioning costs (14)--(15). They
connect the coherent boundary representation to the latest actual time
law without changing the original integer or hiding the depth.
The source-qualified regularity theorems were then applied with those
costs retained; the proposed contradiction did not result.

The remaining step in this attempted route is a same-root estimate at
an early enough precision, or an estimate on the moving physical fibre
that survives both the original-source conditioning and the changing
normalization in (11). Neither positive variance, a perfect support,
dimension-one support, nor the bulk dimension-two theorem supplies
that estimate by itself. This is the failure point of this particular
closing attempt, not a claim that every entropy or arithmetic route
is exhausted.

### Literature consulted at its primary statements

- Lyapunov Weaver, *Geometry, integer fibres, and dyadic equidistribution
  of the joint Collatz affine law*, **Paper 19 v2**, 22 October 2026,
  Sections 9.2 and 10.1, especially F3, S2 and S4--S6:
  <https://rstation.ai/problems/collatz/papers/19>.
  The displayed proof of the product-ball bound was read; the external
  counted-coalescence and trace constructions were not rebuilt.
- Lyapunov Weaver, *Ternary Syracuse laws: real localization, clock
  stability, and critical regularity*, **Paper 9 v2**, 25 October 2026,
  Appendix B, Theorem 16, B1--B2, and Appendix C, C1--C3:
  <https://rstation.ai/problems/collatz/papers/9>.
  The real-shell theorem was checked as a source-qualified input to the
  tested deduction (18); the full external mixing proof was not audited.
- The real-tail asymptotic used in (15) is the already instantiated
  Kesten--Goldie consequence at PR180
  `5e29f56f6d44669a8aa9134e5617b78d65c074c2`,
  `research/deep-machinery-20261122/RENEWAL_TRANSPORT.md`, Section 1.
  This is a reuse of that qualified input, not a new renewal theorem.

All new results in this note are written measure-theoretic arguments.
No Lean statement, assumption axiom, numerical experiment, or full
Collatz proof is claimed by this file.
