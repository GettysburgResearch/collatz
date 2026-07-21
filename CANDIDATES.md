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
- a phase-survival Doob transform with positive symbolic drift;
- an exact finite-interval lift;
- a critical particle completion whose distinguished spine is ordinary Collatz.

None receives a `K-####` identifier because none selects one finite starting state that survives indefinitely.

## Current preferred candidate format: two-layer marked rewrite grammar

A future candidate should consist of one finite interval or particle population together with one distinguished marker.

### Layer 1 — unmarked population or interval

The unmarked layer may use:

- a finite interval
  
  \[
  [v,q),
  \qquad q-v=n;
  \]
- an ordered population
  
  \[
  [x]=\{1,\ldots,x\};
  \]
- negative-cycle phases and padding counters;
- collision-code or mixed-radix macro-tiles.

This layer should regenerate and carry a positive growth, pressure, or phase potential.

### Layer 2 — marked ordinary spine

One finite root particle \(j_0\) is marked. Every rewrite must send it through the distinguished child

\[
\chi(j)=
\begin{cases}
(0,j/2),&j\text{ even},\\[1mm]
(1,(3j+1)/2),&j\text{ odd}.
\end{cases}
\]

The marked ranks are therefore exactly

\[
j_0,T(j_0),T^2(j_0),\ldots.
\]

The grammar must prove that this marked lineage is defined forever and unbounded.

This format certifies the ordinary starting integer at the beginning rather than trying to recover it later from an unmarked or adic escape path.

## Equivalent endpoint format

By `L-0014`, a candidate may instead carry finite endpoints

\[
I_t=[v_t,q_t)
\]

with exact rewrites

\[
[v,q)
\mapsto
[\lceil v/2\rceil,\lceil q/2\rceil)
\]

for even length and

\[
[v,q)
\mapsto
[\lfloor3v/2\rfloor,\lceil3q/2\rceil)
\]

for odd length.

The physical Collatz state is the finite interval length

\[
n_t=q_t-v_t.
\]

A negative-cycle gauge may simplify the lower endpoint, but the upper endpoint or marked boundary must remain explicit.

## Equivalent phase graph plus padding stack

A candidate may still use:

1. finite negative phase targets \(-v_i\);
2. mismatch/recovery types;
3. cycle-padding counters;
4. exact return towers;
5. graph-cycle or phase-potential expansion.

However, every accepted return edge must also specify how the distinguished ordinary marker is transported. Unmarked phase closure is not enough.

## Exact path weights

For a physical parity word \(w\), a candidate grammar may use the following search scores.

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

### Ordinary marked-spine mass

For root population \([n_0]\), the one marked descendant of the specified root has mass

\[
\mu_{\mathrm{marked}}(L)=\frac1{2^Ln_0}.
\]

The escape and growth weights rank unmarked populations. Only the marked layer certifies one ordinary finite trajectory.

## Leading finite testbeds

### Critical particle completion

`T-0018` is now the most direct string-rewrite testbed. Adjacent parent pairs produce one branch-zero and three branch-one children, while a distinguished marker follows the physical Collatz child.

### O-0008 — negative eleven-cycle padding towers

The unmarked phase-plus-counter structure is rich and exact. The next task is to lift every tower edge to the marked particle layer.

### O-0007 — stationary negative-136 chart

The chart

\[
M=2048,
\qquad N=2187,
\qquad A=\{0,2,4,5\}
\]

remains the cleanest stationary signed-radix gauge.

### O-0005 — large finite repair alphabet

The 339-branch chart may be useful as a rare unmarked repair component, but it still needs an ordinary marker transport rule.

## Non-negotiable candidate checks

A future `K-####` file must prove:

- one finite positive starting integer exists explicitly;
- every selected word agrees with the unique deterministic Collatz trajectory;
- the marker is sent through the distinguished child forever;
- the population/interval and marker rules remain compatible;
- no inverse-limit or nonordinary 2-adic point is substituted for the marker;
- positivity holds at every physical boundary;
- every reachable grammar cycle has justified net growth, including repair edges;
- pressure or escape claims are not substituted for marked-rank growth;
- the marked trajectory is unbounded or otherwise avoids the terminal cycle forever.
