# Packet: Affine ping-pong / Schottky certificates

Agent: `grok45-01`  
Branch: `cursor/affine-pingpong-schottky-a643`  
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
| L-0101 | Lemma | No positive-interval supercritical inverse Schottky | PROPOSED | `claims/lemmas/L-0101-no-positive-interval-schottky.md` |
| L-0102 | Lemma | No compact infinity-chart Schottky for supercritical \(h\) | PROPOSED | `claims/lemmas/L-0102-infinity-chart-no-compact-schottky.md` |
| L-0103 | Lemma | Periodic block schedules give periodic parity words | PROPOSED | `claims/lemmas/L-0103-periodic-block-schedule-trap.md` |
| L-0104 | Lemma | Precision drain on explicit pair `1111010`/`1101110` | PROPOSED | `claims/lemmas/L-0104-precision-drain-two-port.md` |
| L-0105 | Lemma | Odd-multiplier thinning for all \(2^{L'}\) image ports | PROPOSED | `claims/lemmas/L-0105-odd-multiplier-thinning.md` |
| O-0101 | Observation | Finite shadows / greedy deaths | EMPIRICAL | `claims/observations/O-0101-finite-schottky-shadows.md` |
| C-0101 | Conjecture | Aperiodic integer Schottky certificate exists | IDEA | `claims/conjectures/C-0101-schottky-counterexample.md` |
| C-0102 | Conjecture | Universal precision drain | SUPERSEDED by L-0105 | `claims/conjectures/C-0102-universal-precision-drain.md` |
| M-0101 | Methodology | `directions/` handoff convention | PROPOSED | `claims/methodology/M-0101-directions-directory.md` |
| X-0101…X-0109 | Experiments | Census through complementary-domain probe | EMPIRICAL | `experiments/X-010*` |

Identifier range `*-0101`–`*-0199` is reserved for this packet to avoid
collisions with `*-0001` (collision-fiber bootstrap) and `*-9000`
(termination frontier).

## Headline results

1. **Naive real Schottky is dead:** supercritical inverse branches and
   infinity-chart forward maps preserve no compact positive interval
   (`L-0101`, `L-0102`).
2. **Periodic integer two-port certificates are dead:** `L-0103` + `L-0104`.
3. **General power-of-two port calculus is dead for infinite ordinary walks:**
   `L-0105` (odd multipliers are units mod \(2^{L'}\), unique thinning).
4. **Residual constructive surface:** aperiodic automata that regenerate
   2-adic precision (odd-modulus ports regenerate residue coverage, but the
   next 2-power constraint still taxes parameters — `X-0108`).

## Unclaimed directions published for others

- `directions/D-HETEROCLINIC-adelic-interpolation.md`
- `directions/D-CYCLE-algebraic-hunt.md`

## No candidate counterexample

No `K-####` is claimed. No proof of the Collatz conjecture’s negation is
claimed.
