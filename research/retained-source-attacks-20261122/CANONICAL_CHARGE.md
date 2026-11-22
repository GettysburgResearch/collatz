# Nonlinear canonical charge and the physical parameter family

Date: 2026-11-22.

**Status: source-qualified written deductions; the attempted closing argument
does not eliminate escape.** This continuation tests two nonlinear uses of the
actual canonical reference: relative entropy between its two inverse kernels,
and complete monotonicity of an all-positive parameter deformation. The first
has an exact finite budget. The second has an unavoidable pole at the least
ordinary integer in each hypothetical escaping component. Neither argument
provides a zero-charge theorem. No infinite result in this note is asserted to
have been formalized in Lean.

## 1. Frozen inputs and the question being attacked

Use the accelerated odd map

\[
U(n)=(3n+1)/2^{v_2(3n+1)}
\]

on positive odd ternary units that are not themselves periodic; kill forward
motion on entering a periodic vertex. The sources are:

| Source | Exact location and use |
|---|---|
| PR180, `a66a44c9bf058cd7efe1018827ddda9a13297a21` | `research/deep-machinery-20261122/BOUNDARY_RIGIDITY.md`, (1)--(3), (6), (16), (19)--(20): actual stationary reference, component clock masses and the canonical potential. |
| PR177, `e4ca639326bac73da8c2a698dec8a749e5efbe68` | `research/lean-exact-witness-global-20261121/LITERATURE_CANONICAL_ENERGY.md`, (1), (4)--(12): finite absolute canonical variation and its exact original sources. |
| PR175, `08fe1388ad63c758680b3695249aca319515c47d` | `research/lean-global-closure-20261121/machinery/EXACT_RUN_WEIGHT_COMMUTATOR.md`, (7)--(8), (27): the proposed run commutator has already been evaluated and retains the escape coefficient. |
| PR185, `980d40fc4afeaaf8f2a9256f322acf3e4568e013` | `research/multiple-attacks-20261122/STRICT_GREEN_VOLTERRA.md`, (1)--(2), (9)--(13), and `HARMONIC_KERNEL_FACTORIZATION.md`, (11)--(18): actual path occupation, the entire **linear** correction family, and the ordinary/critical harmonic correspondence. |

All predecessor-population and canonical-envelope qualifications of those
inputs are retained. This note does not reprove their existence theory.

The ordinary reference and critical reference satisfy

\[
L\nu=\nu,\quad
0<\delta\nu\le h\le\nu\le A,\quad
\lambda(n)=\frac{3n}{3n+1},\quad
d(n)=(1-\lambda(n))h(n),\quad D=\sum_n d(n)<\infty.
\tag{1}
\]

Let

\[
K(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)},\quad
K_h(q,n)=\mathbf1_{Un=q}\frac{\lambda(n)h(n)}{h(q)},
\quad g=d/\nu.
\tag{2}
\]

Both are genuine probability rows. The canonical potential is

\[
R=\sum_{j\ge0}K^jg=1-\lambda h/\nu,\qquad (I-K)R=g.
\tag{3}
\]

The killed forward composition operator is denoted by \(C\). The new
upstream variation theorem supplies

\[
\sum_n\nu(n)|R(n)-CR(n)|<\infty.
\tag{4}
\]

Fix a hypothetical escaping ordinary component \(E\). Its actual integer
clock obeys \(\ell(Un)=\ell(n)+1\), and every clock level has mass

\[
\sum_{\ell(n)=r}\nu(n)=c_E>0.
\]

For any forward ray \(q_k\) in this component,

\[
\nu(q_k)\longrightarrow c_E,\qquad
R(q_k)\longrightarrow F_E:=D_E/c_E,
\qquad D_E=\sum_{n\in E}d(n)>0.
\tag{5}
\]

The central goal is to exclude this positive ordinary component. The latest
PR175 already shows why a bound obtained just by dropping the run-weight
commutator cannot do so. The following calculations instead keep a nonlinear
change of measure and the whole physical path.

## 2. An exact finite relative-entropy budget

