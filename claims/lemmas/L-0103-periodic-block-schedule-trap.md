# L-0103 — Periodic block schedules cannot certify aperiodic divergence

Claim ID: `L-0103`  
Title: A purely periodic schedule of accelerated blocks yields an eventually periodic parity word  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`  
Scope: finite block alphabets with periodic infinite schedules  
Related counterexample candidates: none (obstruction to a certificate format)

## Statement

Let \(w_1,\ldots,w_m\) be finite chronological parity words, and let
\(\sigma\in\{1,\ldots,m\}^{\mathbb N}\) be an eventually periodic sequence.
The concatenated parity word

\[
W=w_{\sigma_0}w_{\sigma_1}w_{\sigma_2}\cdots
\]

is eventually periodic as a bitstring.

Consequently any integer orbit that follows \(W\) forever has an eventually
periodic shortcut-parity itinerary.

## Proof

If \(\sigma\) is eventually periodic with period \(p\) after time \(T\), then
the block concatenation after the corresponding finite prefix is the endless
repetition of the finite bitstring \(w_{\sigma_T}\cdots w_{\sigma_{T+p-1}}\),
hence eventually periodic.

## Motivation

Integer Schottky searches that close as expanding self-loops or expanding
2-cycles at the block level produce periodic schedules. Those are the wrong
shape for an aperiodic divergent ordinary orbit. They remain relevant only as
cycle candidates (subcritical composed fixed points) or as finite shadows.

## Dependency audit

- Purely combinatorial; no Collatz dynamics beyond the meaning of parity words.

## Gap audit

- Does not by itself reprove the collision-fiber packet’s aperiodicity theorem
  for induced radix orbits; it only constrains certificate schedules.
- Aperiodic schedules (Sturmian, morphic, automaton-driven) are not ruled out.

## Adversarial tests

`X-0103` / `X-0105` expanding self-loops and attempted 2-cycles instantiate the
trap; concrete “alternators” in `X-0105` fail once the forced periodic residue
pattern breaks (`O-0101`).

## Remaining uncertainty

None for the combinatorial statement.

## Suggested next attack

Require certificate automata whose accepted languages contain aperiodic
infinite words, and prove height expansion along every accepted word.
