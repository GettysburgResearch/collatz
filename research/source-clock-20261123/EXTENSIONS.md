# Positive lower information dimension of the actual real law

Date: 2026-11-23.

**Status: SOURCE-QUALIFIED written theorem.** The actual canonical real
boundary has a strictly positive lower Shannon information dimension. This
is an all-scale statement about mean information, stronger in that direction
than merely having upper local dimension one. It does not assert a positive
lower local dimension or an all-scale pointwise mass bound.

The proof combines the retained selection identity with a summable tail
bound for the actual valuation clock at low-profile endpoints. It requires
no global valuation moment, lower return-frequency assertion, or rate in
the selection theorem. The infinite result is not claimed as Lean checked.

## 1. Notation and exact dependencies

Use the ordinary root, trace kernel, path variables, and constants of
[BOUNDARY_OVERLAP.md](BOUNDARY_OVERLAP.md). The independently reviewed
version used here has SHA-256
`086640abba47b80e1c6d9baee8b2e6bb003e8fd320fe5afb2cd202e7b10838c4`.
In particular,

\[
 \mathsf P_q(W_r=w)=a_r\frac{F(X_r)}{F(q)},\qquad
 a_r=3^r2^{-A_r},\qquad
 R_r\uparrow R,
\]

and every low-profile prefix \(F(X_r)\le B\) has its entire real image
inside \([R_r,R_r+Da_r^\rho]\), with \(\rho=1/40\) and
\(D=D(q,B)\ge1\).

Decrease the permitted positive floor \(\alpha\), if necessary, so that
\(0<\alpha\le1\). Fix \(B>2\), and define

\[
 \theta=\frac{1-2/B}{2/\alpha-2/B}\in(0,1),\qquad
 p_B=\frac{3\alpha}{64B},\qquad
 \kappa=-\log(1-p_B)>0,\qquad
 \lambda_6=\log(64/3)>0.
 \tag{E1}
\]