Put

\[
u=1-R=\lambda h/\nu,\qquad \delta_0=3\delta/4.
\]

Since \(\lambda(n)\ge3/4\),

\[
\delta_0\le u\le1,\qquad
Ku=u+g=u/\lambda,
\qquad K_h(q,n)=\lambda(q)K(q,n)\frac{u(n)}{u(q)}.
\tag{6}
\]

These equalities use the actual canonical functions; an arbitrary harmonic
surrogate would not suffice. Define the row divergence using natural logs:

\[
J(q):=D_{\rm KL}\bigl(K(q,\cdot)\Vert K_h(q,\cdot)\bigr).
\]

The two rows have the same support, and their likelihood ratios are bounded
above and below by positive constants from (6). Consequently the countable
entropy sum is absolutely finite. Direct substitution gives

\[
\boxed{
J(q)=(I-K)\log u(q)-\log\lambda(q)
=\log Ku(q)-K\log u(q)\ge0.}
\tag{7}
\]

The last inequality is the elementary concavity inequality for the logarithm.
No stationary-entropy classification is imported.

### Justifying the infinite signed sum

The logarithm is \(\delta_0^{-1}\)-Lipschitz on \([\delta_0,1]\).
On this closed escaping component, (4) therefore implies

\[
\sum_{n\in E}\nu(n)|\log u(Un)-\log u(n)|<\infty.
\tag{8}
\]

The same bound, after averaging incoming edges, controls
\(\sum_E\nu|(I-K)\log u|\). Thus the signed summation below is licensed;
it is not subtraction of two possibly infinite integrals of \(\log u\).

Let \(\bar\psi_r=c_E^{-1}\sum_{\ell(n)=r}\nu(n)\psi(n)\), with
\(\psi=\log(1-R)\). The source formula for the level mean of \(R\) gives
\(\bar R_r\to0\) as \(r\to-\infty\). Since
\(|\log(1-R)|\le R/\delta_0\), this proves \(\bar\psi_r\to0\) there.
As \(r\to+\infty\), the single forward state \(q_r\) has mass
\(\nu(q_r)\to c_E\). Boundedness of \(\psi\) and (5) imply
\(\bar\psi_r\to\log(1-F_E)\). Also
\(\overline{K\psi}_r=\bar\psi_{r-1}\). Telescoping finite clock intervals
and using (8) now gives

\[
\sum_{q\in E}\nu(q)(I-K)\log u(q)=c_E\log(1-F_E).
\tag{9}
\]

Write

\[
H_E:=\sum_{n\in E}\nu(n)\log\left(1+\frac1{3n}\right).
\]

This is finite: (1) gives
\(d(n)\ge\delta\nu(n)/(4n)\), and hence
\(H_E\le\tfrac13\sum_E\nu(n)/n\le4D_E/(3\delta)\).
Equations (7)--(9) prove the exact budget

\[
\boxed{
\sum_{q\in E}\nu(q)J(q)
=H_E+c_E\log(1-F_E)<\infty.}
\tag{10}
\]

In particular,

\[
\boxed{-c_E\log(1-F_E)\le H_E.}
\tag{11}
\]

This is a nonlinear quantitative restriction on the actual component. It
does not make \(F_E\) zero: its right side is a positive finite ordinary
height cost, not an error known to vanish. Nor is \(J\) a divergence between
the laws at distinct arithmetic siblings. It compares the stationary and
critical inverse laws at the **same** root. Applying an entropy-growth theorem
for sibling mixing to this different quantity would drop that distinction.

## 3. A probability law on whole ordinary paths

The parameter-family test can be made on actual ordinary paths, without
assuming a finite invariant measure on the full component.

Normalize each synchronous level by \(c_E\). Choose the state at level zero
with probability \(\nu(n)/c_E\). Its positive-clock future is deterministic;
sample its negative-clock past with the inverse kernel \(K\). Harmonicity and
the exact level masses make these finite-dimensional probabilities
consistent. They define a probability law \(\Pi_E\) on two-sided paths
\((Q_r)_{r\in\mathbb Z}\) satisfying

