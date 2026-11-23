# The last-contact measure supplies an L² source class for the ordinary channels

**Status: source-qualified written deduction. No new Lean declaration,
vanishing residue, or Collatz convergence claim.**

## 1. Priority and the additional interface

PR183 at `68345f60a4f757acb42a69a4ac95910f8ce26163` already proves the
ordinary component channel geometry and the asynchronous residue:

- `research/profound-step-20261122/operator/WOLD_CHANNELS.md`, especially
  W7--W13, identifies the synchronous classes, their common capacity,
  the bilateral shift for each escaping component, and the frequency
  residue.
- `research/profound-step-20261122/transport/ASYNCHRONOUS_RESIDUE.md`,
  especially A6--A19, proves the Abel and Cesàro component residues and
  verifies its source hypothesis for the original projected `n^{-4}` law.
- `research/profound-step-20261122/transport/OPERATOR_REVIEW.md` records
  an independent reconstruction of the channel formulas.

Those sources import the ordinary harmonic flow from PR185 at
`276be8154f4e867acc0230466b34d9cb224aacf5`. Their general complete-source
extension assumes

\[
\sum_x\frac{|a(x)|}{\sqrt{\nu(x)}}<\infty.
\tag{1}
\]

The companion [ORDINARY_LAST_CONTACT_MEASURE.md](ORDINARY_LAST_CONTACT_MEASURE.md) constructs a finite
ordinary last-contact measure `eta=nu 1_Lambda`, with

\[
\sum_{j\ge0}L^j\eta=\nu\mathbf1_T\le\nu,\qquad
\eta(\mathcal C)=C_{\mathcal C},\qquad
M:=\sum_x\eta(x)=\sum_{\mathcal C}C_{\mathcal C}<\infty.
\tag{2}
\]

Here `Lambda` consists only of escaping odd-unit last contacts, `T`
is the future-defined sector at or after a last contact, and `L` is
killed on entering any periodic orbit. All sources in `Lambda` escape.
The definitions and source-qualified hypotheses of that note are
retained exactly.

Equation (2) permits a stronger source extension on this particular
ordinary boundary: **every `a=eta f` with `f in L²(eta)` is admissible**.
Condition (1) is not needed for this class. In particular, (2) does not
claim that `sum sqrt(eta(x))` is finite.

## 2. Uniform normalized bounds with the source energy itself

Allow complex `f`, and set `a(x)=eta(x)f(x)`. Its actual collision energy is

\[
\mathcal E_\nu(a)=\sum_x\frac{|a(x)|^2}{\nu(x)}
=\sum_x\eta(x)|f(x)|^2=\|f\|_{L^2(\eta)}^2.
\tag{3}
\]

Also `sum |a| <= sqrt(M) ||f||`, so every finite-discount transport is
well defined. Define

\[
B_{r,\theta}a=\sum_{k\ge0}r^ke^{ik\theta}L^ka,
\qquad
C_{J,\theta}a=\frac1J\sum_{0\le k<J}e^{ik\theta}L^ka.
\]

For `x` in `Lambda` reaching `q`, let `d(x,q)` be its unique hitting
depth. Nonperiodicity ensures uniqueness. At each target, (2) gives
the subprobability weights

\[
\sum_{\substack{x\in\Lambda\\x\to q}}
\frac{\eta(x)}{\nu(q)}\le1.
\]

Weighted Cauchy--Schwarz therefore gives

\[
\frac{|B_{r,\theta}a(q)|^2}{\nu(q)}
\le\sum_{\substack{x\in\Lambda\\x\to q}}
\eta(x)|f(x)|^2r^{2d(x,q)}.
\tag{4}
\]

Every source has one distinct surviving endpoint at each depth. Summing
(4) over targets, then summing the geometric series, proves

\[
\boxed{
(1-r^2)\mathcal E_\nu(B_{r,\theta}a)
\le\|f\|_{L^2(\eta)}^2.
}
\tag{5}
\]

For the finite clock sum, replace `r^d` in the same argument by
`1_{d<J}`. Each source now has exactly `J` endpoints, giving

\[
\boxed{
J\mathcal E_\nu(C_{J,\theta}a)
\le\|f\|_{L^2(\eta)}^2.
}
\tag{6}
\]

Both bounds are uniform in the frequency and the indicated clock
parameter. They preserve every original source mass and every collision.
They are stronger than a triangle estimate involving (1) on this
last-contact source class.

