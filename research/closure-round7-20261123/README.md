# Round seven: finite prime detection, exact jet clearing, and actual-source separation

23 November 2026. Parent checkpoint:
`e4367dd2c4406c1041e66d82dfba822908747fa3`.

**Full Collatz remains OPEN.** Three parallel attacks on actual germ
construction, ordinary descent, and source transfer produced four connected
results. The strongest new cycle statement is finite: a supplied eventual
cycle has an explicit Taylor-order certificate for every prime in its
reduced clock. Its bound is independent of the actual preperiod. No
arbitrary-source germ, universal paid descent selector, or forward
collision convergence rate is constructed.

The general results below have independent written reviews. Seven finite
arithmetic transport theorems are additionally Lean checked. Exact bounded
controls support the formulas without replacing their general proofs.
The [report index](../../reports/2026-11-23-closure-round7/README.md) records
the precise source, review, execution, and publication boundaries.

## 1. Every reduced-clock prime has a finite detection certificate

Use the shortcut map and the literal binary Taylor germ

\[
B_n(z)=\sum_{k\ge0}e_k3^{-p_{k+1}}z^k,
\qquad J_n(t)=B_n(2+t)=\sum_{j\ge0}c_j(n)t^j.
\]

Suppose the actual orbit is eventually periodic, with cycle length A
and odd count p. Put

\[
g=\gcd(A,p),\quad u=A/g,\quad v=p/g,\quad
F(z)=z^u-3^v,\quad D_{\rm red}=2^u-3^v.
\]

Let C(z) be the complete chronological numerator of that cycle, and
let `R=Res(F,C)`, a nonzero integer. For every prime ell dividing
`D_red`, define the first forbidden Taylor order

\[
\delta_\ell=\min\{j:v_\ell(\operatorname{den}c_j(n))>0\}.
\]

The new finite theorem proves

\[
\boxed{\delta_\ell\le
\left\lfloor\frac{u\,v_\ell(R)}{v_\ell(D_{\rm red})}\right\rfloor
<u^2(2p-1).}
\]

The first inequality uses a finite Taylor truncation evaluated at a
genuine algebraic pole. The norm bounds the numerator valuation, and the
full valuation of `F(2)` bounds at least one pole's distance from two.
The second inequality supplies a simple explicit height bound. Neither
argument evaluates an infinite series at its pole.

For ell other than two and three, truncated coefficient integrality is
exactly invariant along every actual prefix. Therefore the same first
forbidden order, and the same period-dependent upper bound, apply at the
original source however long its preperiod is.

**Ordinary conditional consequence.** If a positive ordinary source is
already known to be eventually periodic with these cycle parameters,
and its first `u^2(2p-1)` actual coefficients all belong to `Z[1/3]`, it
reaches one. The preceding packet supplies the positive-cycle arithmetic
that every nonstandard ordinary cycle has `D_red>1` coprime to six.

This is a finite test for a supplied eventual cycle. It does not prove
eventual periodicity, provide a universal period bound, or compute the
actual coefficients of an arbitrary ordinary source.

[Complete finite theorem](FINITE_JET_BOUND.md) ·
[independent review](../../reports/2026-11-23-closure-round7/DETECTOR_REVIEW.md).

## 2. Arbitrarily late specified-prime detection, even above any floor

For every Taylor order `k>=1` and real floor `M>0`, an explicit primitive
positive rational cycle has all its states greater than M and satisfies

\[
\boxed{v_5(\operatorname{den}c_j)=\max(0,j+1-k)
\quad\hbox{for every }j\ge0.}
\]

The family uses `W_m=u^(m-1)v`, with
`u=1^p 0^(A-p)`, `v=0 1^p 0^(A-p-1)`,
`A=3 mod20`, `p=1 mod20`, and `m=4 mod5`. Hensel digit choices set the
exact delay. Irrational rotation gives base clocks with the real cycle
floor as high as desired. A full-denominator gcd argument proves that
every member is nonintegral; these are actual rational cycles.

The delayed prime is specifically five. Other forbidden primes already
occur in the source denominator. Thus this is not a family of arbitrarily
long initial jets in `Z[1/3]`, and does not refute a possible stronger
bound restricted to hypothetical ordinary cycles.

There is also a genuine ordinary construction. Any finite prefix of
such a rational orbit has arbitrarily large positive ordinary sources
with that literal prefix which then reach a power of two and one. If
the common prefix has length h, their actual Taylor coefficients satisfy

\[
v_2(c_j(n)-c_j(r))\ge h-j\qquad(0\le j\le h).
\]

The proof uses the full carry and the fact that two generates the units
modulo `3^s`. Every constructed ordinary shadow already has its entire
germ in `Z[1/3][[t]]`. The ordinary source changes with the requested
horizon. Binary convergence of these finite witnesses does not preserve
the arithmetic coefficient ring and does not give one ordinary source
realizing the whole rational cycle.

