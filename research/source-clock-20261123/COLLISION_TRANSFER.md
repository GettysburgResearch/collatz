# Full local dimension does not supply the retained collision upper bound

Date: 2026-11-23.

**Status: exact analytic nonimplication and source-qualified target test.**
Section 1 is a model probability measure, not a Collatz path law and not a
counterexample to any theorem in this packet. It shows that even the stronger
conclusion of almost-everywhere *exact* local dimension one does not imply
the collision upper bound needed by the retained target. Section 2 tests
the low-profile restriction against that precise target law.

## 1. An exactly one-dimensional law can have the critical collision excess

Fix any `0 < theta < 1`, and put `beta = theta/2`. Let `mu` have density
on `(0,1)`

\[
f(x)=C_\beta x^{\beta-1}\bigl(\log(e/x)\bigr)^{1/4},\qquad
C_\beta^{-1}=\int_0^1
x^{\beta-1}\bigl(\log(e/x)\bigr)^{1/4}\,dx.
\tag{1}
\]

The normalizing integral is finite and positive. With `x = exp(-u)`, it is
`integral_0^infinity exp(-beta*u)(1+u)^(1/4) du`. Thus `mu` is a nonatomic
probability measure. For every `x` strictly between zero and one, its
density is continuous, finite, and positive. Consequently

\[
\mu([x-t,x+t])=2tf(x)+o(t),\qquad
\dim_{\rm loc}\mu(x)=1.                                      \tag{2}
\]

In particular the local dimension exists and equals one at `mu`-almost
every point. This is stronger than the upper-local-dimension conclusion
proved for the actual boundary in `BOUNDARY_OVERLAP.md`.

For `epsilon = 3^(-m)`, partition `[0,1)` into its usual ternary intervals
`I_(m,k) = [k*epsilon,(k+1)*epsilon)`. Since `beta < 1`, integration over
`[epsilon/2,epsilon]` gives

\[
\begin{aligned}
\mu(I_{m,0})
&\ge C_\beta\frac\epsilon2\,
  \epsilon^{\beta-1}\bigl(\log(e/\epsilon)\bigr)^{1/4}\\
&=\frac{C_\beta}{2}\epsilon^\beta
   \bigl(\log(e/\epsilon)\bigr)^{1/4}.
\end{aligned}                                                \tag{3}
\]

Keeping just this one cell in the collision sum therefore proves

\[
\begin{aligned}
\sum_k\mu(I_{m,k})^2
&\ge\frac{C_\beta^2}{4}\,
  3^{-\theta m}\sqrt{1+m\log3}\\
&\ge c_\theta\sqrt m\,3^{-\theta m}
\qquad(m\ge1),
\end{aligned}                                                \tag{4}
\]

where `c_theta = (C_beta^2/4)*sqrt(log 3) > 0`. In particular this collision
sum is not `O(3^(-theta*m))`.

The same example has **Shannon information dimension one** as well. Indeed,
`integral f*abs(log f)` is finite: after `x = exp(-u)`, the integrand is
bounded by a constant times `exp(-beta*u)*(1+u)^(5/4)`. Jensen's inequality
for the convex function `v*log v`, applied on each ternary cell, gives

\[
\int_0^1 f\log f\,dx
\ge\sum_k\mu(I_{m,k})\log\frac{\mu(I_{m,k})}{3^{-m}}
=m\log3-H_m(\mu).
\]

Since there are `3^m` cells,

\[
m\log3-\int_0^1 f\log f\,dx
\le H_m(\mu)\le m\log3,\qquad
\frac{H_m(\mu)}{m\log3}\longrightarrow1.                    \tag{4a}
\]

The example thus has a fixed probability law, a fixed ternary partition,
no atoms, exact local dimension one almost everywhere, and full lower and
upper Shannon information dimensions. These conclusions do not by
themselves remove the square-root collision excess, even when there is no
moving root or change of law. The lack of a uniform concentration estimate
matters independently of those additional Collatz issues.

