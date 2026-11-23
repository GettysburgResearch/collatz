# Independent review: actual stationary real-series deductions

Reviewer: root agent. Date: 2026-11-23.

**Verdict: VERIFIED at the written scope.** Target:
`research/profound-step-20261123/STATIONARY_REAL.md`,
SHA-256 `0e2d6b1a718e46d5baf1acc60c1aebadc43826e642c8d2601e9b8c947479bad4`.

This review reconstructs the new logarithmic identities, drift
classification, finite-word transfer, and minimum-source information cost.
It retains the exact qualifications of the previously supplied stationary
lift and whole-path source; it is not a replay of those historical inputs.

## Logarithms and drift

The lower bound \(R_m\ge2^{-G_1}\) controls the negative logarithmic part
by \(G_1\log2\). The upper bound \((3/2)^m-1\) is deterministic.
The correction \(\log(1+1/(3R_m))\) is integrably dominated. Consequently
taking expectations in the finite recursion is legitimate and gives the
displayed identity without assuming an integrable logarithm of the infinite
series.

The lower-tail bound uses both monotonicities: \(R_k\) increases and its
correction decreases. Under *conditional* criticality, \(L_1=-\log3\)
cancels the factor \(1/3\) in the upper logarithmic bound. Birkhoff's
conditional theorem gives \(S_n/n\to0\), and
\(0\le M_n^+/n\le\log(3/2)\) supplies the required domination.
Thus the probability estimate tends to zero; increasing partial sums turn
this into almost sure divergence. The iid rate invokes the martingale
maximal inequality only in the previously established geometric equality
branch, whose variance is finite and has the stated value.

On negative conditional logarithmic drift, exponential convergence of the
series follows directly. On positive drift, its logarithmic growth rate is
that drift; on zero drift the preceding argument applies. The normalized
logarithms converge in \(L^1\) because their positive parts are uniformly
bounded and their negative parts have the explicit integrable bound divided
by \(m\). Cesaro averaging of the decreasing correction terms therefore
gives the exact positive/negative drift balance. An overall critical mean
is correctly distinguished from criticality on every invariant component.

## Finite ordinary words and atoms

The finite periodization is an averaging device with the original gaps
retained. The centered backward sum is \(B_j-B_{j-k}\); the common mean
drift and the initial logarithmic term cancel exactly. Phases
\(j=m,\ldots,N\) avoid the seam. The displayed ordinary word count retains
denominator \(N\), while its endpoint version uses \(N+1\) and discards
exactly \(m\) early clocks. The ordinary affine remainder bounds the
partial sum by the moving \(q_j\), not by a uniform real height.

The separate independent arithmetic-agent review reconstructs the atom
classification and this finite seam calculation. Root also checked that a
recurrent ternary atom has odd, nonzero denominator \(2^A-3^h\) and odd
carry. On the atomic event both consecutive values are rational 2-adic
units, so the gap is their exact valuation. The finite invariant atomic
measure is supported on rational cycles, not necessarily ordinary integer
cycles. Their rational means exclude them from a conditionally critical
component but not from an arbitrary mixture with merely a total mean bound.

## Minimum-source attempt and literature

The selected minimum is a strict forward scale record, so its first
descending ladder time is infinite. The whole-path conditional sampling
law has density at most \(1/p_0\) relative to uniform time times the common
path law. Each path has at most \(2L+1\) sampled clocks near its minimum,
which proves the estimate uniformly in the inverse clock.

For any alternative law assigning this event mass at least \(\rho\),
binary relative-entropy data processing gives
\(\rho\log(1/t)-\log2\), with the stated upper bound \(t\) on its original
probability. Infinite relative entropy and zero original event mass are
consistent with the claim.

The primary Brofferio–Buraczewski–Damek paper was opened and its iid driver,
critical invariant Radon measure, and moment assumptions checked. The note
does not assert that the deterministic future from the minimum verifies
those hypotheses. Its new calculations are direct stationary identities,
not an unjustified application of that renewal theorem.

No Lean formalization is claimed for these measure-theoretic results.
The first unresolved closing step remains a finite real realization on the
actual stationary law or a sufficient quantitative estimate on its original
ternary factor.
