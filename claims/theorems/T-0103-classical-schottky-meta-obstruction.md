# T-0103 — Meta-obstruction for classical Schottky Collatz certificates

Claim ID: `T-0103`  
Title: Trichotomy for classical Schottky-style Collatz counterexample certificates  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0101`, `T-0102`, `L-0101`, `L-0108`, `L-0109`, `L-0110`, `L-0111`  
Scope: meta-theorem organizing the ping-pong packet’s negative surface  
Related counterexample candidates: none

## Statement

Call a counterexample certificate format **classical Schottky-style** if it is
one of:

1. a compact positive (or compact infinity-chart) IFS of accelerated inverse
   branches;
2. a finite forward automaton on a fixed dyadic modulus \(2^A\) with block
   labels of length \(\le A\);
3. an eventually periodic (or, for accounting purposes, arbitrary morphic)
   schedule of accelerated blocks with supercritical cyclic concatenation,
   relying on that periodicity to close;
4. a pure power-of-two port / multi-port calculus without growing prepaid state.

Then:

**Trichotomy.** Any classical Schottky-style attempt to produce an ordinary
positive divergent Collatz orbit fails in at least one of the following ways:

- **(Geom)** the real IFS domain cannot be a compact positive set
  (`L-0101`, `L-0102`, `L-0109`);
- **(Det)** the forward finite dyadic format has no branching and reduces to a
  deterministic residue orbit (`L-0108`, `T-0101`(E));
- **(Per)** an expanding periodic (hence also the cyclic part of an eventually
  periodic) realization is a negative rational 2-adic point, not a positive
  integer (`T-0101`(D), `L-0107`);
- **(Tax)** every 2-power enabling constraint taxes bits, odd transport does
  not refund them, and morphic / multi-chart generation does not cancel the
  tax (`T-0101`(A), `L-0110`, `L-0111`).

Consequently, a surviving constructive path must leave classical Schottky-style
formats and use at least one of:

- **growing prepaid state / growing geometry** (bridge: `directions/D-BRIDGE-growing-geometry-tax.md`);
- **non-residue certificate structure** (e.g. heteroclinic/adelic scaffolds);
- **subcritical cycle search** (algebraic cycle handoff), which is not a
  Schottky divergence certificate.

## Motivation

Stops further local rediscovery of dead Schottky subclasses and points agents
at the escape hatches.

## Proof

Case analysis on the four format families, citing the listed lemmas/theorems.
The “consequently” list is the logical complement relative to this packet’s
explored formats, not an exhaustive classification of all mathematics.

## Gap audit

- “Classical Schottky-style” is deliberately scoped; clever formats may sit
  outside the four bullets.
- Does not resolve Collatz.
- Complementary-domain free-group ping-pong on \(\mathbb{RP}^1\) is not fully
  inside (Geom) if domains are noncompact complements — noted as residual in
  `C-0101`.

## Adversarial tests

Packet experiments `X-0101`–`X-0114` instantiate each failure mode.

## Suggested next attack

Pursue a bridge issue; do not open new classical Schottky subclasses without
first showing they escape the trichotomy.
