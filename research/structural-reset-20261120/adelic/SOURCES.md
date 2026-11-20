# Sources, normalization, and novelty boundary

## Main proof: no external analytic dependency

The final proof in `PRIME_HEIGHT_ESCAPE.md` is elementary: exact affine
iteration, gcd divisibility, logarithms, finite factorization, and
telescoping variation. No S-part or Subspace Theorem is used in
any main claim ADEL-001 through ADEL-007.

The initial idea to examine prime-height concentration and the
fixed-window Diophantine reconstruction were developed by the adelic
agent. The root agent supplied the elementary bounded-window gcd
replacement and then the stronger unrestricted height-variation charge.
Both were independently reconstructed before the final packet was
written. No priority claim relative to the full literature is made.

## Repository input and inherited boundaries

Frozen prior research input (PR148, not the repository's main branch):
`55d8968d2ecbc23a91c9c4733929f34be9bf0d28`.

This new packet is published from main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; the preceding research files
are source-pinned provenance, not a wholesale import of PR148.

Read before constructing the route:

- `AGENTS.md`, `README.md`, `docs/RESEARCH_MAP.md`;
- `research/RESULTS_CATALOG.md`, `research/integrated/ERRATA.md`;
- `research/integrated/factor-complexity/README.md`;
- `research/independent-attack-20261120/README.md` and its fixed-form
  comparison;
- `research/forward-bridge-20261120/CYCLE_REVIEW.md`.

No unreviewed SC*/FC* synthesis is imported. No fixed powered-factor
cover is assumed for arbitrary cycles. No completion or changing finite
witness is substituted for one positive ordinary source.

## Closely related recent primary research

The primary manuscript [Multiplicative rank, height, and energy of odd
Collatz trajectories](https://rstation.ai/problems/collatz/papers/137),
by `lyapunov_weaver`, v1 of 13 November 2026, is closely related.
Its Sections 3, 5 and 6 use the same exact affine gcd divisibility,
then multiplicative independence and exponent budgets to obtain
rank-dependent height bounds and sparse visits to bounded-rank groups.
Its Theorem 3 states
\((m/N)^3\log_2N\le200(1+T/N)(r+1)^2\) for visits to a rank-\(r\)
group. The present packet instead bounds partial S-parts and their
logarithmic weight, uniformly over changing choices of bounded-size
prime sets, using total height variation. It does not replace that
paper's results for arbitrary low-rank groups. Its cycle exclusion and
computational dependencies are not imported. This source was inspected,
not reviewed as a whole; no blanket acceptance or priority claim follows.

Jean-Louis Verger-Gaugry's [Divergent Trajectories in the 3x+1 Problem
and a S-units Equation](https://arxiv.org/html/2611.14569v1),
arXiv:2611.14569v1, 9 November 2026, Theorem 1.2(iii), gives an infinite-
prime conclusion for the prime sets associated with wave minima under
a bounded-wave-height hypothesis. That restricted statement neither
supplies the present weighted theorem nor its missing retention bridge.
It is recorded as an external comparison, not a load-bearing input.

## Initial comparison: sharp S-parts of a fixed polynomial

Yann Bugeaud, Jan-Hendrik Evertse, and Kalman Gyory,
**S-parts of values of univariate polynomials, binary forms and decomposable
forms at integral points**, *Acta Arithmetica* **184** (2018), 151--185,
[DOI 10.4064/aa170828-7-3](https://doi.org/10.4064/aa170828-7-3).

- [Author-hosted full paper](https://irma.math.unistra.fr/~bugeaud/travaux/BuEvGy-AAdef.pdf).
- [Publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/112532/s-parts-of-values-of-univariate-polynomials-binary-forms-and-decomposable-forms-at-integral-points).
- [Original preprint](https://arxiv.org/abs/1708.08290).

Theorem 2.1(i) gives, for fixed separable degree-\(d\) polynomial \(f\),
fixed finite \(S\), and every \(\epsilon>0\),

\[
 [f(n)]_S\ll_{f,S,\epsilon}|f(n)|^{1/d+\epsilon}
\]

at nonzero values. The constant is ineffective. The exponent is
\(1/d+\epsilon\), not \(1-1/d+\epsilon\). In contrast, the binary-form
Theorem 2.4(i) allows both coordinates to vary and has exponent
\(2/d+\epsilon\). These distinct normalizations were checked directly
in the primary source.

For distinct rational affine forms this comparison can be reconstructed
in dimension two using \((n,1)\), \(X,Y\) at infinity, and the maximally
divisible affine form together with \(Y\) at each fixed prime. A
primary theorem statement is Jan-Hendrik Evertse,
[The p-adic Subspace Theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf),
May 2011, Theorem 1.1 and its two-dimensional applications.

The final elementary proof removes this dependency, its ineffective
constants, and the need to truncate valuation words.

## Classical bounded-prime-support finiteness

Frits Beukers and Hans Peter Schlickewei,
**The equation x+y=1 in finitely generated groups**,
*Acta Arithmetica* **78** (1996), 189--199,
[DOI 10.4064/aa-78-2-189-199](https://doi.org/10.4064/aa-78-2-189-199).

- [Primary journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa78/aa7826.pdf).
- [Author-hosted version](https://webspace.science.uu.nl/~beuke106/s-units.pdf).
- [Publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/78/2/109078/the-equation-x-y-1-in-finitely-generated-groups).

Their Theorem 1.1 bounds the number of solutions of \(x+y=1\) in the
divisible closure of a rank-\(r\) subgroup of \((\mathbb C^*)^2\) by
\(2^{8r+8}\). This is uniform in the generators, not only for one
specified prime set.

For a primitive cycle using at most \(s\) primes, enlarge its support
by 2 and 3. The distinct transitions give distinct solutions
\((2^{a_j}n_{j+1},-3n_j)\) of \(x+y=1\) in a group of rank at most
\(2(s+2)\). Hence its odd period is at most \(2^{16s+40}\). Bounded
period implies finitely many exponent words because \(\sum a_j\le2m\).
Thus raw bounded-prime-support cycle finiteness is already a classical
consequence, with a better numerical dependence than the elementary
bound in this packet.

The distinctive written result here is the elementary, uniform control
of the *fraction of aggregate prime height*, including moving choices
of the heaviest bounded-size prime set, and its extension to arbitrary
ordinary nonperiodic histories. The known S-unit corollary is not
advertised as new.

## Evidence limits

The primary statements above were checked in author or journal PDFs and
publisher records on 20 November 2026. Literature inspection is not an
exhaustive novelty certificate. The main proofs have no computation
dependency. No expanded finite verification, large search, empirical
claim of ordinary escape, or assertion of full cycle exclusion appears
in this packet.
