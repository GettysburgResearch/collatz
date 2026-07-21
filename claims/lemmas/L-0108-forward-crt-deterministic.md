# L-0108 — Forward finite CRT Schottky is a deterministic functional graph

Claim ID: `L-0108`  
Title: Length-\(L\) words biject with residues mod \(2^L\); forward CRT automata have out-degree one  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `D-0103`  
Scope: forward finite CRT automata with edge labels of length \(L\le A\)  
Related counterexample candidates: none (structural reduction)

## Statement

1. For each \(L\ge1\), the map \(w\mapsto r(w)\) is a bijection between
   chronological parity words of length \(L\) and residues modulo \(2^L\).

2. Consequently, in a finite CRT Schottky automaton modulo \(M=2^A\)
   (`D-0103`) whose edges are words of length \(L\le A\) enabled by the
   current state, each state enables **at most one** word of each fixed
   length \(L\).

3. Taking single-step edges (\(L=1\)), the automaton is exactly the
   functional graph of \(T\) acting on \(\mathbb Z/2^A\mathbb Z\): every
   node has out-degree one. Variable-\(L\) accelerations are deterministic
   paths in that same functional graph.

4. Therefore a forward finite CRT “Schottky” system has **no branching**.
   Any infinite run’s state sequence is the unique \(T\)-orbit of its start
   residue. Label aperiodicity cannot arise from nondeterministic edge
   choice at fixed \(L\); the only residual forward question is whether
   some ordinary positive integer’s deterministic residue orbit realizes an
   infinite supercritical density schedule — which for purely periodic
   residue cycles reduces to `L-0107`.

## Proof

(1) Distinct words produce distinct parity constraints, hence distinct
residues; there are \(2^L\) words and \(2^L\) residues, so the map is
bijective. Equivalently, the first \(L\) shortcut parities of an integer are
exactly its residue mod \(2^L\) (Terras coding).

(2) Enablement at state \(r\bmod 2^A\) for a word of length \(L\) requires
\(r\equiv r(w)\pmod{2^L}\). By (1) there is at most one such \(w\).

(3) For \(L=1\), the unique enabled bit is the parity of \(r\), and the
unique successor is \(T(r)\bmod 2^A\).

(4) Immediate from out-degree one.

## Motivation

Prevents wasting further search on “branching forward Schottky automata”
with fixed dyadic modulus. Branching exists only in the **inverse** Collatz
graph (or in multi-chart / collision-fiber side constraints).

## Dependency audit

- Parity/residue coding: `D-0101` / classical Terras.
- Format: `D-0103`.

## Gap audit

- Does not kill inverse-branch Schottky designs.
- Does not kill automata whose states include odd moduli \(3^B\) with
  nondeterministic decoding — still, Collatz forward dynamics remains
  deterministic on \(\mathbb Z\).
- Collision fibers create forward nondeterminism only after quotienting by
  a radix identification, which is the other packet’s setting.

## Adversarial tests

`X-0112`: shortcut graph mod \(2^A\) is a functional graph; “Markov branching
subshifts” of forward edges do not exist beyond subset restrictions of a
deterministic path.

## Remaining uncertainty

None for the bijection / out-degree claims.

## Suggested next attack

Inverse-branch integer ping-pong (`X-0113`), or explicitly reduce `C-0101`’s
forward finite-CRT subclass to classical supercritical subshift survivors.
