# D-8802 — Autonomous finite-state directive generator

Claim ID: D-8802  
Title: Autonomous deterministic finite-state directive generator  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: none  
Scope: autonomous deterministic finite-state generators over a finite output alphabet  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

An **autonomous deterministic finite-state directive generator** is a quadruple

```text
G=(Q,q_0,sigma,o)
```

where:

- `Q` is a finite nonempty state set;
- `q_0 in Q` is the initial state;
- `sigma:Q->Q` is a deterministic transition map;
- `o:Q->{0,1}` is an output map.

It emits the directive

```text
eps_n=o(sigma^n(q_0)),  n>=0.
```

Every directive emitted by such a generator is eventually periodic.

## Definitions

- **Autonomous** means that the transition receives no external input stream.
- A directive is **eventually periodic** when there exist `N>=0` and `p>=1`
  such that `eps_(n+p)=eps_n` for every `n>=N`.
- The state set must remain fixed and finite for the entire infinite run.

## Proof

The state sequence

```text
q_0, sigma(q_0), sigma^2(q_0), ...
```

takes values in finite `Q`. Hence two states repeat: there exist `0<=i<j` with

```text
sigma^i(q_0)=sigma^j(q_0).
```

Determinism gives

```text
sigma^(i+k)(q_0)=sigma^(j+k)(q_0)
```

for every `k>=0`. Applying `o` proves eventual periodicity with preperiod `i`
and period dividing `j-i`. **QED**

## Dependency audit

None.

## Gap audit

This definition does not include:

- transducers driven by an external aperiodic input;
- counters, stacks, queues, or tapes with unbounded content;
- state spaces that grow with depth;
- arithmetic algorithms retaining an unbounded integer quotient or carry;
- nondeterministic systems unless one deterministic infinite run is separately
  selected.

Those systems need not emit eventually periodic directives.

## Adversarial tests

Any functional graph on a finite set consists of directed cycles with finite
in-trees. Starting at any node therefore reaches one cycle after finitely many
steps, which is the graph-theoretic form of the proof.

## Remaining uncertainty

None in the definition or eventual-periodicity conclusion.

## Suggested next attack

Combine this definition with `T-8812` to delimit exactly which bounded-state
certificate formats cannot select a positive ordinary completion.