For comparison with the precise target, use

\[
\theta=\frac{\Phi(\log_2 3)}{\log3},\qquad
\Phi(a)=a\log a-(a-1)\log(a-1).
\]

This is the exponent in PR #185,
`2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
`research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`,
Theorem 3 and equations (16), (20). The model does **not** represent its
ordinary residue marginal. It establishes that the boundary dimension
statement alone does not imply the requested analytic upper bound; any
successful transfer must use more of the actual arithmetic law.

## 2. The retained moving-root law keeps a positive high-profile mass

Retain exactly the ordinary source and law in the cited PR185 note:

\[
q_j=U^j(q_0),\quad v_j=\nu(q_j)\uparrow C_E>0,\quad
\pi_M=\frac1{M+1}\sum_{j=0}^M\delta_{q_j},
\]

\[
\zeta_{M,r}=(K_\nu^r)_*
\left(\frac1{M+1}\sum_{j=0}^M\delta_{q_{r+j}}\right).
\tag{5}
\]

Its exact retracing relation is

\[
\zeta_{M,r}\ge c_0\pi_M,\qquad
c_0=v_0/C_E>0,
\quad\text{for every finite }r.                              \tag{6}
\]

For the same source-qualified component construction, write `F = h_tr`.
The comparisons used in the boundary note are

\[
F(n)\ge\eta G(n),\qquad G(n)=n h(n),\qquad
h(n)\ge\delta\nu(n),
\tag{7}
\]

with fixed positive `eta, delta`. These comparisons are pinned in PR #180,
`04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
`research/high-variance-20261123/ANALYTIC_GLUING.md`, equations (2), (5),
and the subsection “Keeping the PR178 trace law distinct.”

Since `v_j >= v_0`, (7) gives the uniform spine bound

\[
F(q_j)\ge\eta\delta v_0q_j.                                  \tag{8}
\]

In a non-eventually-periodic positive orbit the `q_j` are distinct. A
distinct sequence of positive integers has only finitely many terms below
any fixed bound. Therefore, for every fixed `B`,

\[
\#\{j\ge0:F(q_j)\le B\}<\infty,
\qquad \pi_M\{F\le B\}\longrightarrow0.                     \tag{9}
\]

Equations (6) and (9) imply

\[
\boxed{\quad
\liminf_{M\to\infty}\inf_{r\ge0}
\zeta_{M,r}\{F>B\}\ge c_0>0.
\quad}                                                       \tag{10}
\]

This is a consequence of the *retained* forward-spine atoms. It is not a
counterexample produced by choosing another root distribution.

For each fixed root, the boundary proof obtains infinitely many inverse
depths with `F(X_r) <= B`. Equation (10) does not contradict that statement:
the root of `zeta_(M,r)` moves forward as the inverse clock increases. It
does show why one cannot discard the complement of the low-profile event
as an error tending to zero for the actual target law.

The independent composition estimate

\[
\mathsf P_q\{F(X_r)\le B,\ A_r\ge6r\}
\le \frac B{F(q)}(64/81)^r
\]

controls the accumulated clock at low-profile endpoints; it does not remove
the high-profile mass in (10). This clock estimate is developed separately
by the boundary lane in this packet.

## 3. The next usable bridge

A completion through the collision route must control the entire same-law
ordinary residue marginal in (5), or explicitly bound the collision of
its retained high-profile part. Neither an almost-sure real local-dimension
statement nor a bound on low-profile cylinders supplies that control.

The needed bound is still, along a compatible sequence of `M, m, r`,

\[
\operatorname{Col}_m(\zeta_{M,r})
=o\!\left(\sqrt m\,3^{-\theta m}\right),
\qquad m\longrightarrow\infty,\quad m^2=O(M).
\]

No such upper bound is proved here. Sections 1 and 2 separate the missing
uniform concentration from the distinct issue of retaining the actual
source and clock.