\[
UQ_r=Q_{r+1},\qquad
\Pi_E(Q_r=n)=\nu(n)/c_E\quad(\ell(n)=r).
\tag{12}
\]

There are no repeated states. In particular,

\[
\boxed{\Pi_E(n\text{ lies on the path})=\nu(n)/c_E.}
\tag{13}
\]

This is a law on ordinary integers within the same component, not a law
obtained by freely choosing independent valuations. Every finite interval
of a sampled path is an actual finite simple forward path. The pinned
occupation bound therefore extends monotonically to the entire path:

\[
\#\{r:Q_r\le X\}\le5X^{39/40},\qquad
\sum_{r\in\mathbb Z}\frac1{Q_r}\le200.
\tag{14}
\]

The two-sided extension uses increasing finite clock intervals; it does not
claim that an inverse ray is the forward orbit of one starting integer.

## 4. The all-positive physical family and its boundary coefficient

For real \(z\ge0\), use the physical deformation

\[
\lambda_z(n)=\frac{3n}{3n+z}.
\tag{15}
\]

Unlike \(1-z/(3n+1)\), this multiplier stays positive at every positive
parameter. Define its component boundary coefficient by

\[
\boxed{
B_E(z)=c_E\,\mathbb E_{\Pi_E}
\prod_{r\in\mathbb Z}\lambda_z(Q_r).}
\tag{16}
\]

The product converges by (14). It is positive for every finite \(z\ge0\).
For each sampled path it is the Laplace transform of a sum of independent
exponential variables with rates \(3Q_r\). This conditional sum is finite
almost surely because its mean is at most \(200/3\). Averaging over paths
shows directly that \(B_E\) is completely monotone; in particular
\((-1)^jB_E^{(j)}(z)\ge0\) for \(z>0\). The auxiliary exponentials are
only a representation of the displayed product. They do not change the
ordinary Collatz path law.

For clarity, (16) agrees with the boundary value of the physical harmonic
family. For a fixed root \(q\), let

\[
h_z(q)=\nu(q)\,\mathbb E_q^K
\prod_{i\ge1}\lambda_z(X_i),
\tag{17}
\]

where \(X_i\) are its actual inverse states; the starting root is excluded.
The Markov property gives \(h_z=L(\lambda_z h_z)\).
On the event \(Q_k=q_k\), the product over levels below \(k\) has exactly
the conditional law in (17). That event has probability
\(\nu(q_k)/c_E\to1\). Bounded convergence for (16) and the vanishing
remaining level mass give

\[
\lim_{k\to\infty}h_z(q_k)=B_E(z).
\tag{18}
\]

At \(z=1\), (17) is the supplied \(h\). This also follows pointwise without
any additional Banach-space membership: write \(T=L\lambda\). The imported
identity \(\nu-h=\sum_{j\ge1}L^j d\) gives

\[
0\le T^k\nu-h=T^k(\nu-h)
\le\sum_{j\ge k+1}L^j d\longrightarrow0
\]

at each fixed root, while the finite inverse-path expectation defining
\(T^k\nu\) decreases to (17). Therefore

\[
\boxed{B_E(0)=c_E,\qquad B_E(1)=c_E-D_E=c_E(1-F_E).}
\tag{19}
\]

Differentiation at zero is justified by the uniform bound (14), and (13)
gives a further exact physical identity:

