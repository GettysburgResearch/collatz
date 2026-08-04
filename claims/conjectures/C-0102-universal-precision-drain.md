# C-0102 — Universal precision drain for odd-multiplier port transitions

Claim ID: `C-0102`  
Title: Odd-multiplier transitions between power-of-two ports force unbounded modulus for infinite walks  
Status: `SUPERSEDED` (resolved by `L-0105` for the power-of-two port class)  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `L-0104`, `L-0105`  
Scope: historical conjecture; see `L-0105`  
Related counterexample candidates: none

## Statement

Originally conjectured universal precision drain for odd-multiplier
power-of-two image ports. That statement is now proved as `L-0105`.

Residual open form: classify whether non-power-of-two ports can regenerate
2-adic precision while keeping height expansion on an aperiodic language
(`C-0101`).

## Motivation

Retained for ledger continuity.

## Proof or construction

See `L-0105`.

## Gap audit

- Needs precise quantifiers on “transition class” and “precision-neutral”.
- Must not silently assume the collision-fiber packet’s theorems.

## Suggested next attack

Prove the index-\(2^{L'}\) thinning lemma for a single transition in full
generality, then iterate.
