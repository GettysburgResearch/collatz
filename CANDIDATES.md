# Candidate counterexamples

Last updated: 2026-07-21

There is currently **no candidate positive integer** and no finite symbolic construction proved to define an infinite positive-integer Collatz trajectory.

## Candidate-adjacent mechanisms

The collision charts `O-0001` through `O-0008` are conditional counterexample mechanisms. An infinite accepted orbit beginning from one ordinary finite state would lift to a positive Collatz counterexample, but no such orbit has been established.

The repository now supplies abundant finite resources:

- universal finite-horizon stack amplification;
- exponentially unbounded supercritical branch count;
- arbitrary finite 3-adic precision;
- preservation of finite alphabet geometry;
- complete projection modulo \(2^b\) for every \(b\);
- exact negative-template return interpretations;
- graph-directed expansion with compensated local contraction;
- exact synchronous coupling to moving negative phases;
- countable cycle-padded return towers;
- renewal-pressure and Kraft conservation laws.

None receives a `K-####` identifier because none selects one finite starting state that survives indefinitely.

## Current preferred candidate format: phase graph plus padding stack

A future candidate may consist of:

1. a finite set of negative phase targets
   \[
   -v_i;
   \]
2. a finite control graph of mismatch/recovery types;
3. one or more nonnegative cycle-padding counters \(t\);
4. exact return towers
   \[
   T^{L_e(t)}(q-v_i)=F_{e,t}(q)-v_j;
   \]
5. exact dyadic cylinders describing the admissible values of \(q\);
6. a deterministic stack or substitution rule that maps every accepted state to another accepted state;
7. one explicit finite quotient \(q_0>v_i\) initializing the grammar;
8. a phase-potential or cycle-product certificate showing that every reachable grammar cycle expands;
9. a pressure audit distinguishing the exceptional accepted language from typical complete renewal coverage.

The positive starting integer is

\[
n_0=q_0-v_i.
\]

`T-0014` gives the exact one-step phase/difference dynamics. `T-0015` supplies the cycle-padding towers. `T-0013` supplies graph expansion, and `T-0016` supplies the fair and tilted pressure operators.

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

It must define a deterministic forward-invariant family of ordinary quotient sets \(S_i\), contain one explicit \(q_0\in S_i\), and certify unbounded growth.

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

is often the simpler first-order representation of the same transport.

## Leading finite testbeds

### O-0008 — complement atlas of the negative eleven-cycle

The finite control states are the eleven cycle phases. One mismatch followed by synchronized recovery either returns to the eleven-cycle or descends to the negative three-cycle. Complete cycle padding gives countable exact edge towers.

This is the leading phase-plus-counter prototype, but its supercritical thresholds are high and no closed stack rule is known.

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

## Pressure obligations

For graph edges \(e:i\to j\), a candidate should record

\[
\mathcal A_s(i,j)=\sum_{e:i\to j}2^{-L_e}\lambda_e^s.
\]

The fair matrix \(\mathcal A_0\) measures 2-adic cylinder mass; the tilted matrix \(\mathcal A_1\) measures Collatz growth weight. A complete broad cover has negative typical logarithmic drift by `T-0016`, so a valid counterexample must live in an exceptional pressure-positive language.

## Non-negotiable candidate checks

A future `K-####` file must prove:

- one finite positive starting integer exists explicitly;
- every selected word agrees with the unique deterministic Collatz trajectory;
- the selector and every padding-counter update are defined forever;
- no inverse-limit or nonordinary 2-adic point is substituted for an integer;
- positivity holds at every phase boundary;
- every reachable grammar cycle has justified net growth, including repair edges;
- the exceptional language actually contains the stated ordinary start;
- the trajectory is unbounded or otherwise avoids the terminal cycle forever.