\[
\boxed{B'_E(0)=-\frac13\sum_{n\in E}\frac{\nu(n)}n.}
\tag{20}
\]

Jensen's inequality applied to the product at \(z=1\) recovers (11):
its expected logarithm is \(-H_E/c_E\). More explicitly, if \(P\) denotes
that path product, define the probability tilt
\(d\widetilde\Pi_E/d\Pi_E=P/\mathbb E P\). Then

\[
c_E D_{\rm KL}(\Pi_E\Vert\widetilde\Pi_E)
=H_E+c_E\log(1-F_E)
=\sum_{q\in E}\nu(q)J(q).
\tag{20a}
\]

The entropy budget and the physical family therefore measure the same
surviving ordinary boundary through compatible nonlinear formulas.

## 5. The least ordinary state forces a nonremovable pole

An ambitious possible completion was to combine complete monotonicity with
an entire continuation of order below one. This is not valid for the
physical family (16). Its first pole can be identified exactly.

Let \(m=\min E\), an actual ordinary positive integer. On a path that avoids
\(m\), all states are at least \(m+2\). On a path that visits \(m\), it
visits it exactly once; every other state is also at least \(m+2\).
Separate these two events in (16):

\[
B_E(z)=A_E(z)+\frac{3m}{z+3m}\,C_E(z),
\tag{21}
\]

where

\[
\begin{aligned}
A_E(z)&=c_E\mathbb E\left[
\mathbf1_{\{m\text{ absent}\}}\prod_n\lambda_z(n)\right],\\
C_E(z)&=c_E\mathbb E\left[
\mathbf1_{\{m\text{ present}\}}\prod_{n\ne m}\lambda_z(n)\right].
\end{aligned}
\]

The same product estimates first give a holomorphic continuation of (16)
throughout \(\operatorname{Re}z>-3m\): on compact subsets the finitely many
small denominators are bounded away from zero, and the remaining logarithmic
tails are uniformly controlled by (14). Both functions in (21) are
holomorphic in a neighborhood of \(-3m\), so (21) continues that original
positive-parameter function across the boundary except at the displayed
pole. To justify
this without exchanging an uncontrolled product and expectation, take
\(|z+3m|<3\). Every remaining possible pole \(-3n\), \(n\ge m+2\),
stays outside this disk. On its compact subsets,
\(\log|\lambda_z(n)|\) is bounded above by \(C_m/n\), uniformly over
the sampled paths; (14) gives a common integrable constant for the product.
The height tail in the same occupation bound gives uniform convergence of
the product after truncating to heights at most \(X\). Each such product
is a finite rational function with no pole in the disk. Uniform limits
and bounded expectation give the claimed holomorphy.

At the pole, every remaining factor is \(n/(n-m)>1\). Equation (13)
therefore proves

\[
\boxed{
\begin{aligned}
\operatorname*{Res}_{z=-3m}B_E(z)
&=3m c_E\mathbb E\left[
\mathbf1_{\{m\text{ present}\}}
\prod_{n\ne m}\frac{n}{n-m}\right]\\
&\ge3m\nu(m)>0.
\end{aligned}}
\tag{22}
\]

The residue is finite. Indeed, for \(n\ge m+2\),

\[
-\log(1-m/n)\le\frac{m(m+2)}{2n},
\]

so the product in (22) is at most \(\exp(100m(m+2))\) by (14).
Thus \(-3m\) is a **nonremovable simple pole of the actual component
boundary coefficient**, not merely a pole of a diagonal formula that
might cancel after taking the boundary value.

The separate [analytic parameter calculation](ANALYTIC_PARAMETER.md) sharpens
the entire growth bound for the strict correction and tests the same-source
log-convexity needed in that approach. The entire correction in PR185
instead deforms transport by
\(1-z/(3n+1)\). Its positivity is available only on a bounded positive
parameter interval. It cannot be substituted for (15) while retaining
complete monotonicity for all \(z\ge0\). Conversely, the all-positive
physical family has the pole (22), so it cannot be assigned the entire
continuation of that different correction. This identifies the exact
obstruction to the proposed complex-analytic completion.

## 6. Outcome

The nonlinear attack yields the finite exact entropy identity (10), the
whole-path representation (16), its physical normalization and first
derivative (19)--(20), and the strictly positive pole residue (22).
They retain the same actual canonical sources and the same escaping
component throughout.

The entropy budget allows a positive \(F_E\); the physical parameter family
has precisely the singularity that prevents the proposed entire-function
contradiction. No sibling lower bound, vanishing of \(D_E\), elimination of
an escaping component, or exclusion of a nontrivial positive cycle has been
obtained. The periodic states were killed before any of these constructions.
