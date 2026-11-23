# Can phase recurrence force the missing halving drift?

This is a full-closure attempt using the newly forced dyadic section.
The key question is whether deterministic information about the leading
digits can force enough divisions by two on every fixed ordinary orbit.
The finite statements below are distinguished from an infinite ordinary
orbit, and from a limit obtained by changing the starting integer.

## 1. Keep the integer information that a phase rotation discards

For the actual odd orbit, write

\[
x_{j+1}=\frac{3x_j+1}{2^{a_j}},\qquad
a_j=\nu_2(3x_j+1),\quad \alpha=\log_2 3.
\]

There is the exact real identity

\[
\log_2 x_N=\log_2 x_0+N\alpha-\sum_{j<N}a_j+E_N,
\qquad
0\le E_N\le\sum_{j<N}\frac1{x_j}.
\tag{J1}
\]

For an orbit that is not eventually periodic, the positive integers `x_j` are distinct: a repeat
would make the subsequent deterministic orbit periodic. In particular
`x_j` eventually exceeds every fixed bound. The reciprocal average tends
to zero. The elementary cutoff estimate

\[
\sum_{j<N}\frac1{x_j}\le K+\frac{N}{K+1}
\tag{J2}
\]

proves this by first taking `N` to infinity at fixed `K`, then increasing
`K`. Sorting distinct odd states gives the sharper harmonic bound, but
that sharpening is unnecessary for the limit.

To force ordinary descent from a starting value, (J1) needs a **strict
surplus** of the accumulated halving count over `N*alpha`, large enough
to pay the actual nonnegative error. Passing to logarithms modulo one
erases the entire integer sum `sum a_j`; its return requires a separate
argument.

## 2. The deterministic Fourier gain

Put `z_j=exp(2*pi*i*k*log2(x_j))` and `w=exp(2*pi*i*k*alpha)`. The exact
coboundary identity is

\[
(1-w)\sum_{j<N}z_j
 =z_0-z_N+\sum_{j<N}(z_{j+1}-wz_j).
\]

The actual phase error in (J1) bounds the final sum. The new Lean module
[`ReturnFourier.lean`](lean/ReturnFourier.lean) proves the conservative
constant in

\[
|1-w|\left|\sum_{j<N}z_j\right|
\le 2+4\pi k\sum_{j<N}\frac1{x_j}.
\tag{J3}
\]

For each nonzero frequency, irrationality of `log2(3)` makes `1-w` nonzero.
Together with (J2), this gives vanishing normalized Fourier sums for any
injective ordinary odd orbit. The mathematical consequence is pointwise
equidistribution of binary mantissas, without a random-parity assumption.
The precise compiled finite/limit scope is recorded in
[`RETURN_DYNAMICS.md`](RETURN_DYNAMICS.md) and the execution report; the
words "equidistribution" do not stand in for a silently imported Lean
proof of a criterion that has not been compiled. The temporal-density-zero
statement for actual marked odd-state visits is now separately compiled in
[`MarkFrequency.lean`](lean/MarkFrequency.lean), using a direct finite
kernel proof rather than assuming that criterion.

This is useful deterministic information about any hypothetical
nonperiodic counterexample, but its conclusion is about the fractional
part of logarithmic height. It does not give the missing halving surplus
in (J1). Nontrivial periodic orbits also require a separate argument.

## 3. A stationary law with the wrong drift

At large real height the phase error tends to zero. If the odd 2-adic
coordinate is retained, the limiting update is

\[
(\theta,z)\longmapsto
\left(\theta+\alpha\pmod1,\frac{3z+1}{2^{\nu_2(3z+1)}}\right).
\]

At the 2-adic integer `z=-1`, the valuation is one and the second
coordinate stays `-1`. Hence the product of uniform circle measure and
the point mass at `-1` is invariant. It has a perfectly uniform phase
marginal but halving count one at every odd step, giving positive real
height drift `alpha-1`.

This law is **not** a positive ordinary orbit or a Collatz counterexample.
It proves a precise limitation of the proposed inference: stationarity
and the proven phase marginal alone do not imply geometric valuation
statistics, mean valuation two, or negative height drift. A complete
joining argument has to exclude such biased laws for a **fixed positive
ordinary starting integer**, retaining any unbounded tail information
needed for its valuation observable.

## 4. Ordinary marked prefixes realize every fixed precision of that law

The obstruction is not removed by asking that every finite prefix be
realizable by positive ordinary integers in the new section. For
`m>=0`, define

\[
D=2^m,\quad b=D-m,\quad
n_m=2^b(2^m+1)-1=2^D+2^b-1.
\]

The binary depth of `n_m` is exactly `D`, and

\[
(D+1)(n_m-2^D)\le2\,2^D\le70\,2^D.
\]

Thus these odd starts lie even in the narrower constant-two band. For
every `j<=b`, the credited rising-prefix identity gives

\[
T^j(n_m)+1=3^j2^{b-j}(2^m+1),\qquad T^j(n_m)\ge n_m.
\tag{J4}
\]

Given any finite horizon `L`, precision `K>=1`, and height floor `M`,
choose `m=M+L+K+2`. The elementary bound `2m<=2^m` gives `b>=L+K`, and
therefore an ordinary marked `n_m>M` with

\[
T^j(n_m)\equiv-1\pmod{2^K},\qquad
T^j(n_m)\ge n_m,
\qquad 0\le j\le L.
\tag{J5}
\]

All these states are odd. In particular the first `L` full shortcut steps
are also successive odd steps. The all-parameter construction is in
[`BandSimulation.lean`](lean/BandSimulation.lean), reusing the source's
ordinary `odd_run` theorem rather than introducing a completed binary
input as an ordinary witness.

Taking `K` and `M` to infinity along increasing `L`, (J3) and (J5) explain
how finite empirical laws from **different** ordinary marked starts can
approach the biased product law above. The normalizations are decisive:
the starting integer depends on the horizon and precision. Neither this
limit nor compactness supplies one fixed positive integer satisfying all
the finite constraints. The 2-adic limit `-1` is outside the positive
ordinary starting domain.

## 5. What the full proof attempt still needs

A successful use of the new section needs more than another phase visit
or a stationary marginal. It must control the integer halving cocycle for
the same fixed orbit, or construct an actual descending certificate for
each residual marked input. The offset route gives a constructive class
of such certificates and an exact family beyond its window; see
[`BAND_DESCENT.md`](BAND_DESCENT.md). Its later multiplier obligation is
not supplied by phase equidistribution or by the finite realizations here.

The joint real/2-adic route was pursued as a possible global proof. The
missing exclusion of biased limiting behavior for a fixed ordinary input
remains an open mathematical statement, not an assumed regularity rule.
