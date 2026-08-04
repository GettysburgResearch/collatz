# D-0103 — Finite CRT Schottky automaton

Claim ID: `D-0103`  
Title: Fixed-modulus CRT Schottky automata as prepaid-precision certificates  
Status: `IDEA`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0102`, `L-0105`, `L-0106`  
Scope: certificate format avoiding unbounded modulus growth  
Related counterexample candidates: `C-0101`

## Statement

A **finite CRT Schottky automaton** is a finite directed graph \(\mathcal{A}\)
whose states are residues modulo a fixed modulus

\[
M=2^A\cdot 3^B\qquad(A,B\ge0),
\]

and whose edges are labeled by chronological parity words of length
\(L\le A\) (so the enabling constraint is already encoded in the state) together
with an exact affine update on the cover parameter \(q\) in
\(n=Mq+r\).

Because \(M\) is fixed, the automaton does not demand unbounded new 2-adic
precision along a run (`L-0105` taxes are prepaid by the state’s \(2^A\)
factor). A counterexample certificate in this format is an infinite accepted
run together with one ordinary seed \(n_0=Mq_0+r_0\) whose forward orbit
realizes the edge labels and whose height \(h(n)\to\infty\), with the label
stream not eventually periodic (`L-0103`).

## Motivation

After `L-0106`, odd-modulus regeneration is not a loophole. The remaining
integer format that avoids growing towers is a **finite** CRT state.

## Proof or construction

Definition only. Searches: `X-0111`.

## Gap audit

- Finite-state expanding cycles tend to collapse to `L-0107`.
- Aperiodic acceptance with ordinary lifts is the residual question inside
  `C-0101`.
- If \(L>A\) edges are forbidden by definition; allowing them reintroduces tax.

## Suggested next attack

Prove that every height-expanding infinite run in a finite CRT automaton is
eventually periodic in labels (hence killed by `L-0107`), or exhibit a
counterexample run.
