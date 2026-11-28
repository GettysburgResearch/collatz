# Final attempt ledger: near-fair tilt and the critical selector

Date: 2026-11-28. This records the last attempted closure of the
one-copy bound in [CRITICAL_GRADE_TAIL.md](CRITICAL_GRADE_TAIL.md).
No full-proof lower bound was obtained. The calculation below preserves
the rare-event scale, but leaves an ordinary positive-integer exponential
moment unevaluated. It is not a new proof-equivalence claim.

## 1. What the near-fair tilt does preserve

Keep the median clock \(h=\lfloor\mu\log X\rfloor\) and the actual
ordinary grade
\(W_X(n)=2(a_h(n)-h/2)/\sqrt h\). Fix a real \(\lambda\), and set

\[
p_h=\frac{1+\lambda/\sqrt h}{2},\qquad
c_h=(1-\lambda^2/h)^{h/2},\qquad
t_h=\frac{\sqrt h}{2}\log\frac{p_h}{1-p_h}.
\tag{1}
\]

For large \(h\), the stationary real/ternary affine seed of bias
\(p_h\) exists. Drive its future with that same bias and keep the full
ordinary selector \(K_{h,X}\). A word of grade \(a\) has likelihood
relative to fair bits

\[
\ell_h(a)=2^hp_h^a(1-p_h)^{h-a}
=c_h\exp\!\left(t_h\frac{2(a-h/2)}{\sqrt h}\right).
\tag{2}
\]

This is an exact algebraic identity. Also
\(c_h\to e^{-\lambda^2/2}\) and \(t_h\to\lambda\), but replacing
the exponent parameter inside an unbounded expectation requires care.

The original full-conductor word argument gives

\[
\frac{2^h}{X}\Pr_{p_h}(K_{h,X}=1)
=\mathbb E_{R_0}\frac1X
\sum_{n=\lfloor R_0\rfloor+1}^{\lfloor R_0\rfloor+X}
\ell_h(a_h(n)).
\tag{3}
\]

For a fixed seed shift, at most \(\min(\lfloor R_0\rfloor,X)\)
terms leave and the same number enter. Since

\[
0\le\ell_h(a)\le (1+|\lambda|/\sqrt h)^h
\le e^{|\lambda|\sqrt h},
\]

the difference between (3) and the unshifted weighted ordinary mean is
at most

\[
e^{|\lambda|\sqrt h}\,
\frac{\mathbb E_{p_h}\min(R_0,X)}X.
\tag{4}
\]

The affine-series fractional-moment proof in
[CONDUCTOR_AND_STATIONARY_TRANSFER.md](../factoring/CONDUCTOR_AND_STATIONARY_TRANSFER.md)
is uniform for \(p\) in a sufficiently small fixed neighborhood of
\(1/2\). In particular

\[
\mathbb E_p R_0^{1/2}
\le\frac{p\,2^{-1/2}}
{1-(1-p)2^{-1/2}-p(3/2)^{1/2}}\le C
\tag{5}
\]

there, since the denominator is strictly positive at \(p=1/2\).
Thus (4) is \(X^{-1/2+o(1)}\), and we obtain the rigorous transfer

\[
\boxed{
\frac{\Pr_{p_h}(K_{h,X}=1)}{X/2^h}
=c_h\,\frac1X\sum_{n=1}^X e^{t_hW_X(n)}+o(1).}
\tag{6}
\]

The error in (6) is absolute **after** division by the rare-event
scale \(X/2^h\). For \(\lambda<0\), the seed has finite mean
\(p_h/(1-2p_h)=\sqrt h/(2|\lambda|)-1/2\), improving the displayed
error to \(X^{-1+o(1)}\).

## 2. Where the attempted closure stopped

The selector probability is exactly \(X/2^h\) for fair future words.
That normalization does not hold for biased words: their probabilities
differ with the grade, and (6) retains precisely that difference. The
finite mean or fractional moment of the stationary seed pays for
changing the source interval; it does not bound the remaining
exponential moment or choose its sign.

Likewise, the unconditional grade under \(\Pr_{p_h}\) is binomial,
but its law after conditioning on \(K_{h,X}=1\) is the unresolved
integer-selected law. Treating it as an independent binomial draw would
discard the arithmetic quantity the tilt was introduced to estimate.
An unqualified moment-generating-function limit also cannot be inferred
from a central limit theorem without uniform integrability. Equation
(6) deliberately keeps the exact finite exponential moment.

The actual one-copy association counterexample in
[STATIONARY_GRADE_ANTICORRELATION.md](STATIONARY_GRADE_ANTICORRELATION.md)
rules out a universal all-scale positive-association inequality. It says
nothing against a vanishing-error asymptotic estimate. A second possible
shortcut, a blanket real-rooted or ultra-log-concave ordinary grade
polynomial, fails already in small exact native examples:

- At \(h=3,X=7\), the grade polynomial is
  \(3z+3z^2+z^3\); its nonzero quadratic factor has discriminant
  \(-3\).
- At \(h=3,X=9\), it is \(1+3z+4z^2+z^3\). Dividing coefficients
  by \(\binom3a\) gives \((1,1,4/3,1)\), which is not log-concave.

These finite observations only reject the specified general-purpose
polynomial premises; no asymptotic obstruction is inferred from them.

## 3. What was genuinely evaluated, and what remains

The positive result is the relative stationary evaluation at moving
precritical clocks in
[PRECRITICAL_STATIONARY_EVALUATION.md](../factoring/PRECRITICAL_STATIONARY_EVALUATION.md).
The original full height-process theorem permits clocks
\(\mu\log X-w_X\sqrt{\log X}\) with arbitrary deterministic
\(w_X\to\infty\), \(w_X=o(\sqrt{\log X})\), and gives the Gaussian
selected-grade law with an error small relative to \(X/2^h\).

At the median, the strictly negative grade tail comes entirely from
genuine postminimum futures. The exact cycle mixture and its uniform
nonstandard-cycle gap are written in the critical-grade note. The
preminimum process, a stationary marginal, weak compact-quotient mixing,
and the near-fair change of measure do not fix the remaining mixture.

As a final literature check, the original source of Leen's tilted
ternary laws was retrieved and its main regularity/Fourier statements
and their scope inspected:
[Zenodo 23268832](https://doi.org/10.5281/zenodo.23268832),
`tilted-syracuse-laws.tex`, SHA256
`3855fc67c0c30c0e8e78af3de93fd85279d4376f2cb7c1e5d63d24433ce70afc`.
Its scalar ternary density and compact-parameter Fourier estimates do
not supply a joint real-window, full-conductor, ordinary-diagonal
relative estimate. No such conclusion was imported from them.

All statements in this ledger are written deductions or explicitly
identified finite examples. No new Lean formalization is claimed.
