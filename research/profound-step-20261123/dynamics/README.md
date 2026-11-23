# Actual-source coalescence and critical collisions

**Written research result; escape exclusion remains OPEN.**

Read [COALESCENCE_AND_CRITICAL_COLLISIONS.md](COALESCENCE_AND_CRITICAL_COLLISIONS.md).

This attempt tested whether the new actual real-boundary regularity could
supply the quantitative smoothing needed by the ternary collision route.
It preserves one fixed original ordinary orbit throughout.

## Exact results

With \(N\) original orbit states and finite inverse clock \(r\),
\[
 \|\zeta_{N,r}-\eta_N\|_{\rm TV}
 =\frac1N\sum_{j<N}\left(1-\frac{\nu(q_j)}{\nu(q_{j+r})}\right),
 \qquad
 \sup_r\|\zeta_{N,r}-\eta_N\|_{\rm TV}
 =\frac{\mathbb E\min(\tau,N)}N.
\]
Here \(\eta_N\) is the unchanged empirical forward law, and \(\tau\)
is the actual first coalescence clock under the supplied whole-path law.

For the actual trace profile, this strengthens the previous retained
high-profile fraction to whole mass: for every \(B_N=o(N)\),
\(\inf_r\zeta_{N,r}\{F>B_N\}\to1\). Low-profile endpoint estimates
therefore cover an asymptotically vanishing part of the required law.

The collision comparison has the square-root scale:
\[
 |\sqrt{\operatorname{Col}_Q(P)}-\sqrt{\operatorname{Col}_Q(Q')}|
 \le\sqrt2\,\|P-Q'\|_{\rm TV}.
\]
At \(Q\asymp N^{1/\theta}\), a sufficient uniform comparison rate is
\(\mathbb E\min(\tau,N)=o(\sqrt N)\). Label-dependent inverse clocks
bounded by \(o(\sqrt N)\) already satisfy the required variation bound
by an exact finite telescope. Neither result bounds the original orbit's
collisions.

A second theorem constructs one fixed absolutely continuous reweighting
on the same hypothetical ordinary component, preserving the stated
harmonic/path properties and PR180's absolutely-continuous-stable boundary
regularity, but with uniform variation defect at least a constant divided
by \(\log N\). This changes the harmonic law; it does not assert that the
distinguished canonical law is slow. It identifies the role of a
quantitative property specific to that canonical construction.

## What was attempted and not obtained

The intended proof was to transfer actual real-boundary information into
an actual-source residue collision upper. Coupling gives an exact
representation and the correct comparison scale. The needed quantitative
coalescence or direct arithmetic pair estimate is still missing.

The slow reweighting is a conditional deformation under the hypothetical
escaping-component premise. It is not an ordinary counterexample, an
independence theorem for Collatz, or a claim that every entropy method fails.

## Evidence

All new results are written proofs. No Lean theorem, numerical search, or
historical proof replay is claimed by this lane. Exact source scope is in
[SOURCES.json](SOURCES.json). The author used the primary Aldous–Fill
coupling statement and the pinned current proof files, including PR180's
new boundary extension and PR182's common pressure maximum.

The root coordinates independent review and publication. The scientific
claims and their scope are separate from checkout integrity checks.
