# Candidate counterexamples

Last updated: 2026-07-21

There is currently **no candidate positive integer** and no finite symbolic construction proved to define an infinite positive-integer Collatz trajectory.

## Candidate-adjacent mechanisms

The collision charts `O-0001` through `O-0008` are conditional counterexample mechanisms. An infinite accepted orbit beginning from one ordinary finite state would lift to a positive Collatz counterexample, but no such orbit has been established.

The repository now supplies abundant finite and symbolic resources:

- universal finite-horizon stack amplification;
- exponentially unbounded supercritical branch count;
- arbitrary finite 3-adic precision;
- preservation of finite alphabet geometry;
- complete projection modulo \(2^b\) for every \(b\);
- exact negative-template return interpretations;
- graph-directed expansion with compensated local contraction;
- exact synchronous coupling to moving negative phases;
- countable cycle-padded return towers;
- renewal-pressure and Kraft conservation laws;
- an exact phase-survival Doob transform with positive symbolic Collatz drift.

None receives a `K-####` identifier because none selects one finite starting state that survives indefinitely.

## Current preferred candidate format: escape-weighted phase graph plus padding stack

A future candidate may consist of:

1. a finite set of negative phase targets
   \[
   -v_i;
   \]
2. a finite control graph of mismatch/recovery types;
3. one or more nonnegative cycle-padding counters;
4. exact return towers
   \[
   T^{L_e(t)}(q-v_i)=F_{e,t}(q)-v_j;
   \]
5. exact dyadic cylinders describing the admissible values of \(q\);
6. a deterministic stack or substitution rule mapping every accepted state to another accepted state;
7. one explicit finite quotient \(q_0>v_i\) initializing the grammar;
8. a phase-potential or cycle-product certificate showing that every reachable grammar cycle expands;
9. a pressure audit distinguishing the exceptional accepted language from complete renewal coverage;
10. an escape-likelihood audit comparing selected edge frequencies with
    \[
    \mathbb Q_v(e)=\frac{S_e(v)-1}{2(v-1)}.
    \]

The positive starting integer is

\[
n_0=q_0-v_i.
\]

`T-0014` supplies the exact one-step phase/difference dynamics. `L-0013` gives the rounded physical-parity phase maps. `T-0015` supplies cycle-padding towers. `T-0013` supplies graph expansion, `T-0016` supplies fair and growth pressure, and `T-0017` supplies phase escape pressure.

## Three exact path weights

For a physical parity word \(w\), a candidate grammar should record:

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

A complete broad grammar has negative typical Collatz logarithmic drift and fair phase absorption at \(1\). A viable candidate must be incomplete, exceptional, pressure-positive, and arithmetically nonempty in ordinary integers.

## Equivalent negative-return graph format

More generally, a candidate may use a finite-state or regular infinite language of negative return templates

\[
T^{L_e}(-u_e)=-v_j
\]

with exact cylinders and maps

\[
q\equiv v_i-u_e\pmod{2^{L_e}},
\qquad
F_e(q)=3^{a_e}\frac{q-v_i+u_e}{2^{L_e}}.
\]

It must define a deterministic forward-invariant family of ordinary quotient sets, contain one explicit ordinary quotient, and certify unbounded growth.

## Equivalent run-length format

`T-0004` gives another candidate description by one finite initial triple

\[
(d_0,u_0,C_0)
\]

and a rigorously closed infinite chain

\[
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1}.
\]

The negative-shadow equation

\[
Nq=Mq'+a
\]

is often the simpler first-order representation of the same boundary transport.

## Leading finite testbeds

### O-0008 — complement atlas of the negative eleven-cycle

The finite control states are the eleven cycle phases. One mismatch followed by synchronized recovery either returns to the eleven-cycle or descends to the negative three-cycle. Complete cycle padding gives countable exact edge towers.

This is the leading phase-plus-counter prototype. The next version should choose tower edges according to the phase escape likelihood rather than fair frequency.

### O-0007 — stationary negative-136 chart

The fixed-phase chart has

\[
M=2048,
\qquad N=2187,
\qquad A=\{0,2,4,5\}.
\]

Digit zero is one full circuit of the negative eleven-cycle. This remains the cleanest stationary signed-radix testbed.

### O-0005 — large finite repair alphabet

The 339-branch chart has rich finite modular geometry but a stationary aspect ratio of only about

\[
3.26\cdot10^{-9}.
\]

It may be useful as a rare repair component rather than a stationary grammar.

## Non-negotiable candidate checks

A future `K-####` file must prove:

- one finite positive starting integer exists explicitly;
- every selected word agrees with the unique deterministic Collatz trajectory;
- the selector and every padding-counter update are defined forever;
- no inverse-limit or nonordinary 2-adic point is substituted for an integer;
- positivity holds at every phase boundary;
- every reachable grammar cycle has justified net growth, including repair edges;
- the exceptional language actually contains the stated ordinary start;
- positive escape or tilted pressure is converted into actual ordinary trajectory growth;
- the trajectory is unbounded or otherwise avoids the terminal cycle forever.