## 3. Uniform frequency residues for the complete L² boundary class

Use PR183's integer coordinate `h_mathcal C(x)`, characterized by
`h_mathcal C(Ux)=h_mathcal C(x)+1`. Its choice of origin only changes
an amplitude by a scalar phase. Define

\[
A_{\mathcal C,f}(\theta)
=\sum_{x\in\Lambda\cap\mathcal C}
\eta(x)f(x)e^{-i\theta h_{\mathcal C}(x)},
\qquad
\mathcal R_f(\theta)
=\sum_{\mathcal C}
\frac{|A_{\mathcal C,f}(\theta)|^2}{C_{\mathcal C}}.
\tag{7}
\]

By `eta(mathcal C)=C_mathcal C`, componentwise Cauchy--Schwarz gives

\[
\mathcal R_f(\theta)\le\|f\|_{L^2(\eta)}^2.
\tag{8}
\]

The complete-source formulas are

\[
\boxed{
\lim_{r\uparrow1}(1-r^2)\mathcal E_\nu(B_{r,\theta}a)
=\lim_{J\to\infty}J\mathcal E_\nu(C_{J,\theta}a)
=\mathcal R_f(\theta),
}
\tag{9}
\]

with both limits uniform in `theta`.

For finite support, the Abel formula is PR183 W11. The unmodulated
Cesàro formula is PR183 A9. Its finite-source proof also gives the
displayed modulated version: a pair meeting at clocks `(p,q)` has the
constant phase `exp(i(p-q)theta)` multiplying its real Cesàro common-tail
kernel. There are finitely many pairs, and the lag identity gives
exactly the phases in (7), uniformly on the circle.

For the infinite extension, take increasing finite subsets `F` of
`Lambda` and replace `f` by `f 1_F`. Applying (5)--(6) to the omitted
tail controls the difference of normalized norms by
`||f 1_(Lambda minus F)||_L²(eta)`, uniformly in every parameter.
The difference of their squared energies is at most

\[
2\|f\|_{L^2(\eta)}
\|f\mathbf1_{\Lambda\setminus F}\|_{L^2(\eta)}.
\tag{10}
\]

Equation (8) gives the identical tail estimate for the limiting
amplitude vectors. These tails tend to zero. The finite-source limits
therefore pass uniformly to (9). This argument needs no uniform bound
on source meeting times, no summability of their square roots, and no
exchange of limits without a displayed tail control.

## 4. The canonical source and the exact remaining boundary mass

For `f=1`, the original source is exactly `a=eta`. At zero frequency,
(2) gives

\[
\boxed{
\mathcal R_1(0)
=\sum_{\mathcal C}\frac{C_{\mathcal C}^2}{C_{\mathcal C}}
=M=\mathcal E_\nu(\eta).
}
\tag{11}
\]

Thus both upper bounds (5)--(6) are attained asymptotically at zero
frequency by the canonical last-contact source. If an escaping
component exists, this number is strictly positive. Finite boundary
mass is therefore compatible with a nonzero ordinary channel residue.

More generally, let `A` be the sigma-algebra on `Lambda` generated by
the ordinary component partition. Equation (7) at zero frequency is
the concrete conditional-mean identity

\[
\mathcal R_f(0)
=\|\mathbb E_\eta[f\mid A]\|_{L^2(\eta)}^2.
\tag{12}
\]

No normalization of the finite measure is required. The formula is
also valid in the zero-measure case. It identifies which ordinary
boundary part survives asynchronous averaging; it does not prove
that this part is absent.

## 5. Scope and relation to the original full-source task

PR183 owns the Wold geometry, asynchronous pair limits, and the verified
application of (1) to its original projected `n^{-4}` source. The addition
here is the uniform energy-tail control (5)--(10) for the larger
`L²(eta)` boundary source class, and its canonical exact value (11).

This extension applies to sources supported on `Lambda`. It does not
move an arbitrary original atom to a last-contact ancestor, change an
atom's clock, or upgrade a general source to this class without a proof.
The full projected law in PR183 already has its own valid source-tail
argument. Its escaping residue is not removed by the present extension.

All these operators are killed on entry into any periodic orbit. The
nontrivial-cycle second-order pole remains the separate PR183 statement
A21--A24. No part of this note discards it or proves it vanishes.
