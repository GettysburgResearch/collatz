# Session report — affine ping-pong / Schottky certificates

```text
Agent: grok45-01
Issue: unavailable via GitHub Issues API (claim in directions/D-PINGPONG-schottky-certificates.md)
Branch: cursor/affine-pingpong-schottky-a643
PR: https://github.com/gfreund123/collatz/pull/11
Starting hypothesis: A finite Schottky system of accelerated affine Collatz
  blocks can certify a divergent ordinary orbit, bypassing carry-tile
  regeneration inside one collision fiber.
```

## Approaches attempted

1. Defined affine block data and real/integer Schottky certificate formats
   (`D-0101`, `D-0102`).
2. Searched for compact IFS ping-pong on \((0,\infty)\) with supercritical
   inverse branches (`X-0102`).
3. Retargeted to the chart \(t=1/x\) (`X-0104`).
4. Built integer port graphs with power-of-two and general moduli
   (`X-0103`, `X-0105`).
5. Built residue automata over supercritical blocks (`X-0106`).
6. Probed Syracuse valuation ping-pong (`X-0107`).
7. Analyzed odd-modulus “precision regeneration” after proving thinning
   (`X-0108`, `L-0105`).
8. Published unclaimed IDEA handoffs for the heteroclinic and algebraic-cycle
   directions under `directions/` (`M-0101`), because Issues could not be
   created with the available token.

## New results

### Proposed lemmas

- `L-0101` — no compact positive-interval Schottky for supercritical inverses.
- `L-0102` — same obstruction in the infinity chart for compact IFS format.
- `L-0103` — periodic block schedules yield periodic parity words.
- `L-0104` — exact precision drain for the expanding pair `1111010`/`1101110`.
- `L-0105` — **general** odd-multiplier thinning: every \(2^{L'}\) image-port
  constraint selects at most one parameter class mod \(2^{L'}\).

### Empirical observations

- `O-0101` — finite expanding shadows exist; mild greedy walks die by depth 20
  in the tested library; symbolic automaton cycles do not lift infinitely.

### Conjectures

- `C-0101` — an aperiodic integer Schottky automaton with precision
  regeneration still exists (open, speculative).
- `C-0102` — superseded by `L-0105` on the power-of-two port class.

## Candidate counterexamples

None.

## Failed approaches

- Compact real IFS ping-pong on positives or at infinity.
- Periodic two-port expanding certificates.
- Pure power-of-two port calculus for infinite ordinary walks.
- Mild supercritical greedy languages without repair/regeneration accounting.

## Potential errors

- `L-0101` / `L-0102` deliberately leave open classical complementary-domain
  free-group ping-pong on \(\mathbb{RP}^1\) (not the compact IFS format).
- `L-0105` does not kill odd-modulus destination ports; `X-0108` only sketches
  why naive regeneration may still be taxed at the next 2-power edge.
- Experiment bounds are finite; do not over-read as universal nonexistence of
  all automata.

## Files changed

- `PACKET.md`, `NEGATIVE_RESULTS_PINGPONG.md`
- `directions/**`
- `claims/definitions/D-0101*`, `D-0102*`
- `claims/lemmas/L-0101`…`L-0105`
- `claims/observations/O-0101*`
- `claims/conjectures/C-0101*`, `C-0102*`
- `claims/methodology/M-0101*`
- `experiments/X-0101`…`X-0108`
- `reports/grok45-01/2026-07-21-pingpong-schottky.md`

## Claims affected

Packet-local `*-01xx` only. Contested root ledgers intentionally untouched.

## Recommended next actions

1. Independent review of `L-0101`, `L-0102`, `L-0105`.
2. Attempt complementary-domain Möbius ping-pong on \(\mathbb{RP}^1\).
3. Design edges that buy more binary digits than `L-0105` taxes — or prove
   impossible (`C-0101` decision procedure).
4. Open GitHub Issues from `directions/D-HETEROCLINIC-*` and
   `directions/D-CYCLE-*` when permissions allow; claim/assign separately.
5. Optional bridge meeting with collision-fiber “growing geometry” (`Q-0010`)
   without merging ledgers prematurely.

## Organizational improvement ideas

- Adopt `M-0101` (`directions/`) whenever Issues are blocked.
- Reserve claim ID blocks per packet (`0100`, `9000`, …) in README later.
- Keep packet-local `PACKET.md` ledgers until an integrator merges.

```text
HANDOFF FROM: grok45-01
HANDOFF TO: any / verifier-01
CURRENT CLAIM OR CANDIDATE: L-0105 (obstruction) + C-0101 (residual hope)
BLOCKING STEP: either exhibit a precision-regenerating aperiodic automaton
  edge library, or prove C-0101 false
FILES TO READ: PACKET.md; claims/lemmas/L-0105-*.md; claims/conjectures/C-0101-*.md;
  experiments/X-0108-odd-modulus-regen/
FAILED ATTEMPTS: compact IFS (pos & infinity); periodic two-ports; pure 2-power ports
MOST PROMISING NEXT MOVE: quantify binary-digit budget vs L-0105 tax along
  mixed odd/even modulus walks; or complementary-domain RP^1 ping-pong
MAIN RISK: precision regeneration may be illusory once all edge types are taxed
POSSIBLE ORGANIZATIONAL IMPROVEMENT: paste directions/* into Issues ASAP
```
