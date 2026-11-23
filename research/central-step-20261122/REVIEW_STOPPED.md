# Independent review of the stopped-law argument

Reviewed: [STOPPED_MIXING.md](STOPPED_MIXING.md), Sections 1--5, against
the frozen PR180 common-reference formulas B25--B37 and the PR185 exact
inverse path-law comparison. The sibling precision formulas were also
checked algebraically. This review does not re-certify the upstream
analytic construction or claim that its inputs have been formalized.

**Result: no blocking mathematical error found in the uniform
excess-clock harmonicization theorem.** Its scope is the displayed
unchanged original-source family and the canonical monotone excess
\(P^mV-G\).

## Original sources and finite domination

The bound \(C(p)\le C_0p^{5/2}\), together with
\(p_n=\pi(n)\le2n\), gives
\[
\sum_n n^{-4}C(p_n)
\le 2^{5/2}C_0\sum_n n^{-3/2}<\infty.
\]
Thus \(Z\) and the pair measure \(\Xi\) are finite. Colliding labels remain
separate in this estimate; no weight is replaced by a function of the
current forward endpoint. Omitting labels killed by the specified
periodic boundary only reduces the positive sums.

The complete Radon--Nikodym comparison gives
\(\mu_q^G\le\delta^{-1}\mu_q^\nu\), so one factor
\(\delta^{-1}\), as written, is sufficient. The original-source constant
\(C(p)\) controls every retained forward root because the future-contact
count decreases and \(\nu\) increases along the path.

## Domain, component clock, and tail

An inverse parent of a retained nonperiodic state cannot itself be
periodic. Restricting to unit parents is compatible with the critical
law because \(V\) and \(G\) vanish on nonunits.

For eventually killed components, the component in the note is the
connected component of the retained graph; deleting periodic vertices
may split a larger ordinary basin into several such components. Minus
the number of steps to the exit is a valid clock on each one.

The sign is correct:
\[
h_C(x)+\tau=h_C(p)+k
\quad\Longrightarrow\quad
\tau-k=h_C(p)-h_C(x).
\]
Every individual clock difference is finite. Continuity from above for
the finite measure \(\Xi\) therefore proves \(\Gamma(r)\to0\), and gives
the stated supremum over all forward clocks without a mean hitting-time
assumption.

## Bounded stopping and the density distinction

The identity \(K_Gv_m=v_{m+1}\), nonnegativity, and
\(0\le v_m\le2\chi-1\) validate the martingale stopped at
\(\tau\wedge(k+r)\). Its remaining index on the hit event is at least
\(m\); monotonicity gives the endpoint bound \(v_m(X_\tau)\).
The complementary event has the stated constant bound. Stopping is
bounded, including when \(k+r=0\).

Summing the actual endpoint estimate gives precisely
\(ZA(m)+(2\chi-1)\Gamma(r)\). Taking
\(m=\lfloor R/2\rfloor\) and \(r=R-m\) proves the uniform limit.

For finite densities, the separate requirement \(m\ge1\) correctly
avoids the nonunit contribution at \(D_0\). The oscillation bound is
\(4\chi\), not \(8\chi\), because both nonnegative normalized densities
lie in \([0,4\chi]\). The note correctly leaves the ordinary endpoint
oscillation unproved rather than replacing it by Haar convergence.

## Strict first return

If the current root is a contact, taking one inverse edge raises the
endpoint layer to \(\ell(q)+1\); otherwise the strict entrance has layer
\(\ell(q)\). Consequently the uniform original-root bound with
\[
C^+(p)=\frac1{\kappa c_{\ell(p)+1}\nu(p)}
\]
is valid. Its growth is still \(O(p^{5/2})\). The same proof works after
defining \(Z^+\), \(\Xi^+\), and \(\Gamma^+\) using this enlarged constant.
This is a notation clarification: the strict-return statement should
not be read as retaining the smaller numerical \(Z,\Gamma\) from first
entrance.

## Interaction with closure

The displayed finite-floor horizon depends on the fixed ancestral
minimum. The new actual inverse horizon is \(k+R\). The latter eventually
outgrows any fixed finite-floor horizon, as the note states. Raising the
floor removes old source atoms and introduces a boundary term; it is
not a legitimate way to discard their amplitude.

The strict versus weak clock inequalities in the companion
[CRITICAL_BOUNDARY.md](CRITICAL_BOUNDARY.md) are consistent with this
argument. Excess-clock harmonicization approaches the positive canonical
profile on a hypothetical escaping path. It supplies no estimate forcing
the canonical escape charge or capacity to vanish.

The sibling residue cycle and geometric-period identities are
algebraically consistent. Their finite-density diagnostic is explicitly
kept separate from a claim about the full canonical \(G\), which is the
necessary distinction.
