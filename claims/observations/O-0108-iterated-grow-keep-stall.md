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

## Interpretation

`O-0107`’s local grow+keep events are real but, in this alphabet and floor,
do **not** constitute a regenerative divergence engine. Next fuel-search
moves: enlarge the excursion alphabet, allow controlled depth dips with
scheduled repair, or change charts (\(-5\) vs \(-17\) vs mixed templates).
