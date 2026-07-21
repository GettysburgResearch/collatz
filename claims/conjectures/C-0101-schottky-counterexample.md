# C-0101 — Aperiodic integer Schottky certificate exists

Claim ID: `C-0101`  
Title: Existence of an aperiodic integer Schottky automaton certifying a divergent Collatz orbit  
Status: `IDEA` (severely restricted by `L-0105`–`L-0109`)  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0102`, `D-0103`, `L-0101`–`L-0109`  
Scope: speculative existence claim; most naive subclasses now refuted  
Related counterexample candidates: none yet

## Statement

There exists a finite certificate \(\mathcal{A}\) in some Schottky-like format
such that a single ordinary positive integer realizes an infinite
height-expanding aperiodic Collatz run.

## Present status after the continuation session

The following subclasses are **refuted or reduced**:

| Subclass | Verdict | Why |
|---|---|---|
| Compact positive IFS of supercritical inverses | Refuted | `L-0101` |
| Compact infinity-chart IFS | Refuted | `L-0102` |
| Periodic expanding block schedules | Refuted for \(\mathbb Z_{>0}\) | `L-0103`, `L-0107` |
| Pure power-of-two port calculus with growing towers | Unique 2-adic point; expanding periodic case negative | `L-0105`, `L-0107` |
| Odd-modulus “precision regeneration” | Does not regenerate free parameters | `L-0106` |
| Forward finite CRT automata mod \(2^A\) | No branching; deterministic functional graph | `L-0108` |
| Compact inverse IFS on \(\{g_0,g_1\}\) | Refuted | `L-0109` |

## Residual forms still open inside this packet

1. **Bridge to collision fibers:** Schottky-style free semigroups on
   multi-digit charts with growing geometry (`Q-0010` in the other packet).
2. **Non-classical domains:** unbounded cones, adelic/heteroclinic scaffolds
   (`directions/D-HETEROCLINIC-*`), or other state beyond affine \(\mathbb R\).
3. **Complementary-domain free-group ping-pong on \(\mathbb{RP}^1\)** with
   accelerated inverses — still only weakly probed (`X-0109`).

## Motivation

Keeps an explicit living conjecture so the packet does not pretend the
mission is closed, while advertising that classical Schottky is largely dead.

## Proof or construction

None.

## Suggested next attack

Stop searching classical IFS / finite dyadic CRT formats. Either:
- open a bridge issue with the collision-fiber growing-geometry program; or
- pursue the heteroclinic / cycle directions already handed off; or
- attempt a serious complementary-domain Möbius argument on \(\mathbb{RP}^1\).