Write \(L_N=\#\{0\le j<N:F(X_j)\le B\}\). The finite prefix
information inequality from the companion note is

\[
 a_r\le\frac{F(q)}\alpha e^{-\kappa L_r}.
 \tag{E2}
\]

The new low-profile clock estimate in Section 2 was independently derived
by the target-descent attack during review of the companion theorem. All
trace, positive-floor, and path-packing qualifications in that theorem
remain attached. Its selection input may also be read from PR175,
`8870528daa6a13cc941d602e578e35c8bfa4bf4f`,
`research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`,
Section 5, equation (16), which provides the stronger mean-absolute
correlation statement under its pinned ordinary trace input. That statement
is not an \(L^1\) assertion about the random sample-path averages.

For a boundedly supported real probability \(\mu\), let

\[
 H_k(\mu)=-\sum_{j\in\mathbb Z}
    \mu([j2^{-k},(j+1)2^{-k}))
       \log\mu([j2^{-k},(j+1)2^{-k})),
 \quad
 \underline d_I(\mu)=\liminf_{k\to\infty}
       \frac{H_k(\mu)}{k\log2}.
 \tag{E3}
\]

These entropies are finite because the support is bounded. The logarithms
are natural. The information dimension in (E3) concerns the averaged
information of a fine partition; it is distinct from the almost-sure lower
local dimension.

## 2. The actual valuation clock has a summable tail at low-profile nodes

For \(r\ge1\), there are \(\binom{A-1}{r-1}\) words of \(r\)
positive integers with total \(A\). Actual legal inverse words are a
subset. Their low-profile cylinder probabilities therefore give

\[
 \mathsf P_q(F(X_r)\le B,A_r\ge6r)
 \le\frac{B}{F(q)}3^r
       \sum_{A\ge6r}\binom{A-1}{r-1}2^{-A}.
\]

Use \(2^{-A}=(2/3)^A(3/4)^A\) and the elementary generating sum

\[
 \sum_{A\ge r}\binom{A-1}{r-1}(3/4)^A=3^r.
\]

It follows that

\[
 \boxed{\mathsf P_q(F(X_r)\le B,A_r\ge6r)
 \le\frac{B}{F(q)}\left(\frac{64}{81}\right)^r.}
 \tag{E4}
\]

The event restriction is essential: (E4) is not a tail estimate for the
unrestricted canonical clock. In particular, almost surely every sufficiently
late low-profile endpoint has \(A_r<6r\). Its prefix multiplier then
satisfies \(a_r\ge(3/64)^r\).

## 3. A positive amount of mass has a good return at every large horizon

Selection with the entire path space as its event gives

\[
 \frac1N\sum_{j<N}\mathbb E_q g(X_j)\longrightarrow1.
\]

Since \(g\le2/B+(2/\alpha-2/B)\mathbf1_{F\le B}\),

\[
 \liminf_{N\to\infty}\frac{\mathbb E_q L_N}{N}\ge\theta.
 \tag{E5}
\]

Put \(b=\theta/2\), and let
\(\mathcal E_N=\{L_N\ge bN\}\). Since \(0\le L_N\le N\),
\(\mathbb E L_N/N\le b+(1-b)\mathsf P_q(\mathcal E_N)\). Thus

\[
 \liminf_N\mathsf P_q(\mathcal E_N)
 \ge p_*:=\frac{\theta-b}{1-b}
          =\frac{\theta}{2-\theta}>0.
 \tag{E6}
\]

On \(\mathcal E_N\), choose the latest low-profile time \(r<N\).
For all sufficiently large \(N\),

\[
 F(X_r)\le B,\qquad L_r=L_N-1\ge bN-1,
 \qquad bN/2\le r<N.
\]

Consequently, with constants
\(C_q=(F(q)/\alpha)e^\kappa\) and \(\beta=\kappa b\),

\[
 a_r\le C_qe^{-\beta N}.
 \tag{E7}
\]

Union-bounding (E4) over \(bN/2\le r<N\) costs an exponentially small
probability. Outside that exceptional event, the chosen endpoint also has
\(A_r<6r\), and its shadow radius \(t_r=Da_r^\rho\) lies in the
deterministic range

\[
 e^{-\rho\lambda_6N}\le t_r
 \le D C_q^\rho e^{-\rho\beta N}.
 \tag{E8}
\]

The lower bound uses \(D\ge1\), \(r\le N\), and
\(a_r\ge(3/64)^r\). This is a statement holding on a positive-probability
event at each large horizon. It does not assert a positive lower frequency
of low-profile visits on each sample path.

## 4. Full real ball masses are small on a set of positive mass

Fix any probability \(\eta\) on the real line and \(0<s<1\).
The companion heavy-cell estimate, at each depth \(r\) and each total
\(A\), is

\[
 \mathsf P_q(F(X_r)\le B,A_r=A,
             \eta([R-t,R+t])>t^s)
 \le\frac{8B}{F(q)}t^{1-s},
 \quad t=D(3^r2^{-A})^\rho,
 \tag{E9}
\]

provided \(3^r2^{-A}\le1\). Sum (E9) over every total satisfying
\(3^r2^{-A}\le C_qe^{-\beta N}\), and then over \(1\le r<N\).
The geometric sum gives an exceptional probability at most

\[
 \frac{8B}{F(q)}
 \frac{N D^{1-s} C_q^{\rho(1-s)}}{1-2^{-\rho(1-s)}}
 e^{-\rho\beta(1-s)N}.
 \tag{E10}
\]

This tends to zero exponentially up to its factor \(N\), independently
of the choice of reference probability \(\eta\). On \(\mathcal E_N\)
outside this exception and the clock exception from (E4), equations
(E8)--(E10) yield

\[
 \eta([R-e^{-\rho\lambda_6N},R+e^{-\rho\lambda_6N}])
 \le (D C_q^\rho)^s e^{-s\rho\beta N}.
 \tag{E11}
\]

Thus the event in (E11) has lower limiting \(\mathsf P_q\)-probability
at least \(p_*\). No rate in the selection theorem was needed: its only
use was the expectation bound (E5).

## 5. An explicit positive lower information dimension

Take \(\eta=\mu_q=\mathcal L_{\mathsf P_q}(R)\), and set

\[
 k_N=\left\lceil\frac{\rho\lambda_6}{\log2}N\right\rceil.
\]

The dyadic cell of mesh \(2^{-k_N}\) containing \(R\) is contained
in the ball in (E11). On that event its information is therefore at least

\[
 s\rho\beta N-s\log(D C_q^\rho).
\]

Information is nonnegative elsewhere. Taking expectations, using (E6) and
the vanishing exceptional probabilities, gives

\[
 \liminf_N\frac{H_{k_N}(\mu_q)}{k_N\log2}
 \ge\frac{p_*s\beta}{\lambda_6}.
\]

Here \(0<\rho\lambda_6/\log2<1\), so \(k_N\) increases by zero or
one at each step and tends to infinity. It takes every sufficiently large
integer value. The displayed inequality therefore controls the full
liminf in (E3), rather than only a subsequence. Finally let \(s\uparrow1\):

\[
 \boxed{\underline d_I(\mu_q)\ge
 d_B:=\frac{\kappa\theta^2}
             {2(2-\theta)\log(64/3)}>0.}
 \tag{E12}
\]

The bound is independent of the fixed ordinary root \(q\). The onset may
depend on \(q\); the finite constants \(D\) and \(C_q\) disappear after
division by the resolution. The same lower bound holds using arbitrary
uniform meshes: partitions with comparable mesh sizes have conditional
entropy bounded by an absolute constant, since one interval intersects
only a bounded number of intervals of the other partition.

### Fixed affine changes, absolutely continuous reweighting, and the component law

A fixed nonzero affine change of the real coordinate preserves (E3). This
follows from the same bounded cell-intersection argument, after shifting
the dyadic level by a constant depending on the affine slope.

The **same** coefficient \(d_B\) also transfers to every fixed path
probability \(\mathsf Q_q\ll\mathsf P_q\), without a loss from a
likelihood comparison. Write \(\mathsf Q_q=w\mathsf P_q\), where
\(w\ge0\) and \(\mathbb E_qw=1\). The full-event selection identity
extends first to bounded simple functions, then to the integrable density
\(w\) by truncation:

\[
 \mathbb E_{\mathsf Q_q}\frac1N\sum_{j<N}g(X_j)
 =\mathbb E_q\!\left[w\frac1N\sum_{j<N}g(X_j)\right]
 \longrightarrow1.
 \tag{E13}
\]

The averages are uniformly bounded, which bounds the truncation error by
\((2/\alpha)\mathbb E_q(w-\min\{w,m\})\), independently of \(N\).
Thus (E5)--(E6) hold under \(\mathsf Q_q\) with the same \(\theta\)
and \(p_*\). Equations (E2), (E7), and (E8) are pathwise statements.
The exceptional probabilities from (E4) and (E10) tend to zero under
\(\mathsf P_q\), and hence under the fixed absolutely continuous
\(\mathsf Q_q\). No exponential rate after reweighting is needed.
Run (E9)--(E11)
with reference measure \(\eta=\widetilde\mu_q\), the real marginal of
\(\mathsf Q_q\), and repeat the entropy argument. It proves

\[
 \boxed{\underline d_I(\widetilde\mu_q)\ge d_B.}
 \tag{E14}
\]

The changed path law need not be Markov for this transfer; its density is
fixed, rather than chosen separately at each resolution. In particular,
(E14) also holds after conditioning on any fixed positive-probability path
event. The retained critical and ordinary conditional path laws are covered
by the pinned bounded comparisons. For example, if
\(\eta_0G\le F\le2G\), their likelihood upper bounds relative to
the trace law can be taken as \(2/\eta_0\) and
\(2/(\eta_0\delta)\), respectively. Their precise sizes are not needed
for (E14).

For a whole component law, condition at clock zero. Its real boundary
distribution is a countable mixture of the corresponding fixed-root
marginals, changed by the exact affine coordinate
\(Z=(q-R)/\chi(q)\). Entropy is concave under this mixture. For any
finite selection of roots of total weight \(w\), discard the nonnegative
entropy contribution of the remaining mixture and apply (E12) or (E14)
to those finitely many fixed affine coordinates. The lower information
dimension is at least \(w\) times the root-uniform lower bound. Let
\(w\uparrow1\).

In particular, the actual common ordinary boundary law \(\mu_E\) obeys

\[
 \boxed{\underline d_I(\mu_E)\ge d_B>0.}
 \tag{E15}
\]

The corresponding whole critical and trace laws have the same lower bound.
This transfer retains the original conditional path laws and their
likelihood factors; it does not replace the component law by a convenient
measure on its support.

## 6. What this does and does not supply for the closing attack

Equations (E12) and (E15) force linear growth of the real partition entropy
at **every sufficiently fine scale in the liminf sense**. The earlier
upper-local-dimension theorem supplied fine scales along individual paths;
the expectation and clock-tail argument here obtains an all-scale mean
conclusion for the actual probability law.

The explicit coefficient is only a positive one. The proof supplies neither
full lower information dimension nor the actual ternary collision upper
bound needed to oppose PR185's critical lower bound. In particular, (E11)
controls a positive part of the boundary probability at each resolution;
it is not a uniform upper bound on all cell masses. An uncontrolled remaining
part can dominate collision probability. The retained original-source clock
and the conversion from real boundary information to the actual ternary
inverse-time law still need a further argument.
