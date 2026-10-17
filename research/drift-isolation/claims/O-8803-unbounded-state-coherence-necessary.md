# O-8803 — Unbounded-state coherence is necessary

Claim ID: O-8803  
Title: Finite local realizability plus bounded-state failure forces an unbounded coherence problem  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-8811, R-8802, O-8802  
Scope: methodological consequence for the exact `4 -> 5` chart  
Related counterexample candidates: issue #26; no `K-####` candidate

## Observation

The exact chart has the following paired boundary:

1. every finite legal binary directive is realized by infinitely many positive
   roots (`L-8811`);
2. no autonomous deterministic finite-state directive generator can select a
   positive infinite survivor (`R-8802`);
3. an infinite survivor exists exactly when the nested least positive roots
   remain bounded, equivalently eventually stabilize (`O-8802`).

Therefore the missing information is neither a finite forbidden word nor a
bounded autonomous control state. It is the unbounded arithmetic coherence
required to keep one ordinary root inside all nested cylinders.

## Consequences

A positive construction must use a genuinely non-eventually-periodic directive
and retain unbounded arithmetic information, for example a growing quotient,
carry, height, counter, stack, or recursively certified residue.

A negative proof must do more than reject every bounded prefix separately. It
must prove a global statement such as

```text
m_n -> infinity,
```

where `m_n` is the least positive depth-`n` root, or provide an equivalent
ranking/Diophantine obstruction tied to one root at all depths.

## Status boundary

This is a synthesis of proved/proposed interfaces, not a theorem that every
unbounded-state construction fails. It does not privilege a positive or
negative resolution.

## Suggested next attack

Use the exact composition law of `L-8804` to search for a recursive height
inequality on `m_n`, or deliberately construct an aperiodic nested residue whose
least representatives stabilize.
