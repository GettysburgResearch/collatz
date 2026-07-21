# O-0108 — Iterated grow+keep on \(-17\) stalls (no \(+10\)-bit escape)

Claim ID: `O-0108`  
Title: Local grow+keep moves do not iterate to large archimedean escapes  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: `O-0107`  
Scope: `X-0131`  
Related counterexample candidates: none

## Statement

Starting from \(120\) seeds in \(-17\) cylinders of depth \(m\in\{11,22,33\}\),
a beam search of depth \(\le30\) over an alphabet of short supercritical,
mild, and hold (`template`) moves that enforce a depth floor
\(v_2(n+17)\ge2\) achieved:

- **max bit-length gain \(+2\)**;
- **\(0\) escapes** with \(+10\) bits while holding the floor;
- all frontiers eventually stalled (no legal grow+keep/repair/hold extension).

## Follow-up scans

- `X-0132` scheduled dip/repair: max \(1\) epoch, max \(+2\) bits.
- `X-0133` mixed \(-5\)/\(-17\) dual-depth \(\max(v_2(n+5),v_2(n+17))\):
  max bit gain improved to \(+5\), still **\(0\)** \(+10\)-bit escapes.

## Interpretation

`O-0107`’s local grow+keep events are real but, in these alphabets and
floors, do **not** constitute a regenerative divergence engine. Next:
morphic / automatic large alphabets, or a lemma elevating the deep-burn
half of `C-0104`.