[Family and convergent-shadow proofs](ORDINARY_DESCENT.md) ·
[independent review](../../reports/2026-11-23-closure-round7/DESCENT_REVIEW.md).

## 3. An exact denominator clock along one actual orbit

If a finite actual Taylor jet through order r is rational and belongs to
`Z[1/3]`, write `S_r(n)` for the largest exponent of three in its reduced
denominators. Then

\[
\boxed{S_r(T^Nn)=\max\{S_r(n)-p_N,0\}.}
\]

Each odd step clears exactly one remaining denominator layer. Even
steps preserve it. Binary integrality of the actual coefficients removes
the apparent powers of two from division by `2+t`. Positive ternary
convergence radius gives `S_r(n)=O(r)`, so increasing jets become ordinary
integer jets after linearly many odd steps, conditional on that germ.

The complete same-source identity at every order is

\[
2^j3^{p_N}c_j(n)-C_j(N)
=2^N\sum_{i=0}^j\binom N{j-i}2^ic_i(T^Nn),
\]
\[
C_j(N)=\sum_{k<N}e_k\binom kj2^k3^{p_N-p_{k+1}}.
\]

The full tail is retained. These identities do not create a strict
Diophantine height saving or a decreasing ordinary-state rank. Rationality
of the first unknown derivative is still unproved for an arbitrary
ordinary source; the recurrence itself keeps the original multiplier.
The convergent source 85 has `c_1(85)=0`, preventing a proposed universal
nonvanishing shortcut.

[Arithmetic transport](GERM_CONSTRUCTION.md) ·
[seven public Lean theorems](GermConstruction.lean) ·
[independent review](../../reports/2026-11-23-closure-round7/GERM_REVIEW.md).
The exact valuation equality is a written proof; Lean proves finite
integer clearing and the subring equivalence from the coefficient equations.

## 4. The inverse entrance law cannot be identified with the forward law

PR177's new ordinary inverse entrance law is inspected at
`3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`. On a hypothetical escaping
odd component, it is

\[
\nu_j(n)=r(n)^s1_{n\in\operatorname{Pred}(q_j)}/A_j,
\qquad s>1,\qquad 0<r(n)\le1/n.
\]

Keep the same actual source and its forward empirical law
`pi_N=N^(-1) sum_(i<N) delta_(q_i)`. Using the already proved whole-orbit
count with `theta=H_2(log_3 2)<1`, the new comparison proves, uniformly
in the inverse root j,

\[
\boxed{1-\operatorname{TV}(\pi_N,\nu_j)
=O\!\left(N^{-(1-\theta/s)}/\sqrt{1+\log N}\right).}
\]

If the growing moduli satisfy `H_N/Q_N=o(N)`, the projected total
variation also tends to one. These are precisely scales where the
existing complete-quotient collision-packing upper tends to zero.
The inverse laws retain an atom at the original source and hence have
collision dimension zero. None of this assigns a collision dimension
to the forward stationary law.

For `j>=N-1`, the actual-source entropy cost obeys

\[
\operatorname{KL}(\pi_N\Vert\nu_j)
\ge(s/\theta-1)\log N+
\frac{s}{2\theta}\log(1+\log N)-O(1).
\]

Thus convergence of the inverse endpoint sampler supplies no direct
small-error comparison for the chronological forward empirical law.
An additional arithmetic transport must pay for this change of law.
The separate signed transport term and optimal pressure trial remain open.

[Actual-source comparison and exact constants](SOURCE_TRANSFER.md) ·
[independent review](../../reports/2026-11-23-closure-round7/TRANSFER_REVIEW.md).
The note also retains an actual periodic compiler control showing
exponentially growing transported anchors; it explicitly makes no
escaping-ray counterexample claim from that control.

## Evidence and the next mathematical step

| Result | Evidence and scope |
| --- | --- |
| Finite resultant detector and prefix-independent bound | Written proof, independent reconstruction, selected exact resultant/Taylor controls |
| Arbitrary specified-prime delay and arbitrary rational floor | Written five-adic and real proofs; five complete rational-cycle replays |
| Genuinely convergent ordinary shadows | Explicit full-carry construction; two complete ordinary trajectories and exact jet comparisons |
| Finite jet arithmetic | Seven public Lean theorems, fresh compilation and axiom audit; exact valuation law separately reviewed |
| Forward/inverse separation and entropy cost | Written actual-source proof with pinned entrance-law premise; exact finite normalized-law controls |

Normal and optimized executions of [exact_replay.py](exact_replay.py)
passed with byte-identical output. Inputs, controls, source refresh, and
literature discovery boundaries are pinned in [SOURCES.json](SOURCES.json)
and the report receipts. No new external analytic theorem is imported
from a search excerpt.

The next closing step must still act on **one fixed arbitrary positive
ordinary source**: construct its required arithmetic germ, provide a
universally available paid descending block, or prove the actual forward
collision/pressure input. The finite detector removes an unbounded
Taylor-order search once a cycle is supplied. The other results explain
the exact arithmetic information that finite shadows and inverse-law
convergence leave missing.
