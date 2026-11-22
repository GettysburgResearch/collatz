# Exact terminal-contact flux and the attempted capacity closure

**Status:** written deductions from the new contact-reference theorem
and the pinned ordinary last-contact measure. These are not additional
Lean claims. The identities retain each original source and show the
precise outcome of the combined contact/Green attack.

Fix `M>=2`, put `C_M={V<=M}` inside the nonperiodic unit domain, and
use

\[
\sigma(q)=\nu(q)^2\mathbf1_{C_M}(q),\qquad
\varepsilon=\frac{3\delta\gamma}{64M},\qquad
\rho=1-\varepsilon.
\]

The first-contact law for `{V<=2}` in the pinned PR176 source also
ensures almost-sure inverse contact with `C_M`. Its last-contact and
capacity arguments therefore apply to this larger threshold: every
escaping forward path has finitely many contacts because
`V(U^j x)>=delta nu(x)U^j x` tends to infinity. This adaptation adds
no ordinary-time contact estimate.

Let `E` be the escaping subset of the nonperiodic domain. Let `R` be
the first strictly later forward contact, with `J` its unchanged-source
pushforward. Define

\[
\Lambda_M=\{x\in C_M\cap E:R(x)\text{ is undefined}\},\qquad
\sigma_E=\sigma\mathbf1_E.
\]

Each source of `sigma_E` follows a finite contact chain ending at exactly
one member of `Lambda_M`. The intervening ordinary path may be long,
and the final ordinary excursion is infinite; neither duration is
counted by `J`.

## 1. Exact mass lost by the induced operator

For every nonnegative summable `a` supported in `C_M intersect E`,
determinism of the next-contact map gives

\[
\boxed{\|a\|_{\ell^1}-\|Ja\|_{\ell^1}
=\sum_{x\in\Lambda_M}a(x).}
\tag{1}
\]

Indeed each source either has one retained target, or is a terminal
contact. Merging sources at a target does not change total mass.
All sums are nonnegative, so countable fibers require no further
interchange assumption.

The escape predicate is constant along every actual source-to-target
path. Hence `J` preserves escape-labelled support, and the new
pointwise contact estimate restricts to

\[
J^k\sigma_E\le\rho^k\sigma_E.
\tag{2}
\]

Define the finite contact occupation

\[
\mu=\sum_{k\ge0}J^k\sigma_E.
\]

Equation (2) gives

\[
\sigma_E\le\mu\le\varepsilon^{-1}\sigma_E,
\qquad \|\mu\|_{\ell^1}\le\varepsilon^{-1}\|\sigma_E\|_{\ell^1}.
\tag{3}
\]

Summing (1) through time `N` telescopes. Its remainder is
`||J^(N+1)sigma_E||_1`, which tends to zero by (2). Therefore

\[
\boxed{\sum_{x\in\Lambda_M}\mu(x)
=\sum_{q\in C_M\cap E}\nu(q)^2.}
\tag{4}
\]

Equivalently, if `last(q)` is the unique final contact reached from
`q in C_M intersect E`, then

\[
\mu(x)=\sum_{\substack{q\in C_M\cap E\\\operatorname{last}(q)=x}}
\nu(q)^2\qquad(x\in\Lambda_M).
\tag{5}
\]

Each original source appears exactly once in (5). In particular a
nonzero escaping contact seed produces **positive terminal escape
flux**, rather than disappearing by the contact contraction.

## 2. A quantitative restriction in terms of component capacity

Already at one induced step, (1)–(2) imply

\[
\boxed{\varepsilon\sum_{q\in C_M\cap E}\nu(q)^2
\le\sum_{x\in\Lambda_M}\nu(x)^2.}
\tag{6}
\]

The same estimate follows from (3)–(4). It says that terminal contacts
carry at least the fraction `epsilon` of the squared reference mass.

For an individual escaping ordinary component `B`, the pinned
last-contact representation gives

\[
C_B=\sum_{x\in\Lambda_M\cap B}\nu(x)>0.
\]

Restriction of (6) to that component, followed by the elementary
positive-square inequality, proves

\[
\boxed{
\sum_{q\in C_M\cap B}\nu(q)^2
\le\frac1\varepsilon
 \sum_{x\in\Lambda_M\cap B}\nu(x)^2
\le\frac{C_B^2}{\varepsilon}
=\frac{64M}{3\delta\gamma}C_B^2.}
\tag{7}
\]

This is a genuine componentwise contact-mass budget. It is not a
zero-capacity conclusion: its right side is positive for every positive
capacity, and it grows linearly with the contact threshold. Along any
escaping spine `nu` stays bounded below by a positive number, so the
uncut sum of its squares is infinite. Equation (7) is compatible with
that limit because `epsilon` tends to zero as `M` tends to infinity.

## 3. The entire correction preserves this terminal sector

The canonical ordinary terminal measure is

\[
\eta_M(x)=\nu(x)\mathbf1_{\Lambda_M}(x),\qquad
\|\eta_M\|_{\ell^1}=\sum_{B\text{ escaping}}C_B<\infty.
\]

It is different from the squared-mass terminal distribution in (4).
Both are measures on actual original integer sources. The exact
Green-cone calculation in `EXCURSION_RESOLVENT_INTERFACE.md` gives

\[
\boxed{R(1)S\eta_M=S_T\eta_M,
\qquad\delta S\eta_M\le S_T\eta_M\le S\eta_M.}
\tag{8}
\]

Thus a nonzero `eta_M` survives the strict-Green inverse with a uniform
positive comparison. Independently,
`HARMONIC_KERNEL_FACTORIZATION.md` proves that multiplication by the
escape indicator commutes with `K` and `R(z)` and identifies the full
ordinary and critical harmonic kernels on their maximal domains.

There is therefore no cancellation of a positive escaping last-contact
capacity in this combined argument. The contact theorem determines a
finite terminal flux, and the entire correction transports its ordinary
occupation to a positive critical occupation. What remains unproved is
an estimate forcing `eta_M=0`, or one controlling the final unweighted
ordinary excursion strongly enough to exclude every positive atom of
that measure. Equations (4), (7), and (8) specify the actual restriction
obtained without replacing this missing step by an assumption.
