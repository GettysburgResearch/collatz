Claim ID: D-9201  
Title: Finite-horizon shortcut safety language and canonical tail  
Status: PROPOSED  
Authoring agent: gpt56-sol-01  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: positive integers under the shortcut `3n+1` map  
Related counterexample candidates: none

## Statement

Let

$$
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
$$

For an integer `d >= 0`, define the forbidden and safe sets

$$
F_d=\{n\in\mathbb Z_{>0}:T^j(n)\in\{1,2\}
\text{ for some }j\in\{0,\ldots,d\}\},
$$

$$
S_d=\mathbb Z_{>0}\setminus F_d.
$$

Encode each positive integer by its unique finite binary word in
least-significant-digit-first order. A word is canonical exactly when it is
nonempty and ends in `1`.

For a finite forbidden set `F`, its **canonical tail component** means the two
left quotients reached after a prefix is not a prefix—including equality—of
any encoding in `F`:

- the residual after a prefix ending in `0`;
- the residual after a prefix ending in `1`.

On another input bit, either residual moves to the ending-`0` residual on `0`
and to the ending-`1` residual on `1`.

The **sink-stripped boundary** is the subgraph induced by all other states of
the minimal complete DFA for the canonical encodings of
$\mathbb Z_{>0}\setminus F$.

## Definitions

The time interval in `F_d` is inclusive: orbit states `0,1,...,d` are
inspected. This convention makes

$$
F_0=\{1,2\}.
$$

The DFA alphabet is `{0,1}` and all transitions read from least significant
to most significant bit. Noncanonical raw words are rejected.

## Motivation

Every regular Collatz sanctuary must be contained in every `S_d`. Finite
safety automata can therefore supply exact finite-horizon examples for
automata learning. The canonical tail distinguishes the cofinite artifact of
finite checking from the depth-dependent boundary where structural
information can occur.

## Proof or construction

This file introduces definitions only. Exact construction of the automata is
given in `experiments/X-9201-sink-stripped-safety/run.py`.

## Dependency audit

No earlier repository claim is used. The shortcut map and canonical binary
encoding are restated here.

## Gap audit

- Nonemptiness of every fixed-depth `S_d` is not asserted to imply
  nonemptiness of their infinite intersection.
- A finite word is never treated as an infinite 2-adic stream.
- "Tail" refers to DFA input behavior, not to a tail of a Collatz orbit.

## Adversarial tests

The experiment compares reverse-tree membership, direct shortcut iteration,
and DFA acceptance on bounded ranges. It also freezes independently obtained
state counts from draft PR #12.

## Remaining uncertainty

None in the definitions. The mathematical consequences are separated into
`L-9201`.

## Suggested next attack

Compare canonical, state-label-independent fingerprints of sink-stripped
boundary DAGs across successive depths and test any proposed widening with an
exact one-step closure checker.
