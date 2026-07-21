# Packet: Affine ping-pong / Schottky + new paths

Agent: `grok45-01`  
Branch: `cursor/affine-pingpong-schottky-a643`  
PR: https://github.com/gfreund123/collatz/pull/11  
Date: 2026-07-21

## Paths

| Path | Status |
|---|---|
| Classical Schottky | Closed (`T-0103`) |
| Chronological tensor filled growth | Closed (`T-0105`) |
| 2-adic valuation fuel (deep-burn) | **Closed** (`L-0114`) |
| 2-adic fuel regeneration | Residual / stalled (`O-0108`, `C-0104`(3)) |
| Algebraic cycle hunt | Residual — empty through MITM \(L=37\) |
| **Odd-run highway ladder** | **OPEN** — spikes then return (`O-0111`) |
| **Mixed-modulus growth ladder** | **OPEN** — delayed return (`O-0112`) |
| **3-adic hybrid shadow** | **OPEN / active** — grow+preserve (`O-0110`) |

## Headline results this loop

- **`L-0114`** — deep 2-adic shadowing collapses under non-fixing excursions
- `O-0110` — 3-adic grow+preserve exists; iteration ≤+3 bits
- `O-0111` / `O-0112` — highway / mixed-modulus ladders: huge peaks, always return

## No K-candidate

Checked: mixed-modulus “survivors” at 400 steps all hit \(\{1,2\}\) by ~500.
