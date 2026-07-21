# Packet: Affine ping-pong / Schottky certificates

Agent: `grok45-01`  
Branch: `cursor/affine-pingpong-schottky-a643`  
PR: https://github.com/gfreund123/collatz/pull/11  
Date: 2026-07-21  
Issue: unavailable via API (claim recorded in `directions/D-PINGPONG-schottky-certificates.md`)

## Mission link

Construct a Collatz counterexample certificate using affine ping-pong / Schottky
methods, orthogonal to collision-fiber carry regeneration and AYH tropical
templates.

## Claim ledger (packet-local)

| ID | Type | Title | Status | File |
|---|---|---|---|---|
| D-0101 | Definition | Affine Collatz blocks | PROPOSED | `claims/definitions/D-0101-affine-collatz-blocks.md` |
| D-0102 | Definition | Schottky system formats | IDEA | `claims/definitions/D-0102-schottky-system.md` |
| D-0103 | Definition | Finite CRT Schottky automaton | IDEA | `claims/definitions/D-0103-finite-crt-schottky.md` |
| L-0101–L-0109 | Lemmas | Classical Schottky obstructions | PROPOSED | `claims/lemmas/` |
| L-0110 | Lemma | Morphic/S-adic schedules obey accounting | PROPOSED | `claims/lemmas/L-0110-morphic-schedule-accounting.md` |
| L-0111 | Lemma | Multi-chart schedules still pay tax | PROPOSED | `claims/lemmas/L-0111-multichart-tax.md` |
| **T-0101** | Theorem | Unified precision accounting | PROPOSED | `claims/theorems/T-0101-precision-accounting.md` |
| **T-0102** | Theorem | Digit-transfer Schottky obstruction / bridge | PROPOSED | `claims/theorems/T-0102-digit-transfer-schottky-obstruction.md` |
| **T-0103** | Theorem | Classical Schottky meta-obstruction trichotomy | PROPOSED | `claims/theorems/T-0103-classical-schottky-meta-obstruction.md` |
| O-0101 | Observation | Finite shadows / greedy deaths | EMPIRICAL | `claims/observations/O-0101-finite-schottky-shadows.md` |
| C-0101 | Conjecture | Schottky certificate exists | IDEA (restricted) | `claims/conjectures/C-0101-schottky-counterexample.md` |
| C-0102 | Conjecture | Universal precision drain | SUPERSEDED | `claims/conjectures/C-0102-universal-precision-drain.md` |
| M-0101 | Methodology | `directions/` handoff convention | PROPOSED | `claims/methodology/M-0101-directions-directory.md` |
| X-0101…X-0115 | Experiments | Through digit-transfer periodic checks | EMPIRICAL | `experiments/X-010*` |

## Headline results

1. **T-0101** unifies tax additivity, unique cylinders, inverse limits, expanding
   periodic ⇒ negative fp, and finite prepaid-state constraints.
2. **T-0102** ports the obstruction surface onto digit-transfer charts \(H_D\)
   and states the bridge trichotomy toward growing geometry.
3. **T-0103** meta-theorem: classical Schottky-style formats fail via
   Geom / Det / Per / Tax; escape hatches listed.
4. **L-0110 / L-0111**: morphic and multi-chart schedules do not cancel tax.
5. Empirics (`X-0114`): 40/40 random schedules tax\(=\sum L\); 8/8 supercritical
   concatenations have negative fps; cylinders unique. (`X-0115`): periodic
   digit streams on `64→81` and `512→729` charts all negative fps.

## Directions / bridges

- Unclaimed: heteroclinic, algebraic cycle (`directions/`)
- **New bridge:** `directions/D-BRIDGE-growing-geometry-tax.md`
  (Q-0010 ↔ tax language)

## No candidate counterexample

No `K-####`. Classical Schottky inside this packet is organized as exhausted
under `T-0103`.
