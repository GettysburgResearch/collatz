# Candidate counterexamples

Last updated: 2026-07-21

There is currently **no candidate positive integer**, no regular sanctuary, and
no finite symbolic construction proved to define an infinite positive-integer
Collatz trajectory.

## Literature-informed boundary

The literature-review branch and PR #12 change the interpretation of the
marked interval/particle route.

`L-0015` proves that regular finite endpoint or population languages have
regular ordinary marker projections. `T-0020` proves that finitely many regular
phase domains with fixed finite Collatz blocks compile to a one-step regular
sanctuary.

Therefore:

> A finite-state regular marked interval, marked-particle, carry-phase, or
> negative-target grammar is not a new existential class. It belongs to the
> exact regular-sanctuary program already implemented in PR #12.

Finite decoration may produce a clearer certificate, but it does not bypass the
ordinary marker problem.

## Current preferred candidate format: counter-stack marked sanctuary

A future candidate should carry one explicitly finite ordinary marker together
with one genuinely unbounded memory component.

A useful abstract state is

\[
(i,t,\rho,n),
\]

where:

- \(i\) is a finite negative phase or macro-rule type;
- \(t\ge0\) is an unbounded cycle-padding or valuation counter;
- \(\rho\) is a finite low-order residue/carry obligation;
- \(n\) is one ordinary marked positive integer.

A certified edge should have the form

\[
(i,t,\rho,n)
\longmapsto
(j,t+\Delta_e,\rho',T^{b_e(t)}(n)).
\]

Unlike a finite-state regular grammar, the block length and next residue
obligation may depend on the unbounded counter.

### Layer 1 — unmarked regenerative structure

The auxiliary layer may use:

- negative-cycle padding towers from `T-0015`;
- collision-code or mixed-radix relays;
- an ordered particle population from `T-0018`;
- graph-cycle potentials and tilted/escape pressure;
- a unary stack encoding valuation fuel.

It must prove regeneration and positive full-cycle growth.

### Layer 2 — marked ordinary spine

One finite root \(n_0\) is marked. Every macro-edge must replay the exact
shortcut trajectory and send the marker to

\[
T^{b_e(t)}(n).
\]

In the particle completion, the one-step distinguished child is

\[
\chi(j)=
\begin{cases}
(0,j/2),&j\text{ even},\\[1mm]
(1,(3j+1)/2),&j\text{ odd}.
\end{cases}
\]

The marker must remain explicit at every finite stage.

## What would still count as a regular-sanctuary candidate

Any proposal with all of the following should be compiled through `T-0020`
and checked by PR #12 rather than treated as a separate route:

1. finitely many phases;
2. regular canonical marker domains;
3. finitely many fixed block lengths;
4. rational finite-state extraction of the marker;
5. exact block closure among those regular domains.

Such a proposal is valuable only if the compiled sanctuary DFA passes the exact
certificate checker.

## What genuinely exceeds the regular class

At least one of the following is required:

- an unbounded pushdown stack;
- an unbounded padding/valuation counter;
- variable block lengths controlled by that memory;
- a genuinely nonregular ordinary survivor language;
- a non-rational marker/configuration coupling.

The negative eleven-cycle padding towers are currently the cleanest source of
such unbounded memory.

## Exact search scores

For a physical parity word \(w\), auxiliary search may track:

### Fair cylinder mass

\[
\mu_{\mathrm{fair}}(w)=2^{-|w|}.
\]

### Collatz growth tilt

\[
\mu_{\mathrm{growth}}(w)
=
2^{-|w|}\frac{3^{a(w)}}{2^{|w|}}.
\]

### Phase escape tilt

\[
\mu_{\mathrm{escape}}(w)
=
2^{-|w|}\frac{S_w(v)-1}{v-1}.
\]

### Fully marked descendant mass

For one specified root in a population of size \(n_0\),

\[
\mu_{\mathrm{marked}}(L)=\frac1{2^Ln_0}.
\]

The first three weights guide exceptional-language search. None replaces exact
marked-rank replay.

## Leading testbeds

### Negative eleven-cycle counter tower

`O-0008` and `T-0015` provide finitely many mismatch types and an unbounded
cycle-padding counter. This is the leading nonregular candidate architecture.

### Critical ordered-particle completion

`T-0018` supplies a finite local rewrite and an explicit ordinary marker. It is
the preferred marker layer for any counter-stack grammar.

### Regular controls

Every bounded counter truncation and every finite-state approximation should be
compiled through `L-0015`/`T-0020` and submitted to PR #12's exact verifier.
This gives concrete counterexample words and maximal safe kernels when the
approximation fails.

### Large finite repair alphabets

`O-0005` and the dyadic-projection charts remain possible rare repair
components, but they require a counter-compatible marker transport theorem.

## Non-negotiable candidate checks

A future `K-####` file must prove:

- one finite positive starting integer exists explicitly;
- every selected macro-word agrees with the unique deterministic Collatz
  trajectory;
- the marker is transported exactly forever;
- the counter/stack update is total on the accepted state set;
- the counter never becomes invalid or negative;
- every next residue/carry obligation is satisfied;
- no inverse-limit or nonordinary adic point is substituted for the marker;
- positivity holds at every physical boundary;
- every reachable grammar cycle has justified net growth, including repairs;
- pressure, attractor, or escape statements are not substituted for marked-rank
  growth;
- the trajectory is unbounded or permanently avoids the terminal cycle.
