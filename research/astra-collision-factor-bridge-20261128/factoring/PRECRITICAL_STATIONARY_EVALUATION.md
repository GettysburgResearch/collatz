# Evaluating the rare grade-selected trace at moving precritical clocks

Date: 2026-11-28. **Positive, source-qualified relative asymptotic.** This
note evaluates the one-copy stationary selector far beyond the initial
binary-information horizon, all the way to clocks approaching the median
from outside its Gaussian window. The median itself remains open.

The Brownian height theorem is prior work of David Leen. The deduction here
applies its full endpoint continuity to the same joint stationary selector
constructed in this pass. No new Brownian theorem, fresh-bit law beyond
the binary horizon, or full Collatz proof is claimed.

## 1. The exact imported primary input

The original source is [Leen, Brownian motion in Collatz orbits,
version 2](https://doi.org/10.5281/zenodo.23269488). The inspected TeX has
SHA-256 **211bc4fe107b3821e510486be28cf53f69751f71394582822faf385d09561e37**.
Its main fate-clock theorem and the complete *Height process* proposition
and proof were read directly. The latter is labelled prop:height, in the
section *All integers, the shortcut clock, and the height process*. This
pass does not rebuild or formally certify that imported development.

Put
\[
d=\log(4/3),\qquad \mu=2/d,\qquad
\sigma^2=2(\log3)^2/d^3,\qquad c_*=\sigma/\mu.
\tag{1}
\]

Let \(\tau_n\) be the first global-minimum date of the ordinary source \(n\),
\(L_n=\log n\), and \(\ell_n(j)=\log T^j(n)\). The original proposition gives
\[
\mathcal D_n(s)=
\frac{\ell_n(\lfloor s\tau_n\rfloor)-L_n+\lfloor s\tau_n\rfloor/\mu}
{c_*\sqrt{L_n}}
\ \Longrightarrow B(s),\qquad 0\le s\le1,
\tag{2}
\]
in the **uniform topology on the entire interval**, jointly with the
minimum label and
\[
\frac{\tau_n-\mu L_n}{\sigma\sqrt{L_n}}\Longrightarrow B(1),
\qquad \frac{\tau_n}{\mu L_n}\longrightarrow1.
\tag{3}
\]
The Brownian endpoint in (3) is the same one as in (2).

The primary proof compares the height process to the capped passage process
uniformly, including time 1. This licenses the moving evaluation below;
separate fixed-time central limit theorems would not be enough. Its sample
\([2,X]\) can be replaced by \([1,X]\) at error at most \(1/X\).

## 2. A finite correction bound before the minimum

Write \(a_j(n)\) for the number of odd departures before native date \(j\).
The exact product gives
\[
\ell_n(j)-L_n+j/\mu
=\log3\,(a_j(n)-j/2)+C_j(n),\qquad
C_j(n)=\sum_{\substack{i<j\\T^i(n)\ {\rm odd}}}
\log\left(1+\frac1{3T^i(n)}\right).
\tag{4}
\]

All states before the first minimum are distinct: a repetition would put
the remaining trajectory on a cycle whose minimum had already been visited.
Thus, for \(1\le j\le\tau_n\),
\[
0\le C_j(n)\le\frac13\sum_{m=1}^j\frac1m
\le\frac{1+\log j}{3}.
\tag{5}
\]
This is \(o(\sqrt{\log X})\) at logarithmic clocks before the minimum. No
uniform orbit-packing theorem or assumption about the postminimum future
is needed for (5).

## 3. A moving approach to the critical clock

Let \(w_X\) be any deterministic positive function with
\[
w_X\longrightarrow\infty,\qquad w_X=o(\sqrt{\log X}),
\qquad
h_X=\left\lfloor\mu\log X-w_X\sqrt{\log X}\right\rfloor.
\tag{6}
\]

**Theorem 1.** For a uniform ordinary source through \(X\),
\[
\boxed{\displaystyle
G_X(n):=\frac{2(a_{h_X}(n)-h_X/2)}{\sqrt{h_X}}
\Longrightarrow N(0,1).}
\tag{7}
\]

**Proof.** Uniform sampling gives \(\log X-L_n=O_P(1)\), since its upper
tail is at most \(e^{-t}+O(1/X)\). Equation (3) therefore implies
\(\tau_n=\mu\log X+O_P(\sqrt{\log X})\). Hence
\(\Pr(h_X<\tau_n)\to1\), while \(h_X/\tau_n\to1\).

Uniform-topology convergence to a continuous Brownian path allows the
random evaluation point \(h_X/\tau_n\):
\[
\mathcal D_n(h_X/\tau_n)\Longrightarrow B(1)
\tag{8}
\]
on the event of probability \(1-o(1)\). To see this without a rate, bound
the difference from \(\mathcal D_n(1)\) by the modulus of continuity at
\(\delta\), outside the event \(|1-h_X/\tau_n|>\delta\), then take
\(X\to\infty\) followed by \(\delta\downarrow0\).

On that event, (4) gives
\[
G_X(n)=
\frac{2c_*\sqrt{L_n}}{\log3\sqrt{h_X}}
\mathcal D_n(h_X/\tau_n)
-\frac{2C_{h_X}(n)}{\log3\sqrt{h_X}}.
\tag{9}
\]
The last term tends to zero by (5). The first coefficient tends to one
because \(h_X\sim\mu\log X\) and \(2c_*/(\log3\sqrt\mu)=1\).
This proves (7). ∎

The theorem permits arbitrarily slow divergence of \(w_X\). It does not
give a convergence rate uniform over all choices of that function, and the
function cannot be chosen after seeing the sampled integer.

## 4. The relative stationary selector is actually evaluated

Use the fair joint stationary seed and one-copy selector \(K_{h,X}\) from
[STATIONARY_COLLISION_CONSUMER.md](STATIONARY_COLLISION_CONSUMER.md).
Its future grade \(A_h\) belongs to the same path as its real and ternary
coordinates. Put \(\rho_X=X/2^{h_X}\). Eventually \(X\le2^{h_X}\), so
\(K_{h_X,X}\) is an indicator with probability exactly \(\rho_X\).

The full-law stationary transfer yields
\[
\sup_t\left|
\frac{\Pr\{K_{h_X,X}=1,\
2(A_{h_X}-h_X/2)/\sqrt{h_X}\le t\}}{\rho_X}
-\Pr\{G_X(n)\le t\}\right|
\le \frac{eC_0\log X}{X},
\tag{10}
\]
where the explicit absolute \(C_0\) is given in the companion note.
Convergence to a continuous Gaussian distribution is uniform at the
distribution-function level. Thus
\[
\boxed{\displaystyle
\sup_{t\in\mathbb R}\left|
\frac{\Pr\{K_{h_X,X}=1,\
2(A_{h_X}-h_X/2)/\sqrt{h_X}\le t\}}{\rho_X}
-\Phi(t)\right|\longrightarrow0.}
\tag{11}
\]

In particular, for every fixed \(z>0\),
\[
\boxed{\displaystyle
\Pr\!\left\{K_{h_X,X}=1,\
A_{h_X}\le\left\lfloor h_X/2-z\sqrt{h_X}/2\right\rfloor\right\}
=[\Phi(-z)+o(1)]\,\frac X{2^{h_X}}.}
\tag{12}
\]

This is an error \(o(\rho_X)\), not merely \(o(1)\). Its probability scale is
\[
\rho_X=X^{1-\mu\log2}
\exp\bigl((\log2)w_X\sqrt{\log X}+O(1)\bigr),
\tag{13}
\]
with leading power approximately \(X^{-3.8188}\). It lies far beyond
complete binary-cylinder sampling. The uniformity in (11) is absolute
after division by \(\rho_X\); it is not a relative Gaussian-tail estimate
when \(|t|\) grows.

The same argument at any fixed \(h_X\sim c\mu\log X\), \(0<c<1\), uses
\(B(c)/\sqrt c\) and gives the same Gaussian law. Those fixed precritical
consequences of the existing height theorem are not claimed as new grade
laws. The point here is the moving approach (6) and its exact rare-selector
normalization.

## 5. An explicit positive bound inside earlier critical windows

For a fixed \(u\in\mathbb R\), take an integer clock
\[
h_X(u)=\mu\log X+\sigma u\sqrt{\log X}+o(\sqrt{\log X}).
\tag{14}
\]
Let \(G_X\) now use that clock. On \(\tau_n>h_X(u)\), the same bounded
correction and joint endpoint continuity give, for each fixed \(t\),
\[
\boxed{\displaystyle
\Pr\{\tau_n>h_X(u),\ G_X(n)\le t\}
\longrightarrow \Pr\{u<B(1)\le t\}
=(\Phi(t)-\Phi(u))_+.}
\tag{15}
\]
The joint inequalities can be approximated away from their Gaussian
boundary points, which have zero probability. This is a statement about
the original ordinary paths, with no independent future substituted.

Since \(\Pr(\tau_n\le h_X(u))\to\Phi(u)\), it follows that
\[
(\Phi(t)-\Phi(u))_+
\le\liminf_X\Pr(G_X\le t)
\le\limsup_X\Pr(G_X\le t)
\le(\Phi(t)-\Phi(u))_++\Phi(u).
\tag{16}
\]
The stationary grade-selected trace divided by \(X/2^{h_X(u)}\) has these
same bounds. If \(u<-z\), its negative-grade coefficient is therefore
between the explicit positive lower bound
\(\Phi(-z)-\Phi(u)\) and \(\Phi(-z)\).

At the median \(u=0\) and the required negative threshold \(t=-z\),
the survivor contribution (15) is zero. The entire desired negative tail
comes from sources that have already reached their minimum. The moving
precritical trace has been evaluated at its relative scale, but its
extension to the median requires their genuine ordinary postminimum
futures. That is exactly the remaining obligation in
[CRITICAL_GRADE_TAIL.md](../arithmetic/CRITICAL_GRADE_TAIL.md).

## 6. The closing side of a fixed critical window

There is a sharper description on the other side of the boundary in
(15). Retain the cycle notation of
[CRITICAL_GRADE_TAIL.md](../arithmetic/CRITICAL_GRADE_TAIL.md):
\(d_C\) is the density of the basin of the genuine positive cycle
\(C\), \(\alpha_C\) its odd-state fraction, and
\[
\delta_C=\log2-\alpha_C\log3,\qquad
r_C=\delta_C/(\log2-\tfrac12\log3)>0.
\tag{17}
\]
In addition to the primary height input, use the uniform distinct-orbit
packing estimate explicitly inspected and cited in that companion note.
Then, for every fixed \(u\) and every fixed \(t<u\),
\[
\boxed{\displaystyle
\lim_{X\to\infty}\Pr\{G_X(n)\le t\}
=\sum_{C\ \mathrm{cyclic}}d_C\,
\Phi\!\left(u+\frac{t-u}{r_C}\right).}
\tag{18}
\]
The same limit holds for the stationary grade-selected probability
divided by \(X/2^{h_X(u)}\).

Here is the extension of the companion argument. Put
\(L_X=X3^{a_h(n)}2^{-h}\). The exact grade identity at (14) gives
\[
\frac{\log L_X}{\delta_1\sigma\sqrt{\log X}}
=\sqrt{\frac h{\mu\log X}}\,G_X-u+o(1),
\qquad \delta_1=1/\mu.
\tag{19}
\]
For a nonperiodic endpoint, the uniform distinct-orbit product bound
implies \(L_X\ge e^{-B}\), with absolute \(B\). Since \(t<u\), (19)
therefore excludes all such endpoints from the event for large \(X\).
For sources already in a fixed cycle, let \(t_C(n)\) be its entry date
and put \(Z_X=(t_C(n)-\mu\log X)/(\sigma\sqrt{\log X})\). The
cycle-product identity gives
\[
G_X=u+r_C(Z_X-u)+o_{\Pr}(1).
\tag{20}
\]
The entry clock on that basin converges, as a finite measure, to
\(d_C\) times the standard normal law. The threshold in (18) is
strictly below \(u\), so it already guarantees entry. Continuity of
the normal law proves the single-cycle term. The proper minimum law
permits truncation to finitely many component labels and then removal
of that truncation, exactly as in the companion proof.

For the known cycle \(\{1,2\}\), \(r_C=1\). For every other positive
cycle the elementary cycle-product estimate gives
\(r_C\le r_*<1\), where the exact \(r_*\) is defined in the companion
note. Writing \(b\) for the known basin's density yields
\[
\sum_C d_C\Phi\!\left(u+\frac{t-u}{r_C}\right)
\le b\Phi(t)+(1-b)\Phi\!\left(u+\frac{t-u}{r_*}\right)
\le\Phi(t).
\tag{21}
\]
The gap between the two Gaussian coefficients is strictly positive
when \(t<u\). Thus a matching relative lower bound \(\Phi(t)\) at
any one fixed pair \((u,t)\) with \(t<u\) would force \(b=1\), and
the named positive-predecessor input would then give full Collatz.

This identifies the boundary precisely. The preminimum positive
contribution is explicitly evaluated for \(t>u\); the full-proof
quantile lies in \(t<u\), where that contribution is zero and the
cycle mixture records the entire answer. No continuation across that
boundary follows merely from uniform continuity of the capped height
process. Equation (18) is an extension of the companion cycle
calculation, independently reconstructed by both the arithmetic lane
and coordinator; it is not an estimate forcing the mixture to be
Gaussian.

## 7. Verification boundary

The deterministic product and correction estimate are proved here. The
random-time argument uses the full uniform topology and joint endpoint
statement inspected in the original source; no varying-parameter
moderate-deviation estimate is assumed. The stationary transfer was
independently reviewed in this pass and has a finite integer-window Lean
kernel. These probability limits are written, source-qualified deductions,
not new Lean formalizations and not extrapolations from finite scans.
Section 6 additionally uses the source-qualified packing and component
truncation inputs named in the arithmetic companion.
