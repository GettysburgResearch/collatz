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
| L-0101 | Lemma | No positive-interval supercritical inverse Schottky | PROPOSED | `claims/lemmas/L-0101-no-positive-interval-schottky.md` |
| L-0102 | Lemma | No compact infinity-chart Schottky for supercritical \(h\) | PROPOSED | `claims/lemmas/L-0102-infinity-chart-no-compact-schottky.md` |
| L-0103 | Lemma | Periodic block schedules give periodic parity words | PROPOSED | `claims/lemmas/L-0103-periodic-block-schedule-trap.md` |
| L-0104 | Lemma | Precision drain on explicit pair `1111010`/`1101110` | PROPOSED | `claims/lemmas/L-0104-precision-drain-two-port.md` |
| L-0105 | Lemma | Odd-multiplier thinning + nested inverse-limit form | PROPOSED | `claims/lemmas/L-0105-odd-multiplier-thinning.md` |
| L-0106 | Lemma | Bit budget: odd transport does not regenerate free parameters | PROPOSED | `claims/lemmas/L-0106-bit-budget-no-regen.md` |
| L-0107 | Lemma | Expanding periodic schedules realize negative rational fixed points | PROPOSED | `claims/lemmas/L-0107-expanding-periodic-negative-fixed-point.md` |
| L-0108 | Lemma | Forward finite CRT automata are deterministic (no branching) | PROPOSED | `claims/lemmas/L-0108-forward-crt-deterministic.md` |
| L-0109 | Lemma | Compact inverse IFS on \(\{g_0,g_1\}\) impossible | PROPOSED | `claims/lemmas/L-0109-inverse-compact-ifs-obstruction.md` |
| O-0101 | Observation | Finite shadows / greedy deaths | EMPIRICAL | `claims/observations/O-0101-finite-schottky-shadows.md` |
| C-0101 | Conjecture | Schottky certificate exists | IDEA (severely restricted) | `claims/conjectures/C-0101-schottky-counterexample.md` |
| C-0102 | Conjecture | Universal precision drain | SUPERSEDED by L-0105 | `claims/conjectures/C-0102-universal-precision-drain.md` |
| M-0101 | Methodology | `directions/` handoff convention | PROPOSED | `claims/methodology/M-0101-directions-directory.md` |
| X-0101…X-0113 | Experiments | Census through inverse-branch probe | EMPIRICAL | `experiments/X-010*` |

Identifier range `*-0101`–`*-0199` is reserved for this packet.

## Headline results

### Session 1
1. Compact real Schottky dead (`L-0101`, `L-0102`).
2. Periodic two-port certificates wrong shape (`L-0103`, `L-0104`).
3. Power-of-two image ports thin uniquely (`L-0105`).

### Session 2 (continuation)
4. **Bit budget:** odd image moduli do not regenerate free 2-adic parameters; generic total tax equals total parity length (`L-0106`, `X-0110`).
5. **Expanding periodic schedules** realize only their negative rational fixed point (`L-0107`).
6. **Forward finite CRT Schottky has no branching** — residues biject with words; the dyadic shortcut graph is a functional graph (`L-0108`, `X-0112`).
7. **Elementary inverse IFS** on \(\{g_0,g_1\}\) cannot live on a compact positive set; pure \(g_1\) attracts to \(-1\) (`L-0109`, `X-0113`).
8. Classical Schottky formats inside this packet are largely exhausted; `C-0101` survives only in bridge / non-classical forms.

## Unclaimed directions published for others

- `directions/D-HETEROCLINIC-adelic-interpolation.md`
- `directions/D-CYCLE-algebraic-hunt.md`

## Recommended next steps (outside classical Schottky)

1. Bridge issue to collision-fiber growing geometry (`Q-0010`).
2. Claim heteroclinic or algebraic-cycle handoffs.
3. Serious complementary-domain Möbius argument on \(\mathbb{RP}^1\) (still weakly open).

## No candidate counterexample

No `K-####` is claimed. No proof of the Collatz conjecture’s negation is claimed.
